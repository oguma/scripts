echo "[.basex]"
cat .basex | grep -i port
echo ""
echo "[webapp/WEB-INF/jetty.xml]"
cat webapp/WEB-INF/jetty.xml | grep -i \"port\"
