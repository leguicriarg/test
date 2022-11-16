import datetime
import random
import numpy as np
import pandas as pd


class HotelsInfo:      
    def last (hotel_list, dateFrom, dateTo):
        
        list_rooms = ['Doble','Individual','Junior','Suite','Simple']
        list_boards = ['Desayuno','Media Pension','Solo Alojamiento','Pension Completa','Todo Incluido']
        format = '%Y-%m-%d'
        date_list = []
        avg_price = []
        min_price = []
        max_price = []
        dateFrom = datetime.datetime.strptime(dateFrom, format)
        dateTo = datetime.datetime.strptime(dateTo, format)
        
        def boards(list_boards,date_list):
            """_summary_ : creates a list with all possible boards in each day

            Args:
                list_boards (list): list of available boards
                date_list (list): list of dates

            Returns:
                boards_list (list): randomized list of boards for each day
            """
            
            boards_list = []
            for day in range(len(date_list)):
                boards_list.append(random.choice(list_boards))
            return boards_list

        def rooms(list_rooms,date_list):
            """_summary_: creates a list with all possible boards in each date

            Args:
                list_rooms (list): list of available rooms
                date_list (list): list of dates

            Returns:
                rooms_list(list): randomized list of rooms for each day
            """
            
            rooms_list = []
            for day in range(len(date_list)):
                rooms_list.append(random.choice(list_rooms))
            return rooms_list

        def daterange(dateFrom, dateTo, format):
            
            """_summary_ : creates a list of dates

            Args:
                dateFrom (datetime): date for query (from)
                dateTo (datetime): date for query (to)
                format (string): string with the format 

            Returns:
                date_list (list): list of dates between selected range
            """
            
            date_list = []
            for day in range(int ((dateTo - dateFrom).days)+1):
                date_list.append((dateFrom + datetime.timedelta(day)).strftime(format))
            return date_list

        def daily_price(date_list):
            
            """_summary_: creates a list of random prices for each date

            Args:
                date_list (list): list of dates in selected range
            Returns:
                daily_prices_list (list): list of dates between selected range
            """
            
            daily_prices_list = []
            for day in range(len(date_list)):
                prices = []
                for daily_price in range(5): 
                    prices.append(random.randint(20,380))
                daily_prices_list.append(prices)
            
            return daily_prices_list
        
        def final_kpis(df_temp):
            """_summary_: creates dictionary for query response

            Args:
                df_temp (dataframe): dataframe with all data

            Returns:
                dict_response (dictionary): dictionary with elements required
            """
            
            dict_response = {}
            name_max_price = df_temp.loc[df_temp['max'].idxmax()]
            name_min_price = df_temp.loc[df_temp['min'].idxmin()]
            max_list = df_temp['max'].tolist()
            min_list = df_temp['min'].tolist()
            avg = df_temp['avg'].tolist()
            dict_response = {'avg': avg,
                            'max_price_data': name_max_price['hotel'],
                            'min_price_data': name_min_price['hotel'], 
                            'max_price_list': max_list,
                            'min_price_list': min_list,
                            'more_expensive_day': name_max_price['date']
                            }
            return (dict_response)
        
        

        date_list = daterange(dateFrom, dateTo, format)
        df_temp = pd.DataFrame()
        prices = daily_price(date_list)
        rooms_list = rooms(list_rooms,date_list)
        board_list =  boards(list_boards,date_list)

        # Create a DF with all the data in list format
        for hotel in hotel_list:
            df_temp['date'] = date_list 
            df_temp['hotel'] = hotel
            df_temp['prices'] = prices
            df_temp['board'] = board_list
            df_temp['room'] = rooms_list
        
        # Reorganize the temp dataframe
        df_temp = df_temp.reset_index()
        df_temp = df_temp[['hotel','date','board','room','prices']]

        # We have prices as list in a df column. This is for avg, min and max price of each list
        for index in df_temp.index:
            avg_price.append(np.average(df_temp['prices'][index]))
            min_price.append(np.amin(df_temp['prices'][index]))
            max_price.append(np.amax(df_temp['prices'][index]))
        
        # Create new columns with the result of the avg, max and min
        df_temp['avg'] = avg_price
        df_temp['min'] = min_price
        df_temp['max'] = max_price
        
        #print(df_temp)
    
        final_data = final_kpis(df_temp)
        
        return final_data