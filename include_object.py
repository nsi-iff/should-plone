from should_dsl import matcher

@matcher
def include_object():
    '''Checks if the Plone Portal has a given object '''
    return(lambda portal, object_id: object_id in portal.objectIds(), "%s has %sobject %s")

