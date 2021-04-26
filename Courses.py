import csv
import pandas as pd

#Spring 2021 Data
csedata = {'CSE 101LLB - Computers A General Intro': ['Winikus'], 'CSE 111LLB - Intro To Quantitative Analysis': ['Winikus', 'Hughes'], 'CSE 115LLR - Computer Science I': ['Hertz', 'Alphonce'], 'CSE 116LLB - Computer Science Ii': ['Hartloff', 'Akhter'], 'CSE 191LR - Intro Discrete Structures': ['Akhter', 'Knepley', 'Meng'], 'CSE 220LLB - Systems Programming': ['Blanton'], 'CSE 241LLB - Digital Systems': ['Winikus'], 'CSE 250LR - Data Structures': ['Hughes'], 'CSE 305LR - Programming Languages': ['Ziarek'], 'CSE 306LLB - Software Quality In Practice': ['Alphonce'], 'CSE 312LR - Web Applications': ['Hartloff'], 'CSE 331LR - Algo And Complexity': ['Sariyuce'], 'CSE 341LR - Computer Organization': ['Ghanei'], 'CSE 370LR - Applied Hci': ['Hunt'], 'CSE 379LLB - Intro To Microproccessors': ['Schindler'], 'CSE 396LR - Intro Theory Of Computatn': ['Regan'], 'CSE 404LR - Software Project Management': ['Hunt'], 'CSE 410LEC - Special Topics-Advanced Blockchain Concepts': ['Ramamurthy'], 'CSE 410LEC - Special Topics-Computer Security': ['Blanton'], 'CSE 410LEC - Special Topics-Machine Learning And Society': ['Joseph'], 'CSE 410LEC - Special Topics-Introduction To Matlab': ['Miller'], 'CSE 410LEC - Special Topics-Iot And Cybersecurity': ['Xu'], 'CSE 410LEC - Special Topics-Computational Investment 2': ['Liu'], 'CSE 421LEC - Operating Systems': ['Ghanei'], 'CSE 431LEC - Algorithms Anal & Dsgn 1': ['Li'], 'CSE 432LEC - Randomized Algorithms': ['Hughes'], 'CSE 442LR - Software Eng Concepts': ['Hertz'], 'CSE 443LEC - Compilers': ['Alphonce'], 'CSE 446LEC - Reinforcement Learning': ['Vereshchaka'], 'CSE 453LEC - Hardware/software Integrated': ['Schindler'], 'CSE 455LEC - Intro To Pattern Recognition': ['Dong'], 'CSE 460LEC - Data Models And Query Language': ['Das Bhattacharjee'], 'CSE 462LEC - Database Systems': ['Kennedy'], 'CSE 467LEC - Computational Linguistics': ['Chaves'], 'CSE 468LEC - Robotics Algorithms': ['Ghanei'], 'CSE 473LEC - Comp Vision & Image Proc': ['Doermann'], 'CSE 474LEC - Intro Machine Learning': ['Chandola', 'Das Bhattacharjee'], 'CSE 486LEC - Distributed Systems': ['Blanton'], 'CSE 487LEC - Data Intensive Computing': ['Ramamurthy'], 'CSE 489LEC - Modern Network Concepts': ['Mi'], 'CSE 490LEC - Computer Architecture': ['Sridhar'], 'CSE 492TUT - Undergrad Peer Mentoring': ['Hunt'], 'CSE 493LLB - Intro Vlsi Electronics': ['Sridhar'], 'CSE 496TUT - Internship/practicum': ['Kennedy'], 'CSE 497TUT - Dept Honors Thesis': ['Hughes']}
easdata = {'EAS 160LAB - Engineering Machine Shop': ['Peng'], 'EAS 198SEM - Ub Seminar-The Places You Will Go': ['Zirnheld'], 'EAS 199SL - Ub Seminar-Grand Challenges For Engineeri': ['Latorre'], 'EAS 200LR - Ee Concepts For Non-Majors': ['Rivera Reyes'], 'EAS 202SEM - Impact On Society': ['Latorre'], 'EAS 207LR - Statics': ['Hajesfandiari'], 'EAS 208LR - Dynamics': ['Nightingale'], 'EAS 209LR - Mechanics Of Solids': ['Hajesfandiari'], 'EAS 230LLB - Engineering Computations': ['Hammond'], 'EAS 240LEC - Introduction To Programming': ['Mastronarde'], 'EAS 305LR - Appl Prob & Stat Infer': ['* Fadeyi'], 'EAS 345LEC - Introduction To Data Science': ['Ramamurthy'], 'EAS 346LEC - Communicating With Data': ['Schimpf'], 'EAS 360LEC - Stem Communications': ['Depowski'], 'EAS 460LEC - Special Topics-Equity And Inclusion In Engine': ['Moore'], 'EAS 494SEM - Interdisciplin Senior Design': ['Olewnik']}
dmsdata = {'DMS 103SEM - Basic Video': ['Best'], 'DMS 105SEM - Basic Documentary': ['Waham'], 'DMS 107LEC - Film & Media History 1': ['* Colleran'], 'DMS 110LEC - Programming For Digitalart': ['Sack'], 'DMS 121SEM - Basic Digital Arts': ['Dolecki'], 'DMS 122SEM - Intro To Physical Computing': ['Geistweidt'], 'DMS 201LEC - Green Media': ['Anstey'], 'DMS 211LEC - Plasma': ['* Sarlin'], 'DMS 213LEC - Immigration And Film': ['* Subramanian'], 'DMS 220LEC - Machines, Codes And Cultures': ['* Lison'], 'DMS 302SEM - Experimental Moving Image': ['Kraning'], 'DMS 321SEM - Web Development': ['Pollard'], 'DMS 333LEC - World Cinema': ['* Colleran'], 'DMS 342SEM - Intermediate Documentary Wkshp': ['Livingston'], 'DMS 343LEC - Intermediate Post-Production': ['Bouquard'], 'DMS 394LEC - Topics In Asian Cinema-Korean Drama And Film': ['Rhee'], 'DMS 406SEM - Ethnographic Media': ['Elder'], 'DMS 410LEC - Non Fiction Film': ['Elder'], 'DMS 418LEC - Special Topics-Landscape Projections': ['Kraning'], 'DMS 429LEC - Italian Cinema': ['Chiesa'], 'DMS 435SEM - Scriptwriting: All Media': ['Anstey'], 'DMS 439SEM - Virtual Worlds 2': ['Pape'], 'DMS 441SEM - Adv Video Production': ['Lee'], 'DMS 448SEM - Games, Gender And Culture': ['Mejeur'], 'DMS 462SEM - Game Design': ['Pape'], 'DMS 474SEM - Media Theories & Approaches': ['Reid'], 'DMS 480SEM - Social Media & Networks': ['Rhee'], 'DMS 496TUT - Media Arts Internship': ['Waham'], 'DMS 499TUT - Independent Study': ['Sarlin']}
chedata = {'CHE 101LR - General Chemistry': ['Liwosz'], 'CHE 102LR - General Chemistry': ['Keister'], 'CHE 106LLR - Chemistry-Prin & Applic': ['Cook'], 'CHE 107LR - Gen Chem For Engineers I': ['Liwosz'], 'CHE 108LR - Gen Chem For Engineers Ii': ['Keister'], 'CHE 110DIS - Prob Solving Gen Chem 1': ['Clizbe'], 'CHE 202LLR - Organic Chemistry Ii': ['Davison'], 'CHE 204LEC - Organic Chem Lec Only': ['Gong'], 'CHE 214LEC - Analytical Chemistry': ['Gardella'], 'CHE 215LAB - Analytical Chemistry Lab': ['* Aga'], 'CHE 252LLR - Contemp Organic Chemistry': ['Rohde'], 'CHE 290LAB - Undergrad Research': ['Zurek'], 'CHE 312LEC - Chem Of Bio Systems': ['Atilla-Gokcumen'], 'CHE 320LEC - Physical Chemistry Lec': ['Autschbach'], 'CHE 322LLB - Inorganic Chemistry Ii': ['Morrow    * Gong'], 'CHE 330LAB - Physical Chemistry Lab': ['* Zurek'], 'CHE 376LLB - Intro Chemical Literature': ['Clarke'], 'CHE 414LAB - Instrumental Analysis': ['* Aga    * Aga'], 'CHE 455LEC - Advanced Organic Chem': ['Murkin'], 'CHE 458LEC - Physical Chemistry 2': ['Prasad'], 'CHE 476LEC - Intro To Polymers': ['Rzayev'], 'CHE 498TUT - Senior Research': ['Gong']}


# prof = pd.DataFrame([['CSE111', 'Winikus', ' ',' ',' ','','','']], columns=['Course Name', 'Professor', 'Ratings', 'Difficulty', 'Num of Reviews', 'Spring 21', 'Summer 21', 'Fall 21'])
# prof.to_csv('CSProfessors.csv', index=False)
#
# df2 = pd.DataFrame(['Cse115', 'Hertz', ' ',' ',' ','','',''])
# # df2.to_csv('CSProfessors.csv', mode='a', index=False, header=False)
# prof = pd.concat(df2, ignore_index=True)

def createCSV(dep):
    df = pd.DataFrame({'Course Name':[''],
                        'Event':[''],
                        'Ratings':[""],
                        'Difficulty':[''],
                        'Num of Reviews':[''],
                        'Spring 21':[''],
                        'Summer 21':[''],
                        'Fall 21':[""]
                       })
    df.to_csv(dep + ".csv", index=False)

createCSV("CSE")

# with open('cseprof.csv', 'w', newline='') as csvfile:
#     fieldnames = ['Course Name', 'Professor']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#     writer.writeheader()
#     for item in csedata.items():
#         writer.writerow({'Course Name': item[0], 'Professor': item[1][0]})
#         if len(item[1]) != 1:
#             for prof in range(1, len(item[1])):
#                 writer.writerow({'Course Name': "", 'Professor': item[1][prof]})