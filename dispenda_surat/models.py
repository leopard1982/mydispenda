from django.db import models
from django.contrib.auth.models import User, AbstractUser


class ExtendUser(AbstractUser):
    master_view = models.BooleanField(default=True)
    master_add = models.BooleanField(default=False)
    master_update = models.BooleanField(default=False)
    master_delete = models.BooleanField(default=False)
    approve_view = models.BooleanField(default=False)
    approve_add = models.BooleanField(default=False)
    approve_update = models.BooleanField(default=False)
    approve_delete = models.BooleanField(default=False)
    surattugas_view = models.BooleanField(default=True)
    surattugas_add = models.BooleanField(default=False)
    surattugas_update = models.BooleanField(default=False)
    surattugas_delete = models.BooleanField(default=False)
    laporan_view = models.BooleanField(default=True)
    laporan_add = models.BooleanField(default=False)
    laporan_update = models.BooleanField(default=False)
    laporan_delete = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    desc = models.CharField(max_length=256)
