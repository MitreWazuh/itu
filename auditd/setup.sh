//https://www.redhat.com/sysadmin/configure-linux-auditing-auditd


sudo apt-get install auditd audispd-plugins




// on wazuh agent ossec.conf add this
// /var/ossec/etc/ossec.conf
  <localfile>
    <log_format>syslog</log_format>
    <location>/var/log/audit/audit.log</location>
  </localfile>


// add audit rules on agent
// /etc/audit/rules.d/
