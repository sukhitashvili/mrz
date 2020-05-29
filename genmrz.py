from mrz.generator.td3 import TD3CodeGenerator  # for passports
from mrz.generator.td1 import TD1CodeGenerator  # for ID cards


def gen_passport_text(
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
    generates passport MRZ.
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
    td3_generator = TD3CodeGenerator(doc_type,  # Document type   Normally 'P' for passport
                                     country,  # Country         3 letters code or country name
                                     surname,  # Surname(s)      Special characters will be transliterated
                                     name,  # Given name(s)   Special characters will be transliterated
                                     passport_number,  # Passport number
                                     nationality,  # Nationality     3 letter code or country name
                                     birth_date,  # Birth date      YYMMDD
                                     genre,  # Genre           Male: 'M', Female: 'F' or Undefined 'X'
                                     expiry_date,  # Expiry date     YYMMDD
                                     id)  # Id number       Not mandatory field
    return str(td3_generator)


def gen_id_card_text(
        doc_type: str = 'ID',
        country: str = 'ESP',
        doc_number: str = 'BAA000589',
        birth_date: str = '800101',
        sex: str = 'F',
        expiry_date: str = '250101',
        nationality: str = 'ESP',
        surname: str = 'ESPAÑOLA ESPAÑOLA',
        given_name: str = 'CARMEN',
        ):
    '''
    generates MRZ for ID cards by input data.
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

    td1_generator = TD1CodeGenerator(
        document_type=doc_type,      # Document type   Normally 'I' or 'ID' for id cards
        country_code=country,        # Country         3 letters code or country name
        document_number=doc_number,  # Document number
        birth_date=birth_date,       # Birth date      YYMMDD
        sex=sex,                     # Genre           Male: 'M', Female: 'F' or Undefined
        expiry_date=expiry_date,     # Expiry date     YYMMDD
        nationality=nationality,     # Nationality
        surname=surname,             # Surname         Special characters will be transliterated
        given_names=given_name    # Given name(s)   Special characters will be transliterated
    )
    return str(td1_generator)
