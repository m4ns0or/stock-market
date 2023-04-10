# sstock-market-
In this assignment you are to simulate a simple stock market. There will be 4 different stocks that can be bought:
1. Facebook ($180)
2. Google ($1285)
3. Microsoft ($161)
4. Tesla ($702)
The player will be given $10000 to begin their stock trading and can buy or sell stocks at any time. They may buy stocks for free but there is a 1% transaction fee for selling a stock. The simulation will show the value of each stock, the number of shares owned and the player’s net value of all shares owned. On each day, there is an 80% chance that there will be a minor change of each share’s value (A minor change is between 0.5 to 3%, up or down). There is a 15% chance that there will be no change and 5% chance that a major change (a major change is 5% to 15%, up or down). A stock’s value may not be worth less than $0.01. The game will run for 365 days or until the player goes bankrupt (They own no stock and have less than $100). The goal of the game is for the player to double their starting money in the shortest amount of time.
Example:
Day 1:
Company Name Price Shares Owned ==========================================
1. Facebook 2. Google
3. Microsoft 4. Tesla
$180 0 $1285 0 $161 0 $702 0
Total value of all shares: $0 Total cash on hand: $10000
1. Buy
2. Sell
3. End the day
What would you like to do? 1
Which stock would you like to buy (1-4)? 3
How many would you like to buy? 20
<clear screen>
Company Name Price Shares Owned ==========================================
 1. Facebook 2. Google
3. Microsoft 4. Tesla
$180 0 $1285 0 $161 20 $702 0
Total value of all shares: $3220 Total cash on hand: $6780
1. Buy
2. Sell
3. End the day
What would you like to do?

Step 1: The Display
Start by writing the code for the display. For this, you will need to make variables for the price of each stock item and another variable for the quantity of shares for each company. The prices cannot be constants because they will change. You will also need a variable to keep track of the days that have elapsed.
Step 2: The Menu
Add the three-choice menu to the bottom of the display. This should include the input commands for the player’s choice. Put the display and menu inside of a DO-WHILE loop and have this loop run until the day is equal to 365. Use the System(“cls”) command to clear the screen before each day.
Step 3: Buying
Write an IF statement that detects if the user has chosen to buy stocks. If they have chosen to buy stocks, the program will ask which stock they wish to buy. It will then ask how many shares the user wants to buy. The program will check if the user has enough money to afford this transaction and process the change if they do.
Step 4: Selling
Write an IF statement that detects if the user has chosen to sell stocks. If they have chosen to sell stocks, the program will ask which stocks they wish to sell. It will then ask how many shares they wish to sell. The program will check if the user actually owns that many shares. If they do, it will process the transaction and subtract the transaction fee from their money total (1% of the transaction).
Step 5: Changing Stock Prices
Write an IF statement that detects if the user has chosen to End the Day. If they have chosen this option, the program will increment the day by 1. It will also change the stock prices.
How to change the stock prices:
For each stock item, we need to generate a number between 1 and 100. This will be used to determine the type of change that will occur.
If the number is between 0 and 80, there will be a minor change. The program will generate the amount of change that happens. To do this, we need to generate a percentage change between 0.5% and 3%. However, we cannot use the modulus of doubles. To get around this, we generate a number from 5% and 30% and then divide that number by 10.
We then need to determine if the change is going up or down. Generate another number between 0 and 1. If the number is 0, we consider that the change is going up and we change the stock price up by the amount generated. We do the same thing going down if the number is 1.
If the number is between 81 and 85, there will be a major change. We do the same thing as shown above but we generate numbers from 5% to 15%.
If the number is not in either of the above ranges, we do nothing since there is no change.

Step 6: Checking for a win/loss.
In the IF statement for the end of the day, we need to add another set of IF statements to check if the player has won or lost. If the player has no money and no stocks, then they have gone bankrupt. The program should output a message telling them this and return 0 to end the program.
If the player has $20,000 in cash, then they have won the game. The program will tell them they have won the game in X number of days where X is the number of days that have elapsed. It will then return 0 to end the game.
