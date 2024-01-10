from django.db import models
from django.contrib.auth.models import User
from django_fsm import transition, FSMField
from .constants import TicketState
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name=_("User"))
    first_name = models.CharField(max_length=50, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=50, verbose_name=_("Last Name"))
    personal_id = models.IntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = _("Users")

    def __str__(self):
        return f'{self.personal_id}'


class ChatList(models.Model):
    user_one = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='user1_chats')
    user_two = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='user2_chats')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'چت ها'

    def __str__(self):
        return f'{self.id}'


class DirectMessages(models.Model):
    chat = models.ForeignKey(ChatList, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='messages')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'پیام ها'

    def __str__(self):
        return f'{self.id}'


class Ticket(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='tickets')
    message = models.TextField()
    answer = models.TextField(null=True, blank=True)
    state = FSMField(choices=TicketState.choices, default=TicketState.CREATED, protected=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'تیکت ها'

    def __str__(self):
        return f'{self.id}'

    @transition(field=state,
                source=TicketState.CREATED,
                target=TicketState.PENDING)
    def created_to_pending(self):
        pass

    @transition(field=state,
                source=TicketState.PENDING,
                target=TicketState.ANSWERED)
    def pending_to_answered(self):
        pass
