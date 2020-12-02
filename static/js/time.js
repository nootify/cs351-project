$(document).ready(function() {
    function getTime() {
        $.ajax({
            url: "/time",
            type: "get",
            success: function(response) {
                $("#time").html(response);
            },
            error: function(error) {
                console.error(`Could not retrieve time: ${error}`);
            }
        });
    }
    setInterval(getTime, 3000);
});
