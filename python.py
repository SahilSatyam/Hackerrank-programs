"""
UPDATE RETN_REM_JIRA_INFO
SET INGS_PROC_EXEC_ID= 1, APPL_SYS_ID= 24039, ISSUE_KEY='N/A', ISSUE_SUM_TX='N/A', ISSUE_DESC_TXT='N/A', ISSUE_URL_TXT='N/A', ISSUE_CREATED_CD='N/A', CRE_TS='20-JUN-24 01.00.00.000000000 AM UTC'
WHERE APPL_SYS_ID = 24039;
"""

new_issue_created = {
        'INGS_PROC_EXEC_ID': get_exec_id(),
        'APPL_SYS_ID': app_id,
        'ISSUE_KEY': fetch_issue_details["issue_key"],
        'ISSUE_SUM_TX': fetch_issue_details["issue_summary"],
        'ISSUE_DESC_TXT': fetch_issue_details["issue_description"].replace("'",""),
        'ISSUE_CREATED_CD': 'Yes',
        'ISSUE_URL_TXT': 'https://jiradc-ccb-cluster02.prod.aws.jpmchase.net/browse/{0}'.format(fetch_issue_details["issue_key"]),
        'CRE_TS': get_cre_ts()
    }

update_record_after_jira_creation = "UPDATE {tablename} SET " .format(
    tablename='ICE_GOS.RETN_REM_JIRA_INFO',
    columns=', '.join(new_issue_created.keys()),
    values=tuple(new_issue_created.values())
    )
