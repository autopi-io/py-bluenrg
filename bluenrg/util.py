import logging
import threading

from timeit import default_timer as timer


log = logging.getLogger(__name__)


def inheritors(cls, recursive=False):
    ret = set()

    work = [cls]
    while work:
        parent = work.pop()
        for child in parent.__subclasses__():
            if child not in ret:
                ret.add(child)

                if recursive:
                    work.append(child)

    return ret


def cached_inheritors(cls, func, **kwargs):
    attr = "{:}.{:}".format(cls.__name__, "_cached_inheritors")

    if not hasattr(cls, attr):
        setattr(cls, attr, {func(c): c for c in inheritors(cls, **kwargs)})

    return getattr(cls, attr)


def set_attr_default(obj, key, default):
    if not hasattr(obj, key):
        setattr(obj, key, default)

    return getattr(obj, key)


class WorkerThread(threading.Thread):

    def __init__(self, name=None, target=None, interval=0.1):
        if target == None:
            raise ValueError("Target function must be defined")

        super(WorkerThread, self).__init__()

        # Generate name if none specified
        if name == None:
            name = "{:s}_{{id}}".format(target.__name__)

        # Standard attributes
        self.name = name.format(id=id(self))
        self.daemon = True

        # Additional attributes
        self.target = target
        self.interval = interval
        self.terminate = threading.Event()

    def run(self):
        try:
            while not self.terminate.is_set():
                self.target()

        except Exception:
            log.exception("Fatal exception in worker thread '%s'", self.name)
        finally:
            log.info("Worker thread '%s' terminated", self.name)

    def kill(self):

        if log.isEnabledFor(logging.DEBUG):
            log.debug("Killing worker thread '%s'...", self.name)

        # Set terminate flag
        self.terminate.set()

        # Wait for thread to terminate
        self.join()

    def wait(self):
        return self.terminate.wait(self.interval)


class ResultMatcher(object):

    def __init__(self):
        self._event = threading.Event()
        self._func = None
        self._result = None

    def setup(self, match_func):
        self._func = match_func
        self._result = None
        self._event.clear()

    def wait(self, timeout):
        start = timer()

        self._event.wait(timeout)

        if self._result != None:
            log.info("Waited {:} second(s) for result {:}".format(timer() - start, self._result))

        return self._result 

    def match(self, result):
        if self._event.is_set():
            if log.isEnabledFor(logging.DEBUG):
                log.debug("Already matched - skipping result {:}".format(result))

            return False

        if not self._func:
            if log.isEnabledFor(logging.DEBUG):
                log.debug("No match function - skipping result {:}".format(result))

            return False

        if log.isEnabledFor(logging.DEBUG):
            log.debug("Matching result {:}".format(result))

        if self._func(result):
            self._result = result
            self._event.set()

            return True

        if log.isEnabledFor(logging.DEBUG):
            log.debug("No match for result {:}".format(result))

        return False

    def fail(self, result):
        if not self._event.is_set():
            self._result = result
            self._event.set()