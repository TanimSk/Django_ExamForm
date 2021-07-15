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

    if key == '**':
        if mode == '**':
            Mcsv.write_row(filename, row)
            return 'OK'

        elif mode == '**':
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
