<!-- passmark: 83 -->
## Test 1 - 1.1 + 1.2 Security Controls, CIA, AAA, Zero Trust (21 Q)

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
7. A finance clerk's laptop is stolen from a car. The drive used full-disk encryption and the company keeps nightly cloud backups. Which statement is MOST accurate?
   - **[x] Confidentiality held because of FDE, and availability held because of backups**  - [ ] Integrity failed, because the thief now controls the data  - [ ] Confidentiality failed, because physical possession bypasses encryption  - [ ] Availability failed, because the device itself is gone
   - *FDE keeps the data unreadable (confidentiality); backups mean the clerk can keep working (availability). Integrity is about unauthorised change to data the business relies on, and the backup copy is untouched. Possession does not defeat strong encryption with a good key. Losing one device is not loss of availability when the data is backed up. Hook: C = who can read, I = has it changed, A = can I get it.*
   - @1.2.cia
8. A supplier disputes a purchase order, claiming your buyer never sent it. Which control would have BEST let you prove the buyer's origin of the message?
   - **[x] The buyer signing the order with her private key**  - [ ] Sending the order over a TLS-encrypted connection  - [ ] Attaching a SHA-256 hash of the order to the email  - [ ] Requiring the buyer to use MFA to log into email
   - *Non-repudiation comes from a digital signature: only the holder of the private key could have produced it, and it also proves integrity. TLS protects the channel, not who authored the message. A bare hash proves nothing about origin, since anyone can recompute one after editing. MFA proves who logged in, not that this specific message is unaltered and theirs. Analogy: a wax seal only you own.*
   - @1.2.cia
9. Ransomware encrypts a hospital's patient-records share. The servers stay online and the files are still there, but no clinician can open any of them until the data is restored. Which CIA element is MOST directly affected?
    - **[x] Availability**  - [ ] Integrity  - [ ] Confidentiality  - [ ] Non-repudiation
    - *Availability = authorised users can get to the data when they need it, and here nobody can. Confidentiality would need the data to be read or copied by someone unauthorised; the stem gives no sign of exfiltration (if it did, that would be a second impact, as in double extortion). Integrity tempts because files were changed, but the clinical harm the stem stresses is being locked out. Non-repudiation is about proving who did something, not CIA. Hook: can't get to it = A.*
    - @1.2.cia
10. A contractor logs into the VPN with password plus MFA but cannot reach the engineering file server. The help desk confirms her credentials are fine. Where should they look FIRST?
    - **[x] Her group membership and the server's access rules**  - [ ] The MFA app on her phone  - [ ] The RADIUS accounting logs for her session  - [ ] Her password expiry date
    - *She authenticated, so the failure is authorization: what an identity may access. Check groups/roles and ACLs. MFA and password are authentication, already passed. Accounting logs record what happened but do not grant access; they may confirm the deny, but the fix is in authorization. Hook: AuthN = who are you, AuthZ = what may you do, Accounting = what did you do.*
    - @1.2.aaa
11. A microservice calls an internal payments API thousands of times an hour, with no human present. What is the BEST way for the API to authenticate it?
    - **[x] A certificate issued to the service, checked with mutual TLS**  - [ ] An allow list of the microservice's source IP addresses  - [ ] A long-lived API key hard-coded in the service's source  - [ ] An OAuth token obtained with a developer's own credentials
    - *A service certificate checked with mutual TLS gives the microservice its own cryptographic machine identity, and both ends prove themselves on every connection. The IP allow list is the most tempting, but an IP identifies a location, not a service, and anything else on that host or a spoofed address passes too. A hard-coded key leaks with the code, and borrowing a developer's credentials ties a machine to a person who may leave. Hook: machines get their own passports.*
    - @1.2.aaa
12. A company with 8,000 staff wants access to follow job function, so a new payroll hire automatically gets payroll folders and loses them when she moves teams. What is the company choosing?
    - **[x] A role-based authorization model**  - [ ] A stronger authentication factor  - [ ] More detailed accounting logs  - [ ] A gap analysis against ISO 27001
    - *Authorization models apply permissions at scale; role-based ties rights to job roles instead of individual users. Authentication factors prove identity but grant nothing. Accounting records use. A gap analysis finds missing controls, it does not assign access. Analogy: wristband colour decides which rooms you enter.*
    - @1.2.aaa
13. A new regulation takes effect in six months. The compliance lead has its control checklist and must produce a prioritised remediation plan before any budget is set. What should she do FIRST?
    - **[x] A gap analysis comparing current controls with the checklist**  - [ ] A risk assessment ranking the top threats to the business  - [ ] A vulnerability scan of every in-scope system  - [ ] A business impact analysis of critical processes
    - *A gap analysis compares the current state with a required state, such as a regulation's control list, and its output is exactly a prioritised remediation plan. A risk assessment is tempting because it also steers spending, but it ranks threats and likelihood rather than checking each required control. A vulnerability scan finds technical flaws, not missing policies or processes, and a BIA ranks processes by downtime impact. Hook: packed suitcase versus packing list.*
    - @1.2.gap
14. A bank's zero trust system sees a teller sign in from a new laptop at 2 a.m. and demands a hardware-key prompt before allowing access. Which zero trust concept is shown?
    - **[x] Adaptive identity**  - [ ] Threat scope reduction  - [ ] Implicit trust zone  - [ ] Policy enforcement point
    - *Adaptive identity raises or lowers authentication strength based on context: device, location, time, behaviour. Threat scope reduction limits what a user can reach, not how hard login is. An implicit trust zone is the area past the enforcement point. The PEP enforces a decision but does not choose the extra factor. Analogy: your bank texting you when your card is used abroad.*
    - @1.2.zt
15. After a breach in which one stolen account reached 300 servers, an architect wants the NEXT stolen account to reach as little as possible. Which zero trust goal BEST fits?
    - **[x] Threat scope reduction**  - [ ] Adaptive identity  - [ ] Policy administrator  - [ ] Non-repudiation
    - *Threat scope reduction shrinks the blast radius through least privilege and microsegmentation. Adaptive identity makes stealing the account harder but does not limit reach once it is used. The policy administrator relays decisions; it is a component, not a goal. Non-repudiation proves who acted. Analogy: watertight compartments on a ship.*
    - @1.2.zt
16. A zero trust team writes rules such as "finance app: managed device + finance role + compliant patch level" and lets the system apply them to every request. Which control plane concept is this?
    - **[x] Policy-driven access control**  - [ ] Implicit trust zone  - [ ] Subject/system  - [ ] Threat scope reduction
    - *Policy-driven access control means access decisions come from defined policies evaluated per request, not from network location. Implicit trust zone and subject/system are data plane items. Threat scope reduction is the outcome of tight policies, not the mechanism. Hook: the rulebook the policy engine reads.*
    - @1.2.zt
17. After a fraudulent change to supplier bank details, the audit log shows it was made by "finance_team", a login used by six clerks. Which security property can the company NOT achieve for this action?
    - **[x] Non-repudiation**  - [ ] Availability  - [ ] Confidentiality  - [ ] Authorization
    - *Non-repudiation means a specific person cannot credibly deny an action. A shared login ties the change to a group, not an individual, so any of the six can deny it. Give each clerk a named account (and digital signatures for high-value approvals). Availability and confidentiality are not in question, and the login was authorized to make the change. Hook: shared account = shared alibi.*
    - @1.2.cia

### Key facts
- **Categories: technical, managerial, operational, physical. Types: preventive, deterrent, detective, corrective, compensating, directive.**
- **CIA: confidentiality (encryption), integrity (hashing), availability (redundancy, backups). Non-repudiation = digital signature.**
- **AAA: authentication (people and systems), authorization (models such as role-based), accounting. Gap analysis (1.2) = current vs required state, output is a prioritised remediation plan.**
- **Zero trust control plane: adaptive identity, threat scope reduction, policy-driven access control, policy engine, policy administrator. Data plane: subject/system, PEP, implicit trust zones.**
18. In a zero trust design, which component weighs identity, device posture and threat intelligence to decide whether a request is allowed?
   - **[x] Policy engine**  - [ ] Policy administrator  - [ ] Policy enforcement point  - [ ] Implicit trust zone
   - *The policy engine decides. The policy administrator acts on that decision and sets up or tears down the session. The PEP sits in the traffic path and opens or closes the connection. Analogy: judge (engine), clerk (administrator), bailiff at the door (PEP).*
   - @1.2.zt
19. An access proxy sits between remote engineers and an internal build server and opens or closes each connection as instructed. In zero trust terms, what is the proxy, and which plane is it in?
   - **[x] Policy enforcement point, in the data plane**  - [ ] Policy engine, in the control plane  - [ ] Policy administrator, in the control plane  - [ ] Subject, in the data plane
   - *The PEP enforces in the traffic path, so it lives in the data plane with the subject and the implicit trust zone. Engine and administrator make and push decisions, so they form the control plane. Hook: control plane thinks, data plane carries.*
   - @1.2.zt
20. PBQ 1.1 - Controls matrix. A logistics firm lists new controls. Pick the CATEGORY, then the TYPE that best fits each control's main purpose. ¶  1  Data-loss prevention rule blocking card numbers in outbound email ¶  2  Policy requiring visitors to be escorted at all times ¶  3  Guard checks the CCTV monitors and radios in anything odd ¶  4  Locked gate on the fuel depot ¶  5  Restoring the dispatch database from snapshot after corruption
   - [p] Control 1 (Data-loss prevention rule blocking card numbers in outbound email): CATEGORY :: A Technical · B Managerial · C Operational · D Physical = a
   - [p] Control 1 (Data-loss prevention rule blocking card numbers in outbound email): TYPE :: A Preventive · B Deterrent · C Detective · D Corrective · E Compensating · F Directive = a
   - [p] Control 2 (Policy requiring visitors to be escorted at all times): CATEGORY :: A Technical · B Managerial · C Operational · D Physical = b
   - [p] Control 2 (Policy requiring visitors to be escorted at all times): TYPE :: A Preventive · B Deterrent · C Detective · D Corrective · E Compensating · F Directive = f
   - [p] Control 3 (Guard checks the CCTV monitors and radios in anything odd): CATEGORY :: A Technical · B Managerial · C Operational · D Physical = c
   - [p] Control 3 (Guard checks the CCTV monitors and radios in anything odd): TYPE :: A Preventive · B Deterrent · C Detective · D Corrective · E Compensating · F Directive = c
   - [p] Control 4 (Locked gate on the fuel depot): CATEGORY :: A Technical · B Managerial · C Operational · D Physical = d
   - [p] Control 4 (Locked gate on the fuel depot): TYPE :: A Preventive · B Deterrent · C Detective · D Corrective · E Compensating · F Directive = a
   - [p] Control 5 (Restoring the dispatch database from snapshot after corruption): TYPE :: A Preventive · B Deterrent · C Detective · D Corrective · E Compensating · F Directive = d
   - *1: DLP is enforced by a system and stops the email, so technical/preventive. 2: a written rule is managerial and tells people what to do, so directive. 3: a person watching screens is operational and notices events, so detective. 4: a gate is physical and blocks entry, so preventive. 5: restoring after damage is corrective. Hook: paper = managerial, people = operational, systems = technical, touchable = physical.*
   - @1.1.type

21. PBQ 1.2 - AAA. A university IT team is reviewing its access setup. Answer each part.
    - [p] Students type a password and approve a phone prompt before the portal opens :: A Authentication · B Authorization · C Accounting · D Non-repudiation = a
    - [p] Lab printers must present an 802.1X credential before the switch port forwards traffic :: A Authenticating people · B Authenticating systems · C Authorization · D Accounting = b
    - [p] A monthly report lists each user's Wi-Fi session start time and megabytes transferred :: A Authentication · B Authorization · C Accounting · D Non-repudiation = c
    - [p] A lecturer can edit grades for her own modules but only view others :: A Authentication · B Authorization · C Accounting · D Non-repudiation = b
    - *1: password plus phone prompt is two factors proving who the student is, so authentication. 2: a printer proving itself to the port is authenticating a system, not a person; authorization would come after it is identified. 3: recording sessions and usage is accounting, not non-repudiation, which needs proof tied to one signer. 4: deciding what an identified user may do is authorization. Hook: who are you, what may you do, what did you do.*
    - @1.2.aaa

## Test 2 - 1.2 + 1.3 Physical Security, Deception, Change Management (18 Q)

1. A records office wants after-hours motion detection across a large floor split up by plasterboard and fabric partitions, so one sensor cannot see every corner directly. Which sensor type is the BEST fit?
   - **[x] Microwave**  - [ ] Infrared  - [ ] Pressure  - [ ] Access badge
   - *Microwave sensors emit radio-frequency energy and detect changes in the reflected signal; they cover large areas and the signal can pass through thin non-metallic materials such as plasterboard (metal reflects it, which can also cause false alarms beyond the room). Passive infrared needs line of sight to a heat source. Pressure only fires where someone steps. A badge reader logs entry but detects nothing inside. Hook: infrared = heat, pressure = weight, microwave/ultrasonic = bounced waves.*
   - @1.2.phys
2. Strangers keep slipping into a distribution centre alongside delivery drivers. CCTV records them, but nobody stops them, and each case needs a judgement call (is this a new driver's mate or an intruder?). What should be added?
   - **[x] A security guard at the delivery entrance**  - [ ] More cameras with higher resolution  - [ ] Perimeter fencing around the car park  - [ ] Brighter lighting at the loading bay
   - *Guards bring human judgement and an on-the-spot response; cameras only record or alert. Fencing protects the perimeter, but these people come through a legitimate door. Lighting deters and helps cameras but cannot ask "who are you with?". Analogy: a smoke alarm vs a firefighter.*
   - @1.2.phys
3. A data centre has a 2.4 m fence with a single gate. Which statement about the fence is MOST accurate?
   - **[x] It deters and delays, but raises no alert without added sensors**  - [ ] It prevents entry, so a determined attacker cannot reach the building  - [ ] It is a detective control, because guards can see anyone climbing it  - [ ] It is a compensating control for having no vestibule at the door
   - *A fence is a physical control that deters and delays intruders and channels people to the gate, but on its own it detects nothing. The preventive claim is the tempting trap: a determined attacker can climb or cut a fence, so it only slows them. Detection comes from the guards or sensors, not the fence, and nothing here substitutes for a missing primary control, so it is not compensating. Hook: a fence buys time, it does not ring a bell.*
   - @1.2.phys
4. A SOC wants a high-confidence alert if an intruder dumps credentials from the domain and tries to use them. What should they plant?
   - **[x] A honeytoken: a fake admin account that no one ever uses**  - [ ] A honeynet of decoy servers in the DMZ  - [ ] A honeyfile named salaries.xlsx on a share  - [ ] Tokenization of the account database
   - *A honeytoken is fake data (credential, record, API key) whose any use proves compromise. A honeynet catches network exploration, not reuse of a dumped credential. A honeyfile alerts on opening a file. Tokenization replaces real data with substitutes for protection, not bait. Analogy: a map maker's fake street that catches copiers.*
   - @1.2.dcpt
5. A threat research team wants to watch how attackers move laterally between hosts after the initial break-in. Which deception tool is the BEST fit?
   - **[x] Honeynet**  - [ ] Honeypot  - [ ] Honeyfile  - [ ] Honeytoken
   - *Lateral movement needs several hosts to move between, so a network of decoys: honeynet. One honeypot shows the initial attack but nowhere to pivot. Honeyfiles and honeytokens are single bait items. Hook: one pot, many pots = a net.*
   - @1.2.dcpt
6. A manager proposes deploying a honeypot and dropping the planned firewall upgrade to save money. What is the BEST response?
   - **[x] Decline: a honeypot detects and gathers intel but blocks nothing**  - [ ] Approve: attackers drawn to the decoy will leave production alone  - [ ] Approve: the honeypot acts as an IPS once attackers touch it  - [ ] Decline: a honeynet is needed, as one honeypot is too easy to spot
   - *Decline, because deception tools give high-confidence detection and attacker intelligence but enforce nothing, so they layer on top of preventive controls like a firewall rather than replacing them. The diversion argument is the tempting one, but attackers can fingerprint or simply ignore the decoy and go straight for real systems. A honeypot does not block traffic like an IPS, and a honeynet still prevents nothing. Hook: bait is not a lock.*
   - @1.2.dcpt
7. A network team wants to push a firewall rule change on Friday afternoon. The change advisory board refuses to approve it until the team attaches results from the staging lab. Which change management element is the CAB enforcing?
   - **[x] Test results as an input to the approval process**  - [ ] A backout plan  - [ ] A maintenance window  - [ ] Ownership
   - *The approval process relies on evidence: impact analysis and test results show the change works and what it touches. A backout plan is how you undo it. A maintenance window is when you do it. Ownership is who is accountable. Hook: no evidence, no approval.*
   - @1.3.proc
8. Before a mail server migration, the change owner emails the sales director, the help desk lead and the compliance officer to explain what will happen and get their input. Who are these people in change management terms?
    - **[x] Stakeholders**  - [ ] Owners  - [ ] The CAB  - [ ] Approvers of the backout plan
    - *Stakeholders are people affected by or with an interest in the change, who should be informed and consulted. The owner is the one accountable person driving it. The CAB formally approves. Analogy: neighbours told about building work vs the builder who is responsible.*
    - @1.3.proc
9. Every month, junior admins patch the same web servers and occasionally skip the step of draining load-balancer traffic first. What would BEST reduce these errors?
    - **[x] A standard operating procedure for the patch process**  - [ ] A longer maintenance window  - [ ] A new impact analysis for each patch  - [ ] Adding the admins as stakeholders
    - *An SOP documents the exact repeatable steps so routine changes are done the same way every time. A longer window gives more time but not the missed step. Repeating impact analysis for an unchanged routine adds paperwork, not consistency. Stakeholders are consulted, not instructed. Analogy: a pilot's pre-flight checklist.*
    - @1.3.proc
10. A team adds a new monitoring agent to all servers. The next morning, the agent is not running anywhere, and the endpoint protection logs show it was blocked. What was MOST likely missed in the change plan?
    - **[x] Adding the agent to the application allow list**  - [ ] Removing the agent from the deny list on the firewall  - [ ] Scheduling a service restart  - [ ] Updating the network diagram
    - *An allow list permits only approved software; anything new is blocked until added. Change plans must update allow/deny lists. A firewall deny list filters traffic, not local execution. A restart would not get past an allow list. Diagrams matter but did not cause the block. Analogy: a guest list at the door.*
    - @1.3.tech
11. A change to a 15-year-old inventory app is high risk because the vendor has gone, and no one is sure which reporting tools pull data from it. Which technical implications apply? (Select 2)
    - **[x] Legacy application**  - **[x] Dependencies**  - [ ] Restricted activities  - [ ] Deny list
    - *Legacy = old, unsupported, poorly documented, so behaviour after a change is unpredictable. Dependencies = other systems that rely on it and may break. Restricted activities are actions limited to the scope of the approved change; deny lists block named items. Neither is described. Analogy: pulling one brick from an old wall.*
    - @1.3.tech
12. During an approved change to patch a database, an admin notices an unrelated disk-space warning and decides to "quickly" resize a volume too. What should happen?
    - **[x] Stop and raise a separate change request for the resize**  - [ ] Proceed, since the maintenance window covers that server  - [ ] Proceed, then add the resize to the change ticket afterward  - [ ] Proceed only if the patch's backout plan also covers it
    - *The approval covers the database patch only, so any other work is a restricted activity that needs its own request, impact analysis and backout plan. Adding it to the ticket afterward is the tempting shortcut, but documentation after the fact is not approval. An open window says when work may happen, not what work, and the patch's backout plan was never written for a volume resize. Hook: approved means THIS change, not any change.*
    - @1.3.tech
13. After a VLAN redesign goes live, a responder in a drill isolates the wrong segment because the playbook still lists the old address ranges. Which TWO updates were MOST clearly missed? (Select 2)
    - **[x] Network diagrams**  - **[x] IR policies and procedures that reference addressing**  - [ ] The backout plan for the VLAN change  - [ ] The stakeholder list for the change
    - *Change management ends with documentation: diagrams and the policies and procedures that depend on them must match the new network, or responders act on stale data. The backout plan is tempting, but it only describes how to undo the change and is not what responders use day to day. The stakeholder list says who to consult, not where systems live. Hook: update the map after the new road opens.*
    - @1.3.doc
14. A firewall config was edited by three admins this month, and one edit broke a partner connection. The team must find which edit caused it and undo only that one, keeping the other two. What should they have in place?
    - **[x] Version control for the configuration files**  - [ ] Nightly full backups of the firewall configuration  - [ ] A documented backout plan for each change  - [ ] Centralised syslog of firewall traffic
    - *Version control records each edit with its author and time and lets you revert one specific change while keeping later ones. Nightly backups are the tempting choice, but restoring one rolls back every edit since that snapshot and shows no authorship per line. A backout plan undoes a whole change, not a selected edit, and traffic logs show packets, not config history. Hook: page history for configs.*
    - @1.3.doc

### Key facts
- **Physical: bollards, access control vestibule, fencing, video surveillance, guards, access badges, lighting, sensors (infrared = heat, pressure = weight, microwave and ultrasonic = reflected waves).**
- **Honeypot = decoy system; honeynet = decoy network; honeyfile = decoy file; honeytoken = decoy datum.**
- **Change management: approval, ownership, stakeholders, impact analysis, test results, backout plan, maintenance window, SOP. Technical: allow/deny lists, restricted activities, downtime, service/application restart, legacy apps, dependencies. Docs: diagrams, policies/procedures, version control.**
15. A firmware change on a VPN concentrator failed and remote staff were cut off for four hours while engineers worked out how to roll back. Which part of the change process was MOST clearly missing?
   - **[x] A backout plan**  - [ ] A stakeholder list  - [ ] An allow list update  - [ ] A maintenance window
   - *A backout plan documents exactly how to return to the previous state, which turns a four-hour hunt into a quick rollback. A maintenance window limits who is hurt but does not shorten the outage. Hook: no backout plan, no change.*
   - @1.3.proc
16. Which sequence BEST reflects a sound change management process?
   - **[x] Request, impact analysis, testing, approval, implementation, documentation**  - [ ] Request, approval, impact analysis, testing, implementation, documentation  - [ ] Request, impact analysis, approval, implementation, testing, documentation  - [ ] Request, testing, approval, impact analysis, implementation, documentation
   - *Impact analysis and test results are inputs to the approval decision, so both come before approval, then implementation, then documentation. Approving first and analysing later is the tempting order, but then the CAB approves without evidence. Testing after implementation tests in production, and analysing impact after approval is too late to change the decision. Hook: no evidence, no approval.*
   - @1.3.proc
17. PBQ 1.4 - Physical security for a new branch. Pick the best control for each spot. ¶  Spot 1  Glass storefront where a car could mount the kerb from a busy road ¶  Spot 2  Staff entrance where people let whoever is behind them walk through ¶  Spot 3  Cash room where every entry must be tied to a named person ¶  Spot 4  Unstaffed back office that should raise an alarm if anything moves after hours ¶  Spot 5  Rear alley where staff leave at closing and cameras show only shadows at night
   - [p] Spot 1 (Glass storefront where a car could mount the kerb) :: A Bollards · B Access control vestibule · C Access badge · D Ultrasonic sensor · E Lighting · F Fencing = a
   - [p] Spot 2 (Staff entrance where people let whoever is behind them through) :: A Bollards · B Access control vestibule · C Access badge · D Ultrasonic sensor · E Lighting · F Fencing = b
   - [p] Spot 3 (Cash room where every entry must be tied to a named person) :: A Bollards · B Access control vestibule · C Access badge · D Ultrasonic sensor · E Lighting · F Fencing = c
   - [p] Spot 4 (Unstaffed back office that should alarm on movement after hours) :: A Bollards · B Access control vestibule · C Access badge · D Ultrasonic sensor · E Lighting · F Fencing = d
   - [p] Spot 5 (Rear alley where cameras show only shadows at night) :: A Bollards · B Access control vestibule · C Access badge · D Ultrasonic sensor · E Lighting · F Fencing = e
   - [p] Spot 6, investigators need to see who actually stood at the cash room door, even if a badge was borrowed :: A Video surveillance · B Access badge · C Access control vestibule · D Security guard = a
   - [p] Spot 7, a dark stockroom corridor where the sensor should react to a person's warmth but not to boxes moving on a conveyor :: A Infrared sensor · B Pressure sensor · C Microwave sensor · D Ultrasonic sensor = a
   - [p] Spot 8, the floor directly in front of the safe, alarming only when someone stands on that exact spot :: A Infrared sensor · B Pressure sensor · C Microwave sensor · D Ultrasonic sensor = b
   - *1: bollards stop vehicles while letting pedestrians pass; fencing would block customers too. 2: a vestibule lets one person through at a time and defeats tailgating, which a badge reader alone does not. 3: a personal badge logs each entry against a named person. 4: an ultrasonic sensor bounces sound waves and detects motion anywhere in the room. 5: lighting deters and lets cameras see. 6: video shows the actual face, which a badge log cannot. 7: infrared reacts to body heat, while microwave and ultrasonic react to any movement. 8: pressure reacts to weight on one spot. Hook: posts for cars, airlock for tailgaters, badge for the log, sensor for the empty room, light for the alley.*
   - @1.2.phys

18. PBQ 1.5 - Deception triage. Four alerts fire overnight. Name the decoy that raised each.
   - [p] Someone opened "VPN_passwords.docx" on the HR share :: A Honeypot · B Honeynet · C Honeyfile · D Honeytoken = c
   - [p] A fake AWS key planted in an old Git repo was used from 203.0.113.50 :: A Honeypot · B Honeynet · C Honeyfile · D Honeytoken = d
   - [p] An attacker scanned and logged into a lone fake SSH server at 198.51.100.20 :: A Honeypot · B Honeynet · C Honeyfile · D Honeytoken = a
   - [p] The same attacker hopped across six decoy hosts in a fake subnet :: A Honeypot · B Honeynet · C Honeyfile · D Honeytoken = b
   - *File = honeyfile. Fake credential/key = honeytoken. One fake system = honeypot. Many decoy systems = honeynet. Hook: pot = one, net = many, file = a document, token = a fake datum.*
   - @1.2.dcpt

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
   - **[x] Dual control: two custodians must jointly approve each release**  - [ ] Encrypt every escrowed key under the custodian's master key  - [ ] Send every key release to the custodian's SIEM for review  - [ ] Rotate all escrowed keys every 90 days
   - *Dual control (often implemented as M of N) means no single person can release a key alone, which directly stops one rogue administrator. Logging releases to a SIEM is tempting, but it is detective: it tells you after the key has gone. Do not confuse it with split knowledge, where each person holds only part of the key. A master key held by the same custodian still lets that admin decrypt everything, and rotation only shortens how long a stolen key stays useful. Hook: two keys to open the vault.*
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
   - **[x] Asymmetric agrees a session key; symmetric then encrypts the traffic**  - [ ] Symmetric agrees a session key; asymmetric then encrypts the traffic  - [ ] Asymmetric encrypts the traffic; symmetric hashes it for integrity  - [ ] Asymmetric signs each packet; symmetric authenticates the server
   - *Asymmetric methods solve sharing a secret between strangers, then the much faster symmetric cipher carries the bulk data with the agreed session key. The reversed version is the tempting trap: asymmetric is far too slow for bulk traffic, and a symmetric key cannot be agreed safely without already sharing a secret. Symmetric ciphers do not hash, and the server is authenticated by its certificate signature, an asymmetric operation. Hook: asymmetric moves the key, symmetric moves the data.*
   - @1.4.kex
9. Two branch routers that have never shared a secret must create the same session key over the internet, and an eavesdropper recording every packet must not be able to work it out. Which method is designed for this?
   - **[x] Diffie-Hellman key exchange**  - [ ] Sending the key in a password-protected ZIP  - [ ] Hashing the key with SHA-256 before sending it  - [ ] Steganography to hide the key in an image
   - *Diffie-Hellman (and its elliptic curve form, ECDH) lets both sides compute the same secret from exchanged public values without ever transmitting the secret. A ZIP password still has to be shared somehow. A hash cannot be reversed into a usable key at the other end. Steganography hides data but is not a key-agreement protocol. Hook: DH = mix paint colours in public, only the two of you get the same final colour.*
   - @1.4.kex
10. An architect proposes moving signing keys from RSA-2048 to ECC for a fleet of low-power IoT sensors. What is the MAIN advantage of ECC here?
    - **[x] Similar strength from much shorter keys, so less CPU and bandwidth**  - [ ] Faster encryption, since ECC is a symmetric stream cipher  - [ ] Built-in forward secrecy with no key exchange needed  - [ ] Resistance to the quantum attacks that break RSA
    - *ECC reaches strength comparable to RSA with far smaller keys, about 256-bit ECC versus RSA-3072, which suits constrained devices. Quantum resistance is the tempting distractor, but Shor's algorithm breaks ECC as well as RSA, so it is not post-quantum. ECC is asymmetric, not a stream cipher, and forward secrecy comes from ephemeral key exchange such as ECDHE, not from ECC itself. Hook: same lock strength, smaller key.*
    - @1.4.keylen
11. A packet capture on the office LAN shows HR portal usernames and passwords readable in cleartext as staff log in. What is the BEST fix?
    - **[x] Enable TLS on the portal and redirect all requests to it**  - [ ] Enable full-disk encryption on the portal's server  - [ ] Store the portal's passwords as salted bcrypt hashes  - [ ] Move the portal onto an isolated HR-only VLAN
    - *The credentials are exposed in transit, so transport encryption with TLS fixes it, with a redirect so nobody stays on the cleartext path. Salted bcrypt hashing is tempting because it protects passwords, but only the stored copies, not the ones crossing the wire. FDE protects data at rest on a stolen disk, and a VLAN shrinks who can sniff while anyone on it still sees cleartext. Hook: match the encryption to where the data is.*
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
16. Call-centre agents confirm callers by asking for two characters of their national insurance number. A privacy review says agents must not be able to read the whole number, but the CRM must keep it intact for payroll exports. Which BEST meets this?
    - **[x] Data masking in the agents' CRM view**  - [ ] Tokenization of the number in the CRM  - [ ] Encryption of the CRM database at rest  - [ ] Salted hashing of the stored number
    - *Masking hides part of a value at display time while the system keeps the real data, so agents see only what they need and exports still work. Tokenization is tempting, but it replaces what is stored, breaking the payroll export that needs the real number. Encryption at rest still shows the full value to an authorised agent on screen, and a hash cannot be turned back into the number. Hook: masking = what you see, tokenization = what is stored.*
    - @1.4.obf
17. DLP shows nothing unusual, yet a departing engineer's holiday photos on a personal blog are each several MB larger than his camera normally produces, and they open and look normal. What should the analyst suspect?
    - **[x] Steganography concealing data inside the photos**  - [ ] Encryption of the photos so DLP cannot inspect them  - [ ] Tokenization of design files into the photo metadata  - [ ] Data masking of the files to slip past DLP rules
    - *Steganography hides data inside a normal-looking carrier file, so the photo still opens fine while content filters miss the payload, and unusual size is a classic clue. Encryption is tempting because it also defeats DLP, but an encrypted photo would not open as a normal image. Tokenization and masking protect data by replacing or hiding values, they do not carry it out. Hook: invisible ink on a postcard.*
    - @1.4.steg
18. A review of a legacy file-transfer tool finds it encrypts data with DES and RC4. Which recommendation is BEST?
    - **[x] Replace them with AES, using a 256-bit key where possible**  - [ ] Keep DES but double the number of times each file is encrypted  - [ ] Replace them with SHA-256  - [ ] Replace them with RSA for all bulk data
    - *Algorithm choice matters as much as key length: DES (56-bit key) and RC4 are deprecated and breakable. AES is the current symmetric standard, and a longer key (AES-256) gives the most brute-force resistance. Re-running a weak cipher keeps its weakness (3DES is itself deprecated). SHA-256 is a hash, not encryption. RSA is too slow for bulk data. Hook: old ciphers retire; AES is the default.*
    - @1.4.sym

### Key facts
- **Encrypt for confidentiality with the recipient's public key; sign with your own private key. Key escrow = a trusted third party holds key copies; risk = extra copy, mitigate with dual control.**
- **Levels: full-disk, partition, volume, file, database, record; transport = data in transit. Symmetric (AES) for bulk, asymmetric (RSA, ECC) for key exchange and signatures; DH agrees keys without sending them. Longer keys = stronger but slower; ECC = shorter keys for similar strength.**
- **Tools: TPM (per device), HSM (dedicated tamper-resistant hardware), KMS (central key lifecycle), secure enclave (isolated processor area).**
- **Obfuscation: steganography (hide data in other files), tokenization (random substitute, real value in a vault), data masking (hide part of a value).**
19. PBQ 1.7 - Encryption choices. A hospital trust lists nine data protection needs. Pick the BEST option for each.
    - [p] Ward tablets are often left in corridors; a thief must get nothing, including cached and swap data :: A Full-disk · B File · C Transport · D Masking = a
    - [p] Research data where one stolen key must expose only one patient :: A Full-disk · B Record · C Volume · D Database = b
    - [p] Lab results travelling between two hospital systems over the WAN :: A File · B Database · C Transport (TLS) · D Record = c
    - [p] Algorithm for encrypting a nightly 2 TB imaging archive in a short window :: A RSA · B AES · C SHA-256 · D ECC = b
    - [p] Two sites must derive a shared secret without ever sending it :: A Diffie-Hellman · B AES · C RSA signature · D Key escrow = a
    - [p] A shared ward PC keeps patient data on D:, but C: must stay unencrypted for a legacy tool :: A Partition · B Record · C Full-disk · D File = a
    - [p] A spreadsheet emailed to auditors that must stay protected wherever it is copied :: A File · B Volume · C Database · D Transport = a
    - [p] A LUN on the SAN carved out for imaging data :: A Volume · B Record · C File · D Partition = a
    - [p] The DBA wants the engine itself to encrypt all tables and logs at rest with no app changes :: A Database · B Record · C Volume · D Transport = a
    - *1: full-disk covers everything on the device, including caches and swap; file-level misses copies the OS writes. 2: record-level gives each row its own key, so one key exposes one patient. 3: data in motion needs transport encryption. 4: AES is fast symmetric bulk encryption; RSA and ECC are slow asymmetric, SHA-256 is a hash. 5: Diffie-Hellman derives a shared secret without sending it. 6: partition encryption covers one partition and leaves the other clear. 7: file encryption travels with the file, while transport only protects the email in transit. 8: a SAN LUN is a logical volume. 9: database encryption is applied by the engine across the whole database. Hook: where is the data, and how big is it?*
    - @1.4.enclvl

20. PBQ 1.8 - Crypto tools and obfuscation. Match each requirement at a bank to the BEST tool or technique.
    - [p] The root CA signing key needs FIPS 140-2 Level 3 certified hardware serving several CA servers :: A TPM · B HSM · C Secure enclave · D Key management system = b
    - [p] A laptop's disk key sealed to the boot measurements of that one machine :: A TPM · B HSM · C Secure enclave · D Key management system = a
    - [p] One cloud service that issues, rotates and logs use of encryption material for 300 apps :: A TPM · B HSM · C Secure enclave · D Key management system = d
    - [p] A mobile banking app keeps biometric templates out of reach of a compromised phone OS :: A TPM · B HSM · C Secure enclave · D Key management system = c
    - [p] Testers need realistic-looking customer records without seeing real account numbers :: A Data masking · B Steganography · C Key stretching · D Salting = a
    - [p] The core system swaps card numbers for stand-ins with no mathematical link, yet a vault can map them back for refunds :: A Hashing · B Tokenization · C Masking · D Encryption = b
    - *1: an HSM is dedicated certified crypto hardware for high-value keys; a TPM is per device and not built for CA throughput. 2: a TPM is a chip in one machine that measures boot. 3: a KMS manages key lifecycle centrally for many apps, while an HSM is the hardware it may sit on. 4: a secure enclave is an isolated processor area the main OS cannot read. 5: masking hides real values for display or test data. 6: tokens are random stand-ins mapped in a vault; hashes and ciphertext are derived from the data and encryption is reversible with the key. Hook: TPM per box, HSM per vault, KMS per fleet, enclave per phone.*
    - @1.4.tool

## Test 4 - 1.4 Cryptography II: Hashing, Salting, Signatures, Certificates (19 Q)

1. A sysadmin downloads a hypervisor ISO from a mirror site. The vendor's own page lists a SHA-256 value for the file. What does comparing the two values prove?
   - **[x] The file is unaltered from the copy the vendor hashed**  - [ ] The vendor signed the file, proving who published it  - [ ] The file is free of malware and safe to install  - [ ] The mirror delivered the file over an encrypted channel
   - *A matching hash proves integrity: any change, even one bit, gives a completely different digest. The signature option is tempting, but a bare hash proves no origin or non-repudiation; that needs the vendor's private key. If the vendor itself shipped malware the hash would still match, and the hash says nothing about how the file was transported. Hook: hash = fingerprint, signature = sealed fingerprint.*
   - @1.4.hash
2. A legacy document system still uses MD5 to detect changes in stored contracts. Researchers have shown two different files can be crafted with the same MD5 value. What is the BEST recommendation?
   - **[x] Replace MD5 with SHA-256 for the change checks**  - [ ] Replace MD5 with SHA-1 for the change checks  - [ ] Keep MD5 but add a unique salt to each file's hash  - [ ] Encrypt each contract with AES-256 instead of hashing it
   - *SHA-256 from the SHA-2 family has no practical collisions, so it restores trust that a changed file will be detected. SHA-1 is the tempting upgrade, but practical SHA-1 collisions have also been demonstrated and it is deprecated. Salting defends passwords against precomputed tables, not crafted collisions, and AES gives confidentiality, not a change fingerprint. Hook: a hash is only as good as its collision resistance.*
   - @1.4.hash
3. After a breach, analysts notice that 214 accounts in the stolen password table share exactly the same stored value, and it matches a well-known value for "Summer2024!". What weakness does this reveal?
   - **[x] Passwords were hashed without a unique salt per user**  - [ ] Passwords were encrypted with a key that was too short  - [ ] Passwords were stored with key escrow  - [ ] Passwords were tokenized instead of masked
   - *A salt is a random value added to each password before hashing, so identical passwords give different hashes. Without it, the same password always yields the same value and can be looked up in precomputed tables. Key length relates to encryption, and passwords should be hashed, not encrypted. Escrow and tokenization do not apply. Hook: salt makes every hash unique.*
   - @1.4.salt
4. An attacker has a huge precomputed table of hashes for common passwords. Which change to the password store BEST makes that table useless?
   - **[x] Add a unique random salt to each password before hashing**  - [ ] Switch the hash algorithm from SHA-256 to SHA-512  - [ ] Encrypt the password table with AES-256 at rest  - [ ] Enforce a 30-day password expiry for every user
   - *A unique salt means each password hashes differently, so the attacker would need a separate table per salt, which is impractical. Switching to SHA-512 is tempting, but a table can simply be rebuilt for any unsalted algorithm. Encryption at rest does not help once the table contents are stolen with the key or from memory, and frequent expiry pushes users to predictable passwords. Hook: every lock gets its own cut.*
   - @1.4.salt
5. A start-up already salts its SHA-256 password hashes, yet a red team cracked 40% of a stolen copy overnight on a GPU rig. What should it add?
   - **[x] Key stretching such as PBKDF2 or bcrypt**  - [ ] A longer 64-byte salt for each user  - [ ] A switch from SHA-256 to SHA-512  - [ ] AES encryption of the stored hashes
   - *Key stretching runs the hash many thousands of times, so every guess costs the attacker real time while one login stays quick. A longer salt is tempting, but salts only defeat precomputed tables; the GPU is guessing each salted hash directly. SHA-512 is still built for speed, and encrypting hashes helps only if the key was not stolen too. Hook: salt beats precomputation, stretching beats speed.*
   - @1.4.stretch
6. A vendor signs its software updates. When a client receives an update, which key does it use to verify the signature?
   - **[x] The vendor's public key**  - [ ] The vendor's private key  - [ ] The client's private key  - [ ] A shared symmetric key from the vendor
   - *The vendor signs with its private key; anyone verifies with the matching public key, usually taken from the vendor's certificate. If a client needed the vendor's private key, the key would no longer be private. The client's own keys play no part. Symmetric keys cannot give non-repudiation because both sides hold them. Hook: sign private, verify public.*
   - @1.4.sig
7. An endpoint agent refuses to install a driver update because its digital signature fails verification, although the file name and size look normal. What is the BEST next action?
   - **[x] Block it and obtain a fresh copy from the vendor's official source**  - [ ] Install it if its SHA-256 matches the hash on the download page  - [ ] Install it if the vendor's certificate is not on the CRL  - [ ] Re-sign it with the company's own code-signing certificate
   - *A failed signature means the file was changed or was not signed by the vendor, so it must be blocked and replaced from a trusted source. A matching hash is tempting, but if the file came from a tampered page the hash can be tampered too, and it cannot outweigh a broken signature. A non-revoked vendor certificate says nothing about this altered file, and re-signing would vouch for code you cannot trust. Hook: a broken seal means do not drink.*
   - @1.4.sig
8. Which process BEST describes how a digital signature is created for an email?
   - **[x] Hash the message, then encrypt the hash with the sender's private key**  - [ ] Encrypt the message with the recipient's public key, then hash it  - [ ] Hash the message with a salt and send the salt separately  - [ ] Encrypt the message with a shared AES key known to both sides
   - *The signature is the message digest encrypted with the sender's private key. The recipient decrypts it with the sender's public key and compares it with their own hash of the message: a match proves integrity, authenticity and non-repudiation. Encrypting with the recipient's public key is confidentiality, not signing. Salts are for password storage. A shared AES key cannot prove which party wrote it. Hook: signature = sealed fingerprint.*
   - @1.4.sig
9. A group of shipping firms want a shared record of container handovers that no single firm can quietly edit after the fact. Why is a blockchain-based open public ledger a good fit?
   - **[x] Each block carries the previous block's hash and every party holds a copy**  - [ ] Each block is encrypted so only the firm that wrote it can read it  - [ ] A trusted central CA signs every entry and can revoke false ones  - [ ] Each entry is tokenized so container numbers stay private
   - *Hash chaining means altering an old block breaks every later link, and because every participant holds the ledger, tampering is evident. A central CA is tempting because signatures do give integrity, but a central authority that can revoke or rewrite entries is exactly the single point of control the ledger avoids. Encryption and tokenization give secrecy, while an open ledger is about transparency. Hook: every page quotes the page before it.*
   - @1.4.chain
10. A company's public online store shows browser warnings because it uses a self-signed certificate. What is the BEST fix?
    - **[x] Replace it with a certificate from a public third-party CA**  - [ ] Replace it with a certificate from the company's private CA  - [ ] Reissue the self-signed certificate with a 4096-bit key  - [ ] Replace it with a self-signed wildcard for the domain
    - *Customers' browsers only trust certificates that chain to a root already in their trust store, which for a public site means a public third-party CA. The private CA is tempting, but its root exists only on managed company devices, so customers still see warnings. A longer key or a wildcard is still self-signed and still untrusted. Hook: self-signed = vouching for yourself.*
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
    - **[x] Revoke the old certificate so it appears on the CRL and in OCSP**  - [ ] Nothing more, since the new certificate supersedes the old one  - [ ] Securely delete the old key and certificate from the server  - [ ] Enable forward secrecy so past sessions cannot be decrypted
    - *Revocation publishes the old certificate as untrusted through the CRL and OCSP, so clients reject it even when an attacker presents it with the stolen key. Secure deletion is tempting, but it only removes your copy; the attacker's copy stays valid until revoked. A new certificate does not cancel the old one, and forward secrecy protects past sessions, not future impersonation. Hook: rotate AND revoke.*
    - @1.4.revoke
15. A bank wants clients to check a certificate's revocation status in real time for each connection, rather than downloading a large list that may be hours old. What should it rely on?
    - **[x] OCSP**  - [ ] CRL  - [ ] CSR  - [ ] Wildcard certificates
    - *OCSP (online certificate status protocol) answers "is this one certificate still good?" on demand. A CRL is a periodically published list the client must download and may be out of date. A CSR is a request for a new certificate. Wildcards are a naming option. Hook: CRL = printed list, OCSP = phone the bank.*
    - @1.4.revoke
16. A developer needs HTTPS for a throwaway test VM that only she will use for an afternoon. Which choice is MOST appropriate?
    - **[x] A self-signed certificate**  - [ ] A wildcard certificate from a public CA  - [ ] An extended validation certificate from a public CA  - [ ] A certificate signed by the company's root CA private key directly
    - *Self-signed certificates are free and instant, fine for short-lived internal testing where you control the only client. Public CA certificates cost time or money and a public wildcard would put a high-value key on a throwaway VM. Using the root CA key directly for a test box puts the organisation's root of trust at risk. Hook: self-signed for the lab, CA-signed for anyone else.*
    - @1.4.cert
17. A company builds an internal PKI. Its architect keeps the root CA powered off in a safe and uses an online intermediate CA to issue everyday certificates. Why?
    - **[x] A breached intermediate can be revoked without replacing the root**  - [ ] An offline root's certificates never need to be revoked  - [ ] The root escrows the intermediate's key so it can be recovered  - [ ] Clients validate chains faster when the root is not online
    - *Every device trusts the root in its store, so keeping the root offline protects that anchor, and if the online intermediate is compromised the root simply revokes it and signs a new one. The never-revoked option is tempting, but offline only lowers the chance of compromise; any certificate can still need revocation. CAs do not escrow subordinate keys as a design goal, and clients validate using the stored root certificate, not a live root. Hook: the crown stays in the vault, the deputy signs the paperwork.*
    - @1.4.cert

### Key facts
- **Hashing = one-way fingerprint for integrity; use SHA-256, avoid MD5 (collisions). Salt = unique random value per password, defeats rainbow tables. Key stretching (PBKDF2, bcrypt) slows each guess.**
- **Digital signature = hash encrypted with the sender's private key; verify with the sender's public key. Gives integrity, authenticity, non-repudiation.**
- **Blockchain = hash-linked blocks on a distributed open public ledger; tampering is evident.**
- **Certificates: CA signs; root of trust = root CA in the trust store; self-signed = untrusted outside your control; third-party CA for public sites; CSR holds public key + identity; wildcard = one label (*.example.com); revoke via CRL (list) or OCSP (real-time query).**
18. PBQ 1.9 - Password store review. A developer proposes how a new app will store passwords. Pick the BEST choice for each part.
    - [p] Stored form of each password :: A AES-encrypted · B Hashed · C Base64-encoded · D Tokenized = b
    - [p] Hash algorithm :: A MD5 · B SHA-256 · C CRC32 · D Base64 = b
    - [p] Salt policy :: A One salt for all users · B A random unique salt per user · C No salt · D The username as salt = b
    - [p] Defence against fast GPU guessing :: A Key stretching (bcrypt or PBKDF2) · B Shorter salt · C Data masking · D Steganography = a
    - [p] Where the salt is stored :: A Alongside each hash · B Kept secret in an HSM only · C Sent to the user by email · D Not stored at all = a
    - *1: hashing is one-way, so a stolen store reveals no plaintext; encryption can be reversed by anyone with the key. 2: MD5 has known collisions, CRC32 is a checksum, Base64 is encoding. 3: a unique random salt makes identical passwords hash differently. 4: stretching makes every guess expensive. 5: salts are not secrets; they are stored with the hash so the system can recompute it at login. Hook: hash, salt, stretch.*
    - @1.4.salt

19. PBQ 1.10 - Certificate lifecycle. A retailer is setting up TLS for shop.example.net and its sister sites. Answer each part.
    - [p] First step on the web server :: A Generate a key pair and CSR · B Request the CA's private key · C Send the server's private key to the CA · D Self-sign a root = a
    - [p] Who signs it so customers' browsers accept it without warnings :: A The web server itself · B A trusted third-party CA · C The company's private CA · D The OCSP responder = b
    - [p] One certificate for www, shop and pay under example.net :: A Wildcard *.example.net · B Wildcard *.shop.example.net · C Self-signed for example.net · D Root CA certificate = a
    - [p] Why the browser trusts it :: A It chains to a root CA in the trust store · B It was issued from a CSR · C It uses a 4096-bit key · D It appears on the CRL = a
    - [p] The server's private key is later stolen. What should the CA publish? :: A Revocation via the CRL and OCSP · B A renewed certificate with the same key · C An updated CSR · D A new root certificate = a
    - *1: the server generates its own key pair and CSR; private keys never leave it. 2: public trust needs a third-party CA; a private CA's root is not in customers' stores. 3: a wildcard at the example.net level covers one label, so www, shop and pay; the shop-level wildcard covers only names under shop. 4: trust comes from chaining to a stored root, and appearing on a CRL means revoked. 5: a stolen key means revocation; renewing with the same key keeps it compromised. Hook: request, sign, trust, revoke.*
    - @1.4.cert

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
   - **[x] Internal, low sophistication, using legitimate access**  - [ ] Internal, high sophistication, using privilege escalation  - [ ] Internal, high resources, using custom malware  - [ ] Internal, unintentional, breaking policy by accident
   - *Insiders already hold credentials and know where the data is, so the attack costs little skill or money. The unintentional option is tempting, but deliberately copying the customer table on her last day is a malicious act, not an accident. She needed no escalation or custom malware, because her own access was enough. Hook: the threat already has a badge.*
   - @2.1.insider
7. Which control would BEST reduce the impact of the insider in the previous scenario before she leaves?
   - **[x] Remove her privileged access at notice and add DLP on uploads**  - [ ] Raise logging on her account so any copying is recorded  - [ ] Have her re-sign the acceptable use policy before leaving  - [ ] Enforce MFA on her account for all database logins
   - *Insiders bypass the perimeter, so you cut their access when risk rises and block data leaving through DLP. Extra logging is tempting, but it is detective and only tells you after the table has gone. Re-signing a policy deters only the honest, and MFA proves it is her, which is exactly the problem. Hook: lock the inside door, not just the front gate.*
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
11. Marketing staff sign up for an AI transcription service with company cards and upload recorded client calls to save time. Security has never assessed the service. What is this an example of, and what is the MAIN risk?
    - **[x] Shadow IT; client data in an unassessed external service**  - [ ] Insider threat; deliberate exfiltration of client data  - [ ] Supply chain attack; a compromised vendor tool  - [ ] Hacktivism; client recordings leaked for publicity
    - *Shadow IT is staff using technology outside approved channels, usually with good intent, which puts data in services with no security review, contract or monitoring. Insider threat is tempting because staff moved data out, but the intent was productivity, not theft. Nothing says the vendor was compromised, and no cause or publicity is involved. Hook: helpful, hidden, unmanaged.*
    - @2.1.shadowit
12. A CISO wants to reduce shadow IT without killing productivity. What is the BEST first step?
    - **[x] Discover unsanctioned apps, then offer approved alternatives**  - [ ] Block every unapproved SaaS domain at the web proxy  - [ ] Add a shadow IT clause to the acceptable use policy  - [ ] Require MFA on all corporate accounts
    - *Shadow IT exists because users need something, so first find it, for example with CASB or proxy logs, then provide a sanctioned option and a request process. Blanket blocking is tempting, but it stops work and pushes users to personal devices, making the problem less visible. A policy clause alone changes little, and MFA protects corporate logins, not data sent to unsanctioned apps. Hook: find it, then replace it.*
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
18. A botnet floods a payment processor's servers throughout Black Friday. No data is touched and no demand arrives; weeks later, intel shows the processor's rival paid the botnet operators. Which motivation BEST describes the attack?
    - **[x] Service disruption**  - [ ] Disruption or chaos  - [ ] Blackmail  - [ ] Data exfiltration
    - *Service disruption fits because the attack had a specific goal, knocking a named service over at its busiest time, and someone paid for exactly that outcome. Disruption or chaos is tempting because no demand arrived, but chaos is mayhem for its own sake with no target benefit. Nothing was threatened, so not blackmail, and no data left. Hook: a hired outage is targeted disruption, not random chaos.*
    - @2.1.motivdisrupt
19. Over three nights, NetFlow shows 40 GB of design files leaving an aerospace firm to an overseas host. No ransom, leak or public claim follows. Which motivation is MOST likely?
    - **[x] Data exfiltration for espionage**  - [ ] Data exfiltration for financial gain  - [ ] Data exfiltration for blackmail  - [ ] Data exfiltration for revenge
    - *Large quiet transfers of design data with no follow-up point to espionage: the thief wants to use the information, not monetise or publicise it. Financial gain is tempting, but criminals usually demand payment or sell visibly, and nothing followed. Blackmail requires a threat, and revenge actors want visible harm. Hook: the data left and went silent.*
    - @2.1.motiv
20. An intel report describes a state-sponsored group that has kept hidden footholds in several ministries for years, quietly returning whenever it is cleaned out. What term BEST describes this kind of threat?
    - **[x] Advanced persistent threat (APT)**  - [ ] Insider threat  - [ ] Hacktivist campaign  - [ ] Unskilled attacker
    - *APT = a well-funded, skilled actor (usually a nation-state) that gets in, stays hidden and keeps coming back over a long period. Insiders already belong to the organisation; hacktivists want attention; unskilled attackers lack the skill to stay hidden. Hook: advanced tools, persistent presence.*
    - @2.1.nation

- **Actors: nation-state, unskilled attacker, hacktivist, insider, organized crime, shadow IT. Attributes: internal/external, resources/funding, sophistication. Motives: exfiltration, espionage, service disruption, blackmail, financial gain, philosophical/political, ethical, revenge, disruption/chaos, war.**
21. PBQ 2.1 - Actor profiles. Match each incident to the MOST likely actor, then its main motivation. ¶  1  Ransomware with a leak-site threat against a law firm ¶  2  Defacement of an oil company site with a climate message ¶  3  Sales team running an unapproved file-sharing app ¶  4  Months-long silent access to a ministry's email ¶  5  Teen running a downloaded DDoS tool against a school
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

## Test 6 - 2.2 Threat Vectors, Attack Surfaces, Social Engineering (24 Q)

1. Staff at a logistics firm receive texts saying "Your parcel is held, pay the 1.99 redelivery fee" with a short link. Which vector is this?
   - **[x] Smishing**  - [ ] Vishing  - [ ] Phishing  - [ ] Brand impersonation
   - *Smishing is phishing delivered over SMS, and the lure here arrives as a text message. Phishing is tempting because it is the umbrella term, but on the exam it means the email form. Vishing is voice, and brand impersonation may be part of the lure but is not the delivery channel. Hook: S for SMS.*
   - @2.2.msg
2. An attacker sends a team chat message from a compromised partner account with a link to a "shared invoice". Which control would BEST reduce this vector?
   - **[x] Restrict external chat access and scan links in messages**  - [ ] Enforce phishing-resistant MFA on all staff chat accounts  - [ ] Sandbox all email attachments at the mail gateway  - [ ] Block removable media on all user endpoints
   - *Instant messaging is a message-based vector, so limit who outside can message in and inspect links where they arrive. MFA is tempting, but the partner's account is already compromised, so your own users' MFA does nothing about the malicious link. A mail gateway does not see chat traffic, and removable media is a different vector. Hook: the vector is the conversation, so control the conversation.*
   - @2.2.msg
3. A marketing PC is infected when a user simply previews a forum post. The payload was a crafted PNG that triggered a parsing flaw in the renderer. Which vector BEST describes this?
   - **[x] Image-based**  - [ ] Message-based  - [ ] Removable device  - [ ] Unsecure network
   - *Image-based vectors hide exploit code in image files, here a malformed PNG that the renderer mishandles. Message-based is tempting because it arrived in a post, but the malicious content is the image, not a message lure. Nothing was plugged in, and the network carried the file normally. Hook: a picture worth a thousand exploits.*
   - @2.2.file
4. A finance team receives a spreadsheet titled "Q3 bonuses" from an outside address. Opening it and clicking Enable Content launches a downloader. What is the BEST mitigation for this file-based vector?
   - **[x] Block macros in internet files and sandbox attachments**  - [ ] Enforce SPF, DKIM and DMARC checks on inbound mail  - [ ] Apply DLP rules to outbound finance email  - [ ] Require S/MIME signing on internal finance email
   - *The payload is the document's active content, so blocking macros in internet-sourced files and detonating attachments in a sandbox stops it. SPF, DKIM and DMARC are tempting, but they verify the sending domain, and an attacker can send from a legitimately configured domain of their own. DLP watches data leaving, and S/MIME signs your own mail. Hook: the file is the payload, so treat files with suspicion.*
   - @2.2.file
5. A caller claiming to be from the bank's fraud team asks a payroll clerk to read out the code just texted to her phone. Which attack is this?
   - **[x] Vishing**  - [ ] Smishing  - [ ] Watering hole  - [ ] Brand impersonation on a website
   - *Vishing = voice phishing; the call is the vector even though a text is involved, because the code is extracted by voice. Smishing would be a lure in the SMS itself. Hook: V for voice.*
   - @2.2.voice
6. Reception staff find a thumb drive marked "Bonus list - confidential" near the entrance and insert it into the visitor-badge PC to find its owner. Which control BEST blocks this vector?
   - **[x] Device control blocking unapproved removable media, plus training**  - [ ] Full-disk encryption on the visitor-badge PC  - [ ] Host firewall rules blocking inbound connections  - [ ] MFA on the reception PC login
   - *Device control stops unknown USB media from mounting, and training addresses the curiosity the drop relies on. FDE is tempting because it is a USB-adjacent data control, but it protects the PC's own disk if stolen, not against what is plugged in. The payload runs locally, so inbound firewall rules and login MFA do not stop it. Hook: if you did not bring it, do not plug it in.*
   - @2.2.removable
7. A security team compares two inventory tools: one installs a client on every laptop, the other scans over the network with no install. Which statement about attack surface is MOST accurate?
   - **[x] The client-based tool adds software on every host that may be vulnerable**  - [ ] The agentless tool adds no attack surface, since nothing is installed  - [ ] The client-based tool adds none, since it needs no network credentials  - [ ] Both add the same attack surface, since they collect the same data
   - *A client-based tool puts another program on every endpoint, and that program can have its own flaws to patch. The agentless claim is tempting, but agentless scanning needs network access and often privileged credentials, which are an attack surface of their own. Collecting the same data says nothing about how exposure is created. Hook: every agent is another door to lock.*
   - @2.2.software
8. A plant still runs a Windows version that has had no vendor updates for three years because the CNC software needs it. What is the BEST interim approach?
   - **[x] Isolate it on its own segment with strict access rules until replaced**  - [ ] Add host antivirus and leave it on the plant network  - [ ] Apply the last vendor patches and keep it on the office VLAN  - [ ] Place it behind NAT so it has no public IP address
   - *An unsupported system cannot be fixed, so the compensating control is isolation with tightly limited access while replacement is planned. Antivirus is tempting, but it cannot close unpatched OS flaws and may not even support the old OS. The last patches leave every later flaw open, and NAT hides it from the internet but not from anything already inside. Hook: if you cannot fix it, fence it.*
   - @2.2.unsupported
9. A sales rep in a coffee shop joins a network called "Free_Cafe_WiFi" and gets a certificate warning when opening the CRM. Which vector is MOST relevant and what is the BEST protection?
   - **[x] Unsecure network; always-on VPN**  - [ ] Watering hole; DNS filtering on the laptop  - [ ] Typosquatting; registering look-alike CRM domains  - [ ] Unsupported system; updating the laptop's browser
   - *An untrusted hotspot that triggers a certificate warning suggests an on-path attacker, and an always-on VPN encrypts traffic whatever network carries it. Watering hole is tempting, but nothing suggests a trusted site was compromised. Typosquatting needs a mistyped domain, which nothing here suggests, and an up-to-date browser still shows the warning because the threat is the network. Hook: treat every public network as hostile.*
   - @2.2.network
10. At a conference, an engineer sees contact cards and files appearing on meeting-room laptops unprompted. The source is a phone a few metres away that is not on the venue Wi-Fi. Which vector should be reduced FIRST?
    - **[x] Bluetooth, by turning off discoverable mode**  - [ ] Wi-Fi, by enabling WPA3 on the room access point  - [ ] NFC, by disabling tap-to-share on the laptops  - [ ] Wired, by enabling 802.1X on the room's ports
    - *Unsolicited pushes from a nearby device are Bluetooth bluejacking, so turning off discoverability or Bluetooth stops them. NFC is tempting as another short-range channel, but it works over a few centimetres, not metres. The phone is not on the Wi-Fi, and 802.1X protects wired ports. Hook: short range, short leash.*
    - @2.2.network
11. A visitor plugs a small device into a wall port in an empty meeting room and it immediately receives an internal IP address. Which vector is this, and the BEST control?
    - **[x] Unsecure wired network; 802.1X and disabling unused ports**  - [ ] Rogue access point; wireless intrusion prevention  - [ ] Removable device; endpoint device control  - [ ] Default credentials; changing switch admin passwords
    - *Any port that hands out access is an unsecure wired network, and 802.1X makes a device authenticate before the port forwards traffic, while unused ports should be off. Rogue access point is tempting because the device could broadcast Wi-Fi later, but the entry here is the wired jack. Device control only governs what plugs into endpoints, and nobody logged into the switch. Hook: a live jack in an empty room is an open door.*
    - @2.2.network
12. An external scan shows TCP 3389 (RDP) and 23 (Telnet) forwarded through a branch router's public IP 203.0.113.40. What is the BEST action?
    - **[x] Remove public RDP and Telnet and require VPN for remote admin**  - [ ] Move RDP and Telnet to non-standard high ports  - [ ] Put an IPS in front of the router's public interface  - [ ] Enforce strong passwords and lockout on both services
    - *Open service ports widen the attack surface, so close what is not needed and gate admin access behind a VPN. Strong passwords are tempting, but Telnet still sends them in cleartext and RDP stays exposed to its own exploits. Changing ports is obscurity that scanners defeat, and an IPS only catches known patterns against services that should not be public. Hook: every open port is an unlocked window.*
    - @2.2.ports
13. A month after a contractor installs a door-entry intercom, an attacker logs into its web console with a username and password listed in the vendor's online manual. Which vector does this represent?
    - **[x] Default credentials**  - [ ] Open service port  - [ ] Supply chain  - [ ] Unsupported system
    - *Default credentials are published by vendors and tried automatically by botnets such as Mirai, so they must be changed at deployment. Open service port is tempting because the console was reachable, but the attacker got in because the login was never changed. The vendor planted nothing, and the device is still supported. Hook: the password is in the PDF.*
    - @2.2.defcreds
14. Forty client firms are hit with ransomware on the same night. All of them use the same IT services company, whose remote monitoring agent runs on their machines. Which vector is this?
    - **[x] Supply chain via a managed service provider**  - [ ] Vulnerable client-based software on each host  - [ ] Watering hole via the provider's customer portal  - [ ] Business email compromise of the provider
    - *A trusted provider with admin tooling across every client is a supply chain vector: breach one, reach many. Vulnerable client-based software is tempting because an agent was involved, but the common root is the compromised provider using its legitimate access. Nothing points to a site visited by victims or to payment fraud by email. Hook: breach one, reach many.*
    - @2.2.supply
15. Before giving a cleaning contractor badge access to the server floor, what is the BEST supply chain control?
    - **[x] Vet the supplier and limit badges to escorted, scheduled visits**  - [ ] Have the contractor sign an NDA and the AUP  - [ ] Issue badges matching the standard staff access profile  - [ ] Review the supplier's SOC 2 report once a year
    - *Suppliers are part of the attack surface, so vet them and give least privilege: escorted, time-limited access to the sensitive floor. The SOC 2 review is tempting, but it assesses the supplier's own controls and does nothing to limit what its staff can reach on your floor. An NDA and AUP are agreements, not access controls, and staff-level badges exceed what cleaners need. Hook: trust, but scope it.*
    - @2.2.supply
16. Every employee at a bank receives an email from "IT-Support" asking them to re-validate their password at a look-alike portal. What is this, and what is the BEST technical control?
    - **[x] Phishing; phishing-resistant MFA such as FIDO2**  - [ ] Phishing; mandatory 90-day password changes  - [ ] Typosquatting; registering look-alike domains  - [ ] Pretexting; awareness posters in the office
    - *A broad email credential lure is phishing, and FIDO2 or passkeys are bound to the real domain, so a captured password alone cannot be replayed and the key will not answer the fake site. Password rotation is tempting, but a stolen password works immediately, long before any 90-day change. Registering look-alikes cannot cover every possible fake domain, and posters are not a technical control. Hook: if the key will not talk to the fake site, the phish fails.*
    - @2.2.phish
17. The CFO receives an email from the real mailbox of a known supplier, which was hacked, asking to update the bank details for the next payment. Which attack is this, and the BEST process control?
    - **[x] Business email compromise; verify bank changes via a known phone number**  - [ ] Phishing; stricter spam filtering on inbound mail  - [ ] Brand impersonation; a DMARC reject policy on the domain  - [ ] Pretexting; extra awareness training for the CFO
    - *BEC uses a genuine or convincingly spoofed business mailbox to redirect money, and out-of-band verification on a known number defeats it. DMARC is tempting, but the mail really came from the supplier's own domain, so it passes authentication. Spam filters rarely flag a legitimate sender, and training alone is weaker than a mandatory verification step. Hook: money moves, so verify on a second channel.*
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
    - **[x] Typosquatting and brand impersonation**  - [ ] Watering hole and brand impersonation  - [ ] Typosquatting and pretexting  - [ ] Business email compromise and typosquatting
    - *A near-miss domain swapping 1 for l is typosquatting, and copying the company's logo and look is brand impersonation. Watering hole is tempting because a malicious site is involved, but it means compromising a real site the victims already use, not building a fake one. No invented backstory or compromised mailbox is described. Hook: wrong letter, right logo.*
    - @2.2.typo
22. Days before a product launch, fake posts claiming the device catches fire spread across social media from a network of new accounts. Which term BEST fits?
    - **[x] Disinformation**  - [ ] Misinformation  - [ ] Typosquatting  - [ ] Impersonation
    - *Disinformation is deliberately false and spread to cause harm; misinformation is false but shared without intent (people resharing in good faith). A coordinated new-account network shows intent. Hook: dis = deliberate.*
    - @2.2.misinfo
23. A warehouse still uses access points running WEP, with WPS PIN setup switched on for convenience. Why is this an attack vector?
    - **[x] Both are weak: WEP keys crack quickly and WPS PINs can be brute forced**  - [ ] WEP is weak, but WPS is safe because it only runs during setup  - [ ] WPS is weak, but WEP is safe when a 128-bit key is used  - [ ] Both are safe as long as MAC filtering is also enabled
    - *WEP can be cracked in minutes regardless of key length, and the WPS PIN can be brute forced in halves, so either one lets outsiders in. The WPS-only-at-setup idea is tempting, but if the PIN feature is left on it can be attacked at any time. MAC filtering is trivially bypassed by spoofing a seen address. Use WPA3 and turn WPS off. Hook: old wireless locks have published master keys.*
    - @2.2.network

- **Vectors: message (email, SMS, IM), image, file, voice, removable device, vulnerable software (client-based vs agentless), unsupported systems, unsecure networks (wireless, wired, Bluetooth), open ports, default credentials, supply chain (MSP, vendors, suppliers). Human: phishing, vishing, smishing, mis/disinformation, impersonation, BEC, pretexting, watering hole, brand impersonation, typosquatting.**
24. PBQ 2.2 - Social engineering triage. Match each report to the technique. ¶  1  An automated voice on a desk phone asks staff to key in their MFA code ¶  2  A message to staff mobiles about an unpaid toll links to a payment page ¶  3  A long-standing supplier's genuine mailbox asks accounts to pay into new bank details ¶  4  Staff who mistype the company domain by one character land on a fake login page ¶  5  Engineers are infected after downloading tools from the industry association site they visit weekly
    - [p] Report 1 :: A Vishing · B Smishing · C BEC · D Typosquatting · E Watering hole · F Phishing · G Pretexting = a
    - [p] Report 2 :: A Vishing · B Smishing · C BEC · D Typosquatting · E Watering hole · F Phishing · G Pretexting = b
    - [p] Report 3 :: A Vishing · B Smishing · C BEC · D Typosquatting · E Watering hole · F Phishing · G Pretexting = c
    - [p] Report 4 :: A Vishing · B Smishing · C BEC · D Typosquatting · E Watering hole · F Phishing · G Pretexting = d
    - [p] Report 5 :: A Vishing · B Smishing · C BEC · D Typosquatting · E Watering hole · F Phishing · G Pretexting = e
    - *1: a voice channel extracting a code is vishing, even when automated. 2: a lure delivered as a mobile text is smishing; phishing is the email form. 3: a genuine business mailbox redirecting payments is BEC, not generic phishing. 4: a near-miss domain catching mistypes is typosquatting. 5: compromising a site the targets already trust and visit is a watering hole. Pretexting needs an invented backstory to a person, which none of these centre on. Hook: name the channel first, then the trick.*
    - @2.2.se

## Test 7 - 2.3 Vulnerabilities I: Application, OS, Web, Hardware (21 Q)

1. An EDR alert shows a process writing code into the memory of a running svchost.exe, then that svchost connects out to 198.51.100.7. Which vulnerability class is being exploited?
   - **[x] Memory injection**  - [ ] Race condition  - [ ] SQL injection  - [ ] Resource reuse
   - *Memory injection = placing malicious code into another process's memory so it runs under that trusted process (DLL injection is a common form). It hides from tools that only look at process names. SQL injection targets databases. Hook: hide in someone else's coat.*
   - @2.3.memory
2. A C service copies a user-supplied name into a fixed 64-byte stack array with strcpy(), and long names crash it. Which developer change BEST removes the root cause?
   - **[x] Bounds-checked copies with input length validation**  - [ ] Compiling with ASLR and DEP enabled  - [ ] Placing a WAF in front of the service  - [ ] Running the service as a least-privilege account
   - *Bounds-checked copies with validated length fix the buffer overflow in the code itself, so oversized input can never spill past the array. ASLR and DEP are tempting, but they only make exploitation harder; the overflow and the crash remain. Hook: a pint glass does not hold a litre.*
   - @2.3.memory
3. A gift-card site validates that a card still has credit, then deducts it in a separate step. A script fires 20 redemptions within the same millisecond and all succeed. Which flaw is this?
   - **[x] Race condition (TOC/TOU)**  - [ ] Buffer overflow  - [ ] Cross-site scripting  - [ ] Directory traversal
   - *Time-of-check to time-of-use: state changes between the check and the action. Fix with locking or atomic transactions. Hook: two people grab the last seat at once.*
   - @2.3.race
4. An app checks a temp file's permissions, then opens it. Between the two steps an attacker swaps it for a symlink to /etc/shadow. What does this describe?
   - **[x] Race condition**  - [ ] Directory traversal  - [ ] Memory injection  - [ ] Privilege escalation
   - *A race condition (TOC/TOU): the file was valid at time-of-check but different at time-of-use; atomic check-and-open calls close the gap. Directory traversal is tempting because a sensitive path is reached, but traversal abuses ../ sequences in input, not a timing gap. Hook: what you checked is not what you used.*
   - @2.3.race
5. A popular note-taking app's auto-updater pulls a trojanised build after the vendor's build server was compromised. Which vulnerability is this?
   - **[x] Malicious update**  - [ ] Race condition  - [ ] Jailbreaking  - [ ] Default credentials
   - *Malicious update = attacker code shipped through the legitimate update channel, so it arrives signed and trusted. Defend with code-signing checks, staged rollouts and vendor monitoring. Hook: the delivery van is real, the parcel is not.*
   - @2.3.update
6. A trojanised build could be shipped, validly signed, from a vendor's compromised build server. Which control BEST limits how many of 3,000 endpoints it reaches before anyone notices?
   - **[x] Staged rollout to a pilot ring first**  - [ ] Code-signing verification on every endpoint  - [ ] Application allow listing by publisher  - [ ] Scheduled full antivirus scans
   - *A staged rollout limits the blast radius, so odd behaviour in the pilot ring stops the update before broad deployment. Signature verification is tempting, but a build signed on the vendor's own compromised server passes the check, and publisher allow listing trusts it for the same reason. Hook: canary first, flock later.*
   - @2.3.update
7. A monthly vendor bulletin describes a flaw that lets a local standard user gain SYSTEM rights on the company's standard desktop build, on every hardware model. Which category BEST fits, and the BEST response?
   - **[x] OS-based; test and deploy the vendor patch**  - [ ] Firmware; flash the BIOS update  - [ ] Misconfiguration; reapply the baseline  - [ ] Zero-day; isolate affected hosts
   - *The flaw is in the operating system code and the vendor has shipped a fix, so it is OS-based and patch management is the control. Firmware is tempting because of the low-level rights, but the bug spans every hardware model and the fix comes in the OS bulletin; a zero-day would have no fix yet. Hook: the foundation cracked, so fix the foundation.*
   - @2.3.os
8. A login form returns all users when the username is entered as admin' OR '1'='1. What is the BEST fix?
   - **[x] Parameterised queries (prepared statements)**  - [ ] A WAF rule blocking SQL keywords  - [ ] Blocklist filtering of quote characters  - [ ] A least-privilege database account
   - *Parameterised queries keep user data separate from SQL code, so input can never change the query's structure. A WAF rule is tempting but is a compensating control that encoding tricks can bypass, as can blocklists; least privilege only limits damage. Hook: never let the user write your SQL.*
   - @2.3.sqli
9. A WAF log shows requests containing UNION SELECT and -- comments against /products?id=. Which attack is being attempted?
   - **[x] SQL injection**  - [ ] Cross-site scripting  - [ ] Directory traversal  - [ ] Buffer overflow
   - *UNION SELECT and SQL comment markers are SQL injection signatures. XSS shows script tags; traversal shows ../ sequences. Hook: SQL words in a URL = SQLi.*
   - @2.3.sqli
10. A recipe site saves reviews to its database and shows them to everyone. One review carries JavaScript that posts each viewer's session token to an outside host. Which vulnerability is this?
    - **[x] Stored (persistent) cross-site scripting**  - [ ] Reflected cross-site scripting  - [ ] SQL injection  - [ ] Cross-site request forgery
    - *Stored XSS saves the script on the server so it runs for everyone who views the page. Reflected XSS bounces off a crafted link to one victim. CSRF makes a victim's browser send a request; it does not inject script. Hook: stored = booby-trapped page, reflected = booby-trapped link.*
    - @2.3.xss
11. A forum strips script tags from posts, yet attackers still get JavaScript to run in other users' browsers through event-handler attributes. What is the BEST combination of controls?
    - **[x] Context-aware output encoding plus a Content Security Policy**  - [ ] Parameterised queries plus input length limits  - [ ] HttpOnly cookies plus HSTS  - [ ] Anti-CSRF tokens plus SameSite cookies
    - *Output encoding makes the browser treat injected content as text, and CSP blocks inline or untrusted scripts, which together stop XSS. HttpOnly is tempting because it stops cookie theft, but the script still runs and can act as the user; HSTS only forces HTTPS. Hook: encode on the way out.*
    - @2.3.xss
12. A vendor advisory says a flaw on 200 laptops lets malware persist even after the drive is wiped and Windows is reinstalled. Which category, and BEST fix?
    - **[x] Firmware; apply the vendor's UEFI/BIOS update**  - [ ] Rootkit; reimage from trusted media  - [ ] OS-based; deploy the cumulative OS patch  - [ ] Legacy hardware; segment the laptops
    - *Surviving a wipe and reinstall means the flaw lives below the OS in firmware, so the vendor firmware update plus Secure Boot is the fix. Reimaging is tempting, but a reinstall never touches firmware, so the implant returns. Hook: the bug is in the basement, not the living room.*
    - @2.3.hw
13. A NAS model's manufacturer stopped publishing security fixes for it last year, but it still serves file shares. What is the MAIN risk?
    - **[x] Newly found flaws will stay unpatched**  - [ ] Its known flaws now count as zero-days  - [ ] Its configuration will drift from baseline  - [ ] Its firmware signature can no longer be verified
    - *End-of-life means no vendor patches, so every new flaw stays open for as long as the device runs. Zero-day is tempting, but a zero-day is unknown to the vendor; EOL flaws can be public and simply never fixed. Hook: still works, but nobody is fixing it.*
    - @2.3.hw
14. A plant's control system only runs on an unsupported OS release, cannot be changed without halting production, and its vendor has gone out of business. Which BEST describes it and the MOST practical mitigation?
    - **[x] Legacy; isolate it on a segmented network**  - [ ] End-of-life; apply the final vendor patch  - [ ] Zero-day; deploy a virtual patch via IPS  - [ ] Misconfiguration; reapply a hardened baseline
    - *A legacy system still in critical use with no support is mitigated by segmentation and access restriction when replacement is impossible. Applying a final vendor patch is tempting, but there is no vendor left and the platform cannot be changed without stopping production. Hook: if it is old and vital, put a fence round it.*
    - @2.3.hw
15. A pen tester bypasses a web app's login by editing a hidden form field from role=user to role=admin. Which BEST describes the root cause?
    - **[x] Authorisation decided from client-side data**  - [ ] Missing sanitisation against injection  - [ ] Session tokens with no expiry  - [ ] Direct object references by record ID
    - *The server trusted a value the browser supplied to decide authorisation, a web-based application flaw fixed by enforcing roles server side. Missing sanitisation is tempting because input was edited, but nothing was injected into an interpreter; the value was simply believed. Hook: never let the customer set their own price tag.*
    - @2.3.web
16. A team keeps finding injection and logic flaws in production web apps months after release. Which practice BEST catches these before release?
    - **[x] SAST and DAST in the CI/CD pipeline**  - [ ] A WAF in blocking mode  - [ ] Annual third-party penetration tests  - [ ] A public bug bounty programme
    - *SAST checks source code and DAST probes the running build, so flaws are caught in the pipeline before release. A WAF is tempting but only filters attacks after deployment and never fixes the code; annual tests and bounties also find bugs after release. Hook: find bugs where they are cheap, in the pipeline.*
    - @2.3.web
17. After a breach, the leaked user table shows every password stored as a fast, unsalted hash, and most were recovered in minutes with precomputed tables. Which vulnerability category is this?
    - **[x] Cryptographic**  - [ ] Misconfiguration  - [ ] Web-based  - [ ] Memory injection
    - *Weak algorithms and missing salts are cryptographic vulnerabilities; the fix is a slow salted hash such as bcrypt or Argon2. Misconfiguration is tempting, but SY0-701 lists poor crypto choices as their own category, distinct from insecure settings. Hook: the lock is old and everyone has the key.*
    - @2.3.crypto
18. A scan reports that a public web server still negotiates TLS 1.0 and export-grade ciphers for compatibility. What is the BEST action?
    - **[x] Allow only TLS 1.2+ with strong cipher suites**  - [ ] Enable HSTS on the site  - [ ] Reissue the certificate with a 4096-bit key  - [ ] Place the server behind a WAF
    - *Removing old protocol versions and weak suites closes the cryptographic flaw and the downgrade path. HSTS is tempting, but it only forces HTTPS, not which TLS version or cipher is negotiated; a bigger key does not remove weak suites either. Hook: a door that still accepts the old key is not locked.*
    - @2.3.crypto
19. A test VM spun up by a developer ships with debug mode on and a stack trace page that reveals database credentials. Which vulnerability is this?
    - **[x] Misconfiguration**  - [ ] Zero-day  - [ ] Firmware flaw  - [ ] Race condition
    - *Misconfiguration = insecure settings, not bad code: debug enabled, open storage, default accounts, verbose errors. Fixed by hardened baselines and config checks. Not a zero-day, since nothing unknown is involved. Hook: the software is fine, the settings are not.*
    - @2.3.misconfig
20. A scan finds directory listing enabled on newly built web servers every month, even though each one is fixed after the scan. What is the BEST long-term fix?
    - **[x] Hardened golden image with automated configuration enforcement**  - [ ] More frequent vulnerability scans of new servers  - [ ] A WAF rule blocking directory index pages  - [ ] A change advisory board review of each build
    - *Building the secure setting into the base image and enforcing it automatically stops the misconfiguration recurring at the source. More frequent scanning is tempting, but it only finds the problem sooner; it does not stop new servers being built wrong. Hook: fix the mould, not each brick.*
    - @2.3.misconfig
21. PBQ 2.3 - Vulnerability classifier. Match each finding to its category. ¶  1  A single quote typed in the search box returns an error listing table names ¶  2  Once a product review is saved, every visitor's browser sends its session cookie to an outside host ¶  3  Two near-simultaneous withdrawals are both approved, overdrawing the account ¶  4  An implant persists after the disk is replaced and the OS reinstalled ¶  5  The server agrees to export-grade suites when an old client asks
    - [p] Finding 1 :: A SQL injection · B XSS · C Race condition · D Firmware · E Cryptographic · F Buffer overflow · G Memory injection = a
    - [p] Finding 2 :: A SQL injection · B XSS · C Race condition · D Firmware · E Cryptographic · F Buffer overflow · G Memory injection = b
    - [p] Finding 3 :: A SQL injection · B XSS · C Race condition · D Firmware · E Cryptographic · F Buffer overflow · G Memory injection = c
    - [p] Finding 4 :: A SQL injection · B XSS · C Race condition · D Firmware · E Cryptographic · F Buffer overflow · G Memory injection = d
    - [p] Finding 5 :: A SQL injection · B XSS · C Race condition · D Firmware · E Cryptographic · F Buffer overflow · G Memory injection = e
    - *1: a quote breaking the query = SQLi. 2: stored script running for every visitor = XSS, not memory injection, which targets a local process. 3: a gap between check and debit = race condition. 4: survives disk and OS replacement = firmware. 5: weak suites accepted = cryptographic. Hook: ask where the flaw lives - query, page, timing, chip, or maths.*
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
3. An admin finds 60 test VMs on a hypervisor that no team claims, unpatched and still attached to the production network. What is the BEST response?
   - **[x] Inventory owners, then decommission or patch each VM**  - [ ] Move them to an isolated VLAN indefinitely  - [ ] Snapshot them all, then patch in place  - [ ] Install EDR agents on every VM
   - *VM sprawl is fixed by lifecycle control: find owners, remove what is unneeded and patch what stays. Isolating them is tempting, but it leaves unmanaged, unpatched assets around forever instead of resolving them. Hook: you cannot secure what you forgot you had.*
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
   - **[x] Revoke and rotate the exposed key**  - [ ] Purge the key from the repository history  - [ ] Make the repository private  - [ ] Review the key's recent API activity
   - *Revoking the key first makes every copy useless, because bots scrape public repos within minutes. Purging history is tempting, but copies already exist outside the repo; reviewing activity is the next step, not the first. Hook: a leaked key is a spent key.*
   - @2.3.cloud
7. An employee installs an app on her company phone from a file a colleague shared, rather than through the official store. Which term describes this, and the MAIN risk?
   - **[x] Side loading; the app skipped store vetting**  - [ ] Jailbreaking; the OS sandbox is removed  - [ ] Rooting; the app gains root by default  - [ ] Shadow IT; the app breaks licensing terms
   - *Installing outside the official store is side loading, so the app never went through store malware vetting. Jailbreaking is tempting because both bypass the store, but jailbreaking modifies the OS itself, which did not happen here. Hook: food from a stall with no hygiene certificate.*
   - @2.3.mob
8. A user runs a public exploit on an iPhone so it accepts themes and apps that Apple would never approve. The MDM flags the device. Why is this a security concern?
   - **[x] Jailbreaking breaks the sandbox and code-signing protections**  - [ ] Side loading voids the device's encryption keys  - [ ] Rooting exposes the IMEI to remote cloning  - [ ] Jailbreaking deletes the MDM enrolment profile
   - *Jailbreaking modifies iOS to remove sandboxing and code-signing enforcement, so apps can gain elevated access and MDM controls can no longer be trusted. Side loading is tempting, but it only means installing from outside the store; the OS itself was altered here. Hook: removing the guard rails also removes the protection.*
   - @2.3.mob
9. Company email must stay off phones whose OS restrictions have been removed or that run apps from unknown sources. Which control BEST enforces this?
   - **[x] MDM compliance checks tied to conditional access**  - [ ] A mobile VPN required for mail access  - [ ] S/MIME certificates on each phone  - [ ] NAC on the office wireless network
   - *MDM detects jailbroken or rooted devices and unknown-source apps, and conditional access blocks failing devices from mail. A VPN is tempting but only protects the connection; a compromised phone still connects. Hook: check the device before it gets the data.*
   - @2.3.mob
10. A network switch vendor ships units with a hidden debug account that a researcher later discloses. Which vulnerability category is this?
    - **[x] Supply chain - hardware provider**  - [ ] Supply chain - service provider  - [ ] Cloud-specific  - [ ] Race condition
    - *The flaw came built in from the hardware supplier. Service provider = an MSP or cloud provider; software provider = a library or app vendor. Hook: the threat was in the box.*
    - @2.3.supply
11. A remote code execution flaw is disclosed in a widely used open-source logging library bundled inside hundreds of commercial products. Which control BEST helps an organisation find where it is affected?
    - **[x] A software bill of materials (SBOM)**  - [ ] Authenticated vulnerability scanning  - [ ] Vendor right-to-audit clauses  - [ ] File integrity monitoring
    - *An SBOM lists every component in each application, so you can search for the vulnerable library directly. Vulnerability scanning is tempting, but scanners often miss libraries buried inside vendor products and depend on a signature existing. Hook: an ingredients label for software.*
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
    - **[x] Behaviour-based anomaly detection**  - [ ] Signature-based IPS with daily updates  - [ ] Weekly authenticated vulnerability scans  - [ ] Threat feeds of known IoCs
    - *Behaviour-based detection flags unusual processes, connections and privilege changes, which works even when no signature exists. A signature IPS is tempting because it updates often, but no signature exists for an unknown flaw. Hook: you cannot match a fingerprint you have never seen.*
    - @2.3.zeroday
15. A vendor announces an actively exploited zero-day in your firewall's VPN portal and publishes a temporary workaround but no patch. What should you do FIRST?
    - **[x] Apply the workaround and increase monitoring**  - [ ] Schedule the fix for the next change window  - [ ] Run a vulnerability scan to confirm exposure  - [ ] Fail over to the standby firewall
    - *Applying the vendor workaround cuts risk immediately and extra monitoring catches exploitation while you wait for a patch. Scanning first is tempting, but exploitation is already active and a scanner may lack a check for a brand new flaw; the standby unit has the same bug. Hook: tourniquet now, surgery later.*
    - @2.3.zeroday
16. A cloud tenant's serverless functions all assume one shared identity that can read and write every database in the account. What weakness is this, and the BEST fix?
    - **[x] Over-permissive IAM; a least-privilege role per function**  - [ ] Weak secrets; rotate the role's access keys  - [ ] Network exposure; add security group rules  - [ ] Resource reuse; isolate function memory
    - *One broad identity means any compromised function reaches every database, so scope a least-privilege role per function. Rotating keys is tempting, but the role keeps the same excessive permissions after rotation. Hook: one key for every door means one theft opens all.*
    - @2.3.cloudiam
17. A company's laptop images are built by an outsourced imaging firm. Which control BEST reduces supply chain risk here?
    - **[x] Verify images against known-good hashes and audit the provider**  - [ ] Require the provider to hold ISO 27001  - [ ] Run EDR on laptops after first boot  - [ ] Sign an NDA covering the imaging work
    - *Verifying each delivered image and keeping the right to audit checks what the supplier actually ships. Requiring ISO 27001 is tempting, but a certificate shows a process exists, not that each image is clean. Hook: trust, then verify.*
    - @2.3.supplyverify
18. A help-desk tech reports that a company tablet has a "system" app no one installed, and the OS reports it cannot verify the boot chain. Which is MOST likely?
    - **[x] The device has been rooted or jailbroken**  - [ ] A side-loaded app is running  - [ ] An evil twin is intercepting traffic  - [ ] An MDM profile failed to install
    - *A failed boot chain check plus an unexplained system-level app means the OS itself was modified, which is rooting or jailbreaking. Side loading is tempting because of the unknown app, but installing an app from outside the store does not break boot chain verification. Hook: if the device cannot trust its own startup, neither should you.*
    - @2.3.rooted
19. PBQ 2.3 - Cloud and virtual findings. Match each finding to its vulnerability. ¶  1  Code in one tenant's guest takes control of the host that runs every guest ¶  2  A freshly provisioned instance can read fragments of another customer's records ¶  3  Staff install a productivity tool from a file emailed by a coworker ¶  4  Attackers exploit a flaw the maker had no record of ¶  5  Customer staff data leaks after the outsourced payroll platform is breached
    - [p] Finding 1 :: A VM escape · B Resource reuse · C Side loading · D Zero-day · E Supply chain (service provider) · F Supply chain (hardware provider) · G Jailbreaking = a
    - [p] Finding 2 :: A VM escape · B Resource reuse · C Side loading · D Zero-day · E Supply chain (service provider) · F Supply chain (hardware provider) · G Jailbreaking = b
    - [p] Finding 3 :: A VM escape · B Resource reuse · C Side loading · D Zero-day · E Supply chain (service provider) · F Supply chain (hardware provider) · G Jailbreaking = c
    - [p] Finding 4 :: A VM escape · B Resource reuse · C Side loading · D Zero-day · E Supply chain (service provider) · F Supply chain (hardware provider) · G Jailbreaking = d
    - [p] Finding 5 :: A VM escape · B Resource reuse · C Side loading · D Zero-day · E Supply chain (service provider) · F Supply chain (hardware provider) · G Jailbreaking = e
    - *1: guest reaching the host = VM escape. 2: uncleared reassigned memory or disk = resource reuse, since nothing broke out. 3: install from outside the store = side loading, not jailbreaking, as the OS is untouched. 4: unknown to the maker = zero-day. 5: a third party running a service = service provider supply chain. Hook: escape breaks out, reuse inherits.*
    - @2.3.misc

- **2.3 part II: virtualization (VM escape, resource reuse), cloud-specific, supply chain (service, hardware, software provider), mobile (side loading, jailbreaking), zero-day.**

## Test 9 - 2.4 Malware, Physical + Network Attacks (28 Q)

1. A hospital's file shares are encrypted overnight and a note demands payment for the key. What is the BEST preparation to recover WITHOUT paying?
   - **[x] Tested offline or immutable backups**  - [ ] Volume shadow copies on each file server  - [ ] RAID 6 on the file-share storage  - [ ] Real-time replication to a second site
   - *Offline or immutable backups that have been restore-tested are out of the attacker's reach and proven to work. Replication is tempting, but it copies the encrypted files to the second site within seconds; ransomware also routinely deletes shadow copies, and RAID is availability, not backup. Hook: a backup you have never restored is a hope, not a backup.*
   - @2.4.ransom
2. A "free video downloader" really does download videos, but it also quietly lets an outsider control the PC. What is this?
   - **[x] Trojan (with a remote access capability)**  - [ ] Worm  - [ ] Logic bomb  - [ ] Bloatware
   - *Trojan = malware disguised as wanted software; the user installs it willingly. Adding remote control makes it a RAT. A worm spreads itself without user action. Hook: the wooden horse looked like a gift.*
   - @2.4.trojan
3. Malware spreads from one unpatched server to 400 others in an hour over SMB with no user clicking anything. What type is it, and the BEST containment?
   - **[x] Worm; segment and block SMB while patching**  - [ ] Virus; quarantine infected attachments  - [ ] Trojan; remove the installer and reset passwords  - [ ] Rootkit; reimage the first server only
   - *Self-propagation over the network with no user action is a worm, contained by segmentation and blocking the exploited service while patching. Virus is tempting, but a virus needs a host file and someone to open it. Hook: worms crawl on their own.*
   - @2.4.worm
4. A virus differs from a worm MAINLY because a virus:
   - **[x] Needs a host file and user action to spread**  - [ ] Hides itself from the OS in the kernel  - [ ] Waits for a trigger condition before acting  - [ ] Disguises itself as legitimate software
   - *A virus attaches to a program or document and spreads only when that host is run or shared, whereas a worm spreads by itself. Disguise is tempting, but that defines a trojan; hiding is a rootkit and waiting for a trigger is a logic bomb. Hook: virus hitchhikes, worm walks.*
   - @2.4.worm
5. A new laptop from a retailer arrives with trial antivirus, three games and a "PC optimiser" the user never asked for. What is this, and what should IT do?
   - **[x] Bloatware; reimage with a clean corporate build**  - [ ] Spyware; block its telemetry at the proxy  - [ ] Trojan; isolate the laptop for forensics  - [ ] Adware; install a browser ad blocker
   - *Unwanted software preinstalled by the seller is bloatware, removed by deploying the standard corporate image. Trojan is tempting because the user did not ask for it, but a trojan is malware disguised as something the user chose to install. Hook: junk that came in the box.*
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
11. During a walk-through, a guard finds a small reader with a battery pack hidden behind the panel of the lobby's proximity badge reader. Which attack does it MOST likely support?
    - **[x] RFID cloning**  - [ ] Card skimming  - [ ] Bluesnarfing  - [ ] Tailgating
    - *The hidden reader captures proximity badge IDs so duplicates can be made, which is RFID cloning; encrypted cards and badge plus PIN mitigate. Skimming is tempting, but it targets payment cards, not building access badges. Hook: copy the key without touching the owner.*
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
17. Laptops in the car park join a network broadcasting the office SSID, but it is served from a device IT does not own. What is this, and the BEST mitigation?
    - **[x] Evil twin; 802.1X with server certificate validation**  - [ ] Rogue AP; enable MAC filtering  - [ ] Deauthentication; enable 802.11w  - [ ] Bluejacking; disable Bluetooth
    - *A fake AP copying the corporate SSID is an evil twin, and 802.1X clients that validate the server certificate refuse to authenticate to it. Rogue AP is tempting, but that term covers any unauthorised AP, and MAC filtering stops clients joining, not clients trusting a fake. Hook: same name, different face.*
    - @2.4.wireless
18. Every laptop on a floor drops off Wi-Fi at once and repeatedly reconnects, and a capture shows a flood of management frames spoofing the AP's MAC address. What is happening?
    - **[x] A deauthentication attack**  - [ ] RF jamming  - [ ] An evil twin  - [ ] ARP poisoning
    - *Forged management frames that knock clients off are a deauthentication attack; 802.11w protected management frames mitigate. Jamming is tempting because of the mass drop-off, but jamming is raw RF noise with no frames to capture. Hook: someone keeps hanging up your call.*
    - @2.4.wireless
19. An attacker on the same LAN sends unsolicited replies mapping the gateway's IP to his own MAC, so hosts send their outbound traffic through his laptop. What type of attack is this?
    - **[x] On-path**  - [ ] DNS poisoning  - [ ] MAC flooding  - [ ] Evil twin
    - *Poisoning ARP tables places the attacker between hosts and the gateway, which is an on-path attack; dynamic ARP inspection mitigates. DNS poisoning is tempting because a mapping is forged, but DNS maps names to IPs, while here IPs were mapped to MACs. Hook: the postman reads your letters.*
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
    - **[x] Isolate affected hosts, then collect the script and IoCs**  - [ ] Delete the task on every host via GPO  - [ ] Decode the PowerShell to scope the attack  - [ ] Reimage all affected workstations
    - *Containment comes first to stop spread, then evidence is preserved for analysis. Decoding the script is tempting, but analysis follows containment, and deleting or reimaging destroys evidence of fileless malware. Hook: stop the bleeding, then study the wound.*
    - @2.4.mal
23. A user reports a pop-up saying "Your files are locked - send 0.5 BTC" but their files open normally. Which is the MOST likely situation?
    - **[x] Ransomware bluff; files not yet encrypted**  - [ ] Ransomware; encryption already complete  - [ ] Spyware staging data for exfiltration  - [ ] Logic bomb that has already triggered
    - *Files opening normally means nothing is encrypted, so this is a bluff that still needs investigating for real compromise. Completed encryption is tempting because of the ransom note, but encrypted files would not open. Hook: test the lock before paying for the key.*
    - @2.4.ransom
24. Infected hosts keep resolving known command-and-control domains, and some users receive forged records for a partner's site. Which pair of controls MOST directly addresses both?
    - **[x] A DNS sinkhole and DNSSEC validation**  - [ ] DNS over HTTPS and HSTS  - [ ] A web proxy and TLS inspection  - [ ] An IPS and egress port filtering
    - *A sinkhole answers lookups for known bad domains with a safe address, breaking callbacks, and DNSSEC rejects records whose signatures do not validate. DNS over HTTPS is tempting, but it only encrypts the query channel; it neither validates records nor blocks bad domains. Hook: control the phone book.*
    - @2.4.dns
25. Wireless clients in one wing lose connectivity whenever a van parks outside. A spectrum analyser shows strong noise across the 2.4 GHz band and no management frames from the source. Which attack is this?
    - **[x] Wireless jamming, a denial of service**  - [ ] Deauthentication attack  - [ ] Evil twin  - [ ] Bluesnarfing
    - *Jamming floods the radio band with noise so nothing can be heard: pure DoS at the RF level. Deauthentication sends forged 802.11 frames instead, and an evil twin offers a fake AP. Find the source with physical searches and spectrum analysis. Hook: shouting over everyone, not tricking anyone.*
    - @2.4.wireless
26. Visitors to a retailer's site reach an attacker's server. The DNS records were changed through the company's registrar account after its password was phished, and no resolver caches were touched. Which attack is this?
    - **[x] Domain hijacking**  - [ ] DNS poisoning  - [ ] Typosquatting  - [ ] Evil twin
    - *Domain hijacking = taking control of the domain registration itself, then pointing its records anywhere. DNS poisoning corrupts a resolver's cache instead; typosquatting uses a look-alike name. Defend with registrar MFA and registry lock. Hook: they stole the deed, not the street sign.*
    - @2.4.dns

- **Malware: ransomware, trojan, worm, spyware, bloatware, virus, keylogger, logic bomb, rootkit. Physical: brute force, RFID cloning, environmental. Network: DDoS (amplified, reflected), DNS, wireless, on-path, credential replay, malicious code.**
27. PBQ 2.4 - Malware identification. Match each behaviour to the malware type. ¶  1  Infection reaches 300 servers over file sharing in an hour though nobody opened anything ¶  2  Tools on the live system report nothing, but an offline scan finds unknown drivers ¶  3  Payroll records vanish the day an admin's account is disabled ¶  4  A free PDF converter works as advertised but opens a back channel to an outsider ¶  5  A small inline adapter is found on a manager's keyboard cable
    - [p] Behaviour 1 :: A Worm · B Rootkit · C Logic bomb · D Trojan · E Keylogger · F Virus · G Ransomware = a
    - [p] Behaviour 2 :: A Worm · B Rootkit · C Logic bomb · D Trojan · E Keylogger · F Virus · G Ransomware = b
    - [p] Behaviour 3 :: A Worm · B Rootkit · C Logic bomb · D Trojan · E Keylogger · F Virus · G Ransomware = c
    - [p] Behaviour 4 :: A Worm · B Rootkit · C Logic bomb · D Trojan · E Keylogger · F Virus · G Ransomware = d
    - [p] Behaviour 5 :: A Worm · B Rootkit · C Logic bomb · D Trojan · E Keylogger · F Virus · G Ransomware = e
    - *1: spreads with no user action = worm, not virus, which needs a host file opened. 2: invisible to the live OS = rootkit. 3: waits for a condition = logic bomb. 4: disguised as wanted software = trojan. 5: inline hardware capturing keys = keylogger. Hook: spread, hide, wait, disguise, record.*
    - @2.4.mal

28. PBQ 2.4 - Network attack identification. Match each capture to the attack. ¶  1  A web server's bandwidth is saturated by tens of thousands of residential IP addresses ¶  2  Users typing the correct bank URL reach a fake site, though the registrar records are unchanged ¶  3  Laptops join an AP broadcasting the office network name from a device IT does not own ¶  4  Hosts' tables show the gateway's address now resolving to a workstation's MAC ¶  5  An NTLM hash that was never cracked is used to log on to a file server
    - [p] Capture 1 :: A DDoS · B DNS poisoning · C Evil twin · D On-path · E Credential replay · F Domain hijacking · G Jamming = a
    - [p] Capture 2 :: A DDoS · B DNS poisoning · C Evil twin · D On-path · E Credential replay · F Domain hijacking · G Jamming = b
    - [p] Capture 3 :: A DDoS · B DNS poisoning · C Evil twin · D On-path · E Credential replay · F Domain hijacking · G Jamming = c
    - [p] Capture 4 :: A DDoS · B DNS poisoning · C Evil twin · D On-path · E Credential replay · F Domain hijacking · G Jamming = d
    - [p] Capture 5 :: A DDoS · B DNS poisoning · C Evil twin · D On-path · E Credential replay · F Domain hijacking · G Jamming = e
    - *1: many sources = DDoS. 2: right name, wrong IP with registrar untouched = DNS poisoning, not domain hijacking. 3: copied SSID = evil twin. 4: ARP tricks = on-path. 5: reused hash = credential replay. Hook: volume, map, mask, middle, reuse.*
    - @2.4.net

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
   - **[x] Rolling codes so each message is valid only once**  - [ ] Stronger encryption of the unlock message  - [ ] Digitally signing each unlock message  - [ ] A longer key stored in the fob
   - *Rolling codes or nonces make every captured message worthless after one use, which defeats replay. Encryption and signing are tempting, but a recorded encrypted or signed message is still valid when resent unchanged. Hook: yesterday's ticket should not get you in today.*
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
    - **[x] Brute force; bcrypt's work factor slows each guess**  - [ ] Brute force; the salt makes guessing impossible  - [ ] Rainbow table; the salt blocks precomputed lookups  - [ ] Dictionary; bcrypt locks out after failures
    - *Trying every combination offline is brute force, and bcrypt's tunable work factor makes each guess expensive. The salt is tempting, but salts defeat precomputed tables, not a live brute force against one hash; offline attacks face no lockout. Hook: make every guess cost a coin.*
    - @2.4.pw
12. A user's account logs in from London at 09:00 and from Singapore at 09:20 the same morning. Which indicator is this?
    - **[x] Impossible travel**  - [ ] Account lockout  - [ ] Resource consumption  - [ ] Out-of-cycle logging
    - *No one flies that fast, so one of the logins is probably an attacker with stolen credentials (or a VPN, which needs checking). Hook: physics says no.*
    - @2.4.ioc
13. A SaaS admin sees one account with live sessions in three browsers in three countries at the same moment. Which indicator is this, and what is the BEST first action?
    - **[x] Concurrent session usage; revoke all sessions and reset credentials**  - [ ] Concurrent session usage; enforce MFA at next login  - [ ] Impossible travel; geo-block the newest country  - [ ] Account lockout; unlock and notify the user
    - *Simultaneous sessions from several places is concurrent session usage, and revoking every session plus resetting credentials evicts the attacker now. Enforcing MFA is tempting, but stolen session tokens stay valid until revoked, so MFA at next login does not remove the intruder. Hook: one person, three places = more than one person.*
    - @2.4.ioc
14. A server's security log has no entries between 02:00 and 03:00, and the log service shows a restart at 03:01 by an account no one recognises. Which indicator does this MOST suggest?
    - **[x] Missing logs**  - [ ] Out-of-cycle logging  - [ ] Resource inaccessibility  - [ ] Account lockout
    - *A gap followed by an unexplained service restart suggests someone cleared or stopped logging to hide activity, the missing logs indicator; forward logs to a SIEM in real time. Out-of-cycle logging is tempting because the restart is unusual, but that indicator means unexpected extra log activity, the opposite of a gap. Hook: the silence is the clue.*
    - @2.4.ioc2
15. At 03:00 on a Sunday a file server logs a burst of thousands of audit entries, far outside any backup or scheduled job. Which indicator is this?
    - **[x] Out-of-cycle logging**  - [ ] Missing logs  - [ ] Published or documented  - [ ] Concurrent session usage
    - *Out-of-cycle logging = log activity at unexpected times or volumes, unlike normal patterns. Missing logs is the opposite. Hook: noise when it should be quiet.*
    - @2.4.ioc2
16. A database server's CPU sits at 100% and outbound traffic triples overnight, while the users' app becomes unreachable. Which TWO indicators are shown?
    - **[x] Resource consumption and resource inaccessibility**  - [ ] Account lockout and impossible travel  - [ ] Blocked content and published/documented  - [ ] Missing logs and concurrent sessions
    - *High CPU, disk or bandwidth use suggests cryptomining, exfiltration or DDoS; services or files becoming unavailable (including ransomware) are resource inaccessibility. Hook: busy and broken at the same time.*
    - @2.4.ioc2
17. After a breach that spread from a guest Wi-Fi laptop to the HR database, what mitigation would MOST limit similar lateral movement?
    - **[x] Segmentation with firewall rules between zones**  - [ ] WPA3-Enterprise on the guest Wi-Fi  - [ ] EDR on the HR database servers  - [ ] MFA for HR application logins
    - *Segmentation with enforced rules between guest, user and server zones stops a compromise in one zone reaching another. WPA3-Enterprise is tempting, but it secures who joins the Wi-Fi, not where an infected guest device can go afterwards. Hook: bulkheads in a ship stop one leak sinking it.*
    - @2.5.mit
18. A kiosk PC in a hotel lobby only ever needs a browser, yet staff keep finding games installed. What is the BEST mitigation?
    - **[x] Application allow list permitting only the approved browser**  - [ ] A block list of known game names  - [ ] Weekly manual cleanup  - [ ] Full-disk encryption on the kiosk
    - *An allow list denies everything not explicitly approved, which suits single-purpose systems. Block lists always lag behind. FDE protects data at rest, not what runs. Hook: guest list at the door, not a list of banned people.*
    - @2.5.allowlist
19. EDR flags a laptop connecting to known ransomware infrastructure. What is the BEST immediate mitigation?
    - **[x] Isolate the host via EDR, keeping it powered on**  - [ ] Power it off to stop any encryption  - [ ] Reimage it from the golden image  - [ ] Block the domain at the perimeter firewall
    - *Network isolation contains spread while keeping memory evidence for forensics. Powering off is tempting to halt encryption, but it destroys volatile evidence; blocking one domain at the perimeter leaves the host free to spread internally. Hook: quarantine the patient, do not cremate them.*
    - @2.5.isolate
20. A new marketing intern is given the same file share rights as the marketing director "to save time". Which principle is violated, and what control fixes it?
    - **[x] Least privilege; role-based permissions scoped to the job**  - [ ] Separation of duties; split approval steps  - [ ] Job rotation; rotate share ownership  - [ ] Zero trust; continuous device posture checks
    - *Least privilege means only the access the job needs, implemented with role-scoped permissions and ACLs. Separation of duties is tempting, but it splits a sensitive task between people; it does not trim one person's excess rights. Hook: give the intern a key to their own office, not the master key.*
    - @2.5.leastpriv
21. An audit finds an old FTP server still powered on in a rack, with live DNS and a public IP, though its service moved to SFTP last year. What is the BEST action?
    - **[x] Decommission it and update the asset inventory**  - [ ] Patch it and keep it as a fallback  - [ ] Move it behind the firewall on a private IP  - [ ] Disable FTP but leave the host running
    - *A system with no remaining purpose should be decommissioned: wiped, removed from DNS and IP space, and recorded in inventory. Patching and keeping it is tempting, but an unneeded host still needs patching forever and is likely to be forgotten again. Hook: switched on and forgotten is a breach.*
    - @2.5.mit
22. A hardening checklist for a new internet-facing Linux web server is being written. Which set BEST reflects standard hardening?
    - **[x] Change defaults, disable unused services, remove unneeded packages, add HIPS**  - [ ] Keep vendor default accounts, enable a host firewall, add HIPS, encrypt the disk  - [ ] Install the full package set, disable unused ports, add EDR, enable logging  - [ ] Allow root SSH with keys, keep all services running, add HIDS, patch monthly
    - *Hardening shrinks the attack surface: no defaults, fewer services and packages, plus host protection. The full-package option is tempting because it closes ports and adds EDR, but every extra package is more code to exploit and patch. Hook: lock it, strip it, watch it.*
    - @2.5.hard
23. A laptop's EDR is healthy, but on hotel Wi-Fi another guest connects straight to its file-sharing and remote desktop services. Which endpoint hardening control would BEST stop this?
    - **[x] A host-based firewall**  - [ ] A host-based IDS  - [ ] Full-disk encryption  - [ ] An application allow list
    - *A host-based firewall filters traffic at the endpoint and denies unsolicited connections even on untrusted networks. A HIDS is tempting, but it detects and alerts rather than blocking the connection; FDE protects data at rest only. Hook: carry your own wall.*
    - @2.5.hostfw
24. Forensics shows a trusted Windows service process was forced by another process to load a malicious library into its memory at runtime, so the attacker's code ran under the service's name. Which attack is this?
    - **[x] DLL injection**  - [ ] Privilege escalation  - [ ] Buffer overflow  - [ ] Trojan
    - *Forcing a running process to load a malicious library is DLL injection, a form of memory injection that hides behind a trusted process. A trojan is tempting because malicious code hides in something trusted, but a trojan is software the user installs believing it is legitimate. Hook: a stowaway library in a trusted ship.*
    - @2.4.inject

- **App attacks: injection, buffer overflow, replay, privilege escalation, forgery (CSRF, SSRF), directory traversal. Crypto: downgrade, collision, birthday. Password: spraying, brute force. IoCs: account lockout, concurrent sessions, blocked content, impossible travel, resource consumption, resource inaccessibility, out-of-cycle logging, published/documented, missing logs. Mitigation: segmentation, ACLs/permissions, allow list, isolation, patching, encryption, monitoring, least privilege, configuration enforcement, decommissioning, hardening.**
25. PBQ 2.4 - Indicators of compromise. Match each observation to the indicator. ¶  1  Dozens of staff are refused sign-in on Monday even with the right password ¶  2  The proxy keeps denying one host's requests to a known C2 domain ¶  3  Your customer list is offered for sale on a dark-web forum ¶  4  One user signs in from London, then Sydney 30 minutes later ¶  5  The security log has a one-hour hole right after an admin sign-in
    - [p] Observation 1 :: A Account lockout · B Blocked content · C Published/documented · D Impossible travel · E Missing logs · F Out-of-cycle logging · G Concurrent session usage = a
    - [p] Observation 2 :: A Account lockout · B Blocked content · C Published/documented · D Impossible travel · E Missing logs · F Out-of-cycle logging · G Concurrent session usage = b
    - [p] Observation 3 :: A Account lockout · B Blocked content · C Published/documented · D Impossible travel · E Missing logs · F Out-of-cycle logging · G Concurrent session usage = c
    - [p] Observation 4 :: A Account lockout · B Blocked content · C Published/documented · D Impossible travel · E Missing logs · F Out-of-cycle logging · G Concurrent session usage = d
    - [p] Observation 5 :: A Account lockout · B Blocked content · C Published/documented · D Impossible travel · E Missing logs · F Out-of-cycle logging · G Concurrent session usage = e
    - *1: mass refusals with right passwords = account lockout, often from guessing. 2: repeated denials to a bad domain = blocked content. 3: your data seen publicly = published/documented. 4: impossible geography = impossible travel, not concurrent sessions, as the logins are sequential. 5: a gap = missing logs. Hook: each one is a symptom, not proof, so investigate.*
    - @2.4.ioc

26. PBQ 2.5 - Pick the BEST mitigation for each finding. ¶  1  Web servers run a version named in a vendor advisory that has a fixed release out ¶  2  A stolen laptop's customer records were readable by anyone who removed the drive ¶  3  An admin account logged in at 03:00 for a week before anyone noticed ¶  4  Servers built to the baseline are found weeks later with settings changed by hand ¶  5  Switches accept cleartext remote management sessions on port 23
    - [p] Finding 1 :: A Patching · B Encryption · C Monitoring · D Configuration enforcement · E Disabling ports/protocols · F Segmentation · G Decommissioning = a
    - [p] Finding 2 :: A Patching · B Encryption · C Monitoring · D Configuration enforcement · E Disabling ports/protocols · F Segmentation · G Decommissioning = b
    - [p] Finding 3 :: A Patching · B Encryption · C Monitoring · D Configuration enforcement · E Disabling ports/protocols · F Segmentation · G Decommissioning = c
    - [p] Finding 4 :: A Patching · B Encryption · C Monitoring · D Configuration enforcement · E Disabling ports/protocols · F Segmentation · G Decommissioning = d
    - [p] Finding 5 :: A Patching · B Encryption · C Monitoring · D Configuration enforcement · E Disabling ports/protocols · F Segmentation · G Decommissioning = e
    - *1: a fixed release exists = patching. 2: readable data at rest = encryption (FDE). 3: unnoticed activity = monitoring. 4: drift = configuration enforcement. 5: port 23 is Telnet, cleartext, so disable it and use SSH; segmentation would only limit who reaches it. Hook: fix, scramble, watch, enforce, close.*
    - @2.5.hard

## Test 11 - 3.1 Architecture Models I: Cloud + Network Infrastructure (20 Q)

1. A startup moves its customer portal to an IaaS provider. After a breach, investigators find the guest OS on the VMs had not been patched for a year. Who was responsible for that patching?
   - **[x] The customer**  - [ ] The cloud provider  - [ ] Both parties equally  - [ ] The hypervisor vendor
   - *In IaaS the customer owns everything from the guest OS upward, including patching, while the provider secures facilities, hardware and hypervisor. The provider is tempting because it runs the platform, but its duty stops at the hypervisor. Hook: IaaS = you get the empty flat, you buy the locks.*
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
   - **[x] A compromised service can be contained without stopping the rest**  - [ ] Fewer network connections between components need monitoring  - [ ] Service-to-service calls stay in-process, off the network  - [ ] One shared database simplifies access control for all services
   - *Microservices isolate failures, so one compromised or broken service can be contained and patched alone. Fewer connections is tempting because each service is smaller, but splitting the app creates more network paths, not fewer. Hook: watertight compartments, more doors to guard.*
   - @3.1.micro
9. A water utility keeps the control network for its pumps on switches with no cable or wireless link to the office LAN. Updates come in on a scanned USB drive. What is this design called?
   - **[x] Air-gapped (physical isolation)**  - [ ] VLAN segmentation  - [ ] Screened subnet  - [ ] Software-defined networking
   - *Air gap = no physical connection at all. Data crosses by removable media, which is why removable media is the main risk (Stuxnet). VLANs share hardware, so logical. A screened subnet is a DMZ. SDN is about programmable control.*
   - @3.1.airgap
10. A hospital wants guest Wi-Fi users, medical devices and staff laptops on the same physical switches but unable to reach each other except through a firewall. What is the BEST fit?
    - **[x] VLANs per group, routed through the firewall**  - [ ] Air-gapped switches per group  - [ ] A screened subnet for medical devices  - [ ] Port security with MAC filtering
    - *VLANs logically split shared switches into separate segments, and routing between them through the firewall controls what crosses. An air gap is tempting for strong isolation, but it needs separate hardware and allows no firewall path at all. Hook: one building, locked internal doors.*
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
15. A pen tester running code inside a tenant VM gains execution on the host that schedules every VM, then reads other tenants' disks. What is this attack?
    - **[x] VM escape**  - [ ] Resource reuse  - [ ] Privilege escalation  - [ ] VM sprawl
    - *Moving from a guest to the hypervisor and on to other guests is VM escape, the worst virtualization failure. Resource reuse is tempting because other tenants' data is read, but reuse leaks leftovers through reallocated memory or disk without breaking out. Hook: the prisoner walks into the warden's office.*
    - @3.1.virt
16. Developers can create VMs from a self-service portal with no owner field and no expiry date, and the hypervisor now hosts hundreds of idle, unpatched VMs. What is the BEST control?
    - **[x] A VM lifecycle process tied to the asset inventory**  - [ ] Monthly vulnerability scans of the hypervisor  - [ ] Moving the VMs onto a separate VLAN  - [ ] Converting the VMs into containers
    - *VM sprawl is fixed with lifecycle management: owners, inventory and expiry so unused VMs are removed. Moving them to a VLAN is tempting, but it hides the problem while the unowned VMs stay unpatched. Hook: you cannot secure what you forgot you had.*
    - @3.1.virt
17. An architect says moving a workload to a public cloud "removes our responsibility for the data." What is the BEST response?
    - **[x] The organisation stays accountable for its data in every cloud model**  - [ ] Correct, once a SaaS contract is signed  - [ ] Correct, if the provider holds ISO 27001  - [ ] Correct, only for data encrypted at rest
    - *Responsibility for tasks can shift; accountability for the data never does. Certifications and contracts help but do not transfer ownership of the data or of breach duties.*
    - @3.1.hybrid
18. A team running a hybrid environment wants one set of user identities that works on-premises and in the cloud. Which approach BEST supports this?
    - **[x] Federation or directory sync from one identity source**  - [ ] Separate local accounts in each environment  - [ ] Cloud-only accounts protected with MFA  - [ ] A PAM vault holding every user's credentials
    - *One authoritative identity source, synced or federated, means joiners and leavers are handled once in both environments. Cloud-only accounts with MFA are tempting because they are secure, but on-premises systems would still need separate identities. Hook: one passport, two countries.*
    - @3.1.hybrid
19. A security lead must explain why the company's new microservices platform needs more API security work than the old monolith. Which reason is MOST accurate?
    - **[x] Internal calls become network APIs, adding endpoints**  - [ ] Each service requires its own public IP address  - [ ] Services cannot share one certificate authority  - [ ] Service meshes turn off authentication by default
    - *Splitting a monolith turns in-process function calls into network API calls, so there are more endpoints to authenticate and protect. The public IP option is tempting, but most services stay internal behind a gateway; it is the internal calls that multiply. Hook: every wall you add is another door.*
    - @3.1.micro
20. PBQ 3.1 - Pick the model. A logistics firm is placing workloads. Choose the BEST architecture for each. ¶  1  Logic that runs for a few seconds each time a parcel scanner fires, with no host to manage ¶  2  Tracking app that must behave identically on a laptop, an on-premises host or the cloud ¶  3  Twelve regional networks built from the same reviewed definition files ¶  4  Payroll where the firm manages only its users and data ¶  5  Turbine controllers whose updates arrive only on a scanned USB drive
    - [p] Workload 1 :: A Serverless · B Containerization · C Infrastructure as code · D SaaS · E Air-gapped · F PaaS · G VLAN segmentation = a
    - [p] Workload 2 :: A Serverless · B Containerization · C Infrastructure as code · D SaaS · E Air-gapped · F PaaS · G VLAN segmentation = b
    - [p] Workload 3 :: A Serverless · B Containerization · C Infrastructure as code · D SaaS · E Air-gapped · F PaaS · G VLAN segmentation = c
    - [p] Workload 4 :: A Serverless · B Containerization · C Infrastructure as code · D SaaS · E Air-gapped · F PaaS · G VLAN segmentation = d
    - [p] Workload 5 :: A Serverless · B Containerization · C Infrastructure as code · D SaaS · E Air-gapped · F PaaS · G VLAN segmentation = e
    - *1: event-driven with no host = serverless. 2: portable app plus dependencies = container. 3: networks from reviewed files = IaC. 4: only users and data left to you = SaaS, not PaaS, where you still own the code. 5: data only by removable media = air gap, not VLANs, which share hardware. Hook: event, package, recipe, rental, island.*
    - @3.1.models

## Test 12 - 3.1 Architecture Models II: Embedded, ICS/SCADA, IoT, Considerations (21 Q)

1. A smart-building firm deploys 4,000 networked thermostats that ship with a shared factory login and never receive firmware updates. What is the BEST first mitigation?
   - **[x] Segment them on a dedicated VLAN and change the factory credentials**  - [ ] Install a host-based IPS agent on each thermostat  - [ ] Enable full-disk encryption on each thermostat  - [ ] Route all thermostat traffic through a forward proxy
   - *Segmenting the devices and removing default credentials fixes the actual weakness and limits the blast radius on devices that cannot be patched. A host-based IPS agent is tempting, but constrained IoT devices cannot run agents. FDE protects stored data, not the login, and a forward proxy only filters outbound web traffic. Hook: fence it and change the lock.*
   - @3.1.iot
2. A security review of consumer smart devices lists several concerns. Which one MOST often makes these devices a security problem?
   - **[x] Weak default settings and short vendor support lifecycles**  - [ ] Use of lightweight cryptographic algorithms  - [ ] Deterministic real-time task scheduling  - [ ] Dependence on serverless cloud back ends
   - *Consumer IoT is built for price and features, so default credentials and little ongoing patching are the recurring weakness. Lightweight cryptography is tempting, but it is a deliberate fit for constrained hardware, not the main problem. Real-time scheduling and serverless back ends are design choices, not the typical flaw. Hook: smart device, dumb defaults.*
   - @3.1.iot
3. A gas pipeline operator monitors valves across 900 km from a central control room using remote terminal units. Which system type is this?
   - **[x] SCADA**  - [ ] RTOS  - [ ] SDN  - [ ] Serverless
   - *SCADA (Supervisory Control and Data Acquisition) supervises geographically spread industrial sites. It is a type of ICS. RTOS is the OS inside a time-critical device. SDN and serverless are IT models.*
   - @3.1.ics
4. A factory's decades-old PLCs speak only unauthenticated legacy protocols and cannot be replaced this year. What is the BEST protection?
   - **[x] Isolate the ICS network and allow access only via a jump server**  - [ ] Install an EDR agent on each PLC controller  - [ ] Run weekly active vulnerability scans on the PLCs  - [ ] Place the PLCs behind a reverse proxy server
   - *Segmentation with a single controlled entry point protects devices that cannot authenticate or be patched, while keeping availability first. EDR is tempting, but PLCs cannot run host agents. Active scans can crash fragile controllers, and a reverse proxy is for publishing web servers. Hook: if you cannot fix the box, fence the box.*
   - @3.1.ics
5. In an industrial control environment, which goal usually takes PRIORITY over confidentiality?
   - **[x] Availability of the controlled process**  - [ ] Non-repudiation of operator logins  - [ ] Data sovereignty of sensor logs  - [ ] Obfuscation of the control logic
   - *ICS downtime can cause blackouts or physical harm, so availability (with safety) leads, and patching and scanning are planned around it. Non-repudiation is tempting as an accountability goal, but it does not drive ICS design. Sovereignty and obfuscation are confidentiality-flavoured. Hook: in a plant, the lights stay on first.*
   - @3.1.ics
6. An anti-lock braking unit must pulse the brakes on a guaranteed, fixed schedule no matter what else the car is doing. What does it MOST likely run on?
   - **[x] A real-time operating system (RTOS)**  - [ ] A general-purpose desktop OS  - [ ] A container on a shared host  - [ ] A serverless function
   - *RTOS guarantees deterministic timing. Security work is hard because they are minimal and long-lived; any delay from security tooling is unacceptable. Desktop OS and cloud models cannot guarantee millisecond response.*
   - @3.1.rtos
7. Why is it often hard to add security tools to an RTOS-based medical pump?
   - **[x] Extra processing can break the strict timing the device relies on**  - [ ] Most RTOS devices lack a network stack for tools to reach  - [ ] RTOS firmware is obfuscated, so scanners cannot parse it  - [ ] An RTOS fails open, so any added agent is bypassed
   - *An RTOS must meet hard deadlines, and agents or heavy crypto add processing that can make the pump miss them. The no-network-stack claim is tempting, but many RTOS devices are networked, which is why they need protecting. Obfuscation and fail-open are unrelated to the difficulty. Hook: on an RTOS, timing is the product.*
   - @3.1.rtos
8. A printer's firmware is fixed in a chip and the vendor ships updates only rarely. Which term BEST describes this kind of device?
   - **[x] Embedded system**  - [ ] Microservice  - [ ] Jump server  - [ ] Thin client
   - *Embedded systems are purpose-built computers inside a product (printers, cameras, cars). Hard to patch, often long-lived. Hook: computer hidden in a thing. The others are architectures or appliances.*
   - @3.1.emb
9. A security lead must protect a fleet of embedded badge readers that will never receive firmware fixes. Which is the BEST compensating approach?
   - **[x] Segment them and monitor their traffic for anomalies**  - [ ] Install host-based firewalls on each reader  - [ ] Move the readers into the screened subnet  - [ ] Delay controls until patch availability improves
   - *When fixes will never come, isolation plus monitoring contains abuse and makes it visible. Host-based firewalls are tempting, but embedded readers cannot run add-on software. A screened subnet is for internet-facing services, and waiting for patches contradicts the scenario. Hook: cannot patch, so fence and watch.*
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
14. Remote battery-backed field sensors began failing weeks early after a firmware update added AES-256 to every message. Which considerations are the team MOST trading off?
    - **[x] Power and compute against security**  - [ ] Responsiveness against scalability  - [ ] Ease of deployment against cost  - [ ] Availability against risk transference
    - *Heavier encryption consumes CPU cycles and battery on constrained devices, so power and compute are traded against security, usually solved with lightweight crypto. Availability is tempting because sensors go down, but the root cause is resource limits, and risk transference is contractual. The other pairs are not about device resources. Hook: every cipher costs battery.*
    - @3.1.power
15. A team selects a SaaS ticketing tool over self-hosting because it can be live in a day with no servers to build. Which consideration drove this?
    - **[x] Ease of deployment**  - [ ] Inability to patch  - [ ] Resilience  - [ ] Compute
    - *Ease of deployment = how quickly and simply it goes live. Resilience is surviving failures. Compute is processing capacity. Inability to patch is a negative trait.*
    - @3.1.deploy
16. A finance director asks why the design using one database host, saving 40,000 a year, was rejected. The architect points to last year's half-day trading halt when that same host lost a disk. Which pair of considerations was weighed?
    - **[x] Cost against availability and resilience**  - [ ] Compute against power  - [ ] Responsiveness against risk transference  - [ ] Patch availability against scalability
    - *Saving money on one host against keeping trading running after a fault is the classic cost versus availability and resilience trade-off. Responsiveness is tempting, but it is about speed of reply, not surviving failure. Compute against power and patch availability do not describe a single point of failure. Hook: cheap now, expensive when it breaks.*
    - @3.1.cost
17. A trading firm needs its order system to keep running even if a server dies mid-session. Which architectural feature addresses this MOST directly?
    - **[x] Clustering with automatic failover**  - [ ] Real-time replication to a cold site  - [ ] Hourly snapshots of the order servers  - [ ] Nightly offsite backups with journaling
    - *A cluster with automatic failover keeps the order system running when one node dies, which is high availability. Replication is tempting, but a cold site has no running systems, so service still stops. Snapshots and backups restore later rather than keeping it up. Hook: HA keeps it up, backups bring it back.*
    - @3.1.ha
18. A firm evaluates a network camera vendor. The review finds the vendor publishes security fixes within days of a flaw being disclosed and supports each model for seven years. Which consideration does this MOST directly measure?
   - **[x] Patch availability**  - [ ] Inability to patch  - [ ] Risk transference  - [ ] Responsiveness
   - *Patch availability = whether, and how quickly, fixes exist for a product. Inability to patch is when fixes cannot be applied at all. Risk transference shifts impact by contract. Responsiveness is how fast a system answers requests.*
   - @3.1.patch
19. An app team compares two clouds. One answers API calls in 20 ms, the other in 300 ms. Which consideration is this?
    - **[x] Responsiveness**  - [ ] Risk transference  - [ ] Ease of recovery  - [ ] Inability to patch
    - *Responsiveness = how quickly the system reacts to requests. Users notice it, so it affects availability in practice. The others are about contracts, restore speed and legacy devices.*
    - @3.1.respond
20. A hospital's MRI scanner runs an embedded OS and the vendor says unapproved patches void its regulatory certification and support. What is the BEST way to reduce risk?
    - **[x] Isolate it on a restricted segment with strict allow-lists**  - [ ] Apply OS patches during a planned maintenance window  - [ ] Install EDR on it in monitor-only mode  - [ ] Transfer the risk to the vendor via the support contract
    - *When patching is forbidden, compensating controls such as segmentation, allow-listing and monitoring reduce risk without touching the certified build. Monitor-only EDR is tempting, but installing any agent is itself an unapproved change. Patching in a window still breaks certification, and transferring risk does not reduce it. Hook: cannot touch it, so wall it off.*
    - @3.1.emb
21. PBQ 3.1 - Match the system. A city's operations centre lists its devices. Pick the BEST term for each. ¶  1  Supervisory system watching water pumps across the city ¶  2  Controller that must fire the airbags in vehicles within a guaranteed few milliseconds ¶  3  Smart bins that report fill level over Wi-Fi ¶  4  Firmware-only controller inside each parking meter
    - [p] Device 1 :: A SCADA · B RTOS · C IoT · D Embedded system = a
    - [p] Device 2 :: A SCADA · B RTOS · C IoT · D Embedded system = b
    - [p] Device 3 :: A SCADA · B RTOS · C IoT · D Embedded system = c
    - [p] Device 4 :: A SCADA · B RTOS · C IoT · D Embedded system = d
    - *1: wide-area supervision of industrial process = SCADA. 2: guaranteed timing = RTOS. 3: consumer-style connected sensor = IoT. 4: dedicated computer in a product = embedded. Overlap is real (IoT devices are embedded too); pick the most specific fit.*
    - @3.1.models

## Test 13 - 3.2 Secure Enterprise Infrastructure: Placement, Appliances, Firewalls, Secure Comms (25 Q)

1. A company is putting a public web server online. Where is it BEST placed?
   - **[x] In a screened subnet between two firewall interfaces**  - [ ] On the internal LAN behind a reverse proxy  - [ ] In the management VLAN beside the jump server  - [ ] On the internal LAN with a host-based firewall
   - *A screened subnet lets the public reach the server while a compromise still has a firewall between it and internal systems. A reverse proxy is tempting, but the server itself would still sit on the trusted LAN. The management VLAN and a host firewall alone mix public exposure with trusted zones. Hook: the hotel lobby, not the back office.*
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
   - **[x] Active devices can block traffic; passive ones only observe and alert**  - [ ] Active devices are always inline; passive ones are always on a tap  - [ ] Passive devices fail closed; active devices fail open  - [ ] Active devices send probes; passive ones only read logs
   - *Active means the device can take action such as dropping packets (IPS), while passive only watches and alerts (IDS). The always-inline claim is tempting, but placement and activity are separate attributes that merely tend to go together. Failure modes are unrelated, and passive sensors read traffic copies, not just logs. Hook: active acts, passive reports.*
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
    - **[x] 802.1X with EAP and a RADIUS server**  - [ ] Port security with MAC address filtering  - [ ] A separate VLAN for conference rooms  - [ ] A captive portal on the wired network
    - *802.1X keeps each port blocked until the device or user authenticates through EAP to RADIUS. MAC filtering is tempting, but MAC addresses are easily spoofed. A VLAN separates traffic without authenticating anyone, and a captive portal is weak web-based gating. Hook: show ID at the door, not just a name tag.*
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
19. Remote staff on unmanaged home PCs need encrypted access to internal file shares over TCP 443, and IT cannot install any software on those PCs. Which option fits BEST?
    - **[x] A TLS VPN portal**  - [ ] An IPSec remote-access VPN  - [ ] IPSec tunnel mode with ESP  - [ ] An SD-WAN edge appliance
    - *A TLS VPN can run clientless in the browser over 443, so nothing needs installing. An IPSec remote-access VPN is tempting, but it needs a client on each PC. Tunnel mode ESP is also IPSec, and SD-WAN connects sites, not individual users. Hook: TLS rides in the browser.*
    - @3.2.vpn
20. Two offices need a permanent encrypted link where the payload AND the original IP headers are protected. Which configuration is BEST?
    - **[x] IPSec in tunnel mode with ESP**  - [ ] IPSec in transport mode with AH only  - [ ] An unencrypted GRE tunnel  - [ ] A TLS forward proxy
    - *Tunnel mode wraps the entire original packet in a new one; ESP encrypts. Transport mode protects only the payload, and AH gives integrity without encryption. Hook: tunnel = packet inside an armoured van; transport = only the letter is sealed.*
    - @3.2.tunnel
21. A retailer with 200 stores wants to route traffic over cheap broadband and 4G links, steering cloud app traffic directly to the cloud instead of back through headquarters. Which technology fits?
    - **[x] SD-WAN**  - [ ] MPLS  - [ ] IPSec site-to-site VPN  - [ ] UTM
    - *SD-WAN centrally steers traffic per application over any mix of links, including breaking cloud traffic out locally. A site-to-site IPSec VPN is tempting, but it only encrypts fixed tunnels and does no app-aware path selection. MPLS is a costly carrier circuit, and UTM is a security appliance. Hook: SD-WAN picks the road per app.*
    - @3.2.sdwan
22. A consultancy has closed its offices and wants its staff, wherever they are, to get firewalling, web filtering and zero trust access from cloud points of presence near them, joined with SD-WAN networking. What is this model?
    - **[x] SASE (Secure Access Service Edge)**  - [ ] UTM appliance at headquarters  - [ ] IPSec transport mode  - [ ] A screened subnet
    - *SASE = network plus security as a cloud service at the edge, near users. Hook: SD-WAN plus a security stack in the cloud. A UTM at HQ forces traffic home. The others are single mechanisms.*
    - @3.2.sase
23. A branch office will reach head office over the public internet, a leased line or 4G backup. The architect must decide which links carry which traffic and how each is secured. Which infrastructure consideration is she addressing?
   - **[x] Connectivity**  - [ ] Failure modes  - [ ] Device attribute  - [ ] Attack surface
   - *Connectivity = how sites and devices are linked (internet, MPLS, cellular, satellite) and the security each link needs, such as VPN encryption over untrusted links. Failure modes describe fail-open or fail-closed. Device attribute is active vs. passive or inline vs. tap/monitor.*
   - @3.2.conn
24. A security manager has budget for one control at a branch where ransomware recently arrived inside an HTTPS download that the old port-based firewall permitted. Which choice MOST effectively addresses the gap?
    - **[x] An NGFW with application and content inspection**  - [ ] A second stateful firewall from another vendor  - [ ] An IDS sensor connected to a SPAN port  - [ ] A web application firewall at the branch
    - *An NGFW inspects content inside allowed traffic and can block malware in downloads. The WAF is tempting, but it protects web servers from inbound attacks, not users downloading files. A second stateful firewall sees the same ports, and an IDS on a SPAN can only alert. Hook: match the control to the gap.*
    - @3.2.select
25. PBQ 3.2 - Network design. A clinic is building a new site. Choose the BEST control for each need. ¶  1  Stop unknown devices joining via wall ports ¶  2  Block XSS against the patient portal ¶  3  Admins reach the server zone through one monitored host ¶  4  Watch internal traffic without risk of dropping packets ¶  5  Encrypted link to head office, whole packet protected
    - [p] Need 1 (Stop unknown devices joining via wall ports) :: A 802.1X · B WAF · C Jump server · D IDS on a tap · E IPSec tunnel mode = a
    - [p] Need 2 (Block XSS against the patient portal) :: A 802.1X · B WAF · C Jump server · D IDS on a tap · E IPSec tunnel mode = b
    - [p] Need 3 (Admins reach the server zone through one monitored host) :: A 802.1X · B WAF · C Jump server · D IDS on a tap · E IPSec tunnel mode = c
    - [p] Need 4 (Watch internal traffic without risk of dropping packets) :: A 802.1X · B WAF · C Jump server · D IDS on a tap · E IPSec tunnel mode = d
    - [p] Need 5 (Encrypted link to head office, whole packet protected) :: A 802.1X · B WAF · C Jump server · D IDS on a tap · E IPSec tunnel mode = e
    - *1: port-based NAC. 2: layer 7 app inspection. 3: single hardened admin entry. 4: passive monitoring sees copies only. 5: tunnel mode wraps the whole packet. Hook: door, letter-reader, drawbridge, CCTV, armoured van.*
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
12. A software vendor wants customers to confirm that a downloaded installer is bit-for-bit what was released. What should it publish alongside the file?
    - **[x] A SHA-256 hash of the file**  - [ ] An AES-encrypted copy of the file  - [ ] An obfuscated build of the installer  - [ ] A tokenized download URL
    - *A hash is a one-way fingerprint, so any change to the file gives a different value and integrity can be confirmed. Encryption is tempting, but it provides confidentiality, and an altered file can be encrypted just as easily. Obfuscation and tokenization do not verify content. Hook: same fingerprint, same file.*
    - @3.3.hash
13. A developer ships a mobile app and wants to make its JavaScript hard for competitors to read, without encrypting it. Which method fits?
    - **[x] Obfuscation**  - [ ] Tokenization  - [ ] Hashing  - [ ] Geographic restriction
    - *Obfuscation makes something hard to understand while it still works (renaming variables, scrambling logic). It is not strong protection, just a speed bump. The others do not keep code runnable but unreadable.*
    - @3.3.obf
14. A European company must ensure customer data stays subject to EU law and is not stored by its cloud provider in other countries. Which concept is this?
    - **[x] Data sovereignty**  - [ ] Data masking  - [ ] Data in use  - [ ] Obfuscation
    - *Data sovereignty = data is subject to the laws of the country where it is stored. Choose cloud regions and contracts accordingly. The others are protection methods or states, not legal jurisdiction.*
    - @3.3.sov
15. A streaming service's licence allows a film to be shown only to viewers located in Canada. Which method BEST enforces this?
    - **[x] Geographic restrictions**  - [ ] Data sovereignty controls  - [ ] Data segmentation  - [ ] Permission restrictions
    - *Geographic restrictions use the viewer's geolocation (IP or GPS) to allow or block access. Data sovereignty is tempting, but it concerns which laws apply to stored data, not where viewers are. Segmentation isolates data, and permissions control who, not where. Hook: sovereignty is where data lives, geo-restriction is where users stand.*
    - @3.3.geo
16. An auditor asks how a company stops a stolen backup tape from being readable. Which method is the BEST answer?
    - **[x] Encryption with keys stored separately**  - [ ] Tokenization of sensitive fields  - [ ] Hashing of the backup files  - [ ] Masking of account numbers
    - *Encryption makes the whole tape unreadable without a key held elsewhere. Tokenization is tempting, but it only replaces selected fields, leaving the rest readable. Hashing only produces a fingerprint and leaves the tape readable, and masking only hides values on display. Hook: lock the whole box, not a few items.*
    - @3.3.enc
17. A firm keeps HR records on a separate database server on its own network segment, reachable only from the HR application. Which data protection method is this?
    - **[x] Segmentation**  - [ ] Tokenization  - [ ] Obfuscation  - [ ] Hashing
    - *Segmentation separates sensitive data so a breach elsewhere does not reach it. Hook: keep the jewels in a different room. The other three transform the data rather than isolating it.*
    - @3.3.seg
18. A file share holds board minutes. Everyone in the company currently has read access. What is the BEST first fix?
    - **[x] Restrict permissions to the board and named secretaries**  - [ ] Encrypt the share with a key held by IT  - [ ] Move the share to its own network segment  - [ ] Apply a confidential classification label
    - *Tightening ACLs applies least privilege so only those who need the minutes can read them. Segmentation is tempting, but staff could still reach the share if its permissions stay open. Transparent encryption still decrypts for any permitted user, and a label alone enforces nothing. Hook: fix who, not where.*
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
23. A manufacturer's internal pricing playbook is shared with the whole sales force, but leaking it to rivals would hurt the business. It is not personal data and is not limited to a named few. Which classification fits BEST?
    - **[x] Private**  - [ ] Public  - [ ] Confidential  - [ ] Critical
    - *Private (also restricted, classified or internal use only) = not for outsiders; staff may need extra rights or an NDA. Confidential is more sensitive, viewable only with specifically granted access, which does not fit a whole sales force. Public needs no protection. Critical is about availability, not secrecy.*
    - @3.3.class
24. PBQ 3.3 - Pick the protection. A health insurer reviews data flows. Choose the BEST method for each. ¶  1  Agents see only the last four digits of member IDs ¶  2  Card numbers replaced with vault-mapped stand-ins ¶  3  Verify archived claim files were not modified ¶  4  Laptops unreadable if stolen ¶  5  Block logins from outside approved countries
    - [p] Need 1 (Agents see only the last four digits of member IDs) :: A Masking · B Tokenization · C Hashing · D Encryption · E Geographic restrictions = a
    - [p] Need 2 (Card numbers replaced with vault-mapped stand-ins) :: A Masking · B Tokenization · C Hashing · D Encryption · E Geographic restrictions = b
    - [p] Need 3 (Verify archived claim files were not modified) :: A Masking · B Tokenization · C Hashing · D Encryption · E Geographic restrictions = c
    - [p] Need 4 (Laptops unreadable if stolen) :: A Masking · B Tokenization · C Hashing · D Encryption · E Geographic restrictions = d
    - [p] Need 5 (Block logins from outside approved countries) :: A Masking · B Tokenization · C Hashing · D Encryption · E Geographic restrictions = e
    - *1: partial display = masking. 2: random stand-in with lookup = tokenization. 3: integrity check = hashing. 4: unreadable without key = encryption. 5: location-based access = geographic restrictions. Hook: hide, swap, fingerprint, lock, fence.*
    - @3.3.meth

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
    - **[x] Encrypt the backups**  - [ ] Hash the backup files  - [ ] Replicate them to a second vault  - [ ] Replace them with snapshots
    - *Encrypting offsite backups keeps their contents unreadable if a drive is lost, provided keys are held separately. Hashing is tempting, but it only proves integrity and hides nothing. Replication and snapshots add copies or speed but do nothing for confidentiality. Hook: if it leaves the building, lock it.*
    - @3.4.bkp
17. A company can lose at most 15 minutes of order data. Its backups run nightly. Which backup consideration should change FIRST?
    - **[x] Frequency**  - [ ] Onsite/offsite placement  - [ ] Restore testing  - [ ] Encryption
    - *How often you back up sets how much data you can lose, so nightly runs cannot meet a 15-minute RPO. Restore testing is tempting because it is good practice, but it does not shrink the data-loss window. Placement and encryption address disasters and theft. Hook: frequency fixes RPO.*
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
21. An IT manager boasts that nightly backups have completed for two years, yet nobody can say whether the files are usable or how long getting systems back would take. Which backup consideration is MOST neglected?
   - **[x] Recovery**  - [ ] Frequency  - [ ] Onsite/offsite  - [ ] Encryption
   - *The recovery consideration means regularly test-restoring to prove backups work and to measure how long it takes. Frequency is tempting, but nightly runs say nothing about whether data can be used. Placement and encryption protect copies, they do not prove them. Hook: a backup you never restored is just a hope.*
   - @3.4.bkp
22. A data centre wants servers to keep running through a brief power blip and for long enough to start backup power during a longer outage. What combination is BEST?
    - **[x] A UPS for the short term, plus a generator for the long term**  - [ ] A generator alone  - [ ] A UPS alone for multi-day outages  - [ ] A surge protector and a cold site
    - *UPS = battery, instant, minutes of runtime; bridges the gap until the generator starts. Generator = fuel, long-running, takes time to start. Hook: the UPS catches you, the generator carries you.*
    - @3.4.pwr
23. A retailer's recovery facility already has racks, servers and network links installed, but staff must load the latest backups and configure systems before it can take over, which takes about a day. Which site type is this?
    - **[x] Warm site**  - [ ] Hot site  - [ ] Cold site  - [ ] Multi-cloud
    - *Warm site = equipment in place, data and configuration still to load; hours to a day or so. Hot is live with current data. Cold is space and power only. Multi-cloud is spreading across providers, not a recovery facility.*
    - @3.4.site
24. PBQ 3.4 - Resilience plan. A regional insurer is upgrading resilience. Choose the BEST fit for each need. ¶  1  Back online within minutes after losing HQ ¶  2  Keep servers up for the 30 seconds before backup power takes over ¶  3  Payment engine keeps processing when a single processor fails ¶  4  Roll back a VM quickly after a bad patch ¶  5  Stay up if one hosting vendor suffers a global outage
    - [p] Need 1 (Back online within minutes after losing HQ) :: A Hot site · B UPS · C Parallel processing · D Snapshot · E Multi-cloud · F Generator · G Warm site = a
    - [p] Need 2 (Keep servers up for the 30 seconds before backup power takes over) :: A Hot site · B UPS · C Parallel processing · D Snapshot · E Multi-cloud · F Generator · G Warm site = b
    - [p] Need 3 (Payment engine keeps processing when a single processor fails) :: A Hot site · B UPS · C Parallel processing · D Snapshot · E Multi-cloud · F Generator · G Warm site = c
    - [p] Need 4 (Roll back a VM quickly after a bad patch) :: A Hot site · B UPS · C Parallel processing · D Snapshot · E Multi-cloud · F Generator · G Warm site = d
    - [p] Need 5 (Stay up if one hosting vendor suffers a global outage) :: A Hot site · B UPS · C Parallel processing · D Snapshot · E Multi-cloud · F Generator · G Warm site = e
    - *1: minutes to recover needs a hot site; a warm site needs hours to load data. 2: only a UPS bridges instantly; the generator is what takes 30 seconds to start. 3: parallel processing drops the failed CPU and the rest carry on. 4: a snapshot is a point-in-time VM copy. 5: multi-cloud avoids dependence on one provider. Hook: ready room, battery, many hands, photo, second landlord.*
    - @3.4.res

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
   - **[x] Replace default credentials and manage them over SSH, not Telnet**  - [ ] Enable SNMPv2c with a unique community string  - [ ] Upgrade the firmware once they are in production  - [ ] Build a site-to-site VPN for management traffic
   - *Default credentials and cleartext management are the first things attackers try, so unique credentials and SSH come before go-live. SNMPv2c is tempting, but its community strings travel in cleartext; SNMPv3 is the secure choice. Updating firmware after go-live leaves a window, and a VPN does not fix default logins. Hook: change the locks before you open the doors.*
   - @4.1.hardnet
4. A water utility's SCADA HMI runs an old OS that the vendor will not let you patch without voiding support. What is the BEST way to harden it?
   - **[x] Isolate it on a segmented network with tight firewall rules**  - [ ] Apply OS patches in the next maintenance window  - [ ] Install host-based antivirus in passive mode  - [ ] Place it in the screened subnet for vendor access
   - *Segmentation with strict firewall rules protects the HMI without changing the vendor-supported build, which suits ICS where uptime is critical. Passive antivirus is tempting, but any added software is still an unsupported change and adds attack surface. Patching voids support, and a screened subnet exposes it to the internet. Hook: if you cannot fix the box, fence the box.*
   - @4.1.hardics
5. A medical pump vendor uses a real-time operating system (RTOS) on its devices. Why is hardening an RTOS-based device MORE difficult than hardening a laptop?
   - **[x] Tight timing and resource limits rule out agents and frequent patches**  - [ ] Its firmware is code-signed, so it can never be modified  - [ ] It lacks a network stack, so it cannot be scanned  - [ ] It fails closed whenever any patch is applied
   - *An RTOS must meet strict deadlines on small CPUs and memory, so agents and frequent patches can break timing; rely on vendor updates, segmentation and disabling unused features. Code signing is tempting, but it controls who may update firmware, not whether updates are possible. Many RTOS devices are networked, and fail-closed describes what a control does when it fails, not a hardening step. Hook: timing is the product.*
   - @4.1.hardiot
6. A hotel installs 200 smart TVs and thermostats. Which TWO actions BEST harden these IoT devices? (Select 2)
   - **[x] Change default passwords and keep firmware updated**  - **[x] Place them on a separate VLAN from guest and staff systems**  - [ ] Install endpoint antivirus on each device  - [ ] Hide the SSID that the devices connect to
   - *IoT hardening means removing defaults, updating firmware and segmenting the devices. Endpoint antivirus is tempting, but IoT devices cannot run it. Hiding an SSID is not a control since sniffers still see it. Hook: the minibar goes in its own locked cupboard.*
   - @4.1.hardiot
7. A start-up's cloud account was set up quickly. Which hardening action gives the BIGGEST reduction in risk to the cloud infrastructure?
   - **[x] Enforce MFA on root and admin accounts and remove unused access keys**  - [ ] Encrypt every storage bucket with provider-managed keys  - [ ] Put a web application firewall on all public endpoints  - [ ] Replicate all workloads to a second region for resilience
   - *Cloud breaches mostly start with compromised identities, so MFA on privileged accounts and removing stale keys cuts risk the most. Provider-managed encryption is tempting, but a stolen admin key can still read the data. A WAF protects only web apps, and a second region improves availability but does nothing about the stolen-credential risk. Hook: in the cloud, identity is the perimeter.*
   - @4.1.hardcloud
8. A new file server is built from a standard image. Which change BEST hardens it as a server and also benefits a workstation build?
   - **[x] Remove unneeded services and enable a host-based firewall**  - [ ] Move the server into the screened subnet  - [ ] Apply data masking to all shared files  - [ ] Configure it as the jump server for admins
   - *Least functionality plus a host firewall shrinks the attack surface on both servers and workstations. The screened subnet is tempting, but placement is network design, not host hardening, and a file server belongs inside. Masking and a jump server role do not harden the build. Hook: if it is not needed, it is not installed.*
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
12. A sales rep often works from coffee shops. Which connection choice is MOST secure for reaching company systems?
    - **[x] Use the phone's cellular data rather than cafe Wi-Fi**  - [ ] Join cafe Wi-Fi that uses a captive portal  - [ ] Join the cafe Wi-Fi with the strongest signal  - [ ] Tether over Bluetooth to a colleague's laptop
    - *Cellular data is encrypted to the carrier and avoids rogue access points, so it is safer than open Wi-Fi (a VPN adds more). A captive portal is tempting, but it only gates access and does not encrypt traffic. The strongest signal may be an evil twin, and Bluetooth tethering adds pairing risks. Hook: open Wi-Fi is shouting in a crowded cafe.*
    - @4.1.conn
13. A law firm is replacing WPA2-PSK. It wants a mode that resists offline dictionary attacks on a shared passphrase. Which should it choose?
    - **[x] WPA3-Personal with SAE**  - [ ] WPA2-Personal with TKIP  - [ ] WEP with a 128-bit key  - [ ] An open network with a captive portal
    - *WPA3 replaces the PSK 4-way handshake with SAE (Simultaneous Authentication of Equals, a dragonfly handshake) that resists offline guessing and gives forward secrecy. TKIP and WEP are deprecated. A captive portal does not encrypt traffic.*
    - @4.1.wpa3
14. A hospital wants every clinician to log on to Wi-Fi with their own directory account so access can be revoked per person. Which design BEST fits?
    - **[x] WPA3-Enterprise using 802.1X with a RADIUS server**  - [ ] WPA3-Personal with one passphrase per ward  - [ ] MAC address filtering on each access point  - [ ] A hidden SSID with a long passphrase
    - *Enterprise mode = 802.1X port-based authentication; the AP passes credentials to a AAA server (RADIUS) that checks the directory. Per-user accounts, per-user revocation and accounting. Shared passphrases cannot be revoked per person. MAC filtering is easily spoofed. Hiding the SSID is not authentication.*
    - @4.1.aaa
15. A university's 802.1X Wi-Fi should authenticate users with a username and password but protect the exchange inside a TLS tunnel, without issuing a certificate to every student. Which EAP method fits BEST?
    - **[x] PEAP**  - [ ] EAP-TLS  - [ ] LEAP  - [ ] PAP
    - *PEAP (and EAP-TTLS) build a TLS tunnel using only a server certificate, then send the user's password inside it. EAP-TLS needs client certificates on every device. LEAP is old Cisco and weak. PAP sends passwords in the clear. Hook: PEAP = Protected, server cert only.*
    - @4.1.auth
16. A web form accepts an order quantity. Testers enter "1; DROP TABLE orders" and the app errors. What is the BEST fix in the code?
    - **[x] Server-side input validation using an allow list**  - [ ] Client-side input validation in JavaScript  - [ ] A WAF rule that blocks the word DROP  - [ ] Generic error pages that hide SQL details
    - *Server-side validation with an allow list rejects anything that is not an integer in range, and attackers cannot bypass it (pair it with parameterized queries). Client-side validation is tempting, but a proxy skips it entirely. A keyword WAF rule is easily evaded, and hiding errors leaves the flaw in place. Hook: never trust the browser.*
    - @4.1.input
17. A banking app's session cookie was stolen by a script injected into a forum page and also captured on an HTTP link. Which cookie attributes would have helped MOST?
    - **[x] HttpOnly and Secure**  - [ ] Expires and Path  - [ ] Domain and Max-Age  - [ ] SameSite=None and Path
    - *Secure cookies: HttpOnly stops JavaScript reading the cookie (XSS theft); Secure sends it only over HTTPS. SameSite helps against CSRF, but setting it to None removes that protection. Expiry and path settings do not stop either theft. Hook: HttpOnly = hands off for scripts, Secure = only in the armoured truck.*
    - @4.1.cookie
18. A development team wants to find hard-coded passwords and unsafe functions in source code before it is ever compiled or run. Which technique is BEST?
    - **[x] Static code analysis (SAST)**  - [ ] Dynamic analysis of the running app (DAST)  - [ ] Fuzzing the production API  - [ ] A user acceptance test
    - *Static analysis reads the code without executing it and flags patterns like hard-coded secrets and buffer overflows. Dynamic analysis and fuzzing need a running app. UAT checks business features, not security flaws. Note: static analysis can produce false positives that need review.*
    - @4.1.sast
19. Users get an OS warning that a new desktop tool's publisher cannot be verified. IT wants to prove each internal release came from the company and was not altered. What should the build pipeline add?
    - **[x] Code signing with the company's code-signing certificate**  - [ ] Obfuscation of the source code  - [ ] A self-extracting ZIP archive  - [ ] An MD5 checksum on the intranet page
    - *Code signing = a digital signature over the binary, proving origin (publisher) and integrity. Obfuscation hides logic but proves nothing. ZIP is packaging. A bare hash on the same site can be swapped with the file, and MD5 is weak. Hook: a wax seal on the package.*
    - @4.1.sign
20. Analysts want to open suspicious email attachments to see what they do without risking the corporate network. Which control is BEST?
    - **[x] A sandbox that runs the file in isolation**  - [ ] Static code analysis of the attachment  - [ ] A honeyfile placed on the file server  - [ ] A forward proxy that scans downloads
    - *A sandbox executes untrusted files in an isolated environment so analysts can watch their behaviour safely. Static analysis is tempting, but it reads code without running it, so it cannot show what the file does. A honeyfile detects access, and a proxy filters traffic. Hook: let it run in a cage.*
    - @4.1.sandbox
21. A mobile app team pushes a new release. Which practice BEST lets the team detect attacks against the app once it is in production?
    - **[x] Centralise app logs and alert on unusual errors or access**  - [ ] Run static code analysis before each release  - [ ] Sign every release with a code-signing certificate  - [ ] Validate all input on the server side
    - *Monitoring means watching the app after release through logs and alerts, because pre-release testing misses things. Static analysis is tempting, but it is a pre-release check that sees nothing in production. Code signing and input validation prevent problems rather than detect them. Hook: test before, watch after.*
    - @4.1.mon
22. A manufacturer uses embedded controllers in conveyor belts. Which hardening approach is MOST realistic?
    - **[x] Vendor firmware updates plus network segmentation**  - [ ] Install an EDR agent on each controller  - [ ] Enrol each controller in the MDM console  - [ ] Place the controllers in the screened subnet
    - *Embedded controllers have limited resources and fixed functions, so harden them with vendor firmware, disabled unused interfaces and isolation. EDR is tempting, but controllers cannot run host agents. MDM is for mobile devices, and the screened subnet exposes them to the internet. Hook: fixed box, fenced box.*
    - @4.1.hardics
23. A field team uses tablets that store customer signatures. Which mobile hardening setting is MOST important if a tablet is stolen?
    - **[x] Full device encryption with a strong screen lock**  - [ ] Remote wipe enabled through the MDM  - [ ] Geofencing limited to customer sites  - [ ] Bluetooth and NFC radios disabled
    - *Encryption with a strong lock keeps the data unreadable even if the thief keeps the tablet offline. Remote wipe is tempting, but it only works if the device reconnects, which a thief can prevent. Geofencing and disabling radios do not protect stored data. Hook: wipe needs a signal, encryption does not.*
    - @4.1.hardmob

### Key facts
- **Baseline: establish, deploy, maintain. Hardening targets: mobile, workstations, switches, routers, cloud, servers, ICS/SCADA, embedded, RTOS, IoT.**
- **Wireless install: site survey, heat map. Security: WPA3 (SAE), AAA/RADIUS with 802.1X, EAP (PEAP, EAP-TLS, EAP-TTLS).**
- **Mobile: MDM; BYOD, COPE, CYOD; cellular, Wi-Fi, Bluetooth.**
- **App security: input validation, secure cookies, static code analysis, code signing, sandboxing, monitoring.**
24. PBQ 4.1 - Mobile deployment models. Match each company's plan to the model.
    - [p] Staff use phones they bought themselves, with a work app added :: A BYOD · B COPE · C CYOD = a
    - [p] The firm buys and owns the phones and lets staff install games and social apps :: A BYOD · B COPE · C CYOD = b
    - [p] Staff select one of three approved models, which the firm then buys and owns :: A BYOD · B COPE · C CYOD = c
    - [p] Which model gives the company LEAST control over the device :: A BYOD · B COPE · C CYOD = a
    - [p] Link abused when an attacker about 10 metres away pulls contacts from a discoverable phone :: A Cellular · B Wi-Fi · C Bluetooth · D NFC = c
    - *BYOD means the user owns the device, so the company has least control; COPE is corporate-owned but personally enabled; CYOD is a company-owned device chosen from an approved list. COPE and CYOD are easy to confuse, but CYOD is defined by the choice from a list, COPE by personal use of a company phone. Bluesnarfing steals data over Bluetooth at around 10 metres, while NFC works only within centimetres. Hook: B = Bring, P = Personally enabled, C = Choose.*
    - @4.1.deploy

## Test 17 - 4.2 + 4.3 Asset Management, Disposal, Vulnerability Management (27 Q)

1. A marketing team signs up for a cloud note-taking service on a corporate card, and security only learns of it when customer data appears in it. At which asset lifecycle stage should this have been caught FIRST?
   - **[x] Acquisition/procurement**  - [ ] Assignment/accounting  - [ ] Monitoring/asset tracking  - [ ] Disposal/decommissioning
   - *Acquisition/procurement is the first gate where security vets the vendor, licensing and data handling before purchase, and card purchases that bypass it create shadow IT. Monitoring/asset tracking is tempting because enumeration could later discover the service, but by then the data is already exposed, so it is not the first control point. Hook: vet before you buy.*
   - @4.2.acq
2. During an incident, responders find an old database server and lose hours deciding whether they may shut it down and how sensitive its contents are. Which asset management practice was MOST likely missing?
   - **[x] Assignment of ownership and classification**  - [ ] Enumeration during asset tracking  - [ ] Acquisition through an approved vendor  - [ ] Certification of prior sanitization
   - *Assignment/accounting gives every asset an accountable owner who can make decisions and a classification that states how sensitive its data is. Enumeration is tempting, but the server was already found; discovering it does not tell you who decides or what the data is worth. Hook: no owner means nobody to call at 2 a.m.*
   - @4.2.own
3. A network sweep finds 60 devices answering on the network that are not in the CMDB. Which activity found them, and what should follow?
   - **[x] Enumeration; inventory them with owners, or remove them if unauthorized**  - [ ] Attestation; have each department sign off that its devices are approved  - [ ] Classification; label each device by the sensitivity of the data it holds  - [ ] Sanitization; wipe each device before it is allowed back on the network
   - *Enumeration is the monitoring/asset tracking activity that actively discovers what is really on the network, and unknown devices must then be inventoried with an owner or removed. Attestation is tempting, but it is a periodic owner sign-off of known access, and nobody can attest to devices they do not know about. Hook: count the sheep, then check the ear tags.*
   - @4.2.track
4. A firm retires 50 laptops with SSDs and plans to sell them to staff. Which method is BEST to make the data unrecoverable while keeping the drives usable?
   - **[x] Cryptographic or manufacturer secure erase**  - [ ] Degaussing each drive  - [ ] A multi-pass overwrite of the drive  - [ ] Physical shredding of each drive
   - *Secure erase or crypto erase (destroying the drive's encryption key) is the sanitization method that reaches all flash cells and leaves the SSD reusable. Degaussing is tempting as a classic wipe method, but it has no effect on flash memory, and overwriting misses blocks hidden by wear leveling. Hook: reuse = sanitize; no reuse = destroy.*
   - @4.2.disp
5. A hospital pays a vendor to shred failed hard drives that held patient records. An auditor later asks how the hospital knows those specific drives were destroyed. What should the hospital have obtained?
   - **[x] A certificate of destruction listing serial numbers**  - [ ] A data retention schedule covering the drives  - [ ] An attestation report signed by IT managers  - [ ] An asset inventory entry marked as disposed
   - *Certification is documented proof from the destruction vendor, ideally per serial number, that specific media was destroyed. An inventory entry marked disposed is tempting, but it is only the hospital's own record, not evidence the vendor actually destroyed the drives. Hook: no certificate, no proof.*
   - @4.2.cert
6. Storage admins want to wipe a closed project's mailbox archive to free space, but legal says regulators may request those emails for another six years. What must happen before decommissioning?
   - **[x] Data retention requirements must be met first**  - [ ] The media must be sanitized and the wipe certified  - [ ] The archive must be classified and an owner reassigned  - [ ] The disks must be degaussed to meet compliance
   - *Data retention requirements from law, regulation or policy must be honoured before data is disposed of, so decommissioning waits until the period ends. Sanitization with certification is tempting because it is the proper disposal step, but doing it now destroys records that must legally be kept. Hook: retain first, then sanitize.*
   - @4.2.ret
7. A team must find missing patches and weak configurations across 2,000 servers every week with minimal staff effort. What is the BEST method?
   - **[x] Credentialed vulnerability scanning**  - [ ] Non-credentialed vulnerability scanning  - [ ] Penetration testing  - [ ] A system/process audit
   - *Credentialed scans log in and read installed software and settings, so they reliably find missing patches and misconfigurations at scale with automation. Non-credentialed scanning is tempting, but it only sees what is exposed on the network, missing local patch levels and producing more false positives. Hook: with the keys, the scanner sees inside the house.*
   - @4.3.scan
8. A team pulls dozens of open-source libraries into its app. Which method BEST alerts them when a CVE is later published against one of those components?
   - **[x] Package monitoring**  - [ ] Static analysis  - [ ] Dynamic analysis  - [ ] Code signing
   - *Package monitoring (software composition analysis) tracks third-party components and versions against vulnerability databases and alerts when new CVEs appear. Static analysis is tempting, but it reviews source code at a point in time and does not track flaws newly published against dependencies. Hook: think Log4j.*
   - @4.3.app
9. A tester runs automated attacks against the staging web app while it is running, and finds a reflected XSS. Which analysis type was used?
    - **[x] Dynamic analysis**  - [ ] Static analysis  - [ ] Package monitoring  - [ ] Code signing
    - *Dynamic analysis (DAST) tests the running app from outside, including fuzzing. Static analysis reads code without running it. Package monitoring watches dependencies. Code signing proves origin. Hook: static = reading the recipe, dynamic = tasting the soup.*
    - @4.3.app
10. A hospital CISO wants intelligence about attacks hitting other hospitals, shared by peer members under confidentiality rules. Which source is BEST?
    - **[x] An industry ISAC**  - [ ] A proprietary/third-party threat feed  - [ ] OSINT feeds  - [ ] Dark web monitoring
    - *An ISAC (information sharing and analysis center) is a sector-specific body whose members share threat data with each other in confidence. A proprietary feed is tempting because it is high quality, but it is sold by a vendor rather than shared among sector peers. Hook: ISAC = industry insiders sharing.*
    - @4.3.feed
11. A monitoring service reports that employee usernames and passwords are being sold on a criminal marketplace. Which source produced this, and what should the company do FIRST?
    - **[x] Dark web monitoring; reset affected credentials and check for misuse**  - [ ] OSINT; search public paste sites to confirm the scope first  - [ ] An ISAC; report the leak to sector peers before acting  - [ ] Proprietary feed; validate it against a second paid feed
    - *Dark web monitoring finds leaked credentials and data for sale, and the first action is to reset the affected accounts and review logins for misuse. Confirming scope via OSINT is tempting, but it delays containment while attackers may already be using the credentials. Hook: leaked password = reset now, research later.*
    - @4.3.feed
12. A games studio publishes a page explaining how outside researchers may test its matchmaking service, what is out of scope, and how to report findings for payment. What is this?
    - **[x] A bug bounty under a responsible disclosure program**  - [ ] A third-party penetration test under rules of engagement  - [ ] A proprietary threat intelligence feed from researchers  - [ ] An external system audit against a published standard
    - *A responsible disclosure program gives outsiders a published, authorized route to report flaws, and a bug bounty adds payment for valid findings. A penetration test is tempting because it has scope and rules, but it is a contracted engagement with a specific firm, not an open invitation to the public. Hook: open invitation plus payment = bounty.*
    - @4.3.bounty
13. An assessor interviews staff and samples change tickets to see whether patches are approved, tested and deployed as policy requires. Which identification method is this?
    - **[x] A system/process audit**  - [ ] A credentialed vulnerability scan  - [ ] A penetration test  - [ ] Package monitoring
    - *An audit checks whether controls and processes are designed and followed, such as patch approval and testing, by reviewing evidence. A credentialed scan is tempting because it finds missing patches, but it reports the technical state of hosts, not whether the process was followed. Hook: scans check machines, audits check people and paperwork.*
    - @4.3.audit
14. A scanner reports a critical Apache flaw on a server that runs only IIS, and the admin confirms Apache is not installed. What is this, and what should the analyst do?
    - **[x] A false positive; document it and tune the scanner**  - [ ] A false negative; document it and tune the scanner  - [ ] A true positive; raise an exception for the server  - [ ] A true negative; close the finding with no action
    - *A false positive is a reported finding that is not real, so it should be documented and the scanner tuned or the finding suppressed. False negative is tempting because of the word false, but it means a real flaw the scanner missed, the opposite case. Hook: false positive = false alarm, false negative = silent burglar.*
    - @4.3.conf
15. Which scanner outcome is the MOST dangerous for an organization?
    - **[x] A false negative**  - [ ] A false positive  - [ ] A true positive  - [ ] A true negative
    - *False negative = a real vulnerability not reported, so nobody fixes it. False positives waste time but are visible. True positives are found real flaws, which you can fix. True negatives are correct clean results.*
    - @4.3.conf
16. Two findings both score CVSS 8.1. Finding A is on the internet-facing checkout API; finding B is on an isolated training PC with no network cable. Which should be fixed first, and why?
    - **[x] Finding A, because environmental factors raise its priority**  - [ ] Both equally, because the CVSS base scores are identical  - [ ] Finding B, because its fix carries less business risk  - [ ] Neither, until a temporal score shows active exploitation
    - *Environmental variables such as internet exposure, asset value and compensating controls adjust real priority beyond the CVSS base score, so the reachable checkout API comes first. Treating them equally is tempting because the scores match, but base scores describe the flaw in general, not its risk in your environment. Hook: same score, different doorstep.*
    - @4.3.prio
17. A report lists "CVE-2024-12345" next to a finding. What does that identifier provide?
    - **[x] A unique public ID for one specific known flaw**  - [ ] A 0-10 severity rating for that specific flaw  - [ ] A category of weakness type such as injection  - [ ] An entry in a checklist of secure settings
    - *CVE (Common Vulnerability Enumeration in the objectives) is a unique public identifier, maintained by MITRE and used in NIST's NVD, so all tools and vendors refer to the same flaw. The severity rating is tempting, but that is CVSS, a separate score, and weakness categories are CWE. Hook: CVE is the name tag, CVSS is the thermometer.*
    - @4.3.cvss
18. A flaw would expose about 40% of a customer database's value if exploited. Which analysis term describes this percentage?
    - **[x] Exposure factor**  - [ ] Risk tolerance  - [ ] Vulnerability classification  - [ ] Environmental variable
    - *Exposure factor = percentage of an asset's value lost if the threat happens (used in SLE = asset value x EF). Risk tolerance = how much risk the business will accept. Classification sorts flaw types. Environmental variables adjust priority for your setup.*
    - @4.3.ef
19. A high-severity flaw affects a legacy controller with no vendor patch. Production cannot stop. What is the BEST response?
    - **[x] Segment it, add compensating controls and record an exception**  - [ ] Transfer the risk by buying cyber insurance for the line  - [ ] Accept the risk informally until a patch is released  - [ ] Rescan weekly and validate until the vendor issues a fix
    - *When patching is impossible, segmentation and compensating controls reduce exposure, and a documented, approved exception records the decision. Insurance is tempting because it is a listed response, but it only transfers financial impact and does nothing to stop exploitation. Hook: cannot patch? Fence it and write it down.*
    - @4.3.resp
20. A business unit asks to skip a required patch on one app for 90 days during peak season. What makes this an acceptable exception?
    - **[x] Risk owner approval, an expiry date and compensating controls**  - [ ] A help desk ticket recording the business request  - [ ] A rescan confirming the flaw is still rated medium  - [ ] Segmentation of the app, which removes the need for approval
    - *Exceptions/exemptions are acceptable only when formally approved by someone with authority to accept the risk, time-limited and backed by compensating controls. Segmentation is tempting because it reduces risk, but it does not replace documented approval for not meeting the requirement. Hook: exception = signed, dated, compensated.*
    - @4.3.resp
21. After a patch rollout, how should the team BEST validate remediation?
    - **[x] Rescan the affected systems to confirm the finding is gone**  - [ ] Confirm the patch tool shows the job deployed successfully  - [ ] Check the CVSS score to confirm the severity has dropped  - [ ] Request attestation from each system owner by email
    - *Validation means verifying the fix actually took, usually by rescanning and confirming the finding no longer appears. A successful deployment status is tempting, but it only shows the job ran; installs can fail, need reboots or miss hosts. Hook: trust, but rescan.*
    - @4.3.valid
22. The board wants to understand the vulnerability program's progress. Which report is MOST useful to them?
    - **[x] Trends in open criticals and time to remediate**  - [ ] Per-host findings with CVE IDs and CVSS scores  - [ ] Scan coverage logs listing every host scanned  - [ ] A list of this month's false positives tuned out
    - *Vulnerability reporting should fit its audience, and executives need trends, risk and remediation speed to judge progress. Per-host CVE detail is tempting because it is accurate, but it is engineer-level data that does not show whether risk is going down. Hook: the board wants the trend line, not the spreadsheet.*
    - @4.3.report
23. A company with low risk tolerance finds a medium-severity flaw with a working public exploit on its customer portal. What is MOST likely?
    - **[x] Remediate quickly despite the medium score**  - [ ] Accept it, since only highs exceed tolerance  - [ ] Record an exception until the next cycle  - [ ] Buy insurance to transfer the risk
    - *Low risk tolerance plus a public exploit on a customer-facing system raises priority beyond the raw CVSS rating, so fast remediation is expected. An exception is tempting as a formal response, but exceptions suit cases where fixing is impractical, not a fixable, actively exploitable flaw at a low-tolerance firm. Hook: context beats the score.*
    - @4.3.prio
24. A scanner groups findings as "missing patch", "misconfiguration", "weak cipher" and "default credentials", and maps each to a CWE type. Which 4.3 analysis activity is this?
    - **[x] Vulnerability classification**  - [ ] Exposure factor  - [ ] Risk tolerance  - [ ] Responsible disclosure
    - *Vulnerability classification = sorting flaws by type or category (for example by CWE or by missing patch versus misconfiguration) so similar issues get the same fix and owner. Exposure factor is the percentage of value lost. Risk tolerance is how much risk the business accepts. Responsible disclosure is how outsiders report flaws.*
    - @4.3.class
25. A bank hires an outside firm, under a signed scope and rules of engagement, to actively exploit weaknesses in its online banking platform and show how far an attacker could get. Which identification method is this?
    - **[x] Penetration testing**  - [ ] A credentialed vulnerability scan  - [ ] An OSINT threat feed  - [ ] A proprietary/third-party threat feed
    - *Penetration testing = authorized, scoped attempts to exploit vulnerabilities and chain them, proving real impact. A scan only identifies likely flaws without exploiting them. OSINT feeds are free public intelligence; proprietary/third-party feeds are paid commercial intelligence. Neither tests your systems. Hook: the scan finds the unlocked door, the pen test walks through it.*
    - @4.3.pentest
26. A retailer cannot fully patch its legacy point-of-sale estate this year. The board buys a policy that pays breach response, legal and notification costs if a card-data flaw is exploited. Which vulnerability response is this?
   - **[x] Insurance**  - [ ] Segmentation  - [ ] Compensating controls  - [ ] An exception/exemption
   - *Insurance (cyber insurance) transfers part of the financial impact to an insurer; it does not remove the flaw. Segmentation isolates the systems on the network. Compensating controls are other safeguards that reduce the risk. An exception/exemption formally records a decision not to apply a required fix. Hook: insurance pays for the damage, it does not stop it.*
    - @4.3.insure

### Key facts
- **4.2: acquisition/procurement; assignment (ownership, classification); monitoring (inventory, enumeration); disposal (sanitization, destruction, certification, data retention).**
- **4.3 identify: vuln scan, app security (static, dynamic, package monitoring), threat feeds (OSINT, proprietary/third-party, ISAC, dark web), pen test, responsible disclosure/bug bounty, audit.**
- **Analysis: false positive/negative, prioritize, CVSS (score), CVE (ID), classification, exposure factor, environmental variables, impact, risk tolerance.**
- **Response: patch, insurance, segmentation, compensating controls, exceptions/exemptions. Validate: rescan, audit, verify. Then report.**
27. PBQ 4.2 - Asset lifecycle. Match each event to the stage.
   - [p] Security reviews a SaaS provider's SOC 2 report before the contract is signed :: A Acquisition · B Assignment · C Monitoring/tracking · D Disposal = a
   - [p] The payroll manager is named responsible for a new server and its data is labelled Confidential :: A Acquisition · B Assignment · C Monitoring/tracking · D Disposal = b
   - [p] A quarterly sweep compares hosts answering on the network with the CMDB :: A Acquisition · B Assignment · C Monitoring/tracking · D Disposal = c
   - [p] Backup tapes past their legal hold period go to a vendor who returns serial-numbered proof :: A Acquisition · B Assignment · C Monitoring/tracking · D Disposal = d
   - [p] Best method for magnetic tape that will never be reused :: A Single-pass overwrite · B Degauss or shred · C Cryptographic erase · D Quick format = b
   - *Acquisition is vetting before buying, assignment sets owner and classification, monitoring enumerates and reconciles inventory, and disposal covers destruction, certification and retention. For tapes that will not be reused, degauss or shred; cryptographic erase is tempting but only works if the data was encrypted with a key you can destroy. Hook: buy, own, watch, dispose.*
   - @4.2.disp

## Test 18 - 4.4 Security Monitoring + Tools: SIEM, SCAP, NetFlow, DLP (22 Q)

1. An analyst must correlate failed VPN logins, firewall denies and domain controller events from 30 sources on one screen. Which tool is BEST?
   - **[x] A SIEM**  - [ ] A vulnerability scanner  - [ ] A NetFlow collector alone  - [ ] A host-based antivirus console
   - *SIEM (security information and event management) aggregates logs from many sources, normalizes and correlates them, alerts, and keeps them for reporting. NetFlow shows traffic metadata only. Scanners find flaws. Antivirus sees only endpoints. Hook: SIEM = the control room with every camera feed.*
   - @4.4.siem
2. A SOC's SIEM fires 4,000 alerts a day, almost all from one nightly backup job copying large volumes to a storage server. Analysts now skim the queue. What is the BEST fix?
   - **[x] Tune the rule to exclude the known backup activity**  - [ ] Lower the severity of all data transfer alerts  - [ ] Archive these alerts and review them weekly  - [ ] Add a correlation rule that escalates repeats
   - *Alert tuning removes known benign activity from a specific rule, cutting false positives so real alerts get attention. Lowering severity for all transfer alerts is tempting, but it also buries genuine exfiltration alerts. Hook: tune narrowly, not broadly.*
   - @4.4.tune
3. The SIEM flags a workstation beaconing to a known malware domain at 03:00. What is the BEST immediate response?
   - **[x] Quarantine the host, then investigate**  - [ ] Run an antivirus scan, then close the alert  - [ ] Reimage the host to remove the malware  - [ ] Tune the rule to confirm a true positive
   - *Quarantine isolates the host to stop spread or exfiltration while preserving evidence for investigation. Reimaging is tempting because it removes the malware, but it destroys forensic evidence and skips scoping how far the attacker got. Hook: isolate first, clean later.*
   - @4.4.resp
4. A regulator requires one year of security logs, but the SIEM's searchable storage holds only 90 days. Which monitoring activity BEST meets the requirement?
   - **[x] Archiving**  - [ ] Log aggregation  - [ ] Alert tuning  - [ ] Reporting
   - *Archiving moves older logs to cheaper long-term storage so retention rules are met and later investigations remain possible. Log aggregation is tempting because it centralizes logs, but it is about collection, not keeping data beyond the SIEM's window. Hook: aggregate to see, archive to keep.*
   - @4.4.arch
5. Which list BEST describes the three resource categories 4.4 says you should monitor?
   - **[x] Systems, applications and infrastructure**  - [ ] People, processes and policies  - [ ] Hot, warm and cold sites  - [ ] Confidentiality, integrity and availability
   - *Monitoring computing resources = systems (servers, endpoints), applications (app logs, errors), and infrastructure (network devices, cloud). The others are lists from other objectives.*
   - @4.4.res
6. A government contractor wants tools from different vendors to check 500 servers against the same published hardening checklist and exchange results in standard formats. Which framework fits BEST?
   - **[x] SCAP**  - [ ] CIS Benchmarks  - [ ] STIX/TAXII  - [ ] CVSS
   - *SCAP is a NIST suite of standards (XCCDF, OVAL, CVE, CVSS and others) that lets different tools share compliance content and results. CIS Benchmarks are tempting because they are hardening checklists, but they are the content, not the interoperable format and protocol suite tools use to exchange it. Hook: Benchmark = the what, SCAP = how tools speak it.*
   - @4.4.scap
7. A team wants a vendor-neutral, consensus set of configuration settings for Windows Server and Ubuntu to measure systems against. What should they use?
   - **[x] CIS Benchmarks**  - [ ] SCAP  - [ ] The NVD CVE list  - [ ] A NetFlow baseline
   - *CIS Benchmarks are prescriptive, consensus-based secure configuration guides for specific products. SCAP is tempting, but it is the protocol suite used to automate checking, not a vendor-neutral list of recommended settings itself. Hook: the benchmark is the recipe.*
   - @4.4.bench
8. A factory has PLC sensors that cannot run third-party software, plus Windows servers that can. Which monitoring approach fits EACH?
   - **[x] Agentless for the sensors; agent-based for the servers**  - [ ] Agent-based for the sensors; agentless for the servers  - [ ] Agentless for both, for consistent coverage and less upkeep  - [ ] Agent-based for both, using lightweight embedded agents
   - *Agentless monitoring queries or observes devices over the network and suits hosts that cannot run software, while agents give deeper visibility on hosts that can. Agentless for both is tempting for simplicity, but it gives up the process, file and local log detail agents provide on servers. Hook: no installs possible = agentless.*
   - @4.4.agent
9. A router's interface goes down and it sends an unsolicited alert to the management station. What is this?
   - **[x] An SNMP trap**  - [ ] An SNMP GET request  - [ ] A NetFlow record  - [ ] A syslog archive
   - *SNMP traps are sent by the device on an event (to UDP 162); polling (GET) is the manager asking (UDP 161). Use SNMPv3 for authentication and encryption. NetFlow records traffic conversations. Archives are storage. Hook: a trap springs by itself.*
   - @4.4.snmp
10. A university's internet link is saturated. The network team needs records of who talked to whom, on which ports and how many bytes, for every conversation, but cannot store full captures. Which tool fits BEST?
    - **[x] NetFlow**  - [ ] Full packet capture  - [ ] SNMP polling of interface counters  - [ ] A SIEM with firewall logs
    - *NetFlow records flow metadata such as source, destination, ports, protocol and bytes, which is light to store. SNMP interface polling is tempting because it shows bandwidth use, but only totals per interface, not who was talking to whom. Hook: SNMP says the pipe is full, NetFlow says who filled it.*
    - @4.4.flow
11. NetFlow shows a print server sent 40 GB to an unfamiliar external IP overnight, with no change tickets raised. What is the BEST conclusion?
    - **[x] Possible exfiltration requiring investigation**  - [ ] A false positive caused by print spooling  - [ ] A routine patch download from the vendor  - [ ] A true negative against the NetFlow baseline
    - *Large outbound flows from a host that should send little externally are a classic exfiltration indicator needing investigation. A vendor patch download is tempting as routine, but that would be inbound traffic, not 40 GB sent out. Hook: watch the direction of the bytes.*
    - @4.4.flow
12. An employee tries to upload a spreadsheet of customer card numbers to a personal cloud drive. Which tool BEST blocks this?
    - **[x] DLP (data loss prevention)**  - [ ] Antivirus  - [ ] NetFlow  - [ ] An SNMP trap
    - *DLP inspects content in use, in motion and at rest for patterns (card numbers, PII) and blocks or alerts. Antivirus looks for malware. NetFlow lacks content. SNMP is device monitoring.*
    - @4.4.dlp
13. A help desk PC shows a popup saying a file matching a known trojan signature was quarantined on the local disk. Which tool did this?
    - **[x] Antivirus**  - [ ] DLP  - [ ] A SIEM  - [ ] File integrity monitoring
    - *Antivirus detects malware mainly by signature, plus some heuristics, and quarantines the file on the host. File integrity monitoring is tempting because it watches files, but it alerts on changes to monitored files and does not identify or quarantine malware. Hook: AV knows the bad guys by face.*
    - @4.4.av
14. A tool probes a web server and reports outdated OpenSSL and weak cipher suites, each mapped to a CVE and CVSS score. Which tool produced this?
    - **[x] A vulnerability scanner**  - [ ] A SIEM  - [ ] DLP  - [ ] Antivirus
    - *Vulnerability scanners probe hosts for known flaws, missing patches and weak configurations, and map results to CVEs and CVSS. A SIEM is tempting because it often displays these findings, but it only ingests scanner output; it does not probe hosts itself. Hook: the scanner finds, the SIEM collects.*
    - @4.4.vscan
15. Each month the SOC manager sends leadership a summary of incidents, top alert types and mean time to respond. Which monitoring activity is this?
    - **[x] Reporting**  - [ ] Log aggregation  - [ ] Alerting  - [ ] Archiving
    - *Reporting turns monitoring data into summaries and metrics for decisions and compliance. Log aggregation is tempting because the figures come from centralized logs, but aggregation is the collection step, not producing management summaries. Hook: aggregate in, report out.*
    - @4.4.act
16. Events from 200 servers arrive in different formats and time zones, so a single attack shows up as unrelated entries hours apart. Which SIEM function addresses this?
    - **[x] Log aggregation**  - [ ] Alert tuning  - [ ] Archiving  - [ ] Correlation rules
    - *Log aggregation collects logs centrally and parses them into a common format with synchronized time stamps, so events line up. Correlation rules are tempting, but they depend on normalized, time-aligned data and cannot link events still in mismatched formats and zones. Hook: normalize before you correlate.*
    - @4.4.act
17. After a malware cleanup on a quarantined laptop, how should the SOC BEST confirm remediation worked?
    - **[x] Rescan and monitor for repeat alerts before release**  - [ ] Release it once the cleanup ticket is closed  - [ ] Tune the rule that fired to stop repeat alerts  - [ ] Reimage it and release it with no further checks
    - *Validation confirms the threat is gone through rescans and monitoring before the system returns to the network. Closing the ticket is tempting, but it only records that work was done, not that it worked. Hook: validate, then release.*
    - @4.4.resp
18. A cloud team extends monitoring to load balancers, virtual networks and DNS, beyond its VMs. Which resource category is it adding?
    - **[x] Infrastructure**  - [ ] Applications  - [ ] Systems  - [ ] Endpoints
    - *Infrastructure covers network and platform components such as load balancers, routers, VPCs and DNS. Applications is tempting because these are cloud services, but that category means software and its logs, not the underlying platform. Hook: systems = hosts, applications = software, infrastructure = the plumbing.*
    - @4.4.res
19. Why does 4.4 list vulnerability scanning as an ongoing MONITORING activity rather than a one-time test?
    - **[x] New CVEs and configuration drift appear constantly**  - [ ] Scans supply the log data that the SIEM correlates  - [ ] Continuous scans block exploits as they occur  - [ ] Auditors require scans to be run at least daily
    - *Scanning is continuous because new vulnerabilities are published and configurations drift all the time, so a one-time result goes stale. Feeding the SIEM is tempting because results can be ingested, but that is a side benefit, not the reason scanning is repeated. Hook: today's clean scan is tomorrow's finding.*
    - @4.4.act
20. A new DLP rule blocks every email containing the word "account", stopping much of finance's work. What is the BEST action?
    - **[x] Tune it to match validated account number patterns**  - [ ] Switch the rule to monitor-only mode permanently  - [ ] Exempt the finance team from the DLP policy  - [ ] Archive blocked messages for weekly manual release
    - *Tuning refines DLP patterns, for example to real account numbers with checksum validation, cutting false positives while keeping protection. Monitor-only is tempting because it ends the disruption, but it permanently removes blocking for genuinely sensitive data. Hook: fix the rule, not the protection.*
    - @4.4.tune
21. A switch is managed with SNMPv2c and the community string "public". What is the BEST change?
    - **[x] Migrate to SNMPv3 with authentication and encryption**  - [ ] Set a long random community string on SNMPv2c  - [ ] Restrict SNMPv2c to a read-only community string  - [ ] Move SNMP polling to TCP 161 for reliability
    - *SNMPv3 adds user authentication and encryption, which v1 and v2c lack. A long random community string is tempting, but v2c still sends it in clear text, so anyone sniffing the network can capture it. Hook: v3 is the only secure SNMP.*
    - @4.4.snmp

### Key facts
- **Monitor systems, applications, infrastructure. Activities: log aggregation, alerting, scanning, reporting, archiving, alert response (quarantine, alert tuning, validation).**
- **Tools: SCAP, benchmarks, agent vs agentless, SIEM, antivirus, DLP, SNMP traps (UDP 162), NetFlow, vulnerability scanners.**
22. PBQ 4.4 - Pick the tool. For each need, choose the BEST tool.
    - [p] Link a VPN login, a DC privilege change and a firewall allow into one timeline :: A SIEM · B NetFlow · C DLP · D SCAP · E Antivirus · F Vulnerability scanner = a
    - [p] See which internal hosts sent the most bytes to which external IPs, without payloads :: A SIEM · B NetFlow · C DLP · D SCAP · E Antivirus · F Vulnerability scanner = b
    - [p] Stop a spreadsheet of national insurance numbers leaving as an email attachment :: A SIEM · B NetFlow · C DLP · D SCAP · E Antivirus · F Vulnerability scanner = c
    - [p] Check 300 hosts against an XCCDF checklist and export results other tools can read :: A SIEM · B NetFlow · C DLP · D SCAP · E Antivirus · F Vulnerability scanner = d
    - [p] A downloaded file matching a known signature is moved to a protected folder :: A SIEM · B NetFlow · C DLP · D SCAP · E Antivirus · F Vulnerability scanner = e
    - [p] Find which hosts still run an OpenSSL version with a published CVE :: A SIEM · B NetFlow · C DLP · D SCAP · E Antivirus · F Vulnerability scanner = f
    - [p] A router reports a fan failure to the management station without being asked :: A SNMP trap · B SNMP poll · C NetFlow · D Syslog archive = a
    - *SIEM correlates events across sources, NetFlow gives conversation metadata, DLP controls sensitive content, SCAP standardizes compliance checking, antivirus quarantines known malware and scanners find known flaws. For the router, a trap is device-initiated; a poll is tempting but that is the manager asking. Hook: who talks (NetFlow), what is said (DLP), what is wrong (scanner), what it all means (SIEM).*
    - @4.4.tool

## Test 19 - 4.5 Enterprise Capabilities: Firewall, IDS/IPS, Web + DNS Filter, OS Security, Email, EDR (25 Q)

1. A firewall ACL has these rules in order: 1) deny any any, 2) allow TCP 443 to 198.51.100.10. HTTPS to the web server fails. Why?
   - **[x] Rules are processed top-down and the deny-all matches first**  - [ ] HTTPS uses UDP, not TCP  - [ ] The allow rule needs port 80 as well  - [ ] Firewalls process the most specific rule first
   - *Firewall rules/access lists are evaluated top to bottom and the first match wins, so specific allows go above the implicit or explicit deny at the bottom. HTTPS is TCP 443 (HTTP/3 uses UDP but that is not the issue). Port 80 is not needed for HTTPS. Most firewalls do not reorder by specificity.*
   - @4.5.rules
2. An online shop's storefront and inbound SMTP relay must be reachable from the internet. If either is breached, the attacker must not reach the HR network directly. Where should they be placed?
   - **[x] A screened subnet between external and internal firewalls**  - [ ] The internal LAN behind a next-generation firewall  - [ ] A separate VLAN on the internal core switch  - [ ] A host-based firewall on each server in the LAN
   - *A screened subnet (DMZ) isolates public-facing services between firewall layers, so a compromise there does not give direct access to internal networks. A VLAN on the internal switch is tempting, but it still sits inside the trusted network rather than in a filtered zone between firewalls. Hook: public services live in the moat, not the castle.*
   - @4.5.dmz
3. A network IPS drops traffic matching the byte pattern of a known exploit, and separately alerts when a host suddenly sends 10x its usual volume. Which TWO detection methods are shown? (Select 2)
   - **[x] Signature-based**  - **[x] Anomaly/trend-based**  - [ ] Reputation-based  - [ ] Heuristic sandboxing
   - *Signature detection matches known patterns, while anomaly or trend analysis flags deviation from a baseline. Reputation-based is tempting, but it judges sources or domains by their history, not a host's traffic volume against its baseline. Hook: signatures know the face, anomalies notice odd behaviour.*
   - @4.5.ids
4. A firm with many remote laptops wants web filtering enforced even when users browse from home without the VPN. Which approach fits BEST?
   - **[x] Agent-based web filtering**  - [ ] A centralized proxy  - [ ] DNS filtering at the office resolver  - [ ] Content categorization on the edge firewall
   - *Agent-based filtering runs on each device and enforces policy wherever it connects. A centralized proxy is tempting as the classic filter, but it only sees traffic routed through it, which home browsing without the VPN is not. Hook: the agent goes where the laptop goes.*
   - @4.5.web
5. A school must block thousands of gambling and adult sites, including newly launched ones, without staff maintaining URL lists. Which web filter feature is BEST?
   - **[x] Content categorization with block rules**  - [ ] Reputation-based scoring of domains  - [ ] URL scanning against threat lists  - [ ] DNS filtering of malicious domains
   - *Content categorization uses vendor databases that label sites by type, so block rules apply to whole categories. Reputation scoring is tempting, but it rates risk and trustworthiness, not subject matter, so a reputable gambling site would pass. Hook: category = what it is, reputation = how trustworthy.*
   - @4.5.web
6. A user clicks a link to a domain registered yesterday that no vendor has classified yet. Which web filter feature is MOST likely to block it?
   - **[x] Reputation scoring of the domain**  - [ ] Content categorization  - [ ] A block rule for the phishing category  - [ ] DNS filtering of known malicious domains
   - *Reputation scoring weighs domain age, history and threat data, so newly registered, unrated domains are treated as high risk. A category block is tempting, but an unclassified domain has no category yet to match. Hook: new and unknown = low reputation.*
   - @4.5.web
7. Malware on several PCs contacts its command server by generating random domain names and resolving them. Which control BEST blocks this early for every device on the network?
   - **[x] DNS filtering at the internal resolver**  - [ ] Agent-based web filtering on laptops  - [ ] URL scanning on the web proxy  - [ ] An email security gateway
   - *DNS filtering refuses to resolve malicious or suspicious domains, so the connection never starts, and it covers every device using the resolver. URL scanning is tempting, but it only sees web traffic sent through the proxy, and C2 traffic often uses other ports or bypasses it. Hook: no name, no call home.*
   - @4.5.dns
8. A Windows admin must stop USB storage and enforce a 15-minute screen lock on 3,000 domain-joined PCs. Which tool is BEST?
   - **[x] Group Policy**  - [ ] SELinux  - [ ] NetFlow  - [ ] A web proxy
   - *Group Policy (GPOs) centrally pushes security settings to Windows machines in Active Directory. SELinux is Linux. NetFlow is traffic data. A proxy filters web traffic.*
   - @4.5.os
9. A web server is compromised, but the attacker's process cannot read the password hash file even though it runs as a privileged service account. Which feature MOST likely stopped it?
   - **[x] SELinux enforcing mandatory access control**  - [ ] Group Policy restricting file permissions  - [ ] File integrity monitoring on the hash file  - [ ] Discretionary ACLs set by the file owner
   - *SELinux enforces mandatory access control policies that confine each process by label, so even a privileged service cannot read files outside its policy. Group Policy is tempting for restricting access, but it manages Windows settings and file permissions that a privileged account can override. Hook: MAC limits even root.*
   - @4.5.os
10. An admin is replacing insecure protocols. Which pairing of secure protocol and default port is correct?
    - **[x] SFTP on TCP 22**  - [ ] FTPS on TCP 22  - [ ] LDAPS on TCP 389  - [ ] SMTPS on TCP 25
    - *SFTP runs over SSH on TCP 22. FTPS is tempting because it is also secure file transfer, but it is FTP over TLS on 990 (implicit) or 21 with explicit TLS, not 22; LDAPS uses 636 and SMTPS 465. Hook: SFTP rides SSH.*
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
14. Which control BEST removes spam, malicious attachments and phishing links before messages reach user mailboxes?
    - **[x] A secure email gateway**  - [ ] A DMARC reject policy  - [ ] DNS filtering  - [ ] Endpoint DLP
    - *A secure email gateway sits in the mail flow and filters spam, malware, attachments and URLs before delivery. A DMARC reject policy is tempting, but it only handles messages spoofing domains that publish DMARC, not malware or phishing sent from other domains. Hook: DMARC checks the sender's claim, the gateway checks the contents.*
    - @4.5.gate
15. An attacker replaces a system DLL on a payment server with a trojanized copy that no antivirus signature detects. Which control would MOST quickly detect the change?
    - **[x] File integrity monitoring (FIM)**  - [ ] Signature-based antivirus  - [ ] Host-based DLP  - [ ] A credentialed vulnerability scan
    - *FIM hashes critical files and alerts when they change unexpectedly, whether or not the malware is known. Antivirus is tempting, but no signature matches this file, so it would miss the change. Hook: FIM does not care what it is, only that it changed.*
    - @4.5.fim
16. A contractor plugs a personal laptop into a meeting-room wall port. It must be placed in a quarantine VLAN until its patch level and antivirus status are checked. Which capability does this?
    - **[x] NAC**  - [ ] EDR  - [ ] Port security with MAC filtering  - [ ] Agent-based web filtering
    - *Network access control checks identity and device posture before granting access and can quarantine non-compliant devices. Port security is tempting because it acts on the switch port, but it only allows or blocks MAC addresses and cannot assess patch or antivirus status. Hook: NAC asks how healthy you are, not just who you are.*
    - @4.5.nac
17. The SOC wants to spot ransomware-like behaviour on laptops, remotely cut a host off the network and roll back file changes. Which tool fits BEST?
    - **[x] EDR**  - [ ] Signature-based antivirus  - [ ] NAC  - [ ] UBA
    - *EDR records endpoint behaviour, detects suspicious activity beyond signatures and lets responders isolate and remediate hosts. NAC is tempting because it can quarantine, but it controls network admission and has no behavioural detection or rollback on the endpoint. Hook: EDR sees, isolates and fixes on the host.*
    - @4.5.edr
18. A SOC has separate consoles for laptop agents, the mail filter, firewall sensors and the cloud identity provider. Analysts want one detection and response product that correlates these signals into a single incident timeline. What should it choose?
    - **[x] XDR**  - [ ] EDR  - [ ] UBA  - [ ] NAC
    - *XDR extends EDR-style detection and response across endpoints, email, network and identity with automated correlation. EDR is tempting, but it covers only endpoint telemetry and leaves the other consoles separate. Hook: X = across everything.*
    - @4.5.edr
19. A finance user who normally works 9-to-5 from Leeds downloads 5,000 files at 02:00 from a new country. Which capability is BEST suited to flag this?
    - **[x] UBA/UEBA**  - [ ] DLP  - [ ] EDR  - [ ] Signature-based IDS
    - *User behaviour analytics baselines each user's normal activity and flags deviations in time, location and volume, catching compromised accounts and insiders. DLP is tempting because files are involved, but it inspects content for sensitive patterns, not whether the user's behaviour is unusual. Hook: UBA knows the user's habits.*
    - @4.5.uba
20. After a signature update, an inline IPS starts blocking a legitimate business application. What is the BEST action?
    - **[x] Tune or add a narrow exception for that signature**  - [ ] Switch the IPS to detection-only mode  - [ ] Roll back to the previous signature set  - [ ] Allow all traffic from the application server
    - *Investigating and tuning, or adding a narrowly scoped exception, fixes the false positive while keeping all other protection. Rolling back the update is tempting as a quick fix, but it also discards protection against the new threats in that update. Hook: scalpel, not sledgehammer.*
    - @4.5.ids
21. Two data centres must protect all traffic between them, for every application, with one control at the network layer. Which is BEST?
    - **[x] An IPsec site-to-site tunnel**  - [ ] TLS on each application  - [ ] An SSH tunnel per service  - [ ] A dedicated MPLS circuit
    - *IPsec operates at layer 3 and protects all traffic between the sites in one tunnel. TLS is tempting because it is strong encryption, but it protects one application session at a time and must be configured per app; MPLS is private routing, not encryption. Hook: IPsec protects the pipe, TLS protects the conversation.*
    - @4.5.proto
22. Network DLP on the egress points is in place, but staff copy data to USB drives at their desks. What should be added?
    - **[x] Endpoint DLP agents that control removable media**  - [ ] More network DLP sensors  - [ ] A stricter DMARC policy  - [ ] A web content category block
    - *DLP locations: network (data in motion), endpoint (data in use, USB, print, clipboard) and storage (data at rest). USB copying never crosses the network. DMARC and web categories are unrelated.*
    - @4.5.dlp
23. A firewall admin is told to "allow DNS" for internal resolvers to reach the internet. Which port and protocol selection is MOST accurate?
    - **[x] UDP and TCP 53**  - [ ] TCP 443 only  - [ ] UDP 161 only  - [ ] TCP 25 only
    - *DNS uses UDP 53 for most queries and TCP 53 for large responses and zone transfers (DNS over HTTPS uses 443, but that is a separate choice). 161 is SNMP. 25 is SMTP.*
    - @4.5.ports
24. A company sends all staff web traffic through one appliance in its data centre, which checks every requested address against threat lists before fetching the page. Which TWO web filter features are shown? (Select 2)
    - **[x] Centralized proxy**  - **[x] URL scanning**  - [ ] Agent-based filtering  - [ ] Content categorization
    - *A centralized proxy sits in the traffic path for everyone routed through it, and URL scanning inspects each requested address against threat data. Content categorization is tempting, but it labels sites by subject such as gambling, not by matching against threat lists. Note the objectives expand URL as Universal Resource Locator.*
    - @4.5.web

### Key facts
- **Firewall: rules top-down, first match, implicit deny; access lists; ports/protocols; screened subnet. IDS/IPS: signatures, trends/anomaly.**
- **Web filter: agent-based, centralized proxy, URL scanning, content categorization, block rules, reputation. DNS filtering.**
- **OS security: Group Policy (Windows), SELinux (Linux MAC). Secure protocols: choose protocol, port, transport.**
- **Email: SPF (who may send), DKIM (signature), DMARC (policy + reports), gateway. Also FIM, DLP, NAC, EDR/XDR, UBA.**
25. PBQ 4.5 - Firewall rules. Build rules for a DMZ web server at 203.0.113.10 and an internal DB at 192.0.2.20. Pick the action for each rule.
    - [p] Internet -> 203.0.113.10 TCP 443 :: A Allow · B Deny = a
    - [p] Internet -> 192.0.2.20 TCP 1433 :: A Allow · B Deny = b
    - [p] 203.0.113.10 -> 192.0.2.20 TCP 1433 :: A Allow · B Deny = a
    - [p] Internet -> 203.0.113.10 TCP 23 :: A Allow · B Deny = b
    - [p] Last rule in the list :: A Allow any any · B Deny any any = b
    - [p] Where should rule 1 sit relative to the last rule :: A Above it · B Below it = a
    - *Allow only what is needed: public HTTPS to the DMZ web server, and the web server to the DB on SQL Server's port. Never expose the DB to the internet. Telnet (23) is insecure and unneeded. End with deny-all (implicit deny) and keep allows above it because the first match wins.*
    - @4.5.rules

## Test 20 - 4.6 IAM I: Provisioning, Identity Proofing, Federation, SSO, Access Control Models (24 Q)

1. A new nurse starts Monday. HR enters her record and, overnight, accounts are created in the directory, EHR and email with the "Ward Nurse" role. What is this process?
   - **[x] Provisioning**  - [ ] Identity proofing  - [ ] Attestation  - [ ] Federation
   - *Provisioning creates accounts and grants access when someone joins, ideally automated from HR as the source of truth. Identity proofing is tempting because it also happens at onboarding, but it verifies who the person is before credentials are issued, not the creation of accounts. Hook: proof the person, provision the accounts.*
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
6. Employees of a manufacturer sign in once with company credentials and then reach a partner's supplier portal without a separate partner account. What makes this possible?
   - **[x] Federation between the two organizations**  - [ ] Kerberos SSO within the domain  - [ ] LDAP directory synchronization  - [ ] Role-based access control
   - *Federation creates trust so the partner's service provider accepts assertions from the manufacturer's identity provider. Kerberos SSO is tempting because it gives single sign-on, but it works within a domain or realm, not across separate organizations' web portals. Hook: SSO inside, federation across.*
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
    - **[x] Fewer passwords to reuse and one place to disable access**  - [ ] Delegated API access without sharing user passwords  - [ ] A breached SSO login exposes only one application  - [ ] Identity documents are verified before account creation
    - *SSO reduces password fatigue and reuse and centralizes control, so disabling one account removes access everywhere. Delegated API access is tempting because OAuth is often used alongside SSO, but that is authorization for apps, not the core SSO benefit. Hook: one key, so guard it with MFA.*
    - @4.6.sso
11. A company's new HR SaaS supports SAML and OIDC but its old intranet only supports LDAP. Which IAM concern does this highlight?
    - **[x] Interoperability between identity systems and protocols**  - [ ] Attestation  - [ ] Time-of-day restrictions  - [ ] Identity proofing
    - *Interoperability = whether different systems and standards can work together for authentication and authorization; you may need connectors or an IdP that bridges protocols. The others are separate IAM topics.*
    - @4.6.interop
12. A call centre wants stolen agent credentials to be useless outside the 08:00-18:00 shift pattern. Which control is BEST?
    - **[x] Time-of-day restrictions**  - [ ] Just-in-time permissions  - [ ] Password expiration  - [ ] Ephemeral credentials
    - *Time-of-day restrictions limit when accounts can authenticate, shrinking the window for misuse of stolen credentials. Just-in-time permissions are tempting, but they grant temporary privilege elevation on request, not a fixed daily login window for standard users. Hook: the account sleeps when the shift ends.*
    - @4.6.tod
13. A new analyst asks for domain admin "just in case" she needs it. Her job only needs read access to reports. What principle should guide the decision?
    - **[x] Least privilege**  - [ ] Separation of duties  - [ ] Implicit trust  - [ ] Defense in depth
    - *Least privilege = give only the access needed to do the job, nothing more. Separation of duties splits critical tasks between people. Implicit trust is what zero trust removes. Defense in depth layers controls.*
    - @4.6.lp
14. A large hospital has 400 job titles and thousands of staff moving between wards. Which access model is EASIEST to manage at scale while limiting rights?
    - **[x] Role-based access control**  - [ ] Discretionary access control by each file owner  - [ ] Individual permissions per user  - [ ] Mandatory access control with labels on every record
    - *RBAC maps permissions to roles, so moving staff means changing role membership, not hundreds of permissions. DAC and per-user rights do not scale and cause creep. MAC is rigid and suited to classified environments.*
    - @4.6.ac
15. A cloud provider wants to grant access to a storage bucket only when the user's project tag matches the bucket's project tag and the request comes from the corporate network. Which model fits BEST?
    - **[x] Attribute-based access control (ABAC)**  - [ ] Discretionary access control  - [ ] Mandatory access control  - [ ] Role-based access control
    - *ABAC evaluates attributes of subject, object and environment in policies (if tag matches AND network = corporate). RBAC uses only roles. MAC uses labels. DAC uses owner choice.*
    - @4.6.ac
16. An audit finds 40 active accounts belonging to people who left last year. What is the BEST long-term fix?
    - **[x] HR-driven automated de-provisioning plus access reviews**  - [ ] A one-time cleanup of the 40 orphaned accounts  - [ ] Password expiry so unused accounts lock themselves  - [ ] Time-of-day restrictions on all user accounts
    - *Automating removal from HR leaver events, with periodic attestation to catch stragglers, fixes the root cause. A one-time cleanup is tempting because it removes the current risk, but the manual process will keep creating new orphaned accounts. Hook: fix the process, not just the list.*
    - @4.6.deprov
17. A new SaaS vendor offers to sync passwords from the on-premises directory. The security team prefers SAML federation. Why is federation BETTER?
    - **[x] The SaaS app never receives passwords, only signed assertions**  - [ ] SAML encrypts the synced password hashes in transit  - [ ] Federation grants delegated API access through tokens  - [ ] The SaaS app can query the directory over LDAPS
    - *With federation the service provider trusts signed assertions from the IdP and never stores or sees the password. Encrypting synced hashes is tempting, but SAML does not sync passwords at all, and synced hashes would still live at another provider. Hook: assertions travel, passwords stay home.*
    - @4.6.fed
18. A help desk can reset any user's password, including executives', without approval or extra verification. What implication is MOST concerning?
    - **[x] It creates an account takeover path to high-value accounts**  - [ ] It causes privilege creep for help desk staff  - [ ] It breaks least privilege for the executives' accounts  - [ ] It weakens the password complexity policy for executives
    - *Broad, unverified reset rights let a rogue or socially engineered help desk agent take over executive accounts, so resets should be scoped, verified and logged. Privilege creep is tempting, but creep is gradual accumulation through role changes, not a deliberately broad assignment. Hook: whoever can reset can impersonate.*
    - @4.6.perm
19. A user logs in once to Windows and then reaches file shares and intranet apps without re-entering credentials, using tickets from a domain controller. What is this?
    - **[x] Single sign-on with Kerberos**  - [ ] Federation with OAuth  - [ ] Discretionary access control  - [ ] Attestation
    - *Inside an Active Directory domain, Kerberos gives SSO: the KDC issues a ticket-granting ticket, then service tickets. Federation spans organizations. DAC and attestation are other topics.*
    - @4.6.sso
20. Two firms merge. Staff in each need access to some of the other's apps quickly, while each keeps its own directory for now. What is the BEST approach?
    - **[x] Federation trust between the two IdPs**  - [ ] Password sync between both directories  - [ ] Duplicate accounts created in each directory  - [ ] Shared role groups mirrored by hand
    - *Federation lets each IdP keep authenticating its own users while the other side trusts their assertions. Duplicate accounts are tempting as a quick fix, but they create orphaned accounts and sync gaps. Hook: trust, do not copy.*
    - @4.6.fed
21. A user's OAuth access token for a reporting API is stolen. Which design choice MOST limits the damage?
    - **[x] Short-lived tokens with narrow scopes**  - [ ] Signing tokens with a stronger algorithm  - [ ] Long-lived refresh tokens for convenience  - [ ] Encrypting stored tokens on the server
    - *Short expiry and narrow scopes mean a stolen token works briefly and only for limited actions. Stronger signing is tempting, but it prevents forgery, not misuse of a genuine stolen token. Hook: small keys that expire fast.*
    - @4.6.oauth
22. An auditor asks how a contractor obtained access to the payments system. The company produces records showing who asked for the access, who agreed to it and when it was granted. Which provisioning practice does this show?
    - **[x] A documented access request and approval workflow**  - [ ] Attestation of the contractor's access  - [ ] Identity proofing of the contractor  - [ ] Periodic access review
    - *Good provisioning records who requested access, who approved it and what was granted, making access justified and auditable. Attestation is tempting because a manager signs off, but attestation is a periodic recertification of existing access, not the original approval. Hook: approval at the door, attestation on the rounds.*
    - @4.6.prov
23. A shared "scanner" service account has write rights to every file share. Which change BEST reflects least privilege?
    - **[x] Limit it to the scan folder and deny interactive logon**  - [ ] Vault its password and rotate it monthly  - [ ] Convert it to an ephemeral credential  - [ ] Apply time-of-day restrictions to it
    - *Least privilege limits the account to the one folder it needs, and blocking interactive logon stops it being used as a user account. Vaulting and rotation is tempting good practice, but it protects the credential without reducing what the account can do if misused. Hook: shrink the rights, not just the secret's lifespan.*
    - @4.6.lp

### Key facts
- **Lifecycle: provisioning, de-provisioning, permission assignments (watch for creep), identity proofing, attestation.**
- **Federation (IdP/SP trust); SSO via LDAP, OAuth (delegated authorization, tokens), SAML (XML assertions); interoperability.**
- **Access control: mandatory (labels), discretionary (owner), role-based, rule-based, attribute-based, time-of-day, least privilege.**
24. PBQ 4.6 - Access control models. Match each scenario to the model.
    - [p] Military system: users with "Secret" clearance cannot read "Top Secret" labelled files; only admins set labels :: A Mandatory · B Discretionary · C Role-based · D Rule-based · E Attribute-based = a
    - [p] A file owner shares her folder with two colleagues of her choice :: A Mandatory · B Discretionary · C Role-based · D Rule-based · E Attribute-based = b
    - [p] Everyone in the "Accounts Payable" group gets the same finance app rights :: A Mandatory · B Discretionary · C Role-based · D Rule-based · E Attribute-based = c
    - [p] A firewall denies all traffic from 203.0.113.0/24, for every user :: A Mandatory · B Discretionary · C Role-based · D Rule-based · E Attribute-based = d
    - [p] Access allowed if department=Research AND device=managed AND location=UK :: A Mandatory · B Discretionary · C Role-based · D Rule-based · E Attribute-based = e
    - *MAC = labels and clearances set centrally, users cannot change. DAC = owner decides. RBAC = rights by job role. Rule-based = system-wide rules applied to all (ACLs, firewalls). ABAC = combine many attributes of user, resource and context. Hook: Mandatory = the military, Discretionary = the owner, Role = the job, Rule = the list, Attribute = the checklist.*
    - @4.6.ac

## Test 21 - 4.6 IAM II: MFA, Passwords, Passwordless, Privileged Access (23 Q)

1. A bank requires a password and the answer to a security question for online login. A regulator says this is not MFA. Why?
   - **[x] Both are something you know**  - [ ] Neither is phishing-resistant  - [ ] The question is something you are  - [ ] MFA requires a hardware token
   - *MFA needs factors from different categories, and a password and a security answer are both knowledge. Lack of phishing resistance is tempting because it is a real weakness, but MFA is defined by factor categories, not phishing resistance. Hook: two knows still equal one factor.*
   - @4.6.factor
2. A data centre wants staff to enter with a palm vein scan. Which biometric metric should the team watch so that impostors are NOT let in?
   - **[x] False acceptance rate (FAR)**  - [ ] False rejection rate (FRR)  - [ ] Crossover error rate only as a cost figure  - [ ] Mean time to repair
   - *FAR = impostors wrongly accepted (a security failure). FRR = genuine users wrongly rejected (a usability failure). The crossover error rate (CER), where they meet, compares systems; lower is better. MTTR is resilience. Hook: FAR = fraud accepted.*
   - @4.6.bio
3. A field engineer gets a 6-digit code that changes every 30 seconds from an app on her phone. What is this?
   - **[x] A soft token using TOTP**  - [ ] A hard token using a smart card chip  - [ ] Something you are  - [ ] An HOTP code that never expires
   - *Software (soft) token = an app generating time-based one-time passwords (TOTP). Hard tokens are dedicated devices (key fobs). HOTP is counter-based and stays valid until used, not time-based. A phone app is something you have.*
   - @4.6.token
4. An executive has been targeted by SIM swapping. Which second factor is BEST for him?
   - **[x] A FIDO2 hardware security key**  - [ ] SMS one-time codes  - [ ] TOTP codes in a phone app  - [ ] Push approval to his phone
   - *A FIDO2 key is not tied to a phone number and is phishing-resistant, so SIM swapping cannot capture it. TOTP is tempting because a SIM swap does not steal the app seed, but its codes can still be phished and relayed, so it is weaker than a key. Hook: no phone number, nothing to swap.*
   - @4.6.key
5. Staff receive repeated MFA push prompts at night until someone taps Approve. Which mitigation is BEST?
   - **[x] Number matching in the push prompt**  - [ ] Shorter push approval timeouts  - [ ] Switching the second factor to SMS  - [ ] Stronger password complexity rules
   - *Number matching makes the user enter the code shown on the login screen, so a blind approval cannot succeed. Shorter timeouts are tempting, but the attacker can simply keep sending new prompts. Hook: match the number, beat the bombing.*
   - @4.6.mfa
6. A policy requires 8-character complex passwords changed every 30 days, and users now write passwords on sticky notes. Which change BEST aligns with current NIST guidance?
   - **[x] Long passphrases, breach screening, change only on compromise**  - [ ] Longer complex passwords with expiry every 60 days  - [ ] Keep 8 characters but add a password history of 24  - [ ] More required symbols and a minimum age of one day
   - *NIST SP 800-63B favours length, screening against breached passwords and changing only on evidence of compromise, because forced expiry drives weak patterns and notes. Longer passwords with 60-day expiry is tempting as a compromise, but periodic forced change still causes the same predictable behaviour. Note the exam still lists expiration and age as settings to know.*
   - @4.6.pw
7. An audit shows staff cycle through several throwaway passwords in a few minutes so they can return to the one they had before. Which TWO settings stop this? (Select 2)
   - **[x] Password history (prevent reuse of the last N passwords)**  - **[x] Minimum password age**  - [ ] Maximum password length  - [ ] Account lockout threshold
   - *History blocks reuse; minimum age stops users cycling through history in one sitting. Max length does not stop reuse. Lockout limits guessing.*
   - @4.6.pw
8. A team must manage 300 unique site passwords, some shared between colleagues. What is the BEST approach?
   - **[x] An enterprise password manager with MFA on the vault**  - [ ] Browser-saved passwords synced to work profiles  - [ ] SSO federation to all 300 external sites  - [ ] An encrypted spreadsheet on a restricted share
   - *An enterprise password manager generates and stores unique, strong passwords in an encrypted vault with controlled sharing and audit. An encrypted spreadsheet is tempting because it is protected, but one shared decryption password exposes everything, with no per-user access control or audit. Hook: vault, not spreadsheet.*
   - @4.6.pwmgr
9. Which login method is passwordless?
    - **[x] Windows Hello for Business with a local PIN**  - [ ] A password plus a TOTP authenticator code  - [ ] Kerberos SSO after a domain logon  - [ ] A password manager autofilling a passphrase
    - *Windows Hello for Business uses a device-bound private key unlocked locally by biometrics or a PIN that never leaves the device, so no shared secret is sent to the server. The local PIN is tempting to dismiss as a password, but it only unlocks the key on that device and is useless elsewhere. Hook: no shared secret on the wire = passwordless.*
    - @4.6.pwless
10. Why are passkeys (FIDO2) highly resistant to phishing?
    - **[x] The key signs only for the registered site's origin**  - [ ] The one-time code expires within 30 seconds  - [ ] The private key is synced to the server for checks  - [ ] Biometric matching is performed on the server
    - *FIDO2/WebAuthn binds each key pair to the real site's origin, so a lookalike domain cannot obtain a valid signature. Short code lifetime is tempting, but that describes TOTP, whose codes can still be relayed in real time. Hook: wrong domain, no signature.*
    - @4.6.pwless
11. A sysadmin needs domain admin for a two-hour change window. Under PAM, how should this work?
    - **[x] Just-in-time elevation, approved, logged and auto-removed**  - [ ] A separate admin account with standing rights  - [ ] Checking out the shared domain admin password  - [ ] Ephemeral API keys issued for the window
    - *Just-in-time permissions grant privilege only when approved and only for the window, removing standing privilege an attacker could steal. A separate admin account is tempting as best practice, but with standing rights it still holds privilege around the clock. Hook: privilege on demand, gone when done.*
    - @4.6.jit
12. Root passwords for 200 Linux servers are stored in a spreadsheet. Which PAM capability BEST fixes this?
    - **[x] Password vaulting with checkout and rotation**  - [ ] Just-in-time elevation for root  - [ ] Ephemeral credentials for each admin  - [ ] A personal password manager per admin
    - *Password vaulting stores privileged credentials centrally, logs checkouts and rotates them after use. A personal password manager is tempting, but each admin would hold copies of static shared secrets without central rotation or session control. Hook: vault, check out, rotate.*
    - @4.6.vault
13. A CI pipeline needs cloud credentials to deploy. Which approach BEST reduces risk if the pipeline is compromised?
    - **[x] Ephemeral credentials issued per job**  - [ ] A vaulted access key rotated monthly  - [ ] A scoped key stored as a pipeline secret  - [ ] Just-in-time approval for each deploy
    - *Ephemeral credentials are created on demand and expire within minutes, so a stolen one is soon useless. A vaulted key rotated monthly is tempting, but a thief still has weeks of valid access. Hook: minutes, not months.*
    - @4.6.ephem
14. An admin uses one domain admin account all day, including for email and web browsing. What is the BEST change?
    - **[x] Separate daily and admin accounts**  - [ ] Add MFA to the admin account  - [ ] Vault and rotate its password daily  - [ ] Apply time-of-day restrictions
    - *Privileged accounts should be used only for privileged tasks, so a standard account handles email and browsing. MFA is tempting, but malware from a phishing email runs with the logged-in admin's rights regardless of how he authenticated. Hook: do not read email as god.*
    - @4.6.pam
15. A retailer's VPN accepts a password and a phone push, but only when the phone's GPS reading matches the login's country. Which factor does the GPS condition add?
    - **[x] Somewhere you are**  - [ ] Something you have  - [ ] Something you are  - [ ] Something you know
    - *GPS or IP geolocation is somewhere you are, used as an extra condition. Something you have is tempting because the phone supplies the reading, but the phone is already the have factor and its position is a separate attribute. Hook: have = the device, somewhere = where it is.*
    - @4.6.factor
16. A company issues employees smart cards with certificates for laptop login. Which implementation is this, and what is the second factor usually added?
    - **[x] A hard token (smart card); a PIN to unlock it**  - [ ] A soft token; a fingerprint  - [ ] A biometric; a password  - [ ] Somewhere you are; a GPS fix
    - *Smart cards (like PIV/CAC) are hard tokens holding a private key; a PIN (know) unlocks the card (have), making MFA. The other pairings misclassify the card.*
    - @4.6.token
17. A lockout threshold of 3 attempts lets an attacker lock out every user by deliberately guessing wrong. What is the BEST balance?
    - **[x] Moderate threshold with timed unlock, plus MFA and spray alerts**  - [ ] Threshold of one attempt with admin-only unlock  - [ ] Remove lockout and rely on complexity rules  - [ ] Higher threshold with permanent lockout on trigger
    - *A sensible threshold with an automatic unlock timer slows guessing without enabling mass denial of service, and MFA plus alerting catches spraying. Removing lockout is tempting to stop the denial of service, but it lets attackers guess freely. Hook: slow them down, do not lock everyone out.*
    - @4.6.pw
18. Which MFA implementation is the MOST phishing-resistant?
    - **[x] FIDO2 security key**  - [ ] SMS code  - [ ] TOTP authenticator code  - [ ] Push approval without number matching
    - *Security keys use origin-bound public key crypto, so a phishing site cannot replay them. TOTP and SMS codes can be typed into a fake site and relayed. Plain push is vulnerable to fatigue.*
    - @4.6.key
19. A vendor support engineer needs to reach a production database once a month. What is the BEST PAM approach?
    - **[x] Brokered session with approval, vaulted credential and recording**  - [ ] A dedicated vendor account with a strong password  - [ ] Site-to-site VPN restricted to the database subnet  - [ ] A vendor account with MFA and quarterly attestation
    - *Brokering through a PAM gateway gives approved, time-bound sessions where the credential is never revealed and activity is recorded. An MFA-protected vendor account is tempting, but it is standing access that exists all month and is not recorded. Hook: rent the access, do not hand over the keys.*
    - @4.6.vault
20. Staff must complete MFA at every sign-in, which annoys people working on managed devices in the office. Which approach BEST keeps security while reducing friction?
    - **[x] Conditional access that steps up MFA on risk**  - [ ] Exempt the office IP range from MFA  - [ ] SSO so MFA is entered once per day  - [ ] Extend session tokens to 30 days
    - *Conditional or risk-based access weighs device, location and behaviour, and asks for more factors only when risk rises. A blanket office-IP exemption is tempting, but anyone on that network, including an attacker inside, would skip MFA entirely. Hook: ask harder when it looks riskier.*
    - @1.2.zt
21. Which statement BEST describes a hard token compared with a soft token?
    - **[x] Hard is a dedicated device; soft is an app on a general device**  - [ ] Hard uses TOTP codes; soft uses HOTP counter codes  - [ ] Hard is something you have; soft is something you know  - [ ] Hard stores a private key; soft cannot generate OTPs
    - *A hard token is a dedicated physical device such as a key fob or smart card, while a soft token is an authenticator app on a phone or PC. Classifying a soft token as something you know is tempting, but both are something you have, and both can use TOTP or HOTP. Hook: hard = its own device, soft = an app.*
    - @4.6.token

### Key facts
- **Factors: know, have, are, somewhere you are. Implementations: biometrics (FAR, FRR, CER), hard/soft tokens (TOTP, HOTP), security keys (FIDO2).**
- **Passwords: length, complexity, reuse/history, expiration, age; password managers; passwordless (passkeys, Windows Hello).**
- **PAM: just-in-time permissions, password vaulting, ephemeral credentials.**
22. PBQ 4.6 - Factors. Classify each item.
   - [p] A pattern drawn to unlock a phone :: A Something you know · B Something you have · C Something you are · D Somewhere you are = a
   - [p] A smart card inserted into a reader :: A Something you know · B Something you have · C Something you are · D Somewhere you are = b
   - [p] Typing rhythm captured while a password is entered :: A Something you know · B Something you have · C Something you are · D Somewhere you are = c
   - [p] Login allowed only when the source IP resolves to the UK office :: A Something you know · B Something you have · C Something you are · D Somewhere you are = d
   - [p] A one-time code from an authenticator app :: A Something you know · B Something you have · C Something you are · D Somewhere you are = b
   - [p] A password plus a PIN counts as :: A Single factor · B Multifactor = a
   - *Know covers passwords, PINs and patterns; have covers smart cards, keys and phones with soft tokens; are covers physical and behavioural biometrics such as typing rhythm; somewhere covers GPS or IP location. Password plus PIN is tempting as MFA because there are two steps, but both are knowledge, so it is single factor. Hook: count categories, not steps.*
   - @4.6.factor

23. PBQ 4.6 - PAM toolkit. Pick the BEST tool for each need.
    - [p] A DBA's account joins an admin group after approval and is removed automatically at 17:00 :: A Just-in-time permissions · B Password vaulting · C Ephemeral credentials · D Separate admin account = a
    - [p] The shared firewall admin password is checked out, then changed after each use :: A Just-in-time permissions · B Password vaulting · C Ephemeral credentials · D Separate admin account = b
    - [p] A container receives a cloud token minted at start-up that lapses after 15 minutes :: A Just-in-time permissions · B Password vaulting · C Ephemeral credentials · D Separate admin account = c
    - [p] An attacker steals a vaulted password that has since been rotated. Its value is :: A Useless · B Valid until the next vault audit · C Valid only from the original host = a
    - *JIT grants time-limited elevation to an existing identity, vaulting secures and rotates existing privileged secrets, and ephemeral credentials are created on demand and expire quickly. Ephemeral is tempting for the DBA case because access is temporary, but the DBA's own account is being elevated, not issued a new short-lived credential. Hook: rotation makes stolen copies stale.*
    - @4.6.pam

## Test 22 - 4.7 + 4.8 + 4.9 Automation, Incident Response, Forensics, Investigation Data Sources (30 Q)

1. A company's onboarding script creates accounts, assigns groups by role and emails the manager, cutting setup from two days to ten minutes. Which TWO automation benefits are MOST clearly shown? (Select 2)
   - **[x] Efficiency/time saving**  - **[x] Enforcing consistent baselines for access**  - [ ] Removing all technical debt  - [ ] Eliminating any single point of failure
   - *4.7 benefits: efficiency, enforcing baselines, standard infrastructure configurations, scaling securely, employee retention, reaction time, workforce multiplier. Automation can add technical debt and become a single point of failure, so those are considerations, not benefits.*
   - @4.7.ben
2. A cloud team's pipeline automatically refuses any deployment whose template would make a storage bucket readable by anyone on the internet. Which automation use case is this?
   - **[x] Guard rails**  - [ ] Security groups  - [ ] Resource provisioning  - [ ] Enforcing baselines
   - *Guard rails are automated policy checks that stop an unsafe configuration before it is deployed while letting teams keep moving. Enforcing baselines is tempting, but it is a benefit of automation, not a use case, and it describes keeping settings consistent rather than blocking a risky deployment. Security groups control network traffic and resource provisioning creates resources. Hook: the barrier on a mountain road.*
   - @4.7.guard
3. When the SIEM detects a confirmed phishing click, a SOAR playbook disables the user's sessions, opens a ticket, and pages on-call if it is not acknowledged in 15 minutes. Which use cases are shown?
   - **[x] Disabling access, ticket creation and escalation**  - [ ] Resource provisioning and continuous integration  - [ ] User provisioning and guard rails  - [ ] Security groups and employee retention
   - *4.7 use cases: user and resource provisioning, guard rails, security groups, ticket creation, escalation, enabling/disabling services and access, CI and testing, integrations and APIs. This flow disables, tickets and escalates. Faster response also shows the "reaction time" benefit.*
   - @4.7.use
4. A single engineer wrote all the automation scripts and has now left. Nobody understands them and they break after an OS update. Which TWO considerations were overlooked? (Select 2)
   - **[x] Ongoing supportability**  - **[x] Technical debt**  - [ ] Workforce multiplier  - [ ] Scaling securely
   - *Considerations: complexity, cost, single point of failure, technical debt, ongoing supportability. Undocumented scripts built by one person are hard to support and pile up debt. Workforce multiplier and scaling are benefits.*
   - @4.7.cons
5. Every time a developer commits code, the pipeline builds it and runs unit tests, a SAST scan and a dependency check, and rejects the merge if any of them fail. Which automation use case is this?
   - **[x] Continuous integration and testing**  - [ ] Guard rails  - [ ] Resource provisioning  - [ ] Integrations and APIs
   - *Continuous integration and testing automatically builds and tests every change so flaws are caught early, and adding security scans is the classic DevSecOps use. Guard rails is the most tempting because the merge is blocked, but guard rails stop unsafe infrastructure configurations, not code that fails tests. Provisioning creates resources and APIs connect tools. Hook: CI tests every commit.*
   - @4.7.use
6. The SOC's threat intelligence platform pushes each newly reported malicious IP straight to the perimeter firewall's management interface, and the firewall begins blocking it within seconds with no analyst involved. Which automation use case is this?
   - **[x] Integrations and APIs**  - [ ] Guard rails  - [ ] Security groups  - [ ] Ticket escalation
   - *Integrations and APIs let one tool drive another, so a threat feed can update firewall rules automatically and improve reaction time. Security groups is tempting because traffic gets blocked, but security groups are a use case for automating access rules on cloud resources, not tool-to-tool integration. Guard rails stop unsafe changes and escalation routes tickets. Hook: APIs are the wiring between tools.*
   - @4.7.api
7. A SOC routes all alert triage through one SOAR server. During a routine OS upgrade on that server, no alerts were enriched or ticketed for six hours. Which automation consideration was MOST clearly overlooked?
   - **[x] Single point of failure**  - [ ] Technical debt  - [ ] Ongoing supportability  - [ ] Complexity
   - *A single point of failure is one component whose loss stops every process that depends on it, so the server needed redundancy and a manual fallback. Ongoing supportability is tempting because an upgrade was involved, but the problem was that everything depended on one box, not that nobody could maintain the scripts. Technical debt and complexity describe messy or hard-to-predict automation. Hook: one engine, every car stops.*
   - @4.7.cons
8. A web server is confirmed compromised and the attacker still has an active session. The team has finished scoping the incident. What should the team do NEXT?
   - **[x] Isolate the server from the network**  - [ ] Wipe and rebuild the server  - [ ] Restore the server from backup  - [ ] Remove the attacker's web shell
   - *Containment comes next after analysis, so isolating the server limits damage while keeping evidence intact. Removing the web shell is tempting, but that is eradication, and doing it while the attacker is still connected can tip them off and miss other footholds. Wiping is also eradication and destroys evidence, and restoring is recovery. Hook: contain before you clean, clean before you restore.*
   - @4.8.contain
9. After an incident, the team restores servers but the same attacker is back in a week via a web shell they missed. Which phase was incomplete?
    - **[x] Eradication**  - [ ] Preparation  - [ ] Detection  - [ ] Lessons learned
    - *Eradication removes all malware, backdoors and persistence and fixes the entry point. A surviving web shell means eradication failed, and recovery happened too soon.*
    - @4.8.erad
10. After a ransomware case is closed, the IR lead meets IT, legal and comms to walk through the timeline and decide which runbooks change. Which IR phase is this, and what is its MAIN purpose?
    - **[x] Lessons learned, to improve future response**  - [ ] Recovery, to confirm services are restored  - [ ] Analysis, to scope the affected systems  - [ ] Preparation, to build the response team
    - *Lessons learned reviews what happened after the incident and feeds improvements back into preparation. Preparation is tempting because the runbooks will change, but the meeting itself is the post-incident review; preparation is where the updated runbooks then get used. Recovery restores services and analysis scopes the incident during the response. Hook: last phase feeds the first.*
    - @4.8.lessons
11. An IR team wants to rehearse a data breach response. The facilitator reads out scenario updates and each team member explains what they would do, without touching any systems. What is this?
    - **[x] A tabletop exercise**  - [ ] A simulation  - [ ] A walkthrough of the playbook by one analyst  - [ ] A threat hunt
    - *A tabletop exercise is a discussion-based rehearsal where participants talk through their actions as a scenario unfolds, at low cost and risk. A simulation is tempting because it also uses a scenario, but a simulation acts out the incident with real or realistic systems and injects, such as a fake phishing campaign. A solo walkthrough is not a team exercise and a hunt searches for real threats. Hook: tabletop = talk, simulation = do.*
    - @4.8.test
12. A SOC hired six analysts who have never used its EDR console or its incident playbooks. Before they join the on-call rota, which IR activity is MOST appropriate?
    - **[x] Training**  - [ ] A tabletop exercise  - [ ] A simulation  - [ ] Threat hunting
    - *Training teaches people their roles, tools and procedures before a real incident. A tabletop exercise is tempting, but exercises test a plan with people who already know it; they do not teach a console from scratch. A simulation is also a test, and hunting is an operational activity. Hook: train first, then test.*
    - @4.8.train
13. After an outage caused by malware, the team asks "why" repeatedly and finds a missing patch, then a broken patch approval process. What technique is this?
    - **[x] Root cause analysis**  - [ ] Threat hunting  - [ ] Tabletop exercise  - [ ] Chain of custody
    - *RCA digs past symptoms to the underlying cause (5 whys, fishbone) so the fix stops recurrence. Hunting looks for undetected threats. Tabletops rehearse plans. Chain of custody tracks evidence.*
    - @4.8.rca
14. No alert has fired, but an analyst uses new threat intel about an APT's techniques to search EDR data for signs of that group. What is this?
    - **[x] Threat hunting**  - [ ] Incident containment  - [ ] Alert tuning  - [ ] Root cause analysis
    - *Threat hunting = proactive, hypothesis-driven search for threats that evaded existing detections, often using intel and frameworks like MITRE ATT&CK. Containment follows a known incident. Tuning adjusts rules. RCA explains a past event.*
    - @4.8.hunt
15. A company receives notice of a lawsuit about a former employee. Counsel instructs IT to stop the routine deletion of that employee's mailbox. What is this?
    - **[x] A legal hold**  - [ ] Data sanitization  - [ ] Chain of custody  - [ ] Containment
    - *Legal hold = preservation order that suspends normal retention and deletion for relevant data once litigation is expected. Sanitization destroys data. Chain of custody records who handles evidence. Containment is IR.*
    - @4.8.hold
16. An investigator seizes a laptop that may be used in a lawsuit. Which record BEST helps prove in court that the evidence was not altered while in the company's care?
    - **[x] Chain of custody**  - [ ] Legal hold notice  - [ ] Forensic report  - [ ] E-discovery request
    - *Chain of custody documents everyone who handled the evidence, when and why, so gaps cannot be used to argue tampering. A legal hold is tempting because it is also legal, but it orders data to be preserved; it does not record who handled the item. The report presents findings and e-discovery is the process of producing data. Hook: custody = every hand that touched it.*
    - @4.8.coc
17. A responder is collecting evidence from a running, compromised server. By order of volatility, which should be captured FIRST?
    - **[x] RAM contents**  - [ ] Disk image  - [ ] Remote syslog entries  - [ ] Swap/page file
    - *Order of volatility starts with the most short-lived data: CPU registers and cache, then RAM and live network state, then temporary files such as swap, then disk, then remote logs and archives. Swap is tempting because it holds memory pages, but it is written to disk and survives longer than RAM. Remote logs are stored elsewhere and last longest here. Hook: grab what dies first.*
    - @4.8.acq
18. Before analyzing a disk image, the examiner hashes both the original drive and the image and finds them identical, then works only on the copy behind a write blocker. Which forensic principle is this?
    - **[x] Preservation of evidence integrity**  - [ ] E-discovery  - [ ] Root cause analysis  - [ ] Recovery
    - *Preservation = protect evidence from change: write blockers, working copies, hashes (such as SHA-256) to prove integrity, secure storage. E-discovery is the legal process of finding and producing electronic data. RCA and recovery are IR topics.*
    - @4.8.pres
19. A court case requires the company to search, review and hand over all emails mentioning a contract. Which process is this?
    - **[x] E-discovery**  - [ ] Threat hunting  - [ ] Data retention  - [ ] Incident containment
    - *E-discovery = identifying, collecting and producing electronically stored information for legal proceedings. Hunting finds threats. Retention keeps data for set periods. Containment limits an incident.*
    - @4.8.ediscovery
20. A forensic investigation into data theft is complete. Legal counsel needs something that explains what was found and can be independently checked. Which output is MOST appropriate?
    - **[x] A forensic report**  - [ ] The chain of custody form  - [ ] The verified disk image  - [ ] A lessons-learned summary
    - *A forensic report documents findings, methods, timeline and evidence references so others can verify the conclusions. Chain of custody is tempting because courts need it, but it only shows handling, not what was found. The raw image needs expert analysis and lessons learned is an IR improvement step. Hook: custody proves integrity, the report tells the story.*
    - @4.8.report
21. An analyst suspects 198.51.100.77 scanned the company last night and wants to know which destination ports it tried and whether each connection was permitted. Which log source is BEST?
    - **[x] Firewall logs**  - [ ] IPS/IDS logs  - [ ] Endpoint logs  - [ ] Application logs
    - *Firewall logs record every allowed and denied connection with source, destination, port and time. IPS/IDS logs are tempting, but they record traffic that matched an attack signature, not every connection attempt and its permit or deny result. Endpoint and application logs only cover individual hosts and apps. Hook: firewall = who knocked and was let in.*
    - @4.9.fw
22. A user says she never logged in at 23:40, but her account shows a successful logon. Which source BEST confirms when the logon happened on her PC and what type of logon it was?
    - **[x] OS security logs**  - [ ] Endpoint (EDR) logs  - [ ] Network logs  - [ ] Application logs
    - *OS security logs record logons with type and source, such as Windows event ID 4624 for success and 4625 for failure, or Linux auth logs. Endpoint EDR logs are tempting, but they focus on processes, files and threats rather than being the authoritative logon audit record. Network logs lack user logon detail and application logs cover app events. Hook: who logged on = OS security log.*
    - @4.9.os
23. A file-sharing platform's audit trail shows that a user selected 2,000 customer records and used the "Download all" feature. Which log source recorded this?
    - **[x] Application logs**  - [ ] Endpoint logs  - [ ] OS security logs  - [ ] Firewall logs
    - *Application logs capture what users do inside the software, such as logins, exports and admin changes. Endpoint logs are tempting because the file ended up on a laptop, but they see processes and files on the host, not which feature was used inside the platform. OS logs cover the operating system and firewalls see connections only. Hook: inside the app = app log.*
    - @4.9.app
24. An investigator checks a leaked document's author, creation date and the GPS location in an attached photo. Which data type is this?
    - **[x] Metadata**  - [ ] A packet capture  - [ ] A dashboard  - [ ] A firewall log
    - *Metadata = data about data: file author and timestamps, email headers (sender, route), photo EXIF (camera, GPS). Useful for timelines and attribution. The others are separate data sources.*
    - @4.9.meta
25. The SOC needs to know exactly what data an attacker sent in a suspicious session, including the payload. Which source is BEST?
    - **[x] A packet capture (PCAP)**  - [ ] NetFlow records  - [ ] An automated weekly report  - [ ] A dashboard summary
    - *Packet captures record full traffic, including payloads (if not encrypted), for deep analysis in tools like Wireshark. NetFlow has metadata only. Reports and dashboards summarise; they do not hold the raw packets.*
    - @4.9.pcap
26. A CIO wants a summary of failed logins, top blocked sites and patch status in her inbox every Monday morning. Which data source fits BEST?
    - **[x] Automated reports**  - [ ] Dashboards  - [ ] SIEM correlation alerts  - [ ] Vulnerability scans
    - *Automated reports are scheduled summaries that tools generate and deliver. Dashboards are tempting because they summarise the same data, but they are a live on-screen view, not a scheduled delivery. Alerts fire on single events and scans cover only weaknesses. Hook: report comes to you, dashboard you go to.*
    - @4.9.src
27. A SOC adopts playbooks so that three analysts can handle the alert volume that used to need ten. Which automation benefit does this BEST describe?
   - **[x] Workforce multiplier**  - [ ] Employee retention  - [ ] Enforcing baselines  - [ ] Standard infrastructure configurations
   - *Workforce multiplier = fewer people doing more work. Employee retention is about staff staying because less boring toil, which is related but not what is measured here. Baselines and standard configs are about consistent settings.*
   - @4.7.ben
28. A team's SOAR playbooks now have so many branches and integrations that nobody can predict what they will do during an incident. Which automation consideration does this show?
   - **[x] Complexity**  - [ ] Cost  - [ ] Workforce multiplier  - [ ] Reaction time
   - *Complexity is a listed consideration: more automation means more moving parts to understand and support. Cost is the licence and build spend. Workforce multiplier and reaction time are benefits, not drawbacks. Related considerations: single point of failure, technical debt, ongoing supportability.*
   - @4.7.con
29. PBQ 4.8 - IR process order. Each event happened during a ransomware case. Pick the IR phase for each.
   - [p] Event 1: Backups are restored to rebuilt hosts and watched for a week :: A Preparation · B Detection · C Analysis · D Containment · E Eradication · F Recovery · G Lessons learned = f
   - [p] Event 2: Responders confirm the strain and list every affected host :: A Preparation · B Detection · C Analysis · D Containment · E Eradication · F Recovery · G Lessons learned = c
   - [p] Event 3: The team agrees runbook changes in a post-incident review :: A Preparation · B Detection · C Analysis · D Containment · E Eradication · F Recovery · G Lessons learned = g
   - [p] Event 4: Affected hosts are moved to a quarantine VLAN :: A Preparation · B Detection · C Analysis · D Containment · E Eradication · F Recovery · G Lessons learned = d
   - [p] Event 5: Months earlier, the jump bag and contact list were assembled :: A Preparation · B Detection · C Analysis · D Containment · E Eradication · F Recovery · G Lessons learned = a
   - [p] Event 6: Persistence scheduled tasks are deleted and the VPN flaw is patched :: A Preparation · B Detection · C Analysis · D Containment · E Eradication · F Recovery · G Lessons learned = e
   - [p] Event 7: EDR raises an alert on mass file renames :: A Preparation · B Detection · C Analysis · D Containment · E Eradication · F Recovery · G Lessons learned = b
   - *Each event maps to its phase in the order preparation, detection, analysis, containment, eradication, recovery, lessons learned. The common trap is calling patching the flaw recovery, but removing persistence and closing the entry point is eradication; recovery is restoring and monitoring. Hook: "Please Don't Ask Cats Every Rainy Lunch".*
   - @4.8.ir

30. PBQ 4.9 - Data sources. For each question, pick the BEST source.
    - [p] Was the SQL injection attempt dropped or just raise an alert :: A IPS/IDS logs · B Endpoint logs · C Network logs · D Vulnerability scans · E Dashboards · F Firewall logs · G Automated reports = a
    - [p] Which parent process launched PowerShell on a finance workstation at 02:13 :: A IPS/IDS logs · B Endpoint logs · C Network logs · D Vulnerability scans · E Dashboards · F Firewall logs · G Automated reports = b
    - [p] Did the server's uplink lose connectivity at 02:15 :: A IPS/IDS logs · B Endpoint logs · C Network logs · D Vulnerability scans · E Dashboards · F Firewall logs · G Automated reports = c
    - [p] Was the exploited weakness already known on that host last month :: A IPS/IDS logs · B Endpoint logs · C Network logs · D Vulnerability scans · E Dashboards · F Firewall logs · G Automated reports = d
    - [p] The CISO wants to watch open incidents by severity in real time :: A IPS/IDS logs · B Endpoint logs · C Network logs · D Vulnerability scans · E Dashboards · F Firewall logs · G Automated reports = e
    - *IPS/IDS logs show the signature match and the action taken, endpoint logs show processes on a host, network logs come from switches, routers and VPNs, vulnerability scans show weaknesses that existed before the incident, and dashboards give a live view. The common trap is firewall logs for the first item, but a firewall records allowed or denied connections, not whether an attack signature was blocked or only alerted; automated reports are scheduled, not real time. Hook: live = dashboard, scheduled = report.*
    - @4.9.src

### Key facts
- **4.7 use cases: user/resource provisioning, guard rails, security groups, ticket creation, escalation, enable/disable services and access, CI/testing, integrations/APIs. Benefits: efficiency, enforce baselines, standard configs, scale securely, retention, reaction time, workforce multiplier. Considerations: complexity, cost, SPOF, technical debt, supportability.**
- **IR: preparation, detection, analysis, containment, eradication, recovery, lessons learned. Training; testing (tabletop, simulation); RCA; threat hunting.**
- **Forensics: legal hold, chain of custody, acquisition (order of volatility), reporting, preservation (hashes, write blockers), e-discovery.**
- **4.9 log data: firewall, application, endpoint, OS security, IPS/IDS, network, metadata. Data sources: vulnerability scans, automated reports, dashboards, packet captures.**

## Test 23 - 5.1 Security Governance: Policies, Standards, Procedures, Roles (28 Q)

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
5. Auditors find staff treat "remote workers should lock screens in public" as optional. Management wants violations to carry sanctions. What is the BEST change?
   - **[x] Make it a mandatory standard**  - [ ] Reword the guideline more strongly  - [ ] Add it to the onboarding procedure  - [ ] Cover it in awareness training
   - *Only mandatory documents such as a policy or standard can be enforced with sanctions. Rewording the guideline is tempting, but a guideline stays advisory however firmly it is phrased. Procedures list steps and training raises awareness, but neither makes the rule binding. Hook: guidelines guide, standards command.*
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
9. A hospital hires 40 nurses a month. Some start with no EHR access while others are given a former nurse's login. Which document would BEST fix this?
   - **[x] An onboarding procedure**  - [ ] An access control standard  - [ ] An acceptable use policy  - [ ] An identity management policy
   - *An onboarding procedure gives repeatable steps so each new hire gets the right role-based access, equipment and training every time. An access control standard is tempting, but it sets the rules such as least privilege and review frequency; it does not give the steps a new starter goes through. The AUP covers user behaviour and a policy states intent. Hook: a procedure is the recipe.*
   - @5.1.proc
10. During a phishing incident, a junior analyst follows a pre-written decision flow: check the headers, pull the email from all mailboxes, block the sender, reset the clicked user's password. What is this document?
   - **[x] Playbook**  - [ ] Policy  - [ ] Standard  - [ ] Guideline
   - *A playbook is a procedure with step-by-step actions for a specific incident type. Hook: play by play. Policy states who has authority, not the steps; a standard sets values; a guideline is optional.*
   - @5.1.proc
11. A change advisory board approves a firewall rule change. Under the change management procedure, what must be in place BEFORE the change is made?
   - **[x] A backout plan**  - [ ] An updated network diagram  - [ ] A post-change review  - [ ] Updated documentation
   - *A backout plan, along with a maintenance window and testing, must be ready before implementing so the change can be reversed if it fails. Updated documentation and diagrams are tempting because they are required too, but they are updated after the change is made. A review happens after implementation. Hook: know the way back before you go.*
   - @5.1.proc
12. A US retailer opens its first store in Germany and must change how it handles employee personal data there. Which category of external consideration does the EU GDPR fall under in the SY0-701 objectives?
   - **[x] Global**  - [ ] National  - [ ] Industry  - [ ] Legal
   - *GDPR applies across many countries and to anyone handling EU residents' data, so the objectives treat it as a global consideration. National is tempting because the store is in Germany, but GDPR is not German law; it spans the whole EU and beyond. Industry rules come from sector bodies, and legal is a separate external consideration about lawsuits and liability rather than where the rule applies. Hook: many countries = global.*
   - @5.1.ext
13. A small online shop must follow strict card data rules, enforced through its merchant contract rather than by any law. Which external consideration is this?
   - **[x] Industry**  - [ ] Regulatory  - [ ] National  - [ ] Legal
   - *PCI DSS is set by the card brands and enforced by contract, so it is an industry consideration. Regulatory is tempting because PCI DSS feels like a regulation, but it is not issued by a government regulator. National and legal considerations come from legislation. Hook: industry = rules from your sector, not a parliament.*
   - @5.1.ext
14. A city requires contractors handling resident data to store it within the state. A vendor's internal policy allows storage in any region. What should the vendor do FIRST?
   - **[x] Update its policy to meet the requirement**  - [ ] Request a risk exception from the city  - [ ] Transfer the risk with insurance  - [ ] Accept the risk with sign-off
   - *External legal and local requirements override internal policy, so the policy must be revised to meet them. A risk exception is tempting, but exceptions are internal approvals to deviate from your own policy; they cannot waive someone else's legal requirement. Insurance and internal acceptance do not make the vendor compliant. Hook: the law sets the floor.*
   - @5.1.ext
15. A remote work policy written in 2019 has never been reviewed and does not mention personal devices or home Wi-Fi. What should governance require?
   - **[x] Scheduled reviews plus reviews after major changes**  - [ ] Reviews triggered by audit findings  - [ ] Reviews triggered by security incidents  - [ ] Reviews at each manager's request
   - *Policies need monitoring and revision on a schedule, often yearly, and also when laws, technology or incidents change. Review after an incident is tempting because incidents do trigger revisions, but on its own that is reactive and leaves gaps like this one. Audit-only or manager-driven reviews are also ad hoc. Hook: service the car on schedule, not only after a breakdown.*
   - @5.1.revise
16. A post-breach review shows the incident response procedure has no legal hold step. What is the BEST governance action?
   - **[x] Revise the procedure now with version control**  - [ ] Add a legal hold guideline  - [ ] Wait for the annual procedure review  - [ ] Retrain staff on the current procedure
   - *Lessons learned should trigger a prompt, tracked revision so everyone works from the corrected version. A guideline is tempting because it is quick, but guidelines are optional, so the legal hold step could still be skipped. Waiting leaves a known gap and retraining on the current version repeats it. Hook: fix the document, then train.*
   - @5.1.revise
17. At a multinational, which governance body sets overall security direction and holds executives accountable on behalf of the owners?
   - **[x] Board of directors**  - [ ] Security steering committee  - [ ] Change advisory board  - [ ] Government entity
   - *A board of directors sets direction and oversees executives for shareholders. A steering committee is tempting, but committees advise leadership and work under the board; they do not answer to owners. A change advisory board approves IT changes and a government entity regulates from outside. Hook: the board sits at the top.*
   - @5.1.gov
18. Each business unit of a conglomerate picks its own security tools and policies. Audits show inconsistent controls but fast local decisions. Which governance model is this?
   - **[x] Decentralized**  - [ ] Centralized  - [ ] Government entity  - [ ] Federated identity
   - *Decentralized = authority spread to units; fast and local but inconsistent. Centralized = one team decides for all; consistent but slower. Federated identity is an IAM term, not governance.*
   - @5.1.gov
19. A public water utility must follow security rules issued by a public regulator, which also inspects its controls each year. Which governance structure provides this oversight?
   - **[x] Government entity**  - [ ] Board of directors  - [ ] Committee  - [ ] Centralized governance
   - *Government entities govern public bodies and regulated sectors by issuing rules and inspecting compliance. Centralized is tempting because one body sets rules for all, but centralized versus decentralized describes where authority sits inside an organisation, not who oversees from outside. Boards and committees are internal. Hook: outside regulator = government entity.*
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
23. A warehouse supervisor is dismissed on Friday. On Monday, IT finds his badge still opens the loading dock, his laptop was not returned and his cloud storage account is active. Which document would MOST directly have prevented this?
   - **[x] An offboarding procedure**  - [ ] An access control standard  - [ ] An acceptable use policy  - [ ] A physical security standard
   - *An offboarding procedure lists the steps when someone leaves: disable accounts and badges, collect assets and hand over data. An access control standard is tempting because it covers access rules, but it sets requirements, not the step-by-step actions triggered by a departure. The AUP governs behaviour and a physical standard sets facility rules. Hook: leavers need a checklist.*
   - @5.1.proc

### Key facts
- **Policy = intent (AUP, infosec, BC, DR, IR, SDLC, change mgmt); standard = mandatory specifics (password, access control, physical, encryption); procedure = steps (change mgmt, on/offboarding, playbooks); guideline = optional.**
- **External: regulatory, legal, industry, local/regional, national, global. Governance: boards, committees, government entities, centralized vs decentralized.**
- **Owner decides, custodian/steward cares for, controller sets purpose, processor acts on instructions.**
24. A company needs a document stating how IT systems and data will be restored after its primary data centre is lost. Which document is this?
   - **[x] Disaster recovery policy**  - [ ] Business continuity policy  - [ ] Information security policy  - [ ] Change management policy
   - *Disaster recovery covers restoring IT after a disaster. Business continuity is broader: keeping the whole business operating during disruption. The information security policy is the umbrella statement of intent. Hook: BC keeps the shop open, DR gets the computers back.*
   - @5.1.policy
25. A cross-department group meets monthly to review security risks and advise the executives, while one corporate office sets security policy for every subsidiary. Which pair BEST describes this governance setup?
   - **[x] Committee, centralized**  - [ ] Board, decentralized  - [ ] Government entity, centralized  - [ ] Committee, decentralized
   - *A working group under leadership that advises is a committee; the board sits at the top. One office deciding for all units is centralized; decentralized lets each unit set its own. *
   - @5.1.gov
26. A firm operating on four continents must reconcile the privacy laws of every market it serves. Which external consideration is this?
   - **[x] Global**  - [ ] National  - [ ] Local/regional  - [ ] Industry
   - *Many countries at once = global. One country = national. A state or city = local/regional. Industry considerations come from sector bodies, like PCI DSS for card data.*
   - @5.1.gov
27. PBQ 5.1 - Governance documents. Classify each item. ¶  1  "Leadership commits to safeguarding customer trust and assigns security duties to every manager" ¶  2  "Public web services accept TLS 1.2 or newer, nothing older" ¶  3  "For a new hire: 1) create directory account, 2) add role groups, 3) issue laptop, 4) enrol MFA" ¶  4  "It is a good idea to keep a privacy screen on your laptop when travelling"
   - [p] Item 1 (Leadership commits to safeguarding customer trust and assigns...) :: A Policy · B Standard · C Procedure · D Guideline = a
   - [p] Item 2 (Public web services accept TLS 1.2 or newer, nothing older) :: A Policy · B Standard · C Procedure · D Guideline = b
   - [p] Item 3 (For a new hire: 1) create directory account, 2) add role groups,...) :: A Policy · B Standard · C Procedure · D Guideline = c
   - [p] Item 4 (It is a good idea to keep a privacy screen on your laptop when...) :: A Policy · B Standard · C Procedure · D Guideline = d
   - *1: high-level intent, so policy. 2: a specific mandatory value, so standard. 3: ordered steps, so procedure (onboarding). 4: "a good idea" = optional, so guideline. Hook: policy = why, standard = how much, procedure = how, guideline = suggestion.*
   - @5.1.std

28. PBQ 5.1 - Data roles at a clinic that uses a cloud billing provider. Pick each role. ¶  1  A patient who asks what billing data is held about him ¶  2  The billing provider, which may only run invoices the clinic requests ¶  3  The practice manager, the senior person ultimately responsible for all billing records ¶  4  The clinic as an organisation, which chose to collect insurance details and for what ¶  5  The sysadmin who configures nightly backups and share permissions
   - [p] Party 1 (A patient who asks what billing data is held about him) :: A Data subject · B Processor · C Custodian · D Controller · E Owner = a
   - [p] Party 2 (The billing provider, which may only run invoices the clinic requests) :: A Data subject · B Processor · C Custodian · D Controller · E Owner = b
   - [p] Party 3 (The practice manager, the senior person ultimately responsible for...) :: A Data subject · B Processor · C Custodian · D Controller · E Owner = e
   - [p] Party 4 (The clinic as an organisation, which chose to collect insurance...) :: A Data subject · B Processor · C Custodian · D Controller · E Owner = d
   - [p] Party 5 (The sysadmin who configures nightly backups and share permissions) :: A Data subject · B Processor · C Custodian · D Controller · E Owner = c
   - *1: the person the data is about, so data subject. 2: acts only on instructions, so processor. 3: senior and ultimately responsible, so owner. 4: decides purpose and means, so controller. 5: implements technical care, so custodian.*
   - @5.1.roles

## Test 24 - 5.2 Risk Management + Business Impact Analysis (27 Q)

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
10. A control costs 60,000 a year and would eliminate a risk with an ALE of 25,000. What is the BEST decision on financial grounds?
   - **[x] Do not buy it; accept or find a cheaper control**  - [ ] Buy it; it removes the risk entirely  - [ ] Buy it; the SLE exceeds its cost  - [ ] Transfer the risk to justify the cost
   - *A control is justified when its yearly cost is less than the annual loss it prevents, and 60,000 to prevent 25,000 is a net loss. Comparing with SLE is tempting, but cost per year must be compared to ALE, the yearly expected loss, not a single event. Removing the risk entirely does not change the maths and transfer is a different strategy. Hook: never pay more than the yearly loss.*
   - @5.2.quant
11. Where should a company track each identified risk with its owner, score, chosen treatment and current status?
   - **[x] Risk register**  - [ ] Risk matrix  - [ ] Business impact analysis  - [ ] Asset inventory
   - *A risk register is the central record of risks with owners, ratings, responses, KRIs and status. A risk matrix is tempting because it scores risks, but it only plots likelihood against impact and does not track owners or treatment. A BIA covers process downtime and the inventory lists assets. Hook: register = the risk ledger.*
   - @5.2.reg
12. The register lists "failed backup jobs per week" with an alert if it exceeds 3. What is this metric?
   - **[x] Key risk indicator (KRI)**  - [ ] Risk appetite  - [ ] Recovery point objective  - [ ] Annualized rate of occurrence
   - *KRI = a measurable early warning that a risk is rising. Analogy: a fuel gauge warning light. Appetite is the overall willingness to take risk; RPO is a data loss target; ARO is how often an event occurs.*
   - @5.2.reg
13. A risk in the register has had no treatment progress for a year. The register shows a score and a KRI but nobody accountable for acting on it. What is the BEST fix?
   - **[x] Assign a risk owner**  - [ ] Lower the risk threshold  - [ ] Formally accept the risk  - [ ] Add a second KRI
   - *Each risk needs an owner who is accountable for its treatment and monitoring, otherwise nothing happens. Formal acceptance is tempting, but acceptance itself must be signed off by an accountable owner and does not fix the missing accountability. Changing the threshold or adding KRIs only changes when alerts fire. Hook: no owner, no action.*
   - @5.2.reg
14. A board says "we accept small security risks if they help us enter new markets quickly." Which risk appetite is this?
   - **[x] Expansionary**  - [ ] Conservative  - [ ] Neutral  - [ ] Zero tolerance
   - *Expansionary = willing to take more risk for growth. Conservative = avoids risk; neutral = balanced. Hook: expand = accept risk to grow.*
   - @5.2.appetite
15. A pension fund refuses any new technology without long proven use and favours safety over growth. Which appetite is this?
   - **[x] Conservative**  - [ ] Expansionary  - [ ] Neutral  - [ ] Transference
   - *Conservative appetite = low willingness to take risk. Transference is a treatment strategy, not an appetite.*
   - @5.2.appetite
16. A company's risk appetite is conservative. For its payroll service it states that up to 4 hours of downtime a month is acceptable. What does the 4-hour figure represent?
   - **[x] Risk tolerance**  - [ ] Risk threshold  - [ ] Recovery time objective  - [ ] Key risk indicator
   - *Risk tolerance is the acceptable deviation around a specific objective, here monthly downtime. Risk threshold is tempting, but a threshold is the trigger line on an indicator that prompts action, not the acceptable variation itself. An RTO is a restore target per incident and a KRI is the metric being watched. Hook: appetite is the diet, tolerance is today's allowance.*
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
20. The board wants a quarterly summary of the top risks, how their scores have changed and the status of each treatment. Which risk management activity does this describe?
   - **[x] Risk reporting**  - [ ] Risk monitoring  - [ ] Risk analysis  - [ ] Risk identification
   - *Risk reporting communicates risk status and trends to stakeholders so they can make decisions. Monitoring is tempting because it tracks the same data, but monitoring is the ongoing watching of risks and KRIs; reporting is presenting the results to leadership. Analysis scores risks and identification lists them. Hook: monitor to know, report to tell.*
   - @5.2.report
21. During a BIA, the finance team says the payroll system can be down for at most 8 hours before fines start. Which metric is this?
   - **[x] RTO**  - [ ] RPO  - [ ] MTBF  - [ ] MTTR
   - *RTO (recovery time objective) = maximum tolerable downtime target to restore service. RPO = maximum data loss in time. MTBF and MTTR describe actual reliability and repair, not targets.*
   - @5.2.bia
22. An online shop takes backups every 24 hours but says losing more than 1 hour of orders is unacceptable. What is the problem?
   - **[x] Backups do not meet the 1-hour RPO**  - [ ] The RTO is too short  - [ ] The MTBF is too high  - [ ] The MTTR is too low
   - *RPO = how much data, measured in time, can be lost. Daily backups can lose up to 24 hours. Fix: more frequent backups or replication. RTO is about time to restore, not data lost.*
   - @5.2.bia
23. A small bank lacks staff to run 24x7 monitoring, so it signs a contract with a managed security service provider that carries liability for missed detections. Which risk strategy is this MAINLY?
   - **[x] Transfer**  - [ ] Avoid  - [ ] Accept  - [ ] Exemption
   - *Transfer = shift the risk (or its cost) to another party, through insurance or by contracting out the work. The bank still keeps accountability for its data. Avoid would stop the activity. Exemption is a form of acceptance.*
   - @5.2.strat

### Key facts
- **Assessment types: ad hoc, recurring, one-time, continuous. Qualitative = ratings; quantitative = SLE = AV x EF, ALE = SLE x ARO.**
- **Register: risks, owners, KRIs, threshold. Appetite: expansionary, conservative, neutral; tolerance = acceptable deviation.**
- **Strategies: transfer, accept (exception, exemption), avoid, mitigate. BIA: RTO, RPO, MTTR, MTBF.**
24. Which statement BEST distinguishes a risk exemption from a risk exception?
   - **[x] Exemption is a standing release; exception is temporary**  - [ ] Exemption is temporary; exception is a standing release  - [ ] Exemption transfers the risk; exception accepts it  - [ ] Exemption needs compensating controls; exception does not
   - *An exemption is a standing approved release from a requirement, while an exception is a temporary approved deviation, usually with compensating controls and an expiry date. The reversed option is the most tempting because the words sound alike, so remember exception = expires. Both are forms of risk acceptance, not transfer. Hook: exception expires, exemption endures.*
   - @5.2.strat
25. A KRI is set so that when the number of unpatched critical servers exceeds 5, the risk is escalated to leadership. What is the value 5?
   - **[x] Risk threshold**  - [ ] Risk appetite  - [ ] Exposure factor  - [ ] Risk tolerance statement
   - *The threshold is the trigger line on an indicator. Appetite is how much risk the organization is willing to pursue overall (expansionary, neutral, conservative). Exposure factor is the percentage of an asset lost in one event.*
   - @5.2.strat
26. PBQ 5.2 - Quantitative risk. A distribution centre is worth 800,000. A fire would destroy 40 percent of it. Fires are expected once every 20 years. Fire suppression upgrades cost 10,000 a year. Type numbers without commas or symbols.
   - [p] SLE = 320000 | 320,000
   - [p] ARO, as a decimal = 0.05 | .05
   - [p] ALE = 16000 | 16,000
   - [p] Is the upgrade justified on cost alone :: A No, it costs more than the ALE · B Yes, it costs less than the ALE · C Only if ARO is 1 · D Cannot tell without the RTO = b
   - [p] Strategy the upgrade represents :: A Accept · B Avoid · C Mitigate · D Transfer = c
   - *1: SLE = 800,000 x 0.40 = 320,000. 2: once in 20 years = 1/20 = 0.05. 3: ALE = 320,000 x 0.05 = 16,000. 4: 10,000 a year to reduce a 16,000 yearly loss is worth it. 5: a control that reduces impact is mitigation. Hook: SLE = AV x EF, ALE = SLE x ARO.*
   - @5.2.quant

27. PBQ 5.2 - BIA for a ticketing system over one year. ¶  Run times between failures: 500 h, 700 h, 900 h ¶  Repair times: 1 h, 2 h, 6 h ¶  Business says: restore within 3 hours; lose no more than 30 minutes of bookings. Type numbers only.
   - [p] MTBF in hours = 700
   - [p] MTTR in hours = 3
   - [p] RTO in hours = 3
   - [p] RPO in minutes = 30
   - [p] Was the RTO met for every failure :: A Yes · B No, one repair took 6 hours · C RTO only applies to backups · D Only MTBF matters = b
   - *1: MTBF = (500 + 700 + 900) / 3 = 700. 2: MTTR = (1 + 2 + 6) / 3 = 3. 3: RTO = 3 hours. 4: RPO = 30 minutes. 5: the average equals the RTO, but the 6-hour repair breached it. Hook: averages hide bad days.*
   - @5.2.bia

## Test 25 - 5.3 Third-Party Risk: Vendor Assessment + Agreements (25 Q)

1. A payroll SaaS vendor will hold all employee bank details. Procurement must decide how much to trust the vendor's security claims before signing. Which evidence gives the BEST assurance?
   - **[x] A recent independent third-party assessment report**  - [ ] The vendor's completed security questionnaire  - [ ] The vendor's signed internal attestation  - [ ] A right-to-audit clause in the draft contract
   - *An independent third-party assessment is the strongest evidence because a neutral party tested the controls. The questionnaire is tempting but is self-reported and unverified, and a right-to-audit clause only grants a future right, it is not evidence today. Hook: trust, but verify with someone neutral.*
   - @5.3.vend
2. A bank wants assurance that a vendor can show its access controls are working in practice, not just documented. What should the bank request?
   - **[x] Internal audit reports with remediation**  - [ ] The vendor's access control policy  - [ ] A signed MOA covering access  - [ ] A completed vendor questionnaire
   - *Evidence of internal audits and remediation shows the vendor actually tests its own controls and fixes findings. A policy is tempting but only says what should happen, not that anyone checks it. Hook: policy is the promise, audit evidence is the proof.*
   - @5.3.vend
3. Before connecting a vendor's portal to its network, a manufacturer wants to see whether the portal can be broken into. Which assessment fits BEST, assuming the contract allows it?
   - **[x] Penetration testing of the vendor's portal**  - [ ] A security questionnaire  - [ ] A conflict of interest check  - [ ] A business partnership agreement
   - *Pen testing actively tries to exploit weaknesses, giving direct evidence. A questionnaire is self-reported. Permission and scope must be written down first.*
   - @5.3.vend
4. After a breach at a hosting provider, a customer discovers its contract gives it no way to inspect the provider's controls. Which clause should have been included?
   - **[x] Right-to-audit clause**  - [ ] Non-compete clause  - [ ] Force majeure clause  - [ ] Termination for convenience
   - *Right-to-audit lets the customer (or its auditor) inspect the vendor's controls and records. Hook: no clause, no peek. Force majeure excuses non-performance in disasters.*
   - @5.3.audit
5. A large cloud provider refuses individual on-site audits from its thousands of customers. A customer's contract requires assurance over the provider's controls. What is the MOST practical way to meet this?
   - **[x] Review the provider's independent audit reports**  - [ ] Send the provider a detailed questionnaire  - [ ] Run a pen test of the provider's platform  - [ ] Add a right-to-audit clause at renewal
   - *Shared independent third-party audit reports and certifications give verified assurance at scale, which is how large providers satisfy customers. A questionnaire is tempting but is only self-reported, and pen testing a provider's platform without its permission is not allowed. Hook: one audit, many readers.*
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
9. During vendor selection, the evaluation panel learns that one panel member's spouse is a director at a shortlisted cloud vendor. What should happen FIRST?
   - **[x] Disclose it and recuse that member**  - [ ] Ask the vendor to sign an NDA  - [ ] Run extra due diligence on the vendor  - [ ] Add a right-to-audit clause
   - *A conflict of interest must be disclosed and managed, usually by recusal, so the selection stays objective. Extra due diligence is tempting but checks the vendor, not the biased evaluator, so the conflict remains. Hook: fix the judge before judging the vendor.*
   - @5.3.select
10. Two vendors pass every technical check. Vendor A is cheaper; Vendor B can store data in-region as the company's privacy law requires and has stronger financials. Which factor should MOST strongly drive the choice?
   - **[x] Fit with risk and compliance requirements**  - [ ] Lowest total contract price  - [ ] Shortest onboarding timeline  - [ ] Most generous SLA rebates
   - *Vendor selection weighs risk and compliance fit first, because a cheap vendor that breaks a legal requirement creates fines and liability. Price is tempting but does not offset non-compliance, and SLA rebates only compensate after failure. Hook: compliance first, cost second.*
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
16. A penetration test SOW lists the IP ranges, dates and deliverables. Which additional item is MOST critical to agree in writing before testing starts?
   - **[x] Signed authorization and out-of-scope systems**  - [ ] The SLA for remediation of findings  - [ ] The report format and severity scale  - [ ] An MOU on future test cycles
   - *Written authorization and explicit exclusions make the test legal and prevent damage to systems not covered. Report format is tempting but is a deliverable detail that cannot make an unauthorized test lawful. Hook: no signature, no scan.*
   - @5.3.contract
17. A vendor passed its security assessment two years ago. Since then it was acquired and moved to new data centres, but no one at the customer noticed. Which practice was MISSING?
   - **[x] Vendor monitoring**  - [ ] Due diligence  - [ ] Supply chain analysis  - [ ] Right-to-audit clause
   - *Vendor monitoring tracks a vendor's changes, breaches and SLA results after the contract starts, which would have caught the acquisition. Due diligence is tempting but happens before signing, and it was done here. Hook: onboarding is not the end.*
   - @5.3.mon
18. Which activity is part of vendor monitoring?
   - **[x] Reviewing monthly SLA reports and news of vendor breaches**  - [ ] Checking the vendor's references before signing  - [ ] Writing the initial RFP  - [ ] Signing the NDA
   - *Monitoring happens after the contract starts. References, RFP and NDA are selection-stage activities.*
   - @5.3.mon
19. A company has 200 small suppliers and cannot audit each one. What is the MOST efficient first step to assess them?
   - **[x] Send a standard security questionnaire**  - [ ] Add a right-to-audit clause to each contract  - [ ] Request independent audit reports from all  - [ ] Perform supply chain analysis on each supplier
   - *A standard questionnaire gathers control information cheaply at scale, and risky answers then trigger deeper checks. Requesting audit reports is tempting but most small suppliers will not have them, and a right-to-audit clause only creates a future right. Hook: survey wide, then dig deep.*
   - @5.3.quest
20. A vendor answers yes to every control on a security questionnaire, including full disk encryption and MFA. What is the MAIN weakness of relying on this result?
   - **[x] The answers are self-reported and unverified**  - [ ] Questionnaires do not cover technical controls  - [ ] It cannot be used in contract negotiation  - [ ] It covers only the vendor's subcontractors
   - *Questionnaires rely on the vendor's honesty, so critical answers should be verified with evidence or audits. Saying they do not cover technical controls is tempting but wrong, since they routinely ask about encryption and MFA. Hook: a yes is not proof.*
   - @5.3.quest
21. During an authorized bank pen test, a tester finds a vendor-hosted server that is not listed in scope but appears to belong to the bank's environment. What should the tester do?
   - **[x] Stop and report it to the bank's contact**  - [ ] Scan it lightly to confirm ownership  - [ ] Test it, since it serves the bank  - [ ] Add it to scope and continue
   - *Rules of engagement limit testing to the agreed scope, and third-party assets need the owner's permission, so the tester stops and reports. A light scan is tempting but is still active testing of an unauthorized system. Hook: out of scope means hands off.*
   - @5.3.roe
22. Which item belongs in the rules of engagement for a test of a vendor's system?
   - **[x] Allowed testing hours and emergency contacts**  - [ ] The SLA uptime target  - [ ] Project deliverables and payment terms  - [ ] The vendor's data retention schedule
   - *Rules of engagement define how the test runs: time windows, allowed techniques, contacts and stop conditions. The SLA uptime target is tempting but belongs in the service agreement; payment terms belong in the SOW and data retention in the vendor's own policy. Hook: RoE is the how, SOW is the what.*
   - @5.3.roe
23. A port authority and the coast guard put in writing that the port will feed camera logs nightly and the coast guard will review alerts within an hour. No money changes hands and it is not a commercial contract. Which agreement is this?
   - **[x] MOA**  - [ ] MOU  - [ ] SLA  - [ ] NDA
   - *MOA (memorandum of agreement) = defines specific responsibilities and is more formal than an MOU (memorandum of understanding), which states shared intent. Hook: understanding = intent, agreement = duties. SLA sets service targets; NDA covers secrecy.*
   - @5.3.agree

### Key facts
- **Assessment: pen testing, right-to-audit, internal audit evidence, independent assessments, supply chain analysis. Selection: due diligence, conflict of interest.**
- **SLA = service levels; MOA/MOU = intent (MOA more formal); MSA = master terms; SOW/WO = specific job; NDA = secrecy; BPA = partnership.**
- **Then: vendor monitoring, questionnaires, rules of engagement.**
24. PBQ 5.3 - Agreements. Pick the document for each need. ¶  1  CDN must restore service within 15 minutes or refund part of the fee ¶  2  A bidder will see unreleased chip designs during the tender ¶  3  Standard legal and payment terms reused for every future engagement with a consultancy ¶  4  Describes the migration project: steps, outputs and due dates ¶  5  Two agencies record that they hope to share threat data someday, with no duties yet ¶  6  Two firms co-sell a product and divide revenue, losses and decision rights
   - [p] Need 1 (CDN must restore service within 15 minutes or refund part of the fee) :: A SLA · B NDA · C MSA · D SOW · E MOU · F BPA · G MOA = a
   - [p] Need 2 (A bidder will see unreleased chip designs during the tender) :: A SLA · B NDA · C MSA · D SOW · E MOU · F BPA · G MOA = b
   - [p] Need 3 (Standard legal and payment terms reused for every future engagement with a consultancy) :: A SLA · B NDA · C MSA · D SOW · E MOU · F BPA · G MOA = c
   - [p] Need 4 (Describes the migration project: steps, outputs and due dates) :: A SLA · B NDA · C MSA · D SOW · E MOU · F BPA · G MOA = d
   - [p] Need 5 (Two agencies record that they hope to share threat data someday, with no duties yet) :: A SLA · B NDA · C MSA · D SOW · E MOU · F BPA · G MOA = e
   - [p] Need 6 (Two firms co-sell a product and divide revenue, losses and decision rights) :: A SLA · B NDA · C MSA · D SOW · E MOU · F BPA · G MOA = f
   - *1: measurable service targets with penalties make it an SLA; it is not an SOW because no project work is described. 2: protecting secrets shared before a deal is an NDA. 3: reusable umbrella terms are an MSA, not an SOW. 4: one project's tasks and deliverables is an SOW. 5: shared intent with no duties is an MOU; an MOA would set specific duties. 6: sharing profits and decisions is a BPA. Hook: service, secret, master, work, understanding, partners.*
   - @5.3.agree

25. PBQ 5.3 - Vendor risk. A new HR SaaS vendor will hold staff records. Answer each part.
   - [p] Strongest evidence of its controls before signing :: A Vendor-completed questionnaire · B Signed management attestation by the vendor · C Independent third-party assessment report · D Evidence of the vendor's internal audits = c
   - [p] Contract term that lets you inspect its controls later :: A Right-to-audit · B SLA · C NDA · D Rules of engagement = a
   - [p] Checking the separate company that runs the vendor's data centre :: A Supply chain analysis · B Vendor monitoring · C Due diligence on the vendor alone · D Penetration testing = a
   - [p] After go-live, reviewing breach news and monthly SLA reports :: A Due diligence · B Vendor monitoring · C Vendor selection · D Supply chain analysis = b
   - *1: an independent assessment beats anything the vendor produces about itself, including internal audits. 2: right-to-audit grants inspection rights; an SLA only sets service targets. 3: the vendor's own suppliers are covered by supply chain analysis, not by checking the vendor alone. 4: ongoing tracking after signing is monitoring; due diligence happens before signing.*
   - @5.3.vend

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
7. A compliance team spends days each month pulling screenshots of system settings for auditors, and drift between pulls goes unnoticed. What would MOST improve compliance monitoring?
   - **[x] Automated continuous control checks**  - [ ] Quarterly internal self-assessments  - [ ] Annual external audits  - [ ] Signed attestations from system owners
   - *Automation checks controls continuously and collects evidence consistently, catching drift between manual pulls. Quarterly self-assessments are tempting but still leave long gaps and stay manual. Hook: machines watch all the time, people only sometimes.*
   - @5.4.mon
8. When the new remote access policy goes live, the HR portal will not let any user continue until they tick "I have read and accept this policy." What is this called?
   - **[x] Acknowledgement**  - [ ] Attestation by a third party  - [ ] Due diligence  - [ ] Data inventory
   - *Acknowledgement = an individual confirms they received and understood a policy. Attestation = a formal statement, often by management or an auditor, that controls are in place and compliant.*
   - @5.4.attest
9. Under a cyber insurance renewal, the COO must sign and submit a declaration that MFA and offline backups are in place across the company. What is this?
   - **[x] Attestation**  - [ ] Acknowledgement  - [ ] Guideline  - [ ] Questionnaire
   - *Attestation = a formal declaration that requirements are met, putting the signer on the hook. Analogy: signing a tax return. An acknowledgement only confirms receipt.*
   - @5.4.attest
10. A US company that has only served US customers starts selling to EU residents through its website. Its servers stay in the US. Which legal implication now applies?
   - **[x] Global, because GDPR covers EU residents**  - [ ] National, because servers are in the US  - [ ] Local/regional, based on the head office state  - [ ] None until it opens an EU office
   - *Privacy law follows the people whose data is processed, so GDPR applies to a non-EU firm serving EU residents, a global legal implication. The national option is tempting but server location does not exempt the company from GDPR. Hook: the law follows the person, not the server.*
   - @5.4.law
11. A firm has customers in several US states, each with different breach notification deadlines and content rules. What is the BEST approach to compliance?
   - **[x] Map each state rule and meet the strictest**  - [ ] Follow only federal breach rules  - [ ] Follow the head office state's rule  - [ ] Apply the rule only where staff work
   - *Local/regional laws apply wherever affected residents live, so mapping them and meeting the strictest overlapping rule covers all. Following only federal rules is tempting but many breach notification duties are set at state level. Hook: residents bring their laws with them.*
   - @5.4.law
12. A fitness app logs Priya's runs, heart rate and home address. In privacy law terms, what is Priya?
   - **[x] Data subject**  - [ ] Data controller  - [ ] Data processor  - [ ] Data custodian
   - *Data subject = the individual the data identifies. They hold rights such as access, correction and erasure.*
   - @5.4.subject
13. A customer asks an online store for a copy of all personal data it holds about her. What does the store need FIRST to answer accurately?
   - **[x] A data inventory showing where her data is**  - [ ] Confirmation from its cloud processor  - [ ] An updated retention policy  - [ ] An acknowledgement signed by the customer
   - *A data inventory maps where personal data lives, which is required to find every record for the request. Asking the processor is tempting but the store, as controller, is accountable and the processor holds only part of the data. Hook: you cannot hand over what you cannot find.*
   - @5.4.subject
14. A clinic stores patient scans with a cloud provider that follows the clinic's instructions. The provider is breached. Who is PRIMARILY accountable to the patients under GDPR-style law?
   - **[x] The clinic, as data controller**  - [ ] The provider, as data processor  - [ ] The provider, as data owner  - [ ] The clinic's IT team, as custodian
   - *The controller decides why and how data is processed and stays accountable to data subjects even when work is outsourced. The processor is tempting because it was breached, but it has duties to the controller, not primary accountability. Hook: outsource the work, not the accountability.*
   - @5.4.ctrl
15. A marketing agency processes a client's customer list to send the client's newsletters. It then starts using the list for its own campaigns. How has its role changed?
   - **[x] It is acting as a controller without authority**  - [ ] It remains a processor, so this is allowed  - [ ] It has become the data owner  - [ ] It has become a joint data custodian
   - *Deciding its own purposes for the data makes the agency a controller, and doing so without a lawful basis breaks privacy law. Staying a processor is tempting but processors may only act on the controller's instructions. Hook: whoever decides the why is the controller.*
   - @5.4.ctrl
16. Two departments argue over who decides retention and access rules for customer support recordings. What is the BEST governance fix?
   - **[x] Assign a single data owner**  - [ ] Make IT the data custodian  - [ ] Let the DPO set the rules  - [ ] Ask the processor to decide
   - *A single data owner, a senior business role, is accountable for the data set and decides retention and access, settling disputes. Making IT the custodian is tempting but custodians implement rules, they do not set them. Hook: owners decide, custodians do.*
   - @5.4.own
17. A company buys a list of email addresses from a data broker for marketing. What should it confirm FIRST?
   - **[x] The data was lawfully collected for this use**  - [ ] The broker will sign an NDA  - [ ] The file is encrypted in transit  - [ ] The list is in the data inventory
   - *Buying data does not grant the right to use it, so lawful collection and consent for marketing must be confirmed first. Encryption in transit is tempting but protects the file, not the legality of using it. Hook: you cannot buy rights the seller never had.*
   - @5.4.own
18. A new DPO cannot answer "where do we keep passport scans?" She commissions a spreadsheet mapping each system to the personal data it holds, the purpose and the retention period. What is this?
   - **[x] Data inventory**  - [ ] Risk register  - [ ] Asset tag list  - [ ] Change log
   - *Data inventory = a record of what personal data exists, where, why and for how long. It underpins retention, requests and breach response.*
   - @5.4.inv
19. An insurer keeps every customer email since 1998 "just in case", all encrypted at rest. What is the MAIN privacy problem?
   - **[x] Data is kept longer than needed**  - [ ] Encryption keys may be lost  - [ ] The data was not classified  - [ ] The emails lack acknowledgements
   - *Retention rules require keeping personal data only as long as legally or business needed, and excess data increases breach impact. Key loss is tempting but is an availability issue, and encryption does not fix over-retention. Hook: old data is liability.*
   - @5.4.inv
20. Tax law requires invoices be kept for 7 years. A customer asks for erasure of all her data after 2 years. What is the BEST response?
   - **[x] Keep invoices until the legal period ends, erase the rest**  - [ ] Erase everything, since erasure overrides retention  - [ ] Keep all data until the tax period ends  - [ ] Anonymize the invoices and erase now
   - *A legal retention duty overrides erasure only for the data the law requires, so the rest must be erased now. Erasing everything is tempting but would break tax law; keeping all data keeps more than the law needs. Hook: keep only what the law requires.*
   - @5.4.inv
21. A former user demands that a social media site delete her account data entirely. Which right is she using?
   - **[x] Right to be forgotten (erasure)**  - [ ] Right to audit  - [ ] Right of first refusal  - [ ] Due care
   - *Right to be forgotten = GDPR right to erasure of personal data, with some exceptions. Right to audit is a vendor contract clause.*
   - @5.4.forget
22. After an erasure request, a company deletes a user's records from production. Copies remain in nightly backups and a developer test database. What is the BEST assessment?
   - **[x] Erasure is incomplete until all copies are handled**  - [ ] Erasure is complete, since production is clean  - [ ] Only the backups need action  - [ ] Only the test copy needs action
   - *Erasure must cover every copy, with backups handled per policy and test data deleted, which a data inventory helps track. Clearing only backups is tempting but the test database is a live copy that also must go. Hook: forgotten means forgotten everywhere.*
   - @5.4.forget
23. A credit union's risk staff spot-check firewall rules every sprint, and a CPA firm reviews the same controls before each regulator filing. Which compliance monitoring elements are these?
   - **[x] Internal and external compliance monitoring**  - [ ] Only external monitoring  - [ ] Due diligence only  - [ ] Data inventory and retention
   - *Compliance monitoring can be internal (own staff) and external (auditors, regulators); using both adds independence. Due diligence is research before a decision; a data inventory is a privacy record.*
   - @5.4.mon

### Key facts
- **Reporting: internal vs external. Non-compliance: fines, sanctions, reputational damage, loss of license, contractual impacts.**
- **Monitoring: due diligence (research) vs due care (ongoing action), attestation and acknowledgement, internal and external, automation.**
- **Privacy: local/regional, national, global laws; data subject; controller vs processor; ownership; data inventory and retention; right to be forgotten.**
24. PBQ 5.4 - Compliance programme. Pick the best match for each situation. ¶  1  The board's audit committee reviews monthly compliance metrics ¶  2  The company files a breach notice with a government authority within 72 hours ¶  3  An authority orders the company to pay 2 million ¶  4  A medical board revokes a hospital's licence ¶  5  An employee ticks a box confirming she read the new remote access policy ¶  6  The CFO signs a declaration to an insurer that MFA is in place
   - [p] Situation 1 :: A Internal reporting · B External reporting · C Acknowledgement · D Attestation = a
   - [p] Situation 2 :: A Internal reporting · B External reporting · C Acknowledgement · D Attestation = b
   - [p] Situation 3 :: A Fine · B Loss of license · C Contractual impact · D Sanctions = a
   - [p] Situation 4 :: A Fine · B Loss of license · C Contractual impact · D Sanctions = b
   - [p] Situation 5 :: A Internal reporting · B External reporting · C Acknowledgement · D Attestation = c
   - [p] Situation 6 :: A Internal reporting · B External reporting · C Acknowledgement · D Attestation = d
   - *1: a board committee is inside the organization, so internal reporting. 2: notice to an authority is external reporting, not an attestation. 3: a money penalty is a fine; sanctions restrict activity. 4: losing the right to operate is loss of license, because the licence itself is withdrawn. 5: confirming receipt of a policy is acknowledgement. 6: formally declaring controls are in place is attestation.*
   - @5.4.report

25. PBQ 5.4 - Privacy request. A European customer asks a travel company to erase her data. The company uses a cloud CRM vendor. Answer each part.
   - [p] Her role :: A Data subject · B Controller · C Processor · D Data owner = a
   - [p] The travel company's role :: A Data subject · B Controller · C Processor · D Custodian = b
   - [p] The CRM vendor's role :: A Data subject · B Controller · C Processor · D Data owner = c
   - [p] Tool needed to find all copies :: A Data inventory · B Risk register · C Asset register = a
   - [p] Booking invoices required by tax law :: A Erase now, since erasure overrides retention · B Keep for the legal period, then delete · C Anonymize now and keep = b
   - [p] The company also serves Australia, whose privacy act applies across all its states :: A Local/regional · B National · C Global = b
   - *1: she is the person the data identifies. 2: the company decides purpose, so controller. 3: the CRM acts on instructions, so processor. 4: a data inventory shows where personal data lives; an asset register lists hardware and software. 5: legal retention overrides erasure for that data only. 6: one country's law is a national implication, even if it covers many regions.*
   - @5.4.forget

## Test 27 - 5.5 + 5.6 Audits, Penetration Testing, Security Awareness (28 Q)

1. After an external audit, the audit firm issues a signed opinion that the company's controls meet the stated framework. What is this opinion?
   - **[x] Attestation**  - [ ] Acknowledgement  - [ ] Self-assessment  - [ ] Rules of engagement
   - *Attestation = an auditor formally vouches that controls meet requirements. Customers rely on it instead of auditing themselves. Self-assessment is done by the organization itself.*
   - @5.5.attest
2. A company's own team checks each department against the security policy before an official audit. Which activity is this?
   - **[x] Internal self-assessment**  - [ ] Regulatory examination  - [ ] Independent third-party audit  - [ ] Passive reconnaissance
   - *Self-assessments are internal reviews to find gaps early. Analogy: a practice exam. Regulatory exams and independent audits are external.*
   - @5.5.int
3. The head of internal audit finds that the COO keeps softening her reports before they reach the board. To protect her independence, to whom should she report directly?
   - **[x] Audit committee**  - [ ] CISO  - [ ] Chief compliance officer  - [ ] Change advisory board
   - *Internal audit reports to the board's audit committee so it is independent of the managers it audits. The CISO is tempting but is management and owns many of the controls being audited. Hook: auditors answer to the board, not the audited.*
   - @5.5.int
4. Examiners from the national banking authority arrive to review a bank's cyber controls under its supervisory powers. Findings may lead to enforcement. What type of audit is this?
   - **[x] Regulatory examination**  - [ ] Independent third-party audit  - [ ] External assessment  - [ ] Internal compliance review
   - *A supervising authority reviewing a business it oversees is a regulatory examination, with enforcement power behind it. An independent third-party audit is tempting but is commissioned by the company from a hired firm, not imposed by a regulator. Hook: who sends the examiners decides the type.*
   - @5.5.ext
5. Enterprise customers ask a SaaS firm for assurance about its security that they can trust without auditing it themselves. Which is the BEST option?
   - **[x] An independent third-party audit**  - [ ] An internal self-assessment report  - [ ] A management attestation letter  - [ ] Results of internal audits
   - *A third-party auditor has no stake in the result, so customers can rely on its findings. Internal audit results are tempting but come from the firm's own staff and lack independence. Hook: independence is what customers buy.*
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
11. A payroll clerk gets an email signed by the CFO, from ceo-office-mail.net, asking her to change an employee's bank details before tonight's run. What should training teach her to do FIRST?
   - **[x] Report it via the phishing button**  - [ ] Reply to ask the CFO to confirm  - [ ] Check the link and header details herself  - [ ] Delete it and continue working
   - *Recognizing the signs and reporting lets security analyse and pull every copy. Replying is tempting but goes to the attacker's domain, and deleting stops the security team from protecting others. Hook: recognize, then report.*
   - @5.6.phish
12. Which sign MOST strongly suggests an email is phishing?
   - **[x] A lookalike sender domain**  - [ ] A valid SPF pass result  - [ ] An external sender banner  - [ ] A link to a well-known cloud service
   - *A domain that imitates the real one is a classic phishing indicator. The external banner is tempting but appears on all outside mail, and SPF passes for any domain the attacker controls. Hook: check the domain letter by letter.*
   - @5.6.phish
13. The security team runs simulated phishing campaigns each quarter. What is the MAIN goal?
   - **[x] Measure and improve recognition and reporting**  - [ ] Test the email filter's detection rate  - [ ] Identify users for disciplinary action  - [ ] Meet an annual attestation requirement
   - *Campaigns build user skills and give metrics such as click and report rates. Testing the email filter is tempting but simulations are usually allowlisted, since the target is the user. Hook: train the human, not the filter.*
   - @5.6.phish
14. An accountant who never works weekends starts downloading large client files at 2 a.m. on Sundays. No settings were changed. Which anomalous behaviour category BEST fits?
   - **[x] Unexpected**  - [ ] Risky  - [ ] Unintentional  - [ ] Insider threat
   - *Unexpected behaviour is activity outside a user's normal pattern, which may signal a compromised account or insider. Risky is tempting but means actions that weaken security, such as disabling controls, which did not happen here. Hook: unexpected breaks the pattern.*
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
   - **[x] Hybrid/remote work environments**  - [ ] Operational security  - [ ] Insider threat  - [ ] Social engineering
   - *Remote work training covers screen locks, shoulder surfing and public Wi-Fi in places like cafes. OPSEC is tempting but is about not leaking small details through what you post or say. Hook: where you work changes what you protect.*
   - @5.6.train
18. A receptionist is handed a padded envelope with an unbranded USB-C drive and a note: "Board slides - please load before 9." No one expected it. What should training say to do?
   - **[x] Give it to security unopened**  - [ ] Scan it with antivirus before opening  - [ ] Open it on an isolated kiosk PC  - [ ] Call the board secretary to verify it
   - *Removable media training says unknown drives go to security, which can analyse them safely, since malicious devices can attack on connection. Scanning first is tempting but some devices act as keyboards and run before antivirus can help. Hook: if you did not expect it, do not plug it.*
   - @5.6.train
19. A developer posts a photo of her desk on social media, with a sticky note showing a server name and the office badge visible. Which training topic covers this?
   - **[x] Operational security (OPSEC)**  - [ ] Password complexity  - [ ] Data retention  - [ ] Change management
   - *OPSEC = avoiding leaking small details that attackers can combine. Passwords may apply too, but the core issue is oversharing.*
   - @5.6.train
20. A company wants to show whether its awareness programme is working over time. Which approach BEST provides initial and recurring reporting?
   - **[x] Baseline phishing test, then regular campaigns**  - [ ] Annual policy acknowledgements  - [ ] Course completion rates per quarter  - [ ] One large campaign after training
   - *A baseline sets the starting point and regular campaigns show the trend in click and report rates. Completion rates are tempting but measure attendance, not behaviour change. Hook: baseline, then trend.*
   - @5.6.report
21. Before launching awareness training, the team surveys roles, past incidents and threats faced by each department. Which phase is this?
   - **[x] Development**  - [ ] Execution  - [ ] Reporting  - [ ] Attestation
   - *Development = designing content to fit audience and risk. Execution = delivering it (sessions, modules, campaigns). Hook: design, then deliver.*
   - @5.6.prog
22. Finance staff face wire fraud attempts, and developers face code repository attacks. How should training execution BEST handle this?
   - **[x] Common baseline plus role-based modules**  - [ ] The same general module for everyone  - [ ] Phishing simulations only  - [ ] Technical training for developers only
   - *Role-based content targets each group's real threats, such as business email compromise for finance, on top of a shared baseline. One general module is tempting because it is consistent, but it misses the attacks each role actually faces. Hook: train for the threats each role sees.*
   - @5.6.prog
23. While tidying folder permissions, a junior admin picks the wrong option and leaves a shared drive readable by all staff. He spots nothing until a colleague mentions it a week later. Which anomalous behaviour category BEST fits?
    - **[x] Unintentional**  - [ ] Risky  - [ ] Unexpected  - [ ] Malicious
    - *Unintentional = human error, such as a misconfigured security setting, a mistyped domain or a misplaced USB drive. Risky covers actions like changing security settings on purpose, editing system files or uploading sensitive files. Unexpected = activity outside the user's normal pattern, such as a login from another country. No harmful intent, so not malicious. Fix with training and permission reviews.*
    - @5.6.anom

### Key facts
- **Attestation = formal assurance. Internal: compliance, audit committee, self-assessments. External: regulatory, examinations, assessment, independent third-party audit.**
- **Pen testing: physical, offensive, defensive, integrated; known, partially known, unknown environment. Recon: passive vs active.**
- **Awareness: phishing (campaigns, recognize, respond), anomalous behaviour (risky, unexpected, unintentional), training topics, initial and recurring reporting, development and execution.**
24. An outside firm evaluates a company's security maturity against a framework and gives recommendations, but does not issue a formal opinion. What is this?
   - **[x] External assessment**  - [ ] Attestation  - [ ] Internal compliance check  - [ ] Regulatory examination
   - *An assessment evaluates and advises. An attestation is a formal written opinion by an independent auditor. A regulatory examination is done by the regulator itself. Internal compliance is done by your own staff.*
   - @5.5.int
25. A user forwards a suspicious email to the SOC. An analyst checks its headers, removes every copy from all mailboxes and thanks the user. Which awareness practice is this?
   - **[x] Responding to reported suspicious messages**  - [ ] Phishing campaign  - [ ] Situational awareness  - [ ] Operational security
   - *Handling what users report closes the loop and encourages more reporting. A phishing campaign is a simulated test the organization sends. Situational awareness is staff noticing what is happening around them.*
   - @5.6.train
26. Staff training covers callers who pretend to be IT support and ask for MFA codes. Which training topic is this?
   - **[x] Social engineering**  - [ ] Insider threat  - [ ] Password management  - [ ] Hybrid/remote work
   - *Impersonation over the phone is social engineering (vishing). Insider threat is about trusted staff misusing access. Password management covers managers and reuse.*
   - @5.6.train
27. PBQ 5.5 - Penetration test scoping. Answer each part.
   - [p] Testers receive a VPN login with standard rights and a subnet list, nothing more :: A Known environment · B Partially known environment · C Unknown environment = b
   - [p] The client shares its repo, architecture docs and a domain admin account :: A Known environment · B Partially known environment · C Unknown environment = a
   - [p] Red team attacks while the blue team responds, sharing findings live :: A Offensive · B Defensive · C Integrated = c
   - [p] Harvesting staff names from LinkedIn and old conference talks :: A Passive reconnaissance · B Active reconnaissance = a
   - [p] Sending SYN probes and grabbing banners from the target's mail gateway :: A Passive reconnaissance · B Active reconnaissance = b
   - [p] Signed sheet listing test windows, excluded hosts and an emergency phone number :: A SLA · B Rules of engagement · C MOU = b
   - *1: some information, so partially known. 2: full information, so known. 3: working together = integrated. 4: no contact with targets, so passive. 5: sends packets, so active. 6: RoE governs how the test runs.*
   - @5.5.pen

28. PBQ 5.6 - Awareness programme review. ¶  Q1 campaign: 28 percent clicked, 3 percent reported. Q3 campaign: 9 percent clicked, 31 percent reported. ¶  Incidents: E1 user plugs in a found USB stick. E2 user emails a file to the wrong client by mistake. E3 user turns off the VPN to stream video. Answer each part.
   - [p] Which metric shows users are becoming active defenders :: A Click rate · B Report rate · C Training completion rate · D Repeat-clicker count = b
   - [p] Which reporting type does the Q1 to Q3 comparison represent :: A Initial · B Recurring · C Attestation = b
   - [p] E1 training topic :: A Removable media · B Insider threat · C Social engineering = a
   - [p] E2 behaviour category :: A Risky · B Unintentional · C Unexpected = b
   - [p] E3 behaviour category :: A Risky · B Unintentional · C Unexpected = a
   - *1: report rate shows users act, not just avoid clicking. 2: tracking change over time is recurring reporting; Q1 alone would be the initial baseline. 3: a found USB stick is removable media, even though baiting is also social engineering. 4: an honest mistake is unintentional. 5: knowingly bypassing a control is risky, not merely unexpected.*
   - @5.6.train

