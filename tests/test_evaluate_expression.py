from cfgen import cfgen

from nose.tools import assert_equals
from nose.tools.nontrivial import raises


def test_evaluate_expression():
    assert_equals(cfgen.evaluate_expression("echo abc"), ("abc"))
