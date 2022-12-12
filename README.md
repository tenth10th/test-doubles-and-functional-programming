# Test Doubles and Functional Programming

We cover the practice of writing Tests for Software very frequently here at [Boston Software Crafters](), but usually apply Test Driven Development to fairly simple cases, some of which are already (intentionally, even!) easy to write tests for.

Unit Testing, especially, is a "functional" practice, and it's not really a surprise that it's easier to do against "purely functional" code:

 * Takes explicit inputs (fewer is better!) and doesn't read from shared or global state

 * Does not "mutate" or alter any object(s) that are passed in as inputs

 * Does not write to or otherwise "mutate" any shared or global state

 * Returns new objects or values as outputs (again, not altering the inputs - treating inputs and outputs as if they were immutable, even if they _technically_ aren't)

In pure (or "mostly pure") functional scenarios, it's easy to write tests - Pass in some inputs, and make assertions about the expected outputs.

Unfortunately, we sometimes have to deal with "side effects" - We might have very practical reasons for breaking the above rules, such as:

 * Reading from or writing to a Database, a File, or some other Data Store

 * Requesting data from an API, somewhere else in our system (possibly via code we didn't write!)

 * Requesting data through HTTP, where any number of surprising things could go wrong each time we make a request!

How can we change our tactics in difficult situations? What can we do when our code relies on other code or libraries that we can't control, or gets data from dynamic and/or unreliable sources, e.g. "The Internets"?

Let's do a quick, introductory overview of two approaches for Testing things that are hard to test.

_*DISCLAIMER:* These are very deep topics, and we're going to talk about two of them tonight - Needless to say, we're just going to scrape the surface, but hopefully enough to get you interested. Functional Programming, especially, is a "whole thing", but I'm just going to touch on it, in the context of testing._

## Test Doubles

Terminology around Testing, and especially around Mocking, is extremely inconsistent! Naming stuff is hard, and every new language and testing library is a new chance to mis-use some words. But having clear vocabulary is important!

The phrase "Test Double" can be used to describe ["any case where you replace a Production object, for Testing Purposes."](https://martinfowler.com/bliki/TestDouble.html#:~:text=Test%20Double%20is%20a%20generic,production%20object%20for%20testing%20purposes.), and in his Blog post, Martin Fowler attempts to itemize some more specific types of them as well:

 * *Dummy* objects are passed around, but never actually used (i.e. they are just used to satisfy the requirements for calling a function or method).

 * *Fake* objects actually have working implementations, but usually take some shortcut which makes them not suitable for Production (an InMemoryTestDatabase is a good example).

 * *Stubs* provide canned answers to calls made during the test, usually not responding at all to anything outside what was needed for a specific test.

 * *Spies* are stubs that also record some information based on how they were called. One form of this might be an email service that records how many messages it was sent.

 * *Mocks* are pre-programmed with expectations which form a specification of the calls they are expected to receive. They can throw an exception if they receive a call they don't expect and are checked during verification to ensure they got all the calls they were expecting.

Depending on your preferred Stack and 

## Functional Core, Imperative Shell

Functional Programming is a very deep, diverse, and sometimes controversial subject, and some smart, very passionate people would be happy to explain why you should always use it - Or never ever use it at all.

To be honest, I'm not an expert, and we don't have the time to cover it in detail today.

But even without going into a lot of detail, there are some ideas we can borrow, in trying to write code that is easier to Test. (It also can't fully eliminate our need for Mocks and other Test Doubles, which is why I covered those first - But it can help us keep their usage to a minimum.)

## Setup

At minimum, we need to install the `PyTest` library (a framework for creating, discovering, and running Tests), and `Toolz`, which provides some Functional Programming abstractions for Python. We've also included some other handy Python development tools like `black` (for automatic code formatting), `isort` (for automatic import sorting) and `rope` (which helps VSCode perform refactoring in Python).

_(This setup should happen automatically in GitPod, but if not, use the "Manual Setup via Pip" instructions below.)_

### Automated Setup via Poetry

The dependencies and virtual environment of this project can be managed automatically using `poetry`:
```
poetry install
```

### Manual Setup via Pip
Alternately, create or select an environment through some other means, then install the required packages directly using `pip`. (If you open this repo in GitPod, you'll get a suitable Python environment automatically.)
```
pip install -r requirements.txt
```