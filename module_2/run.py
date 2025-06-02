from scrape import Scrape
from clean import Clean

if __name__ == "__main__":
    # URL to scrape data from
    url = "https://www.thegradcafe.com"

    # Data file name prefix and extension
    filename = "html_"
    extension = ".txt"

    # Formatted file name
    output = "applicant_data.json"

    # Number of grad applicant entries per page
    m = 20

    # Number of grad applicant entries to scrape 
    n = 10000 // m + 1

    # Uncomment the line below for Web scraping
    # Scrape().scrape_data(url, n)

    # Extract pretty data to json
    grad_info = Clean().clean_data(filename, extension, n)
    Clean().save_data(grad_info)