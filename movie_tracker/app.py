"""Flask web UI for the movie/series tracker.

Run with:
    python app.py
Then open http://127.0.0.1:5000
"""

from flask import Flask, redirect, render_template, request, url_for

import storage

app = Flask(__name__)


@app.before_request
def _ensure_db():
    storage.init_db()


@app.route("/")
def index():
    type_ = request.args.get("type") or None
    status = request.args.get("status") or None
    sort_by = request.args.get("sort", "title")
    entries = storage.list_entries(type_=type_, status=status, sort_by=sort_by)
    return render_template(
        "index.html",
        entries=entries,
        types=storage.TYPES,
        statuses=storage.STATUSES,
        selected_type=type_,
        selected_status=status,
        selected_sort=sort_by,
    )


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        storage.add_entry(
            title=request.form["title"].strip(),
            type_=request.form["type"],
            status=request.form["status"],
            rating=_to_int(request.form.get("rating")),
            current_season=_to_int(request.form.get("current_season")),
            current_episode=_to_int(request.form.get("current_episode")),
            total_episodes=_to_int(request.form.get("total_episodes")),
            notes=request.form.get("notes") or None,
        )
        return redirect(url_for("index"))
    return render_template("form.html", entry=None, types=storage.TYPES, statuses=storage.STATUSES)


@app.route("/edit/<int:entry_id>", methods=["GET", "POST"])
def edit(entry_id):
    entry = storage.get_entry(entry_id)
    if entry is None:
        return redirect(url_for("index"))

    if request.method == "POST":
        storage.update_entry(
            entry_id,
            title=request.form["title"].strip(),
            type=request.form["type"],
            status=request.form["status"],
            rating=_to_int(request.form.get("rating")),
            current_season=_to_int(request.form.get("current_season")),
            current_episode=_to_int(request.form.get("current_episode")),
            total_episodes=_to_int(request.form.get("total_episodes")),
            notes=request.form.get("notes") or None,
        )
        return redirect(url_for("index"))
    return render_template("form.html", entry=entry, types=storage.TYPES, statuses=storage.STATUSES)


@app.route("/delete/<int:entry_id>", methods=["POST"])
def delete(entry_id):
    storage.delete_entry(entry_id)
    return redirect(url_for("index"))


@app.route("/stats")
def stats():
    return render_template("stats.html", stats=storage.get_stats(), statuses=storage.STATUSES, types=storage.TYPES)


def _to_int(value):
    if value is None or value == "":
        return None
    return int(value)


if __name__ == "__main__":
    app.run(debug=True)
