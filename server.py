#//// Imports ////#


from flask import Flask, render_template, request
from colorthief import ColorThief # To fetch the colors of the uploaded image.
from werkzeug.utils import secure_filename # Used to sanitize and secure filenames before storing them on the server for security reasons.
import os # To specify the file paths.

# Basically, secure_filename removes or replaces characters that could be used for malicious purposes, such as directory traversal attacks.


#//// App Initializations + Config ////#


da_app = Flask(__name__)


da_app.config["UPLOAD_FOLDER"] = "static/images/" # Configuring the directory in which user's images will be stored!!!!!

# "/static/images/" Won't work!!!!!


#//// Website Routes ////#


@da_app.route("/")
def main_page():

    return render_template("index.html", colors="", da_image="")


@da_app.route("/submit", methods=["POST"])
def image_submit(): # Loads when the user submits the image.

    da_image = request.files["da_image"] # Getting the data of the image file.

    da_filename = secure_filename(da_image.filename) # Securing the data encrypted in the file.

    da_image.save(os.path.join(da_app.config["UPLOAD_FOLDER"], da_filename)) # Saving the image into static/images folder.

    da_path = f"{da_app.config["UPLOAD_FOLDER"]}{da_filename}" # Specifying the path to the file.

    da_colors = ColorThief(da_path) # Getting the colors of the image using a path from "da_path" variable.

    color_pallet = da_colors.get_palette(color_count=11) # Returning 5 most common colours in the image.

    return render_template("index.html", colors=color_pallet, da_image=da_path)


if __name__ == "__main__":

    da_app.run(debug=True)
