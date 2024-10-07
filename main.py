from PIL import Image


def convertImage():
    imagePath = "F:\\Docs\\priyanka_sign_clean.png"
    outputImgPath ="F:\\Docs\\_pri_sign_transparent_3.png"
    img = Image.open(imagePath)
    img = img.convert("RGBA")

    data = img.getdata()

    newData = []

    colorToRemove = 200

    for item in data:
        if item[0] >= colorToRemove and item[1] >= colorToRemove and item[2] >= colorToRemove:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save(outputImgPath, "PNG")
    print("Successful")


convertImage()
