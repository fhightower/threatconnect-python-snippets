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

- `tcconfig`: get a standard ThreatConnect configuration to start a script

### Indicators

#### Retrieving Indicators

- `tcrindicators`: retrieve indicators (all indicator types)
- Coming soon...

#### Filtering Indicators

Coming soon...

#### Creating Indicators

Coming soon...

#### Deleting Indicators

Coming soon...

### Groups

#### Retrieving Groups

- `tcradversaries`: retrieve adversaries
- `tcrcampaigns`: retrieve campaigns
- `tcrdocuments`: retrieve documents
- `tcremails`: retrieve emails
- `tcrgroups`: retrieve groups (all group types)
- `tcrincidents`: retrieve incidents
- `tcrsignatures`: retrieve signatures
- `tcrthreats`: retrieve threats

#### Filtering Groups

Coming soon...

#### Creating Groups

- `tccadversaries`: create adversaries
- `tcccampaigns`: create campaigns
- `tccdocuments`: create documents
- `tccemails`: create emails
- `tccincidents`: create incidents
- `tccsignatures`: create signatures
- `tccthreats`: create threats

#### Updating Groups

- `tcuadversaries`: update adversaries
- `tcucampaigns`: update campaigns
- `tcudocuments`: update documents
- `tcuemails`: update emails
- `tcuincidents`: update incidents
- `tcusignatures`: update signatures
- `tcuthreats`: update threats

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

#### Retrieving Victims

#### Filtering Victims

#### Creating Victims

#### Updating Victims

#### Deleting Victims

### Metadata

#### Retrieving Metadata

Coming soon...

#### Adding Metadata

- `tcaattribute`: adding an attribute
- `tcaratings`: adding a threat and confidence rating
- `tcasecuritylabel`: adding a security label
- `tcatag`: adding a tag

#### Updating Metadata

Coming soon...

#### Deleting Metadata

Coming soon...
