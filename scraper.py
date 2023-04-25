import contextlib
import typing
import bs4
import requests

regions = []

def get_soup(region: str = 'US') -> bs4.BeautifulSoup:
    headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
                'cache-control': 'max-age=0',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"Windows"',
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
    r = requests.get(
        f"https://www.imdb.com/calendar/?ref_=rlm&region={region}", headers=headers)
    return bs4.BeautifulSoup(r.text, "html.parser")

def get_regions(soup: bs4.BeautifulSoup) -> typing.List[str]:
    # find the select element with id="country-selector"
    select_element = soup.find('select', {'id': 'country-selector'})

    # get a list of all options under the select element
    options = select_element.find_all('option')

    # create a list to store the regions
    regions = []

    # loop through each option and add its value to the regions list
    for option in options:
        value = option.get('value')
        if value != '':
            regions.append(value)

    return regions

def get_movies(soup: bs4.BeautifulSoup) -> typing.List[dict]:
    coming_soon = soup.find_all(
        'li', {'class': 'ipc-metadata-list-summary-item ipc-metadata-list-summary-item--click sc-8c2b7f1f-0 bpqYIE'})

    movies = []

    for movie in coming_soon:
        with contextlib.suppress(AttributeError):
            title = movie.find('a').text.strip()
            genres = [g.text.strip() for g in movie.find_all(
                'span', {'class': 'ipc-metadata-list-summary-item__li'})]
            cast = [c.text.strip() for c in movie.find('ul', {
                'class': 'ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--no-wrap ipc-inline-list--inline ipc-metadata-list-summary-item__stl base'}).find_all('li')]
            # print(f'{title}\nGenres: {", ".join(genres)}\nCast: {", ".join(cast)}\n')
            movies.append({
                'title': title,
                "genres": genres,
                "cast": cast,
            })

    return movies