import requests
import sms_helper
import libgpt
from flask import Flask, request
from time import sleep

"""
Issues:
- Context causes GPT-3 to fail on prompts requesting code examples
- Response is somehow faster than the submitted SMS sometimes - race condition?
"""

app = Flask(__name__)

src_phone="+18885551111" # Your Twilio Number Here

def check_authorized_phone(dst_phone):
    authorized_phones = ('+18885552222',) # Your Client Phone Number Here
    if dst_phone in authorized_phones:
        return True
    else:
        return False

def handle_race_condition():
	sleep(1)
	return

@app.route('/sms', methods=['POST'])
def print_body():
    body_content = request.form['Body']
    dst_phone = request.form['From'].split('%2B')[0]

    verify_webhook = request.headers.get('X-Twilio-Signature', None)

    if verify_webhook == None:
        return f'Unauthorized', 401

    if check_authorized_phone(dst_phone) == False:
        print(f'[!] Unauthorized access detected from: {dst_phone}')
        return f'Unauthorized', 401

    if check_authorized_phone(dst_phone) == True:
        print(f'[+] Authorized: {dst_phone}')
        make_ai_request = libgpt.query(body_content)

        handle_race_condition()

        sms_helper.broker_sms(make_ai_request, src_phone, dst_phone)

        return 'OK', 200

    return 'OK', 200


@app.errorhandler(500)
def internal_server_error(error):
    return 'An internal server error has occurred.', 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
