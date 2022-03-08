# coldfront-plugin-allocation-api

[ColdFront](https://github.com/ubccr/coldfront) is a convenient resource allocation tool that provides a single point of entry for a multitude of systems. But what happens when a new application is added into an environment without ColdFront support? The ColdFront plugin and allocations API project aims to solve that issue by providing a centralized API service with a defined interface that allows developers to easily develop new plugins for ColdFront.

## Design

The ColdFront allocation API is a Django application that is intended to be used as a ColdFront plugin. This plugin allows the allocation API - and thus ColdFront -  to communicate with other systems in a generic fashion through additional application-specific plugins. Doing so simplifies the process of extending ColdFront to support additional applications, as the allocation API defines a clear interface for those plugins to implement. This interface handles:

* Creation of an allocation
* Removal of an allocation
* Creation of an user
* Removal of an user

The interface is a `signals.py` file that defines receivers that are called when ColdFront emits the matching signal.

Note that the allocation API could be integrated into the base ColdFront repository; however maintaining it as its own separate plugin allows for faster development and test cycles.

## Developing an Allocation Plugin

Developing an allocation plugin is straightforward using the [OpenStack plugin](https://github.com/nerc-project/coldfront-plugin-openstack) as a model. The key file is [`signals.py`](https://github.com/nerc-project/coldfront-plugin-openstack/blob/main/src/coldfront_plugin_openstack/signals.py), which defines the following receivers:

* `activate_allocation_receiver` - create an allocation
* `allocation_disable_receiver` - disable an allocation
* `activate_allocation_user_receiver` - create an allocation user
* `allocation_remove_user_receiver` - remove an allocation user

## Available Plugins

* [OpenStack plugin](https://github.com/nerc-project/coldfront-plugin-openstack)
* OpenShift plugin (**under development**)