# -*- coding: utf-8 -*-
"""Test constants for DSM 6 NAS."""
from .const import (
    SERIAL,
    SESSION_ID,
    UNIQUE_KEY,
    DEVICE_TOKEN,
    SYNO_TOKEN,
    DSM_AUTH_OTP_NOT_SPECIFIED,
)

# DSM 6 RAW DATA
DSM_6_LOGIN = {
    "data": {"is_portal_port": False, "sid": SESSION_ID, "synotoken": SYNO_TOKEN},
    "success": True,
}
DSM_6_LOGIN_2SA = DSM_AUTH_OTP_NOT_SPECIFIED
DSM_6_LOGIN_2SA_OTP = {
    "data": {
        "did": DEVICE_TOKEN,
        "is_portal_port": False,
        "sid": SESSION_ID,
        "synotoken": SYNO_TOKEN,
    },
    "success": True,
}

DSM_6_INFORMATION = {
    "data": {
        "codepage": "fre",
        "model": "DS918+",
        "ram": 4096,
        "serial": SERIAL,
        "temperature": 40,
        "temperature_warn": False,
        "time": "Sun Mar 29 19:33:41 2020",
        "uptime": 155084,
        "version": "24922",
        "version_string": "DSM 6.2.2-24922 Update 4",
    },
    "success": True,
}

DSM_6_UTILIZATION = {
    "data": {
        "cpu": {
            "15min_load": 51,
            "1min_load": 37,
            "5min_load": 33,
            "device": "System",
            "other_load": 3,
            "system_load": 0,
            "user_load": 4,
        },
        "disk": {
            "disk": [
                {
                    "device": "sdc",
                    "display_name": "Drive 3",
                    "read_access": 3,
                    "read_byte": 55261,
                    "type": "internal",
                    "utilization": 12,
                    "write_access": 15,
                    "write_byte": 419425,
                },
                {
                    "device": "sda",
                    "display_name": "Drive 1",
                    "read_access": 3,
                    "read_byte": 63905,
                    "type": "internal",
                    "utilization": 8,
                    "write_access": 14,
                    "write_byte": 414795,
                },
                {
                    "device": "sdb",
                    "display_name": "Drive 2",
                    "read_access": 3,
                    "read_byte": 55891,
                    "type": "internal",
                    "utilization": 10,
                    "write_access": 15,
                    "write_byte": 415658,
                },
            ],
            "total": {
                "device": "total",
                "read_access": 9,
                "read_byte": 175057,
                "utilization": 10,
                "write_access": 44,
                "write_byte": 1249878,
            },
        },
        "lun": [],
        "memory": {
            "avail_real": 156188,
            "avail_swap": 4146316,
            "buffer": 15172,
            "cached": 2764756,
            "device": "Memory",
            "memory_size": 4194304,
            "real_usage": 24,
            "si_disk": 0,
            "so_disk": 0,
            "swap_usage": 6,
            "total_real": 3867268,
            "total_swap": 4415404,
        },
        "network": [
            {"device": "total", "rx": 109549, "tx": 45097},
            {"device": "eth0", "rx": 109549, "tx": 45097},
            {"device": "eth1", "rx": 0, "tx": 0},
        ],
        "space": {
            "total": {
                "device": "total",
                "read_access": 1,
                "read_byte": 27603,
                "utilization": 1,
                "write_access": 23,
                "write_byte": 132496,
            },
            "volume": [
                {
                    "device": "md2",
                    "display_name": "volume1",
                    "read_access": 1,
                    "read_byte": 27603,
                    "utilization": 1,
                    "write_access": 23,
                    "write_byte": 132496,
                }
            ],
        },
        "time": 1585503221,
    },
    "success": True,
}

DSM_6_STORAGE = {
    "data": {
        "disks": [
            {"id": "test_disk"},
            {
                "adv_progress": "",
                "adv_status": "normal",
                "below_remain_life_thr": False,
                "compatibility": "disabled",
                "container": {
                    "order": 0,
                    "str": "DS918+",
                    "supportPwrBtnDisable": False,
                    "type": "internal",
                },
                "device": "/dev/sda",
                "disable_secera": False,
                "diskType": "SATA",
                "disk_code": "ironwolf",
                "erase_time": 448,
                "exceed_bad_sector_thr": False,
                "firm": "SC60",
                "has_system": True,
                "id": "sda",
                "ihm_testing": False,
                "is4Kn": False,
                "isSsd": False,
                "isSynoPartition": True,
                "is_erasing": False,
                "longName": "Drive 1",
                "model": "ST4000VN008-2DR166      ",
                "name": "Drive 1",
                "num_id": 1,
                "order": 1,
                "overview_status": "normal",
                "pciSlot": -1,
                "perf_testing": False,
                "portType": "normal",
                "remain_life": -1,
                "remote_info": {"compatibility": "disabled", "unc": 0},
                "serial": "ZDH4LYTS",
                "size_total": "4000787030016",
                "smart_progress": "",
                "smart_status": "normal",
                "smart_test_limit": 0,
                "smart_testing": False,
                "status": "normal",
                "support": False,
                "temp": 24,
                "testing_progress": "",
                "testing_type": "",
                "tray_status": "join",
                "unc": 0,
                "used_by": "reuse_1",
                "vendor": "Seagate",
            },
            {
                "adv_progress": "",
                "adv_status": "normal",
                "below_remain_life_thr": False,
                "compatibility": "disabled",
                "container": {
                    "order": 0,
                    "str": "DS918+",
                    "supportPwrBtnDisable": False,
                    "type": "internal",
                },
                "device": "/dev/sdb",
                "disable_secera": False,
                "diskType": "SATA",
                "disk_code": "ironwolf",
                "erase_time": 448,
                "exceed_bad_sector_thr": False,
                "firm": "SC60",
                "has_system": True,
                "id": "sdb",
                "ihm_testing": False,
                "is4Kn": False,
                "isSsd": False,
                "isSynoPartition": True,
                "is_erasing": False,
                "longName": "Drive 2",
                "model": "ST4000VN008-2DR166      ",
                "name": "Drive 2",
                "num_id": 2,
                "order": 2,
                "overview_status": "normal",
                "pciSlot": -1,
                "perf_testing": False,
                "portType": "normal",
                "remain_life": -1,
                "remote_info": {"compatibility": "disabled", "unc": 0},
                "serial": "ZDH4LS72",
                "size_total": "4000787030016",
                "smart_progress": "",
                "smart_status": "normal",
                "smart_test_limit": 0,
                "smart_testing": False,
                "status": "normal",
                "support": False,
                "temp": 24,
                "testing_progress": "",
                "testing_type": "",
                "tray_status": "join",
                "unc": 0,
                "used_by": "reuse_1",
                "vendor": "Seagate",
            },
            {
                "adv_progress": "",
                "adv_status": "normal",
                "below_remain_life_thr": False,
                "compatibility": "disabled",
                "container": {
                    "order": 0,
                    "str": "DS918+",
                    "supportPwrBtnDisable": False,
                    "type": "internal",
                },
                "device": "/dev/sdc",
                "disable_secera": False,
                "diskType": "SATA",
                "disk_code": "ironwolf",
                "erase_time": 452,
                "exceed_bad_sector_thr": False,
                "firm": "SC60",
                "has_system": True,
                "id": "sdc",
                "ihm_testing": False,
                "is4Kn": False,
                "isSsd": False,
                "isSynoPartition": True,
                "is_erasing": False,
                "longName": "Drive 3",
                "model": "ST4000VN008-2DR166      ",
                "name": "Drive 3",
                "num_id": 3,
                "order": 3,
                "overview_status": "normal",
                "pciSlot": -1,
                "perf_testing": False,
                "portType": "normal",
                "remain_life": -1,
                "remote_info": {"compatibility": "disabled", "unc": 0},
                "serial": "ZDH4LQ1H",
                "size_total": "4000787030016",
                "smart_progress": "",
                "smart_status": "normal",
                "smart_test_limit": 0,
                "smart_testing": False,
                "status": "normal",
                "support": False,
                "temp": 23,
                "testing_progress": "",
                "testing_type": "",
                "tray_status": "join",
                "unc": 0,
                "used_by": "reuse_1",
                "vendor": "Seagate",
            },
        ],
        "env": {
            "batchtask": {"max_task": 64, "remain_task": 64},
            "bay_number": "4",
            "data_scrubbing": {"sche_enabled": "0", "sche_status": "disabled",},
            "ebox": [],
            "fs_acting": False,
            "isSyncSysPartition": False,
            "is_space_actioning": False,
            "isns": {"address": "", "enabled": False},
            "isns_server": "",
            "max_fs_bytes": "118747255799808",
            "max_fs_bytes_high_end": "219902325555200",
            "model_name": "DS918+",
            "ram_enough_for_fs_high_end": False,
            "ram_size": 4,
            "ram_size_required": 32,
            "showpooltab": False,
            "status": {"system_crashed": False, "system_need_repair": False,},
            "support": {"ebox": True, "raid_cross": True, "sysdef": True,},
            "support_fit_fs_limit": True,
            "unique_key": UNIQUE_KEY,
            "volume_full_critical": 0.1,
            "volume_full_warning": 0.2,
        },
        "hotSpareConf": {"cross_repair": True, "disable_repair": []},
        "hotSpares": [],
        "iscsiLuns": [],
        "iscsiTargets": [],
        "ports": [],
        "ssdCaches": [],
        "storagePools": [
            {
                "cacheStatus": "",
                "can_do": {
                    "data_scrubbing": True,
                    "delete": True,
                    "expand_by_disk": 1,
                    "migrate": {"to_raid5+spare": "1-1", "to_raid6": 1},
                    "raid_cross": True,
                },
                "container": "internal",
                "deploy_path": "volume_1",
                "desc": "Situé sur Groupe de stockage 1, RAID 5",
                "device_type": "raid_5",
                "disk_failure_number": 0,
                "disks": ["sda", "sdb", "sdc"],
                "drive_type": 0,
                "id": "reuse_1",
                "is_actioning": False,
                "is_scheduled": False,
                "is_writable": True,
                "last_done_time": 1551201018,
                "limited_disk_number": 24,
                "maximal_disk_size": "0",
                "minimal_disk_size": "4000681164800",
                "next_schedule_time": 0,
                "num_id": 1,
                "pool_path": "reuse_1",
                "progress": {"percent": "-1", "step": "none"},
                "raidType": "single",
                "raids": [
                    {
                        "designedDiskCount": 3,
                        "devices": [
                            {"id": "sdc", "slot": 2, "status": "normal",},
                            {"id": "sdb", "slot": 1, "status": "normal",},
                            {"id": "sda", "slot": 0, "status": "normal",},
                        ],
                        "hasParity": True,
                        "minDevSize": "4000681164800",
                        "normalDevCount": 3,
                        "raidPath": "/dev/md2",
                        "raidStatus": 1,
                        "spares": [],
                    }
                ],
                "scrubbingStatus": "no_action",
                "size": {"total": "7991698522112", "used": "7991698522112",},
                "space_path": "/dev/md2",
                "ssd_trim": {"support": "not support"},
                "status": "normal",
                "suggestions": [],
                "timebackup": False,
                "vspace_can_do": {
                    "drbd": {
                        "resize": {
                            "can_do": False,
                            "errCode": 53504,
                            "stopService": False,
                        }
                    },
                    "flashcache": {
                        "apply": {"can_do": True, "errCode": 0, "stopService": True,},
                        "remove": {"can_do": True, "errCode": 0, "stopService": False,},
                        "resize": {"can_do": True, "errCode": 0, "stopService": False,},
                    },
                    "snapshot": {
                        "resize": {
                            "can_do": False,
                            "errCode": 53504,
                            "stopService": False,
                        }
                    },
                },
            }
        ],
        "volumes": [
            {"id": "test_volume"},
            {
                "atime_checked": False,
                "atime_opt": "relatime",
                "cacheStatus": "",
                "can_do": {
                    "data_scrubbing": True,
                    "delete": True,
                    "expand_by_disk": 1,
                    "migrate": {"to_raid5+spare": "1-1", "to_raid6": 1},
                    "raid_cross": True,
                },
                "container": "internal",
                "deploy_path": "volume_1",
                "desc": "Situé sur Groupe de stockage 1, RAID 5",
                "device_type": "raid_5",
                "disk_failure_number": 0,
                "disks": [],
                "drive_type": 0,
                "eppool_used": "0",
                "exist_alive_vdsm": False,
                "fs_type": "btrfs",
                "id": "volume_1",
                "is_acting": False,
                "is_actioning": False,
                "is_inode_full": False,
                "is_scheduled": False,
                "is_writable": True,
                "last_done_time": 1551201018,
                "limited_disk_number": 24,
                "max_fs_size": "1152921504606846976",
                "next_schedule_time": 0,
                "num_id": 1,
                "pool_path": "reuse_1",
                "progress": {"percent": "-1", "step": "none"},
                "raidType": "single",
                "scrubbingStatus": "no_action",
                "size": {
                    "free_inode": "0",
                    "total": "7672030584832",
                    "total_device": "7991698522112",
                    "total_inode": "0",
                    "used": "4377452806144",
                },
                "ssd_trim": {"support": "not support"},
                "status": "normal",
                "suggestions": [],
                "timebackup": False,
                "used_by_gluster": False,
                "vol_path": "/volume1",
                "vspace_can_do": {
                    "drbd": {
                        "resize": {
                            "can_do": False,
                            "errCode": 53504,
                            "stopService": False,
                        }
                    },
                    "flashcache": {
                        "apply": {"can_do": True, "errCode": 0, "stopService": True,},
                        "remove": {"can_do": True, "errCode": 0, "stopService": False,},
                        "resize": {"can_do": True, "errCode": 0, "stopService": False,},
                    },
                    "snapshot": {
                        "resize": {
                            "can_do": False,
                            "errCode": 53504,
                            "stopService": False,
                        }
                    },
                },
            },
        ],
    },
    "success": True,
}
