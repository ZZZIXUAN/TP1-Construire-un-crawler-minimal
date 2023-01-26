from urllib.parse import urljoin, urlparse


def is_url_valid(link):
    """
    Rejeter un lien si
        - vide
        - PDF ou DOC
        - liens d'envoi
    @input :
        lien : Line présent dans la page web parent_url
    @output :
        booléen : invalid ou non
    """
    if not link or any(ext in link for ext in ('.pdf', 'docx')) \
            or link.startswith('mailto:') or ('#' in link):
        return False
    else:
        return True


def get_clean_url(parent_url, link):
    """
    Nettoyer l'URL en
        - liens relatifs complets
        - toujours commencer l'URL par 'http://'
        - supprimer le final "/"
    @input :
        parent_url : URL récupérée
        line : Lien présent dans la page web parent_url
    @output :
        url : l'URL propre
    """
    if link[:2] == '//':
        link = link[2:]

    if not bool(urlparse(link).netloc):  # analyse des URLs
        link = urljoin(parent_url, link.strip())  # compléter les chemins relatifs pour en faire des chemins absolus

    return link
