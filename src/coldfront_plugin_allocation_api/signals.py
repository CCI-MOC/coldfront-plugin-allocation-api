import os

from django.dispatch import receiver
from django_q.tasks import async_task

from coldfront.core.allocation.signals import (allocation_activate,
                                               allocation_activate_user,
                                               allocation_disable,
                                               allocation_remove_user)


@receiver(allocation_activate)
def activate_allocation_receiver(sender, **kwargs):
    allocation_pk = kwargs.get('allocation_pk')
    # Note(knikolla): Only run this task using Django-Q if a qcluster has
    # been configured.
    if os.getenv('REDIS_HOST'):
        # TODO: Django Q call to task
        pass
    else:
        # TODO: Call to task
        pass


@receiver(allocation_disable)
def allocation_disable_receiver(sender, **kwargs):
    allocation_pk = kwargs.get('allocation_pk')
    # TODO: Implement and call task


@receiver(allocation_activate_user)
def activate_allocation_user_receiver(sender, **kwargs):
    allocation_user_pk = kwargs.get('allocation_user_pk')
    # TODO: Implement and call task


@receiver(allocation_remove_user)
def allocation_remove_user_receiver(sender, **kwargs):
    allocation_user_pk = kwargs.get('allocation_user_pk')
    # TODO: Implement and call task
