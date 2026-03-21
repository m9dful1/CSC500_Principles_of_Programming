# Dictionary: insert, update, remove
player_stats = {"health": 100, "wins": 7, "level": 3}

player_stats["weapon"] = "plasma rifle"         # Add new stat
player_stats["health"] = 85                     # Update after taking damage
player_stats.update({"shield": 50, "xp": 340})  # Merge in additional stats
del player_stats["wins"]                        # Remove a stat

print(player_stats)
# Output: {'health': 85, 'level': 3, 'weapon': 'plasma rifle', 'shield': 50, 'xp': 340}