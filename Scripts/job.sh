#!/bin/bash
python=
metadata_path=
xml_path=

core=fbk_test1__CORE_DATASET
master=fbk_test1__MASTER_DATA
visual=fbk_test1__VISUALIZATION_TABLES
prefix=fbk_test1__

dhost=''
dport='31010'
duser=''
dpass=''

EXTRACT=1
GRAPHS=1
MARKDOWN=1

if [[ $EXTRACT == '1' ]]
then
    echo 'Extract metadata.'
    $python metadata_extractor.py --data-path $metadata_path \
                                  --xml-path $xml_path \
                                  --dremio-host $dhost \
                                  --dremio-port $dport \
                                  --dremio-user $duser \
                                  --dremio-pass $dpass \
                                  --space-core $core \
                                  --space-master $master \
                                  --space-visual $visual \
                                  --prefix $prefix
fi

if [[ $GRAPHS == '1' ]]
then
    echo 'Create graphs.'
    $python create_graph_png.py --data-path $metadata_path \
                                --space-core $core \
                                --space-master $master \
                                --space-visual $visual
fi

if [[ $MARKDOWN == '1' ]]
then
    echo 'Write markdown.'
    $python write_markdown.py --data-path $metadata_path
fi
