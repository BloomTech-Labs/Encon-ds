from flask import Flask, request, jsonify
from flask import render_template, make_response
from .calc import calculate
import pandas as pd
import os

# Data files
path_states = os.path.join(os.getcwd(),"data/states_dataset.csv")
path_devices = os.path.join(os.getcwd(),"data/devices_dataset.csv")
# Check if file path exixt
#os.path.exists(path_states)
# Read in csvs
states = pd.read_csv(path_states)
devices = pd.read_csv(path_devices)
# Check shape
#print(states.shape)
#print(devices.shape)


# device = ["Coffee maker", "Microwave", "Dishwasher", "Washer", "Dryer",
#           "Iron", "Ceiling fan", "Space heater", "Laptop", "Computer monitor",
#           "Computer tower", 'Television 19"-36"', 'Television 53"-61"',
#           "Toaster", "Space heater (40gal)"]

# wattage = [900, 750, 1200, 350, 1800, 100, 65, 1200, 50, 150, 120, 65, 170, 800, 4500 ]

# data = {"device": device, "wattage": wattage}

# devices = pd.DataFrame(data=data)


# state =["US Average", "Alabama","Alaska", "Arizona", "Arkansas",  "California",
#          "Colorado", "Connecticut","District Of Columbia", "Delaware", "Florida",
#          "Georgia", "Hawaii", "Idaho,", "Illinois", "Indiana",
#          "Iowa", "Kansas", "Kentucky", "Louisiana","Maine",
#          "Maryland","Massachusetts" , "Michigan", "Minnesota", "Mississippi",
#          "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire",
#          "New Jersey", "New Mexico", "New York","North Carolina", "North Dakota",
#          "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island",
#          "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
#          "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

# abbrev = ["US", "AL", "AK", "AZ", "AR", "CA",
#           "CO", "CT", "DC", "DE", "FL",
#           "GA", "HI", "ID", "IL", "IN",
#           "IA", "KS", "KY", "LA", "ME",
#           "MD", "MA", "MI", "MN", "MS",
#           "MO", "MT", "NE", "NV", "NH",
#           "NJ", "NM", "NY", "NC", "ND",
#           "OH", "OK", "OR", "PA", "RI",
#           "SC", "SD", "TN", "TX", "UT",
#           "VT", "VA", "WA", "WV", "WI", "WY"]

# rate = [13.2, 11.85, 21.75, 12.21, 9.3, 18.34,
#         11.89, 21.51, 13, 12.25, 11.99,
#         10.7, 32.08, 9.83, 12.19,11.87,
#         11.44, 10.29, 10.21, 8.84, 17.26,
#         13.07, 22.51, 15, 12.79, 10.95,
#         9.28, 10.83, 9.6, 11.79, 19.96,
#         15.72, 12.21, 17.27, 10.99, 9.17,
#         11.98, 8.8, 10.63, 12.53, 22.7,
#         11.89, 10.57, 10.78, 11.65, 10.01,
#         16.73, 11.4, 9.31, 9.72, 14.01, 10.56]

# data = {"state": state, "abbrev": abbrev, "rate": rate }

# states = pd.DataFrame(data=data)

# states["rate"] = (states["rate"]/100)



# def calculate(device, state, hours, days):
#     device = device
#     wattage = devices[devices["device"] == device]["wattage"].item()
#     state = state 
#     utility_rate = states[states["state"] == state]["rate"].item()
#     hours_per_day = hours
#     days_per_year = days * 52
#     watts_per_kilowatt = 1000

#     energy_used = (wattage*hours_per_day*days_per_year)/watts_per_kilowatt
#     cost_per_year = round(energy_used* utility_rate,2)

#     return("Energy used-----" + str(energy_used), "Cost per year---" + str(cost_per_year))


app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def Welcome():
    return "Welcome to EnCon"

@app.route('/calculate/<device>/<state>/<hours>/<days>', methods = ['GET', 'POST'])
def show_result(device, state, hours, days):
    device = str(device)
    state = str(state)
    hours = int(hours)
    days = int(days)
    result = calculate(device, state, hours, days)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
    print(calculate("Ceiling fan","Missouri",8,5))