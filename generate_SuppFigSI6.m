%% Load data
load('nepsy_ICSSinh.mat');
load('gamma.mat');
load('group.mat');

%%
y = nepsy_ICSSinh(group=='ASD');
x = gamma(group=='ASD');
figure;
plot(gamma(group=='ASD'), y, 'sr',...
    'linew', 2, 'markersize', 10, 'MarkerFaceColor', 'r');
hold on;
[r, p] = corrcoef(x(~isnan(y)), y(~isnan(y)));
fprintf(1, 'ASD only: R = %0.2f, P = %f\n', r(1, 2), p(1, 2)/2);

ylabel('ICSS_{inh} Scores', 'FontSize', 20);
xlabel('MEG Gamma Activity', 'FontSize', 20);
set(gca, 'FontSize', 20);


%% Plot TD as needed
includeTD = true;
if includeTD
    y = nepsy_ICSSinh(group=='TD');
    x = gamma(group=='TD');
    
    plot(x, y, 'ob',...
        'linew', 2, 'markersize', 10, 'MarkerFaceColor', 'b');
    hold on;
    
    [r, p] = corrcoef(x(~isnan(y)), y(~isnan(y)));
    fprintf(1, 'TD only: R = %0.2f, P = %f\n', r(1, 2), p(1, 2)/2);
    
end

%% Correlation with both groups if TD is included
y = nepsy_ICSSinh;
x = gamma;
[r, p] = corrcoef(gamma(~isnan(y)), y(~isnan(y)));
fprintf(1, 'Both groups: R = %0.2f, P = %f\n', r(1, 2), p(1, 2)/2);
