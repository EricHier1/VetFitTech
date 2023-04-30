from flask import Flask, render_template
from str_functions import create_gui

app = Flask(__name__)


@app.route('/')
def home():
    create_gui()
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
