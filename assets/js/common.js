// aHR0cHM6Ly9naXRodWIuY29tL2x1b3N0MjYvYWNhZGVtaWMtaG9tZXBhZ2U=
$(function () {
    lazyLoadOptions = {
        scrollDirection: 'vertical',
        effect: 'fadeIn',
        effectTime: 300,
        placeholder: "",
        onError: function(element) {
            console.log('[lazyload] Error loading ' + element.data('src'));
        },
        afterLoad: function(element) {
            if (element.is('img')) {
                // remove background-image style
                element.css('background-image', 'none');
                element.css('min-height', '0');
            } else if (element.is('div')) {
                // set the style to background-size: cover;
                element.css('background-size', 'cover');
                element.css('background-position', 'center');
            }
        }
    }

    $('img.lazy, div.lazy:not(.always-load)').Lazy({visibleOnly: true, ...lazyLoadOptions});
    $('div.lazy.always-load').Lazy({visibleOnly: false, ...lazyLoadOptions});

    $('[data-toggle="tooltip"]').tooltip()

    // Masonry is only loaded on the Showcase page
    if ($.fn.masonry) {
        var $grid = $('.grid').masonry({
            "percentPosition": true,
            "itemSelector": ".grid-item",
            "columnWidth": ".grid-sizer"
        });
        // layout Masonry after each image loads
        $grid.imagesLoaded().progress(function () {
            $grid.masonry('layout');
        });

        $(".lazy").on("load", function () {
            $grid.masonry('layout');
        });
    }

    // Theme toggle (initial theme is set in head.html before first paint)
    $('.theme-toggle').on('click', function () {
        var next = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', next);
        localStorage.setItem('theme', next);
    });

    // News: reveal older items
    $('.news-toggle').on('click', function () {
        var $list = $($(this).data('target'));
        var expanded = $list.toggleClass('expanded').hasClass('expanded');
        $(this).attr('aria-expanded', expanded);
        $(this).find('i').toggleClass('fa-chevron-down fa-chevron-up');
        $(this).find('span').text(expanded ? 'Show fewer' : $(this).data('label') || 'Show all updates');
    }).each(function () {
        $(this).data('label', $(this).find('span').text());
    });

    // Publications: abstract toggle
    $('.abstract-toggle').on('click', function () {
        var $box = $(this).closest('.pub-body').find('.pub-abstract');
        $box.toggleClass('open');
        $(this).attr('aria-expanded', $box.hasClass('open'));
    });

    // Publications: BibTeX toggle and copy
    $('.bibtex-toggle').on('click', function () {
        var $box = $(this).closest('.pub-body').find('.pub-bibtex');
        $box.toggleClass('open');
        $(this).attr('aria-expanded', $box.hasClass('open'));
    });
    $('.pub-bibtex .copy-btn').on('click', function () {
        var $btn = $(this);
        var text = $btn.siblings('pre').text().trim();
        navigator.clipboard.writeText(text).then(function () {
            $btn.html('<i class="fas fa-check"></i> Copied');
            setTimeout(function () { $btn.html('<i class="far fa-copy"></i> Copy'); }, 1600);
        });
    });

    // Publications: search and type filter
    var $items = $('.pub-item[data-search]');
    if ($items.length && $('#pub-search').length) {
        var activeType = 'all';
        // Remember each item's original place so "Newest" can restore the by-year grouping
        $items.each(function () { $(this).data('home', this.parentNode).data('index', $(this).index()); });
        var applyFilter = function () {
            var q = $('#pub-search').val().toLowerCase().trim();
            var visible = 0;
            $items.each(function () {
                var $el = $(this);
                var ok = (activeType === 'all' || $el.data('type') === activeType) &&
                         (!q || $el.data('search').indexOf(q) !== -1);
                $el.toggle(ok);
                if (ok) visible++;
            });
            var flat = $('#pub-flat').is(':visible');
            $('.pub-year-group').each(function () {
                $(this).toggle(!flat && $(this).find('.pub-item').filter(function () { return this.style.display !== 'none'; }).length > 0);
            });
            $('#pub-empty').toggle(visible === 0);
        };
        $('#pub-search').on('input', applyFilter);
        $('.sort-btn').on('click', function () {
            $('.sort-btn').removeClass('active');
            $(this).addClass('active');
            if ($(this).data('sort') === 'cited') {
                var sorted = $items.get().sort(function (a, b) { return $(b).data('citations') - $(a).data('citations'); });
                $('#pub-flat').append(sorted).show();
            } else {
                $('#pub-flat').hide();
                $items.get().sort(function (a, b) { return $(a).data('index') - $(b).data('index'); })
                    .forEach(function (el) { $(el).data('home').appendChild(el); });
            }
            applyFilter();
        });
        $('.filter-btn:not(.sort-btn)').on('click', function () {
            $('.filter-btn:not(.sort-btn)').removeClass('active');
            $(this).addClass('active');
            activeType = $(this).data('filter');
            applyFilter();
        });
    }

    // Service page: conference / journal tabs (also selectable via #journals in the URL)
    var showTab = function (name) {
        $('.service-tabs [data-tab]').each(function () {
            var on = $(this).data('tab') === name;
            $(this).toggleClass('active', on).attr('aria-selected', on);
            $('#panel-' + $(this).data('tab')).prop('hidden', !on);
        });
    };
    $('.service-tabs [data-tab]').on('click', function () {
        showTab($(this).data('tab'));
        history.replaceState(null, '', '#' + $(this).data('tab'));
    });
    if ($('.service-tabs').length && $('#panel-' + location.hash.slice(1)).length) {
        showTab(location.hash.slice(1));
    }

    // Scroll reveal
    var reveals = document.querySelectorAll('.reveal');
    if ('IntersectionObserver' in window) {
        var observer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('in');
                    observer.unobserve(entry.target);
                }
            });
        }, { rootMargin: '0px 0px -60px 0px' });
        reveals.forEach(function (el) { observer.observe(el); });
    } else {
        reveals.forEach(function (el) { el.classList.add('in'); });
    }
})
