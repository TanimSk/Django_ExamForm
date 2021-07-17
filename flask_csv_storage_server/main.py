from flask import Flask, request
import Mcsv
from evaluate import evaluate
import json

app = Flask(__name__)


@app.route("/csv_manager", methods=["POST"])
def save():
    mode = request.form["mode"]
    filename = request.form["filename"]
    key = request.form["key"]

    if key == 'KEY':
        if mode == 'w':
            ques_json = request.form["ques_json"]
            ans_json = request.form["ans_json"]
            Mcsv.write_row("C_answers/"+filename, evaluate(ques_json, ans_json))
            return 'OK'

        elif mode == 'wh':
            ques_csv = request.form["ques_csv"]
            ans_csv = request.form["ans_csv"]
            file = "C_questions/"+filename
            Mcsv.write_file(file, ques_csv, 'q')
            file = "C_answers/"+filename
            Mcsv.write_file(file, ans_csv, 'a')

            return 'OK'

        elif mode == 'r':
            return {'question': str(Mcsv.get_csv("C_questions/"+filename, 0)), 'answer': str(Mcsv.get_csv("C_answers/"+filename, 1))}

        elif mode == 'd':
            Mcsv.remove_csv("C_questions/"+filename)
            Mcsv.remove_csv("C_answers/"+filename)
            return 'OK'
        else:
            return 'WRONG MODE'
    else:
        return 'ERROR'


if __name__ == "__main__":
    app.run()
