import glob
import pandas as pd
import numpy as np
from IPython.display import display
import seaborn as sns
import matplotlib.pyplot as plt

search_values = [0.01, 0.03, 0.05, 0.07, 0.1, 0.3, 0.5, 0.7]

def load_df(file_name_pattern):
    file_names = glob.glob(file_name_pattern)
    if len(file_names) > 0:
        df = pd.read_csv(file_names[0])
        df.rename(columns={'Unnamed: 0': 'Trial'}, inplace=True)
        return df
    return pd.DataFrame()

def display_trial_stats(df, title_prefix, ylim_bottom, ylim_top):
    successes = df[df.reached_destination==True].Trial
    failures = df[df.reached_destination==False].Trial

    print "The destination was reached in {} out of {} trials.".format(successes.shape[0], df.shape[0])
    display(df[['total_reward', 'negative_reward', 'trial_length']].describe().T)

    sns.set(font_scale=1.5, style={"axes.facecolor": "white"})
    plt.figure(figsize=(16, 8))
    ax = sns.tsplot(df.trial_length, color='.75', legend=True, condition='Trial Length')
    ax = sns.tsplot(df.total_reward, color='#106B70', legend=True, condition='Total Reward')
    ax = sns.tsplot(df.negative_reward, color='#D43500', legend=True, condition='Negative Reward')
    ax = sns.rugplot(successes, color='green', height=1, linewidth=10, alpha=0.1)
    ax = sns.rugplot(failures, color='red', height=1, linewidth=10, alpha=0.1)
    plt.legend(labels=['Trial Length', 'Total Reward', 'Negative Reward', 'Reached Destination'], frameon=True)
    ax.set(xlabel='Trial', ylabel='Value')
    ax.set_title(title_prefix + ': Trial Length, Total Reward, and Negative Reward for each Trial')
    plt.ylim(ylim_bottom, ylim_top)
    plt.plot([0, 100], [0, 0], linewidth=1, color='.5')

def display_random_agent_stats():
    df = load_df("./data/trial_stats_*_random_agent.csv")
    display_trial_stats(df, 'Random Action Agent', -30, 70)

def display_naive_agent_stats():
    df = load_df("./data/trial_stats_*_naive_agent.csv")
    display_trial_stats(df, 'Naive Agent', -25, 45)

def display_informed_driver_agent_stats():
    df = load_df("./data/trial_stats_*_informed_driver_agent.csv")
    display_trial_stats(df, 'Informed Driver Agent', -5, 45)

def display_stats_for_the_q_learning_agent_with_params(value):
    df = load_df("./data/gridsearch/alpha_{}/*_g:{}_e:{}.csv".format(value, value, value))
    results = score_grid_search_results()["a:{},g:{},e:{}".format(value, value, value)]
    print "This agent received a fitness score of {}.".format(results['score'])
    display_trial_stats(df, "Q-Learning Agent: a, g, and e set to {}".format(value), -20, 70)

def calculate_scaled_score(score, maximum, minimum, bigger_is_better=True):
    if bigger_is_better:
        normalised_score = (float(score) - minimum) / (maximum - minimum)
    else:
        normalised_score = (maximum - float(score)) / (maximum - minimum)

    return normalised_score * 100

grid_search_extrema_memo = {}
def grid_search_value_extrema(memo_key, operation):
    if memo_key in grid_search_extrema_memo:
        return grid_search_extrema_memo[memo_key]
    min_val = 10000
    max_val = -10000

    for a in search_values:
        for g in search_values:
            for e in search_values:
                file_name_pattern = "./data/gridsearch/alpha_{}/*_g:{}_e:{}.csv".format(a, g, e)
                df = load_df(file_name_pattern)
                if not df.empty:
                    val = operation(df)
                    if val > max_val:
                        max_val = val
                    if val < min_val:
                        min_val = val

    extrama = {'max': max_val, 'min': min_val}
    grid_search_extrema_memo[memo_key] = extrama
    return extrama

def raw_total_reward_score_calculator(df):
    return np.average(df[df.Trial > 80].total_reward)

def raw_negative_reward_score_calculator(df):
    total_negative_reward = np.sum(df.negative_reward)
    last_trials_with_negative_rewards = df[df.negative_reward < 0].Trial.tolist()[-2:]
    return np.average(last_trials_with_negative_rewards) * total_negative_reward

def raw_trial_length_score_calculator(df):
    return np.average(df[df.Trial > 80].trial_length)

def raw_destination_score_calculator(df):
    last_trial_failures = df[df.reached_destination == False].Trial.tolist()[-2:]
    if len(last_trial_failures) == 0:
        return 0
    else:
        return np.average(last_trial_failures)

def fitness_score(df):
    raw_total_reward_score = raw_total_reward_score_calculator(df)
    total_reward_extrema = grid_search_value_extrema('avg_total_reward', raw_total_reward_score_calculator)
    total_reward_score = calculate_scaled_score(raw_total_reward_score, total_reward_extrema['max'], total_reward_extrema['min'])

    raw_negative_reward_score = raw_negative_reward_score_calculator(df)
    negative_reward_extrema = grid_search_value_extrema('avg_last_negative_rewards', raw_negative_reward_score_calculator)
    negative_reward_score = calculate_scaled_score(raw_negative_reward_score, negative_reward_extrema['max'], negative_reward_extrema['min'])

    raw_trial_length_score = raw_total_reward_score_calculator(df)
    trial_length_extrema = grid_search_value_extrema('avg_trial_length', raw_trial_length_score_calculator)
    trial_length_score = calculate_scaled_score(raw_trial_length_score, trial_length_extrema['max'], trial_length_extrema['min'], False)

    raw_destination_score = raw_destination_score_calculator(df)
    destination_extrema = grid_search_value_extrema('avg_last_trial_failures', raw_destination_score_calculator)
    destination_score = calculate_scaled_score(raw_destination_score, destination_extrema['max'], destination_extrema['min'], False)

    return np.average([total_reward_score, negative_reward_score, trial_length_score, destination_score])

scored_results_memo = {}
def score_grid_search_results():

    if len(scored_results_memo) > 0: return scored_results_memo

    for a in search_values:
        for g in search_values:
            for e in search_values:
                file_name_pattern = "./data/gridsearch/alpha_{}/*_g:{}_e:{}.csv".format(a, g, e)
                df = load_df(file_name_pattern)
                if not df.empty:
                    key = "a:{},g:{},e:{}".format(a, g, e)
                    scored_results_memo[key] = {
                            'df': df,
                            'score': fitness_score(df),
                            'params': {
                                'alpha': a,
                                'gamma': g,
                                'epsilon': e,
                            }
                        }

    return scored_results_memo

def find_optmal_parameters():
    scored_results = score_grid_search_results()
    sorted_results = sorted(scored_results.items(), key=lambda x: x[1]['score'], reverse=True)
    optimal_simulation_details = sorted_results[0][1]

    return (optimal_simulation_details['df'],
            optimal_simulation_details['params'],
            optimal_simulation_details['score'])

def find_least_optmal_parameters():
    scored_results = score_grid_search_results()
    sorted_results = sorted(scored_results.items(), key=lambda x: x[1]['score'])
    optimal_simulation_details = sorted_results[0][1]

    return (optimal_simulation_details['df'],
            optimal_simulation_details['params'],
            optimal_simulation_details['score'])

def display_optimal_simulation():
    df, params, fitness_score = find_optmal_parameters()
    print "The optimal parameters are: {}".format(params)
    print "This agent received a fitness score of {}.".format(fitness_score)
    title = "Optimal Q-Learning Agent: a:{}, g:{}, e:{}".format(
        params['alpha'], params['gamma'], params['epsilon'])
    display_trial_stats(df, title, -20, 70)

def display_least_optimal_simulation():
    df, params, fitness_score = find_least_optmal_parameters()
    print "The least optimal parameters are: {}".format(params)
    print "This agent received a fitness score of {}.".format(fitness_score)
    title = "Least Optimal Q-Learning Agent:\na:{}, g:{}, e:{}".format(
        params['alpha'], params['gamma'], params['epsilon'])
    display_trial_stats(df, title, -20, 70)

def display_grid_search_score_heatmaps():
    scored_results = score_grid_search_results()
    scores = [result['score'] for key, result in scored_results.iteritems()]
    max_score = max(scores)
    min_score = min(scores)
    ax = plt.figure(figsize=(16, 25))
    plot_title = "Grid Search Fitness Scores\nMin: {}   |   Max: {}".format(round(min_score, 3), round(max_score, 3))
    plt.suptitle(plot_title)
    cbar_ax = ax.add_axes([0.05, 0.92, 0.935, 0.02])
    for i in range(0,len(search_values)):
        alpha = search_values[i]
        score_grid = pd.DataFrame(columns=search_values)
        for gamma in reversed(search_values):
            gamma_scores = []
            for epsilon in search_values:
                key = "a:{},g:{},e:{}".format(alpha, gamma, epsilon)
                gamma_scores.append(scored_results[key]['score'])
            gamma_df = pd.DataFrame([gamma_scores], index=[gamma], columns=search_values)
            score_grid = score_grid.append(gamma_df)
        plt.subplot(4,2,i+1)
        ax = sns.heatmap(score_grid,
                         annot=True,
                         cmap=sns.blend_palette(['#D43500','#FFFFFF', '#005C28'], as_cmap=True),
                         cbar=i == 0,
                         vmin=min_score, vmax=max_score,
                         cbar_ax=None if i else cbar_ax,
                         cbar_kws={"orientation": "horizontal"})
        ax.set(xlabel='Epsilon', ylabel='Gamma')
        ax.set_title('Alpha {}'.format(alpha))
    plt.tight_layout()
    plt.subplots_adjust(top=0.88)
    plt.show()

def remove_empty_rows(df, columns):
    return df[(df[columns].T != 0).any()]

def optimal_q_and_n_less_empty_rows():
    truncator = lambda x: round(x, 3)
    numeric_columns = ['forward', 'left', 'right', 'None']
    Q_sparse = remove_empty_rows(load_df("./data/Q_optimal_*.csv"), numeric_columns)
    Q_sparse[numeric_columns] = Q_sparse[numeric_columns].applymap(truncator)

    N_sparse = remove_empty_rows(load_df("./data/N_optimal_*.csv"), numeric_columns)

    print "State encoding:"
    print "    tl: Traffic light"
    print "    o:  Oncoming traffic"
    print "    r:  Traffic coming from the right"
    print "    l:  Traffic coming from the left"
    print "    dd: Desired direction"
    print "NB: Please note that states that were not experienced by the agent are not displayed.\n"
    print "Q(s,a):"
    display(Q_sparse)
    print "N(s,a):"
    display(N_sparse)
