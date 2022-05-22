import requests
import os
import time

class ImageHandler():

    def __init__(self):
        self.folder_name = "images"

    # Method for checking if folder exists, if it doesn't, create it.
    def check_folder(self, subfolder = None):
        if not os.path.exists(self.folder_name):
            os.makedirs(self.folder_name)

        if subfolder:
            if not os.path.exists(f"{self.folder_name}/{subfolder}"):
                os.makedirs(f"{self.folder_name}/{subfolder}")

    # Method for checking if image exists.
    def check_image(self, image_name, subfolder = None):

        if subfolder:
            if os.path.exists(f"{self.folder_name}/{subfolder}/{image_name}.jpg"):
                return True
            else:
                return False
        else:
            if os.path.exists(f"{self.folder_name}/{image_name}.jpg"):
                return True
            else:
                return False

    # Method for downloading an image from a URL.
    def download_image(self, image_url, image_name, subfolder = None):

        # Check if folder exists, if not, create it.
        self.check_folder(subfolder)

        # Check if image exists, if not, download it.
        if not self.check_image(image_name, subfolder):

            # Download image from URL.
            img_data = self.get_website_content(image_url).content

            if subfolder:
                image_path = f"{self.folder_name}/{subfolder}/{image_name}.jpg"
            else:
                image_path = f"{self.folder_name}/{image_name}.jpg"

            with open(image_path, 'wb') as handler:
                handler.write(img_data)

            return True
        else:
            return False

    def get_website_content(self, url):
        response = requests.get(url)

        # Recursive if 503.
        if response.status_code == 503:
            
            # Wait for a while.
            print("503 error, trying again...", end = '')
            time.sleep(5)

            response = self.get_website_content(url) # This fucks up. I don't think the recursive works just right yet.

        return response