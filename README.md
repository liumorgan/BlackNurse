# BlackNurse
Blacknurse is a low bandwidth ICMP attack that is capable of doing denial of service to well known firewalls. Most ICMP attacks that we see are based on ICMP Type 8 Code 0 also called a ping flood attack. BlackNurse is based on ICMP with Type 3 Code 3 packets. We know that when a user has allowed ICMP Type 3 Code 3 to outside interfaces, the BlackNurse attack becomes highly effective even at low bandwidth