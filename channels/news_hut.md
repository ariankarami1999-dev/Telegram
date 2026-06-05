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
<img src="https://cdn4.telesco.pe/file/IneErGZv4QmiBZWoqkdC5QVDewi_CXjRNhA98r2ou6B8t6Zzo3rYfPodQlbVVtnesRz3XrJQ6X-er5cMu_nUUs_jLnq8qzitOg1BaCX14xfKcIaxbqx187YvQ-E08lFOXZ3KXqqxGg8zj1danBEYZXkSQ9Nm7igGUyY3Ne4QKIDOkkJ0gv9r59GpUwiPLrUtY-tFL0WzD3PWC7W0aRcKkx3DFTg-nOhA4Fhuy6xOBIqZArF5JE4NU-4pnLgi5sH9y4lVBWyWJuQ8u7H_1DrEUl0qB32z80IG5LVBZfuU68NYFMaeTEU0p5SBWnLLJ3ZLx1-yIjmg-17RN4qVcR9StQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 228K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 07:35:57</div>
<hr>

<div class="tg-post" id="msg-65307">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">پرسرعت وصله
👌
👌</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/news_hut/65307" target="_blank">📅 01:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65306">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Barko VPN_v2.2.apk</div>
  <div class="tg-doc-extra">61.9 MB</div>
</div>
<a href="https://t.me/news_hut/65306" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👈
بهترین فیلترشکن حال حاضر ایران
👉
💎
با همه نت ها پرسرعت کار میکنه بدون محدودیت
💎
👌
پیشنهاد ما دانلود این فیلترشکنه
🔧
لینک دانلود داخلی با نت ملی با سرعت بالا
👇
https://uploadb.com/plx39j7b72sy/Barko__v2.2.apk.html</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/news_hut/65306" target="_blank">📅 01:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65305">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b30ed4f9c.mp4?token=J4HXdAOYDOUWE0-LG5seD5Wwpw8u94YnJAUFQv40SjgrNspW5wyF0HSDQTY2bSvpV4nBwRNbuz3cIgZKXcgQEy0TpYlXnMCHIBJYCv1cTeBEpdpVi4OLDukMmSVSWvHcD3oPFszS-eP9-2EJV7ReUgdcPW-KdSqZwqW8qeSo4l1TJOCuS3tI5Fr0kuv24WkrRPiBFTE4pIqqMFSIFmNwfMgkS6UNybGDgkBwLA75ZJRu3xBCd7ZwJrxMLj_FxpS0kj9OM0InlA4_AKVgUrQUpunRDLCBakbl_e9q1EpTzpiMDpznLlS6TlzU3O4GWMdWA4_BKbif6hIJRLA2MQ2Eow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b30ed4f9c.mp4?token=J4HXdAOYDOUWE0-LG5seD5Wwpw8u94YnJAUFQv40SjgrNspW5wyF0HSDQTY2bSvpV4nBwRNbuz3cIgZKXcgQEy0TpYlXnMCHIBJYCv1cTeBEpdpVi4OLDukMmSVSWvHcD3oPFszS-eP9-2EJV7ReUgdcPW-KdSqZwqW8qeSo4l1TJOCuS3tI5Fr0kuv24WkrRPiBFTE4pIqqMFSIFmNwfMgkS6UNybGDgkBwLA75ZJRu3xBCd7ZwJrxMLj_FxpS0kj9OM0InlA4_AKVgUrQUpunRDLCBakbl_e9q1EpTzpiMDpznLlS6TlzU3O4GWMdWA4_BKbif6hIJRLA2MQ2Eow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: من نمی‌خواهم با آیت‌الله ملاقات کنم، اما اگر با او ملاقات می‌کردم، برایم افتخار بود که با او دیدار کنم. من محترمانه رفتار می‌کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/65305" target="_blank">📅 00:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65304">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/433ea342ed.mp4?token=Ap6140bYd5a3sFYWYPUgJ7T9p1EesHVwr8kZho0Yuvtd-MX9wfVVR6nMTsk9hgXaWF_LcBDUhH0K8wP9jd6fuGozwwnBnXY4wsAw0Wmmbrgu8KIoWVEm24fcQeOc9OT1NAcjytVvmzwBG9uEZXNQfPSASGRZmRbVu5FDo4yotifOw2UqlbnECBWUMjR45SeST0NCwIpSZd4eUK166q26i_Fr3W6YnZKk7fFg8bvKJyfs2Rws3SHDnDdKtApxzHgmBnXN2RMPFJRov6kELql7Yph_QOu6niK5t8L5WdhjyUcKcWWXXjkxp2vxa2RaPUhUfGDbaxx28SN8_FUQwVyvBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/433ea342ed.mp4?token=Ap6140bYd5a3sFYWYPUgJ7T9p1EesHVwr8kZho0Yuvtd-MX9wfVVR6nMTsk9hgXaWF_LcBDUhH0K8wP9jd6fuGozwwnBnXY4wsAw0Wmmbrgu8KIoWVEm24fcQeOc9OT1NAcjytVvmzwBG9uEZXNQfPSASGRZmRbVu5FDo4yotifOw2UqlbnECBWUMjR45SeST0NCwIpSZd4eUK166q26i_Fr3W6YnZKk7fFg8bvKJyfs2Rws3SHDnDdKtApxzHgmBnXN2RMPFJRov6kELql7Yph_QOu6niK5t8L5WdhjyUcKcWWXXjkxp2vxa2RaPUhUfGDbaxx28SN8_FUQwVyvBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره ایران: تمام ۱۵۹ کشتی آن‌ها در کف اقیانوس قرار دارند. ما در واقع از آن‌ها در آنجا عکس گرفتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/65304" target="_blank">📅 00:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65303">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfa40321ec.mp4?token=H930gsDod75IUkNhCfJP02QgtkOoOmuo5_GJ-8RvsctnmoWcEQpp7yrwjSnVqGcckJ2v77DkXvLVoUQPWxseBPoaBZ_z25afQh5MmEQakepR8EWVWOjX_vy3YQyiOmQ7WmLWYrfKYMv8UjotkGJ4UmMHqO2QRKdwQhH7BYJtzgELdBybfl9q-IqKQZrILzbyTBeaviiJ3QWr1d9wJ3SgTPo9xuCArnn6w8Ut2doIw-mItC6EsEnbYQxsv0xJ52daHXgTP0E4cpd2Qa3fJPbvXUaRSQtBpXSx71LEyQJly39WcW0eCK2yHKyo6nLVJvPI2DIsUwD4iTO3ygLwt0b97Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfa40321ec.mp4?token=H930gsDod75IUkNhCfJP02QgtkOoOmuo5_GJ-8RvsctnmoWcEQpp7yrwjSnVqGcckJ2v77DkXvLVoUQPWxseBPoaBZ_z25afQh5MmEQakepR8EWVWOjX_vy3YQyiOmQ7WmLWYrfKYMv8UjotkGJ4UmMHqO2QRKdwQhH7BYJtzgELdBybfl9q-IqKQZrILzbyTBeaviiJ3QWr1d9wJ3SgTPo9xuCArnn6w8Ut2doIw-mItC6EsEnbYQxsv0xJ52daHXgTP0E4cpd2Qa3fJPbvXUaRSQtBpXSx71LEyQJly39WcW0eCK2yHKyo6nLVJvPI2DIsUwD4iTO3ygLwt0b97Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: حزب‌الله هیچ چیزی را رد نکرد. آنها با ما تماس گرفتند و گفتند، «چطور است که متوقف شویم؟»
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/65303" target="_blank">📅 00:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65302">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1eed315e2a.mp4?token=WV0N_F45SE9PO6ElXZc4Fzmc7glKZ9QydKt8LgifxREzhBmdcDZHwmjkvny94HjB2DNJNZORpQ-BL3IopxkoIN96stJ0SsXCx9IiLpAdxkNwNRPnYh8oUGv8lRrfYyItMwmTPeVCFHiWTemlLR0dRZ_5-NH1ZkQPOmyMPTSXsXirweyRLHqxU8lhUXVTNzOVutLPIYBfgZYuCj4CAWq3ayTAvs0seR1HR2trYB-1KxTAH-Kt-nSVHEbw3BIaFms2YAoPSKKx4_GmHwZxLaS0SS57SgLkomk-2fRDxyE0mSwsMdtfXwBWUxsZ9A2P6xSnFkinXa_fglEukmEhiV06yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1eed315e2a.mp4?token=WV0N_F45SE9PO6ElXZc4Fzmc7glKZ9QydKt8LgifxREzhBmdcDZHwmjkvny94HjB2DNJNZORpQ-BL3IopxkoIN96stJ0SsXCx9IiLpAdxkNwNRPnYh8oUGv8lRrfYyItMwmTPeVCFHiWTemlLR0dRZ_5-NH1ZkQPOmyMPTSXsXirweyRLHqxU8lhUXVTNzOVutLPIYBfgZYuCj4CAWq3ayTAvs0seR1HR2trYB-1KxTAH-Kt-nSVHEbw3BIaFms2YAoPSKKx4_GmHwZxLaS0SS57SgLkomk-2fRDxyE0mSwsMdtfXwBWUxsZ9A2P6xSnFkinXa_fglEukmEhiV06yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: من تا الان به هشت جنگ پایان دادم و به‌زودی یه جنگ نهم هم تموم میشه
شاید حتی بشه دهمین جنگ. فکر نمی‌کنم هیچ رئیس‌جمهوری تا حالا حتی یه جنگ رو هم تموم کرده باشه
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/65302" target="_blank">📅 00:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65301">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NW6QzzcH7sAByDqhnIgzfXAKywLp0F2OzgdNHxw_cECxT7S695axbNurYpxtNjzH6CypwR4r8gktUzOpZ394LzVo0DTLvfLLS2DXXMnKhGNJDBeUVXpD6DupzdJUZR5k7xUIQkU8tU_q17ZznZPRlVdRqFMvmN2DEPTOtGgHlACQrMSYT4nDSeHX-JmJMTv8_HWV5r2avL4NCHQhOwbeGMI2rI1Vx_YUGZYe-Hbpb2sAczwCqOqTOQqfFkTgA3KQoukS7-TUtrbpD38XyClw6qDUPPEdXMxtynEucxPziULYOxN0IG71-9MCJrSq8WZPPjb7EbC2faSquHLgjmlwxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تورم نقطه به نقطه سالانه برخی اقلام اعلامی مرکز آمار: از ۴۳٠ درصد تا ۱٠٠ درصد
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/65301" target="_blank">📅 22:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65300">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsiWpIoiWa59JCirB-yWGcp1RYcec4qOhsHaCDZI-ACRkhio3gHWYx8LQYrYEWCAVmMFKzKPZwQoalFkVx2uBAjapbw3dnM72phchMMKQ2jo8PoVLK8yMvCwvp3olmdsPTAguLub27THsX9UGLzBvzsWRsFFf80JzT5qqfW0He2fosXL9TXhp0KlWYP2ePhQ84w0N7qwY_vcRe3xqKTI0mrFGgOWqxWBleBVTRu0AFTRJHwISY6JSnaUu8W12RtgZBGiiR8HQzktoxBwtj1TxTsaep-0WyyHGuTSvxkLizv-HMtInhWl2gRdVxwGLFNmx0Zpm7GRJvdOkkML7722WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پرتغال
🇵🇹
-
🇨🇱
شیلی
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
شنبه ساعت ۲۱:۱۵
🏟
ورزشگاه ملی لیسبون
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
پرتغال در ۱۰ دیدار اخیر خود، شش برد و سه تساوی کسب کرده و در یک بازی شکست خورده است.
✅
شیلی در ۱۰ دیدار اخیر خود، چهار برد و دو تساوی کسب کرده و در چهار بازی شکست خورده است.
📈
میانگین گل در ۱۰ دیدار اخیر پرتغال  ۳.۶ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر شیلی  ۲.۵ گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: نتیجه مسابقه: پرتغال - ضریب: ۱.۲۰
🧠
پیش‌بینی آگاهانه، تمرین شناخت خود است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/65300" target="_blank">📅 22:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65299">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mSpLB7R954pqKR3nK0GbeGDKpAeTShzqNCzb5Bkem596pQ1aEmK5Mc4TZRozoL3wxbObScv7xkCEWcxD8FU3r2Rc0pcMYWfob4F1MKzs9Ft-EdD8BqDbyehStx_QLhU42SeDTW-tECbH1vtSmmGMTjdgYjN5QeEdTPlw2NjY7hstg3iBrQKrisQYYqoBFj5-D8lb_L_N8KInGRR6SuxjF5KVRM0I0Q4N7QD8qeusUi0Y9DLe1yTqg0uSht98LHzMHV2RTsyScbmYWQxYnjR8AKN98DTYQUKUsKHVg8JSgyPbr_AMvqGyl8HtQ8N6ZI6ykNLOmW5JNmUNCQMxa84iRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن های chatgpt، grok و deepseek رفع فیلتر شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/65299" target="_blank">📅 22:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65298">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7628778a5e.mp4?token=fybURIH05ezZ_KU9Ax9L6PW2EK18upX27p8MccGlRt2_x9n_RT6TDsKCXO6TCxbAYqG8MULPdv6BlXh1kllhsMvyeguMyvok_-rkvY5YOs6YcJfeF4mqpQbH4BpK5HGarQ4YIVxcBQTFpOwxi5bI8WGWTEyor0Q3smNa8N5u-y_mc5Mh6hwyHxDIYxLKCdifU-VzpJLZQr-J2xuD2iVXKdJV7_n0Hg2SdijzprVmHG9B2mLqKwUhf5BylaJxX4z-mv2d-bSom7R8zt4JEE6BUY_1sqvy77oeAeQVPQF22gyZg48PInvBVlB9TwUrEr_LCOXzR3sToymotDxicdF--w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7628778a5e.mp4?token=fybURIH05ezZ_KU9Ax9L6PW2EK18upX27p8MccGlRt2_x9n_RT6TDsKCXO6TCxbAYqG8MULPdv6BlXh1kllhsMvyeguMyvok_-rkvY5YOs6YcJfeF4mqpQbH4BpK5HGarQ4YIVxcBQTFpOwxi5bI8WGWTEyor0Q3smNa8N5u-y_mc5Mh6hwyHxDIYxLKCdifU-VzpJLZQr-J2xuD2iVXKdJV7_n0Hg2SdijzprVmHG9B2mLqKwUhf5BylaJxX4z-mv2d-bSom7R8zt4JEE6BUY_1sqvy77oeAeQVPQF22gyZg48PInvBVlB9TwUrEr_LCOXzR3sToymotDxicdF--w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روز اول جنگ مجری صداوسیما حواسش نبود میکروفونش بازه، میگه همه گذاشتن فرار کردن، هیچکس نمونده
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/65298" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65297">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🟢
سایت معتبر رومابت برای جام جهانی بونوس های متنوعی داره ، از دست ندید</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/65297" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65296">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jt5BlmMY1rl23oiPymSG8BHNVOtBKTjGkfjBSYOLLdvwpZx_6dyv6nwKJz2IEZinSnDhnjnyr835Uj_NxvSveyCud5Q3YLuNXpjVocLx8-DzDKwFbStMp5JPco0b2C1rwLTsdPCuUfgN4ROPzBZuDqlT7hFDdECRsF2ewUj8B8pvQBumHyq4OXrED9QAWwTMBn9DcHxwRFRIxGG5zHYXFwpCS7D4OTm-O1BKcD1DlnvY2EWqoTTg1RTZzF33D5POoJrZNuwHEgAmaJljkAzmnwHTVgFwos6P4-0gz9cZKzsIgKvradLGUqkf1wlZ_1Pctr2vR6jp56ZmmKzv_-OV0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💳
در
#رومابت
میتوانید با کارت بانکی ایران ، انواع ووچر و همچین انواع ارزهای رایج حسابتون را شارژ و برداشت کنید
✅
🎁
10% بونوس برای شارژ با رمز ارز
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
پلن وفاداری همراه با کش بک بی نظیر
#RomaBet
📣
‌
#بدون_احراز_هویت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⛔
در صورت فیلتر بودن از طریق VPN غیر از سرور انگلیس ( سرور
🇺🇸
🇩🇪
🇨🇦
🇫🇮
🇹🇷
👇
👇
)
🇪🇺
https://trentivo6402.bar
✅
کانال تلگرامی
#رومابت
14
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/65296" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65295">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ:
ایران موافقت کرده اورانیوم ها تو خاک خودش از بین بره
📌
با این حساب ترامپ از یکی دیگه از خواسته هاش که دریافت اورانیوم توسط آمریکا بوده هم کوتاه اومده
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/65295" target="_blank">📅 18:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65294">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qt7nduve4exKx4-lsPAwZVO_ec_yezO0Z21lqvcdXt7xXLOPhwIXzfmBJdvjRwG95rhZfAfApO5d_gC6bm3v4-W-OFYHB8bdfqhbL3rXRUzBOHN1QUhkqEe1TYqpRK6h9bMotPOlViZ6gsAbx3TdNYTxJqo7qbApxeY0hZfmh5I5lAF2DFPbAR0znmbYcUzIkYbSQ3h99SuX6S1_Z9_kA_TCFmLoOnAvRXu0OJ4Cn2o5MFezjVE9_18HDzyN_Ca5wlRzCCZqBwoC2Prtys92eOG_pEXuBw_XyA6tUeOiwXprGFSxNve8xUL5ymx759mbBvHbQ_nOYrjVWTvw8P7K6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
وال استریت ژورنال: ترامپ به طور خصوصی به دستیاراش گفته که در صورت کشته شدن نیروهای آمریکایی توسط تهران، آتش‌بس با ایران رو تموم و جنگ رو شروع کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/65294" target="_blank">📅 17:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65293">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlWqJHnUTJwIsAfpUOBHQyiFV2V1C_8PcQtZ8KHq6mAmN-b5Y6nlzvUIVVN0TL0JRtH8yjxTH2NIEKVu3GshZMh1oOhc5yqaVZPT_9_b055v4QOCnD6u2ohZjOsLgNWU8EGqFb-rzRqkxxH_9pdlrpr0XvIKDNhMchYXLfkrmHKgPvI8fjQf5x8sMdP1rsLY3zAdClK6ptpvRBnTDpEJoa9INACWRQEcFIOoz1Q8OmzEstyvrPnNocTbRREAEPqba7Fbxa9cddfUE3b4CGKuJt7Jg-7F6G9tByXvOXlWKFrnMW82AHVwAbokZsyCo6sTWTPN_4cJH5ML4HilZE9PRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/65293" target="_blank">📅 16:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65292">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2074c6ee2.mp4?token=p4Pm88pMnIS2Rqqcdg0CDRhtWE3agT47hTLIciGZ6Td6AY-8htw9pFw1ngcD0LGMsa4JVQIINty88bzRzU63WKqol7dpsLO3EQXe62HEz5A_evIrwR5D75CIvoEyMtX7pi_RdTBToo2ySbuPc8X0s4WafbEKR-9cc70AfsNa2Z0we-U98YmFUUK0y6Lh3ZEjufoN9MmF4D0DDmga96uJv1KP4R1nNJarpKTkrf24OD2fNhgYfaxyhcV_sphKYRENsyIjuh2fYS0p44jsgWAjMsKbsMfcsuP6B0kpSuUZK7gMZ05C9nzeVaC_5GDr1llw4BWZMGkhna-irSzU_Zhfmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2074c6ee2.mp4?token=p4Pm88pMnIS2Rqqcdg0CDRhtWE3agT47hTLIciGZ6Td6AY-8htw9pFw1ngcD0LGMsa4JVQIINty88bzRzU63WKqol7dpsLO3EQXe62HEz5A_evIrwR5D75CIvoEyMtX7pi_RdTBToo2ySbuPc8X0s4WafbEKR-9cc70AfsNa2Z0we-U98YmFUUK0y6Lh3ZEjufoN9MmF4D0DDmga96uJv1KP4R1nNJarpKTkrf24OD2fNhgYfaxyhcV_sphKYRENsyIjuh2fYS0p44jsgWAjMsKbsMfcsuP6B0kpSuUZK7gMZ05C9nzeVaC_5GDr1llw4BWZMGkhna-irSzU_Zhfmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
با اینکه آتش‌بس تو اسرائیل و لبنان اعلام شده امروز جنگنده‌های اسرائیلی اهدافی تو تبنین و حاروف تو جنوب لبنان رو منهدم کردند
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/65292" target="_blank">📅 16:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65291">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76fad04c34.mp4?token=kuRFKVI1ubI9vVZ_Dz4w_OUBuKbJDnc_YV4oSUFN6MCWLAvz3QN5fY4t2MzRef4oCIsgdD1oP6cUkXXtCBZqqIsrZTwv3AHTulGbF1Gbrue4Ey-6ihiSAh8XW73EHgB4r2USAsq3vt89Od-lXC-1TGH3MC_tbqE34Q54BkqCR0YA7dm8XfA1KFQkaFjWOrdidKLeBm3Bg2uquJLgcDDATT1X1bD-Z_Rcv2O4p9dan9ZJ47UsHA9lmdnMXsSvOXCgMsYkJUXZdamufERkQa_wsc_XEumu_zIe5yEYuwfZbW_y60jYJdDTA0QQzaInSt74q9gbFCuDF4M80znTlVxoOjqR4m7oHKahVvhP2gqcGoDptuFTMH4zPqRWbNUv9zMlr8AWi8b_rZznhy4lFPN9oRBZMS4R7C4ucnrOzGWHu1ZqXXKq8YlImSXLtdegJkoOJ_bow6WtocoaXzMVhW9rJTia2kOmfTzAQ6-ISc3EeZ35CRs1yl6g4gghUyQ2bM4LXqHp-fodBQ97-3C4tZXdYFbH50S8DVG4zRlbeA8jAg8cilRPQA6MbxmCv9FzC9cRceYgbXKsjpGvTx5Icj4ZhTsTpB9Ta30K29FCZD4vAujAX-carFlPcLqsiKMQRyWDkZgEByETYE5Ep5Gaz36siFyY1T34Y7E6Un9PsbTcAoE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76fad04c34.mp4?token=kuRFKVI1ubI9vVZ_Dz4w_OUBuKbJDnc_YV4oSUFN6MCWLAvz3QN5fY4t2MzRef4oCIsgdD1oP6cUkXXtCBZqqIsrZTwv3AHTulGbF1Gbrue4Ey-6ihiSAh8XW73EHgB4r2USAsq3vt89Od-lXC-1TGH3MC_tbqE34Q54BkqCR0YA7dm8XfA1KFQkaFjWOrdidKLeBm3Bg2uquJLgcDDATT1X1bD-Z_Rcv2O4p9dan9ZJ47UsHA9lmdnMXsSvOXCgMsYkJUXZdamufERkQa_wsc_XEumu_zIe5yEYuwfZbW_y60jYJdDTA0QQzaInSt74q9gbFCuDF4M80znTlVxoOjqR4m7oHKahVvhP2gqcGoDptuFTMH4zPqRWbNUv9zMlr8AWi8b_rZznhy4lFPN9oRBZMS4R7C4ucnrOzGWHu1ZqXXKq8YlImSXLtdegJkoOJ_bow6WtocoaXzMVhW9rJTia2kOmfTzAQ6-ISc3EeZ35CRs1yl6g4gghUyQ2bM4LXqHp-fodBQ97-3C4tZXdYFbH50S8DVG4zRlbeA8jAg8cilRPQA6MbxmCv9FzC9cRceYgbXKsjpGvTx5Icj4ZhTsTpB9Ta30K29FCZD4vAujAX-carFlPcLqsiKMQRyWDkZgEByETYE5Ep5Gaz36siFyY1T34Y7E6Un9PsbTcAoE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
فیلم جدید و ویرال شده از حمله هوایی آمریکا به پل B1 در کرج
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65291" target="_blank">📅 15:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65290">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-XPh0l_IM15R_0h3Qw84Kslmt0VUVNibWhrBr8mZ5iHEDBSSd35pH2zYhSIjhLAlFsrSRabRwGthyBxNMsofw1r2nYWkHtRd-JXEpHNkd09JakrhiIcrQV4TpMyK1lF7D_jXx4dTspQNiV8mPIeyLcGYUIBC3r-Dq-dOW-UW9sxI1QaQB2EWjMGJQnuZpiuU0HNlcSmepiM-mLE7SDJ1VWGgIaYRbl_jsozxJbzorqQqkBaE0oEQceSPlOMy8N7Sj7GF_fIhe73-qE3CmtqwInf9HONtE05aOp89MM4tMl_w1JYFh-zPoR5Q9KkbKL9ujFPKoTI1G0MXhsmUlV9Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تو ۲۴ ساعت گذشته بیش از ۲۰۰ میلیارد دلار از ارزش بازار رمز‌ارزها ریخت
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/65290" target="_blank">📅 14:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65289">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/news_hut/65289" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🔵
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/65289" target="_blank">📅 14:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65288">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-text">🔺
بانس‌های فوق خفن مل‌بت
🔺
🫴
100 درصد پاداش اولین واریز
😀
100 درصد بانس یکشنبه ها
🎁
100 درصد بانس چهارشنبه ها
🔹
هر روز 1 چرخش گردونه 1 یورویی
😀
3 درصد باز پرداخت نقدی
😀
بانس شرط رایگان 30 دلاری
🎩
10 درصد باز پرداخت نقدی کازینو
🎆
بانس هدیه روز تولد
💵
و چندین بانس دیگر از جمله بانس خوش‌آمد گویی، بانس شرطبندی طولانی مدت، بانس 1750 یورویی کازینو و...
💰
هنگام ثبت‌نام با وارد کردن کد هدیه Sport100 بانس 100 دلاری رایگان دریافت کنید!
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/65288" target="_blank">📅 14:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65287">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f7496394.mp4?token=iYqUgHKr2IfeX4B5PTHOrZUiZAE930c_t-IluMrx6_yjVv6q9M3029qS30WXi8BFuVNyW07dep-vBCKCaycq6e-0O0PCtmZ5hEXoMWcsN1GunfjgZhuiGTZ6npNUTotZM9yVycdeVKxgud6eINoRu8Li9eZMlm0hrsoI_83lTPCFSbh3ppkO8aO62WkcD5NtWVFUntQGf3rK8b0k-e-SkkBt6DajA4zj3kBlnbYO4FYYc1nS03UqDvpYeVEnwqbdYHvVV8_W8UqFuFjT2Yzx03X0sEILwV3mxjlksPBbNdIFs2ho75m8mHYciy74UzMELSaQAB3qr3i678viSM8w8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f7496394.mp4?token=iYqUgHKr2IfeX4B5PTHOrZUiZAE930c_t-IluMrx6_yjVv6q9M3029qS30WXi8BFuVNyW07dep-vBCKCaycq6e-0O0PCtmZ5hEXoMWcsN1GunfjgZhuiGTZ6npNUTotZM9yVycdeVKxgud6eINoRu8Li9eZMlm0hrsoI_83lTPCFSbh3ppkO8aO62WkcD5NtWVFUntQGf3rK8b0k-e-SkkBt6DajA4zj3kBlnbYO4FYYc1nS03UqDvpYeVEnwqbdYHvVV8_W8UqFuFjT2Yzx03X0sEILwV3mxjlksPBbNdIFs2ho75m8mHYciy74UzMELSaQAB3qr3i678viSM8w8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئویی آخرالزمانی از بمباران پایگاه چهارم شکاری دزفول در یک فروردین که به تازگی وایرال شده!!
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65287" target="_blank">📅 11:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65286">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gngehLb536bd5d7zN4l0GqiWdfwLwLV_DvB5zfnH3S3gbLR6gyEg0jg_GYz-2Vv8BEGSQhRs-TXzUI9RWUpYdiYkctPpCWBODGab0jPQPw6P5zGotcrB2cGdrF2vEPavdP0_qCLtwBW0Lo3zlhseq3BIGgDl6yBtGxN74gSh1thAGPHOKxygE62wfbTF8Tny4Um1QrWUDCn8VbvhBcOVIu5QskHkPw_27RRV4BsTZigb6O8EbCwT0gYNVyIxPL8pedVn_fd4BkI02IsOsWQpk4mRvLRL_wGyyMq_mKH1lysVPyefTOYtPeiE4fXnbLCEciVONk00LUB-GFTEjCp0DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژنرال دن کین، رئیس ستاد ارتش امریکا برای اولین بار به کاراکاس پایتخت ونزوئلا سفر کرد و نشون میده روابط دو کشور بعد از افتتاح سفارت داره بهتر و بهتر میشه
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65286" target="_blank">📅 10:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65285">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‼️
کویت تصویر لحظه اولیه حمله با پهپاد شاهد از طرف جمهوری اسلامی به فرودگاه این کشور رو منتشر کرد؛
وزارت بهداشت کویت هم اعلام کرد طی این حمله یه تبعه هندی کشته و ۶۳ نفر هم زخمی شدن
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65285" target="_blank">📅 09:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65284">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31e323d6f5.mp4?token=ERH5cqv82efEExSUNs1_5cc5OmUKWqf-8yK7f4lJRTJ2MSLlAXxnR_A3r5u-xS7wqzJbY2AbKQiHncw6bAHAGNFGu2EKUqD1czGKGTY21kAeHvzX4fJxbEWFEpjqOtxJUR7EPaOd9sv-aghIZEkj48Vb_iXbfOi4NPWCLxJ5-ekUSWaqECHKb5MOQZru_cPQq4s5iWJLBHayPzPx7XtsjWPp-BMDmrF9L24ODCbdQJKwu1s09Lm96zz7SdENUXOgbC2f9VVJVTvTcidhmQ4X2212bGVSk5OEM7_RtK7jhjgekBJAnVfUbR5gNdqqrPBwcDI_BP34dxqRvHXYVxXdLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31e323d6f5.mp4?token=ERH5cqv82efEExSUNs1_5cc5OmUKWqf-8yK7f4lJRTJ2MSLlAXxnR_A3r5u-xS7wqzJbY2AbKQiHncw6bAHAGNFGu2EKUqD1czGKGTY21kAeHvzX4fJxbEWFEpjqOtxJUR7EPaOd9sv-aghIZEkj48Vb_iXbfOi4NPWCLxJ5-ekUSWaqECHKb5MOQZru_cPQq4s5iWJLBHayPzPx7XtsjWPp-BMDmrF9L24ODCbdQJKwu1s09Lm96zz7SdENUXOgbC2f9VVJVTvTcidhmQ4X2212bGVSk5OEM7_RtK7jhjgekBJAnVfUbR5gNdqqrPBwcDI_BP34dxqRvHXYVxXdLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
مجلس نمایندگان ایالات متحده قطعنامه‌ اختیارات جنگی رئیس جمهور ترامپ رو با رای ۲۱۵ به ۲۰۸ تصویب کرد.
برای اولین بار مجلس نمایندگان تونست رای بیشتر رو بیاره حالا این قطعنامه نیاز به تصویب مجلس سنا رو داره و بعدش میره روی میز ترامپ برای وتو!
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/65284" target="_blank">📅 08:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65281">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVertigo</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClRl9YKZxPaKPjzH9uaQaf9tXrKgHLU7tIyHEYoPN2RG4eK4O80k7vwU5SanL1b7UadEjA60pg08AugXrv8ubVSoxHqvMGcj0fEJSmTYS_PllPWKNAg1TuhXd0340MenZHyMxsJv0s_kJJntM_sKJ2jwPeXEvZBNV2n6-MGsK2CSQsoZCMvQJRHHysJhyQytMXUmpjmNt27onIHSjfTqupGIoCfgtjLfUXNC28fzNDA22qsNrxxDqXV7_ljKaaSn4NolxhFp2xrMue8x_Sg5YmiW0RvBlXMHllQKRYyYIyVsqUmv7W0rbA-_GTM9cwm42T8i2zn7VjDn_3qMm_cM0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
Vertigo Vpn
⚡️
🔥
آفر ویژه محدود
🔥
♾️
نامحدود تک‌کاربره 739 هزار تومان
♾️
نامحدود دوکاربره  879 هزار تومان
💎
سایر پلن‌ها
🔹
10 گیگ
⬅️
120 تومان
🔹
30 گیگ
⬅️
299 تومان
🎁
طرح معرفی دوستان
هر 2 نفر که معرفی کنی، 10 گیگ هدیه می‌گیری!
✅
سرعت بالا
✅
اتصال پایدار
✅
مناسب گیم و استریم
✅
پشتیبانی سریع
📩
برای خرید و اکانت تست پیام بده
@VertigoSupport
➖
➖
➖
➖
➖
➖
🫆
@Vertigo_Vpn</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65281" target="_blank">📅 00:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65278">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/426918b893.mp4?token=TlHvMsnnZhAUiZO3Gzx2wTBs7L9XfVqE5M0Ew7iM9nkxDjbr7eFgsXNHxs7LDxtqSgrfrFdNs3Hawfq7nibsm2Lgy_mfaU0C8ELBcBfITYS3Yat0SZ6mgpypC1dzDXYIkPQbLR8NRwPjyAXljPhn__qPbLl29-vVOY8A1k25W_vgvwl-Ejnlq16WBuWt4UMBb5259rQLxCRWHAAwnCJB1ndmocFLdKxq3TYklPmr0Wpy-KCxR7Nj_hI0P9Nccj54nk4QTECO_zmI4h6FXQ9ZYTm7iiPCxbC7Y1Wo8bv_AgQJSCKN_RVxKbvsvnkNuk_X6D6-_hc4JLYfpFCDYlgEDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/426918b893.mp4?token=TlHvMsnnZhAUiZO3Gzx2wTBs7L9XfVqE5M0Ew7iM9nkxDjbr7eFgsXNHxs7LDxtqSgrfrFdNs3Hawfq7nibsm2Lgy_mfaU0C8ELBcBfITYS3Yat0SZ6mgpypC1dzDXYIkPQbLR8NRwPjyAXljPhn__qPbLl29-vVOY8A1k25W_vgvwl-Ejnlq16WBuWt4UMBb5259rQLxCRWHAAwnCJB1ndmocFLdKxq3TYklPmr0Wpy-KCxR7Nj_hI0P9Nccj54nk4QTECO_zmI4h6FXQ9ZYTm7iiPCxbC7Y1Wo8bv_AgQJSCKN_RVxKbvsvnkNuk_X6D6-_hc4JLYfpFCDYlgEDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی درمورد نقض آتش‌بس: تو اون منطقه از دنیا، آتش‌بس یعنی وقتی دارن با یه شدت کمتر و کنترل‌شده‌تر همدیگه رو می‌زنن
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65278" target="_blank">📅 00:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65277">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7323f0dce0.mp4?token=ucRRbf5qdbduARXhcHOqikgOTyqo2B8fnPb-al1rzJJArX1rdLN1IWPV4G4-mol10yeWVB1lgspPKpTEZhnvMUUqzkpzmoS_wpHynE7sfX65OMwAfATapMX10anQgat5ebob6moEcPmFBfWdWI8IvRPCWqSv6REOPoiJ7b8Q00dZEro9aQbSggRFlZvjxKJgJmXz-akfs1KezSzxPRzpOF4LdEbUGCDCx8vZ5dubguGMhyaUM9AX7F7ld7_6XOoJYap-k9a2D9klrkZ2mjrpBGs_me5QHH9bvimPYZEdu5b0AqAaL3SB1Z-fdXQ9-159Gqxa5l_waD3Lk42tQsg41Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7323f0dce0.mp4?token=ucRRbf5qdbduARXhcHOqikgOTyqo2B8fnPb-al1rzJJArX1rdLN1IWPV4G4-mol10yeWVB1lgspPKpTEZhnvMUUqzkpzmoS_wpHynE7sfX65OMwAfATapMX10anQgat5ebob6moEcPmFBfWdWI8IvRPCWqSv6REOPoiJ7b8Q00dZEro9aQbSggRFlZvjxKJgJmXz-akfs1KezSzxPRzpOF4LdEbUGCDCx8vZ5dubguGMhyaUM9AX7F7ld7_6XOoJYap-k9a2D9klrkZ2mjrpBGs_me5QHH9bvimPYZEdu5b0AqAaL3SB1Z-fdXQ9-159Gqxa5l_waD3Lk42tQsg41Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی: مذاکره بسیار خوب پیش می‌رود... ممکن است اتفاق نیفتد، اما اگر بیفتد، احتمال می‌دهم در طول آخر هفته رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65277" target="_blank">📅 00:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65276">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wpcqpo8emKaoMh6Wp9jQVel63xB-g_uwVK2dEzb5AvLqesg2O-ME8-_2oyG6EEzBItqZdmeMASOe0PfWVfmEgPMNflAzTb3iZ9TmHSQiiN_RhxsTuptmZP_elx4BkprKhpb0Xfdnbxuacig9jby6euq83DqwG_fivtQMaovYCRDBwmYmB6BK44fgpmRDhWBKe1LPas_S1zAGkBcXw2TJakCC0A1J87WjyyJaU32f51gDWUxZtqREHcoo7pSUIdT6CXzRp3obPX-Gj6Yx9tbg-QqkGeHpslDDt9OVGAPDtw7YQBjkaPTJBr8EYjjESfUgoDCciRM8dUgGWDxqLKnhJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام:
❌
ادعا: ایران امروز ادعا کرد که به ترمینال مسافران فرودگاه بین‌المللی کویت حمله نکرده و خسارات وارد شده در واقع توسط یک موشک رهگیر آمریکایی ایجاد شده است. کاملاً غلط.
✔️
حقیقت: ایران با پهپادها به فرودگاه غیرنظامی حمله کرد؛ این یک حمله عمدی، محاسبه‌شده و بی‌توجیه بود
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65276" target="_blank">📅 23:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65274">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bac082417.mp4?token=HcAm6LqmBV5s7wPuOOOAVPy-ntMgP01RgHjeoOR9jdDvVm-nW4zyKSrBWKMuKdnhUtxHLh_M4_q_fn4SaBZGUxYh5Pk8FULWhlUpgGxxOQ6srebypM6HvoZwMLhk9Q64c8yIl3LiPtDVarU_rFQ56hsX2juMIulNwKXSrjke54o6fuGXiVxjsI6LToO_0DpCPLGeJpWPqd8-DOBIPV2uE9rlhdTHqn0yrYTBQVCalTv1IrFWJjk4GDl9Jibh1DVL2bb5_vJ2Y0XK7nPPRRfcJ8IWa3CQpccZKvCCt-j585NDlkHAaLVx02uB5R1S_oHbr_ddOW0hQuiO5QI94vbi8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bac082417.mp4?token=HcAm6LqmBV5s7wPuOOOAVPy-ntMgP01RgHjeoOR9jdDvVm-nW4zyKSrBWKMuKdnhUtxHLh_M4_q_fn4SaBZGUxYh5Pk8FULWhlUpgGxxOQ6srebypM6HvoZwMLhk9Q64c8yIl3LiPtDVarU_rFQ56hsX2juMIulNwKXSrjke54o6fuGXiVxjsI6LToO_0DpCPLGeJpWPqd8-DOBIPV2uE9rlhdTHqn0yrYTBQVCalTv1IrFWJjk4GDl9Jibh1DVL2bb5_vJ2Y0XK7nPPRRfcJ8IWa3CQpccZKvCCt-j585NDlkHAaLVx02uB5R1S_oHbr_ddOW0hQuiO5QI94vbi8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
دیده شدن ترامپ تو پارک زرقان شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65274" target="_blank">📅 23:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65273">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAGQNRyoniCJaEZJBpdogyhKtZNCTxaeexG58E8NOEUrUwMZI6q5sVOlqJ-yy19xdsj5ZjqOy1wddGdjdtIlLy_xC4pUId58lOalg6HFAZ3sKhiGdM8dRxdKAw7mPLVcHtQsurkW4MSDWg6oASg07M1UvDBgiX-PCh_yAn39Z7M4szIYeHM86bhwxQfx574JWh4BYDQBXUD2ZEesxsB6aaE4BP1VjAD_0kKrJ6ZCMv2fnHwzbayl9Am_iwXLk1dZPTqIFqEnM7DI5U1QkAg4dSqMknjrGdW1lK88RneYWiNuVtrwhNtaYYeknf4ZdIpNcAS8js8ou2TJ5iUCMT1fpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اسپانیا
🇪🇸
-
🇮🇶
عراق
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
پنجشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه ریازور
🎲
با بیش از ۳۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
اسپانیا در ۲۸ بازی اخیر خود در لیگ شکست نخورده است.
✅
عراق در ۷ بازی اخیر خود در لیگ مساوی نکرده است.
📈
میانگین گل در ۱۰ دیدار اخیر اسپانیا  ۳.۴ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر عراق  ۱.۸ گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از ۲.۵ - ضریب : ۱.۲۹
🧠
پس از باخت، به خودتان زمان بدهید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65273" target="_blank">📅 23:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65272">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vlscy4eleOPtwPFjC-EFo8UbjtlTFfDLam71g8TJof51nkFqtNsTSzO1cY3j-kABKrvpBdZxogdYjEBLhcLQZF6VcNMm2Dm8OMtQ4cyuwlUHSFJrpT47iYdFJ6CUdL_hQDPusT8Uh3bMojpkz34RI8jyG6ujA1E_ks53NFhp5Vd4oxjxNyHAdLsXHhfsGDEF_KlcOjGOYf9S2tKUiVfRi77a_MBRCIyWYYGRy0UCXpGDvjCrGYdzguHP9Rm9O9OmQdLJ9hA4OS8T0Rkj81UYxCtEfv2xutdOhTbj1bXmf4KEgquxrTxPqmzTd-5XFQOarl0G9N_C-PhuJDZEFpokag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا مامان روبیکا گم شده دست کسیه بره تحویل بده شر نشه
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65272" target="_blank">📅 22:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65271">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a2c124cf3.mp4?token=sqSZcgGSv-Kpy1w0tMZ6qRi2UD7KvwSzc2q_ZmQ04YxLHJVXAi6TxfmeidFlk6B6ELh4gxhVxHtsoYe3MEUZRVfrenp7TRmHFHsMKN9zIM7fVTrgdx9aeQV_Uv4AgJ_CePrgtolqQSJJn_bwRb65ILm0DWTD40pA57SXY--Q2yKjicvlB8CjYRW8Py_WhFFQfdS_dB5OWtNov1qCIvtwoNo--_IgkTDx54FhNyBNsPmeoUJ_VMSHLu2pDXa7VoAknKlntuaWuJ6vOM4fC7bvSN5vkL1HjPYFRSeNJoW5OUhMbl0sozlp4j2MGXaP_zl48BNS11YCKGadsstkl9c-DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a2c124cf3.mp4?token=sqSZcgGSv-Kpy1w0tMZ6qRi2UD7KvwSzc2q_ZmQ04YxLHJVXAi6TxfmeidFlk6B6ELh4gxhVxHtsoYe3MEUZRVfrenp7TRmHFHsMKN9zIM7fVTrgdx9aeQV_Uv4AgJ_CePrgtolqQSJJn_bwRb65ILm0DWTD40pA57SXY--Q2yKjicvlB8CjYRW8Py_WhFFQfdS_dB5OWtNov1qCIvtwoNo--_IgkTDx54FhNyBNsPmeoUJ_VMSHLu2pDXa7VoAknKlntuaWuJ6vOM4fC7bvSN5vkL1HjPYFRSeNJoW5OUhMbl0sozlp4j2MGXaP_zl48BNS11YCKGadsstkl9c-DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: شما درباره تغییر رژیم صحبت می‌کردید. چرا الان هیچ‌کس درباره آن صحبت نمی‌کند؟
🇮🇱
نتانیاهو: چرا این را می‌گویید؟
🎙
خبرنگار: به نظر می‌رسد ترامپ آماده است با این رژیم فعلی معامله کند.
🇮🇱
نتانیاهو: این به این معنا نیست که او می‌خواهد این رژیم فعلی باقی بماند!
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65271" target="_blank">📅 21:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65270">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🟢
سایت معتبر رومابت برای جام جهانی بونوس های متنوعی داره ، از دست ندید</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/65270" target="_blank">📅 21:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65269">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwRDIvPKiuc-roOrM0Obm5zQnNQ2o1c2LxA8ffqkUO8adaC_CKO3e-UwWD9wLgDnTCp9qGmG5rIsUVk5BcX1eAklWBWSgPDtS3-PVPOsKH0JgpCvUUpAE_gvoKkIqPKQWa3zwQWS5lrxA10zAA4znmtzUgi1RcY_kTQm__DAPoKW3WezWCw8sbug6GEzNzTj2Amadpii8YCzcMlwVxtRs3h3z3uxuXKEi27Olcg1ZCenSUCzFHQMnQGIVd68K1SBKcb4evuNndqKIYfsfgA6vUbaxpti9MBw4PhhyJXhk2jnMlqwf8SLCRnbtyJNpEKss8v26o2MVgi6lS39NRYicg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💳
در
#رومابت
میتوانید با کارت بانکی ایران ، انواع ووچر و همچین انواع ارزهای رایج حسابتون را شارژ و برداشت کنید
✅
🎁
10% بونوس برای شارژ با رمز ارز
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
پلن وفاداری همراه با کش بک بی نظیر
#RomaBet
📣
‌
#بدون_احراز_هویت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⛔
در صورت فیلتر بودن از طریق VPN غیر از سرور انگلیس ( سرور
🇺🇸
🇩🇪
🇨🇦
🇫🇮
🇹🇷
👇
👇
)
🇪🇺
https://trentivo6402.bar
✅
کانال تلگرامی
#رومابت
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65269" target="_blank">📅 21:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65268">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترامپ: هنوز افتخار اینکه آیت‌الله خامنه‌ای را ببینم نداشتم، اما دوست دارم با او ملاقات کنم  @News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65268" target="_blank">📅 18:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65267">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: با مجتبی رابطه خوبی دارم. دوست دارم با او ملاقات کنم!  @News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65267" target="_blank">📅 18:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65266">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">کاکولدزاده تر و بی‌غیرت تر از اعراب حاشیه خلیج فارس تاریخ به خودش نمی‌بینه، به مادر این اعراب تجاوز کنی شبش بیانیه می‌ده محکومش می‌کنه
#hjAly‌
@News_Huy</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65266" target="_blank">📅 18:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65265">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aa2babe8c.mp4?token=GJXE_axD3GL1WYmFdyWucamIIub8R3k-CNzeU_efDwVuGBC4523x2wO9sQX86GRDrfPzeKmgCwodfYMVPqlljezBoFA7SnOyYX9cfg1InAbG7TMlK6rrXCTkoD49St8CAxjJOaMLhcrykVR_Fkh7EMzcRHySK2P215z_mQQbREhJ50RS6_6pABtDO8B0CQbS1dwkauvLNg3Ue2YU86MDW5toYzqU0OXTNnWXQFkqsS4jeYnY7Yj20qO0iKxKbxtmTGrY1OTe7LhTuU2OkGSjvoje3ntCAHc-KwBCqYpOKyl57C5d2BzAvx5G2T7D5FBFubde5C_1vRjDo4XLEG_hWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aa2babe8c.mp4?token=GJXE_axD3GL1WYmFdyWucamIIub8R3k-CNzeU_efDwVuGBC4523x2wO9sQX86GRDrfPzeKmgCwodfYMVPqlljezBoFA7SnOyYX9cfg1InAbG7TMlK6rrXCTkoD49St8CAxjJOaMLhcrykVR_Fkh7EMzcRHySK2P215z_mQQbREhJ50RS6_6pABtDO8B0CQbS1dwkauvLNg3Ue2YU86MDW5toYzqU0OXTNnWXQFkqsS4jeYnY7Yj20qO0iKxKbxtmTGrY1OTe7LhTuU2OkGSjvoje3ntCAHc-KwBCqYpOKyl57C5d2BzAvx5G2T7D5FBFubde5C_1vRjDo4XLEG_hWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: با مجتبی رابطه خوبی دارم. دوست دارم با او ملاقات کنم
!
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65265" target="_blank">📅 14:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65264">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8fa16c5af.mp4?token=g2SAKhdr8OhAm6pzP2XnDBLxMsg0O8d8gQ9oOCO1I9bM_MaeIbeb4c7hqjcf5H5lwgIAObvsgV9eZWpLgti7FfmWsgQL3CLQn4qXUFkZbwp7wg5wxE0TNwVWlRCb8zWZbPOHEzszHctlH6V98x24mvrz35YcrEo9o-3z7GVVQraMQ3V4gXN4prB6PDX2fdWvkEFYqhK-5NDQReWgiMkSaIx2fuXvCohypd7jegsDQnm0cupzuyOpoTitQyLoGnKPMpePaaDQecWqvYZd_7fZrPL1cBiKazFz0oAMR476XQggtX20WhooiYgmLXPLC0x1wjjiy-5ZZzAoq7HuAACv4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8fa16c5af.mp4?token=g2SAKhdr8OhAm6pzP2XnDBLxMsg0O8d8gQ9oOCO1I9bM_MaeIbeb4c7hqjcf5H5lwgIAObvsgV9eZWpLgti7FfmWsgQL3CLQn4qXUFkZbwp7wg5wxE0TNwVWlRCb8zWZbPOHEzszHctlH6V98x24mvrz35YcrEo9o-3z7GVVQraMQ3V4gXN4prB6PDX2fdWvkEFYqhK-5NDQReWgiMkSaIx2fuXvCohypd7jegsDQnm0cupzuyOpoTitQyLoGnKPMpePaaDQecWqvYZd_7fZrPL1cBiKazFz0oAMR476XQggtX20WhooiYgmLXPLC0x1wjjiy-5ZZzAoq7HuAACv4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره اینکه آیا نتانیاهو او را برای جنگ با ایران فریب داده است:
منظورم این است که من کسی هستم که این را شروع کردم.
نمی‌خواهم کسی را خسته کنم، اما من این را شروع کردم زیرا نمی‌توانیم اجازه دهیم که آن‌ها سلاح اتمی داشته باشند.
اگر من نبودم، اسرائیل وجود نداشت
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65264" target="_blank">📅 14:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65263">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/416ff3bf1f.mp4?token=isD5mKwQzhfiW1_JfTCoui4JbaatpB6_2RGkr-5lgQfbH6CMtqO_pdiLRGKnARxGmGOTficF38LgOH3EXyb2XnY_UtBK3l1mGFnJqXPMo8A67YHnTjJMaB2zeG7tJCFWFd2db9h2wvnLUuRX5muPwTGe8-FbMYhGCdelvDHacGnws_WseMBoOuWPztHlM2M92SipVgbdbVbPVmu0rmvZ-qhSVNNIMhefXqHPNSCBvK9Od9gIcNt7Q1w_z7sSwH6kXX90_W4dQotZSZnL8IfeGGPQnKlyRgo0ziXxnYKYqmXkwLYDTuXZVgH0EiXnZpNyqhZAwkmuyTFB3OdziNFy5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/416ff3bf1f.mp4?token=isD5mKwQzhfiW1_JfTCoui4JbaatpB6_2RGkr-5lgQfbH6CMtqO_pdiLRGKnARxGmGOTficF38LgOH3EXyb2XnY_UtBK3l1mGFnJqXPMo8A67YHnTjJMaB2zeG7tJCFWFd2db9h2wvnLUuRX5muPwTGe8-FbMYhGCdelvDHacGnws_WseMBoOuWPztHlM2M92SipVgbdbVbPVmu0rmvZ-qhSVNNIMhefXqHPNSCBvK9Od9gIcNt7Q1w_z7sSwH6kXX90_W4dQotZSZnL8IfeGGPQnKlyRgo0ziXxnYKYqmXkwLYDTuXZVgH0EiXnZpNyqhZAwkmuyTFB3OdziNFy5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوش‌چشم، تحلیلگر صداوسیما: انتقام کشته شدگان رو بخاطر حفظ جان قالیباف نگرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65263" target="_blank">📅 14:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65262">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/news_hut/65262" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✈️
اپلیکیشن MelBet
🥇
🎁
کد هدیه 100 دلاری:
Sport100
🔒
برای تعیین رمز ورود حداقل از 8 کاراکتر و حروف بزرگ و کوچک انگلیسی و اعداد انگلیسی استفاده کنید، مانند Hamid120
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/65262" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65261">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-text">💛
هنوز توی MelBet با این همه آپشن خفن و ضرایب فوق العاده ثبتنام نکردی
⁉️
بعد میاید سوال میکنید کدوم سایت معتبره
❗️
👀
اگه میخواید توی شرطبندی موفق باشید و درآمد کسب کنید در اولین قدم باید سایتی با آپشن های بی نظیر و ضرایب استاندارد و امنیت مالی بالا داشته باشید
✔️
🎚️
همین حالا از طریق لینک زیر ثبتنام کنید و وارد دنیای جدیدی از شرطبندی بشید
🆕
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/65261" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65260">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
📰
#فوری؛ نیویورک پست: ترامپ پیش‌بینی میکنه که با رهبر معظم ایران، مجتبی خامنه‌ای که احتمالا همجنسگراست، دیدار خواهد کرد؛ «رابطه بسیار خوبی دارند»!!  رئیس‌جمهور ترامپ در مصاحبه‌ای با «پاد فورس وان» که چهارشنبه منتشر شد، گفت انتظار دارد با رهبر معظم ایران، مجتبی…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65260" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65259">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQVQJJQlXDmGt3VzTG4dS_KjVSHoh9ja07TLB8BfRHV02WyRYwVrliIBiuTxtjGFWsmplCs8JHJ8cJDbJsNBMlH6iyKXaDnbnDvSRvrvDG5tvzaAWj38tQQ3QLcyEPlnXurMPw8bVO6q1p3FMTAqhvd8GvM-DEaYWKmS-_Mo2DttGVPLBOCvqoR11NTx9mnOzaIzNPkTdJbj7gjtD57WRTKD1sAHRZly-PAbeQv04sThP2f89a6OOxC9qbDGc1zuXsdGzamvHO05QrlAQSKzAoSKCnVK72ye1MQIGQr8CZYXdujRb9P8ttDtxml4NEDkpxADCBgc3XFtYvej5-VYdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست قیمت جدید و نجومی خودروهای آشغال داخلی:
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65259" target="_blank">📅 12:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65258">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gHW3zZc-cNvEHUiGRcFezFQxjaNRJPZWJwEUVaZG5_zbPC3XTt3iCQBJhNopnmPlS7NRCcCllElWct70mJyL7oxw84OV4iqyFNjrJqhsNhu71YBIYEu2UTfv6MlqRkU73g0NnqWnTVIha7_GzGPykyqaXMeTzLDRwOr4HK2dQaybW0ktSHqaI7itBzdP2CxYxdkTBQyJhliURu1FjHZlx3q5B7H8YpDZKGJzC_cqT5R3DgM8sia5HTiF40GH_f0qx9z9wZXPxBLEqlVLr2vdn_gcI9x0gsGQZe_6WAkZQxRSZ5UTmQmi4uQoXf5uitVtZqh65ElsnjY3YMxCFoR6XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکنا: آخوندای قم پیشنهاد دادن علی‌خامنه‌ای در قم دفن بشه
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65258" target="_blank">📅 12:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65256">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EtA2JgkJPKl1Ky6XCkmvuzGb8lNjs9U3xVoynpzPyF_irHbg3bYTfu0A8P5LAGk_2svrfpWfjVZXdsNUBGqkELR1m3bg1EtDjgVxC02wx1AxQA4IbH9ZJ9E6AHWCaTWtsQGrknSOGfQhCwE-X9BhHyu2je2kY3ryHhA4QIDfTM1yQt64QIYlBxO_sB2dOh4qpU22z0yb9wltWxvAnUpchhYpvmgxbb0JZnUPn77Zo7nxq3_sT0KTnZ50pSjSOTzVe9FMwpy5GTKq97CkoH0znh0npWKF2tCJ3HIO7l6aFZ2BAd1Uit5DeNzlUn6CMtfRYHiMe7KyC2Gq0aQGuOn42A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hGlANGzzsDUrQgGSCESn-KpBVWgQecYpry8mooLJ75PtxShNYa6bRaRAS-b-dcmJ-mrSSN6rcIzj92pVBiucX8lrVenHR7yjjWruPhW_cKX3ka75RlgiepyJlckajJLqOcki_w4_qbAY2E8qfWtuQEGa6cBBcQW3x7D50vLdY8Af4ztt0dIJYQD6LXSRD9Rms3ei0FYmEj4Rgy3k6TsnxW4AHS-Sc_nD6rNgzk4CnybSdpwpkYPvPOqcrO9T4pIb_kDee5HFfw3A_OHyajFB4RAU-FwdkVCD3WLJ6VMdU7agwdwVMQGPcUx_kHF_0SMT_VcsjrcfpovT27duBP8VoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
وضعیت فرودگاه کویت که گفته میشه مربوط به حملات دیشب سپاهه
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65256" target="_blank">📅 11:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65255">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWhLOIljwILrJOXSvomP_KYSBfE1wrOCfRcOEu9WXVXKDLSdSTmYuVhw1iV4tm0SodOGtNZWIeuX20Eeh0QWNVxus9XZLmlZhR11JMJKsFpo5lIujlQfQaEaX4FptXXN1FwfGTl4_IeqnKQf81T8_9RMHq1DEqJgde-gHhXs66AiyfeXgoVVof4UWpp0nPUh289t0LHREjs0cJSqFoAi8_a21wTltfqQ_Cq0fLfi35p-C1LMcz34lRrl1-BdZrH4pl4aqShkcKEEfZbfGjSMGlGuUziFXr3-I7NWcbxQ-ZzmnBzICGo32AA7YhD3Q5g3qbnupZN4Y6q89wWm7nS4FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیت کوین در ۴۸ ساعت گذشته بدون هیچ خبر منفی مهمی؛  ۸۰۰۰ دلار (۱۰٪-) سقوط کرد
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65255" target="_blank">📅 11:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65254">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">طبق گزارش سنتکام، ایران چندین موشک بالستیک به سمت همسایگان منطقه‌ای شلیک کرد. همه آنها به اهداف مورد نظر خود اصابت نکردند.
دو موشک شلیک شده به کویت در مسیر خود به هدف نرسیدند یا متلاشی شدند.
سه موشک که به سمت بحرین شلیک شده بودند توسط پدافند هوایی ایالات متحده و بحرین رهگیری شدند. هیچ پرسنل آمریکایی آسیب ندی
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65254" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65253">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">هواپیمایی کشوری کویت اعلام کرد که حمله جمهوری اسلامی خسارت شدیدی به تعدادی از تاسیسات فرودگاه شهر کویت وارد کرده و همچنین شماری مجروح بر جای گذاشته است.
هواپیمایی کشوری کویت اعلام کرد که ساختمان تی۱ فرودگاه شهر کویت بامداد چهارشنبه با پهپادها و موشک‌های ایرانی هدف قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65253" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65252">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bac9b656e.mp4?token=VGoxHatWl3zQ97o4kYaleaPodybheCKGFB7qSLSvt9DNHdU-b3ORIaTJrt92uYvepeaHhoaGMLqgKs4cAivcd593LhZhbKzbks5SHPAhxJVLPK8UwjFsPUW3raVb8GIKPWHMQvMX_4uP0OAZmsVizdAgZKnDK4y5sx438QOd_OLmC-kv-A9XXaioaM-5jZX1E-OfJhY2A_sFbt7lOUCYBsSn_ExxcCvDYMKyJzQ2jGym3eVvKNVzbF04f2Qw-etZ8BTE72QPs02unlyZBjGCeooND62tORe3A_0bFv48X-lVaRHz9K_uY4zEaQReSkeVdG57rDlXGNo0ffg1m2FQ6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bac9b656e.mp4?token=VGoxHatWl3zQ97o4kYaleaPodybheCKGFB7qSLSvt9DNHdU-b3ORIaTJrt92uYvepeaHhoaGMLqgKs4cAivcd593LhZhbKzbks5SHPAhxJVLPK8UwjFsPUW3raVb8GIKPWHMQvMX_4uP0OAZmsVizdAgZKnDK4y5sx438QOd_OLmC-kv-A9XXaioaM-5jZX1E-OfJhY2A_sFbt7lOUCYBsSn_ExxcCvDYMKyJzQ2jGym3eVvKNVzbF04f2Qw-etZ8BTE72QPs02unlyZBjGCeooND62tORe3A_0bFv48X-lVaRHz9K_uY4zEaQReSkeVdG57rDlXGNo0ffg1m2FQ6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلمی از پهپاد شاهد-۱۳۶ که دیشب به سمت آسمان کویت درحال حرکت بود
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65252" target="_blank">📅 10:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65251">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
حریم هوایی بحرین،کویت،امارات به طور کامل به روی کلیه ترددهای هوایی بسته شده است
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/65251" target="_blank">📅 02:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65250">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
حمله سپاه پاسداران به کویت  @News_Hut</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/65250" target="_blank">📅 02:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65249">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
حمله سپاه پاسداران به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/65249" target="_blank">📅 02:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65248">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">✔️
اعتبارشو صد درصد تضمین میکنیم
ارزون‌تر، مطمئن‌تر و قوی‌تر از همه جا
🔥
ضمانت بازگشت وجه در صورت عدم رضایت
.
دیگه چی‌ میخوایید؟
😍</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/65248" target="_blank">📅 02:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65246">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
آمریکا بزرگترین صرافیای ایران یعنی نوبیتکس،بیت‌پین، رمزینکس و والکس رو تحریم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/65246" target="_blank">📅 00:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65242">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tLVUeIxXTE2_1Q21X_jmA868fcC7f8Yw5YH2f4_yEwT5u2LedHWL7H9yAKgT3gHlC78WAdv1XCLrNaTzQc8eUiH5jYphpt_ukX5f7uHoRUALrHAad2YtrGMdGXqXw-fgF-XCeMiEeGWuKPrIgJsDVdHH1rhhW7UXmJhIVMzj8xXrmbyk847xOC86agGF-ayLi1_rXjXe6GmBbZHLrYDks8TVIh8yPYQ2QiHnO-H43v5qekrZLPxNXdYQqrvMso6K8V9BeDTm1PJIVG6iimXYPZLcqojuqDJOe-2VZyvZeSfxKtIlul-B_ezVMWIjth9RmV14k9eszcK2AyHE62Iq7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E4OeH6yxK-EMH7Mi03aIrtwC_vy0qmnKe0BPtxgiuwJYYFMY8_V0CbINrR1CL83A3CsDi_cHkGjNAt5KkMx5LrD27-prs8XogXI58_phZiczDurDPwK4TiZuYnhkdm8fMUZ1or-92sRAx74dHyjrPHLGTql_8UxTNbbqx8yAO_P6oxaA6nFfTtBA2AuBz1FzzdRAthI9ElJLP-aB8tmiGrXRi29F15mqZIXMlkeNhjKmsDJ0oqrzhuuMSh8xxd4eO4BPGNm0JH3oNkTjddNaiuzHR1yEwWodWlg4lW19tg5qLa5SMw8tK7H2GKGQ0y4RKpQ3WLVmf-eEVUCXj86Uwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه شرکت به‌نام دکترتور اومده تور آب‌بازی تو چیتگر تهران گذاشته که مردم از جمله دخترا و پسرا میان بهم آب میپاشن و هم‌دیگه رو خیس می‌کنن
ولی خب بعد چند ساعت از بالا دستور دادن همچیزو کنسل کنن
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/65242" target="_blank">📅 23:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65241">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmN1rEAPlKVwU-RJIQH79V0X_As9tRfx5fLb5unfF2eJLSSY9OLkWQTBjpeLxViy7G6cWynbzQl3nEZmMJwipWmiyv3u9Rxbc779SCkMQFlwW7Ml5ZGf3hq2xYB1t9QeTpseTfd8MlWOkETsIhu_92KQzBb0NX1dZVPhb0rneCh4j-glT5HL0mQmgsBYaZP5qfUGmb62t5jbHA2p6eQih9-YSaYAsuedBfbj9DIZmMhJHjCVh6w4AUHhzPBHCBQ8jwqRr0I9I2BVDDFe8PDL47thoySEMMjvI-7z-2QiRQGalqtMineA6dMnhbxJj9m_4Wfb1A6_ZSu2jmtVrH5T_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام: ابراهیم لینکلن و نیروها همچنان به محاصره دریایی ایران ادامه میده و تاکنون ۱۲۲ کشتی رو از مسیرشون تغییر دادن
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65241" target="_blank">📅 22:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65240">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JSztd-CrwqDBz3OSkBdI6AQLuK30O70axXAEZLsHLjm2MT61pCemtWyRFa72slrnwg943cwEpNBBht7AQzcJUpB5bp7kSJ_99qi0vkIBDjdThzbRqpZ8sUiunXPmH7S1SrvDrtOGmjqF9j014n8M4R6me76WjrgUN4W-VWXKFfXsCWzVi0C-dWZsTn7PKZ__jay_QJboA750VZ4gTNj4FQt7UCOHXLBdK0o9yNkD1dhmqkuyTZqheg7g7wk6D8e1cqknLxbUZQYjU3nkDjlu6RFslNu4-AjB6NxiS67TQoGvEaMYa4BXRxF-chN4Iaa5v2TNroXFfVeOKWdfxbwAcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق آمار، سالانه 60 هزار ایرانی بر اثر مصرف دخانیات فوت میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65240" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65239">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/news_hut/65239" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
#اپلیکیشن
اندروید سایت جهانی دربی بت
👍
اسپانسر لیگ انگلیس
👍
🔥
امکان شارژ امن از طریق کارت بانکی
➖
➖
➖
➖
➖
➖
➖
➖
➖
🪙
همین حالا عضو شوید
👇
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/65239" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65238">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcc4M1JJMaBzTPQWbVzGAJXq0xF_AwbO6Ej-lnwaC1_oW7pngFgRAe4qg5UksiDXo5CeJtShwKysN9_wvJvtTs_v8pCAAdnAHG4ZCUMKnUAWjzyFrsmWWkgFpK8kkj9qodjtSMAud1jRM-vhcEianYr3VfOdtkFe7WXKykMw9DISLMYkFgE1aF6u6UpLY44Dl0mXi4fDDF4vTIMB4DGjpGxyO_FshhjWUuGziI18_Rs6aYkj9WawUtu9UGk0QreZIC6vK--AA594QHnW4vsCyfjTkopyN1PPE_bnrltGElIFEAhIej8g4lrkYJHBvB81jAmP5OipU5EMzckhHaPfoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
🚨
کد هدیه ثبت نام:
GG007
⚠
️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت g12 :
🪙
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65238" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65237">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
امتحانات نهایی که قرار بود ۲۱ تیر شروع بشه جلو افتاد و رسما از ۱۳ تیر برگزار میشن
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65237" target="_blank">📅 15:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65236">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6YXKTKi3jwsAwrxhGvIZuGhDQW_h3EYYJZxSxZ_0-YE0RS15OuWewDAsNFLZCW63H1nQ3DuJRfXxN5gyNv_fGwHb5qLaq5dBp1SxNzOYLA4JpDR10D7-D2wTzvhlyLkQWJzuS_dmUze3s5Dxw4k0vx7EzwEwsxOFLbg93-0pROZ66grlj4mS9eF7XC5gxYXKMQOOVgAIUC_c12pIGO8QRKzjxWQRmhpaQiHgAfJEW4HngJrkOliZC58ZcRyY5G9R2ukQyG3fd-P_w7q1YI4-On9SGfpisbU6ng19Hbi7L81sRZJW_zfvtVJMvm9-knEyWYBiECVdRCWSSiTJNJBBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
داعش با انتشار پوستری، جام جهانی را به بمب‌گذاری و پاپ را به ترور تهدید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/65236" target="_blank">📅 14:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65235">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a43d73ec7.mp4?token=eSWGGLLINE5Y1h5ns_Yr1xNmW8TGh4mp_palk7dsml6-VO062nBPVT8bep23Rxzn2VQYoGXa857ZQOMpnY34A-GeVK2RgOPqINgM6ICh6EoBl0-xjo4-t5uMAgWAHntsOAkC-g-V2GD8ZQE0bHiC-UadXKY_EIQA2Bil7AVKtVWeOmdbodZ7EYFNnVERg6F2Z_y9pxC3U8QlnOqNwW2DPHfTK8qztL2YjOTGLO8qWSGuSLbn8sRFuntKH-A-GfzjUN2qikpWRk97f6UXKyOscAG6Cx0vbjVBQ4Totmm_tlE6-e_LWTN9esDFogNsuxV4IJ5vqNTKscvOwWmB18G-Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a43d73ec7.mp4?token=eSWGGLLINE5Y1h5ns_Yr1xNmW8TGh4mp_palk7dsml6-VO062nBPVT8bep23Rxzn2VQYoGXa857ZQOMpnY34A-GeVK2RgOPqINgM6ICh6EoBl0-xjo4-t5uMAgWAHntsOAkC-g-V2GD8ZQE0bHiC-UadXKY_EIQA2Bil7AVKtVWeOmdbodZ7EYFNnVERg6F2Z_y9pxC3U8QlnOqNwW2DPHfTK8qztL2YjOTGLO8qWSGuSLbn8sRFuntKH-A-GfzjUN2qikpWRk97f6UXKyOscAG6Cx0vbjVBQ4Totmm_tlE6-e_LWTN9esDFogNsuxV4IJ5vqNTKscvOwWmB18G-Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
علی‌رغم درخواست ترامپ برای آتش‌بس در لبنان، ارتش اسرائیل دقایقی پیش مناطقی از این کشور را که در تصاحب حزب‌الله است، بمباران کرد
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65235" target="_blank">📅 13:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65234">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f14e605921.mp4?token=JLRza6wqiMBrl_bbabSYaD9s9P8D5CaMuFLYx8a9PZrLhISqkDMgHw7I78oufhUNH0T0r9X7Vlpp30Iosq5cSnU2CJ2YhxYeZJi67lKpaW2_dHlaPHgTxVzBIS8HIr5uTbdBoUWQcFDYZv_GjC_qKE_jgiWK6KzExRA8MAqVHDktu0mCqPeCIGFXz-dHPDIDNtIbyx483CCYjVdFpp5x2slzNeK_1y7zWeD3WufYTp8XS1XG0hZTr7XhEg9nuyfZYgc3KrzP--c-UMFfQ54h0YzdZHF3nZBlimabPZp3yedPVnpH91jXJecIhek2hZ7OkrHzg4-fX067C3yVXtcQcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f14e605921.mp4?token=JLRza6wqiMBrl_bbabSYaD9s9P8D5CaMuFLYx8a9PZrLhISqkDMgHw7I78oufhUNH0T0r9X7Vlpp30Iosq5cSnU2CJ2YhxYeZJi67lKpaW2_dHlaPHgTxVzBIS8HIr5uTbdBoUWQcFDYZv_GjC_qKE_jgiWK6KzExRA8MAqVHDktu0mCqPeCIGFXz-dHPDIDNtIbyx483CCYjVdFpp5x2slzNeK_1y7zWeD3WufYTp8XS1XG0hZTr7XhEg9nuyfZYgc3KrzP--c-UMFfQ54h0YzdZHF3nZBlimabPZp3yedPVnpH91jXJecIhek2hZ7OkrHzg4-fX067C3yVXtcQcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🔝
دیوید بارنیا رئیس موساد:
تغییر رژیم در ایران یک هدف ممکن و قابل دستیابی است. این یک وظیفه قابل انجام است اما نیازمند تعهد، صبر و فداکاری برای هدف خواهد بود. این وظیفه باید در رأس اولویت‌های ما باقی بماند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65234" target="_blank">📅 12:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65233">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b11e2b7f3c.mp4?token=lanZO7gDVLr55m7KMjJ4yBgiYyuJRjKeb50UyZyXeuajNepZpczzQlCyj_Hbgc3yGqZOQPbNDe-1C02jdAiMiHf3RHLo5sPWgoBL7rV1z4D3jZ8riQE53avMzf3McTyfBVwiYCsAmAOBvMq6F6EyqBbhH-N9grkjiovJT1DGjdP9Xc57XfO7JhYsPcffmU8RFLRueVGiiMNCgzR4lVWI9xtGk6siMT_qHDwCAa96AhhoxC2KhXXIPvq2TEWfMXtsqjoVxHPRjmwfXdyr887e-mZo2kvfmhUrQUP0uvMXdzI269diE-8EqNNv2SnXU9UQkASnsJp6rn4DQXS3sI82Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b11e2b7f3c.mp4?token=lanZO7gDVLr55m7KMjJ4yBgiYyuJRjKeb50UyZyXeuajNepZpczzQlCyj_Hbgc3yGqZOQPbNDe-1C02jdAiMiHf3RHLo5sPWgoBL7rV1z4D3jZ8riQE53avMzf3McTyfBVwiYCsAmAOBvMq6F6EyqBbhH-N9grkjiovJT1DGjdP9Xc57XfO7JhYsPcffmU8RFLRueVGiiMNCgzR4lVWI9xtGk6siMT_qHDwCAa96AhhoxC2KhXXIPvq2TEWfMXtsqjoVxHPRjmwfXdyr887e-mZo2kvfmhUrQUP0uvMXdzI269diE-8EqNNv2SnXU9UQkASnsJp6rn4DQXS3sI82Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امروز دانش‌آموزای تهرانی در مخالفت با تاثیر قطعی معدل، جلوی وزارت آموزش و پرورش تجمع کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/65233" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65232">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65232" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/65232" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65231">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTJBKkZL8Naeqc7X8ipKNqZIWptnj71cS0ez-EuBAc-6LfuYomMn9lDaiwXJ9ZTtGoJAtAhArfSt08NSzEJ1F1npVTGrhQjHl4PWeGSITKUoBfU4csu3IYmyr_BwZyryZB2_CrS_fWdZVt9hSqnwixfpcG_u1x4QNrjb3LY7sbb78592qQa47jMk0kc5gxZL2ECQ2arUVVlYrBPh5Nn-TcQUfJ9_Lega4JpPlOP6rQ-dA8ZIiiacTzTS3ZplljaKegd2VaFZQ7Ow_aNp30KaMZfptXdqAjT3_qauaXGTyZov0QMr4qV4ozZuy-SLEeBEk8I9s8uQCCgh_gzRfVN8-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
روی بهترین مسابقات ورزش های الکترونیک پیش بینی کنید و برنده شوید!
🎮
تنوع گسترده از بازی های انلاین  CSGO, DOTA , FIFA وMORTAL COMBAT ...
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65231" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65229">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e2d6ed8f2.mp4?token=h7HacR25g96vtGGrPOzYRCr_9D9qFXGuDaLVUmJB4Dmmc_p4JpUyANGNuuSXjR-K3r8hsrWNSfhrhSzmR1Tj-opmnxqNTXUWygWAxEvzpLUgHOg2nO8t2arzMXsySOO3rylYbvwTR_PCXzQJOvQO5kia9T1KywDjZi_CcqNpx8JMe5Om-ZxT1isxXqUuHsJDK1OhaHJwod2rbdF9GoeNpTWaurS1IDeulIHG0q3Ij_Rk_K_JdZIu-U6gpBBWrJv078FTo9QIxR2PX_yuWLwty4126wa8odBku-3ptVvvzVlzVusCBtzMTX-iPBNFyeEPLG2IPXbMG1i4bc07XYw8aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e2d6ed8f2.mp4?token=h7HacR25g96vtGGrPOzYRCr_9D9qFXGuDaLVUmJB4Dmmc_p4JpUyANGNuuSXjR-K3r8hsrWNSfhrhSzmR1Tj-opmnxqNTXUWygWAxEvzpLUgHOg2nO8t2arzMXsySOO3rylYbvwTR_PCXzQJOvQO5kia9T1KywDjZi_CcqNpx8JMe5Om-ZxT1isxXqUuHsJDK1OhaHJwod2rbdF9GoeNpTWaurS1IDeulIHG0q3Ij_Rk_K_JdZIu-U6gpBBWrJv078FTo9QIxR2PX_yuWLwty4126wa8odBku-3ptVvvzVlzVusCBtzMTX-iPBNFyeEPLG2IPXbMG1i4bc07XYw8aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
واکنش یک‌عدد ملا در تجمعات شبانه حکومتی مقابل یک ماشین با چند سرنشین زن:
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/65229" target="_blank">📅 10:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65228">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e2983c9bf.mp4?token=m4ljAL1y1JhPGFTt_E7aUzA7JhtVAoy1JY1UBQw-yGpxyLAvrCG9vYMX8bDrfzDt0vZA68M-XFGzhA4yn6zX35FQ-rB9Th6lsA6r9JRiqQq7Mv658F1fwPesNRpZRFiIv2uxL32AKYIxzsqJofFzYRWf0daKuf6Iyx4Osut1Gfo0z6JB-HVrqcnnwa4O7xSFy8g7CWrgjDtvIrFYxHxe2jRltw1XYPIdYsu63bIOM3NgeDOGCjTIn8tQ4DEuLHzBsaYLesUGJO3VEK_cpnZ6u79bYZNSYYk5ACYFoY5phQsErl19nXYK-e8Dy6ieKGh-QIfA0GR1Dkwx69ej1hhRJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e2983c9bf.mp4?token=m4ljAL1y1JhPGFTt_E7aUzA7JhtVAoy1JY1UBQw-yGpxyLAvrCG9vYMX8bDrfzDt0vZA68M-XFGzhA4yn6zX35FQ-rB9Th6lsA6r9JRiqQq7Mv658F1fwPesNRpZRFiIv2uxL32AKYIxzsqJofFzYRWf0daKuf6Iyx4Osut1Gfo0z6JB-HVrqcnnwa4O7xSFy8g7CWrgjDtvIrFYxHxe2jRltw1XYPIdYsu63bIOM3NgeDOGCjTIn8tQ4DEuLHzBsaYLesUGJO3VEK_cpnZ6u79bYZNSYYk5ACYFoY5phQsErl19nXYK-e8Dy6ieKGh-QIfA0GR1Dkwx69ej1hhRJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
نواب دبیرکل حزب باقر قالیباف: آماده بازگشت به جنگ هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65228" target="_blank">📅 10:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65227">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/159f752950.mp4?token=a0mIDdjL0-pT4Zn0ZVlSp2wKle53xjviKkIh0UdSJw7oUGANTpTBE9OaE7oOAtzkkL5etyjHTDScQCk2CsYWPLpN0kU4MDzLON3rJ6M8cCIneWCNU7qtHKQVw2Ak-t25-6TDN1R99BmpyAuelh4V7VRUKq_wtT2V5sSv0Yq77PPAE5wjXi8rijSn8x-HhLCuMXmvvInWS7ZkVwZN20O7CHJsKhFkDlb7gpsUSjW-po_adbw_ALy5gQzCGZJiDomlE3YlqRtUAQBOgj62TmGGe-rrE1ucLe1lp0BnI5bABZCTgpKj_4P9LiG3MlAPGdoEu_a18E9UwsY5sGvSFtX21Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/159f752950.mp4?token=a0mIDdjL0-pT4Zn0ZVlSp2wKle53xjviKkIh0UdSJw7oUGANTpTBE9OaE7oOAtzkkL5etyjHTDScQCk2CsYWPLpN0kU4MDzLON3rJ6M8cCIneWCNU7qtHKQVw2Ak-t25-6TDN1R99BmpyAuelh4V7VRUKq_wtT2V5sSv0Yq77PPAE5wjXi8rijSn8x-HhLCuMXmvvInWS7ZkVwZN20O7CHJsKhFkDlb7gpsUSjW-po_adbw_ALy5gQzCGZJiDomlE3YlqRtUAQBOgj62TmGGe-rrE1ucLe1lp0BnI5bABZCTgpKj_4P9LiG3MlAPGdoEu_a18E9UwsY5sGvSFtX21Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇱🇧
درگیری تن به تن نیروهای ارتش اسرائیل با حزب الله در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/65227" target="_blank">📅 01:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65226">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f218bec310.mp4?token=Z9RG5iWgwZ4SjmJngSdxytUaLP19r9rp27oU-qvrMsazHYbGSyM-9aXTgIToc35R_cjdbgRZb8fYYS9T1CI42WmnPqIRX-jgpe8ute8mOY39zY0JY-si46hTbJAHZ8vIfLRq2zttJilGF-EPJS3arMW8L3a5E0dKevGGK5HlydMuvZ2o5SejEVfXbTuRCFPDpuML7bUq1GaPqrkSkaF15MWLR3uEuLcWSLLjS0rjmEospBop_YBVndtxf95ohfBZ-n2IHASlED3Nk5v4_an6-89PW3NJupXkwThi6fD4ibwVA-RXotwmfmBZc-ID45TMkdP0cawQWpqFB4d26M4mlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f218bec310.mp4?token=Z9RG5iWgwZ4SjmJngSdxytUaLP19r9rp27oU-qvrMsazHYbGSyM-9aXTgIToc35R_cjdbgRZb8fYYS9T1CI42WmnPqIRX-jgpe8ute8mOY39zY0JY-si46hTbJAHZ8vIfLRq2zttJilGF-EPJS3arMW8L3a5E0dKevGGK5HlydMuvZ2o5SejEVfXbTuRCFPDpuML7bUq1GaPqrkSkaF15MWLR3uEuLcWSLLjS0rjmEospBop_YBVndtxf95ohfBZ-n2IHASlED3Nk5v4_an6-89PW3NJupXkwThi6fD4ibwVA-RXotwmfmBZc-ID45TMkdP0cawQWpqFB4d26M4mlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
وضعیت عجیب جنوب لبنان پس از حملات امشب و امروز اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/news_hut/65226" target="_blank">📅 01:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65225">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-poll">
<h4>📊 اخبار جام جهانیو پوشش بدیم</h4>
<ul>
<li>✓ 👍</li>
<li>✓ 👎</li>
</ul>
</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/65225" target="_blank">📅 01:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65224">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">رئیس‌جمهور ایالات متحده آمریکا یک «تماس بسیار خوب با حزب‌الله» داشت، که یک FTO (سازمان تروریستی خارجی) تعیین شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/news_hut/65224" target="_blank">📅 22:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65221">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWsKlCnE_zp-Lmyu-Ea8fROb-i96FULhSCPlxKF2lf72YrE8bxDQ8e9EGj6kj5r1tK8Y9naCTaXJkyrkT41y0CIKFGTa0Kg-WwUomG0DZCxWrbXoLHNs2LdPM7ywAvxVNGIB7LsAfkxL1mPO-OLaARSl85xWcySqekTTHqEmTANRHXjJmeORAC78ErL7EDLkSLDE2sLtFAvp0VnD8wp5VHETyd4DDVcfKym4L5r20uI-FxIoHO76e-Ig0dEiMpBsIOL4FdXHmFw1YfL4vTelPrFlaEfROVEURW3jzAq9QRBk26KxglvCZyZGLYwfHRbEg-GyPMhpVB0qnLvCp-ddqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: گفتگوها با جمهوری اسلامی (ایران!) با سرعتی بالا در حال جریان است. از توجه شما به این موضوع سپاسگزارم! رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/65221" target="_blank">📅 21:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65220">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QirUnvx95Dd5I_VNe-TqaND8QwyzfGaTgCxso8uBTTTQormY2oxtRH2VoRufjJVLTUR_Diwjii3LQ025il8dJNCELuACKZTatqD8WrdPlncuRM1stawWSE6ic21eIwecIx684d4pQ2HgxYydev2o22prKEsl_TYZ03P4HVuvNBTMfRjwauwv7J5acR1QD8X1MkyEp7N_bpEI6aDz-n4ENOP4R_wssS7cV9Pm6tONRJ516BRhjqVUNnwvkXw6YBaA-Cyuk47pYeBbItbawKc9A1pr2iB3Z4NU5-nFiWwDdgoNfj7--CRYzoknQ5OUlSSWTxQscBbGFzndnPwuqolEOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
#فووری
؛ ترامپ: با نتانیاهو صحبت کردم و دو طرف قرار شد به حملات خاتمه دهند و آتش‌بس را اجرا کنند!
@News_Hut</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/65220" target="_blank">📅 21:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65217">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSA0_T3Hoh2nhaqVksnzKcLjk12R72fsWKMWuSwgHjEE_8ALQZhhQ8vXP4tAhqb38Qk1ILnR5ZT5S454z40YIS-6MD5pPHh697Wurvg_k88RQ6YE4tKuZUalOArXxyZ1JOf4oAFMBYtWNCGnDq6Hkln1P0PXLnLlJJ6gCzjPG-G6QV1DPknvhbOg1FpSvhY8K1hkr2Ax-EPwLySB2a-eMvRBjizJJD4ml3LCQOQMAyz6zHrwJAVd7AweA59yVhfbgK2Xh5L_upx6oAN7zRvGO22f98YjcC2ncrksoaZUbvYvaslMGI2737PgMtZdYG-SHpMnPvvJlkl2l3-2_hDm-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ایزدخواه، نماینده‌ی مجلس: آخرش که قرار است فلسطین اشغالی را بصورت زمینی آزاد کنیم؛ چرا همین الان تمرین آن را از امارات شروع نکنیم‌؟!
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65217" target="_blank">📅 21:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65214">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
📰
مصاحبه NBCNEWS در گفتگو با ترامپ درباره تعلیق مذاکرات:  فکر می‌کنم ما زیاد صحبت کرده‌ایم، سکوت کردن خیلی خوب خواهد بود. سکوت به این معنا نیست که ما شروع به بمباران کنیم، ما محاصره را ادامه می‌دهیم. محاصره یک تکه فولاد است. فکر می‌کنم تا هر زمانی که آن‌ها…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65214" target="_blank">📅 20:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65213">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇺🇸
سنتکام: دیشب ساعت ۱۱ شب به وقت شرقی(۶ صبح به‌وقت ایران)، نیروهای آمریکایی با موفقیت دو موشک بالستیک ایرانی را که به نیروهای آمریکایی مستقر در کویت هدف گرفته شده بودند، رهگیری کردند. این موشک‌ها بلافاصله منهدم شدند و هیچ یک از پرسنل آمریکایی آسیبی ندیدند.…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65213" target="_blank">📅 18:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65212">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kuEV4NPKX2KdLFGnlZRSRRqwRH2cez6-KM8QOV2IjgeQbQKOb52T4VQx9iikf2dK5BmtqoR7uArFcn721yiAAb2LlRFIrDuaOYcG2zUoPyrCQyoV461TFwl4osKx3pyFlhX8j-kypgVYKawQtOpFUdw-6v_6nw5uwmCHiZH-OwlrIPDAA6sOgyAUMEMrxUHQFLbWSg2WQSPfi3oRCcNJF7QGyVYfo_XIuTcVyccp36MJ3CWc3q89fQ0Lk7Hp-52D3UT8v30swgb21Qo9krs6mqVrOK0py1xLt_wNLoJl9lx_YhPnIMKuNoDK9uYZIaEwTQQm82wswLXoRBcvpo-99A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام: دیشب ساعت ۱۱ شب به وقت شرقی(۶ صبح به‌وقت ایران)، نیروهای آمریکایی با موفقیت دو موشک بالستیک ایرانی را که به نیروهای آمریکایی مستقر در کویت هدف گرفته شده بودند، رهگیری کردند. این موشک‌ها بلافاصله منهدم شدند و هیچ یک از پرسنل آمریکایی آسیبی ندیدند.
فرماندهی مرکزی آمریکا هوشیار باقی می‌ماند و به حمایت از آتش‌بس جاری ادامه خواهد داد و در عین حال از نیروهای خود در برابر تجاوزات ایران محافظت خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/65212" target="_blank">📅 18:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65211">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JSEJtAtmQoFUft3zTUKzNbTYmpRRM7VXtBNhzDNBStT_pJQPKxMe478-y0gKtFH1AJ7_AH_YXJNcUbgpgBRPqv1HQvumwEu7sKLUfUEuqeHvhQ0ExB6fZhNGGGGlXUOpMWumSS73BXfLmiuq8tNNhloJkDoX4p0Ki5LTb5bmZS2D8heslQxYMLjiPQgj5bJLPgz7bvmDT3vm5YnCK2zYO6xIxztf6TUtfFkaqODHgyEQZv3WMOnd7Nz6tCaprignqeq4vl2eOp3A4obf1425pFPZgg0MLuA1nGX-ohfkoTATUuG4zDLIsp5UViyYEUo7ILVZpcVlVqdcKWbL6CJRlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیرنویس فوری شبکه‌ی خبر به نقل از سخنگو نیروهای مسلح: تداوم حملات اسرائیل به لبنان قابل تحمل نخواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65211" target="_blank">📅 17:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65210">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RplCj2qX9cMj6nOBgOlgxDwNszpLtbD-ki7bjEdj-go8m2-fFK7mjNHoNil72AH1-4HIunR3sz0kS0SSOuROL14dwS_mZLPYLXSBBXTK4f1HyDu2WPQUIGRmcdRk10eG7Ri85DXL1I15TzA2_kh1UaGwyUQPBZNyq1VdZMydlSQWlAxxFJIqHSI79T0tJHvxeMr9k_kOsyaBScEJrku_HFhAF29y3xN62Q8iUV9mP5B7FLYfr1Eqw4qncIPwOsT8bBDY_sZI2WSE8jGWO7nqumQmkcjlrW7lH7vdFPg8QqzkhNoV56SSZREfyj1ukDfsdzke-s_gIc_Jy8YUiZRrjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تهدید امریکا توسط باقر قالیباف: محاصره دریایی و تشدید جنایات جنگی در لبنان، گواه عدم پایبندی واشنگتن به آتش بس است و هر گزینه ای بهایی دارد که پرداخت خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/65210" target="_blank">📅 16:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65209">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIIKrSaApEVvOo9EC-AIyy4Rc2TwqxfOQWFzHY_sPGdtO1aObyz-F00kTaT8RrwhANGK-iSPbpFvFCKwgpf-jUm9yJS2w87UYiWEv3FbyByIN5vS-PJKD8r2V4ej053KratHzpNCdtQb2eOIPvX_oa2oOgS5ZDu192_hkgGTonKlAtavd9aZPDBj0fVmFfYVje5iIV9qQ9GB6wNCpoxqVwqLi-Z1hnTL-S5LODxAI5y1qqbniPjqO6Dph1Pj4B_yNg472Rc1G-Lobzh2nQAYs9J6UefJs2bAc-XYFnMiBAPD24Es73Jb8sEZcZPFWE7lG5I6G1gaVwMYaVLjHDRHmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی، صبح امروز و همزمان با اذان صبح، مهرداد محمدی‌نیا و اشکان مالکی از معترضان دستگیر شده دی‌ماه رو اعدام کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65209" target="_blank">📅 14:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65208">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65208" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65208" target="_blank">📅 14:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65207">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKD6JCmO4fQmj2tclOtRM-6XzIJC-igLl6aUouylNVZDb17mat7ZlRhibIdE-h1c_ozCxNzcWljsHz43-1rUo7XL0G54RHvQR6kIornCxuDS-Q88NyXKr_K_Cth34nCGoE8dBqaS9-LlGq9qF1dQLFkLHwqJJVuOihUN80qwH4wDoDlAX9xCBQ6Ib8xgMIUNthdRuH_xNzawBrmRnCQqwAINiIxFaYOMxOw4xIhLxLoJpREJrAJwFUykA9n6s0268Kuu7ABJuKU2BMVU1_XBTQRZG4Q1BlGpbsNUKx0yvl3vk6BlFv35kiqtRwiXUAETlGU9WoegPDcZtOwgutEsfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌇
بونوس‌های شبانه از 1xBet
🌒
هر چهارشنبه و پنج‌شنبه از ساعت ۶ عصر تا ۱۱:۵۹ شب، برای واریزهای 5.50€+، 50 اسپین رایگان در بازی
👑
Crown Coins
👑
اهدا میشه!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65207" target="_blank">📅 14:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65206">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ol39wEG3HLWfMcMDph5mu2ncQmqcwVxy-7rCVWz6RtEDdbM1aaevm2-QVAepG_fzRQDwXJE99lYtZZCOZ09MOg7zvfkoyNVOVWd8lKe9QidK4Tm0GYgYRGOV1ijiDi3SkeScjHFY9rrVBmjb-pedeSgA_oiaizXi7O1JfcFDAjO14j8yHMX4EVtdH1uPkcCARFqazVu8bJ-pIrpRzoBJfxi_T7OKRsAbbSALtWS8QVytRymmW1Ksb_KpR7RSVU9HN76o-GZQLsRxxkybqFMJ9pCcyMh9ErHKowx9P9rPuRv45F3ESDD-lphFnrSDlSqpzFLqaV6P1RWJE9G6D_dvdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: ایران واقعاً می‌خواهد به یک توافق برسد، و این توافق برای ایالات متحده آمریکا و کسانی که با ما هستند، توافق خوبی خواهد بود.
اما آیا دموکرات‌ها و جمهوری‌خواهانِ به‌ظاهر میهن‌پرست نمی‌فهمند که وقتی افراد سیاسیِ فرصت‌طلب، به شکلی بی‌سابقه و بارها و بارها به‌طور منفی اظهار نظر می‌کنند و می‌گویند که باید سریع‌تر عمل کنم، یا آهسته‌تر عمل کنم، یا وارد جنگ شوم، یا وارد جنگ نشوم، یا هر چیز دیگری، انجام درست وظیفه‌ام و مذاکره کردن برای من بسیار دشوارتر می‌شود؟
فقط آرام بنشینید و آسوده باشید؛ در نهایت همه‌چیز به‌خوبی پیش خواهد رفت، همیشه همین‌طور می‌شود!
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65206" target="_blank">📅 14:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65205">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
شاید باورتون نشه ولی ترامپ و کابینه‌اش همشون خردادین!!
• دونالد ترامپ: ۲۴ خرداد
• مارکو روبیو: ۷ خرداد
• پیت هگست: ۱۶ خرداد
زندگی ۹۰ میلیون ایرانی تو دست خردادیای مودیه.
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/65205" target="_blank">📅 13:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65204">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🇺🇸
گزارش سنتکام از درگیری‌های دیشب بین‌ امریکا و سپاه در قشم:  در این آخر هفته حملات دفاعی به سایت‌های رادار و فرماندهی و کنترل پهپادهای ایرانی در گوروک، ایران و جزیره قشم انجام داد. این حملات سنجیده و عمدی در روزهای شنبه و یکشنبه در پاسخ به اقدامات تهاجمی…</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/65204" target="_blank">📅 11:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65203">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e4c45b1ee.mp4?token=dj3foSLKD8Mo-IlEbbgm3crZMum4H9Fjg0q_ezJV7TSVsgGZiqt3eIZkK58j_71srtrwn5hIF8VZ7CAg81GhzenyEoCVN9wWvhJwI_CdhKCuuSrv_CWkw9Pj8qcywkm8HbEL8G4l7uwL3el2h9zzzHQddRuSq27LrI0rHsOlzUGSdPOQQHvLPMXbXDvLLrd0nx1T_sLl05vrCpvbLeqEuKAGbEgXsplIUUl8EHDFgOb5JN84td2Nhkibu2YQU-TCo9uwymJ3aPP3EiquifxI65FV4JfSGW-wolrgU6XWShl7l8WfLDSKZIxxocfDwP-58pJgLy53xyp8AzMigHlwjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e4c45b1ee.mp4?token=dj3foSLKD8Mo-IlEbbgm3crZMum4H9Fjg0q_ezJV7TSVsgGZiqt3eIZkK58j_71srtrwn5hIF8VZ7CAg81GhzenyEoCVN9wWvhJwI_CdhKCuuSrv_CWkw9Pj8qcywkm8HbEL8G4l7uwL3el2h9zzzHQddRuSq27LrI0rHsOlzUGSdPOQQHvLPMXbXDvLLrd0nx1T_sLl05vrCpvbLeqEuKAGbEgXsplIUUl8EHDFgOb5JN84td2Nhkibu2YQU-TCo9uwymJ3aPP3EiquifxI65FV4JfSGW-wolrgU6XWShl7l8WfLDSKZIxxocfDwP-58pJgLy53xyp8AzMigHlwjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواد ظریف در پاسخ به سؤال میگن شما پشت پرده مذاکرات هستید، گفت:
من اصلا هیچکارم
@News_Hut</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/65203" target="_blank">📅 10:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65199">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بر اساس تحلیل تصاویر ماهواره‌ای CNN، ایران ۵۰ ورودی از ۶۹ تونل موشکی زیرزمینی هدف‌گرفته‌شده توسط آمریکا و اسرائیل را دوباره بازگشایی کرده است؛ در ۱۸ سایت زیرزمینی، عملیات خاک‌برداری و پاکسازی برای بازگرداندن دسترسی دیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/65199" target="_blank">📅 23:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65197">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c57vNZO7W_7VwaWDmnQARGWVTY1mrP2iIHGNbzmmcIvfYLBMDrQwanoYaTbq6vhvzBHHA5zKabeHJr3lyZs9t6fs5v2htsBw6a1pZvM9IbfhvdvDWEz0SoIUAHCKtfB7YzN-9CZwsyt2VD34NHZBqg3P59QYPj0C1MlH36DkyAZdA9Nw1jUM3A6oyJEWxqOY04WrQ9jVh1tvmOU8hdLAF_Zz-kgS6DLSUrEqdX-AGAy2VyOv6GT5yGpZ4LvHok5W6OJkROuh2urXeUQDAwE8YiR3EC67TmAsurXwfmK-vkvC7_tN0Xj_cgcDcAhGZ-SuTy8EJevIu_BDlgrUUq5ruw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طباطبایی، معاون پزشکیان: رئیس‌جمهور ‎از خدمت به مردم عقب نخواهد نشست
@News_Hut</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/65197" target="_blank">📅 23:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65195">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">طبق گزارش The Jerusalem Post، ایران ادعا می‌کند پس از بیرون کشیدن/مرمت تونل‌هایی که در جریان حملات آسیب دیده بودند، آمادگی شلیک موشک‌ها در سطح منطقه را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/65195" target="_blank">📅 22:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65191">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
📰
#مهم؛ ایران اینترنشنال: پزشکیان از سمت ریاست جمهوری استعفا داد  @News_Hut</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/news_hut/65191" target="_blank">📅 21:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65190">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDfVKTHAkWM88BXXaUKVtykRH7JL8Zi3Jv6ZzfhYM4uNaQi628YJMrH2tN1IpCOh-s6CDqGs7sawMmzISLeXSB0NUt1qZy0meQF8jxF4h6V1M4qdfwtloiKLiJxceh3_r7KH-UN1a971owshLUJjTTsYGtFEQoj2Le6jkBtxTBlmvHcJcEIS-wNP2f8l_7n_DZFkEzq0tHYLv51X4rBZYRUNnAIjqJTql_q0RwDGhNBvqZJvPlEt72Clq2_OSC-bJEgYW3JYnXlwGZLv8sDsrT-jmcdAoY9R-BpG3Kfbu9RAjJhRGzrqJcgFjsrUkGV4aT4ImWP16Qw3434rdDM62g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
#مهم
؛ ایران اینترنشنال: پزشکیان از سمت ریاست جمهوری استعفا داد
@News_Hut</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/news_hut/65190" target="_blank">📅 21:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65186">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vXyeMKXRI6DMVDv50YdZXj6WyOamCcaMuzPLqJSXEE-Dtg6BFR6SSb1vipwE8lIYbVxNEj470dsETUaaLdqLpZReZnvxhZeLA7J4h0FVSR5Y5bdmPWdOb5P3v5vx6tutnudXAOVNG6OvDoXB0LT-vYHX7hlTaA7L5JdfG4SrMJLlOuLxapmhpY8jJPiWNALodijKXmlgqaAsRhVVVrhGCpAFdCrA3Z72FbnyVaIARthHvc5VHJQLg5n5OfTIcStqOxawDTpS-aPpk9evNabpZ3t236SJgH-R6bVrAtcIu6kAu_JtZKHXPuhknY3nPS3ssPbFlu3nL8RG8gSaAbfXQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eMQVRBoz4hHad7AWVTObn_A3coY4ZayC2tGw-aEvrSMbqX_5pccyRaCS-pzWEgUwPmOmAhHu3IX_z0bCCfJTWXp7m5xnhDXxaVhTsDSkNvqRNuXHKrtc9iI5qkdQUWNws5yisVQm10c0BQ5TBmmR_qJ58mRBnGrWz0JsPdn0qbL2gIeqNNmPRHqbd-5U-xpPcW0kQKYOoj457t8KzqYM06gj5gnHStsVxlajuE6GRNrWNNbEPKYNO9B34iP0DmFK55ztvhjAKOU5ycHw3IvKDgB1HiKBy4JKyHU6sGDntguJGa5s5DXQ2ofmt_EsU3TLmcQsKR6R4ZaT5hKhjPv4Zg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a589784b7.mp4?token=HufHQe32ToAGyAJI_kLq16Aj6FCdNg6n51bojEXDqLMfGj9JpnracFqk1Qm5Lxs-o8To7KG7Xj8RBkwXX27fUOXZ9HPkAIMqEgYuBIqHCuaO3CyoJB2i9KlfflpcR4pJUs8H070ctS7fotPLlj4jmyC1IsZ1c_pWn5uAHTqKkavl3x0LxvRqM03_OcjnioyvQESd0BYxkC9QMKRel4pNAUFXbHbqhaqSE3l-ecIJqZfE2XQOJUK7ksoen5mm9G4pN7Sra6zC13Zh1WFRepuOZMRi3xL4f8Saf8g5bhXb1lJOwB1iy01_L-SfNMHUU_ecFnbPZBPKb8cb5cmeL6_Aow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a589784b7.mp4?token=HufHQe32ToAGyAJI_kLq16Aj6FCdNg6n51bojEXDqLMfGj9JpnracFqk1Qm5Lxs-o8To7KG7Xj8RBkwXX27fUOXZ9HPkAIMqEgYuBIqHCuaO3CyoJB2i9KlfflpcR4pJUs8H070ctS7fotPLlj4jmyC1IsZ1c_pWn5uAHTqKkavl3x0LxvRqM03_OcjnioyvQESd0BYxkC9QMKRel4pNAUFXbHbqhaqSE3l-ecIJqZfE2XQOJUK7ksoen5mm9G4pN7Sra6zC13Zh1WFRepuOZMRi3xL4f8Saf8g5bhXb1lJOwB1iy01_L-SfNMHUU_ecFnbPZBPKb8cb5cmeL6_Aow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
اسرائیل رسما داره حزب الله رو تو جنوب لبنان به شکل خایه‌فنگ‌طوری با خاک و خون یکی میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/news_hut/65186" target="_blank">📅 18:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65185">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C39qD8uM7BJP7opManTSEjyMgJqHfvmfmt57WpjBsiYlw0aHV00KB_O3YtyUvyBIsdG9kO4UljLhv5LfoBS3nm6xFwZjIr5a3lbmk_IYMP8WTOt5IICghdjctMNChECBE7wPRa_EiWhO7V1wZBeY1GYqVymDlj9GDIjciwm8PfkabmaBa4NHuC_EbFU3qhaYHuaYEIzjanZc3e0QEVkHPQsgZe6vH6K_geRqzh1I0ROuDegFbG9QpR7S785FaxPhwHP0-v8WgnAuWQvFUhsmAUZGG27-LapCCKFAmauUVtSBE7hqk4UpTBCIyIqBmGoocWKskfc3mNeR_K35R7u6RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست قیمت جدید خودرو های مدیران خودرو با ۸۵ تا ۱۰۰ درصد افزایش قیمت
@News_Hut</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/news_hut/65185" target="_blank">📅 15:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65184">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
گزارش شنیده شدن صدای توافق‌های عمل نکرده در جزیره قشم
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/65184" target="_blank">📅 14:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65183">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec47112ddd.mp4?token=ELt5IK0L7V0kOCAPzybv96ZxtHeuLAZzl5Zn3fE1GM3CM6a4CwWPG2PgmJ1k0zZ9xFu8aPBMqWFEbn0ue5L249vXxLw__st5wOwAay1Yh2oNS8uu1RG8nyg3U1wGsjFZePX1ulmetqWt7NupMzLLG56JC0pj1Gfp37ZySl_LmxeKm3PnZfOppep4PufEcmxqZedNczioJJBGS_Mre4LUb2NjA3Z8axTDCV9UG7EEbyC33t3c2SZZtGxOcMJNcQRfGsurBnsTRmgpW4UumDuRJUWe1dQbjxoJqSMKDAIsgkhtA49cvnfI0GN4uUeMgoBMNJE6u2NKEz_8zM7FeWBCvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec47112ddd.mp4?token=ELt5IK0L7V0kOCAPzybv96ZxtHeuLAZzl5Zn3fE1GM3CM6a4CwWPG2PgmJ1k0zZ9xFu8aPBMqWFEbn0ue5L249vXxLw__st5wOwAay1Yh2oNS8uu1RG8nyg3U1wGsjFZePX1ulmetqWt7NupMzLLG56JC0pj1Gfp37ZySl_LmxeKm3PnZfOppep4PufEcmxqZedNczioJJBGS_Mre4LUb2NjA3Z8axTDCV9UG7EEbyC33t3c2SZZtGxOcMJNcQRfGsurBnsTRmgpW4UumDuRJUWe1dQbjxoJqSMKDAIsgkhtA49cvnfI0GN4uUeMgoBMNJE6u2NKEz_8zM7FeWBCvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: بزرگ‌ترین سرمایه ایران، «رسانه‌های فیک‌نیوز» هستن که مدام موفقیت‌های آمریکا رو کوچک جلوه میدن
شما یه پیروزی بزرگ توی یه نبرد به دست میارید
ولی اونا میگن شکست خوردید! این واقعاً چیز بدیه برای کشور ما
@News_Hut</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/news_hut/65183" target="_blank">📅 14:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65182">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTM7YBl0MRKXkyfRF0ruz7l8QK3-SUIRgjStdoMqmmCepa3i_ln3UTD5mu7SJIvxNVYykKEFk_2NBPdWMRbeaklI_1fWYGBdjG517c_IYBMxtSMsV66KCL44Ky1njyMC8EgYTF-zSfWIkqYvgtEpihzL657BkhXDmrYAvEOKn09Suxg71VmIBy_zqWQgGbdlC5s_9ot2quYH5wb1B7zGWKTsPV_rrtpRAp9dnzuxvKItcMo5BeCwExmud7-yynnMitaRMb4z7P85EZj48DLnfSLsgDXumX7h_lSRmg89Qt9s4UQPPUnMv1GHY-O-zqRE_BPEuWpUzAUbwtzLKCKbQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تردد خودروهای پلاک مناطق آزاد  تا اطلاع ثانوی تو سراسر کشور مجاز شد
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/65182" target="_blank">📅 12:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65179">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/473b1fd669.mp4?token=F2uNof2d2xm4gPnfysG2sThSCbIt9nTN0ZRTuWw5BNGvb7VlPQUlG8h8VaEorF3i8xyVWio2BW_lu6SXAXt1GFVyt1sC1HT3qtB-AhBEK2he9aYTfv4_6QXIt9f-5vyRu6rPN5xNUXJi3XPqTQDM_wukCjEv_ddmO7Z3ounDOwbbqigBArWDakrVh6DGPXZq44ZTpuVuGBOZi5px_dDUBFJg_uT16VGs_vuzN-812ghMwJkSCKbnOWBBhPPluLVE1cT2nf2j5FXKpMHycqZMCP9Uada1s659erQV-N-MYQku9GbAasKbCKiAQe9mKX553HKTO8AjQxQA50XDK7j_iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/473b1fd669.mp4?token=F2uNof2d2xm4gPnfysG2sThSCbIt9nTN0ZRTuWw5BNGvb7VlPQUlG8h8VaEorF3i8xyVWio2BW_lu6SXAXt1GFVyt1sC1HT3qtB-AhBEK2he9aYTfv4_6QXIt9f-5vyRu6rPN5xNUXJi3XPqTQDM_wukCjEv_ddmO7Z3ounDOwbbqigBArWDakrVh6DGPXZq44ZTpuVuGBOZi5px_dDUBFJg_uT16VGs_vuzN-812ghMwJkSCKbnOWBBhPPluLVE1cT2nf2j5FXKpMHycqZMCP9Uada1s659erQV-N-MYQku9GbAasKbCKiAQe9mKX553HKTO8AjQxQA50XDK7j_iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: اگر عجله کنید، توافق خوبی نخواهید بست. اما به آرامی و پیوسته، فکر می‌کنم داریم به آنچه می‌خواهیم می‌رسیم — و اگر به آنچه می‌خواهیم نرسیم، به روش دیگری به آن پایان خواهیم داد
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/65179" target="_blank">📅 11:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65178">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4173e3828.mp4?token=oaxJtqu-tiXFzkemzsbmkJSq7FS5HYj3Ho5qR_Hzw6ToXaWDC_S-_6whwDNtWvWmtP8g0NZ0s3wCrEeYXPAR2GFqGmJUjYw54SmxXfcjQqZ6qLPip8QDbCK3KUILibaOBV4f41HlicXvR5mGtHU_vsFIjPdBokNpuTQonhLHKvZrovq2gx6WNzX72DMMQvmUWhKWAXXJgMpBNMljer-FtHp-N-3iBfYLZop14qdMzNO9OdBE9IBYr-nJjZTgwx_0G26Dn6NNB0KXCZsnuxOTCdtQfveYlylBHVDd-j67EOhcJsLThX7b9c7MRD7Osg3fWOdTKJqXwyGp1zN-SbJLhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4173e3828.mp4?token=oaxJtqu-tiXFzkemzsbmkJSq7FS5HYj3Ho5qR_Hzw6ToXaWDC_S-_6whwDNtWvWmtP8g0NZ0s3wCrEeYXPAR2GFqGmJUjYw54SmxXfcjQqZ6qLPip8QDbCK3KUILibaOBV4f41HlicXvR5mGtHU_vsFIjPdBokNpuTQonhLHKvZrovq2gx6WNzX72DMMQvmUWhKWAXXJgMpBNMljer-FtHp-N-3iBfYLZop14qdMzNO9OdBE9IBYr-nJjZTgwx_0G26Dn6NNB0KXCZsnuxOTCdtQfveYlylBHVDd-j67EOhcJsLThX7b9c7MRD7Osg3fWOdTKJqXwyGp1zN-SbJLhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار حسین علایی: ۳ روز قبل‌ از جنگ رمضان‌ به آقای شمخانی گفتم آمریکا و اسرائیل با ترور رهبری جنگ را آغاز می‌کنند، آقای شمخانی گفت «نمی‌توانند، پيدايش نخواهند کرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/65178" target="_blank">📅 09:40 · 10 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
