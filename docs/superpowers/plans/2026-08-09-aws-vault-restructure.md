# AWS Obsidian Vault Restructure Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reorganize the AWS Obsidian vault from vendor-prefixed flat folders (`Amazon/`, `AWS/`, `Cloud/`, `EC2/`, `S3/`) into 13 numbered domain folders with a home index, a per-folder index note, consistent `#AWS #Service #<Domain>` / `#AWS #Concept #<Domain>` tagging, and full wikilink navigation.

**Architecture:** A single Python tool (`tools/retag.py`) plus a TSV manifest (`tools/moves.tsv`) performs all 91 file moves, retags each note, fixes `###` headings, and remaps wikilinks globally. Tasks then create 71 new notes, 13 index notes, and `Home.md`. Final task verifies counts and link integrity.

**Tech Stack:** Obsidian vault (markdown + tag lines, no YAML frontmatter in notes), Python 3, bash `git mv`.

**Plan location:** `docs/superpowers/plans/2026-08-09-aws-vault-restructure.md`

## Global Constraints

- Working dir is the vault root: `/Users/lizard/Library/Mobile Documents/iCloud~md~obsidian/Documents/AWS`
- Do NOT touch `.trash/`, `.git/`, `.obsidian/`, `.makemd/`, `.space/`, `Tags/`
- Tag format, line 1 of every note: `#AWS #Service #<Domain>` for services, `#AWS #Concept #<Domain>` for concepts
- Heading format: `### <Note Basename>` (exact basename, no extension)
- Description: 2–4 sentence plain paragraph under the heading
- `### Related Services` section: bullets `- [[Wikilink]]: <1-line blurb>`; every existing related-service link preserved, renamed targets updated
- `### Related Concepts` section: bullets `- <Concept>: <1-line blurb>`
- Wikilinks use the basename only (no path prefix): `[[S3]]`, `[[Lambda]]`, `[[Security Groups vs NACLs]]`
- Every `.md` in a folder must be linked from that folder's index note; every index note linked from `Home.md`
- Domain folder names (exact): `01 Concepts`, `02 Compute`, `03 Storage`, `04 Database`, `05 Networking`, `06 Security`, `07 Analytics`, `08 Machine Learning`, `09 Integration`, `10 Management`, `11 Developer Tools`, `12 Migration`, `13 Business`
- Domain tags (exact): Concept, Compute, Storage, Database, Networking, Security, Analytics, ML, Integration, Management, DevTools, Migration, Business
- Final `.md` counts per domain (incl. index): 25, 16, 22, 14, 13, 21, 8, 11, 7, 10, 11, 10, 7; plus `Home.md` = 177 total
- Deleted hub notes: `AWS/AWS.md`, `Amazon/Amazon.md`, `S3/S3.md`
- New notes live in their domain folder and are NOT in `tools/moves.tsv` (they are written by tasks with final tags/headings already correct)
- Existing notes that are not deep-dived: content preserved verbatim; only tag line + heading rewritten

---

## Canonical File Map (authoritative)

Old path → New path (these are the `tools/moves.tsv` rows; tag = domain tag; kind = `Service`|`Concept`):

| Old | New | Tag | Kind |
|---|---|---|---|
| AWS/AWS Shared Responsibility Model.md | 01 Concepts/Shared Responsibility Model.md | Concept | Concept |
| AWS/AWS Architecture Design Principles.md | 01 Concepts/Architecture Design Principles.md | Concept | Concept |
| AWS/AWS Migration Strategies.md | 01 Concepts/Migration Strategies.md | Concept | Concept |
| AWS/AWS Cloud Adoption Framework (CAF).md | 01 Concepts/CAF.md | Concept | Concept |
| AWS/AWS Well-Architected Framework.md | 01 Concepts/Well-Architected Framework.md | Concept | Concept |
| AWS/AWS rePost.md | 01 Concepts/rePost.md | Concept | Service |
| AWS/AWS Customer Carbon Footprint Tool (CCFT).md | 01 Concepts/CCFT.md | Concept | Service |
| Cloud/Infrastructure as a Service (IaaS).md | 01 Concepts/IaaS.md | Concept | Concept |
| Cloud/Platform as a Service (PaaS).md | 01 Concepts/PaaS.md | Concept | Concept |
| Cloud/Software as a Service (SaaS).md | 01 Concepts/SaaS.md | Concept | Concept |
| Cloud/Infrastructure as Code (IaC).md | 01 Concepts/IaC.md | Concept | Concept |
| EC2/Amazon EC2.md | 02 Compute/EC2.md | Compute | Service |
| AWS/AWS Lambda.md | 02 Compute/Lambda.md | Compute | Service |
| AWS/AWS Elastic Beanstalk.md | 02 Compute/Elastic Beanstalk.md | Compute | Service |
| AWS/AWS Fargate.md | 02 Compute/Fargate.md | Compute | Service |
| AWS/AWS Auto Scaling.md | 02 Compute/Auto Scaling.md | Compute | Service |
| AWS/AWS Outposts.md | 02 Compute/Outposts.md | Compute | Service |
| Amazon/Amazon Lightsail.md | 02 Compute/Lightsail.md | Compute | Service |
| S3/Amazon S3.md | 03 Storage/S3.md | Storage | Service |
| S3/S3 Access Control.md | 03 Storage/S3 Access Control.md | Storage | Service |
| S3/S3 Encryption.md | 03 Storage/S3 Encryption.md | Storage | Service |
| S3/S3 Event Notifications.md | 03 Storage/S3 Event Notifications.md | Storage | Service |
| S3/S3 Glacier.md | 03 Storage/S3 Glacier.md | Storage | Service |
| S3/S3 Intelligent-Tiering.md | 03 Storage/S3 Intelligent-Tiering.md | Storage | Service |
| S3/S3 Lifecycle.md | 03 Storage/S3 Lifecycle.md | Storage | Service |
| S3/S3 One Zone-IA.md | 03 Storage/S3 One Zone-IA.md | Storage | Service |
| S3/S3 Replication.md | 03 Storage/S3 Replication.md | Storage | Service |
| S3/S3 Select.md | 03 Storage/S3 Select.md | Storage | Service |
| S3/S3 Standard-Infrequent Access (IA).md | 03 Storage/S3 Standard-Infrequent Access (IA).md | Storage | Service |
| S3/S3 Standard.md | 03 Storage/S3 Standard.md | Storage | Service |
| S3/S3 Versioning.md | 03 Storage/S3 Versioning.md | Storage | Service |
| Amazon/Amazon EFS.md | 03 Storage/EFS.md | Storage | Service |
| Amazon/Amazon FSx File Gateway.md | 03 Storage/FSx File Gateway.md | Storage | Service |
| AWS/AWS Backup.md | 03 Storage/Backup.md | Storage | Service |
| AWS/AWS DataSync.md | 03 Storage/DataSync.md | Storage | Service |
| Amazon/Amazon RDS.md | 04 Database/RDS.md | Database | Service |
| Amazon/Amazon Aurora.md | 04 Database/Aurora.md | Database | Service |
| Amazon/Amazon DynamoDB.md | 04 Database/DynamoDB.md | Database | Service |
| Amazon/Amazon Redshift.md | 04 Database/Redshift.md | Database | Service |
| Amazon/Amazon Neptune.md | 04 Database/Neptune.md | Database | Service |
| Amazon/Amazon VPC.md | 05 Networking/VPC.md | Networking | Service |
| Amazon/Amazon CloudFront.md | 05 Networking/CloudFront.md | Networking | Service |
| Amazon/Amazon Route 53.md | 05 Networking/Route 53.md | Networking | Service |
| Amazon/Amazon API Gateway.md | 05 Networking/API Gateway.md | Networking | Service |
| AWS/AWS Direct Connect.md | 05 Networking/Direct Connect.md | Networking | Service |
| AWS/AWS IAM.md | 06 Security/IAM.md | Security | Service |
| AWS/AWS Key Management Service (KMS).md | 06 Security/KMS.md | Security | Service |
| AWS/AWS Security Token Service (STS).md | 06 Security/STS.md | Security | Service |
| AWS/AWS Shield.md | 06 Security/Shield.md | Security | Service |
| AWS/AWS Artifact.md | 06 Security/Artifact.md | Security | Service |
| AWS/AWS CloudTrail.md | 06 Security/CloudTrail.md | Security | Service |
| AWS/AWS Config.md | 06 Security/Config.md | Security | Service |
| Amazon/Amazon GuardDuty.md | 06 Security/GuardDuty.md | Security | Service |
| Amazon/Amazon Inspector.md | 06 Security/Inspector.md | Security | Service |
| Amazon/Amazon Macie.md | 06 Security/Macie.md | Security | Service |
| Amazon/Amazon Detective.md | 06 Security/Detective.md | Security | Service |
| Amazon/Amazon Cognito.md | 06 Security/Cognito.md | Security | Service |
| Amazon/Amazon Athena.md | 07 Analytics/Athena.md | Analytics | Service |
| Amazon/Amazon Kinesis.md | 07 Analytics/Kinesis.md | Analytics | Service |
| Amazon/Amazon QuickSight.md | 07 Analytics/QuickSight.md | Analytics | Service |
| AWS/AWS Glue.md | 07 Analytics/Glue.md | Analytics | Service |
| Amazon/Amazon SageMaker.md | 08 Machine Learning/SageMaker.md | ML | Service |
| Amazon/Amazon Rekognition.md | 08 Machine Learning/Rekognition.md | ML | Service |
| Amazon/Amazon Comprehend.md | 08 Machine Learning/Comprehend.md | ML | Service |
| Amazon/Amazon Polly.md | 08 Machine Learning/Polly.md | ML | Service |
| Amazon/Amazon Transcribe.md | 08 Machine Learning/Transcribe.md | ML | Service |
| Amazon/Amazon Lex.md | 08 Machine Learning/Lex.md | ML | Service |
| Amazon/Amazon Kendra.md | 08 Machine Learning/Kendra.md | ML | Service |
| Amazon/Amazon SQS.md | 09 Integration/SQS.md | Integration | Service |
| Amazon/Amazon SNS.md | 09 Integration/SNS.md | Integration | Service |
| Amazon/Amazon EventBridge.md | 09 Integration/EventBridge.md | Integration | Service |
| Amazon/Amazon CloudWatch.md | 10 Management/CloudWatch.md | Management | Service |
| AWS/AWS CloudFormation.md | 10 Management/CloudFormation.md | Management | Service |
| AWS/AWS Management Console.md | 10 Management/Management Console.md | Management | Service |
| AWS/AWS CodeCommit.md | 11 Developer Tools/CodeCommit.md | DevTools | Service |
| AWS/AWS CodeBuild.md | 11 Developer Tools/CodeBuild.md | DevTools | Service |
| AWS/AWS CodeDeploy.md | 11 Developer Tools/CodeDeploy.md | DevTools | Service |
| AWS/AWS CodePipeline.md | 11 Developer Tools/CodePipeline.md | DevTools | Service |
| AWS/AWS CodeStar.md | 11 Developer Tools/CodeStar.md | DevTools | Service |
| AWS/AWS Application Composer.md | 11 Developer Tools/Application Composer.md | DevTools | Service |
| AWS/AWS CLI.md | 11 Developer Tools/AWS CLI.md | DevTools | Service |
| AWS/AWS Application Migration Service (MGN).md | 12 Migration/MGN.md | Migration | Service |
| AWS/AWS Application Discovery Service.md | 12 Migration/Application Discovery Service.md | Migration | Service |
| AWS/AWS Database Migration Service (DMS).md | 12 Migration/DMS.md | Migration | Service |
| AWS/AWS Schema Conversion Tool (SCT).md | 12 Migration/SCT.md | Migration | Service |
| AWS/AWS Migration Hub.md | 12 Migration/Migration Hub.md | Migration | Service |
| AWS/AWS Snowball.md | 12 Migration/Snowball.md | Migration | Service |
| AWS/AWS Snowball Edge.md | 12 Migration/Snowball Edge.md | Migration | Service |
| AWS/AWS Snowcone.md | 12 Migration/Snowcone.md | Migration | Service |
| Amazon/Amazon Connect.md | 13 Business/Connect.md | Business | Service |
| Amazon/Amazon Elastic Transcoder.md | 13 Business/Elastic Transcoder.md | Business | Service |

---

### Task 1: Scaffolding — folders, tools, manifest, home index

**Files:**
- Create: `tools/retag.py`
- Create: `tools/moves.tsv` (all 91 rows from the Canonical File Map, tab-separated, one header line `old\tnew\ttag\tkind`)
- Delete: `AWS/AWS.md`, `Amazon/Amazon.md`, `S3/S3.md` (after the move step)
- Create: `Home.md` (vault root)
- Create: empty index stubs are NOT created here — each domain task creates its own index note

**Interfaces:**
- Produces: `tools/retag.py` (run by every later task — idempotent), `tools/moves.tsv`, `Home.md`
- Later tasks consume the manifest + tool exactly as created here

- [ ] **Step 1: Create `tools/retag.py`**

```python
#!/usr/bin/env python3
"""Rewrite AWS vault: move files per manifest, retag line 1, fix ### heading, remap wikilinks."""
import os
import subprocess
import sys

ROOT = "/Users/lizard/Library/Mobile Documents/iCloud~md~obsidian/Documents/AWS"
MANIFEST = os.path.join(ROOT, "tools", "moves.tsv")
SKIP_DIRS = {".git", ".trash", ".obsidian", ".makemd", ".space", "Tags", "tools", "docs"}


def load_manifest():
    moves = []
    with open(MANIFEST, encoding="utf-8") as fh:
        for line in fh:
            line = line.rstrip("\n")
            if not line or line.startswith("#"):
                continue
            old, new, tag, kind = line.split("\t")
            moves.append((old, new, tag, kind))
    return moves


def relink_map(moves):
    m = {}
    for old, new, tag, kind in moves:
        old_base = os.path.splitext(os.path.basename(old))[0]
        new_base = os.path.splitext(os.path.basename(new))[0]
        if old_base != new_base:
            m[old_base] = new_base
    return m


def retag_content(path, name, tag, kind):
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().split("\n")
    if lines:
        lines[0] = f"#AWS #{kind} #{tag}"
    for i, ln in enumerate(lines):
        if ln.startswith("### "):
            lines[i] = f"### {name}"
            break
    return "\n".join(lines)


def main():
    moves = load_manifest()
    rmap = relink_map(moves)
    for old, new, tag, kind in moves:
        oldp = os.path.join(ROOT, old)
        newp = os.path.join(ROOT, new)
        os.makedirs(os.path.dirname(newp), exist_ok=True)
        if os.path.exists(oldp):
            subprocess.run(["git", "mv", oldp, newp], check=False)
            if not os.path.exists(newp) and os.path.exists(oldp):
                os.rename(oldp, newp)
        if os.path.exists(newp):
            name = os.path.splitext(os.path.basename(new))[0]
            content = retag_content(newp, name, tag, kind)
            for oldb, newb in rmap.items():
                content = content.replace(f"[[{oldb}", f"[[{newb}")
            with open(newp, "w", encoding="utf-8") as fh:
                fh.write(content)
    for dirpath, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for fn in files:
            if not fn.endswith(".md"):
                continue
            p = os.path.join(dirpath, fn)
            with open(p, encoding="utf-8") as fh:
                c = fh.read()
            changed = False
            for oldb, newb in rmap.items():
                if f"[[{oldb}" in c:
                    c = c.replace(f"[[{oldb}", f"[[{newb}")
                    changed = True
            if changed:
                with open(p, "w", encoding="utf-8") as fh:
                    fh.write(c)
    print("retag.py complete: moved/retagged/linked")


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Create `tools/moves.tsv`**

Every row from the Canonical File Map table, tab-separated, with header line:

```
old	new	tag	kind
```

First row (verify with `python3 tools/retag.py` later that one row works end-to-end):

```
AWS/AWS Shared Responsibility Model.md	01 Concepts/Shared Responsibility Model.md	Concept	Concept
```

(Write all 91 rows exactly as in the Canonical File Map table.)

- [ ] **Step 3: Delete hub notes before moves to avoid filename collisions**

```bash
rm -f "S3/S3.md"
git rm --ignore-unmatch "S3/S3.md"
```

Do NOT delete `AWS/AWS.md` or `Amazon/Amazon.md` yet — they are deleted in Task 2 after `tools/retag.py` has run (they are not in the manifest, so no collision; deletion order is not critical, but `S3/S3.md` MUST be removed before `S3/Amazon S3.md → S3.md`).

- [ ] **Step 4: Run `tools/retag.py` and verify the first moves**

```bash
python3 tools/retag.py
ls "01 Concepts" | head
```

Expected: `01 Concepts/` contains `Shared Responsibility Model.md` (tag `#AWS #Concept #Concept`, heading `### Shared Responsibility Model`).

- [ ] **Step 5: Create `Home.md`** (vault root)

```markdown
#AWS #MOC
### AWS — Home

Central index for the AWS study vault.

## Domains

- [[01 Concepts]] — cloud fundamentals, AWS concepts, pricing, and cost tools
- [[02 Compute]] — EC2, Lambda, containers, and serverless
- [[03 Storage]] — S3, EBS, EFS, backup, and transfer
- [[04 Database]] — relational, NoSQL, and analytics databases
- [[05 Networking]] — VPC, CDN, DNS, and APIs
- [[06 Security]] — identity, access, encryption, and threat detection
- [[07 Analytics]] — query, streaming, and BI
- [[08 Machine Learning]] — AI/ML services
- [[09 Integration]] — queues, topics, and event routing
- [[10 Management]] — monitoring, provisioning, and governance
- [[11 Developer Tools]] — CI/CD and developer services
- [[12 Migration]] — migrate and transfer tools
- [[13 Business]] — productivity and end-user applications
```

Note: the index notes linked above are named exactly `<Domain>.md`? NO — the index notes are named `Index.md` inside each folder. Wikilinks resolve by basename, so `[[Index]]` would be ambiguous. Therefore each index note is named `<Folder Number> <Domain>.md`? NO — simplest unambiguous scheme: name each folder's index note `<Domain>.md`? That would clash with the folder name only, which is fine (Obsidian links by note). Decision: **each index note is named `Index.md`** inside its folder, and `Home.md` links to them using full paths: `[[01 Concepts/Index|Concepts]]`. Update `Home.md` links accordingly (see Step 6).
```

The index-note naming decision is finalized in Step 6 below — replace Step 5's link list with the correct form.

- [ ] **Step 6: Finalize index-note naming + correct `Home.md`**

Index notes are named `Index.md` in each folder (unambiguous, per-folder). `Home.md` must link to each with a path-qualified alias:

```markdown
#AWS #MOC
### AWS — Home

Central index for the AWS study vault.

## Domains

- [[01 Concepts/Index|Concepts]] — cloud fundamentals, AWS concepts, pricing, and cost tools
- [[02 Compute/Index|Compute]] — EC2, Lambda, containers, and serverless
- [[03 Storage/Index|Storage]] — S3, EBS, EFS, backup, and transfer
- [[04 Database/Index|Database]] — relational, NoSQL, and analytics databases
- [[05 Networking/Index|Networking]] — VPC, CDN, DNS, and APIs
- [[06 Security/Index|Security]] — identity, access, encryption, and threat detection
- [[07 Analytics/Index|Analytics]] — query, streaming, and BI
- [[08 Machine Learning/Index|Machine Learning]] — AI/ML services
- [[09 Integration/Index|Integration]] — queues, topics, and event routing
- [[10 Management/Index|Management]] — monitoring, provisioning, and governance
- [[11 Developer Tools/Index|Developer Tools]] — CI/CD and developer services
- [[12 Migration/Index|Migration]] — migrate and transfer tools
- [[13 Business/Index|Business]] — productivity and end-user applications
```

- [ ] **Step 7: Delete remaining hub notes**

```bash
git rm --ignore-unmatch "AWS/AWS.md" "Amazon/Amazon.md"
```

- [ ] **Step 8: Verify and commit**

```bash
git add -A
git status --short | head -30
```

Expected: moved notes staged as renames; `Home.md`, `tools/` added; hub files deleted.

```bash
git commit -m "chore: scaffold vault restructure (tools, manifest, home index)"
```

---

### Task 2: 01 Concepts — moves + 13 new notes + index

**Files:**
- Move (via `tools/retag.py`): all 11 Concept rows from the Canonical File Map
- Create: `01 Concepts/Cloud Computing Overview.md`, `01 Concepts/AWS Global Infrastructure.md`, `01 Concepts/Regions & Availability Zones.md`, `01 Concepts/Edge Locations.md`, `01 Concepts/AWS Pricing Models.md`, `01 Concepts/AWS Support Plans.md`, `01 Concepts/Total Cost of Ownership.md`, `01 Concepts/AWS Budgets.md`, `01 Concepts/AWS Cost Explorer.md`, `01 Concepts/AWS Account & Root User.md`, `01 Concepts/AWS Free Tier.md`, `01 Concepts/AWS Support.md`, `01 Concepts/AWS Well-Architected Tool.md`
- Create: `01 Concepts/Index.md`

**Interfaces:**
- Consumes: `tools/retag.py`, `tools/moves.tsv`
- Produces: 13 concept notes with tags `#AWS #Concept #Concept` or `#AWS #Service #Concept` (per note below); `01 Concepts/Index.md` (name `Index.md`, links all 24 notes)

- [ ] **Step 1: Run the move tool for Concepts**

```bash
python3 tools/retag.py
ls "01 Concepts"
```

Expected: 11 moved notes present with corrected tags/headings.

- [ ] **Step 2: Create the 13 new Concept notes** (each full file):

`01 Concepts/Cloud Computing Overview.md`:
```markdown
#AWS #Concept #Concept
### Cloud Computing Overview

Cloud computing delivers on-demand IT resources over the internet with pay-as-you-go pricing. AWS provides three primary service models — IaaS, PaaS, and SaaS — alongside global infrastructure for low-latency delivery. Key benefits include elasticity, economies of scale, and reduced capital expenditure.

### Related Services

- [[AWS Global Infrastructure]]: The physical regions and edge locations that power cloud delivery.
- [[Regions & Availability Zones]]: Geographic distribution for resilience and low latency.

### Related Concepts

- IaaS: Virtualized compute, storage, and networking on demand.
- PaaS: Managed platforms for application deployment.
- SaaS: Ready-to-use software delivered over the internet.
- [[Shared Responsibility Model]]: Splits security duties between AWS and the customer.
```

`01 Concepts/AWS Global Infrastructure.md`:
```markdown
#AWS #Concept #Concept
### AWS Global Infrastructure

The physical footprint of AWS spanning regions, Availability Zones (AZs), and edge locations. Regions are independent geographic areas; each region contains multiple AZs, and edge locations cache content closer to users. This design supports high availability, disaster recovery, and low-latency delivery.

### Related Services

- [[Regions & Availability Zones]]: The core building blocks of the global footprint.
- [[Edge Locations]]: PoPs that accelerate content delivery.
- [[CloudFront]]: CDN that uses edge locations.

### Related Concepts

- High Availability: Redundant infrastructure across AZs.
- Disaster Recovery: Region replication for resilience.
- Latency: Reduced by geographic distribution.
```

`01 Concepts/Regions & Availability Zones.md`:
```markdown
#AWS #Concept #Concept
### Regions & Availability Zones

Regions are separate geographic areas containing two or more Availability Zones. AZs are isolated data centers within a region with independent power, networking, and cooling, connected by low-latency links. Deploying across AZs provides fault tolerance and high availability.

### Related Services

- [[EC2]]: Places instances in specific AZs.
- [[VPC]]: Spans AZs within a region.
- [[RDS Multi-AZ]]: Replicates databases across AZs.

### Related Concepts

- [[AWS Global Infrastructure]]: The overall physical layout.
- Fault Tolerance: Survives single-AZ failure.
- Low Latency: Data centers close to users.
```

`01 Concepts/Edge Locations.md`:
```markdown
#AWS #Concept #Concept
### Edge Locations

Edge locations are points of presence (PoPs) distributed around the world that cache content and accelerate delivery. Services like CloudFront and AWS Global Accelerator use them to serve users from the nearest location, reducing latency and improving throughput.

### Related Services

- [[CloudFront]]: CDN serving cached content from edge locations.
- [[AWS Global Accelerator]]: Routes traffic through edge PoPs for performance.

### Related Concepts

- Caching: Storing copies of content closer to users.
- CDN: Content delivery network built on edge locations.
- Latency: Minimized by geographic proximity.
```

`01 Concepts/AWS Pricing Models.md`:
```markdown
#AWS #Concept #Concept
### AWS Pricing Models

AWS offers flexible pricing including On-Demand, Reserved Instances, Savings Plans, and Spot. On-Demand is pay-per-use with no commitment; Reserved and Savings Plans trade upfront commitment for discounts; Spot provides steep discounts on unused capacity. Pricing varies by service and region.

### Related Services

- [[AWS Cost Explorer]]: Analyzes and forecasts spend.
- [[AWS Budgets]]: Sets thresholds and alerts on cost.
- [[AWS Free Tier]]: Free usage to get started.

### Related Concepts

- On-Demand: Pay for what you use, no commitment.
- Reserved/Savings Plans: Discounts for commitment.
- Spot: Variable pricing on spare capacity.
- [[Total Cost of Ownership]]: Comparing cloud vs on-premises cost.
```

`01 Concepts/AWS Support Plans.md`:
```markdown
#AWS #Concept #Concept
### AWS Support Plans

AWS support tiers provide access to technical support, guidance, and account assistance. Plans range from Basic (no charge, limited) to Developer, Business, Enterprise On-Ramp, and Enterprise, each adding faster response times, support channels, and additional features like Trusted Advisor and infrastructure event management.

### Related Services

- [[AWS Support]]: The service behind support cases and health monitoring.
- [[Trusted Advisor]]: Automated best-practice checks included with paid plans.

### Related Concepts

- SLAs: Response-time commitments per plan.
- Enterprise Support: Technical account management and architectural guidance.
```

`01 Concepts/Total Cost of Ownership.md`:
```markdown
#AWS #Concept #Concept
### Total Cost of Ownership

TCO compares the full cost of running workloads in the cloud versus on-premises, including hardware, software, operations, power, and staff. AWS provides the TCO Calculator to model these costs, accounting for utilization, pricing models, and reserved capacity discounts.

### Related Services

- [[AWS Cost Explorer]]: Ongoing spend visibility after migration.
- [[AWS Pricing Models]]: The pricing options that affect TCO.

### Related Concepts

- Capex vs Opex: Upfront capital vs operational expense.
- Utilization: Cloud scales to actual usage.
- Economies of Scale: AWS passes on volume pricing.
```

`01 Concepts/AWS Budgets.md`:
```markdown
#AWS #Service #Concept
### AWS Budgets

AWS Budgets lets you set custom cost and usage budgets with alerts sent via email or SNS when thresholds are reached. Budgets cover cost, usage, reserved-instance coverage and utilization, and Savings Plans, enabling proactive spend management.

### Related Services

- [[AWS Cost Explorer]]: Visualizes the spend budgets track.
- [[CloudWatch]]: Delivers budget alarm notifications.

### Related Concepts

- Cost Alerts: Notifications at defined thresholds.
- Usage Tracking: Monitoring resource consumption.
- [[AWS Pricing Models]]: Understanding what drives cost.
```

`01 Concepts/AWS Cost Explorer.md`:
```markdown
#AWS #Service #Concept
### AWS Cost Explorer

AWS Cost Explorer provides interactive charts and reports for analyzing historical and forecasted AWS spend. It supports filtering by service, region, tag, and dimension, and includes a cost anomaly detection feature to surface unexpected charges.

### Related Services

- [[AWS Budgets]]: Sets alerts on the spend Cost Explorer tracks.
- [[AWS Organizations]]: Aggregates cost across accounts.
- [[AWS Pricing Models]]: Context for interpreting costs.

### Related Concepts

- Cost Anomaly Detection: Automated identification of unusual spend.
- Forecasting: Projecting future costs from history.
```

`01 Concepts/AWS Account & Root User.md`:
```markdown
#AWS #Concept #Concept
### AWS Account & Root User

Every AWS account has a root user with full, unrestricted access. AWS recommends enabling MFA on the root user, never using it for daily tasks, and instead creating IAM users/roles for day-to-day administration. Root user credentials can be used to close the account or change support plans.

### Related Services

- [[IAM]]: The identities used instead of the root user.
- [[AWS Organizations]]: Manages multiple accounts centrally.
- [[CloudTrail]]: Records root user activity.

### Related Concepts

- [[IAM Roles]]: Temporary credentials for administration.
- MFA: Multi-factor authentication for root protection.
- Least Privilege: Limit root usage to emergencies.
```

`01 Concepts/AWS Free Tier.md`:
```markdown
#AWS #Concept #Concept
### AWS Free Tier

AWS Free Tier provides free usage tiers to explore services: always-free services (e.g., certain Lambda requests, DynamoDB capacity), 12-month free services (e.g., 750 EC2 hours/month), and short-term trial offers. It is a way to learn and prototype without incurring costs.

### Related Services

- [[AWS Budgets]]: Prevents surprise charges after free limits.
- [[EC2]]: Included in the 12-month free tier.
- [[Lambda]]: Always-free tier with monthly request allowance.

### Related Concepts

- [[AWS Pricing Models]]: Understanding when free tiers end.
- Cost Control: Monitoring usage to stay within limits.
```

`01 Concepts/AWS Support.md`:
```markdown
#AWS #Service #Concept
### AWS Support

AWS Support is the customer service organization providing technical assistance, health checks, and case management. It powers the AWS Health Dashboard, support cases, and — for Enterprise plans — technical account managers and architectural guidance.

### Related Services

- [[AWS Support Plans]]: The tiers defining support scope and SLAs.
- [[AWS Well-Architected Tool]]: Reviews workloads with AWS assistance.
- [[Trusted Advisor]]: Automated checks available with support plans.

### Related Concepts

- Support Cases: Tracks issues with AWS.
- Health Dashboard: Service and account health status.
```

`01 Concepts/AWS Well-Architected Tool.md`:
```markdown
#AWS #Service #Concept
### AWS Well-Architected Tool

AWS Well-Architected Tool reviews your workloads against the six Well-Architected Framework pillars — operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability. It generates milestone-based recommendations to improve architecture.

### Related Services

- [[Well-Architected Framework]]: The pillars the tool assesses.
- [[AWS Support]]: Enterprise support can assist with reviews.

### Related Concepts

- Pillars: The six lenses for evaluating architecture.
- Workload Review: Continuous improvement cycles.
```

- [ ] **Step 3: Create `01 Concepts/Index.md`**

```markdown
#AWS #MOC
### Concepts — Index

Cloud fundamentals, AWS concepts, pricing, and cost tools.

## Concepts

- [[Cloud Computing Overview]]
- [[AWS Global Infrastructure]]
- [[Regions & Availability Zones]]
- [[Edge Locations]]
- [[Shared Responsibility Model]]
- [[Architecture Design Principles]]
- [[Migration Strategies]]
- [[CAF]]
- [[Well-Architected Framework]]
- [[Total Cost of Ownership]]
- [[AWS Account & Root User]]

## Services & Tools

- [[IaaS]]
- [[PaaS]]
- [[SaaS]]
- [[IaC]]
- [[AWS Pricing Models]]
- [[AWS Support Plans]]
- [[AWS Support]]
- [[AWS Free Tier]]
- [[AWS Budgets]]
- [[AWS Cost Explorer]]
- [[AWS Well-Architected Tool]]
- [[rePost]]
- [[CCFT]]
```

- [ ] **Step 4: Verify and commit**

```bash
ls "01 Concepts" | wc -l
```

Expected: 25 (24 notes + `Index.md`).

```bash
git add -A && git commit -m "feat: build 01 Concepts domain (13 new notes + index)"
```

---

### Task 3: 02 Compute — moves + 8 new notes + index

**Files:**
- Move (via `tools/retag.py`): all 7 Compute rows
- Create: `02 Compute/EC2 Instance Types.md`, `02 Compute/EC2 Pricing Models.md`, `02 Compute/EC2 AMIs.md`, `02 Compute/EC2 Storage.md`, `02 Compute/ECS.md`, `02 Compute/EKS.md`, `02 Compute/Batch.md`, `02 Compute/App Runner.md`
- Create: `02 Compute/Index.md`
- Deep-dive rewrite: `02 Compute/EC2.md`, `02 Compute/Lambda.md` (add sections below)

**Interfaces:**
- Consumes: `tools/retag.py`
- Produces: 8 new notes (tag `#AWS #Service #Compute`), `Index.md` linking 15 notes

- [ ] **Step 1: Run the move tool**

```bash
python3 tools/retag.py
ls "02 Compute"
```

Expected: `EC2.md`, `Lambda.md`, `Elastic Beanstalk.md`, `Fargate.md`, `Auto Scaling.md`, `Outposts.md`, `Lightsail.md`.

- [ ] **Step 2: Deep-dive `EC2.md` — append these sections after the existing description**

```markdown
### Instance Types

- [[EC2 Instance Types]]: Families optimized for different workloads.
- [[EC2 Pricing Models]]: On-Demand, Reserved, Spot, and Savings Plans.

### AMIs & Storage

- [[EC2 AMIs]]: Pre-configured machine images for launching instances.
- [[EC2 Storage]]: EBS volumes and instance store options.
```

- [ ] **Step 3: Deep-dive `Lambda.md` — append this section after the existing description**

```markdown
### Runtime & Limits

Lambda supports multiple runtimes and charges per invocation and compute time. Event sources include S3, DynamoDB Streams, Kinesis, SQS, and API Gateway. See [[Lambda]] related concepts for serverless patterns.
```

(Note: `[[Lambda]]` self-link is intentionally avoided — reference plain concepts instead. Replace the self-link text with: "See the Related Services and Related Concepts sections below.")

- [ ] **Step 4: Create the 8 new Compute notes** (full files):

`02 Compute/EC2 Instance Types.md`:
```markdown
#AWS #Service #Compute
### EC2 Instance Types

EC2 instance types are grouped into families: general purpose, compute optimized, memory optimized, storage optimized, and accelerated computing. Each family balances CPU, memory, storage, and network to match workload needs, with size tiers scaling resources within a family.

### Related Services

- [[EC2]]: The service that launches these instances.
- [[EC2 Pricing Models]]: How instance usage is billed.
- [[Auto Scaling]]: Adjusts instance counts by type.

### Related Concepts

- vCPU: Virtual CPU sizing.
- Instance Families: Purpose-built resource balances.
- [[EC2 AMIs]]: The images instances are launched from.
```

`02 Compute/EC2 Pricing Models.md`:
```markdown
#AWS #Service #Compute
### EC2 Pricing Models

EC2 offers On-Demand (pay per second, no commitment), Reserved Instances (discount for 1- or 3-year commitment), Savings Plans (flexible usage-based discounts), Spot Instances (steeply discounted spare capacity), and Dedicated Hosts. Choosing the right model balances cost and flexibility.

### Related Services

- [[EC2]]: The compute service these models price.
- [[AWS Pricing Models]]: General AWS pricing concepts.
- [[Auto Scaling]]: Uses spot and on-demand capacity.

### Related Concepts

- On-Demand: Flexible, no commitment.
- Spot: Interruptible, low-cost capacity.
- Reserved/Savings Plans: Commitment for discounts.
```

`02 Compute/EC2 AMIs.md`:
```markdown
#AWS #Service #Compute
### EC2 AMIs

An Amazon Machine Image (AMI) is a template containing the OS, applications, and configuration used to launch EC2 instances. AMIs can be created from existing instances, imported, or selected from the Marketplace, and include metadata like block-device mapping and permissions.

### Related Services

- [[EC2]]: Launches instances from AMIs.
- [[EC2 Storage]]: Block devices defined by the AMI.
- [[AWS Backup]]: Creates instance backups as images.

### Related Concepts

- Golden Image: A standardized, pre-hardened AMI.
- Image Permissions: Sharing AMIs across accounts.
- [[EC2 Instance Types]]: Pairs an AMI with an instance type.
```

`02 Compute/EC2 Storage.md`:
```markdown
#AWS #Service #Compute
### EC2 Storage

EC2 instances use two block storage options: EBS volumes (durable, network-attached, detached and reattached) and instance store volumes (ephemeral, physically attached, lost on stop). File-level shared storage can be added via EFS, and object storage via S3.

### Related Services

- [[EBS]]: Persistent block storage for instances.
- [[EFS]]: Shared file storage for Linux instances.
- [[S3]]: Object storage for data exchange and backup.

### Related Concepts

- [[EC2 AMIs]]: Images store root volumes.
- Durability: EBS persists independently of the instance.
- Ephemeral Storage: Instance store data is temporary.
```

`02 Compute/ECS.md`:
```markdown
#AWS #Service #Compute
### ECS

Amazon Elastic Container Service (ECS) is a fully managed container orchestration service for running Docker containers. It supports Fargate (serverless) and EC2 launch types, integrates with load balancers and Service Discovery, and uses task definitions to describe containers.

### Related Services

- [[Fargate]]: Serverless compute for ECS tasks.
- [[EKS]]: Kubernetes alternative to ECS.
- [[ELB]]: Distributes traffic to container tasks.

### Related Concepts

- Task Definition: Blueprint for a container group.
- Container: Packaged application and dependencies.
- Service: Maintains desired task count.
```

`02 Compute/EKS.md`:
```markdown
#AWS #Service #Compute
### EKS

Amazon Elastic Kubernetes Service (EKS) is a managed Kubernetes service. AWS runs the control plane for high availability, integrates with IAM, ELB, and CloudWatch, and supports self-managed nodes, managed node groups, and Fargate for running pods.

### Related Services

- [[ECS]]: AWS's own container orchestrator.
- [[Fargate]]: Run EKS pods without managing nodes.
- [[CloudWatch]]: Monitoring and logging for clusters.

### Related Concepts

- Kubernetes: Open-source container orchestration.
- Control Plane: Managed by AWS in EKS.
- Node Group: Worker nodes running pods.
```

`02 Compute/Batch.md`:
```markdown
#AWS #Service #Compute
### AWS Batch

AWS Batch is a fully managed batch computing service for running large-scale parallel jobs. It dynamically provisions EC2 or Fargate resources based on job queue demand, supports containerized and native jobs, and is suited for rendering, analytics, and scientific workloads.

### Related Services

- [[EC2]]: Backs batch compute environments.
- [[Fargate]]: Serverless option for batch jobs.
- [[Step Functions]]: Orchestrates multi-step batch pipelines.

### Related Concepts

- Job Queue: Pending jobs awaiting compute.
- Compute Environment: Managed capacity for jobs.
- Parallelism: Scales jobs across resources.
```

`02 Compute/App Runner.md`:
```markdown
#AWS #Service #Compute
### AWS App Runner

AWS App Runner is a fully managed service for deploying containerized web applications directly from a source repo or image. It handles scaling, load balancing, TLS, and deployment automatically, making it one of the simplest ways to run web apps and APIs on AWS.

### Related Services

- [[ECS]]: More control for container orchestration.
- [[Fargate]]: Serverless containers with more configuration.
- [[ELB]]: Load balancing for App Runner services.

### Related Concepts

- Containerized Apps: Deploy from source or image.
- Auto Scaling: Managed, no capacity planning.
- Serverless: No infrastructure to manage.
```

- [ ] **Step 5: Create `02 Compute/Index.md`**

```markdown
#AWS #MOC
### Compute — Index

EC2, Lambda, containers, and serverless compute.

## Services

- [[EC2]]
- [[EC2 Instance Types]]
- [[EC2 Pricing Models]]
- [[EC2 AMIs]]
- [[EC2 Storage]]
- [[Lambda]]
- [[Elastic Beanstalk]]
- [[ECS]]
- [[EKS]]
- [[Fargate]]
- [[Batch]]
- [[App Runner]]
- [[Auto Scaling]]
- [[Outposts]]
- [[Lightsail]]
```

- [ ] **Step 6: Verify and commit**

```bash
ls "02 Compute" | wc -l
```

Expected: 16 (15 notes + `Index.md`).

```bash
git add -A && git commit -m "feat: build 02 Compute domain (8 new notes + index + deep dives)"
```

---

### Task 4: 03 Storage — moves + 4 new notes + S3 hub rewrite + index

**Files:**
- Move (via `tools/retag.py`): all 17 Storage rows
- Create: `03 Storage/EBS.md`, `03 Storage/Storage Gateway.md`, `03 Storage/S3 Deep Archive.md`, `03 Storage/S3 Transfer Acceleration.md`
- Deep-dive rewrite: `03 Storage/S3.md` (append sections below)
- Create: `03 Storage/Index.md`

**Interfaces:**
- Consumes: `tools/retag.py`
- Produces: 4 new notes (tag `#AWS #Service #Storage`), `Index.md` linking 21 notes

- [ ] **Step 1: Run the move tool**

```bash
python3 tools/retag.py
ls "03 Storage"
```

Expected: `S3.md` + 12 S3 sub-topics + `EFS.md`, `FSx File Gateway.md`, `Backup.md`, `DataSync.md`.

- [ ] **Step 2: Deep-dive `S3.md` — append these sections**

```markdown
### Archival & Transfer

- [[S3 Deep Archive]]: Lowest-cost long-term archival class.
- [[S3 Glacier]]: Flexible archival retrieval in minutes to hours.
- [[S3 Transfer Acceleration]]: Faster uploads via edge locations.

### Storage Class Transitions

- [[S3 Lifecycle]]: Automates movement between classes.
- [[S3 Intelligent-Tiering]]: Auto-tiers by access patterns.
```

- [ ] **Step 3: Create the 4 new Storage notes** (full files):

`03 Storage/EBS.md`:
```markdown
#AWS #Service #Storage
### EBS

Amazon Elastic Block Store (EBS) provides persistent, network-attached block storage for EC2 instances. Volumes are replicated within an Availability Zone, support snapshots to S3 for backup, and offer several volume types (gp2/gp3, io1/io2, st1, sc1) for cost and performance.

### Related Services

- [[EC2]]: Attaches EBS volumes to instances.
- [[EC2 Storage]]: How EBS fits into EC2 storage options.
- [[S3]]: Stores EBS snapshots.

### Related Concepts

- Snapshots: Incremental backups to S3.
- IOPS: Input/output operations per second.
- [[EC2 AMIs]]: Root volumes originate from images.
```

`03 Storage/Storage Gateway.md`:
```markdown
#AWS #Service #Storage
### Storage Gateway

AWS Storage Gateway provides hybrid cloud storage, connecting on-premises environments to AWS. Modes include File Gateway (SMB/NFS to S3), Volume Gateway (block storage with snapshots), and Tape Gateway (virtual tapes to S3/Glacier).

### Related Services

- [[S3]]: Backend storage for file and tape gateways.
- [[S3 Glacier]]: Archival for virtual tapes.
- [[DataSync]]: Large-scale data transfer to AWS.

### Related Concepts

- Hybrid Cloud: On-premises + AWS storage.
- Caching: Local cache for low-latency access.
- Snapshots: Point-in-time recovery to AWS.
```

`03 Storage/S3 Deep Archive.md`:
```markdown
#AWS #Service #Storage
### S3 Deep Archive

S3 Deep Archive is the lowest-cost S3 storage class for rarely accessed, long-term retention (e.g., compliance archives). Retrieval takes 12 to 48 hours and objects must be stored for at least 180 days, making it appropriate only for cold data.

### Related Services

- [[S3]]: The service providing this storage class.
- [[S3 Lifecycle]]: Automates transitions into Deep Archive.
- [[S3 Glacier]]: Faster archival alternative.

### Related Concepts

- Retrieval Time: Hours, not minutes.
- Minimum Storage Duration: 180-day commitment.
- Archival: Long-term, low-access data.
```

`03 Storage/S3 Transfer Acceleration.md`:
```markdown
#AWS #Service #Storage
### S3 Transfer Acceleration

S3 Transfer Acceleration speeds up uploads to S3 by routing traffic through AWS edge locations. It uses optimized network paths instead of direct internet routes, reducing latency for long-distance or large-object transfers.

### Related Services

- [[S3]]: The target bucket for accelerated uploads.
- [[CloudFront]]: Edge locations used for acceleration.

### Related Concepts

- Edge Locations: PoPs that optimize network paths.
- Upload Throughput: Faster for cross-region transfers.
```

- [ ] **Step 4: Create `03 Storage/Index.md`**

```markdown
#AWS #MOC
### Storage — Index

S3, EBS, EFS, backup, and data transfer.

## S3

- [[S3]]
- [[S3 Access Control]]
- [[S3 Encryption]]
- [[S3 Event Notifications]]
- [[S3 Versioning]]
- [[S3 Lifecycle]]
- [[S3 Replication]]
- [[S3 Select]]
- [[S3 Standard]]
- [[S3 Standard-Infrequent Access (IA)]]
- [[S3 One Zone-IA]]
- [[S3 Intelligent-Tiering]]
- [[S3 Glacier]]
- [[S3 Deep Archive]]
- [[S3 Transfer Acceleration]]

## Block, File & Hybrid

- [[EBS]]
- [[EFS]]
- [[FSx File Gateway]]
- [[Storage Gateway]]

## Backup & Transfer

- [[Backup]]
- [[DataSync]]
```

- [ ] **Step 5: Verify and commit**

```bash
ls "03 Storage" | wc -l
```

Expected: 22 (21 notes + `Index.md`).

```bash
git add -A && git commit -m "feat: build 03 Storage domain (4 new notes + index + S3 hub)"
```

---

### Task 5: 04 Database — moves + 8 new notes + index

**Files:**
- Move (via `tools/retag.py`): all 5 Database rows
- Create: `04 Database/DynamoDB DAX.md`, `04 Database/DynamoDB Streams.md`, `04 Database/RDS Multi-AZ.md`, `04 Database/RDS Read Replicas.md`, `04 Database/RDS Backups.md`, `04 Database/ElastiCache.md`, `04 Database/DocumentDB.md`, `04 Database/Redshift Spectrum.md`
- Create: `04 Database/Index.md`

**Interfaces:**
- Consumes: `tools/retag.py`
- Produces: 8 new notes (tag `#AWS #Service #Database`), `Index.md` linking 13 notes

- [ ] **Step 1: Run the move tool**

```bash
python3 tools/retag.py
ls "04 Database"
```

Expected: `RDS.md`, `Aurora.md`, `DynamoDB.md`, `Redshift.md`, `Neptune.md`.

- [ ] **Step 2: Create the 8 new Database notes** (full files):

`04 Database/DynamoDB DAX.md`:
```markdown
#AWS #Service #Database
### DynamoDB DAX

DynamoDB Accelerator (DAX) is an in-memory cache for DynamoDB that delivers single-digit-millisecond read performance. It sits between applications and DynamoDB, caching frequently accessed items to reduce read cost and latency, and is managed by AWS with automatic failover.

### Related Services

- [[DynamoDB]]: The underlying NoSQL database.
- [[ElastiCache]]: General-purpose in-memory caching.

### Related Concepts

- In-Memory Caching: Low-latency reads.
- Read Throughput: Offloads reads from the table.
- TTL: Cache item expiration.
```

`04 Database/DynamoDB Streams.md`:
```markdown
#AWS #Service #Database
### DynamoDB Streams

DynamoDB Streams captures item-level changes (create, update, delete) in a time-ordered stream. Applications can consume these events to trigger workflows, replicate data, or maintain analytics, and stream records are retained for 24 hours.

### Related Services

- [[DynamoDB]]: The source table for changes.
- [[Lambda]]: Processes stream records via event source mapping.
- [[Kinesis]]: Alternative streaming data pipeline.

### Related Concepts

- Change Data Capture: Recording modifications.
- Event-Driven Architecture: React to table changes.
- Streams TTL: 24-hour record retention.
```

`04 Database/RDS Multi-AZ.md`:
```markdown
#AWS #Service #Database
### RDS Multi-AZ

RDS Multi-AZ provides high availability by automatically replicating a primary database to a standby in another Availability Zone. Failover is automatic, synchronous replication keeps data in sync, and the standby is not used for reads.

### Related Services

- [[RDS]]: The managed database service.
- [[RDS Read Replicas]]: Asynchronous read scaling (separate feature).
- [[VPC]]: Network placement across AZs.

### Related Concepts

- Failover: Automatic switch to standby on failure.
- Synchronous Replication: Standby stays current.
- High Availability: Survives AZ failure.
```

`04 Database/RDS Read Replicas.md`:
```markdown
#AWS #Service #Database
### RDS Read Replicas

RDS Read Replicas are asynchronous copies of a database used to offload read traffic and improve performance. They can be promoted to standalone instances, support cross-region replication, and help scale read-heavy workloads.

### Related Services

- [[RDS]]: The primary database being replicated.
- [[RDS Multi-AZ]]: Availability-focused replication (distinct from replicas).
- [[Route 53]]: Routes reads to replica endpoints.

### Related Concepts

- Asynchronous Replication: Replicas may lag slightly.
- Read Scaling: Distribute SELECT traffic.
- Promotion: Convert a replica to a primary.
```

`04 Database/RDS Backups.md`:
```markdown
#AWS #Service #Database
### RDS Backups

RDS provides automated backups with point-in-time recovery (restorable to any second in the retention window) and manual snapshots that persist until deleted. Backups and snapshots are stored in S3 and are encrypted if the database is encrypted.

### Related Services

- [[RDS]]: The database service backing up data.
- [[S3]]: Where backups and snapshots are stored.
- [[AWS Backup]]: Centralized backup management.

### Related Concepts

- Point-in-Time Recovery: Restore to any second.
- Retention Period: How long automated backups are kept.
- Snapshots: Manual, persistent backups.
```

`04 Database/ElastiCache.md`:
```markdown
#AWS #Service #Database
### ElastiCache

Amazon ElastiCache is a fully managed in-memory data store compatible with Redis and Memcached. It powers caching, session stores, leaderboards, and pub/sub, delivering microsecond latency and reducing load on backend databases.

### Related Services

- [[RDS]]: Offloads reads from relational databases.
- [[DynamoDB]]: Offloads reads from NoSQL tables.
- [[DynamoDB DAX]]: DynamoDB-specific in-memory cache.

### Related Concepts

- Redis/Memcached: In-memory engines.
- TTL: Cache expiration policies.
- Cache Hit Ratio: Effectiveness of caching.
```

`04 Database/DocumentDB.md`:
```markdown
#AWS #Service #Database
### DocumentDB

Amazon DocumentDB is a MongoDB-compatible managed document database. It stores JSON-like documents with a flexible schema, supports up to 15 read replicas, and offers automatic scaling, encryption, and point-in-time backups.

### Related Services

- [[DynamoDB]]: Other NoSQL option for key-value/document data.
- [[Neptune]]: Graph database for connected data.
- [[RDS]]: Relational alternative.

### Related Concepts

- Document Model: JSON-like flexible schemas.
- MongoDB Compatibility: Drop-in migration support.
- Read Replicas: Scale reads up to 15 copies.
```

`04 Database/Redshift Spectrum.md`:
```markdown
#AWS #Service #Database
### Redshift Spectrum

Redshift Spectrum lets you run SQL queries directly against data in S3 without loading it into Redshift. It uses the Redshift cluster to coordinate queries while massively parallel nodes scan S3, enabling petabyte-scale analytics over a data lake.

### Related Services

- [[Redshift]]: The cluster that runs Spectrum queries.
- [[S3]]: The data lake being queried.
- [[Athena]]: Serverless alternative for S3 queries.

### Related Concepts

- Data Lake: Querying raw data in S3.
- External Tables: Tables backed by S3.
- ELT/ETL: Spectrum avoids loading data.
```

- [ ] **Step 3: Create `04 Database/Index.md`**

```markdown
#AWS #MOC
### Database — Index

Relational, NoSQL, and analytics databases.

## Relational

- [[RDS]]
- [[RDS Multi-AZ]]
- [[RDS Read Replicas]]
- [[RDS Backups]]
- [[Aurora]]
- [[Redshift]]
- [[Redshift Spectrum]]

## NoSQL & In-Memory

- [[DynamoDB]]
- [[DynamoDB DAX]]
- [[DynamoDB Streams]]
- [[DocumentDB]]
- [[Neptune]]
- [[ElastiCache]]
```

- [ ] **Step 4: Verify and commit**

```bash
ls "04 Database" | wc -l
```

Expected: 14 (13 notes + `Index.md`).

```bash
git add -A && git commit -m "feat: build 04 Database domain (8 new notes + index)"
```

---

### Task 6: 05 Networking — moves + 7 new notes + index

**Files:**
- Move (via `tools/retag.py`): all 5 Networking rows
- Create: `05 Networking/ELB.md`, `05 Networking/NAT Gateway.md`, `05 Networking/Security Groups vs NACLs.md`, `05 Networking/VPC Peering.md`, `05 Networking/VPC Endpoints.md`, `05 Networking/Transit Gateway.md`, `05 Networking/AWS Global Accelerator.md`
- Create: `05 Networking/Index.md`

**Interfaces:**
- Consumes: `tools/retag.py`
- Produces: 7 new notes (tag `#AWS #Service #Networking`), `Index.md` linking 12 notes

- [ ] **Step 1: Run the move tool**

```bash
python3 tools/retag.py
ls "05 Networking"
```

Expected: `VPC.md`, `CloudFront.md`, `Route 53.md`, `API Gateway.md`, `Direct Connect.md`.

- [ ] **Step 2: Create the 7 new Networking notes** (full files):

`05 Networking/ELB.md`:
```markdown
#AWS #Service #Networking
### ELB

Elastic Load Balancing (ELB) automatically distributes traffic across targets. Types include Application Load Balancer (HTTP/HTTPS, path-based routing), Network Load Balancer (TCP/UDP, extreme performance), and Gateway Load Balancer (third-party appliances). It integrates with Auto Scaling and Route 53.

### Related Services

- [[EC2]]: Common targets for load-balanced traffic.
- [[Auto Scaling]]: Scales targets in response to load.
- [[Route 53]]: DNS routing to the load balancer.

### Related Concepts

- Health Checks: Monitor target availability.
- Target Group: Logical set of targets.
- Listener: Rules that route traffic.
```

`05 Networking/NAT Gateway.md`:
```markdown
#AWS #Service #Networking
### NAT Gateway

A NAT (Network Address Translation) Gateway enables instances in private subnets to access the internet (or AWS services) without receiving unsolicited inbound traffic. It is managed by AWS, scales automatically, and provides predictable outbound connectivity.

### Related Services

- [[VPC]]: The network where NAT Gateways live.
- [[Security Groups vs NACLs]]: The security layers applied around NAT.
- [[Route 53]]: Not directly related; use [[VPC]] routing instead.

### Related Concepts

- Private Subnet: No direct internet access.
- Outbound Only: Initiated connections only.
- Elastic IP: Stable source address.
```

`05 Networking/Security Groups vs NACLs.md`:
```markdown
#AWS #Service #Networking
### Security Groups vs NACLs

Security Groups are stateful virtual firewalls at the instance/ENI level, allowing only rules that permit traffic (no explicit deny). NACLs are stateless, subnet-level firewalls with numbered allow/deny rules evaluated in order. Both are used together for defense in depth.

### Related Services

- [[VPC]]: The network layer hosting both.
- [[EC2]]: Security Groups attach to instances.
- [[NAT Gateway]]: Traffic subject to these controls.

### Related Concepts

- Stateful vs Stateless: SG auto-allows return traffic; NACL does not.
- Default Deny: SG has no traffic until rules added.
- Rule Evaluation: NACL rules processed by number.
```

`05 Networking/VPC Peering.md`:
```markdown
#AWS #Service #Networking
### VPC Peering

VPC Peering connects two VPCs via a private, encrypted route so they can communicate as if on the same network. Peering is not transitive (no A→B→C), does not require a gateway, and can connect VPCs across accounts or regions.

### Related Services

- [[VPC]]: The networks being connected.
- [[Transit Gateway]]: Hub-and-spoke alternative for many VPCs.
- [[Route 53]]: Optional DNS integration.

### Related Concepts

- Non-Transitive: A-B peering does not reach C.
- Private Connectivity: No internet exposure.
- CIDR Overlap: Cannot peer overlapping ranges.
```

`05 Networking/VPC Endpoints.md`:
```markdown
#AWS #Service #Networking
### VPC Endpoints

VPC Endpoints enable private connectivity between a VPC and AWS services (e.g., S3, DynamoDB, Lambda) without traversing the public internet. Gateway endpoints (S3, DynamoDB) and interface endpoints (ENI-based, most services) both keep traffic inside the AWS network.

### Related Services

- [[VPC]]: The network hosting endpoints.
- [[S3]]: Uses gateway endpoints.
- [[DynamoDB]]: Uses gateway endpoints.

### Related Concepts

- Private Connectivity: Traffic stays in AWS network.
- Endpoint Policy: Controls access through the endpoint.
- Interface Endpoint: ENI-based, supports most services.
```

`05 Networking/Transit Gateway.md`:
```markdown
#AWS #Service #Networking
### Transit Gateway

AWS Transit Gateway is a hub-and-spoke network router that connects VPCs, VPNs, and Direct Connect attachments in one place. It supports transitive routing across many VPCs, simplifies network architecture, and centralizes route management.

### Related Services

- [[VPC]]: Spokes attached to the transit hub.
- [[Direct Connect]]: On-premises connectivity into the hub.
- [[VPC Peering]]: Mesh alternative for small numbers of VPCs.

### Related Concepts

- Hub-and-Spoke: Central router model.
- Route Tables: Per-attachment routing.
- Transitive Routing: Traffic flows between spokes via the hub.
```

`05 Networking/AWS Global Accelerator.md`:
```markdown
#AWS #Service #Networking
### AWS Global Accelerator

AWS Global Accelerator improves application availability and performance by directing traffic through AWS edge locations to optimal regional endpoints. It provides static IP addresses, fast failover via health checks, and acceleration over the AWS global network.

### Related Services

- [[ELB]]: Common endpoint behind the accelerator.
- [[CloudFront]]: CDN counterpart (caching vs network path).
- [[Edge Locations]]: PoPs that route traffic.

### Related Concepts

- Static IPs: Fixed anycast addresses.
- Health-Based Routing: Automatic failover.
- Network Acceleration: Optimized global path.
```

- [ ] **Step 3: Create `05 Networking/Index.md`**

```markdown
#AWS #MOC
### Networking — Index

VPC, CDN, DNS, load balancing, and APIs.

## VPC & Routing

- [[VPC]]
- [[Security Groups vs NACLs]]
- [[NAT Gateway]]
- [[VPC Peering]]
- [[VPC Endpoints]]
- [[Transit Gateway]]

## Edge & Delivery

- [[CloudFront]]
- [[Route 53]]
- [[AWS Global Accelerator]]

## Load Balancing & APIs

- [[ELB]]
- [[API Gateway]]

## Hybrid

- [[Direct Connect]]
```

- [ ] **Step 4: Verify and commit**

```bash
ls "05 Networking" | wc -l
```

Expected: 13 (12 notes + `Index.md`).

```bash
git add -A && git commit -m "feat: build 05 Networking domain (7 new notes + index)"
```

---

### Task 7: 06 Security — moves + 8 new notes + IAM deep dive + index

**Files:**
- Move (via `tools/retag.py`): all 12 Security rows
- Create: `06 Security/WAF.md`, `06 Security/Secrets Manager.md`, `06 Security/ACM.md`, `06 Security/Security Hub.md`, `06 Security/CloudHSM.md`, `06 Security/IAM Roles.md`, `06 Security/IAM Policies.md`, `06 Security/IAM Identity Center.md`
- Deep-dive rewrite: `06 Security/IAM.md` (append sections)
- Create: `06 Security/Index.md`

**Interfaces:**
- Consumes: `tools/retag.py`
- Produces: 8 new notes (tag `#AWS #Service #Security`), `Index.md` linking 20 notes

- [ ] **Step 1: Run the move tool**

```bash
python3 tools/retag.py
ls "06 Security"
```

Expected: `IAM.md`, `KMS.md`, `STS.md`, `Shield.md`, `Artifact.md`, `CloudTrail.md`, `Config.md`, `GuardDuty.md`, `Inspector.md`, `Macie.md`, `Detective.md`, `Cognito.md`.

- [ ] **Step 2: Deep-dive `IAM.md` — append these sections**

```markdown
### Policies & Roles

- [[IAM Policies]]: JSON documents that define permissions.
- [[IAM Roles]]: Temporary credentials for users and services.

### Federated Access

- [[IAM Identity Center]]: Centralized SSO across AWS accounts and apps.
- [[STS]]: Issues the temporary credentials behind roles.
```

- [ ] **Step 3: Create the 8 new Security notes** (full files):

`06 Security/WAF.md`:
```markdown
#AWS #Service #Security
### WAF

AWS WAF is a managed web application firewall that filters and monitors HTTP(S) traffic. It protects CloudFront, ALB, and API Gateway from common attacks like SQL injection and cross-site scripting using rules, rule groups, and rate-based rules.

### Related Services

- [[CloudFront]]: Common integration point for WAF.
- [[Shield]]: DDoS protection layered with WAF.
- [[API Gateway]]: Protected via web ACLs.

### Related Concepts

- Web ACL: Set of rules applied to traffic.
- Rate-Based Rule: Blocks IPs exceeding a threshold.
- OWASP: Common managed rule sets.
```

`06 Security/Secrets Manager.md`:
```markdown
#AWS #Service #Security
### Secrets Manager

AWS Secrets Manager securely stores and rotates database credentials, API keys, and other secrets. It integrates with RDS and Lambda for automatic rotation, encrypts secrets with KMS, and enforces fine-grained access via IAM.

### Related Services

- [[KMS]]: Encrypts secrets at rest.
- [[RDS]]: Credential rotation for databases.
- [[IAM]]: Authorizes secret access.

### Related Concepts

- Secret Rotation: Automated credential replacement.
- Secret Versioning: Multiple versions of a secret.
- Retrieval API: Get secret value with IAM.
```

`06 Security/ACM.md`:
```markdown
#AWS #Service #Security
### ACM

AWS Certificate Manager (ACM) provisions, manages, and renews public and private SSL/TLS certificates for use with CloudFront, ALB, and API Gateway. Certificates integrate with Route 53 DNS validation and are automatically renewed.

### Related Services

- [[CloudFront]]: Serves HTTPS content with ACM certs.
- [[ELB]]: Terminates TLS with ACM certs.
- [[Route 53]]: DNS validation for cert issuance.

### Related Concepts

- TLS/SSL: Encrypts traffic in transit.
- Auto-Renewal: Managed certificate lifecycle.
- Public vs Private CA: ACM public certs vs Private CA.
```

`06 Security/Security Hub.md`:
```markdown
#AWS #Service #Security
### Security Hub

AWS Security Hub aggregates security findings from GuardDuty, Inspector, Macie, IAM Access Analyzer, and third-party tools into one view. It runs continuous checks against AWS Foundational Security Best Practices and CIS standards, enabling centralized posture management.

### Related Services

- [[GuardDuty]]: Feeds threat detection findings.
- [[Inspector]]: Feeds vulnerability findings.
- [[Config]]: Supports compliance checks.

### Related Concepts

- Findings: Aggregated security events.
- Standards: AWS FSBP, CIS, PCI DSS.
- Insight: Cross-finding queries.
```

`06 Security/CloudHSM.md`:
```markdown
#AWS #Service #Security
### CloudHSM

AWS CloudHSM provides dedicated hardware security modules (HSMs) for generating and storing cryptographic keys. Unlike KMS's shared, AWS-managed service, CloudHSM gives customers exclusive control over the HSM and keys, satisfying compliance requirements for hardware key custody.

### Related Services

- [[KMS]]: Managed alternative for key storage.
- [[ACM]]: Can integrate with private CA.

### Related Concepts

- HSM: Tamper-resistant hardware for keys.
- Key Custody: Exclusive customer control.
- FIPS: Validated hardware modules.
```

`06 Security/IAM Roles.md`:
```markdown
#AWS #Service #Security
### IAM Roles

IAM Roles are identities with permissions that are assumed to obtain temporary credentials via STS. Roles have no permanent keys and are used by AWS services (e.g., Lambda execution roles), EC2 instances, and federated users to grant scoped, temporary access.

### Related Services

- [[IAM]]: The service that defines roles and policies.
- [[STS]]: Issues the temporary credentials when a role is assumed.
- [[IAM Policies]]: Attach permissions to roles.

### Related Concepts

- Trust Policy: Who can assume the role.
- Temporary Credentials: Short-lived access keys.
- Cross-Account Access: Roles for account delegation.
```

`06 Security/IAM Policies.md`:
```markdown
#AWS #Service #Security
### IAM Policies

IAM Policies are JSON documents that define permissions — which actions are allowed or denied on which resources under which conditions. Policies attach to IAM users, groups, or roles, and support managed, inline, and customer-managed policy types.

### Related Services

- [[IAM]]: The service enforcing policies.
- [[IAM Roles]]: Identities that carry policies.
- [[STS]]: Evaluates policies when issuing credentials.

### Related Concepts

- Allow vs Deny: Explicit deny overrides allow.
- Policy Elements: Effect, Action, Resource, Condition.
- Least Privilege: Grant minimal permissions.
```

`06 Security/IAM Identity Center.md`:
```markdown
#AWS #Service #Security
### IAM Identity Center

AWS IAM Identity Center (formerly AWS SSO) provides centralized single sign-on across AWS accounts and business applications. It connects to external identity providers (SAML/OIDC), manages permission sets for account access, and supports MFA policies.

### Related Services

- [[IAM]]: Underlying account permissions.
- [[AWS Organizations]]: Scope of accounts for SSO.
- [[Cognito]]: Customer-facing app authentication (distinct use case).

### Related Concepts

- SSO: Single sign-on for users.
- Permission Set: Role-like assignment per account.
- Identity Provider: External IdP federation.
```

- [ ] **Step 4: Create `06 Security/Index.md`**

```markdown
#AWS #MOC
### Security — Index

Identity, access, encryption, and threat detection.

## Identity & Access

- [[IAM]]
- [[IAM Roles]]
- [[IAM Policies]]
- [[IAM Identity Center]]
- [[STS]]
- [[Cognito]]

## Encryption & Keys

- [[KMS]]
- [[CloudHSM]]
- [[ACM]]
- [[Secrets Manager]]

## Threat Detection & Compliance

- [[GuardDuty]]
- [[Inspector]]
- [[Detective]]
- [[Macie]]
- [[Shield]]
- [[WAF]]
- [[Security Hub]]
- [[CloudTrail]]
- [[Config]]
- [[Artifact]]
```

- [ ] **Step 5: Verify and commit**

```bash
ls "06 Security" | wc -l
```

Expected: 21 (20 notes + `Index.md`).

```bash
git add -A && git commit -m "feat: build 06 Security domain (8 new notes + index + IAM deep dive)"
```

---

### Task 8: 07 Analytics — moves + 3 new notes + index

**Files:**
- Move (via `tools/retag.py`): all 4 Analytics rows
- Create: `07 Analytics/OpenSearch.md`, `07 Analytics/Lake Formation.md`, `07 Analytics/EMR.md`
- Create: `07 Analytics/Index.md`

**Interfaces:**
- Consumes: `tools/retag.py`
- Produces: 3 new notes (tag `#AWS #Service #Analytics`), `Index.md` linking 7 notes

- [ ] **Step 1: Run the move tool**

```bash
python3 tools/retag.py
ls "07 Analytics"
```

Expected: `Athena.md`, `Kinesis.md`, `QuickSight.md`, `Glue.md`.

- [ ] **Step 2: Create the 3 new Analytics notes** (full files):

`07 Analytics/OpenSearch.md`:
```markdown
#AWS #Service #Analytics
### OpenSearch

Amazon OpenSearch Service (formerly Elasticsearch) is a managed search and analytics engine. It indexes and queries logs, documents, and other data with full-text search, powers log analytics dashboards (Kibana/OpenSearch Dashboards), and integrates with CloudWatch Logs and Kinesis.

### Related Services

- [[Kinesis]]: Streams data into OpenSearch.
- [[CloudWatch]]: Sends logs for search and alerting.
- [[Lambda]]: Processes records before ingestion.

### Related Concepts

- Full-Text Search: Query indexed documents.
- Index: Logical collection of documents.
- Dashboards: Kibana-style visualization.
```

`07 Analytics/Lake Formation.md`:
```markdown
#AWS #Service #Analytics
### Lake Formation

AWS Lake Formation simplifies building and securing a data lake. It ingests and catalogs data in S3, centralizes permissions for analytics services, and automates ETL with Glue, giving analysts governed access to the data lake.

### Related Services

- [[S3]]: The storage backing the data lake.
- [[Glue]]: ETL and catalog for the lake.
- [[Athena]]: Queries data in the lake.

### Related Concepts

- Data Lake: Centralized raw + curated data.
- Lake Permissions: Column/row-level access control.
- Catalog: Metadata for queryable tables.
```

`07 Analytics/EMR.md`:
```markdown
#AWS #Service #Analytics
### EMR

Amazon EMR (Elastic MapReduce) is a managed big-data platform for running open-source frameworks like Apache Spark, Hadoop, Hive, and Flink. It processes large data sets stored in S3, scales clusters on EC2, and is used for ETL, machine learning, and log analysis.

### Related Services

- [[S3]]: Source and destination for processed data.
- [[EC2]]: Backs EMR cluster nodes.
- [[Glue]]: Serverless ETL alternative.

### Related Concepts

- Cluster: Managed set of EC2 nodes.
- Spark/Hadoop: Open-source processing engines.
- Spot Instances: Lower-cost cluster nodes.
```

- [ ] **Step 3: Create `07 Analytics/Index.md`**

```markdown
#AWS #MOC
### Analytics — Index

Query, streaming, ETL, and business intelligence.

- [[Athena]]
- [[Kinesis]]
- [[Glue]]
- [[EMR]]
- [[OpenSearch]]
- [[Lake Formation]]
- [[QuickSight]]
```

- [ ] **Step 4: Verify and commit**

```bash
ls "07 Analytics" | wc -l
```

Expected: 8 (7 notes + `Index.md`).

```bash
git add -A && git commit -m "feat: build 07 Analytics domain (3 new notes + index)"
```

---

### Task 9: 08 Machine Learning — moves + 3 new notes + index

**Files:**
- Move (via `tools/retag.py`): all 7 ML rows
- Create: `08 Machine Learning/Bedrock.md`, `08 Machine Learning/Translate.md`, `08 Machine Learning/Textract.md`
- Create: `08 Machine Learning/Index.md`

**Interfaces:**
- Consumes: `tools/retag.py`
- Produces: 3 new notes (tag `#AWS #Service #ML`), `Index.md` linking 10 notes

- [ ] **Step 1: Run the move tool**

```bash
python3 tools/retag.py
ls "08 Machine Learning"
```

Expected: `SageMaker.md`, `Rekognition.md`, `Comprehend.md`, `Polly.md`, `Transcribe.md`, `Lex.md`, `Kendra.md`.

- [ ] **Step 2: Create the 3 new ML notes** (full files):

`08 Machine Learning/Bedrock.md`:
```markdown
#AWS #Service #ML
### Bedrock

Amazon Bedrock is a fully managed service for building generative AI applications using foundation models from Anthropic, AI21, Cohere, Meta, and Amazon. It provides model access via API, supports fine-tuning and agents, and integrates with the rest of AWS for secure, scalable GenAI.

### Related Services

- [[SageMaker]]: For building and training custom models.
- [[Lambda]]: Runs application logic calling Bedrock.
- [[KMS]]: Encrypts prompts and responses.

### Related Concepts

- Foundation Model: Pre-trained LLM served via API.
- GenAI: Generative applications.
- Guardrails: Content filtering for model output.
```

`08 Machine Learning/Translate.md`:
```markdown
#AWS #Service #ML
### Translate

Amazon Translate is a neural machine translation service supporting dozens of languages. It provides real-time and batch translation APIs, custom terminology and formality settings, and integrates with S3, Lambda, and other services for multilingual content pipelines.

### Related Services

- [[Comprehend]]: NLP analysis alongside translation.
- [[Polly]]: Speaks translated text.
- [[S3]]: Batch translation input/output.

### Related Concepts

- Neural MT: Deep-learning translation.
- Custom Terminology: Domain-specific phrasing.
- Batch vs Real-Time: API modes.
```

`08 Machine Learning/Textract.md`:
```markdown
#AWS #Service #ML
### Textract

Amazon Textract extracts text, tables, and forms from scanned documents using machine learning. It goes beyond OCR by preserving structure and relationships, enabling document processing for invoices, IDs, and forms, and integrates with Step Functions and Lambda.

### Related Services

- [[Rekognition]]: Image analysis (distinct from documents).
- [[Lambda]]: Automates document workflows.
- [[Comprehend]]: Extracts meaning from extracted text.

### Related Concepts

- OCR: Optical character recognition.
- Document Structure: Tables and forms preserved.
- Automated Processing: Pipeline from scan to data.
```

- [ ] **Step 3: Create `08 Machine Learning/Index.md`**

```markdown
#AWS #MOC
### Machine Learning — Index

AI/ML services for building intelligent applications.

## Platform

- [[SageMaker]]
- [[Bedrock]]

## Language & Speech

- [[Comprehend]]
- [[Polly]]
- [[Transcribe]]
- [[Translate]]
- [[Lex]]
- [[Kendra]]

## Vision & Documents

- [[Rekognition]]
- [[Textract]]
```

- [ ] **Step 4: Verify and commit**

```bash
ls "08 Machine Learning" | wc -l
```

Expected: 11 (10 notes + `Index.md`).

```bash
git add -A && git commit -m "feat: build 08 Machine Learning domain (3 new notes + index)"
```

---

### Task 10: 09 Integration — moves + 3 new notes + index

**Files:**
- Move (via `tools/retag.py`): all 3 Integration rows
- Create: `09 Integration/Step Functions.md`, `09 Integration/AppSync.md`, `09 Integration/Amazon MQ.md`
- Create: `09 Integration/Index.md`

**Interfaces:**
- Consumes: `tools/retag.py`
- Produces: 3 new notes (tag `#AWS #Service #Integration`), `Index.md` linking 6 notes

- [ ] **Step 1: Run the move tool**

```bash
python3 tools/retag.py
ls "09 Integration"
```

Expected: `SQS.md`, `SNS.md`, `EventBridge.md`.

- [ ] **Step 2: Create the 3 new Integration notes** (full files):

`09 Integration/Step Functions.md`:
```markdown
#AWS #Service #Integration
### Step Functions

AWS Step Functions orchestrates workflows by coordinating Lambdas, ECS tasks, and other services as state machines. It handles retries, branching, parallel execution, and human approval steps, making it the standard way to build reliable multi-step serverless processes.

### Related Services

- [[Lambda]]: Common task type in workflows.
- [[SQS]]: Message queues for decoupling.
- [[EventBridge]]: Schedules workflow triggers.

### Related Concepts

- State Machine: Defined workflow of states.
- Standard vs Express: Long-running vs high-volume executions.
- Retries & Error Handling: Built-in resilience.
```

`09 Integration/AppSync.md`:
```markdown
#AWS #Service #Integration
### AppSync

AWS AppSync is a managed GraphQL service that builds real-time and offline-capable APIs. It resolves queries against DynamoDB, Lambda, and other data sources, supports subscriptions for live updates, and authenticates with Cognito, IAM, or API keys.

### Related Services

- [[DynamoDB]]: Common data source.
- [[Lambda]]: Custom resolvers.
- [[Cognito]]: User authentication.

### Related Concepts

- GraphQL: Typed query language.
- Resolvers: Map fields to data sources.
- Subscriptions: Real-time push updates.
```

`09 Integration/Amazon MQ.md`:
```markdown
#AWS #Service #Integration
### Amazon MQ

Amazon MQ is a managed message broker for Apache ActiveMQ and RabbitMQ. It provides JMS and AMQP protocols for applications using open-source brokers, offering a migration path from self-managed brokers without rewriting applications.

### Related Services

- [[SQS]]: Native AWS queue alternative.
- [[SNS]]: Pub/sub alternative.

### Related Concepts

- JMS/AMQP: Standard messaging protocols.
- Broker: Server hosting queues/topics.
- Lift-and-Shift: Migrate existing brokers.
```

- [ ] **Step 3: Create `09 Integration/Index.md`**

```markdown
#AWS #MOC
### Integration — Index

Queues, topics, and event routing.

- [[SQS]]
- [[SNS]]
- [[EventBridge]]
- [[Step Functions]]
- [[AppSync]]
- [[Amazon MQ]]
```

- [ ] **Step 4: Verify and commit**

```bash
ls "09 Integration" | wc -l
```

Expected: 7 (6 notes + `Index.md`).

```bash
git add -A && git commit -m "feat: build 09 Integration domain (3 new notes + index)"
```

---

### Task 11: 10 Management — moves + 6 new notes + index

**Files:**
- Move (via `tools/retag.py`): all 3 Management rows
- Create: `10 Management/Systems Manager.md`, `10 Management/Control Tower.md`, `10 Management/Compute Optimizer.md`, `10 Management/CloudShell.md`, `10 Management/AWS Organizations.md`, `10 Management/Trusted Advisor.md`
- Create: `10 Management/Index.md`

**Interfaces:**
- Consumes: `tools/retag.py`
- Produces: 6 new notes (tag `#AWS #Service #Management`), `Index.md` linking 9 notes

- [ ] **Step 1: Run the move tool**

```bash
python3 tools/retag.py
ls "10 Management"
```

Expected: `CloudWatch.md`, `CloudFormation.md`, `Management Console.md`.

- [ ] **Step 2: Create the 6 new Management notes** (full files):

`10 Management/Systems Manager.md`:
```markdown
#AWS #Service #Management
### Systems Manager

AWS Systems Manager gives you operational control across EC2 and on-premises resources. It includes Parameter Store (secure key-value storage), Run Command (remote commands), Patch Manager, Session Manager, and State Manager for unified configuration and automation.

### Related Services

- [[EC2]]: Primary managed resource.
- [[CloudWatch]]: Monitoring alongside SSM.
- [[Lambda]]: Automation hooks.

### Related Concepts

- Parameter Store: Secure config storage.
- Run Command: Execute commands at scale.
- Session Manager: Shell access without inbound ports.
```

`10 Management/Control Tower.md`:
```markdown
#AWS #Service #Management
### Control Tower

AWS Control Tower establishes a multi-account environment with guardrails. It creates accounts via AWS Organizations, applies preventive and detective controls (SCPs + Config rules), and provides a landing zone with centralized logging and identity.

### Related Services

- [[AWS Organizations]]: Account structure underneath.
- [[IAM Identity Center]]: Identity for the landing zone.
- [[Security Hub]]: Aggregates guardrail findings.

### Related Concepts

- Landing Zone: Baseline multi-account setup.
- Guardrails: Preventive/detective controls.
- Account Factory: Standardized account creation.
```

`10 Management/Compute Optimizer.md`:
```markdown
#AWS #Service #Management
### Compute Optimizer

AWS Compute Optimizer uses machine learning to recommend optimal EC2 instance types, Auto Scaling configurations, EBS volumes, and Lambda memory. Recommendations reduce cost while maintaining performance based on utilization history.

### Related Services

- [[EC2]]: Instance right-sizing recommendations.
- [[Auto Scaling]]: Configuration guidance.
- [[Trusted Advisor]]: Complementary cost checks.

### Related Concepts

- Right-Sizing: Match resources to usage.
- Utilization Analysis: ML on CloudWatch metrics.
- Savings: Cost reduction recommendations.
```

`10 Management/CloudShell.md`:
```markdown
#AWS #Service #Management
### CloudShell

AWS CloudShell is a browser-based shell with the AWS CLI and other tools pre-installed. It is authenticated with your console session, includes 1 GB of persistent storage, and lets you manage AWS resources without local setup.

### Related Services

- [[AWS CLI]]: The command-line tool available in CloudShell.
- [[Management Console]]: Launches CloudShell.
- [[IAM]]: Uses your console identity.

### Related Concepts

- Browser Shell: No local install.
- Pre-Authenticated: Uses console credentials.
- Persistent Storage: 1 GB home directory.
```

`10 Management/AWS Organizations.md`:
```markdown
#AWS #Service #Management
### AWS Organizations

AWS Organizations centrally manages multiple AWS accounts. It provides consolidated billing, Service Control Policies (SCPs) for guardrails, and organizational units (OUs) to organize accounts — the foundation for multi-account architecture.

### Related Services

- [[Control Tower]]: Automates Organizations-based landing zones.
- [[IAM]]: Permissions within each account.
- [[IAM Identity Center]]: SSO across organization accounts.

### Related Concepts

- OU: Organizational unit grouping accounts.
- SCP: Guardrails on account permissions.
- Consolidated Billing: Single bill for all accounts.
```

`10 Management/Trusted Advisor.md`:
```markdown
#AWS #Service #Management
### Trusted Advisor

AWS Trusted Advisor inspects your environment against best practices for cost optimization, performance, security, fault tolerance, and service limits. Checks range from S3 bucket permissions to unused resources; core checks are free, with full checks on paid support plans.

### Related Services

- [[AWS Support Plans]]: Defines which checks are available.
- [[Security Hub]]: Broader security posture checks.
- [[Compute Optimizer]]: Deeper cost recommendations.

### Related Concepts

- Best Practices: Automated checks across categories.
- Service Limits: Alerts on approaching quotas.
- Core Checks: Free subset for all accounts.
```

- [ ] **Step 3: Create `10 Management/Index.md`**

```markdown
#AWS #MOC
### Management — Index

Monitoring, provisioning, and governance.

## Monitoring & Operations

- [[CloudWatch]]
- [[Systems Manager]]

## Provisioning & Governance

- [[CloudFormation]]
- [[Control Tower]]
- [[AWS Organizations]]
- [[Trusted Advisor]]
- [[Security Hub]]

## Console & Cost

- [[Management Console]]
- [[CloudShell]]
- [[AWS CLI]]
- [[Compute Optimizer]]
```

Note: `[[Security Hub]]` and `[[AWS CLI]]` are cross-domain links (Security / Developer Tools) — this is intentional and valid. Update the count expectation: this index lists 11 entries but only 9 are in this folder.

- [ ] **Step 4: Verify and commit**

```bash
ls "10 Management" | wc -l
```

Expected: 10 (9 notes + `Index.md`).

```bash
git add -A && git commit -m "feat: build 10 Management domain (6 new notes + index)"
```

---

### Task 12: 11 Developer Tools — moves + 3 new notes + index

**Files:**
- Move (via `tools/retag.py`): all 7 DevTools rows
- Create: `11 Developer Tools/X-Ray.md`, `11 Developer Tools/Cloud9.md`, `11 Developer Tools/CodeArtifact.md`
- Create: `11 Developer Tools/Index.md`

**Interfaces:**
- Consumes: `tools/retag.py`
- Produces: 3 new notes (tag `#AWS #Service #DevTools`), `Index.md` linking 10 notes

- [ ] **Step 1: Run the move tool**

```bash
python3 tools/retag.py
ls "11 Developer Tools"
```

Expected: `CodeCommit.md`, `CodeBuild.md`, `CodeDeploy.md`, `CodePipeline.md`, `CodeStar.md`, `Application Composer.md`, `AWS CLI.md`.

- [ ] **Step 2: Create the 3 new DevTools notes** (full files):

`11 Developer Tools/X-Ray.md`:
```markdown
#AWS #Service #DevTools
### X-Ray

AWS X-Ray traces requests as they flow through distributed applications. It maps the services and calls behind each request, identifies latency bottlenecks and errors, and integrates with Lambda, API Gateway, and EC2 via the X-Ray SDK.

### Related Services

- [[Lambda]]: Automatic tracing integration.
- [[API Gateway]]: Traces API request paths.
- [[CloudWatch]]: Metrics and logs alongside traces.

### Related Concepts

- Trace: End-to-end request path.
- Segment/Subsegment: Service-level trace units.
- Service Map: Visual dependency graph.
```

`11 Developer Tools/Cloud9.md`:
```markdown
#AWS #Service #DevTools
### Cloud9

AWS Cloud9 is a cloud-based integrated development environment (IDE). It runs in the browser with terminal, code editor, and debugging tools, pairs with EC2 environments, and is often used for serverless development with Lambda.

### Related Services

- [[EC2]]: Backs Cloud9 environments.
- [[Lambda]]: Serverless development workflow.
- [[CodeCommit]]: Git repositories from the IDE.

### Related Concepts

- Cloud IDE: Browser-based development.
- Environment: Provisioned workspace.
- Collaboration: Real-time pair programming.
```

`11 Developer Tools/CodeArtifact.md`:
```markdown
#AWS #Service #DevTools
### CodeArtifact

AWS CodeArtifact is a fully managed artifact repository for storing and sharing packages (npm, Maven, PyPI, NuGet). It integrates with CodeBuild and CodePipeline for secure package delivery, supports proxying upstream registries, and provides private package hosting.

### Related Services

- [[CodeBuild]]: Resolves packages from CodeArtifact.
- [[CodePipeline]]: Automates package deployment.
- [[CodeCommit]]: Source control alongside packages.

### Related Concepts

- Repository: Logical package store.
- Upstream: Proxy to public registries.
- Package Resolution: Dependency fetching.
```

- [ ] **Step 3: Create `11 Developer Tools/Index.md`**

```markdown
#AWS #MOC
### Developer Tools — Index

CI/CD and developer services.

## CI/CD

- [[CodePipeline]]
- [[CodeBuild]]
- [[CodeDeploy]]
- [[CodeCommit]]

## Development Environment

- [[CodeStar]]
- [[Cloud9]]
- [[AWS CLI]]
- [[Application Composer]]

## Packages, Artifacts & Observability

- [[CodeArtifact]]
- [[X-Ray]]
```

- [ ] **Step 4: Verify and commit**

```bash
ls "11 Developer Tools" | wc -l
```

Expected: 11 (10 notes + `Index.md`).

```bash
git add -A && git commit -m "feat: build 11 Developer Tools domain (3 new notes + index)"
```

---

### Task 13: 12 Migration — moves + 1 new note + index

**Files:**
- Move (via `tools/retag.py`): all 8 Migration rows
- Create: `12 Migration/Transfer Family.md`
- Create: `12 Migration/Index.md`

**Interfaces:**
- Consumes: `tools/retag.py`
- Produces: 1 new note (tag `#AWS #Service #Migration`), `Index.md` linking 9 notes

- [ ] **Step 1: Run the move tool**

```bash
python3 tools/retag.py
ls "12 Migration"
```

Expected: `MGN.md`, `Application Discovery Service.md`, `DMS.md`, `SCT.md`, `Migration Hub.md`, `Snowball.md`, `Snowball Edge.md`, `Snowcone.md`.

- [ ] **Step 2: Create the 1 new Migration note** (full file):

`12 Migration/Transfer Family.md`:
```markdown
#AWS #Service #Migration
### Transfer Family

AWS Transfer Family is a managed service for moving data in and out of S3 and EFS using SFTP, FTPS, and FTP protocols. It provides managed servers, integrates with IAM for user access, and suits legacy file-transfer workloads migrating to AWS.

### Related Services

- [[S3]]: Primary storage for transfer servers.
- [[EFS]]: Alternative storage destination.
- [[DataSync]]: High-volume automated transfer.

### Related Concepts

- SFTP/FTPS/FTP: File transfer protocols.
- Managed Server: No servers to operate.
- Identity Provider: IAM or AD integration.
```

- [ ] **Step 3: Create `12 Migration/Index.md`**

```markdown
#AWS #MOC
### Migration — Index

Migrate and transfer tools.

## Server & Application Migration

- [[MGN]]
- [[Application Discovery Service]]
- [[Migration Hub]]

## Database Migration

- [[DMS]]
- [[SCT]]

## Data Transfer

- [[Snowball]]
- [[Snowball Edge]]
- [[Snowcone]]
- [[Transfer Family]]
```

- [ ] **Step 4: Verify and commit**

```bash
ls "12 Migration" | wc -l
```

Expected: 10 (9 notes + `Index.md`).

```bash
git add -A && git commit -m "feat: build 12 Migration domain (1 new note + index)"
```

---

### Task 14: 13 Business — moves + 4 new notes + index

**Files:**
- Move (via `tools/retag.py`): both Business rows
- Create: `13 Business/Chime.md`, `13 Business/WorkSpaces.md`, `13 Business/WorkDocs.md`, `13 Business/SES.md`
- Create: `13 Business/Index.md`

**Interfaces:**
- Consumes: `tools/retag.py`
- Produces: 4 new notes (tag `#AWS #Service #Business`), `Index.md` linking 6 notes

- [ ] **Step 1: Run the move tool**

```bash
python3 tools/retag.py
ls "13 Business"
```

Expected: `Connect.md`, `Elastic Transcoder.md`.

- [ ] **Step 2: Create the 4 new Business notes** (full files):

`13 Business/Chime.md`:
```markdown
#AWS #Service #Business
### Chime

Amazon Chime provides online meetings, video conferencing, chat, and business calling. It integrates with Alexa for Business and calendar tools, supports screen sharing and recording, and offers a secure communications layer for organizations.

### Related Services

- [[Connect]]: Contact-center telephony (distinct from Chime).
- [[WorkDocs]]: Document collaboration alongside meetings.
- [[WorkSpaces]]: Virtual desktops for remote work.

### Related Concepts

- Video Conferencing: Meetings and screen share.
- Chat & Calling: Unified communications.
- Alexa for Business: Voice integration.
```

`13 Business/WorkSpaces.md`:
```markdown
#AWS #Service #Business
### WorkSpaces

Amazon WorkSpaces is a fully managed virtual desktop infrastructure (VDI) service. It provisions Windows or Linux desktops in the cloud, lets users access them from any device, and provides persistent, pay-as-you-go desktops without managing the underlying infrastructure.

### Related Services

- [[WorkDocs]]: Secure storage for desktop users.
- [[Chime]]: Voice/video for remote workers.
- [[IAM]]: User identity for desktops.

### Related Concepts

- VDI: Virtual desktop infrastructure.
- BYOD: Access from personal devices.
- Persistent Desktops: User-specific state retained.
```

`13 Business/WorkDocs.md`:
```markdown
#AWS #Service #Business
### WorkDocs

Amazon WorkDocs is a secure content collaboration service for creating, sharing, and storing documents. It supports versioning, commenting, and access control, integrates with WorkSpaces, and offers audit logging for compliance.

### Related Services

- [[WorkSpaces]]: Desktop integration.
- [[Chime]]: Collaboration alongside documents.
- [[S3]]: Underlying object storage.

### Related Concepts

- Document Collaboration: Shared workspaces.
- Version Control: Track document revisions.
- Access Controls: Fine-grained permissions.
```

`13 Business/SES.md`:
```markdown
#AWS #Service #Business
### SES

Amazon Simple Email Service (SES) is a cost-effective platform for sending and receiving email at scale. It handles marketing and transactional email, supports deliverability monitoring, reputation management, and integrates with SNS, Lambda, and other services.

### Related Services

- [[SNS]]: Alternative push notification channel.
- [[Lambda]]: Processes inbound email.
- [[Route 53]]: Domain and DKIM DNS records.

### Related Concepts

- Deliverability: Inbox placement and reputation.
- Transactional Email: Password resets, receipts.
- DKIM/SPF: Email authentication.
```

- [ ] **Step 3: Create `13 Business/Index.md`**

```markdown
#AWS #MOC
### Business — Index

Productivity and end-user applications.

- [[Chime]]
- [[Connect]]
- [[WorkSpaces]]
- [[WorkDocs]]
- [[SES]]
- [[Elastic Transcoder]]
```

- [ ] **Step 4: Verify and commit**

```bash
ls "13 Business" | wc -l
```

Expected: 7 (6 notes + `Index.md`).

```bash
git add -A && git commit -m "feat: build 13 Business domain (4 new notes + index)"
```

---

### Task 15: Global verification — counts, links, tags

**Files:**
- Modify: none (verification only)
- Read-only checks over the whole vault

**Interfaces:**
- Consumes: everything from Tasks 1–14

- [ ] **Step 1: Verify per-folder note counts**

```bash
for d in "01 Concepts" "02 Compute" "03 Storage" "04 Database" "05 Networking" "06 Security" "07 Analytics" "08 Machine Learning" "09 Integration" "10 Management" "11 Developer Tools" "12 Migration" "13 Business"; do printf "%s: " "$d"; ls "$d"/*.md | wc -l; done
```

Expected (each folder incl. `Index.md`): 25, 16, 22, 14, 13, 21, 8, 11, 7, 10, 11, 10, 7.

- [ ] **Step 2: Verify no stale wikilinks to old names**

```bash
grep -rn "\[\[Amazon " --include="*.md" . 2>/dev/null | grep -v "/docs/" || echo "none"
grep -rn "\[\[AWS AWS" --include="*.md" . 2>/dev/null || echo "none"
grep -rn "\[\[AWS .*|" --include="*.md" . 2>/dev/null || echo "none"
```

Expected: all three print `none` (no references to `Amazon <X>` or the old `AWS AWS` pattern).

- [ ] **Step 3: Verify every wikilink target resolves to a file**

Run a Python check:

```python
import os, re
root = "/Users/lizard/Library/Mobile Documents/iCloud~md~obsidian/Documents/AWS"
skip = {".git", ".trash", ".obsidian", ".makemd", ".space", "Tags", "docs"}
names = set()
for dp, ds, fs in os.walk(root):
    ds[:] = [d for d in ds if d not in skip]
    for f in fs:
        if f.endswith(".md"):
            names.add(os.path.splitext(f)[0])
missing = []
for dp, ds, fs in os.walk(root):
    ds[:] = [d for d in ds if d not in skip]
    for f in fs:
        if not f.endswith(".md"):
            continue
        p = os.path.join(dp, f)
        for m in re.findall(r"\[\[([^\]|]+)", open(p, encoding="utf-8").read()):
            target = m.split("/")[-1].strip()
            if target and target not in names:
                missing.append(f"{p}: [[{target}]]")
if missing:
    print("\n".join(sorted(set(missing))))
else:
    print("all wikilinks resolve")
```

Expected: prints `all wikilinks resolve`. Any missing target must be fixed by creating the note or correcting the link.

- [ ] **Step 4: Verify tag line format across all notes**

```bash
grep -rn "^#AWS #" --include="*.md" . | grep -v "/docs/" | grep -v "#AWS #MOC" | wc -l
```

Expected: 162 (one per content note; 13 MOC index notes + Home.md excluded). Then spot-check tags:

```bash
head -1 "02 Compute/EC2.md" "06 Security/IAM.md" "01 Concepts/IaaS.md" "Home.md"
```

Expected: `#AWS #Service #Compute`, `#AWS #Service #Security`, `#AWS #Concept #Concept`, `#AWS #MOC`.

- [ ] **Step 5: Verify old folders are empty or gone**

```bash
ls AWS Amazon Cloud EC2 S3 2>/dev/null
```

Expected: empty or directory-not-found for all five old folders (only `Tags/` remains, empty).

- [ ] **Step 6: Final commit**

```bash
git add -A
git status --short | head -20
git commit -m "chore: complete AWS vault restructure"
```

---

## Self-Review

**Spec coverage:** Every domain folder, every moved note (91), every new note (71), the 13 index notes, and `Home.md` are mapped in a concrete task. Deep-dive requirements (EC2, Lambda, S3, IAM) are explicit. Hub deletions (`AWS.md`, `Amazon.md`, `S3.md`) are in Task 1. `Tags/` and `.trash/` are untouched.

**Placeholder scan:** All 71 new notes have complete content inline. No "TBD"/"similar to Task N" steps. The one earlier self-link (`[[Lambda]]` in Task 3 Step 3) is flagged and replaced.

**Type/naming consistency:** Wikilink basenames match created filenames everywhere (e.g. `Security Groups vs NACLs.md` ↔ `[[Security Groups vs NACLs]]`; `S3 Standard-Infrequent Access (IA).md` ↔ `[[S3 Standard-Infrequent Access (IA)]]`). The `tools/retag.py` manifest is the single source of truth for renames, so `retag_content`/`relink_map` stay in sync. `Home.md` uses path-qualified `[[01 Concepts/Index|Concepts]]` links matching the `Index.md` naming decided in Task 1 Step 6.
