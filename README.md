# cyber-tools-index

Cyber tools index for [free-llms-api_mcp-server](https://github.com/djmahe4/awesome-free-llm-apis/tree/main/mcp-server)

<!-- TOOLS:START -->
## Categories

- [Blockchain](#blockchain) (15)
- [Blue Team](#blue-team) (37)
- [Cloud](#cloud) (22)
- [Containers](#containers) (15)
- [Cracking](#cracking) (34)
- [Crypto](#crypto) (14)
- [Enterprise](#enterprise) (80)
- [Forensics](#forensics) (59)
- [Llm](#llm) (52)
- [Misc](#misc) (41)
- [Mobile](#mobile) (18)
- [Networking](#networking) (58)
- [PWN](#pwn) (36)
- [Recon](#recon) (87)
- [Reversing](#reversing) (33)
- [Stego](#stego) (15)
- [Web](#web) (60)
- [Wireless](#wireless) (41)

## Blockchain

| Tool | Description |
| :--- | :--- |
| [aderyn](https://github.com/Cyfrin/aderyn) | Solidity static analyzer for Rust-based projects, integrates with editors for code quality checks. |
| [crytic-compile](https://github.com/crytic/crytic-compile) | Crytic-compile is a Python library and command-line tool for compiling smart contracts across multiple frameworks and protocols, generating AST/ABI and bytecodes for analysis. |
| [crytic-medusa](https://github.com/crytic/medusa) | Parallelized, coverage-guided, mutational Solidity smart contract fuzzing tool using go-ethereum. |
| [echidna](https://hub.docker.com/r/trailofbits/echidna) | Echidna is a Haskell library for fuzzing/property-based testing of EVM code, generating inputs tailored to actual code and checking invariants. |
| [eth-ape](https://github.com/ApeWorX/ape) | eth-ape is a Python framework for building and exploring on-chain applications on Ethereum, supporting multiple contract languages and chains through a modular plugin system. |
| [foundry](https://github.com/foundry-rs/foundry) | Foundry is a blazing fast, portable, and modular toolkit for Ethereum application development, written in Rust. It includes Forge for building, testing, fuzzing, debugging, and deploying Solidity contracts, Cast for interacting with EVM smart contracts, Anvil for fast local Ethereum development, and Chisel for a fast, utilitarian, and verbose Solidity REPL. Target platform: Ethereum. |
| [halmos](https://github.com/a16z/halmos) | Halmos is a symbolic testing tool for EVM smart contracts, primarily used for formal verification of Solidity/Foundry code. |
| [heimdall-rs](https://github.com/Jon-Becker/heimdall-rs) | Heimdall-rs is a Rust-based EVM smart contract toolkit for bytecode analysis and contract information extraction. |
| [ityfuzz](https://github.com/fuzzland/ityfuzz) | ItyFuzz is a fast EVM and MoveVM smart contract hybrid fuzzer combining symbolic execution and fuzzing to find bugs in smart contracts offchain and onchain. |
| [manticore](https://pypi.org/project/manticore/) | Manticore is a symbolic execution tool for analyzing Ethereum smart contracts and Linux ELF binaries, enabling program exploration, input generation, and error discovery through a Python API and CLI. |
| [mythril](https://pypi.org/project/mythril/) | Mythril is a security analysis tool for Ethereum smart contracts, using symbolic execution, SMT solving, and taint analysis to detect vulnerabilities across various EVM-compatible blockchains. |
| [slither-analyzer](https://pypi.org/project/slither-analyzer/) | Slither is a static analysis framework for Solidity and Vyper smart contracts, detecting vulnerabilities and providing detailed contract information. |
| [solc-select](https://github.com/crytic/solc-select) | solc-select is a tool to manage and switch between different Solidity compiler versions for Ethereum development. |
| [solgraph](https://www.npmjs.com/package/solgraph) | solgraph is a JavaScript library for visualizing Solidity code dependencies, useful for developers working with Ethereum smart contracts. |
| [surya](https://www.npmjs.com/package/surya) | Surya is a JavaScript library for performing security verification on web applications, primarily used to protect against malicious bots. |

## Blue Team

| Tool | Description |
| :--- | :--- |
| [aide](https://packages.debian.org/search?keywords=aide) | aide is an advanced intrusion detection environment for Linux systems, providing file integrity checking and monitoring. |
| [apparmor-utils](https://packages.debian.org/search?keywords=apparmor-utils) | apparmor-utils provides command-line tools for managing AppArmor profiles on Linux systems. |
| [atomic-red-team](https://github.com/redcanaryco/atomic-red-team) | Atomic Red Team is a library of tests mapped to the MITRE ATT&CK framework, enabling security teams to quickly, portably, and reproducibly test their environments. |
| [auditd](https://packages.debian.org/search?keywords=auditd) | auditd is a user space tool for security auditing on Linux systems, monitoring and logging system calls and events. |
| [bandit](https://pypi.org/project/bandit/) | Bandit is a security linter for Python code that scans files for common security issues by analyzing the Abstract Syntax Tree (AST). It is used to identify vulnerabilities in Python applications. |
| [capa](https://github.com/mandiant/capa) | capa detects capabilities in executable files, identifying techniques like backdoors, service creation, and network communication. |
| [chaosreader](https://packages.debian.org/search?keywords=chaosreader) | Chaosreader is a network session tracer that exports data to HTML format, suitable for various Debian-based systems. |
| [chkrootkit](https://packages.debian.org/search?keywords=chkrootkit) | chkrootkit is a rootkit detector for Unix-like operating systems. |
| [clamav](https://packages.debian.org/search?keywords=clamav) | ClamAV is an open-source anti-virus engine for Unix systems, providing a command-line interface for virus scanning and a daemon for continuous monitoring. |
| [cortex](https://hub.docker.com/r/thehiveproject/cortex) | Cortex is an open-source, free observables analysis and active response engine for SOCs, CSIRTs, and security researchers, enabling automated analysis of IP, email, URLs, domains, files, and hashes through a web interface or REST API. |
| [darkstat](https://packages.debian.org/search?keywords=darkstat) | darkstat is a network traffic analyzer that passively monitors network traffic and generates bandwidth graphs and reports. |
| [fail2ban](https://packages.debian.org/search?keywords=fail2ban) | fail2ban bans hosts causing multiple authentication errors, protecting servers against brute-force attacks. |
| [floss](https://github.com/mandiant/flare-floss) | FLOSS is a static analysis tool for malware that automatically extracts and deobfuscates all strings from binary files, enhancing basic static analysis with advanced techniques. |
| [hayabusa](https://github.com/Yamato-Security/hayabusa) | Hayabusa is a Rust-based threat hunting and fast forensics timeline generator for Windows event logs, supporting Sigma v2 correlation rules. |
| [inetsim](https://packages.debian.org/search?keywords=inetsim) | inetsim is a software suite for simulating common internet services, useful for testing and development. |
| [laurel](https://github.com/threathunters-io/laurel) | LAUREL is an event post-processing plugin for auditd that generates useful, enriched JSON-based audit logs for modern security monitoring setups. |
| [loki](https://github.com/Neo23x0/Loki-RS) | Loki-RS is a high-performance, multi-threaded YARA & IOC scanner for Linux and macOS, designed for incident response and digital forensics. |
| [lynis](https://packages.debian.org/search?keywords=lynis) | Lynis is a security auditing tool for Unix-based systems. |
| [maltrail](https://github.com/stamparm/maltrail) | Maltrail is a network traffic detection system that identifies communication with known malicious infrastructure using a set of indicators called trails, combining static trails, public feeds, and optional operator-supplied trails. |
| [MISP-docker](https://github.com/MISP/misp-docker) | MISP-docker provides a production-ready Docker image for MISP, a collaborative platform for threat intelligence sharing, with features like MISP and MISP modules split into separate containers, optional MISP-Guard for traffic filtering, and support for LDAP, OIDC, and CustomAuth authentication. |
| [osquery](https://github.com/osquery/osquery) | osquery is a SQL-powered framework for operating system instrumentation, monitoring, and analytics, available for Linux, macOS, and Windows. |
| [phishkit-triage](https://github.com/trac3r00/phish-triage) | phishkit-triage is a Python toolkit for examining phishing emails (.eml files), extracting indicators of compromise (IOCs), and producing analyst-oriented reports and detection content. It supports SPF, DKIM, DMARC, URL and attachment hash enrichment, and assigns verdicts based on analysis. |
| [quark-engine](https://pypi.org/project/quark-engine/) | quark-engine is an Android malware scoring system that analyzes obfuscated malware samples to identify and categorize their malicious behaviors, targeting Android devices. |
| [rkhunter](https://packages.debian.org/search?keywords=rkhunter) | rkhunter is a rootkit and backdoor scanner for Linux systems. |
| [sentrypeer](https://packages.debian.org/search?keywords=sentrypeer) | sentrypeer is a network security tool for detecting and preventing peer-to-peer (P2P) traffic on a network. |
| [sigma-cli](https://pypi.org/project/sigma-cli/) | sigma-cli is a command-line interface for Sigma, a language for writing detection rules for security information and event management (SIEM) systems. It allows users to manage and execute Sigma rules on various SIEM platforms. |
| [sigma-rules](https://github.com/SigmaHQ/sigma) | Sigma-rules is an open-source repository of generic detection rules for SIEM systems, supporting various log formats and platforms. |
| [suricata](https://packages.debian.org/search?keywords=suricata) | Suricata is a high-performance open-source Intrusion Detection System (IDS) and Network Security Monitoring (NSM) tool designed to detect malicious activity in network traffic. |
| [thehive](https://hub.docker.com/r/strangebee/thehive) | TheHive: collaborative cyber incident response management platform for Docker. |
| [tiger](https://packages.debian.org/search?keywords=tiger) | Tiger is a security auditing and intrusion detection tool for Linux systems. |
| [ufw](https://packages.debian.org/search?keywords=ufw) | ufw is a command-line utility for managing a Netfilter firewall, providing a simple way to configure iptables rules for inbound and outbound traffic. |
| [velociraptor](https://github.com/Velocidex/velociraptor) | Velociraptor is an endpoint visibility and collection tool using VQL queries for digital forensics, endpoint protection, and incident response. |
| [wazuh-docker](https://github.com/wazuh/wazuh-docker) | Wazuh-docker provides Docker containers for deploying the Wazuh cybersecurity platform, including the Wazuh manager, dashboard, and OpenSearch for log analysis and monitoring. |
| [yara](https://packages.debian.org/search?keywords=yara) | YARA is a pattern matching tool for malware researchers, primarily used to identify malicious files based on patterns in binary code. |
| [yara-x-cli](https://github.com/VirusTotal/yara-x) | yara-x-cli is a Rust-based reimplementation of YARA, designed for malware analysis with improved performance and user-friendliness. It allows creating rules to detect patterns in files based on textual or binary data. |
| [zeek](https://hub.docker.com/r/zeek/zeek) | Zeek is a network forensic analysis tool for monitoring and analyzing network traffic, providing comprehensive visibility into network activity. |
| [zircolite](https://hub.docker.com/r/wagga40/zircolite) | Zircolite is a fast, standalone, and battle-tested SIGMA-based detection tool for EVTX or JSON logs, designed for real-time threat detection and analysis. |

## Cloud

| Tool | Description |
| :--- | :--- |
| [cartography](https://pypi.org/project/cartography/) | Cartography is a Python tool that pulls infrastructure assets and their relationships into a Neo4j graph database, supporting platforms like AWS, GCP, Azure, Kubernetes, and more. It helps answer questions about access, vulnerabilities, and network paths in technical infrastructure. |
| [checkov](https://github.com/bridgecrewio/checkov) | Checkov is a static code analysis tool for infrastructure as code (IaC) and software composition analysis (SCA) for images and open source packages, detecting security and compliance misconfigurations across multiple cloud platforms and IaC formats. |
| [cloud_enum](https://github.com/initstring/cloud_enum) | cloud_enum is a multi-cloud OSINT tool for enumerating public resources in AWS, Azure, and Google Cloud. |
| [CloudBrute](https://github.com/0xsha/CloudBrute) | CloudBrute is a tool for black-box enumeration of cloud infrastructure, including storage and apps on major providers like Amazon, Google, Microsoft, DigitalOcean, Alibaba, Vultr, and Linode. It supports concurrent scanning, modular configuration, and proxy support for cross-platform use. |
| [cloudfox](https://github.com/BishopFox/cloudfox) | CloudFox is an open-source command-line tool for automating situational awareness in cloud environments, helping penetration testers identify exploitable attack paths in AWS infrastructure. |
| [cloudgoat](https://pypi.org/project/cloudgoat/) | CloudGoat is a vulnerable AWS environment generator for cybersecurity professionals to practice penetration testing and cloud security skills. |
| [cloudlist](https://github.com/projectdiscovery/cloudlist) | Cloudlist is a multi-cloud tool for listing assets from various cloud providers, supporting keyless authentication and multiple output formats. |
| [cloudmapper](https://github.com/duo-labs/cloudmapper) | CloudMapper analyzes AWS environments, auditing for misconfigurations and collecting metadata, with support for generating reports and visualizations. |
| [cloudsplaining](https://pypi.org/project/cloudsplaining/) | cloudsplaining analyzes AWS IAM policies for potential misconfigurations and risks. |
| [enumerate-iam](https://github.com/andresriancho/enumerate-iam) | enumerate-iam is a Python script that enumerates AWS IAM permissions using non-destructive API calls, making it useful for security assessments and policy analysis. |
| [GCPBucketBrute](https://github.com/RhinoSecurityLabs/GCPBucketBrute) | GCPBucketBrute is a script to enumerate Google Storage buckets, determine access permissions, and check for privilege escalation using GCP user/service account credentials or unauthenticated methods. It supports Linux/OS X and Python3. |
| [kics](https://hub.docker.com/r/checkmarx/kics) | KICS scans Infrastructure as Code (IAC) files for security vulnerabilities, supporting multiple platforms and outputting results in JSON format. |
| [kube-hunter](https://pypi.org/project/kube-hunter/) | kube-hunter is a Kubernetes security scanner that detects weaknesses in Kubernetes clusters by simulating an attacker's perspective. It can be run on any machine and supports remote, interface, and network scanning. Target platform: Kubernetes. |
| [pacu](https://pypi.org/project/pacu/) | pacu is an AWS exploitation framework for testing the security of Amazon Web Services environments, compatible with Python 3.9 and later. |
| [principalmapper](https://pypi.org/project/principalmapper/) | principalmapper is a Python tool for mapping and visualizing principal components in data, useful for dimensionality reduction and feature extraction in machine learning and data analysis. |
| [prowler](https://pypi.org/project/prowler/) | Prowler is an open-source security tool for AWS, GCP, and Azure, performing security best practices assessments, audits, and compliance checks based on various frameworks like CIS, NIST, PCI-DSS, and GDPR. |
| [PurplePanda](https://github.com/carlospolop/PurplePanda) | PurplePanda identifies privilege escalation paths within and across different cloud platforms, focusing on permissions and dangerous configurations. It supports GCP, GitHub, and Kubernetes, and uses Neo4j for data visualization. |
| [roadrecon](https://pypi.org/project/roadrecon/) | roadrecon 2.0.0 is an Entra ID (Azure AD) reconnaissance tool for red and blue teams, compatible with Python 3.10-3.14. |
| [s3scanner](https://github.com/sa7mon/S3Scanner) | s3scanner is a multi-threaded tool to find open S3 buckets across various cloud providers, including AWS, DigitalOcean, DreamHost, GCP, Linode, Scaleway, and custom, by scanning bucket permissions and saving results to a Postgres database or RabbitMQ. |
| [scoutsuite](https://pypi.org/project/scoutsuite/) | Scoutsuite is an open-source security assessment tool for AWS environments, identifying misconfigurations and vulnerabilities. |
| [steampipe](https://github.com/turbot/steampipe) | Steampipe is a zero-ETL tool that allows querying APIs and services using SQL, enabling real-time data access and parallel querying across multiple data sources. |
| [stratus](https://github.com/DataDog/stratus-red-team) | Stratus Red Team emulates offensive attack techniques in the cloud for security testing and detection. |

## Containers

| Tool | Description |
| :--- | :--- |
| [cdk](https://github.com/cdk-team/CDK) | CDK is an open-source container penetration toolkit for evaluating and exploiting vulnerabilities in Kubernetes, Docker, and Containerd environments, without OS dependencies. It provides useful net-tools and PoCs/EXPs to escape containers and gain cluster control. |
| [deepce](https://github.com/stealthcopter/deepce) | deepce is a pure sh script for Docker enumeration, privilege escalation, and container escape, compatible with most containers. |
| [dive](https://github.com/wagoodman/dive) | dive is a CLI tool for exploring Docker image layers, showing contents, changes, and estimating image efficiency. It supports building and analyzing images directly from the command line and integrates with CI/CD pipelines. |
| [docker-bench-security](https://github.com/docker/docker-bench-security) | docker-bench-security is a script that automates checks for Docker container security best practices based on the CIS Docker Benchmark. |
| [dockle](https://github.com/goodwithtech/dockle) | Dockle is a container image linter for security, helping build best-practice Docker images by checking against CIS benchmarks and other security standards. |
| [grype](https://github.com/anchore/grype) | Grype is a vulnerability scanner for container images and filesystems, supporting major OS and language-specific packages, and providing threat prioritization with EPSS, KEV, and risk scoring. |
| [hadolint](https://github.com/hadolint/hadolint) | Hadolint is a Dockerfile linter that checks for best practices and potential issues in Dockerfiles, using Haskell and ShellCheck for inline Bash code validation. |
| [kube-bench](https://github.com/aquasecurity/kube-bench) | kube-bench checks Kubernetes deployments against CIS Kubernetes Benchmark security standards. |
| [kubeaudit](https://github.com/Shopify/kubeaudit) | kubeaudit is a command line tool and Go package to audit Kubernetes clusters for security concerns such as running as non-root, using a read-only root filesystem, and dropping capabilities. |
| [kubescape](https://github.com/kubescape/kubescape) | Kubescape is an open-source Kubernetes security platform for risk analysis, security, compliance, and misconfiguration scanning. |
| [kubesec](https://github.com/controlplaneio/kubesec) | kubesec is a static analysis tool for Kubernetes resources to identify security risks. |
| [peirates](https://github.com/inguardians/peirates) | Peirates is a Kubernetes penetration testing tool that automates privilege escalation and token theft within a cluster. |
| [syft](https://github.com/anchore/syft) | Syft is a CLI tool and Go library for generating Software Bill of Materials (SBOMs) from container images and filesystems, supporting multiple packaging ecosystems and output formats like CycloneDX and SPDX. |
| [terrascan](https://github.com/tenable/terrascan) | Terrascan is a static code analyzer for Infrastructure as Code, detecting compliance and security violations across various cloud platforms and IAC tools. |
| [trivy](https://github.com/aquasecurity/trivy) | Trivy is a comprehensive security scanner for container images, filesystems, Git repositories, VMs, and Kubernetes, identifying vulnerabilities, misconfigurations, secrets, and licenses. |

## Cracking

| Tool | Description |
| :--- | :--- |
| [bruteforce-luks](https://packages.debian.org/search?keywords=bruteforce-luks) | bruteforce-luks is a command-line tool for attempting to decrypt LUKS encrypted volumes by brute force. |
| [brutespray](https://github.com/x90skysn3k/brutespray) | Brutespray is a fast, multi-protocol credential brute-forcer that parses Nmap, Nessus, and Nexpose output to automatically test default and custom credentials across 40+ protocols in parallel. |
| [cewl](https://packages.debian.org/search?keywords=cewl) | cewl is a custom word list generator for ethical hacking and security testing, primarily used for creating word lists from websites for password cracking and other security assessments. |
| [changeme](https://github.com/ztgrace/changeme) | changeme is a default credential scanner supporting HTTP/HTTPS, MSSQL, MySQL, PostgreSQL, SSH, SNMP, MongoDB, and FTP protocols. It uses YAML files for credential storage and can be run on Linux with Docker support for other platforms. |
| [chntpw](https://packages.debian.org/search?keywords=chntpw) | chntpw is a utility for recovering NT SAM passwords on Windows systems. |
| [crowbar](https://github.com/galkan/crowbar) | Crowbar is a brute force tool for penetration testing, supporting protocols like OpenVPN, RDP, SSH, and VNC. |
| [crunch](https://packages.debian.org/search?keywords=crunch) | Crunch is a utility for generating custom wordlists, primarily used in cybersecurity for password cracking and security testing. |
| [cupp](https://github.com/Mebus/cupp) | CUPP (Common User Passwords Profiler) is a Python tool for generating custom wordlists based on user information, aiding in password strength analysis and dictionary attacks. |
| [DefaultCreds-cheat-sheet](https://github.com/ihebski/DefaultCreds-cheat-sheet) | DefaultCreds-cheat-sheet is a tool for cybersecurity professionals to identify devices with default passwords, assisting in penetration testing and blue team operations. |
| [duplicut](https://github.com/nil0x42/duplicut) | Duplicut removes duplicates from massive wordlists without changing their order, keeping the first occurrence of each word. It's optimized in C and can handle files larger than RAM by using chunk-based scans or disk partitions. |
| [fcrackzip](https://packages.debian.org/search?keywords=fcrackzip) | fcrackzip is a password cracker for zip archives. |
| [gpp-decrypt](https://github.com/t0thkr1s/gpp-decrypt) | gpp-decrypt is a Python tool to parse and decrypt Group Policy Preferences (GPP) XML files, extracting usernames and passwords. |
| [hashcat](https://packages.debian.org/search?keywords=hashcat) | Hashcat is a world's fastest and most advanced password recovery utility for various hash types, supporting CPU, GPU, and FPGA. |
| [hashid](https://packages.debian.org/search?keywords=hashid) | hashid identifies different types of hashes used to encrypt data, useful for cybersecurity analysis and forensic investigations. |
| [Hob0Rules](https://github.com/praetorian-inc/Hob0Rules) | Hob0Rules provides password cracking rules for Hashcat based on statistics and industry patterns, including 'hob064' for quick cracking and 'd3adhob0' for extensive use. |
| [hydra](https://packages.debian.org/search?keywords=hydra) | Hydra is a fast network logon cracker designed to brute-force passwords on various protocols and services. |
| [john](https://packages.debian.org/search?keywords=john) | John the Ripper is a fast password cracker designed to recover passwords from various encrypted files. |
| [kwprocessor](https://github.com/hashcat/kwprocessor) | kwprocessor is an advanced keyboard-walk generator with configurable basechars, keymap, and routes, designed to mimic human-generated passwords for efficient password cracking. |
| [legba](https://crates.io/crates/legba) | legba is a fast multi-protocol credential bruteforcer/sprayer/enumerator for authentication. |
| [maskprocessor](https://packages.debian.org/search?keywords=maskprocessor) | maskprocessor is a high-performance word generator with a per-position configurable charset, suitable for generating potential passwords or keys. |
| [medusa](https://packages.debian.org/search?keywords=medusa) | Medusa is a fast, parallel, modular login brute-forcer for network services, targeting various protocols and platforms. |
| [name-that-hash](https://pypi.org/project/name-that-hash/) | name-that-hash identifies the type of cryptographic hash algorithm used for a given hash value, supporting multiple hash types and Python 3.6+. |
| [OneRuleToRuleThemStill](https://github.com/stealthsploit/OneRuleToRuleThemStill) | OneRuleToRuleThemStill is an optimized hashcat rule set with 6.9% fewer rules while maintaining performance, targeting Lifeboat and LastFM data breaches. |
| [ophcrack](https://packages.debian.org/search?keywords=ophcrack) | Ophcrack is a Microsoft Windows password cracker using rainbow tables, available as a graphical (ophcrack) and command-line (ophcrack-cli) version. |
| [Pantagrule](https://github.com/rarecoil/pantagrule) | Pantagrule is a series of hashcat rules generated from real-world compromised passwords, optimized for better performance and transparency. |
| [patator](https://pypi.org/project/patator/) | Patator is a multi-threaded Python brute-forcer supporting various protocols including FTP, SSH, SMTP, HTTP, and more. |
| [pdfcrack](https://packages.debian.org/search?keywords=pdfcrack) | pdfcrack is a command-line tool for cracking passwords on PDF files. |
| [pipal](https://github.com/digininja/pipal) | Pipal is a password analysis tool for cracked password dumps, providing statistics and information to help interpret results. It requires Ruby 1.9.x and works on any vanilla Ruby install. Usage includes options for showing top results, outputting to a file, and comparing against external word lists. |
| [princeprocessor](https://packages.debian.org/search?keywords=princeprocessor) | Standalone password candidate generator using the PRINCE algorithm for generating strong passwords. |
| [search-that-hash](https://pypi.org/project/search-that-hash/) | search-that-hash is a Python tool for searching hash values against various online databases to identify the original file or information. It is useful for cybersecurity professionals and forensic analysts to quickly determine the source of suspicious files. Target platform: Python. |
| [statsprocessor](https://packages.debian.org/search?keywords=statsprocessor) | statsprocessor is a word generator based on per-position Markov chains, suitable for various Linux distributions and architectures. |
| [sucrack](https://packages.debian.org/search?keywords=sucrack) | sucrack is a multithreaded su bruteforcer for Linux systems. |
| [trevorspray](https://pypi.org/project/trevorspray/) | trevorspray is a Python-based tool for conducting network reconnaissance and vulnerability scanning. |
| [username-anarchy](https://github.com/urbanadventurer/username-anarchy) | Username Anarchy is a command-line tool for generating usernames during penetration testing, supporting various formats and sources like social networks and country databases. |

## Crypto

| Tool | Description |
| :--- | :--- |
| [codext](https://pypi.org/project/codext/) | CodExt is a Python library that extends the native codecs library with over 150 new encodings and provides a CLI for encoding/decoding text and files. |
| [cribdrag](https://github.com/SpiderLabs/cribdrag) | cribdrag is a script for performing crib dragging attacks against ciphertext encrypted using an XOR operation with a predictable key, supporting One-Time Pad with reused key and other stream ciphers. |
| [factordb-python](https://pypi.org/project/factordb-python/) | factordb-python is a Python library and command-line tool to query the FactorDB, a database of known number factorizations. |
| [fastcoll](https://github.com/upbit/clone-fastcoll) | fastcoll is a tool for generating collision pairs for hash functions, primarily used in cryptographic analysis and security research. It targets Windows and is compatible with hash functions like SHA-1 and SHA-256. |
| [featherduster](https://github.com/nccgroup/featherduster) | FeatherDuster is a Python-based cryptanalysis tool for breaking weak cryptographic systems, designed to simplify the process of identifying and exploiting vulnerabilities in encrypted data. |
| [hash_extender](https://github.com/iagox86/hash_extender) | hash_extender is a tool for performing hash length extension attacks on various hashing algorithms including MD4, MD5, RIPEMD-160, SHA-0, SHA-1, SHA-256, SHA-512, and WHIRLPOOL. |
| [lascar](https://github.com/Ledger-Donjon/lascar) | Lascar is an open-source Python library for side-channel analysis, providing tools for trace acquisition, signal synchronization, and custom attacks. It is designed for both experienced and novice users and is compatible with mainstream Python libraries. |
| [pemcrack](https://github.com/robertdavidgraham/pemcrack) | pemcrack is a slow tool for brute-forcing or dictionary cracking of encrypted private keys in SSL PEM files. |
| [PkCrack](https://github.com/keyunluo/pkcrack) | PkCrack is a known-plaintext attack tool for breaking PkZip encryption, using an algorithm developed by Eli Biham and Paul Kocher. It requires a known plaintext file and the encrypted ZIP archive to decrypt the latter. |
| [RsaCtfTool](https://github.com/RsaCtfTool/RsaCtfTool) | RsaCtfTool is an RSA attack utility for recovering private keys from weak public keys and decrypting data, primarily for educational purposes. |
| [rsatool](https://github.com/ius/rsatool) | rsatool calculates RSA and RSA-CRT parameters from given primes or modulus/private exponent, outputting in OpenSSL-compatible formats. |
| [xortool](https://pypi.org/project/xortool/) | xortool is a Python tool for analyzing multi-byte XOR ciphers, guessing key lengths and keys based on character frequency, and supports both binary and text files. |
| [yafu](https://github.com/bbuhrow/yafu) | YAFU is an automated integer factorization tool using modern algorithms, suitable for academic and general factorization tasks. It supports Windows, Linux, and WSL, and can be built from source with specific CPU optimizations. |
| [z3-solver](https://pypi.org/project/z3-solver/) | Z3-solver is an efficient SMT solver library for bitvectors, booleans, arrays, and other data types, primarily used in formal verification and automated reasoning. |

## Enterprise

| Tool | Description |
| :--- | :--- |
| [abuseACL](https://github.com/AetherBlack/abuseACL) | abuseACL is a Python script to automatically list vulnerable Windows ACEs/ACLs using LDAP. |
| [aclpwn](https://pypi.org/project/aclpwn/) | aclpwn is a Python tool for auditing Access Control Lists (ACLs) in network devices, identifying misconfigurations and potential vulnerabilities. |
| [adidnsdump](https://pypi.org/project/adidnsdump/) | adidnsdump is a Python tool for dumping DNS records from ADI (Active Directory Integrated) DNS servers, useful for network forensic analysis and penetration testing. |
| [asrepcatcher](https://github.com/Yaxxine7/ASRepCatcher) | ASRepCatcher uses ARP spoofing to intercept AS-REP Kerberos messages from domain clients, extracting hashes for offline cracking. Targets all users on the same VLAN, regardless of Kerberos pre-authentication settings. Supports relay and listen modes. |
| [autobloody](https://pypi.org/project/autobloody/) | autobloody is a Python script for automating the process of sending HTTP requests to test web applications for vulnerabilities. |
| [azurehound](https://github.com/BloodHoundAD/AzureHound) | AzureHound is a tool for collecting Azure data to feed into BloodHound for network visualization and analysis. |
| [bloodhound](https://pypi.org/project/bloodhound/) | Bloodhound is a network visualization and analysis tool for Active Directory environments, mapping user and group relationships for security analysis. |
| [bloodhound-ce](https://hub.docker.com/r/specterops/bloodhound) | BloodHound-ce is an open-source tool for visualizing and analyzing Active Directory and Azure environment relationships, using graph theory to identify attack paths and privilege relationships. |
| [bloodyad](https://pypi.org/project/bloodyad/) | bloodyad is a Python library for automating Active Directory attacks, primarily used for security testing and penetration. It targets Windows environments and supports LDAP protocol. |
| [bqm](https://github.com/Acceis/bqm) | BQM (Bloodhound Query Merger) deduplicates and merges custom BloodHound queries from different datasets into a single customqueries.json file. |
| [certipy-ad](https://pypi.org/project/certipy-ad/) | Certipy-AD is a toolkit for enumerating and abusing Active Directory Certificate Services, supporting various attack paths and misconfigurations. |
| [certsync](https://pypi.org/project/certsync/) | certsync synchronizes SSL/TLS certificates across multiple servers. |
| [cmloot](https://github.com/shelltrail/cmloot) | cmloot.py is a Python script for enumerating Configuration Manager servers, creating inventories, and downloading files from SCCM servers using credentials or pass-the-hash. |
| [coercer](https://pypi.org/project/coercer/) | Coercer is a Python library for manipulating HTTP requests and responses, primarily used for testing and debugging web applications. It targets HTTP/1.1 and is compatible with Python 3.6+. |
| [conpass](https://github.com/login-securite/conpass) | Continuous password spraying tool for Active Directory, targeting domain policies and avoiding lockouts. |
| [cyperoth](https://github.com/seajaysec/cypheroth) | Cypheroth is a bash script that automates running Cypher queries against Bloodhound's Neo4j backend and saves output to spreadsheets. It is primarily used by cybersecurity professionals for active directory assessments on Linux, macOS, and Windows. |
| [dfscoerce](https://github.com/Wh04m1001/dfscoerce) | DFSCoerce is a proof-of-concept tool for exploiting MS-DFSNM coerce authentication using NetrDfsRemoveStdRoot and NetrDfsAddStdRoot methods, targeting Windows environments. |
| [dploot](https://pypi.org/project/dploot/) | dploot is a Python tool for extracting local administrator passwords from Windows systems using the Windows Management Instrumentation (WMI) interface. |
| [enum4linux-ng](https://github.com/cddmp/enum4linux-ng) | enum4linux-ng is a Python-based tool for enumerating information from Windows and Samba systems, supporting YAML and JSON export, and multiple authentication methods. |
| [evil-winrm](https://rubygems.org/gems/evil-winrm) | evil-winrm is a Ruby-based WinRM shell for hacking and penetration testing, targeting Windows platforms. |
| [ExtractBitlockerKeys](https://github.com/p0dalirius/ExtractBitlockerKeys) | ExtractBitlockerKeys is a Python and PowerShell script for extracting BitLocker recovery keys from a domain using LDAP. It supports multithreading and exports results in JSON, XLSX, and SQLite formats. |
| [freeipscanner](https://github.com/scrt/freeipscanner) | freeipscanner is a bash script that identifies stale ADIDNS entries on a local subnet by comparing DNS names with IP addresses that do not respond to arping requests. It is useful for network administrators to clean up unused DNS records. Target platform: Linux. Protocol: ARP, DNS. |
| [gmsadumper](https://github.com/micahvandeusen/gMSADumper) | gMSADumper reads and parses gMSA password blobs if accessible, supporting basic, pass-the-hash, and Kerberos authentication. |
| [godap](https://github.com/Macmod/godap) | godap is a terminal user interface (TUI) for LDAP, supporting authentication, object exploration, and management in AD environments. |
| [GoExec](https://github.com/FalconOpsLLC/goexec) | GoExec is a Windows remote execution multitool using various methods like DCOM, WMI, SCMR, and TSCH for lateral movement and remote access. |
| [goldencopy](https://github.com/Dramelac/GoldenCopy) | GoldenCopy copies user properties and groups from Neo4j (Bloodhound) to create identical golden tickets for mimikatz or ticketer. |
| [GoMapEnum](https://github.com/nodauf/GoMapEnum) | GoMapEnum is a tool for user enumeration and password bruteforce on Azure, ADFS, OWA, O365, Teams, and LinkedIn. |
| [gosecretsdump](https://github.com/c-sto/gosecretsdump) | gosecretsdump is a fast NTDS.dit file parser and secrets dumper for Windows environments, using Go language for improved performance compared to Impacket's secretsdump.py. |
| [GPOddity](https://github.com/synacktiv/GPOddity) | GPOddity automates GPO attack vectors through NTLM relaying, targeting vulnerable Group Policy Objects. |
| [hekatomb](https://pypi.org/project/hekatomb/) | Hekatomb is a Python library for network traffic analysis and manipulation, primarily used for cybersecurity research and testing. |
| [impacket](https://pypi.org/project/impacket/) | Impacket is a Python library for working with network protocols, providing low-level access to packets and protocol implementations. It supports protocols like SMB, MSRPC, and TDS, and can be used for network analysis and security testing. |
| [kerbrute](https://github.com/ropnop/kerbrute) | Kerbrute is a tool for performing Kerberos pre-authentication bruteforcing to enumerate valid Active Directory accounts. |
| [keytabextract](https://github.com/sosdave/KeyTabExtract) | KeyTabExtract is a utility to extract information from .keytab files, useful for Linux Kerberos authentication. It outputs realm, service principal, encryption type, and NTLM hash. |
| [krbjack](https://pypi.org/project/krbjack/) | krbjack is a Kerberos AP-REQ hijacking tool that exploits DNS zone updates to perform man-in-the-middle attacks, targeting Active Directory environments with the ZONE_UPDATE_UNSECURE flag enabled. |
| [krbrelayx](https://github.com/dirkjanm/krbrelayx) | Krbrelayx is a toolkit for abusing Kerberos, enabling Kerberos relaying and exploiting unconstrained delegation. |
| [ldapdomaindump](https://pypi.org/project/ldapdomaindump/) | ldapdomaindump is a Python tool for extracting information from Active Directory via LDAP, suitable for security assessments and penetration testing. |
| [ldapnomnom](https://github.com/lkarlslund/ldapnomnom) | ldapnomnom is a tool for anonymously bruteforcing Active Directory usernames using cLDAP requests on Domain Controllers. |
| [ldaprelayscan](https://github.com/zyn3rgy/LdapRelayScan) | ldaprelayscan checks for LDAP protections regarding NTLM authentication relay on Domain Controllers, supporting LDAPS and LDAP protocols. |
| [ldapsearchad](https://pypi.org/project/ldapsearchad/) | ldapsearchad is a Python library for searching Active Directory using LDAP. |
| [LDAPWordlistHarvester](https://github.com/p0dalirius/pyLDAPWordlistHarvester) | LDAPWordlistHarvester is a Python tool to generate a wordlist from LDAP information for cracking domain passwords. |
| [ldeep](https://pypi.org/project/ldeep/) | ldeep is a network scanner for identifying open ports and services on a target host. |
| [linWinPwn](https://github.com/lefayjey/linWinPwn) | linWinPwn is a bash script for Active Directory penetration testing, offering enumeration, exploitation, and password dumping functionalities using various tools like Impacket, BloodHound, and Kerbrute. |
| [lnkup](https://github.com/Plazmaz/lnkUp) | lnkup generates malicious LNK file payloads for data exfiltration, targeting Windows. |
| [lsassy](https://pypi.org/project/lsassy/) | lsassy is a Python script for extracting user credentials from Active Directory using the LDAP protocol. |
| [manspider](https://pypi.org/project/manspider/) | manspider is a Python library for web scraping and data extraction, primarily used for cybersecurity research and analysis. |
| [masky](https://pypi.org/project/masky/) | Masky is a Python library and CLI tool for remotely dumping domain user credentials using legitimate Windows and Active Directory features, targeting ADCS. |
| [mitm6](https://pypi.org/project/mitm6/) | mitm6 is a tool for IPv4 over IPv6 Man-in-the-Middle attacks, primarily used for security testing and analysis. |
| [netexec](https://github.com/Pennyw0rth/NetExec) | NetExec is an open-source network execution tool for Windows, Linux, and macOS, designed for penetration testing and security assessments. It supports various protocols and features for active directory enumeration and exploitation. |
| [noPac](https://github.com/Ridter/noPac) | noPac exploits CVE-2021-42278 and CVE-2021-42287 to impersonate a Domain Administrator from a standard domain user, targeting Windows domain environments. |
| [ntlm_theft](https://github.com/Greenwolf/ntlm_theft) | ntlm_theft generates NTLMv2 hash theft files for phishing attacks targeting SMB and internal networks. |
| [ntlmv1-multi](https://github.com/evilmog/ntlmv1-multi) | ntlmv1-multi formats NTLMv1 challenge responses for hashcat mode 14000, supporting NTLMv1, NTLMv1-ESS, and MSCHAPv2 hashes. |
| [PassTheCert](https://github.com/AlmondOffSec/PassTheCert) | PassTheCert is a proof-of-concept tool that allows authenticating to an LDAP/S server with a certificate through Schannel, enabling authentication when PKINIT is not supported. |
| [PCredz](https://github.com/lgandx/PCredz) | PCredz extracts credentials and sensitive information from pcap files or live network traffic, targeting protocols like HTTP, SMTP, FTP, and SNMP. |
| [petitpotam](https://github.com/topotam/PetitPotam) | PetitPotam is a proof-of-concept tool to exploit MS-EFSRPC for authentication coercion on Windows hosts. |
| [pkinittools](https://github.com/dirkjanm/PKINITtools) | pkinittools: A set of Python scripts for Kerberos PKINIT and relaying to AD CS, enabling TGT requests and NT hash extraction. |
| [powerview](https://pypi.org/project/powerview/) | PowerView.py is a Python script for querying and manipulating Active Directory using LDAP, LDAPS, or GC protocols. |
| [pretender](https://github.com/RedTeamPentesting/pretender) | pretender is a Go-based tool for conducting DHCPv6 DNS takeover and mDNS, LLMNR, and NetBIOS-NS spoofing attacks, primarily targeting Windows hosts. |
| [privexchange](https://github.com/dirkjanm/PrivExchange) | PrivExchange is a proof-of-concept tool for exploiting Exchange Web Services to escalate privileges to Domain Admin. |
| [PXEThief](https://github.com/blurbdust/PXEThief) | PXEThief is a Python tool for extracting passwords from Microsoft Endpoint Configuration Manager (ConfigMgr) during PXE boot, targeting Network Access Accounts and Task Sequence credentials. |
| [pypykatz](https://pypi.org/project/pypykatz/) | pypykatz is a Python implementation of Mimikatz, used for extracting credentials from memory on Windows systems. |
| [pysnaffler](https://pypi.org/project/pysnaffler/) | pysnaffler is a Python-based network packet sniffer for capturing and analyzing network traffic. |
| [pywerview](https://pypi.org/project/pywerview/) | pywerview is a Python script for gathering information from a Windows domain, primarily used for reconnaissance and forensic analysis. |
| [pywhisker](https://pypi.org/project/pywhisker/) | pywhisker is an unofficial Python tool for manipulating the msDS-KeyCredentialLink attribute of target users/computers to obtain full control, supporting various authentication methods and operating on UNIX-based systems. |
| [pywsus](https://github.com/GoSecure/pywsus) | pywsus is a Python tool for implementing a malicious WSUS server, enabling MITM attacks on Windows Update clients. It targets Windows platforms using HTTP for WSUS and UpdateServiceUrlAlternate. |
| [RemoteMonologue](https://github.com/3lp4tr0n/RemoteMonologue) | RemoteMonologue is a Windows credential harvesting tool that leverages DCOM for NTLM authentication coercion, enabling remote user compromise and credential spraying. |
| [Responder](https://github.com/lgandx/Responder) | Responder is a network security tool that captures credentials by poisoning LLMNR, NBT-NS, and MDNS requests, supporting protocols like HTTP, SMB, MSSQL, FTP, LDAP, and Kerberos. |
| [roadtx](https://pypi.org/project/roadtx/) | roadtx is a Python library for exchanging ROADtools tokens, primarily used in cybersecurity for authentication and authorization processes. |
| [roastinthemiddle](https://github.com/Tw1sm/RITM) | RITM is a Python tool for performing ARP spoofing and Kerberoasting attacks, targeting Windows environments. |
| [ruler](https://github.com/sensepost/ruler) | Ruler is a tool for remote Exchange server abuse, supporting MAPI/HTTP and RPC/HTTP protocols, enabling user enumeration, rule creation, GAL dump, and VBScript execution through Outlook features. |
| [rusthound](https://github.com/NH-RED-TEAM/RustHound) | RustHound is a cross-platform BloodHound collector tool written in Rust, compatible with Linux, Windows, and macOS. It generates JSON files for analyzing with BloodHound. |
| [rusthound-ce](https://github.com/g0h4n/RustHound-CE) | RustHound-CE is a cross-platform BloodHound collector tool written in Rust, compatible with Linux, Windows, and macOS, using LDAP(S) or ADWS for Active Directory data ingestion. |
| [sccmsecrets](https://github.com/synacktiv/SCCMSecrets) | SCCMSecrets.py is an SCCM policies exploitation tool for credentials harvesting, initial access, and lateral movement. |
| [sccmwtf](https://github.com/xpn/sccmwtf) | SCCMwtf is a proof-of-concept tool for exploring SCCM in a lab environment, designed for cybersecurity research and analysis. |
| [shadowcoerce](https://github.com/ShutdownRepo/shadowcoerce) | ShadowCoerce is a proof-of-concept tool for abusing MS-FSRVP to coerce authentication on a target server, requiring the 'File Server VSS Agent Service' to be enabled. |
| [smbclientng](https://pypi.org/project/smbclientng/) | smbclientng is a Python library for accessing SMB/CIFS file shares, enabling file operations over the network. |
| [sprayhound](https://pypi.org/project/sprayhound/) | Sprayhound is a Python library for automating HTTP requests and analyzing responses, primarily used for web application security testing. |
| [spraykatz](https://github.com/aas-n/spraykatz) | Spraykatz is a credentials gathering tool for Windows machines and large Active Directory environments, automating remote procdump and parsing of lsass process. |
| [targetedKerberoast](https://github.com/ShutdownRepo/targetedKerberoast) | targetedKerberoast is a Python script for performing targeted Kerberoasting attacks, attempting to set and abuse SPNs on user accounts to extract Kerberos hashes. |
| [windapsearch](https://github.com/ropnop/go-windapsearch) | windapsearch is a tool for enumerating users, groups, and computers in a Windows domain through LDAP queries. It supports anonymous and authenticated binds, and can output results in JSON format. Target platform: Windows, Linux, Mac. Protocol: LDAP. |
| [zerologon](https://github.com/SecuraBV/CVE-2020-1472) | Zerologon is a Python script using Impacket to test for the Zerologon exploit (CVE-2020-1472), targeting domain controllers for Netlogon authentication bypass. |

## Forensics

| Tool | Description |
| :--- | :--- |
| [autopsy](https://packages.debian.org/search?keywords=autopsy) | Autopsy is a graphical interface to SleuthKit, a suite of command-line tools for forensic analysis of digital evidence. |
| [bulk-extractor](https://packages.debian.org/search?keywords=bulk-extractor) | bulk-extractor is a forensic tool for extracting files from digital media. |
| [chainsaw](https://github.com/WithSecureLabs/chainsaw) | Chainsaw is a fast Windows forensic tool for searching event logs, using Sigma rules, and extracting artefacts. It runs on MacOS, Linux, and Windows. |
| [ctf-usb-keyboard-parser](https://github.com/TeamRocketIst/ctf-usb-keyboard-parser) | A Python script for parsing USB keyboard data from PCAP files or Bluetooth snooping logs, converting raw byte sequences into readable keystrokes. |
| [dc3dd](https://packages.debian.org/search?keywords=dc3dd) | dc3dd is a forensic version of GNU dd, designed for data acquisition and analysis, supporting various platforms and protocols. |
| [dcfldd](https://packages.debian.org/search?keywords=dcfldd) | dcfldd is an enhanced version of dd for forensic and security purposes, supporting various platforms and protocols. |
| [Depix](https://github.com/spipm/Depix) | Depix is a tool for depixelizing images, primarily used for privacy and security purposes. It targets web applications and protocols. |
| [dislocker](https://packages.debian.org/search?keywords=dislocker) | dislocker is a command-line tool for reading and writing BitLocker-encrypted volumes on Linux. |
| [dissect.target](https://pypi.org/project/dissect.target/) | dissect.target is a Python library for forensic analysis of disk images and memory dumps, supporting Windows, Linux, and macOS. |
| [dvcs-ripper](https://github.com/kost/dvcs-ripper) | dvcs-ripper is a Perl script for downloading and cloning web-accessible version control repositories (SVN, GIT, HG, BZR, etc.) even when directory browsing is disabled. |
| [elf-pe-viewer-vscode](https://github.com/theluckystrike/elf-pe-viewer-vscode) | Browser-based ELF viewer and PE viewer for VS Code: headers, sections, imports, exports, symbols and a hex view for ELF, PE (EXE, DLL) and Mach-O files. |
| [ewf-tools](https://packages.debian.org/search?keywords=ewf-tools) | EWF-tools is a collection of utilities for handling EWF (Expert Witness Format) files, commonly used in digital forensics and incident response. |
| [ext3grep](https://packages.debian.org/search?keywords=ext3grep) | ext3grep is a tool to recover deleted files on ext3 filesystems. |
| [ext4magic](https://packages.debian.org/search?keywords=ext4magic) | ext4magic is a utility for recovering deleted files from ext3 or ext4 partitions on Linux systems. |
| [extundelete](https://packages.debian.org/search?keywords=extundelete) | Extundelete is a utility to recover deleted files from ext3/ext4 partitions. |
| [ffmpeg](https://github.com/FFmpeg/FFmpeg) | FFmpeg is a multimedia framework that can record, convert, and stream audio and video. It includes libraries and tools for decoding, encoding, filtering, and streaming. Primary use case is for multimedia processing and streaming. Target platforms include Linux, macOS, and Windows. Supports various codecs and protocols. |
| [firefox_decrypt](https://github.com/unode/firefox_decrypt) | Firefox Decrypt extracts passwords from Mozilla Firefox, Waterfox, Thunderbird, and SeaMonkey profiles using the known master password. |
| [firmware-mod-kit](https://github.com/rampageX/firmware-mod-kit) | Firmware Mod Kit is a collection of scripts and utilities to extract and rebuild Linux-based firmware images, primarily for embedded devices like routers. It allows users to modify the firmware's file system or web UI and then rebuild and flash the modified firmware onto the device, though this can potentially brick the device if not used carefully. |
| [foremost](https://packages.debian.org/search?keywords=foremost) | Foremost is a forensic tool for recovering lost files from digital media. |
| [forensics-extra](https://packages.debian.org/search?keywords=forensics-extra) | A metapackage for additional console and GUI components in a forensics environment. |
| [galleta](https://packages.debian.org/search?keywords=galleta) | galleta is an Internet Explorer cookie forensic analysis tool for Linux. |
| [gtkwave](https://github.com/gtkwave/gtkwave) | GTKWave is a GTK+ based wave viewer for Unix and Win32, supporting LXT, LXT2, VZT, FST, and GHW files, as well as standard Verilog VCD/EVCD files. |
| [guymager](https://packages.debian.org/search?keywords=guymager) | Forensic imaging tool based on Qt for creating disk images for forensic analysis. |
| [hachoir](https://pypi.org/project/hachoir/) | Hachoir is a Python library for parsing and viewing binary files, allowing users to explore and manipulate file structures. |
| [hashdeep](https://packages.debian.org/search?keywords=hashdeep) | hashdeep recursively computes hashsums or piecewise hashings for files and directories. |
| [hex-viewer-online](https://github.com/theluckystrike/hex-viewer-vscode) | Browser-based hex viewer that displays any file as hex and text without uploading the file, including a data inspector, find, and structure view for multiple formats. |
| [hexyl](https://packages.debian.org/search?keywords=hexyl) | Command-line hex viewer with colored output for analyzing binary data. |
| [imhex](https://github.com/WerWolv/ImHex) | A multi-platform hex editor for reverse engineering, programming, and cybersecurity tasks. |
| [libimage-exiftool-perl](https://packages.debian.org/search?keywords=libimage-exiftool-perl) | libimage-exiftool-perl is a Perl library and program to read and write metadata in multimedia files. |
| [mac-robber](https://packages.debian.org/search?keywords=mac-robber) | mac-robber collects data about allocated files in mounted filesystems, primarily for forensic analysis and system auditing. |
| [magicrescue](https://packages.debian.org/search?keywords=magicrescue) | magicrescue: recover files by looking for magic bytes, primarily for data recovery on various Linux distributions. |
| [memdump](https://packages.debian.org/search?keywords=memdump) | memdump is a utility to dump memory contents to standard output, primarily used for debugging and forensic analysis on various Linux architectures. |
| [memprocfs](https://github.com/ufrisk/MemProcFS) | MemProcFS allows viewing physical memory as files in a virtual file system, enabling easy memory analysis for live memory, memory dump files, and remote live memory incident response. |
| [mvt](https://pypi.org/project/mvt/) | MVT is a forensic toolkit for Android and iOS devices, collecting traces to identify potential compromises. It supports public IOCs for spyware detection and requires digital forensics knowledge. Target platform: Android/iOS. Usage: mvt-ios, mvt-android commands for analysis. Installation via pip or uv. |
| [oletools](https://pypi.org/project/oletools/) | oletools is a Python library for analyzing Microsoft Office files, primarily used for forensic analysis and security research. |
| [pasco](https://packages.debian.org/search?keywords=pasco) | pasco is an Internet Explorer cache forensic analysis tool for Debian-based systems. |
| [peepdf-3](https://pypi.org/project/peepdf-3/) | peepdf-3 is a Python library for parsing and analyzing PDF files, useful for cybersecurity professionals and researchers. |
| [plaso](https://pypi.org/project/plaso/) | plaso is a Python library for processing and analyzing digital forensic artifacts, primarily used for log file analysis and incident response. |
| [poppler-utils](https://packages.debian.org/search?keywords=poppler-utils) | poppler-utils: PDF utilities based on Poppler for extracting text, images, and metadata from PDF files. |
| [pulseview](https://github.com/sigrokproject/pulseview) | PulseView is a free, open-source logic analyzer software for the Sigrok project, designed to capture and analyze digital waveforms from logic analyzers. |
| [python-evtx](https://pypi.org/project/python-evtx/) | python-evtx is a pure Python parser for Windows event log files (.evtx), enabling programmatic access to event records on various platforms. |
| [recoverjpeg](https://packages.debian.org/search?keywords=recoverjpeg) | recoverjpeg is a command-line tool for recovering corrupted JPEG and MOV files on Linux systems. |
| [RegRipper](https://github.com/keydet89/RegRipper3.0) | RegRipper3.0 is a forensic tool for extracting information from Windows Registry hives, supporting both GUI and command-line interfaces for various plugins. |
| [rifiuti2](https://packages.debian.org/search?keywords=rifiuti2) | rifiuti2 is a tool for analyzing Microsoft Windows Recycle Bin files, serving as a replacement for rifiuti. |
| [samdump2](https://packages.debian.org/search?keywords=samdump2) | samdump2 is a tool for extracting Windows 2k/NT/XP password hashes from memory dumps. |
| [scalpel](https://packages.debian.org/search?keywords=scalpel) | Scalpel is a fast, filesystem-independent file recovery tool for Linux. |
| [scrounge-ntfs](https://packages.debian.org/search?keywords=scrounge-ntfs) | scrounge-ntfs is a data recovery program for NTFS filesystems, suitable for Linux. |
| [sigrok-cli](https://github.com/sigrokproject/sigrok-cli) | sigrok-cli is a command-line interface for the sigrok open-source hardware logic analyzer framework, enabling users to capture and analyze digital signals from hardware devices. |
| [sleuthkit](https://packages.debian.org/search?keywords=sleuthkit) | Sleuthkit is a set of command-line tools for forensic analysis of volume and filesystem data, supporting multiple platforms and file systems. |
| [ssdeep](https://packages.debian.org/search?keywords=ssdeep) | ssdeep is a recursive piecewise hashing tool used for comparing files and detecting similarities. |
| [testdisk](https://packages.debian.org/search?keywords=testdisk) | TestDisk is a free, open-source partition recovery and disk repair tool for Linux and other Unix-like operating systems. |
| [unblob](https://pypi.org/project/unblob/) | unblob extracts files from various binary container formats, supporting 78+ types including SquashFS, JFFS2, UBI/UBIFS, ext, CPIO, ZIP, and more. It recursively processes nested containers, identifies unknown chunks, and generates detailed JSON reports. Runs as a regular user and is compatible with Linux. |
| [unhide](https://packages.debian.org/search?keywords=unhide) | unhide is a forensic tool to find hidden processes and ports on Linux systems. |
| [USB-HID-decoders](https://github.com/Nissen96/USB-HID-decoders) | USB-HID-decoders is a tool for extracting and decoding raw HID data from PCAP files, including keyboard, mouse, and tablet inputs. It supports PCAP extraction, keyboard and mouse decoding, and visualization of tablet pen strokes. |
| [usbrip](https://pypi.org/project/usbrip/) | usbrip is a command-line tool for tracking USB device usage on a Windows system, useful for forensic analysis and security auditing. |
| [vcdvcd](https://github.com/cirosantilli/vcdvcd) | vcdvcd is a Python library for parsing Verilog value change dumps (VCD) and a command-line tool for pretty-printing VCD files. |
| [vinetto](https://packages.debian.org/search?keywords=vinetto) | Vinetto is a forensics tool to examine Thumbs.db files. |
| [volatility3](https://pypi.org/project/volatility3/) | Volatility3 is a memory forensic framework for analyzing Windows memory dumps. |
| [zbar-tools](https://packages.debian.org/search?keywords=zbar-tools) | zbar-tools: QR code/bar code scanner and decoder utilities for Linux. |

## Llm

| Tool | Description |
| :--- | :--- |
| [AgentDojo](https://github.com/ethz-spylab/agentdojo) | AgentDojo is a dynamic environment for evaluating prompt injection attacks and defenses for large language model agents. |
| [Agentic-Bug-Hunter](https://github.com/Awarexone/Agentic-Bug-Hunter) | AI-powered bug bounty hunting toolkit for ethical hacking and vulnerability discovery. |
| [AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard) | AI-Infra-Guard is a full-stack AI red teaming platform by Tencent Zhuque Lab, offering comprehensive security checks for AI infrastructure, including agent, AI tool, skill, and LLM scans, to identify and mitigate risks. |
| [AISecLists](https://github.com/SecNode/AISecLists) | AISecLists is a curated collection of prompt lists for diverse AI security assessments, including LLM jailbreaks, prompt injection, and information disclosure. |
| [Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | Anthropic-Cybersecurity-Skills is an open-source library of 817 cybersecurity skills mapped to 6 frameworks, compatible with 26+ AI platforms, and covering 34 security domains for authorized penetration testing and security research. |
| [bolt](https://github.com/CyberStrikeus/bolt) | Bolt is a plugin-based security tool server that allows for the execution of various penetration testing tools via MCP (Multi-Process Communication). It supports both native TypeScript plugins and external MCP servers, providing a unified interface for security assessments. |
| [bountyforge](https://github.com/Gabson0x/bountyforge) | BountyForge is an AI-driven bug bounty tool that automates parallelized security assessments for web/APIs, smart contracts, and infrastructure, generating submission-ready reports for various platforms. |
| [cai-framework](https://github.com/aliasrobotics/cai) | CAI Framework: The archived open-source cybersecurity AI research project, now succeeded by Cybersecurity Superintelligence. |
| [cain-agent](https://github.com/cdxiaodong/cain-agent) | Cain-agent is an AI penetration testing tool for real-world authorized assessments, focusing on business-logic flaws, auth chains, and cloud misconfigurations. It supports multiple cloud platforms including AWS, Azure, GCP, and Chinese clouds, and is built on the Claude Agent SDK. |
| [cisco-ai-mcp-scanner](https://pypi.org/project/cisco-ai-mcp-scanner/) | A Python tool for scanning MCP servers and tools for potential security findings using YARA rules, LLM-based analysis, and Cisco AI Defense inspect API. |
| [cisco-ai-skill-scanner](https://pypi.org/project/cisco-ai-skill-scanner/) | cisco-ai-skill-scanner is a Python tool for scanning Cisco AI skills, primarily used for security assessments on Cisco devices. |
| [Claude-Red](https://github.com/SnailSploit/Claude-Red) | Claude-Red is a library of offensive security skills for the Claude Skills system, providing expert-level methodology for various attack surfaces. |
| [Decepticon](https://github.com/PurpleAILAB/Decepticon) | Decepticon is an autonomous red team agent for cybersecurity testing, primarily used for penetration testing and vulnerability assessment. It runs nmap and generates reports. Target platform/protocol: Network and system security. |
| [domaintools-mcp](https://api.domaintools.com/v1/mcp) | The domaintools-mcp tool connects AI agents to DomainTools' comprehensive DNS datasets, enabling security teams to perform complex domain investigations and infrastructure mapping through natural language. |
| [DorkAgent](https://github.com/yee-yore/DorkAgent) | DorkAgent is an LLM-powered agent for automated Google Dorking in bug hunting and pentesting, supporting Serper and SerpApi search engines and various LLM providers. |
| [exploitdb-mcp-server](https://github.com/Cyreslab-AI/exploitdb-mcp-server) | ExploitDB MCP Server provides access to Exploit-DB functionality via Model Context Protocol, enabling AI assistants to search, retrieve, and analyze security exploits and vulnerabilities. |
| [fofa-mcp-server](https://github.com/help116114/fofa-mcp-server) | A Model Context Protocol (MCP) server enabling AI assistants to query FoFa's database for internet-connected devices and services using search capabilities and user information retrieval. |
| [FuzzyAI](https://github.com/cyberark/FuzzyAI) | FuzzyAI is a tool for automated LLM fuzzing to identify and mitigate potential jailbreaks in LLM APIs. |
| [garak](https://pypi.org/project/garak/) | garak is an LLM vulnerability scanner that probes for weaknesses like hallucination, data leakage, and toxicity generation across various models including Hugging Face, OpenAI, and AWS. |
| [giskard](https://pypi.org/project/giskard/) | Giskard is an open-source Python library for testing and evaluating agentic systems, including LLMs and black-box agents, using modular, lightweight, and dynamic packages. |
| [greynoise-mcp-server](https://github.com/GreyNoise-Intelligence/greynoise-mcp-server) | greynoise-mcp-server is an MCP server for the GreyNoise API, providing access to threat intelligence and operational tools for IP context, GNQL search, and more. |
| [hackingBuddyGPT](https://github.com/ipa-lab/hackingBuddyGPT) | hackingBuddyGPT is an open-source framework for building LLM-driven security-testing agents, providing essential groundwork for ethical hackers to express new experiments in a few dozen lines of code. |
| [hexstrike-ai](https://github.com/0x4m4/hexstrike-ai) | HexStrike AI MCP Agents is an advanced MCP server that lets AI agents (Claude, GPT, Copilot, etc.) autonomously run 150+ cybersecurity tools for automated pentesting, vulnerability discovery, bug bounty automation, and security research. It supports multiple AI agents and integrates with various security tools. |
| [L1B3RT4S](https://github.com/elder-plinius/L1B3RT4S) | Jailbreak prompts for all flagship llms |
| [leakix-mcp](https://github.com/LeakIX/leakix-mcp) | MCP server for the LeakIX API, enabling security research and reconnaissance through various tools and queries. |
| [llm-guard](https://pypi.org/project/llm-guard/) | LLM-Guard sanitizes, detects harmful language, prevents data leakage, and resists prompt injection attacks to secure interactions with Large Language Models. |
| [mcp-pulsedive](https://github.com/pipeworx-io/mcp-pulsedive) | mcp-pulsedive is an unofficial integration for the Pipeworx MCP gateway, providing threat intelligence IOC enrichment through Pulsedive. |
| [mcp-security-hub](https://github.com/FuzzingLabs/mcp-security-hub) | mcp-security-hub is a GitHub repository for cybersecurity tools, primarily used for code, projects, and people in the security community. |
| [mcp-shodan](https://github.com/w0h1v/mcp-shodan) | mcp-shodan is an MCP server for Shodan, providing AI agents with network intelligence, DNS, and vulnerability intelligence over the Model Context Protocol. |
| [mcp-virustotal](https://github.com/w0h1v/mcp-virustotal) | mcp-virustotal is an MCP server for VirusTotal API, providing comprehensive security reports, relationship analysis, and pagination support for URLs, files, IPs, and domains. |
| [mcp_zoomeye](https://github.com/zoomeye-ai/mcp_zoomeye) | A Model Context Protocol server that provides network asset information based on query conditions, supporting ZoomEye dorks and other search parameters. |
| [MetasploitMCP](https://github.com/GH05TCREW/MetasploitMCP) | MetasploitMCP is an MCP server for Metasploit Framework integration, enabling AI assistants to dynamically access and control Metasploit functionality through standardized tools. |
| [nebula](https://github.com/BerylliumSec/nebula-apt) | Nebula is a secret-free APT repository for Nebula Linux releases, providing both stable and prerelease versions for Debian-based systems. |
| [nemoguardrails](https://pypi.org/project/nemoguardrails/) | NeMo Guardrails is an open-source toolkit for adding programmable guardrails to LLM-based conversational systems, enabling control over model output and enhancing security and trustworthiness. |
| [open-interpreter](https://pypi.org/project/open-interpreter/) | Open Interpreter allows language models to run code locally, providing a natural-language interface for various tasks like data analysis, web browsing, and more. It supports Python, JavaScript, Shell, and other languages. |
| [osint-mcp-server](https://github.com/badchars/osint-mcp-server) | osint-mcp-server is an AI-driven OSINT MCP server that consolidates 37 tools and 12 data sources (Shodan, VirusTotal, Censys, etc.) for automated, full-spectrum intelligence gathering and attack surface mapping. |
| [pallms](https://github.com/mik0w/pallms) | PALLMs is a collection of attack payloads for large language models, primarily used for educational purposes to understand and mitigate vulnerabilities. It targets LLMs and includes prompt injection and unbounded consumption examples. |
| [pentagi](https://github.com/vxcontrol/pentagi) | PentAGI is an autonomous AI system for performing complex penetration testing tasks. |
| [pentagi-docker](https://github.com/vxcontrol/pentagi) | PentAGI is an autonomous AI system for performing complex penetration testing tasks using Docker. |
| [PentestGPT](https://github.com/GreyDGL/PentestGPT) | PentestGPT is an AI-powered autonomous penetration testing agent using large language models for automated CTF and pentest tasks. |
| [PortSwigger-mcp-server](https://github.com/PortSwigger/mcp-server) | PortSwigger-mcp-server is an extension for Burp Suite that integrates with AI clients using the Model Context Protocol (MCP), supporting both Streamable HTTP and legacy SSE transports. |
| [promptfoo](https://github.com/promptfoo/promptfoo) | promptfoo is a CLI and library for evaluating and red-teaming LLM-based apps, supporting automated evaluations, model comparisons, and CI/CD integration. |
| [publicwww-mcp](https://github.com/publicwww-com/publicwww-mcp) | publicwww-mcp is an MCP server for searching source code from AI assistants like Claude, ChatGPT, and Cursor. It allows users to find and extract information from web pages, such as scripts, libraries, and tracking IDs, and save them as clusters. It supports various clients including web, desktop, and command-line tools. |
| [PurpleLlama](https://github.com/meta-llama/PurpleLlama) | PurpleLlama is an open-source project for evaluating and improving the cybersecurity of large language models, including tools for attack and defense postures. |
| [pyrit](https://pypi.org/project/pyrit/) | PyRIT is an open-source toolkit for assessing the security and safety weaknesses in generative AI systems through automated scans and human-led testing. It supports various AI models and protocols. |
| [raptor](https://github.com/gadievron/raptor) | Raptor is an autonomous security research framework that chains together static analysis, binary analysis, LLM-powered vulnerability validation, exploit generation, and patch writing into a single workflow for codebases and binaries. |
| [searchcode-mcp](https://api.searchcode.com/v1/mcp) | searchcode-mcp is a network analysis and scanning tool that integrates with the Model Context Protocol (MCP) for AI-assisted security tasks, enabling cybersecurity professionals to perform vulnerability scanning and static code analysis through natural language interfaces. |
| [shannon](https://github.com/KeygraphHQ/shannon) | Shannon is an AI-powered web application and API pentester that analyzes source code, identifies attack vectors, and executes real exploits to prove vulnerabilities before they reach production. It is designed for use in cybersecurity and DevSecOps environments. |
| [SkillSpector](https://github.com/NVIDIA/SkillSpector) | SkillSpector is a security scanner for AI agent skills, detecting vulnerabilities, malicious patterns, and security risks before installation. |
| [trailofbits-skills](https://github.com/trailofbits/skills) | Trail of Bits skills for security research, vulnerability detection, and audit workflows, compatible with Claude Code, Codex, and ChatGPT. |
| [Vigil](https://github.com/deadbits/vigil-llm) | Vigil is a Python library and REST API for detecting prompt injections, jailbreaks, and other threats in Large Language Model prompts and responses. |
| [vulners-mcp](https://github.com/vulnersCom/vulners-mcp) | Vulners MCP Server provides seamless access to the Vulners vulnerability database through AI assistants like Claude Desktop, enabling security researchers and developers to query comprehensive vulnerability data, search for CVEs, and audit software packages directly through natural language conversations. |

## Misc

| Tool | Description |
| :--- | :--- |
| [anew](https://github.com/tomnomnom/anew) | anew adds new lines to files, skipping duplicates. Primary use: deduplicating lists. Target platform: cross-platform. Protocol: file-based. |
| [arsenal-cli](https://pypi.org/project/arsenal-cli/) | Arsenal-cli is a command-line tool for pentesters to quickly search, select, and execute pre-defined penetration testing commands. |
| [Caldera](https://github.com/mitre/caldera) | Caldera is a cyber security platform for automating adversary emulation, assisting manual red-teams, and incident response using the MITRE ATT&CK framework. It includes a core system with a REST API and web interface, and a plugin ecosystem for expanding capabilities. |
| [CredMaster](https://github.com/knavesec/CredMaster) | CredMaster is a password spraying tool that uses FireProx APIs to rotate IP addresses, enhancing anonymity and evading throttling during authentication attempts. |
| [CyberChef](https://github.com/gchq/CyberChef) | CyberChef is a web app for encryption, encoding, compression, and data analysis in browsers and Node.js. |
| [empire](https://hub.docker.com/r/bcsecurity/empire) | Empire is a post-exploitation framework for Windows environments, allowing attackers to maintain persistence, gather information, and execute commands on compromised systems. |
| [evilginx](https://github.com/kgretzky/evilginx2) | evilginx is a man-in-the-middle attack framework used for phishing login credentials and session cookies, allowing bypass of 2-factor authentication. It is a successor to Evilginx and is fully written in GO as a standalone application. |
| [EvilGoPhish](https://github.com/fin3ss3g0d/evilgophish) | EvilGoPhish combines evilginx3 and GoPhish for social engineering and phishing campaigns, targeting web applications and protocols. |
| [faraday-cli](https://pypi.org/project/faraday-cli/) | faraday-cli is a command-line interface for automating security workflows with Faraday, a web-based platform for managing and analyzing cybersecurity data. |
| [gf](https://github.com/tomnomnom/gf) | A wrapper around grep to simplify and avoid errors in common search patterns, supporting custom engines like Silver Searcher. |
| [gitleaks](https://github.com/gitleaks/gitleaks) | Gitleaks is a tool for detecting secrets like passwords, API keys, and tokens in git repos and files. |
| [gophish](https://github.com/gophish/gophish) | Gophish is an open-source phishing toolkit for businesses and penetration testers, enabling quick and easy phishing engagements and security awareness training. It supports Windows, Mac, and Linux platforms. |
| [Havoc](https://github.com/HavocFramework/Havoc) | Havoc is a modern post-exploitation C2 framework for Windows, Linux, and macOS, featuring a cross-platform UI, multi-user control, and customizable C2 profiles. |
| [InternalAllTheThings](https://github.com/swisskyrepo/InternalAllTheThings) | InternalAllTheThings is a collection of Active Directory and internal penetration testing cheatsheets, providing useful payloads and bypasses for security assessments. |
| [LaZagne](https://github.com/AlessandroZ/LaZagne) | LaZagne is an open-source tool for retrieving passwords from various software on Windows, Linux, and Mac platforms. |
| [linux-smart-enumeration](https://github.com/diego-treitos/linux-smart-enumeration) | A Linux enumeration tool for pentesting and CTFs with verbosity levels, focusing on privilege escalation. |
| [Loki-C2](https://github.com/boku7/Loki) | Loki-C2 is a Node.js-based command and control framework for script-jacking vulnerable Electron applications, enabling backdoor and hollowing without invalidating code signing. |
| [merlin](https://github.com/Ne0nd0g/merlin) | Merlin is a cross-platform HTTP/2 C2 server and agent for post-exploitation. |
| [mimipenguin](https://github.com/huntergregal/mimipenguin) | MimiPenguin is a Linux tool to extract login passwords from the current user by analyzing memory and system files, targeting GNOME Keyring and other authentication mechanisms. |
| [Modlishka](https://github.com/drk1wi/Modlishka) | Modlishka is an open-source penetration testing tool that acts as a man-in-the-middle proxy, transparently handling multi-domain HTTP/HTTPS traffic over a single domain, supporting TLS and non-TLS, and bypassing many common 2FA implementations. |
| [Mythic](https://github.com/its-a-feature/Mythic) | Mythic is a collaborative, multi-platform red teaming framework for post-exploit operations, built with GoLang, Docker, and a web UI. |
| [notify](https://github.com/projectdiscovery/notify) | Notify is a Go-based tool for streaming output to various platforms including Slack, Discord, Telegram, and more. |
| [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) | PayloadsAllTheThings is a comprehensive list of useful payloads and bypasses for web application security and penetration testing. It serves as a cheatsheet for ethical hackers and security professionals. |
| [pdtm](https://github.com/projectdiscovery/pdtm) | pdtm is a Go-based tool for managing open source projects from ProjectDiscovery, supporting installation, update, and removal of projects. |
| [PEASS-ng](https://github.com/peass-ng/PEASS-ng) | PEASS-ng is a suite of scripts for Linux and Windows to identify local privilege escalation paths, providing detailed information with color-coded output for easy recognition. |
| [PoshC2](https://github.com/nettitude/PoshC2) | PoshC2 is a proxy-aware C2 framework for red teaming, post-exploitation, and lateral movement, supporting Windows, *nix, and OSX. |
| [pspy](https://github.com/DominicBreuker/pspy) | pspy is a command-line tool for monitoring Linux processes without root permissions, useful for CTF enumeration and demonstrating command-line security issues. |
| [PyExfil](https://github.com/ytisf/PyExfil) | PyExfil is a Python toolkit for researching and stress-testing data exfiltration techniques across various channels, including network, physical, and steganographic methods, primarily for red team simulation and DLP detection testing. |
| [qsreplace](https://github.com/tomnomnom/qsreplace) | qsreplace reads URLs from stdin, replacing all query string values with a user-supplied value. Primary use: batch URL manipulation for testing or analysis. Target platform: Cross-platform, compatible with HTTP(S) URLs. |
| [RedEye](https://github.com/cisagov/RedEye) | RedEye is an open-source visual analytic tool for Red and Blue Team operations, supporting C2 log visualization and analysis. |
| [SecLists](https://github.com/danielmiessler/SecLists) | SecLists is a comprehensive collection of lists for security assessments, including usernames, passwords, URLs, and fuzzing payloads. |
| [SET](https://github.com/trustedsec/social-engineer-toolkit) | SET is an open-source penetration testing framework for authorized social-engineering assessments, targeting Linux, macOS, and Windows through WSL/WSL2. |
| [sliver-client](https://github.com/BishopFox/sliver) | Sliver is an open-source, cross-platform adversary emulation and red team framework for authorized security testing, supporting C2 over mTLS, WireGuard, HTTP(S), and DNS. |
| [sliver-server](https://github.com/BishopFox/sliver) | Sliver is an open-source, cross-platform adversary emulation and red team framework for authorized security testing, supporting C2 over mTLS, WireGuard, HTTP(S), and DNS. |
| [spiderfoot](https://hub.docker.com/r/spiderfoot/spiderfoot) | Spiderfoot is an open-source intelligence (OSINT) tool for gathering information about a target using various online sources. |
| [sploitscan](https://pypi.org/project/sploitscan/) | SploitScan is a cybersecurity utility for identifying and assessing vulnerabilities and associated exploits, supporting CVE information retrieval, EPSS integration, and multiple exploit databases. |
| [SquarePhish](https://github.com/secureworks/squarephish) | SquarePhish is an advanced phishing tool using OAuth Device code authentication flow and QR codes to trick victims into granting access to their accounts. |
| [SUDO_KILLER](https://github.com/TH3xACE/SUDO_KILLER) | SUDO_KILLER is a tool for manually exploiting privilege escalation vulnerabilities in the sudo program on Unix-like systems, targeting Linux environments. |
| [trufflehog](https://github.com/trufflesecurity/trufflehog) | TruffleHog is a tool for discovering, classifying, validating, and analyzing leaked credentials in various sources including Git, chats, wikis, logs, and more. It supports over 800 secret types and can validate the live status of each secret. |
| [usbkill](https://github.com/hephaest0s/usbkill) | usbkill is an anti-forensic kill-switch for Linux, *BSD, and OS X that shuts down the computer upon detecting USB activity, enhancing security against unauthorized access. |
| [Zphisher](https://github.com/htr-tech/zphisher) | Zphisher is an automated phishing tool with 30+ templates, designed for educational purposes only. It supports multiple tunneling options and can be used on Linux and Termux platforms. |

## Mobile

| Tool | Description |
| :--- | :--- |
| [adb](https://packages.debian.org/search?keywords=adb) | ADB (Android Debug Bridge) is a versatile command-line tool for interacting with Android devices, enabling debugging, file transfer, and device management. |
| [androguard](https://pypi.org/project/androguard/) | Androguard is a Python-based tool for analyzing Android applications, primarily used for malware analysis and security research. |
| [apk-mitm](https://www.npmjs.com/package/apk-mitm) | apk-mitm is a tool for intercepting and modifying Android APK files, primarily used for security testing and analysis. |
| [apkid](https://pypi.org/project/apkid/) | APKiD identifies compilers, packers, and obfuscators in Android APKs, similar to PEiD for Android. |
| [apkleaks](https://pypi.org/project/apkleaks/) | apkleaks scans APK files for URIs, endpoints, and secrets using jadx disassembler. |
| [apksigner](https://packages.debian.org/search?keywords=apksigner) | Apksigner is a command line tool for signing and verifying Android APKs. |
| [apktool](https://github.com/iBotPeaches/Apktool) | Apktool is a tool for reverse engineering Android APK files, decoding resources and rebuilding them with modifications. |
| [dex2jar](https://github.com/pxb1988/dex2jar) | dex2jar converts Android .dex files to Java .class files for analysis and debugging. |
| [drozer](https://pypi.org/project/drozer/) | drozer is an open-source Android security testing framework that allows security professionals to search for vulnerabilities in apps and devices by simulating app interactions with the Android Runtime and other apps' IPC endpoints. |
| [jadx](https://github.com/skylot/jadx) | jadx is a command-line and GUI tool for decompiling Android APKs and DEX files to Java source code, supporting various Android and Java file formats. |
| [medusa-frida](https://github.com/Ch0pin/medusa) | medusa-frida is a modular automation framework for runtime testing and investigating Android and iOS apps, using Frida for dynamic analysis. It supports bypassing protections, inspecting network activity, tracing API calls, and monitoring malware behavior. |
| [mobsf](https://hub.docker.com/r/opensecurity/mobile-security-framework-mobsf) | MobSF is an automated mobile application pentesting framework for Android, iOS, and Windows Mobile, supporting static and dynamic analysis, and integrating with DevSecOps pipelines via REST APIs and CLI tools. |
| [objection](https://pypi.org/project/objection/) | objection is a runtime mobile exploration toolkit using Frida for assessing mobile app security on iOS and Android, enabling tasks like inspecting file systems, bypassing SSL pinning, and memory manipulation. |
| [qark](https://pypi.org/project/qark/) | qark is a static code analysis tool for identifying security vulnerabilities in Android applications. |
| [rms-runtime-mobile-security](https://www.npmjs.com/package/rms-runtime-mobile-security) | rms-runtime-mobile-security is a runtime security tool for mobile applications, designed to protect against malicious activities and ensure secure execution environments. |
| [scrcpy](https://packages.debian.org/search?keywords=scrcpy) | scrcpy: Display and control your Android device over USB or TCP/IP. |
| [smali](https://packages.debian.org/search?keywords=smali) | Smali is an assembler/disassembler for Android's DEX format, used for reverse engineering and customizing Android applications. |
| [zipalign](https://packages.debian.org/search?keywords=zipalign) | zipalign aligns the resources in Android APK files to improve performance on ARM processors. |

## Networking

| Tool | Description |
| :--- | :--- |
| [arp-scan](https://packages.debian.org/search?keywords=arp-scan) | arp-scan is a network tool for ARP scanning and fingerprinting, targeting IPv4 networks. |
| [arping](https://packages.debian.org/search?keywords=arping) | arping sends IP and/or ARP pings to the MAC address, useful for network diagnostics and security. |
| [bettercap](https://github.com/bettercap/bettercap) | bettercap is a versatile, extensible framework for WiFi, Bluetooth, CAN-bus, HID, and Ethernet network reconnaissance and MITM attacks, suitable for security researchers and red teamers. |
| [chisel](https://github.com/jpillora/chisel) | Chisel is a fast TCP/UDP tunnel over HTTP, secured via SSH, for passing through firewalls and providing a secure endpoint into your network. |
| [dns2tcp](https://packages.debian.org/search?keywords=dns2tcp) | dns2tcp is a TCP-over-DNS tunnel server and client for Linux. |
| [dnscat2](https://github.com/iagox86/dnscat2) | dnscat2 is a DNS tunnel for encrypted command-and-control channels, supporting any data and running on various platforms. |
| [dnschef](https://github.com/iphelix/dnschef) | DNSChef is a DNS proxy tool for penetration testers and malware analysts, intercepting and modifying DNS queries and responses. |
| [dnsutils](https://packages.debian.org/search?keywords=dnsutils) | dnsutils provides command-line tools for querying DNS servers, primarily used for network diagnostics and troubleshooting on Unix-like systems. |
| [ettercap-text-only](https://packages.debian.org/search?keywords=ettercap-text-only) | Ettercap-text-only is a console-mode version of Ettercap, a network sniffer and packet manipulation tool for security testing and analysis. |
| [fping](https://packages.debian.org/search?keywords=fping) | fping is a network tool that sends ICMP ECHO_REQUEST packets to multiple hosts concurrently, reporting their reachability and response times. |
| [frpc](https://github.com/fatedier/frp) | Client binary for frp (Fast Reverse Proxy) that runs behind NAT or firewalls to forward local TCP, UDP, HTTP, or HTTPS ports to an frps server. |
| [frps](https://github.com/fatedier/frp) | frps is a fast reverse proxy for exposing local servers behind NAT or firewalls to the internet, supporting TCP, UDP, HTTP, and HTTPS protocols. |
| [gost](https://github.com/ginuerzh/gost) | GO Simple Tunnel - a simple tunnel written in golang, supporting multiple tunnel types, proxy protocols, and features like port forwarding, DNS resolution, and more. |
| [hping3](https://packages.debian.org/search?keywords=hping3) | hping3 is a command-line utility for sending custom TCP/IP packets, used for network testing and security auditing on Unix-like systems. |
| [iftop](https://packages.debian.org/search?keywords=iftop) | iftop is a network traffic monitor that displays bandwidth usage on a network interface in real-time. |
| [iodine](https://packages.debian.org/search?keywords=iodine) | iodine is a tool for tunneling IPv4 data through a DNS server, primarily used for bypassing network censorship and enhancing privacy. |
| [iptraf-ng](https://packages.debian.org/search?keywords=iptraf-ng) | iptraf-ng is a network traffic monitor for Linux, providing real-time statistics and analysis of network traffic on IP networks. |
| [ligolo-agent](https://github.com/nicocha30/ligolo-ng) | Ligolo-agent is a lightweight tunneling tool using TUN interfaces for pentesting and post-exploitation, supporting Windows, Linux, MacOS, and BSD. |
| [ligolo-proxy](https://github.com/nicocha30/ligolo-ng) | Ligolo-ng is a simple, lightweight tunneling tool that uses TUN interfaces for establishing reverse TCP/TLS connections, suitable for pentesting and post-exploitation on Windows, Linux, MacOS, and BSD. |
| [macchanger](https://packages.debian.org/search?keywords=macchanger) | macchanger is a utility for manipulating the MAC address of network interfaces on Linux systems. |
| [masscan](https://packages.debian.org/search?keywords=masscan) | masscan is a fast TCP port scanner designed for network discovery and security auditing. |
| [mitmproxy](https://pypi.org/project/mitmproxy/) | mitmproxy is an interactive, SSL/TLS-capable intercepting proxy for HTTP/1, HTTP/2, and WebSockets, available for MacOS, Windows, and POSIX systems. |
| [nbtscan](https://packages.debian.org/search?keywords=nbtscan) | nbtscan is a network scanning tool that searches for NetBIOS information on a network. |
| [ncrack](https://packages.debian.org/search?keywords=ncrack) | Ncrack is a high-speed network authentication cracking tool targeting various protocols including SSH, FTP, and VNC. |
| [nebula-overlay](https://packages.debian.org/search?suite=default&section=all&arch=any&searchon=names&keywords=nebula) | Nebula-overlay is a performant, scalable network overlay tool for creating virtual networks. |
| [netcat-openbsd](https://packages.debian.org/search?keywords=netcat-openbsd) | netcat-openbsd: TCP/IP swiss army knife for network communication and data transfer. |
| [netdiscover](https://packages.debian.org/search?keywords=netdiscover) | netdiscover is an active/passive network address scanner using ARP requests, designed for Linux. |
| [netsniff-ng](https://packages.debian.org/search?keywords=netsniff-ng) | netsniff-ng is a Linux network packet sniffer toolkit for capturing and analyzing network traffic. |
| [ngrep](https://packages.debian.org/search?keywords=ngrep) | ngrep is a network grep tool for filtering and searching network traffic based on patterns. |
| [nipe](https://github.com/htrgouvea/nipe) | Nipe is a Perl engine that routes traffic through the Tor network to anonymize internet activity. |
| [nmap](https://packages.debian.org/search?keywords=nmap) | nmap is a network scanning tool for discovering hosts and services on a network. |
| [onesixtyone](https://packages.debian.org/search?keywords=onesixtyone) | onesixtyone is a fast and simple SNMP scanner for network discovery and security auditing. |
| [p0f](https://packages.debian.org/search?keywords=p0f) | Passive OS fingerprinting tool for network traffic analysis. |
| [PRET](https://github.com/RUB-NDS/PRET) | PRET is a Python-based toolkit for testing printer security, supporting PostScript, PJL, and PCL. It facilitates communication between the user and the printer, allowing for various attacks and fuzzing operations. Target platform: Network printers and USB printers. |
| [proxychains4](https://packages.debian.org/search?keywords=proxychains4) | proxychains4 redirects connections through SOCKS or HTTP proxies, enhancing network security and anonymity. |
| [pwnat](https://github.com/samyk/pwnat) | pwnat is a tool that allows clients behind NATs to communicate with servers behind separate NATs without port forwarding, DMZ, or third-party involvement, by exploiting NAT translation tables. |
| [redsocks](https://packages.debian.org/search?keywords=redsocks) | redsocks is a TCP connection redirector to a SOCKS or HTTPS proxy server, suitable for Linux. |
| [rustscan](https://crates.io/crates/rustscan) | RustScan is a fast port scanner built in Rust, designed for quick network discovery and security auditing. |
| [smbclient](https://packages.debian.org/search?keywords=smbclient) | smbclient is a command-line tool for accessing SMB/CIFS shares on Unix-like systems. |
| [smbmap](https://pypi.org/project/smbmap/) | smbmap is a Python tool for enumerating SMB shares and files, primarily used for penetration testing and network auditing. |
| [snmp](https://packages.debian.org/search?keywords=snmp) | SNMP (Simple Network Management Protocol) applications for network management and monitoring. |
| [socat](https://packages.debian.org/search?keywords=socat) | socat is a versatile network utility for bidirectional data transfer between two endpoints, supporting multiple protocols and platforms. |
| [sshuttle](https://pypi.org/project/sshuttle/) | sshuttle is a transparent proxy server that forwards traffic over SSH, enabling secure remote network access without requiring admin privileges. It works on Linux and MacOS and supports DNS tunneling. |
| [sslscan](https://packages.debian.org/search?keywords=sslscan) | sslscan tests SSL/TLS enabled services to discover supported cipher suites. |
| [sslsplit](https://packages.debian.org/search?keywords=sslsplit) | sslsplit is a transparent SSL/TLS interception tool for analyzing encrypted network traffic. |
| [sslstrip](https://packages.debian.org/search?keywords=sslstrip) | sslstrip is a tool that intercepts SSL/TLS traffic and converts it to HTTP, allowing for man-in-the-middle attacks on HTTPS connections. |
| [stunnel4](https://packages.debian.org/search?keywords=stunnel4) | stunnel4 is a universal SSL tunnel for network daemons, enabling secure communication over insecure networks. |
| [tcpdump](https://packages.debian.org/search?keywords=tcpdump) | tcpdump is a command-line network traffic analyzer for capturing and analyzing network packets on various platforms and protocols. |
| [tcpflow](https://packages.debian.org/search?keywords=tcpflow) | tcpflow is a command-line tool for capturing and analyzing TCP/IP traffic, useful for network debugging and analysis. |
| [tcpreplay](https://packages.debian.org/search?keywords=tcpreplay) | tcpreplay is a tool to replay saved tcpdump files at arbitrary speeds, primarily used for network testing and analysis. |
| [tor](https://packages.debian.org/search?keywords=tor) | Tor is an anonymizing overlay network for TCP, enabling users to route their internet traffic through multiple volunteer-operated relays to protect privacy and anonymity. |
| [traceroute](https://packages.debian.org/search?keywords=traceroute) | traceroute traces the route taken by packets over an IPv4/IPv6 network, useful for diagnosing network connectivity issues. |
| [tshark](https://packages.debian.org/search?keywords=tshark) | tshark is a network traffic analyzer for capturing and analyzing network packets, primarily used for troubleshooting and security analysis on various platforms and protocols. |
| [whois](https://packages.debian.org/search?keywords=whois) | The 'whois' tool is an intelligent WHOIS client used to query WHOIS databases for information about domain names, IP addresses, and other network resources. |
| [wireshark-common](https://packages.debian.org/search?keywords=wireshark-common) | Wireshark-common provides common files for the network traffic analyzer Wireshark, supporting multiple architectures and protocols. |
| [wstunnel](https://github.com/erebe/wstunnel) | wstunnel is a command-line tool for tunneling traffic over Websocket or HTTP2, enabling bypass of firewalls and proxies. It supports static and dynamic tunneling, SOCKS5, TCP, UDP, and UDP tunneling, and is available as a standalone binary. |
| [yersinia](https://github.com/tomac/yersinia) | Yersinia is a framework for layer 2 attacks, primarily used to perform Spanning Tree Protocol (STP) attacks such as sending configuration (conf) and topology change (tcn) BPDUs to disrupt network operations. |
| [zmap](https://packages.debian.org/search?keywords=zmap) | ZMap is a fast single packet network scanner designed for Internet-wide network surveys. |

## PWN

| Tool | Description |
| :--- | :--- |
| [AFLplusplus](https://github.com/AFLplusplus/AFLplusplus) | AFL++ is a high-performance fuzzing tool that extends Google's AFL with advanced features like QEMU mode, collision-free coverage, and enhanced mutation techniques, targeting a wide range of applications and protocols. |
| [boofuzz](https://pypi.org/project/boofuzz/) | Boofuzz is a network protocol fuzzer for humans, a fork of Sulley, designed for extensibility and ease of use, supporting various communication mediums and protocols. |
| [DNSExfiltrator](https://github.com/Arno0x/DNSExfiltrator) | DNSExfiltrator is a tool for covert data exfiltration using DNS requests. |
| [Donut](https://github.com/TheWover/donut) | Donut generates position-independent shellcode for in-memory execution of VBScript, JScript, EXE, DLL, and .NET assemblies, supporting encryption, compression, and various patching techniques. |
| [Egress-Assess](https://github.com/FortyNorthSecurity/Egress-Assess) | Egress-Assess tests egress data detection capabilities using FTP, HTTP, and HTTPS. |
| [eviltree](https://github.com/t3l3machus/eviltree) | Eviltree is a Python3 tool that extends the classic 'tree' command with regex search capabilities, highlighting files containing matches in nested directory structures. It's useful for post-exploitation enumeration and searching for secrets in files across Linux and Windows platforms. |
| [exploitdb](https://gitlab.com/exploit-database/exploitdb) | Exploit-Database is a repository of known software vulnerabilities and exploits, primarily used for security research and penetration testing. |
| [Freeze](https://github.com/Tylous/Freeze) | Freeze is a payload toolkit for bypassing EDRs using suspended processes, direct syscalls, and alternative execution methods. |
| [Hoaxshell](https://github.com/t3l3machus/hoaxshell) | Hoaxshell is a Windows reverse shell payload generator and handler that uses the HTTP(S) protocol to establish a beacon-like reverse shell, targeting Windows platforms. |
| [honggfuzz](https://github.com/google/honggfuzz) | Honggfuzz is a security-oriented, feedback-driven fuzzer that uses code coverage to evolve inputs, supporting persistent fuzzing for high-speed testing on Linux, macOS, Android, and Windows. |
| [interactsh-client](https://github.com/projectdiscovery/interactsh) | Interactsh-client is a tool for detecting out-of-band interactions using DNS/HTTP(S)/SMTP(S)/LDAP protocols. It supports multiple server endpoints and provides features like AES encryption, automatic TLS, and customizable payloads. |
| [Ivy](https://github.com/optiv/Ivy) | Ivy is a VBA payload creation framework for executing arbitrary shellcode in memory, bypassing EDRs and signature-based detection. |
| [libc-database](https://github.com/niklasb/libc-database) | libc-database is a tool for building and querying a database of libc offsets, aiding in exploitation and CTF challenges. It supports multiple Linux distributions and provides a web interface for easy access. |
| [metasploit](https://github.com/rapid7/metasploit-framework) | Metasploit Framework is an open-source tool for developing, testing, and using exploit code. It primarily targets network security professionals and ethical hackers for penetration testing and vulnerability assessment. |
| [nanodump](https://github.com/fortra/nanodump) | NanoDump is a flexible tool for creating minidumps of the LSASS process, supporting various methods for privilege escalation and handling. |
| [one_gadget](https://rubygems.org/gems/one_gadget) | one_gadget is a Ruby gem for finding one-gadgets in libc files, aiding in CTF pwn challenges. |
| [patchelf](https://packages.debian.org/search?keywords=patchelf) | patchelf modifies properties of ELF executables, useful for re-linking and updating binary files. |
| [Penelope](https://github.com/brightio/penelope) | Penelope is a modern shell handler for penetration testers and CTF players, providing advanced features like automatic PTY upgrades, session management, logging, and file transfers. |
| [preeny](https://github.com/zardus/preeny) | Preeny is a set of preload libraries for Linux that disable functions like fork(), rand(), and alarm(), and can convert server applications to console applications, patch binaries, and more. |
| [pwncat-cs](https://pypi.org/project/pwncat-cs/) | pwncat-cs is a post-exploitation framework for Linux and Windows targets, automating common red team operations and enhancing shell interactions. |
| [pwninit](https://crates.io/crates/pwninit) | pwninit automates starting binary exploit challenges for ELF files. |
| [pwntools](https://pypi.org/project/pwntools/) | pwntools is a Python library for exploit development and CTF challenges, supporting various architectures and protocols. |
| [QueenSono](https://github.com/ariary/QueenSono) | QueenSono is a Golang tool for ICMP data exfiltration, enabling bindshell, HTTP over ICMP tunneling, and other ICMP-based communication methods. |
| [radamsa](https://gitlab.com/akihe/radamsa) | radamsa is a general-purpose fuzzer for crafting malicious inputs for security testing. |
| [ROPgadget](https://pypi.org/project/ROPgadget/) | ROPgadget is a Python script for analyzing ROP (Return-Oriented Programming) gadgets in binary files, aiding in exploit development. |
| [ropium](https://github.com/Boyan-MILANOV/ropium) | ROPium is a tool for building ROP exploits by automatically extracting and chaining gadgets from binaries, supporting X86 and X64 architectures. |
| [ropper](https://pypi.org/project/ropper/) | Ropper is a ROP (Return-Oriented Programming) gadget search tool for binary files, aiding in exploitation and analysis. |
| [ropr](https://crates.io/crates/ropr) | ropr is a fast multithreaded ROP gadget finder, an alternative to ropper and ropgadget. |
| [RouterSploit](https://github.com/threat9/routersploit) | RouterSploit is an open-source Python framework for exploiting embedded devices, supporting modules for brute-forcing, credential testing, scanning, and payload generation. |
| [scapy](https://pypi.org/project/scapy/) | Scapy is a Python library for crafting and sending network packets, primarily used for network analysis and penetration testing. |
| [ScareCrow](https://github.com/optiv/ScareCrow) | ScareCrow is a payload creation framework for side-loading into legitimate Windows processes to bypass EDR controls by unhooking system DLLs in memory using VirtualProtect and decrypting shellcode. |
| [seccomp-tools](https://rubygems.org/gems/seccomp-tools) | seccomp-tools: A set of tools to analyze seccomp rules for Linux systems. |
| [ShellNoob](https://github.com/reyammer/shellnoob) | ShellNoob is a shellcode writing toolkit for Linux/x86, Linux/x86_64, Linux/ARM, FreeBSD/x86, and FreeBSD/x86_64. |
| [spike](https://packages.debian.org/search?keywords=spike) | Spike is a lightweight secrets management tool using SPIFFE identity control plane, suitable for various Linux distributions. |
| [unicorn](https://github.com/trustedsec/unicorn) | Unicorn is a PowerShell downgrade attack tool for injecting shellcode into memory, supporting custom shellcode, Cobalt Strike, and Metasploit. |
| [Villain](https://github.com/t3l3machus/Villain) | Villain is a high-level C2 framework for reverse TCP and HoaxShell-based shells, enhancing functionality and sharing among connected servers. |

## Recon

| Tool | Description |
| :--- | :--- |
| [alterx](https://github.com/projectdiscovery/alterx) | Fast and customizable subdomain wordlist generator using DSL for subdomain enumeration and pattern mining. |
| [amass](https://github.com/owasp-amass/amass) | Amass is an open-source tool for network mapping and external asset discovery using DNS enumeration and OSINT techniques. |
| [asnmap](https://github.com/projectdiscovery/asnmap) | asnmap is a Go CLI and library for quickly mapping organization network ranges using ASN information, supporting ASN, ORG, DNS, and IP lookups with JSON, CSV, and text output formats. |
| [assetfinder](https://github.com/tomnomnom/assetfinder) | assetfinder is a command-line tool for finding domains and subdomains related to a given domain using various online sources. |
| [axiom](https://github.com/pry0cc/axiom) | Axiom is a dynamic infrastructure framework for efficiently working with multi-cloud environments, deploying repeatable infrastructure for offensive and defensive security tasks. It supports tools like nmap, ffuf, and masscan, and can distribute scans across multiple instances for quick results. |
| [bbot](https://pypi.org/project/bbot/) | bbot is a multipurpose OSINT scanner for hackers, automating reconnaissance, bug bounties, and ASM. |
| [blackbird](https://github.com/p1ngul1n0/blackbird) | Blackbird is an OSINT tool for fast username and email searches across 600 platforms, with free AI-powered profiling and automated analysis. |
| [censys](https://pypi.org/project/censys/) | Censys is a comprehensive search engine for internet assets, allowing users to discover and analyze information about websites, services, and devices on the internet. |
| [certSniff](https://github.com/A-poc/certSniff) | certSniff is a Python-based keyword sniffer that monitors certificate transparency logs for specified strings, useful for security audits and compliance checks. |
| [chaos](https://github.com/projectdiscovery/chaos-client) | Chaos Client is a Go tool to communicate with Chaos dataset API for subdomain enumeration and other domain-related queries. It requires a projectdiscovery cloud API key for authentication. Primary use case is for security researchers and penetration testers to gather subdomains and other domain information. Target platform is any system with Go installed. It supports both CLI and library usage. |
| [commit-stream](https://github.com/x1sec/commit-stream) | commit-stream is a GitHub search tool for code, projects, and people. It allows users to search for repositories, commits, and contributors based on various criteria. |
| [crosslinked](https://pypi.org/project/crosslinked/) | Crosslinked is a Python library for creating and managing cross-site request forgery (CSRF) tokens, primarily used in web applications to protect against CSRF attacks. It supports Python 3 and is compatible with various web frameworks. |
| [dnsdumpster](https://dnsdumpster.com/developer/) | dnsdumpster is a DNS information and attack surface analysis tool accessible via API, providing DNS records, ASN details, and network banners for domains. |
| [dnsenum](https://packages.debian.org/search?keywords=dnsenum) | dnsenum is a tool to enumerate domain DNS information, primarily used for network security assessments. |
| [dnsgen](https://pypi.org/project/dnsgen/) | dnsgen is a Python tool for generating DNS queries for testing and penetration testing. |
| [dnsrecon](https://pypi.org/project/dnsrecon/) | dnsrecon is a DNS enumeration tool for gathering information about DNS records and configurations. |
| [dnstwist](https://pypi.org/project/dnstwist/) | dnstwist is a domain name permutation engine for detecting homograph phishing attacks, typo squatting, and brand impersonation. It is a Python tool that can be used on any platform supporting Python 3. |
| [dnsx](https://github.com/projectdiscovery/dnsx) | dnsx is a fast and multi-purpose DNS toolkit for running various DNS queries, including A, AAAA, CNAME, PTR, NS, MX, TXT, SRV, and SOA records, with support for custom resolvers and wildcard filtering. |
| [emailharvester](https://pypi.org/project/emailharvester/) | EmailHarvester 2.0.1 is a Python tool to retrieve domain email addresses from search engines like Google, Bing, and Yahoo, with options to export results and use custom User-Agent strings. |
| [EyeWitness](https://github.com/FortyNorthSecurity/EyeWitness) | EyeWitness is a web screenshot tool that provides server header info and identifies default credentials, supporting cross-platform use with Chromium for reliable headless screenshots. |
| [FavFreak](https://github.com/devanshbatham/FavFreak) | FavFreak is a Python tool for reconnaissance using favicon hashes, sorting domains/subdomains/IPs based on their hashes, and matching them against a fingerprint dictionary for bug bounty hunting and OSINT. |
| [findomain](https://github.com/Findomain/Findomain) | findomain is a fast and comprehensive tool for domain recognition, supporting subdomain enumeration, monitoring, and data import from other tools. It targets Linux and Windows platforms. |
| [Gato](https://github.com/praetorian-inc/gato) | Gato is a deprecated GitHub Actions pipeline enumeration and attack tool, superseded by Trajan. It identifies and exploits pipeline vulnerabilities in public and private repositories. |
| [gau](https://github.com/lc/gau) | gau fetches known URLs from AlienVault's OTX, Wayback Machine, Common Crawl, and URLScan for domain enumeration and security research. |
| [ghunt](https://pypi.org/project/ghunt/) | GHunt is an offensive Google framework for OSINT, email, Gaia ID, Drive file/folder, and geolocation information retrieval. It supports CLI and Python library usage, with JSON export and browser extension for ease of login. Target platform: Python 3.10+. |
| [github-subdomains](https://github.com/gwen001/github-subdomains) | github-subdomains is a Go tool for finding subdomains on GitHub using provided tokens or an environment variable. |
| [GooFuzz](https://github.com/m3n0sd0n4ld/GooFuzz) | GooFuzz is a Bash script for OSINT-based directory and file enumeration using Google Dorks, without leaving evidence on the target server. |
| [gospider](https://github.com/jaeles-project/gospider) | Gospider is a fast web spider written in Go for reconnaissance and bug bounty hunting, supporting features like sitemap parsing, robots.txt handling, and parallel crawling. |
| [gowitness](https://github.com/sensepost/gowitness) | gowitness is a web screenshot utility using Chrome Headless for security footprinting and reporting. |
| [h8mail](https://pypi.org/project/h8mail/) | h8mail is a Python tool for email OSINT and password breach hunting, using various breach and reconnaissance services, or local data. It supports email pattern matching, local searches, and output to CSV. Compatible with the Breached Compilation torrent scripts and available via pip. |
| [hakcheckurl](https://github.com/hakluke/hakcheckurl) | Takes a list of URLs and returns their HTTP response codes, useful for quickly determining the status of multiple web pages. |
| [hakrawler](https://github.com/hakluke/hakrawler) | hakrawler is a simple, fast web crawler for discovering endpoints and assets within a web application, supporting single URLs, multiple URLs from a file, and subdomain crawling. |
| [hakrevdns](https://github.com/hakluke/hakrevdns) | hakrevdns is a small, fast tool for performing reverse DNS lookups en masse, useful for finding domains and subdomains from IP addresses. It supports custom resolvers, protocols, and threading. |
| [holehe](https://pypi.org/project/holehe/) | holehe is a Python tool to check if an email is used on various websites and retrieve information if the password is forgotten. |
| [httprobe](https://github.com/tomnomnom/httprobe) | httprobe is a command-line tool for probing a list of domains to find active HTTP and HTTPS servers. It reads domain names from standard input and outputs the working HTTP and HTTPS URLs. It supports custom ports, concurrency, and timeout settings. Target platform: Unix-like systems. Protocol: HTTP/HTTPS. |
| [httpx](https://github.com/projectdiscovery/httpx) | httpx is a fast and multi-purpose HTTP toolkit for running multiple probes using the retryablehttp library, supporting hosts, URLs, and CIDR inputs. |
| [hunter-io-agents](https://hunter.io/agents.md) | Hunter-io-agents connects Hunter.io to AI agents for email address verification, contact discovery, and company enrichment. |
| [ignorant](https://pypi.org/project/ignorant/) | ignorant 1.2 checks if a phone number is used on Snapchat, instagram etc. |
| [iKy](https://github.com/kennbroorg/iKy) | iKy is an OSINT tool for collecting, gathering, profiling, and creating timelines from email data. |
| [instaloader](https://pypi.org/project/instaloader/) | Instaloader is a Python script for downloading Instagram content, including pictures, videos, and metadata. |
| [knock-subdomains](https://pypi.org/project/knock-subdomains/) | knock-subdomains is a Python tool for identifying subdomains of a domain by sending DNS queries. |
| [linkedin2username](https://github.com/initstring/linkedin2username) | linkedin2username is an OSINT tool that generates username lists for company employees on LinkedIn using web scraping. It requires a valid LinkedIn account for login and supports various username formats. Target platform: Web, Protocol: HTTP/HTTPS. |
| [LinkFinder](https://github.com/GerbenJavado/LinkFinder) | LinkFinder is a Python script that discovers endpoints and their parameters in JavaScript files, useful for penetration testers and bug hunters. |
| [maigret](https://pypi.org/project/maigret/) | Maigret is a command-line tool for collecting information about a person by username from thousands of websites, supporting 3,000+ sites and offering AI analysis. |
| [maltego-trx](https://pypi.org/project/maltego-trx/) | Maltego TRX is a Python library for developing Maltego transforms, enabling users to create custom data connectors and enrichment tools for cybersecurity analysis. |
| [mapcidr](https://github.com/projectdiscovery/mapcidr) | mapcidr is a utility for performing operations on CIDR ranges, including expansion, slicing, aggregation, and filtering. It supports IPv4 and IPv6 and can be used as a CLI tool or library. |
| [maryam](https://pypi.org/project/maryam/) | maryam is a Python library for information gathering and reconnaissance on social media platforms. |
| [massdns](https://github.com/blechschmidt/massdns) | MassDNS is a high-performance DNS resolver for bulk lookups and reconnaissance, targeting millions or billions of domain names. |
| [meg](https://github.com/tomnomnom/meg) | meg is a tool for fetching many paths for many hosts efficiently, designed to avoid overwhelming target systems. |
| [metabigor](https://github.com/j3ssie/metabigor) | Metabigor is a command-line tool for OSINT that discovers network ranges, certificates, related domains, exposed ports, CDN vendors, and code leaks using free sources. |
| [mosint](https://github.com/alpkeskin/mosint) | Mosint is an automated email OSINT tool written in Go, designed for security researchers to investigate target emails efficiently, verifying, validating, and checking social media, data breaches, and pastebin dumps. |
| [naabu](https://github.com/projectdiscovery/naabu) | naabu is a fast, reliable port scanner written in Go that performs SYN/CONNECT/UDP scans to enumerate valid ports for hosts, supporting multiple input formats and output options. |
| [nmapAutomator](https://github.com/21y4d/nmapAutomator) | nmapAutomator automates network enumeration and reconnaissance tasks, running scans in the background to save time during penetration testing. |
| [onionsearch](https://pypi.org/project/onionsearch/) | onionsearch 1.3 is a Python script that scrapes URLs from various .onion search engines. |
| [osmedeus](https://github.com/j3ssie/osmedeus) | Osmedeus is a security-focused declarative orchestration engine for automating complex workflows with YAML definitions, supporting distributed execution, rich function libraries, and event-driven scheduling. |
| [osrframework](https://pypi.org/project/osrframework/) | OSRFramework is a set of AGPLv3+ OSINT tools for online research, developed by i3visio analysts. |
| [parsero](https://pypi.org/project/parsero/) | Parsero is a free script written in Python which reads the Robots.txt file of a web server and looks at the Disallow entries, helps with recon. |
| [phoneinfoga](https://github.com/sundowndev/phoneinfoga) | PhoneInfoga is an open-source tool for gathering information about phone numbers, including country, carrier, and reputation reports, using various OSINT techniques. |
| [Photon](https://github.com/s0md3v/Photon) | Photon is a fast OSINT crawler for data extraction, flexible configuration, and smart thread management. |
| [puredns](https://github.com/d3mondev/puredns) | puredns is a fast domain resolver and subdomain bruteforcing tool that accurately filters out wildcard subdomains and DNS poisoned entries using massdns and trusted resolvers. |
| [pwndb](https://github.com/davidtavarez/pwndb) | pwndb is a Python tool for searching leaked credentials using the Onion service, targeting email addresses or domains. |
| [pyonyphe](https://github.com/onyphe/pyonyphe) | pyonyphe is a Python client and CLI for ONYPHE, a Cyber Defense Search Engine, providing access to various API endpoints for querying and exporting cybersecurity data. |
| [recon-ng](https://github.com/lanmaster53/recon-ng) | Recon-ng is an open-source intelligence gathering tool for conducting web-based reconnaissance quickly and thoroughly, similar to the Metasploit Framework but focused on open source data. |
| [reconftw](https://github.com/six2dez/reconftw) | reconftw is a tool for automated reconnaissance on a target domain, running a set of tools to identify vulnerabilities and gather OSINT data. It is compatible with Linux, macOS, and Windows. |
| [robin](https://github.com/apurvsinghgautam/robin) | AI-powered dark web OSINT tool using LLMs for refined queries and investigation summaries. |
| [SecretFinder](https://github.com/m4ll0k/SecretFinder) | SecretFinder is a Python script for extracting sensitive data like API keys, access tokens, JWTs, and more from JavaScript files. It supports URLs, files, and folders, and outputs results in HTML or plaintext. |
| [sherlock-project](https://pypi.org/project/sherlock-project/) | Sherlock-project is a Python tool to search for social media accounts by username across 400+ platforms. |
| [shodan](https://pypi.org/project/shodan/) | Shodan is a search engine for Internet-connected devices, providing developers with access to Shodan's data to automate tasks and integrate into existing tools. It supports Python 2.6+ and 3.4+. |
| [shuffledns](https://github.com/projectdiscovery/shuffledns) | shuffledns is a Go wrapper for massdns to enumerate valid subdomains using active bruteforce and resolve subdomains with wildcard handling, supporting easy input-output. |
| [smap](https://github.com/s0md3v/smap) | Smap is a passive port scanner using Shodan.io's API, designed as a drop-in replacement for Nmap with features like vulnerability detection, service/version fingerprinting, and optional Nmap acceleration. |
| [Sn1per](https://github.com/1N3/Sn1per) | Sn1per is an automated penetration testing and attack surface management platform that performs reconnaissance, scanning, exploitation, and reporting in a single workspace. |
| [social-analyzer](https://pypi.org/project/social-analyzer/) | Social-Analyzer is a Python tool for analyzing and finding a person's profile across 300+ social media websites, using string analysis and detection modules with a rating mechanism from 0 to 100. It's useful for investigating suspicious or malicious activities and is used by some law enforcement agencies. |
| [socialscan](https://pypi.org/project/socialscan/) | socialscan is an open-source intelligence tool for checking email address and username availability on online platforms, offering 100% accuracy and fast searches through concurrent queries. |
| [ssh-audit](https://pypi.org/project/ssh-audit/) | ssh-audit is a tool for auditing SSH server and client configurations, providing security information and recommendations. |
| [stringcheese](https://github.com/MathisHammel/stringcheese) | StringCheese is a Python script for automatically extracting CTF flags from files using various encodings and transformations. |
| [subfinder](https://github.com/projectdiscovery/subfinder) | subfinder is a fast, passive subdomain enumeration tool using curated online sources, optimized for speed and resource efficiency. |
| [subjs](https://github.com/lc/subjs) | subjs fetches JavaScript files from a list of URLs or subdomains, aiding in the discovery of undocumented endpoints and secrets. |
| [sublist3r](https://pypi.org/project/sublist3r/) | Sublist3r is a Python tool for gathering subdomains of a domain using various online sources. |
| [subzy](https://github.com/PentestPad/subzy) | Subzy is a subdomain takeover vulnerability checker that uses response fingerprints to identify vulnerable subdomains. It supports single or multiple targets and can be run from the command line. |
| [Telepathy](https://github.com/jordanwildon/Telepathy) | Telepathy is an OSINT toolkit for investigating Telegram chats, allowing analysts to archive chats, gather memberlists, and perform various analyses. It is primarily used in investigative journalism, academic research, and intelligence gathering. |
| [theHarvester](https://github.com/laramies/theHarvester) | theHarvester is an open-source intelligence tool for gathering email addresses, subdomains, and names from various public sources for reconnaissance and security assessments. |
| [toutatis](https://pypi.org/project/toutatis/) | toutatis is a Python tool to retrieve private information from Instagram accounts via API, targeting developers and security researchers. |
| [uncover](https://github.com/projectdiscovery/uncover) | uncover is a CLI tool for discovering exposed hosts on the internet using multiple search engines like Shodan, Censys, and FOFA. |
| [unfurl](https://github.com/tomnomnom/unfurl) | Unfurl extracts and displays information from URLs provided as input, useful for reconnaissance and analysis. |
| [vulscan](https://github.com/scipag/vulscan) | Vulscan enhances Nmap for vulnerability scanning using version detection and an offline VulDB database. |
| [waybackurls](https://github.com/tomnomnom/waybackurls) | Fetches all URLs known to the Wayback Machine for a given domain. |
| [waymore](https://pypi.org/project/waymore/) | waymore is a Python library for automating web scraping and data extraction, primarily used for cybersecurity threat intelligence gathering. |

## Reversing

| Tool | Description |
| :--- | :--- |
| [angr](https://pypi.org/project/angr/) | angr is a multi-architecture binary analysis toolkit for dynamic symbolic execution and static analyses on binaries, supporting Python 3.12 and later. |
| [binutils](https://packages.debian.org/search?keywords=binutils) | binutils: GNU assembler, linker, and binary utilities for various architectures. |
| [binwalk](https://packages.debian.org/search?keywords=binwalk) | Binwalk is a tool for analyzing binary files and extracting embedded files and firmware. |
| [checksec](https://packages.debian.org/search?keywords=checksec) | checksec is a Bash script to test executable properties for security vulnerabilities. |
| [cutter](https://github.com/rizinorg/cutter) | Cutter is a free and open-source reverse engineering platform powered by rizin, designed for advanced analysis and customization. |
| [decomp2dbg](https://github.com/mahaloz/decomp2dbg) | decomp2dbg is a plugin that syncs symbols between decompilers (IDA Pro, Binary Ninja, Ghidra, angr-management) and debuggers (gdb, GEF, pwndbg) for efficient reverse engineering. |
| [detect-it-easy](https://github.com/horsicq/DIE-engine) | detect-it-easy (DIE) is a free, open-source binary analysis tool for detecting malicious software, primarily used for reverse engineering and malware analysis. It supports ELF, PE, and other binary formats, and includes features like entropy analysis, signature matching, and unpacking capabilities. Target platform: Windows, Linux, macOS. Primary use case: Malware analysis, reverse engineering, and security research. |
| [edb-debugger](https://packages.debian.org/search?keywords=edb-debugger) | edb-debugger: Cross-platform x86/x86-64 debugger for debugging applications and systems. |
| [ELFkickers](https://github.com/BR903/ELFkickers) | ELFkickers is a collection of programs for accessing and manipulating ELF files, primarily used for cybersecurity analysis and reverse engineering. |
| [frida-tools](https://pypi.org/project/frida-tools/) | CLI tools for Frida, enabling dynamic instrumentation and debugging of applications on various platforms. |
| [gdb](https://packages.debian.org/search?keywords=gdb) | GNU Debugger (GDB) is a powerful command-line tool for debugging programs, supporting multiple programming languages and platforms. |
| [GEF](https://github.com/hugsy/gef) | GEF (GDB Enhanced Features) is a Python script for GDB that provides advanced debugging capabilities for exploit developers and reverse engineers on Linux, enhancing the debugging experience with architecture-agnostic features and fast execution. |
| [ghidra](https://packages.debian.org/search?keywords=ghidra) | Ghidra is a reverse engineering tool for analyzing and understanding binary software. |
| [hexedit](https://packages.debian.org/search?keywords=hexedit) | Hexedit is a simple hexadecimal and ASCII file editor for viewing and editing binary files. |
| [jd-gui](https://github.com/java-decompiler/jd-gui) | JD-GUI is a standalone Java decompiler GUI that displays Java source code from CLASS files, useful for browsing and analyzing Java bytecode. |
| [Krakatau](https://github.com/Storyyeller/Krakatau) | Krakatau is a Java decompiler, assembler, and disassembler that converts binary classfiles to human-readable text, allows modifications, and reassembles them. It handles obfuscated code and supports Java 14 features. Target platform: Java bytecode. |
| [ltrace](https://packages.debian.org/search?keywords=ltrace) | Tracks runtime library calls in dynamically linked programs, useful for debugging and performance analysis on Linux. |
| [nasm](https://packages.debian.org/search?keywords=nasm) | nasm is a general-purpose x86 assembler used for writing machine code in assembly language. |
| [peda](https://github.com/longld/peda) | PEDA is a Python-based GDB extension for exploit development, enhancing debugging with features like syntax highlighting, disassembly, and ROP gadget search. |
| [pwndbg](https://github.com/pwndbg/pwndbg) | pwndbg is a GDB and LLDB plugin that enhances debugging for low-level software developers, reverse-engineers, and exploit developers with features like a robust hexdump command and improved usability. |
| [pyinstxtractor](https://github.com/extremecoders-re/pyinstxtractor) | PyInstaller Extractor is a Python script to extract the contents of PyInstaller-generated executable files, fixing pyc headers for decompilation. |
| [qemu-system-x86](https://packages.debian.org/search?keywords=qemu-system-x86) | qemu-system-x86: QEMU full system emulation binaries for x86 architecture. |
| [qemu-user-static](https://packages.debian.org/search?keywords=qemu-user-static) | qemu-user-static provides static versions of QEMU user mode emulation binaries, enabling execution of binaries for different architectures on the host system. |
| [Qiling](https://github.com/qilingframework/qiling) | Qiling is an advanced binary emulation framework for cross-architecture and platform analysis, supporting Windows, macOS, Linux, Android, and more. It provides a sandboxed environment for malware analysis and reverse engineering. |
| [radare2](https://packages.debian.org/search?keywords=radare2) | radare2 is a free and advanced command line hexadecimal editor and reverse engineering framework for analyzing and manipulating binary files. |
| [rappel](https://github.com/yrp604/rappel) | Rappel is a Linux-based assembly REPL for x86, amd64, armv7, and armv8, allowing interactive assembly programming and debugging. |
| [rizin](https://packages.debian.org/search?keywords=rizin) | rizin is a reverse engineering framework for analyzing binary files, supporting multiple architectures and protocols. |
| [rp-lin](https://github.com/0vercl0k/rp) | rp-lin is a fast C++ ROP gadget finder for PE/ELF/Mach-O binaries targeting x86/x64/ARM/ARM64 architectures. |
| [rr](https://packages.debian.org/search?keywords=rr) | rr is an application execution recorder, player, and debugger for Linux. |
| [strace](https://packages.debian.org/search?keywords=strace) | strace is a system call tracer for debugging and monitoring applications on Unix-like operating systems. |
| [uncompyle6](https://pypi.org/project/uncompyle6/) | uncompyle6 decompiles Python 3.6+ bytecode to readable source code. |
| [upx-ucl](https://packages.debian.org/search?keywords=upx-ucl) | upx-ucl is an efficient live-compressor for executables, reducing their size without significantly impacting performance. |
| [valgrind](https://packages.debian.org/search?keywords=valgrind) | Valgrind is an instrumentation framework for building dynamic analysis tools, primarily used for memory debugging, memory leak detection, and profiling. |

## Stego

| Tool | Description |
| :--- | :--- |
| [exiv2](https://packages.debian.org/search?keywords=exiv2) | exiv2 is a C++ library and command-line tool for manipulating image metadata, supporting EXIF, IPTC, and XMP formats. |
| [jsteg](https://github.com/lukechampine/jsteg) | jsteg is a Go package for hiding data inside JPEG files using steganography by manipulating the least-significant bits of the image. It supports hiding up to 10-14 bytes of data per byte of JPEG file size and includes a command-line tool for easy use. |
| [openstego](https://github.com/syvaidya/openstego) | OpenStego is a steganography tool for hiding data and watermarks within image files, supporting both GUI and command line interfaces. |
| [outguess](https://packages.debian.org/search?keywords=outguess) | Outguess is a universal steganographic tool for hiding data within files. |
| [pngcheck](https://packages.debian.org/search?keywords=pngcheck) | pngcheck is a command-line tool to print information and verify the integrity of PNG, JNG, and MNG files. |
| [pngtools](https://packages.debian.org/search?keywords=pngtools) | pngtools is a suite of command-line tools for manipulating PNG images, suitable for Linux and Unix-like systems. |
| [sonic-visualiser](https://packages.debian.org/search?keywords=sonic-visualiser) | Sonic Visualiser is a tool for viewing and analyzing the contents of music audio files. |
| [stegextract](https://github.com/evyatarmeged/stegextract) | stegextract is a command-line tool for detecting and extracting hidden files and text from images using steganography techniques. It is useful for penetration testing and CTF challenges. |
| [steghide](https://packages.debian.org/search?keywords=steghide) | Steghide is a steganography tool for hiding files within image and audio files. |
| [stegosaurus](https://github.com/AngelKitty/stegosaurus) | Stegosaurus is a Python steganography tool that embeds payloads within Python bytecode (pyc or pyo) files without altering runtime behavior or file size. |
| [stegoveritas](https://pypi.org/project/stegoveritas/) | Stegoveritas is a Python library for detecting steganography in images, primarily used for cybersecurity analysis. |
| [stegseek](https://github.com/RickdeJager/stegseek) | Stegseek is a fast steghide cracker for extracting hidden data from files using wordlist brute-force. |
| [stegsnow](https://packages.debian.org/search?keywords=stegsnow) | stegsnow is a steganography tool for hiding data in ASCII files, compatible with Debian-based systems. |
| [stegsolve](https://github.com/Giotino/stegsolve) | StegSolve is a Java-based steganography tool for analyzing and manipulating images to hide data, supporting zoom, drag-and-drop, and channel plane extraction. |
| [zsteg](https://rubygems.org/gems/zsteg) | zsteg detects hidden data in PNG and BMP files. |

## Web

| Tool | Description |
| :--- | :--- |
| [arjun](https://pypi.org/project/arjun/) | Arjun is an HTTP parameter discovery tool that finds valid parameters for URL endpoints using a large dictionary of 25,890 parameter names, supporting GET/POST requests and exporting results to various formats. |
| [beef](https://hub.docker.com/r/beefproject/beef) | BeEF is a penetration testing framework that hooks web browsers to launch directed command modules and further attacks from within the browser context. It is primarily used for assessing web application security. |
| [brakeman](https://rubygems.org/gems/brakeman) | Brakeman is a static analysis tool for detecting security vulnerabilities in Ruby on Rails applications. |
| [cariddi](https://github.com/edoardottt/cariddi) | cariddi is a Go-based tool for domain crawling and secret scanning, targeting web applications and infrastructure. |
| [clairvoyance](https://pypi.org/project/clairvoyance/) | Clairvoyance 2.5.5 is a Python tool to obtain GraphQL API schemas even if introspection is disabled, producing JSON format for use with other tools like GraphQL Voyager or InQL. |
| [CMSmap](https://github.com/dionach/CMSmap) | CMSmap is a Python-based CMS scanner that automates the detection of security flaws in WordPress, Joomla, Drupal, and Moodle. |
| [commix](https://pypi.org/project/commix/) | Automated OS command injection exploitation tool for web applications. |
| [corscanner](https://pypi.org/project/corscanner/) | corscanner is a Python tool for quickly identifying common CORS misconfigurations on websites, supporting various output formats and concurrency options. |
| [Corsy](https://github.com/s0md3v/Corsy) | Corsy is a lightweight CORS misconfiguration scanner for Python 3, targeting web applications to identify and report various CORS misconfigurations. |
| [crlfuzz](https://github.com/dwisiswant0/crlfuzz) | crlfuzz is a fast CRLF injection vulnerability scanner written in Go. |
| [dalfox](https://github.com/hahwul/dalfox) | Dalfox is an open-source XSS scanner and utility for automated vulnerability detection. |
| [dirsearch](https://pypi.org/project/dirsearch/) | dirsearch is a Python script for web directories and files discovery. |
| [droopescan](https://pypi.org/project/droopescan/) | droopescan is a plugin-based scanner for identifying issues with CMSs like Drupal, Wordpress, Moodle, and SilverStripe. |
| [feroxbuster](https://crates.io/crates/feroxbuster) | Feroxbuster is a fast, simple, recursive content discovery tool for web applications, primarily used in penetration testing and URL bruteforce. |
| [ffuf](https://github.com/ffuf/ffuf) | ffuf is a fast web fuzzer written in Go for content discovery, vhost discovery, parameter fuzzing, and POST data fuzzing. |
| [ghauri](https://github.com/r0oth3x49/ghauri) | An advanced cross-platform tool for automating SQL injection detection and exploitation targeting MySQL, MSSQL, Postgres, Oracle, and Access. |
| [git-dumper](https://pypi.org/project/git-dumper/) | git-dumper is a Python script for cloning private Git repositories without authentication. |
| [gobuster](https://github.com/OJ/gobuster) | Gobuster is a high-performance directory/file, DNS, and virtual host brute-forcing tool written in Go, designed for security professionals and penetration testers. |
| [Gopherus](https://github.com/tarunkant/Gopherus) | Gopherus generates Gopher payloads for exploiting SSRF and gaining RCE in various servers, supporting MySQL, PostgreSQL, FastCGI, Memcached, Redis, Zabbix, and SMTP. |
| [graphw00f](https://github.com/dolevf/graphw00f) | graphw00f is a GraphQL Server Engine Fingerprinting utility for security professionals to identify the technology behind a given GraphQL endpoint. |
| [Gxss](https://github.com/KathanP19/Gxss) | Gxss is a lightweight tool for checking reflecting parameters in URLs, supporting GET and POST methods, and can be used in bug bounty workflows. |
| [h2csmuggler](https://github.com/BishopFox/h2csmuggler) | h2csmuggler smuggles HTTP traffic past insecure HTTP/2 cleartext (h2c) proxy configurations, allowing bypass of proxy rules and access controls. |
| [jaeles](https://github.com/jaeles-project/jaeles) | Jaeles is a flexible web application scanner framework in Go, designed for automated bug bounty testing and security research. |
| [jsluice](https://github.com/BishopFox/jsluice) | jsluice extracts URLs, paths, secrets, and other interesting bits from JavaScript code. |
| [jwt_tool](https://github.com/ticarpi/jwt_tool) | jwt_tool is a Python toolkit for testing, tweaking, and cracking JSON Web Tokens, suitable for pentesters, CTF challengers, and developers. |
| [katana](https://github.com/projectdiscovery/katana) | Katana is a fast, configurable web crawling and spidering framework supporting standard and headless modes, JavaScript parsing, and customizable output formats. |
| [kr](https://github.com/assetnote/kiterunner) | kr is a Contextual Content Discovery Tool for web applications. |
| [kxss](https://github.com/Emoe/kxss) | kxss is a URL parameter scanner that identifies XSS vulnerabilities by testing unfiltered parameters. It outputs results in a format easier to parse for automated scripts. Target platform: Web applications. Protocol: HTTP/HTTPS. |
| [mitmproxy2swagger](https://pypi.org/project/mitmproxy2swagger/) | Converts mitmproxy capture files to Swagger/OpenAPI specifications for API documentation. |
| [nikto](https://github.com/sullo/nikto) | Nikto is an open-source web server scanner that detects vulnerabilities on web servers. It is primarily used for security assessments and penetration testing. Target platform: Web servers. Protocol: HTTP/HTTPS. |
| [nomore403](https://github.com/devploit/nomore403) | nomore403 is a command-line tool for testing HTTP access-control bypasses and parser inconsistencies around 401, 403, and related responses. It automates request mutations, captures baseline responses, and highlights likely bypasses with replayable evidence. |
| [NoSQLMap](https://github.com/codingo/NoSQLMap) | NoSQLMap is an open-source Python tool for auditing and automating injection attacks on NoSQL databases and web applications, primarily targeting MongoDB and CouchDB. |
| [nuclei](https://github.com/projectdiscovery/nuclei) | Nuclei is a fast, customizable vulnerability scanner using YAML-based templates, designed to detect real-world vulnerabilities with zero false positives. |
| [Oralyzer](https://github.com/r0075h3ll/Oralyzer) | Oralyzer is a Python tool for detecting open redirects, CRLF injection, and DOM XSS vulnerabilities on websites. |
| [PadBuster](https://github.com/AonCyberLabs/PadBuster) | Automated script for performing Padding Oracle attacks on web applications. |
| [paramspider](https://github.com/devanshbatham/ParamSpider) | paramspider is a tool for mining URLs from Web Archives to aid in bug hunting, fuzzing, and further probing. It targets web applications and protocols. |
| [phpggc](https://github.com/ambionics/phpggc) | phpggc is a PHP library and tool for generating unserialize() payloads for various frameworks and libraries, aiding in exploit development and security testing. |
| [PhpSploit](https://github.com/nil0x42/phpsploit) | PhpSploit is a full-featured C2 framework that silently persists on web servers via a polymorphic PHP oneliner, enabling stealthy command-and-control communications. |
| [pp-finder](https://github.com/yeswehack/pp-finder) | pp-finder is a JavaScript prototype pollution finder tool that helps hackers identify potential prototype pollution candidates in code by parsing and analyzing the source code. |
| [proxify](https://github.com/projectdiscovery/proxify) | A versatile proxy for capturing, manipulating, and replaying HTTP/HTTPS traffic, supporting MITM, SOCKS5, and non-HTTP protocols. |
| [raccoon-scanner](https://pypi.org/project/raccoon-scanner/) | raccoon-scanner is a Python-based network scanner for identifying open ports and services on a target host. |
| [smuggler](https://github.com/defparam/smuggler) | Smuggler is an HTTP Request Smuggling / Desync testing tool written in Python 3 for identifying potential desync issues in web applications. |
| [sqlmap](https://pypi.org/project/sqlmap/) | sqlmap is an open-source tool for automating SQL injection and database takeover, supporting multiple platforms and protocols. |
| [sslyze](https://pypi.org/project/sslyze/) | sslyze is an open-source tool for auditing SSL/TLS configurations of servers. |
| [SSRFmap](https://github.com/swisskyrepo/SSRFmap) | SSRFmap is an automatic SSRF fuzzer and exploitation tool that takes a Burp request file and parameter to fuzz, targeting server-side request forgery vulnerabilities. |
| [symfony-exploits](https://github.com/ambionics/symfony-exploits) | Exploits targeting Symfony, focusing on secret fragments. |
| [testssl.sh](https://github.com/drwetter/testssl.sh) | testssl.sh is a command-line tool for assessing SSL/TLS security on servers. It checks for vulnerabilities and supports multiple protocols including TLS 1.3. Target platform: Unix-like systems. Primary use case: Security audits and penetration testing of web servers. |
| [tlsx](https://github.com/projectdiscovery/tlsx) | tlsx is a fast and configurable TLS grabber for data collection and analysis, supporting multiple modes, probes, and output formats. |
| [tomcatwardeployer](https://github.com/mgeeky/tomcatwardeployer) | tomcatWarDeployer is a penetration testing tool for Apache Tomcat that automatically deploys a JSP backdoor WAR package and provides a reverse TCP payload connection or bind shell. |
| [tplmap](https://github.com/epinna/tplmap) | Tplmap is a tool for detecting and exploiting Server-Side Template Injection (SSTI) vulnerabilities in web applications, supporting multiple template engines and providing techniques for remote code execution, file manipulation, and more. |
| [wafw00f](https://pypi.org/project/wafw00f/) | WAFW00F is a Python tool for detecting and fingerprinting web application firewalls (WAFs) by analyzing HTTP responses and using simple logic to identify various WAF solutions. |
| [webanalyze](https://github.com/rverton/webanalyze) | webanalyze is a Go-based tool that automates the process of identifying and listing technologies used on websites, similar to Wappalyzer, for security and enumeration purposes. |
| [whatweb](https://packages.debian.org/search?keywords=whatweb) | Whatweb is a web scanner that identifies technologies used on websites, such as CMS, JavaScript frameworks, and server software. |
| [wpscan](https://rubygems.org/gems/wpscan) | WPScan is a black box WordPress vulnerability scanner targeting WordPress websites. |
| [x8](https://crates.io/crates/x8) | x8 is a hidden parameters discovery suite for web security reconnaissance and content discovery, compatible with the Rust programming language and available via Cargo. |
| [xsrfprobe](https://pypi.org/project/xsrfprobe/) | XSRFProbe is a powerful CSRF audit and exploitation toolkit that detects vulnerabilities, bypasses, and generates proof of concepts for web applications. |
| [XSStrike](https://github.com/s0md3v/XSStrike) | XSStrike is an advanced XSS scanner with multi-threaded crawling, context analysis, and intelligent payload generation for detecting and exploiting reflected and DOM XSS vulnerabilities. |
| [XXEinjector](https://github.com/enjoiz/XXEinjector) | XXEinjector automates exploiting XML External Entity (XXE) vulnerabilities using direct and out-of-band methods. |
| [ysoserial](https://github.com/frohoff/ysoserial) | A Java tool for generating payloads that exploit unsafe object deserialization in applications, targeting various libraries and JRE versions. |
| [zaproxy](https://github.com/zaproxy/zaproxy) | ZAPROXY is an open-source web application security scanner that automatically finds vulnerabilities during development and testing, suitable for both beginners and experienced pentesters. |

## Wireless

| Tool | Description |
| :--- | :--- |
| [aircrack-ng](https://packages.debian.org/search?keywords=aircrack-ng) | Aircrack-ng is a suite of tools for wireless network security auditing, primarily used for cracking WEP and WPA keys. |
| [airgeddon](https://github.com/v1s1t0r1sh3r3/airgeddon) | A multi-use bash script for Linux systems to audit wireless networks, supporting WEP, WPA, WPA2, and WPA3. |
| [angryoxide](https://github.com/Ragnt/AngryOxide) | AngryOxide is a Rust-based 802.11 attack tool for capturing EAPOL messages and conducting automated attacks, targeting specific MAC addresses or SSIDs, with features like auto-hunt, whitelist protection, and geo-fencing. |
| [asleap](https://packages.debian.org/search?keywords=asleap) | asleap is a tool for capturing and analyzing 802.11 WEP keys using the LEAP authentication protocol. |
| [avrdude](https://packages.debian.org/search?keywords=avrdude) | avrdude is a software tool for programming Atmel AVR microcontrollers via a serial connection. |
| [bluez](https://packages.debian.org/search?keywords=bluez) | Bluez is a Linux daemon for Bluetooth protocol stack, providing tools for managing Bluetooth devices and connections. |
| [btlejack](https://pypi.org/project/btlejack/) | btlejack is a Bluetooth Low Energy (BLE) sniffer and analyzer for Linux. |
| [bully](https://packages.debian.org/search?keywords=bully) | Bully is a C-based implementation of the WPS brute force attack targeting various platforms and architectures. |
| [cowpatty](https://packages.debian.org/search?keywords=cowpatty) | cowpatty is a brute-force WPA dictionary attack tool for Linux. |
| [crackle](https://packages.debian.org/search?keywords=crackle) | crackle exploits a flaw in the BLE pairing process that allows an attacker to guess or very quickly brute force the Temporary Key. With the TK and other data collected from the pairing process, the Short Term Key and later the Long Term Key can be collected. |
| [eaphammer](https://github.com/s0lst1c3/eaphammer) | eaphammer is a toolkit for performing targeted evil twin attacks against WPA2-Enterprise networks, designed for use in wireless assessments and red team engagements. |
| [fern-wifi-cracker](https://packages.debian.org/search?keywords=fern-wifi-cracker) | Fern-Wifi-Cracker is a graphical tool for auditing Wi-Fi networks, primarily used for security assessments and penetration testing on Linux platforms. |
| [fluxion](https://github.com/FluxionNetwork/fluxion) | Fluxion is a security auditing and social-engineering tool for capturing WPA/WPA2 handshakes using a captive portal attack on Linux-based systems, particularly Kali Linux. |
| [gnuradio](https://packages.debian.org/search?keywords=gnuradio) | GNU Radio is a free software development toolkit for software defined radios, enabling the creation of custom radio hardware and software applications. |
| [gqrx-sdr](https://packages.debian.org/search?keywords=gqrx-sdr) | gqrx-sdr is a software-defined radio receiver for Linux, supporting various radio protocols and frequency bands. |
| [hackrf](https://packages.debian.org/search?keywords=hackrf) | HackRF is a software-defined radio (SDR) peripheral for radio communication and analysis, supporting various radio protocols and platforms. |
| [hcxdumptool](https://packages.debian.org/search?keywords=hcxdumptool) | hcxdumptool is a small tool to capture packets from WLAN devices, primarily used for security testing and analysis. |
| [hcxtools](https://packages.debian.org/search?keywords=hcxtools) | hcxtools: Tools for converting captures to use with hashcat or John the Ripper, supporting various protocols and platforms. |
| [horst](https://packages.debian.org/search?keywords=horst) | Horst is a highly optimized radio scanning tool for Linux. |
| [hostapd-mana](https://github.com/sensepost/hostapd-mana) | hostapd-mana: SensePost's modified hostapd for WiFi attacks, targeting WPA2 networks. |
| [iw](https://packages.debian.org/search?keywords=iw) | iw is a command-line tool for configuring Linux wireless devices. |
| [kismet](https://packages.debian.org/search?keywords=kismet) | Kismet is a wireless network detector, sniffer, and intrusion detection system. |
| [libnfc-crypto1-crack](https://github.com/droidnewbie2/acr122uNFC) | libnfc-crypto1-crack is a tool for performing hardnested attacks on Mifare Classic Plus tags using LibNFC USB readers. |
| [libnfc-dev](https://packages.debian.org/search?keywords=libnfc-dev) | libnfc-dev: Development files for the Near Field Communication (NFC) library, enabling software development for NFC devices on various platforms. |
| [mdk4](https://packages.debian.org/search?keywords=mdk4) | mdk4 is a wireless attack tool for IEEE 802.11 networks, primarily used for security testing and auditing. |
| [mfcuk](https://packages.debian.org/search?keywords=mfcuk) | mfcuk is a command-line tool for MiFare Classic smartcard cloning and analysis, targeting the MiFare Classic protocol on various platforms. |
| [mfdread](https://github.com/zhovner/mfdread) | mfdread is a Python script for parsing Mifare 1k/4k and Mifare Mini dumps into human-readable format, typically used with tools like mfterm or mfoc. |
| [mfoc](https://packages.debian.org/search?keywords=mfoc) | mfoc is a command-line tool for offline cracking of MIFARE Classic RFID cards. |
| [mousejack](https://github.com/BastilleResearch/mousejack) | MouseJack is a tool for discovering and researching vulnerabilities in wireless mice using the Bluetooth protocol. |
| [pixiewps](https://packages.debian.org/search?keywords=pixiewps) | Offline WPS password brute-forcing tool for various platforms. |
| [proxmark3](https://github.com/RfidResearchGroup/proxmark3) | proxmark3 is an open-source tool for RFID analysis and hacking, supporting protocols like ISO14443A, ISO14443B, and MIFARE, and enabling cloning, simulation, and penetration testing of RFID tags. |
| [PSKracker](https://github.com/soxrok2212/PSKracker) | PSKracker is a C-based tool for generating default passwords and WPS pins for various Wi-Fi models, primarily for security testing and auditing. |
| [reaver](https://packages.debian.org/search?keywords=reaver) | Reaver is a brute force attack tool targeting the Wi-Fi Protected Setup (WPS) PIN number for WPA/WPA2 networks. |
| [rfkill](https://packages.debian.org/search?keywords=rfkill) | rfkill is a command-line tool for managing wireless devices, enabling or disabling them. |
| [rtl-433](https://packages.debian.org/search?keywords=rtl-433) | rtl-433 is a tool for decoding 433.9 MHz radio frequency data, commonly used for weather stations, security systems, and other low-power devices. |
| [sipvicious](https://pypi.org/project/sipvicious/) | sipvicious is a Python library for SIP testing and analysis, primarily used for security assessments and penetration testing. |
| [spooftooph](https://packages.debian.org/search?keywords=spooftooph) | spooftooph is a network security tool for detecting and preventing IP spoofing attacks. |
| [wifiphisher](https://github.com/wifiphisher/wifiphisher) | Wifiphisher is a rogue Access Point framework for conducting Wi-Fi security testing and penetration testing, enabling users to perform targeted Wi-Fi association attacks and mount phishing attacks to capture credentials or infect devices. |
| [wifipumpkin3](https://github.com/P0cL4bs/wifipumpkin3) | wifipumpkin3 is a Python-based framework for conducting rogue access point and man-in-the-middle attacks, targeting Linux platforms. |
| [wifite2](https://github.com/derv82/wifite2) | wifite2 is a Python script for auditing wireless networks, automating the process of capturing and cracking WPS, WPA, and WEP passwords using various methods. It is designed for Kali Linux and requires a wireless card with monitor mode and packet injection capabilities. |
| [wireless-tools](https://packages.debian.org/search?keywords=wireless-tools) | wireless-tools: Linux Wireless Extensions manipulation utilities for network configuration and management. |
<!-- TOOLS:END -->
