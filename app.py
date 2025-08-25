from flask import Flask, render_template, request, jsonify
from data.data import get_hospitals_coordinates

app = Flask(__name__)

@app.route('/')
def show_map():
    return render_template('map.html')

@app.route('/get-coordinates')
def get_coordinates():
    hospitals = get_hospitals_coordinates()
    start = request.args.get('start', hospitals["Kungälvs sjukhus"])
    stop = request.args.get('stop', hospitals["Norra Älvsborgs länssjukhus"])
    end = request.args.get('end', hospitals["Sahlgrenska Universitetssjukhuset"])

    return jsonify({'start': start, 'stop': stop, 'end': end})

if __name__ == '__main__':
    app.run(debug=True)
