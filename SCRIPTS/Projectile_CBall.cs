using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;

public class BallRED : MonoBehaviour
{
    [SerializeField] float force = 100f;
    Rigidbody rb;
    void Start() {
        rb = GetComponent<Rigidbody>();
        rb.AddForce(transform.forward * force, ForceMode.Impulse);
        System.Threading.Thread.Sleep(100);
    }
}
