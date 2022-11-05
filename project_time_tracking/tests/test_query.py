from django.test import TestCase
from django.db import connection

from backend_plentific.api.utils.query import Query


class PopulatePPDRecordsTestsCase(TestCase):

    def test_row_to_dict_returns_list_of_rows(self) -> None:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM api_pricepaiddata LIMIT 50")
        rows = Query.rows_to_dict(cursor=cursor)
        self.assertEqual(isinstance(rows, list), True)
        self.assertEqual(isinstance(rows[0], dict), True)

    def test_get_price_brackets_returns_price_bracket_list(self):
        price_brackets = Query.get_price_brackets(bracket_range=7)
        self.assertEqual(len(price_brackets) == 6, True)

    def test_range_list_to_str_price_with_single_elmented_array(self):
        element = 1000000
        single_elemented_list = [element]
        str_description = f"over £{element}"
        price_brackets = Query.range_list_to_str_price(bracket=single_elemented_list)

        self.assertEqual(price_brackets == str_description, True)

    def test_range_list_to_str_price_with_two_elmented_array(self):
        element_one = 1000000
        element_two = 200000
        single_elemented_list = [element_one, element_two]
        str_description = f"£{element_one}-£{element_two}"
        price_brackets = Query.range_list_to_str_price(bracket=single_elemented_list)
        self.assertEqual(price_brackets == str_description, True)

    def test_get_histogram_price_brackets_returns_none(self):
        histogram_data = Query.get_histogram_price_brackets(date=None, postcode=None)
        self.assertEqual(histogram_data is None, True)

    def test_get_histogram_price_brackets_returns_filled_values(self):
        date = '2018-10-01'
        postcode = 'SW11 7AY'
        str_date = "October 2018"
        data_keys = {
            "data": lambda value: len(value) > 0,
            "date": lambda value: value == str_date,
            "postcode": lambda value: value == postcode,
        }
        histogram_data = Query.get_histogram_price_brackets(date=date, postcode=postcode)
        histogram_data_keys = list(histogram_data.keys())
        self.assertEqual(isinstance(histogram_data, dict), True)
        for key in data_keys:
            with self.subTest(key):
                self.assertEqual(key in histogram_data_keys, True)
                self.assertEqual(data_keys[key](histogram_data[key]), True)

    def test_get_histogram_price_brackets_returns_empty_values(self):
        date = '2028-10-01'
        postcode = 'SW11 7AY'
        str_date = 'October 2028'
        data_keys = {
            "data": lambda value: len(value) == 0,
            "date": lambda value: value == str_date,
            "postcode": lambda value: value == postcode,
        }
        histogram_data = Query.get_histogram_price_brackets(date=date, postcode=postcode)
        histogram_data_keys = list(histogram_data.keys())
        self.assertEqual(isinstance(histogram_data, dict), True)
        for key in data_keys:
            with self.subTest(key):
                self.assertEqual(key in histogram_data_keys, True)
                self.assertEqual(data_keys[key](histogram_data[key]), True)

    def test_get_line_chart_price_per_postcode_returns_filled_list(self):
        frm = '2018-01-01'
        postcode = 'SW11 7AY'
        to = '2018-12-01'
        line_chart_data = Query.get_line_chart_price_per_postcode(frm=frm, to=to, postcode=postcode)

        self.assertEqual(isinstance(line_chart_data, list), True)
        self.assertEqual(len(line_chart_data) > 0, True)

    def test_get_line_chart_price_per_postcode_returns_empty_list(self):
        frm = None
        postcode = None
        to = None
        line_chart_data = Query.get_line_chart_price_per_postcode(frm=frm, to=to, postcode=postcode)

        self.assertEqual(isinstance(line_chart_data, list), True)
        self.assertEqual(len(line_chart_data) == 0, True)
