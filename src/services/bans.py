import discord


def generate_embed(ban_entry):
    user = ban_entry.user
    embed = discord.Embed(color=discord.Color(0xFF0000))
    embed.title = f"{user.name}#{user.discriminator}"
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="**Reason:**", value=ban_entry.reason)
    return embed


def make_filter(attribute, value):
    def filter_entries(entry):
        return value in getattr(entry.user, attribute).lower()

    return filter_entries


def search_bans(bans, keyword):
    user_name, _, user_discriminator = keyword.partition("#")
    filtered_entries = filter(make_filter("name", user_name.lower()), bans)
    if user_discriminator:
        filtered_entries = filter(make_filter("discriminator", user_discriminator), filtered_entries)
    return list(filtered_entries)
