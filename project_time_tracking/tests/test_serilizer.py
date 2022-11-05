from django.test import TestCase

from backend_plentific.api import serializers


class PopulatePPDRecordsTestCase(TestCase):
    def test_PricePerPostCodeSerializer_saves(self):
        data = {
            "reference": "{8CAC1318-C832-0253-E053-604A8C08E51}",
            "dot": "2018-12-20",
            "postcode": "NE15 8RB",
            "property_type": "S",
            "old_new": "N",
            "duration": "F",
            "paon": "6",
            "saon": "",
            "street": "SUGLEY VILLAS",
            "locality": "",
            "city": "NEWCASTLE UPON TYNE",
            "district": "NEWCASTLE UPON TYNE",
            "county": "TYNE AND WEAR",
            "ppd_catagory_type": "A",
            "record_status": "A"
        }
        serializer = serializers.PricePaidDataSerializer(data=data)
        serializer.is_valid()
        self.assertEqual(serializer.is_valid(), True)
        serializer.save()

    def test_PricePaidDataSerializer_validates(self):
        ppc_data = [
            {
                "date": "2020-01-06",
                "postcode": "SW11 7AY",
                "detached": 438730.2651072125,
                "flats": 288057.40124740126,
                "terraced": 249461.5894039735,
                "semi_detached": 271370.6959876543,
                "other": 1080088.9431818181
            },
            {
                "date": "2020-01-07",
                "postcode": "SW11 7AY",
                "detached": 487166.99447513814,
                "flats": 293395.04137931037,
                "terraced": 257875.69210526315,
                "semi_detached": 310189.40285714285,
                "other": 688573.2954545454
            }
        ]

        serializer = serializers.PricePerPostCodeSerializer(data=ppc_data, many=True)
        self.assertEqual(serializer.is_valid(), True)

    def test_NumOfTrsByPriceRangeSerilizer_valiates(self):
        data = {
            "data": [
                {
                    "label": "£768000-£926333",
                    "value": 84324.99
                },
                {
                    "label": "£926334-£1084667",
                    "value": 39033.00
                },
                {
                    "label": "£1084668-£1243001",
                    "value": 26646.887
                },
                {
                    "label": "£1243002-£1401335",
                    "value": 20557.877
                },
                {
                    "label": "over £1401336",
                    "value": 69953.789
                }
            ],
            "date": "March 2018",
            "postcode": "SW11 7AY"
        }
        serializer = serializers.NumOfTrsByPriceRangeSerilizer(data=data)


        self.assertEqual(serializer.is_valid(), True)

        data = {k: v for k, v in data.items() if k != 'postcode'}
        serializer = serializers.NumOfTrsByPriceRangeSerilizer(data=data)

        self.assertEqual(serializer.is_valid(), False)

    def test_AverageHousePotParamsSerizlizer_validates(self):
        data = {"format": 'json', "frm": '2018-01-01', "to": '2021-12-01', "postcode": 'SW11 7AY',}
        serializer = serializers.AverageHousePotParamsSerizlizer(data=data)

        self.assertEqual(serializer.is_valid(), True)

        data = {k: v for k, v in data.items() if k != 'frm'}
        serializer = serializers.AverageHousePotParamsSerizlizer(data=data)

        self.assertEqual(serializer.is_valid(), False)

    def test_NumOfTutParamsSerializer_validates(self):
        data = { "format": 'json',  "date": '2018-10-01', "postcode": 'SW11 7AY'}
        serializer = serializers.NumOfTutParamsSerializer(data=data)

        self.assertEqual(serializer.is_valid(), True)

        data = {k: v for k, v in data.items() if k != 'date'}
        serializer = serializers.NumOfTutParamsSerializer(data=data)

        self.assertEqual(serializer.is_valid(), False)

