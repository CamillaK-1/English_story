# model_story.py

from model_node import Node
from model_choice import Choice


class Story:

    def __init__(
        self,
        title,
        first_id,
        first_title,
        first_description,
    ):

        self.title = title

        self.nodes = {}

        first_node = Node(
            id=first_id,
            title=first_title,
            description=first_description
        )

        self.first_node = first_node

        self.nodes[first_id] = first_node

    def add_node(
        self,
        node_id,
        title,
        description,
    ):

        self.nodes[node_id] = Node(
            id=node_id,
            title=title,
            description=description,
        )

    def add_choice(
        self,
        parent_id,
        title,
        next_id,

        fatigue_change=0,
        belonging_change=0,
        selfworth_change=0,
        tension_change=0,
    ):

        choice = Choice(
            title=title,

            fatigue_change=fatigue_change,
            belonging_change=belonging_change,
            selfworth_change=selfworth_change,
            tension_change=tension_change,

            next_id=next_id,
        )

        self.nodes[parent_id].add_choice(choice)

    def find(self, node_id):

        return self.nodes.get(node_id)