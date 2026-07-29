package com.shyam.fakejobdetector.service;

import com.shyam.fakejobdetector.model.JobListing;
import com.shyam.fakejobdetector.repository.JobRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;
import org.springframework.http.*;
import java.util.Map;
import java.util.HashMap;

@Service
public class JobService {

    @Autowired
    private JobRepository jobRepository;

    private final String FLASK_URL = "https://fakejobdetector-fa3d.onrender.com";

    public String analyzeJob(String description) {
        // call Flask API
        RestTemplate restTemplate = new RestTemplate();
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);

        Map<String, String> body = new HashMap<>();
        body.put("text", description);

        HttpEntity<Map<String, String>> request = new HttpEntity<>(body, headers);
        ResponseEntity<Map> response = restTemplate.postForEntity(FLASK_URL, request, Map.class);

        String result = (String) response.getBody().get("result");

        // save to database
        JobListing listing = new JobListing();
        listing.setDescription(description);
        listing.setResult(result);
        jobRepository.save(listing);

        return result;
    }
}