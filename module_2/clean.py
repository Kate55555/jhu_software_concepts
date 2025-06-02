from bs4 import BeautifulSoup
import json
import re

class Clean:    

    def load_data(self, filename: str) -> list:
        """
        Load data from html file
        """
        # Open a file for reading
        f = open(filename, "rb+")

        # Read the entire file into a bin string
        file = f.read()

        # Load file binary data to Beautiful soup
        soup = BeautifulSoup(file, "html.parser")

        f.close()

        # Find all table rows that represent uni name and other info
        return soup.find_all("tr", class_=None)


    def clean_data(self, prefix: str, ext: str, n: int): 
        """
        Convert data into structured format

        :param prefix: a name of a file prefix to read
        :param ext: a file extension to read
        :param n: a number fo files to read
        :return: None
        """
        clean_list =[]  # A nested list of universitioes with details

        for i in range(1, n+1):
            # Load data from a file
            filename = "module_2/html/" + prefix + str(i) + ext
            trows = self.load_data(filename)

            # Loop through the rows (universities) and find related info
            for row in trows:
                temp_dict = {}  # A dictionary to collect specific uni info
                
                # Get data from the first row where we find uni name
                row_title = row.text.strip()

                # If the first row contains some data
                if (row_title != ""):
                    # Split into meaningful elements
                    temp_split = row_title.split("\n")

                    # Clean elements and add non-empty values
                    clean_split = self._clean_list(temp_split)
                    try:
                        temp_dict["program"] = clean_split[1] + ", " + clean_split[0]
                        temp_dict["Degree"] = clean_split[2]
                        temp_dict["date_added"] = "Added on " + clean_split[3]
                        temp_dict["status"] = clean_split[4]
                    except:
                        temp_dict["program"] = clean_split[0]
                        temp_dict["Degree"] = clean_split[1]
                        temp_dict["date_added"] = "Added on " + clean_split[2]
                        temp_dict["status"] = clean_split[3]

                    # Get a link to applicant entry - within row
                    url_link = row.find("a").attrs["href"]
                    temp_dict["url"] = "https://www.thegradcafe.com" + url_link

                    # Get the next sibling - we know it always exists in the markup
                    next_sibling = row.next_sibling

                    # Split into meaningful elements
                    temp_split = next_sibling.text.strip().split("\n")

                    # Add additional details about the uni
                    clean_split = self._clean_list(temp_split)
                    temp_dict["term"] = clean_split[1]
                    temp_dict["US/Internaional"] = clean_split[2]

                    # Add GRE, GRE V, GRE AW, GPA if available
                    pattern = re.compile(
                        r"^(?:(?P<GRE_plain>GRE\ \d+)|"
                        r"(?P<GRE_V>GRE\ V\ .+)|"
                        r"(?P<GRE_AW>GRE\ AW\ .+)|"
                        r"(?P<GPA>GPA\ \d+\.\d+))$"
                    )
                    for score in clean_split:
                        m = pattern.match(score)
                        if m:
                            if m.group("GRE_plain"):
                                temp_dict["GRE"] = score
                            if m.group("GRE_V"):
                                temp_dict["GRE V"] = score
                            if m.group("GRE_AW"):
                                temp_dict["GRE AW"] = score
                            if m.group("GPA"):
                                temp_dict["GPA"] = score

                    # Comments are optional, so we check if we can get them
                    next_next_sibling = next_sibling.next_sibling

                    # If there are comments, the row would have a class specified
                    if (next_next_sibling.attrs != {} 
                        and next_next_sibling.attrs["class"] == ["tw-border-none"]):
                        # Add comments to the uni info
                        temp_dict["comments"] = next_next_sibling.text.strip()
                    
                    # Add all available uni details to a nested list
                    clean_list.append(temp_dict)
            
        return clean_list


    def _clean_list(self, dirty_list: list) -> list:
        """
        Clean a list from the phrases that do not matter to us.

        :param dirty_list: A list to be cleaned.
        :return: A list that excludes meaningless phrases.
        """
        # A list of not very useful words
        rubbish = ["", "Total comments", "Open options", "See More", "Report"]
        clean_list = []

        for element in dirty_list:
            cleany = element.strip()
            if (cleany not in rubbish):
                # Add the data to the clean list
                clean_list.append(cleany)
        
        return clean_list


    def save_data(self, gradcafe: list): 
        """
        Save the cleaned data into a json file 'applicant_data.json'
        """
        f = open("module_2/applicant_data.json", "r+")

        gradcafe_json = json.dumps(gradcafe)
        f.write(gradcafe_json)
        f.close()
        
