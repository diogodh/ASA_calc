import math


Age = 30
bmi = 31
DMNonInsulinMed = 1
DypsneaExert = 1
copd = 1
htnmed = 1
RenalFail = 1
Male = 1 
Smoke = 1

Bleeding = 0
DMInsulin = 0
Dialysis = 0
Dissem_cancer = 0
DypsneaRest = 0 
PartialDep = 0
FullDep = 0
chf = 0
sirs = 0
Sepsis = 0
SepShock = 0
Asian = 0
Black = 0
Hisp = 0
Other_race = 0
Unknown_race = 0
Steriod = 0
Transfusion = 0
Ventilator = 0
Open_wound_infect = 0
Weight_loss = 0
Ascites = 0

asa2 = -3.24351831113285 + (Age * 0.0497993850335345) + (Ascites * 1.51797138812861) + (Bleeding * 1.17418453645172) + (bmi * 0.0884386364902865) + (DMInsulin * 2.27518467134173) + (DMNonInsulinMed * 1.72074309477173) + (Dialysis * 9.2428669797984) + (Dissem_cancer * 2.21496632424592) + (DypsneaExert * 0.879072990128699) + (DypsneaRest * 0.74865913121185) + (PartialDep * 1.47354081204275) + (FullDep * 9.38888111430853) + (chf * 0.182975421162722) + (copd * 1.61737020813774) + (htnmed * 2.45356319429656) + (sirs * 0.491545532218731) + (Sepsis * 0.723575023319239) + (SepShock * -8.82611893338179) + (Asian * -0.318803652840306) + (Black * -0.0810928588581289) + (Hisp * -0.221275223784211) + (Other_race * -0.08277715695164) + (Unknown_race * -0.747166691899994) + (RenalFail * 0.76002624838999) + (Male * -0.503406543681855) + (Smoke * 1.29123631147632) + (Steriod * 2.27223880532616) + (Transfusion * 1.24167149658114) + (Ventilator * 0.465436345926141) + (Open_wound_infect * 0.444602266409906) + (Weight_loss * 1.53567146257999)
asa3 = -8.81611015024614 + (Age * 0.0887900821192252) + (Ascites * 2.37140129721831) + (Bleeding * 2.59967997874157) + (bmi * 0.162320037925795) + (DMInsulin * 3.77362614842436) + (DMNonInsulinMed * 2.46114747451174) + (Dialysis * 6.41828547432435) + (Dissem_cancer * 3.68543364904125) + (DypsneaExert * 1.71327881147886) + (DypsneaRest * 1.71833560678456) + (PartialDep * 2.63664553966606) + (FullDep * 12.3858665516951) + (chf * 2.10495927136399) + (copd * 3.06139282713194) + (htnmed * 3.08198135894838) + (sirs * 0.804282970648836) + (Sepsis * 0.958064998788846) + (SepShock * -3.2229106168553) + (Asian * -0.533453481364095) + (Black * 0.0138730751472354) + (Hisp * -0.309478451542563) + (Other_race * 0.0318240176047917) + (Unknown_race * -1.09683175003938) + (RenalFail * 2.29605765188033) + (Male * -0.332361244418369) + (Smoke * 1.80075235287704) + (Steriod * 3.23260333396562) + (Transfusion * 2.10457246760009) + (Ventilator * 1.6507592539009) + (Open_wound_infect * 1.2722325796638) + (Weight_loss * 2.6311769776807)
asa4 = -13.9542686674263 + (Age * 0.113640039476673) + (Ascites * 3.08927465242668) + (Bleeding * 3.23975652348996) + (bmi * 0.159418297492223) + (DMInsulin * 4.35763150530437) + (DMNonInsulinMed * 2.58147786059758) + (Dialysis * 8.53461931969202) + (Dissem_cancer * 3.97845701666912) + (DypsneaExert * 2.36863119520404) + (DypsneaRest * 2.73500348220787) + (PartialDep * 3.19397136180891) + (FullDep * 13.687069734634) + (chf * 3.3625262596574) + (copd * 3.7439295098463) + (htnmed * 3.44548888192323) + (sirs * 1.08580901808062) + (Sepsis * 1.41488334723383) + (SepShock * -2.17321141919362) + (Asian * -1.00588149705396) + (Black * 0.0759400261726127) + (Hisp * -0.266678911378697) + (Other_race * -0.32690162035079) + (Unknown_race * -0.965137117213889) + (RenalFail * 2.93133637315272) + (Male * 0.147728559435881) + (Smoke * 2.08515237349285) + (Steriod * 3.49926215775259) + (Transfusion * 2.93392252563445) + (Ventilator * 2.4063879264187) + (Open_wound_infect * 1.84069552523472) + (Weight_loss * 2.74604881740667)


denom = 1 + (math.exp(asa4) + math.exp(asa3) + math.exp(asa2)) / 100

risk1 = 1 / denom
risk2 = math.exp(asa2) / denom
risk3 = math.exp(asa3) / denom
risk4 = math.exp(asa4) / denom

print("\nRisk 1: {:.0f}%".format(risk1))
print("Risk 2: {:.0f}%".format(risk2))
print("Risk 3: {:.0f}%".format(risk3))
print("Risk 4: {:.0f}%".format(risk4))

max_percent = max(risk1, risk2, risk3, risk4)

if max_percent == risk1:
    print("\nASA1: {:.0f}%\n".format(max_percent))
elif max_percent == risk2:
    print("\nASA2: {:.0f}%\n".format(max_percent))
elif max_percent == risk4:
    print("\nASA3: {:.0f}%\n".format(max_percent))
else:
    print("\nASA4: {:.0f}%\n".format(max_percent))