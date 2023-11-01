# Sarah Ma
# Project 2 - Image Processing

from PIL import Image, ImageFilter
import numpy as np


def main():
    # Change the path in Line 6 to the path of the image you want to use as input 
    # for Windows users the path specify the path as "c:\\users\\alark1\\Pictures\\usfca.png"
    inputImage = Image.open('C:\\Desktop\\CS 110\\project2\\usfca.png')
    imageWidth, imageHeight = inputImage.size
    copyImage(inputImage, imageWidth, imageHeight)

    # Display the menu
    display_menu(inputImage, imageWidth, imageHeight)

# Creates a copy of an image given the image variable, its width, and height
def copyImage(inputImage, imageWidth, imageHeight):
    copyImageOutput = Image.new('RGB', (imageWidth, imageHeight), 'white')

    for i in range(imageWidth):
        for j in range(imageHeight):
            pixelColors = inputImage.getpixel((i, j))
            copyImageOutput.putpixel((i, j), pixelColors)

    copyImageOutput.save('copy.png')

# Part 1

# Displays the menu, for part one there are 3 options: flip vertical, find pattern. and make grayscale 
def display_menu(inputImage, imageWidth, imageHeight):
    print('Menu: \n 1. Flip Vertical \n 2. Find Pattern \n 3. Make Grayscale \n 4. Rotate \n 5. Swap Corners \n 6. Blur \n 7. Sharpen \n 8. Edge Detection \n 9. Scale Larger \n 10. Exit')
    # Input validation
    while True:    
        try:
            user_choice = int(input('Choose an option (1-10): '))
            if 1 <= user_choice <= 10:
                break
            else:
                print('Please enter a number between 1 and 10.')
        except ValueError:
            print('Please enter a valid integer.')

    if user_choice == 1:
        flip_vertical(inputImage, imageWidth, imageHeight)
    elif user_choice == 2:
        find_pattern()
    elif user_choice == 3:
        make_grayscale(inputImage, imageWidth, imageHeight)
    elif user_choice == 4:
        rotate(inputImage, imageWidth, imageHeight)
    elif user_choice == 5:
        swap_corners(inputImage, imageWidth, imageHeight)
    elif user_choice == 6:
        blur(inputImage, imageWidth, imageHeight)
    elif user_choice == 7:
        sharpen_image()
    elif user_choice == 8:
        edge_detection(inputImage, imageWidth, imageHeight)
    elif user_choice == 9:
        factor = int(input('Enter scale factor: '))
        scale_larger(inputImage, imageWidth, imageHeight, factor)
    else:
        print('Exiting program.')

# Function to flip the image vertical
def flip_vertical(inputImage, imageWidth, imageHeight):
    # Create a new image with the same dimensions
    flippedImage = Image.new('RGB', (imageWidth, imageHeight), 'white')

    # Iterate through the original image's pixels
    for width in range(imageWidth):
        for height in range(imageHeight):
            # Get the pixel color from the original image but flipped vertically
            pixelColors = inputImage.getpixel((width, -height))

            # Set the corresponding pixel in the flipped image
            flippedImage.putpixel((width, height), pixelColors)

    # Save the flipped image to a file called 'copy.png'
    flippedImage.save('C:\\Desktop\\CS 110\\project2\\vertical-flip.png')
    print("Image successfully flipped vertically and saved as 'vertical-flip.png'")

# Function to find pattern
def find_pattern():
    inputImage = Image.open('C:\\Desktop\\CS 110\\project2\\red-image.png')
    imageWidth, imageHeight = inputImage.size

    # Create a new image with the same dimensions
    resultsImage = Image.new('RGB', (imageWidth, imageHeight), 'white')

    # Iterate through the original image's pixels
    for width in range(imageWidth):
        for height in range(imageHeight):
            pixelColors = inputImage.getpixel((width, height))
            
            # If the pixel is more red than blue and green then...
            if pixelColors[0] > pixelColors[1] and pixelColors[0] > pixelColors[2]:
                # Set the color to white
                newColors = (255, 255, 255)
            else:
                # Else keep it the same color
                newColors = pixelColors

            # Set the corresponding pixel with it's new color that it was assigned in the if else loop
            resultsImage.putpixel((width, height), newColors)

    # Save the mystery image to a file called 'mystery-solved.png'
    resultsImage.save('mystery-solved.png')
    print("Mystery pattern found and saved as 'mystery-solved.png'")

# Function to make image grayscale
def make_grayscale(inputImage, imageWidth, imageHeight):
    # Create a new image with the same dimensions
    grayscaleImage = Image.new('RGB', (imageWidth, imageHeight), 'white')

    # Iterate through the original image's pixels
    for width in range(imageWidth):
        for height in range(imageHeight):
            # Get the pixel color from the original image
            pixelColors = inputImage.getpixel((width, height))

            # Calculate grayscal value using the average
            grayValue = int(0.3 * pixelColors[0] + 0.59 * pixelColors[1] + 0.11 * pixelColors[2])
            # Set a variable to the gray RGB color of the averages
            grayPixel = (grayValue, grayValue, grayValue)

            # Set the current pixel's RGB to the gray pixel value
            grayscaleImage.putpixel((width, height), grayPixel)

    # Save the grayscale image as 'grayscale.png'
    grayscaleImage.save('grayscale.png')
    print("Image converted to grayscale and saved as 'grayscale.png'")

# Part 2

def rotate(inputImage, imageWidth, imageHeight):
    rotatedWidth, rotatedHeight = imageHeight, imageWidth
    rotatedImage = Image.new('RGB', (rotatedWidth, rotatedHeight), 'white')
    for width in range(imageWidth):
        for height in range(imageHeight):
            pixelColors = inputImage.getpixel((width, height))
            rotatedImage.putpixel((height, rotatedHeight - width - 1), pixelColors)

    rotatedImage.save('rotate.png')
    print("Image rotated 90 degrees clockwise and saved as 'rotate.png'") 

def swap_corners(inputImage, imageWidth, imageHeight):
    swappedCornersImage = Image.new('RGB', (imageWidth, imageHeight), 'white')

    # Quadrant 1
    for width in range(imageWidth):
        for height in range(imageHeight):
            pixelColors = inputImage.getpixel((width, height))

            if width < imageWidth / 2 and height < imageHeight / 2:
                newWidth = width + imageWidth // 2
                newHeight = height + imageHeight // 2

            elif width >= imageWidth / 2 and height < imageHeight / 2:
                newWidth = width - imageWidth // 2
                newHeight = height + imageHeight // 2

            elif width < imageWidth / 2 and height >= imageHeight / 2: 
                newWidth = width + imageWidth // 2
                newHeight = height - imageHeight // 2

            elif width >= imageWidth / 2 and height >= imageHeight / 2:
                newWidth = width - imageWidth // 2
                newHeight = height - imageHeight // 2            

            swappedCornersImage.putpixel((newWidth, newHeight), pixelColors)


    swappedCornersImage.save('cornerswap.png')
    print("Image swapped corners and saved as 'cornerswap.png")

def blur(inputImage, imageWidth, imageHeight):
    blurredImage = Image.new('RGB', (imageWidth, imageHeight), 'white')

    for width in range(imageWidth):
        for height in range(imageHeight):
            redSum = 0
            greenSum = 0
            blueSum = 0
            count = 0

            for row in range(max(0, width - 1), min(imageWidth, width +2)):
                for  col in range(max(0,height - 1), min(imageHeight, height + 2)):
                    pixelColors = inputImage.getpixel((row, col))
                    redSum += pixelColors[0]
                    greenSum += pixelColors[1]
                    blueSum += pixelColors[2]
                    count += 1

            averageRed = redSum // count
            averageGreen = greenSum // count
            averageBlue = blueSum // count

            blurredImage.putpixel((width, height), (averageRed, averageGreen, averageBlue))

    blurredImage.save('blurred.png')
    print("Image blurred and saved as 'blurred.png'")


def sharpen_image():
    inputImage = Image.open('C:\\Desktop\\CS 110\\project2\\usf-campus.jpg')
    imageWidth, imageHeight = inputImage.size

    sharpenedImage = Image.new('RGB', (imageWidth, imageHeight), 'white')
    kernel = [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]

    # Amount of sharpening
    amount = 5

    # Blur the image
    blurredImage = inputImage.filter(ImageFilter.GaussianBlur(radius=1))

    for width in range(1, imageWidth - 1):
        for height in range(1, imageHeight - 1):
            # Get the original pixel value
            original = inputImage.getpixel((width, height))

            # Get the blurred pixel value
            blurred = blurredImage.getpixel((width, height))

            # Calculate the sharpened pixel value
            sharpenedRed = original[0] + (original[0] - blurred[0]) * amount
            sharpenedGreen = original[1] + (original[1] - blurred[1]) * amount
            sharpenedBlue = original[2] + (original[2] - blurred[2]) * amount

            # Clip the sharpened pixel values to the range [0, 255]
            sharpenedRed = min(255, max(0, int(sharpenedRed)))
            sharpenedGreen = min(255, max(0, int(sharpenedGreen)))
            sharpenedBlue = min(255, max(0, int(sharpenedBlue)))

            # Set the sharpened pixel value in the output image
            sharpenedImage.putpixel((width, height), (sharpenedRed, sharpenedGreen, sharpenedBlue))

    # Save the sharpened image
    sharpenedImage.save('sharpened.png')

    print("Image sharpened and saved as 'sharpened.png'")

def edge_detection(inputImage, imageWidth, imageHeight):
    sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

    grayscaleImage = inputImage.convert("L")  # Convert the image to grayscale
    edgeImage = Image.new("L", grayscaleImage.size)  # Create an empty image for edge detection

    for width in range(1, imageWidth - 1):
        for height in range(1, imageHeight - 1):
            # Extract the 3x3 region from the grayscale image
            region = grayscaleImage.crop((width - 1, height - 1, width + 2, height + 2))
            pixels = list(region.getdata())
            pixels = np.array(pixels).reshape(3, 3)

            # Apply the Sobel operators for horizontal and vertical edges
            gradient_x = np.sum(sobel_x * pixels)
            gradient_y = np.sum(sobel_y * pixels)

            # Calculate the magnitude of the gradient
            edge_magnitude = int(np.sqrt(gradient_x ** 2 + gradient_y ** 2))

            # Set the corresponding pixel in the edge image
            edgeImage.putpixel((width, height), edge_magnitude)

    edgeImage.save('sobel.png')
    print("Edge detection complete. Result saved as 'sobel.png'")

def scale_larger(inputImage, imageWidth, imageHeight, factor=2):
    # Calculate the new dimensions
    newWidth = int(imageWidth * factor)
    newHeight = int(imageHeight * factor)

    # Create a new image with the new dimensions
    largerImage = Image.new('RGB', (newWidth, newHeight), 'white')

    for newX in range(newWidth):
        for newY in range(newHeight):
            # Map the new coordinates to the original image
            x = int(newX / factor)
            y = int(newY / factor)
            pixelColors = inputImage.getpixel((x, y))
            largerImage.putpixel((newX, newY), pixelColors)

    # Save the scaled larger image as 'scaled.png'
    largerImage.save('scaled.png')
    print(f"Image scaled by a factor of {factor} and saved as 'scaled.png'")

main()
