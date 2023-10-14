from django.test import TestCase
import unittest
import utils
from datetime import datetime
import utiles


class TestEvaluateSImilarity(unittest.Testcase):

    def test_similarity(self):
        now = datetime.now()
        result = utiles.compare_folders('admin','test1',now.strftime("%d%m%Y%H%M%S"))
        self.assertTrue(result>80)

