Portfolio Trade Order Compliance & Execution Checker

A simple Python project that checks proposed portfolio trades before execution. It checks each trade based on cash balance, available holdings, restricted securities, and maximum position limits.

- Validates trade details
- Checks restricted securities
- Checks available holdings for sell orders
- Checks available cash for buy orders
- Calculates position concentration
- Gives three decisions: Approved, Rejected, or Needs Manual Sign-off

Input:
Trade details are provided through a CSV file containing portfolio ID, security ID, action, quantity, price, and security type.

Output :
Each trade gets a decision along with a reason explaining the result.

Technologies used : 
- Python
- CSV
