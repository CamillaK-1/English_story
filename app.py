from flask import Flask, render_template, request, redirect, session

from story_data import main_story


app = Flask(__name__, 
            template_folder='templates',   # ← Add this
            static_folder='static')        # ← Good practice too

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

    # HANDLE CHOICE (POST)
    if request.method == "POST":
        choice_index = int(request.form.get("choice"))
        chosen_choice = current_node.choices[choice_index]

        # record choice in session history
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

        # END CONDITION
        if next_id == "ending":
            ending_type = get_ending(
                session["fatigue"],
                session["selfworth"],
                session["belonging"],
                session["tension"],
            )
            # Store ending type in session for the ending page
            session["ending_type"] = ending_type
            # For AJAX or normal POST, redirect to ending page
            return redirect("/ending")

        # Normal flow: update current node
        session["current_node"] = next_id

        # If this is an AJAX request, return only the story HTML (no layout)
        if request.headers.get("X-Requested-With") == "XMLHttpRequest":
            new_node = main_story.find(next_id)
            new_chapter_index = CHAPTER_ORDER.index(next_id) + 1
            # Compute next_node for the template (for the hidden next page preview)
            next_node = None
            if new_node.choices:
                first_next_id = new_node.choices[0].next_id
                if first_next_id != "ending":
                    next_node = main_story.find(first_next_id)
            # Render only the story template (without base.html)
            return render_template(
                "story.html",
                node=new_node,
                chapter=new_chapter_index,
                next_node=next_node
            )
        else:
            # Normal form submit (non-AJAX) – redirect to GET /story
            return redirect("/story")

    # GET request: normal page load
    next_node = None
    if current_node.choices:
        first_next_id = current_node.choices[0].next_id
        if first_next_id != "ending":
            next_node = main_story.find(first_next_id)

    return render_template(
        "story.html",
        node=current_node,
        chapter=chapter_index,
        next_node=next_node
    )
@app.route("/ending")
def ending():
    ending_type = session.get("ending_type", "balanced")
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
def get_ending(fatigue, selfworth, belonging, tension):

    scores = {
        "high_fatigue": fatigue,
        "low_selfworth": -selfworth,
        "low_belonging": -belonging,
        "high_tension": tension
    }

    # find strongest emotional force
    top_ending = max(scores, key=scores.get)
    top_value = scores[top_ending]

    # thresholds (soft gates, not hard locks)
    thresholds = {
        "high_fatigue": 12,
        "low_selfworth": 8,
        "low_belonging": 8,
        "high_tension": 10
    }

    # if strong enough → that ending
    if top_value >= thresholds[top_ending]:
        return top_ending

    # fallback logic (important for your “Balanced” ending)
    burnout_score = fatigue + tension
    identity_score = selfworth + belonging

    if burnout_score > 18:
        return "high_fatigue"

    if identity_score < -10:
        return "low_selfworth"

    return "balanced"
    
if __name__ == "__main__":

    app.run(debug=True)
