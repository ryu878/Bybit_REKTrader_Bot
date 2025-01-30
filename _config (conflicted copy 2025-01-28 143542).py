risk_limit_base_value = 100000
deleverage_steps = 3

taker_fee = 0.075 # 0.02, 0.055
taker_mult = 4  # 0.3%

min_notional_value = 5
min_notional_value_mult = 1

max_account_leverage = 20
max_bots = 5
max_pos_divider = 200

bybit_api_key = ''
bybit_api_secret = ''

aadreseach_token = ''

acc_type = 'UNIFIED'
coin = 'USDT'
category = 'linear'

entry_order_timeInForce = 'PostOnly'
entry_sell_order_side = 'Sell'
entry_sell_order_type = 'Limit'
entry_buy_order_side = 'Buy'
entry_buy_order_type = 'Limit'

tp_order_timeInForce = 'PostOnly'
tp_buy_order_side = 'Buy'
tp_buy_order_type = 'Limit'
tp_buy_deleverage_order_type = 'Market'
tp_sell_order_side = 'Sell'
tp_sell_order_type = 'Limit'
tp_sell_deleverage_order_type = 'Market'

# asset_list_type = 'pre_filtered' # Use Pre Filtered Most Liquiduty Assets from AAD Research API
# asset_list_type = 'all_futures' # Trade using all Perpetual Futures on Bybit
asset_list_type = 'custom_list' # Create Your Custom List of Assets to Trade

custom_list = ['BTCUSDT', 'ETHUSDT']