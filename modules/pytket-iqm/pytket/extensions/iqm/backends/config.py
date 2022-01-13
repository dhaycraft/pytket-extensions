# Copyright 2020-2022 Cambridge Quantum Computing
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""IQM config."""

from typing import Any, Dict, Optional, Type, ClassVar
from dataclasses import dataclass
from pytket.config import PytketExtConfig


@dataclass
class IQMConfig(PytketExtConfig):
    """Holds config parameters for pytket-iqm."""

    ext_dict_key: ClassVar[str] = "iqm"

    username: Optional[str]

    api_key: Optional[str]

    @classmethod
    def from_extension_dict(
        cls: Type["IQMConfig"], ext_dict: Dict[str, Any]
    ) -> "IQMConfig":
        return cls(ext_dict.get("username", None), ext_dict.get("api_key", None))


def set_iqm_config(
    username: Optional[str] = None,
    api_key: Optional[str] = None,
) -> None:
    """Set default value for IQM API token."""
    config = IQMConfig.from_default_config_file()
    if username is not None:
        config.username = username
    if api_key is not None:
        config.api_key = api_key
    config.update_default_config_file()
