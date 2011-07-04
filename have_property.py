from should_dsl import matcher

@matcher
class HaveProperty(object):
    name = 'have_property'
    def __call__(self, property_name, with_value):
        self.property_name = property_name
        self.with_value = with_value
        return self

    def match(self, portal):
        self.actual_value = portal.getProperty(self.property_name)
        return self.with_value == self.actual_value

    def message_for_failed_should(self):
        return 'expected portal to have property %s with value %s, got %s' % (
 self.property_name, self.with_value, self.actual_value)

    def message_for_failed_should_not(self):
        return 'expected portal to have property %s with value different of %s, but got it' % (
 self.property_name, self.with_value)

