from flask import Flask, request
from sqldb import load_image, get_image
import base64

app = Flask(__name__)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() == "jpg"


@app.post("/upload")
def upload_file():
    photos = request.files

    for photo in photos.getlist(""):
        if allowed_file(photo.filename):
            return "ID: " + load_image(photo.read())
        return "Wrong format!"


@app.get("/get/<photo_id>")
def get_file(photo_id):
    photo = get_image(photo_id)
    photo = base64.b64encode(photo[0]).decode('utf-8')
    return f"<img src='data:image/jpg;base64,{photo}'>"


app.run()
