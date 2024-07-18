# What is a container?

A container is a self-contained, virtual computer. It exists as a file on your computer, but when run, can be interacted with as though the user is using a different computer.

## Why use containers?

For our use case(s), reproducibility is the biggest advantage. Since containers function as virtual computers, if everyone uses the same container, then we know the exact conditions and programs that were used to run analyses. There are no concerns about different people using different versions of software and/or operating systems. Another benefit to using containers, is that containers are portable. Because a container is just a file, it can easily be shared with someone else and that person will be able to run analyses exactly as you've run them, without the need to install the programs needed for the analyses.

Additionally, using containers allows us to install software without modifying the underlying operating system. Some software installations have are more complex than others and containers reduce the risk that we accidentally modify the underlying operating system in a way which screws things up.

# Creating containers

