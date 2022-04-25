# s22-team2-project

<h3 align="center"><b>Team Members:</b></h3>
<p align="center">Christopher Andrews<br>
Joseph Cooper<br>
Ronnie Jackson<br>
Terrell McIllwain<br>
Zachary Kent</p>
<br><br>

--------------------------------------------
<h1 align="center"><b>DEMO DRAFT</b></h1>
The purpose of this network is to be able to give the system a picture of a Magic the Gathering (MtG) card and then have the system the
name of the card to the user. To accomplish this, we have set up several parts to create the current version of the system to do this task.<br>

<h3 align="center"><b>Parts of Network</b></h3>

<b><i>Data File:</i></b> The first part needed is a data file containing over 30,000 unique MtG cards. Every entry has the given card's name, the set that card was
released in, the 'collector-number,' and finally the file name of which the given picture shows the card's clean image.<br>
<br>
<b><i>Real Life Set: </i></b>Finally, the last part of the network that will be used is a group of 600 real life images of MtG cards with widely varying levels of 'noise'
within the background. Many of these images are also crooked, sideways, or upside down so that both the image reader and the card finder
can be used in tangent with one another.<br>
<br>
<b><i>Image Reader: </i></b>The next part is the beginning neural net; the image reader. This first neural net will take a given image and adjust it to not only be
straightened out, but also take the image within the MtG card and pass both forward.<br>
<br>
<b><i>Card Finder: </i></b>Then, there is the second neural net; the card finder. The card finder which will take an image once it has passed through the image
reader and then determine what the title of the MtG card is by the image on the center of the card.<br>
<br>
