import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st

# Streamlit app function
def scrape_books(url):
    current_page = 1
    data = []
    proceed = True

    while proceed:
        st.write(f"Currently scraping page: {current_page}")
        
        # Update the URL dynamically based on the current page number
        page_url = f"{url}/catalogue/page-{current_page}.html"

        page = requests.get(page_url)
        soup = BeautifulSoup(page.text, "html.parser")

        # If the page doesn't exist, stop the loop
        if "404 Not Found" in soup.title.text:
            proceed = False
        else:
            # Scrape all books from the current page
            all_books = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
            for book in all_books:
                item = {}
                item['Title'] = book.find("img").attrs["alt"]
                item['Link'] = book.find("a").attrs["href"]
                item['Price'] = book.find("p", class_="price_color").text[2:]  # Skip the currency symbol
                item['Stock'] = book.find("p", class_="instock availability").text.strip()
                data.append(item)

        current_page += 1

    return pd.DataFrame(data)

# Streamlit UI
st.title("Book Scraper")

# Input URL
url = st.text_input("Enter the base URL to scrape")

# If a URL is provided, scrape the data
if url:
    df = scrape_books(url)
    
    # Display the scraped data
    st.write("Scraped Data:")
    st.dataframe(df)

    # Provide a download link for the Excel file
    if not df.empty:
        df.to_excel("books.xlsx", index=False)
        with open("books.xlsx", "rb") as file:
            st.download_button(label="Download Excel file", data=file, file_name="books.xlsx", mime="application/vnd.ms-excel")
