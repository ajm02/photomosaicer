This is Photomosaicer V1, a tool that can create mosaics (image made up of other images). You provide it an image, and the tool will make a mosaic of that image using
7000 source images, giving you the option to save and view the mosaic that was created.

This is a project I have made, mainly because I really liked the idea of creating mosaics, and being able to show them to others. This is written in Python, for simplicity,
and to make it easy for others to read. The tool works by taking in 2 or 3 arguments. The first is a path to an image file, which will be the image to turn into a mosaic.
The second is the number of source images to use as 'low', 'med' or 'high' which can be thought of as the resolution for the mosaic. 'low' means to create the mosaic with
source images of size 50X50 pixels, therefore providing a low quality image, 'high' uses source images of 10X10 pixels, providing a high quality image (will take longer to
produce) and 'med' is in between, with source images of size 30X30 pixels. The third, which is an optional argument, is the save location and the name of file to save.
I have installed two packages for this program: PIL, for image processing, and tqdm to show a progress bar for the execution of the code. Once the arguments are provided, the
program will generate a mosaic for the image provided, according to the resolution provided and if given, save the image to specified location. The program will also give you
a y or n option for if you wish to see the image.

In order to run this program:

1. Ensure you have a Python interpreter installed, and have downloaded the folder in which this README is contained
2. Navigate to this folder in the command line and use one of the following commands:

 - python photomosaicer.py <Path-To-Image> <Resolution>
 - python photomosaicer.py <Path-To-Image> <Save-Under> <Resolution>

 <Path-To-Image>: This is the system path to the image you wish to turn into a mosaic, e.g. D:\Documents\tree.jpg will use tree.jpg in D:\Documents
 <Save-Under>: This is file name of the mosaic image to save and its location, e.g. D:\Documents\mosaic_tree.jpg will save the mosaic as mosaic_tree.jpg in D:\Documents.
 You must ensure you provide the 3 letter extension for the file name, if unsure, please affix .jpg at the end of the file name provided
 <Resolution>: This is given with 3 possible words, 'low', 'med' or 'high', 'low' provided a low quality image, 'med', medium quality and 'high', high quality

 Examples: 'python photomosaicer.py D:\Documents\tree.jpg med' produces a medium quality mosaic of tree.jpg 
	   'python photomosaicer.py D:\Documents\tree.jpg D:\Documents\mosaic_tree.jpg high' produces a high quality mosaic of tree.jpg and saves it as mosaic_tree.jpg in
            D:\Documents

3. Wait for the progress bar to finish and if you wish to view the created mosaic, enter 'y' (please ensure you have image viewing software to be able to view the image)

The given image must be a valid image file such as jpg and have both the height and width at or above 400 pixels, otherwise it will be rejected by the program. For the best
quality of mosaics produced, please use as large of an image as you can. If you wish to add some of your own source images, first make sure they are square images (same width
as height) and put them in the folder source_images.

In the future, I hope to add an indexing system to the code, which should provided a large speedup to the program, especially for high quality mosaics. I would like to thank
Robert Heaton - Programming Projects for Advanced Beginners for providing a guide on mosaic creators, as well as Prasun Roy for his natural images dataset and unsplash.com
for the 7000 source images I used.