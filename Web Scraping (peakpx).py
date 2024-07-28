import requests
import bs4

total_images = 0

for page in range(1, 15):
    website_link = f"https://www.peakpx.com/en/search?q=Games&device=2&page={page}"
    website = requests.get(website_link)
    print(f"Link: {website_link}")
    html = website.text

    html_parser = bs4.BeautifulSoup(html, "html.parser")
    finds = html_parser.findAll("link", attrs={"itemprop": "contentUrl"})

    def download_Image(url, path):
        with open(path, "wb") as file:
                file.write(url)

    for find in finds:
        linkStart = str(find).index("https")
        linkEnd = str(find).index("jpg")
        imageLink = str(find)[linkStart:linkEnd + 3]
        imageContent = requests.get(imageLink).content

        titleStart = str(find).index("HD-wallpaper")
        titleEnd = str(find).index("jpg")
        imageTitle = str(find)[titleStart + 13:titleEnd + 3]
        
        imagePath = "C:\\Users\\[Users]\\Pictures\\Wallpapers\\Games\\" + imageTitle

        download_Image(imageContent, imagePath)
        
        total_images += 1
        print(f"{total_images}: image Downloaded successful as {imageTitle}")