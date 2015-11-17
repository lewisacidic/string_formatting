from string_formatting import camel2snail

def test_camel2snail():
    assert camel2snail('CamelCase') == 'camel_case'

