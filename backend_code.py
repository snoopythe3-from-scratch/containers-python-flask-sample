import scratchattach as sa
server = sa.init_cloud_server(
    '192.168.0.99', 8080, # set IP address and port
    thread=True, # if set to True, the server will run in a thread
    length_limit=None, allow_non_numeric=True, # customize what cloud values are allowed
    whitelisted_projects=None, allow_nonscratch_names=True, blocked_ips=[],
    sync_players=True, # when set to False, other players will no longer be notified about cloud updates (only the server will see and parse them)
    log_var_sets=False # when set to True, all var sets will be printed to the console (can be spammy)
)
server.start()
