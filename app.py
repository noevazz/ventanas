from flask import Flask, request, jsonify, Response
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client 
import os

account_sid = os.environ['account_sid_']
auth_token = os.environ['auth_token_']
client = Client(account_sid, auth_token) 

app = Flask(__name__)

@app.route('/')
def main():
    return "HELLO"

@app.route('/testsms', methods=['POST'])
def testsms():
    print("⭐ Recibiendo datos de UBIDOTS: ")
    data = request.json
    print(data)
    number = data['number']
    message = data["message"]
    if number == "all":
        to = []
        for msgs in client.messages.list():
            if("Join" in msgs.body):
                if msgs.from_.replace('whatsapp:+','') not in to:
                    to.append(msgs.from_.replace('whatsapp:+',''))
                
        print("#########################################################################")
        print(to)
        for number in to:
            client.messages.create(to=f'whatsapp:+{number}', from_='whatsapp:+14155238886', body=message )
        status_code = Response(status=201)
    else:   
        message = client.messages.create(to=f'whatsapp:+521{number}', from_='whatsapp:+14155238886', body=message) 
        print(message.sid)
    return Response(status=201)


if __name__ == '__main__':
    app.run(debug=True)