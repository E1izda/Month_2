from datetime import datetime as dt

def checktime(func):
    def wrapper(*args, **kwargs):
        time_now = dt.now()
        formatted_time = time_now.strftime("%H:%M:%S %d/%m/%Y")
        print(f"функция была вызвана в {formatted_time}")
        return func(*args, **kwargs)
    return wrapper

@checktime
def hello_world():
    print("hello world")

hello_world()