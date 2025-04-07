from rest_framework.test import APITestCase
from django.db import IntegrityError
from library.test.TestUtils import TestUtils
from django.urls import reverse
from unittest.mock import patch
from django.urls import get_resolver
from django.test import TestCase
from library.models import Task


class RestrictAccessExceptionalTest(APITestCase):
    
    def test_missing_ip_in_request(self):
        """Test if the middleware handles missing IP gracefully"""
        test_obj = TestUtils()
        try:
            # Simulate a request with no IP header
            response = self.client.get(reverse('home'), HTTP_X_FORWARDED_FOR=None)
            if response.status_code == 403:
                test_obj.yakshaAssert("TestMissingIP", True, "exceptional")
                print("TestMissingIP = Passed")
            else:
                test_obj.yakshaAssert("TestMissingIP", False, "exceptional")
                print("TestMissingIP = Failed")
        except Exception as e:
            test_obj.yakshaAssert("TestMissingIP", False, "exceptional")
            print("TestMissingIP = Failed")

    def test_invalid_ip_format(self):
        """Test if the middleware handles invalid IP format correctly"""
        test_obj = TestUtils()
        try:
            # Simulate a request with an invalid IP address format
            response = self.client.get(reverse('home'), HTTP_X_FORWARDED_FOR='invalid_ip')
            if response.status_code == 403:
                test_obj.yakshaAssert("TestInvalidIPFormat", True, "exceptional")
                print("TestInvalidIPFormat = Passed")
            else:
                test_obj.yakshaAssert("TestInvalidIPFormat", False, "exceptional")
                print("TestInvalidIPFormat = Failed")
        except Exception as e:
            test_obj.yakshaAssert("TestInvalidIPFormat", False, "exceptional")
            print("TestInvalidIPFormat = Failed")
