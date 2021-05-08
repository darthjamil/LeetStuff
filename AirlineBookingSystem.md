# Requirements
## Functional
Sections (base these on fault domains)
- User accounts
- Finding flights
- Reservation, purchasing
- Booking lookup/update/cancel

Primary use cases
- Create account (GDPR, CCPA, security, partner connections)
- Find a flight (one-way, return flights)
- View potential flights (e.g. duration; up to date availability info)
- Configure and reserve the flight (emails, receipts)
- Flight reminders/notifications
- Booking lookup (cancellation, boarding pass, changes)
- Cancel/update booking

## Non-Functional
- HA, durable, scalable (to number of customers and flights)
- Endpoint tracking, distributed error logging
- Applicable to multiple airports
- Analytics, reporting
- Metrics, alerting
- Account security

## Scalability assumptions
- Rolled out in 1 airport, then to many
- Airport has 1,000 flights per day
- 1M bookings per day to start per airport
- One day this system might not be tied to an airport, but may become more central

# Design
- Microservice architecture
  -- Based on fault domains: user accounts, search, purchase, view/configure flight info

## Front-End
user --> LB --> - front-end server 1
                - front-end server 2
                - ...
                (JS/React for Web, React Native for mobile, statically rendered pages served from Node/Next.JS)
                (Next.JS may allow us to host the static site on a CDN)

## Back-End
request --> service discovery --> - LB --> account management API
                                  - LB --> flight search API
                                  - LB --> purchase API
                                  - LB --> booking API

admin user/service --> LB --> flight entry API

Services written in Node.

## Storage
Flight Entry API   w--> SQL cluster (flights data)
                   w--> Elastic Search cluster
                   w--> <bus>
                       
Flight Search API  r--> Elastic Search cluster

Purchasing API     w--> RavenDB cluster (purchases)

Booknig API        w--> RavenDB cluster (booking data)
                   w--> <bus>

NB: User accounts API not shown

## Workers
- Search worker: Updates Elastic based on new flights, flight cancellation, new bookings, booking cancellations.

## APIs
Admin
- Guid Create(string source, string destination, FlightDetails details) // returns flightID
- void Cancel(Guid flightID) // cancels flight
- FlightSummary Search(int page, int itermsPerPage, FilterCriteria criteria)

Search
- FlightSummary Search(string fromCity, string destinationCity, int page, int itermsPerPage, FilterCriteria criteria) // different flightSUmmary object from above

Booking
- Guid? Book(Guid flightID)
- bool Cancel(Guid bookingID)

NB: Update, etc not shown
NB: User account and purchasing APIs not shown

# Analytics
## Monitoring
- Flights booked per day [success/fail]
- Searches per day
- Number of accounts created
- GA stats (e.g. page views, etc.)

## Metrics
- Number of cancellations over time [by ariline, by source, by destination]
- Ratio of searches that led to a booking per week


