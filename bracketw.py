import random

# PROJECT: 2026 Women's NCAA Predictor

# --- KEY DATA POINTS & VARIABLES ---

# KENPOM / NET RATINGS:
# Using adjusted efficiency metrics. 
# Top Tier: UConn (undefeated), UCLA, and South Carolina.
# Dark Horse: Vanderbilt (Ranked #12 in Net, great defensive value).

# VEGAS ODDS & FAVORITES:
# National Title Favorites: UConn (-275), UCLA (+550), Texas (+650).
# Elite Eight Spreads: Looking for teams that cover the spread consistently (e.g., LSU, Texas).

# UPSET WATCH:
# Significant 2026 Upsets: 
# - #10 Virginia defeated #2 Iowa (83-75) in the Round of 32.
# - #6 Notre Dame defeated #2 Vanderbilt (67-64) to reach the Elite Eight.
# - #5 Kentucky defeated #4 West Virginia.

# PREVIOUS GAMES / MOMENTUM:
# - UConn remains undefeated (36-0) heading into the Elite Eight.
# - Hannah Hidalgo (Notre Dame) is on a historic run (Triple-double in Sweet 16).
# - Duke's defense has been suffocating, winning 21 of their last 23 games.

# --- MOMENTUM CALCULATION---
def calculate_momentum(seed, margin_of_victory):
   # (17- seed) makes a #1 seed = 16 and a #16 seed = 1
   seed_factor = 17 - seed
   # Dividing by 10 keeps the margin
   margin_factor= margin_of_victory / 10.0
   momentum_score= seed_factor + margin_factor
   return momentum_score
#--- UPSET WATCH CALCULATION--
def calculate_upset(winner_seed, loser_seed, margin_of_triumph):
    # Everything below this is indented 4 spaces
    "Calculates an 'Upset Factor' based on seed difference and margin."
    
    if winner_seed > loser_seed:
        # Indented 8 spaces because it's inside the 'if'
        seed_diff = winner_seed - loser_seed
        
    elif winner_seed == loser_seed:
        seed_diff = 0.5
        
    else:
        # This returns 0 immediately and exits the function
        return 0 

    # These final two lines are back to 4 spaces 
    # (They only run if the favorite didn't win)
    upset_score = seed_diff * margin_of_triumph
    return upset_score
#--- TEAMS PLAYING MARCH 28 (DATA PENDING RESULTS)---

# --- SATURDAY SWEET 16 + VEGAS SPREADS ---

# Michigan is a 5.5-point favorite
michigan = {"name":"Michigan", "seed":2, "adjem":27.50, "spread":-5.5,
            "upset": calculate_upset(2,7,29), "momentum": calculate_momentum(2,29)}
lousiville = {"name": "Lousiville", "seed": 3, "adjem": 25.80, "spread": 5.5,
              "upset": calculate_upset(3,6,1), "momentum": calculate_momentum(3,1)}

# Texas is a heavy 14.5-point favorite
Kentucky = {"name":"Kentucky", "seed":5, "adjem":21.40, "spread": 14.5,
            "upset": calculate_upset(5,4,1), "momentum": calculate_momentum(5,2)}
Texas = {"name": "Texas", "seed": 1, "adjem": 33.30, "spread": -14.5,
         "upset": calculate_upset(1,8,42), "momentum": calculate_momentum(1,42)}

# South Carolina is a colossal 17.5-point favorite
SouthCarolina = {"name":"SouthCarolina", "seed":1, "adjem":48.20, "spread": -17.5,
                 "upset": calculate_upset(1,8,40), "momentum": calculate_momentum(1,40)}
OKLAHOMA = {"name": "OKLAHOMA", "seed": 4, "adjem": 22.10, "spread": 17.5,
            "upset": calculate_upset(4,5,6), "momentum": calculate_momentum(4,6)}

# TCU is a 9.5-point favorite
tcu = {"name":"TCU", "seed":3, "adjem":26.50, "spread": -9.5,
       "upset": calculate_upset(3,6,3), "momentum": calculate_momentum(3,3)}
virginia = {"name": "Virginia", "seed": 10, "adjem": 18.90, "spread": 9.5,
            "upset": calculate_upset(10,2,8), "momentum": calculate_momentum(10,8)}

def predict_matchup(team1, team2):
    # Vegas Adjustment: We add the favorite's spread to their power
    # (Using abs() on the negative number to get the points)
    v_adj1 = abs(team1["spread"]) if team1["spread"] < 0 else 0
    v_adj2 = abs(team2["spread"]) if team2["spread"] < 0 else 0
    
    power1 = team1["adjem"] + team1["momentum"] + team1["upset"] + v_adj1
    power2 = team2["adjem"] + team2["momentum"] + team2["upset"] + v_adj2
    
    print(f"--- VEGAS-ADJUSTED PREDICTION: {team1['name']} vs {team2['name']} ---")
    print(f"{team1['name']} Power: {power1:.2f}")
    print(f"{team2['name']} Power: {power2:.2f}")
    
    if power1 > power2:
        return f"PREDICTION: {team1['name']} wins!"
    else:
        return f"PREDICTION: {team2['name']} wins!"

# Running the full slate
print(predict_matchup(michigan, lousiville))
print(predict_matchup(Kentucky, Texas))
print(predict_matchup(OKLAHOMA, SouthCarolina))
print(predict_matchup(virginia, tcu))