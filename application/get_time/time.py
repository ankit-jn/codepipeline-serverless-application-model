from datetime import datetime

def get_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return {
        "statusCode": 200,
        "body": {
            "time": current_time
        }
    }