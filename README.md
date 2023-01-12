##### And the survey from Travis says:

[![Build Status](https://travis-ci.org/ShavingSeagull/Herculean.svg?branch=master)](https://travis-ci.org/ShavingSeagull/Herculean)


# HERCULEAN

## Overview

**You can find the live site on [Render](https://herculean-store.onrender.com/)**

### Why was it created?

This is the end of stream three - and my final overall - project for [Code Institute's](https://www.codeinstitute.net/)
Full Stack Web Developer course. This site is the culmination of all my hard work over
the last year and a half and includes front-end and back-end, the whole shebang.
The site is written in HTML, CSS, JavaScript/jQuery, Python and Django.

### Its purpose?

To function as a fully-fledged e-commerce website, using Stripe's API to process the payments.

## Features

The site is primarily designed as a fitness store, but also houses customer accounts and fitness
articles in the form of a blogpost layout.

### Major areas of the site
- User account area
  - Ability to see other users' public profiles
- Product pages
  - Reviews and rating system
- Fitness news from staff
  - Commenting using Disqus
- Cart and checkout
  - Promo code functionality
  
## Technology

### Major tech used:
- [Django 2.0](https://www.djangoproject.com/)
  - The main framework and driving force behind Herculean
- [Bootstrap 3](https://getbootstrap.com/)
  - I use a lot of custom CSS too, but Bootstrap makes life easier
- [jQuery](https://jquery.com/)
  - Minor scripting required on the site, mostly done using jQuery
- [Stripe](https://stripe.com/)
  - Stripe handles all user payments
- [Disqus](https://disqus.com/)
  - Disqus enables commenting on the fitness articles
- [Gravatar](https://gravatar.com/)
  - Provides the default avatar for those too bashful to upload a picture
- [Amazon Web Services](https://aws.amazon.com/)
  - AWS hosts the static and media files using [S3](https://aws.amazon.com/s3/)
  
### Testing

Testing is done using the Django testing framework, continuously integrated by Travis.
There is also an extensive list of manual tests, which are included in the TDD folder in the repo.

## Acknowledgements

As always, I'd like to give the biggest thanks imaginable to [Matt Rudge](https://github.com/lechien73)
of the [Code Institute](https://www.codeinstitute.net/) for his persistent wisdom and sometimes
bacon saving knowledge. He has been my personal mentor throughout this course and I couldn't have asked for
a better ally. So thank you, Matt.

I'd like to thank the folks at [Start Bootstrap](https://startbootstrap.com/), who provide quality
themes and templates for developers to use. The home page and the individual product pages were loosely
based on templates provided by Start Bootstrap; however, they have been largely changed from their initial
layout. Having never built an e-commerce site before, the templates gave a good idea of where to go more than
anything. I like to be original.
