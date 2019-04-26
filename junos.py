from napalm.junos.junos import JunOSDriver
from custom_napalm.yaml import chassis_views


class CustomJunOSDriver(JunOSDriver):
    """NAPALM custom methods."""

    def get_serial_numbers(self):
        """ Returns a list of serial numbers 
            show chassis hardware detail
        """
        inventory = chassis_views.junos_inventory_table(self.device)
        inventory.get()
        inventory_items = inventory.items()
        inventory_table = []

        for item in inventory_items:
            inventory_entry = {elem[0]: elem[1] for elem in item[1]}
            inventory_table.append(inventory_entry)

        return inventory_table
