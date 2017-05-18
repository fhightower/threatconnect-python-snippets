#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Create snippets based on a template.

For example, once you create a snippet that will filter adversaries, you can easily create copies of that snippet for all of the other group types. This script is code, to write code (snippets), to write code (scripts that talk to ThreatConnect's API via the Python SDK).
"""

# define the starting template we will use to create the other snippets
snippet_template = """
<snippet>
    <content><![CDATA[
# add filter(s) for adversaries
filter1 = adversaries.add_filter()
filter1.add_${1:owner}(${2:owner})

]]></content>
    <tabTrigger>tcfadversaries</tabTrigger>
    <scope>source.python</scope>
</snippet>
"""

# these are the names of the objects in the snippet that should be replaced
object_names = ["adversaries", "adversary"]

# replace any brackets with other characters (this will be undone later)
snippet_template = snippet_template.replace("{", "!?!").replace("}", "?!?")

# replace all of the object names in the current snippet with brackets
for name in object_names:
    # replace the object name
    snippet_template = snippet_template.replace(name, "{}")
    # replace the capitalized object name
    snippet_template = snippet_template.replace(name.title(), "{}")

# this is the prefix of the action we are performing with this snippet
action_letter = "f"
groups = ["campaign", "document", "email", "incident", "signature", "threat"]
# indicators = ["address", "file", "host", "url"]

# create a snippet for each group
for group in groups:
    plural_group = group + "s"

    # fill in the snippet_template with the group names as appropriate
    new_snippet = snippet_template.format(plural_group, plural_group,
                                          plural_group)
    # add the original brackets back into the snippet
    new_snippet = new_snippet.replace("?!?", "}").replace("!?!", "{")

    # write the new snippet to the appropriate file
    with open("./../tc_python_snippets/" + "tc" + action_letter +
              plural_group + ".sublime-snippet", "w+") as f:
        f.write(new_snippet)
