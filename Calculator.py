from flask import Flask, render_template, request, redirect, url_for

import os

app = Flask(__name__, template_folder='.')

# In-memory task list (not persistent)
tasks = []

@app.route("/")
def index():
    return render_template("Template.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")
    if task:
        tasks.append(task)
    return redirect(url_for("index"))

@app.route("/delete/<int:task_id>")
def delete(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for("index"))

# ... your Flask app setup code ...

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)