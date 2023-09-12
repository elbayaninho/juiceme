import { Configuration, LogLevel } from "@azure/msal-browser";

export const msalConfiguration: Configuration = {
    auth: {
        clientId: "a126fcf5-bbce-4a16-bf19-c4b93c3490ec",
        redirectUri: "http://localhost:5173/redirect"
    },
    cache: {
        cacheLocation: "sessionStorage", // This configures where your cache will be stored
        storeAuthStateInCookie: false, // Set this to "true" if you are having issues on IE11 or Edge
    },
    system: {
        loggerOptions: {
            loggerCallback: (level, message, containsPii) => {
                if (containsPii) {
                    return;
                }
                switch (level) {
                    case LogLevel.Error:
                        console.error(message);
                        return;
                    case LogLevel.Info:
                        console.info(message);
                        return;
                    case LogLevel.Verbose:
                        console.debug(message);
                        return;
                    case LogLevel.Warning:
                        console.warn(message);
                        return;
                    default:
                        return;
                }
            }
        }
    }
};

export const loginRequest = {
    scopes: ["api://e1560700-bd97-4cf1-a39a-dcb795cae5cb/access_as_user"]
};