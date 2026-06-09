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
<img src="https://cdn5.telesco.pe/file/llK7IPcic6konEPbVGFxlEjg5XxBRTDtANNjc6nAKnpw1qBD3rJLmwSkSzBL2Fimt7EzXMHkFsnJXfZ1HBDDHHTT_vo6S8de0DXo0RpXETArp5Viz_5_Sbjmn41zy4rUV5-BdG73iXAjDIOI8paJvoEyvbqtGbjNVOZ4KiqKGsz_RGS0XZCuTyjTG-2oyiGkoBtApPEygPkYLwDfEzNhtHDxKbzyktig0B8iE8Xd-JbxkKcscWo4U9Ueua8d0-fZhzW65gIBxZ9vLu7w30nf6YeaWXAuechbYkDyqPwU1Itk-NdvvBLuhBhBsVrwp8QXgzrVbg21dIu4Cw7K0PqPYw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 297K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 16:54:32</div>
<hr>

<div class="tg-post" id="msg-91691">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
#
فوری
؛ پس از اعتراضات اخیر دانش‌آموزان، تاثیر معدل سال یازدهم در کنکور مثبت شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/Futball180TV/91691" target="_blank">📅 16:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91690">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78f1cc690c.mp4?token=tKPTJHPFfsmtTv2fE2A_NGYGWS-4y1JgotNHwwMsFHlbzEj1wn4mkM2p1YGhstne3fa8D9i0MEnEXQabedBK9ZwLTyqX93rxlLAmVn3EGoxCefTuV-1hQS6VQdyfrX0aLJgwfUvegQLCuD83TuVisNVuSWy8OfIS3fD2oqXukr12aY7MPZ1A6hzGhAUai3cTks4mmBRnPRwABddbA0ZPHd9WcVdrzPKV0sS08PDEbVcCVbwJZ7yOYF64fYi0nTsotfTQtBO5uhHr6rIbWPFzmxczvAZB2uZKowWmpiU77kxwpSrQCAJ808UJ3O7pP1uQ5wsONijOjyTbbLaqK9n1zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78f1cc690c.mp4?token=tKPTJHPFfsmtTv2fE2A_NGYGWS-4y1JgotNHwwMsFHlbzEj1wn4mkM2p1YGhstne3fa8D9i0MEnEXQabedBK9ZwLTyqX93rxlLAmVn3EGoxCefTuV-1hQS6VQdyfrX0aLJgwfUvegQLCuD83TuVisNVuSWy8OfIS3fD2oqXukr12aY7MPZ1A6hzGhAUai3cTks4mmBRnPRwABddbA0ZPHd9WcVdrzPKV0sS08PDEbVcCVbwJZ7yOYF64fYi0nTsotfTQtBO5uhHr6rIbWPFzmxczvAZB2uZKowWmpiU77kxwpSrQCAJ808UJ3O7pP1uQ5wsONijOjyTbbLaqK9n1zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
دیروز وسط‌تمرین یوگا‌ کف تهرون و صدای پدافند؛ چه ترکیب متناقض و عجیبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/Futball180TV/91690" target="_blank">📅 16:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91689">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/871f3caa0a.mp4?token=c0oa4eQDsnmCBiu2qvGwpGwDHBqgD0MjfPzso4fpEXlcFGA9vC-t-zzXySsr81SzEIY5bmPHGYp2jExf8twxi1kh0gYxjnt6bdXW-t5WqLkO9rSBLrBEYMkd7t1epMVgG8US3ozjMBUrnsWKptDoU4SUWjSG6fN1y3orv0OkRtHtV8Amo45uXzVHlITIh7sphZ9_aFs-AntJFthCOtsYnXbaPJta6QoatTCIGMJDdiShKN3GSBmrX6LULQkKhQeaPG3NTzWU0M2WoH-jWUUNBcdp-_KTXqxhBlnrF3EArkpY7WW17miOFLdkwpAeNH8j48YzQvnZxhIyAmT2dbEIOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/871f3caa0a.mp4?token=c0oa4eQDsnmCBiu2qvGwpGwDHBqgD0MjfPzso4fpEXlcFGA9vC-t-zzXySsr81SzEIY5bmPHGYp2jExf8twxi1kh0gYxjnt6bdXW-t5WqLkO9rSBLrBEYMkd7t1epMVgG8US3ozjMBUrnsWKptDoU4SUWjSG6fN1y3orv0OkRtHtV8Amo45uXzVHlITIh7sphZ9_aFs-AntJFthCOtsYnXbaPJta6QoatTCIGMJDdiShKN3GSBmrX6LULQkKhQeaPG3NTzWU0M2WoH-jWUUNBcdp-_KTXqxhBlnrF3EArkpY7WW17miOFLdkwpAeNH8j48YzQvnZxhIyAmT2dbEIOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو ازبکستان روی سکوهای استادیوم یه‌ پسره اومد اینجوری از زیدش خاستگاری کرد که دختره کاسه کوزشو شکوند و جواب رد داد
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/Futball180TV/91689" target="_blank">📅 16:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91688">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa9aa48bcb.mp4?token=XOhH28LXskNzg1nnyTUslpV1_Qzgu6l2XSV2n_LPp3nwUPqRunqx3xmmYTQV7FtTmkQ2Jj6xplO04AbiBCM0_Fiq-hk5m1yPKTrXYQcvHVXT7o-TuppNWkXfOVjsrJPmZ9yoefZYzwQMZiaKJC35u3J0rI39fHPamI5R2UA_NOVQtu6dERY5OcHyhe19r_0IdgfKvfQUrU8Z6VIMfgB5EsY7q2q2yA9uRBFNIuO4o0LbH-Ww4BE60k5ryKUKnFlFJCbYODH4BBB0VRB9TOvZyVczLTXvUWnNrKRfsVZevsteKZ1igH7uUxdcpgkc1l3Quvx8S0fRUJG2-qoft6k1dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa9aa48bcb.mp4?token=XOhH28LXskNzg1nnyTUslpV1_Qzgu6l2XSV2n_LPp3nwUPqRunqx3xmmYTQV7FtTmkQ2Jj6xplO04AbiBCM0_Fiq-hk5m1yPKTrXYQcvHVXT7o-TuppNWkXfOVjsrJPmZ9yoefZYzwQMZiaKJC35u3J0rI39fHPamI5R2UA_NOVQtu6dERY5OcHyhe19r_0IdgfKvfQUrU8Z6VIMfgB5EsY7q2q2yA9uRBFNIuO4o0LbH-Ww4BE60k5ryKUKnFlFJCbYODH4BBB0VRB9TOvZyVczLTXvUWnNrKRfsVZevsteKZ1igH7uUxdcpgkc1l3Quvx8S0fRUJG2-qoft6k1dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکم رونالدینیو افسانه ای ببینیم
❤️‍🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/Futball180TV/91688" target="_blank">📅 16:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91687">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/813a70ddec.mp4?token=LE1rw-0Rz4EdBgPfvi5mjgbKLzePJm1GGDX4Q4E5HffTShEPN22kx5sdzwqOdC2_pFITYmY1T09ziBBA45tgTKVGb9vMcPqPj5Brt1-KBLvsivN68udzVhDLMZw9z_OifL1moa_0QsoqRv-GE4LQfiupVYYFAxjLcX0UY0_bkLBkmYGKSoyTJuFt39WfUNazFcjpufXOoXrgcbH6oyxv7Vj2b8XBXOnjBi7b6166GZhIYshWReBNvw1d_ECoOFXLzmcLlz4J0lQYeWino4tExnZmaczAsoJznPfNBCyMABw39BdXIrcUw3dej-sN_FHXXJaA8LcdJYWxrXitpBjyuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/813a70ddec.mp4?token=LE1rw-0Rz4EdBgPfvi5mjgbKLzePJm1GGDX4Q4E5HffTShEPN22kx5sdzwqOdC2_pFITYmY1T09ziBBA45tgTKVGb9vMcPqPj5Brt1-KBLvsivN68udzVhDLMZw9z_OifL1moa_0QsoqRv-GE4LQfiupVYYFAxjLcX0UY0_bkLBkmYGKSoyTJuFt39WfUNazFcjpufXOoXrgcbH6oyxv7Vj2b8XBXOnjBi7b6166GZhIYshWReBNvw1d_ECoOFXLzmcLlz4J0lQYeWino4tExnZmaczAsoJznPfNBCyMABw39BdXIrcUw3dej-sN_FHXXJaA8LcdJYWxrXitpBjyuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
الهه منصوریان بعد زد و خورد شدید و فدراسیون ووشو: من در برابر بی عدالتی سکوت نخواهم کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/Futball180TV/91687" target="_blank">📅 16:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91686">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76ea15ec78.mp4?token=j7YLHWyzPl0MN45pCmEwOXHa9vBawr5dweme1bfc2VwNbvmV6CgXBwtu1GEJMkOLqxEDkUvjExrNeZDJMRF9EQ48NzTx-wZhA1LatKHhdXzY4EYoKkTQBp2H0IIPltZFY7DTdpT1YI-zmXiu-zfge6CZI6IQ18JdhAlkiqyCYbO9zVziApeax9y9yKxdNA4lFC6jLPOjOI-vkprpf7rBQO5dTTKBSVQpHSAz4xRAxIwdf7VjJ0wXxzYMyy5Heq4uMSPhDLRnXKPpLyvbhWa2gWp-ASqJXSUrijjFADmoo-XBhBdF0k3HNDdhY-FOizIVvXystR1tknoWKS3z3DsODw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76ea15ec78.mp4?token=j7YLHWyzPl0MN45pCmEwOXHa9vBawr5dweme1bfc2VwNbvmV6CgXBwtu1GEJMkOLqxEDkUvjExrNeZDJMRF9EQ48NzTx-wZhA1LatKHhdXzY4EYoKkTQBp2H0IIPltZFY7DTdpT1YI-zmXiu-zfge6CZI6IQ18JdhAlkiqyCYbO9zVziApeax9y9yKxdNA4lFC6jLPOjOI-vkprpf7rBQO5dTTKBSVQpHSAz4xRAxIwdf7VjJ0wXxzYMyy5Heq4uMSPhDLRnXKPpLyvbhWa2gWp-ASqJXSUrijjFADmoo-XBhBdF0k3HNDdhY-FOizIVvXystR1tknoWKS3z3DsODw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بازیکنای برزیل یه دروازه خالی گل میکنن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/Futball180TV/91686" target="_blank">📅 15:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91685">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfdTEEQ1z0SxFlJZu6_fus4wzp7ikHpvu_QckU4NhECW8djBcxfk-8RoC1no0_M3HEaCxGoJ0Q2Wf8ss-53jXh-jCwMKLdRzcCTtLkkyAWhD7tUsQGnLnMi82iHZd4KbA-_gz9khfw2yOL3i5qb_jj0nfMggl5TGRhSdMNKVMGCHkv1umJNsVhvSsvPvUSkkvqdlPEL8vGAT4oQn7BNQXjlzFOaQicNnRVdMtg55zyWMUG6GpadEd28jsqXv_DVwDryVQSlHVGCtB06MdacjystJVZ8F4i_iLK5gf9zFucOpJxHIAFLQgaaUv2ewVZSMTDr_Ch-UHNhqM22sV4L5KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مورینیو وارد مادرید شد
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/Futball180TV/91685" target="_blank">📅 15:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91684">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd169632cc.mp4?token=Z6iVhDlumtaKWb6TiTjs7fgQaeDaNBN3kWvTVxWodlWU3GtxCOzP2Ltg-uUmNxFodcoK5Pmjkv-U7RYW2JVcSvMJa1TylVg_bP8QCf9ViKtdpOBNZdU6OJNUIASMPmjXgA3ESZxClOEZT7fbPLcEx85WEM54XJFl7XDGyhlZxc1AvKXMlVT97VuwyN5SQsWE_2err-WxXzgJPwKD4PhCGK8skqyFeQ4KB15AoJwt03tIPd9tRgkTblfGKLNZ1bIg-4FgDx6UF6wNYOfyFT6RzVvN2HMzj_J_2wdMxgiQXnkUw_JyAhDhxAlNY5WwQs8WaoqDFV6SHxi0kvuvZkhQRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd169632cc.mp4?token=Z6iVhDlumtaKWb6TiTjs7fgQaeDaNBN3kWvTVxWodlWU3GtxCOzP2Ltg-uUmNxFodcoK5Pmjkv-U7RYW2JVcSvMJa1TylVg_bP8QCf9ViKtdpOBNZdU6OJNUIASMPmjXgA3ESZxClOEZT7fbPLcEx85WEM54XJFl7XDGyhlZxc1AvKXMlVT97VuwyN5SQsWE_2err-WxXzgJPwKD4PhCGK8skqyFeQ4KB15AoJwt03tIPd9tRgkTblfGKLNZ1bIg-4FgDx6UF6wNYOfyFT6RzVvN2HMzj_J_2wdMxgiQXnkUw_JyAhDhxAlNY5WwQs8WaoqDFV6SHxi0kvuvZkhQRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گاوی اینو با این افکت صدا توی تیک تاک آپلود کرده:
صبح بخیر عوضی فوق العاده؛چه حسی داره به عنوان خفن ترین
مادرجنده
دنیا بیدار بشی؟
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/Futball180TV/91684" target="_blank">📅 15:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91683">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0ie8OM9GQ23vUsxxU73IqEJyC_vev0c89Bu0KufxutDh8rj4UwRw55Z6A2yxfWnGCN2rV64CEgdP8Aye-TR3hC6T1vbYHYuoJ48HNYd2EXYMJs-5iW3KF6TAiZ1SNXrYl_cEIDW3Zco5x30nJZe-clAnrh5X8PExN7Uikgfq3IUUZ8Trg2oL_BBSI-YGVmmoNxH5npx8bBKCXAfhK_plA6VA8GAxR_IYjLHJQvE6drfkgv4FVEb9HrNS3SVadZCNpt2bbBjSudUkbra_giBVIlyy9a65I4-tqI-uMgcWGFn4ruVUO-_anZ_KtUawGAI58_GnVrmHb9zzshVtIaBXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🔻
خوزه آلوارز خیلی نزدیک به لاپورتا:
🔻
بارسلونا همچنان روند جذب آلوارز رو دنبال‌ می‌کنه. ۱۲۰ میلیون دلار حداکثر پیشنهاد بارسلونا برای آلوارز خواهد بود. مذاکرات در روزهای آینده انجام خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/Futball180TV/91683" target="_blank">📅 15:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91682">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAyMpZnL_zpYfjlJ6A_7SnSJBLrTOX67u1IuhBwJmHeTo20HIK1qmbQxmZSN5t_bI5Yt3rGDm8loNWwiCSKAognq1hzJqTHjAImrJ2vrO855kXHPG9znCAs-HoVEIULvbqGyC5GlV7L2r_rYxluPpOKMv-Gj11woXvkoOB6bPLWX9fwm4Ipg4iYn6vS6CQbO7lBxgBJUjCMrOWgfqkhStSate1_0Wh4D_NdV01Tzg21ZA_GR8p7YqW6HGr2aQGn92SFlK99GxiCg_orNQA2nLM4VyG4Gg6VHE18yhTerSIOen1UPXbxMHtlG5II62Bw92KcAX9xqLxKQogb6x_CyFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
خدای جام جهانی؛ زاگالو با ۴قهرمانی جهان با برزیل
🥇
۱۹۵۸(به عنوان بازیکن قهرمان)
🥇
۱۹۶۲(به عنوان بازیکن قهرمان)
🥇
۱۹۷۰(به عنوان سرمربی قهرمان)
🥇
۱۹۹۴(به عنوان مربی و مدیر فنی قهرمان)
🥈
۱۹۹۸(به عنوان سرمربی نایب قهرمان)
🏆
اوبه عنوان بازیکن، سرمربی،مربی، مدیر فنی قهرمان جام جهانی شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/91682" target="_blank">📅 15:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91681">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d15a705f7b.mp4?token=QZgxDYbP-ZkipTiOm2rOnoSlFtzoEAkrzPrnjXEA6BjbMqdfUlcDHFALQlK4AjW_VE71xhdKmpZJwVkeGYOnt65WqjeUpEtkhTTmJzUiypxxxS_riuAWAsrjX6r4l3LFCUINbBGKyDaFRXZqjhxLFkFoFhzJVDEGQcic2jI1tLAvI8PUfC_FIPm7rYT6OUZ6AZ6_iFbAT6G3RdpCqZj7g4IFJLON1HmXwg1p4_0S2EaovyyUDjLhhP-5WuU9xkOXL0X0Ebvu4zo8rX8I2kz_olkV4LwSKTPu8Ewyh4l2fjKSYLi6PK-ZRstHjMXIOlraCafuIHFmSYCKfP3QjMVYRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d15a705f7b.mp4?token=QZgxDYbP-ZkipTiOm2rOnoSlFtzoEAkrzPrnjXEA6BjbMqdfUlcDHFALQlK4AjW_VE71xhdKmpZJwVkeGYOnt65WqjeUpEtkhTTmJzUiypxxxS_riuAWAsrjX6r4l3LFCUINbBGKyDaFRXZqjhxLFkFoFhzJVDEGQcic2jI1tLAvI8PUfC_FIPm7rYT6OUZ6AZ6_iFbAT6G3RdpCqZj7g4IFJLON1HmXwg1p4_0S2EaovyyUDjLhhP-5WuU9xkOXL0X0Ebvu4zo8rX8I2kz_olkV4LwSKTPu8Ewyh4l2fjKSYLi6PK-ZRstHjMXIOlraCafuIHFmSYCKfP3QjMVYRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مکزیکی‌ها این ویدیو رو‌ از اعضای تیم قلعه‌نویی منتشر کردن و‌ نوشتن که تمرینات فوق پیشرفته ایران در اطراف استخر برگزار میشه و اینقدر امکانات اونجا درخشانه که رو دست نداره
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/91681" target="_blank">📅 15:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91680">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a39f457cd6.mp4?token=OJPqIFn8GxDVrCn4jcTqYxpTPNNt-yF2YaiJZE1Thd8F4JghBp113I6wzIVxA3k-1NdB_f1BX6WGr4kEwhvyUBpMI-qB-n9tsI5zFzoyIljT7hMoYB21IjwhhFWw8gOn-2rRrDYT0j59S4wiTafaj_hsGL5Cd3hwo46_Tk8ZWDMDQ2BaGfngfhEs_9vp3D1pwx2r54rTSseygeyc6HZffLpMO006r1FCi79LGnurt5hKTbT_bXkOrMU0ZN-nM115McZSzo2kZpQ7VVs1sKsXXkRCJZYMNgbtGL3LROjexRKfTj_g1H9iI0aLyQDwUi0-jyda0TEm9ONXhhLbduoz-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a39f457cd6.mp4?token=OJPqIFn8GxDVrCn4jcTqYxpTPNNt-yF2YaiJZE1Thd8F4JghBp113I6wzIVxA3k-1NdB_f1BX6WGr4kEwhvyUBpMI-qB-n9tsI5zFzoyIljT7hMoYB21IjwhhFWw8gOn-2rRrDYT0j59S4wiTafaj_hsGL5Cd3hwo46_Tk8ZWDMDQ2BaGfngfhEs_9vp3D1pwx2r54rTSseygeyc6HZffLpMO006r1FCi79LGnurt5hKTbT_bXkOrMU0ZN-nM115McZSzo2kZpQ7VVs1sKsXXkRCJZYMNgbtGL3LROjexRKfTj_g1H9iI0aLyQDwUi0-jyda0TEm9ONXhhLbduoz-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ دیشب رفته بوده فینال NBA ببینه که باز انگار تو حالت چرت زدن سوژه شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/Futball180TV/91680" target="_blank">📅 15:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91679">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrJ9Eqjvf19C8yxXxnGtU79gWUkA1U3q_nzEvtKkfnLbEofavlHB9F5soT8zTgFcaQsxS-LFEFcDGtErTeYQFP3wNEk-mGT6e2AnkRUrNiOS7JC81BtT_JYdcOGNlQWI6EDBMjPQ-QkyLuBAXxb5UjRwrxPNKxpyQyjCkw1pnN_vwWCgJpolRQT9nO9BjrdSuJij4NUKQ7UlnYlLSi4qVnbuJ2lUguwL6M4rHVUmLHeysmywOOQwALBgfnCCJKwUICa-GuarGs8-nM6aXXiRNCOQrQyOYmJ8SVCAli8LOHud2WdrfAP7z3smVIgpoIaKU2TkKyKvH9px71k7XNqwsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
دوست دختر رودریگو دی‌پائول:
«بعد از جشن قهرمانی آرژانتین در جام جهانی، رودریگو مست به خانه آمد. من مجبور شدم مثل یک بچه از او مراقبت کنم چون نمی‌توانست جشن گرفتن را متوقف کند. به او گفتم که دوستش دارم تا آرام شود. سپس او پاسخ داد: «من هم تو را دوست دارم مسی.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/91679" target="_blank">📅 14:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91678">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🏆
اینفانتینو رئیس فیفا درحال خط‌کشی استادیوم نیوجرسی آمریکا در آستانه جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/91678" target="_blank">📅 14:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91677">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rbf-g6wucchLW3Y89XDYZEkr00CG3Cuie2Tn9jFsb1QOqB0UXT6b1Si1CJpbsUgfbds6prJ810eW-H2bui6_M5T-MamiEjkGjfcggNUMzitK6WhMlPXoXqw_9s6HCR84whmD4ggzVFChwxyZiHB5_jOFgWErdurNGTUTTLD9c-I_LGA__xj3xYs28vAnWHyNzXjgVwxpH7mI1fUxgDrHTfgpvASXHX7son_Xji04lF9sxgy7KBqsTASAuggwllsjrnAQ4HkF9apb_B2fqq41E7zXDogHcDs18V-vPnQolagDivgqWLL93ti_jA_5utZKmbq6c-y6dpgJt5n-Z0-xlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همسر نیمار به همراه بچه‌هاش یه ویلای خیلی لوکس و خفن تو آمریکا اجاره کردن که تو این یه ماه کنار نیمار باشن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/91677" target="_blank">📅 14:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91676">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">📰
⚪️
اسکای اسپورت: هدف رئال مادرید اکنون قرارداد با ریکاردو کالافیوری است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/91676" target="_blank">📅 14:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91675">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJJkSn36yijw7Yg9TBTWATdWGSxh7GI90jdVmgU7l-KdskFZ5GB40iqUMQTOU3JokGPPUDWRabXqmgs2a6m_-TpbIUL1Ix9tN5Gzs8pzzGDew5mqM7VgZ9Wf_9werJXFC_17bYavOFdehQMttVB1KQd4YZk95MgKAFpek1dbOZnjT_KHzxc0pDqpWSjN4ozi3-lFBQ--GBac7Xv414f_SRBOILVbHrjK9gXiUJulEOQD8sbPyfGZor1ep9eT7YVb3NOB-lnjFheJKU4J1UUSHByEQ2GQr_naGTrNkDWygnybL9izvISW86BRMwT-w-R_ng-Nw05yWqKpmHq7ENhPow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
⚪️
اسکای اسپورت:
هدف رئال مادرید اکنون قرارداد با ریکاردو کالافیوری است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/91675" target="_blank">📅 14:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91671">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qx-ZOtRTbUydYNYIJjPvJpJjI4DNWkZ7jpACOy7Ncz1fwrGnHmZ1X78l2uiBO6hHi1fWd5zeR-RoC7I62dxbUXmMkuUBFj-Ydc0qTwXCwL9znp5WBy9boPRuzvmDFxwzMQtOtHdsgTYMwlNDkx0k6gS6zVf3HExIyzdBpFf3Ji064ES2C7z2ZO-G_BS-6MyNnUxegXVWqV8tMXfEA3qv7y5VWqFHuzMtXrBXcQqHh05MJjikzBrXra_NUMft46wTvsTk8F5T4DEql2yuHMXOB1rJHIMsxLazUs7-TWkhBED4uK6cA-YqoHJpV34t96M8gb27giGExr2-B3-QFqAfPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ntVOE_DzHcTVCWWQD9PL1oDw7i_J3GgWAuaLiAUMWiNOm66zfXklHCuKYj_rfpe17blY1eWxVNwZEOpCw94fI1MyZwIBPct4hjjZuE4yTbSKp_4naS45Usyk0wiQbVfy3nSygn-LVgdZ2F3QZFNGqn2R_KZ8IqUWC2MLj48nMFmOszl8JWAki6K2TXwNG6Itbipek1qZGPEepY_i_79QZZBETm9-SHZkrsLMkuzBoFenJF-QnoziQjNjLUAQgFhtPJk1CIg6-yqATG3Pgb81R5WF4ITP00PG1OLO4uxJw--bA1qHuzn059VD_YDoEqKwB_J_-x8MbvvB3Iz7qnIKzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u5mzdCf1ZSF3kW5Ykovu_qiiGDpvvhlYX-M7AsYUmxoibdiYlHPguCgdz7fbgwMQqhMSjPuFdVRJ8L1gM5Hx-UrnIlUFxFwUhlahMgaR0IiYjZEP1jpQYwkLlXxpODIEtA3ioj-BFIuiScxSt9cAsEvKrLxbyKn2JoR9Xj0_xefUWEDHOMV8ty_aa-POYXb594om4T3rUIhaYbqj_lqs0E5GUh1JOvH3D8sUDpIyITYupuhHze-xgGdqPfx1WUUOcLGQ4uodOBqp42H3bAdcQMqa2YuIibCksQLPzo7MQeOlrkoYeHbePdjl9VCC6aG4ZefqdX7FgxnBg2-18mVU_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CLkx2SNjwx-8ESfJdqB2kB5hQp3_jWg0HFz57DbstZK0n_91tkSQV1D-UNAQPmHoS53T8d1zTVoEJycKVMSda1e-W3_YBk4K_kCeEMrRYc1pKEkBAnKWtzki6ZQcXG1OLEOEjPhATTx7b9qLSyAgv_15VduVi2QDAe6PViG9YiTb9QuYv0Ls84mbvzl29HdwZprOSsC9rDewEG7ItdB_kGP2G3EIEVcbVDc3JNaSHP0yRUb8Zz3hi7ghJ3nN02jSpX_JEIo71lTtjB1fcFS8AC7db_aOJgEBfEBLozDsQZnNE7QjBcTvbntVeqJ4_PQpZPDTmtYiMkHu4vbZhYF0Yw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مجری داف و جذاب شاختار هستن.
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/91671" target="_blank">📅 14:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91670">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f43f043a30.mp4?token=XViQWDVAwDbK-J8sBXu3fJav4MXCoU_bSoWwOAmUpMmvNsWnshBNSYez0weKTG9441e0ACl0D2F7zfB9BInQO37d7j_-0SGA5W0xA21zbQ7ps0IOCUJOI_u47nrbd2dTLVq5PO8_qh1s3xpSKVPHCEklQbLnS60S9VrHHBiQsAa_AAZhxdyzl6Wy9BlSCUBCNKe7asGpnfNsZ01bL7-CUDMDyOxM_QujbCtwJWokzp57-SgaPtrTjkRJ63JjzTdfdSRBT1EJkwc9b2mYfqulyrbke8AaPcNx-_HZbyQOzO9_rSAlWr3-bBqdz1legkVyDpRVnX_lLhX2zLrgY7qUcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f43f043a30.mp4?token=XViQWDVAwDbK-J8sBXu3fJav4MXCoU_bSoWwOAmUpMmvNsWnshBNSYez0weKTG9441e0ACl0D2F7zfB9BInQO37d7j_-0SGA5W0xA21zbQ7ps0IOCUJOI_u47nrbd2dTLVq5PO8_qh1s3xpSKVPHCEklQbLnS60S9VrHHBiQsAa_AAZhxdyzl6Wy9BlSCUBCNKe7asGpnfNsZ01bL7-CUDMDyOxM_QujbCtwJWokzp57-SgaPtrTjkRJ63JjzTdfdSRBT1EJkwc9b2mYfqulyrbke8AaPcNx-_HZbyQOzO9_rSAlWr3-bBqdz1legkVyDpRVnX_lLhX2zLrgY7qUcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
صحبت‌های عجیب و کنایه آمیز شهربانو منصوریان: من راه میرم روزی ۵۰ میـ‌لیون درمیارم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/91670" target="_blank">📅 14:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91669">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🇯🇵
تیم‌ملی ژاپن کمپ تمرینی خودشو که داخل مکزیک بود بخاطر شرایط بد و‌ امکانات ضعیف به آمریکا تغییر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/91669" target="_blank">📅 14:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91667">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R-H7AJzN1UZ9spTNVBKVBdvzrbCZCmD78nEWpKmWniL4pZ2Ew9DBa_D7EBwjnYwf7k1-yPMECGS69iueeUgEXeTkzOjSyMV6xR4FhkzHhNK116BlmikfelarFY6KHq_BY4ANacF8ErD1pTAYF1e1oLuV9uUEEM3z9y2WTCW3LTJgJWXGRuP8fNkRMc2btWE06Fx6FG80xP8KlZQdvAwC0kdhJfSshjXXMhDvFcxU3dhXSJp8VluCty_QluUVo8LJGznn8Mn3qb0ZsYwzlsK8-4Fw33-VTU3emRbPBtdhnaY3tbqBYUjhuhU4H0Ht10InlWqcWWYDTsMA1WHuhR5iGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e9H22heNcryHUAi5eIJ4yskytAu-hhIkm3I3XhNFUj5HPDF3etljOv3KiDWlxyeiJ4NNQkwcHIRkxa5aEbHnqbMahrHB87pKrQ-DTP6CwFaOG_WRyWDAh7PDj3RLButQrfEyO7lLWHzQafJ1P1AiaBHOJejnRhQqzOBZCLgSCm_VPsuC6khcviOImPr9DvRx658O_MZbLP0szAANywVFf0ZDxYjRzSfTFO6gR-hC0ADOA0s-7gy_ZXH2F1miJAABApeFrOvFG2WNW2ctCoWobZKDFM4S_O6LgvFbm6nDF_OP4y8MKRcIBv8xdMeFhxmWPe70pWsp1NQRspcalG8B0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
مسی قلب‌ها تو تمرینات آرژانتین.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/91667" target="_blank">📅 14:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91666">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gLt1KVheIGQD5Zb9fOe1ouZ_wIasXMXetC567a6SdC9wWbM1te_srB5aciFkdDDP8Z_BtOw1VBKcDwYSeSv3TwfVXg7IaDAsACNk_wNOlInqpTrCntZeFlToAbr7i7ykXqrn429BjOCng3CZesFi7EyZQlGXAo8z7bIMJZjh5x1EUqod2L5J3_YPWEyrGQiyhKsuPlWzim9C1sH9r3DAMuXjlt21Tl2mIFusWN5IUIN7ps9h6lCybGHd612O9mRl5xWnku1P82pyzzxed6PFi_rnc88cOsHxv13kgv_QrpA7GQPqZqc3auEBiy8uG5qR3z7xfkFOu6KVzz0WwvmfTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین بازیکنان تاریخ جام جهانی از نظر امباپه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/91666" target="_blank">📅 13:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91665">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57c3ac63bd.mp4?token=QElmpET93eqHe-UQ_9MGjduDh2dWNjHmXQcEekyS68okEpUyfBmb90scU63Ak5__PYKYc41chJp_11F4YuXEjDo86oA5jpC8gT6z6015MIdSCAjxx5-3wI8ytK2HX6Q6kAbZw6pHTy94-tY9qKoxdAKEb3hHbUOMQ1ntRVtLLXzW7hLcRwt8yPkAABQXF9j4Q2x4tYn7sq9lL0qucoR5snGz-LiD72IEnFQH7lJ1jqPcny0Yhdd766jWCVbfCZP-kV4xDCs3xgXRSJnBOVoX4MQ7eGa2cXmEh0_cFsT6RNoa3NR3Y74UETzT5bk1yVxyHor7mW9o3uoDpYj07HKAag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57c3ac63bd.mp4?token=QElmpET93eqHe-UQ_9MGjduDh2dWNjHmXQcEekyS68okEpUyfBmb90scU63Ak5__PYKYc41chJp_11F4YuXEjDo86oA5jpC8gT6z6015MIdSCAjxx5-3wI8ytK2HX6Q6kAbZw6pHTy94-tY9qKoxdAKEb3hHbUOMQ1ntRVtLLXzW7hLcRwt8yPkAABQXF9j4Q2x4tYn7sq9lL0qucoR5snGz-LiD72IEnFQH7lJ1jqPcny0Yhdd766jWCVbfCZP-kV4xDCs3xgXRSJnBOVoX4MQ7eGa2cXmEh0_cFsT6RNoa3NR3Y74UETzT5bk1yVxyHor7mW9o3uoDpYj07HKAag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
💥
بعد شکیرا، اسپید و شیدا مقصودلو، حالا نورا فتحی هم موزیک‌ویدیو جام‌جهانی منتشر کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/91665" target="_blank">📅 13:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91664">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/520253fcb9.mp4?token=fOIl6YVEJB5OCy7KSIVgczXKL0lCcbRZrK77jhWJ95Dh-Ac05NUAwFS7gx6TD7enW59go48_pfj4dtDRcsU6DmJCjHrjT0QnJW3gVSxJZbhkM0OUui_b6HnQWgFXVbbAeGLR1lfb1djBT0L-7ufRuqE9tvB3Uv8HBIg6jgy1QJGmIvtQMneQg9wRzbd-pu2CVmIrwUzO9AeZoPCMaojdzEpQeXEHnxVBVFocpbw9PmCv9dwgrZ3964ZRZCji-ZbC_0xclW6XXkLPUWtYNAiRWDypS7iLlQiP_JHahgZxL9ouFxBW0XGPFStCnIvh_WJrJHR-WAtC-ngvGsyxHEAhng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/520253fcb9.mp4?token=fOIl6YVEJB5OCy7KSIVgczXKL0lCcbRZrK77jhWJ95Dh-Ac05NUAwFS7gx6TD7enW59go48_pfj4dtDRcsU6DmJCjHrjT0QnJW3gVSxJZbhkM0OUui_b6HnQWgFXVbbAeGLR1lfb1djBT0L-7ufRuqE9tvB3Uv8HBIg6jgy1QJGmIvtQMneQg9wRzbd-pu2CVmIrwUzO9AeZoPCMaojdzEpQeXEHnxVBVFocpbw9PmCv9dwgrZ3964ZRZCji-ZbC_0xclW6XXkLPUWtYNAiRWDypS7iLlQiP_JHahgZxL9ouFxBW0XGPFStCnIvh_WJrJHR-WAtC-ngvGsyxHEAhng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
آموزش رقص در ایران با موزیک دای‌دای شکیرا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/91664" target="_blank">📅 13:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91663">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4qf0ExhAjhX1Iz7D96vgE96QlKUoM-cSwbyXx1sAr6DLGZgf4f2DKiyMlRxJF-24hb7HG8ESwClZRw7fAtWrvN6Ns7nYmKgqAnt69g6rPxWPaoVf9WAhuoGQUR6jhi0iAVWGimshJe49oz4DyBfPK9ELHv2c7oRkL4O-HBVE4mogpafWYysDT0KKD4ScO_HPygif4SLhCpKOC1m1XE6pjIrWSWqpVapMHt5w0ERILQezExgzdoRGgbCaaXQeVjZxiSq-Fnq6_7qXQ533D0sBNPpRyFDCryedgkvSG6lfPVkMsqkfKrS0Jw7NGGqs5RiFEH2xMXaGdyy2rQs8E0e9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
✔️
پسران رگنار و عکس رسمی برای جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/91663" target="_blank">📅 13:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91661">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d43531369.mp4?token=pkl1cYsPsg8uYdXEY26cYXHGSnEC5W2Cqz2s7Zq64_AhmH5mq1CT3Nbyq_9rz9ZRwggl7ula3SUkBwcuwaBv9CJQsEsQPttyhTfaXFQchFiX1iMHyyW_uZGkXljCVowKdcDZ1xatiPnKZFtNT6ebz68ddBN7rhr-UMsa-Od64KFBTR0MMAhVLisYwmPqxNTUXh9h7JbYQ6LYmYb2tXl_IeJWpUHH20h_tdHU-QsVbZWybNnFDyNcjU1eJawJP5nJy1gOBxfeW_e0QbblMGM0fmkp_QGtadASzZIeUA443ClZG6XFoX6J3AyVB93Jeqd4SPCww9-mDc2aW_7GfTvh2IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d43531369.mp4?token=pkl1cYsPsg8uYdXEY26cYXHGSnEC5W2Cqz2s7Zq64_AhmH5mq1CT3Nbyq_9rz9ZRwggl7ula3SUkBwcuwaBv9CJQsEsQPttyhTfaXFQchFiX1iMHyyW_uZGkXljCVowKdcDZ1xatiPnKZFtNT6ebz68ddBN7rhr-UMsa-Od64KFBTR0MMAhVLisYwmPqxNTUXh9h7JbYQ6LYmYb2tXl_IeJWpUHH20h_tdHU-QsVbZWybNnFDyNcjU1eJawJP5nJy1gOBxfeW_e0QbblMGM0fmkp_QGtadASzZIeUA443ClZG6XFoX6J3AyVB93Jeqd4SPCww9-mDc2aW_7GfTvh2IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
صحبت‌های یه خانوم دهه شصتی که ده تا شکم زاییده و میگه هنوز این تعداد بچه کمه
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/91661" target="_blank">📅 13:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91657">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eSzCPpzsTSvyb0wPVb4KJ-fKq7QkF4i-w2ujL9q2CU04r7mg7GGv3efpN1PBksVL7nCROHiEmwxPHMbMDf82OxAkyKML3gp1TG-t2r8iymEA6gKkHP1p_Yl5a5iBTa2JU_bhW7XL4kMCkcGbgTgS0t7-CMfIdc6nUsZYSxHx6TTudWGMoCT-oaYJsO46CJ8HyRikoy0gD6d3_6IYgFtiIenVCzHoiAYPUkEHCiy-tolP9Iw4i9MVcGRXW49FlmLVXVzXcHDGPCuzeMYCjXvEX7VQnj0boC_D0gSxLisg6T0BWw-pVtaeCPxUECNEAmwMNSRCTOze1Q9unetzmquOIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s0rdN4OIj-6M36u8Ym3JNfquEDDS_zVLQftlb8wZJ-w94b5WNseQgLonRYMTZJRfrvXEo7hL6N2Gc-G2jGx2UCnwLUw6ER_Rn_AVQmDrY577Szjcbco7kVJTCNtp1zYxqAnkUY5Ucg0rQlkbgt8xEy1yumrtNlkyO668TqusdSP3VtpKjtQrvJg3Q0u-PWGfq33ml2Ok6XDWRZPiMYNCP0eMUr8zzoftbBV1o2O2brFiriT1PHRjOzoM0nvpyzWqC42OcqO7PaePtm2VeLTD_OgX_gmVkyc9L5_D21KeS2i6N4bcRzZ9hXEa0M2qiOsDn8CfaRb20OZpxeAYuRhHeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RZ4_SDufbp0C0znkt1uzW3oNUIxWMnUeDp681qa-wnoKJZOcb0JSW0O8wdxsucoKRAhA1-gyOTwngGFoo8-ERuAoFs5a3GF3b6iJzWqrGKY8bciCxN2Iy3pgv8PHqo-NwqNJzv4RUCML5qpFYxdJiufCOuaRVrANYOYO8cRIKApclEgV3dlp4A6ApWn_5yulaEkNYVLFqTt0ie6tpyvbTGFAv4--w9baPm5IC5PxQkzFdDfXmp4Yz4Ca-M8cnY7cRDiGmme-XE56y1iAYaHb4AsP8Nukiz5hPTAg3RK3uAMePUTIBVhs-xoeBm0bRhd-4GNfBZPhQWAh1gyywjZESA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UBJ7qv1XEbAd49Tr4N9W1LTdNwr2v0vhBqewPpzOabW0bHaomAIxmkFgFD0NHntGRQCNPwneSAn69_Zz6hZLVyLGpNiMsimpxBg6fzsi8CWF_tUM3ga29dk1zjSHJ71BUtcrd2X9uEcDTDNI0rd7cTl8pDwo_Km78xZ8sMxbGipOm2OU7aEMTz1_nmtOdvaghiCe7Kb45er6hODl6G6tKCN-Oiauymo2YUYsPjrtAGFGELXY9_s1lbeEM7IxLIrzY0u0S18vZxBen7d_ovST21T74_tf7ElAlqQu_FAIHS3vLNBnQUBidqyfGxKgk1f7XReqFl5XQyI8B_bvefrVlw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
داوران چهار بازی اول جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/91657" target="_blank">📅 13:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91656">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3909e54d84.mp4?token=ckeSX3PPyt6KG6ArsePDmGU9BWIu-bkZqt4zQCckLwQTMRMt_G-AIC6cBuAo4vZu5tLL4RBWC0PLXrG9dhX5s4CVCYJxH6LcY9qyropYvzWMQidOsKwuForw7qARF0eZJZqnDxBQ1ZGNTc3cL3np7bRgZD2HkbTSv5ql2fMVuOFrFeCEu1izUqrATVQF2wx8LVAkmtndxY6fDTCxzTHrAmoYbDwVU7TmKiqGRwuUW-1zTsdKQYKxInH2sb5a1Bsc9-MwZr9LFFHC0ZMx6I5z9Dtgx-oiOdZeb2CO6lsny1EjrxZLwl34uz-6rcWiNizi8EQsKlieTAo4wriGRWNWQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3909e54d84.mp4?token=ckeSX3PPyt6KG6ArsePDmGU9BWIu-bkZqt4zQCckLwQTMRMt_G-AIC6cBuAo4vZu5tLL4RBWC0PLXrG9dhX5s4CVCYJxH6LcY9qyropYvzWMQidOsKwuForw7qARF0eZJZqnDxBQ1ZGNTc3cL3np7bRgZD2HkbTSv5ql2fMVuOFrFeCEu1izUqrATVQF2wx8LVAkmtndxY6fDTCxzTHrAmoYbDwVU7TmKiqGRwuUW-1zTsdKQYKxInH2sb5a1Bsc9-MwZr9LFFHC0ZMx6I5z9Dtgx-oiOdZeb2CO6lsny1EjrxZLwl34uz-6rcWiNizi8EQsKlieTAo4wriGRWNWQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهکار حمید سحری راجب وضعیت اولیسه و ری‌اکشن پرز
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/91656" target="_blank">📅 13:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91655">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
ادعای
مصطفی پوردهقان، نماینده مجلس: رفع فیلتر واتساپ و یوتیوب در دستور کار قرار گرفته و بزودی این دو اپ بدون فیلتر در دسترس مردم قرار میگیرن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/91655" target="_blank">📅 12:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91654">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e68f156545.mp4?token=DmpZzzeUfO4v8Em9rSvuJRv8rP14WKBNiq2Ch8q7QwXthe_kTrc3hjQMenj9dkpi_yp8W9YudQBjpmx9jEOoujrHIbdQDKm5jto-6Foy8Hnj6b3Co5DhLbTCQ-3EecmWBEmhHX_8BzhbUctn_JhLV_vVOsyIY_Ba202G6F-jlhIGfolEfRuSZ0LC0Anhyy8giXHJ7dluGAt4s33EtQ_XEzpxQJjzCcWdeC-N2H1_qJGfh-qHk_q9aH0mwenYe0re0gfoKvSWsPUNH_DwvvLqHSrf0koj5SMOx-2Rv1QunUcAUgny-ugwu5vRIJPyMELXMrrt6S0Kszjt1lSt_oT-VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e68f156545.mp4?token=DmpZzzeUfO4v8Em9rSvuJRv8rP14WKBNiq2Ch8q7QwXthe_kTrc3hjQMenj9dkpi_yp8W9YudQBjpmx9jEOoujrHIbdQDKm5jto-6Foy8Hnj6b3Co5DhLbTCQ-3EecmWBEmhHX_8BzhbUctn_JhLV_vVOsyIY_Ba202G6F-jlhIGfolEfRuSZ0LC0Anhyy8giXHJ7dluGAt4s33EtQ_XEzpxQJjzCcWdeC-N2H1_qJGfh-qHk_q9aH0mwenYe0re0gfoKvSWsPUNH_DwvvLqHSrf0koj5SMOx-2Rv1QunUcAUgny-ugwu5vRIJPyMELXMrrt6S0Kszjt1lSt_oT-VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
لیونل مسی: «از نظر اهمیت، بهترین گل دوران حرفه‌ای من در وقت اضافه فینال جام جهانی مقابل فرانسه بود.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/91654" target="_blank">📅 12:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91652">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RSQevP9AnUe18WI0DhatWxQT5YR6e2YpXrJGO3H5Ctd9j8i-5TZ9FYfOzaEYVpeNAo6VixHHCh5X7dexGKIzRvBDD0wK5v4Ar3cF9NhS-EeuCip99vaf0hv1N7HkHs7M5XH7GIboo_v18KSq-ZBWqnxDHswUt8NGJr8s6Ii37uWKrIMvOPoiyPG_IIbZltAyx2rb-eR1wxdMI21MZhSEGQOlP0u2FkOZntRc9hem9_Nfui4t-PPyOMjU0WDGu1KRu_9AvZilgr-9LUGVBQF4r43EHWmawEyfjWxxb11oqb2VclKLpocxnJc311UBFqF0hjzwaLyDpr0yz6U2cOYUmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔙
هواداری که به خاطر نوشیدن ۳۲ بطری آبجو از کشورهای حاضر در جام جهانی مشهور شد، دوباره برگشته است…
🔺
این بار او ۴۸ بطری از هر کشور حاضر در جام جهانی ۲۰۲۶ دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/91652" target="_blank">📅 12:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91651">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ls7dlY5oklv5xZCw58DL2hnIxDGBqWWjb2yqjnunbt974DWn6QlacaJa8zjCeDO8RPOU-D8PT0h8Va4QPTdUdaSjD7CufYLxWLFFcIsg9CgObikyP_W03Yx5-U-EWahbvONZ6JYSYby_loAL8TXJeTiqObKNeXnXnJFEHyEQ4PRQaM8vB6YLRyEsf1PuQKLVj8X0-Fw46JdEAXeXIlGG1C8lrhlc6HXvUvBECaWiz_ms_I6-_S1capBFj3TY6usEWORPy5IVBJPbz-vOhy7Q2FSKn7C7SWk_DxfNlXJZpRCHS0yjKXC8Yxgk6fQfV-s3jBaoyuClE6RFcmAV6pQ4OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ژوزه‌مورینیو دقایقی‌پیش وارد مادرید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/91651" target="_blank">📅 12:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91650">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGuB-sgQ2ssfL9bUlQNbBybgSQ4R1Ar08yt0dYWvioemsVOlBLvEWQ8LqmWmAXw2nT9lFSADQR5DA-Xgy-yAgEltrZDtdA2bB9vfDMGMXQfDBriEPpv6j0l1J6OyWYFCFFVMlhN-w6ASB-QaJ1KJttEsWQR9zbbZdeJMBXrM9G2SYTYve6FOohaWjFf5PZCqVD08bNd-RgzzEr_6AaQsSaZVM-rPZYmE09k0DfVEI6jL35w5KopkbMl0zFxGSfkLBSr5u0BoYvDNmIvMd2IvScPQxXuJ1tGY6KiZvIzUJSesu-9Y1rAhIrXJyVcDmZugp24_dNAo9YfLjWW343GPZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی فرانسه در گذر زمان..
انگار دو تا کشور جدان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/91650" target="_blank">📅 12:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91649">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DgiYqHueVjGZPaA8lAdRLo9jvmlvxrWJdjq2Ws20cppf0tAumDtJrzwpCMXMhOQGjGwhmvpaSe093G1S4LMgerWDii4DMlI7aeO4VpTPRPPiF-SBs8jEnoKDs0ioxOV2_E7Th5gRati7WBPjS-kjnZGikdSyh_J9eHDj1p_mn6IsB1MwWNieHOniLC_Y5eVg0qsjJKYHfEl265PbgQWkK_7DbBN-WjJz0iZdTqtYIAtfTD_yUExDf5BfHwGjSZ0X1z5b_lyE9TnEX2269-X1Qumq3BA1VibPRtIRjt33_Yu51E0NLn8bRr4W_dsPM5ZJJsmKCsiSt06hIQW9V6E1-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇺🇸
ترامپ دیشب سر زده بلند شده رفته فینال NBA رو ببینه که باعث شوکه شدن افراد حاضر در سالن شده و از نکات جالب اینکه تمام ستاره‌های دو تیم فینالیست توسط ماموران مخفی آمریکا بازرسی و تفتیش بدنی شدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/91649" target="_blank">📅 12:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91648">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b81ccf3378.mp4?token=bYCGRZVFK0fHUFDmI-9KqIn05yy-zRs5nmgJi467mp5wt7LxqwuO0PVZ0jlbEhGZeFPs_sxRLJx1mOG_0hyl4rZu5pe7wHjfQBB2KQ_iMna8BGRtOxpWcW3t3PQulCitz7QHyjp0NCaDaC58xOoBzwVcKXORngvL5ZC2JpxvgpIuaMc_brm07qPnkCJeXq5PuplmVPvEqaWZfhi1_HqDolTDnZQhu420_gXDJLHBtefrwWdq4-VsW8KDaXeiJ9qdP_-g1ucjh3CWTsxpkv6x4CUnOGa476KgN9myW9LXJnCiYHRPRhtYQr1I8CK11olRATQtPjW2J3MrduQkn6YQcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b81ccf3378.mp4?token=bYCGRZVFK0fHUFDmI-9KqIn05yy-zRs5nmgJi467mp5wt7LxqwuO0PVZ0jlbEhGZeFPs_sxRLJx1mOG_0hyl4rZu5pe7wHjfQBB2KQ_iMna8BGRtOxpWcW3t3PQulCitz7QHyjp0NCaDaC58xOoBzwVcKXORngvL5ZC2JpxvgpIuaMc_brm07qPnkCJeXq5PuplmVPvEqaWZfhi1_HqDolTDnZQhu420_gXDJLHBtefrwWdq4-VsW8KDaXeiJ9qdP_-g1ucjh3CWTsxpkv6x4CUnOGa476KgN9myW9LXJnCiYHRPRhtYQr1I8CK11olRATQtPjW2J3MrduQkn6YQcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
حمایت و تشویق کیم‌کارداشیان برای لوئیز همیلتون دوس‌پسرش بعد نایب‌قهرمان در رالی موناکو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/91648" target="_blank">📅 11:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91647">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔥
🏆
برخی از درخشان‌ترین سیوهای تاریخ جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/91647" target="_blank">📅 11:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91646">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
تیم ملی جمهوری اسلامی به فیفا درخواست داده تو بازی با مصر به خاطر عاشورا بازوبند مشکی ببندن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/91646" target="_blank">📅 11:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91644">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9FSMOwkSoGXjMEk5P6jst4jE2B_p4xulLmZtuIF_svyLOCAX3HUSocCnE4k2XrHunYuHwPY_VKNhgzxwWlhQNCUUEP3aFkv-D4dsUIpZWX1Apz6mxBG-iD8I8akWziW1Sf-VjStB53tE5bFIo9RcR4WDuAnrYgfIdwSBIhglzlatqwBp0kUzOgB0qR8w5wuijq3du1um1THmyEvxn2oXMCNIP5IkGjLAVh5PP4BkQPRjUzX2pMP1yNwekIEOtmVpVYMv77XFvNmphl9EMfSNTqMwS2jRJ1MRQ48T6hdwPAy8ULi-H2Ee-MUPorHEYWvnpzyW118FCvFbK4c4tOMQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇩🇪
فوری از اتلتیک؛
بایرن مونیخ هم به جمع مشتریان یوشکو گواردیول مدافع کروات منچسترسیتی پیوسته و قصد داره برای جذبش تلاش کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/91644" target="_blank">📅 11:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91643">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mk0Ta6J_AVR5LGRIdY4NOwQ1TXw5LRXxggFwJGmbUn9c7lgL-PiFHkLpNgtN0uL_uI1YnvP5DHqcBzcjIrn4-AW51Mc8EtTrKg6po8JeHv6y-QNfzwjpf1GhUKWy3TzeMb1mfuhzXJsreJebabfA4lCFOMk3ee79aGkqiMWWGXP54smhthSu4kyg_tOlD49-nAHqrw5bonDuyWz4LjcBb_Nwa-zIvoskYadiVNefWK7rI9ChlORxqKIEM0qJFUKt8BHQ8inZ62ELJiUSFsuG1aVokJkYcUqHpMDeKnpsGJxNLoR-pg8Vd2yK3Jjk2S9m3GCFkkuwRUywkOCRQo6YDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
🔥
لامین یامال از زمان جام جهانی قبلی ۱۰ سانتی‌متر قد کشیده است. یامال که برای اولین بار در ترکیب جام جهانی حضور دارد، با قد ۱۸۱ سانتی‌متری خود جلب توجه می‌کند.
✔️
در سال ۲۰۲۳ که به تمرینات تیم اصلی بارسلونا پیوست، قد او ۱.۷۱ متر بود، اما با برنامه تمرینی حرفه‌ای و رژیم غذایی مناسب به سرعت رشد کرد و به ۱.۸۱ متر رسید. یامال که هنوز ۱۸ سال دارد، پیش‌بینی می‌شود تا ۲۱ سالگی قدش همچنان افزایش یابد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/91643" target="_blank">📅 11:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91642">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
تیم ملی جمهوری اسلامی به فیفا درخواست داده تو بازی با مصر به خاطر عاشورا بازوبند مشکی ببندن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/91642" target="_blank">📅 10:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91641">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🙂
دیوث بازی مرحوم مارادونا در جام‌جهانی ۸۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/91641" target="_blank">📅 10:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91640">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
ویلای ۳ طبقه علی کریمی به متراژ ۱۱۵۰ متر مربع در شهرستان لاهیجان توسط قوه قضاییه مصادره شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/91640" target="_blank">📅 10:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91639">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14ade73f00.mp4?token=M575zIyRMC9RutKfCivLGtUCZ_GYf19-IrGqRWzA-78YWh0SHuZ0JdvEpsdO0HFuSjPeuhaJ9rWR-1EADMbZ6o6dolJ3meLjqIIde9GgeuHiYW-p3ZkJvRrWSevODU24oAPT9sB6giR7eI-LicJFvBq9L82GJT2Z1gCQGVEvjJZtJrNXEkWhrlO9saqsp5odSv2I0VG98vTUcK0PZx-jSDF27SeoBTjbw43BdLb-Ya3ZwOf8URjr0WgiiyMftHTBPZ1sdpdPaGtdkB1udmeQl2wQrAm0dqezZGbDLgpSWwrLIIj_oTuvZlMxOjoCS3CAc-g6c75XnfgL0UEQ00VUhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14ade73f00.mp4?token=M575zIyRMC9RutKfCivLGtUCZ_GYf19-IrGqRWzA-78YWh0SHuZ0JdvEpsdO0HFuSjPeuhaJ9rWR-1EADMbZ6o6dolJ3meLjqIIde9GgeuHiYW-p3ZkJvRrWSevODU24oAPT9sB6giR7eI-LicJFvBq9L82GJT2Z1gCQGVEvjJZtJrNXEkWhrlO9saqsp5odSv2I0VG98vTUcK0PZx-jSDF27SeoBTjbw43BdLb-Ya3ZwOf8URjr0WgiiyMftHTBPZ1sdpdPaGtdkB1udmeQl2wQrAm0dqezZGbDLgpSWwrLIIj_oTuvZlMxOjoCS3CAc-g6c75XnfgL0UEQ00VUhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🙂
سوال روز مخاطبان فوتبال: یعنی آنتونی گوردون با ۸۵ میلیون دلار رفته تو پاچه بارسلونا؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/91639" target="_blank">📅 10:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91638">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ایران میخواسته یه بازی دوستانه با کشور گرنادا که کلا ۱۲۰ هزار تا جمعیت داره برگزار کنه که لغو شد
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/91638" target="_blank">📅 10:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91637">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15d23ccc5d.mp4?token=noYH1wDWXoO5QgEws9_xAubaNg9zP962p8aP6O5M7vHDwnRcYlFD03iMsxLl60tAOyCT8Yq6q9NRvwmMX-ZA0a1C1euhUKm5f_wf0Pyyq_nhWH1MJ_s3pP9pPcANs_4wizaxd0Dl_AAlxKgtaZMFZUPjeOBWBTDY1h4ajGbWwR1WtlfTqmCswGWAZqy4oL_YQ5uWl16sFwsd-Cd9FqBlA_gb76B-OCcSAqyo4YUvIv0MEAJimaRsb3eH4Pkn05oW-0d30w2mwQzmAVNxsCTcYKQOmsy7ETRaVU5AZTt7DjwIRmFKORnQSdZIwa4iomKKnj4Xy0twe0EMaCP3LzeAUaDsRWN6fmYtmJOd3Coc2VsibJfKj1i33jvggOAUi84G2wQrWuGgTs6UrcnbxkEzl7leONUnSR0RbXzzQV-b3S2vt1U_eTEm1P8s2P7tTKj_5B_9_fN1JoprYFmIE0CcWSBtFoGpkOGCsH8HLpPjhqtYsXpco8GRbkHz6HfF9XT6-kXbx5mNAvPmSJZcjkYmDVfPVelbseEzIahEmMlInakOihqtEVaot1Bdn8_yoKMy1J_YF5fu08lPP5F_1FTfuQCBGECCemLt4gOvYQ9SYsHAFp0jWZM1HplbuilwQKUfmplJy9GGaaMXLbRC2kwsnzHkwyHKusJJR8AzkSGLWd4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15d23ccc5d.mp4?token=noYH1wDWXoO5QgEws9_xAubaNg9zP962p8aP6O5M7vHDwnRcYlFD03iMsxLl60tAOyCT8Yq6q9NRvwmMX-ZA0a1C1euhUKm5f_wf0Pyyq_nhWH1MJ_s3pP9pPcANs_4wizaxd0Dl_AAlxKgtaZMFZUPjeOBWBTDY1h4ajGbWwR1WtlfTqmCswGWAZqy4oL_YQ5uWl16sFwsd-Cd9FqBlA_gb76B-OCcSAqyo4YUvIv0MEAJimaRsb3eH4Pkn05oW-0d30w2mwQzmAVNxsCTcYKQOmsy7ETRaVU5AZTt7DjwIRmFKORnQSdZIwa4iomKKnj4Xy0twe0EMaCP3LzeAUaDsRWN6fmYtmJOd3Coc2VsibJfKj1i33jvggOAUi84G2wQrWuGgTs6UrcnbxkEzl7leONUnSR0RbXzzQV-b3S2vt1U_eTEm1P8s2P7tTKj_5B_9_fN1JoprYFmIE0CcWSBtFoGpkOGCsH8HLpPjhqtYsXpco8GRbkHz6HfF9XT6-kXbx5mNAvPmSJZcjkYmDVfPVelbseEzIahEmMlInakOihqtEVaot1Bdn8_yoKMy1J_YF5fu08lPP5F_1FTfuQCBGECCemLt4gOvYQ9SYsHAFp0jWZM1HplbuilwQKUfmplJy9GGaaMXLbRC2kwsnzHkwyHKusJJR8AzkSGLWd4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از هواداران ایرانی بانو شکیرا هستند
🐸
😊
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/91637" target="_blank">📅 10:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91636">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🏆
🇺🇸
🇮🇷
کشور آمریکا خبر داد که تمام بلیت‌فروشی هواداران ایران که از طریق سایت فدراسیون تهیه کرده‌اند برای جام‌جهانی مصادره شده و حق حضور در خاک آمریکا رو ندارند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/91636" target="_blank">📅 09:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91635">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2OW-6QLT1n0yTney98VATEGGALx2-Vnneb_ZCF2aPSCBDgO7_6orgT7cnoF7hraIAQ3nAF-oS7AAjiOoOeopH6IbhsODcYK-AmKRBS8vGw945DTANWPPpqFxAk7v6Dq6kCxQDIzYi_WgOvICuox_DYeQoYXB6DOZ7478uKU5--RG885o1jDRv8xwSEPQjvYeiRpQb2RuJAIkDxhWoD0F5qBmUZ1JfrnOLobFalgtwNimAMLKT4rJqUyFHR4GebYb21Y3KZt-NJZm1f28vAwJzCqtu5Hj3KEH9UOnM8Ab0Q8mHoXLXjIwSFqUZqTzPZdB43F046HZ8LQ6W9Hcz7NFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همه مدل موهای نیمار در یک قاب.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/91635" target="_blank">📅 09:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91634">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/584eabaeab.mp4?token=eENhyrJWLa4FkKKFrEBviZqCcCrCJmCtrpRtgllfzCJAj5S5rqW8n31W_zWQfItAUn_UXVhlgiWuXMpUw1gRQjwmZkre5R-OJH4ie1vuzxnYcVfTyG_2dAEzI-A4yd_jZYtE2h3JA5gbbnvHTaoOAcjrEFH8hZyJ8o3IOR79S-zS-uhfERfnuU_zZbS06C25UlW5moH6qJ2MmtoQin6LvGXg2xIRtxb-v9BNXSOVQFLNDOp6d2lUobENAgVqKyz7_4KGwuEhcWfuKZCtAW2cK4RCU1pjAh3RfesrMobdKFek1NupQU9gAgKp6T9pvdqeSkN_6HSnPsMPkZpSA3ZU_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/584eabaeab.mp4?token=eENhyrJWLa4FkKKFrEBviZqCcCrCJmCtrpRtgllfzCJAj5S5rqW8n31W_zWQfItAUn_UXVhlgiWuXMpUw1gRQjwmZkre5R-OJH4ie1vuzxnYcVfTyG_2dAEzI-A4yd_jZYtE2h3JA5gbbnvHTaoOAcjrEFH8hZyJ8o3IOR79S-zS-uhfERfnuU_zZbS06C25UlW5moH6qJ2MmtoQin6LvGXg2xIRtxb-v9BNXSOVQFLNDOp6d2lUobENAgVqKyz7_4KGwuEhcWfuKZCtAW2cK4RCU1pjAh3RfesrMobdKFek1NupQU9gAgKp6T9pvdqeSkN_6HSnPsMPkZpSA3ZU_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های جالب و عجیب لامین یامال ستاره بارسلونا درباره دلیل بستن باند روی دستش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/91634" target="_blank">📅 09:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91633">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37b5e13b24.mp4?token=mSP6pRjSqx6KHLVW5tAkJM_y6zHFchS9zx9WMdV0zc6qroCNKSyCScuMCP2v7jl8tNwVUyCwEK80rYLoud8Dcce9A5ApKUBnCN_M44hZ9MJiWVFaxmt2LaOGLvTrdkXnXmptSY4Vj0Ny1Hjq1FK9a0vrhxDePC0FY6HMMLrPgNM-1nS4aZVJUh_zv_nkXha5OluuZHNvBfaUvAvHzD2Uq4keHSKWGzfa7vZZ8Qfo0jtowRWc495OhIFiPlbGT5p5eOXHQ7r7U3JhFnodOBBAEx66SKadnCiHdZbf5HWiqJ2xuR6yP_Ow_aeHEAmcSppVe1XtK2VefChRM_MRyCg5RpS8Zz244M8Q_uyleSICHMEsglGk5-83_LH6mSpgUoMwYoS4awQHQp2D7f7kktAvjUIYw7gjdiQVKy0qtsj6b63ZwaHUPLhcJik2b03SUe72nTxMTUgiVJObzgKNMTVdLBjsogKOrdyoXt4R6bcEES8xVpdAt6WUEoXFvYwgSAb0l4sXgundU4JfcDwX1pGAqeysa1EkdNwniQbgt_cxdFrVallN5__6y_7iZ88nDBSm2Px69Ix7LSksQHiZfheYV9eXlLnY37BREbfkNrCYvAjQy93xqIIV4fXmMbdnUPxr0TCpsAAuaFF2TFfj_HA2KABr5RVc4ZiU1pkC0ResWRI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37b5e13b24.mp4?token=mSP6pRjSqx6KHLVW5tAkJM_y6zHFchS9zx9WMdV0zc6qroCNKSyCScuMCP2v7jl8tNwVUyCwEK80rYLoud8Dcce9A5ApKUBnCN_M44hZ9MJiWVFaxmt2LaOGLvTrdkXnXmptSY4Vj0Ny1Hjq1FK9a0vrhxDePC0FY6HMMLrPgNM-1nS4aZVJUh_zv_nkXha5OluuZHNvBfaUvAvHzD2Uq4keHSKWGzfa7vZZ8Qfo0jtowRWc495OhIFiPlbGT5p5eOXHQ7r7U3JhFnodOBBAEx66SKadnCiHdZbf5HWiqJ2xuR6yP_Ow_aeHEAmcSppVe1XtK2VefChRM_MRyCg5RpS8Zz244M8Q_uyleSICHMEsglGk5-83_LH6mSpgUoMwYoS4awQHQp2D7f7kktAvjUIYw7gjdiQVKy0qtsj6b63ZwaHUPLhcJik2b03SUe72nTxMTUgiVJObzgKNMTVdLBjsogKOrdyoXt4R6bcEES8xVpdAt6WUEoXFvYwgSAb0l4sXgundU4JfcDwX1pGAqeysa1EkdNwniQbgt_cxdFrVallN5__6y_7iZ88nDBSm2Px69Ix7LSksQHiZfheYV9eXlLnY37BREbfkNrCYvAjQy93xqIIV4fXmMbdnUPxr0TCpsAAuaFF2TFfj_HA2KABr5RVc4ZiU1pkC0ResWRI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇮🇷
مستند کوتاه و دیدنی تلویزیون اسکاتلند از تیم‌ملی فوتبال ایران در اولین دوره جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/91633" target="_blank">📅 09:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91632">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/237827913f.mp4?token=faLQwk4eTdvg1jOknneVEId69FSFQGvfVPI4SK0n1BVxGUPyyGcreThajHt0X9TlmCK9V2Fd2WAK9jyAjV_8QQmfqZl4yS4CBtVm5n2lLpXI-X8ia_CE57Avij9Bjd1oBeM3AXxkphJN8ZxOXNNoszhKWdP1GTcZN25gOWDJfU2OxlSvIKmupODPUkuii4b55MjdQS71Pfz4TUDsogV91yH9S4yCFlm_vqZiG6GW4rj95tzRFoW5mZlJ8NVHuVyW_Bmre70kqrmN0OM2K4Ll_PbWjq52N-eGBw1Kv4vYF5vzMychdrLpI9KuIrdl69erACc7RNXllzHLPy7oVNtuybvxyK-7JFtmUX8c1IAV_2JRzECIOpwc8GVK89hJvde-nUi87WrMBZOzjlNKwHCLdHhh6hLbkCb8kqKaSkQrijJKJQ_GSpgeYDfXo2yjrk1ca3HfqViXEIXdq3R2S3qoHF3uKgePnKNynwBtGT0wEaZ-fE7xRPSjFKq2lt5pv-35EzMQBshc2mIExxpLNDVQ4QB3Arm03HAZqx_LEXbRPweUYO34n4wPEqTwH_IYp7SKECKI7X1-4d6-PL5iVg7Eu-wiJC88x7ZdClQHIlMu7D0D2WbfAbzIKCf8qe9EVqlKUyrFcEaGGcJd2-Ox0hMsygPPIs167GWLPHsPpQS_lyU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/237827913f.mp4?token=faLQwk4eTdvg1jOknneVEId69FSFQGvfVPI4SK0n1BVxGUPyyGcreThajHt0X9TlmCK9V2Fd2WAK9jyAjV_8QQmfqZl4yS4CBtVm5n2lLpXI-X8ia_CE57Avij9Bjd1oBeM3AXxkphJN8ZxOXNNoszhKWdP1GTcZN25gOWDJfU2OxlSvIKmupODPUkuii4b55MjdQS71Pfz4TUDsogV91yH9S4yCFlm_vqZiG6GW4rj95tzRFoW5mZlJ8NVHuVyW_Bmre70kqrmN0OM2K4Ll_PbWjq52N-eGBw1Kv4vYF5vzMychdrLpI9KuIrdl69erACc7RNXllzHLPy7oVNtuybvxyK-7JFtmUX8c1IAV_2JRzECIOpwc8GVK89hJvde-nUi87WrMBZOzjlNKwHCLdHhh6hLbkCb8kqKaSkQrijJKJQ_GSpgeYDfXo2yjrk1ca3HfqViXEIXdq3R2S3qoHF3uKgePnKNynwBtGT0wEaZ-fE7xRPSjFKq2lt5pv-35EzMQBshc2mIExxpLNDVQ4QB3Arm03HAZqx_LEXbRPweUYO34n4wPEqTwH_IYp7SKECKI7X1-4d6-PL5iVg7Eu-wiJC88x7ZdClQHIlMu7D0D2WbfAbzIKCf8qe9EVqlKUyrFcEaGGcJd2-Ox0hMsygPPIs167GWLPHsPpQS_lyU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👍
رفیق خوبه اینجوری پایه باشه. حتی وقتی موهات سفید میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/91632" target="_blank">📅 09:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91631">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Fifa World Cup 2010 (Playing Football Games)-[www.Patoghu.com]</div>
  <div class="tg-doc-extra">[www.Patoghu.com]</div>
</div>
<a href="https://t.me/Futball180TV/91631" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🏆
بریم به حال و هوای جام جهانی 2010
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/91631" target="_blank">📅 05:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91630">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGZHgjvLEzsjqWOseNdtApL8PpHjlywiOuLMobG3BVnB3VW0lguQe28xyevD9lSSglcWYUPeU_ejP5CBrMd30ZzAiPQKu-aS_uo_gVV91QgHwkCTPY4NTcjvGVDDxVlR2cMVY-5_uPDCOT-Ir1gLFGQ-gIWSQKq3c6Xdn_VjxHXsGNpt3JrQORFH44mT4oM9iAr7duqJRAN3p8TQYDy07DBkvHNxai3dsHtwn39mKr3pKQ0F1kKlXhftDDuIG_lssf82BvZPZvC5LmNXpDXtGAXA1dSvbcK6LUaSfe2MssQFwRW_GjuMj__Dd9frvQHs0Tlx-oYIf2CcX4DI_HpN6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فورییییی
از موندو:
🟡
🔵
الهلال و النصر پیشنهادی به ارزش ۸۰ میلیون یورو برای جذب رافینیا ارائه داده‌اند؛
با حقوقی چهار برابر حقوق فعلی‌اش!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/Futball180TV/91630" target="_blank">📅 01:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91629">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axnusDTOn-2RnTCPSJI8jPrt1yg1X5k-_kDWNEmX3AcyzkwF_CUCDNjFwgKzfWldBRhwOtToKWJamJsyBb6t7wGBKXdlcGdkxO019SG9qO3rSVevQ3jUUZom-gqYvI-rV6WzIYeky4ZgMvHO0GEerMlJKEA7dTQ3g3Lrd8NUI65FWYm8W01QoFEkZoa8pONHF7rhHQQLIWjn1gfcfgm5mrDlBfxAk-k8VO1Tn51PI1Zn88tNmYEaGRPeC1LBoOk0f3KDd-yywxT8PPj-CddG_Jkkul-zf3BWzjWG5yQkM4YeKcs6FG9UcYaKnE00HKfucX8WaTaxnVWpXfJwC4Ojvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
رامون آلوارز: بنظرم بازیکنی که پرز قراره براش 150 میلیون دلار هزینه کنه خولیان آلوارزه
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/Futball180TV/91629" target="_blank">📅 01:29 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91628">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-owQfa3GqvnfAU_EPZpuHMUaW6zzIphoRPBoGlRZYASH9r04Nt45XycuCnlK2NByNYSFNvP96t6ZTlbIvHJhyYYqFojwRZo0dr_JhU26FDBh26uGgNNUvR6hZ7lBVzf07oDRwwufbSzqgCGwzFSmcVp4ht0Ct9dhy9YrtyqS3DGcJz4Xb0JPiQ37JN92BbArFltIpi1kd-NCv99fZ9X44kBhGxKxAOKzKBP2UEvfR-HeLQKONoF1WiIHAywQ0ybCpuluRyG5UJycJpwk6LLiOyfIHvjMss3MVBNarIKfc8hfzrhvJ5sXffpwf_D_bpy58hK4sCTjG3r_wQilC3hnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
رونالدو در کنار رئیس جمهور پرتغال قبل از سفر به آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/Futball180TV/91628" target="_blank">📅 01:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91627">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">عمر آرتان، داور سومالیایی منتخب فیفا، از ورود به آمریکا منع شد.  او قرار بود اولین داور کشورش در جام جهانی باشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/91627" target="_blank">📅 00:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91626">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ce3S86d4NHoMhtXY984QG7-uBWQbQA2ACEtaLndL0MG9Q77aboZCcHO6Kf9L97ExtS1UtevmPGnvz0sN1W3HT4MDjf4gAEVC0FqwxPFshXozQPw3OFHGuINWdbEpdGpXDe5koUNfJ6Orwb0dsfGpEGIRNshQdFI9s4z8LsO_pOvrCS_nPmA8Gz-Pkq7zNp8dbgcAnkSgd06Jy-Y6-3lBAgxfCKFe5UFzpTaB238tKkQH-PIJEMsMwL7U86e7GOgIb5pDrKN7XspibJ7qKfq3RWAFs-hBoGpTzmGgqSgoT7EAOgRQ4HKfhRzOanaWuhKVnugRI4VGy8lIUGY4srpOqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📣
🏆
ویلتون سامبایو برزیلی داور بازی افتتاحیه جام‌جهانی میان مکزیک و آفریقای جنوبی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/91626" target="_blank">📅 00:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91625">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ElsghVIuqVHEHeZnfYcV4mvMg849JMCX9svP9QTDYmPxckSpxwJQXG94bJcj4vjw88JgCdp8inBqE1DWn47l4iGYIxm0YKRsO-3tQyKuIKmltpIxUhCtK4oC24Loh6_DnK2MV-vKbtauPrxogTV2bHnugeOxXvgtks0zUqFK956P845C5EeEk8qHGuLjYwrKFy696IR60twN1uDm0T6-Nyje0kLq3sLjnhfmj8mbQnZkE26EsMDxvBw0eFhBvvfpaJwFj77R5rbOU9AiDpmpu9L9Uo0c3LMebW46Gjgf6Dx3x_OlwrTYcCq1zC8gqD_XxsAJ6lQjdKECrhBBl-gJlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">POV: Bitcoin in 2010
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/91625" target="_blank">📅 00:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91624">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uj_F9GxFarOoGj3PXhz1t6U3nmA_DTAQ8WLJtio2Ptb5LgryRDD7toQI4_l1mWS5vUZJS_nflhsUMiP2yhZPp19xrsNtqhZ-mrh0eLSUOBooL3MzmC_oafI1EXwsMctkgR-hTbrfHAhoCc-a1S97PpPoETjw__qzTOg80TmwHMMFr1gc8QieZa9ey0CrcribAxa3RKuyRugRq0EZzjMPfFX6z5jq0qj_L1o78EDUfaLwtg3bjN7wazJh0UUEKEoF3xIMg09NnMy7lcYROfhwoqPP3IL-itJa3wP5wZGmZ3tV8ssjtxbw_a5MoAL6uh0rmCdACmSVFBEDUunvmwnalA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
آمار پشم ریزون  مایکل اولیسه تو بازی امشب: 3 گل 3 دریبل موفق  4 شوت تو چارچوب  4 لمس توپ تو محوطه جریمه 5 شوت   نمره 10 از سوفااسکور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/91624" target="_blank">📅 00:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91623">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/YNWxawSfCZzna0AhwbL7MllvMv8TScNc5NcjoSzhujwqn96Z5GpEmLRxxD_b6SO9M_eSQXkujFzmZprWaWYuRQktBwkynWZUB0cvqVniWwvCr404V3VZUw4VsFc40TVk8XTwlbEdz8Wsed2Xwfby3GUt9HMu--XfJXUV8rP-nawVJpc9lipLISr33Vx7qgnvmr3B0synrBTshe4q2zpWQZ2eCeW8ZssvMHX8MWSVfwT3vW7pRZFrIzUIkC97T1cow1ilUBgqnf9rSoW1GuwJTGm2ky166XQCpwhLhP1Fj8deI1kd9gpEBCAGr1FYVkqGBEvYW2N9xkra3yCJEBfBGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
آمار پشم ریزون  مایکل اولیسه تو بازی امشب:
3 گل
3 دریبل موفق
4 شوت تو چارچوب
4 لمس توپ تو محوطه جریمه
5 شوت
نمره 10 از سوفااسکور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/91623" target="_blank">📅 00:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91622">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaea310c51.mp4?token=eadkRBGdRwom3KS7SfFkkgsornFjYU0wlxTFAzetx7eFQyTAJXspSkeIlh-EO7d4KITTmrCgAYeda3liZy41EZL7GJx1pmYTyNczSm0OFiDISZQsdKPg3dj1hPVpOcx_WV7xsUzS-ROF5HnIVfYyUdzn7glyZmsIVGicFdHzafqlo0rUvsXmexK1kgUD-8jK8mJsAms71YB6hmEkCK_96YEaekdxiLJJq0qPzUKAtfv0NmuClq6seuxUQl_UgjYHKVJqNVUny8_9lBaXSazMuYU82Rm6eQ9lYqRlAQtZXtPnPzC54tG-71KKlLJ3xRlvTGsijB-T_uz1WgSpKnnZQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaea310c51.mp4?token=eadkRBGdRwom3KS7SfFkkgsornFjYU0wlxTFAzetx7eFQyTAJXspSkeIlh-EO7d4KITTmrCgAYeda3liZy41EZL7GJx1pmYTyNczSm0OFiDISZQsdKPg3dj1hPVpOcx_WV7xsUzS-ROF5HnIVfYyUdzn7glyZmsIVGicFdHzafqlo0rUvsXmexK1kgUD-8jK8mJsAms71YB6hmEkCK_96YEaekdxiLJJq0qPzUKAtfv0NmuClq6seuxUQl_UgjYHKVJqNVUny8_9lBaXSazMuYU82Rm6eQ9lYqRlAQtZXtPnPzC54tG-71KKlLJ3xRlvTGsijB-T_uz1WgSpKnnZQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوپر گل اولیسه و هتریکش تو بازی امشب
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/91622" target="_blank">📅 00:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91621">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fw5ZSjKqu0cD3vR4wZjI70_cBpX4kmVGlU-fIyhHZOmAeONFbPadRz06QLf2UsbiyFS7U89QlC7bo1YoeyaEljgUOtT73Buk3OFxpA52rOsOb4VliSt8WyBlnF4YteMI7TuKy0Qe6ucG7i0juCltBySK_XDX_JOXXQXgi8pWuBLrtVBwWgi5Yryf-Oh2IVQDjKabe5kXzr-QRYHjRtA091bohnIch-Je388U9s88M5vK4SDtq2x-YaxLN0kHvuKZmhplEB5Lx0XpVDQEpnuYjyKN6UdlsoLmo1PAW-nG_wp8WQVXOitV8rHLkLbqXg7jCAswfmfxgJEGDdtKU5xtGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکل اولیسه توی ۱۷ بازی اولش برای تیم ملی فرانسه ۶ گل زده و اولین بازیکنیه که بعد از داوید ترزگه این آمار رو ثبت کرده. ترزگه آخرین بار تو سال ۲۰۰۰ تونسته بود تو ۱۷ بازی اول ملیش ۶ گل بزنه.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/91621" target="_blank">📅 00:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91620">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">پشماممممم اولیسسسسسه چقد خوبببببه
🔥
🔥
🔥
🔥
حیف این پسر بره زیر سایه امباپه تو رئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/91620" target="_blank">📅 00:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91619">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb905f6488.mp4?token=LX_gfc-VNMirIZMKhV7R9kyXrko8eunbIFSJSqgfKP2DWQZ_mWm_Rt8HFuOjnoLWb6ioiMhCX_BLPJKJb9fGVi61TMBRzuZGPufSVYSDDobTowcZwISyrCKY3uEw3to0hDM4kCiB_uir9t_UeInBKFYjbNWhhyORT3v111RJBSbRTkAfMRnyRwpRR9zETdbSeQxh8MopkuLnZRra9u6q_c-ZXXGrs1eNvDinM8avBQ0e84YLwf_Myxj52OGWbzE9opVg1DhzddKGutTn4hNcFGPUWtZJF56w_7OxkGAvfllnaKt0CVRRjdSFGviWowqxdsWec9bK4bIIDkDmRmqdMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb905f6488.mp4?token=LX_gfc-VNMirIZMKhV7R9kyXrko8eunbIFSJSqgfKP2DWQZ_mWm_Rt8HFuOjnoLWb6ioiMhCX_BLPJKJb9fGVi61TMBRzuZGPufSVYSDDobTowcZwISyrCKY3uEw3to0hDM4kCiB_uir9t_UeInBKFYjbNWhhyORT3v111RJBSbRTkAfMRnyRwpRR9zETdbSeQxh8MopkuLnZRra9u6q_c-ZXXGrs1eNvDinM8avBQ0e84YLwf_Myxj52OGWbzE9opVg1DhzddKGutTn4hNcFGPUWtZJF56w_7OxkGAvfllnaKt0CVRRjdSFGviWowqxdsWec9bK4bIIDkDmRmqdMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گل سرگیِف بازیکن پرسپولیس به تیم ملی هلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/91619" target="_blank">📅 00:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91618">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پشماممممم اولیسسسسسه چقد خوبببببه
🔥
🔥
🔥
🔥
حیف این پسر بره زیر سایه امباپه تو رئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/91618" target="_blank">📅 00:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91617">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ck9E0ynpUWXSRXvCM7Z3H-lIw-gDRhF9xFaaqXNl9XchEO9WwOdPVPZQhfluIQTI8qMPzvUt7pvsRvCB3B_5yKfgpIjsILq9oRw13nsqlQdbKiKXYWUyA72NTh3RAvFQdSGmxItt2j4PtsVABDJkuHYUqSO9x2rJWtDF4S0yktJrVV--o6Vkq9c5G6ZMcoYhp-AsgFHYNwMroYmQvTJJ0ZKrwNCua4MI7Nn9hDCz0tPjwCDerqVlK2OdZEoPGN6U9zUHMxrmloCGpHWEKy5SFJkL3KTRLtfra8J5WzF4R1-j9XXBmsQHR3gfKe4s0TJsEfR0n69SNOnN3PRNjEc28A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمر آرتان، داور سومالیایی منتخب فیفا، از ورود به آمریکا منع شد.
او قرار بود اولین داور کشورش در جام جهانی باشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/91617" target="_blank">📅 00:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91616">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzfwOOpleA0hJzAX7_rE3TWYIeuNkMNDXmIdZVVkuN0OLulIoy0eM-8yMQPCFU5-Pjw6mQ7Y_Y95JfPM8fjt4zst-GsYYYFGhRM2peqHfQKinDLZd4KECe-dLhg6xIX2skaV2rWA6Xwb5HKZvjotHErI6pnwawt7HRx8NTeuq8W_CGs8BTKWnqL0d0ZrJwcyq4cHrff5ndGRX2xhD3ecsG0UvLnotNmPss00HUoVQ-ULwouIzpajrBMEm-sBFZTRNH6wo0v5GpP13dpxNGWl8scS1vePP1bKk8Eb9UhrFmlZN-2HNmMwM_hI4WWfepjLWsA0eHuqYZtVw3_lMq4CEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فووووری؛ یونایتد، psg، آرسنال و لیورپول بدنبال جذب ماتئوس فرناندز ستاره وستهام. تیم لندنی خواستار دریافت ۸۰ میلیون یورو برای فروش این بازیکن شده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/91616" target="_blank">📅 00:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91615">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REJ-XEr7NPp09pFxyreKqe3xIBYy9wnXxA8p_MBk1psqfD2dXs7cvPnOdUUj9LatXon4BT8WCndnWHWsO6zEcj8qFcU9e9Lec6c-i4PhGI_y0pv95lJiStm2u7Fx7yJ0RA4nCq_PHl-DbsRiDc0Nx-Y3plUNl2KlHus0XqrRCWC5o3qloDCtFp59f_PMplGdXgUmcz6MB2B7LAAMj_ikJAI6d8wYpFVV-_SuhjTTKbXaYq8EBub6JwfddxKK4fYUiox6qW7j3GoLMknEt2eDAuqr5lSA2vqYy519eDIeu8s8jiVrSr7MvPi6XCGhYcmJXR_2GqCNadNSOU425cBpcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فووووووری
؛ گستون آیدول خبرنگار مطرح آرژانتینی: منچستریونایتد درحال آماده سازی اولین پیشنهاد برای جذب رومرو ستاره خط دفاعی آرژانتین و تاتنهامه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/91615" target="_blank">📅 23:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91614">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9c9b54af6.mp4?token=L4pNR8DeXV3RB8jJBeJAXobNdJrb5q3dvZc0BCr2xQDXmxafzknnlkHmyDeXx8wI-XF4TfRB_wQPQd4rcxFb8JO0_Npgn8laBwLi8_bAOCr-GDgzLKsHzR41mW_J6CT9Oj_fLO0-E1QZtxeOttGxbl9j0lRJBH_zX-iCGLBvFVpfuZ8o0kzFSu8RL-disYwZjRcHvXtt0E_tbZr3EcquqDLYyp27FGJZaD3D4fvaWRzO9BiiE8SUbQBR5jsXhv4tJQygBosx3ySSw7-s1asuRTl_dad6Yv1RmA6_8H5UZgckje5JltOhuszimolVWyRiM-0iB_DnqJkir0iFhLJvRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9c9b54af6.mp4?token=L4pNR8DeXV3RB8jJBeJAXobNdJrb5q3dvZc0BCr2xQDXmxafzknnlkHmyDeXx8wI-XF4TfRB_wQPQd4rcxFb8JO0_Npgn8laBwLi8_bAOCr-GDgzLKsHzR41mW_J6CT9Oj_fLO0-E1QZtxeOttGxbl9j0lRJBH_zX-iCGLBvFVpfuZ8o0kzFSu8RL-disYwZjRcHvXtt0E_tbZr3EcquqDLYyp27FGJZaD3D4fvaWRzO9BiiE8SUbQBR5jsXhv4tJQygBosx3ySSw7-s1asuRTl_dad6Yv1RmA6_8H5UZgckje5JltOhuszimolVWyRiM-0iB_DnqJkir0iFhLJvRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چی زد اولیسه
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/91614" target="_blank">📅 23:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91613">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔥
چالش جذاب و ترسناک‌نیمار در آستانه جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/91613" target="_blank">📅 23:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91612">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4-Zz99jOCwq6m4SHY1uHigB08pwOUcPtZlbYU-F8L10bOmz9Z_lUrXMdfzttHH6H-wd0Xnv6gi6lFTD0SAZXnSBQpv1FWupHiilDHYT3Y-4LIXMBJkRcvXxhn_8mirwek0Pv4ar2USdpPS7dp_8WJxBIPcSRs8IGJ0M8qaCueW-u1reGn8HPysxoVzHdVQ4S-PmBlrPU2oOY2rHGSNGj--v0x1VQqnGOUzZvYWFUsWNsCI9hOvIZsrFJNVeNFohg7DXDdQVPLZZoqg7vlxvrHN184JG_wjpUw5Iaq5B7bO3CehyEyp1XfDHkPzFgrpT58mEEyAylk1Pud_qW2pavA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
دی یونگ: میخواهیم همه را در جام‌جهانی شگفت زده کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/91612" target="_blank">📅 23:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91611">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUWcSme6V_lQrYaAuLx11P01XAO1XWyWhM3k6MMOxlwBtax0mJfGF9-Jd982wRiCl8PKcSIplXUubgvFjD9p51i5rwJ-ak4DkBojmzChF8vIvTprGqpZnan90uHL2V7IRr90CPq1tWXfQrhlE_T4ZFguJNJltTGlfqw0Cn-0riZSLpf2oc3vuCMXYf245ErsK18X_lAa-9lqBs7wUerp5UxIUl3VSCAT4wJqrhBN9ZqNFUCbMcmzeYq7ZqCYq3bCMBJjfQ6Ws55uP957SC_3LHLSZNMnGpaxnIbRotEfD3UqCStkQKlvLpiBlSspmP9pc1USXS8mUSEIZInrKqzQoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
دی یونگ: میخواهیم همه را در جام‌جهانی شگفت زده کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/91611" target="_blank">📅 23:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91610">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-u6drWgG___NA6L4vXR93Lfy64EdagUnH1wRR5figihyyepMSBvXQMNIIFefV97T7zOEwpqtvde_aHxNfj3Mb-T6xk351QaeWymLPFiNRsWFLpTKBwTDa5pA1A49JBP362BlZmjQlBxcCbPtIjxRX-5mhl6wygz0bwD-OiKzBPE3OIjl3Onm5NRZZfjN2Bt1CD6nPZA9aQ8_dd8s1apNHT7nxXQmKyZRNCN2BKewhnbzFjXmDtdj1e-FnM8io9JPLZZWBw_C8Ao9lPbqQz2t6VCiFKXszz4ZyRlQVXuxJljN4JszW5B5t_uJFwn_6MpWTPH3ss2KRdZqtx6ao-nrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اولین خاطره‌ای که از جام جهانی داری ؟
🎙
یامال : بازی آلمان و برزیل و فینال 2014
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/91610" target="_blank">📅 23:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91609">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jT-dgQwUjmOTyBLP8ZwFgWfK4InpZrxzlKnoF5C8r31SilmiX7K6dpP87V4IykmItrhiyf7UGElKOX2HlK9IUc9bEexQqMrWsAbLBRgpUkFBD_hHL8sobchKd_FCc8LgRukgLB_o1JJxzYQE557FimB6GakFbeHcyhx9GWMcIEAVC-AD_gSGwC9yW6iXfnVuXJNIlJq-j3GpS11zmU6S49RozIwKsu1hkUSQT7sIfoQPDahiD6xmiklE9xJ1u7CfjuNx4NJyHylQaFl6QJkHqxW32IPwpjGzn0ALdR2GP0sHnvUlr70piG8lkF4niV7ZR6ZIgav3_-e8bvAgD8Wt_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
| کیلیان امباپه دهمین بازیکن با بیشترین بازی برای تیم ملی فرانسه با ۹۸ بازی ملی شد و از لوران بلان، وینسنتی لیزارازو و کریم بنزما پیشی گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/91609" target="_blank">📅 23:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91608">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d43547db82.mp4?token=FoLiowOkxpTS3PuZ-ELkZr-nJMMISgwa7TvRd3zb7Ml0RCJbbgfz23PjyCmrR-WNHgMa3Dne-loaU7gG1zc6yI-RgStgR9WkaTd8wNEKwXbC-wDF4EB_M7HhV7oM13p4Ev2u1KgU_BEJpolvyPWfBsARoDzwexMZG9yVtC83H1u_UMmr5sLRVKKIrdU64MweMC6ISaU3jJ5_Ia_Xr6_7_pj3jAzgDMDTbFsESpFwPw_wnc3JRZ7p_UKspQhA0AD-ateDJ5_GL6twuMhjSvXWY9tdqVTcNS7EMV8kwrLGQQqMMTxWt8cnzZr0E3q5tLLPFMpTQFIoWA4DFiA6S7fJ5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d43547db82.mp4?token=FoLiowOkxpTS3PuZ-ELkZr-nJMMISgwa7TvRd3zb7Ml0RCJbbgfz23PjyCmrR-WNHgMa3Dne-loaU7gG1zc6yI-RgStgR9WkaTd8wNEKwXbC-wDF4EB_M7HhV7oM13p4Ev2u1KgU_BEJpolvyPWfBsARoDzwexMZG9yVtC83H1u_UMmr5sLRVKKIrdU64MweMC6ISaU3jJ5_Ia_Xr6_7_pj3jAzgDMDTbFsESpFwPw_wnc3JRZ7p_UKspQhA0AD-ateDJ5_GL6twuMhjSvXWY9tdqVTcNS7EMV8kwrLGQQqMMTxWt8cnzZr0E3q5tLLPFMpTQFIoWA4DFiA6S7fJ5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازم اینترنتا وصل شد گیر این فن پیجا افتادیم.
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/91608" target="_blank">📅 23:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91607">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f21c49fb96.mp4?token=CwyZJSjMEgqjtAtv9WmZ4UTz4RRy5yg8AP2b-uJQoiGMuy9dWKD9uqj3Br0XfOHJ0Xe9ELwZee1HVWEVXLj2TjPh5di2anWbVspkV_itJgtfIWp8EY8EzYICTAWxuvk4voYTr68aHdia6zw9L0b3TbPoLPl44QNzvdTFpQ5uLY9ng-XimQG_2N2nWYxwlNkjXQ3ezDVmHRcaGj9gnLCcj6xpzGYVjckDW3kbBa0hwVjf--C326YMpVdjPoAIQAV4acbPeT_WhveUHUvpvSSikOQ5EOeftCkp8RoNWFxSWUlsZDPPuAv6izS7KUN4D0Pzw9J_oQsSqk8GFoM28km8Yyo0AnNU2pOVj9W5f_oNnE21hsp0nZTLIhPEqU0ZEp_nLaA51CsY-5mdTUGU-pZkRACAyFBj3ih0ESKQa2uBlcQ1xY6VAW0p8p99avmCHBqR4W8_5fKawLW5G015G7O5yAIYbp2fQUQZOesNqy0QEne1m1ozqPHrWIrEbBB9f3GtxY5RrxiJBqe6PRLRfU1_vB3yy8Dyi8f-vQZ0g-CNE_4qqRokuLdxUIKrdtvAyVw3OgRUskHQisCmMJIOUIrkRTS_Ot41p72QV2PFaY6oVHpZvoaKJO7qIjJ4rwda2xocsyKSeKTRhRV_hmUk3sOllg-Lq8mpG-qm-YPWjNCbyYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f21c49fb96.mp4?token=CwyZJSjMEgqjtAtv9WmZ4UTz4RRy5yg8AP2b-uJQoiGMuy9dWKD9uqj3Br0XfOHJ0Xe9ELwZee1HVWEVXLj2TjPh5di2anWbVspkV_itJgtfIWp8EY8EzYICTAWxuvk4voYTr68aHdia6zw9L0b3TbPoLPl44QNzvdTFpQ5uLY9ng-XimQG_2N2nWYxwlNkjXQ3ezDVmHRcaGj9gnLCcj6xpzGYVjckDW3kbBa0hwVjf--C326YMpVdjPoAIQAV4acbPeT_WhveUHUvpvSSikOQ5EOeftCkp8RoNWFxSWUlsZDPPuAv6izS7KUN4D0Pzw9J_oQsSqk8GFoM28km8Yyo0AnNU2pOVj9W5f_oNnE21hsp0nZTLIhPEqU0ZEp_nLaA51CsY-5mdTUGU-pZkRACAyFBj3ih0ESKQa2uBlcQ1xY6VAW0p8p99avmCHBqR4W8_5fKawLW5G015G7O5yAIYbp2fQUQZOesNqy0QEne1m1ozqPHrWIrEbBB9f3GtxY5RrxiJBqe6PRLRfU1_vB3yy8Dyi8f-vQZ0g-CNE_4qqRokuLdxUIKrdtvAyVw3OgRUskHQisCmMJIOUIrkRTS_Ot41p72QV2PFaY6oVHpZvoaKJO7qIjJ4rwda2xocsyKSeKTRhRV_hmUk3sOllg-Lq8mpG-qm-YPWjNCbyYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این طرف تو جام جهانیم ول کن گورتزکا نیست
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/91607" target="_blank">📅 23:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91606">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92d1d72e16.mp4?token=KyF_124djX8jX4nOM1h3prJKFzwIvHT7_NGcHGQVLFZ8aqLJ5N9e2QhDPRh9Be0JOdICCxlpHaCyE6kc1itJGE6jE3EtE7_9gpXlG_mnN3nsAf78ABx2FFjS-UVxD7GymNqgf9Qrv0dnUALN8YWoiYW_SvQkEuGysPBCT3GJ3pfuxToNBx1v0vzwRYR0C-_Mzl5mghGaRA2NUYmmfHig-bZ16yPDK6yoOxtXi_uUJfNmJOvjTmTkF1A_vSdQKVXMyddNACr3xNW7cGZ32Zk5pOFvwx6SceZ-t6RrJ0iWkvMY06lS9cbncPA7e7sIBSEMnVILYUD7qId3zlsLABdu1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92d1d72e16.mp4?token=KyF_124djX8jX4nOM1h3prJKFzwIvHT7_NGcHGQVLFZ8aqLJ5N9e2QhDPRh9Be0JOdICCxlpHaCyE6kc1itJGE6jE3EtE7_9gpXlG_mnN3nsAf78ABx2FFjS-UVxD7GymNqgf9Qrv0dnUALN8YWoiYW_SvQkEuGysPBCT3GJ3pfuxToNBx1v0vzwRYR0C-_Mzl5mghGaRA2NUYmmfHig-bZ16yPDK6yoOxtXi_uUJfNmJOvjTmTkF1A_vSdQKVXMyddNACr3xNW7cGZ32Zk5pOFvwx6SceZ-t6RrJ0iWkvMY06lS9cbncPA7e7sIBSEMnVILYUD7qId3zlsLABdu1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهکار ریدمانی امشب امباپه
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/91606" target="_blank">📅 23:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91605">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PlR9T88ejip__b9jZWDJnKel49kbyAJ96lHcvpRXKDZqzZFhoBDSj93-nVuc1QBFdr5KZAWNGy-lI8JPQybzZLY4iA5Hub4-MdIYKvmR9yshOetxVuVChtmVhCIyHs4yUdNuPJA5EO98DqblTgh-uzkSwn8efnwd48ZNYUi98sfd4BxHgE0MTLt4NmESrnCWDTuF7M3XYipJADSYcEaq439fUARG8aiUFoftkFk3wytc2Y7338DV3k31CuQiQM8YSYNS4L7jNWmxiWG1R7iEKJrV8_h0FQpL2NiDd73H49Dsc5aZRlNIfeLDCNbv3BAhLFFFQBUx0hUS2PaFbYexkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فورییییی
؛ در نزدیکی کمپ تمرینی تیم ملی سوئیس در سن دیگو آتش‌سوزی رخ داده
❗️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/91605" target="_blank">📅 23:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91604">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37db48d9f1.mp4?token=h5x3K4eqaeHnANTi3egFZa3x0MPv2T8d5pUTLLfnj1PsB1gJhTfe7zkZ0eD6vch509Fd2kUU33-Tp8gUiT2BAzvgBg8N9pANe0gy1E_0nux8T8ONLibKk-P101KbbMD6izV6ku9FvLH1NVAzMujDwLwd-a1aczJyfQDgwJ_RvSSaMrwltm8hFjx-2ciuXdY4muClLZVA-YNGvCcUs_ASVg-NQF4WhPqPRAVcPhYH8czWIMZFimhKrEOJUogrjbHVGb7ucnd6Ehk6tNLsGIjwuythI3g6uOecGpT3ryJtIFMfud68R7wbqcPCLeH8IdbaLijRQsdE4IkOqb4VU2GnAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37db48d9f1.mp4?token=h5x3K4eqaeHnANTi3egFZa3x0MPv2T8d5pUTLLfnj1PsB1gJhTfe7zkZ0eD6vch509Fd2kUU33-Tp8gUiT2BAzvgBg8N9pANe0gy1E_0nux8T8ONLibKk-P101KbbMD6izV6ku9FvLH1NVAzMujDwLwd-a1aczJyfQDgwJ_RvSSaMrwltm8hFjx-2ciuXdY4muClLZVA-YNGvCcUs_ASVg-NQF4WhPqPRAVcPhYH8czWIMZFimhKrEOJUogrjbHVGb7ucnd6Ehk6tNLsGIjwuythI3g6uOecGpT3ryJtIFMfud68R7wbqcPCLeH8IdbaLijRQsdE4IkOqb4VU2GnAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
زلزله 7/8 ریشتری‌ فیلیپین اینجوری باعث شد این 3 ساختمان متصل به هم از هم جدا شن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/91604" target="_blank">📅 23:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91603">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45f87b14f6.mp4?token=R9fA-swFTGcA5H7PW7-F_VI9kXyf5imjp82HVQ94gVRU7qa6T28F5izfUALOJHBGBP16hZXbbtmD3zHrVuCXvvlFfk1NmBsZFUSUxLP3htv949mX_7oVFwTsIje4AqkQOAJHB-J1hPv15YImYts90dLi2WfSGllZsdTP8h67e8wy5snplxbW6LIaMSfmYpUlm-iKOivkNg4ccn4HPa3tMe6g4m_R7bdshIZyrwuehhZoS-7WjEh8KDid6A2YKOEM3fIj0UrCDR8FbUTr3M2zIfF8WVpYEKH3HISRZ7HjiXjEpSfHqbS-spDZabhVl5l6tdfcMIPUcwIZNMDzrzhGLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45f87b14f6.mp4?token=R9fA-swFTGcA5H7PW7-F_VI9kXyf5imjp82HVQ94gVRU7qa6T28F5izfUALOJHBGBP16hZXbbtmD3zHrVuCXvvlFfk1NmBsZFUSUxLP3htv949mX_7oVFwTsIje4AqkQOAJHB-J1hPv15YImYts90dLi2WfSGllZsdTP8h67e8wy5snplxbW6LIaMSfmYpUlm-iKOivkNg4ccn4HPa3tMe6g4m_R7bdshIZyrwuehhZoS-7WjEh8KDid6A2YKOEM3fIj0UrCDR8FbUTr3M2zIfF8WVpYEKH3HISRZ7HjiXjEpSfHqbS-spDZabhVl5l6tdfcMIPUcwIZNMDzrzhGLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
ایکر کاسیاس در مصاحبه با روماریو: «مسی خواب و خوراک رو ازم گرفته بود.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/91603" target="_blank">📅 22:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91602">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgqmHYBwEbu7G6RyP8WsAIYqp05gWGdGeJzBGv6CuZ9FOQ_i_51PyZYbrDFBQPQ9oqgxjTUwI0JMV7REd_A5p6Gd5vap3Y-RqlrG52d1ftSzY_eyiy1hhvQtJ4WNVCnt6zDQaJK95W_uLaPTOatsyMIZu3ZVKCWvvT7M7qLSbR28kg1tL4z8A20FHdpcJ5gmM2SZkCy9_MuskA31_nPsp-j_Mr4A4MV3w7JwlAEGt2PrdKS48MNXTlKHa7-5OAGTzbudZO54xnrDamyiRSGoxxlnVvpAx5tyYfSfVmFgV2yea6pQiVjop__cj7MCcTpMusq7OZoHUC-GFTpf6kAsKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برونو گیمارش:
«برزیل هر تورنمنتی بره مدعی قهرمانیه. پنج‌تا قهرمانی جام جهانی داریم و این اتفاقی نیست. فقط باید تمرکزمون رو روی هر بازی بذاریم؛ اگه همه‌چی خوب پیش بره، دوباره قهرمان جهان میشیم.»
🇧🇷
🏆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/91602" target="_blank">📅 22:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91600">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b_ujcCT_4bk9epsAC3ZbYoXRoxbjOgSehDZWAH4L0ZScr--2pxH1YG1qzwQmBfUlaIPMJPlw4bHu1APGQsAx7GvYXscAfh4R0MPrjHRHCpijjnO9oPw7oFNv0a6b4ritMZpNNuaX6GpbiHq8I80LBoXoYdX6rlKxn7v4XnO_MVk4yssxTUmsEqC4Vf2ziZoxL0l58ESdIyN1u7RKgJlIXhh_5TAZZApOXmZbaXBThmGPBi7FmVvOat9vEuE06LS17pIb4Q38DqgcxPxmsmXywOM7Ie84nVF-fV3AoUFtmbtnc4MHLWzGhAnuGD7p-F3RXJurJIZV_9-IVCJp0Birng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nDhdnTG4K8xUXaEpeT7D6KCFMXYAOtQWkyo1Rj3cBbUWWUkztBKgWnLQ0G-P3ua43zRaii_GngtSXW1ilN-jPf0eDJBcneyLix_bD47XlySRDwCim7EXviF9tIW0GfsIjIe7OuG6WMAbjU30wwgh5IM5hiIMiqGDjpSEPe-_BJYJ-Gpe8npf-mCUjsWS2pSijXqvyOkLOqzD1SZvnwiuZzw0GN10lJXDd3VJldOCFf8uKb9n0q5lvhNjI77fpG4k08L5IFRTwJnBQNywLcUuQprWk9MSR7JSvJGj4NhRx63kXJ-mbfFG6gQO00HO-dGC1UEgbC5LMDJM8Wui_ZFwtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
خوزه فلیکس دیاز :
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گواردیول میخواد به رئال مادرید بپیونده!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/91600" target="_blank">📅 22:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91599">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCxfnwyZTbijmtoDUbqbEu6QEgUkKIxXjaAyn6sVKI3fVPiyk2L4LGOyEGYtcDMFz-v13gDcyioVnvzifZOrjoSylkMtSiAwCGQPGL90FCggwOBhlGkOFdtR2cV-hyHg2I5cII1_6CySOwhF3Xf0xQXqUlLlGqOZTfujPM0bjjQQ8edS7u6M9YKPkFQmyBQs5w0MjTtoh7-9Kuc_15PPIckQSyC8jm-EhuFQxHgzLkfsVfiubsfAbmy0ldRkKo4VmxJ-CS8cNs4d6HhqFVQUS3HtHbtmtIpyYsM4o47hEJn_QVXgOkwjROHjkw6RpVFOPk4KG_DLxxvYzpYhHHLhUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
خوزه فلیکس دیاز :
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گواردیول میخواد به رئال مادرید بپیونده
!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/91599" target="_blank">📅 22:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91598">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q61Ovr9EXDIlncjpghHPTI5QN563ApXdoetAeIIVCZ4Qp04RrtGI1CnHSFrhPPIyTi3qRGH4VhWHWrq6yBHSJT3AyGZ0cGin5vRcnZDHatPDqDNAr745GOIH-3AfefgAw6cSdW4hB1faIX25KBB-yRJ6bp1ZFJrHsADyZaBWie_CxifjSbqcTsYpd-Q3D4gDCiBKJfRw5gASGK7IVVpu4_pvrpFpYKVwz2XfQbjhn5bl5mYM3yQsCf2rE4L8C0PtTvs6Xz1ZFJYG82tEZZ_8VAT33IJzzmJBn4STFIY7ZWeU7mVdfMMW_FPuOM6ktys6msZ9-EsnVZuE9IztlVoPxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
فدراسیون فوتبال برزیل: نیمار روز دوشنبه MRI انجام داده و آزمایش‌ها نشان داد که درمان او به خوبی پیش رفته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/91598" target="_blank">📅 22:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91597">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/svgujdQ3nKQENW07sM7UsXa-WgD2Yms1dHWI6QLptsQd3EIgEMuznnN8bhqJjbJ-aTLIW_7oayTr4y-afkyOQXX5MRbH_kE_Lrj4CCAVWdhMUZa26VbCFYz6vVQH4bs1rL1KqFRakoWf_7_ChERFkf6xpZotsxS8CyPwa8AC5ygPVPOXTLeMSsvPzWunAqbhcfGwZ-2evUn-tBaIiKdU08MYnuoFt59UG6M10tTJooc1J8KKqdpxTZZ3vjYdfOXVxMmgyZ5lvlFMJHJ-FKA7BvI2QccQy_AAGkILgNwsuA02MHYckAPEP_lhnxe-MhbgAj7AHVY9Sjd_PoK_hX27iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
رومانو: برناردو سیلوا تصمیم گرفته مقصدشو بعد جام جهانی مشخص کنه
❗️
بارسلونا و اتلتیکو مدت هاست که با ژرژ مندس، مدیر برنامه‌های برناردو سیلوا در ارتباطن ولی خوب هنوز با هیچ تیمی به توافق نرسیده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/91597" target="_blank">📅 22:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91596">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfYH0Trhwkf71JPUDzf2oksXlMyAiN29huopS8ZvDQtDBDMq_ObAHG6vPkhgVkYV0HpFNE3pAQ_ab8Xz0I7nsV8gCRayXNLoMsQp0-iKbPA5pJWiqyUwXJRhjGRje40yu53wApVmWg4r4KGHASO-AIrT_OKbwhjVXVbNHh8N_dIY2qCl_ai8OGZhaugRAfNA3nNqOLyvJlyI46-hVCN2tns-fHvBGO6K9pYcO8GX4HfBLg8nFJRaTDvleRarbhYhfu3vs3Wx8PRkPSnMjCwu1iB-i8f7at2thVfZmy8-5oE5br71CAfA9bWflPEk0h7iHo0P4_aT-vs1wU5rE1pxsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
#فکت
؛ مسی زیر نظر اسکالونی داخل تیم ملی آرژانتین در 7 سال اخیر جام های بیشتری نسبت به تعداد شکست‌هایش داره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/91596" target="_blank">📅 22:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91595">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70f1d33e7b.mp4?token=OAkVM-VDc5UN46mnQaytO7B5sR3KoJCLYZJXgT7dZYWZy_X4OuLVJFSm3Fisoh2o_4PfPVREemNn7sdTHwaEjo4JLCFcwIr50t06WqTlH-NcaLpVYVCQgFQvV0nHk-2-R9kmCn_4fE-wKYEkm127KXjsReCa1skYW7Fo3Y8WkcAZSsXv4HNtp4y1pMpKmk3ScMdamUZSMy9688cK56TApnDZfHDKPvNB3WD-EAlV7g64bedyXJ_X3SWq0zxVJxYH8LWuxOcnRTW6w3Hs9gpGHmtNYOuT07JSRntUJx7MF8d5cwUOQnquScWpI1FehrtKOcIAeFLnJcCk7DDcddJ3HyUc4JF5nUEOEHRm93JoYMxlcxEDAmo3EVfgUzkT7jQBqbkhLD3yvm4-cjbu2skVudIKJ6ZKFUb3qEpFeurWKb7G1HRalljAF0KY8QPfuBy4LtdEFpp4CiXpiwVp0Xd6VTn6iMfCsvt8mQlVvgbVTmh13SxdUh7koVFS3XPRMCXJA3q_HV8RFWd180bF7mmx18eQzuoIM0lDAJfxVhPiZossizUQRCNQjJ-mg2ijwyvNN_JOzy-GGdjM6DRv1Jar02JgM6Om2-Fs0R0plp97zCJIYXQAc-6uPm4Bp5KQZ-nVDkcFpangr-Wyrv9v4MoHMedvFwRsp4ubWhoGk_B65rM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70f1d33e7b.mp4?token=OAkVM-VDc5UN46mnQaytO7B5sR3KoJCLYZJXgT7dZYWZy_X4OuLVJFSm3Fisoh2o_4PfPVREemNn7sdTHwaEjo4JLCFcwIr50t06WqTlH-NcaLpVYVCQgFQvV0nHk-2-R9kmCn_4fE-wKYEkm127KXjsReCa1skYW7Fo3Y8WkcAZSsXv4HNtp4y1pMpKmk3ScMdamUZSMy9688cK56TApnDZfHDKPvNB3WD-EAlV7g64bedyXJ_X3SWq0zxVJxYH8LWuxOcnRTW6w3Hs9gpGHmtNYOuT07JSRntUJx7MF8d5cwUOQnquScWpI1FehrtKOcIAeFLnJcCk7DDcddJ3HyUc4JF5nUEOEHRm93JoYMxlcxEDAmo3EVfgUzkT7jQBqbkhLD3yvm4-cjbu2skVudIKJ6ZKFUb3qEpFeurWKb7G1HRalljAF0KY8QPfuBy4LtdEFpp4CiXpiwVp0Xd6VTn6iMfCsvt8mQlVvgbVTmh13SxdUh7koVFS3XPRMCXJA3q_HV8RFWd180bF7mmx18eQzuoIM0lDAJfxVhPiZossizUQRCNQjJ-mg2ijwyvNN_JOzy-GGdjM6DRv1Jar02JgM6Om2-Fs0R0plp97zCJIYXQAc-6uPm4Bp5KQZ-nVDkcFpangr-Wyrv9v4MoHMedvFwRsp4ubWhoGk_B65rM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یورگن کلینزمن: در فینال جام یوفای سال ۱۹۸۹ اشتوتگارت در برابر ناپولی، با دیدن گرم کردن معروف مارادونا قبل از بازی، شکست خوردیم. همواره او را به چشم هنرمندی میدیدم که با ذهن خود درگیر بود. این ویژگی در داخل زمین برای او یک مزیت بود اما در خارج از زمین او را گرفتار مواد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/91595" target="_blank">📅 22:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91594">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rsN0NcvzKEj5SaG0p7Bkfs1WFXNEf3RGb6KkHJn7RhwHq-D5uAzyvRhJEg8GmbEZyHc-8R2K1LMPLVNOo_LMExZNjGahlELTIl-ZY1KORVUCAzU69Wc-Whgq4zIwcQQgg49O-rDQy-lI3ovTUCDt1j5PJpiNCgpDkRu-vzG9nFDdXauMzdb2vd_xupDmOTp7dsH_0ewvifS146RzLKP3dYr93Zh4RpNPfq3DD_wuCKh7g7L-zroYCElpwG9rGOjWqZXoQfrX4dKxRr6Xd0guAZg6prleAXUAUrvNFJ7y5sk9VcMl4I5-57zcwowjhu1V4MjYSNGc3rR9G13oRnnXgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آرژانتین
🇦🇷
-
🇮🇸
ایسلند
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
بامداد چهارشنبه ساعت ۰۴:۳۰
🏟
ورزشگاه جردن-هیر
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
آرژانتین در
۱۰
دیدار اخیر خود،
هشت
برد و
یک
تساوی کسب کرده و در
یک
بازی شکست خورده است.
✅
ایسلند در
۱۰
دیدار اخیر خود،
دو
برد و
سه
تساوی کسب کرده و در
پنج
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر آرژانتین
۲
.
۶
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر ایسلند
۳
.
۵
گل در هر بازی بوده است.
🧠
وقتی نتیجه از تصمیم مهم‌تر شد، تفریح تمام شده است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/91594" target="_blank">📅 22:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91593">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxN4rUHtrkna6dO64o5FP4tBqsmt6ZhJEDZX_iIMq2W5EDPhmj4qyOfZGOvOwbDIQMJdxL36sbjXzCUBIXjXvmnXeP5Ajf-VRH6Nwaky4rEnoawpCLit598lKvxQfcVt2eyD5mwPaOqt9E7HWMHYdSqSnNQnbfrAVBVeHVr3aGNqb6d6cz_PIxia0WVmiA6SBgHM1wFyrdbStdJ6hT6Wq5dxu8AF_wTHU8lY6aofGN_5uBA0ZiJLDMkIXVtOHf4rEsKeWfWlTl68L3s8znHJYeDqjjO3-uyZktD9Yk2QIe2C2NHXrPXownmCQickzq4E-EDBdbkW-kUvGICFLrLF_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شیا رائل ویتست، بازیکن آمریکایی تیم بسکتبال بانوان استقلال، با یه فرد ایرانی ازدواج کرد!!
چرا اونا میان اینور ازدواج میکنن
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/91593" target="_blank">📅 21:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91592">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxOBNCW5tQkTopM3H0m3gRqJgVHe-JguoK3-JIg2HSvGV-80g7dAU_GMzcRUV1HVyRFnk29uXDCVQXhoGVTsvL3dwlasOHw2Fiuscyt0FPewgk9WhKwr5na2SdDmtDS5T4UI4U6LGCzcCVB77hUvqFVR0rXZHCAxRgGMlMm1XCYn55cWRCwq8iXOED3Ex9sIEc_M7iqBL9r_-v8o7z_8nTxs9Jx4wPp70WpAtnVeetG5aPYL6GlnkV7HrjZ1Ktv9woomDt6HU9JxTskIax3HofLKBGTyphOvU3ddxbNr16x8SFfjd8S2GHriBziRu8GMxUn-kDSaLodBI8qhUIRVMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشرف حکیمی: به مردان میگم دوستانتان و همسرانتان ممکن است به شما خیانت کنند، اما عشق مادر بالاتر از همه چیز است
❤️‍🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/91592" target="_blank">📅 21:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91591">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RI9a9QKr_sIjmJzhGe8OjUqQ2Hf09_PuMX4LR_InNmNQ4QR5IIToneB0YHUKgkb8BRyPzsnxggMqFh9NWwIr54FjnXxLzG9O9DXR73IK7bckDIBdp-TUh06WcugI8HifiK49mpegKS0R7iGTJHOL-VXIwByOFKtoHR7max184U8UEq-oNiXVeKtvVxC4cFme5j_ozy846RK5UKuPJm42bJReYuZ0PoP5KYjGsnEo6ZJyjmvEDzXI08PF1Pu9pWl5JMq7r6avYd_5at1FosVwbNcsAOkEuZ18vU8egZMhhcUYPxZcJM3JU3x7Lb8x0yV7M6GKNYFp6DyTKXzWmiHv5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری از تیم ملی ایران در جام جهانی 1978، آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/91591" target="_blank">📅 21:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91590">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7evckT_t-iQ4dTrMgO4aUYYLUAtYp5bG0YPZk2GSVv_YdFHtFvCXkQoD3VjPz-JqjbNaxU8kRSHlipKWAMfpgDm_8t97ILva2AeAT4LVbmVc16q1wMOczzcVlOXoY7RJ1pKDYUFQeyjkPHp-V9-Hl6XjpSvdGWprycamjPefDfksMWNVrvxv3VsFXR-gaxmH_So6noGY2UJoTOPvu-PocNJ_Wr4dWzhKW159rF2nqAfcrrKcgCIzUib9FpN_BcwbtchiO4i-klPuOh78K9T5hndrp68xj8HvTPJIEjghjgijxSCAmhDWHJ9yQGvVWIccvI6Ok4qqk-klpjeVCmUPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قهرمان ⁧ جام جهانی⁩ ۲۰۲۶ کیه؟
‏اگر جواب رو می‌دونید، وقتشه که در لیگ پیش‌بینی جام جهانی «همراه من» ثبتش کنید!
‏پیش‌بینی‌ها از امروز، ۱۹ خرداد شروع می‌شه. رقابتی که فقط به شانس نیست، به تحلیل و شناخت فوتبال هم بستگی داره
‏اولین پیش‌بینی شما چیه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/91590" target="_blank">📅 21:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91589">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPP3sf21fJbso8fJ8S-72GVsbTrft6YDzXNsAihkdfLOU6Q-oN3NY1rKy4D4GKtNgCOEWz0bP9DD5FK5_v252bzWfnvPDbKyYOptGOa6PEToPKyFZIO1vPEUEP8rXdmtSni-_GSj34fIeJ4w1ThQy_aZrCo8v1sfsoekLjqIhtfOY8ge2W-emTdPuibqwleRSeHQlAQ35zsib4pvi8NXDTXJrGAzkQ6cHs_j6-l_jMhMfUhSMYIwqHdJTh-ztWyenO15PWy70Tz-VaeNYBBuB6eTqkIf18j5IMu8unFGUhJU3H7t06yDGFfvppLJe2BcdXIy1HxJZugHqKpM2xLMWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🗞
اسکای آلمان:
بایرن مونیخ در صورت داشتن پیشنهاد 200 میلیون یورویی با فروش مایکل اولیسه موافقت خواهد کرد
!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/91589" target="_blank">📅 21:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91588">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4_1o069sbVow31jACATjLpL4lMvjSooppCwZtS33rUkOEiGqylAud7Vq4nN7ziGtgyRDCgP8N7XsjOjNqQ0fRVhbgPanZRpwFjnf7Vm-vnNj2lx6jCTgsL8sJSWsRXp9lg0T8fT6s3I8CMGhUUstbtckFq3XuVoZowiUWK5NutS4J91PiEUoAjXFsNmEJJW7tY6Tp--_Z-MkBlMrWR4ZL1H_5krgVq1CCuVg42TSij0ZRepAt_meoxewjSCuy5FDOJeXzzahvHX7RmCH7si8HtrNJ8O5PHVX--iSB4DcApQ_nQtkM-l0LQfG2RjyxLMp1uSwmbwBNe7GUqircF4ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇱
تیمبر به دلیل مصدومیت از لیست تیم ملی هلند برای حضور در جام جهانی خط خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/91588" target="_blank">📅 21:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91587">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🏅
تاجرنیا و جویباری بزودی برای کسری طاهری و محمد جواد حسین نژاد اقدام میکنند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/91587" target="_blank">📅 21:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91586">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvYG7S-7yXF4wBQ0gzLM7bp1JosquKIusJMWmJPx7_j1vMWI2o0gdMGHK15GdR69RsO5zyLu0Q0hfrCfKaIcsT0pSZlXxgye7mpsiwUYKjEPC0lUOdlBm84_MqcfrPlL_qpChr7DJ7p_bFcM8cW40DjkMHtQdeXplcarYLj2QCvfgobRWn6Eed2yDnR2CeQ4DcATjo33fF8i_w3ZVjizyicbgKMt5-ckTxpBbxdd5V-NAxxnXJ16clU8U2hvUNAAveSa_87ulwUUXsRsIkTz8y2e-4G4a_LyMLpDRW5-BT6Kzlslt_OYHG5Bu77mR9oywpFpKz2-OfdgDJxYZJD7uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترکیب ازبکستان مقابل هلند با حضور فیکس آشورماتوف و اورونوف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/91586" target="_blank">📅 21:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91585">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HH2ib6qF5R_ehWoikvdAX_U1MnLY0CZ6hMkPuO9x1rU_qILm84hwbfQtma7IlUB5bWD7UW0McR2lKumz7FqDpZZdZkA5uEwVJ6RyQaifYcDAgIkvfp7q2ZhbqN6Fx3UmKgpBkYFGlT8Q6PfldhVfwkfH2mdhjPAkjivZWSXXc5qPql0F5ltv_1jzDl5jNetEh2NRyOLcQfnXXrgwwRUmVGV8LJa4LghfsVY6GUbhrwvrr47FiHJKJCDY5veLkw9UccAyVlCoH7U6wM8yCP9anhowCTP0YIOdzKly5nNeudjR6YTALSQ7RXocG9rfYVS33t5K8pIUUFqgkWDb2lXV_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
کارلو آنچلوتی انتظار داره نیمار این هفته به تمرینات گروهی برزیل اضافه بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/91585" target="_blank">📅 21:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91584">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9bJoAD_4-ioDSFxHcLQvMaSOrXHrhXOGT8UVAEqszUQd1b_Tu5hsk23kFiMu9aHCb1ldbI7lniSr_b8xTOUXn9WzFCQH7eqo-LzHHgOhO5JCFRQa4nbV9rslwA2EecGzD8IjI4EXsCFFn0-37QAQf6Ja9_iNBeQ0ItWxTfIlEQVsteTka6iplOSUDX8qLM1jc69YIW3L10EG3FupmhLfJEtUvT45G4jfe3veomQaPZGEQpYE8MJVeb5g-6jrvagVeSsjf1nNkBqLJZd6QgHy5jbMwSXnhfiFACkAUEeHdTFdDyWqDkYFlb9tmM0CfpECzxYnQj1KxJhRHy52ISZ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنایی که بیشترین دقایق بازی رو در جام جهانی داشتن؛
لیونل مسی قلب‌ها در صدر
🫶
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/91584" target="_blank">📅 20:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91583">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJZg-I7NqsMJP5JvxHBjb-ayudhhNjOId1jOZidzgg1CBKyrvcJjRTNISm0zvuxDulT83qXJqdyGtwdRZ704MB01GBEFhXE0ThcfHlQgifxMur2nDmhEEjYi5ATxE3XwmK6h8NVmDEKQ00NR9UmEBtjbNt4GqFq1w-HT4LCG6UzQ2BhMdt_KG5pJ51Lzjvfhi0SozHhknMGuzN03QrhljtXiJQY0XFkdjJl5z0yI4EclGt365cd6Q5t6Cgl45FpbXmhkHcWH-TR7Fm5IaqSHJDa5ieaB2KzeQ5jYaZtB_VKeWKYybi7MXl_VVn7NC8RA3wjljIf14W_HA4YkpiieEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همسر سپهر حیدری هم پرقدرت فعالیتشو شروع کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/91583" target="_blank">📅 20:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91581">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/emtd5STmmv8L8aXqX1sGdAOyg8lVtebNfUrUQqTGXVDn87p2QfgVH5v6FJqgRKhRNa0YGOFFZsq41D3tpX4VPkudD-qoWsFFYjBx0GGHfUz4Rtv81y1LYz8aYZxudeMG_6zl25gT6byk4B5f7AfKxfXNdWAVR8eqBXH9P5IuPM1zbxQJwkqIzsevBGcT_tRqTsP4OB43RfvvGAiVaE5KyCGXrh6fshUtvkSRJwCif2b8crMSCM2xY3VQf1faNr6QSdFhPZZUpcMtEjm921oM8wlD4lENdXP7n_Xcq2-zosTGAUffB-Z3F1PiRFa1n4xZEtPGxHubqwoVM1-9wsjHFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/laZuUxRBQ-Rzyo-24dH9US9Zzd4L-jqnTbvy2P57PSf8_32qNiwoUNSlhRsUg7MIpM79EwSxRkpwf7V3jk8VDdLFlztNeP0MrPrsQ-fw7Q_Y_IWDGlQyZ6PJO91EAPEZdxveQ0DNYHV1JW6OQlyjmAaQ5lqFr6XjUEHlGuDNMAwBMso0eY8iR6Itbvt_AbD-QdsC9vROr5LPrh40y0AZLOr-mwtmGa_fIAyzqksucN75O7aio87ZvwQ_EDhSGwZtHe812C-n3nMLziF1_Y4Q4AM7ySfarwIpJujZ4Op8Fxi1pRhaauxIodia_eSVXR2tQZMyIcHI7tO-u3D6WYjXyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خدایا یا من پولدار بشم یا دنیا جهانبخت تو روبیکا و بله چنل بزنه. واکنش خدا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/91581" target="_blank">📅 19:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91580">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ab5cab715c.mp4?token=I2FbO9x_tCBHe-oNoG8WpmvT3DT37F7Gfos0zGjz_svv4XFIyg3M_3b3-r2HcadiKtpvtFXx8mCz6BRx9htEhtBhpINJ5hch3euEqW3PEIAAWsGkrcVXsvj6j4yqK5HvJFlTcfcvSlf1SGNegBC7UsiIa2Qvgz6ksWs5VtNLVBKHst1EiTNJCMc12U2r3j4VmPjAZEmYmH-riNwZULjWjD_kZp5J50Dra4HnHY_FyS4Cnbo7AEzDiQ5l76MuhIpiUFMsgBf9yD1lFRnON4nI0vcRMJAOk6onjs5izwXf6hNehX2Pj_r1p9Zavq2xN3-pKk22GwP4-3iKOtO7kr-rqg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ab5cab715c.mp4?token=I2FbO9x_tCBHe-oNoG8WpmvT3DT37F7Gfos0zGjz_svv4XFIyg3M_3b3-r2HcadiKtpvtFXx8mCz6BRx9htEhtBhpINJ5hch3euEqW3PEIAAWsGkrcVXsvj6j4yqK5HvJFlTcfcvSlf1SGNegBC7UsiIa2Qvgz6ksWs5VtNLVBKHst1EiTNJCMc12U2r3j4VmPjAZEmYmH-riNwZULjWjD_kZp5J50Dra4HnHY_FyS4Cnbo7AEzDiQ5l76MuhIpiUFMsgBf9yD1lFRnON4nI0vcRMJAOk6onjs5izwXf6hNehX2Pj_r1p9Zavq2xN3-pKk22GwP4-3iKOtO7kr-rqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخورد مقامات آمریکایی با بازیکنان تیم ملی سنگال
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/91580" target="_blank">📅 19:46 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
