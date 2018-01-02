from models import DummyList


def main():

    dummy_list = DummyList(50)
    for i in range(100): 
        dummy_list.next_year()
        dummy_list.find_wife()
        dummy_list.set_babies()
        # print "YEAR: {0}".format(dummy_list.year)
        dummy_list.summary() 

if __name__ == "__main__":
    main()
