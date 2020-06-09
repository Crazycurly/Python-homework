import random
from threading import Thread
from queue import Queue


def gen_card():
    card = []
    for suit in ['S', 'H', 'D', 'C']:
        for rank in range(1, 14):
            card.append(suit+str(rank))

    card.append('J1')
    card.append('J2')
    random.shuffle(card)

    return(card[:27], card[27:])


def print_card(human_card, pc_card):

    print('玩家的牌:', end=' ')
    for i in human_card:
        print(i, end=' ')

    print('\n電腦的牌:', end=' ')
    # for i in pc_card:
    #     print(i, end=' ')
    # print('\n')

    for i in range(len(pc_card)):
        print(i+1, end=' ')
    print('\n')


def pair(human_card, pc_card):
    q = Queue()
    t1 = Thread(target=pair_job, args=(human_card, q))
    t2 = Thread(target=pair_job, args=(pc_card, q))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    return(q.get(), q.get())


def pair_job(card, q):
    dropped_cards = []
    tmp = sorted(card, key=lambda card: card[1:])

    if 'J1' in tmp:
        tmp.remove('J1')
    if 'J2' in tmp:
        tmp.remove('J2')

    for i in range(len(tmp) - 1):
        if tmp[i] and tmp[i][1:] == tmp[i + 1][1:]:
            dropped_cards += [tmp[i], tmp[i + 1]]
            tmp[i] = tmp[i + 1] = None
    # print(dropped_cards)
    card = [card for card in card if card not in dropped_cards]
    q.put(card)


def chk_end(human_card, pc_card):
    if human_card == []:
        print('玩家勝利!!')
        return 1
    elif pc_card == []:
        print('電腦勝利!!')
        return 1
    else:
        return 0


if __name__ == "__main__":
    human_card, pc_card = gen_card()
    print_card(human_card, pc_card)
    print('整理牌中...')
    human_card, pc_card = pair(human_card, pc_card)
    print_card(human_card, pc_card)

    while True:
        tmp = int(input('\n請玩家輸入想抽的牌的編號: '))
        human_card.append(pc_card[tmp-1])
        del pc_card[tmp-1]
        human_card, pc_card = pair(human_card, pc_card)
        print_card(human_card, pc_card)

        if chk_end(human_card, pc_card):
            break

        print('\n輪到電腦抽牌...')
        r = random.randint(0, len(human_card)-1)
        pc_card.append(human_card[r])
        del human_card[r]
        human_card, pc_card = pair(human_card, pc_card)
        print_card(human_card, pc_card)

        if chk_end(human_card, pc_card):
            break
