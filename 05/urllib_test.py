import urllib.request


def get_wikidocs(page):
    resource = 'https://wikidocs.net/{}'.format(page)
    with urllib.request.urlopen(resource) as S:
        with open('wikidocs_%s.html' % page, 'wb') as f:
            f.write(S.read())


get_wikidocs(12)