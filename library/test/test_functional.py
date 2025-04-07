from django.test import TestCase
from django.urls import reverse
from library.test.TestUtils import TestUtils
from library.models import Task
from rest_framework.test import APITestCase
from django.test import TestCase
from django.http import HttpResponse
import re

class RestrictAccessFunctionalTest(APITestCase):
    
    def test_allowed_ip_access(self):
        test_obj = TestUtils()
        try:
            response = self.client.get(reverse('home'))  # Assuming the 'home' view is accessible
            if response.status_code == 403:
                test_obj.yakshaAssert("TestAllowedIPAccess", True, "functional")
                print("TestAllowedIPAccess = Passed")
            else:
                test_obj.yakshaAssert("TestAllowedIPAccess", False, "functional")
                print("TestAllowedIPAccess = Failed")
        except Exception as e:
            test_obj.yakshaAssert("TestAllowedIPAccess", False, "functional")
            print("TestAllowedIPAccess = Failed")

    def test_blocked_ip_access(self):
        test_obj = TestUtils()
        try:
            response = self.client.get(reverse('home'), HTTP_X_FORWARDED_FOR='203.0.113.5')
            if response.status_code == 200:
                test_obj.yakshaAssert("TestBlockedIPAccess", True, "functional")
                print("TestBlockedIPAccess = Passed")
            else:
                test_obj.yakshaAssert("TestBlockedIPAccess", False, "functional")
                print("TestBlockedIPAccess = Failed")
        except Exception as e:
            test_obj.yakshaAssert("TestBlockedIPAccess", False, "functional")
            print("TestBlockedIPAccess = Failed")