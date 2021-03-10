from selenium import webdriver

op = webdriver.FirefoxOptions()
op.add_argument('--headless')
browser = webdriver.Firefox(options=op)
browser.get('http://localhost:1337')

assert 'Django' in browser.title