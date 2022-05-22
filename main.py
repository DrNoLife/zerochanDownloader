from ImageHandler import ImageHandler
from WebHandler import WebHandler


# Get image information from website.
website_url = f"https://www.zerochan.net/Nekomimi?p="
webHandler = WebHandler(website_url)
images = webHandler.get_image_information(max_page = 7) # max_page max value is currently 100, due to fuckery on the website.

# Download images.
imageHandler = ImageHandler()
total_image_count = len(images)
loop_counter = 1

for image in images:

    print(f"[{loop_counter} / {total_image_count}] Downloading image: {image['image_name']}", end=' - ')

    full_name = image['image_name'] + '#' + image['image_id']
    result = imageHandler.download_image(image['image_url'], full_name, subfolder = "neko")

    if result:
        print(f"Downloaded.")
    else:
        print(f"Already exists.")

    loop_counter += 1