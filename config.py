import os


def config():
    return {
        "prefix": {
            "file_name": "prefix.json",
            "default": "$"
        },
        "storage": {
            "folder_name": "storage"
        },
        "status": {
            "file_name": "status.json",
            "default": "minecraft"
        },
        "bot": {
            "token": os.getenv("bot_token")
        },
        "commands": {
            "folder_name": "commands"
        },
        "invite": {
            "client_id": "837510590749474856"
        },
        "badwords": {
            "file_name": "badwords.json"
        },
        "roles": {
            "file_name": "roles.json"
        },
        "developers": [
            474566033798332417,
            356386418722996225
        ],
        "immunes": [
            474566033798332417,
            356386418722996225,
            820361265087643699
        ],
        "vote": {
            "links": [
                "https://minecraftservers.biz/servers/149924/",
                "https://minecraftlist.org/vote/22622",
                "https://minecraft-mp.com/server/284916/vote/",
                "https://www.planetminecraft.com/server/torussmp-whitelist-survival-no-afk-kick-no-land-claim"
                "-community-dreamsmp-like-brand-new/vote/",
                "https://topg.org/minecraft-servers/server-628267",
                "https://minecraftservers.biz/servers/148916/",
                "https://topservers.com/minecraft/in-1866",
                "https://minecraft-server-list.com/server/474969/vote/"
            ]
        }
    }
