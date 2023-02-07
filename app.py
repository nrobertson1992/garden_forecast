import streamlit as st

st.title('Preston and Isaac help Nathan Plan a Garden')

st.write('What should I grow? Help me pick how many square feet of each crop I should grow, and click calculate to see the results. I only have 80 square feet, so don\'t put in more than that!')

col1, col2 = st.columns(2)

with col1:
	zucchini = st.number_input('How many sq ft of zucchini?',key='zucchini',min_value=0,max_value=80,step=1)
	cherry_tomatoes = st.number_input('How many sq ft of cherry tomatoes?',key='cherry_tomatoes',min_value=0,max_value=80,step=1)
	basil = st.number_input('How many sq ft of cherry tomatoes?',key='basil',min_value=0,max_value=80,step=1)
	spinach = st.number_input('How many sq ft of raspberries?',key='spinach',min_value=0,max_value=80,step=1)

with col2:
	raspberries = st.number_input('How many sq ft of raspberries?',key='raspberries',min_value=0,max_value=80,step=1)
	grapes = st.number_input('How many sq ft of grapes?',key='grapes',min_value=0,max_value=80,step=1)
	squash = st.number_input('How many sq ft of raspberries?',key='squash',min_value=0,max_value=80,step=1)
	broccoli = st.number_input('How many sq ft of broccoli?',key='broccoli',min_value=0,max_value=80,step=1)

if st.button('Calculate Nathan\'s Harvest'):
	space_used = zucchini + cherry_tomatoes + basil + spinach + raspberries + grapes + squash + broccoli
	if space_used > 80:
		st.write('Oh no! That\'s more than 80 square feet.')
	else:
		zucchini_harvest = zucchini * 1
		cherry_tomatoes_harvest = cherry_tomatoes * 20
		basil_harvest = basil * 2
		spinach_harvest = spinach * 1
		raspberries_harvest = raspberries * 3
		grapes_harvest = grapes * 4
		squash_harvest = squash * 1.5
		broccoli_harvest = broccoli * .66

		fruit_harvest = cherry_tomatoes_harvest + raspberries_harvest + grapes_harvest
		vegetable_harvest = zucchini_harvest + basil_harvest + spinach_harvest + squash_harvest + broccoli_harvest
		total_harvest = fruit_harvest + vegetable_harvest

		st.header('Vegetable Harvest')
		st.markdown("""
			There will be **{}** pounds of vegetables produced.
			""".format(vegetable_harvest))
		st.markdown("""
			* Zucchini: {} pounds
			* Basil: {} pounds
			* Spinach: {} pounds
			* Squash: {} pounds
			* Broccoli: {} pounds
			""".format(zucchini_harvest, basil_harvest, spinach_harvest, squash_harvest, broccoli_harvest))

		st.header('Fruit Harvest')
		st.markdown("""
			There will be **{}** pounds of vegetables produced.
			""".format(fruit_harvest))

		st.markdown("""
			* Cherry Tomatoes: {} pounds
			* Raspberries: {} pounds
			* Grapes: {} pounds
			""".format(cherry_tomatoes_harvest, raspberries_harvest, grapes_harvest))

		st.header('Total Harvest')
		st.markdown("""
			There will be a total of **{}** pounds of produce generated in Nathan's garden over the season, and {} square feet left over.
			""".format(total_harvest, 80-space_used))

