from flask import Flask, render_template, abort
from data import CRITERIA, PLATFORMS, JUDGEMENTS, compute_score, get_platform_data, get_category_scores
from itertools import groupby

app = Flask(__name__)


def score_color(score: float) -> str:
    if score >= 8:
        return "#28a745"
    if score >= 5:
        return "#fd7e14"
    return "#dc3545"


@app.context_processor
def inject_globals():
    return {"platforms": PLATFORMS, "score_color": score_color, "zip": zip}


@app.route("/")
def index():
    cards = []
    for service, info in PLATFORMS.items():
        score = compute_score(service)
        cat_scores = get_category_scores(service)
        cards.append({**info, "service": service, "score": score, "cat_scores": cat_scores})
    cards.sort(key=lambda x: x["score"], reverse=True)
    return render_template("index.html", cards=cards)


@app.route("/platform/<service>")
def platform(service):
    if service not in PLATFORMS:
        abort(404)
    data = get_platform_data(service)

    # group criteria by category preserving order
    categories = []
    for cat, items in groupby(CRITERIA, key=lambda c: c["category"]):
        crit_list = list(items)
        judgements = [data["judgements"].get(c["id"], {}) for c in crit_list]
        categories.append({"name": cat, "criteria": crit_list, "judgements": judgements})

    cat_scores = get_category_scores(service)
    return render_template("platform.html", platform=data, categories=categories, cat_scores=cat_scores)


if __name__ == "__main__":
    app.run(debug=True)
