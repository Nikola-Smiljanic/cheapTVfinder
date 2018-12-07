from pac.scraper import Scraper
from pro.tehnomanija import Store as tehno
from pro.emmi import Store as emmi


def run():
    a = Scraper(name='Tehnomanija')
    tehno.extract(a)
    a.name = "Emmi"
    emmi.extract(a)


if __name__ == '__main__':
    run()
