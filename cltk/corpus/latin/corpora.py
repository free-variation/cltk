"""Latin language corpora available for download or loading locally.
All remote corpora hosted by github on the cltk organization account, eg:
'http://github.com/cltk' + name
"""

LATIN_CORPORA = [
    {'encoding': 'utf-8',
     'markup': 'tei_xml',
     'location': 'remote',
     'type': 'text',
     'name': 'latin_text_perseus'},
    {'encoding': 'utf-8',
     'markup': 'xml',
     'name': 'latin_treebank_perseus',
     'location': 'remote',
     'type': 'treebank'},
    {'encoding': 'utf-8',
     'markup': 'plaintext',
     'name': 'latin_text_lacus_curtius',
     'location': 'remote',
     'type': 'text'},
    {'encoding': 'utf-8',
     'markup': 'plaintext',
     'name': 'latin_text_latin_library',
     'location': 'remote',
     'type': 'text'},
    {'encoding': 'latin-1',
     'markup': 'beta_code',
     'name': 'phi5',
     'location': 'local',
     'type': 'text'},
    {'encoding': 'latin-1',
     'markup': 'beta_code',
     'name': 'phi7',
     'location': 'local',
     'type': 'text'},
    {'encoding': 'utf-8',
     'markup': 'plaintext',
     'name': 'latin_proper_names_cltk',
     'location': 'remote',
     'type': 'lexicon'},
    {'name': 'latin_models_cltk',
     'location': 'remote',
     'type': 'model'},
    {'encoding': 'utf-8',
     'markup': 'python',
     'name': 'latin_pos_lemmata_cltk',
     'location': 'remote',
     'type': 'lemma'},
    {'encoding': 'utf-8',
     'markup': 'xml',
     'name': 'latin_treebank_index_thomisticus',
     'location': 'remote',
     'type': 'treebank'},
    {'encoding': 'xml',
     'markup': 'plaintext',
     'name': 'latin_lexica_perseus',
     'location': 'remote',
     'type': 'lexicon'},
    {'encoding': 'utf-8',
     'markup': 'plaintext',
     'name': 'latin_training_set_sentence_cltk',
     'location': 'remote',
     'type': 'training_set'},
    {'name': 'latin_word2vec_cltk',
     'location': 'remote',
     'type': 'model'},
    {'encoding': 'utf-8',
     'markup': 'tei_xml',
     'location': 'remote',
     'type': 'text',
     'name': 'latin_text_antique_digiliblt'},
]
