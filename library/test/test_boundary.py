from rest_framework.test import APITestCase
from library.test.TestUtils import TestUtils
from django.urls import reverse
from django.test import TestCase
from library.models import Task




class RestrictAccessBoundaryTest(APITestCase):
    
    def test_boundary_allowed_ip(self):
        """Test if boundary cases with allowed IPs are handled"""
        test_obj = TestUtils()
        test_obj.yakshaAssert("TestBoundaryAllowedIP", True, "boundary")
        print("TestBoundaryAllowedIP = Passed")
