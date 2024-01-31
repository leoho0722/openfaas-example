import logging

logging.basicConfig(level=logging.DEBUG)


def handle(req):
    logging.debug("Hello-2 Received a message")

    return req
