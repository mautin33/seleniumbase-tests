import sys

sys.path.append(PATH)

from home_page import HomePage

class HomeTest(HomePage):
    
    # Setup 
    def setUp(self):
        super().setUp()
        print("Running before each test")

        # open home page
        self.openPage()

        # accept cookies
        self.click(self.cookiesBtn)

    # TearDown
    def tearDown(self):
        print("Running after each test")
        super().tearDown()


    def testHome(self):

        # assert page title
        self.assert_title(self.title)
        
        # assert page logo
        self.assert_element(self.pageLogo)

        # assert copyright
        self.scroll_to_bottom()
        self.assert_text(self.copyRightTxt, self.copyRight)
    
    
    def testNewsletter(self):

        #fill newsletter
        self.send_keys(self.newsLtrUserN, "Testing newsletter")
        self.send_keys(self.newsLtrEmail, "testingnewsletter@gmail.com")
        
        #click subscribe
        self.click(self.subscribeBtn)

        

         
         



