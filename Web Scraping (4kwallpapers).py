import requests
import bs4
from time import sleep

def download_Image(urlContent, path):
    with open(path, "wb") as file:
            file.write(urlContent)

total_images = 0

for page in range(1, 15):
    try:
        website_link = f"https://4kwallpapers.com/anime/?page={page}"
        website = requests.get(website_link)
        print(f"Link: {website_link} Page: {page}")
    except Exception:
        break
    html = website.text

    html_parser = bs4.BeautifulSoup(html, "html.parser")
    finds = html_parser.findAll("img", attrs={"itemprop": "thumbnail"})

    for find in finds:
        try:
            start = str(find).index("https://4kwallpapers.com/images/walls/thumbs/") + 45
        except ValueError:
            try:
                start = str(find).index("https://4kwallpapers.com/images/walls/thumbs_2t/") + 48
            except ValueError:
                start = str(find).index("https://4kwallpapers.com/images/walls/thumbs_uwide/") + 51
        try:
            end = str(find).index("jpg")
            linkTitle = str(find)[start: end + 3]
        except ValueError:
            try:
                end = str(find).index("png")
                linkTitle = str(find)[start: end + 3]
            except ValueError:
                end = str(find).index("jpeg")
                linkTitle = str(find)[start: end + 4]

        link = "https://4kwallpapers.com/images/walls/thumbs_3t/" + linkTitle

        imageContent = requests.get(link).content

        titleStart = str(find).index("alt=")
        titleEnd = str(find).index("\" ")
        title = str(find)[titleStart + 5: titleEnd].strip().replace(", ", "_").replace(" ", "-").replace(":", "_")

        x = linkTitle.split(".")
        imageCode = x[0]
        fileExtension = "." + x[1]

        imagePath = "C:\\Users\\[User]\\Pictures\\Wallpapers\\Anime\\" + title + fileExtension

        download_Image(imageContent, imagePath)

        total_images += 1
        print(f"{total_images}: image {imageCode} Downloaded successful as {title}{fileExtension}")
    sleep(0.5)

print(f"{total_images} images downloaded")