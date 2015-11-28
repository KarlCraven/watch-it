# Watch It!
Watch It! is a Python module for generating an HTML document of Movie and TV Show recommendations using data from a pre-prepared .csv file containing the relevant data. Once the page has been generated and opens in your browser, you can hover over the media tiles to view additional information, or click on them to watch a Youtube video trailer.

## Usage
1. Replace the data in the included media.csv file with the data you want included on the webpage. Please note that certain columns only relate to Movies and certain columns only relate to TV Shows. If you review the example data you should be able to see which is which.
2. All of the enclosed files should be kept in the same directory together.
3. Run the **media_database.py** module from IDLE to begin the generation of the webpage. It will open up in your default browser.

## Appearance
This module makes use of Bootstrap but some classes and styles have been adjusted in the **watch_it.py** file. Feel free to customize the appearance further to suit your needs.

## Questions?
Contact me on Twitter @swisodi

## Credits
This module is adapted from the Fresh Tomatoes module created for the [Programming Foundations With Python](https://www.udacity.com/course/viewer#!/c-ud036-nd/l-3602388773/m-3658268560) course offered by [Udacity](www.udacity.com). These files constitute my submission for the final project in this course and for the first project in their Full Stack Web Developer Nanodegree course.

## Changelog
The following changes were made to the default Fresh Tomatoes code:
* I modified the media.py module to include two child classes for Movie and TVshow, which both inherit from the Media class, and have additional attributes of their own.
* I amended the media_database.py file so that the data is now read from the media.csv file in the package rather than being included within the body of the Python code itself. This should make the addition of further media to the webpage much easier.
* I also customized the Fresh Tomatoes module to change the appearance and displayed content of the output HTML file in the following ways:
   * Changed the css to generate a darker theme for the page, allow up to 4 columns of tiles for larger devices, added a larger H1 syle, and adjusted some padding & margins.
   * Output additional information about the Media objects within the tiles. This information is different for Movies than it is for TV Shows.
  * Added a JQuery function to animate the contents of each media tile as the user hovers their mouse over it. This action reveals the additional information hidden by default below the media images when the page loads, allowing for the inclusion of more information without breaking the layout of the page.