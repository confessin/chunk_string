#!/usr/bin/env python
# encoding: utf-8

"""
A Chunker which generates keywords from a blob of text
"""
import re
import traceback
import urllib2
from bs4 import BeautifulSoup
from nltk import pos_tag, RegexpParser, clean_html
from random import randint


__author__ = 'confessin@gmail.com (Mohammad Rafi)'


# TODO (confessin): Add more types of regexes.
GRAMMARS = [
    # adj/noun, noun, adjective.
    r"""
    NP_CHUNK_ADJ: {<J.*|NUM>+<N.*>+<J.*|NUM>?}
    """,
    # verb to verb
    r"""
    TO_CHUNK: {<V.*>+<TO><V.*>+}
    {<N.*>+<TO><V.*>+}
    """,
    r"""
    NP_CHUNK_VRB: {<V.*|DT|IN>+<N.*>+<V.*|DT>?}
    """,
    r"""
    NP_CHUNK_NN: {<N.*><N.*>+}
    """
]


class CreateChunks():
  """A concrete class for creating chunks."""

  def __init__(self,):
    self.status = ''

  def get_conf(self, inp):
    foo = inp
    if isinstance(foo, list):
      self.conf = "list"
      self.status = 'r'
      return True
    elif isinstance(foo, str):
      if len(inp) < 150:
        if inp.startswith('http') or inp.lower().endswith(
                ('.com', '.htm', '.php', '.html', '/')):
          #only wiki links for now
          assert inp.__contains__('wikipedia'), "we are only processing wiki links for now"
          print "link"
          self.conf = "link"
          self.status = "2"
          return True
      self.conf = "para"
      self.status = '1'
      return True
    else:
      raise Exception("Unknown Object Type")

  def sanity_check(self):
    #sanity check on status
    assert self.status=='r', "Assertion Error:::convert it into a list first, the current status is %s"%self.status
    #sanity check on
    return True

  def cleanup(self, sent_list):
    self.sanity_check()
    # input is a list of sentences
    # remove all the special chars
    proc1 = []
    processed_sents = []
    for sentence in sent_list:
      temp = ' '.join(word for word in sentence.split()
                      if not word.lower().startswith(('http', '(http',)))
      temp = temp.replace('&quot', '')
      temp = temp.replace('&amp', '')
      for char in sentence:
        if not char.lower() in 'abcdefghijlijklmnopqrstuvwxyz' and char != ' ':
          temp = temp.replace(char, '')
      proc1.append(temp.lower())
      #for removing links
    for sent in proc1:
      temp = ''
      for word in sent.split():
        if word.endswith(('com', 'org')) or len(word) < 2 or word in ('rt',):
          continue
        try:
          word.encode('ascii')
        except:
          continue
        # remove links such as edit for wiki links
        #if self.conf == '2':
        #  if word.__contains__(('edit','hide','citation')):
        #    continue
        #else:
        temp += word + ' '
      processed_sents.append(temp.strip())
    return processed_sents

  def post_cleanup(self, tag_sent, keyword=None):
    #TODO: if len of chunk is > 3, permute over it and give 3 word chunks
    tuple_iii = []
    for node in tag_sent:
      if len(node) > 3:
        for id, leaf in enumerate(node):
          try:
            tuple_iii.append((node[id], node[id + 1], node[id + 2]))
          except:
            pass
      else:
        tuple_iii.append(node)
    cleaned_up = []
    for chunk in tuple_iii:
      temp = ' '.join(i for i, j in chunk if j not in (
                      'IN', 'VBP', 'DT', 'VBZ', 'PRP'))
      try:
        temp = temp.encode('ascii')
      except:
        continue
      cleaned_up.append(temp)
    if keyword:
      temp = []
      for chunk in cleaned_up:
        for word in keyword.split():
          if chunk.__contains__(word):
            temp.append(chunk.strip())
      cleaned_up = [i for i in set(temp) if len(i.split()) >= 2]
    #print cleaned_up
    return cleaned_up
    #    if pos in

  #only wiki links
  #TODO
  def process_link(self, inp):
    """
    Take up a link download the html, clean it and break it into sents
    """
    url = inp
    try:
      request = urllib2.Request(url)
      request.add_header('User-Agent', self.browsers[randint(0, 28)])
      request.add_header('Accept',
                         ('text/html,application/xhtml+xml,'
                          'application/xml;q=0.9,*/*;q=0.8'))
      request.add_header('Accept-Language', 'en-us,en;q=0.5')
      soup = BeautifulSoup(urllib2.urlopen(request).read())
      content_div = soup.findAll(id="content")[0]
      raw_text = clean_html(str(content_div))
      f = open('wiki_text2.txt', 'w')
      f.write(raw_text)
      f.close()
      return self.process_text(raw_text)
    except:
      traceback.print_exc()
      raise "cant process link :traceback:%s" % traceback.format_exc()

  def process_text(self, inp):
    #inp should be a text
    assert isinstance(inp, str), ('input type should be a string instead '
                                  'found: %s') % type(inp)
    whole_new_list = []
    #removing all wiki related things
    inp = re.sub(r'\[[a-z]+\]', '', inp)
    #split the whole text by '.'
    sents_list = inp.split('.')
    for sent in sents_list:
      temp = sent.split('\n')
      whole_new_list += temp
    sents_list = whole_new_list
    #TODO: remove words starting '[' and ending with ']'
    #update the status
    self.status = 'r'
    return sents_list

  #@sanity_check
  def start_chunks(self, inp, keyword=None):
    #validate input
    try:
      print type(inp)
      self.get_conf(inp)
    except AssertionError:
      return None, "error in validating input"
    except:
      return None, "Unknown Object Type"
    print "starting job:::status:%s" % self.status
    self.inp = inp
    self.processed_inp = inp  # this should always be list of sentences
    # there are 3 levels of processing involved acc to statuses
    i = 0
    while i < 4:
      status = self.status
      if status == 'r':
        #self.processed_inp
        print "status success"
        break
      if status == '1':  # chunk
        print "found a chunk"
        #call a func
        self.processed_inp = self.process_text(inp)
        pass
      if status == '2':  # link
        print "link"
        #call a func
        self.processed_inp = self.process_link(inp)
        pass
      i += 1
    #preprocessing
    sentences = self.cleanup(self.processed_inp)
    #now do a sanity check
    self.sanity_check()  # now
    print "tagging each word to its pos tag"
    #tag pos to each word in a sentence
    pos_sents = self.tag_sent(sentences)
    print "making chunks"
    tag_sent = self.parse_sent(pos_sents)
    # postprocessing
    tag_sent = self.post_cleanup(tag_sent, keyword=keyword)
    #print tag_sent
    #local filtering
    return set(tag_sent), False
    #tuple_iii = []
    #for node in tag_sent:
    #  for id, leaf in enumerate(node):
    #    try: tuple_iii.append((node[id],node[id+1],node[id+2]))
    #    except: pass

  #{<DT|IN|JJ.*|PRP|NUM>*<NN.*>*<IN|JJ|NUM>?}
  #{<DT|IN|JJ.*|PRP|NUM>*<NN.*>*<IN|JJ|NUM>?}

  def parse_sent(self, pos_tagged_sentence, grammar=None):
        #wq = csv.writer(open('wiki2.csv','w'))
    parsed_tagged_sents = []
    for grammar in GRAMMARS:
      #if not grammar:
        #grammar = r"""
        #  NP_CHUNK: {<VBP|VBG|VB|VB*|IN|JJ>*<NNP|NN>*<VBP|VBG|VB|IN|JJ>?}
        #  """
      parsedsent = []
      #parsed_tagged_sents = []
      cp = RegexpParser(grammar)
      for sentence in pos_tagged_sentence:
        result = cp.parse(sentence)
        #print result
        for node in result:
          if str(type(node)) == "<class 'nltk.tree.Tree'>":
            #wq.writerow((grammar.strip(),sentence,node.leaves()))
            temp = ' '.join(word for word, POS in node.leaves())
            if len(temp.split()) >= 2:
              parsedsent.append(temp)
              parsed_tagged_sents.append(node.leaves())
              #print grammar,node.leaves()
    return parsed_tagged_sents

  def tag_sent(self, sentences):
    pos_sentence = []  # a list of list of pos of each word in each sentence
    for sentence in sentences:
      #sentence.remove(r'http*')
      pos_sentence.append(pos_tag(sentence.split()))
    #ws = csv.writer(open('tagged_sentences','w'))
    #for i in pos_sentence:ws.writerow(i)
    return pos_sentence
