import unittest
from ludibrio import Stub
from should_dsl import should, should_not
from include_object import include_object

class PlonePortal(object):
    def objectIds(self):
        return ['object1', 'object2']

class IncludeObjectSpec(unittest.TestCase):

    def it_checks_if_an_object_is_included_in_a_Plone_Portal(self):
        #self.failIf('object_id' in self.portal.objectIds())
        #with Stub() as portal:
        #    portal.objectIds() >> ['object1', 'object2']
        portal = PlonePortal()
        #should work
        portal |should| include_object('object1')
        #should not work
        portal |should_not| include_object('object3')

