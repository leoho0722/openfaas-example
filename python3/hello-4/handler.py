import json
import logging
import os


def handle(req):
    logging.debug("Hello-4 Received a message")
    save_to_fs(req)
    return req


def save_to_fs(message):
    logging.debug(f"Hello-4 The message to save: {message}")
