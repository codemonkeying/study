<!-- passmark: 83 -->
## Test 1 - 1.1 + 1.2 Security Controls, CIA, AAA, Zero Trust (20 Q)

1. An auditor flags that a clinic's on-call procedure says "the IT lead reviews the VPN log each Monday," but nobody has done it in four months. Which control CATEGORY has failed?
   - **[x] Operational**  - [ ] Managerial  - [ ] Technical  - [ ] Physical
   - *Operational = a control carried out by people as a routine. The procedure exists (that part is managerial) but the human activity stopped. Hook: paper decides, people do, systems enforce, things block. Managerial is tempting because a procedure document is mentioned, but the failure is in the doing. Technical would be the VPN logging itself, which still works.*
   - @1.1.cat
2. A CISO has budget for ONE item and wants a MANAGERIAL control that will shape all later spending. Which should she pick?
   - **[x] A risk assessment that ranks the top threats to the business**  - [ ] A night guard rota for the head office lobby  - [ ] A next-generation firewall for the branch offices  - [ ] Badge readers on every internal office door
   - *Managerial controls are planning and oversight: risk assessments, policies, security plans. They steer which other controls get bought. Analogy: the architect's drawing before the builders arrive. Guard rota = operational; firewall = technical; badge readers = physical.*
   - @1.1.cat
3. A warehouse wants to reduce forklift-battery theft from its loading yard. Which option is a PHYSICAL control rather than an operational one?
   - **[x] A locked steel cage around the charging station**  - [ ] A supervisor counting batteries at every shift change  - [ ] Staff training on spotting unfamiliar visitors  - [ ] A guard walking the yard perimeter each hour
   - *Physical = a tangible object that protects a place or asset. The cage keeps working with nobody present. Counting, training and patrolling are all people doing things, so operational. Hook: if it works while everyone is asleep and you can touch it, it is physical. Trap: guards are operational even though they stand in a physical place.*
   - @1.1.cat
4. A payment terminal cannot be patched until the vendor ships firmware next quarter. Meanwhile, the team adds a daily manual review of its transaction logs. What is the BEST description of this review's control type?
   - **[x] Compensating**  - [ ] Detective  - [ ] Corrective  - [ ] Preventive
   - *Compensating = a substitute measure used because the primary control (the patch) is not possible yet. A log review is detective by nature, which is why Detective tempts, but the scenario's key fact is "stands in for the missing patch". Corrective would fix damage after an incident; nothing here stops an attack, so not preventive. Hook: "can't do X, so we do Y meanwhile" = compensating.*
   - @1.1.type
5. A retailer's loss-prevention team wants to cut shoplifting attempts without adding staff or physically blocking customers. Which control type should they focus on?
   - **[x] Deterrent**  - [ ] Preventive  - [ ] Directive  - [ ] Corrective
   - *Deterrent controls discourage the attempt: visible dome cameras, "CCTV in operation" signs, security tags on display. They do not stop a determined thief. Preventive would physically block (locked cabinets), which the brief rules out. Directive tells people what to do, aimed at staff rather than thieves. Corrective acts after the loss. Analogy: a "Beware of the dog" sign.*
   - @1.1.type
6. An IPS drops a packet matching a known exploit, then a SOC analyst reimages the workstation that sent it. Which control types are shown, in order?
   - **[x] Preventive, then corrective**  - [ ] Detective, then compensating  - [ ] Preventive, then compensating  - [ ] Detective, then corrective
   - *An IPS sits inline and blocks, so preventive (an IDS would only detect). Reimaging restores a clean state after the event, so corrective. Hook: IPS Prevents, IDS Detects; corrective = the plaster after the cut. Compensating would be a stand-in for a control you cannot deploy, which is not the case here.*
   - @1.1.type
7. PBQ 1.1 - Controls matrix. A logistics firm lists new controls. Pick the CATEGORY, then the TYPE that best fits each control's main purpose. ¶  1  Data-loss prevention rule blocking card numbers in outbound email ¶  2  Policy requiring visitors to be escorted at all times ¶  3  Guard checks the CCTV monitors and radios in anything odd ¶  4  Locked gate on the fuel depot ¶  5  Restoring the dispatch database from snapshot after corruption
   - [p] Control 1 category :: A Technical · B Managerial · C Operational · D Physical = a
   - [p] Control 1 type :: A Preventive · B Deterrent · C Detective · D Corrective · E Compensating · F Directive = a
   - [p] Control 2 category :: A Technical · B Managerial · C Operational · D Physical = b
   - [p] Control 2 type :: A Preventive · B Deterrent · C Detective · D Corrective · E Compensating · F Directive = f
   - [p] Control 3 category :: A Technical · B Managerial · C Operational · D Physical = c
   - [p] Control 3 type :: A Preventive · B Deterrent · C Detective · D Corrective · E Compensating · F Directive = c
   - [p] Control 4 category :: A Technical · B Managerial · C Operational · D Physical = d
   - [p] Control 4 type :: A Preventive · B Deterrent · C Detective · D Corrective · E Compensating · F Directive = a
   - [p] Control 5 type :: A Preventive · B Deterrent · C Detective · D Corrective · E Compensating · F Directive = d
   - *1: DLP is enforced by a system and stops the email, so technical/preventive. 2: a written rule is managerial and tells people what to do, so directive. 3: a person watching screens is operational and notices events, so detective. 4: a gate is physical and blocks entry, so preventive. 5: restoring after damage is corrective. Hook: paper = managerial, people = operational, systems = technical, touchable = physical.*
   - @1.1.type
8. A finance clerk's laptop is stolen from a car. The drive used full-disk encryption and the company keeps nightly cloud backups. Which statement is MOST accurate?
   - **[x] Confidentiality held because of FDE, and availability held because of backups**  - [ ] Integrity failed, because the thief now controls the data  - [ ] Confidentiality failed, because physical possession bypasses encryption  - [ ] Availability failed, because the device itself is gone
   - *FDE keeps the data unreadable (confidentiality); backups mean the clerk can keep working (availability). Integrity is about unauthorised change to data the business relies on, and the backup copy is untouched. Possession does not defeat strong encryption with a good key. Losing one device is not loss of availability when the data is backed up. Hook: C = who can read, I = has it changed, A = can I get it.*
   - @1.2.cia
9. A supplier disputes a purchase order, claiming your buyer never sent it. Which control would have BEST let you prove the buyer's origin of the message?
   - **[x] The buyer signing the order with her private key**  - [ ] Sending the order over a TLS-encrypted connection  - [ ] Attaching a SHA-256 hash of the order to the email  - [ ] Requiring the buyer to use MFA to log into email
   - *Non-repudiation comes from a digital signature: only the holder of the private key could have produced it, and it also proves integrity. TLS protects the channel, not who authored the message. A bare hash proves nothing about origin, since anyone can recompute one after editing. MFA proves who logged in, not that this specific message is unaltered and theirs. Analogy: a wax seal only you own.*
   - @1.2.cia
10. Ransomware encrypts a hospital's patient-records share. The servers stay online and the files are still there, but no clinician can open any of them until the data is restored. Which CIA element is MOST directly affected?
    - **[x] Availability**  - [ ] Integrity  - [ ] Confidentiality  - [ ] Non-repudiation
    - *Availability = authorised users can get to the data when they need it, and here nobody can. Confidentiality would need the data to be read or copied by someone unauthorised; the stem gives no sign of exfiltration (if it did, that would be a second impact, as in double extortion). Integrity tempts because files were changed, but the clinical harm the stem stresses is being locked out. Non-repudiation is about proving who did something, not CIA. Hook: can't get to it = A.*
    - @1.2.cia
11. A contractor logs into the VPN with password plus MFA but cannot reach the engineering file server. The help desk confirms her credentials are fine. Where should they look FIRST?
    - **[x] Her group membership and the server's access rules**  - [ ] The MFA app on her phone  - [ ] The RADIUS accounting logs for her session  - [ ] Her password expiry date
    - *She authenticated, so the failure is authorization: what an identity may access. Check groups/roles and ACLs. MFA and password are authentication, already passed. Accounting logs record what happened but do not grant access; they may confirm the deny, but the fix is in authorization. Hook: AuthN = who are you, AuthZ = what may you do, Accounting = what did you do.*
    - @1.2.aaa
12. A microservice calls an internal payments API thousands of times an hour, with no human present. What is the BEST way for the API to authenticate it?
    - **[x] A certificate issued to the service, checked with mutual TLS**  - [ ] A shared admin password stored in a wiki page  - [ ] The caller's source IP address on an allow list  - [ ] A one-time code sent to the developer's phone
    - *Authenticating systems uses machine identities: certificates, tokens or API keys. Mutual TLS proves both ends. A wiki password is shared and exposed. IP addresses can be spoofed or reused and identify a location, not a service. An SMS code needs a human. Analogy: a passport for a machine.*
    - @1.2.aaa
13. A company with 8,000 staff wants access to follow job function, so a new payroll hire automatically gets payroll folders and loses them when she moves teams. What is the company choosing?
    - **[x] A role-based authorization model**  - [ ] A stronger authentication factor  - [ ] More detailed accounting logs  - [ ] A gap analysis against ISO 27001
    - *Authorization models apply permissions at scale; role-based ties rights to job roles instead of individual users. Authentication factors prove identity but grant nothing. Accounting records use. A gap analysis finds missing controls, it does not assign access. Analogy: wristband colour decides which rooms you enter.*
    - @1.2.aaa
14. PBQ 1.2 - AAA. A university IT team is reviewing its access setup. Answer each part.
    - [p] Students prove identity with a password and a phone prompt :: A Authentication · B Authorization · C Accounting = a
    - [p] Lab printers present device certificates to join the wired network via 802.1X :: A Authenticating people · B Authenticating systems · C Accounting = b
    - [p] A report shows each user's login time and data used on Wi-Fi :: A Authentication · B Authorization · C Accounting = c
    - [p] A lecturer can edit grades for her own modules but only view others :: A Authentication · B Authorization · C Accounting = b
    - *1: proving identity is authentication. 2: device certificates authenticate systems, not people. 3: logging who did what and when is accounting. 4: deciding what an authenticated user may do is authorization. Hook: who are you, what may you do, what did you do.*
    - @1.2.aaa
15. A new regulation takes effect in six months. The compliance lead has a checklist of the controls it requires and wants to know which ones the company is still missing before planning any spend. What should she do FIRST?
    - **[x] Perform a gap analysis of current controls against the checklist**  - [ ] Commission a penetration test of the external network  - [ ] Buy cyber insurance to cover the compliance shortfall  - [ ] Run a tabletop exercise based on a breach scenario
    - *Gap analysis compares the current state with a required state (a regulation, framework or baseline) and lists what is missing; the result becomes a prioritised remediation plan. A pentest finds exploitable weaknesses, not missing paperwork or process controls. Insurance transfers risk but closes no gaps. A tabletop tests incident response. Analogy: comparing your packed suitcase with the packing list before the trip.*
    - @1.2.gap
16. A bank's zero trust system sees a teller sign in from a new laptop at 2 a.m. and demands a hardware-key prompt before allowing access. Which zero trust concept is shown?
    - **[x] Adaptive identity**  - [ ] Threat scope reduction  - [ ] Implicit trust zone  - [ ] Policy enforcement point
    - *Adaptive identity raises or lowers authentication strength based on context: device, location, time, behaviour. Threat scope reduction limits what a user can reach, not how hard login is. An implicit trust zone is the area past the enforcement point. The PEP enforces a decision but does not choose the extra factor. Analogy: your bank texting you when your card is used abroad.*
    - @1.2.zt
17. After a breach in which one stolen account reached 300 servers, an architect wants the NEXT stolen account to reach as little as possible. Which zero trust goal BEST fits?
    - **[x] Threat scope reduction**  - [ ] Adaptive identity  - [ ] Policy administrator  - [ ] Non-repudiation
    - *Threat scope reduction shrinks the blast radius through least privilege and microsegmentation. Adaptive identity makes stealing the account harder but does not limit reach once it is used. The policy administrator relays decisions; it is a component, not a goal. Non-repudiation proves who acted. Analogy: watertight compartments on a ship.*
    - @1.2.zt
18. A zero trust team writes rules such as "finance app: managed device + finance role + compliant patch level" and lets the system apply them to every request. Which control plane concept is this?
    - **[x] Policy-driven access control**  - [ ] Implicit trust zone  - [ ] Subject/system  - [ ] Threat scope reduction
    - *Policy-driven access control means access decisions come from defined policies evaluated per request, not from network location. Implicit trust zone and subject/system are data plane items. Threat scope reduction is the outcome of tight policies, not the mechanism. Hook: the rulebook the policy engine reads.*
    - @1.2.zt
19. PBQ 1.3 - Zero trust request flow. ¶  Engineer's laptop ---> Access proxy ---> Build server ¶  Component X weighs identity, device posture and threat intel, then says allow or deny ¶  Component Y takes that verdict, issues the session credentials and tells the proxy ¶  Once past the proxy, the build server's subnet is treated as trusted. Name each piece.
    - [p] Component X :: A Policy engine · B Policy administrator · C Policy enforcement point · D Subject · E Implicit trust zone = a
    - [p] Component Y :: A Policy engine · B Policy administrator · C Policy enforcement point · D Subject · E Implicit trust zone = b
    - [p] The access proxy :: A Policy engine · B Policy administrator · C Policy enforcement point · D Subject · E Implicit trust zone = c
    - [p] The engineer on the laptop :: A Policy engine · B Policy administrator · C Policy enforcement point · D Subject · E Implicit trust zone = d
    - [p] The build server's subnet :: A Policy engine · B Policy administrator · C Policy enforcement point · D Subject · E Implicit trust zone = e
    - [p] Plane holding X and Y :: A Control plane · B Data plane = a
    - *X decides = policy engine. Y executes the decision and sets up or tears down the session = policy administrator. The proxy sits in the traffic path and opens or closes the connection = PEP. The requester = subject. The trusted area behind the PEP = implicit trust zone, which zero trust keeps as small as possible. Engine + administrator = control plane; subject, PEP and trust zone = data plane. Analogy: judge, clerk, bailiff at the door.*
    - @1.2.zt
20. After a fraudulent change to supplier bank details, the audit log shows it was made by "finance_team", a login used by six clerks. Which security property can the company NOT achieve for this action?
    - **[x] Non-repudiation**  - [ ] Availability  - [ ] Confidentiality  - [ ] Authorization
    - *Non-repudiation means a specific person cannot credibly deny an action. A shared login ties the change to a group, not an individual, so any of the six can deny it. Give each clerk a named account (and digital signatures for high-value approvals). Availability and confidentiality are not in question, and the login was authorized to make the change. Hook: shared account = shared alibi.*
    - @1.2.cia

### Key facts
- **Categories: technical, managerial, operational, physical. Types: preventive, deterrent, detective, corrective, compensating, directive.**
- **CIA: confidentiality (encryption), integrity (hashing), availability (redundancy, backups). Non-repudiation = digital signature.**
- **AAA: authentication (people and systems), authorization (models such as role-based), accounting. Gap analysis (1.2) = current vs required state, output is a prioritised remediation plan.**
- **Zero trust control plane: adaptive identity, threat scope reduction, policy-driven access control, policy engine, policy administrator. Data plane: subject/system, PEP, implicit trust zones.**

## Test 2 - 1.2 + 1.3 Physical Security, Deception, Change Management (17 Q)

1. A records office wants after-hours motion detection across a large floor split up by plasterboard and fabric partitions, so one sensor cannot see every corner directly. Which sensor type is the BEST fit?
   - **[x] Microwave**  - [ ] Infrared  - [ ] Pressure  - [ ] Access badge
   - *Microwave sensors emit radio-frequency energy and detect changes in the reflected signal; they cover large areas and the signal can pass through thin non-metallic materials such as plasterboard (metal reflects it, which can also cause false alarms beyond the room). Passive infrared needs line of sight to a heat source. Pressure only fires where someone steps. A badge reader logs entry but detects nothing inside. Hook: infrared = heat, pressure = weight, microwave/ultrasonic = bounced waves.*
   - @1.2.phys
2. Strangers keep slipping into a distribution centre alongside delivery drivers. CCTV records them, but nobody stops them, and each case needs a judgement call (is this a new driver's mate or an intruder?). What should be added?
   - **[x] A security guard at the delivery entrance**  - [ ] More cameras with higher resolution  - [ ] Perimeter fencing around the car park  - [ ] Brighter lighting at the loading bay
   - *Guards bring human judgement and an on-the-spot response; cameras only record or alert. Fencing protects the perimeter, but these people come through a legitimate door. Lighting deters and helps cameras but cannot ask "who are you with?". Analogy: a smoke alarm vs a firefighter.*
   - @1.2.phys
3. A data centre has a 2.4 m fence with a single gate. Which statement about the fence is MOST accurate?
   - **[x] It deters casual intruders and channels people to the gate, but a determined attacker can still climb or cut it**  - [ ] It replaces the need for badge readers at the building door  - [ ] It detects intruders and raises an alert when touched  - [ ] It is a technical control because it is part of the site design
   - *Fencing is a physical control that deters and delays and creates a controlled entry point. It is not detection unless sensors are added, and it does not replace inner layers (defence in depth). Being part of a design does not make it technical; technical means enforced by systems.*
   - @1.2.phys
4. PBQ 1.4 - Physical security for a new branch. Pick the best control for each spot. ¶  Spot 1  Glass storefront next to a busy road ¶  Spot 2  Staff entrance where people hold the door for whoever is behind them ¶  Spot 3  Cash room where you must know exactly who entered and when ¶  Spot 4  Unstaffed back office that should alert on motion at night, mounted high on the ceiling ¶  Spot 5  Poorly lit rear alley used by staff at closing time
   - [p] Spot 1 :: A Bollards · B Access control vestibule · C Access badge · D Ultrasonic sensor · E Lighting · F Honeypot = a
   - [p] Spot 2 :: A Bollards · B Access control vestibule · C Access badge · D Ultrasonic sensor · E Lighting · F Honeypot = b
   - [p] Spot 3 :: A Bollards · B Access control vestibule · C Access badge · D Ultrasonic sensor · E Lighting · F Honeypot = c
   - [p] Spot 4 :: A Bollards · B Access control vestibule · C Access badge · D Ultrasonic sensor · E Lighting · F Honeypot = d
   - [p] Spot 5 :: A Bollards · B Access control vestibule · C Access badge · D Ultrasonic sensor · E Lighting · F Honeypot = e
   - [p] Spot 6, a recorded view of everyone at the cash room door for later review :: A Video surveillance · B Bollards · C Fencing · D Honeyfile = a
   - [p] Spot 7, a dark stockroom corridor that should alert on a warm body :: A Infrared sensor · B Pressure sensor · C Microwave sensor · D Ultrasonic sensor = a
   - [p] Spot 8, the floor directly in front of the safe, alert only when stepped on :: A Infrared sensor · B Pressure sensor · C Microwave sensor · D Ultrasonic sensor = b
   - *1: bollards stop vehicles while letting pedestrians pass. 2: a vestibule (two doors, one opens at a time) defeats tailgating; a badge reader alone does not. 3: a personal badge ties each entry to a named person and logs it. 4: an ultrasonic sensor bounces sound waves and detects motion in the room. 5: lighting deters and helps cameras. 6: video surveillance records for later review. 7: infrared detects heat. 8: pressure detects weight. A honeypot is a network decoy. Hook: posts for cars, airlock for tailgaters, badge for the log, sensor for the empty room, light for the alley, camera for the record.*
   - @1.2.phys
5. A SOC wants a high-confidence alert if an intruder dumps credentials from the domain and tries to use them. What should they plant?
   - **[x] A honeytoken: a fake admin account that no one ever uses**  - [ ] A honeynet of decoy servers in the DMZ  - [ ] A honeyfile named salaries.xlsx on a share  - [ ] Tokenization of the account database
   - *A honeytoken is fake data (credential, record, API key) whose any use proves compromise. A honeynet catches network exploration, not reuse of a dumped credential. A honeyfile alerts on opening a file. Tokenization replaces real data with substitutes for protection, not bait. Analogy: a map maker's fake street that catches copiers.*
   - @1.2.dcpt
6. A threat research team wants to watch how attackers move laterally between hosts after the initial break-in. Which deception tool is the BEST fit?
   - **[x] Honeynet**  - [ ] Honeypot  - [ ] Honeyfile  - [ ] Honeytoken
   - *Lateral movement needs several hosts to move between, so a network of decoys: honeynet. One honeypot shows the initial attack but nowhere to pivot. Honeyfiles and honeytokens are single bait items. Hook: one pot, many pots = a net.*
   - @1.2.dcpt
7. A manager proposes deploying a honeypot and dropping the planned firewall upgrade to save money. What is the BEST response?
   - **[x] Decline: decoys give high-confidence detection and intel, but they do not block attacks**  - [ ] Approve: attackers will spend their time on the honeypot instead  - [ ] Approve: a honeypot encrypts traffic to the real servers  - [ ] Decline: honeypots are illegal to run on corporate networks
   - *Deception tools add detection and attacker intelligence with few false positives, since no legitimate user should touch them. They are a layer, never a substitute for preventive controls. Attackers may skip the decoy entirely. Honeypots do no encryption, and running one on your own network is legal.*
   - @1.2.dcpt
8. PBQ 1.5 - Deception triage. Four alerts fire overnight. Name the decoy that raised each.
   - [p] Someone opened "VPN_passwords.docx" on the HR share :: A Honeypot · B Honeynet · C Honeyfile · D Honeytoken = c
   - [p] A fake AWS key planted in an old Git repo was used from 203.0.113.50 :: A Honeypot · B Honeynet · C Honeyfile · D Honeytoken = d
   - [p] An attacker scanned and logged into a lone fake SSH server at 198.51.100.20 :: A Honeypot · B Honeynet · C Honeyfile · D Honeytoken = a
   - [p] The same attacker hopped across six decoy hosts in a fake subnet :: A Honeypot · B Honeynet · C Honeyfile · D Honeytoken = b
   - *File = honeyfile. Fake credential/key = honeytoken. One fake system = honeypot. Many decoy systems = honeynet. Hook: pot = one, net = many, file = a document, token = a fake datum.*
   - @1.2.dcpt
9. A network team wants to push a firewall rule change on Friday afternoon. The change advisory board refuses to approve it until the team attaches results from the staging lab. Which change management element is the CAB enforcing?
   - **[x] Test results as an input to the approval process**  - [ ] A backout plan  - [ ] A maintenance window  - [ ] Ownership
   - *The approval process relies on evidence: impact analysis and test results show the change works and what it touches. A backout plan is how you undo it. A maintenance window is when you do it. Ownership is who is accountable. Hook: no evidence, no approval.*
   - @1.3.proc
10. Before a mail server migration, the change owner emails the sales director, the help desk lead and the compliance officer to explain what will happen and get their input. Who are these people in change management terms?
    - **[x] Stakeholders**  - [ ] Owners  - [ ] The CAB  - [ ] Approvers of the backout plan
    - *Stakeholders are people affected by or with an interest in the change, who should be informed and consulted. The owner is the one accountable person driving it. The CAB formally approves. Analogy: neighbours told about building work vs the builder who is responsible.*
    - @1.3.proc
11. Every month, junior admins patch the same web servers and occasionally skip the step of draining load-balancer traffic first. What would BEST reduce these errors?
    - **[x] A standard operating procedure for the patch process**  - [ ] A longer maintenance window  - [ ] A new impact analysis for each patch  - [ ] Adding the admins as stakeholders
    - *An SOP documents the exact repeatable steps so routine changes are done the same way every time. A longer window gives more time but not the missed step. Repeating impact analysis for an unchanged routine adds paperwork, not consistency. Stakeholders are consulted, not instructed. Analogy: a pilot's pre-flight checklist.*
    - @1.3.proc
12. PBQ 1.6 - Change post-mortem. Mid-morning on a Wednesday, the moment the CAB signed off, an engineer flashed new firmware onto the VPN concentrator. Remote staff were cut off for four hours while the team searched for a way back to the old firmware, and the review could not name anyone accountable. Answer each part.
    - [p] What would have shortened the four-hour outage :: A Stakeholder list · B Backout plan · C Allow list · D SOP for logging = b
    - [p] When the work should have been scheduled :: A Business hours so staff can report problems · B Right after approval · C A pre-agreed maintenance window · D Any time, firmware is low risk = c
    - [p] Pre-approval step that would have flagged the remote-access impact :: A Ownership · B Impact analysis · C Version control · D Service restart = b
    - [p] Gap shown by "nobody could say who was responsible" :: A Ownership · B Stakeholders · C Test results · D Dependencies = a
    - [p] The firmware reboots the concentrator. Technical implication the plan must cover :: A Legacy application · B Downtime and verifying the service restarts · C Deny list update · D Restricted activities = b
    - [p] The vendor notes the RADIUS plug-in application on the concentrator must be closed and relaunched to load new libraries. Technical implication :: A Application restart · B Legacy application · C Allow list · D Version control = a
    - [p] Correct order, first to last :: A Request, implement, approve, document · B Request, impact analysis and testing, approval, implement, document · C Implement, test, request, approve · D Request, approve, implement, impact analysis = b
    - *1: a backout plan lists exactly how to return to the previous state. 2: a maintenance window is a pre-agreed low-impact slot; mid-week business hours hurt users. 3: impact analysis identifies who and what is affected before approval. 4: ownership = one accountable person or team. 5: a reboot means downtime, and the service (and any security agents) must be checked after restart. 6: an application that must be relaunched is an application restart, which can drop sessions. 7: analysis and tests feed approval, then implementation, then documentation. Hook: no backout plan, no change.*
    - @1.3.proc
13. A team adds a new monitoring agent to all servers. The next morning, the agent is not running anywhere, and the endpoint protection logs show it was blocked. What was MOST likely missed in the change plan?
    - **[x] Adding the agent to the application allow list**  - [ ] Removing the agent from the deny list on the firewall  - [ ] Scheduling a service restart  - [ ] Updating the network diagram
    - *An allow list permits only approved software; anything new is blocked until added. Change plans must update allow/deny lists. A firewall deny list filters traffic, not local execution. A restart would not get past an allow list. Diagrams matter but did not cause the block. Analogy: a guest list at the door.*
    - @1.3.tech
14. A change to a 15-year-old inventory app is high risk because the vendor has gone, and no one is sure which reporting tools pull data from it. Which technical implications apply? (Select 2)
    - **[x] Legacy application**  - **[x] Dependencies**  - [ ] Restricted activities  - [ ] Deny list
    - *Legacy = old, unsupported, poorly documented, so behaviour after a change is unpredictable. Dependencies = other systems that rely on it and may break. Restricted activities are actions limited to the scope of the approved change; deny lists block named items. Neither is described. Analogy: pulling one brick from an old wall.*
    - @1.3.tech
15. During an approved change to patch a database, an admin notices an unrelated disk-space warning and decides to "quickly" resize a volume too. What should happen?
    - **[x] Stop: the resize is outside the approved scope and needs its own change request**  - [ ] Proceed: the maintenance window is already open  - [ ] Proceed if the admin restarts the database service afterward  - [ ] Proceed and record it later in version control
    - *Restricted activities: the change authorises specific work only; anything else needs its own approval, analysis and backout plan. An open window is not permission. A restart adds downtime but does not make the work approved. Recording it later does not replace approval. Hook: approved means THIS change, not any change.*
    - @1.3.tech
16. After a VLAN redesign goes live, the incident response playbook still shows the old subnets. Which TWO updates are MOST important? (Select 2)
    - **[x] Update the network diagrams**  - **[x] Update the IR policies and procedures that reference the subnets**  - [ ] Delete the old change ticket to avoid confusion  - [ ] Reset passwords on all switches
    - *Documentation must match reality: diagrams and the policies/procedures that depend on them. Stale docs mislead responders during an incident. Deleting tickets destroys the audit trail. Password resets are unrelated. Analogy: updating the map after a new road opens.*
    - @1.3.doc
17. A firewall config was edited by three admins this month, and one edit broke a partner connection. The team wants to see who changed what and roll back only that edit. What should they have in place?
    - **[x] Version control for the configuration files**  - [ ] A longer maintenance window  - [ ] An updated stakeholder list  - [ ] Daily full backups only
    - *Version control records each change with author and time and lets you revert a specific version. Full backups restore everything to a point in time but do not show who changed which line. Window and stakeholders do not track edits. Analogy: a shared document's page history.*
    - @1.3.doc

### Key facts
- **Physical: bollards, access control vestibule, fencing, video surveillance, guards, access badges, lighting, sensors (infrared = heat, pressure = weight, microwave and ultrasonic = reflected waves).**
- **Honeypot = decoy system; honeynet = decoy network; honeyfile = decoy file; honeytoken = decoy datum.**
- **Change management: approval, ownership, stakeholders, impact analysis, test results, backout plan, maintenance window, SOP. Technical: allow/deny lists, restricted activities, downtime, service/application restart, legacy apps, dependencies. Docs: diagrams, policies/procedures, version control.**

## Test 3 - 1.4 Cryptography I: PKI, Encryption, Tools, Obfuscation (20 Q)

1. A procurement officer must send a price sheet that only the partner's finance director can open. The director has published her certificate on the partner portal. What should the officer encrypt the file with?
   - **[x] The director's public key**  - [ ] The director's private key  - [ ] The officer's own private key  - [ ] The officer's own public key
   - *To keep something confidential for one person, encrypt with that person's public key; only her private key decrypts it. The officer's private key is used for signing, which proves origin but hides nothing (anyone with his public key could read it). Nobody but the director ever holds her private key. Hook: lock with THEIR public, they open with THEIR private. Analogy: a post box slot anyone can use, one key opens it.*
   - @1.4.pki
2. A developer accidentally pushes a folder to a public code repository. It contains web.crt, web.key, web.csr and the CA's chain bundle. Which file's exposure is MOST serious?
   - **[x] web.key**  - [ ] web.crt  - [ ] web.csr  - [ ] The CA chain bundle
   - *The .key file is the private key; with it an attacker can impersonate the server or decrypt traffic tied to it. Certificates, CSRs and chain bundles only contain public information and are handed out to every visitor anyway. Next steps: revoke the certificate and issue a new one with a fresh key pair. Hook: public parts are meant to be seen; the private key is the crown jewel.*
   - @1.4.pki
3. A law firm encrypts each partner's mailbox. Policy requires that, if a partner leaves or loses his key, the firm can still decrypt his mail for legal holds. What should it put in place?
   - **[x] Key escrow with a trusted custodian**  - [ ] Key stretching on each partner's password  - [ ] Shorter certificate lifetimes for all partners  - [ ] Tokenization of every mailbox item
   - *Key escrow keeps a copy of the decryption key with a trusted party, released only under defined conditions. Key stretching hardens passwords against guessing but stores nothing to recover. Shorter certificate lifetimes change renewal, not recovery. Tokenization swaps data for tokens and is aimed at structured data like card numbers. Analogy: a spare key lodged with a solicitor.*
   - @1.4.escrow
4. The security team agrees to key escrow but worries that a single rogue administrator at the custodian could pull out any key. Which control BEST addresses that concern?
   - **[x] Require two or more custodians to approve and jointly perform each key release**  - [ ] Store the escrowed keys in the same data centre as the encrypted data  - [ ] Increase every key from 2048 to 4096 bits  - [ ] Publish the escrow key list on the intranet for transparency
   - *Escrow's main risk is the extra copy of every key. Splitting control (dual control, split knowledge, M of N) means no single person can release a key alone. Co-locating keys with data makes one breach expose both. Longer keys do nothing if the key itself is stolen. Publishing the list helps attackers. Hook: two keys to open the vault.*
   - @1.4.escrow
5. Sales reps regularly leave laptops in taxis. Whoever picks one up must not be able to read anything from it, not even cached data or the swap file the OS wrote on its own. Which encryption level fits BEST?
   - **[x] Full-disk encryption**  - [ ] File-level encryption of the Documents folder  - [ ] Database encryption  - [ ] Transport encryption with TLS
   - *FDE (BitLocker, FileVault) encrypts the whole drive, so temp files, caches and swap are covered too. File-level encryption leaves copies the OS writes elsewhere. Database encryption protects a database, not the laptop. TLS protects data in transit, not a powered-off disk. Hook: lost device = FDE.*
   - @1.4.enclvl
6. An insurer stores millions of customer rows and wants a breach of any single encryption key to expose only one customer's data, not the whole table. Which approach fits BEST?
   - **[x] Record-level encryption with a separate key per customer**  - [ ] Database-level encryption with one master key  - [ ] Full-disk encryption on the database server  - [ ] Volume encryption on the storage array
   - *Record-level encryption protects individual rows, so per-record keys limit the damage of one stolen key. Database, disk and volume encryption all use one key for everything below them and mostly defend against stolen media, not a query through the running app. Hook: the finer the encryption level, the smaller the blast radius (and the more keys to manage).*
   - @1.4.enclvl
7. A media company must encrypt a 6 TB nightly backup before it leaves the building, within a two-hour window. Which choice is BEST for the bulk encryption?
   - **[x] AES-256, a symmetric cipher**  - [ ] RSA-4096 applied directly to the backup  - [ ] SHA-256 over the whole backup file  - [ ] Base64 encoding of the backup stream
   - *Symmetric ciphers like AES are fast and built for bulk data; asymmetric RSA is far slower and only practical for small items such as keys. SHA-256 is a hash: it proves integrity but cannot be decrypted. Base64 is encoding, readable by anyone. Hook: asymmetric moves the key, symmetric moves the data.*
   - @1.4.sym
8. A developer asks why a TLS session uses both asymmetric and symmetric cryptography instead of just one. What is the BEST answer?
   - **[x] Asymmetric methods safely agree a session key; the faster symmetric cipher then encrypts the traffic**  - [ ] Asymmetric encrypts the traffic; symmetric is only used to sign the certificate  - [ ] Symmetric is for the server, asymmetric is for the client  - [ ] Using both doubles the key length and so doubles the security
   - *Key exchange solves "how do two strangers share a secret over an open network"; once they have the session key, symmetric encryption carries the data efficiently. Certificates are signed asymmetrically, not symmetrically. Both sides use both methods. Key lengths do not add up like that. Analogy: send the safe's combination in a locked box, then use the safe.*
   - @1.4.kex
9. Two branch routers that have never shared a secret must create the same session key over the internet, and an eavesdropper recording every packet must not be able to work it out. Which method is designed for this?
   - **[x] Diffie-Hellman key exchange**  - [ ] Sending the key in a password-protected ZIP  - [ ] Hashing the key with SHA-256 before sending it  - [ ] Steganography to hide the key in an image
   - *Diffie-Hellman (and its elliptic curve form, ECDH) lets both sides compute the same secret from exchanged public values without ever transmitting the secret. A ZIP password still has to be shared somehow. A hash cannot be reversed into a usable key at the other end. Steganography hides data but is not a key-agreement protocol. Hook: DH = mix paint colours in public, only the two of you get the same final colour.*
   - @1.4.kex
10. An architect proposes moving signing keys from RSA-2048 to ECC for a fleet of low-power IoT sensors. What is the MAIN advantage of ECC here?
    - **[x] Comparable strength with much shorter keys, so less CPU, memory and bandwidth**  - [ ] ECC is a symmetric cipher, so it is faster than any asymmetric method  - [ ] ECC keys never need to be rotated  - [ ] ECC removes the need for certificates
    - *ECC gives similar security to RSA with far smaller keys (a 256-bit ECC key is roughly comparable to RSA-3072), which suits constrained devices. ECC is still asymmetric. All keys need lifecycle management and rotation. ECC public keys still travel in certificates. Hook: longer keys resist brute force but cost performance; ECC gets the strength cheaper.*
    - @1.4.keylen
11. An audit finds that an internal HR portal sends logins across the office LAN over plain HTTP. What is the BEST fix?
    - **[x] Enable HTTPS (TLS) on the portal and redirect HTTP to it**  - [ ] Encrypt the portal server's disk with FDE  - [ ] Hash passwords in the database with a salt  - [ ] Move the portal to a separate VLAN
    - *The data at risk is in transit, so it needs transport encryption. FDE protects data at rest when the disk is stolen. Salted hashing protects stored passwords, not the ones crossing the wire. A VLAN limits who can sniff but anyone on it still sees cleartext. Hook: match the encryption to where the data is: at rest, in transit, in use.*
    - @1.4.transport
12. A company wants each laptop to store its disk-encryption key in hardware on the motherboard and release it only if the boot files have not been tampered with. Which component provides this?
    - **[x] TPM**  - [ ] HSM  - [ ] Key management system  - [ ] Secure enclave in the CPU of a phone
    - *A TPM (trusted platform module) is a chip on the motherboard that stores keys and measures the boot process, which BitLocker uses to unlock the drive only on an unchanged system. An HSM is a separate, high-capacity device for servers and CAs. A KMS manages keys centrally, often in the cloud. A phone's secure enclave protects keys and biometrics on mobile devices. Hook: TPM = one machine, HSM = the data centre.*
    - @1.4.tool
13. A payment processor's private CA signs thousands of certificates a day. Auditors require the signing key to sit in tamper-resistant hardware that performs the crypto itself so the key never leaves it. What should it use?
    - **[x] An HSM**  - [ ] A TPM in the CA server  - [ ] An encrypted file on the CA server's disk  - [ ] A key escrow service
    - *An HSM (hardware security module) is dedicated, tamper-resistant hardware built for high-volume key storage and crypto operations, often clustered for availability. A TPM is per-device and not designed for CA throughput. A key file on disk can be copied. Escrow stores backup copies; it does not do signing. Analogy: a bank vault with its own clerk who signs documents without the seal ever leaving.*
    - @1.4.hsm
14. A phone app unlocks with a fingerprint. The vendor promises that even if malware gains full control of the phone's OS, it cannot read the fingerprint data or the keys it protects. What makes this possible?
    - **[x] A secure enclave isolated from the main operating system**  - [ ] Full-disk encryption on the phone's storage  - [ ] Tokenization of the fingerprint template  - [ ] A key management system in the vendor's cloud
    - *A secure enclave is a hardware-isolated processor area with its own protected memory; the main OS can ask it for a result but never reads the secret. FDE protects the phone at rest but the running OS sees decrypted data. Tokenization is for replacing data like card numbers in databases. A cloud KMS keeps keys off the device, which is the opposite of local biometric matching. Hook: enclave = a room inside the house the house owner cannot enter.*
    - @1.4.tool
15. An online shop wants card numbers out of its own database entirely to shrink its PCI DSS scope, while still allowing refunds against past orders. Which technique fits BEST?
    - **[x] Tokenization through the payment provider**  - [ ] Data masking on the order screen  - [ ] Steganography in the order records  - [ ] Hashing card numbers with SHA-256
    - *Tokenization replaces the card number with a random token; the real number lives only in the provider's vault, which can map the token back for a refund. Masking just hides digits on screen; the full number is still stored. Steganography hides data, it does not remove it. A hash of a 16-digit number can be brute forced and cannot be used for a refund. Analogy: a coat-check ticket instead of the coat.*
    - @1.4.obf
16. Call-centre agents need to confirm a caller's identity but should never see full national insurance numbers. Which BEST meets this?
    - **[x] Data masking that shows only the last few characters**  - [ ] Tokenization of the number in the CRM database  - [ ] Full-disk encryption on agent PCs  - [ ] Transport encryption between the CRM and the agent PCs
    - *Masking hides part of a value at display time (XX XX XX 12 C) while the system keeps the real data. Tokenization changes what is stored, which may break other processes that need the real number. FDE and TLS protect data at rest and in transit, but the agent would still see the full value on screen. Hook: masking = what you see, tokenization = what is stored.*
    - @1.4.obf
17. DLP shows nothing unusual, but an analyst notices a departing engineer has posted dozens of holiday photos to a personal blog, each a few MB bigger than similar photos from his phone. What should the analyst suspect?
    - **[x] Steganography used to hide data inside the images**  - [ ] Tokenization of the image metadata  - [ ] Data masking applied by the blog platform  - [ ] Key stretching of the image files
    - *Steganography hides data inside another file, such as an image or audio, so it slips past content filters; oversized images are a classic clue. Tokenization and masking protect data, they do not smuggle it. Key stretching is for passwords. Hook: stego = a secret message written in invisible ink on a postcard.*
    - @1.4.steg
18. PBQ 1.7 - Encryption choices. A hospital trust lists five data protection needs. Pick the BEST option for each.
    - [p] Stolen ward tablets must reveal nothing :: A Full-disk · B Record · C Transport · D Masking = a
    - [p] Each patient row in the research database protected separately :: A Full-disk · B Record · C Volume · D Transport = b
    - [p] Lab results sent from the lab system to the records system :: A File · B Database · C Transport (TLS) · D Steganography = c
    - [p] Algorithm for encrypting a nightly 2 TB imaging archive :: A RSA · B AES · C SHA-256 · D Diffie-Hellman = b
    - [p] Two sites agreeing a VPN session key over the internet :: A Diffie-Hellman · B AES · C Masking · D Escrow = a
    - [p] Only the data partition of a shared ward PC, leaving the OS partition clear :: A Partition · B Record · C Transport · D File = a
    - [p] One spreadsheet sent to auditors, encrypted on its own :: A File · B Volume · C Database · D Full-disk = a
    - [p] A logical volume on the storage array holding imaging data :: A Volume · B Record · C File · D Transport = a
    - [p] The whole patient database encrypted at rest by the database engine :: A Database · B Record · C Partition · D Masking = a
    - *1: FDE covers the whole device at rest. 2: record-level encryption limits each key's exposure to one row. 3: data moving between systems needs transport encryption. 4: bulk data = fast symmetric AES; RSA is for small items, SHA-256 is a hash. 5: key exchange creates the shared session key, then AES uses it. 6: partition encryption covers one partition only. 7: file encryption protects a single file wherever it goes. 8: volume encryption covers a logical volume. 9: database encryption protects the whole database at rest. Hook: where is the data, and how big is it?*
    - @1.4.enclvl
19. PBQ 1.8 - Crypto tools and obfuscation. Match each requirement at a bank to the BEST tool or technique.
    - [p] Root CA signing key in tamper-resistant hardware :: A TPM · B HSM · C Secure enclave · D Key management system = b
    - [p] Laptop disk key bound to the motherboard and boot state :: A TPM · B HSM · C Secure enclave · D Key management system = a
    - [p] One central service to create, rotate and audit keys for 300 cloud apps :: A TPM · B HSM · C Secure enclave · D Key management system = d
    - [p] Mobile banking app keeps biometric keys out of reach of the phone OS :: A TPM · B HSM · C Secure enclave · D Key management system = c
    - [p] Test environment needs realistic customer data without real account numbers on screen :: A Data masking · B Steganography · C Key escrow · D Key exchange = a
    - [p] Card numbers replaced in the core system by values with no mathematical link to them :: A Hashing · B Tokenization · C Masking · D Encoding = b
    - *1: HSM = dedicated tamper-resistant crypto hardware for high-value keys. 2: TPM = chip per device, measures boot. 3: KMS = centralised key lifecycle (create, rotate, revoke, audit). 4: secure enclave = isolated processor area on the device. 5: masking hides real values for display or testing. 6: tokens are random stand-ins mapped in a vault, unlike hashes which are derived from the data. Hook: TPM per box, HSM per vault, KMS per fleet, enclave per phone.*
    - @1.4.tool
20. A review of a legacy file-transfer tool finds it encrypts data with DES and RC4. Which recommendation is BEST?
    - **[x] Replace them with AES, using a 256-bit key where possible**  - [ ] Keep DES but double the number of times each file is encrypted  - [ ] Replace them with SHA-256  - [ ] Replace them with RSA for all bulk data
    - *Algorithm choice matters as much as key length: DES (56-bit key) and RC4 are deprecated and breakable. AES is the current symmetric standard, and a longer key (AES-256) gives the most brute-force resistance. Re-running a weak cipher keeps its weakness (3DES is itself deprecated). SHA-256 is a hash, not encryption. RSA is too slow for bulk data. Hook: old ciphers retire; AES is the default.*
    - @1.4.sym

### Key facts
- **Encrypt for confidentiality with the recipient's public key; sign with your own private key. Key escrow = a trusted third party holds key copies; risk = extra copy, mitigate with dual control.**
- **Levels: full-disk, partition, volume, file, database, record; transport = data in transit. Symmetric (AES) for bulk, asymmetric (RSA, ECC) for key exchange and signatures; DH agrees keys without sending them. Longer keys = stronger but slower; ECC = shorter keys for similar strength.**
- **Tools: TPM (per device), HSM (dedicated tamper-resistant hardware), KMS (central key lifecycle), secure enclave (isolated processor area).**
- **Obfuscation: steganography (hide data in other files), tokenization (random substitute, real value in a vault), data masking (hide part of a value).**

## Test 4 - 1.4 Cryptography II: Hashing, Salting, Signatures, Certificates (19 Q)

1. A sysadmin downloads a hypervisor ISO from a mirror site. The vendor's own page lists a SHA-256 value for the file. What does comparing the two values prove?
   - **[x] The file is identical to the one the vendor hashed, so it was not altered**  - [ ] The file is encrypted and safe to store unprotected  - [ ] The mirror site's certificate is valid  - [ ] The file contains no malware of any kind
   - *A matching hash proves integrity: any change, even one bit, produces a completely different digest. It does not encrypt anything. It says nothing about the mirror's TLS certificate. If the vendor itself shipped malware, the hash would still match. Note the hash must come from a trusted source, not the same mirror. Hook: hash = fingerprint of the file.*
   - @1.4.hash
2. A legacy document system still uses MD5 to detect changes in stored contracts. Researchers have shown two different files can be crafted with the same MD5 value. What is the BEST recommendation?
   - **[x] Move to SHA-256, since MD5 is vulnerable to collisions**  - [ ] Keep MD5 but run it twice on each file  - [ ] Replace MD5 with AES encryption of each contract  - [ ] Replace MD5 with Base64 encoding of each contract
   - *A collision is two inputs with the same hash, which lets an attacker swap a document without detection. SHA-256 (SHA-2 family) has no practical collisions. Double MD5 keeps the weakness. AES gives confidentiality, not a change fingerprint. Base64 is reversible encoding with no security. Hook: a hash is only as good as its collision resistance.*
   - @1.4.hash
3. After a breach, analysts notice that 214 accounts in the stolen password table share exactly the same stored value, and it matches a well-known value for "Summer2024!". What weakness does this reveal?
   - **[x] Passwords were hashed without a unique salt per user**  - [ ] Passwords were encrypted with a key that was too short  - [ ] Passwords were stored with key escrow  - [ ] Passwords were tokenized instead of masked
   - *A salt is a random value added to each password before hashing, so identical passwords give different hashes. Without it, the same password always yields the same value and can be looked up in precomputed tables. Key length relates to encryption, and passwords should be hashed, not encrypted. Escrow and tokenization do not apply. Hook: salt makes every hash unique.*
   - @1.4.salt
4. An attacker has a huge precomputed table of hashes for common passwords. Which change to the password store BEST makes that table useless?
   - **[x] Add a random, unique salt to each password before hashing**  - [ ] Store the hashes on an encrypted volume  - [ ] Force users to change passwords every 30 days  - [ ] Display only the first four characters of each hash
   - *Rainbow tables are precomputed for unsalted hashes; a unique salt means the attacker would need a separate table per salt, which is impractical. Volume encryption does not help once the attacker has the table contents. Frequent rotation leads to weaker, predictable passwords. Hiding hash characters on screen is masking, irrelevant to an offline attack. Analogy: every lock gets its own cut, so a master key ring is worthless.*
   - @1.4.salt
5. A start-up already salts its password hashes but fears a GPU rig could still test billions of guesses per second against a stolen copy. What should it add?
   - **[x] Key stretching, such as PBKDF2 or bcrypt, to make each guess slow**  - [ ] A shorter salt so hashing is faster for users  - [ ] Base64 encoding of the stored hashes  - [ ] Data masking on the login page
   - *Key stretching runs the hash many thousands of times (PBKDF2, bcrypt), so each guess costs the attacker real time while a single login stays quick. A shorter salt weakens things. Base64 is reversible and adds nothing. Masking only hides characters on screen. Hook: salt beats precomputation, stretching beats speed.*
   - @1.4.stretch
6. A vendor signs its software updates. When a client receives an update, which key does it use to verify the signature?
   - **[x] The vendor's public key**  - [ ] The vendor's private key  - [ ] The client's private key  - [ ] A shared symmetric key from the vendor
   - *The vendor signs with its private key; anyone verifies with the matching public key, usually taken from the vendor's certificate. If a client needed the vendor's private key, the key would no longer be private. The client's own keys play no part. Symmetric keys cannot give non-repudiation because both sides hold them. Hook: sign private, verify public.*
   - @1.4.sig
7. An endpoint agent refuses to install a driver update because its digital signature fails verification, although the file name and size look normal. What is the BEST next action?
   - **[x] Block the update and obtain a fresh copy from the vendor's official source**  - [ ] Install it, since the file name and size match the vendor's release notes  - [ ] Disable signature checking temporarily for this driver  - [ ] Re-sign the file with the company's own code-signing certificate
   - *A failed signature means the file was changed or did not come from the vendor, so integrity and authenticity are unproven. Name and size are easy to fake. Disabling checks is exactly what an attacker wants. Re-signing it would vouch for a file you cannot trust. Hook: a broken seal means do not drink.*
   - @1.4.sig
8. Which process BEST describes how a digital signature is created for an email?
   - **[x] Hash the message, then encrypt the hash with the sender's private key**  - [ ] Encrypt the message with the recipient's public key, then hash it  - [ ] Hash the message with a salt and send the salt separately  - [ ] Encrypt the message with a shared AES key known to both sides
   - *The signature is the message digest encrypted with the sender's private key. The recipient decrypts it with the sender's public key and compares it with their own hash of the message: a match proves integrity, authenticity and non-repudiation. Encrypting with the recipient's public key is confidentiality, not signing. Salts are for password storage. A shared AES key cannot prove which party wrote it. Hook: signature = sealed fingerprint.*
   - @1.4.sig
9. A group of shipping firms want a shared record of container handovers that no single firm can quietly edit after the fact. Why is a blockchain-based open public ledger a good fit?
   - **[x] Each block includes the hash of the previous block and copies are held by all participants, so changes are evident**  - [ ] Each block is encrypted so only the original firm can read it  - [ ] A central administrator can roll back any incorrect entries  - [ ] The ledger uses tokenization to hide every container number
   - *Blockchain chains blocks by hash: altering an old entry breaks every later link, and every participant holds a copy of the open ledger, so tampering is visible. The point is transparency, not secrecy. A central admin who can rewrite history is exactly what it avoids. Tokenization is unrelated. Analogy: a shared notebook where every page quotes the page before it.*
   - @1.4.chain
10. A company's public online store shows browser warnings because it uses a self-signed certificate. What is the BEST fix?
    - **[x] Get a certificate from a third-party CA that browsers already trust**  - [ ] Tell customers to click through the warning  - [ ] Switch from TLS to plain HTTP so the warning goes away  - [ ] Generate a new self-signed certificate with a longer key
    - *Browsers trust certificates that chain to a root CA in their trust store; public sites need a third-party (public) CA certificate. Training users to ignore warnings makes them easy prey for real attacks. Plain HTTP removes encryption. A longer self-signed key is still self-signed and still untrusted. Hook: self-signed = vouching for yourself.*
    - @1.4.cert
11. An internal wiki uses a certificate from the company's own private CA. Managed laptops trust it, but contractors' personal laptops show warnings. Why?
    - **[x] The private CA's root certificate is not in the contractors' trust stores**  - [ ] The wiki's certificate uses a wildcard name  - [ ] Private CAs cannot issue TLS certificates  - [ ] The wiki's certificate is listed on the OCSP responder as good
    - *Trust starts at a root of trust: a root CA certificate installed in the device's trust store. Managed devices received the company root through policy; personal ones did not. Wildcards have no bearing on trust. Private CAs issue TLS certificates all the time. An OCSP "good" status would be fine. Hook: the chain of trust is only as good as its anchor.*
    - @1.4.cert
12. A team requests a certificate for *.example.com. Which hostname would it NOT protect?
    - **[x] api.dev.example.com**  - [ ] www.example.com  - [ ] mail.example.com  - [ ] shop.example.com
    - *A wildcard covers exactly one label in the asterisk's place, so www, mail and shop are covered, but a second level such as api.dev.example.com is not (it would need *.dev.example.com or a SAN entry). The bare domain example.com is also not matched by the wildcard itself. Hook: one star, one label. Risk: one stolen wildcard key exposes every subdomain.*
    - @1.4.wild
13. An admin is preparing a certificate signing request for a new VPN gateway. What should the CSR contain?
    - **[x] The gateway's public key and identity details such as its hostname**  - [ ] The gateway's private key so the CA can sign it  - [ ] The CA's private key  - [ ] The CRL of all previously revoked certificates
    - *CSR generation creates a key pair on the gateway; the CSR holds the public key plus subject details, and is signed with the private key to prove possession. The private key never leaves the device. The CA's private key stays with the CA. CRLs are published separately by the CA. Hook: send the CA your public key and your name, never your secret.*
    - @1.4.csr
14. A web server's private key was stolen last night. The new certificate is installed. What must ALSO happen so clients stop trusting the old one?
    - **[x] Revoke the old certificate so it appears on the CRL and in OCSP responses**  - [ ] Nothing, since the new certificate replaces it automatically  - [ ] Delete the old certificate file from the server  - [ ] Wait for the old certificate to expire
    - *An attacker with the old key could still present the old certificate until it is revoked; revocation publishes it on the CA's CRL (certificate revocation list) and OCSP. Deleting your copy does nothing to the attacker's copy. Waiting for expiry leaves months of exposure. Hook: rotate AND revoke.*
    - @1.4.revoke
15. A bank wants clients to check a certificate's revocation status in real time for each connection, rather than downloading a large list that may be hours old. What should it rely on?
    - **[x] OCSP**  - [ ] CRL  - [ ] CSR  - [ ] Wildcard certificates
    - *OCSP (online certificate status protocol) answers "is this one certificate still good?" on demand. A CRL is a periodically published list the client must download and may be out of date. A CSR is a request for a new certificate. Wildcards are a naming option. Hook: CRL = printed list, OCSP = phone the bank.*
    - @1.4.revoke
16. A developer needs HTTPS for a throwaway test VM that only she will use for an afternoon. Which choice is MOST appropriate?
    - **[x] A self-signed certificate**  - [ ] A wildcard certificate from a public CA  - [ ] An extended validation certificate from a public CA  - [ ] A certificate signed by the company's root CA private key directly
    - *Self-signed certificates are free and instant, fine for short-lived internal testing where you control the only client. Public CA certificates cost time or money and a public wildcard would put a high-value key on a throwaway VM. Using the root CA key directly for a test box puts the organisation's root of trust at risk. Hook: self-signed for the lab, CA-signed for anyone else.*
    - @1.4.cert
17. PBQ 1.9 - Password store review. A developer proposes how a new app will store passwords. Pick the BEST choice for each part.
    - [p] Stored form of each password :: A AES-encrypted · B Hashed · C Base64-encoded · D Tokenized = b
    - [p] Hash algorithm :: A MD5 · B SHA-256 · C CRC32 · D Base64 = b
    - [p] Salt policy :: A One salt for all users · B A random unique salt per user · C No salt · D The username as salt = b
    - [p] Defence against fast GPU guessing :: A Key stretching (bcrypt or PBKDF2) · B Shorter salt · C Data masking · D Steganography = a
    - [p] Where the salt is stored :: A Alongside each hash · B Kept secret in an HSM only · C Sent to the user by email · D Not stored at all = a
    - *1: hashing is one-way, so a stolen store reveals no plaintext; encryption can be reversed by anyone with the key. 2: MD5 has known collisions, CRC32 is a checksum, Base64 is encoding. 3: a unique random salt makes identical passwords hash differently. 4: stretching makes every guess expensive. 5: salts are not secrets; they are stored with the hash so the system can recompute it at login. Hook: hash, salt, stretch.*
    - @1.4.salt
18. PBQ 1.10 - Certificate lifecycle. A retailer is setting up TLS for shop.example.net and several other subdomains. Answer each part.
    - [p] First step on the web server :: A Generate a key pair and CSR · B Send the private key to the CA · C Download the CRL · D Self-sign the root = a
    - [p] Who signs the certificate for public customers :: A The web server itself · B A trusted third-party CA · C The OCSP responder · D The developer = b
    - [p] One certificate covering www, shop and pay subdomains :: A Wildcard *.example.net · B Self-signed · C Root CA certificate · D CSR = a
    - [p] Why the browser trusts it :: A It chains to a root CA in the trust store · B It uses a long key · C It is listed on the CRL · D It was installed recently = a
    - [p] Key is later stolen. Status the CA publishes :: A Revoked on the CRL and via OCSP · B Renewed · C Escrowed · D Masked = a
    - *1: CSR generation starts on the server with its own key pair. 2: public trust needs a third-party CA. 3: a wildcard covers one label of subdomains. 4: root of trust = the root CA certificate already in the browser or OS store. 5: revocation lists the certificate on the CRL and OCSP. Hook: request, sign, trust, revoke.*
    - @1.4.cert
19. A company builds an internal PKI. Its architect keeps the root CA powered off in a safe and uses an online intermediate CA to issue everyday certificates. Why?
    - **[x] The root is the root of trust; if the intermediate is breached it can be revoked and replaced without rebuilding trust on every device**  - [ ] Offline roots issue certificates faster than online ones  - [ ] Intermediate CAs do not need private keys  - [ ] Browsers only accept certificates signed directly by an offline root
    - *Every device trusts the root CA certificate in its store, so a stolen root key would undermine every certificate. Keeping the root offline protects that anchor; the intermediate does the daily signing and can be revoked by the root if compromised. Offline roots issue nothing day to day. Every CA has a private key. Browsers accept chains through intermediates. Hook: the crown stays in the vault, the deputy signs the paperwork.*
    - @1.4.cert

### Key facts
- **Hashing = one-way fingerprint for integrity; use SHA-256, avoid MD5 (collisions). Salt = unique random value per password, defeats rainbow tables. Key stretching (PBKDF2, bcrypt) slows each guess.**
- **Digital signature = hash encrypted with the sender's private key; verify with the sender's public key. Gives integrity, authenticity, non-repudiation.**
- **Blockchain = hash-linked blocks on a distributed open public ledger; tampering is evident.**
- **Certificates: CA signs; root of trust = root CA in the trust store; self-signed = untrusted outside your control; third-party CA for public sites; CSR holds public key + identity; wildcard = one label (*.example.com); revoke via CRL (list) or OCSP (real-time query).**

## Test 5 - 2.1 Threat Actors, Attributes, Motivations (21 Q)

1. A regional energy grid operator finds an implant in its control network that has been beaconing quietly for 14 months, using tooling no security vendor has catalogued. Nothing has been stolen or sold. Which actor is MOST likely responsible?
   - **[x] Nation-state**  - [ ] Organized crime  - [ ] Hacktivist  - [ ] Unskilled attacker
   - *Nation-state = government-backed, the most funding and patience, custom tools, aims like espionage or pre-positioning for war. Organized crime is well funded too but wants a payout soon; 14 months with nothing monetised does not fit. Hacktivists want publicity, not silence. Unskilled attackers cannot build novel tooling. Hook: flag on the payroll, patience in the plan.*
   - @2.1.nation
2. Threat intel links an intrusion at a shipping firm to a foreign military unit. The attackers wiped navigation servers on the same day a border dispute escalated. Which motivation BEST fits?
   - **[x] War**  - [ ] Financial gain  - [ ] Blackmail  - [ ] Ethical
   - *Destructive attacks timed with a geopolitical conflict, by a military actor, point to war as the motive. No ransom or extortion demand rules out financial gain and blackmail. Ethical hackers report flaws, they do not wipe servers. Hook: tanks on the border, wipers in the network.*
   - @2.1.nation
3. A help desk sees a burst of failed attacks from one IP using an unmodified public exploit kit, with the kit's default banner still in the payload. Which actor and sophistication level fit BEST?
   - **[x] Unskilled attacker, low sophistication**  - [ ] Nation-state, high sophistication  - [ ] Organized crime, high sophistication  - [ ] Insider threat, medium sophistication
   - *Unskilled attacker (the 701 term for script kiddie) runs others' tools without changing them, so a default banner is a giveaway. Low resources, low skill. Nation-states and organised gangs customise and hide. An insider would not need a noisy external exploit. Analogy: driving a car without knowing what an engine is.*
   - @2.1.unskilled
4. A city council website is defaced with a protest message about a planned road scheme the day before a public vote. Which actor is MOST likely?
   - **[x] Hacktivist**  - [ ] Organized crime  - [ ] Nation-state  - [ ] Shadow IT
   - *Hacktivist = attacks to promote a political or social cause; defacement and DDoS are typical because they are public. No ransom means not organised crime. A nation-state would not waste access on a local protest banner. Shadow IT is unapproved tech, not an attacker. Hook: hacker plus activist, the message is the goal.*
   - @2.1.hacktivist
5. An activist group leaks a pharmaceutical firm's internal emails, saying the public deserves to know about suppressed trial results. Which motivation is this?
   - **[x] Philosophical or political beliefs**  - [ ] Financial gain  - [ ] Revenge  - [ ] Espionage
   - *A cause-driven leak to shape public opinion is philosophical/political motivation. They are not selling the data (not financial). Revenge is personal grievance, usually from an ex-employee. Espionage is quiet and the data is kept, not published. Hook: belief drives the leak.*
   - @2.1.hacktivist
6. A database admin given two weeks' notice copies the customer table to a personal cloud drive on her last afternoon. Which actor attributes BEST describe her?
   - **[x] Internal, with legitimate access and low cost to attack**  - [ ] External, well funded and highly sophisticated  - [ ] Internal, but needing custom exploits to reach the data  - [ ] External, relying on default credentials to get in
   - *Insider threats are internal: they already hold credentials and know where the data is, so they need little skill or money. Custom exploits are unnecessary when you have the keys. External options ignore that she is staff. Hook: the threat already has a badge.*
   - @2.1.insider
7. Which control would BEST reduce the impact of the insider in the previous scenario before she leaves?
   - **[x] Disabling her access as soon as notice is given, plus DLP on cloud uploads**  - [ ] A stronger perimeter firewall at the internet edge  - [ ] An IPS signature for known exploit kits  - [ ] Longer password requirements for all staff
   - *Insiders bypass the perimeter, so you control their access and watch data leaving: timely deprovisioning, least privilege, DLP. Firewalls and IPS target outsiders. Longer passwords do nothing against someone who already knows hers. Hook: lock the inside door, not just the front gate.*
   - @2.1.insider
8. A fired engineer logs back in through a forgotten service account and deletes the build pipeline. Which motivation is MOST likely?
   - **[x] Revenge**  - [ ] Espionage  - [ ] Financial gain  - [ ] Philosophical beliefs
   - *Destruction by someone with a personal grievance against the employer = revenge. No data was sold or kept, so not financial or espionage. No cause is declared. Hook: grudge plus leftover access.*
   - @2.1.insider
9. A gang encrypts a dental chain's servers and threatens to publish patient X-rays unless paid in cryptocurrency within 72 hours. Which actor and motive fit BEST?
   - **[x] Organized crime, financial gain**  - [ ] Hacktivist, political beliefs  - [ ] Nation-state, espionage  - [ ] Insider, revenge
   - *Ransom plus deadline plus crypto payment = organised crime chasing money. Well funded and professional, but profit focused. Hacktivists publish to make a point, not for payment. Nation-states rarely demand ransom. Hook: follow the wallet.*
   - @2.1.orgcrime
10. An attacker emails a CFO: "We have screenshots of your private messages. Pay 2 BTC or we send them to your board." No systems are encrypted. Which motivation is this?
    - **[x] Blackmail**  - [ ] Service disruption  - [ ] Data exfiltration  - [ ] War
    - *Blackmail = threatening to release damaging information unless paid. It is aimed at a person, and nothing is disrupted. Data exfiltration may have happened earlier but the motive now is coercion. Hook: pay or I tell.*
    - @2.1.orgcrime
11. Marketing staff sign up for an AI transcription service with company cards and upload recorded client calls. IT was never told. What is this an example of, and what is the MAIN risk?
    - **[x] Shadow IT, unmanaged data leaving the organisation**  - [ ] Insider threat, deliberate sabotage  - [ ] Hacktivism, public data leaks  - [ ] Unskilled attacker, malware infection
    - *Shadow IT = staff using tech outside IT's approval. Usually well meaning, but data lands in services with no security review, contract or monitoring. It is not malicious sabotage. Hook: helpful, hidden, unmanaged.*
    - @2.1.shadowit
12. A CISO wants to reduce shadow IT without killing productivity. What is the BEST first step?
    - **[x] Discover what unsanctioned apps are in use, then offer approved alternatives**  - [ ] Fire staff found using any unapproved app  - [ ] Block all outbound HTTPS from user subnets  - [ ] Publish a list of hacker groups to watch for
    - *Shadow IT happens because users need something; find it (for example CASB or proxy logs), then give a sanctioned option and a request process. Firing and blanket blocking drive it further underground or stop work. Threat actor lists are unrelated. Hook: find it, then replace it.*
    - @2.1.shadowit
13. Two attacks hit a retailer: one used a zero-day in the POS firmware, the other used a leaked password. Which attribute MOST separates the two actors?
    - **[x] Level of sophistication and resources**  - [ ] Internal versus external location  - [ ] Whether the target was a retailer  - [ ] Whether the attack used the internet
    - *Writing or buying a zero-day takes skill and money; reusing a leaked password takes almost none. Attributes on the exam: internal/external, resources/funding, sophistication. Both could be external. Hook: what did it cost them to do this?*
    - @2.1.attr
14. Ranking actors by budget alone, which one usually sits at the TOP?
    - **[x] Nation-state**  - [ ] Hacktivist  - [ ] Unskilled attacker  - [ ] Shadow IT
    - *Government budgets beat everyone, organised crime is next. Hacktivists often rely on volunteers. Unskilled attackers have almost nothing. Shadow IT is not an attacker at all. Hook: rank them by wallet: state, crime, activist, kid.*
    - @2.1.attr
15. A researcher finds an IDOR bug in a bank's app, reports it through the bank's disclosure programme and waits for the fix before publishing. Which motivation is this?
    - **[x] Ethical**  - [ ] Blackmail  - [ ] Financial gain  - [ ] Disruption or chaos
    - *Ethical (white hat, often through bug bounty or responsible disclosure) means finding flaws to get them fixed, with permission or proper reporting. A bounty may pay, but the defining trait is disclosure, not extortion. Blackmail would demand payment to stay silent. Hook: report, wait, then publish.*
    - @2.1.motiv
16. A competitor's agent poses as a cleaner to photograph a startup's whiteboard roadmap. Which motivation is this?
    - **[x] Espionage**  - [ ] Service disruption  - [ ] Revenge  - [ ] Ethical
    - *Espionage = secretly collecting information for advantage; corporate espionage counts, not just governments. Nothing is broken, so not disruption. No grudge, so not revenge. Hook: watch and copy, never break.*
    - @2.1.motiv
17. An anonymous forum user floods a game studio's login servers for hours, posting "just for fun" with no demands. Which motivation is MOST likely?
    - **[x] Disruption or chaos**  - [ ] Financial gain  - [ ] Philosophical beliefs  - [ ] Espionage
    - *No ransom, no cause, no stolen data: the goal is the mayhem itself. Service disruption is close, but the stated reason ("for fun") points at chaos. Hook: some people just want to watch the servers burn.*
    - @2.1.motivdisrupt
18. A botnet takes a payment processor offline during Black Friday, and the operators later sell "downtime as a service" to the processor's rival. Which motivation BEST describes the attack?
    - **[x] Service disruption, paid for by a competitor**  - [ ] Data exfiltration  - [ ] Ethical  - [ ] Blackmail
    - *The aim was to knock the service over at its busiest moment; the rival paid for that outcome. No data left, no threat to release anything. Hook: if the goal is "make it stop working", it is service disruption.*
    - @2.1.motivdisrupt
19. Logs show 40 GB of design files leaving an aerospace firm to an overseas host over three nights, but no ransom or leak follows. Which motivation is MOST likely?
    - **[x] Data exfiltration for espionage**  - [ ] Service disruption  - [ ] Revenge  - [ ] Disruption or chaos
    - *Large quiet outbound transfers with no follow-up demand = stealing data to use it. Nothing was disrupted. Revenge actors want visible harm. Hook: the data left and went silent.*
    - @2.1.motivdisrupt
20. PBQ 2.1 - Actor profiles. Match each incident to the MOST likely actor, then its main motivation. ¶  1  Ransomware with a leak-site threat against a law firm ¶  2  Defacement of an oil company site with a climate message ¶  3  Sales team running an unapproved file-sharing app ¶  4  Months-long silent access to a ministry's email ¶  5  Teen running a downloaded DDoS tool against a school
    - [p] Incident 1 actor :: A Nation-state · B Organized crime · C Hacktivist · D Unskilled attacker · E Shadow IT = b
    - [p] Incident 1 motive :: A Financial gain · B Political beliefs · C Espionage · D Disruption/chaos · E None (not malicious) = a
    - [p] Incident 2 actor :: A Nation-state · B Organized crime · C Hacktivist · D Unskilled attacker · E Shadow IT = c
    - [p] Incident 2 motive :: A Financial gain · B Political beliefs · C Espionage · D Disruption/chaos · E None (not malicious) = b
    - [p] Incident 3 actor :: A Nation-state · B Organized crime · C Hacktivist · D Unskilled attacker · E Shadow IT = e
    - [p] Incident 3 motive :: A Financial gain · B Political beliefs · C Espionage · D Disruption/chaos · E None (not malicious) = e
    - [p] Incident 4 actor :: A Nation-state · B Organized crime · C Hacktivist · D Unskilled attacker · E Shadow IT = a
    - [p] Incident 4 motive :: A Financial gain · B Political beliefs · C Espionage · D Disruption/chaos · E None (not malicious) = c
    - [p] Incident 5 actor :: A Nation-state · B Organized crime · C Hacktivist · D Unskilled attacker · E Shadow IT = d
    - [p] Incident 5 motive :: A Financial gain · B Political beliefs · C Espionage · D Disruption/chaos · E None (not malicious) = d
    - *1: ransom plus leak threat = organised crime, money. 2: cause-driven defacement = hacktivist, political. 3: unsanctioned app = shadow IT, convenience not malice. 4: long silent access to government mail = nation-state, espionage. 5: off-the-shelf tool, no demand = unskilled attacker, chaos. Hook: ask "what do they get out of it?"*
    - @2.1.actor
21. An intel report describes a state-sponsored group that has kept hidden footholds in several ministries for years, quietly returning whenever it is cleaned out. What term BEST describes this kind of threat?
    - **[x] Advanced persistent threat (APT)**  - [ ] Insider threat  - [ ] Hacktivist campaign  - [ ] Unskilled attacker
    - *APT = a well-funded, skilled actor (usually a nation-state) that gets in, stays hidden and keeps coming back over a long period. Insiders already belong to the organisation; hacktivists want attention; unskilled attackers lack the skill to stay hidden. Hook: advanced tools, persistent presence.*
    - @2.1.nation

- **Actors: nation-state, unskilled attacker, hacktivist, insider, organized crime, shadow IT. Attributes: internal/external, resources/funding, sophistication. Motives: exfiltration, espionage, service disruption, blackmail, financial gain, philosophical/political, ethical, revenge, disruption/chaos, war.**

## Test 6 - 2.2 Threat Vectors, Attack Surfaces, Social Engineering (24 Q)

1. Staff at a logistics firm receive texts saying "Your parcel is held, pay the 1.99 redelivery fee" with a short link. Which vector is this?
   - **[x] Smishing (SMS-based message)**  - [ ] Vishing  - [ ] Watering hole  - [ ] Typosquatting
   - *Smishing = phishing over SMS; it is a message-based vector. Vishing is voice. A watering hole compromises a site the victims already visit. Typosquatting relies on a mistyped domain, not a text lure. Hook: S for SMS.*
   - @2.2.msg
2. An attacker sends a team chat message from a compromised partner account with a link to a "shared invoice". Which control would BEST reduce this vector?
   - **[x] Restricting external access in the chat platform and scanning links**  - [ ] Disabling Bluetooth on all laptops  - [ ] Changing the Wi-Fi WPA3 passphrase  - [ ] Enforcing full-disk encryption
   - *Instant messaging is a message-based vector like email: limit who can message in from outside and inspect links. Bluetooth, Wi-Fi keys and FDE do nothing about a malicious link in a chat. Hook: the vector is the conversation, so control the conversation.*
   - @2.2.msg
3. A marketing PC is infected after opening a PNG from a forum. The image renderer had an unpatched parsing flaw. Which vector BEST describes this?
   - **[x] Image-based**  - [ ] Voice call  - [ ] Removable device  - [ ] Default credentials
   - *Image-based vectors hide code or exploits in image files (malformed data, steganography, SVG scripts). File-based is the broader cousin, but the exam lists image-based separately and the file here is an image. Hook: a picture worth a thousand exploits.*
   - @2.2.file
4. A finance team receives a macro-enabled spreadsheet titled "Q3 bonuses" from an outside address. What is the BEST mitigation for this file-based vector?
   - **[x] Block macros in files from the internet and sandbox attachments**  - [ ] Require WPA3 on the office wireless  - [ ] Disable USB ports on the finance PCs  - [ ] Move the mail server into a screened subnet
   - *File-based vectors (Office macros, PDFs, archives) are cut by blocking internet macros and detonating attachments in a sandbox. Wireless, USB and DMZ placement do not touch an emailed file. Hook: the file is the payload, so treat files with suspicion.*
   - @2.2.file
5. A caller claiming to be from the bank's fraud team asks a payroll clerk to read out the code just texted to her phone. Which attack is this?
   - **[x] Vishing**  - [ ] Smishing  - [ ] Watering hole  - [ ] Brand impersonation on a website
   - *Vishing = voice phishing; the call is the vector even though a text is involved, because the code is extracted by voice. Smishing would be a lure in the SMS itself. Hook: V for voice.*
   - @2.2.voice
6. Reception staff find a thumb drive marked "Bonus list - confidential" near the entrance and insert it into the visitor-badge PC to find its owner. Which control BEST blocks this vector?
   - **[x] Endpoint policy blocking unapproved removable media, plus awareness training**  - [ ] TLS 1.3 on the corporate website  - [ ] A longer DNS TTL  - [ ] Stronger password complexity
   - *Removable devices (USB drops) rely on curiosity; stop them with device control and training. TLS, DNS and passwords are unrelated to a stick in a USB port. Hook: if you did not bring it, do not plug it in.*
   - @2.2.removable
7. A security team compares two inventory tools: one installs a client on every laptop, the other scans over the network with no install. Which statement about attack surface is MOST accurate?
   - **[x] The client-based tool adds software on each host that itself may be vulnerable**  - [ ] Agentless tools never create any network exposure  - [ ] Client-based tools remove the need to patch the OS  - [ ] Agentless tools must run as malware to work
   - *Vulnerable software is a vector: client-based means another program on every endpoint to patch; agentless means no install, but it needs credentials and network access, which have their own risks. Hook: every agent is another door to lock.*
   - @2.2.software
8. A plant still runs a Windows version that has had no vendor updates for three years because the CNC software needs it. What is the BEST interim approach?
   - **[x] Isolate it on its own segment with strict access rules until it can be replaced**  - [ ] Leave it as is, since it has worked for years  - [ ] Join it to the main office VLAN for easier monitoring  - [ ] Install the newest browser on it
   - *Unsupported systems and applications cannot be patched, so the vector stays open; compensate by isolating and limiting access, and plan replacement. Joining the office VLAN spreads the risk. A new browser does not fix the OS. Hook: if you cannot fix it, fence it.*
   - @2.2.unsupported
9. A sales rep connects to a coffee-shop open Wi-Fi named "Free_Cafe_WiFi" and gets a certificate warning on the CRM. Which vector is MOST relevant and what is the BEST protection?
   - **[x] Unsecure wireless network; always-on VPN**  - [ ] Removable device; USB blocking  - [ ] Default credentials; password change  - [ ] Watering hole; DNS filtering only
   - *Open or rogue wireless is an unsecure network vector, and a cert warning suggests an on-path attacker. An always-on VPN encrypts traffic regardless of the hotspot. Hook: treat every public network as hostile.*
   - @2.2.network
10. An engineer notices a nearby phone pushing unsolicited contact cards and files to conference-room laptops. Which vector should be reduced FIRST?
    - **[x] Bluetooth, by turning off discoverable mode**  - [ ] Wired Ethernet, by 802.1X  - [ ] Voice calls, by caller ID  - [ ] SMS, by spam filtering
    - *Unsolicited pushes from a nearby device are Bluetooth (bluejacking; data theft is bluesnarfing). Disable discoverability or Bluetooth when unused. 802.1X protects wired/Wi-Fi ports. Hook: short range, short leash.*
    - @2.2.network
11. A visitor plugs a small device into a live network jack in an empty meeting room and immediately gets an internal IP address. Which vector is this, and the BEST control?
    - **[x] Unsecure wired network; 802.1X port authentication and disabling unused jacks**  - [ ] Bluetooth; turning off discoverable mode  - [ ] Voice call; caller ID checks  - [ ] Image-based; blocking PNG files
    - *Wired networks are an unsecure network vector when any jack hands out access. 802.1X (port-based NAC) makes a device authenticate before the port forwards traffic, and unused ports should be disabled. Hook: a live jack in an empty room is an open door.*
    - @2.2.network
12. An external scan shows TCP 3389 (RDP) and 23 (Telnet) open on a branch router's public IP 203.0.113.40. What is the BEST action?
    - **[x] Close the unneeded ports and put remote admin behind a VPN**  - [ ] Change the router's hostname  - [ ] Add a login banner to the Telnet service  - [ ] Move RDP to port 3390 and leave it public
    - *Open service ports expand the attack surface; anything not required should be closed, and admin access gated. A banner or hostname changes nothing. Moving the port is obscurity: scanners still find it. Hook: every open port is an unlocked window.*
    - @2.2.ports
13. A facilities contractor mounts a door-entry intercom whose web console still opens with the factory login printed in its manual. Which vector does this represent?
    - **[x] Default credentials**  - [ ] Image-based  - [ ] Unsupported application  - [ ] Supply chain
    - *Default credentials are published in manuals and botnets (for example Mirai) try them automatically. Change them during deployment. It is not image-based (nothing is hidden in a picture file), the device is still supported, and the supplier did not plant anything; the installer just left the factory login in place. Hook: the password is in the PDF.*
    - @2.2.defcreds
14. Forty client firms are hit with ransomware on the same night. The common link is the outsourced IT provider whose remote monitoring agent runs on all their machines. Which vector is this?
    - **[x] Supply chain, via an MSP**  - [ ] Watering hole  - [ ] Typosquatting  - [ ] Unskilled attacker
    - *Supply chain vectors abuse trusted third parties: MSPs, vendors, suppliers. One breach fans out to every customer. A watering hole is a website, not a trusted admin tool. Hook: breach one, reach many.*
    - @2.2.supply
15. Before giving a cleaning contractor badge access to the server floor, what is the BEST supply chain control?
    - **[x] Vet the supplier and limit badge access to escorted, scheduled times**  - [ ] Install a WAF in front of the website  - [ ] Ask the contractor to sign the AUP only  - [ ] Give the contractor a domain admin account for convenience
    - *Suppliers and vendors are part of the attack surface; vet them and give least privilege. A WAF is unrelated. An AUP alone does not control physical access. Domain admin is the opposite of least privilege. Hook: trust, but scope it.*
    - @2.2.supply
16. Every employee at a bank receives an email from "IT-Support" asking them to re-validate their password at a look-alike portal. What is this, and what is the BEST technical control?
    - **[x] Phishing; phishing-resistant MFA (FIDO2) plus mail filtering**  - [ ] Vishing; caller ID blocking  - [ ] Watering hole; patching browsers only  - [ ] Pretexting; a clean desk policy
    - *A broad credential lure by email is phishing. Filters catch some, and FIDO2/passkeys stop stolen passwords from being usable on the fake site because the key is bound to the real domain. Hook: if the key will not talk to the fake site, the phish fails.*
    - @2.2.phish
17. The CFO receives an email from the real mailbox of a known supplier, which was hacked, asking to update the bank details for the next payment. Which attack is this, and the BEST process control?
    - **[x] Business email compromise; verify bank changes by calling a known number**  - [ ] Typosquatting; register look-alike domains  - [ ] Smishing; block SMS on company phones  - [ ] Watering hole; patch the CFO's browser
    - *BEC uses a real or convincingly spoofed business mailbox to redirect payments. Because the email is genuine, filters often miss it; out-of-band verification is the fix. Hook: money moves, so verify on a second channel.*
    - @2.2.bec
18. A caller says, "I'm from the auditor's office, we're on a deadline for the regulator, I just need the VPN group name to finish the report." Which technique is the attacker MAINLY using?
    - **[x] Pretexting**  - [ ] Typosquatting  - [ ] Watering hole  - [ ] Brand impersonation
    - *Pretexting = an invented backstory that makes the request seem normal (auditor plus deadline). Impersonation is close, but the stem stresses the story. Brand impersonation copies a company's look in emails or sites. Hook: the pretext is the script.*
    - @2.2.pretext
19. A visitor in a hi-vis vest and hard hat walks behind a delivery driver into a data centre, saying he is "here about the HVAC". Which social engineering method BEST describes this?
    - **[x] Impersonation**  - [ ] Typosquatting  - [ ] Misinformation  - [ ] Watering hole
    - *Impersonation = pretending to be someone with a reason to be there (contractor, IT, police). Following the driver in is tailgating, a physical technique he also used. Hook: dress the part and doors open.*
    - @2.2.pretext
20. Attackers compromise a niche forum used by industrial control engineers and plant malware in its downloads page. Which attack is this?
    - **[x] Watering hole**  - [ ] Typosquatting  - [ ] Vishing  - [ ] Business email compromise
    - *Watering hole = infect a site the target group already trusts and visits, and wait. Typosquatting needs a mistyped URL. Hook: poison the pond the prey drinks from.*
    - @2.2.watering
21. Customers report a site at "paypa1-billing.example" with the real company's logo asking for card details. Which TWO techniques are combined here?
    - **[x] Typosquatting and brand impersonation**  - [ ] Watering hole and vishing  - [ ] Pretexting and smishing  - [ ] BEC and misinformation
    - *Typosquatting registers a near-miss domain (1 for l). Brand impersonation copies a trusted company's look to win trust. Hook: wrong letter, right logo.*
    - @2.2.typo
22. Days before a product launch, fake posts claiming the device catches fire spread across social media from a network of new accounts. Which term BEST fits?
    - **[x] Disinformation**  - [ ] Misinformation  - [ ] Typosquatting  - [ ] Impersonation
    - *Disinformation is deliberately false and spread to cause harm; misinformation is false but shared without intent (people resharing in good faith). A coordinated new-account network shows intent. Hook: dis = deliberate.*
    - @2.2.misinfo
23. PBQ 2.2 - Social engineering triage. Match each report to the technique. ¶  1  Phone call from "IT" asking for an MFA code ¶  2  Text with a fake toll-road payment link ¶  3  Real vendor mailbox asking to change payment account ¶  4  Look-alike domain one letter off the company's ¶  5  Trusted industry site serving malware downloads
    - [p] Report 1 :: A Vishing · B Smishing · C BEC · D Typosquatting · E Watering hole = a
    - [p] Report 2 :: A Vishing · B Smishing · C BEC · D Typosquatting · E Watering hole = b
    - [p] Report 3 :: A Vishing · B Smishing · C BEC · D Typosquatting · E Watering hole = c
    - [p] Report 4 :: A Vishing · B Smishing · C BEC · D Typosquatting · E Watering hole = d
    - [p] Report 5 :: A Vishing · B Smishing · C BEC · D Typosquatting · E Watering hole = e
    - *Voice = vishing, SMS = smishing, genuine business mailbox redirecting money = BEC, misspelled domain = typosquatting, compromised site the victims already trust = watering hole. Hook: name the channel first, then the trick.*
    - @2.2.se
24. A warehouse still uses access points running WEP, with WPS PIN setup switched on for convenience. Why is this an attack vector?
    - **[x] Both are known-broken wireless options that let outsiders recover keys or join the network**  - [ ] WEP and WPS only slow the network down  - [ ] WPS encrypts traffic more strongly than WPA3  - [ ] They matter only on wired networks
    - *WEP can be cracked in minutes and the WPS PIN can be brute forced, so either one turns the Wi-Fi into an open door. Use WPA3 (or WPA2-Enterprise at minimum) and turn WPS off. Hook: old wireless locks have published master keys.*
    - @2.2.network

- **Vectors: message (email, SMS, IM), image, file, voice, removable device, vulnerable software (client-based vs agentless), unsupported systems, unsecure networks (wireless, wired, Bluetooth), open ports, default credentials, supply chain (MSP, vendors, suppliers). Human: phishing, vishing, smishing, mis/disinformation, impersonation, BEC, pretexting, watering hole, brand impersonation, typosquatting.**

## Test 7 - 2.3 Vulnerabilities I: Application, OS, Web, Hardware (21 Q)

1. An EDR alert shows a process writing code into the memory of a running svchost.exe, then that svchost connects out to 198.51.100.7. Which vulnerability class is being exploited?
   - **[x] Memory injection**  - [ ] Race condition  - [ ] SQL injection  - [ ] Resource reuse
   - *Memory injection = placing malicious code into another process's memory so it runs under that trusted process (DLL injection is a common form). It hides from tools that only look at process names. SQL injection targets databases. Hook: hide in someone else's coat.*
   - @2.3.memory
2. A C service copies a user-supplied name into a 64-byte buffer with no length check, and long inputs crash it. What is the BEST developer fix?
   - **[x] Bounds checking and input validation, using safe string functions**  - [ ] Running the service on a different port  - [ ] Adding a CAPTCHA to the login page  - [ ] Hashing the user's name before storing it
   - *That is a buffer overflow: data spills past the buffer and can overwrite memory, sometimes giving code execution. Fix it in code with length checks and safe functions; ASLR and DEP help as backups. Changing ports or adding CAPTCHA does nothing. Hook: a pint glass does not hold a litre.*
   - @2.3.memory
3. A gift-card site validates that a card still has credit, then deducts it in a separate step. A script fires 20 redemptions within the same millisecond and all succeed. Which flaw is this?
   - **[x] Race condition (TOC/TOU)**  - [ ] Buffer overflow  - [ ] Cross-site scripting  - [ ] Directory traversal
   - *Time-of-check to time-of-use: state changes between the check and the action. Fix with locking or atomic transactions. Hook: two people grab the last seat at once.*
   - @2.3.race
4. An app checks a temp file's permissions, then opens it. Between the two steps an attacker swaps it for a symlink to /etc/shadow. What does this describe?
   - **[x] Race condition - the file changed between time-of-check (TOC) and time-of-use (TOU)**  - [ ] Memory injection into the kernel  - [ ] A malicious update from the vendor  - [ ] A downgrade attack
   - *Same class as before but in the file system: the check was valid, the use was not. Atomic open-and-check calls close the gap. Hook: what you checked is not what you used.*
   - @2.3.race
5. A popular note-taking app's auto-updater pulls a trojanised build after the vendor's build server was compromised. Which vulnerability is this?
   - **[x] Malicious update**  - [ ] Race condition  - [ ] Jailbreaking  - [ ] Default credentials
   - *Malicious update = attacker code shipped through the legitimate update channel, so it arrives signed and trusted. Defend with code-signing checks, staged rollouts and vendor monitoring. Hook: the delivery van is real, the parcel is not.*
   - @2.3.update
6. What control BEST reduces the risk of a malicious update reaching all 3,000 endpoints at once?
   - **[x] Stage updates to a test ring first and verify signatures before broad rollout**  - [ ] Turn off all updates permanently  - [ ] Allow users to install updates from any website  - [ ] Disable the host firewall during updates
   - *Staged rings limit the blast radius; signature checks catch tampering in transit. Turning off updates leaves known flaws open. Hook: canary first, flock later.*
   - @2.3.update
7. A patch Tuesday bulletin lists a kernel privilege escalation flaw in the desktop OS used across the company. Which vulnerability category is this, and the BEST response?
   - **[x] OS-based; test and deploy the patch promptly**  - [ ] Web-based; add a WAF rule  - [ ] Hardware; replace the CPUs  - [ ] Cloud-specific; change the CSP
   - *Flaws in the operating system itself are OS-based. The OS is a huge shared attack surface, so patch management is the main control. A WAF guards web apps. Hook: the foundation cracked, so fix the foundation.*
   - @2.3.os
8. A login form returns all users when the username is entered as admin' OR '1'='1. What is the BEST fix?
   - **[x] Parameterised queries (prepared statements)**  - [ ] Encrypting the database at rest  - [ ] Moving the database to another subnet  - [ ] Longer session timeouts
   - *Classic SQL injection: input is treated as SQL code. Parameterised queries keep data and code separate; input validation helps too. Encryption at rest does nothing when the app itself runs the query. Hook: never let the user write your SQL.*
   - @2.3.sqli
9. A WAF log shows requests containing UNION SELECT and -- comments against /products?id=. Which attack is being attempted?
   - **[x] SQL injection**  - [ ] Cross-site scripting  - [ ] Directory traversal  - [ ] Buffer overflow
   - *UNION SELECT and SQL comment markers are SQL injection signatures. XSS shows script tags; traversal shows ../ sequences. Hook: SQL words in a URL = SQLi.*
   - @2.3.sqli
10. A recipe site saves reviews to its database and shows them to everyone. One review carries JavaScript that posts each viewer's session token to an outside host. Which vulnerability is this?
    - **[x] Stored (persistent) cross-site scripting**  - [ ] Reflected cross-site scripting  - [ ] SQL injection  - [ ] Cross-site request forgery
    - *Stored XSS saves the script on the server so it runs for everyone who views the page. Reflected XSS bounces off a crafted link to one victim. CSRF makes a victim's browser send a request; it does not inject script. Hook: stored = booby-trapped page, reflected = booby-trapped link.*
    - @2.3.xss
11. What is the BEST combination of controls against XSS?
    - **[x] Output encoding and input validation, with a Content Security Policy**  - [ ] Parameterised SQL queries only  - [ ] Full-disk encryption on the web server  - [ ] Changing the web server to a non-standard port
    - *XSS is stopped by encoding output so the browser treats it as text, validating input, and CSP to limit where scripts may load from. Parameterised queries fix SQLi, not XSS. Hook: encode on the way out.*
    - @2.3.xss
12. A security engineer finds that the BIOS on 200 laptops has a known flaw allowing persistence below the OS. Which category, and BEST fix?
    - **[x] Firmware vulnerability; apply the vendor's firmware update**  - [ ] Web vulnerability; add a WAF  - [ ] OS vulnerability; reinstall Windows  - [ ] Cloud vulnerability; rotate API keys
    - *Firmware sits under the OS, so reinstalling the OS does not remove it. Patch firmware from the vendor and enable Secure Boot. Hook: the bug is in the basement, not the living room.*
    - @2.3.hw
13. A NAS model's manufacturer stopped publishing security fixes for it last year, but it still holds file shares. What is the MAIN risk?
    - **[x] New vulnerabilities will never be patched**  - [ ] The device will stop working on a set date  - [ ] Its data is automatically deleted  - [ ] It can no longer be monitored
    - *End-of-life (EOL) means no more vendor support or patches, so new flaws stay open forever. It may run fine for years, which is why it is easy to ignore. Hook: still works, but nobody is fixing it.*
    - @2.3.hw
14. A manufacturer runs a 20-year-old control system that cannot be upgraded without halting production, and the vendor went bust. Which BEST describes it and the MOST practical mitigation?
    - **[x] Legacy hardware; segment it and restrict access**  - [ ] Zero-day; wait for the vendor patch  - [ ] Shadow IT; ban its use  - [ ] Cloud-specific; move it to SaaS
    - *Legacy = old systems still in use that may lack modern security and support. If you cannot replace them, isolate them. There is no vendor to patch it. Hook: if it is old and vital, put a fence round it.*
    - @2.3.hw
15. A pen tester bypasses a web app's login by editing a hidden form field from role=user to role=admin. Which BEST describes the root cause?
    - **[x] The app trusts client-side input for authorisation decisions**  - [ ] A buffer overflow in the web server  - [ ] An expired TLS certificate  - [ ] A race condition in the database
    - *Web apps must enforce authorisation on the server; anything in the browser can be changed. This is a web-based application flaw. Hook: never let the customer set their own price tag.*
    - @2.3.web
16. Which practice BEST prevents many web-based vulnerabilities before release?
    - **[x] Secure coding with static and dynamic testing in the pipeline**  - [ ] Annual password rotation for developers  - [ ] Installing antivirus on the web server only  - [ ] Using a larger instance size in the cloud
    - *SAST checks source code, DAST probes the running app; together they catch injection and logic flaws early. Antivirus and bigger servers do not fix code. Hook: find bugs where they are cheap, in the pipeline.*
    - @2.3.web
17. After a breach, the leaked user table shows every password stored as a plain MD5 digest with no salt. Which vulnerability category is this?
    - **[x] Cryptographic**  - [ ] Race condition  - [ ] Memory injection  - [ ] Hardware
    - *Weak or outdated algorithms (MD5, SHA-1, DES), poor key handling or missing salts are cryptographic vulnerabilities. Rainbow tables crack unsalted MD5 fast. Fix: a slow salted hash such as bcrypt or Argon2. Hook: the lock is old and everyone has the key.*
    - @2.3.crypto
18. A web server still accepts TLS 1.0 and export-grade ciphers for "compatibility". What is the BEST action?
    - **[x] Disable old protocol versions and weak cipher suites**  - [ ] Add a CAPTCHA to the homepage  - [ ] Rename the server  - [ ] Turn off HTTP logging
    - *Supporting weak protocols is a cryptographic vulnerability and invites downgrade attacks. Allow only TLS 1.2+ with strong suites. Hook: a door that still accepts the old key is not locked.*
    - @2.3.crypto
19. A test VM spun up by a developer ships with debug mode on and a stack trace page that reveals database credentials. Which vulnerability is this?
    - **[x] Misconfiguration**  - [ ] Zero-day  - [ ] Firmware flaw  - [ ] Race condition
    - *Misconfiguration = insecure settings, not bad code: debug enabled, open storage, default accounts, verbose errors. Fixed by hardened baselines and config checks. Not a zero-day, since nothing unknown is involved. Hook: the software is fine, the settings are not.*
    - @2.3.misconfig
20. A scan shows the same misconfiguration (directory listing on) recurring on new web servers every month. What is the BEST long-term fix?
    - **[x] A hardened template and automated configuration enforcement**  - [ ] Manually fixing each server after the scan  - [ ] Turning off the vulnerability scanner  - [ ] Asking developers to remember the setting
    - *Recurring misconfigurations point to a process gap; build the secure setting into the baseline image and enforce it with config management or IaC checks. Hook: fix the mould, not each brick.*
    - @2.3.misconfig
21. PBQ 2.3 - Vulnerability classifier. Match each finding to its category. ¶  1  ' OR 1=1 -- in a search box returns all records ¶  2  Comment field runs script in readers' browsers ¶  3  Two requests both pass a balance check before either debits ¶  4  BIOS flaw survives OS reinstall ¶  5  Server still allows TLS 1.0 and RC4
    - [p] Finding 1 :: A SQL injection · B XSS · C Race condition · D Firmware · E Cryptographic = a
    - [p] Finding 2 :: A SQL injection · B XSS · C Race condition · D Firmware · E Cryptographic = b
    - [p] Finding 3 :: A SQL injection · B XSS · C Race condition · D Firmware · E Cryptographic = c
    - [p] Finding 4 :: A SQL injection · B XSS · C Race condition · D Firmware · E Cryptographic = d
    - [p] Finding 5 :: A SQL injection · B XSS · C Race condition · D Firmware · E Cryptographic = e
    - *1: SQL syntax in input = SQLi. 2: script in a page others view = stored XSS. 3: check then use with a gap = race condition. 4: below the OS = firmware. 5: weak protocol and cipher = cryptographic. Hook: ask where the flaw lives - query, page, timing, chip, or maths.*
    - @2.3.app

- **2.3 part I: memory injection, buffer overflow, race conditions (TOC/TOU), malicious update, OS-based, web-based (SQLi, XSS), hardware (firmware, end-of-life, legacy), cryptographic, misconfiguration.**

## Test 8 - 2.3 Vulnerabilities II: Virtualization, Cloud, Mobile, Supply Chain, Zero-day (19 Q)

1. A researcher shows that code running in a guest VM can write to the hypervisor's memory and then control other tenants' VMs on the same host. What is this called?
   - **[x] VM escape**  - [ ] Resource reuse  - [ ] Side loading  - [ ] Memory injection into a browser
   - *VM escape = breaking out of a guest to reach the hypervisor or other guests; the worst virtualization flaw because isolation is the whole point. Patch the hypervisor promptly. Resource reuse leaks old data instead. Hook: the prisoner leaves the cell and walks into the warden's office.*
   - @2.3.virt
2. A new VM on a shared host reads leftover fragments of another customer's data from memory that was reassigned without being cleared. Which vulnerability is this?
   - **[x] Resource reuse**  - [ ] VM escape  - [ ] Race condition  - [ ] Jailbreaking
   - *Resource reuse = memory or storage given to a new VM without being wiped, leaking the previous user's data. The VM did not break out, it just inherited dirty memory. Hook: a hotel room that was never cleaned.*
   - @2.3.virt
3. An admin finds 60 forgotten test VMs on a hypervisor, unpatched and still on the production network. Which is the BEST response?
   - **[x] Inventory and decommission unused VMs, and patch the rest**  - [ ] Give each VM a public IP for remote patching  - [ ] Increase host RAM to run them faster  - [ ] Convert them all to containers immediately
   - *VM sprawl means unmanaged guests that nobody patches, each a foothold. Track them and remove what is not needed. Public IPs widen exposure. Hook: you cannot secure what you forgot you had.*
   - @2.3.virt
4. A developer turns on public access for an object store to host a demo page and forgets that invoices live in the same container. Which vulnerability category BEST fits?
   - **[x] Misconfiguration**  - [ ] Firmware flaw  - [ ] VM escape  - [ ] Legacy hardware
   - *Misconfiguration (here a cloud-specific one). Cloud-specific vulnerabilities centre on settings the customer controls: public buckets, over-broad IAM, exposed management APIs. Under shared responsibility, that bucket setting is the customer's job. Hook: in the cloud, a checkbox can be a breach.*
   - @2.3.cloud
5. A firm rents IaaS virtual machines. Which task falls to the firm rather than the provider?
   - **[x] Patching the guest OS and configuring IAM**  - [ ] Physical security of the data centre  - [ ] Patching the hypervisor  - [ ] Cooling and power in the facility
   - *IaaS: the provider runs facilities, hardware and hypervisor; the customer owns the OS, apps, data and identities. Hook: the landlord fixes the roof, you lock your flat.*
   - @2.3.cloud
6. An API key with full admin rights to a cloud account is found in a public code repository. What should be done FIRST?
   - **[x] Revoke and rotate the key, then review its recent activity**  - [ ] Delete the repository and assume no harm  - [ ] Make the repository private and keep the key  - [ ] Email developers a reminder about secrets
   - *Once public, assume the secret is compromised; bots scrape repos within minutes. Revoke first, then check logs for misuse. Making the repo private does not un-leak it. Hook: a leaked key is a spent key.*
   - @2.3.cloud
7. An employee installs an app on her company phone from a downloaded APK rather than the official store. Which term describes this, and the MAIN risk?
   - **[x] Side loading; the app skipped store vetting and may be malicious**  - [ ] Jailbreaking; the phone loses all encryption  - [ ] Rooting; it voids the warranty only  - [ ] Tethering; it uses mobile data
   - *Side loading = installing apps outside the official store. No vetting, so trojans slip in. MDM can block unknown sources. Jailbreaking is removing OS restrictions, a different act. Hook: food from a stall with no hygiene certificate.*
   - @2.3.mob
8. A user removes iOS restrictions to install custom themes. The MDM flags the device. Why is this a security concern?
   - **[x] Jailbreaking bypasses OS security controls, so apps can gain elevated access**  - [ ] It slows the phone's battery charging  - [ ] It changes the phone's IMEI number  - [ ] It permanently disables Wi-Fi
   - *Jailbreaking (iOS) and rooting (Android) give root access and break the sandbox and store protections that MDM relies on. Most MDMs then block corporate access. Hook: removing the guard rails also removes the protection.*
   - @2.3.mob
9. What is the BEST control to stop side loading and jailbroken devices accessing company email?
   - **[x] MDM policy with compliance checks that block non-compliant devices**  - [ ] A stronger Wi-Fi passphrase in the office  - [ ] Antivirus on the mail server only  - [ ] Disabling Bluetooth on all phones
   - *MDM enforces app source rules and jailbreak/root detection, then conditional access blocks failing devices. The Wi-Fi password and Bluetooth are unrelated. Hook: check the device before it gets the data.*
   - @2.3.mob
10. A network switch vendor ships units with a hidden debug account that a researcher later discloses. Which vulnerability category is this?
    - **[x] Supply chain - hardware provider**  - [ ] Supply chain - service provider  - [ ] Cloud-specific  - [ ] Race condition
    - *The flaw came built in from the hardware supplier. Service provider = an MSP or cloud provider; software provider = a library or app vendor. Hook: the threat was in the box.*
    - @2.3.supply
11. A widely used open-source logging library is found to have a remote code execution flaw, and it is bundled inside hundreds of commercial products. Which control BEST helps an organisation find where it is affected?
    - **[x] A software bill of materials (SBOM) for its applications**  - [ ] A clean desk policy  - [ ] Port security on switches  - [ ] Faraday cages in the server room
    - *Software provider supply chain risk: you inherit flaws in components you never chose directly. An SBOM lists the components so you can search for the vulnerable one. Hook: an ingredients label for software.*
    - @2.3.supply
12. A payroll SaaS provider suffers a breach that exposes all its customers' staff data. Which category BEST fits from the customer's view?
    - **[x] Supply chain - service provider**  - [ ] Supply chain - hardware provider  - [ ] Legacy hardware  - [ ] Jailbreaking
    - *A third party that runs a service for you is a service provider; its breach is your exposure. Mitigate with vendor assessments, contracts and right-to-audit. Hook: you outsourced the work, not the risk.*
    - @2.3.supply
13. Attackers break into firms through a remote-access gateway bug that had never been reported to the maker, so no fix exists. What is this?
    - **[x] Zero-day**  - [ ] End-of-life vulnerability  - [ ] Misconfiguration  - [ ] Resource reuse
    - *Zero-day = unknown to the vendor, so zero days to fix before exploitation. No signature or patch exists. EOL flaws are known but will not be fixed. Hook: the vendor learns about it from the attack.*
    - @2.3.zeroday
14. Which approach gives the BEST chance of detecting a zero-day exploit?
    - **[x] Behaviour-based detection and anomaly monitoring**  - [ ] Signature-based antivirus alone  - [ ] Waiting for the next patch cycle  - [ ] Changing all user passwords monthly
    - *No signature exists for a zero-day, so look for odd behaviour: unusual processes, outbound connections, privilege changes. Defence in depth and segmentation limit damage. Hook: you cannot match a fingerprint you have never seen, but you can spot odd behaviour.*
    - @2.3.zeroday
15. A vendor announces an actively exploited zero-day in your firewall and publishes a temporary workaround but no patch. What should you do FIRST?
    - **[x] Apply the workaround and increase monitoring until the patch ships**  - [ ] Ignore it until a patch is released  - [ ] Replace the firewall with a different vendor's that day  - [ ] Turn off the firewall to prevent exploitation
    - *Mitigations (disable the affected feature, restrict management access) reduce risk now; heavy monitoring catches exploitation. Turning off the firewall is worse than the flaw. Hook: tourniquet now, surgery later.*
    - @2.3.zeroday

16. A cloud tenant's serverless functions all share one IAM role with full access to every database. What weakness is this, and the BEST fix?
    - **[x] Over-permissive identity; give each function its own least-privilege role**  - [ ] VM escape; patch the hypervisor  - [ ] Side loading; enable MDM  - [ ] Legacy hardware; replace servers
    - *Cloud-specific flaws are often identity related. One compromised function now reaches everything. Scope roles per function. Hook: one key for every door means one theft opens all.*
    - @2.3.cloudiam
17. A company's laptop images are built by an outsourced imaging firm. Which control BEST reduces supply chain risk here?
    - **[x] Verify image integrity against a known-good hash and audit the provider**  - [ ] Trust the provider because it is certified  - [ ] Let staff reimage their own laptops from USB  - [ ] Disable all updates after imaging
    - *Supply chain controls: vet suppliers, verify what they deliver (hashes, signatures), keep the right to audit. Certification alone is not proof. Hook: trust, then verify.*
    - @2.3.supplyverify
18. A help-desk tech reports that a company tablet has a "system" app no one installed, and the OS reports it cannot verify the boot chain. Which is MOST likely?
    - **[x] The device has been rooted or jailbroken**  - [ ] The tablet's battery is failing  - [ ] A Wi-Fi channel conflict  - [ ] The user forgot their passcode
    - *A failed boot chain integrity check plus unexplained system apps point to a rooted/jailbroken device. Quarantine through MDM and reimage. Hook: if the phone cannot trust its own startup, neither should you.*
    - @2.3.rooted
19. PBQ 2.3 - Cloud and virtual findings. Match each finding to its vulnerability. ¶  1  Guest code reaches the hypervisor ¶  2  New VM reads previous tenant's data from memory ¶  3  App installed from an APK link ¶  4  Bug exploited before the vendor knows it exists ¶  5  Breach at the payroll SaaS company
    - [p] Finding 1 :: A VM escape · B Resource reuse · C Side loading · D Zero-day · E Supply chain (service provider) = a
    - [p] Finding 2 :: A VM escape · B Resource reuse · C Side loading · D Zero-day · E Supply chain (service provider) = b
    - [p] Finding 3 :: A VM escape · B Resource reuse · C Side loading · D Zero-day · E Supply chain (service provider) = c
    - [p] Finding 4 :: A VM escape · B Resource reuse · C Side loading · D Zero-day · E Supply chain (service provider) = d
    - [p] Finding 5 :: A VM escape · B Resource reuse · C Side loading · D Zero-day · E Supply chain (service provider) = e
    - *1: breaking out of the guest = VM escape. 2: uncleared reassigned memory = resource reuse. 3: outside the store = side loading. 4: unknown to vendor = zero-day. 5: third-party service breach = supply chain service provider. Hook: escape breaks out, reuse inherits.*
    - @2.3.misc

- **2.3 part II: virtualization (VM escape, resource reuse), cloud-specific, supply chain (service, hardware, software provider), mobile (side loading, jailbreaking), zero-day.**

## Test 9 - 2.4 Malware, Physical + Network Attacks (28 Q)

1. A hospital's file shares are encrypted overnight and a note demands payment for the key. What is the BEST preparation to recover WITHOUT paying?
   - **[x] Tested offline or immutable backups**  - [ ] A larger SIEM licence  - [ ] Stronger Wi-Fi encryption  - [ ] More firewall rules on the guest network
   - *Ransomware encrypts data for payment; the real defence is backups attackers cannot reach (offline, immutable) and that you have actually restored from. Paying does not guarantee a key. Hook: a backup you have never restored is a hope, not a backup.*
   - @2.4.ransom
2. A "free video downloader" really does download videos, but it also quietly lets an outsider control the PC. What is this?
   - **[x] Trojan (with a remote access capability)**  - [ ] Worm  - [ ] Logic bomb  - [ ] Bloatware
   - *Trojan = malware disguised as wanted software; the user installs it willingly. Adding remote control makes it a RAT. A worm spreads itself without user action. Hook: the wooden horse looked like a gift.*
   - @2.4.trojan
3. Malware spreads from one unpatched server to 400 others in an hour over SMB with no user clicking anything. What type is it, and the BEST containment?
   - **[x] Worm; isolate segments and block the exploited port while patching**  - [ ] Virus; tell users not to open attachments  - [ ] Spyware; clear browser caches  - [ ] Keylogger; change passwords only
   - *Worms self-propagate across networks by exploiting flaws. Contain with segmentation and blocking the service, then patch. A virus needs a host file and user action. Hook: worms crawl on their own.*
   - @2.4.worm
4. A virus differs from a worm MAINLY because a virus:
   - **[x] Needs a host file or user action to spread**  - [ ] Can only infect Linux systems  - [ ] Never damages files  - [ ] Always spreads by email only
   - *A virus attaches to a program or document and spreads when that is run or shared. A worm spreads itself. Hook: virus hitchhikes, worm walks.*
   - @2.4.worm
5. A new laptop from a retailer arrives with trial antivirus, three games and a "PC optimiser" the user never asked for. What is this, and what should IT do?
   - **[x] Bloatware; remove it and deploy a clean corporate image**  - [ ] A rootkit; replace the motherboard  - [ ] A logic bomb; wait for it to trigger  - [ ] Ransomware; restore from backup
   - *Bloatware = preinstalled unwanted software. Not usually malicious, but it uses resources and adds attack surface. Reimage with a standard build. Hook: junk that came in the box.*
   - @2.4.bloat
6. A coupon add-on for the browser logs each page a user opens and quietly uploads that list to a marketing broker. What type of malware is this?
   - **[x] Spyware**  - [ ] Worm  - [ ] Logic bomb  - [ ] Ransomware
   - *Spyware collects information about the user without consent: browsing, location, sometimes keystrokes. Ransomware demands payment. Hook: spy = watching you.*
   - @2.4.spyware
7. An attacker learns a manager's password even though it was never typed on a phishing page. A small device sits between the keyboard and the PC. What is it?
   - **[x] A hardware keylogger**  - [ ] A rootkit  - [ ] A worm  - [ ] An RFID cloner
   - *Keyloggers capture keystrokes, in software or as an inline hardware dongle. MFA limits the damage because a stolen password alone is not enough. Physical inspection finds hardware ones. Hook: the keyboard tells everything to a third listener.*
   - @2.4.keylog
8. A disgruntled admin plants a script that will delete payroll records if his account is ever disabled. What is this?
   - **[x] Logic bomb**  - [ ] Trojan  - [ ] Worm  - [ ] Spyware
   - *Logic bomb = code that waits for a trigger (date, event, account removal) then does damage. Often an insider. Code review and change control catch them. Hook: it sits quietly until the condition is met.*
   - @2.4.logicbomb
9. Antivirus shows a server as clean, yet traffic analysis shows it beaconing to 203.0.113.80. A boot-time offline scan finds hidden kernel drivers. Which malware is MOST likely?
   - **[x] Rootkit**  - [ ] Bloatware  - [ ] Keylogger only  - [ ] Adware
   - *Rootkits hide in the kernel or firmware and lie to the OS, so tools running on the infected OS see nothing. Scan offline or from trusted media, and usually rebuild. Hook: the liar controls the witness.*
   - @2.4.rootkit
10. Several staff open the same shared spreadsheet, and each time it is opened, malicious code copies itself into other documents on that user's PC and on the file share. Nothing spreads until someone opens an infected file. Which type of malware is this?
    - **[x] Virus**  - [ ] Worm  - [ ] Bloatware  - [ ] Logic bomb
    - *A virus attaches to a host file and spreads only when a user runs or opens it. A worm would spread over the network with no user action. Bloatware is unwanted preinstalled software. A logic bomb waits for a trigger and does not copy itself. Hook: virus hitchhikes, worm walks.*
    - @2.4.virus
11. A badge cloning device is found taped to the side of a lobby reader. Which attack does it support?
    - **[x] RFID cloning**  - [ ] Brute force against the door lock  - [ ] Environmental attack  - [ ] DNS poisoning
    - *RFID cloning copies a proximity badge's ID so a duplicate opens doors. Stronger cards with encryption and MFA at doors (badge plus PIN) mitigate. Hook: copy the key without touching the owner.*
    - @2.4.rfid
12. A thief smashes a side window on a branch office to get at the server closet. Which physical attack type is this?
    - **[x] Brute force**  - [ ] RFID cloning  - [ ] Environmental  - [ ] Tailgating via impersonation
    - *Physical brute force = forcing your way in: breaking doors, windows, locks. Mitigated by barriers, bollards, alarms, cameras. Hook: no trick, just force.*
    - @2.4.phys
13. Intruders sabotage a server room's air conditioning and the room's temperature climbs until the hardware trips its thermal shutdown. Which attack is this?
    - **[x] Environmental**  - [ ] Brute force against the servers  - [ ] Worm  - [ ] Logic bomb
    - *Environmental attacks target power, cooling, fire suppression or humidity to take systems down indirectly. Monitor environment and protect HVAC controls. Hook: attack the room, not the computer.*
    - @2.4.phys
14. A web service is flooded with traffic from 50,000 compromised IoT devices across the world. Which attack is this, and the BEST mitigation?
    - **[x] DDoS; an upstream DDoS mitigation or scrubbing service**  - [ ] DNS poisoning; flush the local cache  - [ ] On-path; enable HTTPS  - [ ] Replay; add timestamps
    - *Distributed denial of service uses many sources (a botnet), so blocking single IPs fails. Absorb it upstream with a CDN or scrubbing provider. Hook: you cannot outshout a stadium, so let someone bigger take the noise.*
    - @2.4.ddos
15. A victim at 192.0.2.10 is flooded by large DNS replies it never asked for. Captures show the queries came from many open resolvers, each sent a tiny request carrying 192.0.2.10 as the source. What is this?
    - **[x] Reflected, amplified DDoS**  - [ ] DNS cache poisoning  - [ ] Credential replay  - [ ] Wireless deauthentication
    - *Reflection: spoofing the victim's IP so third-party servers reply to it. Amplification: small request, big reply (DNS, NTP, memcached). Fix by closing open resolvers and source-address filtering. Hook: whisper a question, the victim gets the shout.*
    - @2.4.ddos
16. Users typing the bank's correct URL land on a fake site. The local resolver holds a forged record for the bank's domain. Which attack is this?
    - **[x] DNS poisoning**  - [ ] Typosquatting  - [ ] Watering hole  - [ ] Reflected DDoS
    - *DNS poisoning plants a false record so a correct name resolves to the attacker's IP. DNSSEC signs records so forgeries can be detected. Typosquatting relies on a wrong URL. Hook: right address, wrong map.*
    - @2.4.dns
17. A rogue access point with the same SSID as the office network appears in the car park, and users' laptops connect to it. What is this, and the BEST mitigation?
    - **[x] Evil twin; WPA3-Enterprise with server certificate validation and wireless monitoring**  - [ ] Bluejacking; disable Bluetooth  - [ ] Logic bomb; code review  - [ ] Amplified DDoS; rate limiting
    - *An evil twin imitates a legitimate SSID to capture traffic or credentials. 802.1X with certificate checks makes clients refuse the fake, and WIDS spots rogues. Hook: same name, different face.*
    - @2.4.wireless
18. Every laptop on a floor suddenly drops off Wi-Fi at once, repeatedly, and a capture shows many 802.11 deauthentication frames. What is happening?
    - **[x] A deauthentication attack**  - [ ] DNS poisoning  - [ ] An RFID cloning attack  - [ ] A worm outbreak
    - *Forged deauth frames knock clients off, often to push them to an evil twin or capture handshakes. 802.11w (protected management frames, required in WPA3) mitigates. Hook: someone keeps hanging up your call.*
    - @2.4.wireless
19. An attacker on the same LAN sends forged ARP replies so that traffic to the gateway passes through his laptop. What type of attack is this?
    - **[x] On-path (ARP poisoning)**  - [ ] Amplified DDoS  - [ ] Logic bomb  - [ ] Directory traversal
    - *On-path = the attacker sits between two parties, reading or changing traffic. ARP poisoning is a LAN way to get there. Dynamic ARP inspection and encryption mitigate. Hook: the postman reads your letters.*
    - @2.4.onpath
20. An attacker captures an NTLM hash from the network and uses it to authenticate to a file server without ever cracking it. What is this?
    - **[x] Credential replay (pass the hash)**  - [ ] Password spraying  - [ ] Birthday attack  - [ ] Brute force against the hash
    - *Credential replay reuses captured authentication data as-is. Pass the hash needs no plaintext. Mitigate with Kerberos, disabling NTLM, and limiting admin logins. Hook: you do not need to read the ticket to use it.*
    - @2.4.replay
21. A legitimate web page on a partner's site starts injecting a script that redirects visitors to an exploit kit. Which network attack type on the objectives does this BEST fit?
    - **[x] Malicious code**  - [ ] DNS poisoning  - [ ] On-path  - [ ] Wireless deauthentication
    - *Malicious code covers scripts, macros and executables used to deliver attacks across the network (for example a hijacked web script). DNS was not changed and there is no interception. Hook: the page itself carries the poison.*
    - @2.4.net
22. During an incident, many workstations show the same scheduled task named "UpdateSvc" running a base64 PowerShell command. What should the analyst do FIRST?
    - **[x] Isolate the affected hosts, then collect the script and IoCs**  - [ ] Reboot every workstation immediately  - [ ] Delete the task and close the ticket  - [ ] Email all staff the script for awareness
    - *Contain first to stop spread, preserve evidence for analysis, then hunt using the IoCs. Rebooting loses memory evidence, especially for fileless malware. Hook: stop the bleeding, then study the wound.*
    - @2.4.mal
23. A user reports a pop-up saying "Your files are locked - send 0.5 BTC" but their files open normally. Which is the MOST likely situation?
    - **[x] A ransomware bluff with no encryption yet, which still needs investigating**  - [ ] Confirmed worm infection  - [ ] A hardware keylogger  - [ ] A logic bomb that already deleted data
    - *Some campaigns bluff to scare victims into paying. Still check for real compromise, but encrypted files are the giveaway of true ransomware. Hook: test the lock before paying for the key.*
    - @2.4.ransom
24. Which network attack does a DNS sinkhole or DNSSEC MOST directly help against?
    - **[x] DNS-based attacks, such as poisoning or malware callbacks to known bad domains**  - [ ] RFID cloning at the front door  - [ ] Physical brute force on a cabinet  - [ ] Environmental attacks on HVAC
    - *DNSSEC validates records; a sinkhole redirects lookups for known malicious domains to a safe address, breaking callbacks. Physical attacks are untouched. Hook: control the phone book.*
    - @2.4.dns
25. PBQ 2.4 - Malware identification. Match each behaviour to the malware type. ¶  1  Spreads across SMB with no user action ¶  2  Hides kernel drivers from the OS ¶  3  Deletes data when an account is disabled ¶  4  Free app that also gives remote control ¶  5  Records keystrokes to steal passwords
    - [p] Behaviour 1 :: A Worm · B Rootkit · C Logic bomb · D Trojan · E Keylogger = a
    - [p] Behaviour 2 :: A Worm · B Rootkit · C Logic bomb · D Trojan · E Keylogger = b
    - [p] Behaviour 3 :: A Worm · B Rootkit · C Logic bomb · D Trojan · E Keylogger = c
    - [p] Behaviour 4 :: A Worm · B Rootkit · C Logic bomb · D Trojan · E Keylogger = d
    - [p] Behaviour 5 :: A Worm · B Rootkit · C Logic bomb · D Trojan · E Keylogger = e
    - *Self-spreading = worm. Hiding below the OS = rootkit. Trigger condition = logic bomb. Disguised as wanted software = trojan. Captures keys = keylogger. Hook: spread, hide, wait, disguise, record.*
    - @2.4.mal
26. PBQ 2.4 - Network attack identification. Match each capture to the attack. ¶  1  Thousands of sources flood one web server ¶  2  Resolver returns a forged IP for the correct domain ¶  3  Fake AP with the corporate SSID ¶  4  Forged ARP replies redirect gateway traffic ¶  5  Captured hash reused to log in
    - [p] Capture 1 :: A DDoS · B DNS poisoning · C Evil twin · D On-path · E Credential replay = a
    - [p] Capture 2 :: A DDoS · B DNS poisoning · C Evil twin · D On-path · E Credential replay = b
    - [p] Capture 3 :: A DDoS · B DNS poisoning · C Evil twin · D On-path · E Credential replay = c
    - [p] Capture 4 :: A DDoS · B DNS poisoning · C Evil twin · D On-path · E Credential replay = d
    - [p] Capture 5 :: A DDoS · B DNS poisoning · C Evil twin · D On-path · E Credential replay = e
    - *Many sources = DDoS. Right name, wrong IP = DNS poisoning. Copied SSID = evil twin. ARP tricks = on-path. Reused credential material = replay. Hook: volume, map, mask, middle, reuse.*
    - @2.4.net
27. Wireless clients in one wing lose connectivity whenever a van parks outside. A spectrum analyser shows strong noise across the 2.4 GHz band and no management frames from the source. Which attack is this?
    - **[x] Wireless jamming, a denial of service**  - [ ] Deauthentication attack  - [ ] Evil twin  - [ ] Bluesnarfing
    - *Jamming floods the radio band with noise so nothing can be heard: pure DoS at the RF level. Deauthentication sends forged 802.11 frames instead, and an evil twin offers a fake AP. Find the source with physical searches and spectrum analysis. Hook: shouting over everyone, not tricking anyone.*
    - @2.4.wireless
28. Visitors to a retailer's site reach an attacker's server. The DNS records were changed through the company's registrar account after its password was phished, and no resolver caches were touched. Which attack is this?
    - **[x] Domain hijacking**  - [ ] DNS poisoning  - [ ] Typosquatting  - [ ] Evil twin
    - *Domain hijacking = taking control of the domain registration itself, then pointing its records anywhere. DNS poisoning corrupts a resolver's cache instead; typosquatting uses a look-alike name. Defend with registrar MFA and registry lock. Hook: they stole the deed, not the street sign.*
    - @2.4.dns

- **Malware: ransomware, trojan, worm, spyware, bloatware, virus, keylogger, logic bomb, rootkit. Physical: brute force, RFID cloning, environmental. Network: DDoS (amplified, reflected), DNS, wireless, on-path, credential replay, malicious code.**

## Test 10 - 2.4 + 2.5 App, Crypto + Password Attacks, Indicators, Mitigation, Hardening (26 Q)

1. A network tool's web form takes a hostname to ping. Entering 192.0.2.5; cat /etc/passwd returns the password file. Which attack is this, and the BEST fix?
   - **[x] Command injection; validate input and avoid passing it to a shell**  - [ ] XSS; add output encoding  - [ ] Replay; add timestamps  - [ ] Downgrade; disable TLS 1.0
   - *Injection attacks feed code into an interpreter: SQL, OS command, LDAP. The semicolon chains a second command. Use allow-list validation and APIs that do not invoke a shell. Hook: the app ran your sentence and then theirs.*
   - @2.4.inject
2. A standard user exploits a misconfigured service running as SYSTEM to add himself to the local Administrators group. What is this?
   - **[x] Privilege escalation (vertical)**  - [ ] Horizontal movement only  - [ ] Directory traversal  - [ ] Credential replay
   - *Vertical privilege escalation = gaining higher rights than granted. Horizontal is reaching another user's data at the same level. Least privilege for services and patching mitigate. Hook: climbing the ladder, not walking the corridor.*
   - @2.4.privesc
3. An IDS alert shows a request to a legacy service with a 4,000-character string of 0x90 bytes followed by shellcode, and the service crashed seconds later. Which application attack does this indicate?
   - **[x] Buffer overflow**  - [ ] Directory traversal  - [ ] Cross-site request forgery  - [ ] Password spraying
   - *A long run of NOP (0x90) bytes, a NOP sled, followed by shellcode and a crash is the classic sign of a buffer overflow attempt: input larger than the buffer overwrites memory to redirect execution. Traversal shows ../, CSRF is a forged browser request, spraying is login attempts. Hook: overfill the glass and steer where it spills.*
   - @2.4.overflow
4. A WAF flags a request to an image handler with img=..%2f..%2f..%2fwindows%2fwin.ini. Which attack is being attempted?
   - **[x] Directory traversal**  - [ ] SQL injection  - [ ] Server-side request forgery  - [ ] Birthday attack
   - *Directory (path) traversal uses ../ (here URL-encoded as ..%2f) to climb out of the web root and read other files. Fix with canonical path checks and an allow list of files. Hook: dot-dot-slash walks up the stairs.*
   - @2.4.traversal
5. While still signed in to her payroll portal, an employee opens a forum post with a hidden auto-submitting form that changes her direct-deposit account. The portal accepts it because her cookie rides along. Which attack is this, and the BEST fix?
   - **[x] Cross-site request forgery; anti-CSRF tokens and SameSite cookies**  - [ ] Stored XSS; output encoding only  - [ ] SQL injection; prepared statements  - [ ] Directory traversal; path checks
   - *CSRF tricks the browser into sending an authenticated request the user did not intend. A unique token per form that the attacker cannot guess breaks it. Hook: forging her signature on a cheque she is already holding.*
   - @2.4.forgery
6. An attacker makes a cloud web app fetch http://169.254.169.254/ and returns the instance's temporary credentials. Which attack is this?
   - **[x] Server-side request forgery (SSRF)**  - [ ] Cross-site request forgery (CSRF)  - [ ] Replay attack  - [ ] DNS poisoning
   - *SSRF makes the server send requests on the attacker's behalf, often to internal-only addresses like the cloud metadata service. CSRF abuses the user's browser instead. Hook: client-side forgery tricks the browser, server-side tricks the server.*
   - @2.4.forgery
7. An attacker records a valid "unlock" message sent from a car fob and plays it back later to open the car. Which control BEST defeats this?
   - **[x] Rolling codes or nonces and timestamps so each message is valid once**  - [ ] Longer passwords on the owner's account  - [ ] Output encoding in the app  - [ ] Disabling the car's radio entirely
   - *A replay attack resends captured valid data. One-time values (nonces, rolling codes, session tokens with expiry) make old messages worthless. Hook: yesterday's ticket should not get you in today.*
   - @2.4.replay
8. An on-path attacker strips the TLS 1.3 options from a client's hello so the session falls back to an old, weak version. What is this?
   - **[x] Downgrade attack**  - [ ] Collision attack  - [ ] Birthday attack  - [ ] Password spraying
   - *Downgrade = forcing weaker protocols or ciphers that are easier to break (for example SSL stripping to HTTP). Disable legacy versions and use HSTS. Hook: talk them into the old lock.*
   - @2.4.crypt
9. An attacker creates two different contracts that produce the same MD5 hash, then gets one signed and swaps in the other. Which attack is this, and which concept explains why it is feasible?
   - **[x] Collision attack, made easier by the birthday paradox**  - [ ] Downgrade attack, made easier by TLS 1.0  - [ ] Replay attack, made easier by missing nonces  - [ ] Brute force, made easier by short passwords
   - *A collision is two inputs with the same hash. The birthday paradox means collisions appear far sooner than the hash size suggests (about 2^(n/2) tries). Use SHA-256 or better. Hook: in a room of 23 people, two probably share a birthday.*
   - @2.4.crypt
10. Logs show one login attempt each for 3,000 accounts using "Spring2025!", then a pause, then "Summer2025!". No account locks out. Which attack is this?
   - **[x] Password spraying**  - [ ] Brute force against one account  - [ ] Credential replay  - [ ] Rainbow table attack
   - *Spraying tries a few common passwords across many accounts, staying under lockout thresholds. Detect by many-account failures from one source; stop with MFA and banned-password lists. Hook: a little on everyone, not a lot on one.*
   - @2.4.pw
11. A stolen database of salted bcrypt hashes is attacked offline with a GPU trying every combination up to 8 characters. Which attack type, and why does bcrypt help?
    - **[x] Offline brute force; bcrypt is deliberately slow, so each guess costs more**  - [ ] Spraying; bcrypt locks the accounts  - [ ] Replay; bcrypt adds timestamps  - [ ] Downgrade; bcrypt forces TLS 1.3
    - *Offline brute force is not limited by lockouts, only by compute. Slow salted hashes make each guess expensive and defeat precomputed tables. Hook: make every guess cost a coin.*
    - @2.4.pw
12. A user's account logs in from London at 09:00 and from Singapore at 09:20 the same morning. Which indicator is this?
    - **[x] Impossible travel**  - [ ] Account lockout  - [ ] Resource consumption  - [ ] Out-of-cycle logging
    - *No one flies that fast, so one of the logins is probably an attacker with stolen credentials (or a VPN, which needs checking). Hook: physics says no.*
    - @2.4.ioc
13. A SaaS admin sees the same account with three active sessions at once from different browsers and countries. Which indicator is this, and what is the BEST first action?
    - **[x] Concurrent session usage; revoke sessions and reset the credentials**  - [ ] Blocked content; add the sites to the allow list  - [ ] Resource inaccessibility; reboot the server  - [ ] Published documentation; ignore it
    - *Concurrent sessions from unusual places suggest credential or token theft. Kill all sessions, reset, enforce MFA. Hook: one person, three places = more than one person.*
    - @2.4.ioc
14. A server's security log was empty for 02:00-03:00, and the log service shows a restart at 03:01 by an account no one recognises. Which indicator does this MOST suggest?
    - **[x] Missing logs, a sign an attacker tried to cover tracks**  - [ ] Blocked content, a normal web filter action  - [ ] Account lockout from a forgotten password  - [ ] Impossible travel from a VPN user
    - *Gaps or wiped logs are a classic IoC; attackers clear logs to hide. Forward logs to a SIEM in real time so local tampering does not erase them. Hook: the silence is the clue.*
    - @2.4.ioc2
15. At 03:00 on a Sunday a file server logs a burst of thousands of audit entries, far outside any backup or scheduled job. Which indicator is this?
    - **[x] Out-of-cycle logging**  - [ ] Missing logs  - [ ] Published or documented  - [ ] Concurrent session usage
    - *Out-of-cycle logging = log activity at unexpected times or volumes, unlike normal patterns. Missing logs is the opposite. Hook: noise when it should be quiet.*
    - @2.4.ioc2
16. A database server's CPU sits at 100% and outbound traffic triples overnight, while the users' app becomes unreachable. Which TWO indicators are shown?
    - **[x] Resource consumption and resource inaccessibility**  - [ ] Account lockout and impossible travel  - [ ] Blocked content and published/documented  - [ ] Missing logs and concurrent sessions
    - *High CPU, disk or bandwidth use suggests cryptomining, exfiltration or DDoS; services or files becoming unavailable (including ransomware) are resource inaccessibility. Hook: busy and broken at the same time.*
    - @2.4.ioc2
17. PBQ 2.4 - Indicators of compromise. Match each observation to the indicator. ¶  1  Many staff report "account locked" on Monday morning ¶  2  Web proxy repeatedly stops a host reaching a known C2 domain ¶  3  Your customer list appears on a leak forum ¶  4  London then Sydney logins 30 minutes apart ¶  5  Log server shows a gap after an admin login
    - [p] Observation 1 :: A Account lockout · B Blocked content · C Published/documented · D Impossible travel · E Missing logs = a
    - [p] Observation 2 :: A Account lockout · B Blocked content · C Published/documented · D Impossible travel · E Missing logs = b
    - [p] Observation 3 :: A Account lockout · B Blocked content · C Published/documented · D Impossible travel · E Missing logs = c
    - [p] Observation 4 :: A Account lockout · B Blocked content · C Published/documented · D Impossible travel · E Missing logs = d
    - [p] Observation 5 :: A Account lockout · B Blocked content · C Published/documented · D Impossible travel · E Missing logs = e
    - *Mass lockouts can mean brute force. Repeated blocks to a bad domain = something on the host is trying to call home. Data seen publicly = published/documented. Impossible geography = impossible travel. Gaps = missing logs. Hook: each one is a symptom, not proof, so investigate.*
    - @2.4.ioc
18. After a breach that spread from a guest Wi-Fi laptop to the HR database, what mitigation would MOST limit similar lateral movement?
    - **[x] Segmentation, with firewall rules between guest, user and server zones**  - [ ] Longer guest Wi-Fi passwords  - [ ] More frequent antivirus signature updates  - [ ] A new login banner on the HR app
    - *Segmentation splits the network so a compromise in one zone cannot freely reach another; ACLs between zones enforce it. Hook: bulkheads in a ship stop one leak sinking it.*
    - @2.5.mit
19. A kiosk PC in a hotel lobby only ever needs a browser, yet staff keep finding games installed. What is the BEST mitigation?
    - **[x] Application allow list permitting only the approved browser**  - [ ] A block list of known game names  - [ ] Weekly manual cleanup  - [ ] Full-disk encryption on the kiosk
    - *An allow list denies everything not explicitly approved, which suits single-purpose systems. Block lists always lag behind. FDE protects data at rest, not what runs. Hook: guest list at the door, not a list of banned people.*
    - @2.5.allowlist
20. EDR flags a laptop connecting to known ransomware infrastructure. What is the BEST immediate mitigation?
    - **[x] Isolate the host from the network while keeping it powered for forensics**  - [ ] Power it off and reimage at once  - [ ] Ignore it until the user complains  - [ ] Give the user admin rights to clean it
    - *Isolation (network quarantine) contains spread and preserves memory evidence. Powering off loses volatile data. Hook: quarantine the patient, do not cremate them.*
    - @2.5.isolate
21. A new marketing intern is given the same file share rights as the marketing director "to save time". Which principle is violated, and what control fixes it?
    - **[x] Least privilege; role-based permissions and ACLs scoped to the job**  - [ ] Defence in depth; a second firewall  - [ ] Non-repudiation; digital signatures  - [ ] Availability; RAID storage
    - *Least privilege = only the access needed for the job. Access control lists and permissions implement it. Extra firewalls do not narrow file rights. Hook: give the intern a key to their own office, not the master key.*
    - @2.5.leastpriv
22. An audit finds an old FTP server still powered on in a rack, with live DNS and a public IP, though its service was moved to SFTP last year. What is the BEST action?
    - **[x] Decommission it: wipe, remove DNS and IP, and update the asset inventory**  - [ ] Leave it running as a backup  - [ ] Move it to port 2121  - [ ] Add it to the guest VLAN
    - *Decommissioning removes systems that are no longer needed so they cannot be forgotten and exploited. Configuration enforcement keeps the remaining estate on its baseline. Hook: switched off and forgotten is fine; switched on and forgotten is a breach.*
    - @2.5.mit
23. A hardening checklist for a new Linux web server is being written. Which set BEST reflects standard hardening techniques?
    - **[x] Change default passwords, disable unused ports and services, remove unneeded software, install HIPS/endpoint protection**  - [ ] Enable all services in case they are needed, keep defaults for support  - [ ] Allow root SSH with a password, disable logging to save disk  - [ ] Install every available package, turn off the host firewall
    - *Hardening shrinks the attack surface: fewer services, ports and packages, no defaults, plus host protection (HIDS/HIPS, EDR, host firewall) and encryption. The others expand it. Hook: lock it, strip it, watch it.*
    - @2.5.hard
24. A laptop's EDR is healthy, but an attacker on the same hotel network reaches its SMB and RDP services directly. Which hardening technique on the endpoint itself would BEST block these inbound connections?
    - **[x] A host-based firewall that denies unsolicited inbound traffic**  - [ ] A longer screen-lock timeout  - [ ] Full-disk encryption  - [ ] Removing bloatware
    - *A host-based firewall filters traffic at the endpoint, so it protects the device even on untrusted networks with no perimeter firewall. FDE protects data at rest, not open services. Hook: carry your own wall.*
    - @2.5.hostfw
25. PBQ 2.5 - Pick the BEST mitigation for each finding. ¶  1  Critical vendor fix for a web server flaw is available ¶  2  Laptops store customer data unencrypted ¶  3  No alerts exist for admin logins at night ¶  4  Servers drift from the hardened baseline over time ¶  5  Telnet enabled on all switches
    - [p] Finding 1 :: A Patching · B Encryption · C Monitoring · D Configuration enforcement · E Disabling ports/protocols = a
    - [p] Finding 2 :: A Patching · B Encryption · C Monitoring · D Configuration enforcement · E Disabling ports/protocols = b
    - [p] Finding 3 :: A Patching · B Encryption · C Monitoring · D Configuration enforcement · E Disabling ports/protocols = c
    - [p] Finding 4 :: A Patching · B Encryption · C Monitoring · D Configuration enforcement · E Disabling ports/protocols = d
    - [p] Finding 5 :: A Patching · B Encryption · C Monitoring · D Configuration enforcement · E Disabling ports/protocols = e
    - *A vendor fix = patch. Data at rest = encryption (FDE). No alerting = monitoring. Drift = configuration enforcement (automated baselines). Telnet sends cleartext, so disable it and use SSH. Hook: fix, scramble, watch, enforce, close.*
    - @2.5.hard
26. Forensics shows a legitimate Windows service was made to load an attacker's library file at runtime, so the malicious code ran inside the trusted process. Which attack is this?
    - **[x] DLL injection**  - [ ] Directory traversal  - [ ] Cross-site request forgery  - [ ] Downgrade attack
    - *DLL injection forces a running process to load a malicious dynamic link library, a form of memory injection that hides behind a trusted process name. Defend with application allow lists, EDR and least privilege. Hook: a stowaway library in a trusted ship.*
    - @2.4.inject

- **App attacks: injection, buffer overflow, replay, privilege escalation, forgery (CSRF, SSRF), directory traversal. Crypto: downgrade, collision, birthday. Password: spraying, brute force. IoCs: account lockout, concurrent sessions, blocked content, impossible travel, resource consumption, resource inaccessibility, out-of-cycle logging, published/documented, missing logs. Mitigation: segmentation, ACLs/permissions, allow list, isolation, patching, encryption, monitoring, least privilege, configuration enforcement, decommissioning, hardening.**

## Test 11 - 3.1 Architecture Models I: Cloud + Network Infrastructure (20 Q)

1. A startup moves its customer portal to an IaaS provider. After a breach, investigators find the guest OS on the VMs had not been patched for a year. Who was responsible for that patching?
   - **[x] The customer, because IaaS hands over everything from the OS upward**  - [ ] The provider, because it owns the hypervisor and hardware  - [ ] Shared equally, as set out in every IaaS contract by default  - [ ] The provider, because the portal runs inside its data centre
   - *Responsibility matrix: in IaaS the provider secures physical, network and hypervisor; the customer owns guest OS, apps and data. Hook: IaaS = you get the empty flat, you buy the locks. Hypervisor ownership does not extend to the guest OS. "Shared equally" is never the default split. Location does not move duty.*
   - @3.1.resp
2. A team is choosing between IaaS, PaaS and SaaS for a new HR tool and wants the provider to carry the MOST security responsibility. Which should they choose?
   - **[x] SaaS**  - [ ] PaaS  - [ ] IaaS  - [ ] On-premises
   - *SaaS: the provider runs the whole stack; the customer still owns its data, users and access settings. PaaS leaves the code to you; IaaS leaves OS upward; on-premises leaves everything. Analogy: SaaS is a hotel room, IaaS is a bare rented flat.*
   - @3.1.resp
3. A bank keeps its core ledger in its own data centre but bursts its customer analytics into a public cloud during month-end. Which model is this, and what is its MAIN security challenge?
   - **[x] Hybrid cloud; keeping policies and identity consistent across both environments**  - [ ] Community cloud; agreeing costs with other member banks  - [ ] Private cloud; losing physical control of the ledger hardware  - [ ] Multi-tenant SaaS; the provider patching the ledger application
   - *Hybrid = on-premises or private plus public, connected. The hard part is consistent configuration, IAM and monitoring across both. Community cloud is shared by organisations with common needs. Private cloud keeps hardware under the bank's control. Nothing here is SaaS.*
   - @3.1.hybrid
4. A retailer's cloud app relies on a third-party payment gateway and an external email-sending service. What should the security team do FIRST to manage the risk these introduce?
   - **[x] Assess each vendor's security posture and set contractual security requirements**  - [ ] Move both services in-house before the next release  - [ ] Block the vendors' IP ranges at the perimeter firewall  - [ ] Encrypt the app's database with a customer-managed key
   - *Third-party vendors in the cloud stack extend your attack surface; you manage that with due diligence, contracts and right-to-audit. In-sourcing is costly and rarely first. Blocking breaks the service. Database encryption does not address the vendors at all.*
   - @3.1.vendor
5. An ops lead finds that the staging and production cloud networks have drifted apart after months of console clicks. Which approach BEST prevents this happening again?
   - **[x] Infrastructure as code with templates kept in version control**  - [ ] A monthly manual comparison of both consoles  - [ ] Moving staging onto on-premises servers  - [ ] Giving only one admin console access
   - *IaC defines infrastructure in files, so every deploy is repeatable and changes are reviewed in git. Hook: a recipe, not a memory. Manual comparison detects drift late. Moving staging adds a new difference. One admin still clicks by hand.*
   - @3.1.iac
6. A shared Terraform module that every product team reuses turns out to allow SSH from any internet address. Why is this worse than the same mistake on a single hand-built server?
   - **[x] The template repeats the flaw everywhere it is deployed**  - [ ] IaC templates cannot be changed once applied  - [ ] SSH is only dangerous when defined in code  - [ ] Templates bypass the provider's firewall
   - *IaC brings consistency, which cuts both ways: a bad template is a bad clone factory. Scan templates before deployment. Templates can be edited and re-applied; SSH risk is the same whatever creates it; templates use the provider's firewall rules, they do not bypass them.*
   - @3.1.iac
7. A media firm runs image-resizing as cloud functions that start on upload and stop seconds later. What security work does the firm STILL own?
   - **[x] Its function code, permissions and the data passed in**  - [ ] Patching the OS of the servers running the functions  - [ ] Hardening the hypervisor under the function runtime  - [ ] Physical access control at the provider's site
   - *Serverless: the provider manages servers and runtime; you own code, IAM roles and data. Hook: no servers to patch, but still code to secure. The other three are the provider's side of the serverless line.*
   - @3.1.svless
8. A travel site splits its monolith into small services for search, booking and payments, each with its own API. Which is a security BENEFIT of this design?
   - **[x] A compromise of one service can be contained without taking down the rest**  - [ ] There are fewer network connections to monitor  - [ ] Authentication between components is no longer needed  - [ ] All services share one database, simplifying access control
   - *Microservices isolate failures and let you scale and patch each piece. The trade-off is more APIs and service-to-service traffic, so more to secure, and each call still needs authentication. Shared databases undo the isolation.*
   - @3.1.micro
9. A water utility keeps the control network for its pumps on switches with no cable or wireless link to the office LAN. Updates come in on a scanned USB drive. What is this design called?
   - **[x] Air-gapped (physical isolation)**  - [ ] VLAN segmentation  - [ ] Screened subnet  - [ ] Software-defined networking
   - *Air gap = no physical connection at all. Data crosses by removable media, which is why removable media is the main risk (Stuxnet). VLANs share hardware, so logical. A screened subnet is a DMZ. SDN is about programmable control.*
   - @3.1.airgap
10. A hospital wants guest Wi-Fi users, medical devices and staff laptops on the same physical switches but unable to reach each other except through a firewall. What is the BEST fit?
    - **[x] Separate VLANs per group with inter-VLAN routing through the firewall**  - [ ] An air gap between each group  - [ ] One flat network with strong passwords  - [ ] A separate internet line for every department
    - *Logical segmentation: VLANs split one switch into separate broadcast domains; a firewall controls what crosses. Air gap means separate hardware, which the brief rules out. Flat networks let threats move sideways. Extra lines are cost without segmentation.*
    - @3.1.seg
11. A provider wants to change routing and access rules across hundreds of switches from one central program instead of logging into each device. Which architecture enables this?
    - **[x] Software-defined networking, separating the control plane from the data plane**  - [ ] Air-gapped management network  - [ ] Infrastructure as a service  - [ ] Port security with 802.1X
    - *SDN moves the decisions (control plane) into a central controller that programs the forwarding (data plane). Hook: one brain, many hands. The controller becomes a high-value target, so protect it. 802.1X is port authentication, IaaS is a cloud model.*
    - @3.1.sdn
12. A defence contractor must prove it physically controls the servers holding classified designs. Which deployment BEST suits this?
    - **[x] On-premises, in its own secured data centre**  - [ ] Public cloud SaaS in the same country  - [ ] Serverless functions with encrypted inputs  - [ ] A hybrid model with burst to public cloud
    - *On-premises gives full control of hardware, access and staff, at the cost of doing all the security, power and patching yourself. Every cloud option places hardware under the provider's control.*
    - @3.1.onprem
13. A retailer runs one data centre that hosts every service for 300 stores. Which risk is MOST associated with this centralised design?
    - **[x] A single point of failure that can stop every store at once**  - [ ] Inconsistent security policy between stores  - [ ] Too many sites to monitor  - [ ] Data scattered across many jurisdictions
    - *Centralised: easier to manage and monitor, but one outage or breach hits everything. Decentralised spreads risk but makes consistent policy and visibility harder, which is what the other three describe.*
    - @3.1.central
14. A company moves its apps into containers. Which statement about container isolation is MOST accurate?
    - **[x] Containers share the host OS kernel, so a kernel flaw can affect them all**  - [ ] Each container runs its own full OS kernel  - [ ] Containers are isolated by separate physical hardware  - [ ] Containers cannot reach the network unless air-gapped
    - *Containers package app plus dependencies but share the host kernel; VMs each carry a full guest OS on a hypervisor. That makes containers lighter but weaker at isolation. Hook: flats in one building share the foundations.*
    - @3.1.cont
15. A pen tester breaks out of a guest VM and runs code on the hypervisor, reaching other tenants' VMs. What is this attack?
    - **[x] VM escape**  - [ ] VM sprawl  - [ ] Resource reuse  - [ ] Container drift
    - *VM escape = guest to hypervisor, the worst virtualization failure. VM sprawl is unmanaged, forgotten VMs. Resource reuse is leftover data in reallocated memory or disk. Container drift is not the term here.*
    - @3.1.virt
16. An audit finds 60 test VMs nobody owns, many unpatched and still on the production network. What is the BEST control?
    - **[x] A VM provisioning and decommissioning process tied to the asset inventory**  - [ ] Moving the VMs into containers  - [ ] Air-gapping the hypervisor host  - [ ] Doubling the host's RAM
    - *That is VM sprawl. Fix it with lifecycle management: owners, inventory, expiry dates. Containerising spreads the same mess. Air-gapping production is impractical. RAM solves nothing.*
    - @3.1.virt
17. PBQ 3.1 - Pick the model. A logistics firm is placing workloads. Choose the BEST architecture for each. ¶  1  Short-lived code that runs when a parcel is scanned ¶  2  Packaging the tracking app with its libraries to run the same on any host ¶  3  Repeatable build of 12 identical regional networks ¶  4  Payroll the firm wants fully managed by a vendor ¶  5  Turbine controller network that must have no connection to anything
    - [p] Workload 1 :: A Serverless · B Containerization · C Infrastructure as code · D SaaS · E Air-gapped = a
    - [p] Workload 2 :: A Serverless · B Containerization · C Infrastructure as code · D SaaS · E Air-gapped = b
    - [p] Workload 3 :: A Serverless · B Containerization · C Infrastructure as code · D SaaS · E Air-gapped = c
    - [p] Workload 4 :: A Serverless · B Containerization · C Infrastructure as code · D SaaS · E Air-gapped = d
    - [p] Workload 5 :: A Serverless · B Containerization · C Infrastructure as code · D SaaS · E Air-gapped = e
    - *1: event-driven, no server to run = serverless. 2: app plus dependencies, portable = container. 3: identical repeatable builds = IaC. 4: vendor runs it all = SaaS. 5: no links at all = air gap. Hook: event, package, recipe, rental, island.*
    - @3.1.models
18. An architect says moving a workload to a public cloud "removes our responsibility for the data." What is the BEST response?
    - **[x] The organisation stays accountable for its data in every cloud model**  - [ ] Correct, once a SaaS contract is signed  - [ ] Correct, if the provider holds ISO 27001  - [ ] Correct, only for data encrypted at rest
    - *Responsibility for tasks can shift; accountability for the data never does. Certifications and contracts help but do not transfer ownership of the data or of breach duties.*
    - @3.1.hybrid
19. A team running a hybrid environment wants one set of user identities that works on-premises and in the cloud. Which approach BEST supports this?
    - **[x] Federated identity or directory sync between on-premises and cloud**  - [ ] Separate local accounts created in each environment  - [ ] A shared admin password used in both  - [ ] Air-gapping the cloud tenant
    - *Hybrid works best with one identity source, synced or federated, so joiners and leavers are handled once. Duplicate accounts drift and get orphaned. Shared passwords break accountability. An air-gapped cloud is a contradiction.*
    - @3.1.hybrid
20. A security lead must explain why the company's new microservices platform needs more API security work than the old monolith. Which reason is MOST accurate?
    - **[x] Internal calls now cross the network as APIs, adding endpoints to protect**  - [ ] Microservices cannot use TLS between services  - [ ] Each microservice must run on its own physical server  - [ ] Microservices store all data in plaintext by design
    - *Splitting a monolith turns in-process function calls into network API calls, so the attack surface grows. TLS works fine between services (often mutual TLS). No physical server or plaintext requirement exists.*
    - @3.1.micro

## Test 12 - 3.1 Architecture Models II: Embedded, ICS/SCADA, IoT, Considerations (21 Q)

1. A smart-building firm deploys 4,000 networked thermostats with default passwords and no update mechanism. What is the BEST first mitigation?
   - **[x] Put the devices on an isolated network segment and change default credentials**  - [ ] Install endpoint antivirus on each thermostat  - [ ] Replace them with on-premises servers  - [ ] Turn on full-disk encryption for each device
   - *IoT devices are cheap, weakly secured and often cannot run agents. Segment them, change defaults, and restrict what they talk to. Antivirus and FDE need resources these devices lack. Servers do not replace thermostats.*
   - @3.1.iot
2. Which characteristic MOST often makes consumer IoT devices a security problem?
   - **[x] Weak defaults and little or no ongoing vendor patching**  - [ ] Powerful CPUs that attackers can mine with  - [ ] Too many security settings for users  - [ ] Encryption that cannot be disabled
   - *The IoT pattern: priced for features not security, default credentials, short support life. Hook: smart device, dumb security. The other options invert the real problem.*
   - @3.1.iot
3. A gas pipeline operator monitors valves across 900 km from a central control room using remote terminal units. Which system type is this?
   - **[x] SCADA**  - [ ] RTOS  - [ ] SDN  - [ ] Serverless
   - *SCADA (Supervisory Control and Data Acquisition) supervises geographically spread industrial sites. It is a type of ICS. RTOS is the OS inside a time-critical device. SDN and serverless are IT models.*
   - @3.1.ics
4. A factory's PLC network was built decades ago and talks only legacy protocols with no authentication. What is the BEST protection without replacing the PLCs?
   - **[x] Isolate the ICS network and tightly control the few paths into it**  - [ ] Install an EDR agent on every PLC  - [ ] Connect the PLCs to the corporate Wi-Fi for monitoring  - [ ] Enable automatic internet updates on each PLC
   - *ICS priorities: availability and safety first, so isolate and restrict access (segmentation, jump hosts, one-way gateways). PLCs usually cannot run agents. Wi-Fi and internet updates widen the attack surface.*
   - @3.1.ics
5. In an industrial control environment, which goal usually takes PRIORITY over confidentiality?
   - **[x] Availability and safety of the physical process**  - [ ] Hiding the plant's IP addresses  - [ ] Encrypting historian data at rest  - [ ] Data sovereignty of sensor logs
   - *For ICS, downtime can mean explosions or blackouts, so availability and safety lead; patching and scanning are planned around that. The other three are confidentiality-flavoured.*
   - @3.1.ics
6. An anti-lock braking unit must pulse the brakes on a guaranteed, fixed schedule no matter what else the car is doing. What does it MOST likely run on?
   - **[x] A real-time operating system (RTOS)**  - [ ] A general-purpose desktop OS  - [ ] A container on a shared host  - [ ] A serverless function
   - *RTOS guarantees deterministic timing. Security work is hard because they are minimal and long-lived; any delay from security tooling is unacceptable. Desktop OS and cloud models cannot guarantee millisecond response.*
   - @3.1.rtos
7. Why is it often hard to add security tools to an RTOS-based medical pump?
   - **[x] Extra processing can break the strict timing the device relies on**  - [ ] RTOS devices have no network connection by law  - [ ] An RTOS encrypts all memory, blocking scanners  - [ ] RTOS vendors forbid passwords on devices
   - *Timing is the product. Agents or heavy crypto risk missing deadlines, so security is designed in or applied around the device (segmentation). The other claims are false.*
   - @3.1.rtos
8. A printer's firmware is fixed in a chip and the vendor ships updates only rarely. Which term BEST describes this kind of device?
   - **[x] Embedded system**  - [ ] Microservice  - [ ] Jump server  - [ ] Thin client
   - *Embedded systems are purpose-built computers inside a product (printers, cameras, cars). Hard to patch, often long-lived. Hook: computer hidden in a thing. The others are architectures or appliances.*
   - @3.1.emb
9. A security lead must protect a fleet of embedded badge readers that will never receive firmware fixes. Which is the BEST compensating approach?
   - **[x] Segment them and monitor their traffic for anomalies**  - [ ] Re-flash them with a desktop OS  - [ ] Turn off logging to save memory  - [ ] Give them direct internet access for vendor support
   - *Inability to patch is a listed exam consideration; you compensate with isolation and monitoring. Re-flashing voids the device. Removing logs and adding internet access make things worse.*
   - @3.1.patch
10. A board is choosing between an in-house data centre and a cloud provider. Which consideration is BEST described as "the cloud lets us add capacity in minutes when demand spikes"?
    - **[x] Scalability**  - [ ] Risk transference  - [ ] Ease of recovery  - [ ] Inability to patch
    - *Scalability = grow or shrink resources with demand. Risk transference is shifting financial impact (insurance, contracts). Ease of recovery is how quickly you restore. Inability to patch is a legacy/embedded issue.*
    - @3.1.scale
11. A CFO prefers moving the email system to a provider partly because "if it fails, the provider's SLA penalties and liability cover us." Which consideration is this?
    - **[x] Risk transference**  - [ ] Responsiveness  - [ ] Compute  - [ ] Ease of deployment
    - *Risk transference shifts some impact to a third party through contracts or insurance. Accountability for the data stays with the company. The others are technical capacity or speed factors.*
    - @3.1.risk
12. A plant's legacy HMI runs an OS the vendor stopped supporting years ago and the line cannot stop for an upgrade. Which consideration is MOST in play?
    - **[x] Inability to patch**  - [ ] Scalability  - [ ] Ease of deployment  - [ ] Cost of cloud egress
    - *No vendor patches and no downtime window = inability to patch, mitigated by isolation, allow-listing and monitoring. Patch availability is the related question of whether a fix exists at all.*
    - @3.1.patch
13. An architect compares two designs: one rebuilds from IaC templates in 20 minutes, the other needs a week of manual setup. Which consideration separates them MOST?
    - **[x] Ease of recovery**  - [ ] Risk transference  - [ ] Power  - [ ] Data sovereignty
    - *Ease of recovery = how fast and simply you get back after failure. Templated rebuilds win. The others do not describe rebuild speed.*
    - @3.1.recov
14. Remote solar-powered field sensors keep dying when firmware with stronger encryption is installed. Which considerations is the team MOST trading off?
    - **[x] Power and compute against security**  - [ ] Risk transference against cost  - [ ] Scalability against responsiveness  - [ ] Data sovereignty against geolocation
    - *Constrained devices have limited battery and CPU; heavier crypto drains both. Lightweight algorithms are the usual answer. The other pairs are not about limited device resources.*
    - @3.1.power
15. A team selects a SaaS ticketing tool over self-hosting because it can be live in a day with no servers to build. Which consideration drove this?
    - **[x] Ease of deployment**  - [ ] Inability to patch  - [ ] Resilience  - [ ] Compute
    - *Ease of deployment = how quickly and simply it goes live. Resilience is surviving failures. Compute is processing capacity. Inability to patch is a negative trait.*
    - @3.1.deploy
16. A finance director asks why the cheaper single-server design was rejected. The architect replies that one failure would stop trading for hours. Which pair of considerations was weighed?
    - **[x] Cost against availability and resilience**  - [ ] Compute against power  - [ ] Responsiveness against risk transference  - [ ] Patch availability against scalability
    - *Every architecture choice trades cost against availability and resilience. A single server is cheap but a single point of failure. The other pairs do not describe the "one failure stops us" problem.*
    - @3.1.cost
17. A trading firm needs its order system to keep running even if a server dies mid-session. Which architectural feature addresses this MOST directly?
    - **[x] High availability through redundant, clustered servers**  - [ ] Air-gapping the order system  - [ ] Moving it to an RTOS  - [ ] Weekly offsite backups
    - *High availability = always-on through redundancy and automatic failover. Backups recover later but do not keep it running. Air gaps and RTOS do not add redundancy.*
    - @3.1.ha
18. A firm evaluates a network camera vendor. The review finds the vendor publishes security fixes within days of a flaw being disclosed and supports each model for seven years. Which consideration does this MOST directly measure?
   - **[x] Patch availability**  - [ ] Inability to patch  - [ ] Risk transference  - [ ] Responsiveness
   - *Patch availability = whether, and how quickly, fixes exist for a product. Inability to patch is when fixes cannot be applied at all. Risk transference shifts impact by contract. Responsiveness is how fast a system answers requests.*
   - @3.1.patch
19. PBQ 3.1 - Match the system. A city's operations centre lists its devices. Pick the BEST term for each. ¶  1  Supervisory system watching water pumps across the city ¶  2  Controller that must fire the airbags in vehicles within a guaranteed few milliseconds ¶  3  Smart bins that report fill level over Wi-Fi ¶  4  Firmware-only controller inside each parking meter
    - [p] Device 1 :: A SCADA · B RTOS · C IoT · D Embedded system = a
    - [p] Device 2 :: A SCADA · B RTOS · C IoT · D Embedded system = b
    - [p] Device 3 :: A SCADA · B RTOS · C IoT · D Embedded system = c
    - [p] Device 4 :: A SCADA · B RTOS · C IoT · D Embedded system = d
    - *1: wide-area supervision of industrial process = SCADA. 2: guaranteed timing = RTOS. 3: consumer-style connected sensor = IoT. 4: dedicated computer in a product = embedded. Overlap is real (IoT devices are embedded too); pick the most specific fit.*
    - @3.1.models
20. An app team compares two clouds. One answers API calls in 20 ms, the other in 300 ms. Which consideration is this?
    - **[x] Responsiveness**  - [ ] Risk transference  - [ ] Ease of recovery  - [ ] Inability to patch
    - *Responsiveness = how quickly the system reacts to requests. Users notice it, so it affects availability in practice. The others are about contracts, restore speed and legacy devices.*
    - @3.1.respond
21. A hospital's MRI scanner runs an embedded OS and the vendor says unapproved patches void its regulatory certification and support. What is the BEST way to reduce risk?
    - **[x] Isolate it on a restricted network segment with strict allow-lists**  - [ ] Apply the OS patches anyway  - [ ] Connect it directly to the internet for vendor telemetry  - [ ] Remove it from the asset inventory
    - *When you cannot patch, compensate: segmentation, allow-listing and monitoring. Patching against the vendor creates safety and compliance problems. Internet exposure increases risk. Removing from inventory hides it, it does not protect it.*
    - @3.1.emb

## Test 13 - 3.2 Secure Enterprise Infrastructure: Placement, Appliances, Firewalls, Secure Comms (25 Q)

1. A company is putting a public web server online. Where should it be placed?
   - **[x] In a screened subnet between the internet and the internal network**  - [ ] On the internal LAN next to the database  - [ ] On the guest Wi-Fi VLAN  - [ ] Directly on the internet with no firewall
   - *Public-facing servers go in a screened subnet (DMZ) so a compromise does not land attackers inside. Hook: the hotel lobby, not the back office. The LAN exposes internal systems; guest Wi-Fi mixes untrusted users; no firewall is no control.*
   - @3.2.place
2. An architect groups systems into "untrusted," "screened" and "trusted" areas, each with its own rules for traffic crossing between them. What is she defining?
   - **[x] Security zones**  - [ ] Failure modes  - [ ] Attack vectors  - [ ] Recovery sites
   - *Security zones group assets by trust level; policy is enforced where zones meet. Failure modes describe what a device does when it breaks. The others are unrelated.*
   - @3.2.zone
3. A team turns off unused services, closes unneeded ports and removes old test servers. What are they MAINLY reducing?
   - **[x] The attack surface**  - [ ] The recovery point objective  - [ ] The failure mode  - [ ] The data classification level
   - *Attack surface = every point an attacker could use. Less running, less to attack. RPO is backup timing. Failure mode is breakdown behaviour. Classification labels data.*
   - @3.2.surf
4. A card-processing firm's policy says that if its perimeter firewall's inspection engine ever faults, no transaction traffic may pass unchecked, even if that halts sales. How should the firewall be configured?
   - **[x] Fail-closed**  - [ ] Fail-open  - [ ] Passive monitoring  - [ ] Port mirroring
   - *Fail-closed blocks traffic on failure: security over availability. Fail-open lets traffic pass: availability over security, used where outage is worse than risk. Hook: closed door vs propped-open door.*
   - @3.2.fail
5. Clinicians fear that a fault in the new inline IPS guarding the electronic patient record system would lock them out mid-shift. Which configuration answers that fear, and at what cost?
   - **[x] Fail-open; traffic keeps flowing but goes uninspected during the fault**  - [ ] Fail-closed; traffic is blocked until the IPS is restored  - [ ] Tap mode; the IPS can then still block attacks  - [ ] Fail-open; no trade-off since the IPS is redundant
   - *Fail-open keeps clinical access alive at the cost of a security gap. Fail-closed is the opposite. In tap mode the device only sees copies and cannot block. There is always a trade-off.*
   - @3.2.fail
6. A SOC wants to watch traffic to the database without any chance of the sensor slowing or dropping packets. How should it be connected?
   - **[x] Passively, via a network tap or SPAN port**  - [ ] Inline, between the switch and the database  - [ ] As the database's default gateway  - [ ] Fail-closed, inline with the core router
   - *Passive / tap / monitor = sees a copy, never touches live traffic, can only detect (IDS). Inline = traffic passes through, can block (IPS), but adds a failure point. Hook: inline can intervene; tap can only tell.*
   - @3.2.attr
7. Which statement about active versus passive security devices is MOST accurate?
   - **[x] Active devices can respond, for example by blocking; passive ones only observe and alert**  - [ ] Passive devices must always be placed inline  - [ ] Active devices never generate logs  - [ ] Passive devices are always firewalls
   - *Active = takes action (IPS dropping packets). Passive = watches (IDS). Placement usually follows: active inline, passive on a tap. The other options are false.*
   - @3.2.attr
8. Admins must manage servers inside a locked-down subnet. The policy says no direct RDP or SSH from laptops. What should be deployed?
   - **[x] A hardened jump server that admins log into first**  - [ ] A forward proxy for web browsing  - [ ] A load balancer in front of the servers  - [ ] A passive IDS sensor
   - *Jump server (jump box) = one hardened, monitored entry point into a secure zone. Hook: a single guarded drawbridge. Proxies broker web traffic, load balancers spread load, an IDS only watches.*
   - @3.2.jump
9. A school wants all student web traffic to pass through one device that can cache pages and block categories of sites. What is the BEST fit?
   - **[x] A forward proxy server**  - [ ] A reverse proxy in the DMZ  - [ ] A jump server  - [ ] A layer 4 firewall
   - *Forward proxy = acts for internal clients going out: filtering, caching, logging. Reverse proxy sits in front of servers for inbound users. A layer 4 firewall sees ports, not site categories.*
   - @3.2.proxy
10. A company publishes several internal web apps to the internet through one device that hides the real servers and terminates TLS. What is this device?
    - **[x] A reverse proxy**  - [ ] A forward proxy  - [ ] A jump server  - [ ] A network tap
    - *Reverse proxy = stands in front of servers for inbound clients, hiding them and often offloading TLS. Forward = for clients going out. Hook: forward faces out, reverse faces in.*
    - @3.2.proxy
11. A SOC wants both alerts AND automatic blocking on known exploit signatures at the internet edge. Which device is BEST?
    - **[x] An inline IPS**  - [ ] A passive IDS on a SPAN port  - [ ] A forward proxy  - [ ] A jump server
    - *IPS inline detects and blocks. IDS on a SPAN only alerts. The other two are not signature-detection tools.*
    - @3.2.ids
12. A ticket-sales site puts one virtual IP in front of a pool of web servers; the device behind it probes each server and quietly drops dead ones from rotation. Which device is this, and what security benefit does it add?
    - **[x] A load balancer; it keeps the site available and can absorb some DoS traffic**  - [ ] A jump server; it limits admin access  - [ ] A WAF; it blocks SQL injection  - [ ] An IDS; it alerts on failed servers
    - *Load balancers distribute requests (round robin, least connections) and route around failed nodes, improving availability. Some also do TLS offload. WAFs inspect app attacks; IDS alerts on threats, not health.*
    - @3.2.lb
13. A security team places small devices at several network points that gather traffic statistics and send them to a central collector such as the SIEM. What are these devices called?
    - **[x] Sensors**  - [ ] Jump servers  - [ ] Load balancers  - [ ] Reverse proxies
    - *Sensors gather traffic or events for analysis and send them to a collector (a central console or SIEM); they are usually passive. The others move or control traffic.*
    - @3.2.sensor
14. Visitors keep plugging laptops into conference-room wall ports and getting onto the corporate LAN. What is the BEST fix?
    - **[x] 802.1X port-based authentication using EAP with a RADIUS server**  - [ ] A WAF in front of the web servers  - [ ] Moving the LAN to a public cloud  - [ ] A reverse proxy for the conference room
    - *802.1X = port-based network access control. The switch (authenticator) relays EAP messages to RADIUS (authentication server); the port stays blocked until the device or user authenticates. The others do not control physical port access.*
    - @3.2.port
15. In an 802.1X setup, what role does the switch play?
    - **[x] Authenticator, passing EAP messages to the authentication server**  - [ ] Supplicant, requesting access on the user's behalf  - [ ] Authentication server, checking the credentials itself  - [ ] Certificate authority, issuing device certificates
    - *Supplicant = client device. Authenticator = switch or AP. Authentication server = RADIUS. Hook: the guest, the doorman, the guest list.*
    - @3.2.port
16. A retailer's web store keeps being hit by SQL injection and cross-site scripting. Which control is MOST targeted at this?
    - **[x] A web application firewall**  - [ ] A layer 4 stateful firewall  - [ ] A jump server  - [ ] 802.1X on the store's switches
    - *WAF inspects HTTP at layer 7 for app attacks like SQLi and XSS. A layer 4 firewall sees IPs and ports, so allowed HTTPS with an injection payload sails through. Hook: WAF reads the letter, layer 4 only reads the envelope.*
    - @3.2.fw
17. A small branch with no IT staff wants firewall, IPS, anti-malware, web filtering and VPN in one box. What is this called?
    - **[x] Unified threat management (UTM)**  - [ ] Web application firewall  - [ ] Software-defined WAN  - [ ] Jump server
    - *UTM = all-in-one security appliance, simple for small sites, but a single point of failure and can bottleneck. A WAF only protects web apps. SD-WAN is about WAN routing.*
    - @3.2.fw
18. A firewall rule must allow Microsoft Teams but block a game that also uses TCP 443. Which firewall type can tell them apart?
    - **[x] A next-generation (layer 7) firewall with application awareness**  - [ ] A layer 4 firewall filtering by port  - [ ] A packet filter based on source IP  - [ ] A passive IDS on a tap
    - *NGFWs identify the application regardless of port. Layer 4 sees two flows on 443 and cannot distinguish. An IDS cannot block. Hook: layer 4 knows the door number, layer 7 knows who is walking through.*
    - @3.2.fw
19. Remote staff need encrypted access to internal file shares from home without installing a client, using only a browser. Which option fits BEST?
    - **[x] A TLS (SSL) VPN through the browser**  - [ ] An IPSec site-to-site tunnel  - [ ] A jump server on the internet with RDP open  - [ ] A forward proxy for the home network
    - *TLS VPNs often run clientless or with a light client over 443, easy through hotel firewalls. IPSec site-to-site links networks, not single remote users. Exposing RDP is a classic breach path.*
    - @3.2.vpn
20. Two offices need a permanent encrypted link where the payload AND the original IP headers are protected. Which configuration is BEST?
    - **[x] IPSec in tunnel mode with ESP**  - [ ] IPSec in transport mode with AH only  - [ ] An unencrypted GRE tunnel  - [ ] A TLS forward proxy
    - *Tunnel mode wraps the entire original packet in a new one; ESP encrypts. Transport mode protects only the payload, and AH gives integrity without encryption. Hook: tunnel = packet inside an armoured van; transport = only the letter is sealed.*
    - @3.2.tunnel
21. A retailer with 200 stores wants to route traffic over cheap broadband and 4G links, steering cloud app traffic directly to the cloud instead of back through headquarters. Which technology fits?
    - **[x] SD-WAN**  - [ ] A jump server  - [ ] An air-gapped network  - [ ] 802.1X
    - *SD-WAN centrally manages WAN links of any type and picks paths per application. It does not secure traffic by itself, so it is usually paired with security services. The others are not WAN technologies.*
    - @3.2.sdwan
22. A consultancy has closed its offices and wants its staff, wherever they are, to get firewalling, web filtering and zero trust access from cloud points of presence near them, joined with SD-WAN networking. What is this model?
    - **[x] SASE (Secure Access Service Edge)**  - [ ] UTM appliance at headquarters  - [ ] IPSec transport mode  - [ ] A screened subnet
    - *SASE = network plus security as a cloud service at the edge, near users. Hook: SD-WAN plus a security stack in the cloud. A UTM at HQ forces traffic home. The others are single mechanisms.*
    - @3.2.sase
23. A branch office will reach head office over the public internet, a leased line or 4G backup. The architect must decide which links carry which traffic and how each is secured. Which infrastructure consideration is she addressing?
   - **[x] Connectivity**  - [ ] Failure modes  - [ ] Device attribute  - [ ] Attack surface
   - *Connectivity = how sites and devices are linked (internet, MPLS, cellular, satellite) and the security each link needs, such as VPN encryption over untrusted links. Failure modes describe fail-open or fail-closed. Device attribute is active vs. passive or inline vs. tap/monitor.*
   - @3.2.conn
24. PBQ 3.2 - Network design. A clinic is building a new site. Choose the BEST control for each need. ¶  1  Stop unknown devices joining via wall ports ¶  2  Block XSS against the patient portal ¶  3  Admins reach the server zone through one monitored host ¶  4  Watch internal traffic without risk of dropping packets ¶  5  Encrypted link to head office, whole packet protected
    - [p] Need 1 :: A 802.1X · B WAF · C Jump server · D IDS on a tap · E IPSec tunnel mode = a
    - [p] Need 2 :: A 802.1X · B WAF · C Jump server · D IDS on a tap · E IPSec tunnel mode = b
    - [p] Need 3 :: A 802.1X · B WAF · C Jump server · D IDS on a tap · E IPSec tunnel mode = c
    - [p] Need 4 :: A 802.1X · B WAF · C Jump server · D IDS on a tap · E IPSec tunnel mode = d
    - [p] Need 5 :: A 802.1X · B WAF · C Jump server · D IDS on a tap · E IPSec tunnel mode = e
    - *1: port-based NAC. 2: layer 7 app inspection. 3: single hardened admin entry. 4: passive monitoring sees copies only. 5: tunnel mode wraps the whole packet. Hook: door, letter-reader, drawbridge, CCTV, armoured van.*
    - @3.2.select
25. A security manager has budget for one control at a branch where staff complain the old firewall cannot spot malware in allowed web traffic. Which choice MOST effectively addresses the stated gap?
    - **[x] An NGFW with application awareness and threat inspection**  - [ ] A second layer 4 firewall in series  - [ ] A jump server for branch admins  - [ ] A passive network tap
    - *Selecting effective controls means matching the control to the actual gap: content inside allowed traffic needs deep inspection. More layer 4 filtering sees the same ports. A jump server and a tap do not inspect or block web content.*
    - @3.2.select

## Test 14 - 3.3 Protecting Data: Types, Classification, States, Methods (24 Q)

1. A US clinic stores patient diagnoses and a payment processor stores card numbers. What data type do BOTH most clearly fall under?
   - **[x] Regulated data**  - [ ] Public data  - [ ] Trade secrets  - [ ] Non-human-readable data
   - *Regulated data is governed by laws or industry rules (HIPAA for health, PCI DSS for cards, GDPR for personal data). Public is free to share. Trade secrets are protected by the firm's own secrecy. Format is not the point.*
   - @3.3.type
2. A bakery chain's dough-proofing method gives it an edge only because rivals do not know it; it was never registered with any authority. What type of data is it?
   - **[x] Trade secret**  - [ ] Regulated data  - [ ] Legal information  - [ ] Public data
   - *Trade secret = valuable because it is secret, with no public registration. Patents and copyrights are intellectual property protected by registration or law. Hook: tell anyone and the protection is gone.*
   - @3.3.type
3. A security team finds a barcode export and a binary database file being copied out. A DLP rule focused on readable keywords missed them. Which data type explains the gap?
   - **[x] Non-human-readable data**  - [ ] Human-readable data  - [ ] Legal information  - [ ] Public data
   - *Non-human-readable data (barcodes, QR codes, binary, encoded) needs a machine to interpret, so keyword DLP can miss it. Human-readable is text a person can read directly. The other two are about content, not format.*
   - @3.3.type
4. A software firm's source code and its registered logo are best described as which data type?
   - **[x] Intellectual property**  - [ ] Financial information  - [ ] Regulated data  - [ ] Legal information
   - *IP covers creations of the mind: code, designs, trademarks, patents. Financial information is accounts and transactions. Legal information is contracts, case files and court records.*
   - @3.3.ip
5. A government contractor labels a design as accessible only to a named project team, with the most severe damage if leaked. Which classification is MOST appropriate?
   - **[x] Confidential**  - [ ] Public  - [ ] Critical  - [ ] Sensitive
   - *Confidential = very sensitive data you may view only with additional, specifically granted access; the tier above sensitive (IP, PII, PHI). Public needs no protection. Critical is about availability, not secrecy. Labels vary by organisation, so read the scenario.*
   - @3.3.class
6. A company's marketing brochure and press releases are posted on its website. What classification do they hold?
   - **[x] Public**  - [ ] Confidential  - [ ] Critical  - [ ] Restricted
   - *Public = intended for release, no harm if seen. Still protect its integrity (no defacement). The others need access control.*
   - @3.3.class
7. A logistics firm labels its routing database "critical" even though it holds nothing secret. What does that label MAINLY express?
   - **[x] The business cannot operate without it, so availability matters most**  - [ ] Only executives may read it  - [ ] It contains regulated health data  - [ ] It can be posted publicly
   - *Critical = essential to operations; the focus is availability and integrity, not secrecy. Hook: you can tell anyone, but you cannot lose it. The other options describe confidentiality labels or public data.*
   - @3.3.class
8. A laptop holding an unencrypted customer export is left in a taxi. Which data state was unprotected?
   - **[x] Data at rest**  - [ ] Data in transit  - [ ] Data in use  - [ ] Data in sovereignty
   - *At rest = stored on a disk, USB, backup. Full-disk encryption protects it. In transit = moving across a network. In use = in memory or being processed. "Data in sovereignty" is not a state.*
   - @3.3.state
9. Malware scrapes card numbers from a point-of-sale terminal's RAM while the payment is being processed. Which data state is attacked?
   - **[x] Data in use**  - [ ] Data at rest  - [ ] Data in transit  - [ ] Archived data
   - *In use = decrypted in memory while processing; RAM scrapers target it. Protections include secure enclaves and memory protection. At rest and in transit encryption do not help once the data is decrypted in memory.*
   - @3.3.state
10. A firm wants to stop staff in a call centre from seeing full card numbers on screen, while the billing system still uses the real values. Which method is BEST?
    - **[x] Data masking, showing only the last four digits**  - [ ] Hashing every card number with SHA-256  - [ ] Full-disk encryption on agents' PCs  - [ ] Geographic restrictions on the call centre
    - *Masking hides part of the value in the display; the original stays intact underneath. Hashing is one-way, so billing could not use it. FDE protects data at rest, not on screen. Geo restrictions control location.*
    - @3.3.mask
11. A merchant wants its systems never to store real card numbers, replacing them with random values that a secure vault can map back. Which method is this?
    - **[x] Tokenization**  - [ ] Hashing  - [ ] Masking  - [ ] Segmentation
    - *Tokenization swaps sensitive data for a random token with no mathematical link; only the vault can reverse it. That shrinks PCI scope. Hashing cannot be reversed. Masking hides on display. Segmentation isolates data, it does not replace it. Hook: casino chips stand in for cash.*
    - @3.3.token
12. A software vendor wants to verify that a downloaded installer has not been altered. Which method should it publish alongside the file?
    - **[x] A cryptographic hash of the file**  - [ ] A tokenized copy of the file  - [ ] A masked version of the installer  - [ ] The file's data classification label
    - *Hashing gives a fixed-length fingerprint; any change produces a different value, so it proves integrity. It is one-way, not encryption. Tokens, masks and labels do not verify integrity.*
    - @3.3.hash
13. A developer ships a mobile app and wants to make its JavaScript hard for competitors to read, without encrypting it. Which method fits?
    - **[x] Obfuscation**  - [ ] Tokenization  - [ ] Hashing  - [ ] Geographic restriction
    - *Obfuscation makes something hard to understand while it still works (renaming variables, scrambling logic). It is not strong protection, just a speed bump. The others do not keep code runnable but unreadable.*
    - @3.3.obf
14. A European company must ensure customer data stays subject to EU law and is not stored by its cloud provider in other countries. Which concept is this?
    - **[x] Data sovereignty**  - [ ] Data masking  - [ ] Data in use  - [ ] Obfuscation
    - *Data sovereignty = data is subject to the laws of the country where it is stored. Choose cloud regions and contracts accordingly. The others are protection methods or states, not legal jurisdiction.*
    - @3.3.sov
15. A streaming service is legally allowed to show a film only in Canada. What should it use to enforce this?
    - **[x] Geographic restrictions based on user geolocation**  - [ ] Hashing of the video files  - [ ] Tokenization of user accounts  - [ ] Data classification of the film as restricted
    - *Geolocation identifies where a user is (IP, GPS); geographic restrictions use it to allow or block access. VPNs can evade it, so it is not foolproof. The others do not consider location.*
    - @3.3.geo
16. An auditor asks how a company stops a stolen backup tape from being readable. Which method is the BEST answer?
    - **[x] Encryption of the backup data with keys held separately**  - [ ] Masking the account numbers in the backup  - [ ] Obfuscating file names on the tape  - [ ] Labelling the tape as confidential
    - *Encryption makes data unreadable without the key; keys must be stored apart from the tape. Masking a few fields leaves the rest exposed. Obfuscation is weak. A label protects nothing on its own.*
    - @3.3.enc
17. A firm keeps HR records on a separate database server on its own network segment, reachable only from the HR application. Which data protection method is this?
    - **[x] Segmentation**  - [ ] Tokenization  - [ ] Obfuscation  - [ ] Hashing
    - *Segmentation separates sensitive data so a breach elsewhere does not reach it. Hook: keep the jewels in a different room. The other three transform the data rather than isolating it.*
    - @3.3.seg
18. A file share holds board minutes. Everyone in the company currently has read access. What is the BEST first fix?
    - **[x] Restrict permissions to the board and named secretaries only**  - [ ] Hash every document on the share  - [ ] Move the share to a different country  - [ ] Obfuscate the folder name
    - *Permission restrictions apply least privilege through ACLs. Hashing breaks readability for everyone. Moving countries is sovereignty, not access. A renamed folder is still open.*
    - @3.3.perm
19. A company's web traffic between the browser and its online banking site must be protected from eavesdropping on public Wi-Fi. Which state and control pair is correct?
    - **[x] Data in transit, protected with TLS**  - [ ] Data at rest, protected with full-disk encryption  - [ ] Data in use, protected with masking  - [ ] Data at rest, protected with tokenization
    - *Moving across networks = in transit; TLS (or a VPN) encrypts it. FDE protects stored data. Masking changes display. Tokenization replaces stored values.*
    - @3.3.state
20. A file contains quarterly revenue figures, bank account numbers and payroll totals. Which data type BEST describes it?
   - **[x] Financial information**  - [ ] Legal information  - [ ] Intellectual property  - [ ] Trade secret
   - *Financial information = accounts, transactions, payroll and revenue; a prime fraud target and often regulated. Legal information is contracts and case files. IP is creations of the mind. A trade secret is valued for being secret.*
   - @3.3.fin
21. A law firm stores client contracts, litigation case files and court filings. Which data type are these?
   - **[x] Legal information**  - [ ] Financial information  - [ ] Public data  - [ ] Non-human-readable data
   - *Legal information = contracts, case records, court documents; often covered by privilege, so strong access control is needed. Financial information is accounts and transactions. Filings may become public, but case files are not.*
   - @3.3.legal
22. A company labels employee home addresses, medical leave notes and salary details so only HR can see them. Which classification BEST fits personal data about individuals like this?
   - **[x] Sensitive**  - [ ] Public  - [ ] Critical  - [ ] Proprietary
   - *Sensitive = a broad classification covering PII, PHI and intellectual property; addresses, medical notes and salaries are PII/PHI. Public needs no protection. Critical is about availability, not secrecy. Proprietary data is the organisation's own trade secrets, not personal details. Labels vary by organisation.*
   - @3.3.class
23. PBQ 3.3 - Pick the protection. A health insurer reviews data flows. Choose the BEST method for each. ¶  1  Agents see only the last four digits of member IDs ¶  2  Card numbers replaced with vault-mapped stand-ins ¶  3  Verify archived claim files were not modified ¶  4  Laptops unreadable if stolen ¶  5  Block logins from outside approved countries
    - [p] Need 1 :: A Masking · B Tokenization · C Hashing · D Encryption · E Geographic restrictions = a
    - [p] Need 2 :: A Masking · B Tokenization · C Hashing · D Encryption · E Geographic restrictions = b
    - [p] Need 3 :: A Masking · B Tokenization · C Hashing · D Encryption · E Geographic restrictions = c
    - [p] Need 4 :: A Masking · B Tokenization · C Hashing · D Encryption · E Geographic restrictions = d
    - [p] Need 5 :: A Masking · B Tokenization · C Hashing · D Encryption · E Geographic restrictions = e
    - *1: partial display = masking. 2: random stand-in with lookup = tokenization. 3: integrity check = hashing. 4: unreadable without key = encryption. 5: location-based access = geographic restrictions. Hook: hide, swap, fingerprint, lock, fence.*
    - @3.3.meth
24. A manufacturer's internal pricing playbook is shared with the whole sales force, but leaking it to rivals would hurt the business. It is not personal data and is not limited to a named few. Which classification fits BEST?
    - **[x] Private**  - [ ] Public  - [ ] Confidential  - [ ] Critical
    - *Private (also restricted, classified or internal use only) = not for outsiders; staff may need extra rights or an NDA. Confidential is more sensitive, viewable only with specifically granted access, which does not fit a whole sales force. Public needs no protection. Critical is about availability, not secrecy.*
    - @3.3.class

## Test 15 - 3.4 Resilience + Recovery: HA, Sites, Capacity, Testing, Backups, Power (24 Q)

1. An e-commerce site runs four identical web servers behind a device that shares requests among them. Which HA approach is this?
   - **[x] Load balancing**  - [ ] Clustering with shared storage  - [ ] A cold site  - [ ] Journaling
   - *Load balancing spreads requests over independent nodes and routes around failures. Clustering ties servers together to act as one system, often with shared storage and failover. Hook: load balancer = many tills, one queue; cluster = one till with a spare cashier ready.*
   - @3.4.ha
2. A database must keep running if its server fails, with a second node taking over the same storage automatically. Which approach fits BEST?
   - **[x] A failover cluster**  - [ ] Round-robin load balancing of web servers  - [ ] A weekly tape backup  - [ ] A cold site
   - *Clustering gives automatic failover for stateful systems like databases. Load balancing suits stateless front ends. Backups and cold sites recover later; they do not keep the service up.*
   - @3.4.ha
3. A bank needs to resume trading within minutes of losing its main data centre, regardless of cost. Which recovery site fits?
   - **[x] Hot site**  - [ ] Warm site  - [ ] Cold site  - [ ] Mobile site with no data
   - *Hot site = fully equipped, data current, ready almost immediately; most expensive. Warm = hardware ready, data needs loading (hours to days). Cold = space and power only (days to weeks).*
   - @3.4.site
4. A charity has a tiny budget and can tolerate two weeks of downtime. Which site is MOST appropriate?
   - **[x] Cold site**  - [ ] Hot site  - [ ] Warm site  - [ ] Active-active second data centre
   - *Cold site: cheapest, empty room with power and network; you bring hardware and data. Fits long tolerable downtime. Hot and active-active cost far more; warm is a middle ground not needed here.*
   - @3.4.site
5. A firm's primary and backup data centres are 5 km apart. A regional flood takes out both. Which principle was ignored?
   - **[x] Geographic dispersion**  - [ ] Platform diversity  - [ ] Capacity planning  - [ ] Journaling
   - *Geographic dispersion places sites far enough apart that one disaster (flood, quake, power grid) cannot hit both. The other principles would not have prevented a shared regional event.*
   - @3.4.geo
6. An airline builds its booking front end on two different web server products from two vendors, so one vendor's exploitable bug cannot take bookings offline. Which concept is this?
   - **[x] Platform diversity**  - [ ] Geographic dispersion  - [ ] Multi-cloud  - [ ] Clustering
   - *Platform diversity = different OSs, vendors or tech, so one flaw does not hit all. It adds management cost. Multi-cloud is diversity across cloud providers specifically.*
   - @3.4.div
7. A fintech's board asks that no single cloud vendor's regional failure or pricing change can strand the product, so workloads are built to run on AWS and Azure. Which resilience concept is this?
   - **[x] Multi-cloud**  - [ ] Community cloud  - [ ] Cold site  - [ ] Journaling
   - *Multi-cloud = more than one cloud provider, avoiding dependence on one. Community cloud is one cloud shared by organisations with common needs. The others are unrelated.*
   - @3.4.multi
8. A council writes plans for keeping essential services such as payroll and emergency calls working during a prolonged IT outage, including manual workarounds. What is this?
   - **[x] Continuity of operations planning**  - [ ] Capacity planning  - [ ] Platform diversity  - [ ] Parallel processing
   - *COOP covers keeping essential functions running during disruption, often with manual fallbacks. Capacity planning sizes resources for demand. Parallel processing spreads work across many processors.*
   - @3.4.coop
9. A help desk plans for a product launch by checking whether it has enough trained staff to cover triple call volume. Which capacity area is this?
   - **[x] People**  - [ ] Technology  - [ ] Infrastructure  - [ ] Platform diversity
   - *Capacity planning covers people (staff, skills, cross-training), technology (apps, licences, compute) and infrastructure (network, power, data centre). Staffing is the people part.*
   - @3.4.cap
10. Before Black Friday, a retailer confirms its servers, bandwidth and data-centre power can handle five times normal load. Which areas of capacity planning are covered?
    - **[x] Technology and infrastructure**  - [ ] People only  - [ ] Continuity of operations only  - [ ] Platform diversity and geographic dispersion
    - *Servers and applications = technology; bandwidth and power = infrastructure. No staffing is mentioned, so not people. Dispersion and diversity are resilience design, not sizing.*
    - @3.4.cap
11. A management team talks through a ransomware scenario around a table, with no systems touched, to check roles and decisions. Which test is this?
    - **[x] Tabletop exercise**  - [ ] Failover test  - [ ] Parallel processing  - [ ] Full simulation with live systems
    - *Tabletop = discussion-based walk-through; cheap and safe, finds gaps in plans and roles. Failover actually switches systems. Parallel processing spreads transactions over multiple CPUs or systems. A simulation acts the scenario out more realistically.*
    - @3.4.test
12. A team switches production traffic from the primary database to the standby during a maintenance window to prove the switch works. Which test is this?
    - **[x] Failover test**  - [ ] Tabletop exercise  - [ ] Parallel processing  - [ ] Phishing simulation
    - *Failover testing actually moves the workload to the backup system. Riskier than a tabletop but proves it works. Parallel processing is about spreading work across processors, not switching to a standby.*
    - @3.4.test
13. A payments platform spreads its transaction workload across many CPUs and several servers at once, so if one processor fails the remaining ones simply absorb its share. Which recovery and resilience option is this?
    - **[x] Parallel processing**  - [ ] Tabletop exercise  - [ ] Failover test  - [ ] Cold site activation
    - *Parallel processing (3.4 recovery testing) = multiple CPUs or systems process transactions simultaneously; faster, and a failed processor is taken out of the pool while the rest carry on. Tabletop is discussion only. Failover switches to a standby. A cold site is an empty recovery facility.*
    - @3.4.test
14. Before patching a production VM, an admin wants an instant point-in-time copy to roll back to if the patch fails. What is BEST?
    - **[x] A snapshot**  - [ ] An offsite tape backup  - [ ] Journaling  - [ ] A cold site
    - *Snapshots capture a VM or volume state in seconds for quick rollback. They are not a replacement for real backups since they often live on the same storage. Tapes are slow to restore. Journaling logs changes.*
    - @3.4.snap
15. A company keeps all backups on a NAS in the same server room. A fire destroys both. What should it have done?
    - **[x] Kept a copy offsite**  - [ ] Taken backups more often  - [ ] Used snapshots instead  - [ ] Encrypted the NAS
    - *Onsite backups restore fast; offsite copies survive site-wide disasters. You need both (3-2-1: three copies, two media, one offsite). Frequency, snapshots and encryption do not help if everything burns together.*
    - @3.4.bkp
16. A law firm's weekly backup drives are handed to a third-party vault service and kept off site. Which control BEST protects their contents if a drive goes missing?
    - **[x] Encrypt the backups**  - [ ] Increase backup frequency  - [ ] Use platform diversity  - [ ] Label them as public
    - *Offsite backups leave your control, so encrypt them and protect the keys. Frequency affects data loss, not theft. The other options do nothing for confidentiality.*
    - @3.4.bkp
17. A company can lose at most 15 minutes of order data. Its backups run nightly. What should change FIRST?
    - **[x] Backup frequency, to match the 15-minute tolerance**  - [ ] Move backups to a cold site  - [ ] Switch to tabletop testing  - [ ] Encrypt the nightly backup
    - *How often you back up sets how much data you can lose (this links to RPO). Nightly = up to 24 hours lost. A cold site, tests and encryption do not shrink the gap.*
    - @3.4.bkp
18. An incident response team rehearses a ransomware attack by injecting realistic fake alerts into an isolated copy of the environment and working through the response, without touching production. Which test is this?
   - **[x] Simulation**  - [ ] Tabletop exercise  - [ ] Fail over  - [ ] Parallel processing
   - *Simulation = acting out a scenario with realistic events in a controlled setting; more hands-on than a tabletop discussion. Fail over actually moves production to the backup. Parallel processing spreads work across multiple processors.*
   - @3.4.test
19. An organisation copies its database to a second site continuously so the copy is almost always current. What is this?
    - **[x] Replication**  - [ ] Snapshot  - [ ] Journaling  - [ ] Tape rotation
    - *Replication keeps a near-real-time copy elsewhere. It also copies corruption or ransomware, so it does not replace point-in-time backups. Snapshots are moments in time. Journaling logs each change.*
    - @3.4.repl
20. After a crash, a database replays its log of recent writes to reach a consistent state without losing committed transactions. Which feature made this possible?
    - **[x] Journaling**  - [ ] Replication  - [ ] Snapshots  - [ ] Load balancing
    - *Journaling records changes before or as they are applied, so the system can replay or roll back to a consistent point. Hook: the ship's log. The others copy data or spread load rather than logging each change.*
    - @3.4.journal
21. An IT manager boasts that nightly backups have completed for two years, but nobody has ever tried restoring one. Which backup consideration is MOST neglected?
   - **[x] Recovery, by regularly testing restores**  - [ ] Frequency  - [ ] Onsite/offsite placement  - [ ] Snapshots
   - *A backup is only useful if you can recover from it; test restores regularly to prove data and procedures work and how long it takes. Frequency is already nightly; placement and snapshots do not prove restorability.*
   - @3.4.bkp
22. A data centre wants servers to keep running through a brief power blip and for long enough to start backup power during a longer outage. What combination is BEST?
    - **[x] A UPS for the short term, plus a generator for the long term**  - [ ] A generator alone  - [ ] A UPS alone for multi-day outages  - [ ] A surge protector and a cold site
    - *UPS = battery, instant, minutes of runtime; bridges the gap until the generator starts. Generator = fuel, long-running, takes time to start. Hook: the UPS catches you, the generator carries you.*
    - @3.4.pwr
23. PBQ 3.4 - Resilience plan. A regional insurer is upgrading resilience. Choose the BEST fit for each need. ¶  1  Back online within minutes after losing HQ ¶  2  Keep servers up for the 30 seconds before the generator starts ¶  3  Spread transactions over many CPUs so losing one does not stop processing ¶  4  Roll back a VM quickly after a bad patch ¶  5  Survive a provider-wide cloud outage
    - [p] Need 1 :: A Hot site · B UPS · C Parallel processing · D Snapshot · E Multi-cloud = a
    - [p] Need 2 :: A Hot site · B UPS · C Parallel processing · D Snapshot · E Multi-cloud = b
    - [p] Need 3 :: A Hot site · B UPS · C Parallel processing · D Snapshot · E Multi-cloud = c
    - [p] Need 4 :: A Hot site · B UPS · C Parallel processing · D Snapshot · E Multi-cloud = d
    - [p] Need 5 :: A Hot site · B UPS · C Parallel processing · D Snapshot · E Multi-cloud = e
    - *1: minutes to recover = hot site. 2: instant bridge power = UPS. 3: work spread across processors, survivors carry on = parallel processing. 4: point-in-time VM copy = snapshot. 5: avoid one provider = multi-cloud. Hook: ready room, battery, many hands, photo, second landlord.*
    - @3.4.res
24. A retailer's recovery facility already has racks, servers and network links installed, but staff must load the latest backups and configure systems before it can take over, which takes about a day. Which site type is this?
    - **[x] Warm site**  - [ ] Hot site  - [ ] Cold site  - [ ] Multi-cloud
    - *Warm site = equipment in place, data and configuration still to load; hours to a day or so. Hot is live with current data. Cold is space and power only. Multi-cloud is spreading across providers, not a recovery facility.*
    - @3.4.site

## Test 16 - 4.1 Secure Baselines, Hardening, Wireless, Mobile, Application Security (24 Q)

1. A retailer has 400 store servers. Security writes a hardened build from a CIS benchmark, pushes it with configuration management, and reviews it after each Patch Tuesday. A new hire asks what the review step is called. What should you tell him?
   - **[x] Maintaining the baseline**  - [ ] Establishing the baseline  - [ ] Deploying the baseline  - [ ] Decommissioning the baseline
   - *Secure baseline lifecycle = establish (write it, often from a benchmark), deploy (push it out, ideally automated), maintain (revise as patches and threats change). Reviewing after each patch cycle is maintenance. Establish is tempting because the benchmark is mentioned, but that step already happened. Deploy is the push. Hook: write it, ship it, keep it current.*
   - @4.1.base
2. A quarterly compliance scan shows 30 of 400 servers now allow SMBv1, which the approved build disables. No change tickets exist. What is the BEST next action?
   - **[x] Re-apply the baseline with configuration management and investigate who changed it**  - [ ] Raise a change request to add SMBv1 to the baseline  - [ ] Accept the risk because only 30 servers are affected  - [ ] Rebuild all 400 servers from installation media
   - *This is configuration drift: systems wandering from the approved baseline. Fix by re-enforcing the baseline and finding the cause. Adding SMBv1 rewards the drift. Risk acceptance for an unapproved insecure protocol is not a valid shortcut. Rebuilding everything is heavy and touches the 370 healthy servers. Analogy: realigning a car that pulls to one side.*
   - @4.1.base
3. A new core switch and edge router arrive for a branch office. Which hardening step should the network engineer do FIRST, before connecting them to production?
   - **[x] Replace default credentials and disable Telnet and HTTP management in favour of SSH and HTTPS**  - [ ] Install endpoint antivirus on the switch and router operating systems  - [ ] Enroll the switch in the mobile device management console  - [ ] Turn on every port so users can connect on day one
   - *Network device hardening: change defaults, use encrypted management (SSH, HTTPS, SNMPv3), disable unused ports and services, update firmware. Switches and routers do not run general antivirus. MDM is for phones and tablets. Enabling all ports widens the attack surface. Hook: fewer doors, stronger locks.*
   - @4.1.hardnet
4. A water utility's SCADA HMI runs an old OS that the vendor will not let you patch without voiding support. What is the BEST way to harden it?
   - **[x] Isolate it on a segmented network with tight firewall rules and monitoring**  - [ ] Apply the latest OS patches regardless of vendor support  - [ ] Connect it to the corporate Wi-Fi so it gets centrally managed  - [ ] Install a full desktop office suite for operator convenience
   - *ICS/SCADA hardening relies on segmentation and network-level controls because patching is often restricted and uptime is critical. Patching against vendor terms risks safety and support. Joining corporate Wi-Fi expands exposure. Extra software adds attack surface. Hook: if you cannot fix the box, fence the box.*
   - @4.1.hardics
5. A medical pump vendor uses a real-time operating system (RTOS) on its devices. Why is hardening an RTOS-based device MORE difficult than hardening a laptop?
   - **[x] It has tight timing and resource limits, so you often cannot add agents or patch freely**  - [ ] An RTOS cannot be connected to any network  - [ ] An RTOS always runs with no authentication by design  - [ ] An RTOS is only found in mainframes, not devices
   - *RTOS = OS built to respond within strict deadlines; embedded devices have small CPUs and memory, so security agents and frequent patches may break timing. Rely on vendor updates, segmentation and disabling unused features. Many RTOS devices are networked. Lack of authentication is a weakness some have, not a definition. Mainframes are unrelated.*
   - @4.1.hardiot
6. A hotel installs 200 smart TVs and thermostats. Which TWO actions BEST harden these IoT devices? (Select 2)
   - **[x] Change default passwords and keep firmware updated**  - **[x] Place them on a separate VLAN from guest and staff systems**  - [ ] Give each device a public IP for easier remote support  - [ ] Disable logging to save device storage
   - *IoT hardening = remove defaults, patch firmware, segment. Public IPs expose them directly to the internet (think Mirai botnet). Disabling logs removes visibility. Analogy: putting the minibar in its own locked cupboard.*
   - @4.1.hardiot
7. A start-up's cloud account was set up quickly. Which hardening action gives the BIGGEST reduction in risk to the cloud infrastructure?
   - **[x] Enforce MFA on the root and admin accounts and remove unused access keys**  - [ ] Turn off the provider's activity logging to lower costs  - [ ] Make storage buckets public so teams can share files  - [ ] Give all developers the owner role to avoid delays
   - *Cloud hardening starts with identity: protect privileged accounts with MFA, remove stale keys, least privilege, and keep logging on. Disabling logs blinds you. Public buckets are a classic data leak. Owner for everyone breaks least privilege.*
   - @4.1.hardcloud
8. A new file server is built from a standard image. Which change BEST hardens it as a server and also benefits a workstation build?
   - **[x] Remove unneeded services and software, and enable a host-based firewall**  - [ ] Enable the guest account for troubleshooting  - [ ] Allow all users local administrator rights  - [ ] Disable automatic updates to avoid reboots
   - *Server and workstation hardening share basics: least functionality, host firewall, patches, least privilege. A guest account and local admin for all widen access. Turning off updates leaves known flaws open. Hook: if it is not needed, it is not installed.*
   - @4.1.hardsrv
9. Before adding access points to a new warehouse with metal racking, the network team walks the floor with a tool that measures signal and interference. What are they doing, and what output do they create?
   - **[x] A site survey, producing a heat map of signal coverage**  - [ ] A penetration test, producing an exploit report  - [ ] A tabletop exercise, producing lessons learned  - [ ] A war-driving attack, producing a list of SSIDs
   - *Wireless installation considerations: site survey (measure RF, interference, dead zones) and heat map (visual of signal strength). Good placement also limits signal leaking outside the building. War driving is an attacker searching for networks. Pen tests and tabletops are different activities.*
   - @4.1.site
10. A wireless survey of a law office finds its staff SSID is easy to pick up from the street and the coffee shop opposite. What should the network team do FIRST?
    - **[x] Adjust access point placement and transmit power to reduce coverage outside**  - [ ] Hide the SSID so outsiders cannot connect  - [ ] Switch the network to WEP for compatibility  - [ ] Add more access points near the windows
    - *Lower power and reposition APs so the signal stays inside. Hiding the SSID is weak: it is still visible to sniffers. WEP is broken. More APs at the windows makes leakage worse. Hook: keep the bubble inside the building.*
    - @4.1.site
11. An accounting firm lets staff read email on personal phones. Which MDM capability BEST protects company data if a phone is lost, without erasing the employee's personal photos?
    - **[x] Containerization with a selective (remote) wipe of the work container**  - [ ] Full device remote wipe  - [ ] Geofencing that disables the camera at the office  - [ ] Forcing the phone to use only cellular data
    - *Containerization (storage segmentation) keeps work data in a managed space that MDM can wipe alone. A full wipe destroys personal data, which hurts BYOD acceptance. Geofencing and cellular-only do not protect a lost phone's data.*
    - @4.1.mdm
12. PBQ 4.1 - Mobile deployment models. Match each company's plan to the model.
    - [p] Staff bring their own phones and install a work app :: A BYOD · B COPE · C CYOD = a
    - [p] The company buys phones, owns them, and allows some personal use :: A BYOD · B COPE · C CYOD = b
    - [p] Staff pick from an approved list of three models, then the company provides it :: A BYOD · B COPE · C CYOD = c
    - [p] Which model gives the company LEAST control over the device :: A BYOD · B COPE · C CYOD = a
    - [p] Connection method most at risk from bluejacking and bluesnarfing :: A Cellular · B Wi-Fi · C Bluetooth = c
    - *BYOD = bring your own device (user owns it, least control). COPE = corporate-owned, personally enabled. CYOD = choose your own device from an approved list, company owned. Bluejacking sends unsolicited messages and bluesnarfing steals data over Bluetooth. Hook: B = Bring, P = Personally enabled, C = Choose.*
    - @4.1.deploy
13. A sales rep often works from coffee shops. Which connection choice is MOST secure for reaching company systems?
    - **[x] Use the phone's cellular connection rather than open public Wi-Fi**  - [ ] Join the strongest open Wi-Fi network available  - [ ] Leave Bluetooth discoverable for quick pairing  - [ ] Share files over NFC with nearby colleagues
    - *Cellular data is encrypted to the carrier and avoids rogue or evil twin hotspots on open Wi-Fi (a VPN adds more protection). Discoverable Bluetooth invites bluejacking and bluesnarfing. NFC is short range but not a remote access method. Hook: open Wi-Fi = shouting in a crowded cafe.*
    - @4.1.conn
14. A law firm is replacing WPA2-PSK. It wants a mode that resists offline dictionary attacks on a shared passphrase. Which should it choose?
    - **[x] WPA3-Personal with SAE**  - [ ] WPA2-Personal with TKIP  - [ ] WEP with a 128-bit key  - [ ] An open network with a captive portal
    - *WPA3 replaces the PSK 4-way handshake with SAE (Simultaneous Authentication of Equals, a dragonfly handshake) that resists offline guessing and gives forward secrecy. TKIP and WEP are deprecated. A captive portal does not encrypt traffic.*
    - @4.1.wpa3
15. A hospital wants every clinician to log on to Wi-Fi with their own directory account so access can be revoked per person. Which design BEST fits?
    - **[x] WPA3-Enterprise using 802.1X with a RADIUS server**  - [ ] WPA3-Personal with one passphrase per ward  - [ ] MAC address filtering on each access point  - [ ] A hidden SSID with a long passphrase
    - *Enterprise mode = 802.1X port-based authentication; the AP passes credentials to a AAA server (RADIUS) that checks the directory. Per-user accounts, per-user revocation and accounting. Shared passphrases cannot be revoked per person. MAC filtering is easily spoofed. Hiding the SSID is not authentication.*
    - @4.1.aaa
16. A university's 802.1X Wi-Fi should authenticate users with a username and password but protect the exchange inside a TLS tunnel, without issuing a certificate to every student. Which EAP method fits BEST?
    - **[x] PEAP**  - [ ] EAP-TLS  - [ ] LEAP  - [ ] PAP
    - *PEAP (and EAP-TTLS) build a TLS tunnel using only a server certificate, then send the user's password inside it. EAP-TLS needs client certificates on every device. LEAP is old Cisco and weak. PAP sends passwords in the clear. Hook: PEAP = Protected, server cert only.*
    - @4.1.auth
17. A web form accepts an order quantity. Testers enter "1; DROP TABLE orders" and the app errors. What is the BEST fix in the code?
    - **[x] Server-side input validation that only accepts an integer in an allowed range**  - [ ] Client-side JavaScript that blocks letters in the box  - [ ] A longer session timeout for the order page  - [ ] Hiding the error message from the user
    - *Input validation checks type, length, format and range on the server, ideally with an allow list (plus parameterized queries for SQL). Client-side checks are easily bypassed with a proxy. Hiding errors does not fix the injection. Hook: never trust the browser.*
    - @4.1.input
18. A banking app's session cookie was stolen by a script injected into a forum page and also captured on an HTTP link. Which cookie attributes would have helped MOST?
    - **[x] HttpOnly and Secure**  - [ ] Expires and Path  - [ ] Domain and Max-Age  - [ ] SameSite=None and Path
    - *Secure cookies: HttpOnly stops JavaScript reading the cookie (XSS theft); Secure sends it only over HTTPS. SameSite helps against CSRF, but setting it to None removes that protection. Expiry and path settings do not stop either theft. Hook: HttpOnly = hands off for scripts, Secure = only in the armoured truck.*
    - @4.1.cookie
19. A development team wants to find hard-coded passwords and unsafe functions in source code before it is ever compiled or run. Which technique is BEST?
    - **[x] Static code analysis (SAST)**  - [ ] Dynamic analysis of the running app (DAST)  - [ ] Fuzzing the production API  - [ ] A user acceptance test
    - *Static analysis reads the code without executing it and flags patterns like hard-coded secrets and buffer overflows. Dynamic analysis and fuzzing need a running app. UAT checks business features, not security flaws. Note: static analysis can produce false positives that need review.*
    - @4.1.sast
20. Users get an OS warning that a new desktop tool's publisher cannot be verified. IT wants to prove each internal release came from the company and was not altered. What should the build pipeline add?
    - **[x] Code signing with the company's code-signing certificate**  - [ ] Obfuscation of the source code  - [ ] A self-extracting ZIP archive  - [ ] An MD5 checksum on the intranet page
    - *Code signing = a digital signature over the binary, proving origin (publisher) and integrity. Obfuscation hides logic but proves nothing. ZIP is packaging. A bare hash on the same site can be swapped with the file, and MD5 is weak. Hook: a wax seal on the package.*
    - @4.1.sign
21. Analysts want to open suspicious email attachments to see what they do without risking the corporate network. Which control is BEST?
    - **[x] A sandbox that runs the file in an isolated environment**  - [ ] A honeyfile placed on the file server  - [ ] Opening the file on a manager's laptop  - [ ] Converting the file to a PDF first
    - *Sandboxing = run untrusted code in isolation so its behaviour can be watched without affecting real systems; browsers and mobile apps also sandbox each other. A honeyfile is a decoy to detect access. A real laptop risks infection. Conversion may not neutralize all threats and does not show behaviour.*
    - @4.1.sandbox
22. A mobile app team pushes a new release. Which practice BEST supports the 4.1 "monitoring" requirement for application security?
    - **[x] Collect app and security logs centrally and alert on unusual errors or access patterns**  - [ ] Disable logging in production to improve speed  - [ ] Rely only on pre-release code reviews  - [ ] Ask users to email screenshots of any problems
    - *Monitoring = watching apps after release (logs, alerts, anomaly detection) because pre-release testing misses things. Disabling logs removes evidence. Code review is valuable but static. User screenshots are slow and unreliable. Hook: test before, watch after.*
    - @4.1.mon
23. A manufacturer uses embedded controllers in conveyor belts. Which hardening approach is MOST realistic?
    - **[x] Apply vendor firmware updates when available, disable unused interfaces, and segment the devices**  - [ ] Install an EDR agent on each controller  - [ ] Join each controller to the Windows domain  - [ ] Allow internet access so they can self-update from any site
    - *Embedded systems have limited resources and fixed function: harden via vendor firmware, removing unused ports and features, and network isolation. EDR and domain joining usually are not supported. Open internet access increases exposure.*
    - @4.1.hardics
24. A field team uses tablets that store customer signatures. Which mobile hardening setting is MOST important if a tablet is stolen?
    - **[x] Full device encryption with a strong screen lock**  - [ ] A brighter screen for outdoor use  - [ ] Unlimited failed unlock attempts  - [ ] Sideloading apps from any source
    - *Mobile hardening: encryption, strong PIN or biometrics, lockout after failed attempts, patching, and blocking sideloading. Unlimited attempts invite brute force. Sideloading bypasses app store checks. Screen brightness is not security.*
    - @4.1.hardmob

### Key facts
- **Baseline: establish, deploy, maintain. Hardening targets: mobile, workstations, switches, routers, cloud, servers, ICS/SCADA, embedded, RTOS, IoT.**
- **Wireless install: site survey, heat map. Security: WPA3 (SAE), AAA/RADIUS with 802.1X, EAP (PEAP, EAP-TLS, EAP-TTLS).**
- **Mobile: MDM; BYOD, COPE, CYOD; cellular, Wi-Fi, Bluetooth.**
- **App security: input validation, secure cookies, static code analysis, code signing, sandboxing, monitoring.**

## Test 17 - 4.2 + 4.3 Asset Management, Disposal, Vulnerability Management (27 Q)

1. A department wants to buy a cheap cloud note-taking app with a credit card. Which asset management step should catch this BEFORE it is used?
   - **[x] Procurement review, so security can vet the vendor and the purchase is recorded**  - [ ] Sanitization of the app's data at end of life  - [ ] A rescan after the app is installed  - [ ] Certification of destruction from the vendor
   - *Acquisition/procurement = the gate where security checks vendors, licensing and data handling before buying, and the asset enters the inventory. Card purchases skip it, creating shadow IT. Sanitization and destruction certificates are disposal steps. Rescans are vulnerability validation.*
   - @4.2.acq
2. During an incident, nobody can say who is responsible for an old database server or what data it holds. Which asset management practice was MISSING?
   - **[x] Assigning an owner and a data classification to each asset**  - [ ] Purchasing the server from an approved vendor  - [ ] Degaussing the server's drives  - [ ] Running a dark web threat feed
   - *Assignment/accounting: every asset needs an owner (accountable person) and a classification (how sensitive its data is) so decisions can be made fast. Procurement and degaussing are other lifecycle stages. Threat feeds are about external threats. Hook: no owner = nobody to call at 2 a.m.*
   - @4.2.own
3. A network scan finds 60 devices that are not in the CMDB. Which activity found them, and what should follow?
   - **[x] Enumeration; add them to the inventory or remove them if unauthorized**  - [ ] Data retention; keep them for seven years  - [ ] Sanitization; wipe them immediately  - [ ] Attestation; ask each user to sign off
   - *Monitoring/asset tracking = inventory plus enumeration (actively discovering what is really on the network). Unknown devices are either added and owned, or removed. Wiping devices you have not identified is premature. Attestation is an IAM access review. Analogy: counting the sheep and checking ear tags.*
   - @4.2.track
4. A firm retires 50 laptops with SSDs that will be resold to staff. Which method is BEST to make data unrecoverable while keeping the drives usable?
   - **[x] Sanitization using the drive's secure erase or cryptographic erase function**  - [ ] Degaussing each SSD  - [ ] Deleting the files and emptying the recycle bin  - [ ] A quick format of each drive
   - *Sanitization removes data so the media can be reused. For SSDs, use manufacturer secure erase or crypto erase (destroy the encryption key). Degaussing does not work on flash and wrecks magnetic drives. Delete and quick format leave data recoverable. Hook: reuse = sanitize; no reuse = destroy.*
   - @4.2.disp
5. A hospital pays a vendor to shred failed hard drives holding patient records. What should the hospital get from the vendor to prove it was done?
   - **[x] A certificate of destruction listing the drives' serial numbers**  - [ ] A copy of the vendor's ISO 9001 quality badge  - [ ] A memorandum of understanding  - [ ] A heat map of the shredding facility
   - *Certification = documented proof, ideally with serial numbers, that media was destroyed or sanitized. Good for audits and regulators. A quality badge does not prove this job. An MOU is a loose agreement. Heat maps are for Wi-Fi.*
   - @4.2.cert
6. A legal team says email for a closed project must be kept for six years, but storage admins want to delete it now to save space. Which disposal consideration applies?
   - **[x] Data retention requirements must be met before decommissioning**  - [ ] Media must be degaussed before retention starts  - [ ] Retention only applies to paper records  - [ ] Destruction always takes priority over legal rules
   - *Data retention = keep data for the period required by law, regulation or policy, then dispose of it properly. Decommissioning must respect it. Retention covers electronic records too. Degaussing would destroy what must be kept.*
   - @4.2.ret
7. PBQ 4.2 - Asset lifecycle. Match each event to the stage.
   - [p] Vendor security questionnaire before signing a purchase order :: A Acquisition · B Assignment · C Monitoring/tracking · D Disposal = a
   - [p] Tagging a new server with the owner "Payroll manager" and label "Confidential" :: A Acquisition · B Assignment · C Monitoring/tracking · D Disposal = b
   - [p] Quarterly reconciliation of the CMDB against agent check-ins :: A Acquisition · B Assignment · C Monitoring/tracking · D Disposal = c
   - [p] Shredding tapes past their retention date :: A Acquisition · B Assignment · C Monitoring/tracking · D Disposal = d
   - [p] Best method for magnetic tape that will never be reused :: A Quick format · B Degauss or shred · C Delete files · D Encrypt in place = b
   - *Acquisition = buying and vetting. Assignment/accounting = ownership and classification. Monitoring = inventory and enumeration. Disposal = sanitize, destroy, certify, honour retention. Degaussing works on magnetic media; shredding works on everything.*
   - @4.2.disp
8. A security team wants to find missing patches and weak configurations across 2,000 servers every week with minimal effort. What is the BEST identification method?
   - **[x] Scheduled credentialed vulnerability scans**  - [ ] An annual penetration test  - [ ] A bug bounty program  - [ ] A tabletop exercise
   - *Vulnerability scanning is automated and repeatable; credentialed scans log in and see installed software and settings, giving fewer false positives than non-credentialed scans. Pen tests are deeper but infrequent and manual. Bug bounties rely on outsiders. Tabletops test IR plans.*
   - @4.3.scan
9. A team pulls dozens of open-source libraries into its app. Which application security method BEST identifies when one of them gets a newly published vulnerability?
   - **[x] Package monitoring (software composition analysis) of dependencies**  - [ ] Static analysis of the team's own code only  - [ ] Penetration testing once a year  - [ ] A system and process audit
   - *Package monitoring tracks third-party components and their versions against vulnerability databases and alerts on new CVEs (think Log4j). Static analysis of your own code misses library flaws. Annual tests are too slow. Audits review processes.*
   - @4.3.app
10. A tester runs automated attacks against the staging web app while it is running, and finds a reflected XSS. Which analysis type was used?
    - **[x] Dynamic analysis**  - [ ] Static analysis  - [ ] Package monitoring  - [ ] Code signing
    - *Dynamic analysis (DAST) tests the running app from outside, including fuzzing. Static analysis reads code without running it. Package monitoring watches dependencies. Code signing proves origin. Hook: static = reading the recipe, dynamic = tasting the soup.*
    - @4.3.app
11. A CISO wants threat intelligence specific to her sector that peers share in confidence. Which source is BEST?
    - **[x] An information sharing and analysis center (ISAC) for her industry**  - [ ] Public OSINT on social media  - [ ] The dark web, searched by the CISO herself  - [ ] The vendor's marketing newsletter
    - *ISAC = information-sharing organization where members of one sector (finance, health, energy) share threats. OSINT is free and public but not sector specific. Dark web monitoring is useful for leaked credentials but risky to do yourself and unfocused. Marketing is not intel.*
    - @4.3.feed
12. A company's monitoring service reports that employee credentials are being sold on a forum. Which threat feed type produced this, and what should the company do FIRST?
    - **[x] Dark web monitoring; force resets for the affected accounts and check for misuse**  - [ ] OSINT; publish the list on the intranet  - [ ] A proprietary feed; ignore it until it is confirmed by a second vendor  - [ ] An ISAC feed; wait for the next quarterly meeting
    - *Dark web intelligence finds leaked credentials and data for sale. Act fast: reset and look for logins using them. Publishing the list spreads the leak. Waiting gives attackers time. Proprietary/third-party feeds are paid commercial sources.*
    - @4.3.feed
13. A games studio publishes rules for hackers who find flaws in its matchmaking service, and sends a cash reward for each confirmed report. What is this?
    - **[x] A bug bounty under a responsible disclosure program**  - [ ] An unauthorized penetration test  - [ ] A system audit  - [ ] A proprietary threat feed
    - *Responsible disclosure program = a safe, published route for reporting flaws; a bug bounty adds payment. Scope and rules make it authorized. Pen tests are contracted engagements. Audits check against a standard.*
    - @4.3.bounty
14. An auditor reviews how patches are approved, tested and deployed, and whether that process is followed. Which identification method is this?
    - **[x] A system/process audit**  - [ ] A vulnerability scan  - [ ] A threat feed  - [ ] Dynamic analysis
    - *Audits find weaknesses in processes and controls, not only in software, e.g. patches skipped because the approval step is unclear. Scans find technical flaws on hosts. Feeds give external intel. Dynamic analysis tests a running app.*
    - @4.3.audit
15. A scanner reports a critical Apache flaw on a server that runs IIS and has no Apache installed. What is this, and what should the analyst do?
    - **[x] A false positive; confirm it, document it and tune the scanner**  - [ ] A false negative; patch Apache immediately  - [ ] A true positive; isolate the server  - [ ] A zero-day; contact the vendor
    - *Confirmation step: a false positive = reported but not real. Verify, then suppress or tune so it does not waste time again. A false negative is the reverse: a real flaw the scan missed, which is more dangerous because nobody looks for it. Hook: false positive = false alarm, false negative = silent burglar.*
    - @4.3.conf
16. Which scanner outcome is the MOST dangerous for an organization?
    - **[x] A false negative**  - [ ] A false positive  - [ ] A true positive  - [ ] A true negative
    - *False negative = a real vulnerability not reported, so nobody fixes it. False positives waste time but are visible. True positives are found real flaws, which you can fix. True negatives are correct clean results.*
    - @4.3.conf
17. Both findings on a ticket read 8.1 (High). Finding A sits on the checkout API that customers reach from the internet; finding B is on a training PC with no network cable. Which should the team fix first, and why?
    - **[x] Patch the checkout API first, because environmental factors and business impact raise its priority**  - [ ] Treat them the same because the CVSS scores match  - [ ] Patch the training PC first because it is easier  - [ ] Ignore both until the score reaches 9.0
    - *CVSS base scores rate severity (0-10) but not your context. Environmental variables (exposure, compensating controls, asset value) and industry/organizational impact decide real priority. Easy-first is not risk-based. Waiting for 9.0 ignores real exposure.*
    - @4.3.prio
18. A report lists "CVE-2024-12345" next to a finding. What does that identifier give the team?
    - **[x] A unique, public name for a specific known vulnerability, so tools and vendors refer to the same flaw**  - [ ] A severity score from 0 to 10  - [ ] A signed patch for the flaw  - [ ] A list of attackers using it
    - *CVE = Common Vulnerability Enumeration (the exam objectives' expansion; MITRE's own name is Common Vulnerabilities and Exposures), a catalogue ID run by MITRE and fed into NIST's NVD. CVSS = the separate severity score. Neither is a patch or attribution. Hook: CVE is the name tag, CVSS is the thermometer.*
    - @4.3.cvss
19. A flaw would expose about 40% of a customer database's value if exploited. Which analysis term describes this percentage?
    - **[x] Exposure factor**  - [ ] Risk tolerance  - [ ] Vulnerability classification  - [ ] Environmental variable
    - *Exposure factor = percentage of an asset's value lost if the threat happens (used in SLE = asset value x EF). Risk tolerance = how much risk the business will accept. Classification sorts flaw types. Environmental variables adjust priority for your setup.*
    - @4.3.ef
20. A high-severity flaw is on a legacy controller with no patch available. Production cannot stop. What is the BEST response?
    - **[x] Segment the device and add compensating controls, and record a formal exception**  - [ ] Ignore it because no patch exists  - [ ] Unplug the controller and halt production  - [ ] Buy cyber insurance and take no other action
    - *Response options: patch, segmentation, compensating controls, insurance (transfer), and exceptions/exemptions (approved, documented, time-bound acceptance). When patching is impossible, reduce exposure and document. Ignoring it is not a documented decision. Halting ignores business needs. Insurance alone transfers money, not the threat.*
    - @4.3.resp
21. A business unit asks to skip a required patch on one app for 90 days during peak season. Which response is this, and what makes it acceptable?
    - **[x] An exception, approved by the risk owner with an expiry date and compensating controls**  - [ ] An exemption granted verbally by the help desk  - [ ] Risk avoidance, because the app stays online  - [ ] Validation, because the app was rescanned
    - *Exceptions/exemptions are formal, documented, approved by someone with authority, and time-limited. Verbal help desk approval has no authority or trail. Avoidance would mean stopping the activity. Validation checks a fix worked.*
    - @4.3.resp
22. After a patch rollout, how should the team BEST validate remediation?
    - **[x] Rescan the affected systems and verify the finding is gone**  - [ ] Close the ticket once the patch job reports "sent"  - [ ] Ask system owners if they noticed any change  - [ ] Wait for the next annual audit
    - *Validation = rescanning, audit and verification that the fix actually took. "Sent" does not mean installed. Owner opinions are not evidence. An annual audit is too late. Hook: trust, but rescan.*
    - @4.3.valid
23. The board wants to understand the vulnerability program's progress. Which report is MOST useful to them?
    - **[x] Trend of open critical findings and average time to remediate, by business unit**  - [ ] The full raw scanner output for every host  - [ ] A list of every CVE ID found this month  - [ ] Packet captures of the scans
    - *Vulnerability reporting should fit the audience: executives need trends, risk and remediation time; engineers need host details. Raw output and CVE lists overwhelm. Packet captures are not progress reports.*
    - @4.3.report
24. A company with low risk tolerance must decide on a medium flaw with a working public exploit on a customer portal. What is MOST likely?
    - **[x] Remediate quickly, because a public exploit and customer impact exceed its tolerance**  - [ ] Accept the risk because it is only medium  - [ ] Wait for CVSS to rise before acting  - [ ] Classify it as a false positive to close it
    - *Risk tolerance = how much risk the organization will accept. Low tolerance plus a known exploit and sensitive exposure push priority up beyond the raw score. Accepting ignores context. Waiting lets attackers move. Misclassifying hides real risk.*
    - @4.3.prio

25. A scanner groups findings as "missing patch", "misconfiguration", "weak cipher" and "default credentials", and maps each to a CWE type. Which 4.3 analysis activity is this?
    - **[x] Vulnerability classification**  - [ ] Exposure factor  - [ ] Risk tolerance  - [ ] Responsible disclosure
    - *Vulnerability classification = sorting flaws by type or category (for example by CWE or by missing patch versus misconfiguration) so similar issues get the same fix and owner. Exposure factor is the percentage of value lost. Risk tolerance is how much risk the business accepts. Responsible disclosure is how outsiders report flaws.*
    - @4.3.class
26. A bank hires an outside firm, under a signed scope and rules of engagement, to actively exploit weaknesses in its online banking platform and show how far an attacker could get. Which identification method is this?
    - **[x] Penetration testing**  - [ ] A credentialed vulnerability scan  - [ ] An OSINT threat feed  - [ ] A proprietary/third-party threat feed
    - *Penetration testing = authorized, scoped attempts to exploit vulnerabilities and chain them, proving real impact. A scan only identifies likely flaws without exploiting them. OSINT feeds are free public intelligence; proprietary/third-party feeds are paid commercial intelligence. Neither tests your systems. Hook: the scan finds the unlocked door, the pen test walks through it.*
    - @4.3.pentest
27. A retailer cannot fully patch its legacy point-of-sale estate this year. The board buys a policy that pays breach response, legal and notification costs if a card-data flaw is exploited. Which vulnerability response is this?
   - **[x] Insurance**  - [ ] Segmentation  - [ ] Compensating controls  - [ ] An exception/exemption
   - *Insurance (cyber insurance) transfers part of the financial impact to an insurer; it does not remove the flaw. Segmentation isolates the systems on the network. Compensating controls are other safeguards that reduce the risk. An exception/exemption formally records a decision not to apply a required fix. Hook: insurance pays for the damage, it does not stop it.*
    - @4.3.insure

### Key facts
- **4.2: acquisition/procurement; assignment (ownership, classification); monitoring (inventory, enumeration); disposal (sanitization, destruction, certification, data retention).**
- **4.3 identify: vuln scan, app security (static, dynamic, package monitoring), threat feeds (OSINT, proprietary/third-party, ISAC, dark web), pen test, responsible disclosure/bug bounty, audit.**
- **Analysis: false positive/negative, prioritize, CVSS (score), CVE (ID), classification, exposure factor, environmental variables, impact, risk tolerance.**
- **Response: patch, insurance, segmentation, compensating controls, exceptions/exemptions. Validate: rescan, audit, verify. Then report.**

## Test 18 - 4.4 Security Monitoring + Tools: SIEM, SCAP, NetFlow, DLP (22 Q)

1. An analyst must correlate failed VPN logins, firewall denies and domain controller events from 30 sources on one screen. Which tool is BEST?
   - **[x] A SIEM**  - [ ] A vulnerability scanner  - [ ] A NetFlow collector alone  - [ ] A host-based antivirus console
   - *SIEM (security information and event management) aggregates logs from many sources, normalizes and correlates them, alerts, and keeps them for reporting. NetFlow shows traffic metadata only. Scanners find flaws. Antivirus sees only endpoints. Hook: SIEM = the control room with every camera feed.*
   - @4.4.siem
2. A SOC's SIEM fires 4,000 alerts a day, almost all for one harmless backup job. Analysts now ignore the queue. What is the BEST fix?
   - **[x] Tune the alert rule to exclude the known backup activity**  - [ ] Turn off the SIEM's alerting  - [ ] Hire more analysts to read every alert  - [ ] Delete old logs to speed up the SIEM
   - *Alert tuning reduces false positives so real alerts get attention (avoiding alert fatigue). Disabling alerts blinds the SOC. More staff does not fix noisy rules. Deleting logs harms investigations and retention.*
   - @4.4.tune
3. The SIEM flags a workstation beaconing to a known malware domain at 03:00. What is the BEST immediate response?
   - **[x] Quarantine the workstation from the network, then investigate**  - [ ] Archive the alert for the monthly report  - [ ] Re-run the vulnerability scan next week  - [ ] Reboot the workstation and close the ticket
   - *Alert response and remediation: quarantine to stop spread or exfiltration, then investigate and validate the fix. Archiving delays action. A scan next week is too late. Rebooting can destroy volatile evidence and does not remove malware.*
   - @4.4.resp
4. A regulator requires security logs be kept for one year, but the SIEM only holds 90 days of hot storage. Which monitoring activity solves this?
   - **[x] Archiving older logs to cheaper long-term storage**  - [ ] Alert tuning  - [ ] Agentless scanning  - [ ] Deleting logs after 90 days
   - *Archiving = moving logs to long-term storage to meet retention and support later investigations. Tuning affects alert volume. Scanning finds flaws. Deleting would break the regulation.*
   - @4.4.arch
5. Which list BEST describes the three resource categories 4.4 says you should monitor?
   - **[x] Systems, applications and infrastructure**  - [ ] People, processes and policies  - [ ] Hot, warm and cold sites  - [ ] Confidentiality, integrity and availability
   - *Monitoring computing resources = systems (servers, endpoints), applications (app logs, errors), and infrastructure (network devices, cloud). The others are lists from other objectives.*
   - @4.4.res
6. A government contractor wants to check 500 servers automatically against a published hardening checklist using standard formats that different tools understand. Which framework fits BEST?
   - **[x] SCAP (Security Content Automation Protocol)**  - [ ] SNMP traps  - [ ] NetFlow  - [ ] STIX/TAXII
   - *SCAP is a NIST suite of standards (such as XCCDF checklists, OVAL checks, CVE, CVSS) so tools can share compliance content and results. SNMP traps are device alerts. NetFlow is traffic metadata. STIX/TAXII share threat intel.*
   - @4.4.scap
7. A team wants a vendor-neutral set of recommended secure settings for Windows Server and Ubuntu to compare systems against. What should they use?
   - **[x] CIS Benchmarks**  - [ ] A CVE list  - [ ] A NetFlow baseline  - [ ] A bug bounty report
   - *Benchmarks (CIS Benchmarks, DISA STIGs, vendor guides) are prescriptive configuration best practices; scans compare systems against them. CVEs list flaws, not settings. NetFlow and bug bounties are unrelated.*
   - @4.4.bench
8. A factory has sensors that cannot run software, plus Windows servers that can. Which monitoring approach fits EACH?
   - **[x] Agentless for the sensors; agents for the servers**  - [ ] Agents on both, installed by force  - [ ] Agentless on both, since agents are always worse  - [ ] No monitoring on the sensors at all
   - *Agent-based = software on the host, deep visibility, but needs install and upkeep. Agentless = query over the network (SNMP, WMI, SSH) or watch traffic, no install, less detail. Mix them by what each device supports. Skipping the sensors leaves a blind spot.*
   - @4.4.agent
9. A router's interface goes down and it sends an unsolicited alert to the management station. What is this?
   - **[x] An SNMP trap**  - [ ] An SNMP GET request  - [ ] A NetFlow record  - [ ] A syslog archive
   - *SNMP traps are sent by the device on an event (to UDP 162); polling (GET) is the manager asking (UDP 161). Use SNMPv3 for authentication and encryption. NetFlow records traffic conversations. Archives are storage. Hook: a trap springs by itself.*
   - @4.4.snmp
10. A university's link to the internet is saturated. The network team needs per-conversation records (source, destination, port, byte count) for every flow, but has no storage for full captures. Which tool fits BEST?
    - **[x] NetFlow**  - [ ] Full packet capture  - [ ] A DLP endpoint agent  - [ ] A SCAP scanner
    - *NetFlow (and IPFIX, sFlow) records flow metadata: source, destination, ports, protocol, bytes and time. Light to store and good for spotting exfiltration or beaconing. Packet capture keeps everything, which is heavy. DLP inspects content. SCAP checks configuration.*
    - @4.4.flow
11. NetFlow shows a print server sent 40 GB to 203.0.113.50 overnight. What is the BEST conclusion?
    - **[x] Possible data exfiltration that needs investigation**  - [ ] Normal behaviour for a print server  - [ ] A false negative from the SIEM  - [ ] A failed SNMP poll
    - *Large outbound flows from a host that should not send much are a classic exfil indicator. Print servers do not normally upload 40 GB to the internet. It is a detection, not a false negative. SNMP polls are tiny.*
    - @4.4.flow
12. An employee tries to upload a spreadsheet of customer card numbers to a personal cloud drive. Which tool BEST blocks this?
    - **[x] DLP (data loss prevention)**  - [ ] Antivirus  - [ ] NetFlow  - [ ] An SNMP trap
    - *DLP inspects content in use, in motion and at rest for patterns (card numbers, PII) and blocks or alerts. Antivirus looks for malware. NetFlow lacks content. SNMP is device monitoring.*
    - @4.4.dlp
13. A help desk PC shows a popup that a known trojan was found and quarantined. Which tool did this?
    - **[x] Antivirus**  - [ ] DLP  - [ ] A SIEM  - [ ] A vulnerability scanner
    - *Antivirus detects malware mainly by signatures plus some heuristics and quarantines it. DLP protects data. A SIEM collects and correlates. Scanners find unpatched flaws, not active malware.*
    - @4.4.av
14. A scanner reports outdated OpenSSL and weak cipher suites on a web server. Which tool produced this?
    - **[x] A vulnerability scanner**  - [ ] NetFlow  - [ ] DLP  - [ ] An SNMP trap receiver
    - *Vulnerability scanners probe hosts for known flaws, missing patches and weak configurations, and map them to CVEs with CVSS scores. The others do not test hosts for flaws.*
    - @4.4.vscan
15. PBQ 4.4 - Pick the tool. For each need, choose the BEST tool.
    - [p] Correlate logs across firewall, DC and VPN :: A SIEM · B NetFlow · C DLP · D SCAP · E Antivirus = a
    - [p] Show traffic volume by source and destination without payloads :: A SIEM · B NetFlow · C DLP · D SCAP · E Antivirus = b
    - [p] Stop a file with PII from being emailed outside :: A SIEM · B NetFlow · C DLP · D SCAP · E Antivirus = c
    - [p] Check 300 hosts against a standard XCCDF checklist :: A SIEM · B NetFlow · C DLP · D SCAP · E Antivirus = d
    - [p] Quarantine a known malicious file on a laptop :: A SIEM · B NetFlow · C DLP · D SCAP · E Antivirus = e
    - [p] Router reports its fan has failed, unprompted :: A SNMP trap · B SNMP poll · C NetFlow = a
    - *SIEM correlates. NetFlow = metadata about conversations. DLP = content control. SCAP = standard compliance checking. Antivirus = malware. Traps are device-initiated. Hook: who talks (NetFlow), what is said (DLP), what is wrong (scanner), what does it all mean (SIEM).*
    - @4.4.tool
16. Monthly, the SOC manager sends leadership a summary of incidents, top alert types and mean time to respond. Which monitoring activity is this?
    - **[x] Reporting**  - [ ] Log aggregation  - [ ] Scanning  - [ ] Quarantine
    - *Reporting turns monitoring data into summaries for decisions and compliance. Aggregation collects logs. Scanning checks for flaws. Quarantine isolates a host.*
    - @4.4.act
17. Logs from 200 servers each use a different time zone and format, which makes correlation hard. Which SIEM function addresses this?
    - **[x] Log aggregation with normalization and time synchronization**  - [ ] Alert tuning  - [ ] Archiving  - [ ] Agentless scanning
    - *Aggregation collects logs centrally and parses them into a common format; NTP keeps time stamps consistent so events line up. Tuning is about noise. Archiving is storage. Scanning finds flaws.*
    - @4.4.act
18. After a malware cleanup, how should the SOC BEST confirm remediation worked?
    - **[x] Rescan the host and watch for repeat alerts before releasing it from quarantine**  - [ ] Release the host as soon as the ticket is closed  - [ ] Disable the alert that fired  - [ ] Reformat the SIEM database
    - *Validation step of alert response: confirm the threat is gone (scan, monitor) before returning the system. Releasing on ticket status alone is unverified. Disabling the alert blinds you. Reformatting the SIEM is destructive.*
    - @4.4.resp
19. A cloud team wants its monitoring to cover load balancers, virtual networks and IAM changes, not just VMs. Which category of resource is it adding?
    - **[x] Infrastructure**  - [ ] Applications  - [ ] Systems only  - [ ] Physical sites
    - *Infrastructure = network and platform components (load balancers, routers, VPCs, identity services). Systems = hosts. Applications = software. Physical sites are not a 4.4 monitoring category.*
    - @4.4.res
20. A SOC runs weekly authenticated scans of servers as part of monitoring. Why include scanning as a MONITORING activity, not only a one-time test?
    - **[x] New vulnerabilities and drift appear constantly, so ongoing scans catch them**  - [ ] Scans replace the need for a SIEM  - [ ] Scanning is required only for wireless networks  - [ ] Scans prevent attacks by themselves
    - *Scanning is listed with aggregation, alerting, reporting and archiving: continuous because new CVEs and config changes happen all the time. Scans do not replace a SIEM, are not wireless-only, and only find, not block.*
    - @4.4.act
21. A DLP rule blocks every email containing "account", stopping half of finance's work. What is the BEST action?
    - **[x] Tune the rule to match real sensitive patterns, such as account numbers with validation**  - [ ] Turn off DLP for finance permanently  - [ ] Tell finance to use personal email  - [ ] Archive all blocked messages and ignore them
    - *Tuning applies to DLP as well as SIEM: refine patterns to cut false positives. Disabling DLP or moving to personal email increases risk. Ignoring blocked mail breaks the business.*
    - @4.4.tune
22. An SNMP-managed switch is still configured with v2c and the community string "public". What is the BEST change?
    - **[x] Move to SNMPv3 with authentication and encryption**  - [ ] Change the community string to "private"  - [ ] Disable all monitoring on the switch  - [ ] Allow SNMP from any IP address
    - *SNMPv1/v2c use plain-text community strings. SNMPv3 adds user authentication and encryption. "private" is just another default. Disabling monitoring loses visibility. Any-IP access widens exposure.*
    - @4.4.snmp

### Key facts
- **Monitor systems, applications, infrastructure. Activities: log aggregation, alerting, scanning, reporting, archiving, alert response (quarantine, alert tuning, validation).**
- **Tools: SCAP, benchmarks, agent vs agentless, SIEM, antivirus, DLP, SNMP traps (UDP 162), NetFlow, vulnerability scanners.**

## Test 19 - 4.5 Enterprise Capabilities: Firewall, IDS/IPS, Web + DNS Filter, OS Security, Email, EDR (25 Q)

1. A firewall ACL has these rules in order: 1) deny any any, 2) allow TCP 443 to 198.51.100.10. HTTPS to the web server fails. Why?
   - **[x] Rules are processed top-down and the deny-all matches first**  - [ ] HTTPS uses UDP, not TCP  - [ ] The allow rule needs port 80 as well  - [ ] Firewalls process the most specific rule first
   - *Firewall rules/access lists are evaluated top to bottom and the first match wins, so specific allows go above the implicit or explicit deny at the bottom. HTTPS is TCP 443 (HTTP/3 uses UDP but that is not the issue). Port 80 is not needed for HTTPS. Most firewalls do not reorder by specificity.*
   - @4.5.rules
2. An online shop's storefront and its inbound SMTP relay must be reachable from the internet. If either is breached, the attacker must not land on the HR network. Where should they be placed?
   - **[x] In a screened subnet (DMZ) between the external and internal firewalls**  - [ ] On the internal LAN with the file servers  - [ ] Directly on the internet with no firewall  - [ ] On the guest Wi-Fi VLAN
   - *Screened subnet = a separate zone for public-facing services, so a compromise there does not give direct access to the LAN. The LAN option mixes trust levels. No firewall is reckless. Guest Wi-Fi is the wrong trust zone.*
   - @4.5.dmz
3. A network IPS drops traffic matching a known exploit pattern, and also alerts when a host suddenly sends 10x its normal traffic. Which TWO detection methods are shown? (Select 2)
   - **[x] Signature-based**  - **[x] Anomaly/trend-based**  - [ ] Honeypot-based  - [ ] Certificate-based
   - *IDS/IPS use signatures (known patterns, low false positives, miss new attacks) and anomaly or trend analysis (deviation from a baseline, can catch new attacks, more false positives). IDS alerts; IPS sits inline and blocks. Honeypots are decoys. Certificates are not detection methods.*
   - @4.5.ids
4. A firm with many remote laptops wants web filtering to work even when users are off the VPN at home. Which approach fits BEST?
   - **[x] Agent-based web filtering on each laptop**  - [ ] A centralized proxy in the head office only  - [ ] A firewall rule on the office router  - [ ] Hiding the office SSID
   - *Agent-based filtering travels with the device and enforces policy anywhere. A centralized proxy only sees traffic routed through it. Office router rules do not see home traffic. SSIDs are irrelevant. Hook: the agent goes where the laptop goes.*
   - @4.5.web
5. A school wants to block gambling and adult sites without listing every URL. Which web filter feature is BEST?
   - **[x] Content categorization with block rules by category**  - [ ] A single deny rule for TCP 443  - [ ] URL scanning of only the first 10 sites visited  - [ ] Disabling DNS on student devices
   - *Content categorization uses vendor databases to label sites (gambling, adult, social media) so you block categories. Blocking 443 kills all HTTPS. Partial scanning misses most traffic. No DNS breaks everything.*
   - @4.5.web
6. A user clicks a link to a brand-new domain registered yesterday that is not yet categorized. Which web filter feature is MOST likely to block it?
   - **[x] Reputation scoring that treats new or unrated domains as high risk**  - [ ] A category block for "news"  - [ ] An allow list of all .com domains  - [ ] The proxy's caching function
   - *Reputation-based filtering rates sites by age, history and threat data; newly registered domains are often phishing. Categories may not exist yet. Allowing all .com is useless. Caching speeds browsing, not security.*
   - @4.5.web
7. Malware on several PCs resolves randomly generated domain names to find its command server. Which control BEST blocks this early, for every device on the network?
   - **[x] DNS filtering that refuses to resolve known malicious and suspicious domains**  - [ ] A longer DHCP lease time  - [ ] Content categorization on the email gateway  - [ ] Disabling SNMP on the PCs
   - *DNS filtering stops the lookup itself, so the connection never starts, and it covers any device using that resolver. DHCP and SNMP do not affect lookups. Email gateways do not see DNS queries from malware.*
   - @4.5.dns
8. A Windows admin must stop USB storage and enforce a 15-minute screen lock on 3,000 domain-joined PCs. Which tool is BEST?
   - **[x] Group Policy**  - [ ] SELinux  - [ ] NetFlow  - [ ] A web proxy
   - *Group Policy (GPOs) centrally pushes security settings to Windows machines in Active Directory. SELinux is Linux. NetFlow is traffic data. A proxy filters web traffic.*
   - @4.5.os
9. A Linux web server is compromised, but the attacker's process cannot read /etc/shadow even though it runs as a privileged service. Which feature MOST likely stopped it?
   - **[x] SELinux enforcing mandatory access control policies**  - [ ] Group Policy  - [ ] A DLP agent  - [ ] DNSSEC
   - *SELinux (Security-Enhanced Linux) adds MAC: labels and policies limit what each process can touch, even if it has root-like rights. Group Policy is Windows. DLP watches data flow. DNSSEC signs DNS records.*
   - @4.5.os
10. An admin must replace insecure protocols. Which choice pairs the right secure protocol and port?
    - **[x] SFTP over SSH on TCP 22 instead of FTP on TCP 21**  - [ ] Telnet on TCP 23 instead of SSH on TCP 22  - [ ] HTTP on TCP 80 instead of HTTPS on TCP 443  - [ ] LDAP on TCP 389 instead of LDAPS on TCP 636
    - *Protocol selection, port selection and transport method: pick encrypted protocols on their standard ports (SSH/SFTP 22, HTTPS 443, LDAPS 636, SMTPS 465 or STARTTLS on 587, IMAPS 993). The other options swap secure for insecure.*
    - @4.5.proto
11. A company wants to stop attackers sending mail that claims to be from its domain. Which DNS record lists the servers allowed to send its mail?
    - **[x] SPF**  - [ ] DKIM  - [ ] DMARC  - [ ] MX
    - *SPF (Sender Policy Framework) = TXT record listing authorized sending IPs. DKIM signs messages with a key published in DNS. DMARC tells receivers what to do when SPF/DKIM fail and asks for reports. MX says where to deliver incoming mail.*
    - @4.5.mail
12. Partners report spoofed invoices from the company's domain still land in inboxes, even though SPF and DKIM exist. Which addition BEST tells receivers to reject failures and send reports?
    - **[x] A DMARC record with p=reject**  - [ ] A second SPF record  - [ ] A longer DKIM key only  - [ ] An extra MX record
    - *DMARC sets policy (none, quarantine, reject) for messages that fail alignment and gives aggregate reports. Two SPF records is invalid. Key length does not set policy. MX is delivery routing.*
    - @4.5.mail
13. A mail gateway receives a message with a valid digital signature in the header, verified with a public key in the sender's DNS. Which control is this?
    - **[x] DKIM**  - [ ] SPF  - [ ] DMARC  - [ ] S/MIME user certificate
    - *DKIM (DomainKeys Identified Mail) signs mail at the sending server; receivers check with the public key in DNS, proving the domain and that content was not altered. SPF checks sending IPs. DMARC is the policy layer. S/MIME is user-level signing and encryption.*
    - @4.5.mail
14. Which device BEST scans all inbound mail for malware, spam and phishing links before it reaches user mailboxes?
    - **[x] An email security gateway**  - [ ] A NetFlow collector  - [ ] A DNS filter  - [ ] A NAC appliance
    - *A secure email gateway sits in the mail path (on-prem or cloud) and filters spam, malware, URLs and attachments, and often enforces SPF/DKIM/DMARC checks and DLP. NetFlow sees no content. DNS filters lookups. NAC controls network admission.*
    - @4.5.gate
15. An attacker modifies a system DLL on a payment server. Which control would MOST quickly detect the change?
    - **[x] File integrity monitoring (FIM)**  - [ ] A web filter  - [ ] SPF  - [ ] A heat map
    - *FIM hashes critical files and alerts when they change unexpectedly (Tripwire is a classic example; PCI DSS requires it). Web filters and SPF are other areas. Heat maps are wireless.*
    - @4.5.fim
16. A contractor plugs a personal laptop into a meeting-room network jack. It should be placed in a quarantine VLAN until it passes posture checks. Which capability does this?
    - **[x] Network access control (NAC)**  - [ ] DLP  - [ ] FIM  - [ ] DKIM
    - *NAC checks identity and device health (patches, AV, agent present) before granting access, often using 802.1X, and can quarantine or remediate. Agents can be persistent or dissolvable; agentless checks exist too. DLP, FIM and DKIM do not control network admission.*
    - @4.5.nac
17. The SOC wants to detect ransomware behaviour on laptops, isolate a host remotely, and roll back changes. Which tool fits BEST?
    - **[x] EDR (endpoint detection and response)**  - [ ] Traditional signature antivirus  - [ ] A web proxy  - [ ] SNMP traps
    - *EDR records endpoint behaviour, detects suspicious activity (not only signatures), and lets responders isolate, investigate and remediate. XDR extends this across endpoints, network, cloud and email for correlated detection. Antivirus is mostly signatures. Proxies and SNMP do not act on hosts.*
    - @4.5.edr
18. A SOC has separate consoles for laptop agents, the mail filter, firewall sensors and the cloud identity provider. Analysts want one product that stitches these signals into a single incident timeline. What should it choose?
    - **[x] XDR (extended detection and response)**  - [ ] A standalone host firewall  - [ ] A DMARC report viewer  - [ ] A file integrity monitor
    - *XDR = EDR extended across many telemetry sources with automated correlation. The others cover one narrow area each.*
    - @4.5.edr
19. A finance user who normally logs in 9-to-5 from Leeds downloads 5,000 files at 02:00 from a new country. Which capability is BEST suited to flag this?
    - **[x] User behavior analytics (UBA/UEBA)**  - [ ] SPF  - [ ] Group Policy  - [ ] Content categorization
    - *UBA builds a baseline of normal user behaviour and flags deviations like odd hours, location and volume, catching compromised accounts and insiders. SPF is email. Group Policy pushes settings. Categorization is web filtering.*
    - @4.5.uba
20. PBQ 4.5 - Firewall rules. Build rules for a DMZ web server at 203.0.113.10 and an internal DB at 192.0.2.20. Pick the action for each rule.
    - [p] Internet -> 203.0.113.10 TCP 443 :: A Allow · B Deny = a
    - [p] Internet -> 192.0.2.20 TCP 1433 :: A Allow · B Deny = b
    - [p] 203.0.113.10 -> 192.0.2.20 TCP 1433 :: A Allow · B Deny = a
    - [p] Internet -> 203.0.113.10 TCP 23 :: A Allow · B Deny = b
    - [p] Last rule in the list :: A Allow any any · B Deny any any = b
    - [p] Where should rule 1 sit relative to the last rule :: A Above it · B Below it = a
    - *Allow only what is needed: public HTTPS to the DMZ web server, and the web server to the DB on SQL Server's port. Never expose the DB to the internet. Telnet (23) is insecure and unneeded. End with deny-all (implicit deny) and keep allows above it because the first match wins.*
    - @4.5.rules
21. An IPS keeps blocking a legitimate business application after a signature update. What is the BEST action?
    - **[x] Investigate and tune or create a narrow exception for that signature**  - [ ] Switch the IPS to off permanently  - [ ] Move the IPS out of line so it only alerts forever  - [ ] Roll back to signatures from two years ago
    - *False positives are tuned with targeted exceptions, keeping protection elsewhere. Turning off or permanently going passive drops prevention. Old signatures miss current threats.*
    - @4.5.ids
22. A team must choose between TLS and IPsec to protect traffic between two data centres, for all protocols at the network layer. Which is BEST?
    - **[x] An IPsec site-to-site tunnel**  - [ ] TLS on each individual application  - [ ] SNMPv2c  - [ ] Plain GRE with no encryption
    - *Transport method choice: IPsec works at layer 3 and protects all traffic between sites. TLS protects one application session at a time. SNMPv2c is monitoring and unencrypted. GRE alone does not encrypt.*
    - @4.5.proto
23. Network DLP on the egress points is in place, but staff copy data to USB drives at their desks. What should be added?
    - **[x] Endpoint DLP agents that control removable media**  - [ ] More network DLP sensors  - [ ] A stricter DMARC policy  - [ ] A web content category block
    - *DLP locations: network (data in motion), endpoint (data in use, USB, print, clipboard) and storage (data at rest). USB copying never crosses the network. DMARC and web categories are unrelated.*
    - @4.5.dlp
24. A firewall admin is told to "allow DNS" for internal resolvers to reach the internet. Which port and protocol selection is MOST accurate?
    - **[x] UDP and TCP 53**  - [ ] TCP 443 only  - [ ] UDP 161 only  - [ ] TCP 25 only
    - *DNS uses UDP 53 for most queries and TCP 53 for large responses and zone transfers (DNS over HTTPS uses 443, but that is a separate choice). 161 is SNMP. 25 is SMTP.*
    - @4.5.ports

25. A company routes all staff web traffic through one centralized proxy in its data centre, which checks each requested Universal Resource Locator (URL) against threat lists before allowing it. Which TWO web filter features are shown? (Select 2)
    - **[x] Centralized proxy**  - **[x] URL scanning**  - [ ] Agent-based filtering  - [ ] DNS filtering
    - *A centralized proxy sits in the traffic path for every user routed through it; URL scanning inspects each requested address (and often the page) against threat and category data. Agent-based filtering runs on each device instead. DNS filtering acts on name lookups, not full URLs. Note the objectives expand URL as Universal Resource Locator (more commonly Uniform Resource Locator).*
    - @4.5.web

### Key facts
- **Firewall: rules top-down, first match, implicit deny; access lists; ports/protocols; screened subnet. IDS/IPS: signatures, trends/anomaly.**
- **Web filter: agent-based, centralized proxy, URL scanning, content categorization, block rules, reputation. DNS filtering.**
- **OS security: Group Policy (Windows), SELinux (Linux MAC). Secure protocols: choose protocol, port, transport.**
- **Email: SPF (who may send), DKIM (signature), DMARC (policy + reports), gateway. Also FIM, DLP, NAC, EDR/XDR, UBA.**

## Test 20 - 4.6 IAM I: Provisioning, Identity Proofing, Federation, SSO, Access Control Models (24 Q)

1. A new nurse starts Monday. HR enters her in the HR system and, overnight, accounts are created in the directory, EHR and email with the "Ward Nurse" role. What is this process?
   - **[x] User provisioning driven by HR as the source of truth**  - [ ] De-provisioning  - [ ] Attestation  - [ ] Identity federation
   - *Provisioning = creating accounts and granting access when someone joins, ideally automated from HR. De-provisioning removes it at leave. Attestation is a periodic review. Federation links identities between organizations.*
   - @4.6.prov
2. An engineer resigned three weeks ago, yet his VPN account was used last night. Which process failed?
   - **[x] De-provisioning on termination**  - [ ] Identity proofing at hiring  - [ ] Password complexity  - [ ] Single sign-on configuration
   - *De-provisioning should disable or remove accounts promptly when someone leaves, ideally triggered from HR on the last day. Proofing happens at onboarding. Complexity does not matter if the account should not exist. SSO would make one disable effective everywhere but is not what failed.*
   - @4.6.deprov
3. A developer moved from payments to marketing two years ago but still has write access to the payments database. What is this problem called, and what fixes it?
   - **[x] Permission creep; review and remove old rights when roles change**  - [ ] Privilege escalation exploit; patch the database  - [ ] Federation failure; reissue SAML certificates  - [ ] Credential stuffing; enforce MFA
   - *Permission assignments and implications: rights pile up as people move (privilege creep), breaking least privilege. Fix with role-change processes and access reviews. An exploit is an attack, not slow accumulation. SAML and stuffing are unrelated.*
   - @4.6.perm
4. Before issuing a remote employee a smart card, a bank checks her passport on a live video call and matches it to HR records. What is this?
   - **[x] Identity proofing**  - [ ] Attestation  - [ ] Authorization  - [ ] Accounting
   - *Identity proofing = verifying a person really is who they claim before creating credentials (documents, records, in-person or video checks). Attestation is periodic confirmation of access. Authorization grants rights. Accounting logs activity.*
   - @4.6.proof
5. Every quarter, managers must confirm that each team member's access is still needed, and sign off. What is this called?
   - **[x] Attestation (access recertification)**  - [ ] Identity proofing  - [ ] Provisioning  - [ ] Federation
   - *Attestation = an owner formally confirms access is correct, catching creep and orphaned accounts. Often required by auditors. Proofing verifies identity at the start. Provisioning creates access. Federation shares identity across domains.*
   - @4.6.attest
6. Employees of a manufacturer log in once with company credentials and then reach a partner's supplier portal without a separate account. What makes this possible?
   - **[x] Federation, where the partner trusts the manufacturer's identity provider**  - [ ] Discretionary access control  - [ ] A shared password for all staff  - [ ] Time-of-day restrictions
   - *Federation = trust between organizations so one identity provider (IdP) vouches for users to another's service provider (SP). Users keep one identity. Shared passwords destroy accountability. DAC and time rules are access models.*
   - @4.6.fed
7. A web app redirects the user to the corporate IdP, which returns a signed XML assertion saying who the user is and their group membership. Which standard is this?
   - **[x] SAML**  - [ ] OAuth  - [ ] LDAP  - [ ] RADIUS
   - *SAML (Security Assertion Markup Language) passes XML assertions from IdP to SP for browser SSO, mostly enterprise web apps. OAuth is authorization using tokens (often JSON). LDAP is a directory query protocol. RADIUS is network AAA.*
   - @4.6.saml
8. A fitness app asks: "Allow FitApp to read your calendar?" The user clicks yes and FitApp gets a token, never seeing the user's password. Which standard is this?
   - **[x] OAuth**  - [ ] SAML  - [ ] Kerberos  - [ ] LDAP
   - *OAuth 2.0 = delegated authorization: a user grants an app limited access to resources via access tokens. It is not, alone, an authentication protocol; OpenID Connect adds identity on top. SAML is XML-based SSO. Kerberos uses tickets within a domain. LDAP is directory lookup. Hook: OAuth = valet key, not the master key.*
   - @4.6.oauth
9. An internal app looks up a user's department and group membership from Active Directory on TCP 636. Which protocol is in use?
   - **[x] LDAPS (LDAP over TLS)**  - [ ] SAML  - [ ] OAuth  - [ ] SNMPv3
   - *LDAP queries directories (TCP/UDP 389); LDAPS wraps it in TLS on 636. Many SSO setups use LDAP as the back-end directory. SAML and OAuth are web federation and authorization. SNMP is device monitoring.*
   - @4.6.ldap
10. An IT manager evaluates SSO. Which is the BEST security benefit?
    - **[x] Fewer passwords to reuse or write down, and one place to disable access**  - [ ] Users never need any authentication  - [ ] Compromise of the SSO account affects only one app  - [ ] It removes the need for MFA
    - *SSO reduces password fatigue and centralizes control and logging. Downside: the SSO account is a single key to everything, so protect it with MFA. It still requires authentication. The other options are the reverse of reality.*
    - @4.6.sso
11. A company's new HR SaaS supports SAML and OIDC but its old intranet only supports LDAP. Which IAM concern does this highlight?
    - **[x] Interoperability between identity systems and protocols**  - [ ] Attestation  - [ ] Time-of-day restrictions  - [ ] Identity proofing
    - *Interoperability = whether different systems and standards can work together for authentication and authorization; you may need connectors or an IdP that bridges protocols. The others are separate IAM topics.*
    - @4.6.interop
12. PBQ 4.6 - Access control models. Match each scenario to the model.
    - [p] Military system: users with "Secret" clearance cannot read "Top Secret" labelled files; only admins set labels :: A Mandatory · B Discretionary · C Role-based · D Rule-based · E Attribute-based = a
    - [p] A file owner shares her folder with two colleagues of her choice :: A Mandatory · B Discretionary · C Role-based · D Rule-based · E Attribute-based = b
    - [p] Everyone in the "Accounts Payable" group gets the same finance app rights :: A Mandatory · B Discretionary · C Role-based · D Rule-based · E Attribute-based = c
    - [p] A firewall denies all traffic from 203.0.113.0/24, for every user :: A Mandatory · B Discretionary · C Role-based · D Rule-based · E Attribute-based = d
    - [p] Access allowed if department=Research AND device=managed AND location=UK :: A Mandatory · B Discretionary · C Role-based · D Rule-based · E Attribute-based = e
    - *MAC = labels and clearances set centrally, users cannot change. DAC = owner decides. RBAC = rights by job role. Rule-based = system-wide rules applied to all (ACLs, firewalls). ABAC = combine many attributes of user, resource and context. Hook: Mandatory = the military, Discretionary = the owner, Role = the job, Rule = the list, Attribute = the checklist.*
    - @4.6.ac
13. A call centre wants agents to log in to the CRM only during their 08:00-18:00 shifts. Which control is BEST?
    - **[x] Time-of-day restrictions**  - [ ] Discretionary access control  - [ ] Identity proofing  - [ ] Federation
    - *Time-of-day restrictions limit when accounts can authenticate, reducing the window for misuse of stolen credentials. DAC is owner-chosen sharing. Proofing and federation are other topics.*
    - @4.6.tod
14. A new analyst asks for domain admin "just in case" she needs it. Her job only needs read access to reports. What principle should guide the decision?
    - **[x] Least privilege**  - [ ] Separation of duties  - [ ] Implicit trust  - [ ] Defense in depth
    - *Least privilege = give only the access needed to do the job, nothing more. Separation of duties splits critical tasks between people. Implicit trust is what zero trust removes. Defense in depth layers controls.*
    - @4.6.lp
15. A large hospital has 400 job titles and thousands of staff moving between wards. Which access model is EASIEST to manage at scale while limiting rights?
    - **[x] Role-based access control**  - [ ] Discretionary access control by each file owner  - [ ] Individual permissions per user  - [ ] Mandatory access control with labels on every record
    - *RBAC maps permissions to roles, so moving staff means changing role membership, not hundreds of permissions. DAC and per-user rights do not scale and cause creep. MAC is rigid and suited to classified environments.*
    - @4.6.ac
16. A cloud provider wants to grant access to a storage bucket only when the user's project tag matches the bucket's project tag and the request comes from the corporate network. Which model fits BEST?
    - **[x] Attribute-based access control (ABAC)**  - [ ] Discretionary access control  - [ ] Mandatory access control  - [ ] Role-based access control
    - *ABAC evaluates attributes of subject, object and environment in policies (if tag matches AND network = corporate). RBAC uses only roles. MAC uses labels. DAC uses owner choice.*
    - @4.6.ac
17. During an audit, 40 active accounts belong to people who left last year. What is the BEST long-term fix?
    - **[x] Automate de-provisioning from the HR system and run periodic access reviews**  - [ ] Delete the audit finding  - [ ] Give the accounts longer passwords  - [ ] Rename the accounts to "former staff"
    - *Orphaned accounts come from manual leaver processes. Automate removal tied to HR events, and catch stragglers with attestation. Longer passwords and renaming leave usable accounts. Deleting findings hides risk.*
    - @4.6.deprov
18. A new SaaS vendor offers to sync passwords from the on-premise directory. The security team prefers SAML federation. Why is federation BETTER?
    - **[x] Credentials stay with the company IdP and only signed assertions are sent to the SaaS app**  - [ ] Federation sends passwords in plain text for speed  - [ ] Federation removes the need for any directory  - [ ] Password sync is always encrypted with SAML
    - *With federation the SP never stores or sees the password; it trusts the IdP's signed assertion, and disabling the user at the IdP blocks access everywhere. Federation does not send passwords and still relies on a directory. Password sync spreads secrets to another provider.*
    - @4.6.fed
19. A help desk can reset any user's password, including executives, without approval. What implication of permission assignment is MOST concerning?
    - **[x] Help desk staff could take over high-value accounts, so reset rights should be scoped and logged**  - [ ] Executives will forget their passwords more often  - [ ] The help desk needs domain admin to do this properly  - [ ] Password resets break SAML
    - *Permissions have implications: broad reset rights are an account takeover path (and a social engineering target). Scope them, require verification and log use. More rights for the help desk is the wrong way. Resets do not break SAML.*
    - @4.6.perm
20. A user logs in once to Windows and then reaches file shares and intranet apps without re-entering credentials, using tickets from a domain controller. What is this?
    - **[x] Single sign-on with Kerberos**  - [ ] Federation with OAuth  - [ ] Discretionary access control  - [ ] Attestation
    - *Inside an Active Directory domain, Kerberos gives SSO: the KDC issues a ticket-granting ticket, then service tickets. Federation spans organizations. DAC and attestation are other topics.*
    - @4.6.sso
21. A company merges with another firm. Staff in each need access to some of the other's apps quickly, while each keeps its own directory. What is the BEST approach?
    - **[x] Set up federation trust between the two identity providers**  - [ ] Create duplicate accounts by hand for every user in both directories  - [ ] Share one admin password between both IT teams  - [ ] Merge all users into a spreadsheet of credentials
    - *Federation lets each IdP keep authenticating its own users while the other side trusts the assertions. Manual duplicates create orphaned accounts and sync gaps. Shared admin passwords and spreadsheets break accountability and confidentiality.*
    - @4.6.fed
22. A user's OAuth access token for a reporting API is stolen. Which design choice MOST limits the damage?
    - **[x] Short-lived tokens with narrow scopes**  - [ ] Tokens that never expire  - [ ] One token with full admin scope for all APIs  - [ ] Embedding the user's password in the token
    - *OAuth tokens should be scoped to only needed permissions and expire quickly, with refresh tokens protected. Non-expiring or broad tokens give attackers long, wide access. Passwords never belong in tokens.*
    - @4.6.oauth
23. An auditor asks how a contractor's access was approved. The company can show the request, the manager's approval and the date it was granted. Which provisioning practice does this show?
    - **[x] A documented, approved access request workflow**  - [ ] Identity proofing by passport  - [ ] Time-of-day restrictions  - [ ] Mandatory access control labels
    - *Good provisioning records who asked, who approved and what was granted, so access is justified and auditable. The others do not answer how access was approved.*
    - @4.6.prov
24. A shared "scanner" service account has rights to write to every file share. Which change BEST reflects least privilege?
    - **[x] Limit it to the single scan folder it needs, and stop interactive logon for it**  - [ ] Add it to Domain Admins so it never fails  - [ ] Share its password with the help desk  - [ ] Leave it, because service accounts are exempt
    - *Service accounts need least privilege too: only the resources they use, no interactive logon, and managed credentials. Domain Admin and shared passwords are huge risks. No account is exempt.*
    - @4.6.lp

### Key facts
- **Lifecycle: provisioning, de-provisioning, permission assignments (watch for creep), identity proofing, attestation.**
- **Federation (IdP/SP trust); SSO via LDAP, OAuth (delegated authorization, tokens), SAML (XML assertions); interoperability.**
- **Access control: mandatory (labels), discretionary (owner), role-based, rule-based, attribute-based, time-of-day, least privilege.**

## Test 21 - 4.6 IAM II: MFA, Passwords, Passwordless, Privileged Access (23 Q)

1. A bank requires a password and a security question for online login. A regulator says this is not MFA. Why?
   - **[x] Both are something you know, so it is a single factor used twice**  - [ ] Security questions count as something you are  - [ ] MFA must always include a smart card  - [ ] Passwords are not an authentication factor
   - *MFA needs factors from different categories: something you know, have, are, or somewhere you are. Two knowledge items are still one factor. Questions are knowledge. MFA can use phones, keys, biometrics, not only smart cards.*
   - @4.6.factor
2. PBQ 4.6 - Factors. Classify each item.
   - [p] A PIN :: A Something you know · B Something you have · C Something you are · D Somewhere you are = a
   - [p] A FIDO2 USB key :: A Something you know · B Something you have · C Something you are · D Somewhere you are = b
   - [p] A fingerprint :: A Something you know · B Something you have · C Something you are · D Somewhere you are = c
   - [p] Login allowed only from IPs geolocated to the UK office :: A Something you know · B Something you have · C Something you are · D Somewhere you are = d
   - [p] An authenticator app code on a phone :: A Something you know · B Something you have · C Something you are · D Somewhere you are = b
   - [p] Password plus fingerprint counts as :: A Single factor · B Multifactor = b
   - *Know = PIN, password, passphrase. Have = security key, smart card, phone with a soft token. Are = biometrics. Somewhere = location via GPS or IP. Two different categories = MFA.*
   - @4.6.factor
3. A data centre wants staff to enter with a palm vein scan. Which biometric metric should the team watch so that impostors are NOT let in?
   - **[x] False acceptance rate (FAR)**  - [ ] False rejection rate (FRR)  - [ ] Crossover error rate only as a cost figure  - [ ] Mean time to repair
   - *FAR = impostors wrongly accepted (a security failure). FRR = genuine users wrongly rejected (a usability failure). The crossover error rate (CER), where they meet, compares systems; lower is better. MTTR is resilience. Hook: FAR = fraud accepted.*
   - @4.6.bio
4. A field engineer gets a 6-digit code that changes every 30 seconds from an app on her phone. What is this?
   - **[x] A soft token using TOTP**  - [ ] A hard token using a smart card chip  - [ ] Something you are  - [ ] An HOTP code that never expires
   - *Software (soft) token = an app generating time-based one-time passwords (TOTP). Hard tokens are dedicated devices (key fobs). HOTP is counter-based and stays valid until used, not time-based. A phone app is something you have.*
   - @4.6.token
5. An executive is a target of SIM swapping. Which second factor is BEST for him?
   - **[x] A hardware security key (FIDO2)**  - [ ] SMS one-time codes  - [ ] Email one-time codes to a personal account  - [ ] A security question about his first car
   - *Security keys are phishing-resistant and not tied to a phone number. SMS codes are exposed by SIM swap and interception. Email codes depend on another account's security. Questions are knowledge and often researchable.*
   - @4.6.key
6. Staff get repeated MFA push prompts at night until someone taps Approve. Which mitigation is BEST?
   - **[x] Use number matching or a FIDO2 key so a blind approval is not enough**  - [ ] Turn off MFA during the night  - [ ] Allow unlimited push requests  - [ ] Switch to a security question
   - *MFA fatigue (push bombing) relies on users approving to stop prompts. Number matching (user types the code shown at login) and phishing-resistant keys stop it, plus rate limits and alerting. The others weaken security.*
   - @4.6.mfa
7. A password policy requires 8 characters with complexity and a change every 30 days. Users now write passwords on notes. Which change BEST aligns with current guidance?
   - **[x] Require longer passphrases (e.g. 14+), check against breached lists, and change only on compromise**  - [ ] Shorten the change interval to 15 days  - [ ] Require exactly 8 characters with symbols  - [ ] Ban password managers
   - *Length beats complexity; frequent forced expiry leads to weak patterns and notes (NIST SP 800-63B guidance). Screening against breached passwords helps. Shorter intervals make it worse. Banning managers pushes reuse. Note: the exam still lists expiration and age as policy settings you should know.*
   - @4.6.pw
8. An audit shows staff cycle through several throwaway passwords in a few minutes so they can return to the one they had before. Which TWO settings stop this? (Select 2)
   - **[x] Password history (prevent reuse of the last N passwords)**  - **[x] Minimum password age**  - [ ] Maximum password length  - [ ] Account lockout threshold
   - *History blocks reuse; minimum age stops users cycling through history in one sitting. Max length does not stop reuse. Lockout limits guessing.*
   - @4.6.pw
9. A team shares 300 unique site passwords. What is the BEST way for each person to manage strong, unique passwords?
   - **[x] An enterprise password manager with MFA on the vault**  - [ ] A shared spreadsheet on the file server  - [ ] One strong password reused on all sites  - [ ] Browser autofill on shared kiosks
   - *Password managers generate and store unique, long passwords in an encrypted vault, and enterprise versions allow controlled sharing and audit. Spreadsheets and reuse expose everything at once. Shared kiosks leak credentials.*
   - @4.6.pwmgr
10. Which login method is passwordless?
    - **[x] Windows Hello for Business using a device-bound key unlocked by face or PIN**  - [ ] A password plus an SMS code  - [ ] A password plus a security question  - [ ] A long passphrase stored in a manager
    - *Passwordless = no shared secret sent to the server; a device holds a private key (FIDO2/passkeys, Windows Hello) unlocked locally by biometrics or a local PIN. The PIN never leaves the device. The others still use passwords.*
    - @4.6.pwless
11. Why are passkeys (FIDO2) highly resistant to phishing?
    - **[x] The key is bound to the real site's origin, so a fake domain cannot get a valid signature**  - [ ] They send the password faster than an attacker can read it  - [ ] They rely on SMS delivery  - [ ] They are stored on the server in plain text
    - *FIDO2/WebAuthn uses public key crypto: the private key stays on the device and signs a challenge only for the registered origin. A lookalike site gets nothing reusable. There is no password, no SMS, and the server stores only the public key.*
    - @4.6.pwless
12. A sysadmin needs domain admin for a two-hour change window. Under PAM, how should this work?
    - **[x] Just-in-time elevation that is approved, logged and automatically removed after the window**  - [ ] Permanent domain admin "for convenience"  - [ ] Using a colleague's admin account  - [ ] Adding his normal account to Domain Admins and removing it next audit
    - *JIT permissions grant privilege only when needed and only for a set time, reducing standing privileges an attacker could steal. Permanent rights and borrowed accounts break least privilege and accountability.*
    - @4.6.jit
13. Root passwords for 200 Linux servers are in a spreadsheet. What PAM capability BEST fixes this?
    - **[x] Password vaulting with check-out, automatic rotation and session recording**  - [ ] Emailing the spreadsheet only to admins  - [ ] Using the same root password on all servers  - [ ] Printing the passwords and locking them in a drawer
    - *Password vaulting stores privileged credentials in a secure vault; admins check them out, use is logged, and passwords rotate after use. The other options keep shared, static secrets.*
    - @4.6.vault
14. A CI pipeline needs cloud credentials to deploy. Which approach BEST reduces risk if the pipeline is compromised?
    - **[x] Ephemeral credentials issued per job that expire in minutes**  - [ ] A long-lived access key in the repository  - [ ] The cloud root account's password  - [ ] A key that is rotated once a year
    - *Ephemeral credentials are short-lived and created on demand, so a stolen one is soon useless. Long-lived or yearly-rotated keys give lasting access. Root should never be used by automation.*
    - @4.6.ephem
15. An admin logs in daily with an account that is a domain admin, and uses it to read email. What is the BEST change?
    - **[x] Separate a standard daily account from an admin account used only for admin tasks**  - [ ] Keep one account but add a longer password  - [ ] Disable email for admins  - [ ] Give all staff admin so it is consistent
    - *Privileged accounts should be used only for privileged work; phishing a daily-use admin account gives instant domain control. A longer password does not stop malware running as admin. The other options are impractical or worse.*
    - @4.6.pam
16. A retailer's VPN accepts a password and then a push to a phone only if the phone is in the same country as the login. Which factor does location add?
    - **[x] Somewhere you are**  - [ ] Something you are  - [ ] Something you know  - [ ] Something you have
    - *Location (GPS, IP geolocation) = somewhere you are, used as an extra condition or in risk-based decisions. The phone is the "have" factor; location is an attribute of it.*
    - @4.6.factor
17. A company issues employees smart cards with certificates for laptop login. Which implementation is this, and what is the second factor usually added?
    - **[x] A hard token (smart card); a PIN to unlock it**  - [ ] A soft token; a fingerprint  - [ ] A biometric; a password  - [ ] Somewhere you are; a GPS fix
    - *Smart cards (like PIV/CAC) are hard tokens holding a private key; a PIN (know) unlocks the card (have), making MFA. The other pairings misclassify the card.*
    - @4.6.token
18. PBQ 4.6 - PAM toolkit. Pick the BEST tool for each need.
    - [p] Admin rights for one hour, then removed :: A Just-in-time permissions · B Password vaulting · C Ephemeral credentials = a
    - [p] Store the shared firewall admin password and rotate it after each use :: A Just-in-time permissions · B Password vaulting · C Ephemeral credentials = b
    - [p] A container gets a cloud token valid for 15 minutes, created at start-up :: A Just-in-time permissions · B Password vaulting · C Ephemeral credentials = c
    - [p] Attacker steals a vaulted password that has since rotated. Its value is :: A Useless · B Still valid forever = a
    - *JIT = time-limited elevation of an identity. Vaulting = secure storage and rotation of existing privileged secrets. Ephemeral = credentials created on demand that expire quickly. Rotation makes stolen copies stale.*
    - @4.6.pam
19. An account lockout of 3 attempts lets an attacker lock out every user by guessing wrongly. What is the BEST balance?
    - **[x] A moderate threshold with a lockout timer, plus MFA and monitoring for spraying**  - [ ] No lockout at all  - [ ] Permanent lockout after one failure  - [ ] Disable logging of failed attempts
    - *Lockouts slow brute force but low thresholds enable denial of service. Combine a sensible threshold and duration with MFA and alerts. No lockout invites guessing. One-failure permanent lockout is unworkable. Disabling logs hides attacks.*
    - @4.6.pw
20. Which MFA implementation is the MOST phishing-resistant?
    - **[x] FIDO2 security key**  - [ ] SMS code  - [ ] TOTP authenticator code  - [ ] Push approval without number matching
    - *Security keys use origin-bound public key crypto, so a phishing site cannot replay them. TOTP and SMS codes can be typed into a fake site and relayed. Plain push is vulnerable to fatigue.*
    - @4.6.key
21. A vendor support engineer needs to reach a production database once a month. What is the BEST PAM approach?
    - **[x] Brokered access through a PAM gateway with approval, a vaulted credential and recorded session**  - [ ] Give the vendor a permanent VPN and the DBA password  - [ ] Create a shared vendor account with no expiry  - [ ] Email the password before each session
    - *PAM for third parties: approved, time-bound sessions, credentials never revealed, and recording for audit. Permanent, shared or emailed credentials are the classic supply chain breach path.*
    - @4.6.vault
22. Users must sign in with MFA every time, which annoys staff in the secure office. Which approach BEST keeps security while reducing friction?
    - **[x] Conditional (risk-based) access that steps up MFA for unusual location, device or behaviour**  - [ ] Remove MFA for everyone in the office  - [ ] Allow "remember this device" forever on shared PCs  - [ ] Replace MFA with a longer password
    - *Adaptive or conditional access weighs context (managed device, known location) and asks for more factors when risk rises. Removing MFA or remembering shared devices forever weakens controls. A longer password is still one factor.*
    - @1.2.zt
23. Which statement BEST describes a hard token compared with a soft token?
    - **[x] A hard token is a dedicated physical device; a soft token is an app on a general device such as a phone**  - [ ] A hard token is a password; a soft token is a fingerprint  - [ ] Hard tokens never expire; soft tokens expire daily  - [ ] Soft tokens cannot generate one-time passwords
    - *Hard = key fob, smart card, USB key. Soft = authenticator app. Both are something you have and both can generate OTPs. Passwords and fingerprints are other factor types.*
    - @4.6.token

### Key facts
- **Factors: know, have, are, somewhere you are. Implementations: biometrics (FAR, FRR, CER), hard/soft tokens (TOTP, HOTP), security keys (FIDO2).**
- **Passwords: length, complexity, reuse/history, expiration, age; password managers; passwordless (passkeys, Windows Hello).**
- **PAM: just-in-time permissions, password vaulting, ephemeral credentials.**

## Test 22 - 4.7 + 4.8 + 4.9 Automation, Incident Response, Forensics, Investigation Data Sources (29 Q)

1. A company's onboarding script creates accounts, assigns groups by role and emails the manager, cutting setup from two days to ten minutes. Which TWO automation benefits are MOST clearly shown? (Select 2)
   - **[x] Efficiency/time saving**  - **[x] Enforcing consistent baselines for access**  - [ ] Removing all technical debt  - [ ] Eliminating any single point of failure
   - *4.7 benefits: efficiency, enforcing baselines, standard infrastructure configurations, scaling securely, employee retention, reaction time, workforce multiplier. Automation can add technical debt and become a single point of failure, so those are considerations, not benefits.*
   - @4.7.ben
2. A cloud team's pipeline blocks any deployment that would create a storage bucket open to the public. What is this control?
   - **[x] A guard rail**  - [ ] Ticket escalation  - [ ] Employee retention  - [ ] A legal hold
   - *Guard rails = automated policies that stop unsafe configurations before they happen while letting teams move quickly. Escalation routes tickets. Retention is a benefit. Legal hold is forensics. Analogy: the barrier on a mountain road.*
   - @4.7.guard
3. When the SIEM detects a confirmed phishing click, a SOAR playbook disables the user's sessions, opens a ticket, and pages on-call if it is not acknowledged in 15 minutes. Which use cases are shown?
   - **[x] Disabling access, ticket creation and escalation**  - [ ] Resource provisioning and continuous integration  - [ ] User provisioning and guard rails  - [ ] Security groups and employee retention
   - *4.7 use cases: user and resource provisioning, guard rails, security groups, ticket creation, escalation, enabling/disabling services and access, CI and testing, integrations and APIs. This flow disables, tickets and escalates. Faster response also shows the "reaction time" benefit.*
   - @4.7.use
4. A single engineer wrote all the automation scripts and has now left. Nobody understands them and they break after an OS update. Which TWO considerations were overlooked? (Select 2)
   - **[x] Ongoing supportability**  - **[x] Technical debt**  - [ ] Workforce multiplier  - [ ] Scaling securely
   - *Considerations: complexity, cost, single point of failure, technical debt, ongoing supportability. Undocumented scripts built by one person are hard to support and pile up debt. Workforce multiplier and scaling are benefits.*
   - @4.7.cons
5. A developer pushes code and the pipeline automatically runs unit tests, a SAST scan and a dependency check before merging. Which use case is this?
   - **[x] Continuous integration and testing**  - [ ] User provisioning  - [ ] Ticket escalation  - [ ] Legal hold
   - *CI automatically builds and tests every change, catching flaws early. Adding security scans is a classic DevSecOps use. The other options are unrelated workflows.*
   - @4.7.use
6. A firewall vendor exposes a REST API. The SOC's threat intel platform uses it to block new malicious IPs within seconds. What is this an example of?
   - **[x] Integrations and APIs for automated response**  - [ ] Manual change management  - [ ] Root cause analysis  - [ ] Data retention
   - *APIs let tools talk to each other so automation can act across products, improving reaction time and acting as a workforce multiplier. The other options do not describe tool integration.*
   - @4.7.api
7. A SOC automates triage but every alert now runs through one SOAR server. If it fails, nothing is processed. Which consideration is this?
   - **[x] Single point of failure**  - [ ] Employee retention  - [ ] Enforcing baselines  - [ ] Efficiency
   - *Automation can concentrate risk: if the engine fails, every dependent process stops. Plan redundancy and manual fallback. The others are benefits.*
   - @4.7.cons
8. PBQ 4.8 - IR process order. Put the incident response phases in order for a ransomware case.
   - [p] Step 1: IR plan, tools, jump bag and contact list ready before anything happens :: A Preparation · B Detection · C Analysis · D Containment · E Eradication · F Recovery · G Lessons learned = a
   - [p] Step 2: EDR alerts on mass file renames :: A Preparation · B Detection · C Analysis · D Containment · E Eradication · F Recovery · G Lessons learned = b
   - [p] Step 3: Team confirms it is ransomware and scopes affected hosts :: A Preparation · B Detection · C Analysis · D Containment · E Eradication · F Recovery · G Lessons learned = c
   - [p] Step 4: Infected hosts isolated from the network :: A Preparation · B Detection · C Analysis · D Containment · E Eradication · F Recovery · G Lessons learned = d
   - [p] Step 5: Malware and persistence removed, exploited flaw patched :: A Preparation · B Detection · C Analysis · D Containment · E Eradication · F Recovery · G Lessons learned = e
   - [p] Step 6: Restore from clean backups and monitor :: A Preparation · B Detection · C Analysis · D Containment · E Eradication · F Recovery · G Lessons learned = f
   - [p] Step 7: Meeting to update the plan :: A Preparation · B Detection · C Analysis · D Containment · E Eradication · F Recovery · G Lessons learned = g
   - *Exam order: preparation, detection, analysis, containment, eradication, recovery, lessons learned. Hook: "Please Don't Ask Cats Every Rainy Lunch". Contain before you clean, clean before you restore.*
   - @4.8.ir
9. A web server is confirmed compromised and the attacker is still connected. What is the BEST next step?
   - **[x] Contain it by isolating the server while preserving evidence**  - [ ] Immediately wipe and reinstall the server  - [ ] Hold a lessons-learned meeting  - [ ] Restore it from last night's backup in place
   - *Containment comes before eradication and recovery: limit spread and damage. Wiping first destroys evidence and may miss other footholds. Lessons learned is last. Restoring onto a live compromise may be reinfected.*
   - @4.8.contain
10. After an incident, the team restores servers but the same attacker is back in a week via a web shell they missed. Which phase was incomplete?
    - **[x] Eradication**  - [ ] Preparation  - [ ] Detection  - [ ] Lessons learned
    - *Eradication removes all malware, backdoors and persistence and fixes the entry point. A surviving web shell means eradication failed, and recovery happened too soon.*
    - @4.8.erad
11. After a ransomware case is closed, the IR lead books a review with IT, legal and comms to walk through the timeline and decide which runbooks change. What is the MAIN goal of this session?
    - **[x] Improve future response and prevent recurrence**  - [ ] Assign blame to the employee who clicked the link  - [ ] Collect evidence for court  - [ ] Restore services
    - *Lessons learned (post-incident review) feeds improvements back into preparation. Blame discourages reporting. Evidence and recovery belong to earlier phases.*
    - @4.8.lessons
12. A team wants to rehearse its response to a data breach by talking through a scenario around a table, without touching systems. What is this?
    - **[x] A tabletop exercise**  - [ ] A full simulation  - [ ] A penetration test  - [ ] Threat hunting
    - *Tabletop = discussion-based walk-through of a scenario; cheap and low risk. A simulation acts out the incident with systems or realistic injects (for example a fake phishing campaign). Pen tests attack real systems. Threat hunting looks for live threats.*
    - @4.8.test
13. New SOC analysts have never used the IR playbooks. Which IR element is MOST directly addressed by running them through the tools and procedures?
    - **[x] Training**  - [ ] Root cause analysis  - [ ] E-discovery  - [ ] Legal hold
    - *Training ensures everyone knows their role, tools and procedures before a real incident. RCA, e-discovery and legal hold are investigation and legal tasks.*
    - @4.8.train
14. After an outage caused by malware, the team asks "why" repeatedly and finds a missing patch, then a broken patch approval process. What technique is this?
    - **[x] Root cause analysis**  - [ ] Threat hunting  - [ ] Tabletop exercise  - [ ] Chain of custody
    - *RCA digs past symptoms to the underlying cause (5 whys, fishbone) so the fix stops recurrence. Hunting looks for undetected threats. Tabletops rehearse plans. Chain of custody tracks evidence.*
    - @4.8.rca
15. No alert has fired, but an analyst uses new threat intel about an APT's techniques to search EDR data for signs of that group. What is this?
    - **[x] Threat hunting**  - [ ] Incident containment  - [ ] Alert tuning  - [ ] Root cause analysis
    - *Threat hunting = proactive, hypothesis-driven search for threats that evaded existing detections, often using intel and frameworks like MITRE ATT&CK. Containment follows a known incident. Tuning adjusts rules. RCA explains a past event.*
    - @4.8.hunt
16. A company receives notice of a lawsuit about a former employee. Counsel instructs IT to stop the routine deletion of that employee's mailbox. What is this?
    - **[x] A legal hold**  - [ ] Data sanitization  - [ ] Chain of custody  - [ ] Containment
    - *Legal hold = preservation order that suspends normal retention and deletion for relevant data once litigation is expected. Sanitization destroys data. Chain of custody records who handles evidence. Containment is IR.*
    - @4.8.hold
17. An investigator seizes a laptop. Which record BEST ensures the evidence will be accepted in court?
    - **[x] Chain of custody showing everyone who handled it, when and why**  - [ ] A lessons-learned report  - [ ] A heat map of the office  - [ ] The laptop's warranty records
    - *Chain of custody documents every transfer and access, proving the evidence was not tampered with. Gaps can make evidence inadmissible. The others do not track handling.*
    - @4.8.coc
18. A responder is about to collect evidence from a running, compromised server. Which should be captured FIRST, by order of volatility?
    - **[x] CPU registers and cache**  - [ ] The hard drive image  - [ ] Archived backup tapes  - [ ] Printed configuration documents
    - *Acquisition follows order of volatility: most volatile first (registers, cache, RAM, network connections and running processes), then disk, then remote logs and archives. Pulling the plug first loses memory evidence such as decryption keys.*
    - @4.8.acq
19. Before analyzing a disk image, the examiner hashes both the original drive and the image and finds them identical, then works only on the copy behind a write blocker. Which forensic principle is this?
    - **[x] Preservation of evidence integrity**  - [ ] E-discovery  - [ ] Root cause analysis  - [ ] Recovery
    - *Preservation = protect evidence from change: write blockers, working copies, hashes (such as SHA-256) to prove integrity, secure storage. E-discovery is the legal process of finding and producing electronic data. RCA and recovery are IR topics.*
    - @4.8.pres
20. A court case requires the company to search, review and hand over all emails mentioning a contract. Which process is this?
    - **[x] E-discovery**  - [ ] Threat hunting  - [ ] Data retention  - [ ] Incident containment
    - *E-discovery = identifying, collecting and producing electronically stored information for legal proceedings. Hunting finds threats. Retention keeps data for set periods. Containment limits an incident.*
    - @4.8.ediscovery
21. At the end of a forensic investigation, which output is MOST important for management and legal teams?
    - **[x] A clear report of findings, methods, timeline and evidence references**  - [ ] The raw disk image emailed to all staff  - [ ] A list of the investigator's tools only  - [ ] Deleting the evidence once the case closes
    - *Forensic reporting documents what was found, how, and the supporting evidence, in a way others can verify. Sharing raw images leaks data. A tool list alone is not findings. Evidence must be kept per legal hold and retention.*
    - @4.8.report
22. An analyst investigating a suspected scan from 198.51.100.77 wants to see which ports were blocked or allowed at the perimeter. Which log source is BEST?
    - **[x] Firewall logs**  - [ ] Application logs on the web server  - [ ] Endpoint antivirus logs  - [ ] Metadata of an email attachment
    - *Firewall logs record allowed and denied connections with source, destination, ports and time, ideal for scans and lateral movement. Application logs show what the app did. AV logs show malware. Email metadata is about messages.*
    - @4.9.fw
23. A user says she never logged in at 23:40, but the account shows successful logons. Which source BEST confirms when and from where the logon happened on her Windows PC?
    - **[x] OS-specific security logs (Windows Security event log)**  - [ ] NetFlow summaries  - [ ] The vulnerability scan report  - [ ] The web proxy cache
    - *OS security logs record logons (Windows event ID 4624 success, 4625 failure), privilege use and policy changes. Linux equivalents are auth logs. NetFlow lacks user identity. Scan reports show flaws. Proxy cache stores web content.*
    - @4.9.os
24. A file-sharing app shows a user exported 2,000 records via the "Download all" feature. Which log source recorded this action?
    - **[x] Application logs**  - [ ] IPS logs  - [ ] Switch interface logs  - [ ] OS boot logs
    - *Application logs capture events inside the app: logins, exports, errors, admin changes. IPS logs show blocked attacks. Network device logs show link state and traffic. Boot logs show startup.*
    - @4.9.app
25. An investigator checks a leaked document's author, creation date and the GPS location in an attached photo. Which data type is this?
    - **[x] Metadata**  - [ ] A packet capture  - [ ] A dashboard  - [ ] A firewall log
    - *Metadata = data about data: file author and timestamps, email headers (sender, route), photo EXIF (camera, GPS). Useful for timelines and attribution. The others are separate data sources.*
    - @4.9.meta
26. The SOC needs to know exactly what data an attacker sent in a suspicious session, including the payload. Which source is BEST?
    - **[x] A packet capture (PCAP)**  - [ ] NetFlow records  - [ ] An automated weekly report  - [ ] A dashboard summary
    - *Packet captures record full traffic, including payloads (if not encrypted), for deep analysis in tools like Wireshark. NetFlow has metadata only. Reports and dashboards summarise; they do not hold the raw packets.*
    - @4.9.pcap
27. PBQ 4.9 - Data sources. For each question, pick the BEST source.
    - [p] Was the exploit attempt against the web server blocked or only detected :: A IPS/IDS logs · B Endpoint logs · C Network logs · D Vulnerability scans · E Dashboards = a
    - [p] Which process on a laptop spawned PowerShell at 02:13 :: A IPS/IDS logs · B Endpoint logs · C Network logs · D Vulnerability scans · E Dashboards = b
    - [p] Did the switch port the server uses go down at 02:15 :: A IPS/IDS logs · B Endpoint logs · C Network logs · D Vulnerability scans · E Dashboards = c
    - [p] Was the server already missing the patch for the exploited CVE :: A IPS/IDS logs · B Endpoint logs · C Network logs · D Vulnerability scans · E Dashboards = d
    - [p] Give the CISO a live view of open incidents by severity :: A IPS/IDS logs · B Endpoint logs · C Network logs · D Vulnerability scans · E Dashboards = e
    - *IPS/IDS logs show detections and the action taken. Endpoint (EDR) logs show processes, files and registry on a host. Network logs come from routers, switches, VPNs and wireless. Vulnerability scans show known weaknesses before the incident. Dashboards give a real-time summary view; automated reports deliver scheduled summaries.*
    - @4.9.src
28. A CIO wants a weekly email summarising failed logins, top blocked sites and patch status, without anyone building it by hand. Which data source fits BEST?
    - **[x] Automated reports from the SIEM and security tools**  - [ ] A packet capture  - [ ] A forensic disk image  - [ ] Raw firewall logs
    - *Automated reports are scheduled summaries that tools generate and send. Dashboards are the live, on-screen version. PCAPs, disk images and raw logs are detailed evidence, not executive summaries.*
    - @4.9.src

29. PBQ 4.7 - Automation and orchestration. Classify each item.
    - [p] A script spins up VMs and storage for a new project from a template :: A User provisioning · B Resource provisioning · C Security groups = b
    - [p] Automation adds new servers to the right firewall rule set by tag :: A User provisioning · B Resource provisioning · C Security groups = c
    - [p] Every new server built by code has identical approved settings :: A Standard infrastructure configurations · B Technical debt · C Cost = a
    - [p] Automation lets the team add 500 hosts without lowering security :: A Scaling in a secure manner · B Complexity · C Single point of failure = a
    - [p] Analysts spend less time on boring repetitive tasks and are less likely to quit :: A Employee retention · B Workforce multiplier · C Cost = a
    - [p] Three analysts handle the work of ten thanks to playbooks :: A Employee retention · B Workforce multiplier · C Reaction time = b
    - [p] The SOAR licence and build effort exceed the budget :: A Cost · B Complexity · C Efficiency = a
    - [p] Playbooks have so many branches that nobody can predict what they will do :: A Cost · B Complexity · C Enforcing baselines = b
    - *Use cases: user provisioning (accounts), resource provisioning (infrastructure), security groups (access by membership or tag). Benefits: standard infrastructure configurations, scaling in a secure manner, employee retention (less toil), workforce multiplier (fewer people do more), reaction time. Considerations: cost and complexity, alongside single point of failure, technical debt and ongoing supportability.*
    - @4.7.pbq

### Key facts
- **4.7 use cases: user/resource provisioning, guard rails, security groups, ticket creation, escalation, enable/disable services and access, CI/testing, integrations/APIs. Benefits: efficiency, enforce baselines, standard configs, scale securely, retention, reaction time, workforce multiplier. Considerations: complexity, cost, SPOF, technical debt, supportability.**
- **IR: preparation, detection, analysis, containment, eradication, recovery, lessons learned. Training; testing (tabletop, simulation); RCA; threat hunting.**
- **Forensics: legal hold, chain of custody, acquisition (order of volatility), reporting, preservation (hashes, write blockers), e-discovery.**
- **4.9 log data: firewall, application, endpoint, OS security, IPS/IDS, network, metadata. Data sources: vulnerability scans, automated reports, dashboards, packet captures.**

## Test 23 - 5.1 Security Governance: Policies, Standards, Procedures, Roles (27 Q)

1. A marketing intern streams games on a company laptop overnight and installs a crypto miner "to learn". HR finds nothing in his signed onboarding pack forbids it. Which document should be updated FIRST to close this gap?
   - **[x] The acceptable use policy**  - [ ] The non-disclosure agreement  - [ ] The incident response plan  - [ ] The data retention standard
   - *AUP = what users may and may not do with company systems; users sign it. Hook: house rules for the kit. Analogy: rules posted at a gym. NDA is signed at hiring too, but covers secrecy, not system use. The IR plan handles incidents after they happen. Retention covers how long data is kept.*
   - @5.1.policy
2. A ransomware outbreak hits a law firm. Staff argue about who may call the insurer, who talks to the press and when to involve police. Which policy was MOST clearly missing?
   - **[x] Incident response policy**  - [ ] Business continuity policy  - [ ] Change management policy  - [ ] Software development lifecycle policy
   - *The IR policy sets authority, roles, communication and escalation during a security incident. BC tempts: it keeps the business running in a disruption, but does not assign who speaks to police about an attack. Change management governs planned changes. SDLC governs building software.*
   - @5.1.policy
3. A developer pushes code straight to production with no security review, citing deadlines. Leadership wants a top-level rule that security testing is required before any release. Which policy BEST fits?
   - **[x] Software development lifecycle (SDLC) policy**  - [ ] Acceptable use policy  - [ ] Disaster recovery policy  - [ ] Information security policy only
   - *SDLC policy = how software is planned, coded, tested and released, including security gates. Analogy: a factory rule that no product ships without inspection. The general infosec policy states overall intent but rarely the dev pipeline gates. AUP governs users; DR restores after a disaster.*
   - @5.1.policy
4. The security team publishes advice: "consider using a password manager and enable passkeys where offered." Nobody is disciplined for ignoring it. What kind of document is this?
   - **[x] Guideline**  - [ ] Standard  - [ ] Procedure  - [ ] Policy
   - *Guideline = recommended, not mandatory. Hook: guidelines guide, they do not command. Analogy: a travel guide suggests restaurants. Standards and policies are mandatory; a procedure is ordered steps.*
   - @5.1.guide
5. Auditors find staff treat "remote workers should lock screens in public" as optional. Management wants it enforceable with sanctions. What is the BEST change?
   - **[x] Move the requirement from the guideline into a standard or policy**  - [ ] Reword the guideline more strongly  - [ ] Add it to the onboarding procedure as a tip  - [ ] Email the guideline again
   - *Only mandatory documents (policy, standard) can be enforced. A guideline, however strongly worded, remains advice. A tip in a procedure is still advice. Re-sending changes nothing.*
   - @5.1.guide
6. A bank's policy says "accounts must be protected by strong authentication." An engineer asks what "strong" means in numbers. Which document should answer?
   - **[x] Password and authentication standard**  - [ ] Acceptable use policy  - [ ] Password guideline  - [ ] Onboarding procedure
   - *Standards turn policy intent into specific, measurable mandatory values, such as length, lockout and MFA. Hook: standards give the numbers. Analogy: building code heights for handrails. A guideline would be optional; AUP covers user behaviour; onboarding is a process.*
   - @5.1.std
7. A cloud team asks which algorithms and key lengths are allowed for data at rest. Which document is MOST appropriate?
   - **[x] Encryption standard**  - [ ] Information security policy  - [ ] Data retention guideline  - [ ] Change management procedure
   - *An encryption standard lists approved algorithms, key sizes and key handling, mandatory and specific. The infosec policy says data must be protected but not which cipher. Retention covers how long, not how.*
   - @5.1.std
8. A data centre manager must define badge types, visitor escort rules and which zones need two-factor entry. Which document type is she writing?
   - **[x] Physical security standard**  - [ ] Access control guideline  - [ ] Business continuity policy  - [ ] Visitor onboarding procedure
   - *Physical security standards set mandatory requirements for facilities: zones, badges, escorts. Access control standards cover logical access rules (least privilege, review frequency). Guideline is optional; BC is about keeping operations running.*
   - @5.1.std
9. A hospital hires 40 nurses each month. Some start without EHR access, others get a previous nurse's account. What would BEST fix this?
   - **[x] A documented onboarding procedure that provisions access by role**  - [ ] A stronger acceptable use policy  - [ ] A new encryption standard  - [ ] A guideline asking managers to be careful
   - *Procedure = repeatable steps; onboarding provisions the right access, equipment and training every time. Analogy: a recipe gives the same cake every time. AUP is about behaviour, not provisioning; a guideline is optional.*
   - @5.1.proc
10. During a phishing incident, a junior analyst follows a pre-written decision flow: check the headers, pull the email from all mailboxes, block the sender, reset the clicked user's password. What is this document?
   - **[x] Playbook**  - [ ] Policy  - [ ] Standard  - [ ] Guideline
   - *A playbook is a procedure with step-by-step actions for a specific incident type. Hook: play by play. Policy states who has authority, not the steps; a standard sets values; a guideline is optional.*
   - @5.1.proc
11. A change board approves a firewall rule change. Which part of the change management PROCEDURE should be completed BEFORE the change is made?
   - **[x] A tested backout plan and an agreed maintenance window**  - [ ] A lessons-learned report  - [ ] A new acceptable use policy  - [ ] An updated vendor SLA
   - *The change procedure covers the steps: request, impact analysis, approval, test, backout plan, window, then implement and document. Lessons learned comes after an incident. AUP and SLA are unrelated to this change.*
   - @5.1.proc
12. A US retailer opens a store in Germany. Which external consideration MOST directly forces changes to how it handles staff data there?
   - **[x] Global regulation such as the EU GDPR**  - [ ] The retailer's own password standard  - [ ] Industry best-practice blogs  - [ ] The retailer's board meeting schedule
   - *External considerations: regulatory, legal, industry, local/regional, national and global. GDPR (General Data Protection Regulation) spans many countries, so the objectives treat it as a global consideration. Internal standards and board meetings are internal. Blogs are not binding.*
   - @5.1.ext
13. A small online shop that takes card payments must follow strict rules on card data even though no law names it. Which external consideration is this?
   - **[x] Industry requirement (PCI DSS)**  - [ ] National law  - [ ] Local building code  - [ ] Internal guideline
   - *PCI DSS (Payment Card Industry Data Security Standard) is set by the card brands and enforced by contract, so it is an industry consideration. Hook: industry = rules from your sector, not a parliament. National law tempts, but PCI DSS is not legislation.*
   - @5.1.ext
14. A city government requires all contractors handling resident data to store it within the state. The vendor's policy says data may be stored anywhere. What should the vendor do?
   - **[x] Follow the local requirement, since external legal obligations override internal policy**  - [ ] Ignore it; internal policy takes priority  - [ ] Ask the city to change its law  - [ ] Store half the data locally
   - *Local/regional and national legal requirements must be met; internal policies should be updated to reflect them. Hook: the law sets the floor. Asking for a law change is not a control. Half-compliance is non-compliance.*
   - @5.1.ext
15. A company's remote work policy was written in 2019 and has never been reviewed. It does not mention personal devices or home Wi-Fi. What should governance require?
   - **[x] A scheduled review cycle, plus reviews after major changes**  - [ ] Delete the policy until a new one is needed  - [ ] Let each manager write their own version  - [ ] Review only after an audit failure
   - *Monitoring and revision: policies are reviewed on a schedule (often yearly) and when laws, technology or incidents change. Analogy: servicing a car on a schedule, not only after a breakdown. Waiting for an audit failure is reactive; per-manager versions break consistency.*
   - @5.1.revise
16. After a breach, the review shows the incident response procedure skipped a legal hold step. What is the BEST governance action?
   - **[x] Update the procedure and record the revision with an owner and date**  - [ ] Train staff on the old version again  - [ ] Write a new guideline instead  - [ ] Wait for the next yearly review
   - *Lessons learned feed revision; changes are tracked so everyone uses the current version. Retraining on a faulty version repeats the gap. A guideline is optional. Waiting leaves a known gap open.*
   - @5.1.revise
17. A multinational wants major security decisions approved by senior directors who answer to shareholders. Which governance structure fits?
   - **[x] Board of directors**  - [ ] Change advisory board  - [ ] Help desk team  - [ ] Data custodians
   - *Boards set direction and oversee executives on behalf of owners. A change advisory board (a committee) approves IT changes, not strategy. Custodians run day-to-day data handling.*
   - @5.1.gov
18. Each business unit of a conglomerate picks its own security tools and policies. Audits show inconsistent controls but fast local decisions. Which governance model is this?
   - **[x] Decentralized**  - [ ] Centralized  - [ ] Government entity  - [ ] Federated identity
   - *Decentralized = authority spread to units; fast and local but inconsistent. Centralized = one team decides for all; consistent but slower. Federated identity is an IAM term, not governance.*
   - @5.1.gov
19. A public water utility's security programme is overseen by a state agency that sets rules and inspects it. Which governance structure is involved?
   - **[x] Government entity**  - [ ] Board of directors  - [ ] Internal committee  - [ ] Decentralized model
   - *Government entities govern public bodies and regulated sectors through rules and oversight. A board or committee is internal. Decentralized describes where authority sits, not who oversees.*
   - @5.1.gov
20. A sales VP is the senior executive ultimately responsible for all customer relationship data. Day to day, other staff keep it accurate, labelled and backed up. What is the VP's role?
   - **[x] Data owner**  - [ ] Data custodian  - [ ] Data processor  - [ ] Data steward
   - *Owner = senior person ultimately responsible for the data (e.g. the head of sales owns customer records, the finance director owns financial records). Custodian/steward = handles security, accuracy and sensitivity labels day to day. Analogy: the homeowner is responsible, the caretaker looks after the house. Processor acts for a controller under privacy law.*
   - @5.1.roles
21. A data quality lead checks that customer records are accurate, labelled correctly and used per policy, but does not own the data. Which role is this?
   - **[x] Data steward**  - [ ] Data owner  - [ ] Data controller  - [ ] System administrator
   - *Steward (often treated as one role with custodian) = keeps data accurate, private and compliant, assigns sensitivity labels and maps them to access, on the owner's behalf. Owner is the senior person ultimately responsible. Controller decides how data is used. A sysadmin is not a data role.*
   - @5.1.roles
22. A gym chain decides why and how members' health data is collected. It hires a cloud analytics firm that processes the data only on its instructions. Which statement is correct?
   - **[x] The gym is the controller; the analytics firm is the processor**  - [ ] The analytics firm is the controller  - [ ] Both are processors  - [ ] The members are the controllers
   - *Controller = decides purpose and means; processor = handles data on the controller's behalf. Hook: controller commands, processor performs. Members are the data subjects.*
   - @5.1.roles
23. PBQ 5.1 - Governance documents. Classify each item. ¶  1  "Leadership commits to safeguarding customer trust and assigns security duties to every manager" ¶  2  "Public web services accept TLS 1.2 or newer, nothing older" ¶  3  "For a new hire: 1) create directory account, 2) add role groups, 3) issue laptop, 4) enrol MFA" ¶  4  "It is a good idea to keep a privacy screen on your laptop when travelling"
   - [p] Item 1 :: A Policy · B Standard · C Procedure · D Guideline = a
   - [p] Item 2 :: A Policy · B Standard · C Procedure · D Guideline = b
   - [p] Item 3 :: A Policy · B Standard · C Procedure · D Guideline = c
   - [p] Item 4 :: A Policy · B Standard · C Procedure · D Guideline = d
   - *1: high-level intent, so policy. 2: a specific mandatory value, so standard. 3: ordered steps, so procedure (onboarding). 4: "a good idea" = optional, so guideline. Hook: policy = why, standard = how much, procedure = how, guideline = suggestion.*
   - @5.1.std
24. PBQ 5.1 - Data roles at a clinic that uses a cloud billing provider. Pick each role. ¶  1  A patient who asks what billing data is held about him ¶  2  The billing provider, which may only run invoices the clinic requests ¶  3  The practice manager, the senior person ultimately responsible for all billing records ¶  4  The clinic as an organisation, which chose to collect insurance details and for what ¶  5  The sysadmin who configures nightly backups and share permissions
   - [p] Party 1 :: A Data subject · B Processor · C Custodian · D Controller · E Owner = a
   - [p] Party 2 :: A Data subject · B Processor · C Custodian · D Controller · E Owner = b
   - [p] Party 3 :: A Data subject · B Processor · C Custodian · D Controller · E Owner = e
   - [p] Party 4 :: A Data subject · B Processor · C Custodian · D Controller · E Owner = d
   - [p] Party 5 :: A Data subject · B Processor · C Custodian · D Controller · E Owner = c
   - *1: the person the data is about, so data subject. 2: acts only on instructions, so processor. 3: senior and ultimately responsible, so owner. 4: decides purpose and means, so controller. 5: implements technical care, so custodian.*
   - @5.1.roles

25. PBQ 5.1 - Policy and standard types. Pick the document for each need. ¶  1  Top-level statement of the organization's security goals and responsibilities ¶  2  How the business keeps critical operations running during a disruption ¶  3  How IT systems and data are restored after a site is lost ¶  4  Rule that every production change needs approval and a backout plan ¶  5  Mandatory least privilege and quarterly access reviews
   - [p] Need 1 :: A Information security policy · B Business continuity policy · C Disaster recovery policy · D Change management policy · E Access control standard = a
   - [p] Need 2 :: A Information security policy · B Business continuity policy · C Disaster recovery policy · D Change management policy · E Access control standard = b
   - [p] Need 3 :: A Information security policy · B Business continuity policy · C Disaster recovery policy · D Change management policy · E Access control standard = c
   - [p] Need 4 :: A Information security policy · B Business continuity policy · C Disaster recovery policy · D Change management policy · E Access control standard = d
   - [p] Need 5 :: A Information security policy · B Business continuity policy · C Disaster recovery policy · D Change management policy · E Access control standard = e
   - *1: the umbrella intent is the information security policy. 2: keeping the business running is business continuity. 3: restoring IT after a disaster is disaster recovery. 4: governing changes is change management policy (the procedure holds the steps). 5: specific mandatory access rules are an access control standard.*
   - @5.1.policy
26. PBQ 5.1 - Governance structures and external considerations. Pick the best match.
   - [p] A cross-department group meets monthly to review security risks and advise executives :: A Board · B Committee · C Government entity = b
   - [p] One corporate security office sets policy and tools for every subsidiary :: A Centralized · B Decentralized = a
   - [p] A court order requires preserving emails for a lawsuit :: A Legal · B Industry · C Global = a
   - [p] A country-wide data protection law applies to all firms in that country :: A Local/regional · B National · C Global = b
   - [p] A government health agency sets patient data rules and fines providers that breach them :: A Regulatory · B Industry · C Global = a
   - [p] A firm operating on four continents must reconcile privacy laws in every market :: A Local/regional · B National · C Global = c
   - *1: a working group under leadership is a committee; a board sits at the top. 2: one team decides for all, so centralized. 3: court orders and lawsuits are legal considerations. 4: one country = national. 5: a government agency setting and enforcing rules = regulatory. 6: many countries = global.*
   - @5.1.gov
27. A warehouse supervisor is dismissed on Friday. On Monday, IT finds his badge still opens the loading dock, his laptop was never returned and his cloud storage account is active. Which document would MOST directly have prevented this?
   - **[x] An offboarding procedure with a checklist to revoke access, collect equipment and transfer data**  - [ ] An acceptable use policy he signed at hiring  - [ ] A guideline reminding managers to tell IT about leavers  - [ ] An encryption standard
   - *Offboarding procedure = ordered steps when someone leaves: disable accounts and badges, collect assets, hand over or archive data. The AUP sets behaviour rules but does not remove access. A guideline is optional. Encryption does not stop an active account.*
   - @5.1.proc

### Key facts
- **Policy = intent (AUP, infosec, BC, DR, IR, SDLC, change mgmt); standard = mandatory specifics (password, access control, physical, encryption); procedure = steps (change mgmt, on/offboarding, playbooks); guideline = optional.**
- **External: regulatory, legal, industry, local/regional, national, global. Governance: boards, committees, government entities, centralized vs decentralized.**
- **Owner decides, custodian/steward cares for, controller sets purpose, processor acts on instructions.**

## Test 24 - 5.2 Risk Management + Business Impact Analysis (26 Q)

1. A new CISO wants to start a risk programme at a logistics firm. Before scoring anything, what should she do FIRST?
   - **[x] Identify assets, threats and vulnerabilities**  - [ ] Buy cyber insurance  - [ ] Calculate the ALE for every server  - [ ] Set the risk appetite to conservative
   - *Risk identification comes first: you cannot analyse or treat risks you have not listed. Analogy: a doctor examines before prescribing. ALE needs identified risks and values. Insurance is a treatment, which comes later.*
   - @5.2.ident
2. A workshop of department heads lists "warehouse flooding", "payroll vendor breach" and "loss of key developer". What activity is this?
   - **[x] Risk identification**  - [ ] Risk transference  - [ ] Risk acceptance  - [ ] Quantitative analysis
   - *Brainstorming possible events is risk identification. No numbers are assigned yet, so not quantitative. Transfer and accept are treatment choices made after analysis.*
   - @5.2.ident
3. A retailer reviews risk every quarter on a fixed calendar. Which assessment type is this?
   - **[x] Recurring**  - [ ] Ad hoc  - [ ] One-time  - [ ] Continuous
   - *Recurring = done at regular intervals. Ad hoc = triggered by an event; one-time = for a single project; continuous = ongoing, often automated. Hook: recurring = on the calendar.*
   - @5.2.assess
4. A zero-day in the company's VPN appliance is announced on a Friday. The CISO orders an immediate risk review of remote access. Which assessment type is this?
   - **[x] Ad hoc**  - [ ] Recurring  - [ ] Continuous  - [ ] One-time
   - *Ad hoc = unscheduled, prompted by a new event. Recurring is tempting because the firm may also have scheduled reviews, but this one was triggered. Continuous is automated and always on.*
   - @5.2.assess
5. A cloud team uses a tool that checks configurations against policy every few minutes and updates risk scores automatically. Which assessment type is this?
   - **[x] Continuous**  - [ ] Recurring  - [ ] Ad hoc  - [ ] One-time
   - *Continuous = ongoing, near real-time assessment, usually automated. Recurring has fixed intervals with gaps between. One-time is a single project assessment, such as before a merger.*
   - @5.2.assess
6. A startup has no historical loss data. The team rates each risk as low, medium or high for likelihood and impact on a heat map. What analysis is this?
   - **[x] Qualitative**  - [ ] Quantitative  - [ ] Annualized loss expectancy  - [ ] Business impact analysis
   - *Qualitative = relative ratings and judgement, quick when numbers are missing. Quantitative needs money values and rates. A BIA looks at business process downtime effects, not a general heat map.*
   - @5.2.qual
7. In a risk matrix, a risk is rated "almost certain" to happen but "minor" in effect. Which two factors does the matrix combine?
   - **[x] Likelihood and impact**  - [ ] RTO and RPO  - [ ] MTTR and MTBF  - [ ] Exposure factor and ARO
   - *Risk analysis combines likelihood (probability) with impact. RTO/RPO are recovery targets; MTTR/MTBF are reliability metrics. EF and ARO are quantitative inputs, not matrix labels.*
   - @5.2.qual
8. A laptop is worth 2,000 and theft destroys its full value. What is the exposure factor?
   - **[x] 100 percent**  - [ ] 50 percent  - [ ] 2,000  - [ ] 0.5
   - *EF = share of the asset's value lost in one event. Full loss = 100 percent, so SLE = 2,000. Hook: EF is a percentage, SLE is money.*
   - @5.2.quant
9. A data centre outage costs 40,000 each time and happens twice a year. What is the ALE?
   - **[x] 80,000**  - [ ] 20,000  - [ ] 40,000  - [ ] 160,000
   - *ALE = SLE x ARO = 40,000 x 2 = 80,000. 20,000 divides instead of multiplies. 40,000 is the SLE. Hook: single loss times yearly count.*
   - @5.2.quant
10. A mitigation costs 60,000 a year and would remove a risk with an ALE of 25,000. What is the BEST decision on financial grounds?
   - **[x] Do not buy it; the control costs more than the expected loss**  - [ ] Buy it; any reduction is worth it  - [ ] Buy it twice for redundancy  - [ ] Double the ARO to justify it
   - *A control should cost less per year than the loss it prevents. Spending 60,000 to stop 25,000 is a net loss. Accepting or a cheaper control makes sense. Fudging ARO falsifies the analysis.*
   - @5.2.quant
11. Where should a company record each risk with its owner, score, treatment and status?
   - **[x] Risk register**  - [ ] Change log  - [ ] Asset tag database  - [ ] SIEM dashboard
   - *Risk register = the central list of risks with owners, ratings, responses and KRIs. A change log records changes; SIEM tracks events. Analogy: a ledger for risks.*
   - @5.2.reg
12. The register lists "failed backup jobs per week" with an alert if it exceeds 3. What is this metric?
   - **[x] Key risk indicator (KRI)**  - [ ] Risk appetite  - [ ] Recovery point objective  - [ ] Annualized rate of occurrence
   - *KRI = a measurable early warning that a risk is rising. Analogy: a fuel gauge warning light. Appetite is the overall willingness to take risk; RPO is a data loss target; ARO is how often an event occurs.*
   - @5.2.reg
13. A risk has no named person responsible for it in the register and nothing has changed in a year. What is the BEST fix?
   - **[x] Assign a risk owner who is accountable for the response**  - [ ] Delete the risk from the register  - [ ] Raise the risk threshold  - [ ] Move it to the IT backlog
   - *Each risk needs an owner who is accountable for treatment and monitoring. Deleting hides it. Raising the threshold just ignores it on paper.*
   - @5.2.reg
14. A board says "we accept small security risks if they help us enter new markets quickly." Which risk appetite is this?
   - **[x] Expansionary**  - [ ] Conservative  - [ ] Neutral  - [ ] Zero tolerance
   - *Expansionary = willing to take more risk for growth. Conservative = avoids risk; neutral = balanced. Hook: expand = accept risk to grow.*
   - @5.2.appetite
15. A pension fund refuses any new technology without long proven use and favours safety over growth. Which appetite is this?
   - **[x] Conservative**  - [ ] Expansionary  - [ ] Neutral  - [ ] Transference
   - *Conservative appetite = low willingness to take risk. Transference is a treatment strategy, not an appetite.*
   - @5.2.appetite
16. Appetite is broad willingness to take risk. What is risk TOLERANCE?
   - **[x] The acceptable deviation around a specific objective, such as up to 4 hours of downtime**  - [ ] The total budget for security  - [ ] The amount of insurance purchased  - [ ] A list of all risks
   - *Tolerance = the specific acceptable variation for a given risk. The risk threshold is the line that triggers action. Analogy: appetite is your diet; tolerance is how many biscuits you allow today. A list of risks is the register.*
   - @5.2.appetite
17. A clinic cannot afford to rebuild after a ransomware attack, so it buys cyber insurance. Which strategy is this?
   - **[x] Transfer**  - [ ] Accept  - [ ] Avoid  - [ ] Mitigate
   - *Transfer shifts the financial impact to a third party, such as an insurer. Mitigate reduces likelihood or impact with controls. Note the risk itself is shared, not removed.*
   - @5.2.strat
18. A legacy lab system cannot meet the patching standard, so the CISO signs a time-limited approval with compensating controls. What is this?
   - **[x] A risk exception under acceptance**  - [ ] Risk avoidance  - [ ] Risk transfer  - [ ] A KRI
   - *Acceptance can be formal: an exception (temporary deviation from a policy) or exemption (a standing release from a requirement). Avoidance would stop using the system. Transfer moves the cost elsewhere.*
   - @5.2.strat
19. A fintech drops a planned feature that would store raw card numbers because the compliance risk is too high. Which strategy is this?
   - **[x] Avoid**  - [ ] Mitigate  - [ ] Accept  - [ ] Transfer
   - *Avoid = stop or never start the risky activity. Mitigate would build the feature with controls. Hook: avoid = don't play the game.*
   - @5.2.strat
20. The board wants a quarterly summary of top risks, trends and treatment status. What does this describe?
   - **[x] Risk reporting**  - [ ] Risk identification  - [ ] Penetration testing  - [ ] Vendor monitoring
   - *Risk reporting communicates the status of risks to stakeholders so they can decide. Identification lists them; reporting summarises them for leadership.*
   - @5.2.report
21. During a BIA, the finance team says the payroll system can be down for at most 8 hours before fines start. Which metric is this?
   - **[x] RTO**  - [ ] RPO  - [ ] MTBF  - [ ] MTTR
   - *RTO (recovery time objective) = maximum tolerable downtime target to restore service. RPO = maximum data loss in time. MTBF and MTTR describe actual reliability and repair, not targets.*
   - @5.2.bia
22. An online shop takes backups every 24 hours but says losing more than 1 hour of orders is unacceptable. What is the problem?
   - **[x] Backups do not meet the 1-hour RPO**  - [ ] The RTO is too short  - [ ] The MTBF is too high  - [ ] The MTTR is too low
   - *RPO = how much data, measured in time, can be lost. Daily backups can lose up to 24 hours. Fix: more frequent backups or replication. RTO is about time to restore, not data lost.*
   - @5.2.bia
23. PBQ 5.2 - Quantitative risk. A distribution centre is worth 800,000. A fire would destroy 40 percent of it. Fires are expected once every 20 years. Fire suppression upgrades cost 10,000 a year. Type numbers without commas or symbols.
   - [p] SLE = 320000 | 320,000
   - [p] ARO, as a decimal = 0.05 | .05
   - [p] ALE = 16000 | 16,000
   - [p] Is the upgrade justified on cost alone :: A No, it costs more than the ALE · B Yes, it costs less than the ALE · C Only if ARO is 1 · D Cannot tell without the RTO = b
   - [p] Strategy the upgrade represents :: A Accept · B Avoid · C Mitigate · D Transfer = c
   - *1: SLE = 800,000 x 0.40 = 320,000. 2: once in 20 years = 1/20 = 0.05. 3: ALE = 320,000 x 0.05 = 16,000. 4: 10,000 a year to reduce a 16,000 yearly loss is worth it. 5: a control that reduces impact is mitigation. Hook: SLE = AV x EF, ALE = SLE x ARO.*
   - @5.2.quant
24. PBQ 5.2 - BIA for a ticketing system over one year. ¶  Run times between failures: 500 h, 700 h, 900 h ¶  Repair times: 1 h, 2 h, 6 h ¶  Business says: restore within 3 hours; lose no more than 30 minutes of bookings. Type numbers only.
   - [p] MTBF in hours = 700
   - [p] MTTR in hours = 3
   - [p] RTO in hours = 3
   - [p] RPO in minutes = 30
   - [p] Was the RTO met for every failure :: A Yes · B No, one repair took 6 hours · C RTO only applies to backups · D Only MTBF matters = b
   - *1: MTBF = (500 + 700 + 900) / 3 = 700. 2: MTTR = (1 + 2 + 6) / 3 = 3. 3: RTO = 3 hours. 4: RPO = 30 minutes. 5: the average equals the RTO, but the 6-hour repair breached it. Hook: averages hide bad days.*
   - @5.2.bia

25. PBQ 5.2 - Risk process terms. Pick the best match.
   - [p] A single risk assessment done only for a planned data centre move :: A Ad hoc · B Recurring · C One-time · D Continuous = c
   - [p] Leadership balances risk and reward, neither seeking nor avoiding risk :: A Expansionary · B Conservative · C Neutral = c
   - [p] A KRI value above which the risk must be escalated :: A Risk threshold · B Risk appetite · C Exposure factor = a
   - [p] A low-impact risk is documented and no control is added because fixing it costs more :: A Accept · B Avoid · C Transfer · D Mitigate = a
   - [p] A permanent, approved release from a requirement for a system class :: A Exception · B Exemption = b
   - [p] Chance that an event occurs, expressed as a number between 0 and 1 :: A Probability · B Impact · C SLE = a
   - *1: done once for a single project, so one-time. 2: balanced = neutral. 3: the trigger line is the risk threshold. 4: knowingly living with it is acceptance. 5: exemption is a standing release; an exception is a temporary deviation. 6: probability is the numeric chance; impact is the effect if it happens; likelihood is often the qualitative version.*
   - @5.2.strat
26. A small bank lacks staff to run 24x7 monitoring, so it signs a contract with a managed security service provider that carries liability for missed detections. Which risk strategy is this MAINLY?
   - **[x] Transfer**  - [ ] Avoid  - [ ] Accept  - [ ] Exemption
   - *Transfer = shift the risk (or its cost) to another party, through insurance or by contracting out the work. The bank still keeps accountability for its data. Avoid would stop the activity. Exemption is a form of acceptance.*
   - @5.2.strat

### Key facts
- **Assessment types: ad hoc, recurring, one-time, continuous. Qualitative = ratings; quantitative = SLE = AV x EF, ALE = SLE x ARO.**
- **Register: risks, owners, KRIs, threshold. Appetite: expansionary, conservative, neutral; tolerance = acceptable deviation.**
- **Strategies: transfer, accept (exception, exemption), avoid, mitigate. BIA: RTO, RPO, MTTR, MTBF.**

## Test 25 - 5.3 Third-Party Risk: Vendor Assessment + Agreements (25 Q)

1. A payroll SaaS vendor will hold all employee bank details. Its sales team sends a glossy security brochure. What is the BEST evidence to request instead?
   - **[x] A recent independent assessment by a third-party auditor**  - [ ] A longer marketing brochure  - [ ] A list of the vendor's customers  - [ ] The vendor's logo on a compliance website
   - *Independent assessments by a third party are stronger than vendor claims. (Off-syllabus example: a SOC 2 Type II report tests controls over a period.) Hook: trust, but verify with someone neutral. A customer list proves popularity, not security.*
   - @5.3.vend
2. A bank wants proof that a vendor's own auditors actually check its access controls each year. What should it ask for?
   - **[x] Evidence of internal audits and their findings**  - [ ] The vendor's AUP  - [ ] An MOU  - [ ] The vendor's org chart
   - *Evidence of internal audits shows the vendor monitors its own controls and fixes findings. An AUP is a policy, not proof it works. An MOU is a non-binding agreement.*
   - @5.3.vend
3. Before connecting a vendor's portal to its network, a manufacturer wants to see whether the portal can be broken into. Which assessment fits BEST, assuming the contract allows it?
   - **[x] Penetration testing of the vendor's portal**  - [ ] A security questionnaire  - [ ] A conflict of interest check  - [ ] A business partnership agreement
   - *Pen testing actively tries to exploit weaknesses, giving direct evidence. A questionnaire is self-reported. Permission and scope must be written down first.*
   - @5.3.vend
4. After a breach at a hosting provider, a customer discovers its contract gives it no way to inspect the provider's controls. Which clause should have been included?
   - **[x] Right-to-audit clause**  - [ ] Non-compete clause  - [ ] Force majeure clause  - [ ] Termination for convenience
   - *Right-to-audit lets the customer (or its auditor) inspect the vendor's controls and records. Hook: no clause, no peek. Force majeure excuses non-performance in disasters.*
   - @5.3.audit
5. A large cloud provider refuses on-site audits from each of its thousands of customers. What is the MOST practical alternative?
   - **[x] Accept its third-party audit reports and certifications**  - [ ] Drop the requirement entirely  - [ ] Visit the data centre unannounced  - [ ] Rely on the provider's blog posts
   - *Shared independent third-party audit reports and certifications (examples, off-syllabus: SOC 2, ISO 27001) give assurance at scale. Unannounced visits break contracts. Blog posts are marketing.*
   - @5.3.audit
6. A router vendor's chips come from a subcontractor in another country. A buyer worries about tampered firmware. What should it perform?
   - **[x] Supply chain analysis**  - [ ] Risk transference  - [ ] Data inventory  - [ ] Passive reconnaissance
   - *Supply chain analysis looks at the vendor's suppliers, parts and software sources for risk. Analogy: checking where a restaurant gets its ingredients. Data inventory lists your data, not suppliers.*
   - @5.3.supply
7. A widely used software update was trojanized at the vendor and pushed to customers. Which risk was underestimated?
   - **[x] Supply chain risk from a trusted vendor**  - [ ] Insider threat at the customer  - [ ] Physical intrusion  - [ ] Weak passwords on customer laptops
   - *A compromise upstream reaches all customers through trusted channels. The customer's insiders and passwords are not the root cause here.*
   - @5.3.supply
8. Before signing with a new managed security provider, a firm checks its finances, lawsuits, breach history and references. What is this?
   - **[x] Due diligence**  - [ ] Due care  - [ ] Attestation  - [ ] Risk acceptance
   - *Due diligence = investigating before deciding. Due care = acting responsibly after. Hook: diligence is research, care is behaviour. Attestation is a formal statement of compliance.*
   - @5.3.select
9. The IT manager choosing a cloud vendor is married to the vendor's sales director. What is the BEST action?
   - **[x] Disclose the conflict of interest and remove the manager from the decision**  - [ ] Proceed if the price is low  - [ ] Ask the vendor for a discount  - [ ] Keep it confidential to avoid embarrassment
   - *Conflicts of interest must be disclosed and managed, usually by recusal, so selection is objective. Hiding it risks a biased deal.*
   - @5.3.select
10. Two vendors pass every technical check. Which factor should MOST strongly guide the final selection?
   - **[x] How well each meets the company's risk and compliance requirements**  - [ ] Which has the nicer website  - [ ] Which sales rep responded faster  - [ ] Which has the lower first-month cost only
   - *Selection weighs risk, compliance fit, financial health and support, not presentation. First-month cost ignores the long-term cost and risk.*
   - @5.3.select
11. A video platform needs its CDN provider to commit to a monthly availability figure and a 15-minute response to outages, with fee rebates when either is missed. Which agreement covers this?
   - **[x] SLA**  - [ ] NDA  - [ ] MOU  - [ ] BPA
   - *SLA (service level agreement) = measurable service targets and penalties. Hook: SLA = the scoreboard. NDA = secrecy; MOU = non-binding intent; BPA = partnership terms.*
   - @5.3.agree
12. Two city hospitals want to record a shared goal of pooling threat intelligence someday, without yet committing to any duties or payments. Which document fits?
   - **[x] MOU**  - [ ] MSA  - [ ] SLA  - [ ] SOW
   - *MOU (memorandum of understanding) = a statement of shared intent, usually non-binding. MOA (memorandum of agreement) is more formal and can set specific duties. MSA and SOW are binding contracts.*
   - @5.3.agree
13. Two firms co-sell a product and need to define how they split profits, decision rights and responsibilities. Which agreement fits?
   - **[x] BPA**  - [ ] NDA  - [ ] SLA  - [ ] MOU
   - *BPA (business partners agreement) = how partners share profits, losses and duties. SLA covers service levels, not profit shares.*
   - @5.3.agree
14. A company signs a master agreement with a consultancy. For each new project, it issues a short document listing the tasks, deliverables and deadlines. What are these two documents?
   - **[x] MSA, then SOW or work order per project**  - [ ] SLA, then NDA  - [ ] MOU, then BPA  - [ ] NDA, then MOA
   - *MSA (master service agreement) sets the general terms once; each SOW (statement of work) or WO (work order) defines a specific job. Hook: MSA = the umbrella, SOW = each raindrop.*
   - @5.3.contract
15. Before a vendor sees source code during a bid, what should it sign?
   - **[x] NDA**  - [ ] SLA  - [ ] BPA  - [ ] SOW
   - *NDA (non-disclosure agreement) legally protects confidential information shared. The other documents cover service, partnership and tasks.*
   - @5.3.contract
16. A penetration test SOW lists the IP ranges, dates and deliverables. What else MUST it or a linked document clearly state?
   - **[x] Written authorization and what is out of scope**  - [ ] The tester's home address  - [ ] The vendor's marketing plan  - [ ] The customer's revenue
   - *Scope and authorization protect both sides; testing without them can be illegal. Out-of-scope items prevent accidents. The rest is irrelevant.*
   - @5.3.contract
17. A vendor passed assessment two years ago. Since then it was acquired and changed data centres. What does this show the need for?
   - **[x] Ongoing vendor monitoring**  - [ ] A one-time assessment only  - [ ] Risk avoidance  - [ ] A new AUP
   - *Vendor monitoring tracks performance, SLA results, breaches and changes over time; a vendor's risk changes after signing. Hook: onboarding is not the end.*
   - @5.3.mon
18. Which activity is part of vendor monitoring?
   - **[x] Reviewing monthly SLA reports and news of vendor breaches**  - [ ] Checking the vendor's references before signing  - [ ] Writing the initial RFP  - [ ] Signing the NDA
   - *Monitoring happens after the contract starts. References, RFP and NDA are selection-stage activities.*
   - @5.3.mon
19. A company has 200 small suppliers and cannot audit each one. What is the MOST efficient first step?
   - **[x] Send a standard security questionnaire and tier vendors by risk**  - [ ] Pen test all 200  - [ ] Ignore small vendors  - [ ] Ask each for an MOU
   - *Questionnaires gather self-reported control information at scale; high-risk answers trigger deeper checks. Pen testing all is costly; ignoring them leaves gaps.*
   - @5.3.quest
20. What is the main LIMITATION of a vendor security questionnaire?
   - **[x] Answers are self-reported and may not be verified**  - [ ] It is legally binding  - [ ] It always includes pen testing  - [ ] It cannot ask about encryption
   - *Questionnaires rely on honesty; verify critical answers with evidence or audits. They are not contracts.*
   - @5.3.quest
21. A tester contracted by a bank discovers a vendor-hosted server not in scope. What do the rules of engagement say to do?
   - **[x] Stop, do not test it, and report it to the contact**  - [ ] Exploit it to show impact  - [ ] Test it quietly and delete logs  - [ ] Share it on social media
   - *Rules of engagement (RoE) define scope, timing, methods, contacts and what to do with surprises. Testing third-party assets needs their permission.*
   - @5.3.roe
22. Which item belongs in rules of engagement for a test of a vendor's system?
   - **[x] Allowed testing hours and emergency contacts**  - [ ] The vendor's annual revenue  - [ ] The tester's salary  - [ ] The SLA uptime target
   - *RoE sets how testing is done: windows, techniques allowed, data handling, contacts and stop conditions. SLA targets belong in the service agreement.*
   - @5.3.roe
23. PBQ 5.3 - Agreements. Pick the document for each need. ¶  1  Uptime and response times with penalties ¶  2  Keep shared designs confidential ¶  3  Overall terms for many future projects ¶  4  Tasks, deliverables and deadlines for one project ¶  5  Non-binding statement of shared goals ¶  6  How partners split profits and duties
   - [p] Need 1 :: A SLA · B NDA · C MSA · D SOW · E MOU · F BPA = a
   - [p] Need 2 :: A SLA · B NDA · C MSA · D SOW · E MOU · F BPA = b
   - [p] Need 3 :: A SLA · B NDA · C MSA · D SOW · E MOU · F BPA = c
   - [p] Need 4 :: A SLA · B NDA · C MSA · D SOW · E MOU · F BPA = d
   - [p] Need 5 :: A SLA · B NDA · C MSA · D SOW · E MOU · F BPA = e
   - [p] Need 6 :: A SLA · B NDA · C MSA · D SOW · E MOU · F BPA = f
   - *1: SLA = service levels. 2: NDA = secrecy. 3: MSA = master terms. 4: SOW = one job. 5: MOU = intent. 6: BPA = partnership. Hook: service, secret, master, work, understanding, partners.*
   - @5.3.agree
24. PBQ 5.3 - Vendor risk. A new HR SaaS vendor will hold staff records. Answer each part.
   - [p] Strongest evidence of its controls :: A Sales brochure · B Self-filled questionnaire · C Independent third-party assessment report · D Customer testimonials = c
   - [p] Clause letting you inspect its controls later :: A Right-to-audit · B Force majeure · C Non-compete · D Exclusivity = a
   - [p] Checking its subcontracted data centre :: A Supply chain analysis · B Risk acceptance · C Due care · D Active reconnaissance = a
   - [p] After go-live, tracking breaches and SLA reports :: A Due diligence · B Vendor monitoring · C Vendor selection · D MOU = b
   - *1: independent testing beats claims. 2: right-to-audit gives inspection rights. 3: subcontractors are part of the supply chain. 4: ongoing tracking is monitoring; due diligence is before signing.*
   - @5.3.vend

25. A port authority and the coast guard put in writing that the port will feed camera logs nightly and the coast guard will review alerts within an hour. No money changes hands and it is not a commercial contract. Which agreement is this?
   - **[x] MOA**  - [ ] MOU  - [ ] SLA  - [ ] NDA
   - *MOA (memorandum of agreement) = defines specific responsibilities and is more formal than an MOU (memorandum of understanding), which states shared intent. Hook: understanding = intent, agreement = duties. SLA sets service targets; NDA covers secrecy.*
   - @5.3.agree

### Key facts
- **Assessment: pen testing, right-to-audit, internal audit evidence, independent assessments, supply chain analysis. Selection: due diligence, conflict of interest.**
- **SLA = service levels; MOA/MOU = intent (MOA more formal); MSA = master terms; SOW/WO = specific job; NDA = secrecy; BPA = partnership.**
- **Then: vendor monitoring, questionnaires, rules of engagement.**

## Test 26 - 5.4 Compliance + Privacy (25 Q)

1. A CISO sends the audit committee a monthly dashboard of policy exceptions and overdue patches. Which kind of compliance reporting is this?
   - **[x] Internal**  - [ ] External  - [ ] Regulatory examination  - [ ] Attestation by a third party
   - *Internal reporting goes to management, boards and committees inside the organization. External reporting goes to regulators, customers or partners. Hook: who reads it decides the type.*
   - @5.4.report
2. A healthcare provider must notify the national regulator within a set time after a data breach. Which kind of compliance reporting is this?
   - **[x] External**  - [ ] Internal  - [ ] Self-assessment  - [ ] Risk register update
   - *External reporting = to regulators, authorities or affected parties, often with deadlines. GDPR, for example, sets 72 hours to notify the supervisory authority. Self-assessment and register updates are internal.*
   - @5.4.report
3. A card processor ignores PCI DSS findings for two years. Its acquiring bank stops letting it process cards. Which consequence of non-compliance is this?
   - **[x] Contractual impact**  - [ ] Loss of license  - [ ] Criminal sanction  - [ ] Reputational damage only
   - *PCI DSS is enforced through contracts, so the bank ending the processing deal is a contractual impact. Loss of license comes from a licensing authority, such as a medical or banking regulator.*
   - @5.4.conseq
4. A regulator bans a bank from offering new accounts for a year after repeated security failures. Which consequence is this?
   - **[x] Sanctions**  - [ ] Fines  - [ ] Reputational damage  - [ ] Contractual impact
   - *Sanctions = penalties that restrict activity, such as bans or orders. Fines are money penalties. Both can come together; here the restriction is the key fact.*
   - @5.4.conseq
5. A meal-kit company's breach trends on social media for a week. Subscriptions drop 20 percent and investors grow nervous, yet no regulator or partner has acted. What consequence is this?
   - **[x] Reputational damage**  - [ ] Loss of license  - [ ] Sanctions  - [ ] Contractual impact
   - *Reputational damage = lost trust and business, often costing more than fines. No regulator or contract was involved here.*
   - @5.4.conseq
6. Before launching in a new country, a company checks its local partners and hosting provider against the privacy law. After launch, it trains its own staff and enforces controls every day. Which terms match these two activities?
   - **[x] Due diligence, then due care**  - [ ] Due care, then due diligence  - [ ] Attestation, then acknowledgement  - [ ] Internal, then external audit
   - *Due diligence = investigating and checking, especially third parties; due care = the organization's own ongoing responsible action. Rule of thumb: your own ongoing actions are due care, checking a third party is due diligence. Hook: diligence = do your homework, care = keep doing the right thing.*
   - @5.4.mon
7. A compliance team spends days each month pulling screenshots of settings for auditors. What would MOST improve compliance monitoring?
   - **[x] Automated tools that continuously check controls and collect evidence**  - [ ] More staff to take screenshots  - [ ] Checking only once a year  - [ ] Removing the controls from scope
   - *Automation gives continuous, consistent monitoring and evidence. Annual checks leave long gaps. Removing scope just hides the problem.*
   - @5.4.mon
8. When the new remote access policy goes live, the HR portal will not let any user continue until they tick "I have read and accept this policy." What is this called?
   - **[x] Acknowledgement**  - [ ] Attestation by a third party  - [ ] Due diligence  - [ ] Data inventory
   - *Acknowledgement = an individual confirms they received and understood a policy. Attestation = a formal statement, often by management or an auditor, that controls are in place and compliant.*
   - @5.4.attest
9. Under a cyber insurance renewal, the COO must sign and submit a declaration that MFA and offline backups are in place across the company. What is this?
   - **[x] Attestation**  - [ ] Acknowledgement  - [ ] Guideline  - [ ] Questionnaire
   - *Attestation = a formal declaration that requirements are met, putting the signer on the hook. Analogy: signing a tax return. An acknowledgement only confirms receipt.*
   - @5.4.attest
10. A US company with only US customers sells to EU residents through its website for the first time. Which privacy consideration now applies?
   - **[x] Global law such as GDPR, because it covers EU residents' data**  - [ ] Only the company's home state law  - [ ] No law, since servers are in the US  - [ ] Only industry guidelines
   - *Privacy law follows the people whose data it is, not just the server. GDPR applies to processing EU residents' data even by non-EU firms; It counts as a global (multi-country) legal implication. Server location alone does not exempt it.*
   - @5.4.law
11. A firm operates in several US states, each with its own breach notification rules. What is the BEST approach?
   - **[x] Map each local/regional requirement and meet the strictest where they overlap**  - [ ] Follow only the federal rules  - [ ] Pick the easiest state's rule  - [ ] Ignore states without offices
   - *Legal implications exist at local/regional, national and global levels. Meeting the strictest common rule simplifies compliance. Ignoring states where residents live breaks their laws.*
   - @5.4.law
12. A fitness app logs Priya's runs, heart rate and home address. In privacy law terms, what is Priya?
   - **[x] Data subject**  - [ ] Data controller  - [ ] Data processor  - [ ] Data custodian
   - *Data subject = the individual the data identifies. They hold rights such as access, correction and erasure.*
   - @5.4.subject
13. A customer asks an online store for a copy of all personal data held about her. What is the FIRST thing the store needs to do this well?
   - **[x] Know where her data is stored, using its data inventory**  - [ ] Delete all her data  - [ ] Refer her to the cloud provider  - [ ] Ask her to sue
   - *You cannot answer a data subject request without knowing where data lives. Deleting is a different request. The store, as controller, is responsible, not its provider.*
   - @5.4.subject
14. A clinic uses a cloud provider to store scans. The provider is breached. Who is primarily accountable to patients under GDPR-style law?
   - **[x] The clinic, as controller, though the processor also has duties**  - [ ] Only the cloud provider  - [ ] Only the patients  - [ ] No one, since it was a third party
   - *The controller decides why and how data is used and remains accountable; processors must protect data and follow instructions. Outsourcing the work does not outsource the accountability.*
   - @5.4.ctrl
15. A marketing agency starts using a client's customer list for its own campaigns. What has happened?
   - **[x] The processor has acted as a controller without authority**  - [ ] The agency became the data subject  - [ ] It is normal processor work  - [ ] The client is now the processor
   - *A processor may only use data per the controller's instructions. Deciding its own purposes makes it a controller and is likely unlawful.*
   - @5.4.ctrl
16. Two departments argue over who decides retention rules for customer support recordings. What is the BEST governance fix?
   - **[x] Assign a single data owner accountable for that data set**  - [ ] Let both departments decide separately  - [ ] Give IT ownership by default  - [ ] Delete the recordings
   - *Data ownership must be clear: one senior owner has overall responsibility for the data set and settles disputes like this (e.g. the head of sales owns customer records). Custodians/stewards then apply labels and access day to day; IT is not the owner by default.*
   - @5.4.own
17. A company buys a dataset of email addresses from a broker. What should it check FIRST about ownership?
   - **[x] Whether the data was lawfully collected and it has the right to use it**  - [ ] Only the file format  - [ ] How large the file is  - [ ] Whether the broker has a website
   - *Buying data does not give the right to use it if collection broke privacy law. Ownership and rights to use must be confirmed.*
   - @5.4.own
18. A new DPO cannot answer "where do we keep passport scans?" She commissions a spreadsheet mapping each system to the personal data it holds, the purpose and the retention period. What is this?
   - **[x] Data inventory**  - [ ] Risk register  - [ ] Asset tag list  - [ ] Change log
   - *Data inventory = a record of what personal data exists, where, why and for how long. It underpins retention, requests and breach response.*
   - @5.4.inv
19. An insurer keeps every customer email since 1998 "just in case." What is the MAIN privacy problem?
   - **[x] Keeping data longer than needed breaks retention rules and increases breach impact**  - [ ] Storage is cheap so there is no issue  - [ ] Emails cannot hold personal data  - [ ] Only encryption matters
   - *Retention policies keep data only as long as legally or business needed, then securely delete it. Old data is liability. Encryption reduces but does not remove that risk.*
   - @5.4.inv
20. Tax law requires invoices be kept for 7 years. A customer asks for deletion after 2 years. What is the BEST response?
   - **[x] Keep the invoices for the legal retention period and delete other data**  - [ ] Delete everything immediately  - [ ] Ignore the request  - [ ] Keep everything forever
   - *Legal retention obligations can override erasure rights for the specific data needed; other data should be deleted. Ignoring the request is non-compliant.*
   - @5.4.inv
21. A former user demands that a social media site delete her account data entirely. Which right is she using?
   - **[x] Right to be forgotten (erasure)**  - [ ] Right to audit  - [ ] Right of first refusal  - [ ] Due care
   - *Right to be forgotten = GDPR right to erasure of personal data, with some exceptions. Right to audit is a vendor contract clause.*
   - @5.4.forget
22. A company deletes a user's data from production after an erasure request, but it remains in backups and a test environment. What is the risk?
   - **[x] The erasure is incomplete; copies must be tracked and handled**  - [ ] No risk; backups do not count  - [ ] The user must re-request  - [ ] Test environments are exempt
   - *Erasure must cover all copies, or backups must be handled per policy (for example, deleted on restore or expiry). A data inventory helps find copies.*
   - @5.4.forget
23. PBQ 5.4 - Compliance programme. Pick the best match for each situation. ¶  1  Board audit committee reviews monthly compliance metrics ¶  2  Breach notice sent to the national regulator ¶  3  Regulator issues a 2 million penalty ¶  4  Medical licence board suspends a hospital's operation licence ¶  5  Employee clicks "I have read the policy"
   - [p] Situation 1 :: A Internal reporting · B External reporting · C Acknowledgement = a
   - [p] Situation 2 :: A Internal reporting · B External reporting · C Acknowledgement = b
   - [p] Situation 3 :: A Fine · B Loss of license · C Contractual impact = a
   - [p] Situation 4 :: A Fine · B Loss of license · C Contractual impact = b
   - [p] Situation 5 :: A Internal reporting · B External reporting · C Acknowledgement = c
   - *1: inside the company, so internal. 2: to a regulator, so external. 3: money penalty, so fine. 4: losing the right to operate, so loss of license. 5: personal confirmation of a policy, so acknowledgement.*
   - @5.4.report
24. PBQ 5.4 - Privacy request. A European customer asks a travel company to erase her data. The company uses a cloud CRM vendor. Answer each part.
   - [p] Her role :: A Data subject · B Controller · C Processor = a
   - [p] The travel company's role :: A Data subject · B Controller · C Processor = b
   - [p] The CRM vendor's role :: A Data subject · B Controller · C Processor = c
   - [p] Tool needed to find all copies :: A Data inventory · B Risk register · C SLA = a
   - [p] Booking invoices required by tax law :: A Delete now · B Keep for the legal period, then delete · C Keep forever = b
   - [p] The company also serves Australia, where one countrywide privacy act requires breach notification :: A Local/regional · B National · C Global = b
   - *1: she is the person the data is about. 2: the company decides purpose, so controller. 3: the CRM acts on instructions, so processor. 4: a data inventory shows where data lives. 5: legal retention can override erasure for that data only. 6: a single country's law is a national legal implication.*
   - @5.4.forget

25. A credit union's risk staff spot-check firewall rules every sprint, and a CPA firm reviews the same controls before each regulator filing. Which compliance monitoring elements are these?
   - **[x] Internal and external compliance monitoring**  - [ ] Only external monitoring  - [ ] Due diligence only  - [ ] Data inventory and retention
   - *Compliance monitoring can be internal (own staff) and external (auditors, regulators); using both adds independence. Due diligence is research before a decision; a data inventory is a privacy record.*
   - @5.4.mon

### Key facts
- **Reporting: internal vs external. Non-compliance: fines, sanctions, reputational damage, loss of license, contractual impacts.**
- **Monitoring: due diligence (research) vs due care (ongoing action), attestation and acknowledgement, internal and external, automation.**
- **Privacy: local/regional, national, global laws; data subject; controller vs processor; ownership; data inventory and retention; right to be forgotten.**

## Test 27 - 5.5 + 5.6 Audits, Penetration Testing, Security Awareness (27 Q)

1. After an external audit, the audit firm issues a signed opinion that the company's controls meet the stated framework. What is this opinion?
   - **[x] Attestation**  - [ ] Acknowledgement  - [ ] Self-assessment  - [ ] Rules of engagement
   - *Attestation = an auditor formally vouches that controls meet requirements. Customers rely on it instead of auditing themselves. Self-assessment is done by the organization itself.*
   - @5.5.attest
2. A company's own team checks each department against the security policy before an official audit. Which activity is this?
   - **[x] Internal self-assessment**  - [ ] Regulatory examination  - [ ] Independent third-party audit  - [ ] Passive reconnaissance
   - *Self-assessments are internal reviews to find gaps early. Analogy: a practice exam. Regulatory exams and independent audits are external.*
   - @5.5.int
3. The head of internal audit finds that the COO keeps softening her reports. To protect auditor independence, to whom should she report directly?
   - **[x] Audit committee**  - [ ] Change advisory board  - [ ] Help desk  - [ ] Red team
   - *The audit committee gives internal audit independence: auditors report to it, not to the managers they audit. A CAB approves changes.*
   - @5.5.int
4. A national banking regulator sends examiners to review a bank's cyber controls. What type of audit is this?
   - **[x] Regulatory examination (external)**  - [ ] Internal self-assessment  - [ ] Penetration test  - [ ] Vendor questionnaire
   - *Regulators perform examinations of the businesses they supervise; findings can lead to sanctions. It is external because it is done by an outside authority.*
   - @5.5.ext
5. A SaaS firm's customers demand unbiased proof of security. Which is the BEST option?
   - **[x] Hire an independent third-party auditor**  - [ ] Publish its internal audit notes  - [ ] Ask staff to attest personally  - [ ] Run a phishing campaign
   - *Independent third-party audits are trusted because the auditor has no stake in the result. Internal notes lack independence.*
   - @5.5.ext
6. Testers are hired to tailgate staff into a data centre and plug a device into a rack. Which test type is this?
   - **[x] Physical penetration test**  - [ ] Defensive test  - [ ] Passive reconnaissance  - [ ] Code review
   - *Physical pen tests check doors, badges, guards and human trust. Hook: if you need shoes, it's physical. Passive recon gathers info without touching the target.*
   - @5.5.pen
7. A red team attacks while the blue team detects and responds, and both share results in real time to improve controls. Which approach is this?
   - **[x] Integrated penetration testing**  - [ ] Unknown environment testing  - [ ] Offensive only  - [ ] Defensive only
   - *Integrated = offensive and defensive (informally called purple teaming) working together. Offensive = attacking (red); defensive = detecting and responding (blue).*
   - @5.5.pen
8. A retailer wants to see what a stranger could achieve, so the contract gives the testers no IP ranges, accounts or diagrams. Which environment is this?
   - **[x] Unknown environment**  - [ ] Known environment  - [ ] Partially known environment  - [ ] Integrated
   - *Unknown (black box) = no prior info, like an outsider. Known (white box) = full info. Partially known (gray box) = some info.*
   - @5.5.pen
9. A tester reads the company's job ads, DNS records and staff social media profiles without sending traffic to its servers. What is this?
   - **[x] Passive reconnaissance**  - [ ] Active reconnaissance  - [ ] Exploitation  - [ ] Lateral movement
   - *Passive recon gathers public info (OSINT) without touching target systems, so it is hard to detect. Active recon (port scans, banner grabbing) interacts directly.*
   - @5.5.recon
10. A tester runs a port scanner against the target's public IPs. Which phase is this, and what is a risk?
   - **[x] Active reconnaissance; it can be detected and logged**  - [ ] Passive reconnaissance; it is undetectable  - [ ] Reporting; no risk  - [ ] Exploitation; it gains root access
   - *Scanning sends packets to the target, so it is active and visible to IDS. It discovers hosts and ports but does not itself exploit them.*
   - @5.5.recon
11. A payroll clerk gets a message signed by the CFO, from ceo-office-mail.net, asking her to change an employee's bank details before tonight's run. What should training teach her to do FIRST?
   - **[x] Report it through the phishing button or security team and not reply**  - [ ] Reply asking if it is real  - [ ] Make the change, since it comes from the CFO  - [ ] Forward it to colleagues as a warning
   - *Recognize (urgency, odd domain, unusual request) and report. Replying engages the attacker. Forwarding spreads the risk; let security warn others.*
   - @5.6.phish
12. Which sign MOST strongly suggests an email is a phishing attempt?
   - **[x] A sender domain that differs slightly from the real one, with urgent pressure**  - [ ] The email has a company logo  - [ ] It was sent during office hours  - [ ] It uses the recipient's first name
   - *Lookalike domains plus urgency are classic indicators. Logos and names are easy to fake, so they prove nothing either way.*
   - @5.6.phish
13. The security team runs simulated phishing campaigns each quarter. What is the MAIN goal?
   - **[x] Measure and improve user recognition and reporting**  - [ ] Punish users who click  - [ ] Test the mail server's speed  - [ ] Collect real passwords
   - *Campaigns build skills and give metrics (click rate, report rate). Shaming harms reporting culture. Simulations should never collect real credentials.*
   - @5.6.phish
14. An accountant who never works weekends starts downloading large client files at 2 a.m. on Sundays. What should this be recognized as?
   - **[x] Unexpected behaviour worth reporting**  - [ ] Normal behaviour  - [ ] A phishing campaign  - [ ] A physical test
   - *Anomalous behaviour recognition: unexpected activity versus a user's normal pattern may signal insider threat or a compromised account.*
   - @5.6.anom
15. A user disables antivirus to install a free tool from a forum to "work faster". Which behaviour category is this?
   - **[x] Risky**  - [ ] Unexpected  - [ ] Unintentional  - [ ] Authorized
   - *Risky = actions that weaken the device or expose data, such as changing security settings, editing the hosts file, replacing system files or uploading sensitive files. Unintentional = an honest mistake, like mistyping a domain or emailing the wrong person. Unexpected = outside the user's normal pattern. Hook: risky weakens, unintentional slips.*
   - @5.6.anom
16. An HR clerk accidentally sends a salary spreadsheet to an external address with a similar name. Which behaviour category is this?
   - **[x] Unintentional**  - [ ] Risky  - [ ] Malicious insider  - [ ] Unexpected
   - *Unintentional = a mistake without intent. Training and tools such as DLP and address warnings help. Malicious would require intent.*
   - @5.6.anom
17. A remote worker joins calls from cafes and leaves her laptop unlocked when ordering. Which training topic MOST applies?
   - **[x] Hybrid/remote work security and situational awareness**  - [ ] Change management  - [ ] Risk quantification  - [ ] Vendor monitoring
   - *Remote training covers screen locks, shoulder surfing, public Wi-Fi and VPN use. Situational awareness = noticing surroundings and risks.*
   - @5.6.train
18. A receptionist is handed a padded envelope with an unbranded USB-C drive and a note: "Board slides - please load before 9." No one expected it. What should training say to do?
   - **[x] Hand them to security without plugging them in**  - [ ] Plug in to find the owner  - [ ] Take them home  - [ ] Throw them in the bin
   - *Removable media training: unknown drives and cables may carry malware (USB drop attacks, malicious cables). Security can analyse them safely.*
   - @5.6.train
19. A developer posts a photo of her desk on social media, with a sticky note showing a server name and the office badge visible. Which training topic covers this?
   - **[x] Operational security (OPSEC)**  - [ ] Password complexity  - [ ] Data retention  - [ ] Change management
   - *OPSEC = avoiding leaking small details that attackers can combine. Passwords may apply too, but the core issue is oversharing.*
   - @5.6.train
20. A company wants to track whether its awareness programme works. Which approach BEST combines initial and recurring reporting and monitoring?
   - **[x] A baseline phishing test at launch, then regular campaigns tracking click and report rates**  - [ ] One test at launch only  - [ ] Annual policy sign-off only  - [ ] Counting training slides
   - *Initial = baseline; recurring = trend over time. Report rate rising is as important as click rate falling. Slide counts measure effort, not results.*
   - @5.6.report
21. Before launching awareness training, the team surveys roles, past incidents and threats faced by each department. Which phase is this?
   - **[x] Development**  - [ ] Execution  - [ ] Reporting  - [ ] Attestation
   - *Development = designing content to fit audience and risk. Execution = delivering it (sessions, modules, campaigns). Hook: design, then deliver.*
   - @5.6.prog
22. Finance staff face wire fraud attempts, and developers face code repository attacks. How should training be executed?
   - **[x] Tailor content by role, in addition to a common baseline**  - [ ] Give everyone identical content only  - [ ] Train only IT staff  - [ ] Skip finance since they are not technical
   - *Effective execution targets role-based risks; finance needs business email compromise and payment fraud content. Training only IT ignores the most targeted users.*
   - @5.6.prog
23. PBQ 5.5 - Penetration test scoping. Answer each part.
   - [p] Testers receive a VPN login with standard rights and a subnet list, nothing more :: A Known environment · B Partially known environment · C Unknown environment = b
   - [p] The client shares its repo, architecture docs and a domain admin account :: A Known environment · B Partially known environment · C Unknown environment = a
   - [p] Red team attacks while the blue team responds, sharing findings live :: A Offensive · B Defensive · C Integrated = c
   - [p] Harvesting staff names from LinkedIn and old conference talks :: A Passive reconnaissance · B Active reconnaissance = a
   - [p] Sending SYN probes and grabbing banners from the target's mail gateway :: A Passive reconnaissance · B Active reconnaissance = b
   - [p] Signed sheet listing test windows, excluded hosts and an emergency phone number :: A SLA · B Rules of engagement · C MOU = b
   - *1: some information, so partially known. 2: full information, so known. 3: working together = integrated. 4: no contact with targets, so passive. 5: sends packets, so active. 6: RoE governs how the test runs.*
   - @5.5.pen
24. PBQ 5.6 - Awareness programme review. ¶  Q1 campaign: 28 percent clicked, 3 percent reported. Q3 campaign: 9 percent clicked, 31 percent reported. ¶  Incidents: E1 user plugs in a found USB stick. E2 user emails a file to the wrong client by mistake. E3 user turns off the VPN to stream video. Answer each part.
   - [p] Trend shown by Q1 to Q3 :: A Worse · B Improving on both clicks and reports · C No change = b
   - [p] Which metric shows users are becoming active defenders :: A Click rate · B Report rate · C Number of emails sent = b
   - [p] E1 training topic :: A Removable media · B Password management · C Insider threat = a
   - [p] E2 behaviour category :: A Risky · B Unintentional · C Malicious = b
   - [p] E3 behaviour category :: A Risky · B Unintentional · C Unexpected = a
   - *1: clicks fell and reports rose, so improving. 2: reporting shows users act, not just avoid. 3: a found USB stick is a removable media risk. 4: an honest mistake is unintentional. 5: knowingly bypassing a control is risky.*
   - @5.6.train

25. PBQ 5.5 - Audits and test types. Pick the best match.
   - [p] Internal team checks that departments follow PCI DSS and internal policy :: A Internal compliance · B Regulatory examination · C Independent third-party audit = a
   - [p] An outside firm evaluates security maturity against a framework, without issuing an audit opinion :: A External assessment · B Attestation · C Self-assessment = a
   - [p] Testers try to breach systems as attackers would :: A Offensive · B Defensive · C Integrated = a
   - [p] Staff practise detecting and responding to simulated attacks :: A Offensive · B Defensive · C Integrated = b
   - *1: internal checking against rules is internal compliance. 2: an external assessment evaluates and advises; attestation is a formal opinion. 3: attacking is offensive. 4: detecting and responding is defensive.*
   - @5.5.int
26. PBQ 5.6 - Awareness practices. Pick the best match.
   - [p] SOC analyst receives a user-reported email: checks headers, removes copies from all mailboxes, thanks the user :: A Responding to reported suspicious messages · B Phishing campaign · C Situational awareness = a
   - [p] New hires read and sign the security rules in the employee handbook :: A Policy/handbooks · B Operational security · C Execution = a
   - [p] Training on spotting colleagues who copy data before resigning :: A Insider threat · B Removable media · C Password management = a
   - [p] Training on using a password manager and never reusing passwords :: A Password management · B Social engineering · C Insider threat = a
   - [p] Training on callers pretending to be IT support asking for MFA codes :: A Social engineering · B Hybrid/remote work · C Operational security = a
   - *1: handling what users report is responding to reported suspicious messages. 2: written rules staff acknowledge are policy/handbooks. 3: watching for staff who misuse access is insider threat. 4: password managers and no reuse are password management. 5: impersonation by phone is social engineering (vishing).*
   - @5.6.train
27. While tidying folder permissions, a junior admin picks the wrong option and leaves a shared drive readable by all staff. He spots nothing until a colleague mentions it a week later. Which anomalous behaviour category BEST fits?
    - **[x] Unintentional**  - [ ] Risky  - [ ] Unexpected  - [ ] Malicious
    - *Unintentional = human error, such as a misconfigured security setting, a mistyped domain or a misplaced USB drive. Risky covers actions like changing security settings on purpose, editing system files or uploading sensitive files. Unexpected = activity outside the user's normal pattern, such as a login from another country. No harmful intent, so not malicious. Fix with training and permission reviews.*
    - @5.6.anom

### Key facts
- **Attestation = formal assurance. Internal: compliance, audit committee, self-assessments. External: regulatory, examinations, assessment, independent third-party audit.**
- **Pen testing: physical, offensive, defensive, integrated; known, partially known, unknown environment. Recon: passive vs active.**
- **Awareness: phishing (campaigns, recognize, respond), anomalous behaviour (risky, unexpected, unintentional), training topics, initial and recurring reporting, development and execution.**

