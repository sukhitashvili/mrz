import os
from typing import Tuple

import cv2
import names
import numpy as np

from getmrz import add_mrz_passport, add_mrz_id_card
from utils import random_char, random_number, genre, random_date

pass_img_dir = os.listdir('./images/passports')
id_img_dir = os.listdir('./images/ids')


def passport(bgr_image, x_y: Tuple = (50, 200)):
    org_width = bgr_image.shape[1]
    org_height = bgr_image.shape[0]
    width = 600
    height = 300
    dim = (width, height)
    bgr_image = cv2.resize(bgr_image, dim, interpolation=cv2.INTER_AREA)
    random_fr_name = names.get_first_name()
    random_ls_name = names.get_last_name()
    p_number = random_number(7)
    br_date = random_date()
    gen = genre()
    expiry_date = random_date()
    id = 'ID' + random_number(8)
    img_with_mrz = add_mrz_passport(bgr_image,
                                    coords=x_y,
                                    doc_type='P',
                                    # country=c_code,
                                    surname=random_ls_name,
                                    name=random_fr_name,
                                    passport_number=p_number,
                                    # nationality=nationality,
                                    birth_date=br_date,
                                    genre=gen,
                                    expiry_date=expiry_date,
                                    id=id
                                    )

    dim = (org_width, org_height)
    img_with_mrz = cv2.resize(img_with_mrz, dim, interpolation=cv2.INTER_AREA)

    x = x_y[0]
    y = x_y[1]
    epsilon = 4  # to make sure that box does not cover letters and is lower
    h = 2 * 14 + epsilon
    w = 44 * 10 + epsilon

    scale_x = org_width / width
    scale_y = org_height / height

    x_y = (int(np.round(x * scale_x)), int(np.round(y * scale_y)))
    width_height = (int(np.round(w * scale_x)), int(np.round(h * scale_y)))

    return img_with_mrz, x_y, width_height


def id_cards(bgr_image, x_y: Tuple = (50, 200)):
    org_width = bgr_image.shape[1]
    org_height = bgr_image.shape[0]
    width = 600
    height = 300
    dim = (width, height)
    bgr_image = cv2.resize(bgr_image, dim, interpolation=cv2.INTER_AREA)
    random_fr_name = names.get_first_name()
    random_ls_name = names.get_last_name()
    doc_number = random_char(3) + random_number(6)
    br_date = random_date()
    gen = genre()
    expiry_date = random_date()
    img_with_mrz = add_mrz_id_card(bgr_image,
                                   coords=x_y,
                                   doc_type='ID',
                                   country='ESP',
                                   doc_number=doc_number,
                                   birth_date=br_date,
                                   sex=gen,
                                   expiry_date=expiry_date,
                                   nationality='ESP',
                                   surname=random_ls_name,
                                   given_name=random_fr_name
                                   )
    dim = (org_width, org_height)
    img_with_mrz = cv2.resize(img_with_mrz, dim, interpolation=cv2.INTER_AREA)

    x = x_y[0]
    y = x_y[1]
    epsilon = 4  # to make sure that box does not cover letters and is lower
    h = 3 * 14 + epsilon
    w = 30 * 10 + epsilon

    scale_x = org_width / width
    scale_y = org_height / height

    x_y = (int(np.round(x * scale_x)), int(np.round(y * scale_y)))
    width_height = (int(np.round(w * scale_x)), int(np.round(h * scale_y)))

    return img_with_mrz, x_y, width_height


if __name__ == '__main__':
    for name in id_img_dir:
        img_path = os.path.join('images', 'passports', name)
        img = cv2.imread(img_path)
        img, (x, y), (w, h) = passport(img)
        # cv2.imwrite('./images/results/' + name, img)
        start_point = (x, y)
        end_point = ((x + w), (y + h))
        color = (255, 0, 0)
        img = cv2.rectangle(img, start_point, end_point, color, thickness=3)
        cv2.imshow(name, img)
        cv2.waitKey(0)
