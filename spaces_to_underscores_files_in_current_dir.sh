for i in *' '*; do mv "$i" `echo $i | sed -e 's/ /_/g'`; done
