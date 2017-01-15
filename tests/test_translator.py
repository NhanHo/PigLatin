import unittest
import pig_latin.translator.translator as translator


class TranslationTest(unittest.TestCase):
    """TranslationTest"""
    def test_word_translation(self):
        """Test translation of one word"""
        self.assertEqual(translator.translate_word("hour"), "ourhay")
        self.assertEqual(translator.translate_word(""), "")
        self.assertEqual(translator.translate_word("aaa"), "aaayay")

    def test_paragraph_translation(self):
        p1 = """This is a sentence.
        This is another sentence"""
        p2 = """isThay isyay ayay entencesay.
        isThay isyay anotheryay entencesay"""
        self.assertEqual(translator.translate_paragraph(p1), p2)

        p3 = "...."
        self.assertEqual(translator.translate_paragraph(p3), p3)

        p4 = ""
        self.assertEqual(translator.translate_paragraph(p4), p4)

        p5 = ".a.a."
        p6 = ".ayay.ayay."
        self.assertEqual(translator.translate_paragraph(p5), p6)
