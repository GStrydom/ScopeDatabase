// search index for WYSIWYG Web Builder
var database_length = 0;

function SearchPage(url, title, keywords, description)
{
   this.url = url;
   this.title = title;
   this.keywords = keywords;
   this.description = description;
   return this;
}

function SearchDatabase()
{
   database_length = 0;
   this[database_length++] = new SearchPage("index.html", "Untitled Page", "untitled page piping scope database ", "");
   this[database_length++] = new SearchPage("estimates.html", "estimates", "estimates piping scope database nbsp pre shut phase erect scaffold remove insulation execution demo to quantiy ops tech install isolation and pt spades verify spade positions obtain setup hot cold work permits hp flushing of lines power brush disconnect instruments cut line dismantle steam tracing unbolt joints rigging activities rig out pipe supports up new grind prep section qc fit check tack weld bolt plumbers plug installation for purge preheat inspection ndt pwht after report release pressure test prepare re instate loop checks despade tsa touch paint on field welds pickling passivate carry flange management sapref quality handling other lineclass diameter length cuts ", "");
   return this;
}
