# -*- coding: UTF-8 -*-
import unittest

from my_lib import get_token, get_html, my_opener


class TestCaseRun(unittest.TestCase):
    """
    I added two values in the test below "actual_result" and "expected_value" these value represent the names they stand for 
    when you run a test and need to be fill in accodenly. I made an example, tests_file_type that shows how you could test something.
    you see that I match if "image" is in file_type and pass the test if this is true. It a simple test but it give you clear view how can make
    a unittest.

    You can find more assertion methods around this hash: 
        https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual

    Ok. you may think why is this needed ?
    It's all about concept and vision that make programming easier.
    We test code that is important but I miss the concept this could be the result because the project made some 
    changes from dating bot to learn TDD and to use queue system to scrape webpage(s). 
    Still the initial projectname is a bit confusing because the site happens to be dating site however the code only download 
    image(s) from a certain URL.

    Let's work on the concept, I'm a customer and I need an image scraper for dating site. To be true I had some problems with my developer
    and he left the project but I still have the code and I need you to make sure it works well in a optimized manner.
    
    I remember you said you had experience with queues and Docker (I know in reality this was the opposite) but hell it's good money
    so let's make it happend. 

    By now you know more and less what I need but still we have some problem(s):
        What do I need for the first stage prototype ? 
            # Prove that the application can pop a URL from a queue and download a image.
            # The URL's will be supplied in JSON format
            # I need a clear seperation of worker and queue in code 
        What do you need know to build the application 
            let's talk about this when you read this

    You can find part of the code that need to be tested below for a test 

    Please fix the tests in a way that they would pass the tests.
        #execute in root of project `python -m unittest` to run the test, it can take a while because the connection is real 
        if correct you can already spot a problem with a proxy.
        #remove all print statement 
        #first test passes(test_file_type) but the you need to fix the others

    We do a review after this is done

    `if we can't test it broken by design` 
    """

    def setUp(self):

        # Proxy variables
        self.test_my_ip_url = 'http://www.httpbin.org/ip'
        self.proxy = {'http': 'http://188.234.151.103:8080/'}
        self.proxy_ip = self.proxy.get('http').split('//')[1].split(':')[0]

        # Headers const
        self.uri = 'http://dating.ru'
        self.user = 'Alexey'

        mail = 'moalexey@gmail.com'
        password = 'u8PZ3EE2vP'

        self.test_image_uri = 'http://dating.ru/get_image.php?oid=149661164'
        self.file_type = 'image/JPEG'

        self.login_data = {
            'oid': '',
            'level': 'Low',
            'email': mail,
            'passwd': password,
            'submit': '%C2%EE%E9%F2%E8'
        }

        header_for_img = {
            'GET': '/get_image.php?{} HTTP/1.1'.format(self.test_image_uri.split('?')[1]),
            'Host': 'dating.ru',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36',
            'DNT': '1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',        
        }

    def tests_file_type(self):
        """
        Example of a test
        """
        html = get_html(uri=self.uri)
        self.login_data['tcurl'] = get_token(html)
        opener = my_opener(login_data=self.login_data)
        response = opener.open(self.test_image_uri)

        expected_value = self.file_type
        actual_value = response.info().get('Content-Type')

        self.assertIn(expected_value, actual_value)

    def tests_get_html(self):
        """
        Why do we need this ? For checking of connection and is site online. 
        """
        expected_value = '<form name="login"'
        actual_value = get_html()
        # Test 1 get html

        self.assertIn(expected_value, actual_value)

    def tests_get_token_from_html(self):
        """
        You could test this by checking if the token value is not null 
        e.g assertIsNotNone(token_value)
        """
        expected_value = 'maybe not even needed because token is variable'
        actual_value = 'token value'
        # Test 2 get token from html
        html = get_html(uri=self.uri)
        actual_value = get_token(html)
        self.assertIsNotNone(actual_value)

    def tests_access_picture_max_size(self):
        """
        I would say if the status_code is 200 and file_type match a certain type 
        it a success e.g tuple (200, 'image/png')
        Don't use print statement unless you test something
        """
        # Test 3 are we have access to an picture of max size?
        html = get_html(uri=self.uri)
        self.login_data['tcurl'] = get_token(html)
        opener = my_opener(login_data=self.login_data)
        response = opener.open(self.test_image_uri)

        expected_value = self.file_type
        actual_value = response.info().get('Content-Type')

        self.assertIn(expected_value, actual_value)

    def tests_access_through_proxy(self):
        # Test 4: Check request through proxy
        opener = my_opener(proxy=self.proxy)
        req = opener.open(self.test_my_ip_url)
        data = req.read().decode('utf8')
        expected_value = self.proxy_ip
        actual_value = data

        self.assertIn(expected_value, actual_value)
