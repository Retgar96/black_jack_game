
all_hands = [[1, 1]]

def sum_hand(hand = []):
    hand.sort()
    sum = 0
    for card in hand:
        sum +=card

    if sum == 21 and all_comparison(all_hands, hand):
        all_hands.append(hand)
        with open('combination_with_21.txt', 'a') as file:
            file.write(f'{hand};\n')
        return False
    elif sum > 21:
        return  False
    else:
        return True


def all_comparison(all_hands, hand):
    for h in all_hands:
        if h == hand:
            return False
    return True


if __name__ == '__main__':

    with open('combination_with_21.txt', 'w') as file:
        file.write(f'Комбинации карт с 21 очком.\n')

    numbers_classic = [1,2,3,4,5,6,7,8,9,10,11]
    hand = [0,0,0,0,0,0,0,0]


    for card_0 in numbers_classic:
        hand[0] = card_0
        if sum_hand(hand):
            for card_1 in numbers_classic:
                hand[1] = card_1
                if sum_hand(hand):
                    for card_2 in numbers_classic:
                        hand[2] = card_2
                        if sum_hand(hand):
                            for card_3 in numbers_classic:
                                hand[3] = card_3
                                if sum_hand(hand):
                                    for card_4 in numbers_classic:
                                        hand[4] = card_4
                                        if sum_hand(hand):
                                            for card_5 in numbers_classic:
                                                hand[5] = card_5
                                                if sum_hand(hand):
                                                    for card_6 in numbers_classic:
                                                        hand[6] = card_6
                                                        if sum_hand(hand):
                                                            for card_7 in numbers_classic:
                                                                hand[7] = card_7
                                                                sum_hand(hand)
                                                                    # print(hand)
                                                        else:
                                                            hand[7] = 0

                                                else:
                                                    hand[6] = 0
                                                    break
                                        else:
                                            hand[5] = 0
                                            break
                                else:
                                    hand[4] = 0
                                    break
                        else:
                            hand[3] = 0
                            break
                else:
                    hand[2] = 0
                    break
        else:
            hand[1] = 0
            break




