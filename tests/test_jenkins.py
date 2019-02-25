from unittest import TestCase

import jenkins


class TestLookup2(TestCase):
    def test_lookup2(self):
        self.assertEqual(jenkins.lookup2("foobar"),
                         0x9D3FFA02)
        self.assertEqual(jenkins.lookup2(""),
                         0)
        self.assertEqual(jenkins.lookup2("hello world"),
                         0x1AA919E6)
        self.assertEqual(jenkins.lookup2("           "),
                         0xF55976FA)
        self.assertEqual(jenkins.lookup2("1234567890abcdefghijklmnopqstuvwxyz"),
                         0x49EAEE3E)
        self.assertEqual(jenkins.lookup2("This is the time for all good men to come to the aid of their country"),
                         0xCF874E3D)

    def test_ooat(self):
        self.assertEqual(jenkins.ooat("foobar"),
                         0xF952FDE7)
        self.assertEqual(jenkins.ooat(""),
                         0)
        self.assertEqual(jenkins.ooat("hello world"),
                         0x3E4A5A57)
        self.assertEqual(jenkins.ooat("           "),
                         0x9AEAF441)
        self.assertEqual(jenkins.ooat("1234567890abcdefghijklmnopqstuvwxyz"),
                         0xB77A0169)
        self.assertEqual(jenkins.ooat("This is the time for all good men to come to the aid of their country"),
                         0x768ECFFE)
