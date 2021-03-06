"""ConfigurationPolicy class"""

from .halo_endpoint import HaloEndpoint


class ConfigurationPolicy(HaloEndpoint):
    """ConfigurationPolicy class:

    The list_all() method allows filtering by using keyword arguments. An
    exhaustive list of keyword arguments can be found at
    https://api-doc.cloudpassage.com/help#list-configuration-policies


    Args:
        session (:class:`cloudpassage.HaloSession`): This will define how you
            interact with the Halo API, including proxy settings and API keys
            used for authentication.

    """

    object_name = "policy"
    objects_name = "policies"

    @classmethod
    def endpoint(cls):
        """Return the endpoint for API requests."""
        return "/v1/%s" % ConfigurationPolicy.objects_name

    @classmethod
    def object_key(cls):
        """Return the key used to pull the policy from the json document."""
        return ConfigurationPolicy.object_name

    @classmethod
    def pagination_key(cls):
        """Return the pagination key for parsing paged results."""
        return ConfigurationPolicy.objects_name
