from datetime import datetime

class TimeUtil:
    def __init__(self) -> None:
        pass

    def get_time():
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return {
            "statusCode": 200,
            "body": {
                "time": current_time
            }
        }