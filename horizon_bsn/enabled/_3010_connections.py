# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from openstack_dashboard.settings import STATIC_URL

# The name of the panel to be added to HORIZON_CONFIG. Required.
PANEL = 'connections'

# The name of the dashboard the PANEL associated with. Required.
PANEL_DASHBOARD = 'project'

# The name of the panel group the PANEL associated with. Optional.
PANEL_GROUP = 'network'

# Python panel class of the PANEL to be added.
ADD_PANEL = 'horizon_bsn.content.connections.panel.Connections'

# A list of applications to be prepended to INSTALLED_APPS
# This is commented out, since the app is installed by _3000_connections.py
# ADD_INSTALLED_APPS = ['horizon_bsn']

# Automatically discover static resources in installed apps
AUTO_DISCOVER_STATIC_FILES = True

CONNECTIONS_STATIC_BASE = 'dashboard/project/connections'
CSS_BASE = '%s/css' % CONNECTIONS_STATIC_BASE
PREFIX_URL = '%s/' % STATIC_URL.strip('/')

ADD_SCSS_FILES = [
    PREFIX_URL + '%s/network-template.css' % CSS_BASE,
    PREFIX_URL + '%s/opentip.css' % CSS_BASE,
    PREFIX_URL + '%s/panel-settings.css' % CSS_BASE]
