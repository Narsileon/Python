import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from localization import t

Etages = [1]

def main():
    display_data()

def display_data():
    for i in Etages:
        print ("{} - {} {}".format(t("retail_spaces"), t("floor"), i))
        print ("-----------------------")
        for x in range(12,42):
            print("{} 1.{}".format(t("retail_spaces"), x))
    
main()
