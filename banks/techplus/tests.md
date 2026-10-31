<!-- passmark: 72 -->
## Test 1 - 1.2 + 1.3 Number Systems, Data Units, Speeds (31 Q)

1. A student is learning number systems. Which list correctly gives the number of digits or symbols each system uses?
   - **[x] Binary 2, octal 8, decimal 10, hexadecimal 16**  - [ ] Binary 2, octal 6, decimal 10, hexadecimal 12  - [ ] Binary 1, octal 8, decimal 10, hexadecimal 16  - [ ] Binary 2, octal 8, decimal 12, hexadecimal 32
   - *The base is the count of symbols: binary 0-1, octal 0-7, decimal 0-9, hex 0-9 plus A-F. Hook: BI = two wheels, OCTopus = eight arms, DECade = ten, HEX + DEC = 6 + 10 = 16. Binary 1 is tempting, but you need both 0 and 1.*
   - @1.2.nota
2. A web designer is handed the colour code #00FF00. Which number system is the code written in?
   - **[x] Hexadecimal**  - [ ] Binary  - [ ] Octal  - [ ] Decimal
   - *The letter F gives it away: only hex uses A-F. Web colours are three hex pairs for red, green and blue, so #00FF00 is pure green. Decimal and octal cannot hold letters; binary only has 0 and 1.*
   - @1.2.nota
3. A technician wants to write a long binary value like 11111111 in a short form that is easy to read and converts neatly, four bits per symbol. Which system is BEST?
   - **[x] Hexadecimal**  - [ ] Decimal  - [ ] Octal  - [ ] Binary
   - *One hex symbol is exactly four bits, so 11111111 becomes FF. That is why MAC addresses and colour codes use hex. Octal groups three bits, which does not divide 8 evenly. Decimal works but does not line up with bits. Analogy: hex is shorthand for binary, like initials for a full name.*
   - @1.2.nota
4. What is the binary number 1101 in decimal?
   - [=] 13 | thirteen
   - *Place values from the right are 1, 2, 4, 8. 1101 = 8 + 4 + 0 + 1 = 13. Reading it as one thousand one hundred and one is the classic slip; binary places double, they do not go up by ten.*
   - @1.2.nota
5. What is the hexadecimal value 1A in decimal?
   - [=] 26 | twenty-six | twenty six
   - *Hex places are 16s and 1s. 1A = one 16 + A (10) = 26. A common slip is 1 + 10 = 11, forgetting that the left digit is worth 16. Analogy: like 2 quarters and a dime, the left coin is worth more.*
   - @1.2.nota
6. What is the decimal number 255 in hexadecimal?
   - **[x] FF**  - [ ] EE  - [ ] FE  - [ ] 100
   - *FF = 15 x 16 + 15 = 240 + 15 = 255, the largest value one byte can hold (11111111). FE is 254, EE is 238 and hex 100 is 256, one too many.*
   - @1.2.nota
7. A log shows a value of octal 17. What is that in decimal?
   - **[x] 15**  - [ ] 17  - [ ] 23  - [ ] 9
   - *Octal places are 8s and 1s. 17 = one 8 + 7 = 15. Reading it as decimal 17 ignores the base. 23 is what you get if you wrongly treat 17 as hex (16 + 7). Hook: in any base, "10" equals the base itself, so octal 10 = 8.*
   - @1.2.nota
8. Which binary number equals decimal 10 and hex A?
   - [=] 1010 | 00001010
   - *10 = 8 + 2, so the 8 place and the 2 place are on: 1010. Hex A also means 10. 1001 is 9 and 1100 is 12, near misses that flip the wrong place.*
   - @1.2.nota
9. A file is described as having a size of exactly one "binary digit". Which unit is that?
   - **[x] Bit**  - [ ] Byte  - [ ] Kilobit  - [ ] Hertz
   - *A bit (binary digit) is a single 1 or 0, the smallest unit of data. A byte is 8 bits. Hertz measures cycles per second, not data. Analogy: a bit is one light switch; a byte is a row of eight.*
   - @1.3.storage
10. A single character such as the letter "K" in a plain text file usually takes up how much space?
    - **[x] One byte (8 bits)**  - [ ] One bit  - [ ] One kilobyte  - [ ] Four bits
    - *In plain text (ASCII), one character fits in one byte of 8 bits. One bit can only show two states, far too few for an alphabet. A kilobyte would hold roughly a thousand characters. Hook: byte = one bite of text, one letter.*
    - @1.3.storage
11. Which list shows storage units from SMALLEST to LARGEST?
    - **[x] KB, MB, GB, TB, PB**  - [ ] KB, GB, MB, TB, PB  - [ ] MB, KB, GB, PB, TB  - [ ] KB, MB, TB, GB, PB
    - *Kilo, Mega, Giga, Tera, Peta, each step roughly 1000 (1024 in binary) times bigger. Hook: "King Mike Gets Tea Pots". The wrong orders swap neighbouring prefixes, the usual trap.*
    - @1.3.storage
12. A customer wants a drive to store about 3,000 GB of family videos. Which drive size is the SMALLEST that will fit?
    - **[x] 4 TB**  - [ ] 2 TB  - [ ] 500 GB  - [ ] 1 PB
    - *3,000 GB is about 3 TB, so 2 TB is too small and 4 TB fits. 500 GB is far too small. 1 PB (about 1,000 TB) would fit but is huge overkill and data-centre sized. Hook: about 1,000 GB = 1 TB.*
    - @1.3.storage
13. Which item would MOST likely be measured in megabytes (MB)?
    - **[x] A single photo taken on a phone**  - [ ] A company data centre's total storage  - [ ] A home internet connection speed  - [ ] The speed of a processor
    - *Phone photos are usually a few MB. A data centre is measured in PB. Internet speed is in bits per second (Mbps), and processor speed is in GHz. Hook: small files KB, photos and songs MB, movies GB, drives TB, data centres PB.*
    - @1.3.storage
14. A video streaming company stores the whole of its film library across many servers. Which unit BEST describes that total storage?
    - **[x] Petabytes (PB)**  - [ ] Megabytes (MB)  - [ ] Kilobytes (KB)  - [ ] Gigahertz (GHz)
    - *Huge libraries run to thousands of terabytes, which is petabytes. MB and KB are for single files. GHz measures processor speed, not storage. Analogy: if a TB is a bookshelf, a PB is a whole library building.*
    - @1.3.storage
15. A laptop has 16 GB of memory and a 1 TB drive. The owner asks which is bigger. What is the BEST answer?
    - **[x] The 1 TB drive, since 1 TB is about 1,000 GB**  - [ ] The 16 GB memory, since 16 is more than 1  - [ ] They are the same size  - [ ] They cannot be compared because the units differ
    - *1 TB is roughly 1,000 GB (1,024 in binary), so 1 TB is about 60 times 16 GB. Comparing just the numbers ignores the unit, a common trap. GB and TB are both bytes, so they can be compared.*
    - @1.3.storage
16. An internet plan is advertised as "500 Mbps". What does the unit measure?
    - **[x] Megabits per second of data transfer**  - [ ] Megabytes of total storage  - [ ] Megahertz of processor speed  - [ ] Megabytes per month allowance
    - *Mbps = megabits per second, a throughput (speed) measure. Network speeds use small b, bits. Storage uses big B, bytes. MHz is clock speed. Hook: "ps" means per second, so it is a rate, not an amount.*
    - @1.3.thru
17. Two ISPs both quote "100". One says 100 Mbps and the other 100 MBps. Which is TRUE?
    - **[x] 100 MBps is about 8 times faster than 100 Mbps**  - [ ] They are exactly the same speed  - [ ] 100 Mbps is 8 times faster than 100 MBps  - [ ] 100 MBps is about 1,000 times faster
    - *Small b is bits, big B is bytes, and a byte is 8 bits, so 100 MBps = 800 Mbps. Ads nearly always use bits (Mbps), so watch the case of the B. Hook: Big B, Bigger number.*
    - @1.3.thru
18. Joe downloads an 800 megabit file on a steady 100 Mbps connection. About how long does it take, ignoring overhead?
    - **[x] 8 seconds**  - [ ] 80 seconds  - [ ] 0.8 seconds  - [ ] 64 seconds
    - *Both are in megabits, so 800 / 100 = 8 seconds. 80 and 0.8 are decimal-point slips; 64 multiplies by 8 when no bit/byte conversion is needed. Analogy: filling an 800 litre tank at 100 litres per second.*
    - @1.3.thru
19. A small office is choosing a wired network upgrade. Which speed is the FASTEST?
    - **[x] 10 Gbps**  - [ ] 1,000 Mbps  - [ ] 100 Mbps  - [ ] 900 Kbps
    - *10 Gbps = 10,000 Mbps. 1,000 Mbps is only 1 Gbps. 900 Kbps is under 1 Mbps. Hook: Kbps, Mbps, Gbps, Tbps each about 1,000 times the last. Do not be fooled by the bigger raw number 1,000.*
    - @1.3.thru
20. Which link speed would MOST likely be found on an internet backbone between data centres, rather than in a home?
    - **[x] Terabits per second (Tbps)**  - [ ] Kilobits per second (Kbps)  - [ ] Megabits per second (Mbps)  - [ ] Bits per second (bps)
    - *Backbone and undersea links carry huge traffic, measured in Tbps. Homes are usually in Mbps or low Gbps. Kbps is old dial-up territory. bps is the base unit, far too small. Analogy: a home line is a driveway; a backbone is a 20-lane motorway.*
    - @1.3.thru
21. A user complains that a "56 Kbps" modem is slow. How does that compare with a 1 Mbps link?
    - **[x] The 1 Mbps link is roughly 18 times faster**  - [ ] The modem is faster because 56 is bigger than 1  - [ ] They are about the same  - [ ] The 1 Mbps link is 1,000 times faster
    - *1 Mbps = 1,000 Kbps, and 1,000 / 56 is about 18. Comparing raw numbers without units is the trap. 1,000 times would be 1 Gbps.*
    - @1.3.thru
22. A laptop spec sheet says "Processor: 3.2 GHz". What does that figure describe?
    - **[x] The processor's clock speed, about 3.2 billion cycles per second**  - [ ] The processor's memory size in gigabytes  - [ ] The laptop's Wi-Fi download speed  - [ ] The amount of data the CPU can store
    - *GHz (gigahertz) is billions of cycles per second, the CPU's clock speed. Memory is GB, network speed is Gbps or Mbps. The CPU does not store data long term. Analogy: a metronome ticking 3.2 billion times a second.*
    - @1.3.speed
23. What is 2.4 GHz expressed in MHz?
    - **[x] 2,400 MHz**  - [ ] 240 MHz  - [ ] 24,000 MHz  - [ ] 2.4 MHz
    - *1 GHz = 1,000 MHz, so 2.4 x 1,000 = 2,400 MHz. The other options are decimal point slips. Hook: giga is a thousand mega.*
    - @1.3.speed
24. Two otherwise similar older PCs are compared. One CPU runs at 800 MHz, the other at 2 GHz. Which statement is MOST accurate?
    - **[x] The 2 GHz CPU has the higher clock speed, 2,000 MHz vs 800 MHz**  - [ ] The 800 MHz CPU is faster since 800 is bigger than 2  - [ ] They run at the same speed  - [ ] GHz and MHz cannot be compared
    - *Convert to the same unit: 2 GHz = 2,000 MHz, more than 800 MHz. The trap is comparing the bare numbers. Both are hertz, so they compare directly.*
    - @1.3.speed
25. A shop lists four specs on a phone box. Which pairing of item and unit is CORRECT?
    - **[x] Processor speed - GHz**  - [ ] Broadband speed - GB  - [ ] Photo size - Mbps  - [ ] Storage capacity - MHz
    - *CPU clock speed is in GHz. Broadband speed is bits per second (Mbps), photo size is bytes (MB) and storage capacity is bytes (GB or TB). Hook: Hz = how fast it ticks, bps = how fast data flows, B = how much it holds.*
    - @1.3.speed
26. Which TWO describe a rate rather than an amount? (Select 2)
    - **[x] 300 Mbps**  - **[x] 3.5 GHz**  - [ ] 2 TB  - [ ] 512 GB
    - *Mbps is data per second (throughput) and GHz is cycles per second (clock speed), both rates. TB and GB are amounts of storage. Hook: "per second" or hertz = a rate; bytes alone = a bucket size.*
    - @1.3.thru
27. Binary 111 is the largest value three bits can show. What is it in decimal?
    - [=] 7 | seven
    - *111 = 4 + 2 + 1 = 7. Three bits give 8 combinations (0-7), which is why one octal digit maps to exactly three bits. 8 is the slip of counting combinations instead of the top value.*
    - @1.2.nota
28. What is hexadecimal 10 in decimal?
    - **[x] 16**  - [ ] 10  - [ ] 2  - [ ] 8
    - *In any base, "10" equals the base, so hex 10 = 16. Binary 10 would be 2 and octal 10 would be 8. Reading it as plain decimal 10 is the trap.*
    - @1.2.nota
29. A teacher asks which number system people use every day for money and prices. Which is it?
    - **[x] Decimal**  - [ ] Hexadecimal  - [ ] Binary  - [ ] Octal
    - *Decimal (base 10, digits 0-9) is everyday counting, likely from ten fingers. Computers work in binary internally and show hex to humans for short forms. Octal appears mainly in older systems and file permission codes.*
    - @1.2.nota
30. A phone shows "Storage: 128 GB, 4 GB used by photos". Roughly how much space is free?
    - **[x] 124 GB**  - [ ] 132 GB  - [ ] 124 MB  - [ ] 12.4 GB
    - *128 - 4 = 124 GB. Adding instead of subtracting gives 132. Switching to MB or moving the decimal point changes the size by a factor of about 1,000 or 10.*
    - @1.3.storage
31. A USB stick holds 64 GB and each photo is about 4 MB. Roughly how many photos will fit, using 1 GB = about 1,000 MB?
    - **[x] About 16,000**  - [ ] About 16  - [ ] About 1,600  - [ ] About 256
    - *64 GB = about 64,000 MB, and 64,000 / 4 = 16,000. 16 comes from dividing 64 by 4 without converting GB to MB. 256 multiplies instead of dividing. Hook: convert to the same unit first, then divide.*
    - @1.3.storage

## Test 2 - 1.1 + 1.4 How Computers Work + Troubleshooting Steps (31 Q)

1. A cashier scans a barcode, the till looks up the price, the screen shows it and the sale is saved to a database. Which order of the computing cycle is shown?
   - **[x] Input, processing, output, storage**  - [ ] Processing, input, storage, output  - [ ] Input, output, processing, storage  - [ ] Storage, input, processing, output
   - *Scan = input, look up = processing, screen = output, saved = storage. Hook: IPOS. Analogy: a kitchen: ingredients in, cooking, plate served, leftovers in the fridge.*
   - @1.1.ipos
2. During a video call, which device acts as INPUT?
   - **[x] Webcam**  - [ ] Speakers  - [ ] Monitor  - [ ] Printer
   - *A webcam sends images into the computer, so input. Speakers, monitor and printer all send results out to the user, so output. Hook: input = into the computer.*
   - @1.1.ipos
3. Which component does most of the PROCESSING in a computer?
   - **[x] CPU**  - [ ] Hard drive  - [ ] Keyboard  - [ ] Monitor
   - *The CPU (Central Processing Unit) runs instructions and works on data. The drive stores, the keyboard inputs and the monitor outputs. Analogy: the CPU is the chef; everything else delivers ingredients or serves the plate.*
   - @1.1.ipos
4. A user writes a report and wants it to still be there after shutting down the PC. Which part of the computing cycle covers this?
   - **[x] Storage, such as saving to an SSD**  - [ ] Processing in the CPU  - [ ] Output to the monitor  - [ ] Input from the keyboard
   - *Storage keeps data for later, even with power off (an SSD or hard drive). Processing changes data but does not keep it. Output only shows it. Analogy: storage is a filing cabinet; the screen is just a noticeboard.*
   - @1.1.ipos
5. Which TWO devices are used for OUTPUT? (Select 2)
   - **[x] Printer**  - **[x] Speakers**  - [ ] Microphone  - [ ] Scanner
   - *Printers and speakers deliver results to people. Microphones and scanners bring sound or images in, so they are input. Hook: if it reaches your eyes or ears, it is output.*
   - @1.1.ipos
6. A touchscreen on a tablet both shows pictures and senses taps. How is it BEST classified?
   - **[x] Both an input and an output device**  - [ ] Only an input device  - [ ] Only an output device  - [ ] A storage device
   - *The display shows output and the touch layer takes input. Calling it only one ignores half its job. It does not keep data, so it is not storage. Other examples: a headset with mic, a multifunction printer that also scans.*
   - @1.1.ipos
7. Nina brightens a photo in an editing app. The CPU changing the pixel values is which step?
   - **[x] Processing**  - [ ] Input  - [ ] Output  - [ ] Storage
   - *Changing or calculating data is processing. Loading the photo was input and saving it later will be storage. The screen showing the brighter photo is output.*
   - @1.1.ipos
8. A smart thermostat reads the room temperature, decides to turn on the heat, lights up a "Heating" icon and logs the reading. Which part is OUTPUT?
   - **[x] Lighting up the "Heating" icon**  - [ ] Reading the room temperature  - [ ] Deciding to turn on the heat  - [ ] Logging the reading
   - *Showing the icon gives a result to the user, so output. Reading the sensor is input, deciding is processing and logging is storage. IPOS applies to any computing device, not just PCs.*
   - @1.1.ipos
9. A user's PC suddenly can't print. What should a technician do FIRST?
   - **[x] Identify the problem by asking the user questions and finding what changed**  - [ ] Replace the printer driver  - [ ] Order a new printer  - [ ] Write the fix in the ticket
   - *Step 1 is identify the problem: gather information, question the user, check for recent changes. Replacing drivers or hardware jumps to a fix with no theory. Documenting comes last. Analogy: a doctor asks about symptoms before prescribing.*
   - @1.4.steps
10. Which is the correct order of the troubleshooting steps?
    - **[x] Identify, theory, test, plan and implement, verify, document**  - [ ] Identify, test, theory, plan and implement, document, verify  - [ ] Theory, identify, test, verify, plan and implement, document  - [ ] Identify, theory, plan and implement, test, verify, document
    - *Identify the problem, establish a theory of probable cause, test the theory, establish a plan of action and implement it, verify full system function with preventive measures, then document. Hook: "I Think Test Plans Verify Docs". Testing must come before the fix plan, not after.*
    - @1.4.steps
11. Mia's laptop won't power on. The charger light is off, so she suspects the charger. Which step is she on?
    - **[x] Establish a theory of probable cause**  - [ ] Identify the problem  - [ ] Test the theory  - [ ] Verify full system function
    - *Suspecting a likely cause is forming a theory. She has not yet tried a different charger, which would be testing. Identifying was noting it won't power on.*
    - @1.4.steps
12. A monitor shows no picture. The tech checks that it is plugged in and switched on before opening the PC. Which principle is this?
    - **[x] Question the obvious**  - [ ] Document findings  - [ ] Escalate the problem  - [ ] Verify full system function
    - *When forming a theory, check the simple causes first: power, cables, switches. It is quick and often the answer. Opening the PC first wastes time. Analogy: check the car has fuel before calling a mechanic.*
    - @1.4.steps
13. A tech sees an unfamiliar error code. What is the BEST way to research it while forming a theory?
    - **[x] Search the vendor knowledge base and trusted internet sources**  - [ ] Reinstall the operating system right away  - [ ] Guess and replace the most expensive part  - [ ] Close the ticket and wait for it to recur
    - *Researching the knowledge base or internet is part of establishing a theory. Reinstalling or replacing parts skips straight to fixes and can lose data or money. Closing the ticket leaves the user stuck.*
    - @1.4.steps
14. A tech swaps in a known-good charger and the laptop now powers on. What has she just done?
    - **[x] Tested the theory, and it was confirmed**  - [ ] Documented the findings  - [ ] Identified the problem  - [ ] Added preventive measures
    - *Trying a known-good part tests the theory. Now she can plan and implement the fix, such as ordering a new charger. Documenting and preventive measures come later.*
    - @1.4.steps
15. A tech tests her theory that the network cable is faulty, but a new cable doesn't help. What should she do NEXT?
    - **[x] Establish a new theory, researching or escalating if needed**  - [ ] Document that the cable was the cause  - [ ] Tell the user it is fixed  - [ ] Verify full system function
    - *A failed test sends you back to form a new theory. Documenting a wrong cause or claiming a fix would mislead. Verifying only follows a fix. Analogy: a detective drops one suspect and looks at the next.*
    - @1.4.steps
16. Leo has confirmed that a loose cable stopped his printer. What is his NEXT step?
    - **[x] Establish a plan of action and implement the fix**  - [ ] Identify the problem  - [ ] Document the findings  - [ ] Establish a theory of probable cause
    - *Once the theory is confirmed, plan the fix and carry it out, here reseating the cable. Identifying and theorising are already done; documenting is last.*
    - @1.4.steps
17. Before replacing a shared office printer during working hours, what should a tech consider as part of the plan of action?
    - **[x] How the change affects users and when to do it**  - [ ] Which ticket notes to delete afterwards  - [ ] Whether to skip testing the theory  - [ ] How to avoid telling the users
    - *Planning means thinking about the impact and timing of the fix, for example doing it at lunch. Deleting notes, skipping tests or hiding work from users go against the method.*
    - @1.4.steps
18. After fixing a PC, a tech checks that email, printing and the internet all work for the user. Which step is this?
    - **[x] Verify full system function**  - [ ] Test the theory  - [ ] Identify the problem  - [ ] Document findings
    - *Verifying confirms the whole system works after the fix, not just the part that was broken. Testing the theory happened before the fix. Analogy: after fixing a flat tyre you take the car for a short drive.*
    - @1.4.steps
19. A PC kept overheating because its vents were blocked by a stack of papers. After clearing them, what is the BEST preventive measure?
    - **[x] Show the user how to keep the vents clear**  - [ ] Replace the CPU  - [ ] Close the ticket without comment  - [ ] Reinstall the operating system
    - *Preventive measures, part of the verify step, stop it happening again: here, user education. Replacing the CPU or reinstalling the OS do not address the cause.*
    - @1.4.steps
20. Why is the final step, documenting findings, actions and outcomes, MOST useful?
    - **[x] It helps anyone facing the same problem fix it faster later**  - [ ] It proves the user caused the problem  - [ ] It replaces the need to verify the fix  - [ ] It is only needed when the fix fails
    - *Documentation builds a knowledge base so the next tech can solve it quickly. It is not about blame and does not replace verifying. Document every fix, not only failures. Analogy: a recipe card so you never have to work out the dish again.*
    - @1.4.steps
21. Raj has fixed the issue. Which TWO steps are still to come? (Select 2)
    - **[x] Verify full system function and add preventive measures**  - **[x] Document findings, actions and outcomes**  - [ ] Identify the problem  - [ ] Test the theory
    - *After plan and implement come verify, then document. Identifying and testing are done before the fix. Hook: fix, check, write it down.*
    - @1.4.steps
22. Priya's printer stopped working and a colleague suggests buying a new one immediately. Why is that a poor first move?
    - **[x] It skips identifying the problem and testing a theory, so the money may be wasted**  - [ ] Buying parts is always the final step  - [ ] New printers never fix printing problems  - [ ] It must be documented before it can be bought
    - *Buying parts is not a troubleshooting step on its own. Without identifying and testing a cause, the real fault might be a cable or paper jam. The method protects time and money.*
    - @1.4.steps
23. A user says "The internet is broken." The tech asks, "Did anything change just before this started?" Which step is this question part of?
    - **[x] Identify the problem**  - [ ] Test the theory  - [ ] Verify full system function  - [ ] Document findings
    - *Asking about recent changes gathers information, part of identifying the problem. It also helps form a theory later. Testing would involve trying something.*
    - @1.4.steps
24. Several users in one office lose network access at the same time. What does this MOST likely suggest while identifying the problem?
    - **[x] A shared cause, such as a switch or router, rather than one PC**  - [ ] Each PC has a separate faulty cable  - [ ] All users mistyped their passwords  - [ ] The monitors are faulty
    - *Gathering symptoms includes seeing who is affected. Many users at once points to something they share. Separate failures at the same moment are unlikely, and monitors have nothing to do with network access.*
    - @1.4.steps
25. Which troubleshooting step comes just BEFORE verifying full system function?
    - **[x] Establish a plan of action and implement the solution**  - [ ] Test the theory  - [ ] Document findings  - [ ] Establish a theory of probable cause
    - *You can only verify after you have implemented a fix. Testing the theory and forming it come earlier; documenting comes after verifying.*
    - @1.4.steps
26. A scanner copies a paper photo into a computer. Which step of the computing cycle is the scanner doing?
    - **[x] Input**  - [ ] Output  - [ ] Processing  - [ ] Storage
    - *A scanner turns paper into digital data going into the computer, so input. A printer does the opposite, output. Hook: scanner in, printer out.*
    - @1.1.ipos
27. A user says their keyboard isn't working. Why should the tech check that it is plugged in BEFORE reinstalling drivers?
    - **[x] Simple causes are common and quick to rule out**  - [ ] Driver problems never happen  - [ ] Checking cables means the theory does not need testing  - [ ] It means the fix will not need documenting
    - *Questioning the obvious saves time: a loose plug takes seconds to check, a driver reinstall takes much longer. Complex causes do happen, and every theory still needs testing and every fix documenting.*
    - @1.4.steps
28. A tech has tried several theories and none work. The issue is beyond her skills. What is the BEST action?
    - **[x] Escalate to a more experienced tech or vendor**  - [ ] Close the ticket as resolved  - [ ] Keep guessing and replacing parts  - [ ] Skip to documenting a likely cause
    - *If no theory is confirmed, establish a new theory or escalate. Closing the ticket or documenting an unproven cause misleads the next person. Random part swaps waste money.*
    - @1.4.steps
29. Which device is used for STORAGE, keeping data when the computer is turned off?
    - **[x] Solid-state drive (SSD)**  - [ ] CPU  - [ ] Monitor  - [ ] Mouse
    - *An SSD keeps data with the power off. The CPU processes, the monitor outputs and the mouse inputs. Analogy: storage is a notebook you can close and reopen tomorrow.*
    - @1.1.ipos
30. Sam says into his phone, "Set a timer for ten minutes." The phone hears him, works out the request, shows the countdown and saves it to the alarms list. Which part is INPUT?
    - **[x] The microphone picking up his voice**  - [ ] Working out the request  - [ ] Showing the countdown  - [ ] Saving it to the alarms list
    - *Voice into the microphone is input. Working it out is processing, the countdown on screen is output and saving to the list is storage.*
    - @1.1.ipos
31. A tech fixes a user's slow PC by removing a startup program. Before closing the ticket, what should she do LAST?
    - **[x] Document the problem, the fix and the outcome**  - [ ] Establish a theory of probable cause  - [ ] Identify the problem again  - [ ] Test the theory
    - *Documenting is the final step, after verifying the PC runs well. The other steps all come before the fix. Hook: if it is not written down, it did not happen.*
    - @1.4.steps

## Test 3 - 2.1 Computing Devices + Internet of Things (19 Q)

1. A nurse wants a light device for reading long manuals on night shifts. Battery life and an easy-on-the-eyes screen matter more than apps. Which is the BEST fit?
   - **[x] E-reader**  - [ ] Gaming console  - [ ] Workstation  - [ ] Smartwatch
   - *An e-reader is built for one job, reading, with a paper-like screen and long battery life. Hook: E-READER = electronic reader. Analogy: a pocket library that only does books. A smartwatch is portable but far too small to read manuals; a workstation and console stay put.*
   - @2.1.dev
2. A small firm needs one always-on machine that hosts its website and shared files for 40 staff. Which device type should it buy?
   - **[x] Server**  - [ ] Workstation  - [ ] Laptop  - [ ] Tablet
   - *A server SERVES many users at once and is built to run all day. Analogy: a waiter serving many tables. A workstation is powerful too, but it is built for one person at a desk, not for serving 40 people.*
   - @2.1.dev
3. Ana does 3D modelling and video rendering at her desk all day. Which device type MOST suits her?
   - **[x] Workstation**  - [ ] Server  - [ ] Tablet  - [ ] E-reader
   - *A workstation is a high-powered desktop for heavy single-user work like design and editing. Analogy: a professional kitchen versus a camping stove. A server is powerful but meant to serve others over the network, not for one person's creative work. A tablet is too weak.*
   - @2.1.dev
4. A pilot school wants trainees to practise emergencies in a fully computer-generated cockpit, with the real room hidden. Which technology fits?
   - **[x] Virtual reality**  - [ ] Augmented reality  - [ ] A streaming media stick  - [ ] A smart home assistant
   - *VR replaces the real world with a fully digital one. Hook: VR replaces, AR adds. Analogy: a flight simulator you wear on your head. AR is tempting but keeps the real world visible and adds items on top.*
   - @2.1.dev
5. A furniture shop's app lets customers point their phone camera at their room and see a new sofa placed in it. What is this?
   - **[x] Augmented reality**  - [ ] Virtual reality  - [ ] Home automation  - [ ] Casting
   - *AR adds digital objects over the real view. Hook: AR = Add to Reality. Analogy: sticky notes on your window. VR would hide the room entirely, which defeats the point of seeing the sofa in it.*
   - @2.1.dev
6. Joe travels for work and wants ONE small device for calls, email, maps and reading. Which is the BEST choice?
   - **[x] Smartphone**  - [ ] Laptop  - [ ] E-reader  - [ ] Workstation
   - *A smartphone is a pocket computer that also makes calls. Analogy: a Swiss army knife in your pocket. A laptop does email but is not a phone and not pocket-sized. An e-reader is mostly for books.*
   - @2.1.dev
7. A student wants a portable computer with a built-in physical keyboard for typing long essays in the library. Which device type fits BEST?
   - **[x] Laptop**  - [ ] Tablet  - [ ] Smartphone  - [ ] Gaming console
   - *A laptop has keyboard, screen and battery in one folding case. Analogy: a briefcase office. A tablet is tempting as portable, but it is mainly a touch screen with no built-in keyboard.*
   - @2.1.dev
8. A shop wants staff to show customers a large touch-screen catalogue while walking the floor, without a keyboard in the way. Which device fits BEST?
   - **[x] Tablet**  - [ ] Laptop  - [ ] Workstation  - [ ] Server
   - *A tablet is a flat touch-screen device, bigger than a phone, normally without a built-in keyboard. Analogy: a large notepad you tap. A laptop would work but is awkward to hold standing up; a workstation is not portable.*
   - @2.1.dev
9. A family wants a device mainly for playing games on the living-room TV with controllers. Which device type is this?
   - **[x] Gaming console**  - [ ] Workstation  - [ ] Server  - [ ] Streaming media stick
   - *A gaming console is built for games on a TV. A streaming stick also plugs into the TV, but it plays online shows, not console games with controllers. A workstation could run games but is a desk work machine.*
   - @2.1.dev
10. Tom forgot to turn his heating down before a week away. Which device would let him fix this from his phone?
    - **[x] Smart thermostat**  - [ ] Smart door lock  - [ ] Video doorbell  - [ ] Fitness tracker
    - *A smart thermostat is an IoT (Internet of Things) home automation device controlled from an app. Hook: IoT = everyday things on the internet. Analogy: a heating remote that works from anywhere. The lock and doorbell are home automation too, but they do not control heating.*
    - @2.1.iot
11. Kim wants to let a dog walker in while she is at work, without hiding a key. What should she install?
    - **[x] Smart door lock**  - [ ] Smart thermostat  - [ ] Streaming media device  - [ ] Home assistant speaker
    - *A smart lock or deadbolt can be unlocked from an app, often with temporary codes. Analogy: handing over a key from miles away. A home assistant may control a lock, but on its own it cannot unlock a door.*
    - @2.1.iot
12. Lisa wants to see and talk to whoever is at her front door from her phone. Which device is BEST?
    - **[x] Video doorbell**  - [ ] Streaming stick  - [ ] Smart thermostat  - [ ] E-reader
    - *A video doorbell is an IoT security device with camera, mic and phone alerts. Analogy: a peephole you can look through from anywhere. A streaming stick handles video too, but it plays shows on a TV.*
    - @2.1.iot
13. A café owner wants to watch the till area live from home over the internet. Which device should she use?
    - **[x] IP security camera**  - [ ] Home assistant  - [ ] Smart thermostat  - [ ] Streaming media stick
    - *An IP (Internet Protocol) camera sends video over the network so it can be viewed remotely. Analogy: a guard's monitor in your pocket. A streaming stick shows video on a TV; it does not capture it.*
    - @2.1.iot
14. Which device is BEST described as an IoT medical device?
    - **[x] A glucose monitor that sends readings to the patient's phone**  - [ ] A treadmill that uploads runs to a training app  - [ ] A smartwatch that shows text messages  - [ ] A speaker that reads out the weather
    - *Medical IoT devices track health for patients or doctors. Analogy: a nurse who texts you your results. The treadmill is exercise equipment and the watch is a wearable: both health-ish, but not medical devices.*
    - @2.1.iot
15. Which two items are IoT devices rather than general-purpose computing devices? (Select 2)
    - **[x] A fridge that alerts you when milk runs low**  - **[x] A car that downloads map updates and reports faults**  - [ ] A laptop used for school work  - [ ] A workstation used for video editing
    - *IoT means ordinary things (appliances, vehicles) that connect to a network. The fridge is a home appliance; the car is an IoT vehicle. Laptops and workstations are computers by design, so they are computing devices, not IoT "things".*
    - @2.1.iot
16. A household has a smart thermostat, a smartwatch, a tablet and a desktop tower. Which item is a WEARABLE?
    - **[x] Smartwatch**  - [ ] Smart thermostat  - [ ] Tablet  - [ ] Desktop tower
    - *A wearable is worn on the body, like a smartwatch or fitness band. Wearables are a kind of IoT, but "wearable" is the more specific label. The thermostat is IoT home automation; the tablet is a mobile device; the desktop is a workstation.*
    - @2.1.iot
17. A gym member's exercise bike shares her ride stats with an online app. Which IoT category is this?
    - **[x] Exercise equipment**  - [ ] Medical device  - [ ] Home automation  - [ ] Security system
    - *Connected treadmills and bikes are IoT exercise equipment. Analogy: a coach logging every ride. Medical device is tempting because it involves health, but medical IoT is for health care, such as heart or glucose monitors.*
    - @2.1.iot
18. A family wants to say "turn off the lights" and "play the news" to one device in the kitchen. What should they buy?
    - **[x] A home assistant smart speaker**  - [ ] A streaming media stick  - [ ] A video doorbell  - [ ] A gaming console
    - *A home assistant is a voice-controlled IoT hub that can answer questions and control other smart devices. Analogy: a butler who listens for your call. A streaming stick plays shows on a TV, it does not take voice commands for the lights.*
    - @2.1.iot
19. Raj plugs a small stick into his TV's HDMI port so it can play shows from online services over his Wi-Fi. Which IoT category is this?
    - **[x] Streaming media device**  - [ ] Home assistant  - [ ] Security camera  - [ ] Wearable
    - *A streaming stick or box connects the TV to the internet to play online video, making it an IoT streaming media device. A security camera captures video rather than playing it, and a home assistant is a voice hub.*
    - @2.1.iot

### Key facts
- **VR = fully digital world (replaces) · AR = digital items over the real world (adds)**
- **Server serves many users · workstation = powerful one-user desk computer · tablet = touch, no keyboard · e-reader = made for books**
- **IoT = everyday things online: appliances, thermostats, locks, doorbells, home assistants, cameras, cars, streaming, medical, exercise, wearables**

## Test 4 - 2.2 Inside the Computer: Motherboard, CPU, RAM, Network Card (20 Q)

1. A technician is building a PC. Which part must be chosen FIRST because the CPU, RAM and expansion cards all plug into it?
   - **[x] Motherboard**  - [ ] Power supply  - [ ] Network card  - [ ] Storage drive
   - *The motherboard (system board) connects every part so they can talk; the CPU socket and RAM slots must match it. Hook: MOTHER holds the whole family. Analogy: the street map linking every house. A network card plugs into the motherboard, not the other way round.*
   - @2.2.board
2. Sam wants his PC to boot from a USB stick before the hard drive. Where should he change this?
   - **[x] The BIOS/UEFI setup screen**  - [ ] The Windows Control Panel  - [ ] The web browser settings  - [ ] The network card properties
   - *The BIOS (Basic Input/Output System) or UEFI firmware runs before the OS and controls boot order. Analogy: choosing which door to enter before you go in. Windows settings load too late to pick what boots first.*
   - @2.2.board
3. Which statement BEST describes firmware such as the BIOS?
   - **[x] Software stored on a chip on the hardware itself**  - [ ] An app installed from the operating system store  - [ ] A cable that links the CPU to memory  - [ ] Temporary data held in RAM while running
   - *Firmware is low-level software kept on a chip in the device, so it is there before any drive is read. Hook: FIRM = fixed between hard and soft. Analogy: instructions printed inside a washing machine lid. It is not an OS app and not volatile RAM data.*
   - @2.2.board
4. A PC powers on but gives beeps and never shows the boot screen, even with the drive removed. Which component's start-up code runs FIRST and is reporting the fault?
   - **[x] The BIOS/UEFI firmware on the motherboard**  - [ ] The operating system on the drive  - [ ] The web browser's cache  - [ ] The printer driver
   - *Firmware checks the hardware before any OS loads, which is why it still runs with the drive removed. Analogy: the caretaker who unlocks the building before staff arrive. The OS lives on the drive, so it cannot be what is running here.*
   - @2.2.board
5. Which two components sit directly on the motherboard rather than outside the case? (Select 2)
   - **[x] CPU**  - **[x] RAM**  - [ ] Monitor  - [ ] Printer
   - *The CPU sits in its socket and RAM in its slots on the motherboard. Monitors and printers are external peripherals connected by cable. Analogy: rooms inside the house versus cars parked outside.*
   - @2.2.board
6. A manufacturer releases a fix for a motherboard boot bug. What must the user update?
   - **[x] The firmware (BIOS/UEFI)**  - [ ] The RAM modules  - [ ] The GPU driver only  - [ ] The web browser
   - *Boot behaviour lives in motherboard firmware, so the fix is a firmware/BIOS update. A GPU driver controls the graphics card inside the OS, not the boot. Swapping RAM changes hardware, not code.*
   - @2.2.board
7. Which component carries out program instructions and is often called the brain of the computer?
   - **[x] CPU**  - [ ] GPU  - [ ] RAM  - [ ] NIC
   - *The CPU (Central Processing Unit) fetches and runs instructions; its speed is quoted in GHz. Analogy: the head chef. The GPU is a processor too, but it specialises in graphics.*
   - @2.2.comp
8. Priya's laptop slows to a crawl when she has 40 browser tabs and a spreadsheet open, but is fine with a few. Which upgrade will help MOST?
   - **[x] More RAM**  - [ ] A faster network card  - [ ] A larger monitor  - [ ] A firmware update
   - *RAM (Random Access Memory) holds open programs and data. When it is full, the system crawls. Analogy: a bigger desk so more papers fit at once. A faster NIC speeds downloads, not juggling open tabs.*
   - @2.2.comp
9. A gamer gets choppy frame rates in new 3D games, while the CPU is mostly idle. Which part should he upgrade FIRST?
   - **[x] GPU**  - [ ] NIC  - [ ] Storage drive  - [ ] RAM speed only
   - *The GPU (Graphics Processing Unit) draws the images, so it limits 3D games. Hook: G for Graphics. Analogy: a better artist paints scenes faster. The CPU being idle shows it is not the bottleneck.*
   - @2.2.comp
10. Why does a computer need BOTH RAM and a storage drive?
    - **[x] RAM is fast working space that empties at power off; storage keeps files**  - [ ] RAM keeps files long term; storage runs the programs  - [ ] They do the same job and one is a spare  - [ ] Storage is only used when RAM fails
    - *They work together: RAM is the desk, storage is the filing cabinet. Programs load from storage into RAM so the CPU can work fast. The other options reverse or confuse these roles.*
    - @2.2.comp
11. A laptop spec sheet lists "CPU 3.8 GHz, RAM 16 GB, SSD 512 GB, GPU 8 GB". Which line describes the part that holds open programs while they run?
    - **[x] RAM 16 GB**  - [ ] CPU 3.8 GHz  - [ ] SSD 512 GB  - [ ] GPU 8 GB
    - *RAM is the working memory for open programs. The CPU runs the instructions, the SSD keeps files long term and the GPU's memory is for graphics. Analogy: RAM is the desk, the SSD the filing cabinet.*
    - @2.2.comp
12. A user double-clicks an app saved on the SSD. Where is it copied so the CPU can work with it quickly?
    - **[x] RAM**  - [ ] The GPU  - [ ] The NIC  - [ ] The BIOS chip
    - *Programs load from storage into RAM because RAM is much faster for the CPU to read and write. The BIOS chip holds start-up firmware, not apps, and the NIC handles network traffic.*
    - @2.2.comp
13. A user's laptop says "Disk full" and she cannot save any more videos, though it runs open apps smoothly. Which component should be upgraded?
    - **[x] The storage drive, to a larger capacity**  - [ ] RAM  - [ ] The CPU  - [ ] The GPU
    - *Saved files live on the storage drive, so a bigger drive gives room for more videos. More RAM helps with many open programs, not with saved files. The CPU and GPU do not hold files.*
    - @2.2.comp
14. A support script says "RAM, CPU, GPU, storage". Which pairing is correct?
    - **[x] CPU runs instructions, GPU renders graphics**  - [ ] RAM renders graphics, CPU stores files  - [ ] GPU stores files, storage runs instructions  - [ ] Storage holds open programs, RAM keeps files when off
    - *CPU = general instructions, GPU = graphics, RAM = fast temporary working memory, storage = long-term files. Each wrong option swaps two roles.*
    - @2.2.comp
15. A desktop PC suddenly cannot reach the network, though other PCs on the same switch work. Which component should the technician check FIRST?
    - **[x] The NIC and its cable**  - [ ] The graphics card  - [ ] The RAM modules  - [ ] The CPU cooler
    - *A NIC (Network Interface Card) connects the PC to the network. If only one PC is down, start with its NIC, cable and link light. Analogy: if no mail arrives, check your own letterbox first. GPU and RAM faults show other symptoms.*
    - @2.2.nic
16. Ben's desktop has no Wi-Fi. He wants Wi-Fi without replacing the motherboard. What is the BEST fix?
    - **[x] Install a wireless NIC expansion card in a free slot**  - [ ] Enable the onboard wired NIC  - [ ] Add more RAM  - [ ] Update the GPU driver
    - *An expansion card NIC plugs into a motherboard slot to add a feature. Onboard means already built into the board, and the wired one would still need a cable. Analogy: adding a shelf to a bookcase.*
    - @2.2.nic
17. A laptop's network chip is soldered onto the motherboard and cannot be removed. What type of NIC is this?
    - **[x] Onboard NIC**  - [ ] Expansion card NIC  - [ ] External GPU  - [ ] USB hub
    - *Onboard (integrated) NICs are part of the system board. Hook: ON the board. Analogy: a built-in oven versus one you slot in. An expansion card goes in a slot and can be swapped.*
    - @2.2.nic
18. An office needs its main file-editing PCs to have the MOST reliable, consistent network connection. Which NIC type should they use?
    - **[x] Wired NIC with an Ethernet cable**  - [ ] Wireless NIC on the busiest Wi-Fi band  - [ ] Bluetooth adapter  - [ ] NFC reader
    - *A wired NIC is not affected by walls, distance or radio interference, so it is steadier. Analogy: a landline versus a mobile in a basement. Wireless is convenient but less consistent; Bluetooth and NFC are not for LAN access.*
    - @2.2.nic
19. Eva wants her laptop to use Wi-Fi at home and a cable in the office. What does it need?
    - **[x] Both a wireless NIC and a wired NIC**  - [ ] Two graphics cards  - [ ] Two BIOS chips  - [ ] Extra RAM
    - *Each connection type needs its own interface: wireless for Wi-Fi, wired for an Ethernet cable. Many laptops have both built in or add wired via a USB adapter. Analogy: a front door and a garage door.*
    - @2.2.nic
20. What is the MAIN advantage of an onboard NIC compared with an expansion card NIC?
    - **[x] It is built into the motherboard, so it works without using a slot or adding a card**  - [ ] It is always wireless  - [ ] It can be upgraded by swapping it out  - [ ] It needs no driver on any operating system
    - *Onboard NICs come with the board, saving a slot and cost. Being built in is also why they cannot simply be swapped out; that flexibility belongs to expansion cards. Onboard NICs can be wired or wireless and still use drivers.*
    - @2.2.nic

### Key facts
- **Motherboard = system board, everything plugs in · BIOS/UEFI = firmware on a board chip, runs first, sets boot order**
- **CPU = brain (GHz) · GPU = graphics · RAM = fast temporary memory · storage = keeps files**
- **NIC: wired (cable, steadier) vs wireless (Wi-Fi) · onboard (built in) vs expansion card (added in a slot)**

## Test 5 - 2.3 Storage: Volatile, Local, Network (20 Q)

1. Zoe's PC loses power during a storm. Her saved spreadsheet is fine, but the essay she had not saved is gone. Why?
   - **[x] Unsaved work was only in volatile RAM**  - [ ] The ROM chip erased the essay  - [ ] The SSD is volatile storage  - [ ] The essay was stored on the cloud
   - *Volatile memory needs power to hold data. Hook: volatile = vanishes. Analogy: words on a steamy mirror. The SSD is non-volatile, which is why the saved file survived. ROM does not erase user files.*
   - @2.3.vol
2. Which two are non-volatile? (Select 2)
   - **[x] ROM**  - **[x] HDD**  - [ ] RAM  - [ ] CPU cache
   - *ROM (Read-Only Memory) and an HDD (Hard Disk Drive) keep data without power. RAM and CPU cache are fast working memory that clear at power off. Analogy: carved stone and a printed book last; chalk does not.*
   - @2.3.vol
3. A router's start-up code must survive every power cut and is rarely changed. Where is it BEST kept?
   - **[x] ROM**  - [ ] RAM  - [ ] Cloud storage  - [ ] An optical disc
   - *ROM holds fixed start-up firmware and keeps it with no power. Hook: Read-Only = look, don't touch. RAM would lose it at every reboot. Cloud storage needs a working network first.*
   - @2.3.vol
4. Why do computers run open programs from RAM even though it is volatile?
   - **[x] RAM is far faster for the CPU to work with than a drive**  - [ ] RAM keeps data after shutdown  - [ ] RAM is cheaper per GB than any drive  - [ ] RAM is stored on the internet
   - *Speed is the trade-off: RAM is very fast but temporary. Analogy: a desk is quick to work at but cleared nightly. RAM is actually more expensive per GB than drives, and it does not keep data after shutdown.*
   - @2.3.vol
5. What is the KEY difference between RAM and ROM?
   - **[x] RAM is read-write and volatile; ROM is mostly read-only and non-volatile**  - [ ] RAM is non-volatile; ROM loses data at power off  - [ ] RAM is a storage drive; ROM is a network card  - [ ] Both are volatile but ROM is slower
   - *RAM = working memory, changes constantly, empties at power off. ROM = fixed instructions, kept with no power. Analogy: notepad versus printed book. The wrong options reverse or mislabel the two.*
   - @2.3.vol
6. Which of these is volatile?
   - **[x] The contents of RAM**  - [ ] Files on an SSD  - [ ] Start-up code in ROM  - [ ] Photos on a USB flash drive
   - *Only RAM loses its contents when power goes. SSDs and flash drives also use chips, which tempts people, but flash is non-volatile. ROM keeps firmware without power.*
   - @2.3.vol
7. Max's five-year-old laptop takes three minutes to boot from a spinning HDD. Which upgrade will speed boot up MOST?
   - **[x] Replace the HDD with an SSD**  - [ ] Add an optical drive  - [ ] Add a USB flash drive  - [ ] Swap the keyboard
   - *An SSD (Solid-State Drive) uses flash chips with no moving parts, so it loads the OS far faster than a spinning HDD. Analogy: flipping a switch versus winding a music box. A flash drive is external and not where the OS boots from.*
   - @2.3.local
8. A video editor wants the FASTEST internal drive for working on large files. Which should she choose?
   - **[x] NVMe SSD**  - [ ] HDD  - [ ] Blu-ray drive  - [ ] USB flash drive
   - *NVMe (Non-Volatile Memory Express) SSDs connect straight to fast lanes on the motherboard, beating older SSDs and far beating HDDs. Analogy: a motorway versus a country lane. Optical and flash drives are much slower.*
   - @2.3.local
9. A photographer needs 8TB of local archive space on a tight budget, and speed is not critical. Which is the BEST choice?
   - **[x] HDD**  - [ ] NVMe SSD  - [ ] Optical discs  - [ ] RAM
   - *HDDs (spinning platters) give the most space for the money. Analogy: a big cheap shed versus a small pricey locker. NVMe is faster but costs far more per TB. RAM is volatile and not storage.*
   - @2.3.local
10. A courier keeps dropping his laptop. Which drive type is LEAST likely to be damaged by knocks?
    - **[x] SSD**  - [ ] HDD  - [ ] Optical drive  - [ ] Tape drive
    - *An SSD has no moving parts. An HDD has a spinning platter and moving read arm that can be damaged by a knock while running. Optical and tape drives also have moving parts.*
    - @2.3.local
11. A school needs to give out a training video on discs that play in older DVD players. Which storage type fits?
    - **[x] Optical disc**  - [ ] NVMe SSD  - [ ] NAS  - [ ] RAM
    - *Optical media (CD, DVD, Blu-ray) is read by a laser. Hook: optical = light. A NAS shares files over the network and cannot be posted to a DVD player.*
    - @2.3.local
12. Lily needs to carry project files between school and home computers, with no internet at school. What is the SIMPLEST choice?
    - **[x] USB flash drive**  - [ ] Cloud storage  - [ ] File server  - [ ] Internal HDD
    - *External flash storage is small, plugs in anywhere and keeps data without power. Cloud needs internet, which she lacks at school. A file server is not something she can carry.*
    - @2.3.local
13. A camera stores its photos on a small removable card that can be moved to a laptop. What is this?
    - **[x] External flash storage (SD card)**  - [ ] An internal HDD  - [ ] A ROM chip  - [ ] A NAS device
    - *SD (Secure Digital) cards are removable flash storage. Analogy: a film roll you can swap between cameras. ROM is not user-removable and holds firmware, not photos.*
    - @2.3.local
14. Which option is LOCAL storage, used by one computer only?
    - **[x] An SSD inside the laptop**  - [ ] A shared file server  - [ ] An online cloud drive  - [ ] A NAS on the office network
    - *Local storage sits in or plugs into one machine. NAS, file servers and cloud are all shared over a network. Analogy: your own wallet versus a shared bank.*
    - @2.3.local
15. A family wants every phone and laptop at home to back up photos to one box on the home network, without a monthly fee. What should they buy?
    - **[x] A NAS**  - [ ] A cloud storage subscription  - [ ] A ROM chip  - [ ] More RAM
    - *NAS (Network-Attached Storage) is a box of drives on the local network that many devices share. Analogy: a family bookshelf in the hallway. Cloud storage works but usually has a monthly fee and lives off-site.*
    - @2.3.net
16. A small office wants shared storage that still works if the internet connection goes down. Which is the BEST choice?
    - **[x] NAS or file server on the office LAN**  - [ ] Cloud storage only  - [ ] Each user's RAM  - [ ] A ROM chip
    - *Local network storage is reached over the LAN, so it does not depend on the internet. Analogy: a filing cabinet in the office still opens during a road closure. Cloud storage needs internet access.*
    - @2.3.net
17. Omar wants his files on his phone, laptop and work PC from anywhere in the world. What fits BEST?
    - **[x] Cloud storage**  - [ ] A NAS with no remote access  - [ ] An internal HDD  - [ ] An optical disc
    - *Cloud storage keeps files on a provider's servers, reachable from any device with internet. Analogy: a mailbox you can open at any post office. An internal HDD lives in one computer.*
    - @2.3.net
18. A company already runs a Windows server that holds the department's shared folders with user permissions. What is this machine acting as?
    - **[x] A file server**  - [ ] A NAS appliance  - [ ] A cloud provider  - [ ] A ROM chip
    - *A file server is a full computer whose job is storing and sharing files for many users. A NAS is a dedicated storage box rather than a general server, so NAS is the close distractor.*
    - @2.3.net
19. A family keeps all its backups on a NAS in the house. What risk does ALSO copying them to cloud storage reduce?
    - **[x] A fire or burglary at home destroying both the PCs and the NAS**  - [ ] Losing unsaved work in RAM during a power cut  - [ ] Needing internet access to reach files  - [ ] A slow home Wi-Fi connection
    - *Cloud storage sits on a provider's servers far away, so one event at home cannot wipe out every copy. Cloud does not save unsaved RAM work, and it adds an internet dependency rather than removing one.*
    - @2.3.net
20. Which statement BEST compares NAS and cloud storage?
    - **[x] NAS is on your own local network; cloud is on a provider's servers over the internet**  - [ ] NAS is volatile; cloud is non-volatile  - [ ] NAS reads discs with a laser; cloud uses flash  - [ ] NAS is a CPU; cloud is a GPU
    - *Both keep data without power, so the volatile option is wrong. Location is the difference. Analogy: your garage versus a rented storage unit across town.*
    - @2.3.net

### Key facts
- **Volatile = lost at power off (RAM) · non-volatile = kept (ROM, HDD, SSD, flash)**
- **HDD spins, cheap + big · SSD flash, no moving parts, fast · NVMe = fastest SSD type · optical = laser discs · flash = USB stick, SD card**
- **NAS / file server = shared on the local network · cloud = provider's servers over the internet**

## Test 6 - 2.4 + 2.5 Peripherals, Installation, Cables, Connectors, Displays (25 Q)

1. A small office loses mains power for a few minutes about once a month, and staff lose unsaved work. Which device should be added to each PC?
   - **[x] UPS**  - [ ] NAS  - [ ] Second monitor  - [ ] Projector
   - *A UPS (Uninterruptible Power Supply) has a battery that takes over when mains fails, giving time to save and shut down. Hook: U for Uninterrupted. Analogy: a spare torch that switches on when the lights go out. A NAS stores files but does not keep a PC running.*
   - @2.4.dev
2. An accountant receives paper receipts and needs them as PDF files. Which device should she use?
   - **[x] Scanner**  - [ ] Printer  - [ ] Projector  - [ ] Web camera
   - *A scanner turns paper into a digital file. A printer does the reverse. A web camera can take a picture, but a scanner gives flat, readable documents.*
   - @2.4.dev
3. Sam joins video calls from a desktop that has no camera or microphone. Which two devices should he add? (Select 2)
   - **[x] Web camera**  - **[x] Headset**  - [ ] Scanner  - [ ] Projector
   - *A webcam sends his picture; a headset carries his voice and the call audio. Analogy: a face and a voice to join the conversation. A scanner and projector do neither.*
   - @2.4.dev
4. A teacher needs a 3-metre-wide image on the classroom wall for slides. Which display device fits BEST?
   - **[x] Projector**  - [ ] Monitor  - [ ] Smart watch  - [ ] Web camera
   - *A projector throws a large image onto a wall or screen. A monitor is a desk display and too small for the whole class. A webcam captures images rather than showing them.*
   - @2.4.dev
5. A meeting room wants a large display that can also run streaming apps on its own and accept casts from phones. Which is the BEST fit?
   - **[x] Smart TV**  - [ ] Projector with no inputs  - [ ] VGA monitor  - [ ] Scanner
   - *A smart TV is a display with built-in apps and casting support. A VGA monitor shows only what a PC sends it, with no apps. Analogy: a TV with its own video shop inside.*
   - @2.4.dev
6. Ella plugs in a new printer. Windows detects it but it will not print, and the maker's site offers a download for that model. What should she do FIRST?
   - **[x] Install the maker's printer driver**  - [ ] Buy more RAM  - [ ] Reinstall the web browser  - [ ] Replace the USB cable with HDMI
   - *A driver is software that lets the OS (Operating System) talk to a device. Analogy: a translator between computer and device. If plug-and-play did not fully set it up, the correct driver usually fixes it. RAM and browsers do not teach the PC to use a printer.*
   - @2.4.inst
7. A user plugs in a USB mouse and it works within seconds, with nothing to install. What is this called?
   - **[x] Plug-and-play**  - [ ] Web-based configuration  - [ ] Manual driver installation  - [ ] Casting
   - *Plug-and-play means the OS detects the device and loads a driver by itself. Analogy: plugging in a lamp and it just lights. Manual driver installation is the opposite case.*
   - @2.4.inst
8. A new network printer has an IP address of 192.0.2.25. How does the technician MOST likely change its settings?
   - **[x] Type the IP address into a web browser to open its settings page**  - [ ] Change the boot order in the PC's BIOS  - [ ] Plug it into an HDMI port on a monitor  - [ ] Open the printer's ROM chip with a screwdriver
   - *IP-based peripherals usually have a web-based configuration page reached at their address. Analogy: calling a shop's number to change your order. BIOS settings belong to the PC, not the printer.*
   - @2.4.inst
9. Why might an office choose an IP-based printer over a USB printer?
   - **[x] Many computers can use it over the network**  - [ ] It needs no power cable  - [ ] It never needs a driver  - [ ] It only works with one computer
   - *IP-based peripherals join the network with their own address, so every PC can print to them. Analogy: a shop with a street address anyone can visit. A USB printer serves the one PC it plugs into. IP printers still need power and usually a driver.*
   - @2.4.inst
10. After installing a printer and its driver, what is a sensible step to confirm the job is done?
    - **[x] Print a test page**  - [ ] Delete the driver  - [ ] Restart the internet router  - [ ] Unplug the printer
    - *A test page proves the printer, connection and driver work together. Analogy: after fixing a tap, turn it on to check. Deleting the driver undoes the work; the router is unrelated.*
    - @2.4.inst
11. A technician is wiring a new office wall socket. Which connector goes on the end of a standard copper Ethernet cable?
    - **[x] RJ45**  - [ ] HDMI  - [ ] SFP  - [ ] USB-C
    - *RJ45 (Registered Jack 45) is the clip-in plug on copper network cables. SFP is for fibre modules in switches. HDMI is for video.*
    - @2.5.net
12. A technician has a box of loose RJ45 plugs and a reel of network cable. Which tool does she need to make patch cables?
    - **[x] Crimper**  - [ ] Cable tester  - [ ] Multimeter  - [ ] Label maker
    - *A crimper squeezes the plug onto the wires. Hook: crimp = squeeze. The cable tester is tempting, but it checks a finished cable; it does not attach the plug.*
    - @2.5.net
13. A newly made network cable works only intermittently. What should the technician use FIRST to check every wire is connected?
    - **[x] Cable tester**  - [ ] Crimper  - [ ] Projector  - [ ] Soldering iron
    - *A cable tester sends a signal down each wire to confirm continuity. Analogy: tasting the soup after cooking. The crimper built the cable but cannot tell you if it works.*
    - @2.5.net
14. A switch in a network rack must connect to a fibre optic link to another building. What should be plugged into the switch port?
    - **[x] SFP module**  - [ ] RJ45 plug  - [ ] VGA adapter  - [ ] Lightning cable
    - *An SFP (Small Form-factor Pluggable) module slots into the switch so it can take fibre. Analogy: a travel plug adapter. RJ45 is for copper, not fibre.*
    - @2.5.net
15. A shopper pays by holding her phone a few centimetres from a card reader. Which wireless technology is used?
    - **[x] NFC**  - [ ] Bluetooth  - [ ] 802.11x Wi-Fi  - [ ] RF dongle
    - *NFC (Near Field Communication) works only at tap distance. Hook: NEAR field. Bluetooth reaches around a room, and Wi-Fi (802.11x) a whole building, so neither is the tap-to-pay standard.*
    - @2.5.net
16. A user wants wireless headphones that pair directly with her phone without any dongle. Which interface fits BEST?
    - **[x] Bluetooth**  - [ ] NFC  - [ ] RF with a USB receiver  - [ ] Thunderbolt
    - *Bluetooth pairs devices directly over a short range, around a room. RF devices usually need their own USB receiver dongle. NFC range is only a few centimetres.*
    - @2.5.periph
17. A new wireless mouse comes with a tiny USB receiver that must stay plugged into the laptop. Which interface does it use?
    - **[x] RF**  - [ ] Bluetooth  - [ ] NFC  - [ ] Lightning
    - *RF (Radio Frequency) peripherals talk to their own receiver dongle. Analogy: a toy car with its own remote. Bluetooth is tempting, but it uses the laptop's built-in radio without a dedicated dongle.*
    - @2.5.periph
18. A designer wants ONE port on her laptop to drive a high-resolution dock with displays, fast storage and charging. Which interface is BEST?
    - **[x] Thunderbolt**  - [ ] USB-A  - [ ] Lightning  - [ ] VGA
    - *Thunderbolt is a high-speed interface carrying data, video and power, and newer versions use the USB-C shape. Analogy: one pipe for water, gas and power. Lightning is Apple's phone connector, not a dock interface; USB-A is older and slower.*
    - @2.5.periph
19. Leo needs to charge an iPhone 12 and a modern Android phone. Which pair of connectors does he need?
    - **[x] Lightning for the iPhone 12, USB-C for the Android**  - [ ] USB-C for both phones  - [ ] USB-B for the iPhone, USB-A for the Android  - [ ] HDMI for both phones
    - *iPhones before the iPhone 15 use Lightning; most modern Android phones use USB-C. USB-C is reversible and oval. USB-B is the squarish plug on printers.*
    - @2.5.periph
20. An office printer's cable has a flat rectangular plug at the PC end and a squarish plug at the printer end. Which connectors are these?
    - **[x] USB-A at the PC, USB-B at the printer**  - [ ] USB-C at both ends  - [ ] RJ45 at the PC, SFP at the printer  - [ ] Lightning at the PC, VGA at the printer
    - *USB-A is the classic flat rectangle on computers; USB-B is the squarer device-end plug often on printers. USB-C is smaller, oval and reversible.*
    - @2.5.periph
21. Leo wants ONE cable from his laptop to the living-room TV carrying both picture and sound. What is the MOST common choice?
    - **[x] HDMI**  - [ ] VGA  - [ ] DVI  - [ ] RJ45
    - *HDMI (High-Definition Multimedia Interface) carries digital video and audio and is on almost every TV. VGA (Video Graphics Array) is analog video only, and DVI (Digital Visual Interface) normally carries no sound.*
    - @2.5.display
22. A school has an old projector with only a blue 15-pin video input. Which cable does the teacher need?
    - **[x] VGA**  - [ ] HDMI  - [ ] DisplayPort  - [ ] Lightning
    - *VGA is the old analog connector, often blue with 15 pins. Analogy: a cassette deck next to a streamer. HDMI and DisplayPort are newer digital plugs that will not fit.*
    - @2.5.display
23. A new monitor and the PC's graphics card both have a port with one angled corner, made mainly for computer displays. Which cable should be used?
    - **[x] DisplayPort**  - [ ] USB-B  - [ ] RJ45  - [ ] DVI
    - *DisplayPort is a digital video and audio connector common on monitors and graphics cards, recognised by its angled corner. DVI is also a monitor connector, but it is a wide plug with pins, not angled.*
    - @2.5.display
24. A presenter wants the projector to show EXACTLY what is on her laptop, including her slides and notes window. What should she use?
    - **[x] Mirroring**  - [ ] Casting a single video  - [ ] Crimping  - [ ] Scanning
    - *Mirroring copies the whole screen to the other display. Casting usually sends one video or app to a TV while your device does other things. Analogy: a mirror shows everything; casting hands over one film.*
    - @2.5.display
25. Nina wants to send a film from her phone to the smart TV over Wi-Fi and keep using her phone for messages. What is she doing?
    - **[x] Casting**  - [ ] Mirroring  - [ ] Using a USB-C cable  - [ ] Using a VGA cable
    - *Casting sends media wirelessly to a TV, which then plays it while the phone stays free. Mirroring would show her messages on the TV too. USB-C can carry video, but it is a cable, not over Wi-Fi.*
    - @2.5.display

### Key facts
- **UPS = battery time in a power cut · plug-and-play = auto setup · driver = software so the OS can use the device · IP devices: settings page at their IP in a browser**
- **RJ45 = copper network plug · SFP = module for fibre · crimper makes cables, tester checks them · NFC = tap, Bluetooth = room range, RF = own dongle**
- **USB-A flat, USB-B printer, USB-C oval reversible · Lightning = older iPhones · Thunderbolt = fast data + video + power**
- **VGA analog, old · DVI video only · HDMI video + sound, TVs · DisplayPort for monitors · mirroring = same screen, casting = send media to a TV**

## Test 7 - 2.6-2.9 Virtualization, Cloud, Internet Access, Networking, Wireless (32 Q)

1. Sam uses Windows but wants to try Linux for a course without buying another computer or wiping his drive. What is the BEST option?
   - **[x] Run Linux in a virtual machine using a hypervisor**  - [ ] Add a second monitor  - [ ] Install a new network card  - [ ] Update the BIOS
   - *A hypervisor lets one physical machine run virtual machines, each with its own OS. Hook: HYPER = above, it sits over the VMs. Analogy: a landlord splitting a house into flats. A second monitor adds screen space, not a new OS.*
   - @2.6.virt
2. A server runs a hypervisor with three virtual machines, each running its own operating system. What are those operating systems called?
   - **[x] Guest OSs**  - [ ] Host firmware  - [ ] Hypervisors  - [ ] Device drivers
   - *The OS inside a VM is the guest; the real machine underneath is the host. Hook: the guest visits, the host owns the house. The hypervisor is the layer that shares out the hardware, not the OS in each VM.*
   - @2.6.virt
3. Which software shares one physical computer's CPU, memory and storage among several virtual machines?
   - **[x] Hypervisor**  - [ ] Guest OS  - [ ] Web browser  - [ ] Device driver
   - *The hypervisor allocates hardware to each VM. A guest OS runs inside one VM and only sees its share. A driver helps an OS use one device.*
   - @2.6.virt
4. A startup wants to rent virtual servers, storage and networks in the cloud, and install and manage its own operating systems. Which model fits?
   - **[x] IaaS**  - [ ] PaaS  - [ ] SaaS  - [ ] On premises
   - *IaaS (Infrastructure as a Service) rents raw building blocks; you manage the OS and up. Analogy: renting an empty kitchen and bringing your own food. PaaS hides the servers and OS, which is not what they want.*
   - @2.6.cloud
5. Developers want to upload their app's code and have the provider handle servers, OS and scaling. Which cloud model is BEST?
   - **[x] PaaS**  - [ ] IaaS  - [ ] SaaS  - [ ] Hybrid
   - *PaaS (Platform as a Service) gives a ready platform to run your own code. Analogy: an equipped kitchen; you bring the recipe. IaaS would make them manage servers too; SaaS is a finished app, not a place to run their code.*
   - @2.6.cloud
6. A company pays per user each month for webmail and an online office suite that staff use in a browser. Which model is this?
   - **[x] SaaS**  - [ ] PaaS  - [ ] IaaS  - [ ] On premises
   - *SaaS (Software as a Service) is a finished app you just use. Analogy: eating at a restaurant. Nothing to install or manage, which rules out IaaS and PaaS.*
   - @2.6.cloud
7. A hospital keeps patient records on servers in its own building but runs email and payroll in the cloud. What deployment is this?
   - **[x] Hybrid**  - [ ] On premises only  - [ ] Cloud only  - [ ] Peer-to-peer
   - *Hybrid mixes on-premises systems with cloud services. On premises alone means everything stays in your own building. Analogy: some savings at home, some in the bank.*
   - @2.6.cloud
8. A family in a city wants the FASTEST home internet for 4K streaming and large uploads, and every service type is available. Which should they choose?
   - **[x] Fiber optic**  - [ ] DSL  - [ ] Satellite  - [ ] Cable
   - *Fiber optic carries data as light through glass and gives the highest speeds, often matching upload and download. Cable is fast too but usually with much slower uploads. DSL over copper phone lines is slower.*
   - @2.7.isp
9. Mia lives on a remote farm with no phone, cable or fibre lines and weak mobile signal. Which internet service is MOST likely to work?
   - **[x] Satellite**  - [ ] DSL  - [ ] Cable  - [ ] Fiber optic
   - *Satellite needs only a dish with a clear view of the sky. DSL, cable and fibre all need a physical line to the house. Its trade-off can be higher delay and weather sensitivity.*
   - @2.7.isp
10. An ISP offers internet over the house's existing copper telephone line. Which service is this?
    - **[x] DSL**  - [ ] Cable  - [ ] Fiber optic  - [ ] Satellite
    - *DSL (Digital Subscriber Line) uses phone lines. Cable is the close distractor, but it runs over the TV coax network. Analogy: delivering new parcels down the old garden path.*
    - @2.7.isp
11. A builder needs internet at a temporary site office for three months, with no fixed lines installed. Which option is the BEST fit?
    - **[x] Cellular (4G/5G) router**  - [ ] Fiber optic  - [ ] DSL  - [ ] Cable
    - *Cellular wireless uses the mobile network, so it needs no fixed line and can be moved. Fixed services take time to install and need a line. Wireless RF (fixed wireless) is another line-free option, but cellular is the easiest to set up quickly.*
    - @2.7.isp
12. Two laptops on the same Wi-Fi need to send data to each other. Which identifier tells the network which DEVICE should receive it?
    - **[x] IP address**  - [ ] Port number  - [ ] Wi-Fi password  - [ ] Screen resolution
    - *An IP (Internet Protocol) address identifies a device on a network, like a street address. A port picks which SERVICE on that device gets the data, like a flat number in the building.*
    - @2.8.ids
13. A technician notices a laptop's IP address changed after a reboot, but one hardware ID on its network card stayed the same. Which ID stayed the same?
    - **[x] MAC address**  - [ ] IP address  - [ ] Port number  - [ ] Domain name
    - *A MAC (Media Access Control) address is a hardware ID burned into the NIC at manufacture. IP addresses can be handed out afresh. Analogy: a car's chassis number versus its current parking spot.*
    - @2.8.ids
14. What port number does HTTPS, secure web browsing, use by default?
    - [=] 443
    - *HTTPS (Hypertext Transfer Protocol Secure) uses port 443. Plain HTTP uses port 80, the common mix-up. A port picks the service on a device; the IP picks the device.*
    - @2.8.ids
15. A web server at 203.0.113.10 runs both a website and an email service. How does incoming data reach the RIGHT service?
    - **[x] Each service listens on its own port number**  - [ ] Each service has its own MAC address on one NIC  - [ ] The router changes the IP for each service  - [ ] The CPU guesses from the file size
    - *Network communication uses IP to find the device and port to find the service. Analogy: IP = building address, port = flat number. One NIC has one MAC; the router does not rename services.*
    - @2.8.ids
16. Jo sees a padlock in the address bar when she visits her bank. What does it MOST reliably tell her?
    - **[x] The connection to the site is encrypted with HTTPS**  - [ ] The site is guaranteed not to be a scam  - [ ] The site is stored on her own hard drive  - [ ] Her Wi-Fi password was recently changed
    - *The padlock means secure web browsing: data in transit is encrypted. It does not prove the site is honest; scam sites can use HTTPS too. Analogy: a sealed envelope protects the letter but does not prove who wrote it.*
    - @2.8.svc
17. A designer must send a 3GB artwork file to a printing company's server. Which network service is she using?
    - **[x] File transfer**  - [ ] Secure web browsing  - [ ] Email with an attachment  - [ ] Casting
    - *File transfer services (such as FTP or SFTP) move files between computers and handle large sizes. Email is tempting, but mail systems usually limit attachments to tens of megabytes, far below 3GB.*
    - @2.8.svc
18. Which network service sends a message to a colleague's mailbox, where it waits until they open it?
    - **[x] Email**  - [ ] File transfer  - [ ] Secure web browsing  - [ ] Peer-to-peer gaming
    - *Email is store-and-forward: mail servers hold the message until the recipient collects it. Analogy: a letter waiting in a post box. File transfer moves files to a server, not to a person's inbox.*
    - @2.8.svc
19. A new broadband line arrives in a small office. Which device converts the ISP's line signal into a network connection?
    - **[x] Modem**  - [ ] Switch  - [ ] Access point  - [ ] Firewall
    - *A modem converts the ISP (Internet Service Provider) signal. Analogy: the gate between your garden and the public road. A switch only links devices inside the network.*
    - @2.8.devs
20. An office needs to plug 20 wired PCs into the same LAN. Which device should they add?
    - **[x] Switch**  - [ ] Modem  - [ ] Router  - [ ] Access point
    - *A switch connects many wired devices on one LAN. A router is tempting, but its job is moving traffic between networks (LAN to internet); home routers usually have only a few ports.*
    - @2.8.devs
21. Staff laptops in a new meeting room cannot connect because the room only has wired sockets. Which device lets them join the network wirelessly?
    - **[x] Access point**  - [ ] Modem  - [ ] Switch  - [ ] Cable tester
    - *An access point adds Wi-Fi to a wired network. Analogy: a doorway from the garden into the house. A switch adds more wired ports, not Wi-Fi.*
    - @2.8.devs
22. An office wants to block unwanted inbound traffic from the internet using rules, while letting web traffic out. Which device does this job?
    - **[x] Firewall**  - [ ] Switch  - [ ] Access point  - [ ] Modem
    - *A firewall allows or blocks traffic based on rules. Analogy: a security guard checking passes. A router moves traffic between networks, and a home router box often includes a firewall, but the filtering job is the firewall's.*
    - @2.8.devs
23. Staff PCs all open shared files from one central office server that controls access. Which model is this?
    - **[x] Client/server**  - [ ] Peer-to-peer  - [ ] WAN  - [ ] Hybrid cloud
    - *In client/server, many clients ask one central server. Analogy: diners ordering from one kitchen. Peer-to-peer has no central server; devices share directly as equals.*
    - @2.8.model
24. Two laptops at a café share a folder directly with each other, with no server involved. Which model is this?
    - **[x] Peer-to-peer**  - [ ] Client/server  - [ ] WAN  - [ ] IaaS
    - *Peer-to-peer means each device is equal and shares directly. Analogy: friends swapping books instead of borrowing from a library. Client/server needs a central server.*
    - @2.8.model
25. Ava's studio has a network in its main building and a link to a second office in another city. Which terms describe these two?
    - **[x] LAN in the building, WAN between the cities**  - [ ] WAN in the building, LAN between the cities  - [ ] LAN for both networks  - [ ] Peer-to-peer in the building, NAS between the cities
    - *A LAN (Local Area Network) covers one building or site; a WAN (Wide Area Network) joins sites far apart. Hook: L for Local, W for Wide. Analogy: rooms in a house versus roads between towns.*
    - @2.8.model
26. A family's 802.11n router is ten years old. Which standard should they look for in a new router for the BEST speed and handling of many devices?
    - **[x] 802.11ax (Wi-Fi 6)**  - [ ] 802.11ac (Wi-Fi 5)  - [ ] 802.11n (Wi-Fi 4)  - [ ] 802.11x
    - *Newer standards are faster and cope better with crowded networks: n (Wi-Fi 4) < ac (Wi-Fi 5) < ax (Wi-Fi 6). Hook: ax comes last in the alphabet. "802.11x" is just a name for the whole family, not a standard.*
    - @2.9.std
27. Ben's Wi-Fi gets weaker as he moves to the far bedroom, through three walls. What is the MOST likely cause?
    - **[x] Attenuation**  - [ ] Interference  - [ ] A wrong MAC address  - [ ] Casting
    - *Attenuation is signal loss over distance and through walls. Analogy: a voice getting quieter as you walk away. Interference is other signals getting in the way, which does not depend on which room he is in.*
    - @2.9.std
28. Kate's 2.4GHz Wi-Fi drops every time the kitchen microwave runs. What is the MOST likely cause, and a fix?
    - **[x] Interference; move her devices to the 5GHz band**  - [ ] Attenuation; buy a longer Ethernet cable for the microwave  - [ ] A bad MAC address; replace the NIC  - [ ] A full hard drive; delete old files
    - *Microwave ovens give off signal near 2.4GHz and interfere with Wi-Fi. Moving to 5GHz avoids it. Analogy: talking next to a blender. Attenuation is about distance and walls, not other devices.*
    - @2.9.std
29. A user wants the BEST Wi-Fi coverage in a far garden shed and does not need top speed. Which band should the device use?
    - **[x] 2.4GHz**  - [ ] 5GHz  - [ ] 6GHz  - [ ] Whichever band is newest
    - *Lower frequency travels further and through walls better, but is slower and more crowded. Analogy: a deep voice carries through walls; a high whistle does not. 5GHz and 6GHz are faster but have shorter range.*
    - @2.9.band
30. A gamer sits in the same room as a new Wi-Fi 6E router and wants the fastest, least crowded band. Which should he use?
    - **[x] 6GHz**  - [ ] 2.4GHz  - [ ] 5GHz  - [ ] 900MHz
    - *6GHz, added with Wi-Fi 6E (an 802.11ax extension), is fast and less crowded but short range, which does not matter in the same room. 802.11n uses 2.4/5GHz and 802.11ac uses 5GHz; older devices cannot use 6GHz.*
    - @2.9.band
31. A small office has a modem from its ISP and a switch linking its PCs. Which device sends traffic BETWEEN the office LAN and the internet?
    - **[x] Router**  - [ ] Switch  - [ ] Access point  - [ ] NIC
    - *A router moves traffic between different networks, such as the LAN and the internet. A switch only links devices inside one LAN, and an access point adds Wi-Fi. Home "routers" often combine router, switch, access point and firewall in one box.*
    - @2.8.devs
32. An older laptop supports only 802.11n (Wi-Fi 4). Which TWO bands can it use? (Select 2)
    - **[x] 2.4GHz**  - **[x] 5GHz**  - [ ] 6GHz  - [ ] 900MHz
    - *802.11n works on both 2.4GHz and 5GHz. 6GHz needs Wi-Fi 6E, so older devices cannot use it. 900MHz is not a home Wi-Fi band.*
    - @2.9.band

### Key facts
- **Hypervisor runs VMs · guest OS = inside the VM · SaaS = finished app, PaaS = platform for devs, IaaS = raw servers · hybrid = on premises + cloud**
- **Fiber fastest · cable = TV coax · DSL = phone line · satellite = remote · cellular = mobile network, no fixed line**
- **IP = which device (can change) · MAC = NIC hardware ID (fixed) · port = which service · HTTPS 443, HTTP 80**
- **Modem = to ISP · router = between networks · switch = wired inside the LAN · access point = Wi-Fi · firewall = allow/block by rules · client/server vs peer-to-peer · LAN local, WAN wide**
- **802.11n (Wi-Fi 4) < ac (Wi-Fi 5) < ax (Wi-Fi 6) · 2.4GHz far + slow + crowded · 5/6GHz fast + short · attenuation = distance/walls, interference = other signals**

## Test 8 - 3.1 Operating Systems, File Systems, User Interfaces (26 Q)

1. Dana needs to email 300 holiday photos, but the folder is too big for the mail limit. What should she do FIRST to make the folder smaller to send?
   - **[x] Compress it into a single .zip file**  - [ ] Encrypt the folder with a password  - [ ] Set the folder to read-only  - [ ] Rename the files with shorter names
   - *Compression packs files into less space, and a .zip also bundles many files into one attachment. Analogy: vacuum-packing clothes into a suitcase. Encryption protects content but does not shrink it. Read-only and shorter names change nothing about size that matters.*
   - @3.1.fs
2. Priya's laptop holds private client files. She wants them unreadable if the laptop is stolen. Which file system feature should she use?
   - **[x] Encryption**  - [ ] Compression  - [ ] Hidden attribute  - [ ] Shortcuts
   - *Encryption scrambles the data so only someone with the key or password can read it. Analogy: writing a diary in secret code. Hidden only stops a file showing in a normal list; anyone can still open it. Compression only saves space.*
   - @3.1.fs
3. A user can open a shared spreadsheet but gets "access denied" when saving changes. What is MOST likely the cause?
   - **[x] The user has read permission but not write permission**  - [ ] The file extension is wrong for the program  - [ ] The file is compressed on the disk  - [ ] The printer driver is out of date
   - *Permissions decide who can read, change or delete a file or folder. Opening works, saving does not, so read yes, write no. Analogy: a museum lets you look at the painting but not touch it. A wrong extension would stop it opening at all. Compression and drivers do not block saving.*
   - @3.1.fs
4. Which of these would Windows MOST likely refuse as a file name?
   - **[x] report?.docx**  - [ ] report-1.docx  - [ ] report_final.docx  - [ ] report 2024.docx
   - *Naming restrictions: Windows blocks \ / : * ? " < > | because they have special jobs. Spaces, hyphens and underscores are fine. Hook: a question mark asks a question, it cannot be a name.*
   - @3.1.fs
5. Leo double-clicks a file called budget.xlsx and it opens in the spreadsheet app. What told the OS which app to use?
   - **[x] The file extension**  - [ ] The file size  - [ ] The folder it is stored in  - [ ] The file's permissions
   - *The extension (the letters after the last dot) marks the file type, and the OS links each type to a default app. .xlsx = spreadsheet, .docx = document, .mp3 = audio, .exe = program. Size, folder and permissions do not choose the app.*
   - @3.1.fs
6. A friend sends Sam "invoice.pdf.exe". What is the BEST advice?
   - **[x] Do not open it: the real extension is .exe, so it is a program, not a PDF**  - [ ] Open it: the .pdf part shows it is a document  - [ ] Rename it to invoice.pdf and then open it  - [ ] Compress it first so it is safe to open
   - *Only the LAST extension counts. .exe runs code, a common malware trick. Renaming does not change what the content is; compression does not make it safe. Hook: read file names from the right.*
   - @3.1.fs
7. Which file system would a new Windows 11 PC MOST likely use for its main drive?
   - **[x] NTFS**  - [ ] APFS  - [ ] ext4  - [ ] FAT32
   - *File system types: NTFS = Windows (supports permissions, encryption, big files). APFS = Apple macOS/iOS. ext4 = Linux. FAT32 = old, very compatible, used on small USB sticks but limited to 4 GB per file.*
   - @3.1.fs
8. Ana wants to copy a 6 GB video to a USB stick that must work on both a Mac and a Windows PC. The copy fails with "file too large". Which change is BEST?
   - **[x] Reformat the stick as exFAT**  - [ ] Reformat the stick as FAT32  - [ ] Turn on the hidden attribute for the video  - [ ] Change the video's extension to .zip
   - *FAT32 has a 4 GB per-file limit, which is why the copy fails. exFAT removes that limit and both Windows and macOS can read and write it. Analogy: a bigger envelope that every post office accepts. Changing the extension does not change the file.*
   - @3.1.fs
9. Tom keeps work files, school files and photos all on his desktop and cannot find anything. What is the BEST fix?
   - **[x] Create folders (directories) for each topic and move the files into them**  - [ ] Compress every file on the desktop  - [ ] Give every file the same extension  - [ ] Set all the files to hidden
   - *Folders (also called directories) group related files in a tree, like drawers in a filing cabinet. Compressing, changing extensions or hiding files does not organise anything; hiding just makes them harder to find.*
   - @3.1.fs
10. A PC suddenly feels slow. Mia wants to see which running programs are using the most CPU and memory. Which tool is BEST?
   - **[x] Task Manager (Windows) or Activity Monitor (macOS)**  - [ ] Disk Cleanup  - [ ] The web browser history  - [ ] Device Manager
   - *Task Manager / Activity Monitor are system utilities that list running processes and the resources they use, and can end a frozen one. Disk Cleanup frees disk space; Device Manager handles hardware and drivers.*
   - @3.1.sys
11. What is a "process"?
   - **[x] A program that is currently running in memory**  - [ ] A program saved on the disk but not open  - [ ] A file that tells the OS how to use a printer  - [ ] A folder holding system files
   - *A process is a program while it runs. Analogy: a recipe in a book is the program; the cooking in progress is the process. Open the same app twice and you can see two processes. A driver is the printer file; a saved program is just a file.*
   - @3.1.sys
12. A new printer is plugged in but the PC cannot print to it. What is the MOST likely missing piece?
   - **[x] The printer's driver**  - [ ] A word processing app  - [ ] A file compression tool  - [ ] A browser extension
   - *A driver is small software that lets the OS talk to a specific piece of hardware. Analogy: a translator between the OS and the device. Without it, the OS does not know how to use the printer.*
   - @3.1.sys
13. Nobody is logged in, yet a PC still accepts print jobs and installs updates overnight. What kind of program makes this possible?
   - **[x] A service**  - [ ] A driver  - [ ] A shortcut  - [ ] An extension
   - *A service runs in the background with no window, often starting before anyone logs in (for example the print spooler or update service). Analogy: the building's heating that runs all night. A driver connects hardware; it is not a background job by itself.*
   - @3.1.sys
14. After a driver update, a webcam stops working. Where should the user go FIRST to roll the driver back?
   - **[x] Device Manager**  - [ ] Task Manager  - [ ] Disk Cleanup  - [ ] File Explorer
   - *Device Manager is the Windows utility that lists hardware and lets you update, disable or roll back drivers. Task Manager handles processes; Disk Cleanup frees space; File Explorer manages files.*
   - @3.1.sys
15. Which of these is a system utility rather than a productivity app?
   - **[x] A disk cleanup tool that deletes temporary files**  - [ ] A spreadsheet for monthly budgets  - [ ] A presentation for a sales meeting  - [ ] A word processor for letters
   - *System apps and utilities look after the computer itself: disk cleanup, backup, Task Manager, Settings, antivirus. Productivity apps help the user make work: documents, spreadsheets, slides.*
   - @3.1.sys
16. One app has frozen and will not close, but the rest of the PC works. What is the BEST next step?
   - **[x] End the app's process in Task Manager**  - [ ] Unplug the PC from the wall  - [ ] Reinstall the operating system  - [ ] Uninstall the display driver
   - *Ending one process stops only that app and keeps everything else running. Pulling the power risks losing other unsaved work. Reinstalling the OS or removing drivers is far too drastic. Hook: smallest fix first.*
   - @3.1.sys
17. A user says "Windows Update keeps restarting even after I stop it." Where should a technician look to set it to manual?
   - **[x] The Services utility**  - [ ] Device Manager  - [ ] The browser settings  - [ ] The file's properties
   - *The Services utility lists background services and lets you start, stop or change startup type (automatic, manual, disabled). Device Manager is for hardware; file properties are for one file.*
   - @3.1.sys
18. A user wants to see how much free space is left on the C: drive. Which built-in tool shows this MOST directly?
   - **[x] File Explorer, viewing the drive's properties**  - [ ] Task Manager's process list  - [ ] The browser's download page  - [ ] Device Manager's driver list
   - *Right-click the drive in File Explorer and choose Properties to see used and free space. Task Manager shows running processes; Device Manager shows hardware.*
   - @3.1.sys
19. Which BEST describes a GUI?
   - **[x] You click icons, menus and windows with a mouse or touch**  - [ ] You type text commands at a prompt  - [ ] It runs in the background with no window  - [ ] It lets the OS talk to hardware
   - *GUI = Graphical User Interface: pictures, icons, windows. Easy to learn. Typed commands = command line. Background with no window = service. Talks to hardware = driver.*
   - @3.1.ui
20. An IT admin must rename 500 files in the same way every week. Which interface is MOST efficient?
   - **[x] The command line, using a script**  - [ ] The GUI, renaming each file by hand  - [ ] Device Manager  - [ ] A browser extension
   - *The command line (console or terminal) takes typed commands and can be scripted, so repeated bulk jobs run fast. Analogy: a GUI is ordering from a picture menu; the command line is telling the chef exactly what you want. Renaming 500 files by hand is slow and error-prone.*
   - @3.1.ui
21. Which is an example of a console / command-line interface?
   - **[x] Windows PowerShell or a Linux terminal**  - [ ] The Windows Start menu  - [ ] A phone's home screen  - [ ] The macOS Dock
   - *PowerShell, Command Prompt and Linux/macOS Terminal are text interfaces. The Start menu, home screen and Dock are graphical (GUI).*
   - @3.1.ui
22. A colleague wants to know when a file was created and how big it is. Where should she look?
   - **[x] The file's properties**  - [ ] Task Manager  - [ ] Device Manager  - [ ] The recycle bin
   - *File properties show details such as size, type, location, created and modified dates, and attributes. Right-click the file and choose Properties (Windows) or Get Info (macOS).*
   - @3.1.ui
23. A manager wants a policy file that staff can open but cannot accidentally change. Which file attribute is BEST?
   - **[x] Read-only**  - [ ] Hidden  - [ ] Compressed  - [ ] Archive
   - *Read-only lets people view but not save changes. Hidden only removes it from normal view. Compressed saves space. Archive marks a file as changed since the last backup.*
   - @3.1.ui
24. A user cannot find a settings file that support says "is definitely in that folder". What is the MOST likely reason?
   - **[x] The file has the hidden attribute set**  - [ ] The file is read-only  - [ ] The file is compressed  - [ ] The file has a long name
   - *Hidden files do not show in a normal folder view unless you turn on "show hidden items". OSes hide many system files to stop accidents. Read-only and compressed files still show.*
   - @3.1.ui
25. Which TWO details are file attributes or properties you can view for a file? (Select 2)
   - **[x] Date modified**  - **[x] Read-only**  - [ ] CPU usage  - [ ] Driver version
   - *Date modified (a property) and read-only (an attribute) belong to the file. CPU usage belongs to a running process in Task Manager; driver version belongs to hardware in Device Manager.*
   - @3.1.ui
26. A new employee who has never used a computer needs to start working today. Which interface is BEST for her?
   - **[x] A GUI, because icons and menus are easy to learn**  - [ ] The command line, because it is faster for experts  - [ ] A server console with no desktop  - [ ] A script that runs at startup
   - *GUIs are designed for ease of use: you can see and point at what you want. The command line is powerful but you must remember commands, which suits experienced admins. Hook: GUI = see and click; CLI = know and type.*
   - @3.1.ui

## Test 9 - 3.2 + 3.3 Types of Software, Productivity + Collaboration Tools (32 Q)

1. A user clicks Print in a word processor. The app does not talk to the printer directly. What does the OS do in this situation?
   - **[x] Acts as the interface between the app and the hardware**  - [ ] Converts the document to a spreadsheet  - [ ] Encrypts the document before printing  - [ ] Shares the document with a colleague
   - *A main job of the OS is to sit between apps and hardware, so app makers do not have to write code for every printer, disk or screen. Analogy: a waiter between diners (apps) and the kitchen (hardware).*
   - @3.2.func
2. A PC runs a browser, music and a spreadsheet at once. Which OS function shares the CPU between them?
   - **[x] Task / process management**  - [ ] Disk management  - [ ] Device management  - [ ] Access control
   - *Process (task) management schedules running programs on the CPU and memory so they appear to run together. Analogy: a traffic officer giving each car a turn. Disk management handles storage; device management handles hardware; access control handles who may use what.*
   - @3.2.func
3. A technician adds a new hard drive and needs to create a partition and format it. Which OS function is this?
   - **[x] Disk management**  - [ ] Application management  - [ ] Process management  - [ ] Access control
   - *Disk management covers partitioning, formatting and tracking where files sit on storage. Application management is installing, updating and removing apps.*
   - @3.2.func
4. Two people share a family PC. Each should see only their own files after logging in. Which OS function makes this work?
   - **[x] Access control with separate user accounts**  - [ ] Device management  - [ ] Disk compression  - [ ] Process management
   - *Access control checks who you are (login) and what you may use (permissions). Separate accounts keep each person's files private. Analogy: each flatmate has a key to their own room.*
   - @3.2.func
5. An office wants to install, update and remove programs on PCs safely. Which OS function covers this?
   - **[x] Application management**  - [ ] Device management  - [ ] Disk management  - [ ] Access control
   - *Application management = installing, updating, running and uninstalling software. Device management is about hardware and drivers.*
   - @3.2.func
6. A user plugs in a new USB keyboard and it works within seconds without any setup. Which OS function handled this?
   - **[x] Device management**  - [ ] Application management  - [ ] Disk management  - [ ] Access control
   - *Device management detects hardware, loads the right driver and lets apps use it. Plug and play is device management at work.*
   - @3.2.func
7. Which statement BEST sums up why a computer needs an operating system?
   - **[x] It manages hardware and resources and gives apps and users a way to use them**  - [ ] It is only needed to connect to the internet  - [ ] It is only needed to play videos  - [ ] It replaces the need for a CPU
   - *The OS is the manager: it runs the hardware, shares resources, controls access and provides an interface. Without it, apps could not run. Internet and video are things apps do on top of the OS.*
   - @3.2.func
8. A user installs a new app and Windows asks for an administrator password before continuing. What is the MAIN reason?
   - **[x] Access control stops standard users from making system-wide changes**  - [ ] The app needs a new driver for the screen  - [ ] The disk must be reformatted first  - [ ] The app is a cloud service  
   - *Access control limits risky actions to admin accounts, so malware or mistakes cannot change the whole system. This is access control working together with application management.*
   - @3.2.func
9. Which device MOST likely runs an embedded operating system?
   - **[x] A smart washing machine's control panel**  - [ ] A gaming laptop  - [ ] A web server in a data centre  - [ ] A tablet
   - *Embedded OS = small, built into a device to do one job: appliances, car systems, smart thermostats, routers. Laptops run desktop OSes, servers run server OSes, tablets run mobile OSes.*
   - @3.2.types
10. A small company needs one machine to host email and shared files for all 40 staff at once. Which OS type is BEST?
   - **[x] Server**  - [ ] Desktop  - [ ] Mobile  - [ ] Embedded
   - *Server OSes (Windows Server, many Linux distributions) are built to serve many users and run services all day. Analogy: a restaurant kitchen versus a home kitchen. A desktop OS is for one person at a desk.*
   - @3.2.types
11. Which TWO are mobile operating systems? (Select 2)
   - **[x] Android**  - **[x] iOS**  - [ ] Windows Server  - [ ] macOS
   - *Android and iOS run phones and tablets, built for touch, battery life and app stores. macOS is Apple's desktop OS; Windows Server is a server OS.*
   - @3.2.types
12. A graphic designer edits large video and 3D files at her desk all day. Which OS type does her machine MOST likely run?
   - **[x] Desktop / workstation**  - [ ] Embedded  - [ ] Mobile  - [ ] Server
   - *Desktop/workstation OSes (Windows, macOS, Linux desktop) serve one user doing full work with keyboard, mouse and big screens. Workstation just means a powerful desktop.*
   - @3.2.types
13. What is the MAIN difference between a server OS and a desktop OS?
   - **[x] A server OS is built to provide services to many users at once**  - [ ] A server OS can only run on phones  - [ ] A desktop OS cannot connect to a network  - [ ] A desktop OS has no graphical interface
   - *Server OS = shares resources (files, email, websites) with many users. Desktop OS = one person's daily work. Desktops do network fine and do have a GUI; many servers run without one.*
   - @3.2.types
14. A smart thermostat has software that cannot be swapped for a general-purpose OS and does one job. What type of OS is this?
   - **[x] Embedded**  - [ ] Server  - [ ] Desktop  - [ ] Mobile
   - *Embedded systems are purpose-built, usually with limited hardware and updates through firmware. Hook: EMBEDDED = BEDDED into the device.*
   - @3.2.types
15. Which feature is MOST typical of a mobile OS rather than a desktop OS?
   - **[x] Touch-first design and an app store tuned for battery life**  - [ ] Running many users' email accounts at once  - [ ] Controlling a single appliance function  - [ ] Running only from the command line
   - *Mobile OSes focus on touch, sensors, power saving and app stores. Many users' services = server; single appliance = embedded.*
   - @3.2.types
16. A school buys a few desktop PCs for students and one machine to store everyone's coursework centrally. Which OS pairing is BEST?
   - **[x] Desktop OS on the student PCs, server OS on the storage machine**  - [ ] Server OS on all machines  - [ ] Mobile OS on the student PCs, embedded OS on the storage machine  - [ ] Embedded OS on all machines
   - *Match the OS to the job: one user each = desktop; serving many = server. Embedded is for appliances, mobile for phones and tablets.*
   - @3.2.types
17. Amir must write a two-page letter to a landlord. Which type of software is BEST?
   - **[x] Word processing**  - [ ] Spreadsheet  - [ ] Presentation  - [ ] Visual diagramming
   - *Word processors (Microsoft Word, Google Docs) are for text documents: letters, reports, essays. Spreadsheets are for numbers; presentations are slides; diagramming is drawings.*
   - @3.3.prod
18. A club treasurer wants to add up monthly costs and have totals update automatically when a number changes. Which tool is BEST?
   - **[x] A spreadsheet with formulas**  - [ ] A word processor with a table  - [ ] A presentation app  - [ ] A visual diagramming app
   - *Spreadsheets (Excel, Google Sheets) use cells and formulas, so totals recalculate when inputs change. A word processor table holds numbers but does not calculate well.*
   - @3.3.prod
19. A teacher wants slides with pictures to show on a projector during a lesson. Which software is BEST?
   - **[x] Presentation software**  - [ ] Spreadsheet software  - [ ] An email client  - [ ] A word processor
   - *Presentation software (PowerPoint, Google Slides, Keynote) builds slides for showing to an audience. Hook: present = slides.*
   - @3.3.prod
20. An office manager needs to draw a floor plan and a flowchart of the hiring process. Which tool is BEST?
   - **[x] Visual diagramming software**  - [ ] Spreadsheet software  - [ ] Presentation software  - [ ] Instant messaging
   - *Visual diagramming tools (Visio, Lucidchart, draw.io) make flowcharts, floor plans and network diagrams with shapes and connectors. Presentation apps can draw shapes but are not built for accurate plans.*
   - @3.3.prod
21. A sales team needs a chart of quarterly sales figures that will be pasted into a report. Where should the chart be built FIRST?
   - **[x] In a spreadsheet, from the data**  - [ ] In an email client  - [ ] In a visual diagramming app by hand  - [ ] In a conferencing app
   - *Spreadsheets turn rows of numbers into charts that update with the data, which can then be pasted into a word processor or presentation. Drawing a chart by hand loses the link to the numbers.*
   - @3.3.prod
22. A technician must show how the office router, switch, printers and PCs connect, with boxes and connecting lines. Which software is BEST?
   - **[x] Visual diagramming software**  - [ ] Spreadsheet software  - [ ] Word processing software  - [ ] An email client
   - *Network diagrams are drawn with shapes and connectors in diagramming tools such as Visio or draw.io. Spreadsheets are for numbers, word processors for text documents, and email for messages.*
   - @3.3.prod
23. Which TWO tasks are BEST suited to word processing software? (Select 2)
   - **[x] Writing a CV**  - **[x] Drafting a school report**  - [ ] Tracking stock levels with formulas  - [ ] Drawing a network diagram
   - *Word processors handle formatted text documents: CVs, reports, letters. Stock with formulas = spreadsheet; network diagrams = diagramming.*
   - @3.3.prod
24. Which feature is MOST typical of presentation software rather than a word processor?
   - **[x] Showing slides full screen one at a time, with private speaker notes**  - [ ] Checking spelling as you type  - [ ] Printing a multi-page letter  - [ ] Changing the font size of text
   - *Presentation software (PowerPoint, Keynote) is built around slides shown to an audience, with speaker notes only the presenter sees. Spell check, printing and fonts are common to most office apps.*
   - @3.3.prod
25. A remote team needs to talk face to face and share screens in a weekly meeting. Which tool is BEST?
   - **[x] Conferencing software**  - [ ] An email client  - [ ] Document sharing  - [ ] A word processor
   - *Conferencing software (Teams, Zoom, Google Meet) gives live video, audio and screen sharing. Email is not live. Document sharing stores files but is not a meeting.*
   - @3.3.collab
26. Jo needs a quick yes or no from a colleague in another building within the next minute. Which tool is BEST?
   - **[x] Instant messaging**  - [ ] Email  - [ ] A shared document  - [ ] A scheduled video conference
   - *Instant messaging (Teams chat, Slack) is for fast, short, real-time text. Email suits longer or formal messages where a delay is fine. Booking a conference is overkill for a quick answer.*
   - @3.3.collab
27. A help desk technician needs to see and control a user's screen from another city to fix a setting. Which tool is BEST?
   - **[x] Remote support software**  - [ ] Instant messaging  - [ ] A web browser  - [ ] Presentation software
   - *Remote support tools (Quick Assist, TeamViewer, Remote Desktop) let a technician view and control a PC over the network, with the user's permission. Analogy: lending the technician your hands from afar.*
   - @3.3.collab
28. Five people keep emailing versions of the same report and lose track of the latest one. What is the BEST fix?
   - **[x] Store one copy with a document sharing service so everyone edits the same file**  - [ ] Email the report more often  - [ ] Print the report and pass it around  - [ ] Save the report as a compressed file
   - *Document sharing (OneDrive, Google Drive, SharePoint) keeps a single file in one place with version history, so there is no "final_v7" mess. Analogy: one whiteboard everyone writes on instead of photocopies.*
   - @3.3.collab
29. A project team wants one place with shared notes, task lists, files and chat for their project. Which tool BEST fits?
   - **[x] An online workspace**  - [ ] An email client  - [ ] A desktop word processor  - [ ] Remote support software
   - *An online workspace (Microsoft Teams, Notion, Confluence) combines files, notes, tasks and chat in one shared area. Email and a single word processor do not give a shared hub.*
   - @3.3.collab
30. Which TWO are typical uses of an email client such as Outlook or Thunderbird? (Select 2)
   - **[x] Sending and receiving messages with attachments**  - **[x] Managing a calendar and contacts**  - [ ] Controlling another user's PC  - [ ] Building slides for a talk
   - *An email client is an app for reading and sending email, and often includes calendar and contacts. Controlling a PC = remote support; slides = presentation. A web browser can also be used to reach webmail and other cloud tools.*
   - @3.3.collab
31. In a spreadsheet, Ola types a number into the box where column B meets row 4. What is that box called?
   - **[x] A cell (B4)**  - [ ] A slide  - [ ] A formula  - [ ] A tab
   - *A cell is where a column and a row meet, named by its column letter and row number, such as B4. Formulas such as =B4*2 refer to cells by name. A slide belongs to presentation software.*
   - @3.3.prod
32. A team member has no apps installed except the OS defaults, but must join the team's cloud workspace and read shared files today. Which tool will she MOST likely use?
   - **[x] A web browser**  - [ ] Visual diagramming software  - [ ] A disk cleanup utility  - [ ] A desktop presentation app
   - *Web browsing is a collaboration tool in its own right: browsers open webmail, online workspaces, document sharing and even conferencing without installing anything extra.*
   - @3.3.collab

## Test 10 - 3.4 + 3.5 Web Browsers, Privacy, Extensions, AI (29 Q)

1. Kim uses a library computer to check her email. She wants no history, cookies or form data saved after she closes the browser. What should she use?
   - **[x] Private / incognito browsing**  - [ ] A pop-up blocker  - [ ] Profile sync  - [ ] A new bookmark
   - *Private browsing deletes history, cookies and form data when the window closes. It does NOT hide you from the website, your employer or your internet provider. She should still log out.*
   - @3.4.priv
2. Which statement about private browsing is TRUE?
   - **[x] It stops the browser saving history on this device, but websites and the network can still see your activity**  - [ ] It makes you completely anonymous online  - [ ] It blocks all malware  - [ ] It encrypts every file you download
   - *Private browsing only affects what is stored locally. Analogy: shredding your own receipts; the shop still knows you bought something. It is not a VPN or antivirus.*
   - @3.4.priv
3. A company updated its website, but Raj still sees the old page. Other people see the new one. What should he try FIRST?
   - **[x] Clear the browser cache and reload**  - [ ] Install a new browser extension  - [ ] Change the default search engine  - [ ] Turn on the pop-up blocker
   - *The cache stores copies of pages and images to load sites faster. A stale copy can show an old page. Clearing it forces a fresh download. Analogy: throwing away an old printed menu and asking for the new one.*
   - @3.4.priv
4. Why does a browser keep a cache at all?
   - **[x] To load pages faster by reusing files already downloaded**  - [ ] To block all advertising  - [ ] To store passwords securely  - [ ] To sync bookmarks across devices
   - *Caching saves images, scripts and pages locally so return visits are quicker and use less data. The trade-off: it takes disk space and can show outdated content.*
   - @3.4.priv
5. Lena is buying concert tickets and the payment window will not appear. A browser icon says something was blocked. What is the BEST next step?
   - **[x] Allow pop-ups for that trusted ticket site only**  - [ ] Turn off the pop-up blocker for all sites  - [ ] Clear the cache  - [ ] Switch to private browsing
   - *Pop-up blockers stop new windows, which are often ads or scams, but they can also block real ones like payment windows. Allowing a single trusted site keeps protection on elsewhere. Turning it off everywhere removes the protection.*
   - @3.4.priv
6. The browser offers to save the password for Ben's bank. He shares the PC with others who use his account. What is the BEST choice?
   - **[x] Do not save it, or use a password manager protected with a master password**  - [ ] Save it, because the browser always encrypts it from other users  - [ ] Save it and turn on private browsing  - [ ] Write it in a bookmark name
   - *Browser password management is handy, but anyone using the same logged-in profile may be able to auto-fill or view saved passwords. A password manager with its own master password, or not saving it, is safer here.*
   - @3.4.priv
7. Which TWO actions remove saved data from a browser? (Select 2)
   - **[x] Clearing the cache**  - **[x] Clearing cookies and browsing history**  - [ ] Turning on the pop-up blocker  - [ ] Changing the browser theme
   - *Clearing browsing data removes the cache, cookies, history and optionally saved passwords. Pop-up blockers and themes do not delete anything.*
   - @3.4.priv
8. A user's browser suggests a strong, random password when she creates a new online account. Which feature is this?
   - **[x] Built-in password management**  - [ ] Pop-up blocking  - [ ] Private browsing  - [ ] Caching
   - *Modern browsers include a password manager that can generate, save and auto-fill passwords. Saved passwords can sync to other devices through the profile.*
   - @3.4.priv
9. Carlos wants a tool inside his browser that checks spelling as he types on any website. What should he add?
   - **[x] An extension (add-on) from the browser's official store**  - [ ] A new default search engine  - [ ] A bookmark  - [ ] A private window
   - *Extensions / add-ons are small programs that add features to a browser. Install them from the official store (Chrome Web Store, Firefox Add-ons) and check reviews and permissions.*
   - @3.4.ext
10. After installing a "coupon finder" extension, Nina's browser shows extra ads and her home page has changed. What should she do FIRST?
   - **[x] Remove the extension**  - [ ] Clear the cache only  - [ ] Change the browser theme  - [ ] Turn on profile sync
   - *A bad or malicious extension can inject ads and change settings. Removing it is the fix. Clearing the cache does not remove the extension. Turning on sync could copy it to her other devices.*
   - @3.4.ext
11. A web app works in a coworker's browser but not in Ben's. Ben has several extensions. Which step is BEST for testing whether an extension is the cause?
   - **[x] Disable the extensions, then re-enable them one at a time**  - [ ] Uninstall the browser completely  - [ ] Delete all bookmarks  - [ ] Change the default search engine
   - *Disabling keeps the extension installed but turned off, so it is easy to switch back. Re-enabling one at a time finds the culprit. Analogy: flipping fuses off and on to find which circuit trips.*
   - @3.4.ext
12. What is the difference between disabling and removing an extension?
   - **[x] Disabling turns it off but keeps it installed; removing uninstalls it**  - [ ] Disabling deletes it; removing hides it  - [ ] They are the same thing  - [ ] Removing only works in private browsing
   - *Disable = off switch, easy to turn back on. Remove = uninstall. Use disable for testing, remove for anything unwanted or suspicious.*
   - @3.4.ext
13. Before adding an extension, which is the BEST thing to check?
   - **[x] The permissions it asks for and that it comes from the official store**  - [ ] That it has a colourful icon  - [ ] That it was sent as an email attachment  - [ ] That it disables the pop-up blocker
   - *An extension that asks to "read and change all your data on all websites" sees everything you do. Only add trusted ones from the official store and check reviews. Email attachments are a common malware route.*
   - @3.4.ext
14. Rosa wants an ad blocker on only her work laptop, but it keeps appearing on her home PC too. What is the MOST likely reason?
   - **[x] Profile sync is copying her extensions to both devices**  - [ ] The cache is full  - [ ] The pop-up blocker installed it  - [ ] Private browsing is turned on
   - *Signing in to the same browser profile syncs bookmarks, passwords, settings and extensions. She can turn off syncing for extensions or remove it on one device.*
   - @3.4.ext
15. A council's online form only works properly in a supported, up-to-date browser. Mo's PC has an old browser with no updates. What should he do FIRST?
   - **[x] Use a current, compatible browser**  - [ ] Install more extensions  - [ ] Clear his bookmarks  - [ ] Turn off accessibility features
   - *Compatible browser: sites are built for current versions of common browsers (Chrome, Edge, Firefox, Safari). Old unsupported browsers break pages and miss security fixes.*
   - @3.4.cfg
16. Sara uses a laptop at work and a desktop at home. She wants the same bookmarks and saved passwords on both. Which feature is BEST?
   - **[x] Profile sync**  - [ ] Private browsing  - [ ] Clearing the cache  - [ ] A pop-up blocker
   - *Signing in to a browser profile syncs bookmarks, history, passwords and settings across devices. Analogy: a backpack of your stuff that follows you to any desk.*
   - @3.4.cfg
17. Tim visits a recipe site every day and wants to get back to it in one click. What should he do?
   - **[x] Bookmark the page**  - [ ] Clear the cache  - [ ] Open it in private browsing  - [ ] Install a password manager
   - *A bookmark (favourite) saves a page's address for quick return. Folders on the bookmarks bar keep them tidy.*
   - @3.4.cfg
18. When Jen types words into the address bar, results come from a search engine she does not like. What should she change?
   - **[x] The default search engine in browser settings**  - [ ] The pop-up blocker settings  - [ ] The cache size  - [ ] The file extension
   - *The default search engine is the one used when you search from the address bar. It can be changed in settings. A search engine that changed without permission can be a sign of an unwanted extension.*
   - @3.4.cfg
19. An older user finds website text too small to read. What is the BEST browser setting to change?
   - **[x] Zoom or default font size in the accessibility settings**  - [ ] The default search engine  - [ ] The pop-up blocker  - [ ] Profile sync
   - *Accessibility settings include zoom, font size, high contrast, captions and screen reader support. Ctrl and + also zooms in most browsers.*
   - @3.4.cfg
20. A user wants the browser to use a dark theme that is easier on her eyes at night. Which setting area should she use?
   - **[x] Appearance**  - [ ] Privacy and security  - [ ] Extensions  - [ ] Downloads
   - *Appearance settings control themes, light or dark mode, toolbar layout and fonts. They change the look, not how the browser handles data.*
   - @3.4.cfg
21. Which TWO are browser configuration settings rather than privacy tools? (Select 2)
   - **[x] Default search engine**  - **[x] Appearance / theme**  - [ ] Private browsing  - [ ] Pop-up blocker
   - *Search engine and appearance shape how the browser works and looks. Private browsing and pop-up blockers are privacy and safety features.*
   - @3.4.cfg
22. A bank website has a chat window that answers typed questions like "How do I reset my PIN?" at any hour. What is this?
   - **[x] A chatbot**  - [ ] A virtual assistant on a smart speaker  - [ ] A pop-up blocker  - [ ] Remote support software
   - *A chatbot is AI (Artificial Intelligence) software that holds a typed conversation to answer common questions, often on websites. It saves staff time and works around the clock.*
   - @3.5.ai
23. Ana says "set a timer for 10 minutes" to her phone and it does it. What type of AI is she using?
   - **[x] A virtual assistant**  - [ ] Generative AI for code  - [ ] A website chatbot  - [ ] A recommendation engine
   - *Virtual assistants (Siri, Alexa, Google Assistant) take voice commands and carry out tasks: timers, reminders, calls, smart home control. Hook: assistant = does jobs for you.*
   - @3.5.ai
24. A marketing worker asks an AI tool to "write three short product descriptions for a new water bottle" and gets new text in seconds. What kind of AI is this?
   - **[x] Generative AI creating content**  - [ ] A pop-up blocker  - [ ] A virtual assistant setting a reminder  - [ ] A spam filter
   - *Generative AI creates new content (text, images, audio, video) from a prompt. Analogy: a writer who drafts on request. Always check the output for errors before using it.*
   - @3.5.ai
25. A new programmer asks an AI tool to write a function that sorts a list. What is the BEST practice with the result?
   - **[x] Review and test the code before using it**  - [ ] Use it as is, because AI code is always correct  - [ ] Paste in company passwords so the AI can improve it  - [ ] Delete it, because AI cannot write code
   - *Generative AI can write code, but it can make mistakes or produce insecure code. Treat it like a draft from a helper. Never paste secrets or private data into public AI tools.*
   - @3.5.ai
26. A streaming service shows "Because you watched this, you might like..." Which use of AI is this?
   - **[x] Predictions and suggestions**  - [ ] Generative AI creating images  - [ ] A virtual assistant  - [ ] A chatbot
   - *Recommendation systems analyse past behaviour to predict what you will like. Other examples: shopping suggestions, predictive text on a phone keyboard, sat-nav travel time estimates.*
   - @3.5.ai
27. Which is the BEST example of AI predictions and suggestions?
   - **[x] A phone keyboard offering the next word as Omar types**  - [ ] A website chat window answering billing questions  - [ ] Asking a smart speaker to turn off the lights  - [ ] Asking an AI tool to draw a logo from a description
   - *Predictive text guesses the next word from what you and others usually type. It suggests; you decide. The chat window is a chatbot, the smart speaker is a virtual assistant, and drawing a logo is generative AI.*
   - @3.5.ai
28. An employee wants to paste a confidential customer list into a public AI chatbot to get a summary. What is the BEST advice?
   - **[x] Do not: data entered may be stored or used by the AI provider**  - [ ] Go ahead: chatbots delete everything instantly  - [ ] Go ahead, but in private browsing  - [ ] Go ahead, but compress the list first
   - *Public AI tools may keep prompts and use them to train models. Follow company policy and use only approved tools for private data. Private browsing only affects your own device, not the AI provider.*
   - @3.5.ai
29. Which TWO are examples of generative AI? (Select 2)
   - **[x] Creating a picture from the prompt "a cat in a spacesuit"**  - **[x] Drafting a cover letter from a short description**  - [ ] Sorting files by date in File Explorer  - [ ] Blocking a pop-up window
   - *Generative AI makes new content: images, text, code, music. Sorting files and blocking pop-ups are normal software features with no AI content creation.*
   - @3.5.ai

## Test 11 - 4.1 + 4.2 Programming Language Types + Data Types (27 Q)

1. A game studio needs its finished product to run as fast as possible, and it will ship one ready-made program file to players. Which language category BEST fits?
   - **[x] Compiled**  - [ ] Markup  - [ ] Query  - [ ] Scripting
   - *Compiled languages, like C and C++, are translated in full into machine code before running, so the result is fast and ships as one program file. Hook: COMPILE = translate the whole book before printing. Scripting is tempting but is usually interpreted line by line, which is slower. Markup and query don't build programs.*
   - @4.1.lang
2. A tester changes one line of a Python script and runs it again straight away, with no build step. Why is this possible?
   - **[x] Python is interpreted, so code is read and run line by line**  - [ ] Python is compiled into a program each time it is saved  - [ ] Python is a markup language read only by browsers  - [ ] Python is assembly code sent straight to the CPU
   - *An interpreter reads and runs code as it goes, so there is no separate compile step. Analogy: a live interpreter translating a speech sentence by sentence. The trade-off is speed: compiled code usually runs faster.*
   - @4.1.lang
3. A web designer wants to mark text on a page as a heading and turn another line into a link. Which type of language is she using?
   - **[x] Markup**  - [ ] Query  - [ ] Assembly  - [ ] Compiled
   - *Markup languages such as HTML (Hypertext Markup Language) and XML (Extensible Markup Language) label content so it can be shown or structured. They don't contain program logic. Hook: HTML and XML both end in ML = Markup Language. Analogy: sticky notes saying "title here", "link here".*
   - @4.1.lang
4. A sales manager wants a list of every customer in a database who spent more than $500 last month. Which type of language is BEST for this?
   - **[x] Query**  - [ ] Markup  - [ ] Assembly  - [ ] Scripting
   - *A query language, such as SQL (Structured Query Language), asks a database to find, add or change records. Hook: QUERY = question. Analogy: asking a librarian for all books by one author. Scripting could do it with extra work, but the query language is the direct tool.*
   - @4.1.lang
5. A firmware engineer writes code using short instructions like MOV and ADD that map almost one to one onto CPU instructions. What category is this?
   - **[x] Assembly**  - [ ] Scripting  - [ ] Markup  - [ ] Query
   - *Assembly is a low-level language very close to the processor's own machine code. It is fast and precise but hard for people to read. Scripting is the opposite end: high level and easy to write.*
   - @4.1.lang
6. An admin wants to automate renaming 500 files every night. Which language category is the MOST practical choice?
   - **[x] Scripting, such as PowerShell or Python**  - [ ] Markup, such as HTML or XML  - [ ] Query, such as SQL  - [ ] Assembly for the CPU
   - *Scripting languages are interpreted and great for quick automation of everyday jobs. Markup only describes content, query talks to databases, and assembly would be slow to write for a simple task. Hook: SCRIPT = a to-do list the computer follows.*
   - @4.1.lang
7. Which TWO are interpreted language types according to the exam objectives? (Select 2)
   - **[x] Scripting languages**  - **[x] Markup languages**  - [ ] Assembly languages  - [ ] Compiled languages
   - *The objectives list scripting and markup under interpreted: they are read and processed by another program (an interpreter or browser) rather than built into a machine-code file. Compiled and assembly are both turned into machine code ahead of time.*
   - @4.1.lang
8. A developer must hand a program to customers but does not want them reading the original source code. Which approach BEST helps?
   - **[x] Use a compiled language and ship only the program file**  - [ ] Use a scripting language and ship the script file  - [ ] Write it in markup so the browser hides it  - [ ] Write it as queries stored in the database
   - *A compiled program ships as machine code, so the readable source stays with the developer. A script is the source itself, so anyone can open it. Analogy: selling a baked cake rather than the recipe card.*
   - @4.1.lang
9. Which statement BEST compares compiled and interpreted code?
   - **[x] Compiled code is translated before running; interpreted code is translated as it runs**  - [ ] Compiled code runs line by line; interpreted code is built first  - [ ] Interpreted code always runs faster than compiled code  - [ ] Only compiled code can contain loops and branches
   - *Compiled = translate everything first, then run (usually faster). Interpreted = translate on the fly (easier to test and change). The second option swaps the two. Both kinds can use loops and branches.*
   - @4.1.lang
10. A data file stores settings in tags like <colour>blue</colour> so different programs can read them. Which language is MOST likely in use?
   - **[x] XML**  - [ ] SQL  - [ ] C++  - [ ] Assembly
   - *Extensible Markup Language (XML) is a markup language that labels data with tags for sharing between programs. SQL queries databases, C++ is compiled, assembly is low level. Hook: angle-bracket tags = markup.*
   - @4.1.lang
11. A student sees this line: SELECT name FROM pupils WHERE grade = 10. What type of language is it?
   - **[x] Query**  - [ ] Markup  - [ ] Assembly  - [ ] Compiled
   - *SELECT ... FROM ... WHERE is SQL, a query language that asks a database for matching records. Here it fetches the names of all pupils in grade 10. Hook: it reads like a question to the database.*
   - @4.1.lang
12. A company builds a program in C and wants to run it on a new type of processor. What MOST likely needs to happen?
   - **[x] The source code must be compiled again for that processor**  - [ ] The program will run unchanged on any CPU  - [ ] The program must be rewritten in HTML  - [ ] The database must be queried again
   - *Compiled machine code is made for one kind of processor and OS, so it is rebuilt (recompiled) for a different one. Interpreted code is more portable because the interpreter handles the differences. Analogy: a book translated into French must be translated again for German readers.*
   - @4.1.lang
13. A form asks "Do you want the newsletter?" with a single tick box. Which data type BEST stores the answer?
   - **[x] Boolean**  - [ ] String  - [ ] Float  - [ ] Char
   - *A Boolean holds only true or false, perfect for yes/no answers. A string could store the word "yes" but wastes space and invites typos. Hook: Boolean = light switch, on or off.*
   - @4.2.types
14. A shop app stores the price 19.99. Which data type is BEST?
   - **[x] Float**  - [ ] Integer  - [ ] Boolean  - [ ] Char
   - *A float (floating-point number) holds numbers with a decimal part. An integer would drop the .99 and store 19. Hook: FLOAT = the decimal point floats in the number.*
   - @4.2.types
15. A program counts how many people walk through a door today. Which data type is BEST?
   - **[x] Integer**  - [ ] Float  - [ ] String  - [ ] Boolean
   - *An integer is a whole number with no decimal part, ideal for counts. You can't have 3.5 people, so a float adds nothing. A string "42" can't be added up without converting.*
   - @4.2.types
16. A quiz stores each answer as a single letter: A, B, C or D. Which data type is the BEST fit?
   - **[x] Char**  - [ ] String  - [ ] Integer  - [ ] Float
   - *A char (character) holds exactly one letter, digit or symbol. A string also works but is meant for a sequence of characters. Hook: CHAR = one CHARacter.*
   - @4.2.types
17. A sign-up form collects a customer's full name, "Maria Lopez". Which data type should hold it?
   - **[x] String**  - [ ] Char  - [ ] Integer  - [ ] Boolean
   - *A string is a sequence of characters, including spaces. A char holds only one character. Analogy: a string of beads, each bead a character.*
   - @4.2.types
18. A phone number like 0412 555 019 starts with a zero and is never used in sums. Which data type is BEST?
   - **[x] String**  - [ ] Integer  - [ ] Float  - [ ] Boolean
   - *Store phone numbers, postcodes and ID codes as strings. An integer would drop the leading zero (0412 becomes 412) and cannot hold spaces. Hook: if you would never add it up, it probably isn't a number.*
   - @4.2.types
19. A program adds "5" + "5" and the result is "55", not 10. What is the MOST likely cause?
   - **[x] The values are strings, so they were joined together**  - [ ] The values are floats, so they were rounded  - [ ] The values are Booleans, so they were compared  - [ ] The values are chars, so they were sorted
   - *With strings, + joins (concatenates) the text: "5" + "5" = "55". To get 10 the values must be numbers such as integers. Analogy: gluing two "5" labels side by side instead of counting.*
   - @4.2.types
20. A weather app stores the temperature 21.5 degrees in an integer. What happens?
   - **[x] The decimal part is lost and it stores 21**  - [ ] It is stored exactly as 21.5  - [ ] It becomes the Boolean value true  - [ ] It is turned into the string "21.5"
   - *An integer can only hold whole numbers, so the .5 is dropped. A float is the right type for readings with decimals.*
   - @4.2.types
21. Which TWO values are numeric data types? (Select 2)
   - **[x] 42 (integer)**  - **[x] 3.14 (float)**  - [ ] "42" (string)  - [ ] true (Boolean)
   - *Integers and floats are the number types in the objectives. "42" in quotes is a string, text that only looks like a number. true is a Boolean.*
   - @4.2.types
22. A Boolean variable can hold how many possible values?
   - **[x] Two: true or false**  - [ ] One: true only  - [ ] Ten: the digits 0 to 9  - [ ] Any letter of the alphabet
   - *A Boolean is either true or false (sometimes shown as 1 or 0). It is the type used for conditions in IF and WHILE. Any single letter would be a char.*
   - @4.2.types
23. Which of these values is a float?
   - **[x] 7.5**  - [ ] 7  - [ ] "7.5"  - [ ] true
   - *7.5 is a number with a decimal part, so a float. 7 is a whole number (integer). "7.5" in quotes is a string, text that only looks like a number. true is a Boolean.*
   - @4.2.types
24. A developer stores a customer's age in a string, then tries to check age > 18. What is the MOST likely problem?
   - **[x] Text cannot be compared as a number without converting it first**  - [ ] Strings can only store a single letter  - [ ] Ages must always be stored as Booleans  - [ ] Comparing values is only allowed on chars
   - *Strings are text, so maths and numeric comparisons don't work reliably until the value is converted to an integer. Store ages as integers from the start. A string can hold many characters, unlike a char.*
   - @4.2.types
25. Which value is a char rather than a string?
   - **[x] 'Y'**  - [ ] "Yes"  - [ ] "Y and N"  - [ ] "Hello"
   - *'Y' is a single character, so a char. The others contain several characters, so they are strings. Hook: count the characters; one = char.*
   - @4.2.types
26. A student labels the data types in a program. Which TWO of her labels are correct? (Select 2)
   - **[x] false is a Boolean**  - **[x] -7 is an integer**  - [ ] 2.5 is an integer  - [ ] "London" is a char
   - *false is a Boolean, and -7 is a whole number, so an integer (integers can be negative). 2.5 has a decimal part, so it is a float. "London" has many characters, so it is a string.*
   - @4.2.types
27. A coder uses Python to automate a task, HTML to lay out the result page, and SQL to pull figures from the sales database. Which list shows the categories in that order?
   - **[x] Scripting, markup, query**  - [ ] Compiled, query, markup  - [ ] Markup, scripting, assembly  - [ ] Query, markup, scripting
   - *Python = interpreted scripting, HTML = markup, SQL = query. Real projects often mix several categories, each doing the job it is best at.*
   - @4.1.lang

## Test 12 - 4.3 + 4.4 Variables, Objects, Program Logic + Organisation (34 Q)

1. A game tracks a player's score, which goes up every time a coin is collected. What should hold the score?
   - **[x] A variable**  - [ ] A constant  - [ ] A comment  - [ ] A flow chart
   - *A variable is a named value that can change while the program runs. A constant is set once and stays fixed. Analogy: a scoreboard that keeps being updated.*
   - @4.3.ident
2. A payroll program uses a tax rate of 0.1 in twenty places and it must never change while the program runs. What is the BEST way to store it?
   - **[x] As a constant**  - [ ] As a loop  - [ ] As a comment  - [ ] As a variable changed in each place
   - *A constant fixes the value so it can't be changed by mistake, and if the law changes you update it in one place. A comment is ignored by the computer. Hook: CONSTANT = constantly the same. Analogy: a price printed on the menu, not written in chalk.*
   - @4.3.ident
3. A teacher's program must hold the names of all 30 pupils in a class. What is the BEST structure?
   - **[x] An array**  - [ ] A constant  - [ ] A char  - [ ] A Boolean
   - *An array stores a list of values under one name, each in a numbered slot (index). A char holds one letter; a Boolean holds true or false. Analogy: an egg box: one box, many numbered spaces.*
   - @4.3.ident
4. A developer copies the same 15 lines that calculate shipping cost into six different places. What would BEST improve this?
   - **[x] Put the lines in a function and call it from each place**  - [ ] Turn the lines into comments  - [ ] Store the lines in a constant  - [ ] Change the variables into Booleans
   - *A function is a named, reusable block of code. Write it once, call it many times, and fix bugs in one place. Analogy: a coffee machine button: press it and the same steps happen every time.*
   - @4.3.ident
5. Trace this pseudocode. What is printed? ¶ colours = ["red", "green", "blue"] ¶ print colours[1]
   - **[x] green**  - [ ] red  - [ ] blue  - [ ] An error, because there is no item 1
   - *Arrays usually count from 0: index 0 = red, index 1 = green, index 2 = blue. Trap: picking red because "1 means first". Hook: arrays start at zero, like a building's ground floor.*
   - @4.3.ident
6. Trace this pseudocode. What is printed? ¶ FUNCTION double(n) ¶   RETURN n * 2 ¶ END FUNCTION ¶ x = double(4) ¶ print x + 1
   - **[x] 9**  - [ ] 8  - [ ] 10  - [ ] 5
   - *double(4) returns 4 * 2 = 8, so x = 8, and x + 1 = 9. 8 forgets the + 1; 10 doubles 5 instead; 5 forgets to call the function. A function takes an input (parameter) and can hand back a result (return value).*
   - @4.3.ident
7. Which TWO are identifiers, meaning names a programmer gives to things in code? (Select 2)
   - **[x] A variable named totalPrice**  - **[x] A function named calculateTax**  - [ ] The ELSE keyword  - [ ] A comment line explaining the code
   - *Identifiers are names chosen by the programmer for variables, constants, arrays and functions. ELSE is a built-in keyword of the language, and comments are notes ignored by the computer.*
   - @4.3.ident
8. Trace this pseudocode. What is the final value of total? ¶ total = 10 ¶ total = total + 5 ¶ total = total * 2
   - **[x] 30**  - [ ] 20  - [ ] 25  - [ ] 15
   - *Run it in order: total = 10, then 10 + 5 = 15, then 15 * 2 = 30. 20 forgets the + 5 step (10 * 2); 25 does it in the wrong order (10 * 2 + 5). The value changes, which is why total is a variable.*
   - @4.3.ident
9. In an online shop, a Product object has name, price and colour, plus addToCart() and applyDiscount(). What are name, price and colour?
   - **[x] Properties (attributes) of the object**  - [ ] Methods of the object  - [ ] Separate arrays  - [ ] Comments for the programmer
   - *Properties, also called attributes, describe what an object HAS or IS. Methods are what it DOES, like addToCart(). Hook: properties = nouns and adjectives, methods = verbs. Analogy: a car's colour vs its drive() action.*
   - @4.3.obj
10. Using the same Product object, what is applyDiscount()?
   - **[x] A method**  - [ ] A property  - [ ] An attribute  - [ ] A constant
   - *A method is an action an object can perform, written like a function that belongs to the object. Properties and attributes are its data. The brackets () are a hint that it does something.*
   - @4.3.obj
11. A Dog object has breed = "Collie" and a bark() method. Which line MOST likely changes a property?
   - **[x] myDog.breed = "Poodle"**  - [ ] myDog.bark()  - [ ] print "bark"  - [ ] WHILE myDog.bark()
   - *Setting myDog.breed gives a new value to a property. myDog.bark() calls a method, which runs an action. The dot means "belonging to this object".*
   - @4.3.obj
12. A school system models students as objects. Which TWO would MOST likely be methods? (Select 2)
   - **[x] enrol()**  - **[x] printReport()**  - [ ] dateOfBirth  - [ ] studentID
   - *Methods are actions: enrolling a student, printing a report. dateOfBirth and studentID describe the student, so they are properties (attributes). Hook: if you can put "do" in front of it, it is a method.*
   - @4.3.obj
13. A bank account object has a balance and a deposit() method. A customer deposits $50 into an account holding $200. What is the balance property afterwards?
   - **[x] 250**  - [ ] 200  - [ ] 50  - [ ] 150
   - *The deposit() method acts on the object and updates its balance property: 200 + 50 = 250. 150 is a withdrawal; 200 forgets the update. Methods often change an object's properties.*
   - @4.3.obj
14. What BEST describes an object in programming?
   - **[x] A bundle of related data (properties) and actions (methods)**  - [ ] A value that can only be true or false  - [ ] A note that the computer ignores  - [ ] A diagram of boxes and arrows
   - *An object groups what something is (properties/attributes) with what it does (methods). A true/false value is a Boolean; an ignored note is a comment; boxes and arrows are a flow chart.*
   - @4.3.obj
15. Before coding, a team writes the steps in plain English like "IF stock is low THEN send email". What is this called?
   - **[x] Pseudocode**  - [ ] Assembly  - [ ] A comment  - [ ] Compiled code
   - *Pseudocode is code-like plain language used to plan logic. It isn't real code and no computer runs it. Hook: PSEUDO = fake. Analogy: writing a recipe in your own words before cooking.*
   - @4.4.org
16. A new hire must change a complex function nobody explained. What would have helped her MOST?
   - **[x] Comments and documentation describing what the code does**  - [ ] More constants in the code  - [ ] Shorter variable names like x and y  - [ ] Compiling the code twice
   - *Comments are notes inside the code for humans, and documentation explains the program in more depth. The computer ignores both. Shorter names make it harder, not easier. Analogy: labels on the wires behind a TV.*
   - @4.4.org
17. A flow chart has a diamond shape with "Is the password correct?" and two arrows, Yes and No. What does the diamond represent?
   - **[x] A decision (branch)**  - [ ] A loop counter  - [ ] The start of the program  - [ ] An input of data
   - *In flow charts, a diamond is a decision with a yes/no question; each arrow is a different path. Ovals are start/end, rectangles are process steps, and parallelograms are input/output.*
   - @4.4.org
18. A flow chart reads: Start -> Input two numbers -> Add them -> Display result -> End. What concept does this show?
   - **[x] A sequence of steps run in order**  - [ ] A loop that repeats forever  - [ ] A branch with two paths  - [ ] An object with methods
   - *A sequence is steps run one after another with no decisions or repeats. There is no diamond (branch) and no arrow going back (loop). Hook: sequence = a straight line.*
   - @4.4.org
19. A developer builds a racing game using Car objects, each with speed and colour properties and accelerate() and brake() methods. Which technique is this?
   - **[x] Object-oriented programming**  - [ ] Pseudocode planning  - [ ] Markup  - [ ] Query writing
   - *Object-oriented programming (OOP) organises code around objects that bundle properties and methods. It makes code reusable: create many Car objects from one design. Analogy: one cookie cutter, many cookies.*
   - @4.4.org
20. Which TWO are planning or organising tools used BEFORE writing real code? (Select 2)
   - **[x] Pseudocode**  - **[x] A flow chart**  - [ ] A compiler  - [ ] A Boolean
   - *Pseudocode (plain-language steps) and flow charts (diagrams) plan the logic first. A compiler is a tool that translates finished code, and a Boolean is a data type.*
   - @4.4.org
21. In many languages a line starting with // or # is ignored when the program runs. What is its purpose?
   - **[x] To leave a comment explaining the code to people**  - [ ] To declare a constant  - [ ] To start a loop  - [ ] To call a function
   - *Comments are skipped by the computer and exist only to help humans understand the code. Good comments explain WHY, not just what. Hook: comments talk to people, code talks to the computer.*
   - @4.4.org
22. Trace this pseudocode. What is printed? ¶ age = 16 ¶ IF age >= 18 THEN ¶   print "Adult" ¶ ELSE ¶   print "Minor" ¶ END IF
   - **[x] Minor**  - [ ] Adult  - [ ] Adult then Minor  - [ ] Nothing is printed
   - *16 >= 18 is false, so the ELSE branch runs and prints Minor. Only one branch of an IF/ELSE runs, never both. This is branching: the program picks a path.*
   - @4.4.logic
23. Trace this pseudocode. What is printed last? ¶ count = 0 ¶ WHILE count < 3 ¶   count = count + 1 ¶   print count ¶ END WHILE
   - **[x] 3**  - [ ] 2  - [ ] 4  - [ ] 0
   - *Loop runs: count 0 -> 1 (print 1), 1 -> 2 (print 2), 2 -> 3 (print 3). Now 3 < 3 is false, so it stops. Last printed is 3. 2 is tempting if you forget the add happens before print; 4 if you think it runs once more.*
   - @4.4.logic
24. Trace this pseudocode. What is the final value of sum? ¶ sum = 0 ¶ FOR i = 1 TO 4 ¶   sum = sum + i ¶ END FOR
   - **[x] 10**  - [ ] 4  - [ ] 6  - [ ] 15
   - *1 + 2 + 3 + 4 = 10. 6 stops at 3 (1+2+3); 15 goes up to 5. A FOR loop repeats a fixed number of times. Hook: write a little table of i and sum for each pass.*
   - @4.4.logic
25. A smart thermostat program must keep checking the temperature until the room reaches 21 degrees. Which logic is BEST?
   - **[x] A loop such as WHILE temperature < 21**  - [ ] A single IF statement run once  - [ ] A constant set to 21  - [ ] A comment saying "heat to 21"
   - *A loop repeats a check until a condition changes. A single IF checks only once and then moves on. Analogy: waiting at the kettle, checking again and again until it boils.*
   - @4.4.logic
26. A ticket app charges $5 for children and $12 for adults depending on age. Which logic concept BEST handles this?
   - **[x] Branching**  - [ ] Looping  - [ ] Sequence only  - [ ] An array
   - *Branching (IF/ELSE) chooses between paths based on a condition, here age. Looping repeats steps; it doesn't choose a price. Hook: branch = fork in the road.*
   - @4.4.logic
27. Trace this pseudocode. What is printed? ¶ score = 75 ¶ IF score >= 90 THEN print "A" ¶ ELSE IF score >= 70 THEN print "B" ¶ ELSE print "C"
   - **[x] B**  - [ ] A  - [ ] C  - [ ] A and B
   - *75 >= 90 is false, so check the next test: 75 >= 70 is true, so print B and skip the rest. Branches are checked top to bottom and only the first true one runs.*
   - @4.4.logic
28. A programmer writes this and the program never stops: ¶ x = 1 ¶ WHILE x > 0 ¶   x = x + 1 ¶ END WHILE ¶ What is the MOST likely cause?
   - **[x] The condition is always true, so it is an infinite loop**  - [ ] The IF branch has no ELSE  - [ ] x should be a string  - [ ] A comment is missing
   - *x starts at 1 and only grows, so x > 0 is never false and the loop never ends. Fix: change the condition or make x move toward it. Analogy: a treadmill with no stop button.*
   - @4.4.logic
29. Trace this pseudocode. What is printed? ¶ x = 7 ¶ IF x > 10 THEN ¶   print "Big" ¶ ELSE ¶   print "Small" ¶ END IF ¶ print "Done"
   - **[x] Small, then Done**  - [ ] Big, then Done  - [ ] Small only  - [ ] Done only
   - *7 > 10 is false, so Small is printed. The last line sits outside the IF, so it always runs: Done. Trap: forgetting steps after the branch still run in sequence.*
   - @4.4.logic
30. A flow chart has a decision "More items to scan?" whose Yes arrow points BACK to the "Scan item" box. What does this show?
   - **[x] A loop**  - [ ] A sequence with no decisions  - [ ] An object property  - [ ] A comment
   - *An arrow that goes back to an earlier step means repeat, which is looping. The decision decides when to stop: when the answer is No, the flow leaves the loop.*
   - @4.4.logic
31. Trace this pseudocode. What is printed? ¶ prices = [4, 6, 10] ¶ total = 0 ¶ FOR EACH p IN prices ¶   total = total + p ¶ END FOR ¶ print total
   - **[x] 20**  - [ ] 10  - [ ] 16  - [ ] 3
   - *The loop visits each array item: 0 + 4 = 4, 4 + 6 = 10, 10 + 10 = 20. 3 is the number of items, not their total; 10 is the last item or a half-finished total. Arrays and loops often work together.*
   - @4.4.logic
32. Trace this pseudocode. What is printed? ¶ n = 10 ¶ WHILE n > 4 ¶   n = n - 3 ¶ END WHILE ¶ print n
   - **[x] 4**  - [ ] 1  - [ ] 7  - [ ] 10
   - *10 > 4 so n = 7; 7 > 4 so n = 4; 4 > 4 is false, so stop. Print 4. 1 is one pass too many; 7 is one too few. Hook: check the condition before each pass.*
   - @4.4.logic
33. Trace this pseudocode. What is printed? ¶ loggedIn = true ¶ IF loggedIn = true THEN ¶   print "Welcome" ¶ ELSE ¶   print "Please sign in" ¶ END IF
   - **[x] Welcome**  - [ ] Please sign in  - [ ] Welcome, then Please sign in  - [ ] true
   - *loggedIn is the Boolean true, so the condition passes and the THEN branch runs; the ELSE branch is skipped. Booleans are the natural type for conditions in branches and loops.*
   - @4.4.logic
34. A developer is told: "Use a loop to check each of the 30 names in the class array and an IF to flag any that are blank." Which TWO logic concepts does this combine? (Select 2)
   - **[x] Looping**  - **[x] Branching**  - [ ] Compiling  - [ ] Markup
   - *The loop repeats the check for every name; the IF branches to flag only blanks. Most real programs mix sequence, loops and branches. Compiling and markup are about language types, not logic.*
   - @4.4.logic

## Test 13 - 5.1 + 5.2 Value of Data, Flat Files vs Databases, Storing Data (31 Q)

1. A bakery owner says, "Our customer email list is just a file, it is not worth anything." Which response BEST explains why the list is a business asset?
   - **[x] It helps the bakery earn money, so losing it would cost the business**  - [ ] It is stored on a computer, so it counts as hardware  - [ ] It takes up disk space, which the bakery pays for  - [ ] It must be printed and filed to count as an asset
   - *Data is an asset because it has value: it brings in sales and informs decisions. Analogy: like stock on the shelves, it is worth money and worth protecting. Hardware and disk space are about where data lives, not its value. Printing has nothing to do with it.*
   - @5.1.asset
2. An online shop is listing which data needs the strongest protection and the fastest recovery. Which item is MOST critical?
   - **[x] Customer orders and payment records**  - [ ] Photos from last year's staff party  - [ ] Draft designs for an old logo  - [ ] The office canteen menu
   - *Critical data = the business cannot run without it. No orders means no shop. The others are non-critical: annoying to lose but work carries on. Analogy: house keys versus a fridge magnet.*
   - @5.1.asset
3. A small firm has limited backup space. Which approach is BEST?
   - **[x] Protect critical data first, then non-critical data if space allows**  - [ ] Back up the largest files first because they took longest to make  - [ ] Back up the oldest files first because they are most at risk  - [ ] Back up everything equally and skip anything that does not fit
   - *Priority follows value, not size or age. Hook: in a fire, grab the passports before the magazines. Size and age are tempting but say nothing about how much the business depends on the data.*
   - @5.1.asset
4. Which statement about non-critical data is MOST accurate?
   - **[x] The business can keep running if it is lost, though it may still have some value**  - [ ] It has no value at all and should be deleted  - [ ] It is any data stored in the cloud rather than locally  - [ ] It is any data that already has a backup copy
   - *Non-critical does not mean worthless; it means its loss does not stop operations. Where data is stored, or whether it is backed up, does not decide how critical it is.*
   - @5.1.asset
5. A gym manager wants to decide which classes to cut. Which is the MOST data-driven approach?
   - **[x] Review attendance records for each class over the last six months**  - [ ] Ask the longest-serving instructor which classes feel quiet  - [ ] Cut the classes the manager personally likes least  - [ ] Keep the timetable and decide again next year
   - *Data-driven = decisions based on collected facts, not opinion or habit. The instructor's feeling is tempting but it is a guess, not measured data. Analogy: checking the forecast before planning a picnic.*
   - @5.1.biz
6. A café records every sale at the till with the time, item and price. Which step of using data is this?
   - **[x] Capture and collection**  - [ ] Monetization  - [ ] Meaningful reporting  - [ ] Correlation
   - *Capture/collection is gathering raw facts as they happen; it comes before any analysis or reporting. Monetization is earning money from data. Correlation is spotting a relationship. Analogy: a tally chart by the till.*
   - @5.1.biz
7. A shop's data shows umbrella sales rise on rainy days. A manager concludes "selling umbrellas makes it rain". What is the BEST correction?
   - **[x] The two are correlated, but that does not prove one causes the other**  - [ ] The data must be wrong because the result is impossible  - [ ] Umbrella sales are non-critical data and should be ignored  - [ ] The finding is Big Data and needs special tools to read
   - *Correlation = two things change together. It is useful for planning (stock more umbrellas when rain is forecast) but it does not show cause. The data is fine; the conclusion is wrong.*
   - @5.1.biz
8. A sales director has a 40-page spreadsheet export but needs to decide quickly which region is falling behind. What would help MOST?
   - **[x] A short report with a chart comparing sales by region**  - [ ] A larger export with every raw transaction included  - [ ] A copy of the database stored on a flash drive  - [ ] A list of every column name in the sales table
   - *Meaningful reporting turns raw data into something a person can act on. More raw data makes the problem worse. Hook: data is the ingredients, a report is the meal.*
   - @5.1.biz
9. A fitness app company sells anonymised, aggregated exercise trends to sportswear brands. What is this an example of?
   - **[x] Data monetization**  - [ ] Data capture  - [ ] Data persistence  - [ ] Data correlation
   - *Monetization = making money from data, by selling it, selling insights, or using it to target products. Capture is collecting it; persistence is it staying stored. Selling trends is turning data into revenue.*
   - @5.1.biz
10. A national card-payment network handles millions of transactions per minute and wants to spot fraud patterns across all of them. Which term BEST describes this data?
   - **[x] Big Data**  - [ ] A flat file  - [ ] Non-critical data  - [ ] A key/value pair
   - *Big Data = data so large, fast and varied that ordinary tools struggle, so it needs special analytics. One big spreadsheet is not Big Data. Analogy: counting every raindrop in a storm, not one bucket.*
   - @5.1.biz
11. A supermarket analyses loyalty-card purchases and finds families who buy nappies often also buy coffee, so it places them on the same promotion. What is this process called?
   - **[x] Data analytics**  - [ ] Data backup  - [ ] Data import  - [ ] Data persistence
   - *Analytics = examining data to find patterns that support decisions. Backup copies data, import loads it, persistence keeps it. Only analytics produces the insight.*
   - @5.1.biz
12. A library sets up a new database. Before any book details can be entered, what must happen FIRST?
   - **[x] Create the database and its tables**  - [ ] Run a report of overdue books  - [ ] Query for books by a given author  - [ ] Restore the database from backup
   - *Database uses run in a natural order: create the structure, input/import data, query it, report on it. You cannot query or report on tables that do not exist. Analogy: build the shelves before shelving the books.*
   - @5.2.uses
13. A shop has 5,000 products in a supplier's CSV file and wants them in its new database without retyping. What is the BEST action?
   - **[x] Import the CSV file into the database**  - [ ] Create a report from the CSV file  - [ ] Query the CSV file for each product one by one  - [ ] Back up the CSV file to the cloud
   - *Import = bringing existing data in from another source in bulk. Input is typing it in manually. A report or query reads data that is already there. Backing up just copies the file.*
   - @5.2.uses
14. A receptionist needs to find every patient with an appointment on Friday. Which database function is she using?
   - **[x] Query**  - [ ] Create  - [ ] Import  - [ ] Constraint
   - *A query asks the database a question and returns matching records. Create builds structure, import loads data, a constraint is a rule on what data is allowed. Hook: query = ask.*
   - @5.2.uses
15. A database query reads: `SELECT Name FROM Customers WHERE City = 'Leeds';` What will it return?
   - **[x] The names of customers whose city is Leeds**  - [ ] Every column for customers in Leeds  - [ ] The names of all customers, sorted by city  - [ ] A new table called Leeds
   - *SELECT picks the column(s) (Name), FROM picks the table (Customers), WHERE filters the rows (City = 'Leeds'). Every column would need SELECT *. Nothing is sorted or created. Read it like a sentence: show Name from Customers where City is Leeds.*
   - @5.2.uses
16. A Products table has columns Name and Price. Which query lists every product costing more than 20?
   - **[x] `SELECT Name, Price FROM Products WHERE Price > 20;`**  - [ ] `SELECT Products FROM Name WHERE Price > 20;`  - [ ] `SELECT Name, Price FROM Products WHERE Price < 20;`  - [ ] `SELECT Price > 20 FROM Products WHERE Name;`
   - *Pattern: SELECT columns FROM table WHERE condition. The second option swaps table and column. The third uses less-than, giving cheap products. The fourth jumbles the parts.*
   - @5.2.uses
17. A manager wants a printable monthly summary of sales totals by store, with headings and totals. Which database function is BEST?
   - **[x] Report**  - [ ] Import  - [ ] Create  - [ ] Input
   - *A report presents query results in a readable, formatted layout for people. Import and input put data in; create builds structure. Hook: query finds it, report shows it.*
   - @5.2.uses
18. A club stores its member list in a single spreadsheet. Now five volunteers need to update it at the same time and edits keep overwriting each other. What is the BEST next step?
   - **[x] Move the data into a database that supports concurrent users**  - [ ] Email the spreadsheet to each volunteer in turn  - [ ] Split the spreadsheet into five separate files  - [ ] Save the spreadsheet as a plain text file
   - *Databases handle many users at once, locking only what is being changed. A flat file usually allows one safe editor at a time. Five separate files would create five conflicting versions. Analogy: a shared booking system versus one paper diary passed round.*
   - @5.2.flat
19. A user keeps a 30-item shopping list for personal use. Which storage is MOST appropriate?
   - **[x] A flat file such as a simple spreadsheet or text file**  - [ ] A relational database with several linked tables  - [ ] A cloud database cluster with automatic scaling  - [ ] A document database with a schema designer
   - *Flat files suit small, simple, single-user data: quick to set up, no training needed. A database would be overkill. Hook: do not hire a lorry to carry a sandwich.*
   - @5.2.flat
20. An online store's product spreadsheet has grown to two million rows and searches now take minutes. Which TWO database advantages address this? (Select 2)
   - **[x] Scalability**  - **[x] Speed of searching large data**  - [ ] Easier to print  - [ ] No need for any structure
   - *Databases are built to scale to huge numbers of records and use indexes to search them quickly. Printing is not a database strength, and databases need more structure, not less.*
   - @5.2.flat
21. A school wants to store student names, exam marks, photos and scanned permission letters, all linked to each student. Why is a database BETTER than a flat file here?
   - **[x] It can hold a variety of data types and link them together**  - [ ] It needs no planning before data is added  - [ ] It can only be used by one person at a time  - [ ] It stores everything as plain text
   - *Databases support a variety of data (text, numbers, dates, images) and relationships between them. Flat files are usually one simple layout of plain data. Databases need more planning, not less.*
   - @5.2.flat
22. In a customer spreadsheet, one row holds a single customer's name, phone number and email. What is that row called?
   - **[x] A record**  - [ ] A field  - [ ] A schema  - [ ] A query
   - *A record is one complete entry about one thing. A field is one item of data, such as the phone number column. Schema is the overall design; a query is a question. Analogy: a record is one index card in a box.*
   - @5.2.flat
23. A user types an order into a database, closes the app and restarts the PC. The next day the order is still there. Which concept does this show?
   - **[x] Data persistence**  - [ ] Data correlation  - [ ] Data monetization  - [ ] Data compression
   - *Persistence = data stays saved after the program closes or power goes off, because it is on storage, not just in RAM. Analogy: writing in pen in a notebook rather than on a steamed-up window.*
   - @5.2.store
24. A sales rep visits farms with no mobile signal but must look up customer details there. Which setup is BEST?
   - **[x] A local copy on the laptop that works offline and syncs later**  - [ ] A cloud-only database that needs an internet connection  - [ ] A database on the office server reached over VPN  - [ ] A shared spreadsheet edited live in a web browser
   - *Offline access needs the data stored locally. Cloud-only, VPN and browser-based options all fail without a connection. Syncing later keeps the central copy up to date.*
   - @5.2.store
25. A company with staff in five countries wants everyone to reach the same database from anywhere, without running its own servers. Which option is BEST?
   - **[x] A cloud-hosted database**  - [ ] A database on one employee's laptop  - [ ] A flat file on a USB flash drive  - [ ] A local database on the head office PC
   - *Cloud storage gives availability from anywhere with internet access, and the provider runs the hardware. A laptop, flash drive or single office PC is only available where that device is and when it is switched on.*
   - @5.2.store
26. What is the MAIN availability drawback of storing a database only in the cloud?
   - **[x] It cannot be reached if the internet connection fails**  - [ ] It cannot be backed up  - [ ] Only one user can open it at a time  - [ ] Data disappears when the app is closed
   - *Cloud = available anywhere online, unavailable when offline. Cloud data can be backed up, supports many users, and persists. Hook: cloud is great until the Wi-Fi dies.*
   - @5.2.store
27. A shop's till stores the day's sales in a local database on the till itself. What is the MAIN availability benefit compared to cloud-only storage?
   - **[x] Sales can still be recorded during an internet outage**  - [ ] Head office can see sales from anywhere instantly  - [ ] The data is automatically copied to another country  - [ ] No backups are ever needed
   - *Local storage keeps working offline. Remote viewing and off-site copies are cloud strengths. Local data still needs backups, because the till could fail.*
   - @5.2.store
28. A marketing team wants to check whether sales tend to rise around the dates its newsletter goes out. Which order of steps is MOST sensible?
   - **[x] Collect sales data, look for a correlation with send dates, then report the findings**  - [ ] Report the findings, then collect sales data to support them  - [ ] Look for a correlation first, then decide what data to collect  - [ ] Sell the sales data, then use the income to fund the newsletter
   - *Data-driven flow: capture/collect, analyse (correlation), then report meaningfully. Reporting before collecting is guesswork. You cannot find a correlation in data you do not have yet.*
   - @5.1.biz
29. A hospital IT lead is sorting its data into critical and non-critical. Which question BEST decides which group a data set belongs in?
   - **[x] Could the hospital keep operating safely if this data were lost?**  - [ ] How many megabytes does the data take up?  - [ ] Is the data stored in the cloud or on a local server?  - [ ] How long ago was the data first created?
   - *Criticality is about dependence: if work stops or patients are put at risk without it, it is critical. Size, location and age do not decide how much the organisation relies on it. Hook: ask "what breaks if this vanishes?"*
   - @5.1.asset
30. A query against an Orders table reads: `SELECT * FROM Orders WHERE Total >= 100;` An order has a Total of exactly 100. Is it returned?
   - **[x] Yes, because >= means greater than or equal to**  - [ ] No, because only totals above 100 are returned  - [ ] No, because * means only the first column is returned  - [ ] Yes, but only its Total column is shown
   - *>= includes the boundary value, so 100 matches. > alone would exclude it. * means all columns, so the whole row is shown, not just Total.*
   - @5.2.uses
31. A shop assistant types each new phone order into an on-screen form, and the form saves it into the database. Which database use is this?
   - **[x] Input**  - [ ] Import  - [ ] Query  - [ ] Report
   - *Input = entering data by hand, one record at a time, usually through a form. Import loads a batch of existing data from another file. Query asks questions of stored data; a report presents it. Hook: input is typed, import is loaded.*
   - @5.2.uses

## Test 14 - 5.3 + 5.4 Relational vs Non-relational Databases, Backups (31 Q)

1. A company wants to store customer names, phone numbers and postcodes in fixed columns that every record shares. What type of data is this?
   - **[x] Structured**  - [ ] Semistructured  - [ ] Non-structured  - [ ] Encrypted
   - *Structured = fixed rows and columns, every record has the same fields. Hook: a form where every box is the same. Encrypted is about secrecy, not structure.*
   - @5.3.struct
2. A developer stores settings in a JSON (JavaScript Object Notation) file. Each entry has labelled fields, but different entries can have different fields. How is this data BEST described?
   - **[x] Semistructured**  - [ ] Structured  - [ ] Non-structured  - [ ] Relational
   - *Semistructured = labels/tags give some organisation but no fixed table layout. JSON and XML are classic examples. Not fully structured because fields vary; not non-structured because labels exist.*
   - @5.3.struct
3. A marketing team has a folder of promotional videos and voice recordings. How is this data BEST described?
   - **[x] Non-structured**  - [ ] Structured  - [ ] Semistructured  - [ ] Relational
   - *Non-structured (unstructured) data has no fields or labels inside it: video, audio, images, free text. Hook: a shoebox of photos versus a filled-in form.*
   - @5.3.struct
4. An email has set fields such as To, From and Subject, plus a free-text body. How is an email usually classified?
   - **[x] Semistructured**  - [ ] Structured  - [ ] Non-structured  - [ ] Key/value
   - *A mix of labelled fields and free content is semistructured. The fixed headers tempt "structured", but the body has no set layout. It is not a database type like key/value.*
   - @5.3.struct
5. Which data type is HARDEST to search and analyse with a standard relational database query?
   - **[x] Non-structured data such as recorded phone calls**  - [ ] Structured data in a sales table  - [ ] Semistructured data with labelled JSON fields  - [ ] A table of employee IDs and names
   - *Relational queries work on columns. Recordings have no columns, so they need special tools (for example speech-to-text) before analysis. Structured tables are easiest; semistructured is in between.*
   - @5.3.struct
6. A shop has a Customers table (CustomerID, Name, Email) and an Orders table (OrderID, CustomerID, Total). In the Customers table, what is CustomerID MOST likely to be?
   - **[x] The primary key**  - [ ] A foreign key  - [ ] The schema  - [ ] A constraint name
   - *A primary key uniquely identifies each row in its own table. Analogy: a passport number, no two people share it. In the Orders table the same column would be the foreign key.*
   - @5.3.rel
7. Using the same tables, what is CustomerID in the Orders table?
   - **[x] A foreign key that links each order to a customer**  - [ ] The primary key of the Orders table  - [ ] A record that holds the whole customer  - [ ] A semistructured field
   - *A foreign key is a column that points to the primary key of another table, creating the relationship. OrderID is the Orders primary key. Hook: foreign key = a reference to someone else's ID.*
   - @5.3.rel
8. A database designer documents which tables exist, what columns each has, their data types and how tables link. What is this design called?
   - **[x] The schema**  - [ ] A record  - [ ] A report  - [ ] A query
   - *The schema is the blueprint of a relational database's structure. Analogy: the architect's floor plan, not the furniture. Records are the data inside; reports and queries use the data.*
   - @5.3.rel
9. In a Products table, which describes a column (field) rather than a row (record)?
   - **[x] Price, holding one value for every product**  - [ ] All details of the blue kettle  - [ ] Product 42 with its name and price  - [ ] The last product added today
   - *A column/field is one attribute across every record. A row/record is one complete item. Hook: rows run across (one thing), columns run down (one property).*
   - @5.3.rel
10. A database rule stops anyone saving an order with a negative quantity or with no customer. What is this rule called?
   - **[x] A constraint**  - [ ] A foreign key  - [ ] A report  - [ ] A schema
   - *Constraints enforce rules on data: NOT NULL, UNIQUE, value ranges, valid foreign keys. They keep bad data out. A foreign key is one kind of constraint, but the broader answer is constraint.*
   - @5.3.rel
11. A clerk tries to add a second customer with the same CustomerID as an existing one, and the database refuses. Which TWO explain why? (Select 2)
   - **[x] CustomerID is the primary key, so it must be unique**  - **[x] A constraint is enforcing that uniqueness**  - [ ] The table has no schema  - [ ] Foreign keys must always be blank
   - *Primary keys must be unique and not empty, and the database enforces that with a constraint. Every relational table has a schema. Foreign keys normally hold a value pointing to another table.*
   - @5.3.rel
12. A web app needs to store user preferences such as theme = dark and language = en, looked up instantly by a name. Which database type is the BEST fit?
   - **[x] Key/value**  - [ ] Relational  - [ ] Document  - [ ] Flat file
   - *Key/value stores pair a unique key with a value for very fast lookups. Analogy: a coat-check ticket, hand in the number, get the coat. Relational tables would be overkill for simple pairs.*
   - @5.3.nosql
13. A blog platform stores each post as a self-contained JSON item holding the title, body, tags and comments, and posts can have different fields. Which database type is this?
   - **[x] Document**  - [ ] Key/value  - [ ] Relational  - [ ] Flat file
   - *Document databases store whole semistructured documents (often JSON), each able to have its own fields. Key/value only maps a key to a value, without querying inside. Relational needs fixed columns.*
   - @5.3.nosql
14. A startup's product data changes shape often: some items have sizes, others colours, others neither. Which choice is BEST?
   - **[x] A non-relational document database**  - [ ] A relational database with a fixed schema  - [ ] A single flat text file  - [ ] A key/value store with one key for the whole catalogue
   - *Non-relational document databases handle varying fields without changing a schema. Relational needs every row to fit the same columns. One key for everything throws away lookup by item.*
   - @5.3.nosql
15. Which statement BEST contrasts relational and non-relational databases?
   - **[x] Relational uses tables with a fixed schema; non-relational stores data more flexibly, such as key/value pairs or documents**  - [ ] Relational cannot be queried; non-relational can  - [ ] Relational stores only images; non-relational stores only text  - [ ] Relational works offline only; non-relational works online only
   - *The core difference is structure: tables and keys versus flexible models. Both can be queried, store many data types, and run locally or in the cloud.*
   - @5.3.nosql
16. A key/value store saves a shopping basket as cart123 = [kettle, toaster]. Which part is the key?
   - **[x] cart123**  - [ ] [kettle, toaster]  - [ ] kettle  - [ ] The equals sign
   - *The key is the unique name used to look the data up (cart123); the value is what is stored under it (the list of items). Hook: the key is the label on the locker, the value is what is inside.*
   - @5.3.nosql
17. An accounting team needs strict links between invoices, customers and payments, with rules preventing an invoice for a customer that does not exist. Which database type is BEST?
   - **[x] Relational**  - [ ] Key/value  - [ ] Document  - [ ] Non-structured file store
   - *Relational databases enforce relationships with primary/foreign keys and constraints, ideal for financial data. Non-relational stores are flexible but do not enforce links as strictly.*
   - @5.3.nosql
18. A user wants to protect only her Documents and Photos folders each night. Which backup type is BEST?
   - **[x] File backup**  - [ ] System backup  - [ ] Restore  - [ ] Disk defragmentation
   - *A file backup copies chosen files and folders: smaller and faster. A system backup copies the whole machine. Restore gets data back; defragmenting just tidies a drive.*
   - @5.4.bak
19. A design studio's PC failed and took two days to reinstall the OS, apps and settings. What backup would have MOST reduced that downtime?
   - **[x] A system backup (image of the whole computer)**  - [ ] A file backup of the Desktop folder  - [ ] A printed list of installed software  - [ ] A copy of the browser bookmarks
   - *A system backup captures the OS, apps, settings and files so the whole machine can be rebuilt in one go. File backups only save data, so you still reinstall everything else.*
   - @5.4.bak
20. A user accidentally deletes a spreadsheet and last night's backup exists. What is the process of getting it back called?
   - **[x] Restoring**  - [ ] Importing  - [ ] Querying  - [ ] Archiving
   - *Restoring = copying data from a backup back to where it is used. Importing loads data into a database from another format. Hook: backup puts it in the safe; restore takes it out.*
   - @5.4.bak
21. An office has backed up every night for a year but has never tried restoring anything. What is the BEST next step?
   - **[x] Test a restore to confirm the backups actually work**  - [ ] Stop backing up, since nothing has gone wrong  - [ ] Delete older backups to save space  - [ ] Switch from file backups to no backups
   - *A backup is only useful if it can be restored. Testing catches corrupt or incomplete backups before an emergency. Analogy: check the spare tyre has air before the puncture.*
   - @5.4.bak
22. Which TWO statements about file and system backups are correct? (Select 2)
   - **[x] A system backup can rebuild the operating system and applications**  - **[x] A file backup is usually smaller and quicker than a system backup**  - [ ] A file backup includes installed programs  - [ ] A system backup cannot be restored to new hardware in any case
   - *System = whole machine; file = selected data, so smaller and faster. File backups do not capture installed programs. System images can often be restored to replacement hardware.*
   - @5.4.bak
23. A ransomware attack encrypts a shop's PC. The owner has a system backup from yesterday. What should happen FIRST to recover after the PC is cleaned or wiped?
   - **[x] Restore the system backup**  - [ ] Create a new database schema  - [ ] Run a sales report  - [ ] Import a supplier CSV file
   - *Restoring the backup returns the machine to its last good state. The other actions do not recover lost data. Hook: backups are the main way to recover from ransomware without paying.*
   - @5.4.bak
24. A student wants a cheap, pocket-sized copy of her coursework to take between home and college. Which option is BEST?
   - **[x] A USB flash drive**  - [ ] An external hard drive  - [ ] A system backup to a NAS  - [ ] A tape library
   - *Flash drives are small, cheap and portable, ideal for a few files. An external HDD holds more but is bulkier. NAS and tape are office-scale options, not pocket copies.*
   - @5.4.loc
25. A photographer needs to back up 3 TB of RAW photos locally each week. Which option is BEST?
   - **[x] An external hard drive**  - [ ] A single SD card  - [ ] A USB flash drive  - [ ] Burning them to DVDs
   - *External HDDs give large capacity at low cost per GB, suiting terabytes of data. SD cards and flash drives are typically much smaller. DVDs would need hundreds of discs.*
   - @5.4.loc
26. A drone pilot's camera records to removable media, and she keeps a spare copy of each flight on a second card. What local storage is she using?
   - **[x] SD card**  - [ ] External HDD  - [ ] Cloud storage  - [ ] Optical disc
   - *SD (Secure Digital) cards are small removable flash media used in cameras, drones and phones. They work as quick local backups but are easy to lose.*
   - @5.4.loc
27. A small office keeps its only backup on an external drive in the same room as its server. What risk does this MOST leave uncovered?
   - **[x] A fire or flood could destroy both the server and the backup**  - [ ] The backup will be too slow to restore  - [ ] The backup cannot hold system images  - [ ] Staff will not be able to read the files
   - *Backups in the same place share the same disasters and theft. Keep at least one copy off-site, for example in the cloud. Analogy: do not keep the spare house key inside the house.*
   - @5.4.loc
28. Which is the MAIN advantage of cloud backup over a local external drive?
   - **[x] The copy is stored off-site and can be reached from anywhere online**  - [ ] It works with no internet connection  - [ ] Restoring large data is always faster  - [ ] It never has any ongoing cost
   - *Cloud backups survive local disasters and are reachable anywhere online. They need internet, large restores are often slower than a local drive, and they usually have subscription costs.*
   - @5.4.loc
29. A freelancer wants backups that are quick to restore AND survive a house fire. Which TWO should she use together? (Select 2)
   - **[x] An external hard drive at home**  - **[x] A cloud storage backup**  - [ ] A second folder on the same internal drive  - [ ] A copy on the same laptop's desktop
   - *Local gives fast restores; cloud gives off-site safety. Copies on the same drive fail together with that drive, so they are not real backups.*
   - @5.4.loc
30. In a relational database, Orders has CustomerID 7, but no customer with ID 7 exists in Customers. The database refuses to save the order. What is the MOST likely reason?
   - **[x] A foreign key constraint requires the customer to exist first**  - [ ] The Orders table has no primary key  - [ ] Relational databases cannot store numbers  - [ ] The schema only allows document data
   - *A foreign key must match an existing primary key in the linked table; the constraint blocks orphan records. This keeps the data consistent.*
   - @5.3.rel
31. A query reads: `SELECT OrderID FROM Orders WHERE CustomerID = 7;` What does it return?
   - **[x] The order IDs of all orders placed by customer 7**  - [ ] Customer 7's name and email  - [ ] Order number 7 only  - [ ] Every column of every order
   - *The WHERE filter matches the foreign key CustomerID, so it finds all of that customer's orders, showing only OrderID. Name and email live in Customers, not Orders. Order 7 would need WHERE OrderID = 7.*
   - @5.3.rel

## Test 15 - 6.1 Confidentiality, Integrity, Availability, Privacy, AAA (23 Q)

1. A thief breaks into a shop's server and downloads its customer list but changes nothing. Which security goal was broken?
   - **[x] Confidentiality**  - [ ] Integrity  - [ ] Availability  - [ ] Accounting
   - *Confidentiality = only the right people can see data. The list was read, not changed, so integrity tempts but is fine. The server stayed up, so availability is fine. Accounting is the record of what users did, not a goal that gets broken. Analogy: someone reading your diary without tearing out pages.*
   - @6.1.cia
2. An attacker quietly changes the prices in an online store's database so items sell for 1 cent. Which goal of the CIA triad is MOST directly affected?
   - **[x] Integrity**  - [ ] Confidentiality  - [ ] Availability  - [ ] Authorization
   - *Integrity = data stays correct and is changed only by people allowed to change it. Nothing secret leaked, so not confidentiality. The site still works, so not availability. Authorization decides who may edit, but the triad goal that suffered is integrity. Hook: integrity = "is it still true?"*
   - @6.1.cia
3. A flood of fake traffic knocks a ticket-selling website offline for a whole day. Which goal was hit?
   - **[x] Availability**  - [ ] Integrity  - [ ] Confidentiality  - [ ] Non-repudiation
   - *Availability = systems and data are there when people need them. No data was read or changed. Non-repudiation is proof someone did something, unrelated. Analogy: a shop with its shutters jammed closed.*
   - @6.1.cia
4. A small office wants to keep its file server working if one hard drive fails. Which goal does adding a second mirrored drive MOSTLY support?
   - **[x] Availability**  - [ ] Confidentiality  - [ ] Integrity  - [ ] Authentication
   - *A spare copy keeps the service running, so availability. Mirroring does not hide data from anyone (confidentiality) or prove who logged in (authentication). Integrity tempts because data is copied, but the goal here is staying up. Analogy: a spare tyre.*
   - @6.1.cia
5. A company wants to be sure a downloaded contract file has not been altered since it was sent. Which goal is it checking?
   - **[x] Integrity**  - [ ] Availability  - [ ] Confidentiality  - [ ] Authorization
   - *Checking a file is unchanged is integrity. Confidentiality would be about who can read it. Availability is whether you can get it at all. Hook: integrity = untampered. Analogy: an unbroken seal on a jar.*
   - @6.1.cia
6. Which action BEST protects confidentiality of payroll files on a shared drive?
   - **[x] Limit folder access to the HR team only**  - [ ] Make a nightly backup copy of the folder  - [ ] Add a second power supply to the server  - [ ] Show the file size in the folder view
   - *Restricting who can open the files keeps them secret. Backups and power supplies help availability, a common mix-up. File size has nothing to do with security.*
   - @6.1.cia
7. A help desk worker sees a staff member's home address and phone number in a ticket. What kind of data is this?
   - **[x] PII**  - [ ] Public data  - [ ] Metadata only  - [ ] Open source data
   - *PII (Personally Identifiable Information) = data that points to one person: name, address, phone, ID numbers. Public data is meant for anyone. Metadata is data about data, like file dates. Analogy: the label on a posted parcel.*
   - @6.1.priv
8. Which of these items is MOST clearly PII?
   - **[x] A customer's passport number**  - [ ] The store's opening hours  - [ ] The average price of milk  - [ ] The number of staff in a team
   - *A passport number identifies exactly one person. The others are general facts about no specific person. Hook: if it can find a single human, it is PII.*
   - @6.1.priv
9. A web shop based in the US sells to customers in France and Germany. Which regulation MOST likely sets rules for how it handles their personal data?
   - **[x] GDPR**  - [ ] WPA3  - [ ] HTTPS  - [ ] SSO
   - *GDPR (General Data Protection Regulation) is the EU law protecting personal data of people in the EU, wherever the company is based. WPA3 is Wi-Fi security, HTTPS is web encryption, SSO is a login method. Trap: all four are real acronyms, only one is a law.*
   - @6.1.priv
10. A website shows a pop-up asking visitors to accept or reject tracking cookies before continuing. Why does it MOST likely do this?
    - **[x] Privacy rules require consent before tracking**  - [ ] Cookies make the site load much faster  - [ ] The pop-up blocks all viruses on the page  - [ ] It is needed for the HTTPS padlock to show
    - *Cookie consent comes from privacy laws such as GDPR: users must agree before non-essential tracking. The pop-up does not speed loading, stop viruses or affect certificates. Analogy: asking before taking someone's photo.*
    - @6.1.priv
11. Sam wants to share holiday photos on social media without strangers learning where he lives. What should he do FIRST?
    - **[x] Set the account to private and check who can see posts**  - [ ] Post the photos only in the evening  - [ ] Use a longer caption under each photo  - [ ] Add more hashtags to each post
    - *Privacy settings control who sees the posts, which is the real protection. Posting time, captions and hashtags do nothing for privacy, and hashtags make posts easier to find. Hook: lock the door before decorating the room.*
    - @6.1.priv
12. An employee needs to send a spreadsheet of customer bank details to a colleague. Which method BEST respects privacy?
    - **[x] Share it through the company's access-controlled file share**  - [ ] Attach it to a message on a public chat group  - [ ] Upload it to a free public file link site  - [ ] Paste the details into a personal email account
    - *An access-controlled company share limits who can open the file. Public chat, public links and personal email all risk the data reaching the wrong people. Analogy: handing a letter over in person instead of pinning it on a notice board.*
    - @6.1.priv
13. Before chatting with a stranger over an instant messaging app, which habit BEST protects your privacy?
    - **[x] Do not share personal details such as address or date of birth**  - [ ] Turn on read receipts so they know you saw messages  - [ ] Use a profile photo with your house in the background  - [ ] Share your phone number so they can verify you
    - *Messages can be saved, forwarded or screenshotted, so keep PII out of IM. Read receipts, revealing photos and sharing your number all give away more information. Hook: assume every chat could end up on a screen you do not control.*
    - @6.1.priv
14. To log in, a user enters a password and then a code sent to her phone. What is this called?
    - **[x] MFA**  - [ ] SSO  - [ ] Single factor  - [ ] Least privilege
    - *MFA (Multifactor Authentication) = two or more different factor types: something you know (password) plus something you have (phone). SSO (Single Sign-On) is one login for many apps. Single factor is just the password. Least privilege is about permissions, not login.*
    - @6.1.aaa
15. A user logs in once in the morning and can then open email, the HR portal and the file share without logging in again. What is this?
    - **[x] SSO**  - [ ] MFA  - [ ] Accounting  - [ ] Non-repudiation
    - *SSO (Single Sign-On) = one login unlocks many systems. MFA is about the number of factor types, not the number of apps. Accounting logs activity. Analogy: one wristband that gets you into every ride at a theme park.*
    - @6.1.aaa
16. Which login method is single-factor authentication?
    - **[x] A password and a PIN**  - [ ] A password and a fingerprint  - [ ] A smart card and a PIN  - [ ] A fingerprint and a phone code
    - *A password and a PIN are both "something you know", so it is still one factor type even with two steps. Each other pair mixes two different types (know, have, are), so those are MFA. Trap: two steps does not mean two factors.*
    - @6.1.aaa
17. A new receptionist needs to book meeting rooms. Following least privilege, what access should she get?
    - **[x] Only the booking system access her job needs**  - [ ] Administrator rights on all office computers  - [ ] The same access as the IT manager  - [ ] Full access now, trimmed later if problems appear
    - *Least privilege = give only the access needed to do the job, nothing more. Admin rights or copying a manager's access gives far more than needed. "Trim later" usually never happens. Analogy: a hotel key card that opens only your own room.*
    - @6.1.aaa
18. Why should a home user do daily web browsing with a standard user account rather than an administrator account?
    - **[x] Malware that runs gets fewer rights to change the system**  - [ ] Websites load faster on a standard account  - [ ] Standard accounts do not need a password  - [ ] Admin accounts cannot open a web browser
    - *An admin account lets anything you run install software and change settings, including malware. A standard account limits the damage. Speed, passwords and browser access are not the reason. Hook: drive in normal mode, use admin only for repairs.*
    - @6.1.aaa
19. A manager wants to see which staff member opened a confidential report last Tuesday. Which part of AAA helps MOST?
    - **[x] Accounting**  - [ ] Authentication  - [ ] Authorization  - [ ] Availability
    - *Accounting = recording who did what and when, through logs. Authentication proves who you are; authorization decides what you can open. Availability is a CIA goal. Analogy: a visitors' sign-in book. Hook: AAA in order is who are you, what may you do, what did you do.*
    - @6.1.aaa
20. Which are examples of accounting (tracking user activity)? (Select 2)
    - **[x] Browser history**  - **[x] Location tracking on a company phone**  - [ ] A password policy  - [ ] A WPA3 Wi-Fi setting
    - *Browser history and location tracking both record what a user did or where they went. A password policy is about authentication. WPA3 is Wi-Fi encryption. Hook: if it leaves a trail you can look back on, it is accounting.*
    - @6.1.aaa
21. A user signs an online contract with a digital signature, then later claims she never agreed. Which concept means she cannot believably deny it?
    - **[x] Non-repudiation**  - [ ] Availability  - [ ] Authorization  - [ ] Single sign-on
    - *Non-repudiation = proof that a person did an action, so they cannot deny it. Digital signatures and detailed logs provide it. Authorization only says what she was allowed to do, not that she did it. Analogy: a signed delivery receipt.*
    - @6.1.aaa
22. A staff member can log in to the payroll app but gets "access denied" when trying to open the salary report. Which step stopped her?
    - **[x] Authorization**  - [ ] Authentication  - [ ] Accounting  - [ ] Integrity
    - *She already proved who she is (authentication worked). The app then checked her permissions and refused, which is authorization. Accounting may log the attempt but does not block it. Analogy: the passport check lets you into the airport, but your boarding pass decides which plane.*
    - @6.1.aaa
23. Ransomware locks a clinic's appointment files so staff cannot open them. Logs show no files were copied out and none were edited. Which goal of the CIA triad was MOST directly hit?
    - **[x] Availability**  - [ ] Confidentiality  - [ ] Integrity  - [ ] Accounting
    - *Staff cannot get to the data when they need it, so availability is hit. Nothing was copied out (confidentiality) or edited (integrity). Accounting is part of AAA, and here the logs did their job. Hook: if people cannot use it, think availability.*
    - @6.1.cia

## Test 16 - 6.2 Staying Safe: Awareness, Securing Devices, Licensing, Safe Sources, Browsing (26 Q)

1. Lee gets an email that looks like it is from his bank, saying his account is locked and asking him to click a link and enter his password. What is this MOST likely?
   - **[x] Phishing**  - [ ] A software patch  - [ ] A firewall alert  - [ ] A licence renewal
   - *Phishing = fake messages that trick people into giving away details or clicking bad links. Urgency plus a request for a password is the classic sign. Banks do not ask for passwords by email. Analogy: a fisherman's bait. Hook: urgent + link + login = phish.*
   - @6.2.aware
2. Someone phones the office pretending to be from IT and asks a worker to read out her password "to fix an urgent problem". What is this?
   - **[x] Social engineering**  - [ ] Anti-malware scanning  - [ ] Software piracy  - [ ] Patching
   - *Social engineering = tricking people rather than hacking machines. Real IT staff should never need your password. The other options are tools or licence issues. Hook: the attacker hacks the human.*
   - @6.2.aware
3. An email from an unknown sender has an attachment called invoice.pdf.exe. What should the user do FIRST?
   - **[x] Not open it and report it to IT**  - [ ] Open it to see what the invoice is for  - [ ] Forward it to colleagues to ask their opinion  - [ ] Reply and ask the sender if it is safe
   - *The .exe at the end means it is a program pretending to be a PDF, a common way to spread malware. Reporting lets IT warn others. Opening or forwarding spreads risk, and replying confirms your address is active. Analogy: a parcel you did not order that is ticking.*
   - @6.2.aware
4. A worker finds a USB stick labelled "Salaries 2025" in the car park. What is the BEST action?
   - **[x] Hand it to IT without plugging it in**  - [ ] Plug it in to find out who owns it  - [ ] Plug it into a home PC instead of a work PC  - [ ] Format it and keep it as a spare
   - *Dropped USB sticks are a known trick to get malware onto a computer: curiosity does the work. Plugging it in anywhere risks infection. Handing it in keeps you safe. Hook: found media is bait.*
   - @6.2.aware
5. A trusted news website starts showing pop-ups saying "Your PC is infected, call this number now". What is the MOST likely explanation?
   - **[x] The site or its adverts are compromised and showing malicious content**  - [ ] Your antivirus is warning you through the website  - [ ] The site has upgraded its HTTPS certificate  - [ ] Your PC needs a Wi-Fi password change
   - *Even real sites can be compromised or serve bad adverts. Fake virus warnings with phone numbers are scams. Real antivirus warns through its own app, not a web page. Close the tab and do not call.*
   - @6.2.aware
6. Which signs suggest an email is a phishing attempt? (Select 2)
   - **[x] The sender address does not match the company name**  - **[x] It demands action within one hour or the account closes**  - [ ] It is addressed to you and sent during office hours  - [ ] It comes from a colleague you emailed yesterday about the same topic
   - *Mismatched sender addresses and pressure to act fast are classic phishing signs. Normal timing and an expected reply from a known colleague are ordinary, though still check anything odd. Hook: scammers rush you so you do not think.*
   - @6.2.aware
7. An old app on a laptop has a known security hole, and the vendor has released a fix. What is the BEST action?
   - **[x] Install the update (patch) now**  - [ ] Buy a cable lock for the laptop  - [ ] Turn the screen brightness down  - [ ] Change the desktop wallpaper
   - *Patching closes known holes. Attackers look for unpatched systems. A cable lock stops theft, not software attacks. Analogy: fixing a broken window lock once you know it is broken.*
   - @6.2.secure
8. Which tool BEST blocks unwanted network traffic from the internet from reaching a PC?
   - **[x] Firewall**  - [ ] Anti-malware  - [ ] Cable lock  - [ ] Password manager
   - *A firewall allows or blocks traffic by rules. Anti-malware finds harmful files that already arrived. A cable lock is physical. A password manager stores logins. Analogy: a security guard at the building door checking who comes in.*
   - @6.2.secure
9. A user downloaded a file that turns out to hide a virus. Which tool is MOST likely to detect and remove it?
   - **[x] Anti-malware software**  - [ ] A firewall rule  - [ ] A USB port lock  - [ ] Security awareness training
   - *Anti-malware scans files and removes harmful software. A firewall controls traffic, not files already saved. USB locks block ports. Training helps people avoid the download in the first place, but cannot remove it.*
   - @6.2.secure
10. A sales rep often works from hotel lobbies with her laptop. Which physical control BEST prevents someone walking off with it while she gets coffee?
    - **[x] A cable lock attached to the table**  - [ ] A longer screen timeout  - [ ] A WPA3 Wi-Fi network  - [ ] An open-source office suite
    - *A cable lock ties the laptop to something solid. A longer screen timeout actually weakens security. WPA3 and software choice do nothing against theft. Analogy: a bike lock.*
    - @6.2.secure
11. A school wants to stop students plugging their own USB sticks into lab PCs. Which control fits BEST?
    - **[x] USB port locks**  - [ ] Cable locks  - [ ] Longer passwords  - [ ] Cookie consent banners
    - *USB locks physically block the ports. Cable locks stop theft of the whole device, not port use. Passwords and cookie banners do not control USB ports.*
    - @6.2.secure
12. Which steps BEST secure a new home laptop? (Select 2)
    - **[x] Turn on automatic updates**  - **[x] Set a strong login password or PIN**  - [ ] Turn off the built-in firewall to speed things up  - [ ] Share the admin account with all family members
    - *Updates patch holes and a login protects against anyone who picks up the device. Disabling the firewall removes protection, and sharing an admin account breaks least privilege and accountability.*
    - @6.2.secure
13. A small business wants an office app it pays for once and keeps using forever, with no monthly fee. Which licence type fits?
    - **[x] Perpetual**  - [ ] Subscription  - [ ] Pirated  - [ ] Trial
    - *Perpetual = pay once, use that version for good (updates may cost extra). Subscription charges regularly and stops working if you stop paying. Piracy is illegal copying. Trials expire. Note: "one-time" and perpetual both mean paying once.*
    - @6.2.lic
14. A charity wants software whose source code anyone can read and change, usually free of charge. Which type should it look for?
    - **[x] Open source**  - [ ] Proprietary  - [ ] Subscription  - [ ] Pirated
    - *Open source = code is public and can be changed and shared under its licence. Proprietary software is owned by a company that keeps the code secret. Subscription is a payment model, not about code access. Analogy: a public recipe vs a secret family recipe.*
    - @6.2.lic
15. A friend offers Jo a copy of a paid photo editor plus a key generator so she does not have to pay. What is this?
    - **[x] Software piracy, which is illegal and risky**  - [ ] Open-source sharing, which is allowed  - [ ] A normal perpetual licence transfer  - [ ] A free trial from the publisher
    - *Using paid software without paying is piracy. It breaks the licence and the law, and cracked copies often carry malware. Open source is free because the owner allows it, not because someone cracked it.*
    - @6.2.lic
16. After installing paid software, it asks for a 25-character code printed on the receipt. What is this code?
    - **[x] A product key**  - [ ] A Wi-Fi pre-shared key  - [ ] A digital certificate  - [ ] A cookie
    - *A product key (or serial number) proves you bought a valid licence and activates the software. A PSK is a Wi-Fi password. Certificates prove a website's identity. Cookies are small website files.*
    - @6.2.lic
17. Mia wants a free PDF reader. Which source is SAFEST?
    - **[x] The developer's official website or the official app store**  - [ ] A pop-up advert offering a "free download"  - [ ] A file-sharing site with a cracked version  - [ ] A link in an email from an unknown sender
    - *Official sites and app stores check software and give real copies. Ads, cracked downloads and unknown email links are common ways to spread malware. Hook: get software from the shop, not from the back of a van.*
    - @6.2.src
18. A new laptop's graphics driver is out of date. Where should the user get the update?
    - **[x] The OEM (original manufacturer) support site**  - [ ] A random third-party "driver booster" site  - [ ] A forum post with a download link  - [ ] A USB stick from a stranger
    - *OEM (Original Equipment Manufacturer) drivers are made and tested for that hardware. Third-party driver sites can bundle unwanted software or malware. Hook: go to whoever made the part.*
    - @6.2.src
19. A new laptop came with several trial games and toolbars the user will never use. What is the BEST action?
    - **[x] Uninstall the unwanted and unnecessary software**  - [ ] Leave them installed in case they are needed  - [ ] Turn off the firewall so they run better  - [ ] Copy them to a USB stick as a backup
    - *Removing unneeded software frees space and removes things that could have security holes. Less software means less to attack and patch. Analogy: clearing out a cluttered garage.*
    - @6.2.src
20. Anti-malware finds a malicious browser extension. What should the user do?
    - **[x] Remove the extension and run a full scan**  - [ ] Disable the anti-malware so the extension works  - [ ] Ignore it if the browser still opens  - [ ] Install a second copy of the extension
    - *Malicious software should be removed and the device scanned for anything else left behind. Disabling protection or ignoring it leaves the threat active.*
    - @6.2.src
21. A browser shows "Your connection is not private: certificate is invalid" when Tom visits his bank's site. What should he do?
    - **[x] Stop and not enter details; check the address or contact the bank**  - [ ] Click "proceed anyway" and log in as normal  - [ ] Turn off the browser's warnings for good  - [ ] Clear his cookies and type his password again
    - *A certificate proves a site is who it claims to be. An invalid one may mean a fake site or an attack, so do not send passwords. Bypassing or disabling warnings removes the safety net. Analogy: a bank cashier with no ID badge.*
    - @6.2.browse
22. Which are signs of a valid, secure website connection? (Select 2)
    - **[x] The address starts with https://**  - **[x] The browser shows no certificate warning**  - [ ] The page has a lot of flashing adverts  - [ ] The site asks you to disable your antivirus
    - *HTTPS with a valid certificate (no warning) means the connection is encrypted and the site's identity checked. Flashing ads and requests to disable antivirus are red flags. Note: HTTPS proves encryption, not that the site is honest.*
    - @6.2.browse
23. An employee wants to paste a confidential client contract into a free public AI chatbot to summarise it. What is the BEST advice?
    - **[x] Do not paste confidential data; the service may store or use it**  - [ ] It is fine because AI chatbots are always private  - [ ] It is fine if he deletes the chat afterwards  - [ ] Paste it but remove only the page numbers
    - *Many public AI tools may keep what you type and use it for training. Confidential data should stay out unless the company approves the tool. Deleting the chat may not remove it from the provider. Hook: treat a public AI chat like a public forum.*
    - @6.2.browse
24. Kim uses free public Wi-Fi in a cafe. Which habit BEST protects her privacy while browsing?
    - **[x] Use only HTTPS sites and avoid logging in to sensitive accounts**  - [ ] Turn on file sharing so friends can send files  - [ ] Accept every cookie pop-up quickly  - [ ] Post her location on social media while there
    - *On public Wi-Fi others may watch traffic, so stick to encrypted sites and save banking for a trusted network or a VPN. File sharing, accepting all cookies and posting location all expose more about her.*
    - @6.2.browse
25. A designer pays a monthly fee for a photo app, always gets the latest version, and loses access if she stops paying. Which licence type is this?
    - **[x] Subscription**  - [ ] Perpetual  - [ ] Open source  - [ ] Product key
    - *Subscription = regular payments for continued use, usually with updates included. Perpetual is pay once and keep. Open source is about public code. A product key activates a licence but is not a licence type. Analogy: renting a flat versus buying one.*
    - @6.2.lic
26. A company sells accounting software, keeps its source code secret and forbids customers from changing it. How is this software BEST described?
    - **[x] Proprietary**  - [ ] Open source  - [ ] Pirated  - [ ] Public domain
    - *Proprietary software is owned by its maker, who controls the code and the licence terms. Open source shares the code for anyone to read and change. Pirated means used without a valid licence. Hook: proprietary = property of the company.*
    - @6.2.lic

## Test 17 - 6.3 Passwords + Password Managers (20 Q)

1. Which password is the STRONGEST?
   - **[x] Purple-Kettle-Rain-42-Window**  - [ ] Password1  - [ ] Summer2025  - [ ] qwerty123
   - *Length beats almost everything: a long passphrase with mixed characters is hardest to guess. The others are short and appear on common-password lists. Hook: long and random beats short and clever.*
   - @6.3.pw
2. A company policy says passwords must include upper case, lower case, numbers and symbols. Which best practice is this?
   - **[x] Complexity**  - [ ] History  - [ ] Expiration  - [ ] Single sign-on
   - *Complexity = using a mix of character types so there are more possible combinations. History stops reuse of old passwords. Expiration forces changes after a set time. SSO is a login method.*
   - @6.3.pw
3. A system will not let Raj reuse any of his last 10 passwords. Which setting is this?
   - **[x] Password history**  - [ ] Password length  - [ ] Password complexity  - [ ] Password manager
   - *Password history remembers old passwords so users cannot cycle back to them. Length and complexity are about the new password's makeup. Analogy: a shop that remembers you already returned that item.*
   - @6.3.pw
4. A policy forces users to change their password every 90 days. What is this called?
   - **[x] Expiration**  - [ ] History  - [ ] Complexity  - [ ] Reset
   - *Expiration (password age) sets how long a password lasts before it must change. A reset is what happens when you forget it. Analogy: a milk carton's use-by date.*
   - @6.3.pw
5. Ana uses the same password for her email, shopping and bank accounts. The shopping site is breached. What is the MAIN risk?
   - **[x] Attackers can try that password on her other accounts**  - [ ] Her password becomes too short  - [ ] Her bank account becomes open source  - [ ] Her Wi-Fi switches to WPA
   - *Reusing passwords means one breach unlocks many accounts, because attackers try leaked passwords on other sites. Use a different password for each site. Analogy: one key that opens your house, car and office.*
   - @6.3.pw
6. Which change MOST improves a password's strength?
   - **[x] Making it much longer**  - [ ] Swapping the letter o for a 0  - [ ] Adding the current year at the end  - [ ] Using your pet's name in capitals
   - *Each extra character multiplies the number of guesses needed, so length matters most. Swapping letters for numbers, adding a year and using pet names are tricks attackers already try first.*
   - @6.3.pw
7. Which are good password practices? (Select 2)
   - **[x] Use a different password for every site**  - **[x] Use long passphrases**  - [ ] Write passwords on a note stuck to the monitor  - [ ] Use your birthday so it is easy to remember
   - *Unique passwords stop one breach spreading, and long passphrases are hard to guess yet easy to remember. Sticky notes can be seen by anyone, and birthdays are easy to find online.*
   - @6.3.pw
8. A worker says, "I just add 1 to my password each time it expires." Why is this a weak habit?
   - **[x] Attackers who know an old password can easily guess the new one**  - [ ] It makes the password too long to type  - [ ] It turns off password history  - [ ] It breaks the company firewall
   - *Predictable changes (Pass1, Pass2, Pass3) defeat the point of expiration. History blocks exact repeats, but not small tweaks. Hook: a new password should not be guessable from the old one.*
   - @6.3.pw
9. A password policy needs a minimum length. Which minimum is BEST for a user account today?
   - **[x] 12 or more characters**  - [ ] 4 characters  - [ ] 6 characters  - [ ] 8 characters with no other rules
   - *Short passwords can be guessed quickly by computers. Current advice favours long passwords of 12 or more characters. 4 or 6 is far too short, and 8 is now seen as a bare minimum at best.*
   - @6.3.pw
10. Which password is the WEAKEST?
    - **[x] admin**  - [ ] Tr0mbone!Lake-Sunset  - [ ] 7#kQ9z!pLm2v  - [ ] correct-horse-battery-staple-9
    - *"admin" is short, a common default and on every attacker's list. The others are long, mixed or random. Hook: if it could be a default, it is weak.*
    - @6.3.pw
11. Leo has 60 online accounts and struggles to remember a unique password for each. What is the BEST solution?
    - **[x] Use a password manager**  - [ ] Use one strong password for all of them  - [ ] Save them in a text file on the desktop  - [ ] Use his name plus the site name
    - *A password manager stores and fills unique, strong passwords in an encrypted vault, so he only remembers one master password. Reuse, plain text files and predictable patterns are all risky. Analogy: a locked safe for all your keys.*
    - @6.3.mgmt
12. What is a key benefit of a password manager?
    - **[x] It can create long random passwords and fill them in for you**  - [ ] It makes Wi-Fi faster  - [ ] It removes the need for any password at all  - [ ] It turns off MFA on all accounts
    - *Password managers generate and remember strong unique passwords, so you can use them without memorising them. You still need a strong master password and they do not touch Wi-Fi speed. MFA can and should stay on.*
    - @6.3.mgmt
13. Why is the master password of a password manager so important?
    - **[x] It unlocks every password stored in the vault**  - [ ] It is shared with every website you visit  - [ ] It is only used once and then deleted  - [ ] It sets the Wi-Fi encryption type
    - *The master password protects the whole vault, so it should be long and unique and ideally backed by MFA. Websites never see it. Analogy: the key to the safe holding all your other keys.*
    - @6.3.mgmt
14. Before choosing a password manager, which privacy question MATTERS most?
    - **[x] Is the vault encrypted so the provider cannot read your passwords?**  - [ ] Does it come with lots of colour themes?  - [ ] Does it show adverts on the login page?  - [ ] Can it change your desktop wallpaper?
    - *A good password manager encrypts the vault so only you can unlock it, not even the company. Themes, ads and wallpaper have nothing to do with privacy.*
    - @6.3.mgmt
15. Nia forgot her email password. What is the SAFEST way to get back in?
    - **[x] Use the official "forgot password" reset on the real site**  - [ ] Reply to an email offering to reset it for a fee  - [ ] Ask a friend to guess it for her  - [ ] Click a reset link in a text from an unknown number
    - *Use the official reset process, which usually checks identity through a recovery email, phone or code. Unexpected reset messages are a common phishing trick. Hook: start the reset yourself; never follow one someone sends you.*
    - @6.3.mgmt
16. A family installs a new smart camera that came with the login admin / admin. What should they do FIRST?
    - **[x] Change the default username and password**  - [ ] Leave it, because nobody knows the brand  - [ ] Write the default on the camera  - [ ] Turn off the camera's updates
    - *Default logins are published online and attackers scan for them. Changing them is the first step for any new device. Hiding the brand does not help. Analogy: changing the locks when you move into a new house.*
    - @6.3.mgmt
17. A shared office PC logs straight into the desktop with no password. What is the BEST fix?
    - **[x] Enable a password or PIN on the account**  - [ ] Turn down the screen brightness  - [ ] Move the PC closer to the window  - [ ] Install more games on it
    - *Enabling a password stops anyone who walks by from using the PC and its data. Brightness, position and games do not control access. Hook: no password = open door.*
    - @6.3.mgmt
18. When setting up account recovery, a site asks for an answer to "What is your pet's name?" Tom's dog's name appears in many of his public social media posts. What is the BEST approach?
    - **[x] Use an answer that others cannot find or guess, and store it in his password manager**  - [ ] Use the dog's real name so he will remember it  - [ ] Leave the answer blank  - [ ] Use the same answer on every site
    - *Reset details are a back door into the account, so they must be as hard to guess as a password. Anything posted online is easy for attackers to find. Storing the made-up answer in a password manager means he will not forget it. Hook: a recovery answer is a second password.*
    - @6.3.mgmt
19. A phone app asks to turn on a screen lock with a PIN. Why is this a good idea?
    - **[x] It stops anyone who finds the phone from opening it**  - [ ] It makes the battery last longer  - [ ] It makes the phone connect to Wi-Fi faster  - [ ] It turns off all app updates
    - *Enabling a screen lock password or PIN protects the phone if lost or stolen. It does not affect battery, Wi-Fi speed or updates.*
    - @6.3.mgmt
20. A password manager warns that one saved password appeared in a known data breach. What should the user do?
    - **[x] Change that password on the site to a new unique one**  - [ ] Ignore it if the site still works  - [ ] Copy the same password to more sites  - [ ] Delete the password manager
    - *A breached password is known to attackers, so change it right away to a new unique one, ideally generated by the manager. Breach alerts are one of the privacy benefits of password managers.*
    - @6.3.mgmt

## Test 18 - 6.4 + 6.5 Encryption + Wi-Fi Security (22 Q)

1. A message reads "Meet at noon" before encryption and "x8#Qf!2pL" after. What are these called, in order?
   - **[x] Plain text, then cipher text**  - [ ] Cipher text, then plain text  - [ ] Hash, then key  - [ ] Key, then certificate
   - *Plain text = readable original. Cipher text = scrambled result after encryption. Only the right key turns cipher text back. Hook: cipher = coded.*
   - @6.4.rest
2. A company laptop is stolen from a car. Which protection BEST keeps the files on it secret?
   - **[x] Full disk encryption**  - [ ] A strong Wi-Fi password  - [ ] HTTPS on the company website  - [ ] A VPN to the office
   - *Disk encryption protects data at rest: without the key, the thief only sees cipher text. Wi-Fi, HTTPS and VPN protect data moving across networks (in transit), not files stored on a stolen drive.*
   - @6.4.rest
3. Which are examples of data at rest? (Select 2)
   - **[x] Photos stored on a locked phone**  - **[x] Files on an encrypted USB stick in a drawer**  - [ ] A web page loading over HTTPS  - [ ] Work traffic sent through a VPN
   - *Data at rest is stored, not moving. HTTPS and VPN traffic is moving across a network, so it is in transit. Hook: rest = sitting still.*
   - @6.4.rest
4. A user wants to protect one sensitive spreadsheet on a shared PC without encrypting the whole drive. What should she use?
   - **[x] File encryption on that spreadsheet**  - [ ] A VPN connection  - [ ] WPA3 on the router  - [ ] A cookie consent banner
   - *File-level encryption protects a single file at rest. A VPN and WPA3 protect data moving over networks. Cookie banners are about web privacy.*
   - @6.4.rest
5. Why should a phone used for work have device encryption and a screen lock turned on?
   - **[x] If it is lost, the stored data cannot easily be read**  - [ ] It makes calls clearer  - [ ] It stops all phishing emails  - [ ] It makes app downloads faster
   - *Mobile device encryption protects stored data at rest; the screen lock stops casual access and usually unlocks the key. It does not affect call quality, stop phishing or speed up downloads.*
   - @6.4.rest
6. Without the right key, what does an attacker see when opening an encrypted file?
   - **[x] Unreadable cipher text**  - [ ] The original plain text  - [ ] A list of all your passwords  - [ ] The file's original author only
   - *Encryption turns data into cipher text that is useless without the key. That is the whole point: stolen data stays secret. Hook: no key, no meaning.*
   - @6.4.rest
7. Ben sees a padlock and "https://" when shopping online. What does this mainly protect?
   - **[x] His card details while they travel to the site**  - [ ] His files stored on his laptop  - [ ] His phone if it is stolen  - [ ] His router's admin password
   - *HTTPS (Hypertext Transfer Protocol Secure) encrypts data in transit between browser and website. It does nothing for stored files, a stolen phone or router settings.*
   - @6.4.transit
8. An employee working from a hotel needs to reach company files safely over the hotel Wi-Fi. What is the BEST option?
   - **[x] Connect through the company VPN**  - [ ] Use disk encryption only  - [ ] Turn off the laptop firewall  - [ ] Share the files over a public link
   - *A VPN (Virtual Private Network) creates an encrypted tunnel across an untrusted network, protecting data in transit. Disk encryption protects stored files, not the connection. The other options weaken security. Analogy: a private tunnel under a busy road.*
   - @6.4.transit
9. A lawyer must send a confidential contract by email so only the client can read it. What should she use?
   - **[x] Email encryption**  - [ ] A longer subject line  - [ ] Full disk encryption on her PC  - [ ] A different font
   - *Email encryption protects the message in transit (and often in the mailbox) so only the recipient can read it. Disk encryption protects her own PC, not the sent email. Subject lines and fonts do nothing.*
   - @6.4.transit
10. Which are examples of data in transit? (Select 2)
    - **[x] A banking app sending a payment to the bank's server**  - **[x] A web page loading over HTTPS**  - [ ] Photos saved on a phone's storage  - [ ] Backups kept on an external drive
    - *Data in transit is moving across a network. Mobile apps should encrypt what they send, just as HTTPS does. Saved photos and backups are data at rest.*
    - @6.4.transit
11. A shopping site's login page uses http:// with no padlock. What is the MAIN risk?
    - **[x] The password could be read while travelling over the network**  - [ ] The site will run slower on phones  - [ ] The password will be too short  - [ ] The site cannot show images
    - *Without HTTPS, data is sent as plain text, so anyone on the path (like public Wi-Fi) could read it. Speed, password length and images are not the issue.*
    - @6.4.transit
12. Priya saves a report on her encrypted laptop drive, then emails it to a client. While the email is crossing the internet, what protects the report?
    - **[x] Encryption of data in transit, such as email encryption**  - [ ] Her laptop's full disk encryption  - [ ] The screen lock on her laptop  - [ ] Her password manager's vault
    - *Disk encryption only protects the copy stored on her drive (at rest); once the file leaves the laptop it needs in-transit protection such as email encryption. Screen locks and password vaults do not protect a message on the network. Hook: is it travelling or sitting?*
    - @6.4.transit
13. Jo sets up a new home router. All her devices are new. Which Wi-Fi security type should she choose?
    - **[x] WPA3**  - [ ] WPA  - [ ] WPA2  - [ ] Open
    - *WPA3 (Wi-Fi Protected Access 3) is the newest and strongest. WPA2 is still common but older. WPA is outdated and weak. Open has no encryption. Order weakest to strongest: Open, WPA, WPA2, WPA3.*
    - @6.5.wifi
14. Which Wi-Fi option sends traffic with no encryption at all?
    - **[x] Open**  - [ ] WPA  - [ ] WPA2  - [ ] WPA3
    - *An open network needs no password and does not encrypt traffic, so anyone nearby could read it. All WPA versions encrypt, though WPA is old and weak. Analogy: shouting across a room instead of passing a sealed note.*
    - @6.5.wifi
15. Put these in order from WEAKEST to STRONGEST.
    - **[x] Open, WPA, WPA2, WPA3**  - [ ] WPA3, WPA2, WPA, Open  - [ ] WPA, Open, WPA3, WPA2  - [ ] WPA2, WPA, Open, WPA3
    - *Open has no encryption, then each WPA version gets stronger. Hook: higher number = newer = stronger.*
    - @6.5.wifi
16. On a home network using WPA2 or WPA3 Personal, everyone joins with the same Wi-Fi password. What is this shared password called?
    - **[x] Pre-shared key (PSK)**  - [ ] Product key  - [ ] Digital certificate  - [ ] Master password
    - *A PSK (pre-shared key) is the shared Wi-Fi password set on the router. A product key activates software, a certificate proves a website's identity, and a master password unlocks a password manager.*
    - @6.5.wifi
17. Which Wi-Fi password (PSK) is BEST?
    - **[x] A long random phrase such as River-Pocket-Lantern-73**  - [ ] The word wifi  - [ ] The house number  - [ ] The default printed on the router
    - *A long random PSK is hard to guess. "wifi" and a house number are easy guesses, and the printed default may be visible to visitors or guessable for that model.*
    - @6.5.wifi
18. Jo's router broadcasts the network name "BrandX-5G-1234". What is the BEST new SSID?
    - **[x] A new name that does not reveal the brand, owner or address**  - [ ] Her full name and house number  - [ ] Her Wi-Fi password, so guests remember it  - [ ] Keep the default brand name
    - *The SSID (Service Set Identifier) is the network name. Changing it from the default hides the router model, which could hint at known weaknesses. It should not give away personal details or the password.*
    - @6.5.wifi
19. Which steps BEST secure a new small office Wi-Fi network? (Select 2)
    - **[x] Change the router's default admin password**  - **[x] Turn on WPA3 (or WPA2 if devices need it) with a strong PSK**  - [ ] Leave the network open so visitors can join easily  - [ ] Pick WPA because it is the oldest and most tested
    - *Default admin logins are public and encryption with a strong key stops strangers joining or snooping. Open networks offer no protection and WPA is outdated and weak.*
    - @6.5.wifi
20. A neighbour has been using Lisa's Wi-Fi without asking. What should Lisa do FIRST on the router?
    - **[x] Change the Wi-Fi password (PSK) to a new strong one**  - [ ] Change the SSID only  - [ ] Turn the router upside down  - [ ] Switch from WPA2 to Open
    - *A new PSK disconnects anyone using the old one. Renaming the SSID alone does not change the password. Switching to Open would let even more people in.*
    - @6.5.wifi
21. A cafe offers free Wi-Fi for customers but wants to stop strangers reading their traffic. Which choice is BEST?
    - **[x] An encrypted network (WPA2 or WPA3) with a password shown at the till**  - [ ] An open network with a friendly SSID  - [ ] An open network that hides its SSID  - [ ] The router's default settings
    - *Encryption protects traffic over the air even if many people know the password. An open network, hidden or not, sends traffic unencrypted. Default settings leave default passwords in place.*
    - @6.5.wifi
22. An older printer only supports WPA2, while all other devices support WPA3. What is the MOST sensible choice?
    - **[x] Use WPA2/WPA3 mixed mode, or replace the printer when possible**  - [ ] Switch the whole network to Open  - [ ] Switch everything to the original WPA  - [ ] Remove the Wi-Fi password entirely
    - *Most routers can run a WPA2/WPA3 mode so older devices still join with encryption. Dropping to Open, WPA or no password makes the whole network weaker for one device.*
    - @6.5.wifi

