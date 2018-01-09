"""Print out all the melons in our inventory."""


from melons import melon_info


def print_melon(melon_info):
    """Print each melon."""
    for melon in melon_info:
        print melon.upper()
        print melon_info[melon][0] + ": " + melon_info[melon][1]

# for i in melon_names:
#     print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])
print_melon(melon_info)
