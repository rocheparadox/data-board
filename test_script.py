#Author : Roche Christopher
#File created on 01 Aug 2019 7:39 PM

from data_board import data_board
import time

data_board_obj = data_board(20003, '0.0.0.0')

data_board_obj.start_server()

try:

    for i in range(50):
        print(i)
        time.sleep(1)
        data_board_obj.set_data(i)

    data_board_obj.stop_server()

except KeyboardInterrupt:
    data_board_obj.stop_server()