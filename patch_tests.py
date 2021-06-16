import unittest
from patch_base import get_holidays
from requests.exceptions import Timeout
from unittest.mock import patch


class TestCalendar(unittest.TestCase):
    # decorator patches requests in main file and pass that to the test function
    @patch('patch_base.requests')
    def test_get_holidays_timeout(self, mock_requests):
        mock_requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_holidays()
            mock_requests.get.assert_called_once()

    @patch('patch_base.requests')
    def test_wrong_request(self, mock_requests):
        mock_requests.get.status_code.return_value = 400
        self.assertEqual(get_holidays(), 'aaa')



if __name__ == '__main__':
    unittest.main()
