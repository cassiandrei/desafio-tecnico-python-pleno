from herois.models import Heroi


def play_combate(player1id, player2id):
    player1 = Heroi.objects.filter(id=player1id).first()
    player2 = Heroi.objects.filter(id=player2id).first()

    vitorias_player1 = 0
    vitorias_player2 = 0

    #força
    if player1.forca > player2.forca:
        vitorias_player1 += 1
    else:
        vitorias_player2 += 1

    #velocidade
    if player1.velocidade > player2.velocidade:
        vitorias_player1 += 1
    else:
        vitorias_player2 += 1

    if vitorias_player1 == vitorias_player2:
        sum1 = player1.forca + player1.velocidade
        sum2 = player2.forca + player2.velocidade

        if sum1 > sum2:
            vitorias_player1 += 1
        elif sum2 > sum1:
            vitorias_player2 += 1

    if vitorias_player1 == vitorias_player2:
        return 'Empate'

    if vitorias_player1 > vitorias_player2:
        return player1id
    else:
        return player2id


