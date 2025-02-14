![image](https://github.com/user-attachments/assets/ff2a22d2-0405-41e8-84f4-a8869bcdf3c2)

# Announcement: Discontinuation of Free Bots for Bybit 
I regret to inform that I will no longer be updating or maintaining my free trading bots for the Bybit exchange. This decision comes after a deeply disappointing experience with Bybit's unethical practices, particularly regarding their affiliate program and their handling of user earnings.

Despite fully complying with Bybit's rules, including completing KYC (Know Your Customer) requirements, my affiliate earnings were abruptly terminated without valid justification. Bybit cited "one IP address" as the reason, a claim that is both unreasonable and unfair, especially for users in shared living environments or using shared internet connections. This behavior demonstrates a lack of transparency and fairness, and it has eroded my trust in Bybit as a reliable platform.

As a result, I have decided to shift my focus to [BingX](https://bingx.com/invite/HAJ8YQQAG/), a more transparent and user-friendly exchange that aligns with my values of fairness and integrity. Moving forward, I will be developing and updating trading bots exclusively for [BingX](https://bingx.com/invite/HAJ8YQQAG/), and I encourage my community to explore this platform as a viable alternative to Bybit.

I want to thank everyone who has supported my work and used my free bots for Bybit. Your trust and feedback have been invaluable, and I hope to continue providing value to the crypto community through my future projects on [BingX](https://bingx.com/invite/HAJ8YQQAG/). Stay tuned for updates, and feel free to reach out if you have any questions or need assistance during this transition.

Thank you for your understanding and support.

---

# Bybit REKTrader Bot [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://aadresearch.xyz) [![Generic badge](https://img.shields.io/badge/Python-3.8+-<COLOR>.svg)](https://aadresearch.xyz) 
Liquidation-Based Trading Bot (Shorts Only)

[![Latest release](https://badgen.net/github/release/Naereen/Strapdown.js)](https://aadresearch.xyz)

## Overview:
This project is a trading bot designed to leverage liquidation data to identify potential market opportunities and execute short trades. The bot focuses exclusively on short positions, but the architecture is modular, allowing you to easily extend it to support long positions if desired. The primary goal of this project is educational, providing a hands-on opportunity to learn about trading strategies, market data analysis, and algorithmic trading.

## Key Features
1. **Liquidation Data Integration:**
   - The bot monitors liquidation events in real-time using data from Bybit API.
   - It identifies large liquidation clusters, which often indicate potential market reversals or increased volatility.

2. **Short-Only Strategy:**
   - The bot is configured to open short positions when specific liquidation-based conditions are met (e.g., a surge in long liquidations suggesting potential downward pressure).

3. **Risk Management:**
   - Includes averaging and take-profit mechanisms to manage risk.
   - Position sizing is static and you can adjust it using settings.

4. **Modular Design:**
   - The code is structured to allow easy addition of long-position support.
   - Customizable parameters for strategy tuning.

5. **Educational Focus:**
   - The project is designed for learning purposes, with clear documentation and comments in the code.
   - Encourages experimentation with different strategies and parameters.


## How It Works
1. The bot continuously monitors liquidation data from the exchange.
2. When a significant liquidation event occurs (a large number of long positions liquidated), the bot evaluates market conditions.
3. If the conditions align with the strategy, the bot opens a short position.
4. The trade is managed according to predefined risk management rules.

## Future Enhancements (Optional)
- Add support for long positions to create a more balanced strategy.
- Incorporate machine learning models to predict liquidation patterns.
- Integrate additional data sources, such as funding rates or order book depth.
- Improve the backtesting framework with more advanced analytics.


```
git clone git@github.com:ryu878/Bybit_REKTrader_Bot.git

conda create --name Bybit_REKTrader_Bot -c conda-forge python=3.11

conda activate Bybit_REKTrader_Bot

pip install -r requirements.txt
```
## Disclaimer
This project is for informational and educational purposes only. You should not use this information or any other material as legal, tax, investment, financial or other advice. Nothing contained here is a recommendation, endorsement or offer by me to buy or sell any securities or other financial instruments. If you intend to use real money, use it at your own risk. Under no circumstances will I be responsible or liable for any claims, damages, losses, expenses, costs or liabilities of any kind, including but not limited to direct or indirect damages for loss of profits.

## Contacts
I develop trading bots of any complexity, dashboards and indicators for crypto exchanges, forex and stocks.
To contact me:

Discord: https://discord.gg/zSw58e9Uvf

🐀 Join Bybit: https://www.bybit.com/invite?ref=P11NJW

😎 Register on BingX and get a **20% discount** on fees: https://bingx.com/invite/HAJ8YQQAG/

## VPS for bots and scripts
I prefer using DigitalOcean.
  
[![DigitalOcean Referral Badge](https://web-platforms.sfo2.digitaloceanspaces.com/WWW/Badge%202.svg)](https://www.digitalocean.com/?refcode=3d7f6e57bc04&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge)
  
To get $200 in credit over 60 days use my ref link: https://m.do.co/c/3d7f6e57bc04
