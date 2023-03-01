# CMPT 120 Yet Another Image Processer
# Starter code for cmpt120imageManip.py
# Date: December 1, 2021
# Description: Image Processor Final Project

from cmpt120imageProjHelper import getBlackImage, rgb_to_hsv


# Basic 1: Red Filter
def redFilter(pixels):
    height = len(pixels)
    width = len(pixels[0])

    for row in range(height):
        for col in range(width):
            pixels[row][col][1] = 0
            pixels[row][col][2] = 0

    return pixels


# Basic 2: Green Filter
def greenFilter(pixels):
    height = len(pixels)
    width = len(pixels[0])

    for row in range(height):
        for col in range(width):
            pixels[row][col][0] = 0
            pixels[row][col][2] = 0

    return pixels


# Basic 3: Blue Filter
def blueFilter(pixels):
    height = len(pixels)
    width = len(pixels[0])

    for row in range(height):
        for col in range(width):
            pixels[row][col][0] = 0
            pixels[row][col][1] = 0

    return pixels


# Basic 4: Sepia Filter
def sepiaFilter(pixels):
    height = len(pixels)
    width = len(pixels[0])

    for row in range(height):
        for col in range(width):
            pixel = pixels[row][col]

            red, green, blue = pixel[0], pixel[1], pixel[2]

            sepiaRed = (red * 0.393) + (green * 0.769) + (blue * 0.189)
            sepiaGreen = (red * 0.349) + (green * 0.686) + (blue * 0.168)
            sepiaBlue = (red * 0.272) + (green * 0.534) + (blue * 0.131)

            # Use min to convert sepia > 255 to 255
            minSepiaRed = min(int(sepiaRed), 255)
            minSepiaGreen = min(int(sepiaGreen), 255)
            minSepiaBlue = min(int(sepiaBlue), 255)

            pixels[row][col][0] = minSepiaRed
            pixels[row][col][1] = minSepiaGreen
            pixels[row][col][2] = minSepiaBlue

    return pixels


# Define scale up and scale down functions to use in warm and cold filters
def scaleUp(value):
    if value < 64:
        scaledUpValue = value / (64 * 80)

    elif 64 <= value and value < 128:
        scaledUpValue = (value - 64) / (128 - 64) * (160 - 80) + 80

    else:
        scaledUpValue = (value - 128) / (255 - 128) * (255 - 160) + 160

    return int(scaledUpValue)


def scaleDown(value):
    if value < 64:
        scaledDownValue = value / (64 * 50)

    elif 64 <= value and value < 128:
        scaledDownValue = (value - 64) / (128 - 64) * (100 - 50) + 50

    else:
        scaledDownValue = (value - 128) / (255 - 128) * (255 - 100) + 100

    return int(scaledDownValue)


# Basic 5: Warm Filter
def warmFilter(pixels):
    height = len(pixels)
    width = len(pixels[0])

    for row in range(height):
        for col in range(width):
            red = pixels[row][col][0]
            blue = pixels[row][col][2]

            warmRed = scaleUp(red)
            warmBlue = scaleDown(blue)

            pixels[row][col][0] = warmRed
            pixels[row][col][2] = warmBlue

    return pixels


# Basic 6: Cold Filter
def coldFilter(pixels):
    height = len(pixels)
    width = len(pixels[0])

    for row in range(height):
        for col in range(width):
            pixel = pixels[row][col]

            red = pixel[0]
            blue = pixel[2]

            coldBlue = scaleUp(blue)
            coldRed = scaleDown(red)

            pixel[0] = coldRed
            pixel[2] = coldBlue

    return pixels


# Advanced 1: Rotate Left
def rotateLeft(pixels):
    height = len(pixels)
    width = len(pixels[0])

    result = getBlackImage(height, width)

    for row in range(height):
        for col in range(width):
            result[-col][row] = pixels[row][col]

    return result


# Advanced 2: Rotate Right
def rotateRight(pixels):
    height = len(pixels)
    width = len(pixels[0])

    result = getBlackImage(height, width)

    for row in range(height):
        for col in range(width):
            result[col][row] = pixels[-row][col]

    return result


# Advanced 3: Double Size
def doubleSize(pixels):
    height = len(pixels)
    width = len(pixels[0])

    result = getBlackImage(width * 2, height * 2)

    for row in range(height):
        for col in range(width):
            pixel = pixels[row][col]

            result[row * 2][col * 2] = pixel
            result[(row * 2) + 1][col * 2] = pixel
            result[row * 2][(col * 2) + 1] = pixel
            result[(row * 2) + 1][(col * 2) + 1] = pixel

    return result


# Advanced 4: Half Size
def halfSize(pixels):
    height = len(pixels)
    width = len(pixels[0])

    result = getBlackImage(width // 2, height // 2)

    for row in range(height // 2):
        for col in range(width // 2):

            # In every 2x2 block of pixels define each
            firstPixel = pixels[row * 2][col * 2]
            secondPixel = pixels[(row * 2) + 1][col * 2]
            thirdPixel = pixels[row * 2][(col * 2) + 1]
            fourthPixel = pixels[(row * 2) + 1][(col * 2) + 1]

            red = firstPixel[0] + secondPixel[0] + thirdPixel[0] + fourthPixel[0]
            green = firstPixel[1] + secondPixel[1] + thirdPixel[1] + fourthPixel[1]
            blue = firstPixel[2] + secondPixel[2] + thirdPixel[2] + fourthPixel[2]

            result[row][col][0] = red // 4
            result[row][col][1] = green // 4
            result[row][col][2] = blue // 4

    return result


# Advanced 5: Locate Fish
def locateFish(pixels):
    height = len(pixels)
    width = len(pixels[0])
    result = getBlackImage(width, height)

    # record all instances of yellow
    yellowRows = []
    yellowCols = []

    for row in range(height):
        for col in range(width):

            result[row][col] = pixels[row][col]
            pixel = result[row][col]

            # convert rgb values to hsv values
            r,g,b = pixel[0],pixel[1],pixel[2]
            h,s,v = rgb_to_hsv(r, g, b)

            # find all instances of yellow pixels on fish and add to list
            if (48 < h < 74) and s > 40 and v > 55:
                yellowRows.append(row)
                yellowCols.append(col)

    # find the top most and bottom most row and col that it appears on
    topRow, bottomRow = min(yellowRows), max(yellowRows)
    topCol, bottomCol = min(yellowCols), max(yellowCols)

    return topRow, bottomRow, topCol, bottomCol

def makeGreenBox(pixels, topRow, bottomRow, topCol, bottomCol):
    for row in range(topRow, bottomRow):
        pixels[row][topCol] = [0, 255, 0]

    for row in range(topRow, bottomRow):
        pixels[row][bottomCol] = [0, 255, 0]

    for row in pixels[topRow]:
        for col in range(topCol, bottomCol):
            pixels[topRow][col] = [0, 255, 0]

    for row in pixels[bottomRow]:
        for col in range(topCol, bottomCol):
            pixels[bottomRow][col] = [0, 255, 0]
