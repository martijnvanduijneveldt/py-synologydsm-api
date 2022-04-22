"""Synology DSM tests."""
import pytest

from src.synology_dsm.api.audio_station import AudioStationInfo
from . import SynologyDSMMock
from . import VALID_HOST
from . import VALID_HTTPS
from . import VALID_OTP
from . import VALID_PASSWORD
from . import VALID_PORT
from . import VALID_USER_2SA
from . import VALID_VERIFY_SSL
from .const import DEVICE_TOKEN
from .const import SESSION_ID
from .const import SYNO_TOKEN
from synology_dsm.const import API_AUTH
from synology_dsm.exceptions import SynologyDSMLogin2SARequiredException


class TestSynologyDSM7:
    """SynologyDSM 7 test cases."""

    def test_login(self, dsm_7):
        """Test login."""
        assert dsm_7.login()
        assert dsm_7.apis.get(API_AUTH)
        assert dsm_7._session_id == SESSION_ID
        assert dsm_7._syno_token == SYNO_TOKEN

    def test_login_2sa(self):
        """Test login with 2SA."""
        dsm_7 = SynologyDSMMock(
            VALID_HOST,
            VALID_PORT,
            VALID_USER_2SA,
            VALID_PASSWORD,
            VALID_HTTPS,
            VALID_VERIFY_SSL,
        )
        dsm_7.dsm_version = 7
        with pytest.raises(SynologyDSMLogin2SARequiredException) as error:
            dsm_7.login()
        error_value = error.value.args[0]
        assert error_value["api"] == "SYNO.API.Auth"
        assert error_value["code"] == 403
        assert error_value["reason"] == "One time password not specified"
        assert (
                error_value["details"]
                == "Two-step authentication required for account: valid_user_2sa"
        )

        assert dsm_7.login(VALID_OTP)

        assert dsm_7._session_id == SESSION_ID
        assert dsm_7._syno_token == SYNO_TOKEN
        assert dsm_7._device_token == DEVICE_TOKEN
        assert dsm_7.device_token == DEVICE_TOKEN

    def test_login_2sa_new_session(self):
        """Test login with 2SA and a new session with granted device."""
        dsm_7 = SynologyDSMMock(
            VALID_HOST,
            VALID_PORT,
            VALID_USER_2SA,
            VALID_PASSWORD,
            VALID_HTTPS,
            VALID_VERIFY_SSL,
            device_token=DEVICE_TOKEN,
        )
        dsm_7.dsm_version = 7
        assert dsm_7.login()

        assert dsm_7._session_id == SESSION_ID
        assert dsm_7._syno_token == SYNO_TOKEN
        assert dsm_7._device_token == DEVICE_TOKEN
        assert dsm_7.device_token == DEVICE_TOKEN

    def test_upgrade(self, dsm_7):
        """Test upgrade."""
        assert dsm_7.upgrade
        dsm_7.upgrade.update()
        assert dsm_7.upgrade.update_available
        assert dsm_7.upgrade.available_version == "7.0.1-42218 Update 3"
        assert dsm_7.upgrade.reboot_needed == "now"
        assert dsm_7.upgrade.service_restarts == "some"
        assert dsm_7.upgrade.available_version_details == {
            "buildnumber": 42218,
            "major": 7,
            "micro": 1,
            "minor": 0,
            "nano": 3,
            "os_name": "DSM",
        }

    def test_audio_station_info(self, dsm_7):
        """Test gettting audio station info"""
        dsm_7.audio_station.update()

        info = dsm_7.audio_station.info
        assert info.browse_personal_library == "all"
        assert info.dsd_decode_capability is True
        assert info.enable_equalizer is False
        assert info.enable_personal_library is False
        assert info.enable_user_home is True
        assert info.has_music_share is True
        assert info.is_manager is True
        assert info.playing_queue_max == 8192
        assert info.privilege.playlist_edit is True
        assert info.privilege.remote_player is True
        assert info.privilege.sharing is True
        assert info.privilege.tag_edit is True
        assert info.privilege.upnp_browse is True
        assert info.remote_controller is False
        assert info.same_subnet is True
        assert info.serial_number == "mySerialNumber"
        assert info.settings.audio_show_virtual_library is True
        assert info.settings.disable_upnp is False
        assert info.settings.enable_download is False
        assert info.settings.prefer_using_html5 is True
        assert info.settings.transcode_to_mp3 is True
        assert info.sid == "mySid"
        assert info.support_bluetooth is False
        assert info.support_usb is False
        assert info.support_virtual_library is True
        assert info.transcode_capability == ["wav", "mp3"]
        assert info.version == 5068
        assert info.version_string == "7.0.0-5068"

    def test_audio_station_remote_player_list(self, dsm_7):
        """Test getting a list of remote players."""
        dsm_7.audio_station.update()
        players = dsm_7.audio_station.remote_players

        assert len(players) == 4

        # get first player
        player = dsm_7.audio_station.get_remote_player(players[0].player.id)
        assert player is not None
        assert player.player.name == "Denon AVR-X2700H (DLNA)"

        assert player.status.state == "transitioning"
        assert player.status.stop_index == 0
        assert player.status.subplayer_volume is None
        assert player.status.volume == 42
        assert player.status.position == 0
        assert player.status.playlist_timestamp == 1650661485

        assert player.status.song.additional.song_audio.bitrate == 320000
        assert player.status.song.additional.song_audio.channel == 1
        assert player.status.song.additional.song_audio.duration == 295
        assert player.status.song.additional.song_audio.filesize == 1
        assert player.status.song.additional.song_audio.frequency == 0

        assert player.status.song.additional.song_tag.album == "25"
        assert player.status.song.additional.song_tag.album_artist == "Adele"
        assert player.status.song.additional.song_tag.artist == "Adele"
        assert player.status.song.additional.song_tag.comment == "Some random comment"
        assert player.status.song.additional.song_tag.composer == "Adele Adkins & Greg Kurstin"
        assert player.status.song.additional.song_tag.disc == 1
        assert player.status.song.additional.song_tag.genre == "Pop"
        assert player.status.song.additional.song_tag.track == 1
        assert player.status.song.additional.song_tag.year == 2015

        assert player.status.song.id == "music_20508"
        assert player.status.song.path == "music/Adele/25 [2015]/CD1 - 01 - Hello.mp3"
        assert player.status.song.title == "Hello"
        assert player.status.song.type == "file"
