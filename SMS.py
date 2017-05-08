from Kandy import *
#import pprint
#pp = pprint.PrettyPrinter(indent=4)

class SMS:
    domain_api_key = None
    domain_secret = None
    user_id = None

    user_access_token = None
    device_id = None


    #   Check user auth details
    def check_init_error(self, domain_api_key, domain_secret, user_id):
        if not domain_api_key:
            raise ValueError('Invalid domain key.')
        if not domain_secret:
            raise ValueError('Invalid domain secret.')
        if not user_id:
            raise ValueError('Invalid user ID.')



    #   Constructor
    def __init__(self, domain_api_key, domain_secret, user_id):
        self.check_init_error(domain_api_key, domain_secret, user_id)
        self.domain_api_key = domain_api_key
        self.domain_secret = domain_secret
        self.user_id = user_id


        #   Get user access token
        print("Getting User Access Token")
        data = User.get_user_access_token(self.domain_api_key, self.domain_secret, self.user_id)
        if data and data['status'] == 0 and data['result'] and data['result']['user_access_token']:
            self.user_access_token = data['result']['user_access_token']
            print("User Access Token: " + self.user_access_token)
        else:
            err = "Server replied with invalid User Access Token."
            raise ValueError(err)
        print('')

        #   Get device ID
        print("Getting Device ID")
        data = User.get_devices(self.user_access_token)
        if data and data['result'] and data['result']['devices'] and data['result']['devices'][0] and data['result']['devices'][0]['id']:
            self.device_id = data['result']['devices'][0]['id']
            print("Device ID: " + self.device_id)
        else:
            err = "Server replied with invalid User Access Token."
            raise ValueError(err)
        print('')


    #   Send SMS
    def send(self, source, destination, text):
        if not self.device_id:
            raise ValueError('Invalid device ID.')

        #   Actual sending
        print("Sending SMS")
        data = Device.send_sms(self.user_access_token, self.device_id, source, destination, text)
        if data and data['status'] == 0:
            print("SMS sent successfully!")
            return True
        else:
            err = "Could not send SMS."
            raise ValueError(err)



def main():
    domain_api_key = "<domain_api_key>"
    domain_secret = "<domain_secret>"
    user_id = "<user_id>"

    source_phone_number = "<source_phone_number>"
    destination_phone_number = "<destination_phone_number>"
    message = "<message>"

    try:
        sms = SMS(domain_api_key, domain_secret, user_id)
        sms.send(source_phone_number, destination_phone_number, message)
    except Exception as e:
      print('Error: ' + str(e))


if __name__ == "__main__":
    main()
