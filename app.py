# Databricks notebook source
from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# Load model
model = pickle.load(open("flight_rf.pkl", "rb"))


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:
        # ---------------- DATE ---------------- #
        date_dep = request.form["Dep_Time"]
        Journey_day = int(pd.to_datetime(date_dep).day)
        Journey_month = int(pd.to_datetime(date_dep).month)

        Dep_hour = int(pd.to_datetime(date_dep).hour)
        Dep_min = int(pd.to_datetime(date_dep).minute)

        date_arr = request.form["Arrival_Time"]
        Arrival_hour = int(pd.to_datetime(date_arr).hour)
        Arrival_min = int(pd.to_datetime(date_arr).minute)

        dur_hour = abs(Arrival_hour - Dep_hour)
        dur_min = abs(Arrival_min - Dep_min)

        # ---------------- STOPS ---------------- #
        Total_stops = int(request.form["stops"])

        # ---------------- DEFAULT VALUES ---------------- #
        Jet_Airways = IndiGo = Air_India = Multiple_carriers = 0
        SpiceJet = Vistara = GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

        s_Delhi = s_Kolkata = s_Mumbai = s_Chennai = 0
        d_Cochin = d_Delhi = d_New_Delhi = d_Hyderabad = d_Kolkata = 0

        # ---------------- AIRLINE ---------------- #
        airline = request.form["airline"]

        if airline == "Jet Airways":
            Jet_Airways = 1
        elif airline == "IndiGo":
            IndiGo = 1
        elif airline == "Air India":
            Air_India = 1
        elif airline == "Multiple carriers":
            Multiple_carriers = 1
        elif airline == "SpiceJet":
            SpiceJet = 1
        elif airline == "Vistara":
            Vistara = 1
        elif airline == "GoAir":
            GoAir = 1
        elif airline == "Multiple carriers Premium economy":
            Multiple_carriers_Premium_economy = 1
        elif airline == "Jet Airways Business":
            Jet_Airways_Business = 1
        elif airline == "Vistara Premium economy":
            Vistara_Premium_economy = 1
        elif airline == "Trujet":
            Trujet = 1

        # ---------------- SOURCE ---------------- #
        Source = request.form["Source"]

        if Source == "Delhi":
            s_Delhi = 1
        elif Source == "Kolkata":
            s_Kolkata = 1
        elif Source == "Mumbai":
            s_Mumbai = 1
        elif Source == "Chennai":
            s_Chennai = 1

        # ---------------- DESTINATION ---------------- #
        Destination = request.form["Destination"]

        if Destination == "Cochin":
            d_Cochin = 1
        elif Destination == "Delhi":
            d_Delhi = 1
        elif Destination == "New Delhi":   # ✅ FIXED
            d_New_Delhi = 1
        elif Destination == "Hyderabad":
            d_Hyderabad = 1
        elif Destination == "Kolkata":
            d_Kolkata = 1

        # ---------------- PREDICTION ---------------- #
        prediction = model.predict([[
            Total_stops,
            Journey_day,
            Journey_month,
            Dep_hour,
            Dep_min,
            Arrival_hour,
            Arrival_min,
            dur_hour,
            dur_min,
            Air_India,
            GoAir,
            IndiGo,
            Jet_Airways,
            Jet_Airways_Business,
            Multiple_carriers,
            Multiple_carriers_Premium_economy,
            SpiceJet,
            Trujet,
            Vistara,
            Vistara_Premium_economy,
            s_Chennai,
            s_Delhi,
            s_Kolkata,
            s_Mumbai,
            d_Cochin,
            d_Delhi,
            d_Hyderabad,
            d_Kolkata,
            d_New_Delhi
        ]])

        output = round(prediction[0], 2)

        return render_template(
            "home.html",
            prediction_text=f"Your Flight Price is ₹ {output}"
        )

    except Exception as e:
        return render_template("home.html", prediction_text=f"Error: {str(e)}")


if __name__ == "__main__":
    app.run(debug=True)