import os
from typing import Tuple

import cv2
import names

from getmrz import add_mrz_passport, add_mrz_id_card
from utils import random_char, random_number, genre, random_date

pass_img_dir = os.listdir('./images/passports')
id_img_dir = os.listdir('./images/ids')


def passport(img, top_left: Tuple = (130, 350)):
    random_fr_name = names.get_first_name()
    random_ls_name = names.get_last_name()
    p_number = random_number(7)
    br_date = random_date()
    gen = genre()
    expiry_date = random_date()
    id = 'ID' + random_number(8)
    img_with_mrz = add_mrz_passport(img,
                                    coords=top_left,
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

    return img_with_mrz


def id_cards(img, top_left: Tuple = (130, 350)):
    random_fr_name = names.get_first_name()
    random_ls_name = names.get_last_name()
    doc_number = random_char(3) + random_number(6)
    br_date = random_date()
    gen = genre()
    expiry_date = random_date()
    img_with_mrz = add_mrz_id_card(img,
                                   coords=top_left,
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

    return img_with_mrz


if __name__ == '__main__':
    for name in id_img_dir:
        img_path = os.path.join('images', 'passports', name)
        img = cv2.imread(img_path)
        img = passport(img)
        # cv2.imwrite('./images/results/' + name, img)
        cv2.imshow(name, img)
        cv2.waitKey(0)
