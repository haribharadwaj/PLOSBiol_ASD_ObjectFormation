%% Load data
load('gammaFig3.mat');


%% Plot results (Fig. 3E)
ntd = 26;
nasd = 21;

figure;
errorbar(1, mean(gammaFig3(1:ntd)), std(gammaFig3(1:ntd))/sqrt(double(ntd)),...
    'ob', 'linew', 2, 'markersize', 8);
hold on;
errorbar(2, mean(gammaFig3((ntd+1):end)),...
    std(gammaFig3((ntd+1):end))/sqrt(double(nasd)),...
    'sr', 'linew', 2, 'markersize', 8);
xlim([0.5, 2.5]);
set(gca, 'FontSize', 14, 'Xtick', [1, 2], 'XTickLabel', {'TD', 'ASD'});
ylabel('Gamma Power (Z-Score)');

[h, p, ci, stats] = ttest2(gammaFig3(1:ntd), gammaFig3((ntd+1):end));
fprintf(1, 't = %f, p = %f\n', stats.tstat, p);