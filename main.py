import glob
import cv2


def sp_noise(image, prob):
    output = cv2.GaussianBlur(image, (7, 7), 0)
    return output

path = "test_images/imgs/*.*"
for file in glob.glob(path):

        print(file)
        img = cv2.imread(file,1)
        out=sp_noise(img,.01)
        cv2.imwrite(file,out)
