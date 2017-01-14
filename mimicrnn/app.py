#!C:\Users\Jordan_2\Documents\Programming\Onomastic\Scripts\python

from flask import Flask, render_template
import keras_rnn
app = Flask(__name__)

@app.route("/")
def main():
	return render_template('index.html')

if __name__ == "__main__":
	app.run()