def balikkata(kata):
    n = len(kata)
    if n == 0:
        return
    
    balikkata(kata[1:])
    print(kata[0], end='')

balikkata("HALO")
