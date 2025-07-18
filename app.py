from flask import Flask, render_template, request, redirect, url_for, session
import random
from strategy import Strategy  # 전략 점수 계산 클래스 사용

app = Flask(__name__)
app.secret_key = "yacht-secret"

strategies = [
    "1s", "2s", "3s", "4s", "5s", "6s",
    "Choice", "3 of a kind", "4 of a kind",
    "Full House", "S. Straight", "L. Straight", "Yacht"
]

def calculate_score(strategy, dice):
    strategy_scores = Strategy(dice).calculate_all()
    return strategy_scores.get(strategy, 0)

@app.route('/')
def index():
    return redirect(url_for('setup'))

@app.route('/setup', methods=['GET', 'POST'])
def setup():
    if request.method == 'POST':
        players = request.form.getlist('players')
        session['players'] = [p.strip() for p in players if p.strip()]
        session['scores'] = [0] * len(session['players'])
        session['turn'] = 0
        session['roll'] = 0
        session['dice'] = [random.randint(1, 6) for _ in range(5)]
        session['kept'] = [False] * 5
        session['used_strategies'] = [{} for _ in session['players']]
        session['history'] = [[] for _ in session['players']]
        return redirect(url_for('game'))
    return render_template('setup.html')

@app.route('/game', methods=['GET', 'POST'])
def game():
    if 'players' not in session or 'scores' not in session:
        return redirect(url_for('setup'))  # 세션이 없으면 setup으로

    if request.method == 'POST':
        if 'toggle' in request.form:
            index = int(request.form['toggle'])
            kept = session.get('kept', [False] * 5)
            kept[index] = not kept[index]
            session['kept'] = kept

        elif request.form.get('action') == 'roll' and session['roll'] < 3:
            dice = session.get('dice', [1] * 5)
            kept = session.get('kept', [False] * 5)
            for i in range(5):
                if not kept[i]:
                    dice[i] = random.randint(1, 6)
            session['dice'] = dice
            session['roll'] += 1

        elif 'strategy' in request.form:
            strat = request.form['strategy']
            turn = session['turn']
            score = calculate_score(strat, session['dice'])

            session['scores'][turn] += score
            session['used_strategies'][turn][strat] = True
            session['history'][turn].append((strat, score))

            session['turn'] = (turn + 1) % len(session['players'])
            session['roll'] = 0
            session['dice'] = [random.randint(1, 6) for _ in range(5)]
            session['kept'] = [False] * 5

        if all(len(player_strats) >= 13 for player_strats in session['used_strategies']):
            return redirect(url_for('game_over'))

    if request.method == 'GET':
        if all(len(player_strats) >= 13 for player_strats in session['used_strategies']):
            return redirect(url_for('game_over'))

    player_name = session['players'][session['turn']]
    used = session['used_strategies'][session['turn']]

    return render_template('index.html',
                           player=player_name,
                           roll=session['roll'],
                           dice=session['dice'],
                           kept=session['kept'],
                           scores=session['scores'],
                           players=session['players'],
                           strategies=strategies,
                           used=used,
                           history=session['history'])

@app.route('/game_over')
def game_over():
    if 'scores' not in session or 'players' not in session or 'history' not in session:
        return redirect(url_for('setup'))

    scores = session['scores']
    players = session['players']
    history = session['history']
    max_score = max(scores)
    winners = [players[i] for i, s in enumerate(scores) if s == max_score]

    rendered = render_template('game_over.html',
                               winners=winners,
                               scores=scores,
                               players=players,
                               history=history)

    session.clear()
    return rendered

if __name__ == "__main__":
    app.run(debug=True)
