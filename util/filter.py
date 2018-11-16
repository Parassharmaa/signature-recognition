import cv2
a = cv2.imread('img.jpg',0) 
ret,thr = cv2.threshold(a, 0, 255, cv2.THRESH_OTSU)
resized_image = cv2.resize(thr, (600,600))
cv2.imwrite('processed.jpg',resized_image)
cv2.destroyAllWindows()