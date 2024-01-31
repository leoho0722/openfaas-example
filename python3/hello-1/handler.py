from enum import Enum, unique
import requests


def handle(req):
    """handle a request to the function
    Args:
        req (flask.request): request body
    """

    def response(status, body):
        """create an HTTP response
        Args:
            status (int): HTTP status code
            body (any): HTTP response body
        """

        return {
            "status": status,
            "body": body,
        }

    if req.method == 'POST':
        body = req.get_json()
        current_stage = body.get("stage").get("current")
        next_stage = body.get("stage").get("next")

        current_is_valid = is_valid_stage(current_stage)
        next_is_valid = is_valid_stage(next_stage)

        if not current_is_valid or not next_is_valid:
            return response(400, "Invalid stage name")

        req_body = {
            "stage": {
                "current": {
                    "status": "finsihed",
                    "name": get_stage_name(current_stage)
                },
                "next": {
                    "status": "ready",
                    "name": get_stage_name(next_stage)
                }
            },
        }
        res = requests.post(
            f"http://127.0.0.1:8080/function/{get_stage_name(next_stage)}",
            json=req_body
        )

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
    """get the name of a pipeline stage
    Args:
        stage (str): pipeline stage name
    """

    return PipelineStage(stage).value


def is_valid_stage(stage):
    """check if a pipeline stage is valid
    Args:
        stage (str): pipeline stage name
    """

    try:
        get_stage_name(stage)
        return True
    except ValueError:
        return False
