#GETIP

I was at the Stansted airport lounge waiting to catch my flight to Bologna for the weekend. With 2 hours to kill I thought I should spend it wisely rather than shopping or walking aimlessly in the departure area. And what better way to do that than hack together something that was both simple, useful and won't take forever to accomplish. So, I decided to put together this simple tool for looking up domain information. It runs on a command line and can only query one domain at a time ATM but have included a todo list with all the improvements I plan to make in the future. If you have an idea for an improvement or feature request please raise a ticket or pull request and I will definitely look into it.

Command line utility to get location information for an IP or Domain name via [ip-api.com](http://ip-api.com/docs/api:json)

## Usage

Add binary to $PATH

```
$ getip yahoo.co.uk

+----------------------------------+-----------------------+
|              Value               |       Response        |
+==================================+=======================+
| Country:                         | United Kingdom        |
+----------------------------------+-----------------------+
| Country Code:                    | GB                    |
+----------------------------------+-----------------------+
| Region:                          | ENG                   |
+----------------------------------+-----------------------+
| Region Name:                     | England               |
+----------------------------------+-----------------------+
| City:                            | London                |
+----------------------------------+-----------------------+
| Latitude:                        | 51.514                |
+----------------------------------+-----------------------+
| Longitude:                       | -0.129                |
+----------------------------------+-----------------------+
| Timezone:                        | Europe/London         |
+----------------------------------+-----------------------+
| ISP:                             | Yahoo! Europe         |
+----------------------------------+-----------------------+
| Organisation:                    | Yahoo! Europe         |
+----------------------------------+-----------------------+
| Autonomous System Number & Name: | AS34010 Yahoo! Europe |
+----------------------------------+-----------------------+
| Querying data Address (You):     | 77.238.184.24         |
+----------------------------------+-----------------------+
```


