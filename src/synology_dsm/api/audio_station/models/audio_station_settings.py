class AudioStationSettings:
    def __init__(self, data):
        """Initialize AudioStationSettings object."""
        self._data = data

    @property
    def audio_show_virtual_library(self) -> bool:
        """Return if audio_show_virtual_library is enabled."""
        return self._data["audio_show_virtual_library"]

    @property
    def disable_upnp(self) -> bool:
        """Return disable_upnp status"""
        return self._data["disable_upnp"]

    @property
    def enable_download(self) -> bool:
        """Return enable_download status."""
        return self._data["enable_download"]

    @property
    def prefer_using_html5(self) -> bool:
        """Return if prefer_using_html5 is enabled."""
        return self._data["prefer_using_html5"]

    @property
    def transcode_to_mp3(self) -> bool:
        """Return if prefer_using_html5 is enabled."""
        return self._data["transcode_to_mp3"]
