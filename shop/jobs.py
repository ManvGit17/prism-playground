"""Background jobs."""


class Worker:
    def run(self):
        return "done"


def dispatch(worker):
    return worker.run()


def run_all(workers):
    return [dispatch(w) for w in workers]
