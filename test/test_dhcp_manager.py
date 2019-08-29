import unittest
from .. import dhcp_manager


class TestDhcpManager(unittest.TestCase):

    def setUp(self):
        self.dhcp_manager = dhcp_manager.DHCPManager()

    def test_parse_file(self):
        FILE = "test.conf"
        self.assertEqual(self.dhcp_manager.parse_file(FILE), False)

        FILE = "dhcp.conf"
        self.assertEqual(self.dhcp_manager.parse_file(FILE), True)

        result = """option domain-name "example.org";
        option domain-name-servers ns1.example.org, ns2.example.org;
        default-lease-time 600;
        max-lease-time 7200;
        ddns-update-style none;
        subnet 10.5.5.0 netmask 255.255.255.224 {
        range 10.5.5.26 10.5.5.30;
        option domain-name-servers ns1.internal.example.org;
        option domain-name "internal.example.org";
        option subnet-mask 255.255.255.224;
        option routers 10.5.5.1;
        option broadcast-address 10.5.5.31;
        default-lease-time 600;
        max-lease-time 7200;
        }"""

        arr_data = result.split("\n")
        arr_data_parse = str(self.dhcp_manager).split("\n")

        for i in range(0, len(arr_data) - 1):
            self.assertEqual(arr_data[i].strip(), arr_data_parse[i].strip())    
        
    def test_add_line_config(self):
        self.dhcp_manager.add_line_config("hello world;")

if __name__ == '__main__':
    unittest.main()