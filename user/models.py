from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User as auth_user

import datetime

# User-Related Models

class RoleManager(models.Manager):
    def check_role(self, data,data2):
        print("Went under check_roles")
        print(data,data2)
        try:
            Role.objects.get(user_id_id=data, publication_id=data2)
            return True
        except Role.DoesNotExist:
            return False


class Profile(models.Model):
    USER_TYPES = (
        ('u', 'User'),
        ('w', 'Webmaster')
    )
    user = models.OneToOneField(auth_user, on_delete=models.CASCADE, related_name='profile')
    user_type = models.CharField(max_length=1, choices=USER_TYPES, default='u')
    avatar = models.ImageField(blank=True, upload_to='storage/uploads/avatar/%Y/%m/%d/')
    bio = models.TextField(default='', blank=True)
    phone = models.CharField(max_length=20, blank=True, default='')
    birth_date = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=100, default='', blank=True)
    country = models.CharField(max_length=100, default='', blank=True)
    reputation = models.IntegerField(default=1)
    user_followers = models.ManyToManyField('Profile', related_name='follows',blank=True)
    subscriptions = models.ManyToManyField('Publication',blank=True,related_name='subcribers')

    def __str__(self):
        return str(self.user.username)

    def save(self, *args, **kwargs):
        if self.id and self.avatar:
            current_avatar = Profile.objects.get(pk=self.id).avatar
            if current_avatar != self.avatar:
                current_avatar.delete()
        super(Profile, self).save(*args, **kwargs)

    def is_user(self):
        return self.user_type == 'u'

    def is_webmaster(self):
        return self.user_type == 'w'

# Publication Models
class Publication(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    description = models.CharField(max_length=500, null=True, blank=True)
    cover = models.ImageField(blank=True, upload_to='storage/uploads/publication/covers/%Y/%m/%d/')
    created = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField('Category', blank=True)
    roles = models.ManyToManyField(auth_user, through='Role', symmetrical=False)
    slug = models.SlugField(max_length=40, unique=True)

    def save(self, *args, **kwargs):
        date = datetime.date.today().strftime('%y%m%d')
        self.slug = '%s-%s' % (
            slugify(self.name), date
        )

        super(Publication, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=40, unique=True)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return str(self.title)

# User/Publication Models
class Role(models.Model):
    ROLE_TYPES = (
        ('a', 'Administrator'),
        ('e', 'Editor'),
        ('m', 'Moderator'),
        ('s', 'Staff'),
        ('c', 'Contributor'),
        ('f', 'Follower'),
    )
    user_id = models.ForeignKey(auth_user, on_delete=models.CASCADE, null=True)
    publication = models.ForeignKey('Publication', blank=True, on_delete=models.CASCADE)
    role = models.CharField(max_length=1, choices=ROLE_TYPES, default='s')
    objects = RoleManager()

    def save(self, *args, **kwargs):
        print(self)
        super(Role, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.user_id)
