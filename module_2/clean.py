from bs4 import BeautifulSoup

class Clean:    

    def load_data(self):
        """
        Load data from html file
        """
        f = open()
        pass

    def clean_data(self, prefix: str, ext: str, n: int): 
        """
        Convert data into structured format

        :param prefix: a name of a file prefix to read
        :param ext: a file extension to read
        :param n: a number fo files to read
        :return: None
        """
        dirty_list =[]  # A nested list of universitioes with details

        for i in range(1, n+1):
            filename = "module_2/html/" + prefix + str(i) + ext
            
            # Open a file for reading
            f = open(filename, "rb+")

            # Read the entire file into a bin string
            file = f.read()

            # Load file binary data to Beautiful soup
            soup = BeautifulSoup(file, "html.parser")

            # Find all table rows that represent uni name and other info
            trows = soup.find_all("tr", class_=None)

            # Loop through the rows (universities) and find related info
            for row in trows:
                temp_list = []  # A list to collect specific uni info
                
                # Get data from the first row where we find uni name
                row_title = row.text.strip()

                # If the first row contains some data
                if (row_title != ""):
                    # Add the data to the temp list
                    temp_list.append(row_title)

                    # Get the next sibling - we know it always exists in the markup
                    next_sibling = row.next_sibling

                    # Add additional details about the uni
                    temp_list.append(next_sibling.text.strip())

                    # Comments are optional, so we check if we can get them
                    next_next_sibling = next_sibling.next_sibling

                    # If there are comments, the row would have a class specified
                    if (next_next_sibling.attrs != {} 
                        and next_next_sibling.attrs['class'] == ['tw-border-none']):
                        # Add comments to the uni info
                        temp_list.append(next_next_sibling.text.strip())
                    
                    # Add all availbale uni details to a nested list
                    dirty_list.append(temp_list)
            pass


    def save_data(self): 
        """
        Save cleaned data into a json file 'applicant_data.json'
        """
        pass