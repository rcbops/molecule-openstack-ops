import os
import pytest
import testinfra.utils.ansible_runner


"""ASC-536: Perform Service Delivery Sign Off Tasks"""


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('os-infra_hosts')[:1]


@pytest.mark.test_id('ca13af99-5f93-11e8-8d43-6c96cfdb252f')
def test_pccommon(host):
    """Verify pccommon.sh runs without error"""
    pre = ("lxc-attach -n $(lxc-ls -1 | grep utility | head -n 1) "
           "-- bash -c '. /root/openrc ; ")
    post = "'"
    cmd = "{} source pccommon.sh {}".format(pre, post)
    result = host.run(cmd)

    assert result.rc == 0
