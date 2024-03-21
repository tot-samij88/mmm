import json
from auths.views import SetLoggingHistoryAPIView
from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from .models import ExmoneyUser, UsersLogins
from .serializers import RegisterSerializer, UserSerializer
from django.contrib.auth.models import User
# Register API


class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args,  **kwargs):
        promocode = json.loads(request.body).get("promocode")
        # Promocode не введен
        # # # # # 
        # # # # # 
        if not promocode or promocode == '':
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()

            # SetLoggingHistoryAPIView.post(self, request)
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
                username = json.loads(request.body).get("username")
            except KeyError:
                return Response({'error':'enter username key'})
            try:
                user_login = UsersLogins.objects.create(
                    user = ExmoneyUser.objects.get(username=username),
                    user_agent=client_user_agent,
                    user_ip=client_ip
                )
            except Exception as err:
                return Response({'error': str(err)})
            # SetLoggingHistoryAPIView.post(self, request)

            return Response({
                "user": UserSerializer(user,context=self.get_serializer_context()).data,
                "message": "User Created Successfully.  Now perform Login to get your token",
                "token": serializer.get_tokens(user),
            })
        else:
            check_promo = ExmoneyUser.objects.filter(promocode=promocode).first()
            # Корректный promocode
            if check_promo:
                check_promo.promo_count += 1
                check_promo.save()

                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                user = serializer.save()
                user.promo_count += 1
                user.save()
                # SetLoggingHistoryAPIView.post(self, request)
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
                    username = json.loads(request.body).get("username")
                except KeyError:
                    return Response({'error':'enter username key'})
                try:
                    user_login = UsersLogins.objects.create(
                        user = ExmoneyUser.objects.get(username=username),
                        user_agent=client_user_agent,
                        user_ip=client_ip
                    )
                except Exception as err:
                    return Response({'error': str(err)})
                # SetLoggingHistoryAPIView.post(self, request)
                SetLoggingHistoryAPIView.post(self, request)
                return Response({
                    "user": UserSerializer(user,context=self.get_serializer_context()).data,
                    "message": "User Created Successfully.  Now perform Login to get your token",
                    "token": serializer.get_tokens(user),
                })
            #  Не корректный promocode
            else:
                return Response({
                    "user": "promo incorrect",
                })
