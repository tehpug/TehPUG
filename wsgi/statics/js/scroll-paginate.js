(function($) {
    $.fn.scrollPagination = function(options) {
        var settings = {
            page: 1,
            count: 10,
            noMorePosts: 'No More Posts!',
            scrollForMore: 'Scroll for more or click here',
            clickForMore: 'Click for more',
            loading: 'Loading Posts',
            delay: 500,
            scroll  : true
        };

        // Extend the options so they work with the plugin
        if(options) {
            $.extend(settings, options);
        }

        // For each so that we keep chainability.
        return this.each(function() {

            // Some variables
            $this = $(this);
            $settings = settings;
            var page = $settings.page;
            var busy = false; // Checks if the scroll action is happening
            // so we don't run it multiple times

            // Custom messages based on settings
            if($settings.scroll == true) $initmessage = $settings.scrollForMore;
            else $initmessage = $settings.clickForMore;

            // Append custom messages and extra UI
            $this.append('<div class="rows"></div><div class="loading-bar">'+$initmessage+'</div>');

            function getData() {
                // Post data to ajax.php
                $.get('/news/ajax', {
                    page: page,
                    count: $settings.count
                }, function(data) {
                    // Change loading bar content (it may have been altered)
                    $this.find('.loading-bar').html($initmessage);
                    // If there is no data returned, there are no more posts to be shown. Show error
                    if(data == "") {
                        $this.find('.loading-bar').html($settings.noMorePosts);
                    }
                    else {
                        // Offset increases
                        page += 1;
                        // Append the data to the content div
                        $this.find('.rows').append(data);
                        // No longer busy!
                        busy = false;
                    }
                });
            }

            getData(); // Run function initially
            // If scrolling is enabled
            if($settings.scroll == true) {
                // .. and the user is scrolling
                $(window).scroll(function() {
                    // Check the user is at the bottom of the element
                    if($(window).scrollTop() + $(window).height() > $this.height() && !busy) {
                        // Now we are working, so busy is true
                        busy = true;
                        // Tell the user we're loading posts
                        $this.find('.loading-bar').html($settings.loading);
                        // Run the function to fetch the data inside a delay
                        // This is useful if you have content in a footer you
                        // want the user to see.
                        setTimeout(function() {
                            getData();
                        }, $settings.delay);
                    }
                });
            }
            // Also content can be loaded by clicking the loading bar/
            $this.find('.loading-bar').click(function() {
                if(busy == false) {
                    busy = true;
                    getData();
                }
            });
        });
    };
})(jQuery);
