def intro():
    text = 'This is a small programm to calculate the extended euclidian algorithm. ' \
           'It also makes a chart with every step of iteration, and saves it to the path you entered, in .csv. ' \
           'Just follow the instructions, enter a filepath and two natural numbers (different from zero).'
    return text


def enter_num(order):
    return f'Please enter the {order} number!'


def enter_filename():
    return 'Please enter the Filename you wish for the chart to be saved with!'


def enter_filepath():
    return 'Please enter the Filepath you want the chart to be saved in!'


def enter_fileformat():
    return 'Please enter the Fileformat you want the chart to be saved in! (txt, pdf)'


def end_success():
    return 'Successfully saved as csv!' \
           'Your final results are a as GCD, \u03B10 and  \u03B20 as linear combination, such that:' \
           'gcd(a,b) = d = \u03B1 a + \u03B2 b'
