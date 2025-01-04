from flask import Flask, request, session, Response
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

from query_data import get_query_response


app = Flask(__name__)
app.secret_key = '3d6f45a5fc12445dbac2f59c3b6c7cb1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


account_sid = 'YOUR_SSID'
auth_token = 'YOUR_TOKEN'
client = Client(account_sid, auth_token)


@app.route("/bot", methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    text = request.values.get('From', '').lower()
    print(text)

    resp = MessagingResponse()
    msg = resp.message()
    response = get_query_response(incoming_msg)
    msg.body(response)

    message = client.messages.create(
        from_='whatsapp:+14155238886', body=response, to=text, status_callback='https://8b76-105-112-182-49.ngrok-free.app/bot')

    return Response(str(resp), mimetype='text/xml')

if __name__ == "__main__":
    app.run()
