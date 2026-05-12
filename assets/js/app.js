// --------------------------------------------------
// APP.JS
// --------------------------------------------------

//
// Initialize Foundation
// --------------------------------------------------

$(document).foundation();

//
// Custom JS
// --------------------------------------------------

// WCAG AA: Update ARIA attributes when abstract toggles are activated
$(document).on('on.zf.toggler off.zf.toggler', '.abstract', function () {
    var abstractId = $(this).attr('id');
    var button = $('button[data-toggle="' + abstractId + '"]');
    var isVisible = $(this).is(':visible');
    button.attr('aria-expanded', isVisible);
    $(this).attr('aria-hidden', !isVisible);
});
