import logging

from django.core.management.base import BaseCommand
#from telegram.ext import Updater

from django_telegrambot.apps import DjangoTelegramBot


class Command(BaseCommand):

    def handle(self, *args, **options):

        from django_telegrambot.apps import DjangoTelegramBot

        DjangoTelegramBot().custom_ready()
