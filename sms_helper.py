import os
from twilio.rest import Client

def broker_sms(msgbody, src_phone, dst_phone):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    #print(f'Msgbody: {msgbody}')

    message = client.messages.create(
        body=msgbody,
        from_=str(src_phone),
        to=str(dst_phone))

if __name__ == '__main__':
    broker_sms(msgbody, dst_phone)
