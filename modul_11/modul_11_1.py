from PIL import Image
from urllib.request import urlopen
from PIL import ImageFilter


url = 'https://img3.procvetok.com/crop/w500h500/32/a0/32a074858cfe875cb16d47a91e7d3c93.jpg'
try:
    with Image.open(urlopen(url)) as img:
        file = img.filter(ImageFilter.CONTOUR).resize((250, 250))
        file = file.rotate(45)
        file.show()
        file.save('arbuz.png')
except Exception as exc:
    print(exc)
