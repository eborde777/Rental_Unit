function get_state_cities(){
    new Ajax.Request('/posts/ajax_purpose_state/', {
        method: 'post',
        parameters: $H({'state':$('id_state').getValue()}),
        onSuccess: function(place) {
            var e = $('id_cities')
            if (place.responseText){
                e.update(place.responseText)
            }
        }
    });
}