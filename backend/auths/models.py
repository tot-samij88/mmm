from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import Permission
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
import random


class ExmoneyUserManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, phone, email, password=None):
        """
        Создает пользователя
        first_name,last_name,phone,email
        :var login -> str
        :var password -> str
        """
        # Проверка если login пустой, вызовет исключение
        if not username:
            raise ValueError('Користувач повинен бути з логіном')
        if not first_name:
            raise ValueError('Користувач повинен бути з іменем')
        if not last_name:
            raise ValueError('Користувач повинен бути з прізвищем')
        if not phone:
            raise ValueError('Користувач повинен бути з телефоном')
        if not email:
            raise ValueError('Користувач повинен бути з ел.поштою')

        # Создает екземпляр класса пользователя и присваетвает ему login
        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
        )
        # Добавляет в екземпляр класса пользователя password, используя встроеный метод абстракного класса set_password
        user.set_password(password)
        # Сохраняет екземпляр класса в бд. В качестве параметра принимает бд в которой сохранять
        user.save(using=self._db)
        # Возращаем екземпляр класса пользователя
        return user

    def create_superuser(self, username, first_name, last_name, phone, email, password=None):
        """
        Функция создает суперпользователя при команде сreatesuperuser
        """
        if not username:
            raise ValueError('Користувач повинен бути з логіном')
        if not first_name:
            raise ValueError('Користувач повинен бути з іменем')
        if not last_name:
            raise ValueError('Користувач повинен бути з прізвищем')
        if not phone:
            raise ValueError('Користувач повинен бути з телефоном')
        if not email:
            raise ValueError('Користувач повинен бути з ел.поштою')
        # Создает екземпляр класса пользователя и присваевает ему login и password
        user = self.create(username=username,
                           first_name=first_name,
                           last_name=last_name,
                           phone=phone,
                           email=email
                           )
        user.set_password(password)
        # Устанавливает поле is_admin -> True
        user.is_admin = True
        # Устанавливает поле is_superuser -> True
        user.is_superuser = True
        # user.is_allowed_to_add_client = True // Это как пример что можно сюда добавить что угодно

        # Сохраняет екземпляр класса в бд. В качестве параметра принимает бд в которой сохранять
        user.save(using=self._db)

        # Дает все разрашения суперпользователю
        for x in Permission.objects.all():
            user.user_permissions.add(x)
        # Возвращаем екземпляр класса пользователя
        return user


class ExmoneyUser(AbstractBaseUser, PermissionsMixin):
    # Екземпляр класа менеджера пользователя
    objects = ExmoneyUserManager()
    # Логин пользователя
    username = models.CharField(max_length=100, verbose_name='Логін', unique=True, db_index=True)
    first_name = models.CharField(max_length=40, verbose_name='Ім\'я')
    last_name = models.CharField(max_length=70, verbose_name='Прізвище')
    phone = models.CharField(max_length=100, verbose_name='Телефон', unique=True, db_index=True)
    email = models.CharField(max_length=100, verbose_name='Пошта', unique=True, db_index=True)
    promocode = models.CharField(verbose_name='Промокод', max_length=100, default='__')
    promo_count = models.IntegerField(verbose_name='Кількість промо-переходів', default=0)
    is_first_deposit = models.BooleanField(default=False, verbose_name='Чи був перший депозит')
    bonus_balanse = models.FloatField(default=0, verbose_name='Бонусний баланс')
    # Активен ли пользователь, ето требует система автентификации Django
    is_active = models.BooleanField(default=True, verbose_name='Активний')
    # Пользователь является админом? ето требует система аутентификации Django
    is_admin = models.BooleanField(default=False, verbose_name='Адміністратор')

    # Какое поле считать как username
    # МультиЛогин должен быть кастомный - https://stackoverflow.com/questions/31370118/multiple-username-field-in-django-user-model
    USERNAME_FIELD = 'username'

    # Какие поля обязательны при вызове команды createsuperuser
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'email']

    # Метод получения полного имени пользователя
    # Требует Django
    def get_full_name(self):
        return "{} {}".format(self.last_name, self.first_name)

    # Метод получения имени пользователя
    # Требует Django
    def get_short_name(self):
        return self.username

    # Репрезентация записи в str, перегрузка строеного метода класса
    def __str__(self):
        return self.get_full_name()

    @property
    def is_staff(self):
        # Is the user a member of staff?
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    # Служебный класс по метаданным модели(название, назначение, ...)

    class Meta:
        # Название модели в удобном формате
        # Еденичное
        verbose_name = 'Client'
        # Множественное
        verbose_name_plural = 'Clients'


@receiver(post_save, sender=ExmoneyUser)
def post_save_user_promocode(sender, instance, created, **kwargs):
    if created:
        lower = "abcdefghijklnoqprstuvwxyz"
        upper = "ABCDEFGHIJKLNOPQRSTUVWXYZ"
        numbers = "0123456789"
        string = lower + upper + numbers
        lenght = 8
        promocode = "".join(random.sample(string, lenght))
        print(f'{instance.username}{promocode}')
        instance.promocode = f'{instance.username}{promocode}'
        instance.save()


class TwoFA_keys(models.Model):
    # Модель для генерации двухфакторки
    user = models.ForeignKey(ExmoneyUser, on_delete=models.CASCADE)

    secret = models.CharField(verbose_name='Секретний токен', max_length=50)

    approved = models.BooleanField(
        verbose_name='Підтвердженний ?', default=False)

    date = models.DateTimeField(
        verbose_name='Дата створення токену', default=timezone.now)

    class Meta:
        ordering = ['-date', ]
        verbose_name = 'Секретний токен'
        verbose_name_plural = 'Секретні токени'

    def __str__(self):
        return str(self.secret)


TYPE_PAYMENT_METHOD = (
    (0, 'Не обрано',),
    (1, 'Крипто'),
    (2, 'Карта')
)


class PaymentMethod(models.Model):
    # Модель для хранения карточек или кошельков
    user = models.ForeignKey(ExmoneyUser, on_delete=models.CASCADE)

    type = models.IntegerField(
        choices=TYPE_PAYMENT_METHOD, verbose_name='Тип метода оплаты', default=0)

    card_number = models.CharField(
        verbose_name='Банківська карта', max_length=16, blank=True, null=True)

    wallet = models.CharField(verbose_name='Гаманець',
                              max_length=41, blank=True, null=True)

    is_published = models.BooleanField(
        verbose_name='Відображати ?', default=True)

    date = models.DateTimeField(
        verbose_name='Дата збереження методу оплати', default=timezone.now)

    class Meta:
        ordering = ['-date', ]
        verbose_name = 'Спосіб оплати'
        verbose_name_plural = 'Способи оплати'

    def __str__(self):
        if self.card_number:
            return str(self.card_number)
        else:
            return str(self.wallet)


class UsersLogins(models.Model):
    # Модель для хранения истории логинов пользователей
    user = models.ForeignKey(ExmoneyUser, on_delete=models.CASCADE)

    user_agent = models.CharField(
        verbose_name='User agent', max_length=255, blank=True)

    user_ip = models.CharField(
        verbose_name='User ip', max_length=22, blank=True)

    date = models.DateTimeField(
        verbose_name='Дата збереження методу оплати', default=timezone.now)

    class Meta:
        ordering = ['-date', ]
        verbose_name = 'Історія логіну'
        verbose_name_plural = 'Історії логінів'


class InvitedUsers(models.Model):
    invited_by = models.ForeignKey(ExmoneyUser, on_delete=models.CASCADE, related_name='invited_by')
    invited = models.ForeignKey(ExmoneyUser, on_delete=models.CASCADE, related_name='invited')
    date = models.DateTimeField(verbose_name='Дата реєстрації', default=timezone.now)
    bonus = models.FloatField(default=0, verbose_name='Нараховані бонуси')

    class Meta:
        ordering = ['-date', ]
        verbose_name = 'Запрошений користувачь'
        verbose_name_plural = 'Запрошені користувачі'

    def __str__(self):
        return str(self.invited_by) + " " + str(self.invited)


class ReferralBonuses(models.Model):
    first_level = models.FloatField(default=0, verbose_name='Процент першого рівня')
    second_level = models.FloatField(default=0, verbose_name='Процент другого рівня')
    third_level = models.FloatField(default=0, verbose_name='Процент третього рівня')
    fourth_level = models.FloatField(default=0, verbose_name='Процент четвертого рівня')
    fifth_level = models.FloatField(default=0, verbose_name='Процент п\'ятого рівня')
    
    class Meta:
        verbose_name = 'Бонусний процент'
        verbose_name_plural = 'Бонусні проценти'

    def __str__(self):
        return str('ReferralBonuses')
