$(document).ready(
    function() {
        window.setInterval(
            function () {
                $.ajax({
                    url: $("#comments").data('url'),
                    success: function (response) {
                        $("#comments").html(response);
                    }
                })
            },
            2000
        )
    }
);
