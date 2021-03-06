from PyCat import pycat


class TestBoundaryValue:
    def test_WeakNormal(self):
        assert pycat.ipCheck("0.128.128.128")
        assert pycat.ipCheck("255.128.128.128")

        assert pycat.ipCheck("128.0.128.128")
        assert pycat.ipCheck("128.255.128.128")

        assert pycat.ipCheck("128.128.0.128")
        assert pycat.ipCheck("128.128.255.128")

        assert pycat.ipCheck("128.128.128.0")
        assert pycat.ipCheck("128.128.128.255")

    def test_WeakRobust(self):
        assert not pycat.ipCheck("-1.128.128.128")
        assert not pycat.ipCheck("256.128.128.128")

        assert not pycat.ipCheck("128.-1.128.128")
        assert not pycat.ipCheck("128.256.128.128")

        assert not pycat.ipCheck("128.128.-1.128")
        assert not pycat.ipCheck("128.128.256.128")

        assert not pycat.ipCheck("128.128.128.-1")
        assert not pycat.ipCheck("128.128.128.256")

    def test_StrongNormal(self):
        assert pycat.ipCheck("0.0.128.128")
        assert pycat.ipCheck("0.255.128.128")
        assert pycat.ipCheck("255.0.128.128")
        assert pycat.ipCheck("255.255.128.128")

        assert pycat.ipCheck("0.128.0.128")
        assert pycat.ipCheck("0.128.255.128")
        assert pycat.ipCheck("255.128.0.128")
        assert pycat.ipCheck("255.128.255.128")

        assert pycat.ipCheck("0.128.128.0")
        assert pycat.ipCheck("0.128.128.255")
        assert pycat.ipCheck("255.128.128.0")
        assert pycat.ipCheck("255.128.128.255")

        assert pycat.ipCheck("128.0.0.128")
        assert pycat.ipCheck("128.0.255.128")
        assert pycat.ipCheck("128.255.0.128")
        assert pycat.ipCheck("128.255.255.128")

        assert pycat.ipCheck("128.0.128.0")
        assert pycat.ipCheck("128.0.128.255")
        assert pycat.ipCheck("128.255.128.0")
        assert pycat.ipCheck("128.255.128.255")

        assert pycat.ipCheck("128.128.0.0")
        assert pycat.ipCheck("128.128.0.255")
        assert pycat.ipCheck("128.128.255.0")
        assert pycat.ipCheck("128.128.255.255")

        assert pycat.ipCheck("0.0.0.128")
        assert pycat.ipCheck("255.0.0.128")
        assert pycat.ipCheck("0.255.0.128")
        assert pycat.ipCheck("0.0.255.128")
        assert pycat.ipCheck("255.255.0.128")
        assert pycat.ipCheck("255.0.255.128")
        assert pycat.ipCheck("0.255.255.128")
        assert pycat.ipCheck("255.255.255.128")

        assert pycat.ipCheck("0.0.128.0")
        assert pycat.ipCheck("255.0.128.0")
        assert pycat.ipCheck("0.255.128.0")
        assert pycat.ipCheck("0.0.128.255")
        assert pycat.ipCheck("255.255.128.0")
        assert pycat.ipCheck("255.0.128.255")
        assert pycat.ipCheck("0.255.128.255")
        assert pycat.ipCheck("255.255.128.255")

        assert pycat.ipCheck("0.128.0.0")
        assert pycat.ipCheck("255.128.0.0")
        assert pycat.ipCheck("0.128.255.0")
        assert pycat.ipCheck("0.128.0.255")
        assert pycat.ipCheck("255.128.255.0")
        assert pycat.ipCheck("255.128.0.255")
        assert pycat.ipCheck("0.128.255.255")
        assert pycat.ipCheck("255.128.255.255")

        assert pycat.ipCheck("128.0.0.0")
        assert pycat.ipCheck("128.255.0.0")
        assert pycat.ipCheck("128.0.255.0")
        assert pycat.ipCheck("128.0.0.255")
        assert pycat.ipCheck("128.255.255.0")
        assert pycat.ipCheck("128.255.0.255")
        assert pycat.ipCheck("128.0.255.255")
        assert pycat.ipCheck("128.255.255.255")

        assert pycat.ipCheck("0.0.0.0")
        assert pycat.ipCheck("255.0.0.0")
        assert pycat.ipCheck("0.255.0.0")
        assert pycat.ipCheck("0.0.255.0")
        assert pycat.ipCheck("0.0.0.255")
        assert pycat.ipCheck("255.255.0.0")
        assert pycat.ipCheck("255.0.255.0")
        assert pycat.ipCheck("255.0.0.255")
        assert pycat.ipCheck("0.255.255.0")
        assert pycat.ipCheck("0.255.0.255")
        assert pycat.ipCheck("0.0.255.255")
        assert pycat.ipCheck("255.255.255.0")
        assert pycat.ipCheck("255.255.0.255")
        assert pycat.ipCheck("255.0.255.255")
        assert pycat.ipCheck("0.255.255.255")
        assert pycat.ipCheck("255.255.255.255")

    def test_StrongRobust(self):
        assert not pycat.ipCheck("-1.-1.128.128")
        assert not pycat.ipCheck("-1.256.128.128")
        assert not pycat.ipCheck("256.-1.128.128")
        assert not pycat.ipCheck("256.256.128.128")

        assert not pycat.ipCheck("-1.128.-1.128")
        assert not pycat.ipCheck("-1.128.256.128")
        assert not pycat.ipCheck("256.128.-1.128")
        assert not pycat.ipCheck("256.128.256.128")

        assert not pycat.ipCheck("-1.128.128.-1")
        assert not pycat.ipCheck("-1.128.128.256")
        assert not pycat.ipCheck("256.128.128.-1")
        assert not pycat.ipCheck("256.128.128.256")

        assert not pycat.ipCheck("128.-1.-1.128")
        assert not pycat.ipCheck("128.-1.256.128")
        assert not pycat.ipCheck("128.256.-1.128")
        assert not pycat.ipCheck("128.256.256.128")

        assert not pycat.ipCheck("128.-1.128.-1")
        assert not pycat.ipCheck("128.-1.128.256")
        assert not pycat.ipCheck("128.256.128.-1")
        assert not pycat.ipCheck("128.256.128.256")

        assert not pycat.ipCheck("128.128.-1.-1")
        assert not pycat.ipCheck("128.128.-1.256")
        assert not pycat.ipCheck("128.128.256.-1")
        assert not pycat.ipCheck("128.128.256.256")

        assert not pycat.ipCheck("-1.-1.-1.128")
        assert not pycat.ipCheck("256.-1.-1.128")
        assert not pycat.ipCheck("-1.256.-1.128")
        assert not pycat.ipCheck("-1.-1.256.128")
        assert not pycat.ipCheck("256.256.-1.128")
        assert not pycat.ipCheck("256.-1.256.128")
        assert not pycat.ipCheck("-1.256.256.128")
        assert not pycat.ipCheck("256.256.256.128")

        assert not pycat.ipCheck("-1.-1.128.-1")
        assert not pycat.ipCheck("256.-1.128.-1")
        assert not pycat.ipCheck("-1.256.128.-1")
        assert not pycat.ipCheck("-1.-1.128.256")
        assert not pycat.ipCheck("256.256.128.-1")
        assert not pycat.ipCheck("256.-1.128.256")
        assert not pycat.ipCheck("-1.256.128.256")
        assert not pycat.ipCheck("256.256.128.256")

        assert not pycat.ipCheck("-1.128.-1.-1")
        assert not pycat.ipCheck("256.128.-1.-1")
        assert not pycat.ipCheck("-1.128.256.-1")
        assert not pycat.ipCheck("-1.128.-1.256")
        assert not pycat.ipCheck("256.128.256.-1")
        assert not pycat.ipCheck("256.128.-1.256")
        assert not pycat.ipCheck("-1.128.256.256")
        assert not pycat.ipCheck("256.128.256.256")

        assert not pycat.ipCheck("128.-1.-1.-1")
        assert not pycat.ipCheck("128.256.-1.-1")
        assert not pycat.ipCheck("128.-1.256.-1")
        assert not pycat.ipCheck("128.-1.-1.256")
        assert not pycat.ipCheck("128.256.256.-1")
        assert not pycat.ipCheck("128.256.-1.256")
        assert not pycat.ipCheck("128.-1.256.256")
        assert not pycat.ipCheck("128.256.256.256")

        assert not pycat.ipCheck("-1.-1.-1.-1")
        assert not pycat.ipCheck("256.-1.-1.-1")
        assert not pycat.ipCheck("-1.256.-1.-1")
        assert not pycat.ipCheck("-1.-1.256.-1")
        assert not pycat.ipCheck("-1.-1.-1.256")
        assert not pycat.ipCheck("256.256.-1.-1")
        assert not pycat.ipCheck("256.-1.256.-1")
        assert not pycat.ipCheck("256.-1.-1.256")
        assert not pycat.ipCheck("-1.256.256.-1")
        assert not pycat.ipCheck("-1.256.-1.256")
        assert not pycat.ipCheck("-1.-1.256.256")
        assert not pycat.ipCheck("256.256.256.-1")
        assert not pycat.ipCheck("256.256.-1.256")
        assert not pycat.ipCheck("256.-1.256.256")
        assert not pycat.ipCheck("-1.256.256.256")
        assert not pycat.ipCheck("256.256.256.256")


class TestEquivalenceClass:
    def test_WeakNormal(self):
        assert pycat.ipCheck("128.128.128.128")
        assert pycat.ipCheck("128.128.128.128/16")
        assert pycat.ipCheck("128.128.128.128/255.255.0.0")
        assert pycat.ipCheck("128.128.128.128/0.0.255.255")

    def test_WeakRobust(self):
        assert not pycat.ipCheck("128.-128.128.128")
        assert not pycat.ipCheck("128.400.128.128")
        assert not pycat.ipCheck("128.abc.128.128")
        assert not pycat.ipCheck("128.128,128.128")
        assert not pycat.ipCheck("128..128.128")
        assert not pycat.ipCheck("128.128.128.128/-16")
        assert not pycat.ipCheck("128.128.128.128/40")
        assert not pycat.ipCheck("128.128.128.128/200.200.0.0")
        assert not pycat.ipCheck("128.128.128.128/#$%")

    def test_StrongNormal(self):
        "Same as weak normal test"
        pass

    def test_StrongRobust(self):
        assert not pycat.ipCheck("128.-128,128.128")
        assert not pycat.ipCheck("128.-128..128")
        assert not pycat.ipCheck("128.-128.128.128/-16")
        assert not pycat.ipCheck("128.-128.128.128/40")
        assert not pycat.ipCheck("128.-128.128.128/200.200.0.0")
        assert not pycat.ipCheck("128.-128.128.128/#$%")

        assert not pycat.ipCheck("128.400,128.128")
        assert not pycat.ipCheck("128.400..128")
        assert not pycat.ipCheck("128.400.128.128/-16")
        assert not pycat.ipCheck("128.400.128.128/40")
        assert not pycat.ipCheck("128.400.128.128/200.200.0.0")
        assert not pycat.ipCheck("128.400.128.128/#$%")

        assert not pycat.ipCheck("128.abc,128.128")
        assert not pycat.ipCheck("128.abc..128")
        assert not pycat.ipCheck("128.abc.128.128/-16")
        assert not pycat.ipCheck("128.abc.128.128/40")
        assert not pycat.ipCheck("128.abc.128.128/200.200.0.0")
        assert not pycat.ipCheck("128.abc.128.128/#$%")

        assert not pycat.ipCheck("128.,128.128")
        assert not pycat.ipCheck("128.128,128.128/-16")
        assert not pycat.ipCheck("128.128,128.128/40")
        assert not pycat.ipCheck("128.128,128.128/200.200.0.0")
        assert not pycat.ipCheck("128.128,128.128/#$%")

        assert not pycat.ipCheck("128..128.128/-16")
        assert not pycat.ipCheck("128..128.128/40")
        assert not pycat.ipCheck("128..128.128/200.200.0.0")
        assert not pycat.ipCheck("128..128.128/#$%")

        assert not pycat.ipCheck("128.-128,.128")
        assert not pycat.ipCheck("128.400,.128")
        assert not pycat.ipCheck("128.abc,.128")

        assert not pycat.ipCheck("128.-128,128.128/-16")
        assert not pycat.ipCheck("128.-128,128.128/40")
        assert not pycat.ipCheck("128.-128,128.128/200.200.0.0")
        assert not pycat.ipCheck("128.-128,128.128/#$%")

        assert not pycat.ipCheck("128.400,128.128/-16")
        assert not pycat.ipCheck("128.400,128.128/40")
        assert not pycat.ipCheck("128.400,128.128/200.200.0.0")
        assert not pycat.ipCheck("128.400,128.128/#$%")

        assert not pycat.ipCheck("128.abc,128.128/-16")
        assert not pycat.ipCheck("128.abc,128.128/40")
        assert not pycat.ipCheck("128.abc,128.128/200.200.0.0")
        assert not pycat.ipCheck("128.abc,128.128/#$%")

        assert not pycat.ipCheck("128.-128..128/-16")
        assert not pycat.ipCheck("128.-128..128/40")
        assert not pycat.ipCheck("128.-128..128/200.200.0.0")
        assert not pycat.ipCheck("128.-128..128/#$%")

        assert not pycat.ipCheck("128.400..128/-16")
        assert not pycat.ipCheck("128.400..128/40")
        assert not pycat.ipCheck("128.400..128/200.200.0.0")
        assert not pycat.ipCheck("128.400..128/#$%")

        assert not pycat.ipCheck("128.abc..128/-16")
        assert not pycat.ipCheck("128.abc..128/40")
        assert not pycat.ipCheck("128.abc..128/200.200.0.0")
        assert not pycat.ipCheck("128.abc..128/#$%")

        assert not pycat.ipCheck("128.,128.128/-16")
        assert not pycat.ipCheck("128.,128.128/40")
        assert not pycat.ipCheck("128.,128.128/200.200.0.0")
        assert not pycat.ipCheck("128.,128.128/#$%")

        assert not pycat.ipCheck("128.-128,.128/-16")
        assert not pycat.ipCheck("128.-128,.128/40")
        assert not pycat.ipCheck("128.-128,.128/200.200.0.0")
        assert not pycat.ipCheck("128.-128,.128/#$%")

        assert not pycat.ipCheck("128.400,.128/-16")
        assert not pycat.ipCheck("128.400,.128/40")
        assert not pycat.ipCheck("128.400,.128/200.200.0.0")
        assert not pycat.ipCheck("128.400,.128/#$%")

        assert not pycat.ipCheck("128.abc,.128/-16")
        assert not pycat.ipCheck("128.abc,.128/40")
        assert not pycat.ipCheck("128.abc,.128/200.200.0.0")
        assert not pycat.ipCheck("128.abc,.128/#$%")


class TestEdge:
    def test_WeakNormal(self):
        assert pycat.ipCheck("0.0.0.0")
        assert pycat.ipCheck("0.0.0.0/0")
        assert pycat.ipCheck("0.0.0.0/0.0.0.0")
        assert pycat.ipCheck("0.0.0.0/255.255.255.255")

    def test_WeakRobust(self):
        assert not pycat.ipCheck("-1.-1.-1.-1")
        assert not pycat.ipCheck("256.256.256.256")
        assert not pycat.ipCheck("a.a.a.a")
        assert not pycat.ipCheck("0,0,0,0")
        assert not pycat.ipCheck("0...")
        assert not pycat.ipCheck("0.0.0.0/-1")
        assert not pycat.ipCheck("0.0.0.0/33")
        assert not pycat.ipCheck("0.0.0.0/-1.-1.-1.-1")
        assert not pycat.ipCheck("0.0.0.0/@")

    def test_StrongNormal(self):
        "Same as weak normal test"
        pass

    def test_StrongRobust(self):
        assert not pycat.ipCheck("-1,-1,-1,-1")
        assert not pycat.ipCheck("-1...")
        assert not pycat.ipCheck("-1.-1.-1.-1/-1")
        assert not pycat.ipCheck("-1.-1.-1.-1/33")
        assert not pycat.ipCheck("-1.-1.-1.-1/-1.-1.-1.-1")
        assert not pycat.ipCheck("-1.-1.-1.-1/@")

        assert not pycat.ipCheck("256,256,256,256")
        assert not pycat.ipCheck("256...")
        assert not pycat.ipCheck("256.256.256.256/-1")
        assert not pycat.ipCheck("256.256.256.256/33")
        assert not pycat.ipCheck("256.256.256.256/-1.-1.-1.-1")
        assert not pycat.ipCheck("256.256.256.256/@")

        assert not pycat.ipCheck("a,a,a,a")
        assert not pycat.ipCheck("a...")
        assert not pycat.ipCheck("a.a.a.a/-1")
        assert not pycat.ipCheck("a.a.a.a/33")
        assert not pycat.ipCheck("a.a.a.a/-1.-1.-1.-1")
        assert not pycat.ipCheck("a.a.a.a/@")

        assert not pycat.ipCheck("0,,,")
        assert not pycat.ipCheck("0,0,0,0/-1")
        assert not pycat.ipCheck("0,0,0,0/33")
        assert not pycat.ipCheck("0,0,0,0/-1.-1.-1.-1")
        assert not pycat.ipCheck("0,0,0,0/@")

        assert not pycat.ipCheck("0.../-1")
        assert not pycat.ipCheck("0.../33")
        assert not pycat.ipCheck("0.../-1.-1.-1.-1")
        assert not pycat.ipCheck("0.../@")

        assert not pycat.ipCheck("-1,,,")
        assert not pycat.ipCheck("256,,,")
        assert not pycat.ipCheck("a,,,")

        assert not pycat.ipCheck("-1,-1,-1,-1/-1")
        assert not pycat.ipCheck("-1,-1,-1,-1/33")
        assert not pycat.ipCheck("-1,-1,-1,-1/-1.-1.-1.-1")
        assert not pycat.ipCheck("-1,-1,-1,-1/@")

        assert not pycat.ipCheck("256,256,256,256/-1")
        assert not pycat.ipCheck("256,256,256,256/33")
        assert not pycat.ipCheck("256,256,256,256/-1.-1.-1.-1")
        assert not pycat.ipCheck("256,256,256,256/@")

        assert not pycat.ipCheck("a,a,a,a/-1")
        assert not pycat.ipCheck("a,a,a,a/33")
        assert not pycat.ipCheck("a,a,a,a/-1.-1.-1.-1")
        assert not pycat.ipCheck("a,a,a,a/@")

        assert not pycat.ipCheck("-1.../-1")
        assert not pycat.ipCheck("-1.../33")
        assert not pycat.ipCheck("-1.../-1.-1.-1.-1")
        assert not pycat.ipCheck("-1.../@")

        assert not pycat.ipCheck("256.../-1")
        assert not pycat.ipCheck("256.../33")
        assert not pycat.ipCheck("256.../-1.-1.-1.-1")
        assert not pycat.ipCheck("256.../@")

        assert not pycat.ipCheck("a.../-1")
        assert not pycat.ipCheck("a.../33")
        assert not pycat.ipCheck("a.../-1.-1.-1.-1")
        assert not pycat.ipCheck("a.../@")

        assert not pycat.ipCheck("0,,,/-1")
        assert not pycat.ipCheck("0,,,/33")
        assert not pycat.ipCheck("0,,,/-1.-1.-1.-1")
        assert not pycat.ipCheck("0,,,/@")

        assert not pycat.ipCheck("-1,,,/-1")
        assert not pycat.ipCheck("-1,,,/33")
        assert not pycat.ipCheck("-1,,,/-1.-1.-1.-1")
        assert not pycat.ipCheck("-1,,,/@")

        assert not pycat.ipCheck("256,,,/-1")
        assert not pycat.ipCheck("256,,,/33")
        assert not pycat.ipCheck("256,,,/-1.-1.-1.-1")
        assert not pycat.ipCheck("256,,,/@")

        assert not pycat.ipCheck("a,,,/-1")
        assert not pycat.ipCheck("a,,,/33")
        assert not pycat.ipCheck("a,,,/-1.-1.-1.-1")
        assert not pycat.ipCheck("a,,,/@")


class TestDecisionTableBased:
    def test_RuleA(self):
        "3 points, 4 words, 0 <= numbers <= 255"
        assert pycat.ipCheck("128.128.128.128")

    def test_RuleB(self):
        "Otherwise"
        assert not pycat.ipCheck("abc.-128,400")
