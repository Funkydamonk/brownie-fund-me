from brownie import FundMe
from scripts.helpful import get_account
from scripts.deploy import deploy_fund_me


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    print(f"The current entry fee is {entrance_fee}")
    print("Funding")
    fund_me.fund({"from": account, "value": (entrance_fee * 2)})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    print("Withdrawing funds")
    fund_me.withdraw({"from": account})
    print("Funds have been withdrawn")


def getPrice():
    fund_me = FundMe[-1]
    price = fund_me.getPrice()
    print(price)


def main():
    fund()
    getPrice()
    withdraw()
