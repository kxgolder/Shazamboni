import json
import asyncio
import websockets
import motor


async def handler(websocket):
    while True:
        try:
            message = await websocket.recv()
        except websockets.ConnectionClosedOK:
            break
        try:
            result = json.loads(message)
            print(f"degrees: {result['degrees']}, distance: {result['distance']}")
            motor.drive(result["degrees"], result["distance"])
        except:
            continue
        # print(message)

async def main():
    async with websockets.serve(handler, "", 8001):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
