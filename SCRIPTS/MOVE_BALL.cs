using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BALLMOVE : MonoBehaviour
{
    [SerializeField] GameObject BallSpawnPoint;
    [SerializeField] GameObject Ball;
    public UDPReceive udpr;
    // Start is called before the first frame update
    void Start()
    {
        
    }
    // Update is called once per frame
    void Update()
    {
        string data = udpr.data;
        data=data.Remove(0,1);
        data=data.Remove(data.Length -1,1);
        string[] info = data.Split(',');
        float x=-float.Parse(info[0]);
        float y=float.Parse(info[1]);
        float z=float.Parse(info[2]);
        gameObject.transform.localPosition=new Vector3(x,-5,-1);
        // x=4*x;
        // gameObject.transform.Rotate(0,x,0,Space.Self);
        // gameObject.transform.RotateAround(transform.position, transform.up, Time.deltaTime * 90f);
        if(z==1)
        {
            Instantiate(Ball,BallSpawnPoint.transform.position,BallSpawnPoint.transform.rotation);
        }
        if(y==1){
            transform.rotation=Quaternion.Euler(0,4*x,0);
        }
        if(y==2){
            transform.rotation=Quaternion.Euler(-10,4*x,0);
        }
        if(y==3){
            transform.rotation=Quaternion.Euler(-20,4*x,0);
        }

    }
}