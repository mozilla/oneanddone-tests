Selenium Tests for oneanddone
====================

Thank you for checking out Mozilla's OneAndDone test suite. Mozilla and the Mozwebqa team are grateful for the help and hard work of many contributors like yourself.
The following contributors have submitted pull requests to oneanddone-tests:

https://github.com/mozilla/oneanddone-tests/contributors

Getting involved as a contributor
------------------------------------------

We love working with contributors to fill out the Selenium test coverage for oneanddone-tests, but it does require a few skills.   You will need to know some Python, some Selenium and you will need some basic familiarity with Github.

If you know some Python, it's worth having a look at the Selenium framework to understand the basic concepts of browser based testing and especially page objects. Our suite uses [Selenium WebDriver][webdriver].

To brush up on Python skills before engaging with us, [Dive Into Python][dive] is an excellent resource.  MIT also has [lecture notes on Python][mit] available through their open courseware.The programming concepts you will need to know include functions, working with classes, and some object oriented programming basics.

[mit]: http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-189-a-gentle-introduction-to-programming-using-python-january-iap-2011/
[dive]: http://www.diveintopython.net/toc/index.html
[webqa]: http://quality.mozilla.org/teams/web-qa/
[webdriver]: http://seleniumhq.org/docs/03_webdriver.html

Questions are always welcome
----------------------------
While we take pains to keep our documentation updated, the best source of information is those of us who work on the project.  Don't be afraid to join us in irc.mozilla.org #mozwebqa to ask questions about our Selenium tests.  Mozilla also hosts the #mozillians chat room to answer your general questions about contributing to Mozilla.

[mozwebqa]:http://02.chat.mibbit.com/?server=irc.mozilla.org&channel=#mozwebqa
[mozillians]:http://02.chat.mibbit.com/?server=irc.mozilla.org&channel=#mozillians

How to Set up and Build the Tests Locally
-----------------------------------------
This repository contains Selenium tests used to test the oneanddone website.

Detailed instructions for getting set up and running our Selenium tests can be found on the MDN website at https://developer.mozilla.org/en-US/docs/Mozilla/QA/Running_Web_QA_automated_tests.

Please follow the steps in that document and feel free to ask questions in irc if you get stuck.

Writing Tests
-------------

If you want to get involved and add more tests then there's just a few things
we'd like to ask you to do:

1. Use an existing file from this repository as a template for all new tests and page objects
2. Follow our simple [style guide][Style Guide]
3. Fork this project with your own GitHub account
4. Add your test into the "tests" folder and the necessary methods for it into the appropriate file in "pages"
5. Make sure all tests are passing and submit a pull request with your changes

[GitHub Templates]: https://github.com/mozilla/mozwebqa-test-templates 
[Style Guide]: https://wiki.mozilla.org/QA/Execution/Web_Testing/Docs/Automation/StyleGuide

License
-------
This software is licensed under the [MPL] 2.0:

    This Source Code Form is subject to the terms of the Mozilla Public
    License, v. 2.0. If a copy of the MPL was not distributed with this
    file, You can obtain one at http://mozilla.org/MPL/2.0/.

[MPL]: http://www.mozilla.org/MPL/2.0/
