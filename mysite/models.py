from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

class CategoryCatalog(models.Model):

    class Meta:
        db_table = 'category'

    parent_cat = models.ForeignKey('CategoryCatalog', blank=True, null=True, default=None)
    title_cat = models.CharField(max_length=50, verbose_name='Name category')
    short_desc_cat = models.CharField(max_length=200, verbose_name='Short description')
    description_cat = models.TextField()
    image_cat = models.ImageField(
        upload_to='images/catalog_images',
        blank=True,
        null=True,
        default=None
    )

    def __str__(self):
        return self.title_cat

class Products(models.Model):

    class Meta:
        db_table = 'product'

    title_pro = models.CharField(max_length=150, verbose_name='Name product')
    code_pro = models.CharField(max_length=50, verbose_name='Code product')
    category_pro = models.ForeignKey('CategoryCatalog', verbose_name='Category product')
    manufactures_pro = models.ForeignKey('Manufactures', verbose_name='Manufacture product')
    descriptions_pro = models.TextField(verbose_name='Description')
    image_pro = models.ImageField(
        upload_to='images/product_images',
        blank=True,
        null=True,
        default=None
    )

    def __str__(self):
        return self.title_pro

class CategoryManufactures(models.Model):
    class Meta:
        db_table = 'category_manufactures'

    name_category_man = models.CharField(
        max_length=50,
        verbose_name='Name category manufactures'
    )
    parent_category_man = models.ForeignKey(
        'CategoryManufactures',
        verbose_name='Parent category manufactures',
        blank=True,
        null=True,
        default=None
    )

    def __str__(self):
        return self.name_category_man

class Manufactures(models.Model):
    class Meta:
        db_table = 'manufactures'

    title_man = models.CharField(max_length=100, verbose_name='Name manufacture')
    site_man = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        default=None,
        verbose_name='Site manufactures'
    )
    category_man = models.ManyToManyField(
        'CategoryManufactures',
        verbose_name='Category manufactures',
    )

    def __str__(self):
        return self.title_man


class CategoryArticle(models.Model):
    class Meta:
        db_table = 'category_article'

    title_cat = models.CharField(max_length=100, verbose_name='Name category')
    parent_cat = models.ForeignKey(
        'CategoryArticle',
        verbose_name='Parent category',
        blank=True,
        null=True,
        default=None
    )
    description_cat = models.TextField(
        verbose_name='Description category',
        blank=True,
        null=True,
        default=None
    )

    def __str__(self):
        return self.title_cat

class Article(models.Model):
    class Meta:
        db_table = 'article_content'

    title_article = models.CharField(max_length=100, verbose_name='Title article')
    category_article = models.ForeignKey('CategoryArticle', verbose_name='Category article')
    description_article = RichTextUploadingField(config_name='awesome_ckeditor')
    active_article = models.BooleanField(verbose_name='Active article', default=True)
    create_article = models.DateTimeField(verbose_name='Create data article', default=timezone.now)
    like = models.SmallIntegerField(default=0)

    def publish(self):
        self.create_article = timezone.now()
        self.save()

    def __str__(self):
        return self.title_article

class Comments(models.Model):
    class Meta:
        db_table = 'comments_article'

    comment_text = RichTextField(config_name='frontend', verbose_name='Comment')
    comment_article = models.ForeignKey(Article)