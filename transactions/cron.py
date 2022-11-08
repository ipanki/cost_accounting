from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models import Sum
from django_cron import CronJobBase, Schedule

from .models import Transaction


class SendMail(CronJobBase):
    RUN_AT_TIMES = ['9:00']
    RETRY_AFTER_FAILURE_MINS = 1
    schedule = Schedule(run_at_times=RUN_AT_TIMES,
                        retry_after_failure_mins=RETRY_AFTER_FAILURE_MINS)
    code = 'manager.send_mail'

    def do(self):
        for user in User.objects.all():
            report = Transaction.objects.filter(user=user).values(
                'tags', 'tags__name', 'income').annotate(total=Sum('sum'))
            send_mail(
                'New transactions report',
                f"{report} ",
                'shadyc49@gmail.com',
                [f'{user.email}'],
                fail_silently=False, )
