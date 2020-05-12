def find_amount(Tab,Money,amount):
    if Tab[amount]!=-1:
        return Tab[amount]
    else:
        miin=100000000
        for money in Money:
            if amount-money>=0:
                if miin>(find_amount(Tab,Money,amount-money)+1):
                    miin = Tab[amount-money]+1
        Tab[amount]=miin
        return Tab[amount]

Money=[1,5,8]
Tab=[-1 for i in range(16)]
Tab[0]=0
print(find_amount(Tab,Money,15))
