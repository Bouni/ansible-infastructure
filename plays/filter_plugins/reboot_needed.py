from ansible.utils.display import Display

class FilterModule(object):
    def filters(self):
        return {"reboot_needed": self.reboot_needed_filter}

    def reboot_needed_filter(self, host, **kwargs):
        message = f"Host \"{host}\" needs to be rebooted"
        Display().warning(message)
        return message
