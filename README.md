# s22-team2-project

<h3 align="center"><b>Team Members:</b></h3>
<p align="center">Christopher Andrews<br>
Joseph Cooper<br>
Ronnie Jackson<br>
Terrell McIllwain<br>
Zachary Kent</p>
<br><br>

--------------------------------------------
Hello! Welcome to team 2, or team Neocognitron's, Magic the Gathering Card Reader! This system is built towards taking in a picture of a Magic the Gathering (which will be shortened to MtG for brevity) card and then returning the name of the card after the system has completed reading it. Images of these cards can be submitted to the system in other without facing the correct direction and it will be adjusted for easier detection.

In order to demonstrate how this can work, however, it is required that a few things be set up in advance before you can try the demo for yourself!

Firstly, while the team tested and built parts of the system outside of Jupyterhub, the entirety of the model has been configured in JupyterHub for convinence. As such, it is requried that you also have your system ready to utilize JupyterHub as well. If you do not already have it, please follow this link: https://jupyter.org/install.

Also, just in case, if you do not have a version of Python3 installed, it may be best to do so as well. Higher Python3's would be advised, such as something above 3.5. This link can prove helpful: https://python.org/downloads/.

Finally, once you have JupytrHub as well as Python prepared, there is one last thing needed to get this system to function. Using the terminal, you will want to type:
<b>pip install opencv-python</b>
<br>You will then hit enter. Upon doing so, JupytrHub will install the neccessary parts that is required for our system to function. You will know it has finished when the words 'Successfully installed' appear at the beginning of a line of text after running the command.

Once all of this is completed, please continue to the 'demo' folder found within this repository. From there, there will be a step-by-step process to show you how this system works from beginning to end. Thank you and we hope you enjoy our project!
<hr>
<h3 align="center"><b>Parts of Network</b></h3>

<b><i>Card File:</i></b> This data file contains over 30,000 unique MtG cards. Each entry has the given card's name, the set that card was
released in, the 'collector-number,' and finally the file name of which the given picture shows the card's clean image.<br>
<br>
<b><i>Real Life Data File: </i></b>A secondary data file containing about 600 images of MtG cards taken with widely varying levels of 'noise'
within the background. Many of these images are also crooked, sideways, or upside down.<br>
<br>
<b><i>Image Extractor: </i></b>This program takes a real life image and using cv2 contour lines will extract the card from the real world image and resize it for the reading Neural net.<br>
<br>
<b><i>Image Reader: </i></b>The second and final neural network within the system. The card finder will take an image given and determine what the title of the MtG card is both by the characters it can read on the label and the image on the center of the card.<br>
