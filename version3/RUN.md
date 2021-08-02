1. Download Friday-WorkingHours.pcap. from: http://205.174.165.80/CICDataset/CIC-IDS-2017/Dataset/PCAPs.

2. The DDoS LOIC attack is at (15:56 – 16:16) according to the documentation:  https://www.unb.ca/cic/datasets/ids-2017.html.
So please slice the pcap on this part (considering the timezone (+5 hours)):

```console
editcap -A "2017-07-07 20:55:00" -B "2017-07-07 21:15:00" Friday-WorkingHours.pcap demo.pcap
```

3. run ```tcpreplay``` on the ```editcap``` if we need to replicate the attack scenario on a VM
(```tcpreplay``` makes it more realistic to run attacks and let nprobe monitor a veth on a namespace where tcpreplay is run), 
so please create a namespace and one veth (veth1) is on that side and the other ```veth``` (```veth0```) will be monitored by ```nprobe``` 
in the next step) when you run ```tcpreplay```, it should be something like this:

```console
sudo ip netns exec tcpreplay tcpreplay -i veth1 demo.pcap
```

4. run nprobe on the other side of the ```veth``` (```veth0```) and send it directly to Kafka.

```console
sudo nprobe -T "%IPV4_SRC_ADDR %IPV4_DST_ADDR  %IN_PKTS %IN_BYTES %OUT_PKTS %OUT_BYTES %FLOW_ACTIVE_TIMEOUT %FLOW_INACTIVE_TIMEOUT %L4_SRC_PORT %L4_DST_PORT %TCP_FLAGS %CLIENT_TCP_FLAGS %SERVER_TCP_FLAGS %PROTOCOL %SRC_TOS %LONGEST_FLOW_PKT %SHORTEST_FLOW_PKT %TCP_WIN_MSS_IN %TCP_WIN_MSS_OUT %SRC_TO_DST_SECOND_BYTES %DST_TO_SRC_SECOND_BYTES %LAST_SWITCHED %FIRST_SWITCHED %MIN_IP_PKT_LEN %MAX_IP_PKT_LEN %DIRECTION %FLOW_ID %FLOW_START_SEC %FLOW_END_SEC %DURATION_IN %DURATION_OUT %PAYLOAD_HASH %PROTOCOL_MAP %FLOW_DURATION_MICROSECONDS" -i veth0 --kafka "20.56.232.206:29092;network-data"
```
