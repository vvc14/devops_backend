from flask import Flask, request, jsonify

app = Flask(__name__)

bookmarks = [
    {
        "id": 1,
        "title": "OpenAI",
        "url": "https://chat.openai.com",
        "category": "AI",
        "favourite": True
    },
]


@app.get("/")
def home():
    return jsonify({
        "status": "Bookmarks Manager API running successfully at port 8000"
    })


@app.get("/bookmarks")
def get_bookmarks():
    return jsonify(bookmarks)


@app.get("/bookmarks/<int:id>")
def get_bookmark(id):
    for bookmark in bookmarks:
        if bookmark["id"] == id:
            return jsonify(bookmark)

    return jsonify({
        "error": "Bookmark not found"
    }), 404


@app.post("/bookmarks")
def add_bookmark():
    data = request.get_json()

    new_bookmark = {
        "id": len(bookmarks) + 1,
        "title": data["title"],
        "url": data["url"],
        "category": data["category"],
        "favourite": data["favourite"]
    }

    bookmarks.append(new_bookmark)

    return jsonify({
        "status": "New bookmark added successfully",
        "new_bookmark": new_bookmark
    }), 201


@app.patch("/bookmarks/<int:id>")
def update_bookmark(id):
    data = request.get_json()

    for bookmark in bookmarks:
        if bookmark["id"] == id:
            bookmark.update(data)

            return jsonify({
                "status": "Bookmark updated successfully",
                "bookmark": bookmark
            })

    return jsonify({
        "error": "Bookmark not found"
    }), 404


@app.delete("/bookmarks/<int:id>")
def delete_bookmark(id):
    for bookmark in bookmarks:
        if bookmark["id"] == id:
            bookmarks.remove(bookmark)

            return jsonify({
                "status": "Bookmark deleted successfully",
                "bookmark": bookmark
            })

    return jsonify({
        "error": "Bookmark not found"
    }), 404


if __name__ == "__main__":
    app.run(debug=True)
