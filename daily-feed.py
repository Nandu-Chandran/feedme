import yaml
import feedparser
from tinyhtml import h, html, frag

with open('config.yaml','r') as file:
    data = yaml.safe_load(file)
    
feed_links=[links for links in data['links']]

def create_html(html_content):
    with open('index.html', "w") as file:
        file.write(html_content)

def create_layout(title, body): 
    return html()( 
        h("head")( 
            h("title")(title), 
        ), 
        h("body")(body) 
    ) 

def get_feed_data(feed,number):
    parser= feedparser.parse(feed)
    feed_data= f"\n<tbody>\n<h4>"+feed+'</h4>'
    for items,data in enumerate(parser.entries):
        if items == number:
            break
        else:
            row=f'['+data.published[0:11]+']'+' '+'\n<a href="'+data.link+'" target="_blank">'+data.title+'</a>'+'<br>'
        feed_data+=row
    feed_data+="</tbody>\n"
    return feed_data
   
new_data=''
for feed in feed_links:
    data=get_feed_data(feed,7)
    print((data))
    
    new_data+=data
create_html(str(new_data)) 
