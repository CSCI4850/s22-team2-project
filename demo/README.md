Here in the demo, we will break down our system into two parts; the Image Extractor and the Image Reader. We will walkthrough how to do both individually.<br>

<h2><b>Image Extractor</b></h2>
The Image Extractor takes any given image and crop/rotate it to a proper orientation. Once it has completed, it will send the resized image to the neural net to determine what card the image contains.<br>
<br>
To use the demo's extractor, you first need to upload the 'Extractor Demo.ipynb' onto JupyterHub, followed by the Pics folder and all 30 images within it. Make sure that both 'Extractor Demo.ipynb' as well as the Pics folder are on the same level before proceeding. This means that in the directory on the side of JupyterHub, Pics folder and 'Extractor Demo.ipynb' need to be beside one another.<br>
<br>
Next, open the Extractor Demo. You should see two boxes with code inside of them. You will need to run both of them in the given order. Assuming you have set up cv2 as explained in the s22-team2-project README file, you should encounter no issue.<br>
<br>
Running the first box loads in libraries that the Extractor needs to function. The first time you run this box, it may take a few seconds. Then you will be prepared for the second box.<br>
<br>
The second box holds the extractor itself. When you run it, it will begin going through each of the 30 images found within the Pics folder. If the Pics folder is not on the same level as the Extractor, you will run into an error stating that <b><i>'NoneType' object has no attribute 'shape'</i></b>. You will need to get the Pics in the correct level and retry the Exractor code.<br>
<br>
Assuming Pics is set up correctly, the code will continue as intended. It will iterate through 30 real life images that have been prepared for this demo, detecting where in the image that the card is and extracting only the card from the entire image. It will then compare the width of the extracted image with the height. If the width is larger, it will rotate the card so that it is lined up vertically.<br>
<br>
For this demo, once the 30 images get completed, the extracted images a folder called Results will. If this folder does not already exist, the Extractor Demo will create a Results folder to store the extracted images into.<br>
<br>
In practice with the neural net, extracted images are passed directly to the Image Reader and no copies are saved. By doing this, both testing and training images are able to be passed to the neural net with the same sizes and parameters regardless of its source.<br>
<br>
<p align=center>This concludes the demo on the Image Extractor.</p>

<h2><b>Image Reader</b></h2>
At the beginning of the Image Reader is the Image Extractor. So if you followed the previous demo, you already know how the beginning of the main code for the reader will work.<br>
<br>
The first block sets up the libraries required to run the system. Then, on the second block of code, it collects the .csv file containing the image file paths and names of each corresponding card.<br>
<br>
After the .csv and libraries have been prepared, the third block is the Image Extractor itself, where it prepares the real life images for later.<br>
<br>
Next, we are going to build an array of the clean images. All 30,000 MtG card images are prepared at a pixel size of 250x300 to be passed in to the neural net later. Then, on the next code block, it tests the array to ensure that the images are set up correctly.<br>
<br>
After defining a function called list_2D, which assists the network for the next couple of code blocks, the function for the encoder is created. This encoder effectively turns a name comprised of characters, numbers, and symbols into rows of 1's and 0's so that the system can better read and organize the data being used.<br>
<br>
Once the cards are encoded, it checks each card name in the .csv to make sure they can all fit within the given number of MAX Characters determined in the Encoder (which for out network is 36). Whatever card names exceed 36 characters are pushed out of the array of cards so that it will not create an issue during the model.<br>
<br>
Next, the decoder is defined. This takes the rows of 1's and 0's back into a readable name once the model is done with them so that the user can effectively read it properly. The following code block gives an example of this by outputting 'Wall of Roots' from the decoder.<br>
<br>
With the data generator, it takes the large list of image arrays and labels that match withthem, and then splits them into two groups to help train the neural network. This is the final step required before the neural network itself is constructed and compiled.<br>
<br>
Now that everything has been set up and prepared, it is time to beuild the neural net itself. We start by creating the model, making a network with multiple hidden layers that take in the images found within the array and scan each one by a small group of pixels at a time until the entire image has been scanned and studied.<br>
<br>
After constructing the network, you compile it by beginning the training. It goes through multiple rounds of training, picking groups of images to run through each round which are called 'epochs.' These epochs help calculate and show the percentage of how often the network was accurate in inputing the card's name versus how often it did not successfully name the card.<br>
<br>
After all the epochs are completed, it outputs a graph showing the progres of accuracy and loss over the course of the entire training. Following this, we test to see if the system can properly pull out a image of a real life photo of a MtG card after it has been extracted.<br>
<br>
Finally, at the end of the system, it attempts to read the card from the real life image and output the name that it believes the image is displaying.<br>
<br>
<p align=center>This concludes the demo on the Image Reader.</p>
