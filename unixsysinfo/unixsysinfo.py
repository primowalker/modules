'''
The unixsysinfo module provides easy access to the most common Linux types of system information. 
The module can be imported with the import statement:

import unixsysinfo

This module uses only standard Python modules so no third party modules need to be added to
the system for this module to work.

This module should work with Python 2.6 and up.
'''

from __future__ import absolute_import
import platform
import pwd
import grp
import commands
from itertools import islice

# Get basic system info
node = platform.node()
dist_linux = platform.linux_distribution()
dist_solaris = platform.platform()
arch = platform.architecture()
kernel_linux = platform.release()
kernel_solaris = platform.version()
release_solaris = platform.release()

# Get disk info
df = commands.getoutput('df -k')
fstab_linux = commands.getoutput('cat /etc/fstab')
fdisk_linux = commands.getoutput('fdisk -l | grep /dev/')
vfstab_solaris = commands.getoutput('cat /etc/vfstab')
format_solaris = commands.getoutput('echo | format')
metastat_solaris = commands.getoutput('metastat')


# Get LVM information
pvs_linux = commands.getoutput('pvs')
vgs_linux = commands.getoutput('vgs')
lvs_linux = commands.getoutput('lvs')
vxdisk_list_solaris = commands.getoutput('vxdisk list')
cfgadm_solaris = commands.getoutput('cfgadm -la')

# Get networking info
ifconfig_linux = commands.getoutput('ifconfig')
ifconfig_solaris = commands.getoutput('ifconfig -a')
ifconfig_aix = commands.getoutput('ifconfig -a')
ipaddr_linux = commands.getoutput('ip addr show')
iproute_linux = commands.getoutput('ip route')
routes_solaris = commands.getoutput('netstat -r')
routes_aix = commands.getoutput('netstat -r')
ipneigh_linux = commands.getoutput('ip neigh show')
ntpq_linux = commands.getoutput('ntpq -p  2')

# Get running processes
def ps():
	ps = commands.getstatusoutput("ps -ef")
	for proc in ps:
		print (proc)

# Get CPU info
cpuinfo_linux = commands.getoutput("cat /proc/cpuinfo | grep processor | wc -l")
cpuinfo_solairs = ('Placholder - Fix This!')
cpuinfo_aix = ('lsdev | grep Processor | wc -l')

# Get Memory info
def meminfo_linux():
	mem_info = commands.getoutput("cat /proc/meminfo")
	lines = mem_info.splitlines()
	iterator = islice(lines, 2)
	for i in iterator:
		print (i)
meminfo_solaris = commands.getoutput('prtconf | grep Memory')
meminfo_aix = commands.getoutput('lsattr -El sys0 -a realmem | awk '{size = $2/1024/1024 ; print " Total Free Memory " "\t" size" GB"}'`

# Print all the users and their login shells
def user():
	users = pwd.getpwall()
	for user in users:
		print('{0}:{1}:{2}:{3}'.format(user.pw_name, user.pw_uid, user.pw_gid, user.pw_shell))

# Print all the groups
def group():
	groups = grp.getgrall()
	for group in groups:
		print('{0}:{1}:{2}'.format(group.gr_name, group.gr_gid, group.gr_passwd))

# Get shadow file info
shadow = commands.getoutput('cat /etc/shadow')

# Get crontab information
crontabs_linux = commands.getoutput('tail -n +1 -- /var/spool/cron/tabs/*')
crontabs_solaris = ('Placholder - Fix This!')
crontabs_aix = ('Placholder - Fix This!')

# Uptime, reboots, system crashes
uptime = commands.getoutput('uptime')
reboots = commands.getoutput('last | head -10')
crashes = commands.getoutput('last | grep crash')

# Messages and dmesg issues
dmesg = commands.getoutput('dmesg | grep -i \'(err|warn|fail)\' | grep -iv \'(interrupt|override)\'')
messages_linux = commands.getoutput('cat /var/log/messages | grep -i \'(err|warn|fail)\' | grep -iv \'(interrupt|override|vas|syslog)\'')
messages_solaris = commands.getoutput('cat /var/adm/messages | grep -i \'(err|warn|fail)\' | grep -iv \'(interrupt|override|vas|syslog)\'')