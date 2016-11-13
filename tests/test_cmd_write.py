from cfgen import cfgen
from nose.tools import assert_equals
import os

def setup():
    test_root_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(test_root_dir + "/test_dir")
    clean()
    

def test_cmd_write():
    cfgen.cmd_write("test.cfg")
    
    with open("test.cfg") as actual, open("test.cfg.expected") as expected:
            actual_lines = actual.read().splitlines()
            expected_lines = expected.read().splitlines()

    assert_equals(len(actual_lines), len(expected_lines))
    
    for line_number in range(0, len(actual_lines)):
        assert_equals(actual_lines[line_number], expected_lines[line_number])

    
def clean():
    if os.path.isfile("test.cfg"):
        os.remove("test.cfg")
    if os.path.isfile("test.cfg.metaconfig.cache"):
        os.remove("test.cfg.metaconfig.cache")
    