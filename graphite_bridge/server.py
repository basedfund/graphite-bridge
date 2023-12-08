import requests

class GraphiteServer:
    def __init__(self, serverUrl, client_id):
        self.__serverUrl = serverUrl
        self.__client_id = client_id

    def get_client_config(self):
        response = requests.get(self.__serverUrl + "/client/config?clientId=" + self.__client_id)
        return response
    
    def get_strategy_configs(self, strategy_ids):
        return []
    
    def upload_state(self, strategy_id, state):
        response = requests.post(self.__serverUrl + "/client/upload?clientId=" + self.__client_id)
        return 0
    
