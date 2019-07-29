from CryptoTest.FernetTest import FernetTest
from CryptoTest.SimpleCryptTest import SimpleCryptTest
from CryptoTest.KeyGenerator import KeyGenerator
from RegexTest.reg_test import RegTest
from ZipcodeCheck.zip_codes_check import ZipcodesCheck
from DateTimeCheck.date_time_check import DateTimeCheck

if __name__ == '__main__':

    #######################################

    list_of_json = [{'title':'abc'},{'title':'bc'},{'title':'bc'},{'title':'abc'}, {'title':'bc'}, {'title':'a'}]
    print(group_by_ss(list_of_json, 'title'))
    ######################################

    # dt = DateTimeCheck()
    # print(dt.format_hours_12(60))


    ########################################
    #z = ZipcodesCheck()
    #print(z.fetch_details_from_zip('00544'))
    #print(z.get_zip_details_from_db('00544', z.connectDb()))
    #z.lib_zipcodes_sanity_check_list()

    #print(z.fetch_details_using_zip_country())

    #print(z.find_lat_long('Abbeville'))

    ################################
    # r = RegTest()
    # pattern = r'[A-Za-z\d\!\@\#\$\%\^\&\*\(\)]{8,8}'
    # str = 'Abc#j5GS'
    # print(r.regtest(pattern,str))

    #############################
    # l = []
    # name = "PR"
    # l += name
    # print(l)

    # l = []
    # name = "PR"
    # # list += name
    # l = l + list(name)
    # print(l)

    ########################
    # s = SimpleCryptTest()
    # s.printTest()
    #
    # c = s.encryptTest()
    # print(c)
    #
    # f = FernetTest()
    # ci = f.encryptionTest()
    # print(ci)
    # print(FernetTest.token_storage)
    #
    # k = KeyGenerator()
    # print('8 char key:', k.generateKey(8))
    #
    # print('Mac Address:', k.gettingMacAddress())