import unittest
import pig_latin.pig_latin
import pig_latin.translator.translator as translator


class PigLatinTestCase(unittest.TestCase):
    def setUp(self):
        self.app = pig_latin.app.test_client()

    def test_one(self):
        p = "abcd"
        rv = self.app.post('/', data="abcd")
        self.assertEqual(rv.data.decode("ascii"),
                         translator.translate_paragraph(p))
