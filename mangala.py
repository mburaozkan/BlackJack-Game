import tkinter


def zero():
    global player1_1_int
    global player1_2_int
    global player1_3_int
    global player1_4_int
    global player1_5_int
    global player1_6_int
    global player2_1_int
    global player2_2_int
    global player2_3_int
    global player2_4_int
    global player2_5_int
    global player2_6_int
    global turn
    if player1_1_int.get() + player1_2_int.get() + player1_3_int.get() + player1_4_int.get() + player1_5_int.get() \
            + player1_6_int.get() == 0:
        player1_7_int.set(
            player1_7_int.get() + player2_1_int.get() + player2_2_int.get() + player2_3_int.get() + player2_4_int.get()
            + player2_5_int.get() + player2_6_int.get())
        player2_1_int.set(0)
        player2_2_int.set(0)
        player2_3_int.set(0)
        player2_4_int.set(0)
        player2_5_int.set(0)
        player2_6_int.set(0)
        turn = -1
        if player1_7_int.get() > player2_0_int.get():
            turn_and_winner_text.set('1. Oyuncu Kazandı !!!')
        if player1_7_int.get() < player2_0_int.get():
            turn_and_winner_text.set('2. Oyuncu Kazandı !!!')
        if player1_7_int.get() == player2_0_int.get():
            turn_and_winner_text.set('Oyun Berabere Bitti !!!')
    if player2_1_int.get() + player2_2_int.get() + player2_3_int.get() + player2_4_int.get() + player2_5_int.get() \
            + player2_6_int.get() == 0:
        player2_0_int.set(
            player2_0_int.get() + player1_1_int.get() + player1_2_int.get() + player1_3_int.get() + player1_4_int.get()
            + player1_5_int.get() + player1_6_int.get())
        player1_1_int.set(0)
        player1_2_int.set(0)
        player1_3_int.set(0)
        player1_4_int.set(0)
        player1_5_int.set(0)
        player1_6_int.set(0)
        turn = -1
        if player1_7_int.get() > player2_0_int.get():
            turn_and_winner_text.set('1. Oyuncu Kazandı !!!')
        if player1_7_int.get() < player2_0_int.get():
            turn_and_winner_text.set('2. Oyuncu Kazandı !!!')
        if player1_7_int.get() == player2_0_int.get():
            turn_and_winner_text.set('Oyun Berabere Bitti !!!')


def queue():
    global turn
    if turn == -1:
        pass
    else:
        turn += 1
        print(turn)
        if turn % 2 == 0:
            turn_and_winner_text.set('1. Oyuncunun Sırası')
        if turn % 2 == 1:
            turn_and_winner_text.set('2. Oyuncunun Sırası')


def spereader1():
    zero()
    while player1_1_int.get() != 0 and turn % 2 == 0:
        if player1_1_int.get() == 1:
            player1_1_int.set(0)
            player1_2_int.set(player1_2_int.get() + 1)
            if player1_2_int.get() == 1 and player2_2_int.get() != 0:
                player1_7_int.set(player1_7_int.get() + player1_2_int.get() + player2_2_int.get())
                player2_2_int.set(0)
                player1_2_int.set(0)
            queue()

        if player1_1_int.get() == 2:
            player1_1_int.set(0)
            player1_2_int.set(player1_2_int.get() + 1)
            player1_3_int.set(player1_3_int.get() + 1)
            if player1_3_int.get() == 1 and player2_3_int.get() != 0:
                player1_7_int.set(player1_7_int.get() + player1_3_int.get() + player2_3_int.get())
                player2_3_int.set(0)
                player1_3_int.set(0)
            queue()

        if player1_1_int.get() == 3:
            player1_1_int.set(0)
            player1_2_int.set(player1_2_int.get() + 1)
            player1_3_int.set(player1_3_int.get() + 1)
            player1_4_int.set(player1_4_int.get() + 1)
            if player1_4_int.get() == 1 and player2_4_int.get() != 0:
                player1_7_int.set(player1_7_int.get() + player1_4_int.get() + player2_4_int.get())
                player2_4_int.set(0)
                player1_4_int.set(0)
            queue()

        if player1_1_int.get() == 4:
            player1_1_int.set(0)
            player1_2_int.set(player1_2_int.get() + 1)
            player1_3_int.set(player1_3_int.get() + 1)
            player1_4_int.set(player1_4_int.get() + 1)
            player1_5_int.set(player1_5_int.get() + 1)
            if player1_5_int.get() == 1 and player2_5_int.get() != 0:
                player1_7_int.set(player1_7_int.get() + player1_5_int.get() + player2_5_int.get())
                player2_5_int.set(0)
                player1_5_int.set(0)
            queue()

        if player1_1_int.get() == 5:
            player1_1_int.set(0)
            player1_2_int.set(player1_2_int.get() + 1)
            player1_3_int.set(player1_3_int.get() + 1)
            player1_4_int.set(player1_4_int.get() + 1)
            player1_5_int.set(player1_5_int.get() + 1)
            player1_6_int.set(player1_6_int.get() + 1)
            if player1_6_int.get() == 1 and player2_6_int.get() != 0:
                player1_7_int.set(player1_7_int.get() + player1_6_int.get() + player2_6_int.get())
                player2_6_int.set(0)
                player1_6_int.set(0)
            queue()

        if player1_1_int.get() == 6:
            player1_1_int.set(0)
            player1_2_int.set(player1_2_int.get() + 1)
            player1_3_int.set(player1_3_int.get() + 1)
            player1_4_int.set(player1_4_int.get() + 1)
            player1_5_int.set(player1_5_int.get() + 1)
            player1_6_int.set(player1_6_int.get() + 1)
            player1_7_int.set(player1_7_int.get() + 1)

        if player1_1_int.get() == 7:
            player1_1_int.set(0)
            player1_2_int.set(player1_2_int.get() + 1)
            player1_3_int.set(player1_3_int.get() + 1)
            player1_4_int.set(player1_4_int.get() + 1)
            player1_5_int.set(player1_5_int.get() + 1)
            player1_6_int.set(player1_6_int.get() + 1)
            player1_7_int.set(player1_7_int.get() + 1)
            player2_6_int.set(player2_6_int.get() + 1)
            if player2_6_int.get() % 2 == 0:
                player1_7_int.set(player1_7_int.get() + player2_6_int.get())
                player2_6_int.set(0)
            queue()

        if player1_1_int.get() == 8:
            player1_1_int.set(0)
            player1_2_int.set(player1_2_int.get() + 1)
            player1_3_int.set(player1_3_int.get() + 1)
            player1_4_int.set(player1_4_int.get() + 1)
            player1_5_int.set(player1_5_int.get() + 1)
            player1_6_int.set(player1_6_int.get() + 1)
            player1_7_int.set(player1_7_int.get() + 1)
            player2_6_int.set(player2_6_int.get() + 1)
            player2_5_int.set(player2_5_int.get() + 1)
            if player2_5_int.get() % 2 == 0:
                player1_7_int.set(player1_7_int.get() + player2_5_int.get())
                player2_5_int.set(0)
            queue()

        if player1_1_int.get() == 9:
            player1_1_int.set(0)
            player1_2_int.set(player1_2_int.get() + 1)
            player1_3_int.set(player1_3_int.get() + 1)
            player1_4_int.set(player1_4_int.get() + 1)
            player1_5_int.set(player1_5_int.get() + 1)
            player1_6_int.set(player1_6_int.get() + 1)
            player1_7_int.set(player1_7_int.get() + 1)
            player2_6_int.set(player2_6_int.get() + 1)
            player2_5_int.set(player2_5_int.get() + 1)
            player2_4_int.set(player2_4_int.get() + 1)
            if player2_4_int.get() % 2 == 0:
                player1_7_int.set(player1_7_int.get() + player2_4_int.get())
                player2_4_int.set(0)
            queue()

        if player1_1_int.get() == 10:
            player1_1_int.set(0)
            player1_2_int.set(player1_2_int.get() + 1)
            player1_3_int.set(player1_3_int.get() + 1)
            player1_4_int.set(player1_4_int.get() + 1)
            player1_5_int.set(player1_5_int.get() + 1)
            player1_6_int.set(player1_6_int.get() + 1)
            player1_7_int.set(player1_7_int.get() + 1)
            player2_6_int.set(player2_6_int.get() + 1)
            player2_5_int.set(player2_5_int.get() + 1)
            player2_4_int.set(player2_4_int.get() + 1)
            player2_3_int.set(player2_3_int.get() + 1)
            if player2_3_int.get() % 2 == 0:
                player1_7_int.set(player1_7_int.get() + player2_3_int.get())
                player2_3_int.set(0)
            queue()


def spereader2():
    zero()
    while player1_2_int.get() != 0 and turn % 2 == 0:
        if player1_2_int.get() == 1:
            player1_2_int.set(0)
            player1_3_int.set(player1_3_int.get() + 1)
            if player1_3_int.get() == 1 and player2_3_int.get() != 0:
                player1_7_int.set(player1_7_int.get() + player1_3_int.get() + player2_3_int.get())
                player2_3_int.set(0)
                player1_3_int.set(0)
            queue()

        if player1_2_int.get() == 2:
            player1_2_int.set(0)
            player1_3_int.set(player1_3_int.get() + 1)
            player1_4_int.set(player1_4_int.get() + 1)
            if player1_4_int.get() == 1 and player2_4_int.get() != 0:
                player1_7_int.set(player1_7_int.get() + player1_4_int.get() + player2_4_int.get())
                player2_4_int.set(0)
                player1_4_int.set(0)
            queue()

        if player1_2_int.get() == 3:
            player1_2_int.set(0)
            player1_3_int.set(player1_3_int.get() + 1)
            player1_4_int.set(player1_4_int.get() + 1)
            player1_5_int.set(player1_5_int.get() + 1)
            if player1_5_int.get() == 1 and player2_5_int.get() != 0:
                player1_7_int.set(player1_7_int.get() + player1_5_int.get() + player2_5_int.get())
                player2_5_int.set(0)
                player1_5_int.set(0)
            queue()

        if player1_2_int.get() == 4:
            player1_2_int.set(0)
            player1_3_int.set(player1_3_int.get() + 1)
            player1_4_int.set(player1_4_int.get() + 1)
            player1_5_int.set(player1_5_int.get() + 1)
            player1_6_int.set(player1_6_int.get() + 1)
            if player1_6_int.get() == 1 and player2_6_int.get() != 0:
                player1_7_int.set(player1_7_int.get() + player1_6_int.get() + player2_6_int.get())
                player2_6_int.set(0)
                player1_6_int.set(0)
            queue()

        if player1_2_int.get() == 5:
            player1_2_int.set(0)
            player1_3_int.set(player1_3_int.get() + 1)
            player1_4_int.set(player1_4_int.get() + 1)
            player1_5_int.set(player1_5_int.get() + 1)
            player1_6_int.set(player1_6_int.get() + 1)
            player1_7_int.set(player1_7_int.get() + 1)

        if player1_2_int.get() == 6:
            player1_2_int.set(0)
            player1_3_int.set(player1_3_int.get() + 1)
            player1_4_int.set(player1_4_int.get() + 1)
            player1_5_int.set(player1_5_int.get() + 1)
            player1_6_int.set(player1_6_int.get() + 1)
            player1_7_int.set(player1_7_int.get() + 1)
            player2_6_int.set(player2_6_int.get() + 1)
            if player2_6_int.get() % 2 == 0:
                player1_7_int.set(player1_7_int.get() + player2_6_int.get())
                player2_6_int.set(0)
            queue()

        if player1_2_int.get() == 7:
            player1_2_int.set(0)
            player1_3_int.set(player1_3_int.get() + 1)
            player1_4_int.set(player1_4_int.get() + 1)
            player1_5_int.set(player1_5_int.get() + 1)
            player1_6_int.set(player1_6_int.get() + 1)
            player1_7_int.set(player1_7_int.get() + 1)
            player2_6_int.set(player2_6_int.get() + 1)
            player2_5_int.set(player2_5_int.get() + 1)
            if player2_5_int.get() % 2 == 0:
                player1_7_int.set(player1_7_int.get() + player2_5_int.get())
                player2_5_int.set(0)
            queue()

        if player1_2_int.get() == 8:
            player1_2_int.set(0)
            player1_3_int.set(player1_3_int.get() + 1)
            player1_4_int.set(player1_4_int.get() + 1)
            player1_5_int.set(player1_5_int.get() + 1)
            player1_6_int.set(player1_6_int.get() + 1)
            player1_7_int.set(player1_7_int.get() + 1)
            player2_6_int.set(player2_6_int.get() + 1)
            player2_5_int.set(player2_5_int.get() + 1)
            player2_4_int.set(player2_4_int.get() + 1)
            if player2_4_int.get() % 2 == 0:
                player1_7_int.set(player1_7_int.get() + player2_4_int.get())
                player2_4_int.set(0)
            queue()

        if player1_2_int.get() == 9:
            player1_2_int.set(0)
            player1_3_int.set(player1_3_int.get() + 1)
            player1_4_int.set(player1_4_int.get() + 1)
            player1_5_int.set(player1_5_int.get() + 1)
            player1_6_int.set(player1_6_int.get() + 1)
            player1_7_int.set(player1_7_int.get() + 1)
            player2_6_int.set(player2_6_int.get() + 1)
            player2_5_int.set(player2_5_int.get() + 1)
            player2_4_int.set(player2_4_int.get() + 1)
            player2_3_int.set(player2_3_int.get() + 1)
            if player2_3_int.get() % 2 == 0:
                player1_7_int.set(player1_7_int.get() + player2_3_int.get())
                player2_3_int.set(0)
            queue()

        if player1_2_int.get() == 10:
            player1_2_int.set(0)
            player1_3_int.set(player1_3_int.get() + 1)
            player1_4_int.set(player1_4_int.get() + 1)
            player1_5_int.set(player1_5_int.get() + 1)
            player1_6_int.set(player1_6_int.get() + 1)
            player1_7_int.set(player1_7_int.get() + 1)
            player2_6_int.set(player2_6_int.get() + 1)
            player2_5_int.set(player2_5_int.get() + 1)
            player2_4_int.set(player2_4_int.get() + 1)
            player2_3_int.set(player2_3_int.get() + 1)
            player2_2_int.set(player2_2_int.get() + 1)
            if player2_2_int.get() % 2 == 0:
                player1_7_int.set(player1_7_int.get() + player2_2_int.get())
                player2_2_int.set(0)
            queue()


def spereader3():
    zero()
    while player1_3_int.get() != 0 and turn % 2 == 0:
        if player1_3_int.get() == 1:
            player1_3_int.set(0)
            player1_4_int.set(player1_4_int.get() + 1)
            if player1_4_int.get() == 1 and player2_4_int.get() != 0:
                player1_7_int.set(player1_7_int.get() + player1_4_int.get() + player2_4_int.get())
                player2_4_int.set(0)
                player1_4_int.set(0)
            queue()

        if player1_3_int.get() == 2:
            player1_3_int.set(0)
            player1_4_int.set(player1_4_int.get() + 1)
            player1_5_int.set(player1_5_int.get() + 1)
            if player1_5_int.get() == 1 and player2_5_int.get() != 0:
                player1_7_int.set(player1_7_int.get() + player1_5_int.get() + player2_5_int.get())
                player2_5_int.set(0)
                player1_5_int.set(0)
            queue()

        if player1_3_int.get() == 3:
            player1_3_int.set(0)
            player1_4_int.set(player1_4_int.get() + 1)
            player1_5_int.set(player1_5_int.get() + 1)
            player1_6_int.set(player1_6_int.get() + 1)
            if player1_6_int.get() == 1 and player2_6_int.get() != 0:
                player1_7_int.set(player1_7_int.get() + player1_6_int.get() + player2_6_int.get())
                player2_6_int.set(0)
                player1_6_int.set(0)
            queue()
        if player1_3_int.get() == 4:
            player1_3_int.set(0)
            player1_4_int.set(player1_4_int.get() + 1)
            player1_5_int.set(player1_5_int.get() + 1)
            player1_6_int.set(player1_6_int.get() + 1)
            player1_7_int.set(player1_7_int.get() + 1)

        if player1_3_int.get() == 5:
            player1_3_int.set(0)
            player1_4_int.set(player1_4_int.get() + 1)
            player1_5_int.set(player1_5_int.get() + 1)
            player1_6_int.set(player1_6_int.get() + 1)
            player1_7_int.set(player1_7_int.get() + 1)
            player2_6_int.set(player2_6_int.get() + 1)
            if player2_6_int.get() % 2 == 0:
                player1_7_int.set(player1_7_int.get() + player2_6_int.get())
                player2_6_int.set(0)
            queue()

        if player1_3_int.get() == 6:
            player1_3_int.set(0)
            player1_4_int.set(player1_4_int.get() + 1)
            player1_5_int.set(player1_5_int.get() + 1)
            player1_6_int.set(player1_6_int.get() + 1)
            player1_7_int.set(player1_7_int.get() + 1)
            player2_6_int.set(player2_6_int.get() + 1)
            player2_5_int.set(player2_5_int.get() + 1)
            if player2_5_int.get() % 2 == 0:
                player1_7_int.set(player1_7_int.get() + player2_5_int.get())
                player2_5_int.set(0)
            queue()

        if player1_3_int.get() == 7:
            player1_3_int.set(0)
            player1_4_int.set(player1_4_int.get() + 1)
            player1_5_int.set(player1_5_int.get() + 1)
            player1_6_int.set(player1_6_int.get() + 1)
            player1_7_int.set(player1_7_int.get() + 1)
            player2_6_int.set(player2_6_int.get() + 1)
            player2_5_int.set(player2_5_int.get() + 1)
            player2_4_int.set(player2_4_int.get() + 1)
            if player2_4_int.get() % 2 == 0:
                player1_7_int.set(player1_7_int.get() + player2_4_int.get())
                player2_4_int.set(0)
            queue()

        if player1_3_int.get() == 8:
            player1_3_int.set(0)
            player1_4_int.set(player1_4_int.get() + 1)
            player1_5_int.set(player1_5_int.get() + 1)
            player1_6_int.set(player1_6_int.get() + 1)
            player1_7_int.set(player1_7_int.get() + 1)
            player2_6_int.set(player2_6_int.get() + 1)
            player2_5_int.set(player2_5_int.get() + 1)
            player2_4_int.set(player2_4_int.get() + 1)
            player2_3_int.set(player2_3_int.get() + 1)
            if player2_3_int.get() % 2 == 0:
                player1_7_int.set(player1_7_int.get() + player2_3_int.get())
                player2_3_int.set(0)
            queue()

        if player1_3_int.get() == 9:
            player1_3_int.set(0)
            player1_4_int.set(player1_4_int.get() + 1)
            player1_5_int.set(player1_5_int.get() + 1)
            player1_6_int.set(player1_6_int.get() + 1)
            player1_7_int.set(player1_7_int.get() + 1)
            player2_6_int.set(player2_6_int.get() + 1)
            player2_5_int.set(player2_5_int.get() + 1)
            player2_4_int.set(player2_4_int.get() + 1)
            player2_3_int.set(player2_3_int.get() + 1)
            player2_2_int.set(player2_2_int.get() + 1)
            if player2_2_int.get() % 2 == 0:
                player1_7_int.set(player1_7_int.get() + player2_2_int.get())
                player2_2_int.set(0)
            queue()

        if player1_3_int.get() == 10:
            player1_3_int.set(0)
            player1_4_int.set(player1_4_int.get() + 1)
            player1_5_int.set(player1_5_int.get() + 1)
            player1_6_int.set(player1_6_int.get() + 1)
            player1_7_int.set(player1_7_int.get() + 1)
            player2_6_int.set(player2_6_int.get() + 1)
            player2_5_int.set(player2_5_int.get() + 1)
            player2_4_int.set(player2_4_int.get() + 1)
            player2_3_int.set(player2_3_int.get() + 1)
            player2_2_int.set(player2_2_int.get() + 1)
            player2_1_int.set(player2_1_int.get() + 1)
            if player2_1_int.get() % 2 == 0:
                player1_7_int.set(player1_7_int.get() + player2_1_int.get())
                player2_1_int.set(0)
            queue()


def spereader4():
    zero()
    while player1_4_int.get() != 0 and turn % 2 == 0:
        if player1_4_int.get() == 1:
            player1_4_int.set(0)
            player1_5_int.set(player1_5_int.get() + 1)
            if player1_5_int.get() == 1 and player2_5_int.get() != 0:
                player1_7_int.set(player1_7_int.get() + player1_5_int.get() + player2_5_int.get())
                player2_5_int.set(0)
                player1_5_int.set(0)
            queue()
        if player1_4_int.get() == 2:
            player1_4_int.set(0)
            player1_5_int.set(player1_5_int.get() + 1)
            player1_6_int.set(player1_6_int.get() + 1)
            if player1_6_int.get() == 1 and player2_5_int.get() != 0:
                player1_7_int.set(player1_7_int.get() + player1_6_int.get() + player2_6_int.get())
                player2_6_int.set(0)
                player1_6_int.set(0)
            queue()

        if player1_4_int.get() == 3:
            player1_4_int.set(0)
            player1_5_int.set(player1_5_int.get() + 1)
            player1_6_int.set(player1_6_int.get() + 1)
            player1_7_int.set(player1_7_int.get() + 1)

        if player1_4_int.get() == 4:
            player1_4_int.set(0)
            player1_5_int.set(player1_5_int.get() + 1)
            player1_6_int.set(player1_6_int.get() + 1)
            player1_7_int.set(player1_7_int.get() + 1)
            player2_6_int.set(player2_6_int.get() + 1)
            if player2_6_int.get() % 2 == 0:
                player1_7_int.set(player1_7_int.get() + player2_6_int.get())
                player2_6_int.set(0)
            queue()

        if player1_4_int.get() == 5:
            player1_4_int.set(0)
            player1_5_int.set(player1_5_int.get() + 1)
            player1_6_int.set(player1_6_int.get() + 1)
            player1_7_int.set(player1_7_int.get() + 1)
            player2_6_int.set(player2_6_int.get() + 1)
            player2_5_int.set(player2_5_int.get() + 1)
            if player2_5_int.get() % 2 == 0:
                player1_7_int.set(player1_7_int.get() + player2_5_int.get())
                player2_5_int.set(0)
            queue()

        if player1_4_int.get() == 6:
            player1_4_int.set(0)
            player1_5_int.set(player1_5_int.get() + 1)
            player1_6_int.set(player1_6_int.get() + 1)
            player1_7_int.set(player1_7_int.get() + 1)
            player2_6_int.set(player2_6_int.get() + 1)
            player2_5_int.set(player2_5_int.get() + 1)
            player2_4_int.set(player2_4_int.get() + 1)
            if player2_4_int.get() % 2 == 0:
                player1_7_int.set(player1_7_int.get() + player2_4_int.get())
                player2_4_int.set(0)
            queue()

        if player1_4_int.get() == 7:
            player1_4_int.set(0)
            player1_5_int.set(player1_5_int.get() + 1)
            player1_6_int.set(player1_6_int.get() + 1)
            player1_7_int.set(player1_7_int.get() + 1)
            player2_6_int.set(player2_6_int.get() + 1)
            player2_5_int.set(player2_5_int.get() + 1)
            player2_4_int.set(player2_4_int.get() + 1)
            player2_3_int.set(player2_3_int.get() + 1)
            if player2_3_int.get() % 2 == 0:
                player1_7_int.set(player1_7_int.get() + player2_3_int.get())
                player2_3_int.set(0)
            queue()

        if player1_4_int.get() == 8:
            player1_4_int.set(0)
            player1_5_int.set(player1_5_int.get() + 1)
            player1_6_int.set(player1_6_int.get() + 1)
            player1_7_int.set(player1_7_int.get() + 1)
            player2_6_int.set(player2_6_int.get() + 1)
            player2_5_int.set(player2_5_int.get() + 1)
            player2_4_int.set(player2_4_int.get() + 1)
            player2_3_int.set(player2_3_int.get() + 1)
            player2_2_int.set(player2_2_int.get() + 1)
            if player2_2_int.get() % 2 == 0:
                player1_7_int.set(player1_7_int.get() + player2_2_int.get())
                player2_2_int.set(0)
            queue()

        if player1_4_int.get() == 9:
            player1_4_int.set(0)
            player1_5_int.set(player1_5_int.get() + 1)
            player1_6_int.set(player1_6_int.get() + 1)
            player1_7_int.set(player1_7_int.get() + 1)
            player2_6_int.set(player2_6_int.get() + 1)
            player2_5_int.set(player2_5_int.get() + 1)
            player2_4_int.set(player2_4_int.get() + 1)
            player2_3_int.set(player2_3_int.get() + 1)
            player2_2_int.set(player2_2_int.get() + 1)
            player2_1_int.set(player2_1_int.get() + 1)
            if player2_1_int.get() % 2 == 0:
                player1_7_int.set(player1_7_int.get() + player2_1_int.get())
                player2_1_int.set(0)
            queue()

        if player1_4_int.get() == 10:
            player1_4_int.set(0)
            player1_5_int.set(player1_5_int.get() + 1)
            player1_6_int.set(player1_6_int.get() + 1)
            player1_7_int.set(player1_7_int.get() + 1)
            player2_6_int.set(player2_6_int.get() + 1)
            player2_5_int.set(player2_5_int.get() + 1)
            player2_4_int.set(player2_4_int.get() + 1)
            player2_3_int.set(player2_3_int.get() + 1)
            player2_2_int.set(player2_2_int.get() + 1)
            player2_1_int.set(player2_1_int.get() + 1)
            player1_1_int.set(player1_1_int.get() + 1)
            if player1_1_int.get() == 1 and player2_1_int.get() != 0:
                player1_7_int.set(player1_7_int.get() + player1_1_int.get() + player2_1_int.get())
                player2_1_int.set(0)
                player1_1_int.set(0)
            queue()


def spereader5():
    zero()
    while player1_5_int.get() != 0 and turn % 2 == 0:
        if player1_5_int.get() == 1:
            player1_5_int.set(0)
            player1_6_int.set(player1_6_int.get() + 1)
            if player1_6_int.get() == 1 and player2_6_int.get() != 0:
                player1_7_int.set(player1_7_int.get() + player1_6_int.get() + player2_6_int.get())
                player2_6_int.set(0)
                player1_6_int.set(0)
            queue()

        if player1_5_int.get() == 2:
            player1_5_int.set(0)
            player1_6_int.set(player1_6_int.get() + 1)
            player1_7_int.set(player1_7_int.get() + 1)

        if player1_5_int.get() == 3:
            player1_5_int.set(0)
            player1_6_int.set(player1_6_int.get() + 1)
            player1_7_int.set(player1_7_int.get() + 1)
            player2_6_int.set(player2_6_int.get() + 1)
            if player2_6_int.get() % 2 == 0:
                player1_7_int.set(player1_7_int.get() + player2_6_int.get())
                player2_6_int.set(0)
            queue()

        if player1_5_int.get() == 4:
            player1_5_int.set(0)
            player1_6_int.set(player1_6_int.get() + 1)
            player1_7_int.set(player1_7_int.get() + 1)
            player2_6_int.set(player2_6_int.get() + 1)
            player2_5_int.set(player2_5_int.get() + 1)
            if player2_5_int.get() % 2 == 0:
                player1_7_int.set(player1_7_int.get() + player2_5_int.get())
                player2_5_int.set(0)
            queue()

        if player1_5_int.get() == 5:
            player1_5_int.set(0)
            player1_6_int.set(player1_6_int.get() + 1)
            player1_7_int.set(player1_7_int.get() + 1)
            player2_6_int.set(player2_6_int.get() + 1)
            player2_5_int.set(player2_5_int.get() + 1)
            player2_4_int.set(player2_4_int.get() + 1)
            if player2_4_int.get() % 2 == 0:
                player1_7_int.set(player1_7_int.get() + player2_4_int.get())
                player2_4_int.set(0)
            queue()

        if player1_5_int.get() == 6:
            player1_5_int.set(0)
            player1_6_int.set(player1_6_int.get() + 1)
            player1_7_int.set(player1_7_int.get() + 1)
            player2_6_int.set(player2_6_int.get() + 1)
            player2_5_int.set(player2_5_int.get() + 1)
            player2_4_int.set(player2_4_int.get() + 1)
            player2_3_int.set(player2_3_int.get() + 1)
            if player2_3_int.get() % 2 == 0:
                player1_7_int.set(player1_7_int.get() + player2_3_int.get())
                player2_3_int.set(0)
            queue()

        if player1_5_int.get() == 7:
            player1_5_int.set(0)
            player1_6_int.set(player1_6_int.get() + 1)
            player1_7_int.set(player1_7_int.get() + 1)
            player2_6_int.set(player2_6_int.get() + 1)
            player2_5_int.set(player2_5_int.get() + 1)
            player2_4_int.set(player2_4_int.get() + 1)
            player2_3_int.set(player2_3_int.get() + 1)
            player2_2_int.set(player2_2_int.get() + 1)
            if player2_2_int.get() % 2 == 0:
                player1_7_int.set(player1_7_int.get() + player2_2_int.get())
                player2_2_int.set(0)
            queue()

        if player1_5_int.get() == 8:
            player1_5_int.set(0)
            player1_6_int.set(player1_6_int.get() + 1)
            player1_7_int.set(player1_7_int.get() + 1)
            player2_6_int.set(player2_6_int.get() + 1)
            player2_5_int.set(player2_5_int.get() + 1)
            player2_4_int.set(player2_4_int.get() + 1)
            player2_3_int.set(player2_3_int.get() + 1)
            player2_2_int.set(player2_2_int.get() + 1)
            player2_1_int.set(player2_1_int.get() + 1)
            if player2_1_int.get() % 2 == 0:
                player1_7_int.set(player1_7_int.get() + player2_1_int.get())
                player2_1_int.set(0)
            queue()

        if player1_5_int.get() == 9:
            player1_5_int.set(0)
            player1_6_int.set(player1_6_int.get() + 1)
            player1_7_int.set(player1_7_int.get() + 1)
            player2_6_int.set(player2_6_int.get() + 1)
            player2_5_int.set(player2_5_int.get() + 1)
            player2_4_int.set(player2_4_int.get() + 1)
            player2_3_int.set(player2_3_int.get() + 1)
            player2_2_int.set(player2_2_int.get() + 1)
            player2_1_int.set(player2_1_int.get() + 1)
            player1_1_int.set(player1_1_int.get() + 1)
            if player1_1_int.get() == 1 and player2_1_int.get() != 0:
                player1_7_int.set(player1_7_int.get() + player1_1_int.get() + player2_1_int.get())
                player2_1_int.set(0)
                player1_1_int.set(0)
            queue()

        if player1_5_int.get() == 10:
            player1_5_int.set(0)
            player1_6_int.set(player1_6_int.get() + 1)
            player1_7_int.set(player1_7_int.get() + 1)
            player2_6_int.set(player2_6_int.get() + 1)
            player2_5_int.set(player2_5_int.get() + 1)
            player2_4_int.set(player2_4_int.get() + 1)
            player2_3_int.set(player2_3_int.get() + 1)
            player2_2_int.set(player2_2_int.get() + 1)
            player2_1_int.set(player2_1_int.get() + 1)
            player1_1_int.set(player1_1_int.get() + 1)
            player1_2_int.set(player1_2_int.get() + 1)
            if player1_2_int.get() == 1 and player2_2_int.get() != 0:
                player1_7_int.set(player1_7_int.get() + player1_2_int.get() + player2_2_int.get())
                player2_2_int.set(0)
                player1_2_int.set(0)
            queue()


def spereader6():
    zero()
    while player1_6_int.get() != 0 and turn % 2 == 0:
        if player1_6_int.get() == 1:
            player1_6_int.set(0)
            player1_7_int.set(player1_7_int.get() + 1)

        if player1_6_int.get() == 2:
            player1_6_int.set(0)
            player1_7_int.set(player1_7_int.get() + 1)
            player2_6_int.set(player2_6_int.get() + 1)
            if player2_6_int.get() % 2 == 0:
                player1_7_int.set(player1_7_int.get() + player2_6_int.get())
                player2_6_int.set(0)
            queue()

        if player1_6_int.get() == 3:
            player1_6_int.set(0)
            player1_7_int.set(player1_7_int.get() + 1)
            player2_6_int.set(player2_6_int.get() + 1)
            player2_5_int.set(player2_5_int.get() + 1)
            if player2_5_int.get() % 2 == 0:
                player1_7_int.set(player1_7_int.get() + player2_5_int.get())
                player2_5_int.set(0)
            queue()

        if player1_6_int.get() == 4:
            player1_6_int.set(0)
            player1_7_int.set(player1_7_int.get() + 1)
            player2_6_int.set(player2_6_int.get() + 1)
            player2_5_int.set(player2_5_int.get() + 1)
            player2_4_int.set(player2_4_int.get() + 1)
            if player2_4_int.get() % 2 == 0:
                player1_7_int.set(player1_7_int.get() + player2_4_int.get())
                player2_4_int.set(0)
            queue()

        if player1_6_int.get() == 5:
            player1_6_int.set(0)
            player1_7_int.set(player1_7_int.get() + 1)
            player2_6_int.set(player2_6_int.get() + 1)
            player2_5_int.set(player2_5_int.get() + 1)
            player2_4_int.set(player2_4_int.get() + 1)
            player2_3_int.set(player2_3_int.get() + 1)
            if player2_3_int.get() % 2 == 0:
                player1_7_int.set(player1_7_int.get() + player2_3_int.get())
                player2_3_int.set(0)
            queue()

        if player1_6_int.get() == 6:
            player1_6_int.set(0)
            player1_7_int.set(player1_7_int.get() + 1)
            player2_6_int.set(player2_6_int.get() + 1)
            player2_5_int.set(player2_5_int.get() + 1)
            player2_4_int.set(player2_4_int.get() + 1)
            player2_3_int.set(player2_3_int.get() + 1)
            player2_2_int.set(player2_2_int.get() + 1)
            if player2_2_int.get() % 2 == 0:
                player1_7_int.set(player1_7_int.get() + player2_2_int.get())
                player2_2_int.set(0)
            queue()

        if player1_6_int.get() == 7:
            player1_6_int.set(0)
            player1_7_int.set(player1_7_int.get() + 1)
            player2_6_int.set(player2_6_int.get() + 1)
            player2_5_int.set(player2_5_int.get() + 1)
            player2_4_int.set(player2_4_int.get() + 1)
            player2_3_int.set(player2_3_int.get() + 1)
            player2_2_int.set(player2_2_int.get() + 1)
            player2_1_int.set(player2_1_int.get() + 1)
            if player2_1_int.get() % 2 == 0:
                player1_7_int.set(player1_7_int.get() + player2_1_int.get())
                player2_1_int.set(0)
            queue()

        if player1_6_int.get() == 8:
            player1_6_int.set(0)
            player1_7_int.set(player1_7_int.get() + 1)
            player2_6_int.set(player2_6_int.get() + 1)
            player2_5_int.set(player2_5_int.get() + 1)
            player2_4_int.set(player2_4_int.get() + 1)
            player2_3_int.set(player2_3_int.get() + 1)
            player2_2_int.set(player2_2_int.get() + 1)
            player2_1_int.set(player2_1_int.get() + 1)
            player1_1_int.set(player1_1_int.get() + 1)
            if player1_1_int.get() == 1 and player2_1_int.get() != 0:
                player1_7_int.set(player1_7_int.get() + player1_1_int.get() + player2_1_int.get())
                player2_1_int.set(0)
                player1_1_int.set(0)
            queue()

        if player1_6_int.get() == 9:
            player1_6_int.set(0)
            player1_7_int.set(player1_7_int.get() + 1)
            player2_6_int.set(player2_6_int.get() + 1)
            player2_5_int.set(player2_5_int.get() + 1)
            player2_4_int.set(player2_4_int.get() + 1)
            player2_3_int.set(player2_3_int.get() + 1)
            player2_2_int.set(player2_2_int.get() + 1)
            player2_1_int.set(player2_1_int.get() + 1)
            player1_1_int.set(player1_1_int.get() + 1)
            player1_2_int.set(player1_2_int.get() + 1)
            if player1_2_int.get() == 1 and player2_2_int.get() != 0:
                player1_7_int.set(player1_7_int.get() + player1_2_int.get() + player2_2_int.get())
                player2_2_int.set(0)
                player1_2_int.set(0)
            queue()

        if player1_6_int.get() == 10:
            player1_6_int.set(0)
            player1_7_int.set(player1_7_int.get() + 1)
            player2_6_int.set(player2_6_int.get() + 1)
            player2_5_int.set(player2_5_int.get() + 1)
            player2_4_int.set(player2_4_int.get() + 1)
            player2_3_int.set(player2_3_int.get() + 1)
            player2_2_int.set(player2_2_int.get() + 1)
            player2_1_int.set(player2_1_int.get() + 1)
            player1_1_int.set(player1_1_int.get() + 1)
            player1_2_int.set(player1_2_int.get() + 1)
            player1_3_int.set(player1_3_int.get() + 1)
            if player1_3_int.get() == 1 and player2_3_int.get() != 0:
                player1_7_int.set(player1_7_int.get() + player1_3_int.get() + player2_3_int.get())
                player2_3_int.set(0)
                player1_3_int.set(0)
            queue()


def spereader2_1():
    zero()
    while player2_1_int.get() != 0 and turn % 2 == 1 and turn != -1:
        if player2_1_int.get() == 1:
            player2_1_int.set(0)
            player2_0_int.set(player2_0_int.get() + 1)

        if player2_1_int.get() == 2:
            player2_1_int.set(0)
            player2_0_int.set(player2_0_int.get() + 1)
            player1_1_int.set(player1_1_int.get() + 1)
            if player1_1_int.get() % 2 == 0:
                player2_0_int.set(player2_0_int.get() + player1_1_int.get())
                player1_1_int.set(0)
            queue()

        if player2_1_int.get() == 3:
            player2_1_int.set(0)
            player2_0_int.set(player2_0_int.get() + 1)
            player1_1_int.set(player1_1_int.get() + 1)
            player1_2_int.set(player1_2_int.get() + 1)
            if player1_2_int.get() % 2 == 0:
                player2_0_int.set(player2_0_int.get() + player1_2_int.get())
                player1_2_int.set(0)
            queue()

        if player2_1_int.get() == 4:
            player2_1_int.set(0)
            player2_0_int.set(player2_0_int.get() + 1)
            player1_1_int.set(player1_1_int.get() + 1)
            player1_2_int.set(player1_2_int.get() + 1)
            player1_3_int.set(player1_3_int.get() + 1)
            if player1_3_int.get() % 2 == 0:
                player2_0_int.set(player2_0_int.get() + player1_3_int.get())
                player1_3_int.set(0)
            queue()

        if player2_1_int.get() == 5:
            player2_1_int.set(0)
            player2_0_int.set(player2_0_int.get() + 1)
            player1_1_int.set(player1_1_int.get() + 1)
            player1_2_int.set(player1_2_int.get() + 1)
            player1_3_int.set(player1_3_int.get() + 1)
            player1_4_int.set(player1_4_int.get() + 1)
            if player1_4_int.get() % 2 == 0:
                player2_0_int.set(player2_0_int.get() + player1_4_int.get())
                player1_4_int.set(0)
            queue()

        if player2_1_int.get() == 6:
            player2_1_int.set(0)
            player2_0_int.set(player2_0_int.get() + 1)
            player1_1_int.set(player1_1_int.get() + 1)
            player1_2_int.set(player1_2_int.get() + 1)
            player1_3_int.set(player1_3_int.get() + 1)
            player1_4_int.set(player1_4_int.get() + 1)
            player1_5_int.set(player1_5_int.get() + 1)
            if player1_5_int.get() % 2 == 0:
                player2_0_int.set(player2_0_int.get() + player1_5_int.get())
                player1_5_int.set(0)
            queue()

        if player2_1_int.get() == 7:
            player2_1_int.set(0)
            player2_0_int.set(player2_0_int.get() + 1)
            player1_1_int.set(player1_1_int.get() + 1)
            player1_2_int.set(player1_2_int.get() + 1)
            player1_3_int.set(player1_3_int.get() + 1)
            player1_4_int.set(player1_4_int.get() + 1)
            player1_5_int.set(player1_5_int.get() + 1)
            player1_6_int.set(player1_6_int.get() + 1)
            if player1_6_int.get() % 2 == 0:
                player2_0_int.set(player2_0_int.get() + player1_6_int.get())
                player1_6_int.set(0)
            queue()

        if player2_1_int.get() == 8:
            player2_1_int.set(0)
            player2_0_int.set(player2_0_int.get() + 1)
            player1_1_int.set(player1_1_int.get() + 1)
            player1_2_int.set(player1_2_int.get() + 1)
            player1_3_int.set(player1_3_int.get() + 1)
            player1_4_int.set(player1_4_int.get() + 1)
            player1_5_int.set(player1_5_int.get() + 1)
            player1_6_int.set(player1_6_int.get() + 1)
            player2_6_int.set(player2_6_int.get() + 1)
            if player2_6_int.get() == 1 and player1_6_int != 0:
                player2_0_int.set(player2_0_int.get() + player2_6_int.get() + player1_6_int.get())
                player2_6_int.set(0)
                player1_6_int.set(0)
            queue()

        if player2_1_int.get() == 9:
            player2_1_int.set(0)
            player2_0_int.set(player2_0_int.get() + 1)
            player1_1_int.set(player1_1_int.get() + 1)
            player1_2_int.set(player1_2_int.get() + 1)
            player1_3_int.set(player1_3_int.get() + 1)
            player1_4_int.set(player1_4_int.get() + 1)
            player1_5_int.set(player1_5_int.get() + 1)
            player1_6_int.set(player1_6_int.get() + 1)
            player2_6_int.set(player2_6_int.get() + 1)
            player2_5_int.set(player2_5_int.get() + 1)
            if player2_5_int.get() == 1 and player1_5_int != 0:
                player2_0_int.set(player2_0_int.get() + player2_5_int.get() + player1_5_int.get())
                player2_5_int.set(0)
                player1_5_int.set(0)
            queue()

        if player2_1_int.get() == 10:
            player2_1_int.set(0)
            player2_0_int.set(player2_0_int.get() + 1)
            player1_1_int.set(player1_1_int.get() + 1)
            player1_2_int.set(player1_2_int.get() + 1)
            player1_3_int.set(player1_3_int.get() + 1)
            player1_4_int.set(player1_4_int.get() + 1)
            player1_5_int.set(player1_5_int.get() + 1)
            player1_6_int.set(player1_6_int.get() + 1)
            player2_6_int.set(player2_6_int.get() + 1)
            player2_5_int.set(player2_5_int.get() + 1)
            player2_4_int.set(player2_4_int.get() + 1)
            if player2_4_int.get() == 1 and player1_4_int != 0:
                player2_0_int.set(player2_0_int.get() + player2_4_int.get() + player1_4_int.get())
                player2_4_int.set(0)
                player1_4_int.set(0)
            queue()


def spereader2_2():
    zero()
    while player2_2_int.get() != 0 and turn % 2 == 1 and turn != -1:
        if player2_2_int.get() == 1:
            player2_2_int.set(0)
            player2_1_int.set(player2_1_int.get() + 1)
            if player2_1_int.get() == 1 and player1_1_int != 0:
                player2_0_int.set(player2_0_int.get() + player2_1_int.get() + player1_1_int.get())
                player2_1_int.set(0)
                player1_1_int.set(0)
            queue()

        if player2_2_int.get() == 2:
            player2_2_int.set(0)
            player2_1_int.set(player2_1_int.get() + 1)
            player2_0_int.set(player2_0_int.get() + 1)

        if player2_2_int.get() == 3:
            player2_2_int.set(0)
            player2_1_int.set(player2_1_int.get() + 1)
            player2_0_int.set(player2_0_int.get() + 1)
            player1_1_int.set(player1_1_int.get() + 1)
            if player1_1_int.get() % 2 == 0:
                player2_0_int.set(player2_0_int.get() + player1_1_int.get())
                player1_1_int.set(0)
            queue()

        if player2_2_int.get() == 4:
            player2_2_int.set(0)
            player2_1_int.set(player2_1_int.get() + 1)
            player2_0_int.set(player2_0_int.get() + 1)
            player1_1_int.set(player1_1_int.get() + 1)
            player1_2_int.set(player1_2_int.get() + 1)
            if player1_2_int.get() % 2 == 0:
                player2_0_int.set(player2_0_int.get() + player1_2_int.get())
                player1_2_int.set(0)
            queue()

        if player2_2_int.get() == 5:
            player2_2_int.set(0)
            player2_1_int.set(player2_1_int.get() + 1)
            player2_0_int.set(player2_0_int.get() + 1)
            player1_1_int.set(player1_1_int.get() + 1)
            player1_2_int.set(player1_2_int.get() + 1)
            player1_3_int.set(player1_3_int.get() + 1)
            if player1_3_int.get() % 2 == 0:
                player2_0_int.set(player2_0_int.get() + player1_3_int.get())
                player1_3_int.set(0)
            queue()

        if player2_2_int.get() == 6:
            player2_2_int.set(0)
            player2_1_int.set(player2_1_int.get() + 1)
            player2_0_int.set(player2_0_int.get() + 1)
            player1_1_int.set(player1_1_int.get() + 1)
            player1_2_int.set(player1_2_int.get() + 1)
            player1_3_int.set(player1_3_int.get() + 1)
            player1_4_int.set(player1_4_int.get() + 1)
            if player1_4_int.get() % 2 == 0:
                player2_0_int.set(player2_0_int.get() + player1_4_int.get())
                player1_4_int.set(0)
            queue()

        if player2_2_int.get() == 7:
            player2_2_int.set(0)
            player2_1_int.set(player2_1_int.get() + 1)
            player2_0_int.set(player2_0_int.get() + 1)
            player1_1_int.set(player1_1_int.get() + 1)
            player1_2_int.set(player1_2_int.get() + 1)
            player1_3_int.set(player1_3_int.get() + 1)
            player1_4_int.set(player1_4_int.get() + 1)
            player1_5_int.set(player1_5_int.get() + 1)
            if player1_5_int.get() % 2 == 0:
                player2_0_int.set(player2_0_int.get() + player1_5_int.get())
                player1_5_int.set(0)
            queue()

        if player2_2_int.get() == 8:
            player2_2_int.set(0)
            player2_1_int.set(player2_1_int.get() + 1)
            player2_0_int.set(player2_0_int.get() + 1)
            player1_1_int.set(player1_1_int.get() + 1)
            player1_2_int.set(player1_2_int.get() + 1)
            player1_3_int.set(player1_3_int.get() + 1)
            player1_4_int.set(player1_4_int.get() + 1)
            player1_5_int.set(player1_5_int.get() + 1)
            player1_6_int.set(player1_6_int.get() + 1)
            if player1_6_int.get() % 2 == 0:
                player2_0_int.set(player2_0_int.get() + player1_6_int.get())
                player1_6_int.set(0)
            queue()

        if player2_2_int.get() == 9:
            player2_2_int.set(0)
            player2_1_int.set(player2_1_int.get() + 1)
            player2_0_int.set(player2_0_int.get() + 1)
            player1_1_int.set(player1_1_int.get() + 1)
            player1_2_int.set(player1_2_int.get() + 1)
            player1_3_int.set(player1_3_int.get() + 1)
            player1_4_int.set(player1_4_int.get() + 1)
            player1_5_int.set(player1_5_int.get() + 1)
            player1_6_int.set(player1_6_int.get() + 1)
            player2_6_int.set(player2_6_int.get() + 1)
            if player2_6_int.get() == 1 and player1_6_int != 0:
                player2_0_int.set(player2_0_int.get() + player2_6_int.get() + player1_6_int.get())
                player2_6_int.set(0)
                player1_6_int.set(0)
            queue()

        if player2_2_int.get() == 10:
            player2_2_int.set(0)
            player2_1_int.set(player2_1_int.get() + 1)
            player2_0_int.set(player2_0_int.get() + 1)
            player1_1_int.set(player1_1_int.get() + 1)
            player1_2_int.set(player1_2_int.get() + 1)
            player1_3_int.set(player1_3_int.get() + 1)
            player1_4_int.set(player1_4_int.get() + 1)
            player1_5_int.set(player1_5_int.get() + 1)
            player1_6_int.set(player1_6_int.get() + 1)
            player2_6_int.set(player2_6_int.get() + 1)
            player2_5_int.set(player2_5_int.get() + 1)
            if player2_5_int.get() == 1 and player1_5_int.get() != 0:
                player2_0_int.set(player2_0_int.get() + player2_5_int.get() + player1_5_int.get())
                player2_5_int.set(0)
                player1_5_int.set(0)
            queue()


def spereader2_3():
    zero()
    while player2_3_int.get() != 0 and turn % 2 == 1 and turn != -1:
        if player2_3_int.get() == 1:
            player2_3_int.set(0)
            player2_2_int.set(player2_2_int.get() + 1)
            if player2_2_int.get() == 1 and player1_2_int.get() != 0:
                player2_0_int.set(player2_0_int.get() + player2_2_int.get() + player1_2_int.get())
                player2_2_int.set(0)
                player1_2_int.set(0)
            queue()

        if player2_3_int.get() == 2:
            player2_3_int.set(0)
            player2_2_int.set(player2_2_int.get() + 1)
            player2_1_int.set(player2_1_int.get() + 1)
            if player2_1_int.get() == 1 and player1_1_int.get() != 0:
                player2_0_int.set(player2_0_int.get() + player2_1_int.get() + player1_1_int.get())
                player2_1_int.set(0)
                player1_1_int.set(0)
            queue()

        if player2_3_int.get() == 3:
            player2_3_int.set(0)
            player2_2_int.set(player2_2_int.get() + 1)
            player2_1_int.set(player2_1_int.get() + 1)
            player2_0_int.set(player2_0_int.get() + 1)

        if player2_3_int.get() == 4:
            player2_3_int.set(0)
            player2_2_int.set(player2_2_int.get() + 1)
            player2_1_int.set(player2_1_int.get() + 1)
            player2_0_int.set(player2_0_int.get() + 1)
            player1_1_int.set(player1_1_int.get() + 1)
            if player1_1_int.get() % 2 == 0:
                player2_0_int.set(player2_0_int.get() + player1_1_int.get())
                player1_1_int.set(0)
            queue()

        if player2_3_int.get() == 5:
            player2_3_int.set(0)
            player2_2_int.set(player2_2_int.get() + 1)
            player2_1_int.set(player2_1_int.get() + 1)
            player2_0_int.set(player2_0_int.get() + 1)
            player1_1_int.set(player1_1_int.get() + 1)
            player1_2_int.set(player1_2_int.get() + 1)
            if player1_2_int.get() % 2 == 0:
                player2_0_int.set(player2_0_int.get() + player1_2_int.get())
                player1_2_int.set(0)
            queue()

        if player2_3_int.get() == 6:
            player2_3_int.set(0)
            player2_2_int.set(player2_2_int.get() + 1)
            player2_1_int.set(player2_1_int.get() + 1)
            player2_0_int.set(player2_0_int.get() + 1)
            player1_1_int.set(player1_1_int.get() + 1)
            player1_2_int.set(player1_2_int.get() + 1)
            player1_3_int.set(player1_3_int.get() + 1)
            if player1_3_int.get() % 2 == 0:
                player2_0_int.set(player2_0_int.get() + player1_3_int.get())
                player1_3_int.set(0)
            queue()

        if player2_3_int.get() == 7:
            player2_3_int.set(0)
            player2_2_int.set(player2_2_int.get() + 1)
            player2_1_int.set(player2_1_int.get() + 1)
            player2_0_int.set(player2_0_int.get() + 1)
            player1_1_int.set(player1_1_int.get() + 1)
            player1_2_int.set(player1_2_int.get() + 1)
            player1_3_int.set(player1_3_int.get() + 1)
            player1_4_int.set(player1_4_int.get() + 1)
            if player1_4_int.get() % 2 == 0:
                player2_0_int.set(player2_0_int.get() + player1_4_int.get())
                player1_4_int.set(0)
            queue()

        if player2_3_int.get() == 8:
            player2_3_int.set(0)
            player2_2_int.set(player2_2_int.get() + 1)
            player2_1_int.set(player2_1_int.get() + 1)
            player2_0_int.set(player2_0_int.get() + 1)
            player1_1_int.set(player1_1_int.get() + 1)
            player1_2_int.set(player1_2_int.get() + 1)
            player1_3_int.set(player1_3_int.get() + 1)
            player1_4_int.set(player1_4_int.get() + 1)
            player1_5_int.set(player1_5_int.get() + 1)
            if player1_5_int.get() % 2 == 0:
                player2_0_int.set(player2_0_int.get() + player1_5_int.get())
                player1_5_int.set(0)
            queue()

        if player2_3_int.get() == 9:
            player2_3_int.set(0)
            player2_2_int.set(player2_2_int.get() + 1)
            player2_1_int.set(player2_1_int.get() + 1)
            player2_0_int.set(player2_0_int.get() + 1)
            player1_1_int.set(player1_1_int.get() + 1)
            player1_2_int.set(player1_2_int.get() + 1)
            player1_3_int.set(player1_3_int.get() + 1)
            player1_4_int.set(player1_4_int.get() + 1)
            player1_5_int.set(player1_5_int.get() + 1)
            player1_6_int.set(player1_6_int.get() + 1)
            if player1_6_int.get() % 2 == 0:
                player2_0_int.set(player2_0_int.get() + player1_6_int.get())
                player1_6_int.set(0)
            queue()

        if player2_3_int.get() == 10:
            player2_3_int.set(0)
            player2_2_int.set(player2_2_int.get() + 1)
            player2_1_int.set(player2_1_int.get() + 1)
            player2_0_int.set(player2_0_int.get() + 1)
            player1_1_int.set(player1_1_int.get() + 1)
            player1_2_int.set(player1_2_int.get() + 1)
            player1_3_int.set(player1_3_int.get() + 1)
            player1_4_int.set(player1_4_int.get() + 1)
            player1_5_int.set(player1_5_int.get() + 1)
            player1_6_int.set(player1_6_int.get() + 1)
            player2_6_int.set(player2_6_int.get() + 1)
            if player2_6_int.get() == 1 and player1_6_int != 0:
                player2_0_int.set(player2_0_int.get() + player2_6_int.get() + player1_6_int.get())
                player2_6_int.set(0)
                player1_6_int.set(0)
            queue()


def spereader2_4():
    zero()
    while player2_4_int.get() != 0 and turn % 2 == 1 and turn != -1:
        if player2_4_int.get() == 1:
            player2_4_int.set(0)
            player2_3_int.set(player2_3_int.get() + 1)
            if player2_3_int.get() == 1 and player1_3_int.get() != 0:
                player2_0_int.set(player2_0_int.get() + player2_3_int.get() + player1_3_int.get())
                player2_3_int.set(0)
                player1_3_int.set(0)
            queue()

        if player2_4_int.get() == 2:
            player2_4_int.set(0)
            player2_3_int.set(player2_3_int.get() + 1)
            player2_2_int.set(player2_2_int.get() + 1)
            if player2_2_int.get() == 1 and player1_2_int.get() != 0:
                player2_0_int.set(player2_0_int.get() + player2_2_int.get() + player1_2_int.get())
                player2_2_int.set(0)
                player1_2_int.set(0)
            queue()

        if player2_4_int.get() == 3:
            player2_4_int.set(0)
            player2_3_int.set(player2_3_int.get() + 1)
            player2_2_int.set(player2_2_int.get() + 1)
            player2_1_int.set(player2_1_int.get() + 1)
            if player2_1_int.get() == 1 and player1_1_int.get() != 0:
                player2_0_int.set(player2_0_int.get() + player2_1_int.get() + player1_1_int.get())
                player2_1_int.set(0)
                player1_1_int.set(0)
            queue()

        if player2_4_int.get() == 4:
            player2_4_int.set(0)
            player2_3_int.set(player2_3_int.get() + 1)
            player2_2_int.set(player2_2_int.get() + 1)
            player2_1_int.set(player2_1_int.get() + 1)
            player2_0_int.set(player2_0_int.get() + 1)

        if player2_4_int.get() == 5:
            player2_4_int.set(0)
            player2_3_int.set(player2_3_int.get() + 1)
            player2_2_int.set(player2_2_int.get() + 1)
            player2_1_int.set(player2_1_int.get() + 1)
            player2_0_int.set(player2_0_int.get() + 1)
            player1_1_int.set(player1_1_int.get() + 1)
            if player1_1_int.get() % 2 == 0:
                player2_0_int.set(player2_0_int.get() + player1_1_int.get())
                player1_1_int.set(0)
            queue()

        if player2_4_int.get() == 6:
            player2_4_int.set(0)
            player2_3_int.set(player2_3_int.get() + 1)
            player2_2_int.set(player2_2_int.get() + 1)
            player2_1_int.set(player2_1_int.get() + 1)
            player2_0_int.set(player2_0_int.get() + 1)
            player1_1_int.set(player1_1_int.get() + 1)
            player1_2_int.set(player1_2_int.get() + 1)
            if player1_2_int.get() % 2 == 0:
                player2_0_int.set(player2_0_int.get() + player1_2_int.get())
                player1_2_int.set(0)
            queue()

        if player2_4_int.get() == 7:
            player2_4_int.set(0)
            player2_3_int.set(player2_3_int.get() + 1)
            player2_2_int.set(player2_2_int.get() + 1)
            player2_1_int.set(player2_1_int.get() + 1)
            player2_0_int.set(player2_0_int.get() + 1)
            player1_1_int.set(player1_1_int.get() + 1)
            player1_2_int.set(player1_2_int.get() + 1)
            player1_3_int.set(player1_3_int.get() + 1)
            if player1_3_int.get() % 2 == 0:
                player2_0_int.set(player2_0_int.get() + player1_3_int.get())
                player1_3_int.set(0)
            queue()

        if player2_4_int.get() == 8:
            player2_4_int.set(0)
            player2_3_int.set(player2_3_int.get() + 1)
            player2_2_int.set(player2_2_int.get() + 1)
            player2_1_int.set(player2_1_int.get() + 1)
            player2_0_int.set(player2_0_int.get() + 1)
            player1_1_int.set(player1_1_int.get() + 1)
            player1_2_int.set(player1_2_int.get() + 1)
            player1_3_int.set(player1_3_int.get() + 1)
            player1_4_int.set(player1_4_int.get() + 1)
            if player1_4_int.get() % 2 == 0:
                player2_0_int.set(player2_0_int.get() + player1_4_int.get())
                player1_4_int.set(0)
            queue()

        if player2_4_int.get() == 9:
            player2_4_int.set(0)
            player2_3_int.set(player2_3_int.get() + 1)
            player2_2_int.set(player2_2_int.get() + 1)
            player2_1_int.set(player2_1_int.get() + 1)
            player2_0_int.set(player2_0_int.get() + 1)
            player1_1_int.set(player1_1_int.get() + 1)
            player1_2_int.set(player1_2_int.get() + 1)
            player1_3_int.set(player1_3_int.get() + 1)
            player1_4_int.set(player1_4_int.get() + 1)
            player1_5_int.set(player1_5_int.get() + 1)
            if player1_5_int.get() % 2 == 0:
                player2_0_int.set(player2_0_int.get() + player1_5_int.get())
                player1_5_int.set(0)
            queue()

        if player2_4_int.get() == 10:
            player2_4_int.set(0)
            player2_3_int.set(player2_3_int.get() + 1)
            player2_2_int.set(player2_2_int.get() + 1)
            player2_1_int.set(player2_1_int.get() + 1)
            player2_0_int.set(player2_0_int.get() + 1)
            player1_1_int.set(player1_1_int.get() + 1)
            player1_2_int.set(player1_2_int.get() + 1)
            player1_3_int.set(player1_3_int.get() + 1)
            player1_4_int.set(player1_4_int.get() + 1)
            player1_5_int.set(player1_5_int.get() + 1)
            player1_6_int.set(player1_6_int.get() + 1)
            if player1_6_int.get() % 2 == 0:
                player2_0_int.set(player2_0_int.get() + player1_6_int.get())
                player1_6_int.set(0)
            queue()


def spereader2_5():
    zero()
    while player2_5_int.get() != 0 and turn % 2 == 1 and turn != -1:
        if player2_5_int.get() == 1:
            player2_5_int.set(0)
            player2_4_int.set(player2_4_int.get() + 1)
            if player2_4_int.get() == 1 and player1_4_int.get() != 0:
                player2_0_int.set(player2_0_int.get() + player2_4_int.get() + player1_4_int.get())
                player2_4_int.set(0)
                player1_4_int.set(0)
            queue()

        if player2_5_int.get() == 2:
            player2_5_int.set(0)
            player2_4_int.set(player2_4_int.get() + 1)
            player2_3_int.set(player2_2_int.get() + 1)
            if player2_3_int.get() == 1 and player1_3_int != 0:
                player2_0_int.set(player2_0_int.get() + player2_3_int.get() + player1_3_int.get())
                player2_3_int.set(0)
                player1_3_int.set(0)
            queue()

        if player2_5_int.get() == 3:
            player2_5_int.set(0)
            player2_4_int.set(player2_4_int.get() + 1)
            player2_3_int.set(player2_2_int.get() + 1)
            player2_2_int.set(player2_2_int.get() + 1)
            if player2_2_int.get() == 1 and player1_2_int != 0:
                player2_0_int.set(player2_0_int.get() + player2_2_int.get() + player1_2_int.get())
                player2_2_int.set(0)
                player1_2_int.set(0)
            queue()

        if player2_5_int.get() == 4:
            player2_5_int.set(0)
            player2_4_int.set(player2_4_int.get() + 1)
            player2_3_int.set(player2_2_int.get() + 1)
            player2_2_int.set(player2_2_int.get() + 1)
            player2_1_int.set(player2_1_int.get() + 1)
            if player2_1_int.get() == 1 and player1_1_int.get() != 0:
                player2_0_int.set(player2_0_int.get() + player2_1_int.get() + player1_1_int.get())
                player2_1_int.set(0)
                player1_1_int.set(0)
            queue()

        if player2_5_int.get() == 5:
            player2_5_int.set(0)
            player2_4_int.set(player2_4_int.get() + 1)
            player2_3_int.set(player2_2_int.get() + 1)
            player2_2_int.set(player2_2_int.get() + 1)
            player2_1_int.set(player2_1_int.get() + 1)
            player2_0_int.set(player2_0_int.get() + 1)

        if player2_5_int.get() == 6:
            player2_5_int.set(0)
            player2_4_int.set(player2_4_int.get() + 1)
            player2_3_int.set(player2_2_int.get() + 1)
            player2_2_int.set(player2_2_int.get() + 1)
            player2_1_int.set(player2_1_int.get() + 1)
            player2_0_int.set(player2_0_int.get() + 1)
            player1_1_int.set(player1_1_int.get() + 1)
            if player1_1_int.get() % 2 == 0:
                player2_0_int.set(player2_0_int.get() + player1_1_int.get())
                player1_1_int.set(0)
            queue()

        if player2_5_int.get() == 7:
            player2_5_int.set(0)
            player2_4_int.set(player2_4_int.get() + 1)
            player2_3_int.set(player2_2_int.get() + 1)
            player2_2_int.set(player2_2_int.get() + 1)
            player2_1_int.set(player2_1_int.get() + 1)
            player2_0_int.set(player2_0_int.get() + 1)
            player1_1_int.set(player1_1_int.get() + 1)
            player1_2_int.set(player1_2_int.get() + 1)
            if player1_2_int.get() % 2 == 0:
                player2_0_int.set(player2_0_int.get() + player1_2_int.get())
                player1_2_int.set(0)
            queue()

        if player2_5_int.get() == 8:
            player2_5_int.set(0)
            player2_4_int.set(player2_4_int.get() + 1)
            player2_3_int.set(player2_2_int.get() + 1)
            player2_2_int.set(player2_2_int.get() + 1)
            player2_1_int.set(player2_1_int.get() + 1)
            player2_0_int.set(player2_0_int.get() + 1)
            player1_1_int.set(player1_1_int.get() + 1)
            player1_2_int.set(player1_2_int.get() + 1)
            player1_3_int.set(player1_3_int.get() + 1)
            if player1_3_int.get() % 2 == 0:
                player2_0_int.set(player2_0_int.get() + player1_3_int.get())
                player1_3_int.set(0)
            queue()

        if player2_5_int.get() == 9:
            player2_5_int.set(0)
            player2_4_int.set(player2_4_int.get() + 1)
            player2_3_int.set(player2_2_int.get() + 1)
            player2_2_int.set(player2_2_int.get() + 1)
            player2_1_int.set(player2_1_int.get() + 1)
            player2_0_int.set(player2_0_int.get() + 1)
            player1_1_int.set(player1_1_int.get() + 1)
            player1_2_int.set(player1_2_int.get() + 1)
            player1_3_int.set(player1_3_int.get() + 1)
            player1_4_int.set(player1_4_int.get() + 1)
            if player1_4_int.get() % 2 == 0:
                player2_0_int.set(player2_0_int.get() + player1_4_int.get())
                player1_4_int.set(0)
            queue()

        if player2_5_int.get() == 10:
            player2_5_int.set(0)
            player2_4_int.set(player2_4_int.get() + 1)
            player2_3_int.set(player2_2_int.get() + 1)
            player2_2_int.set(player2_2_int.get() + 1)
            player2_1_int.set(player2_1_int.get() + 1)
            player2_0_int.set(player2_0_int.get() + 1)
            player1_1_int.set(player1_1_int.get() + 1)
            player1_2_int.set(player1_2_int.get() + 1)
            player1_3_int.set(player1_3_int.get() + 1)
            player1_4_int.set(player1_4_int.get() + 1)
            player1_5_int.set(player1_5_int.get() + 1)
            if player1_5_int.get() % 2 == 0:
                player2_0_int.set(player2_0_int.get() + player1_5_int.get())
                player1_5_int.set(0)
            queue()


def spereader2_6():
    zero()
    while player2_6_int.get() != 0 and turn % 2 == 1 and turn != -1:
        if player2_6_int.get() == 1:
            player2_6_int.set(0)
            player2_5_int.set(player2_5_int.get() + 1)
            if player2_5_int.get() == 1 and player1_5_int != 0:
                player2_0_int.set(player2_0_int.get() + player2_5_int.get() + player1_5_int.get())
                player2_5_int.set(0)
                player1_5_int.set(0)
            queue()

        if player2_6_int.get() == 2:
            player2_6_int.set(0)
            player2_5_int.set(player2_5_int.get() + 1)
            player2_4_int.set(player2_4_int.get() + 1)
            if player2_4_int.get() == 1 and player1_4_int != 0:
                player2_0_int.set(player2_0_int.get() + player2_4_int.get() + player1_4_int.get())
                player2_4_int.set(0)
                player1_4_int.set(0)
            queue()

        if player2_6_int.get() == 3:
            player2_6_int.set(0)
            player2_5_int.set(player2_5_int.get() + 1)
            player2_4_int.set(player2_4_int.get() + 1)
            player2_3_int.set(player2_3_int.get() + 1)
            if player2_3_int.get() == 1 and player1_3_int != 0:
                player2_0_int.set(player2_0_int.get() + player2_3_int.get() + player1_3_int.get())
                player2_3_int.set(0)
                player1_3_int.set(0)
            queue()

        if player2_6_int.get() == 4:
            player2_6_int.set(0)
            player2_5_int.set(player2_5_int.get() + 1)
            player2_4_int.set(player2_4_int.get() + 1)
            player2_3_int.set(player2_3_int.get() + 1)
            player2_2_int.set(player2_2_int.get() + 1)
            if player2_2_int.get() == 1 and player1_2_int != 0:
                player2_0_int.set(player2_0_int.get() + player2_2_int.get() + player1_2_int.get())
                player2_2_int.set(0)
                player1_2_int.set(0)
            queue()

        if player2_6_int.get() == 5:
            player2_6_int.set(0)
            player2_5_int.set(player2_5_int.get() + 1)
            player2_4_int.set(player2_4_int.get() + 1)
            player2_3_int.set(player2_3_int.get() + 1)
            player2_2_int.set(player2_2_int.get() + 1)
            player2_1_int.set(player2_1_int.get() + 1)
            if player2_1_int.get() == 1 and player1_1_int != 0:
                player2_0_int.set(player2_0_int.get() + player2_1_int.get() + player1_1_int.get())
                player2_1_int.set(0)
                player1_1_int.set(0)
            queue()

        if player2_6_int.get() == 6:
            player2_6_int.set(0)
            player2_5_int.set(player2_5_int.get() + 1)
            player2_4_int.set(player2_4_int.get() + 1)
            player2_3_int.set(player2_3_int.get() + 1)
            player2_2_int.set(player2_2_int.get() + 1)
            player2_1_int.set(player2_1_int.get() + 1)
            player2_0_int.set(player2_0_int.get() + 1)

        if player2_6_int.get() == 7:
            player2_6_int.set(0)
            player2_5_int.set(player2_5_int.get() + 1)
            player2_4_int.set(player2_4_int.get() + 1)
            player2_3_int.set(player2_3_int.get() + 1)
            player2_2_int.set(player2_2_int.get() + 1)
            player2_1_int.set(player2_1_int.get() + 1)
            player2_0_int.set(player2_0_int.get() + 1)
            player1_1_int.set(player1_1_int.get() + 1)
            if player1_1_int.get() % 2 == 0:
                player2_0_int.set(player2_0_int.get() + player1_1_int.get())
                player1_1_int.set(0)
            queue()

        if player2_6_int.get() == 8:
            player2_6_int.set(0)
            player2_5_int.set(player2_5_int.get() + 1)
            player2_4_int.set(player2_4_int.get() + 1)
            player2_3_int.set(player2_3_int.get() + 1)
            player2_2_int.set(player2_2_int.get() + 1)
            player2_1_int.set(player2_1_int.get() + 1)
            player2_0_int.set(player2_0_int.get() + 1)
            player1_1_int.set(player1_1_int.get() + 1)
            player1_2_int.set(player1_2_int.get() + 1)
            if player1_2_int.get() % 2 == 0:
                player2_0_int.set(player2_0_int.get() + player1_2_int.get())
                player1_2_int.set(0)
            queue()

        if player2_6_int.get() == 9:
            player2_6_int.set(0)
            player2_5_int.set(player2_5_int.get() + 1)
            player2_4_int.set(player2_4_int.get() + 1)
            player2_3_int.set(player2_3_int.get() + 1)
            player2_2_int.set(player2_2_int.get() + 1)
            player2_1_int.set(player2_1_int.get() + 1)
            player2_0_int.set(player2_0_int.get() + 1)
            player1_1_int.set(player1_1_int.get() + 1)
            player1_2_int.set(player1_2_int.get() + 1)
            player1_3_int.set(player1_3_int.get() + 1)
            if player1_3_int.get() % 2 == 0:
                player2_0_int.set(player2_0_int.get() + player1_3_int.get())
                player1_3_int.set(0)
            queue()

        if player2_6_int.get() == 10:
            player2_6_int.set(0)
            player2_5_int.set(player2_5_int.get() + 1)
            player2_4_int.set(player2_4_int.get() + 1)
            player2_3_int.set(player2_3_int.get() + 1)
            player2_2_int.set(player2_2_int.get() + 1)
            player2_1_int.set(player2_1_int.get() + 1)
            player2_0_int.set(player2_0_int.get() + 1)
            player1_1_int.set(player1_1_int.get() + 1)
            player1_2_int.set(player1_2_int.get() + 1)
            player1_3_int.set(player1_3_int.get() + 1)
            player1_4_int.set(player1_4_int.get() + 1)
            if player1_4_int.get() % 2 == 0:
                player2_0_int.set(player2_0_int.get() + player1_4_int.get())
                player1_4_int.set(0)
            queue()


turn = 0

main_window = tkinter.Tk()
main_window.title('Mangala')
main_window.geometry('640x480')
main_window.configure(background='brown')

game_frame = tkinter.Frame(main_window, relief="sunken", borderwidth=1, background='brown')
game_frame.grid(row=0, column=0, sticky='news')

separator_frame = tkinter.Frame(game_frame, relief='raised', borderwidth=1, background='black')
separator_frame.grid(row=2, column=1, columnspan=6)

player1_1_int = tkinter.IntVar()
player1_1_int.set(4)
player1_1 = tkinter.Label(game_frame, textvariable=player1_1_int)
player1_1.grid(row=3, column=1)

player1_2_int = tkinter.IntVar()
player1_2_int.set(4)
player1_2 = tkinter.Label(game_frame, textvariable=player1_2_int)
player1_2.grid(row=3, column=2)

player1_3_int = tkinter.IntVar()
player1_3_int.set(4)
player1_3 = tkinter.Label(game_frame, textvariable=player1_3_int)
player1_3.grid(row=3, column=3)

player1_4_int = tkinter.IntVar()
player1_4_int.set(4)
player1_4 = tkinter.Label(game_frame, textvariable=player1_4_int)
player1_4.grid(row=3, column=4)

player1_5_int = tkinter.IntVar()
player1_5_int.set(4)
player1_5 = tkinter.Label(game_frame, textvariable=player1_5_int)
player1_5.grid(row=3, column=5)

player1_6_int = tkinter.IntVar()
player1_6_int.set(4)
player1_6 = tkinter.Label(game_frame, textvariable=player1_6_int)
player1_6.grid(row=3, column=6)

player1_7_int = tkinter.IntVar()
player1_7_int.set(0)
player1_7 = tkinter.Label(game_frame, textvariable=player1_7_int)
player1_7.grid(row=1, column=7, rowspan=3)

player2_0_int = tkinter.IntVar()
player2_0_int.set(0)
player2_0 = tkinter.Label(game_frame, textvariable=player2_0_int)
player2_0.grid(row=1, column=0, rowspan=3)

player2_1_int = tkinter.IntVar()
player2_1_int.set(4)
player2_1 = tkinter.Label(game_frame, textvariable=player2_1_int)
player2_1.grid(row=1, column=1)

player2_2_int = tkinter.IntVar()
player2_2_int.set(4)
player2_2 = tkinter.Label(game_frame, textvariable=player2_2_int)
player2_2.grid(row=1, column=2)

player2_3_int = tkinter.IntVar()
player2_3_int.set(4)
player2_3 = tkinter.Label(game_frame, textvariable=player2_3_int)
player2_3.grid(row=1, column=3)

player2_4_int = tkinter.IntVar()
player2_4_int.set(4)
player2_4 = tkinter.Label(game_frame, textvariable=player2_4_int)
player2_4.grid(row=1, column=4)

player2_5_int = tkinter.IntVar()
player2_5_int.set(4)
player2_5 = tkinter.Label(game_frame, textvariable=player2_5_int)
player2_5.grid(row=1, column=5)

player2_6_int = tkinter.IntVar()
player2_6_int.set(4)
player2_6 = tkinter.Label(game_frame, textvariable=player2_6_int)
player2_6.grid(row=1, column=6)

hazne_2_1_button = tkinter.Button(game_frame, text='Dağıt', command=spereader2_1)
hazne_2_1_button.grid(row=0, column=1)

hazne_2_2_button = tkinter.Button(game_frame, text='Dağıt', command=spereader2_2)
hazne_2_2_button.grid(row=0, column=2)

hazne_2_3_button = tkinter.Button(game_frame, text='Dağıt', command=spereader2_3)
hazne_2_3_button.grid(row=0, column=3)

hazne_2_4_button = tkinter.Button(game_frame, text='Dağıt', command=spereader2_4)
hazne_2_4_button.grid(row=0, column=4)

hazne_2_5_button = tkinter.Button(game_frame, text='Dağıt', command=spereader2_5)
hazne_2_5_button.grid(row=0, column=5)

hazne_2_6_button = tkinter.Button(game_frame, text='Dağıt', command=spereader2_6)
hazne_2_6_button.grid(row=0, column=6)

hazne_1_button = tkinter.Button(game_frame, text='Dağıt', command=spereader1)
hazne_1_button.grid(row=4, column=1)

hazne_2_button = tkinter.Button(game_frame, text='Dağıt', command=spereader2)
hazne_2_button.grid(row=4, column=2)

hazne_3_button = tkinter.Button(game_frame, text='Dağıt', command=spereader3)
hazne_3_button.grid(row=4, column=3)

hazne_4_button = tkinter.Button(game_frame, text='Dağıt', command=spereader4)
hazne_4_button.grid(row=4, column=4)

hazne_5_button = tkinter.Button(game_frame, text='Dağıt', command=spereader5)
hazne_5_button.grid(row=4, column=5)

hazne_6_button = tkinter.Button(game_frame, text='Dağıt', command=spereader6)
hazne_6_button.grid(row=4, column=6)

turn_and_winner_text = tkinter.StringVar()
turn_and_winner_text.set('1. Oyuncunun Sırası')
turn_and_winner_label = tkinter.Label(game_frame, textvariable=turn_and_winner_text)
turn_and_winner_label.grid(row=5, column=0, columnspan=7)

main_window.mainloop()
