import functools
import requests
import time
def retry(max_retries=20, interval=1, exc=Exception, exc_handler=lambda exc: True):
    def wrapper(f):
        @functools.wraps(f)
        def wrapped(*args, **kwargs):
            retries = max_retries
            while retries > 0:
                try:
                    result = f(*args, **kwargs)
                    return result
                except exc as exp:
                    if exc_handler(exp):
                        time.sleep(interval)
                        retries -= 1
                        print("Retry ", retries)
                    else:
                        raise
        return wrapped
    print(max_retries, " ", interval)
    return wrapper
              
              
@retry(exc_handler=lambda exc: str(exc).startswith(500), max_retries=20)
def get(a, b, c):
    raise requests.HTTPError("500 abc")
    
                    
            
class onefs:
    @retry(exc=requests.HTTPError, exc_handler=lambda exc: str(exc).startswith('500'), interval=0.05)
    def get_export(self, id):
        self.display(id)
        raise requests.HTTPError("500 abc")
    def display(self, *args):
        print(*args)
    @retry()
    def enable_guest(self, id):
        self.display(id)
        raise requests.HTTPError("abc")
        
