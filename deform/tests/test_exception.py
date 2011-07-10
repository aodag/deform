import unittest

class TestValidationFailure(unittest.TestCase):
    def _makeOne(self, field, cstruct, error):
        from deform.exception import ValidationFailure
        return ValidationFailure(field, cstruct, error)

    def test_render(self):
        widget = DummyWidget()
        form = DummyForm(widget)
        cstruct = {}
        e = self._makeOne(form, cstruct, None)
        result = e.render()
        self.assertEqual(result, cstruct)

    def test_get_widget_resources(self):
        widget = DummyWidget()
        form = DummyForm(widget)
        form.widget_resources = {"js": "this is resources"}
        cstruct = {}
        e = self._makeOne(form, cstruct, None)
        resources = e.get_widget_resources()
        self.assertEqual(resources, {"js": "this is resources"})

class DummyForm(object):
    def __init__(self, widget):
        self.widget = widget
    def get_widget_resources(self):
        return self.widget_resources

class DummyWidget(object):
    def serialize(self, field, cstruct):
        return cstruct
    
