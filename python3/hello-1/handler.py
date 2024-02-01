import logging
import os
import threading
from enum import Enum, unique
from time import sleep

import requests

logging.basicConfig(level=logging.DEBUG)


def handle(req):
    """Handle a request to the function.

    Args:
        req (flask.request): Request body
    """

    def response(status, body):
        """Create an HTTP response.

        Args:
            status (int): HTTP status code
            body (any): HTTP response body
        """

        return {
            "status": status,
            "body": body,
        }

    def current_task_finish_and_start_next_task(body, next_stage):
        """Finish the current task and start the next one.

        Args:
            body (dict): Request body
            next_stage (str): Next pipeline stage name
        """

        def trigger():
            _ = requests.post(
                f"http://gateway.openfaas:8080/function/{next_stage}",
                json=body
            )

            logging.info(f"Trigger function {next_stage}\n")

        threading.Thread(target=trigger).start()

    logging.info("Function hello-1 running...\n")

    if req.method == 'POST':
        next_stage = os.getenv("next_stage")
        next_is_valid = is_valid_stage(next_stage)

        if not next_is_valid:
            return response(400, "Invalid next stage name")

        sleep(2)  # Simulate a long-running task

        req_body = {
            "stage": {
                "current": {
                    "status": "finished",
                    "name": "hello-1"
                },
                "next": {
                    "status": "ready",
                    "name": next_stage
                }
            },
        }

        logging.info(f"Function hello-1 will trigger function {next_stage}\n")

        current_task_finish_and_start_next_task(req_body, next_stage)

        logging.info("Function hello-1 finished\n")

        return response(200, req_body)
    else:
        return response(405, "Method not allowed")


@unique
class PipelineStage(Enum):
    HELLO_1 = "hello-1"
    HELLO_2 = "hello-2"
    HELLO_3 = "hello-3"
    HELLO_4 = "hello-4"


def get_stage_name(stage):
    """Get the name of a pipeline stage.

    Args:
        stage (str): Pipeline stage name
    """

    return PipelineStage(stage).value


def is_valid_stage(stage):
    """Check if a pipeline stage is valid.

    Args:
        stage (str): Pipeline stage name
    """

    try:
        get_stage_name(stage)
        return True
    except ValueError:
        return False
