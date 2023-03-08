Feature: Modifying visiblity of content items and sending them to a review.

    Scenario: Sending content to a review process.
        Given user is an administrator.
        And unpublished content item is created.
        When user selects "Submit for publication".
        Then content item will change it's review state to pending.

    Scenario: Reviewer can see content item with pending review status.
        Given user is a reviewer.
        And content item with pending review status has been created.
        When user opens list of content items.
        Then user will see that content item (green color).
    
    Scenario: Reviewer can publish content item with pending review status
        Given user is a reviewer.
        And content item has been created.
        And that content item has pending rewiew status.
        And user has that content item opened.
        When he selects "Publish" option from sidebar menu.
        Then content item will change it's state to published.

    Scenario: Reviewer can't see content item with private review status.
        Given user is a reviewer.
        And content item was created.
        And it was not published or sent to review.
        When user open list of content items of a certain type.
        Then user can't see that content item.

