from django.db import models

from django.utils import timezone

class User(models.Model):
    # These fields tie to the roles!
    ADMIN = 1
    MANAGER = 2
    EMPLOYEE = 3

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (MANAGER, 'Manager'),
        (EMPLOYEE, 'Employee')
    )

    use_in_migrations = True
    user_email = models.TextField()
    password = models.CharField(max_length=10)
    user_name = models.TextField()
    phone = models.TextField()
    birth = models.TextField()
    address = models.TextField(blank=True)
    job = models.TextField()
    user_interests = models.TextField()
    token = models.TextField()
    # role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=3)

    def __str__(self):
        return f'{self.pk}'

    class Meta:
        db_table = "users"
        verbose_name = 'user'
        verbose_name_plural = 'users'

