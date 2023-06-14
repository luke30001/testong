from telethon import TelegramClient

client = TelegramClient("server", 1286167, "a41691f6c0b646c222b9c5559f0ac116",use_ipv6=True)

async def main():
    # Now you can use all client methods listed below, like for example...
    await client.send_message('me', 'Hello to myself!')

with client:
    client.loop.run_until_complete(main())
