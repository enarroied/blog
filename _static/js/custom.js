// Add 'target=_blank' and 'rel=noopener noreferrer' to all external links
$(document).ready(function () {
    $('a[href^="http"]').attr({
        target: "_blank",
        rel: "noopener noreferrer"
    });
});
