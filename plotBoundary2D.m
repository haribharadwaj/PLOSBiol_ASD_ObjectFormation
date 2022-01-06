function plotBoundary2D(model, x, y, alpha)
% Plots decision boundary for 2-way classification in 2D feature space

if ~exist('alpha', 'var')
    alpha = 0.1;
end

x1_range = linspace(floor(min(x(:, 1)) - 1), ...
    ceil(max(x(:, 1))+1), 100);
x2_range = linspace(floor(min(x(:, 2)) - 1), ...
    ceil(max(x(:, 2)) + 1), 100);


if ~ishold
    figure;
end
cats = categories(y);
[x1grid, x2grid] = meshgrid(x1_range, x2_range); 
xgrid = [x1grid(:), x2grid(:)];
label = model.predict(xgrid);
label = double(reshape(label, size(x1grid)) == cats{1});
hold on;
h = pcolor(x1grid, x2grid, label);
h.EdgeColor = 'none';
set(h, 'facealpha', alpha);
shading('interp');
hold on;
plot(x(y == cats{1}, 1), x(y == cats{1}, 2), 'sr',...
    'markersize', 10, 'linew', 2, 'markerfacecolor', 'r'); 
hold on;
plot(x(y == cats{2}, 1), x(y == cats{2}, 2), 'ob',...
    'markersize', 10, 'linew', 2, 'markerfacecolor', 'b');
axis tight;
