(function(){
    var $ = django.jQuery;
    $(document).ready(function(){
        $('input.tags-input').each(function(idx, el){
            const tagify = new Tagify(el, {
                originalInputValueFormat: valuesArr => valuesArr.map(item => item.value).join(',')
            });
        });
    });
})();