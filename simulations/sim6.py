from .simulation import *
from router import *
from secure_router import *
from simple_blockchain import Blockchain
import sys
import io


def sim6():
    """
    Simulation 5:
    """

    # North & Latin America
    NAS1_config = ('localhost', 1, 5001)
    NAS2_config = ('localhost', 2, 5002)
    NAS3_config = ('localhost', 3, 5003)
    NAS4_config = ('localhost', 4, 5004)
    NAS5_config = ('localhost', 5, 5005)
    NAS6_config = ('localhost', 6, 5006)
    NAS7_config = ('localhost', 7, 5007)
    NAS8_config = ('localhost', 8, 5008)
    NAS9_config = ('localhost', 9, 5009)
    NAS10_config = ('localhost', 10, 5010)
    NAS11_config = ('localhost', 11, 5011)
    NAS12_config = ('localhost', 12, 5012)
    NAS13_config = ('localhost', 13, 5013)
    NAS14_config = ('localhost', 14, 5014)
    NAS15_config = ('localhost', 15, 5015)
    NAS16_config = ('localhost', 16, 5016)
    NAS17_config = ('localhost', 17, 5017)
    NAS18_config = ('localhost', 18, 5018)
    NAS19_config = ('localhost', 19, 5019)
    NAS20_config = ('localhost', 20, 5020)
    NAS21_config = ('localhost', 21, 5021)

    # South America
    SAS1_config = ('localhost', 101, 5101)
    SAS2_config = ('localhost', 102, 5102)
    SAS3_config = ('localhost', 103, 5103)
    SAS4_config = ('localhost', 104, 5104)
    SAS5_config = ('localhost', 105, 5105)
    SAS6_config = ('localhost', 106, 5106)
    SAS7_config = ('localhost', 107, 5107)

    # Africa
    FAS1_config = ('localhost', 201, 5201)
    FAS2_config = ('localhost', 202, 5202)
    FAS3_config = ('localhost', 203, 5203)
    FAS4_config = ('localhost', 204, 5204)
    FAS5_config = ('localhost', 205, 5205)
    FAS6_config = ('localhost', 206, 5206)
    FAS7_config = ('localhost', 207, 5207)
    FAS8_config = ('localhost', 208, 5208)
    FAS9_config = ('localhost', 209, 5209)
    FAS10_config = ('localhost', 210, 5210)
    FAS11_config = ('localhost', 211, 52011)
    FAS12_config = ('localhost', 212, 52012)
    FAS13_config = ('localhost', 213, 52013)
    FAS14_config = ('localhost', 214, 52014)
    FAS15_config = ('localhost', 215, 52015)

    # Europe
    EAS1_config = ('localhost', 301, 5301)
    EAS2_config = ('localhost', 302, 5302)
    EAS3_config = ('localhost', 303, 5303)
    EAS4_config = ('localhost', 304, 5304)
    EAS5_config = ('localhost', 305, 5305)
    EAS6_config = ('localhost', 306, 5306)
    EAS7_config = ('localhost', 307, 5307)
    EAS8_config = ('localhost', 308, 5308)
    EAS9_config = ('localhost', 309, 5309)
    EAS10_config = ('localhost', 310, 5310)
    EAS11_config = ('localhost', 311, 5311)
    EAS12_config = ('localhost', 312, 5312)
    EAS13_config = ('localhost', 313, 5313)
    EAS14_config = ('localhost', 314, 5314)
    EAS15_config = ('localhost', 315, 5315)
    
    # Middle East
    MAS1_config = ('localhost', 401, 5401)
    MAS2_config = ('localhost', 402, 5402)
    MAS3_config = ('localhost', 403, 5403)
    MAS4_config = ('localhost', 404, 5404)

    # Russia
    RAS1_config = ('localhost', 501, 5501)
    RAS2_config = ('localhost', 502, 5502)
    RAS3_config = ('localhost', 503, 5503)
    RAS4_config = ('localhost', 504, 5504)
    RAS5_config = ('localhost', 505, 5505)
    RAS6_config = ('localhost', 506, 5506)
    RAS7_config = ('localhost', 507, 5507)
    RAS8_config = ('localhost', 508, 5508)

    # China
    CAS1_config = ('localhost', 601, 5601)
    CAS2_config = ('localhost', 602, 5602)
    CAS3_config = ('localhost', 603, 5603)
    CAS4_config = ('localhost', 604, 5604)

    # Pacific
    PAS1_config = ('localhost', 701, 5701)
    PAS2_config = ('localhost', 702, 5702)
    PAS3_config = ('localhost', 703, 5703)
    PAS4_config = ('localhost', 704, 5704)
    PAS5_config = ('localhost', 705, 5705)
    PAS6_config = ('localhost', 706, 5706)
    PAS7_config = ('localhost', 707, 5707)
    PAS8_config = ('localhost', 708, 5708)
    PAS9_config = ('localhost', 709, 5709)
    PAS10_config = ('localhost', 710, 5710)
    PAS11_config = ('localhost', 711, 5711)
    PAS12_config = ('localhost', 712, 5712)
    PAS13_config = ('localhost', 713, 5713)
    PAS14_config = ('localhost', 714, 5714)
    PAS15_config = ('localhost', 715, 5715)
    PAS16_config = ('localhost', 716, 5716)
    PAS17_config = ('localhost', 717, 57017)

    blockchain = Blockchain()
    
    # North & Latin America
    NAS1 = SecureEBGP(*NAS1_config, blockchain)
    NAS2 = EBGPRouter(*NAS2_config)
    NAS3 = SecureEBGP(*NAS3_config, blockchain)
    NAS4 = EBGPRouter(*NAS4_config)
    NAS5 = SecureEBGP(*NAS5_config, blockchain)
    NAS6 = SecureEBGP(*NAS6_config, blockchain)
    NAS7 = EBGPRouter(*NAS7_config)
    NAS8 = SecureEBGP(*NAS8_config, blockchain)
    NAS9 = EBGPRouter(*NAS9_config)
    NAS10 = SecureEBGP(*NAS10_config, blockchain)
    NAS11 = SecureEBGP(*NAS11_config, blockchain)
    NAS12 = EBGPRouter(*NAS12_config)
    NAS13 = SecureEBGP(*NAS13_config, blockchain)
    NAS14 = EBGPRouter(*NAS14_config)
    NAS15 = EBGPRouter(*NAS15_config)
    NAS16 = EBGPRouter(*NAS16_config)
    NAS17 = SecureEBGP(*NAS17_config, blockchain)
    NAS18 = SecureEBGP(*NAS18_config, blockchain)
    NAS19 = SecureEBGP(*NAS19_config, blockchain)
    NAS20 = EBGPRouter(*NAS20_config)
    NAS21 = SecureEBGP(*NAS21_config, blockchain)
    
    # South America
    SAS1 = EBGPRouter(*SAS1_config)
    SAS2 = SecureEBGP(*SAS2_config, blockchain)
    SAS3 = SecureEBGP(*SAS3_config, blockchain)
    SAS4 = EBGPRouter(*SAS4_config)
    SAS5 = EBGPRouter(*SAS5_config)
    SAS6 = SecureEBGP(*SAS6_config, blockchain)
    SAS7 = EBGPRouter(*SAS7_config)

    # Africa
    FAS1 = SecureEBGP(*FAS1_config, blockchain)
    FAS2 = EBGPRouter(*FAS2_config)
    FAS3 = EBGPRouter(*FAS3_config)
    FAS4 = SecureEBGP(*FAS4_config, blockchain)
    FAS5 = SecureEBGP(*FAS5_config, blockchain)
    FAS6 = EBGPRouter(*FAS6_config)
    FAS7 = SecureEBGP(*FAS7_config, blockchain)
    FAS8 = SecureEBGP(*FAS8_config, blockchain)
    FAS9 = EBGPRouter(*FAS9_config)
    FAS10 = EBGPRouter(*FAS10_config)
    FAS11 = EBGPRouter(*FAS11_config)
    FAS12 = SecureEBGP(*FAS12_config, blockchain)
    FAS13 = EBGPRouter(*FAS13_config)
    FAS14 = EBGPRouter(*FAS14_config)
    FAS15 = SecureEBGP(*FAS15_config, blockchain)

    # Europe
    EAS1 = SecureEBGP(*EAS1_config, blockchain)
    EAS2 = EBGPRouter(*EAS2_config)
    EAS3 = SecureEBGP(*EAS3_config, blockchain)
    EAS4 = EBGPRouter(*EAS4_config)
    EAS5 = EBGPRouter(*EAS5_config)
    EAS6 = SecureEBGP(*EAS6_config, blockchain)
    EAS7 = SecureEBGP(*EAS7_config, blockchain)
    EAS8 = EBGPRouter(*EAS8_config)
    EAS9 = EBGPRouter(*EAS9_config)
    EAS10 = SecureEBGP(*EAS10_config, blockchain)
    EAS11 = EBGPRouter(*EAS11_config)
    EAS12 = EBGPRouter(*EAS12_config)
    EAS13 = EBGPRouter(*EAS13_config)
    EAS14 = EBGPRouter(*EAS14_config)
    EAS15 = EBGPRouter(*EAS15_config)

    # Middle East
    MAS1 = SecureEBGP(*MAS1_config, blockchain)
    MAS2 = SecureEBGP(*MAS2_config, blockchain)
    MAS3 = EBGPRouter(*MAS3_config)
    MAS4 = EBGPRouter(*MAS4_config)

    # Russia
    RAS1 = SecureEBGP(*RAS1_config, blockchain)
    RAS2 = SecureEBGP(*RAS2_config, blockchain)
    RAS3 = EBGPRouter(*RAS3_config)
    RAS4 = EBGPRouter(*RAS4_config)
    RAS5 = EBGPRouter(*RAS5_config)
    RAS6 = SecureEBGP(*RAS6_config, blockchain)
    RAS7 = EBGPRouter(*RAS7_config)
    RAS8 = SecureEBGP(*RAS8_config, blockchain)

    # China
    CAS1 = SecureEBGP(*CAS1_config, blockchain)
    CAS2 = SecureEBGP(*CAS2_config, blockchain)
    CAS3 = EBGPRouter(*CAS3_config)
    CAS4 = SecureEBGP(*CAS4_config, blockchain)

    # Pacific
    PAS1 = SecureEBGP(*PAS1_config, blockchain)
    PAS2 = SecureEBGP(*PAS2_config, blockchain)
    PAS3 = SecureEBGP(*PAS3_config, blockchain)
    PAS4 = EBGPRouter(*PAS4_config)
    PAS5 = SecureEBGP(*PAS5_config, blockchain)
    PAS6 = SecureEBGP(*PAS6_config, blockchain)
    PAS7 = SecureEBGP(*PAS7_config, blockchain)
    PAS8 = SecureEBGP(*PAS8_config, blockchain)
    PAS9 = SecureEBGP(*PAS9_config, blockchain)
    PAS10 = SecureEBGP(*PAS10_config, blockchain)
    PAS11 = SecureEBGP(*PAS11_config, blockchain)
    PAS12 = EBGPRouter(*PAS12_config)
    PAS13 = SecureEBGP(*PAS13_config, blockchain)
    PAS14 = EBGPRouter(*PAS14_config)
    PAS15 = EBGPRouter(*PAS15_config)
    PAS16 = SecureEBGP(*PAS16_config, blockchain)
    PAS17 = SecureEBGP(*PAS17_config, blockchain)

    # North & Latin America
    NAS1.add_neighbors([NAS2_config, NAS8_config, NAS17_config])
    NAS2.add_neighbors([NAS1_config, NAS3_config, NAS8_config])
    NAS3.add_neighbors([NAS2_config, NAS4_config, NAS9_config])
    NAS4.add_neighbors([NAS3_config, NAS5_config, NAS10_config, NAS11_config])
    NAS5.add_neighbors([NAS4_config, NAS6_config, NAS11_config, NAS12_config, NAS13_config])
    NAS6.add_neighbors([NAS5_config, NAS7_config, NAS13_config])
    NAS7.add_neighbors([NAS6_config, EAS3_config])
    NAS8.add_neighbors([NAS1_config, NAS2_config, NAS9_config, NAS10_config, NAS14_config, PAS9_config])
    NAS9.add_neighbors([NAS3_config, NAS8_config, NAS10_config])
    NAS10.add_neighbors([NAS4_config, NAS8_config, NAS9_config, NAS11_config, NAS14_config, NAS15_config, NAS16_config])
    NAS11.add_neighbors([NAS4_config, NAS5_config, NAS10_config])
    NAS12.add_neighbors([NAS5_config, NAS13_config, NAS16_config])
    NAS13.add_neighbors([NAS5_config, NAS6_config, NAS12_config, NAS18_config, SAS1_config, FAS1_config, FAS5_config, EAS3_config])
    NAS14.add_neighbors([NAS8_config, NAS10_config, NAS15_config, NAS17_config])
    NAS15.add_neighbors([NAS10_config, NAS14_config, NAS17_config])
    NAS16.add_neighbors([NAS10_config, NAS12_config, NAS18_config])
    NAS17.add_neighbors([NAS1_config, NAS14_config, NAS15_config, NAS18_config, NAS19_config, PAS8_config])
    NAS18.add_neighbors([NAS13_config, NAS16_config, NAS17_config, NAS21_config])
    NAS19.add_neighbors([NAS17_config, NAS20_config])
    NAS20.add_neighbors([NAS19_config, NAS21_config])
    NAS21.add_neighbors([NAS18_config, NAS20_config, SAS2_config])

    # South America
    SAS1.add_neighbors([NAS13_config])
    SAS2.add_neighbors([SAS3_config, SAS4_config, NAS21_config])
    SAS3.add_neighbors([SAS2_config, SAS5_config, FAS5_config])
    SAS4.add_neighbors([SAS2_config, SAS6_config])
    SAS5.add_neighbors([SAS3_config, SAS6_config])
    SAS6.add_neighbors([SAS4_config, SAS5_config, SAS7_config])
    SAS7.add_neighbors([SAS6_config])

    # Africa
    FAS1.add_neighbors([FAS5_config, NAS13_config, EAS12_config])
    FAS2.add_neighbors([FAS7_config])
    FAS3.add_neighbors([FAS4_config, FAS7_config])
    FAS4.add_neighbors([FAS3_config, FAS8_config, MAS2_config]) 
    FAS5.add_neighbors([FAS1_config, FAS6_config, FAS9_config, NAS13_config, SAS3_config])
    FAS6.add_neighbors([FAS5_config, FAS7_config])
    FAS7.add_neighbors([FAS2_config, FAS3_config, FAS6_config, FAS8_config, FAS9_config, FAS12_config])
    FAS8.add_neighbors([FAS4_config, FAS7_config, FAS10_config, FAS13_config, PAS1_config])
    FAS9.add_neighbors([FAS7_config])
    FAS10.add_neighbors([FAS8_config, FAS12_config])
    FAS11.add_neighbors([FAS12_config])
    FAS12.add_neighbors([FAS7_config, FAS10_config, FAS11_config, FAS13_config, FAS14_config, FAS15_config])
    FAS13.add_neighbors([FAS8_config, FAS12_config])
    FAS14.add_neighbors([FAS12_config, FAS15_config])
    FAS15.add_neighbors([FAS12_config, FAS14_config])

    # Europe
    EAS1.add_neighbors([EAS2_config, EAS5_config, EAS6_config, RAS1_config])
    EAS2.add_neighbors([EAS1_config, EAS3_config, EAS8_config]) 
    EAS3.add_neighbors([EAS2_config, EAS4_config, EAS12_config, NAS7_config, NAS13_config]) 
    EAS4.add_neighbors([EAS3_config, EAS7_config, EAS8_config])
    EAS5.add_neighbors([EAS1_config, EAS6_config, EAS8_config, EAS11_config])
    EAS6.add_neighbors([EAS1_config, EAS5_config, EAS9_config, EAS10_config, RAS1_config])
    EAS7.add_neighbors([EAS4_config, EAS8_config, EAS12_config, EAS13_config])
    EAS8.add_neighbors([EAS2_config, EAS4_config, EAS5_config, EAS7_config, EAS11_config])
    EAS9.add_neighbors([EAS6_config, EAS10_config, EAS11_config])
    EAS10.add_neighbors([EAS6_config, EAS9_config, EAS14_config, MAS1_config, RAS1_config, RAS2_config])
    EAS11.add_neighbors([EAS5_config, EAS8_config, EAS9_config, EAS13_config, EAS14_config, EAS15_config])
    EAS12.add_neighbors([EAS3_config, EAS7_config, FAS1_config])
    EAS13.add_neighbors([EAS7_config, EAS11_config])
    EAS14.add_neighbors([EAS10_config, EAS11_config])
    EAS15.add_neighbors([EAS11_config])

    # Middle East
    MAS1.add_neighbors([MAS2_config, EAS10_config, RAS2_config])
    MAS2.add_neighbors([MAS1_config, MAS3_config, FAS4_config])
    MAS3.add_neighbors([MAS2_config, MAS4_config, PAS1_config])
    MAS4.add_neighbors([MAS3_config])
    
    # Russia
    RAS1.add_neighbors([RAS2_config, RAS3_config, EAS1_config, EAS6_config, EAS10_config])
    RAS2.add_neighbors([RAS3_config, EAS10_config, MAS1_config])
    RAS3.add_neighbors([RAS1_config, RAS2_config, RAS5_config])
    RAS4.add_neighbors([RAS5_config])
    RAS5.add_neighbors([RAS3_config, RAS4_config, RAS7_config])
    RAS6.add_neighbors([RAS7_config, CAS1_config])
    RAS7.add_neighbors([RAS5_config, RAS6_config, RAS8_config])
    RAS8.add_neighbors([RAS7_config])

    # China
    CAS1.add_neighbors([CAS3_config, CAS4_config, RAS6_config])
    CAS2.add_neighbors([CAS4_config, PAS1_config, PAS3_config])
    CAS3.add_neighbors([CAS1_config, CAS4_config])
    CAS4.add_neighbors([CAS1_config, CAS2_config, CAS3_config, PAS8_config])

    # Pacific
    PAS1.add_neighbors([PAS2_config, FAS8_config, MAS3_config, CAS2_config])
    PAS2.add_neighbors([PAS1_config, PAS3_config])
    PAS3.add_neighbors([PAS2_config, PAS4_config, PAS5_config, PAS8_config, CAS2_config])
    PAS4.add_neighbors([PAS3_config])
    PAS5.add_neighbors([PAS3_config, PAS6_config])
    PAS6.add_neighbors([PAS5_config, PAS7_config, PAS11_config, PAS13_config])
    PAS7.add_neighbors([PAS6_config, PAS8_config])
    PAS8.add_neighbors([PAS3_config, PAS7_config, PAS9_config, CAS4_config, NAS17_config])
    PAS9.add_neighbors([PAS8_config, PAS10_config, NAS8_config])
    PAS10.add_neighbors([PAS9_config])
    PAS11.add_neighbors([PAS6_config, PAS12_config, PAS15_config])
    PAS12.add_neighbors([PAS11_config, PAS13_config])
    PAS13.add_neighbors([PAS6_config, PAS12_config, PAS14_config, PAS15_config, PAS16_config])
    PAS14.add_neighbors([PAS13_config, PAS16_config])
    PAS15.add_neighbors([PAS11_config, PAS13_config, PAS16_config])
    PAS16.add_neighbors([PAS13_config, PAS14_config, PAS15_config, PAS17_config])
    PAS17.add_neighbors([PAS16_config])

    for AS in [NAS1, NAS2, NAS3, NAS4, NAS5, NAS6, NAS7, NAS8, NAS9, NAS10, NAS11, NAS12, NAS13, NAS14, NAS15, NAS16, NAS17, NAS18, NAS19, NAS20, NAS21]: AS.start()
    for AS in [SAS1, SAS2, SAS3, SAS4, SAS5, SAS6, SAS7]: AS.start()
    for AS in [FAS1, FAS2, FAS3, FAS4, FAS5, FAS6, FAS7, FAS8, FAS9, FAS10, FAS11, FAS12, FAS13, FAS14, FAS15]: AS.start()
    for AS in [EAS1, EAS2, EAS3, EAS4, EAS5, EAS6, EAS7, EAS8, EAS9, EAS10, EAS11, EAS12, EAS13, EAS14, EAS15]: AS.start()
    for AS in [MAS1, MAS2, MAS3, MAS4]: AS.start()
    for AS in [RAS1, RAS2, RAS3, RAS4, RAS5, RAS6, RAS7, RAS8]: AS.start()


    print('this might take a while ...')
    # Suppress print statements
    sys.stdout = io.StringIO()

    NAS10.advertise_route("1.1.0.0/24")
    SAS6.advertise_route("100.100.1.1/24")
    FAS12.advertise_route("200.200.2.2/24")
    EAS8.advertise_route("300.300.3.3/24")
    MAS2.advertise_route("400.400.4.4/24")
    RAS5.advertise_route("500.500.5.5/24")
    CAS3.advertise_route("600.600.6.6/24")
    PAS6.advertise_route("700.700.7.7/24")
    
    # Reset sys.stdout to its original value (optional)
    sys.stdout = sys.__stdout__

    print('Simulation ended. Press control + c to end this process.')


Simulation().add(fun=sim6, num_id=6)