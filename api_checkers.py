from api_parser import clean_json, get_parameters, log_file
from api_conf import ssl_verify
import requests
import json

def check_login(output):
    if 'Login or password does not match.' in output:
        return False
    elif 'Veuillez vous connecter' in output:
        return False
    return True

def log_user_with_login(params, session):
    try:
        payload = {'login': params['login'], 'password': params['password']}
        r = session.post('https://intra.epitech.eu/?format=json', data=payload, verify=ssl_verify)
        log_file("Intra logged user %s in %s seconds" %(params['login'], r.elapsed))
        return (check_login(clean_json(r.text)))
    except Exception as e:
        return json.dumps({"error": {"message": "Network error , the server couldn't reach Epitech's API", "code": 500}})

def log_and_check_params(mandatory_params, request):
    error = {}
    session = requests.Session()
    params = {}
    if request.get_json() and len(request.get_json()) > 0:
        params = request.get_json()
    elif request.form and len(request.form) != 0:
        params = request.form
    elif request.args and len(request.args) != 0:
        params = request.args
    for param in mandatory_params:
        if param not in params.keys():
            error = {"error": {"code": 400, "message": "Missing parameter : %s" %param}}
        if "login" and "password" in params.keys():
            if not log_user_with_login(params, session):
                error = {"error": {"code": 401, "message": "Invalid login/password combinaison"}}
        elif "token" in params.keys():
            session.cookies['PHPSESSID'] = params['token']
        else:
            error = {"error": {"code":401, "message":"No token or login/password"}}
    return error, session, params
