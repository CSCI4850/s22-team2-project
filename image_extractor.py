import cv2

image = cv2.imread('test/IMG_8291.JPG', cv2.IMREAD_UNCHANGED)
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

cv2.imshow("result", ROI)
cv2.waitKey(0)
cv2.imwrite("test/2c/new_card.png", ROI)