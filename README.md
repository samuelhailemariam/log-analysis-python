## log-analysis-with-python

#### Log Analysis Using Regular Expressions with Python

A Python script that automates the processing of of a given application log and generates a report based on the information extracted from the log files. There are two reports generated. The first generates a report of frequency of error types and second generated a list of users with the accompanying frequency of ERRORS or INFO messages generated.

##### Example of log file entries:

- May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (breee)
- May 27 11:47:40 ubuntu.local ticky: ERROR: Permission denied while closing ticket [#1234] (britanni)
- May 27 11:51:40 ubuntu.local ticky: INFO: Created ticket [#1234] (ahmed.miller)
- May 27 11:55:40 ubuntu.local ticky: ERROR: Ticket doesn't exist [#1234] (enim.non)
- May 27 11:59:40 ubuntu.local ticky: INFO: Permission denied while closing ticket [#1234] (ahmed.miller)
