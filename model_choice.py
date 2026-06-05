# model_choice.py

class Choice:

    def __init__(
        self,
        title,
        fatigue_change=0,
        belonging_change=0,
        selfworth_change=0,
        tension_change=0,
        next_id=None,
    ):

        self.title = title

        self.fatigue_change = fatigue_change
        self.belonging_change = belonging_change
        self.selfworth_change = selfworth_change
        self.tension_change = tension_change

        self.next_id = next_id