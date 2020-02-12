import time
import unittest
import WebTable
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test(unittest.TestCase):
    def test_web_table(self):
        driver = webdriver.Firefox(executable_path='D:\Code\Selenium\geckodriver.exe')
        # driver.implicitly_wait(30)

        driver.get("https://www.x-rates.com/historical/?from=USD&amount=1&date=2020-02-11")

        # w = WebTable(driver.find_element_by_xpath("//*[@id='webtable']"))
        w = WebTable.WebTable(driver.find_element_by_class_name('ratesTable'))
        # try:
        #     element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
        #      "html.js.flexbox.flexboxlegacy.canvas.canvastext.webgl.no-touch.geolocation.postmessage.no-websqldatabase.indexeddb.hashchange.history.draganddrop.websockets.rgba.hsla.multiplebgs.backgroundsize.borderimage.borderradius.boxshadow.textshadow.opacity.cssanimations.csscolumns.cssgradients.no-cssreflections.csstransforms.csstransforms3d.csstransitions.fontface.generatedcontent.video.audio.localstorage.sessionstorage.webworkers.applicationcache.svg.inlinesvg.smil.svgclippaths.cookies body div#__tealiumGDPRecModal div.privacy-basic div.privacy-basic-body div.privacy-button-container button.privacy-basic-button.privacy-basic-button-submit")))
        #     driver.find_element_by_css_selector(
        #         "html.js.flexbox.flexboxlegacy.canvas.canvastext.webgl.no-touch.geolocation.postmessage.no-websqldatabase.indexeddb.hashchange.history.draganddrop.websockets.rgba.hsla.multiplebgs.backgroundsize.borderimage.borderradius.boxshadow.textshadow.opacity.cssanimations.csscolumns.cssgradients.no-cssreflections.csstransforms.csstransforms3d.csstransitions.fontface.generatedcontent.video.audio.localstorage.sessionstorage.webworkers.applicationcache.svg.inlinesvg.smil.svgclippaths.cookies body div#__tealiumGDPRecModal div.privacy-basic div.privacy-basic-body div.privacy-button-container button.privacy-basic-button.privacy-basic-button-submit").click()
        # finally:
        #     print("noooo")
        driver.find_element_by_css_selector( "html.js.flexbox.flexboxlegacy.canvas.canvastext.webgl.no-touch.geolocation.postmessage.no-websqldatabase.indexeddb.hashchange.history.draganddrop.websockets.rgba.hsla.multiplebgs.backgroundsize.borderimage.borderradius.boxshadow.textshadow.opacity.cssanimations.csscolumns.cssgradients.no-cssreflections.csstransforms.csstransforms3d.csstransitions.fontface.generatedcontent.video.audio.localstorage.sessionstorage.webworkers.applicationcache.svg.inlinesvg.smil.svgclippaths.cookies body div#__tealiumGDPRecModal div.privacy-basic div.privacy-basic-body div.privacy-button-container button.privacy-basic-button.privacy-basic-button-submit").click()

        print("No of rows : ", w.get_row_count())
        print("------------------------------------")
        print("No of cols : ", w.get_column_count())
        print("------------------------------------")
        print("Table size : ", w.get_table_size())
        print("------------------------------------")
        print("First row data : ", w.row_data(1))
        print("------------------------------------")
        print("First column data : ", w.column_data(1))
        print("------------------------------------")
        print("All table data : ", w.get_all_data())
        print("------------------------------------")
        print("presence of data : ", w.presence_of_data("Chercher.tech"))
        print("------------------------------------")
        print("Get data from Cell : ", w.get_cell_data(2, 2))


if __name__ == "__main__":
    unittest.main()
