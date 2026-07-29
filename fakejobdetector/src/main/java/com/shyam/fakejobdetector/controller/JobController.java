package com.shyam.fakejobdetector.controller;

import com.shyam.fakejobdetector.service.JobService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import java.util.Map;
import java.util.HashMap;

@RestController
@RequestMapping("/api/job")
@CrossOrigin(origins = "*")
public class JobController {

    @Autowired
    private JobService jobService;

    @PostMapping("/analyze")
    public Map<String, String> analyzeJob(@RequestBody Map<String, String> request) {
        String description = request.get("description");
        String result = jobService.analyzeJob(description);
        Map<String, String> response = new HashMap<>();
        response.put("result", result);
        return response;
    }
}