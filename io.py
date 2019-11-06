import pandas as pd

import euclid.strings as strs
from euclid.extended_euclidian_algorithm import eea


def get_savepath():
    filename = input(strs.enter_filename())  # Todo: Make it navigable (via OS)
    filepath = input(strs.enter_filepath())
    # fileformat = input(strs.enter_fileformat())  # Todo: Make it chooseable (like Dropdown)

    make_savepath = f'{filepath}/{filename}.csv'

    return make_savepath


def get_numbers():
    firstnum = int(input(strs.enter_num('first')))
    secondnum = int(input(strs.enter_num('second')))
    return firstnum, secondnum


def make_data():
    a, b = get_numbers()
    df = pd.DataFrame((eea(a, b, 1, 0, 0, 1, [])), columns=['a', 'b', '\u03B10', '\u03B11', '\u03B20', '\u03B21', 'q'])
    return df


def make_output():
    savepath = get_savepath()
    df = make_data()
    df.to_csv(savepath)  # Todo: Make index, etc. chooseable/customizable


def successful_end():
    savepath = get_savepath()
    return f'{strs.end_success()}'
