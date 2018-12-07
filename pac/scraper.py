import os
import json
from grab import Grab
from datetime import datetime


class Scraper(object):
    marke = ['LG', 'Sony', 'Samsung', 'Vox', 'Fox']

    def __init__(self, g=Grab(), output=[], name='test'):
        self.g = g
        self.output = output
        self.name = name

    def output_prices(self, m):
        dir1 = '../log/' + self.name
        if not os.path.exists(dir1):
            os.makedirs(dir1)

        directory = dir1 + '/' + datetime.now().strftime("%d-%m-%Y")
        if not os.path.exists(directory):
            os.makedirs(directory)

        f = open(directory + '/' + m + '.txt', 'w+')
        json.dump(self.output, f, indent=0)
        self.output = []
