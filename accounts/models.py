from datetime import datetime
from .firebase_config import firebase

db = firebase.database()

class WaterTest:
    def __init__(self, user_id, ph, temperature, tds, turbidity, chemicals):
        self.user_id = user_id
        self.ph = ph
        self.temperature = temperature
        self.tds = tds
        self.turbidity = turbidity
        self.chemicals = chemicals
        self.timestamp = datetime.now().isoformat()

    def save(self):
        data = {
            'ph': self.ph,
            'temperature': self.temperature,
            'tds': self.tds,
            'turbidity': self.turbidity,
            'chemicals': self.chemicals,
            'timestamp': self.timestamp
        }
        return db.child('tests').child(self.user_id).push(data)

    @staticmethod
    def get_user_tests(user_id):
        tests = db.child('tests').child(user_id).get()
        return tests.val() if tests.val() else {}

    @staticmethod
    def get_latest_test(user_id):
        tests = db.child('tests').child(user_id).order_by_child('timestamp').limit_to_last(1).get()
        return next(iter(tests.val().values())) if tests.val() else None