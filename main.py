from flask import Flask,render_template,request
import joblib
import numpy as np
app = Flask(__name__)
model = joblib.load('IPL_winner_prediction.pkl')

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    temp_array = list()
    toss_winner = list()

    if request.method == 'POST':

        #Team1
        team1 = request.form['Team1']
        if team1 == 'Chennai Super Kings':
            temp_array = temp_array + [1] * 1 + [0] * 6
        elif team1 == 'Kings XI Punjab':
            temp_array = temp_array + [0] * 1 + [1] * 1 + [0] * 5
        elif team1 == 'Kolkata Knight Riders':
            temp_array = temp_array + [0] * 2 + [1] * 1 + [0] * 4
        elif team1 == 'Mumbai Indians':
            temp_array = temp_array + [0] * 3 + [1] * 1 + [0] * 3
        elif team1 == 'Rajasthan Royals':
            temp_array = temp_array + [0] * 4 + [1] * 1 + [0] * 2
        elif team1 == 'Royal Challengers Bangalore':
            temp_array = temp_array + [0] * 5 + [1] * 1 + [0] * 1
        else:
            temp_array = temp_array + [0] * 6 + [1] * 1

        # Team2
        team2 = request.form['Team2']
        if team2 == 'Chennai Super Kings':
            temp_array = temp_array + [1] * 1 + [0] * 6
        elif team2 == 'Kings XI Punjab':
            temp_array = temp_array + [0] * 1 + [1] * 1 + [0] * 5
        elif team2 == 'Kolkata Knight Riders':
            temp_array = temp_array + [0] * 2 + [1] * 1 + [0] * 4
        elif team2 == 'Mumbai Indians':
            temp_array = temp_array + [0] * 3 + [1] * 1 + [0] * 3
        elif team2 == 'Rajasthan Royals':
            temp_array = temp_array + [0] * 4 + [1] * 1 + [0] * 2
        elif team2 == 'Royal Challengers Bangalore':
            temp_array = temp_array + [0] * 5 + [1] * 1 + [0] * 1
        else:
            temp_array = temp_array + [0] * 6 + [1] * 1

        #Team1_pts
        Team1_pts = int(request.form['Team1_pts'])

        #Team1_NRR
        Team1_NRR = float(request.form['Team1_NRR'])

        #Team2_pts
        Team2_pts = int(request.form['Team2_pts'])

        #Team2_NRR
        Team2_NRR = float(request.form['Team2_NRR'])

        # toss_win
        toss_win = request.form['Toss_winnng_team']
        if toss_win == 'Chennai Super Kings':
            toss_winner = toss_winner + [1] * 1 + [0] * 6
        elif toss_win == 'Kings XI Punjab':
            toss_winner = toss_winner + [0] * 1 + [1] * 1 + [0] * 5
        elif toss_win == 'Kolkata Knight Riders':
            toss_winner = toss_winner + [0] * 2 + [1] * 1 + [0] * 4
        elif toss_win == 'Mumbai Indians':
            toss_winner = toss_winner + [0] * 3 + [1] * 1 + [0] * 3
        elif toss_win == 'Rajasthan Royals':
            toss_winner = toss_winner + [0] * 4 + [1] * 1 + [0] * 2
        elif toss_win == 'Royal Challengers Bangalore':
            toss_winner = toss_winner + [0] * 5 + [1] * 1 + [0] * 1
        else:
            toss_winner = toss_winner + [0] * 6 + [1] * 1

        temp_array = [Team1_pts]+[Team1_NRR]+[Team2_pts]+[Team2_NRR] + temp_array + toss_winner
        pred_array = np.array([temp_array])
        prediction = model.predict(pred_array)[0]

    return render_template('result.html',Winner=prediction,team1=team1,team2=team2,Team1_pts=Team1_pts,Team2_pts=Team2_pts,Team1_NRR=Team1_NRR,Team2_NRR=Team2_NRR,temp_array=temp_array)

if __name__ == '__main__':
    app.run(debug=True)