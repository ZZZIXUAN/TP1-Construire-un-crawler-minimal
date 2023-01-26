from crawler import Crawler
import requests
from lxml import etree
import argparse

# Utilisez argparse pour passer des arguments au programme directement et l'exécuter
parser = argparse.ArgumentParser(description="TP 1 Construire un crawler minimal")
parser.add_argument('-u', '--url', metavar='', default='https://ensai.fr/',
                    type=str, help='Seed URL for crawling')   # le type de données de l'argument à passer
parser.add_argument('-d', '--depth', metavar='', default=50,  # 50 est le nombre de pages à explorer
                    type=int, help='Number of links to crawl over')
args = parser.parse_args()


if __name__ == '__main__':
    # On essaye différentes méthodes du site crawler
    # Méthode 1 : Appeler notre fonction crawler écrite
    Crawler(args.url, args.depth)

    # Méthode 2 : Utiliser request directement
    res = requests.get('https://ensai.fr/').text   # initier une demande
    result = etree.HTML(res).xpath('//a/@href')    # xpath analyse l'attribut href de la balise a
    result = list(set(result))  # dé-pesage
    print(result)

    with open('file/crawled_webpages.txt', 'w') as fp:  # stockage
        for url in result[:50]:
            fp.write(url + '\n')

    # Méthode 3 : Utiliser sitemap pour réduire les requêtes aux urls tout en découvrant plus de pages
    res2 = requests.get('http://ensai.fr/sitemap_index.xml').text
    print(res2)

    with open('file/robots.txt', 'w') as fp2:  # écrire tous les résultats de la recherche dans le fichier robot.txt
        for url in etree.HTML(res2).xpath('//loc/text()'):
            print(url)
            fp2.write(url + '\n')
            detail_res2 = requests.get(url).text
            for detail_url in etree.HTML(detail_res2).xpath('//loc/text()'):  # explorer l'URL de niveau suivant
                fp2.write(detail_url + '\n')
