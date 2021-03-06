#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR {{ info.version }} ({{ info.filename }}) on {{ info.date }}.
#  {{ info.year }}, SMART Platforms.


import io
import unittest
import json
from {% if info.lowercase_import_hack %}{{ class|lower }}{% else %}{{ class }}{% endif %} import {{ class }}
from fhirdate import FHIRDate


class {{ class }}Tests(unittest.TestCase):
    def instantiate_from(self, filename):
        with io.open(filename, 'r', encoding='utf-8') as handle:
            js = json.load(handle)
        instance = {{ class }}(js)
        self.assertIsNotNone(instance, "Must have instantiated a test instance")
        return instance
    
{%- for tcase in tests %}
    
    def test{{ class }}{{ loop.index }}(self):
        inst = self.instantiate_from("{{ tcase.filename }}")
        self.assertIsNotNone(inst, "Must have instantiated a {{ class }} instance")
    {% for onetest in tcase.tests %}
    {%- if "str" == onetest.class %}
        self.assertEqual(inst.{{ onetest.path }}, "{{ onetest.value|replace('"', '\\"') }}")
    {%- else %}{% if "int" == onetest.class or "float" == onetest.class or "NSDecimalNumber" == onetest.class %}
        self.assertEqual(inst.{{ onetest.path }}, {{ onetest.value }})
    {%- else %}{% if "bool" == onetest.class %}
        {%- if onetest.value %}
        self.assertTrue(inst.{{ onetest.path }})
        {%- else %}
        self.assertFalse(inst.{{ onetest.path }})
        {%- endif %}
    {%- else %}{% if "FHIRDate" == onetest.class %}
        self.assertEqual(inst.{{ onetest.path }}.date, FHIRDate("{{ onetest.value }}").date)
        self.assertEqual(inst.{{ onetest.path }}.isostring, "{{ onetest.value }}")
    {%- else %}
        # Don't know how to create unit test for "{{ onetest.path }}", which is a {{ onetest.class }}
    {%- endif %}{% endif %}{% endif %}{% endif %}
    {%- endfor %}
{%- endfor %}


