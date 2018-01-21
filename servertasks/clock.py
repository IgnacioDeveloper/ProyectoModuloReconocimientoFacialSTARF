from django.utils import timezone
from datetime import datetime, time
import json

class Reloj():

    @staticmethod
    def get_servidor_time():
        now = timezone.now()
        return now
