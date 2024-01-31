import logging
import os

from enum import Enum, unique
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

    logging.debug("function hello-3 running...\n")

    if req.method == 'POST':
        next_stage = os.getenv("next_stage")
        next_is_valid = is_valid_stage(next_stage)

        if not next_is_valid:
            return response(400, "Invalid next stage name")

        gateway_url = os.getenv("gateway")

        req_body = {
            "stage": {
                "current": {
                    "status": "finished",
                    "name": "hello-3"
                },
                "next": {
                    "status": "ready",
                    "name": next_stage
                }
            },
        }
        _ = requests.post(
            f"{gateway_url}/function/{next_stage}",
            json=req_body
        )

        logging.debug("function hello-3 finished\n")

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
