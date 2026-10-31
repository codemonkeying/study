TECH+ FC0-U71 QUICK REF  (study ref techplus · /ref in a quiz)
EXAM  70 Q max · 60 min · pass 650/900 · multiple choice only (no PBQs)
      D1 IT concepts 13% · D2 Infrastructure 24% · D3 Apps/software 18%
      D4 Software dev 13% · D5 Data/databases 13% · D6 Security 19%
      practice exam: study techplus practice_exam  (menu 'p')

NUMBERS  binary = base 2 (0 1) · decimal = base 10 · hex = base 16 (0-9 A-F, F = 15)
  bit row 128 64 32 16 8 4 2 1 · 101 = 5 · 1000 = 8 · 1111 = 15 · 0x10 = 16
UNITS  8 bits = 1 byte · KB < MB < GB < TB < PB (x1000 each)
  storage = bytes (B) · speed = bits per second (Kbps Mbps Gbps) · CPU speed = GHz
  small letter b = bits, big B = bytes · 100 Mbps is about 12.5 MB per second

TROUBLESHOOTING  (in order)
  1 identify the problem  2 theory of probable cause  3 test the theory
  4 plan of action + implement  5 verify + preventive measures  6 document

HARDWARE
  CPU = brain · RAM = desk (fast, volatile, lost at power off) · SSD/HDD = filing cabinet
  volatile = RAM, CPU cache · non-volatile = SSD, HDD, ROM, flash, SD card
  SSD = no moving parts, fast · HDD = spinning disk, cheap per GB · NAS = storage on the network
  local = on the device · network = NAS/file share · cloud = someone else's servers online
PLUGS  USB-C = reversible, modern · Lightning = older iPhones · Thunderbolt = fast, USB-C shape
  video: VGA old analog · DVI · HDMI video + sound (TVs) · DisplayPort (monitors)
  RJ45 = Ethernet network plug · RJ11 = phone plug (smaller)
DEVICES  workstation · server · mobile (phone, tablet) · IoT = smart home gear · wearable = watch
NETWORK  LAN = one building · WAN = cities apart · client/server = central box · P2P = equals
  router joins networks · switch joins devices on a LAN · modem = to the ISP · AP = Wi-Fi
  Wi-Fi 2.4 GHz = further, slower · 5 GHz = faster, shorter · 6 GHz = Wi-Fi 6E, fastest
  wired = faster + steadier · wireless = convenient · cellular = mobile data · satellite = remote
CLOUD  SaaS = finished app (Gmail) · PaaS = platform for devs · IaaS = rented raw servers
  public · private · hybrid = own + cloud · VM = computer inside a computer, run by hypervisor

SOFTWARE
  OS = manages hardware (Windows, macOS, Linux, Android, iOS) · driver = lets OS talk to device
  app types: productivity (Word, Excel) · collaboration (Teams, email) · browser · business
  process = running program · service = background, no window · Task Manager = what's running
  install: check requirements · licence · updates/patches fix bugs + security holes
  AI = computer doing human-like tasks · generative AI makes new text/images · check its output

SOFTWARE DEV
  compiled (C, C++) = translated first, runs fast · interpreted (Python, JS) = line by line
  markup (HTML) = page structure, not a program · query (SQL) = ask a database
  types: char = one character · string = text · integer = whole number · float = decimals
         Boolean = true/false (2 values) · "25" in quotes = text, not a number
  variable = labelled box that can change · constant = never changes · array = list of values
  function = reusable named block · object = data + actions together
  if/else = decision · loop (for/while) = repeat · flowchart: oval start/end, diamond decision
  pseudocode = plain-English steps before real code

DATA
  structured = rows + columns (spreadsheet, table) · semi = tagged (email, JSON)
  non-structured = audio, video, free text
  flat file = one table (CSV, spreadsheet) · relational = linked tables (row = record, column = field)
  primary key = unique row ID · foreign key = links to another table's primary key
  NoSQL = flexible: document (JSON) · key-value · graph
  database vs flat file: many users at once, bigger, safer, less duplicate data
BACKUPS  full = everything · incremental = changed since last backup · 3-2-1 rule
  3 copies · 2 media types · 1 offsite (cloud) · test your restores

SECURITY
  CIA  confidentiality = only right people see it · integrity = not changed · availability = there when needed
  AAA  authentication = who you are · authorisation = what you may do · accounting = log what you did
  MFA = two+ different kinds: know (password) · have (phone, token) · are (fingerprint)
  passwords: long beats complex · unique per site · password manager · no reuse
  reset process = a back door; keep recovery details hard to guess
  phishing = fake email/text asking for info · check sender + links · report it
  malware: virus · ransomware (locks files, wants money) · spyware · keylogger
  encryption at rest = stored data (BitLocker, FileVault) · in transit = moving (HTTPS padlock, VPN)
  Wi-Fi: WPA3 best · WPA2 ok · change default router password · keep firmware updated
  licences: open source = code shared · proprietary = closed · subscription vs one-off · EULA
  privacy: only share what's needed · check app permissions · public Wi-Fi = use VPN
