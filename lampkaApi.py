from flask import Flask

app = Flask(__name__)

@app.route("/")
def toggle_lampka():
    # TODO: tu wstaw kod wlazcajacy lampke zamiast ponizszej lini
    return "<p>Hello, World!</p>"