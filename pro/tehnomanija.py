import urllib.parse
from pac import scraper


class Store(scraper.Scraper):
    name = 'tehnomanija'

    def extract(self):
        for m in self.marke:
            get = {
                'filter_submited': '1',
                'show_filters': '1',
                'sort': 'price_asc',
                'filters[Robna marka][]': m,
                'filters[stock][]': 'sve',
                'items_per_page': '120'
            }
            self.g.go("https://www.tehnomanija.rs/tv-i-video/televizori?" + urllib.parse.urlencode(get))
            televizori = self.g.doc.select("//div[@class='product-wrap-grid']")
            for televizor in televizori:
                product = televizor.select(".//div[@class='product-name-grid']").text()
                price = televizor.select('.//div[@class="price"]').text()
                info = televizor.select(".//div[@class='buttons-grid']").text()
                self.output.append({
                    'product': product,
                    'price': price,
                    'info': info
                })

            self.output_prices(m)


if __name__ == '__main__':
    Store.extract()
