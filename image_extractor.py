import cv2
import numpy as np

def mouse_callback(event, x, y, flags, params):
    global num_click
    if num_click < 2 and event == cv2.EVENT_LBUTTONDOWN:
        num_click = num_click + 1
        print(num_click)
        global upper_bound, lower_bound, left_bound, right_bound
        upper_bound.append(max(i for i in hor if i < y) + 1)
        lower_bound.append(min(i for i in hor if i > y) - 1)
        left_bound.append(max(i for i in ver if i < x) + 1)
        right_bound.append(min(i for i in ver if i > x) - 1)


filename = cv2.imread('test/1.png', cv2.IMREAD_UNCHANGED)
 
#print('Original Dimensions : ',filename.shape)
 
scale_percent = 20 # percent of original size
width = int(filename.shape[1] * scale_percent / 100)
height = int(filename.shape[0] * scale_percent / 100)
dim = (width, height)

filename = cv2.resize(filename, dim, interpolation = cv2.INTER_AREA)
thr = 100  # edge detection threshold
lined = 50  # number of consequtive True pixels required an axis to be counted as line
num_click = 0  # select only twice
upper_bound, lower_bound, left_bound, right_bound = [], [], [], []
winname = 'img'

cv2.namedWindow(winname)
cv2.setMouseCallback(winname, mouse_callback)

img = cv2.imread(str(filename), 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
bw = cv2.Canny(gray, thr, 3*thr)

height, width, _ = img.shape

# find horizontal lines
hor = []
for i in range (0, height-1):
    count = 0
    for j in range (0, width-1):
        if bw[i,j]:
            count = count + 1
        else:
            count = 0
        if count >= lined:
            hor.append(i)
            break

# find vertical lines
ver = []
for j in range (0, width-1):
    count = 0
    for i in range (0, height-1):
        if bw[i,j]:
            count = count + 1
        else:
            count = 0
        if count >= lined:
            ver.append(j)
            break

# draw lines
disp_img = np.copy(img)
for i in hor:
    cv2.line(disp_img, (0, i), (width-1, i), (0,0,255), 1)
for i in ver:
    cv2.line(disp_img, (i, 0), (i, height-1), (0,0,255), 1)

while num_click < 2:
    cv2.imshow(winname, disp_img)
    cv2.waitKey(10)
disp_img = img[min(upper_bound):max(lower_bound), min(left_bound):max(right_bound)]
cv2.imshow(winname, disp_img)
cv2.waitKey()   # Press any key to exit
cv2.destroyAllWindows()