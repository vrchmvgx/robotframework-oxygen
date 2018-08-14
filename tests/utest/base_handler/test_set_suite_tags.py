import unittest
from oxygen.base_handler import BaseHandler
from unittest.mock import MagicMock
from yaml import load

class TestSetSuiteTags(unittest.TestCase):
  def setUp(self):
    with open('../config.yml', 'r') as infile:
      self._config = load(infile)
      self._object = BaseHandler(self._config['oxygen.zap'])

    self._suite = MagicMock()
    self._suite.set_tags = MagicMock()
    self._tags = (MagicMock(), MagicMock())

  def tearDown(self):
    pass

  def test_tags_are_set(self):
    self._object._set_suite_tags(self._suite, *self._tags)
    self._suite.set_tags.assert_called_once_with(self._tags)

if __name__ == '__main__':
  unittest.main()
