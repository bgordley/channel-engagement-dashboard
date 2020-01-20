class WebServiceException(Exception):
    def __init__(self, status_code, url):
        # Call the base class constructor with the parameters it needs
        super().__init__("Web service call failed with status '%s': '%s'" % (status_code, url))
