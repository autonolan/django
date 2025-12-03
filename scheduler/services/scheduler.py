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
