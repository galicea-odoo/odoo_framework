odoo.define('website_event.website_event', function (require) {

var ajax = require('web.ajax');
var Widget = require('web.Widget');
var web_editor_base = require('web_editor.base')
// https://www.odoo.com/documentation/11.0/reference/javascript.html#web_editor.base

var EventRegistrationForm = Widget.extend({
    start: function() {
        var self = this;
        var res = this._super.apply(this.arguments).then(function() {
            $('#front3_form .front3-submit')
                .off('click')
                .removeClass('front3-submit')
                .click(function (ev) {
                    self.on_click(ev);
                });
        });
        return res
    },
    on_click: function(ev) {
        alert('reakcja na przycisk');
    },
});

web_editor_base.ready().then(function(){
    var event_registration_form = new EventRegistrationForm().appendTo($('#front3_form'));
});

return { EventRegistrationForm: EventRegistrationForm };

});
