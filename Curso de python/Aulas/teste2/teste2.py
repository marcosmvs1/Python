cid = str(input(' '))
if (cid[:5].upper() == 'jogo que eu joguei') == True:
    print('SIM vc digitou uma cidade com santo')
elif (cid[:5].upper() == 'SANTO') == False:
    print('Sua cidade não começa com santo')