class Players:
    def __init__(self, *args):
        self.username = args[0]
        self.label = args[1]
        self.grid = [[0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]]

    def get_player_username(self):
        """
        Retrieves the username of the player.
        """
        print(self.username)

    def set_player_username(self, username):
        """
        Set the username of the player.
        """
        self.username = username

    def get_player_label(self):
        """
        Get the player label.
        """
        print(self.label)

    def set_player_label(self, new_label):
        """
        Set the label of the player.
        """
        self.label = new_label

    def update_profile(self, label, username):
        """
        Update the profile of the player.
        """
        self.set_player_label(label)
        self.set_player_username(username)

    def chatgpt_move(self):
        pass

    def __str__(self):
        """
        Returns a string representation of the object.

        :return: A string representing the characteristics of each player.
        :rtype: str
        """
        return f"Classe qui détermine les caractéristiques de chaque joueur !"

    def __repr__(self):
        """
        Return a string representation of the object.

        Returns:
            str: The string representation of the object.
        """
        return f"MyClass(Players: {self.__class__}) for player:  {self.username} with label {self.label} !"
