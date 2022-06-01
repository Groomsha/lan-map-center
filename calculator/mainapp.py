#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#

"""
Project Name: 'ip-calculator'
Version: 0.1
Description: App for calculating masks and subnets
Ihor Cheberiak (c) 2021
https://www.linkedin.com/in/ihor-cheberiak/
"""

import argparse

from bash_sources.main_bash_application import MainBashApplication

help_parser = argparse.ArgumentParser(description="The script for calculating masks and subnets 'IP Calculator'")
help_parser.add_argument("-b", '--bush', type=str, default="-bash", help="Bash IP Calculator")

args_parser = help_parser.parse_args()


if __name__ == '__main__':
	if args_parser.bush:
		bash_calc = MainBashApplication()
	else:
		pass