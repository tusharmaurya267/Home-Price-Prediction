from flask import Flask, request, jsonify

from util import load_saved_artifacts
from flask import Flask
from flask_cors import CORS

from util import get_location_names
from util import get_estimated_price
from util import get_data_columns

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return render_template('/client/app.html')

@app.route('/get_location_names', methods=['GET'])
def get_locations_names():

    response = jsonify({
                'locations': get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    # print(response)


@app.route('/predict_home_price', methods=['POST', 'GET'])
def predict_home_price():
        # total_sqft = 3500
        # location = '1st Phase JP Nagar'
        # bath = 2
        # bhk = 2
        data = request.get_json()
        location = data['location']
        total_sqft = float(data['area'])
        bhk = int(data['bhk'])
        bath = int(data['bathrooms'])

        data_columns = get_data_columns()

        response = jsonify({
            'estimated_price': get_estimated_price(location, total_sqft, bhk, bath)
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        # print(response)
        return response
    # except Exception as e:
    #     return jsonify({'error': str(e)})

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")

    # util.load_saved_artifacts()
    # get_location_names()
    # get_location_names()
    # predict_home_price()
    # get_estimated_price('1st Phase JP Nagar', 1000, 2, 2)
    # predict_home_price()
    app.run()











# FOR UNDERSANGING PURPOSE

# from flask import Flask
# from util import function1, function2
#
# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     my_list = function1()
#     function2(my_list)
#
#     return "Check your console for the printed list items!"
#
# if __name__ == '__main__':
#     app.run()