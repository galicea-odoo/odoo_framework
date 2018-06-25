odoo.debug = true;

odoo.define('demo_js.demo_js', function (require) {
 'use strict';


  var core = require('web.core');
  var Widget = require('web.Widget');


  var MyWidget0 = Widget.extend({
    template: "myWidget0",

    init: function (parent) {
       this._super(parent);
    },
 });

 core.form_custom_registry.add("mywidget0", MyWidget0);

});
