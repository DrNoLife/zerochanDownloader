from bs4 import BeautifulSoup
import requests

class WebHandler():

    def __init__(self, url):
        self.website_url = url

    def get_image_information(self, max_page = 1):

        print("Getting image information...")

        result = []

        # Iterate through the pages.
        for page_number in range(1, max_page + 1):

            print(f"\tCurrent page: {page_number} / {max_page}")

            # Get the website content.
            website_html = requests.get(self.website_url + str(page_number)).text
            soup = BeautifulSoup(website_html, features="html.parser")

            # Find ul with id of "thumbs2" and iterate through all its content. 
            thumbs_ul = soup.find(id = 'thumbs2')
            

            for li in thumbs_ul.find_all('li'):

                # Skip if li has no class.
                if not li.has_attr('class'):
                    continue

                all_a_tags_inside_p = li.find('p').find_all('a')

                # Get the information that we need.
                image_id = li.find('a').get('href').replace('/', '')
                image_url = all_a_tags_inside_p[1].get('href')
                image_name = all_a_tags_inside_p[0].text

                # Add the information to the result list.
                result_dict = {
                    'image_id': image_id,
                    'image_name': image_name,
                    'image_url': image_url,
                }
                result.append(result_dict)  

        print("Done.\n\n")
        return result