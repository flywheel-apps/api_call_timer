import time
import os
import json

import pandas
import pandas as pd
import flywheel
from fw_client import FWClient

import StandardFinderCalls as fc

NREP = 300

def get_site_base(fw_client):
	site_url = fw_client.get_config().site.get('api_url')  # Get the URL
	site_base = site_url.rsplit('/', maxsplit=1)[0]  # Remove the "/api"
	site_base = site_base.split('/')[-1]  # remove the "http://"
	return site_base


def get_api_key_from_client(fw_client):
	"""
	Parses the api key from an instance of the flywheel client
	Args:
		fw_client (flywheel.Client): an instance of the flywheel client

	Returns:
		(str): the api key
	"""
	site_base = get_site_base(fw_client)
	key_string = fw_client.get_current_user().api_key.key
	api_key = ':'.join([site_base, key_string])
	return api_key


def prep_directory(fw):
	# Setup file structure
	site_base = get_site_base(fw)
	BASE_DIR = os.path.dirname(os.path.realpath(__file__))
	BASE_DIR = os.path.join(BASE_DIR, "Sites", site_base)
	if not os.path.exists(BASE_DIR):
		os.mkdir(BASE_DIR)

	DF_PATH = os.path.join(BASE_DIR, 'call_time_df.pkl')
	return BASE_DIR, DF_PATH


def load_or_create_df(DF_PATH):
	if os.path.exists(DF_PATH):
		df = pandas.read_pickle(DF_PATH)
		qlist = list(df['query'])
		tlist = list(df['time'])
		slist = list(df['site'])
		print(f'Loaded df with {len(df)} elements')

	else:
		qlist = []
		tlist = []
		slist = []

	data_dict = {'query': qlist, 'time': tlist, 'site': slist}

	return data_dict

def initialize_test_containers(fw, prjlabel, sublabel, seslabel, acqlabel):
	init_project = fw.projects.find(f"label={prjlabel}")
	if len(init_project) > 1:
		print('YO TOO MANY PROJECTS BRO, PICKING NUMERO UNO')
	init_project = init_project[0]
	init_subject = init_project.subjects.find_first(f"label={sublabel}")
	init_session = init_subject.sessions.find_first(f"label={seslabel}")
	init_acquisition = init_session.acquisitions.find_first(f"label={acqlabel}")

	print(f"plabel={prjlabel}")
	print(f"sublabel={sublabel}")
	print(f"seslabel={seslabel}")
	print(f"acqlabel={acqlabel}")
	return init_project, init_subject, init_session, init_acquisition


def run_query_calls(nrep, fw, core_client, data_dict, site, init_project, init_subject, init_session, init_acquisition):

	# These are used in the query strings and are needed as local variables
	prjlabel = init_project.label
	sublabel = init_subject.label
	seslabel = init_session.label
	acqlabel = init_acquisition.label

	for query in fc.test_calls:
		for i in range(nrep):
			print(query)
			a = time.time()
			try:
				exec(query)
			except Exception as e:
				print(e)
				a = 0
			if a:
				b = time.time()
			else:
				b = -1
			dur = b-a

			data_dict['query'].append(query)
			data_dict['time'].append(dur)
			data_dict['site'].append(site)

	return data_dict

def pop_df_metadata(df, core_client, init_project, BASE_DIR):
	projects = core_client.get('/api/projects?stats=true')
	nprojects = len(projects)
	project = core_client.get('/api/projects', params={"filter": f'label="{init_project.label}"',"stats":True,'limit':1})[0]

	nsubjects=project.get('subject_count','NA')
	nsessions=project.get('session_count','NA')
	nacquisitions=project.get('acquisition_count','NA')

	meta = {
		"nproj": nprojects,
		"nsub": nsubjects,
		"nses": nsessions,
		"nacq": nacquisitions
	}

	json_out = os.path.join(BASE_DIR, 'project_meta.json')
	# Serializing json
	json_object = json.dumps(meta, indent=4)
	print(f"saving to {json_out}")
	# Writing to sample.json
	with open(json_out, "w") as outfile:
		outfile.write(json_object)



def main(api_key, prjlabel, sublabel, seslabel, acqlabel):

	fw = flywheel.Client(api_key)

	# Initialize client
	api_key = get_api_key_from_client(fw)
	core_client = FWClient(api_key=api_key, client_name="my-app", client_version="1.0")

	BASE_DIR, DF_PATH = prep_directory(fw)
	data_dict = load_or_create_df(DF_PATH)
	site = get_site_base(fw)

	init_project, init_subject, init_session, init_acquisition = initialize_test_containers(fw, prjlabel, sublabel, seslabel, acqlabel)

	data_dict = run_query_calls(NREP, fw, core_client, data_dict, site, init_project, init_subject, init_session, init_acquisition)

	df = pd.DataFrame.from_dict(data_dict)
	print(f"saving to {DF_PATH}")
	df.to_pickle(DF_PATH)

	pop_df_metadata(df, core_client, init_project, BASE_DIR)

	return DF_PATH


#
# from fw_client import FWClient
# from fw_core_client import CoreClient
# import os
#
# api_key = os.environ["FWGA_API"]
# fw_client = FWClient(api_key=api_key, client_name="my-app", client_version="1.0")
# core_client = CoreClient(api_key=api_key, client_name="my-app", client_version="1.0")
#
# core_project = core_client.get(f"/projects", params={"filter":f'label=0000aaWork',"limit":1})
# fw_project = fw_client.get(f"/projects", params={"filter":f'label=0000aaWork',"limit":1})


# rsync -r davidparker@scien-dev1:/persistent-data/david/Finder-Tests /Users/davidparker/Documents/Flywheel/SSE/MyWork/Gears/Import_metadata_gitlab
# rsync -r /Users/davidparker/Documents/Flywheel/SSE/MyWork/Gears/Import_metadata_gitlab/Finder_Tests davidparker@scien-dev1:/persistent-data/david