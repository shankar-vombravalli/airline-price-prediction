
# ✈️ Flight Price Prediction Web App

## 📌 Project Overview

This project is a **Machine Learning Web Application** that predicts flight ticket prices based on user inputs like departure time, arrival time, source, destination, airline, and number of stops.

The model is trained using **Random Forest Regressor** and deployed using **Flask**.

---

## 🚀 Features

* Predict flight ticket price 💰
* Real-time user input via web form
* Boarding pass style UI 🎫
* Full-screen background with modern design 🌄
* Fast and simple prediction

---

## 🛠️ Tech Stack

* Python 🐍
* Flask 🌐
* Scikit-learn 🤖
* Pandas 📊
* HTML + CSS 🎨

---

## 📂 Project Structure

```
Flight-Price-Prediction/
│
├── app.py                  # Flask backend
├── flight_rf.pkl           # Trained ML model
│
├── templates/
│     └── home.html         # Frontend UI
│
├── static/
│     └── css/
│          └── styles.css   # Styling
│
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```
git clone https://github.com/shankar-vombravalli/Flight-Price-Prediction.git
cd Flight-Price-Prediction
```

---

### 2️⃣ Install Requirements

```
pip install -r requirements.txt
```

👉 If no requirements file:

```
pip install flask pandas scikit-learn
```

---

### 3️⃣ Fix Model Version Issue (IMPORTANT)

If you get sklearn error:

```
ValueError: incompatible dtype
```

Run:

```
pip install scikit-learn==0.22.1
```

---

### 4️⃣ Run Application

```
python app.py
```

---

### 5️⃣ Open in Browser

```
http://127.0.0.1:5000/
```

---

## 📊 Input Features

* Departure Time
* Arrival Time
* Source
* Destination
* Total Stops
* Airline

---

## 🤖 Model Details

* Algorithm: Random Forest Regressor
* Input: Encoded categorical + time features
* Output: Predicted flight price

---

## 🎯 How It Works

1. User enters flight details
2. Flask receives input
3. Data is preprocessed
4. Model predicts price
5. Result shown as ticket UI

---

## 🧠 Challenges Faced

* Handling categorical encoding manually
* Fixing sklearn model compatibility
* UI rendering issues in Flask
* Creating realistic ticket UI

---

## 📈 Future Improvements

* Add airline logos 🏢
* Add ticket QR code 🧾
* Deploy on cloud (Render / AWS)
* Improve UI animations ✨

---

## 🙌 Author

**Shankar Vombravalli**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!

<img width="931" height="671" alt="airline_image_output" src="https://github.com/user-attachments/assets/3a5e2fa3-8cf3-4cdb-b587-8337ea1c70f6" />

