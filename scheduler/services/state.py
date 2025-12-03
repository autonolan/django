class InMemoryState:
    def __init__(self):
        self.worker_status = {}
        self.active_orders = []

state = InMemoryState()