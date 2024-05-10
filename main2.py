import math

# coefficients for risk calculation
coefficients = {
    "intercept": [-3.24351831113285, -8.81611015024614, -13.9542686674263],
    "age": [0.0497993850335345, 0.0887900821192252, 0.113640039476673],
    "ascites": [1.51797138812861, 2.37140129721831, 3.08927465242668],
    "bleeding": [1.17418453645172, 2.59967997874157, 3.23975652348996],
    "bmi": [0.0884386364902865, 0.162320037925795, 0.159418297492223],
    "dminsulin": [2.27518467134173, 3.77362614842436, 4.35763150530437],
    "dmnoninsulinmed": [1.72074309477173, 2.46114747451174, 2.58147786059758],
    "dialysis": [9.2428669797984, 6.41828547432435, 8.53461931969202],
    "dissem_cancer": [2.21496632424592, 3.68543364904125, 3.97845701666912],
    "dypsneaexert": [0.879072990128699, 1.71327881147886, 2.36863119520404],
    "dypsnearest": [0.74865913121185, 1.71833560678456, 2.73500348220787],
    "partialdep": [1.47354081204275, 2.63664553966606, 3.19397136180891],
    "fulldep": [9.38888111430853, 12.3858665516951, 13.687069734634],
    "chf": [0.182975421162722, 2.10495927136399, 3.3625262596574],
    "copd": [1.61737020813774, 3.06139282713194, 3.7439295098463],
    "htnmed": [2.45356319429656, 3.08198135894838, 3.44548888192323],
    "sirs": [0.491545532218731, 0.804282970648836, 1.08580901808062],
    "sepsis": [0.723575023319239, 0.958064998788846, 1.41488334723383],
    "sepshock": [-8.82611893338179, -3.2229106168553, -2.17321141919362],
    "asian": [-0.318803652840306, -0.533453481364095, -1.00588149705396],
    "black": [-0.0810928588581289, 0.0138730751472354, 0.0759400261726127],
    "hisp": [-0.221275223784211, -0.309478451542563, -0.266678911378697],
    "other_race": [-0.08277715695164, 0.0318240176047917, -0.32690162035079],
    "unknown_race": [-0.747166691899994, -1.09683175003938, -0.965137117213889],
    "renalfail": [0.76002624838999, 2.29605765188033, 2.93133637315272],
    "male": [-0.503406543681855, -0.332361244418369, 0.147728559435881],
    "smoke": [1.29123631147632, 1.80075235287704, 2.08515237349285],
    "steriod": [2.27223880532616, 3.23260333396562, 3.49926215775259],
    "transfusion": [1.24167149658114, 2.10457246760009, 2.93392252563445],
    "ventilator": [0.465436345926141, 1.6507592539009, 2.4063879264187],
    "open_wound_infect": [0.444602266409906, 1.2722325796638, 1.84069552523472],
    "weight_loss": [1.53567146257999, 2.6311769776807, 2.74604881740667]
}

# example features
features = {
    "age": 50,
    "male": 1,
    "bmi": 26,
   
    "partialdep": 0,
    "fulldep": 0,
    "dminsulin": 1,
    "dypsneaexert": 0,
    "dypsnearest": 0,
    "copd": 0,
    "chf": 0,
    "htnmed": 0,
    "smoke": 1,
    "dialysis": 0,
    "renalfail": 0,
    "ventilator": 0,

    "ascites": 0,
    "bleeding": 0,
    "dissem_cancer": 0,
    "sirs": 0,
    "sepsis": 0,
    "sepshock": 0,
    "asian": 0,
    "black": 0,
    "hisp": 0,
    "other_race": 0,
    "unknown_race": 0,
    "steriod": 0,
    "transfusion": 0,
    "open_wound_infect": 0,
    "weight_loss": 0
    
}

# calculate asa scores
def calculate_asa_score(coefficients, features):
    score = coefficients['intercept']
    for feature, coef_list in coefficients.items():
        if feature != 'intercept':
            index = min(len(coef_list) - 1, features.get(feature, 0))
            score += coef_list[index]
    return score

# calculate risks
def calculate_risk(scores):
    exp_scores = {key: math.exp(value) for key, value in scores.items()}
    denom = 1 + sum(exp_scores.values())
    risks = {key: exp_score / denom for key, exp_score in exp_scores.items()}
    return risks

# print risks
def print_risks(risks):
    for key, value in risks.items():
        print("{}: {:.0f}%".format(key.upper(), value * 100))

# main function
def main(coefficients, features):
    asa_scores = {key: calculate_asa_score(coefficients, features) for key in coefficients['intercept']}
    risks = calculate_risk(asa_scores)
    print_risks(risks)
    max_risk_key = max(risks, key=risks.get)
    print("most significant asa model: {} ({:.0f}%)".format(max_risk_key.upper(), risks[max_risk_key] * 100))

# example usage
main(coefficients, features)
