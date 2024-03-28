import yaml
import PIL
import google.generativeai as genai

# Store API key in a seperate YAML file and load it safely
# Prevents the API key from being accidentally leaked
with open('assets/credentials.yml', 'r') as credentials :
    creds = yaml.safe_load(credentials)

GOOGLE_API_KEY = creds['gemini_api_key']

genai.configure(api_key = GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro-vision')

it_support_img = PIL.Image.open('assets/error_msg.png')

prompt = """
Act as a customer support agent. Remember to ask for relevant information based on the customer issue to solve the problem.
Don't deny them help without asking for relevant information. For the attached support image, create a response
with the following information :

orig_msg : The original customer message
orig_lang : Detected language of the customer message
trans_msg : Customer message translated in english
orig_res : Response to the customer in orig_lang
trans_res : orig_res translated to english
"""

res = model.generate_content([prompt, it_support_img])
print(res.text)