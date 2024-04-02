import os
from PIL import Image


im = Image.new("RGBA", (200, 185), "white")

logo = Image.open("transparent.png")


for filename in os.listdir("flags"):
    flag = Image.open("flags\\" + filename)

    end_logo = im.copy()
    end_logo.paste(flag, (0, 8))
    end_logo.paste(logo, (0, 0), mask = logo)

    end_logo.save("done\\" + filename)
