import yaml
import google.generativeai as genai

# Store API key in a seperate YAML file and load it safely
# Prevents the API key from being accidentally leaked
with open('assets/credentials.yml', 'r') as credentials :
    creds = yaml.safe_load(credentials)

GOOGLE_API_KEY = creds['gemini_api_key']

genai.configure(api_key = GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

response = model.generate_content('Tell me more about Crux AI as a company and its employees (https://getcrux.ai)')
print(response.text)