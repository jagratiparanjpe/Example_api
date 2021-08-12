import helper.helper as helper
import unittest
from unittest.mock import Mock, patch
import covid_api


class TestCovidAPI(unittest.TestCase):

    def test_covid_api(self):
        with patch('covid_api.requests.get') as mocked_get:
            mocked_get.status_code = 200
            mocked_get.return_value.json.return_value = { 'data' : [{'confirmed': 3000, 'deaths': 1, 'recovered': 30},{'confirmed': 2000, 'deaths': 0, 'recovered': 20}]}
            res = covid_api.get_iso_data('2021-02-03', 'xyz', 'https://covid-api.com/api/reports?')
            mocked_get.assert_called_with('https://covid-api.com/api/reports?date=2021-02-03&iso=xyz')
            self.assertEqual(res, ['2021-02-03', 'xyz', 5000, 1, 50])


if __name__ == '__main__':
    unittest.main()