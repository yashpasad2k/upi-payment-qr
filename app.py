from flask import Flask, request, render_template
import qrcode
from io import BytesIO
import base64

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def generate_qr():
    if request.method == "POST":
        upi_id = request.form.get("upi_id")
        amount = request.form.get("amount", "0")  # Optional amount
        name = request.form.get("name", "Recipient")

        # Generate UPI Payment URL
        upi_url = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu=INR"

        # Generate QR Code
        qr = qrcode.make(upi_url)
        buffer = BytesIO()
        qr.save(buffer, format="PNG")
        qr_base64 = base64.b64encode(buffer.getvalue()).decode()

        return render_template("index.html", qr_code=qr_base64, upi_url=upi_url)

    return render_template("index.html", qr_code=None)

if __name__ == "__main__":
    app.run(debug=True)
