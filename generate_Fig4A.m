%% Load data
load('erp3.mat');
load('gamma.mat');
load('group.mat');

%% Load a random number generator seed for repeatable bootstraps
load('s.mat')
rng(s);

%% Classification
x = [erp3, gamma]; % Change this to include just ERP or botth ERP and gamma
y = group;
n_splits = 50;
perc = 90;
accuracy = zeros(n_splits, 1);
for k = 1:n_splits
    [x_train, x_test, y_train, y_test] = train_test_split(x, y, perc);
    model = fitcsvm(x_train, y_train);
    label = model.predict(x_test);
    accuracy(k) = sum(label == y_test)*100 / numel(label);
    hold on;
    plotBoundary2D(model, x, y, 0.1/n_splits); % Will superpose different splits
    fprintf(1, 'Split #%d, Classification Accuracy = %0.2f %%\n', k, accuracy(k));
end
fprintf(1, 'Mean accuracy = %0.2f %%\n', mean(accuracy));
xlabel('ERP (Z-score)', 'FontSize', 20);
ylabel('Gamma Power (Z-score)', 'FontSize', 20);
set(gca, 'FontSize', 20);

