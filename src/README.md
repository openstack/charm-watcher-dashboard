# Overview

This subordinate charm provides the Watcher Dashboard plugin for use with the OpenStack Dashboard.

OpenStack Ussuri or later is required.

# Usage

Example minimal deploy:

    juju deploy openstack-dashboard --config openstack-origin=cloud:bionic-ussuri
    juju deploy watcher-dashboard
    juju add-relation \
        openstack-dashboard:dashboard-plugin watcher-dashboard:dashboard

# Bugs

Please report bugs on [Launchpad][lp-bugs-charm-watcher-dashboard].

For general questions please refer to the OpenStack [Charm Guide][cg].

# Contact Information

Though this will be listed in the charm store itself don't assume a user will
know that, so include that information here:

## OpenStack Watcher

- [Watcher][wiki-watcher]
- [Watcher Bugs][lp-bugs-watcher]
- Watcher IRC on freenode at #openstack-watcher

<!-- LINKS -->

[cg]: https://docs.openstack.org/charm-guide
[lp-bugs-charm-watcher-dashboard]: https://bugs.launchpad.net/charm-watcher-dashboard/+filebug
[lp-bugs-watcher]: https://launchpad.net/watcher
[wiki-watcher]: https://wiki.openstack.org/wiki/Watcher
