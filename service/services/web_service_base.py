class WebServiceBase(object):
    def get_auth_token(self):
        raise NotImplementedError("Method implementation required.")

    def get_channel(self, channel_name):
        raise NotImplementedError("Method implementation required.")

    def get_stream(self, channel_name):
        raise NotImplementedError("Method implementation required.")

    def get_game(self, game_id):
        raise NotImplementedError("Method implementation required.")

    def get_source(self):
        raise NotImplementedError("Method implementation required.")
