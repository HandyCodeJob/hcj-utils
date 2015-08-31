import time

def timeit(method):
    """
    Quick and simple timing decorator
    Credit: https://www.andreas-jung.com
    """
    def timed(*args, **kwargs):
        time_start = time.time()
        result = method(*args, **kwargs)
        time_end = time.time()
        print("{name}({args}, {kwargs}) "
              "in {time} sec".format(name=method.__name__,
                                     args=args,
                                     kwargs=kwargs,
                                     time=time_end - time_start))
        return result
    return timed
