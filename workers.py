# workers/worker_one.py
import asyncio
import websockets
import json
import sys


async def run_worker(worker_id: int) -> None:
    print(f"worker id: {worker_id}")
    try:
        async with websockets.connect(
            f"ws://127.0.0.1:8000/ws/worker/{worker_id}/"
        ) as ws:
            print(f"{worker_id}: connected")

            while True:
                message = json.loads(await ws.recv())

                # interpret command
                if message["command"] == "pick_from_shelf":
                    print(f"{worker_id} picking...")
                    await asyncio.sleep(2)  # simulate doing work

                    # send completion back
                    await ws.send(
                        json.dumps(
                            {
                                "event": "task_complete",
                                "order_id": message["order_id"],
                            }
                        )
                    )
    except Exception as e:
        print(f"Connection error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python worker_one.py <worker_id>")
        sys.exit(1)
    asyncio.run(run_worker(sys.argv[1]))
