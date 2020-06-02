import cv2
import numpy as np
import os

kernel = np.ones((5, 5), np.uint8)


def inpaint(bgr_image, mask_h_per_from_bottom=0.35, radius: int = 10):
    org_width = bgr_image.shape[1]
    org_height = bgr_image.shape[0]
    width = 600
    height = 300
    dim = (width, height)
    bgr_image = cv2.resize(bgr_image, dim, interpolation=cv2.INTER_AREA)

    flags = cv2.INPAINT_TELEA
    mask_top = np.zeros([int(np.round(bgr_image.shape[0] * (1 - mask_h_per_from_bottom))), bgr_image.shape[1]],
                        dtype=np.uint8)
    gray_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)
    mask = (gray_image < 140).astype('uint8')

    mask_bottom = mask[int(np.round(bgr_image.shape[0] * (1 - mask_h_per_from_bottom))):, ...]
    mask_bottom = cv2.dilate(mask_bottom, kernel, iterations=1)
    mask_bottom = cv2.medianBlur(mask_bottom, 7)
    mask = np.vstack((mask_top, mask_bottom))
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
        output = inpaint(image)
        save_path = os.path.join(path_2, name)
        cv2.imwrite(save_path, output)
