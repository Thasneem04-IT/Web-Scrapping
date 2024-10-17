# import requests
# from bs4 import BeautifulSoup
# from transformers import pipeline
# from sentence_transformers import SentenceTransformer

# # Step 1: Function to scrape website content
# def scrape_website(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
    
#     # Extract text from paragraphs
#     paragraphs = soup.find_all('p')
#     text_content = " ".join([para.get_text() for para in paragraphs])
#     print(text_content)
    
#     return text_content

# # Step 2: Load a lightweight local LLM for question-answering
# def load_local_llm():
#     # Load a small model for question-answering
#     model_name = 'distilbert-base-uncased-distilled-squad'  # Small, CPU-friendly model
#     qa_pipeline = pipeline('question-answering', model=model_name)
#     return qa_pipeline

# # Step 3: Function to ask specific company-related questions
# def ask_questions(qa_pipeline, text):
#     questions = [
#         "What is the company description?",
#         "Who are the partners of the company?",
#         "Who are the customers of the company?",
#         "What is the revenue of the company?"
#     ]
    
#     extracted_info = {}
    
#     for question in questions:
#         answer = qa_pipeline(question=question, context=text)
#         extracted_info[question] = answer['answer']
    
#     return extracted_info

# # Step 4: Main function to scrape and ask questions
# def get_company_details(url):
#     # Scrape the content
#     scraped_text = scrape_website(url)
    
#     if len(scraped_text.strip()) == 0:
#         print("No content found to process.")
#         return
    
#     # Load the local LLM model
#     qa_pipeline = load_local_llm()
    
#     # Ask the relevant questions
#     details = ask_questions(qa_pipeline, scraped_text)
    
#     # Display the results
#     for question, answer in details.items():
#         print(f"{question}: {answer}")

# # Test with any company URL
# url = "https://www.kern.ai/"
# get_company_details(url)


import requests
from bs4 import BeautifulSoup
from transformers import pipeline

# Step 1: Function to scrape website content from multiple tags
def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract text from multiple tags like paragraphs, headings, and list items
    paragraphs = soup.find_all('p')
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    list_items = soup.find_all('li')
    
    # Combine all text content
    content = []
    
    # Append text from each tag section
    content.extend([para.get_text() for para in paragraphs])
    content.extend([heading.get_text() for heading in headings])
    content.extend([li.get_text() for li in list_items])
    
    # Join all content into one text block
    text_content = " ".join(content)
    print(text_content)
    
    return text_content

# Step 2: Load both question-answering and summarization models
def load_models():
    # Load a small model for question-answering
    qa_model_name = 'distilbert-base-uncased-distilled-squad'
    qa_pipeline = pipeline('question-answering', model=qa_model_name)

    # Load a model for summarization
    summarization_model_name = 't5-small'
    summarizer = pipeline('summarization', model=summarization_model_name)
    
    return qa_pipeline, summarizer

# Step 3: Function to handle different types of questions
def handle_questions(qa_pipeline, summarizer, text):
    while True:
        question = input("Enter your question (or type 'exit' to quit): ")
        if question.lower() == 'exit':
            print("Exiting.")
            break
        
        if "explain" in question.lower() or "about" in question.lower():
            # Use summarization for open-ended questions
            summary = summarizer(text, max_length=50, min_length=30, do_sample=False)
            print(f"Answer: {summary[0]['summary_text']}\n")
        else:
            # Use QA model for specific questions
            answer = qa_pipeline(question=question, context=text)
            print(f"Answer: {answer['answer']}\n")

# Step 4: Main function to scrape and ask questions
def get_company_details(url):
    # Scrape the content
    scraped_text = scrape_website(url)
    
    if len(scraped_text.strip()) == 0:
        print("No content found to process.")
        return
    
    # Load the local LLM models (QA + Summarization)
    qa_pipeline, summarizer = load_models()
    
    # Allow manual question asking
    handle_questions(qa_pipeline, summarizer, scraped_text)

# Test with any company URL
url = "https://www.kern.ai/"
get_company_details(url)
