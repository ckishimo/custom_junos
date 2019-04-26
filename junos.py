from napalm.junos.junos import JunOSDriver
from custom_napalm.yaml import layer2_views


class CustomJunOSDriver(JunOSDriver):
    """NAPALM custom methods."""

    def get_vlans(self):
        """ Returns a list of vlans and ports
            show vlans
        """
        vlans = layer2_views.junos_vlans_table(self.device).get()
        vlans_items = vlans.items()
        vlans_table = []

        for vlan_table_entry in vlans_items:
            vlan_entry = {elem[0]: elem[1] for elem in vlan_table_entry[1]}
            vlans_table.append(vlan_entry)

        return vlans_table
