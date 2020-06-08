# Copyright 2020 GRNET SA
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from unittest import mock

import reactive.watcher_dashboard_handlers as handlers

import charms_openstack.test_utils as test_utils


class TestRegisteredHooks(test_utils.TestRegisteredHooks):

    def test_hooks(self):
        defaults = [
            'charm.installed',
            'config.changed',
            'update-status',
            'upgrade-charm']
        hook_set = {
            'when': {
                'dashboard_available': (
                    'dashboard.available',),
            },
        }
        # test that the hooks were registered via the
        # reactive.watcher_dashboard_handlers
        self.registered_hooks_test_helper(handlers, hook_set, defaults)


class TestWatcherDashboardHandlers(test_utils.PatchHelper):

    def setUp(self):
        super().setUp()
        self.watcher_dashboard_charm = mock.MagicMock()
        self.patch_object(handlers.charm, 'provide_charm_instance',
                          new=mock.MagicMock())
        self.provide_charm_instance().__enter__.return_value = \
            self.watcher_dashboard_charm
        self.provide_charm_instance().__exit__.return_value = None
        self.patch('charms.reactive.endpoint_from_flag')

    def test_dashboard_available(self):
        mock_flag = mock.Mock()
        self.endpoint_from_flag.return_value = mock_flag
        self.watcher_dashboard_charm.purge_packages = ['n1']
        self.watcher_dashboard_charm.packages = ['p1', 'p2']
        handlers.dashboard_available()
        self.watcher_dashboard_charm.assess_status.assert_called_once_with()
        mock_flag.publish_plugin_info.assert_called_once_with(
            "", None, conflicting_packages=['n1'],
            install_packages=['p1', 'p2'])
