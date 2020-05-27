from contextlib import contextmanager, AbstractContextManager, ExitStack
class ResourceManager(AbstractContextManager):
    def __init__(self, acquire_resource, release_resource, check_resource_ok=None):
        self.acquire_resource = acquire_resource
        self.release_resource = release_resource
        if check_resource_ok is None:
            def check_resource_ok(resource):
                return False
        self.check_resource_ok = check_resource_ok
    @contextmanager
    def _cleanup_on_error(self):
        '''
        # The following block won't clean up the resource
        # ResourceManager's __exit__ won't be called due to the exception in the __enter__ method
        try:
            print("cleanup_on_error")
            yield
        finally:
            print("cleanup done")
        '''
            
        '''
        in the following logic, push adds the callback (which is the self's __exit__ method)
        in case of exception in self's __enter__, the exception will be caught by the context manager
        and thrown again, which causes the following exit_stack's __exit__ to be invoked. The statements after yield
        will not be executed. The exit_stack __exit__ method executes the self's __exit__ method that was pushed earlier. 

        in case of success, stack.pop_all() will transfer __exit__ to a new stack so that
        __exit__ will not be called
        '''
        with ExitStack() as stack:
            print("cleanup_on_error")
            stack.push(self)
            yield
            # The validation check passed and didn't raise an exception
            # Accordingly, we want to keep the resource, and pass it
            # back to our caller
            print("Before pop_all")
            stack.pop_all()
            print("After pop_all")
    def __enter__(self):
        resource = self.acquire_resource()
        with self._cleanup_on_error():
            print("Check Resource")
            if not self.check_resource_ok(resource):
                msg = "Failed validation for {!r}"
                raise RuntimeError(msg.format(resource))
        print("Got Resource")
        return resource
    def __exit__(self, *exc_details):
        # We don't need to duplicate any of our resource release logic
        self.release_resource()


def acquire():
    print("acquire")

def release():
    print("release")

def use():
    with ResourceManager(acquire, release) as rm:
        print("Use")

if __name__ == '__main__':
    use()
    
