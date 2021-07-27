# from django.core.mail import send_mail
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# # from .models import Application


# @receiver(post_save, sender=Application)
# def create_employee_profile(sender, instance, created, **kwargs):
#     if created:
#         send_mail(
#             "Subject here",
#             "Here is the message.",
#             "from@example.com",
#             ["to@example.com"],
#             fail_silently=False,
#         )


# # @receiver(post_save, sender=Application)
# # def save_employee_profile(sender, instance, **kwargs):
# #     instance.employee.save()
