from napalm.junos.junos import JunOSDriver
from custom_napalm.yaml import chassis_views


class CustomJunOSDriver(JunOSDriver):
    """NAPALM custom methods."""

    def get_alarms(self):
        """Returns a list of alarms.

            show chassis alarms
        """
        alarms_table = []

        alarms = chassis_views.junos_alarms_table(self.device).get()
        alarms_items = alarms.items()

        for item in alarms_items:
            alarm_entry = {elem[0]: elem[1] for elem in item[1]}
            alarms_table.append(alarm_entry)

        return alarms_table
