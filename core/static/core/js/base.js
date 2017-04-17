$(document).ready(
    function () {

        $('.categories').chosen();

        function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", $('meta[name=csrf]').attr("content"));
                }
            }
        });

        $(".sign-in-button").on('click', function () {
            $.ajax({
                url: $(".sign-in-button").data('url'),
                success: function (response) {
                    $("#sign-in-content").html(response);
                }
            });
        })
    }
);
