from django.db import models
from django.urls import reverse


class Project(models.Model):
    """
    Head Projectclass
    """
    name = models.CharField(max_length=255, unique=True, help_text="Уникальное имя проекта")

    created = models.DateField(null=True, blank=True)

    PROJECT_STATUS = (
        ('RUN', 'In progress'),
        ('PAUSE', 'Paused'),
        ('ENDED', 'Сompleted'),
    )
    status = models.CharField(max_length=8, choices=PROJECT_STATUS, blank=True, default='RUN', help_text='Статус проекта')

    class Meta:
        ordering = ["created", '-name']

    def __str__(self):
        return self.name


class PrivateCloudPassport(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name='private_cloud_technical_passport')
    content = models.TextField()

    def __str__(self):
        return f'Private Cloud Technical Passport for {self.project.name}'


class S3Passport(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name='s3_technical_passport')
    content = models.TextField()

    def __str__(self):
        return f'S3 Technical Passport for {self.project.name}'


class MinimalYaml(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name='minimal_yaml')
    content = models.TextField()

    def __str__(self):
        return f'Minimal YAML for {self.project.name}'


class ProjectDocuments(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_documents')
    name = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return f'Project Document {self.name} for {self.project.name}'

class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    SERVER = 'server'
    SWITCH = 'switch'
    STORAGE = 'storage'
    
    EQUIPMENT_TYPE_CHOICES = [
        (SERVER, 'Server'),
        (SWITCH, 'Switch'),
        (STORAGE, 'Storage'),
    ]
    
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='equipment')
    type = models.CharField(max_length=7, choices=EQUIPMENT_TYPE_CHOICES)
    model = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='equipment', null=True, blank=True)

    def __str__(self):
        return f'{self.model} ({self.get_type_display()})'


class Server(models.Model):
    equipment = models.OneToOneField(Equipment, on_delete=models.CASCADE, primary_key=True, related_name='server_details')
    cpu = models.CharField(max_length=255)
    ram = models.CharField(max_length=255)
    storage_capacity = models.CharField(max_length=255)
    operating_system = models.CharField(max_length=255)

    def __str__(self):
        return f'Server {self.equipment.model} details'


class Switch(models.Model):
    equipment = models.OneToOneField(Equipment, on_delete=models.CASCADE, primary_key=True, related_name='switch_details')
    port_count = models.IntegerField()
    throughput = models.CharField(max_length=255)
    layer = models.CharField(max_length=255)

    def __str__(self):
        return f'Switch {self.equipment.model} details'


class Storage(models.Model):
    equipment = models.OneToOneField(Equipment, on_delete=models.CASCADE, primary_key=True, related_name='storage_details')
    capacity = models.CharField(max_length=255)
    type = models.CharField(max_length=255)  # e.g., SSD, HDD
    raid_support = models.CharField(max_length=255)

    def __str__(self):
        return f'Storage {self.equipment.model} details'
