# Overview

This subordinate charm provides the Watcher Dashboard plugin for use with the OpenStack Dashboard.

# Usage

Example minimal deploy:

    juju deploy openstack-dashboard --config openstack-origin=cloud:bionic-ussuri
    juju deploy watcher-dashboard
    juju add-relation \
        openstack-dashboard:dashboard-plugin watcher-dashboard:dashboard

# Bugs

Please report bugs on [GitHub](https://github.com/grnet/charm-watcher-dashboard/issues).

For general questions please refer to the OpenStack [Charm Guide](https://docs.openstack.org/charm-guide/latest/).

# Contact Information

Though this will be listed in the charm store itself don't assume a user will
know that, so include that information here:

## OpenStack Watcher

- [Watcher](https://wiki.openstack.org/wiki/Watcher)
- [Watcher Bugs](https://launchpad.net/watcher)
- Watcher IRC on freenode at #openstack-watcher
