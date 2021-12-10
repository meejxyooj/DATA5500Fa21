import numpy as np
import json
import requests


class CountrySpecificResults():
    def __init__(self, country_name):
        self.country_name = country_name
        self.daylst = []
        self.confirmed_cases = []
        self.new_cases = []
        self.high = 0
        self.zeroday = ""
        self.highmonthname = ""
        self.lowmonthname = ""
        self.__confirmedCovidCases()
        self.__newCovidCases()
        self.__populate_month_stats()
        self.__highmonth()
        self.__lowmonth()

    def __confirmedCovidCases(self):
        url = 'https://covid-api.mmediagroup.fr/v1/history?country=' + self.country_name + '&status=confirmed'
        request = requests.get(url)
        confirmeddct = json.loads(request.text)

        key1 = "All"
        key2 = "dates"
        # datekey = specific date

        self.confirmed_cases = []
        self.daylst = []
        for datekey in confirmeddct[key1][key2]:
            if datekey <= "2021-09-30":
                self.confirmed_cases.append(float(confirmeddct[key1][key2][datekey]))
                self.daylst.append(datekey)
        self.confirmed_cases.reverse()
        self.daylst.reverse()
        # print(self.confirmed_cases)

    def __newCovidCases(self):
        self.high = 0
        self.new_cases = []
        for i in range(1, len(self.confirmed_cases)):
            self.new_cases.append(self.confirmed_cases[0])
            newcase = float(self.confirmed_cases[i] - self.confirmed_cases[i - 1])
            if newcase > self.high:
                self.high = newcase
                self.day = self.daylst[i]

            if newcase == 0:
                self.zeroday = self.daylst[i]

    def __populate_month_stats(self):
        self.month_data_dict = dict()
        for i in range(len(self.daylst)-1):
            month = self.daylst[i][:7]
            if month in self.month_data_dict:
                self.month_data_dict[month] += self.new_cases[i]
            # elif self.month_data_dict == {'2021-09': 30}:
            #     self.month_data_dict[month] = self.new_cases[i]
            else:
                self.month_data_dict[month] = self.new_cases[i]
            # print("Month", month)
            # print(self.month_data_dict[month])

    def __highmonth(self):
        max_count = 0
        for month, totalcases in self.month_data_dict.items():
            if totalcases > max_count:
                max_count = totalcases
                self.highmonthname = month

    def __lowmonth(self):
        min_count = float("inf")
        for month, totalcases in self.month_data_dict.items():
            if totalcases < min_count:
                max_count = totalcases
                self.lowmonthname = month

    def countryResults(self):
        print("------Results------")
        print("Country = ", self.country_name)
        print("Confirmed Cases = ", self.confirmed_cases[-1])
        print("Current Highest Count to Date = ", self.high, "Date", self.day)
        print("Average for whole dataset = ", np.mean(self.confirmed_cases))
        print("Most Recent 0 Case Day:", self.zeroday)
        print("The month with the highest new cases: Month:", self.highmonthname[5:7], "; Year :",
              self.highmonthname[:4])
        self.__lowmonth()
        print("The month with the lowest new cases: Month:", self.lowmonthname[5:7], "; Year :", self.lowmonthname[:4])

    # def jsondump(self):
    #     results = {}
    #     countrydictionary = {}
    #     countrydictionary["Country"] = self.country_name
    #     countrydictionary["Confirmed_Cases"] = self.confirmed_cases[-1]
    #     countrydictionary["Date_Of_Max"] = self.day
    #     countrydictionary["Max"] = self.high
    #     self.daylst.reverse()
    #     self.new_cases.reverse()


mycountries = ["US", "France", "Thailand"]

for country in mycountries:
    stats = CountrySpecificResults(country)
    stats.countryResults()