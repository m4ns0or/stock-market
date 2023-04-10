import random

# Prices and shares for each stock item
fb_price = 180
fb_shares = 0
goog_price = 1285
goog_shares = 0
msft_price = 161
msft_shares = 0
tsla_price = 702
tsla_shares = 0

# Starting money and day
money = 10000
day = 1

# Run the game for 365 days or until the player goes bankrupt
while day <= 365 and money >= 100:
    # Clear the screen and show the current status
    print(chr(27) + "[2J")
    print("Day", day)
    print("Company Name   Price     Shares Owned")
    print("--------------------------------------")
    print("1. Facebook    ${}        {}".format(fb_price, fb_shares))
    print("2. Google      ${}       {}".format(goog_price, goog_shares))
    print("3. Microsoft   ${}        {}".format(msft_price, msft_shares))
    print("4. Tesla       ${}        {}".format(tsla_price, tsla_shares))
    print("Total value of all shares: ${}".format(fb_price*fb_shares + goog_price*goog_shares + msft_price*msft_shares + tsla_price*tsla_shares))
    print("Total cash on hand: ${}".format(money))
    
    # Show the menu and get the player's choice
    print("\n1. Buy\n2. Sell\n3. End the day")
    choice = input("What would you like to do? ")
    
    # Buy stocks
    if choice == "1":
        stock_choice = input("Which stock would you like to buy (1-4)? ")
        shares = int(input("How many shares would you like to buy? "))
        if stock_choice == "1":
            if money >= fb_price * shares:
                fb_shares += shares
                money -= fb_price * shares
        elif stock_choice == "2":
            if money >= goog_price * shares:
                goog_shares += shares
                money -= goog_price * shares
        elif stock_choice == "3":
            if money >= msft_price * shares:
                msft_shares += shares
                money -= msft_price * shares
        elif stock_choice == "4":
            if money >= tsla_price * shares:
                tsla_shares += shares
                money -= tsla_price * shares
    
    # Sell stocks
    elif choice == "2":
        stock_choice = input("Which stock would you like to sell (1-4)? ")
        shares = int(input("How many shares would you like to sell? "))
        if stock_choice == "1":
            if fb_shares >= shares:
                fb_shares -= shares
                money += fb_price * shares * 0.99
        elif stock_choice == "2":
            if goog_shares >= shares:
                goog_shares -= shares
                money += goog_price * shares * 0.99
        elif stock_choice == "3":
            if msft_shares >= shares:
                msft_shares -= shares
                money += msft_price * shares * 0.99
        elif stock_choice == "4":
            if tsla_shares >= shares:
                tsla_shares -= shares
                money += tsla_price * shares * 0.99
    
# End the day and change stock prices
    elif choice == "3":
        day += 1
        print("End of day", day)
        old_prices = [fb_price, goog_price, msft_price, tsla_price]
        for i in range(len(old_prices)):
            old_price = old_prices[i]
            new_price = max(0.01, round(random.uniform(0.9, 1.1) * old_price, 2))
            print(["Facebook", "Google", "Microsoft", "Tesla"][i], "old price:", old_price, "new price:", new_price)
            if new_price > old_price:
                print(f"The price of {['Facebook', 'Google', 'Microsoft', 'Tesla'][i]} went up from ${old_price} to ${new_price}")
            elif new_price < old_price:
                print(f"The price of {['Facebook', 'Google', 'Microsoft', 'Tesla'][i]} went down from ${old_price} to ${new_price}")
            else:
                print(f"The price of {['Facebook', 'Google', 'Microsoft', 'Tesla'][i]} stayed the same at ${new_price}")
            if i == 0:
                fb_price = new_price
            elif i == 1:
                goog_price = new_price
            elif i == 2:
                msft_price = new_price
            else:
                tsla_price = new_price
        print(f"Day {day} is over. You have ${money} in cash.")
        
# Invalid choice
else:
    print("Invalid choice. Please try again.")       