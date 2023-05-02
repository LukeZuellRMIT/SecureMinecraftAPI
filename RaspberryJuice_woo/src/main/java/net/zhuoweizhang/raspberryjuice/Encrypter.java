package net.zhuoweizhang.raspberryjuice;

import java.io.*;
import java.nio.charset.StandardCharsets;

public class Encrypter {
    Process mProcess;
    public static final String PYTHON_PATH = "StartingOver/script_python.py";

    public void runScript() {
        Process process;
        try {
            process = Runtime.getRuntime().exec(new String[] { PYTHON_PATH, "arg1", "arg2" });
            mProcess = process;
        } catch (Exception e) {
            System.out.println("Exception Raised" + e.toString());
        }
        InputStream stdout = mProcess.getInputStream();
        BufferedReader reader = new BufferedReader(new InputStreamReader(stdout, StandardCharsets.UTF_8));
        String line;
        try {
            while ((line = reader.readLine()) != null) {
                System.out.println("stdout: " + line);
            }
        } catch (IOException e) {
            System.out.println("Exception in reading output" + e.toString());
        }
    }
}

class Solution {
    public static void main(String[] args) {
        // chmod permissions
        File file = new File("StartingOver/script_python.py");
        file.setWritable(true);
        file.setReadable(true);
        file.setExecutable(true);

        Encrypter scriptPython = new Encrypter();
        scriptPython.runScript();
    }

}