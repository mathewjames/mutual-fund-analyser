#!/usr/bin/python3
# https://stackoverflow.com/a/9865189
# https://askubuntu.com/a/716396

from . import mutual_fund as mf
from .models import Funds

BASE_URL = "https://www.moneycontrol.com/mutual-funds/nav/"

urls = (
    BASE_URL + "aditya-birla-sun-life-equity-fund/MAC006",
    BASE_URL + "axis-bluechip-fund-regular-plan/MAA009",
    BASE_URL + "aditya-birla-sun-life-midcap-fund/MBS027",
    BASE_URL
    + "icici-prudential-india-opportunities-fund-regular-plan/MPI4087",
    BASE_URL
    + "aditya-birla-sun-life-retirement-fund-the-30s-plan-growth/MBS3016",
     BASE_URL + "axis-multicap-fund-regular-plan/MAA739",
     BASE_URL + "sbi-focused-equity-fund/MSB059"
)

for url in urls:
    fund_dict = mf.parse(url)
    fund = Funds(
        url = fund_dict["url"].replace(BASE_URL, ""),
        name = fund_dict["name"],
        aum = fund_dict["aum"],
        snapshot = fund_dict["snapshot"],
        portfolio = fund_dict["portfolio"],
    )
    fund.save()

