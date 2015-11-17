import re

def camel2snail(s):

    ''' converts a CamelCase string to camel_case. '''
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

