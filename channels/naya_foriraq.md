<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/QMVulSDysSn5NG_2fcnDz8fthwrr1Ksg613eJxavvaiK6z97jfa0HuMH3gbkxSrtCYjuDEsrduQRTtCDNNtnlNXvxnwKV2i7DVM3_CE3CFEMHVp1-gRzmbfDvWzQ8_rmhwGbKsQDjD8OKY8RUy0iWvVNrZdQZcKh4KJFwb_L662vjLesXWeZ3S7WUtf0rXdppzOXNEtHPZYRbF3eeapvK1BBKimpURY6vXOqTDkj6OT2OzAtkZzW90UYuORjHjYD4Kh8ANiWLpNdG_YpeSdj2d7lQS44W3K9SWcpOHgp-Dj8mL4s_YrM1dtyH0QuRdNT_N8RvPDRTlXjo-InxQFj2w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 254K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-24 19:09:59</div>
<hr>

<div class="tg-post" id="msg-75380">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">رئيس مجلس النواب يدعو رئيس مجلس الوزراء علي فالح الزيدي والوزراء المصوت عليهم لأداء اليمين الدستورية</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/naya_foriraq/75380" target="_blank">📅 19:04 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75379">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5223d3a624.mp4?token=t_aRgHP2CcyjBHfxJsNZ_M4kJQ4vfFZYqX0HdVEwSWr7OiVcRh_s9bgtqpIO7Ag1JLw6wZKEQgeGRdboqkOvSg6qFd__-aLouqjCBlTm7CcP2fVhTr43gYTmA5znuN0sJLuUvWSMyz2mmy3Pl8aM41BYWzg1FsDjNFN8FYApAmjNF9_Aav8zj1XviX9suZFXQf1SQDGXIHVhz677YSn77DPKunhJimVfwi7M6IAR66YjejfuCGbANgxDYhFvRHAg0FNNvwKEkmMFjc0vCa8FzZz7lumwUCLPSutd8HH5hEaL_BSSI0oArGb0l4h7LHFpzSBaMz1DlPFiEvf7PW4lQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5223d3a624.mp4?token=t_aRgHP2CcyjBHfxJsNZ_M4kJQ4vfFZYqX0HdVEwSWr7OiVcRh_s9bgtqpIO7Ag1JLw6wZKEQgeGRdboqkOvSg6qFd__-aLouqjCBlTm7CcP2fVhTr43gYTmA5znuN0sJLuUvWSMyz2mmy3Pl8aM41BYWzg1FsDjNFN8FYApAmjNF9_Aav8zj1XviX9suZFXQf1SQDGXIHVhz677YSn77DPKunhJimVfwi7M6IAR66YjejfuCGbANgxDYhFvRHAg0FNNvwKEkmMFjc0vCa8FzZz7lumwUCLPSutd8HH5hEaL_BSSI0oArGb0l4h7LHFpzSBaMz1DlPFiEvf7PW4lQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
طيران مسير في سماء العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/naya_foriraq/75379" target="_blank">📅 19:04 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75378">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">توترات بين الأحزاب السنية بشأن الثقة بأحد الأسم المطروحة لإحدى الوزارات.</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/naya_foriraq/75378" target="_blank">📅 19:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75377">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0642dd7275.mp4?token=IyE_Jsm_P7SnXOeZP7S3p8PQnoHUTGh2nmRdcnHKEUEvlW_wGs6-sBZ4Dv2JPiIjQFpHOYoozQZGUFbAIWqosUflN7DqgrpGyx3xYuqZyMRTkv28B-_l9ySDRiwXHmW7DY0iWKfFIZM2B9euMXhPTBcmRChs4wdW15j4CuhsQOmEZzFvShJvFWVJlPuUH2OJnIfcb4O9s3eGpa2tidJ5Vvm2oauBnhiQiPJRd349ea0mg0V80kw1-2mAy05wVE5Z6xvxJ-y4fm8lnCeM1pkYoin4iL5lw9SISJAmot84hUseBrnm1XAkSMZh9nJ1zWTpTaZpfnFI7J6wPgoAcpIeEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0642dd7275.mp4?token=IyE_Jsm_P7SnXOeZP7S3p8PQnoHUTGh2nmRdcnHKEUEvlW_wGs6-sBZ4Dv2JPiIjQFpHOYoozQZGUFbAIWqosUflN7DqgrpGyx3xYuqZyMRTkv28B-_l9ySDRiwXHmW7DY0iWKfFIZM2B9euMXhPTBcmRChs4wdW15j4CuhsQOmEZzFvShJvFWVJlPuUH2OJnIfcb4O9s3eGpa2tidJ5Vvm2oauBnhiQiPJRd349ea0mg0V80kw1-2mAy05wVE5Z6xvxJ-y4fm8lnCeM1pkYoin4iL5lw9SISJAmot84hUseBrnm1XAkSMZh9nJ1zWTpTaZpfnFI7J6wPgoAcpIeEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
خلافات داخل مجلس النواب العراقي خلال طرح اسم لأحدى الوزارت.</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/naya_foriraq/75377" target="_blank">📅 18:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75376">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇶
الوزارات التي تم التصويت عليها من قبل البرلمان العراقي: مجلس النواب يُصوّت بالأغلبية المطلقة على باسم محمد خضير وزيراً للنفط.  مجلس النواب يُصوّت بالأغلبية المطلقة على محمد نوري احمد وزيراً للصناعة.  مجلس النواب يُصوّت بالأغلبية المطلقة على علي سعد وهيب…</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/naya_foriraq/75376" target="_blank">📅 18:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75375">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac7120c31b.mp4?token=KV3FjjoFxMTR7tqUEF87FNIaPzbQDr9pJCSYBVcHk-ukFNkEny9jhNYhqHuNPOb5aENxnSSyad9Fy7xJnKgfKKEV9wJZUpdW6M6jLgEmXESHxoQ_Vnz323YhxLwSNgdGjYpCIE0sIO7Rf4I5YQ3tjL1jR7AmaNP4vRXX9eGUYZtAxqaIeFKpgDs6n7vmqldj_kT_Wpn2p10lp7ubOzJMh2AuPA6qdoM_gb5K5XBt__BQeKr6jLTpYQbzDlxn_B5zy9_THUf7hn9wnkp2DMUz8K5_L2g1YsHUvHhI48Ls06PYWIHk1kbbwojx_2n6Kk8I5TkleMwpSe5d3_es9F31xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac7120c31b.mp4?token=KV3FjjoFxMTR7tqUEF87FNIaPzbQDr9pJCSYBVcHk-ukFNkEny9jhNYhqHuNPOb5aENxnSSyad9Fy7xJnKgfKKEV9wJZUpdW6M6jLgEmXESHxoQ_Vnz323YhxLwSNgdGjYpCIE0sIO7Rf4I5YQ3tjL1jR7AmaNP4vRXX9eGUYZtAxqaIeFKpgDs6n7vmqldj_kT_Wpn2p10lp7ubOzJMh2AuPA6qdoM_gb5K5XBt__BQeKr6jLTpYQbzDlxn_B5zy9_THUf7hn9wnkp2DMUz8K5_L2g1YsHUvHhI48Ls06PYWIHk1kbbwojx_2n6Kk8I5TkleMwpSe5d3_es9F31xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
الوزارات التي تم التصويت عليها من قبل البرلمان العراقي: مجلس النواب يُصوّت بالأغلبية المطلقة على باسم محمد خضير وزيراً للنفط.  مجلس النواب يُصوّت بالأغلبية المطلقة على محمد نوري احمد وزيراً للصناعة.  مجلس النواب يُصوّت بالأغلبية المطلقة على علي سعد وهيب…</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/naya_foriraq/75375" target="_blank">📅 18:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75374">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfa365d566.mp4?token=rohHujM9py4FB0wylZz6kWvU35WgOGzQlXaUHTkWzuH4BPZvAsxTVT96r2kzg3kWPwDzaTuQTRHGd4GprI0MW20D0rpxkbvrC2md8iT-jmKz9NbCbUiOc2mKSoI9EYjcmbWwLlLbgzzQSqZd-3Nsrv_EVktN7CkkBhDmca41pbo4CgyidhA_7n2YnU-7ZPtdkClcD6swgG3buu2ytcIV-yQ6Jty0PQLUUxYb1tRDmhOEWV4ISJp7sZsju03cemtPsEkY2heHNEpTId6X1uApWUvie-q7kGYlP_flXPHCAfhEtxtUe3Hjc198EwjryO46i3nN1UFdkzyTQPyDmGn24g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfa365d566.mp4?token=rohHujM9py4FB0wylZz6kWvU35WgOGzQlXaUHTkWzuH4BPZvAsxTVT96r2kzg3kWPwDzaTuQTRHGd4GprI0MW20D0rpxkbvrC2md8iT-jmKz9NbCbUiOc2mKSoI9EYjcmbWwLlLbgzzQSqZd-3Nsrv_EVktN7CkkBhDmca41pbo4CgyidhA_7n2YnU-7ZPtdkClcD6swgG3buu2ytcIV-yQ6Jty0PQLUUxYb1tRDmhOEWV4ISJp7sZsju03cemtPsEkY2heHNEpTId6X1uApWUvie-q7kGYlP_flXPHCAfhEtxtUe3Hjc198EwjryO46i3nN1UFdkzyTQPyDmGn24g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
الوزارات التي تم التصويت عليها من قبل البرلمان العراقي: مجلس النواب يُصوّت بالأغلبية المطلقة على باسم محمد خضير وزيراً للنفط.  مجلس النواب يُصوّت بالأغلبية المطلقة على محمد نوري احمد وزيراً للصناعة.  مجلس النواب يُصوّت بالأغلبية المطلقة على علي سعد وهيب…</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/naya_foriraq/75374" target="_blank">📅 18:54 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75373">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">استهداف دبابة ميركافا من قبل حزب الله في بلدة الطيبة جنوب لبنان.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/naya_foriraq/75373" target="_blank">📅 18:40 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75372">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مجلس النواب يُصوّت على المنهاج الوزاري لرئيس مجلس الوزراء المكلّف علي فالح الزيدي</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/naya_foriraq/75372" target="_blank">📅 18:38 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75371">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4850c33fc2.mp4?token=vuYLZQJW6eqLie_6apxUzgjWjRCugkTfshW-wOa4u--XxXLHVWjQ_YV26pox46k55CPeaRDzG1U83n80h96HDaSUC0P95UcgoKMBSz1xMlgqBOjF2YK8-L2BsH0Y0WRL5tNMEvRUlmAJIKo44MY4HVeBRcSEg5baMc-w79KxSHwUbU7uoev9Zaei9krvoNb5sUxkL7ykLf9mku1r7-e4EjwfWRkV97f_1kCJLoD-LXeRoemwSu0-AdsDHs2lMxB7r8X-1Z9MHax_Sq6URHuSRfjkqecGhpjnFdAc4YtM0stUCbYL5Prtt58VuxBfyUw5jZ5O9doUJN354kNrWaB52A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4850c33fc2.mp4?token=vuYLZQJW6eqLie_6apxUzgjWjRCugkTfshW-wOa4u--XxXLHVWjQ_YV26pox46k55CPeaRDzG1U83n80h96HDaSUC0P95UcgoKMBSz1xMlgqBOjF2YK8-L2BsH0Y0WRL5tNMEvRUlmAJIKo44MY4HVeBRcSEg5baMc-w79KxSHwUbU7uoev9Zaei9krvoNb5sUxkL7ykLf9mku1r7-e4EjwfWRkV97f_1kCJLoD-LXeRoemwSu0-AdsDHs2lMxB7r8X-1Z9MHax_Sq6URHuSRfjkqecGhpjnFdAc4YtM0stUCbYL5Prtt58VuxBfyUw5jZ5O9doUJN354kNrWaB52A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئيس مجلس الوزراء المكلّف "علي الزيدي" يبدأ قراءة المنهاج الوزاري للتصويت عليه.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/naya_foriraq/75371" target="_blank">📅 18:37 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75370">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8da1de53a6.mp4?token=sdrlQHEGeK4o7mZosI2ntBRGnu9REukj6CRblFA7pT5dMQ6KFzrNbIeNdfp5EkH4KPaRpb2Ahk6kFOVOt-7bJQt6g-uMjPHPh1c3qTSlv__Xq4q_y7plsG3-S33pMMJFAc2YjIxH0usz6h3dofBAOnwV62JtBjG9AxtEIS6K8tlhm-h8f9KT75osIRP6LODxbxUSeEwvOmrfc5gRYzg999GzkTqw6ZZZ943gjhyfJfXTTsscMa6hP_NVVUkRE97G4tiE6O2gjCr1t7DbqIGqK1d3NJEQGQThGdhHY4QiXFtvt79GcP_k439mh6M8tNoeWgV95pMQmRHedBPypJkPvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8da1de53a6.mp4?token=sdrlQHEGeK4o7mZosI2ntBRGnu9REukj6CRblFA7pT5dMQ6KFzrNbIeNdfp5EkH4KPaRpb2Ahk6kFOVOt-7bJQt6g-uMjPHPh1c3qTSlv__Xq4q_y7plsG3-S33pMMJFAc2YjIxH0usz6h3dofBAOnwV62JtBjG9AxtEIS6K8tlhm-h8f9KT75osIRP6LODxbxUSeEwvOmrfc5gRYzg999GzkTqw6ZZZ943gjhyfJfXTTsscMa6hP_NVVUkRE97G4tiE6O2gjCr1t7DbqIGqK1d3NJEQGQThGdhHY4QiXFtvt79GcP_k439mh6M8tNoeWgV95pMQmRHedBPypJkPvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجلس النواب يعقد جلسته للتصويت على المنهاج الوزاري وحكومة علي الزيدي</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/naya_foriraq/75370" target="_blank">📅 18:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75369">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72718a0f45.mp4?token=BhyzkaAbwmR1QESWq7rj2Buzth-G8et0gIZqBSMttyGjrwvvWYSnzW6flRYwcQThdK-G1YGBRdt2HoztY-_YgKpGjc1zWRa02Sm05SrBXm97hR8lLtMJHuphrfGN5733tcQZNGq5x9J8KqCjAMFgjFNOa9BETl0JfvYnxxQ18QWClXB4Q9Sw1CXkRJOZL-DBCBnZ9HC3Rm830g3Uyd7P-xlH9XVLlW4vxyumMqWm0nXOozIhIT3_-6kgqOKZYlDnoSxizVg9W2Qa34RY7LX85y2TN-do5OXCj0r3EIjjqGvR6WdzPmNK24FsLlCZuyuzK2fDqIgTvnF1VJFCQ6zZvb9oQFI9BeieKzgH9DAnhCsZ26JM--9aG9NR2-9eaUXbcZXt7HHN1mtUo_NkQhT_mXnqcy1UhBtVsJT-RqjqT9FB8JEYkgwf35OFYsvRWugixYKaYUVNsDN3sUlwg7nMrGVe7Aw2w40p3qWfFlxgLgkQR_sO1TnHbo698QKo0Zc_mV3OPkwinSIIRp9keD0yBpStEeV72Yq3XFsEli9iPsDMTZ5ewSwGmBHiy4NL22XMjjPUA-htTmIEmtIKa4FhsSOMecH_Rv0h0RFB5HYTzAt1oTXVUQ3Kk0gh3TnwO3eH7_A2IxpMxiPmM_rLFqoTnsTScjJ5SFR97ivUQPSQXZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72718a0f45.mp4?token=BhyzkaAbwmR1QESWq7rj2Buzth-G8et0gIZqBSMttyGjrwvvWYSnzW6flRYwcQThdK-G1YGBRdt2HoztY-_YgKpGjc1zWRa02Sm05SrBXm97hR8lLtMJHuphrfGN5733tcQZNGq5x9J8KqCjAMFgjFNOa9BETl0JfvYnxxQ18QWClXB4Q9Sw1CXkRJOZL-DBCBnZ9HC3Rm830g3Uyd7P-xlH9XVLlW4vxyumMqWm0nXOozIhIT3_-6kgqOKZYlDnoSxizVg9W2Qa34RY7LX85y2TN-do5OXCj0r3EIjjqGvR6WdzPmNK24FsLlCZuyuzK2fDqIgTvnF1VJFCQ6zZvb9oQFI9BeieKzgH9DAnhCsZ26JM--9aG9NR2-9eaUXbcZXt7HHN1mtUo_NkQhT_mXnqcy1UhBtVsJT-RqjqT9FB8JEYkgwf35OFYsvRWugixYKaYUVNsDN3sUlwg7nMrGVe7Aw2w40p3qWfFlxgLgkQR_sO1TnHbo698QKo0Zc_mV3OPkwinSIIRp9keD0yBpStEeV72Yq3XFsEli9iPsDMTZ5ewSwGmBHiy4NL22XMjjPUA-htTmIEmtIKa4FhsSOMecH_Rv0h0RFB5HYTzAt1oTXVUQ3Kk0gh3TnwO3eH7_A2IxpMxiPmM_rLFqoTnsTScjJ5SFR97ivUQPSQXZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هل ناقشت دعم الصين لإيران مع الرئيس الصيني؟
‏ترامب: لقد ناقشنا الأمر. هممم. أعني، عندما تقول "دعم"، فهم لا يخوضون حربًا معنا أو أي شيء من هذا القبيل. قال إنه لن يقدم معدات عسكرية. هذا تصريحٌ كبير. لكن في الوقت نفسه قال إنهم يشترون الكثير من نفطهم من هناك، ويرغبون في الاستمرار في ذلك.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/naya_foriraq/75369" target="_blank">📅 18:22 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75368">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامب: عرض الرئيس الصيني تقديم المساعدة بشأن إيران</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/naya_foriraq/75368" target="_blank">📅 18:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75367">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">قيادات سياسية ورئاسات في مبنى البرلمان قبل انطلاق جلسة منح الثقة لحكومة الزيدي</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/naya_foriraq/75367" target="_blank">📅 18:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75366">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rhrsk4YpLd8FYMwlG3N9sMuXlOgRkFX6ExYMJRVvY4X9sMmQ9cNGnD6LTkZXPaSQ0qnWJA0FZN50Gqgp39MqXeOe30HhXCratPF2w5Cp9Dc_qWMv5YxavpTzLw2VDYDyWeWyJ7ZCdK_2zVjiuzhyTVJovhILuSl60cLBwR00xC8VeukD1BBtTV1Wr1Zsr-IFD0mHu1KcGEos7lc3sLPY6C-m_ZkAHOzlHZNj765lDboYZXIH5fYcSHk339A5HUZC34I5k7VMtXJwyeFlioLJi-EVJWsratuvH8mzsRWUaOJKOxX6yl1f5rS4w-ZmotKyObZ-k3GMIwDlpOEF_jKXhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرع جرس البرلمان إيذاناً ببدء جلسة منح الثقة لحكومة علي الزيدي</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/naya_foriraq/75366" target="_blank">📅 18:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75365">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/piOZ88IsIQgAM7-rZcXSOXGLDAvi6w_mU1FOo0H6MjRJSFlhLHk_AJUew4lSp-NwwPoMXBXQ55ZrSzzh7r6W01GObnBxkHnf_1XO78b4OC_OUySrr85sxHRqfNG-owV5xjrAG6LaPvNpQbme34eGHAxy-ATqYXuH2JzLUl1T_vviEEsmOxg8x93URxupNYDpK425qak3XPdlCH4_mCtMlGse4uP7wrQYjUQ3f5IZeGEWxWZCqQ1MRbjdFow8gTFok_nS_VqQ8aWlEtd1EoVL45Ok0GMlAWt5yB8LpHzXZUAuynovsqynJs9RnWrGlGx7EGAElVcYA0sy5K6C1M8LjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قائد القيادة المركزية الأمريكية:
في الأشهر الثلاثين الماضية فقط قبل بدء عملية الغضب الملحمي، هاجمت جماعات إرهابية مدعومة من إيران القوات والدبلوماسيين الأمريكيين أكثر من 350 مرة - أي ما يعادل هجومًا كل ثلاثة أيام أو أكثر، مما أسفر عن مقتل أربعة من أفراد الخدمة الأمريكية وإصابة ما يقرب من 200 آخرين.</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/naya_foriraq/75365" target="_blank">📅 17:45 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75364">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">القيادات السياسية والرئاسات تتوافد لمجلس النواب العراقي للمشاركة في جلسة منح الثقة لحكومة علي الزيدي</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/naya_foriraq/75364" target="_blank">📅 17:31 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75363">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">فايننشال تايمز:
‏السعودية تطرح معاهدة عدم اعتداء في الشرق الأوسط مع إيران.</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/naya_foriraq/75363" target="_blank">📅 17:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75362">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 13-05-2026 دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في بلدة عيناثا جنوبي لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/naya_foriraq/75362" target="_blank">📅 17:22 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75361">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/km6nyKSTo2weRytQCNoBrJWuVSZRODLA9aSguZaSnh7ti86Phwsw-1NJRgB5OUvILESJqPt-YtIUM6wP_zGp80x2GkLnK1OeIjeDPlPJBQ7yS91iAZtw6cENsx_89GNeG-W7PxYAY2WZ_F0gOaq95RveDVi47ySA34jYbEhL1JbwZfV5Cd5G4xtAuQe_afnmzic_UPTZ0RF9IkaIZ4EILbRHakp10xoWP5UOWPO-TWfcFutVRTr7qZwRNpShg42lt8cBrinuu5QrdxSeykp4ui1hJF_PtkiipZ03Ug8p1Y8y2-jQAvc8eFbNjdbGPY4EVETZLKut6FfWPn7hxl_XAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هيئة الاعلام والاتصالات العراقية: ايقاف برنامج (الحق يقال) الذي يقدمه عدنان الطائي لمدة 45 يوم بسبب مخالفة الضوابط والمعايير الاعلامية</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/naya_foriraq/75361" target="_blank">📅 17:19 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75360">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 09-05-2026 جنود من جيش العدو الإسرائيلي في محيط بلدة دير سريان جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/naya_foriraq/75360" target="_blank">📅 17:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75359">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">تأجيل الجلسة نصف ساعة</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/naya_foriraq/75359" target="_blank">📅 16:48 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75358">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">الان - العراق   المرشحين للوزارات ورئيس الوزراء يغادرون القصر الرئاسي باتجاه قاعة مجلس النواب</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/naya_foriraq/75358" target="_blank">📅 16:44 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75357">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">الان - العراق
المرشحين للوزارات ورئيس الوزراء يغادرون القصر الرئاسي باتجاه قاعة مجلس النواب</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/naya_foriraq/75357" target="_blank">📅 16:30 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75356">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">صندوق النقد الدولي:
العراق سعى للحصول على مساعدات مالية، محادثات جارية مع العراق حول حجم التمويل وهيكلة قرض محتمل.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/75356" target="_blank">📅 16:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75355">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i280HVuUSIv9Rhem0m3f_zMVnFWr1O8e9tyCc4GAI4AlP43sARsTDmssAFWscAfzTGq74G5xFz5FnIZfvANwFRT3dxAqsvu5vhdtPAyzXyEFKuzePpZDkh1mQOLZIsJjMfiroAkn8w67AmCb3J6jGoP6jbyYTCS-0TdAI7MWY2uTTkv2vNJ-LeqgfweZR3x6J5MFd7HX5wshRdZUTtruHgP1vHRLCXFztbd_ZW55JXVibH6TlX_TjjJHu64bpb0z895yYz4Iale7Hb3f9fNLNOtVYKvBvQT49fGFgLc63rpCsHwOT0GANfhyEiiwFoB9qv73t8U_apizdoYUG_lJOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غضب جماهيري في مواقع التواصل الاجتماعي بعدما بثت قناة العربية السعودية تقرير خاطئ يتحدث عن العراقيات نقلا عن تقرير أمريكي وبعد البحث تبين انه غير صحيح وغير موجود</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/75355" target="_blank">📅 16:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75354">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">مكتب نتن ياهو:
توجيهات لوزير الخارجية لجدعون ساعر برفع دعوى ضد نيويورك تايمز على خلفية أحد المقالات حول اغتصاب أسرى فلسطينيين في السجون الإسرائيلية.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/75354" target="_blank">📅 15:38 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75353">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">وزيى الحرب الصهيوني:
مهمتنا في إيران لم تنتهِ، جاهزون لاحتمال أن نضطر للعمل قريبًا.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/75353" target="_blank">📅 15:29 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75352">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QvSBUDxvutNpcgXsAFM1tU3db1F7YnxbCN8JtcfY3dOVOhoYTFFaF7uu70w5KfFHGOCVwsSKFyfDPVtTucC7EOAhT3-JqTHDW1KFaCXgUnQzK1o_6vCBalYDya067bLMNKRNb2URyOxF4b1ywWKXnp7a8QCXBBHoZHprl6i8MI6AJxdb-lGId4vzCm0guEpYgX7lUSbK_U241Cx6toYM_kLZFpFOxJnH4IeM4CtqffvykDJLKLIy7xuee2gaGUGJHShwNbaZhDSiDNNn9pc-YcOoxTCgOzOV-9VECD5621YrpOjIHGBvjWMbl3z6Dz44hVHEBKEwnCBey39k8QxFEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوالف الگهوة / نايا   مصطفى جبار سند المرياني وزير مرشح بقوة في حكومة الزيدي …</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/75352" target="_blank">📅 15:12 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75351">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">CV حكومة علي الزيدي.pdf</div>
  <div class="tg-doc-extra">8 MB</div>
</div>
<a href="https://t.me/naya_foriraq/75351" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">السّير الذاتية لمرشحي الكابينة الوزارية لحكومة رئيس الوزراء المكلف علي الزيدي</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/75351" target="_blank">📅 15:08 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75350">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">رئيس حزب
إسرائيل بيتنا
ليبرمان:
أنا قلق جداً ولدي كل الأسباب للقلق، أن رئيس وزراء السابع من أكتوبر (يقصد نتن ياهو) مع تقديم قانون حل الكنيست، سيبدأ عملية عسكرية تهدف فقط لأغراض الانتخابات</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/75350" target="_blank">📅 14:47 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75349">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 08-05-2026 قاعدة شراغا التابعة لجيش العدو الإسرائيلي جنوب مستوطنة نهاريا بصواريخ نوعيّة.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/75349" target="_blank">📅 14:42 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75348">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🏴‍☠️
قائد سلاح الجو الإسرائيلي السابق اللواء عميكام نوركين:
أنا أشعر بالخجل والعار مما حدث لنا في السابع من أكتوبر 2023. من دون الولايات المتحدة، لما كانت إسرائيل قادرة على الصمود خلال الحرب</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/75348" target="_blank">📅 14:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75347">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">صافرات الانذار تدوي في المستوطنات الشمالية بعد هجوم لحزب الله</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/75347" target="_blank">📅 13:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75345">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">وفاة ضابط برتبة مقدم وجرح ثلاثة مراتب آخرين من جهاز المخابرات العراقي بحادث سير على الطريق الدولي .</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/75345" target="_blank">📅 13:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75344">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SK4WHMmlr-clJb9sPmfcujQSIrDQAFPfi5ChAaZOBFka5G1w2WV0vjrDUORPMMjLWvg-usv3nz87Cohb217pi99BA7c5n6vSTgk8MQg4U4NZMprpbJ18Js35A6FqE2x1xfWKvVgtZODbeOmEQWJnOZZOzdz7KRgL-kDlhKwaZP5_4HJGVb7uFGIWXoRmiVCWXxUmeYA7HMrllX_w-RFggBDgNLQyoUASfhPy8dM9A8QV7PE0mxOx54z8PUt_cWHsocX4txHnEb-5WITDzE6cvsjXy4YZpLhTZ4DxXBT6Tl182rx3bRYj6JRYzyXoS_vQ1l6nYu4ASJAbw90qmkPe6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جريمة بحق طفلة شيعية في سوريا..
بعد 45 يوماً من اختطاف الطفلة الشيعية زينب صدام ذات ال 15 عام في قرية الغور الغربية بمدينة حمص، عثر عليها مرمية على جانب الطريق بعد دفع ديتها متعرضة للاغتصاب الوحشي وفاقدة للذاكرة بسبب حقنها بجرعات مكثفة من المخدرات وبعد ذلك قامت حكومة الجولاني الإرهابية بزجها في السجن وترك مرتكبي هذه الجريمة من عصاباتهم دون حساب.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/75344" target="_blank">📅 12:19 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75343">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">عدد كبير من القتلى والجرحى في صفوف جنود الاحتلال الإسرائيلي بعد كمين من قبل حزب الله في جنوب لبنان</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/75343" target="_blank">📅 12:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75342">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">بلومبرغ عن بيانات ملاحية:
9 سفن محملة بالنفط والغاز عبرت مضيق هرمز منذ يوم الأحد
لا تزال بعض السفن الـ9 داخل خط الحصار الأمريكي في مضيق هرمز</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/75342" target="_blank">📅 11:15 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75341">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">إطلاق نار داخل معسكر دبلن في مطار بغداد الجناح العسكري .</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/75341" target="_blank">📅 11:01 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75340">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">إطلاق نار داخل معسكر دبلن في مطار بغداد الجناح العسكري .</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/75340" target="_blank">📅 10:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75339">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">حدث بحري شمال شرق الفجيرة</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/75339" target="_blank">📅 10:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75338">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">حدث بحري شمال شرق الفجيرة</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/75338" target="_blank">📅 10:31 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75337">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇮🇷
وزير الخارجية الإيراني: مضيق هرمز مفتوح أمام جميع السفن التجارية من وجهة نظرنا لكن يتعين عليها التعاون مع قواتنا البحرية</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/75337" target="_blank">📅 10:30 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75336">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‏وزارة خارجية كوريا الجنوبية: 24 من أفراد الطاقم على متن السفينة الكورية في مضيق هرمز</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/75336" target="_blank">📅 06:37 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75335">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8522f3e0a6.mp4?token=RCgWDgrNRjwX8SZLBa-a4lALCbwpCHJAHQOOmeX9VPBBdlXd3yAqsx_7TlFiJrn7K8vzFuiOMWqcFE-LxaJnLzOAuKSAwIhlmmSEzRT0dE4ZeQ8gVDGDlwv0LGtRNMMu3bilZLofnND4XDXP6lsGPMbVIR1Y4jpLdRo8Nr9LOK6NXJv2UxGjpx141sM4RX2IlaJCGYO4OhTtBXPiXJ094uQo-RKjIMzN0N9Toik_npBsTtvZkFohdITAOsNqoXHHRS_4pbBv2DRj6KBHgvm-K7GRaKTI_8i_Mfp_mmwoIr4Q0LFmfuovIeXsGBWklmUaz-norYvOmWPi1mcaTfE-5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8522f3e0a6.mp4?token=RCgWDgrNRjwX8SZLBa-a4lALCbwpCHJAHQOOmeX9VPBBdlXd3yAqsx_7TlFiJrn7K8vzFuiOMWqcFE-LxaJnLzOAuKSAwIhlmmSEzRT0dE4ZeQ8gVDGDlwv0LGtRNMMu3bilZLofnND4XDXP6lsGPMbVIR1Y4jpLdRo8Nr9LOK6NXJv2UxGjpx141sM4RX2IlaJCGYO4OhTtBXPiXJ094uQo-RKjIMzN0N9Toik_npBsTtvZkFohdITAOsNqoXHHRS_4pbBv2DRj6KBHgvm-K7GRaKTI_8i_Mfp_mmwoIr4Q0LFmfuovIeXsGBWklmUaz-norYvOmWPi1mcaTfE-5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏الرئيس الصيني يستقبل الرئيس الأميركي في بكين</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/75335" target="_blank">📅 06:35 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75334">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2c71524f9.mp4?token=rq3HZNdcru6Iic66UFYly2Y6ZNYHAuqRr6EruyJNvIC7FtRCJLUbT4h12h3bBrdon-QN6poGW714lQOeU9V2pUJp45DShxvAV9CnoaPehJ1TkTx332jyG4q4eQLWXQ2IXuq2RTBbs0LvrHlnOPai1HDF19g9AIF_SzEBFqrUcMrLNEk1f8GEmeqjta72_nU6lqmr1egaCgBjg9ZWucz_ZIcO2tYIxFu84r-7yz6_wENQaxpquO8dnZ_lvzPssd7OnR2wvWP31BEtbfCj2c-PpzrfLHBr-Aj9MNiFW7HmZhWMbRezcl9kpiAi0l78UEg6Va4Ea1hLiSys_zC0dke4jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2c71524f9.mp4?token=rq3HZNdcru6Iic66UFYly2Y6ZNYHAuqRr6EruyJNvIC7FtRCJLUbT4h12h3bBrdon-QN6poGW714lQOeU9V2pUJp45DShxvAV9CnoaPehJ1TkTx332jyG4q4eQLWXQ2IXuq2RTBbs0LvrHlnOPai1HDF19g9AIF_SzEBFqrUcMrLNEk1f8GEmeqjta72_nU6lqmr1egaCgBjg9ZWucz_ZIcO2tYIxFu84r-7yz6_wENQaxpquO8dnZ_lvzPssd7OnR2wvWP31BEtbfCj2c-PpzrfLHBr-Aj9MNiFW7HmZhWMbRezcl9kpiAi0l78UEg6Va4Ea1hLiSys_zC0dke4jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏الرئيس الصيني يستقبل الرئيس الأميركي في بكين</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/75334" target="_blank">📅 05:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75333">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sx1lAfhijhR2ehy_ZYx94INhpZa11ZgeS9C805m3TGQB4yaIHZzca-JkWTYONedL6AcQ_coQ_hEtnkm8Z9LEOzUHGy-Tb874Nxvi8uVUQvieojjcHynDOvC7_bPR4ddgKfaMFgAY-ooS3r_Tv7eVcGIhPyV9-I0InnhgKwFKu7hFxKAsdaIrMGkpSjPhUG7k2n_cqMl5_h_r0Gu-CN1FQAoi08Yg6Yr5ORrosv27Z7Ru-5U94W_2Rfw5TvcMRZBBe2rGlKUOhnALqUxFH-lS91dAtfYCC7mwxEwI-GsYm4yBvbngF0V8UHoi3L95QWrzKK1j3x1JvUyBXeaZN3CR6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نواب اسعد العيداني ينسحبون من تحالف تصميم " الشيخية " وينضمون لتحالف الاساس في مجلس النواب !!</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/75333" target="_blank">📅 02:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75332">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6MThjlOnYStFkAcI3ewkJVVgFuWMFxpZ-8CbiuAlxyZQkYoj7SAgUGET6Kzc1_Usyk_aTeI7UlLULMppzSPLshe2Y247zcNpVYSIU2spAPuGY1BYQV6R08p_6JphkjlyDljK1ziXc_UQ6LgWnvmzDUik08lH2usqIkkihyiF0zyO9rZULnrTGMi1aLwo15Lg_gKq1Jt61rM_kGGDX--Pzhcy_hyv3IqqUYwJhS2UTBjkkYqCTNjWvCaS6Yc2gzuqBEt2eQA1jqEOV2HZkBix85-YjK22lRgOf58Lc6ougFCrxvAlsFEvpriG81zUrKNceBUA4qupuuqun6PD9Yg0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
القوات المسلحة المغربية تعلن العثور على جثة جندي أميركي ثان كان مفقودا في كاب درعة اثناء مناورة في أفريقيا</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/75332" target="_blank">📅 02:04 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75331">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">واشنطن بوست
:
وفقا لتقرير استخباراتي أمريكي سري، تكتسب الصين مزايا استراتيجية من حرب إيران. يشير التقييم إلى أن بكين تستفيد دبلوماسيًا واقتصاديًا وعسكريًا، بينما تنفق الولايات المتحدة مواردها في الصراع.
وتشمل النتائج الرئيسية ما يلي:
باعت الصين أسلحة لدول الخليج خلال الهجمات الإيرانية.
ساعدت بكين الدول على إدارة نقص الطاقة بعد أن أغلقت إيران مضيق هرمز.
استنفذت الحرب مخزونات الصواريخ والدفاع الأمريكية، مما أثار مخاوف بشأن استعدادها لصراع مع تايوان.
تدرس الصين العمليات العسكرية الأمريكية وتستخدم رسائل مناهضة للحرب لتصوير أمريكا على أنها مزعزعة للاستقرار.
يقول المحللون إن الصراع يحسن نفوذ الصين العالمي ويضعف مكانة الولايات المتحدة مع حلفائها.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/75331" target="_blank">📅 01:11 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75330">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‏
روبيو
: آمل أن تلعب الصين دورا أكثر فاعلية لإقناع إيران بالتراجع عن سلوكها بالمنطقة، نريد أن تدير أميركا استراتيجيا علاقتها المعقدة مع الصين، والصين هي التحدي السياسي الأكبر الذي نواجهه جيوسياسيا.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/75330" target="_blank">📅 01:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75329">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترفيهي
‏الإمارات تنفي زيارة نتن ياهو أو استقبال وفد عسكري إسرائيلي</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/75329" target="_blank">📅 00:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75328">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9J74TnxvME4ICJ-F6ATuRPDkrJd9U25d9jGpFGZ844JhSMsjfuXqHetdqFFxdPthQmmmbtGcPRT_dbFeIbSSnkJ4DIxq0MdM7YjEwlUm82FwYQSzAWOGvnBaN8KRynFIshGHQglSnnBN2gFkcCLpT7zlLVCDYdK7iAHfFYZ5X9VO_x7wnlz5KtH3Fyg7VCD8Yv0wQ9j-Di7zQve5dMV3UpU-TXXZnhfSOVQs4muUGchkk8aNt7XR_daHm7FtwZT-_aew4yaYM2TbpLEOWXvSA_NEjZ00xUx3_8OxKeptahD6VAzB1tIuGlChAc4HO8Oj4gc8G6g5n8ncNY8ytepvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
وزير الخارجية الايراني عباس ‏عراقجي يعلق على لقاء نتن ياهو ومحمد بن زايد:
لقد كشف نتنياهو الآن علنًا ما نقلته أجهزة الأمن الإيرانية إلى قيادتنا منذ زمن بعيد. ‏إن العداء مع الشعب الإيراني العظيم مقامرة طائشة. أما التواطؤ مع إسرائيل في ذلك فهو أمر لا يُغتفر. ‏سيُحاسب أولئك الذين يتآمرون مع إسرائيل لبث الفرقة.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/75328" target="_blank">📅 23:49 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75327">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سيد وهب الحسني حصة بدر تقترب من حقيبة وزارة النقل العراقية ..</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/75327" target="_blank">📅 23:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75326">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سوالف الگهوة / نايا   ابرز الحصص الكردية في حكومة الزيدي  - فارس عيسى نائب رئيس وزراء  - خالد شواني العدل  - نوزاد الإسكان  - فؤاد حسين الخارجية  - سروة البيئة   - اما كتلة الموقف النيابية ظلت بلا موقف حكومي ..</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/75326" target="_blank">📅 23:34 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75325">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">طائرات مسيرة تستهدف مقرات المعارضة الايرانية الكردية في قضاء بحركة ضمن محافظة اربيل</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/75325" target="_blank">📅 23:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75324">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">سوالف الگهوة / نايا   ابرز الحصص الكردية في حكومة الزيدي  - فارس عيسى نائب رئيس وزراء  - خالد شواني العدل  - نوزاد الإسكان  - فؤاد حسين الخارجية  - سروة البيئة   - اما كتلة الموقف النيابية ظلت بلا موقف حكومي ..</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/75324" target="_blank">📅 23:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75322">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">انفجارات تهز محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/75322" target="_blank">📅 23:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75321">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">انفجارات تهز محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/75321" target="_blank">📅 23:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75320">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">تيار الحكمة يعلن ترشيح:
- فالح الساري وزيراً للمالية
صفاء الكناني وزيراً للشباب والرياضة</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/75320" target="_blank">📅 22:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75319">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">كتلة تقدم النيابية تعلن ترشيح:
- محمد نوري الكربولي وزيراً للصناعة
- عبدالكريم عبطان وزيراً للتربية</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/75319" target="_blank">📅 22:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75318">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مجلس الشيوخ الأمريكي يرفض مشروع قرار وقف الأعمال العدائية ضد إيران دون تفويض الكونغرس</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/75318" target="_blank">📅 22:29 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75317">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">شركة هاباغ لويد للحاويات:
نتكبد تكاليف إضافية بين 50 و60 مليون دولار أسبوعيا بسبب إغلاق مضيق هرمز.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/75317" target="_blank">📅 22:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75316">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 11-05-2026 آلية لوجستية (هيمت) تابعة لجيش العدو الإسرائيلي في بلدة طيرحرفا جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/75316" target="_blank">📅 22:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75315">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jyaki0ZIn2xt0QAKms79lcCkv0gEVBSrg9V-xLaJO0vafx8iHpTXli3v-3bqii13A9USFdraRYvWuauata81hufrAm_aWojx5MoJnhdPEvXckBHnC-tTGdy6InrNiEbF7gDnNEdTcM1NcILVQ1dMPYDKXTIi7H6yM_Sr6FPMgnGU4KdgQXDPKMQ5AR7wrfOAPxqfm2CX6zfXEnYrBghJIkCPIngeE169dN4dEmITUOCeEi5s-N0n0E7ix5RjGGwJo2_CT7vLEORCiLdIRZ-tI_urFsMsI7m3efLC7VWL5-GFSbnG08EPrAnyEeM7L7OWK93w7xWu-GjffBQnFinPRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عصابات تابعة لحزب البارتي في اقليم كردستان العراق تختطف المعارض السياسي (اسلام زيباري) وتنقله الى جهة غير معلومة</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/75315" target="_blank">📅 21:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75314">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مكتب نتن ياهو: زيارة نتنياهو أفضت إلى تحسن تاريخي في العلاقات بين إسرائيل والإمارات</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/75314" target="_blank">📅 21:49 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75313">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">📰
‏
NBC:
عدة سفن وناقلات مرتبطة بالصين عبرت مضيق هرمز خلال آخر 24 ساعة</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/75313" target="_blank">📅 21:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75312">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 11-05-2026 آلية هامر تابعة لجيش العدو الإسرائيلي في بلدة طيرحرفا جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/75312" target="_blank">📅 21:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75311">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اعلام العدو: نتن ياهو اجرى زيارة للامارات</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/75311" target="_blank">📅 20:53 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75310">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">العراق يصدر اول شحنة كبريت بأسعار قاربت 800 دولار للطن للاستفادة من ارتفاع اسعاره عالميا حيث قفزت أسعار الكبريت بنسبة 15% خلال الأسابيع الأخيرة لتقترب من مستوى 800 دولار للطن وهو أعلى مستوى تاريخي تقريبًا.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/75310" target="_blank">📅 20:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75309">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اعلام العدو: ‏نتن ياهو يلتقي محمد بن زايد</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/75309" target="_blank">📅 20:34 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75308">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اعلام العدو:
‏نتن ياهو يلتقي محمد بن زايد</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/75308" target="_blank">📅 20:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75307">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">وكالة رويترز تزعم: طائرات حربية سعودية استهدفت مواقع للفصائل العراقية خلال الحرب</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/75307" target="_blank">📅 20:16 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75306">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">وكالة رويترز تزعم: طائرات حربية سعودية استهدفت مواقع للفصائل العراقية خلال الحرب</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/75306" target="_blank">📅 20:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75305">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzFgbHk9bmJFtSXwgTkfg7BbZJReXrLynd2W5EdW-J0rUWl2GIzUYq975UPubNMc_Dj0nIbXY4bDbA2h-O9QSW9jgO-wKfv2UR9Hf-k3L5T_CzvSvAzcYG27-v_FdWxPKpMw2NpA55c93FD3RJulyxTo_V8SQTt8G32wlTPUHKtnog7TR_r1wiqHd-iI-EUNUn89RqkaC07etkjSxs_5Pyu6iUa7QtPzp2aiitMw-3COQOOZN7XVwa4spLPf3TAZG5p40lDvm-yzeOuVfSOXr1lZ719I8sW7drmJhjFqhNQAyiRtOuavgB9A72l2O3oeGM3H2tX_6HINw2WGIsMjXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
‏
وزير الخارجية الإيراني عباس عراقجي:
‏في محاولة واضحة لبثّ الفتنة، هاجمت الكويت بشكل غير قانوني زورقاً إيرانياً واحتجزت أربعة من مواطنيها في الخليج الفارسي. وقد وقع هذا العمل غير القانوني بالقرب من جزيرة تستخدمها الولايات المتحدة لمهاجمة إيران. ‏نطالب بالإفراج الفوري عن مواطنينا ونحتفظ بحقنا في الرد.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/75305" target="_blank">📅 20:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75304">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">مقرر الإطار التنسيقي عباس العامري: نحن لا نريد علاقة مؤقتة، بل نريد علاقة متينة مع الولايات المتحدة، وليس مع إدارة واحدة فقط، ونريد دخول كل الشركات الامريكية الاستثمارية للعراق"</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/75304" target="_blank">📅 19:53 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75303">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🏴‍☠️
جيش العدو الإسرائيلي
يعلن عن هجوم جوي استهدف قواته في جنوب لبنان.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/75303" target="_blank">📅 19:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75302">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سوالف الگهوة / نايا
مصطفى جبار سند المرياني وزير مرشح بقوة في حكومة الزيدي …</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/75302" target="_blank">📅 18:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75301">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سوالف الگهوة / نايا
ابرز الحصص لدولة القانون في حكومة الزيدي
- عبد الحسين الصحة " الفضيلة "
- عامر الخزاعي التعليم " الدعوة "
- الداخلية قدمت دولة القانون " قاسم عطا ، ياسر المالكي ، عبد الأمير الشمري "</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/75301" target="_blank">📅 18:29 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75300">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ab19cc8eb.mp4?token=pqUpzGkljIcsVNd86TvXg4aiDrOBFNOUKhkfE1JJff5DHCp8yEefNpe4zD5jryUaeYMxHEjQkUHefjQZv01xmN7mE_l8b9Mu-9gTAPtine92MY1RAipMCKzJfkIjJqWiKD-5DgY75j9vcTKsyFzRVOttt92zs6M4-cS5cXH12BhvCr0XrLNLQSJKMeekmzgZH-MMT70fd8Lkch9sIVEGpw6r_tBEoEAb7l8DWWLqVkUdhrV9CRlrNCFQuxMEmKy9Lbo7AAhj8a8RuVJSz8HzgR0gjejaKSPKLJVVC6kzEhqxTJgW7ZP0yJGukWfKykOzwP053PDJ7yPbqw0whjDcgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ab19cc8eb.mp4?token=pqUpzGkljIcsVNd86TvXg4aiDrOBFNOUKhkfE1JJff5DHCp8yEefNpe4zD5jryUaeYMxHEjQkUHefjQZv01xmN7mE_l8b9Mu-9gTAPtine92MY1RAipMCKzJfkIjJqWiKD-5DgY75j9vcTKsyFzRVOttt92zs6M4-cS5cXH12BhvCr0XrLNLQSJKMeekmzgZH-MMT70fd8Lkch9sIVEGpw6r_tBEoEAb7l8DWWLqVkUdhrV9CRlrNCFQuxMEmKy9Lbo7AAhj8a8RuVJSz8HzgR0gjejaKSPKLJVVC6kzEhqxTJgW7ZP0yJGukWfKykOzwP053PDJ7yPbqw0whjDcgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
إستهداف مواقع المعارضة الكردية الإيرانية في مدينة حلبجة شمالي العراق.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/75300" target="_blank">📅 17:34 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75299">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f60e50230.mp4?token=Zf2GHZlAdawQ2Tu0XGCIbWUzKhj7Z1iz-fcwQF1SxBBtoNuQXkCC5FmEbP40KFSpUofMRvpGEhFdI7qdgGhQalJIUQ_2ck2I8W6g2jq_WIF5qkx9Wzr_e8nU4xCo0qk-rPUGlcXZzbTX3VnxrHs81LuYcRylwbXsoGrP1I1NlMRLk2Z032Kcmoc4SDYONSf_DKTyD4wFS6A8PgZr3I-ygHPZNKbi1HW4cWo5-ZAkVYEfVUZeV2LHeI234ooDwTFjBLMlwKg5yu3J6fzhweEnQjAp3sBBMzkjRqh6XZD02w5U5nnLU0p0xVw54gBL-VgnHwKah-Snjvy2EQfqcSlNyDrbuBl1NQeiy24dR0eElB_GbEnONOZ2RpaSZShFZsNxpi3v3w4nDvjiGcpoSgn8kpU3fxSJjBtMBrw-V_4zOpZGC-hNPYLKTuhsZT_qX5WCNuUwEoZoJZfzrgeT9g73Nw-UTwRKr1h1Ry3AKTCqLtnuGgB9FKjgZ8Wbo52fViqzxdCDn9sSW7R5d-UjN-B9gPOkajSJrO-NHqOQpuB3dmccA0dZ2BrZxglgS_CYvaAB1_p0Lad5uZipyh1EYjbefHFpGQ_W-11hgxOlAydmjIm6M78cQ0Skl_rlZsqd_OyAoQGR-QSnVUmX0Gc6b543lrIcmbJARDbYMhoglMOKhIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f60e50230.mp4?token=Zf2GHZlAdawQ2Tu0XGCIbWUzKhj7Z1iz-fcwQF1SxBBtoNuQXkCC5FmEbP40KFSpUofMRvpGEhFdI7qdgGhQalJIUQ_2ck2I8W6g2jq_WIF5qkx9Wzr_e8nU4xCo0qk-rPUGlcXZzbTX3VnxrHs81LuYcRylwbXsoGrP1I1NlMRLk2Z032Kcmoc4SDYONSf_DKTyD4wFS6A8PgZr3I-ygHPZNKbi1HW4cWo5-ZAkVYEfVUZeV2LHeI234ooDwTFjBLMlwKg5yu3J6fzhweEnQjAp3sBBMzkjRqh6XZD02w5U5nnLU0p0xVw54gBL-VgnHwKah-Snjvy2EQfqcSlNyDrbuBl1NQeiy24dR0eElB_GbEnONOZ2RpaSZShFZsNxpi3v3w4nDvjiGcpoSgn8kpU3fxSJjBtMBrw-V_4zOpZGC-hNPYLKTuhsZT_qX5WCNuUwEoZoJZfzrgeT9g73Nw-UTwRKr1h1Ry3AKTCqLtnuGgB9FKjgZ8Wbo52fViqzxdCDn9sSW7R5d-UjN-B9gPOkajSJrO-NHqOQpuB3dmccA0dZ2BrZxglgS_CYvaAB1_p0Lad5uZipyh1EYjbefHFpGQ_W-11hgxOlAydmjIm6M78cQ0Skl_rlZsqd_OyAoQGR-QSnVUmX0Gc6b543lrIcmbJARDbYMhoglMOKhIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
12-05-2026
جندي من جيش العدو الإسرائيلي في محيط موقع خربة المنارة على الحدود الجنوبية اللبنانية بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/75299" target="_blank">📅 17:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75298">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">⭐️
إستهداف مواقع المعارضة الكردية الإيرانية في مدينة حلبجة شمالي العراق.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/75298" target="_blank">📅 17:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75297">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">سوالف الگهوة / نايا
ابرز الحصص الكردية في حكومة الزيدي
- فارس عيسى نائب رئيس وزراء
- خالد شواني العدل
- نوزاد الإسكان
- فؤاد حسين الخارجية
- سروة البيئة
- اما كتلة الموقف النيابية ظلت بلا موقف حكومي ..</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/75297" target="_blank">📅 16:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75296">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBBTjbLKsGhc4X3pxiEtY6BY1JBiqR655jaQ2vmmbzkQqOzyrOANDzbk31s8VtRHuDhujCOpobjvld5u1NvwYcU8vDXfotTDGhEaHkptReJpgEm6d8tGBMIvNDGLUjkhmGI_TMwIns96cXNDPxH2-eRVpZfTYkGiNndLzjtQO6KTkZMY3Iow64iCcyZ3n5mMm9-8tpP3AWk-b4nyQzIHXofaNrVcxe3Tu7bRoRBNwUfWzOFPHpMDbDY_Nq62nTrIddm3nBW167_2Ep63NgugWNeUA-JDEzhu5dq7tVfGXnSiiodDb1yck3Xl0RbOELX0_g-m1SI62kZzUBa_OG1-RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
دوي إنفجارات عنيفة بريف محافظة القنيطرة السورية والجولان المحتل وتصاعد أعمدة الدخان.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/75296" target="_blank">📅 16:07 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75295">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🌟
🏴‍☠️
دبابة ميركافا تابعة لجيش الإحتلال الصهيوني يتم دكها واعطابها من قبل أبناء نصرالله في بلدة عيناتا بجنوب لبنان.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/75295" target="_blank">📅 15:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75294">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dc6ea4372.mp4?token=gNAgS3Xxy02KMGGhAa20PmpYx3R3uqdLRo-p7QpJbmJWscwtYsgQ-Kra8voWpc8RUuFNkXZeqpuRmi6TgFjllZXuHVYJjmmQ1TigW0PNkHtFbxcpodMjmDQUhWaeg2Fy9WFqRdIScwuYNe0orGbXFHYmoIjozztRyk4yqCCnQF0EsoY2j2K7pdW6cLBbfcD_ItnyTyWd3FiECoF27ORUhCXeJDDGmJPRKCkUtJSiwFThmCnp78WEr_OVCrjhOAexHthvBwnkoI-DTWidMvZBaMRtGeNvPiNCFSSGRllbWr3DAXq5vwo-L-5VEtFKQ-xEy6bG2vu42QJm97Pe1Gz6nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dc6ea4372.mp4?token=gNAgS3Xxy02KMGGhAa20PmpYx3R3uqdLRo-p7QpJbmJWscwtYsgQ-Kra8voWpc8RUuFNkXZeqpuRmi6TgFjllZXuHVYJjmmQ1TigW0PNkHtFbxcpodMjmDQUhWaeg2Fy9WFqRdIScwuYNe0orGbXFHYmoIjozztRyk4yqCCnQF0EsoY2j2K7pdW6cLBbfcD_ItnyTyWd3FiECoF27ORUhCXeJDDGmJPRKCkUtJSiwFThmCnp78WEr_OVCrjhOAexHthvBwnkoI-DTWidMvZBaMRtGeNvPiNCFSSGRllbWr3DAXq5vwo-L-5VEtFKQ-xEy6bG2vu42QJm97Pe1Gz6nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
أسعار النفط العالمي تتجاوز 108 دولار للبرميل الواحد.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/75294" target="_blank">📅 15:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75293">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27da7c312c.mp4?token=pztEhmNk7crWADsK1-ZdALABmFQMaD24Rny2Sbs6Iajk-UufnNHXj_uSJSOK9MAX5NaxVQFDcdtDl-qA_ICRYT2e97M4i4Y35O04vQMQvw4wUt_VWqOi9iUmLUaPPVGMfrCG7RW_KgWAN3FPXnQhIa2lYXO9wwSEFIMj39LOtoEZ0W96cxGkBXYORvhFppSPX9gxb_T0MhGFhsAIKPNcfui5Q0QA_R_lVkRvGvs70WcrnX_YwYLuinRcJED6g4533j1t-R67SxDF9Eb4kZUuazEOtmmZ9_2MRsMUm-EWCltu2NE5XegZuaiMQ_vkZ4DvBR4bC9tLu0z0rmSktQFG8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27da7c312c.mp4?token=pztEhmNk7crWADsK1-ZdALABmFQMaD24Rny2Sbs6Iajk-UufnNHXj_uSJSOK9MAX5NaxVQFDcdtDl-qA_ICRYT2e97M4i4Y35O04vQMQvw4wUt_VWqOi9iUmLUaPPVGMfrCG7RW_KgWAN3FPXnQhIa2lYXO9wwSEFIMj39LOtoEZ0W96cxGkBXYORvhFppSPX9gxb_T0MhGFhsAIKPNcfui5Q0QA_R_lVkRvGvs70WcrnX_YwYLuinRcJED6g4533j1t-R67SxDF9Eb4kZUuazEOtmmZ9_2MRsMUm-EWCltu2NE5XegZuaiMQ_vkZ4DvBR4bC9tLu0z0rmSktQFG8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب يغادر واشنطن متوجهًا إلى بكين في الصين.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/75293" target="_blank">📅 15:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75292">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ailp5PisvZW4JNCNpuB59MpRvVj7SeotQC6Sn-5xr7-Bi3qmTZlzl6OYV27ieB-si-unuxOLcHR6OV4vwPYfJxUI1fPOVUpBhscybEqZ9PcvlxhDXRxogXatFYxd91hXKljAQEeJ0ltmOxrTVZsuY5P8tVnkyVtmvg1WYZTUPjelb7WoeoN3-x_ShxakrMsxuheq-oqg3DeNXiZYYrcpgqeMOnU7ecXss19g6CIqW5sHhXtDbOPTwMyljuUm7GM9EY51VbfnNZlT_D7BwyUxrlYeyXcoykn2JlZLRQWlwKTA61QfAfbFpDZcAzi88sf8OSGmsIgtZYFwW8fSdSkb6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
الإمارات تبدأ بتركيب حواجز مضادة للطائرات المسيّرة حول مستودعات النفط القريبة من مطار دبي الدولي من خلال هياكل وشبكات معدنية.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/75292" target="_blank">📅 15:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75291">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">▫️
🔵
بولندا: دفعنا بمقاتلاتنا الجوية بسبب الضربات الروسية على أوكرانيا</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/75291" target="_blank">📅 14:58 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75290">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JsvnMdUd2YdEWyKYjbEzijQQAPi8ShnMRZOeKnPL56HIsT1F6rglKLEoi-qYmjGudz7Dgv5ENrhNK5m8i7Xk7jdL4vkSrCyMvN0STv4pemqGYJQN4WTl3UGQFKabsqeibdL7pZ5_1VZio4VU1In45a5RONZCkPy3xWSN8gWvKAURse4DnFYUm5hHv3SFx0m05TRlLM6pCaAmhYUKUQqtaz6kLQ8cbyUrxdl56II8iYRBao0euo9uogsaQWUBqhu_yi4IAubowtVEKzQVQSAcHAcsoTinhG7aP348zONag4Hnn_P3BwRgl5tMgY_GvQQ9LgEWzi_xE6wwqriB4vJ0dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
أسعار النفط العالمي تتجاوز 108 دولار للبرميل الواحد.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/75290" target="_blank">📅 14:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75289">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a14692654c.mp4?token=aoDMduTzrd2JX2L3gUH0rO2scE6XnSzJvK_gFhuyBeMzH6mBtQAaQWWgHOSXboAA8cJ72D-ugo-LXyGDy0UQmV8ZJlB2nXjVLo-2CDigkXVp35YcdG7CWRRHWN09PDn9_EfwAUICQntSsFgAVTvXnct3wwhBIywOETcArTUo6Pj1xnIb6vFb6YXeGrI_kzCxt4nOrjphCyKyiPpRuwCxXc6hghMjtnmG5r-zFPvZ8z3sHWoZFCsJG1vHs6SvBbfDSv06Khg39mJNA4_DqwZngKjbg25QkqJocKaB7A7KywAVSzsSNpjcwLzZXtSOochoq1nh7pb-VTYrmxd13KnU52kpxM2jkXQD7alSXPcfNnbdQfWBZ5eD0Eq5HdA2ktQb5Yzb-patZ9lYPrkr8serCTlWLr3nfPc9bn7Py-b56vM0GIk6PM29wKmIppFY_jbP5rFxa47YDc1mQIoDMmisc8r3v8FXhsvmciN6kmptt20DL4zBTKrHnjVTWc2MtA5G1LWRRJuxvMdQ2AHR2xiCNVzD3T2m1nNj6ozgXb9eYvP8udjduczmGYsG7MD-qSRlltAj9-AYjz4U2vGBn7YZxw-sSdMDJh4twmOFX1sLw6XpCVFYgIG-brFu217tBKDbRA-Oudf5-vmR668w_n8__XEln9iEvcoNp00dypN71Ls" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a14692654c.mp4?token=aoDMduTzrd2JX2L3gUH0rO2scE6XnSzJvK_gFhuyBeMzH6mBtQAaQWWgHOSXboAA8cJ72D-ugo-LXyGDy0UQmV8ZJlB2nXjVLo-2CDigkXVp35YcdG7CWRRHWN09PDn9_EfwAUICQntSsFgAVTvXnct3wwhBIywOETcArTUo6Pj1xnIb6vFb6YXeGrI_kzCxt4nOrjphCyKyiPpRuwCxXc6hghMjtnmG5r-zFPvZ8z3sHWoZFCsJG1vHs6SvBbfDSv06Khg39mJNA4_DqwZngKjbg25QkqJocKaB7A7KywAVSzsSNpjcwLzZXtSOochoq1nh7pb-VTYrmxd13KnU52kpxM2jkXQD7alSXPcfNnbdQfWBZ5eD0Eq5HdA2ktQb5Yzb-patZ9lYPrkr8serCTlWLr3nfPc9bn7Py-b56vM0GIk6PM29wKmIppFY_jbP5rFxa47YDc1mQIoDMmisc8r3v8FXhsvmciN6kmptt20DL4zBTKrHnjVTWc2MtA5G1LWRRJuxvMdQ2AHR2xiCNVzD3T2m1nNj6ozgXb9eYvP8udjduczmGYsG7MD-qSRlltAj9-AYjz4U2vGBn7YZxw-sSdMDJh4twmOFX1sLw6XpCVFYgIG-brFu217tBKDbRA-Oudf5-vmR668w_n8__XEln9iEvcoNp00dypN71Ls" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 11-05-2026 آلية هندسية (D9) تابعة لجيش العدو الإسرائيلي على طريق الناقورة جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/75289" target="_blank">📅 14:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75288">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874e2b8aab.mp4?token=lR6leEw5dLC2VObsPJ8mp8y1e01tmBA-E6s9wUr2KGh0hVg8LIfYgpTPf5QAtHKtAKDr_ME8B_9XdCEGqBVDldBEKLGsK8J7lVqgH3pVvNPp2c39GWd4ZtiPRfx3fdBSJGCS6tpi7mDtwMgjtNav-qfDNpAL4DDnCV1RtnxUWzQxgUT8jrUOV_laXJRYrN6u4zBkFTttIG8Hk2_W-efoVO1jXuecrlYk9WF8sQq-Z-W9NfhvLw01YMhbB-X2UazgDPBO46Cy96tVO70Jshj_TttmJ6_mH36J3Cmb50pGY2LCdZ0TgwvPdyuG752pZz-JId6M6DN5qJGDqOI3lfMgLkVs_RemqtKQMRG3IbHyqK3PsS59tnjO_lsdkO3EB6qXpJLF2BZGxFcP-kSZRSawAE_gfhOUI6PkCpGp7qRhE0eHL0tBQgsW_C_K_LUpTgv0wHWye03TC5xGQsXUZSNpzFxFyybzZ2wGRjMcjfXRnDa0lPM8jpArqEVhXFzDiY_RDrVVrAxYhDWLZyPfOzzoHE4Xfs2Kw2Ak2p_6JJvyKj269ToJI7oX75W6mYFfsc_DQ0IYznt2KkmEJyPGLyNvb1GZDZv_aMQ3SXgaxNWVvc8pOnK5R4uvBE5VhwHbC9I-HCsN2L3nIXetuqIRTLqKn-ZLqwDfUqfxmYPDwNcCSTY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874e2b8aab.mp4?token=lR6leEw5dLC2VObsPJ8mp8y1e01tmBA-E6s9wUr2KGh0hVg8LIfYgpTPf5QAtHKtAKDr_ME8B_9XdCEGqBVDldBEKLGsK8J7lVqgH3pVvNPp2c39GWd4ZtiPRfx3fdBSJGCS6tpi7mDtwMgjtNav-qfDNpAL4DDnCV1RtnxUWzQxgUT8jrUOV_laXJRYrN6u4zBkFTttIG8Hk2_W-efoVO1jXuecrlYk9WF8sQq-Z-W9NfhvLw01YMhbB-X2UazgDPBO46Cy96tVO70Jshj_TttmJ6_mH36J3Cmb50pGY2LCdZ0TgwvPdyuG752pZz-JId6M6DN5qJGDqOI3lfMgLkVs_RemqtKQMRG3IbHyqK3PsS59tnjO_lsdkO3EB6qXpJLF2BZGxFcP-kSZRSawAE_gfhOUI6PkCpGp7qRhE0eHL0tBQgsW_C_K_LUpTgv0wHWye03TC5xGQsXUZSNpzFxFyybzZ2wGRjMcjfXRnDa0lPM8jpArqEVhXFzDiY_RDrVVrAxYhDWLZyPfOzzoHE4Xfs2Kw2Ak2p_6JJvyKj269ToJI7oX75W6mYFfsc_DQ0IYznt2KkmEJyPGLyNvb1GZDZv_aMQ3SXgaxNWVvc8pOnK5R4uvBE5VhwHbC9I-HCsN2L3nIXetuqIRTLqKn-ZLqwDfUqfxmYPDwNcCSTY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله: مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 12-05-2026 دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في محيط موقع خربة المنارة على الحدود الجنوبيّة اللبنانيّة بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/75288" target="_blank">📅 12:31 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75287">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9495fe1b87.mp4?token=UrX0mGmoP7bLDfEYnV-1CneJFL-FWg9_JDQJvrJspL6KV2w10Ymjb6N6vbKgmsw198r2uGSaNEQnE_FHoogD0P9uGritf198ExIEzjs92ViPx2ldHrzqfMsAlA8KzESQdT6OniSn4KoR6w_kTIUIsqAjQbBOck3hJ5KRdOrrAst_kWTxK_D-WomjoCFjYslK9wztZjUUI1mefa26xUldo9LLMEe74CuiwuCvhxWr0c1cX9zva3pvB31i5FL_TB6f_64yzXYaq9rIdVxBlN54G0O6AWqut--PzkVrntIp1xWLLnMFemGnQkRY5VI7BQO1FTMbSGQVx1xbp72oLCStBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9495fe1b87.mp4?token=UrX0mGmoP7bLDfEYnV-1CneJFL-FWg9_JDQJvrJspL6KV2w10Ymjb6N6vbKgmsw198r2uGSaNEQnE_FHoogD0P9uGritf198ExIEzjs92ViPx2ldHrzqfMsAlA8KzESQdT6OniSn4KoR6w_kTIUIsqAjQbBOck3hJ5KRdOrrAst_kWTxK_D-WomjoCFjYslK9wztZjUUI1mefa26xUldo9LLMEe74CuiwuCvhxWr0c1cX9zva3pvB31i5FL_TB6f_64yzXYaq9rIdVxBlN54G0O6AWqut--PzkVrntIp1xWLLnMFemGnQkRY5VI7BQO1FTMbSGQVx1xbp72oLCStBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غارة صهيونية جديدة على الطريق الساحلي في منطقة الجية جنوب بيروت</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/75287" target="_blank">📅 12:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75286">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">وكالة الطاقة الدولية: خسائر إمدادات النفط نتيجة إغلاق مضيق هرمز 12.8 مليون برميل يوميا منذ فبراير.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/75286" target="_blank">📅 12:24 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75285">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‏إيطاليا: سنرسل كاسحات ألغام قرب الخليج.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/75285" target="_blank">📅 12:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75284">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e6808ae10.mp4?token=pFAf9s8QWODuGtCW79xwU561xoyG3b7AhZ6jEX6qjF9QzrxXcZksS_axakHV9qnSc_i9pCfhnFzYpB94KHmalkyPprghFW9imbKCpYr31VFMr2TnmliY3oypBHdi3mJkMFsPn66IHukTneqyqXoamuzZMlTpAo42KjveHFpRv5b0I4QjkqkQc0PyqFHh7km6y1F0W9nnPqH3YeH74NnkeC89QYeHrG0uVexoTADyt-Y2U_MqiczU2yrAJtevahvaZ3xhxbry9OGhNVN-8WxgLyHOln-MEONP5uYq8Eq6wrK_IJaqjrudtz2cdqIcHtUEA90aZLaKTEi-b6muu334xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e6808ae10.mp4?token=pFAf9s8QWODuGtCW79xwU561xoyG3b7AhZ6jEX6qjF9QzrxXcZksS_axakHV9qnSc_i9pCfhnFzYpB94KHmalkyPprghFW9imbKCpYr31VFMr2TnmliY3oypBHdi3mJkMFsPn66IHukTneqyqXoamuzZMlTpAo42KjveHFpRv5b0I4QjkqkQc0PyqFHh7km6y1F0W9nnPqH3YeH74NnkeC89QYeHrG0uVexoTADyt-Y2U_MqiczU2yrAJtevahvaZ3xhxbry9OGhNVN-8WxgLyHOln-MEONP5uYq8Eq6wrK_IJaqjrudtz2cdqIcHtUEA90aZLaKTEi-b6muu334xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غارة صهيونية جديدة على الطريق الساحلي في منطقة الجية جنوب بيروت</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/75284" target="_blank">📅 10:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75283">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">انفجار يهز منطقة الكرادة وسط العاصمة بغداد</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/75283" target="_blank">📅 10:24 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75282">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇶
سلسلة الجثث مجهولة الهوية في العاصمة بغداد
- جريمة تهز العاصمة بغداد العثور على جثة طفلة تبلغ من العمر ٤ سنوات تعرضت لحالة اغتصاب وخنق بمنطقة الدسيم شرق العاصمة بغداد .
- العثور على جثة مجهولة الهوية في نهر التاجي شمال بغداد</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/75282" target="_blank">📅 09:52 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75281">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">انفجار يهز منطقة الكرادة وسط العاصمة بغداد</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/75281" target="_blank">📅 09:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75280">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">انفجار يهز منطقة الكرادة وسط العاصمة بغداد</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/75280" target="_blank">📅 09:31 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75279">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nexd_N98XEl4OkXDv4WnBT_QiUAAjuHrBXaKUHQI67nHOpNF3IpLkyin5jNDZopVL4mbMybExrHI0ajFlIEfrs-xNBZt1FBREPyKC5PoqZ1yNBIZNJHAhYR0ioCoXCgbuKpRjHU1Q5r6VvjFfwnnLiWbqibWr7IQd4Qw_wBX62rvLBbF7GWsyZrFGguFAGYqG24dWdsIlEP321aiaCiQoUMn1QxqESsFj8_DDUbGMakCsb4xOmOPTaYAPhzhq0oIjxHd1bs9fHeiFkbVK_I8D-d4VXie_9W2OEyBC7TA1qSExuSkJamF1oBpkqerjv9GgVmpOKmdaD8ilxIWV8eGHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب
:
ذكرت CNBC بشكل خاطئ أن جنسن هواونج، العظيم من نفيديا، لم يتم دعوته إلى التجمع المذهل لأعظم رجال الأعمال في العالم الذين يذهبون بفخر إلى الصين. في الواقع، جنسن حاليًا على متن طائرة الرئاسة، وما لم أطلب منه المغادرة، وهو أمر غير محتمل إلى حد كبير، فإن تقرير CNBC غير صحيح، أو كما يقولون في السياسة، أخبار مزيفة!
إنه لشرف لي أن يسافر جنسن، وإيلون، وتيم أبل، ولاري فينك، وستيفن شوارزمان، وكيلي أورتبرج (بوينج)، وبراين سيكس (كارجيل)، وجين فرير (سيتي)، ولاري كولب (جي إي إيروسبيس)، وديفيد سولومون (غولدمان ساكس)، وسانجاي ميهراوترا (ميكرون)، وكريستيانو أمون (كوالكوم)، والعديد من الآخرين إلى البلد العظيم الصين، حيث سأطلب من الرئيس شي، وهو قائد ذو تميز استثنائي، "فتح" الصين حتى يتمكن هؤلاء الأشخاص البارعين من ممارسة سحرهم، والمساعدة في رفع جمهورية الشعب إلى مستوى أعلى!
في الواقع، أعدكم، أنه عندما نجتمع، وهو ما سيحدث في غضون ساعات، سأقوم بذلك كأول طلب لي. لم أر أو سمع أبدًا عن أي فكرة من شأنها أن تكون مفيدة أكثر لبلدينا الرائعين!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/75279" target="_blank">📅 07:16 · 23 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
