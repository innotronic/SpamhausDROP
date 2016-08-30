# SpamhausDROP
This System V init script fetches and adds or removes the [Spamhaus DROP IP blacklist](https://www.spamhaus.org/drop/) to/from the routing table.
It combines the DROP, EDROP and DROPv6 list.
A daily cron job triggers refreshing.

## Usage
Just install the RPM and start the services a first time:

    service SpamhausDROP start

Check if the DROP list is active:

    service SpamhausDROP status

Force refreshing the list:

    service SpamhausDROP refresh

Remove blacklist:

    service SpamhausDROP stop 


## Build
If you like, build the RPM on your own:

  rpmbuild --rebuild SpamhausDROP-x.x-1.src.rpm


## License
Copyright (c) 2016 [Innotronic Ingenieurbüro GmbH](https://www.inno.ch/)


This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/.

