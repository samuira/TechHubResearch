from googlemaps import Client as GoogleMaps
import psycopg2
from pprint import pprint
import zipcodes
#import geonameszip

class ZipcodesCheck:


    def connectDb(self):
        try:
            conn = psycopg2.connect("dbname='branchspot_dev_db' "
                                    "user='branchspot' host='localhost' password='branchspot_dev_pass'")
            return conn
        except:
            print("I am unable to connect to the database")

    def get_zip_details_from_db(self, zipcode=None, conn=None):
        #conn = self.connectDb()
        zip_cur = conn.cursor()
        zip_cur.execute("""SELECT * from public.locations_zipcode where code = %s;""",(zipcode,))
        zip_cur_rows = zip_cur.fetchall()
        city_cur = conn.cursor()
        city_cur.execute("""SELECT * from public.locations_city where id = %s""", (zip_cur_rows[0][7],))
        city_cur_rows = city_cur.fetchall()
        state_cur = conn.cursor()
        state_cur.execute("""SELECT * from public.locations_state where id = %s""",(city_cur_rows[0][9],))
        state_cur_rows = state_cur.fetchall()
        return {'code': zip_cur_rows[0][6], 'city_name': city_cur_rows[0][7], 'state_name': state_cur_rows[0][4], 'state_abbreviation': state_cur_rows[0][5]}

    def is_zipcode_valid(self, zipcode=None):
        return zipcodes.is_valid(zipcode)

    def fetch_details_from_zip(self, zipcode=None):
        if not zipcodes.is_valid(zipcode):
            return {"message":'zipcode {} is not valid'.format(zipcode)}
        else:
            return zipcodes.matching(zipcode)

    def search_similer_zip_list(self, zipcode=None):
        if not zipcodes.is_valid(zipcode):
            return {"message": 'zipcode {} is not valid'.format(zipcode)}
        else:
            return pprint(zipcodes.similar_to(zipcode))

    # def fetch_details_using_zip_country(self, zipcode=None, country_code=None):
    #     return geonameszip.lookup_postal_code('77098', 'US')

    def find_lat_long(self, city_name):
        gmap_api_key = 'AIzaSyAN-T0GpRBmSzqAAx2n0W1GyZNfHy-wu7E'

        gmaps = GoogleMaps(gmap_api_key)

        try:
            result = gmaps.geocode(city_name)
            print(str(result).replace("'",'"'))
            formatted_address = result[0]['formatted_address']
            # print(formatted_address)
            placemark = result[0]['geometry']
        except:
            Msg = {"Message": "Invalid City name"}
            return Msg
        else:
            lat = placemark['location']['lat']  # Note these are backwards from usual
            lng = placemark['location']['lng']
            return formatted_address, lat, lng

    def lib_zipcodes_sanity_check_list(self):
        conn = self.connectDb()
        zip_cur = conn.cursor()
        zip_cur.execute("""SELECT * from public.locations_zipcode;""")
        zip_cur_rows = zip_cur.fetchall()
        check_list = []
        check_dict = {'code':'', 'city_name_check': False, 'state_name_check': False, 'state_abbreviation_check': False}
        city_t = 0
        city_f = 0
        state_t = 0
        state_f = 0
        for row in zip_cur_rows:
            try:
                check_dict['code'] = row[6]
                from_db_json = self.get_zip_details_from_db(row[6], conn)
                from_zipcodes_lib = self.fetch_details_from_zip(row[6])

                check_dict['city_name_check'] = True if from_db_json['city_name'].lower() == from_zipcodes_lib[0]['city'].lower() else False
                check_dict['state_abbreviation_check'] = True if from_db_json['state_abbreviation'].lower() == from_zipcodes_lib[0]['state'].lower() else False

                if check_dict['city_name_check']:
                    city_t +=1
                else:
                    city_f +=1

                if check_dict['state_abbreviation_check']:
                    state_t +=1
                else:
                    state_f +=1
                print('*******************************')
                print('city check true count:', city_t)
                print('city check false count:', city_f)
                print('state check true count:', state_t)
                print('state check false count:', state_f)
                check_list.append(check_dict)
            except Exception as e:
                pass
        print('#################################')
        print('actual count:', len(zip_cur_rows))
        print('check_list count:',len(check_list))
        print('city check true count:',city_t)
        print('city check false count:',city_f)
        print('state check true count:',state_t)
        print('state check false count:',state_f)
        #print(check_list)


