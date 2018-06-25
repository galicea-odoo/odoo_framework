odoo.debug = true;

odoo.define('demo_js.akcja', function (require) {
 'use strict';


  var core = require('web.core');
  var Widget = require('web.Widget');


 var MyWidget1 = Widget.extend({
//    template: "myWidget1",

        start: function() {
            alert('Hello World!');
        }
 });

 core.action_registry.add("myaction1", MyWidget1);

});
