meta:
  id: rsv
  file-extension: rsv
  endian: le
seq:
  - id: version
    type: u4
  - id: region
    type: region
    size-eos: true
types:
  region:
    seq:
      - id: file_size
        type: u4
        valid: _io.size
      - id: magic
        size: 4
        contents: .rsv
      - id: position
        type: position
      - id: locations_offset
        type: u4
      - id: locations_size
        type: u4
      - id: chunks_offset
        type: u4
      - id: chunks_size
        type: u4
    instances:
      locations:
        type: locations
        size: locations_size
        pos: locations_offset
      chunks_data:
        type: chunks_data
        size: chunks_size
        pos: chunks_offset
  position:
    seq:
      - id: x
        type: s8
      - id: y
        type: s8
  locations:
    seq:
      - id: locations
        type: location
        repeat: eos
  location:
    seq:
      - id: position
        type: position
      - id: offset
        type: u4
      - id: pad
        size: 4
    instances:
      chunk:
        type: chunk
        pos: offset
        io: _root.region.chunks_data._io
  chunks_data:
    seq:
      - id: a
        type: u1
        repeat: eos
  chunk:
    seq:
      - id: chunk_size
        type: u4
      - id: magic
        size: 4
        #contents: chnk
      - 