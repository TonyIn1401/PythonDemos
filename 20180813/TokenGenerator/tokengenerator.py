#_*_ coding: utf-8 _*_
import requests
import urllib
import configparser
import json
import pyperclip
from urllib import parse

class TokenGenerator:
    def __init__(self):
        self.config_path = "C:\\WorkSpace\\Python\Repository\\20180813\\TokenGenerator\\config.ini"
        cf = configparser.ConfigParser()
        cf.read(self.config_path)

        self.gcdm_token_api = cf.get('gcdm', 'gcdm_token_api')
        self.gcdm_basic_token = cf.get('gcdm', 'gcdm_basic_token')
        self.gcdm_user = cf.get('gcdm', 'gcdm_user')
        self.gcdm_password = cf.get('gcdm', 'gcdm_password')

        self.btcapi_authorazation_type = cf.get('btcapi', 'btcapi_authorazation_type')
        self.gateway_token_api = cf.get('btcapi', 'btcapi_token_api')
        self.gateway_get_usid = cf.get('btcapi', 'btcapi_get_usid')

    def get_ini(self):
        cf = configparser.ConfigParser()
        cf.read("config.ini")
        print(self.gcdm_password)

    def get_token_from_gcdm(self):
        headers = {'Authorization': self.gcdm_basic_token, "ContentType": "application/x-www-form-urlencoded"}
        body = {"grant_type":"password","username":self.gcdm_user,"password":self.gcdm_password}
        r = requests.post(self.gcdm_token_api, headers=headers, data=body)
        if(r.status_code!=200):
            return None
        content = bytes.decode(r.content)
        json_obj = json.loads(content)
        return json_obj

    def get_token_from_btcapi(self, cac_json):
        if(cac_json == None):
            return "Cannot get gcdm token!!!"

        s = requests.session()
        headers_1 = {"User-Agent":"PostmanRuntime/7.2.0", "Postman-Token":"3aa4ed0a-91b2-4efc-966a-638849e157a4", "Cache-Control": "no-cache"}        
        gateway_response_for_state = s.get(self.gateway_token_api, headers=headers_1, allow_redirects=False)
        if(gateway_response_for_state.status_code != 302):
            return "Cannot get state from gateway!!!"

        location_with_state = gateway_response_for_state.headers["Location"]
        location_params = location_with_state.split('?')[1].split('&')
        redirectUrl = parse.unquote(list(filter(lambda x: not (x.find("redirect_uri") == -1), location_params))[0].split('=')[1])
        state = list(filter(lambda x: not (x.find("state=") == -1), location_params))[0]
        scope = list(filter(lambda x: not (x.find("scope=") == -1), location_params))[0]
        token = cac_json["access_token"]
        refresh = cac_json["refresh_token"]
        redict_url_1 = "{}?{}&{}&token={}&refresh={}".format(redirectUrl, scope, state, token, refresh)
        oauth_response = s.get(redict_url_1, allow_redirects=False)

        if(gateway_response_for_state.status_code != 302):
            return "Cannot validate gcdm token from gateway!!!"

        location_with_permission = oauth_response.headers["Location"]
        r4 = s.get(location_with_permission, allow_redirects=False)

        if(gateway_response_for_state.status_code != 302):
            return "Cannot get accesstoken from gateway!!!"

        redict_url_2 = r4.headers["Location"]
        access_token_str = redict_url_2[redict_url_2.find('#',1)+1:redict_url_2.find('&',1)]
        return access_token_str[access_token_str.find('=',1)+1:]

    def generate_token(self):
        gcdm_json = self.get_token_from_gcdm()
        ppStr = self.get_token_from_btcapi(gcdm_json)
        pyperclip.copy(ppStr)

if __name__ == '__main__':
    token_generator = TokenGenerator()
    token_generator.generate_token()    