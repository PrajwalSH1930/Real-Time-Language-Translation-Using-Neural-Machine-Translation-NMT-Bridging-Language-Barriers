from flask import Flask, render_template, request
from model import translate_english_to_indian, supported_languages

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    translated_text = ""
    if request.method == "POST":
        english_text = request.form["english_text"]
        target_language_code = request.form["target_language"]
        translated_text = translate_english_to_indian(english_text, target_language_code)

    return render_template("index.html", translated_text=translated_text, languages=supported_languages)

if __name__ == "__main__":
    app.run(debug=True)