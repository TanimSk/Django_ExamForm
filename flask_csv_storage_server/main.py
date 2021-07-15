from flask import Flask, request
import Mcsv

app = Flask(__name__)


@app.route("/csv_manager", methods=["POST"])
def save():
    mode = request.form["mode"]
    filename = request.form["filename"]
    row = request.form["row"]
    key = request.form["key"]

    print(mode, filename, row, key)

    if key == 'KEY':
        if mode == 'w':
            Mcsv.write_row(filename, row)
            return 'OK'

        elif mode == 'wh':
            Mcsv.write_rows(filename, row)
            return 'OK'

        elif mode == 'r':
            return Pycsv.get_csv(filename)

        elif mode == 'd':
            Mcsv.remove_csv(filename)
            return 'OK'
        else:
            return 'WRONG MODE'
    else:
        return 'ERROR'


if __name__ == "__main__":
    app.run()
