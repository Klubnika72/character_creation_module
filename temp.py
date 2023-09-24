# Тестовые данные.
<<<<<<< HEAD
TEST_DATA: list[tuple[int, str, bool]] = [
=======
TEST_DATA = [
>>>>>>> a459ef30904b699cf49192b2ea5bbfc2b67d1d46
    (44, 'success', True),
    (16, 'failure', True),
    (4, 'success', False),
    (21, 'failure', False),
]

<<<<<<< HEAD
BONUS: float = 1.1
ANTIBONUS: float = 0.8


def add_rep(current_rep: float,
            rep_points: int, buf_effect: bool) -> float:
=======
BONUS = 1.1
ANTIBONUS = 0.8


def add_rep(current_rep,
            rep_points, buf_effect):
>>>>>>> a459ef30904b699cf49192b2ea5bbfc2b67d1d46
    current_rep += rep_points
    if buf_effect:
        return current_rep * BONUS
    return current_rep


<<<<<<< HEAD
def remove_rep(current_rep: float,
               rep_points: int, debuf_effect: bool) -> float:
=======
def remove_rep(current_rep,
               rep_points, debuf_effect):
>>>>>>> a459ef30904b699cf49192b2ea5bbfc2b67d1d46
    current_rep -= rep_points
    if debuf_effect:
        return current_rep * ANTIBONUS
    return current_rep


<<<<<<< HEAD
def main(duel_res: float) -> float:
=======
def main(duel_res):
>>>>>>> a459ef30904b699cf49192b2ea5bbfc2b67d1d46
    current_rep = 0.0
    for rep, result, effect in duel_res:
        if result == 'success':
            current_rep = add_rep(current_rep, rep, effect)
        if result == 'failure':
            current_rep = remove_rep(current_rep, rep, effect)
    return (f'После {len(duel_res)} поединков, '
            f'репутация персонажа — {current_rep:.3f} очков.')


# Тестовый вызов функции main.
print(main(TEST_DATA))