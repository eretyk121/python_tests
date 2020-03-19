import unittest
from unittest.mock import patch
import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.dirs, self.docs = app.update_date()
        self.error_docs = [{"type": "insurance", "number": "10006"}]
        with patch('app.update_date', return_value=(self.dirs, self.docs)):
            with patch('app.input', return_value='q'):
                app.secretary_program_start()

    def test_not_raise_get_doc(self):
        with patch('app.update_date', return_value=(self.dirs, self.error_docs)):
            with patch('app.input', return_value='q'):
                app.secretary_program_start()
            app.get_all_doc_owners_names()

    def test_delete(self):
        before_len = len(self.docs)
        with patch('app.input', return_value='10006'):
            app.delete_doc()
        self.assertLess(len(self.docs), before_len)

    def test_add_new_document_to_new_directory(self):
        before_len = len(self.docs)
        self.assertEqual(before_len, 3)
        with patch('app.input', side_effect=['10007', 'passport', 'testUser', '1']):
            app.add_new_doc()
        self.assertGreater(len(self.docs), before_len)
        self.assertEqual(len(self.docs), 4)

    def test_get_owner_name(self):  # мой тест на соответствие вывода имен по номеру документа
        for number in self.docs:
            with patch('app.input', return_value=number['number']):
                res = app.get_doc_owner_name()
                self.assertEqual(res, number['name'])

    def test_all_document_owners(self):
        list_len = len(self.docs)
        for name in self.docs:
            result = app.get_all_doc_owners_names()
            self.assertIn(name['name'], result)
            self.assertEqual(list_len, len(result))

    def test_remove_doc_from_shelf(self):
        quantity_before = len(self.dirs["2"])
        app.remove_doc_from_shelf('10006')
        quantity_after = len(self.dirs["2"])
        self.assertLess(quantity_after, quantity_before)

    def test_add_new_shelf(self):
        shelf_quantity_before = len(self.dirs)
        app.add_new_shelf('4')
        shelf_quantity_after = len(self.dirs)
        self.assertLess(shelf_quantity_before, shelf_quantity_after)

    def test_move_doc_to_shelf(self):
        doc_num = '10006'
        for key, val in self.dirs.items():
            if doc_num in val:
                old_shelf = key
        with patch('app.input', side_effect=[doc_num, '3']):
            app.move_doc_to_shelf()
        self.assertNotEqual(old_shelf, 3)

