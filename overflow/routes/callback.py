import secrets

from flask import jsonify, request

from overflow import app,db
from overflow.models.payment import PaymentDump
from overflow.others.schema import payment_schema
# TODO : add esocte support for the app {on successful copy}


# You may create a separate URL for every endpoint you need
@app.route('/mpesa/stkpush', methods=["POST"])
def listenb2c():
    # save the data
    request_data = request.data
    if request_data:
        # response
        decoded = request_data.decode()
        lookup = PaymentDump(decoded)
        db.session.add(lookup)
        db.session.commit()
        payment_schema.dump(lookup)
    else:
        pass
        # TODO : add logging reason why we could not add payments to the datbase

    message = {
        "ResultCode": 0,
        "ResultDesc": "The service was accepted successfully",
        "ThirdPartyTransID": secrets.token_hex()
    }
    # Send the response back to the server
    return jsonify({'message': message}), 200


@app.route("/mpesa/reversals", methods=["POST"])
def reversals():

    # save the data
    request_data = request.data
    decoded = request_data.decode()

    # define the response
    message = {
        "ResultCode": 0,
        "ResultDesc": "The service was accepted successfully",
        "ThirdPartyTransID": secrets.token_hex()
    }
    # Send the response back to the server
    return jsonify({'message': message}), 200


# Change this part to reflect the API you are testing
@app.route('/mpesa/b2b/v1')
def listenb2b():
    request_data = request.data
    print(request_data)
    message = {
        "ResultCode": 0,
        "ResultDesc": "The service was accepted successfully",
        "ThirdPartyTransID": "1234567890"
    }
    return message
