from django.shortcuts import render, redirect
from django.http import JsonResponse
from .firebase_config import auth, firebase
from django.contrib import messages
import json
import random
from datetime import datetime

def dashboard_view(request):
    if 'uid' not in request.session:
        return redirect('login')
    
    try:
        # Verify user is authenticated
        user_info = auth.get_account_info(request.session['uid'])
        request.session['user_id'] = user_info['users'][0]['localId']
        return render(request, "dashboard.html", {'uid': request.session['uid']})
    except Exception as e:
        messages.error(request, "Session expired. Please login again.")
        return redirect('login')

def save_test_data(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
    try:
        data = json.loads(request.body)
        user_id = data.get('user_id')  # Should be sent from IoT device
        
        # Save to Firebase
        db = firebase.database()
        test_data = {
            'ph': data.get('ph'),
            'temperature': data.get('temperature'),
            'tds': data.get('tds'),
            'turbidity': data.get('turbidity'),
            'chemicals': data.get('chemicals', []),
            'timestamp': {'.sv': 'timestamp'}  # Firebase server timestamp
        }
        
        db.child('tests').child(user_id).push(test_data)
        return JsonResponse({'success': True})
    
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def get_test_history(request):
    if 'uid' not in request.session:
        return JsonResponse({'error': 'Unauthorized'}, status=401)
    
    try:
        db = firebase.database()
        user_id = request.session['user_id']
        tests = db.child('tests').child(user_id).get().val()
        return JsonResponse({'tests': tests or {}})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def generate_dummy_test(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
    try:
        chemicals = [
            {"name": "Lead", "safe": 0.015},
            {"name": "Copper", "safe": 1.3},
            {"name": "Nitrate", "safe": 10},
            {"name": "Arsenic", "safe": 0.01},
            {"name": "Mercury", "safe": 0.002}
        ]
        
        chemical_data = [{
            "name": chem["name"],
            "present": random.uniform(0, chem["safe"] * 1.5),
            "safe": chem["safe"]
        } for chem in chemicals]
        
        test_data = {
            "ph": random.uniform(6, 10),
            "temperature": random.uniform(10, 40),
            "tds": random.uniform(0, 1200),
            "turbidity": random.uniform(0, 5),
            "chemicals": chemical_data,
            "timestamp": datetime.now().isoformat()
        }
        
        # Save to Firebase if you want
        if 'uid' in request.session:
            db = firebase.database()
            db.child('tests').child(request.session['user_id']).push(test_data)
        
        return JsonResponse(test_data)
    
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)