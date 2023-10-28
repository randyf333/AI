import PIL
from PIL import Image
import urllib.request
import io, sys
print(PIL.PILLOW_VERSION)
f = sys.argv[1]
#f = io.BytesIO(urllib.request.urlopen(https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.shutterstock.com%2Fsearch%2Fapple&psig=AOvVaw3VaoK5V-CufZb0Qzawtknm&ust=1630156020500000&source=images&cd=vfe&ved=0CAgQjRxqFwoTCJDGpsai0fICFQAAAAAdAAAAABAJ).read())
img = Image.open(f)
print (img.size)
pix = img.load()
print (pix[2,5])
img = img.show()
