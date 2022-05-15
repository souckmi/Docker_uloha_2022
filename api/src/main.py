from flask import Flask, render_template, request
from flask_restful import Resource, Api
import sender

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/save_record', methods=["POST"])
def save_record():
    records = request.form.get("record")
    records_list = records.split("\n\n")
    sender.saveParams(records_list)
    return render_template("saved_record.html", records = records)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)