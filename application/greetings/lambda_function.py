from core.GetTime.time import TimeUtil

def lambda_handler(event, context):
    time_util = TimeUtil()

    now = time_util.get_time()
    current_time = now.strftime("%H:%M:%S")
    return {
        "statusCode": 200,
        "body": {
            "message": "Hello Visitor!!!",
            "time": "You visited us at {0}".format(current_time)
        }
    }