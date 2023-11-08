class Players_class:
    def __init__(self, username, label):
        self.username = username
        self.label = label

    def get_player_username(self):
        print(self.username)

    def set_player_username(self, username):
        self.username = username
