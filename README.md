
# Web Scraping and Company Information Extraction using LangChain and Ollama

## Overview

This project demonstrates how to scrape website content and extract specific company-related information using a combination of **BeautifulSoup** for web scraping and **LangChain** with **OllamaLLM** for natural language processing (NLP). The script automates the process of retrieving a company's description, products/services, use cases, customers, and partners from a given website.

## Features

- **Web Scraping**: Uses `requests` and `BeautifulSoup` to scrape and clean the content from a company's webpage.
- **NLP Processing**: Leverages `LangChain` and **Ollama's Llama2 model** to extract company information.
- **User Input**: Prompts the user for a URL and processes the website's content.
- **Extracts Key Information**:
  - Company Description
  - Products/Services
  - Use Cases
  - Key Customers
  - Partners

## Prerequisites

- **Python 3.7+**
- Install the required packages via `pip`:
  ```bash
  pip install requests beautifulsoup4 langchain_ollama
  ```

## How it Works

1. **Web Scraping**: The function `scrape_website(url)` retrieves the content of a company’s website. It uses a custom **User-Agent** header to avoid blocks by web servers and cleans the retrieved HTML to extract readable text.
   
2. **Prompt-based Information Extraction**: After scraping the content, the script uses a predefined template and **Ollama’s Llama2 model** through **LangChain** to extract relevant company information.

3. **Running the Script**: The main function `get_company_info()` asks the user for a company URL, scrapes the content, and then passes it to the language model to extract the necessary details.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/company-info-extraction.git
   cd company-info-extraction
   ```

2. **Install dependencies**:
   ```bash
   pip install requests beautifulsoup4 langchain_ollama
   ```

3. Ensure that you have the required access to the **OllamaLLM** model. You can get started by following the [Ollama Llama2 Model Setup Guide](https://ollama.com/).

## Usage

1. **Run the script**:
   ```bash
   python main.py
   ```

2. **Input the company URL**: You will be prompted to enter the URL of the company’s website that you wish to scrape and extract information from.

3. **Extracted Information**: The script will output the following:
   - Brief company description.
   - List of products or services.
   - Use cases of the company’s offerings.
   - Key customers.
   - Company partners.

### Example

After running the script and providing a company URL, the output will look like:

```
Enter the Company URL: https://example.com
Extracted Company Information:
{
  "Description": "A leading tech company...",
  "Products/Services": ["Software development", "Cloud solutions"],
  "Use Cases": ["Cloud infrastructure for healthcare"],
  "Customers": ["Company A", "Company B"],
  "Partners": ["Partner X", "Partner Y"]
}
```

