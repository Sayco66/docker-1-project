FROM busybox

ENV VAR_1="Some variable for 1"

RUN export VAR_1="Some variable for 1, but different"

RUN export VAR_2="Some variable for 2"

CMD echo FOO is $VAR_1, BAR is $VAR_2