from cfgen import cfgen
from nose.tools import assert_equals
import os

def setup():
    test_root_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(test_root_dir + "/test_dir")
    clean()
    

def test_cmd_write():
    cfgen.cmd_write("test.cfg")
    
    # check target file
    actual_target_lines, expected_target_lines = get_file_lines("test.cfg", "test.cfg.expected")
    assert_lines_equal(actual_target_lines, expected_target_lines)

    # check cache
    actual_cache_lines, expected_cache_lines = get_file_lines("test.cfg.metaconfig.cache", "test.cfg.metaconfig.cache.expected")
    assert_lines_equal(actual_cache_lines, expected_cache_lines)

   
    
def clean():
    if os.path.isfile("test.cfg"):
        os.remove("test.cfg")
    if os.path.isfile("test.cfg.metaconfig.cache"):
        os.remove("test.cfg.metaconfig.cache")

def get_file_lines(filename1, filename2):
    with open(filename1) as f1, open(filename2) as f2:
        f1_lines = f1.read().splitlines()
        f2_lines = f2.read().splitlines()
    return f1_lines, f2_lines


def assert_lines_equal(lines1, lines2):
    assert_equals(len(lines1), len(lines2))
    for line_number in range(0, len(lines1)):
        assert_equals(lines1[line_number], lines2[line_number])

