def handle(req):
    """handle a request to the function
    Args:
        req (flask.request): request body
    """

    def response(status, body):
        """create an HTTP response
        Args:
            status (int): HTTP status code
            body (str): HTTP response body
        """

        return {
            "status": status,
            "body": body,
            "headers": {
                "Content-Type": "application/json"
            }
        }

    body = req.get_json()
    message = body.get("message", "Hello, World!")

    if req.method == 'POST':
        return response(200, message)
    else:
        return response(405, "Method not allowed")
