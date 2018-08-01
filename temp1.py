import cv2 as cv

print ("Imported CV2")

img = cv.imread("notepad_pic.png")
print "read image file size = {}x{}".format(img.shape[1], img.shape[0])
cv.imshow("Original....", img)

img_smooth = cv.GaussianBlur(img, (7,7),0)
cv.imshow("Smoothed....", img_smooth)

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grayed....", img_gray)

img_edges = cv.Canny(img_gray, 30, 100)
cv.imshow("Edges....", img_edges)
cv.waitKey()

