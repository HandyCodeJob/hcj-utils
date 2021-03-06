# Logging with papertrail

Get the v8 package for rsyslog (Ubuntu)

```
sudo add-apt-repository ppa:adiscon/v8-stable
sudo apt-get update
sudo apt-get install rsyslog
```

Get the v8 repo (centOS)

```
sudo curl -o /etc/yum.repos.d/rsyslog.repo http://rpms.adiscon.com/v8-stable/rsyslog.repo
sudo yum install rsyslog
```

Get the tls perm and check the md5:

```
sudo curl -o /etc/papertrail-bundle.pem https://papertrailapp.com/tools/papertrail-bundle.pem
echo c75ce425e553e416bde4e412439e3d09 /etc/papertrail-bundle.pem | md5sum -c -
```

Now edit the config file (we will make a newone in *.d/)

```
sudo vim /etc/rsyslog.d/22-papertrail.conf
```

Then add this
```
# Papertrail
$DefaultNetstreamDriverCAFile /etc/papertrail-bundle.pem # trust these CAs
$ActionSendStreamDriver gtls # use gtls netstream driver
$ActionSendStreamDriverMode 1 # require TLS
$ActionSendStreamDriverAuthMode x509/name # authenticate by hostname
$ActionSendStreamDriverPermittedPeer *.papertrailapp.com
# http://help.papertrailapp.com/kb/configuration/advanced-unix-logging-tips/#rsyslog_queue
$ActionResumeInterval 10
$ActionQueueSize 100000
$ActionQueueDiscardMark 97500
$ActionQueueHighWaterMark 80000
$ActionQueueType LinkedList
$ActionQueueFileName papertrailqueue
$ActionQueueCheckpointInterval 100
$ActionQueueMaxDiskSpace 2g
$ActionResumeRetryCount -1
$ActionQueueSaveOnShutdown on
$ActionQueueTimeoutEnqueue 2
$ActionQueueDiscardSeverity 0

*.*                                         @@logs.papertrailapp.com
```

Restart rsyslog now

```
sudo service rsyslog restart
```
