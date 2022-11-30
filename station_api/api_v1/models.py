import django.core.validators
import django.db.models
import django.utils.crypto
import django.utils.safestring


class Service(django.db.models.Model):
    token = django.db.models.CharField(
        verbose_name='API Token',
        unique=True,
        max_length=32,
        help_text=(
            '<a onclick="GenerateToken()">Generate new</a>'
            '<script>'
            'function GenerateToken() {'
            'const symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";'
            'let token = "api-insecure-";'
            'for (let i = 0; i < 18; i++) {'
            'token += symbols[Math.floor(Math.random() * symbols.length)];'
            'if (i == 6) token += "-";'
            '}'
            'document.getElementById("id_token").value = token;'
            '}'
            'if (!document.getElementById("id_token").value) GenerateToken();'
            '</script>'
        ),
        validators=(
            django.core.validators.RegexValidator(
                regex='api-insecure-[a-zA-Z0-9]{7}-[a-zA-Z0-9]{11}',
            ),
        )
    )
    
    name = django.db.models.CharField(
        verbose_name='Name',
        max_length=32,
        unique=True,
    )
    
    date = django.db.models.DateTimeField(
        verbose_name='Creation date',
        auto_now_add=True,
        editable=False,
    )
    
    class Meta:
        abstract = True


class Flight(Service):
    ...


class Station(Service):
    status = django.db.models.IntegerField(
        verbose_name='Station status',
        choices=(
            (0, 'Closed'),
            (1, 'Closing'),
            (2, 'Opening'),
            (3, 'Opened'),
        ),
        default=0,
    )
    
    charging = django.db.models.OneToOneField(
        verbose_name='Flight',
        to=Flight,
        on_delete=django.db.models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )
    
    aruco_marker = django.db.models.IntegerField(
        verbose_name='ArUco marker ID',
        unique=True,
    )
    
    def open_station(self) -> None:
        assert self.status == 0
        self.status = 2
    
    def set_opened(self) -> None:
        assert self.status == 2
        self.status = 3
    
    def close_station(self) -> None:
        assert self.status == 3
        self.status = 1
    
    def set_closed(self) -> None:
        assert self.status == 1
        self.status = 0
    
    def set_flight(self, flight: Flight) -> None:
        assert self.status == 3 and self.charging is None
        self.charging = flight
    
    def remove_flight(self, flight: Flight) -> None:
        assert self.status == 3 and self.charging == flight
        self.charging = None
    
    class Meta:
        verbose_name = 'charge station'
        verbose_name_plural = 'charge stations'
    
    def __str__(self) -> str:
        return f'Station id={self.id} name={self.name} status={self.status}'

    def show_token(self) -> str:
        return django.utils.safestring.mark_safe(
            f'<code id="show_btn_{self.id}">'
            f'<a onclick="document.getElementById(\'show_btn_{self.id}\').textContent = {self.token!r}"'
            '>show token</a>'
            '</code>'
        )
    
    show_token.short_description = 'API token'
    show_token.allow_tags = True
