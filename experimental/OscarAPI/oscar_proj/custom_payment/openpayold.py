import requests
import lxml.etree
import datetime
import json


def handle_response(xml_root=None):
    root = xml_root
    final_response = dict()
    for value in root:
        if value.text is not None:
            final_response[value.tag] = value.text
    return final_response


def check_postal_code(postal_code):
    if len(str(postal_code)) == 4:
        return postal_code
    else:
        raise TypeError("Postal code should be of length 4")


def check_date_format(date_val):
    if date_val is not None:
        try:
            if datetime.datetime.strptime(date_val, "%d %b %Y"):
                return date_val
            else:
                raise TypeError()
        except TypeError as e:
            print(e)


class Client(object):

    def __init__(self, jam_auth_token=None, auth_token=None, plan_id=None, price=None, jam_retailer_order_no=None,
                 jam_first_name=None, jam_other_names=None, jam_family_name=None, jam_email=None, jam_address1=None,
                 jam_address2=None, jam_date_of_birth=None, jam_suburb=None, jam_state=None, jam_postcode=None,
                 jam_delivery_date=None, callback_url=None, cancel_url=None, failure_url=None):
        """
        :param jam_auth_token: Jam Auth Token from Merchant
        :param auth_token: Auth Token from Merchant
        :param plan_id: Plan ID comes from Openpay server
        :param price: Product Purchase Price
        :param jam_retailer_order_no: Merchant order no.
        :param jam_first_name: Client first name
        :param jam_family_name: Client family name
        :param jam_other_names: Client middle names
        :param jam_email: Client Email ID
        :param jam_address1: Client physical address (line 1) as it would be known to the credit checking authority.
                                                                                This is typically their home address.
        :param jam_address2: Client physical address (line 2).
        :param jam_date_of_birth: Client DOB. Format: dd mmm yyyy Example: 15 Jan 2018.
        :param jam_suburb: Client physical suburb.
        :param jam_state: The state for the address (e.g. VIC, NSW, etc).
        :param jam_postcode: The postcode for the client address. Format: NNNN (zero-padded to the left).
        :param jam_delivery_date: Format: dd mmm yyyy. Example: 15 Jan 2018.
        """
        self.jam_auth_token = jam_auth_token
        self.auth_token = auth_token
        self.plan_id = plan_id
        self.price = price
        self.JamRetailerOrderNo = jam_retailer_order_no
        self.JamFirstName = jam_first_name
        self.JamOtherNames = jam_other_names
        self.JamFamilyName = jam_family_name
        self.JamEmail = jam_email
        self.JamAddress1 = jam_address1
        self.JamAddress2 = jam_address2
        self.JamDateOfBirth = jam_date_of_birth
        self.JamSuburb = jam_suburb
        self.JamState = jam_state
        self.JamPostcode = jam_postcode
        self.JamDeliveryDate = jam_delivery_date
        self.JamCallbackURL = callback_url
        self.JamCancelURL = cancel_url
        self.JamFailURL = failure_url

    def new_online_order(self, purchase_price=None, plan_creation_type=None):
        """
        :param purchase_price: Product Purchase Price
        :param plan_creation_type: Based on this flag, plan will be created as pending capture.
        :return: Order status and Plan ID
        """
        if plan_creation_type is not None:
            payload = "<NewOnlineOrder>" \
                      "<JamAuthToken>{}</JamAuthToken>" \
                      "<AuthToken>{}</AuthToken>" \
                      "<PurchasePrice>{}</PurchasePrice>" \
                      "<PlanCreationType>{}</PlanCreationType>" \
                      "</NewOnlineOrder>".format(self.jam_auth_token, self.auth_token, purchase_price,
                                                 plan_creation_type
                                                 )

        else:
            payload = "<NewOnlineOrder>" \
                      "<JamAuthToken>{}</JamAuthToken>" \
                      "<AuthToken>{}</AuthToken>" \
                      "<PurchasePrice>{}</PurchasePrice>" \
                      "</NewOnlineOrder>".format(self.jam_auth_token, self.auth_token, purchase_price)
        # print(payload)
        url = "https://retailer.myopenpay.com.au/ServiceTraining/JAMServiceImpl.svc/NewOnlineOrder"
        headers = {'Content-Type': "application/xml"}
        response = requests.request("POST", url, data=payload, headers=headers)
        xml_response = response.text
        root = lxml.etree.fromstring(xml_response)
        resp = handle_response(xml_root=root)
        self.plan_id = resp.get('PlanID')
        self.price = purchase_price
        return resp

    def create_merchant_demographic_info(self, order_id=None, first_name=None, family_name=None, email=None, dob=None,
                                         address_1=None, address_2=None, suburb=None, state=None, postcode=None,
                                         delivery_date=None):
        """
        :param order_id: Merchant order ID
        :param first_name: Client first name
        :param family_name: Client family name
        :param email: Client Email ID
        :param dob: Client Date-of-birth
        :param address_1: Client address line 1
        :param address_2: Client address line 2
        :param suburb: Client suburb
        :param state: Client state
        :param postcode: Client Postal code
        :param delivery_date: Client delivery date
        :return:
        """
        self.JamRetailerOrderNo = order_id
        self.JamFirstName = first_name
        self.JamFamilyName = family_name
        self.JamEmail = email
        self.JamAddress1 = address_1
        self.JamAddress2 = address_2
        self.JamDateOfBirth = check_date_format(dob)
        self.JamSuburb = suburb
        self.JamState = state
        self.JamPostcode = check_postal_code(postcode)
        self.JamDeliveryDate = check_date_format(delivery_date)
        return self.__dict__

    def set_callback_url(self, callback_url=None, cancel_url=None, failure_url=None):
        """
        :param callback_url: A URL where we will redirected after successful payment through Openpay.
        :param cancel_url: A URL where we will redirected after cancel payment through Openpay.
        :param failure_url: A URL where we will redirected after unsuccessful payment through Openpay.
        :return: client object
        """
        self.JamCallbackURL = callback_url
        self.JamCancelURL = cancel_url
        self.JamFailURL = failure_url
        return self.__dict__

    def create_online_plan(self):
        url = "https://retailer.myopenpay.com.au/WebSalesTraining/"
        querystring = {
            "JamCallbackURL": self.JamCallbackURL,
            "JamCancelURL": self.JamCancelURL,
            "JamFailURL": self.JamFailURL,
            "JamAuthToken": self.jam_auth_token,
            "JamPlanID": self.plan_id,
            "JamRetailerOrderNo": str(self.JamRetailerOrderNo),
            "JamPrice": str(self.price),
            "JamFirstName": self.JamFirstName,
            "JamFamilyName": self.JamFamilyName,
            "JamEmail": self.JamEmail,
            "JamAddress1": self.JamAddress1,
            "JamSuburb": self.JamSuburb,
            "JamState": self.JamState,
            "JamPostcode": str(self.JamPostcode)
        }
        headers = {
            'Cache-Control': "no-cache",
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        return response.url

    def check_order_capture(self, plan_id):
        url = "https://retailer.myopenpay.com.au/ServiceTraining/JAMServiceImpl.svc/OnlineOrderCapturePayment"

        payload = "<OnlineOrderCapturePayment>" \
                  "<JamAuthToken>{}</JamAuthToken>" \
                  "<AuthToken>{}</AuthToken>" \
                  "<PlanID>{}</PlanID>" \
                  "</OnlineOrderCapturePayment>".format(self.jam_auth_token, self.auth_token, plan_id)
        headers = {
            'Content-Type': "application/xml",
            'cache-control': "no-cache",
        }

        response = requests.request("POST", url, data=payload, headers=headers)
        xml_response = response.text
        root = lxml.etree.fromstring(xml_response)
        # reason = root.find('reason')
        # # if reason.text:
        resp = handle_response(xml_root=root)
        return resp

    def check_order_status(self, plan_id):
        url = "https://retailer.myopenpay.com.au/ServiceTraining/JAMServiceImpl.svc/OnlineOrderStatus"
        payload = "<OnlineOrderStatus>" \
                  "<JamAuthToken>{}</JamAuthToken>" \
                  "<AuthToken>{}</AuthToken>" \
                  "<PlanID>{}</PlanID>" \
                  "</OnlineOrderStatus>".format(self.jam_auth_token, self.auth_token, plan_id)
        headers = {
            'Content-Type': "application/xml",
            'Cache-Control': "no-cache",
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        xml_response = response.text
        root = lxml.etree.fromstring(xml_response)
        # reason = root.find('reason')
        # # if reason.text:
        resp = handle_response(xml_root=root)
        return resp

    def refund(self, plan_id, new_purchase_price=0.00, full_refund=False):
        # removing conflicting of logic between new price and full_refund
        if full_refund:
            new_purchase_price = 0.00
        url = "https://retailer.myopenpay.com.au/ServiceTraining/JAMServiceImpl.svc/OnlineOrderReduction"

        payload = "<OnlineOrderReduction>" \
                  "<JamAuthToken>{}</JamAuthToken>" \
                  "<AuthToken>{}</AuthToken>" \
                  "<PlanID>{}</PlanID>" \
                  "<NewPurchasePrice>{}</NewPurchasePrice>" \
                  "<FullRefund>{}</FullRefund>" \
                  "</OnlineOrderReduction>".format(self.jam_auth_token, self.auth_token, plan_id, new_purchase_price,
                                                   full_refund)
        headers = {
            'Content-Type': "application/xml",
            'Cache-Control': "no-cache"
        }

        response = requests.request("POST", url, data=payload, headers=headers)
        xml_response = response.text
        root = lxml.etree.fromstring(xml_response)
        resp = handle_response(xml_root=root)
        return resp

    def order_dispatch_plan(self, plan_id):
        url = "https://retailer.myopenpay.com.au/ServiceTraining/JAMServiceImpl.svc/OnlineOrderDispatchPlan"
        payload = "<OnlineOrderDispatchPlan>" \
                  "<JamAuthToken>{}</JamAuthToken>" \
                  "<PlanID>{}</PlanID>" \
                  "</OnlineOrderDispatchPlan>".format(self.jam_auth_token, plan_id)
        headers = {
            'Content-Type': "application/xml",
            'Cache-Control': "no-cache"
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        xml_response = response.text
        root = lxml.etree.fromstring(xml_response)
        resp = handle_response(xml_root=root)
        return resp

    def timely_status(self, jam_auth_token):
        url = "https://integration.dev.myopenpay.com.au/JamServiceImpl.svc/RetailerPlanInformation"

        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache"
        }
        payload = {"AuthToken": "155f5b95-a40a-4ae5-8273-41ae83fec8c9"}
        response = requests.request("POST", url, data=payload, headers=headers)
        return response.text

    def max_min_purchase(self, auth_token):
        url = "https://retailer.myopenpay.com.au/ServiceTraining/JAMServiceImpl.svc/RetailerPlanInformation"
        payload = '{"AuthToken": ' + auth_token + '}'
        headers = {
            'Content-Type': "application/json",
            'cache-control': "no-cache",
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        response = json.loads(response.text)
        max_price, min_price = (response["RetailerPlanPeriods"][0]["MaxPurchasePrice"]), (
        response["RetailerPlanPeriods"][0]["MinPurchasePrice"])
        return ({"max_price": max_price, "min_price": min_price})
