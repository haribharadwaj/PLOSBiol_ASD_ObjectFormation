function [x_train, x_test, y_train, y_test] = train_test_split(x, y, perc)

nsamps = numel(y);
ntrain = floor(perc * nsamps/100);

order = randperm(nsamps);
x_train = x(order(1:ntrain), :);
y_train = y(order(1:ntrain));
x_test = x(order((ntrain + 1):end), :);
y_test = y(order((ntrain + 1):end));


