import time,os,paramiko
import urllib2
import commands

def do_check_status(thunder):
    return u"ok"

def do_install(ip, hypervisor):
    ruidossh = paramiko.SSHClient()
    ruidossh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ruidossh.connect("10.60.1.4",username="root",password="temporal",key_filename="/home/aboldu/rhyns/rhyns/key")
    time.sleep(1)
    ruidossh.exec_command("unlink /tftpboot/pxelinux")
    time.sleep(1)
    if (hypervisor == "xen"):
      #XEN
      ruidossh.exec_command("ln -s abiquoxen /tftpboot/pxelinux")
    elif (hypervisor == "kvm"):
      #KVM
      ruidossh.exec_command("ln -s abiquokvm /tftpboot/pxelinux")
    elif (hypervisor == "xenserver"):
      #XenServer
      ruidossh.exec_command("ln -s xenserver /tftpboot/pxelinux")
    elif (hypervisor == "esxi"):
      #ESXi
      ruidossh.exec_command("ln -s esxi /tftpboot/pxelinux")
    elif (hypervisor == "vbox"):
      #VirtualBox
      #Abiquo V2V
      ruidossh.exec_command("ln -s abiquovbox /tftpboot/pxelinux")
    else:
	  pass
    os.system("ipmitool -U root -H "+ip+" -P temporal chassis bootdev pxe")
    os.system("ipmitool -U root -H "+ip+" -P temporal chassis power reset")

def do_poweron(thunder):
    os.system("ipmitool -U root -H "+thunder.ipmiip+" -P temporal chassis power on")

def do_poweroff(thunder):
    os.system("ipmitool -U root -H "+thunder.ipmiip+" -P temporal chassis power off")

def do_reboot(thunder):
    os.system("ipmitool -U root -H "+thunder.ipmiip+" -P temporal chassis power reset")

def do_check_hypervisor(thunder):
    hv = "unknown"
    try:
      api_hv = urllib2.urlopen("http://mothership/nodecollector/"+thunder.ip+"/hypervisor/").read()
    except urllib2.HTTPError:
      return u"unknown"
    if ("kvm" in api_hv):
        hv = u"kvm"
    elif ("xenserver" in api_hv):
        hv = u"xenserver"
    elif ("vmx" in api_hv):
        hv = u"esxi"
    elif ("hyperv" in api_hv):
        hv = u"hyperv"
    elif ("xen" in api_hv):
        hv = u"xen"
    return hv

def do_check_power(thunder):
    return (commands.getoutput("ipmitool -U root -H "+thunder.ipmiip+" -P temporal chassis status | grep 'System Power' | awk '{print $4}' " ) )





