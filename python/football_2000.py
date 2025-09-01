#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Football 2000 - Russian Football League Simulator
Ported from BASIC to Python with detailed match simulation
"""

import random
import time
import os
import sys

class FootballGame:
    def __init__(self):
        # Initialize random seed
        random.seed(time.time())

        # Team names in Russian
        self.teams = [
            "Арсенал", "Астон Вилла", "Блэкборн", "Болтон", "Челси",
            "Ковентри", "Манчестер Юнайтед", "Ньюкастл", "Эвертон", "Лидс",
            "Ливерпуль", "Манчестер Сити", "Мидлсброу", "Ноттингем", "Тотенхем",
            "Королевский парк", "Шеффилд", "Уэстхем", "Саутгемптон", "Уимблдон"
        ]

        # Team strength ratings
        self.team_strength = [
            970, 830, 910, 430, 810, 385, 1100, 1180, 665, 900,
            975, 860, 890, 880, 910, 840, 790, 770, 550, 685
        ]

        # Players for each team (16 players per team)
        self.players = [
            # Team 1 - Арсенал
            ["Симан", "Диксон", "Кеоун", "Винтербурн", "Диксон", "Адамс", "Мерсон", "Хелдер",
             "Лужный", "Бергкамп", "Кивомия", "Бертрам", "Боулд", "Парлоур", "Дженсен", "Хартсон"],

            # Team 2 - Астон Вилла
            ["Соунсенд", "Милошевич", "Босинч", "Спинк", "Енюогу", "Карр", "Саутгейт", "Стаунтон",
             "Джонсон", "Йорк", "Тарелли", "Скимека", "Чарлз", "Макграф", "Кинг", "Дрейпер"],

            # Team 3 - Блэкборн
            ["Флауэрс", "Галашер", "Берг", "Хендри", "Силкокс", "Бохинен", "Кервуд", "Кенна",
             "Рипли", "Саттон", "Кирар", "Мимс", "Ле Сокс", "Гудмунсон", "Маккинли", "Невелл"],

            # Team 4 - Болтон
            ["Бранаган", "Девисон", "Бергссон", "Колеман", "Тейрклоу", "Курсик", "Селларс", "Ли",
             "Макгинли", "Блейк", "Паателайнен", "Грин", "Филипс", "Стубс", "Томпсон", "Дефрейтас"],

            # Team 5 - Челси
            ["Харин", "Синклер", "Спенсер", "Джонсен", "К��арк", "Гуллит", "Тайз", "Тарлонг",
             "Тьюа", "Джола", "Петреску", "Хичкок", "Барли", "Ли", "Телан", "Пикок"],

            # Team 6 - Ковентри
            ["Борроуз", "Огризович", "Басст", "Ноу", "Ричардсон", "Джесс", "Хелан", "Страшан",
             "Ндлову", "Дублин", "Салако", "Морган", "Гоулд", "Борроуз", "Пикеринг", "Дерби"],

            # Team 7 - Манчестер Юнайтед
            ["Шмейхель", "Брюс", "Невилл", "Бекхем", "Мэй", "Ирвин", "Скоулс", "Коул",
             "Шерингем", "Кин", "Палистер", "Макклейр", "Ван Дер Гоу", "Шарп", "Батт", "Гигс"],

            # Team 8 - Ньюкастл
            ["Гислоп", "Хоуэй", "Бартон", "Джинола", "Бетти", "Китсон", "Тердинанда", "Асприлья",
             "Пикок", "Ли", "Гиллеспи", "Кларк", "Бересфорд", "Бердсли", "Срникеке", "Альберт"],

            # Team 9 - Эвертон
            ["Саутолл", "Эмбрелл", "Уотсон", "Хоттигер", "Канчелскис", "Лимпар", "Амокачи", "Норт",
             "Тергюсон", "Райдаут", "Хин��лиффе", "Киртон", "Джексон", "Ансворт", "Паркинсон", "Стюарт"],

            # Team 10 - Лидс
            ["Лукич", "Дориго", "Ветеран", "Келли", "Макалистер", "Рейдеби", "Палмер", "Уайт",
             "Дин", "Йебоан", "Пролин", "Бини", "Ремберт", "Спид", "Толис", "Торнингтон"],

            # Team 11 - Ливерпуль
            ["Джеймс", "Бабб", "Руддок", "Скейлс", "Джонс", "Макатир", "Барнс", "Макманаман",
             "Оуэн", "Тауэлер", "Колимор", "Редкнапп", "Стенгард", "Бьорнеби", "Харкнес", "Т��мас"],

            # Team 12 - Манчестер Сити
            ["Кинкладзе", "Шумерби", "Дибл", "Керннаган", "Курл", "Тронтжек", "Вонк", "Рослер",
             "Куин", "Ломас", "Симонс", "Иммел", "Брайтвелл", "Бигри", "Клоу", "Тликрофт"],

            # Team 13 - Мидлсброу
            ["Адамс", "Эмерсон", "Барнби", "Флеминг", "Морис", "Поллок", "Бранко", "Уайт",
             "Хигнет", "Джуниньо", "Тьортофт", "Толш", "Кокс", "Пирсон", "Мур", "Хендри"],

            # Team 14 - Ноттингем
            ["Стоун", "Пирс", "Хааланд", "Кроссли", "Тоан", "Кемпбел", "Ли", "Джемил",
             "Рой", "Силензи", "Барт-Вилья", "Купер", "Райт", "Литл", "Филипс", "Четтл"],

            # Team 15 - Тотенхем
            ["Токер", "Кемпбелл", "Токс", "Каддервуд", "Мабют", "Остин", "Уилсон", "Синтон",
             "Розентал", "Армстронг", "Раш", "Коуэлс", "Дозелл", "Курслейк", "Торсведт", "Андертон"],

            # Team 16 - Королевский парк
            ["Соммер", "Макдоналд", "Бардсли", "Синклер", "Хателли", "Холлоуэй", "Бреветт", "Дичио",
             "Ятес", "Импи", "Куаши", "Галлен", "Робертс", "Мелдикс", "Паркер", "Реди"],

            # Team 17 - Шеффилд
            ["Вудс", "Брискоу", "Токер", "Стефанович", "Нолан", "Деграйси", "Толда", "Брайт",
             "Дж��нс", "Херст", "Хайд", "Витингем", "Флинкер", "Прессман", "Меридан", "Ковачевич"],

            # Team 18 - Уэстхем
            ["Коти", "Хагс", "Билич", "Монкур", "Брейкер", "Микложко", "Мартин", "Дикс",
             "Димитреску", "Бишоп", "Слейтер", "Доуи", "Дани", "Сили", "Потс", "Рипер"],

            # Team 19 - Саутгемптон
            ["Луккич", "Дориго", "Ветеран", "Келли", "Макалистер", "Рейдеби", "Палмер", "Уайт",
             "Дин", "Йебоан", "Пролин", "Бини", "Ремберт", "Спид", "Толис", "��орнингтон"],

            # Team 20 - Уимблдон
            ["Саливан", "Фирэ", "Джонс", "Кимбл", "Ардли", "Ленардуцци", "Гейл", "Кларк",
             "Экоку", "Госдэн", "Харфорд", "Каннингэм", "Робсон", "Блисетт", "Барнетт", "Рид"]
        ]

        # Player ratings for each team (16 players per team)
        self.player_ratings = [
            [80,90,60,60,60,80,70,70,70,80,60,30,40,30,50,40],  # Арсенал
            [60,50,60,40,70,60,60,70,60,70,70,30,30,40,30,30],  # Астон Вилла
            [70,90,50,50,60,50,60,70,70,70,90,30,40,40,30,40],  # Блэкборн
            [30,20,30,10,20,70,30,50,50,50,30,5,20,5,5,5],     # Болтон
            [60,60,50,60,80,60,50,40,80,80,40,50,30,10,30,30],  # Челси
            [20,40,20,20,20,50,30,70,50,10,30,5,5,5,5,5],      # Ковентри
            [80,70,60,60,60,80,80,90,90,70,80,60,60,40,60,60],  # Манчестер Юнайтед
            [70,90,70,80,70,80,90,90,80,80,70,60,70,70,60,50],  # Ньюкастл
            [50,60,40,30,60,50,70,40,60,60,50,30,40,20,30,20],  # Эвертон
            [40,50,30,40,60,70,50,60,70,70,60,40,50,60,40,30],  # Лидс
            [70,80,70,60,70,80,80,90,90,80,70,70,60,60,70,50],  # Ливерпуль
            [50,60,40,50,40,60,60,70,60,60,50,40,50,40,30,30],  # Манчестер Сити
            [60,70,60,50,50,60,80,70,80,90,70,50,60,50,40,40],  # Мидлсброу
            [50,60,50,40,40,50,60,60,70,70,60,40,50,40,30,30],  # Ноттингем
            [60,70,60,50,60,70,70,80,80,70,60,50,60,50,40,40],  # Тотенхем
            [40,50,40,30,30,40,50,50,60,50,40,30,40,30,20,20],  # Королевский парк
            [50,60,50,40,40,50,60,60,70,60,50,40,50,40,30,30],  # Шеффилд
            [50,60,60,50,50,60,70,70,80,70,60,50,60,50,40,40],  # Уэстхем
            [40,50,30,40,60,70,50,60,70,70,60,40,50,60,40,30],  # Саутгемптон
            [30,40,30,20,30,40,40,50,60,50,40,30,40,30,20,20]   # Уимблдон
        ]

        # Match state variables
        self.score1 = 0
        self.score2 = 0
        self.minute = 0
        self.ball_holder = 0
        self.team_with_ball = 1
        self.match_events = []

    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def wait_for_key(self, message="Нажмите любую клавишу для продолжения..."):
        """Wait for user input"""
        input(message)

    def display_teams(self):
        """Display all teams with their strength ratings"""
        print("\n=== ФУТБОЛ 2000 ===")
        print("Команды и их рейтинги силы:")
        print("-" * 40)
        for i, (team, strength) in enumerate(zip(self.teams, self.team_strength), 1):
            print(f"{i:2d}. {team:<20} - {strength}")

    def select_lineup(self, team_idx):
        """Select 11 players from 16 available for a team"""
        print(f"\nВЫБЕРИТЕ ИГРОКОВ СТАРТОВОГО СОСТАВА (11) для команды {self.teams[team_idx]}")
        print("Игрок          Рейтинг")

        for j in range(16):
            if self.player_ratings[team_idx][j] > 0:
                print(f"{j+1:2d}. {self.players[team_idx][j]:<15} {self.player_ratings[team_idx][j]}")

        lineup = []
        ratings = []
        selected_indices = []

        for i in range(11):
            while True:
                try:
                    choice = int(input(f"Выберите игрока #{i+1}: ")) - 1
                    if 0 <= choice < 16 and self.player_ratings[team_idx][choice] > 0:
                        if choice not in selected_indices:
                            lineup.append(self.players[team_idx][choice])
                            ratings.append(self.player_ratings[team_idx][choice])
                            selected_indices.append(choice)
                            break
                        else:
                            print("Этот игрок уже выбран!")
                    else:
                        print("Неверный выбор!")
                except (ValueError, KeyboardInterrupt):
                    print("Введите число или нажмите Ctrl+C для выхода!")
                except Exception as e:
                    print(f"Ошибка: {e}")

        return lineup, ratings

    def display_match_header(self, team1_idx, team2_idx, lineup1, lineup2):
        """Display match information"""
        self.clear_screen()
        print(f"  ДОБРО ПОЖАЛОВАТЬ НА МАТЧ   {self.teams[team1_idx]}:{self.teams[team2_idx]}")
        print("  Составы команд:")
        print("=" * 60)

        for i in range(11):
            print(f"{lineup1[i]:<25} {lineup2[i]}")

        self.wait_for_key()

    def draw_field(self, ball_pos_x=50):
        """Draw ASCII football field"""
        print("=" * 70)
        print("║" + " " * 68 + "║")
        print("║  ┌────┐" + " " * 50 + "┌────┐  ║")
        print("║  │ GK │" + " " * 50 + "│ GK │  ║")
        print("║  └────���" + " " * 50 + "└────┘  ║")
        print("║" + " " * 68 + "║")

        # Ball position line
        ball_line = "║" + " " * ball_pos_x + "⚽" + " " * (67 - ball_pos_x) + "║"
        print(ball_line)

        print("║" + " " * 68 + "║")
        print("=" * 70)

    def simulate_action(self, lineup1, ratings1, lineup2, ratings2):
        """Simulate a single action in the match"""
        action_type = random.randint(1, 100)

        if action_type <= 60:  # Normal play
            return self.normal_play(lineup1, ratings1, lineup2, ratings2)
        elif action_type <= 70:  # Shot on goal
            return self.shot_on_goal(lineup1, ratings1, lineup2, ratings2)
        elif action_type <= 80:  # Foul
            return self.handle_foul(lineup1, ratings1, lineup2, ratings2)
        elif action_type <= 90:  # Corner kick
            return self.corner_kick()
        else:  # Offside
            return self.offside()

    def normal_play(self, lineup1, ratings1, lineup2, ratings2):
        """Normal play action"""
        if self.team_with_ball == 1:
            current_lineup = lineup1
            current_ratings = ratings1
        else:
            current_lineup = lineup2
            current_ratings = ratings2

        # Random player gets the ball
        self.ball_holder = random.randint(0, 10)
        player_name = current_lineup[self.ball_holder]

        # Check if player loses the ball
        if random.randint(1, 100) > current_ratings[self.ball_holder]:
            self.team_with_ball = 3 - self.team_with_ball  # Switch teams (1->2, 2->1)
            return f"Мяч потерян! {player_name} теряет мяч"

        return f"{player_name} ведет мяч"

    def shot_on_goal(self, lineup1, ratings1, lineup2, ratings2):
        """Handle shot on goal"""
        if self.team_with_ball == 1:
            shooter = lineup1[self.ball_holder]
            shooter_rating = ratings1[self.ball_holder]
            goalkeeper = lineup2[0]  # First player is goalkeeper
            gk_rating = ratings2[0]
            attacking_team = 1
        else:
            shooter = lineup2[self.ball_holder]
            shooter_rating = ratings2[self.ball_holder]
            goalkeeper = lineup1[0]
            gk_rating = ratings1[0]
            attacking_team = 2

        shot_quality = random.randint(1, 100) + shooter_rating
        save_quality = random.randint(1, 100) + gk_rating

        if shot_quality > save_quality + 20:
            # Goal!
            if attacking_team == 1:
                self.score1 += 1
            else:
                self.score2 += 1

            self.draw_goal_animation(shooter)
            return f"ГОООЛ!!! {shooter} забивает! Счет {self.score1}:{self.score2}"

        elif shot_quality > save_quality:
            return f"{shooter} бьет по воротам, но {goalkeeper} отбивает!"

        else:
            return f"{shooter} бьет мимо ворот!"

    def draw_goal_animation(self, scorer):
        """Draw goal celebration"""
        self.clear_screen()
        print("\n" * 5)
        print("  " + "ГОООЛ!!!" * 8)
        print(f"\n  Гол забил {scorer}!")
        print(f"  Счет: {self.score1}:{self.score2}")
        print("\n" + "  ⚽ " * 20)
        time.sleep(2)

    def handle_foul(self, lineup1, ratings1, lineup2, ratings2):
        """Handle foul situations"""
        foul_type = random.randint(1, 100)

        if foul_type <= 70:
            return self.free_kick(lineup1, ratings1, lineup2, ratings2)
        else:
            return self.penalty_kick(lineup1, ratings1, lineup2, ratings2)

    def free_kick(self, lineup1, ratings1, lineup2, ratings2):
        """Handle free kick"""
        self.clear_screen()
        print("НАРУШЕНИЕ ПРАВИЛ")
        print("В ваши ворота назначен штрафной удар.")

        if self.team_with_ball == 1:
            print("\nВыберите игрока который его выполнит:")
            for i in range(11):
                print(f"{i+1}. {lineup1[i]} - {ratings1[i]}")

            while True:
                try:
                    choice = int(input("Вы выбрали: ")) - 1
                    if 0 <= choice < 11:
                        break
                except ValueError:
                    pass

            kicker_rating = ratings1[choice]
            gk_rating = ratings2[0]
            kicker_name = lineup1[choice]
            gk_name = lineup2[0]
        else:
            # AI team takes free kick
            choice = random.randint(0, 10)
            kicker_rating = ratings2[choice]
            gk_rating = ratings1[0]
            kicker_name = lineup2[choice]
            gk_name = lineup1[0]

        # Calculate free kick result
        kick_quality = random.randint(1, 100) + kicker_rating
        save_quality = random.randint(1, 100) + gk_rating

        self.animate_free_kick()

        if kick_quality > save_quality + 30:
            if self.team_with_ball == 1:
                self.score1 += 1
            else:
                self.score2 += 1
            return f"ГОООЛ с штрафного! {kicker_name} забивает! Счет {self.score1}:{self.score2}"
        elif kick_quality > save_quality:
            return f"{kicker_name} бьет штрафной, {gk_name} отбивает!"
        else:
            return f"{kicker_name} бьет штрафной мимо ворот!"

    def penalty_kick(self, lineup1, ratings1, lineup2, ratings2):
        """Handle penalty kick"""
        self.clear_screen()
        print("В ваши ворота назначено ПЕНАЛЬТИ!")

        if self.team_with_ball == 1:
            print("\nВыберите игрока который его выполнит:")
            for i in range(11):
                print(f"{i+1}. {lineup1[i]} - {ratings1[i]}")

            while True:
                try:
                    choice = int(input("Вы выбрали: ")) - 1
                    if 0 <= choice < 11:
                        break
                except ValueError:
                    pass

            kicker_rating = ratings1[choice]
            gk_rating = ratings2[0]
            kicker_name = lineup1[choice]
            gk_name = lineup2[0]
        else:
            choice = random.randint(0, 10)
            kicker_rating = ratings2[choice]
            gk_rating = ratings1[0]
            kicker_name = lineup2[choice]
            gk_name = lineup1[0]

        # Penalty calculation
        kick_quality = random.randint(1, 100) + kicker_rating
        save_quality = random.randint(1, 100) + gk_rating

        self.animate_penalty()

        if kick_quality > save_quality + 20:
            if self.team_with_ball == 1:
                self.score1 += 1
            else:
                self.score2 += 1
            return f"ПЕНАЛЬТИ ЗАБИТ! {kicker_name} не ош��бается! Счет {self.score1}:{self.score2}"
        else:
            return f"ПЕНАЛЬТИ НЕ ЗАБИТ! {gk_name} отбивает удар {kicker_name}!"

    def animate_free_kick(self):
        """Animate free kick"""
        print("\n" + "⚽ летит к воротам..." + "." * 20)
        time.sleep(1)

    def animate_penalty(self):
        """Animate penalty kick"""
        print("\n" + "ПЕНАЛЬТИ! Игрок готовится к удару...")
        time.sleep(1)
        print("⚽ УДАР!")
        time.sleep(1)

    def corner_kick(self):
        """Handle corner kick"""
        return "Угловой удар!"

    def offside(self):
        """Handle offside"""
        self.team_with_ball = 3 - self.team_with_ball
        return "Офсайд! Мяч переходит к противнику"

    def simulate_detailed_match(self, team1_idx, team2_idx):
        """Simulate detailed match with real-time action"""
        print(f"\n=== МАТЧ: {self.teams[team1_idx]} против {self.teams[team2_idx]} ===")

        # Select lineups
        lineup1, ratings1 = self.select_lineup(team1_idx)

        # AI selects lineup for team 2
        lineup2 = []
        ratings2 = []
        available = list(range(16))
        for _ in range(11):
            # AI picks best available players
            best_idx = max(available, key=lambda x: self.player_ratings[team2_idx][x])
            lineup2.append(self.players[team2_idx][best_idx])
            ratings2.append(self.player_ratings[team2_idx][best_idx])
            available.remove(best_idx)

        self.display_match_header(team1_idx, team2_idx, lineup1, lineup2)

        # Initialize match
        self.score1 = 0
        self.score2 = 0
        self.minute = 0
        self.team_with_ball = random.randint(1, 2)
        self.ball_holder = random.randint(0, 10)

        # Simulate 90 minutes
        for minute in range(1, 91):
            self.minute = minute

            # Every 5 minutes, show action
            if minute % 5 == 0:
                self.clear_screen()
                self.draw_field(random.randint(10, 60))
                print(f"\nМинута: {minute}")
                print(f"Счет: {self.teams[team1_idx]} {self.score1} - {self.score2} {self.teams[team2_idx]}")

                # Simulate action
                event = self.simulate_action(lineup1, ratings1, lineup2, ratings2)
                print(f"\n{event}")

                if minute < 90:
                    time.sleep(2)  # Pause between actions

        # Final result
        self.clear_screen()
        print(f"\n=== МАТЧ ОКОНЧЕН ===")
        print(f"{self.teams[team1_idx]} {self.score1} - {self.score2} {self.teams[team2_idx]}")

        if self.score1 > self.score2:
            print(f"Победа: {self.teams[team1_idx]}!")
        elif self.score2 > self.score1:
            print(f"Победа: {self.teams[team2_idx]}!")
        else:
            print("Ничья!")

        self.wait_for_key()

    def display_team_players(self, team_index):
        """Display players for a specific team"""
        if 0 <= team_index < len(self.teams):
            print(f"\nИгроки команды {self.teams[team_index]}:")
            print("-" * 50)
            for i, (player, rating) in enumerate(zip(self.players[team_index], self.player_ratings[team_index]), 1):
                print(f"{i:2d}. {player:<20} - Рейтинг: {rating}")
        else:
            print("Неверный номер команды!")

    def run_menu(self):
        """Main game menu"""
        while True:
            self.clear_screen()
            print("\n=== ФУТБОЛ 2000 ===")
            print("ГЛАВНОЕ МЕНЮ")
            print("=" * 30)
            print("1. Показать все команды")
            print("2. Показать игроков команды")
            print("3. Детальная симуляция матча")
            print("4. Быстрый матч")
            print("5. Случайный матч")
            print("6. Выход")

            choice = input("\nВыберите опцию (1-6): ").strip()

            if choice == '1':
                self.display_teams()
                self.wait_for_key()

            elif choice == '2':
                self.display_teams()
                try:
                    team_num = int(input("\nВведите номер команды (1-20): ")) - 1
                    if 0 <= team_num < 20:
                        self.display_team_players(team_num)
                        self.wait_for_key()
                    else:
                        print("Неверный номер команды!")
                        self.wait_for_key()
                except ValueError:
                    print("Пожалуйста, введит�� корректный но��ер!")
                    self.wait_for_key()

            elif choice == '3':
                self.display_teams()
                try:
                    team1 = int(input("\nВведите номе�� первой команды (1-20): ")) - 1
                    team2 = int(input("Введите номер второй команды (1-20): ")) - 1
                    if 0 <= team1 < 20 and 0 <= team2 < 20 and team1 != team2:
                        self.simulate_detailed_match(team1, team2)
                    else:
                        print("Н��верные номера ��оманд!")
                        self.wait_for_key()
                except ValueError:
                    print("Пожалуйста, введите корректные номера!")
                    self.wait_for_key()

            elif choice == '4':
                self.display_teams()
                try:
                    team1 = int(input("\nВведите номер первой команды (1-20): ")) - 1
                    team2 = int(input("Введите номер второй команды (1-20): ")) - 1
                    if 0 <= team1 < 20 and 0 <= team2 < 20 and team1 != team2:
                        self.quick_match(team1, team2)
                    else:
                        print("Неверные номера команд!")
                        self.wait_for_key()
                except ValueError:
                    print("Пожалуйста, введите корректные номера!")
                    self.wait_for_key()

            elif choice == '5':
                team1 = random.randint(0, 19)
                team2 = random.randint(0, 19)
                while team2 == team1:
                    team2 = random.randint(0, 19)
                self.simulate_detailed_match(team1, team2)

            elif choice == '6':
                print("Спасибо за игру!")
                break

            else:
                print("Неверный выбор! Пожалуйста, выберите 1-6.")
                self.wait_for_key()

    def quick_match(self, team1_idx, team2_idx):
        """Quick match simulation without detailed play-by-play"""
        team1 = self.teams[team1_idx]
        team2 = self.teams[team2_idx]
        strength1 = self.team_strength[team1_idx]
        strength2 = self.team_strength[team2_idx]

        # Calculate goals based on team strength and random factors
        base_goals1 = (strength1 / 400) + random.uniform(0, 2)
        base_goals2 = (strength2 / 400) + random.uniform(0, 2)

        goals1 = max(0, int(base_goals1))
        goals2 = max(0, int(base_goals2))

        print(f"\n=== БЫСТРЫЙ МАТЧ ===")
        print(f"{team1} {goals1} - {goals2} {team2}")

        if goals1 > goals2:
            print(f"Победа: {team1}!")
        elif goals2 > goals1:
            print(f"Победа: {team2}!")
        else:
            print("Ничья!")

        self.wait_for_key()

def main():
    """Main function to start the game"""
    try:
        game = FootballGame()
        game.run_menu()
    except KeyboardInterrupt:
        print("\n\nИгра прервана пользователем. До свидания!")
    except Exception as e:
        print(f"\nПроизошла ошибка: {e}")
        print("Пожалуйста, перезапустите игру.")

if __name__ == "__main__":
    main()
