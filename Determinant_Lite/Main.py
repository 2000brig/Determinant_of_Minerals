import pandas as pd
from prettytable import PrettyTable
from prettytable import FRAME
from sklearn.model_selection import train_test_split
from datetime import datetime
#Introduce
print('\n THIS IS A LIGHT VERSION OF DETERMINANT OF MINERALS (V.3.1.0)')
print('\n About author:')
about = PrettyTable(border=True, hrules=FRAME, field_names=["Point", "Value"])
about.add_row(["First Name", "Ivan"])
about.add_row(["Last Name", "Bryhas"])
about.add_row(["University", "BNTU"])
about.add_row(["Department", "Mining and Environmental Engineering"])
about.add_row(["Status", "Third-year student"])
about.add_row(["Hobbies", "Teeth of Cretaceous sharks"])
about.add_row([" ", "Stratigraphy"])
about.add_row([" ", "ML & Neural Networks"])
about.add_row(["Other", "Third place at XI all-Russian"])
about.add_row([" ", "open field Olympiad for young geologists"])
about.add_row([" ", "GSA Member"])
print(about)
input('Push ENTER, Please!')
print('\n This program is a small part (some trial part) of big Determinant of Minerals Project!')
print('\n The application is accompanied by a CSV-File with some minerals (Table.csv)')
print('\n You can attach your own minerals database (To do this, follow the document: ***)')
print('\n Now relax and try using the program ;)')
print('\n Welcome to  Multi-Classifier!')

#All-program body
def model_en():
    from sklearn.naive_bayes import MultinomialNB
    from sklearn.ensemble import RandomForestClassifier
    #Read csv
    url = "Table.csv"
    names = ['1.HARDNESS', '2.COLOR', '3.STREAK', '4.LUSTRE', '5.TRANSPARENCY', '(*)NAME', '(*)RUNAME', '(*)LINK1', '(*)LINK2']
    #Create DATASET
    dataset = pd.read_csv(url, skiprows=1, names=names, delimiter=";", usecols=range(9))
    #print('Срез тестовой выборки: \n', dataset.head())
    dataset = dataset.sample(frac=1)
    dataset = dataset.sample(frac=1)
    dataset = dataset.sample(frac=1)
    X = dataset.iloc[:, :-4].values
    y = dataset.iloc[:, 5].values + ' || ' + dataset.iloc[:, 6].values + ' || ' + dataset.iloc[:, 7].values + ' || ' + dataset.iloc[:, 8].values
    X, X_test, y, y_test = train_test_split(X, y, test_size=0.40)
    #Text part
    print('','___'*22, '\n','| |'*22, '\n', '___'*22)
    print('\n Please, enter parameters of your mineral following the tables:')
    p1 = input('\n I. Please, Enter HARDNESS of your mineral (Mohs scale): ')
    print('','___'*22, '\n','| |'*22, '\n', '___'*22)
    # Accordances tables
    color = PrettyTable(border=True, hrules=FRAME, field_names=["Color", "Number"])
    color.add_row(["Black", 1])
    color.add_row(["Gray", 2])
    color.add_row(["White", 3])
    color.add_row(["Red", 4])
    color.add_row(["Orange", 5])
    color.add_row(["Yellow", 6])
    color.add_row(["Blue", 7])
    color.add_row(["Green", 8])
    color.add_row(["Brown", 9])

    lustre = PrettyTable(border=True, hrules=FRAME, field_names=["Type of Lustre", "Number"])
    lustre.add_row(["Vitreous (like a glass)", 1])
    lustre.add_row(["Adamantine", 2])
    lustre.add_row(["Submetallic", 3])
    lustre.add_row(["Metallic", 4])
    lustre.add_row(["Waxy", 5])
    lustre.add_row(["Dull (no lustre)", 6])
    lustre.add_row(["Greasy (resemble fat)", 7])

    transparency = PrettyTable(border=True, hrules=FRAME, field_names=["Type of Transparency", "Number"])
    transparency.add_row(["Transparent", 1])
    transparency.add_row(["Semitransparent", 2])
    transparency.add_row(["Non Transparent", 3])

    print('\nII. Color table:')
    print(color)
    p2 = input('II. Please, Enter COLOR of your mineral: ')
    print('','___'*22, '\n','| |'*22, '\n', '___'*22)
    print('\nIII. Streak color table:')
    print(color)
    p3 = input('III. Please, Enter STREAK color of you mineral: ')
    print('','___'*22, '\n','| |'*22, '\n', '___'*22)
    print('\nIV. Lustre table:')
    print(lustre)
    p4 = input('IV. Please, Enter LUSTRE of your mineral: ')
    print('','___'*22, '\n','| |'*22, '\n', '___'*22)
    print('\nV. Transparency table:')
    print(transparency)
    p5 = input('V. Please, Enter TRANSPARENCY of your mineral: ')
    ###

    #Classification process
    frame = [float(p1),int(p2),int(p3),int(p4),int(p5)]
    model2 = MultinomialNB(alpha=1.0, fit_prior=False)
    model2.fit(X, y)
    predicted2 = model2.predict([frame])
    classifier = RandomForestClassifier(n_estimators=50)
    classifier.fit(X, y)
    predicted = classifier.predict([frame])
    ###
    #Result
    if predicted == predicted2:
        f = open('history.txt', 'a')
        f.write('Multi-Classifier' + ' || ' + str(predicted) + ' || ' + str(datetime.today()) + '\n')
        f.close()
        print('\n ---> Maybe that mineral is ', predicted, ' <--- \n')
    else:
        f = open('history.txt', 'a')
        f.write('Naive Bayes Classifier' + ' || ' + str(predicted2) + ' || ' + str(datetime.today()) + '\n')
        f.close()
        print('\n ---> Maybe that mineral is ', predicted2, ' <--- \n (Following Naive Bayes Classifier) \n')

        f = open('history.txt', 'a')
        f.write('RandomTree Classifier' + ' || ' + str(predicted) + ' || ' + str(datetime.today()) + '\n')
        f.close()
        print('\n ---> Maybe that mineral is ', predicted, ' <--- \n (Following RandomTree Classifier) \n')
    ###

    #Feautures for creating formulas
    #def make_uchr(code: str):
    #    return chr(int(code.lstrip("U+").zfill(8), 16))
    #print('Hr',make_uchr("U+2078"))
    #print("\u0043\u0061\u0053\u004f\u00b9")
    #print(dataset['(*)NAME'])
    ###
    #Exit or try again menu
    exitter = input(
        '\n Thanks for using our program! \n \n For trying again enter letter <a> and press ENTER \n \n Please, press ENTER for exit from program. \n>>> ')
    if exitter == 'a':
        model_en()
    elif exitter == 'а':
        model_en()
    else:
        exit(0)
    ###
#RUN PROGRAM
model_en()