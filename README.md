Role Name
=========

This is a simple test repo using the [molecule framework](https://molecule.readthedocs.io/en/latest/)
for deploying system state via [ansible](https://www.ansible.com/)
and validating that state using
[infratest](https://testinfra.readthedocs.io/en/latest/).

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: molecule-openstack-ops, x: 42 }

Generate Molecule Config from Ansible Dynamic Inventory
-------------------------------------------------------

The `moleculerize` tool will build molecule config files from a RPC-O Ansible dynamic inventory file. As a
prerequisite to using the `moleculerize` tool a dynamic inventory must be generated from a RPC-O build:

```
sudo su -
cd /opt/openstack-ansible/playbooks/inventory
./dynamic_inventory.py > /path/to/dynaic_inventory.json
```

Now you can generate a `molecule.yml` config file using the `moleculerize` tool:

```
moleculerize /path/to/dynaic_inventory.json
```


License
-------

Apache

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
