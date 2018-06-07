.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
    :alt: License: AGPL-3

Fast Product Quantities Search
==============================

Currently search product by quantity is verry slow.
With this module search time is divided by ~ 200 (tested on 80k products).
For 80K products in databases, search product by quantity 
take ~ 6.6 mn (400 second). So odoo, compute quantities for each product and 
make filter in python side.
With this module product are filtred in one SQL request executed in 2 seconds.


Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/rwsdigital/odoo-stock-logistics-workflow/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed feedback.
