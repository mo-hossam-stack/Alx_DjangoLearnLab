from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book

def run():
    book_ct = ContentType.objects.get_for_model(Book)

    can_view = Permission.objects.get(codename='can_view', content_type=book_ct)
    can_create = Permission.objects.get(codename='can_create', content_type=book_ct)
    can_edit = Permission.objects.get(codename='can_edit', content_type=book_ct)
    can_delete = Permission.objects.get(codename='can_delete', content_type=book_ct)

    editors, _ = Group.objects.get_or_create(name='Editors')
    viewers, _ = Group.objects.get_or_create(name='Viewers')
    admins, _ = Group.objects.get_or_create(name='Admins')

    editors.permissions.set([can_view, can_create, can_edit])
    viewers.permissions.set([can_view])
    admins.permissions.set([can_view, can_create, can_edit, can_delete])
