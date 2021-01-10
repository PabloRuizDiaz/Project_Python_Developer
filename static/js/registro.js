$(document).ready(function(){
    $('.btn-send').click(function(e)
    {
        e.preventDefault();

        country = document.getElementById('country').value;

        var url = window.location.href

        $.post(url, {country: country},
            function(data) {
                $('#div_image').html('<img src="data:image/png;base64,' + data + '" />');      
                    
            }
        );
 
    });
});
