# UPI QR Code Generator

## 🚀 Overview
This is a simple **Flask-based web application** that generates **QR codes** for UPI payments. Users can enter their **UPI ID**, recipient name, and an optional amount to generate a QR code that can be scanned for quick payments.

## 🔥 Features
- Generate UPI payment QR codes.
- Supports multiple UPI apps (PhonePe, Google Pay, Paytm, etc.).
- Simple and user-friendly interface.
- Dynamic QR code generation using the `qrcode` Python library.
- Deployable on **Flask**.

## 📌 Installation
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/yashpasad2k/upi-qr-flask.git
cd upi-qr-flask
```

### **2️⃣ Install Dependencies**
Make sure you have Python installed. Then run:
```sh
pip install -r requirements.txt
```

### **3️⃣ Run the Application**
```sh
python app.py
```
The application will start at **http://127.0.0.1:5000/**.

## 🛠 Usage
1. Enter your **UPI ID**, recipient name, and amount (optional).
2. Click on **"Generate QR Code"**.
3. A QR code will be generated for the entered UPI details.
4. Scan the QR code using any UPI payment app to make a transaction.

## 📸 Screenshot
![UPI QR Code Generator](https://your-image-url.com)

## 🤝 Contributing
Feel free to fork this repository, make improvements, and submit a pull request. Contributions are always welcome!

## 📜 License
This project is licensed under the **MIT License**.

---
Made with ❤️ using Flask & Python.

