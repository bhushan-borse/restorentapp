from flask import jsonify


def create_response(data=None, success=True, message=None, code=200, error=None):
    data_dict = dict()

    data_dict["code"] = code
    data_dict["data"] = data
    data_dict["message"] = message
    data_dict["success"] = success
    data_dict["error"] = error

    return jsonify(data_dict)
