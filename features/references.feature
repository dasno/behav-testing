Feature: Creation, modificitaion and deletion of referenced content items.

    Scenario: Accessing method relation modification form
        Given user is an administrator.
        And user is on the method edit page.
        When user selects Relations tab.
        Then user is on the relation modification form.
    
    Scenario: Add reference to related tool to an existing method.
        Given user is an administrator.
        And some method already exists.
        And user is on method relation modification form.
        When user inputs name of his desired tool.
        And user selects it and click Save.
        Then related tool has been added to the method. 

    Scenario: Remove reference to related tool from method.
        Given user is an administrator.
        And is at edit method's relations form.
        When user clicks on small x in the top left corner of tool and clicks Save.
        Then reference to that tool has been removed.


    Scenario: Tool referenced by method is reachable via navigating to the method and clicking through to that tool.
        Given user is consumer.
        And method is created and published.
        And published method references a tool.
        When user clicks to list of methods.
        And selects said method.
        And clicks on referenced too.
        Then page of that tool will open.

