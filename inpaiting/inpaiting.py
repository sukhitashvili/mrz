import cv2
import numpy as np
import os
from typing import Tuple

kernel = np.ones((5, 5), np.uint8)


def inpaint(bgr_image, x_y: Tuple = (50, 200), height_width: Tuple = (100, 300), radius: int = 10):
    '''
    remove black color text form specified area.
    :param bgr_image: opencv-python image (BGR);
    :param x_y: x,y coordinates of top-left part of the text;
    :param height_width: height and width of the text;
    :param radius: the parameter for inpainting function;
    :return: the same size and format image with removed text.
    '''
    org_width = bgr_image.shape[1]
    org_height = bgr_image.shape[0]
    width = 600
    height = 300
    dim = (width, height)
    bgr_image = cv2.resize(bgr_image, dim, interpolation=cv2.INTER_AREA)

    flags = cv2.INPAINT_TELEA
    gray_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)
    mask = (gray_image < 140).astype('uint8')
    zero_mask = np.zeros(mask.shape, dtype=np.uint8)
    zero_mask[x_y[1]:(x_y[1]+height_width[0]), x_y[0]:(x_y[0]+height_width[1])] = 1
    mask = mask * zero_mask

    mask = cv2.dilate(mask, kernel, iterations=1)
    mask = cv2.medianBlur(mask, 7)
    output = cv2.inpaint(bgr_image, mask, radius, flags=flags)
    dim = (org_width, org_height)
    output = cv2.resize(output, dim, interpolation=cv2.INTER_AREA)
    return output


if __name__ == '__main__':
    path_1 = './images/docs_with_mrz'
    path_2 = './images/removed_mrz_results'
    ld = os.listdir(path_1)
    for name in ld:
        read_path = os.path.join(path_1, name)
        image = cv2.imread(read_path)
        output = inpaint(image, )
        save_path = os.path.join(path_2, name)
        # cv2.imwrite(save_path, output)
        cv2.imshow(name, output)
        cv2.waitKeyEx(0)
