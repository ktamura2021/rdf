#!/usr/bin/env python3

fp = open('RDF_triterpene.ttl', 'w')

# 既定のものはここに書く
# prefix.ccを使うとよく使われているURIがわかる(必ずしも最適解とは限らない)
fp.write('@prefix uniprot: <http://purl.uniprot.org/uniprot/> .\n')
fp.write('@prefix pubmed: <https://identifiers.org/> .\n')
fp.write('@prefix rh: <http://rdf.rhea-db.org/> .\n')
fp.write('@prefix CHEBI: <http://purl.obolibrary.org/obo/CHEBI_> .\n')
fp.write('@prefix : <https://raw.githubusercontent.com/ktamura2021/rdf/main/ontology.ttl#> .\n')
# 自分の述語を定義しておかないといけない ":" ひとまず自分の管理下の場所を指定する file名に#を突っ込む
# purl.org(https://purl.archive.org)に登録して、自分の述語を置くところを指定して、そこから自分のgithubのオントロジーファイル(自分で使ったtermを規定していく)
# togoidのリポジトリが参考になる(https://github.com/togoid/togoid-config/blob/main/ontology/togoid-ontology.html)


num = 0
with open('triterpenoid_DB_PCP2015.tsv', encoding='utf-8') as f:
    for row in f:
        if num == 0:
            num += 1
            continue
        else:
            fields = row.strip().split('\t')
            fp.write('\n')
            fp.write(f'[]\n') #空ノード []
            fp.write(f'    :uniprot uniprot:{fields[0]} ;\n') #:uniprotはedgeの定義、uniprot:がprefix
            fp.write(f'    :citation pubmed:{fields[1]} ;\n') #objectは:で定義されているものか、""で囲むただの文字列
            fp.write(f'    :commonname "{fields[2]}" ;\n')
            fp.write(f'    :rhea rh:{fields[3]} ;\n')
            fp.write(f'    :substrate CHEBI:{fields[4]} ;\n')
            fp.write(f'    :product CHEBI:{fields[5]} .\n')
            num += 1


fp.close()

