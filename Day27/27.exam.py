
# < Network >

"""
< 용어 > 
HTTP, DNS, DHCP
TCP, UDP / PORT
IP  / IP


< DNS (Domain Name System) >
- Domain주소를 IP Number 로 변환시켜주는 역할
- ex) www.google.com => IP주소와 Port번호의 결합 (59.18.46.113:80)
- 들어가고자 하는 사이트의 IP 주소를 알려준다. (UDP 방식)

< DHCP (Dynamic Host Configuration Protocol) >
- 동적 호스트 설정 프로토콜 (UDP 방식)
- 네트워크에 유일한 IP주소를 자동으로 할당하고 관리하는 서비스



< HTTP (Hyper Text Transfer Protocol) >
- TCP 방식
TCP 먼저 생성되어야 함. (TCP 사용해서 포장)
생성 되고 SYN - ACK 
(SYN - ACK : 3-way handshake)
(   SYN -> ACK, SYN -> ACK  )

TCP 단계에서
- port 확인
- Sequence Num
- ACK Num


연결 끊을 시
SYN - ACK : close 4-way handshake

흐름제어, 오류제어

"""