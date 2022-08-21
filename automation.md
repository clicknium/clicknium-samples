![background](img/logo.png)

[Clicknium](https://www.clicknium.com/) provides the automation technology in a variety of scenarios with different forms, such as SAP automation, Java automation, Windows desktop automation and image automation. Let's discuss about the automation technology that underlies.

# Introduction

Regarding software automation technology, it was mainly used for software testing in the very begining, especially for UI automation testing. Many system software designs take the accessibility to the disabled users into account. See [windows accessibility](https://www.microsoft.com/en-us/accessibility/?rtc=1). In recent years, RPA (Robotic Process Automation) has been accepted by more and more enterprises. RPA plays a great role in multiple business field scenarios to optimize the process, reduce costs and increase efficiency, and quickly improve the level of the informatization. RPA products generally include automated operation components for various softwares, data processing components, process logic control components, etc., among which UI automation components are the mostly used.

# Windows UI Automation Technology

Windows applications include a functional design: Accessibility, which allows more users to operate the softwares. For example, allow the the blind users to read the screen through the voice, and etc. The UI automation technology provided by Microsoft can access the control elements of the windows application. The main technologies are as follows:
- UIA (UI Automation) 
UI Automation provides programmatic access to information about the user interface (UI) for Microsoft windows, enabling assistive technology products (such as screen readers) to provide information about the UI to end users using means other than standard input and Manipulate UI. UI Automation also enables automated test scripts to interact with the UI.
- MSAA（Microsoft Active Accessibility）
Microsoft Active Accessibility was the application accessibility solution from Microsoft earlier. 

UIA is the new accessibility model for Microsoft Windows, offering more improvements than MSAA.

||UIA|MSAA|
|--------|---------|-------|
|Programing Languages| written in managed code, client applications are most easily programmed using C# | based on the Component Object Model (COM) with support for dual interfaces.|
|Windows Presentation Foundation|full support |WPF do not contain native support for MSAA|
|Servers and Clients|a core service between the server (called a provider) and the client, providing more information to the client|servers and clients communicate directly, largely through the server's implementation of IAccessible|
|Security|UIA removes the need of providers to call through to other provider code. The UI Automation core service does all the necessary aggregation.|Some IAccessible customization scenarios require wrapping a base IAccessible and calling through to it. There is a potential security risk, since a partially trusted component should not be an intermediary on a code path.|

If you are interested in Windows automation technology, you can directly go to [Microsoft's official technical documentation](https://docs.microsoft.com/zh-CN/dotnet/framework/ui-automation/ui-automation-overview).

# Java Access Bridge (JAB)
Java Access Bridge is a technology that exposes the Java Accessibility API in a Microsoft Windows DLL, enabling Java applications and applets that implement the Java Accessibility API to be visible to assistive technologies on Microsoft Windows systems. Java Accessibility API is part of Java Accessibility Utilities, which is a set of utility classes that help assistive technologies provide access to GUI toolkits that implement the Java Accessibility API.
Here is the architecture of Java Access Bridge from oracle official site:

![jab architecture](img/jab-block-diagram.gif)

To learn more about JAB, please visit [oracle](https://docs.oracle.com/javase/8/docs/technotes/guides/access/jab/introduction.html#jab-overview)

# Web Automation
Web automation mainly depends on the type of browsers, and currently there are two main categories:

## Internet Explorer(IE)  

Through javascript injection based on the Component Object Model (COM).  
Due to different versions of IE, it is still a technical difficulty of making multiple versions of IE compatible.

## Chromium-based browsers

There are generally three ways:
- Selenium webdriver

To learm more about webdriver, please visit [WebDriver](https://w3c.github.io/webdriver/), [Chrome webdriver](https://chromedriver.chromium.org/).

- Chrome devtool protocol(CDP)

As CDP is used in many tools, you can refer to [awesome-chrome-devtools](https://github.com/ChromeDevTools/awesome-chrome-devtools).
Related to web automation testing, they are Puppeteer and Playwright.
The playwright python code start the Chrome browser is as below:
```python
browser = p.chromium.launch(channel="chrome", headless=False)
context = browser.new_context()
# Open new page
page = context.new_page()
# Go to https://www.google.com/
page.goto("https://www.google.com/")
```
With ProcessExplorer, you can see that Chrome starts the parameters as follows.
```
"C:\Program Files\Google\Chrome\Application\chrome.exe" --disable-background-networking --enable-features=NetworkService,NetworkServiceInProcess --disable-background-timer-throttling --disable-backgrounding-occluded-windows --disable-breakpad --disable-client-side-phishing-detection --disable-component-extensions-with-background-pages --disable-default-apps --disable-dev-shm-usage --disable-extensions --disable-features=ImprovedCookieControls,LazyFrameLoading,GlobalMediaControls,DestroyProfileOnBrowserClose,MediaRouter,AcceptCHFrame,AutoExpandDetailsElement --allow-pre-commit-input --disable-hang-monitor --disable-ipc-flooding-protection --disable-popup-blocking --disable-prompt-on-repost --disable-renderer-backgrounding --disable-sync --force-color-profile=srgb --metrics-recording-only --no-first-run --enable-automation --password-store=basic --use-mock-keychain --no-service-autorun --export-tagged-pdf --no-sandbox --user-data-dir=C:\Users\test\AppData\Local\Temp\playwright_chromiumdev_profile-V3LZUg **--remote-debugging-pipe** --no-startup-window
```
According to the chrome startup parameter description:
```
--remote-debugging-pipe: Enables remote debug over stdio pipes [in=3, out=4]. Optionally, specifies the format for the protocol messages, can be either "JSON" (the default) or "CBOR"
```

For the way to use CDP, you can get started from [this link](https://github.com/aslushnikov/getting-started-with-cdp/blob/master/README.md).
More crhome startup parameters can be found in the official documentation, or [here](https://github.com/GoogleChrome/chrome-launcher/blob/master/docs/chrome-flags-for-tools.md).
- Native messaging
Extensions and apps can exchange messages with native applications by an API similar to the other  [message passing APIs](https://developer.chrome.com/docs/apps/nativeMessaging/messaging). Native applications that support this feature must register a native messaging host knowing how to communicate with the extension. Chrome starts the host in a separate process and communicates with it using standard input and standard output streams.

More about Native Messaging, please visit [this link](https://developer.chrome.com/docs/apps/nativeMessaging/messaging).

#  SAP Automation
As SAP provides the script automation by itself, most RPA products automate SAP applications based on its own automation technology.

- Automated supplementary technology
In addition to the above native automation technologies, the following automation technologies are generally used in achieving the hybrid automation.
  - Image recognition, shortcut keys
  - OCR
  - Screen word picking
  - computer vision
  - Windows Native API

# What Clicknium Do
With the automation technologies above, Clicknium offers development tools that allow users to: 
- Capture UI elements and store them as locators or selectors.
- Automate all kinds of applications with a single Python API.
- Higher efficiency in writing code with locator IntelliSense.

In addition to the automation technologies above, Clicknium also performs other enhancements: 
- Combine various automation technologies to increase the robustness.
- Find the UI component with a fast searching algorithm.
- Algorithm for generating locators.
- ... ...

You can visit [Clicknium Visual Studio Code Extension change log](https://marketplace.visualstudio.com/items/ClickCorp.clicknium/changelog) to see more functions.