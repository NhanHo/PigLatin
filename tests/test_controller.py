import unittest
import pig_latin.pig_latin
import pig_latin.translator.translator as translator


class PigLatinTestCase(unittest.TestCase):
    def setUp(self):
        self.app = pig_latin.app.test_client()

    def test_translation_service(self):
        """ We want to test and make sure the controller right now is returning the
        same value as the value by out translator module. And return error 400
        if the request is invalid"""
        p = "This. is. a. sentence"
        rv = self.app.post('/', data=p)
        self.assertEqual(rv.data.decode("ascii"),
                         translator.translate_paragraph(p))
        self.assertEqual(rv.status_code, 200)

        p = ""
        rv = self.app.post('/', data=p)
        self.assertEqual(rv.status_code, 400)

        p = "Non-ascii sentence. 🦄"
        rv = self.app.post('/', data=p)
        self.assertEqual(rv.status_code, 400)
