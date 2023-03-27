from json.decoder import JSONDecodeError

def set_auth_cookies(response):
    """
    :param response:
    :return: полученные с сервера куки
    """
    cookies = dict(response.cookies)
    if "error" not in cookies.keys():
        return cookies

def json_parser(response):
    """"
    Проверка возможности парсинга
    """
    try:

        return response.json()
    except JSONDecodeError:
        return "Response is not json format"