import itertools
from collections import defaultdict
from random import shuffle


class Game:
    def __init__(self, player1, player2):
        self.players = {player1, player2}

    def __eq__(self, obj):
        return self.players == obj.players

    def __repr__(self):
        t = sorted(list(self.players))
        return f'{t[0]} | {t[1]}'


class TournamentGenerator:

    @staticmethod
    def _print_gameday(day_num, byes, games):
        byes_section = f'{byes} has a bye' if byes else 'No byes'
        print(f'Day {day_num} - {byes_section}. Games:')
        for g in games:
            print(f'\t{g}')
        print('-----------------')

    def __init__(self, players):
        self.players = players
        self.all_games = list(Game(*list(c)) for c in itertools.combinations(players, 2))
        shuffle(self.all_games)

    def print_tournament(self, games_per_player_per_day_cap, games_per_day_cap):
        day = 1
        occurred_games = [
            Game('Casey', 'Chris'),
            Game('Lawrence', 'Matt'),
            Game('Alex', 'Thomas')
        ]
        self._print_gameday(day, ['Adrian'], occurred_games)

        day += 1
        day2_games = [
            Game('Alex', 'Chris'),
            Game('Lawrence', 'Casey'),
            Game('Adrian', 'Matt')
        ]
        occurred_games.extend(day2_games)
        self._print_gameday(2, ['Thomas'], day2_games)

        remaining_games = [g for g in self.all_games if g not in occurred_games]

        while remaining_games:
            day += 1
            games_per_player = defaultdict(int)

            daily_games = []

            orig_len = len(remaining_games)
            for idx, g in enumerate(reversed(remaining_games)):
                orig_idx = orig_len - idx - 1
                p1, p2 = g.players
                games_per_player[p1]
                games_per_player[p2]
                if games_per_player[p1] < games_per_player_per_day_cap and games_per_player[p2] < games_per_player_per_day_cap:
                    games_per_player[p1] += 1
                    games_per_player[p2] += 1
                    daily_games.append(remaining_games.pop(orig_idx))
                    if len(daily_games) == games_per_day_cap:
                        break

            self._print_gameday(day, [p for p in self.players if games_per_player[p] == 0], daily_games)


def main():
    players = ['Casey', 'Thomas', 'Lawrence', 'Chris', 'Matt', 'Adrian', 'Alex']
    games_per_player_per_day_cap = 2
    games_per_day_cap = 4
    tg = TournamentGenerator(players)

    tg.print_tournament(games_per_player_per_day_cap, games_per_day_cap)


if __name__ == '__main__':
    main()
