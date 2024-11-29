from django.contrib import admin

from cms import models as cms_models
from cms.widgets import HtmlEditor, TagsInput


class PageAdmin(admin.ModelAdmin):
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
        ("SEO", {
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
                "no_cache",
                "is_searchable",
            ],
        }),
        ("Page Structure", {
            "fields": [
                "url",
                "level",
            ],
        }),
        ("Timestamps", {
            "fields": [
                "published_at",
                "created_at",
                "updated_at",
            ],
        }),
        ("Search", {
            "fields": [
                "search_vector",
                "full_text",
            ],
        }),
    )
    formfield_overrides = {
        cms_models.TagsField: {"widget": TagsInput},
    }
    list_display = (
        "path",
        "title",
        "page_type",
        "is_searchable",
        "is_in_sitemap",
        "date_published",
    )
    list_filter = [
        "page_type",
        "is_searchable",
        "is_in_sitemap",
        "published_at",
    ]
    readonly_fields = (
        "level",
        "url",
        "search_vector",
        "full_text",
        "created_at",
        "updated_at",
    )
    save_as = True
    search_fields = ("path", "title", "page_type")


class PageHtmlAdmin(PageAdmin):
    fieldsets = (
        *PageAdmin.fieldsets,
        ("Content", {
            "fields": [
                "html",
            ],
        }),
    )
    formfield_overrides = {
        cms_models.HtmlField: {"widget": HtmlEditor},
        cms_models.TagsField: {"widget": TagsInput},
    }
    readonly_fields = PageAdmin.readonly_fields + ("page_type",)


class SettingsAdmin(admin.ModelAdmin):
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    fieldsets = (
        ("Basic Information", {
            "fields": [
                "site_root_url",
            ],
        }),
        ("SEO", {
            "fields": [
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
        ("Timestamps", {
            "fields": [
                "created_at",
                "updated_at",
            ],
        }),
    )


admin.site.register(cms_models.Page, PageAdmin)
admin.site.register(cms_models.PageHtml, PageHtmlAdmin)
admin.site.register(cms_models.Settings, SettingsAdmin)
