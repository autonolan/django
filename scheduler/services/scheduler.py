import json
from channels.db import database_sync_to_async
from ..models import Order, Workstation, ActivityLog
from .state import state

class Scheduler:
    async def log(self, message):
        await database_sync_to_async(ActivityLog.objects.create)(message=message)
    
    async def register_worker(self, id, ws):
        state.worker_status[id] = {"busy": False, "ws": ws}
        await self.try_assign_work()
    
    async def unregister_worker(self, id):
        state.worker_Status.pop(id, None)
    
    async def worker_finished(self, id):
        state.worker_status[id]["busy"] = False
        await self.try_assign_work()
    
    async def try_assign_work(self):
        idle_workers = [w for w, info in state.worker_status.items() if not info["busy"]]
        if not idle_workers:
            return
        
        order = await database_sync_to_async(lambda: Order.objects.filter(status='pending').exclude(id__in=state.active_orders).first())()
        if not order:
            return
        id = idle_workers[0]
        ws = state.worker_status[id]["ws"]
        state.active_orders.append(order.id)
        state.worker_status[id]["busy"] = True
        await ws.send(json.dumps({
            "command": "pick_from_shelf",
            "order_id": order.id,
            "location": "ShelfArea1"
        }))

        await self.log(f"Assigned order {order.id} to worker {id}.")
    
    @staticmethod
    def _assign_order(order):
        order.status =  'picking'
        order.save()
    
scheduler = Scheduler()