import pickle
import json
import numpy as np
from sklearn.linear_model import LinearRegression

__locations = None
__data_columns = None
__model = None


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk

    global __model
    if __model is None:
        with open('./artifacts/banglore_home_prices_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():
    load_saved_artifacts()
    # print (__locations)
    return __locations

def get_data_columns():
    load_saved_artifacts()
    # print(__data_columns)
    return __data_columns


def get_estimated_price(location, sqft, bhk, bath):
    load_saved_artifacts()
    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    # print(round(__model.predict([x])[0], 2))
    return round(__model.predict([x])[0], 2)


# if __name__ == '__main__':
    # get_data_columns()
    # load_saved_artifacts()
    # print((get_location_names()))
    # print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
    # print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    # print(get_estimated_price('Kalhalli', 3000, 2, 2)) # other location
    # print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location









# FOR UNDERSANGING PURPOSE

# my_list = []  # Declare a global list
#
# def func():
#     global my_list  # Access the global my_list
#     my_list = [1, 2, 3, 4, 5]
#
# def function1():
#     func()  # Call func to modify the global my_list
#     return my_list
#
# def function2(some_list):
#     for item in some_list:
#         print(item)