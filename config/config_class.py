class ViewConfig(object):
    def __init__(
            self, model=None,
            get_before_db_call=None, get_after_before_db_call=None,
            put_before_db_call=None, put_after_before_db_call=None,
            post_before_db_call=None, post_after_before_db_call=None,
            delete_before_db_call=None, delete_after_before_db_call=None,
            is_custom_query=False, raw_query=None
    ):
        # Model is the table name
        self.model = model

        # if there is a extra process want to do after or before db-call then give the function name.
        # based on given conf it will invoke the given fun
        self.get_before_db_call = get_before_db_call
        self.get_after_before_db_call = get_after_before_db_call

        self.put_before_db_call = put_before_db_call
        self.put_after_before_db_call = put_after_before_db_call

        self.post_before_db_call = post_before_db_call
        self.post_after_before_db_call = post_after_before_db_call

        self.delete_before_db_call = delete_before_db_call
        self.delete_after_before_db_call = delete_after_before_db_call

        # if you want to create the custom query-creator
        self.is_custom_query = is_custom_query

        # Instead of ORM query you want to hit your raw or fully customs query and get result
        self.raw_query = raw_query


class RouteConfig(object):
    def __init__(
            self, model=None, url: str = None, endpoint: str = None, methods: list = None,
            view_class=None, view_fun=None, view_config: ViewConfig = None
    ):
        self.model = model
        if not url:
            raise Exception("[ERROR ROUTE CONFIG] Please Provide the url!..")
        self.url = url

        if not endpoint:
            endpoint = url.replace("/", "_")
        self.endpoint = endpoint

        if not methods:
            raise Exception("[ERROR ROUTE CONFIG] Please Provide the methods!..")
        self.methods = methods

        if not view_fun and not view_class:
            raise Exception("[ERROR ROUTE CONFIG] Please Provide the view!..")
        self.view_fun = view_fun
        self.view_class = view_class

        self.view_config: ViewConfig = view_config
