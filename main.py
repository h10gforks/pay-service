from flask import Flask, request, jsonify, json
from random import randint
import traceback

app = Flask("app")

invoke_ids = ["se2021_" + str(x) for x in range(1, 27)]


@app.route("/api/pay", methods=["POST"])
def pay():
    """
    接入所需信息:
    1. invoke_id: se2021_1 se2021_2......
    2. uid: str
    3. amount: float
    :return:
    """
    try:
        request_body = request.json
        if request_body is not None and type(request_body) == dict:
            invoke_id = request_body.get("invoke_id")

            if not invoke_id:
                return jsonify({"msg": f"invoke id not found in request body"}), 400

            if str(invoke_id) not in invoke_ids:
                return jsonify({"msg": f"invoke id {invoke_id} invalid"}), 400

            uid = request_body.get("uid")
            if not uid:
                return jsonify({"msg": "uid not found in request body"}), 400

            amount = request_body.get("amount")
            if not amount:
                return jsonify({"msg": "amount not found in request body"}), 400

            try:
                amount_money = float(amount)
            except ValueError:
                return jsonify({"msg": f"amount <{amount}> convert to number failed"}), 400

            print(f"[request info log] invoke id: {invoke_id} uid: {uid}, amount: {amount}")

            if randint(0, 10) > 1:
                return jsonify({"msg": "success"}), 200
            else:
                return jsonify({"msg": "failed, the balance is not enough"}), 409
        else:
            return jsonify({"msg": "request body invalid"}), 400
    except Exception as e:
        traceback.print_exc()
        return jsonify({"msg": "ooooops, there's some exception did't expect. please tell the TA what data you sent."}), 500


if __name__ == '__main__':
    app.run()
