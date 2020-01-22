class WebServiceException(Exception):
    def __init__(self, status_code, url):
        super().__init__("Web service call failed with status '%s': '%s'" % (status_code, url))
