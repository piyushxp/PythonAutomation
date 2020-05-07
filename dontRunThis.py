from PIL import Image,ImageFilter

img = Image.open('./Source/picture.jpg')

# filtered_img = img.convert('L')
# # print(img.format)
# # print(img.mode)
# # print(img.)
# resize = filtered_img.resize((300,300))
# filtered_img.rotate(90)
# resize.save("grey.png","png")


print(img.size)
img.thumbnail((400,400))
img.save("thumbnail.png","png")