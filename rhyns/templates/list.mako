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
      <a href="${request.route_url('unlock', thunder_id=t.id)}"><img height="23" width="23" alt="lock" src="/static/unlock.png"/></a>
    </div>
    % elif t.power == "off":
  <span class="square_red make_float">
    <div style="float: right;">
      <a href="${request.route_url('lock', thunder_id=t.id)}"><img height="23" width="23" alt="lock" src="/static/lock.png"/></a>
    </div>
    % elif t.status == "installing":
    <div style="float: right;">
      <a href="${request.route_url('lock', thunder_id=t.id)}"><img height="23" width="23" alt="lock" src="/static/lock.png"/></a>
  <span class="square_yellow make_float">
    % else:
  <span class="square make_float">
    <div style="float: right;">
      <a href="${request.route_url('lock', thunder_id=t.id)}"><img height="23" width="23" alt="lock" src="/static/lock.png"/></a>
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
    <a href="${request.route_url('install', thunder_id=t.id, hypervisor='xen')}" onClick="return confirmPost();" >XEN</a><br />

    <a href="${request.route_url('install', thunder_id=t.id, hypervisor='kvm')}" onClick="return confirmPost();" >KVM</a><br />

    <a href="${request.route_url('install', thunder_id=t.id, hypervisor='esxi')}" onClick="return confirmPost();" >ESXi</a><br />

    <a href="${request.route_url('install', thunder_id=t.id, hypervisor='xenserver')}" onClick="return confirmPost();" >XenServer</a><br />

    <a href="${request.route_url('install', thunder_id=t.id, hypervisor='vbox')}" onClick="return confirmPost();" >VirtualBox</a><br />

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
