Here in the demo, we will break down our system into two parts; the Image Extractor and the Image Reader. We will walkthrough how to do both individually.<br><br>

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
Assuming Pics is set up correctly, the code will continue as intended. It will iterate through 30 real life images that have been prepared for this demo, detecting where in the image that the card is and extracting only the card from the entire image. It will then compare the width of the extracted image with the height. If the width is larger, it will rotate the card so that it is lined up vertically.

