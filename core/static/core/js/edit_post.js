$(document).ready(
    function () {
        $(document).on('submit', '.ajaxform', function () {
            $.ajax({
                url: $(this).data('url'),
                type: 'POST',
                data: $(this).serialize(),
                success: function (response) {
                    if (response.success == true) {
                        $('input[type=text], textarea').val('');
                        location.reload(true);
                    }
                }
            });
            return false;
        });

        $(document).on('submit', '.ajaxform-comment', function () {
            $.ajax({
                url: $(this).data('url'),
                type: 'POST',
                data: $(this).serialize(),
                success: function (response) {
                    if (response.success === 'true') {
                        $('input[type=text], textarea').val('');
                    }
                }
            });
            return false;
        });

        $("#edit-button").on('click', function () {
            $.ajax({
                url: $("#edit-area").data('url'),
                success: function (response) {
                    $("#edit-area").html(response);
                }
            });
        });

        $("#cancel").on('click', function () {
            $.ajax({
                url: $(this).data('url'),
                success: function (response) {
                    $("#edit-area").html(response);
                }
            });
        });

        $("button.ajax-like").on('click', function() {
            $.ajax({
                url: $("button.ajax-like").data('url'),
                type: 'POST',
                success: function (response) {
                    var postId = $("button.ajax-like").data('postid');
                    $("#likes-" + postId).html(response.number);
                    if (response.status === 'set') {
                        $("button.ajax-like").html('-');
                    } else {
                        $("button.ajax-like").html('+');
                    }
                }
            });
            return false;
        });

    }
);
