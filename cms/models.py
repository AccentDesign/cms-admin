from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.search import SearchVectorField
from django.core.validators import RegexValidator
from django.db import models

change_frequencies = (
    ("never", "never"),
    ("yearly", "yearly"),
    ("monthly", "monthly"),
    ("weekly", "weekly"),
    ("daily", "daily"),
    ("hourly", "hourly"),
    ("always", "always"),

)
page_types = (
    ("general", "general"),
    ("listing", "listing"),
    ("search", "search"),
)
path_validator = RegexValidator(
    r"^[a-z0-9]+(?:[.-][a-z0-9]+)*$",
    "A path is a sequence of lowercase alphanumeric characters and dashes separated by dots.",
    "invalid",
)


class HtmlField(models.TextField):
    pass


class TagsField(ArrayField):
    pass


class MetaMixin(models.Model):
    meta_description = models.CharField(
        max_length=320,
        blank=True,
        null=True,
    )
    meta_og_site_name = models.CharField(
        max_length=320,
        blank=True,
        null=True,
    )
    meta_og_title = models.CharField(
        max_length=320,
        blank=True,
        null=True,
    )
    meta_og_description = models.CharField(
        max_length=320,
        blank=True,
        null=True,
    )
    meta_og_url = models.URLField(
        max_length=320,
        blank=True,
        null=True,
    )
    meta_og_type = models.CharField(
        max_length=320,
        blank=True,
        null=True,
    )
    meta_og_image = models.URLField(
        max_length=320,
        blank=True,
        null=True,
    )
    meta_og_image_secure_url = models.URLField(
        max_length=320,
        blank=True,
        null=True,
    )
    meta_og_image_width = models.CharField(
        max_length=320,
        blank=True,
        null=True,
    )
    meta_og_image_height = models.CharField(
        max_length=320,
        blank=True,
        null=True,
    )
    meta_article_publisher = models.CharField(
        max_length=320,
        blank=True,
        null=True,
    )
    meta_article_section = models.CharField(
        max_length=320,
        blank=True,
        null=True,
    )
    meta_article_tag = models.CharField(
        max_length=320,
        blank=True,
        null=True,
    )
    meta_twitter_card = models.CharField(
        max_length=320,
        blank=True,
        null=True,
    )
    meta_twitter_image = models.CharField(
        max_length=320,
        blank=True,
        null=True,
    )
    meta_twitter_site = models.CharField(
        max_length=320,
        blank=True,
        null=True,
    )
    meta_robots = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True


class PageMixin(models.Model):
    path = models.CharField(
        max_length=500,
        blank=True,
        validators=[path_validator],
        unique=True,
    )
    title = models.CharField(
        max_length=160,
    )
    page_type = models.CharField(
        max_length=100,
        choices=page_types,
        default="general",
    )
    tags = TagsField(
        models.CharField(max_length=100),
        default=list,
        blank=True,
    )
    categories = TagsField(
        models.CharField(max_length=100),
        default=list,
        blank=True,
    )
    featured_image = models.URLField(
        max_length=320,
        blank=True,
    )
    is_in_sitemap = models.BooleanField()
    is_searchable = models.BooleanField()
    no_cache = models.BooleanField()
    change_frequency = models.CharField(
        max_length=100,
        choices=change_frequencies,
        default="weekly",
    )
    priority = models.DecimalField(
        decimal_places=1,
        max_digits=2,
        default=0.5,
    )
    level = models.GeneratedField(
        db_persist=True,
        expression=None,
        output_field=models.TextField(),
    )
    url = models.GeneratedField(
        db_persist=True,
        expression=None,
        output_field=models.TextField(),
    )
    search_vector = models.GeneratedField(
        db_persist=True,
        expression=None,
        output_field=SearchVectorField(),
    )
    full_text = models.GeneratedField(
        db_persist=True,
        expression=None,
        output_field=models.TextField(),
    )
    created_at = models.GeneratedField(
        db_persist=True,
        expression=None,
        output_field=models.DateTimeField(),
    )
    updated_at = models.GeneratedField(
        db_persist=True,
        expression=None,
        output_field=models.DateTimeField(),
    )
    published_at = models.DateTimeField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.path or "root"

    def date_created(self):
        return self.created_at.date()

    def date_updated(self):
        return self.updated_at.date()

    def date_published(self):
        return self.published_at.date()


class Page(PageMixin, MetaMixin):
    class Meta:
        managed = False
        db_table = "page"
        ordering = ["level", "path"]
        verbose_name_plural = "page"


class PageHtml(PageMixin, MetaMixin):
    html = HtmlField()

    class Meta:
        managed = False
        db_table = "page_html"
        ordering = ["level", "path"]
        verbose_name_plural = "page html"


class Settings(MetaMixin):
    site_root_url = models.CharField(max_length=160, blank=True, null=True)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)

    class Meta:
        managed = False
        db_table = "settings"
        verbose_name_plural = "settings"

    def __str__(self):
        return "settings"
