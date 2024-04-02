import requests, bs4, os

url = "https://www.countries-ofthe-world.com/flags-of-the-world.html"
os.makedirs("flags", exist_ok = True)


res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})


soup = bs4.BeautifulSoup(res.text, "html.parser")


flags = soup.find_all("img")

for flag in flags:
    src = flag.get("src")
    if src.startswith("flags-normal/flag-of"):
        res = requests.get("https://www.countries-ofthe-world.com/" + src, headers={'User-Agent': 'Mozilla/5.0'})

        imageFile = open(os.path.join("flags", os.path.basename(src[len("flags-normal/flag-of-"):])), "wb")
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close

print("Done")
