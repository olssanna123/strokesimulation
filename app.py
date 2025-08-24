from flask import Flask, render_template, request

from data.data import create_sampling_array

app = Flask(__name__)


@app.route('/')
def show_map():
    start = request.args.get('start', '13.388860,52.517037')  # default Berlin
    end = request.args.get('end', '13.397634,52.529407')  # default Berlin

    return render_template('map.html', start=start, end=end)


if __name__ == '__main__':
    app.run(debug=True)
