from browser_config import BrowserConfig
from interact_browser import browserActions

b_cfg = BrowserConfig("Chrome")
b_cfg.setup_browser()

i_bwsr = browserActions(b_cfg.driver)
i_bwsr.navigate_to_google()
i_bwsr.search("Selenium with Python")
b_cfg.close_browser()