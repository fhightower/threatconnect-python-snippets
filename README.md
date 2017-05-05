# ThreatConnect Python SDK Sublime Text Snippets

The goal of these snippets are to make writing scripts and applications that talk to ThreatConnect quick and easy.

As the name implies, you will need access to [ThreatConnect's](https://threatconnect.com) API before these snippets are useful. Additionally, these snippets are designed for use with [Sublime Text](https://www.sublimetext.com/3). If you haven't tried it yet, I strongly encourage you to do so.

## Snippet Design Paradigm

If a paradigms is too rich for your blood, feel free to jump to the [Examples](#examples) section below. For the rest, each snippet is constructed as follows:

```
tc<action><object>
```

The `<action>` is usually one letter that represents *what* we want to do (refer to the [Actions](#actions) section below). The `<object>` specifies the type of object (refer to the [Objects](#objects) section below for a list of possible objects) to which the aforementioned action will be done. For you language buffs, the `<object>` is really an indirect object.

### Actions

List of possible actions coming soon...

### Objects

List of possible actions coming soon...

## Examples

- `tcrindicators`: in this snippet, `r` is the action (it stands for "**r**etrieve") and `indicators` are the object. Thus, this snippet provides code to retrieve indicators.
- `tcrgroups`: in this snippet, `r` is the action (it stands for "**r**etrieve") and `groups` are the object. Thus, this snippet provides code to retrieve groups.
- `tcfindicators`: in this snippet, `f` is the action (it stands for "**f**ilter") and `indicators` are the object. Thus, this snippet provides code to filter indicators.
- `tcfgroups`: in this snippet, `f` is the action (it stands for "**f**ilter") and `groups` are the object. Thus, this snippet provides code to filter groups.

## Complete list

More in this section is coming soon...

### Misc.

- `tcconfig`: get a standard ThreatConnect configuration to start a script

### Indicators

More in this section is coming soon...

### Groups

More in this section is coming soon...

### Victims

More in this section is coming soon...
