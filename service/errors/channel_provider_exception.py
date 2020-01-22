class ChannelProviderException(Exception):
    def __init__(self, message):
        super().__init__(message)

    @staticmethod
    def web_service_registration_failure(source):
        return ChannelProviderException("Web service '%s' has not been registered." % source)

    @staticmethod
    def chat_service_registration_failure(source):
        return ChannelProviderException("Chat service '%s' has not been registered." % source)

    @staticmethod
    def db_registration_failure(source):
        return ChannelProviderException("DB '%s' has not been registered." % source)
