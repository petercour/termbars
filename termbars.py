from termgraph import termgraph as tg

labels = ['2007', '2008', '2009', '2010', '2011', '2012', '2014']
data = [[83, 10], [31, 5.0], [16.43, 53.1], [50.21, 7.0],
        [88, 10], [42, 20.2], [30.0, 20.0]]
normal_data = [[48.059508408796894, 50.0], [60.971862871927556, 0.0],
               [3.080530401034929, 12.963561880120743],
               [12.184670116429496, 0.5390254420008624],
               [135.82632600258734, 1.4688443294523499],
               [55.802608883139285, 4.096593359206555],
               [6.737818025010781, 4.042690815006468]]
len_categories = 2
args = {'filename': 'data/ex4.dat', 'title': None, 'width': 25,
        'format': '{:<5.2f}', 'suffix': '', 'no_labels': True,
        'color': None, 'vertical': False, 'stacked': True,
        'different_scale': False, 'calendar': False,
        'start_dt': None, 'custom_tick': '', 'delim': '',
        'verbose': False, 'version': False}
colors = [91, 94]
tg.stacked_graph(labels, data, normal_data, len_categories, args, colors)


