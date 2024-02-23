#Definicja funkcji stolice Europy
def Europe_Capitols ():

    Europe_country = input ('Podaj nazwę kraju w Europie (wpisz poprawnie nazwę!)  ')

    match Europe_country:
        case 'Polska':
            print ('Stolicą kraju', Europe_country, 'jest Warszawa')
        case 'Francja':
            print ('Stolicą kraju', Europe_country, 'jest Paryż')
        case 'Niemcy':
            print ('Stolicą kraju', Europe_country, 'jest Berlin')
        case 'Austria':
            print ('Stolicą kraju', Europe_country, 'jest Wiedeń')
        case 'Hiszpania':
            print ('Stolicą kraju', Europe_country, 'jest Barcelona')
        case 'Wielka Brytania':
            print ('Stolicą kraju', Europe_country, 'jest Londyn')
        case 'Irlandia':
            print ('Stolicą kraju', Europe_country, 'jest Dublin')
        case 'Czechy':
            print ('Stolicą kraju', Europe_country, 'jest Praga')  
        case 'Słowacja':
            print ('Stolicą kraju', Europe_country, 'jest Bratysława')  
        case 'Węgry':
            print ('Stolicą kraju', Europe_country, 'jest Budapeszt')
        case 'Rumunia':
            print ('Stolicą kraju', Europe_country, 'jest Bukareszt')  
        case 'Bułgaria':
            print ('Stolicą kraju', Europe_country, 'jest Sofia')  
        case 'Szwajcaria':
            print ('Stolicą kraju', Europe_country, 'jest Berno')
        case 'Włochy':
            print ('Stolicą kraju', Europe_country, 'jest Rzym')  
        case 'Słowenia':
            print ('Stolicą kraju', Europe_country, 'jest Lublana')
        case 'Chorwacja':
            print ('Stolicą kraju', Europe_country, 'jest Zagrzeb')
        case 'Belgia':
            print ('Stolicą kraju', Europe_country, 'jest Bruksela')
        case 'Holandia':
            print ('Stolicą kraju', Europe_country, 'jest Amsterdam')
        case 'Mołdawia':
            print ('Stolicą kraju', Europe_country, 'jest Kiszyniów')
        case 'Albania':
            print ('Stolicą kraju', Europe_country, 'jest Tirana')
        case 'Grecja':
            print ('Stolicą kraju', Europe_country, 'jest Ateny')
        case 'Estonia':
            print ('Stolicą kraju', Europe_country, 'jest Tallin') 
        case 'Litwa':
            print ('Stolicą kraju', Europe_country, 'jest Wilno') 
        case 'Łotwa':
            print ('Stolicą kraju', Europe_country, 'jest Ryga')
        case 'Norwegia':
            print ('Stolicą kraju', Europe_country, 'jest Oslo')
        case 'Szwecja':
            print ('Stolicą kraju', Europe_country, 'jest Sztokholm')
        case 'Finlandia':
            print ('Stolicą kraju', Europe_country, 'jest Helsinki')
        case 'Dania':
            print ('Stolicą kraju', Europe_country, 'jest Kopenhaga')    
        case _:
            print ('Nie rozpoznaję takiego kraju w Europie') 


#Definicja funkcji stolice Ameryki
def American_Capitols ():

    American_country = input ('Podaj nazwę kraju w Ameryce północnej lub Połódniowej (wpisz poprawnie nazwę!)  ')

    match American_country:
        case 'Polska':
            print ('Stolicą kraju', American_country, 'jest Warszawa')
        case 'Francja':
            print ('Stolicą kraju', American_country, 'jest Paryż')
        case 'Niemcy':
            print ('Stolicą kraju', American_country, 'jest Berlin')
        case 'Austria':
            print ('Stolicą kraju', American_country, 'jest Wiedeń')
        case 'Hiszpania':
            print ('Stolicą kraju', American_country, 'jest Barcelona')
        case 'Wielka Brytania':
            print ('Stolicą kraju', American_country, 'jest Londyn')
        case 'Irlandia':
            print ('Stolicą kraju', American_country, 'jest Dublin')
        case 'Czechy':
            print ('Stolicą kraju', American_country, 'jest Praga')  
        case 'Słowacja':
            print ('Stolicą kraju', American_country, 'jest Bratysława')  
        case 'Węgry':
            print ('Stolicą kraju', American_country, 'jest Budapeszt')
        case 'Rumunia':
            print ('Stolicą kraju', American_country, 'jest Bukareszt')  
        case 'Bułgaria':
            print ('Stolicą kraju', American_country, 'jest Sofia')  
        case 'Szwajcaria':
            print ('Stolicą kraju', American_country, 'jest Berno')
        case 'Włochy':
            print ('Stolicą kraju', American_country, 'jest Rzym')  
        case 'Słowenia':
            print ('Stolicą kraju', American_country, 'jest Lublana')
        case 'Chorwacja':
            print ('Stolicą kraju', American_country, 'jest Zagrzeb')
        case 'Belgia':
            print ('Stolicą kraju', American_country, 'jest Bruksela')
        case 'Holandia':
            print ('Stolicą kraju', American_country, 'jest Amsterdam')
        case 'Mołdawia':
            print ('Stolicą kraju', American_country, 'jest Kiszyniów')
        case 'Albania':
            print ('Stolicą kraju', American_country, 'jest Tirana')
        case 'Grecja':
            print ('Stolicą kraju', American_country, 'jest Ateny')
        case 'Estonia':
            print ('Stolicą kraju', American_country, 'jest Tallin') 
        case 'Litwa':
            print ('Stolicą kraju', American_country, 'jest Wilno') 
        case 'Łotwa':
            print ('Stolicą kraju', American_country, 'jest Ryga')
        case 'Norwegia':
            print ('Stolicą kraju', American_country, 'jest Oslo')
        case 'Szwecja':
            print ('Stolicą kraju', American_country, 'jest Sztokholm')
        case 'Finlandia':
            print ('Stolicą kraju', American_country, 'jest Helsinki')
        case 'Dania':
            print ('Stolicą kraju', American_country, 'jest Kopenhaga')    
        case _:
            print ('Nie rozpoznaję takiego kraju w Europie') 

American_country = None
Alternate_choice = None
Europa_choice = None
Continent_choice = None

#Zapytanie o stolice Europy i wywołanie funkcji
Europa_choice = input ('Czy chcesz dowiedzieć się jak nazywają się stolice krajów w Europie? (wciśnij t lub n) ')

while Europa_choice == 't':
    #Uruchomienie funkcji Europe_Capitols
        Europe_Capitols ()
        Europa_choice = input ('Czy chcesz jeszcze dowiedzieć się jak nazywają się stolice krajów w Europie? (wciśnij t lub n) ')

Alternate_choice = input ('Czy chcesz dowiedzieć się jak nazywają się stolice krajów na innych kontynentach? (Wpisz t lub n) ')

while Alternate_choice =='t':
    #Wyświetlenie listy wyboru kontynentów
        Continent_choice = input ("""Wybierz kontynent lub wpisz stop:
                                     1. Ameryka Północna i Połódniowa wpisz Ameryka
                                     2. Azja wpisz Azja
                                     3. Europa wpisz Europa
                                     """ ) 
        
        while Continent_choice == 'Ameryka':
            American_Capitols ()
            America_choice = input ('Czy chcesz jeszcze dowiedzieć się jak nazywają się stolice krajów w Ameryce? (wciśnij t lub n) ')
            while America_choice == 't':
                American_Capitols ()
                America_choice = input ('Czy chcesz jeszcze dowiedzieć się jak nazywają się stolice krajów w Ameryce? (wciśnij t lub n) ')
           
            Continent_choice = input ("""Wybierz kontynent lub wpisz stop:
                                     1. Ameryka Północna i Połódniowa wpisz Ameryka
                                     2. Azja wpisz Azja
                                     3. Europa wpisz Europa
                                     """ )
                
        while Continent_choice == 'Azja':
            Europe_Capitols ()
            Europe_choice = input ('Czy chcesz jeszcze dowiedzieć się jak nazywają się stolice krajów w Azji? (wciśnij t lub n) ')
            while Europe_choice == 't':
                Europe_Capitols ()
                Europe_choice = input ('Czy chcesz jeszcze dowiedzieć się jak nazywają się stolice krajów w Azji? (wciśnij t lub n) ') 
            
            Continent_choice = input ("""Wybierz kontynent lub wpisz stop:
                                     1. Ameryka Północna i Połódniowa wpisz Ameryka
                                     2. Azja wpisz Azja
                                     3. Europa wpisz Europa
                                     """ )
        
        while Continent_choice == 'Europa':
            Europe_Capitols ()
            Europe_choice = input ('Czy chcesz jeszcze dowiedzieć się jak nazywają się stolice krajów w Europie? (wciśnij t lub n) ')
            while Europa_choice == 't':
                Europe_Capitols ()
                Europe_choice = input ('Czy chcesz jeszcze dowiedzieć się jak nazywają się stolice krajów w Europie? (wciśnij t lub n) ')

            
            Continent_choice = input ("""Wybierz kontynent lub wpisz stop:
                                     1. Ameryka Północna i Połódniowa wpisz Ameryka
                                     2. Azja wpisz Azja
                                     3. Europa wpisz Europa
                                     """ )
print ('Dziękuję za zabawę')
print ('Nie rozpoznaję kontynentu')
Alternate_choice = None
        
Continent_choice = None
