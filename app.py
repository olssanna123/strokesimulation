from flask import Flask, render_template, request

from data.data import create_sampling_array

app = Flask(__name__)


@app.route('/')
def show_map():
    # Only takes WGS84 geographic coordinates
    start = request.args.get('start', '13.0038,55.6050')
    end = request.args.get('end', '11.9668,57.6819')

    return render_template('map.html', start=start, end=end)


if __name__ == '__main__':
    app.run(debug=True)
