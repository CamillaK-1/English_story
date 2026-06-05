from flask import Flask, render_template, request, redirect, session

from story_data import main_story


app = Flask(__name__)

app.secret_key = "secret-key"

CHAPTER_ORDER = [
    "cricket",
    "socks",
    "bill",
    "loss",
    "colleague",
    "drive",
    "professor",
    "counselor",
    "tv",
    "ending"
]


@app.route("/")
def intro():
    session["current_node"] = main_story.first_node.id

    session["fatigue"] = 0
    session["belonging"] = 0
    session["selfworth"] = 0
    session["tension"] = 0

    # track the sequence of choices for end-of-story reasoning
    session["history"] = []

    return render_template("index.html")


@app.route("/begin")
def begin():

    return redirect("/story")


@app.route("/story", methods=["GET", "POST"])
def story():

    current_id = session["current_node"]

    current_node = main_story.find(current_id)

    chapter_index = CHAPTER_ORDER.index(current_id) + 1

    # HANDLE CHOICE
    if request.method == "POST":

        choice_index = int(request.form.get("choice"))
        chosen_choice = current_node.choices[choice_index]

        # record this choice in the session history
        hist = session.get("history", [])
        hist.append({
            "node_id": current_node.id,
            "node_title": current_node.title,
            "choice_title": chosen_choice.title,
            "fatigue_change": chosen_choice.fatigue_change,
            "belonging_change": chosen_choice.belonging_change,
            "selfworth_change": chosen_choice.selfworth_change,
            "tension_change": chosen_choice.tension_change,
        })
        session["history"] = hist

        # update stats
        session["fatigue"] += chosen_choice.fatigue_change
        session["belonging"] += chosen_choice.belonging_change
        session["selfworth"] += chosen_choice.selfworth_change
        session["tension"] += chosen_choice.tension_change

        next_id = chosen_choice.next_id

        # 🚨 END CONDITION
        if next_id == "ending":

            ending_type = get_ending(
                session["fatigue"],
                session["selfworth"],
                session["belonging"],
                session["tension"]
            )

            return render_template(
                "ending.html",
                ending=ending_type,
                history=session.get("history", []),
                stats={
                    "fatigue": session.get("fatigue", 0),
                    "belonging": session.get("belonging", 0),
                    "selfworth": session.get("selfworth", 0),
                    "tension": session.get("tension", 0),
                }
            )

        # normal flow
        session["current_node"] = next_id
        return redirect("/story")

    return render_template(
        "story.html",
        node=current_node,
        chapter=chapter_index
    )
def get_ending(fatigue, selfworth, belonging, tension):

    if fatigue >= 16:
        return "high_fatigue"

    if selfworth <= -10:
        return "low_selfworth"

    if tension >= 14:
        return "high_tension"

    if belonging <= -10:
        return "low_belonging"

    return "balanced"
if __name__ == "__main__":

    app.run(debug=True)