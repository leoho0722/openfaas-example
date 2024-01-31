import asyncio
import json
import logging
import os

from nats.aio.client import Client as NatsClient

logging.basicConfig(level=logging.DEBUG)


def handle(req):
    logging.debug("Hello-3 Received a message")
    save_to_fs(req)
    NATS_URL = os.getenv("nats_url")

    loop = asyncio.new_event_loop()
    loop.run_until_complete(send_message(NATS_URL, req.encode(), loop))
    loop.close()

    return req


async def send_message(nats_url, message, loop):
    client = NatsClient()
    await client.connect(nats_url, loop=loop)
    await client.publish("hello-3", message)
    logging.debug(f"Hello-3 Sent a message: {message}")
    await client.close()


def save_to_fs(message):
    logging.debug(f"Hello-3 The message to save: {message}")
