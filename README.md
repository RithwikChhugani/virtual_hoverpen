# virtual_hoverpen
Project based on python for creating a tool for air drawing

## Repository Details

#### trackbars.py
This python file contains code for storing the values of the object selected for air drawing. In my case, I have taken a marker cap.
In this script, the color detection is done by firstly converting the RGB values to HSV(hue,saturation,value) format. The script allows to set the trackbars for hue, saturation and value channels of the image. Adjust the trackbars such that only the object is visible and rest all background is black. To save the trackbars hit "s" and to cancel hit "esc".
The script will save a file with name pen.npy containing the hsv color ranges of the object.

#### testing_trackbars.py
This script is just for further noise removal and testing the above created file. Here, I performed erosion for getting rid of the white spots in the picture and then dilation for enlarging the object for drawing. 

#### main.py
In this script what I did was, started drawing on the black canvas and then merged the black canvas with the image frame thus finally air drawing. The functionality of eraser is also added to switch between pen and eraser and the feature of clearing the whole screen is added if the selected drawing object is detected too near to the screen.

#### eraser2.png and pen.jpg
These are the images that work as icons on the frame to switch between pen and eraser.
