from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractUser
from user.managers import UserManager


class User(AbstractUser):
    """Custom User Model."""
    email = models.EmailField(
        _('Email'), unique=True, blank=False, null=False,
        error_messages={
            'unique': _("A user with that email address already exists."),
        },
    )
    created_at = models.DateTimeField(_("Added"), auto_now_add=True)

    objects = UserManager()

    @property
    def full_name(self) -> str:
        return ' '.join([str(self.first_name), str(self.last_name)])

    def __str__(self) -> str:
        if self.full_name and len(self.full_name.strip()):
            return self.full_name
        return self.username

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ('first_name', 'last_name', 'username',)
