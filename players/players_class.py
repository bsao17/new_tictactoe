class Players_class:
    def __init__(self, username, label):
        self.username = username
        self.label = label

    def get_player_username(self):
        print(self.username)

    def set_player_username(self, username):
        self.username = username

    def get_player_label(self):
        print(self.label)

    def set_player_label(self, new_label):
        self.label = new_label

    def update_profile(self):
        print("Choississez votre nom d'utilisateur et le symbole qui sera afficher dans vos cases.")
        print()
        self.get_player_username()
        self.set_player_username()
