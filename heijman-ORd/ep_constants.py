# electrophysiology contants

F                               = 96487
R                               = 8314
T                               = 310

l                               = 0.01
a                               = 0.0011

vcell                           = 1000 * 3.14 * a * a * l
ageo                            = 2 * 3.14 * a * a + 2 * pi * a * l
Acap                            = ageo * 2


vmyo                            = vcell * 0.678
vsr                             = vcell * 0.06
vnsr                            = vcell * 0.0552
vjsr                            = vcell * 0.0048
vss                             = vcell * 0.02
vssCaL                          = vcell * 0.002

AF                              = Acap / F
frt                             = F / T / R
RTF                             = 1.0 / frt 



''' ============================ sodium ========================== '''

GNa                             = 9.075
GNaL                            = 65e-4

KmCa                            = 1.25e-4
NCXmax                          = 4.5
ksat                            = 0.32
eta                             = 0.27

KmNai                           = 12.3
KmNao                           = 87.5
KmCai                           = 0.0036
KmCao                           = 1.3



''' =========================== calcium ========================= '''

ibarpca                         = 0.0575
kmpca                           = 5e-4
gcab                            = 1.995084e-7
k_JSR_Leak                      = 1.75e-04
k_JSR_Leak_P                    = 1.1

cmdnbar                         = 0.050 #buffer constants
trpnbar                         = 5.0e-04
kmcmdn                          = 0.00238
kmtrpn                          = 0.0005
kmcsqn                          = 0.8
csqnbar                         = 10
BSRmax                          = 0.047
KmBSR                           = 0.00087
BSLmax                          = 1.124
KmBSL                           = 0.00087

KmCaMK                          = 0.25
iupmax                          = 0.004375
Kmup                            = 0.00092
nsrmax                          = 15.0

dKmPLBCAMK                      = 0.00017
dKmPLBPKA                       = 0.46 * Kmup 
dKmPLBBoth                      = dKmPLBPKA
dJupmax                         = 0.75


CaMK0                           = 0.05 #CAMKII signaling
Km                              = 1.5e-3
betaCamK                        = 6.8e-4
alphaCamK                       = 0.05

tau_PLB_CaMKII                  = 100000
tau_RyR_CaMKII                  = 10000


''' =========================== potassium =========================== '''

GK1max                          = 0.5
GKpmax                          = 3.84e-03  #2.76e-3
GKrmax                          = 0.0138542
prnak                           = 0.01833 
kmnai_NP                        = 2.6
kmnai_P                         = 1.846
kmko                            = 1.5
ibarnak                         = 1.4

gitodv                          = 0.4975



''' =========================== chloride ============================ '''

Kmto2                           = 0.1502
PCl                             = 9e-7
GClb                            = 2.25e-4

CTKClmax                        = 1.77e-5
CTNaClmax                       = 2.46108e-5





