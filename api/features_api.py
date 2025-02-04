# -*- coding: utf-8 -*-
# Copyright 2021 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License")
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import division
from __future__ import print_function

import logging

from framework import basehandlers
from framework import permissions
from framework import ramcache
from internals import models

class FeaturesAPI(basehandlers.APIHandler):
  """Features are the the main records that we track."""

  # TODO(jrobbins): do_get

  # TODO(jrobbins): do_post

  # TODO(jrobbins): do_patch

  @permissions.require_admin_site
  def do_delete(self, feature_id):
    """Delete the specified feature."""
    # TODO(jrobbins): implement undelete UI.  For now, use cloud console.
    feature = self.get_specified_feature(feature_id=feature_id)
    feature.deleted = True
    feature.put()
    ramcache.flush_all()

    return {'message': 'Done'}
