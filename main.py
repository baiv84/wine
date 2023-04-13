import pandas
import pprint
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


def load_wine_rows(file_name='wine.xlsx'):
    """Transform excel table to the list of dictionaries"""
    excel_data_df = pandas.read_excel(file_name, usecols=['Название', 'Сорт',
                                                          'Цена', 'Картинка'])
    wine_excel_rows = excel_data_df.to_dict(orient='records')
    return wine_excel_rows


def load_categories_wine_rows(file_name='wine2.xlsx'):
    """Transform excel table to the list of dictionaries"""
    wine_raw_data = pandas.read_excel(file_name, na_filter=False)
    wine_records = wine_raw_data.to_dict(orient='records')
    
    total_wine_dict = {}
    for wine_record in wine_records:
        category = wine_record['Категория']
        if category not in total_wine_dict:
            total_wine_dict[category] = [dict(Картинка=wine_record['Картинка'],
                                              Категория=category,
                                              Название=wine_record['Название'],
                                              Сорт=wine_record['Сорт'],
                                              Цена=wine_record['Цена']),
                                        ]
        else:
            wine_category_list = total_wine_dict[category]
            wine_category_list.append(wine_record)
            total_wine_dict[category] = wine_category_list
    return total_wine_dict


def main():
    """Program entry point"""
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')
    winery_age, age_tizer = calulate_winery_age()
    
    wine_rows = load_wine_rows()
    rendered_page = template.render(wine_rows=wine_rows,
                                    winery_age=winery_age,
                                    age_tizer=age_tizer)

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__=='__main__':
    #main()
    pp = pprint.PrettyPrinter(width=71, compact=True)
    pp.pprint(load_categories_wine_rows())

