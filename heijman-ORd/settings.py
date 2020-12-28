#simulation settings module

applyVoltageClamp   = 0
vcRate              = -100
runSignalingPathway = 1
runElectrophysiol   = 1
APDRepLevel         = 0.95
showProgress        = 1
bcl                 = 1000
freq                = 10
LastBCL             = freq
storeLast           = 'NaN'
K_o                 = 5.4
Ca_o                = 1.8
Na_o                = 140
Cl_o                = 100
Istim               = -80
stimdur             = 0.5

IKsNPParams         = [7.3990e-003, 3.1196e-002, 8.0019e-001, 5.6992e-003, 4.1520e-002, 
                       1.3489e+000, 3.8839e-001, -1.5019e-001, 6.0693e-001, 9.0654e-002, 
                      -1.1157e-001, 2.8330e-002, 3.1124e-003, -5.1660e-002, 1.5522e+000, 
                       2.7304e-004, 4.4198e-004, -1.2022e+000, 4.0173e-004, 2.0873e-004, 1.9561e-001]
IKsPParams          = [9.9415e-003, 4.4809e-002, 5.8172e-001, 3.3201e-003, 9.4217e-002,
                       9.5364e-001, 5.6356e-001, -1.7986e-001, 5.8381e-001, 6.5700e-002,
                       -1.1899e-001, 1.2406e-002, 3.8525e-004, -6.4118e-002, 7.7992e-001,
                       4.6171e-003, 2.3730e-004, -1.9742e+000, 2.4689e-004, 1.9561e-001]
LCCNPParams         = [        0.59,        0.8,        0.052,          13,         0.132, ]
LCCPParams          = [        0.59,        0.8,        0.052,          13,         0.132, ]
INaNPParams         = [2.15 * 8.25 * 1.1,   0.13,   10.66 + 16.7434, -11.1,         0.3, 
                        ]

    RyRP_Amp            = 1.9925
    RyRP_Tau            = 0.5357
    TauTr               = 75
    observeICaLSS       = 0

    ICaLB               = 0.0
    IKsB                = 0.0
    IKrB                = 0.0
    INaKB               = 0.0
    INaCaB              = 0.0
    IKpB                = 0.0
    IK1B                = 0.0
    INabB               = 0.0
    ITo1B               = 0.0
    ITo2B               = 0.0
    INaB                = 0.0
    INaLB               = 0.0
    IClB                = 0.0
    IpCaB               = 0.0
    CTKClB              = 0.0
    CTNaClB             = 0.0
    ICabB               = 0.0
    IrelB               = 0.0
    IupB                = 0.0
    ItrB                = 0.0
    IleakB              = 0.0
    IdiffB              = 0.0
    CAMKIIB             = 0.0


    return settings 