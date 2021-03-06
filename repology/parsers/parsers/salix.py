# Copyright (C) 2019 Dmitry Marakasov <amdmi3@amdmi3.ru>
#
# This file is part of repology
#
# repology is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# repology is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with repology.  If not, see <http://www.gnu.org/licenses/>.

from typing import Generator

from jsonslicer import JsonSlicer

from repology.packagemaker import PackageFactory, PackageMaker
from repology.parsers import Parser
from repology.transformer import PackageTransformer


class SalixPackagesJsonParser(Parser):
    def iter_parse(self, path: str, factory: PackageFactory, transformer: PackageTransformer) -> Generator[PackageMaker, None, None]:
        with open(path, 'rb') as jsonfile:
            for item in JsonSlicer(jsonfile, ('packages', None)):
                with factory.begin() as pkg:
                    pkg.set_name(item['name'])
                    pkg.set_version(item['ver'])
                    pkg.set_summary(item['descs'])
                    pkg.set_arch(item['arch'])

                    pkg.set_extra_field('location', item['loc'])

                    yield pkg
