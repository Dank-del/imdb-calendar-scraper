from flask import Flask, request
from scraper import get_soup, regions, get_regions, get_movies

app = Flask(__name__)

@app.get('/')
def index():
    return 'Welcome to IMDB Scraper!'

@app.get('/regions')
def get_available_regions():
    return regions

@app.get('/calendar')
def get_calendar_movies():
    if region := request.args.get('region'):
        if region not in regions:
            return {
                'msg': 'Invalid region'
            }
        soup = get_soup(region=region)
        return get_movies(soup)
    return get_movies(get_soup())

if __name__ == '__main__':
    soup = get_soup()
    regions = get_regions(soup)
    app.run()