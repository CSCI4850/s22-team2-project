# s22-team2-project

Team Members:

-Zachary Kent <br> <!-- <br> for a break, seems this file uses HTML rules -->
-Ronnie Jackson <br>
-Christopher Andrews <br>
-Joseph Cooper <br>
-Terrell McIllwain <br>
<br><br>

--------------------------------------------
<center><b>DEMO DRAFT</b></center><br>
<br>
<center><b>Parts of Network</b></center><br>
The purpose of this network is to be able to give the system a picture of a Magic the Gathering (MtG) card and then have the system the<br>
name of the card to the user. To accomplish this, we have set up several parts to create the current version of the system to do this task.<br>
<br>
The first part needed is a data file containing over 30,000 unique MtG cards. Every entry has the given card's name, the set that card was<br>
released in, the 'collector-number,' and finally the file name of which the given picture shows the card's clean image.<br>
<br>
The next part is the beginning neural net; the image reader. This first neural net will take a given image and adjust it to not only be<br>
straightened out, but also take the image within the MtG card and pass both forward.<br>
<br>
Then, there is the second neural net; the card finder. The card finder which will take an image once it has passed through the image<br>
reader and then determine what the title of the MtG card is by the image on the center of the card.<br>
<br>
Finally, the last part of the network that will be used is a group of 600 real life images of MtG cards with widely varying levels of 'noise'<br>
within the background. Many of these images are also crooked, sideways, or upside down so that both the image reader and the card finder<br>
can be used in tangent with one another.<br>
