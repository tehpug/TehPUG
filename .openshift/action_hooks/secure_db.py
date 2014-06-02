import sys, os

repo_dir = os.path.join(os.environ.get('OPENSHIFT_REPO_DIR'), 'wsgi')
sys.path.insert(0, repo_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'tehpug.settings'
username = 'admin'
email = 'k1.hedayati93@gmail.com'

from django.db.utils import IntegrityError

try:
    from django.contrib.auth.models import User
    password = User.objects.make_random_password()
    user = User.objects.create_user(username, email, password)
    user.is_staff = True
    user.is_superuser = True
    user.save()

    print 'Admin User: {}, Password: {}'.format(username, password)
except IntegrityError:
    pass
