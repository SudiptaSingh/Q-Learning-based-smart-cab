from agent import run

search_values = [0.01, 0.03, 0.05, 0.07, 0.1, 0.3, 0.5, 0.7]

for alpha in search_values:
    for gamma in search_values:
        for epsilon in search_values:
            run(alpha, gamma, epsilon)
