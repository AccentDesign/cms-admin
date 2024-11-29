from django.forms import Textarea, TextInput


class HtmlEditor(Textarea):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attrs["class"] = "html-editor"

    class Media:
        css = {
            "all": (
                "https://cdnjs.cloudflare.com/ajax/libs/codemirror/6.65.7/codemirror.css",
            )
        }
        js = (
            "https://cdnjs.cloudflare.com/ajax/libs/codemirror/6.65.7/codemirror.js",
            "https://cdnjs.cloudflare.com/ajax/libs/codemirror/6.65.7/mode/xml/xml.js",
            "https://cdnjs.cloudflare.com/ajax/libs/codemirror/6.65.7/mode/htmlmixed/htmlmixed.js",
            "cms/codemirror-6.65.7/init.js",
        )


class TagsInput(TextInput):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attrs["class"] = "tags-input"

    class Media:
        css = {
            "all": (
                "https://cdn.jsdelivr.net/npm/@yaireo/tagify@4.32.2/dist/tagify.css",
            )
        }
        js = (
            "https://cdn.jsdelivr.net/npm/@yaireo/tagify@4.32.2",
            "https://cdn.jsdelivr.net/npm/@yaireo/tagify@4.32.2/dist/tagify.polyfills.min.js",
            "cms/tagify-4.32.2/init.js",
        )