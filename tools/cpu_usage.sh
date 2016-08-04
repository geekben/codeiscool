#!/bin/bash
# get <pid>'s cpu usage from /proc

function cpu_usage_pid() {
        if [ -z $1 ];then
                echo "Invalid argument: need <pid>!"
                exit -1
        else
                pid=$1
        fi
        if [ -z $2 ];then
                interval=10
        else
                interval=$2
        fi


        cpu1=`head -1 /proc/stat | awk '{for(i=2;i<=NF;i++) sum+=$i; print sum;}'`
        pid1=`cat /proc/$pid/stat | awk '{print $14+$15+$16+$17}'`
        sleep $interval
        cpu2=`head -1 /proc/stat | awk '{for(i=2;i<=NF;i++) sum+=$i; print sum;}'`
        pid2=`cat /proc/$pid/stat | awk '{print $14+$15+$16+$17}'`

        cpu_num=`cat /proc/cpuinfo | grep processor | wc -l  | awk '{print $1}'`

        echo $((100*$cpu_num*($pid2-$pid1)/($cpu2-$cpu1)))

}

#cpu_usage_pid 15479 10
