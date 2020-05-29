import cv2
import numpy as np
from PIL import Image, ImageFont, ImageDraw
from genmrz import gen_passport_text, gen_id_card_text
from typing import Tuple


# Open image with OpenCV
# img = np.ones((100, 512, 3), dtype=np.uint8) * 255


def add_mrz_passport(
        in_image,
        coords: Tuple = (0, 0),
        doc_type: str = 'P',
        country: str = 'GB',
        surname: str = 'MARTIN',
        name: str = 'SARAH',
        passport_number: str = '980XG47',
        nationality: str = 'GBR',
        birth_date: str = '850101',
        genre: str = 'f',
        expiry_date: str = '261228',
        id: str = 'ID88933477'):
    '''
    adds MRZ code on input image.
    :param in_image: input opencv image
    :param coords: x and y coords of top-left corner where mrz will be added
    :param doc_type: Document type   Normally 'P' for passport
    :param country: Country         3 letters code or country name
    :param surname: Surname(s)      Special characters will be transliterated
    :param name: Given name(s)   Special characters will be transliterated
    :param passport_number: Passport number
    :param nationality: Nationality     3 letter code or country name
    :param birth_date: Birth date      YYMMDD
    :param genre: Genre           Male: 'M', Female: 'F' or Undefined 'X'
    :param expiry_date: Expiry date     YYMMDD
    :param id: Id number       Not mandatory field
    :return: str
    '''

    # Make into PIL Image
    pil_img = Image.fromarray(in_image)
    # Get a drawing context
    draw = ImageDraw.Draw(pil_img)
    monospace = ImageFont.truetype("./ocrb_regular.ttf", size=14)
    # generate a text
    text = gen_passport_text(doc_type,
                             country,
                             surname,
                             name,
                             passport_number,
                             nationality,
                             birth_date,
                             genre,
                             expiry_date,
                             id)
    color = (0, 0, 0)
    draw.text(coords, text, color, font=monospace)

    # Convert back to OpenCV image and save
    result = np.array(pil_img)
    return result


def add_mrz_id_card(
        in_image,
        coords: Tuple = (0, 0),
        doc_type: str = 'ID',
        country: str = 'ESP',
        doc_number: str = 'BAA000589',
        birth_date: str = '800101',
        sex: str = 'F',
        expiry_date: str = '250101',
        nationality: str = 'ESP',
        surname: str = 'ESPAÑOLA ESPAÑOLA',
        given_name: str = 'CARMEN'):
    '''
    generates MRZ for ID cards by input data.
    :param in_image: input image
    :param coords: top-left coords of text.
    :param doc_type: Document type   Normally 'I' or 'ID' for id cards
    :param country: Country         3 letters code or country name
    :param doc_number: Document number
    :param birth_date: Birth date      YYMMDD
    :param sex: Genre           Male: 'M', Female: 'F' or Undefined
    :param expiry_date: Expiry date     YYMMDD
    :param nationality: Nationality
    :param surname:  Surname         Special characters will be transliterated
    :param given_name:  Given name(s)   Special characters will be transliterated
    :return:  str of generated MRZ code
    '''

    # Make into PIL Image
    pil_img = Image.fromarray(in_image)
    # Get a drawing context
    draw = ImageDraw.Draw(pil_img)
    monospace = ImageFont.truetype("./ocrb_regular.ttf", size=14)
    # generate a text
    text = gen_id_card_text(
        doc_type,  # Document type   Normally 'I' or 'ID' for id cards
        country,  # Country         3 letters code or country name
        doc_number,  # Document number
        birth_date,  # Birth date      YYMMDD
        sex,  # Genre           Male: 'M', Female: 'F' or Undefined
        expiry_date,  # Expiry date     YYMMDD
        nationality,  # Nationality
        surname,  # Surname         Special characters will be transliterated
        given_name  # Given name(s)   Special characters will be transliterated
    )
    color = (0, 0, 0)
    draw.text(coords, text, color, font=monospace)

    # Convert back to OpenCV image and save
    result = np.array(pil_img)
    return result


if __name__ == '__main__':
    out = add_mrz_passport()
    cv2.imwrite('result.png', out)
