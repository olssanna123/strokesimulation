from flask import Flask, render_template, request

from data.data import get_em_hosp_coord

app = Flask(__name__)


@app.route('/')
def show_map():

    coords = get_em_hosp_coord()

    # Only takes WGS84 geographic coordinates
    start = request.args.get('start', '13.0038,55.6050')
    end = request.args.get('end', coords["Sahlgrenska Universitetssjukhuset"])

    return render_template('map.html', start=start, end=end)


if __name__ == '__main__':
    app.run(debug=True)
