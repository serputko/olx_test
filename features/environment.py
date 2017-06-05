from selenium import webdriver

import os
import shutil
import time
import logging


def before_all(context):
    context.driver = webdriver.Chrome('./chromedriver')
    print("Executing before all")


def before_feature(context, feature):
    print("Before feature\n")
    context.logger = logging.getLogger('seleniumframework_tests')
    hdlr = logging.FileHandler('./seleniumframework_tests.log')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    context.logger.addHandler(hdlr)
    context.logger.setLevel(logging.DEBUG)


def before_scenario(context, scenario):
    print("User data:", context.config.userdata)
    context.driver.maximize_window()
    print("Before scenario\n")


def after_scenario(context, scenario):
    print("scenario status" + scenario.status)
    if scenario.status == "failed":
        if not os.path.exists("failed_scenarios_screenshots"):
            os.makedirs("failed_scenarios_screenshots")
        os.chdir("failed_scenarios_screenshots")
        context.driver.save_screenshot(scenario.name + "_failed.png")


def after_feature(context, feature):
    print("\nAfter Feature")


def after_all(context):
    print("User data:", context.config.userdata)
    # behave -D ARCHIVE=Yes
    if 'ARCHIVE' in context.config.userdata.keys():
        if os.path.exists("failed_scenarios_screenshots"):
            os.rmdir("failed_scenarios_screenshots")
            os.makedirs("failed_scenarios_screenshots")
        if context.config.userdata['ARCHIVE'] == "Yes":
            shutil.make_archive(
                time.strftime("%d_%m_%Y"),
                'zip',
                "failed_scenarios_screenshots")
            # os.rmdir("failed_scenarios_screenshots")
            print("Executing after all")
    context.driver.close()
