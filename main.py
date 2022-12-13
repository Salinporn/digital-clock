#   Course: 01286121 Computer Programming
#   Program: Software Engineering
#   University: Faculty of Engineering, KMITL
#   Year 1, Semester 1

#   Python Individual Project
#   Project: Digital Clock
#   Written by: Salinporn Rattanaprapaporn   


from datetime import datetime
import time
import pytz
from tkinter import *
from tkinter import messagebox, filedialog
import pickle
import winsound


class Clock():
    def __init__(self, window):
        self.window = window
        self.hour = StringVar()
        self.hour.set("00")
        self.minute = StringVar()
        self.minute.set("00")
        self.sec = StringVar()
        self.sec.set("00")
        self.menu()

        # digital clock display default
        self.label = "Bangkok"
        self.gmt = "Etc/GMT-7"
        self.clock = Label(self.window, font=("times", 50, "bold"), width=13, height=2, bg="white", fg="#3D59AB")
        self.clock.grid(row=2)
        self.name = Label(self.window, font=("times", 15, "bold"), fg="#3D59AB")
        self.name.grid(row=1, sticky="N")
        self.updatetime()

    # to update time on display
    def updatetime(self):
        self.home = pytz.timezone(self.gmt)
        self.local_time = datetime.now(self.home)
        self.current_time = self.local_time.strftime("%H:%M:%S")
        self.clock.config(text=self.current_time)
        self.name.config(text=self.label)
        self.clock.after(200, self.updatetime)

    def menu(self):
        # menubar
        menubar = Menu(self.window)
        self.window.config(menu=menubar)
        settingMenu = Menu(menubar, tearoff=False)
        menubar.add_cascade(label="Setting", menu=settingMenu)

        # choose timezones / reset timezone to default time
        timezoneMenu = Menu(settingMenu, tearoff=False)
        settingMenu.add_cascade(label="Set Timezones", menu=timezoneMenu)
        settingMenu.add_command(label="Reset Timezones", command=self.resetTimezone)

        # choose continent
        continentMenu = Menu(timezoneMenu, tearoff=False)
        africaMenu = Menu(continentMenu, tearoff=False)
        timezoneMenu.add_cascade(label="Afica", menu=africaMenu)
        americaMenu = Menu(continentMenu, tearoff=False)
        timezoneMenu.add_cascade(label="America", menu=americaMenu)
        asiaMenu = Menu(continentMenu, tearoff=False)
        timezoneMenu.add_cascade(label="Asia", menu=asiaMenu)
        australiaMenu = Menu(continentMenu, tearoff=False)
        timezoneMenu.add_cascade(label="Australia", menu=australiaMenu)
        europeMenu = Menu(continentMenu, tearoff=False)
        timezoneMenu.add_cascade(label="Europe", menu=europeMenu)

        # cities in Africa
        africaMenu.add_command(label="Abidjan", command=self.zero)
        africaMenu.add_command(label="Accra", command=self.zero)
        africaMenu.add_command(label="Addis_Ababa", command=self.posThree)
        africaMenu.add_command(label="Algiers", command=self.posOne)
        africaMenu.add_command(label="Asmara", command=self.posThree)
        africaMenu.add_command(label="Bamako", command=self.zero)
        africaMenu.add_command(label="Banjul", command=self.zero)
        africaMenu.add_command(label="Bangui", command=self.posOne)
        africaMenu.add_command(label="Bissau", command=self.zero)
        africaMenu.add_command(label="Blantyre", command=self.posTwo)
        africaMenu.add_command(label="Brazzaville", command=self.posOne)
        africaMenu.add_command(label="Bujumbura", command=self.posTwo)
        africaMenu.add_command(label="Cairo", command=self.posTwo)
        africaMenu.add_command(label="Casablanca", command=self.posOne)
        africaMenu.add_command(label="Ceuta", command=self.posOne)
        africaMenu.add_command(label="Conakry", command=self.zero)
        africaMenu.add_command(label="Dakar", command=self.zero)
        africaMenu.add_command(label="Dar_es_Salaam", command=self.posThree)
        africaMenu.add_command(label="Djibouti", command=self.posThree)
        africaMenu.add_command(label="Douala", command=self.posOne)
        africaMenu.add_command(label="El_Aaiun", command=self.posOne)
        africaMenu.add_command(label="Freetown", command=self.zero)
        africaMenu.add_command(label="Harare", command=self.posTwo)
        africaMenu.add_command(label="Johannesburg", command=self.posTwo)
        africaMenu.add_command(label="Juba", command=self.posTwo)
        africaMenu.add_command(label="Kampala", command=self.posThree)
        africaMenu.add_command(label="Khartoum", command=self.posTwo)
        africaMenu.add_command(label="Kigali", command=self.posTwo)
        africaMenu.add_command(label="Kinshasa", command=self.posOne)
        africaMenu.add_command(label="Lagos", command=self.posOne)
        africaMenu.add_command(label="Libreville", command=self.posOne)
        africaMenu.add_command(label="Lome", command=self.zero)
        africaMenu.add_command(label="Luanda", command=self.posOne)
        africaMenu.add_command(label="Lubumbashi", command=self.posTwo)
        africaMenu.add_command(label="Malabo", command=self.posOne)
        africaMenu.add_command(label="Maputo", command=self.posTwo)
        africaMenu.add_command(label="Mogadishu", command=self.posThree)
        africaMenu.add_command(label="Monrovia", command=self.zero)
        africaMenu.add_command(label="Nairobi", command=self.posThree)
        africaMenu.add_command(label="Ndjamena", command=self.posOne)
        africaMenu.add_command(label="Nouakchott", command=self.zero)
        africaMenu.add_command(label="Ouagadougou", command=self.zero)
        africaMenu.add_command(label="Porto-Novo", command=self.posOne)
        africaMenu.add_command(label="Sao_Tome", command=self.zero)
        africaMenu.add_command(label="Tripoli", command=self.posTwo)
        africaMenu.add_command(label="Tunis", command=self.posOne)
        africaMenu.add_command(label="Windhoek", command=self.posTwo)

        # cities in America
        americaMenu.add_command(label="Adak", command=self.posFourteen)
        americaMenu.add_command(label="Anchorage", command=self.negNine)
        americaMenu.add_command(label="Anguilla", command=self.negFour)
        americaMenu.add_command(label="Araguaina", command=self.negThree)
        americaMenu.add_command(label="Argentina", command=self.negThree)
        americaMenu.add_command(label="Atikokan", command=self.negFive)
        americaMenu.add_command(label="Bahia", command=self.negThree)
        americaMenu.add_command(label="Barbados", command=self.negFour)
        americaMenu.add_command(label="Belize", command=self.negSix)
        americaMenu.add_command(label="Bogota", command=self.negFive)
        americaMenu.add_command(label="Boise", command=self.negSeven)
        americaMenu.add_command(label="Cambridge_Bay", command=self.negSeven)
        americaMenu.add_command(label="Campo_Grande", command=self.negFour)
        americaMenu.add_command(label="Cancun", command=self.negFive)
        americaMenu.add_command(label="Cayenne", command=self.negThree)
        americaMenu.add_command(label="Chicago", command=self.negSix)
        americaMenu.add_command(label="Chihuahua", command=self.negSix)
        americaMenu.add_command(label="Costa_Rica", command=self.negSix)
        americaMenu.add_command(label="Danmarkshavn", command=self.zero)
        americaMenu.add_command(label="Dawson", command=self.negSeven)
        americaMenu.add_command(label="Denver", command=self.negSeven)
        americaMenu.add_command(label="Detroit", command=self.negFive)
        americaMenu.add_command(label="Dominica", command=self.negFour)
        americaMenu.add_command(label="Edmonton", command=self.negSeven)
        americaMenu.add_command(label="Eirunepe", command=self.negFive)
        americaMenu.add_command(label="El_Salvador", command=self.negSix)
        americaMenu.add_command(label="Fortaleza", command=self.negThree)
        americaMenu.add_command(label="Guyana", command=self.negFour)
        americaMenu.add_command(label="Grand_Turk", command=self.negFive)
        americaMenu.add_command(label="Guatemala", command=self.negSix)
        americaMenu.add_command(label="Halifax", command=self.negFour)
        americaMenu.add_command(label="Havana", command=self.negFive)
        americaMenu.add_command(label="Hermosillo", command=self.negSeven)
        americaMenu.add_command(label="Indiana: Indianapolis/Petersburg/Vincennes/Winamac", command=self.negFive)
        americaMenu.add_command(label="Indiana: Knox/Tell_City", command=self.negSix)
        americaMenu.add_command(label="Jamaica", command=self.negFive)
        americaMenu.add_command(label="Juneau", command=self.negNine)
        americaMenu.add_command(label="Kentucky: Louisville/Monticello", command=self.negFive)
        americaMenu.add_command(label="Kralendijk", command=self.negFour)
        americaMenu.add_command(label="La_Paz", command=self.negFour)
        americaMenu.add_command(label="Lima", command=self.negFive)
        americaMenu.add_command(label="Los_Angeles", command=self.negEight)
        americaMenu.add_command(label="Maceio", command=self.negThree)
        americaMenu.add_command(label="Managua", command=self.negSix)
        americaMenu.add_command(label="Manaus", command=self.negFour)
        americaMenu.add_command(label="Marigot", command=self.negFour)
        americaMenu.add_command(label="Mazatlan", command=self.negSeven)
        americaMenu.add_command(label="Merida", command=self.negSix)
        americaMenu.add_command(label="Metlakatla", command=self.negNine)
        americaMenu.add_command(label="Mexico_City", command=self.negSix)
        americaMenu.add_command(label="Miquelon", command=self.negThree)
        americaMenu.add_command(label="New_York", command=self.negFive)
        americaMenu.add_command(label="Noronha", command=self.negTwo)
        americaMenu.add_command(label="North_Dakota: Beulah/Center/New_Salem", command=self.negSix)
        americaMenu.add_command(label="Nuuk", command=self.negThree)
        americaMenu.add_command(label="Ojinaga", command=self.negSix)
        americaMenu.add_command(label="Panama", command=self.negFive)
        americaMenu.add_command(label="Paramaribo", command=self.negThree)
        americaMenu.add_command(label="Phoenix", command=self.negSeven)
        americaMenu.add_command(label="Port_of_Spain", command=self.negFour)
        americaMenu.add_command(label="Puerto_Rico", command=self.negFour)
        americaMenu.add_command(label="Regina", command=self.negSix)
        americaMenu.add_command(label="Resolute", command=self.negSix)
        americaMenu.add_command(label="Santarem", command=self.negThree)
        americaMenu.add_command(label="Santiago", command=self.negThree)
        americaMenu.add_command(label="Santo_Domingo", command=self.negFour)
        americaMenu.add_command(label="Sao_Paulo", command=self.negThree)
        americaMenu.add_command(label="Sitka", command=self.negNine)
        americaMenu.add_command(label="St_Johns", command=self.negThreeHalf)
        americaMenu.add_command(label="St_Lucia", command=self.negFour)
        americaMenu.add_command(label="St_Thomas", command=self.negFour)
        americaMenu.add_command(label="St_Vincent", command=self.negFour)
        americaMenu.add_command(label="Tegucigalpa", command=self.negSix)
        americaMenu.add_command(label="Thule", command=self.negFour)
        americaMenu.add_command(label="Toronto", command=self.negFive)
        americaMenu.add_command(label="Vancouver", command=self.negEight)

        # cities in Asia
        asiaMenu.add_command(label="Aden", command=self.posThree)
        asiaMenu.add_command(label="Almaty", command=self.posSix)
        asiaMenu.add_command(label="Amman", command=self.posThree)
        asiaMenu.add_command(label="Anadyr", command=self.posTwelve)
        asiaMenu.add_command(label="Aqtau", command=self.posFive)
        asiaMenu.add_command(label="Ashgabat", command=self.posFive)
        asiaMenu.add_command(label="Atyrau", command=self.posFive)
        asiaMenu.add_command(label="Baghdad", command=self.posThree)
        asiaMenu.add_command(label="Bahrain", command=self.posThree)
        asiaMenu.add_command(label="Baku", command=self.posFour)
        asiaMenu.add_command(label="Bangkok", command=self.posSeven)
        asiaMenu.add_command(label="Barnaul", command=self.posSeven)
        asiaMenu.add_command(label="Beirut", command=self.posTwo)
        asiaMenu.add_command(label="Bishkek", command=self.posSix)
        asiaMenu.add_command(label="Brunei", command=self.posEight)
        asiaMenu.add_command(label="Chita", command=self.posNine)
        asiaMenu.add_command(label="Dubai", command=self.posFour)
        asiaMenu.add_command(label="Dushanbe", command=self.posFive)
        asiaMenu.add_command(label="Famagusta", command=self.posTwo)
        asiaMenu.add_command(label="Gaza", command=self.posTwo)
        asiaMenu.add_command(label="Hebron", command=self.posTwo)
        asiaMenu.add_command(label="Ho_Chi_Minh", command=self.posSeven)
        asiaMenu.add_command(label="Hong_Kong", command=self.posEight)
        asiaMenu.add_command(label="Hovd", command=self.posSeven)
        asiaMenu.add_command(label="Irkutsk", command=self.posEight)
        asiaMenu.add_command(label="Jakarta", command=self.posSeven)
        asiaMenu.add_command(label="Jayapura", command=self.posNine)
        asiaMenu.add_command(label="Jerusalem", command=self.posTwo)
        asiaMenu.add_command(label="Kabul", command=self.posFive)
        asiaMenu.add_command(label="Kamchatka", command=self.posTwelve)
        asiaMenu.add_command(label="Karachi", command=self.posFive)
        asiaMenu.add_command(label="Kathmandu", command=self.posSix)
        asiaMenu.add_command(label="Khandyga", command=self.posThree)
        asiaMenu.add_command(label="Kolkata", command=self.posSix)
        asiaMenu.add_command(label="Krasnoyarsk", command=self.posSeven)
        asiaMenu.add_command(label="Kuala_Lumpur", command=self.posEight)
        asiaMenu.add_command(label="Kuching", command=self.posEight)
        asiaMenu.add_command(label="Kuwait", command=self.posThree)
        asiaMenu.add_command(label="Macau", command=self.posEight)
        asiaMenu.add_command(label="Magadan", command=self.posEleven)
        asiaMenu.add_command(label="Makassar", command=self.posEight)
        asiaMenu.add_command(label="Manila", command=self.posEight)
        asiaMenu.add_command(label="Muscat", command=self.posFour)
        asiaMenu.add_command(label="Nicosia", command=self.posTwo)
        asiaMenu.add_command(label="Novokuznetsk", command=self.posSeven)
        asiaMenu.add_command(label="Novosibirsk", command=self.posSeven)
        asiaMenu.add_command(label="Omsk", command=self.posSix)
        asiaMenu.add_command(label="Oral", command=self.posFive)
        asiaMenu.add_command(label="Phnom_Penh", command=self.posSeven)
        asiaMenu.add_command(label="Pontianak", command=self.posSeven)
        asiaMenu.add_command(label="Pyongyang", command=self.posNine)
        asiaMenu.add_command(label="Qatar", command=self.posThree)
        asiaMenu.add_command(label="Qostanay", command=self.posSix)
        asiaMenu.add_command(label="Qyzylorda", command=self.posFive)
        asiaMenu.add_command(label="Riyadh", command=self.posThree)
        asiaMenu.add_command(label="Sakhalin", command=self.posEleven)
        asiaMenu.add_command(label="Samarkand", command=self.posFive)
        asiaMenu.add_command(label="Seoul", command=self.posNine)
        asiaMenu.add_command(label="Shanghai", command=self.posEight)
        asiaMenu.add_command(label="Singapore", command=self.posEight)
        asiaMenu.add_command(label="Srednekolymsk", command=self.posEleven)
        asiaMenu.add_command(label="Taipei", command=self.posEight)
        asiaMenu.add_command(label="Tashkent", command=self.posFive)
        asiaMenu.add_command(label="Tbilisi", command=self.posFour)
        asiaMenu.add_command(label="Tehran", command=self.posFour)
        asiaMenu.add_command(label="Thimphu", command=self.posSix)
        asiaMenu.add_command(label="Tokyo", command=self.posNine)
        asiaMenu.add_command(label="Tomsk", command=self.posSeven)
        asiaMenu.add_command(label="Ulaanbaatar", command=self.posEight)
        asiaMenu.add_command(label="Urumqi", command=self.posSix)
        asiaMenu.add_command(label="Ust-Nera", command=self.posTen)
        asiaMenu.add_command(label="Vientiane", command=self.posSeven)
        asiaMenu.add_command(label="Vladivostok", command=self.posTen)
        asiaMenu.add_command(label="Yakutsk", command=self.posNine)
        asiaMenu.add_command(label="Yangon", command=self.posSeven)
        asiaMenu.add_command(label="Yekaterinburg", command=self.posFive)
        asiaMenu.add_command(label="Yerevan", command=self.posFour)

        # cities in Australia
        australiaMenu.add_command(label="Adelaide", command=self.posTenHalf)
        australiaMenu.add_command(label="Brisbane", command=self.posTen)
        australiaMenu.add_command(label="Broken_Hill", command=self.posTenHalf)
        australiaMenu.add_command(label="Darwin", command=self.posNineHalf)
        australiaMenu.add_command(label="Eucla", command=self.posEightFortyFive)
        australiaMenu.add_command(label="Hobart", command=self.posEleven)
        australiaMenu.add_command(label="Lindeman", command=self.posTen)
        australiaMenu.add_command(label="Lord_Howe", command=self.posEleven)
        australiaMenu.add_command(label="Melbourne", command=self.posEleven)
        australiaMenu.add_command(label="Perth", command=self.posEight)
        australiaMenu.add_command(label="Sydney", command=self.posEleven)

        # cities in Europe
        europeMenu.add_command(label="Amsterdam", command=self.posOne)
        europeMenu.add_command(label="Andorra", command=self.posOne)
        europeMenu.add_command(label="Astrakhan", command=self.posFour)
        europeMenu.add_command(label="Athens", command=self.posTwo)
        europeMenu.add_command(label="Belgrade", command=self.posOne)
        europeMenu.add_command(label="Berlin", command=self.posOne)
        europeMenu.add_command(label="Bratislava", command=self.posOne)
        europeMenu.add_command(label="Brussels", command=self.posOne)
        europeMenu.add_command(label="Bucharest", command=self.posTwo)
        europeMenu.add_command(label="Budapest", command=self.posOne)
        europeMenu.add_command(label="Busingen", command=self.posOne)
        europeMenu.add_command(label="Chisinau", command=self.posTwo)
        europeMenu.add_command(label="Copenhagen", command=self.posOne)
        europeMenu.add_command(label="Dublin", command=self.zero)
        europeMenu.add_command(label="Gibraltar", command=self.posOne)
        europeMenu.add_command(label="Guernsey", command=self.zero)
        europeMenu.add_command(label="Helsinki", command=self.posTwo)
        europeMenu.add_command(label="Isle_of_Man", command=self.zero)
        europeMenu.add_command(label="Istanbul", command=self.posThree)
        europeMenu.add_command(label="Jersey", command=self.zero)
        europeMenu.add_command(label="Kaliningrad", command=self.posTwo)
        europeMenu.add_command(label="Kiev", command=self.posTwo)
        europeMenu.add_command(label="Kirov", command=self.posThree)
        europeMenu.add_command(label="Lisbon", command=self.zero)
        europeMenu.add_command(label="Ljubljana", command=self.posOne)
        europeMenu.add_command(label="London", command=self.zero)
        europeMenu.add_command(label="Luxembourg", command=self.posOne)
        europeMenu.add_command(label="Madrid", command=self.posOne)
        europeMenu.add_command(label="Malta", command=self.posOne)
        europeMenu.add_command(label="Mariehamn", command=self.posTwo)
        europeMenu.add_command(label="Minsk", command=self.posThree)
        europeMenu.add_command(label="Monaco", command=self.posOne)
        europeMenu.add_command(label="Moscow", command=self.posThree)
        europeMenu.add_command(label="Oslo", command=self.posOne)
        europeMenu.add_command(label="Paris", command=self.posOne)
        europeMenu.add_command(label="Podgorica", command=self.posOne)
        europeMenu.add_command(label="Prague", command=self.posOne)
        europeMenu.add_command(label="Riga", command=self.posTwo)
        europeMenu.add_command(label="Rome", command=self.posOne)
        europeMenu.add_command(label="Samara", command=self.posFour)
        europeMenu.add_command(label="San_Marino", command=self.posOne)
        europeMenu.add_command(label="Sarajevo", command=self.posOne)
        europeMenu.add_command(label="Saratov", command=self.posFour)
        europeMenu.add_command(label="Simferopol", command=self.posThree)
        europeMenu.add_command(label="Skopje", command=self.posOne)
        europeMenu.add_command(label="Sofia", command=self.posTwo)
        europeMenu.add_command(label="Stockholm", command=self.posOne)
        europeMenu.add_command(label="Tallinn", command=self.posTwo)
        europeMenu.add_command(label="Tirane", command=self.posOne)
        europeMenu.add_command(label="Ulyanovsk", command=self.posFour)
        europeMenu.add_command(label="Uzhgorod", command=self.posTwo)
        europeMenu.add_command(label="Vaduz", command=self.posOne)
        europeMenu.add_command(label="Vatican", command=self.posOne)
        europeMenu.add_command(label="Vienna", command=self.posOne)
        europeMenu.add_command(label="Vilnius", command=self.posTwo)
        europeMenu.add_command(label="Volgograd", command=self.posThree)
        europeMenu.add_command(label="Warsaw", command=self.posOne)
        europeMenu.add_command(label="Zagreb", command=self.posOne)
        europeMenu.add_command(label="Zaporozhye", command=self.posTwo)
        europeMenu.add_command(label="Zurich", command=self.posOne)

    # change time and label into Bangkok
    def resetTimezone(self):
        self.gmt = "Etc/GMT-7"
        self.label = "Bangkok"

    # change time into different GMT
    def zero(self):
        self.gmt = "Etc/GMT0"
        self.label = "GMT 0"

    def posOne(self):
        self.gmt = "Etc/GMT-1"
        self.label = "GMT +1"

    def posTwo(self):
        self.gmt = "Etc/GMT-2"
        self.label = "GMT +2"

    def posThree(self):
        self.gmt = "Etc/GMT-3"
        self.label = "GMT +3"

    def posFour(self):
        self.gmt = "Etc/GMT-4"
        self.label = "GMT +4"

    def posFive(self):
        self.gmt = "Etc/GMT-5"
        self.label = "GMT +5"

    def posSix(self):
        self.gmt = "Etc/GMT-6"
        self.label = "GMT +6"

    def posSeven(self):
        self.gmt = "Etc/GMT-7"
        self.label = "GMT +7"

    def posEight(self):
        self.gmt = "Etc/GMT-8"
        self.label = "GMT +8"

    def posEightFortyFive(self):
        self.gmt = "Australia/Eucla"
        self.label = "GMT +8.45"

    def posNine(self):
        self.gmt = "Etc/GMT-9"
        self.label = "GMT +9"

    def posNineHalf(self):
        self.gmt = "Australia/Darwin"
        self.label = "GMT +9.30"

    def posTen(self):
        self.gmt = "Etc/GMT-10"
        self.label = "GMT +10"

    def posTenHalf(self):
        self.gmt = "Australia/Adelaide"
        self.label = "GMT +10.30"

    def posEleven(self):
        self.gmt = "Etc/GMT-11"
        self.label = "GMT +11"

    def posTwelve(self):
        self.gmt = "Etc/GMT-12"
        self.label = "GMT +12"

    def posFourteen(self):
        self.gmt = "Etc/GMT-14"
        self.label = "GMT +14"

    def negTwo(self):
        self.gmt = "Etc/GMT+2"
        self.label = "GMT -2"

    def negThree(self):
        self.gmt = "Etc/GMT+3"
        self.label = "GMT -3"

    def negThreeHalf(self):
        self.gmt = "America/St_Johns"
        self.label = "GMT -3.30"

    def negFour(self):
        self.gmt = "Etc/GMT+4"
        self.label = "GMT -4"

    def negFive(self):
        self.gmt = "Etc/GMT+5"
        self.label = "GMT -5"

    def negSix(self):
        self.gmt = "Etc/GMT+6"
        self.label = "GMT -6"

    def negSeven(self):
        self.gmt = "Etc/GMT+7"
        self.label = "GMT -7"

    def negEight(self):
        self.gmt = "Etc/GMT+8"
        self.label = "GMT -8"

    def negNine(self):
        self.gmt = "Etc/GMT+9"
        self.label = "GMT -9"


class Timer(Clock):
    def __init__(self, window):
        super().__init__(window)

        # button to use countdown function
        btCountdown = Button(self.window, text="Countdown Timer", width=15, height=1, font=("times", 15),
                             bg="#6495ED", fg="#FFF8DC", command=self.countdown)
        btCountdown.grid(row=4, sticky="W")

    def countdown(self):
        self.w1 = Toplevel(self.window)
        self.w1.attributes("-topmost", True)
        self.w1.title("Timer")

        # input hours, minutes, seconds
        hour_input = Entry(self.w1, width=3, font=("times", 50, "bold"), justify="center", fg="#3D59AB",
                           textvariable=self.hour)
        hour_input.grid(row=0, column=0)

        minute_input = Entry(self.w1, width=3, font=("times", 50, "bold"), justify="center", fg="#3D59AB",
                             textvariable=self.minute)
        minute_input.grid(row=0, column=1, pady=7)

        sec_input = Entry(self.w1, width=3, font=("times", 50, "bold"), justify="center", fg="#3D59AB",
                          textvariable=self.sec)
        sec_input.grid(row=0, column=2)

        # button to start countdown
        btSettime = Button(self.w1, text="Set Time", font=("times", 15), bd='5',
                           bg="#6495ED", fg="#FFF8DC", command=self.setTimer)
        btSettime.grid(row=1, column=1)

    def setTimer(self):
        # check if user enters right values which are integer
        try:
            temp = int(self.hour.get()) * 3600 + int(self.minute.get()) * 60 + int(self.sec.get())
        except:
            print("Please enter right values for the input")

        while temp >= 0:
            mins, secs = divmod(temp, 60)
            hours = 0
            if mins > 60:
                hours, mins = divmod(mins, 60)
            self.hour.set(f"{hours:02}")
            self.minute.set(f"{mins:02}")
            self.sec.set(f"{secs:02}")
            self.w1.update()
            time.sleep(1)

            # Show messagebox when total second = 0
            if temp == 0:
                messagebox.showinfo("Countdown", "Time's up!")

            temp -= 1

        self.hour.set("00")
        self.minute.set("00")
        self.sec.set("00")


class StopWatch(Clock):
    def __init__(self, window):
        super().__init__(window)
        self.sw_time = ""

        # button to use stopwatch function
        btCountup = Button(self.window, text="Stopwatch", width=15, height=1, font=("times", 15),
                           bg="#6495ED", fg="#FFF8DC", command=self.stopwatch)
        btCountup.grid(row=4, sticky="E")

    def stopwatch(self):
        self.w2 = Toplevel(self.window)
        self.w2.attributes("-topmost", True)
        self.w2.title("Stopwatch")

        hourlabel = Label(self.w2, width=3, height=1, font=("times", 50, "bold"), justify="center",
                          fg="#3D59AB", bg="white", textvariable=self.hour)
        hourlabel.grid(row=0, column=0)

        minutelabel = Label(self.w2, width=3, height=1, font=("times", 50, "bold"), justify="center",
                            fg="#3D59AB", bg="white", textvariable=self.minute)
        minutelabel.grid(row=0, column=1, pady=7, padx=3)

        secondlabel = Label(self.w2, width=3, height=1, font=("times", 50, "bold"), justify="center",
                            fg="#3D59AB", bg="white", textvariable=self.sec)
        secondlabel.grid(row=0, column=2, padx=1)

        # button to reset time of stopwatch
        self.btReset = Button(self.w2, width=10, text="Reset", font=("times", 15), bd='5',
                              bg="#6495ED", fg="#FFF8DC", command=self.reset_stopwatch)
        self.btReset.grid(row=1, column=0)

        # button to start/stop the time
        self.btStartStop = Button(self.w2, width=10,text="Start", font=("times", 15), bd='5',
                         bg="#6495ED", fg="#FFF8DC", command=self.startstop)
        self.btStartStop.grid(row=1, column=1, padx=1)

        # button to choose file and save laps time into the file
        self.btSaveLaps = Button(self.w2, width=10, text="Choose file", font=("times", 15), bd='5',
                        bg="#6495ED", fg="#FFF8DC", command=self.saveLaps)
        self.btSaveLaps.grid(row=1, column=2, padx=1)

    def startstop(self):
        if self.btStartStop['text'] == "Start":
            # change label and color of the button into "Stop" after clicking it
            self.btStartStop['text'] = "Stop"
            self.btStartStop.config(bg="#DC143C", fg="#FFF8DC")

            self.bool = True
            temp = int(self.hour.get()) * 3600 + int(self.minute.get()) * 60 + int(self.sec.get())

            while self.bool == True:
                secs, msecs = divmod(temp, 60)
                mins = 0
                if secs > 60:
                    hours, mins = divmod(secs, 60)
                self.hour.set(f"{mins:02}")
                self.minute.set(f"{secs:02}")
                self.sec.set(f"{msecs:02}")
                self.w2.update()
                time.sleep(0.001) # make time run in milliseconds

                temp += 1

        elif self.btStartStop['text'] == "Stop":
            # change label and color of the button into "Start" after clicking it
            self.btStartStop['text'] = "Start"
            self.btStartStop.config(bg="#6495ED", fg="#FFF8DC")
            self.bool = False # break the loop to stop the running time


    def reset_stopwatch(self):
        # change label and color of the button to "Start"
        self.btStartStop['text'] = "Start"
        self.btStartStop.config(bg="#6495ED", fg="#FFF8DC")
        self.bool = False
        self.hour.set("00")
        self.minute.set("00")
        self.sec.set("00")
        self.w2.update()

    def saveLaps(self):
        if self.btSaveLaps['text'] == "Choose file":
            # change label and color of the button into "Laps" after clicking it
            self.btSaveLaps['text'] = "Laps"
            self.btSaveLaps.config(bg="#00C957", fg="#FFF8DC")

            # choose/create file in project/stopwatch folder
            self.file = filedialog.asksaveasfilename(initialdir="project/stopwatch")

        elif self.btSaveLaps['text'] == "Laps":
            # add time to text file when user clicks on "Laps" button
            self.sw_time += self.hour.get() + " M : " + self.minute.get() + " S : " + self.sec.get() + " mS\n"
            savefile = open(self.file, "w")
            savefile.write(self.sw_time)
            savefile.close()


class AlarmClock(Clock):
    def __init__(self, window):
        super().__init__(window)
        self.isRun = False

        self.hh = StringVar()
        self.hh_list = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09',
                     '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
                     '20', '21', '22', '23', '24']
        self.hh.set(self.hh_list[0])

        self.mm = StringVar()
        self.mm_list = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09',
                    '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
                    '20', '21', '22', '23', '24', '25', '26', '27', '28', '29',
                    '30', '31', '32', '33', '34', '35', '36', '37', '38', '39',
                    '40', '41', '42', '43', '44', '45', '46', '47', '48', '49',
                    '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60']
        self.mm.set(self.mm_list[0])

        self.ss = StringVar()
        self.ss_list = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09',
                    '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
                    '20', '21', '22', '23', '24', '25', '26', '27', '28', '29',
                    '30', '31', '32', '33', '34', '35', '36', '37', '38', '39',
                    '40', '41', '42', '43', '44', '45', '46', '47', '48', '49',
                    '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60']
        self.ss.set(self.ss_list[0])

        # button to use alarm clock function
        btAlarm = Button(self.window, text="Alarm clock", width=15, height=1, font=("times", 15),
                         bg="#6495ED", fg="#FFF8DC", command=self.alarm)
        btAlarm.grid(row=4)

    def alarm(self):
        self.w3 = Toplevel(self.window)
        self.w3.attributes("-topmost", True)
        self.w3.title("Alarm")

        h = OptionMenu(self.w3, self.hh, *self.hh_list)
        h.config(font=("times", 50, "bold"), bg="white", fg="#3D59AB")
        h.grid(row=0, column=0)

        m = OptionMenu(self.w3, self.mm, *self.mm_list)
        m.config(font=("times", 50, "bold"), bg="white", fg="#3D59AB")
        m.grid(row=0, column=1)

        s = OptionMenu(self.w3, self.ss, *self.ss_list)
        s.config(font=("times", 50, "bold"), bg="white", fg="#3D59AB")
        s.grid(row=0, column=2)

        # button to set time and run the alarm clock
        self.btRunAlarm = Button(self.w3, width=9, text="Set Alarm", font=("times", 15), bd='4',
                           bg="#6495ED", fg="#FFF8DC", command=self.runAlarm)
        self.btRunAlarm.grid(row=1, column=1, pady=7)

    def runAlarm(self):
        alarm_time = f"{self.hh.get()}:{self.mm.get()}:{self.ss.get()}"
        self.isRun = True

        while self.isRun != False:
            time.sleep(1)
            now = datetime.now().strftime("%H:%M:%S")

            # if current time = alarm time user set,
            if now == alarm_time:
                # play beep sound and show message box saying "Wake up!"
                winsound.PlaySound("alarm_beep.wav", winsound.SND_FILENAME)
                messagebox.showinfo("Alarm", "Wake up!")
                self.isRun = False


if __name__ == "__main__":
    root = Tk()
    c = Clock(root)
    tm = Timer(root)
    sw = StopWatch(root)
    al = AlarmClock(root)
    root.title("Digital Clock")
    root.mainloop()
