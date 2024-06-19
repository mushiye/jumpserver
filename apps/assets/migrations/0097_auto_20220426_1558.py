# Generated by Django 3.1.14 on 2022-04-26 07:58

import json

from django.db import migrations

from assets.const import AllTypes

platforms_data_json = '''[
    {
        "category": "host",
        "type": "linux",
        "internal": true,
        "charset": "utf-8",
        "domain_enabled": true,
        "su_enabled": true,
        "name": "Linux",
        "automation": {
            "ansible_enabled": true,
            "ansible_config": {
                "ansible_connection": "smart"
            },
            "ping_enabled": true,
            "gather_facts_enabled": true,
            "gather_accounts_enabled": true,
            "verify_account_enabled": true,
            "change_secret_enabled": true,
            "push_account_enabled": true,
            "ping_method": "posix_ping",
            "gather_facts_method": "gather_facts_posix",
            "gather_accounts_method": "gather_accounts_posix",
            "verify_account_method": "verify_account_posix",
            "change_secret_method": "change_secret_posix",
            "push_account_method": "push_account_posix"
        },
        "protocols": [
            {
                "name": "ssh",
                "port": 22,
                "setting": {
                    "sftp_enabled": true,
                    "sftp_home": "/tmp"
                },
                "primary": true,
                "required": false,
                "default": false
            },
            {
                "name": "telnet",
                "port": 23,
                "required": false,
                "default": false,
                "setting": {}
            },
            {
                "name": "vnc",
                "port": 5900,
                "required": false,
                "default": false,
                "setting": {}
            },
            {
                "name": "rdp",
                "port": 3389,
                "setting": {
                    "console": false,
                    "security": "any"
                },
                "required": false,
                "default": false
            }
        ]
    },
    {
        "category": "host",
        "type": "linux",
        "internal": true,
        "charset": "utf-8",
        "domain_enabled": true,
        "su_enabled": true,
        "name": "Gateway",
        "automation": {
            "ansible_enabled": true,
            "ansible_config": {
                "ansible_connection": "smart"
            },
            "ping_enabled": true,
            "gather_facts_enabled": true,
            "gather_accounts_enabled": true,
            "verify_account_enabled": true,
            "change_secret_enabled": true,
            "push_account_enabled": true,
            "ping_method": "posix_ping",
            "gather_facts_method": "gather_facts_posix",
            "gather_accounts_method": "gather_accounts_posix",
            "verify_account_method": "verify_account_posix",
            "change_secret_method": "change_secret_posix",
            "push_account_method": "push_account_posix"
        },
        "protocols": [
            {
                "name": "ssh",
                "port": 22,
                "setting": {
                    "sftp_enabled": true,
                    "sftp_home": "/tmp"
                },
                "primary": true,
                "required": false,
                "default": false
            },
            {
                "name": "telnet",
                "port": 23,
                "required": false,
                "default": false,
                "setting": {}
            },
            {
                "name": "vnc",
                "port": 5900,
                "required": false,
                "default": false,
                "setting": {}
            },
            {
                "name": "rdp",
                "port": 3389,
                "setting": {
                    "console": false,
                    "security": "any"
                },
                "required": false,
                "default": false
            }
        ]
    },
    {
        "category": "host",
        "type": "unix",
        "internal": true,
        "charset": "utf-8",
        "domain_enabled": true,
        "su_enabled": true,
        "name": "Unix",
        "automation": {
            "ansible_enabled": true,
            "ansible_config": {
                "ansible_connection": "smart"
            },
            "ping_enabled": true,
            "gather_facts_enabled": true,
            "gather_accounts_enabled": true,
            "verify_account_enabled": true,
            "change_secret_enabled": true,
            "push_account_enabled": true,
            "ping_method": "posix_ping",
            "gather_facts_method": "gather_facts_posix",
            "gather_accounts_method": "gather_accounts_posix",
            "verify_account_method": "verify_account_posix",
            "change_secret_method": "change_secret_posix",
            "push_account_method": "push_account_posix"
        },
        "protocols": [
            {
                "name": "ssh",
                "port": 22,
                "setting": {
                    "sftp_enabled": true,
                    "sftp_home": "/tmp"
                },
                "primary": true,
                "required": false,
                "default": false
            },
            {
                "name": "telnet",
                "port": 23,
                "required": false,
                "default": false,
                "setting": {}
            },
            {
                "name": "vnc",
                "port": 5900,
                "required": false,
                "default": false,
                "setting": {}
            },
            {
                "name": "rdp",
                "port": 3389,
                "setting": {
                    "console": false,
                    "security": "any"
                },
                "required": false,
                "default": false
            }
        ]
    },
    {
        "category": "host",
        "type": "unix",
        "internal": true,
        "charset": "utf-8",
        "domain_enabled": true,
        "su_enabled": true,
        "name": "macOS",
        "automation": {
            "ansible_enabled": true,
            "ansible_config": {
                "ansible_connection": "smart"
            },
            "ping_enabled": true,
            "gather_facts_enabled": true,
            "gather_accounts_enabled": true,
            "verify_account_enabled": true,
            "change_secret_enabled": true,
            "push_account_enabled": true,
            "ping_method": "posix_ping",
            "gather_facts_method": "gather_facts_posix",
            "gather_accounts_method": "gather_accounts_posix",
            "verify_account_method": "verify_account_posix",
            "change_secret_method": "change_secret_posix",
            "push_account_method": "push_account_posix"
        },
        "protocols": [
            {
                "name": "ssh",
                "port": 22,
                "setting": {
                    "sftp_enabled": true,
                    "sftp_home": "/tmp"
                },
                "primary": true,
                "required": false,
                "default": false
            },
            {
                "name": "telnet",
                "port": 23,
                "required": false,
                "default": false,
                "setting": {}
            },
            {
                "name": "vnc",
                "port": 5900,
                "required": false,
                "default": false,
                "setting": {}
            },
            {
                "name": "rdp",
                "port": 3389,
                "setting": {
                    "console": false,
                    "security": "any"
                },
                "required": false,
                "default": false
            }
        ]
    },
    {
        "category": "host",
        "type": "unix",
        "internal": true,
        "charset": "utf-8",
        "domain_enabled": true,
        "su_enabled": true,
        "name": "BSD",
        "automation": {
            "ansible_enabled": true,
            "ansible_config": {
                "ansible_connection": "smart"
            },
            "ping_enabled": true,
            "gather_facts_enabled": true,
            "gather_accounts_enabled": true,
            "verify_account_enabled": true,
            "change_secret_enabled": true,
            "push_account_enabled": true,
            "ping_method": "posix_ping",
            "gather_facts_method": "gather_facts_posix",
            "gather_accounts_method": "gather_accounts_posix",
            "verify_account_method": "verify_account_posix",
            "change_secret_method": "change_secret_posix",
            "push_account_method": "push_account_posix"
        },
        "protocols": [
            {
                "name": "ssh",
                "port": 22,
                "setting": {
                    "sftp_enabled": true,
                    "sftp_home": "/tmp"
                },
                "primary": true,
                "required": false,
                "default": false
            },
            {
                "name": "telnet",
                "port": 23,
                "required": false,
                "default": false,
                "setting": {}
            },
            {
                "name": "vnc",
                "port": 5900,
                "required": false,
                "default": false,
                "setting": {}
            },
            {
                "name": "rdp",
                "port": 3389,
                "setting": {
                    "console": false,
                    "security": "any"
                },
                "required": false,
                "default": false
            }
        ]
    },
    {
        "category": "host",
        "type": "unix",
        "internal": true,
        "charset": "utf-8",
        "domain_enabled": true,
        "su_enabled": true,
        "name": "AIX",
        "automation": {
            "ansible_enabled": true,
            "ansible_config": {
                "ansible_connection": "smart"
            },
            "ping_enabled": true,
            "gather_facts_enabled": true,
            "gather_accounts_enabled": true,
            "verify_account_enabled": true,
            "change_secret_enabled": true,
            "push_account_enabled": true,
            "ping_method": "posix_ping",
            "gather_facts_method": "gather_facts_posix",
            "gather_accounts_method": "gather_accounts_posix",
            "verify_account_method": "verify_account_posix",
            "change_secret_method": "change_secret_aix",
            "push_account_method": "push_account_aix"
        },
        "protocols": [
            {
                "name": "ssh",
                "port": 22,
                "setting": {
                    "sftp_enabled": true,
                    "sftp_home": "/tmp"
                },
                "primary": true,
                "required": false,
                "default": false
            },
            {
                "name": "telnet",
                "port": 23,
                "required": false,
                "default": false,
                "setting": {}
            },
            {
                "name": "vnc",
                "port": 5900,
                "required": false,
                "default": false,
                "setting": {}
            },
            {
                "name": "rdp",
                "port": 3389,
                "setting": {
                    "console": false,
                    "security": "any"
                },
                "required": false,
                "default": false
            }
        ]
    },
    {
        "category": "host",
        "type": "windows",
        "internal": true,
        "charset": "utf-8",
        "domain_enabled": true,
        "su_enabled": false,
        "name": "Windows",
        "automation": {
            "ansible_enabled": true,
            "ansible_config": {
                "ansible_shell_type": "cmd",
                "ansible_connection": "ssh"
            },
            "ping_enabled": true,
            "gather_facts_enabled": true,
            "gather_accounts_enabled": true,
            "verify_account_enabled": true,
            "change_secret_enabled": true,
            "push_account_enabled": true,
            "ping_method": "win_ping",
            "gather_facts_method": "gather_facts_windows",
            "gather_accounts_method": "gather_accounts_windows",
            "verify_account_method": "verify_account_windows",
            "change_secret_method": "change_secret_local_windows",
            "push_account_method": "push_account_local_windows"
        },
        "protocols": [
            {
                "name": "rdp",
                "port": 3389,
                "setting": {
                    "console": false,
                    "security": "any"
                },
                "primary": true,
                "required": false,
                "default": false
            },
            {
                "name": "ssh",
                "port": 22,
                "setting": {
                    "sftp_enabled": true,
                    "sftp_home": "/tmp"
                },
                "required": false,
                "default": false
            },
            {
                "name": "vnc",
                "port": 5900,
                "required": false,
                "default": false,
                "setting": {}
            }
        ]
    },
    {
        "category": "host",
        "type": "windows",
        "internal": true,
        "charset": "utf-8",
        "domain_enabled": true,
        "su_enabled": false,
        "name": "Windows-TLS",
        "automation": {
            "ansible_enabled": true,
            "ansible_config": {
                "ansible_shell_type": "cmd",
                "ansible_connection": "ssh"
            },
            "ping_enabled": true,
            "gather_facts_enabled": true,
            "gather_accounts_enabled": true,
            "verify_account_enabled": true,
            "change_secret_enabled": true,
            "push_account_enabled": true,
            "ping_method": "win_ping",
            "gather_facts_method": "gather_facts_windows",
            "gather_accounts_method": "gather_accounts_windows",
            "verify_account_method": "verify_account_windows",
            "change_secret_method": "change_secret_local_windows",
            "push_account_method": "push_account_local_windows"
        },
        "protocols": [
            {
                "name": "rdp",
                "port": 3389,
                "setting": {
                    "console": false,
                    "security": "tls"
                },
                "primary": true,
                "required": false,
                "default": false
            },
            {
                "name": "ssh",
                "port": 22,
                "setting": {
                    "sftp_enabled": true,
                    "sftp_home": "/tmp"
                },
                "required": false,
                "default": false
            },
            {
                "name": "vnc",
                "port": 5900,
                "required": false,
                "default": false,
                "setting": {}
            }
        ]
    },
    {
        "category": "host",
        "type": "windows",
        "internal": true,
        "charset": "utf-8",
        "domain_enabled": true,
        "su_enabled": false,
        "name": "Windows-RDP",
        "automation": {
            "ansible_enabled": true,
            "ansible_config": {
                "ansible_shell_type": "cmd",
                "ansible_connection": "ssh"
            },
            "ping_enabled": true,
            "gather_facts_enabled": true,
            "gather_accounts_enabled": true,
            "verify_account_enabled": true,
            "change_secret_enabled": true,
            "push_account_enabled": true,
            "ping_method": "win_ping",
            "gather_facts_method": "gather_facts_windows",
            "gather_accounts_method": "gather_accounts_windows",
            "verify_account_method": "verify_account_windows",
            "change_secret_method": "change_secret_local_windows",
            "push_account_method": "push_account_local_windows"
        },
        "protocols": [
            {
                "name": "rdp",
                "port": 3389,
                "setting": {
                    "console": false,
                    "security": "rdp"
                },
                "primary": true,
                "required": false,
                "default": false
            },
            {
                "name": "ssh",
                "port": 22,
                "setting": {
                    "sftp_enabled": true,
                    "sftp_home": "/tmp"
                },
                "required": false,
                "default": false
            },
            {
                "name": "vnc",
                "port": 5900,
                "required": false,
                "default": false,
                "setting": {}
            }
        ]
    },
    {
        "category": "host",
        "type": "windows",
        "internal": true,
        "charset": "utf-8",
        "domain_enabled": true,
        "su_enabled": false,
        "name": "RemoteAppHost",
        "automation": {
            "ansible_enabled": true,
            "ansible_config": {
                "ansible_shell_type": "cmd",
                "ansible_connection": "ssh"
            },
            "ping_enabled": true,
            "gather_facts_enabled": true,
            "gather_accounts_enabled": true,
            "verify_account_enabled": true,
            "change_secret_enabled": true,
            "push_account_enabled": true,
            "ping_method": "win_ping",
            "gather_facts_method": "gather_facts_windows",
            "gather_accounts_method": "gather_accounts_windows",
            "verify_account_method": "verify_account_windows",
            "change_secret_method": "change_secret_local_windows",
            "push_account_method": "push_account_local_windows"
        },
        "protocols": [
            {
                "name": "rdp",
                "port": 3389,
                "setting": {
                    "console": false,
                    "security": "any"
                },
                "primary": true,
                "required": false,
                "default": false
            },
            {
                "name": "ssh",
                "port": 22,
                "setting": {
                    "sftp_enabled": true,
                    "sftp_home": "/tmp"
                },
                "required": true,
                "default": false
            }
        ]
    },
    {
        "category": "device",
        "type": "general",
        "internal": true,
        "charset": "utf-8",
        "domain_enabled": true,
        "su_enabled": false,
        "name": "General",
        "automation": {
            "ansible_enabled": false,
            "ansible_config": {
                "ansible_connection": "local"
            },
            "ping_enabled": false,
            "gather_facts_enabled": false,
            "gather_accounts_enabled": false,
            "verify_account_enabled": false,
            "change_secret_enabled": false,
            "push_account_enabled": false
        },
        "protocols": [
            {
                "name": "ssh",
                "port": 22,
                "setting": {
                    "sftp_enabled": true,
                    "sftp_home": "/tmp"
                },
                "primary": true,
                "required": false,
                "default": false
            },
            {
                "name": "telnet",
                "port": 23,
                "required": false,
                "default": false,
                "setting": {}
            }
        ]
    },
    {
        "category": "device",
        "type": "general",
        "internal": true,
        "charset": "utf-8",
        "domain_enabled": true,
        "su_enabled": false,
        "name": "Cisco",
        "automation": {
            "ansible_enabled": false,
            "ansible_config": {
                "ansible_connection": "local"
            },
            "ping_enabled": false,
            "gather_facts_enabled": false,
            "gather_accounts_enabled": false,
            "verify_account_enabled": false,
            "change_secret_enabled": false,
            "push_account_enabled": false
        },
        "protocols": [
            {
                "name": "ssh",
                "port": 22,
                "setting": {
                    "sftp_enabled": true,
                    "sftp_home": "/tmp"
                },
                "primary": true,
                "required": false,
                "default": false
            },
            {
                "name": "telnet",
                "port": 23,
                "required": false,
                "default": false,
                "setting": {}
            }
        ]
    },
    {
        "category": "device",
        "type": "general",
        "internal": true,
        "charset": "utf-8",
        "domain_enabled": true,
        "su_enabled": false,
        "name": "Huawei",
        "automation": {
            "ansible_enabled": false,
            "ansible_config": {
                "ansible_connection": "local"
            },
            "ping_enabled": false,
            "gather_facts_enabled": false,
            "gather_accounts_enabled": false,
            "verify_account_enabled": false,
            "change_secret_enabled": false,
            "push_account_enabled": false
        },
        "protocols": [
            {
                "name": "ssh",
                "port": 22,
                "setting": {
                    "sftp_enabled": true,
                    "sftp_home": "/tmp"
                },
                "primary": true,
                "required": false,
                "default": false
            },
            {
                "name": "telnet",
                "port": 23,
                "required": false,
                "default": false,
                "setting": {}
            }
        ]
    },
    {
        "category": "device",
        "type": "general",
        "internal": true,
        "charset": "utf-8",
        "domain_enabled": true,
        "su_enabled": false,
        "name": "H3C",
        "automation": {
            "ansible_enabled": false,
            "ansible_config": {
                "ansible_connection": "local"
            },
            "ping_enabled": false,
            "gather_facts_enabled": false,
            "gather_accounts_enabled": false,
            "verify_account_enabled": false,
            "change_secret_enabled": false,
            "push_account_enabled": false
        },
        "protocols": [
            {
                "name": "ssh",
                "port": 22,
                "setting": {
                    "sftp_enabled": true,
                    "sftp_home": "/tmp"
                },
                "primary": true,
                "required": false,
                "default": false
            },
            {
                "name": "telnet",
                "port": 23,
                "required": false,
                "default": false,
                "setting": {}
            }
        ]
    },
    {
        "category": "database",
        "type": "mysql",
        "internal": true,
        "charset": "utf-8",
        "domain_enabled": true,
        "su_enabled": false,
        "name": "MySQL",
        "automation": {
            "ansible_enabled": true,
            "ansible_config": {
                "ansible_connection": "local"
            },
            "ping_enabled": true,
            "gather_facts_enabled": false,
            "gather_accounts_enabled": true,
            "verify_account_enabled": true,
            "change_secret_enabled": true,
            "push_account_enabled": true,
            "ping_method": "mysql_ping",
            "gather_accounts_method": "gather_accounts_mysql",
            "verify_account_method": "verify_account_mysql",
            "change_secret_method": "change_secret_mysql",
            "push_account_method": "push_account_mysql"
        },
        "protocols": [
            {
                "name": "mysql",
                "port": 3306,
                "setting": {},
                "required": false,
                "primary": true,
                "default": false
            }
        ]
    },
    {
        "category": "database",
        "type": "mariadb",
        "internal": true,
        "charset": "utf-8",
        "domain_enabled": true,
        "su_enabled": false,
        "name": "MariaDB",
        "automation": {
            "ansible_enabled": true,
            "ansible_config": {
                "ansible_connection": "local"
            },
            "ping_enabled": true,
            "gather_facts_enabled": false,
            "gather_accounts_enabled": true,
            "verify_account_enabled": true,
            "change_secret_enabled": true,
            "push_account_enabled": true,
            "ping_method": "mysql_ping",
            "gather_accounts_method": "gather_accounts_mysql",
            "verify_account_method": "verify_account_mysql",
            "change_secret_method": "change_secret_mysql",
            "push_account_method": "push_account_mysql"
        },
        "protocols": [
            {
                "name": "mariadb",
                "port": 3306,
                "required": false,
                "primary": true,
                "default": false,
                "setting": {}
            }
        ]
    },
    {
        "category": "database",
        "type": "postgresql",
        "internal": true,
        "charset": "utf-8",
        "domain_enabled": true,
        "su_enabled": false,
        "name": "PostgreSQL",
        "automation": {
            "ansible_enabled": true,
            "ansible_config": {
                "ansible_connection": "local"
            },
            "ping_enabled": true,
            "gather_facts_enabled": false,
            "gather_accounts_enabled": true,
            "verify_account_enabled": true,
            "change_secret_enabled": true,
            "push_account_enabled": true,
            "ping_method": "ping_postgresql",
            "gather_accounts_method": "gather_accounts_postgresql",
            "verify_account_method": "verify_account_postgresql",
            "change_secret_method": "change_secret_postgresql",
            "push_account_method": "push_account_postgresql"
        },
        "protocols": [
            {
                "name": "postgresql",
                "port": 5432,
                "required": false,
                "primary": true,
                "default": false,
                "setting": {}
            }
        ]
    },
    {
        "category": "database",
        "type": "oracle",
        "internal": true,
        "charset": "utf-8",
        "domain_enabled": true,
        "su_enabled": false,
        "name": "Oracle",
        "automation": {
            "ansible_enabled": true,
            "ansible_config": {
                "ansible_connection": "local"
            },
            "ping_enabled": true,
            "gather_facts_enabled": false,
            "gather_accounts_enabled": true,
            "verify_account_enabled": true,
            "change_secret_enabled": true,
            "push_account_enabled": true,
            "ping_method": "oracle_ping",
            "gather_accounts_method": "gather_accounts_oracle",
            "verify_account_method": "verify_account_oracle",
            "change_secret_method": "change_secret_oracle",
            "push_account_method": "push_account_oracle"
        },
        "protocols": [
            {
                "name": "oracle",
                "port": 1521,
                "required": false,
                "primary": true,
                "default": false,
                "setting": {}
            }
        ]
    },
    {
        "category": "database",
        "type": "sqlserver",
        "internal": true,
        "charset": "utf-8",
        "domain_enabled": true,
        "su_enabled": false,
        "name": "SQLServer",
        "automation": {
            "ansible_enabled": true,
            "ansible_config": {
                "ansible_connection": "local"
            },
            "ping_enabled": true,
            "gather_facts_enabled": false,
            "gather_accounts_enabled": true,
            "verify_account_enabled": true,
            "change_secret_enabled": true,
            "push_account_enabled": true,
            "ping_method": "sqlserver_ping",
            "verify_account_method": "verify_account_sqlserver",
            "change_secret_method": "change_secret_sqlserver",
            "push_account_method": "push_account_sqlserver"
        },
        "protocols": [
            {
                "name": "sqlserver",
                "port": 1433,
                "required": false,
                "primary": true,
                "default": false,
                "setting": {}
            }
        ]
    },
    {
        "category": "database",
        "type": "clickhouse",
        "internal": true,
        "charset": "utf-8",
        "domain_enabled": true,
        "su_enabled": false,
        "name": "ClickHouse",
        "automation": {
            "ansible_enabled": false,
            "ansible_config": {
                "ansible_connection": "local"
            },
            "ping_enabled": false,
            "gather_facts_enabled": false,
            "gather_accounts_enabled": false,
            "verify_account_enabled": false,
            "change_secret_enabled": false,
            "push_account_enabled": false
        },
        "protocols": [
            {
                "name": "clickhouse",
                "port": 9000,
                "required": false,
                "primary": true,
                "default": false,
                "setting": {}
            }
        ]
    },
    {
        "category": "database",
        "type": "mongodb",
        "internal": true,
        "charset": "utf-8",
        "domain_enabled": true,
        "su_enabled": false,
        "name": "MongoDB",
        "automation": {
            "ansible_enabled": true,
            "ansible_config": {
                "ansible_connection": "local"
            },
            "ping_enabled": true,
            "gather_facts_enabled": false,
            "gather_accounts_enabled": true,
            "verify_account_enabled": true,
            "change_secret_enabled": true,
            "push_account_enabled": true,
            "ping_method": "mongodb_ping",
            "gather_accounts_method": "gather_accounts_mongodb",
            "verify_account_method": "verify_account_mongodb",
            "change_secret_method": "change_secret_mongodb",
            "push_account_method": "push_account_mongodb"
        },
        "protocols": [
            {
                "name": "mongodb",
                "port": 27017,
                "required": false,
                "primary": true,
                "default": false,
                "setting": {}
            }
        ]
    },
    {
        "category": "database",
        "type": "redis",
        "internal": true,
        "charset": "utf-8",
        "domain_enabled": true,
        "su_enabled": false,
        "name": "Redis",
        "automation": {
            "ansible_enabled": false,
            "ansible_config": {
                "ansible_connection": "local"
            },
            "ping_enabled": false,
            "gather_facts_enabled": false,
            "gather_accounts_enabled": false,
            "verify_account_enabled": false,
            "change_secret_enabled": false,
            "push_account_enabled": false
        },
        "protocols": [
            {
                "name": "redis",
                "port": 6379,
                "required": false,
                "setting": {
                    "auth_username": false
                },
                "primary": true,
                "default": false
            }
        ]
    },
    {
        "category": "database",
        "type": "redis",
        "internal": true,
        "charset": "utf-8",
        "domain_enabled": true,
        "su_enabled": false,
        "name": "Redis6+",
        "automation": {
            "ansible_enabled": false,
            "ansible_config": {
                "ansible_connection": "local"
            },
            "ping_enabled": false,
            "gather_facts_enabled": false,
            "gather_accounts_enabled": false,
            "verify_account_enabled": false,
            "change_secret_enabled": false,
            "push_account_enabled": false
        },
        "protocols": [
            {
                "name": "redis",
                "port": 6379,
                "required": false,
                "setting": {
                    "auth_username": true
                },
                "primary": true,
                "default": false
            }
        ]
    },
    {
        "category": "web",
        "type": "website",
        "internal": true,
        "charset": "utf-8",
        "domain_enabled": false,
        "su_enabled": false,
        "name": "Website",
        "automation": {
            "ansible_enabled": false,
            "ping_enabled": false,
            "gather_facts_enabled": false,
            "verify_account_enabled": false,
            "change_secret_enabled": false,
            "push_account_enabled": false,
            "gather_accounts_enabled": false
        },
        "protocols": [
            {
                "name": "http",
                "port": 80,
                "setting": {
                    "username_selector": "name=username",
                    "password_selector": "name=password",
                    "submit_selector": "id=longin_button"
                },
                "primary": true,
                "required": false,
                "default": false
            }
        ]
    },
    {
        "category": "cloud",
        "type": "private",
        "internal": true,
        "charset": "utf-8",
        "domain_enabled": false,
        "su_enabled": false,
        "name": "Vmware-vSphere",
        "automation": {
            "ansible_enabled": false,
            "ansible_config": {},
            "gather_facts_enabled": false,
            "verify_account_enabled": false,
            "change_secret_enabled": false,
            "push_account_enabled": false,
            "gather_accounts_enabled": false
        },
        "protocols": [
            {
                "name": "http",
                "port": 80,
                "setting": {
                    "username_selector": "name=username",
                    "password_selector": "name=password",
                    "submit_selector": "id=longin_button"
                },
                "primary": true,
                "required": false,
                "default": false
            }
        ]
    },
    {
        "category": "cloud",
        "type": "k8s",
        "internal": true,
        "charset": "utf-8",
        "domain_enabled": false,
        "su_enabled": false,
        "name": "Kubernetes",
        "automation": {
            "ansible_enabled": false,
            "ansible_config": {},
            "gather_facts_enabled": false,
            "verify_account_enabled": false,
            "change_secret_enabled": false,
            "push_account_enabled": false,
            "gather_accounts_enabled": false
        },
        "protocols": [
            {
                "name": "k8s",
                "port": 443,
                "required": false,
                "primary": true,
                "default": false,
                "setting": {}
            }
        ]
    }
]'''


def create_internal_platforms(apps, *args):
    platform_cls = apps.get_model('assets', 'Platform')
    platforms_data = json.loads(platforms_data_json)

    for platform_data in platforms_data:
        protocols = platform_data.pop('protocols', [])
        platform_data['protocols'] = [p for p in protocols if p.pop('primary', True) is not None]
        AllTypes.create_or_update_by_platform_data(platform_data, platform_cls=platform_cls)


def update_user_platforms(apps, *args):
    platform_cls = apps.get_model('assets', 'Platform')
    AllTypes.update_user_create_platforms(platform_cls)


def migrate_macos_platform(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    asset_model = apps.get_model('assets', 'Asset')
    platform_model = apps.get_model('assets', 'Platform')
    old_macos = platform_model.objects.using(db_alias).filter(
        name='MacOS', type='macos'
    ).first()
    new_macos = platform_model.objects.using(db_alias).filter(
        name='macOS', type='unix'
    ).first()

    if not old_macos or not new_macos:
        return

    asset_model.objects.using(db_alias).filter(
        platform=old_macos
    ).update(platform=new_macos)

    platform_model.objects.using(db_alias).filter(id=old_macos.id).delete()


def migrate_connectivity(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    asset_model = apps.get_model('assets', 'Asset')
    asset_model.objects.using(db_alias).filter(connectivity='unknown').update(connectivity='-')
    asset_model.objects.using(db_alias).filter(connectivity='failed').update(connectivity='err')


class Migration(migrations.Migration):
    dependencies = [
        ('assets', '0096_auto_20220426_1550'),
    ]

    operations = [
        migrations.RunPython(create_internal_platforms),
        migrations.RunPython(update_user_platforms),
        migrations.RunPython(migrate_macos_platform),
        migrations.RunPython(migrate_connectivity),
    ]