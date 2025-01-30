# Bybit REKTrader Bot (C) 2025 Ryan Hayabusa
#
# Github: https://github.com/ryu878
#
# Discord: https://discord.gg/zSw58e9Uvf
#
# Join Bybit and receive up to $6,045 in Bonuses: https://www.bybit.com/invite?ref=P11NJW
#
# Web: https://aadresearch.xyz
#
#######################################################################################################
from _config import *



# Create list of assets to trade

if asset_list_type == 'pre_filtered':
    print(' You Have Selected Pre-Filtered Asset List')

elif asset_list_type == 'all_futures':
    print(' You Have Selected all_futures Asset List')
    
elif asset_list_type == 'custom_list':
    print(' You Have Selected Custom Asset List')