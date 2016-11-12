from cfgen import cfgen

from nose.tools import assert_equals
from nose.tools.nontrivial import raises


def test_parse_metaconfig_line_spaces():
    assert_equals(cfgen.parse_metaconfig_line("var=expr"), ("var", "expr"))
    assert_equals(cfgen.parse_metaconfig_line("var =expr"), ("var", "expr"))
    assert_equals(cfgen.parse_metaconfig_line("var= expr"), ("var", "expr"))
    assert_equals(cfgen.parse_metaconfig_line("var = expr"), ("var", "expr"))
    assert_equals(cfgen.parse_metaconfig_line("var  =  expr"), ("var", "expr"))
 
 
def test_parse_metaconfig_line_special_characters():
    assert_equals(cfgen.parse_metaconfig_line("var=\\"), ("var", "\\"))
    assert_equals(cfgen.parse_metaconfig_line("var=\""), ("var", "\""))
    assert_equals(cfgen.parse_metaconfig_line("var="), ("var", ""))
 
    for ch in "!@#$%^&*()_+=-|{}[];':/.,<>?`~":
        assert_equals(cfgen.parse_metaconfig_line("var=" + ch), ("var", ch))

@raises(ValueError)
def test_parse_metaconfig_line_errors():
    cfgen.parse_metaconfig_line("var asdf")
    cfgen.parse_metaconfig_line("var:asdf")
    cfgen.parse_metaconfig_line("=asdf")
