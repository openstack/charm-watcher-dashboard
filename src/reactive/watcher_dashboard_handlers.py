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

import charms.reactive as reactive

import charms_openstack.bus
import charms_openstack.charm as charm

charms_openstack.bus.discover()

# Use the charms.openstack defaults for common states and hooks
charm.use_defaults(
    'charm.installed',
    'config.changed',
    'update-status',
    'upgrade-charm')


@reactive.when('dashboard.available')
def dashboard_available():
    """Relation to OpenStack Dashboard principal charm complete.
    """
    with charm.provide_charm_instance() as watcher_dashboard_charm:
        dashboard_relation = reactive.endpoint_from_flag('dashboard.available')
        dashboard_relation.publish_plugin_info(
            "", None,
            conflicting_packages=watcher_dashboard_charm.purge_packages,
            install_packages=watcher_dashboard_charm.packages)
        watcher_dashboard_charm.assess_status()
