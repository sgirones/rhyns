import time,os,paramiko
import urllib2
import commands
import libvirt 

def do_check_status(thunder):
    return u"ok"

def do_install(ip, hypervisor):
    ruidossh = paramiko.SSHClient()
    ruidossh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ruidossh.connect("10.60.1.4",username="root",password="temporal",key_filename="/opt/rhyns/rhyns/key")
    time.sleep(1)
    ruidossh.exec_command("unlink /tftpboot/pxelinux")
    time.sleep(1)
    if (hypervisor == "xen175"):
      ruidossh.exec_command("ln -s abiquoxen175 /tftpboot/pxelinux")
    elif (hypervisor == "xen180"):
      ruidossh.exec_command("ln -s abiquoxen180 /tftpboot/pxelinux")
    elif (hypervisor == "kvm175"):
      ruidossh.exec_command("ln -s abiquokvm175 /tftpboot/pxelinux")
    elif (hypervisor == "kvm180"):
      ruidossh.exec_command("ln -s abiquokvm180 /tftpboot/pxelinux")
    elif (hypervisor == "xenserver"):
      ruidossh.exec_command("ln -s xenserver5 /tftpboot/pxelinux")
    elif (hypervisor == "xenserver6"):
      #ruidossh.exec_command("ln -s xenserver6 /tftpboot/pxelinux")
      pass
    elif (hypervisor == "esxi4"):
      ruidossh.exec_command("ln -s esxi /tftpboot/pxelinux")
    elif (hypervisor == "esxi5"):
      #ruidossh.exec_command("ln -s esxi5 /tftpboot/pxelinux")
      pass
    elif (hypervisor == "vbox175"):
      ruidossh.exec_command("ln -s abiquovbox175 /tftpboot/pxelinux")
    elif (hypervisor == "vbox180"):
      ruidossh.exec_command("ln -s abiquovbox180 /tftpboot/pxelinux")
    else:
	  pass
    os.system("ipmitool -U root -H "+ip+" -P temporal chassis bootdev pxe")
    os.system("ipmitool -U root -H "+ip+" -P temporal chassis power reset")
    os.system("ipmitool -U root -H "+ip+" -P temporal chassis power on")


def do_poweron(thunder):
    os.system("ipmitool -U root -H "+thunder.ipmiip+" -P temporal chassis power on")

def do_poweroff(thunder):
    os.system("ipmitool -U root -H "+thunder.ipmiip+" -P temporal chassis power off")

def do_reboot(thunder):
    os.system("ipmitool -U root -H "+thunder.ipmiip+" -P temporal chassis power reset")


def do_check_hypervisor_by_api(thunder):
    # HYPERV
    req = urllib2.Request('http://'+thunder.ip+':5985/ws')
    try:
        urllib2.urlopen(req,timeout=10)
    except urllib2.HTTPError, e:
        if ("Microsoft-HTTPAPI"  in  e.info().headers[1]):
            return("hyperv")
    except urllib2.URLError, e:
        pass

    # ESXi
    req = urllib2.Request('https://'+thunder.ip)
    try:
        c = urllib2.urlopen(req,timeout=10).read(1000)
        if "ESXi" in c : 
            return("esxi")
    except:
        pass

    # XenServer
    req = urllib2.Request('http://'+thunder.ip)
    try:
        c = urllib2.urlopen(req,timeout=10).read(1000)
        if "XenServer" in c:
            return("xenserver")
    except:
        pass

    # VBOX
    req = urllib2.Request('http://'+thunder.ip+':18083')
    try:
        c = urllib2.urlopen(req,timeout=10).read()
    except urllib2.HTTPError, e:
        if "vbox"  in  str(e.read()):
            return("vbox")
    except:
        pass

    # XEN
    try:
        conn = libvirt.openReadOnly('xen+tcp://'+thunder.ip)
    except libvirt.libvirtError as e:
        pass
    else:
        return("xen")

    # KVM 
    try:
        conn = libvirt.openReadOnly('qemu+tcp://'+thunder.ip+'/system')
    except libvirt.libvirtError as e:
        pass
    else:
        return("kvm")


    
    return("unknown")


def do_check_hypervisor_by_nc(thunder):
    hv = "unknown"
    try:
      api_hv = urllib2.urlopen("http://mothership/nodecollector/"+thunder.ip+"/hypervisor/",timeout=10).read()
    except urllib2.HTTPError:
      return u"unknown"
    except urllib2.URLError:
      return u"unknown"
    if ("kvm" in api_hv):
        hv = u"kvm"
    elif ("xenserver" in api_hv):
        hv = u"xenserver"
    elif ("vmx" in api_hv):
        hv = u"esxi"
    elif ("hyperv" in api_hv):
        hv = u"hyperv"
    elif ("vbox" in api_hv):
        hv = u"vbox"
    elif ("xen" in api_hv):
        hv = u"xen"
    return hv

def do_check_power(thunder):
    return (commands.getoutput("ipmitool -U root -H "+thunder.ipmiip+" -P temporal chassis status | grep 'System Power' | awk '{print $4}' " ) )





