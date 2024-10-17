import requests
from bs4 import BeautifulSoup
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Set a User-Agent header for web scraping
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}

# Function to scrape website content
def scrape_website(url):
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        page_content = soup.get_text()
        cleaned_content = ' '.join(page_content.split())
        print(cleaned_content)
        return cleaned_content
    else:
        print(f"Failed to retrieve the website. Status code: {response.status_code}")
        return ""

# LangChain setup with a prompt template
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Description**: Extract a brief company description. \n"
    "2. **Products/Services**: List the products or services the company offers. \n"
    "3. **Use Cases**: Extract use cases where the company's offerings are applied. \n"
    "4. **Customers**: Identify key customers of the company. \n"
    "5. **Partners**: Identify the company's partners."
)

model = OllamaLLM(model="llama2")

def parse_with_ollama(dom_content):
    # Using LangChain to construct and send the prompt
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    # Invoke the model with the cleaned content
    response = chain.invoke({"dom_content": dom_content})
    return response

# Main function to get company information
def get_company_info():
    company_url = input("Enter the Company URL: ")
    
    # Scrape the website content
    cleaned_content = scrape_website(company_url)

    # Check if content is available
    if cleaned_content:
        # Extract information using the LLM
        extracted_info = parse_with_ollama(cleaned_content)
        
        # Output the extracted details
        print("Extracted Company Information:")
        print(f"{extracted_info}")
    else:
        print("No content available to parse.")

# Run the function to fetch and parse company information
get_company_info()
