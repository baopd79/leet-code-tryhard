---
tags: [moc, ]
created: 2026-05-04
last_reviewed: 2026-05-04
---

# MOC - MOC_Template

<!-- 
MOC = Map of Content. "Trang chủ" của 1 chủ đề lớn.
1 chỗ duy nhất nhìn thấy TẤT CẢ note liên quan + status.
KHÔNG viết nội dung ở đây — chỉ link + 1 câu hint.

Status emoji:
- ✅ Done
- 🚧 Đang làm
- ⏸️ Chưa làm
-->

## Tổng quan

<!-- 1-2 câu mô tả chủ đề này. Định vị nó trong knowledge graph. -->

## Concepts

<!-- 
Khái niệm nền tảng. Sắp xếp từ cơ bản → nâng cao.
Format: STATUS [[Tên note]] — 1 câu hint.
-->

### Cơ bản

- ⏸️ [[ ]] — 
- ⏸️ [[ ]] — 

### Nâng cao

- ⏸️ [[ ]] — 
- ⏸️ [[ ]] — 

## Best Practices / Patterns

<!-- 
Cách giải quyết vấn đề điển hình trong domain này.
Có thể bỏ section nếu topic không có pattern.
-->

- ⏸️ [[ ]] — 

## Interview

### Concept questions

- ⏸️ [[Q - ]] — 
- ⏸️ [[Q - ]] — 

### Scenario questions

- ⏸️ [[S - ]] — 
- ⏸️ [[S - ]] — 

## Resources tổng hợp

<!-- Source học chính thống cho topic này -->

- 
- 

## Auto-list (Dataview)

<!-- 
Tự động liệt kê toàn bộ note theo tag.
Cập nhật real-time khi thêm note mới.
Tách 3 query theo loại để dễ scan.
-->

### Concepts
```dataview
TABLE difficulty, interview_freq, status
FROM #concept AND #
SORT file.name ASC
```

### Concept Questions
```dataview
TABLE difficulty, interview_freq, confidence
FROM #concept-question AND #
SORT confidence ASC, file.name ASC
```

### Scenario Questions
```dataview
TABLE difficulty, interview_freq, confidence
FROM #scenario-question AND #
SORT confidence ASC, file.name ASC
```
