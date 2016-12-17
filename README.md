ComicBookMaker
==============

Script to fetch webcomics, archive them and use them to create ebooks.

[![Build Status](https://travis-ci.org/SylvainDe/ComicBookMaker.svg?branch=master)](https://travis-ci.org/SylvainDe/ComicBookMaker)

[![Quantified Code](https://www.quantifiedcode.com/api/v1/project/f7965ba082d64dd5b87181bea6275a80/badge.svg)](https://www.quantifiedcode.com/app/project/f7965ba082d64dd5b87181bea6275a80)

[![Code Climate](https://codeclimate.com/github/SylvainDe/ComicBookMaker/badges/gpa.svg)](https://codeclimate.com/github/SylvainDe/ComicBookMaker) / [![Issue Count](https://codeclimate.com/github/SylvainDe/ComicBookMaker/badges/issue_count.svg)](https://codeclimate.com/github/SylvainDe/ComicBookMaker)

[![Codacy](https://api.codacy.com/project/badge/Grade/6348e7509d804670824a20eb6f6ec169)](https://www.codacy.com/app/sylvain-desodt-github/ComicBookMaker?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=SylvainDe/ComicBookMaker&amp;utm_campaign=Badge_Grade)

[![Scrutinizer](https://scrutinizer-ci.com/g/SylvainDe/ComicBookMaker/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/SylvainDe/ComicBookMaker/?branch=master)

[![Landscape.io](https://landscape.io/github/SylvainDe/ComicBookMaker/master/landscape.svg?style=flat)](https://landscape.io/github/SylvainDe/ComicBookMaker/master)

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
 * [Tales of Absurdity (from Tapastic)](http://tapastic.com/series/Tales-Of-Absurdity)
 * [Tales of Absurdity (from Tumblr)](http://talesofabsurdity.tumblr.com)
 * [Angry At Nothing](http://www.angryatnothing.net)
 * [Angry At Nothing (from Tapastic)](http://tapastic.com/series/Comics-yeah-definitely-comics-)
 * [Anything Comic](http://www.anythingcomic.com)
 * [Anything Comic (from Tapastic)](http://tapastic.com/series/anything)
 * [Argyle Sweater](http://www.gocomics.com/theargylesweater)
 * [Amazing Super Powers](http://www.amazingsuperpowers.com)
 * [Aurel](http://aurel.blog.lemonde.fr)
 * [Space Avalanche](http://www.spaceavalanche.com)
 * [Ma vie est tout a fait fascinante (Bagieu)](http://www.penelope-jolicoeur.com)
 * [Banana Twinky](http://bananatwinky.tumblr.com)
 * [Jim Benton](http://www.gocomics.com/jim-benton-cartoons)
 * [Berkeley Mews](http://www.berkeleymews.com)
 * [Berkeley Mews (from GoComics)](http://www.gocomics.com/berkeley-mews)
 * [Berkeley Mews (from Tumblr)](http://mews.tumblr.com)
 * [BFGFS (from Tapastic)](https://tapastic.com/series/BFGFS)
 * [BFGFS (from Tumblr)](http://bfgfs.tumblr.com)
 * [Big Foot Justice](http://bigfootjustice.com)
 * [Big Foot Justice (from Tapastic)](http://tapastic.com/series/bigfoot-justice)
 * [Biter Comics](http://www.bitercomics.com)
 * [Blazers At Dawn](http://blazersatdawn.tumblr.com)
 * [Every Day Blues](http://everydayblues.net)
 * [Books of Adam](http://booksofadam.tumblr.com)
 * [Boulet Corp](http://www.bouletcorp.com)
 * [Boulet Corp (from Tumblr)](http://bouletcorp.tumblr.com)
 * [Boulet Corp English](http://english.bouletcorp.com)
 * [Boumeries (En)](http://comics.boumerie.com)
 * [Boumeries (Fr)](http://bd.boumerie.com)
 * [Break Of Day](http://www.gocomics.com/break-of-day)
 * [Brevity](http://www.gocomics.com/brevity)
 * [BuniComics](http://www.bunicomic.com)
 * [Electric Bunny Comic](http://www.electricbunnycomics.com/View/Comic/153/Welcome+to+Hell)
 * [Electric Bunny Comic (from Tumblr)](http://electricbunnycomics.tumblr.com)
 * [ButterSafe](http://buttersafe.com)
 * [Calvin and Hobbes](http://marcel-oehler.marcellosendos.ch/comics/ch/)
 * [Calvin and Hobbes (from GoComics)](http://www.gocomics.com/calvinandhobbes)
 * [Cancer Owl (from Tumblr)](http://cancerowl.tumblr.com)
 * [Cassandra Calin (from Tapastic)](https://tapastic.com/series/C-Cassandra-comics)
 * [Cassandra Calin (from Tumblr)](http://c-cassandra.tumblr.com)
 * [Channelate](http://www.channelate.com)
 * [Chuckle-A-duck](http://chuckleaduck.com)
 * [Victims Of Circumsolar](http://www.victimsofcircumsolar.com)
 * [A Comik](http://acomik.com)
 * [Commit Strip (En)](http://www.commitstrip.com/en)
 * [Commit Strip (Fr)](http://www.commitstrip.com/fr)
 * [Over Compensating](http://www.overcompensating.com)
 * [Completely Serious Comics](http://completelyseriouscomics.com)
 * [Joan Cornella (from Tumblr)](http://cornellajoan.tumblr.com)
 * [C Est Pas En Regardant Ses Pompes (...)](http://cperspqccltt.tumblr.com)
 * [Cube Drone](http://cube-drone.com/comics)
 * [Cheer Up Emo Kid (from Tapastic)](http://tapastic.com/series/CUEK)
 * [Cheer Up Emo Kid (from Tumblr)](http://enzocomics.tumblr.com)
 * [Les Culottees](http://lesculottees.blog.lemonde.fr)
 * [Cyanide and Happiness](http://explosm.net)
 * [Dagsson Hugleikur (from Tumblr)](http://hugleikurdagsson.tumblr.com)
 * [Deadly Panel](http://www.deadlypanel.com)
 * [Deadly Panel (from Tapastic)](https://tapastic.com/series/deadlypanel)
 * [Depressed Alien](http://depressedalien.com)
 * [According To Devin](http://accordingtodevin.tumblr.com)
 * [Mr Ethan Diamond](http://mrethandiamond.tumblr.com)
 * [Dilbert](http://dilbert.com)
 * [Ali Dilem](http://information.tv5monde.com/dilem)
 * [Dinosaur Comics](http://www.qwantz.com)
 * [Disco Bleach](http://discobleach.com)
 * [The Dog House Diaries](http://thedoghousediaries.com)
 * [Doodle For Food](http://doodleforfood.com)
 * [Doodle For Food (from Tapastic)](https://tapastic.com/series/Doodle-for-Food)
 * [Dorris Mc](http://dorrismccomics.com)
 * [Dorris Mc (from GoComics)](http://www.gocomics.com/dorris-mccomics)
 * [Doug Was Taken](http://dougwastaken.tumblr.com)
 * [The Earth Explodes](http://www.earthexplodes.com)
 * [Extra Fabulous Comics](http://extrafabulouscomics.com)
 * [Safely Endangered](http://www.safelyendangered.com)
 * [Safely Endangered (from Tumblr)](http://tumblr.safelyendangered.com)
 * [My Extra Life](http://www.myextralife.com)
 * [Fat Awesome](http://fatawesome.com/comics)
 * [Fat Awesome (from Tumblr)](http://fatawesomecomedy.tumblr.com)
 * [The World Is Flat (from Tapastic)](https://tapastic.com/series/The-World-is-Flat)
 * [The World Is Flat (from Tumblr)](http://theworldisflatcomics.tumblr.com)
 * [floccinaucinihilipilification](http://floccinaucinihilipilificationa.tumblr.com)
 * [Cartooning For Peace](http://cartooningforpeace.blog.lemonde.fr)
 * [Fowl Language Comics (from GoComics)](http://www.gocomics.com/fowl-language)
 * [Fowl Language Comics (from Tapastic)](http://tapastic.com/series/Fowl-Language-Comics)
 * [Fowl Language Comics (from Tumblr)](http://fowllanguagecomics.tumblr.com)
 * [FoxTrot](http://www.gocomics.com/foxtrot)
 * [FoxTrot Classics](http://www.gocomics.com/foxtrotclassics)
 * [Garfield](https://garfield.com)
 * [Garfield (from GoComics)](http://www.gocomics.com/garfield)
 * [Geek And Poke](http://geek-and-poke.com)
 * [The Gentleman Armchair](http://thegentlemansarmchair.com)
 * [Gerbil With A Jetpack](http://gerbilwithajetpack.com)
 * [Glory Owl](http://gloryowlcomix.blogspot.fr)
 * [Xavier Gorce](http://xaviergorce.blog.lemonde.fr)
 * [The Grohl Troll](http://thegrohltroll.com)
 * [Chris Hallback (from Tumblr)](http://chrishallbeck.tumblr.com)
 * [Chris Hallback - The Book of Biff (from Tapastic)](https://tapastic.com/series/Biff)
 * [Chris Hallback - Maximumble (from Tapastic)](https://tapastic.com/series/Maximumble)
 * [Chris Hallback - Minimumble (from Tapastic)](https://tapastic.com/series/Minimumble)
 * [A Ham A Day](http://www.ahammaday.com)
 * [Happle Tea](http://www.happletea.com)
 * [Hark A Vagrant (from Tumblr)](http://beatonna.tumblr.com)
 * [Heck if I Know comics (from Tapastic)](http://tapastic.com/series/Regular)
 * [Heck if I Know comics (from Tumblr)](http://heckifiknowcomics.com)
 * [Hit and Miss Comics](http://hitandmisscomics.tumblr.com)
 * [HM Blanc](http://hmblanc.tumblr.com)
 * [Hoomph](http://hoom.ph)
 * [Horovitz Classic](http://www.horovitzcomics.com)
 * [Horovitz New](http://www.horovitzcomics.com)
 * [Hot Comics For Cool People (from Tapastic)](https://tapastic.com/series/Hot-Comics-For-Cool-People)
 * [Hot Comics For Cool People (from Tumblr)](http://hotcomicsforcoolpeople.tumblr.com)
 * [Invisible Bread](http://invisiblebread.com)
 * [In Your Face Cake (from Tumblr)](http://in-your-face-cake.tumblr.com)
 * [Irwin Cardozo](http://irwincardozocomics.tumblr.com)
 * [Jake Likes Onions](http://jakelikesonions.com)
 * [My Jet Pack](http://myjetpack.tumblr.com)
 * [Jhall Comics (from Tumblr)](http://jhallcomics.tumblr.com)
 * [Just Say Eh](http://www.justsayeh.com)
 * [Just Say Eh (from Tapastic)](http://tapastic.com/series/Just-Say-Eh)
 * [For Lack Of A Better Comic](http://forlackofabettercomic.tumblr.com)
 * [Last Place Comics](http://lastplacecomics.com)
 * [Leleoz (from Tapastic)](https://tapastic.com/series/Leleoz)
 * [Leleoz (from Tumblr)](http://leleozcomics.tumblr.com)
 * [Little Life Lines](http://www.littlelifelines.com)
 * [Little Life Lines (from Tumblr)](https://little-life-lines.tumblr.com)
 * [L.I.N.S. Editions](https://linsedition.com)
 * [L.I.N.S. Editions (from Tumblr)](http://linscomics.tumblr.com)
 * [Loading Artist](http://www.loadingartist.com/latest)
 * [Lol Nein (from Tumblr)](http://lolneincom.tumblr.com)
 * [Mike Luckovich](http://www.gocomics.com/mikeluckovich)
 * [Lunar Baboon](http://www.gocomics.com/lunarbaboon)
 * [Une Annee au Lycee](http://uneanneeaulycee.blog.lemonde.fr)
 * [Mercworks](http://mercworks.net)
 * [Mercworks (from Tumblr)](http://mercworks.tumblr.com)
 * [Lonnie Millsap](http://www.lonniemillsap.com)
 * [Mister & Me](http://www.mister-and-me.com)
 * [Mister & Me (from GoComics)](http://www.gocomics.com/mister-and-me)
 * [Mister & Me (from Tapastic)](https://tapastic.com/series/Mister-and-Me)
 * [Art By Moga](http://artbymoga.tumblr.com)
 * [Infinite Monkey Business](http://infinitemonkeybusiness.net)
 * [Moon Beard](http://moonbeard.com)
 * [Moon Beard (from Tumblr)](http://blog.squiresjam.es/moonbeard)
 * [Tu Mourras Moins Bete](http://tumourrasmoinsbete.blogspot.fr)
 * [Mouse Bear Comedy](http://www.mousebearcomedy.com)
 * [Mouse Bear Comedy (from Tumblr)](http://mousebearcomedy.tumblr.com)
 * [Mr. Lovenstein](http://www.mrlovenstein.com)
 * [Mr. Lovenstein (from Tapastic)](https://tapastic.com/series/MrLovenstein)
 * [NamelessPCs (from Tapastic)](https://tapastic.com/series/NamelessPC)
 * [NeDroid](http://nedroid.com)
 * [Nelluc Nhoj](http://nellucnhoj.com)
 * [Nick Anderson](http://www.gocomics.com/nickanderson)
 * [Non Sequitur](http://www.gocomics.com/nonsequitur)
 * [Comic Nuggets](http://comicnuggets.com)
 * [The Oatmeal (from Tumblr)](http://oatmeal.tumblr.com)
 * [Octopuns](http://www.octopuns.net)
 * [Octopuns (from Tumblr)](http://octopuns.tumblr.com)
 * [Off The Mark](http://www.gocomics.com/offthemark)
 * [Oglaf [NSFW]](http://oglaf.com)
 * [Optipess](http://www.optipess.com)
 * [Endless Origami](http://endlessorigami.com)
 * [Origami Hot Dish](http://origamihotdish.com)
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
 * [The Pigeon Gazette (from Tapastic)](https://tapastic.com/series/The-Pigeon-Gazette)
 * [The Pigeon Gazette (from Tumblr)](http://thepigeongazette.tumblr.com)
 * [Plan C](http://www.plancomic.com)
 * [Plantu](http://plantu.blog.lemonde.fr)
 * [Pleasant Thoughts](http://pleasant-thoughts.com)
 * [Pond Scum](http://pondscumcomic.tumblr.com)
 * [Poorly Drawn Lines](http://poorlydrawnlines.com)
 * [Poorly Drawn Lines (from Tumblr)](http://pdlcomics.tumblr.com)
 * [Yesterday's Popcorn (from Tapastic)](https://tapastic.com/series/Yesterdays-Popcorn)
 * [Yesterday's Popcorn (from Tumblr)](http://yesterdayspopcorn.tumblr.com)
 * [Pundemonium](http://monstika.tumblr.com)
 * [Quarktees](http://www.quarktees.com/blogs/news)
 * [Ted Rall](http://rall.com/comic)
 * [Ted Rall (from GoComics)](http://www.gocomics.com/tedrall)
 * [Michael Ramirez](http://www.gocomics.com/michaelramirez)
 * [RandoWis (from Tapastic)](https://tapastic.com/series/RandoWis)
 * [Classic Randy](http://classicrandy.tumblr.com)
 * [Gone Into Rapture](http://www.goneintorapture.com)
 * [Gone Into Rapture (from Tapastic)](http://tapastic.com/series/Goneintorapture)
 * [Respawn Comic](http://respawncomic.com )
 * [Respawn Comic (from Tumblr)](http://respawncomic.tumblr.com)
 * [Robbie And Bobby (from Tumblr)](http://robbieandbobby.tumblr.com)
 * [Robospunk](http://robospunk.com)
 * [Mandatory Roller Coaster](http://mandatoryrollercoaster.com)
 * [Sarah Andersen (from GoComics)](http://www.gocomics.com/sarahs-scribbles)
 * [Sarah Andersen (from Tapastic)](http://tapastic.com/series/Doodle-Time)
 * [Scandinavia And The World](http://satwcomic.com)
 * [Sephko](http://sephko.tumblr.com)
 * [Sheldon Comics](http://www.sheldoncomics.com)
 * [Sheldon Comics (from GoComics)](http://www.gocomics.com/sheldon)
 * [Small Blue Yonder (from Tapastic)](https://tapastic.com/series/Small-Blue-Yonder)
 * [Saturday Morning Breakfast Cereal](http://www.smbc-comics.com)
 * [Saturday Morning Breakfast Cereal (from GoComics)](http://www.gocomics.com/saturday-morning-breakfast-cereal)
 * [Saturday Morning Breakfast Cereal (from Tumblr)](http://smbc-comics.tumblr.com)
 * [Something Of That Ilk](http://www.somethingofthatilk.com)
 * [Down the Upward Spiral (from Tumblr)](http://downtheupwardspiral.tumblr.com)
 * [Things in squares](http://www.thingsinsquares.com)
 * [Make it stoopid](http://makeitstoopid.com/comic.php)
 * [Everything's Stupid](http://everythingsstupid.net)
 * [Everything's Stupid (from Tapastic)](http://tapastic.com/series/EverythingsStupid)
 * [Sunny Street](http://www.gocomics.com/sunny-street)
 * [Our Super Adventure (from Tapastic)](https://tapastic.com/series/Our-Super-Adventure)
 * [Our Super Adventure (from Tumblr)](http://sarahssketchbook.tumblr.com)
 * [The Ism](http://www.theism-comics.com)
 * [The Odd 1s Out (from Tapastic)](https://tapastic.com/series/Theodd1sout)
 * [The Odd 1s Out (from Tumblr)](http://theodd1sout.tumblr.com)
 * [They Can Talk](http://theycantalk.com)
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
 * [Tumblr Dry (from Tapastic)](https://tapastic.com/series/TumbleDryComics)
 * [Twisted Doodles](http://www.twisteddoodles.com)
 * [Ubertool](http://ubertoolcomic.com)
 * [Ubertool (from Tapastic)](https://tapastic.com/series/ubertool)
 * [Ubertool (from Tumblr)](http://ubertool.tumblr.com)
 * [The Underfold (from Tumblr)](http://theunderfold.tumblr.com)
 * [Unearthed Comics](http://unearthedcomics.com)
 * [Unearthed Comics (from Tapastic)](http://tapastic.com/series/UnearthedComics)
 * [Unearthed Comics (from Tumblr)](http://unearthedcomics.tumblr.com)
 * [Up And Out (from Tumblr)](http://upandoutcomic.tumblr.com)
 * [Up And Out (from Tapastic)](http://tapastic.com/series/UP-and-OUT)
 * [As Per Usual (from Tapastic)](https://tapastic.com/series/AsPerUsual)
 * [As Per Usual (from Tumblr)](http://as-per-usual.tumblr.com)
 * [Vector Belly](http://vectorbelly.tumblr.com)
 * [Vegetables For Dessert](http://tapastic.com/series/vegetablesfordessert)
 * [Vidberg - l'actu en patates](http://vidberg.blog.lemonde.fr)
 * [Waffles And Pancakes](https://tapastic.com/series/Waffles-and-Pancakes)
 * [War And Peas (from Tumblr)](http://warandpeas.tumblr.com)
 * [Warehouse Comic](http://warehousecomic.com)
 * [Webcomic Name](http://webcomicname.com)
 * [Will 5:00 Never Come ?](http://will5nevercome.com)
 * [Wondermark](http://wondermark.com)
 * [Wooden Plank Studios](http://woodenplankstudios.com)
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
