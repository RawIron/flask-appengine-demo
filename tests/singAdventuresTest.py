import webtest
import singAdventures


class AppTest(unittest.TestCase):
    def setUp(self):
        # Create a WSGI application.
        app = webapp2.WSGIApplication([('/', MainPageHandler)])
        # Wrap the app with WebTest TestApp.
        self.testapp = webtest.TestApp(app)

    def test_mainPageHandler(self):
        response = self.testapp.get('/')
        self.assertEqual(response.status_int, 200)
        #self.assertEqual(response.normal_body, 'Hello World!')
        #self.assertEqual(response.content_type, 'text/plain')
