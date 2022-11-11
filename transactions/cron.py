from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django_cron import CronJobBase, Schedule

from transactions.services import get_summary_report


class SendSummaryReports(CronJobBase):
    RUN_AT_TIMES = ['18:47']
    RETRY_AFTER_FAILURE_MINS = 1
    schedule = Schedule(run_at_times=RUN_AT_TIMES,
                        retry_after_failure_mins=RETRY_AFTER_FAILURE_MINS)
    code = 'transactions.send_mail'

    def do(self):
        for user in User.objects.all():
            incomes, expenses = get_summary_report(user)
            msg_plain = render_to_string('summary_report.txt', {
                                         'username': user, 'incomes': incomes, 'expenses': expenses})
            send_mail(
                f'{user} New transactions report',
                f"{msg_plain}",
                'app@mailhog.com',
                ['test@mailhog.com'],
                fail_silently=False, )
