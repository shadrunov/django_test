from django.db import models


class TasksList(models.Model):
    # task_id = models.IntegerField(primary_key=True, autoincrement=True)
    variant_id = models.ForeignKey('VariantsList', on_delete=models.CASCADE, blank=False)
    task_name = models.CharField(max_length=100, blank=False)


class VariantsList(models.Model):
    """Object in the course table in db.
    """

    # variant_id = models.IntegerField(primary_key=True, autoincrement=True)
    variant_name = models.CharField(max_length=100, blank=False)
    KOD_name = models.CharField(max_length=100, blank=False)
    date = models.DateField(blank=False)
    KOD_year = models.CharField(max_length=100, blank=False)
    

class EventTpl(models.Model):
    """Object in the lesson table in db.
    """

    # event_id = models.IntegerField(primary_key=True, autoincrement=True)
    task_id = models.ForeignKey('TasksList', on_delete=models.CASCADE, blank=False)
    sender = models.CharField(max_length=100, blank=False)
    receiver = models.CharField(max_length=100, blank=False)
    file = models.TextField(blank=False)
    violation_level = models.CharField(max_length=100, blank=False)
    verdict = models.CharField(max_length=100, blank=False)


class EventToPolicy(models.Model):
    """Object in the lesson_admins table in db.
    """

    # record_id = models.IntegerField(primary_key=True, autoincrement=True)
    event_id = models.ForeignKey('EventTpl', on_delete=models.CASCADE, blank=False)
    policy_id = models.ForeignKey('Policy', on_delete=models.CASCADE, blank=False)


class EventToObject(models.Model):
    """Object in the lesson_admins table in db.
    """

    # record_id = models.IntegerField(primary_key=True, autoincrement=True)
    event_id = models.ForeignKey('EventTpl', on_delete=models.CASCADE, blank=False)
    object_id = models.ForeignKey('Object', on_delete=models.CASCADE, blank=False)


class EventToTag(models.Model):
    """Object in the lesson_admins table in db.
    """

    # record_id = models.IntegerField(primary_key=True, autoincrement=True)
    event = models.ForeignKey('EventTpl', on_delete=models.CASCADE, blank=False)
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE, blank=False)
    # event_id = models.ForeignKey('EventTpl', on_delete=models.CASCADE, blank=False)
    # tag_id = models.ForeignKey('Tag', on_delete=models.CASCADE, blank=False)


class Policy(models.Model):
    """Object in the lesson_admins table in db.
    """

    # policy_id = models.IntegerField(primary_key=True, autoincrement=True)
    policy_name = models.CharField(max_length=100, blank=False)


class Object(models.Model):
    """Object in the lesson_admins table in db.
    """

    # object_id = models.IntegerField(primary_key=True, autoincrement=True)
    object_name = models.CharField(max_length=100, blank=False)


class Tag(models.Model):
    """Object in the lesson_admins table in db.
    """

    # tag_id = models.IntegerField(primary_key=True, autoincrement=True)
    tag_name = models.CharField(max_length=100, blank=False)
