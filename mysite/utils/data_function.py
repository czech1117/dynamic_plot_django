from random import randint

def create_data():
    data_length = 5
    data_list = []
    for id, data in enumerate(range(0, data_length)):
        data_list.append(
            {'id': id,
             'x': randint(0, 100),
             'y': randint(0, 100)
             }
        )

    return(data_list)