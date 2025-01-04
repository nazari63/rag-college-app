
### COMPUTER AND INFORMATION SECURITY

### (CSC 583)

# Taught by Dr. O. Adeleke

# Lecture One: Introduction to Computer Security

## Introduction

It‘s hard to find a facet of modern life that does not involve a computer system, at least on some level.
Online purchases, debit cards, and automatic bill pay are standard parts of modern life. Some retailers
are using computerized automatic checkout. Because so much of our business is transacted online, a
great deal of personal information is stored in computers. Medical records, tax records, school records,
and more are all stored in computer databases.
This leads to some very important questions:
How is information safeguarded? What are the vulnerabilities to these systems? What steps are taken
to ensure that these systems and data are safe?
This lesson outlines current dangers, describes the most common types of attacks on your personal
computer and network, teaches you how to speak the lingo of both hackers and security professionals,
and outlines the broad strokes of what it takes to secure your computer and your network.


## 1.1 Understanding Computer Security

The first step in understanding computer security is to formulate a realistic assessment of the threats to
those systems. You will need a clear picture of the dangers in order to adequately prepare a defence.
There seem to be two extreme attitudes regarding computer security.
The first group assumes there is no real threat. Subscribers to this belief feel that there is little real
danger to computer systems, and that much of the negative news is simply unwarranted panic. They
often believe taking only minimal security precautions should ensure the safety of their systems. The
prevailing sentiment is, if our organization has not been attacked so far, we must be secure. If decision
makers subscribe to this point of view, they tend to push a reactive approach to security. They will
wait to address security issues until an incident occurs—the proverbial ―closing the barn door after
the horse has already gotten out.‖ If you are fortunate, the incident will have only minor impact on your
organization and will serve as a much needed wakeup call. If you are unfortunate, then your
organization may face serious and possible catastrophic consequences.
People who subscribe to the opposite viewpoint overestimate the dangers. They tend to assume that
talented, numerous hackers are an imminent threat to your system. They may believe that any teenager
with a laptop can traverse highly secure systems at will. Such a worldview makes excellent movie
plots, but it is simply unrealistic. The reality is that many people who call themselves hackers are less
knowledgeable than they think they are. These people have a low probability of being able to
compromise any system that has implemented even moderate security precautions. This does not mean
that skilful hackers do not exist, of course. However, they must balance the costs (financial, time)
against the rewards (ideological, monetary). ―Good‖ hackers tend to target systems that yield the
highest rewards. If a hacker doesn‘t perceive your system as beneficial to these goals, he is less likely


to expend the resources to compromise your system. It is also important to understand that real
intrusions into a network take time and effort.
Both extremes of attitudes regarding the dangers to computer systems are inaccurate. It is certainly true
that there are people who have the understanding of computer systems and the skills to compromise
the security of many, if not most, systems. A number of people who call themselves hackers, though,
are not as skilled as they claim to be.
A better way to assess the threat level to your system is to weigh the attractiveness of your system to
potential intruders against the security measures in place. Keep in mind, too, that the greatest external
threat to any system is not hackers, but malware and denial of service attacks. Malware includes
viruses, worms, Trojan horses. And beyond the external attacks, there is the issue of internal problems
due to ignorance.

## 1.2 Types of Threats to Computer Security

Most attacks can be categorized as one of six broad classes:
i. Malware: This is a generic term for software that has a malicious purpose. It includes virus attacks,
worms, adware, Trojan horses, and spyware. This is the most prevalent danger to your system.
ii. Security breaches: This group of attacks includes any attempt to gain unauthorized access to your
system. This includes cracking passwords, elevating privileges, breaking into a serve etc., all the things
you probably associate with the term hacking.
iii. Denial of service (DoS) attacks: These are designed to prevent legitimate access to your system.
iv. Web attacks: This is any attack that attempts to breach your website. Two of the most common
such attacks are SQL injection and cross-site scripting.


v. Session hijacking: These attacks are rather advanced, and involve an attacker attempting to take
over a session.
vi. DNS poisoning: This type of attack seeks to compromise a DNS server so that users can be
redirected to malicious websites, including phishing websites.

This lesson offers a broad description of each type of attack. Subsequently, we will go into greater
detail with each specific attack, how it is accomplished, and how to avoid it.

1. Malware

Malware is a generic term for software that has a malicious purpose. Three types of malware: viruses,
Trojan horses, and spyware are discussed in this lesson.
A computer virus is similar to a biological virus; both are designed to replicate and spread. The most
common method for spreading a virus is using the victim‘s email account to spread the virus to
everyone in their address book. Some viruses don‘t actually harm the system itself, but all of them
cause network slowdowns due to the heavy network traffic caused by the virus replication.
The Trojan horse gets its name from an ancient tale. The city of Troy was besieged for an extended
period of time. The attackers could not gain entrance, so they constructed a huge wooden horse and
one night left it in front of the gates of Troy. The next morning the residents of Troy saw the horse
and assumed it to be a gift, so they rolled the wooden horse into the city. Unknown to them, several
soldiers where hidden inside the horse. That evening the soldiers left the horse, opened the city gates,
and let their fellow attackers into the city. An electronic Trojan horse works the same way, appearing
to be benign software but secretly downloading a virus or some other type of malware onto your
computer from within.
Spyware is simply software that literally spies on what you do on your computer. Spyware can be as
simple as a cookie—a text file that your browser creates and stores on your hard drive—that a


website you have visited downloads to your machine and uses to recognize you when you return to the
site. However, that flat file can then be read by the website or by other websites. Any data that the file
saves can be retrieved by any website, so your entire Internet browsing history can be tracked.

2. Security Breaches

Next we will look at attacks that breach your system‘s security. This activity is what is commonly
referred to as hacking, though that is not the term hackers themselves use. We will delve into
appropriate terminology in a moment; however, it should be noted at this point that cracking is the
appropriate word for intruding into a system without permission, usually with malevolent intent. Any
attack that is designed to breach your security, either via some operating system flaw or any other
means, can be classified as cracking.
Social engineering: is a technique for breaching a system‘s security by exploiting human nature rather
than technology. The way this method works is rather simple: The perpetrator gets preliminary
information about a target organization and leverages it to obtain additional information from the
system‘s users. For instance, armed with the name of a system administrator, you might call someone
in the business‘s accounting department and claim to be one of the company‘s technical support
personnel. Mentioning the system administrator‘s name would help validate that claim, allowing you
to ask questions in an attempt to ascertain more details about the system‘s specifications. A savvy
intruder might even get the accounting person to say a username and password. As you can see, this
method is based on how well the prospective intruder can manipulate people and actually has little to
do with computer skills.

3. Denial of Service Attacks

In a denial of service (DoS), the attacker does not actually access the system. Rather, he or she simply
blocks access from legitimate users. One common way to do prevent legitimate service is to flood the


targeted system with so many false connection requests, that the system cannot respond to legitimate
requests. DoS is probably the most common attack on the Web.

4. Web Attacks

By their nature, web servers have to allow communications. Oftentimes, websites allow users to
interact with the website. Any part of a website that allows for user interaction is also a potential point
for attempting a web-based attack. SQL injections involve entering SQL (Structured Query Language)
commands into login forms (username and password text fields) in an attempt to trick the server into
executing those commands. The most common purpose is to force the server to log the attacker on,
even though the attacker does not have a legitimate username and password. While SQL injection is
just one type of web attack, it is the most common.

5. Session Hijacking

Session hijacking can be rather complex to perform. For that reason, it is not a very common form of
attack. Simply put, the attacker monitors an authenticated session between the client machine and the
server, and takes that session over.

6. DNS Poisoning

Most of your communication on the Internet will involve DNS, or Domain Name Service. DNS is what
translates the domain names you and I understand (like [http://www.ChuckEasttom.com)](http://www.ChuckEasttom.com)) into IP addresses
that computers and routers understand. DNS poisoning uses one of several techniques to compromise
that process and redirect traffic to an illicit site, often for the purpose of stealing personal information.
Page 16 of 118


## Basic Security Terminology

It is important to know some basic terminology. The security and hacking terms in this lesson are
merely an introduction to computer security terminology, but they are an excellent starting point to
help you prepare for learning more about computer security.
The world of computer security takes its vocabulary from both the professional security community
and the hacker community.

1. Hacker Slang


i. A hacker is an expert on a particular system or systems, a person who simply wants to learn more
about the system. Hackers feel that looking at a system‘s flaws is the best way to learn about that
system. For example, someone well versed in the Linux operating system who works to understand
that system by learning its weaknesses and flaws would be a hacker. This process does often mean
seeing if a flaw can be exploited to gain access to a system. This ―exploiting‖ part of the process is
where hackers differentiate themselves into three groups:

A white hat hacker: Upon finding some flaw in a system, will report the flaw to the vendor of that
system. For example, if they were to discover some flaw in Red Hat Linux, they would then email the
Red Hat company (probably anonymously) and explain exactly what the flaw is and how it was
exploited. White hat hackers are often hired specifically by companies to do penetration tests.
A black hat hacker: Is the person normally depicted in the media. Once she gains access to a system,
her goal is to cause some type of harm. She might steal data, erase files, or deface websites. Black hat
hackers are sometimes referred to as crackers.
A grey hat hacker: Is normally a law-abiding citizen, but in some cases will venture into illegal
activities. Page 17 of 118


Regardless of how hackers view themselves, intruding on any system is illegal. This means that
technically speaking all hackers, regardless of the colour of the metaphorical hat they may wear, are in
violation of the law. However, many people feel that white hat hackers actually perform a service by
finding flaw and informing vendors before those flaws are exploited by less ethically inclined
individuals.
ii. Script Kiddies

A hacker is an expert in a given system, as with any profession it includes its share of frauds. So what
is the term for someone who calls himself or herself a hacker but lacks the expertise? The most common
term for this sort of person is scrip-kiddy. The name comes from the fact that the Internet is full of
utilities and scripts that one can download to perform some hacking tasks.
Many of these tools have an easy-to-use graphical user interface that allows someone with very little
if any skill to operate the tool. A classic example is the Low Earth Orbit Ion Cannon tool for executing
a DoS attack. Someone who downloads such a tool without really understanding the target system is
considered a script kiddy.
iii. Ethical Hacking: Sneakers

When and why would someone give permission to another party to hack his system? The most common
answer is in order to assess system vulnerabilities. This employee, commonly called a sneaker, legally
breaks into a system in order to assess security deficiencies. More and more companies are soliciting
the services of such individuals or firms to assess their vulnerabilities. Anyone hired to assess the
vulnerabilities of a system should be both technically proficient and ethical. Run a criminal background
check, and avoid those people with problem pasts. There are plenty of legitimate security professionals
available who know and understand hacker skills but have never committed security crimes. If you
take the argument that hiring convicted hackers means hiring Page 18 of 118


talented people to its logical conclusion, you could surmise that obviously the person in question is not
as good a hacker as they would like to think, because they were caught.

2. Professional Terms

Security professional terminology describes defensive barrier devices, procedures, and policies. This
is quite logical because hacking is an offensive activity centred on attackers and attack methodologies,
whereas security is a defensive activity concerning itself with defensive barriers and procedures.
i. Security Devices

The most basic security device is the firewall which is a barrier between a network and the outside
world. Sometimes a firewall takes the form of a standalone server, sometimes a router, and sometimes
software running on a machine. Whatever its physical form, a firewall filters traffic entering and exiting
the network. A proxy server is often used with a firewall to hide the internal network‘s IP address and
present a single IP address (its own) to the outside world.
Firewalls and proxy servers guard the perimeter by analyzing traffic (at least inbound and in many
cases outbound as well) and blocking traffic that has been disallowed by the administrator. These two
safeguards are often augmented by an intrusion-detection system (IDS). An IDS simply monitors
traffic, looking for suspicious activity that might indicate an attempted intrusion.
ii. Security Activities

Authentication is the most basic security activity. It is merely the process of determining if the
credentials given by a user or another system (such as a username and password) are authorized to
access the system resource in question. When you log in with your username and password, the system
will attempt to authenticate that username and password. If it is authenticated, you will be granted
access. Page 19 of 118


Auditing is the process of reviewing logs, records, and procedures to determine if these items meet
standards.
The security and hacking terms that we have just covered are only an introduction to computer security
terminology, but they provide an excellent starting point that will help you prepare for learning more
about computer security.

## Post-Test

1. Discuss the two schools of thought with respect to Computer security
2. Discuss the types of threat to computer security
3. How would you differentiate among the three types of hackers?
4. How seriously should you take threats to computer security?
5. How can the level of threat to computer security be assessed?


# Lecture Two: Password

## Introduction

The use of passwords is known to be ancient. Sentries would challenge those wishing to enter an area
or approaching it to supply a password or watchword, and would only allow a person or group to pass
if they knew the password. In modern times, user names and passwords are commonly used by people
during a log in process that controls access to protected computer operating systems, mobile phones,
cable TV decoders, automated teller machines (ATMs), etc. A typical computer user has passwords
for many purposes: logging into accounts, retrieving e-mail, accessing applications, databases,
networks, web sites, and even reading the morning newspaper online. This lesson outlines understand
what is meant by ―Password‖, how to choose a secure and memorable password, factors in the security
of a password system, password security architecture and methods of verifying a password over a
network

## Objectives

After completing this lesson, you will be able to do the following:

1. Understand what is meant by ―Password‖
2. Understand how to choose a secure and memorable password
3. Understand factors in the security of a password system
4. Understand password security architecture
5. Understand Methods of verifying a password over a network

## 2.1 What is a Password

A password is a word or string of characters used for user authentication to prove identity or access
approval to gain access to a resource which should be kept secret from those not allowed access.
Despite the name, there is no need for passwords to be actual words; indeed passwords which are not
Page 22 of 118


actual words may be harder to guess, a desirable property. Some passwords are formed from multiple
words and may more accurately be called a passphrase. Passwords are generally short enough to be
easily memorized and typed.
Most organizations specify a password policy that sets requirements for the composition and usage of
passwords, typically dictating minimum length, required categories (e.g. upper and lower case,
numbers, and special characters), prohibited elements (e.g. own name, date of birth, address, telephone
number).

## 2.2 How to Choose a Secure and Memorable Password

The easier a password is for the owner to remember generally means it will be easier for an attacker to
guess. However, passwords which are difficult to remember may also reduce the security of a system
because:
i. Users might need to write down or electronically store the password,

ii. Users will need frequent password resets and

iii. Users are more likely to re-use the same password.

Similarly, the more stringent requirements for password strength, e.g. ―have a mix of uppercase and
lowercase letters and digits‖ or ―change it monthly‖, the greater the degree to which users will subvert
the system. Some people even argue that longer passwords provide more security (e.g., entropy) than
shorter passwords with a wide variety of characters.
Combining two or more unrelated words is another good method, but a single dictionary word is not.
Having a personally designed algorithm for generating obscure passwords is another good method.
However, asking users to remember a password consisting of a ―mix of uppercase and lowercase
characters‖ is similar to asking them to remember a sequence of bits: hard to remember, and Page 23
of 118


only a little bit harder to crack (e.g. only 128 times harder to crack for 7-letter passwords, less if the
user simply capitalises one of the letters).
Similarly typing the password one keyboard row higher is a common trick known to attackers. A
method to memorize a complex password is to remember a sentence like 'This year I go to Italy on
Friday July 6!' and use the first characters as the actual password. In this case 'TyIgtIoFJ6!‘

## 2.3 Factors in the security of a password system

The security of a password-protected system depends on several factors. The overall system must, of
course, be designed for sound security, with protection against computer viruses, man in-the-middle
attacks and the like. Physical security issues are also a concern, from deterring shoulder surfing to more
sophisticated physical threats such as video cameras and keyboard sniffers. Nowadays, it is a common
practice for computer systems to hide passwords as they are typed. The purpose of this measure is to
avoid bystanders reading the password. However, some argue that this practice may lead to mistakes
and stress, encouraging users to choose weak passwords. As an alternative, users should have the
option to show or hide passwords as they type them.
i. Rate at which an attacker can try guessed passwords

The rate at which an attacker can submit guessed password to the system is a key factor in determining
system security. While some systems impose a time-out of several seconds after a small number (e.g.,
three) of failed password entry attempts, many systems store or transmit a cryptographic hash of the
password in a manner that makes the hash value accessible to an attacker. When this is done, and it is
very common, an attacker can work off-line, rapidly testing candidate passwords against the true
password‘s hash value.
ii. Form of stored passwords
Page 24 of 118


Some computer systems store user passwords as plain text, against which to compare user log on
attempts. If an attacker gains access to such an internal password store, all passwords and so all user
accounts will be compromised. If some users employ the same password for accounts on different
systems, those will be compromised as well. More secure systems store each password in a
cryptographically protected form, so access to the actual password will still be difficult for a snooper
who gains internal access to the system, while validation of user access attempts remains possible. The
most secure don't store passwords at all, but a one-way derivation, such as a polynomial, modulus, or
an advanced hash function.


## 2.4 Methods of verifying a password over a network

i. Simple transmission of the password

Passwords are vulnerable to interception (i.e., ―snooping‖) while being transmitted to the
authenticating machine or person. If the password is carried as electrical signals on unsecured physical
wiring between the user access point and the central system controlling the password database, it is
subject to snooping by wiretapping methods. If it is carried as packetized data over the Internet, anyone
able to watch the packets containing the logon information can snoop with a very low probability of
detection.
ii. Transmission through encrypted channels

The risk of interception of passwords sent over the Internet can be reduced by, among other approaches,
using cryptographic protection. The most widely used is the Transport Layer Security (TLS, previously
called SSL) feature built into most current Internet browsers. Most browsers alert the user of a
TLS/SSL protected exchange with a server by displaying a closed lock icon, or some other sign, when
TLS is in use.
iii. Hash-based challenge-response methods
Page 25 of 118


Unfortunately, there is a conflict between stored hashed passwords and hash-based challenge-response
authentication; the latter requires a client to prove to a server that they know what the shared secret
(i.e., password) is, and to do this, the server must be able to obtain the shared secret from its stored
form. On many systems (including Unix-type systems) doing remote authentication, the shared secret
usually becomes the hashed form and has the serious limitation of exposing passwords to offline
guessing attacks.
iv. Zero-knowledge password proofs

Rather than transmitting a password, or transmitting the hash of the password, password-authenticated
key agreement systems can perform a zero-knowledge password proof, which proves knowledge of
the password without exposing it. Moving a step further, augmented systems for password
authenticated key agreement (e.g., AMP, B-SPEKE, PAK-Z, SRP-6) avoid both the conflict and
limitation of hash-based methods.

## 2.5 Procedures for changing passwords

Usually, a system must provide a way to change a password, either because a user believes the current
password has been (or might have been) compromised, or as a precautionary measure. If a new
password is passed to the system in unencrypted form, security can be lost (e.g., via wiretapping) before
the new password can even be installed in the password database. And, of course, if the new password
is given to a compromised employee, little is gained.
Identity management systems are increasingly used to automate issuance of replacements for lost
passwords, a feature called self-service password reset. The user‘s identity is verified by asking
questions and comparing the answers to ones previously stored (i.e., when the account was opened).
Page 26 of 118


Some password reset questions ask for personal information that could be found on social media, such
as mother‘s maiden name. As a result, some security experts recommend either making up one‘s own
questions or giving false answers.

## 2.6 Number of users per password

Sometimes a single password controls access to a device, for example, for a network router, or
password-protected mobile phone. However, in the case of a computer system, a password is usually
stored for each user account, thus making all access traceable (save, of course, in the case of users
sharing passwords). A would-be user on most systems must supply a username as well as a password,
almost always at account set up time, and periodically thereafter. If the user supplies a password
matching the one stored for the supplied username, he or she is permitted further access into the
computer system. This is also the case for a cash machine, except that the 'user name' is typically the
account number stored on the bank customer‘s card, and the PIN is usually quite short (4 to 6 digits).
Allotting separate passwords to each user of a system is preferable to having a single password shared
by legitimate users of the system, certainly from a security viewpoint.

## 2.7 Password security architecture

Common techniques used to improve the security of computer systems protected by a password
include:
i. Not displaying the password on the display screen as it is being entered or obscuring it as it is typed
by using asterisks (*) or bullets (•).
ii. Allowing passwords of adequate length. (Some legacy operating systems, including early versions
of Unix and Windows, limited passwords to an 8 character maximum, reducing security.)
iii. Requiring users to re-enter their password after a period of inactivity (a semi log-off policy).


iv. Enforcing a password policy to increase password strength and security.

v. Requiring periodic password changes.

vi. Assigning randomly chosen passwords.

vii. Requiring minimum password lengths.

viii. Some systems require characters from various character classes in a password for example, ―must
have at least one uppercase and at least one lowercase letter‖. However, all-lowercase passwords are
more secure per keystroke than mixed capitalization passwords.

ix. Providing an alternative to keyboard entry (e.g., spoken passwords, or biometric passwords).

x. Requiring more than one authentication system, such as 2-factor authentication (something a user
has and something the user knows).

xi. Using encrypted tunnels or password-authenticated key agreement to prevent access to transmitted
passwords via network attacks

xii. Limiting the number of allowed failures within a given time period (to prevent repeated password
guessing). After the limit is reached, further attempts will fail (including correct password attempts)
until the beginning of the next time period. However, this is vulnerable to a form of denial of service
attack.

xiii. Introducing a delay between password submission attempts to slow down automated password
guessing programs.

Some of the more stringent policy enforcement measures can pose a risk of alienating users, possibly
decreasing security as a result.

## 2.8 Password cracking/Strength

Attempting to crack passwords by trying as many possibilities as time and money permit is a brute
force attack. A related method, rather more efficient in most cases, is a dictionary attack.


dictionary attack, all words in one or more dictionaries are tested. Lists of common passwords are also
typically tested.
Password strength is the likelihood that a password cannot be guessed or discovered, and varies with
the attack algorithm used. Cryptologists and computer scientists often refer to the strength or 'hardness'
in terms of entropy.
Passwords easily discovered are termed weak or vulnerable; passwords very difficult or impossible to
discover are considered strong. There are several programs available for password attack (or even
auditing and recovery by systems personnel) such as L0phtCrack, John the Ripper, and Cain; some of
which use password design vulnerabilities (as found in the Microsoft LAN Manager system) to
increase efficiency. These programs are sometimes used by system administrators to detect weak
passwords proposed by users.

## Summary

1. Since users‘ authentication is the key to maintaining the confidentiality of information, password is
a secret sequence of strings that can be used to identify different users.
2. With the tenacity of password attackers, a password must not be too weak to be guessed neither
should it be too strong for the human memory to contain.
3. Password can be changed regularly if required and organizations can enact password policy to
improve it strength and security.
4. A password is personal to individual and should not be display or discuss with someone else.

## Post-Test

1. Explain how to choose a secure and memorable password
2. Explain factors in the security of a password system
3. Explain password security architecture


4. Explain methods of verifying a password over a network


5. Explain what is meant by ―Password‖


6. How can password can be used as a form of computer security

## References

Vance, Ashlee (2010- 01 - 10). "If Your Password Is 123456, Just Make It Hack Me". The New York
Times.
Managing Network Security at the Wayback Machine (archived March 2, 2008). Fred Cohen and
Associates. All.net. Retrieved on 2012- 05 - 20.
The Memorability and Security of Passwords. ncl.ac.uk. Retrieved on 2012- 05 - 20.
Florencio et. al (2014) An Administrator's Guide to Internet Password Research. Retrieved on 2015-
03 - 14.
"The Strong Password Dilemma" by Richard E. Smith
Zhang Y. (2010): The security of modern password expiration: an algorithmic framework and
empirical analysis; Proceeding CCS '10 Proceedings of the 17th ACM conference on Computer and
communications security Pages 176- 186


# Lesson Three: Computer Access Control

## Introduction

In computer security, general access control includes authorization, authentication, access approval,
and audit. A more narrow definition of access control would cover only access approval, whereby the
system makes a decision to grant or reject an access request from an already authenticated subject,
based on what the subject is authorized to access. Authentication and access control are often combined
into a single operation, so that access is approved based on successful authentication, or based on an
anonymous access token.
This lesson outlines what is meant by access control, classification of computer access control and
access control models among things.

## 3.1 Access Control

In any access-control model, the entities that can perform actions on the system are called subjects,
and the entities representing resources to which access may need to be controlled are called objects.
Subjects and objects should both be considered as software entities, rather than as human users: any
human users can only have an effect on the system via the software entities that they control.


Although some systems equate subjects with user IDs, so that all processes started by a user by default
have the same authority, this level of control is not fine-grained enough to satisfy the principle of least
privilege, and arguably is responsible for the prevalence of malware in such systems.
In some models, for example the object-capability model, any software entity can potentially act as
both subject and object.
As at last year (2014), access-control models tend to fall into one of two classes: those based on
capabilities and those based on access control lists (ACLs).
i. In a capability-based model, holding an unforgettable reference or capability to an object provides
access to the object (roughly analogous to how possession of one's house key grants one access to one's
house); access is conveyed to another party by transmitting such a capability over a secure channel
ii. In an ACL-based model, a subject's access to an object depends on whether its identity appears on
a list associated with the object (roughly analogous to how a bouncer at a private party would check
an ID to see if a name appears on the guest list); access is conveyed by editing the list. (Different ACL
systems have a variety of different conventions regarding who or what is responsible for editing the
list and how it is edited.

Both capability-based and ACL-based models have mechanisms to allow access rights to be granted
to all members of a group of subjects (often the group is itself modeled as a subject).
Access control systems provide the essential services of authorization, identification and
authentication (I&A), access approval, and accountability where:

1. authorization specifies what a subject can do
2. identification and authentication ensure that only legitimate subjects can log on to a system
3. access approval grants access during operations, by association of users with the resources that
    they are allowed to access, based on the authorization policy
4. accountability identifies what a subject (or all subjects associated with a user) did

## 3.2 Authorization

Authorization involves the act of defining access-rights for subjects. An authorization policy specifies
the operations that subjects are allowed to execute within a system.
Most modern operating systems implement authorization policies as formal sets of permissions that
are variations or extensions of three basic types of access:
i. Read (R): The subject can:

Read file contents, List directory contents
ii. Write (W): The subject can change the contents of a file or directory with the following tasks: Add,
Update, Delete, Rename

iii. Execute (X): If the file is a program, the subject can cause the program to be run. (In Unix-style
systems, the "execute" permission doubles as a "traverse directory" permission when granted for a
directory.)


These rights and permissions are implemented differently in systems based on discretionary access
control (DAC) and mandatory access control (MAC).

## 3.3 Identification and Authentication (I&A)

Identification and Authentication (I&A) is the process of verifying that an identity is bound to the
entity that makes an assertion or claim of identity. The I&A process assumes that there was an initial
validation of the identity, commonly called identity proofing. Various methods of identity proofing are
available, ranging from in-person validation using government issued identification, to anonymous
methods that allow the claimant to remain anonymous, but known to the system if they return.


method used for identity proofing and validation should provide an assurance level commensurate with
the intended use of the identity within the system. Subsequently, the entity asserts an identity together
with an authenticator as a means for validation. The only requirement for the identifier is that it must
be unique within its security domain.
Authenticators are commonly based on at least one of the following four factors:
i. Something you know: such as a password or a personal identification number (PIN). This assumes
that only the owner of the account knows the password or PIN needed to access the account.
ii. Something you have: such as a smart card or security token. This assumes that only the owner of
the account has the necessary smart card or token needed to unlock the account.
iii. Something you are: such as fingerprint, voice, retina, or iris characteristics.
iv. Where you are: for example inside or outside a company firewall, or proximity of login location to
a personal GPS device.

## 3.4 Access Approval

Access approval is the function that actually grants or rejects access during operations. During access
approval, the system compares the formal representation of the authorization policy with the access
request, to determine whether the request shall be granted or rejected. Moreover, the access evaluation
can be done online/on-going.

## 3.5 Access control models

The three most widely recognized models are Discretionary Access Control (DAC), Mandatory Access
Control (MAC), and Role Based Access Control (RBAC).


i. Discretionary access control
Discretionary access control (DAC) is a policy determined by the owner of an object. The owner
decides who is allowed to access the object, and what privileges they have.
Two important concepts in DAC are:
File and data ownership: Every object in the system has an owner. In most DAC systems, each
object's initial owner is the subject that caused it to be created. The access policy for an object is
determined by its owner.
Access rights and permissions: These are the controls that an owner can assign to other subjects
for specific resources.

Access controls may be discretionary in ACL-based or capability-based access control systems. (In
capability-based systems, there is usually no explicit concept of 'owner', but the creator of an object
has a similar degree of control over its access policy.)
ii. Mandatory access control
Mandatory access control refers to allowing access to a resource if and only if rules exist that allow a
given user to access the resource. It is difficult to manage, but its use is usually justified when used to
protect highly sensitive information. Examples include certain government and military information.
Management is often simplified (over what can be required) if the information can be protected using
hierarchical access control, or by implementing sensitivity labels. What makes the method
"mandatory" is the use of either rules or sensitivity labels.
i. Sensitivity labels: In such a system subjects and objects must have labels assigned to them. A
subject's sensitivity label specifies its level of trust. An object's sensitivity label specifies the level of
trust required for access. In order to access a given object, the subject must have a sensitivity level
equal to or higher than the requested object.


ii. Data import and export: Controlling the import of information from other systems and export to
other systems (including printers) is a critical function of these systems, which must ensure that
sensitivity labels are properly maintained and implemented so that sensitive information is
appropriately protected at all times.

Two methods are commonly used for applying mandatory access control:
i. Rule-based (or label-based) access control: This type of control further defines specific conditions
for access to a requested object. A Mandatory Access Control system implements a simple form of
rule-based access control to determine whether access should be granted or denied by matching:

An object's sensitivity label and A subject's sensitivity label
ii. Lattice-based access control: These can be used for complex access control decisions involving
multiple objects and/or subjects. A lattice model is a mathematical structure that defines greatest lower-
bound and least upper-bound values for a pair of elements, such as a subject and an object.

iii. Role-based access control
Role-based access control (RBAC) is an access policy determined by the system, not by the owner.
RBAC is used in commercial applications and also in military systems, where multi-level security
requirements may also exist. RBAC differs from DAC in that DAC allows users to control access to
their resources, while in RBAC, access is controlled at the system level, outside of the user's control.
Although RBAC is non-discretionary, it can be distinguished from MAC primarily in the way
permissions are handled. MAC controls read and write permissions based on a user's clearance level
and additional labels. RBAC controls collections of permissions that may include complex operations


such as an e-commerce transaction, or may be as simple as read or write. A role in RBAC can be
viewed as a set of permissions.
Three primary rules are defined for RBAC:
Role assignment: A subject can execute a transaction only if the subject has selected or been assigned
a suitable role.
Role authorization: A subject's active role must be authorized for the subject. With rule 1 above, this
rule ensures that users can take on only roles for which they are authorized.
Transaction authorization: A subject can execute a transaction only if the transaction is authorized
for the subject's active role. With rules 1 and 2, this rule ensures that users can execute only transactions
for which they are authorized.

## Summary

1. Access control is a security mechanism that grants access approval based on authorization given to
an authenticated subject.
2. It involves two entities of action performing entity (i.e. the subject) and the other that represents
resources to which access may need to be controlled (i.e. the object).
3. To access a given object, the subject must have a sensitivity level equal to or higher than the
requested subject.
4. The access control system provides services such as authorization (which specifies what a subject
can do), identification and authentication (which ensures only legitimate subjects can log on to the
system), access approval (which grants access during operations and accountability (which identifies
what a subject did).
5. Access control also involves Reading, Writing and Executing to implement authorization.
Page 37 of 118


## Post-Test

1. Explain four factors upon which authentication is based
2. Briefly explain access control models
3. Write a short note on access control?
4. Argue for or against: Use of access control is sufficient to safeguard computer system from all forms
of threat

## References

Abdulaziz Almehmadi and Khalil El-Khatib. 2013. Authorized! access denied, unauthorized! access
granted. In Proceedings of the 6th International Conference on Security of Information and Networks
(SIN '13).
Dieter Gollmann. Computer Security, 3rd ed. Wiley Publishing, 2011, p. 387, bottom
[http://www.pcmag.com/encyclopedia_term/0,2542,t=clipping+level&i=39821,00.asp](http://www.pcmag.com/encyclopedia_term/0,2542,t=clipping+level&i=39821,00.asp)
Jin, Xin, Ram Krishnan, and Ravi Sandhu. "A unified attribute-based access control model covering
dac, mac and rbac." Data and Applications Security and Privacy XXVI. Springer Berlin Heidelberg,

2012. 41-55.
Marcon, A.L.; Olivo Santin, A.; Stihler, M.; Bachtold, J., "A UCONabc Resilient Authorization
Evaluation for Cloud Computing," Parallel and Distributed Systems, IEEE Transactions on , vol.25,
no.2, pp.&nbsp457-467, Feb. 2014 doi: 10.1109/TPDS.2013.113, bottom
Unifying identity management and access control. Source: security.com. Retrieved 15 July 2013. Page
38 of 118


# Lesson Four: Encryption (1)

## Introduction

Encryption is the process of encoding messages or information in such a way that only authorized
parties can read it. Encryption does not of itself prevent interception, but denies the message content
to the interceptor. In an encryption scheme, the message or information, referred to as plaintext, is
encrypted using an encryption algorithm, generating cipher text that can only be read if decrypted. This
lesson outlines encryption and its usefulness, the types of encryption (Symmetric and Asymmetric)
and some problems associated with it.

## Objectives

After completing this lesson, you will be able to do the following:

1. Understand what is meant by ―Encryption‖
2. Distinguish between the two types of encryption.

## 4.1 Encryption

For technical reasons, an encryption scheme usually uses a pseudo-random encryption key generated
by an algorithm. It is in principle possible to decrypt the message without possessing the key, but, for
a well-designed encryption scheme, large computational resources and skill are required. An
authorized recipient can easily decrypt the message with the key provided by the originator to
recipients, but not to unauthorised interceptors.
4.1.1 Uses of Encryption
i. It is used by militaries and governments to facilitate secret communication. It is now commonly used
in protecting information within many kinds of civilian systems.


ii. It can be used to protect data "at rest", such as files on computers and storage devices (e.g. USB
flash drives).

iii. It is also used to protect data in transit, for example data being transferred via networks (e.g. the
Internet, e-commerce), mobile telephones, wireless microphones, wireless intercom systems,
Bluetooth devices and bank automatic teller machines.

4.1.2 Types of Encryption

1. Symmetric key encryption: In this scheme, the encryption and decryption keys are the same. Thus
communicating parties must have the same key before they can achieve secret communication.


2. Public key encryption: In this scheme, the encryption key is published for anyone to use and
encrypt messages. However, only the receiving party has access to the decryption key that enables
messages to be read.

Symmetric-key encryption are algorithms for cryptography that use the same cryptographic keys for
both encryption of plaintext and decryption of cipher text. The keys may be identical or there may be
a simple transformation to go between the two keys. The keys, in practice, represent a shared secret
between two or more parties that can be used to maintain a private information link. This requirement
that both parties have access to the secret key is one of the main drawbacks of symmetric key
encryption, in comparison to public-key encryption.

## 4.2 Types of symmetric-key encryption

Symmetric-key encryption can use either stream ciphers or block ciphers.
i. Stream ciphers encrypt the digits (typically bytes) of a message one at a time.


ii. Block ciphers take a number of bits and encrypt them as a single unit, padding the plaintext so that
it is a multiple of the block size. Blocks of 64 bits have been commonly used even though the Advanced
Encryption Standard (AES) algorithm uses 128-bit blocks.

## 4.3 Implementations

Examples of popular symmetric algorithms include:
Twofish, Serpent, AES (Rijndael), Blowfish, CAST5, RC4, 3DES, Skipjack, Safer+/++ (Bluetooth),
and IDEA.

## 4.4 Cryptographic primitives based on symmetric ciphers

Symmetric ciphers are commonly used to achieve other cryptographic primitives than just encryption.
Encrypting a message does not guarantee that this message is not changed while encrypted. Hence
often a message authentication code is added to a cipher text to ensure that changes to the cipher text
will be noted by the receiver. Message authentication codes can be constructed from symmetric ciphers
(e.g. CBC-MAC). However, symmetric ciphers cannot be used for non-repudiation purposes except
by involving additional parties. Another application is to build hash functions from block ciphers.

## 4.5 Security of symmetric ciphers

Symmetric ciphers have historically been susceptible to known-plaintext attacks, chosen plaintext
attacks, differential cryptanalysis and linear cryptanalysis. Careful construction of the functions for
each round can greatly reduce the chances of a successful attack.
4.5.1 Key generation
When used with asymmetric ciphers for key transfer, pseudo-random key generators are nearly always
used to generate the symmetric cipher session keys. However, lack of randomness in those generators
Page 41 of 118


or in their initialization vectors is disastrous and has led to cryptanalytic breaks in the past. Therefore,
it is essential that an implementation uses a source of high entropy for its initialization.
4.5.2 Asymmetric-Key Encryption (Public-Key Encryption)
Asymmetric-Key Encryption, also known as Public-Key Encryption, is a class of encryption
algorithms which requires two separate keys, one of which is secret (or private) and one of which is
public. Although different, the two parts of this key pair are mathematically linked. The public key is
used to encrypt plain text or to verify a digital signature; whereas the private key is used to decrypt
cipher text or to create a digital signature. The term "asymmetric" stems from the use of different keys
to perform these opposite functions, each the inverse of the other – as contrasted with conventional
("symmetric") encryption which relies on the same key to perform both.
Public-key algorithms are based on mathematical problems which currently admit no efficient solution
that are inherent in certain integer factorization, discrete logarithm, and elliptic curve relationships. It
is computationally easy for a user to generate their own public and private key-pair and to use them
for encryption and decryption. The strength lies in the fact that it is "impossible" (computationally
infeasible) for a properly generated private key to be determined from its corresponding public key.
Thus the public key may be published without compromising security, whereas the private key must
not be revealed to anyone not authorized to read messages or perform digital signatures. Public key
algorithms, unlike symmetric key algorithms, do not require a secure initial exchange of one (or more)
secret keys between the parties.
An analogy to public-key encryption is that of a locked mail box with a mail slot. The mail slot is
exposed and accessible to the public – its location (the street address) is, in essence, the public key.
Anyone knowing the street address can go to the door and drop a written message through the slot.
However, only the person who possesses the key can open the mailbox and read the message.


## 4.6 Problems

A central problem with the use of public-key cryptography is confidence/proof that a particular public
key is authentic, in that it is correct and belongs to the person or entity claimed, and has not been
tampered with or replaced by a malicious third party. The usual approach to this problem is to use a
public-key infrastructure (PKI), in which one or more third parties – known as certificate authorities –
certify ownership of key pairs. PGP, in addition to being a certificate authority structure, has used a
scheme generally called the "web of trust", which decentralizes such authentication of public keys by
a central mechanism, and substitutes individual endorsements of the link between user and public key.
To date, no fully satisfactory solution to the "public key authentication problem" has been found.

## Summary

1. In order to prevent unauthorized parties from accessing information, encryption is a process of
encoding messages.
2. A public or Symmetric key is used to encrypt information. Although, encryption itself does not
prevent interception, it is capable of denying the message content from been intercepted but adding an
authentication code to the cipher text.
3. Key confidentiality among users is a major challenge for data encryption. This can be tackle if
required considerations for public keys are well implemented.

## Post-Test

1. Briefly explain how encryption could be used as computer security measure?
2. Differentiate between Symmetric and Asymmetric Encryption
3. Briefly explain how encryption could be used as computer security measure?
4. Differentiate between Symmetric and Asymmetric Encryption
Page 43 of 118


## References

Becket, B (1988). Introduction to Cryptology. Blackwell Scientific Publications. ISBN 0- 632 - 01836 -

4. OCLC 16832704. Excellent coverage of many classical ciphers and cryptography concepts and of
the "modern" DES and RSA systems.
Christof Paar, Jan Pelzl, Understanding Cryptography, A Textbook for Students and Practitioners.
Springer, 2009. (Slides, online cryptography lectures and other information are available on the
companion web site.) Very accessible introduction to practical cryptography for non-mathematicians.
Introduction to Modern Cryptography by Phillip Rogaway and Mihir Bellare, a mathematical
introduction to theoretical cryptography including reduction-based security proofs. PDF download.
Johann-Christoph Woltag, 'Coded Communications (Encryption)' in Rüdiger Wolfrum (ed) Max
Planck Encyclopedia of Public International Law (Oxford University Press 2009). *"Max Planck
Encyclopedia of Public International Law"., giving an overview of international law issues regarding
cryptography.
Stallings, William (March 2013). Cryptography and Network Security: Principles and Practice (6th
ed.). Prentice Hall. ISBN 978-0133354690. Page 44 of 118


# Lesson Five: Encryption (2)

## Introduction

We started discussing encryption in our last lesson and we defined it as the process of encoding
messages or information in such a way that only authorized parties can read it. In this lesson, we study
some security issues with encryption and look into their advantages and disadvantages among other
things.

## Objectives

After completing this lesson, you will be able to do the following:

1. Understand the advantages and disadvantages of the two types of encryption.
2. Enumerate popular implementation of each type of encryption algorithms

## 5.1 Security

Some encryption schemes can be proven secure on the basis of the presumed difficulty of a
mathematical problem, such as factoring the product of two large primes or computing discrete
logarithms. Note that "secure" here has a precise mathematical meaning, and there are multiple
different (meaningful) definitions of what it means for an encryption scheme to be "secure". The "right"
definition depends on the context in which the scheme will be deployed.
The most obvious application of a public key encryption system is confidentiality – a message that a
sender encrypts using the recipient's public key can be decrypted only by the recipient's paired private
key. This assumes, of course, that no flaw is discovered in the basic algorithm used. Page 45 of 118


## 5.2 Practical Consideration: A postal analogy

An analogy that can be used to understand the advantages of an asymmetric system is to imagine two
people, Alice and Bob, who are sending a secret message through the public mail. In this example,
Alice wants to send a secret message to Bob, and expects a secret reply from Bob.
With a symmetric key system, Alice first puts the secret message in a box, and locks the box using a
padlock to which she has a key. She then sends the box to Bob through regular mail. When Bob receives
the box, he uses an identical copy of Alice's key (which he has somehow obtained previously, maybe
by a face-to-face meeting) to open the box, and reads the message. Bob can then use the same padlock
to send his secret reply.
In an asymmetric key system, Bob and Alice have separate padlocks. First, Alice asks Bob to send his
open padlock to her through regular mail, keeping his key to himself. When Alice receives it she uses
it to lock a box containing her message, and sends the locked box to Bob. Bob can then unlock the box
with his key and read the message from Alice. To reply, Bob must similarly get Alice's open padlock
to lock the box before sending it back to her.
The critical advantage in an asymmetric key system is that Bob and Alice never need to send a copy
of their keys to each other. This prevents a third party – perhaps, in this example, a corrupt postal
worker that will open unlocked boxes – from copying a key while it is in transit, allowing the third
party to spy on all future messages sent between Alice and Bob.
So, in the public key scenario, Alice and Bob need not trust the postal service as much. In addition, if
Bob were careless and allowed someone else to copy his key, Alice's messages to Bob would be
compromised, but Alice's messages to other people would remain secret, since the other people would
be providing different padlocks for Alice to use. Page 46 of 118


Another kind of asymmetric key system, called a three-pass protocol, requires neither party to even
touch the other party's padlock (or key); Bob and Alice have separate padlocks. First, Alice puts the
secret message in a box, and locks the box using a padlock to which only she has a key. She then sends
the box to Bob through regular mail. When Bob receives the box, he adds his own padlock to the box,
and sends it back to Alice. When Alice receives the box with the two padlocks, she removes her padlock
and sends it back to Bob. When Bob receives the box with only his padlock on it, Bob can then unlock
the box with his key and read the message from Alice. Note that, in this scheme, the order of decryption
is NOT the same as the order of encryption – this is only possible if commutative ciphers are used. A
commutative cipher is one in which the order of encryption and decryption is interchangeable, just as
the order of multiplication is interchangeable (i.e., A*B*C = A*C*B = C*B*A). This method is secure for
certain choices of commutative ciphers, but insecure for others (e.g., a simple XOR). For example, let
E 1 () and E 2 () be two encryption functions, and let "M" be the message so that if Alice encrypts it using
E 1 () and sends E 1 (M) to Bob. Bob then again encrypts the message as E 2 (E 1 (M)) and sends it to Alice.
Now, Alice decrypts E 2 (E 1 (M)) using E 1 (). Alice will now get E 2 (M), meaning when she sends this again
to Bob, he will be able to decrypt the message using E 2 () and get "M". Although none of the keys were
ever exchanged, the message "M" may well be a key (e.g., Alice's Public key). This three-pass protocol
is typically used during key exchange.

## 5.3 Actual algorithms: two linked keys

Not all asymmetric key algorithms operate in precisely this fashion. The most common ones have the
property that Alice and Bob each own two keys, one for encryption and one for decryption. In a secure
asymmetric key encryption scheme, the private key should not be deducible from the public key. This
is known as public-key encryption, since an encryption key can be published without compromising
the security of messages encrypted with that key. Page 47 of 118


In the analogy above, Bob might publish instructions on how to make a lock ("public key"). However,
the workings of the lock are such that it is impossible (so far as is known) to deduce from the
instructions given just exactly how to make a key that will open that lock (e.g., a "private key"). Those
wishing to send messages to Bob must use the public key to encrypt the message, and then Bob can
use his private key to decrypt it.
Another example has Alice and Bob each choosing a key at random, and then contacting each other to
compare the depth of each notch on their keys. Having determined the difference, a locked box is built
with a special lock that has each pin inside divided into 2 pins, matching the numbers of their keys.
Now the box will be able to be opened with either key and Alice and Bob can exchange messages
inside the box in a secure fashion.

## 5.4 Disadvantages

There is a possibility that someone could "pick" Bob's or Alice's lock. Among symmetric key
encryption algorithms, only the one-time pad can be proven to be secure against any adversary – no
matter how much computing power is available. However, there is no public-key scheme with this
property, since all public-key schemes are susceptible to a "brute-force key search attack". Such attacks
are impractical if the amount of computation needed to succeed – termed the "work factor" by Claude
Shannon – is out of reach of all potential attackers. In many cases, the work factor can be increased by
simply choosing a longer key. But other algorithms may have much lower work factors, making
resistance to a brute-force attack irrelevant. Some special and specific algorithms have been developed
to aid in attacking some public key encryption algorithms – both RSA and ElGamal encryption have
known attacks that are much faster than the brute-force approach. These factors have changed
dramatically in recent decades, both with the decreasing cost of computing power and with new
mathematical discoveries.


Aside from the resistance to attack of a particular key pair, the security of the certification hierarchy
must be considered when deploying public key systems. Some certificate authority – usually a purpose-
built program running on a server computer – vouches for the identities assigned to specific private
keys by producing a digital certificate. Public key digital certificates are typically valid for several
years at a time, so the associated private keys must be held securely over that time. When a private key
used for certificate creation higher in the PKI server hierarchy is compromised, or accidentally
disclosed, and then a "man-in-the-middle attack" is possible, making any subordinate certificate wholly
insecure.
Major weaknesses have been found for several formerly promising asymmetric key algorithms. The
'knapsack packing' algorithm was found to be insecure after the development of a new attack. Recently,
some attacks based on careful measurements of the exact amount of time it takes known hardware to
encrypt plain text have been used to simplify the search for likely decryption keys (see "side channel
attack"). Thus, mere use of asymmetric key algorithms does not ensure security. A great deal of active
research is currently underway to both discover, and to protect against, new attack algorithms.
Another potential security vulnerability in using asymmetric keys is the possibility of a "man-in-the-
middle" attack, in which the communication of public keys is intercepted by a third party (the "man in
the middle") and then modified to provide different public keys instead. Encrypted messages and
responses must also be intercepted, decrypted, and re-encrypted by the attacker using the correct public
keys for different communication segments, in all instances, so as to avoid suspicion. This attack may
seem to be difficult to implement in practice, but it is not impossible when using insecure media (e.g.,
public networks, such as the Internet or wireless forms of communications) – for example, a malicious
staff member at Alice or Bob's Internet Service Provider (ISP) might find it quite easy to Page 49 of
118


carry out. In the earlier postal analogy, Alice would have to have a way to make sure that the lock on
the returned packet really belongs to Bob before she removes her lock and sends the packet back.
Otherwise, the lock could have been put on the packet by a corrupt postal worker pretending to be Bob,
so as to fool Alice.
5.4.1 Possible Solution
One approach to prevent such attacks involves the use of a certificate authority, a trusted third party
responsible for verifying the identity of a user of the system. This authority issues a tamper-resistant,
non-spoofable digital certificate for the participants. Such certificates are signed data blocks stating
that this public key belongs to that person, company, or other entity.
This approach also has its weaknesses – for example, the certificate authority issuing the certificate
must be trusted to have properly checked the identity of the key-holder, must ensure the correctness of
the public key when it issues a certificate, and must have made arrangements with all participants to
check all their certificates before protected communications can begin. Web browsers, for instance, are
supplied with a long list of "self-signed identity certificates" from PKI providers – these are used to
check the bona fides of the certificate authority and then, in a second step, the certificates of potential
communicators. An attacker who could subvert any single one of those certificate authorities into
issuing a certificate for a bogus public key could then mount a "man-in-the-middle" attack as easily as
if the certificate scheme were not used at all. Despite its theoretical and potential problems, this
approach is widely used. Examples include SSL and its successor, TLS, which are commonly used to
provide security for web browsers, for example, so that they might be used to securely send credit card
details to an online store.


5.5.2 Computational cost
The public key algorithms known thus far are relatively computationally costly compared with most
symmetric key algorithms of apparently equivalent security. The difference factor is the use of typically
quite large keys. This has important implications for their practical use. Most are used in hybrid
cryptosystems for reasons of efficiency – in such a cryptosystem, a shared secret key ("session key")
is generated by one party, and this much briefer session key is then encrypted by each recipient's public
key. Each recipient then uses the corresponding private key to decrypt the session key. Once all parties
have obtained the session key, they can use a much faster symmetric algorithm to encrypt and decrypt
messages. In many of these schemes, the session key is unique to each message exchange, being
pseudo-randomly chosen for each message.

## 5.5 Considerations for using public-key encryption

i. Privilege of key revocation
A malicious (or erroneous) revocation of some (or all) of the keys in the system is likely, or in the
second case, certain, to cause a complete failure of the system. If public keys can be revoked
individually, this is a possibility. However, there are design approaches that can reduce the practical
chance of this occurring. For example, by means of certificates, we can create what is called a
"compound principal" – one such principal could be "Alice and Bob have Revoke Authority".
ii. Distribution of a new key

After a key has been revoked, or when a new user is added to a system, a new key must be distributed
in some predetermined manner. Assume that Carol's key has been revoked (e.g., by exceeding its
expiration date, or because of a compromise of Carol's matching private key). Until a new key has been
distributed, Carol is effectively "out of contact". No one will be able to send her messages.


without violating system protocols (i.e., without a valid public key, no one can encrypt messages to
her), and messages from her cannot be signed, for the same reason.
iii. Spreading the revocation
Notification of a key certificate revocation must be spread to all those who might potentially hold it,
and as rapidly as possible.
There are but two means of spreading information (i.e., a key revocation) in a distributed system: either
the information is "pushed" to users from a central point (or points), or else it is "pulled" from a central
point (or points) by the end users.
Pushing the information is the simplest solution, in that a message is sent to all participants. However,
there is no way of knowing whether all participants will actually receive the message. If the number of
participants is large, and some of their physical or network distances are great, then the probability of
complete success (which is, in ideal circumstances, required for system security) will be rather low. In
a partly updated state, the system is particularly vulnerable to "denial of service" attacks as security
has been breached, and a vulnerability window will continue to exist as long as some users have not
"gotten the word". Put another way, pushing certificate revocation messages is neither easy to secure,
nor very reliable.
The alternative to pushing is pulling. In the extreme, all certificates contain all the keys needed to
verify that the public key of interest (i.e., the one belonging to the user to whom one wishes to send a
message, or whose signature is to be checked) is still valid. In this case, at least some use of the system
will be blocked if a user cannot reach the verification service (i.e., one of the systems that can establish
the current validity of another user's key). Again, such a system design can be made as reliable as one
wishes, at the cost of lowering security – the more servers to check for the possibility of a key
revocation, the longer the window of vulnerability. Page 52 of 118


iv. Recovery from a leaked key
Assume that the principal authorized to revoke a key has decided that a certain key must be revoked.
In most cases, this happens after the fact – for instance, it becomes known that at some time in the past
an event occurred that endangered a private key. Let us denote the time at which it is decided that the
compromise occurred as T.
Such a compromise has two implications. First, messages encrypted with the matching public key (now
or in the past) can no longer be assumed to be secret. One solution to avoid this problem is to use a
protocol that has perfect forward secrecy. Second, signatures made with the no longer trusted to be
actually private key after time T can no longer be assumed to be authentic without additional
information (i.e., who, where, when, etc.) about the events leading up to the digital signature. These
will not always be available, and so all such digital signatures will be less than credible. A solution to
reduce the impact of leaking a private key of a signature scheme is to use timestamps.

## Examples of well-regarded asymmetric key techniques for varied purposes include:

i. Diffie–Hellman key exchange protocol

ii. DSS (Digital Signature Standard), which incorporates the Digital Signature Algorithm

iii. ElGamal

iv. Paillier cryptosystem

v. RSA encryption algorithm (PKCS#1)

vi. Cramer–Shoup cryptosystem

vii. YAK authenticated key agreement protocol

## Summary

In this lesson, you have learnt that Page 53 of 118


1. In order to prevent unauthorized parties from accessing information, encryption is a process of
encoding messages.
2. Symmetric and asymmetric key encryption techniques have their merits and demerits.
3. Most existing public-key encryption techniques are computationally costly
4. To use public-key encryption, some considerations should be made which include the privilege of
key revocation, spreading a revocation and recovering from a leaked key.

## Post-Test

1. Briefly explain issues to consider before using public-key encryption
2. Mention some disadvantages of encryption
3. What do you think could be responsible for the computational cost of most public-key encryption
techniques?
4. Briefly explain how encryption could be used as computer security measure?
5. Differentiate between Symmetric and Asymmetric Encryption

## References

Becket, B (1988). Introduction to Cryptology. Blackwell Scientific Publications. ISBN 0- 632 - 01836 -

4. OCLC 16832704. Excellent coverage of many classical ciphers and cryptography concepts and of
the "modern" DES and RSA systems.
Christof Paar, Jan Pelzl, Understanding Cryptography, A Textbook for Students and Practitioners.
Springer, 2009. (Slides, online cryptography lectures and other information are available on the
companion web site.) Very accessible introduction to practical cryptography for non-mathematicians.
Introduction to Modern Cryptography by Phillip Rogaway and Mihir Bellare, a mathematical
introduction to theoretical cryptography including reduction-based security proofs. PDF download.
Page 54 of 118


Johann-Christoph Woltag, 'Coded Communications (Encryption)' in Rüdiger Wolfrum (ed) Max
Planck Encyclopedia of Public International Law (Oxford University Press 2009). *"Max Planck
Encyclopedia of Public International Law"., giving an overview of international law issues regarding
cryptography.
Stallings, William (March 2013). Cryptography and Network Security: Principles and Practice (6th
ed.). Prentice Hall. ISBN 978-0133354690. Page 55 of 118


# Lesson Six: Confidentiality, Integrity and Availability (CIA)

## Introduction

This does not refer to clandestine operating involving the Central Intelligence Agency; rather it is a
reference to the three pillars of security: confidentiality, integrity, and availability. When you are
thinking about security, your thought processes should always be guided by these three principles. First
and foremost, are you keeping the data confidential? Does your approach help guarantee the integrity
of data? And does your approach still make the data readily available to authorized users?
This lesson outlines the widely used benchmark for evaluation of information systems security;
however we will be focusing on the three core goals of confidentiality, integrity and availability of
information.

## Objectives

After completing this lesson, you will be able to do the following:

1. Understand what is meant by ―confidentiality, integrity and availability of information‖
2. Understand the relationship among these core goals as related to computer system security?
3. Understand the concept of prevention and detection computer security.

## 6.1 The CIA Criteria

You may have heard information security specialists referring to the "CIA" but they're usually not
talking about the Central Intelligence Agency or the Culinary Institute of America.
CIA is a widely used benchmark for evaluation of information systems security, focusing on the three
core goals of confidentiality, integrity and availability of information. Page 56 of 118


Each time an information technology team installs a software application or computer server, analyzes
any data transport method, creates a database, or provides access to information or data sets, CIA
criteria must be addressed.

1. Confidentiality: It refers to limiting information access and disclosure to authorized users (the right
people) and preventing access by or disclosure to unauthorized ones (the wrong people).
Authentication methods like user-IDs and passwords, that uniquely identify data systems' users and
control access to data systems' resources, underpin the goal of confidentiality. It is related to the broader
concept of data privacy i.e. limiting access to individuals' personal information.
2. Integrity: Integrity refers to the trustworthiness of information resources. It includes the concept of
"data integrity" namely, that data have not been changed inappropriately, whether by accident or
deliberately malign activity. It also includes "origin" or "source integrity" that is, that the data actually
came from the person or entity you think it did, rather than an imposter. It can even include the notion
that the person or entity in question entered the right information -- that is, that the information reflected
the actual circumstances (in statistics, this is the concept of "validity") and that under the same
circumstances would generate identical data (what statisticians call "reliability"). On a more restrictive
view, however, integrity of an information system includes only preservation without corruption of
whatever was transmitted or entered into the system, right or wrong.

In information security, data integrity means maintaining and assuring the accuracy and consistency
of data over its entire life-cycle. This means that data cannot be modified in an unauthorized or
undetected manner. This is not the same thing as referential integrity in databases, although it can be
viewed as a special case of consistency as understood in the Page 57 of 118


classic ACID model of transaction processing. Information security systems typically provide message
integrity in addition to data confidentiality.

3. Availability: Availability refers, unsurprisingly, to the availability of information resources. For
any information system to serve its purpose, the information must be available when it is needed. This
means that the computing systems used to store and process the information, the security controls used
to protect it, and the communication channels used to access it must be functioning correctly. High
availability systems aim to remain available at all times, preventing service disruptions due to power
outages, hardware failures, and system upgrades. Ensuring availability also involves preventing denial-
of-service attacks, such as a flood of incoming messages to the target system essentially forcing it to
shut down.

An information system that is not available when you need it is almost as bad as none at all. It may be
much worse, depending on how reliant the organization has become on a functioning computer and
communications infrastructure. Availability, like other aspects of security, may be affected by purely
technical issues (e.g., a malfunctioning part of a computer or communications device), natural
phenomena (e.g., wind or water), or human causes (accidental or deliberate).
For any information system to serve its purpose, the information must be available when it is needed.
This means that the computing systems used to store and process the information, the security controls
used to protect it, and the communication channels used to access it must be functioning correctly.
High availability systems aim to remain available at all times, preventing service disruptions due to
power outages, hardware failures, and system upgrades. Ensuring availability also involves preventing
denial-of-service attacks, such as a flood of incoming messages to the target system essentially forcing
it to shut down. Page 58 of 118


While the relative risks associated with these categories depend on the particular context, the general
rule is that humans are the weakest link. (Again, that's why your ability and willingness to use our data
systems securely is critical.)

## 6.2 Prevention vs. detection

Security efforts to assure confidentiality, integrity and availability can be divided into those oriented
to prevention and those focused on detection. The latter aims to rapidly discover and correct for lapses
that could not be or at least were not prevented.
The balance between prevention and detection depends on the circumstances, and the available security
technologies. For example, many homes have easily defeated door and window locks, but rely on a
burglar alarm to detect (and signal for help after) intrusions through a compromised window or door.
Our information systems use a range of intrusion prevention methods, of which user-IDs and
passwords are only one part. We also employ detection methods like audit trails to pick up suspicious
activity that may signal an intrusion.

## 6.3 Security in context

It is critical to remember that "appropriate" or "adequate" levels of confidentiality, integrity and
availability depend on the context, just as does the appropriate balance between prevention and
detection. The nature of the efforts that the information systems support; the natural, technical and
human risks to those endeavours; governing legal, professional and customary standards all of these
will condition how CIA standards are set in a particular situation. Page 59 of 118


## Summary

In this lesson, we have learnt that

1. The availability of information to users is as important as the confidentiality and integrity of such
information.
2. Just as data integrity means maintaining and assuring the accuracy and consistency of data over its
entire life-cycle, confidentiality ensures that the information is disclosed to the right set of authorized
users.
3. Prevention and detection are the dual approach for ensuring the confidentiality, Integrity and
Availability of data to authorized users.
4. While detection aims to rapidly discover and correct for lapses that could not be or at least were not
prevented, a balance between the two approach depend on the circumstances, and the available security
technologies

## Post-Test

1. Explain what is meant by ―confidentiality, integrity and availability of information‖
2. How do you think they are related to computer system security?
3. Discuss the concept of prevention and detection with respect to these three core goals
(confidentiality, integrity and availability of information).
4. Explain what is meant by ―confidentiality, integrity and availability of information‖
5. How do you think they are related to computer system security?

## References

Anderson, J. M. (2003). "Why we need a new definition of information security". Computers &
Security, 22(4), 308–313. doi:10.1016/S0167-4048(03)00407-3. Page 60 of 118


B., McDermott, E., & Geer, D. (2001). Information security is information risk management. In
Proceedings of the 2001 Workshop on New Security Paradigms NSPW ̳01, (pp. 97 – 104). ACM.
doi:10.1145/508171.508187
Cherdantseva Y. and Hilton J.: "Information Security and Information Assurance. The Discussion
about the Meaning, Scope and Goals". In: Organizational, Legal, and Technological Dimensions of
Information System Administrator. Almeida F., Portela, I. (eds.). IGI Global Publishing. (2013)
https://www.isc2.org/uploadedFiles/(ISC)2_Public_Content/2013%20Global%20Information%20Se
curity%20Workforce%20Study%20Feb%202013.pdf
Perrin, Chad. "The CIA Triad". Retrieved 31 May 2012.
Pipkin, D. (2000). Information security: Protecting the global enterprise. New York: Hewlett-Packard
Company.
Venter, H. S., & Eloff, J. H. P. (2003). "A taxonomy for information security technologies". Computers
& Security, 22(4), 299–307. doi:10.1016/S0167-4048(03)00406-1. Page 61 of 118


# Lesson Seven: Authorization and Authentication (Computer Access Control)

## Introduction

Authorization to access information and other computing services begins with administrative policies
and procedures. The policies prescribe what information and computing services can be accessed, by
whom, and under what conditions. The access control mechanisms are then configured to enforce these
policies. Different computing systems are equipped with different kinds of access control mechanisms;
some may even offer a choice of different access control mechanisms. Authentication, in contrast with
identification which refers to the act of stating or otherwise indicating a claim purportedly attesting to
a person or thing's identity, is the act of confirming the truth of an attribute of a single piece of data
(datum) or entity. Authentication is the process of actually confirming that identity. This lesson outlines
how authorization and authentication can be used in enhancing computer security.

## Objectives

After completing this lesson, you will be able to do the following:

1. Understand what authorization / authentication mean with respect to Computer Security.
2. The role authorization plays in the overall computer security.
3. Understand the three (3) types of authentication
4. Understand factors of authentication

## 7.1 Authorization

It is the function of specifying access rights to resources related to information security and computer
security in general and to access control in particular. More formally, "to authorize" is to define an
access policy. For example, human resources staff is normally authorized to access employee records


and this policy is usually formalized as access control rules in a computer system. During operation,
the system uses the access control rules to decide whether access requests from (authenticated)
consumers shall be approved (granted) or disapproved (rejected). Resources include individual files or
an item's data, computer programs, computer devices and functionality provided by computer
applications. Examples of consumers are computer users, computer programs and other devices on the
computer.
Access control in computer systems and networks rely on access policies. The access control process
can be divided into the following two phases:
i. Policy definition phase where access is authorized, and

ii. Policy enforcement phase where access requests are approved or disapproved.

Authorization is thus the function of the policy definition phase which precedes the policy enforcement
phase where access requests are approved or disapproved based on the previously defined
authorizations.
Most modern, multi-user operating systems include access control and thereby rely on authorization.
Access control also uses authentication to verify the identity of consumers. When a consumer tries to
access a resource, the access control process checks that the consumer has been authorized to use that
resource. Authorization is the responsibility of an authority, such as a department manager, within the
application domain, but is often delegated to a custodian such as a system administrator. Authorizations
are expressed as access policies in some types of "policy definition application", e.g. in the form of an
access control list or a capability, on the basis of the "principle of least privilege": consumers should
only be authorized to access whatever they need to do their jobs. Older and single user operating
systems often had weak or non-existent authentication and access control systems.


"Anonymous consumers" or "guests‖ are consumers that have not been required to authenticate. They
often have limited authorization. On a distributed system, it is often desirable to grant access without
requiring a unique identity. Familiar examples of access tokens include keys and tickets: they grant
access without proving identity.
Trusted consumers are often authorized for unrestricted access to resources on a system, but must be
authenticated so that the access control system can make the access approval decision. "Partially
trusted" and guests will often have restricted authorization in order to protect resources against
improper access and usage. The access policy in some operating systems, by default, grants all
consumers full access to all resources. Others do the opposite, insisting that the administrator explicitly
authorizes a consumer to use each resource.
Even when access is controlled through a combination of authentication and access control lists, the
problems of maintaining the authorization data is not trivial, and often represents as much
administrative burden as managing authentication credentials. It is often necessary to change or remove
a user's authorization: this is done by changing or deleting the corresponding access rules on the
system. Using atomic authorization is an alternative to per-system authorization management, where a
trusted third party securely distributes authorization information.

## 7.2 Authentication

It is the act of confirming the truth of an attribute of a single piece of data (datum) or entity. In contrast
with identification which refers to the act of stating or otherwise indicating a claim purportedly
attesting to a person or thing's identity, authentication is the process of actually confirming that identity.
It might involve confirming the identity of a person by validating their identity documents, verifying
the validity of a Website with a digital certificate, tracing the age of an artefact by carbon


dating, or ensuring that a product is what its packaging and labelling claim to be. In other words,
authentication often involves verifying the validity of at least one form of identification.

## 7.3 Types of Authentication

In computer science, verifying a person's identity is often required to secure access to confidential data
or systems. Authentication can be considered to be of three types:
The first type of authentication is accepting proof of identity given by a credible person who has first-
hand evidence that the identity is genuine. When authentication is required of art or physical objects,
this proof could be a friend, family member or colleague attesting to the item's provenance, perhaps by
having witnessed the item in its creator's possession. With autographed sports memorabilia, this could
involve someone attesting that they witnessed the object being signed. A vendor selling branded items
implies authenticity, while he or she may not have evidence that every step in the supply chain was
authenticated. This hear-say authentication has no use case example in the context of computer
security.
The second type of authentication is comparing the attributes of the object itself to what is known
about objects of that origin. For example, an art expert might look for similarities in the style of
painting, check the location and form of a signature, or compare the object to an old photograph. An
archaeologist might use carbon dating to verify the age of an artefact, do a chemical analysis of the
materials used, or compare the style of construction or decoration to other artefacts of similar origin.
The physics of sound and light, and comparison with a known physical environment, can be used to
examine the authenticity of audio recordings, photographs, or videos. Documents can be verified as
being created on ink or paper readily available at the time of the item's implied creation.
Attribute comparison may be vulnerable to forgery. In general, it relies on the facts that creating a
forgery indistinguishable from a genuine artefact requires expert knowledge, that mistakes are easily
Page 65 of 118


made, and that the amount of effort required to do so is considerably greater than the amount of profit
that can be gained from the forgery.
Criminal and civil penalties for fraud, forgery, and counterfeiting can reduce the incentive for
falsification, depending on the risk of getting caught.
Currency and other financial instruments commonly use this second type of authentication method.
Bills, coins, and cheques incorporate hard-to-duplicate physical features, such as fine printing or
engraving, distinctive feel, watermarks, and holographic imagery, which are easy for trained receivers
to verify.
The third type of authentication relies on documentation or other external affirmations. In criminal
courts, the rules of evidence often require establishing the chain of custody of evidence presented. This
can be accomplished through a written evidence log, or by testimony from the police detectives and
forensics staff that handled it. Some antiques are accompanied by certificates attesting to their
authenticity. Signed sports memorabilia is usually accompanied by a certificate of authenticity. These
external records have their own problems of forgery and perjury, and are also vulnerable to being
separated from the artefact and lost.
In computer science, a user can be given access to secure systems based on user credentials that imply
authenticity. A network administrator can give a user a password, or provide the user with a key card
or other access device to allow system access. In this case, authenticity is implied but not guaranteed.
Consumer goods such as pharmaceuticals, perfume, fashion clothing can use all three forms of
authentication to prevent counterfeit goods from taking advantage of a popular brand's reputation
(damaging the brand owner's sales and reputation). As mentioned above, having an item for sale in a
reputable store implicitly attests to it being genuine, the first type of authentication. The second type
of authentication might involve comparing the quality and craftsmanship of an item, such as an
expensive


handbag, to genuine articles. The third type of authentication could be the presence of a trademark on
the item, which is a legally protected marking, or any other identifying feature which aids consumers
in the identification of genuine brand-name goods. With software, companies have taken great steps to
protect from counterfeiters, including adding holograms, security rings, security threads and colour
shifting ink.

## 7.4 Factors of authentication

The ways in which someone may be authenticated fall into three categories, based on what are known
as the factors of authentication:
i. Something the user knows,
ii. Something the user has, and
iii. Something the user is.

Each authentication factor covers a range of elements used to authenticate or verify a person's identity
prior to being granted access, approving a transaction request, signing a document or other work
product, granting authority to others, and establishing a chain of authority.
Security research has determined that for a positive authentication, elements from at least two, and
preferably all three, factors should be verified.
The three factors (classes) and some of elements of each factor are:
i. the knowledge factors: Something the user knows (e.g., a password, pass phrase, or personal
identification number (PIN), challenge response (the user must answer a question, or pattern)

ii. the ownership factors: Something the user has (e.g., wrist band, ID card, security token, cell phone
with built-in hardware token, software token, or cell phone holding a software token)
Page 67 of 118


iii. the inherence factors: Something the user is or does (e.g., fingerprint, retinal pattern, DNA
sequence (there are assorted definitions of what is sufficient), signature, face, voice, unique bio-electric
signals, or other biometric identifier).

## Summary

In this lesson, you have learnt that

1. Authentication and authorization are very useful for protecting resources against improper access
and usage.
2. The mechanisms that are configured to enforce administrative policies and procedures which
prescribe what information or computing service can be accessed, by whom and under what conditions
is referred to as access control.
3. Just as authentication is used to verify the identity of a consumer, authorization is the responsibility
of an authority within the application domain. Both forms of access control mechanisms can be useful
in enhancing computer security.

## Post-Test

1. Write a short note on authorization and authentication as related to computer security?
2. Argue for or against: Use of authorization/authentication is sufficient to safeguard computer system
from all forms of threat.
3. Write a short note on authorization and authentication as related to computer security?
4. Argue for or against: Use of authorization/ authentication is sufficient to safeguard computer system
from all forms of threat.


## References

A mechanism for identity delegation at authentication level, N Ahmed, C Jensen - Identity and Privacy
in the Internet Age - Springer 2009
Eliasson, C; Matousek (2007). [http://pubs.acs.org/doi/abs/10.1021/ac062223z accessdate=9 Nov
2014 "Noninvasive Authentication of Pharmaceutical Products through Packaging Using Spatially
Offset Raman Spectroscopy"]. Analytical Chemistry 79 (4): 1696–1701.
Federal Financial Institutions Examination Council (2008). "Authentication in an Internet Banking
Environment". Retrieved 2009- 12 - 31.
How Anti-shoplifting Devices Work‖, HowStuffWorks.com
[http://www.cloudave.com/472/authn-authz-and-gluecon/](http://www.cloudave.com/472/authn-authz-and-gluecon/)
[http://www.microsoft.com/en-us/howtotell/Software.aspx](http://www.microsoft.com/en-us/howtotell/Software.aspx)
Li, Ling (March 2013). [http://www.sciencedirect.com/science/article/pii/S0007681312001668
accessdate=9 Nov 2014 "Technology designed to combat fakes in the global supply chain"]. Business
Horizons 56 (2): 167–177.
The Register, UK; Dan Goodin; 30/3/08; Get your German Interior Minister's fingerprint, here.
Compared to other solutions, "It's basically like leaving the password to your computer everywhere
you go, without you being able to control it anymore," one of the hackers comments. Page 69 of 118


# Lesson Eight: Non-Repudiation

## Introduction

Non-repudiation refers to a state of affairs where the purported maker of a statement will not be able
to successfully challenge the validity of the statement or contract. The term is often seen in a legal
setting wherein the authenticity of a signature is being challenged. In such an instance, the authenticity
is being "repudiated". This lesson outlines how the concept of non-repudiation is important in computer
security.

## Objectives

After completing this lesson, you will be able to do the following:

1. Understand concept of non-repudiation.
2. Explain its importance with respect to computer security.

## 8.1 Non-Repudiation

In a general sense, non-repudiation involves associating actions or changes to a unique individual. For
a secure area, for example, it may be desirable to implement a key card access system. Non-repudiation
would be violated if it were not also a strictly enforced policy to prohibit sharing of the key cards and
to immediately report lost or stolen cards. Otherwise determining who performed the action of opening
the door cannot be trivially determined. Similarly, for computer accounts, the individual owner of the
account must not allow others to use that account, especially, for instance, by giving away their
account's password, and a policy should be implemented to enforce this. This prevents the owner of
the account from denying actions performed by the account.
Regarding digital security, the cryptological meaning and application of non-repudiation shifts to
mean:


i. A service that provides proof of the integrity and origin of data.
ii. An authentication that can be asserted to be genuine with high assurance.

Proof of data integrity is typically the easiest of these requirements to accomplish. A data hash, such
as SHA2, is usually sufficient to establish that the likelihood of data being undetectably changed is
extremely low. Even with this safeguard, it is still possible to tamper with data in transit, either through
a man-in-the-middle attack or phishing. Due to this flaw, data integrity is best asserted when the
recipient already possesses the necessary verification information.
The most common method of asserting the digital origin of data is through digital certificates, a form
of public key infrastructure, to which digital signatures belong. Note that the public key scheme is not
used for encryption in this form; confidentiality is not achieved by signing a message with a private
key (since anyone can obtain the public key to reverse the signature). Verifying the digital origin means
that the certified/signed data can be, with reasonable certainty, trusted to be from somebody who
possesses the private key corresponding to the signing certificate. If the key is not properly safeguarded
by the original owner, digital forgery can become a major concern.
The ways in which a party may attempt to repudiate a signature present a challenge to the
trustworthiness of the signatures themselves. The standard approach to mitigating these risks is to
involve a trusted third party (TTP). The two most common TTPs are forensic analysts and notaries.
A forensic analyst who is a specialist in handwriting can look at a signature, compare it to a known
valid signature, and make a reasonable assessment of the legitimacy of the first signature.
A notary: provides a witness whose job is to verify the identity of an individual by checking other
credentials and affixing their certification that the party signing is who they claim to be. Further, a
notary provides the extra benefit of maintaining independent logs of their transactions, complete with
Page 71 of 118


the type of credential checked and another signature that can independently be verified by the preceding
forensic analyst. For this double security, notaries are the preferred form of verification.
On the digital side, the only TTP is the repository for public key certificates. This provides the recipient
with the ability to verify the origin of an item even if no direct exchange of the public information has
ever been made. The digital signature, however, is forensically identical in both legitimate and forged
uses - if someone possesses the private key they can create a "real" signature. The protection of the
private key is the idea behind the United States Department of Defense's Common Access Card (CAC),
which never allows the key to leave the card and therefore necessitates the possession of the card in
addition to the personal identification number (PIN) code necessary to unlock the card for permission
to use it for encryption and digital signatures.

## Summary

In this lesson, you have learnt that

1. Non-repudiation is a term in the legal setting that is often used to challenge the authenticity of a
signature.
2. It also checks for the integrity and origin of a data with the view to assert authentication with high
assurance in digital security.
3. To reduce the risk of challenging the trustworthiness of a signature, the use of a Trusted Third Party
(TTP) which is either Forensic Analysts or Notaries is embraced.

## Post-Test

1. Briefly explain what you understand non-repudiation to mean.
2. How to you think the non-repudiation concept can be made used of in computer security?


3. Briefly explain what you understand non-repudiation to mean.
4. How to you think the non-repudiation concept can be made used of in computer security?

## References

"Non-repudiation in Electronic Commerce" (Jianying Zhou), Artech House, 2001
Non-Repudiation in the Digital Environment (Adrian McCullagh)
'Non-repudiation' taken from Stephen Mason, Electronic Signatures in Law (3rd edn, Cambridge
University Press, 2012) Page 73 of 118


# Lesson Nine: Hash Function (1)

## Introduction

A hash function takes a group of characters (called a key) and maps it to a value of a certain length
(called a hash value or hash). The hash value is representative of the original string of characters, but
is normally smaller than the original. Hashing is done for indexing and locating items in databases
because it is easier to find the shorter hash value than the longer string. It is also used in encryption.
This lesson outlines the meaning of hash function, its usefulness, properties and various hash function
algorithms that can be used to enhance computer security.

## Objectives

After completing this lesson, you will be able to do the following:

1. Understand the meaning of hash function
2. Understand the usefulness of hash function.
3. Understand hash function properties

## 9.1 Definitions

A hash function is any function that can be used to map digital data of arbitrary size to digital data of
fixed size. The values returned by a hash function are called hash values, hash codes, hash sums, or
simply hashes. One practical use is a data structure called a hash table, widely used in computer
software for rapid data lookup. Hash functions accelerate table or database lookup by detecting
duplicated records in a large file. An example is finding similar stretches in DNA sequences. They are
also useful in cryptography. A cryptographic hash function allows one to easily verify that some input
data matches a stored hash value, but makes it hard to construct any data that would hash to the same
value or find any two unique data pieces that hash to the same value. Page 74 of 118


## 9.2 Uses of Hash Functions

1. Hash tables: Hash functions are primarily used in hash tables, to quickly locate a data record (e.g.,
a dictionary definition) given its search key (the headword). Specifically, the hash function is used to
map the search key to an index; the index gives the place in the hash table where the corresponding
record should be stored. Hash tables, in turn, are used to implement associative arrays and dynamic
sets.
2. Caches: Hash functions are also used to build caches for large data sets stored in slow media. A
cache is generally simpler than a hashed search table, since any collision can be resolved by discarding
or writing back the older of the two colliding items. This is also used in file comparison.
3. Bloom filters: Hash functions are an essential ingredient of the Bloom filter, a space-efficient
probabilistic data structure that is used to test whether an element is a member of a set.
4. Finding duplicate records: When storing records in a large unsorted file, one may use a hash
function to map each record to an index into a table T, and collect in each bucket T[i] a list of the
numbers of all records with the same hash value i. Once the table is complete, any two duplicate records
will end up in the same bucket. The duplicates can then be found by scanning every bucket T[i] which
contains two or more members, fetching those records, and comparing them.
Page 75 of 118


5. Protecting data: A hash value can be used to uniquely identify secret information. This requires
that the hash function is collision resistant, which means that it is very hard to find data that generate
the same hash value. These functions are categorized into cryptographic hash functions and provably
secure hash functions.


6. Finding similar records: Hash functions can also be used to locate table records whose key is
similar, but not identical, to a given key; or pairs of records in a large file which have similar keys. For
that purpose, one needs a hash function that maps similar keys to hash values that differ by at most m,
where m is a small integer (say, 1 or 2). If one builds a table T of all record numbers, using such a hash
function, then similar records will end up in the same bucket, or in nearby buckets. Then one need only
check the records in each bucket T[i] against those in buckets T[i+k] where k ranges between −m and
m.


7. Finding similar substrings: The same techniques can be used to find equal or similar stretches in
a large collection of strings, such as a document repository or a genomic database. In this case, the
input strings are broken into many small pieces, and a hash function is used to detect potentially equal
pieces, as above.


8. Geometric hashing: This principle is widely used in computer graphics, computational geometry
and many other disciplines, to solve many proximity problems in the plane or in three-dimensional
space, such as finding closest pairs in a set of points, similar shapes in a list of shapes, similar images
in an image database, and so on.

9.2.1 Standard uses of hashing in cryptography
Some standard applications that employ hash functions include authentication, message integrity
(using an HMAC (Hashed MAC)), message fingerprinting, data corruption detection, and digital
signature efficiency.


## 9.3 Properties of Hash Functions

Good hash functions, in the original sense of the term, are usually required to satisfy certain properties
listed below.

1. Determinism: A hash procedure must be deterministic—meaning that for a given input value
    it must always generate the same hash value. In other words, it must be a function of the data
    to be hashed, in the mathematical sense of the term. 2. Uniformity: A good hash function
    should map the expected inputs as evenly as possible over its output range. That is, every hash
    value in the output range should be generated with roughly the same probability.

Defined range: It is often desirable that the output of a hash function has fixed size. If, for example,
the output is constrained to 32-bit integer values, the hash values can be used to index into an array.
Such hashing is commonly used to accelerate data searches.

4. Variable range: In many applications, the range of hash values may be different for each run of the
program, or may change along the same run (for instance, when a hash table needs to be expanded). In
those situations, one needs a hash function which takes two parameters—the input data z, and the
number n of allowed hash values.
5. Variable range with minimal movement (dynamic hash function): When the hash function is
used to store values in a hash table that outlives the run of the program, and the hash table needs to be
expanded or shrunk, the hash table is referred to as a dynamic hash table.
6. Data normalization: In some applications, the input data may contain features that are irrelevant
for comparison purposes. For example, when looking up a personal name, it may be desirable to ignore
the distinction between upper and lower case letters. For such data, one must use a hash function that
is compatible with the data equivalence criterion being used: that


is, any two inputs that are considered equivalent must yield the same hash value. This can be
accomplished by normalizing the input before hashing it, as by upper-casing all letters.

7. Continuity: A hash function that is used to search for similar (as opposed to equivalent) data must
be as continuous as possible; two inputs that differ by a little should be mapped to equal or nearly equal
hash values. Continuity is desirable for hash functions only in some applications, such as hash tables
used in nearest neighbour search.
8. Non-invertible: In cryptographic applications, hash functions are typically expected to be non-
invertible, meaning that it is not possible to reconstruct the input datum x from its hash value h(x) alone
without spending great amounts of computing time (see also One-way function).

## Summary

In this lesson, you have learnt that

1. A hash value is a number generated from a string of text.
2. The hash is significantly smaller than the text itself and is generated by a formula in such a way that
it is extremely unlikely that some other text will produce the same hash value.
3. Hashing plays a role in security when it is used to ensure that transmitted messages have not been
tampered with. To do this, the sender generates a hash of the message, encrypts it, and sends it with
the message itself. The recipient then decrypts both the message and the hash, produces another hash
from the received message, and compares the two hashes. If they are the same, there is a very high
probability that the message was transmitted intact.

## Post-Test

1. Briefly explain what you understand hash function to mean.
2. Briefly explain five uses of hash function.
3. Briefly explain five properties of hash function


4. Briefly explain what you understand hash function to mean.
5. Explain how hashing could be used as computer security measure?

## References

Bret Mulvey, Evaluation of CRC32 for Hash Tables, in Hash Functions. Accessed April 10, 2009.
Bret Mulvey, Evaluation of SHA-1 for Hash Tables, in Hash Functions. Accessed April 10, 2009.
[http://citeseer.ist.psu.edu/viewdoc/summary?doi=10.1.1.18.7520](http://citeseer.ist.psu.edu/viewdoc/summary?doi=10.1.1.18.7520) Performance in Practice of String
Hashing Functions
Knuth, Donald (1973). The Art of Computer Programming, volume 3, Sorting and Searching. pp. 506–
542.
Menezes, Alfred J.; van Oorschot, Paul C.; Vanstone, Scott A (1996). Handbook of Applied
Cryptography. CRC Press. ISBN 0849385237.
Peter Kankowski. "Hash functions: An empirical comparison".
Sedgewick, Robert (2002). "14. Hashing". Algorithms in Java (3 ed.). Addison Wesley. ISBN 978-
0201361209.
Shlomi Dolev, Limor Lahiani, Yinnon Haviv, "Unique permutation hashing," Theoretical Computer
Science Volume 475, 4 March 2013, Pages 59–65 Page 79 of 118


# Lesson Ten: Hash Function (2)

## Introduction

In continuation of our last lesson, we will look at hash function algorithms and some examples of hash
functions as well. A hash function takes a group of characters (called a key) and maps it to a value of
a certain length (called a hash value or hash). The hash value is representative of the original string of
characters, but is normally smaller than the original. Hashing is done for indexing and locating items
in databases because it is easier to find the shorter hash value than the longer string. It is also used in
encryption.

## Objectives

After completing this lesson, you will be able to do the following:

1. Understand hash function algorithms
2. Know some examples of hash functions

## 10.1 Hash Function Algorithms

10.1.1 Trivial Hash Function
If the datum to be hashed is small enough, one can use the datum itself (reinterpreted as an integer) as
the hashed value. The cost of computing this "trivial" (identity) hash function is effectively zero. This
hash function is perfect, as it maps each input to a distinct hash value.
The meaning of "small enough" depends on the size of the type that is used as the hashed value.


10.1.2 Perfect Hashing
A perfect hash function for the four names shown
A hash function that is injective—that is, maps each valid input to a different hash value—is said to be
perfect. With such a function one can directly locate the desired entry in a hash table, without any
additional searching.
10.1.3 Minimal perfect hashing
A minimal perfect hash function for the four names shown
A perfect hash function for n keys is said to be minimal if its range consists of n consecutive integers,
usually from 0 to n−1. Besides providing single-step lookup, a minimal perfect hash function also
yields a compact hash table, without any vacant slots. Minimal perfect hash functions are much harder
to find than perfect ones with a wider range.
iv. Hashing uniformly distributed data


If the inputs are bounded-length strings and each input may independently occur with uniform
probability (such as telephone numbers, car license plates, invoice numbers, etc.), then a hash function
needs to map roughly the same number of inputs to each hash value. For instance, suppose that each
input is an integer z in the range 0 to N−1, and the output must be an integer h in the range 0 to n−1,
where N is much larger than n. Then the hash function could be h = z mod n (the remainder of z divided
by n), or h = (z × n) ÷ N (the value z scaled down by n/N and truncated to an integer), or many other
formulas.
10.1.4 Hashing Data with Other Distributions
These simple formulas will not do if the input values are not equally likely, or are not independent. For
instance, most patrons of a supermarket will live in the same geographic area, so their telephone
numbers are likely to begin with the same 3 to 4 digits. In that case, if m is 10000 or so, the division
formula (z × m) ÷ M, which depends mainly on the leading digits, will generate a lot of collisions;
whereas the remainder formula z mod m, which is quite sensitive to the trailing digits, may still yield
a fairly even distribution.
10.1.5 Hashing Variable-Length Data
When the data values are long (or variable-length) character strings—such as personal names, web
page addresses, or mail messages—their distribution is usually very uneven, with complicated
dependencies. For example, text in any natural language has highly non-uniform distributions of
characters, and character pairs, very characteristic of the language. For such data, it is prudent to use a
hash function that depends on all characters of the string—and depends on each character in a different
way.


10.1.6 Special-Purpose Hash Functions
In many cases, one can design a special-purpose (heuristic) hash function that yields many fewer
collisions than a good general-purpose hash function. For example, suppose that the input data are file
names such as FILE0000.CHK, FILE0001.CHK, FILE0002.CHK, etc., with mostly sequential numbers. For
such data, a function that extracts the numeric part k of the file name and returns k mod n would be
nearly optimal.
10.1.7 Rolling Hash
In some applications, such as substring search, one must compute a hash function h for every k-
character substring of a given n-character string t; where k is a fixed integer, and n is k. The
straightforward solution, which is to extract every such substring s of t and compute h(s) separately,
requires a number of operations proportional to k·n. However, with the proper choice of h, one can use
the technique of rolling hash to compute all those hashes with an effort proportional to k + n.
10.1.8 Universal Hashing
A universal hashing scheme is a randomized algorithm that selects a hashing function h among a family
of such functions, in such a way that the probability of a collision of any two distinct keys is 1/n, where
n is the number of distinct hash values desired—independently of the two keys. Universal hashing
ensures (in a probabilistic sense) that the hash function application will behave as well as if it were
using a random function, for any distribution of the input data.
10.1.9 Hashing with Checksum Functions
One can adapt certain checksum or fingerprinting algorithms for use as hash functions. Some of those
algorithms will map arbitrary long string data z, with any typical real-world distribution—no matter
how non-uniform and dependent—to a 32-bit or 64-bit string, from which one can extract a hash value.


in 0 through n − 1. This method may produce a sufficiently uniform distribution of hash values, as long
as the hash range size n is small compared to the range of the checksum or fingerprint function..
10.1.10 Hashing with Cryptographic Hash Functions
Some cryptographic hash functions, such as SHA-1, have even stronger uniformity guarantees than
checksums or fingerprints, and thus can provide very good general-purpose hashing functions. In
ordinary applications, this advantage may be too small to offset their much higher cost. However, this
method can provide uniformly distributed hashes even when the keys are chosen by a malicious agent.
This feature may help to protect services against denial of service attacks.
10.1.11 Hashing By Nonlinear Table Lookup
Tables of random numbers (such as 256 random 32 bit integers) can provide high-quality nonlinear
functions to be used as hash functions or for other purposes such as cryptography. The key to be hashed
would be split into 8-bit (one byte) parts and each part will be used as an index for the nonlinear table.
The table values will be added by arithmetic or XOR addition to the hash output value. Because the
table is just 1024 bytes in size, it will fit into the cache of modern microprocessors and allow for very
fast execution of the hashing algorithm.
10.1.12 Locality-Sensitive Hashing
Locality-sensitive hashing (LSH) is a method of performing probabilistic dimension reduction of high-
dimensional data. The basic idea is to hash the input items so that similar items are mapped to the same
buckets with high probability (the number of buckets being much smaller than the universe of possible
input items). This is different from the conventional hash functions, such as those used in cryptography,
as in this case the goal is to maximize the probability of "collision" of similar items rather than to avoid
collisions.


## 10.2 List of hash functions

NIST hash function competition, Bernstein hash, Fowler-Noll-Vo hash function (32, 64, 128, 256, 512,
or 1024 bits), Jenkins hash function (32 bits), Pearson hashing (64 bits), Zobrist hashing, Almost linear
hash function

## Summary

In this lesson, you have learnt that

1. There are several types of hash functions and hash function algorithms.
2. Hash function algorithms are used to derive the various hash functions

## Post-Test

1. Briefly explain five hash function algorithms
2. List five examples of hash functions

## References

Bret Mulvey, Evaluation of CRC32 for Hash Tables, in Hash Functions. Accessed April 10, 2009.
Bret Mulvey, Evaluation of SHA-1 for Hash Tables, in Hash Functions. Accessed April 10, 2009.
[http://citeseer.ist.psu.edu/viewdoc/summary?doi=10.1.1.18.7520](http://citeseer.ist.psu.edu/viewdoc/summary?doi=10.1.1.18.7520) Performance in Practice of String
Hashing Functions
Knuth, Donald (1973). The Art of Computer Programming, volume 3, Sorting and Searching. pp. 506–
542.
Menezes, Alfred J.; van Oorschot, Paul C.; Vanstone, Scott A (1996). Handbook of Applied
Cryptography. CRC Press. ISBN 0849385237.
Peter Kankowski. "Hash functions: An empirical comparison".


Sedgewick, Robert (2002). "14. Hashing". Algorithms in Java (3 ed.). Addison Wesley. ISBN 978-
020136 1209.
Shlomi Dolev, Limor Lahiani, Yinnon Haviv, "Unique permutation hashing," Theoretical Computer
Science Volume 475, 4 March 2013, Pages 59– 65


# Lesson Eleven: Electronic Mail Security

## Introduction

Electronic mail, most commonly referred to as email or e-mail since 1993, is a method of exchanging
digital messages from an author to one or more recipients. Modern email operates across the Internet
or other computer networks. Some early email systems required that the author and the recipient both
be online at the same time, in common with instant messaging. Today's email systems are based on a
store-and-forward model. Email servers accept, forward, deliver, and store messages. Neither the users
nor their computers are required to be online simultaneously; they need connect only briefly, typically
to a mail server, for as long as it takes to send or receive messages. This lesson outlines the concept
behind email and the attached security challenges the various ways of using cryptography to protect
email messages the different email encryption techniques, methods of sending malicious email and
how to identify the source/origin of an email.

## Objectives

After completing this lesson, you will be able to do the following:

1. Understand the concept behind email and the attached security challenges.
2. Understand various ways of using cryptography to protect email messages.
3. Understand email encryption techniques
4. Understand different ways of sending malicious email and how to identify the source of an email

## 11.1 Email Messages

Email messages are composed, delivered, and stored in a multiple step process, which starts with the
message's composition. When the user finishes composing the message and sends it, the message is


transformed into a standard format: an RFC 2822 formatted message. Afterwards, the message can be
transmitted. Using a network connection, the mail client, referred to as a mail user agent (MUA),
connects to a mail transfer agent (MTA) operating on the mail server. The mail client then provides
the sender‘s identity to the server. Next, using the mail server commands, the client sends the recipient
list to the mail server. The client then supplies the message. Once the mail server receives and processes
the message, several events occur: recipient server identification, connection establishment, and
message transmission. Using Domain Name System (DNS) services, the sender‘s mail server
determines the mail server(s) for the recipient(s). Then, the server opens up a connection(s) to the
recipient mail server(s) and sends the message employing a process similar to that used by the
originating client, delivering the message to the recipient(s).
Email messages can be protected by using cryptography in various ways, such as the following:
i. Signing an email message to ensure its integrity and confirm the identity of its sender.

ii. Encrypting the body of an email message to ensure its confidentiality.

iii. Encrypting the communications between mail servers to protect the confidentiality of both message
body and message header.

The first two methods, message signing and message body encryption, are often used together;
however, encrypting the transmissions between mail servers is typically used only when two
organizations want to protect emails regularly sent between each other.
For example, the organizations could establish a virtual private network (VPN) to encrypt the
communications between their mail servers over the Internet. Unlike methods that can only encrypt a
message body, a VPN can encrypt entire messages, including email header information such as
senders, recipients, and subjects. In some cases, organizations may need to protect header information.


However, a VPN solution alone cannot provide a message signing mechanism, nor can it provide
protection for email messages along the entire route from sender to recipient.

## 11.2 Email Encryption Technique

11.2.1 Multipurpose Internet Mail Extensions (MIME)
MIME transforms non-ASCII data at the sender's site to Network Virtual Terminal (NVT) ASCII data
and delivers it to client's Simple Mail Transfer Protocol (SMTP) to be sent through the Internet. The
server SMTP at the receiver's side receives the NVT ASCII data and delivers it to MIME to be
transformed back to the original non-ASCII data.
11.2.2 Message Authentication Code
A Message authentication code (MAC) is a cryptography method that uses a secret key to encrypt a
message. This method outputs a MAC value that can be decrypted by the receiver, using the same
secret key used by the sender. The Message Authentication Code protects both a message's data
integrity as well as its authenticity.

## 11.3 Ways of Sending Malicious Email

11.3.1 Email spoofing
It is the creation of email messages with a forged sender address something which is simple to do
because the core protocols do no authentication. Spam and phishing emails typically use such spoofing
to mislead the recipient about the origin of the message.
11.3.2 Use by spam and worms
Malware such as Klez and Sober and many more modern examples often search for email addresses
within the computer they have infected, and use those addresses both as targets for email, but also to
Page 89 of 118


create credible forged From fields in the emails that they send, so that these emails are more likely to
be opened.
11.3.3 Email bomb
In Internet usage, an email bomb is a form of net abuse consisting of sending huge volumes of email
to an address in an attempt to overflow the mailbox or overwhelm the server where the email address
is hosted in a denial-of-service attack.
Methods of email bombing
There are three methods of perpetrating an email bomb; Mass mailing, list linking and zip bombs:

1. Mass Mailing: Mass mailing consists of sending numerous duplicate mails to the same email
address. These types of mail bombs are simple to design but their extreme simplicity means they can
be easily detected by spam filters.
2. List Linking: List linking means signing a particular email address up to several email list
subscriptions. The victim then has to unsubscribe from these unwanted services manually. In order to
prevent this type of bombing, most email subscription services send a confirmation email to a person's
inbox when that email is used to register for a subscription. This method of prevention is easily


circumvented: if the perpetrator registers a new email account and sets it to automatically forward all
mail to the victim, he or she can reply to the confirmation emails, and the list linking can proceed.

3. Zip bombing: A ZIP bomb is a variant of mail-bombing. After most commercial mail servers began
checking mail with anti-virus software and filtering certain malicious file types, EXE, RAR, Zip, 7-
Zip, mail server software was then configured to unpack archives and check their contents as well. A
new idea to combat this solution was composing a "bomb" consisting of an enormous text file,
containing, for example, only the letter z repeating millions of times. Such a


file compresses into a relatively small archive, but its unpacking (especially by early versions of mail
servers) would use a greater amount of processing, which could result in a DoS (Denial of Service).

11.4 Identifying the source of the email
Although email spoofing is effective in forging the email address, the IP address of the computer
sending the mail can generally be identified from the "Received:" lines in the email header. In many
cases this is likely to be an innocent third party infected by malware that is sending the email without
the owner's knowledge.

## Summary

1. Electronic mail is a medium of communication which involves the exchange of digital messages
from an author to one or more recipients through the internet.
2. Because of the confidentiality of the messages and different attacks such as email spoofing, spam
and worms, necessary security feature must be put in place.
3. Example of such measures include. Cryptography Email Encryption Techniques includes Multi
Internet Mail Extension, Message Authentication Code.

## Post-Test

1. Briefly discuss ways by malicious mail could be sent
2. Explain what email bomb means
3. Briefly explain the email encryption techniques
4. Briefly explain concept behind email and the attached security challenges.
5. Explain how sending/receiving can pose serious challenge(s) computer security?


## References

Alan Henry, Lifehacker. "How to Encrypt Your Email and Keep Your Conversations Private." Aug
14, 2013. Retrieved May 28, 2014.
Luis Rivera, SC Magazine. "Protecting customer privacy through email encryption." March 11, 2014.
July 18, 2014.
Luis Rivera, SC Magazine. ―[1].‖ March 11, 2014. July 22, 2014. By Stan Gibson,
SearchHealthIT.com. "[2]." April 2010. July 22, 2014.
Eric Geier, PCWorld. "How to Encrypt Your Email." Apr 25, 2012. Retrieved May 28, 2014.
Gaw, Shirley; Felten, Edward W.; Fernandez-Kelly, Patricia. "Secrecy, Flagging, and Paranoia:
Adoption Criteria in Encrypted E-Mail | CHI 2006 (Proceedings of ACM SigChi)" (PDF).
Cs.princeton.edu.
In Security and Usability: Designing Secure Systems that People Can Use, eds. L. Cranor and G.
Simson. O'Reilly, 2005, pp. 679-702. "Why Johnny Can‘t Encrypt."
Kindervag, Stephanie; Balaouras; McKee, Jessica (January 30, 2012). "Killing Data (this report costs
499 dollars)". Forrester.com.
Klint Finley, WIRED. "Google‘s Revamped Gmail Could Take Encryption Mainstream." Apr 23,

2014. Retrieved June 04, 2014.


# Lesson Twelve: Internet Protocol Security (IPsec)

## Introduction

Internet Protocol Security (IPsec) is a protocol suite for securing Internet Protocol (IP) communications
by authenticating and encrypting each IP packet of a communication session. It includes protocols for
establishing mutual authentication between agents at the beginning of the session and negotiation of
cryptographic keys to be used during the session. IPsec can be used in protecting data flows between
a pair of hosts (host-to-host), between a pair of security gateways (network-to-network), or between a
security gateway and a host (network-to-host).This lesson outlines Internet Protocol Security (IPsec)
definition, the two main types of transformation that form the basis of IPsec and its architecture.

## Objectives

After completing this lesson, you will be able to do the following:

1. Understand the meaning Internet Protocol Security (IPsec)
2. Understand the two main types of transformation that form the basis of IPsec
3. Understand Internet Protocol Security (IPsec) architecture

## 12.1 Internet Protocol Security

Internet Protocol Security (IPsec) is designed to protect communication in a secure manner using
TCP/IP i.e. Internet protocol suite. It uses cryptographic security services to protect communications
over Internet Protocol (IP) networks. IPsec supports network-level peer authentication, data origin
authentication, data integrity, data confidentiality (encryption), and replay protection.
IPsec is an end-to-end security scheme operating in the Internet Layer of the Internet Protocol Suite,
while some other Internet security systems in widespread use, such as Transport Layer Security (TLS)


and Secure Shell (SSH), operate in the upper layers at Application layer. Hence, only IPsec protects
any application traffic over an IP network. Applications can be automatically secured by IPsec at the
IP layer.
It is also a set of security extensions developed by the Internet Engineering Task force IETF, which
provides security and authentication at the IP layer by transforming data using encryption. Two main
types of transformation that form the basis of IPsec:
i. The Authentication Header (AH)

ii. ESP.

These two protocols provide data integrity, data origin authentication, and anti-replay service. These
protocols can be used alone or in combination to provide the desired set of security services for the
Internet Protocol (IP) layer.
12.2 Security architecture
The basic components of the IPsec security architecture are described in terms of the following
functionalities:
i. Security protocols for AH and ESP

ii. Security association for policy management and traffic processing

iii. Manual and automatic key management for the Internet key exchange (IKE)

iv. Algorithms for authentication and encryption

The set of security services provided at the IP layer includes access control, data origin integrity,
protection against replays, and confidentiality. The algorithm allows these sets to work independently
without affecting other parts of the implementation. The IPsec implementation is operated in a host or
security gateway environment giving protection to IP traffic.


The IPsec suite is an open standard and it uses the following protocols to perform various functions:
i. Authentication Headers (AH) provide connectionless integrity and data origin authentication for IP
datagrams and provides protection against replay attacks.

ii. Encapsulating Security Payloads (ESP) provide confidentiality, data-origin authentication,
connectionless integrity, an anti-replay service (a form of partial sequence integrity), and limited
traffic-flow confidentiality.

iii. Security Associations (SA) provide the bundle of algorithms and data that provide the parameters
necessary for AH and/or ESP operations.

## 12.3 Authentication Header

It is a member of the IPsec protocol suite. AH guarantees connectionless integrity and data origin
authentication of IP packets. Further, it can optionally protect against replay attacks by using the sliding
window technique and discarding old packets.
i. In IPv4, the AH protects the IP payload and all header fields of an IP datagram except for mutable
fields (i.e. those that might be altered in transit), and also IP options such as the IP Security Option
(RFC-1108).

ii. In IPv6, the AH protects most of the IPv6 base header, AH itself, non-mutable extension headers
after the AH, and the IP payload.

## 12.4 Encapsulating Security Payloads (ESP)

Encapsulating Security Payload (ESP) provides confidentiality, in addition to authentication, integrity,
and anti-replay. ESP can be used alone, or in combination with AH. It does not normally sign the entire
packet unless it is being tunnelled—ordinarily, just the IP data payload is protected, not the IP header.
For example, Alice on Computer A sends data to Bob on Computer B. The data payload is


encrypted and signed for integrity. Upon receipt, after the integrity verification process is complete,
the data payload in the packet is decrypted. Bob can be certain it was really Alice who sent the data;
that the data is unmodified, and that no one else was able to read it.

## 12.5 Security token

Some online sites offer customers the ability to use a six-digit code which randomly changes every
30 – 60 seconds on a security token. The keys on the security token have built in mathematical
computations and manipulate numbers based on the current time built into the device. This means that
every thirty seconds there is only a certain array of numbers possible which would be correct to validate
access to the online account. The website that the user is logging into would be made aware of that
devices' serial number and would know the computation and correct time built into the device to verify
that the number given is indeed one of the handful of six-digit numbers that works in that given 30- 60
second cycle. After 30–60 seconds the device will present a new random six-digit number which can
log into the website.

## Summary

In this lesson, you have learnt that

1. IPSec is a security measure that is designed to protect communication using TCP/IP. It protects any
application traffic over an IP network.
2. IPsec has some advantages, to protect data flows between a pair of hosts (host-to-host), a pair of
security gateways (network-to-network), or between a security gateway and a host (network-to-host).
3. The authentication Header (AH) and Encapsulating Security Payloads (ESP) are the two main types
of transformation that form the basis of IPsec.


4. The architecture of IPsec is described by the following functions: Security protocols for AH and
ESP, Security association for policy management and traffic processing, Manual and automatic key
management for the Internet Key Exchange (IKE) and Algorithms for authentication and encryption.

## Post-Test

1. Briefly explain what you understood Internet Protocol Security (IPsec) to mean.
2. Briefly explain Authentication Headers (AH) component of the IPsec
3. Briefly explain Encapsulating Security Payloads (ESP) component of the IPsec
4. Briefly explain what you understood Internet Protocol Security (IPsec) to mean.
5. Explain how (IPsec) could be used as computer security measure?

## References

RFC4301: Security Architecture for the Internet Protocol". Network Working Group of the IETF.
December 2005. p. 4. "The spelling "IPsec" is preferred and used throughout this and all related IPsec
standards. All other capitalizations of IPsec [...] are deprecated."
Thayer, R.; Doraswamy, N.; Glenn, R. (November 1998). IP Security Document Roadmap. IETF. RFC
2411.
Kent, S.; Atkinson, R. (November 1998). IP Authentication Header. IETF. RFC 2402.
Hoffman, P. (December 2005). Cryptographic Suites for IPsec. IETF. RFC 4308.
Kent, S. (December 2005). IP Authentication Header. IETF. RFC 4302.
Kent, S. (December 2005). IP Encapsulating Security Payload (ESP). IETF. RFC 4303.
Paterson, Kenneth G.; Yau, Arnold K.L. (2006- 04 - 24). "Cryptography in theory and practice: The case
of encryption in IPsec" (PDF). Eurocrypt 2006, Lecture Notes in Computer Science Vol. 4004. Berlin.
pp. 12–29. Retrieved 2007- 08 - 13.


Degabriele, Jean Paul; Paterson, Kenneth G. (2007- 08 - 09). "Attacking the IPsec Standards in
Encryption-only Configurations" (PDF). IEEE Symposium on Security and Privacy, IEEE Computer
Society. Oakland, CA. pp. 335–349. Retrieved 2007- 08 - 13. Page 98 of 118


# Lesson Thirteen: Web Application Security

## Introduction

Web application security is a branch of Information Security that deals specifically with security of
websites, web applications and web services. At a high level, Web application security draws on the
principles of application security but applies them specifically to Internet and Web systems. Typically
web applications are developed using programming languages such as PHP, ASP.NET etc. This lesson
outlines the concept behind web application security, methods of web application attacks, Web
Application Security standards and Web Security technology.

## Objectives

After completing this lesson, you will be able to do the following:

1. Understand the concept behind web application security
2. Understand methods of web application attacks.
3. Understand Web Application Security standards
4. Understand Web Security technology

## 13.1 Web Applications Threats

With the emergence of Web 2.0, increased information sharing through social networking and
increasing business adoption of the Web as a means of doing business and delivering service, websites
are often attacked directly. Hackers either seek to compromise the corporate network or the end-users
accessing the website by subjecting them to drive-by downloading. As a result, industry is paying
increased attention to the security of the web applications themselves in addition to the security of the
underlying computer network and operating systems. Page 99 of 118


The majority of web application attacks occur through cross-site scripting (XSS) and SQL injection
attacks which typically result from flawed coding, and failure to sanitize input to and output from the
web application. Phishing is another common threat to the Web application.

## 13.2 Cross-site Scripting

Cross-site Scripting is a type of computer security vulnerability typically found in Web applications.
It enables attackers to inject client-side script into Web pages viewed by other users. A cross-site
scripting vulnerability may be used by attackers to bypass access controls such as the same origin
policy.
By finding ways of injecting malicious scripts into web pages, an attacker can gain elevated access-
privileges to sensitive page content, session cookies, and a variety of other information maintained by
the browser on behalf of the user. Cross-site scripting attacks are therefore a special case of code
injection.
**13.1.1 Types of Cross-site scripting**
There is no single, standardized classification of cross-site scripting flaws, but most experts distinguish
between at least two primary types of XSS: non-persistent and persistent.

1. Non-persistent (Reflected): The non-persistent (or reflected) cross-site scripting vulnerability is by
far the most common type. These holes show up when the data provided by a web client, most
commonly in HTTP query parameters or in HTML form submissions, is used immediately by server-
side scripts to parse and display a page of results for and to that user, without properly sanitizing the
request. A reflected attack is typically delivered via email or a neutral web site. The bait is an innocent-
looking URL, pointing to a trusted site but containing


the XSS vector. If the trusted site is vulnerable to the vector, clicking the link can cause the victim's
browser to execute the injected script.

2. Persistent: The persistent (or stored) XSS vulnerability is a more devastating variant of a cross-site
scripting flaw: it occurs when the data provided by the attacker is saved by the server, and then
permanently displayed on "normal" pages returned to other users in the course of regular browsing,
without proper HTML escaping. A classic example of this is with online message boards where users
are allowed to post HTML formatted messages for other users to read. Persistent XSS can be more
significant than other types because an attacker's malicious script is rendered automatically, without
the need to individually target victims or lure them to a third-party website. Particularly in the case of
social networking sites, the code would be further designed to self-propagate across accounts, creating
a type of a client-side worm.

## 13.3 SQL injection

It is a code injection technique, used to attack data-driven applications, in which malicious SQL
statements are inserted into an entry field for execution (e.g. to dump the database contents to the
attacker). SQL injection must exploit a security vulnerability in an application's software, for example,
when user input is either incorrectly filtered for string literal escape characters embedded in SQL
statements or user input is not strongly typed and unexpectedly executed. SQL injection is mostly
known as an attack vector for websites but can be used to attack any type of SQL database.
**13.3.1 Types of SQL injection**
There are five main sub-classes of SQL injection:
Classic SQLI
Blind or Inference SQL injection
Database management system-specific SQLI



```
Compounded SQLI
SQL injection + insufficient authentication
SQL injection + DDoS attacks
SQL injection + DNS hijacking
SQL injection + XSS
```
## 13.4 Phishing

It is the attempt to acquire sensitive information such as usernames, passwords, and credit card details
(and sometimes, indirectly, money) by masquerading as a trustworthy entity in an electronic
communication. It is typically carried out by email spoofing or instant messaging, and it often directs
users to enter details at a fake website whose look and feel are almost identical to the legitimate one.
It is an example of social engineering techniques used to deceive users and exploits the poor usability
of current web security technologies.
13.4.1 Types of phishing

1. Spear Phishing: It is phishing attempts directed at specific individuals or companies. Attackers may
gather personal information about their target to increase their probability of success. This technique
is, by far, the most successful on the internet today, accounting for 91% of attacks.
2. Clone Phishing: A type of phishing attack whereby a legitimate, and previously delivered, email
containing an attachment or link has had its content and recipient address(es) taken and used to create
an almost identical or cloned email. The attachment or link within the email is replaced with a
malicious version and then sent from an email address spoofed to appear to come from the original
sender. It may claim to be a resend of the original or an updated version to the original.


3. Whaling: Several recent phishing attacks have been directed specifically at senior executives and
other high profile targets within businesses, and the term whaling has been coined for these kinds of
attacks.
4. Rogue WiFi (MitM): Attackers set up or compromise free Wifi access-points, and configure them
to run man-in-the-middle (MitM) attacks, often with tools like sslstrip, to compromise all access point
users.
5. Link Manipulation: Most methods of phishing use some form of technical deception designed to
make a link in an email (and the spoofed website it leads to) appear to belong to the spoofed
organization. Misspelled URLs or the use of subdomains are common tricks used by phishers. In the
following example URL, [http://www.yourbank.example.com/,](http://www.yourbank.example.com/,) it appears as though the URL will take you
to the example section of the yourbank website; actually this URL points to the "yourbank" (i.e.
phishing) section of the example website.
6. Filter Evasion: Phishers have even started using images instead of text to make it harder for anti-
phishing filters to detect text commonly used in phishing emails. However, this has led to the evolution
of more sophisticated anti-phishing filters that are able to recover hidden text in images. These filters
use OCR (optical character recognition) to optically scan the image and filter it.
7. Website Forgery: Once a victim visits the phishing website, the deception is not over. Some
phishing scams use JavaScript commands in order to alter the address bar. This is done either by
placing a picture of a legitimate URL over the address bar, or by closing the original bar and opening
up a new one with the legitimate URL. An attacker can even use flaws in a trusted website's own scripts
against the victim. These types of attacks (known as cross-site scripting) are particularly problematic,
because they direct the user to sign in at their bank or service's


own web page, where everything from the web address to the security certificates appears correct. In
reality, the link to the website is crafted to carry out the attack, making it very difficult to spot without
specialist knowledge. Just such a flaw was used in 2006 against PayPal.

8. Phone Phishing: Not all phishing attacks require a fake website. Messages that claimed to be from
a bank told users to dial a phone number regarding problems with their bank accounts. Once the phone
number (owned by the phisher, and provided by a Voice over IP service) was dialled, prompts told
users to enter their account numbers and PIN. Vishing (voice phishing) sometimes uses fake caller-ID
data to give the appearance that calls come from a trusted organization.

13.5 Web Application Security standards
OWASP is the emerging standards body for Web application security. In particular they have published
the OWASP Top 10 which describes in detail the major threats against web applications. The Web
Application Security Consortium (WASC) has created the Web Hacking Incident Database and also
produced open source best practice documents on Web application security.

## 13.6 Web Security technology

While security is fundamentally based on people and processes, there are a number of technical
solutions to consider when designing, building and testing secure web applications. At a high level,
these solutions include:
i. Black box testing tools such as Web application security scanners, vulnerability scanners and
penetration testing software

ii. White box testing tools such as static source code analysers

iii. Fuzzing Tools used for input testing


iv. Web application security scanner (vulnerability scanner)

v. Web application firewalls (WAF) used to provide firewall-type protection at the web application
layer

vi. Password cracking tools for testing password strength and implementation

## Summary

In this lesson, you have learnt

1. Web application security is a branch of information security that deals precisely with security of
websites, web applications and web services.
2. Most web application attacks occur through cross-site scripting (XSS), SQL injection and Phishing.
3. Cross-site scripting is a type of computer security vulnerability mostly seen in Web applications.
4. SQL injection is technique used to attack data driven application in which malicious SQL statements
are inserted into an entry field for execution. It is mostly used as an attack route for websites but it can
also be used to attack any SQL database.
5. Phishing is the attempt to acquire sensitive information like passwords, usernames and credit card
details by disguising as a trustworthy party in electronic correspondence.
6. The body for measuring the standards for Web application Security is referred to as Web Application
Security Standards (WASP)

## Post-Test

1. Discuss methods of web application attacks.
2. Discuss Web Application Security Standards


3. Discuss Web Security Technology
4. Briefly explain Web Application
5. Explain how web application can pose serious challenge(s) computer security?

## References

2012 Trends Report: Application Security Risks Cenzic, Inc. 11 March 2012. Retrieved 9 July 2012.
Fonseca, J. et al (2007): Testing and Comparing Web Vulnerability Scanning Tools for SQL Injection
and XSS Attacks Dependable Computing, IEEE.
Improving Web Application Security: Threats and Countermeasures, Microsoft Corporation. June
2003.
Niels Provos et al (2007): The Ghost in the Browser.
Niels Provos et al. (2008): All Your iFrames Point to Us.
The Web Hacking Incidents Database. WASC. January 2010.
Web Application Vulnerability Scanners. NIST.


# Lesson Fourteen: Database Security

## Introduction

Database security concerns the use of a broad range of information security controls to protect
databases (potentially including the data, the database applications or stored functions, the database
systems, the database servers and the associated network links) against compromises of their
confidentiality, integrity and availability. It involves various types or categories of controls, such as
technical, procedural/administrative and physical. This lesson outlines database security, types of
database security privilege and evaluation of database security

## Objectives

After completing this lesson, you will be able to do the following:

1. Understand database security
2. Understand types of Database privilege.
3. Understand how to evaluate database security

## 14.1 Database Security Risks

Database security is a specialist topic within the broader realms of computer security, information
security and risk management.
Security risks to database systems include, for example:
i. Unauthorized or unintended activity or misuse by authorized database users, database administrators,
or network/systems managers, or by unauthorized users or hackers (e.g. inappropriate access to
sensitive data, metadata or functions within databases, or inappropriate changes to the database
programs, structures or security configurations);


ii. Malware infections causing incidents such as unauthorized access, leakage or disclosure of personal
or proprietary data, deletion of or damage to the data or programs, interruption or denial of authorized
access to the database, attacks on other systems and the unanticipated failure of database services;
iii. Overloads, performance constraints and capacity issues resulting in the inability of authorized users
to use databases as intended;
iv. Physical damage to database servers caused by computer room fires or floods, overheating,
lightning, accidental liquid spills, static discharge, electronic breakdowns/equipment failures and
obsolescence;
v. Design flaws and programming bugs in databases and the associated programs and systems, creating
various security vulnerabilities (e.g. unauthorized privilege escalation), data loss/corruption,
performance degradation etc.;
vi. Data corruption and/or loss caused by the entry of invalid data or commands, mistakes in database
or system administration processes, sabotage/criminal damage etc.

Many layers and types of information security control are appropriate to databases, including: Access
control, Auditing, Authentication, Encryption, Integrity controls, Backups, Application security,
Database Security applying Statistical Method.
Databases have been largely secured against hackers through network security measures such as
firewalls, and network-based intrusion detection systems. While network security controls remain
valuable in this regard, securing the database systems themselves, and the programs/functions and data
within them, has arguably become more critical as networks are increasingly opened to wider access,
in particular access from the Internet.


Furthermore, system, program, function and data access controls, along with the associated user
identification, authentication and rights management functions, have always been important to limit
and in some cases log the activities of authorized users and administrators. In other words, these are
complementary approaches to database security, working from both the outside-in and the inside-out
as it were.
Many organizations develop their own "baseline" security standards and designs detailing basic
security control measures for their database systems. These may reflect general information security
requirements or obligations imposed by corporate information security policies and applicable laws
and regulations (e.g. concerning privacy, financial management and reporting systems), along with
generally accepted good database security practices (such as appropriate hardening of the underlying
systems) and perhaps security recommendations from the relevant database system and software
vendors.
14.2 Types of Database privilege
Two types of privileges are important relating to database security within the database environment:
system privileges and object privileges.

1. System Privileges: System privileges allow a user to perform administrative actions in a database.
These include privileges (as found in SQL Server) such as: create database, create procedure, create
view, backup database, create table, create trigger, and execute.
2. Object Privileges: Object privileges allow for the use of certain operations on database objects as
authorized by another user. Examples include: usage, select, insert, update, and references.


## 14.3 Database Security Evaluation

One technique for evaluating database security involves performing vulnerability assessments or
penetration tests against the database. Testers attempt to find security vulnerabilities that could be used
to defeat or bypass security controls, break into the database, compromise the system etc.
In database environments where security is critical, continual monitoring for compliance with
standards improves security. Compliance monitoring is similar to vulnerability assessment, except that
the results of vulnerability assessments generally drive the security standards that lead to the
continuous monitoring program. Essentially, vulnerability assessment is a preliminary procedure to
determine risk where a compliance program is the process of on-going risk assessment.

1. Abstraction: Application level authentication and authorization mechanisms may be effective
means of providing abstraction from the database layer. The primary benefit of abstraction is that of a
single sign-on capability across multiple databases and platforms. A single sign-on system stores the
database user's credentials and authenticates to the database on behalf of the user.
2. Database activity monitoring (DAM): Another security layer of a more sophisticated nature
includes real-time database activity monitoring, either by analysing protocol traffic (SQL) over the
network, or by observing local database activity on each server using software agents, or both. Analysis
can be performed to identify known exploits or policy breaches, or baselines can be captured over time
to build a normal pattern used for detection of anomalous activity that could be indicative of intrusion.
3. Native Audit: In addition to using external tools for monitoring or auditing, native database audit
capabilities are also available for many database platforms. The native audit trails are extracted on a
regular basis and transferred to a designated security system where


the database administrators do not have access. This ensures a certain level of segregation of duties
that may provide evidence the native audit trails were not modified by authenticated administrators.

4. Process and Procedures: A good database security program includes the regular review of
privileges granted to user accounts and accounts used by automated processes. For individual accounts
a two-factor authentication system improves security but adds complexity and cost. Accounts used by
automated processes require appropriate controls around password storage such as sufficient
encryption and access controls to reduce the risk of compromise.
5. Statistical Methods: The greatest threat to database security is non-tracked unauthorized changes
by internal and external users. Algorithms based on cryptology and other statistical methods are
deployed to both identify these events and report threats to administrators.

## Summary

1. Unauthorized or unintended activity, Malware infections, Overloads, physical flaws are some of the
available security threats to the database.
2. Among many layers and types of information security control that are appropriate to databases,
network security measures such as firewalls, and network-based intrusion detection systems are largely
used to secure database.
3. Database security directly involves the wide range security controls to protect information in
databases, to ensure confidentiality, integrity and availability.


4. In relating to database security within the database environment, the system privileges allow a user
to perform administrative actions in a database while the object privileges allows for the use of certain
operations on database objects as authorized by another user.
5. Database security can be evaluated using all or few of the techniques such as Abstraction, Database
Active Monitoring, Native Database Audit, Processes and Procedures, Cryptology or other statistical
methods.

## Post-Test

1. What are the possible risks to the database security?
2. Discuss the two types of database security privilege
3. Briefly explain how database security can be evaluated
4. Briefly explain what you understand database security
5. Why do you think database security is important to computer security

## References

Dark Reading - Tech Insight: Database Activity Monitoring
[http://www.databasesecurity.com/dbsec/database-stig-v7r1.pdf](http://www.databasesecurity.com/dbsec/database-stig-v7r1.pdf)
Seema Kedar (1 January 2009). Database Management Systems. Technical Publications. p. 15. ISBN
978 - 81 - 8431 - 584 - 4.
Stephens, Ryan (2011). Sams teach yourself SQL in 24 hours. Indianapolis, Ind: Sams. ISBN
9780672335419.


# Lesson Fifteen: Distributed System Security

## Introduction

Security is one of the leading concerns in developing dependable distributed systems of today, since
the integration of different components in a distributed manner creates new security problems and
issues. Service oriented architectures; the Web, grid computing and virtualization form the backbone
of today‘s distributed systems. A lens to security issues in distributed systems is best provided via
deeper exploration of security concerns and solutions in these technologies.
This lesson outlines the properties of distributed systems, distributed system architecture and
distributed system security architecture (DSSA).

## Objectives

After completing this lesson, you will be able to do the following:


1. Understand distributed systems properties
2. Understand distributed system architecture
3. Understand distributed system security architecture (DSSA)

## 15.1 Distributed Computing

Distributed computing is a field of computer science that studies distributed systems. A distributed
system is a software system in which components located on networked computers communicate and
coordinate their actions by passing messages. The components interact with each other in order to
achieve a common goal. Three significant characteristics of distributed systems are: concurrency of
components, lack of a global clock, and independent failure of components. It also refers to the use of
distributed systems to solve computational problems. A problem is divided into many tasks, each of
which is solved by one or more computers, which communicate with each other by message passing.
A distributed system may have a common goal, such as solving a large computational problem.
Alternatively, each computer may have its own user with individual needs, and the purpose of the
distributed system is to coordinate the use of shared resources or provide communication services to
the users.
Other typical properties of distributed systems include the following:
i. The system has to tolerate failures in individual computers.

ii. The structure of the system (network topology, network latency, number of computers) is not known
in advance, the system may consist of different kinds of computers and network links, and the system
may change during the execution of a distributed program.

iii. Each computer has only a limited, incomplete view of the system. Each computer may know only
one part of the input.


## 15.2 Distributed System Architecture

Client/Server System: The Client-server architecture is a way to provide a service from a central
source. There is a single server that provides a service, and many clients that communicate with the
server to consume its products. In this architecture, clients and servers have different jobs. The server's
job is to respond to service requests from clients, while a client's job is to use the data provided in
response in order to perform some tasks.
Peer-to-Peer System: The term peer-to-peer is used to describe distributed systems in which labour
is divided among all the components of the system. All the computers send and receive data, and they
all contribute some processing power and memory. As a distributed system increases in size, its
capacity of computational resources increases. In a peer-to-peer system, all components of the system
contribute some processing power and memory to a distributed computation.
15.3 Distributed System Applications
Reasons for using distributed systems and distributed computing may include:
i. The very nature of an application may require the use of a communication network that connects
several computers: for example, data produced in one physical location and required in another
location.
ii. There are many cases in which the use of a single computer would be possible in principle, but the
use of a distributed system is beneficial for practical reasons. For example, it may be more cost-
efficient to obtain the desired level of performance by using a cluster of several low-end computers, in
comparison with a single high-end computer. A distributed system can provide more reliability than a
non-distributed system, as there is no single point of failure. Moreover, a distributed system may be
easier to expand and manage than a monolithic uniprocessor system.


## 15.4 Distributed System Security Architecture (DSSA)

It is a computer security architecture that provides a suite of functions including login, authentication,
and access control in a distributed system. To differ from other similar architectures, the DSSA
architecture offers the ability to access all these functions without the trusted server (known as a
certificate authority) being active.
In DSSA, security objects are handled by owners and access is controlled by the central, universally
trusted, certificate authority.
15.5 DSSA/SPX
DSSA/SPX is the authentication protocol of DSSA. The CDC is a certificate granting server while the
certificate is a ticket signed by CA which contains the public key of the party being certified. Since the
CDC is merely distributing previously signed certificates, it is not necessary for it to be trusted.

## Summary

1. A software system that allows components which are located on networked computers to
communicate by passing messages is call distributed system.
2. The purpose of this system is to coordinate the use of shared resources or provide communication
services to the users on the network. It architecture are client/server system and


peer-to-peer system. Security is one of the leading concerns in developing dependable distributed
systems. Therefore, the distributed system security architecture provides a suite of functions for login,
authentication, and access control. Security objects are handled by owners and access is controlled by
the central, universally trusted, certificate authority

## Post-Test

1. Explain what is meant by distributed system
2. Discuss the security challenge(s) that is/are inherent to distributed system and how to overcome
them.
3. Explain what is meant by distributed system
4. Discuss the security challenge(s) that is/are inherent to distributed system

## References

Attiya, Hagit and Welch, Jennifer (2004), Distributed Computing: Fundamentals, Simulations, and
Advanced Topics, Wiley-Interscience ISBN 0- 471 - 45324 - 2.
Coulouris, George et al (2011), Distributed Systems: Concepts and Design (5th Edition), Addison-
Wesley ISBN 0- 132 - 14301 - 1.
Faber, Jim (1998), Java Distributed Computing, O'Reilly: Java Distributed Computing by Jim Faber,
1998
Garg, Vijay K. (2002), Elements of Distributed Computing, Wiley-IEEE Press ISBN 0- 471 - 03600 - 5.
Ghosh, Sukumar (2007), Distributed Systems – An Algorithmic Approach, Chapman & Hall/CRC,
ISBN 978- 1 - 58488 - 564 - 1.
Herlihy, Maurice P.; Shavit, Nir N. (2008), The Art of Multiprocessor Programming, Morgan
Kaufmann, ISBN 0- 12 - 370591 - 6.


Lynch, Nancy A. (1996), Distributed Algorithms, Morgan Kaufmann, ISBN 1- 55860 - 348 - 4.
Tel, Gerard (1994), Introduction to Distributed Algorithms, Cambridge University Press


