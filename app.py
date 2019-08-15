@app.route("/")
def index():
    hurricanes = list(db.collection.find())
    print(hurricanes)
    return render_template("index.html", hurricanes=hurricanes)


if __name__ == "__main__":
    app.run(debug=True)
