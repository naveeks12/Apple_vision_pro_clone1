import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAppleVisionProPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Launch browser and load the page
        cls.driver = webdriver.Chrome()
        cls.driver.get("file:///C:/Users/navee/OneDrive/Desktop/Apple-vision-main/Apple-vision-main/index.html")  # Use 'file:///' prefix
        cls.wait = WebDriverWait(cls.driver, 10)

    @classmethod
    def tearDownClass(cls):
        # Close the browser
        cls.driver.quit()

    def test_main_page_elements(self):
        # Test main page elements
        main_page = self.wait.until(EC.presence_of_element_located((By.ID, "page")))
        
        # Test navigation elements
        nav = main_page.find_element(By.TAG_NAME, "nav")
        self.assertEqual(nav.find_element(By.TAG_NAME, "h3").text.strip(), "Vision Pro")
        self.assertEqual(nav.find_element(By.TAG_NAME, "button").text.strip(), "Notify me")
        
        # Test video element
        video = main_page.find_element(By.TAG_NAME, "video")
        self.assertIn("hero/large_2x.mp4", video.get_attribute("src"))
        
        # Test page bottom elements
        page_bottom = main_page.find_element(By.ID, "page-bottom")
        self.assertEqual(page_bottom.find_element(By.TAG_NAME, "h3").text.strip(), "Introduction")
        self.assertIn("apple_vision_pro_logo", page_bottom.find_element(By.TAG_NAME, "img").get_attribute("src"))

    def test_page1_elements(self):
        page1 = self.wait.until(EC.presence_of_element_located((By.ID, "page1")))
        self.assertEqual(page1.find_element(By.TAG_NAME, "h1").text.strip(), "Welcome to the era of spatial computing")
        self.assertIn("foundation-spatial-computing", page1.find_element(By.TAG_NAME, "video").get_attribute("src"))

    def test_page2_elements(self):
        page2 = self.wait.until(EC.presence_of_element_located((By.ID, "page2")))
        self.assertIn("Apple Vision Pro seamlessly blends", page2.find_element(By.TAG_NAME, "h1").text.strip())
        self.assertIn("foundation-digital-canvas", page2.find_element(By.TAG_NAME, "video").get_attribute("src"))

    def test_design_sections(self):
        # Test page6 elements
        page6 = self.wait.until(EC.presence_of_element_located((By.ID, "page6")))
        self.assertEqual(page6.find_element(By.TAG_NAME, "h3").text.strip(), "Design")
        self.assertEqual(page6.find_element(By.TAG_NAME, "h1").text.strip(), "Designed by Apple.")
        self.assertIn("mobile, and wearable devices", page6.find_element(By.TAG_NAME, "p").text.strip())

        # Test subsequent design pages
        design_pages = {
            "page8": "Enclosure",
            "page9": "Light Seal.",
            "page10": "Head Band.",
            "page11": "Power.",
            "page12": "Sound.",
            "page13": "EyeSight."
        }

        for page_id, span_text in design_pages.items():
            page = self.wait.until(EC.presence_of_element_located((By.ID, page_id)))
            self.assertIn(span_text, page.find_element(By.TAG_NAME, "span").text.strip())

if __name__ == "__main__":
    unittest.main()
