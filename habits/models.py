from django.db import models
from users.models import User
from django.urls import reverse


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='habits', default='')
    creator = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    time = models.TimeField()
    action = models.CharField(max_length=100)
    pleasant_habit = models.BooleanField(default=False)
    related_habit = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='related_habits')
    periodicity = models.CharField(max_length=100, default='daily')
    reward = models.CharField(max_length=100)
    time_required = models.DurationField()
    public = models.BooleanField(default=False)
    linked_habit = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='linked_habits')
    execution_time = models.DateTimeField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('habit-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.action

    def get_public_habits(self):
        return self.objects.filter(public=True)

    def get_user_habits(self, user):
        return self.objects.filter(creator=user)

    class Meta:
        permissions = (
            ('can_edit_habit', 'Can edit habit'),
            ('can_delete_habit', 'Can delete habit'),
        )
