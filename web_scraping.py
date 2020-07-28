# Downloading images from google search for datasets using python script - Web Scraping Hack
from google_images_download import google_images_download
response = google_images_download.googleimagesdownload()
arguments = {"keywords":"Crops", "limit":9,'print_urls':True}
paths = response.download(arguments)
print(paths)