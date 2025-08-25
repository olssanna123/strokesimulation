from flask import Flask, render_template, request

from data.data import get_hospitals_coordinates
from osrm_travel import format_coordinates

app = Flask(__name__)


@app.route('/')
def show_map():
    varberg = '12.25078,57.10557'
    coords = get_hospitals_coordinates()

    # Only takes WGS84 geographic coordinates
    start = request.args.get('start', varberg)
    end = request.args.get('end', coords["Sahlgrenska Universitetssjukhuset"])

    return render_template('map.html', start=start, end=end)


if __name__ == '__main__':
    app.run(debug=True)
