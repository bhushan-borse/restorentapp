def success_response(data=None, success=True, message=None, code=200):
    data_dict = dict()
    
    data_dict["code"] = code
    data_dict["data"] = data
    data_dict["message"] = message
    data_dict["success"] = success
    
    return data_dict


def error_response(error=None, success=False, message=None, code=201):
    data_dict = dict()
    
    data_dict["code"] = code
    data_dict["error"] = error
    data_dict["message"] = message
    data_dict["success"] = success
    
    return data_dict