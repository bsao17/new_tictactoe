class Players:
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
        print("Votre nom d'utilisateur actuel est: ")
        self.get_player_username()
        new_username = input("Choisissez votre nom d'utilisateur ! ")
        self.set_player_username(new_username)
        print(f"Votre nom d'utilisateur est désormais {new_username}")

    def __str__(self):
        return f"Classe qui détermine les caractéristiques de chaque joueur !"

    def __repr__(self):
        return f"MyClass(Players: {self.__class__}) for player:  {self.username} with label {self.label} !"
