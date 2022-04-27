# s22-team2-project

<h3 align="center"><b>Team Members:</b></h3>
<p align="center">Christopher Andrews<br>
Joseph Cooper<br>
Ronnie Jackson<br>
Terrell McIllwain<br>
Zachary Kent</p>
<br><br>

--------------------------------------------
Hello! Welcome to team 2, or team Neocognitron's, Magic the Gathering card reader! This system is built towards taking in a picture of a Magic the Gathering (which will be shortened to MtG for brevity) card and then returning the name of the card after the system has completed reading it. Images of these cards can be submitted to the system in other without facing the correct direction and it will be adjusted for easier detection.

In order to demonstrate how this can work, however, it is required that a few things be set up in advance before you can try the demo for yourself!

Firstly, while the team tested and built parts of the system outside of Jupyterhub, the entirety of the model has been configured in JupyterHub for convinence. As such, it is requried that you also have your system ready to utilize JupyterHub as well. If you do not already have it, please follow this link: https://jupyter.org/install.

Also, just in case, if you do not have a version of Python3 installed, it may be best to do so as well. Higher Python3's would be advised, such as something above 3.5. This link can prove helpful: https://python.org/downloads/.

<h1 align="center"><b>DEMO DRAFT</b></h1>
The purpose of this network is to be able to give the system a picture of a Magic the Gathering (MtG) card and then have the system the
name of the card to the user. To accomplish this, we have set up several parts to create the current version of the system to do this task.<br>

<h3 align="center"><b>Parts of Network</b></h3>

<b><i>Card File:</i></b> This data file contains over 30,000 unique MtG cards. Each entry has the given card's name, the set that card was
released in, the 'collector-number,' and finally the file name of which the given picture shows the card's clean image.<br>
<br>
<b><i>Real Life Data File: </i></b>A secondary data file containing about 600 images of MtG cards taken with widely varying levels of 'noise'
within the background. Many of these images are also crooked, sideways, or upside down.<br>
<br>
<b><i>Image Reader: </i></b>The initial part of the beginning neural net. This neural net will take a given image and adjust it to be as
straight as possible to help the second neural network read it more clearly.<br>
<br>
<b><i>Card Finder: </i></b>The second and final neural network within the system. The card finder will take an image given and determine what the title of the MtG card is both by the characters it can read on the label and the image on the center of the card.<br>

<h3 align="center"><b>Steps</b></h3>
Following the demo of the system found in the 'demo' directory will demonstrate how to follow through on using the system in an entirely. However, before doing that, it is required that JupyterHub first be 
