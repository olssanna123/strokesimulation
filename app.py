from flask import Flask, render_template, request, jsonify
from data.data import get_hospitals_coordinates, create_sampling_array
from montecarlo.loop import loop

app = Flask(__name__)

@app.route('/')
def show_map():
    return render_template('map.html')

@app.route('/get-coordinates')
def get_coordinates():
    array = create_sampling_array()
    res = loop(array)

    hospitals = get_hospitals_coordinates()

    origin = res["Origin"]
    origin_formatted = f"{origin[1]},{origin[0]}"  # lon,lat

    start = request.args.get('start', origin_formatted)
    stop = request.args.get('stop', hospitals["Kungälvs sjukhus"])
    end = request.args.get('end', hospitals["Sahlgrenska Universitetssjukhuset"])

    return jsonify({'start': start, 'stop': stop, 'end': end})

if __name__ == '__main__':
    app.run(debug=True)

