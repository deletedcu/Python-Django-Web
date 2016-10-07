import random

def coin_toss():
    print "Starting Coin Toss!"
    heads = 0
    tails = 0
    for attempt in range(1,5000):
        result = round(random.random())
        if result == 0:
            heads += 1
            print "Attemp #{}: Throwing a coin... It's a head! ... Got {} head(s) so far and {} tail(s) so far.".format (attempt, heads, tails)
        else:
            tails += 1
            print "Attemp #{}: Throwing a coin... It's a tails! ... Got {} head(s) so far and {} tail(s) so far.".format (attempt, heads, tails)
    print "Ending Coin Toss.  Thanks for playing!"

coin_toss()
