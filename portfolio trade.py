import csv

with open("trades_test.csv","r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        pid = row["portfolio_id"]
        sid = row["security_id"]
        act = row["action"]
        qty = int(row["quantity"])
        price = float(row["price"])
        stype = row["security_type"]

        cash = 10000
        restricted = ["ABC", "LMN"]

        holdings = [("XYZ", 50, 100), ("DEF", 20, 50)]
        max_pct = 1 / (len(holdings) + 1)

        decision = "Approved"
        reason = "Trade passed all checks."

        if qty <= 0 or price <= 0:
            decision = "Rejected"
            reason = "Invalid trade data."

        elif act not in ["Buy", "Sell"]:
            decision = "Rejected"
            reason = "Invalid trade data."

        if decision == "Approved":

            if sid in restricted:
                decision = "Rejected"
                reason = "Security is restricted for this portfolio."

        if decision == "Approved" and act == "Sell":

            old_qty = 0
            for h in holdings:
                if h[0] == sid:
                    old_qty = h[1]

            if old_qty < qty:
                decision = "Rejected"
                reason = "Insufficient holdings to sell."

        if decision == "Approved" and act == "Buy":

            cost = qty * price
            if cost > cash:
                decision = "Rejected"
                reason = "Insufficient cash for this buy order."

        if decision == "Approved" and act == "Buy":

            new_cash = cash - (qty * price)
            old_qty = 0
            for h in holdings:
                if h[0] == sid:
                    old_qty = h[1]

            new_qty = old_qty + qty

            stock_value = new_qty * price

            other_value = 0

            for h in holdings:
                if h[0] != sid:
                    other_value+=h[1] * h[2]
                  
            total = new_cash+stock_value + other_value
            pct = stock_value/total

            if pct > max_pct:
                decision = "Needs Manual Sign-off"
                reason = "Exceeds maximum position concentration - requires approval."

        print("Portfolio ID:", pid)
        print("Security ID:", sid)
        print("Action:", act)
        print("Quantity:", qty)
        print("Price:", price)
        print("Security Type:", stype)

        print("Decision:", decision)
        print("Reason:", reason)
        print("-------End--------\n")
