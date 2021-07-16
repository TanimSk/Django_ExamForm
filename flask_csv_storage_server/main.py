from flask import Flask, request
import Mcsv
from evaluate import evaluate

app = Flask(__name__)


@app.route("/csv_manager", methods=["POST"])
def save():
    mode = request.form["mode"]
    filename = request.form["filename"]
    key = request.form["key"]

    print(mode, filename, row, key)

    if key == 'KEY':
        if mode == 'w':
            ques_json =  request.form["ques_json"]
            ans_json = request.form["ans_json"]

            Mcsv.write_row(filename, evaluate.evaluate(ques_json, ans_json))
            return 'OK'

        elif mode == 'wh':
            row = request.form["row"]
            Mcsv.write_rows(filename, row)
            return 'OK'

        elif mode == '**':
            return Pycsv.get_csv(filename)

        elif mode == '**':
            Mcsv.remove_csv(filename)
            return 'OK'
        else:
            return 'WRONG MODE'
    else:
        return 'ERROR'


if __name__ == "__main__":
    app.run()
