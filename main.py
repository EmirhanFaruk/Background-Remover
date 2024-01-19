
# Modification date: Wed Sep 15 23:03:34 2021

# Production date: Sun Sep  3 15:42:51 2023

from PIL import Image

image_input = str(input("Enter the name of the image: "))

#img = Image.open(image_input + ".png")
#widthi, heighti = img.size

#image = Image.open("EmptyImage.png")

crl = int(input("Enter the least red value of the background(r of rgb): "))
crm = int(input("Enter the most red value of the background(r of rgb): "))

cgl = int(input("Enter the least green value of the background(g of rgb): "))
cgm = int(input("Enter the most green value of the background(g of rgb): "))

cbl = int(input("Enter the least blue value of the background(b of rgb): "))
cbm = int(input("Enter the most blue value of the background(b of rgb): "))


img = Image.open(image_input + ".png")
img = img.convert("RGBA")
datas = img.getdata()

newData = []
for item in datas:
    if item[0] <= crm and item[0] >= crl and item[1] <= cgm and item[1] >= cgl and item[2] <= cbm and item[2] >= cbl:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

"""
for i in range(widthi):
    for j in range(heighti):
        px = image.getpixel((i, j))
        if not(px == (cr, cg, cb)):
            img.putpixel ((i, j), px)
"""

image_name = str(input("Enter the new image's name: "))



img.putdata(newData)
new_img_name = image_name + ".png"
img.save(new_img_name,"png")
print(new_img_name + " saved!")

img.show()

input("To quit, press Enter...")


