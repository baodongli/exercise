import datetime
import time

def test_loop():
    loop_interval = datetime.timedelta(seconds=10)
    next_wakeup = datetime.datetime.now() + loop_interval
    iter = 1
    while True:
        print(f"{datetime.datetime.now()}: Processing")
        if iter == 1:
            time.sleep(51)
            iter = 2
        else:
            time.sleep(2)
                
        sleep_duration = next_wakeup - datetime.datetime.now()
        if sleep_duration.total_seconds() > 0:
            print(f"{datetime.datetime.now()}: Sleep {sleep_duration.total_seconds()}")
            time.sleep(sleep_duration.total_seconds())
        else:
            if -sleep_duration > loop_interval:
                next_wakeup += loop_interval
        next_wakeup += loop_interval

if __name__ == "__main__":
    test_loop()
