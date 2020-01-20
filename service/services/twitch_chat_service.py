from service.services.chat_service_base import ChatServiceBase


class TwitchChatService(ChatServiceBase):
    def get_source(self):
        return "Twitch"

    def start_collecting_chat(self, channel_name):
        pass

    def stop_collecting_chat(self, channel_name):
        pass