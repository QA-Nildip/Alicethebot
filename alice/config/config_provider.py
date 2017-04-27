import os
from alice.helper.common_utils import getDictFromJson
from alice.helper.log_utils import LOG


class ConfigProvider(object):
    # __metaclass__ = SingletonMetaClass

    def __init__(self, repo):
        config_file = os.environ["config"]
        LOG.info("config file=" + config_file)
        #self.config = CommonUtils.readResourceJson(__name__, config_file) #relative package path
        self.config = getDictFromJson(config_file) #absolute path to keep file anywhere
        self.repo_name = repo

    def __str__(self):
        return "Alice - Common Config Provider"

    @property
    def organisation(self):
        return self.config.get('organisation')

    @property
    def githubToken(self):
        return self.config.get('tokens').get("github")

    @property
    def slackToken(self):
        return self.config.get('tokens').get("slack")

    @property
    def is_debug(self):
        return self.config.get("debug", False)

    @property
    def repo(self):
        return self.config.get("repo").get(self.repo_name, {})


    @property
    def sensitiveBranches(self):
        return self.repo.get('sensitive_branches')

    @property
    def sensitiveFiles(self):
        return self.repo.get("sensitive_files")

    @property
    def branchListToBeNotifiedFor(self):
        return self.repo.get('notify_direct', {}).get('branch_list_to_be_notified')

    @property
    def actionToBeNotifiedFor(self):
        return self.repo.get('notify_direct', {}).get('action_to_be_notified_on', "opened")

    @property
    def whiteListedMembers(self):
        return self.repo.get('whitelisted_git_members')

    @property
    def superMembers(self):
        return self.repo.get('super_git_members')

    @property
    def mainBranch(self):
        return self.repo.get('main_branch')

    @property
    def testBranch(self):
        return self.repo.get('test_branch')

    @property
    def debug_folks(self):
        return self.config.get('debug_alice', {}).get('debug_folks')

    @property
    def debug_channel(self):
        return self.config.get('debug_alice', {}).get('debug_channel')

    @property
    def alertChannelName(self):
        if self.is_debug:
            return self.debug_channel
        return self.config.get("repo").get(self.repo_name, {}).get('alert_channel')

    @property
    def codeChannelName(self):
        if is_debug:
            return self.debug_channel
        return self.repo.get('code_channel')

    @property
    def personToBeNotified(self):
        if self.config.get("debug"):
            return self.debug_folks
        return self.repo.get('notify_direct', {}).get('person_to_be_notified')

    @property
    def techLeadsToBeNotified(self):
        if self.config.get("debug"):
            return self.debug_folks
        return self.repo.get('notify_direct', {}).get('tech_leads_to_be_notified')

    @property
    def productPlusRequiredDirPattern(self):
        return self.repo.get('product_plus_required_dir_pattern')

    @property
    def devOpsTeam(self):
        if self.config.get("debug"):
            return self.debug_folks
        return self.repo.get("dev_ops_team", [])

    @property
    def checks(self):
        return self.repo.get("checks",[])


    def getSlackName(self, github_name):
        return self.config.get('user_map',{}).get(github_name, github_name)






