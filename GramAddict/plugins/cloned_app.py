from GramAddict.core.plugin_loader import Plugin

# Not really a plugin, but didn't wanna add the parameter to core


class ClonedApp(Plugin):
    """Adds support for cloned apps"""

    def __init__(self):
        super().__init__()
        self.description = "Adds support for cloned apps"
        self.arguments = [
            {
                "arg": "--app-id",
                "nargs": 1,
                "help": "provide app-id if using a custom/cloned app",
                "metavar": "com.instagram.android",
                "default": ["com.instagram.android"],
            },
        ]

    def run(self, device, device_id, args, enabled, storage, sessions, plugin):
        pass
