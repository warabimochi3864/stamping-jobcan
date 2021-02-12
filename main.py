import requests

def main(event, context):

    clientId = event['clientId']
    email = event['email']
    password = event['password']
    group_id = event['groupId']
    login_url = 'https://ssl.jobcan.jp/login/mb-employee'
    stamping_url = 'https://ssl.jobcan.jp/m/work/simplestamp'

    # ログイン用情報
    login_data = {
        'client_id':clientId,
        'email':email,
        'password':password,
        'save_login_info':0,
        'url':'/m',
        'login_type':1,
        'lang_code':'ja'
    }

    # ログイン処理の実施
    request_session = requests.session()
    request_session.post(login_url, data=login_data)

    # cookieからセッションを取得
    cookie_sid_value = request_session.cookies.get("sid")

    # 打刻用項目の作成
    stamping_data = {
        'token':cookie_sid_value,
        'adit_item':'打刻',
        'gps':0,
        'group_id':group_id
    }

    # 打刻処理
    request_session.post(stamping_url, data=stamping_data)