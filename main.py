import datetime
from http.server import HTTPServer
from http.server import SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape


def get_year_tizer(year):
    """Calculate year tizer"""
    tizers = ['лет', 'года', 'год']
    k = (year // 10 % 10 != 1) * (year % 10)
    return tizers[(k == 1) + (1 <= k <= 4)]


def calulate_winery_age():
    """Calculate winery age"""
    age = (datetime.date.today().year - 1920) 
    age_string = get_year_tizer(age)
    return age, age_string


def main():
    """Program entry point"""
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')
    winery_age, age_tizer = calulate_winery_age()
    
    rendered_page = template.render(
        winery_age = winery_age,
        age_tizer = age_tizer
    )
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__=='__main__':
    main()
