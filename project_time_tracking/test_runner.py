from django.test import TransactionTestCase
from django.test.runner import DiscoverRunner
from unittest.suite import TestSuite



class TestRunner(DiscoverRunner):
    """ A test runner to test without database creation """

    def setup_databases(self, **kwargs):
        pass

    def teardown_databases(self, old_config, **kwargs):
        pass

