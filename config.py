class Config(object):
    # In a production app, store this instead in KeyVault or an environment variable
    CLIENT_SECRET = ".LH~15_WLQAD~FrVnItN4Y-6_89XW.eM3x" 

    AUTHORITY = "https://login.microsoftonline.com/mavrogiannischristosoutlook.onmicrosoft.com" 
    CLIENT_ID = "4fe3ab6c-9ae2-41a5-9e84-4c885622432c"

    # TODO: Enter the redirect path you want to use for OAuth requests
    #   Note that this will be the end of the URI entered back in Azure AD
    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL, 
        # which must match your app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"]

    SESSION_TYPE = "filesystem"  # So token cache will be stored in server-side session