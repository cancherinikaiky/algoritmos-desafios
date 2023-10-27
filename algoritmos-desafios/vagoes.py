def organiza(vagoes):
    giros = 0
    for e in range(len(vagoes)):
        for i in range(e + 1, len(vagoes)):
            if vagoes[e] > vagoes[i]:
                vagoes[e], vagoes[i] = vagoes[i], vagoes[e]
                giros += 1
    return giros