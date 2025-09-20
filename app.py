from flask import Flask, render_template, request, jsonify
import qrcode
import io
import base64

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json.get("data")
    if not data:
        return jsonify({"error": "No data provided"}), 400

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")

    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    qr_code_base64 = base64.b64encode(buf.read()).decode("ascii")

    return jsonify({"qr_code": qr_code_base64})

if __name__ == "__main__":
    app.run(debug=True)
