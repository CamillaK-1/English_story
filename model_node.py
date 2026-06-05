# model_node.py

class Node:

    def __init__(
        self,
        id,
        title,
        description,
        music_track=None,
        background_image=None,
    ):

        self.id = id
        self.title = title
        self.description = description

        self.choices = []

        self.music_track = music_track
        self.background_image = background_image

    def add_choice(self, choice):

        self.choices.append(choice)

    def find(self, id, seen=None):

        if self.id == id:
            return self

        return None

    def __repr__(self):

        return f"Node({self.id})"