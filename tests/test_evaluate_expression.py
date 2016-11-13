from cfgen import cfgen

from nose.tools import assert_equals
from nose.tools.nontrivial import raises


def test_evaluate_expression():
    assert_equals(cfgen.evaluate_expression("echo abc", {}), ("abc"))
    assert_equals(cfgen.evaluate_expression("echo $abc", {"abc": "a"}), ("a"))

@raises(ValueError)
def test_evaluate_expression_error():
    cfgen.evaluate_expression("unknown-command", {})
