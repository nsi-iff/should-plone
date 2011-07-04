import unittest
from should_dsl import should, should_not
import have_property

class PlonePortal(object):
    def __init__(self):
        self.title = "That's a title!"

    def getProperty(self, property_name):
        return self.title

class IncludeObjectSpec(unittest.TestCase):

    def it_checks_if_a_portal_has_a_property_with_a_given_value(self):
        #self.assertEquals(value, self.portal.getProperty(property_name))
        portal = PlonePortal()
        #should work
        portal |should| have_property('title', with_value="That's a title!")
        #should not work
        portal |should_not| have_property('title', with_value='wrong title')

