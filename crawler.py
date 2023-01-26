from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from ordered_set import OrderedSet
from helpers import is_url_valid, get_clean_url


class Crawler:

    def __init__(self, url, depth=50):
        self.crawled_urls = OrderedSet([])
        if is_url_valid(url):  # fonction définie dans 'helpers'
            url = get_clean_url(url, '')
            self.depth = depth
            self.index = 0
            self.crawled_urls.add(url)
            self.crawl(url)
            print(*self.crawled_urls, sep='\n')
            print('total: ', len(self.crawled_urls))
        else:
            print('Invalid URL entered')
            print('total: ', len(self.crawled_urls))

    def crawl(self, url):
        """
        Recherche d'URLs
            - recherche des balises d'ancrage avec hrefs dans une page web
            - rejette les liens non désirés ou nettoie les liens obtenus
            - ajouter à un ensemble pour supprimer les doublons
            - "crawled_url" est le référentiel des URLs crawlées
        @input :
            url : URL à crawler
        """
        found_urls = []
        try:
            page = urlopen(url)
            content = page.read()
            soup = BeautifulSoup(content, 'lxml', parse_only=SoupStrainer('a'))
            for anchor in soup.find_all('a'):
                link = anchor.get('href')
                if is_url_valid(link):
                    # Compléter les URLs relatives
                    link = get_clean_url(url, link)
                    found_urls.append(link)
                else:
                    pass

        except HTTPError as e:
            print('HTTPError:' + str(e.code) + ' in ', url)
        except URLError as e:
            print('URLError: ' + str(e.reason) + ' in ', url)
        except Exception:
            import traceback
            print('Generic exception: ' + traceback.format_exc() + ' in ', url)

        cleaned_found_urls = set(found_urls)  # supprimer les répétitions
        self.crawled_urls |= cleaned_found_urls  # union d'ensembles
        if len(self.crawled_urls) > self.depth:
            self.crawled_urls = self.crawled_urls[:self.depth]
            return
        else:
            self.index += 1
            if self.index < len(self.crawled_urls):
                self.crawl(self.crawled_urls[self.index])
            else:
                return
