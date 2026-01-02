@app.route("/submittodoitem", methods=["POST"])
def submit_todo():
    item_name = request.form["itemName"]
    item_desc = request.form["itemDescription"]

    collection.insert_one({
        "itemName": item_name,
        "itemDescription": item_desc
    })

    return jsonify({"message": "Item stored successfully"})

