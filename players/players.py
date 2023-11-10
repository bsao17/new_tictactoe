class Players:
    def __init__(self, username, label):
        self.username = username
        self.label = label

    def get_player_username(self):
        """
        Retrieves the username of the player.

        Returns:
            None
        """
        print(self.username)

    def set_player_username(self, username):
        """
        Set the username of the player.

        Args:
            username (str): The new username for the player.

        Returns:
            None
        """
        self.username = username

    def get_player_label(self):
        """
        Get the player label.

        This method returns the player's label.

        Returns:
            None
        """
        print(self.label)

    def set_player_label(self, new_label):
        """
        Set the label of the player.

        Parameters:
            new_label (str): The new label for the player.

        Returns:
            None
        """
        self.label = new_label

    def update_profile(self):
        # print("Choississez votre nom d'utilisateur et le symbole qui sera afficher dans vos cases.")
        # print("Votre nom d'utilisateur actuel est: ")
        # self.get_player_username()
        # new_username = input("Choisissez votre nom d'utilisateur ! ")
        # self.set_player_username(new_username)
        # print(f"Votre nom d'utilisateur est désormais {new_username}")
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
