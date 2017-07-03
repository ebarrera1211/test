from django.db import models

# Create your models here.
class Board(models.Model):
    site = models.CharField(max_length=200)
    platform = models.CharField(max_length=200)
    revision = models.CharField(max_length=200)
    bmc_hostname = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    use = models.CharField(max_length=200)
    processors_number = models.CharField(max_length=200)
    silicon_rev = models.CharField(max_length=200)
    tdp = models.CharField(max_length=200)
    mem_config = models.CharField(max_length=200)
    pci = models.CharField(max_length=200)
    field = models.CharField(max_length=200)
    pxe = models.CharField(max_length=200)
    dvd = models.CharField(max_length=200)
    os = models.CharField(max_length=200)
    wombat_ip = models.CharField(max_length=200)
    rpi = models.CharField(max_length=200)
    pdu_info = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    comments = models.CharField(max_length=200)
    bmc_version = models.CharField(max_length=200)
    bmc_ip = models.CharField(max_length=200)

    def __str__(self):
        return self.bmc_hostname
