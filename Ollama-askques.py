import requests
from bs4 import BeautifulSoup
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# URL of the website to scrape
url = 'https://pairpoint.io/'

# Set a User-Agent header
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}

# Send a GET request to the website with headers
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    page_content = soup.get_text()
    cleaned_content = ' '.join(page_content.split())
    print(cleaned_content)
else:
    print(f"Failed to retrieve the website. Status code: {response.status_code}")
    cleaned_content = ""

# LangChain setup
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

model = OllamaLLM(model="llama2")

def parse_with_ollama(dom_content, parse_description):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    # Invoke the model with the cleaned content and user description
    response = chain.invoke(
        {"dom_content": dom_content, "parse_description": parse_description}
    )
    return response

# Main loop to ask questions
if cleaned_content:
    while True:
        user_question = input("Enter your question (or type 'exit' to quit): ")
        if user_question.lower() == 'exit':
            break
        answer = parse_with_ollama(cleaned_content, user_question)
        print(f"Answer: {answer}")
else:
    print("No content available to parse.")
