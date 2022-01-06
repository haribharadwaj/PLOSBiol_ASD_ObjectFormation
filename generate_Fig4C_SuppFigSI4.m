%% Load data
load('aud7q_raw.mat');
load('erp3.mat');
load('gamma.mat');
load('group.mat');
load('age.mat');

%% Adjust for age if desired
age_adjust = false;   % true for Fig 4C, false for Supplementary Fig SI-4B

%% Regression Auditory Score -- ASD only
if age_adjust
    x = [erp3(group=='ASD'), gamma(group=='ASD'), age(group == 'ASD')];
else
    x = [erp3(group=='ASD'), gamma(group=='ASD')];
end

y = aud7q_raw(group=='ASD');
model = fitlm(x, y);
aud_predicted = model.predict(x);
figure;
plot(aud_predicted, y, 'sr',...
    'linew', 2, 'markersize', 10, 'MarkerFaceColor', 'r');
hold on;
[r, p] = corrcoef(aud_predicted(~isnan(y)), y(~isnan(y)));
fprintf(1,...
    'For predicted vs. observed auditory scores:\nR = %0.2f, P = %f\n',...
    r(1, 2), p(1, 2)/2);
if age_adjust
    xlabel('Predicted SPQ-APS_{AC}', 'FontSize', 20);
    ylabel('Observed SPQ-APS_{AC}', 'FontSize', 20);
else
    xlabel('Predicted SPQ-APS', 'FontSize', 20);
    ylabel('Observed SPQ-APS', 'FontSize', 20);
end
set(gca, 'FontSize', 20);

hold on; % Draw 45 degree line
% Note, a priori, positive corr expected, hence 1-sided p-value
plot(aud_predicted, aud_predicted, '--k', 'linew', 2);


%% PLOT AGE CORRELATIONS (Supplementary Fig SI-4A)
figure;

plot(age(group=='ASD'), aud7q_raw(group=='ASD'), 'sr',...
    'linew', 2, 'markersize', 10, 'MarkerFaceColor', 'r');
model = fitlm(age(group=='ASD'), aud7q_raw(group=='ASD'));
fitted  = model.predict(age(group=='ASD'));
hold on;
plot(age(group=='ASD'), fitted, '--k', 'linew', 2);
xlabel('Age (years)', 'FontSize', 20);
ylabel('SPQ-APS', 'FontSize', 20);
set(gca, 'FontSize', 20);

selectgroup = (group == 'ASD');

[r, p] = corrcoef(aud7q_raw(~isnan(aud7q_raw) & selectgroup),...
    age(~isnan(aud7q_raw) & selectgroup));
% Note, a priori, positive corr expected, hence 1-sided p-value
fprintf(1,...
    '--- \nFor age vs. auditory scores:\nR = %f, P = %f \n---\n',...
    r(1, 2), p(1, 2)/2);