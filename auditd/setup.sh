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


// on wazuh server ossec.conf file
<ruleset>
    <!-- Default ruleset -->
    <decoder_dir>ruleset/decoders</decoder_dir>
    <decoder_exclude>ruleset/decoders/0040-auditd_decoders.xml</decoder_exclude>
    <rule_dir>ruleset/rules</rule_dir>
    <rule_exclude>0215-policy_rules.xml</rule_exclude>
    <rule_exclude>0365-auditd_rules.xml</rule_exclude>
    <list>etc/lists/audit-keys</list>
    <list>etc/lists/amazon/aws-eventnames</list>
    <list>etc/lists/security-eventchannel</list>
    <list>etc/lists/software-vendors</list>
    <list>etc/lists/common-ports</list>
    <list>etc/lists/rfc-1918</list>
    <list>etc/lists/cve</list>
    <list>etc/lists/malicious-powershell</list>
    <list>etc/lists/bash_profile</list>
    <!-- User-defined ruleset -->
    <decoder_dir>etc/decoders</decoder_dir>
    <rule_dir>etc/rules</rule_dir>
</ruleset>
