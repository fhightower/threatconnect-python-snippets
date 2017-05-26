# ThreatConnect Python SDK Sublime Text Snippets

The goal of this project is to make snippets such that you can write a useful python script that talks with ThreatConnect's API in less than **less than 60 seconds**.

![demo](demo/tc_python_snippets.gif)

As the name implies, you will need access to [ThreatConnect's](https://threatconnect.com) API before these snippets are useful. Additionally, these snippets are designed for use with [Sublime Text](https://www.sublimetext.com/3). If you haven't tried it yet, I strongly encourage you to do so.

## Snippet Design Paradigm

If a paradigms isn't worth your time, feel free to jump to the [Examples](#examples) section below (I don't want to shortchange anyone). For the rest, each snippet is constructed as follows:

```
tc<action><object>
```

The `<action>` is usually one letter that represents *what* we want to do (refer to the [Actions](#actions) section below). The `<object>` specifies the type of object (refer to the [Objects](#objects) section below for a list of possible objects) to which the aforementioned action will be done. For you language buffs, the `<object>` is really an indirect object.

### Actions

| Desired Action | Action Prefix | Description |  
| --- | --- | --- |
| **R**etrieve | `r` | Retrieve something from ThreatConnect |
| **C**reate | `c` | Create something in ThreatConnect |
| **U**pdate | `u` | Update something that already exits in ThreatConnect |
| **D**elete | `d` | Delete something from ThreatConnect |
| **A**dd/set Metadata | `a` | Add metadata to an object |
| **L**oad Metadata | `l` | Load metadata for an object |
| **F**ilter | `f` | Filter objects when retrieving |  

### Objects

List of possible actions coming soon...

## Examples

- `tcrindicators`: in this snippet, `r` is the action (it stands for "**r**etrieve") and `indicators` are the object. Thus, this snippet provides code to retrieve indicators.
- `tcrgroups`: in this snippet, `r` is the action (it stands for "**r**etrieve") and `groups` are the object. Thus, this snippet provides code to retrieve groups.
- `tcfindicators`: in this snippet, `f` is the action (it stands for "**f**ilter") and `indicators` are the object. Thus, this snippet provides code to filter indicators.
- `tcfgroups`: in this snippet, `f` is the action (it stands for "**f**ilter") and `groups` are the object. Thus, this snippet provides code to filter groups.

## Complete List of Snippets

### Helpful Utility Snippets

- `tccommit`: Generic commit
- `tcconfig`: TC configuration heading
- `tcdelete`: Generic delete
- `tcfilter`: Generic filter
- `tcretrieve`: Generic retrieve
- `tctime`: Time format for TC's Py SDK (REQUIRES: from datetime import datetime)

### Indicators

#### Retrieving Indicators

- `tcrindicators`: Retrieve indicators (all indicator types)

##### Multi-Retrieve

- `tcrmaddresses`: Retrieve multiple IP addresses
- `tcrmemailAddresses`: Retrieve multiple email addresses
- `tcrmfiles`: Retrieve multiple file indicators
- `tcrmhosts`: Retrieve multiple hosts
- `tcrmurls`: Retrieve multiple URLs

##### Single Retrieve

- `tcrsaddress`: Retrieve a single IP address
- `tcrsemailAddress`: Retrieve a single email address
- `tcrsfile`: Retrieve a single file indicator
- `tcrshost`: Retrieve a single host
- `tcrsurl`: Retrieve a single URL

#### Filtering Indicators

- `tcfindicators`: Filter indicators

#### Creating Indicators

- `tccindicator`: Create indicator

#### Deleting Indicators

Coming soon...

### Groups

#### Retrieving Groups

- `tcradversaries`: Retrieve adversaries
- `tcrcampaigns`: Retrieve campaigns
- `tcrdocuments`: Retrieve documents
- `tcremails`: Retrieve emails
- `tcrgroups`: Retrieve groups (all group types)
- `tcrincidents`: Retrieve incidents
- `tcrsignatures`: Retrieve signatures
- `tcrthreats`: Retrieve threats

#### Filtering Groups

- `tcfadversaries`: Filter adversaries
- `tcfcampaigns`: Filter campaigns
- `tcfdocuments`: Filter documents
- `tcfemails`: Filter emails
- `tcfgroups`: Filter groups
- `tcfincidents`: Filter incidents
- `tcfsignatures`: Filter signatures
- `tcfthreats`: Filter threats

#### Creating Groups

- `tccadversary`: Create adversary
- `tcccampaign`: Create campaign
- `tccdocument`: Create document
- `tccemail`: Create email
- `tccincident`: Create incident
- `tccsignature`: Create signature
- `tccthreat`: Create threat

#### Updating Groups

- `tcuadversary`: Update adversary
- `tcucampaign`: Update campaign
- `tcudocument`: Update document
- `tcuemail`: Update email
- `tcuincident`: Update incident
- `tcusignature`: Update signature
- `tcuthreat`: Update threat

#### Deleting Groups

- `tcdadversaries`: delete adversaries
- `tcdcampaigns`: delete campaigns
- `tcddocuments`: delete documents
- `tcdemails`: delete emails
- `tcdincidents`: delete incidents
- `tcdsignatures`: delete signatures
- `tcdthreats`: delete threats

### Victims

Coming soon...

<!-- #### Retrieving Victims

#### Filtering Victims

#### Creating Victims

#### Updating Victims

#### Deleting Victims -->

### Metadata

#### Loading/Retrieving Metadata

- `tclassocgroups`: Retrieve associated groups
- `tclassocindicators`: Retrieve associated indicators
- `tclassocvictims`: Retrieve associated victims
- `tclassociations`: Load associations
- `tclattributes`: Load attributes
- `tclfileoccurrences`: Load file occurrences
- `tclsecurity_labels`: Load security labels
- `tcltags`: Load tags

#### Adding Metadata

- `tcaassocgroup`: Add an associated group
- `tcaassocindicator`: Add an associated indicator
- `tcaassocvictim`: Add an associated victim
- `tcaattribute`: Add an attribute
- `tcaratings`: Add threat and confidence ratings
- `tcasecuritylabel`: Add a security label
- `tcatag`: Add a tag

#### Updating Metadata

Coming soon...

#### Deleting Metadata

Coming soon...
