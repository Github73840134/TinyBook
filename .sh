echo "Starting Installation"
wget https://tinybookdownload.sethedwards.repl.co/cli/p1 -t 3 -O decoder.py
wget https://tinybookdownload.sethedwards.repl.co/cli/p2 -t 3 -O lib.pac
python3 decoder.py
python3 -c "import tinybook;tinybook.update()"
rm -rf decoder.py
rm -rf lib.pac
rm -rf mcli.sh
echo "Installation Complete"