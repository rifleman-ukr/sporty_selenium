To run test on your computer you should have installed all required software and test_data.json 
can be edited if you desire.

| Step # |              Description              |                             Result                             |
|:------:|:-------------------------------------:|:--------------------------------------------------------------:|
|   1    |    Go to **Twitch** (customizable)    |       Twitch page is open and Search button is displayed       |
|   2    |       Click in the search icon        |       Search page is open and search input is displayed        |
|   3    | Input **StarCraft II** (customizable) |      Search results are displayed and category is clicked      |
|   4    |          Scroll down 2 times          |    Scroll down is performed and then scroll to last result     |
|   5    |          Select one streamer          | Last displayed streamer home page is open and screenshot taken |

During completion of this task few difficulties were faced. Some of them were successfully passed, 
but some are still incomplete and require some time to deal with. For example:
* In current representation of this test I didn't find a way to force framework to wait until the 
page is fully loaded, that's why in method streamer_page.wait_page_loaded() sleep is used. 
* Second issue I couldn't handle - popup mentioned in task notes. As I'm not a Twitch user
I didn't find a case where this popup is shown and obviously this test doesn't handle such behaviour.

Here is video example of test pass: 
https://drive.google.com/file/d/1HPzqLBDSj6vVLlTqiM2DuglQ9Pz8--Y2