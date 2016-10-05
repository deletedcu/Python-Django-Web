def coinToss():
    print 'Starting the program...'
    random_number=0
    face='none'
    heads=0
    tails=0

    for i in range(1,5001,1):
        import random
        random_num = random.random()
        random_num = round(random_num)
        if random_num == 1:
            face= 'head'
            heads+=1
        else:
            face= 'tail'
            tails+=1
        print 'Attempt #{}: Throwing a coin... it is a {}! ... Got {} head(s) so far and {} tail(s) so far.'.format(i, face, heads, tails)

    print 'Ending the program, thank you!'

coinToss()
