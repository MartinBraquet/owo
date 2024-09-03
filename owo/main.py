import time
from pathlib import Path
from random import random

from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

MIN_WAIT = 2


def run():
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver_service = Service(executable_path='/snap/bin/geckodriver')
    # options.headless = True  # Uncomment if you want to run headless
    driver = Firefox(options=options, service=driver_service)
    DIR = Path(__file__).parent
    credentials = open(DIR / '../credentials', 'r').readlines()
    credentials = {a.split('=')[0]: a.split('=')[1] for a in credentials}
    url = credentials['url']
    driver.get(url)
    user = credentials['user']
    search_form = driver.find_element(value='uid_7')
    search_form.send_keys(user)
    pwd = credentials['pwd']
    search_form = driver.find_element(value='uid_9')
    search_form.send_keys(pwd)
    search_form.submit()
    time.sleep(5)
    active_elem = driver.switch_to.active_element

    def launch(command, wait=MIN_WAIT):
        active_elem.send_keys(command)
        time.sleep(random())
        active_elem.send_keys(Keys.RETURN)
        time.sleep(wait + random())

    def launch_sometimes(command, frequency=0.2):
        if random() < frequency:
            launch(command)

    print('Getting daily cowoncy')
    launch('owo daily')
    n = 1000
    wait = 3 * 60 * 60 / n
    print(f'Waiting {wait:.1f} seconds between commands')
    print('Number of commands in 30 min:', int(30 * 60 / wait))
    for i in range(n // 2):
        print(f'Battle and Hunt #{i + 1}')
        launch('owo b', wait=wait)
        launch('owo h', wait=wait)

        launch_sometimes('owo inv')
        launch_sometimes('owo zoo')
        # launch_sometimes('owo team')
        # launch_sometimes('owo ah')
        launch_sometimes('owo lb')
        launch_sometimes('owo crate')
    print(f'Done running {n} commands')


if __name__ == '__main__':
    run()
