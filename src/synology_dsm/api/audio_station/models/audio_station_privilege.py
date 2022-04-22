class AudioStationPrivilege:
    def __init__(self, data):
        """Initialize AudioStationPrivilege object"""
        self._data = data

    @property
    def playlist_edit(self) -> bool:
        """Return if user is allowed to edit playlist"""
        return self._data["playlist_edit"]

    @property
    def remote_player(self) -> bool:
        """Return if user is allowed to control remote players"""
        return self._data["remote_player"]

    @property
    def sharing(self) -> bool:
        """Return if user is allowed to share songs"""
        return self._data["sharing"]

    @property
    def tag_edit(self) -> bool:
        """Return if user is allowed to edit tags"""
        return self._data["tag_edit"]

    @property
    def upnp_browse(self) -> bool:
        """Return if user is allowed to browse upnp"""
        return self._data["upnp_browse"]
