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
<img src="https://cdn4.telesco.pe/file/YDRXZxuQanonD6AuWL4H-Gp0lFWC1BtB-e0c7A9eRaUYFY7J_d0nR3DkiX-JL6oia_MFPXYpSE11luBtbvDvS6m4DkWPJipoVgEZ1H_-a4uUoqyHWbj4XHIIMr_Yn-hWfHQRyq1DLuE9awXxkF9nYy-orHi6a0FBR1c90TMnZGS3ooYPk9DHlg9x7UzQBATqLC1G_eGO79syJZYFfaEUnXvpGHdfMsiutCvBZsDVG-2r82eiklutnye-qsa8AHw19W7VKllprUo5q0ozWXWZhQ4Bt7VV-HAy_HWjTNsHmT11MglYddUH9BXEjiUcQdsSA51lXEGKoAA73fh-PVVUhA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 271K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-29 23:22:58</div>
<hr>

<div class="tg-post" id="msg-88237">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/660318801d.mp4?token=bE5EjiFqT5qkLmL-JTsFiu3tHq30CZzoJ9CMRHhmILgi7UyFd-jo212OBq_y0pJN8rKwjvjuh5azYb_N4-UXOdQI8QdijO51PJVuG4S5vJpFfQ7OFqhX7yNziOj6QKSOLmGxpT9VNi_Chq-Wn_Sb-5DxWciiJ3UgRlTVWbNzcoVhw2rJJuRI9Y75x-KvnFm4Ucn9dCqoBKezhHoD-PQjOU7LHB2MGZGFdsA4nPoOJYvfELbN3MDnOUD40UAwwKVspe9_ApJXm5wEhMsqPadk7kjrMFR7GDUSO3HGt95MfqotN2l_dB3WUQTDHK3omg-TcRJQJwXMI12cqo2lRv4MkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/660318801d.mp4?token=bE5EjiFqT5qkLmL-JTsFiu3tHq30CZzoJ9CMRHhmILgi7UyFd-jo212OBq_y0pJN8rKwjvjuh5azYb_N4-UXOdQI8QdijO51PJVuG4S5vJpFfQ7OFqhX7yNziOj6QKSOLmGxpT9VNi_Chq-Wn_Sb-5DxWciiJ3UgRlTVWbNzcoVhw2rJJuRI9Y75x-KvnFm4Ucn9dCqoBKezhHoD-PQjOU7LHB2MGZGFdsA4nPoOJYvfELbN3MDnOUD40UAwwKVspe9_ApJXm5wEhMsqPadk7kjrMFR7GDUSO3HGt95MfqotN2l_dB3WUQTDHK3omg-TcRJQJwXMI12cqo2lRv4MkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
حدث امني خطير في امريكا   اعتقال امرأة للاشتباه في تخطيطها لتفجير قنبلة في مبنى الكابيتول بولاية نيويورك .</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/naya_foriraq/88237" target="_blank">📅 23:11 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88236">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🫡
أنا تحت راية أبا الفضل العباس
We will never forget Ya Abu Fathel</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/naya_foriraq/88236" target="_blank">📅 22:47 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88235">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">رويترز : قال مسؤولون كبار إن القوى الإقليمية لكرة القدم في العالم تناقش إمكانية طرح اقتراح بحجب الثقة عن رئيس الفيفا جياني إنفانتينو بعد أن أغضبهم بخططه لبيع حصة في كأس العالم لمستثمرين من القطاع الخاص</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/naya_foriraq/88235" target="_blank">📅 22:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88234">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇮🇶
مصدر امني لنايا
اشتباكات عنيفة شرق العاصمة بغداد في محاولة اعتقال احد قيادات جيش المهدي " ابو درع اللامي " .</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/naya_foriraq/88234" target="_blank">📅 22:07 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88233">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">زلزال قوي يضرب بيرو بدرجة ٦٫٨.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/88233" target="_blank">📅 21:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88232">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇺🇸
حدث امني خطير في امريكا
اعتقال امرأة للاشتباه في تخطيطها لتفجير قنبلة في مبنى الكابيتول بولاية نيويورك .</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/88232" target="_blank">📅 21:28 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88231">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇱
🇹🇷
الاعلام العبري:
المستوى الأمني أوصى بالتهدئة مع تركيا وعدم فتح جبهة إضافية.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/88231" target="_blank">📅 21:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88229">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f8d4d95c8.mp4?token=o22zrfB_dNofX0MpDM6rm8NNukecjgg9U6c9jYPz0t3q1P40lOzYZDveXRIAtGSxmIK0OGCqUNiFNahNxf6xcf9gQuLK3JHJArmxpOsSzF38u6ubJHSmjMlJ-ciCnQKB4jAS1dA05UuFGfmCJoCXX8Rkb0-sitVAX3cbWHRf1qr0uPrE6IDAWTs0NwxZFna0YuY8tLICpdb1SYtXOUwGTaKXx39EYBGpznwKjlqcbNiOyfJHQ344ZKQnSUXHiCrcJXLoUzx5nX38SXmOc0lAlDc0KDo0-9n4MXFNdmB9XLchviLvDjjCibAaPHGkkBOOX9A_RM8G4q-KVhbx4C6T0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f8d4d95c8.mp4?token=o22zrfB_dNofX0MpDM6rm8NNukecjgg9U6c9jYPz0t3q1P40lOzYZDveXRIAtGSxmIK0OGCqUNiFNahNxf6xcf9gQuLK3JHJArmxpOsSzF38u6ubJHSmjMlJ-ciCnQKB4jAS1dA05UuFGfmCJoCXX8Rkb0-sitVAX3cbWHRf1qr0uPrE6IDAWTs0NwxZFna0YuY8tLICpdb1SYtXOUwGTaKXx39EYBGpznwKjlqcbNiOyfJHQ344ZKQnSUXHiCrcJXLoUzx5nX38SXmOc0lAlDc0KDo0-9n4MXFNdmB9XLchviLvDjjCibAaPHGkkBOOX9A_RM8G4q-KVhbx4C6T0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انتشار كثيف للقوات العسكرية على سريع القناة بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/88229" target="_blank">📅 21:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88228">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9276455e9f.mp4?token=lhNpNYCmGA1Nu7PKB2QvEyLCryX9_T2VbMAEuPeE71CLLabELYlx2JdnMC2LGqxUS7f8CwRqWFhWAjUmRrdZYKXL9_steQvwevZ3OAEx7p7_iLeuHIE1eI17Y1OxUPO4lG90nup39CKKQqtV3vayPGUB3X12XyTv-n7PPw4ECqCahapVDo6bULYsoggm1a3w3wgW7nhGNrE2B2jXV1eN31fNueI_nDI9URYvERLeLNpCYFKICSx-OgsYveYJCvfMkTkAMzLACrbGpJ0a6dWENhLVOt12gaYkN10gdPf2EZX5MgFspzoGBhVZVFJcecTvrm2cYp89185Y5ENOqbytCYyv91oT-C_y8Cee_p9LJsGS-Qwj160FrLstTQIpyLrQXwsxixHVvVgyM0Ew8LHu4LXNStQY4sZyjkkVFmSmKbR7i21KpxLQ75JLzX8REAHwdgz6MuSzHGWC07hS4hnsi4yoOM9ty4bPGIDpesJsZCYzTecMBQq7ND4axv8-WG0hgXB27VHgTeREEWJN9RMQO4SWvyhgbnkMTn7C9fWMKn1H_JrXdPQ0JQ8FdrYQyGd7wRJonsHG-xQVCXbBsh4TD1ZdqDMS4TXoPWTZeCyXW0ljp_miYK85LK7lftR7RSthCiZb5Ne3gkKYKTBbCtZ8_42wTGfK0NFj9LYY715Q5Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9276455e9f.mp4?token=lhNpNYCmGA1Nu7PKB2QvEyLCryX9_T2VbMAEuPeE71CLLabELYlx2JdnMC2LGqxUS7f8CwRqWFhWAjUmRrdZYKXL9_steQvwevZ3OAEx7p7_iLeuHIE1eI17Y1OxUPO4lG90nup39CKKQqtV3vayPGUB3X12XyTv-n7PPw4ECqCahapVDo6bULYsoggm1a3w3wgW7nhGNrE2B2jXV1eN31fNueI_nDI9URYvERLeLNpCYFKICSx-OgsYveYJCvfMkTkAMzLACrbGpJ0a6dWENhLVOt12gaYkN10gdPf2EZX5MgFspzoGBhVZVFJcecTvrm2cYp89185Y5ENOqbytCYyv91oT-C_y8Cee_p9LJsGS-Qwj160FrLstTQIpyLrQXwsxixHVvVgyM0Ew8LHu4LXNStQY4sZyjkkVFmSmKbR7i21KpxLQ75JLzX8REAHwdgz6MuSzHGWC07hS4hnsi4yoOM9ty4bPGIDpesJsZCYzTecMBQq7ND4axv8-WG0hgXB27VHgTeREEWJN9RMQO4SWvyhgbnkMTn7C9fWMKn1H_JrXdPQ0JQ8FdrYQyGd7wRJonsHG-xQVCXbBsh4TD1ZdqDMS4TXoPWTZeCyXW0ljp_miYK85LK7lftR7RSthCiZb5Ne3gkKYKTBbCtZ8_42wTGfK0NFj9LYY715Q5Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
نتائج الحرب على إيران.. النفط يصل إلى 94 دولار للبرميل الواحد.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/88228" target="_blank">📅 20:57 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88227">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-_Kq70Aov4GhXOOfdRY5Q6Ju2cLe-PCWpyZkY0bO32YFoWWVrft3Y81yZS76GVnm-3PWnaWVnfIGJDECq5mAf86vvruRVcqwAEm1kjaXQpHCo3J6eIGjrLguSvscdkBzdYuJTFHO_Q4-NQg0e13AOvBwVPsfQpHFHZRvLiLu6quNQlnOFKy35wsTHUqMjWRLgdxabAOeihlE3sB62iJKwh4AEnGUfffYJX6wl0EOnMPmvbGFCc1R6N8zCsPcxRhKxTimOa_afAVupYEQ_1S_JCcNeki2kv_a34YfsemrEynhqXin3AXkzBLFsURH-E3FtGDdkbocvVPrulFt1eh0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">المحور الإماراتي في العراق يرد على زيارة قاليباف بصورة فوتوشوب  من تجيب قاليباف من كبيسة</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/88227" target="_blank">📅 20:01 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88226">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇺🇸
🇮🇷
وزير الخزانة الأمريكي بيسنت بشأن إيران
: سنفرض أشد العقوبات في التاريخ، وسنسقط هذا النظام.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/88226" target="_blank">📅 18:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88225">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇮🇶
🇮🇷
محمد باقر
قاليباف:
- كنا مع العراقيين أخوة وأصدقاء في أصعب الظروف.
- عمق الروابط بين العراق وإيران متجذرة في التاريخ</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/88225" target="_blank">📅 18:29 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88223">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4VuWeh0zXogkChqksQAnsJcG1PaewAEFlXpaycrSyo0Iz4ZN7C59suRQRdV-1BYAAplb8vlyXBdAoD4f4yBKTs3p6NRyuBa2xCFHY7NXIQ6AOM3vgRpxso2ytPWFRsh47nZf8Q9XSGfjiylHXl2GNws8WhcvP3vF-eblZvbH60dWNfvxGyoEjziH67AZkMsX_T71b89GYugMFZu1IYjDXoHv3HBOx7qmFFVM3qFzQcgKac8rdmk3Sq-dxE9bEVdLF5CGiEoOElXtNFnmZjHO2XZW6ve74smFzSwoCmFIP61xvTFYUQb9Z6epV9Gw69NnF3SiD6YDfATm5bdX_Kn5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
وزارة الخارجية الايرانية:
تزامناً مع ذكرى انقلاب 28 مرداد 1332، أقدمت الحكومة الأمريكية على فرض عقوبات اقتصادية وتجارية واسعة النطاق على الشعب الإيراني. ويُعد هذا الإجراء دليلاً آخر على استمرار العداء والخصومة التي ينتهجها صانعو السياسات الأمريكيون تجاه الشعب الإيراني منذ 73 عاماً، كما يثبت الطبيعة المعادية للإنسانية والمخالفة للقانون والاستكبارية للحكومة الأمريكية.
ولا شك أن العقوبات الاقتصادية الأمريكية على إيران، والتي استهدفت الحقوق الإنسانية الأساسية للمواطنين الإيرانيين، تمثل مصداقاً لـ«الإرهاب الاقتصادي» و«الجريمة ضد الإنسانية»، وإن مرتكبي هذه العقوبات والآمرين بها يستحقون المحاكمة والعقاب بسبب ارتكابهم مثل هذه الجرائم الشنيعة.
إن هذه العقوبات، التي تأتي عقب الحروب المفروضة التي استمرت عاماً ونصف العام، وكذلك الحرب التي استمرت 12 يوماً مؤخراً بين الولايات المتحدة والكيان الصهيوني ضد إيران، وبعد فشلهم في تحقيق أهدافهم المتمثلة بإجبار الشعب الإيراني على الاستسلام أمام مطامعهم غير القانونية واللاإنسانية، تستهدف الجمهورية الإسلامية الإيرانية، لكنها لن تُحدث أدنى تأثير في عزم الإيرانيين على حماية استقلال إيران وعزتها وسيادتها الوطنية.
إن فرض العقوبات والضغط الاقتصادي هو الوجه الآخر للحرب والعدوان العسكري، وإدمان الولايات المتحدة المرضي على هذين الأسلوبين لم يعرّض السلام والأمن العالميين للتهديد فحسب، بل تسبب أيضاً في انحطاط أخلاقي غير مسبوق للحضارة الإنسانية. وبناءً على ذلك، فإن أي دولة تؤمن بمبادئ وأهداف ميثاق الأمم المتحدة، ومن بينها مبدأ احترام السيادة الوطنية للدول، لا يمكنها أن تبقى غير مبالية إزاء استمرار خرق الولايات المتحدة للقانون وممارستها العدوانية العلنية تجاه القواعد الأساسية للنظام الدولي.
إن إقدام الولايات المتحدة على الإعلان المثير عن العقوبات الجديدة، رغم أنه يُعد اعترافاً صريحاً بارتكاب جريمة ضد الإنسانية، يمثل استمراراً لسياسة سبق اختبارها وفشلت، وإن إعادة اختبارها مجدداً لن تؤدي بالتأكيد إلا إلى تكرار إخفاقات الماضي وفضيحة مصممي هذه السياسة ومنفذيها. وبطبيعة الحال، ستقع مسؤولية نتائج هذه السياسة وتبعاتها على عاتق الحكومة الأمريكية ومصمميها ومنفذيها.
وتؤكد وزارة الخارجية، مع إدانتها الشديدة لإقدام الولايات المتحدة على تشديد العقوبات غير القانونية والمعادية للإنسانية ضد الشعب الإيراني، أن الجمهورية الإسلامية الإيرانية ثابتة ومصممة على الدفاع عن أمنها ومصالحها الوطنية ومواجهة الهجمات والضغوط العسكرية والاقتصادية والسياسية والنفسية الأمريكية.
وستواصل الجمهورية الإسلامية الإيرانية، بالاعتماد على قدراتها المحلية، وبالنظر إلى تجارب سبعة عقود من المقاومة الشاملة في مواجهة سياسة الضغط الأقصى والعدوان العسكري والإرهاب الحكومي الأمريكي ضد إيران، استخدام جميع الأدوات والقدرات المتاحة لردع شرور العدو الأمريكي-الصهيوني وحماية المصالح الوطنية الإيرانية.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/88223" target="_blank">📅 18:21 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88222">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نايا-NAYA</div>
  <div class="tg-doc-extra"><unknown></div>
</div>
<a href="https://t.me/naya_foriraq/88222" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔻
مناشدة عبر بوت نايا:  نحن مجموعة من صناع المحتوى نناشد الهنود والباكستانيين بالانتقال من الرياض الى نجران. نحن من بعد الله نعتمد عليكم في توثيق الانفجارات والدك اليمني على رؤوس ال سعود ومصالحهم الاقتصادية. نرجو منكم النزوح الى نجران والجنوب خلال الفترة المقبلة…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/88222" target="_blank">📅 18:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88221">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇮🇱
اعلام العدو:
يراقب المسؤولون الأمنيون الإسرائيليون الأتراك ليس فقط على البر، بل في المجال البحري أيضاً. ووفقاً للمصادر، تُرسل تركيا سفناً حربية إلى مناطق في الشرق الأوسط لم تتواجد فيها من قبل، وذلك لإظهار وجودها، وفي بعض الحالات على مقربة من السفن الحربية الإسرائيلية.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/88221" target="_blank">📅 18:02 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88220">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">القوات المسلحة اليمنية تنفذ عمليتين عسكريتين بطائرتين مسيرتين الأولى استهدفت هدفاً حساساً للعدو السعودي في مطار نجران والأخرى استهدفت أرامكو نجران وقد حققت العمليتان هدفيهما بنجاح ردا على انتهاك العدو السعودي لأجواء محافظة صعدة بطيرانه المسير</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/88220" target="_blank">📅 17:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88219">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/88219" target="_blank">📅 17:32 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88218">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/88218" target="_blank">📅 17:32 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88217">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZocURKqrsswnjKbYXMj9_PsKAUAFSSRuOk4IMRl205d6ABkpoP-ZrPvL_Ks0hVdmjcqM0y-_6QmknR6r5Sz1rla9s12lua3iuZWN67q5-lK6SxUSQHJiBCxQQvQLACLVE23yxmCcBYZLBOGPAudWNKgJHtx27tBSkhc0P0Ofbht7ox9yf9YVAmzTQkGeHxfmVvsW16Zi7muslVzsmaOKA14qXIp848tCwARsXZlMFKqkz-P-99jIXTy_ITMmz58uHL4PB3uA0lP4L_rXvole2xXLsOt49NQvu9VpHSQOq7YYOqiJSwMXRvqwLS-HA4VA77nvnL9UloGw1EKe9pDfww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
هيئة الإعلام والاتصالات العراقية تغلق الموقع الرئيس لشركة كورك في العاصمة بغداد وثلاثة مراكز مبيعات أخرى.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/88217" target="_blank">📅 17:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88216">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">وصول رئيس مجلس الشورى في الجمهورية الإسلامية الإيرانية السيد محمد باقر قاليباف والوفد المرافق له الى محافظة كربلاء المقدسة
🇮🇶
اخوتنا قدوتنا
🇮🇷</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/88216" target="_blank">📅 16:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88215">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇮🇶
قوة امنية تداهم مصرف الرافدين الحكومي فرع السعدون وسط العاصمة بغداد واعتقال موظفة كحصيلة اولية ..</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/88215" target="_blank">📅 14:04 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88214">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4UZYn7BA0XwI6MlqUDce7-9Rmp4re2hxSoBj0m4QKbbyQRe13sdVPGyWrU5YwkmEYMJy6w8eSQ_fH1IpgBIBgSKSHxS2cPQregaYecgta-KvgB_k8M0Y8XAYvqceOu6-SFbKopUX0KmGqWScQdt_fDjUPXUC8F4Op4vQ4cnfbaPB60iLqTL_Qka3wqs9ZtlJE3w3uohM1fDMM58M_1imCewpbBH4UAq0K5wzZNaP5fJ-rNKji4mNPT9nWuvvJtXPLs_MFoJRLqmS9QbnzESNdbYE24jQwLtrNjC3AJP7D0FPO7ixT7IZdIAszZhtq--wwGNEdNU2KLxGQ2h6t3X7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">المحور الإماراتي في العراق يرد على زيارة قاليباف بصورة فوتوشوب
من تجيب قاليباف من كبيسة</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/88214" target="_blank">📅 13:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88213">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">السلام على أبا الفضل العباس</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/88213" target="_blank">📅 13:54 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88212">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سليت سيفي في سبيل الله #سالم_المسعودي#100K</div>
  <div class="tg-doc-extra">العباد Abou Al Fadl</div>
</div>
<a href="https://t.me/naya_foriraq/88212" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سليت سيفي
#شاركها</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/88212" target="_blank">📅 13:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88211">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac7120c31b.mp4?token=BVs6CHzkpA_-iFzq8A-vg0ZHAtu78NQt8_xZ8y54rSCo1Urkeix_OTUg-k3iHmt1MbapVOWPULhpt9pEkecc1QDHfjZ0-V_Jh1_ef1CfTSHocaETKGEtEZK9D7fN96PU8oiZl6QdBeVJ40OCRURy30PvIDSf9lUOkJAYNEY0N2vZcELVN1w8mYgtf55LkoXhozffqFtCkmzTogU5yPqzqy0pLYieckLFInB3SssnmSoztNXi5UJvF5u0lSeO7jMsOPOTgZyjBKfitrHpM6Bp7Z8blpBYJGZtuY6_2n61Vw9UvRvvWGaW5tGSSkVpodC-z-F3iQa-tv-iIeZ0r0UFNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac7120c31b.mp4?token=BVs6CHzkpA_-iFzq8A-vg0ZHAtu78NQt8_xZ8y54rSCo1Urkeix_OTUg-k3iHmt1MbapVOWPULhpt9pEkecc1QDHfjZ0-V_Jh1_ef1CfTSHocaETKGEtEZK9D7fN96PU8oiZl6QdBeVJ40OCRURy30PvIDSf9lUOkJAYNEY0N2vZcELVN1w8mYgtf55LkoXhozffqFtCkmzTogU5yPqzqy0pLYieckLFInB3SssnmSoztNXi5UJvF5u0lSeO7jMsOPOTgZyjBKfitrHpM6Bp7Z8blpBYJGZtuY6_2n61Vw9UvRvvWGaW5tGSSkVpodC-z-F3iQa-tv-iIeZ0r0UFNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/88211" target="_blank">📅 13:51 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88210">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhUmasfSGscu_iruUCyib9-UV67iMUHAgLdOwqwgXssY5M2Jm23GF7SVQY0B42io2O69PePwmvb1ClC8N8N7ZmROWp_08ThG02Ck7mOJ3vhPQxdUAUarVHXxZVGOz8kdqmTTGDOV8A4ki0bof0NA_i9LfLc9XG4Ua7U-9vjOj4nbGGjMO6pntpSG0YMwOasUAuqw4aozmWHTTzIptj9qN3OLmrrSfB_aoqmb5_CiT6-MA8ViMOsJDHLGxuQXkqRuLUaHugHS09s-15JvxYZ0Vc970e1nvAlcBBZ-SkRbieG9v9qmtcWxtFQdXkRgyzuwfPvb7LFFzlJFN_Ss9OvP8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
فالح الفياض: تغريدة المتحدث الامني باسم الكتـائب هي "رسائل خشنة"</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/88210" target="_blank">📅 13:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88209">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MhRMlUTCfneIWj1BYyJj2e3wOz-5ScvWODljAVAtknrgogukYcsLfGdqdcQohESdUXKc1gkb9tM43_k2gYPe1A1xaauNpmF56okAExhjLqMgFeHD6GnqvA8sNJE0Yltrr8izppniw-CM_hNr8vpOYd1CIi_0G2p0Nseyvyez8D-3kjZpmlZEdNI9WhezIVuXdmnCCH6fOeXJ1zmu4cVMq_P8IG2kJmAqHMaX5QZautVSDojGKnNCbqZMdZCc5HLZ8uNxtY18e7PY5Va3Lr4t2hH2N4KoomiSoPh8pg45MAhQMgLxwxEPuOQPCENlogdpr1l4FjRgc6P8uC1EvS5gQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
حدث امني قبالة السواحل اليمنية..
سفن صغيرة تقترب من حاملة نفط شرق المكلا في اليمن والأخيرة تطلق نداء إستغاثة.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/88209" target="_blank">📅 13:19 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88208">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RzaJdf5VYc5dQJqEyFl0Dt2dDLylsHBz-FDJ_WEJ1tQZcTdSvSyeLsnFIfx5NIJsLKljf_qMPPbprxignR5iLuKYNGzgLiq9aUOkleySCx6qhyTU6UihasEtYXHExxext2EyOtDA3sZkH5PnJm7bhVTJaBB5xN7yx4p5lym3UpMItZ6h3ZTAEy4nSOj9OsiM_UR4Uc97YgLH0_L8XKIfM_KrbVXuckVK73AFJpf9NGBIVIrEmKO5m1IdmnNWVPWUJQgW3LPxIlNk5ul5rcesx1_AncAqSwwcTVuJDmD5GNZ6ldGbuSfWopAAplqDp2lKMQ1aXdnFqaVsemld0XAIww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
إبراهيم عزيزي:
تحركاتكم تخضع لمراقبتنا الدقيقة.
أي خطأ في الحساب أو خطأ متكرر ستكون له عواقب وخيمة عليكم أكثر من ذي قبل.
أنهوا وجودكم المشؤوم في المنطقة قبل فوات الأوان، واستسلموا للنظام الإيراني الجديد في المنطقة.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/88208" target="_blank">📅 13:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88207">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔻
وزير الخارجية العماني: المرور الآمن عبر مضيق هرمز لا يمكن فصله عن استقرار أمن المنطقة.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/88207" target="_blank">📅 12:57 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88206">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔻
مع إستمرار التوتر في المنطقة وسيطرة إيران على مضيق هرمز.. أسعار النفط العالمية تحلق نحو 93 دولاراً للبرميل الواحد.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/88206" target="_blank">📅 12:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88205">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇹🇷
‏
الدفاع التركية:
لم يكن أي وفد عسكري تركي في مطار أبو الظهور قبل أو أثناء القصف الإسرائيلي.
على إسرائيل وقف الهجمات المتهورة والالتزام بالقانون الدولي من أجل الاستقرار في المنطقة.
تركيا تتعهد حماية سيادة سوريا وسلامة أراضيها.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/88205" target="_blank">📅 12:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88204">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1579180dfb.mp4?token=ZkH2pqP9v3qCHJ6TND85db1U80ObySkJL_fa2udcIqDK0uwW8SA4xk0ipwqd3OfUAS6kNtEoOICu0S8DoMHysmXnGb4cYlMn6a2MfRnfbzj9WUeeaaGHSL61hZaPJ2GmZQ4G4uX0AcgPjhXrwmYvch3M1zlbfAEgX9B3L04iluPm8F-pERkOHnMpDpK1vt_qJcPAUjNSYcWhJLGQLAIOAVkybWwc21ARzlGECpJHVdEifMpFRxAqdJBS1-Mr3fgywELRx2ZVai-iRdo6_CJ06ozcF1gD-7Tztev78v_jE6xK3C7aG4IXZmOOQmzkd9A7BgkuAnH0yIMJjkSJWv1hcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1579180dfb.mp4?token=ZkH2pqP9v3qCHJ6TND85db1U80ObySkJL_fa2udcIqDK0uwW8SA4xk0ipwqd3OfUAS6kNtEoOICu0S8DoMHysmXnGb4cYlMn6a2MfRnfbzj9WUeeaaGHSL61hZaPJ2GmZQ4G4uX0AcgPjhXrwmYvch3M1zlbfAEgX9B3L04iluPm8F-pERkOHnMpDpK1vt_qJcPAUjNSYcWhJLGQLAIOAVkybWwc21ARzlGECpJHVdEifMpFRxAqdJBS1-Mr3fgywELRx2ZVai-iRdo6_CJ06ozcF1gD-7Tztev78v_jE6xK3C7aG4IXZmOOQmzkd9A7BgkuAnH0yIMJjkSJWv1hcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
العلاقات العامة لمصفاة النفط في طهران:
اعمدة الدخان في سماء طهران ناتجة عن حريق طال صهريجين لتعبئة ونقل المنتجات النفطية داخل محيط مصفاة النفط بالعاصمة طهران، ولايوجد أي حريق داخل المصفاة.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/88204" target="_blank">📅 11:47 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88203">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔻
الإعلام البريطاني:
قام مرتزق مدعوم من الإمارات العربية المتحدة، واسمه أبراهام غولان، بتنفيذ عملية مراقبة سرية في لندن عام 2016، استهدفت الناشط البريطاني العراقي أنس التكريتي، الذي كانت أبو ظبي تعتبره مرتبطًا بالإخوان المسلمين من خلال مؤسسته البحثية، مؤسسة قرطبة.
قام غولان، الذي نفذ سابقًا عمليات اغتيال في اليمن لصالح الإمارات العربية المتحدة، بجمع معلومات تفصيلية عن منزل التكريتي ومكانه للعمل وتحركاته، وناقش احتمال قتله.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/88203" target="_blank">📅 11:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88202">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIszFWxVvomkbXEupJb-qGtUL-LaYGu8BEXNxGHA_3UZxn4j0A1b8fJvI2xRa-LtstIpKRA9pltBkzF-VYNz4AuF8TvGXQF6--VZCTHbC_o4II469Xj6RUw784D0RPK35xinDMZE6DejbyibLH2H6iRfhY0TAh5deh65AnL6uMdnCxW8y0vVtzFYB1olq1lsBzcSteRei_NPW-w6q53TF8-p0H6TC54I8MRdQkquCnnAoP7Ijt4PBOQ-3IKCLsqpRyFy8yIfwCTDZQj3ImBy2TjlcSiAVyP5aE2Ban_DZJeWduZg7zLOts9kh36Fbv7i-5LO4SQD_8YCfKMoYOq3Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
مع إستمرار التوتر في المنطقة وسيطرة إيران على مضيق هرمز..
أسعار النفط العالمية تحلق نحو 93 دولاراً للبرميل الواحد.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/88202" target="_blank">📅 10:28 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88201">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srL9F5qEvh_mc_DBJS9D773d_v2vWmhsuplb3G1Kfp4H_cwBFMBv0u-ozA2HamNjvFgsaFlb7FXy_QX4_Z6TK4QR7uTCFVMAoUqDJOc4NgZgK-6ou_XkBZTjXEXFWn-LR7OeqOQjkRMeX3zkSOQ0Yrsxc4ZhOyMcR3c5QabAefsiBWIZq0cafaAkDNA7afKwJejJfRuin_pOf12-YQXYqzl00m-dgkWy4EhW9r5gTYhXqmCoggmzEyAqsGD7ux7J_ulr2Xdm0jJJFcutgnJFzmsDEYEGVki6hZoVtL9_2LgChmjodph0Z-q55LDy4hcIlkVY8T9rVdYA0RWCFJTPhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
رئيس مجلس القضاء الأعلى القاضي فائق زيدان يستقبل رئيس مجلس الشورى الإسلامي الإيراني محمد باقر قاليباف.
#أخوتنا_قوتنا</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/88201" target="_blank">📅 09:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88200">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ki3EB33hFALuFKkunBZn_3NP8BS4WNUOZWvqXd4fNvRj6cyjyAyWn4Z17ahzbB_pHPsNwr7UkuZArh4jEx-eHI1VOmX5IutVBVS-qX5wTVkMGrDsbdKZjwPx5qVo5I5i4AdCYpLzrw03zf7NJcDMkVLkPhUudLgV2UjDbNL_rcborU4j237y5RO_cpfOn4zL2QX-YS4bj7VRBeQc2U-Nqw5I56ZdD7lH0CJroM_EXdQYT5nn7n3HNalm0OIGef4DCqRpe90S0A7tj18Kq2c7TQXV5GUSGAp-CUcFSSHaZK9uakHqNhF_lVC1LmDQDokjHFfOGjeaCShpBi8TTHPTxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب: لم يمنح أحد جمهورية إيران الإسلامية فرصة أكبر مني لعقد صفقة. وللأسف، فقد فشلوا في اغتنامها. لذلك، أعلن اليوم عن العملية الاقتصادية الأكثر سحقًا على الإطلاق ضد أي دولة! ستكون هذه حربًا اقتصادية وعزلة على نطاق غير مسبوق. لقد دُمر أسطولهم البحري، وقُضي…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/88200" target="_blank">📅 09:27 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88199">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWG9Ui-YKDa9hqAc7QSqsrMUSE4wKqh2BzChHjnSe9GVG1Cyh6qarRLctfyuiCS6OvgcVHJKjy7Cw2fx8s4S243X6iDx4OZV1-Ckf_i4RYISuXIaV_s8aNcCIAIf1SCQ-altiDX5NzqL3GNSNgB393j4oeay6i4-vlMD1AS9CX8V2FqKPaluq4cLE5k0vVBDgOisN-Q5OJ_aqM7Viop7L3DX6iIe3vxKBfTckJ3XMrs_DIzlzy_oHzcLJ3IKwDkd4YeBCidtMjLaYj-V3_9R4KRPiKxa2P8zJ--2Xfun2Y_vp_5ELQSL6HOz74rDq_sEloQE0ennwXRUZyepIt03xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🇹🇷
وزير الحرب الإسرائيلي "يسرائيل كاتس":
أردوغان يجر تركيا إلى مغامرات خطيرة في سوريا. لن تسمح إسرائيل لأي طرف بتهديد أمنها.
سيكون من الأفضل لأردوغان أن يواصل إلقاء خطابات جوفاء وخيالية ضد إسرائيل في البرلمان التركي، بدلاً من اختبار عزيمة إسرائيل على الدفاع عن نفسها.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/88199" target="_blank">📅 08:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88198">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامب: لم يمنح أحد جمهورية إيران الإسلامية فرصة أكبر مني لعقد صفقة. وللأسف، فقد فشلوا في اغتنامها. لذلك، أعلن اليوم عن العملية الاقتصادية الأكثر سحقًا على الإطلاق ضد أي دولة! ستكون هذه حربًا اقتصادية وعزلة على نطاق غير مسبوق. لقد دُمر أسطولهم البحري، وقُضي…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/88198" target="_blank">📅 02:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88197">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixrc9XVtfsidm1Atv-1CNLP-jNakl7zTDTU8vfeI0ZImpxrsiemjn95WW0ySzIzVigOmfD6PrryZL6WH5GJV1ywjj1mmL9S9fGRjeN0Ms6rsML2aIk1m_YdBl-D53hgynH4SRS96FydHeLzbdCu0Uy0pcZbDQX7kNw_2gaWd8VSUC6AsXcGg0fo3wgRinYIarSFTccLG7D-tuorlnatQcIAIuSmJpEgyZkME7rDHiUKimqejO-KLEtK1IZpxSMsnCOScip6-fmPt6dhBQTSIAT627U8XTlFsUTZ5C46delD7Gj09irbDx9mud1gmouPu3Hk5gwVwby6T4M7OiFZJfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
لم يمنح أحد جمهورية إيران الإسلامية فرصة أكبر مني لعقد صفقة. وللأسف، فقد فشلوا في اغتنامها. لذلك، أعلن اليوم عن العملية الاقتصادية الأكثر سحقًا على الإطلاق ضد أي دولة! ستكون هذه حربًا اقتصادية وعزلة على نطاق غير مسبوق. لقد دُمر أسطولهم البحري، وقُضي على قواتهم الجوية، وأصبحت مصانعهم العسكرية ركامًا، وعملتهم لا قيمة لها، وبلادهم على وشك الانهيار. كما أعلن اليوم أن أي دولة تسمح لمؤسساتها المالية أو شركاتها أو مطاراتها أو كياناتها الحكومية بتقديم أي نوع من الدعم لإيران ستواجه عواقب اقتصادية وخيمة. تهريب النفط، وخطوط المقايضة، والتحويلات النقدية، ومكاتب الصرافة، وسجلات السفن، والشركات الوهمية - يجب أن يتوقف كل هذا الآن أنتم تعرفون أنفسكم. سيكون هذا يومًا حاسمًا اقتصاديًا، ونحن بحاجة إلى وقوف جميع حلفائنا إلى جانب الولايات المتحدة الأمريكية لعزل التهديد الإيراني وهزيمته. هؤلاء المجانين على وشك الانهيار، وهذه الإجراءات التاريخية ستشلّهم وتقضي على قدرتهم على بثّ الرعب في جميع أنحاء العالم. لن تمتلك إيران أبدًا سلاحًا نوويًا. شكرًا لكم على اهتمامكم بهذا الأمر</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/88197" target="_blank">📅 02:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88196">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇸🇾
تحليق طيران حربي وتفعيل دفاعات جوية في أجواء قاعدة كويرس العسكرية بمحافظة حلب السورية.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/88196" target="_blank">📅 01:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88195">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzr7X6cqRR7w_37vW-2HVaT-aEU6iqI21ZVIiYSHdV8pvGRxp66c4PtnLunLVya7fRy87zcbb_6537lJSVmR9zM4pZPavSzda7B_p7ubaOTd-ZA8NESwjEtiHehB7YHPrwbuMVChkNoB74nhH-5yXwp8oqHCmgbTFwBAkdFa9BqOlWdCnxMCHRQgKaI7MVk79wKFyWFAwq5-sw5bVXb6_JuYiUYIRKnLmzp61LcdZtpysDXkVklCOaiecuh8LQ2utFz4JyBVnjWAJNmAlmffq9x25uMx4ObvmJjNG3XLPD3U3Vo_61JtgSMnZITezwI-UyYkF8T2imcpnpATWesa1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
اتفاقية منتصف المدة قادمة إلى دالاس، تكساس، في 9 و10 سبتمبر. سيكون تجمعا لم يسبق له مثيل - لا يصدق!
لأول مرة على الإطلاق، سيجتمع الجمهوريون من جميع أنحاء بلدنا العظيم في مؤتمر منتصف المدة للاحتفال بانتصاراتنا الهائلة ونجاحنا، وعرض مرشحينا المذهلين، والاستعداد لأهم انتخابات منتصف المدة في التاريخ. حركتنا أكبر وأفضل وأقوى من أي وقت مضى. لقد جعلنا أمريكا عظيمة مرة أخرى، وسنحتفل بهذا النجاح الهائل وغير المسبوق تماما! يحاول المجنون اليساري الراديكالي تدمير بلدنا، لكنهم فشلوا، ولن ينجحوا أبدا، ما لم نسمح بحدوث ذلك - ولن نفعل ذلك!
سنفوز بجوائز منتصف المدة، ونحمي بلدنا ونعتز به، ونجعله أعظم من أي وقت مضى. كن هناك، 9 و10 سبتمبر - لن يكون مثل أي شيء آخر. ستكون الموسيقى والإثارة وأهمية هذه الأمسية في مستويات لم يسبق لها مثيل في مؤتمر أو حدث سياسي. سأكون معك في كلتا الليلتين، وسأذهب. أراك في دالاس!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/88195" target="_blank">📅 01:24 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88193">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇮🇱
‏بريطانيا تستدعي القائم بالأعمال الإسرائيلي بسبب المشروع الاستيطاني E1، وتعلن أنها ستفرض عقوبات ردا على التوسع الاستيطاني الإسرائيلي.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/88193" target="_blank">📅 01:13 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88192">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇸🇾
‏
وزير خارجية الجولاني:
لم تكن هناك نية لإنشاء قاعدة تركية في مطار أبو الظهور.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/88192" target="_blank">📅 01:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88191">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇮🇶
رئيس هيئة الحشد الشعبي السيد فالح الفياض:  المنطقة تواجه حالة من عدم الاستقرار واقتصاد سيء جراء الحرب الأمريكية الصهيونية، والجمهورية الإسلامية تعرضت لحرب شبه عالمية واستطاعت التماسك في مواجهة التحديات،تم استهداف الحشد الشعبي كوسيلة ضغط على فصائل المقاومة،…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/88191" target="_blank">📅 00:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88190">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇮🇶
رئيس هيئة الحشد الشعبي السيد فالح الفياض:
المنطقة تواجه حالة من عدم الاستقرار واقتصاد سيء جراء الحرب الأمريكية الصهيونية، والجمهورية الإسلامية تعرضت لحرب شبه عالمية واستطاعت التماسك في مواجهة التحديات،تم استهداف الحشد الشعبي كوسيلة ضغط على فصائل المقاومة، الحشد الشعبي موجود في كل المناطق الحساسة والخطرة، وهو عامل اطمئنان للجميع، الحشد الشعبي وحد العراقيين وأجهض الطائفية من خلال منح الجميع فرصة الدفاع عن مناطقهم.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/88190" target="_blank">📅 00:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88189">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇺🇦
🇷🇺
عمدة كييف:
"انفجارات في العاصمة. كييف تتعرض لهجوم باليستي.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/88189" target="_blank">📅 00:28 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88188">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇺🇸
الخزانة الاميركية: ‏
تجاوز الدين الفيدرالي الأمريكي 40 تريليون دولار في 19 أغسطس/آب، مع توقعات بأن يتجاوز الإنفاق الحكومي الإيرادات بأكثر من تريليوني دولار هذا العام، وأن تتجاوز مدفوعات الفائدة السنوية تريليون دولار. وتُعدّ الفائدة الآن ثاني أكبر بند إنفاق حكومي، بعد الضمان الاجتماعي فقط.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/88188" target="_blank">📅 00:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88187">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇮🇶
مدير مديرية الإعلام الحربي في هيئة الحشد الشعبي مهند العقابي:  ٣٠ أيلول هو يوم سيادي للعراق كون المقرر فيه إنهاء الوجود الأجنبي في العراق  هناك ماكنة ثالثة قد تكون إعلامية أو ثقافية أو سياسية تحاول التشويش على هذه المناسبة  هناك دعايات تحاول التشويش على…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/88187" target="_blank">📅 00:02 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88186">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBmLTNXaPJb60WhVWp_9KOuMQjl3Q2sS5re97yPen4oXlFWENEOnyu7Zk1VZ9HFhUlxIXxF19aaQhGbHPj24rkC6SW9-i_pqsCD64SrwLwH-ul6KIg2LJjtsDXiDTy4kwsxkwWUSjwK3o1MLRIdjZSnh67elaGfQAQ9c_OUS1i2SmTcFT396ALYJQlWmHODt7gZ6Jd-upTNa53JiphrKJkMwOu2dKh9JonIpYgb7RYmxQ_PwhX_RExTJZumNyvd1CEqKDbyxDsMoQbYCQtwMjX0e8oO68wYLHKU5zTfQJhrbfDbJNKkkmZr-CT8PA8HW2EdHYe1QXckeQNIHSrjh3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
حصيلة عمليات القوات المسلحة اليمنية منذ إعلان قرار حظر الملاحة البحرية على العدو السعودي في ٢٠ يوليو حتى ١٩ أغسطس.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/88186" target="_blank">📅 23:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88185">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇮🇶
مدير مديرية الإعلام الحربي في هيئة الحشد الشعبي مهند العقابي:
٣٠ أيلول هو يوم سيادي للعراق كون المقرر فيه إنهاء الوجود الأجنبي في العراق
هناك ماكنة ثالثة قد تكون إعلامية أو ثقافية أو سياسية تحاول التشويش على هذه المناسبة
هناك دعايات تحاول التشويش على هذه المناسبة الكبيرة للعراق
30 أيلول حدث تاريخي ومنجز اشتركت فيه العديد من الأطراف
ما ينعم به البلد حالياً من أمن واستقرار هو بفضل الأجهزة الأمنية العراقية
هناك من يحاول خلط الأوراق بشأن ملف حصر السلاح بيد الدولة
يفترض بالعراقيين أن يحتفلوا في يوم 30 أيلول لأنه يوم سيادة وفرح
الحشد الشعبي يتقدم يومياً ويصبح أكثر قوة من ناحية العدد والتدريب والتنظيم والتسليح والتجهيز
الحشد الشعبي سندٌ للقوات الأمنية
نأمل إقرار قانون الحشد الشعبي في الأيام المقبلة
فصائل المقاومة حريصة على النظام السياسي
هناك أطراف تحاول تأزيم الموقف بشأن حصر السلاح
نستغرب الحديث عن وقوع مواجهات أو صدامات بعد 30 أيلول
لن يصل العراقيون إلى مرحلة الصدام فيما بينهم
نحرص على إدامة الاستقرار الذي يشهده العراق</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/88185" target="_blank">📅 23:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88184">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇺🇸
‏ترمب: التفاوض مع الإيرانيين حاليا مضيعة للوقت.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/88184" target="_blank">📅 23:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88183">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">س: ما هي الإجراءات الأخرى التي يمكن فرضها على إيران؟  ترامب: حسنًا، لدينا إجراءات يمكننا فرضها. لدينا عقوبات قاسية جدًا، وسنرى ما سيحدث الآن. الممر المائي مفتوح، وهناك العديد من السفن التي تمر عبره. لكن الناس لا يبلغون عن ذلك. وقد يؤدي ذلك إلى إبطاء الأمور...</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/88183" target="_blank">📅 23:17 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88182">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f05a9fd75c.mp4?token=RrSe9QxgsFlHL8ZRJCFn7Vn9Diwczlxaa5DRFmS6X9EVqH8lL7b1si8HCvsDMc3IHfrMFookDjq6c2ToNi6wdMy4tEfmZHd-1tnOVp27EVhz4Fir8a2DTInXAe2us4FIPK-z3-uvsSRWCbsiUEU8V_nDb8wqiFMVqodiEBMznDceRod_cde2WIc4Yj9OPodEOSCcEJ4lr4o_LbyXat3EfgbU6M8P38uQBJ5SbzCWGTdRNoE27wnpq8-ExMn-x9hU5tzT_srTB_sq3sro77cyvv58Qa2y0hOIhquPCu1E_tUZ4GyU2SdxTCvBFWYqcckLyiW8v26JKyfug7K2c5b_0znxFTRnKPkEREhDUrAUMMHzSeDWFerCqAsGH51iTnVUIbfGGhtuBh_Fz5VF-VY1KdWMyVGkDTmuBiKcGHOyQFZqIkDSWpaubHxf0_KPzjUDhrAPdPdCqQDm8rZ0mmX7fK_ziqLZq1Cpih0xkB_h8he5DB39AXh32v0X6q47rkG6ZAPGjymllPQ_4BNEFCXDFeGteZXT4yDVwrhZUSNPWBVqzH5wMgC9OIPBpE99VHwHSSBHk0BpueQ6jU3wfBYizVtfXdQjB6inLzvv05QFeJdpZ0h4SoboBSacRhgJYgCC2eR_nW5b2ePz60Uz7pjhYoCsIV1WIMxM4jT8XGVcd1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f05a9fd75c.mp4?token=RrSe9QxgsFlHL8ZRJCFn7Vn9Diwczlxaa5DRFmS6X9EVqH8lL7b1si8HCvsDMc3IHfrMFookDjq6c2ToNi6wdMy4tEfmZHd-1tnOVp27EVhz4Fir8a2DTInXAe2us4FIPK-z3-uvsSRWCbsiUEU8V_nDb8wqiFMVqodiEBMznDceRod_cde2WIc4Yj9OPodEOSCcEJ4lr4o_LbyXat3EfgbU6M8P38uQBJ5SbzCWGTdRNoE27wnpq8-ExMn-x9hU5tzT_srTB_sq3sro77cyvv58Qa2y0hOIhquPCu1E_tUZ4GyU2SdxTCvBFWYqcckLyiW8v26JKyfug7K2c5b_0znxFTRnKPkEREhDUrAUMMHzSeDWFerCqAsGH51iTnVUIbfGGhtuBh_Fz5VF-VY1KdWMyVGkDTmuBiKcGHOyQFZqIkDSWpaubHxf0_KPzjUDhrAPdPdCqQDm8rZ0mmX7fK_ziqLZq1Cpih0xkB_h8he5DB39AXh32v0X6q47rkG6ZAPGjymllPQ_4BNEFCXDFeGteZXT4yDVwrhZUSNPWBVqzH5wMgC9OIPBpE99VHwHSSBHk0BpueQ6jU3wfBYizVtfXdQjB6inLzvv05QFeJdpZ0h4SoboBSacRhgJYgCC2eR_nW5b2ePz60Uz7pjhYoCsIV1WIMxM4jT8XGVcd1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب: لم تكن الصفقة مع إيران كما قالوا، ولن يكون مضيق هرمز بنفس الأهمية التي كان عليها في الماضي.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/88182" target="_blank">📅 23:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88181">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce1c50722f.mp4?token=gULQ1aXCSRlZPilhndLJPXKH78aRJBI1zzYLul5IgND14Zex58Fa3YAUYJPB0VHZRpJu8MqivgES_M8EMN_wR7NPXbt-6nMEoteWIV7n-lbW5nc3Yu4zxT5OdsIsEvkh0AfzhvRpT1HCVwFEB6Pod0Rx9BEABq4MpFW8fIasTsKEZCqrseDg6Du5zLAG68T6x8SbiyPlBGKYzJpR0v9cv4aGtQtp6vXLj0dOuBDQucPiCKZUlyg14E5pcSI2hs78Y_n9LjJuECy3qpHg-jgDMf6gmwoqqmV3P2CNtFQESXTkVlfLQ4ms3ShbDwzTf-wZRl0EYMoCLYtvKJhMZQJXsqhcRrHT4n8lu0u42BOEdXuBan4EiN0eadSTUaKhomnOsiSctVC2B95wrReI5Q7JpwAOOQra5aRapU0DkpIJ4O9TWMHgdCNj8s9D1uq6xCo8K40iR_RdYOr6lv_mWtpGgI5fI3nsuR0CSlixTEcjP15nmYyuW4Cnbw7_uFYXCN5u5Is95snxHrcscIAFgWIC_TZQArqXxSRZnktELf6cEAT3ms2mne9xsIcin81uSlbN61_CJfyC8hjMnsql-GwsGtdM-1Qz9DsF_cE9VWaW72cqQyLaZGDCVHDZJODZf0IipEPz4Drb_NtKkGByTwmz5_yKDbZ6f3HSYSvCY-ORl4E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce1c50722f.mp4?token=gULQ1aXCSRlZPilhndLJPXKH78aRJBI1zzYLul5IgND14Zex58Fa3YAUYJPB0VHZRpJu8MqivgES_M8EMN_wR7NPXbt-6nMEoteWIV7n-lbW5nc3Yu4zxT5OdsIsEvkh0AfzhvRpT1HCVwFEB6Pod0Rx9BEABq4MpFW8fIasTsKEZCqrseDg6Du5zLAG68T6x8SbiyPlBGKYzJpR0v9cv4aGtQtp6vXLj0dOuBDQucPiCKZUlyg14E5pcSI2hs78Y_n9LjJuECy3qpHg-jgDMf6gmwoqqmV3P2CNtFQESXTkVlfLQ4ms3ShbDwzTf-wZRl0EYMoCLYtvKJhMZQJXsqhcRrHT4n8lu0u42BOEdXuBan4EiN0eadSTUaKhomnOsiSctVC2B95wrReI5Q7JpwAOOQra5aRapU0DkpIJ4O9TWMHgdCNj8s9D1uq6xCo8K40iR_RdYOr6lv_mWtpGgI5fI3nsuR0CSlixTEcjP15nmYyuW4Cnbw7_uFYXCN5u5Is95snxHrcscIAFgWIC_TZQArqXxSRZnktELf6cEAT3ms2mne9xsIcin81uSlbN61_CJfyC8hjMnsql-GwsGtdM-1Qz9DsF_cE9VWaW72cqQyLaZGDCVHDZJODZf0IipEPz4Drb_NtKkGByTwmz5_yKDbZ6f3HSYSvCY-ORl4E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏
ترامب
: لم تكن الصفقة مع إيران كما قالوا، ولن يكون مضيق هرمز بنفس الأهمية التي كان عليها في الماضي.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/88181" target="_blank">📅 23:05 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88180">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
الولايات المتحدة تجري عملية سرية لنقل النفط عبر مضيق هرمز.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/88180" target="_blank">📅 22:50 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88178">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-poll">
<h4>📊 كمواطن عراقي ماذا يهمك اكثر ؟!🇮🇶</h4>
<ul>
<li>✓ نزع السلاح</li>
<li>✓ توفير بانزين وكاز في المحطات</li>
</ul>
</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/88178" target="_blank">📅 22:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88177">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KpOCKJewX3wUJZxpXAkaXW0u84qwKfPymYJTH0CkK-7byf9HeRrsvTwwv-TUkONbo8etn0coZdI1O4fDcPZZHHIjd4gVGBt0F_j7C-3OKGq-9wgdGelv1FvJyKH-2VeLLcWgUL5ilFz9xPfQRmJGEiBQO5xenBMJvfqzKf_hgrXazbZrpyU2EcjgQV7r4gcFbIfMQBT5FmrOphToLLzAAPfXbApg_DmqsR3nc1N9PfE8hMAwVv-645SIheoeHvcYODZSUat9I24X8BNDxVoHbjUP8uXdMv9SoqXpb_gzE2EsIco8ddf26w9GCH171lV_fkbQUzSsRw3EdJbJacojyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
هيئة الاعلام والاتصالات العراقية تقرر منع سجاد سالم من الظهور لمدة 90 يوم</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/88177" target="_blank">📅 21:59 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88176">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇮🇷
🇺🇸
بسبب هزيمتهم النفسية من ايران
إعلام أمريكي : ‏تقدم وحدة تابعة للجيش الأمريكي في ولاية جورجيا لجنودها تصريحًا لمدة أربعة أيام للعب لعبة GTA 6 كحافز لإعادة التجنيد. وقد اختار عشرون جنديًا هذا الحافز بالفعل .</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/88176" target="_blank">📅 21:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88175">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇮🇱
نتن ياهو:
لن نتسامح مع وجود عسكري تركي في سوريا يهدد إسرائيل. لقد أوضحنا الرسالة بشكل جليّ: لا تفعل. يبدو أنهم لم يسمعوا ذلك بوضوح كافٍ، لذلك تأكدنا من أنهم فهموه بشكل أفضل.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/88175" target="_blank">📅 20:54 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88174">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇮🇶
جهاز الأمن الوطني العراقي في قضاء الشرقاط ضمن محافظة صلاح الدين شمالي البلاد يلقي القبض على شخص قام بوضع مادة سامة في خزان ماء الطبخ في احدى المطاعم الامر الذي تسبب بـ(250) حالة تسمم.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/88174" target="_blank">📅 20:49 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88173">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇮🇱
🇸🇾
رويترز:
رئيس الموساد الإسرائيلي رومان جوفمان أجرى مكالمة هاتفية مع وزير الخارجية السوري أسعد الشيباني في 14 أغسطس وناقش الوجود التركي في سوريا</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/88173" target="_blank">📅 20:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88172">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇮🇶
هيئة الاعلام والاتصالات العراقية تصدر حزمة عقوبات بحق قناة الفلوجة:  - إيقاف بث برنامج حوار التاسعة لمدة (10) أيام تبدأ من تاريخ صدور قرارنا هذا المخالفته لائحة قواعد البث الإعلامي  - منع الظهور الإعلامي بحق مقدم البرنامج السيد (علي فرحان) لمدة (10) أيام…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/88172" target="_blank">📅 19:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88171">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e275d7a197.mp4?token=GqBXrOSF_C1sgvPuJnjbCUoy-cKHFGCircOwvcQw9pl4ESSCC7B08yn1_ke36n5NovuciURyPSvKFtzh8v9P3oX47ttyZte_55Bz26lH-ntMuiewyxRjO1BBTJpftWHdR2bGMuL9jslq6OwRB24W0rDjomCaV9tQsrZHttKod0lkBg1Iqq7iWY5BTvlKpFcVl-RISppZe6xPdyVKlPVI_sttk0Y3EVy7GkIQ_dJjwQJUN4SH5b2MfnYjzQLFXv8lVf9tVoS2XeHZkPiT3zL0kSzHwNgOVD-tElHbOcXAPsWwVT2VjulZhIv1-y79rGNgdvvBIN5SCw0SyJmpx60fuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e275d7a197.mp4?token=GqBXrOSF_C1sgvPuJnjbCUoy-cKHFGCircOwvcQw9pl4ESSCC7B08yn1_ke36n5NovuciURyPSvKFtzh8v9P3oX47ttyZte_55Bz26lH-ntMuiewyxRjO1BBTJpftWHdR2bGMuL9jslq6OwRB24W0rDjomCaV9tQsrZHttKod0lkBg1Iqq7iWY5BTvlKpFcVl-RISppZe6xPdyVKlPVI_sttk0Y3EVy7GkIQ_dJjwQJUN4SH5b2MfnYjzQLFXv8lVf9tVoS2XeHZkPiT3zL0kSzHwNgOVD-tElHbOcXAPsWwVT2VjulZhIv1-y79rGNgdvvBIN5SCw0SyJmpx60fuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏يزعم ترامب أن الولايات المتحدة "تمتلك" مضيق هرمز</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/88171" target="_blank">📅 19:08 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88170">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeefd4da47.mp4?token=Cvw7gQ-0ItA7sst5TNw_WhO-Vb22rAcRvh-eduHqlprtdKcDbyDGxaiOuhzOcTvPUrs-QoyVLDWqJtIlWdB_zGzDj5nKVIMC2yi_eeJslo3PZlAivNrFihaEBiL2I4sn2BStotvSUbUaRvDL9eDIr6bSMY-CgorwQ3_B_RivhFkqjaFkwAbL3XKGoNnFsPJ-DFLp-4z1bVHHuS54KCh35q-b4icZNvELW2rlw8s4j-Bwf7r7MTaBaWfI09YloANzWtA5LCwFKkkVRVs1BRS7CTy22y5Ssmpq5Ws6_tLMWjc_r9MLhXELYkreRYCfSJcmwOswI3S0GSBU7CPCuROITQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeefd4da47.mp4?token=Cvw7gQ-0ItA7sst5TNw_WhO-Vb22rAcRvh-eduHqlprtdKcDbyDGxaiOuhzOcTvPUrs-QoyVLDWqJtIlWdB_zGzDj5nKVIMC2yi_eeJslo3PZlAivNrFihaEBiL2I4sn2BStotvSUbUaRvDL9eDIr6bSMY-CgorwQ3_B_RivhFkqjaFkwAbL3XKGoNnFsPJ-DFLp-4z1bVHHuS54KCh35q-b4icZNvELW2rlw8s4j-Bwf7r7MTaBaWfI09YloANzWtA5LCwFKkkVRVs1BRS7CTy22y5Ssmpq5Ws6_tLMWjc_r9MLhXELYkreRYCfSJcmwOswI3S0GSBU7CPCuROITQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏س: هل تتبادلون الرسائل المكتوبة مع كيم جونغ أون؟  ‏ترامب: لا أستطيع أن أخبركم بذلك. لكن علاقتي به ممتازة. لديه 57 سلاحاً نووياً بالغ القوة. سيكون بخير.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/88170" target="_blank">📅 19:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88169">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb0db0a5c6.mp4?token=o80Zl35i-JLrsE8IM7G0aMJLiXAaFwlD_KF_9qLRgcaUBWyd14nvK2MDA1wnWCw9RmQvfijC4CBKD8-511q1hipGnYIyLHoq1G4pvz_vPmrocOScPU5y_hWM83uUu259PHmCrR_1dhMbmZ-AYZc0wp930u9YyNiOl5yh6cZ8hz0WnHLXzsH3s-pn0YSNjXoh_IEb0R4z1aTUMdqAqI_UzzZ-k9cZ7RWsErlmX4KJUNopukFxBZEBIlC1rC9cL2uon7l5uB7JgIA6y-HOz-shLDY0X4SgkgE8swnD3rcSu8w1o1SASxRz7A4khjkevrkP8HFHZfhQcO3c8Jd5j0y4AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb0db0a5c6.mp4?token=o80Zl35i-JLrsE8IM7G0aMJLiXAaFwlD_KF_9qLRgcaUBWyd14nvK2MDA1wnWCw9RmQvfijC4CBKD8-511q1hipGnYIyLHoq1G4pvz_vPmrocOScPU5y_hWM83uUu259PHmCrR_1dhMbmZ-AYZc0wp930u9YyNiOl5yh6cZ8hz0WnHLXzsH3s-pn0YSNjXoh_IEb0R4z1aTUMdqAqI_UzzZ-k9cZ7RWsErlmX4KJUNopukFxBZEBIlC1rC9cL2uon7l5uB7JgIA6y-HOz-shLDY0X4SgkgE8swnD3rcSu8w1o1SASxRz7A4khjkevrkP8HFHZfhQcO3c8Jd5j0y4AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب: تدفق النفط عبر مضيق هرمز لن يكون مثاليا، والمفاوضات قد تبدأ في وقت ما.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/88169" target="_blank">📅 19:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88168">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇺🇸
‏ترامب: لقد توصلنا إلى اتفاق مع كندا.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/88168" target="_blank">📅 19:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88167">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇺🇸
ترامب عن قاعة الاحتفالات الخاصة به: "سيكون لها سقف مقاوم للطائرات المسيّرة. وسيكون فوق السقف العديد من الطائرات المسيّرة، والتي ستحمي واشنطن العاصمة والبيت الأبيض. أمر في غاية الأهمية.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/88167" target="_blank">📅 18:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88166">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fd7a4575d.mp4?token=Ga0dvf2NAum0QNZBSKXZwbnFxYVyDNem9VRr8I8DMwwdPHihBCPbGchPUPzJJmjdsB-Or2PlYyObOymU__t96q_he_0ZzLBaPS1As8IzDMYDvpJkah9_CcEKKZyX7uSYxy0LmOgXGnl6nSUmPOVwP8DJ8CrLIWN99aIMC9Nuw__keTWoE4RmMrJUmC7jI3QedUjEZzFvfcSQfpL1YZH71kuANUnS-RUlUzaJhOi1szczSbVjrEysaOhOcBN5hhFH0Yxo_Qg1tgTPnAb0_ZQHVzT_bqyDlfg5Vl7BHBlxiELM-mp80hBNwsxiblybBjWQ4yQ_KXpr6InH7-TcnHnbkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fd7a4575d.mp4?token=Ga0dvf2NAum0QNZBSKXZwbnFxYVyDNem9VRr8I8DMwwdPHihBCPbGchPUPzJJmjdsB-Or2PlYyObOymU__t96q_he_0ZzLBaPS1As8IzDMYDvpJkah9_CcEKKZyX7uSYxy0LmOgXGnl6nSUmPOVwP8DJ8CrLIWN99aIMC9Nuw__keTWoE4RmMrJUmC7jI3QedUjEZzFvfcSQfpL1YZH71kuANUnS-RUlUzaJhOi1szczSbVjrEysaOhOcBN5hhFH0Yxo_Qg1tgTPnAb0_ZQHVzT_bqyDlfg5Vl7BHBlxiELM-mp80hBNwsxiblybBjWQ4yQ_KXpr6InH7-TcnHnbkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب عن قاعة الاحتفالات الخاصة به: "سيكون لها سقف مقاوم للطائرات المسيّرة. وسيكون فوق السقف العديد من الطائرات المسيّرة، والتي ستحمي واشنطن العاصمة والبيت الأبيض. أمر في غاية الأهمية.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/88166" target="_blank">📅 18:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88165">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇪🇬
🇮🇷
وزير خارجية مصر:
هناك اتصالات مع إيران تتعلق بجهود خفض التصعيد.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/88165" target="_blank">📅 18:46 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88164">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇺🇸
‏
ترامب
: بناء مهبط طائرات الهليكوبتر في البيت الأبيض تبرعت به شركة سيكورسكي.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/88164" target="_blank">📅 18:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88163">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1a2e4d48d.mp4?token=nG4PYaGmUxYuqzYcfkLg4OHgpiwyeAJaXSAO4PXbfBQai2ZMuKnrrrbLJKhghUpURIAAhKPUoGKr7W-IyNF4ZWkFmafXg2r37EVa0I30tvGviTWQ8JIfEIn_pePZLMsIq9pPa7thtm7TjAAfm_RjsKVJM_6OmZtUpwnIh8rd7OiCf6g1oOhSmZ6A0VdbBigLCenePbP8bqhSIGlSBwBwtcgXfzAT9YPU0U-8AtIUugj4v3jfDE8l0S0L20bM9-GBQCEH3KaLnx7ycMYtmTvZm_1oa0pOlTTkkZ6xBen95k79e0Qj3OapHQWOm95txE7XnnGH31mQ1bW80eyMW90DSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1a2e4d48d.mp4?token=nG4PYaGmUxYuqzYcfkLg4OHgpiwyeAJaXSAO4PXbfBQai2ZMuKnrrrbLJKhghUpURIAAhKPUoGKr7W-IyNF4ZWkFmafXg2r37EVa0I30tvGviTWQ8JIfEIn_pePZLMsIq9pPa7thtm7TjAAfm_RjsKVJM_6OmZtUpwnIh8rd7OiCf6g1oOhSmZ6A0VdbBigLCenePbP8bqhSIGlSBwBwtcgXfzAT9YPU0U-8AtIUugj4v3jfDE8l0S0L20bM9-GBQCEH3KaLnx7ycMYtmTvZm_1oa0pOlTTkkZ6xBen95k79e0Qj3OapHQWOm95txE7XnnGH31mQ1bW80eyMW90DSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
طيران مجهول يحلق في اجواء البوعيثة ضمن محافظة بغداد.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/88163" target="_blank">📅 18:14 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88162">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇶
طيران مجهول يحلق في اجواء البوعيثة ضمن محافظة بغداد.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/88162" target="_blank">📅 18:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88161">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇮🇶
وزارة الداخلية العراقية:
محكمة قوى الأمن الداخلي في البصرة تصدر حكماً بالحبس وطرد منتسب من الخدمة بعد إدانته بالاتفاق على بيع 2 كغم من المخدرات مقابل 35 مليون دينار.
يجب حصر المنتسبين بيد الدولة</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/88161" target="_blank">📅 17:27 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88160">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇾🇪
المتحدث باسم القوات المسلحة اليمنية:
القوات المسلحة اليمنية أصبحت اليوم بهذه القوة تفرض المعادلات وتمكنت بعون الله من فرض ثلاث معادلات هي-
المعادلة الأولى هي الحصار بالحصار حيث فرضنا على العدو حصارا محكما لايستطيع أمامه تمرير سفينة واحدة.
المعادلة الثانية هي ضرب التحشيدات السعودية أينما كانت.
المعادلة الثالثة هي حماية سيادة اليمن والتصدي لأي اختراقات للعدو.
وتنفيذا لمعادلة الحصار بالحصار ومنذ إعلان قرار حظر الملاحة البحرية على العدو السعودي في ٢٠ يوليو وحتى يومنا هذا ١٩ أغسطس تمكنت القوات المسلحة اليمنية من استهداف ثماني سفن نفطية سعودية خمس منها في البحر الأحمر وثلاث في خليج عدن والبحر العربي.
كما تم منع ٤٨ سفينة نفطية سعودية من العبور وإجبارها على العودة منها ٣٤ سفينة تم منعها من العبور في البحر العربي والمحيط الهندي و١٤ سفينة تم منعها من العبور  في البحر الأحمر.
وفي إطار الرد على العدوان السعودي على مطار صنعاء وميناء الحديدة وتثبيتا لمعادلة حماية السيادة اليمنية من الاختراقات لأجواء بلدنا وخصوصا في محافظتي صعدة وحجة نفذت القوات المسلحة اليمنية تسع عمليات عسكرية توزعت على ينبع ونجران وجيزان وأبها وإمدادات النفط في المنطقة الشرقية.
وفي إطار تثبيت معادلة استهداف التحشيدات السعودية أينما كانت فقد نفذت القوات المسلحة أربعة عشر عملية عسكرية استهدفت التحشيدات التابعة للعدو السعودي في الرويك والعبر والوديعة ومأرب والمخا وسفن وزوارق نقل معدات وتحشيدات تابعة للعدو السعودي.
كان من نتائج العمليات مايلي:-
- مصرع وإصابة المئات من تحشيدات العدو السعودي بينهم قادة وضباط سعوديون
-  إحراق وتدمير عدد كبير من المخازن والمعدات التابعة لتحشيدات العدو السعودي.
- إغراق  وإحراق سفينتي إنزال عسكرية تنقل الأسلحة والتحشيدات السعودية في المخا.
- إحراق وإغراق أكثر من عشرة زوارق حربية تابعة لتحشيدات العدو السعودي كانت تقوم بأعمال قرصنة وتقطع ونهب في البحر الأحمر بتوجيهات سعودية.
نحذر النظام السعودي من خطورة الإقدام على أي تصعيد فأي تصعيد شامل سيواجه بتصعيد شامل.
ليس أمام النظام السعودي من خيار إلا رفع الحصار وتنفيذ ماتم الاتفاق عليه من رفع الحصار وإنهاء العدوان ودفع المرتبات ورحيل المحتلين وترك ثروات الشعب اليمني للشعب كله.
ننصح المغرر بهم من أبناء بلدنا بالعودة ومغادرة معسكرات العدو  لأنهم يمنيون ولانريد أن نستهدفهم ويكونوا ضحية.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/88160" target="_blank">📅 16:08 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88159">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇮🇶
السيد عباس اليعقوبي:
سيباشر المشاور القانوني بإقامة دعوى قضائية ضد جهاز المخابرات، والقضاء العراقي هو الفيصل بيننا.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/88159" target="_blank">📅 16:03 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88158">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇮🇱
نفتالي بينيت:
سنحقق تطبيع العلاقات مع السعودية، وإندونيسيا، ومع دول أخرى وسنبني تحالفًا للقوى "المعتدلة" في المنطقة ضد القوى "الإسلامية" - ضد إيران، وضد قطر، وتركيا، وجميع القوى "الراديكالية".</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/88158" target="_blank">📅 15:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88157">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBoY5sZxktNDiH4PINfytrfOuoVz4QCc2jA7xu5nQSM0-5S4ihb5f4tdi2ClA60XCCfGbMjLUy2rEUh-d_LIyD0ngSFav1SQFl0EevaqHZEbwYW-yoNXNFOkUrVAPQBYjAb9Y2CY6zZFBIR_2Yiaj3y8teydvvgBilJzAwBBTWOHTF2jgec-z_LroX2D3nOHcyobkMSpoEgDoZb_GOJakq8Z6tUF00laSFPiFsLIfBfdYM_xaj-EPyc2SVRarM5mP3ObASWt7RKJ6DxmdUydCq62ZxEToh6ZKUJ73SA4GUUYfPUCZWAA66PGwG3G8eoUAI4VeU_MpV9ySxbvOsOZ2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
قاليباف
:
أبو مهدي والحاج قاسم العزيزان! ها هي ثمرة جهادكما ودمكما المبارك.
‏في النظام الإقليمي الجديد، أخذ تدخل القوى الأجنبية في المعادلات بين الدول ينحسر بشكل متسارع؛ فأمريكا تبحث عن مخرج مشرّفٍ لها من المنطقة وبات مشروع من النهر إلى البحر للكيان الصهيوني محضَ أضغاث أحلام. ‌
#أخوتنا_قوتنا
⁩</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/88157" target="_blank">📅 14:41 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88156">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qheXTr3-IVXTnSU5tSOyvSUIp9EOi4Ttt0L-T0Md1JML2FrCOOXzqtp6s8UY-gTkGzBmfKG98rcuqlHwbONZ1PiYgKhYBhTdwdXAk-2E_vPvHXujvutXTTo-YAv7DcPEzsCs9kDSEaceEtYRrgxHtb4a-Pspq11jhOyCE2ju46lxFB95idm4hs-MzqGDICSOlarrpwcQiZpSHcwHTYi-BdL51CoaKPJvA3wDJZKFeAWSG8gJ4MOaq_Zp_wfzLP6rctDl9Vjaebz6cu5zMA_t0tnv4SbXYhl65jQZuCjPy_lgeu52B_mZE8fK-rR1PvKymAFGl1890g13vjrTRwGVmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇶
رئيس البرلمان العراقي يدعو قاليباف إلى أن يكون للعراق خصوصية فيما يتعلق بتصدير النفط عبر مضيق هرمز بما يحفظ مصالحه الاقتصادية.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/88156" target="_blank">📅 14:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88155">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">▫️
هجوم مسلح يطال مدير بنك سيد صادق في محافظة السليمانية ضمن اقليم كردستان العراق واصابته اصابة بليغة.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/88155" target="_blank">📅 14:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88154">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇶
🇮🇷
التلفزيون الايراني:
بدء نقل النفط العراقي إلى تركيا وأفغانستان عبر السكك الحديدية من كرمانشاه. أول شحنة تزن 50 ألف طن.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/88154" target="_blank">📅 13:49 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88153">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKsZafQ8HNhKq8oac-yUN-vLik5Q39gWXDdDSkA8qtGyHBmI1vMgNDvj2HI257KjuKPW2Ng2x9MdrWEik_Uc8ROefCnxEzFWvqUJqlPOZVt4_bDgLug_hRrbt6AIMdC-sl2J5vmrRkgj6R5eqzsgKb3Kjs_1A9gZfPP5grsMLmDdxA8uAHEdh2Yd1VPcZwaP15Q8pSiCex6-N6XEX6vjSVlvKU78VC6eg63MljRRF9ae_XCyugcpkmTig2fcQMVHKAiNdAhgkpFmwsdBL8f_tiM3cql7Guv2DDFu-33MOLoz7x4cz44JcdH4x-EMdzyUGzH9e_OepOWTd9yMUD4g8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
القضاء هو طوق النجاة الأخير للدولة العراقية
استنكار سياسي وجماهيري بعد تسريب خبر محاولة استهداف قاضي قضاة العراق وحصن العراق الأخير .</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/88153" target="_blank">📅 12:29 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88152">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c0c38ef88.mp4?token=WRMwDKmOErJ7o8rryjUnAtdzQLvBzuT17BjuQx7dwx9_NU17P-1YvcKlnl5mUx7ej6AQgerCtvPONV5aDtmXfeo082UKsN-u6fCcydv52Rx8zF35K9pFazLWgwc3X1XP584oY9KzyjA-FtvW1XRTOIqj-Xg7gNDRF1MU_8GUCe1Qs6pCIflyvDCq74tt9LSORlYXcvW9ZfHklCdUyCULBmU_PHcqq3cbfN6S82w9MWDwJiSOfvPBj7QMMjsCwZTO7mbeklh4RqzusKPTpNYuIJfLG8JogC6S_NWKe0yXq79X7ltJnUM5I3hbvPSQED1CgSTeMBVo7BYzGs8AaxD6WrhAtTrCEaGkvSy18umJUJVZziJt8aqxVoyddpX8IMYMUMWukFF2yD6_7p0AFHdfmsFtQujYkSGtQagx0Z2X7QQ3YQn9LwrrXW2iErs9CAajg9r_ai4MA7_NgZ77g1QbjBAdBljt2Jg8xKtdEvOy_B9qYkp1b1ecA8vB352m2xstq7ViwiwTiTFbOUrTs18RFRrdpjyjDEo3TXU5I2qVW8TuwKpBO_8DiNu60XGcdJ46hcCKlvt6NiGLO5LoJ8FRdIn9sM5H-AC1e_tuoKPL5GsGy6nrzIYkBSMtSIGdZD7Fnv0Fs4loGNfGT8PrX8mNcCqAdOKsnBUSS1Nf7cihXAc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c0c38ef88.mp4?token=WRMwDKmOErJ7o8rryjUnAtdzQLvBzuT17BjuQx7dwx9_NU17P-1YvcKlnl5mUx7ej6AQgerCtvPONV5aDtmXfeo082UKsN-u6fCcydv52Rx8zF35K9pFazLWgwc3X1XP584oY9KzyjA-FtvW1XRTOIqj-Xg7gNDRF1MU_8GUCe1Qs6pCIflyvDCq74tt9LSORlYXcvW9ZfHklCdUyCULBmU_PHcqq3cbfN6S82w9MWDwJiSOfvPBj7QMMjsCwZTO7mbeklh4RqzusKPTpNYuIJfLG8JogC6S_NWKe0yXq79X7ltJnUM5I3hbvPSQED1CgSTeMBVo7BYzGs8AaxD6WrhAtTrCEaGkvSy18umJUJVZziJt8aqxVoyddpX8IMYMUMWukFF2yD6_7p0AFHdfmsFtQujYkSGtQagx0Z2X7QQ3YQn9LwrrXW2iErs9CAajg9r_ai4MA7_NgZ77g1QbjBAdBljt2Jg8xKtdEvOy_B9qYkp1b1ecA8vB352m2xstq7ViwiwTiTFbOUrTs18RFRrdpjyjDEo3TXU5I2qVW8TuwKpBO_8DiNu60XGcdJ46hcCKlvt6NiGLO5LoJ8FRdIn9sM5H-AC1e_tuoKPL5GsGy6nrzIYkBSMtSIGdZD7Fnv0Fs4loGNfGT8PrX8mNcCqAdOKsnBUSS1Nf7cihXAc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
عدسة نايا تستقبل رئيس البرلمان الإيراني   #اخوتنا_قوتنا</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/88152" target="_blank">📅 12:22 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88151">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇹🇷
🇮🇱
توم براك:
كنا أمس على بعد خطوة واحدة من مواجهة عسكرية مباشرة بين تركيا وإسرائيل.
قصف إسرائيل لمطار أبو الظهور ينذر بمواجهة عسكرية مباشرة بين إسرائيل وتركيا.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/88151" target="_blank">📅 11:44 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88150">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f0774535f.mp4?token=tyF6MTR5DIolbX_iAZzJWL4l1fv_PZdezWrJIpCM3o4Xfe2RoA6NwuLdM_N1_HPooiMXN9hTX_4xjOH-6sYxbrTDNiTOo8RYVGHTy7XmJuR9WYZv2WVy7rZHWt2dNkikrAry7UBWX4P1lgRC-UOoh12Rr2CtMQ3pBqCNLRGqUtP3k6X6ZMS5cbaAbGe9slNE3KCb20jwHr31cCBXaTMQlctsKAn5QFPNNwlLeqwHuUiFIEvNzIw4dZmWb9c0hEMqHcfzfUoIjVmL1HRHOkGQlVPQZt3mxHQPkAa5D3Lwk9fSaza5av-P3dZ8XgOUi4egC-sMNSeDO8CJLEoXS22jVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f0774535f.mp4?token=tyF6MTR5DIolbX_iAZzJWL4l1fv_PZdezWrJIpCM3o4Xfe2RoA6NwuLdM_N1_HPooiMXN9hTX_4xjOH-6sYxbrTDNiTOo8RYVGHTy7XmJuR9WYZv2WVy7rZHWt2dNkikrAry7UBWX4P1lgRC-UOoh12Rr2CtMQ3pBqCNLRGqUtP3k6X6ZMS5cbaAbGe9slNE3KCb20jwHr31cCBXaTMQlctsKAn5QFPNNwlLeqwHuUiFIEvNzIw4dZmWb9c0hEMqHcfzfUoIjVmL1HRHOkGQlVPQZt3mxHQPkAa5D3Lwk9fSaza5av-P3dZ8XgOUi4egC-sMNSeDO8CJLEoXS22jVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
إستهداف مركز شرطة بواسطة طائرة مسيرة في ولاية طرابزون التركية.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/88150" target="_blank">📅 11:11 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88149">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇮🇷
في أعقاب ادعاء البيت الأبيض بخصوص تعليق المفاوضات مع إيران إلى أجل غير مسمى، قال مصدر مطلع مقرب من فريق التفاوض:
"لم تكن هناك مفاوضات مباشرة بين إيران والولايات المتحدة أساسًا."
أجريت محادثات مع سلطنة عمان بشأن فرض سيادة على مضيق هرمز. بعد انتهاك الولايات المتحدة لاتفاقية إسلام آباد، تم تعليق المحادثات مع الجانب الأمريكي، والمحادثات الأخيرة لم تكن لها أي صلة بالولايات المتحدة.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/88149" target="_blank">📅 10:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88148">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔻
إستهداف سفينة في باب المندب قبالة ميناء المخا اليمنية.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/88148" target="_blank">📅 10:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88147">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇮🇷
🇮🇶
أخوّتنا قوّتنا  مع الزيارة الأولى للدكتور محمد باقر قاليباف، رئيس مجلس الشورى الإسلامي الإيراني، إلى العراق، وبعد المساندة المخلصة والمضحّية التي قدّمتها المقاومة العراقية في الحرب ضدّ أمريكا وإسرائيل، وكذلك التشييع المهيب لقائد الثورة في العراق، ستُفتح…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/88147" target="_blank">📅 10:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88146">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHHz6nqjAhv8GPIFw2o1HhKqkbGBAaNilPL8-plfvkzahrBDc-111ViAt8ttFyzKA-1MOnYQYqm2C6It8ga1tLqMP9pXbjrt3TNkkpDTC4QORKTwNqMu8kAgOVIgkG4oGLB5bE9ffVTgyrG6jn447-5K-Ghto_mVx_MJGUJSn-zUARzFICqG5vv37xa3l1S5XDK7-6ZC-U7e-It66mfo_01-3ft10TNFg2F0zNGRKl3ft4YT0Dc8rf-07tnUtl4cCLYOgWTVHRr4HZHtJKBxqGUkIIlKTtuFNO-5vIItoQ3Fd859puPNzu_UpFdtjcvZuwqk5_fH-LQDWuwE-ygxVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
أسعار النفط العالمية تستمر في الإرتفاع وتلامس 92 دولار للبرميل الواحد.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/88146" target="_blank">📅 09:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88145">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">نايا - NAYA
pinned «
رئيس البرلمان الإيراني   يستخدم مصطلح نايا الذي أطلقته امس ليلا ً  " اخوتنا قوتنا " ليطلقهُ رسميا اليوم من بغداد ..
»</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/88145" target="_blank">📅 09:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88144">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇷
🇮🇶
أخوّتنا قوّتنا  مع الزيارة الأولى للدكتور محمد باقر قاليباف، رئيس مجلس الشورى الإسلامي الإيراني، إلى العراق، وبعد المساندة المخلصة والمضحّية التي قدّمتها المقاومة العراقية في الحرب ضدّ أمريكا وإسرائيل، وكذلك التشييع المهيب لقائد الثورة في العراق، ستُفتح…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/88144" target="_blank">📅 09:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88143">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65250e4c36.mp4?token=E2aa2i52G8A4T7Tv0eEgH09O3m3_OLl8LVohOGiS-UhTAysTkG0qVaSU-ZT4SQ1BSIPIy93Z2EkJwLJgSshZ_zWzRcf-DsZU6DUUNOC89mQHfkqEEM8SwVozNrhRxgbl_VEkD2vC83GQgkz8jYzGPq6aEoyW8HD1jcJSkMwOFRW-uYt0UoQV1zCkAK-z4TBdqaOQQwn5kGSqEAMvjKt9iGemAEJduNcDw1708S6gLUtkbF7Ulg2-KfWGjOHvt31QC-L-aPvlpwARRU62kymRpDNRwRap_TtFdG3vw7HN_KdCGquAo8TqUwBYYqnOITJv_AkcTXYKgTpThyU1ybjjDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65250e4c36.mp4?token=E2aa2i52G8A4T7Tv0eEgH09O3m3_OLl8LVohOGiS-UhTAysTkG0qVaSU-ZT4SQ1BSIPIy93Z2EkJwLJgSshZ_zWzRcf-DsZU6DUUNOC89mQHfkqEEM8SwVozNrhRxgbl_VEkD2vC83GQgkz8jYzGPq6aEoyW8HD1jcJSkMwOFRW-uYt0UoQV1zCkAK-z4TBdqaOQQwn5kGSqEAMvjKt9iGemAEJduNcDw1708S6gLUtkbF7Ulg2-KfWGjOHvt31QC-L-aPvlpwARRU62kymRpDNRwRap_TtFdG3vw7HN_KdCGquAo8TqUwBYYqnOITJv_AkcTXYKgTpThyU1ybjjDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
قاليباف:  في حرب رمضان، أدركوا قوة صمود إيران.  المقاومة في العراق هي إحدى الركائز المهمة ونقطة قوة لهذا البلد.  المقاومة تجاوزت حدود إيران والعراق والمنطقة، وأصبحت عالمية.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/88143" target="_blank">📅 09:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88142">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3e6b038ce.mp4?token=a6Gxudv-fCwSdh9nGsmf7E3FrQBMuJx8v-v12dYEDCjkQoq1FQ91offuXE8yoeI4aytAeLNu7MMg6pIR9Djz4Hc6jkDRJ_WtLAlOc5nRLx8nNQJbqmLUBjL245-qwz2zSJR6dd-fKRuK_kWQI0BTrzXMnJWePEQ3XdQtuZEIIlg9xI2UOiy7MQB_sUzO7hQ4B0Pf3KMpv5mhp19Ihh0nvovG-UWNMSsGXQxLApH9p_eID_48kY9Y3CjQhk-WxvNApvpX9SCmigWCkfXn8C9fVmf2DREfFz3B1vaC5CiHXeSCoaghuVFVr4m0NHGrmZP29PMSX1IjM7TxQUFepctOfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3e6b038ce.mp4?token=a6Gxudv-fCwSdh9nGsmf7E3FrQBMuJx8v-v12dYEDCjkQoq1FQ91offuXE8yoeI4aytAeLNu7MMg6pIR9Djz4Hc6jkDRJ_WtLAlOc5nRLx8nNQJbqmLUBjL245-qwz2zSJR6dd-fKRuK_kWQI0BTrzXMnJWePEQ3XdQtuZEIIlg9xI2UOiy7MQB_sUzO7hQ4B0Pf3KMpv5mhp19Ihh0nvovG-UWNMSsGXQxLApH9p_eID_48kY9Y3CjQhk-WxvNApvpX9SCmigWCkfXn8C9fVmf2DREfFz3B1vaC5CiHXeSCoaghuVFVr4m0NHGrmZP29PMSX1IjM7TxQUFepctOfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
قاليباف من موقع استشهاد الحاج قاسم سليماني وأبو مهدي المهندس: لقد كانوا أبطالًا أنقذوا العراق وإيران والمنطقة بأكملها من شر داعش.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/88142" target="_blank">📅 09:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88141">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7fe5e0325.mp4?token=tpnxCvNsd9Y9-5ddhno_YrzXPDsk6VxpZi2V3ikG8_dvYoGFXjdMIriRel2gMNf1-iup6jhED7Kd5Zt2yNUD6aN-KI4Pl3kZlwSi-zNPv6pdGWM7nGy-SNQFkTEuRkGoUukBQPzCsTQ9QzFj7roP03ckRkn3RqaBK4bg5wnHbWySkn7jp_5GVHG1XprNYd5wLlLoeDbVkWVQ9cywK_IuWr4km0mREGQKouIkVBzYkTaJvz5CbJ7GrVqTQzGkC2nEUuHH5ZDxnP6hsj2DSQ5gDIugn1yakbt0P0T6Bc4zQnpSMYQ8m_AXimjfMPcGGY3z8kvyCCZqqpuuaHQCD9MPhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7fe5e0325.mp4?token=tpnxCvNsd9Y9-5ddhno_YrzXPDsk6VxpZi2V3ikG8_dvYoGFXjdMIriRel2gMNf1-iup6jhED7Kd5Zt2yNUD6aN-KI4Pl3kZlwSi-zNPv6pdGWM7nGy-SNQFkTEuRkGoUukBQPzCsTQ9QzFj7roP03ckRkn3RqaBK4bg5wnHbWySkn7jp_5GVHG1XprNYd5wLlLoeDbVkWVQ9cywK_IuWr4km0mREGQKouIkVBzYkTaJvz5CbJ7GrVqTQzGkC2nEUuHH5ZDxnP6hsj2DSQ5gDIugn1yakbt0P0T6Bc4zQnpSMYQ8m_AXimjfMPcGGY3z8kvyCCZqqpuuaHQCD9MPhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
قاليباف مخاطباً قادة النصر:  أبو مهدي وقاسم الأعزاء. انظروا إلى ثمار جهودكم ودمائكم الطاهرة.   اعلموا أننا وجميع المؤمنين بمبادئكم في إيران والعراق، لن نتوقف عن العمل حتى نحقق أهدافكم، ونحن على استعداد للتضحية بأرواحنا وأموالنا وسمعتنا في هذا المسار المقدس.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/88141" target="_blank">📅 09:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88140">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇮🇷
🇮🇶
رئيس مجلس الشورى الإيراني من موقع استشهاد قادة النصر:  العراق دولة مهمة في المنطقة.  الحكومة الأميركية اغتالت البطلين في محور المقاومة اللذين أنقذا المنطقة من "داعش".   في هذه الظروف الراهنة الكل رأى قوة مقاومة إيران في حرب رمضان.   اليوم الجميع أصبح يعرف…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/88140" target="_blank">📅 09:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88139">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بدء المؤتمر الصحفي لرئيس البرلمان الإيراني عند موقع إستشهاد القادة بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/88139" target="_blank">📅 09:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88138">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVKQoAFDTzPCoPwVy4T0S_V90epb-3lNqxlCvOAMSq3pmJ9Dm1_MRh_zuVbl_8f0iZdy2HaQYWvgDxnMuvgVQE63n9i6t3Oa-tN3cmiDXWgn80WklGG9vIYzIXoy8qGxiszGIOsREvUSWL0rCIRi1e8lkV2kr_hcSMLY0qS4bfCww64PlJ-LS9DD_1i8Yv5nhojoLJQLHvpnjJjKV_Qyg6jdnKHwP10Fu4FYtUJhFRT2BvRe49pojfYlGOfRr1ZgEWfSuqq-UDpSGQWFA7kT8iwCR8qio0RmKkLFz4rlj_ptTYTIvZD9bO-0Jp3JOC7-4wbDDvdVNjYb-5s5SpaxkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
رئيس أركان القوات المسلحة الإيرانية:
الدول الواقعة على ضفاف الخليج الفارسي الجنوبي، التي تصدر بيانات مختلفة تعلن فيها أنها لن تسمح للولايات المتحدة باستخدام أراضيها ضد إيران، يجب أن تعلم أن لا شيء يفلت من أعيننا.
من غير المرجح أن يتواجد هذا العدد من الطائرات العسكرية، وخاصة طائرات التزويد بالوقود، في القواعد الإقليمية دون علم الدول المضيفة.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/88138" target="_blank">📅 09:16 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88137">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_PCiX9YgZVQXHepvkHrpgUTW_PK5hE1wEDmBiCQnIQbQg3WnRbjorPFwTXbqIO_PIIAhe5NEGH5awr_rTUABE868Tb7nfO592Cleia8nTPgcTxBvrMNAzR9BqPrCfTtUih77cQc2gnGyvz_vi00xVF4f9UvrXkULN6xDqywYiFWctuTCAkjCL5I5k2p1cix882aUm7FY3mefC_BfOm_8rP5ktjSagJLYZ2jSt-tybTrjXg-mcMkykD1wgIEDSBLCtq3xq_Poh3oXFXxqi_nzefBWCy4Cd3BWmpjm_GI7Yd2gNTQAKJNjQSj3tKATWBKzXkhxAs2RIfy2GIphy-BVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وصول قالیباف إلى مكان استشهاد  الحاج قاسم سليماني والحاج أبومهدي المهندس بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/88137" target="_blank">📅 09:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88136">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdd61bb885.mp4?token=kNqmV3Bzl8rWEqGGL6I95_Rxya1K_Wvv3YM02GBYO7WxIR1PH-4h9kTsjhcv3PlpcDRAkSju-b0aTpb8tsR9mBPAR8Ho-lYDaPWGkpuHRk97IPHXzNprPAdAtazeig1WVFFuxRdHSEscfE1JUmRDQfAi2M_ocQ0atLWYo8azj0dRXySpW5lc8y0AGjUmwlpT-g-ACNSwH2hI-ArWHzdwkBWJWWgO1W_VMnf1CZ6OceozNHs2mXf97mNRencnkVIks4o0iapn4QA7BC0Q8r4Pb19PgWJYgEzIex4Jb7ume3SLa3jwVz4qAKXJHecBWG_OVjawAfMHxdSwb87lSdcRzDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdd61bb885.mp4?token=kNqmV3Bzl8rWEqGGL6I95_Rxya1K_Wvv3YM02GBYO7WxIR1PH-4h9kTsjhcv3PlpcDRAkSju-b0aTpb8tsR9mBPAR8Ho-lYDaPWGkpuHRk97IPHXzNprPAdAtazeig1WVFFuxRdHSEscfE1JUmRDQfAi2M_ocQ0atLWYo8azj0dRXySpW5lc8y0AGjUmwlpT-g-ACNSwH2hI-ArWHzdwkBWJWWgO1W_VMnf1CZ6OceozNHs2mXf97mNRencnkVIks4o0iapn4QA7BC0Q8r4Pb19PgWJYgEzIex4Jb7ume3SLa3jwVz4qAKXJHecBWG_OVjawAfMHxdSwb87lSdcRzDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
لحظة وصول رئيس البرلمان الإيراني محمدباقر قاليباف إلى مطار العاصمة بغداد وإستقباله من قبل المسؤولين العراقيين.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/88136" target="_blank">📅 09:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88135">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇮🇷
🇮🇶
رئيس البرلمان الإيراني محمدباقر قاليباف يصل إلى العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/88135" target="_blank">📅 08:55 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88134">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ebabbf606.mp4?token=qyq3cGnrR_g1ZUEI9MSZ4OVVhXjsBubQeFyJPFPvxgk1PTB1uozzI9P8QiN6zAj1pP2SOBuAsUiFQoExSujejoEy1D3bhfPdheYkyEWF2xs58yqAM1CgQ9UqR7wSDVtyT-Px_O8f9nqiEJQ-BqZ2gfbPfVwE15f-m5QrZDoXWV9d-KROz5KqJlPtzY4k330G4gDNF5dJbY09ClI662dWCyb-Jqtrmb94te9YeQLsQCY6_O2Vxz9a7ybznGseuQh5AKO8_kiAzrOj5uqFDK0_v3WujEKzlxwdZTzt8FPcXS7xtUSD8jnT-9XRVy7eHMm3OKiIbn33FJtJN1Ifa4D1BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ebabbf606.mp4?token=qyq3cGnrR_g1ZUEI9MSZ4OVVhXjsBubQeFyJPFPvxgk1PTB1uozzI9P8QiN6zAj1pP2SOBuAsUiFQoExSujejoEy1D3bhfPdheYkyEWF2xs58yqAM1CgQ9UqR7wSDVtyT-Px_O8f9nqiEJQ-BqZ2gfbPfVwE15f-m5QrZDoXWV9d-KROz5KqJlPtzY4k330G4gDNF5dJbY09ClI662dWCyb-Jqtrmb94te9YeQLsQCY6_O2Vxz9a7ybznGseuQh5AKO8_kiAzrOj5uqFDK0_v3WujEKzlxwdZTzt8FPcXS7xtUSD8jnT-9XRVy7eHMm3OKiIbn33FJtJN1Ifa4D1BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
أخوّتنا قوّتنا  مع الزيارة الأولى للدكتور محمد باقر قاليباف، رئيس مجلس الشورى الإسلامي الإيراني، إلى العراق، وبعد المساندة المخلصة والمضحّية التي قدّمتها المقاومة العراقية في الحرب ضدّ أمريكا وإسرائيل، وكذلك التشييع المهيب لقائد الثورة في العراق، ستُفتح…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/88134" target="_blank">📅 08:27 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
