import datetime
import time

def test_loop():
    loop_interval = datetime.timedelta(seconds=10)
    iter = 1
    while True:
        print(f"{datetime.datetime.now()}: Processing")
        start = datetime.datetime.now()
        if iter == 1:
            time.sleep(51)
            iter = 2
        else:
            time.sleep(2)
        finish = datetime.datetime.now()
                
        sleep_duration = loop_interval - (finish - start)
        if sleep_duration.total_seconds() > 0:
            print(f"{datetime.datetime.now()}: Sleep {sleep_duration.total_seconds()}")
            time.sleep(sleep_duration.total_seconds())

if __name__ == "__main__":
    test_loop()
