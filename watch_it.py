import webbrowser   # webbrowser module
import os           # operating system module
import re           # regular expression module

# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Watch It! media & TV Show Recommendations</title>
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
            background-color: #111;
            color: #EEE;
        }
        .container {
            margin-top: 1em !important;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .media-tile {
            margin-bottom: 20px;
            padding-top: 20px;
            min-height: 470px;
            max-height: 470px;
            overflow: hidden;
        }
        .media-tile:hover {
            background-color: #222;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        p.genre {
            font-weight: bold;
        }
        p.metadata, p.genre {
            font-style: italic;
        }
        .media-tile h2, .media-tile p, .media-tile img {
            position:relative;
            top: 0px;
        }
        h1, h1 a, h1 a:hover, h1 a:visited, h1 a:active {
            font-size: 1.5em !important;
            margin-top: 0 !important;
            margin-bottom: 0.5em !important;
        }
    </style>
    <script type="text/javascript" charset="utf-8">

        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });

        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.media-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });

        // Animate in the media when the page loads
        $(document).ready(function () {
          $('.media-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });

        // Slide media image and information up on tile hover to display additional info that does not fit
        $(document).ready(function () {
            $(".media-tile").hover(function () {
                tp = $(this).children().css('top') == '-180px' ? '0px' : '-180px';
                $(this).children().stop().animate( {top: tp }, 1000);
            },
            function () {
                tp = $(this).children().css('top') == '0px' ? '-180px' : '0px';
                $(this).children().stop().animate( {top: tp }, 1000);
            });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
              <h1><a class="navbar-brand" href="#">Watch It! Movie and TV Show Recommendations</a></h1>
              <p class="directions">Hover over a tile for more info. Click the tile to watch a trailer.</p>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {media_tiles}
    </div>
  </body>
</html>
'''


# A single media entry html template
media_tile_content = '''
<div class="col-sm-6 col-md-4 col-lg-3 media-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{media_title}{media_year}</h2>
    <p>{media_description}</p>
    <p class="genre">{media_genre}</p>
    <p class="metadata">{media_additional_info}</p>
</div>
'''


def create_media_tiles_content(media):
    # The HTML content for this section of the page
    content = ''
    for media in media:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', media.youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', media.youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # variables to hold additional media info
        media_year = ''
        media_rating = ''
        media_director = ''
        media_seasons_episodes = ''
        media_episode_length = ''

        # if each media object has the appropriate attributes, populate the
        # variables with the relevant values
        if hasattr(media, 'year'):
            media_year = ' (' + media.year + ')'

        if hasattr(media, 'rating'):
            media_rating = 'Rating: ' + media.rating

        if hasattr(media, 'director'):
            media_director = '<br>Director: ' + media.director

        if hasattr(media, 'episodes'):
            season_term = ''
            if media.seasons == "1":
                season_term = ' season'
            else:
                season_term = ' seasons'
            media_seasons_episodes = media.episodes + ' episodes over ' + \
            media.seasons + season_term

        if hasattr(media, 'episode_length'):
            media_episode_length = '<br>' + media.episode_length

        # Append the tile for the media with its content filled in
        content += media_tile_content.format(
            media_title=media.title,
            media_year=media_year,
            media_description=media.description,
            media_genre=media.genre,
            media_rating=media_rating,
            media_director=media_director,
            media_additional_info=media_rating + media_director +
            media_seasons_episodes + media_episode_length,
            poster_image_url=media.image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_media_page(media):
    # Create or overwrite the output file
    output_file = open('watch_it.html', 'w')

    # Replace the media tiles placeholder generated content
    rendered_content = main_page_content.format(
        media_tiles=create_media_tiles_content(media))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
