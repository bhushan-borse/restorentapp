import importlib
def register_route(app=None, packages=[]):
    
    if not packages:
        return None
    
    if not app:
        return None
    
    def reg_route(view_class=None, pk=None, endpoint=None, pk_type=None, url=None,):
        view_func = view_class.as_view(endpoint)
        app.add_url_rule(url, defaults={pk: None},
                        view_func=view_func, methods=['GET',])
        app.add_url_rule(url, view_func=view_func, methods=['POST',])
        app.add_url_rule(f'{url}<{pk_type}:{pk}>', view_func=view_func,
                        methods=['GET', 'PUT', 'DELETE'])
    
    
    for package in packages:
        try:
            module = importlib.import_module(f"{package}.views")
            view_list = module.get_api_view()
            for view_obj in view_list:
                reg_route(**view_obj)
        except Exception as err:
            print("[ERROR] Route Registration:- ", err)