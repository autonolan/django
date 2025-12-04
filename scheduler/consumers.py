import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .services.scheduler import scheduler


class WorkerConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.id = self.scope["url_route"]["kwargs"]["id"]
        await self.accept()
        await scheduler.register_worker(self.id, self)
        await scheduler.log(f"{self.id} connected.")

    async def disconnect(self, code):
        print(f"Worker {self.id} disconnected with code {code}")
        await scheduler.unregister_worker(self.id)

    async def receive(self, text_data):
        data = json.loads(text_data)
        print(f"Received from {self.id}: {data}")
        if data.get("event") == "task_complete":
            await scheduler.worker_finished(self.id)
