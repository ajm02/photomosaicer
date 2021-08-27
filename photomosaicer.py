import math
import functions
import classes
import PIL
import os
import json
from sys import argv
from PIL import Image
from tqdm import tqdm

try:
    if len(argv) < 3 or len(argv) > 4:
        raise IndexError("Incorrect number of arguments given.")

    # side_length will be the width/height of each source image
    if argv[len(argv) - 1] == "low":
        side_length = 50

    elif argv[len(argv) - 1] == "med":
        side_length = 30

    elif argv[len(argv) - 1] == "high":
        side_length = 10

    else:
        raise SyntaxError("Unrecognised number of source images requested, please provide correct syntax")

    imagePath = argv[1]
    ogImage = Image.open(imagePath).convert("RGB")
    width, height = ogImage.size

    if width < 400 or height < 400:
        raise classes.ImageTooSmallError("The image provided is too small, please choose another image")

    # Load cached source images
    with open("." + os.path.sep + "source_image_cache" + os.path.sep + "cache.json", "r") as cache:
        json_data = json.load(cache)

    source_colours = [] # Will store tuples of source images and their average rgb
    for file in os.listdir("." + os.path.sep + "source_images"):
        source_image = Image.open(os.path.join("." + os.path.sep + "source_images", file)).convert("RGB")\
            .resize((side_length, side_length))

        # Check if the average rgb for the image is in cache
        if file in json_data.keys():
            average_source_rgb = json_data[file]

        # Otherwise calculate it and add it to the dictionary
        else:
            average_source_rgb = functions.average_rgb(source_image, source_image.size[0])
            json_data[file] = average_source_rgb

        source_colours.append((source_image, average_source_rgb))

    cache.close()
    with open("." + os.path.sep + "source_image_cache" + os.path.sep + "cache.json", "w") as cache:
        json.dump(json_data, cache) # Cache the source images
    cache.close()
    # Resize the image so it can be divided
    resizedImage = ogImage.resize(functions.dividing_size(width, height, side_length))
    resizedWidth, resizedHeight = resizedImage.size
    imageParts = []

    # Keep a list of tuples containing the position of each square
    for i in range(0, resizedWidth, side_length):
        for j in range(0, resizedHeight, side_length):
            imageParts.append((i, j, i + side_length, j + side_length))

    # Create a progress bar, as the next part can be long
    pbar = tqdm(total=len(imageParts))

    for i in imageParts:
        # Extract a square from the image and calculate the average rgb
        part = resizedImage.crop(i)
        average_rgb = functions.average_rgb(part, side_length)

        # Find the most similar source image to the extracted square in terms of rgb
        # Use Pythagoras: sqrt((r2 - r1)^2 + (g2 - g1)^2 + (b2 - b1)^2), smallest value is the closest
        most_similar = (None, 450)
        for j in source_colours:
            r = (j[1][0] - average_rgb[0]) ** 2
            g = (j[1][1] - average_rgb[1]) ** 2
            b = (j[1][2] - average_rgb[2]) ** 2
            difference = math.sqrt(r + g + b)

            if difference < most_similar[1]:
                most_similar = (j[0], difference)

        # Paste the source image onto that square and update the progress bar
        resizedImage.paste(most_similar[0], i)
        pbar.update()

    pbar.close()

    # If save argument was passed, save the mosaic image to the given location as the given name
    if len(argv) == 4:
        resizedImage.save(argv[2])
        file_name_start = argv[2].rfind(os.path.sep) + 1
        print("Photomosaic saved to " + argv[2][:file_name_start] + " as " + argv[2][file_name_start:])

    # Ask if the mosaic image wants to be seen, and display if yes
    see = input("A photomosaic has been created, would you like to see it (y/n?) ")
    if see == "y":
        resizedImage.show()


except (IndexError, FileNotFoundError, SyntaxError, PIL.UnidentifiedImageError, classes.ImageTooSmallError) as err:
    print(err)



