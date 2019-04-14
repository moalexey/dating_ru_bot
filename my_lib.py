# -*- coding: UTF-8 -*-
import urllib.request

def get_token(html='', proxy={}, codec='cp1251'):
    '''Function return string of simbols, token value extracted from html
    '''
    left_tcurl_border = '<form name="login" action="/auth.php" '+\
    'method="post"><input type=hidden value="'
    right_tcurl_border = '" name="tcurl">'

    token = html[
        html.index(left_tcurl_border)+len(left_tcurl_border):
        html.index(right_tcurl_border)]
    return token

def get_html(uri='http://dating.ru', proxy={}, codec='cp1251'):
    '''Return html, sting of simbols
    '''
    opener = my_opener(proxy=proxy)
    req = opener.open(uri)
    html = req.read().decode(codec)
    return html


def my_opener(
    uri='http://dating.ru/auth.php', login_data='', proxy={}, timeout=30, codec='cp1251'):
    '''Return opener object with cookie and proxy handlers
    '''
    # disable proxy by passing an empty dict in
    # proxy_handler = urllib.request.ProxyHandler({'http': 'http://149.202.217.218:80/'})
    # alertnatively you could set a proxy for http with
    # proxy_handler = request.ProxyHandler({'http': 'http://www.example.com:3128/'})
    proxy_handler = urllib.request.ProxyHandler(proxy)
    cookieProcessor = urllib.request.HTTPCookieProcessor()
    opener = urllib.request.build_opener(
        cookieProcessor, proxy_handler)
    opener.open(uri,
        urllib.parse.urlencode(login_data
            ).encode(codec), timeout=timeout)
    return opener
