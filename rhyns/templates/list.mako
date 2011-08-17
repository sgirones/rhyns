# -*- coding: utf-8 -*- 
<%inherit file="layout.mako"/>


<script LANGUAGE="JavaScript">
<!--
function confirmPost()
{
var agree=confirm("Are you sure you do that?");
if (agree)
return true ;
else
return false ;
}
// -->
</script>


<!-- Autorefresh 30s -->

<META HTTP-EQUIV="Refresh" CONTENT="30">


<div style="float:center">
<h1>Thunderdome</h1>
</div>

<ul id="tasks">
% if thunders:
  % for t in thunders:
    % if (t.status == "locked"):
  <span class="square_gray make_float">
    <div style="float: right;">
      <a href="${request.route_url('unlock', thunder_id=t.id)}"><img height="23" width="23" alt="lock" src="/static/lock.png"/></a>
    </div>
    % elif t.power == "off":
  <span class="square_red make_float">
    <div style="float: right;">
      <a href="${request.route_url('lock', thunder_id=t.id)}"><img height="23" width="23" alt="lock" src="/static/unlock.png"/></a>
    </div>
    % elif t.status == "installing":
  <span class="square_yellow make_float">
    <div style="float: right;">
      <a href="${request.route_url('lock', thunder_id=t.id)}"><img height="23" width="23" alt="lock" src="/static/unlock.png"/></a>
    </div>
    % else:
  <span class="square make_float">
    <div style="float: right;">
      <a href="${request.route_url('lock', thunder_id=t.id)}"><img height="23" width="23" alt="lock" src="/static/unlock.png"/></a>
    </div>
    % endif
    <div style="float: right;">
      <a href="${request.route_url('check_status', thunder_id=t.id)}"><img height="23" width="23" alt="Refresh" src="/static/refresh.png"/></a>
    </div>
  <h2>Thunder${t.id}</span>
  <h2>${t.ip}</span>
  </h2>
  <p>Type: ${t.hypervisor}</span>
  </p>
  <p>Status: ${t.status}</span>
  </p>
  <p>Power: ${t.power}</span>
  </p>



    Install hypervisor:<br />
    <a href="${request.route_url('install', thunder_id=t.id, hypervisor='xen175')}" onClick="return confirmPost();" >XEN 1.7.5</a><br />
    
    <a href="${request.route_url('install', thunder_id=t.id, hypervisor='xen180')}" onClick="return confirmPost();" >XEN 1.8.0</a><br />

    <a href="${request.route_url('install', thunder_id=t.id, hypervisor='kvm175')}" onClick="return confirmPost();" >KVM 1.7.5</a><br />

    <a href="${request.route_url('install', thunder_id=t.id, hypervisor='kvm180')}" onClick="return confirmPost();" >KVM 1.8.0</a><br />

    <a href="${request.route_url('install', thunder_id=t.id, hypervisor='esxi')}" onClick="return confirmPost();" >ESXi 4</a><br />
    
    <a href="${request.route_url('install', thunder_id=t.id, hypervisor='esxi5')}" onClick="return confirmPost();" >ESXi 5</a><br />

    <a href="${request.route_url('install', thunder_id=t.id, hypervisor='xenserver')}" onClick="return confirmPost();" >XenServer 5</a><br />
    
    <a href="${request.route_url('install', thunder_id=t.id, hypervisor='xenserver6')}" onClick="return confirmPost();" >XenServer 6</a><br />

    <a href="${request.route_url('install', thunder_id=t.id, hypervisor='vbox175')}" onClick="return confirmPost();" >VirtualBox 1.7.5</a><br />

    <a href="${request.route_url('install', thunder_id=t.id, hypervisor='vbox180')}" onClick="return confirmPost();" >VirtualBox 1.8.0</a><br />

    <a href="${request.route_url('install', thunder_id=t.id, hypervisor='v2v')}" onClick="return confirmPost();" >Abiquo V2V</a><br />


    <p>  </p>

    <a href="${request.route_url('poweron', thunder_id=t.id)}" onClick="return confirmPost();" >Poweron</a>

   <a href="${request.route_url('poweroff', thunder_id=t.id)}" onClick="return confirmPost();" >Poweroff</a>
   <a href="${request.route_url('reboot', thunder_id=t.id)}" onClick="return confirmPost();" >Reboot</a>
    </span>
  % endfor
% else:
  <li>No thunders listed</li>
% endif

</ul>
