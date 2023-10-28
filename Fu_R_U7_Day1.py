import PIL
from PIL import Image
import urllib.request
import io, sys
#print (PIL.PILLOW_VERSION)
# URL = &#39;http://www.w3schools.com/css/trolltunga.jpg&#39;
# #URL = sys.argv[1]
# f = io.BytesIO(urllib.request.urlopen(URL).read())
import tkinter as tk
from PIL import Image, ImageTk # Place this at the end (to
window = tk.Tk()
#window.geometry(&quot;500x500&quot;) # (optional)
imagefile = "cute_dog.jpg"
img = ImageTk.PhotoImage(Image.open(imagefile))
lbl = tk.Label(window, image = img).grid(row = 0, column = 0)
img2 = Image.open(imagefile)
print (img2.size) # a tuple of (# of rows, # of cols)
pix = img2.load()
print (pix[2, 5]) # a tuple of (r, g, b)
def chrome(color):
    if color < (255 // 3): return 0
    elif color > (255 // 3 * 2) and color < 255: return 255
    else: return 127

for x in range(img2.size[0]):
    for y in range(img2.size[1]):
        r, g, b = pix[x, y]
        pix[x, y] = (chrome(r), chrome(g), chrome(b))
#img2.show()
def negate(color):
    return 255-color
img3 = ImageTk.PhotoImage(img2)
lbl2 = tk.Label(window,image = img3).grid(row = 1, column= 0)
img4 = Image.open(imagefile)
pix2 = img4.load()
for x in range(img4.size[0]):
    for y in range(img4.size[1]):
        r,g,b = pix2[x,y]
        pix2[x,y] = (negate(r),negate(g),negate(b))
img5 = ImageTk.PhotoImage(img4)
lbl3 = tk.Label(window,image = img5).grid(row=0,column=1)
img6 = Image.open(imagefile)
pix3 = img6.load()
def sepia(R,G,B):
    mean = (R+G+B)//3
    newR = newG = newB = mean
    return newR, newG, newB
for x in range(img6.size[0]):
    for y in range(img6.size[1]):
        r,g,b = pix3[x,y]
        pix3[x,y] = sepia(r,g,b)
img7 = ImageTk.PhotoImage(img6)
lbl4 = tk.Label(window,image = img7).grid(row = 1, column=1)
# img3 = Image.open(imagefile)
# pix3 = img3.load()
# for x in range(img3.size[0]):
#     for y in range(img3.size[1]):
#         r, g, b = pix3[x,y]
#         pix3[x,y] = (negate(r),negate(g),negate(b))
# lbl2 = tk.Label(window, image = img3).pack()
# img4 = ImageTk.PhotoImage(img2)
# lbl3 = tk.Label(window,image=img4).pack()

window.mainloop()