# BankAccount

BankAccount is a class for using your termial as a ATM

## Installation

Git clone or download the repo/folder to use BankAccount.

```bash
git clone git@github.com:edison4354/WEB_1.1-Homework-2-Forms.git
```

## Usage

```python
import BankAccount

edison_account = BankAccount("Edison Li")

edison_account.deposit() # returns a input for the amount you wish to deposit 
edison_account.withdraw() # returns a input for the amount you wish to withdraw 
edison_account.get_balance() # returns the current balance of your account
edison_account.add_interest() # returns a new balance with the interest added
edison_account.print_receipt() # returns a receipt of your name, account number, routing number, and balance
```

## Contributing
For changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)