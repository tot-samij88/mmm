import json
from urllib import request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, PasswordField
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import exceptions, serializers
from .models import ExmoneyUser, InvitedUsers, PaymentMethod, ReferralBonuses, TwoFA_keys, UsersLogins
from .serializers import LoginHistorySerializer, PaymentMethodGettingCardSerializer, PaymentMethodGettingWalSerializer, PaymentMethodSavingSerializer
from .token_generator import check_approved_otp, creating_token, checking_tokens_otp
from .models import ExmoneyUser, PaymentMethod
from .serializers import PaymentMethodGettingCardSerializer, PaymentMethodGettingWalSerializer, PaymentMethodSavingSerializer
from .token_generator import creating_token, checking_tokens_otp
from rest_framework import status


class CheckAuthView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, ):
        return Response({'status': 'success'})


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields[self.username_field] = serializers.CharField()
        self.fields["password"] = PasswordField()
        self.fields["otp"] = serializers.CharField(allow_blank=True)

    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, user):
        data = super().validate(user)
        refresh = self.get_token(self.user)
        if refresh:
            ex_user = ExmoneyUser.objects.get(username=user['username'])
            is_tfa_approve = TwoFA_keys.objects.filter(
                user=ex_user, approved=True).first()
            if is_tfa_approve:
                if check_approved_otp(user):
                    return data
                return {'otp': True}
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class TwoFA_keysAvailableAPIView(APIView):
    """Перевірка наявності секретного токену у користувача"""

    # На посилання http://127.0.0.1:8000/api/token_check_available/ надіслати POST запит з тілом {"user_id": 1}
    def post(self, request):
        try:
            username = request.data['data']['username']
        except KeyError:
            return {'error': 'enter user_id key'}

        try:
            user = ExmoneyUser.objects.get(username=username)
            is_tfa = TwoFA_keys.objects.filter(user=user).first()
            is_tfa_approve = TwoFA_keys.objects.filter(
                user=user, approved=True).first()
            if is_tfa and is_tfa_approve:
                return Response({'is_tfa': True}, content_type="application/json")
            else:
                if is_tfa:
                    TwoFA_keys.objects.filter(user=user).delete()
                return Response({'is_tfa': False}, content_type="application/json")
        except Exception as err:
            return {'error': str(err)}


class TwoFA_keysAPIView(APIView):
    """Генерація та вивід секретного токену та QR-коду"""

    # На посилання http://127.0.0.1:8000/api/token_create/ надіслати POST запит з тілом {"user_id": 1}
    def post(self, request):
        result = creating_token(request)
        return Response(result, content_type="application/json")


class TwoFA_keysCheckAPIView(APIView):
    """Перевірка достовірності одноразового паролю. Повертає True/False"""

    # На посилання http://127.0.0.1:8000/auth/token_check/ надіслати POST запит з тілом {"username": 1, "otp": 333222}
    def post(self, request):
        result = checking_tokens_otp(request)
        return Response(result, content_type="application/json")


class PaymentMethodSetAPIView(APIView):
    """Збереження нового методу оплати"""

    # На посилання http://127.0.0.1:8000/auth/set_pay_meth надіслати POST запит з тілом {"username": 2, "type": "2", "card_number": "", "wallet": "wdwd3m2km3r"}

    def post(self, request):
        serializer = PaymentMethodSavingSerializer

        try:
            username = request.data['data']['username']
        except KeyError:

            return Response({'error': 'enter username key'})

        try:
            new_pay_method = PaymentMethod.objects.create(
                user=ExmoneyUser.objects.get(username=username),
                type=request.data['data']['type'],
                card_number=request.data['data']['card_number'],
                wallet=request.data['data']['wallet']

            )
        except Exception as err:
            return Response({'error': str(err)})
        return Response({'payment method created': f"{new_pay_method}"})


class PaymentMethodGetAPIView(APIView):
    """Отримання методу оплати"""
    # На посилання http://127.0.0.1:8000/auth/get_pay_meth надіслати POST запит з тілом {"user": 2, "type": 2}

    def post(self, request):
        try:
            types = request.data['data']['type']
            username = request.data['data']['username']
        except KeyError:
            return Response({'error': 'enter type or username key'})

        methods = PaymentMethod.objects.filter(user=ExmoneyUser.objects.get(
            username=username), type=types, is_published=True)

        if types == 2:
            answers = []
            carts = list(PaymentMethodGettingCardSerializer(
                methods, many=True).data)
            for i in carts:
                answer = {}
                answer.update({'card_number': i['card_number']})
                answers.append(answer)
            return Response(answers)
        elif types == 1:
            return Response({"methods": f"{PaymentMethodGettingWalSerializer(methods, many=True).data}"})


class PromoCodeGetAPIView(APIView):
    """Отримання промокоду"""
    # На посилання http://127.0.0.1:8000/auth/promocode надіслати POST запит з тілом {"username": 1}

    def post(self, request):
        try:
            data = json.loads(request.body)
            username = data['data']['username']
        except KeyError:
            return Response({'error': 'enter username key'})

        promocode = ExmoneyUser.objects.filter(
            username=username).values("promocode", "promo_count").first()
        data = {
            'promocode': promocode.get("promocode"),
            'promo_count': promocode.get("promo_count"),

        }
        return Response(json.dumps(data))


class UserInfo(APIView):
    """Отримання промокоду"""
    # На посилання http://127.0.0.1:8000/auth/user-info/ надіслати POST запит з тілом {"username": 1}

    def post(self, request):
        try:
            data = json.loads(request.body)
            username = data['data']['username']
        except KeyError:
            return Response({'error': 'enter username key'})

        get_user = ExmoneyUser.objects.filter(
            username=username).values("username",
                                      "first_name",
                                      "last_name",
                                      "phone",
                                      "email").first()
        payload = {
            'user': get_user
        }
        return Response(payload, status=status.HTTP_200_OK)


class SetLoggingHistoryAPIView(APIView):
    """Saving new logging info"""
    # На посилання http://127.0.0.1:8000/auth/set_logging_history POST запит з тілом {"username": "admin"}

    def post(self, request):

        client_user_agent = request.META['HTTP_USER_AGENT']
        client_ip = None

        remote_address = request.META.get('HTTP_X_REAL_IP')
        if remote_address:
            client_ip = remote_address
        elif request.META.get('REMOTE_ADDR'):
            client_ip = request.META.get('REMOTE_ADDR')
        else:
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            client_ip = x_forwarded_for.split(',')[-1].strip()

        try:
            data = json.loads(request.body)
            username = data['data']['username']
        except KeyError:
            return Response({'error': 'enter user_id key'})
        try:
            user_login = UsersLogins.objects.create(
                user=ExmoneyUser.objects.get(username=username),
                user_agent=client_user_agent,
                user_ip=client_ip
            )
        except Exception as err:
            return Response({'error': str(err)})

        return Response({'new login created': f"{user_login}"})


class GetLoggingHistoryAPIView(APIView):
    """Saving new logging info"""
    # На посилання http://127.0.0.1:8000/auth/get_logging_history POST запит з тілом {"username": "admin"}

    def post(self, request):
        try:
            data = json.loads(request.body)
            username = data['data']['username']
        except KeyError:
            return Response({'error': 'enter username key'})
        history = UsersLogins.objects.filter(
            user=ExmoneyUser.objects.get(username=username))
        history = list(LoginHistorySerializer(history, many=True).data)[:3]
        answers = []

        for i in history:
            answer = {}
            # answer.update({'user_agent': i['user_agent']})
            # answer.update({'user_ip': i['user_ip']})
            answer.update({'date': i['date']})
            answers.append(answer)

        return Response(answers)


class ReferalTestAPIView(APIView):
    """Referal program testig"""
    # На посилання http://127.0.0.1:8000/auth/ref_test надіслати POST запит з тілом {"username": 1, "sum": 2}
    # Вызывать при пополнении депозита пользователем. Передавать имя пользователя и сумму прибыли с завода депозита, которуб будут деребанить инвайтеры

    def post(self, request):
        try:
            data = json.loads(request.body)
            username = data['data']['username']
            sum = data['data']['sum']
        except KeyError:
            return Response({'error': 'enter username/sum key'})

        
        user = ExmoneyUser.objects.get(username=username)
        
        if user.is_first_deposit:
            return Response('It`s not a first deposit')
        else:
            # Referal program counter
            try:
                first_level_user = InvitedUsers.objects.get(invited=user).invited_by
                print(first_level_user)
            except Exception:
                # Пользователь зареган без инвайта
                first_level_user = False
            
            if not first_level_user:
                return Response('There is no first inviter')
            else:
                first_level_cof = ReferralBonuses.objects.first().first_level
                bonus_sum = sum / 100 * first_level_cof

                user.is_first_deposit = True
                user.save()
                first_level_user.bonus_balanse += bonus_sum
                first_level_user.save()

                first_level_user_bonus = InvitedUsers.objects.get(invited=user)
                first_level_user_bonus.bonus = bonus_sum
                first_level_user_bonus.save()

    
                data = {
                    "is_first_deposit": user.is_first_deposit,
                    "bonus_sum": bonus_sum,
                }
                return Response(data)
    