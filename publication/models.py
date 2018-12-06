from django.db import models

# Create your models here.

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
