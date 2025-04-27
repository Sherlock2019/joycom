
#define MyAppName "FlightCommander"
#define MyAppVersion "1.0"
#define MyAppPublisher "YourName"
#define MyAppExeName "FlightCommander.exe"

[Setup]
AppId={{5E6214C2-CE0F-4DF3-9B93-F3C80E5483E1}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
OutputBaseFilename=FlightCommander_Setup
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "profiles\*"; DestDir: "{app}\profiles"; Flags: ignoreversion recursesubdirs
Source: "README.md"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{commondesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Create a &desktop icon"; GroupDescription: "Additional icons:"
