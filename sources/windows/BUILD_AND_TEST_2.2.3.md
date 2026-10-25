# Build and test LUFScale 2.2.3 for Windows

1. Extract the entire ZIP into a new local folder. Do not overlay an old build directory.
2. Open `Create_Offline_Installer_Windows.cmd` from the extracted folder. An Internet connection is required to prepare the pinned build tools and dependencies.
3. Wait for completion. Full build logs are stored in `build-logs`.
4. Test the outputs in `dist`. Confirm version 2.2.3 and open Help after switching application languages. All twelve approved PDF guides are included; their content and layout are retained with version references updated to 2.2.3.
5. Run the native checks listed in `VALIDATION_2.2.3.md`.

## Files to return after testing

- `dist/LUFScale-2.2.3-Setup-x64.exe` and its `.sha256` file.
- `dist/LUFScale-2.2.3-Portable-x64.exe` and its `.sha256` file.

The `dist/LUFScale` folder is the unpacked application used to make Setup; it is not the source/build kit and is not an additional website download.

If construction fails, return the relevant `build-logs` files. No GitHub or website upload is needed during testing.
