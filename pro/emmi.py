import urllib.parse
from pac import scraper


class Store(scraper.Scraper):
    name = 'emmi'
    def extract(self):
        m = "LG"  # na emmiju samo LG me zanima
        get = {
            'go': 'true',
            'Id': 10,
            'categoryId': 256,
            'brandId': 469,
            'limit': -1,
            'offset': 0
        }
        self.g.go("https://www.emmi.rs/konfigurator/proizvodi.10.html?" + urllib.parse.urlencode(get))
        televizori = self.g.doc.select('//div[@class="productListItem"]')
        for televizor in televizori:
            product = televizor.select('.//div[@class="productListTitle"]').text()
            price = televizor.select('.//span[@class="price"]').text()
            info = 'na stanju'
            self.output.append({
                'product': product,
                'price': price,
                'info': info
            })

        self.output_prices(m)


if __name__ == '__main__':
    Store.extract()
