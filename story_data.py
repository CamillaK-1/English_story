from model_story import Story

main_story = Story(
    title="Invisible Weight",

    first_id="cricket",
    first_title="Cricket Club",

    first_description="""
And when the cricket club coach says, you girls are only here to date the boys, you look around and hope that by sitting in silence no one will ask why you are not laughing. You wonder whether the boys hear the same thing or whether this moment is reserved only for you.
"""
)

# -----------------------

# -------------------------
# CHAPTER 1: CRICKET CLUB
# -------------------------

main_story.add_choice(
    "cricket",
    "You stay silent and look down.",
    "socks",

    fatigue_change=2,
    selfworth_change=-2,
    belonging_change= -1,
    tension_change= -1
)

main_story.add_choice(
    "cricket",
    "You force a small laugh to blend in.",
    "socks",

    fatigue_change= 1,
    belonging_change= 2,
    selfworth_change= -1,
    tension_change= -2
)

main_story.add_choice(
    "cricket",
    "You speak up quietly: “That’s not why I’m here.”",
    "socks",

    fatigue_change= 1,
    selfworth_change= 2, 
    belonging_change= -2, 
    tension_change= -2
)

# -------------------------
# CHAPTER 2: SOCKS
# -------------------------

main_story.add_node(
    "socks",
    "School Socks",
    """
You take yourself to school and sit through history, then math, then engish, and a man you’ve never seen before calls you out of the classroom. you need to change your socks, he says.why? Your ankles might be distracting. You can’t help but giggle, a nervous sound that escapes before you can stop it. He doesn’t even smile. And you realise that something, someone, made him think this is okay.
"""
)

main_story.add_choice(
    "socks",
    "You stay silent and go change your socks.",
    "bill",

    fatigue_change= 2, 
    selfworth_change= -2, 
    belonging_change= -1, 
    tension_change= -1
)

main_story.add_choice(
    "socks",
    "You ask, “Are you actually serious?”",
    "bill",

    fatigue_change= 1,
    selfworth_change= 2, 
    belonging_change= -1, 
    tension_change= 2
)

main_story.add_choice(
    "socks",
    "You refuse to take off your socks and storm back to class",
    "bill",

    fatigue_change= 1, 
    selfworth_change= 3, 
    belonging_change= -2, 
    tension_change= 2
)

# -------------------------
# CHAPTER 3: BILL
# -------------------------

main_story.add_node(
    "bill",
    "The Bill",
    """
You wave to the waiter and a man comes over. You tell him you want to pay. He returns and presents the bill to your husband sitting across from you. And although your husband passes the bill to you, you begin to think, maybe erroneously, that there was nothing wrong and you are just overthinking. Then the voice in your head silently tells you to take your foot off your throat because its just a dinner and you don't want to bring any more trouble.
"""
)

main_story.add_choice(
    "bill",
    "You say nothing and pay quietly.",
    "loss",

    fatigue_change= 2, 
    selfworth_change= -2, 
    belonging_change= -1, 
    tension_change= -1
)

main_story.add_choice(
    "bill",
    "You point out, “I asked for the bill. Why did you give it to my dad?”",
    "loss",

    fatigue_change= 1, 
    selfworth_change= 2, 
    belonging_change= -2, 
    tension_change= 2
)

main_story.add_choice(
    "bill",
    "You laugh and shake it off but do not leave the waiter a tip",
    "loss",

    fatigue_change= 1, 
    belonging_change= 2, 
    selfworth_change= -1, 
    tension_change= -2
)

# -------------------------
# CHAPTER 4: LOSS
# -------------------------

main_story.add_node(
    "loss",
    "Loss",
    """
When your stepfather suddenly passes away, your neighbor comes over with some ribs and asks your mom if your family has to move to a neighborhood a little less fancy. You push past your mom and tell your neighbor that your family is perfectly capable of carrying on without him. He stutters. I was just trying to take care of you all. The rain seems to blow in the house and wets your shirt until you realise it wasn't rain afterall. The body keeps score of what the mind forgets.
"""
)

main_story.add_choice(
    "loss",
    "You push back again ‘we don’t need your misogynistic thoughts, thank you very much’",
    "colleague",

    fatigue_change= 1, 
    selfworth_change= 2, 
    belonging_change= 1, 
    tension_change= 2
)

main_story.add_choice(
    "loss",
    "You stay quiet behind your mom again",
    "colleague",

    fatigue_change= 1, 
    selfworth_change= -2, 
    belonging_change= -2, 
    tension_change= -1
)

main_story.add_choice(
    "loss",
    "You apologize and thank him for the food",
    "colleague",

    fatigue_change= 1, 
    selfworth_change= -2, 
    belonging_change= 2, 
    tension_change= -2
)

# -------------------------
# CHAPTER 5: COLLEAGUE
# -------------------------

main_story.add_node(
    "colleague",
    "Colleague",
    """
Your younger male colleague says that women lose all value past the age of 25. A woman over 35 is like a second hand good. A divorced woman is like a used car; too stubborn, too much mileage. What did you just say? How have you just said that? What is wrong with you? The words stink like rotten egg over your creased shirt. You feel the slow drip of being measured and found wanting before you have even begun.
"""
)

main_story.add_choice(
    "colleague",
    "You stay silent and say nothing.",
    "drive",

    fatigue_change= 1, 
    selfworth_change= -2, 
    belonging_change= -1, 
    tension_change= -1
)

main_story.add_choice(
    "colleague",
    "You respond, “That’s a disgusting thing to say. Who are you to measure women?”",
    "drive",

    fatigue_change= 1, 
    selfworth_change= 2, 
    belonging_change= -2, 
    tension_change= 2
)

main_story.add_choice(
    "colleague",
    "You try to laugh it off and change the subject.",
    "drive",

    fatigue_change= 1, 
    belonging_change= 1, 
    selfworth_change= -1, 
    tension_change= -2
)

# -------------------------
# CHAPTER 6: DRIVE
# -------------------------

main_story.add_node(
    "drive",
    "Drive Through",
    """
In line at the drive through it’s finally your turn. You roll down your window and are just about to order when the old man opens his damn mouth first.

Isn't this car too big for you?

You stare at him blankly.

I didn’t mean to say that.

The transaction goes swiftly after that.
"""
)

main_story.add_choice(
    "drive",
    "You say nothing and don't order, driving away quickly",
    "professor",

    fatigue_change= 2, 
    selfworth_change= -2, 
    belonging_change= -1, 
    tension_change= -1
)

main_story.add_choice(
    "drive",
    "You reply, “Excuse me?”",
    "professor",

    fatigue_change= 1, 
    selfworth_change= 2, 
    belonging_change= -2, 
    tension_change= 2
)

main_story.add_choice(
    "drive",
    "You force a small smile and joke “of course I can “",
    "professor",

    fatigue_change= 1, 
    belonging_change= 2, 
    selfworth_change= -1, 
    tension_change= -2
)

# -------------------------
# CHAPTER 7: PROFESSOR
# -------------------------

main_story.add_node(
    "professor",
    "Professor",
    """
You eat quietly at the corner of a meeting room, and a man, a ‘professor’, wanting to make conversation, nursing something, takes out his phone to show you a picture of his wife. You say that she is beautiful. She is, he says, a beautiful and intelligent woman, and of course, merely a researcher. Unlike him.
"""
)

main_story.add_choice(
    "professor",
    "You stay silent and nod.",
    "counselor",

    fatigue_change= 2, 
    selfworth_change= -2, 
    belonging_change= -1, 
    tension_change= -1
)

main_story.add_choice(
    "professor",
    "You say, “Of course?”",
    "counselor",

    fatigue_change= 1, 
    selfworth_change= 2, 
    belonging_change= -2, 
    tension_change= 2
)

main_story.add_choice(
    "professor",
    "You change the subject politely.",
    "counselor",

    fatigue_change= 1, 
    belonging_change= 2, 
    selfworth_change= -1, 
    tension_change= -2
)

# -------------------------
# CHAPTER 8: COUNSELOR
# -------------------------

main_story.add_node(
    "counselor",
    "Counselor",
    """
The new university counselor specializes in future careers. You walk into the room and after a few questions, tell him you want to do medicine. He shakes his head and scorns. To pursue med, you would have to be like Charlie Pienaar, the top scorer in your graduating class, as other counselors have informed him, you might want to consider something more realistic like nursing instead.

You are Charlie Pienaar, you tell him.

It’s as if a wounded Doberman pinscher or a German shepherd has gained the power of speech.

You are Charlie Pienaar? He spits back.

Then he pauses. Everything pauses.

Oh, he says, followed by, yes, I just thought he-she would be-

A guy, you say.

What? he asks.

you instinctively take two steps back though all urgency leaves the possibility of any kind of relationship as you realize nowhere is where you will get from here.
"""
)

main_story.add_choice(
    "counselor",
    "You sigh and leave the room quietly.",
    "tv",

    fatigue_change= 2, 
    selfworth_change= -2, 
    belonging_change= -1, 
    tension_change= -1
)

main_story.add_choice(
    "counselor",
    "You correct him firmly and restate your goals.",
    "tv",

    fatigue_change= 1, 
    selfworth_change= 3, 
    belonging_change= -2, 
    tension_change= 3
)

main_story.add_choice(
    "counselor",
    "You smile and move on, saying you’ll think about nursing.",
    "tv",

    fatigue_change= 1, 
    belonging_change= 2, 
    selfworth_change= -1, 
    tension_change= -2
)

# -------------------------
# CHAPTER 9: TV
# -------------------------

main_story.add_node(
    "tv",
    "Sally Ride",
    """
And when the rocket scientists asked Sally Ride whether 100 tampons would be enough for a week long space mission, you fumble around for the remote to mute the TV. It is all too exhausting as you realise perhaps each sigh is drawn into existence to pull in, pull under, who knows; truth be told, you could no more control those sighs than that which brings the sighs about.
"""
)

main_story.add_choice(
    "tv",
    "Turn off the TV and disengage",
    "ending",

    fatigue_change= 2, 
    selfworth_change= -2, 
    belonging_change= -1, 
    tension_change= -1
)

main_story.add_choice(
    "tv",
    "Turn on the volume again to continue watching, hoping for a good response from Sally Ride",
    "ending",

    fatigue_change= 1, 
    belonging_change= 2, 
    selfworth_change= 1, 
    tension_change= 0
)

main_story.add_choice(
    "tv",
    "Post on instagram about how frustrating their lack of knowledge is",
    "ending",

    fatigue_change= 1, 
    selfworth_change= 2, 
    belonging_change= -2, 
    tension_change= 2
)