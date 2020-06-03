import os
from typing import Tuple

import cv2
import names
import numpy as np

from getmrz import add_mrz_passport, add_mrz_id_card
from utils import random_char, random_number, genre, random_date

pass_img_dir = os.listdir('./images/passports')
id_img_dir = os.listdir('./images/ids')


def passport(bgr_image, x_y: Tuple = (50, 200), width_height: Tuple = (500, 100)):
    '''
    added random passport type MRZ to the input image.
    Args:
        bgr_image: image.
        x_y: top-left coordinates of wanted MRZ location.
        width_height: param of how much long MRZ you want.

    Returns:
        tuple of: image, top_left coordinate of mrz and width and height of it.
    '''
    org_width = bgr_image.shape[1]
    org_height = bgr_image.shape[0]
    random_fr_name = names.get_first_name()
    random_ls_name = names.get_last_name()
    p_number = random_number(7)
    br_date = random_date()
    gen = genre()
    expiry_date = random_date()
    id = 'ID' + random_number(8)

    doc_char_number = 44
    extra_scale = 1.41
    text_size = int(
        np.round((width_height[0] * extra_scale) / doc_char_number))  # in ID's mrz there are 30 chars each line

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
                                    id=id,
                                    text_size=text_size
                                    )

    dim = (org_width, org_height)
    img_with_mrz = cv2.resize(img_with_mrz, dim, interpolation=cv2.INTER_AREA)

    epsilon = 4  # to make sure that box does not cover letters and is lower
    h = 2 * text_size + epsilon
    w = doc_char_number * int(text_size * 0.75) + epsilon

    width_height = (w, h)

    return img_with_mrz, x_y, width_height


def id_cards(bgr_image, x_y: Tuple = (50, 280), width_height: Tuple = (512, 100)):
    '''
    added random ID card MRZ to the input image.
    Args:
        bgr_image: image.
        x_y: top-left coordinates of wanted MRZ location.
        width_height: param of how much long MRZ you want.

    Returns:
        tuple of: image, top_left coordinate of mrz and width and height of it.
    '''
    random_fr_name = names.get_first_name()
    random_ls_name = names.get_last_name()
    doc_number = random_char(3) + random_number(6)
    br_date = random_date()
    gen = genre()
    expiry_date = random_date()

    doc_char_number = 30
    extra_scale = 1.35
    text_size = int(
        np.round((width_height[0] * extra_scale) / doc_char_number))  # in ID's mrz there are 30 chars each line

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
                                   given_name=random_fr_name,
                                   text_size=text_size
                                   )

    epsilon = 4  # to make sure that box does not cover letters and is lower
    h = 3 * text_size + epsilon
    w = doc_char_number * int(text_size * 0.75) + epsilon

    width_height = (w, h)

    return img_with_mrz, x_y, width_height


if __name__ == '__main__':
    for name in id_img_dir:
        img_path = os.path.join('images', 'passports', '-1.jpeg')
        img = cv2.imread(img_path)
        img, (x, y), (w, h) = id_cards(img)
        # cv2.imwrite('./images/results/' + name, img)
        start_point = (x, y)
        end_point = ((x + w), (y + h))
        color = (255, 0, 0)
        img = cv2.rectangle(img, start_point, end_point, color, thickness=3)
        cv2.imshow(name, img)
        cv2.waitKey(0)
