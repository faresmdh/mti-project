# Football club management system

## SRP Principle
* New class ClubManager to handle loading and saving data, allows to separate data class Club and operations class ClubManager.
* New class EventManager to make operations such as adding player to event or removing a player from event.

## OCP Principle
* Make event class an abstract class allowing to add multi types of events such as matches and trainings. This allows to make our code closed for edits (editing the event) and open for extension (create multi types of events)
* Create MonthlySubscription, Subscription and YearlySubscription inherit from the parent class BasicSubscription.

## LSP Principle
