import cv2

# To read the image
img1 = cv2.imread("C:\\Users\\HP\\Pictures\\Camera Roll\\munna.jpg")
print(img1)

# To dispaly the image
cv2.imshow("original", img1)  # Here the parameter "original" is the name of the window in which our image is displayed
cv2.waitKey()  # waitKey function is used to manipulate the time for which the image is displayed(it takes milliseconds)
cv2.destroyAllWindows()

# To resize the image

img2 = cv2.resize(img1, (900, 500))
cv2.imshow("original1", img2)
cv2.waitKey()
cv2.destroyAllWindows()
