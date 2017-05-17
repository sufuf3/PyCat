import json
from PyCat import pycat
from PyCat.scanner import Scanner


class TestCoverage:
    def test_pycat_c0(self):
        assert not pycat.ipCheck("128.400,.128/#$%")
        assert not pycat.ipCheck("140.113.1.256/24")
        assert pycat.ipCheck("128.128.128.128/255.255.0.0")
        assert not pycat.ipCheck("128.128.128.128/255.255.256.0")
        assert not pycat.ipCheck("140.113.1.1/40")
        assert pycat.ipCheck("140.113.1.1/24")

        assert json.loads(pycat.main("0.0.0.0", "17768"))["success"]
        assert not json.loads(pycat.main("140.113.1.1", "88888"))["success"]
        assert json.loads(pycat.main("0.0.0.0"))["success"]
        assert not json.loads(pycat.main("0.0.0.0", "1--2"))["success"]
        assert not json.loads(pycat.main("0.0.0.0", "80000,80001"))["success"]

        scanner = Scanner()

        assert scanner.scanip("127.0.0.1")
        assert not scanner.scanip("256.256.256.256")

    def test_pycat_c1(self):
        "Paths for portCheck"
        assert pycat.portCheck(32768)
        assert not pycat.portCheck(-32768)
        assert not pycat.portCheck("abcde")

        "Paths for ipCheck"
        assert not pycat.ipCheck("128.128.128.-128/16")
        assert not pycat.ipCheck("128.128.128.128/255.255.254.255")
        assert not pycat.ipCheck("128.128.128.128/255.255.256.255")
        assert not pycat.ipCheck("128.128.128.128/-16")
        assert not pycat.ipCheck("128.128.128.-128")
        assert not pycat.ipCheck("128.128")
        assert not pycat.ipCheck("128.128.128.128/255.255.255.abc")
        assert pycat.ipCheck("140.113.1.1/255.255.0.0")

        "Paths for main"
        assert not json.loads(pycat.main("140.113.1.1/-16", "32768"))["success"]
        assert json.loads(pycat.main("140.113.1.1"))["success"]
        assert not json.loads(pycat.main("140.113.1.1", "1-"))["success"]
        assert not json.loads(pycat.main("140.113.1.1", "65536-32768"))["success"]
        assert not json.loads(pycat.main("140.113.1.1", "32768-65536"))["success"]
        assert not json.loads(pycat.main("140.113.1.1", "0,32768,65536"))["success"]
        assert json.loads(pycat.main("140.113.1.1", "32768-65535"))["success"]
        assert json.loads(pycat.main("140.113.1.1", "0,32768,65535"))["success"]
        assert json.loads(pycat.main("140.113.1.1", "32768"))["success"]

        "Paths for scanner"
        scanner = Scanner()
        assert not scanner.scanip("256.256.256.256")
        assert scanner.scanip("127.0.0.1")
