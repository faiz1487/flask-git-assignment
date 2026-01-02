from flask import Flask, jsonify, render_template, request
from pymongo import MongoClient # type: ignore
import json

app = Flask(__name__)

# ---------- MongoDB Atlas Connection ----------
client = MongoClient("YOUR_MONGODB_ATLAS_CONNECTION_STRING")
db = client["assignment_db"]
collection = db["users"]

# ---------- API Route ----------
@app.route("/api")
def api():
    with open("data.json", "r") as file:
        data = json.load(file)
    return jsonify(data)

# ---------- Form Page ----------
@app.route("/", methods=["GET", "POST"])
def form():
    error = None

    if request.method == "POST":
        try:
            name = request.form["name"]
            email = request.form["email"]

            collection.insert_one({
                "name": name,
                "email": email
            })

            return render_template("success.html")

        except Exception as e:
            error = str(e)

    return render_template("form.html", error=error)

# ---------- Run Server ----------
if __name__ == "__main__":
    app.run(debug=True)
