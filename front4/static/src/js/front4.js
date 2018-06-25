odoo.define('website_event.website_event', function (require) {

var ajax = require('web.ajax');
var Widget = require('web.Widget');
var web_editor_base = require('web_editor.base')
// https://www.odoo.com/documentation/11.0/reference/javascript.html#web_editor.base

// Catch registration form event, because of JS for attendee details
var EventRegistrationForm = Widget.extend({
    start: function() {
        var self = this;
        var res = this._super.apply(this.arguments).then(function() {
            $('#front4_form .front4-submit')
                .off('click')
                .removeClass('front4-submit')
                .click(function (ev) {
                    self.on_click(ev);
                });
        });
        return res
    },
    on_click: function(ev) {
        alert('otworz modal');
        ev.preventDefault();
        ev.stopPropagation();
        var $form = $(ev.currentTarget).closest('form'); // formularz z ktorego wywolanie
        var post = {};
        return ajax.jsonRpc($form.attr('action'), // akcja z formularza - wywolywana przez jsonRpc
                            'call', post).then(function (modal) {
                            alert('otwiera!');
            var $modal = $(modal); // dodanie ukrycia
            $modal.appendTo($form).modal();
            $modal.on('click', '.js_goto_event', function () {
                $modal.modal('hide');
            });
        });
    },
});

web_editor_base.ready().then(function(){
    var event_registration_form = new EventRegistrationForm().appendTo($('#front4_form'));
});

return { EventRegistrationForm: EventRegistrationForm };

});
