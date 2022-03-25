import datetime
from openpyxl import Workbook, load_workbook

# # from main import SessionLocal
# from create.tasks_list import create_tasks_list
# from create.policy import create_policy
# from create.object import create_object
# from create.tag import create_tag
# from create.event_tpl import create_event_tpl
# from create.event_to_policy import create_event_to_policy
# from create.event_to_object import create_event_to_object
# from create.event_to_tag import create_event_to_tag
# from read.tasks_list import read_task
# from read.event_tpl import read_event_tpl
# from read.policy import read_policy
# from read.object import read_object
# from read.tag import read_tag

from .models import (
    TasksList,
    VariantsList,
    EventTpl,
    Policy,
    Object,
    Tag,
    EventToObject,
    EventToPolicy,
    EventToTag,
)

# session = SessionLocal()
def process_sheet(wb):

    v = VariantsList(variant_name="Задание 1", KOD_name="Задание 1",
        date=datetime.datetime(2022, 2, 17),
        KOD_year="Задание 1")
    v.save()
    variant_id = v.id

    template_events = []
    sheet = wb["template"]

    row = 3
    curr_task_name = ""
    # curr_policy = ''

    while sheet["D" + str(row)].value != None:

        task_item = {}
        if sheet["A" + str(row)].value:
            curr_task_name = sheet["A" + str(row)].value
        # if sheet['B' + str(row)].value:
        #     curr_policy = sheet['B' + str(row)].value

        task_item["task_name"] = curr_task_name
        # task_item['policy'] = curr_policy
        task_item["file"] = sheet["D" + str(row)].value
        task_item["sender"] = sheet["E" + str(row)].value
        task_item["recipient"] = sheet["F" + str(row)].value
        task_item["policies"] = (
            sheet["G" + str(row)].value.split(",") if sheet["G" + str(row)].value else []
        )
        task_item["objects"] = (
            sheet["H" + str(row)].value.split(",") if sheet["H" + str(row)].value else []
        )
        task_item["verdict"] = sheet["I" + str(row)].value
        task_item["violation_level"] = (
            sheet["J" + str(row)].value if sheet["J" + str(row)].value else ""
        )
        task_item["tag"] = sheet["K" + str(row)].value

        template_events.append(task_item)
        row += 1

    # print(template_events)

    # create list of tasks
    tasks = [event["task_name"] for event in template_events]
    tasks = set(tasks)

    for task in tasks:
        t = TasksList(task_name=task, variant_id=v)
        t.save()

    # create list of policies, objects
    policies = []
    objects = []

    for task in template_events:
        if task["policies"]:
            policies.extend(task["policies"])
        if task["objects"]:
            objects.extend(task["objects"])
    policies = set(policies)
    objects = set(objects)

    for policy in policies:
        if policy:
            p = Policy(policy_name=policy)
            p.save()

    for object in objects:
        if object:
            o = Object(object_name=object)
            o.save()

    # create list of tags
    tags = [event["tag"] for event in template_events]
    tags = set(tags)

    for tag in tags:
        if tag:
            t = Tag(tag_name=tag)
            t.save()

    # create list of event_templates
    # create event_to_tag, event_to_object, event_to_tag
    for event in template_events:
        print("\n")
        print(event)

        e = EventTpl(
            task_id = TasksList.objects.get(task_name=event["task_name"]),
            sender=event["sender"],
            receiver=event["recipient"],
            file=event["file"],
            violation_level=event["violation_level"],
            verdict=event["verdict"]
        )
        
        e.save()

        for policy in event["policies"]:
            etp = EventToPolicy(
                event_id=e, 
                policy_id=Policy.objects.get(policy_name=policy),
            )
            etp.save()

        for object in event["objects"]:
            eto = EventToObject(
                event_id=e, 
                object_id=Object.objects.get(object_name=object),
            )
            eto.save()

        if event["tag"]:
            ett = EventToTag(
                event=e, 
                tag=Tag.objects.get(tag_name=tag),
            )
            ett.save()
