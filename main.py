import math


age = 30
bmi = 31
dmnoninsulinmed = 1
dypsneaexert = 1
copd = 1
htnmed = 1
renalfail = 1
male = 1 
smoke = 1

bleeding = 0
dminsulin = 0
dialysis = 0
dissem_cancer = 0
dypsnearest = 0 
partialdep = 0
fulldep = 0
chf = 0
sirs = 0
sepsis = 0
sepshock = 0
asian = 0
black = 0
hisp = 0
other_race = 0
unknown_race = 0
steriod = 0
transfusion = 0
ventilator = 0
open_wound_infect = 0
weight_loss = 0
ascites = 0

asa2 = -3.24351831113285 + (age * 0.0497993850335345) + (ascites * 1.51797138812861) + (bleeding * 1.17418453645172) + (bmi * 0.0884386364902865) + (dminsulin * 2.27518467134173) + (dmnoninsulinmed * 1.72074309477173) + (dialysis * 9.2428669797984) + (dissem_cancer * 2.21496632424592) + (dypsneaexert * 0.879072990128699) + (dypsnearest * 0.74865913121185) + (partialdep * 1.47354081204275) + (fulldep * 9.38888111430853) + (chf * 0.182975421162722) + (copd * 1.61737020813774) + (htnmed * 2.45356319429656) + (sirs * 0.491545532218731) + (sepsis * 0.723575023319239) + (sepshock * -8.82611893338179) + (asian * -0.318803652840306) + (black * -0.0810928588581289) + (hisp * -0.221275223784211) + (other_race * -0.08277715695164) + (unknown_race * -0.747166691899994) + (renalfail * 0.76002624838999) + (male * -0.503406543681855) + (smoke * 1.29123631147632) + (steriod * 2.27223880532616) + (transfusion * 1.24167149658114) + (ventilator * 0.465436345926141) + (open_wound_infect * 0.444602266409906) + (weight_loss * 1.53567146257999)
asa3 = -8.81611015024614 + (age * 0.0887900821192252) + (ascites * 2.37140129721831) + (bleeding * 2.59967997874157) + (bmi * 0.162320037925795) + (dminsulin * 3.77362614842436) + (dmnoninsulinmed * 2.46114747451174) + (dialysis * 6.41828547432435) + (dissem_cancer * 3.68543364904125) + (dypsneaexert * 1.71327881147886) + (dypsnearest * 1.71833560678456) + (partialdep * 2.63664553966606) + (fulldep * 12.3858665516951) + (chf * 2.10495927136399) + (copd * 3.06139282713194) + (htnmed * 3.08198135894838) + (sirs * 0.804282970648836) + (sepsis * 0.958064998788846) + (sepshock * -3.2229106168553) + (asian * -0.533453481364095) + (black * 0.0138730751472354) + (hisp * -0.309478451542563) + (other_race * 0.0318240176047917) + (unknown_race * -1.09683175003938) + (renalfail * 2.29605765188033) + (male * -0.332361244418369) + (smoke * 1.80075235287704) + (steriod * 3.23260333396562) + (transfusion * 2.10457246760009) + (ventilator * 1.6507592539009) + (open_wound_infect * 1.2722325796638) + (weight_loss * 2.6311769776807)
asa4 = -13.9542686674263 + (age * 0.113640039476673) + (ascites * 3.08927465242668) + (bleeding * 3.23975652348996) + (bmi * 0.159418297492223) + (dminsulin * 4.35763150530437) + (dmnoninsulinmed * 2.58147786059758) + (dialysis * 8.53461931969202) + (dissem_cancer * 3.97845701666912) + (dypsneaexert * 2.36863119520404) + (dypsnearest * 2.73500348220787) + (partialdep * 3.19397136180891) + (fulldep * 13.687069734634) + (chf * 3.3625262596574) + (copd * 3.7439295098463) + (htnmed * 3.44548888192323) + (sirs * 1.08580901808062) + (sepsis * 1.41488334723383) + (sepshock * -2.17321141919362) + (asian * -1.00588149705396) + (black * 0.0759400261726127) + (hisp * -0.266678911378697) + (other_race * -0.32690162035079) + (unknown_race * -0.965137117213889) + (renalfail * 2.93133637315272) + (male * 0.147728559435881) + (smoke * 2.08515237349285) + (steriod * 3.49926215775259) + (transfusion * 2.93392252563445) + (ventilator * 2.4063879264187) + (open_wound_infect * 1.84069552523472) + (weight_loss * 2.74604881740667)


denom = 1 + (math.exp(asa4) + math.exp(asa3) + math.exp(asa2)) / 100

risk1 = 1 / denom
risk2 = math.exp(asa2) / denom
risk3 = math.exp(asa3) / denom
risk4 = math.exp(asa4) / denom

print("\nrisk 1: {:.0f}%".format(risk1))
print("risk 2: {:.0f}%".format(risk2))
print("risk 3: {:.0f}%".format(risk3))
print("risk 4: {:.0f}%".format(risk4))

max_percent = max(risk1, risk2, risk3, risk4)

if max_percent == risk1:
    print("\nasa1: {:.0f}%\n".format(max_percent))
elif max_percent == risk2:
    print("\nasa2: {:.0f}%\n".format(max_percent))
elif max_percent == risk4:
    print("\nasa3: {:.0f}%\n".format(max_percent))
else:
    print("\nasa4: {:.0f}%\n".format(max_percent))