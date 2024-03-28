import yaml
import google.generativeai as genai

# Store API key in a seperate YAML file and load it safely
# Prevents the API key from being accidentally leaked
with open('assets/credentials.yml', 'r') as credentials :
    creds = yaml.safe_load(credentials)

GOOGLE_API_KEY = creds['gemini_api_key']

genai.configure(api_key = GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

it_support_query = "我无法访问公司的网站。每次都显示错误信息。请帮忙解决。"

context = """
Act as a customer support agent. Remember to ask for relevant information based on the customer issue to solve the problem.
Don't deny them help without asking for relevant information. For the above written support request, create a response
with the following information :

orig_msg : The original customer message
orig_lang : Detected language of the customer message
trans_msg : Customer message translated in english
orig_res : Response to the customer in orig_lang
trans_res : orig_res translated to english
"""

prompt = 'Support request : ' + it_support_query + '\n' + context
res = model.generate_content(prompt)
print(res.parts)