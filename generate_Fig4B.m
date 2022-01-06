%% Load data
load('erp3.mat');
load('gamma.mat');
load('group.mat');
load('srs_sci.mat');

%% Regression SRS_SCI -- ASD only
x = [erp3(group=='ASD'), gamma(group=='ASD')];
y = srs_sci(group=='ASD');
model = fitlm(x, y);
srs_predicted = model.predict(x);
figure;
plot(srs_predicted, y, 'sr',...
    'linew', 2, 'markersize', 10, 'MarkerFaceColor', 'r');
hold on;
plot(srs_predicted, srs_predicted, '--k',...
    'linew', 2);
[r, p] = corrcoef(srs_predicted(~isnan(y)), y(~isnan(y)));

% Direction of correlation has a priori expectation => Use 1-tailed p-vals
fprintf(1, 'R = %0.2f, P = %f\n', r(1, 2), p(1, 2)/2);
xlabel('Predicted SRS-SCI Score', 'FontSize', 20);
ylabel('Observed SRS-SCI Score', 'FontSize', 20);
set(gca, 'FontSize', 20);