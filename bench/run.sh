docker run \
    --rm \
    --read-only \
    --network none \
    --memory 500M \
    --cpus 2.0 \
    --user 1000:1000 \
    --env HOME=/jail \
    --env TMPDIR=/jail \
    --workdir /jail \
    --tmpfs /jail:size=100M,noatime,exec,nodev,nosuid,uid=1000,gid=1000,nr_inodes=5k,mode=1700 \
    --volume <repertoire physique>:/jail/student:ro \
    --env EXERCISE=<ExersiceName> \
    --env USERNAME=<username> \
    <image-docker>
