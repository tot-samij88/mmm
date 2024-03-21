import pyotp
from auths.models import ExmoneyUser, TwoFA_keys

 
def creating_token(request):
    """Генерація секретного токену та QR-коду"""
    try:
        username = request.data['data']['username']
    except KeyError:
        return {'error':'enter user_id key'}
    secret = pyotp.random_base32() # генерація токену
    try:
        new_token = TwoFA_keys.objects.create(
            user = ExmoneyUser.objects.get(username=username),
            secret = secret
        )
    except Exception as err:
        return {'error': str(err)}
        
    img = (f'otpauth://totp/Exmoney({ExmoneyUser.objects.get(username=username)})?secret={secret}')
    
    return {'users_token': secret, 'url': img}


def check_approved_otp(user):
    username = user['username']
    otp = user['otp']
    user = ExmoneyUser.objects.get(username=username)
    secret = TwoFA_keys.objects.filter(user=user).first()
    return pyotp.TOTP(str(secret)).verify(otp)


def checking_tokens_otp(request):
    """Перевірка достовірності одноразового паролю"""
    username = request.data['data']['username']
    otp = int(request.data['data']['otp'])
    # Костиль
    user = ExmoneyUser.objects.get(username=username)
    secret = TwoFA_keys.objects.filter(user=user).first()
    # secret = TwoFA_keys.objects.raw("SELECT id, secret FROM two_factor_auth_twofa_keys WHERE user_id=%s", [user_id])[0]
    
    if pyotp.TOTP(str(secret)).verify(otp):
        tfa = TwoFA_keys.objects.filter(user=user).first()
        tfa.approved = True
        tfa.save()
        return {'result': True}
    else: 
        return {'result': False}
