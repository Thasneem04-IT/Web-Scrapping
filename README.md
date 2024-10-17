**Company Information Scraper using LangChain and Ollama**
This project is a web scraping and AI-powered tool that extracts relevant information from a company's website, such as its description, products/services, use cases, customers, and partners. It uses BeautifulSoup for web scraping and the Llama2 model from Ollama through LangChain to analyze and structure the extracted data.

Features
Scrapes Content: Collects all text content from the specified company URL.
AI-Powered Extraction: Uses Llama2 via LangChain to identify and extract:
Company Description
Products or Services
Use Cases
Key Customers
Partners
Interactive Input: Users enter the company URL directly through the console.
Technologies Used
Python: Core programming language for the project.
BeautifulSoup: For web scraping and parsing HTML content.
Requests: For making HTTP requests to company URLs.
LangChain: For integrating the Ollama LLM model and building a prompt-based interaction.
Ollama LLM: Uses Llama2 model for extracting structured information from scraped text.
Prerequisites
Python 3.x installed on your system.
Install required libraries using:
bash
Copy code
pip install requests beautifulsoup4 langchain-core langchain-ollama
Usage
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/your-repo.git
cd your-repo
Run the script:
bash
Copy code
python your_script_name.py
Enter the company URL when prompted (e.g., https://example.com).
The script will scrape the content, send it to the Llama2 model via LangChain, and display the extracted information.
