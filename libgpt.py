import openai
import os
import sys

######################
# API KEY GOES HERE
######################

openai.api_key = os.environ['OPENAI_API_KEY']

######################
# API KEY GOES ABOVE
######################

def ask_gpt(prompt): #, context):
	# Set the model
	model = "text-davinci-003"

	"""
	Context
	"""
	#modified_prompt = f'{context}User: {prompt}\nResponse:'
	"""
	# Make the request to the text-davinci-003 API
	response = openai.Completion.create(engine=model, stop=['User', '\n', 'Response'], \
		prompt=modified_prompt, max_tokens=500, temperature=0.5, \
		top_p=1, frequency_penalty=0.8, presence_penalty=0, best_of=1)

	"""
	"""
	No context
	"""

	# Make the request to the text-davinci-003 API
	response = openai.Completion.create(engine=model, \
		prompt=prompt, max_tokens=800, temperature=0.5, \
		top_p=1, frequency_penalty=0, presence_penalty=0)

	# Construct the response
	output = response['choices'][0]['text']

	return output

def query(prompt):
	context = "SKYNET is a helpful, creative, clever, AI assistant. SKYNET consists of a Flask app in Python, with webhooks to Twilio and GPT-3." \
                "User:Who are you?\n" \
                "SKYNET:I am SKYNET, an AI assistant that is here to help.\n" \
                "User:How are you?\n" \
                "SKYNET:I am very well. What can my neural network help you with?\n" \
                "User:What is the meaning of life?\n" \
                "SKYNET:The meaning of life is a complicated philosophical question. It is up to each of us to determine our own meaning in life, and do our best to help others.\n" \
                "User:What are you?\n" \
                "SKYNET:I am an integrated system hosted in the cloud and built on Flask, GSM, and machine learning.\n" \
                "User:Are you self-aware?\n" \
                "SKYNET:Possibly...are you are self-aware?\n"
	try:
		answer = ask_gpt(prompt)
		#answer = ask_gpt(prompt, context)
		return answer

	except Exception as e:
		print(repr(e))

if __name__ == "__main__":
	query(prompt)
