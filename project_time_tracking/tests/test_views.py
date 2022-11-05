from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class APITestCaseBase(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_average_house_pot_returns_http_status_200(self):
        params = {"frm": '2020-01-01', "to": '2022-12-30', "postcode": 'SW11 7AY'}
        path = "/average_house_pot/"
        response = self.client.get(path, params)

        self.assertEqual(response.status_code == status.HTTP_200_OK, True)

    def test_number_of_tot_returns_http_status_200(self):
        params = {"date": '2018-10-01', "postcode": 'SW11 7AY'}
        path = "/number_of_tot/"
        response = self.client.get(path, params)

        self.assertEqual(response.status_code == status.HTTP_200_OK, True)

    def test_average_house_pot_returns_http_status_400(self):
        path = "/average_house_pot/"
        response = self.client.get(path)

        self.assertEqual(response.status_code == status.HTTP_400_BAD_REQUEST, True)

    def test_number_of_tot_returns_http_status_400(self):
        path = "/number_of_tot/"
        response = self.client.get(path)

        self.assertEqual(response.status_code == status.HTTP_400_BAD_REQUEST, True)
