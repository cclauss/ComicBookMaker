ComicBookMaker
==============

Script to fetch webcomics, archive them and use them to create ebooks.

[![Build Status](https://travis-ci.org/SylvainDe/ComicBookMaker.svg?branch=master)](https://travis-ci.org/SylvainDe/ComicBookMaker)


Longer explanation
------------------

Web crawlers are defined to retrieve comic information and store them into files. This can then be used to generated ebooks.

These webcrawlers are supposed to be easy to write with a minimal amount of boilerplate code whilst trying to keep some flexibility.

Under the hood, there is one class per webcrawler, each of them inherits, directly or not, from an abstract class `GenericComic` which handles all the common logic. Each webcrawler just need to provide specific information (`name` and `url`) and a way to get the comics after a given one (if any) which is done by implementing the `get_next_comic` generator.

Other abstract classes, inheriting from `GenericComic` provide a convenient way to define `get_next_comic`. The most common is `GenericNavigableComic`, used for comics where next/previous strips are available using the relevant link.

The whole project relies heavily on BeautifulSoup.

Command-line interface
----------------------
`comicbookmaker.py` takes multiple arguments.
 * `--comic` (or `-c`) can be used to tell which comic(s) is/are to be considered (defaults to all of them).
 * `--action` (or `-a`) specifies which actions are to be performed on these comics : update (default behavior), book, etc.


See also
--------
[dosage](http://dosage.rocks/) is a project with similar purpose. It seems to be a very nice project but it doesn't handle ebooks generation.


Contributing
------------

Feel free to open issues/open pull requests/ask questions/give comments.

Here is the little to know before contributing :
 - license is MIT
 - all pep8 rules apply except for the length of the lines


Comics supported
----------------
 * [1111 Comics](http://www.1111comics.me)
 * [1111 Comics (from Tapastic)](https://tapastic.com/series/1111-Comics)
 * [1111 Comics (from Tumblr)](http://comics1111.tumblr.com)
 * [Abstruse Goose](http://abstrusegoose.com)
 * [Tales of Absurdity](http://talesofabsurdity.com)
 * [Angry At Nothing](http://www.angryatnothing.net)
 * [Angry At Nothing (from Tapastic)](http://tapastic.com/series/Comics-yeah-definitely-comics-)
 * [Anything Comic](http://www.anythingcomic.com)
 * [Anything Comic (from Tapastic)](http://tapastic.com/series/anything)
 * [Argyle Sweater](http://www.gocomics.com/theargylesweater)
 * [Amazing Super Powers](http://www.amazingsuperpowers.com)
 * [Aurel](http://aurel.blog.lemonde.fr)
 * [Space Avalanche](http://www.spaceavalanche.com)
 * [Ma vie est tout a fait fascinante (Bagieu)](http://www.penelope-jolicoeur.com)
 * [Jim Benton](http://www.gocomics.com/jim-benton-cartoons)
 * [Berkeley Mews](http://www.berkeleymews.com)
 * [Berkeley Mews (from GoComics)](http://www.gocomics.com/berkeley-mews)
 * [Berkeley Mews (from Tumblr)](http://mews.tumblr.com)
 * [Big Foot Justice](http://bigfootjustice.com)
 * [Big Foot Justice (from Tapastic)](http://tapastic.com/series/bigfoot-justice)
 * [Biter Comics](http://www.bitercomics.com)
 * [Every Day Blues](http://everydayblues.net)
 * [Boulet Corp](http://www.bouletcorp.com)
 * [Boulet Corp (from Tumblr)](http://bouletcorp.tumblr.com)
 * [Boulet Corp English](http://english.bouletcorp.com)
 * [Boumeries (En)](http://comics.boumerie.com)
 * [Boumeries (Fr)](http://bd.boumerie.com)
 * [Break Of Day](http://www.gocomics.com/break-of-day)
 * [Brevity](http://www.gocomics.com/brevity)
 * [BuniComics](http://www.bunicomic.com)
 * [Electric Bunny Comic](http://www.electricbunnycomics.com/View/Comic/153/Welcome+to+Hell)
 * [ButterSafe](http://buttersafe.com)
 * [Calvin and Hobbes](http://marcel-oehler.marcellosendos.ch/comics/ch/)
 * [Calvin and Hobbes (from GoComics)](http://www.gocomics.com/calvinandhobbes)
 * [Channelate](http://www.channelate.com)
 * [Chuckle-A-duck](http://chuckleaduck.com)
 * [Victims Of Circumsolar](http://www.victimsofcircumsolar.com)
 * [Commit Strip (En)](http://www.commitstrip.com/en)
 * [Commit Strip (Fr)](http://www.commitstrip.com/fr)
 * [Over Compensating](http://www.overcompensating.com)
 * [Completely Serious Comics](http://completelyseriouscomics.com)
 * [Cube Drone](http://cube-drone.com/comics)
 * [Cheer Up Emo Kid (from Tapastic)](http://tapastic.com/series/CUEK)
 * [Cheer Up Emo Kid (from Tumblr)](http://enzocomics.tumblr.com)
 * [Les Culottees](http://lesculottees.blog.lemonde.fr)
 * [Cyanide and Happiness](http://explosm.net)
 * [Deadly Panel](http://www.deadlypanel.com)
 * [Depressed Alien](http://depressedalien.com)
 * [According To Devin](http://accordingtodevin.tumblr.com)
 * [Mr Ethan Diamond](http://mrethandiamond.tumblr.com)
 * [Dilbert](http://dilbert.com)
 * [Ali Dilem](http://information.tv5monde.com/dilem)
 * [Dinosaur Comics](http://www.qwantz.com)
 * [Disco Bleach](http://discobleach.com)
 * [The Dog House Diaries](http://thedoghousediaries.com)
 * [Extra Fabulous Comics](http://extrafabulouscomics.com)
 * [Safely Endangered](http://www.safelyendangered.com)
 * [Safely Endangered (from Tumblr)](http://tumblr.safelyendangered.com)
 * [My Extra Life](http://www.myextralife.com)
 * [Fat Awesome](http://fatawesome.com/comics)
 * [floccinaucinihilipilification](http://floccinaucinihilipilificationa.tumblr.com)
 * [Cartooning For Peace](http://cartooningforpeace.blog.lemonde.fr)
 * [Fowl Language Comics](http://tapastic.com/series/Fowl-Language-Comics)
 * [Garfield](http://garfield.com)
 * [Geek And Poke](http://geek-and-poke.com)
 * [The Gentleman Armchair](http://thegentlemansarmchair.com)
 * [Gerbil With A Jetpack](http://gerbilwithajetpack.com)
 * [Xavier Gorce](http://xaviergorce.blog.lemonde.fr)
 * [A Ham A Day](http://www.ahammaday.com)
 * [Happle Tea](http://www.happletea.com)
 * [Happy Monday (from Tapastic)](https://tapastic.com/series/HappyMondayComics)
 * [Heck if I Know comics (from Tapastic)](http://tapastic.com/series/Regular)
 * [Heck if I Know comics (from Tumblr)](http://heckifiknowcomics.com)
 * [Horovitz Classic](http://www.horovitzcomics.com)
 * [Horovitz New](http://www.horovitzcomics.com)
 * [Invisible Bread](http://invisiblebread.com)
 * [Irwin Cardozo](http://irwincardozocomics.tumblr.com)
 * [My Jet Pack](http://myjetpack.tumblr.com)
 * [Just Say Eh](http://www.justsayeh.com)
 * [Just Say Eh (from Tapastic)](http://tapastic.com/series/Just-Say-Eh)
 * [For Lack Of A Better Comic](http://forlackofabettercomic.tumblr.com)
 * [LastPlaceComics](http://lastplacecomics.com)
 * [Loading Artist](http://www.loadingartist.com/latest)
 * [Mike Luckovich](http://www.gocomics.com/mikeluckovich)
 * [Lunar Baboon](http://www.gocomics.com/lunarbaboon)
 * [Mercworks](http://mercworks.net)
 * [Mercworks (from Tumblr)](http://mercworks.tumblr.com)
 * [Lonnie Millsap](http://www.lonniemillsap.com)
 * [Infinite Monkey Business](http://infinitemonkeybusiness.net)
 * [Mouse Bear Comedy](http://www.mousebearcomedy.com)
 * [Mouse Bear Comedy (from Tumblr)](http://mousebearcomedy.tumblr.com)
 * [Mr. Lovenstein](http://www.mrlovenstein.com)
 * [NeDroid](http://nedroid.com)
 * [Nelluc Nhoj](http://nellucnhoj.com)
 * [The Oatmeal (from Tumblr)](http://oatmeal.tumblr.com)
 * [Octopuns](http://www.octopuns.net)
 * [Octopuns (from Tumblr)](http://octopuns.tumblr.com)
 * [Off The Mark](http://www.gocomics.com/offthemark)
 * [Oglaf [NSFW]](http://oglaf.com)
 * [Optipess](http://www.optipess.com)
 * [Endless Origami](http://endlessorigami.com)
 * [Oscillating Profundities](http://tapastic.com/series/oscillatingprofundities)
 * [Owl Turd (from Tapastic)](http://tapastic.com/series/Owl-Turd-Comix)
 * [Owl Turd (from Tumblr)](http://owlturd.com)
 * [Pain Train Comics](http://paintraincomic.com)
 * [Perry Bible Fellowship](http://pbfcomics.com)
 * [Peanuts](http://www.gocomics.com/peanuts)
 * [Pearls Before Swine](http://www.gocomics.com/pearlsbeforeswine)
 * [Pear-Shaped Comics](http://pearshapedcomics.com)
 * [Penmen](http://penmen.com)
 * [PhD Comics](http://phdcomics.com/comics/archive.php)
 * [Pictures in Boxes](http://www.picturesinboxes.com)
 * [Pictures in Boxes (from Tumblr)](http://picturesinboxescomic.tumblr.com)
 * [Pie Comic](http://piecomic.tumblr.com)
 * [Plan C](http://www.plancomic.com)
 * [Plantu](http://plantu.blog.lemonde.fr)
 * [Pond Scum](http://pondscumcomic.tumblr.com)
 * [Poorly Drawn Lines](http://poorlydrawnlines.com)
 * [Poorly Drawn Lines (from Tumblr)](http://pdlcomics.tumblr.com)
 * [Pundemonium](http://monstika.tumblr.com)
 * [Quarktees](http://www.quarktees.com/blogs/news)
 * [Ted Rall](http://rall.com/comic)
 * [Ted Rall (from GoComics)](http://www.gocomics.com/tedrall)
 * [Michael Ramirez](http://www.gocomics.com/michaelramirez)
 * [Gone Into Rapture](http://www.goneintorapture.com)
 * [Gone Into Rapture (from Tapastic)](http://tapastic.com/series/Goneintorapture)
 * [Sarah Andersen (from GoComics)](http://www.gocomics.com/sarahs-scribbles)
 * [Sarah Andersen (from Tapastic)](http://tapastic.com/series/Doodle-Time)
 * [Scandinavia And The World](http://satwcomic.com)
 * [Sheldon Comics](http://www.sheldoncomics.com)
 * [Saturday Morning Breakfast Cereal](http://www.smbc-comics.com)
 * [Something Of That Ilk](http://www.somethingofthatilk.com)
 * [Down the Upward Spiral (from Tumblr)](http://downtheupwardspiral.tumblr.com)
 * [Things in squares](http://www.thingsinsquares.com)
 * [Make it stoopid](http://makeitstoopid.com/comic.php)
 * [Everything's Stupid](http://everythingsstupid.net)
 * [Everything's Stupid (from Tapastic)](http://tapastic.com/series/EverythingsStupid)
 * [Sunny Street](http://www.gocomics.com/sunny-street)
 * [Thor's Thundershack](http://www.thorsthundershack.com)
 * [Thor's Thundershack (from Tapastic)](http://tapastic.com/series/Thors-Thundershac)
 * [Three Word Phrase](http://threewordphrase.com)
 * [Three Word Phrase (from Tumblr)](http://www.threewordphrase.tumblr.com)
 * [It's the tie](http://itsthetie.com)
 * [It's the tie (from Tumblr)](http://itsthetie.tumblr.com)
 * [Time Trabble (from Tumblr)](http://timetrabble.tumblr.com)
 * [Tom Toles](http://www.gocomics.com/tomtoles)
 * [Toon Hole](http://www.toonhole.com)
 * [Toon Hole (from Tapastic)](http://tapastic.com/series/TOONHOLE)
 * [Tubey Toons](http://tubeytoons.com)
 * [Tubey Toons (from Tapastic)](http://tapastic.com/series/Tubey-Toons)
 * [Tubey Toons (from Tumblr)](http://tubeytoons.tumblr.com)
 * [Unearthed Comics](http://unearthedcomics.com)
 * [Unearthed Comics (from Tapastic)](http://tapastic.com/series/UnearthedComics)
 * [Unearthed Comics (from Tumblr)](http://unearthedcomics.tumblr.com)
 * [Up And Out (from Tumblr)](http://upandoutcomic.tumblr.com)
 * [Up And Out (from Tapastic)](http://tapastic.com/series/UP-and-OUT)
 * [As Per Usual (from Tapastic)](https://tapastic.com/series/AsPerUsual)
 * [As Per Usual (from Tumblr)](http://as-per-usual.tumblr.com)
 * [Vector Belly](http://vectorbelly.tumblr.com)
 * [Vegetables For Dessert](http://tapastic.com/series/vegetablesfordessert)
 * [Vidberg -l'actu en patates](http://vidberg.blog.lemonde.fr)
 * [Warehouse Comic](http://warehousecomic.com)
 * [Wondermark](http://wondermark.com)
 * [Matt Wuerker](http://www.gocomics.com/mattwuerker)
 * [WuMo](http://www.gocomics.com/wumo)
 * [xkcd](http://xkcd.com)
 * [The Awkward Yeti](http://theawkwardyeti.com)
 * [The Awkward Yeti (from GoComics)](http://www.gocomics.com/the-awkward-yeti)
 * [The Awkward Yeti (from Tapastic)](https://tapastic.com/series/TheAwkwardYeti)
 * [The Awkward Yeti (from Tumblr)](http://larstheyeti.tumblr.com)
 * [Zen Pencils](http://zenpencils.com)
 * [Zen Pencils (from Tumblr)](http://zenpencils.tumblr.com)
 * [Zep World](http://zepworld.blog.lemonde.fr)
 * [Znoflats Comics](http://tapastic.com/series/Znoflats-Comics)
