NET+ N10-009 QUICK REF  (study ref netplus · /ref in a quiz · objectives: study ref netplus obj)
EXAM  90 Q max · 90 min · pass 720/900 · D1 23% D2 20% D3 19% D4 14% D5 24%
      practice exam: study netplus practice_exam  (menu 'p')

OSI 1->7  Please Do Not Throw Sausage Pizza Away   (7->1 All People Seem To Need Data Processing)
  1 Physical  bits     hub, cable, transceiver     4 Transport segments TCP/UDP, ports
  2 Data Link frames   switch, NIC, MAC            5 Session · 6 Presentation (TLS, encoding)
  3 Network   packets  router, L3 switch, IP       7 Application HTTP DNS SMTP

SUBNETTING  (study ref = full table)
  bit row 128 64 32 16 8 4 2 1 · mask row 128 192 224 240 248 252 254 255
  block = 256 - mask octet · network = biggest multiple <= octet · bcast = next - 1
  usable = block - 2 (4th octet) · /24 254 · /23 510 · /22 1022 · /21 2046 · /20 4094
  wildcard = 255 - mask (/27 = 0.0.0.31) · VLSM = biggest subnet first · /30 = P2P

IPv4  RFC1918 10/8 · 172.16/12 (16-31) · 192.168/16 · APIPA 169.254/16 · loopback 127/8
      CGNAT 100.64/10 · A 1-126 /8 · B 128-191 /16 · C 192-223 /24 · D 224-239 mcast · E 240+
IPv6  ::1 loopback · fe80::/10 link-local · fc00::/7 (fd) ULA · 2000::/3 global · ff00::/8 mcast
      one :: only · NDP replaces ARP · SLAAC = self-address from RA · dual stack / tunnel / NAT64

PORTS
  20/21 FTP · 22 SSH/SFTP · 23 Telnet · 25 SMTP · 53 DNS · 67/68 DHCP · 69 TFTP
  80 HTTP · 88 Kerberos · 123 NTP · 161/162 SNMP/trap · 389 LDAP · 443 HTTPS · 445 SMB
  514 syslog · 587 SMTP TLS · 636 LDAPS · 853 DoT · 1433 MSSQL · 1812/1813 RADIUS
  3306 MySQL · 3389 RDP · 5060/5061 SIP · TACACS+ TCP 49
IPSEC  AH = integrity + auth, NO encryption · ESP = encryption (+ integrity) · IKE UDP 500
       tunnel mode = whole packet (site-to-site) · transport = payload only

ROUTING  select: 1 longest prefix · 2 lowest AD · 3 lowest metric
  AD: connected 0 · static 1 · eBGP 20 · EIGRP 90 · OSPF 110 · RIP 120 · iBGP 200
  RIP dist-vector · OSPF/IS-IS link-state · EIGRP hybrid · BGP path-vector (between ASs)
  ip route 0.0.0.0 0.0.0.0 NEXTHOP · PAT = ... overload · FHRP = HSRP / VRRP / GLBP (VIP)
SWITCHING
  802.1Q trunk · native = untagged, must match · switchport mode access / access vlan N
  LACP = channel-group N mode active · STP blocking>listening>learning>forwarding
  root = lowest bridge ID (priority 32768 default, then MAC) · BPDU guard = err-disable
  MTU 1500 · jumbo 9000 · duplex mismatch = late collisions + CRC

WI-FI            band          max
  b              2.4           11M
  a              5             54M
  g              2.4           54M
  n  Wi-Fi 4     2.4+5         600M   MIMO
  ac Wi-Fi 5     5 only        ~6.9G  MU-MIMO
  ax Wi-Fi 6/6E  2.4+5 (+6)    ~9.6G  OFDMA
  2.4 non-overlap 1 6 11 · 802.11h = DFS radar + TPC · WPA3 = SAE · Enterprise = 802.1X + RADIUS
  omni = 360 · Yagi/dish/patch = directional · SSID name · BSSID AP MAC · ESS many APs one SSID

CABLING
  Cat5e 1G/100m · Cat6 10G/55m · Cat6a 10G/100m · Cat8 25-40G/30m · DAC twinax <7m
  MMF aqua 850nm short · SMF yellow 1310/1550 long · SFP 1G · SFP+ 10G · QSFP28 100G
  T568A/B swap orange+green · straight = same both ends · crossover = A+B · rollover = console
  PoE af 15.4W · at 30W · bt 60-100W

DOCS / OPS
  SLA promises · AUP user rules · SDS chemical · MOU non-binding · NDA secrets
  EOL no longer sold · EOS no patches · change: request > CAB > window > rollback > document
  running-config RAM · startup-config NVRAM · copy run start
DR  RPO data loss · RTO downtime · MTTR repair (low) · MTBF between failures (high)
    cold < warm < hot · incremental = full + all · differential = full + latest · 3-2-1
    RAID 0 stripe · 1 mirror · 5 parity (3+) · 6 double (4+) · 10 striped mirrors (4+)

DHCP  DORA · 67/68 · reservation = MAC → same IP · exclusion = never hand out
      options 3 gateway · 6 DNS · 15 domain · 66 TFTP · relay = ip helper-address
      169.254 = no lease (exhausted: bigger scope + shorter lease)
DNS  A · AAAA · CNAME alias · MX mail · TXT SPF/DKIM · NS · PTR reverse · SOA
     recursive = resolver does the work · DNSSEC signs · DoH 443 / DoT 853 encrypt
TIME NTP UDP 123 · PTP hardware ns · NTS authenticated · Kerberos needs < 5 min skew

MONITORING
  SNMP 161 poll · 162 trap · MIB/OID · v1/v2c community = cleartext password · v3 encrypted
  syslog 514 · 0 emerg 1 alert 2 crit 3 err 4 warn 5 notice 6 info 7 debug (lower = worse)
  SIEM collect + correlate · NetFlow/IPFIX/sFlow = who, how much · SPAN / TAP = copy traffic

SECURITY
  CIA · threat = actor · vulnerability = weakness · exploit = technique · risk = likelihood x impact
  RADIUS UDP 1812 users · TACACS+ TCP 49 admins · LDAP 389 · SAML XML SSO · MFA 2+ categories
  attacks > fix: MAC flood > port security · rogue DHCP > DHCP snooping · ARP poison > DAI
                 DNS poison > DNSSEC · rogue switch > BPDU guard · VLAN hop > nonegotiate, native not 1
  fail-safe opens (people) · fail-secure stays locked · screened subnet = public servers

TROUBLESHOOTING  I Take Tea, Pour It, Very Delicious
  identify > theory > test > plan > implement > verify > document
  top-down L7 · bottom-up L1 · divide + conquer L3 (ping)
  CRC = cable/EMI · runts < 64 · giants > 1518 (MTU) · drops = congestion
  err-disabled > shut / no shut · admin down > no shutdown · suspended = LACP mismatch

COMMANDS
  ipconfig /all /release /renew /flushdns · ip a · ip r · ip neigh · arp -a
  ping -t (Win forever) -n 4 · ping -c 4 (Linux) · ping -f -l 1472 (MTU test)
  tracert -d · traceroute · pathping / mtr = per-hop loss
  nslookup NAME SERVER · dig @SERVER NAME MX · dig +short · dig -x IP
  netstat -ano (PID) · ss -tulpn · tcpdump -i eth0 -n port 53 -w cap.pcap
  nmap -sn sweep · -sS SYN · -sU UDP · -sV version · -O OS · -A all · -p- · -Pn
  show ip route · show interface(s) status · show vlan brief · show mac address-table
  show arp · show running-config · show power inline · show cdp/lldp neighbors
