import unittest
from unittest.mock import patch
import yandex

class TestTranslate(unittest.TestCase):

    def test_response_status(self):
        with patch('yandex.input', side_effect=['Привет', 'ru', 'en']):
            status = yandex.get_response_from_server()
        self.assertEqual(status, 200)

    def test_translate_result(self):
        with patch('yandex.input', side_effect=['Привет', 'ru', 'en']):
            result = yandex.get_translate_result()
            self.assertEqual(result, 'Hi')

    def test_incorrect_type_lang(self):
        with patch('yandex.input', side_effect=['Привет', 'ru', 'DT']):
            self.assertRaises(KeyError, yandex.get_translate_result)
    #
    def test_missing_arguments(self):
        with patch('yandex.input', side_effect=['Привет', 'ru']):
            self.assertRaises(StopIteration, yandex.get_translate_result)

