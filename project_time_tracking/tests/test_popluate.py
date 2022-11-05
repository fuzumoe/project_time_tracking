import csv
import inspect
from pathlib import Path

from django.test import TestCase

from backend_plentific.api.models import PricePaidData
from backend_plentific.api.utils.papulate import PopulatePPDRecords


class PopulatePPDRecordsTestsCase(TestCase):

    def setUp(self) -> None:
        self.path = f'{Path(inspect.getfile(self.__class__)).parent.absolute()}/test_data'
        self.references = [

            # 2018
            '{8CAC1318-C832-0253-E053-604A8C08E51}',
            '{8CAC1318-C845-0253-E053-604A8C08E51}',

            # 2019
            '{98C75471-A26E-72E9-E053-604A8C042F0}',
            '{98C75471-A26F-72E9-E053-604A8C042F0}',

            # 2020
            '{B0A9D11B-43A5-4C1F-E053-604A8C0D716}',
            '{B0A9D11B-43A6-4C1F-E053-604A8C0D716}',

            # 2021
            '{D707E536-89BF-0AD9-E053-604A8C067CC}',
            '{D707E536-89C0-0AD9-E053-604A8C067CC}',

            # 2022
            '{E7B085FB-D02A-7E31-E053-604A8C0E67F}',
            '{E7B085FB-D02B-7E31-E053-604A8C0E67F}',
        ]
        self.columns = [
            'reference',
            'price',
            'dot',
            'postcode',
            'property_type',
            'old_new',
            'duration',
            'paon',
            'saon',
            'street',
            'locality',
            'city',
            'district',
            'county',
            'ppd_catagory_type',
            'record_status'
        ]

    def tearDown(self) -> None:
        PricePaidData.objects.filter(reference__in=self.references).delete()

    def test_papulate_papulates_recoreds_with_existing_files(self) -> None:
        records = PricePaidData.objects.filter(reference__in=self.references)
        for record in records:
            with self.subTest(record):
                assert record.reference not in self.references

        status = PopulatePPDRecords.populate(model=PricePaidData, path=self.path, columns=self.columns)
        assert (status, True)

        records = PricePaidData.objects.filter(reference__in=self.references)
        for record in records:
            with self.subTest(record):
                assert record.reference in self.references

    def test_papulate_does_not_papulates_recoreds_with_none_existing_records(self) -> None:
        status = PopulatePPDRecords.populate(model=PricePaidData, path="/temp/no/ffile.csv", columns=self.columns)
        assert (status, False)
