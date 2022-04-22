from typing import List

from .audio_station_privilege import AudioStationPrivilege
from .audio_station_settings import AudioStationSettings


class AudioStationInfo:

    def __init__(self, data):
        """Initialize Audio Station information."""
        self._data = data

    @property
    def browse_personal_library(self) -> str:
        """Return browse_personal_library."""
        return self._data["browse_personal_library"]

    @property
    def dsd_decode_capability(self) -> bool:
        """Return support for dsd_decode."""
        return self._data["dsd_decode_capability"]

    @property
    def enable_equalizer(self) -> bool:
        """Return enable_equalizer."""
        return self._data["enable_equalizer"]

    @property
    def enable_personal_library(self) -> bool:
        """Return enable_personal_library."""
        return self._data["enable_personal_library"]

    @property
    def enable_user_home(self) -> bool:
        """Return if user own music folder is enabled in user home."""
        return self._data["enable_user_home"]

    @property
    def has_music_share(self) -> bool:
        """Return has_music_share."""
        return self._data["has_music_share"]

    @property
    def is_manager(self) -> bool:
        """Return is_manager."""
        return self._data["is_manager"]

    @property
    def playing_queue_max(self) -> int:
        """Return max size of playing queue."""
        return self._data["playing_queue_max"]

    @property
    def privilege(self) -> AudioStationPrivilege:
        """Return privileges."""
        return AudioStationPrivilege(self._data["privilege"])

    @property
    def remote_controller(self) -> bool:
        """Return if is a remote_controller."""
        return self._data["remote_controller"]

    @property
    def same_subnet(self) -> bool:
        """Return if nas is in same subnet."""
        return self._data["same_subnet"]

    @property
    def serial_number(self) -> str:
        """Return nas serial_number."""
        return self._data["serial_number"]

    @property
    def settings(self) -> AudioStationSettings:
        """Return settings."""
        return AudioStationSettings(self._data["settings"])

    @property
    def sid(self) -> str:
        """Return sid."""
        return self._data["sid"]

    @property
    def support_bluetooth(self) -> bool:
        """Return if nas supports bluetooth playback."""
        return self._data["support_bluetooth"]

    @property
    def support_usb(self) -> bool:
        """Return if nas supports usb playback."""
        return self._data["support_usb"]

    @property
    def support_virtual_library(self) -> bool:
        """Return if nas supports virtual_library."""
        return self._data["support_virtual_library"]

    @property
    def transcode_capability(self) -> List[str]:
        """Return list of support transcode formats."""
        return self._data["transcode_capability"]

    @property
    def version(self) -> int:
        """Return version of audio station build."""
        return self._data["version"]

    @property
    def version_string(self) -> int:
        """Return version string of audio station."""
        return self._data["version_string"]
