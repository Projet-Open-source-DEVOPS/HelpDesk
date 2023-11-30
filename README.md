# HelpDesk

## COMMENT LANCER LE PROJET

ET BIEN VOUS ALLEZ DANS LE REPERTOIRE STANDALONE

```bash 
cd standalone
```

ET VOUS FAITES
```bash
./setup.sh
docker-compose up -d
```

A VOUS LES STUDIOS
## FAQ
### When I run the launch.sh script, I have the error : /bin/bash^M : bad interpreter

Type this command on your bash terminal :
```bash
sed -i -e 's/\r$//' setup.sh
```

And try running it again, it should works.
```bash
./setup.sh
```
