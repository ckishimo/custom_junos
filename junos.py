from napalm.junos.junos import JunOSDriver
from custom_napalm.yaml import layer2_views


class CustomJunOSDriver(JunOSDriver):
    """NAPALM custom methods."""

    def get_vlans(self):
        """ Returns a list of vlans and ports
            show vlans
        """
        vlans = layer2_views.junos_vlans_table(self.device)
        vlans.get()
        vlans_items = vlans.items()
        vlans_table = []

        return vlans_table
