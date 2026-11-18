import unittest

from tools.subnet import inspect


class InspectTests(unittest.TestCase):
    def test_slash_24(self):
        facts = inspect("192.168.1.0/24")
        self.assertEqual(facts["network"], "192.168.1.0")
        self.assertEqual(facts["netmask"], "255.255.255.0")
        self.assertEqual(facts["broadcast"], "192.168.1.255")
        self.assertEqual(facts["total_addresses"], 256)
        self.assertEqual(facts["usable_hosts"], 254)
        self.assertEqual(facts["first_host"], "192.168.1.1")
        self.assertEqual(facts["last_host"], "192.168.1.254")

    def test_host_bits_are_ignored(self):
        facts = inspect("10.0.0.77/8")
        self.assertEqual(facts["network"], "10.0.0.0")
        self.assertEqual(facts["usable_hosts"], 16777214)

    def test_slash_32_has_one_address(self):
        facts = inspect("1.2.3.4/32")
        self.assertEqual(facts["total_addresses"], 1)
        self.assertEqual(facts["usable_hosts"], 1)


if __name__ == "__main__":
    unittest.main()
