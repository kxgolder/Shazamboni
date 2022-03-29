import json
import asyncio
import websockets
import motor


async def handler(websocket):
    print(f"Client connected: {websocket.remote_address}")
    await websocket.send("Connected to server.")
    while True:
        try:
            message = await websocket.recv()
            print(message)
        except websockets.ConnectionClosedOK:
            print("Socket closed.")
            break
        try:
            result = json.loads(message)
            print(f"degrees: {result['degrees']}, distance: {result['distance']}")
            motor.drive(result["degrees"], result["distance"])
        except:
            continue
        # print(message)


async def main():
    print("Initializing motor")
    motor.init()
    print("Initializing websocket server")
    async with websockets.serve(handler, "", 8001):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
