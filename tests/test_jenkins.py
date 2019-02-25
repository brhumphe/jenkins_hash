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
        self.assertEqual(2201291178,
                         jenkins.ooat("Character"),
                         "Failed to hash 'Character'")
        self.assertEqual(90817248,
                         jenkins.ooat('ForceField'),
                         "Failed to has 'ForceField'")
        self.assertEqual(254172489,
                         jenkins.ooat('SimpleSpriteParticleEmitter'),
                         "Failed to hash 'SimpleSpriteParticleEmitter'")