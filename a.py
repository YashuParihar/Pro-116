import cv2
import numpy as mp
img=cv2.imread("Solar System.jpg")
sun=img[120:360,400:500]
img[0:240,500:600]=sun
text_to_show="I love coading......."
cv2.putText(img,
            text_to_show,
            (20,220),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=1,
            color=(0,0,255))


cv2.imshow("Display Image",img)

grey_img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("GrayScale",grey_img)
print(img)

black=mp.zeros([600,600])
f_row=black[200:400,200:400]=255
print(f_row)
# print(black)
cv2.imshow("back",black)
cv2.waitKey(0)
