from PIL import Image, ImageDraw, ImageFont

with open('daftarnama.txt', 'r') as f:
    nama = f.read().split('\n')

for name in nama:
    # open the image file
    img = Image.open("base.jpg")

    # create a draw object to draw on the image
    draw = ImageDraw.Draw(img)

    # use a font to draw the text
    font = ImageFont.truetype("Montserrat-Bold.ttf", 36)

    # get the size of the text
    text_size = draw.textsize(name, font)

    # calculate the position of the text so it is centered
    text_x = (img.width - text_size[0]) / 2
    text_y = (img.height - text_size[1]) / 2

    # draw the text on the image with navy color
    draw.text((text_x, 310), name, (0, 0, 128), font=font)

    # save the image
    # img.show()
    img.save('output/' + name + ".jpg")
    print("Berhasil untuk " + name)
