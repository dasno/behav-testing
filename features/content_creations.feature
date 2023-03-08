Feature: Creation, modification and deletion of content items

    Scenario: Opening method creation form
        Given user is an administrator.
        When user clicks "Add new" in side panel and selects method.
        Then Method creation form shows up.
    
    Scenario: Filling method creation form and saving
        Given user is an administrator.
        And is on method creation form.
        When user fills out form with correct information and clicks "Save".
        Then method is created.

    Scenario: Opening method edit form
        Given user is an administrator.
        And at least one method exists.
        And user is on page of specific method.
        When user clicks on "Edit" button in the sidebar.
        Then edit method form will show up.
    
    Scenario: Editing a method
        Given user is an administrator.
        And user is on the method edit form.
        When user changes one or more fields and cliks "Save".
        Then Method has been modified.
    
    Scenario: Accessing content page
        Given user is an administrator.
        And user is on home page.
        When user selects "Contents" from the side bar.
        Then user is on content page.

    Scenario: Delete an content item
        Given user is an administrator.
        And user is on content page.
        And user in in a folder where specific item is located.
        When user clicks on checkbox next to method and clicks on delete icon and confirms.
        Then item is deleted.

    Scenario: Not filling all required fields in method
        Given user is an administrator.
        And user is on the method creation from.
        When user don't fill in the title of a method and saves.
        Then Prompt shows up.

    Scenario: Check method visibility
        Given user is an administrator.
        And a method has been created.
        When user goes to a methods page.
        Then created method shoud be visible as unpublished (red).



