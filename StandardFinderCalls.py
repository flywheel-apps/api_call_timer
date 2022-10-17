


test_calls = [
    ##################
    # Project Calls ##
    ##################
    # Simply call the project by label
    "project=fw.projects.find(f'label={prjlabel}')",
    # Call by label and ID
    "project=fw.get_project(init_project.id)",

    # Call with core client
    'project=core_client.get(f"/api/projects", params={"filter":f"label={prjlabel}","limit":1})',
    # Repeat with limit 2
    'project=core_client.get(f"/api/projects", params={"filter":f"label={prjlabel}","limit":2})',
    'project=core_client.get(f"/api/projects", params={"filter":f"label={prjlabel}","limit":200})',

    ##################
    # Subject Calls ##
    ##################
    'subject = fw.subjects.find(f"label={sublabel},parents.project={init_project.id}")',
    'subject = init_project.subjects.find(f"label={sublabel}")',
    'subject = fw.get_subject(f"{init_subject.id}")',

    # Search all subjects for the subject in the project label
    'subject=core_client.get(f"/api/subjects",params={"filter":f"label={sublabel},project.label={prjlabel}","limit":1})',
    # Search all subjects for the subject in the project ID
    'subject=core_client.get(f"/api/subjects",params={"filter":f"label={sublabel},parents.project={init_project.id}","limit":1})',
    # Search subjects specifically in the project for the label
    'subject=core_client.get(f"/api/projects/{init_project.id}/subjects", params={"filter":f"label={sublabel}","limit":1})',

    # Repeate above with limit=2
    # Search all subjects for the subject in the project label
    'subject=core_client.get(f"/api/subjects",params={"filter":f"label={sublabel},project.label={prjlabel}","limit":2})',
    'subject=core_client.get(f"/api/subjects",params={"filter":f"label={sublabel},project.label={prjlabel}","limit":200})',

    # Search all subjects for the subject in the project ID
    'subject=core_client.get(f"/api/subjects", params={"filter":f"label={sublabel},parents.project={init_project.id}","limit":2})',
    # Search subjects specifically in the project for the label
    'subject=core_client.get(f"/api/projects/{init_project.id}/subjects", params={"filter":f"label={sublabel}","limit":2})',

    ##################
    # Session Calls ##
    ##################
    # Find the session with traditional finder and labels
    'session=fw.sessions.find(f"label={seslabel},subject.label={sublabel},project.label={prjlabel}")',
    # Find the session with traditional finder and IDs
    'session=fw.sessions.find(f"label={seslabel},parents.subject={init_subject.id},parents.project={init_project.id}")',
    # Get the session with ID
    'session=fw.get_session(f"{init_session.id}")',

    # Find session from initial subject object
    'session=init_subject.sessions.find(f"label={seslabel}")',
    # Find session from initial project, providing initial subject label
    'session=init_project.sessions.find(f"label={seslabel},subject.label={sublabel}")',
    # Find session from initial project, providing initial subject ID
    'session=init_project.sessions.find(f"label={seslabel},parents.subject={init_subject.id}")',


    # Core Client calls
    # Search all sessions with subject and project label
    'session=core_client.get(f"/api/sessions", params={"filter":f"label={seslabel},subject.label={sublabel},project.label={prjlabel}","limit":1})',
    'session=core_client.get(f"/api/sessions", params={"filter":f"label={seslabel},subject.label={sublabel}","limit":1})',
    'session=core_client.get(f"/api/sessions", params={"filter":f"label={seslabel},project.label={prjlabel}","limit":1})',

    # Search all session with subject and project ID
    'session=core_client.get(f"/api/sessions", params={"filter":f"label={seslabel},parents.subject={init_subject.id},parent.project={init_project.id}","limit":1})',

    # Search all sessions in the project given a subject label
    'session=core_client.get(f"/api/projects/{init_project.id}/sessions", params={"filter":f"label={seslabel},subject.label={sublabel}","limit":1})',
    # Search all session in the project given a subject ID
    'session=core_client.get(f"/api/projects/{init_project.id}/sessions", params={"filter":f"label={seslabel},parents.subject={init_subject.id}","limit":1})',

    # Search all session in a subject
    'session=core_client.get(f"/api/subjects/{init_subject.id}/sessions", params={"filter":f"label={seslabel}","limit":1})',

    # Repeat above with limit 2

    # Core Client calls
    # Search all sessions with subject and project label
    'session=core_client.get(f"/api/sessions", params={"filter":f"label={seslabel},subject.label={sublabel},project.label={prjlabel}","limit":2})',
    'session=core_client.get(f"/api/sessions", params={"filter":f"label={seslabel},subject.label={sublabel},project.label={prjlabel}","limit":200})',

    # Search all session with subject and project ID
    'session=core_client.get(f"/api/sessions", params={"filter":f"label={seslabel},parents.subject={init_subject.id},parent.project={init_project.id}","limit":2})',

    # Search all sessions in the project given a subject label
    'session=core_client.get(f"/api/projects/{init_project.id}/sessions", params={"filter":f"label={seslabel},subject.label={sublabel}","limit":2})',
    'session=core_client.get(f"/api/projects/{init_project.id}/sessions", params={"filter":f"label={seslabel},subject.label={sublabel}","limit":200})',

    # Search all session in the project given a subject ID
    'session=core_client.get(f"/api/projects/{init_project.id}/sessions", params={"filter":f"label={seslabel},parents.subject={init_subject.id}","limit":2})',

    # Search all session in a subject
    'session=core_client.get(f"/api/subjects/{init_subject.id}/sessions", params={"filter":f"label={seslabel}","limit":2})',

    #######################
    ## Acquisition Calls ##
    #######################
    # Find acquisition given project, subject, session label
    'acquisition=fw.acquisitions.find(f"label={acqlabel},project.label={prjlabel},subject.label={sublabel},session.label={seslabel}")',
    # Find acquisition given IDs
    'acquisition=fw.acquisitions.find(f"label={acqlabel},parents.project={init_project.id},parents.subject={init_subject.id},parents.session={init_session.id}")',
    # Find from session:
    'acquisition=init_session.acquisitions.find(f"label={acqlabel}")',

    # Core Client Calls
    # Search all acquisitions given proj,sub,ses label
    'acquisition=core_client.get(f"/api/acquisitions",params={"filter":f"label={acqlabel},project.label={prjlabel},subject.label={sublabel},session.label={seslabel}","limit":1})',
    'acquisition=core_client.get(f"/api/acquisitions",params={"filter":f"label={acqlabel},subject.label={sublabel},session.label={seslabel}","limit":1})',
    'acquisition=core_client.get(f"/api/acquisitions",params={"filter":f"label={acqlabel},project.label={prjlabel},subject.label={sublabel}","limit":1})',

    # Search all acquisitions given proj,sub,ses id
    'acquisition=core_client.get(f"/api/acquisitions",params={"filter":f"label={acqlabel},parents.project={init_project.id},parents.subject={init_subject.id},parents.session={init_session.id}","limit":1})',

    # Search project for acquisitions given sub,ses label
    'acquisition=core_client.get(f"/api/projects/{init_project.id}/acquisitions",params={"filter":f"label={acqlabel},subject.label={sublabel},session.label={seslabel}","limit":1})',
    # Search session for acquisition given acq label
    'acquisition=core_client.get(f"/api/sessions/{init_session.id}/acquisitions",params={"filter":f"label={acqlabel}","limit":1})',

    # Repeat with limit 2
    # Core Client Calls
    # Search all acquisitions given proj,sub,ses label
    'acquisition=core_client.get(f"/api/acquisitions",params={"filter":f"label={acqlabel},project.label={prjlabel},subject.label={sublabel},session.label={seslabel}","limit":2})',

    # Search all acquisitions given proj,sub,ses id
    'acquisition=core_client.get(f"/api/acquisitions",params={"filter":f"label={acqlabel},parents.project={init_project.id},parents.subject={init_subject.id},parents.session={init_session.id}","limit":2})',

    # Search project for acquisitions given sub,ses label
    'acquisition=core_client.get(f"/api/projects/{init_project.id}/acquisitions",params={"filter":f"label={acqlabel},subject.label={sublabel},session.label={seslabel}","limit":2})',
    'acquisition=core_client.get(f"/api/projects/{init_project.id}/acquisitions",params={"filter":f"label={acqlabel},subject.label={sublabel},session.label={seslabel}","limit":200})',

    # Search session for acquisition given acq label
    'acquisition=core_client.get(f"/api/sessions/{init_session.id}/acquisitions",params={"filter":f"label={acqlabel}","limit":2})',

]