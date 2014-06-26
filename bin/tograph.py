import bigbang.parse as parse
import bigbang.graph as graph
import networkx as nx
from pprint import pprint as pp

fn = "archives/numpy-discussion/2001-November.txt"

messages = parse.open_mail_archive(fn)

#import pdb; pdb.set_trace()

RG = graph.messages_to_reply_graph(messages)

IG = graph.messages_to_interaction_graph(messages)

pdig = nx.to_pydot(IG)

pdig.set_overlap('False')

pdig.write_png('interactions.png',prog='neato')

#print nx.connected_components(G.to_undirected())

#nx.write_dot(IG,"interactions.dot")

#nx.draw_shell(IG)
#plt.show()
nx.write_gml(IG,"interactions.gml")

#pp(G.nodes(data=True))