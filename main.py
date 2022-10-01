from time import time
from modules.BaseModule import BaseModule
import logging
import time
import os

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("log/debug.log", mode='w+'),
        logging.StreamHandler()
    ]
)


def create_dir():
    dir_list = ["data/excel_data", "data/html_data"]
    for item in dir_list:
        if not os.path.exists(item):
            os.makedirs(item)
            logging.info(
                f"creating the following directory- {item} to store the zipped html-file")
        else:
            logging.info(f"directory {item} already exists")


if __name__ == '__main__':
    # get the start time
    st = time.process_time()
    create_dir()
    logging.info("starting the process..")
    url = "https://www.scrapethissite.com/pages/forms"
    total_page_length = 6
    per_page_data = 100
    Base_module_object = BaseModule()
    Base_module_object.init_extract_transform(
        url, total_page_length, per_page_data)
    logging.info(
        "The process completed successfully, the excel dataset can be found in data/excel_data/scraped_excel_data.xlsx")
    # get the end time
    et = time.process_time()
    res = et - st
    logging.info(f'Total Execution time seconds: {res}')
