<!-- passmark: 80 -->
## Test 1 - Prereq: Binary + Hex (30 Q)

1. How many bits are in one IPv4 octet?
   - [ ] 4  - **[x] 8**  - [ ] 16  - [ ] 32
   - *Answer: 8. An octet = 8 bits = one of the four numbers in an IPv4 address (Internet Protocol version 4). The whole address = 4 octets x 8 = 32 bits. Hook: OCTet = 8, like an OCTopus has 8 legs.*
   - @0.bin
2. Type the eight bit values of an octet, left to right, separated by spaces.
   - [=] 128 64 32 16 8 4 2 1
   - *Start at 128 and halve each time: 128 64 32 16 8 4 2 1. The leftmost bit is the biggest. Write this row at the top of your whiteboard before the exam starts; every conversion uses it.*
   - @0.bin
3. What is the largest number one octet can hold?
   - [ ] 128  - [ ] 254  - **[x] 255**  - [ ] 256
   - *All 8 bits on = 128+64+32+16+8+4+2+1 = 255. There are 256 values in total, because 0 counts as one of them. That's why no IPv4 octet goes above 255.*
   - @0.bin
4. Type 11000000 as a decimal number.
   - [=] 192
   - *Only the 128 and 64 bits are on: 128 + 64 = 192. Add up the bit values wherever there's a 1. 192 is also the /26 mask octet.*
   - @0.bin
5. Type 00001010 as a decimal number.
   - [=] 10
   - *The 8 bit and the 2 bit are on: 8 + 2 = 10. Leading zeros change nothing, just like 007 is still 7.*
   - @0.bin
6. Type 11111110 as a decimal number.
   - [=] 254
   - *Everything except the 1 bit = 255 - 1 = 254. Shortcut: 255 minus the bits that are OFF.*
   - @0.bin
7. Type 10101010 as a decimal number.
   - [=] 170
   - *128 + 32 + 8 + 2 = 170. Every other bit is on.*
   - @0.bin
8. Type 01111111 as a decimal number.
   - [=] 127
   - *Every bit except 128 = 255 - 128 = 127. It's the first octet of the loopback range, 127.0.0.1.*
   - @0.bin
9. Type 255 in binary.
   - [=] 11111111
   - *All 8 bits on. 255 in a mask octet means that octet is all network bits.*
   - @0.bin
10. Type 224 in binary.
    - [=] 11100000
    - *Left to right: 128 fits, leaving 96. 64 fits, leaving 32. 32 fits, leaving 0. Everything else is 0. 224 = 3 bits on, which is why 255.255.255.224 is /27 (24 + 3).*
    - @0.bin
11. Type 239 in binary.
    - [=] 11101111
    - *Method: 128 fits, 111 left, so 1. 64 fits, 47 left, so 1. 32 fits, 15 left, so 1. 16 does not fit, so 0. 8 fits, 7 left, so 1. 4, 2 and 1 all fit, so 1 1 1. Result 11101111. Shortcut: 255 - 239 = 16, so only the 16 bit is off.*
    - @0.bin ~26.21
12. Type 100 in binary.
    - [=] 01100100 | 1100100
    - *128 doesn't fit, so 0. 64 fits, 36 left, so 1. 32 fits, 4 left, so 1. 16 no, 8 no, so 0 0. 4 fits, 0 left, so 1. Then 2 and 1 are 0. Result 01100100. Always write all 8 bits so the positions line up.*
    - @0.bin
13. Type 172 in binary.
    - [=] 10101100
    - *128 fits, 44 left. 64 no. 32 fits, 12 left. 16 no. 8 fits, 4 left. 4 fits, 0 left. 2 no, 1 no. Result 10101100. It's the first octet of the 172.16.0.0/12 private range.*
    - @0.bin
14. Type 248 in binary.
    - [=] 11111000
    - *5 bits on: 128+64+32+16+8 = 248. 255.255.255.248 = /29 (24 + 5). Mask octets are always ones from the left, then zeros.*
    - @0.bin
15. Which of these can NOT be a subnet mask octet?
    - [ ] 252  - [ ] 240  - **[x] 250**  - [ ] 128
    - *Answer: 250. Mask octets must be a run of 1s from the left, then 0s. The only legal values are 0 128 192 224 240 248 252 254 255 (the running total of the bit row). 250 is a real number, 11111010, but it's not a legal mask: after the 1s start turning to 0s, a 1 comes back (1111 1 0 1 0). A mask is all 1s, then all 0s, never a 1 after a 0. Hook: the mask values ARE the running total of 128 64 32 ...*
    - @0.bin
16. Type the mask octet you get with the first 4 bits on, 11110000.
    - [=] 240
    - *128+64+32+16 = 240. Running total of the bit row: 128, 192, 224, 240, 248, 252, 254, 255. Four bits in = 240.*
    - @0.bin
17. Mask 255.255.255.192 = slash what? Type just the prefix, e.g. /24.
    - [=] /26 | 26
    - *192 = 11000000 = 2 bits. 8 + 8 + 8 + 2 = 26 network bits. CIDR (Classless Inter-Domain Routing) notation just counts the 1s in the mask.*
    - @0.bin
18. Type the dotted-decimal mask for /20.
    - [=] 255.255.240.0
    - *20 bits = 8 + 8 + 4. Two full octets of 255, then 4 bits on = 240, then 0. Hook: count 8s off the prefix, then look up the leftover bits in the running total.*
    - @0.bin
19. How many bits long is a MAC address?
    - [ ] 32  - **[x] 48**  - [ ] 64  - [ ] 128
    - *MAC (Media Access Control) = the 48-bit hardware address burned into each NIC, written as 12 hex digits, e.g. 00:1A:2B:3C:4D:5E. IPv4 = 32 bits, an IPv6 interface ID = 64, a full IPv6 address = 128.*
    - @0.bin ~1.4
20. How many bits does ONE hex digit represent?
    - [ ] 2  - **[x] 4**  - [ ] 8  - [ ] 16
    - *Answer: 4. 16 is the number of VALUES one hex digit can be (0-F), not bits. 4 bits = 2×2×2×2 = 16 values, so 1 hex digit = 4 bits (a nibble). F = 1111. 2 hex digits = 8 bits = 1 byte; MAC = 12 hex = 48 bits.*
    - @0.bin
21. A technician copies a hardware address off a laptop label. Only one of these strings could be a real 48-bit Ethernet address. Which?
    - [ ] GG:00:45:2C:00:4F  - **[x] 0A:24:D3:00:00:FF**  - [ ] Z0:4F:9A:6F:22:00  - [ ] 7C:1E:52:K0:3B:A9
    - *Answer: 0A:24:D3:00:00:FF. A MAC is six pairs of hexadecimal digits, and hex stops at F, so any G, K or Z rules a string out. The leading three bytes identify the manufacturer (OUI, Organizationally Unique Identifier); the trailing three are assigned per device.*
    - @0.bin ~26.20
22. Type hex F as a decimal number.
    - [=] 15
    - *A=10, B=11, C=12, D=13, E=14, F=15. Hex F = binary 1111, all four bits on. Hook: A is the 10th letter-digit after 0-9.*
    - @0.bin
23. Type hex FF as a decimal number.
    - [=] 255
    - *Hex columns go 16s then 1s, like decimal goes 10s then 1s. FF = (15 × 16) + 15 = 240 + 15 = 255. Binary shortcut: each F = 1111, so FF = 11111111 = 255, the biggest byte. Another example: hex 1A = (1 × 16) + 10 = 26.*
    - @0.bin
24. Type hex A as a 4-bit binary number.
    - [=] 1010
    - *A = 10 = 8 + 2, so bits 8 and 2 on, giving 1010. Nibble values: 8 4 2 1.*
    - @0.bin
25. How many bits are in an IPv6 address?
    - [ ] 32  - [ ] 64  - **[x] 128**  - [ ] 48
    - *IPv6 = 128 bits, written as 8 groups of 4 hex digits separated by colons, e.g. 2001:0db8:0000:0000:0000:ff00:0042:8329. Each group = 16 bits. The first 64 bits are usually the network prefix, the last 64 the interface ID.*
    - @0.bin
26. Full convert: type 10.1.200.37 in binary, as four 8-bit octets separated by dots.
    - [=] 00001010.00000001.11001000.00100101
    - *10 = 8+2 = 00001010. 1 = 00000001. 200 = 128+64+8 = 11001000. 37 = 32+4+1 = 00100101. Write all 8 bits per octet; subnetting is about lining bits up.*
    - @0.bin
27. Type 11000000.10101000.00000001.11111110 in dotted decimal.
    - [=] 192.168.1.254
    - *11000000 = 192, 10101000 = 128+32+8 = 168, 00000001 = 1, 11111110 = 254. A classic home gateway address.*
    - @0.bin
28. A host is 192.168.1.77, mask 255.255.255.224. Type its NETWORK address, all four octets.
    - [=] 192.168.1.64
    - *Table method: 224 = /27, block = 256 - 224 = 32. Networks go .0 .32 .64 .96. 77 sits between 64 and 96, so the network = 192.168.1.64. Binary way, same answer: 77 = 01001101, 224 = 11100000; keep only the bits that are 1 in BOTH = 01000000 = 64.*
    - @0.bin
29. Same host, 192.168.1.77/27. Type its BROADCAST address, all four octets.
    - [=] 192.168.1.95
    - *Block 32: this subnet is .64 to .95, and the next one starts at .96. Broadcast = the last address before the next network = 96 - 1 = 95, so 192.168.1.95. Usable hosts = .65 to .94.*
    - @0.bin
30. Type how many usable host addresses a /27 has.
    - [=] 30
    - *Host bits = 32 - 27 = 5. 2 to the power of 5 = 32 addresses, minus 2 (network + broadcast) = 30 usable. Hook: host bits h, usable = 2^h - 2.*
    - @0.bin

### Key facts
- **Bit row: 128 64 32 16 8 4 2 1. To convert binary to decimal, add the 1s. To convert decimal to binary, go left to right: fits = 1 and subtract, doesn't fit = 0.**
- **Shortcut: 255 minus the value = the bits that are OFF. 239 = 255 - 16, so 11101111.**
- **Mask octets = the running total: 128 192 224 240 248 252 254 255. Prefix = count the 1s. Anything else, like 250, is NOT a valid mask.**
- **Hex: one digit = 4 bits, A=10 through F=15. FF = 255. MAC = 48 bits = 12 hex digits (first 24 = OUI). IPv4 = 32 bits, IPv6 = 128 bits.**
- **Network = IP AND mask. Broadcast = host bits all 1s. Usable hosts = 2 to the power of host bits, minus 2.**

## Test 2 - 1.1/1.6 OSI + Topologies (30 Q)

1. Put the OSI layers in order from Layer 1 to Layer 7.
   - **[x] Physical, Data Link, Network, Transport, Session, Presentation, Application**  - [ ] Physical, Network, Data Link, Transport, Session, Application, Presentation  - [ ] Physical, Data Link, Transport, Network, Presentation, Session, Application  - [ ] Data Link, Physical, Network, Transport, Session, Presentation, Application
   - *OSI (Open Systems Interconnection) model, bottom to top: 1 Physical, 2 Data Link, 3 Network, 4 Transport, 5 Session, 6 Presentation, 7 Application. Hook, 1 to 7: Please Do Not Throw Sausage Pizza Away. 7 to 1: All People Seem To Need Data Processing.*
   - @1.1.osi ~1.1,2.7
2. Which layer NUMBER is the Transport layer?
   - [ ] 3  - **[x] 4**  - [ ] 5  - [ ] 2
   - *Answer: 4. Transport = Layer 4, the ports layer: TCP (Transmission Control Protocol) and UDP (User Datagram Protocol). Please Do Not THROW: the 4th word, T for Transport.*
   - @1.1.osi ~2.8,1.19,1.3
3. Which is Layer 6?
   - [ ] Session  - **[x] Presentation**  - [ ] Application  - [ ] Transport
   - *Layer 6 = Presentation, the translator: formatting, compression, encryption/decryption (e.g. TLS turning data into ciphertext, JPEG/ASCII formats). Sausage PIZZA: P for Presentation, sitting just under Application.*
   - @1.1.osi ~1.25,1.6,1.15
4. Which layer opens, maintains and closes the conversation between two applications?
   - [ ] Transport  - **[x] Session**  - [ ] Presentation  - [ ] Network
   - *Layer 5 Session = sets up, manages and tears down sessions (dialog control, checkpoints). Transport (4) moves the segments reliably; Presentation (6) formats/encrypts; Network (3) routes. Hook: a SESSION is the whole conversation, opened and closed.*
   - @1.1.osi ~1.8,2.6
5. Which layer does a user's browser or email app talk to directly?
   - [ ] Presentation  - [ ] Session  - **[x] Application**  - [ ] Transport
   - *Layer 7 Application = the network services apps use: HTTP (HyperText Transfer Protocol), DNS (Domain Name System), SMTP (Simple Mail Transfer Protocol), FTP (File Transfer Protocol). It's NOT the app itself, but the protocols it calls.*
   - @1.1.osi ~1.22,1.17,2.4
6. Which lists the PDU names for Layers 1, 2, 3 and 4 (TCP), in that order?
   - **[x] Bit, frame, packet, segment**  - [ ] Bit, packet, frame, segment  - [ ] Frame, bit, packet, datagram  - [ ] Bit, frame, segment, packet
   - *PDU (Protocol Data Unit) bottom-up: L1 Bit, L2 Frame, L3 Packet, L4 Segment (TCP) or Datagram (UDP), L5-7 Data. Hook: Big Fat Pigs Sit Down = Bit Frame Packet Segment Data.*
   - @1.1.osi ~1.7,1.21,1.23,2.2
7. A UDP PDU at Layer 4 is called a:
   - [ ] Segment  - **[x] Datagram**  - [ ] Packet  - [ ] Frame
   - *UDP = User DATAGRAM Protocol, so its PDU is a datagram. TCP's is a segment. Packet = L3, frame = L2.*
   - @1.1.osi ~1.13
8. Which three OSI layers refer to their PDU simply as data, rather than as a segment, packet or frame? (Select 3)
   - **[x] Application**  - **[x] Presentation**  - **[x] Session**  - [ ] Transport  - [ ] Network  - [ ] Data Link
   - *Session, Presentation and Application (L5-L7) refer to the PDU as plain data. Naming changes once encapsulation begins: segment or datagram at Transport, packet at Network, frame at Data Link, bits at Physical.*
   - @1.1.osi ~2.5
9. When a PC SENDS data, which way does encapsulation go, and what happens at each layer?
   - **[x] Down from Layer 7 to 1, each layer adds its header**  - [ ] Up from Layer 1 to 7, each layer adds its header  - [ ] Down from Layer 7 to 1, each layer removes a header  - [ ] Only Layers 3 and 4 add headers
   - *Encapsulation = sending side, top down: data gets a TCP/UDP header (segment), then an IP header (packet), then a MAC header + FCS trailer (frame), then goes out as bits. The receiver de-encapsulates bottom up, stripping each header. Hook: wrapping a present layer by layer before posting it.*
   - @1.1.osi ~2.1
10. A packet capture shows two protocols operating at the Network layer of the OSI model. Which two? (Select 2)
    - **[x] IP**  - **[x] ICMP**  - [ ] ARP  - [ ] DNS  - [ ] SNMP
    - *The Network layer handles logical addressing and path selection: IP carries the packets and ICMP (used by ping and traceroute) reports errors about them. ARP is usually placed at L2 for the exam since it resolves MAC addresses. DNS and SNMP are application-layer protocols.*
    - @1.1.osi ~1.12
11. Which protocols work at Layer 7? (Select 3)
    - **[x] HTTP**  - **[x] SMTP**  - **[x] DNS**  - [ ] TCP  - [ ] IP  - [ ] ARP
    - *L7 Application = HTTP (HyperText Transfer Protocol), SMTP (Simple Mail Transfer Protocol), DNS (Domain Name System), FTP (File Transfer Protocol), SSH (Secure Shell). TCP = L4, IP = L3, ARP (Address Resolution Protocol) = L2.*
    - @1.1.osi ~1.10
12. A host needs the hardware address for 10.0.0.1 and sends out a resolution query. What destination address appears in that Ethernet frame?
    - [ ] 00:00:00:00:00:00  - **[x] FF:FF:FF:FF:FF:FF**  - [ ] The router's MAC  - [ ] 33:33:00:00:00:01
    - *Answer: FF:FF:FF:FF:FF:FF. The host does not yet know who owns the IP, so the ARP request floods the local segment as a broadcast with every bit set. Only the owner answers, and that reply is unicast. 33:33... is the IPv6 multicast MAC prefix; all zeros means an unset address.*
    - @1.1.osi ~26.19,1.24
13. Which devices work at Layer 1? (Select 3)
    - **[x] Hub**  - **[x] Repeater**  - **[x] Cabling**  - [ ] Switch  - [ ] Router
    - *L1 Physical = things that just move bits with no addressing: hubs (a hub IS a 'multiport repeater': dumb, many ports, repeats every bit out every port, still L1, NOT L2), repeaters, cables, connectors, media converters. Switch = L2 (reads MACs), router = L3 (reads IPs).*
    - @1.1.osi ~1.2,1.16,2.3,1.20
14. Which devices work at Layer 2? (Select 3)
    - **[x] Switch**  - **[x] Bridge**  - **[x] NIC**  - [ ] Hub  - [ ] Media converter  - [ ] Router
    - *L2 Data Link = anything that reads MAC (Media Access Control) addresses: switches, bridges, NICs (Network Interface Cards, which carry the MAC), wireless APs (Access Points). Hub and media converter = L1; router = L3.*
    - @1.1.osi ~1.5,1.18,1.14,1.11
15. A device that switches frames AND routes between VLANs is called a:
    - **[x] Layer 3 switch**  - [ ] Layer 2 switch  - [ ] Managed switch  - [ ] Bridge
    - *Multilayer / L3 switch = switch hardware that also routes (L2 + L3), usually via SVIs (Switch Virtual Interfaces). A Layer 2 switch only forwards frames inside a VLAN; a managed switch can do VLANs but routes nothing unless it is L3. Common at the distribution and core layers.*
    - @1.1.osi ~1.9
16. Which topology connects every node directly to every other node, giving the most redundancy?
    - [ ] Star  - [ ] Ring  - **[x] Mesh**  - [ ] Hybrid
    - *Full mesh = every node linked to every other: the most paths, the most redundancy, the most cables (n(n-1)/2 links). Exam words: full mesh = every node, partial mesh = only some. Hybrid = a mix of topologies. Star = everything to a central switch; ring and bus are legacy.*
    - @1.6.topo ~7.18,7.19
17. A company has one central switch with every PC cabled to it. Topology?
    - **[x] Star**  - [ ] Mesh  - [ ] Bus  - [ ] Ring
    - *Star = all nodes to one central device. (Mixing several topologies, e.g. stars joined by a mesh = hybrid.) Easy to manage, one cable failing only drops one PC, but the centre is a single point of failure. Hub-and-spoke = the WAN version, with branch sites (spokes) connected to HQ (the hub).*
    - @1.6.topo ~7.21,7.20
18. A data centre has two layers of switches. Every access switch connects to every switch in the upper layer, so any server-to-server path crosses the same number of hops. Which topology is this?
    - [ ] Three-tier  - [ ] Collapsed core  - **[x] Spine and leaf**  - [ ] Hub and spoke
    - *Spine and leaf = 2 layers. Leaf switches (usually ToR, Top of Rack) connect servers; every leaf connects to every spine. Leaf to leaf is always leaf, spine, leaf: 3 switches, whichever spine it takes, so latency is equal and predictable. Great for east-west traffic.*
    - @1.6.topo ~7.22
19. Which is NOT a point-to-point connection?
    - [ ] A WAN link between two routers  - [ ] A site-to-site VPN tunnel  - [ ] A dedicated leased line  - **[x] A Wi-Fi AP serving many clients**
    - *Answer: A Wi-Fi AP serving many clients. Point to point = exactly two endpoints (WAN = Wide Area Network links, VPN = Virtual Private Network tunnels, leased lines). A Wi-Fi AP (Access Point) serving many clients is point-to-multipoint.*
    - @1.6.topo ~7.23
20. In the three-tier model, which layer is the high-speed backbone that just moves traffic fast?
    - **[x] Core**  - [ ] Distribution  - [ ] Access  - [ ] Edge
    - *Three-tier hierarchical model: CORE = fast backbone, no heavy filtering. DISTRIBUTION = the middle: routing between VLANs, ACLs (Access Control Lists), policy. ACCESS = where end devices plug in: port security, PoE (Power over Ethernet), VLAN assignment. Hook, top-down: Core, Distribution, Access = CDA.*
    - @1.6.tier ~7.24
21. Which describe the DISTRIBUTION layer? (Select 2)
    - **[x] Sits between the core and access layers**  - **[x] Routing, filtering and policy between VLANs**  - [ ] Where end devices plug in  - [ ] The fastest backbone, with minimal processing
    - *Distribution = the aggregation/policy middle: inter-VLAN routing, ACLs (Access Control Lists), QoS (Quality of Service) policy, and it aggregates the access switches. Access = end devices; core = backbone.*
    - @1.6.tier ~7.25
22. Which describe the ACCESS layer? (Select 3)
    - **[x] Connects end devices, wired and wireless**  - **[x] Port security and 802.1X at the edge**  - **[x] Marks traffic for QoS**  - [ ] Links the distribution layers together at high speed  - [ ] Handles traffic between sites
    - *Access = the edge: PCs, phones, APs (Access Points), with port security, 802.1X, PoE (Power over Ethernet), VLAN assignment and QoS (Quality of Service) marking. Linking distribution blocks at speed = core.*
    - @1.6.tier ~8.1
23. A small office merges the core and distribution layers into one pair of switches. Design?
    - [ ] Spine and leaf  - **[x] Collapsed core**  - [ ] Partial mesh  - [ ] Three-tier
    - *Collapsed core = a 2-tier design, core + distribution in one layer. Cheaper and simpler, for small or medium sites. It scales less well than full three-tier.*
    - @1.6.tier ~8.2
24. Users on the internet reach a web server in the data centre. Traffic flow?
    - **[x] North-south**  - [ ] East-west  - [ ] Inbound-only  - [ ] Lateral
    - *North-south = in and out of the data centre (client or internet to server). East-west = server to server inside it. Hook: north-south goes OUT through the roof; east-west stays on the same floor.*
    - @1.6.flow ~8.3
25. A web server queries a database server in the same data centre. Traffic flow?
    - [ ] North-south  - **[x] East-west**  - [ ] Perimeter  - [ ] Egress
    - *East-west = inside the data centre, server to server. Modern apps are mostly east-west, which is why spine-and-leaf and internal (micro)segmentation matter. Lateral movement by attackers is east-west too.*
    - @1.6.flow ~8.4
26. Type the OSI layer NUMBER where each problem lives, in order, separated by spaces: a wrong default gateway · a cut cable · a firewall blocking TCP 443 · a wrong VLAN on a switch port.
    - [=] 3 1 4 2
    - *Default gateway / IP routing = L3 Network. Cut cable = L1 Physical. TCP 443 port blocked = L4 Transport. VLAN (Virtual LAN) on a switch port = L2 Data Link.*
    - @1.1.osi
27. Type the layer NUMBER each device works at, in order, separated by spaces: hub, switch, router, wireless access point.
    - [=] 1 2 3 2
    - *Hub = L1, repeats bits with no addressing. Switch = L2, forwards by MAC. Router = L3, forwards by IP. AP (Access Point) = L2, a wireless bridge to the wired LAN (Local Area Network).*
    - @1.1.osi
28. A PC sends a web request. Put the PDUs in the order they're BUILT. Type the letters, e.g. abcde. ¶  A frame · B bits · C data · D packet · E segment
    - [=] cedab | c e d a b | c,e,d,a,b
    - *Encapsulation goes top down: data (L7-5), then segment (L4 adds the TCP header with ports), then packet (L3 adds the IP header), then frame (L2 adds the MAC header + FCS, Frame Check Sequence), then bits on the wire (L1).*
    - @1.1.osi
29. Diagram: ¶  Spine1     Spine2 ¶   |  \     /  | ¶   |    \ /    | ¶   |    / \    | ¶  Leaf1      Leaf2  ¶  servers   servers ¶Traffic goes from a server on Leaf1 to a server on Leaf2. How many SWITCHES does it pass through? Type a number.
    - [=] 3
    - *Leaf1, then any spine, then Leaf2 = 3 switches, always, whichever spine it takes. That's the point of spine and leaf: every path is the same length. Leaves never connect to leaves, spines never to spines.*
    - @1.6.topo
30. A campus has: switches in every floor closet for the PCs, a pair of switches doing inter-VLAN routing and ACLs for each building, and a pair of very fast switches linking the buildings. Which layers are these, in that order?
    - **[x] Access, distribution, core**  - [ ] Core, distribution, access  - [ ] Distribution, access, core  - [ ] Access, core, distribution
    - *Floor closets with PCs = access. Per-building routing + ACLs (Access Control Lists) = distribution. The fast inter-building backbone = core. If a small site merged the last two, that'd be a collapsed core.*
    - @1.6.tier

### Key facts
- **OSI 1-7: Physical, Data Link, Network, Transport, Session, Presentation, Application. Please Do Not Throw Sausage Pizza Away.**
- **PDU: bit (1) · frame (2) · packet (3) · segment TCP / datagram UDP (4) · data (5-7). Big Fat Pigs Sit Down.**
- **Devices: hub/repeater/cable = L1 · switch/bridge/NIC/AP = L2 · router/L3 switch = L3. ARP = L2 (broadcast to FF:FF:FF:FF:FF:FF).**
- **Protocols: TCP/UDP = L4 · IP/ICMP = L3 · HTTP/DNS/SMTP/FTP/SSH = L7. Encryption/format = L6. Sessions = L5.**
- **Encapsulation = sending, top down, adding headers. De-encapsulation = receiving, bottom up.**
- **Topologies: mesh = most redundancy · star = central switch · hybrid = mix · spine-leaf = data centre, every leaf to every spine · point to point = 2 ends.**
- **Three-tier: core (backbone) · distribution (routing/policy) · access (end devices). Collapsed core = core + distribution merged.**
- **North-south = in/out of the data centre · east-west = server to server inside it.**

## Test 3 - 1.2 Appliances + Apps (22 Q)

1. A help desk ticket asks which statements fit the device acting as the default gateway between two subnets. (Select 3)
   - **[x] Works at Layer 3**  - **[x] Forwards packets using IP addresses**  - **[x] Connects different networks together**  - [ ] Forwards frames using MAC addresses  - [ ] Floods unknown traffic out every port in the VLAN
   - *The default gateway is a router: a Layer 3 device that reads destination IP addresses and moves packets from one network to another. Forwarding frames by MAC and flooding unknown destinations inside a VLAN are switch behaviours at Layer 2.*
   - @1.2.appl ~2.9
2. You are explaining the main access-layer device in a wiring closet to an intern. Which statements describe it? (Select 3)
   - **[x] Works at Layer 2**  - **[x] Forwards frames using MAC addresses**  - **[x] Connects devices within one network**  - [ ] Routes packets between subnets by IP  - [ ] Assigns IP addresses to connected hosts
   - *A Layer 2 switch builds a MAC address table (CAM table) by noting the source address on each port, then sends frames only toward the port where the destination lives, all inside one broadcast domain. Routing between subnets needs a router or multilayer switch; handing out IPs is DHCP's job.*
   - @1.2.appl ~2.10
3. A device filters traffic in and out of a network based on rules like "allow TCP 443 from anywhere". Appliance?
   - [ ] Proxy server  - [ ] Vulnerability scanner  - **[x] Firewall**  - [ ] Content filter
   - *Firewall = allows/denies traffic by rules (IP, port, protocol, and on NGFWs (Next-Generation Firewalls) the app and user too). Proxy = a middleman that makes requests on your behalf. Vulnerability scanner = finds weaknesses. Content filter = blocks by category/keyword.*
   - @1.2.appl ~2.11
4. A security team connects a sensor to a SPAN port on the core switch. Which statements are true of this sensor? (Select 3)
   - **[x] Detects suspicious traffic and alerts**  - **[x] Watches a COPY of traffic, not inline**  - **[x] Takes no direct blocking action**  - [ ] Drops malicious packets inline  - [ ] Automatically rewrites firewall rules to stop the attacker
   - *This is an IDS (Intrusion Detection System). It analyses a copy of traffic from a SPAN port or network tap, so it sits out of band and can only log and notify. Blocking inline is the job of an IPS. It does not change firewall rules or drop packets itself.*
   - @1.2.appl ~2.13,2.12
5. An appliance is placed directly in the traffic flow so it can stop exploits as they happen. Which statements apply to it? (Select 3)
   - **[x] Sits inline in the traffic path**  - **[x] Can drop packets and reset connections**  - **[x] Actively prevents the attack**  - [ ] Only receives a mirrored copy of traffic  - [ ] Connects to a SPAN port and never touches live traffic
   - *This is an IPS (Intrusion Prevention System). Being inline means every packet passes through it, so it can drop traffic or reset sessions. The trade-off: a false positive interrupts legitimate users, and a failed unit can cut the link unless it fails open. Receiving only a mirrored copy from a SPAN port or TAP describes a passive IDS, which can alert but cannot block.*
   - @1.2.appl ~2.14
6. A website runs on three identical web servers and needs one address that spreads users across them, skipping any server that fails. Appliance?
   - [ ] Switch  - **[x] Load balancer**  - [ ] Proxy server  - [ ] Bandwidth shaper
   - *Load balancer = shares incoming requests across a pool of servers behind one VIP (Virtual IP), with health checks so a dead server is skipped. It gives both performance and availability.*
   - @1.2.appl ~2.15
7. Three web servers sit behind an appliance that hands server 1 the first visitor, server 2 the second, server 3 the third, then starts over. Algorithm?
   - [ ] Least connections  - **[x] Round-robin**  - [ ] Source IP hash  - [ ] Weighted response time
   - *Round-robin cycles through the pool in fixed order and does not check how busy each server is. Least connections picks the server with the fewest open connections, and weighted response time favours the fastest-responding server. Source IP hashing keeps a given client pinned to the same server for persistence.*
   - @1.2.appl ~26.8
8. Office PCs send their web requests to a device that fetches the page for them, caches it and logs/filters the URLs. Appliance?
   - [ ] Router  - **[x] Forward proxy**  - [ ] Reverse proxy  - [ ] Load balancer
   - *Forward proxy = sits in front of CLIENTS and makes requests on their behalf: caching, URL (Uniform Resource Locator) filtering, logging, hiding client IPs. Reverse proxy = sits in front of SERVERS and takes requests for them (often a load balancer or WAF, Web Application Firewall).*
   - @1.2.appl ~2.16
9. A small office adds one box to the LAN that shares folders to users over SMB. Appliance?
   - [ ] SAN  - **[x] NAS**  - [ ] DAS  - [ ] SSD
   - *NAS (Network-Attached Storage) = one appliance giving FILE-level access over the LAN (Local Area Network), using SMB (Server Message Block, Windows) or NFS (Network File System, Linux). DAS (Direct-Attached Storage) = a disk plugged straight into one server. SSD (Solid-State Drive) = just a drive.*
   - @1.2.appl ~2.17
10. A storage architect is comparing a file-sharing appliance with a dedicated storage fabric. Which statements are accurate? (Select 2)
    - **[x] NAS gives file-level access over the normal LAN**  - **[x] SAN gives block-level access over a dedicated storage network**  - [ ] NAS always runs over Fibre Channel  - [ ] A SAN shares folders to clients using SMB
    - *A NAS is a device on the ordinary LAN that serves files and folders, typically over SMB or NFS. A SAN is a separate storage network that presents raw volumes (LUNs) the servers format themselves, using Fibre Channel, iSCSI or FCoE. Think files versus blocks.*
    - @1.2.appl ~25.15,2.18
11. A research lab building an AI training cluster wants RDMA and sub-microsecond latency on a dedicated non-Ethernet interconnect. Which technology fits?
    - [ ] iSCSI  - [ ] FCoE  - **[x] InfiniBand**  - [ ] NFS
    - *InfiniBand is a purpose-built switched fabric with native RDMA, used in high-performance computing and AI clusters where latency matters most. iSCSI runs storage commands over regular IP, FCoE puts Fibre Channel frames on Ethernet, and NFS is a file-sharing protocol, not an interconnect.*
    - @1.2.appl ~27.20
12. A company has 60 lightweight APs and wants to configure them all, and push firmware, from one place. Device?
    - [ ] Multilayer switch  - [ ] Active hub  - **[x] Wireless LAN controller**  - [ ] Network bridge
    - *WLC (Wireless LAN Controller) = centrally configures and manages many lightweight APs (Access Points): SSIDs (Service Set Identifiers), channels, power, firmware, roaming. Can be a physical box, a VM or cloud-hosted. Autonomous APs are each configured on their own.*
    - @1.2.appl ~2.20
13. What does a wireless access point do?
    - **[x] Bridges Wi-Fi clients onto the wired network**  - [ ] Routes between two public networks  - [ ] Assigns IP addresses to wired PCs only  - [ ] Converts fibre to copper
    - *AP (Access Point), also called a WAP (Wireless Access Point) = L2 bridge between 802.11 wireless and the 802.3 wired LAN. It usually has an uplink to a switch and is often powered by PoE (Power over Ethernet).*
    - @1.2.appl ~2.19
14. A company with users worldwide wants its website's images and video served from servers near each user, to cut load times. Service?
    - [ ] VPN  - **[x] CDN**  - [ ] NAS  - [ ] SAN
    - *CDN (Content Delivery Network) = copies (caches) content on edge servers around the world, so users get it from the closest one: lower latency, faster loads, less load on the origin. Often uses anycast. A side benefit is DDoS (Distributed Denial of Service) absorption.*
    - @1.2.cdn ~2.21
15. Which uses a public network like the internet to create a private, encrypted connection between sites or users?
    - [ ] WWAN  - **[x] VPN**  - [ ] PAN  - [ ] VLAN
    - *VPN (Virtual Private Network) = an encrypted tunnel across an untrusted network (IPsec or SSL/TLS, Transport Layer Security). VLAN (Virtual LAN) = a logical segment on switches, not encrypted. PAN (Personal Area Network) = Bluetooth range. WWAN (Wireless WAN) = cellular.*
    - @1.2.func ~2.22
16. VoIP calls break up whenever someone downloads a big file. Which function lets the admin prioritise voice over the download?
    - [ ] NAC  - **[x] QoS**  - [ ] NAT  - [ ] UTM
    - *QoS (Quality of Service) = classify, mark (DSCP, Differentiated Services Code Point) and prioritise traffic, e.g. voice first, bulk downloads last. NAC (Network Access Control) = who may connect. NAT (Network Address Translation) = rewrites addresses. UTM (Unified Threat Management) = all-in-one security box.*
    - @1.2.func ~2.23
17. Which IP header field is decremented by 1 at each router, so the packet is discarded when it reaches 0?
    - [ ] ToS  - [ ] Options  - **[x] TTL**  - [ ] MTU
    - *TTL (Time To Live) = a hop counter that stops packets looping forever. traceroute abuses it: it sends TTL 1, 2, 3... and each router that drops one replies, revealing the path. MTU (Maximum Transmission Unit) = max packet size, 1500 bytes on Ethernet. ToS (Type of Service) = priority marking.*
    - @1.2.func ~2.24
18. What does TTL mean in an IP packet, and in a DNS record?
    - **[x] IP: hops before the packet dies; DNS: seconds it may be cached**  - [ ] IP: seconds it may be cached; DNS: hops before it dies  - [ ] Both count the hops a packet may cross  - [ ] Both count the seconds a record may be cached
    - *IP TTL counts hops (Windows starts at 128, Linux at 64). DNS (Domain Name System) TTL = how many seconds a resolver may cache a record. Lower the DNS TTL before a migration so changes spread fast.*
    - @1.2.func
19. A company replaces its physical firewall with a firewall VM running on the same hypervisor as its servers. What changed?
    - **[x] A physical appliance became a virtual appliance**  - [ ] The firewall moved from Layer 3 to Layer 7  - [ ] It became a SAN  - [ ] It no longer needs rules
    - *The objectives compare physical vs virtual appliances. Routers, switches, firewalls, load balancers and WLCs all come as virtual appliances too: fast to deploy, snapshot and scale, but they share the host's hardware. In the cloud this is NFV (Network Functions Virtualization).*
    - @1.2.appl
20. Three jobs, one device each: ¶  Slot 1 · one public IP spreads customers across Web1, Web2 and Web3, skipping any server that fails its health check ¶  Slot 2 · office PCs' outbound web goes through it: it caches pages and blocks banned sites ¶  Slot 3 · terminates encrypted tunnels from 200 home workers ¶Type the letters for slots 1, 2 and 3 in order, e.g. abc. ¶  A VPN concentrator · B load balancer · C forward proxy · D NAS · E IDS
    - [=] bca | b c a | b,c,a
    - *Slot 1 = B load balancer: one VIP (Virtual IP), health checks, spreads the pool. Slot 2 = C forward proxy: sits in front of USERS, caching and URL filtering. Slot 3 = A VPN (Virtual Private Network) concentrator, the headend for many remote-access tunnels. NAS (storage) and IDS (passive alerts) don't do any of these jobs.*
    - @1.2.appl ~31.6,31.7,31.8
21. Staff must be blocked from one file-sharing app that hops ports and hides inside HTTPS, while normal web browsing still works. Which firewall can do it?
    - [ ] A stateless packet filter, like a router ACL  - [ ] A stateful firewall that tracks sessions  - **[x] An NGFW with application awareness**  - [ ] A NAT gateway
    - *Answer: An NGFW with application awareness. Stateless = checks each packet's header (IP, port) alone, and return traffic needs its own rule. Stateful = tracks sessions, so replies are allowed automatically, but it still only sees IPs and ports. NGFW (Next-Generation Firewall) = stateful plus deep packet inspection: it identifies the APPLICATION whatever port it uses, and usually adds IPS and URL filtering. Port-hopping or hiding in 443 beats the first two. Hook: stateless = reads the envelope, stateful = remembers the conversation, NGFW = reads the letter.*
    - @1.2.appl
22. PBQ: Place each device and network, top to bottom: ¶  Internet ¶    │ ¶   (1) ───── (5) ── (3) ── public web + mail servers ¶    │ ¶   (2) ¶    │ ¶  core switch ── SPAN port ── (4) ¶    │ ¶  access switches ── (6) ~~~ laptops and phones, wireless ¶    │ ¶  wired users
    - [p] Slot 1, the three-legged edge device filtering by rules :: A firewall · B IPS · C IDS · D WAF · E NAC · F jump box = a
    - [p] Slot 2, inline, blocking attacks in real time :: A firewall · B IPS · C IDS · D WAF · E NAC · F jump box = b
    - [p] Slot 3, in front of the web servers, blocking SQL injection :: A firewall · B IPS · C IDS · D WAF · E NAC · F jump box = d
    - [p] Slot 4, watches a copy of traffic and alerts :: A firewall · B IPS · C IDS · D WAF · E NAC · F jump box = c
    - [p] Slot 5, the network on the firewall's second leg, holding the public servers :: A internal LAN · B DMZ, screened subnet · C guest VLAN · D management VLAN = b
    - [p] Slot 6, joins the wireless laptops and phones to the wired network :: A load balancer · B IDS · C access point · D WAF = c
    - *Answer: 1 firewall · 2 IPS · 3 WAF · 4 IDS · 5 DMZ · 6 access point. Firewall = three legs at the edge (internet, DMZ, LAN), the bouncer on the front door. IPS = inline, so it can drop. IDS = out of band on a SPAN or tap, sees a COPY, alert only (Detects and Dials for help; IPS Prevents). WAF (Web Application Firewall) = Layer 7 in front of web apps, stopping SQL injection and XSS. DMZ (demilitarized zone) / screened subnet = public servers reachable from the internet but isolated from the LAN, so a hacked web server can't reach inside. AP (Access Point) = bridges Wi-Fi to wired. NAC (Network Access Control) = posture/identity check before access, often 802.1X. Jump box = the single hardened admin entry point.*
    - @1.2.appl ~31.1,31.2,31.3,31.4,31.5

### Key facts
- **Router = L3, IP, between networks · switch = L2, MAC, within one network · hub = L1, repeats to all.**
- **Firewall = rules at the edge · IDS = passive copy (SPAN/tap), alerts · IPS = inline, blocks. Smoke alarm vs sprinkler.**
- **Load balancer = one VIP, spreads + health-checks a pool (round-robin, least connections, sticky) · forward proxy = in front of users · reverse proxy = in front of servers.**
- **NAS = file-level box on the LAN (SMB/NFS) · SAN = block-level on its own network (Fibre Channel, iSCSI, FCoE, InfiniBand).**
- **AP bridges Wi-Fi to wired · WLC centrally manages lightweight APs · CDN = content cached near users.**
- **Functions: VPN = encrypted tunnel · QoS = prioritise (voice first) · IP TTL = hops · DNS TTL = cache seconds. UTM = many security tools in one box.**

## Test 4 - 1.3/1.8 Cloud + SDN (30 Q)

1. A company wants its own isolated network, with its own subnets and routing, inside AWS. What is it called?
   - **[x] VPC**  - [ ] Private cloud  - [ ] VXLAN  - [ ] Intranet
   - *VPC (Virtual Private Cloud) = your own logically isolated network inside a PUBLIC cloud, with your own IP ranges, subnets, route tables and gateways. A private cloud = infrastructure dedicated to one organisation. VXLAN (Virtual Extensible LAN) = an overlay tunnelling tech.*
   - @1.3.nfv ~3.1
2. Firewalls, routers and load balancers run as VMs instead of dedicated boxes. What is this called?
   - [ ] SDN  - [ ] SVI  - **[x] NFV**  - [ ] VPC
   - *NFV (Network Functions Virtualization) = network BOXES turned into software (VMs, Virtual Machines, or containers). SDN (Software-Defined Networking) = centralising the CONTROL plane. SVI (Switch Virtual Interface) = a VLAN's routed interface on a switch. Hook: NFV = virtualise the Function (the box); SDN = software Decides (the brain).*
   - @1.3.nfv ~2.25
3. Which describe a cloud network security GROUP? (Select 2)
   - **[x] Firewall rules attached to individual instances or virtual NICs**  - **[x] Stateful: return traffic is allowed automatically**  - [ ] Applies to the whole subnet at once  - [ ] Stateless: return traffic needs its own rule
   - *Security group (AWS SG, Azure NSG, Network Security Group) = a stateful virtual firewall on each instance/NIC (Network Interface Card), so it's more granular. A security LIST / network ACL (NACL) = applies at the SUBNET level, often stateless. Hook: Group = on the guest; List = on the land (subnet).*
   - @1.3.sec ~3.2
4. Which describe a cloud network security LIST? (Select 2)
   - **[x] Filters traffic for a whole subnet**  - **[x] Less granular than per-instance rules**  - [ ] Only attaches to one virtual NIC  - [ ] Replaces the need for an internet gateway
   - *Security list (Oracle Cloud) / NACL (Network Access Control List, AWS) = subnet-level filtering, less granular. Security groups = instance/NIC level. Use both: the list as a coarse fence, the group as a per-server lock.*
   - @1.3.sec ~3.3
5. Which cloud gateway gives public-subnet instances two-way internet access?
   - [ ] NAT gateway  - **[x] Internet gateway**  - [ ] VPN gateway  - [ ] Transit gateway
   - *Internet gateway (IGW) = attaches a VPC (Virtual Private Cloud) to the internet, both ways, for instances with public IPs. NAT (Network Address Translation) gateway = outbound only, for private-subnet instances. VPN (Virtual Private Network) gateway = encrypted link to on-prem.*
   - @1.3.gw ~3.4
6. Private-subnet database servers need to download patches from the internet, but must never accept inbound connections from it. Gateway?
   - **[x] NAT gateway**  - [ ] Internet gateway  - [ ] Direct Connect  - [ ] Load balancer
   - *NAT (Network Address Translation) gateway = translates private IPs to a public IP for OUTBOUND traffic and drops unsolicited inbound. Hook: NAT gateway = a one-way door out.*
   - @1.3.gw ~3.5
7. A company needs an encrypted link from its office to its cloud VPC, over the public internet, set up today. Option?
   - **[x] Site-to-site VPN**  - [ ] Direct Connect  - [ ] Leased line  - [ ] Fibre Channel
   - *VPN (Virtual Private Network) = IPsec tunnel over the internet: cheap, quick, encrypted, but internet performance varies. Direct Connect (AWS) / ExpressRoute (Azure) = a dedicated private circuit to the provider: consistent bandwidth and latency, not over the internet, but it takes weeks to provision and costs more.*
   - @1.3.conn ~3.6
8. A bank needs guaranteed bandwidth and latency between its data centre and its cloud provider, not over the public internet. Option?
   - [ ] Site-to-site VPN  - **[x] Direct Connect**  - [ ] Client VPN  - [ ] Internet gateway
   - *Direct Connect / ExpressRoute = a dedicated private connection from your site (or a colocation facility) to the cloud provider. It isn't encrypted by default; add a VPN over it if encryption is required.*
   - @1.3.conn ~3.7
9. Which cloud deployment models are matched correctly? (Select 3)
   - **[x] Public = provider-owned, shared by many tenants**  - **[x] Private = dedicated to one organisation**  - **[x] Hybrid = public and private combined**  - [ ] Community = one company's on-prem servers only
   - *Public (AWS, Azure, GCP = Google Cloud Platform) = multi-tenant, pay as you go. Private = one organisation, on-prem or hosted. Hybrid = both, working together. Community = shared by organisations with common needs, e.g. several hospitals.*
   - @1.3.model ~3.8,3.9,3.10
10. A company uses Microsoft 365 email in a browser and manages nothing but its users. Service model?
    - [ ] IaaS  - [ ] PaaS  - **[x] SaaS**  - [ ] DaaS
    - *SaaS (Software as a Service) = finished software. IaaS (Infrastructure as a Service) = raw VMs, storage and networks: you manage the OS upwards. PaaS (Platform as a Service) = a ready platform for your code: you manage just the app and data. Hook, pizza: IaaS = buy the ingredients, PaaS = takeaway you bake at home, SaaS = eat at the restaurant.*
    - @1.3.model ~3.11
11. A developer wants to deploy code without managing servers, the OS or runtime patches. Model?
    - [ ] IaaS  - **[x] PaaS**  - [ ] SaaS  - [ ] On-prem
    - *PaaS (Platform as a Service) = provider runs the OS, runtime and middleware; you bring the code and data. IaaS (Infrastructure as a Service, raw VMs) would make you patch the OS yourself. SaaS = no code of your own at all.*
    - @1.3.model ~3.13,3.12
12. An online shop's web tier adds servers automatically during a Black Friday spike, then removes them after. Term?
    - [ ] Scalability  - **[x] Elasticity**  - [ ] Multitenancy  - [ ] Fault tolerance
    - *Elasticity = AUTOMATIC grow AND shrink with real-time demand. Scalability = the ABILITY to grow to handle more load, often planned (scale up = bigger box, scale out = more boxes). Hook: elastic snaps back.*
    - @1.3.scale ~3.15,3.14
13. Many customers' workloads run isolated from each other on the same shared cloud hardware. Term?
    - **[x] Multitenancy**  - [ ] Elasticity  - [ ] Sandboxing  - [ ] Clustering
    - *Multitenancy = many tenants (customers) sharing the same infrastructure, logically isolated. It's why public cloud is cheap. The risk: a flaw in the isolation could leak between tenants.*
    - @1.3.scale ~3.16
14. Branch policy steers Teams traffic onto the private carrier link while software updates go out the cheap internet circuit. Which SD-WAN trait is this?
    - [ ] Transport agnostic  - **[x] Application aware**  - [ ] Zero-touch provisioning  - [ ] Link aggregation
    - *Application awareness lets the SD-WAN identify each flow by application and pick a path for it according to policy and measured link health such as latency, jitter and loss. Link aggregation just bonds links and ignores what the traffic is.*
    - @1.8.sdn ~25.1
15. A retailer's SD-WAN overlay runs equally well whether a store is connected by LTE, DSL, fibre or a carrier label-switched circuit. Which trait?
    - [ ] Application aware  - **[x] Transport agnostic**  - [ ] Central policy management  - [ ] Quality of Service tagging
    - *Transport agnostic means the overlay is independent of the underlay: the SD-WAN builds its encrypted tunnels across whatever circuits are available, whether MPLS, cellular, DSL or fibre.*
    - @1.8.sdn ~25.2
16. A pharmacy chain mails edge appliances to stores; a clerk connects power and WAN, and the box registers itself and downloads its settings. What feature?
    - [ ] Out-of-band management  - **[x] Zero-touch provisioning**  - [ ] Dynamic inventory  - [ ] Configuration drift
    - *Zero-touch provisioning lets a new device locate its controller on first boot, often through DHCP options or a vendor cloud service, and pull configuration and firmware without anyone at the site using a console. Out-of-band management is a separate admin path, not auto-setup. Dynamic inventory tracks which devices exist, and configuration drift is unplanned divergence from a baseline. Neither builds a new device automatically.*
    - @1.8.sdn ~25.3
17. A company moves to zero trust. A contractor needs access to ONE internal billing app for two weeks. Which approach follows zero trust?
    - **[x] Grant per-session access to that app only, after MFA and a device check, expiring in two weeks**  - [ ] Put the contractor on the internal LAN, since that network is trusted  - [ ] Give full VPN access so they can find what they need  - [ ] Share an admin account to save time
    - *Zero trust = never trust, always verify. Every request is authenticated and authorised against policy (who, which device, what, when), with least privilege: just the one app, just for the time needed. Being on the LAN or a VPN earns no trust by itself.*
    - @1.8.zta ~9.2
18. A cloud provider hosting thousands of tenants has run out of VLAN IDs. What is the main reason to move to VXLAN?
    - **[x] About 16 million segments instead of 4094**  - [ ] It encrypts all traffic  - [ ] It removes the need for IP routing  - [ ] It replaces Spanning Tree with link aggregation
    - *An 802.1Q VLAN ID is 12 bits, giving 4094 usable networks. VXLAN tunnels Layer 2 over UDP and identifies segments with a 24-bit VNI, roughly 16 million, which is why large multi-tenant clouds adopt it. It does not encrypt on its own. It still relies on an IP underlay and does not replace STP.*
    - @1.8.vxlan ~9.3
19. How does VXLAN stretch one Layer 2 network across two data centres?
    - [ ] It uses a longer trunk cable  - **[x] It wraps Layer 2 frames in UDP/IP packets**  - [ ] It converts frames to MPLS labels  - [ ] It uses STP between sites
    - *Answer: It wraps Layer 2 frames in UDP/IP packets. VXLAN = Layer 2 encapsulation: the Ethernet frame is wrapped inside UDP (port 4789) over IP, so it can cross any routed L3 network. The endpoints are VTEPs (VXLAN Tunnel End Points). Linking data centres like this = DCI (Data Center Interconnect).*
    - @1.8.vxlan ~9.5,9.4
20. A user on the office LAN is still asked to re-authenticate, and their device is checked, before reaching each app. Model?
    - [ ] Perimeter security  - **[x] Zero trust architecture**  - [ ] Defence in depth  - [ ] Implicit trust
    - *ZTA (Zero Trust Architecture) = never trust, always verify. Being "inside" grants nothing: every request gets policy-based authentication (identity, device health, location), authorisation, and least-privilege access. Old model = castle and moat, trusting everything inside.*
    - @1.8.zta ~9.6
21. Which service combines SD-WAN networking and cloud security into one cloud-delivered service?
    - **[x] SASE**  - [ ] SSE  - [ ] SIEM  - [ ] SWG
    - *SASE (Secure Access Service Edge) = SD-WAN + SSE, delivered from the cloud. SSE (Security Service Edge) = just the security half: SWG (Secure Web Gateway), CASB (Cloud Access Security Broker), ZTNA (Zero Trust Network Access). Hook: SASE = SSE + SD-WAN.*
    - @1.8.sase ~9.7,9.8
22. Remote staff connect straight to SaaS apps. The company wants web filtering, CASB and zero trust access delivered from the cloud, but keeps its existing WAN. Which fits?
    - **[x] SSE**  - [ ] SASE  - [ ] SD-WAN only  - [ ] A bigger on-site firewall
    - *SSE (Security Service Edge) = the cloud SECURITY half: SWG (Secure Web Gateway), CASB (Cloud Access Security Broker), ZTNA (Zero Trust Network Access). SASE (Secure Access Service Edge) = SSE plus SD-WAN networking in one service. Keeping the existing WAN = SSE. Hook: SASE = SSE + SD-WAN.*
    - @1.8.sase ~9.9,9.10
23. One router is running a different config from the one in the IaC repository, because someone changed it by hand. Term?
    - [ ] Version control  - **[x] Configuration drift**  - [ ] Branching  - [ ] Dynamic inventory
    - *Configuration drift = the real device no longer matches the defined state. IaC (Infrastructure as Code) fixes it by re-applying the code and flagging non-compliance. Playbook = an ordered set of automation tasks (e.g. Ansible); template = a reusable config with variables.*
    - @1.8.iac ~9.11
24. A playbook queries AWS at run time to discover which EC2 instances to configure rather than reading a static list. What concept is this?
    - [ ] Configuration drift  - [ ] Golden configuration  - **[x] Dynamic inventory**  - [ ] Playbook templating
    - *With a dynamic inventory the automation tool builds its target list from a live system such as a cloud API, a CMDB or IPAM each time it runs, so added and retired hosts are handled automatically. A static inventory is a manually edited file.*
    - @1.8.iac ~25.4,9.12
25. Two engineers edit the same lines of a config template in Git, and Git refuses to auto-merge. Feature?
    - [ ] Branching  - **[x] Conflict identification**  - [ ] Rollback  - [ ] Central repository
    - *Answer: Conflict identification. Source control terms: version control = history of every change, with rollback. Central repository = the single shared source of truth. Branching = work on a separate copy, then merge back. Conflict identification = overlapping edits get flagged for a human to choose.*
    - @1.8.iac ~25.5,9.13,9.14,9.15
26. Match each need to a service model. Type the letters in order, e.g. abc. ¶  Needs: rent VMs and patch your own OS · deploy code only, no servers · use webmail in a browser ¶  A SaaS · B IaaS · C PaaS
    - [=] bca | b c a | b,c,a
    - *IaaS = you manage the OS up. PaaS = you manage just the code and data. SaaS = you just use it. The provider's share grows left to right.*
    - @1.3.model
27. A company's AWS VPC needs three connections. Pick one for each: ¶  Slot 1 · web servers in the PUBLIC subnet must be reachable from the internet, both ways ¶  Slot 2 · database servers in the PRIVATE subnet may reach out for patches, but nothing may connect in ¶  Slot 3 · the office links to the VPC, ENCRYPTED, running OVER the public internet ¶Type the letters for slots 1, 2 and 3 in order, e.g. abc. ¶  A NAT gateway · B Direct Connect · C internet gateway · D site-to-site VPN · E transit gateway
    - [=] cad | c a d | c,a,d
    - *1 = C internet gateway, two-way for public subnets. 2 = A NAT (Network Address Translation) gateway, outbound only for private subnets. 3 = D site-to-site VPN (Virtual Private Network): an IPsec tunnel over the internet. B Direct Connect is the trap: a private dedicated circuit that does NOT go over the internet and isn't encrypted by default. E transit gateway joins many VPCs together. Hook: "over the internet + encrypted" = VPN; "not over the internet" = Direct Connect.*
    - @1.3.gw
28. Match each SD-WAN feature. Type the letters in order, e.g. abcd. ¶  Needs: steers by app · works over any link · plug-in auto-config · policy set once for every site ¶  A transport agnostic · B central policy management · C application aware · D zero-touch provisioning
    - [=] cadb | c a d b | c,a,d,b
    - *Steers by app = C application aware. Any link = A transport agnostic. Auto-config = D zero-touch provisioning. Set policy once = B central policy management. Those are the four SD-WAN characteristics in the objectives.*
    - @1.8.sdn
29. Match each term. Type the letters in order, e.g. abcd. ¶  Terms: VXLAN · ZTA · SASE · SSE ¶  A never trust, always verify · B SD-WAN plus cloud security · C Layer 2 over UDP, 16 million segments · D cloud security only
    - [=] cabd | c a b d | c,a,b,d
    - *VXLAN = C, Layer 2 encapsulation over UDP/IP with a 24-bit ID. ZTA (Zero Trust Architecture) = A. SASE (Secure Access Service Edge) = B, SD-WAN + SSE. SSE (Security Service Edge) = D, just the security half.*
    - @1.8.sase
30. Match each IaC term. Type the letters in order, e.g. abcd. ¶  Needs: a hand change makes a device differ from the repo · a separate copy of the code to test a change · pull hosts live from the cloud API · the single shared source of truth ¶  A central repository · B dynamic inventory · C configuration drift · D branching
    - [=] cdba | c d b a | c,d,b,a
    - *Hand change = C drift. Separate copy = D branching. Live host list = B dynamic inventory. Single source of truth = A central repository.*
    - @1.8.iac

### Key facts
- **VPC = your isolated network in a public cloud · NFV = network boxes as VMs · SDN = central control plane.**
- **Security group = per instance/NIC, stateful · security list / NACL = per subnet.**
- **Internet gateway = two-way internet · NAT gateway = outbound only · VPN = encrypted over the internet · Direct Connect/ExpressRoute = private dedicated circuit.**
- **IaaS (you run the OS) · PaaS (just your code) · SaaS (just use it). Public / private / hybrid / community.**
- **Elasticity = auto grow AND shrink · scalability = able to grow · multitenancy = shared hardware, isolated tenants.**
- **SD-WAN: application aware · transport agnostic · zero-touch provisioning · central policy management.**
- **VXLAN = L2 in UDP/IP, 24-bit VNI (16M segments vs 4094 VLANs), DCI. ZTA = never trust, always verify. SASE = SD-WAN + SSE.**
- **IaC: playbooks, templates, drift, dynamic inventory · source control: version control, central repo, branching, conflict identification.**

## Test 5 - 1.4 Ports (26 Q)

1. Type the TWO port numbers FTP uses, data first, separated by a space.
   - [=] 20 21 | 20/21 | 20,21 | 20, 21
   - *FTP (File Transfer Protocol) = TCP 20 for DATA, TCP 21 for CONTROL (the commands and login). It's cleartext, so it's insecure. Hook: 21 is the grown-up that gives the orders; 20 does the lifting.*
   - @1.4.ports ~4.13,4.14,3.17
2. Opening TCP 22 on a firewall allows which traffic? (Select 2)
   - **[x] SSH**  - **[x] SFTP**  - [ ] FTPS  - [ ] Telnet
   - *SFTP (SSH File Transfer Protocol) is file transfer INSIDE an SSH (Secure Shell) session, so it uses 22 too. FTPS (FTP Secure) = FTP wrapped in TLS, which uses 990/989 or explicit TLS on 21. Telnet = 23.*
   - @1.4.ports ~4.16,4.17,3.18
3. A scan shows a router still accepting cleartext remote CLI logins. Type the port you should close.
   - [=] 23
   - *Telnet = TCP 23, remote command line in CLEARTEXT: passwords can be sniffed. Replace it with SSH on 22. Hook: 22 = secure, 23 = the older, insecure brother one number up.*
   - @1.4.ports ~4.18,3.20,3.21
4. The company's mail server must accept email relayed from other mail servers on the internet. Type the port to open inbound.
   - [=] 25
   - *SMTP (Simple Mail Transfer Protocol) = TCP 25, server-to-server mail SENDING. Clients submitting mail securely use 587 (SMTPS / submission with TLS). Hook: SMTP = Send Mail To People; 25 = a quarter, posting a letter.*
   - @1.4.ports ~4.19,3.22
5. Clients can ping 8.8.8.8 but can't resolve names, and a new firewall rule is suspected. Type the port the rule must allow.
   - [=] 53
   - *DNS (Domain Name System) = port 53, UDP for normal lookups and TCP for zone transfers and large replies. Hook: 53 looks like "S3" = the name-to-IP lookup service. It's the only one on the list that's commonly UDP AND TCP.*
   - @1.4.ports ~4.20,3.23
6. A secondary DNS server can't finish a zone transfer from the primary. The firewall between them allows only UDP 53. Type the protocol and port to add, e.g. tcp 25.
   - [=] tcp 53 | 53 tcp | tcp/53 | 53/tcp
   - *DNS lookups use UDP 53, but zone transfers (AXFR, copying the whole zone to a secondary) and big replies use TCP 53. Hook: small question = UDP postcard, whole zone = TCP parcel.*
   - @1.4.ports
7. Type the DHCP SERVER port, then the DHCP CLIENT port, separated by a space.
   - [=] 67 68 | 67/68
   - *DHCP (Dynamic Host Configuration Protocol) = UDP 67 on the server, UDP 68 on the client. Hook: the server is older (67), the client is one year younger (68). It replaces manual IP allocation.*
   - @1.4.ports ~4.21,4.22,3.24
8. A switch must pull its firmware image from a TFTP server during an upgrade. Type the port the ACL must allow.
   - [=] 69
   - *TFTP (Trivial File Transfer Protocol) = UDP 69. No login, no encryption, no directory listing: used to push firmware and config files to switches, routers and IP phones. Hook: trivial = UDP, no handshake.*
   - @1.4.ports ~4.23,3.25
9. A web server should redirect unencrypted visitors to HTTPS, so it still listens on the plain web port. Type it.
   - [=] 80
   - *HTTP (HyperText Transfer Protocol) = TCP 80, unencrypted web. HTTPS = 443. Hook: 80 = the ordinary 80s web.*
   - @1.4.ports ~4.24,4.1
10. Log timestamps on every switch are drifting apart. Type the port the firewall must allow to the time server.
    - [=] 123
    - *NTP (Network Time Protocol) = UDP 123. It synchronises clocks, which logs, Kerberos and certificates all depend on. Hook: 1-2-3, like counting seconds.*
    - @1.4.ports ~4.25,4.2
11. Type the port an SNMP AGENT listens on for requests, then the port the MANAGER receives traps on, separated by a space.
    - [=] 161 162 | 161/162
    - *SNMP (Simple Network Management Protocol) = UDP 161 for polls/requests TO the agent on each device, UDP 162 for traps sent FROM the agent to the manager. Hook: 162 is one more, because the trap is the device calling back.*
    - @1.4.ports ~5.1,5.2,4.3
12. An app authenticates users against the directory, unencrypted, and the new firewall broke it. Type the port it needs.
    - [=] 389
    - *LDAP (Lightweight Directory Access Protocol) = TCP/UDP 389, queries directories like Active Directory for users and groups. It's cleartext. LDAPS (LDAP Secure, over SSL/TLS) = 636.*
    - @1.4.ports ~5.3,4.4
13. A new internal web app must be reachable only over TLS. Type the port to allow.
    - [=] 443
    - *HTTPS (HTTP Secure) = TCP 443, web over TLS (Transport Layer Security). Also used by many VPNs and APIs. Hook: 443 = the padlock port.*
    - @1.4.ports ~5.4,4.5
14. Users can't open files on a Windows file share after a firewall change. Type the port to allow.
    - [=] 445
    - *SMB (Server Message Block) = TCP 445, Windows file and printer sharing. Never expose it to the internet: WannaCry spread through 445. Hook: 443 is web, 445 is Windows shares, two doors down.*
    - @1.4.ports ~5.5,4.6
15. A new log collector receives nothing from the routers. Type the default port the collector must listen on.
    - [=] 514
    - *Syslog = UDP 514, devices sending log messages to a central syslog collector or SIEM (Security Information and Event Management). Severity levels 0 (emergency) to 7 (debug). Hook: 514, "five-one-four, log it on the floor". It is UDP, so logs can be lost silently.*
    - @1.4.ports ~5.6,4.7
16. Staff laptops must send email securely through the company mail server. Type the SMTPS port to allow.
    - [=] 587
    - *SMTPS / mail submission = TCP 587, a mail client sending mail securely via STARTTLS (RFC 6409; server-to-server relay stays on 25). Some sources loosely say 587 = 'mail between servers'; either way, pick the email answer. Port 465 = implicit TLS from the first byte (re-standardised by RFC 8314), but the exam answer for SMTPS is 587. Port 25 = plain server-to-server SMTP. Hook: 5-8-7, the SECURE SEND.*
    - @1.4.ports ~5.7,4.8
17. The auditor says directory lookups must be encrypted. Type the port the app should now use.
    - [=] 636
    - *LDAPS (LDAP over SSL/TLS) = TCP 636. Plain LDAP = 389. Hook: 636 reads the same both ways, a sealed envelope; LDAP (389) goes in open, LDAPS (636) comes back sealed.*
    - @1.4.ports ~5.8,4.9
18. A web server in the DMZ must query a Microsoft SQL Server on the inside. Type the port the rule should allow.
    - [=] 1433
    - *SQL (Structured Query Language) Server = TCP 1433, Microsoft's database. It IS on the objectives (1.4). Not on them: MySQL 3306, PostgreSQL 5432, Oracle 1521. Never expose database ports to the internet. Hook: 1433 = "1 for the 4 walls of the 3-3 database" - or just drill it; it's one of the few you have to learn by rote.*
    - @1.4.ports ~5.9,4.10,27.23
19. A scan finds Windows remote desktop exposed to the internet on a server. Type the port you should block.
    - [=] 3389
    - *RDP (Remote Desktop Protocol) = TCP 3389 (UDP too), Microsoft's graphical remote control of another Windows host. Heavily attacked when exposed. Hook: 33-89, double 3s then 89.*
    - @1.4.ports ~5.10,4.11
20. Type the SIP port for UNENCRYPTED signalling, then the SIP over TLS port, separated by a space.
    - [=] 5060 5061 | 5060/5061
    - *SIP (Session Initiation Protocol) = 5060 plain, 5061 over TLS. SIP sets up, manages and ends VoIP calls, video and chat sessions. The voice itself travels in RTP (Real-time Transport Protocol) on other ports. Hook: 61 is 60 with a padlock on.*
    - @1.4.ports ~5.11,5.12,4.12
21. A new SIEM at 10.0.5.20 must receive logs from every switch, and the firewall between them blocks everything by default. Which rule is needed?
    - **[x] Allow UDP 514 to 10.0.5.20**  - [ ] Allow TCP 161 to 10.0.5.20  - [ ] Allow UDP 162 from 10.0.5.20  - [ ] Allow TCP 389 to 10.0.5.20
    - *Syslog = UDP 514 by default, from the devices to the collector. SNMP (Simple Network Management Protocol) polling = UDP 161 and traps = UDP 162, both UDP, not TCP. LDAP (Lightweight Directory Access Protocol) = 389. SIEM = Security Information and Event Management.*
    - @1.4.ports ~26.1
22. A browser on a workstation connects to a server on 443 using local port 51514. What category does 51514 fall into?
    - [ ] Well-known  - [ ] Registered  - **[x] Dynamic / ephemeral**  - [ ] Privileged
    - *Answer: Dynamic / ephemeral. Ports 49152-65535 are the dynamic range that client operating systems borrow for the life of a connection. Well-known is 0-1023 and registered is 1024-49151. Return traffic targets the ephemeral port, so stateless filters must permit that range.*
    - @1.4.ports ~26.2
23. Which are the SECURE versions of these insecure protocols? (Select 3)
    - **[x] Telnet 23 → SSH 22**  - **[x] HTTP 80 → HTTPS 443**  - **[x] LDAP 389 → LDAPS 636**  - [ ] SMTP 25 → SMB 445  - [ ] FTP 21 → TFTP 69
    - *Insecure to secure pairs: Telnet → SSH, HTTP → HTTPS, LDAP → LDAPS, FTP → SFTP (22) or FTPS, SMTP 25 → SMTPS 587, SIP 5060 → 5061, SNMPv1/v2c → SNMPv3 (same ports, adds encryption). TFTP is LESS secure than FTP. SMB is file sharing, not mail.*
    - @1.4.ports
24. Which of these use UDP, not TCP? (Select 4)
    - **[x] DHCP 67/68**  - **[x] TFTP 69**  - **[x] NTP 123**  - **[x] Syslog 514**  - [ ] SSH 22  - [ ] HTTPS 443
    - *On the list, the UDP ones are DHCP, TFTP, NTP, SNMP (161/162) and syslog, plus DNS for normal lookups. SSH, Telnet, SMTP, HTTP(S), SMB, LDAP(S), RDP and SQL = TCP. Hook: the "fire and forget" services (time, logs, small files, addresses) are UDP.*
    - @1.4.ports
25. netstat shows these LISTENING ports on a server: 21, 23, 69, 80, 443. Company policy is encrypted protocols only. Type the ports to CLOSE, separated by spaces, lowest first.
    - [=] 21 23 69 80
    - *21 FTP, 23 Telnet, 69 TFTP and 80 HTTP are all cleartext. Only 443 (HTTPS) is encrypted. Replace them with SFTP 22, SSH 22 and HTTPS 443.*
    - @1.4.ports
26. Match each port to its service. Type the letters in order, e.g. abcd. ¶  Ports: 69 · 162 · 1433 · 5061 ¶  A SNMP traps · B LDAPS · C SIP over TLS · D TFTP · E Microsoft SQL Server
    - [=] daec | d a e c | d,a,e,c
    - *69 = TFTP · 162 = SNMP traps · 1433 = Microsoft SQL Server · 5061 = SIP over TLS.*
    - @1.4.ports

### Key facts
- **20/21 FTP (data/control) · 22 SSH/SFTP/SCP · 23 Telnet · 25 SMTP · 53 DNS · 67/68 DHCP (server/client) · 69 TFTP · 80 HTTP.**
- **123 NTP · 161/162 SNMP (agent/traps) · 389 LDAP · 443 HTTPS · 445 SMB · 514 syslog · 587 SMTPS · 636 LDAPS.**
- **1433 MSSQL · 3389 RDP · 5060/5061 SIP (plain/TLS).**
- **UDP: DHCP, TFTP, NTP, SNMP, syslog, DNS lookups. TCP: everything else on the list (DNS zone transfers use TCP).**
- **Secure swaps: Telnet → SSH · HTTP → HTTPS · LDAP → LDAPS · FTP → SFTP · SMTP 25 → 587 · SIP 5060 → 5061 · SNMPv2c → v3.**
- **Client source ports are temporary high ports (ephemeral). Servers listen on the well-known port.**

## Test 6 - 1.4 Protocols + Casts (24 Q)

1. A file transfer must arrive complete and in order, even over a lossy link. Which features of TCP make that happen? (Select 3)
   - **[x] Connection-oriented, with a three-way handshake**  - **[x] Sequencing, acknowledgements and retransmission**  - **[x] Used by web, email, SSH and file transfer**  - [ ] Connectionless and best-effort  - [ ] Preferred for live voice and video
   - *TCP (Transmission Control Protocol) = reliable: handshake, sequence numbers, ACKs, retransmits lost segments, flow control. UDP (User Datagram Protocol) = connectionless, no guarantees, lower overhead. Hook: TCP = recorded delivery with a signature; UDP = a postcard.*
   - @1.4.ip ~5.14
2. A VoIP system uses UDP for its audio. Which UDP traits explain why? (Select 3)
   - **[x] Connectionless, no handshake**  - **[x] No retransmission of lost data**  - **[x] Preferred for VoIP, video streaming, DNS lookups and DHCP**  - [ ] Guarantees in-order delivery  - [ ] Uses SYN and ACK flags
   - *UDP (User Datagram Protocol) = fire and forget: small header, fast, no recovery. Real-time voice/video would rather drop a packet than wait for a resend. The app handles any reliability it needs.*
   - @1.4.ip ~5.15
3. Which is the TCP three-way handshake, in order?
   - **[x] SYN, SYN-ACK, ACK**  - [ ] SYN, ACK, SYN-ACK  - [ ] ACK, SYN, FIN  - [ ] SYN, SYN-ACK, FIN
   - *Client SYN (synchronise) → server SYN-ACK → client ACK (acknowledge), then data flows. A connection is torn down with FIN (finish), or aborted with RST (reset). A SYN flood sends SYNs and never ACKs, filling the server's half-open table.*
   - @1.4.ip
4. A host sends a SYN to a closed port. What does it usually get back?
   - [ ] SYN-ACK  - **[x] RST**  - [ ] FIN  - [ ] Nothing ever
   - *A closed TCP port replies RST (reset). An open port replies SYN-ACK. No reply at all usually means a firewall is silently dropping it (nmap calls that "filtered"). This is how port scanners work.*
   - @1.4.ip
5. A firewall blocks ALL traffic except TCP and UDP. Now ping and traceroute both fail, though web browsing works. Which protocol was blocked?
   - [ ] CCMP  - [ ] RSTP  - **[x] ICMP**  - [ ] SNMP
   - *ICMP (Internet Control Message Protocol) = L3 diagnostics and errors: echo request/reply (ping), time exceeded (traceroute), destination unreachable. No ports: it rides directly on IP as protocol 1. CCMP = WPA2 Wi-Fi encryption; RSTP = Rapid Spanning Tree; SNMP = device monitoring.*
   - @1.4.ip ~5.13
6. Which ICMP message does a router send back when a packet's TTL hits 0, which is what traceroute relies on?
   - **[x] Time exceeded**  - [ ] Echo reply  - [ ] Redirect  - [ ] Source quench
   - *Traceroute sends packets with TTL (Time To Live) 1, 2, 3... Each router that decrements it to 0 drops it and returns ICMP "time exceeded", revealing that hop. Ping = echo request / echo reply. "Destination unreachable" = no route or the port/host is closed.*
   - @1.4.ip
7. Which statements about the tunneling protocol that uses IP protocol number 47 are correct? (Select 3)
   - **[x] Tunnels other protocols inside IP, point to point**  - **[x] Can carry multicast and routing protocols**  - **[x] Provides NO encryption on its own**  - [ ] Encrypts and authenticates every packet  - [ ] Requires TLS certificates on both endpoints
   - *IP protocol 47 is GRE (Generic Routing Encapsulation). It is a lightweight point-to-point wrapper that can carry multicast and routing protocol traffic such as OSPF, but it offers no confidentiality or authentication, so it is commonly protected with IPsec. GRE uses no certificates or TLS.*
   - @1.4.ip ~5.16
8. Two sites must exchange OSPF updates through a tunnel, and the security team requires confidentiality. Which design is typical?
   - [ ] GRE alone  - **[x] GRE inside IPsec**  - [ ] SSH port forwarding  - [ ] IPsec AH alone
   - *GRE over IPsec is the usual pairing: GRE handles the multicast routing updates that plain policy-based IPsec cannot, and IPsec ESP then encrypts the GRE packets. AH authenticates but provides no encryption, and SSH forwarding does not carry routing protocols. GRE alone carries OSPF but sends it unencrypted, so it fails the confidentiality requirement.*
   - @1.4.ip ~25.13
9. A regulator requires proof that packets between two sites weren't altered, but the data itself may travel in the clear. Which IPsec protocol meets exactly that?
   - [ ] ESP  - **[x] AH**  - [ ] IKE  - [ ] SHA
   - *AH (Authentication Header, IP protocol 51) = proves the packet is genuine and unchanged, but anyone can read it. ESP (Encapsulating Security Payload, IP protocol 50) = encryption + integrity. Hook: AH = "Authentic, Honest, but naked"; ESP = "Encrypts the Secret Payload".*
   - @1.4.ipsec ~5.17
10. A site-to-site VPN must keep payroll data confidential in transit. Which IPsec protocol provides the encryption?
    - [ ] DES  - **[x] ESP**  - [ ] AH  - [ ] RC4
    - *ESP (Encapsulating Security Payload) = confidentiality (encryption) plus integrity and authentication. DES (Data Encryption Standard) and RC4 (Rivest Cipher 4) are cipher algorithms, not IPsec protocols, and both are obsolete.*
    - @1.4.ipsec ~5.18
11. A new IPsec tunnel never comes up, and the firewall log shows UDP 500 being dropped. Which IPsec component is being blocked?
    - [ ] AH  - [ ] ESP  - **[x] IKE**  - [ ] GRE
    - *IKE (Internet Key Exchange) = the handshake: authenticates the peers and builds SAs (Security Associations) and keys. UDP 500, or UDP 4500 with NAT-T (NAT Traversal) when a NAT device is in the path. Then ESP or AH carries the data.*
    - @1.4.ipsec ~5.19,25.14
12. A site-to-site VPN crosses a NAT router and AH keeps failing, while ESP with NAT-T works. Why?
    - **[x] AH signs the IP header, and NAT changes it**  - [ ] AH only works over IPv6 tunnels  - [ ] AH encrypts the header, and NAT can't read it  - [ ] AH needs TCP 500, which NAT blocks
    - *AH (Authentication Header) protects the outer IP header too, so when NAT (Network Address Translation) rewrites the address, the integrity check fails. ESP (Encapsulating Security Payload) doesn't cover the outer header, and NAT-T wraps it in UDP 4500 so it can pass through NAT. That's another reason ESP is what's used in practice.*
    - @1.4.ipsec
13. Which IPsec mode encrypts the WHOLE original packet, including its IP header, and adds a new header, as used between two VPN gateways?
    - **[x] Tunnel mode**  - [ ] Transport mode  - [ ] Aggressive mode  - [ ] Main mode
    - *Tunnel mode = the entire original packet is wrapped in a new IP header: gateway to gateway (site-to-site VPN). Transport mode = only the payload is protected and the original header is kept: host to host. Main/aggressive mode = IKE phase 1 negotiation styles.*
    - @1.4.ipsec
14. Which are the IP protocol numbers for ESP, AH and GRE, in that order?
    - **[x] 50, 51, 47**  - [ ] 51, 50, 47  - [ ] 47, 50, 51  - [ ] 500, 4500, 47
    - *These are IP PROTOCOL numbers, not ports: ESP 50, AH 51, GRE 47 (ICMP = 1, TCP = 6, UDP = 17). A firewall passing IPsec must allow ESP (50) and UDP 500/4500 for IKE. Hook: Encryption comes first, so ESP = 50 and AH = 51 right after it; GRE sits just below at 47.*
    - @1.4.ipsec
15. An admin SSHes from her PC to one switch. Traffic type?
    - **[x] Unicast**  - [ ] Anycast  - [ ] Multicast  - [ ] Broadcast
    - *Unicast = one to one. Most traffic is unicast: web, SSH, the reply to an ARP request.*
    - @1.4.cast ~5.20
16. A video feed is sent once and received only by the hosts that joined its group, 239.1.1.1. Traffic type?
    - [ ] Unicast  - [ ] Anycast  - **[x] Multicast**  - [ ] Broadcast
    - *Multicast = one to many subscribed receivers, using 224.0.0.0-239.255.255.255 (class D) in IPv4 and ff00::/8 in IPv6. Hosts join groups with IGMP (Internet Group Management Protocol). It saves bandwidth versus sending a separate copy to each viewer.*
    - @1.4.cast ~5.21
17. Users around the world hit the same DNS address, 1.1.1.1, and are routed to the nearest server. Traffic type?
    - [ ] Unicast  - **[x] Anycast**  - [ ] Multicast  - [ ] Broadcast
    - *Anycast = one address announced from many locations; routing (usually BGP) delivers each user to the nearest one. Used by DNS root servers and CDNs (Content Delivery Networks). Works in IPv4 and IPv6.*
    - @1.4.cast ~5.22,9.19
18. A DHCP Discover goes to every host on the local segment. Traffic type?
    - [ ] Unicast  - [ ] Anycast  - [ ] Multicast  - **[x] Broadcast**
    - *Broadcast = one to all on the segment: 255.255.255.255 or the subnet's broadcast address, MAC FF:FF:FF:FF:FF:FF. Routers do NOT forward broadcasts, which is why DHCP needs a relay across subnets. IPv6 has NO broadcast; it uses multicast instead.*
    - @1.4.cast ~5.23
19. Which statement about IPv6 traffic types is correct?
    - **[x] IPv6 has no broadcast; multicast does that job**  - [ ] IPv6 has no multicast  - [ ] IPv6 has no anycast  - [ ] IPv6 broadcasts to ff:ff:ff:ff
    - *IPv6 = unicast, multicast and anycast, but no broadcast. The all-nodes multicast group ff02::1 replaces it, and neighbour discovery uses multicast instead of ARP broadcasts.*
    - @1.4.cast
20. Match TCP or UDP to each. Type the letters in order, e.g. aaaaa. ¶  Items: web browsing · a VoIP call's audio · DNS lookup · SSH login · DHCP ¶  A TCP · B UDP
    - [=] abbab | a b b a b | a,b,b,a,b
    - *Web (HTTPS) = TCP. VoIP audio (RTP) = UDP, since late audio is useless. DNS lookups = UDP (zone transfers = TCP). SSH = TCP. DHCP = UDP, because the client has no IP yet to hold a connection.*
    - @1.4.ip
21. A capture shows: ¶  $ sudo tcpdump -n port 443 ¶10.0.0.5.51000 > 10.0.0.9.443: Flags S ¶10.0.0.9.443 > 10.0.0.5.51000: Flags S. ¶10.0.0.5.51000 > 10.0.0.9.443: Flags . ¶What just completed?
    - **[x] The TCP three-way handshake**  - [ ] A TCP connection teardown  - [ ] A port scan finding a closed port  - [ ] A UDP exchange
    - *S = SYN, S. = SYN-ACK, . = ACK: the TCP three-way handshake to HTTPS (443). The client's port 51000 is ephemeral. tcpdump prints flags this way.*
    - @1.4.ip
22. Match each job to its IPsec component. Type the letters in order, e.g. abc. ¶  Jobs: builds the tunnel and keys · integrity only, no encryption · encryption plus integrity ¶  A ESP · B IKE · C AH · D GRE
    - [=] bca | b c a | b,c,a
    - *IKE (UDP 500/4500) negotiates. AH (protocol 51) = integrity + authentication only. ESP (protocol 50) = encryption + integrity.*
    - @1.4.ipsec
23. A firewall must pass a site-to-site IPsec VPN that goes through NAT. Type the three numbers, separated by spaces: the IKE port, the NAT-T port, then the ESP protocol number.
    - [=] 500 4500 50
    - *IKE = UDP 500, NAT-T = UDP 4500, ESP = IP protocol 50. AH (51) won't survive NAT, so it isn't needed here.*
    - @1.4.ipsec
24. Match each to its traffic type. Type the letters in order, e.g. abcd. ¶  Items: ARP request · DNS root server lookup · IPTV channel joined via IGMP · SSH session ¶  A unicast · B multicast · C broadcast · D anycast
    - [=] cdba | c d b a | c,d,b,a
    - *ARP request = broadcast (FF:FF:FF:FF:FF:FF). Root DNS = anycast (nearest instance). IGMP-joined IPTV = multicast. SSH = unicast.*
    - @1.4.cast

### Key facts
- **TCP = handshake SYN → SYN-ACK → ACK, reliable, ordered, retransmits · UDP = connectionless, fast, no retransmit (voice, video, DNS, DHCP).**
- **Closed port replies RST · open port replies SYN-ACK · no reply = filtered by a firewall.**
- **ICMP = ping (echo), traceroute (time exceeded), unreachable. No ports; IP protocol 1.**
- **GRE (proto 47) = tunnels anything incl. multicast, NO encryption → run GRE over IPsec.**
- **IPsec: IKE = keys, UDP 500 / 4500 NAT-T · AH (51) = integrity only, breaks through NAT · ESP (50) = encryption + integrity. Tunnel mode = gateway to gateway; transport = host to host.**
- **Unicast = one · multicast = subscribed group (224-239, IGMP) · anycast = nearest of many · broadcast = all on the segment. IPv6 has no broadcast.**

## Test 7 - 1.5 Cables + Connectors (30 Q)

1. IEEE 802.3 is the family of standards for:
   - [ ] Wi-Fi  - **[x] Wired Ethernet**  - [ ] Cable modems  - [ ] Bluetooth
   - *Answer: Wired Ethernet. IEEE (Institute of Electrical and Electronics Engineers) 802.3 = wired Ethernet: all the BASE-T, BASE-SX/LX standards, and PoE (802.3af/at/bt). 802.11 = Wi-Fi. 802.1Q = VLAN tagging, 802.1X = port authentication.*
   - @1.5.wired ~6.9
2. Ethernet names read speed-BASE-media. What do the T, S and L in 1000BASE-T, 10GBASE-SR and 10GBASE-LR mean?
   - **[x] Twisted pair · Short range, multimode · Long range, single-mode**  - [ ] Twinax · Single-mode · LED multimode  - [ ] Thin coax · Shielded pair · Laser copper  - [ ] Twisted pair · Single-mode · Long-haul coax
   - *Speed (1000 = 1 Gb/s, 10G = 10 Gb/s), BASE = baseband signalling, then media: T = Twisted pair, S = Short (multimode fibre), L = Long (single-mode fibre), C = Copper twinax (CX/CR). Second letter: X = the 1-Gig era (SX/LX/CX), R = the 10-Gig era (SR/LR/CR). Hook: X = eX (old), R = Recent.*
   - @1.5.wired ~6.10,6.12
3. Which standard is 10 Gb/s over twinax, as used by DAC cables in a rack?
   - [ ] 10GBASE-LR  - [ ] 10GBASE-T  - [ ] 10GBASE-SR  - **[x] 10GBASE-CR**
   - *Answer: 10GBASE-CR. C = Copper twinax (DAC, Direct Attach Copper), R = 10-Gig era. SR = short-range multimode fibre, LR = long-range single-mode, T = twisted pair.*
   - @1.5.wired ~6.14
4. Two buildings are 8 km apart and need a 10 Gb/s link. Which transceiver and fibre fit?
   - **[x] 10GBASE-LR on single-mode fibre**  - [ ] 10GBASE-SR on multimode fibre  - [ ] 10GBASE-T on Cat 6a  - [ ] A 10G DAC cable
   - *8 km = single-mode, and LR (Long Reach) reaches 10 km on SMF. SR = multimode, about 300-400 m on OM3/OM4. 10GBASE-T = 100 m of copper. DAC = a few metres inside a rack. Hook: S = Short, L = Long.*
   - @1.5.xcvr ~6.11,6.13
5. A new desk is 130 m of cable from the closet switch, and the PC gets constant errors on Cat 6. What is the problem?
   - **[x] The run is over the 100 m copper limit**  - [ ] Cat 6 can't do 1 Gb/s  - [ ] The switch port needs PoE  - [ ] The cable is shielded
   - *100 m total for copper Ethernet: typically 90 m of permanent horizontal cable plus up to 10 m of patch leads. Beyond that = attenuation errors, whatever the category. (Cat 6 at 10G only reaches 55 m.) Need further? Use fibre or put a switch in the middle.*
   - @1.5.wired ~6.22
6. Which is the MINIMUM twisted-pair category for 1 Gb/s at 100 m?
   - [ ] Cat 5  - **[x] Cat 5e**  - [ ] Cat 6a  - [ ] Cat 3
   - *Cat 5e (enhanced) = 1 Gb/s at 100 m. Cat 5 = 100 Mb/s. Cat 6 = 1 Gb/s at 100 m, or 10 Gb/s up to ~55 m. Cat 6a = 10 Gb/s at the full 100 m.*
   - @1.5.wired ~6.24,6.23
7. A 10 Gb/s copper link must run a full 90 m. Minimum cable category?
   - [ ] Cat 5e  - [ ] Cat 6  - **[x] Cat 6a**  - [ ] Cat 7 only
   - *Cat 6 only does 10GBASE-T to about 55 m (37-55 m depending on crosstalk). Cat 6a (augmented) = 10 Gb/s at 100 m. Hook: the "a" buys you the last 45 metres.*
   - @1.5.wired ~6.25,7.1
8. A data centre architect is evaluating Cat 8 twisted-pair cabling. Which statements are accurate? (Select 3)
   - **[x] 25 or 40 Gb/s**  - **[x] Only about 30 m**  - **[x] Data centre switch-to-server links**  - [ ] 40 Gb/s over the full 100 m  - [ ] Recommended for long runs to office desks
   - *Cat 8 is shielded copper supporting 25 or 40 Gb/s, but only for runs up to about 30 m, so it suits top-of-rack switch to server links. Office horizontal cabling to desks normally uses Cat 6 or Cat 6a at up to 100 m.*
   - @1.5.wired ~7.3
9. Match the copper category to its top speed at 100 m: Cat 5e, Cat 6a, Cat 7. Which list is right?
   - **[x] 1 Gb/s · 10 Gb/s · 10 Gb/s**  - [ ] 100 Mb/s · 1 Gb/s · 40 Gb/s  - [ ] 1 Gb/s · 1 Gb/s · 25 Gb/s  - [ ] 10 Gb/s · 40 Gb/s · 100 Gb/s
   - *Cat 5 100 Mb/s · Cat 5e 1 Gb/s · Cat 6 1 Gb/s (10G to 55 m) · Cat 6a 10 Gb/s · Cat 7 10 Gb/s shielded · Cat 8 25/40 Gb/s but only 30 m.*
   - @1.5.wired ~7.2
10. A campus link must run 20 km between sites. Which traits of the fibre you need make that possible? (Select 3)
    - **[x] Laser light source**  - **[x] Thin ~9 µm core, one light path**  - **[x] Kilometres to 100 km or more**  - [ ] LED light source  - [ ] Cheapest optics and cable
    - *Single-mode (SMF) = a tiny core that carries one mode (path) of laser light, so there's no modal dispersion and it goes far. It costs more. The jacket is usually YELLOW. Hook: Single = one straight laser beam, travels far.*
    - @1.5.wired ~6.17,7.7
11. A data centre wants cheap fibre for 150 m runs between rows. Which traits of the fibre it should use apply? (Select 3)
    - **[x] LED or VCSEL light source**  - **[x] Fat 50 or 62.5 µm core, many light paths**  - **[x] Hundreds of metres, up to about 2 km at low speed**  - [ ] Up to 100 km  - [ ] Always yellow jacket
    - *Multimode (MMF) = bigger core, light bounces along many paths (modes), which smear the signal over distance. Cheaper optics, used inside buildings and data centres. Jacket usually ORANGE (OM1/OM2) or AQUA (OM3/OM4). VCSEL = Vertical-Cavity Surface-Emitting Laser.*
    - @1.5.wired ~6.18,7.6
12. Which are MULTIMODE (short-range) standards? (Select 2)
    - **[x] 1000BASE-SX**  - **[x] 10GBASE-SR**  - [ ] 1000BASE-LX  - [ ] 10GBASE-LR
    - *S = Short = multimode. L = Long = single-mode. 1000BASE-SX reaches ~220-550 m depending on fibre grade; 1000BASE-LX up to 5-10 km on single-mode.*
    - @1.5.wired ~6.15,6.16,26.17
13. Why does a normal fibre link use a PAIR of strands?
    - [ ] One is a spare  - **[x] One transmits, one receives**  - [ ] One carries power  - [ ] To double the distance
    - *Standard duplex fibre = TX on one strand, RX on the other. Plugging them in swapped = TX/RX transposed = no link; flip the pair. BiDi (bidirectional) optics use two wavelengths on ONE strand instead.*
    - @1.5.wired ~26.16
14. Which fibre technology puts 80 or more channels on one strand, each on its own closely spaced wavelength, for long-haul links?
    - [ ] CWDM  - **[x] DWDM**  - [ ] Multimode  - [ ] BiDi SFP
    - *Answer: DWDM. WDM (Wavelength Division Multiplexing) = different colours of light on one fibre. DWDM (Dense) = many tightly spaced channels, long haul, expensive. CWDM (Coarse) = up to 18 channels, wider spacing, cheaper, shorter. Hook: DENSE = packed in tight.*
    - @1.5.wired ~26.13
15. Servers connect to a top-of-rack switch 2 m away at 25 Gb/s, as cheaply as possible. Which traits of the cable you should use apply? (Select 3)
    - **[x] Copper with two inner conductors**  - **[x] Short runs in a rack, a few metres**  - **[x] Fixed SFP+ or QSFP ends, cheap, low latency**  - [ ] Runs of several kilometres  - [ ] Uses laser light
    - *DAC (Direct Attach Copper) = twinax with the transceivers built into the ends. 10G to ~7-10 m, 40G to ~7 m, 100G to ~5 m: faster = shorter. Cheaper and lower-latency than fibre optics for top-of-rack links. AOC (Active Optical Cable) = the fibre version.*
    - @1.5.wired ~6.19,6.20,7.5
16. A cable modem connects to the ISP with an F-type screw connector. Which cable?
    - [ ] Twinax  - **[x] RG-6 coax**  - [ ] RG-59 coax  - [ ] Cat 6
    - *Answer: RG-6 coax. Coax = copper core, insulator, braided shield, outer jacket. RG-6 = thicker, lower loss, the standard for cable broadband (DOCSIS, Data Over Cable Service Interface Specification), satellite and TV. RG-59 = thinner, older, short runs, CCTV (Closed-Circuit TV). RG = Radio Guide.*
    - @1.5.wired ~7.4,26.12,6.21
17. What is a PLENUM space, and which cable must go there?
    - **[x] An air-handling space, like above a drop ceiling; plenum-rated cable**  - [ ] A vertical shaft between floors; riser-rated cable  - [ ] A server rack; shielded cable  - [ ] Outdoors; direct-burial cable
    - *Plenum = space that's part of the air circulation (above ceilings, under raised floors). In a fire, the HVAC (Heating, Ventilation, Air Conditioning) spreads smoke everywhere, so plenum-rated cable has a fire-retardant, low-smoke jacket (FEP, Fluorinated Ethylene Propylene, or special low-smoke PVC). Riser = vertical runs between floors.*
    - @1.5.wired ~7.8
18. An inspector says the cable above the ceiling tiles is the wrong type: it's standard jacket, non-plenum. Main risk?
    - **[x] In a fire it gives off toxic smoke that the air system spreads**  - [ ] It will cause crosstalk with the power cables  - [ ] It can't carry PoE  - [ ] It limits the run to 55 m
    - *Standard (non-plenum) PVC (Polyvinyl Chloride) jacket burns with thick toxic smoke. Fire code requires plenum-rated cable in air-handling spaces. It's a safety and code issue, not a performance one; the cable works fine until the fire.*
    - @1.5.wired ~26.18
19. A Layer 1 device connects a copper Ethernet port to a fibre run. What is it?
    - **[x] Media converter**  - [ ] Bridge  - [ ] Managed switch  - [ ] Router
    - *A transceiver (TRANSmitter + reCEIVER) or media converter works at L1, changing the signal between media, e.g. copper to fibre. No MAC or IP decisions, so not L2/L3.*
    - @1.5.xcvr ~7.9
20. A switch has empty SFP+ and QSFP28 cages. Which statements about filling them are correct? (Select 3)
    - **[x] Hot-swappable transceivers that plug into a switch port**  - **[x] QSFP bundles four lanes for 40 or 100 Gb/s**  - **[x] The module must match the fibre type and the far end**  - [ ] They are soldered permanently into the switch  - [ ] They only work with copper
    - *SFP (Small Form-factor Pluggable) = ~1 Gb/s, SFP+ = 10 Gb/s, SFP28 = 25 Gb/s. QSFP (Quad SFP) = 4 lanes: QSFP+ 40 Gb/s, QSFP28 100 Gb/s. Mismatched modules (SR one end, LR the other; wrong wavelength) = no link.*
    - @1.5.xcvr ~7.11
21. Which storage protocol needs its own transceivers and switches instead of running over Ethernet?
    - [ ] iSCSI  - **[x] Fibre Channel**  - [ ] SMB  - [ ] NFS
    - *Answer: Fibre Channel. SAN = the network, FC = the protocol it runs on. The objectives list transceiver protocols as Ethernet and Fibre Channel (FC). FC = the classic dedicated SAN (Storage Area Network) fabric, with its own FC switches and HBAs (Host Bus Adapters). iSCSI, SMB and NFS all run over ordinary Ethernet.*
    - @1.5.xcvr ~7.10
22. A tech is ordering patch leads for a fibre panel. Which connector types could the panel use? (Select 4)
    - **[x] LC**  - **[x] SC**  - **[x] ST**  - **[x] MPO**  - [ ] RJ45  - [ ] F-type  - [ ] BNC
    - *Fibre: LC (Lucent Connector, small, push-latch, most common on SFPs), SC (Subscriber Connector, square, push-pull), ST (Straight Tip, round bayonet twist), MPO (Multi-fibre Push-On, 12/24+ fibres in one ferrule). Copper: RJ45/RJ11 (twisted pair), F-type/BNC (coax). Hooks: LC = Little Connector; SC = Square; ST = Stick and Twist. See SC/LC/ST/MPO on a new run = fibre = likely a long run, e.g. from another building on campus.*
    - @1.5.conn ~7.12
23. Which connector carries 12 or 24 fibres in one ferrule for 40/100G data centre links?
    - [ ] LC  - [ ] ST  - **[x] MPO**  - [ ] SC
    - *MPO (Multi-fibre Push-On), a.k.a. MTP, is a ribbon connector for parallel optics like 40GBASE-SR4 and 100GBASE-SR4.*
    - @1.5.conn ~7.17
24. Which describe RJ11 vs RJ45? (Select 2)
    - **[x] RJ11 = 6-position, used for analogue phone lines and DSL**  - **[x] RJ45 = 8-position 8-contact, used for Ethernet**  - [ ] RJ11 is the fibre version of RJ45  - [ ] RJ45 is used for coax
    - *RJ (Registered Jack) 11 = smaller, 2-4 wires, phone and DSL (Digital Subscriber Line). RJ45 (really 8P8C, 8 Positions 8 Contacts) = twisted-pair Ethernet with 8 wires.*
    - @1.5.conn ~7.13,7.14
25. Which describe F-type vs BNC? (Select 2)
    - **[x] F-type = screw-on coax, cable modems and TV**  - **[x] BNC = bayonet twist-lock coax, legacy Ethernet and CCTV/test gear**  - [ ] F-type is a fibre connector  - [ ] BNC is for twisted pair
    - *F-type = threaded coax connector on RG-6. BNC (Bayonet Neill-Concelman) = push-and-twist coax connector, seen on old 10BASE2 networks, CCTV and test equipment.*
    - @1.5.conn ~7.15,7.16
26. Campus cabling: ¶  Bldg 1 MDF ════(1)════ Bldg 2 IDF       2 km apart ¶  IDF switch ────(2)──── desk PCs          up to 80 m ¶  Switch ────────(3)──── switch, same rack 3 m, 10 Gb/s ¶  Switch ────────(4)──── ceiling AP        needs power over the cable ¶Match the media to slots 1 to 4. Type the letters in slot order, e.g. abcd. A letter can be used twice. ¶  A Cat 6 · B twinax DAC · C single-mode fibre · D multimode fibre · E RG-6 coax
    - [=] caba | c a b a | c,a,b,a
    - *1 = single-mode fibre: 2 km is past multimode's reach, and fibre has no ground-potential or EMI (Electromagnetic Interference) issues between buildings. 2 = Cat 6 (Cat 5e/6/6a all fine under 100 m). 3 = twinax DAC for short in-rack 10G. 4 = Cat 6 again, carrying PoE (Power over Ethernet), since fibre and DAC carry no power.*
    - @1.5.wired ~31.9,31.10,31.11,31.12
27. Match single-mode or multimode to each. Type the letters in order, e.g. abab. ¶  Items: a 40 km link between towns · a 150 m run between floors · a 10GBASE-SR optic · a 1000BASE-LX optic ¶  A single-mode · B multimode
    - [=] abba | a b b a | a,b,b,a
    - *Long distance and anything L (LX, LR) = single-mode. Short and anything S (SX, SR) = multimode.*
    - @1.5.wired
28. A new SFP+ link won't come up. Side A has a 10GBASE-SR optic, side B has a 10GBASE-LR optic, joined by multimode fibre. Which optic is wrong?
    - **[x] Side B's 10GBASE-LR**  - [ ] Side A's 10GBASE-SR  - [ ] Both; they must be 10GBASE-T  - [ ] Neither; the fibre must be single-mode
    - *SR = multimode, LR = single-mode. The optics must match each other AND the fibre. Swap side B's LR for an SR. This is the 5.2 "transceiver mismatch" fault.*
    - @1.5.xcvr
29. Match each to its connector. Type the letters in order, e.g. abcde. ¶  Items: a cable modem's coax · a desk Ethernet jack · a small push-latch fibre connector on an SFP · a 12-fibre ribbon connector · an old phone line ¶  A RJ11 · B MPO · C F-type · D LC · E RJ45 · F ST
    - [=] cedba | c e d b a | c,e,d,b,a
    - *Cable modem = F-type · Ethernet = RJ45 · SFP fibre = LC · ribbon = MPO · phone/DSL = RJ11.*
    - @1.5.conn
30. Match the MINIMUM copper category to each. Type the letters in order, e.g. abc. ¶  Needs: 10 Gb/s at 100 m · 40 Gb/s at 25 m in the data centre · 1 Gb/s at 100 m ¶  A Cat 5 · B Cat 5e · C Cat 6 · D Cat 6a · E Cat 8
    - [=] deb | d e b | d,e,b
    - *10G at 100 m = Cat 6a (plain Cat 6 only reaches ~55 m at 10G). 40G = Cat 8, up to 30 m. 1G at 100 m = Cat 5e; Cat 5 is only 100 Mb/s.*
    - @1.5.wired

### Key facts
- **speed-BASE-media: T twisted pair · S short multimode · L long single-mode · C copper twinax. X = 1-Gig era, R = 10-Gig era.**
- **Copper max 100 m. Cat 5e 1G · Cat 6 1G (10G to 55 m) · Cat 6a 10G/100 m · Cat 7 10G shielded · Cat 8 25/40G to 30 m.**
- **Single-mode = laser, thin core, km, yellow, costly · multimode = LED/VCSEL, fat core, ~550 m (SX), orange/aqua, cheaper.**
- **Duplex fibre = TX + RX strands; swapped = no link. DWDM = many wavelengths on one fibre, long haul · CWDM = fewer, cheaper.**
- **Twinax/DAC = short in-rack copper (10G ~7 m). Coax RG-6 = cable modem (F-type) · RG-59 = CCTV**
- **Plenum = air-handling space → plenum-rated, low-smoke jacket. Riser = between floors. Non-plenum PVC = toxic smoke.**
- **SFP 1G · SFP+ 10G · SFP28 25G · QSFP+ 40G · QSFP28 100G. Optics must match each other and the fibre. Protocols: Ethernet, Fibre Channel.**
- **Fibre connectors: LC little latch · SC square · ST stick-and-twist · MPO ribbon. Copper: RJ45 Ethernet · RJ11 phone · F-type and BNC coax.**

## Test 8 - 1.7 IPv4 Addressing (25 Q)

1. Type the three RFC 1918 private ranges, smallest prefix number first. ¶Answer format: network address plus prefix, separated by spaces, like 1.0.0.0/8 2.0.0.0/8 3.0.0.0/8
   - [=] 10.0.0.0/8 172.16.0.0/12 192.168.0.0/16
   - *RFC (Request for Comments) 1918 private ranges: 10.0.0.0/8 (10.0.0.0-10.255.255.255), 172.16.0.0/12 (172.16.0.0-172.31.255.255), 192.168.0.0/16. They aren't routed on the internet, so they need NAT (Network Address Translation) to get out. Hook: 10, 172.16-31, 192.168.*
   - @1.7.priv ~8.6
2. Which address is PRIVATE?
   - [ ] 172.32.1.5  - **[x] 172.20.14.9**  - [ ] 192.169.1.1  - [ ] 11.0.0.1
   - *172.16-172.31 is private, so 172.20 is inside it. 172.32 is just past the end (public). 192.169 isn't 192.168. 11.x isn't 10.x. The /12 on 172.16 covers the second octet 16 through 31.*
   - @1.7.priv ~8.13
3. Which describe 10.0.0.0/8? (Select 2)
   - **[x] Class A range**  - **[x] Private, not routed on the internet**  - [ ] Class B range  - [ ] Public range
   - *10.0.0.0/8 = the one Class A private block, about 16.7 million addresses. 172.16.0.0/12 = Class B private, 192.168.0.0/16 = Class C private.*
   - @1.7.priv ~8.12,8.14
4. A PC shows 169.254.33.7 with no gateway. What does that tell you?
   - **[x] It got no DHCP reply and gave itself an APIPA address**  - [ ] It has a public address from the ISP's DHCP  - [ ] It was set statically by an admin  - [ ] It's using the loopback range for testing
   - *APIPA (Automatic Private IP Addressing) = 169.254.0.0/16, self-assigned when DHCP (Dynamic Host Configuration Protocol) fails. It only reaches other APIPA hosts on the same link: no gateway, no internet. IPv6's equivalent = link-local fe80::/10.*
   - @1.7.priv ~8.5
5. Type the IPv4 loopback address.
   - [=] 127.0.0.1
   - *Loopback = 127.0.0.0/8, usually 127.0.0.1, also called localhost. Traffic never leaves the machine: pinging it tests the local TCP/IP stack. IPv6 loopback = ::1.*
   - @1.7.priv ~8.7,8.8
6. Pinging which of these tests the local TCP/IP stack without using the network? (Select 2)
   - **[x] 127.0.0.1**  - **[x] localhost**  - [ ] 169.254.0.1  - [ ] 255.255.255.255
   - *127.0.0.1 and localhost both hit the loopback interface. It proves the IP stack works; it doesn't prove the NIC (Network Interface Card) or cable is fine. 255.255.255.255 = limited broadcast.*
   - @1.7.priv ~8.9
7. A server needs to be reachable from anywhere on the internet. What kind of address must it (or its NAT) have?
   - **[x] A public, globally routable address**  - [ ] An RFC 1918 private address  - [ ] An APIPA link-local address  - [ ] A 127.x loopback address
   - *Public addresses are unique worldwide and routed on the internet, assigned by RIRs (Regional Internet Registries) to ISPs (Internet Service Providers). Private (RFC 1918), APIPA (169.254) and loopback (127) addresses are never routed on the internet.*
   - @1.7.priv
8. Which range is reserved for ISP carrier-grade NAT, and is NOT RFC 1918?
   - [ ] 172.16.0.0/12  - **[x] 100.64.0.0/10**  - [ ] 192.0.2.0/24  - [ ] 169.254.0.0/16
   - *100.64.0.0/10 = CGNAT (Carrier-Grade NAT) shared address space, used between the ISP and your router. If your router's WAN IP is 100.64-100.127, you're behind CGNAT and port forwarding won't work from outside. 192.0.2.0/24 = documentation examples.*
   - @1.7.priv
9. First-octet range for Class A?
   - **[x] 1-126**  - [ ] 0-127  - [ ] 1-191  - [ ] 128-191
   - *Class A = first octet 1-126, default mask /8 (255.0.0.0). The first bit is 0, which technically gives 0-127, but 0 is reserved and 127 is loopback, so the exam answer is 1-126. (Standard: RFC 791 classful A = 0-127; RFC 6890 reserves 0/8 and 127/8. Some sources, e.g. Messer, say 1-127: on the exam, 126 is A and 127 = loopback.)*
   - @1.7.class ~8.17,8.18
10. First-octet range for Class B?
    - [ ] 127-191  - **[x] 128-191**  - [ ] 128-223  - [ ] 192-223
    - *Class B = 128-191, default /16 (255.255.0.0). First bits 10.*
    - @1.7.class ~8.19,8.20
11. First-octet range for Class C?
    - [ ] 191-223  - [ ] 192-255  - **[x] 192-223**  - [ ] 224-239
    - *Class C = 192-223, default /24 (255.255.255.0). First bits 110.*
    - @1.7.class ~8.21,8.22
12. Which describe Class D? (Select 2)
    - **[x] 224-239**  - **[x] Multicast**  - [ ] Default mask /24  - [ ] Private LAN addresses
    - *Class D = 224.0.0.0-239.255.255.255, multicast (first bits 1110). No default mask, since they're group addresses, not networks. E.g. 224.0.0.5 = OSPF routers.*
    - @1.7.class ~8.15
13. Which range is Class E?
    - [ ] 224-239  - **[x] 240-255**  - [ ] 128-191  - [ ] 1-126
    - *Class E = 240-255 (240.0.0.0/4, RFC 1112/6890), reserved/experimental (255.255.255.255 = limited broadcast). Some sources say 240-254 to carve out the broadcast; same answer. Hook for all five, on the first octet: A up to 126, B up to 191, C up to 223, D up to 239 (multicast), E the rest.*
    - @1.7.class ~8.16
14. Type the DEFAULT subnet mask for 150.10.4.2, in dotted decimal.
    - [=] 255.255.0.0
    - *150 is in 128-191, so it's Class B, default /16 = 255.255.0.0. A = 255.0.0.0 (/8), C = 255.255.255.0 (/24). Classful masks are the starting point; CIDR (Classless Inter-Domain Routing) lets you use any prefix.*
    - @1.7.class
15. What replaced classful addressing, letting any prefix length be used, like 200.10.4.0/22?
    - [ ] VLSM  - [ ] RSTP  - **[x] CIDR**  - [ ] MPLS
    - *CIDR (Classless Inter-Domain Routing) = /n prefixes instead of fixed A/B/C sizes, which also allows route summarisation (supernetting). VLSM (Variable Length Subnet Mask) = using DIFFERENT prefix lengths inside one network.*
    - @1.7.sub ~8.11
16. An admin carves one /24 into a /26 for 50 users, a /27 for 25 users and several /30 point-to-point links. Technique?
    - **[x] VLSM**  - [ ] CIDR summarisation  - [ ] Classful subnetting  - [ ] NAT
    - *VLSM (Variable Length Subnet Mask) = subnets of DIFFERENT sizes from one block, sized to fit, so fewer addresses are wasted. Allocate the largest subnet first.*
    - @1.7.sub ~8.10
17. Which are NOT valid host addresses you could assign to a PC? (Select 2)
    - **[x] 192.168.1.0/24**  - **[x] 192.168.1.255/24**  - [ ] 192.168.1.1/24  - [ ] 192.168.1.254/24
    - *In 192.168.1.0/24, .0 = the network address (all host bits 0) and .255 = the broadcast (all host bits 1). Usable hosts = .1 to .254.*
    - @1.7.sub
18. Type the usable host count for a /24.
    - [=] 254
    - */24 = 8 host bits: 2 to the power of 8 = 256 addresses, minus network and broadcast = 254.*
    - @1.7.sub
19. Match private or public to each address. Type the letters in order, e.g. abaab. ¶  Addresses: 10.200.1.1 · 172.33.0.1 · 192.168.44.9 · 8.8.8.8 · 172.31.255.254 ¶  A private · B public
    - [=] ababa | a b a b a | a,b,a,b,a
    - *10.x = private. 172.33 is past 172.31, so public. 192.168.x = private. 8.8.8.8 = Google DNS, public. 172.31.255.254 = the last usable address of the 172.16/12 private block.*
    - @1.7.priv
20. Type the class letter for each first octet, in order, e.g. abcde. ¶  First octets: 200 · 10 · 250 · 130 · 230
    - [=] caebd | c a e b d | c,a,e,b,d
    - *200 = C (192-223). 10 = A (1-126). 250 = E reserved (240-255). 130 = B (128-191). 230 = D multicast (224-239).*
    - @1.7.class
21. ipconfig on three PCs shows: ¶  C:\> ipconfig  (run on each PC) ¶  PC1  172.16.5.20     gateway 172.16.5.1 ¶  PC2  169.254.10.4    gateway (blank) ¶  PC3  192.168.1.40    gateway 192.168.1.1 ¶Which PC failed to get a DHCP lease?
    - [ ] PC1  - **[x] PC2**  - [ ] PC3  - [ ] None of them
    - *PC2 = APIPA 169.254.x.x with no gateway: DHCP failed, so it gave itself an address. PC1 (172.16/12) and PC3 (192.168/16) have normal private addresses and gateways.*
    - @1.7.priv
22. Give the default classful prefix for each address, in order. ¶  Addresses: 172.16.5.5 · 199.9.9.9 · 45.1.2.3 ¶Answer format: slash prefixes separated by spaces, like /30 /30 /30
    - [=] /16 /24 /8 | 16 24 8
    - *172 = Class B /16. 199 = Class C /24. 45 = Class A /8.*
    - @1.7.class
23. A router's WAN port shows 100.72.14.9 and inbound port forwarding from the internet doesn't work. What is the ISP doing?
    - **[x] CGNAT, carrier-grade NAT**  - [ ] APIPA  - [ ] Port address translation on your router  - [ ] Assigning a link-local address
    - *100.64.0.0/10 = CGNAT (Carrier-Grade NAT) shared space. The router's "public" address is really private to the ISP, which NATs again. Fix: ask the ISP for a real public IP, or use IPv6 or a tunnel.*
    - @1.7.priv
24. PBQ: A host is configured as 172.20.37.200/21. Answer each part.
    - [p] Network address = 172.20.32.0
    - [p] Broadcast address = 172.20.39.255
    - [p] First usable host = 172.20.32.1
    - [p] Last usable host = 172.20.39.254
    - [p] Number of usable hosts = 2046
    - */21 = 255.255.248.0, so the 3rd octet moves in blocks of 8: 32, 40... 37 sits in 32-39. Network 172.20.32.0, broadcast 172.20.39.255, hosts .32.1 to .39.254. Host bits = 32 - 21 = 11, and 2^11 - 2 = 2046.*
    - @1.7.sub
25. PBQ: PAT on the edge router. 40 PCs share one public IP. ¶  R1# show ip nat translations ¶  Pro  Inside global       Inside local        Outside local       Outside global ¶  tcp  203.0.113.5:62001  192.168.1.20:50123  198.51.100.80:443   198.51.100.80:443 ¶  tcp  203.0.113.5:62002  192.168.1.31:50999  142.250.1.1:443     142.250.1.1:443 ¶  tcp  203.0.113.5:62003  192.168.1.20:50124  198.51.100.80:443   198.51.100.80:443
    - [p] Type the IP of the inside PC with two open sessions = 192.168.1.20
    - [p] A reply arrives at 203.0.113.5:62002. Type the inside ip:port it is forwarded to = 192.168.1.31:50999 | 192.168.1.31 50999
    - [p] Type the source ip:port that 142.250.1.1 sees = 203.0.113.5:62002 | 203.0.113.5 62002
    - [p] Type the IOS keyword on ip nat inside source that makes this PAT = overload
    - [p] All 40 PCs share 203.0.113.5. How does the router tell the replies apart :: A by the translated (inside global) port number · B by MAC address · C by TTL · D by TCP sequence number = a
    - *Read each row left to right: Inside global is what the internet sees, Inside local is the PC's real private address. .20 has two rows, one per browser connection. A reply to :62002 is looked up in the table and sent to 192.168.1.31:50999. Outside local and global match because only the inside is translated. One public IP, many hosts, told apart by port = PAT, aka NAT overload: ip nat inside source list 1 interface Gi0/0 overload.*
    - @2.1.nat

### Key facts
- **RFC 1918 private: 10.0.0.0/8 · 172.16.0.0/12 (172.16-172.31) · 192.168.0.0/16. Need NAT for the internet.**
- **APIPA 169.254.0.0/16 = no DHCP. Loopback 127.0.0.0/8 (127.0.0.1, localhost) · IPv6 ::1. CGNAT = 100.64.0.0/10.**
- **Classes by first octet: A 1-126 /8 · B 128-191 /16 · C 192-223 /24 · D 224-239 multicast · E 240-255 reserved.**
- **CIDR = any prefix, replaced classes · VLSM = different-size subnets in one block, biggest first.**
- **Network address (host bits 0) and broadcast (host bits 1) can't be given to hosts.**

## Test 9 - 1.7 Subnetting + VLSM (31 Q)

1. Type the mask octet for /26.
   - [=] 192
   - *Mask octet = the running total of the bit row 128 64 32 16 8 4 2 1. /24 is three full octets, then 2 more bits = 128 + 64 = 192. Table row: /25 128 · /26 192 · /27 224 · /28 240 · /29 248 · /30 252.*
   - @1.7.sub
2. Type the CIDR prefix for 255.255.255.224, like /30.
   - [=] /27 | 27
   - *224 = 3 bits on (128+64+32). 24 + 3 = /27. Count the 1s: every 255 = 8.*
   - @1.7.sub ~8.23
3. Type the full mask for /22.
   - [=] 255.255.252.0
   - *22 = 8 + 8 + 6. Two 255s, then 6 bits in the third octet = 252, then 0. Third-octet row: /17 128 · /18 192 · /19 224 · /20 240 · /21 248 · /22 252 · /23 254.*
   - @1.7.sub
4. Type the BLOCK SIZE (increment) for a /28.
   - [=] 16
   - *Block = 256 minus the mask octet = 256 - 240 = 16. It's also the value of the last network bit. Subnets go .0, .16, .32, .48 ... Table row of blocks: /25 128 · /26 64 · /27 32 · /28 16 · /29 8 · /30 4.*
   - @1.7.sub
5. Type the usable hosts for a /27.
   - [=] 30
   - *Host bits = 32 - 27 = 5, so 2 to the 5 = 32 addresses, minus network and broadcast = 30. Shortcut: usable = block - 2.*
   - @1.7.sub
6. Type the usable hosts for a /30.
   - [=] 2
   - *Block 4, minus 2 = 2 usable: perfect for a router-to-router point-to-point link. (/31 is also allowed for point-to-point, with 2 usable and no network/broadcast, but the exam's answer is /30.)*
   - @1.7.sub
7. Type the usable hosts for a /23.
   - [=] 510
   - */23 = 9 host bits = 512 - 2 = 510. Third-octet row doubles from 254 at /24: /23 510 · /22 1022 · /21 2046 · /20 4094 · /19 8190 · /18 16382 · /17 32766.*
   - @1.7.sub
8. A subnet needs 50 hosts. Type the smallest prefix that fits, like /30.
   - [=] /26 | 26
   - */26 = 62 usable, which fits 50. /27 = 30, too small. Method: find the smallest block where block - 2 is at least the host count: 64 - 2 = 62.*
   - @1.7.sub
9. A subnet needs 500 hosts. Type the smallest prefix that fits, like /30.
   - [=] /23 | 23
   - */23 = 510 usable. /24 = 254, too small. Past 254 you're into the third octet: 510, 1022, 2046 ...*
   - @1.7.sub
10. A host is 192.168.1.100/26. Type the NETWORK address.
    - [=] 192.168.1.64
    - */26 block = 64: networks .0, .64, .128, .192. The biggest multiple of 64 not above 100 = 64. Network = 192.168.1.64.*
    - @1.7.sub
11. Same host, 192.168.1.100/26. Type the BROADCAST address.
    - [=] 192.168.1.127
    - *Next network = 64 + 64 = 128, minus 1 = 127. Broadcast = 192.168.1.127. Usable = .65 to .126.*
    - @1.7.sub
12. A host is 10.10.10.130/27. Type the FIRST usable host.
    - [=] 10.10.10.129
    - *Block 32: .0 .32 .64 .96 .128 .160. 130 sits in .128, so network .128, first host .129.*
    - @1.7.sub
13. Same host, 10.10.10.130/27. Type the LAST usable host.
    - [=] 10.10.10.158
    - *Broadcast = next network 160 - 1 = 159. Last usable = broadcast - 1 = 158. The -1 trap: the broadcast itself is NOT usable.*
    - @1.7.sub
14. A host is 172.16.8.33/29. Type the network address.
    - [=] 172.16.8.32
    - */29 block = 8: .32 .40. 33 sits in .32. Broadcast .39, usable .33-.38.*
    - @1.7.sub
15. A host is 154.24.67.147/22. Type the network address.
    - [=] 154.24.64.0
    - */22 = 252 in the THIRD octet, block 4: 60, 64, 68. 67 sits in 64. The fourth octet becomes 0 for the network. Broadcast = 154.24.67.255.*
    - @1.7.sub ~8.25
16. A host is 192.168.50.155/20. Type the BROADCAST address.
    - [=] 192.168.63.255
    - */20 = 240 in the third octet, block 16: 32, 48, 64. 50 sits in 48. Next network 64, minus 1 = 63, and the fourth octet becomes 255. Broadcast = 192.168.63.255.*
    - @1.7.sub ~9.1
17. A host is 10.119.136.143/20. Type the FIRST usable host.
    - [=] 10.119.128.1
    - *Block 16 in the third octet: 128, 144. 136 sits in 128. Network 10.119.128.0, first host 10.119.128.1, broadcast 10.119.143.255.*
    - @1.7.sub ~8.24
18. Two PCs: 192.168.30.40/27 and 192.168.30.70/27. Are they on the same subnet?
    - [ ] Yes, same /24  - **[x] No: .40 is in .32-.63, .70 is in .64-.95**  - [ ] Yes, /27 covers .0-.127  - [ ] Can't tell without the gateway
    - *Answer: No: .40 is in .32-.63, .70 is in .64-.95. Block 32: .32-.63 and .64-.95 are different subnets, so they need a router to talk. Always find each host's block, not just the /24.*
    - @1.7.sub
19. Type the WILDCARD mask for /27, as used in ACLs and OSPF.
    - [=] 0.0.0.31
    - *Answer: 0.0.0.31. A wildcard mask is the subnet mask flipped. Step 1: /27 = mask 255.255.255.224. Step 2: take each octet away from 255: 255-255=0, 255-255=0, 255-255=0, 255-224=31, giving 0.0.0.31. Quicker: /27 has 32 addresses per subnet, and the wildcard is that minus 1 = 31. Why: in a wildcard, 0 means 'this bit must match' and 1 means 'don't care', so 0.0.0.31 says 'the first 27 bits must match, the last 5 can be anything', which is the whole /27. Same trick: /24 → 0.0.0.255, /30 → 0.0.0.3.*
    - @1.7.sub
20. How many /26 subnets fit in one /24?
    - [ ] 2  - **[x] 4**  - [ ] 6  - [ ] 8
    - *Answer: 4. Borrowing 2 bits = 2 squared = 4 subnets (.0, .64, .128, .192), each with 62 hosts. /25 = 2 subnets, /27 = 8, /28 = 16.*
    - @1.7.sub
21. VLSM from 192.168.10.0/24 for three subnets needing 25, 100 and 10 hosts. Which plan works with no overlaps and the least waste?
    - **[x] .0/25 for 100 · .128/27 for 25 · .160/28 for 10**  - [ ] .0/26 for 100 · .64/27 for 25 · .96/28 for 10  - [ ] .0/25 for 100 · .128/28 for 25 · .144/28 for 10  - [ ] .0/28 for 10 · .16/27 for 25 · .128/25 for 100
    - *VLSM (Variable Length Subnet Mask): allocate biggest first, so every block starts on a multiple of its own size. 100 → /25 (126) = .0-.127. 25 → /27 (30) = .128-.159. 10 → /28 (14) = .160-.175. Traps: a /26 holds only 62, a /28 only 14, and .16 isn't a valid start for a /27 (block 32).*
    - @1.7.sub
22. Which subnet is the best fit for a point-to-point WAN link between two routers?
    - [ ] /24  - [ ] /28  - **[x] /30**  - [ ] /32
    - */30 = exactly 2 usable addresses, one per router, so nothing is wasted. /32 = a single host route (a loopback, or one host in an ACL).*
    - @1.7.sub
23. A /24 is summarised with its neighbour into one route, 10.1.0.0/23. What is this called?
    - **[x] Route summarisation**  - [ ] VLSM  - [ ] Subnetting  - [ ] NAT
    - *Summarisation = shorter prefix covering several networks: 10.1.0.0/24 + 10.1.1.0/24 = 10.1.0.0/23. Smaller routing tables. Also called supernetting. It's CIDR in reverse: fewer bits, bigger block.*
    - @1.7.sub
24. Fill in the grid for 192.168.1.200/29. Type the network, first usable, last usable and broadcast, in that order, separated by spaces.
    - [=] 192.168.1.200 192.168.1.201 192.168.1.206 192.168.1.207
    - *Block 8: ..192, 200, 208. 200 is itself a multiple of 8, so it IS the network. First .201. Next network 208 - 1 = broadcast .207. Last usable .206. 6 hosts.*
    - @1.7.sub
25. Fill in the grid for 172.20.100.3/21. Type the mask, network and broadcast, in that order, separated by spaces.
    - [=] 255.255.248.0 172.20.96.0 172.20.103.255
    - */21 = 248 in the third octet, block 8: 88, 96, 104. 100 sits in 96. Next 104 - 1 = 103, fourth octet 255. Hosts = 2046.*
    - @1.7.sub
26. Fill in the grid for 10.5.77.200/18. Type the network and broadcast, separated by a space.
    - [=] 10.5.64.0 10.5.127.255
    - */18 = 192 in the third octet, block 64: 0, 64, 128. 77 sits in 64. Next 128 - 1 = 127. Network 10.5.64.0, broadcast 10.5.127.255, 16382 hosts.*
    - @1.7.sub
27. ipconfig shows: ¶  C:\> ipconfig ¶  IPv4 Address . . : 192.168.20.14 ¶  Subnet Mask  . . : 255.255.255.240 ¶  Default Gateway  : 192.168.20.17 ¶The PC can't reach other subnets. Type the BROADCAST address of the PC's own subnet, which proves the gateway is outside it.
    - [=] 192.168.20.15
    - *255.255.255.240 = /28, block 16: the PC's subnet is .0-.15, broadcast .15. The gateway .17 sits in the NEXT subnet (.16-.31), so the PC can't reach it directly. The gateway must be inside .1-.14. This is the 5.3 "incorrect default gateway" fault.*
    - @1.7.sub
28. VLSM from 10.0.0.0/24. Needs: Sales 60 hosts, IT 28 hosts, WAN link 2 hosts. Allocate biggest first from .0. Type the three subnets in allocation order, separated by spaces, each like 10.9.9.0/24.
    - [=] 10.0.0.0/26 10.0.0.64/27 10.0.0.96/30
    - *Sales 60 → /26 (62) = .0-.63. IT 28 → /27 (30) = .64-.95. WAN 2 → /30 (2) = .96-.99. Each new block starts where the last one ended.*
    - @1.7.sub
29. Same plan. Type the BROADCAST address of the IT subnet, 10.0.0.64/27.
    - [=] 10.0.0.95
    - *64 + 32 = 96, minus 1 = 95. IT's usable hosts = .65-.94.*
    - @1.7.sub
30. A PC is 172.31.8.99 with mask 255.255.254.0. Type how many usable hosts share its subnet.
    - [=] 510
    - *255.255.254.0 = /23 = 9 host bits = 512 - 2 = 510. Its network = 172.31.8.0 (254 in the third octet, block 2: 8 is even), broadcast 172.31.9.255.*
    - @1.7.sub
31. PBQ: VLSM. You have 192.168.50.0/24 for a new branch. Allocate largest first, from the bottom of the range, with no gaps: ¶  Sales    100 hosts ¶  Eng       50 hosts ¶  Mgmt      20 hosts ¶  WAN1, WAN2  2 hosts each, /30 by design standard ¶Answer each part.
    - [p] Sales prefix, e.g. /24 = /25 | 25 | 255.255.255.128
    - [p] Eng network address = 192.168.50.128 | 192.168.50.128/26
    - [p] Mgmt broadcast address = 192.168.50.223
    - [p] WAN1 first usable host = 192.168.50.225
    - [p] WAN2 network address = 192.168.50.228 | 192.168.50.228/30
    - *Sales 100 needs 7 host bits = /25, 126 hosts: .0-.127. Eng 50 = /26, 62 hosts: .128-.191. Mgmt 20 = /27, 30 hosts: .192-.223, broadcast .223. WAN1 /30 = .224-.227, first host .225. WAN2 /30 = .228. Largest first stops the small subnets fragmenting the space.*
    - @1.7.sub

### Key facts
- **Bit row 128 64 32 16 8 4 2 1 · mask row (running total) 128 192 224 240 248 252 254 255.**
- **Block = 256 - mask octet (= the last network bit's value). Network = biggest block multiple ≤ the octet · broadcast = next multiple - 1 · rest of octets: 0 for network, 255 for broadcast.**
- **Usable = block - 2 in the 4th octet. From /24 the counts double: /24 254 · /23 510 · /22 1022 · /21 2046 · /20 4094 · /19 8190 · /18 16382 · /17 32766.**
- **N hosts → smallest block with block - 2 ≥ N. 50 → /26 · 100 → /25 · 500 → /23. /30 = 2 hosts = point-to-point.**
- **Wildcard = 255 - mask per octet (/27 = 0.0.0.31). VLSM = biggest subnet first. Summarising = shorter prefix over several networks.**

## Test 10 - 1.8 IPv6 (23 Q)

1. Why was IPv6 created?
   - **[x] IPv4 address exhaustion**  - [ ] IPv4 had no routing  - [ ] To replace Ethernet  - [ ] To add encryption to DNS
   - *IPv4 = 32 bits ≈ 4.3 billion addresses, long since used up (NAT and CGNAT were stopgaps). IPv6 = 128 bits ≈ 340 undecillion, enough for every device to have a global address. The objectives call it "mitigating address exhaustion".*
   - @1.8.ipv6 ~9.24
2. How many bits are in an IPv6 address, and how is it written?
   - **[x] 128 bits, 8 groups of 4 hex digits separated by colons**  - [ ] 64 bits, 4 groups of decimal separated by dots  - [ ] 48 bits, 6 hex pairs separated by colons  - [ ] 128 bits, 16 decimal octets separated by dots
   - *IPv6 = 128 bits as 8 hextets (16 bits each) of hexadecimal, e.g. 2001:0db8:0000:0000:0000:ff00:0042:8329. 48 bits in hex pairs = a MAC (Media Access Control) address.*
   - @1.8.ipv6 ~9.16,9.17
3. Which TWO rules shorten an IPv6 address? (Select 2)
   - **[x] Drop leading zeros in each group**  - **[x] Replace ONE run of all-zero groups with ::**  - [ ] Drop trailing zeros in each group  - [ ] Use :: as many times as needed
   - *00A7 → A7, 0000 → 0, and one run of consecutive zero groups → ::. :: can only appear ONCE, or you couldn't tell how many zeros each one hides. Trailing zeros matter: 4C00 stays 4C00.*
   - @1.8.ipv6 ~9.18
4. Which is the FULLY compressed form of FE80:00A7:0000:0000:02AA:0000:4C00:FE9A?
   - [ ] FE80:00A7::2AA:0:4C:FE9A  - [ ] FE80:A7::2AA::4C00:FE9A  - [ ] FE80:00A7::2AA:0:4C00:FE9A  - **[x] FE80:A7::2AA:0:4C00:FE9A**
   - *Answer: FE80:A7::2AA:0:4C00:FE9A. Leading zeros dropped (00A7 → A7, 02AA → 2AA); the double 0000 run → ::; the lone 0000 → 0; 4C00 keeps its trailing zeros. Two :: in one address = invalid.*
   - @1.8.ipv6 ~9.21
5. Type 2001:0db8:0000:0000:0000:0000:0000:0001 in its shortest form.
   - [=] 2001:db8::1
   - *0db8 → db8, the six 0000 groups → ::, 0001 → 1. Result 2001:db8::1. The 2001:db8::/32 prefix is reserved for documentation, like 192.0.2.0/24 in IPv4.*
   - @1.8.ipv6
6. Type the IPv6 loopback address in shortest form.
   - [=] ::1
   - *::1 = 0:0:0:0:0:0:0:1, the IPv6 version of 127.0.0.1. :: on its own (all zeros) = the unspecified address, used before a host has one.*
   - @1.8.ipv6
7. Which prefix is IPv6 LINK-LOCAL?
   - [ ] 2002::/16  - **[x] fe80::/10**  - [ ] 2000::/3  - [ ] ff00::/8
   - *Link-local = fe80::/10: every IPv6 interface gives itself one automatically, and it only works on that link, never routed. It's like IPv4 APIPA (169.254), except IPv6 ALWAYS has one, even with a global address. Routers use link-locals as next hops.*
   - @1.8.ipv6 ~9.22,9.20
8. Global unicast IPv6 addresses, the routable "public" ones, start with which prefix?
   - **[x] 2000::/3**  - [ ] fe80::/10  - [ ] fc00::/7  - [ ] ff00::/8
   - *Global unicast = 2000::/3, today's internet addresses start 2 or 3 (e.g. 2001:, 2a00:). Unique local = fc00::/7 (in practice fd00::/8), IPv6's private range like RFC 1918. Multicast = ff00::/8.*
   - @1.8.ipv6 ~9.23
9. Which IPv6 range is the equivalent of IPv4 private (RFC 1918) addresses?
   - [ ] fe80::/10  - **[x] fc00::/7**  - [ ] 2001:db8::/32  - [ ] ::1/128
   - *ULA (Unique Local Address) = fc00::/7, routable inside an organisation but not on the internet. Link-local fe80:: never leaves the link at all. 2001:db8:: = documentation only.*
   - @1.8.ipv6
10. In a typical IPv6 address like 2001:db8:acad:1::25/64, what are the first 64 bits and the last 64 bits?
    - **[x] Network prefix, then interface ID**  - [ ] Interface ID, then MAC address  - [ ] Subnet mask, then host  - [ ] Global ID, then link-local
    - *Normal IPv6 LANs are /64: the first 64 bits = the prefix (routing + subnet), the last 64 = the interface ID. The interface ID can be random (privacy), or built from the MAC with EUI-64 (Extended Unique Identifier: MAC split in half, fffe inserted in the middle, 7th bit flipped).*
    - @1.8.ipv6
11. Which IPv6 address type delivers to the NEAREST of several interfaces sharing one address?
    - [ ] Unicast  - [ ] Multicast  - **[x] Anycast**  - [ ] Broadcast
    - *IPv6 types = unicast (one), multicast (group, ff00::/8) and anycast (nearest). NO broadcast in IPv6: all-nodes multicast ff02::1 does that job.*
    - @1.8.ipv6
12. What replaces ARP in IPv6?
    - **[x] Neighbor Discovery (ICMPv6)**  - [ ] DHCPv6 (stateful)  - [ ] IGMP (multicast)  - [ ] RARP (reverse ARP)
    - *NDP (Neighbor Discovery Protocol) uses ICMPv6 neighbour solicitation/advertisement messages (sent to multicast, not broadcast) to find MACs, plus router solicitation/advertisement to find routers and prefixes. So blocking ALL ICMPv6 breaks IPv6.*
    - @1.8.ipv6
13. A host builds its own global IPv6 address from the prefix in a router advertisement, with no DHCP server. Method?
    - **[x] SLAAC**  - [ ] DHCPv6 stateful  - [ ] APIPA  - [ ] NAT64
    - *SLAAC (Stateless Address Autoconfiguration) = the router advertises the /64 prefix and the host adds its own interface ID. DHCPv6 can still hand out DNS servers (stateless DHCPv6) or the addresses too (stateful).*
    - @1.8.ipv6
14. A company runs IPv4 and IPv6 on every device at the same time while migrating. Method?
    - **[x] Dual stack**  - [ ] Tunnelling  - [ ] NAT64  - [ ] 6to4
    - *Dual stack = both protocols live side by side; each connection uses whichever the far end supports (IPv6 preferred). The cleanest migration, but you manage two address plans and two sets of firewall rules.*
    - @1.8.ipv6 ~10.1
15. An IPv6 site must cross an ISP that only carries IPv4. Method?
    - [ ] Dual stack  - **[x] Tunnelling**  - [ ] NAT64  - [ ] SLAAC
    - *Tunnelling = wrap IPv6 packets inside IPv4 to cross an IPv4-only network (6to4, 6in4, Teredo, ISATAP). Translation (NAT64) is for when one side ONLY speaks one protocol.*
    - @1.8.ipv6 ~9.25
16. IPv6-only phones must reach an IPv4-only website. Method?
    - [ ] SLAAC  - [ ] 6to4  - **[x] NAT64**  - [ ] ISATAP
    - *NAT64 = translates between IPv6 and IPv4 at the edge, so a v6-only client can reach a v4-only server. DNS64 fakes an AAAA record for the v4-only site so the client knows where to send it. Mobile carriers use this widely.*
    - @1.8.ipv6 ~10.2
17. Match the three migration methods. Which list is right, in the order: dual stack, tunnelling, NAT64?
    - **[x] Run both · carry v6 inside v4 · translate v6 to v4**  - [ ] Translate · run both · carry v6 inside v4  - [ ] Carry v6 inside v4 · translate · run both  - [ ] Run both · translate · carry v6 inside v4
    - *The objectives' "compatibility requirements": dual stack = both at once. Tunnelling = encapsulate one inside the other. NAT64 = translate between them.*
    - @1.8.ipv6
18. Type the IPv6 prefix length normally used for a LAN subnet, e.g. /48.
    - [=] /64 | 64
    - */64 for every LAN, so SLAAC works. Sites typically get a /48 or /56 from the ISP and cut it into /64s. /128 = a single host. /127 is used for point-to-point links.*
    - @1.8.ipv6
19. Type the shortest form of each address, in order, separated by spaces: 2001:0db8:0000:0001:0000:0000:0000:0010 · fe80:0000:0000:0000:0a00:27ff:fe4e:66a1.
    - [=] 2001:db8:0:1::10 fe80::a00:27ff:fe4e:66a1
    - *First: 0db8 → db8, the single 0000 → 0, the run of three 0000 → ::, 0010 → 10. Second: the run of three zero groups after fe80 → ::, 0a00 → a00. Use :: on the LONGEST run.*
    - @1.8.ipv6
20. Type the full, uncompressed form of 2001:db8::1:0:5.
    - [=] 2001:0db8:0000:0000:0000:0001:0000:0005
    - *Count the groups you can see: 2001, db8, 1, 0, 5 = 5. There must be 8, so :: hides 3 zero groups. Then pad each group to 4 digits.*
    - @1.8.ipv6
21. Match each address to its type. Type the letters in order, e.g. abcde. ¶  Addresses: fe80::1 · ::1 · 2600:1f18::5 · ff02::1 · fd12:3456::9 ¶  A global unicast · B link-local · C unique local · D multicast · E loopback
    - [=] beadc | b e a d c | b,e,a,d,c
    - *fe80 = link-local. ::1 = loopback. 2600 starts with 2 = global unicast. ff = multicast (ff02::1 = all nodes). fd = unique local (ULA).*
    - @1.8.ipv6
22. Match each scenario to its migration method. Type the letters in order, e.g. abc. ¶  Scenarios: v6-only phones reach a v4-only site · servers run both v4 and v6 · two IPv6 sites connect across an IPv4-only WAN ¶  A dual stack · B tunnelling · C NAT64
    - [=] cab | c a b | c,a,b
    - *v6-only to v4-only = NAT64 (+ DNS64). Both protocols at once = dual stack. Across a v4-only network = tunnelling.*
    - @1.8.ipv6
23. A Linux host shows: ¶  $ ip -6 addr ¶  inet6 2001:db8:acad:10::abc/64 scope global ¶  inet6 fe80::5054:ff:fe12:3456/64 scope link ¶Type the address the host uses as the SOURCE for its router solicitations and neighbour discovery on the local link, without the /64.
    - [=] fe80::5054:ff:fe12:3456 | fe80::5054:ff:fe12:3456/64
    - *NDP (Neighbor Discovery Protocol) messages on the local link use the link-local address, scope link, not the global one. Routers also advertise their own fe80:: address as the default gateway. The ff:fe in the middle shows the interface ID was built with EUI-64 from the MAC 52:54:00:12:34:56 (7th bit flipped).*
    - @1.8.ipv6

### Key facts
- **IPv6 = 128 bits, 8 groups of 4 hex. Drop leading zeros; one :: for the longest zero run, only once.**
- **::1 loopback · :: unspecified · fe80::/10 link-local (always present, like APIPA) · fc00::/7 (fd) unique local = private · 2000::/3 global unicast · ff00::/8 multicast · 2001:db8:: docs.**
- **No broadcast: unicast, multicast, anycast. NDP (ICMPv6) replaces ARP. LANs are /64: prefix + interface ID (random or EUI-64).**
- **SLAAC = host builds its address from the router advert · DHCPv6 = stateful or stateless (just DNS).**
- **Migration: dual stack (both) · tunnelling (v6 inside v4: 6to4, Teredo) · NAT64 + DNS64 (translate v6-only to v4-only).**

## Test 11 - 2.1 Routing + NAT (27 Q)

1. A branch router has three routes an engineer typed in by hand and no routing protocol enabled. What is true of this setup? (Select 3)
   - **[x] Each path exists only because an administrator entered it**  - **[x] No route advertisements cross the wire for an attacker to tamper with**  - **[x] Easy to manage when there are only a handful of networks**  - [ ] Traffic shifts to a backup path on its own when the WAN link drops  - [ ] Grows effortlessly as hundreds of new subnets are added
   - *With hand-entered routes nothing is advertised, so the table is predictable and hard to poison, and it is easy to manage at small scale. The downside is that it never reacts to an outage and becomes a chore as the network grows. Protocols like OSPF exist to fix exactly that.*
   - @2.1.route ~10.3
2. Your company enables OSPF on all 40 of its routers instead of entering paths manually. Which benefits does this bring? (Select 3)
   - **[x] Routers learn remote networks from one another without manual entry**  - **[x] A failed link triggers recalculation and traffic takes a surviving path**  - **[x] Copes well as the number of routers and subnets keeps growing**  - [ ] No updates travel between routers, removing any spoofing risk  - [ ] An administrator must still key in every destination prefix
   - *Protocols such as OSPF, EIGRP and BGP swap reachability information and reconverge after a topology change. The price is some CPU, bandwidth and an exposure to injected routes, which is why neighbour authentication is recommended.*
   - @2.1.route ~10.4
3. What is "convergence"?
   - **[x] All routers agreeing on a consistent routing view after a topology change**  - [ ] Merging two subnets into one summary route  - [ ] Two routing protocols running on one router  - [ ] NAT combining many private IPs onto one public IP
   - *Convergence = the time between a change, like a link going down, and every router's table being correct again. Faster = less packet loss. Link-state and hybrid protocols converge faster than distance-vector.*
   - @2.1.route ~10.6
4. A network under one administrative control, identified by a number that BGP uses, is called a:
   - **[x] Autonomous system**  - [ ] Routing domain  - [ ] Broadcast domain  - [ ] Area 0
   - *AS (Autonomous System) = one organisation's network, like an ISP (Internet Service Provider), identified by an ASN (AS Number). Inside an AS you use IGPs (Interior Gateway Protocols); between ASs you use an EGP (Exterior Gateway Protocol), which in practice means BGP.*
   - @2.1.route ~10.5
5. Which routing protocol runs BETWEEN autonomous systems on the internet?
   - [ ] OSPF  - [ ] EIGRP  - **[x] BGP**  - [ ] Static routing
   - *BGP (Border Gateway Protocol) = the only EGP (Exterior Gateway Protocol) in use, the routing protocol of the internet. Hook: BGP = Between. It's path-vector: it shares the full AS path to each destination, which prevents loops and lets you set policy. TCP (Transmission Control Protocol) port 179.*
   - @2.1.route ~10.14,10.16,10.9
6. Which TWO are interior gateway protocols named on the Network+ objectives? (Select 2)
   - **[x] OSPF**  - **[x] EIGRP**  - [ ] BGP  - [ ] Static routing  - [ ] NAT
   - *IGPs (Interior Gateway Protocols) route inside one AS (Autonomous System): OSPF (Open Shortest Path First) and EIGRP (Enhanced Interior Gateway Routing Protocol). BGP (Border Gateway Protocol) is the exterior protocol BETWEEN ASs. Static routing isn't a protocol at all.*
   - @2.1.route ~10.15
7. A branch has a primary route to HQ learned by OSPF. The admin adds a static route over an LTE link that must be used ONLY if the OSPF route disappears. What makes it work?
   - **[x] Give the static (LTE) route a higher AD than the OSPF route's 110, e.g. 200**  - [ ] Leave the static route at its default AD of 1  - [ ] Give the static route an AD of 90  - [ ] Give the OSPF route a higher metric
   - *A floating static route = a backup static route with a higher AD (Administrative Distance) than the primary. OSPF = 110, so AD 200 keeps it out of the table until OSPF loses the route. At the default AD of 1 it would beat OSPF and always be used. Command: ip route 10.50.0.0 255.255.0.0 10.99.0.1 200.*
   - @2.1.sel ~10.7,10.11
8. An engineer is explaining how OSPF differs from older protocols that swap whole tables. Which statements are accurate for this protocol family? (Select 3)
   - **[x] Each router holds a full database of the area's topology**  - **[x] Advertisements are flooded when a change happens rather than on a fixed timer**  - **[x] Reconverges fast and fits large, hierarchical networks**  - [ ] Sends its entire routing table to neighbours every 30 seconds  - [ ] Chooses paths purely on the number of hops
   - *OSPF routers flood LSAs so each one has the same topology map, then run Dijkstra's SPF calculation locally. Its metric is cost, derived from interface bandwidth, not hop count.*
   - @2.1.route ~10.8
9. Two routers run an FHRP with virtual IP 10.0.0.1. R1 (10.0.0.2) is active, R2 (10.0.0.3) is standby. What should hosts use as their default gateway?
   - **[x] 10.0.0.1**  - [ ] 10.0.0.2  - [ ] 10.0.0.3  - [ ] Both 10.0.0.2 and 10.0.0.3
   - *Hosts point at the VIP (Virtual IP), 10.0.0.1. Whichever router is active answers for it, so when R1 dies R2 takes over the VIP and hosts never notice. Pointing hosts at R1's real address defeats the redundancy. FHRP (First Hop Redundancy Protocol) = HSRP (Hot Standby Router Protocol, Cisco) or VRRP (Virtual Router Redundancy Protocol, open standard).*
   - @2.1.fhrp ~10.12
10. Which routing protocol is usually called HYBRID, or advanced distance-vector?
    - [ ] BGP  - [ ] OSPF  - **[x] EIGRP**  - [ ] Static routing
    - *EIGRP (Enhanced Interior Gateway Routing Protocol) = Cisco-originated. Distance-vector-style metrics (a composite of bandwidth and delay by default) plus link-state-style fast, change-only updates. It keeps a backup "feasible successor" route ready for instant failover.*
    - @2.1.route ~10.10,10.13
11. Match each routing protocol type to its protocol. Type the letters in order, e.g. abc. ¶  Types: hybrid · path-vector · link-state ¶  A BGP · B OSPF · C EIGRP · D static
    - [=] cab | c a b | c,a,b
    - *Hybrid, or advanced distance-vector = C EIGRP (Enhanced Interior Gateway Routing Protocol). Path-vector = A BGP (Border Gateway Protocol). Link-state = B OSPF (Open Shortest Path First). Static isn't a protocol type at all.*
    - @2.1.route
12. Two protocols both offer a route to the same prefix. What decides which goes in the routing table?
    - **[x] Administrative distance, and LOWER wins**  - [ ] Administrative distance, and HIGHER wins  - [ ] Hop count  - [ ] Whichever was learned first
    - *AD (Administrative Distance) = how much the router trusts each route SOURCE, 0-255, lower = more trusted. It only compares between protocols. Within one protocol, the metric decides. Hook: AD = golf score, lowest wins.*
    - @2.1.sel ~10.17
13. Type the default administrative distance of a STATIC route.
    - [=] 1
    - *Connected = 0, static = 1. So a static route overrides OSPF or EIGRP for the same prefix, unless you add a higher AD to make a "floating static" backup route.*
    - @2.1.sel
14. Type the default administrative distance of OSPF.
    - [=] 110
    - *OSPF (Open Shortest Path First) = 110. It's the most tested value. Full ladder: connected 0 · static 1 · eBGP 20 · EIGRP 90 · OSPF 110.*
    - @2.1.sel
15. Type the default ADs for connected, static, eBGP, EIGRP, OSPF, in that order, separated by spaces.
    - [=] 0 1 20 90 110
    - *Connected 0 · static 1 · eBGP (external BGP) 20 · EIGRP (Enhanced Interior Gateway Routing Protocol) internal 90 · OSPF 110 · iBGP (internal BGP) 200 · 255 = never trusted. Hook: 0, 1, 20, then 90, 110.*
    - @2.1.sel
16. A router has routes to 10.1.0.0/16 via EIGRP and 10.1.1.0/24 via OSPF. A packet is sent to 10.1.1.5. Which route is used?
    - **[x] 10.1.1.0/24 via OSPF, because the longest prefix match wins**  - [ ] 10.1.0.0/16 via EIGRP, because EIGRP has the lower AD  - [ ] Both, load-balanced  - [ ] Neither, it uses the default route
    - *Route selection order: 1) longest prefix match = the most specific route; 2) AD, only between routes for the SAME prefix; 3) metric, within one protocol. /24 is more specific than /16, so AD never enters into it. This is the classic trap. No match at all and no default route = the router DROPS the packet (any ICMP 'destination unreachable' goes back to the SOURCE). A gateway of last resort is never added automatically.*
    - @2.1.sel ~10.18
17. Within one routing protocol, two paths to the same prefix exist. Which is chosen?
    - **[x] The lower metric**  - [ ] The higher metric  - [ ] The lower AD  - [ ] The newer route
    - *Metric = the protocol's own path cost, and lower is better. OSPF = cost from bandwidth · EIGRP = composite, bandwidth + delay by default · BGP = attributes such as the AS path. AD compares protocols; metric compares paths within one protocol.*
    - @2.1.sel ~10.19
18. Which maps private internal addresses to public ones?
    - [ ] VPN  - **[x] NAT**  - [ ] GRE  - [ ] VIP
    - *NAT (Network Address Translation) rewrites IP (Internet Protocol) addresses as packets cross the edge. Static NAT = one private to one public, for servers. Dynamic NAT = a pool. PAT = many to one. VPN = Virtual Private Network, GRE = Generic Routing Encapsulation, VIP = Virtual IP.*
    - @2.1.nat ~10.20
19. What makes PAT different from basic NAT? (Select 2)
    - **[x] Many hosts share ONE public IP**  - **[x] Connections are kept apart by source PORT number**  - [ ] Each host gets its own public IP  - [ ] It only translates the destination address
    - *PAT (Port Address Translation), also called NAT overload = what every home router does. It tracks each session by public IP + a unique port, so thousands of hosts fit behind one address. Hook: PAT = Port.*
    - @2.1.nat ~10.21
20. Type the IOS keyword at the end of an ip nat inside source command that turns NAT into PAT.
    - [=] overload
    - *ip nat inside source list 1 interface g0/1 overload = all hosts matched by ACL (Access Control List) 1 share g0/1's address, using ports. Without overload, each host needs its own public address from a pool.*
    - @2.1.nat
21. Internet users must reach a web server at 192.168.1.50 on TCP 443 behind a home router. Configure?
    - **[x] Port forwarding of TCP 443 to 192.168.1.50**  - [ ] A DHCP reservation for 192.168.1.50  - [ ] UPnP enabled on every device  - [ ] A new internal DNS server for the site
    - *Port forwarding = a static PAT rule: inbound public-IP:443 → 192.168.1.50:443. Pair it with a DHCP (Dynamic Host Configuration Protocol) reservation so the server's IP doesn't move. UPnP (Universal Plug and Play) lets any device open ports, which is a security risk. In a business, put the server in a screened subnet (DMZ, demilitarised zone).*
    - @2.1.nat ~27.19
22. Two core routers run VRRP. What does this protocol provide? (Select 3)
    - **[x] A single virtual IP that hosts use as their default gateway**  - **[x] Automatic failover to a backup router when the primary goes down**  - **[x] Resilience for the first-hop gateway without reconfiguring clients**  - [ ] Hands out IP addresses to every host on the segment  - [ ] Makes OSPF or BGP unnecessary between sites
    - *First hop redundancy protocols include HSRP and GLBP from Cisco plus the open VRRP standard. Hosts keep pointing at one virtual address, so a router failure is invisible to them. GLBP can also spread load across routers. FHRPs do not assign addresses (that is DHCP) and do not replace routing protocols.*
    - @2.1.fhrp ~10.22
23. R1 is the VRRP master. It fails and R2 takes over. R1 then comes back online. With default settings, what happens?
    - **[x] R1 takes the master role back, because VRRP preempts by default**  - [ ] R2 stays master until it fails, because VRRP never preempts  - [ ] Both routers become master and load-balance  - [ ] Hosts must renew DHCP before they can use R1 again
    - *VRRP preemption is ON by default: the higher-priority router reclaims master when it returns. HSRP preemption is OFF by default, so you have to configure standby preempt. Classic exam difference. Hook: VRRP takes it back, HSRP holds back.*
    - @2.1.fhrp
24. A router's g0/1 is configured as g0/1.10, g0/1.20 and g0/1.30 to route between VLANs over one trunk. What is true of these logical interfaces? (Select 3)
    - **[x] One physical port is divided into multiple logical interfaces**  - **[x] Each logical interface gets its own IP address on the shared port**  - **[x] Different policies, such as separate ACLs, can be applied to each**  - [ ] The physical port can then hold only a single IP address  - [ ] Routing between the VLANs is no longer required
    - *Each logical interface is bound to a VLAN with 802.1Q tagging. This is router-on-a-stick: one trunk link carries several VLANs and the router routes between them.*
    - @2.1.fhrp ~10.24
25. PBQ: R1# show ip route ¶S*   0.0.0.0/0 1/0 via 203.0.113.1 ¶O    10.0.0.0/8 110/30 via 172.16.1.1 ¶D    10.20.0.0/16 90/2816 via 172.16.2.1 ¶S    10.20.30.0/24 1/0 via 172.16.3.1 ¶C    172.16.1.0/30 is directly connected, Gi0/1 ¶C    172.16.2.0/30 is directly connected, Gi0/2 ¶C    172.16.3.0/30 is directly connected, Gi0/3 ¶C    203.0.113.0/30 is directly connected, Gi0/0 ¶Type the next-hop IP R1 uses for each destination.
    - [p] Next hop for a packet to 10.20.30.77? = 172.16.3.1
    - [p] Next hop for a packet to 10.20.99.1? = 172.16.2.1
    - [p] Next hop for a packet to 10.99.1.1? = 172.16.1.1
    - [p] How does R1 reach 172.16.2.2? :: A 172.16.2.1 · B directly connected out Gi0/2 · C 203.0.113.1 · D 172.16.1.1 = b
    - [p] An admin adds a static route to 10.0.0.0/8 via 172.16.2.1. Which 10.0.0.0/8 route goes in the table :: A the static, AD 1 beats OSPF's 110 · B OSPF, its metric 30 is lower · C both, load-balanced · D whichever was learned first = a
    - *Longest prefix match first. 10.20.30.77 matches /8, /16 and /24, and the /24 wins. 10.20.99.1 matches /16 and /8, so the /16. 10.99.1.1 only matches /8. 8.8.8.8 matches nothing but the default. 172.16.2.2 is on a directly connected subnet. In 1/0 or 110/30 the first number is AD and the second the metric. AD only breaks ties between routes to the SAME prefix, and lower wins: connected 0, static 1, eBGP 20, EIGRP 90, OSPF 110, RIP 120. Metrics are only compared within one protocol.*
    - @2.1.route
26. PBQ: Three routers in a chain, joined by 2 cables. No routing protocol runs. ¶ A router can only hand traffic to the router at the other end of ITS OWN cable. ¶ ¶  LAN-A  10.1.0.0/24 ¶    │ ¶   ==R1== ¶    │ 10.12.0.1   R1 plugs in here ¶    │    CABLE 1   subnet 10.12.0.0/30 ¶    │ 10.12.0.2   R2 plugs in here ¶   ==R2== ¶    │ 10.23.0.2   R2 plugs in here ¶    │    CABLE 2   subnet 10.23.0.0/30 ¶    │ 10.23.0.3   R3 plugs in here ¶   ==R3== ────── ISP 198.51.100.1 ¶    │ ¶  LAN-C  10.3.0.0/24 ¶ ¶Next hop = the IP at the OTHER end of the router's own cable, toward the destination. ¶Parts 1-4: type the full command, like ip route 10.9.9.0 255.255.255.0 10.8.8.8
    - [p] R1: route to LAN-C = ip route 10.3.0.0 255.255.255.0 10.12.0.2
    - [p] R2: route to LAN-A = ip route 10.1.0.0 255.255.255.0 10.12.0.1
    - [p] R2: route to LAN-C = ip route 10.3.0.0 255.255.255.0 10.23.0.3
    - [p] R1: default route so LAN-A can reach the internet = ip route 0.0.0.0 0.0.0.0 10.12.0.2
    - [p] Routes so far are R1 and R2 as above. A LAN-A PC pings a LAN-C PC and it fails. What is missing :: A R3 has no route back to LAN-A · B R1 needs a route to 10.23.0.0/30 · C R2 needs a default route · D the /30 links are too small = a
    - *ip route network mask next-hop. The next hop is always the NEIGHBOUR's IP on the shared link, never your own. The middle router R2 knows only its two connected /30s, so it needs routes to BOTH LANs: forgetting it is the classic mistake. A default route 0.0.0.0 0.0.0.0 means everything else. R1's default points at R2, but R2 also needs its own default to R3 (10.23.0.3) or internet traffic dies at R2. Routing must work both ways: the ping reaches LAN-C, but R3 has no route back to 10.1.0.0/24, so the reply is dropped.*
    - @2.1.route
27. A network administrator wants traffic to move to a backup WAN link automatically if the primary connection fails. Which should be configured?
    - **[x] A dynamic routing protocol such as EIGRP**  - [ ] RSTP  - [ ] LDAP  - [ ] IPsec  - [ ] ACLs
    - *Answer: A dynamic routing protocol (EIGRP). It learns both paths and re-converges onto the backup route when the primary drops (a floating static route is the static alternative). RSTP is Layer 2 loop prevention inside a switched LAN, not WAN path failover. LDAP = directory, IPsec = tunnels, ACLs = filtering. Hook: routers pick paths; STP just blocks loops.*
    - @2.1.route

### Key facts
- **Static = manual, secure, doesn't scale · dynamic = learns and adapts. IOS: ip route net mask next-hop · default = 0.0.0.0 0.0.0.0.**
- **Types: OSPF link-state (cost, full map) · EIGRP hybrid / advanced distance-vector · BGP path-vector, between ASs, TCP 179.**
- **Selection: 1 longest prefix · 2 lowest AD · 3 lowest metric. AD: connected 0 · static 1 · eBGP 20 · EIGRP 90 · OSPF 110 · iBGP 200. Floating static = static with AD above the primary, e.g. 200.**
- **NAT = private to public · static 1:1 · PAT/overload = many to one by port · port forwarding = inbound static PAT.**
- **FHRP = HSRP (Cisco) · VRRP (open) · GLBP (load-balances), sharing a VIP gateway. Subinterface = g0/0.10 + encapsulation dot1q 10 = router-on-a-stick.**

## Test 12 - 2.2 Switching (23 Q)

1. What lets hosts on different switches act as one broadcast domain, wherever they physically sit?
   - **[x] VLAN**  - [ ] VPN  - [ ] Screened subnet  - [ ] Intranet
   - *VLAN (Virtual Local Area Network) = a logical broadcast domain defined by switch configuration, not wiring. One VLAN usually = one IP subnet. VPN (Virtual Private Network) = an encrypted tunnel, which is a different thing.*
   - @2.2.vlan ~10.25
2. Which switch feature stores the VLAN IDs and names configured on the switch?
   - **[x] VLAN database**  - [ ] MAC address table  - [ ] Routing table  - [ ] ARP cache
   - *VLAN database = the switch's record of VLAN IDs and names (vlan.dat on Cisco). VTP (VLAN Trunking Protocol) can copy it between switches. MAC (Media Access Control) table = which MAC is on which port.*
   - @2.2.vlan ~11.1
3. The virtual Layer 3 interface on a switch that routes for a VLAN is called a:
   - **[x] SVI**  - [ ] Subinterface  - [ ] Trunk port  - [ ] Port channel
   - *SVI (Switch Virtual Interface) = interface vlan 10 with an IP, acting as the VLAN's default gateway on a Layer 3 switch. It's faster than router-on-a-stick because routing happens in the switch hardware. A subinterface (g0/0.10) is the ROUTER version.*
   - @2.2.vlan ~11.2
4. Which VLAN carries UNTAGGED frames on an 802.1Q trunk?
   - [ ] Default VLAN  - [ ] Voice VLAN  - [ ] Data VLAN  - **[x] Native VLAN**
   - *Native VLAN = anything arriving on a trunk without a tag goes here. It must MATCH on both ends, or traffic leaks between VLANs. Default VLAN = VLAN 1, where every port starts. Security: move native off VLAN 1 to stop VLAN hopping (double tagging).*
   - @2.2.intf ~11.3
5. Which VLAN type separates and prioritises IP phone traffic?
   - [ ] Data VLAN  - [ ] Management VLAN  - **[x] Voice VLAN**  - [ ] Native VLAN
   - *Voice VLAN = the phone tags its own traffic into it, and QoS (Quality of Service) prioritises it, while the PC plugged into the phone stays on the data VLAN. Both share one access port. VoIP = Voice over Internet Protocol.*
   - @2.2.intf ~11.4
6. Which IEEE standard tags Ethernet frames with a VLAN ID on a trunk?
   - [ ] 802.1X  - **[x] 802.1Q**  - [ ] 802.3ad  - [ ] 802.1D
   - *802.1Q ("dot1q") inserts a 4-byte tag holding a 12-bit VLAN ID (1-4094), plus 3 priority bits used by QoS. Trunk = one link carrying many VLANs. Access port = one VLAN, untagged. Traps: 802.1X = port authentication, 802.3ad = LACP, 802.1D = STP. IEEE = Institute of Electrical and Electronics Engineers.*
   - @2.2.intf ~11.5
7. Which protocol bundles several physical ports into one logical link?
   - [ ] VRRP  - **[x] LACP**  - [ ] HSRP  - [ ] STP
   - *LACP (Link Aggregation Control Protocol, IEEE 802.3ad/802.1AX) = port channel / EtherChannel / NIC teaming. You get more bandwidth and redundancy, and STP sees one link instead of blocking. VRRP (Virtual Router Redundancy Protocol) and HSRP (Hot Standby Router Protocol) are for gateways, not links.*
   - @2.2.intf ~11.6
8. Two security guards use handheld radios: either can talk, but one must finish before the other replies. What transmission mode is this?
   - [ ] Simplex  - **[x] Half-duplex**  - [ ] Full-duplex  - [ ] Auto-MDIX
   - *Half-duplex means both sides can send, just not at the same moment, so collisions are possible on shared media such as hubs. Simplex is strictly one way, and full-duplex sends and receives at once.*
   - @2.2.intf ~11.7
9. Which everyday situation matches a link that sends and receives at the same time?
   - **[x] Two people on a phone call speaking over each other**  - [ ] Two hikers using radios and saying over after each message  - [ ] A radio station broadcasting to listeners  - [ ] Several PCs on a hub waiting their turn on the wire
   - *Full-duplex uses separate paths for each direction, so there are no collisions. Modern switch ports negotiate full duplex by default. Radios taking turns are half duplex, a broadcast is simplex, and a hub forces half duplex.*
   - @2.2.intf ~11.8,26.6
10. One end is set to full duplex, the other autonegotiates and falls back to half. Symptom?
    - **[x] Slow throughput with late collisions and CRC errors**  - [ ] The link won't come up at all on either end  - [ ] Only broadcast traffic fails to cross the link  - [ ] Nothing, autonegotiation fixes it on its own
    - *Duplex mismatch = the classic cause of a link that is up but slow. The half-duplex side sees late collisions and the full side sees CRC (Cyclic Redundancy Check) errors and runts. Fix: set both ends the same, preferably both auto. Speed mismatch (hard-set 1G one end, 100M the other) = NO link light at all. MTU, LACP or wrong-subnet problems all leave the link light ON.*
    - @2.2.intf
11. On a legacy hub segment, a NIC senses the cable, transmits, notices a collision, sends a jam signal and waits a random time. Which access method is this?
    - **[x] CSMA/CD**  - [ ] CSMA/CA  - [ ] Token passing  - [ ] Polling
    - *CSMA/CD is the wired shared-medium method: sense the carrier, transmit, detect collisions, jam and retry after a random backoff. Full-duplex switch links never collide, so it is not used there.*
    - @2.2.intf ~26.3
12. A laptop on an 802.11 network waits for the channel to be quiet plus a random timer before transmitting, since radios cannot hear collisions while sending. Which access method is in use?
    - [ ] CSMA/CD  - **[x] CSMA/CA**  - [ ] Band steering  - [ ] Full duplex
    - *CSMA/CA is the wireless method: check the channel is clear, wait a random backoff, and optionally use RTS/CTS. Memory aid: cable Detects, air Avoids.*
    - @2.2.intf ~26.4
13. An old hub in a lab is replaced with a switch. What is the key change in how frames are delivered?
    - **[x] The switch forwards to the destination port only; the hub repeated to all ports**  - [ ] The hub worked at Layer 2 while the switch works at Layer 1  - [ ] The hub routed between subnets but the switch cannot  - [ ] The switch is limited to half duplex where the hub ran full duplex
    - *A hub is a Layer 1 repeater with a single collision domain. A switch learns MAC addresses into its CAM table, gives each port its own collision domain and runs full duplex. Both remain one broadcast domain without VLANs.*
    - @2.2.intf ~26.5
14. A data center switch is set so no damaged frame ever leaves it, accepting a little extra latency to verify each frame's FCS first. Which switching method is this?
    - **[x] Store-and-forward**  - [ ] Cut-through  - [ ] Fragment-free  - [ ] Flooding
    - *Store-and-forward reads the entire frame and validates the FCS before sending, so errors are not propagated, at the cost of slightly more delay than cut-through.*
    - @2.2.intf ~27.3
15. A low-latency trading network wants switches to forward as soon as the destination MAC is read. Mode?
    - [ ] Store-and-forward  - **[x] Cut-through**  - [ ] Fragment-free  - [ ] Half duplex
    - *Cut-through = starts forwarding after the first 6 bytes (the destination MAC): lowest latency, but it passes on bad frames. Fragment-free = waits for 64 bytes, which drops collision runts. Hook: CUT the queue.*
    - @2.2.intf ~27.4
16. Which protocol prevents switching loops and, in its modern form, converges in seconds?
    - **[x] RSTP**  - [ ] VRRP  - [ ] LACP  - [ ] OSPF
    - *STP (Spanning Tree Protocol, 802.1D) elects a root bridge and blocks redundant links, so frames can't loop forever and create broadcast storms. RSTP (Rapid STP, 802.1w) converges in about 1-2 seconds instead of 30-50. Hook: STP = Stops The Party of loops.*
    - @2.2.stp ~11.9
17. Put the classic 802.1D STP port states in order, from a port coming up to passing traffic. Type the letters, e.g. abcd. ¶  A forwarding · B learning · C blocking · D listening
    - [=] cdba | c d b a | c,d,b,a
    - *Blocking → listening (15 s) → learning (15 s, filling the MAC table) → forwarding. Plus disabled. It takes up to 50 s with max age, which is why PortFast and RSTP exist. RSTP collapses these into discarding, learning, forwarding.*
    - @2.2.stp
18. An office desk port configured with PortFast shuts itself down as soon as an employee connects a small switch that sends BPDUs. Which feature did this?
    - [ ] Root guard  - **[x] BPDU guard**  - [ ] Port mirroring  - [ ] Loop guard
    - *BPDU guard belongs on edge ports. Receiving any BPDU puts the port into err-disabled, which blocks rogue switches and accidental loops. Root guard blocks a port that receives a superior BPDU but leaves it up, and loop guard reacts to BPDUs that stop arriving.*
    - @2.2.stp ~26.10
19. A distribution switch should still exchange spanning tree messages with switches below it, but must block any of them that advertises a better bridge ID. Which feature fits?
    - [ ] BPDU guard  - **[x] Root guard**  - [ ] PortFast  - [ ] DHCP snooping
    - *Root guard places a port in a root-inconsistent blocking state if a superior BPDU arrives, keeping the intended root in place. Unlike BPDU guard, normal BPDUs are still allowed.*
    - @2.2.stp ~26.11
20. The largest payload a link carries without fragmentation is the:
    - **[x] MTU**  - [ ] MSS  - [ ] TTL  - [ ] Frame size limit, 64 bytes
    - *MTU (Maximum Transmission Unit) = 1500 bytes for standard Ethernet. MSS (Maximum Segment Size) = the TCP payload inside it, 1460. 64 bytes = the MINIMUM frame. Bigger packets get fragmented, or dropped if DF (Don't Fragment) is set. Tunnels such as IPsec (Internet Protocol Security) and GRE (Generic Routing Encapsulation) add headers, which cause MTU problems.*
    - @2.2.mtu ~11.10
21. Non-standard Ethernet frames with a much larger payload, used for storage and data centres?
    - **[x] Jumbo frames**  - [ ] Runts  - [ ] Giants  - [ ] Baby giants
    - *Jumbo frames = MTU up to about 9000 bytes, so fewer frames and less CPU (Central Processing Unit) load for iSCSI (Internet Small Computer Systems Interface) SANs (Storage Area Networks) and backups. EVERY device in the path must support it. Runt = under 64 bytes. Giant = an oversized frame when jumbo isn't enabled.*
    - @2.2.mtu ~11.11
22. PBQ: Configure access switch SW3. Data VLAN 10, voice VLAN 50, AP management VLAN 99, guest VLAN 30, parking VLAN 999. ¶  Gi0/1  a desk PC ¶  Gi0/2  an IP phone with a PC plugged into it ¶  Gi0/3  an AP broadcasting staff, voice and guest SSIDs, managed on VLAN 99 untagged ¶  Gi0/24 uplink to the distribution switch ¶  Gi0/9  unused ¶Answer each part.
    - [p] Gi0/2: type the voice VLAN ID = 50
    - [p] Gi0/3 mode :: A access · B trunk = b
    - [p] Gi0/3: type the native VLAN = 99
    - [p] Gi0/24: type the allowed VLAN list, lowest first, separated by commas = 10,30,50,99 | 10, 30, 50, 99 | 10 30 50 99
    - [p] Gi0/9: type the interface command that disables it = shutdown | shut
    - *PC = access VLAN 10. Phone port = access VLAN 10 for the PC plus voice VLAN 50: the phone tags voice and passes the PC's frames untagged. A lightweight AP carrying several SSIDs on their own VLANs = trunk, with the management VLAN 99 as native, since the AP sends its own traffic untagged. Uplinks carry every VLAN in use, and pruning to only those is best practice. Unused ports = parking VLAN AND shut down.*
    - @2.2.vlan
23. PBQ: Two switches joined on Gi0/24: ¶  SW1# show interfaces trunk ¶  Port    Mode  Native  Allowed ¶  Gi0/24  on    1       10,20,30 ¶  SW2# show interfaces trunk ¶  Port    Mode  Native  Allowed ¶  Gi0/24  on    99      10,20 ¶Users in VLAN 30 on SW2 can't reach VLAN 30 on SW1, and both switches log repeated errors on Gi0/24.
    - [p] Which setting mismatches and causes the log errors :: A native VLAN · B trunk mode · C duplex · D speed = a
    - [p] Type the SW1 Gi0/24 command to match SW2's native VLAN = switchport trunk native vlan 99
    - [p] Type the VLAN missing from SW2's allowed list = 30
    - [p] Type the SW2 interface command that adds it without removing the others = switchport trunk allowed vlan add 30
    - *Compare the two outputs column by column: mode on/on matches, but native is 1 vs 99, which logs native VLAN mismatch errors and lets untagged frames land in the wrong VLAN, a security risk too. Fix one end so both match. VLAN 30 isn't allowed on SW2's trunk. Use "add", because a plain "switchport trunk allowed vlan 30" REPLACES the list and cuts VLANs 10 and 20. The native VLAN crosses untagged.*
    - @2.2.vlan

### Key facts
- **VLAN = logical broadcast domain · VLAN database · SVI = interface vlan N, L3 gateway · access port = one VLAN untagged · trunk = 802.1Q tags (dot1q, 4 bytes, VLAN IDs 1-4094).**
- **Native VLAN = untagged on the trunk, must match both ends, move it off VLAN 1 · voice VLAN = phone traffic plus QoS, switchport voice vlan N.**
- **LACP 802.3ad = channel-group N mode active/passive · PAgP = desirable/auto · on = no protocol.**
- **Duplex: simplex one way · half taking turns (CSMA/CD, collisions) · full both at once. Mismatch = late collisions/CRC and slow. CSMA/CA = Wi-Fi.**
- **Store-and-forward checks the CRC · cut-through reads the destination MAC then goes · fragment-free reads 64 bytes.**
- **STP 802.1D: blocking, listening, learning, forwarding (about 50 s) · RSTP 802.1w about 2 s · BPDU guard = err-disable on a BPDU · root guard = block a superior BPDU · PortFast = edge ports.**
- **MTU 1500 · jumbo about 9000, for storage, and every hop must support it.**

## Test 13 - 2.3 Wireless Standards (23 Q)

1. Which legacy 802.11 standards are matched correctly? (Select 2)
   - **[x] 802.11a = 5 GHz, 54 Mbps**  - **[x] 802.11g = 2.4 GHz, 54 Mbps**  - [ ] 802.11b = 5 GHz, 11 Mbps  - [ ] 802.11g = 5 GHz, 600 Mbps
   - *802.11a = 5 GHz, 54 Mbps · 802.11b = 2.4 GHz, 11 Mbps · 802.11g = 2.4 GHz, 54 Mbps, backward compatible with b. Recognition is enough: the detail the exam wants is n/ac/ax = Wi-Fi 4/5/6. Hook: a = Above (5 GHz); b and g = the 2.4 ones.*
   - @2.3.freq ~5.24
2. A company runs 40 APs and wants one place to push SSIDs, security settings and firmware to all of them. Which AP type fits?
   - **[x] Lightweight APs managed by a wireless LAN controller**  - [ ] Autonomous APs, each configured on its own  - [ ] Ad hoc mode on every laptop  - [ ] A point-to-point bridge
   - *Lightweight APs get their config from a WLC (Wireless LAN Controller), on-site or in the cloud, over CAPWAP (Control And Provisioning of Wireless Access Points). Autonomous APs are standalone: fine for one or two, painful at 40. Hook: autonomous = on its own; lightweight = the controller carries the weight.*
   - @2.3.ap ~5.25
3. A café has ONE AP and no IT staff. Which AP type is simplest?
   - **[x] Autonomous, configured on its own through its web page**  - [ ] Lightweight, which needs a controller  - [ ] A mesh of lightweight APs  - [ ] An AP in monitor mode
   - *An autonomous AP holds its own config, so a single AP needs nothing else. A lightweight AP does nothing useful without a controller to join. Controllers pay off once there are many APs.*
   - @2.3.ap ~6.1
4. Which IEEE standard is Wi-Fi 6?
   - [ ] 802.11ac  - [ ] 802.11be  - **[x] 802.11ax**  - [ ] 802.11n
   - *Wi-Fi 6 = 802.11ax: 2.4 AND 5 GHz, about 9.6 Gbps, OFDMA (OFDM Multiple Access, which splits channels between many clients: dense areas), uplink and downlink MU-MIMO, TWT (Target Wake Time, saves battery). Hook: ax = "all + eXtra".*
   - @2.3.freq ~6.4
5. What does the E in Wi-Fi 6E add?
   - **[x] The 6 GHz band**  - [ ] Encryption  - [ ] Extended range on 2.4 GHz  - [ ] A new IEEE standard beyond 802.11ax
   - *Wi-Fi 6E = the same 802.11ax and the same 9.6 Gbps, Extended into 6 GHz. So it covers 2.4 + 5 + 6 GHz. 6 GHz requires WPA3.*
   - @2.3.freq ~6.5,6.6
6. Match each standard to its Wi-Fi generation. Type the letters in order, e.g. abc. ¶  Standards: 802.11ax · 802.11n · 802.11ac ¶  A Wi-Fi 4 · B Wi-Fi 5 · C Wi-Fi 6 · D Wi-Fi 7
   - [=] cab | c a b | c,a,b
   - *ax = Wi-Fi 6/6E (2.4 + 5 (+ 6), 9.6 Gbps) · n = Wi-Fi 4 (2.4 + 5, 600 Mbps) · ac = Wi-Fi 5 (5 only, 6.9 Gbps). Wi-Fi 7 = 802.11be, not on N10-009.*
   - @2.3.freq
7. Which lists the max speeds of 802.11b, a/g, n, ac and ax, in that order?
   - **[x] 11 Mbps · 54 Mbps · 600 Mbps · ~6.9 Gbps · ~9.6 Gbps**  - [ ] 11 Mbps · 54 Mbps · 300 Mbps · ~1.3 Gbps · ~3.5 Gbps  - [ ] 54 Mbps · 11 Mbps · 600 Mbps · ~9.6 Gbps · ~6.9 Gbps  - [ ] 2 Mbps · 11 Mbps · 54 Mbps · 600 Mbps · ~6.9 Gbps
   - *b 11 · a/g 54 · n 600 · ac about 6.9 Gbps · ax about 9.6 Gbps. Hook: "11, 54, 600, then 7 and 10 gig, roughly".*
   - @2.3.freq
8. Which apply to the 2.4 GHz band compared with 5 and 6 GHz? (Select 3)
   - **[x] Longest range and best wall penetration**  - **[x] Most interference and congestion**  - **[x] Fewest non-overlapping channels**  - [ ] Most channels  - [ ] Shortest range
   - *Lower frequency = travels further and passes walls better, but it's crowded: microwaves, Bluetooth, baby monitors, neighbours. It has only 3 non-overlapping channels.*
   - @2.3.freq ~11.15
9. A company is evaluating Wi-Fi 6E radios. Which claim about the 6 GHz band is FALSE?
   - **[x] It reaches farther than any other Wi-Fi band**  - [ ] It offers the largest number of non-overlapping channels  - [ ] It typically has the least interference  - [ ] It supports the highest throughput
   - *6 GHz has wide, uncongested spectrum and top speeds, but as the highest frequency it travels and penetrates walls the least. So the range claim is the false one.*
   - @2.3.freq ~11.17,11.16
10. Type the three non-overlapping 2.4 GHz channels, in order, separated by spaces.
    - [=] 1 6 11
    - *2.4 GHz channels are 5 MHz apart but about 20-22 MHz wide, so only 1, 6 and 11 avoid overlapping in the US. Adjacent APs (Access Points) should use different ones from these three. Hook: 1-6-11, "a one-sixty-eleven".*
    - @2.3.chan ~11.13
11. What happens when you widen a channel from 20 to 80 MHz?
    - **[x] More throughput, but fewer channels and more interference**  - [ ] Range doubles, but throughput stays the same  - [ ] Latency falls, but only 2.4 GHz can use it  - [ ] Interference from neighbours drops to almost none
    - *Channel bonding / wider channels = more data per transmission, but they eat more spectrum, so there are fewer non-overlapping channels to reuse. Use 20 MHz on 2.4 GHz, 40-80 MHz on 5 GHz, 160 MHz on 6 GHz. Hook: a wide road carries more cars but there's less room for other roads.*
    - @2.3.chan ~11.12
12. An AP nudges dual-band clients from 2.4 GHz to 5 or 6 GHz. Feature?
    - [ ] Channel bonding  - [ ] Wi-Fi Direct  - **[x] Band steering**  - [ ] Frequency hopping
    - *Band steering = moves clients off the crowded 2.4 GHz band. Channel bonding = joins channels for width. Wi-Fi Direct = device to device with no AP. FHSS (Frequency-Hopping Spread Spectrum) = old, Bluetooth-style.*
    - @2.3.freq ~11.18
13. Which 802.11 amendment adds DFS and TPC for 5 GHz radar avoidance?
    - **[x] 802.11h**  - [ ] 802.11k  - [ ] 802.11r  - [ ] 802.11s
    - *802.11h = DFS (Dynamic Frequency Selection: detect radar, such as weather or airport radar, and move off the channel; the standard also requires spreading load evenly across channels, so it's not radar-only) + TPC (Transmit Power Control: lowest power needed, to cut interference with satellites and others). Exam clue: 'AP automatically changes frequency/channel to avoid conflicts or interference' = 802.11h. (Vendor auto-channel/RRM dodging other APs is the same idea but proprietary.) A DFS event makes the AP suddenly change channel, which clients see as a brief drop. 802.11k = roaming neighbour reports, 802.11r = fast roaming, 802.11s = mesh. Hook: h = help the radar.*
    - @2.3.chan ~11.14,25.7
14. Why must an AP have the correct country code?
    - **[x] Regulators set the allowed channels and maximum power**  - [ ] It picks the captive portal language  - [ ] It enables WPA3  - [ ] It sets the DHCP scope
    - *Regulatory impacts = the FCC (Federal Communications Commission, US), ETSI (Europe) and ACMA (Australia) set the legal channels and power. E.g. 2.4 GHz channels 12-13 are allowed in Europe and Australia but not the US. A wrong code = illegal transmission, or clients that can't see the network.*
    - @2.3.chan ~25.6
15. What did 5G add over 4G LTE?
    - **[x] mmWave high band and much lower latency**  - [ ] Longer range, with the same latency  - [ ] Satellite backhaul for every cell  - [ ] WPA3 encryption on the radio link
    - *5G bands: low (long range) · mid (the balance) · high / mmWave (millimetre wave: very fast, very short range, blocked by walls and even hands). The main wins over LTE = latency of about 1-10 ms and more capacity.*
    - @1.5.wless ~26.22
16. Which describe satellite internet? (Select 3)
    - **[x] High latency**  - **[x] Weather-dependent interference**  - **[x] Expensive compared with wired service**  - [ ] Low latency  - [ ] Immune to interference
    - *Traditional GEO (Geostationary Earth Orbit, 36,000 km) satellite = about 600 ms round trip, rain fade, costly. It's for remote sites. LEO (Low Earth Orbit, e.g. Starlink) cuts the latency to about 25-60 ms using many low satellites.*
    - @1.5.wless ~6.8
17. Why does GEO satellite internet feel sluggish for VoIP and gaming even when the bandwidth is fine?
    - **[x] About 36,000 km each way adds roughly 600 ms latency**  - [ ] Satellite links run half duplex, so traffic takes turns  - [ ] 802.11h power control throttles the uplink  - [ ] It shares the crowded 2.4 GHz band with Wi-Fi
    - *Latency ≠ bandwidth. Physics sets the minimum delay for geostationary orbit. VoIP (Voice over IP) wants under about 150 ms one way. LEO fixes this by being much closer.*
    - @1.5.wless
18. A client's Wi-Fi radio supports only 802.11ac. Which band can it NOT use?
    - **[x] 2.4 GHz**  - [ ] 5 GHz  - [ ] 20 MHz channels  - [ ] 80 MHz channels
    - *802.11ac (Wi-Fi 5) = 5 GHz only. Most "ac" devices also include an 802.11n radio for 2.4, but the ac standard itself doesn't cover 2.4. Classic trap.*
    - @2.3.freq
19. Which technique lets Wi-Fi 6 serve many clients in one transmission by splitting a channel into resource units?
    - **[x] OFDMA**  - [ ] CSMA/CD  - [ ] DFS  - [ ] Band steering
    - *OFDMA (Orthogonal Frequency-Division Multiple Access) = the channel is divided into RUs (Resource Units), each serving a different client at the same time. It's the key Wi-Fi 6 gain for stadiums and offices.*
    - @2.3.freq
20. Match each description to its standard. Type the letters in order, e.g. abcde. ¶  2.4 GHz only, 54 Mbps · 5 GHz only, about 6.9 Gbps · dual-band, 600 Mbps, first MIMO · 2.4 GHz only, 11 Mbps · dual-band, OFDMA, 9.6 Gbps ¶  A 802.11b · B 802.11g · C 802.11n · D 802.11ac · E 802.11ax · F 802.11a
    - [=] bdcae | b d c a e | b,d,c,a,e
    - *B g = 2.4 / 54. D ac = 5 only / 6.9 Gbps. C n = 2.4 + 5 / 600, MIMO. A b = 2.4 / 11. E ax = OFDMA / 9.6 Gbps. F 802.11a (5 GHz, 54 Mbps) is the decoy.*
    - @2.3.freq
21. A site survey shows: ¶  AP-A  2.4 GHz ch 3 ¶  AP-B  2.4 GHz ch 6 ¶  AP-C  2.4 GHz ch 9 ¶Type the channels AP-A and AP-C should move to, in that order, separated by a space.
    - [=] 1 11 | 11 1
    - *3 overlaps both 1 and 6, and 9 overlaps 6 and 11. Move them to the standard plan: A = 1, B = 6, C = 11. Adjacent-channel interference is worse than sharing the same channel, because devices can't coordinate across partly overlapping channels.*
    - @2.3.chan
22. A 5 GHz AP log shows: ¶  radar detected on ch 52, switching to ch 36 ¶Users report a brief drop every afternoon. What's causing it?
    - **[x] DFS, part of 802.11h**  - [ ] TPC, part of 802.11h  - [ ] Band steering  - [ ] 802.11r fast roaming
    - *DFS (Dynamic Frequency Selection, part of 802.11h) = radar on a DFS channel (52-144) forces the AP off it. Fix: use non-DFS channels (36-48, 149-165) for sensitive users.*
    - @2.3.chan
23. Match each need to a band. Type the letters in order, e.g. abc. ¶  Most clean spectrum but shortest range, needs WPA3 · the middle ground, most common in business · longest range through walls ¶  A 6 GHz · B 2.4 GHz · C 5 GHz
    - [=] acb | a c b | a,c,b
    - *Cleanest spectrum with the shortest range, WPA3 required = A 6 GHz. The middle ground = C 5 GHz. Longest range = B 2.4 GHz.*
    - @2.3.freq

### Key facts
- **b 2.4 GHz 11 Mbps · a 5 GHz 54 · g 2.4 GHz 54 · n = Wi-Fi 4, both bands, 600 Mbps, MIMO · ac = Wi-Fi 5, 5 GHz only, about 6.9 Gbps, MU-MIMO · ax = Wi-Fi 6, 2.4 + 5, about 9.6 Gbps, OFDMA · 6E = ax + 6 GHz.**
- **2.4 = longest range, crowded, 3 non-overlapping channels (1, 6, 11) · 5 = middle, many channels · 6 = cleanest, shortest range, WPA3 required.**
- **Wider channels = more speed, fewer channels, more interference · band steering = push clients to 5/6.**
- **802.11h = DFS (radar + interference, auto-move channel) + TPC (power) · country code = regulator's legal channels and power.**
- **5G = low/mid/mmWave, 1-10 ms · GEO satellite about 600 ms, rain fade, expensive · LEO (Starlink) about 25-60 ms.**

## Test 14 - 2.3 Wireless Security (25 Q)

1. A visitor opens the Wi-Fi list on a phone and picks CoffeeShop-Guest. What is that label called?
   - **[x] SSID**  - [ ] BSSID  - [ ] BSS  - [ ] ESS
   - *The SSID is the human-readable network name, up to 32 characters, broadcast in beacons. The BSSID is the radio's MAC address.*
   - @2.3.ssid ~11.19
2. Why is hiding the SSID weak security?
   - **[x] The SSID still shows in probe and association frames**  - [ ] It turns off encryption on the network  - [ ] It forces clients back to WEP  - [ ] It stops clients roaming between APs
   - *A non-broadcast SSID only removes the name from beacons. Clients still ask for it by name, and tools like airodump-ng show it in seconds. It's obscurity, not security. Use WPA3 instead.*
   - @2.3.ssid ~27.21
3. Which describes how laptops connect in wireless infrastructure mode?
   - **[x] They associate with an access point that bridges them onto the wired network**  - [ ] They link straight to each other in a peer-to-peer group  - [ ] Access points pass traffic between themselves across many paths  - [ ] A pair of directional antennas joins two buildings
   - *Infrastructure mode is the usual AP-based BSS or ESS. Ad hoc is peer to peer without an AP, mesh has APs relaying for each other, and point-to-point links buildings.*
   - @2.3.type ~12.2
4. Which describe AD HOC wireless? (Select 2)
   - **[x] Devices connect directly, with no AP**  - **[x] Quick, temporary setup**  - [ ] Centrally managed by a controller  - [ ] Needs a RADIUS server
   - *Ad hoc (IBSS, Independent Basic Service Set) = peer to peer, no infrastructure. It's good for a quick file share but doesn't scale and has weak management. Wi-Fi Direct is the modern version.*
   - @2.3.type ~11.25
5. A festival site uses access points where only one is cabled and the rest pass traffic to each other, rerouting if one fails. What design is this?
   - **[x] Mesh network**  - [ ] Single AP covering all clients  - [ ] Point-to-point bridge  - [ ] Controller-only client association
   - *In a mesh only some nodes have a wired uplink and the others relay wirelessly (802.11s), finding a new path when a node drops. Common outdoors, at events and in large homes.*
   - @2.3.type ~11.24
6. Which describe point-to-point wireless? (Select 2)
   - **[x] A dedicated link between two sites**  - **[x] Uses directional antennas for long range**  - [ ] Broadcasts to all clients in range  - [ ] Always uses omnidirectional antennas
   - *Point-to-point = a wireless bridge between buildings, often with Yagi or dish antennas on line of sight. Point-to-multipoint = one hub site serving several remote sites.*
   - @2.3.type ~12.1
7. An auditor asks which Wi-Fi security standard you should deploy for the best protection today. Which is it?
   - [ ] WEP  - [ ] WPA  - [ ] WPA2  - **[x] WPA3**
   - *WPA3 adds SAE for Personal mode, which resists offline password guessing, and it is mandatory on 6 GHz. From weakest to strongest: WEP, WPA, WPA2, WPA3.*
   - @2.3.sec ~12.3
8. A legacy warehouse AP supports only WPA2. Which cipher protects its traffic?
   - **[x] AES-CCMP**  - [ ] RC4-TKIP  - [ ] GCMP-256  - [ ] SAE
   - *WPA2 encrypts with AES in CCMP mode. TKIP with RC4 belonged to original WPA and is deprecated. GCMP-256 appears with WPA3-Enterprise 192-bit mode, and SAE is a WPA3 handshake rather than a cipher.*
   - @2.3.sec ~27.9
9. Which should be disabled or avoided as security risks? (Select 3)
   - **[x] WEP**  - **[x] WPA with TKIP**  - **[x] WPS**  - [ ] WPA2 with AES  - [ ] WPA3
   - *WEP = cracked in minutes. WPA/TKIP = deprecated. WPS (Wi-Fi Protected Setup) = the 8-digit PIN is brute-forced in hours (Reaver). WPS lets devices join with a button press or PIN: convenient, but turn it off.*
   - @2.3.sec ~12.5,12.4
10. Which WPA2/WPA3 mode uses one shared password for everyone?
    - **[x] Personal, with a PSK**  - [ ] Enterprise, with 802.1X  - [ ] Open  - [ ] Captive portal
    - *PSK (Pre-Shared Key) = WPA2-Personal: one passphrase for authentication and key derivation. WPA3-Personal replaces PSK with SAE. Fine for a small office, but everyone shares the secret, and when someone leaves you change it everywhere.*
    - @2.3.sec ~12.7,12.8
11. A dental office with five staff wants the best Wi-Fi security but has no RADIUS server. What should it pick?
    - **[x] WPA3-Personal**  - [ ] WPA2-Enterprise  - [ ] WPA2-Personal  - [ ] Open with a captive portal
    - *Without RADIUS you are limited to Personal mode, and WPA3-Personal using SAE is stronger than WPA2-PSK. Enterprise mode requires an authentication server.*
    - @2.3.sec ~12.9
12. Which describe WPA2/WPA3 ENTERPRISE? (Select 2)
    - **[x] Each user authenticates with their own credentials through 802.1X and RADIUS**  - **[x] Uses EAP methods such as PEAP or EAP-TLS**  - [ ] Everyone shares one passphrase  - [ ] Needs no server
    - *Enterprise = 802.1X port-based authentication: the client (supplicant) talks to the AP (authenticator), which asks the RADIUS server. EAP (Extensible Authentication Protocol): PEAP (Protected EAP) = username and password inside TLS; EAP-TLS (Transport Layer Security) = certificates on both sides, the strongest. Per-user logins let you revoke one person.*
    - @2.3.sec ~12.10
13. A web page that blocks network access until a guest accepts terms or logs in is a:
    - **[x] Captive portal**  - [ ] Client isolation page  - [ ] RADIUS server  - [ ] Guest VLAN
    - *Captive portal = hotel and coffee-shop Wi-Fi: HTTP (Hypertext Transfer Protocol) traffic is redirected to a login or AUP (Acceptable Use Policy) page until you complete it. It's access control, NOT encryption: an open SSID with a portal is still unencrypted over the air.*
    - @2.3.sec ~12.6
14. At a hotel, one guest notices another guest's laptop share on the Wi-Fi. Which AP setting prevents wireless clients from talking to one another?
    - [ ] Hide the SSID  - [ ] MAC filtering  - **[x] Client isolation**  - [ ] Move to 2.4 GHz
    - *Client isolation makes the AP drop traffic between associated clients so they only reach the internet. Combine it with a guest VLAN and captive portal. MAC filters are easily spoofed.*
    - @2.3.sec ~28.19
15. An AP mounted in the middle of an open-plan floor must serve desks in every direction around it. Which antenna type suits this?
    - **[x] Omnidirectional**  - [ ] Yagi  - [ ] Parabolic dish  - [ ] Patch
    - *An omnidirectional antenna radiates in a doughnut shape all the way around, which is why most indoor APs use one, such as a dipole. Directional antennas aim the energy in one beam instead.*
    - @2.3.ant ~12.11
16. Standard antenna shape on most indoor APs?
    - **[x] Dipole**  - [ ] Yagi  - [ ] Parabolic dish  - [ ] Grid
    - *Dipole = the "rubber duck" stick antenna, omnidirectional. Place the AP high and central. Ceiling-mounted APs radiate down and out.*
    - @2.3.ant ~12.12
17. A school needs a wireless link to a gym 2 km away with clear line of sight. Which antenna types would concentrate the signal for that link? (Select 3)
    - **[x] Yagi**  - **[x] Parabolic dish**  - **[x] Grid, a parabolic type**  - [ ] Dipole  - [ ] Omnidirectional
    - *Directional antennas focus gain one way: Yagi, parabolic and grid dishes for long line-of-sight hops, and patch or panel for hallways. Gain is quoted in dBi.*
    - @2.3.ant ~12.13
18. A small shop has two standalone access points, each managed through its own web page. What applies to these APs? (Select 3)
    - **[x] Configured individually**  - **[x] Works without a controller**  - **[x] Handles its own security and management**  - [ ] Centrally managed by a WLC  - [ ] Needs a controller to work
    - *Standalone or fat APs carry their full configuration locally. That is fine for a couple of units but tedious at scale. Lightweight APs are the ones that depend on a WLC for configuration and management.*
    - @2.3.ap ~12.14
19. A university deploys 300 thin access points tied to a wireless LAN controller. Which characteristics apply? (Select 3)
    - **[x] Managed centrally by a WLAN controller**  - **[x] Configuration is pushed from the controller**  - **[x] Scale well for large deployments**  - [ ] Each one is configured individually  - [ ] They work fully on their own
    - *Thin APs rely on a WLC, on site or cloud hosted, for configuration, RF tuning, roaming and security, communicating over CAPWAP. Ideal for campuses.*
    - @2.3.ap ~12.15
20. A rogue AP on the corporate SSID copies the real name but has a different BSSID. What is it?
    - **[x] An evil twin**  - [ ] Band steering  - [ ] A mesh node  - [ ] A lightweight AP
    - *Evil twin = a spoofed AP that captures credentials. The WIPS (Wireless Intrusion Prevention System) or a scan reveals it by BSSID. 802.1X with certificate validation stops clients trusting it. The attack itself is in 4.2.*
    - @2.3.ssid
21. Match the term to each description. Type the letters in order, e.g. abcde. ¶  One AP and its clients · the AP radio's MAC · many APs sharing one name · the network name · the shared name of those many APs ¶  A SSID · B BSSID · C ESSID · D BSS · E ESS
    - [=] dbeac | d b e a c | d,b,e,a,c
    - *D BSS = one cell. B BSSID = its MAC. E ESS = the multi-AP set. A SSID = the name. C ESSID = the SSID of an ESS.*
    - @2.3.ssid
22. Match each to its network type. Type the letters in order, e.g. abcd. ¶  Laptops share files with no AP · office Wi-Fi through ceiling APs · two buildings linked by dishes · outdoor nodes relaying for each other ¶  A infrastructure · B mesh · C point-to-point · D ad hoc
    - [=] dacb | d a c b | d,a,c,b
    - *No AP = D ad hoc. Through APs = A infrastructure. Dishes between two sites = C point-to-point. Nodes relaying = B mesh.*
    - @2.3.type
23. Match each site to its security setup. Type the letters in order, e.g. abc. ¶  A 400-staff company with RADIUS and per-user logins · a 5-person office with no server · café guests accepting terms ¶  A WPA3-Personal · B WEP · C captive portal · D WPA3-Enterprise
    - [=] dac | d a c | d,a,c
    - *RADIUS and per-user = D Enterprise (802.1X). No server = A Personal (SAE). Guests accepting terms = C captive portal, with client isolation on a guest VLAN. WEP is never the answer.*
    - @2.3.sec
24. An audit shows: ¶  SSID  Corp    WPA2-TKIP   WPS on ¶  SSID  Guest   Open        isolation off ¶Which THREE changes fix it? (Select 3)
    - **[x] Corp: move from TKIP to WPA3, or at least WPA2-AES**  - **[x] Corp: disable WPS**  - **[x] Guest: enable client isolation**  - [ ] Guest: hide the SSID  - [ ] Corp: enable MAC filtering instead
    - *Corp: drop TKIP for WPA3 (or at least WPA2-AES) and turn WPS off (its PIN can be brute-forced). Guest: client isolation so guests can't attack each other, ideally plus a portal and a separate VLAN. Hiding the SSID and MAC filtering are both trivially bypassed.*
    - @2.3.sec
25. Match each job to an antenna. Type the letters in order, e.g. abcd. ¶  Open-plan office ceiling · a 5 km link between towers · 800 m to the next building down a street · coverage down one long corridor from a wall ¶  A Yagi · B patch · C omnidirectional · D parabolic dish
    - [=] cdab | c d a b | c,d,a,b
    - *All-around = C omni. Longest point-to-point = D parabolic dish. Medium-range directional = A Yagi. Flat wall-mount beam = B patch/panel.*
    - @2.3.ant

### Key facts
- **SSID = the name · BSS = one AP + clients · BSSID = AP radio MAC · ESS = many APs, one SSID (ESSID) = roaming · IBSS = ad hoc. Hidden SSID = not security.**
- **Types: infrastructure (via AP) · ad hoc (no AP) · mesh (nodes relay, 802.11s) · point-to-point (bridge, directional).**
- **WEP < WPA/TKIP < WPA2/AES-CCMP < WPA3/SAE (6 GHz needs it). Kill WPS. Personal = PSK/SAE, one secret · Enterprise = 802.1X + RADIUS + EAP (PEAP, EAP-TLS).**
- **Captive portal = login page, not encryption · client isolation = guests can't see each other.**
- **Omni/dipole = 360 · directional = Yagi, dish/parabolic, grid, patch.**
- **Autonomous = standalone, configured one by one · lightweight = controller-managed (WLC, CAPWAP).**

## Test 15 - 2.4 Physical Install (28 Q)

1. The ISP's fibre enters a building and lands in the room holding the core switches, which feed every floor. What is that room called?
   - **[x] MDF**  - [ ] IDF  - [ ] DSU  - [ ] DCE
   - *MDF (Main Distribution Frame) = the demarc side: ISP (Internet Service Provider) handoff, core switches, often the server room. IDFs (Intermediate Distribution Frames) branch off it. DSU = Data Service Unit, DCE = Data Circuit-terminating Equipment. Hook: MDF = Main, IDF = In-between floors.*
   - @2.4.loc ~12.17
2. Each floor has a small closet with an access switch for that floor's desks, uplinked to the main room. What is the closet called?
   - **[x] IDF**  - [ ] PDU  - [ ] DCI  - [ ] DTE
   - *IDF (Intermediate Distribution Frame) = one per floor or wing: access switches and patch panels, fibre uplink to the MDF. Keeps copper runs under 100 m. PDU = Power Distribution Unit, DTE = Data Terminal Equipment.*
   - @2.4.loc ~12.16
3. How tall is one rack unit, 1U?
   - [ ] 1 inch  - **[x] 1.75 inches**  - [ ] 2 inches  - [ ] 19 inches
   - *1U = 1.75 inches (44.45 mm). 19 inches = the rack's WIDTH, a classic trap. Switches are usually 1U, servers 1-4U.*
   - @2.4.loc ~12.18
4. Size of a standard full-height rack?
   - [ ] 24U  - [ ] 36U  - **[x] 42U**  - [ ] 48U
   - *42U × 1.75 = 73.5 inches of mounting space. Racks come in 2-post (open, for patch panels and switches) and 4-post (for deep servers), and in widths such as 19 inches.*
   - @2.4.loc
5. In a top-of-rack design, where is the access switch?
   - **[x] In every rack, uplinking to the aggregation layer**  - [ ] One per row, at the end of the row  - [ ] Only in the MDF  - [ ] In the IDF on another floor
   - *ToR (Top of Rack) = each rack has its own switch: short cables, more switches. EoR (End of Row) = one bigger switch per row with longer horizontal runs. Both then uplink to the aggregation/spine layer.*
   - @2.4.loc ~24.21
6. Server fans pull air in at the front and push hot air out at the back. Design that keeps this efficient?
   - **[x] Hot aisle / cold aisle, fronts facing each other**  - [ ] All racks facing the same way, front to back  - [ ] Racks back to front in one long line  - [ ] Perforated floor tiles under the hot aisle
   - *Hot/cold aisle: fronts (intakes) face the cold aisle, which has perforated floor tiles. Backs (exhausts) face the hot aisle, where the returns are. Containment (doors or roofs) stops the two mixing. Hook: face to face, back to back.*
   - @2.4.loc
7. In one rack, a switch with port-side intake is mounted next to servers whose fronts face the cold aisle, but the switch's ports face the hot aisle. What happens?
   - **[x] The switch pulls in hot-aisle air and runs hot**  - [ ] Nothing, airflow direction doesn't matter  - [ ] The servers overheat instead  - [ ] The switch's PoE budget drops to zero
   - *Port-side intake means air enters on the port side. With the ports facing the HOT aisle, the switch breathes exhaust air. Fix: order port-side EXHAUST for ports-at-the-back, or turn the switch around. Match every device's airflow to the hot/cold aisle layout.*
   - @2.4.loc ~12.19
8. A switch is mounted at the FRONT of a rack, its ports facing the cold aisle. Which airflow model must it have?
   - [ ] Port-side exhaust  - **[x] Port-side intake**  - [ ] Front-to-back vertical  - [ ] Cold-aisle containment
   - *Port-side intake = air comes IN on the port side. Mixing intake types in one rack blows hot air into a neighbour's intake.*
   - @2.4.loc ~12.20
9. Passive device where horizontal copper runs terminate so short patch leads can connect to switches?
   - **[x] Patch panel**  - [ ] Hub  - [ ] Cable splitter  - [ ] Media converter
   - *Patch panel = punch-down (110 blocks) on the back, RJ45 (Registered Jack 45) on the front. It protects the permanent run, so you only swap patch cables. Label both ends.*
   - @2.4.loc ~12.21
10. A fibre distribution panel does what?
    - **[x] Terminates, splices and manages fibre runs**  - [ ] Connects LAN devices together  - [ ] Converts fibre to copper  - [ ] Amplifies the optical signal
    - *FDP (Fibre Distribution Panel) = the fibre version of a patch panel, with splice trays and LC/SC (Lucent / Subscriber Connector) adapters. Media converters and transceivers handle fibre to copper.*
    - @2.4.loc ~12.22
11. A colocation rack is shared with another tenant's staff walking past. Which is a PHYSICAL control for your gear?
    - **[x] Lockable rack doors or panels**  - [ ] Access control policies  - [ ] Remote monitoring  - [ ] Asset tracking
    - *Physical = a real barrier: rack locks, cages, locked closets, badge readers. Policies = administrative controls. Monitoring = detective.*
    - @2.4.loc ~12.23
12. Device giving battery power during an outage, long enough to shut down or for a generator to start?
    - **[x] UPS**  - [ ] PDU  - [ ] PSU  - [ ] RPS
    - *UPS (Uninterruptible Power Supply) = battery backup, runs for minutes. Types: standby/offline, line-interactive (with AVR, Automatic Voltage Regulation), online/double-conversion (always on battery, cleanest power). Generator = hours or days. PSU (Power Supply Unit) = the power supply inside a device.*
    - @2.4.pwr ~12.24
13. Rack device that distributes power to many outlets, often metering and switching them remotely?
    - [ ] PSU  - [ ] RPS  - **[x] PDU**  - [ ] UPS
    - *PDU (Power Distribution Unit) = the rack's managed power strip: per-outlet metering, remote power cycling, and A and B feeds for dual-PSU servers. RPS (Redundant Power Supply) = a backup supply for a device.*
    - @2.4.pwr ~12.25
14. The whole building goes dark for 20 minutes after a storm. What type of power event is this?
    - **[x] Blackout**  - [ ] Brownout  - [ ] Sag  - [ ] Surge
    - *Blackout = no power at all. Brownout = voltage sag, lights dimming. Surge/spike = too much voltage. UPS covers blackouts; AVR covers brownouts; surge protectors cover spikes.*
    - @2.4.pwr ~13.1
15. Lights dim and servers reboot when the building's air conditioning starts up. What is the likely power event?
    - **[x] A brownout**  - [ ] A blackout  - [ ] A surge  - [ ] An ESD event
    - *Brownout = sag or undervoltage, often during heavy load. It damages power supplies over time. A line-interactive UPS with AVR boosts it back. ESD = Electrostatic Discharge.*
    - @2.4.pwr ~13.2
16. A new switch will sit at the back of a rack with its ports facing the hot aisle, like the servers' rear panels. Which airflow model should it be ordered with?
    - **[x] Port-side exhaust**  - [ ] Port-side intake  - [ ] Either, direction doesn't matter  - [ ] Side-to-side only
    - *Match the switch to the aisle layout. Ports face the hot aisle, so the port side must EXHAUST hot air. Port-side intake would suck in hot aisle air and overheat the switch. Many switches ship with reversible fans or PSUs, so order the right direction.*
    - @2.4.loc ~13.3
17. A rack circuit is rated at 20 A. Following the 80% rule, type the most current, in amps, the equipment on it should draw continuously.
    - [=] 16 | 16a | 16 a
    - *80% of 20 A = 16 A. Planning to that limit leaves headroom for startup surges, so the breaker doesn't trip and drop every device on the circuit. Dual-PSU servers go on separate A and B circuits.*
    - @2.4.pwr ~13.4
18. Why do data centres care about POWER LOAD and plan per-circuit amperage?
    - **[x] Overloading a circuit trips the breaker and drops everything on it**  - [ ] Power draw sets which Wi-Fi channels the APs can use  - [ ] Higher load on a circuit lowers the MTU on its switches  - [ ] It only matters for sizing the UPS batteries
    - *Power load = the total watts/amps drawn. Plan with headroom: keep to about 80% of a breaker's rating. Dual-PSU servers go on separate circuits (A and B feeds) so one tripped breaker doesn't take them down.*
    - @2.4.pwr
19. Which does HVAC control in a server room? (Select 3)
    - **[x] Temperature**  - **[x] Humidity**  - **[x] Air quality**  - [ ] Power load  - [ ] Fire suppression
    - *HVAC (Heating, Ventilation and Air Conditioning). ASHRAE guidance: about 18-27 °C (64-80 °F) at the intake. Too hot = throttling and failure.*
    - @2.4.env ~13.5
20. Why must server-room humidity stay in range?
    - **[x] Too low causes static; too high causes condensation**  - [ ] Too low slows the fans; too high speeds them up  - [ ] High humidity cools the equipment better  - [ ] It only affects Wi-Fi range, not hardware
    - *Low humidity = ESD (Electrostatic Discharge) risk. High = condensation. The typical target is about 40-60% relative humidity.*
    - @2.4.env
21. A facilities manager is choosing suppression for a new server room. Which two should be avoided because they damage electronics? (Select 2)
    - **[x] Water sprinklers**  - **[x] Foam**  - [ ] Clean agent  - [ ] Inert gas
    - *Water and foam leave residue, short circuits and corrosion. Clean agents such as FM-200 or Novec 1230 and inert gases like argon put fires out without residue. Where sprinklers are mandated, pre-action or dry-pipe designs only fill when fire is detected.*
    - @2.4.env ~13.6
22. Why do many server rooms use a PRE-ACTION sprinkler system if water is required?
    - **[x] The pipes stay dry until a detector triggers**  - [ ] It sprays foam instead of water  - [ ] It uses a gas, with no water at all  - [ ] It's the cheapest system to install
    - *Pre-action = two triggers are needed: detection fills the pipes, then heat opens a head. It avoids accidental discharge. Wet-pipe = always full, which is risky over racks.*
    - @2.4.env
23. Match MDF or IDF to each item. Type the letters in order, e.g. aaaa. ¶  Access switches for floor 3 · the ISP handoff and core switch · floor 2's patch panels · the building's demarc ¶  A MDF · B IDF
    - [=] baba | b a b a | b,a,b,a
    - *Floor access switches = IDF. ISP handoff and core = MDF. Floor patch panels = IDF. Demarc = MDF. IDFs uplink by fibre back to the MDF.*
    - @2.4.loc
24. A 42U rack holds a 2U UPS, four 1U switches, a 1U patch panel and three 4U servers. Type how many U are left free, as a number.
    - [=] 23 | 23u
    - *2 + 4×1 + 1 + 3×4 = 2 + 4 + 1 + 12 = 19U used. 42 - 19 = 23U free. Heavy gear like the UPS and servers goes at the bottom.*
    - @2.4.loc
25. Match each power problem to its protection. Type the letters in order, e.g. abcd. ¶  A lightning spike · a 6-hour outage · a 5-minute outage · a sustained sag in voltage ¶  A UPS · B AVR · C surge protector · D generator
    - [=] cdab | c d a b | c,d,a,b
    - *Spike = C surge protector. Long outage = D generator, with the UPS covering the gap until it starts. Short outage = A UPS battery. Sag/brownout = B AVR (Automatic Voltage Regulation, in a line-interactive UPS).*
    - @2.4.pwr
26. A monitoring panel shows: ¶  Rack 7  intake 34 °C  humidity 18% ¶Which TWO problems does it show? (Select 2)
    - **[x] Intake temperature too high**  - **[x] Humidity too low**  - [ ] Humidity too high  - [ ] Intake temperature too low
    - *34 °C intake is above the roughly 27 °C maximum. 18% humidity is below about 40%, so there's ESD risk. Check the hot/cold aisle layout, blanking panels and the HVAC.*
    - @2.4.env
27. Match each room to its fire suppression. Type the letters in order, e.g. abc. ¶  The office hallway · a records room where the code requires sprinklers but water damage must be avoided · the server room ¶  A pre-action sprinkler · B foam · C clean agent · D wet-pipe sprinkler
    - [=] dac | d a c | d,a,c
    - *Offices = D ordinary wet-pipe sprinklers. Sprinklers required but water-sensitive = A pre-action. Servers = C clean agent (FM-200/Novec), no residue. Foam is never used on IT gear.*
    - @2.4.env
28. PBQ: Fitting out a comms rack. ¶  PoE switch budget 370 W. Planned devices: 12 phones at 6 W, 6 APs at 25 W, 4 cameras at 12 W. ¶  Circuit rated 30 A.
    - [p] Type the total PoE draw in watts = 270 | 270 w | 270w
    - [p] Type the PoE headroom left on the switch in watts = 100 | 100 w | 100w
    - [p] Which PoE standard must the switch support for the 25 W APs :: A 802.3af · B 802.3at, PoE+ · C passive 24 V · D 802.3ab = b
    - [p] The circuit is rated 30 A. Type its max continuous load in amps by the 80% rule (amps only, voltage not needed) = 24 | 24 a | 24a
    - *12 × 6 = 72, 6 × 25 = 150, 4 × 12 = 48, total 270 W, leaving 370 - 270 = 100 W. Each standard has a figure at the switch port (PSE) and a lower one at the device (PD) after cable loss: 802.3af 15.4 / 12.95 W, 802.3at PoE+ 30 / 25.5 W, 802.3bt 60-100 / 51-71 W. So 25 W APs need PoE+, and the 12 W cameras fit af. 802.3ab is 1000BASE-T, not PoE. 80% of 30 A = 24 A continuous. A generator takes seconds to start, and the UPS bridges the gap.*
    - @2.4.pwr

### Key facts
- **MDF = main, demarc, core · IDF = floor closets · ToR = switch per rack · EoR = switch per row. 1U = 1.75 inches · full rack 42U.**
- **Hot/cold aisle: intakes face intakes · port-side intake vs exhaust must match the rack · blanking panels stop recirculation.**
- **Patch panel = copper termination · fibre distribution panel = fibre · lockable racks = physical security.**
- **UPS = battery, minutes (standby, line-interactive + AVR, online) · generator = hours · PDU = rack power strip, metered · keep circuits under 80%, A and B feeds.**
- **Blackout = none · brownout = sag · surge = spike. US 110-120 V · Europe 220-240 V.**
- **HVAC: about 18-27 °C, 40-60% humidity. Fire: clean agent/inert gas best · water and foam worst · pre-action if sprinklers are required.**

## Test 16 - 3.1 Docs + Lifecycle (36 Q)

1. Which is true of physical versus logical diagrams?
   - **[x] Physical shows hardware and cabling; logical shows subnets and flow**  - [ ] Physical shows IP addresses; logical shows the cable runs  - [ ] They show the same thing at different zoom levels  - [ ] Logical shows rack positions; physical shows VLANs
   - *Physical diagram = what's plugged into what: devices, ports, cable runs. Logical diagram = how data flows: IP (Internet Protocol) subnets, VLANs (Virtual Local Area Networks), routing, trust zones. Hook: physical = where you'd trip over it, logical = where the packets go.*
   - @3.1.doc ~13.7
2. Best document for finding exactly where a server sits in the data centre?
   - [ ] Logical diagram  - [ ] Layer 3 diagram  - **[x] Rack diagram**  - [ ] Cable map
   - *Rack diagram = which rack and which U (rack unit, 1.75 inches) slot holds each device, front and back. A cable map traces connections, and a logical diagram doesn't show physical placement.*
   - @3.1.doc ~13.8
3. Documentation showing the physical path of every cable, port to port?
   - **[x] Cable maps and diagrams**  - [ ] Network design blueprints  - [ ] Logical diagram  - [ ] IPAM
   - *Cable map = each run from patch panel port to wall jack to switch port. Paired with consistent labelling at both ends, it makes tracing a fault quick. IPAM = IP Address Management.*
   - @3.1.doc ~13.9
4. Type the OSI layer number of a diagram that shows cabling and hardware.
   - [=] 1 | layer 1 | l1
   - *Layer 1 (physical) diagram = cables, patch panels, transceivers, devices. Diagrams are named after the OSI (Open Systems Interconnection) layer they show.*
   - @3.1.doc ~13.10
5. An audit finds 120 installs of a network monitoring tool, but only 100 licences. Which part of asset inventory should have caught this?
   - **[x] Software licensing tracking**  - [ ] Warranty tracking  - [ ] IPAM  - [ ] The SLA
   - *Asset inventory covers hardware, software, licensing and warranty. Tracking licences against installs prevents compliance fines and surprise true-up bills. Warranty = hardware repair and replace cover. IPAM = IP Address Management. SLA = Service Level Agreement with a provider.*
   - @3.1.doc ~13.11
6. Type the OSI layer number of a diagram showing IP addressing, routing and subnets.
   - [=] 3 | layer 3 | l3
   - *Layer 3 (network) diagram = subnets, gateways, routing protocols and areas. Hook: 1 = wires, 2 = switches, 3 = routers.*
   - @3.1.doc ~13.12
7. What does an asset inventory track?
   - **[x] Hardware, software, licences and warranties**  - [ ] Switch configurations and backup schedules  - [ ] IP addresses and DHCP reservations  - [ ] User accounts, passwords and group memberships
   - *Asset inventory = every device and application with its owner, location, serial number, licence, warranty and end-of-life date. It drives budgeting, patching, compliance and lifecycle planning.*
   - @3.1.doc ~13.13
8. Which can be used to tag and track hardware assets?
   - [ ] Barcode labels  - [ ] QR codes  - [ ] RFID tags  - **[x] All of the above**
   - *All of them work: barcodes and QR (Quick Response) codes are cheap and need line of sight, RFID (Radio-Frequency Identification) can be read at a distance in bulk, and GPS (Global Positioning System) tracks mobile or vehicle assets.*
   - @3.1.doc ~13.14
9. Which tags can be read wirelessly at a distance, without line of sight, to track assets?
   - [ ] Barcode  - [ ] QR code  - **[x] RFID**  - [ ] NFC
   - *RFID (Radio-Frequency Identification) = passive or active tags scanned without line of sight, used for assets and badges. NFC (Near-Field Communication) = a very short-range tap of a few cm. Barcodes and QR codes need line of sight.*
   - @3.1.doc ~13.15
10. Tools and processes that plan, track and manage IP addresses are called:
    - **[x] IPAM**  - [ ] IAM  - [ ] DHCP  - [ ] SIEM
    - *IPAM (IP Address Management) = tracks subnets, assignments, DHCP (Dynamic Host Configuration Protocol) scopes and DNS (Domain Name System) records together, so you avoid conflicts and can see how full each subnet is. IAM (Identity and Access Management) is a different thing.*
    - @3.1.doc ~13.16
11. Which agreement defines a service's availability, quality and scope, like 99.9% uptime?
    - **[x] SLA**  - [ ] MOU  - [ ] NDA  - [ ] AUP
    - *SLA (Service Level Agreement) = the measurable promises: uptime, response time, repair time, and the penalties if they're missed. MOU (Memorandum of Understanding) = a non-binding intent. NDA (Non-Disclosure Agreement) = keep secrets.*
    - @3.1.doc ~13.17,13.18
12. During onboarding, a hire asks HR whether streaming games on the company notebook over lunch is allowed. Which signed policy settles it?
    - [ ] Service level agreement  - **[x] Acceptable use policy**  - [ ] Non-disclosure agreement  - [ ] Memorandum of understanding
    - *AUP (Acceptable Use Policy) = the rules for how staff may use company devices, accounts and connectivity, normally acknowledged when they start. An NDA protects confidential information, an SLA covers provider performance, and an MOU is an informal agreement between parties.*
    - @3.1.doc ~27.1
13. Before swapping cells in the server room battery cabinet, a technician wants the manufacturer's PPE, spill and fire guidance for the electrolyte. What should they pull up?
    - [ ] Acceptable use policy  - **[x] Safety data sheet**  - [ ] Standard operating procedure  - [ ] Physical network diagram
    - *SDS (Safety Data Sheet, once called MSDS) = the maker's hazard sheet for a substance: handling, protective gear, first aid, firefighting and disposal. An SOP describes how to do a task, not the chemical hazards.*
    - @3.1.doc ~27.2
14. Assessing a building's layout and interference to plan AP placement is called:
    - **[x] A wireless site survey**  - [ ] A baseline  - [ ] A cable map  - [ ] A penetration test
    - *Site survey = walk the site measuring RF (radio frequency): coverage, interference, obstacles and channel use, before and after install. Predictive survey = modelled from floor plans. Passive survey = just listening.*
    - @3.1.doc ~13.19
15. Tool output showing coloured areas of weak and strong Wi-Fi signal on a floor plan?
    - **[x] Heat map**  - [ ] Rack diagram  - [ ] Syslog  - [ ] Baseline
    - *Heat map = the site survey result: red and green zones of signal strength (RSSI, Received Signal Strength Indicator, in dBm). Weak spots tell you where to add or move an AP (Access Point).*
    - @3.1.doc ~13.20
16. Lifecycle phase where a product is no longer made or sold, though it may still get support?
    - **[x] End of life**  - [ ] End of support  - [ ] General availability  - [ ] Decommissioning
    - *EOL (End of Life) = the vendor stops selling it. EOS (End of Support) = no more patches or fixes: running it is now a security risk. Plan replacement between EOL and EOS.*
    - @3.1.life ~13.21
17. A vendor announces that a firewall model your branches run has reached end of support. Which consequences apply? (Select 3)
    - **[x] Newly found vulnerabilities will not be patched**  - **[x] The vendor will no longer take support cases for it**  - **[x] Keeping it in production creates security and audit exposure**  - [ ] Monthly feature releases will continue for a year  - [ ] It qualifies for free hardware replacement under warranty
    - *Once support ends, flaws stay open and no one at the vendor will help you. Auditors treat unsupported gear as a finding. Plan a replacement, or segment it and add compensating controls until you can.*
    - @3.1.life ~13.22
18. Software embedded in a hardware chip, updated by flashing, is called:
    - [ ] Middleware  - **[x] Firmware**  - [ ] A driver  - [ ] A hypervisor
    - *Firmware = code in the device's flash or ROM (Read-Only Memory): router OS images, BIOS/UEFI (Unified Extensible Firmware Interface), NIC (Network Interface Card) firmware. Updating it fixes bugs and vulnerabilities, but it goes through change management.*
    - @3.1.life ~13.23
19. Which are part of good software management? (Select 3)
    - **[x] Tracking versions and licences**  - **[x] Testing and scheduling patches and upgrades**  - **[x] Planning for vendor end of support**  - [ ] Installing every update the moment it's released, on production  - [ ] Letting each user choose versions
    - *Software management = inventory, licence compliance, patch and upgrade process (test, approve, deploy, verify) and lifecycle planning. Untested patches straight to production cause outages.*
    - @3.1.life ~13.24
20. Formally retiring a device, wiping its data and disposing of it is called:
    - [ ] End of life  - [ ] End of support  - **[x] Decommissioning**  - [ ] Provisioning
    - *Decommissioning = remove it from service, update the inventory and docs, wipe or destroy its data (sanitisation), and recycle it properly. Forgetting to wipe old gear = a data breach.*
    - @3.1.life ~13.25
21. A fixed, approved reference configuration you compare devices against to spot drift is the:
    - **[x] Baseline configuration**  - [ ] Running configuration  - [ ] Startup configuration  - [ ] Performance baseline
    - *Baseline configuration = the known-good settings you compare against to spot drift or unauthorised change. A performance baseline (in 3.2) = normal traffic and usage levels.*
    - @3.1.cfg ~14.1
22. An optimised, pre-approved template used to build every new switch or server is the:
    - [ ] Baseline configuration  - **[x] Golden configuration**  - [ ] Startup configuration  - [ ] Backup configuration
    - *Golden configuration / golden image = the standard template: build every switch or server from it for consistency. A baseline = the minimum approved settings to measure against.*
    - @3.1.cfg ~14.2
23. An engineer adds a new VLAN on a Cisco switch, then the switch loses power before anyone types write memory. Which configuration held the change and is now gone?
    - **[x] Running configuration**  - [ ] Startup configuration  - [ ] Golden configuration  - [ ] Archived configuration
    - *The running-config lives in volatile RAM and is what the device is using right now. The startup-config sits in NVRAM and loads at boot. Save with copy running-config startup-config so changes survive a reload.*
    - @3.1.cfg ~24.5
24. Your team stores versioned switch configs and compares them nightly against an approved baseline. Which goals does this configuration management practice serve? (Select 2)
    - **[x] Keeping device settings uniform and documented**  - **[x] Spotting unauthorised or accidental drift so it can be reverted**  - [ ] Removing the need for change approval  - [ ] Boosting wireless signal strength
    - *Configuration management tracks what each device should look like: baselines, version history, drift alerts and quick restores. Change management is the separate approval process that happens before a change. They complement each other.*
    - @3.1.cfg ~24.6
25. A network admin wants to move the core router to a new firmware train under the formal change process. What does the admin do first?
    - **[x] Raise a change request**  - [ ] Apply the upgrade in production  - [ ] Schedule a post-change review  - [ ] Close the related incident
    - *Typical flow: raise the request with scope, reason, risk and impact, get it reviewed and approved by the CAB, book a maintenance window, implement with a backout plan ready, validate, then document and close.*
    - @3.1.chg ~24.1
26. The scheduled low-usage period set aside for approved changes is the:
    - **[x] Maintenance window**  - [ ] Change freeze  - [ ] Rollback window  - [ ] Service window SLA
    - *Maintenance window = e.g. Sunday 02:00-04:00, agreed with the business, so any outage hurts the fewest people. Emergency changes can bypass it, but still get documented afterwards.*
    - @3.1.chg ~24.2
27. After last night's approved ACL update, payroll cannot reach its database. Which section of the change record lets the team restore service quickest?
    - **[x] The rollback / backout plan**  - [ ] The business justification  - [ ] The approval signature  - [ ] The risk score
    - *The backout plan is the prepared set of steps, plus a saved copy of the prior config, to undo the change. It must exist before the change is approved, so recovery does not depend on improvising during an outage.*
    - @3.1.chg ~24.3
28. Which group reviews and approves proposed changes?
    - [ ] SOC  - **[x] CAB**  - [ ] NOC  - [ ] CIRT
    - *CAB (Change Advisory Board) = IT, security and business representatives who weigh risk and impact and approve, reject or reschedule each change. SOC = Security Operations Centre, NOC = Network Operations Centre, CIRT = Computer Incident Response Team.*
    - @3.1.chg ~24.4
29. At 10 a.m. on a weekday, a junior admin starts flashing new code onto an access switch, saying there's no need for a ticket because it is quick. What is the key issue?
    - **[x] It skips the change management process**  - [ ] Switch firmware must never be upgraded  - [ ] Only the vendor is allowed to upgrade firmware  - [ ] The switch must first be moved to a guest VLAN
    - *Small changes still need a request, approval, a scheduled window, a backout plan and documentation. Unplanned daytime work is a classic cause of outages.*
    - @3.1.chg ~24.20
30. After a fix is applied, where do you record what was done and why?
    - **[x] The change record and documentation**  - [ ] Nowhere, it works now  - [ ] The DHCP scope notes  - [ ] The switch login banner
    - *The last troubleshooting step = document findings, actions and outcomes. Update the change ticket, diagrams and config backups so the next person isn't guessing.*
    - @3.1.chg ~28.16
31. Match each need to a document. Type the letters in order, e.g. abcde. ¶  Which U slot holds SRV-04 · which switch port wall jack 3-17 lands on · which subnet and gateway VLAN 40 uses, and what routes to it · the trunk and STP layout between switches · which addresses are still free in 10.8.0.0/22 ¶  A IPAM · B Layer 2 diagram · C cable map · D rack diagram · E Layer 3 diagram
    - [=] dceba | d c e b a | d,c,e,b,a
    - *U slot = rack diagram. Jack to switch port = cable map. Subnets, gateways and routes = Layer 3 diagram. Trunks and STP = Layer 2 diagram. Free addresses = IPAM (IP Address Management).*
    - @3.1.doc
32. Put the change-management steps in order. Type the letters, e.g. abcdef. ¶  A implement · B request · C document · D approve · E schedule · F verify
    - [=] bdeafc | b d e a f c | b,d,e,a,f,c
    - *Request → CAB approval → schedule in the maintenance window → implement, with a rollback ready → verify it worked → document and close.*
    - @3.1.chg
33. Match each to its agreement or document. Type the letters in order, e.g. abcde. ¶  An ISP promises 99.95% uptime with credits · staff may not use work email for personal business · a contractor must keep the client's designs secret · two departments informally agree to share a lab · the hazards of a UPS battery electrolyte ¶  A MOU · B SDS · C SLA · D NDA · E AUP
    - [=] cedab | c e d a b | c,e,d,a,b
    - *C SLA = measurable service promise. E AUP = user rules. D NDA = confidentiality. A MOU = a non-binding understanding. B SDS = chemical safety.*
    - @3.1.doc
34. Put the hardware lifecycle stages in order. Type the letters, e.g. abcdef. ¶  A decommission · B procure · C EOS · D deploy · E EOL · F maintain
    - [=] bdfeca | b d f e c a | b,d,f,e,c,a
    - *Buy it → deploy → maintain and patch → the vendor stops selling it (EOL, End of Life) → the vendor stops patching it (EOS, End of Support) → decommission, sanitise and dispose.*
    - @3.1.life
35. After an overnight change, a switch comes back up with last week's config. Type the IOS command the tech forgot, in full.
    - [=] copy running-config startup-config | copy run start | write memory | wr | write | wr mem | wri
    - *The change lived only in running-config (RAM). On reboot the device loaded startup-config (NVRAM). Save after every verified change, and keep a versioned backup under configuration management.*
    - @3.1.cfg
36. PBQ: Order a standard change to replace a core switch. ¶  A implement during the maintenance window · B submit the change request with a rollback plan · C CAB approves · D test in the lab and assess the risk · E verify, then update the documentation · F schedule the window and notify users · G close the request
    - [p] Type all 7 letters in order, first step first, e.g. gfedcba = bdcfaeg | b d c f a e g | b,d,c,f,a,e,g
    - [p] The upgrade fails at 2 am. Next step :: A execute the rollback plan · B extend the window and keep going until it works · C escalate to the vendor and wait · D bring forward tomorrow's change to fix it = a
    - *Request, with rollback, then test and assess the risk, then CAB approval, then schedule and notify, then implement, then verify and document, then close. A failed change inside the window = roll back and try again later, which is what the rollback plan is for.*
    - @3.1.chg

### Key facts
- **Physical = cables and devices · logical = subnets, VLANs, flows. Rack diagram = U position · cable map = port to port. L1 cabling · L2 switches/VLANs/STP · L3 IP/routing.**
- **Asset inventory (barcode, QR, RFID, GPS) · IPAM = IP address management · site survey + heat map = Wi-Fi placement.**
- **SLA = measurable promises · AUP = user rules · NDA = secrecy · MOU = non-binding · SDS = chemical hazards · SOP = step-by-step how-to.**
- **Lifecycle: procure, deploy, maintain, EOL (no longer sold), EOS (no patches), decommission (wipe, dispose). Firmware = code on the chip.**
- **Baseline config = the approved reference · golden config = the standard template · running-config in RAM vs startup-config in NVRAM: copy run start.**
- **Change management: request, CAB approval, maintenance window, implement with a rollback plan, verify, document.**

## Test 17 - 3.2 Monitoring (27 Q)

1. Type the UDP port an SNMP agent listens on for GET and SET requests.
   - [=] 161 | udp 161 | udp/161
   - *SNMP (Simple Network Management Protocol): the manager polls agents on UDP (User Datagram Protocol) 161. Hook: poll on 161, trap on 162, "one to ask, two to shout".*
   - @3.2.snmp ~14.3
2. Type the UDP port an SNMP manager receives TRAPS on.
   - [=] 162 | udp 162 | udp/162
   - *Trap = an unsolicited alert from the agent to the manager, on UDP 162 (a link going down, a fan failing). Polling = the manager asks on 161. An inform = a trap that is acknowledged.*
   - @3.2.snmp
3. The device's database of objects an SNMP manager queries, like interface counters, is the:
   - **[x] MIB**  - [ ] OID  - [ ] Community string  - [ ] Trap
   - *MIB (Management Information Base) = the tree of values, each with an OID (Object Identifier) such as 1.3.6.1.2.1.2.2.1.10 for interface input octets. Vendors publish MIB files so the manager can decode them.*
   - @3.2.snmp ~14.4
4. The dotted numeric address of ONE value in the MIB tree is an:
   - [ ] MIB  - **[x] OID**  - [ ] ASN  - [ ] SID
   - *OID (Object Identifier) = dotted numbers like 1.3.6.1.2.1.1.5.0 (the sysName). An snmpget or snmpwalk asks for OIDs.*
   - @3.2.snmp
5. Which SNMP version supports ENCRYPTION and per-user authentication?
   - [ ] SNMPv1  - [ ] SNMPv2c  - **[x] SNMPv3**  - [ ] SNMPv4
   - *SNMPv3 = USM (User-based Security Model): authNoPriv / authPriv, SHA (Secure Hash Algorithm) for integrity and AES (Advanced Encryption Standard) for privacy. v1 and v2c = cleartext. There is no v4.*
   - @3.2.snmp ~14.5
6. In SNMPv2c, what role does the community string play when a manager polls an agent?
   - [ ] A one-time session token  - **[x] A shared password**  - [ ] A symmetric encryption key  - [ ] A unique device serial number
   - *The community string is a shared secret, read-only or read-write, sent unencrypted in each v1/v2c packet. Change the well-known defaults public and private, or better, move to SNMPv3 with authentication and encryption.*
   - @3.2.snmp ~14.6
7. Which SNMP versions use community strings and send them unencrypted? (Select 2)
   - **[x] SNMPv1**  - **[x] SNMPv2c**  - [ ] SNMPv3  - [ ] SNMPv4
   - *v1 and v2c (the c = community) = cleartext communities, so anyone sniffing sees the password. v2c added GETBULK and 64-bit counters. v3 replaced communities with users, auth and encryption.*
   - @3.2.snmp ~14.7,14.8
8. Type the UDP port syslog uses by default.
   - [=] 514 | udp 514 | udp/514
   - *Syslog = devices send log messages to a central collector on UDP 514 (TCP 6514 for syslog over TLS, Transport Layer Security). Hook: "five-one-four, logs out the door".*
   - @3.2.meth
9. A monitoring tool scans the network every night at 2 am to find new or missing devices and update the inventory. Which type of network discovery is this?
   - **[x] Scheduled**  - [ ] Ad hoc  - [ ] Passive  - [ ] Flow-based
   - *Scheduled discovery = runs automatically at set times, keeping the inventory and topology maps current. Ad hoc = run on demand, e.g. after a change or while troubleshooting. Both are named on the objectives (3.2).*
   - @3.2.sol
10. Type the syslog severity range, lowest number to highest, as start-end.
    - [=] 0-7 | 0 - 7 | 0 to 7
    - *Syslog levels run 0 to 7, and LOWER = MORE severe: 0 emergency · 1 alert · 2 critical · 3 error · 4 warning · 5 notice · 6 informational · 7 debug. Hook: "Every Alley Cat Eats Watery Noodles In Dishes". Logging at level 4 keeps 0-4 and drops the noisy 5-7.*
    - @3.2.meth
11. Which is the basic tool for collecting and storing log data from many devices?
    - [ ] SNMP agent  - [ ] Network analyser  - **[x] Syslog server / aggregator**  - [ ] Event Viewer on each PC
    - *Syslog aggregator = one place for every device's logs: searchable, timestamped (so keep NTP, Network Time Protocol, in sync) and kept off the device, so an attacker can't just wipe them. Event Viewer = the local Windows log.*
    - @3.2.meth ~14.12
12. The SOC wants one console that pulls in firewall, server and authentication logs and raises an alarm when events across them form a suspicious pattern. Which capability is that?
    - [ ] Graphing interface utilisation over time  - [ ] Scheduling credentialed vulnerability scans  - [ ] Checking device posture before granting access  - **[x] Aggregating, correlating and alerting on log data**
    - *SIEM (Security Information and Event Management) gathers logs from many sources, correlates them, for example repeated failed logins followed by a success from an unusual location, and alerts. A syslog server only stores messages.*
    - @3.2.meth ~14.13
13. Tool designed to show traffic PATTERNS and usage, like who talks to whom and how much, without full packet capture?
    - [ ] Log aggregator  - **[x] Flow data analyser**  - [ ] Bandwidth shaper  - [ ] Protocol analyser
    - *Flow data = metadata per conversation: source and destination IP, ports, protocol, bytes and time. NetFlow (Cisco), IPFIX (IP Flow Information Export, the standard) or sFlow (sampled). It answers "who's hogging the link?" without storing payloads.*
    - @3.2.meth ~14.9
14. Which are flow-analysis technologies? (Select 2)
    - **[x] NetFlow**  - **[x] sFlow**  - [ ] Nmap  - [ ] Wireshark
    - *NetFlow/IPFIX = records every flow · sFlow = samples 1 in N packets, lighter on big switches. Nmap = discovery and scanning. Wireshark = full packet capture.*
    - @3.2.sol ~14.17
15. Which tools examine the actual CONTENTS of traffic? (Select 2)
    - **[x] Protocol analyser**  - **[x] Packet sniffer**  - [ ] Port scanner  - [ ] Network mapper
    - *Protocol analyser / packet sniffer = Wireshark, tcpdump: captures full packets and decodes each layer. That's deeper than flow data, but much heavier. Port scanners and mappers probe hosts instead of reading traffic.*
    - @3.2.meth ~14.10
16. The record of NORMAL performance that anomaly alerts are measured against is the:
    - [ ] Golden configuration  - **[x] Baseline**  - [ ] SLA  - [ ] Threshold
    - *Baseline = typical CPU (Central Processing Unit), bandwidth, latency and errors over time, including busy periods. Anomaly alerting fires when a metric crosses a threshold relative to it, e.g. link at 95% when it normally peaks at 40%. You need the baseline to know what "bad" looks like.*
    - @3.2.meth ~14.11
17. Your monitoring platform calls the wireless controller's REST interface to pull client counts and posts alerts into the ticketing system. What is this API integration mainly providing?
    - [ ] Full packet capture from the wire  - [ ] Inline blocking of malicious traffic  - **[x] Automated data exchange between systems**  - [ ] Out-of-band console access
    - *API (Application Programming Interface) integration lets tools share structured data programmatically, often REST over HTTPS, instead of relying only on SNMP polling or manual exports.*
    - @3.2.meth ~14.14
18. What does port mirroring do?
    - **[x] Copies a port's traffic to a monitor port for a sniffer**  - [ ] Blocks all traffic on a port until it's re-enabled  - [ ] Bundles several ports into one logical link  - [ ] Copies the switch config to a backup switch
    - *Port mirroring = SPAN (Switched Port Analyzer) on Cisco. It copies frames to the analyser without interrupting them. A network TAP (Test Access Point) is a hardware splitter that does the same without using switch CPU. RSPAN = mirroring across switches.*
    - @3.2.meth ~14.15
19. Which protocol do performance-monitoring tools poll for interface utilisation, CPU and errors?
    - **[x] SNMP**  - [ ] Ping  - [ ] Nmap  - [ ] Syslog
    - *SNMP polling of interface counters every few minutes = the utilisation graphs (MRTG, PRTG, LibreNMS). It's how you find the bottleneck. Syslog = event messages, not counters.*
    - @3.2.sol ~14.18
20. Which protocol do echo requests use to confirm that a device is up?
    - **[x] ICMP**  - [ ] Traceroute  - [ ] RDP  - [ ] SNMP
    - *ICMP (Internet Control Message Protocol) echo request/reply = ping. Traceroute uses TTL (Time To Live) expiry messages. RDP = Remote Desktop Protocol.*
    - @3.2.sol ~14.19
21. Every 60 seconds a dashboard sends ICMP echoes to each router and requests the intranet home page, paging on-call when a check fails. What kind of monitoring is this?
    - **[x] Availability monitoring**  - [ ] Configuration monitoring  - [ ] Flow data analysis  - [ ] Log correlation
    - *Availability monitoring answers is it up: ping, port and HTTP checks, plus uptime figures measured against the SLA. Configuration monitoring watches for config changes; flow analysis looks at who talks to whom.*
    - @3.2.sol ~25.8
22. Which monitoring solution alerts when a switch's running configuration changes unexpectedly?
    - **[x] Configuration monitoring**  - [ ] Availability monitoring  - [ ] Flow analysis  - [ ] Port mirroring
    - *Configuration monitoring = regularly backs up configs, diffs them against the baseline, and alerts on drift. It catches unauthorised changes that skipped change management.*
    - @3.2.sol
23. A manager wants to know the mix of applications on the network, like 30% video. Which solution fits?
    - **[x] Flow data with application identification**  - [ ] Syslog from the core switches  - [ ] SNMP traps from each interface  - [ ] Ping sweeps of every subnet
    - *Traffic analysis = flow data, sometimes with DPI (Deep Packet Inspection) to identify applications. It's used for capacity planning and QoS (Quality of Service) policy.*
    - @3.2.sol
24. Type the syslog severity NAME for each message, in order, separated by spaces. ¶  %LINK-3-UPDOWN · %SYS-5-CONFIG_I · %OSPF-4-ERRRCV · %SYS-2-MALLOCFAIL
    - [=] error notice warning critical | err notice warning crit | error notification warning critical | errors notifications warnings critical
    - *Cisco messages are FACILITY-SEVERITY-MNEMONIC, so the middle number is the level: 3 error (interface down) · 5 notice (configured from console) · 4 warning · 2 critical (memory allocation failed). Full scale 0-7: emergency, alert, critical, error, warning, notice, informational, debug. Hook: "Every Awesome Cisco Engineer Will Need Ice-cream Daily". Lower number = worse.*
    - @3.2.meth
25. Type the net-snmp command that reads the whole system subtree from 10.0.0.1 with SNMPv2c community "public".
    - [=] snmpwalk -v2c -c public 10.0.0.1 system | snmpwalk -v 2c -c public 10.0.0.1 system | snmpwalk -v2c -c public 10.0.0.1 1.3.6.1.2.1.1 | snmpwalk -v 2c -c public 10.0.0.1 1.3.6.1.2.1.1 | snmpwalk -v2c -c public 10.0.0.1 SNMPv2-MIB::system
    - *snmpwalk walks a MIB subtree (snmpget = one OID). -v2c = version, -c = community. It succeeding with "public" is itself an audit finding: default community strings.*
    - @3.2.snmp
26. Match each need to a monitoring tool. Type the letters in order, e.g. abcde. ¶  Graph interface utilisation · keep every device's log messages centrally · correlate firewall and login events into an alert · see which hosts use the most bandwidth · give an IDS a copy of all traffic from one port ¶  A SPAN · B SIEM · C NetFlow · D syslog · E SNMP
    - [=] edbca | e d b c a | e,d,b,c,a
    - *Counters = E SNMP. Log messages = D syslog. Correlation = B SIEM. Top talkers = C NetFlow/flow data. A copy of the traffic = A SPAN/port mirroring.*
    - @3.2.meth
27. A dashboard shows: ¶  WAN1 util: 30-45% weekdays for 3 months ¶  Today 09:00: 97%, flows top talker 10.1.4.22 → cloud backup ¶What is the 30-45% history, and what named the top talker?
    - **[x] The baseline; flow data such as NetFlow**  - [ ] The SLA; SNMP traps  - [ ] The threshold; syslog  - [ ] The baseline; a SIEM correlation rule
    - *The 3-month normal = baseline. 97% crosses it, so an anomaly alert fires. Flow data (NetFlow/IPFIX/sFlow) identified the backup host. Fix: schedule the backup outside hours, or shape it with QoS.*
    - @3.2.meth

### Key facts
- **SNMP: agent UDP 161 (polls) · manager UDP 162 (traps) · MIB = database · OID = one value · v1/v2c = cleartext community strings · v3 = users, auth + encryption.**
- **Syslog UDP 514 (TLS 6514). Levels 0 emerg · 1 alert · 2 crit · 3 err · 4 warn · 5 notice · 6 info · 7 debug: lower = worse.**
- **SIEM = collect + correlate + alert · flow data = NetFlow/IPFIX/sFlow = who, how much · protocol analyser = full packets (Wireshark).**
- **Baseline = normal, anomaly = crossing it · port mirroring = SPAN (TAP = hardware) · API = automated data exchange.**
- **Solutions: discovery (Nmap, CDP/LLDP; ad hoc = on demand, scheduled = automatic) · traffic analysis · performance (SNMP counters) · availability (ping, HTTP checks) · configuration monitoring (drift).**

## Test 18 - 3.3 DR + HA (25 Q)

1. The maximum acceptable DATA LOSS, measured back in time from the outage, is the:
   - **[x] RPO**  - [ ] RTO  - [ ] MTTR  - [ ] MTBF
   - *RPO (Recovery Point Objective) = how much data you can afford to lose. An RPO of 1 hour means backing up or replicating at least hourly. Hook: RPO = Point in the past.*
   - @3.3.metr ~14.20
2. The maximum allowed TIME to restore a service after a disruption is the:
   - [ ] RPO  - **[x] RTO**  - [ ] MTTR  - [ ] MTBF
   - *RTO (Recovery Time Objective) = how quickly you must be back up, e.g. 4 hours. It drives the site choice (hot, warm or cold). Hook: RTO = Time to get back.*
   - @3.3.metr ~14.21
3. A vendor quotes that a failed switch power supply typically takes 45 minutes to swap and verify. Which metric is that figure?
   - [ ] RTO  - [ ] MTBF  - **[x] MTTR**  - [ ] RPO
   - *MTTR (Mean Time To Repair) = average time to fix a failed component, so lower is better. MTBF measures time between failures, RTO is the business target for restoring service, and RPO is acceptable data loss.*
   - @3.3.metr ~14.22
4. A high MTBF means:
   - **[x] The device is more reliable**  - [ ] The device is less reliable  - [ ] Repairs take longer  - [ ] Backups run less often
   - *MTBF (Mean Time Between Failures) = average running time between failures of REPAIRABLE gear, and higher is better. MTTF (Mean Time To Failure) = the same idea for items you replace rather than repair, like a disk.*
   - @3.3.metr ~14.23
5. Match each statement to its metric. Type the letters in order, e.g. abcd. ¶  Back online within 4 hours · lose no more than 15 minutes of data · the switch averages 50,000 hours between failures · a failed PSU takes 30 minutes to swap ¶  A MTTR · B RPO · C MTBF · D RTO
   - [=] dbca | d b c a | d,b,c,a
   - *Time to recover = D RTO. Data loss = B RPO. Between failures = C MTBF. Repair time = A MTTR.*
   - @3.3.metr
6. A DR site with only space, power and cooling, and no equipment?
   - [ ] Warm site  - **[x] Cold site**  - [ ] Hot site  - [ ] Cloud site
   - *Cold site = an empty room: the cheapest, and it takes days or weeks to bring up. DR = Disaster Recovery. Hook: cold = nothing running.*
   - @3.3.site ~14.24
7. An alternate site with some hardware and partial backups installed, needing configuration before use?
   - [ ] Cold site  - **[x] Warm site**  - [ ] Hot site  - [ ] Mirror site
   - *Warm site = some gear and older data, ready in hours to days. The middle ground.*
   - @3.3.site ~15.1
8. Fully equipped site with live, replicated data, able to take over almost immediately?
   - [ ] Cold site  - [ ] Warm site  - **[x] Hot site**  - [ ] Standby cold site
   - *Hot site = duplicate infrastructure with real-time replication: minutes to take over, and the most expensive. It gives the fastest recovery.*
   - @3.3.site ~15.2,15.3
9. Which describe ACTIVE-ACTIVE high availability? (Select 3)
   - **[x] All nodes serve traffic at the same time**  - **[x] No failover gap when one node dies**  - **[x] More complex and costly than active-passive**  - [ ] One node sits idle until needed  - [ ] Cheaper than active-passive
   - *Active-active = load shared across all nodes, so losing one just reduces capacity. Keep each node below about 50% load, or the survivor gets overloaded. HA = High Availability.*
   - @3.3.ha ~15.4
10. Which describe ACTIVE-PASSIVE high availability? (Select 3)
    - **[x] A standby node takes over only when the primary fails**  - **[x] There may be a short failover delay**  - **[x] Simpler and cheaper than active-active**  - [ ] Both nodes share the load normally  - [ ] There is never any interruption
    - *Active-passive = the standby watches with a heartbeat and takes over the VIP (Virtual IP) or service on failure. FHRP (First Hop Redundancy Protocol) routers and many firewall pairs work this way.*
    - @3.3.ha ~15.5
11. Two database hosts share a virtual IP and storage so that when the active node crashes, the standby automatically picks up its workload. What is this arrangement called?
    - [ ] NIC teaming  - **[x] Clustering**  - [ ] Port mirroring  - [ ] Link aggregation
    - *A cluster is multiple servers presenting one service, active-active or active-passive. NIC teaming bonds adapters inside a single host, and link aggregation bonds switch links. Neither protects against a whole server failing.*
    - @3.3.ha ~27.15
12. Which removes a single point of failure for a site's internet access?
    - **[x] Two ISP links from different providers, with failover**  - [ ] One faster link from the same ISP  - [ ] A second router on the same ISP circuit  - [ ] A UPS on the modem and the router
    - *Diversity = different providers, and ideally different physical paths and entry points into the building, so one backhoe can't cut both. Multipathing and redundant hardware go hand in hand. ISP = Internet Service Provider.*
    - @3.3.ha
13. A full backup runs Sunday. Which approach backs up only what changed since the LAST backup of any kind?
    - [ ] Differential  - **[x] Incremental**  - [ ] Snapshot  - [ ] Copy
    - *Incremental = changes since the last backup, full or incremental: the fastest backups and the slowest restore (the full plus EVERY incremental). Differential = changes since the last FULL: they grow each day, but a restore = the full + the latest differential.*
    - @3.3.ha ~27.12
14. A file server gets a full backup each Sunday night and a differential every weeknight. It dies Friday morning. Which backup sets restore it to Thursday night?
    - [ ] Sunday full plus Monday through Thursday differentials  - **[x] Sunday full plus Thursday's differential**  - [ ] Thursday's differential alone  - [ ] Monday's differential plus Thursday's differential
    - *A differential captures everything changed since the last full, so the latest one plus the full is enough. Incrementals would need the full plus every incremental in sequence.*
    - @3.3.ha ~27.13
15. Type the backup rule of thumb: copies, media types, offsite, as three numbers separated by dashes.
    - [=] 3-2-1 | 321 | 3 2 1
    - *3-2-1 = 3 copies of the data, on 2 different media types, with 1 offsite (or in the cloud, ideally immutable against ransomware). Test restores: a backup you've never restored is a hope, not a plan.*
    - @3.3.ha
16. Backups run every 4 hours. After an outage review, the business sets an RPO of 1 hour for the order database. What must change?
    - **[x] Back up or replicate at least every hour**  - [ ] Add a hot site  - [ ] Lower the RTO to 1 hour  - [ ] Increase the MTBF of the server
    - *RPO (Recovery Point Objective) = the most data you can afford to lose, measured back in time. Every 4 hours could lose 4 hours of orders, so backups or replication must run at least hourly. A hot site fixes RTO (Recovery Time Objective), how fast you're back up, not how much data you lose. Hook: RPO = Point in the past, RTO = Time to recover.*
    - @3.3.metr ~26.7
17. A core switch ran 2,000 hours and failed 4 times. The 4 repairs took 8 hours in total. Type the MTBF and the MTTR in hours, separated by a space.
    - [=] 500 2
    - *MTBF (Mean Time Between Failures) = operating time ÷ failures = 2,000 ÷ 4 = 500 h. MTTR (Mean Time To Repair) = repair time ÷ repairs = 8 ÷ 4 = 2 h. Higher MTBF = more reliable; lower MTTR = faster fixes.*
    - @3.3.metr
18. A team talks through a simulated ransomware attack around a table, walking through who does what, with no systems touched. Test type?
    - **[x] Tabletop exercise**  - [ ] Validation test  - [ ] Full failover test  - [ ] Penetration test
    - *Tabletop = discussion-based: cheap, safe, and it finds gaps in the plan and in communication. Hook: talk at the table.*
    - @3.3.test ~15.6
19. DR testing where staff actually execute recovery steps, like restoring backups or failing over to the DR site?
    - **[x] Validation test**  - [ ] Tabletop exercise  - [ ] Walkthrough only  - [ ] Risk assessment
    - *Validation tests = hands-on: restore tests, simulated failover, parallel tests, even full cutover. They prove that the RTO and RPO can actually be met.*
    - @3.3.test ~15.7
20. Why must a DR plan be tested regularly?
    - **[x] To prove it meets the RTO and RPO and hasn't gone stale**  - [ ] Because regulators fine any company with untested backups  - [ ] To raise the MTBF of the servers it protects  - [ ] To lower the licence costs of the backup software
    - *Environments change: new systems, staff turnover, expired credentials. An untested plan fails at the worst moment. Update the plan after every test (lessons learned).*
    - @3.3.test
21. The business says: ¶  "Payroll can be down up to 24 hours, and we can re-enter up to one day of data." ¶Type the RTO and RPO in hours, in that order, separated by a space.
    - [=] 24 24
    - *Down up to 24 h = RTO 24. One day of data loss = RPO 24, so daily backups are enough. A warm or even cold site might do.*
    - @3.3.metr
22. Match each system to the cheapest site that meets its RTO. Type the letters in order, e.g. abc. ¶  A trading platform with an RTO of 5 minutes · an internal wiki with an RTO of 2 weeks · email with an RTO of 12 hours ¶  A hot · B warm · C cold
    - [=] acb | a c b | a,c,b
    - *Minutes = hot (replicated, live). Weeks = cold (space only, the cheapest). Hours to a day = warm.*
    - @3.3.site
23. Backups run nightly: full on Sunday, INCREMENTAL Monday to Saturday. The disk dies Thursday at noon. Which sets are needed, in restore order?
    - **[x] Sunday full, then Monday, Tuesday and Wednesday incrementals**  - [ ] Sunday full, then Wednesday's incremental  - [ ] Wednesday's incremental only  - [ ] Sunday full, then Monday to Thursday incrementals
    - *Restore the full, then every incremental in order up to the last one before the failure: Sunday, Monday, Tuesday, Wednesday. Thursday's backup hasn't run yet at noon, so Thursday morning's changes are lost, within the RPO.*
    - @3.3.ha
24. Same week, but DIFFERENTIAL Monday to Saturday. Failure Thursday at noon. Which sets are needed, in restore order?
    - **[x] Sunday full, then Wednesday's differential**  - [ ] Sunday full, then Monday, Tuesday and Wednesday differentials  - [ ] Wednesday's differential only  - [ ] Sunday full only
    - *The full, plus the latest differential (Wednesday night), which already holds Monday to Wednesday's changes.*
    - @3.3.ha
25. Match each need to the right DR or HA choice. Type the letters in order, e.g. abcd. ¶  Managers talk through a flood scenario, no systems touched · two load-balanced web servers both take traffic, so losing one costs nothing · IT restores last night's backup to the DR site to prove the RTO · a standby firewall takes over within seconds when the primary fails ¶  A active-active · B active-passive · C tabletop exercise · D validation test
    - [=] cadb | c a d b | c,a,d,b
    - *Talking it through = tabletop. Both serving = active-active. Actually restoring = validation test. Standby that takes over = active-passive.*
    - @3.3.test

### Key facts
- **RPO = data loss (backup frequency) · RTO = downtime allowed · MTTR = repair time (lower is better) · MTBF = between failures (higher is better) · MTTF = for non-repairable parts.**
- **Sites: cold (space) < warm (some gear, older data) < hot (live replica) in both cost and speed. Pick the cheapest that meets the RTO.**
- **Active-active = all serving, no gap, costly · active-passive = standby, short failover. Cluster = servers · NIC teaming = adapters · diverse ISPs.**
- **Full · incremental = since the last backup (restore full + all) · differential = since the last full (restore full + latest). 3-2-1. MTBF = uptime ÷ failures · MTTR = repair time ÷ repairs.**
- **Tabletop = discussion · validation = hands-on restore or failover.**

## Test 19 - 3.4 DHCP + NTP (25 Q)

1. Put the four DHCP messages in order. Type the letters, e.g. abcd. ¶  A Request · B Offer · C Acknowledge · D Discover
   - [=] dbac | d b a c | d,b,a,c
   - *DORA: Discover (client broadcast) → Offer (server) → Request (client broadcast) → Acknowledge. DHCP (Dynamic Host Configuration Protocol) = UDP (User Datagram Protocol) 67 server, 68 client. Hook: DORA the explorer.*
   - @3.4.dhcp
2. Type the UDP ports for the DHCP server and client, in that order, separated by a space.
   - [=] 67 68
   - *Server 67, client 68. Hook: the server is older, so lower. DHCPv6 = 547 server, 546 client.*
   - @3.4.dhcp
3. The set of IP addresses a DHCP server can hand out on one subnet is the:
   - **[x] Scope**  - [ ] Lease  - [ ] Reservation  - [ ] Exclusion
   - *Scope = the range for one subnet, e.g. 10.1.1.100-10.1.1.200, plus its options and lease time. One scope per subnet/VLAN (Virtual Local Area Network).*
   - @3.4.dhcp ~15.9
4. The length of time a DHCP client may use its assigned IP is the:
   - [ ] Scope  - **[x] Lease**  - [ ] TTL  - [ ] Reservation
   - *Lease = e.g. 8 days by default in Windows. The client renews at 50% (T1, unicast to its server) and rebinds at 87.5% (T2, to any server). Short leases suit busy guest Wi-Fi.*
   - @3.4.dhcp ~15.10
5. The same IP handed to the same device every time, tied to its MAC, is a DHCP:
   - [ ] Exclusion  - [ ] Static route  - **[x] Reservation**  - [ ] Scope option
   - *Reservation = a MAC (Media Access Control) → IP mapping inside the scope, for printers and servers that need a fixed address but central management. An exclusion is different: it stops addresses being handed out at all.*
   - @3.4.dhcp ~15.8,28.11
6. What does a DHCP exclusion do?
   - **[x] Keeps specific addresses out of the pool so they're never assigned**  - [ ] Blocks one MAC address from getting any lease  - [ ] Reserves one address for one device's MAC  - [ ] Shortens the lease time for a set of clients
   - *Exclusion = carve out addresses inside a scope that are set statically, like the gateway .1 or the servers .2-.20. That avoids duplicate IP conflicts.*
   - @3.4.dhcp ~15.13
7. What are the extra settings, such as gateway and DNS, that DHCP hands out with the IP called?
   - **[x] Scope options**  - [ ] Lease flags  - [ ] Reservations  - [ ] Relays
   - *Options: 3 = router (default gateway) · 6 = DNS (Domain Name System) servers · 15 = domain name · 42 = NTP servers · 66/67 = TFTP (Trivial File Transfer Protocol) server and boot file for PXE (Preboot Execution Environment) and IP phones. Option 1 = subnet mask, so the mask is an option too.*
   - @3.4.dhcp ~15.11
8. Type the scope option number for the DEFAULT GATEWAY.
   - [=] 3 | option 3
   - *Option 3 = router. Option 6 = DNS. Hook: 3 before 6, the gateway before names.*
   - @3.4.dhcp
9. Type the scope option number for DNS servers.
   - [=] 6 | option 6
   - *Option 6 = DNS servers. Option 15 = the DNS domain suffix.*
   - @3.4.dhcp
10. Can clients on a different subnet from the DHCP server still get an address?
    - **[x] Yes, through a DHCP relay agent / IP helper on their router**  - [ ] No, DHCP only ever works on one subnet  - [ ] Only with IPv6  - [ ] Only with static routes
    - *Discover is a broadcast, and routers don't forward broadcasts. A relay agent (Cisco ip helper-address) on the client's gateway forwards it as unicast to the server. One central server can then serve every VLAN.*
    - @3.4.dhcp ~15.12
11. Which NTP time source is the most accurate one a network server can sync to?
    - **[x] A stratum 1 server**  - [ ] A stratum 15 server  - [ ] A stratum 16 server  - [ ] The device's own hardware clock
    - *Stratum = hops from the reference clock. Stratum 0 = the reference itself (GPS, atomic clock), not on the network. Stratum 1 = servers wired to it, and each hop adds 1. Stratum 16 = unsynchronised. Lower is better. Hook: stratum = steps from the source.*
    - @3.4.time
12. Type the UDP port for NTP.
    - [=] 123 | udp 123 | udp/123
    - *NTP = UDP 123. Hook: 1-2-3, time is counting.*
    - @3.4.time
13. Which time protocol gives sub-microsecond precision for finance, industrial and 5G networks?
    - [ ] RTP  - [ ] SNTP  - **[x] PTP**  - [ ] NTP
    - *PTP (Precision Time Protocol, IEEE 1588) = hardware timestamping in NICs (Network Interface Cards) and switches, nanosecond to microsecond accuracy. RTP (Real-time Transport Protocol) = voice and video streams.*
    - @3.4.time ~16.9
14. Which protects time synchronisation against spoofing and tampering?
    - **[x] NTS**  - [ ] SNTP  - [ ] Plain NTP  - [ ] TSP
    - *NTS (Network Time Security) = NTP with a TLS (Transport Layer Security) key exchange to authenticate time packets. Spoofed time can break authentication and hide attacks in the logs.*
    - @3.4.time ~16.10
15. On the warehouse VLAN, laptops that have been online all week work, but scanners powered on today show 169.254.x.x. The DHCP server sits in the data centre and is fine for other VLANs. What is the likely cause?
    - **[x] The warehouse scope has run out of addresses**  - [ ] The DNS server is offline  - [ ] The access switch has lost power  - [ ] The NTP source is unreachable
    - *Old clients still hold valid leases while newcomers get nothing, which points to a full pool. Expand the range, shorten lease times, or reclaim stale leases. A 169.254 address is APIPA, the self-assigned fallback.*
    - @3.4.dhcp ~28.9
16. A brand-new VLAN gets NO DHCP addresses at all, while the same server serves other VLANs. What's missing?
    - **[x] An ip helper-address on the new VLAN's gateway**  - [ ] A DNS forwarder on the new VLAN  - [ ] Port security on the access ports  - [ ] A default route to the internet
    - *The server is fine because other VLANs work. The new VLAN's broadcasts just never reach it. Add ip helper-address on the SVI and create a scope for the new subnet.*
    - @3.4.dhcp ~28.10
17. New hires' PCs lease addresses fine and can print to a local printer, but cannot reach anything on another subnet. Which DHCP option is most likely misconfigured?
    - [ ] Option 6, DNS servers  - **[x] Option 3, default gateway**  - [ ] Option 15, domain name  - [ ] Option 66, TFTP server
    - *Same-subnet traffic works but routed traffic fails, so option 3, the default gateway, is wrong. A bad DNS option (6) would break names while pings to IPs still work. Options 15 and 66 do not affect routing.*
    - @3.4.dhcp ~28.12
18. A rogue home router plugged into the office starts handing out 192.168.0.x addresses. Which switch feature stops it?
    - **[x] DHCP snooping**  - [ ] Port mirroring  - [ ] BPDU guard  - [ ] LACP
    - *DHCP snooping = only "trusted" ports, the uplinks to real servers, may send DHCP Offers and Acks. Rogue offers on user ports are dropped. It also builds the binding table used by DAI (Dynamic ARP Inspection).*
    - @3.4.dhcp
19. Type the Windows command that shows a PC's DHCP server, lease times and DNS servers.
    - [=] ipconfig /all
    - *ipconfig /all shows the DHCP server, lease obtained/expires, DNS servers and MAC. Plain ipconfig doesn't. Renew: ipconfig /release then ipconfig /renew.*
    - @3.4.dhcp
20. Type the two Windows commands that drop and re-request a DHCP lease, in order, separated by ;
    - [=] ipconfig /release; ipconfig /renew
    - */release sends a DHCP Release. /renew runs DORA again. Linux: dhclient -r then dhclient, or nmcli con down/up.*
    - @3.4.dhcp
21. Scope 10.20.0.0/24: pool .1-.254, gateway .1, servers .2-.20, 230 clients, lease 8 days, guest Wi-Fi. Which TWO fixes are needed? (Select 2)
    - **[x] Exclude 10.20.0.1-10.20.0.20 from the pool**  - **[x] Shorten the lease to hours**  - [ ] Reserve 10.20.0.1-10.20.0.20 for the gateway  - [ ] Lengthen the lease to 30 days  - [ ] Add a second DNS option
    - *Exclude .1-.20 so DHCP never hands out the gateway or server addresses, which would cause duplicate-IP conflicts. 230 guests with 8-day leases would exhaust the roughly 234 free addresses, so shorten the lease to hours.*
    - @3.4.dhcp
22. Type the scope option number for each, in order, separated by spaces: default gateway · DNS servers · domain name · TFTP server for IP phones.
    - [=] 3 6 15 66
    - *3 router · 6 DNS · 15 domain · 66 TFTP server name (67 = boot file name). 42 = NTP.*
    - @3.4.dhcp
23. A domain login fails with "clock skew too great", and the PC's clock is 9 minutes off. What needs fixing?
    - **[x] NTP time sync to a common source**  - [ ] DNS forwarding  - [ ] The DHCP lease time  - [ ] The Kerberos password
    - *Kerberos rejects tickets if clocks differ by more than 5 minutes by default. Point the PC and the DC (Domain Controller) at the same NTP source (in AD, the domain hierarchy syncs from the PDC Emulator).*
    - @3.4.time
24. A host gets the prefix 2001:db8:1:1::/64 from a router advertisement and builds its interface ID with EUI-64. Its MAC is 00:1A:2B:3C:4D:5E. Which interface ID does it make?
    - **[x] 021a:2bff:fe3c:4d5e**  - [ ] 001a:2bff:fe3c:4d5e  - [ ] 001a:2b3c:4d5e:fffe  - [ ] fffe:001a:2b3c:4d5e
    - *EUI-64: split the 48-bit MAC in half, insert ff:fe in the middle (00:1A:2B:FF:FE:3C:4D:5E), then flip the 7th bit of the first byte, 00 → 02. Result 021a:2bff:fe3c:4d5e, full address 2001:db8:1:1:21a:2bff:fe3c:4d5e. The address then exposes the MAC, which is why modern OSes use random IDs instead. SLAAC = the host builds its own address. Stateless DHCPv6 adds only extras like DNS. Stateful DHCPv6 hands out the address itself. Hook: split, stuff FFFE, flip the 7th bit. Beyond the exam: EUI-64 isn't named in N10-009, but you see it on routers.*
    - @1.8.ipv6
25. A network administrator is working in the IPAM console. Which task is most likely?
    - **[x] Correlating users and devices with their assigned IP addresses**  - [ ] Listing all MIB values on a switch  - [ ] Identifying wireless frequencies in use  - [ ] Viewing cloud synchronisation between sites  - [ ] Viewing software upgrades over a time frame
    - *Answer: Correlating users with IPs. IPAM (IP Address Management) tracks subnets, assignments, DHCP leases and DNS records, so you can see who or what holds which address. MIB = SNMP; frequencies = Wi-Fi analyser; upgrades = change management. Hook: IPAM = the address book for IPs.*
    - @3.4.ipam

### Key facts
- **DHCP DORA: discover, offer, request, ack · UDP 67 server / 68 client · scope = pool per subnet · lease (renew at 50%) · reservation = MAC → same IP · exclusion = never hand out.**
- **Options: 3 gateway · 6 DNS · 15 domain · 42 NTP · 66/67 TFTP/boot. Relay = ip helper-address on the client gateway. DHCP snooping stops rogue servers.**
- **No lease → 169.254 APIPA: scope exhausted, no relay, or server down. IPs but no other subnets = option 3 wrong.**
- **SLAAC = IPv6 self-addressing from the RA prefix.**
- **NTP UDP 123 (strata, ms) · PTP IEEE 1588 (hardware, ns-µs) · NTS = authenticated NTP. Kerberos needs clocks within 5 minutes.**

## Test 20 - 3.4 DNS (26 Q)

1. A user types mail.eu.contoso.org into a browser. Counting from the root, which label is the second-level domain the company registered?
   - [ ] org  - **[x] contoso**  - [ ] eu  - [ ] mail
   - *Read an FQDN from right to left: the implied root, then the TLD org, then the second-level domain contoso that the organisation registered, then the subdomain eu, then the host mail.*
   - @3.4.dns ~27.16
2. Which DNS record maps a name to an IPv4 address?
   - **[x] A**  - [ ] AAAA  - [ ] PTR  - [ ] CNAME
   - *A = hostname → 32-bit IPv4 address. DNS (Domain Name System) queries use UDP (User Datagram Protocol) 53, and TCP (Transmission Control Protocol) 53 for zone transfers and large replies.*
   - @3.4.dns ~15.19
3. Domain-joined PCs find the domain controllers' LDAP and Kerberos services by looking up _ldap._tcp.corp.example. Which record type?
   - **[x] SRV**  - [ ] MX  - [ ] CNAME  - [ ] TXT
   - *SRV (Service) record = service, protocol, priority, weight, PORT and target host, e.g. _ldap._tcp → dc1 port 389. Active Directory, SIP and XMPP rely on them. Hook: SRV = SeRVice finder, the only common record that carries a port number. Beyond the exam: SRV isn't on the N10-009 record list, but it's how real AD works.*
   - @3.4.dns
4. Which DNS record is an ALIAS pointing one name at another name?
   - [ ] A  - [ ] PTR  - **[x] CNAME**  - [ ] MX
   - *CNAME (Canonical Name) = www.example.com → example.com. It points to a NAME, never an IP, and can't sit at the zone apex. Several aliases can share one target.*
   - @3.4.dns ~15.21
5. Which DNS record names a domain's mail servers?
   - **[x] MX**  - [ ] TXT  - [ ] SOA  - [ ] SRV
   - *MX (Mail Exchanger) = the mail server for the domain, with a priority number where LOWER = preferred. It points to a name that has its own A/AAAA record.*
   - @3.4.dns ~15.22
6. What does a TXT record do? (Select 2)
   - **[x] Gives outside services extra information about the domain, like SPF, DKIM or ownership verification**  - **[x] Doesn't direct any traffic by itself**  - [ ] Reverse lookup from IP to name  - [ ] Lists the mail servers
   - *TXT = free text. SPF (Sender Policy Framework) = which servers may send mail for the domain. DKIM (DomainKeys Identified Mail) = the public signing key. DMARC (Domain-based Message Authentication, Reporting and Conformance) = the policy. Plus verification strings for Microsoft 365, Google and so on.*
   - @3.4.dns ~15.23
7. You delegate a new zone and must tell the parent which servers hold authoritative data for it. Which record type do you publish?
   - [ ] SOA  - **[x] NS**  - [ ] CNAME  - [ ] PTR
   - *NS (Name Server) records list the servers authoritative for a zone, and matching NS records in the parent perform the delegation. The SOA holds the primary server, admin contact, serial and timers.*
   - @3.4.dns ~15.24
8. Which describe a PTR record? (Select 2)
   - **[x] Maps an IP address back to a hostname**  - **[x] Lives in a reverse lookup zone**  - [ ] Maps a hostname to an IPv4 address  - [ ] Names the mail servers
   - *PTR (Pointer) = reverse DNS: 93.184.215.14 → example.com, stored under in-addr.arpa (ip6.arpa for IPv6). Mail servers often reject senders without matching reverse DNS.*
   - @3.4.dns ~15.25
9. A FORWARD lookup zone does what?
   - **[x] Resolves names to IP addresses**  - [ ] Resolves IP addresses to names  - [ ] Forwards all queries to the ISP  - [ ] Stores MAC addresses
   - *Forward zone = A, AAAA, CNAME, MX records: name → IP. Several A records for one name (dig one.one.one.one → 1.1.1.1 and 1.0.0.1) = round-robin DNS for redundancy; a traceroute whose last hop changes between runs = redundant routers. A reverse zone = PTR records: IP → name. A "forwarder" is a different thing: a server you pass queries on to.*
   - @3.4.dns ~16.1
10. A log analyst sees only IP addresses and wants them translated back into hostnames. Which DNS zone type and record serve that purpose?
    - **[x] A reverse lookup zone with PTR records**  - [ ] A forward lookup zone with A records  - [ ] A conditional forwarder  - [ ] A zone containing only MX records
    - *Reverse zones live under in-addr.arpa (or ip6.arpa) with the octets reversed, and PTR records map addresses to names. Mail filters and logging tools rely on them.*
    - @3.4.dns ~16.2
11. A DNS server holding and answering from the ORIGINAL records for a domain is:
    - **[x] Authoritative**  - [ ] Non-authoritative  - [ ] A caching-only resolver  - [ ] A root hint
    - *Authoritative = the source of truth for the zone, and its answers carry the AA (Authoritative Answer) flag. Non-authoritative = an answer from cache, e.g. your ISP's resolver.*
    - @3.4.dns ~16.3
12. You run nslookup against your ISP's caching resolver for a public site. What kind of answer will it report?
    - [ ] Authoritative  - **[x] Non-authoritative**  - [ ] A zone transfer  - [ ] A root hint
    - *A resolver that is not the zone's own server returns data it fetched or cached, so nslookup labels it non-authoritative. That is expected behaviour, and the record's TTL controls how long the cache keeps it.*
    - @3.4.dns ~16.4
13. The authoritative server storing the editable, master copy of a zone is the:
    - **[x] Primary DNS server**  - [ ] Secondary DNS server  - [ ] Root server  - [ ] Caching server
    - *Primary = where you edit records. Secondary = a read-only copy pulled by zone transfer (AXFR full, IXFR incremental) over TCP 53, for redundancy. Active Directory-integrated zones replicate through AD instead.*
    - @3.4.dns ~16.5
14. A backup DNS server holding a read-only COPY of a zone is the:
    - [ ] Primary  - **[x] Secondary**  - [ ] Forwarder  - [ ] Root
    - *Secondary = copies from the primary when the SOA serial number increases. Restrict zone transfers to known secondaries, or anyone can dump the whole zone.*
    - @3.4.dns ~16.6
15. A lookup where the resolver does all the work, contacting root, TLD and authoritative servers, and returns the final answer:
    - **[x] Recursive**  - [ ] Iterative  - [ ] Dynamic  - [ ] Reverse
    - *Recursive = "get me the final answer": the client asks the resolver, and the resolver chases it down. Iterative = each server just gives a referral ("ask .com"), and the asker follows it. Resolvers query iteratively on the client's behalf.*
    - @3.4.dns ~16.7
16. One workstation keeps sending intranet.corp traffic to the wrong IP even though DNS returns the correct one. Which local file would most likely explain this?
    - **[x] The hosts file**  - [ ] The NIC driver settings  - [ ] The routing table  - [ ] The ARP cache
    - *The hosts file is checked before DNS on Windows and Linux, so a stale or malicious entry overrides the real record. Malware sometimes edits it to redirect users.*
    - @3.4.dns ~16.8
17. Which DNS security suite signs records to prove integrity and authenticity?
    - **[x] DNSSEC**  - [ ] DoH  - [ ] DoT  - [ ] DNSCrypt
    - *DNSSEC (DNS Security Extensions) = digital signatures (RRSIG records, a chain of trust from the root via DS records) against cache poisoning. It gives integrity only, NOT confidentiality: queries are still readable.*
    - @3.4.dns ~15.15
18. Which protocols give DNS CONFIDENTIALITY by encrypting queries? (Select 2)
    - **[x] DoH**  - **[x] DoT**  - [ ] DNSSEC  - [ ] DTLS
    - *DoH (DNS over HTTPS, Hypertext Transfer Protocol Secure) and DoT (DNS over TLS, Transport Layer Security) encrypt queries. DNSSEC only signs. DTLS (Datagram TLS) = TLS for UDP applications in general, not DNS-specific.*
    - @3.4.dns ~15.16
19. Which hides DNS queries inside ordinary HTTPS web traffic on 443?
    - [ ] DoT  - **[x] DoH**  - [ ] DNSSEC  - [ ] IPsec
    - *DoH = port 443, indistinguishable from web browsing, which is great for privacy and a headache for corporate DNS filtering. Hook: DoH hides in the Herd (HTTPS).*
    - @3.4.dns ~15.17
20. Type the TCP port DoT uses.
    - [=] 853 | tcp 853 | tcp/853
    - *DoT = DNS over TLS on its own port 853, so it's encrypted but easy to identify and block, unlike DoH on 443.*
    - @3.4.dns ~15.18
21. Which record's TTL most affects how quickly a DNS change reaches users?
    - **[x] The TTL of the record being changed**  - [ ] The TTL of the domain's MX record  - [ ] The lease time on the DHCP scope  - [ ] The serial number in the SOA record
    - *Resolvers keep a record until its TTL (Time To Live) expires. Before a migration, lower the TTL to e.g. 300 seconds a day ahead, then make the change.*
    - @3.4.dns
22. Match each to its record type. Type the letters in order, e.g. abcdefg. ¶  mail.example.com is the mail server · www is an alias of web01 · web01 is 203.0.113.10 · web01 also has 2001:db8::10 · 203.0.113.10 maps back to web01 · SPF policy · ns1 serves the zone ¶  A TXT · B A · C NS · D MX · E PTR · F AAAA · G CNAME
    - [=] dgbfeac | d g b f e a c | d,g,b,f,e,a,c
    - *D MX mail · G CNAME alias · B A IPv4 · F AAAA IPv6 · E PTR reverse · A TXT SPF/verification · C NS name servers.*
    - @3.4.dns
23. A remote user can ping internal IPs but can't open sites by name. Type the Windows command that shows which DNS servers the laptop is using.
    - [=] ipconfig /all
    - *ipconfig /all lists the DNS servers, DHCP server and lease. Plain ipconfig doesn't list DNS. Linux: resolvectl status, or cat /etc/resolv.conf.*
    - @3.4.dns ~28.1
24. The laptop's DNS is 192.168.50.1. Type the command that asks THAT server to resolve google.com.
    - [=] nslookup google.com 192.168.50.1 | dig @192.168.50.1 google.com | dig google.com @192.168.50.1
    - *nslookup name server = query that server directly. Ping only proves the box is up, not that the DNS service works. Linux: dig @192.168.50.1 google.com.*
    - @3.4.dns ~28.2
25. Output: ¶C:\> nslookup example.com ¶DNS request timed out. ¶Server:  UnKnown ¶Address:  10.0.0.53 ¶Ping to 142.250.1.100 works. Type the command that tests the same lookup against 8.8.8.8, to prove 10.0.0.53 is the fault.
    - [=] nslookup example.com 8.8.8.8 | dig @8.8.8.8 example.com | dig example.com @8.8.8.8
    - *If 8.8.8.8 answers but 10.0.0.53 times out, the internal DNS server, or port 53 to it, is the fault. Pinging by IP already proved routing works. The fix: point clients at a working resolver, then escalate the broken server. Afterwards: verify full functionality, then document.*
    - @3.4.dns ~29.3,28.3,28.4
26. A lookup shows: ¶  $ dig example.com ¶;; ANSWER SECTION: ¶example.com.     3600   IN   A   93.184.215.14 ¶;; SERVER: 10.0.0.53#53(10.0.0.53) ¶Type the TTL in seconds, then the IP of the server that answered, separated by a space.
    - [=] 3600 10.0.0.53
    - *The second column of the answer line = TTL, how long resolvers may cache it. IN = the internet class, A = IPv4. The ;; SERVER line = which resolver answered, and #53 = port 53.*
    - @3.4.dns ~29.17,29.18

### Key facts
- **FQDN www.paris.example.com: TLD com · second-level example · subdomain paris · host www. DNS = UDP/TCP 53.**
- **A IPv4 · AAAA IPv6 · CNAME alias to a name · MX mail (lower = preferred) · TXT (SPF/DKIM/verify) · NS name servers · PTR reverse · SOA zone info.**
- **Forward zone name → IP · reverse zone IP → name (in-addr.arpa). Authoritative = holds the records · non-authoritative = cached. Primary = editable · secondary = zone transfer copy.**
- **Recursive = the resolver does all the work · iterative = referrals. Hosts file beats DNS. TTL = cache time.**
- **DNSSEC = signs (integrity) · DoH 443 and DoT 853 = encrypt (confidentiality).**
- **Troubleshooting: ipconfig /all → nslookup name server (dig @server name) → try 8.8.8.8 → fix, verify, document.**

## Test 21 - 3.5 Remote Access (24 Q)

1. VPN type that connects whole NETWORKS, like a branch office to HQ?
   - **[x] Site-to-site**  - [ ] Client-to-site  - [ ] Clientless  - [ ] Split tunnel
   - *Site-to-site VPN (Virtual Private Network) = permanent tunnel between two gateways, usually IPsec (Internet Protocol Security). Users don't run any software; the routers or firewalls do it.*
   - @3.5.vpn ~16.11
2. Sales reps travelling with laptops need secure access to internal resources. Which VPN approaches serve individual users? (Select 2)
   - **[x] Client-to-site / remote access**  - **[x] Clientless, browser-based**  - [ ] Site-to-site  - [ ] Unencrypted GRE tunnel
   - *Remote access VPNs use an installed client with IPsec or TLS. Clientless VPNs give web-portal access over HTTPS with nothing to install. Site-to-site links whole networks, and GRE alone adds no encryption.*
   - @3.5.vpn ~16.12
3. How is CLIENTLESS VPN access usually delivered?
   - **[x] Through a web browser**  - [ ] A command-line client  - [ ] A proxy server  - [ ] A site-to-site gateway
   - *Clientless = a browser SSL/TLS (Secure Sockets Layer / Transport Layer Security) portal. It's good for contractors and unmanaged devices, but only covers web-type apps.*
   - @3.5.vpn ~16.13
4. Sending ONLY corporate traffic through the VPN while everything else goes direct to the internet is:
   - **[x] Split tunnel**  - [ ] Full tunnel  - [ ] Clientless VPN  - [ ] Site-to-site VPN
   - *Split tunnel = saves HQ bandwidth and speeds up YouTube and Teams, but internet traffic skips corporate inspection. Full tunnel = everything goes through the VPN.*
   - @3.5.vpn ~16.14
5. Security wants the proxy and DLP tools at headquarters to see every packet from home workers, including general internet use. How should the VPN be set up?
   - **[x] Full tunnel**  - [ ] Split tunnel  - [ ] Clientless portal  - [ ] Site-to-site
   - *With a full tunnel the default route points into the VPN, so all traffic passes the corporate inspection stack. The trade-off is more load on the HQ link and extra latency.*
   - @3.5.vpn ~24.8
6. Home workers say video meetings over the VPN stutter, and the headquarters internet circuit sits at 100 percent. What change would most likely help?
   - **[x] Switch to split tunnelling**  - [ ] Switch to full tunnelling  - [ ] Add a second VPN concentrator at the branch  - [ ] Lower the MTU on all PCs
   - *With a split tunnel, only corporate traffic goes into the tunnel and SaaS or streaming traffic leaves via the user's own ISP, which takes load off the HQ link. Check that this fits the security policy.*
   - @3.5.vpn ~24.9
7. Headquarters needs a purpose-built device to terminate thousands of employee remote-access tunnels. What is it called?
   - **[x] VPN concentrator / headend**  - [ ] Load balancer  - [ ] Forward proxy  - [ ] Wireless LAN controller
   - *A VPN concentrator offloads the encryption and session handling for large numbers of IPsec or TLS clients, and the feature is often built into an NGFW. In hub-and-spoke designs the headend is the central site.*
   - @3.5.vpn ~24.7
8. An admin needs an encrypted text session to a Linux router's CLI. Which description fits the protocol to use?
   - **[x] Encrypted command-line access on TCP 22**  - [ ] Graphical remote desktop on TCP 3389  - [ ] Unencrypted terminal access on TCP 23  - [ ] Windows file sharing on TCP 445
   - *SSH (Secure Shell) gives an encrypted CLI and also carries SFTP and SCP. It replaces Telnet, which sends everything in cleartext. Prefer key-based authentication.*
   - @3.5.mgmt ~16.15
9. Type the command to open an SSH session to switch 10.0.0.2 as user admin.
   - [=] ssh admin@10.0.0.2 | ssh -l admin 10.0.0.2
   - *user@host, or -l user host. TCP 22. Add -p 2222 for a non-standard port. Telnet 10.0.0.2 would send the password in cleartext.*
   - @3.5.mgmt ~32.25
10. Which is a GUI-based remote connection?
    - [ ] API  - [ ] SSH  - [ ] CLI  - **[x] RDP**
    - *RDP (Remote Desktop Protocol) = graphical Windows desktop, TCP/UDP 3389. VNC (Virtual Network Computing, 5900) = the cross-platform GUI equivalent. Never expose 3389 to the internet: put it behind a VPN or gateway.*
    - @3.5.mgmt ~16.16
11. Type the RDP port.
    - [=] 3389 | tcp 3389 | tcp/3389
    - *RDP = 3389. SSH 22 · Telnet 23 · HTTPS 443 · VNC 5900.*
    - @3.5.mgmt
12. Which method lets systems communicate and be managed automatically by software?
    - **[x] API**  - [ ] RDP  - [ ] Console cable  - [ ] Telnet
    - *API (Application Programming Interface) = e.g. REST (Representational State Transfer) over HTTPS with JSON, used by automation, controllers, SD-WAN (Software-Defined WAN) and IaC (Infrastructure as Code). Scripted, repeatable, no screen-scraping.*
    - @3.5.mgmt ~16.17
13. What is console access?
    - **[x] A direct cable to the device's console port, for setup and recovery**  - [ ] Remote access to the device's CLI over SSH  - [ ] The device's web management page over HTTPS  - [ ] An SNMP poll of the device's status
    - *Console = RJ45 rollover or USB cable into the console port, a terminal emulator (PuTTY) at 9600 baud, 8-N-1. It works with no IP configured at all, which is why it's used for initial setup and password recovery.*
    - @3.5.mgmt ~16.18
14. Dedicated, hardened host admins log into first, which then connects to devices in a more secure segment?
    - **[x] Jump box**  - [ ] Honeypot  - [ ] Proxy server  - [ ] Load balancer
    - *Jump box (bastion host) = the single audited path into the management network, with MFA (Multi-Factor Authentication) and session logging. Admin PCs never touch the switches directly.*
    - @3.5.mgmt ~16.19
15. Managing devices over the SAME network that carries user traffic is:
    - **[x] In-band management**  - [ ] Out-of-band management  - [ ] Console management  - [ ] Inline management
    - *In-band = SSH, HTTPS, SNMP (Simple Network Management Protocol) and RDP across the production network. It's convenient, but if the network is down you lose access too. Use a separate management VLAN to reduce the risk.*
    - @3.5.mgmt ~16.20
16. Devices must stay reachable even when the production network is down. Approach?
    - **[x] Out-of-band management**  - [ ] In-band management  - [ ] A management VLAN on the same switches  - [ ] Port mirroring
    - *OOB (Out-of-Band) = a separate path: console servers, a dedicated management network, or a cellular/LTE (Long-Term Evolution) modem into a console server. It's how you fix the router that just took the WAN down.*
    - @3.5.mgmt ~16.21
17. Which ways of managing a switch use the production data network and therefore count as in-band? (Select 4)
    - **[x] SSH**  - **[x] HTTPS web GUI**  - **[x] SNMP**  - **[x] Telnet**  - [ ] Serial console cable
    - *If management traffic rides the same network as user data, it is in-band, whether that is SSH, a web GUI, SNMP or Telnet. A direct serial console is out-of-band.*
    - @3.5.mgmt ~16.22
18. The WAN is down and you still need to reach a remote router's CLI. Which option is out-of-band?
    - [ ] A network TAP  - [ ] A loopback plug  - **[x] The console port, through a console server**  - [ ] SSH over the management VLAN
    - *A console server cables into device console ports and is reached by its own separate link, such as cellular or a dedicated circuit. A management VLAN still crosses the production switches, so it counts as in-band.*
    - @3.5.mgmt ~16.23
19. Which remote-access method gives admins GUI desktops through a browser without exposing RDP?
    - **[x] An RDP gateway over HTTPS**  - [ ] Telnet with a web front end  - [ ] SNMPv1 with a GUI console  - [ ] Opening TCP 3389 on the firewall
    - *A remote desktop gateway wraps RDP inside HTTPS 443 with MFA, so 3389 never faces the internet. Exposed RDP is among the most common ransomware entry points.*
    - @3.5.mgmt
20. Why is Telnet unacceptable for device management?
    - **[x] It sends everything, including passwords, in cleartext**  - [ ] It's too slow for modern devices to use  - [ ] It only works over the console port  - [ ] It needs a GUI on the device to run
    - *Telnet (TCP 23) = cleartext. Anyone with a sniffer on the path reads the credentials. On Cisco, use transport input ssh on the VTY (virtual terminal) lines.*
    - @3.5.mgmt
21. Match each to its VPN type. Type the letters in order, e.g. abcde. ¶  A branch router permanently tunnels to HQ · a contractor opens a web portal to one intranet app · a laptop runs the VPN client · all laptop traffic is inspected at HQ · only corporate subnets use the tunnel ¶  A split tunnel · B client-to-site · C full tunnel · D site-to-site · E clientless
    - [=] debca | d e b c a | d,e,b,c,a
    - *Network to network = D site-to-site. Browser only = E clientless. Client software = B client-to-site. Everything via HQ = C full tunnel. Only corporate traffic = A split.*
    - @3.5.vpn
22. Match in-band or out-of-band to each. Type the letters in order, e.g. aaaa. ¶  A console server reached over a 4G modem · SSH across the office LAN · a laptop on the console port with a rollover cable · HTTPS to the firewall's web GUI ¶  A in-band · B out-of-band
    - [=] baba | b a b a | b,a,b,a
    - *A separate path = out-of-band (4G console server, direct console cable). Across production = in-band (SSH, HTTPS).*
    - @3.5.mgmt
23. Type the command that opens an SSH session to 203.0.113.5 as user netops on port 2222.
    - [=] ssh -p 2222 netops@203.0.113.5 | ssh netops@203.0.113.5 -p 2222 | ssh -p 2222 -l netops 203.0.113.5
    - *-p sets the port. Moving SSH off 22 cuts log noise from bots but isn't real security: use keys, MFA and a jump host.*
    - @3.5.mgmt
24. Match each need to a management method. Type the letters in order, e.g. abcde. ¶  A Python script updates 200 switch VLANs · a Windows server's GUI · first-time setup of a new router with no IP · an encrypted CLI to a Linux host · the one audited entry point into the management network ¶  A jump box · B console · C SSH · D RDP · E API
    - [=] edbca | e d b c a | e,d,b,c,a
    - *Automation = E API. GUI on Windows = D RDP. No IP yet = B console. Encrypted CLI = C SSH. Single audited entry point = A jump box.*
    - @3.5.mgmt

### Key facts
- **Site-to-site = network to network (IPsec) · client-to-site = VPN client on a device · clientless = browser portal (SSL/TLS). Concentrator = terminates many tunnels.**
- **Full tunnel = all traffic via HQ (inspected, slow) · split tunnel = only corporate traffic via VPN (fast, less visibility).**
- **SSH 22 (encrypted CLI, ssh user@host) · Telnet 23 cleartext, never · RDP 3389 GUI (use a gateway) · API = automation (REST/JSON).**
- **Console = direct serial/USB port, no IP needed · jump box/bastion = hardened hop into the management network.**
- **In-band = over production (SSH, HTTPS, SNMP) · out-of-band = separate path (console server, 4G, dedicated management network).**

## Test 22 - 4.1 Security Concepts I (25 Q)

1. Which encrypt data IN TRANSIT? (Select 3)
   - **[x] TLS**  - **[x] IPsec**  - **[x] VPN**  - [ ] FDE  - [ ] SED  - [ ] EFS
   - *In transit (in motion) = moving across a network: TLS (Transport Layer Security, HTTPS), IPsec (Internet Protocol Security), SSH (Secure Shell) and VPNs (Virtual Private Networks). FDE (Full Disk Encryption, e.g. BitLocker), SED (Self-Encrypting Drive) and EFS (Encrypting File System) protect data at REST.*
   - @4.1.enc ~16.24
2. An auditor asks you to point to information that is stored rather than moving across the network. Which items qualify as data at rest? (Select 3)
   - **[x] Last night's backup image on the NAS**  - **[x] Customer rows sitting in a database on disk**  - **[x] Old project files in cold archive storage**  - [ ] A Teams video call in progress  - [ ] A file being uploaded over SFTP
   - *Data at rest is stored on some medium: disks, backups, archives. Protect it with full-disk or database encryption. Data in transit, like calls and uploads, is protected with TLS, IPsec or SSH.*
   - @4.1.enc ~16.25
3. Which data states should almost always be encrypted? (Select 2)
   - **[x] In transit**  - **[x] At rest**  - [ ] In use  - [ ] In cache
   - *In transit and at rest = the standard pair every policy requires. Data in use sits decrypted in RAM (Random Access Memory) so the CPU (Central Processing Unit) can work on it, and protecting it needs special hardware such as secure enclaves. Hook: rest, road, RAM.*
   - @4.1.enc ~17.1
4. Data being processed in RAM by an application is in which state?
   - [ ] At rest  - [ ] In transit  - **[x] In use**  - [ ] In motion
   - *In use = loaded into memory and being processed. That's why memory-scraping malware and cold-boot attacks target it. "In motion" is just another name for in transit.*
   - @4.1.enc ~27.22
5. The hierarchy that issues, manages, distributes and revokes digital certificates is:
   - **[x] PKI**  - [ ] IAM  - [ ] SAML  - [ ] OCSP
   - *PKI (Public Key Infrastructure) = root CA (Certificate Authority) → intermediate CAs → end-entity certificates. It also includes revocation, through a CRL (Certificate Revocation List) or OCSP (Online Certificate Status Protocol), and the trust stores that browsers and OSs ship with.*
   - @4.1.enc ~17.2
6. A developer generates a TLS certificate on a lab server and signs it with its own key. Which statements about this certificate are true? (Select 3)
   - **[x] No trusted public CA vouches for it**  - **[x] Browsers warn about it unless it is manually trusted**  - **[x] It is acceptable for internal testing and lab use**  - [ ] It is the right choice for a public online store  - [ ] Every browser trusts it automatically
   - *A self-signed certificate is its own issuer, so it is not in any browser trust store. That is fine in a lab or for internal tools. Public sites need a certificate from a trusted CA.*
   - @4.1.enc ~17.3
7. The framework that manages who can access which digital resources is:
   - [ ] PKI  - **[x] IAM**  - [ ] AAA only  - [ ] NAC
   - *IAM (Identity and Access Management) = identities, authentication, authorisation and auditing: SSO, MFA, RBAC, provisioning and deprovisioning. AAA = Authentication (who are you?), Authorisation (what may you do?), Accounting (what did you do?).*
   - @4.1.iam ~17.4
8. MFA requires factors from at least two DIFFERENT categories. Which pair is true MFA?
   - **[x] Password + authenticator app code**  - [ ] Password + security question  - [ ] Two different passwords  - [ ] A PIN + a password
   - *MFA (Multi-Factor Authentication) categories: something you know (password, PIN), have (phone, token, smart card), are (fingerprint, face) and somewhere you are (location). A password + a security question = two things you know, so it's NOT MFA.*
   - @4.1.iam ~17.5
9. Logging in ONCE to reach many systems is:
   - [ ] MFA  - **[x] SSO**  - [ ] RBAC  - [ ] TOTP
   - *SSO (Single Sign-On) = one authentication, then tokens for everything else, via SAML, OAuth/OIDC (OpenID Connect) or Kerberos. Fewer passwords for users, but it makes that one account very valuable, so protect it with MFA.*
   - @4.1.iam ~17.6
10. Which AAA protocol is used for Wi-Fi 802.1X and VPN user logins?
    - **[x] RADIUS**  - [ ] TACACS+  - [ ] LDAP  - [ ] SAML
    - *RADIUS (Remote Authentication Dial-In User Service) = UDP (User Datagram Protocol) 1812 authentication and 1813 accounting. It encrypts only the password field. It's used for 802.1X Wi-Fi, VPNs and switch-port NAC (Network Access Control).*
    - @4.1.iam ~17.7
11. Which directory protocol queries user accounts, groups and devices, e.g. in Active Directory?
    - [ ] RADIUS  - [ ] SAML  - **[x] LDAP**  - [ ] Kerberos
    - *LDAP (Lightweight Directory Access Protocol) = TCP (Transmission Control Protocol) 389. LDAPS (LDAP over TLS) = 636. Apps and appliances use it to look users and groups up in AD (Active Directory).*
    - @4.1.iam ~17.8
12. Which XML-based standard passes authentication data from an identity provider to a web service for SSO?
    - [ ] LDAP  - [ ] TACACS+  - [ ] Kerberos  - **[x] SAML**
    - *SAML (Security Assertion Markup Language) = an XML (Extensible Markup Language) assertion from the IdP (Identity Provider, e.g. Entra ID or Okta) to the SP (Service Provider, the SaaS app). It's the classic web SSO for enterprises.*
    - @4.1.iam ~17.9
13. Which AAA protocol is used mainly for admin logins to NETWORK DEVICES, with per-command authorisation?
    - [ ] RADIUS  - **[x] TACACS+**  - [ ] LDAP  - [ ] SAML
    - *TACACS+ (Terminal Access Controller Access-Control System Plus) = TCP 49. It encrypts the WHOLE payload and separates authentication, authorisation and accounting, so each command can be authorised and logged. Hook: TACACS+ for the admins on the boxes, RADIUS for users on the network.*
    - @4.1.iam ~17.10
14. Which is true of RADIUS versus TACACS+?
    - **[x] RADIUS: UDP, encrypts only the password; TACACS+: TCP 49, encrypts everything**  - [ ] RADIUS: TCP 49, encrypts everything; TACACS+: UDP, encrypts only the password  - [ ] RADIUS: open standard for admins; TACACS+: open standard for Wi-Fi users  - [ ] Both use UDP and encrypt only the password, so either fits the same job
    - *RADIUS = UDP 1812/1813, open standard, combines authentication and authorisation, for network access. TACACS+ = TCP 49, Cisco-originated, full encryption, per-command control for device administration.*
    - @4.1.iam
15. An authenticator app code changes every 30 seconds, computed from the current time and a shared secret. Mechanism?
    - **[x] TOTP**  - [ ] HOTP  - [ ] Kerberos  - [ ] A static PIN
    - *TOTP (Time-based One-Time Password) = an HMAC (Hash-based Message Authentication Code) of the time and a secret. That's why clocks must be in sync. HOTP (HMAC-based OTP) = based on a counter instead. The objectives call it time-based authentication.*
    - @4.1.iam ~17.11
16. What does least privilege mean?
    - **[x] Users get only the access their job needs, nothing more**  - [ ] Every user is an admin, for convenience  - [ ] Access is granted by location  - [ ] Privileges are reviewed only once
    - *Least privilege = the minimum rights needed, for as long as needed. It limits damage from compromised accounts and insiders. Pair it with regular access reviews and JIT (Just-in-Time) admin rights.*
    - @4.1.iam ~17.12
17. Which access model ties permissions to job roles such as helpdesk or finance?
    - [ ] DAC  - [ ] MAC  - **[x] RBAC**  - [ ] ABAC
    - *RBAC (Role-Based Access Control) = assign permissions to roles, then users to roles. When someone moves team, change their role, not dozens of permissions. Compare DAC (Discretionary, the owner decides) and MAC (Mandatory, labels decide).*
    - @4.1.iam ~17.13
18. Allowing or blocking device actions based on GPS location or a defined area is:
    - **[x] Geofencing**  - [ ] Geotagging  - [ ] Least privilege  - [ ] Time-based access
    - *Geofencing = a virtual boundary, via GPS (Global Positioning System), Wi-Fi or IP location. E.g. the MDM (Mobile Device Management) disables the camera inside the lab, or logins from outside the country are blocked. It's the "somewhere you are" factor.*
    - @4.1.iam ~17.14
19. Match the data state to each. Type the letters in order, e.g. aaaaa. ¶  A laptop's BitLocker-protected disk · an HTTPS session to the bank · a spreadsheet open in Excel · a nightly backup tape · a site-to-site IPsec tunnel ¶  A in transit · B in use · C at rest
    - [=] cabca | c a b c a | c,a,b,c,a
    - *Stored = rest (the disk, the tape). Moving = transit (HTTPS, IPsec). Loaded in RAM and being processed = use (the open spreadsheet).*
    - @4.1.enc
20. Match each to its protocol. Type the letters in order, e.g. abcde. ¶  Staff Wi-Fi 802.1X logins · per-command authorisation for switch admins · a firewall looks up AD group membership · SSO into a SaaS app from the corporate identity provider · Windows domain logon tickets ¶  A Kerberos · B TACACS+ · C RADIUS · D SAML · E LDAP
    - [=] cbeda | c b e d a | c,b,e,d,a
    - *802.1X = C RADIUS. Device administration commands = B TACACS+. Directory lookup = E LDAP (389/636). Web SSO assertion = D SAML. AD ticket-based logon = A Kerberos (TCP/UDP 88).*
    - @4.1.iam
21. Type the ports for each, in order, separated by spaces: RADIUS authentication · RADIUS accounting · TACACS+ · LDAP · LDAPS.
    - [=] 1812 1813 49 389 636
    - *RADIUS UDP 1812 authentication, 1813 accounting · TACACS+ TCP 49 · LDAP 389 · LDAPS 636. Only LDAP and LDAPS are on the port list, but the exam expects RADIUS and TACACS+ with 4.1.*
    - @4.1.iam
22. Match the MFA factor category to each. Type the letters in order, e.g. aaaaa. ¶  A fingerprint · a YubiKey · a PIN · login only allowed from inside the country · an SMS code to your phone ¶  A something you have · B somewhere you are · C something you know · D something you are
    - [=] dacba | d a c b a | d,a,c,b,a
    - *Fingerprint = are. Hardware token = have. PIN = know. Location = somewhere. An SMS code proves you have the phone = have (it's weak, because of SIM swapping).*
    - @4.1.iam
23. An intranet server shows a browser warning: ¶  "NET::ERR_CERT_AUTHORITY_INVALID - issuer: intranet01, subject: intranet01" ¶What's causing it?
    - **[x] A self-signed certificate**  - [ ] An expired certificate  - [ ] A revoked certificate  - [ ] A wildcard certificate
    - *Issuer = subject means the certificate signed itself, so it's self-signed and not chained to a trusted CA. Fix: issue it from the internal enterprise CA, whose root is pushed to domain PCs by GPO (Group Policy Object), or use a public CA.*
    - @4.1.enc
24. A user types their corporate email address into the login prompt of a public portal. What is this step?
    - **[x] Identification**  - [ ] Authentication  - [ ] Authorization  - [ ] Accounting
    - *Answer: Identification. Identification = CLAIMING who you are (username, email); it isn't secret. Authentication = PROVING it (password, code, fingerprint). Then authorization = what you may do, accounting = logging what you did. Hook: say who you are, then prove it.*
    - @4.1.iam
25. A security engineer adds new IPS rules to the firewall. Which will this change affect?
    - **[x] Data in transit**  - [ ] Identity and access management  - [ ] Role-based access control  - [ ] Public key infrastructure  - [ ] Encryption protocols
    - *Answer: Data in transit. An IPS sits inline and inspects traffic as it flows in and out, blocking known exploits. So its rules act on data in transit, not on who you are (IAM, RBAC) or keys (PKI). Hook: IPS watches the pipe, not the people.*
    - @4.1.data

### Key facts
- **In transit = TLS, IPsec, SSH, VPN · at rest = FDE/BitLocker, SED, EFS, encrypted backups · in use = in RAM, while processing.**
- **PKI = CA hierarchy, CRL/OCSP revocation · self-signed = issuer equals subject, not trusted by default, lab/internal only.**
- **MFA = 2+ DIFFERENT categories: know, have, are, somewhere. TOTP = time-based code. SSO = one login for many systems.**
- **RADIUS UDP 1812/1813, network access, password-only encryption · TACACS+ TCP 49, device admin, full encryption, per-command · LDAP 389/LDAPS 636 = directory · SAML = XML SSO between IdP and SP · Kerberos 88.**
- **Least privilege = minimum needed · RBAC = permissions by role · geofencing = location rules.**

## Test 23 - 4.1 Security Concepts II (28 Q)

1. What are the three principles of the CIA triad?
   - **[x] Confidentiality, integrity, availability**  - [ ] Control, integrity, authentication  - [ ] Confidentiality, identity, authorisation  - [ ] Compliance, integrity, accounting
   - *CIA triad = Confidentiality (only the right people read it: encryption, access control) · Integrity (it hasn't been altered: hashing, signatures) · Availability (it's there when needed: redundancy, backups, DDoS protection).*
   - @4.1.term ~17.20
2. Match each to the CIA element involved. Type the letters in order, e.g. abc. ¶  A file hash matches after download · a DDoS takes the website offline · a stolen unencrypted laptop ¶  A confidentiality · B integrity · C availability
   - [=] bca | b c a | b,c,a
   - *A matching hash = integrity checked (digital signatures = integrity too: proof it wasn't altered; non-repudiation is a bonus, not one of the CIA three). Offline = availability lost. Data readable by a thief = confidentiality lost.*
   - @4.1.term
3. A security briefing warns of a ransomware gang targeting your sector. Which term best describes the gang?
   - [ ] Risk  - [ ] Vulnerability  - [ ] Exploit  - **[x] Threat**
   - *A threat is anything that could cause harm. A vulnerability is a weakness it could use, an exploit is the method or code that uses the weakness, and risk combines likelihood and impact.*
   - @4.1.term ~17.19
4. Match each to its term. Type the letters in order, e.g. abcd. ¶  An unpatched VPN appliance · a ransomware gang · a public proof-of-concept script for the flaw · the chance and cost of being breached through it ¶  A vulnerability · B risk · C exploit · D threat
   - [=] adcb | a d c b | a,d,c,b
   - *Weakness = vulnerability. Actor = threat. The weaponised technique = exploit. Likelihood × impact = risk.*
   - @4.1.term
5. HR tells IT that a disgruntled network admin will be let go on Friday and still has full privileged accounts today. What threat category concerns the team?
   - [ ] Evil twin  - **[x] Insider threat**  - [ ] Social engineering  - [ ] DDoS
   - *An insider threat comes from someone with legitimate access, whether staff, a contractor or a partner. Disable their access as they are told, monitor privileged activity, and apply least privilege.*
   - @4.1.term ~27.14
6. Which controls deter, detect or prevent damage to PHYSICAL assets? (Select 2)
   - **[x] Security cameras**  - **[x] Hardware locks**  - [ ] A firewall  - [ ] Network segmentation
   - *Physical security objectives = cameras (deter and detect) and locks (prevent). Firewalls and segmentation are logical/technical controls.*
   - @4.1.phys ~17.15
7. Facilities wants controls that physically stop unauthorised people from entering the data hall, not merely record them. Which fit? (Select 2)
   - **[x] Badge readers / key fobs**  - **[x] An access control vestibule**  - [ ] Motion sensors that trigger an alarm  - [ ] CCTV cameras recording the door
   - *Prevention controls block entry, for example badges, locks and vestibules that allow one person at a time. Detection controls, such as cameras and motion sensors, notice or record an event but do not stop it.*
   - @4.1.phys ~27.11
8. The fire code requires that if the building loses power, the electronic locks on the server room exit release so occupants are not trapped. What is this lock behaviour called?
   - **[x] Fail-open / fail-safe**  - [ ] Fail-closed / fail-secure  - [ ] Failover  - [ ] Access control vestibule
   - *Fail-safe locks release when power is lost, so life safety comes first. Fail-secure locks stay locked on power loss to protect assets. Failover refers to redundant systems taking over, not to locks.*
   - @4.1.phys ~27.10
9. The security team deploys a fake file server with deliberately weak settings in the DMZ. Which statements describe this honeypot? (Select 2)
   - **[x] It imitates a real system to lure attackers**  - **[x] It looks vulnerable and is watched closely**  - [ ] It is a form of anti-malware software  - [ ] It is used to launch counterattacks
   - *A honeypot is a decoy. Any activity on it is suspicious and teaches you about attacker tools and methods. It never holds real data, and hacking back is illegal and not its purpose.*
   - @4.1.dcpt ~17.16
10. Instead of one decoy, the researchers build a fake environment of web, database and file servers to observe attackers moving between them. What is this called?
    - **[x] A honeynet**  - [ ] A single honeypot  - [ ] A screened subnet  - [ ] A sinkhole
    - *A honeynet is a group of honeypots that mimic a whole network, which shows lateral movement as well as initial access. A screened subnet is a real DMZ, and a sinkhole redirects malicious traffic.*
    - @4.1.dcpt ~17.17
11. Which could be part of a honeynet?
    - [ ] Fake websites  - [ ] Fake servers  - [ ] Fake databases and file shares  - **[x] All of the above**
    - *Answer: All of the above. Anything that looks real but has no legitimate use: fake shares, fake admin accounts (honeytokens), fake DNS entries.*
    - @4.1.dcpt ~17.18
12. A coffee chain starts accepting card payments through its new point-of-sale terminals. Which standard now applies?
    - **[x] PCI DSS**  - [ ] GDPR  - [ ] HIPAA  - [ ] ISO 27001
    - *PCI DSS (Payment Card Industry Data Security Standard) is required by the card brands for anyone storing, processing or transmitting cardholder data. It covers segmentation, encryption and regular testing. GDPR covers EU personal data, HIPAA covers US health data, and ISO 27001 is a voluntary certification.*
    - @4.1.comp ~24.12
13. A US online retailer starts collecting names and emails from shoppers in France and Germany. Which regulation governs that personal data?
    - [ ] PCI DSS  - [ ] HIPAA  - **[x] GDPR**  - [ ] SOX
    - *GDPR (General Data Protection Regulation) is the EU privacy law. It applies to any organisation handling EU residents' personal data, wherever the organisation is based, and includes breach notification rules.*
    - @4.1.comp ~17.22
14. A Canadian law says patient records must never leave servers physically located in Canada. Which concept is this?
    - **[x] Data locality**  - [ ] PCI DSS  - [ ] Least privilege  - [ ] Geofencing
    - *Data locality, also called data residency, means data must physically stay within a given country or region. Data sovereignty is the related idea that the country's laws apply to that data. Geofencing triggers actions based on a device's location, and least privilege and PCI DSS do not deal with where data is stored.*
    - @4.1.comp ~24.10
15. A European bank is deciding between cloud regions in Frankfurt and Virginia for a customer database. Which compliance concept most drives that choice?
    - **[x] Data locality**  - [ ] RBAC  - [ ] Encryption in use  - [ ] MTTR
    - *The region decides where the data physically lives, which determines whose laws apply. Locality requirements often rule out regions outside the required jurisdiction. RBAC controls who has access, encryption in use protects data being processed, and MTTR is a repair metric.*
    - @4.1.comp ~24.11
16. Before renewing its merchant agreement, a company hires an outside firm to verify that its controls satisfy a mandated framework. What is this engagement?
    - [ ] Penetration test  - **[x] Compliance audit**  - [ ] Vulnerability scan  - [ ] Tabletop exercise
    - *A compliance audit checks controls against a required standard and produces findings or attestation. A pen test actively tries to break in, a scan lists known weaknesses, and a tabletop is a discussion-based exercise.*
    - @4.1.comp ~24.13
17. Everyday sensor-equipped devices like wearables and smart thermostats are called:
    - **[x] IoT**  - [ ] IIoT  - [ ] OT  - [ ] ICS
    - *IoT (Internet of Things) = cameras, TVs, sensors: often weak passwords and rare patches. Segment it on its own VLAN (Virtual Local Area Network), with no route to corporate systems.*
    - @4.1.seg ~17.23
18. The subset of IoT used in industry, like connected factory sensors, is:
    - [ ] SCADA  - **[x] IIoT**  - [ ] BYOD  - [ ] IoT
    - *IIoT (Industrial IoT) = connected machinery and sensors in manufacturing, energy and logistics. It's where IT meets OT (Operational Technology).*
    - @4.1.seg ~17.24
19. Which type of industrial control system monitors geographically spread infrastructure like pipelines and power grids?
    - **[x] SCADA**  - [ ] IIoT  - [ ] PLC  - [ ] OT
    - *SCADA (Supervisory Control and Data Acquisition) = a type of ICS (Industrial Control System) using PLCs (Programmable Logic Controllers) and RTUs (Remote Terminal Units) over wide areas. Its protocols (Modbus, DNP3) often have no authentication at all.*
    - @4.1.seg ~17.25
20. A plant runs PLCs, a DCS and a SCADA system to control its physical processes. Which category groups these control systems together?
    - **[x] ICS**  - [ ] SCADA  - [ ] IoT  - [ ] BYOD
    - *ICS (Industrial Control Systems) is the broad category. SCADA is one type of ICS used for widely distributed sites. Isolate these systems from the corporate network, because many cannot be patched easily.*
    - @4.1.seg ~18.1
21. The umbrella term for ALL hardware and software that monitors and controls physical industrial operations is:
    - [ ] ICS  - [ ] SCADA  - **[x] OT**  - [ ] IIoT
    - *OT (Operational Technology) = the physical-world side, versus IT's data side. In OT, availability and safety come first, so patching is rare and planned. Isolate OT with firewalls, or air-gap it.*
    - @4.1.seg ~18.2
22. A guest network gives internet access but not internal access. Why?
    - **[x] It keeps visitors' devices away from internal systems**  - [ ] It speeds up traffic on the internal network  - [ ] It avoids needing DHCP for the guests  - [ ] It lets the guest SSID use WPA3
    - *Guest network = its own VLAN, a firewall rule "internet only", often client isolation and a captive portal. Visitors' devices aren't managed or trusted.*
    - @4.1.seg ~18.3
23. Employees using their PERSONAL devices for company data and apps is:
    - [ ] COPE  - **[x] BYOD**  - [ ] MDM  - [ ] CYOD
    - *BYOD (Bring Your Own Device) = cheaper and convenient. COPE (Corporate-Owned, Personally Enabled) and CYOD (Choose Your Own Device) = the company owns and manages the device. The BYOD risk is unmanaged personal devices touching company data. Controls: MDM/MAM (Mobile Device / Application Management), containerisation, and a separate BYOD network segment with limited access.*
    - @4.1.seg ~18.4
24. Match each device to its network segment. Type the letters in order, e.g. abcde. ¶  Staff's domain-joined laptops · a visitor's phone · smart TVs and door cameras · PLCs on the factory floor · employees' personal phones with the email app ¶  A BYOD · B IoT · C OT · D corporate · E guest
    - [=] debca | d e b c a | d,e,b,c,a
    - *Each trust level gets its own VLAN and firewall policy. OT is the most isolated, since safety and availability matter most there. Guests get internet only.*
    - @4.1.seg
25. Match each to its compliance item. Type the letters in order, e.g. abcd. ¶  An online shop storing card numbers · a US firm with EU customers' emails · a rule that data must stay in-country · a yearly independent assessor's review ¶  A GDPR · B compliance audit · C data locality · D PCI DSS
    - [=] dacb | d a c b | d,a,c,b
    - *Cards = PCI DSS. EU personal data = GDPR, wherever the company is. In-country = data locality. The independent review = compliance audit.*
    - @4.1.comp
26. Match prevent or detect to each. Type the letters in order, e.g. aaaaa. ¶  CCTV · a mantrap vestibule · a motion sensor · a badge reader · a locked rack ¶  A prevent · B detect
    - [=] babaa | b a b a a | b,a,b,a,a
    - *Notices it = detect (CCTV, motion sensors). Stops entry = prevent (vestibule, badges, locks). Cameras also deter.*
    - @4.1.phys
27. Which fail modes fit the emergency exit on a stairwell and the vault holding backup tapes, in that order?
    - **[x] Fail-safe, then fail-secure**  - [ ] Fail-secure, then fail-safe  - [ ] Fail-safe for both  - [ ] Fail-secure for both
    - *Exit routes = fail-safe (open), because life safety comes first. Asset stores with no one inside = fail-secure (stay locked).*
    - @4.1.phys
28. Monitoring shows: ¶  10.99.0.50 fileshare "FIN-PAYROLL" - login attempt from 10.1.4.77 ¶The share has no real users and exists only to be monitored. What is the share, and what should you investigate?
    - **[x] A honeypot; the host 10.1.4.77**  - [ ] A honeypot; the file server 10.99.0.50  - [ ] A honeynet; the payroll team  - [ ] A screened subnet; the firewall logs
    - *Any touch on a honeypot is suspicious, so 10.1.4.77 is likely compromised and scanning for data. Isolate and investigate it.*
    - @4.1.dcpt

### Key facts
- **CIA = confidentiality (encryption) · integrity (hashes) · availability (redundancy). Threat = actor · vulnerability = weakness · exploit = the technique · risk = likelihood × impact. Insider threat = has legitimate access.**
- **Physical: cameras detect and deter · locks, badges and vestibules prevent · fail-safe = opens (people) · fail-secure = stays locked (assets).**
- **Deception: honeypot = one decoy · honeynet = many decoys · any touch = an alert.**
- **PCI DSS = card data · GDPR = EU personal data, anywhere · data locality = stays in-country (drives cloud region) · audit = checks against a standard.**
- **Segment: IoT · IIoT · SCADA (wide area) within ICS within OT · guest (internet only) · BYOD.**

## Test 24 - 4.2 Attacks (26 Q)

1. An attack where MANY compromised systems flood one target?
   - [ ] SYN flood from one host  - [ ] MitM  - [ ] ARP spoofing  - **[x] DDoS**
   - *DDoS (Distributed Denial of Service) = a botnet of thousands of hosts overwhelming bandwidth, state tables or applications. DoS = one source. Reflected/amplified DDoS = small spoofed requests to DNS or NTP servers produce huge replies aimed at the victim. It hits the A in CIA (availability).*
   - @4.2.att ~18.5
2. Match each to its attack. Type the letters in order, e.g. abc. ¶  One host sends a SYN flood · a 50,000-device botnet floods a website · spoofed 60-byte DNS queries trigger 3,000-byte replies to the victim ¶  A DoS · B amplification · C DDoS
   - [=] acb | a c b | a,c,b
   - *A single source = A DoS. Many sources = C DDoS. A small request producing a big reflected reply = B amplification (reflection). Mitigations: ISP or cloud scrubbing, rate limiting, CDNs (Content Delivery Networks).*
   - @4.2.att
3. A technique that bypasses VLAN segmentation by sending traffic tagged for a VLAN the attacker isn't in?
   - [ ] VLAN pivoting  - [ ] VLAN ID collision  - **[x] VLAN hopping**  - [ ] VLAN spoofing
   - *VLAN hopping: (1) switch spoofing = pretending to be a switch so DTP (Dynamic Trunking Protocol) forms a trunk; (2) double tagging = an outer tag for the native VLAN and an inner tag for the target. Defences: switchport mode access and nonegotiate, and a native VLAN that's unused and not VLAN 1.*
   - @4.2.att ~18.6
4. An attacker floods a switch with frames from thousands of fake source MACs until it broadcasts every frame to all ports. Attack?
   - [ ] ARP spoofing  - **[x] MAC flooding**  - [ ] ARP poisoning  - [ ] MAC spoofing
   - *MAC flooding = fill the CAM (Content Addressable Memory) table, so the switch fails open like a hub and the attacker can sniff everyone's traffic. Defence: port security, limiting the MACs per port.*
   - @4.2.att ~18.7
5. Which protocol finds the MAC address for a known IP on the local subnet?
   - **[x] ARP**  - [ ] RARP  - [ ] DNS  - [ ] DHCP
   - *ARP (Address Resolution Protocol) = the broadcast "who has 192.168.1.1?", answered with the MAC. It has NO authentication: any host can reply, which is why spoofing works. IPv6 uses NDP (Neighbor Discovery Protocol) instead.*
   - @4.2.att ~18.8
6. The table in a host's memory mapping IP addresses to MAC addresses is the:
   - [ ] CAM table  - **[x] ARP cache**  - [ ] Routing table  - [ ] DNS cache
   - *ARP cache = view it with arp -a. Entries age out after minutes. The switch's MAC table (CAM) is different: it maps MAC → port.*
   - @4.2.att ~18.9
7. An attacker sends fake ARP replies saying the gateway's IP maps to the attacker's MAC. What is the act of sending them?
   - [ ] MAC spoofing  - [ ] MAC flooding  - **[x] ARP spoofing**  - [ ] DNS spoofing
   - *ARP spoofing = the act: forged replies (gratuitous ARP). ARP poisoning = the result: victims' caches now hold the wrong mapping, so their traffic flows via the attacker (on-path). Defence: DAI (Dynamic ARP Inspection) using DHCP snooping bindings.*
   - @4.2.att ~18.10
8. A device's ARP cache holds incorrect IP-to-MAC mappings planted by an attacker. Term?
   - [ ] IP conflict  - [ ] MAC table corruption  - **[x] ARP poisoning**  - [ ] Rogue DHCP
   - *Answer: ARP poisoning. Poisoning = the corrupted cache. Hook: SPOOFING is sending the lie, POISONING is the lie sitting in the cache.*
   - @4.2.att ~18.11
9. Remapping a domain to a rogue IP inside a DNS resolver's CACHE, affecting everyone using it?
   - **[x] DNS poisoning**  - [ ] DNS rebinding  - [ ] DNS spoofing of one reply  - [ ] DNS tunnelling
   - *DNS cache poisoning = corrupt the resolver so every client gets the fake IP until the TTL (Time To Live) expires. Defence: DNSSEC (DNS Security Extensions) signatures, and randomised source ports and transaction IDs.*
   - @4.2.att ~18.12
10. Intercepting a DNS query and replying with a forged answer before the real server does?
    - [ ] DNS tunnelling  - **[x] DNS spoofing**  - [ ] DNS rebinding  - [ ] DNS poisoning of the resolver cache
    - *DNS spoofing = the forged reply to a victim, often from an on-path position. Poisoning = that lie stored in a cache. The objectives list both.*
    - @4.2.att ~18.13
11. After a contractor visits, PCs on one floor randomly receive a 10.99.x.x address with a strange gateway and DNS, and some report duplicate IPs. What is most likely to blame?
    - [ ] DNS server failure  - [ ] Rogue AP  - [ ] A disabled DHCP relay  - **[x] A rogue DHCP server**
    - *An unauthorised DHCP server, such as a home router plugged into the LAN, races the real one and hands out bad settings. DHCP snooping on the switches allows offers only from trusted ports.*
    - @4.2.att ~18.14
12. What is an evil twin?
    - **[x] A rogue AP using a real SSID to intercept users**  - [ ] Two legitimate APs sharing the same channel  - [ ] A backup DHCP server handing out leases  - [ ] A mirrored switch port sending copies of traffic
    - *Evil twin = a spoofed SSID, often stronger or near the victims, sometimes with a deauthentication attack to push clients over. A rogue AP = any unauthorised AP plugged into your network. Defences: WIPS (Wireless Intrusion Prevention System), 802.1X with certificate validation, WPA3.*
    - @4.2.att ~18.15
13. Which describe an ON-PATH attack? (Select 3)
    - **[x] The attacker sits between two parties and intercepts traffic**  - **[x] It can modify packets in transit**  - **[x] It can impersonate one party to the other**  - [ ] It always needs physical access  - [ ] It only works if a device is already compromised
    - *On-path (formerly MitM, man-in-the-middle) = achieved by ARP poisoning, a rogue DHCP server, an evil twin or DNS spoofing. Defence: encryption with authentication (TLS with valid certificates, SSH, IPsec), so the interceptor can't read or alter traffic unnoticed.*
    - @4.2.att ~18.16
14. A crafted email that pretends to be from IT and asks you to "verify your password" is:
    - [ ] Spoofing only  - **[x] Phishing**  - [ ] Smishing  - [ ] Pharming
    - *Phishing = a fraudulent message luring you into giving credentials or running malware. Spear phishing = targeted at one person. Whaling = executives. Smishing = SMS. Vishing = voice. Pharming = DNS-based redirection.*
    - @4.2.soc ~18.17
15. Dumpster diving is:
    - **[x] Searching rubbish for discarded documents or media**  - [ ] Recovering deleted files from a used hard disk  - [ ] Driving around scanning for open Wi-Fi networks  - [ ] Watching over someone's shoulder as they type
    - *Defences: cross-cut shredders, locked disposal bins, and media destruction policies for drives and tapes.*
    - @4.2.soc ~18.18
16. A privacy filter that narrows a screen's viewing angle counters:
    - [ ] Screen scraping  - [ ] Spear phishing  - [ ] Pharming  - **[x] Shoulder surfing**
    - *Shoulder surfing = watching someone type or read, in a café, train or open office. Defences: privacy filters, screen positioning, and hiding PIN entry.*
    - @4.2.soc ~18.19
17. A visitor walks close behind an employee and slips through the secure door before it closes, without the employee noticing. What is this called?
    - **[x] Tailgating**  - [ ] Shoulder surfing  - [ ] Piggybacking  - [ ] Phishing
    - *Tailgating means entering behind an authorised person without their knowledge or consent. Piggybacking is the same move done with their consent. Access control vestibules and staff awareness reduce both.*
    - @4.2.soc ~18.20
18. Collective term for software that disrupts systems, steals data or gains access?
    - [ ] Spyware  - [ ] Adware  - **[x] Malware**  - [ ] Ransomware
    - *Malware = the umbrella: viruses, worms, trojans, ransomware, spyware, rootkits, keyloggers, bots. The objectives just list "malware", so know the main types.*
    - @4.2.soc ~18.21
19. Standalone malware that spreads across the network by itself, eating bandwidth?
    - **[x] Worm**  - [ ] Fileless virus  - [ ] Bot  - [ ] Logic bomb
    - *Worm = self-propagating with no user action, e.g. WannaCry over SMB (Server Message Block, TCP 445). Virus = needs a host file and a user action. Trojan = disguised as legitimate software. Ransomware = encrypts data and demands payment. Logic bomb = triggers on a condition.*
    - @4.2.soc ~18.22
20. Customers typing the bank's URL land on a lookalike login page because the resolver returns an attacker's address. Which attack is this, and what DNS extension validates responses?
    - [ ] ARP spoofing, fixed with DHCP snooping  - **[x] DNS poisoning, mitigated with DNSSEC**  - [ ] Evil twin, fixed with WPA3  - [ ] MAC flooding, fixed with port security
    - *DNS cache poisoning inserts false records into a resolver. DNSSEC adds digital signatures so resolvers can check that answers really came from the zone owner and were not altered.*
    - @4.2.att ~28.20
21. Users on 192.168.1.0/24 report traffic stalls. On one PC you run: ¶  C:\> arp -a ¶  Internet Address   Physical Address ¶  192.168.1.1        a4-5e-60-0c-11-9d ¶  192.168.1.40       a4-5e-60-0c-11-9d ¶  192.168.1.52       a4-5e-60-0c-11-9d ¶Which attack is shown, and which switch feature defends against it?
    - **[x] ARP spoofing / poisoning; Dynamic ARP Inspection**  - [ ] MAC flooding; port security  - [ ] Rogue DHCP; DHCP snooping  - [ ] IP conflict; a DHCP reservation
    - *Several IPs, including the gateway, resolving to one MAC means a host is claiming to be all of them in order to sit on-path. DAI (Dynamic ARP Inspection) checks ARP replies against DHCP snooping bindings and drops forged ones.*
    - @4.2.att ~29.11
22. Match each attack to its defence. Type the letters in order, e.g. abcde. ¶  MAC flooding · a rogue DHCP server · ARP poisoning · DNS cache poisoning · a rogue switch plugged into an access port ¶  A DNSSEC · B port security · C BPDU guard · D DAI · E DHCP snooping
    - [=] bedac | b e d a c | b,e,d,a,c
    - *Limit MACs = port security. Trusted DHCP ports only = DHCP snooping. Validate ARP = DAI. Signed records = DNSSEC. BPDU (Bridge Protocol Data Unit) arrives = BPDU guard err-disables the port.*
    - @4.2.att
23. Match each to its attack. Type the letters in order, e.g. abcde. ¶  A frame with two 802.1Q tags reaches a VLAN it shouldn't · the switch CAM table fills and it starts flooding · "CoffeeShop_WiFi" appears twice with different BSSIDs · clients get gateway 192.168.0.1 instead of 10.1.1.1 · the attacker relays and reads traffic between a PC and its gateway ¶  A rogue DHCP · B evil twin · C on-path · D VLAN hopping · E MAC flooding
    - [=] debac | d e b a c | d,e,b,a,c
    - *Double tagging = VLAN hopping. A full CAM table = MAC flooding. Same SSID, different BSSID = evil twin. The wrong gateway from DHCP = rogue DHCP. In between reading traffic = on-path.*
    - @4.2.att
24. Match each to its social engineering attack. Type the letters in order, e.g. abcd. ¶  A stranger walks in behind a staff member through a badge door · someone reads a password off a screen on the train · printed network diagrams are found in the recycling · a "delivery failed" email with a login link ¶  A phishing · B tailgating · C dumpster diving · D shoulder surfing
    - [=] bdca | b d c a | b,d,c,a
    - *Behind someone through a door = tailgating. Watching a screen = shoulder surfing. The recycling bin = dumpster diving. A fake login email = phishing.*
    - @4.2.soc
25. Match each to its malware type. Type the letters in order, e.g. abcd. ¶  Spreads across SMB with no user action · a "free game" installs a backdoor · encrypts files and demands bitcoin · infects a document and spreads when someone opens it ¶  A virus · B ransomware · C worm · D trojan
    - [=] cdba | c d b a | c,d,b,a
    - *No user action = worm. Disguised as something wanted = trojan. Encrypts and demands payment = ransomware. Needs a host file and a user action = virus.*
    - @4.2.soc
26. PBQ: Harden access switch SW5 after an audit.
    - [p] Findings: a user plugged in a home router and handed out rogue IPs. Control :: A DHCP snooping · B DAI · C BPDU guard · D port security = a
    - [p] A host poisoned other hosts' ARP caches :: A DHCP snooping · B DAI · C BPDU guard · D port security = b
    - [p] A lobby port should only ever allow the one kiosk. Type the port-security maximum MAC count = 1
    - [p] Telnet is enabled on the VTY lines. Type the command under line vty 0 15 that allows only SSH = transport input ssh
    - *DHCP snooping trusts only uplink ports to send DHCP offers, killing rogue servers. DAI (Dynamic ARP Inspection) checks ARP against the snooping table. BPDU guard err-disables an access port that receives BPDUs. Port security limits MACs: maximum 1, sticky, shutdown on violation. transport input ssh drops Telnet.*
    - @4.3.hard

### Key facts
- **DoS = one source · DDoS = botnet · amplification = small spoofed request, huge reply.**
- **VLAN hopping = switch spoofing (DTP) or double tagging · MAC flooding = fill the CAM, switch floods like a hub · ARP spoofing = sending lies → ARP poisoning = lies in the cache (on-path). ARP cache: arp -a.**
- **DNS spoofing = forged reply · DNS poisoning = corrupted resolver cache → DNSSEC. Rogue DHCP → DHCP snooping · ARP → DAI · MAC flooding → port security · rogue switch → BPDU guard.**
- **Rogue AP = unauthorised AP on your LAN · evil twin = copied SSID · on-path (MitM) = relay and read/alter; stop it with authenticated encryption.**
- **Social: phishing (spear, whaling, smishing, vishing) · dumpster diving · shoulder surfing · tailgating (no consent) vs piggybacking (with consent). Malware: worm self-spreads · virus needs a host · trojan disguised · ransomware encrypts.**

## Test 25 - 4.3 Defences (28 Q)

1. You are preparing a baseline build for finance desktops. Which steps harden them? (Select 3)
   - **[x] Applying OS and application security updates on a schedule**  - **[x] Disabling or uninstalling services and software that are not needed**  - **[x] Restricting access that requires no authentication**  - [ ] Only renaming the local administrator account  - [ ] Blocking all internet connectivity permanently
   - *Hardening shrinks the attack surface: patch, remove what is not used, and require authentication. Renaming an account alone is weak obscurity, and blocking all internet access is not practical for normal work.*
   - @4.3.hard ~18.23
2. Which are router/switch HARDENING techniques? (Select 3)
   - **[x] Change the default credentials**  - **[x] Disable unused ports and services**  - **[x] Keep the firmware updated**  - [ ] Change the device's hostname  - [ ] Disable SSID broadcast
   - *The objectives: disable unused ports and services, change default passwords. Also: SSH instead of Telnet, SNMPv3, a management ACL, logging to syslog, a login banner. A hostname change isn't security.*
   - @4.3.hard ~18.24
3. Why must default usernames and passwords be changed?
   - **[x] They're publicly documented and the first thing attackers try**  - [ ] They expire automatically after 30 days anyway  - [ ] They're stored in cleartext, unlike changed passwords  - [ ] Vendors void the warranty if they aren't changed
   - *admin/admin, cisco/cisco and the like are in every manual and in the Mirai botnet's wordlist. Change them before the device is connected to the network.*
   - @4.3.hard ~18.25
4. An audit notes that spare switch ports are shut down and placed in VLAN 999, which has no routing. What is this practice meant to achieve?
   - **[x] Preventing someone from plugging in and gaining network access**  - [ ] Freeing bandwidth for active ports  - [ ] Saving PoE budget for other ports  - [ ] Stopping broadcast storms from spreading
   - *A disabled port in a dead-end parking VLAN gives nothing to someone who plugs in, and even if the port is re-enabled by mistake it still reaches nothing. Pair it with 802.1X for active ports.*
   - @4.3.hard ~24.15
5. Type the IOS interface command that disables a port.
   - [=] shutdown | shut
   - *shutdown = administratively down, which shows as "administratively down" in show interfaces. no shutdown re-enables it. For many ports: interface range g0/10 - 24, then shutdown.*
   - @4.3.hard
6. A host is meant to serve only HTTPS. You run: ¶  C:\> netstat -an ¶  TCP    0.0.0.0:3389    LISTENING ¶  TCP    0.0.0.0:443     LISTENING ¶  TCP    0.0.0.0:23      LISTENING ¶Type the listening port that poses the greatest security risk.
   - [=] 23
   - *Port 23 is Telnet, which sends credentials and sessions in cleartext, so disable it. 3389 (RDP) also is not needed for a web-only role and should be restricted, but cleartext Telnet is the worst exposure. 443 is the expected service.*
   - @4.3.hard ~29.12
7. "Port security" can refer to:
   - [ ] Port-based NAC with 802.1X  - [ ] Sticky MAC learning on access ports  - [ ] MAC address limits and filtering on switch ports  - **[x] All of the above**
   - *Answer: All of the above. The term is used loosely. On a Cisco switch, "port security" specifically means limiting and learning MACs per port. NAC (Network Access Control) = deciding who and what may connect.*
   - @4.3.nac ~19.1
8. A kiosk switch port should accept frames only from the single kiosk PC's hardware address and shut down if anything else appears. Which feature does this?
   - [ ] BPDU guard  - **[x] Port security**  - [ ] DHCP snooping  - [ ] LACP
   - *Port security limits the MAC addresses allowed on a port, either sticky or static, and takes a violation action such as shutdown. BPDU guard protects STP, and DHCP snooping filters DHCP offers.*
   - @4.3.nac ~28.18
9. You want switches to hold a port closed until the connecting device proves its identity to a RADIUS server. Which IEEE standard is this?
   - [ ] 802.1Q  - **[x] 802.1X**  - [ ] 802.3af  - [ ] 802.1D
   - *802.1X port-based access control has three parts: the supplicant (the client), the authenticator (the switch or AP) and the authentication server (RADIUS). Hook: X marks the authentication. 802.1Q is VLAN tagging.*
   - @4.3.nac ~19.2
10. What are the 802.1X roles of the device, the switch or AP, and the RADIUS server, in that order?
    - **[x] Supplicant, authenticator, authentication server**  - [ ] Authenticator, supplicant, authentication server  - [ ] Client, controller, directory  - [ ] Supplicant, authentication server, authenticator
    - *Supplicant = asks to join. Authenticator = the gatekeeper that relays. Authentication server = decides. Hook: the Supplicant Supplicates, the Authenticator guards the door, the Server says yes or no.*
    - @4.3.nac
11. Access control that uses each NIC's 48-bit hardware address to decide who may connect?
    - [ ] Rule-based access control  - **[x] MAC address filtering**  - [ ] 802.1X  - [ ] RBAC
    - *MAC filtering = an allow or deny list of MACs on a switch or AP. It's easy to set up but easy to defeat.*
    - @4.3.nac ~19.3
12. A small office secures its Wi-Fi by allowing only an approved list of device hardware addresses. What is the main weakness of this approach?
    - [ ] It requires 802.1X  - [ ] It blocks all guests  - **[x] MAC addresses are easily spoofed**  - [ ] It only works on 5 GHz
    - *MAC addresses are sent in the clear and are easy to change, so an attacker sniffs an allowed one and copies it. Use WPA3 with strong authentication instead of relying on MAC filtering.*
    - @4.3.hard ~24.14
13. A visitor connects a laptop to a lobby wall jack and immediately reaches internal servers. Which two measures prevent a repeat? (Select 2)
    - **[x] Disable switch ports that are not in use**  - **[x] Require 802.1X authentication on access ports**  - [ ] Enable jumbo frames  - [ ] Move the DNS server
    - *A disabled port gives nothing to someone who plugs in, and 802.1X NAC blocks unknown devices on live ports. Port security and a parking VLAN add further layers.*
    - @4.3.nac ~28.17
14. Why is key management listed under NAC and defences?
    - **[x] Keys must be stored, rotated and revoked securely, or 802.1X fails**  - [ ] Keys are only used for Wi-Fi, which NAC controls  - [ ] Key management replaces passwords for all users  - [ ] It covers the physical door keys to the server room
    - *Key management = the key and certificate lifecycle: generation, secure storage (an HSM, Hardware Security Module, or a TPM, Trusted Platform Module), distribution, rotation, expiry and revocation. An expired RADIUS server certificate = nobody can join the Wi-Fi.*
    - @4.3.nac
15. The ordered permit/deny rule list on a router or firewall, filtering by IP, port and protocol, is an:
    - **[x] ACL**  - [ ] NAC  - [ ] RBAC  - [ ] UTM
    - *ACL (Access Control List) = rules checked TOP-DOWN, first match wins, with an implicit deny at the end. Standard ACLs filter by source IP only; extended ACLs by source, destination, protocol and port.*
    - @4.3.rule
16. Blocking or allowing sites based on the web address?
    - [ ] Domain blocklisting at the router only  - **[x] URL filtering**  - [ ] Stateful inspection  - [ ] Content filtering
    - *URL (Uniform Resource Locator) filtering = category and blocklist of web addresses, e.g. block "gambling", via a proxy, NGFW (Next-Generation Firewall) or DNS filter.*
    - @4.3.rule ~19.4
17. A firewall feature scans traffic for banned words, blocked file types like .exe, or known malicious patterns. What is this?
    - [ ] Packet filtering  - [ ] Stateful inspection  - **[x] Content filtering**  - [ ] URL filtering
    - *Content filtering looks inside the payload. Packet filtering checks only header fields such as IP and port, stateful inspection tracks connections, and URL filtering decides by web address or category.*
    - @4.3.rule ~19.5
18. One appliance protecting against many threat types: firewall, IPS, antivirus, filtering and VPN?
    - [ ] IDP  - [ ] AV  - **[x] UTM**  - [ ] A plain packet filter
    - *UTM (Unified Threat Management) = the all-in-one box, typical for SMBs (small and medium businesses). An NGFW is similar but focuses on application-aware firewalling. IPS = Intrusion Prevention System.*
    - @4.3.rule ~19.6
19. When drawing firewall zones for a company, which areas would normally be labelled as trusted? (Select 3)
    - **[x] The internal corporate LAN**  - **[x] The on-premises server network**  - **[x] The intranet**  - [ ] The internet  - [ ] The guest network  - [ ] Public Wi-Fi
    - *Trusted zones are internal networks the organisation controls. Even so, zero trust says internal traffic should still be verified rather than trusted automatically. The internet, guest networks and public Wi-Fi carry unmanaged users, so they are untrusted.*
    - @4.3.zone ~19.7
20. Which segments should a firewall policy treat as untrusted? (Select 3)
    - **[x] The internet**  - **[x] Guest networks**  - **[x] Public Wi-Fi hotspots**  - [ ] The intranet  - [ ] The internal LAN
    - *Untrusted means you do not control the users or devices there. Filter traffic from those zones strictly, and put public-facing servers in a screened subnet (DMZ) between untrusted and trusted zones.*
    - @4.3.zone ~19.8
21. A lightly protected subnet holding public-facing servers, between the internet and the internal firewall?
    - [ ] Captive portal  - [ ] Quarantine VLAN  - [ ] Extranet  - **[x] Screened subnet**
    - *Screened subnet (formerly DMZ, demilitarised zone) = web, mail and DNS servers the internet may reach. If one is breached, the internal firewall still blocks the way to the LAN.*
    - @4.3.zone ~19.9
22. A screened subnet is best described as:
    - **[x] A semi-trusted buffer between inside and outside**  - [ ] A fully trusted zone, the same as the LAN  - [ ] The same thing as a guest Wi-Fi network  - [ ] An unfiltered zone outside the firewall
    - *Rules: internet → DMZ web on 443 only · DMZ → LAN almost nothing (e.g. only the database port to one server) · LAN → DMZ for management. Never let the internet reach the LAN directly.*
    - @4.3.zone ~19.10
23. Firewall ACL, top to bottom: ¶  FW1# show access-lists ¶  1  deny   ip   any  any ¶  2  permit tcp  any  host 10.1.1.10 eq 443 ¶Nobody can reach the web server. Type the rule number that must move to the top.
    - [=] 2 | rule 2
    - *ACLs are first-match. Rule 1 denies everything before rule 2 is ever checked. Put the specific permits first, and let the implicit (or explicit) deny sit at the bottom.*
    - @4.3.rule
24. Match each need to a control. Type the letters in order, e.g. abcde. ¶  Only authenticated domain devices may use any wall port · a lobby port allows exactly one known kiosk MAC · block gambling sites · block .exe downloads and card numbers leaving · host the public web server away from the LAN ¶  A 802.1X · B URL filtering · C port security · D screened subnet · E content filtering
    - [=] acbed | a c b e d | a,c,b,e,d
    - *Authentication per port = 802.1X. One known MAC = port security. By address = URL filtering. Inside the traffic = content filtering. Public servers = screened subnet.*
    - @4.3.rule
25. Match each to its zone. Type the letters in order, e.g. aaaaa. ¶  The internet · the staff LAN · the public mail relay · the guest Wi-Fi · the intranet file server's VLAN ¶  A trusted · B untrusted · C screened subnet
    - [=] bacba | b a c b a | b,a,c,b,a
    - *The internet and guests = untrusted. The staff LAN and internal servers = trusted. Public-facing servers = the screened subnet.*
    - @4.3.zone
26. PBQ: DMZ firewall. ¶  INTERNET ¶    │ ¶  FW-EDGE  outside 203.0.113.2 ¶    ├── DMZ 172.16.10.0/24 ¶    │     WEB   172.16.10.10 ¶    │     MAIL  172.16.10.25 ¶    └── INSIDE 10.10.0.0/16 ¶          IT     10.10.20.0/24 ¶          Staff  10.10.30.0/24 ¶Requirements. Rules are processed top-down, first match wins: ¶  R1 anyone may reach WEB over HTTPS only ¶  R2 anyone may deliver mail to MAIL ¶  R3 only IT may SSH to the DMZ servers ¶  R4 Staff must NOT SSH to the DMZ ¶  R5 everything else is blocked ¶Rule table. Each (n) is a blank you fill in: ¶  #  SOURCE         DEST             PROTO  PORT  ACTION ¶  1  any            (1)              TCP    (2)   permit ¶  2  any            172.16.10.25     TCP    (3)   permit ¶  3  (4)            172.16.10.0/24   TCP    22    permit ¶  4  any            any              any    any   deny ¶Fill the blanks so the table meets R1 to R5.
    - [p] Blank (1): rule 1 DEST, which IP = 172.16.10.10
    - [p] Blank (2): rule 1 PORT = 443
    - [p] Blank (3): rule 2 PORT = 25
    - [p] Blank (4): rule 3 SOURCE, network plus prefix like 10.9.9.0/24 = 10.10.20.0/24 | 10.10.20.0 255.255.255.0
    - [p] An admin adds permit 10.10.0.0/16 → 172.16.10.0/24 TCP 22 ABOVE rule 3. Which requirements does this break :: A R3 only · B R4 only · C R3 and R4 · D none, rule 3 still matches = c
    - *HTTPS = TCP 443, and only to WEB: a /24 destination would expose MAIL too. Server-to-server SMTP = TCP 25 (587 is client submission). Least privilege: IT's /24, not the whole /16. The final explicit deny mirrors the implicit deny and gives logging. A /16 permit above rule 3 includes Staff's 10.10.30.0/24, and first match wins, so Staff can SSH (R4 breaks) and IT is no longer the ONLY group (R3 breaks). A STATEFUL firewall tracks sessions and allows replies automatically. A stateless one, like a router ACL or a cloud network ACL, needs an explicit rule for the return traffic.*
    - @4.3.rule
27. PBQ: ACL LAN-IN is applied inbound on R1's LAN interface. ¶  R1# show access-lists ¶  Extended IP access list LAN-IN ¶  10 permit tcp 10.1.1.0 0.0.0.255 any eq 443 ¶  20 deny   tcp any any eq 23 ¶  30 permit tcp host 10.1.1.50 any eq 22 ¶  40 deny   tcp 10.1.1.0 0.0.0.255 any eq 22 ¶  50 permit udp any any eq 53 ¶  (implicit deny any, not shown by IOS) ¶For each flow, type the sequence number of the line that matches, or 0 for the implicit deny.
    - [p] 10.1.1.9 to a web server on TCP 443 = 10
    - [p] 10.1.1.50 SSH to a router on TCP 22 = 30
    - [p] 10.1.1.60 SSH to a router on TCP 22 = 40
    - [p] 10.1.1.9 pings 8.8.8.8 = 0
    - [p] 10.1.1.50 Telnets to a switch on TCP 23 = 20
    - *Top-down, first match wins. .9 HTTPS hits 10. .50 SSH hits 30 before the deny at 40, since order matters. .60 SSH skips 30 (not host .50) and hits 40. DNS hits 50. Ping is ICMP and matches no line, so the implicit deny drops it. .50 Telnet hits 20 first: denied, even though line 30 trusts .50 for SSH.*
    - @4.3.rule
28. An administrator isolates an IIoT device on its own VLAN. Which device is it most likely?
    - **[x] An irrigation pump**  - [ ] A laser printer  - [ ] An LCD projector  - [ ] A core router  - [ ] A hypervisor
    - *Answer: An irrigation pump. IIoT (Industrial IoT) = connected industrial and OT machinery: pumps, valves, sensors, PLCs. Printers and projectors are ordinary office IoT; routers and hypervisors are IT infrastructure. Segment IIoT because it's rarely patchable. Hook: IIoT = things that move water, oil or factory parts.*
    - @4.3.seg

### Key facts
- **Hardening: patch, disable unused ports and services, change defaults, SSH not Telnet, SNMPv3, parking VLAN + shutdown.**
- **Port security = MAC limit per port (sticky, violation shutdown/restrict/protect) · 802.1X = supplicant, authenticator, RADIUS server · MAC filtering = easily spoofed · key management = key and cert lifecycle.**
- **ACL = top-down, first match, implicit deny · URL filtering = where you're going · content filtering = what's inside · UTM = all-in-one.**
- **Trusted = LAN, intranet · untrusted = internet, guest, public Wi-Fi · screened subnet (DMZ) = public servers, a semi-trusted buffer.**

## Test 26 - 5.1 Troubleshoot Method (25 Q)

1. The VERY FIRST troubleshooting step?
   - **[x] Identify the problem**  - [ ] Establish a theory of probable cause  - [ ] Establish a plan of action  - [ ] Verify full system functionality
   - *Step 1: gather information, question users, identify symptoms, determine what changed, duplicate the problem if possible, and approach multiple problems individually. No guessing yet.*
   - @5.1.meth ~19.11
2. A help desk tech is still in the identify-the-problem stage for a user's dropped VPN. Which activities belong to LATER steps instead? (Select 2)
   - **[x] Drawing up a plan of action to fix it**  - **[x] Proposing a likely cause to test**  - [ ] Asking the user what they see  - [ ] Checking what changed recently  - [ ] Reproducing the issue
   - *Identify the problem means gathering information: question users, find out what changed, identify symptoms, reproduce the issue and back up first. Forming a theory is step 2, and the plan of action is step 4.*
   - @5.1.meth ~19.12
3. A tech calls the reporting user and asks when the outage began and what they were doing at the time. Which troubleshooting step is under way?
   - [ ] Establish a plan of action  - [ ] Document findings  - **[x] Identify the problem**  - [ ] Establish a theory
   - *Interviewing users is information gathering, which is part of step 1, along with identifying symptoms, determining recent changes and duplicating the problem.*
   - @5.1.meth ~19.17
4. Type the step NUMBER for establishing a theory of probable cause.
   - [=] 2
   - *Step 2 = theory: question the obvious, and choose an approach (top-to-bottom, bottom-to-top, divide and conquer). You can use several approaches.*
   - @5.1.meth ~19.13
5. A user says one web app shows an error page. Working down from the OSI layer closest to the user, where does a tech begin?
   - [ ] Physical  - [ ] Network  - [ ] Transport  - **[x] Application**
   - *Top-to-bottom starts at Layer 7, the application, and works down. It suits software-looking symptoms. Bottom-to-top begins with cables and link lights.*
   - @5.1.meth ~19.14
6. A desktop shows no link light after being moved to a new desk. Which OSI troubleshooting approach fits a suspected physical fault best?
   - [ ] Top-to-bottom  - [ ] Divide and conquer  - [ ] Follow the path  - **[x] Bottom-to-top**
   - *Bottom-to-top starts at Layer 1 with cabling, ports and power, then moves up. It is the natural choice when hardware is the likely culprit.*
   - @5.1.meth ~19.15
7. An engineer starts by checking whether the host can reach the gateway by IP. If it can, they look higher in the stack, and if not, lower. What approach is this?
   - [ ] Top-to-bottom  - [ ] Bottom-to-top  - **[x] Divide and conquer**  - [ ] Question the obvious
   - *Divide and conquer begins in the middle of the OSI model, often at Layer 3 with ping, and uses the result to decide which half to search next, saving time on both ends.*
   - @5.1.meth ~25.9
8. Before opening Wireshark on a "dead" printer, a tech glances at whether its power light is on and the cable is seated. Which part of the methodology is this?
   - [ ] Escalate  - **[x] Question the obvious**  - [ ] Document findings  - [ ] Duplicate the problem
   - *Question the obvious, part of establishing a theory, rules out simple causes such as power, cables and switches that are off before spending time on deep analysis.*
   - @5.1.meth ~25.10
9. Which of these belongs to some other step, not to forming a theory of probable cause?
   - [ ] Applying a top-to-bottom OSI approach  - [ ] Combining several approaches  - [ ] Checking the obvious first  - [ ] Applying a bottom-to-top OSI approach  - **[x] Handing the issue to a higher tier**
   - *Step 2 includes questioning the obvious and choosing OSI approaches. Escalation belongs to step 3, when a theory is not confirmed, and step 5, when the fix is outside your authority.*
   - @5.1.meth ~19.16
10. A tech suspects a bad patch cable is causing a user's outage. What should they do next?
    - [ ] Verify full functionality  - **[x] Test the theory to determine the cause**  - [ ] Implement the solution  - [ ] Establish a plan of action
    - *After establishing a theory, test it, for example by swapping the cable. If confirmed, plan the fix. If not, form a new theory or escalate.*
    - @5.1.meth ~19.18
11. Swapping the suspected faulty cable did not fix the issue, so the tech comes up with a different idea or passes the ticket up. Which step are they in?
    - [ ] Establish a theory  - [ ] Identify the problem  - **[x] Test the theory to determine the cause**  - [ ] Establish a plan of action
    - *Step 3 tests the theory. When the test fails, the step tells you to establish a new theory or escalate.*
    - @5.1.meth ~19.19
12. Type the step NUMBER for establishing a plan of action and identifying potential effects.
    - [=] 4
    - *Step 4 = plan + potential effects: what else could this fix break? Does it need a change request and a maintenance window?*
    - @5.1.meth ~19.20,19.21
13. An engineer has written the plan to replace a failing core switch module. What comes next in the methodology? (Select 2)
    - **[x] Carry out the fix**  - **[x] Escalate if needed**  - [ ] Put preventive measures in place  - [ ] Test the theory
    - *Step 5 is to implement the solution or escalate as necessary, for example when the change needs another team's approval. Verifying and preventive measures follow in step 6.*
    - @5.1.meth ~19.22
14. When is the solution implemented? (Select 2)
    - **[x] After establishing a plan and identifying potential effects**  - **[x] Before verifying functionality and preventive measures**  - [ ] Before establishing a plan  - [ ] After documenting
    - *Implement = step 5: after plan (4), before verify (6).*
    - @5.1.meth ~19.24
15. In the CompTIA methodology, at what point do you confirm that everything works and add safeguards against a repeat?
    - [ ] After documenting findings, lessons learned, actions and outcomes  - [ ] At the very start, before any theory  - **[x] Right after implementing the solution**  - [ ] As the final step
    - *Step 6 is to verify full system functionality and, if applicable, implement preventive measures. It comes after the fix and before documentation, which is always last.*
    - @5.1.meth ~19.23
16. The tech has just finished the step that comes immediately before writing up the ticket. Which actions did that step include? (Select 2)
    - **[x] Confirming the whole system works**  - **[x] Adding measures to prevent recurrence**  - [ ] Applying the fix  - [ ] Weighing the possible effects of the change
    - *Step 6, verify functionality and apply preventive measures, comes right before step 7, documentation. Applying the fix and weighing effects come earlier.*
    - @5.1.meth ~19.25
17. What should the final stage of every troubleshooting effort consist of?
    - **[x] Recording findings, actions and outcomes**  - [ ] Putting preventive measures in place  - [ ] Applying the fix  - [ ] Confirming the system works fully
    - *Documenting is step 7. A record of the cause, the fix and the results helps the next tech and feeds the knowledge base.*
    - @5.1.meth ~20.1
18. On the same morning, accounting reports a jammed printer and the sales floor reports a sluggish wireless network. How should the tech proceed?
    - [ ] Assume one root cause  - **[x] Handle each problem separately**  - [ ] Escalate both immediately  - [ ] Reboot all network gear
    - *The methodology says to approach multiple problems individually. Linking unrelated symptoms wastes time, so open separate tickets and work through each one.*
    - @5.1.meth ~25.12
19. A user says "the internet is down." Best first question?
    - **[x] What exactly happens, and what changed recently?**  - [ ] Have you tried a new laptop?  - [ ] Which router model do you have?  - [ ] Can I reimage your PC?
    - *Identify: get specifics (one site? all sites? by name or by IP?) and recent changes. "Internet down" often turns out to be one website, or DNS.*
    - @5.1.meth
20. A fix works on the user's PC. Before closing the ticket, the tech checks other users on the same VLAN and adds a monitoring alert. Which step?
    - **[x] Verify functionality and implement prevention**  - [ ] Document findings, actions and outcomes  - [ ] Test the theory to determine the cause  - [ ] Establish a plan of action to fix it
    - *Step 6 = verify + prevent. Checking only the original PC isn't full functionality.*
    - @5.1.meth
21. Type the step number, 1-7, for each action, in order, separated by spaces. ¶  Applying the ACL fix in the maintenance window · "Did anything change yesterday?" · updating the change ticket · removing the ACL line in the lab confirms it · checking every VLAN can reach the server · "I bet it's the new ACL" · writing up the rollback and who's affected
    - [=] 5 1 7 3 6 2 4
    - *Apply = implement (5). Question = identify (1). Record = document (7). Confirming it = test (3). Check all = verify (6). A guess = theory (2). Rollback and impact = plan (4). Hook: I Take Tea, Pour It, Very Delicious = I 1 Identify · Take 2 Theory · Tea 3 Test · Pour 4 Plan · It 5 Implement · Very 6 Verify · Delicious 7 Document.*
    - @5.1.meth
22. Match each to its OSI approach. Type the letters in order, e.g. abc. ¶  A new cable was just run and the link light is off · only one web app shows an error while everything else works · no idea where to start, so ping first ¶  A bottom-to-top · B divide and conquer · C top-to-bottom
    - [=] acb | a c b | a,c,b
    - *Physical symptoms = bottom-up from Layer 1. App-specific symptoms = top-down from Layer 7. Unknown = divide and conquer from Layer 3.*
    - @5.1.meth
23. The theory "bad switch port" is tested: moving the PC to another port doesn't help. Which TWO options does the methodology allow next? (Select 2)
    - **[x] Establish a new theory**  - **[x] Escalate**  - [ ] Implement the port fix anyway  - [ ] Document and close the ticket  - [ ] Verify full system functionality
    - *Theory not confirmed = establish a new theory (the cable? the NIC? the VLAN?) or escalate. Don't implement a fix for a disproven cause.*
    - @5.1.meth
24. Type the step NUMBER, 1-7, where each happens, in order, separated by spaces: identify potential effects · question the obvious · duplicate the problem · lessons learned · implement preventive measures.
    - [=] 4 2 1 7 6
    - *Potential effects = plan (4). Question the obvious = theory (2). Duplicate = identify (1). Lessons learned = document (7). Preventive measures = verify (6). Hook: I Take Tea, Pour It, Very Delicious = I 1 Identify · Take 2 Theory · Tea 3 Test · Pour 4 Plan · It 5 Implement · Very 6 Verify · Delicious 7 Document.*
    - @5.1.meth
25. PBQ: A ticket: "Printer on floor 3 stopped working this morning." Put the CompTIA methodology steps in order, then classify two actions. ¶  A establish a theory of probable cause · B identify the problem · C test the theory · D establish a plan of action · E implement the solution or escalate · F verify full functionality and preventive measures · G document findings, actions and outcomes
    - [p] Type all 7 letters in order, first step first, e.g. gfedcba = bacdefg | b a c d e f g | b,a,c,d,e,f,g
    - [p] The tech asks users what changed since yesterday. Step :: A identify the problem · B test the theory · C verify · D document = a
    - [p] The tech checks that other floors can still print after the fix. Step :: A identify the problem · B establish a theory · C verify full functionality · D plan = c
    - *Identify (question users, find what changed, duplicate the problem), theory (question the obvious), test, plan, implement or escalate, verify plus preventive measures, then document. Asking what changed = identify. Checking everything works afterwards = verify. Hook: I Take Tea, Pour It, Very Delicious = I 1 Identify · Take 2 Theory · Tea 3 Test · Pour 4 Plan · It 5 Implement · Very 6 Verify · Delicious 7 Document.*
    - @5.1.meth

### Key facts
- **1 Identify (gather info, question users, symptoms, what changed, duplicate, multiple problems individually) · 2 Theory (question the obvious; top-down, bottom-up, divide and conquer) · 3 Test (confirmed → plan; not → new theory or escalate) · 4 Plan + potential effects · 5 Implement or escalate · 6 Verify + preventive measures · 7 Document findings, actions, outcomes, lessons learned.**
- **Hook: I Take Tea, Pour It, Very Delicious. Top-down = start at L7 · bottom-up = L1 (hardware) · divide and conquer = start at L3, e.g. ping.**

## Test 27 - 5.2 Cabling Issues (29 Q)

1. Single-mode fibre needs transceivers and connectors made for single-mode. Why?
   - **[x] SMF has a 9-micron core; MMF optics are built for 50 or 62.5, so light is lost**  - [ ] SMF runs at a different voltage from MMF, so the optics burn out  - [ ] Multimode is copper-based, so it can't carry light from SMF optics  - [ ] It doesn't matter: any fibre optic works with any fibre, just slower
   - *SMF (Single-Mode Fibre) = yellow jacket, 9 µm core, laser at 1310/1550 nm, kilometres. MMF (Multimode Fibre) = aqua/orange, 50/62.5 µm, LED or VCSEL (Vertical-Cavity Surface-Emitting Laser) at 850 nm, a few hundred metres. The optic, the fibre and the far end must all match.*
   - @5.2.cable ~20.2
2. A contractor patches multimode fibre into a 10 km campus link designed for single-mode optics. What can result?
   - [ ] Signal distortion  - [ ] Data errors  - [ ] Limited distance and high attenuation  - **[x] All of the above**
   - *Multimode suffers modal dispersion and higher loss over distance, so a long single-mode run fails or throws errors. Fibre type and optics must match the design.*
   - @5.2.cable ~20.3
3. Cat 5 cables are found on a Gigabit Ethernet link that keeps erroring. Fix?
   - **[x] Replace them with Cat 5e or higher**  - [ ] Leave them  - [ ] Shorten them  - [ ] Add repeaters on each run
   - *Cat 5 = 100 Mbps (100 MHz). Cat 5e = 1 Gbps at 100 m. Cat 6 = 1 Gbps at 100 m, 10 Gbps up to 55 m. Cat 6a = 10 Gbps at 100 m. Cat 8 = 25/40 Gbps up to 30 m.*
   - @5.2.cable ~20.4
4. A 50 m Cat 6 run carries 10 Gbps. What should you do?
   - **[x] Leave it: Cat 6 supports 10G up to 55 m**  - [ ] Extend it  - [ ] Add repeaters  - [ ] Replace it with Cat 6a immediately
   - *Cat 6 = 10GBASE-T up to about 55 m (37-55 depending on crosstalk). Beyond that you need Cat 6a.*
   - @5.2.cable ~20.5
5. Cat 8 carries 40 Gbps across a 100 m segment and fails. Best fix?
   - [ ] Switch to twinax  - [ ] Use repeaters  - **[x] Switch to fibre**  - [ ] Keep the current setup
   - *Answer: Switch to fibre. Cat 8 = 40 Gbps only up to 30 m, meant for data-centre patching. For 100 m at 40G, use fibre (40GBASE-SR4 on OM4 multimode reaches about 150 m, and single-mode goes much further). Twinax DAC (Direct Attach Copper) = under about 7 m.*
   - @5.2.cable ~20.6
6. A cable run passes next to elevator motors, so you choose twisted-pair copper that includes a foil screen to block interference. Which type is it?
   - [ ] Coax  - **[x] STP**  - [ ] UTP  - [ ] Twinax
   - *STP (Shielded Twisted Pair) adds foil or braid around the pairs and must be grounded to be effective. UTP relies on twisting alone.*
   - @5.2.cable ~20.7
7. Which statements are FALSE about UTP cable? (Select 3)
   - **[x] It has a foil shield to reduce interference**  - **[x] It is a type of coaxial cable**  - **[x] It cannot be affected by EMI**  - [ ] It uses twisted copper pairs  - [ ] It carries Ethernet and telephone signals  - [ ] It is inexpensive and easy to install
   - *UTP (Unshielded Twisted Pair) is cheap, common copper with no shield, so it is the most exposed to interference. Coax has a single centre conductor inside a shield, a different design. UTP's twists reduce interference but do not make it immune to EMI.*
   - @5.2.cable ~20.8
8. Why are the wires in twisted-pair cable twisted?
   - **[x] To cancel interference and crosstalk**  - [ ] To make the cable physically stronger  - [ ] To carry PoE without overheating  - [ ] To make the pairs easy to identify
   - *Twisting = each wire in a pair picks up the same noise, which cancels at the receiver (differential signalling). Each pair has a different twist rate, which cuts crosstalk between pairs. Untwisting too much at a termination causes NEXT (Near-End Crosstalk).*
   - @5.2.cable ~20.9
9. STP (Shielded Twisted Pair) cabling reduces: (Select 2)
   - **[x] Crosstalk**  - **[x] EMI**  - [ ] Jitter  - [ ] Attenuation
   - *STP (Shielded Twisted Pair): the shield blocks external EMI and RFI (Radio-Frequency Interference) and crosstalk from neighbouring cables. It doesn't stop attenuation, which is signal loss over distance.*
   - @5.2.cable ~20.10
10. A run must pass near fluorescent ballasts and radio transmitters. Which media choice would suffer the most from that interference?
    - **[x] UTP**  - [ ] Coax  - [ ] STP  - [ ] Fibre
    - *UTP has no shielding, so EMI and RFI hit it hardest. STP and coax are shielded, and fibre carries light, not electricity.*
    - @5.2.cable ~20.11
11. In a factory full of welding gear and heavy motors, which media is completely unaffected by electromagnetic and radio interference?
    - [ ] Coax  - [ ] UTP  - [ ] Twinax  - [ ] STP  - **[x] Fibre**
    - *Fibre carries light through glass, so electrical noise cannot affect it. It also avoids ground loops between buildings.*
    - @5.2.cable ~20.12
12. True or false: attenuation on a long copper run is solved by swapping in a transceiver that amplifies the signal.
    - [ ] True  - **[x] False**
    - *Attenuation is signal loss over distance. Fix it by keeping within the length limit, for example 100 m for copper Ethernet, or by adding a repeater or switch, or by moving to fibre. A transceiver converts media types and does not amplify a degraded signal.*
    - @5.2.cable ~20.13
13. Match each to its signal degradation cause. Type the letters in order, e.g. abc. ¶  Signal from one pair bleeds into another · a motor next to the cable adds noise · the signal weakens over a 130 m run ¶  A attenuation · B crosstalk · C interference
    - [=] bca | b c a | b,c,a
    - *Crosstalk = pair to pair (NEXT/FEXT, Near/Far-End Crosstalk). Interference = external EMI/RFI. Attenuation = loss over distance.*
    - @5.2.cable
14. Cable for a DIRECT link between two PCs, with no switch and no Auto MDI-X?
    - [ ] Patch cable  - **[x] Crossover cable**  - [ ] Rollover cable  - [ ] Straight-through cable
    - *Crossover = one end T568A, the other T568B, so TX (transmit) meets RX (receive). Straight-through (patch) = both ends the same standard, PC to switch. Rollover/Yost = console cable, pins fully reversed.*
    - @5.2.cable ~20.15
15. The common cable for connecting a workstation to a switch?
    - **[x] Straight-through**  - [ ] Rollover  - [ ] Yost  - [ ] Crossover
    - *A patch cable is straight-through: T568B at both ends (usually). It connects unlike devices: a PC (MDI, Medium Dependent Interface) to a switch (MDI-X, crossover).*
    - @5.2.cable ~20.16,20.17
16. Feature that detects the cable type automatically and swaps TX/RX pairs as needed?
    - [ ] Adaptive connector  - [ ] Smart plug  - **[x] Auto MDI-X**  - [ ] Zero-config networking
    - *Auto MDI-X (Medium Dependent Interface Crossover) = on almost every modern port, especially Gigabit (optional in the standard, but near-universal), so crossover cables are mostly legacy.*
    - @5.2.cable ~20.18
17. A tech terminates one end of a patch cable to T568A and the other to T568B. What sets the two standards apart?
    - **[x] The orange and green pairs are swapped**  - [ ] A is for fibre and B is for copper  - [ ] Only B supports PoE  - [ ] A is for shielded cable and B for unshielded
    - *T568A and T568B differ only in swapping the orange and green pairs. Same on both ends = straight-through. Different ends = crossover, though Auto-MDI-X makes this largely irrelevant today. A cable with A on one end and B on the other is a crossover.*
    - @5.2.cable ~27.7
18. A new run passes a basic pin-by-pin continuity check, yet a certifier reports severe NEXT. The installer swapped one conductor of one pair with one conductor of another pair, identically at both ends. What fault is this?
    - [ ] Open  - [ ] Short  - **[x] Split pair**  - [ ] Reversed pair
    - *With a split pair, pin-to-pin continuity looks correct but the pairs are not twisted together as designed, so crosstalk soars. Only a tester that checks pairing or NEXT catches it.*
    - @5.2.cable ~27.8
19. TX wires landing on the other end's TX pins, so no link forms, is called:
    - **[x] TX/RX transposed**  - [ ] A split pair  - [ ] An open  - [ ] Improper grounding
    - *TX/RX transposed = on copper, a miswire or crossover issue that Auto MDI-X usually fixes. On FIBRE it's very common: swap the two LC (Lucent Connector) strands at one end. Hook: fibre link down with the light present? Flip the pair.*
    - @5.2.cable
20. A PC has no link light on its NIC. First suspect?
    - [ ] Wrong DNS server  - [ ] Duplicate IP  - **[x] A bad or unplugged patch cable**  - [ ] An expired DHCP lease
    - *Answer: A bad or unplugged patch cable. No link light = Layer 1: the cable, the port, or the NIC. DNS, IP and DHCP are Layer 3+ and don't affect the link light. Question the obvious, bottom-up.*
    - @5.2.cable ~28.5
21. An installer finishes terminating a new drop and wants proof of correct pinout and continuity before signing off. Which tool should they use?
    - [ ] Toner probe  - **[x] Cable tester**  - [ ] Loopback plug  - [ ] Wi-Fi analyser
    - *A cable tester checks wiremap, continuity, shorts, opens and split pairs. A toner traces where a cable runs, and a loopback plug tests a port.*
    - @5.2.cable ~28.7
22. Linux shows: ¶  $ ip link show eth0 ¶2: eth0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 state DOWN ¶    link/ether 52:54:00:12:34:56 ¶What does NO-CARRIER mean?
    - [ ] No IP address assigned  - **[x] No physical link: check the cable and the port**  - [ ] DNS is missing  - [ ] The interface is disabled in software
    - *UP = enabled in software, but NO-CARRIER = no signal from the other end. It's Layer 1: the cable, a switch port that's shut, or a far-end NIC. "state DOWN" confirms it.*
    - @5.2.cable ~29.14
23. Match each run to the right cable. Type the letters in order, e.g. abcde. ¶  1 Gbps desk drop, 80 m · 10 Gbps to a server, 90 m · 25 Gbps top-of-rack to a server, 2 m · 40 Gbps between two switches in the same row, 25 m, copper · a 10 Gbps link to another building, 3 km ¶  A Cat 8 · B single-mode fibre · C Cat 5e · D twinax DAC · E Cat 6a
    - [=] cedab | c e d a b | c,e,d,a,b
    - *1G at 80 m = Cat 5e minimum. 10G at 90 m = Cat 6a. 25G at 2 m = DAC twinax (cheapest). 40G over 25 m of copper = Cat 8 (up to 30 m). 3 km = single-mode fibre.*
    - @5.2.cable
24. A wiremap shows: ¶  End A pins 1 2 3 4 5 6 7 8 ¶  End B pins 3 6 1 4 5 2 7 8 ¶Both ends' jacks are labelled T568B. What is the cable really?
    - **[x] A crossover**  - [ ] A rollover  - [ ] A split pair  - [ ] A reversed pair
    - *1↔3 and 2↔6 = the orange and green pairs are swapped: one end is really T568A. On a switch with Auto MDI-X it may still work, but re-terminate it to match the labels.*
    - @5.2.cable
25. A new 10G fibre link between two switches: ¶  SW1# show interfaces transceiver ¶  Local SFP: Tx -2.1 dBm, Rx -40.0 dBm ¶  Remote SFP: Tx -2.3 dBm, Rx -40.0 dBm ¶Both lasers are transmitting, but neither side receives any light. Fault?
    - **[x] TX/RX transposed**  - [ ] Attenuation from a long run  - [ ] Dirty connectors  - [ ] Transceiver mismatch
    - *Both transmit and nothing is received = the strands are crossed wrongly, TX into TX. Swap the pair of LC connectors at one end. -40 dBm = no light at all.*
    - @5.2.cable
26. Match each to its degradation cause. Type the letters in order, e.g. abc. ¶  UTP zip-tied along a lift motor's power cable · a 140 m copper run · pairs untwisted 5 cm at the jack ¶  A interference · B crosstalk · C attenuation
    - [=] acb | a c b | a,c,b
    - *Motor = EMI interference. Over 100 m = attenuation. Untwisted pairs at the termination = NEXT crosstalk (keep untwisting to about 13 mm, half an inch).*
    - @5.2.cable
27. A tech runs Cat 6 along fluorescent light fittings above the ceiling. The link negotiates 1 Gbps, then CRC errors climb all day. Which cable fixes it with the least change?
    - **[x] STP**  - [ ] UTP Cat 6a  - [ ] Single-mode fibre  - [ ] Coax
    - *STP (Shielded Twisted Pair, the cable, not Spanning Tree) resists EMI from the ballasts. Cat 6a UTP is still unshielded. Fibre would also work but is a bigger change. Or re-route the UTP away from the lights.*
    - @5.2.cable
28. A new 802.3at AP on Gi0/9 won't power up. Other devices are fine. ¶  SW1# show power inline ¶  Available:370.0(w)  Used:362.5(w)  Remaining:7.5(w) ¶  Interface  Admin  Oper  Power  Device       Class ¶  Gi0/8      auto   on    15.4   IP Phone     3 ¶  Gi0/9      auto   off   0.0    n/a          n/a ¶Cause?
    - **[x] The switch's PoE budget is exhausted: 7.5 W left and the AP needs up to 30 W**  - [ ] The AP needs 802.3bt  - [ ] Gi0/9 is administratively shut down  - [ ] The cable is over 100 m
    - *Read the top line first: Remaining 7.5 W. A PoE+ (802.3at) device can draw up to 30 W at the port, so the switch refuses to power it, and Oper shows off. Admin auto means the port is allowed to give power, so it isn't shut down. Fixes: remove or reprioritise other loads, a bigger PSU, a midspan injector, or a switch with more budget. Hook: check the wallet (Remaining) before blaming the device.*
    - @5.2.intf
29. A laptop keeps linking at 100 Mb/s instead of 1 Gb/s on a new cable run. Which OSI layer is the problem at?
    - **[x] Layer 1**  - [ ] Layer 2  - [ ] Layer 3  - [ ] Layer 4
    - *Answer: Layer 1. 100BASE-TX uses only 2 pairs (1,2 and 3,6); 1000BASE-T needs all 4. One bad pair (poor crimp or punch-down, split pair) and auto-negotiation falls back to 100. Fix: re-terminate and test all 8 wires. Hook: Gig needs all 4 pairs; lose one and you drop to 100.*
    - @1.5.wired

### Key facts
- **Match the fibre type to the optics: SMF (9 µm, yellow, km) vs MMF (50/62.5 µm, aqua, hundreds of m). Wrong type = attenuation, errors, short reach.**
- **Cat 5 100 Mbps · 5e 1G · 6 = 10G up to 55 m · 6a 10G at 100 m · 8 = 25/40G up to 30 m · DAC under 7 m · fibre for long runs.**
- **UTP = no shield, most EMI · STP = shielded, grounded, less EMI/crosstalk · fibre = immune.**
- **Degradation: crosstalk (pair to pair) · interference (EMI/RFI) · attenuation (distance) - a transceiver doesn't fix attenuation.**
- **Termination: T568A vs B swap orange/green · straight-through = same both ends · crossover = A + B · split pair passes continuity but fails crosstalk · TX/RX transposed = flip fibre strands.**
- **No link light / NO-CARRIER = Layer 1. Test with a cable tester or certifier.**

## Test 28 - 5.2 Interface + Hardware (29 Q)

1. What do CRC error counters help identify?
   - **[x] Corrupted frames**  - [ ] Packet drops  - [ ] Throughput  - [ ] Link utilisation
   - *CRC (Cyclic Redundancy Check) = the FCS (Frame Check Sequence) check failed, so the frame is corrupted. Causes: a bad cable, EMI (Electromagnetic Interference), a failing NIC (Network Interface Card), or a duplex mismatch on the full-duplex end.*
   - @5.2.intf ~20.19
2. A switch port's CRC counter keeps climbing while a user complains of slow transfers. What is the most likely cause?
   - [ ] A duplicate IP address  - **[x] A bad cable or EMI**  - [ ] The wrong VLAN  - [ ] An exhausted DHCP scope
   - *A CRC error means the frame checksum failed, so bits were corrupted at Layer 1. Suspect a damaged cable, bad connectors, interference or a duplex mismatch. VLAN and IP issues do not corrupt frames.*
   - @5.2.intf ~24.16
3. A port counter labelled runts is increasing. Which statements apply? (Select 2)
   - **[x] They are frames shorter than the 64-byte Ethernet minimum**  - **[x] They often come from collisions or faulty hardware**  - [ ] They are fragments caused by an MTU mismatch  - [ ] They exceed 1518 bytes
   - *Runts are undersized frames, typically from collisions, a duplex mismatch or a failing NIC. Frames that are too large are giants.*
   - @5.2.intf ~20.20
4. A port shows a rising giants counter. Which statements fit? (Select 2)
   - **[x] They are frames above the normal 1518-byte Ethernet limit**  - **[x] They usually point to an MTU misconfiguration or faulty hardware**  - [ ] They are a deliberate efficiency boost  - [ ] They always mean jumbo frames are working correctly
   - *Giants are oversized frames. They appear when frames above 1518 bytes (1522 with an 802.1Q tag) arrive on a port not configured for jumbo frames, when MTU settings differ between devices, or when a NIC is faulty. Match the MTU end to end.*
   - @5.2.intf ~20.21
5. On a switch, which situation does an increasing drops counter usually represent?
   - [ ] Traffic denied by an access list  - [ ] Frames duplicated by a switching loop  - **[x] Packets thrown away because the queue or buffer was full**  - [ ] Traffic forwarded to the wrong VLAN
   - *Drops occur when packets arrive faster than an interface can send them and the buffers overflow, which is a sign of congestion. QoS or more bandwidth helps.*
   - @5.2.intf ~20.22
6. Every afternoon during backups, an uplink logs thousands of output discards while CRC and input errors stay at zero. What is the likely cause?
   - [ ] Bad cable  - **[x] Congestion**  - [ ] Duplex mismatch  - [ ] EMI
   - *Output drops with a clean physical layer mean the link is oversubscribed. Add bandwidth, use link aggregation, or apply QoS. Cabling faults would show CRC errors.*
   - @5.2.intf ~24.17
7. Match each cause to the counter it raises. Type the letters in order, e.g. abcd. ¶  EMI near a cable corrupts frames · collision fragments under 64 bytes · 9000-byte frames hit a 1500-MTU port · a full egress queue at peak time ¶  A giants · B drops · C CRC · D runts
   - [=] cdab | c d a b | c,d,a,b
   - *Corrupt = CRC. Too small = runts. Too big = giants. No room = drops (discards).*
   - @5.2.intf
8. The link light is on with a fresh patch lead, yet the port's error counters show CRC errors and runts increasing. Likely cause?
   - [ ] Exhausted DHCP scope  - **[x] Duplex mismatch or bad cabling**  - [ ] Wrong default gateway  - [ ] Spanning tree loop
   - *CRC errors and runts are Layer 1 and Layer 2 symptoms: one side half duplex and the other full, or damaged cabling. Set both sides to auto, or hard-code both identically. DHCP, gateway and STP problems do not raise CRC or runt counters.*
   - @5.2.intf ~28.6
9. A user's backups to the NAS crawl. You check the switch: ¶  SW1# show interfaces Gi0/7 ¶Gi0/7 is up, line protocol is up ¶  Half-duplex, 100Mb/s ¶  412 late collisions ¶  1790 CRC, 1824 input errors ¶What is the most likely cause?
   - [ ] VLAN mismatch  - **[x] Duplex mismatch**  - [ ] Exhausted DHCP scope  - [ ] Spanning tree loop
   - *Late collisions on a half-duplex port, plus CRC errors, are the signature of a duplex mismatch where the other end runs full duplex. Fix both sides to match, preferably auto-negotiate on both.*
   - @5.2.intf ~29.4
10. A port the switch shut down itself because of an error or security violation is in which state?
    - [ ] Blocking  - **[x] Error disabled**  - [ ] Administratively down  - [ ] Suspended
    - *Answer: Error disabled. err-disabled = the switch did it: BPDU guard, a port-security violation, UDLD (Unidirectional Link Detection) or link flapping. Recovery: fix the cause, then shutdown / no shutdown, or configure errdisable recovery.*
    - @5.2.intf ~20.23
11. A switch port MANUALLY shut down by an admin shows as:
    - [ ] Inactive  - [ ] Suspended by LACP  - **[x] Administratively down**  - [ ] Err-disabled
    - *"administratively down" = the shutdown command is in the config. Fix: no shutdown. It's a common cause of "no link" after a new VLAN assignment.*
    - @5.2.intf ~20.24
12. A port temporarily inactive because of a configuration conflict, such as an LACP member not matching the bundle, shows as:
    - [ ] Standby  - [ ] Disabled  - **[x] Suspended**  - [ ] Dormant
    - *Suspended = e.g. an EtherChannel member with a different speed, duplex or VLAN settings from the others. Make its config match, and it rejoins.*
    - @5.2.intf ~20.25
13. Someone in marketing connected a travel switch to their desk jack, and now: ¶  SW1# show interfaces Gi0/12 ¶Gi0/12 is down, line protocol is down (err-disabled) ¶What disabled the port?
    - [ ] The cable run is too long  - [ ] PoE budget exceeded  - **[x] A BPDU guard violation**  - [ ] The DHCP lease expired
    - *BPDU guard on an access port shuts it down as soon as it hears an STP BPDU from another switch. Remove the device, then use shutdown and no shutdown, or err-disable recovery.*
    - @5.2.intf ~29.5
14. What is a PoE power budget?
    - **[x] The total power a PoE switch can supply to all ports**  - [ ] The power the switch itself uses to run  - [ ] The voltage supplied on each individual port  - [ ] How long the UPS can keep the switch running
    - *PoE (Power over Ethernet) budget = e.g. 370 W across 48 ports. Once it's used up, new devices get no power even though their ports work. Priority settings decide who keeps power.*
    - @5.2.hw ~21.1
15. A switch keeps denying power to new access points because its PoE budget is exhausted. Which action would NOT help?
    - **[x] Checking each AP's draw with a multimeter**  - [ ] Comparing the switch budget with what the devices need  - [ ] Unplugging PoE devices that are not essential  - [ ] Upgrading the switch or adding a PoE injector
    - *Fix budget issues by comparing the switch's total power with what devices require, cutting the load, or adding capacity. A multimeter is not how you size PoE; read the switch's power figures instead.*
    - @5.2.hw ~21.2
16. Which of the following must be subtracted from the transmitter's output when calculating a long-distance fibre power budget?
    - **[x] Losses from connectors and splices**  - [ ] The switch's total PoE capacity  - [ ] The wavelength of the light  - [ ] The SFP's electrical wattage draw
    - *Answer: Losses from connectors and splices. A fibre power (loss) budget is about LIGHT, not electricity: Tx power minus every loss (fibre length in dB/km, each connector about 0.5 dB, each splice about 0.1 dB, patch panels) must still be above the receiver's sensitivity. If it isn't, the link flaps or stays down; check with a light meter (optical power meter). Don't confuse it with the PoE power budget (watts on a copper switch).*
    - @5.2.hw
17. Tool to verify that a switch's PoE standard is compatible with the connected device?
    - **[x] PoE tester**  - [ ] Cable certifier  - [ ] Power meter  - [ ] Voltage tester
    - *A PoE tester shows the standard negotiated and the wattage delivered (af, at or bt). Incorrect standard = an objective item: a 30 W camera on an 802.3af port won't boot properly.*
    - @5.2.hw ~21.3
18. A pan-tilt-zoom camera draws 25 W at the device and must get its power from the switch port. Which PoE standard is the minimum?
    - [ ] 802.3af (PoE)  - **[x] 802.3at (PoE+)**  - [ ] 802.3bt Type 3 only  - [ ] 802.3ab
    - *802.3af gives about 13 W at the device, 802.3at about 25.5 W, and 802.3bt Type 3 about 51 W or Type 4 about 71 W. 802.3ab is 1000BASE-T, not a power standard. Size by the power the device needs.*
    - @5.2.hw ~26.9
19. Match each power level to its PoE standard. Type the letters in order, e.g. abc. ¶  60-100 W · 15.4 W · 30 W ¶  A 802.3at · B 802.3bt · C 802.3af · D 802.3ab
    - [=] bca | b c a | b,c,a
    - *60-100 W = B 802.3bt PoE++ (Types 3 and 4). 15.4 W = C 802.3af PoE. 30 W = A 802.3at PoE+. 802.3ab = 1000BASE-T, not PoE. Hook: af, at, bt in alphabetical order = more power.*
    - @5.2.hw
20. A desk phone on Gi0/14 stays dark. The switch reports the port as admin auto, oper off, drawing 0.0 W, with 739.2 W of the 740 W pool already allocated. Why won't it power up?
    - [ ] The VLAN is wrong  - [ ] The cable is crossover  - **[x] The switch's PoE budget is used up**  - [ ] DHCP is failing
    - *Less than 1 W remains in the pool, which is too little for a phone, so the port stays off. Free up budget, upgrade the power supply, or use an injector.*
    - @5.2.hw ~29.10
21. A data centre engineer connects a 40G switch port to a server, but the optic on one side is SFP form factor and the other is QSFP. The link never comes up. Why?
    - **[x] Transceiver mismatch**  - [ ] Congestion  - [ ] Duplex mismatch  - [ ] A faulty module
    - *SFP and QSFP modules differ in form factor and speed, so both ends need compatible optics, with matching wavelength and fibre type too. Both modules may work, but they cannot interoperate, so mismatch is more likely than a fault.*
    - @5.2.hw ~21.4
22. To check how much light is reaching the far end of a fibre run, which tool should a tech use?
    - [ ] Wiremap tester  - [ ] Tone generator  - **[x] Optical power meter**  - [ ] Spectrum analyser
    - *An optical power meter, used with a light source, measures received power in dBm to find loss. An OTDR locates where faults are along the run.*
    - @5.2.hw ~21.5
23. A tech wants to certify the signal performance of a new copper Ethernet drop. Which tool is most appropriate?
    - [ ] Network TAP  - **[x] Cable tester**  - [ ] Multimeter  - [ ] Tone generator
    - *A cable tester or certifier checks wiremap, length, crosstalk and attenuation on twisted pair. A tone generator only traces the cable, and a TAP copies traffic.*
    - @5.2.hw ~21.6
24. Match the port state to each. Type the letters in order, e.g. aaaa. ¶  The admin typed shutdown · BPDU guard fired · an LACP member has a different speed from the bundle · port-security violation with mode shutdown ¶  A err-disabled · B suspended · C administratively down
    - [=] caba | c a b a | c,a,b,a
    - *Manual = administratively down. Switch protection = err-disabled. Bundle mismatch = suspended (e.g. LACP on one side but static 'on' mode on the other: the LACP side never hears LACPDUs, so it suspends those members rather than risk a loop).*
    - @5.2.intf
25. A switch shows: ¶  SW1# show interfaces Gi0/1 ¶  Full-duplex, 1000Mb/s ¶  input errors 0, CRC 0, runts 0, giants 18422 ¶The server on Gi0/1 is set to MTU 9000. Cause?
    - **[x] MTU mismatch**  - [ ] Duplex mismatch  - [ ] A bad cable  - [ ] Congestion
    - *Giants with a jumbo-configured server and a 1500-MTU switch port = MTU mismatch. Either enable jumbo frames on the switch (system mtu jumbo 9000) or set the server back to 1500.*
    - @5.2.intf
26. A switch shows: ¶  SW1# show power inline ¶  Gi0/8  auto  on   15.4  Ieee PD class 3  ¶  Gi0/9  auto  faulty  0.0  n/a ¶  Budget 740 W  Used 212 W ¶The device on Gi0/9 is a 45 W 802.3bt access point, and the switch is 802.3at. Fault?
    - **[x] Incorrect PoE standard**  - [ ] PoE budget exceeded  - [ ] A bad cable  - [ ] Transceiver mismatch
    - *The budget is fine (528 W free). The switch's PoE+ (30 W max per port) can't give an 802.3bt device the 45 W it needs. Fix: a bt switch or a bt injector.*
    - @5.2.hw
27. A switch shows: ¶  SW1# show interfaces transceiver ¶  Te1/0/1  SFP-10G-LR  Tx -1.8 dBm  Rx -18.9 dBm  (low alarm -14.4) ¶The link flaps. Fault and first fix?
    - **[x] Low signal strength; inspect and clean the connectors**  - [ ] Transceiver mismatch; replace with an SR optic  - [ ] TX/RX transposed; swap the strands  - [ ] Duplex mismatch; hard-set both ends
    - *Rx far below the alarm threshold = low signal strength. The first fix for fibre: inspect and clean the connectors, then check for bends or bad splices with an OTDR (Optical Time-Domain Reflectometer) or a visual fault locator.*
    - @5.2.hw
28. Match each speed to its transceiver. Type the letters in order, e.g. abcde. ¶  40G · 1G · 100G · 10G · 25G ¶  A SFP+ · B QSFP28 · C SFP · D SFP28 · E QSFP+
    - [=] ecbad | e c b a d | e,c,b,a,d
    - *40G = QSFP+ (4×10) · 1G = SFP · 100G = QSFP28 (4×25) · 10G = SFP+ · 25G = SFP28. Q = Quad lanes.*
    - @5.2.hw
29. PBQ: Interface problems on SW1. ¶  SW1# show interfaces status ¶  Port   Status        Vlan  Duplex  Speed ¶  Gi0/2  connected     10    a-full  a-1000 ¶  Gi0/5  connected     10    a-half  a-100 ¶  Gi0/7  connected     10    a-full  a-1000 ¶  Gi0/9  err-disabled  10    auto    auto ¶ ¶  SW1# show interfaces gi0/2 ¶    1532 input errors, 1532 CRC   rises only while the lift next to the riser runs ¶  SW1# show interfaces gi0/5 ¶    0 collisions, 842 late collision   far end is hard-set to 100 full ¶  SW1# show interfaces gi0/7 ¶    911 input errors, 911 CRC   the cable tester measured the run at 118 m ¶  SW1# show port-security interface gi0/9 ¶    Port Status : Secure-shutdown · Security Violation Count : 1
    - [p] Gi0/2 cause :: A EMI on unshielded cable · B duplex mismatch · C over the distance limit · D port-security violation = a
    - [p] Gi0/5 cause :: A EMI on unshielded cable · B duplex mismatch · C over the distance limit · D port-security violation = b
    - [p] Gi0/7 cause :: A EMI on unshielded cable · B duplex mismatch · C over the distance limit · D port-security violation = c
    - [p] Gi0/9 cause :: A EMI on unshielded cable · B duplex mismatch · C over the distance limit · D port-security violation = d
    - [p] After removing the rogue device, type the two Gi0/9 interface commands, in order, separated by ; = shutdown ; no shutdown | shut ; no shut | shutdown; no shutdown | shut; no shut
    - *CRC errors that track a motor = EMI (electromagnetic interference): shielded cable or a new route. Late collisions on the half-duplex end = duplex mismatch: hard-setting the far end stops autonegotiation, so this end falls back to half (a-half). Errors on a 118 m run = past copper's 100 m limit. Secure-shutdown = port security err-disabled the port: remove the device, then shutdown / no shutdown to bring it back.*
    - @5.2.intf

### Key facts
- **Counters: CRC = corrupt (cable, EMI, NIC, duplex) · runts = under 64 bytes (collisions) · giants = over 1518 bytes (MTU mismatch) · drops = congestion. Half duplex + late collisions + CRC = duplex mismatch.**
- **Port status: err-disabled = switch-triggered (BPDU guard, port security) → fix, then shut/no shut · administratively down = shutdown in config → no shutdown · suspended = LACP member mismatch.**
- **PoE: af 15.4 W · at 30 W · bt 60-100 W. Budget exceeded → show power inline. Incorrect standard = device needs more than the port class.**
- **Transceiver mismatch = form factor, speed, wavelength (SR/LR) or fibre type. Signal strength: OPM / show interface transceiver, clean connectors first.**

## Test 29 - 5.3 Service Issues (33 Q)

1. Someone patches two access switches together with a second cable while STP is disabled. Broadcasts multiply until the network freezes. What is this condition?
   - [ ] Routing loop  - [ ] Flooding attack  - **[x] Switching loop**  - [ ] VLAN hopping
   - *A switching loop is a Layer 2 loop: frames have no TTL, so broadcasts circle and multiply into a broadcast storm and MAC tables flap. STP blocks redundant paths to prevent it.*
   - @5.3.sw ~21.8
2. Which protocols prevent switching loops? (Select 2)
   - **[x] STP**  - **[x] RSTP**  - [ ] SRTP  - [ ] LLDP  - [ ] BPDU
   - *STP (Spanning Tree Protocol, 802.1D) and RSTP (Rapid STP, 802.1w) block redundant paths. A BPDU (Bridge Protocol Data Unit) is the MESSAGE STP uses, not a protocol. SRTP = Secure Real-time Transport Protocol (voice). LLDP = Link Layer Discovery Protocol.*
   - @5.3.sw ~21.9
3. A colleague lists duties of the STP root bridge. Which item on the list is wrong?
   - [ ] All switches compute their path costs toward it  - [ ] It anchors the single loop-free path between any two points  - [ ] It helps keep the topology loop-free  - **[x] It spreads user traffic evenly across switches**
   - *The root bridge, chosen by the lowest bridge ID, is the reference point of the STP tree. STP only blocks paths; it does not balance load.*
   - @5.3.sw ~21.10
4. Bridge ID = priority + MAC, and the lowest wins. Which becomes the root bridge?
   - [ ] A: 40960, MAC ...68:16  - **[x] B: 32768, MAC ...68:17**  - [ ] C: 40960, MAC ...68:18  - [ ] D: 32768, MAC ...68:19
   - *Compare the priority first: 32768 < 40960, so B or D. It's a tie, so the lowest MAC wins: ...17 < ...19, so B. Default priority = 32768, set in steps of 4096. Set the core switch lower on purpose, or an old switch with a low MAC may win.*
   - @5.3.sw ~21.11
5. On an access switch that is not the root, which STP port role is given to the interface with the cheapest path back to the root?
   - [ ] Designated port  - **[x] Root port**  - [ ] Alternate port  - [ ] Edge port
   - *Each non-root switch has one root port, its best path toward the root. Each segment has one designated port, which forwards onto that segment. Alternate ports are blocked backups.*
   - @5.3.sw ~21.12
6. Two switches share a link. On that segment, the port offering the lower cost toward the root is chosen to forward. What role does it get?
   - [ ] Default port  - [ ] Priority port  - **[x] Designated port**  - [ ] Active port
   - *Every segment elects one designated port, the one closest to the root, to forward traffic for it. On the root bridge, all ports are designated.*
   - @5.3.sw ~21.13
7. What are the STP roles of: the best path to the root on a non-root switch · the forwarder for a segment · a redundant port not forwarding, in that order?
   - **[x] Root port · designated port · blocked (alternate) port**  - [ ] Designated port · root port · blocked port  - [ ] Root port · blocked port · designated port  - [ ] Edge port · designated port · disabled port
   - *Root → designated → blocked (called alternate in RSTP). Disabled = administratively shut, not part of STP at all.*
   - @5.3.sw ~21.14,21.15
8. A redundant uplink has been kept out of use by STP so no loop forms. Which state is it in?
   - [ ] Standby  - [ ] Idle  - [ ] Listening  - **[x] Blocking**
   - *Blocking ports, discarding in RSTP, drop data frames but keep listening for BPDUs, so they can take over if the active path fails.*
   - @5.3.sw ~21.16,21.17
9. During STP convergence a port enters the listening state. What does it do there?
   - **[x] Exchanges BPDUs but neither forwards frames nor learns MAC addresses**  - [ ] Only receives BPDUs, never sends them, and drops all frames  - [ ] Forwards frames and learns MACs normally  - [ ] Learns MACs from incoming frames without forwarding yet
   - *The 802.1D sequence is blocking, listening, learning, then forwarding. Listening takes part in the root and role election, learning fills the MAC table, and forwarding passes data.*
   - @5.3.sw ~21.18
10. A port building its MAC table, but not yet forwarding frames, is in which state?
    - **[x] Learning**  - [ ] Discovery  - [ ] Listening  - [ ] Querying
    - *Hook: listen, then learn, then forward. That's why a PC plugged into a non-PortFast port waits about 30 s (up to 50 s) before getting DHCP.*
    - @5.3.sw ~21.19
11. Two PCs on the same switch, access ports, all ports up, both with correct IPs in 10.1.1.0/24, can't communicate. Most likely cause?
    - [ ] Bad switch port  - **[x] Incorrect VLAN assignment**  - [ ] Faulty cable  - [ ] IP misconfiguration
    - *Answer: Incorrect VLAN assignment. Different VLANs = different broadcast domains, so they need a router even on the same switch. Check with show vlan brief.*
    - @5.3.sw ~21.20
12. How are ACL entries evaluated?
    - **[x] Top to bottom; the first match applies and the rest are ignored**  - [ ] All entries are checked and the most specific wins  - [ ] Bottom to top  - [ ] Randomly
    - *ACLs (Access Control Lists) = first match wins. A broad deny above a specific permit blocks it. That's an ordering bug.*
    - @5.3.sw ~21.21
13. What happens to traffic that matches NO ACL entry?
    - [ ] Explicitly denied  - [ ] Implicitly allowed  - [ ] Explicitly allowed  - **[x] Implicitly denied**
    - *Answer: Implicitly denied. Every ACL ends with an invisible deny any. An ACL with only deny lines therefore blocks EVERYTHING. Add permit any at the end if that's what you intend.*
    - @5.3.sw ~21.22
14. The finance VLAN cannot open the ERP server, yet cabling, the host and the app all check out. How might the ACL be at fault?
    - [ ] A deny rule sits above the permit, so valid traffic matches it first  - [ ] There is no permit statement for finance to that server  - [ ] It was bound to the wrong interface or direction  - **[x] Any of the above**
    - *ACLs are processed top-down with first match wins and an implicit deny at the end. Rule order, a missing permit, or applying the ACL in the wrong place or direction all block legitimate traffic.*
    - @5.3.sw ~21.23
15. How does a router pick a route when several match?
    - **[x] Longest prefix, then lowest AD, then lowest metric**  - [ ] Lowest metric, then lowest AD, then longest prefix  - [ ] Highest AD, then highest metric, then newest  - [ ] Most recently learned, then lowest metric
    - *Longest prefix match → AD (Administrative Distance, between protocols) → metric (within one protocol). Use show ip route.*
    - @5.3.rt ~21.24
16. Administrative distance: HIGH AD = most preferred?
    - [ ] True  - **[x] False**
    - *Answer: False. LOWER is more trusted: connected 0, static 1, EIGRP 90, OSPF 110, RIP 120.*
    - @5.3.rt ~21.25
17. Which is NOT a routing METRIC?
    - [ ] Load  - [ ] Bandwidth  - [ ] Delay  - **[x] Admin distance**  - [ ] Hop count
    - *Answer: Admin distance. Metrics compare paths within one protocol (hops, cost, bandwidth, delay). AD compares route sources (protocols).*
    - @5.3.rt ~22.1
18. What is the default route?
    - **[x] The route of last resort, 0.0.0.0/0**  - [ ] The first route in the routing table  - [ ] The route to the DNS server  - [ ] The route with AD 0, 0.0.0.0/32
    - *No default route on the edge router = everything beyond the known networks fails. A missing or wrong default route is an objective item.*
    - @5.3.rt ~22.2
19. Which mitigate ROUTING loops?
    - [ ] Maximum hop count and TTL  - [ ] Split horizon  - [ ] Route poisoning and hold-down timers  - **[x] All of the above**
    - *Answer: All of the above. TTL (Time To Live) kills circling packets. Split horizon = never advertise a route back out the interface it was learned on. Poisoning = advertise a dead route as unreachable. Hold-down = ignore flapping updates for a while.*
    - @5.3.rt ~22.3
20. A PC shows: ¶  C:\> tracert 8.8.8.8 ¶  1    <1 ms  192.168.1.1 ¶  2     *     Request timed out. ¶  3     *     Request timed out. ¶Ping to 8.8.8.8 also fails. Most likely?
    - [ ] A DNS failure on the PC  - **[x] The link or route past the gateway**  - [ ] A faulty NIC in the PC  - [ ] The local gateway is down
    - *Hop 1 answers, so the PC and LAN are fine. Everything past it fails, and it's by IP, so it isn't DNS. Suspect the ISP link, a missing default route on the router, or a firewall.*
    - @5.3.rt ~29.7
21. A DHCP scope is exhausted. Which fixes help? (Select 2)
    - **[x] Shorten the lease time**  - **[x] Enlarge the pool**  - [ ] Extend the lease time  - [ ] Disable the DHCP relay
    - *Exhaustion = every address leased. Add addresses (a wider scope or subnet) and recycle them faster (a shorter lease). IPAM (IP Address Management) monitoring helps you see it coming, but doesn't fix it.*
    - @5.3.ip ~22.4
22. A classic symptom of an EXHAUSTED DHCP scope on a client?
    - **[x] An APIPA 169.254.x.x address**  - [ ] An IP reservation error  - [ ] Congestion  - [ ] A server timeout message
    - *No lease = the client self-assigns APIPA (Automatic Private IP Addressing). Existing clients keep working; new ones fail.*
    - @5.3.ip ~22.5,28.8
23. A PC shows 192.168.1.10/24, gateway 192.168.2.1, DNS 8.8.8.8. It reaches local devices but not websites. Cause?
    - [ ] DHCP misconfigured  - [ ] Incorrect subnet mask  - [ ] Firewall blocking  - **[x] Incorrect default gateway**
    - *Answer: Incorrect default gateway. 192.168.2.1 isn't in 192.168.1.0/24, so the PC can't ARP it and all off-subnet traffic fails. The gateway must be in the host's subnet.*
    - @5.3.ip ~22.6
24. Duplicate IP addresses can be caused by: (Select 2)
    - **[x] Incorrect static IP assignments**  - **[x] Rogue DHCP servers**  - [ ] DNS caching  - [ ] Routing table corruption
    - *A static IP inside the DHCP pool, with no exclusion, eventually gets handed out again. A rogue DHCP server hands out overlapping ranges. Windows warns about the conflict; tools like arping show two MACs for one IP.*
    - @5.3.ip ~22.7
25. A device 192.168.1.100 has mask 255.255.0.0, while every other device uses 255.255.255.0. It reaches the local 192.168.1.x hosts but not 192.168.5.x on another subnet. Cause?
    - [ ] Incorrect default gateway  - **[x] Incorrect subnet mask**  - [ ] IP out of range  - [ ] Incorrect VLAN
    - *Answer: Incorrect subnet mask. A mask that's too wide makes the host think off-subnet hosts, like 192.168.5.x, are local, so it ARPs for them instead of using the gateway. A mask that's too narrow makes it send local traffic to the gateway.*
    - @5.3.ip ~22.8
26. A user can't reach anything. The PC shows: ¶  C:\> ipconfig /all ¶   DHCP Enabled . . : Yes ¶   IPv4 Address . . : 169.254.23.118 ¶   Subnet Mask  . . : 255.255.0.0 ¶   Default Gateway  : (blank) ¶What's the cause?
    - **[x] The PC couldn't reach a DHCP server**  - [ ] A DNS failure  - [ ] A wrong default gateway  - [ ] A wrong subnet mask
    - *169.254 with DHCP enabled = no DHCP server reached: the scope is exhausted, there's no relay, the server is down, or the port is in the wrong VLAN. Next: ipconfig /renew and check the server.*
    - @5.3.ip ~29.1
27. A PC reaches local printers but no other subnets. It shows: ¶  C:\> ipconfig /all ¶   IPv4 Address . . : 10.10.20.55 ¶   Subnet Mask  . . : 255.255.255.0 ¶   Default Gateway  : 10.10.30.1 ¶Type the correct first usable gateway address for this subnet, assuming the router uses .1.
    - [=] 10.10.20.1
    - *The /24 subnet = 10.10.20.0-255. 10.10.30.1 is in a different subnet, so it's unreachable. The router's interface is on 10.10.20.1.*
    - @5.3.ip ~29.2
28. Slow cloud app. A PC shows: ¶  C:\> tracert app.example.com ¶  1    <1 ms  10.0.0.1 ¶  2     3 ms  172.16.0.1 ¶  3   188 ms  203.0.113.9 ¶  4   191 ms  198.51.100.4 ¶  5   192 ms  app.example.com ¶Type the two hop numbers the slow link sits between, separated by a space.
    - [=] 2 3 | 2-3 | 2 to 3
    - *Latency jumps at hop 3 and STAYS high, so the delay is on the link from hop 2 to hop 3 (usually the ISP/WAN edge). A single high hop that drops back afterwards is just a router deprioritising ICMP replies.*
    - @5.3.rt ~29.6
29. Using this table, where will R1 forward packets: ¶  R1# show ip route ¶Gateway of last resort is 198.51.100.1 to network 0.0.0.0 ¶S*   0.0.0.0/0 1/0 via 198.51.100.1 ¶C    172.16.4.0/24 is directly connected, Gi0/1 ¶O    172.20.0.0/16 110/30 via 172.16.4.9, Gi0/1 ¶Type the next hop for 172.20.8.15, then for 1.1.1.1, separated by a space.
    - [=] 172.16.4.9 198.51.100.1
    - *172.20.8.15 falls inside 172.20.0.0/16, the OSPF route, so it goes to 172.16.4.9. 1.1.1.1 matches nothing more specific, so it follows the default route to 198.51.100.1. The router always picks the longest prefix match.*
    - @5.3.rt ~29.19,29.20
30. Four switches, default priority 32768. MACs: ¶  CORE1 0019.aa00.0100 · ACC1 0001.0000.0001 · ACC2 0050.0000.0002 · ACC3 00a0.0000.0003 ¶Which switch does STP elect as root, and how do you fix it?
    - **[x] ACC1; set CORE1's priority lower, e.g. 4096**  - [ ] CORE1; nothing to fix  - [ ] ACC3; set CORE1's priority higher, e.g. 61440  - [ ] ACC1; raise ACC1's MAC address
    - *All tie on 32768, so the lowest MAC wins: ACC1 (0001...), an access switch, which means traffic takes bad paths. Set CORE1's priority lower: 4096, or use root primary (24576 or lower). Any multiple of 4096 below 32768 works.*
    - @5.3.sw
31. PBQ: The network is crawling. ¶  SW3# show logging ¶  %SW_MATM-4-MACFLAP_NOTIF: Host 0050.56aa.0001 in vlan 10 is flapping between port Gi0/1 and port Gi0/2 ¶  (repeated) ¶ ¶  SW3# show processes cpu ¶  CPU utilization for five seconds: 100% ¶ ¶  Broadcast counters on every port climbing fast. ¶  SW3# show spanning-tree ¶  No spanning tree instance exists. ¶ ¶  SW1 priority 32768, MAC 0011.1111.1111 ¶  SW2 priority 4096,  MAC 00aa.aaaa.aaaa ¶  SW3 priority 32768, MAC 0000.0000.0001
    - [p] Problem :: A a broadcast storm from a switching loop · B a duplex mismatch · C DHCP exhaustion · D a routing loop = a
    - [p] What does the show spanning-tree output tell you :: A STP is disabled on SW3, so nothing blocks a looped link · B SW3 is the root bridge · C STP has converged normally · D the ports are err-disabled = a
    - [p] Which switch should be the root bridge :: A SW1 · B SW2 · C SW3 = b
    - [p] Fastest way to stop the storm right now :: A unplug or shut one of the looped ports · B reboot SW1 · C raise SW3's priority · D clear the MAC table = a
    - *MAC flapping between two ports of the same switch plus climbing broadcasts and CPU = a layer 2 loop. With no spanning tree on SW3, nothing blocks the redundant path, so broadcasts circle forever, since Ethernet frames have no TTL. Stop it by pulling a link, then turn STP or RSTP back on. Root bridge = lowest priority first, and only then lowest MAC, so SW2's 4096 beats SW3's lower MAC. BPDU guard on access ports err-disables a port where a switch appears.*
    - @5.3.sw
32. PBQ: Users on LAN-B can't reach the server 10.3.3.10 on LAN-C. ¶ ¶  LAN-B  10.2.2.0/24 ¶    │ ¶    R1   10.2.2.1 · 10.0.12.1 ¶    │        link 10.0.12.0/30 ¶    R2   10.0.12.2 · 10.0.23.2 ¶    │        link 10.0.23.0/30 ¶    R3   10.0.23.3 ¶    │ ¶  LAN-C  10.3.3.0/24 ¶ ¶  LAN-B PC C:\> tracert 10.3.3.10 ¶   1  10.2.2.1 ¶   2  10.0.12.2 ¶   3  10.0.12.1 ¶   4  10.0.12.2 ¶   5  10.0.12.1  ... repeating ¶ ¶  R1# show ip route ¶  C   10.2.2.0/24 Gi0/0 ¶  C   10.0.12.0/30 Gi0/1 ¶  S   10.3.3.0/24 via 10.0.12.2 ¶ ¶  R2# show ip route ¶  C   10.0.12.0/30 Gi0/0 ¶  C   10.0.23.0/30 Gi0/1 ¶  S*  0.0.0.0/0 via 10.0.12.1
    - [p] Symptom :: A a routing loop · B a DNS failure · C an ACL on R2 blocking the traffic · D a duplex mismatch on R1 = a
    - [p] Which router has the faulty or missing route :: A R1 · B R2 · C R3 · D the LAN-B hosts = b
    - [p] Type the full IOS command that fixes it, ip route network mask next-hop = ip route 10.3.3.0 255.255.255.0 10.0.23.3
    - [p] Why do packets bounce between the two routers :: A R1 sends them to R2, and R2's default route sends them back · B R1's static route points the wrong way · C R2 has no route back to LAN-B · D the TTL is set too high on R1 = a
    - *A hop pair repeating = a routing loop. Read R2's table: it has no route to 10.3.3.0/24, so its default route sends the packet back to R1, which sends it to R2 again. R1 is right: its next hop 10.0.12.2 is the correct way to LAN-C. Fix R2 with a route to 10.3.3.0/24 via R3's address on their shared link, 10.0.23.3. Each hop decrements TTL, and at 0 the packet is dropped with an ICMP time exceeded. That is what tracert itself relies on.*
    - @5.3.rt
33. An engineering user's PC keeps getting an IP address from the marketing department's subnet via DHCP. Most likely cause?
    - **[x] The switch port is in the wrong (marketing) VLAN**  - [ ] DHCP address pool exhaustion  - [ ] STP is not enabled  - [ ] A duplicate IP address
    - *Answer: The switch port is in the wrong VLAN. DHCP hands out an address from the scope for the subnet the request ARRIVES on, and the access port's VLAN decides that. Marketing's range = the port is in marketing's VLAN: fix switchport access vlan. Pool exhaustion gives APIPA (169.254), not someone else's subnet.*
    - @5.3.sw

### Key facts
- **STP: loop = no TTL at L2, broadcast storm. Root = lowest bridge ID (priority, then MAC). Roles: root port (best way to root) · designated (one per segment) · blocked/alternate. States: blocking → listening → learning → forwarding.**
- **VLAN: same switch but can't talk = wrong VLAN → switchport access vlan N · show vlan brief.**
- **ACL: top-down, first match, implicit deny at the end · check order, direction, hit counts.**
- **Routing: longest prefix → lowest AD → lowest metric · default 0.0.0.0/0 · loop prevention: TTL, split horizon, poisoning, hold-down.**
- **Addressing: 169.254 = no DHCP (pool exhaustion → bigger scope + shorter lease) · gateway not in the subnet · duplicate IP (static in the pool, rogue DHCP) · wrong mask.**

## Test 30 - 5.4 Performance Issues (26 Q)

1. A branch WAN link chokes every morning when users sync files. Which measures help control the congestion?
   - [ ] QoS  - [ ] More bandwidth  - [ ] Traffic shaping or load balancing  - **[x] All of the above**
   - *QoS protects important traffic, extra bandwidth raises capacity, and shaping or load balancing smooths or spreads the load. Use a baseline to pick the right mix.*
   - @5.4.perf ~22.9
2. Monitoring shows one 1 Gbps firewall interface is always pegged while everything else is idle. What actually removes this bottleneck?
   - [ ] Tuning the routing tables  - **[x] Upgrading the constrained component**  - [ ] Running another diagnostic  - [ ] Watching the bandwidth graphs
   - *A bottleneck is the slowest part of the path. Monitoring and diagnostics only find it; replacing or upgrading that part fixes it.*
   - @5.4.perf ~22.10
3. Most effective fix for a genuine BANDWIDTH (throughput capacity) shortfall?
   - [ ] QoS on all traffic  - **[x] Bigger or bundled links**  - [ ] A CDN for web content  - [ ] Banning heavy apps
   - *Answer: Bigger or bundled links. Bandwidth = the capacity of the pipe; throughput = what you actually get. QoS only decides who suffers when the pipe is full; it doesn't make it bigger.*
   - @5.4.perf ~22.11
4. Users in Europe see high latency to a server hosted in the US. Best fix?
   - [ ] VPN  - [ ] SDN  - [ ] QoS  - **[x] CDN**
   - *Answer: CDN. Latency = delay, mostly from distance (the speed of light). A CDN (Content Delivery Network) caches content at edge locations near the users. QoS can't beat physics.*
   - @5.4.perf ~22.12
5. Which CLI tools detect packet loss? (Select 3)
   - **[x] ping**  - **[x] tracert**  - **[x] traceroute**  - [ ] nslookup  - [ ] netstat
   - *ping = shows a % loss summary · tracert (Windows) / traceroute (Linux) = where along the path loss or delay begins nslookup = DNS only.*
   - @5.4.perf ~22.13
6. VoIP calls have latency and jitter even though the connection is stable. Best fix?
   - [ ] Compression  - [ ] Disabling encryption  - **[x] QoS**  - [ ] Restarting the app
   - *Jitter = VARIATION in delay, which makes voice choppy. QoS puts voice in the priority queue (DSCP EF, Differentiated Services Code Point Expedited Forwarding, value 46). Targets: under 150 ms one-way latency, under 30 ms jitter, under 1% loss.*
   - @5.4.perf ~22.14
7. Match each to its performance term. Type the letters in order, e.g. abcd. ¶  Ping times of 20, 180, 25, 160 ms · 3 of 100 pings never return · a steady 250 ms to Sydney · an uplink at 100% with output drops ¶  A latency · B congestion · C jitter · D packet loss
   - [=] cdab | c d a b | c,d,a,b
   - *Varying delay = jitter. Missing replies = packet loss. Constant delay = latency. A full link = congestion.*
   - @5.4.perf
8. Many wireless clients on one AP compete for airtime at the same time. Term?
   - [ ] Attenuation  - **[x] Contention**  - [ ] Jitter  - [ ] Latency
   - *Contention = Wi-Fi is half duplex and shared, so one talker per channel at a time (CSMA/CA). More clients means more waiting. Fixes: more APs with smaller cells, 5/6 GHz, Wi-Fi 6 OFDMA.*
   - @5.4.perf ~24.18
9. The cafeteria's wireless crawls from 12 to 1 when staff watch videos on their break, and it is fine the rest of the day. What is the best first step?
   - [ ] Re-cable the floor  - [ ] Extend DHCP lease times  - **[x] Add an access point to cover the cafeteria**  - [ ] Rename the SSID
   - *Slowness only at peak density means too many clients on one AP. Add capacity where people gather, and consider rate limits or QoS for streaming.*
   - @5.4.perf ~24.19
10. Users say the CRM portal lags, though Teams calls and mail work normally. Which command reveals the hop where delay first appears?
    - [ ] ipconfig /all  - [ ] nslookup  - **[x] tracert / traceroute**  - [ ] arp -a
    - *tracert lists each router hop with round-trip times, so you can see where latency jumps. pathping adds loss statistics per hop over time.*
    - @5.4.perf ~28.13
11. Traceroute shows a hop jump from 5 ms to 180 ms in busy periods. What evidence shows that this is ongoing congestion rather than a fluke?
    - [ ] ARP table changes over time  - **[x] Link utilisation compared with the normal baseline**  - [ ] DHCP leases issued per hour  - [ ] DNS TTL on the hop's hostname
    - *Comparing peak utilisation against the baseline shows a repeating pattern of saturation. A single traceroute is only a snapshot.*
    - @5.4.perf ~28.14
12. Each weekday from noon to 2 p.m. the WAN saturates and phone calls break up. Without buying a bigger circuit, what is the cheapest remedy?
    - [ ] Disable spanning tree  - [ ] Shorten DHCP leases  - **[x] Apply QoS that prioritises voice**  - [ ] Add a second DNS server
    - *QoS marks voice, for example DSCP EF, and queues it first, so calls stay clear while bulk traffic waits. It reshuffles existing bandwidth rather than adding more.*
    - @5.4.perf ~28.15
13. A 10 Gbps fibre trunk to the server farm reports zero CRC and zero input errors, full duplex, but its Tx and Rx load counters read 254/255 and 251/255. Users call it slow. Why?
    - [ ] A dirty fibre connector  - [ ] Duplex mismatch  - **[x] The link is saturated**  - [ ] Wrong VLAN on the trunk
    - *A load close to 255/255 means the link is running at nearly full capacity, and zero errors rule out a physical fault. Add bandwidth or aggregate links, or apply QoS.*
    - @5.4.perf ~29.13
14. A Wi-Fi analyser in the lab shows RSSI -50 dBm but SNR 12 dB, and users there get slow, dropping connections. Most likely cause?
    - **[x] Interference raising the noise floor**  - [ ] Weak signal, too far from the AP  - [ ] Channel congestion from too many clients  - [ ] The wrong SSID
    - *SNR (Signal-to-Noise Ratio) = signal minus the noise floor, in dB. 25 dB or more is healthy, under about 15 dB is poor. -50 dBm is a strong signal, so a low SNR means the noise is high: microwaves, Bluetooth, cordless phones, neighbour APs. Find the source, or change channel or band. Hook: a loud voice in an even louder room.*
    - @5.4.wifi
15. Several APs in an office overlap on the 2.4 GHz band. Which measure would NOT help?
    - [ ] Survey with an analyser and choose quieter channels  - [ ] Use only channels 1, 6 and 11  - [ ] Shift clients to 5 GHz  - **[x] None of these, all of them help**
    - *On 2.4 GHz only channels 1, 6 and 11 avoid overlapping. Picking clear channels and moving to 5 or 6 GHz, which have many more channels, all reduce co-channel and adjacent-channel interference.*
    - @5.4.wifi ~22.15
16. Clients near the break room lose Wi-Fi throughput whenever the microwave runs. Which step would NOT help?
    - [ ] Keep clients within good range of the AP  - [ ] Remove obstructions or relocate the AP  - [ ] Adjust antenna orientation  - [ ] Identify interferers like microwaves and cordless phones  - **[x] Move everyone to 2.4 GHz to escape the interference**
    - *Microwave ovens and many cordless devices operate around 2.4 GHz, so that band is the busier one. Move to 5 or 6 GHz instead.*
    - @5.4.wifi ~22.16
17. Staff complain of dead spots in a new office wing. Which tools help map where coverage is weak? (Select 2)
    - **[x] A heat map**  - **[x] A Wi-Fi analyser**  - [ ] A signal booster  - [ ] A higher-gain antenna
    - *A site survey with an analyser produces a heat map that shows signal strength by location. Boosters and antennas are possible fixes, but they do not diagnose the problem.*
    - @5.4.wifi ~22.17
18. Clients keep getting disconnected (disassociated) from the AP repeatedly, and the logs show floods of deauth frames. Fix?
    - [ ] Send fewer beacons  - **[x] Enable 802.11w (MFP)**  - [ ] Add a guest SSID  - [ ] Limit the client count
    - *Answer: Enable 802.11w (MFP). Client disassociation = an objective item. Causes: weak signal, roaming thresholds, or a deauth attack (often the first step of an evil twin). 802.11w PMF (Protected Management Frames), mandatory in WPA3, blocks forged deauths.*
    - @5.4.wifi ~22.18
19. Users drop connections whenever they walk from one wing to the next. Which settings support seamless roaming? (Select 3)
    - **[x] The same SSID on every AP**  - **[x] Enough coverage overlap, roughly 15 to 20 percent**  - **[x] Matching security mode and passphrase on all APs**  - [ ] A different passphrase on each AP  - [ ] A different SSID on each AP
    - *Clients roam within one ESS only when the SSID and security match and the cells overlap enough for a handoff. 802.11r fast roaming helps further.*
    - @5.4.wifi ~22.19
20. Users near the edge of a warehouse drop off Wi-Fi, and the laptops show one bar at -82 dBm. Objective issue?
    - **[x] Insufficient coverage / signal loss**  - [ ] Channel overlap  - [ ] Roaming misconfiguration  - [ ] Client disassociation attack
    - *Below about -75 dBm = unreliable. Fix: add an AP or a directional antenna, or reposition. Don't just crank the AP's power, because clients can't transmit back as far (asymmetric power).*
    - @5.4.wifi
21. A survey of 2.4 GHz shows the office AP on channel 4 at -50 dBm, with neighbours on 1 (-61), 6 (-55) and 11 (-72). Type the channel the office AP should use.
    - [=] 11
    - *Stick to channels 1, 6 and 11, the non-overlapping ones. Channel 4 overlaps both 1 and 6. Channel 11 holds only the weakest neighbour at -72 dBm, so it is the quietest choice.*
    - @5.4.wifi ~29.15
22. Choppy VoIP calls. A PC shows: ¶  C:\> ping -n 20 voip.example.com ¶  Reply time=21ms · 19ms · 140ms · 22ms · 188ms · 20ms ... ¶  Packets: Sent = 20, Received = 20, Lost = 0 ¶  Minimum = 19ms, Maximum = 188ms, Average = 58ms ¶Calls are choppy. Problem and fix?
    - **[x] Jitter; QoS for voice**  - [ ] Packet loss; replace the cable  - [ ] Latency; a CDN  - [ ] Congestion; more bandwidth
    - *No loss, but the delay swings from 19 to 188 ms = jitter. Prioritise voice with QoS. A steady high number would be latency instead.*
    - @5.4.perf
23. A VoIP user reports choppy calls to 10.50.1.10. Type the Windows command that sends exactly 100 pings to it, so you can read the loss % and the min/max times.
    - [=] ping -n 100 10.50.1.10 | ping 10.50.1.10 -n 100
    - *ping -n sets the count on Windows (Linux uses -c). 100 samples show packet loss % and the spread between min and max times, which is jitter. Loss or big swings = a QoS or congestion problem, not DNS.*
    - @5.4.perf
24. Match each to its Wi-Fi issue. Type the letters in order, e.g. abcd. ¶  Calls drop walking from AP1 to AP2, which have different passphrases · a microwave kills 2.4 GHz at lunch · a far corner at -84 dBm · a deauth flood in the logs ¶  A roaming misconfiguration · B client disassociation · C interference · D insufficient coverage
    - [=] acdb | a c d b | a,c,d,b
    - *Different security on each AP = roaming misconfiguration. Microwave = interference. -84 dBm = insufficient coverage. Deauth floods = client disassociation.*
    - @5.4.wifi
25. An SNMP graph: ¶  WAN 100 Mbps · baseline 30-40 Mbps · Mon-Fri 09:00-09:30 = 100 Mbps, output drops 12,000 ¶NetFlow top talker at 09:00 = Windows Update from 400 PCs. Best fix?
    - **[x] Stagger the updates or use a local cache**  - [ ] Upgrade the WAN link to 1 Gbps  - [ ] Replace the WAN router with a faster one  - [ ] Lengthen the DHCP lease time
    - *A predictable burst from one non-urgent source = reschedule it (stagger updates, or use a local WSUS/cache). QoS to deprioritise it also works. Buying bandwidth for a 30-minute peak is the expensive choice.*
    - @5.4.perf
26. PBQ: Wi-Fi complaints. Readings from a site survey tool on a laptop: ¶  Area      RSSI    SNR    Ch util  Channel ¶  Lobby    -45 dBm  35 dB   85%     6 ¶  Office   -52 dBm  30 dB   20%     36 ¶  Store    -82 dBm   8 dB   15%     11 ¶  Lab      -50 dBm  12 dB   30%     1
    - [p] Lobby problem :: A weak signal · B channel congestion · C interference · D no problem = b
    - [p] Office problem :: A weak signal · B channel congestion · C interference · D no problem = d
    - [p] Store problem :: A weak signal · B channel congestion · C interference · D no problem = a
    - [p] Lab problem :: A weak signal · B channel congestion · C interference · D no problem = c
    - *Good RSSI is -67 dBm or better, and SNR 25 dB or more is healthy. Lobby: strong signal but 85% utilisation = contention: more capacity. Office: all good. Store: -82 dBm is too weak, so coverage is the gap. Lab: a strong signal but 12 dB SNR = a noisy channel (microwave, Bluetooth, a neighbour AP), so find the source or move off it.*
    - @5.4.wifi

### Key facts
- **Congestion/contention = too much traffic or too many talkers (fix: QoS, shaping, more capacity, more APs) · bottleneck = the slowest link → upgrade it · bandwidth = capacity vs throughput = actual.**
- **Latency = steady delay (distance → CDN) · jitter = variable delay (voice → QoS) · packet loss = ping %.**
- **Tools: ping, tracert/traceroute, SNMP vs baseline, NetFlow top talkers. Load 255/255 = saturated.**
- **Wi-Fi: interference/overlap → 1/6/11, 5/6 GHz · insufficient coverage → heat map + add an AP · disassociation → 802.11w PMF · roaming → same SSID, same security, 15-20% overlap.**

## Test 31 - 5.5 CLI Tools (33 Q)

1. A user says the file server "is down". Type the first command you'd run from their PC to test if the server answers at all.
   - [=] ping
   - *ping = ICMP (Internet Control Message Protocol) echo request/reply: reachability, round-trip time, loss. No reply doesn't always mean the host is down: firewalls often block ICMP. Try a TCP test such as Test-NetConnection -Port 443 or nc -zv.*
   - @5.5.cli ~22.21
2. From a Linux box, pings to 203.0.113.50 time out. Type the command that shows at which router along the path they stop.
   - [=] traceroute | traceroute 203.0.113.50
   - *traceroute (Linux/macOS) sends UDP probes by default, with rising TTL (Time To Live); each router that drops a probe replies "time exceeded". -I uses ICMP, -T uses TCP. Windows spells it differently.*
   - @5.5.cli ~22.22
3. The same fault, but from a Windows PC. Type the command that shows each hop to the host.
   - [=] tracert
   - *tracert = Windows, using ICMP echo with rising TTL. * * * = that hop doesn't reply, which is often just a filter, not a fault, if later hops still answer.*
   - @5.5.cli ~22.23
4. A Windows user can reach 10.0.0.20 by IP but not intranet.corp by name. Type the built-in tool to query DNS for that name.
   - [=] nslookup | nslookup intranet.corp
   - *nslookup name server = ask a specific DNS server. It exists on Linux too, but dig is the preferred Linux/macOS tool. Windows PowerShell also has Resolve-DnsName.*
   - @5.5.cli ~22.24
5. On Linux, you need to see the TTL and which server answered for a DNS record that seems stale. Type the tool.
   - [=] dig
   - *dig (Domain Information Groper) = dig name type @server, e.g. dig example.com MX @8.8.8.8. +short trims the output.*
   - @5.5.cli ~23.1
6. A Linux server with no GUI must capture traffic to prove the firewall is dropping it. Type the capture tool.
   - [=] tcpdump
   - *tcpdump = CLI capture using libpcap and BPF (Berkeley Packet Filter) expressions. Save with -w for Wireshark to open. Windows equivalents: pktmon, or Wireshark's own dumpcap.*
   - @5.5.cli ~22.25
7. You need to see which ports a Windows server is LISTENING on, as well as its open connections. Type the netstat flag.
   - [=] -a
   - *-a = all, including LISTENING. -n = numeric, no DNS lookups (faster). -o = PID (Windows). -b = the executable name (Windows, needs admin). -r = the routing table.*
   - @5.5.cli ~23.2
8. An unknown connection to a foreign IP appears on a Windows PC. Type the netstat flag that shows which program owns it.
   - [=] -b
   - *netstat -b (run as administrator) = the program name, like chrome.exe. -o gives just the PID. On Linux, -p shows the PID/program name.*
   - @5.5.cli ~23.3
9. A Windows PC can't reach anything. Type the command that shows its IP address, mask and gateway.
   - [=] ipconfig | ipconfig /all
   - *ipconfig = the Windows network config tool. ifconfig = legacy Linux/macOS. ip = modern Linux. iwconfig = Linux wireless. iptables = the Linux firewall.*
   - @5.5.cli ~23.4
10. A DNS record was fixed, but one PC still goes to the old IP. Type the ipconfig switch that clears its cached answer.
    - [=] /flushdns
    - */flushdns = clear it, /displaydns = show it, /registerdns = re-register the PC's name in DNS. Use it after changing DNS records or the hosts file, if the old answer sticks.*
    - @5.5.cli ~23.6
11. What resolution does the arp command show?
    - **[x] IP to MAC**  - [ ] MAC to IP  - [ ] IP to FQDN  - [ ] FQDN to IP
    - *ARP (Address Resolution Protocol) = the IP → MAC mapping on the local subnet. DNS = name → IP. arp -a shows the cache.*
    - @5.5.cli ~23.10,23.11
12. A Windows laptop gets an address but cannot browse. You need its DNS server list and adapter hardware address along with the usual IP details. Type the command.
    - [=] ipconfig /all
    - *ipconfig on its own lists only address, mask and gateway. Adding /all reveals DNS servers, the DHCP server, lease times and the physical (MAC) address.*
    - @5.5.cli ~30.1,23.5
13. On an Ubuntu server, type the current iproute2 command, in its shortest form, that lists every interface with its addresses.
    - [=] ip a | ip addr | ip address | ip addr show | ip a s
    - *ip a is the modern replacement for ifconfig. It shows link state, MAC and each IPv4 and IPv6 address per interface. The objectives still name ifconfig too.*
    - @5.5.cli ~30.2
14. An older Linux appliance has only the legacy net-tools package. Type the command that lists its interfaces and addresses.
    - [=] ifconfig | ifconfig -a
    - *ifconfig comes from net-tools and is still found on older Linux and on macOS. The -a flag also lists interfaces that are down.*
    - @5.5.cli ~30.3
15. A Windows PC holds a stale address from the wrong scope. Type the command that gives that lease back to the DHCP server.
    - [=] ipconfig /release
    - */release gives up the current lease and /renew then requests a new one. Running the pair is the usual way to get fresh addressing.*
    - @5.5.cli ~30.4,23.7
16. After moving a Windows desktop to a new VLAN, type the command that makes it ask DHCP for a fresh address.
    - [=] ipconfig /renew
    - */renew restarts the DORA exchange. If the PC still ends up with 169.254.x.x, no DHCP server replied, so check the relay or scope.*
    - @5.5.cli ~30.5
17. A Linux host cannot reach other subnets. Type a command that prints its routes, including which gateway it uses by default.
    - [=] ip r | ip route | ip route show | route -n | netstat -rn | netstat -r
    - *Look for the line starting with default via, which is the gateway. The older equivalent is route -n.*
    - @5.5.cli ~30.7
18. On a Windows server with two NICs, type a command that lists its IPv4 and IPv6 route table.
    - [=] route print | netstat -r | netstat -rn
    - *route print and netstat -r both show the Windows routing table. On a Cisco router the equivalent is show ip route.*
    - @5.5.cli ~30.8
19. You suspect a host has a wrong IP-to-hardware mapping cached for its gateway. Type a command, Windows or Linux, that displays that cache.
    - [=] arp -a | ip neigh | ip n | ip neighbor
    - *arp -a works on both Windows and Linux. On modern Linux, ip neigh shows the same neighbour table.*
    - @5.5.cli ~30.9
20. You want to watch for drops on a flaky link while you wiggle cables. On Windows, type a ping to 10.0.0.1 that keeps going until you stop it with Ctrl+C.
    - [=] ping -t 10.0.0.1 | ping 10.0.0.1 -t
    - *-t keeps Windows ping running indefinitely. Linux ping already runs until stopped.*
    - @5.5.cli ~30.10
21. On a Linux box, type a ping to 10.0.0.1 that sends four echo requests and then stops by itself.
    - [=] ping -c 4 10.0.0.1 | ping 10.0.0.1 -c 4
    - *Linux uses -c for count. Windows uses -n for the same job.*
    - @5.5.cli ~30.11
22. In a Windows batch script, type a ping to 10.0.0.1 that explicitly sets the number of echoes to four.
    - [=] ping -n 4 10.0.0.1 | ping 10.0.0.1 -n 4
    - *Four is already the Windows default, but -n makes it explicit. Related flags: -l sets payload size, and -f sets Don't Fragment.*
    - @5.5.cli ~30.12
23. From a Windows workstation, type the command that lists every router hop toward example.com.
    - [=] tracert example.com
    - *tracert is the Windows spelling and sends ICMP probes. On Linux the tool is traceroute, which uses UDP by default.*
    - @5.5.cli ~30.13
24. From a Linux terminal, type a command that maps the router hops to example.com.
    - [=] traceroute example.com | tracepath example.com | mtr example.com
    - *traceroute is the classic tool, with -I for ICMP and -n to skip name lookups. mtr runs continuously and shows loss per hop.*
    - @5.5.cli ~30.14
25. To test whether Google's public resolver at 8.8.8.8 resolves example.com correctly, type an nslookup command that queries that server directly.
    - [=] nslookup example.com 8.8.8.8
    - *The syntax is nslookup name server. Leave out the server and it asks the system's configured resolver.*
    - @5.5.cli ~30.15
26. On Linux, type a dig command that sends the query for example.com straight to 8.8.8.8 instead of the local resolver.
    - [=] dig @8.8.8.8 example.com | dig example.com @8.8.8.8
    - *With dig, @server picks the server to ask, which proves whether that particular server answers correctly.*
    - @5.5.cli ~30.16
27. Type a netstat command that lists every connection and listening socket, showing numbers instead of resolving names.
    - [=] netstat -an | netstat -na | netstat -a -n
    - *-a includes listening sockets and -n skips DNS and service-name lookups. On modern Linux, ss -tulpn is preferred.*
    - @5.5.cli ~30.17
28. You need to sniff traffic on a headless Linux server's eth0 interface. Type the capture command.
    - [=] tcpdump -i eth0 | sudo tcpdump -i eth0
    - *-i picks the interface. tcpdump needs root privileges, and Ctrl+C ends the capture.*
    - @5.5.cli ~30.18
29. PBQ: Users on floor 2 report problems. Gateway R1 Gi0/1 = 192.168.10.1/24, DHCP and DNS server 192.168.10.53, user VLAN 10. ¶  PC-A C:\> ipconfig /all ¶     IPv4 Address. . . . . . . . . . . : 192.168.10.21 ¶     Subnet Mask . . . . . . . . . . . : 255.255.255.0 ¶     Default Gateway . . . . . . . . . : 192.168.10.1 ¶     DNS Servers . . . . . . . . . . . : 192.168.10.53 ¶  PC-B C:\> ipconfig /all ¶     IPv4 Address. . . . . . . . . . . : 192.168.10.140 ¶     Subnet Mask . . . . . . . . . . . : 255.255.255.128 ¶     Default Gateway . . . . . . . . . : 192.168.10.1 ¶     DNS Servers . . . . . . . . . . . : 192.168.10.53 ¶  PC-B C:\> ping 192.168.10.1 ¶    PING: transmit failed. General failure. ¶  PC-C C:\> ipconfig /all ¶     Autoconfiguration IPv4 Address. . : 169.254.77.12 ¶     Subnet Mask . . . . . . . . . . . : 255.255.0.0 ¶     Default Gateway . . . . . . . . . : ¶  PC-D C:\> ipconfig /all ¶     IPv4 Address. . . . . . . . . . . : 192.168.10.33 ¶     Subnet Mask . . . . . . . . . . . : 255.255.255.0 ¶     Default Gateway . . . . . . . . . : 192.168.10.1 ¶     DNS Servers . . . . . . . . . . . : 192.168.10.254 ¶  PC-D C:\> nslookup intranet.corp ¶    DNS request timed out. ¶ ¶  SW2# show interfaces status ¶  Port   Name  Status     Vlan  Duplex  Speed ¶  Gi0/1  PC-A  connected  10    a-full  a-1000 ¶  Gi0/2  PC-B  connected  10    a-full  a-1000 ¶  Gi0/3  PC-C  connected  30    a-full  a-1000 ¶  Gi0/4  PC-D  connected  10    a-full  a-1000
    - [p] PC-B fault :: A wrong subnet mask · B wrong gateway · C wrong DNS server · D switch port in the wrong VLAN · E no fault = a
    - [p] Type the mask PC-B should have, dotted decimal = 255.255.255.0 | /24
    - [p] PC-C fault :: A wrong subnet mask · B wrong gateway · C wrong DNS server · D switch port in the wrong VLAN · E no fault = d
    - [p] Type the VLAN SW2 Gi0/3 must be moved to = 10
    - [p] PC-D fault :: A wrong subnet mask · B wrong gateway · C wrong DNS server · D switch port in the wrong VLAN · E no fault = c
    - *PC-A is the working baseline to compare against. PC-B: /25 puts .140 in 192.168.10.128/25, so the gateway .1 is off-link and Windows can't even send. PC-C: 169.254 (Autoconfiguration) = APIPA, DHCP failed, and show interfaces status shows its port in VLAN 30, where there's no DHCP server. Changing its IP by hand is the trap; fix the port, then ipconfig /renew. PC-D has a good IP but asks .254 for names instead of .53.*
    - @5.3.ip
30. PBQ: Real outputs (Linux laptop + Windows PC, IPs/MACs redacted). Which command made each? ¶  (1) Ethernet adapter Ethernet: ¶      IPv4 Address. . . . . . . . . . . : 192.168.1.143 ¶      Subnet Mask . . . . . . . . . . . : 255.255.255.0 ¶      Default Gateway . . . . . . . . . : 192.168.1.1 ¶  (2) ens18: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500 ¶          inet 192.168.1.12  netmask 255.255.255.0  broadcast 192.168.1.255 ¶  (3) Interface: 192.168.1.143 --- 0x9 ¶        Internet Address      Physical Address      Type ¶        192.168.1.1           AA-BB-CC-00-02-0B     dynamic ¶        255.255.255.255       FF-FF-FF-FF-FF-FF     static ¶  (4) host.lan (192.168.1.1) at aa:bb:cc:00:00:07 ［ether］ on ens18 ¶      ? (192.168.1.10) at aa:bb:cc:00:00:08 ［ether］ on ens18 ¶  (5) 192.168.1.1 dev ens18 lladdr aa:bb:cc:00:00:07 REACHABLE ¶      192.168.1.192 dev ens18 lladdr aa:bb:cc:00:00:06 STALE ¶  (6) Server:  host.lan ¶      Address:  192.168.1.1 ¶      Non-authoritative answer: ¶      Name:    google.com ¶      Addresses:  198.51.100.14 ¶  (7) ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 19485 ¶      ;; ANSWER SECTION: ¶      google.com.   300   IN   A   198.51.100.142 ¶  (8) google.com has address 198.51.100.142 ¶      google.com mail is handled by 10 smtp.google.com.
    - [p] Output (1) :: A ipconfig (Windows) · B ifconfig (Linux) · C ip neigh (Linux) · D arp -a (Windows) · E arp -a (Linux) · F nslookup · G dig · H host = a
    - [p] Output (2) :: A ipconfig (Windows) · B ifconfig (Linux) · C ip neigh (Linux) · D arp -a (Windows) · E arp -a (Linux) · F nslookup · G dig · H host = b
    - [p] Output (3) :: A ipconfig (Windows) · B ifconfig (Linux) · C ip neigh (Linux) · D arp -a (Windows) · E arp -a (Linux) · F nslookup · G dig · H host = d
    - [p] Output (4) :: A ipconfig (Windows) · B ifconfig (Linux) · C ip neigh (Linux) · D arp -a (Windows) · E arp -a (Linux) · F nslookup · G dig · H host = e
    - [p] Output (5) :: A ipconfig (Windows) · B ifconfig (Linux) · C ip neigh (Linux) · D arp -a (Windows) · E arp -a (Linux) · F nslookup · G dig · H host = c
    - [p] Output (6) :: A ipconfig (Windows) · B ifconfig (Linux) · C ip neigh (Linux) · D arp -a (Windows) · E arp -a (Linux) · F nslookup · G dig · H host = f
    - [p] Output (7) :: A ipconfig (Windows) · B ifconfig (Linux) · C ip neigh (Linux) · D arp -a (Windows) · E arp -a (Linux) · F nslookup · G dig · H host = g
    - [p] Output (8) :: A ipconfig (Windows) · B ifconfig (Linux) · C ip neigh (Linux) · D arp -a (Windows) · E arp -a (Linux) · F nslookup · G dig · H host = h
    - *Answer: 1 ipconfig · 2 ifconfig · 3 Windows arp -a · 4 Linux arp -a · 5 ip neigh · 6 nslookup · 7 dig · 8 host. TELLS: ipconfig = dotted leader lines '. . . . :' and 'Ethernet adapter X:'. ifconfig = 'flags=<UP,...> mtu' then 'inet .. netmask ..' on one line. Windows arp -a = 'Interface: x --- 0x9' header, DASHED MACs, dynamic/static column. Linux arp -a = '? (ip) at mac ［ether］ on ens18' prose, COLON MACs. ip neigh = 'dev ens18 lladdr' + REACHABLE/STALE. nslookup = 'Server:' / 'Address:' of the resolver first, then 'Non-authoritative answer:'. dig = ';;' comment lines, '->>HEADER<<-' status NOERROR, ';; ANSWER SECTION:' with TTL and IN A. host = one plain English sentence: 'has address', 'mail is handled by'. Hook: dashes = Windows, colons = Linux; semicolons = dig; 'Server:' first = nslookup; a sentence = host.*
    - @5.5.cli
31. PBQ: More real outputs. Which command made each? ¶  (1) Tracing route to dns.google ［8.8.8.8］ ¶      over a maximum of 30 hops: ¶        1    <1 ms    <1 ms    <1 ms  host.lan ［192.168.1.1］ ¶        4    24 ms    24 ms    22 ms  100.64.32.1 ¶      Trace complete. ¶  (2) traceroute to 8.8.8.8 (8.8.8.8), 30 hops max, 60 byte packets ¶       1  host.lan (192.168.1.1)  0.461 ms  0.401 ms  0.379 ms ¶       4  203.0.113.17 (203.0.113.17)  30.529 ms  34.781 ms  34.753 ms ¶  (3) Computing statistics for 250 seconds... ¶                  Source to Here   This Node/Link ¶      Hop  RTT    Lost/Sent = Pct  Lost/Sent = Pct  Address ¶       12   46ms     1/  10 = 10%     1/  10 = 10%  198.51.100.87 ¶  (4) HOST: host        Loss%   Snt   Last   Avg  Best  Wrst StDev ¶        1.|-- host.lan    0.0%     5    0.3   0.5   0.3   0.8   0.2 ¶  (5) Reply from 8.8.8.8: bytes=32 time=46ms TTL=113 ¶  (6) 64 bytes from 8.8.8.8: icmp_seq=1 ttl=113 time=34.2 ms ¶  (7) Proto  Local Address          Foreign Address        State ¶      TCP    0.0.0.0:445            0.0.0.0:0              LISTENING ¶      TCP    192.168.1.143:3389     100.64.27.1:44550        ESTABLISHED ¶  (8) Netid State  Recv-Q Send-Q   Local Address:Port  Peer Address:Port ¶      tcp   LISTEN 0      128          0.0.0.0:22         0.0.0.0:* ¶  (9) 18:34:47.800715 IP 192.168.1.12 > 192.168.1.1: ICMP echo request, id 2105, seq 1, length 64 ¶      18:34:45.208071 IP 198.51.100.65.443 > 192.168.1.12.58430: Flags ［P.］, seq 5792:5843 ¶  (10) TCP    192.168.1.143:3389     100.64.27.1:44550        ESTABLISHED ¶         TermService ¶        ［svchost.exe］
    - [p] Output (1) :: A tracert (Windows) · B traceroute (Linux) · C pathping (Windows) · D mtr (Linux) · E ping (Windows) · F ping (Linux) · G netstat -an (Windows) · H ss -tuln (Linux) · I tcpdump · J netstat -b (Windows) = a
    - [p] Output (2) :: A tracert (Windows) · B traceroute (Linux) · C pathping (Windows) · D mtr (Linux) · E ping (Windows) · F ping (Linux) · G netstat -an (Windows) · H ss -tuln (Linux) · I tcpdump · J netstat -b (Windows) = b
    - [p] Output (3) :: A tracert (Windows) · B traceroute (Linux) · C pathping (Windows) · D mtr (Linux) · E ping (Windows) · F ping (Linux) · G netstat -an (Windows) · H ss -tuln (Linux) · I tcpdump · J netstat -b (Windows) = c
    - [p] Output (4) :: A tracert (Windows) · B traceroute (Linux) · C pathping (Windows) · D mtr (Linux) · E ping (Windows) · F ping (Linux) · G netstat -an (Windows) · H ss -tuln (Linux) · I tcpdump · J netstat -b (Windows) = d
    - [p] Output (5) :: A tracert (Windows) · B traceroute (Linux) · C pathping (Windows) · D mtr (Linux) · E ping (Windows) · F ping (Linux) · G netstat -an (Windows) · H ss -tuln (Linux) · I tcpdump · J netstat -b (Windows) = e
    - [p] Output (6) :: A tracert (Windows) · B traceroute (Linux) · C pathping (Windows) · D mtr (Linux) · E ping (Windows) · F ping (Linux) · G netstat -an (Windows) · H ss -tuln (Linux) · I tcpdump · J netstat -b (Windows) = f
    - [p] Output (7) :: A tracert (Windows) · B traceroute (Linux) · C pathping (Windows) · D mtr (Linux) · E ping (Windows) · F ping (Linux) · G netstat -an (Windows) · H ss -tuln (Linux) · I tcpdump · J netstat -b (Windows) = g
    - [p] Output (8) :: A tracert (Windows) · B traceroute (Linux) · C pathping (Windows) · D mtr (Linux) · E ping (Windows) · F ping (Linux) · G netstat -an (Windows) · H ss -tuln (Linux) · I tcpdump · J netstat -b (Windows) = h
    - [p] Output (9) :: A tracert (Windows) · B traceroute (Linux) · C pathping (Windows) · D mtr (Linux) · E ping (Windows) · F ping (Linux) · G netstat -an (Windows) · H ss -tuln (Linux) · I tcpdump · J netstat -b (Windows) = i
    - [p] Output (10) :: A tracert (Windows) · B traceroute (Linux) · C pathping (Windows) · D mtr (Linux) · E ping (Windows) · F ping (Linux) · G netstat -an (Windows) · H ss -tuln (Linux) · I tcpdump · J netstat -b (Windows) = j
    - *Answer: 1 tracert · 2 traceroute · 3 pathping · 4 mtr · 5 Windows ping · 6 Linux ping · 7 netstat -an · 8 ss -tuln · 9 tcpdump · 10 netstat -b. TELLS: tracert = 'Tracing route to', times BEFORE the host, ends 'Trace complete.'. traceroute = lower-case 'traceroute to .. 60 byte packets', host BEFORE the times, no ending line. pathping = 'Computing statistics for N seconds' + Lost/Sent = Pct per hop (trace + ping in one). mtr = Linux live version: Loss% Snt Last Avg Best Wrst StDev. Windows ping = 'Reply from .. bytes=32 TTL=' (capital TTL, 32 bytes). Linux ping = '64 bytes from .. icmp_seq= ttl=' (lower case, 64 bytes, runs until Ctrl+C unless -c). Windows netstat = 'LISTENING' and foreign '0.0.0.0:0'. ss = 'Netid State Recv-Q Send-Q' and 'LISTEN' with '*'. (Linux netstat says 'LISTEN' and 'Active Internet connections'.) tcpdump = timestamp + 'IP src.port > dst.port:' + Flags ［S］/［P.］/［.］. netstat -b = the owning program in ［brackets］ under each line (needs admin).*
    - @5.5.cli
32. You ping 1.1.1.1 successfully, then run arp -a. 1.1.1.1's MAC isn't listed. Why?
    - **[x] 1.1.1.1 is off the local subnet, so frames go to the default gateway's MAC instead**  - [ ] arp -a only shows static entries  - [ ] ICMP doesn't use ARP  - [ ] The ARP cache expired instantly
    - *Answer: It's off the local subnet. ARP only resolves addresses on YOUR subnet. For anything remote the PC ARPs for the gateway and sends the frame to the gateway's MAC; routers rewrite the MACs at every hop. So arp -a shows the gateway's MAC, never 1.1.1.1's. Hook: MACs are local; IPs go the distance.*
    - @5.5.cli
33. From a Windows command prompt, which command shows the FQDN registered for 1.1.1.1?
    - [=] nslookup 1.1.1.1
    - *Answer: nslookup 1.1.1.1, which returns one.one.one.one. Give nslookup an IP and it automatically does a reverse (PTR) lookup. On Linux/macOS use dig -x 1.1.1.1; plain dig 1.1.1.1 treats the IP as a name and finds nothing. Windows doesn't ship dig. Hook: nslookup reverses on its own; dig needs the -x.*
    - @5.5.cli

### Key facts
- **ping (ICMP echo) · Windows: -t forever, -n count, -l size, -f don't fragment · Linux: -c count.**
- **tracert (Windows, ICMP) · traceroute (Linux, UDP) · -d = no name lookups · ping -n (Windows) / -c (Linux) = count.**
- **ipconfig /all · /release · /renew · /flushdns · /displaydns. Linux: ip a, ip r, ip neigh, ip link set eth0 up (old: ifconfig, route -n).**
- **arp -a = IP → MAC cache · arp -d * = clear it. netstat -a all · -n numeric · -o PID · -b executable · -r routes · Linux ss -tulpn.**
- **nslookup name server · nslookup -type=mx · dig @server name type · dig +short · dig -x IP (reverse).**
- **tcpdump -i eth0 · -w file.pcap save · -r read · -n no DNS · filters: port 53, host 10.0.0.9.**

## Test 32 - 5.5 Software Tools (17 Q)

1. A tech opens Wireshark to see exactly what a misbehaving app sends on the wire. What is this kind of tool mainly for?
   - **[x] Capturing traffic and decoding it packet by packet**  - [ ] Controlling which users can reach each service  - [ ] Tracking employees' browsing for HR  - [ ] Blocking web traffic by category
   - *A protocol analyser, or packet sniffer such as Wireshark or tcpdump, captures frames and decodes every header and payload. It observes traffic and does not block it.*
   - @5.5.sw ~22.20
2. Type the Wireshark display filter that shows only DNS traffic.
   - [=] dns
   - *Wireshark DISPLAY filters: dns, http, tcp.port == 443, ip.addr == 10.0.0.9, tcp.flags.syn == 1. CAPTURE filters use tcpdump/BPF syntax instead: port 53, host 10.0.0.9. Hook: display = Wireshark language, capture = tcpdump language.*
   - @5.5.sw
3. Type the Wireshark display filter that shows traffic to or from 10.0.0.9.
   - [=] ip.addr == 10.0.0.9 | ip.addr==10.0.0.9
   - *ip.addr matches either source or destination. ip.src / ip.dst for one direction. && and || combine filters.*
   - @5.5.sw
4. Type the name of the open-source command-line scanner that sweeps a subnet for live hosts and open ports.
   - [=] nmap
   - *nmap performs host discovery, port scans and service or OS detection, for example nmap -sV 10.0.0.0/24. Use it only on networks you are authorised to scan.*
   - @5.5.sw ~23.12
5. Which VENDOR-NEUTRAL Layer 2 protocol do devices use to advertise their identity and capabilities to neighbours?
   - **[x] LLDP**  - [ ] CDP  - [ ] STP  - [ ] SNMP
   - *LLDP (Link Layer Discovery Protocol, IEEE 802.1AB) = switches, phones, APs and servers announce their name, port, VLAN and capabilities. LLDP-MED (Media Endpoint Discovery) also tells phones the voice VLAN. It's the best choice in MULTI-VENDOR networks.*
   - @5.5.sw ~23.13,23.15
6. Two Cisco routers are connected and you want each to list the other's model, IP and port without logging into it. Which vendor-specific discovery protocol does this?
   - [ ] LLDP  - **[x] CDP**  - [ ] VTP  - [ ] PAgP
   - *CDP (Cisco Discovery Protocol) is Cisco-only. LLDP (Link Layer Discovery Protocol, 802.1AB) is the vendor-neutral equivalent. View neighbours with show cdp neighbors or show lldp neighbors.*
   - @5.5.sw ~23.14
7. Type the Cisco command that lists directly connected Cisco neighbours and the local and remote ports.
   - [=] show cdp neighbors | show cdp neighbors detail | show cdp nei | show cdp neighbours
   - *show cdp neighbors = Device ID, local interface, platform, remote port. Add detail for IPs and the IOS version. For multi-vendor gear: show lldp neighbors. It builds a map without walking the building.*
   - @5.5.sw
8. Type the vendor-neutral equivalent command on a Cisco switch.
   - [=] show lldp neighbors | show lldp neighbors detail | show lldp nei | show lldp neighbours
   - *LLDP is often off by default on Cisco: turn it on with lldp run in global config.*
   - @5.5.sw
9. What issues can a speed tester diagnose?
   - [ ] Slow internet speeds  - [ ] Inconsistent performance  - [ ] Whether the ISP is delivering the contracted speed  - **[x] All of the above**
   - *Answer: All of the above. Speed tester = speedtest.net / fast.com against an internet server, measuring download, upload, latency and jitter. Run it wired to rule out Wi-Fi. For internal links, use iperf.*
   - @5.5.sw ~23.16
10. To prove whether a new 10 Gbps link between two servers really delivers its rated speed, a tech runs a client and a server that push traffic between them. Which tool is this?
    - [ ] nslookup  - [ ] Wireshark only  - **[x] iperf**  - [ ] Toner
    - *iperf generates TCP or UDP test traffic between two endpoints and reports real throughput, jitter and loss. Run it in server mode on one end and client mode on the other.*
    - @5.5.sw ~27.18
11. A user on a 500 Mbps plan says "the internet is slow". What should the technician run FIRST to check the service against the plan?
    - **[x] A speed test from the user's PC, then a wired one**  - [ ] iperf3 between two servers in the data centre  - [ ] A protocol analyser on the core switch  - [ ] nmap against the ISP's gateway router
    - *A speed tester measures real throughput to the internet, to compare against what the ISP sells. Testing again wired at the edge rules out Wi-Fi and the LAN. iperf3 tests INTERNAL throughput between two hosts you control. nmap finds open ports, not bandwidth.*
    - @5.5.sw ~27.17
12. Type a tcpdump command that listens on eth0 and writes the packets to cap.pcap so you can open it later in Wireshark.
    - [=] tcpdump -i eth0 -w cap.pcap | sudo tcpdump -i eth0 -w cap.pcap
    - *-w writes raw packets to a pcap file. Remember w for write and r for read.*
    - @5.5.sw ~32.10
13. A colleague emails you cap.pcap. Type the tcpdump command that replays its contents on screen.
    - [=] tcpdump -r cap.pcap
    - *-r reads an existing capture file. Reading a file does not require root.*
    - @5.5.sw ~32.11
14. Type a tcpdump command that captures on eth0 but keeps only DNS traffic on port 53.
    - [=] tcpdump -i eth0 port 53 | sudo tcpdump -i eth0 port 53 | tcpdump -i eth0 -n port 53 | tcpdump -i eth0 -nn port 53
    - *Filter expressions go after the options, for example port, host, net, or a protocol like tcp or udp, combined with and, or and not.*
    - @5.5.sw ~32.12
15. A sensor logs this from 172.16.5.80 within one second: ¶09:14:07 IP 172.16.5.80.40211 > 172.16.5.12.21: Flags S ¶09:14:07 IP 172.16.5.80.40212 > 172.16.5.12.80: Flags S ¶09:14:07 IP 172.16.5.80.40213 > 172.16.5.12.443: Flags S ¶09:14:07 IP 172.16.5.80.40214 > 172.16.5.12.3389: Flags S ¶What activity does this most likely show?
    - [ ] Normal web browsing  - [ ] A DNS zone transfer  - **[x] A port scan against 172.16.5.12**  - [ ] A DHCP request
    - *One source fires SYNs at many different destination ports at the same instant, using consecutive source ports. That is a SYN scan, like nmap -sS. In tcpdump output, S means SYN and R means RST.*
    - @5.5.sw ~29.24
16. A scan shows: ¶  $ nmap 10.0.0.20 ¶  PORT     STATE     SERVICE ¶  22/tcp   open      ssh ¶  23/tcp   filtered  telnet ¶  443/tcp  closed    https ¶Match each meaning to its nmap state. Type the letters in order, e.g. abc. ¶  No reply, a firewall probably dropped it · host answered with RST, nothing listening · a service answered ¶  A closed · B open · C filtered
    - [=] cab | c a b | c,a,b
    - *open = SYN-ACK came back. closed = RST, so the host is up but nothing's listening. filtered = no response or ICMP unreachable, so a firewall is in the way. Hook: filtered = the firewall ate it.*
    - @5.5.sw
17. Type the tcpdump command that captures on eth0 only traffic between host 10.0.0.9 and port 443, with no name resolution.
    - [=] tcpdump -i eth0 -n host 10.0.0.9 and port 443 | tcpdump -i eth0 -n host 10.0.0.9 && port 443 | tcpdump -n -i eth0 host 10.0.0.9 and port 443 | sudo tcpdump -i eth0 -n host 10.0.0.9 and port 443 | tcpdump -i eth0 -nn host 10.0.0.9 and port 443 | tcpdump -n -i eth0 host 10.0.0.9 && port 443
    - *BPF primitives: host, net 10.0.0.0/24, port, src, dst, tcp, udp, icmp. Two primitives MUST be joined: host 10.0.0.9 && port 443. The words and / or / not are valid in place of && / || / ! and mean exactly the same (the exam and man pages usually use the words). host 10.0.0.9 port 443 with nothing between is a syntax error. Each flag takes its own value: -i eth0, so -i -n eth0 would try to capture on an interface called -n. -n stops DNS lookups, and -nn also stops port-name lookups.*
    - @5.5.sw

### Key facts
- **Protocol analyser (Wireshark, tcpdump) = capture + decode · display filters: dns, ip.addr == x, tcp.port == 443 · capture filters: host, port, net (BPF).**
- **nmap: -sn sweep · -sS SYN · -sT connect · -sU UDP · -sV versions · -O OS · -A aggressive · -p 22,80 / -p- · -Pn skip ping. States: open, closed (RST), filtered (firewall).**
- **tcpdump: -i interface · -n numeric · -w save · -r read · host / port / and.**
- **LLDP (802.1AB, vendor-neutral, LLDP-MED voice VLAN) · CDP (Cisco) → show cdp neighbors / show lldp neighbors.**
- **Speed tester = to the internet · iperf3 -s / -c = internal throughput · ping -n (Windows) / -c (Linux) = count, for loss %.**

## Test 33 - 5.5 Hardware Tools (24 Q)

1. Hardware tool to trace and identify one cable within a bundle or wall?
   - [ ] Cable certifier  - [ ] Line tester  - **[x] Toner and probe kit**  - [ ] Wire mapper
   - *Toner (tone generator) = clip it to one end; the probe beeps near the matching wire at the other end, e.g. in the patch panel. It finds unlabelled cables. Hook: TONE to find it, TEST to prove it.*
   - @5.5.hw ~23.17
2. Security wants a passive copy of every frame on the internet uplink for its IDS, without becoming a point of failure in the path. Which device fits?
   - [ ] Transceiver  - [ ] Repeater  - [ ] Ethernet adapter  - **[x] Network TAP**
   - *A TAP (Test Access Point) is inline hardware that copies all traffic, including errored frames, to a monitor port and passes traffic even if it fails. A SPAN or mirror port is the switch-based alternative.*
   - @5.5.hw ~23.19
3. Which task falls outside what a Wi-Fi analyser is built to do?
   - [ ] Showing RSSI for nearby networks  - [ ] Spotting sources of RF interference  - [ ] Displaying which channels are crowded  - **[x] Capturing and decoding the contents of packets**
   - *A Wi-Fi analyser deals with RF: signal strength, channels, SSIDs and interference. Decoding packets is the job of a protocol analyser such as Wireshark.*
   - @5.5.hw ~23.20
4. Which of these LOCATES a fault in a COPPER cable?
   - [ ] A multimeter set to continuity  - [ ] A visual fault locator on the pair  - [ ] A loopback plug in the far jack  - **[x] None of the above: it's a TDR or cable certifier**
   - *Answer: None of the above: it's a TDR or cable certifier. A VFL (Visual Fault Locator) = shines red laser light into FIBRE so breaks and bends glow: fibre only. A multimeter tests continuity but doesn't give a location. A TDR (Time-Domain Reflectometer), or a certifier with TDR, gives the distance to a copper fault.*
   - @5.5.hw ~23.21
5. Which tool shines visible red light into a fibre so that breaks and tight bends glow through the jacket?
   - **[x] Visual fault locator**  - [ ] Optical power meter  - [ ] Toner and probe  - [ ] Fusion splicer
   - *VFL = a cheap red laser pen, good for patch leads and short runs up to a few km. The OTDR gives exact distances on long runs.*
   - @5.5.hw
6. A backbone fibre between buildings has failed and you need to know how many metres along the run the break is. Which tool do you use?
   - [ ] Multimeter  - [ ] Tone generator  - **[x] OTDR**  - [ ] Copper certifier
   - *An OTDR (Optical Time-Domain Reflectometer) sends light pulses and times the reflections to show length, splices and the distance to faults. A light meter only measures total loss.*
   - @5.5.hw ~26.14
7. To confirm a copper conductor is unbroken end to end, a tech measures the ohms between its two ends. Which tool is this?
   - [ ] OTDR  - **[x] Multimeter**  - [ ] Toner probe  - [ ] Spectrum analyser
   - *A multimeter measures resistance, voltage and current. Near-zero ohms means continuity, and an infinite reading, shown as OL (open loop), means a break. It is basic, but useful for checking a single conductor.*
   - @5.5.hw ~26.15
8. A tech has bulk Cat 6 and a bag of RJ45 connectors and needs to make a custom-length patch lead. Which tool presses the connector onto the cable?
   - [ ] Punchdown tool  - **[x] Crimper**  - [ ] Toner probe  - [ ] Cable stripper only
   - *A crimper squeezes the RJ45 contacts onto the conductors. A punchdown tool seats wires into 110 or Krone blocks, keystone jacks and patch panels.*
   - @5.5.hw ~27.5
9. You are terminating a new horizontal run on the rear 110 block of a rack panel. Which hand tool seats each conductor?
   - [ ] Crimper  - **[x] Punchdown tool**  - [ ] OTDR  - [ ] Loopback plug
   - *A punchdown tool pushes each wire into the insulation-displacement contact and trims the excess. Use the correct blade, 110 or Krone, for the block type.*
   - @5.5.hw ~27.6
10. Match each job to a tool. Type the letters in order, e.g. abcde. ¶  Find which unlabelled cable in the ceiling goes to room 12 · prove the pinout on a new run · give an IDS a copy of all traffic on a link without a switch · find the least busy 5 GHz channel · locate a crack in a fibre patch lead ¶  A Wi-Fi analyser · B visual fault locator · C toner and probe · D TAP · E cable tester · F OTDR
    - [=] cedab | c e d a b | c,e,d,a,b
    - *Find = toner. Verify = cable tester. Passive copy = TAP. RF survey = Wi-Fi analyser. Fibre break you can see = visual fault locator.*
    - @5.5.hw
11. True or false: running show interface on a Cisco switch prints its entire configuration, including routing, VLANs and every setting.
    - [ ] True  - **[x] False**
    - *show interface reports per-interface status, speed, duplex, counters and errors. The whole configuration comes from show running-config.*
    - @5.5.dev ~23.24
12. `show config` gives interface status and error counters. True?
    - [ ] True  - **[x] False**
    - *Answer: False. show running-config / show config = the configuration text. Status and counters = show interface(s). Hook: config = what it SHOULD do, interface = what it IS doing.*
    - @5.5.dev ~23.25
13. Type the Cisco command that shows the router's IP-to-MAC mappings.
    - [=] show arp | show ip arp
    - *show arp = IP, MAC, age and interface. Age "-" = the router's own address. Then find the physical port with show mac address-table.*
    - @5.5.dev ~23.26
14. True or false: on a Cisco switch, show vlan lists each VLAN's number and name together with the access ports assigned to it.
    - **[x] True**  - [ ] False
    - *show vlan, or show vlan brief, lists VLAN IDs, names, status and access ports. Trunk ports are not listed there; use show interfaces trunk for those.*
    - @5.5.dev ~23.27
15. Type the Cisco command that shows one-line status, VLAN, duplex and speed for every port.
    - [=] show interfaces status | show interface status | sh int status
    - *show interfaces status = the quickest overview: connected / notconnect / err-disabled, VLAN, a-full / a-1000. Then use show interface Gi0/5 for the counters.*
    - @5.5.dev
16. On a Cisco switch, type the command that displays the learned MAC-to-port table so you can find which port 00a0.c9b2.1f3e lives on.
    - [=] show mac address-table | show mac-address-table | show mac address-table address 00a0.c9b2.1f3e
    - *The MAC address table maps each MAC address to a VLAN and port. Add address followed by the MAC to filter for one entry.*
    - @5.5.dev ~30.20,23.23
17. On a Cisco switch, type the command that shows each port's speed, duplex and error counters such as CRC and runts.
    - [=] show interface | show interfaces | show int
    - *show interfaces gives up and down status, speed and duplex, plus counters for CRC, runts, giants, collisions and input errors.*
    - @5.5.dev ~30.21
18. On a Cisco switch, type a command that lists the VLANs and which access ports belong to each.
    - [=] show vlan | show vlan brief
    - *show vlan brief gives the compact view of VLAN IDs, names and member ports.*
    - @5.5.dev ~30.22
19. On a Cisco router, type the command that shows which networks it knows and the next hop for each.
    - [=] show ip route | show route | sh ip ro
    - *The objectives list show route. On IOS the command is show ip route, which also shows the gateway of last resort.*
    - @5.5.dev ~30.23
20. On a Cisco device, type the command that displays the configuration currently in effect in RAM.
    - [=] show running-config | show run
    - *show running-config prints the active config. show startup-config shows the version saved in NVRAM that loads at boot.*
    - @5.5.dev ~30.24
21. New APs on a Cisco switch will not boot. Type the command that shows the PoE watts each port draws and how much of the budget is left.
    - [=] show power inline | show power
    - *Compare used and available watts. When a phone or AP will not power up, check the budget first.*
    - @5.5.dev ~30.25
22. The switch learned printer 0011.2233.aabb dynamically on Gi0/15 in VLAN 20, and a second address 00e0.4c68.0101 on uplink Gi0/48. Type the port where the printer is cabled.
    - [=] Gi0/15 | GigabitEthernet0/15 | gi0/15 | g0/15
    - *Each MAC table row ties a MAC address to a VLAN and port, so the printer is on Gi0/15 in VLAN 20. A port that shows many MACs is usually an uplink or AP, not the end device.*
    - @5.5.dev ~29.9
23. A router's ARP table reads: ¶Protocol  Address       Age  Hardware Addr   Type  Interface ¶Internet  172.16.0.1      -  00e0.4c68.0001  ARPA  Gi0/0 ¶Internet  172.16.0.44     7  00e0.4c68.0044  ARPA  Gi0/0 ¶Internet  172.31.2.8     15  0011.2233.aabb  ARPA  Gi0/2 ¶Type the interface used to reach 172.31.2.8.
    - [=] Gi0/2 | GigabitEthernet0/2 | g0/2 | gi0/2
    - *show arp maps IP to MAC to interface. An Age of a dash marks the router's own address. To find the physical switch port, look the MAC up in the switch's MAC address table.*
    - @5.5.dev ~29.22
24. A user at 10.1.20.57 reports no network. On the switch: ¶  SW1# show arp ¶  Protocol  Address      Age  Hardware Addr   Type  Interface ¶  Internet  10.1.20.1    -    0011.2233.4401  ARPA  Vlan20 ¶  Internet  10.1.20.57   3    00a0.c9b2.1f3e  ARPA  Vlan20 ¶ ¶  SW1# show mac address-table ¶  Vlan  Mac Address     Type     Ports ¶  20    00a0.c9b2.1f3e  DYNAMIC  Gi0/14 ¶  20    0050.56aa.0001  DYNAMIC  Gi0/24 ¶Which physical port is the user's PC plugged into?
    - [ ] Gi0/24  - **[x] Gi0/14**  - [ ] Vlan20  - [ ] It can't be told from this output
    - *Answer: Gi0/14. Two-step trace: show arp maps the IP to its MAC (10.1.20.57 → 00a0.c9b2.1f3e). show mac address-table maps that MAC to a port (Gi0/14). Vlan20 is the SVI, a logical interface, not a socket in the wall. Gi0/24, with lots of MACs behind it, is usually the uplink. Hook: ARP gives the MAC, the MAC table gives the port.*
    - @5.5.cmd

### Key facts
- **Toner and probe = find a cable · cable tester = verify the wiring · certifier = prove the category · TAP = passive copy · Wi-Fi analyser = RSSI, channels, noise · VFL = red light, fibre breaks · OTDR = distance to a fibre fault · multimeter = continuity/voltage · crimper = RJ45 plug · punchdown = patch panel.**
- **show mac address-table (MAC → port) · show ip route / show route · show interface(s) (counters) · show interfaces status (one line per port) · show running-config · show arp · show vlan brief · show power inline · show cdp/lldp neighbors.**

## Test 34 - 5.5 Tools Drill (24 Q)

1. Type an nmap command that sweeps 10.0.0.0/24 to see which hosts are up, skipping any port scan.
   - [=] nmap -sn 10.0.0.0/24
   - *-sn does host discovery only, a ping sweep. Think s n as scan, no ports.*
   - @5.5.sw ~32.1
2. Type an nmap command that probes 10.0.0.5 and reports the software and version behind each open port.
   - [=] nmap -sV 10.0.0.5
   - *-sV performs version detection, reporting things like OpenSSH 8.9. V is for version.*
   - @5.5.sw ~32.2
3. An auditor needs a list of every live host on 10.8.0.0/22 before a port scan. Which nmap option does ONLY host discovery?
   - **[x] -sn**  - [ ] -sV  - [ ] -p-  - [ ] -A
   - *-sn = ping sweep, no port scan, just which hosts answer. -sV = service versions on open ports. -p- = all 65535 ports. -A = aggressive: OS, versions, scripts and traceroute. Know -sn, -p and -sV for the exam.*
   - @5.5.sw ~32.3
4. A scan shows: ¶  $ nmap 10.0.0.20 ¶PORT     STATE    SERVICE ¶22/tcp   open     ssh ¶23/tcp   open     telnet ¶80/tcp   filtered http ¶What should the technician do about this switch FIRST?
   - **[x] Disable Telnet and use SSH only**  - [ ] Open port 80 on the firewall  - [ ] Change the SSH port to 2222  - [ ] Nothing, the scan is clean
   - *Telnet (23) sends credentials in clear text, so it's the finding: transport input ssh on the VTY lines. filtered = a firewall dropped the probe, no answer either way. Moving SSH to another port is obscurity, not security.*
   - @5.5.sw ~32.4
5. nmap reports a port as "filtered". What does that mean?
   - **[x] A firewall dropped the probe, so nmap can't tell**  - [ ] The port is open and a service answered  - [ ] The host replied with a TCP RST  - [ ] The host is powered off or unreachable
   - *open = a service answered (SYN-ACK). closed = the host replied RST, reachable but nothing listening. filtered = no reply or an ICMP unreachable, so a firewall is in the way.*
   - @5.5.sw ~32.5
6. Type the nmap command that scans only ports 22, 80 and 443 on 10.0.0.9.
   - [=] nmap -p 22,80,443 10.0.0.9 | nmap 10.0.0.9 -p 22,80,443 | nmap -p22,80,443 10.0.0.9
   - *-p takes a list or range: -p 22,80,443 or -p 1-1024. Without -p, nmap scans the 1,000 most common ports.*
   - @5.5.sw ~32.7
7. A technician wants to know which program owns a port and what version it runs on a remote server, without logging in. Best tool?
   - **[x] nmap -sV**  - [ ] netstat -ano  - [ ] arp -a  - [ ] ipconfig /all
   - *nmap -sV probes open ports and reports the service and version, e.g. OpenSSH 8.9. netstat shows connections on the LOCAL machine only. arp = IP to MAC. ipconfig = the local interface settings.*
   - @5.5.sw ~32.8
8. Why should a technician get written permission before running nmap against a network?
   - **[x] Unauthorised scanning can breach policy or law, and it can trip IDS alarms**  - [ ] nmap needs a licence key from the network owner  - [ ] nmap only works with admin credentials for the target  - [ ] Scanning deletes firewall logs
   - *Port scanning is reconnaissance, the first step of an attack. Scan only with written approval and an agreed scope, and warn the SOC (Security Operations Centre) so the alerts aren't treated as an incident.*
   - @5.5.sw ~32.9
9. You need a report like this for 10.0.0.5: ¶PORT     STATE SERVICE VERSION ¶443/tcp  open  https   nginx 1.24.0 ¶3306/tcp open  mysql   MySQL 8.0.36 ¶Type an nmap command that would include the VERSION column.
   - [=] nmap -sV 10.0.0.5 | nmap -A 10.0.0.5 | sudo nmap -sV 10.0.0.5 | sudo nmap -A 10.0.0.5
   - *The VERSION column only appears with -sV, or with -A, which bundles version detection with OS detection and scripts.*
   - @5.5.sw ~29.26
10. Type a dig command that returns only the address for example.com, with no extra sections.
    - [=] dig example.com +short | dig +short example.com
    - *+short prints only the answer. Without it dig shows the question, answer and authority sections plus TTLs.*
    - @5.5.cli ~32.14
11. Using dig, type the query that lists which mail exchangers handle example.com.
    - [=] dig example.com MX | dig MX example.com | dig example.com mx
    - *Put the record type after the name, for example A, AAAA, MX, NS, TXT, CNAME or SOA.*
    - @5.5.cli ~32.15
12. A firewall log shows 8.8.8.8. Type the dig command that asks which hostname belongs to that address.
    - [=] dig -x 8.8.8.8
    - *-x builds a PTR query under in-addr.arpa. Do not confuse it with @8.8.8.8, which only chooses the server to ask.*
    - @5.5.cli ~32.16
13. Without entering interactive mode, ask nslookup for the mail exchanger records of example.com. Type the command.
    - [=] nslookup -type=mx example.com | nslookup -query=mx example.com | nslookup -q=mx example.com
    - *-type accepts mx, ns, txt and more. In interactive mode the equivalent is set type=mx.*
    - @5.5.cli ~32.17
14. On a Windows PC, type a netstat command that lists all sockets numerically and adds the PID that owns each one.
    - [=] netstat -ano | netstat -a -n -o | netstat -nao | netstat -aon
    - *-o appends the PID, which you can match in Task Manager or with tasklist. -b shows the executable name but needs an elevated prompt.*
    - @5.5.cli ~32.18
15. Linux: listening TCP and UDP ports with the owning program, using the tool that replaced netstat.
    - [=] ss -tulpn | ss -tunlp | ss -lntup | sudo ss -tulpn
    - *ss -tulpn: t=TCP u=UDP l=listening p=process n=numeric. It replaces netstat on Linux.*
    - @5.5.cli ~32.19
16. Windows: to check whether a full 1500-byte packet survives the path to 10.0.0.1, send it a ping carrying a 1472-byte payload that routers may not fragment.
    - [=] ping -f -l 1472 10.0.0.1 | ping 10.0.0.1 -f -l 1472
    - *-f sets Don't Fragment and -l sets payload length. 1500 MTU minus 20 bytes of IP header and 8 bytes of ICMP header leaves 1472. If the ping fails with a 'needs to be fragmented' error, the path MTU is lower. Linux equivalent: ping -M do -s 1472.*
    - @5.5.cli ~32.20
17. On Windows, type a trace to example.com that skips reverse DNS for each hop so it finishes faster.
    - [=] tracert -d example.com
    - *-d disables name lookups for each hop, which speeds up the trace a lot. On Linux, traceroute -n does the same.*
    - @5.5.cli ~32.21
18. Windows: after swapping the default gateway hardware, flush every learned IP-to-MAC mapping on this PC.
    - [=] arp -d * | arp -d
    - *arp -d * deletes every ARP cache entry. It needs an admin prompt. Clearing the cache forces fresh IP-to-MAC lookups, which helps after replacing a gateway or NIC. arp -a shows the cache, and arp -s adds a static entry. On Linux, use ip neigh flush all.*
    - @5.5.cli ~32.22
19. A Linux interface eth0 shows state DOWN. Type the iproute2 command that enables it.
    - [=] ip link set eth0 up | ip link set dev eth0 up | sudo ip link set eth0 up
    - *ip link set dev name up or down toggles an interface. The legacy form is ifconfig eth0 up.*
    - @5.5.cli ~32.23
20. Type the iproute2 command that assigns 10.0.0.5 with a 24-bit mask to eth0 on a Linux host.
    - [=] ip addr add 10.0.0.5/24 dev eth0 | ip a add 10.0.0.5/24 dev eth0 | sudo ip addr add 10.0.0.5/24 dev eth0
    - *This change is lost at reboot. Persistent settings belong in netplan or NetworkManager.*
    - @5.5.cli ~32.24
21. A user pastes this from their PC: ¶   Host Name . . . . . . . : LAB-07 ¶   Physical Address. . . . : 7C-1E-52-0B-44-D9 ¶   DHCP Enabled. . . . . . : Yes ¶   DNS Servers . . . . . . : 172.16.0.10 ¶Type the command that produced it.
    - [=] ipconfig /all
    - *Fields like Host Name, Physical Address, DHCP Enabled and DNS Servers only appear with /all. Plain ipconfig lists just address, mask and gateway.*
    - @5.5.cli ~29.16
22. A trace to a public resolver ends: ¶  1    <1 ms  <1 ms  <1 ms  10.10.0.1 ¶  2     6 ms   7 ms   6 ms  100.72.0.1 ¶  3     9 ms   9 ms  10 ms  203.0.113.9 ¶  4    13 ms  12 ms  14 ms  one.one.one.one 1.1.1.1 ¶Trace complete. ¶Type the number of hops to the destination.
    - [=] 4
    - *Four hops with low, steady times is healthy. An address in 100.64.0.0/10 at hop 2 is carrier-grade NAT space used by the ISP. Latency rising gradually with distance is normal.*
    - @5.5.cli ~29.23
23. On a compromised laptop, netstat -ano shows: ¶TCP 0.0.0.0:445 0.0.0.0:0 LISTENING 4 ¶TCP 10.0.0.8:51877 203.0.113.66:4444 ESTABLISHED 7312 ¶Type the PID of the suspicious outbound connection.
    - [=] 7312
    - *With -o, the last column is the PID. Outbound to port 4444 is a common reverse-shell sign. Look it up with tasklist /fi "pid eq 7312", then end it with taskkill /pid 7312 /f.*
    - @5.5.cli ~29.25
24. PBQ: Type the exact command for each job.
    - [p] Windows: show the ARP cache = arp -a
    - [p] Windows: clear the DNS resolver cache = ipconfig /flushdns
    - [p] Linux: show listening TCP and UDP ports with their programs = ss -tulpn | ss -tunlp | sudo ss -tulpn | netstat -tulpn | sudo netstat -tulpn
    - [p] Linux: query DNS for the MX records of example.com = dig example.com mx | dig mx example.com | dig example.com MX | dig -t mx example.com | dig example.com -t mx | nslookup -type=mx example.com
    - [p] Cisco: show a one-line status summary of every interface = show ip interface brief | show ip int brief | sh ip int br
    - *arp -a · ipconfig /flushdns · tracert (Windows) vs traceroute (Linux) · ss -tulpn, with netstat -tulpn still accepted · dig name TYPE · ipconfig /release, then /renew · show ip interface brief = interface, IP, status and protocol at a glance.*
    - @5.5.cli

### Key facts
- **nmap: -sn = host sweep only · -p = port list · -sV = service versions. open = answered · closed = RST · filtered = firewall. Get written permission first.**
- **dig +short · dig name MX · dig -x IP · nslookup -type=mx name.**
- **netstat -ano (PID) · ss -tulpn (Linux listeners + program) · ping -f -l 1472 = MTU test (1472 + 28 header bytes = 1500) · tracert -d · arp -d * · ip link set eth0 up · ip addr add 10.0.0.5/24 dev eth0.**
