#Ambulance Booking App
To build and run the application follow these step:-

`$ sudo docker-compose build`

=>  Go to the directory where your docker file is and run the command to build the list of container which is included in the docker-compose.yml.


`$ sudo docker-compose up`

=>  Go to the directory where your docker file is and run the command to run those containers which is mention in the docker-compose.yml.

You could face few problems related to database.

1.  You may have to run makemigration and migrate. To do that open a seperate terminal while your docker container running and run these commands.

`$ sudo docker-compose exec django python3 manage.py makemigrations`

`$ sudo  docker-compose exec django python3 manage.py migrate`

To create a superuser execute the following command:

`$ sudo docker-compose exec django python3 manage.py createsuperuser`

**Pgadmin4:** To setup pgadmin4 follow this steps.
```
Url: http://127.0.0.1:5050
Email: pgadmin@mail.com
Password: pgadmin

```

After login you need to create a server with the following options:

```
General:
	Name: test_server
Connection:
	host: postgres (name of the docker postgres service which is mention in docker-compose.yml)
	port: 5432
	maintenance database: postgres
	username: admin
```

##API Listing

All the APIs for Ambulance booking app will be mentioned and discussed below.

####1. Sign Up
```
base_url: http://182.75.72.148:8089/api/
url: http://182.75.72.148:8089/api/signup/
method: post
request parameters:
        full_name : John Doe,
        user_phone : 91-9876779989
        user_email : john@xyz.com
        password : Pass@12
response:
        {
          "status": true,
          "message": "Successfully signed up.OTP generated and sent to registered phone number.",
        }
```

####2. OTP Verification
```
base_url: http://182.75.72.148:8089/api/
url: http://182.75.72.148:8089/api/signup_otp_verification/
method: post
request parameter:
        otp : 1898
        user_phone : 91-9876779989
        user_email : john@xyz.com
        device_type : android or ios or web
        device_token : token for push notification
response:
        {
          "status": true,
          "message": "Successfully verified.",
           "data":{
            "access_token" : "abcd@123ABX...",
            "full_name" : "John Doe",
            "profile_picture" : "",
            "user_email" : "john@xyz.com",
            "user_phone" : "9836430000",
            "country_code" : "91",
            "rating": 0
          }
        }
```

####3. SIgn In
```
base_url: http://182.75.72.148:8089/api/
url: http://182.75.72.148:8089/api/login/
method: post
request parameter:
        user_id(email/phone): john@xyz.com
        password : Pass@12
        device_type: ios or android or web
        device_token : token of a device , will be used for push notification
response:
        {
          "status": true,
          "message": "Successfully logged in.",
          "data":{
            "access_token" : "abcd@123ABX...",
            "full_name" : "John Doe",
            "profile_picture" : "",
            "user_email" : "john@xyz.com",
            "user_phone" : "9836430644",
            "country_code" : "91",
            "rating": 4
          }
        }
```

####4. Forget Password
```
base_url: http://182.75.72.148:8089/api/
url: http://182.75.72.148:8089/api/forget_password/
method: post
request parameter:
        user_email : john@xyz.com
        user_phone : 9836430000
response:
        {
          "status": true,
          "message": "Successfully sent mail to registered email id.Check mail."
        }
```
****Note:** At least one field is mandatory; either email or phone or both. 

####5. Get All Ambulance Type
```
base_url: http://182.75.72.148:8089/api/
url: http://182.75.72.148:8089/api/get_ambulance/
method: post
request parameter:
            In header -> access_token
            In body ->
            lat_pick_up : "44.968046"
            lng_pick_up : "-94.420307"
            lat_destination : "44.9680467"
            lng_destination : "-94.420307"
            ambulance_type : "all"/"als"
            schedule_time : timeStampNow/timeStampLater
response:
        {
          "status": true,
          "message": "Successfully got the price details.",
           "data":{
             "arr_ambulance" : [
               { 
                 ambulance_type : "als",
                 ambulance_data : "Advance Life Support",
                 ambulance_minprice : "50.53",
                 ambulance_maxprice : "60.23",
                 currency : "₹"
               },
                 {
                 ambulance_type : "bls",
                 ambulance_data : "Basic Life Support",
                 ambulance_minprice : "50.53",
                 ambulance_maxprice : "60.23",
                 currency : "₹"
               },
                 {
                 ambulance_type : "pt",
                 ambulance_data : "Patient Transport",
                 ambulance_minprice : "50.53",
                 ambulance_maxprice : "60.23",
                 currency : "₹"
               }
               ] 
          }
        }
```
