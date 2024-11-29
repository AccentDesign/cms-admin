from django.contrib import admin

from cms import models


class PageAdmin(admin.ModelAdmin):
    list_display = (
        "path",
        "title",
        "page_type",
        "created_at",
        "updated_at",
    )
    readonly_fields = (
        "level",
        "url",
        "search_vector",
        "full_text",
        "created_at",
        "updated_at",
        "published_at",
    )
    search_fields = ("path", "title", "page_type")
    fieldsets = (
        ("Basic Information", {
            "fields": [
                "path",
                "title",
                "page_type",
                "tags",
                "categories",
                "featured_image",
            ],
        }),
        ("SEO & Sitemap", {
            "fields": [
                "is_in_sitemap",
                "change_frequency",
                "priority",
                "meta_description",
                "meta_og_site_name",
                "meta_og_title",
                "meta_og_description",
                "meta_og_url",
                "meta_og_type",
                "meta_og_image",
                "meta_og_image_secure_url",
                "meta_og_image_width",
                "meta_og_image_height",
                "meta_article_publisher",
                "meta_article_section",
                "meta_article_tag",
                "meta_twitter_card",
                "meta_twitter_image",
                "meta_twitter_site",
                "meta_robots",
            ],
        }),
        ("Performance & Visibility", {
            "fields": [
                "is_searchable",
                "no_cache",
            ],
        }),
        ("Page Structure", {
            "classes": ("collapse",),
            "fields": [
                "url",
                "level",
            ],
        }),
        ("Timestamps", {
            "classes": ("collapse",),
            "fields": [
                "created_at",
                "updated_at",
                "published_at",
            ],
        }),
        ("Advanced Search Data", {
            "classes": ("collapse",),
            "fields": [
                "search_vector",
                "full_text",
            ],
        }),
    )


class PageHtmlAdmin(PageAdmin):
    readonly_fields = PageAdmin.readonly_fields + ("page_type",)
    fieldsets = (
        *PageAdmin.fieldsets,
        ("Specific", {
            "fields": ["html"],
        }),
    )


admin.site.register(models.Page, PageAdmin)
admin.site.register(models.PageHtml, PageHtmlAdmin)
admin.site.register(models.Settings, admin.ModelAdmin)
