import cv2
import matplotlib.pyplot as plt

image = cv2.imread('Testing/Pics/IMG_8227.JPG', cv2.IMREAD_UNCHANGED)
scale_percent = 20 # percent of original size
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
scale_percent = 20 # percent of original size
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

# image = cv2.GaussianBlur(image,(3,3),cv2.BORDER_DEFAULT)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 130, 255, 1)

cnts = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

for c in cnts:
    x,y,w,h = cv2.boundingRect(c)
    ROI = image[y:y+h, x:x+w]
    break
    
width2 = int(ROI.shape[1] * scale_percent / 100)
height2 = int(ROI.shape[0] * scale_percent / 100)

if width2 > height2:
    ROI = cv2.rotate(ROI, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)
    
width = 250
height = 300
dim = (width, height)
 
# resize image
ROI = cv2.resize(ROI, dim, interpolation = cv2.INTER_AREA)

cv2.imwrite("Testing/Results/card" + output + ".png", ROI)

ROI= cv2.cvtColor(ROI, cv2.COLOR_BGR2RGB)

plt.imshow(ROI)#change index here to change image
plt.show()

print (ROI.shape)

output = "17"
# cv2.imshow('result', ROI)
