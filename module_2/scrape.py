import requests
from bs4 import BeautifulSoup

class Scrape:
    """
    The class is to scrape all the data from Gradcafe and then saved it
    """

    def scrape_data(self, url: str, n: int):
        """
        Pull data from grad cafe
        """
        filename = "html_"
        for i in range(1,n+1):
            page = requests.get(url + "/survey/?page=" + str(i))
            soup = BeautifulSoup(page.content, "html.parser")
            results = soup.find("tbody").find_all("tr")
            self.save_data(filename + str(i), results)


    def save_data(self, filename: str, data: list):
        """
        Save data to html
        """
        filepath = "module_2/html/1" + filename + ".txt" 
        with open(filepath, "w", encoding="utf-8") as f:
            for datum in data:
                f.write(f"{datum}")
        f.close()
