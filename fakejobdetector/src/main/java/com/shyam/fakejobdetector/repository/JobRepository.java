package com.shyam.fakejobdetector.repository;

import com.shyam.fakejobdetector.model.JobListing;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface JobRepository extends JpaRepository<JobListing, Long> {
}
