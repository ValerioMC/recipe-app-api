"""
Wait for db docker-compose using only sleep
"""
from typing import Any

from django.core.management.base import BaseCommand
import time

class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any):
        time.sleep(7)