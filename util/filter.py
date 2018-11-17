import cv2


def image_otsu(img):
    img = cv2.imread(img, 0)
    ret, thr = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
    return thr


def image_resize(img, size):
    resized_image = cv2.resize(img, (size[0], size[1]))
    return resized_image


def save_image(save_path, img):
    cv2.imwrite(save_path, img)


# test code
if __name__ == "__main__":
    img = image_otsu("img.jpg")
    img = image_resize(img, (400, 200))
    save_image("processed.jpg", img)
