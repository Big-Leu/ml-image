from flask import Flask, request, jsonify
from flask_cors import CORS
from util.form.crud import commentService, formService
from util.chatbot.chat import get_response
app = Flask(__name__)
CORS(app)


@app.route("/api/v1/form/signUP", methods=["POST"])
async def post_details():
    data = request.json
    if not data:
        return jsonify({"message": "INVALID"}), 400
    result = await formService().signUp(data)
    return jsonify(message=result), 200


@app.route("/api/v1/form/login", methods=["POST"])
async def get_deatails():
    data = request.json
    if not data:
        return jsonify({"message": "INVALID"}), 400
    result = await formService().login(data)
    return jsonify(result), 200


@app.route("/api/v1/form/comment", methods=["POST"])
async def fill_comment():
    data = request.json
    if not data:
        return jsonify({"message": "INVALID"}), 400
    result = await commentService().comment(data)
    return jsonify(result), 200


@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)


if __name__ == "__main__":
    app.run(debug=True)
