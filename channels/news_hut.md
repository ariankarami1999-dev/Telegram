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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 11:58:49</div>
<hr>

<div class="tg-post" id="msg-65308">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b7d22fc01.mp4?token=K6NOwj2MmwidB69elEj1Zt0TUnl1ePiAeeSw3DIskRkh41f3EQVyz_A2dI3FgB3GD6tnkBGflY258l3zV59e6fgzLB5vG9FbYlEhLM1L7c98gLw0-8SZbC3FUfOzYl6i2iBz0Z0Mvir6O1d42MKp94OJbV4H1Q-IYs-vhzuZRK2h9XWOftKgk0qmxUO0aKrja3JmEV4lxKXwAMgOw7btPonVZw1zh6exh9jfUrUwvaMYmgB193OxGP_9OKOAfmGyfzwD6_LUrH8mwXekU-3y5QpNUjo0hUvWDPnc4Mm2PEXxuB2-kHKxQ7DS9Nin2u39K57GRmKSxP2OJ8AbwojpOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b7d22fc01.mp4?token=K6NOwj2MmwidB69elEj1Zt0TUnl1ePiAeeSw3DIskRkh41f3EQVyz_A2dI3FgB3GD6tnkBGflY258l3zV59e6fgzLB5vG9FbYlEhLM1L7c98gLw0-8SZbC3FUfOzYl6i2iBz0Z0Mvir6O1d42MKp94OJbV4H1Q-IYs-vhzuZRK2h9XWOftKgk0qmxUO0aKrja3JmEV4lxKXwAMgOw7btPonVZw1zh6exh9jfUrUwvaMYmgB193OxGP_9OKOAfmGyfzwD6_LUrH8mwXekU-3y5QpNUjo0hUvWDPnc4Mm2PEXxuB2-kHKxQ7DS9Nin2u39K57GRmKSxP2OJ8AbwojpOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: عملیات خشم حماسی پدر، همسر و فرزند مجتبی خامنه‌ای را کشت.
🇺🇸
ترامپ: من فرد مورد علاقه او نیستم، اما احتمالاً او یک حرفه‌ای هست
در برخی زمینه‌ها آوازه خوبی داره، برخی‌ ازش بد میگن اما خب درباره من هم بد میگن!
@News_Hut</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/news_hut/65308" target="_blank">📅 09:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65307">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">پرسرعت وصله
👌
👌</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/65307" target="_blank">📅 01:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65306">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/65306" target="_blank">📅 01:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65305">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/65305" target="_blank">📅 00:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65304">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/65304" target="_blank">📅 00:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65303">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/65303" target="_blank">📅 00:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65302">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/65302" target="_blank">📅 00:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65301">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NW6QzzcH7sAByDqhnIgzfXAKywLp0F2OzgdNHxw_cECxT7S695axbNurYpxtNjzH6CypwR4r8gktUzOpZ394LzVo0DTLvfLLS2DXXMnKhGNJDBeUVXpD6DupzdJUZR5k7xUIQkU8tU_q17ZznZPRlVdRqFMvmN2DEPTOtGgHlACQrMSYT4nDSeHX-JmJMTv8_HWV5r2avL4NCHQhOwbeGMI2rI1Vx_YUGZYe-Hbpb2sAczwCqOqTOQqfFkTgA3KQoukS7-TUtrbpD38XyClw6qDUPPEdXMxtynEucxPziULYOxN0IG71-9MCJrSq8WZPPjb7EbC2faSquHLgjmlwxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تورم نقطه به نقطه سالانه برخی اقلام اعلامی مرکز آمار: از ۴۳٠ درصد تا ۱٠٠ درصد
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/65301" target="_blank">📅 22:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65300">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/65300" target="_blank">📅 22:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65299">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mSpLB7R954pqKR3nK0GbeGDKpAeTShzqNCzb5Bkem596pQ1aEmK5Mc4TZRozoL3wxbObScv7xkCEWcxD8FU3r2Rc0pcMYWfob4F1MKzs9Ft-EdD8BqDbyehStx_QLhU42SeDTW-tECbH1vtSmmGMTjdgYjN5QeEdTPlw2NjY7hstg3iBrQKrisQYYqoBFj5-D8lb_L_N8KInGRR6SuxjF5KVRM0I0Q4N7QD8qeusUi0Y9DLe1yTqg0uSht98LHzMHV2RTsyScbmYWQxYnjR8AKN98DTYQUKUsKHVg8JSgyPbr_AMvqGyl8HtQ8N6ZI6ykNLOmW5JNmUNCQMxa84iRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن های chatgpt، grok و deepseek رفع فیلتر شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/65299" target="_blank">📅 22:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65298">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/65298" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65297">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🟢
سایت معتبر رومابت برای جام جهانی بونوس های متنوعی داره ، از دست ندید</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/65297" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65296">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/65296" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65295">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ:
ایران موافقت کرده اورانیوم ها تو خاک خودش از بین بره
📌
با این حساب ترامپ از یکی دیگه از خواسته هاش که دریافت اورانیوم توسط آمریکا بوده هم کوتاه اومده
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65295" target="_blank">📅 18:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65294">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qt7nduve4exKx4-lsPAwZVO_ec_yezO0Z21lqvcdXt7xXLOPhwIXzfmBJdvjRwG95rhZfAfApO5d_gC6bm3v4-W-OFYHB8bdfqhbL3rXRUzBOHN1QUhkqEe1TYqpRK6h9bMotPOlViZ6gsAbx3TdNYTxJqo7qbApxeY0hZfmh5I5lAF2DFPbAR0znmbYcUzIkYbSQ3h99SuX6S1_Z9_kA_TCFmLoOnAvRXu0OJ4Cn2o5MFezjVE9_18HDzyN_Ca5wlRzCCZqBwoC2Prtys92eOG_pEXuBw_XyA6tUeOiwXprGFSxNve8xUL5ymx759mbBvHbQ_nOYrjVWTvw8P7K6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
وال استریت ژورنال: ترامپ به طور خصوصی به دستیاراش گفته که در صورت کشته شدن نیروهای آمریکایی توسط تهران، آتش‌بس با ایران رو تموم و جنگ رو شروع کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/65294" target="_blank">📅 17:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65293">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlWqJHnUTJwIsAfpUOBHQyiFV2V1C_8PcQtZ8KHq6mAmN-b5Y6nlzvUIVVN0TL0JRtH8yjxTH2NIEKVu3GshZMh1oOhc5yqaVZPT_9_b055v4QOCnD6u2ohZjOsLgNWU8EGqFb-rzRqkxxH_9pdlrpr0XvIKDNhMchYXLfkrmHKgPvI8fjQf5x8sMdP1rsLY3zAdClK6ptpvRBnTDpEJoa9INACWRQEcFIOoz1Q8OmzEstyvrPnNocTbRREAEPqba7Fbxa9cddfUE3b4CGKuJt7Jg-7F6G9tByXvOXlWKFrnMW82AHVwAbokZsyCo6sTWTPN_4cJH5ML4HilZE9PRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/65293" target="_blank">📅 16:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65292">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/65292" target="_blank">📅 16:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65291">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/65291" target="_blank">📅 15:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65290">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-XPh0l_IM15R_0h3Qw84Kslmt0VUVNibWhrBr8mZ5iHEDBSSd35pH2zYhSIjhLAlFsrSRabRwGthyBxNMsofw1r2nYWkHtRd-JXEpHNkd09JakrhiIcrQV4TpMyK1lF7D_jXx4dTspQNiV8mPIeyLcGYUIBC3r-Dq-dOW-UW9sxI1QaQB2EWjMGJQnuZpiuU0HNlcSmepiM-mLE7SDJ1VWGgIaYRbl_jsozxJbzorqQqkBaE0oEQceSPlOMy8N7Sj7GF_fIhe73-qE3CmtqwInf9HONtE05aOp89MM4tMl_w1JYFh-zPoR5Q9KkbKL9ujFPKoTI1G0MXhsmUlV9Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تو ۲۴ ساعت گذشته بیش از ۲۰۰ میلیارد دلار از ارزش بازار رمز‌ارزها ریخت
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65290" target="_blank">📅 14:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65289">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/65289" target="_blank">📅 14:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65288">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/65288" target="_blank">📅 14:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65287">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f7496394.mp4?token=m9LQ70HHVUm0yC0bs10dz8nwVZ-g9nAsQwVPpPSR6gdpwDH8sthsDx3Bzk-Wl-t0KetxaZ6VFRcaX7KV9-ZE-WXZlm6WnBD_MzioOwAqlP4nyrN6KtnkTyfnJpx5jpKZryXzYcedPPPgPkQzpZ2iGbvBi6N996MpKG4IKXC5P9bibC5lX18P-ZEw85A07v23Ic_TGFalXoUJ-CeWvqlVzil8A-7qJfdqsrKc2qoA5K_RLM27ARuK1wVstA8UhljJf_eNt0WgJUpyE2Qpcidh3QKtsrSeBY_LCzWfZB3RZaTvoKY0X-CG5PSrqu1zp0wYfEDE-rWrnWenDAukEPlLzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f7496394.mp4?token=m9LQ70HHVUm0yC0bs10dz8nwVZ-g9nAsQwVPpPSR6gdpwDH8sthsDx3Bzk-Wl-t0KetxaZ6VFRcaX7KV9-ZE-WXZlm6WnBD_MzioOwAqlP4nyrN6KtnkTyfnJpx5jpKZryXzYcedPPPgPkQzpZ2iGbvBi6N996MpKG4IKXC5P9bibC5lX18P-ZEw85A07v23Ic_TGFalXoUJ-CeWvqlVzil8A-7qJfdqsrKc2qoA5K_RLM27ARuK1wVstA8UhljJf_eNt0WgJUpyE2Qpcidh3QKtsrSeBY_LCzWfZB3RZaTvoKY0X-CG5PSrqu1zp0wYfEDE-rWrnWenDAukEPlLzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئویی آخرالزمانی از بمباران پایگاه چهارم شکاری دزفول در یک فروردین که به تازگی وایرال شده!!
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65287" target="_blank">📅 11:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65286">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cmarm_vkKIllHnpI1YJInLnr9KdPfPaEZjXS6Q_CB7oxa8HuCIZ9IzENe5u-ewjwgCeSdfRs1bCF91u96hGPHmNcJkdiXRvzDyL7b7oze8lVHUy0N6ySY-Ro1UEbpzyT-kdyaxIncF_sAzzZTtj6xQiSzoy_Px8AXpIUYBImzKzuq7DUezbxaZnMLe5g5bR9wFO0TpYqGKr9tg2oVbyXIq6zVGbjvaPyHAqHrZFPnbSDL9kB2GZfGBnIUU8WMQuV_oG1gARKzF0lE4lDVKW6VgS6mrzYFq7e7hgRWVO7eJlEVzhvkUyB4trJlBfsHQXRCNVKOFEZeVKXwawd8qQf3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژنرال دن کین، رئیس ستاد ارتش امریکا برای اولین بار به کاراکاس پایتخت ونزوئلا سفر کرد و نشون میده روابط دو کشور بعد از افتتاح سفارت داره بهتر و بهتر میشه
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65286" target="_blank">📅 10:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65285">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‼️
کویت تصویر لحظه اولیه حمله با پهپاد شاهد از طرف جمهوری اسلامی به فرودگاه این کشور رو منتشر کرد؛
وزارت بهداشت کویت هم اعلام کرد طی این حمله یه تبعه هندی کشته و ۶۳ نفر هم زخمی شدن
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65285" target="_blank">📅 09:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65284">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31e323d6f5.mp4?token=Odg7iL81An0Ne2yTua5eEWLz8Ak9uJTDZ9HiJFZIzwO7KgTc0MZMZvcdC-GNxqNOCimSohgJQ5pBVtVLTKWbZIytHRFBBHqtk5PfLjGRuiZrBYOwNZQQse6YQUelZnmENKMseizy1Ujxa9sf9UJK5Opc1gQ3uaZj6EDFZe09N2Ol55igLtty7fiIHE8oI7dp1Ou4PgW2cny3E6r5B67D_-TBEtJfOVZQHtQEI7vAzXOjRVjULypxeT38aRMi65IzWOBOiTcBp0QZN0GnS5Sds1eeWFwuSOxk_-FQR3SCgFkEOKQiZqAgyWm76Uj_R58k8VETqpmUsK02xkPoFN1DCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31e323d6f5.mp4?token=Odg7iL81An0Ne2yTua5eEWLz8Ak9uJTDZ9HiJFZIzwO7KgTc0MZMZvcdC-GNxqNOCimSohgJQ5pBVtVLTKWbZIytHRFBBHqtk5PfLjGRuiZrBYOwNZQQse6YQUelZnmENKMseizy1Ujxa9sf9UJK5Opc1gQ3uaZj6EDFZe09N2Ol55igLtty7fiIHE8oI7dp1Ou4PgW2cny3E6r5B67D_-TBEtJfOVZQHtQEI7vAzXOjRVjULypxeT38aRMi65IzWOBOiTcBp0QZN0GnS5Sds1eeWFwuSOxk_-FQR3SCgFkEOKQiZqAgyWm76Uj_R58k8VETqpmUsK02xkPoFN1DCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
مجلس نمایندگان ایالات متحده قطعنامه‌ اختیارات جنگی رئیس جمهور ترامپ رو با رای ۲۱۵ به ۲۰۸ تصویب کرد.
برای اولین بار مجلس نمایندگان تونست رای بیشتر رو بیاره حالا این قطعنامه نیاز به تصویب مجلس سنا رو داره و بعدش میره روی میز ترامپ برای وتو!
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65284" target="_blank">📅 08:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65281">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65281" target="_blank">📅 00:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65278">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65278" target="_blank">📅 00:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65277">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65277" target="_blank">📅 00:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65276">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wpcqpo8emKaoMh6Wp9jQVel63xB-g_uwVK2dEzb5AvLqesg2O-ME8-_2oyG6EEzBItqZdmeMASOe0PfWVfmEgPMNflAzTb3iZ9TmHSQiiN_RhxsTuptmZP_elx4BkprKhpb0Xfdnbxuacig9jby6euq83DqwG_fivtQMaovYCRDBwmYmB6BK44fgpmRDhWBKe1LPas_S1zAGkBcXw2TJakCC0A1J87WjyyJaU32f51gDWUxZtqREHcoo7pSUIdT6CXzRp3obPX-Gj6Yx9tbg-QqkGeHpslDDt9OVGAPDtw7YQBjkaPTJBr8EYjjESfUgoDCciRM8dUgGWDxqLKnhJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام:
❌
ادعا: ایران امروز ادعا کرد که به ترمینال مسافران فرودگاه بین‌المللی کویت حمله نکرده و خسارات وارد شده در واقع توسط یک موشک رهگیر آمریکایی ایجاد شده است. کاملاً غلط.
✔️
حقیقت: ایران با پهپادها به فرودگاه غیرنظامی حمله کرد؛ این یک حمله عمدی، محاسبه‌شده و بی‌توجیه بود
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65276" target="_blank">📅 23:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65274">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65274" target="_blank">📅 23:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65273">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65273" target="_blank">📅 23:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65272">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vlscy4eleOPtwPFjC-EFo8UbjtlTFfDLam71g8TJof51nkFqtNsTSzO1cY3j-kABKrvpBdZxogdYjEBLhcLQZF6VcNMm2Dm8OMtQ4cyuwlUHSFJrpT47iYdFJ6CUdL_hQDPusT8Uh3bMojpkz34RI8jyG6ujA1E_ks53NFhp5Vd4oxjxNyHAdLsXHhfsGDEF_KlcOjGOYf9S2tKUiVfRi77a_MBRCIyWYYGRy0UCXpGDvjCrGYdzguHP9Rm9O9OmQdLJ9hA4OS8T0Rkj81UYxCtEfv2xutdOhTbj1bXmf4KEgquxrTxPqmzTd-5XFQOarl0G9N_C-PhuJDZEFpokag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا مامان روبیکا گم شده دست کسیه بره تحویل بده شر نشه
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65272" target="_blank">📅 22:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65271">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65271" target="_blank">📅 21:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65270">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🟢
سایت معتبر رومابت برای جام جهانی بونوس های متنوعی داره ، از دست ندید</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/65270" target="_blank">📅 21:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65269">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65269" target="_blank">📅 21:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65268">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامپ: هنوز افتخار اینکه آیت‌الله خامنه‌ای را ببینم نداشتم، اما دوست دارم با او ملاقات کنم  @News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65268" target="_blank">📅 18:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65267">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: با مجتبی رابطه خوبی دارم. دوست دارم با او ملاقات کنم!  @News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65267" target="_blank">📅 18:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65266">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">کاکولدزاده تر و بی‌غیرت تر از اعراب حاشیه خلیج فارس تاریخ به خودش نمی‌بینه، به مادر این اعراب تجاوز کنی شبش بیانیه می‌ده محکومش می‌کنه
#hjAly‌
@News_Huy</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65266" target="_blank">📅 18:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65265">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65265" target="_blank">📅 14:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65264">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8fa16c5af.mp4?token=R4VOJ8DTaobl_qkU6bqRYRQQ1vWndq5nr15n5CwL8DD4YhMPMy5kniR5E5KPXJ1qsWLM7vMW184QLNqXNPdDQf6KQV2yZUWZGJo9Xa5Me_uVTnbBUrLBySrJLWHk0hCzmF8dOCmDJ0jmdsRVmJ3qGF_GSWQ15RdwUJNieGuyBa9MyPLhB6iZUTV4vjsK4Egk8fm9sM95Q96xr6uN_ef7mHEQ-RXN-S5ri-yLqDtXtCIRnl5-gctsLkXutZMmfhD1WGmoz-lxnvMIDgKT_AzhcmA0IOmSfIW3RKAOVrzHeHYZt_wB6pjdJMMDY9QyNMazhSi3dvcy_cXrsqx8pk1PWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8fa16c5af.mp4?token=R4VOJ8DTaobl_qkU6bqRYRQQ1vWndq5nr15n5CwL8DD4YhMPMy5kniR5E5KPXJ1qsWLM7vMW184QLNqXNPdDQf6KQV2yZUWZGJo9Xa5Me_uVTnbBUrLBySrJLWHk0hCzmF8dOCmDJ0jmdsRVmJ3qGF_GSWQ15RdwUJNieGuyBa9MyPLhB6iZUTV4vjsK4Egk8fm9sM95Q96xr6uN_ef7mHEQ-RXN-S5ri-yLqDtXtCIRnl5-gctsLkXutZMmfhD1WGmoz-lxnvMIDgKT_AzhcmA0IOmSfIW3RKAOVrzHeHYZt_wB6pjdJMMDY9QyNMazhSi3dvcy_cXrsqx8pk1PWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره اینکه آیا نتانیاهو او را برای جنگ با ایران فریب داده است:
منظورم این است که من کسی هستم که این را شروع کردم.
نمی‌خواهم کسی را خسته کنم، اما من این را شروع کردم زیرا نمی‌توانیم اجازه دهیم که آن‌ها سلاح اتمی داشته باشند.
اگر من نبودم، اسرائیل وجود نداشت
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65264" target="_blank">📅 14:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65263">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65263" target="_blank">📅 14:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65262">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/65262" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65261">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/65261" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65260">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
📰
#فوری؛ نیویورک پست: ترامپ پیش‌بینی میکنه که با رهبر معظم ایران، مجتبی خامنه‌ای که احتمالا همجنسگراست، دیدار خواهد کرد؛ «رابطه بسیار خوبی دارند»!!  رئیس‌جمهور ترامپ در مصاحبه‌ای با «پاد فورس وان» که چهارشنبه منتشر شد، گفت انتظار دارد با رهبر معظم ایران، مجتبی…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65260" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65259">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQVQJJQlXDmGt3VzTG4dS_KjVSHoh9ja07TLB8BfRHV02WyRYwVrliIBiuTxtjGFWsmplCs8JHJ8cJDbJsNBMlH6iyKXaDnbnDvSRvrvDG5tvzaAWj38tQQ3QLcyEPlnXurMPw8bVO6q1p3FMTAqhvd8GvM-DEaYWKmS-_Mo2DttGVPLBOCvqoR11NTx9mnOzaIzNPkTdJbj7gjtD57WRTKD1sAHRZly-PAbeQv04sThP2f89a6OOxC9qbDGc1zuXsdGzamvHO05QrlAQSKzAoSKCnVK72ye1MQIGQr8CZYXdujRb9P8ttDtxml4NEDkpxADCBgc3XFtYvej5-VYdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست قیمت جدید و نجومی خودروهای آشغال داخلی:
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65259" target="_blank">📅 12:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65258">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gHW3zZc-cNvEHUiGRcFezFQxjaNRJPZWJwEUVaZG5_zbPC3XTt3iCQBJhNopnmPlS7NRCcCllElWct70mJyL7oxw84OV4iqyFNjrJqhsNhu71YBIYEu2UTfv6MlqRkU73g0NnqWnTVIha7_GzGPykyqaXMeTzLDRwOr4HK2dQaybW0ktSHqaI7itBzdP2CxYxdkTBQyJhliURu1FjHZlx3q5B7H8YpDZKGJzC_cqT5R3DgM8sia5HTiF40GH_f0qx9z9wZXPxBLEqlVLr2vdn_gcI9x0gsGQZe_6WAkZQxRSZ5UTmQmi4uQoXf5uitVtZqh65ElsnjY3YMxCFoR6XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکنا: آخوندای قم پیشنهاد دادن علی‌خامنه‌ای در قم دفن بشه
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65258" target="_blank">📅 12:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65256">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EtA2JgkJPKl1Ky6XCkmvuzGb8lNjs9U3xVoynpzPyF_irHbg3bYTfu0A8P5LAGk_2svrfpWfjVZXdsNUBGqkELR1m3bg1EtDjgVxC02wx1AxQA4IbH9ZJ9E6AHWCaTWtsQGrknSOGfQhCwE-X9BhHyu2je2kY3ryHhA4QIDfTM1yQt64QIYlBxO_sB2dOh4qpU22z0yb9wltWxvAnUpchhYpvmgxbb0JZnUPn77Zo7nxq3_sT0KTnZ50pSjSOTzVe9FMwpy5GTKq97CkoH0znh0npWKF2tCJ3HIO7l6aFZ2BAd1Uit5DeNzlUn6CMtfRYHiMe7KyC2Gq0aQGuOn42A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hGlANGzzsDUrQgGSCESn-KpBVWgQecYpry8mooLJ75PtxShNYa6bRaRAS-b-dcmJ-mrSSN6rcIzj92pVBiucX8lrVenHR7yjjWruPhW_cKX3ka75RlgiepyJlckajJLqOcki_w4_qbAY2E8qfWtuQEGa6cBBcQW3x7D50vLdY8Af4ztt0dIJYQD6LXSRD9Rms3ei0FYmEj4Rgy3k6TsnxW4AHS-Sc_nD6rNgzk4CnybSdpwpkYPvPOqcrO9T4pIb_kDee5HFfw3A_OHyajFB4RAU-FwdkVCD3WLJ6VMdU7agwdwVMQGPcUx_kHF_0SMT_VcsjrcfpovT27duBP8VoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
وضعیت فرودگاه کویت که گفته میشه مربوط به حملات دیشب سپاهه
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65256" target="_blank">📅 11:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65255">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWhLOIljwILrJOXSvomP_KYSBfE1wrOCfRcOEu9WXVXKDLSdSTmYuVhw1iV4tm0SodOGtNZWIeuX20Eeh0QWNVxus9XZLmlZhR11JMJKsFpo5lIujlQfQaEaX4FptXXN1FwfGTl4_IeqnKQf81T8_9RMHq1DEqJgde-gHhXs66AiyfeXgoVVof4UWpp0nPUh289t0LHREjs0cJSqFoAi8_a21wTltfqQ_Cq0fLfi35p-C1LMcz34lRrl1-BdZrH4pl4aqShkcKEEfZbfGjSMGlGuUziFXr3-I7NWcbxQ-ZzmnBzICGo32AA7YhD3Q5g3qbnupZN4Y6q89wWm7nS4FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیت کوین در ۴۸ ساعت گذشته بدون هیچ خبر منفی مهمی؛  ۸۰۰۰ دلار (۱۰٪-) سقوط کرد
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65255" target="_blank">📅 11:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65254">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">طبق گزارش سنتکام، ایران چندین موشک بالستیک به سمت همسایگان منطقه‌ای شلیک کرد. همه آنها به اهداف مورد نظر خود اصابت نکردند.
دو موشک شلیک شده به کویت در مسیر خود به هدف نرسیدند یا متلاشی شدند.
سه موشک که به سمت بحرین شلیک شده بودند توسط پدافند هوایی ایالات متحده و بحرین رهگیری شدند. هیچ پرسنل آمریکایی آسیب ندی
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65254" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65253">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">هواپیمایی کشوری کویت اعلام کرد که حمله جمهوری اسلامی خسارت شدیدی به تعدادی از تاسیسات فرودگاه شهر کویت وارد کرده و همچنین شماری مجروح بر جای گذاشته است.
هواپیمایی کشوری کویت اعلام کرد که ساختمان تی۱ فرودگاه شهر کویت بامداد چهارشنبه با پهپادها و موشک‌های ایرانی هدف قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65253" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65252">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bac9b656e.mp4?token=VGoxHatWl3zQ97o4kYaleaPodybheCKGFB7qSLSvt9DNHdU-b3ORIaTJrt92uYvepeaHhoaGMLqgKs4cAivcd593LhZhbKzbks5SHPAhxJVLPK8UwjFsPUW3raVb8GIKPWHMQvMX_4uP0OAZmsVizdAgZKnDK4y5sx438QOd_OLmC-kv-A9XXaioaM-5jZX1E-OfJhY2A_sFbt7lOUCYBsSn_ExxcCvDYMKyJzQ2jGym3eVvKNVzbF04f2Qw-etZ8BTE72QPs02unlyZBjGCeooND62tORe3A_0bFv48X-lVaRHz9K_uY4zEaQReSkeVdG57rDlXGNo0ffg1m2FQ6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bac9b656e.mp4?token=VGoxHatWl3zQ97o4kYaleaPodybheCKGFB7qSLSvt9DNHdU-b3ORIaTJrt92uYvepeaHhoaGMLqgKs4cAivcd593LhZhbKzbks5SHPAhxJVLPK8UwjFsPUW3raVb8GIKPWHMQvMX_4uP0OAZmsVizdAgZKnDK4y5sx438QOd_OLmC-kv-A9XXaioaM-5jZX1E-OfJhY2A_sFbt7lOUCYBsSn_ExxcCvDYMKyJzQ2jGym3eVvKNVzbF04f2Qw-etZ8BTE72QPs02unlyZBjGCeooND62tORe3A_0bFv48X-lVaRHz9K_uY4zEaQReSkeVdG57rDlXGNo0ffg1m2FQ6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلمی از پهپاد شاهد-۱۳۶ که دیشب به سمت آسمان کویت درحال حرکت بود
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65252" target="_blank">📅 10:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65251">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
حریم هوایی بحرین،کویت،امارات به طور کامل به روی کلیه ترددهای هوایی بسته شده است
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/65251" target="_blank">📅 02:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65250">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
حمله سپاه پاسداران به کویت  @News_Hut</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/65250" target="_blank">📅 02:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65249">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
حمله سپاه پاسداران به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/news_hut/65249" target="_blank">📅 02:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65248">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✔️
اعتبارشو صد درصد تضمین میکنیم
ارزون‌تر، مطمئن‌تر و قوی‌تر از همه جا
🔥
ضمانت بازگشت وجه در صورت عدم رضایت
.
دیگه چی‌ میخوایید؟
😍</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/news_hut/65248" target="_blank">📅 02:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65246">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
آمریکا بزرگترین صرافیای ایران یعنی نوبیتکس،بیت‌پین، رمزینکس و والکس رو تحریم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/65246" target="_blank">📅 00:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65242">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rQ_chN3KMkz6MkxM0y5biHJwCDiTv2OgS0FH53cIifww41FYJt15fMRnwaXtpxuqCXQ2WRq0G4wMyt6PmM0Q4QHa4r0ExpW0dksl0eg-SZxdO9zzrK44S1qf5K6RGczmW2LXA4cdFiVinzZNJHrCRt2cBQ5qaoI_qL6_qUpCjgPqp-vCqZk7p-IMgQU-52ykXVIyHBx2xsp1xAF45Zj85HqrWyvb52gq3c98mR3H11ZeQaJfKdJvplQb_O467MIPHbPgccLOn6k1j7nEXBsDgdQIK49IYeZY7KTCDP6E7tVZPv1g5wpECMgUIdeQynbGT2hLKMnqJU60IgVntrak5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E4OeH6yxK-EMH7Mi03aIrtwC_vy0qmnKe0BPtxgiuwJYYFMY8_V0CbINrR1CL83A3CsDi_cHkGjNAt5KkMx5LrD27-prs8XogXI58_phZiczDurDPwK4TiZuYnhkdm8fMUZ1or-92sRAx74dHyjrPHLGTql_8UxTNbbqx8yAO_P6oxaA6nFfTtBA2AuBz1FzzdRAthI9ElJLP-aB8tmiGrXRi29F15mqZIXMlkeNhjKmsDJ0oqrzhuuMSh8xxd4eO4BPGNm0JH3oNkTjddNaiuzHR1yEwWodWlg4lW19tg5qLa5SMw8tK7H2GKGQ0y4RKpQ3WLVmf-eEVUCXj86Uwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه شرکت به‌نام دکترتور اومده تور آب‌بازی تو چیتگر تهران گذاشته که مردم از جمله دخترا و پسرا میان بهم آب میپاشن و هم‌دیگه رو خیس می‌کنن
ولی خب بعد چند ساعت از بالا دستور دادن همچیزو کنسل کنن
@News_Hut</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/65242" target="_blank">📅 23:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65241">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LgvqTYLbv7Fdf78tscoCSHq0a95Z1DEXEbxF0ya895rhENNRewd4um5JNfGblPiAMsmokSSByjX4Qmx4mdIQ5A792va_mipFlfKAhatRpBDHcKSent7wQCujE-UBL6WQXKKvgqum0g4KnabHOMWG6ZgM1LEIrnEjGtdll67eYjMtE1HEb6FNv5hAs0ZTWlnlw9e6BhBDNm1kuzPfJDfM8xrDzfoQhkelzwFA5yS1l1kXMs1ReOAFONrCRjRsWLLK9CRVNpfIsP18v36KJGVhT3OPzrMa2Dlc4yrumZyMNhydfFkZrKQ_knlZVt4vzrjjvFc1GLLYP9_H34c6dL9zGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام: ابراهیم لینکلن و نیروها همچنان به محاصره دریایی ایران ادامه میده و تاکنون ۱۲۲ کشتی رو از مسیرشون تغییر دادن
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65241" target="_blank">📅 22:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65240">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZU0RCehl4tIGjyf0zkCdABkLKPhwYc9_7jVUVQxkxJQQqe-heNlohbiDI3B3HXuu_VpT4ungcdE3knlui95DI47MmIMH5KbBh4f8OUeooHT3elBViEEE0PK975Z7A7jw7G8XX-ke5krFGz1Fw6n6zRKXE8QVTUrpNGWckeP2nJCMzqx1FxprZufcM_1VR5GOvuIGno4EzmMLuxMACMldgypNfmyfhDcwpxZL6pKnXE4SLiJxyTRr_iejI7njMVw4B0BFZwhC_LKvCocgYl9BcNgYWvTCpd6jwtmo-8MPoM0qvJsACkGs2-w0C08P2Wjg1zcbeeDaWXMNaCahJkGmYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق آمار، سالانه 60 هزار ایرانی بر اثر مصرف دخانیات فوت میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65240" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65239">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AdnvXHfv8IKpbzJ7mZXNZAfFCRNBGCS2jSklEKjL2S3gI6GpiToMrI3fe1GJZOyte9H1hs5WCxw6S2WmFCdNLwK1UnMNWD5blwK0FtEpI9sYj8m5Z5L7GFClkOwGkWatSbG3MrA7Za_dtIFT1-0fWcWqgQnex4CLL4wgpqnUsFNv1xExTXrvYWjunRRaB7aphX_xwjUkDfsJGTEkSCzL1Nhq_E3mIVgmqieIeuXpfhRzKQ0vxXFMNGmkEUZ_hzmocbjkEEyQ_5tN0X7rhmnNmoj1Bkj0PIY75kEHn-WIc_rKIMu5zPRDFQclZdP75Vki0JMwwimc_TGVc4mNfTJ_qg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
امتحانات نهایی که قرار بود ۲۱ تیر شروع بشه جلو افتاد و رسما از ۱۳ تیر برگزار میشن
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65237" target="_blank">📅 15:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65236">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgCkhVqWt8F1Mwd8yFOLuBwjCkVTmh-TozbgG3LH_MO31-EdPZ1pZJzUu9CWG0kTaUtTxyJyxSr8YkfrprDSVfcNksuuB1q8kaI8MsuPkaEH4TjZbnEpQkHd6s5XC_cvhU_MWRjTO4ghBOKQuHgxb1iiu3Zrh79GSWJYQx3155pKkFR4oS1t2OFw-I6XohJXQ7d3vHXKNren4CLDIbXwhvWcR0OkqjRWg7YUw3B2jf2GFvObglyFONq1661HxLc3AAimfIB7FD44Fnq8W2PbdvSZmjjOwu-40lQ6gYH7iKoTpo1HAceYqa34UDz9KBXRSfuan-ffpDTwb-KnrhisZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
داعش با انتشار پوستری، جام جهانی را به بمب‌گذاری و پاپ را به ترور تهدید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/65236" target="_blank">📅 14:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65235">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a43d73ec7.mp4?token=r0Qp9_uTAQpQnihQEP-4ADCnkNYK7CsgTA8E8pbPV5iWqJc5sbVJK8EeA1D3zbL3Ta0uFsy3v9XbQA130Aa7VKUTM9Qfdpc9lV967PWaq2pAEjpCjbn_TW5L6WSVARPeFOjWzkoSiHbfvCERdDCk-Sexh1KS_uRPTsDFr2xDnnTt-AatjB6QiSHzohKAGyxbjrwrjdU5QTP223mQF_1z7YBy3Lv9EmSOPxQw4eCnJRyaHdFog0F7m2YsZoZhdbGsEc93-e4IrfWTG40lakGCQcRLGnangqD96dxJxdnYwIRw7DAWeZI4VXx6dvPfKWiYHhraAz9mgrvaD5Ryujgu1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a43d73ec7.mp4?token=r0Qp9_uTAQpQnihQEP-4ADCnkNYK7CsgTA8E8pbPV5iWqJc5sbVJK8EeA1D3zbL3Ta0uFsy3v9XbQA130Aa7VKUTM9Qfdpc9lV967PWaq2pAEjpCjbn_TW5L6WSVARPeFOjWzkoSiHbfvCERdDCk-Sexh1KS_uRPTsDFr2xDnnTt-AatjB6QiSHzohKAGyxbjrwrjdU5QTP223mQF_1z7YBy3Lv9EmSOPxQw4eCnJRyaHdFog0F7m2YsZoZhdbGsEc93-e4IrfWTG40lakGCQcRLGnangqD96dxJxdnYwIRw7DAWeZI4VXx6dvPfKWiYHhraAz9mgrvaD5Ryujgu1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
علی‌رغم درخواست ترامپ برای آتش‌بس در لبنان، ارتش اسرائیل دقایقی پیش مناطقی از این کشور را که در تصاحب حزب‌الله است، بمباران کرد
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65235" target="_blank">📅 13:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65234">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f14e605921.mp4?token=Dqh3eXAZC1ESN9rTxT8uENw6uo1Y-vjqmG7ezEr09--PFGoeWEOzNL33G7yA0MQAQVhWx6G4bO25Uj15TolLkFlL6tR0p_5bq_3mVOvy35cRLnUenQQSlCTw3oc_AAFqvEJbFAmmS23pDspdud8K4azatM3VBgVYXNArfIKV20tWLqz9ENLdIpq0Jw8fmlkrYXjsruial2BnY4MfQE5_M6QWaRZSeyiESi4i6g0EKz0qZNi9Qby6bMaMxZHqwbO1Rclm4lKSArauR-wAdYLPq8OhONPTBeK2gMyM-_9IZudMIQ6mGZgnvMa6JiRg1pUBiiV73rIdRSpr6YExfJiHVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f14e605921.mp4?token=Dqh3eXAZC1ESN9rTxT8uENw6uo1Y-vjqmG7ezEr09--PFGoeWEOzNL33G7yA0MQAQVhWx6G4bO25Uj15TolLkFlL6tR0p_5bq_3mVOvy35cRLnUenQQSlCTw3oc_AAFqvEJbFAmmS23pDspdud8K4azatM3VBgVYXNArfIKV20tWLqz9ENLdIpq0Jw8fmlkrYXjsruial2BnY4MfQE5_M6QWaRZSeyiESi4i6g0EKz0qZNi9Qby6bMaMxZHqwbO1Rclm4lKSArauR-wAdYLPq8OhONPTBeK2gMyM-_9IZudMIQ6mGZgnvMa6JiRg1pUBiiV73rIdRSpr6YExfJiHVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b11e2b7f3c.mp4?token=NqYLTMrlWmtglEew-uENKqLRHuydy5pL_Ja2Ftn-_wm6nIRuSgUK6JZXo-GcKXzTCz6irHhdV6-RCoyJmsZhESichyZYwbKs8NDyfQSQI3KYsBvjCaUmbSJgskATNZadUbVKiuCuo8aabqV8VRIuJ7PDhYO_8kFJ9sMLgfjUj0BKfCpJ4V7s61az_fYZKR3t32SHGXRUVsnGAMcwVA6YkOAuAP4gMSh4p_IoNeY3Bvd9jUWzIh1aLEcOjxd03VIMfeAD5_l4334RMnm46777wOVpy-KBUw_jGeIfVe5TMaAvomuLMeQz0nSUNT7dpJofZiBIXd4dQDxkAGKoRtStFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b11e2b7f3c.mp4?token=NqYLTMrlWmtglEew-uENKqLRHuydy5pL_Ja2Ftn-_wm6nIRuSgUK6JZXo-GcKXzTCz6irHhdV6-RCoyJmsZhESichyZYwbKs8NDyfQSQI3KYsBvjCaUmbSJgskATNZadUbVKiuCuo8aabqV8VRIuJ7PDhYO_8kFJ9sMLgfjUj0BKfCpJ4V7s61az_fYZKR3t32SHGXRUVsnGAMcwVA6YkOAuAP4gMSh4p_IoNeY3Bvd9jUWzIh1aLEcOjxd03VIMfeAD5_l4334RMnm46777wOVpy-KBUw_jGeIfVe5TMaAvomuLMeQz0nSUNT7dpJofZiBIXd4dQDxkAGKoRtStFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امروز دانش‌آموزای تهرانی در مخالفت با تاثیر قطعی معدل، جلوی وزارت آموزش و پرورش تجمع کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/65233" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65232">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65232" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65231">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qF8WGC9y4YqBCwoxmh2QSg7Jx9BFzTgDwsJAL3WbhROYHGIR5j6-FwNxi9gxZBeLEsJYVUc2srLl8AYhUKy5wSxbsrsVRW4Qz1iPvU49UAwZHncJmkHSsDk7a48Tof9y3A5a5_cJi9IoOpGRLSDbh9TYh6QfOBhcgFUCm8DrVOwX9wdHoyZ8f37RdPVtCCFlY9PUqO5zMIW0f8rDX-Jqy6YCOnGpbRQhfhHF1_U2-TbnldWNNUHGENZjP9IHXXoSEAfAmicU2UmThVPYsdtLdR6ntyk4VmIwydJwCqgowyqeQb18L87kxmICAzp7vXWprtEwNscEhfslB_HLllltaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65231" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65229">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e2d6ed8f2.mp4?token=jG27iyBNlk8zW_zPZhxx8-ABpxg6dPbolWJvAEVS19bwP66nEg_CPBr-wPYGF3Ul1AUiV4-CVLQ8UPMqsP9G8AyCgJhNB98WyaAUtUOddQL9JkfBdu8LTk8HwBy5kqTu98NcMmQmJelDsNeazEwn-9FKLfwlywXlSiE_uTO-pL7BAUv1SvyDW_nOksoRZ4Qo5Q9eTtPmC3KSc8pUOOijALrm3VeIM0s2vtUkvHi21dYd4PA0FJA60HFyIb4gA_4D0-JuHgayf70AP-7wuWqzjSz5m5rNxSlAeBl8TzkNnFwh_GgHOO-Pztai_YpZw3s-_15_rmdZCMCQ2jFCICIltQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e2d6ed8f2.mp4?token=jG27iyBNlk8zW_zPZhxx8-ABpxg6dPbolWJvAEVS19bwP66nEg_CPBr-wPYGF3Ul1AUiV4-CVLQ8UPMqsP9G8AyCgJhNB98WyaAUtUOddQL9JkfBdu8LTk8HwBy5kqTu98NcMmQmJelDsNeazEwn-9FKLfwlywXlSiE_uTO-pL7BAUv1SvyDW_nOksoRZ4Qo5Q9eTtPmC3KSc8pUOOijALrm3VeIM0s2vtUkvHi21dYd4PA0FJA60HFyIb4gA_4D0-JuHgayf70AP-7wuWqzjSz5m5rNxSlAeBl8TzkNnFwh_GgHOO-Pztai_YpZw3s-_15_rmdZCMCQ2jFCICIltQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
واکنش یک‌عدد ملا در تجمعات شبانه حکومتی مقابل یک ماشین با چند سرنشین زن:
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/65229" target="_blank">📅 10:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65228">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e2983c9bf.mp4?token=bHxcUxyOrHN0o3XmjTKFUGvI4JhEW7N78dD4tr6kPfiYnp4jnobUuxW09Uo-XRTxLVsxNsOfohOxYiq8NTUyh-SL5jHRWgNUmlLx4umDUQo6ZAInXEU8d7BPsqo9kxtW8vPjPZ7h97kIA-p0h7FE1S5Ke__Vmf0EgylYSNUuuIC2BtMe8tgvIj2m2SK4V9EvdNCY0xbSl2epv7EMLbXs9oLS0-kAZMuEtcV_8gMfQ_wx9Q4ipAU6VJpcSUhk2GgcZXL-8ok_9FRj_H8CmrNOTkVicefj_E4dPuLNJZwLu5Ryylid76XaCspTXxJs9N08qSC8uRLzixPVxSoYqNBPyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e2983c9bf.mp4?token=bHxcUxyOrHN0o3XmjTKFUGvI4JhEW7N78dD4tr6kPfiYnp4jnobUuxW09Uo-XRTxLVsxNsOfohOxYiq8NTUyh-SL5jHRWgNUmlLx4umDUQo6ZAInXEU8d7BPsqo9kxtW8vPjPZ7h97kIA-p0h7FE1S5Ke__Vmf0EgylYSNUuuIC2BtMe8tgvIj2m2SK4V9EvdNCY0xbSl2epv7EMLbXs9oLS0-kAZMuEtcV_8gMfQ_wx9Q4ipAU6VJpcSUhk2GgcZXL-8ok_9FRj_H8CmrNOTkVicefj_E4dPuLNJZwLu5Ryylid76XaCspTXxJs9N08qSC8uRLzixPVxSoYqNBPyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
نواب دبیرکل حزب باقر قالیباف: آماده بازگشت به جنگ هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65228" target="_blank">📅 10:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65227">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/159f752950.mp4?token=T_YlFxYwT93lWrzfpXYiZp5H5abS9wEB0aao1JLUouaGewiAQZ65o6_PKuj30zdADsS7h5lnoi5HNgqonpuy9PqITirMLzpiMj2ft5PF69njLyUfZfROH8bidJLhjqrPSVVMSeXWNm5GAe1L2CbSitwtwunltP58LTu9YbL2-JlvC3JG1N1BNsthcA1sVJvODp2PYLgTkKGq24w5dJWRbxNHceJ-dAs08Y2aQKnK-QbMSg2kjD_o4AMfWx3wrlkhsGB6IP-oMNnSFqRupm9-sOPPKzmZm4EndCvPN9L6-aHghB-w2sX4YCpN355Iq_QylGgsuHDVpRO-DEtw61usqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/159f752950.mp4?token=T_YlFxYwT93lWrzfpXYiZp5H5abS9wEB0aao1JLUouaGewiAQZ65o6_PKuj30zdADsS7h5lnoi5HNgqonpuy9PqITirMLzpiMj2ft5PF69njLyUfZfROH8bidJLhjqrPSVVMSeXWNm5GAe1L2CbSitwtwunltP58LTu9YbL2-JlvC3JG1N1BNsthcA1sVJvODp2PYLgTkKGq24w5dJWRbxNHceJ-dAs08Y2aQKnK-QbMSg2kjD_o4AMfWx3wrlkhsGB6IP-oMNnSFqRupm9-sOPPKzmZm4EndCvPN9L6-aHghB-w2sX4YCpN355Iq_QylGgsuHDVpRO-DEtw61usqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇱🇧
درگیری تن به تن نیروهای ارتش اسرائیل با حزب الله در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/news_hut/65227" target="_blank">📅 01:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65226">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f218bec310.mp4?token=jWTytQE000JRxODYygmCPIytM7BgOcLDujMgY9St8qo_ID3WH2wRUsjvM8it9qc68GBywSatEo_B4j30mzlyfZXnbZtdMvfy1A81xJdRsBbe4AuinpHSPtw4Rjau8EyqTSPtMUSJHIRQ1u1mSgQa-Qrznu90b7AzNfDZlsOwTAEi4E_GUNLp5lB8Mc9UZR8evmKBfp6ggZnkygh2x6bKh5_gMjKkwBm7k34FmZ4cEbaakmS8ic86C1_68G8AnLAeU8WISLCugDg6LToeBUirLu8sDgv8mtR1EJTZYApd7lJms4YFhic_VPxCDdzg9oGwst0rBLI2uN2JDrBmjVOeyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f218bec310.mp4?token=jWTytQE000JRxODYygmCPIytM7BgOcLDujMgY9St8qo_ID3WH2wRUsjvM8it9qc68GBywSatEo_B4j30mzlyfZXnbZtdMvfy1A81xJdRsBbe4AuinpHSPtw4Rjau8EyqTSPtMUSJHIRQ1u1mSgQa-Qrznu90b7AzNfDZlsOwTAEi4E_GUNLp5lB8Mc9UZR8evmKBfp6ggZnkygh2x6bKh5_gMjKkwBm7k34FmZ4cEbaakmS8ic86C1_68G8AnLAeU8WISLCugDg6LToeBUirLu8sDgv8mtR1EJTZYApd7lJms4YFhic_VPxCDdzg9oGwst0rBLI2uN2JDrBmjVOeyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
وضعیت عجیب جنوب لبنان پس از حملات امشب و امروز اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/news_hut/65226" target="_blank">📅 01:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65225">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-poll">
<h4>📊 اخبار جام جهانیو پوشش بدیم</h4>
<ul>
<li>✓ 👍</li>
<li>✓ 👎</li>
</ul>
</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/news_hut/65225" target="_blank">📅 01:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65224">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">رئیس‌جمهور ایالات متحده آمریکا یک «تماس بسیار خوب با حزب‌الله» داشت، که یک FTO (سازمان تروریستی خارجی) تعیین شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/news_hut/65224" target="_blank">📅 22:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65221">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxC9G-deU28P-QZNZvjQ0wWS8Hu7Ol18AcG2iwrOQrV3N54wVy9JpHFcrvfwv97y_hY04yY88RusLoitQhOuUElGn2FoNidyHqDua3wb3c47DJZzcivDL9grukp2m7SI8_utotSDbskR4Vj2kjVNUsz8MriKlIvXoPvLlWoPHhywgNwcokRlADZ9JZPyEl8XCO2ZaKgSW7d1_w8EML68-oIKinDZor5R5IPwr-GBQD-bYaR4jElhfGZ_0zK2znewPuK1ZsuDss49UzzCgwv3sGbYPTUXMof7XHX0U1PJ1RR6kIdTbDhessdxXFsBZcxIvNEj6l9avHITT_9dhRvpfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: گفتگوها با جمهوری اسلامی (ایران!) با سرعتی بالا در حال جریان است. از توجه شما به این موضوع سپاسگزارم! رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/65221" target="_blank">📅 21:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65220">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Dzk0xUE2z1IRI3gaO4EnoJDWhQE068LrO_81ZivEI2srTMLOT7oub2gk5NZvWjdYDUS5k9qSnV29993ukSgj3iRptCmgiEQaGYtaBR4L20FoNuRPneUsU8jJxHXErXXDzrBSBeZhMPHVPWyDeo3tTxi7vVNDQnjbu3xptvCKiWgnuCBjWjdhxWtOWWjbVrbplLV3ND0RFcL-a_TqiIUZu_TVKK-n4GPAbFE07B6HxgSaUN1uTQOoAkN6OCJoE_EWzLqkjFyw-Dkp8GyaEKdd2sJR6urlcF2kSXtSwtmQKtt3TdS6BZ_MaSEQ5KL9NGuvlj7D_EJXa2cZA0jsU8ctRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
#فووری
؛ ترامپ: با نتانیاهو صحبت کردم و دو طرف قرار شد به حملات خاتمه دهند و آتش‌بس را اجرا کنند!
@News_Hut</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/65220" target="_blank">📅 21:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65217">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTdoHzn_1wWCWfp25xJ5R-eBUVqhMqHO9rL0lYVHogGMgwcuodNEi6FFNAGELFSzNK5Q8RXvZe6QHCbVCuHSX4gW59JbWjXISLG5hJz-E53kEMJshJgSXVLNKxhwxBqjzjCscovfPeuWjtLa-od5FC1nUUkc2i_dyqO9gQ0JWYKX2DxcqFs9uR1q-80h0PGJusyyz25DXZL1nWTO9X9UPCLcnejL33GVFUo7yA0h5TLxlusxUjJovk3Z9mO7PMhjHAAIS0MtCNJRKxb1O15-XP8aVMny1FUZdpNz4eUleBW0JbTGvlvQKVX4hOKKEfdEJMvqyjL6-OjELfCpp0GpjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ایزدخواه، نماینده‌ی مجلس: آخرش که قرار است فلسطین اشغالی را بصورت زمینی آزاد کنیم؛ چرا همین الان تمرین آن را از امارات شروع نکنیم‌؟!
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65217" target="_blank">📅 21:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65214">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
📰
مصاحبه NBCNEWS در گفتگو با ترامپ درباره تعلیق مذاکرات:  فکر می‌کنم ما زیاد صحبت کرده‌ایم، سکوت کردن خیلی خوب خواهد بود. سکوت به این معنا نیست که ما شروع به بمباران کنیم، ما محاصره را ادامه می‌دهیم. محاصره یک تکه فولاد است. فکر می‌کنم تا هر زمانی که آن‌ها…</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65214" target="_blank">📅 20:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65213">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇺🇸
سنتکام: دیشب ساعت ۱۱ شب به وقت شرقی(۶ صبح به‌وقت ایران)، نیروهای آمریکایی با موفقیت دو موشک بالستیک ایرانی را که به نیروهای آمریکایی مستقر در کویت هدف گرفته شده بودند، رهگیری کردند. این موشک‌ها بلافاصله منهدم شدند و هیچ یک از پرسنل آمریکایی آسیبی ندیدند.…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/65213" target="_blank">📅 18:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65212">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ip_9sw99VuKOLGHw29aPXa7nK0DZYWB-ItyCeDFhimqq1Qom7iCfYWLnXgR_hmcJ9KKShO5AFJR94thgjdEn9MYK9vNetQaCDXPpDHFuzGVK9pANwmw0MBVGHroL55F1z2ttrcBofG98_Loaq66dN2wXCMUvwH_9m-z98cWAG1CsjGKvPPjHqmN6B4iDvRGp4Aux-6CH1IrDGv0bxlQMnY67e87O-psPj_bo8hlu-uKkkqXGGJiu-v2fN0I6QLeHinf0o2cfLeaXp7zJlA8mrRx4do_Uk7QnQX1WTflZ6Bojq7Kgov1oRnpBdD1maUEzYU3ItNkyI8mpARqHSQMfEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام: دیشب ساعت ۱۱ شب به وقت شرقی(۶ صبح به‌وقت ایران)، نیروهای آمریکایی با موفقیت دو موشک بالستیک ایرانی را که به نیروهای آمریکایی مستقر در کویت هدف گرفته شده بودند، رهگیری کردند. این موشک‌ها بلافاصله منهدم شدند و هیچ یک از پرسنل آمریکایی آسیبی ندیدند.
فرماندهی مرکزی آمریکا هوشیار باقی می‌ماند و به حمایت از آتش‌بس جاری ادامه خواهد داد و در عین حال از نیروهای خود در برابر تجاوزات ایران محافظت خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/65212" target="_blank">📅 18:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65211">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbqNKRoEtIp9ZuBKd8lXpsXQz_c7wW4skJYiiPlfIwXpt7diZPmMRSCjd-2dv-wpOB2yuXLLb8ItxNR74-GqiH6RrB-7zIUsjflOb8_20gIzi0CTslzGGzHPDDTTYzNpLhqi4btjmEs5Bck_sPdKPw06j5w_GWHzbCfdwQJdGXDL7yNLYM_UklFvNbwGN3fUopvYDISyt1WVmnoo_XCUiPnLBWmqAJ7ky58HIOKE1hYPQV_DT77fRBtsFNYZjQUatwMZiNTh_eXh4BlzPaLKr2eZQqtuFg4HlCx-k4fNxEf4tqMDIjIQfsLdTsJTmZgEfvrk1370AVfKBpwAqCXcYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیرنویس فوری شبکه‌ی خبر به نقل از سخنگو نیروهای مسلح: تداوم حملات اسرائیل به لبنان قابل تحمل نخواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65211" target="_blank">📅 17:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65210">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-KikcWn1TDGQAu6RTyoau6YbKK3ETE3rWN1nszbFOHmqE6L_9PS0WBIIhGApcwO0wM6OmxdYPSB4dP2WEJvWaUN_mgoHY-qBS4rf94d0dFCbifiKNWFs0dpLEJG1abLFeHdvXm0ZY4T0KvW7pJ8QJRxN1Eqes7y8s89h-S4l8DprcIwZHJIviecXUSRuxXn_wdKxeGSe4VsVMaTFBoZlCJV6ZqkxIqGwjJqjbwTgFeahv2yXmSgRN-GCnY1KURpLXIdU5qMt_PItImuKAMH3W9plIqQj40h8pP1yAtj-_W20UkzUxhIBmrGexiqmIRx7Gvj6mODmQNRY2eo5dRtpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تهدید امریکا توسط باقر قالیباف: محاصره دریایی و تشدید جنایات جنگی در لبنان، گواه عدم پایبندی واشنگتن به آتش بس است و هر گزینه ای بهایی دارد که پرداخت خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/65210" target="_blank">📅 16:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65209">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTAm9Yivr-mb2ijZWD4B_GrXn9jx7w_d26n4uBBZrFOviilNrV-qLCM09dob0zmM7HC5EWSH381u-3tlFru001ohnCHOP-q0uWecD6gykSo0bXhWB8dzwxsw_23iDkNVCEQZ4BOMUmwk7rBKd_wUw8pC_hOv7xH31LXaEE6lNS5RGfB2YfGWmntXU4LzkWN-zvLiVq3KIhjqOkaytTDplR2CxsNHXGjylQ1DJ1tUTcr7Ick8VzIqKCkvRQr8-yVq-D3RGQWOIgRJ0kDtGfkIyKfPg8bvosN000cpKgk3RrKQfAqUPFM-a8BhfldLy3nxw4sR00JXAevlFo77m13muw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی، صبح امروز و همزمان با اذان صبح، مهرداد محمدی‌نیا و اشکان مالکی از معترضان دستگیر شده دی‌ماه رو اعدام کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65209" target="_blank">📅 14:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65208">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGQzleOpNKIn8W_4vqdB51EfTyamNCViZBRp7k7JKnW55MRGcW9gN0WBHkcfAoix5I7HeG6k9tzqwdntjif84CIKTlAstW4HQo14NX_WoQ34I8qjAqvu-1NGZE_NCekENZvwakHTRLmrSIQcn7ut_h9GqHC0hkvxb1oYCezv3kDb34J2UeXwVZ5l1gDp9eLf4TvV7zVQU4fhRMVrJQBfRXHdoLRfReaNL1dMSc-bEsujFVoDE7IbQhLKnJ_GyD4rDYDX0giN1lVsCxHG3bqbifN1-YRX7_HB_19snPbc0izo9xxyohgxG4firlqd3bTJcMerXOqQTnvCHGSMnco15Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBoR9qUuRgdPI_q3_T3G2A9XP2DqQOqOynMExuppTzUVWfzwOolzkLs023F2Y_HXyIK8ankC_lKwKvCLf2uivV2Z2u8btkXxC77vSL2QjPbTtqNWHYDRVS3SWreOaMp4Je85Bl7I4x-yqETN3_tKHnKISD72ZTFQ2pjmktEZXeARcva8-9TyKyquL8JT1k0cqXVp-RHfYlhomuKZZ7Ev9SVfVas-5LKT7l8h-UmtNzO96yD58Fu-FoY3NC6oHTgaF0m-2tSRHK-43dAKsidHl8RvC210QUqbq01ef13mgGxjywobC2KumRRJacya9Ao8410kHyLz0Z6M9Ypt7AI2kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: ایران واقعاً می‌خواهد به یک توافق برسد، و این توافق برای ایالات متحده آمریکا و کسانی که با ما هستند، توافق خوبی خواهد بود.
اما آیا دموکرات‌ها و جمهوری‌خواهانِ به‌ظاهر میهن‌پرست نمی‌فهمند که وقتی افراد سیاسیِ فرصت‌طلب، به شکلی بی‌سابقه و بارها و بارها به‌طور منفی اظهار نظر می‌کنند و می‌گویند که باید سریع‌تر عمل کنم، یا آهسته‌تر عمل کنم، یا وارد جنگ شوم، یا وارد جنگ نشوم، یا هر چیز دیگری، انجام درست وظیفه‌ام و مذاکره کردن برای من بسیار دشوارتر می‌شود؟
فقط آرام بنشینید و آسوده باشید؛ در نهایت همه‌چیز به‌خوبی پیش خواهد رفت، همیشه همین‌طور می‌شود!
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65206" target="_blank">📅 14:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65205">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🇺🇸
گزارش سنتکام از درگیری‌های دیشب بین‌ امریکا و سپاه در قشم:  در این آخر هفته حملات دفاعی به سایت‌های رادار و فرماندهی و کنترل پهپادهای ایرانی در گوروک، ایران و جزیره قشم انجام داد. این حملات سنجیده و عمدی در روزهای شنبه و یکشنبه در پاسخ به اقدامات تهاجمی…</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/65204" target="_blank">📅 11:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65203">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e4c45b1ee.mp4?token=ZUdNd304xDvMXcFpZ9Asr5kht-vm7JFTW6NtW3i_P9GLP1YofyrGJCLMVroR8th3hFOvK4qI-VKPXUTsR5Ff8CMPFWGMivgX639All3FpICa0Scb4GFzmJPuriUllwqewwalJNMU_WXTJ0j2g-z_klyWo7dJDjT7ZvKqc5dwDk9DIo-TuwCXqCnzX9-iVOh8iTaYEtOnGpgQbfcchTwjiBPPFAQeQWkqC5Whb43I2RP8C-7biqI_v03bcZHv9jlbl97zzm04_WkYH-2P5vowpkHhESyj5lU601AT9mw6TmuxyI2nUP6b_oQ-PrU3sR3FAkwkhiPk2eQxqcXODS1ufQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e4c45b1ee.mp4?token=ZUdNd304xDvMXcFpZ9Asr5kht-vm7JFTW6NtW3i_P9GLP1YofyrGJCLMVroR8th3hFOvK4qI-VKPXUTsR5Ff8CMPFWGMivgX639All3FpICa0Scb4GFzmJPuriUllwqewwalJNMU_WXTJ0j2g-z_klyWo7dJDjT7ZvKqc5dwDk9DIo-TuwCXqCnzX9-iVOh8iTaYEtOnGpgQbfcchTwjiBPPFAQeQWkqC5Whb43I2RP8C-7biqI_v03bcZHv9jlbl97zzm04_WkYH-2P5vowpkHhESyj5lU601AT9mw6TmuxyI2nUP6b_oQ-PrU3sR3FAkwkhiPk2eQxqcXODS1ufQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواد ظریف در پاسخ به سؤال میگن شما پشت پرده مذاکرات هستید، گفت:
من اصلا هیچکارم
@News_Hut</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/65203" target="_blank">📅 10:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65199">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">بر اساس تحلیل تصاویر ماهواره‌ای CNN، ایران ۵۰ ورودی از ۶۹ تونل موشکی زیرزمینی هدف‌گرفته‌شده توسط آمریکا و اسرائیل را دوباره بازگشایی کرده است؛ در ۱۸ سایت زیرزمینی، عملیات خاک‌برداری و پاکسازی برای بازگرداندن دسترسی دیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/65199" target="_blank">📅 23:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65197">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0RiF7uLGbzwhQYY9OUpBr2QEcJV5G9Os2VBZ2i3Mpz3LBf7ZCMlvYR4FFWatb6Ubz2vl12ySX-UonpBN2qM08Ng7FoGciRvQCc_hu1jKpGfrbmqVlxmaz62EhA1jatedCoRI19ZBatZ4udrKrM8hchF-9-3EuC4JSFzdku6pju_3EkOgLupNkNG6ttzSaV39Cvj1ZNsi6FinNSlCAb1wraFi3K5MP518AH7tnT2eH-kL9SUdO8Tkirdi8g1AX7XlXzqUIyLkD1b8ONYGuDyO0MiVZCq0qyudGggRGagoSotSUYFy77lSvkN_Xwlz7mcWUUTAuEQ5KRCWIASDq0DnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طباطبایی، معاون پزشکیان: رئیس‌جمهور ‎از خدمت به مردم عقب نخواهد نشست
@News_Hut</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/65197" target="_blank">📅 23:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65195">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">طبق گزارش The Jerusalem Post، ایران ادعا می‌کند پس از بیرون کشیدن/مرمت تونل‌هایی که در جریان حملات آسیب دیده بودند، آمادگی شلیک موشک‌ها در سطح منطقه را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/65195" target="_blank">📅 22:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65191">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
📰
#مهم؛ ایران اینترنشنال: پزشکیان از سمت ریاست جمهوری استعفا داد  @News_Hut</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/news_hut/65191" target="_blank">📅 21:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65190">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gL8D3qERZQimV_5k_K6k-ap3NtjezTT5-DnEZQe5zO5rRHXmquEBA2QRJcmg43YBRCNfXmP5aSr-0ar2ggftzu01tnkzyVWf4-zsocnoNx1VtIW2cVOMUOHSkUbuGCzRDaWBglwKzPOXA4pKm-wJ25HAqYWShMoFsug42qvivgd5_TbPBSACmOi7lLiXYt2X1bi9DUgr5AkXRWsuWkmin5fBxtwAP-8adzPAx7sFsebYbG5ottdOBWXtenL2AvrQZeDUQHIY0v0XhWU9KaFTs5zNjhHBQDCdeouYLpHQAVSr6GMqGPu_ABIZJF6GCQFRr-EO2peBvX_a81cKTdZ2RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
#مهم
؛ ایران اینترنشنال: پزشکیان از سمت ریاست جمهوری استعفا داد
@News_Hut</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/news_hut/65190" target="_blank">📅 21:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65186">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RT71Zqp-RjZasFaAUEiBaSYhCOifrDt6FFo_VmUBemDf2euKw9ioSsvzIckdnV1XcmYuwAwfDBmPg0YCG1rINjBAFFqs7AZAdkD9W76lPzTh1aqloidhkcumvtn-oy49bF-OAuSbTS-BJhqOZSbOXw7mE0Dodv_R2VG9JeAnz9IKB9ctvVDWwl6VPEf0dXz4tJzUIA3lzuCZJrSnJaq8fNo7z077XiNct-BRJE-GE6cZ3yKvXAEhQY4HrgH16FuRGFhaJbtb8auduNIr8rswiqUglpPov-CnAhgT3SNrtCinyELXa6OSTn_PbnMHmdv4Tvpcfm308xYE20pZZVbFSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SiY3UPXdf4mfLOt_S0aYXM-9cvHV8EPfPmTnnTodHPt-kQJJ8u-Ckwwu0ZrxPpeTq8NSkscO66aWU2wzcazI5RjXejDJGGrguJNIe7Tgrh2XIaWwy-1YBnkBQBKF53g1Va5PhsLYDtWfcDuqM3004V97mx9pZXtGwz6ptnjPO3V0BziUPyH_ZFFhJOHxQ1PHfYV3W87CSpXfGRjY86cPpd-XzFanczu8zsQIXxcjpm8S6EFNZjPi3H4hZ_dqv9EdfRHPbv_AZ2XlG8BC9Twddw9OnHqgbUcRxq5O14ncdt3CMf12DmB0jEIcLFC7CvwFrHGJgCYVdb3-qhFgJha4xA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a589784b7.mp4?token=AiHI6kwu7gQ1-Rh-rXu5vq5fN0ETKlRZ07RwairRfJQ8JbDQo4oYsQA-4R61ZVFMroN1Efy-G1TVbY3CtOf2tTULPM_RkSpGhaTMLUwH1aBjbRV3eh3WDlLGtlKYnrY2u3PFPa4F0h3Ve5PQ3o9kztjDDq7fiCoVNPPmnglGw9fyqvcPzl7lD9PjQ4BYZWeQ9SAkdrzLVGMY7b2IxDESALKN85JnYAz7Lk0u15wznVQCWDd9xKni_SUJlfpPy9e5uSYQV1ZElAeYU6y6UFyWukRIrtbXA5R4g8GZSF7GgDkwFaXwmfLahcDz87a8ZjS-qecqVCBEYuTSpxVIC77fUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a589784b7.mp4?token=AiHI6kwu7gQ1-Rh-rXu5vq5fN0ETKlRZ07RwairRfJQ8JbDQo4oYsQA-4R61ZVFMroN1Efy-G1TVbY3CtOf2tTULPM_RkSpGhaTMLUwH1aBjbRV3eh3WDlLGtlKYnrY2u3PFPa4F0h3Ve5PQ3o9kztjDDq7fiCoVNPPmnglGw9fyqvcPzl7lD9PjQ4BYZWeQ9SAkdrzLVGMY7b2IxDESALKN85JnYAz7Lk0u15wznVQCWDd9xKni_SUJlfpPy9e5uSYQV1ZElAeYU6y6UFyWukRIrtbXA5R4g8GZSF7GgDkwFaXwmfLahcDz87a8ZjS-qecqVCBEYuTSpxVIC77fUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
اسرائیل رسما داره حزب الله رو تو جنوب لبنان به شکل خایه‌فنگ‌طوری با خاک و خون یکی میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/news_hut/65186" target="_blank">📅 18:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65185">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cc5kNPVVapOqpWo1b-dtfveTPKbxFy49bu-AIku3gr585bNiKeDJzcqgRGkwnVfgwBEclxd8EXIZfB57zh_w1cKHzkDJ2xhvHwXL0qmlUZkM13JesVIGp63XlWvlVgOLpeLI8IkQbs7ZQDPmD0sZs-CLypq3wXa6ED4L5zUgyreEYPfhtNWr7i0vIdyC0-x8O7bWARpIFsflugMKJnb7mDXr7hixKMLlI1Nj6OnkahTsAekI6pOwm_XVVW3L0e3pcPMw-1Q3-5p3eCIXdPh47r0sH5Q5rdclDNSHYpef0982PC5NoJhUxrINwhlelNYrGv4Ly0KKmotyO6zGY9uqqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست قیمت جدید خودرو های مدیران خودرو با ۸۵ تا ۱۰۰ درصد افزایش قیمت
@News_Hut</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/news_hut/65185" target="_blank">📅 15:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65184">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
گزارش شنیده شدن صدای توافق‌های عمل نکرده در جزیره قشم
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/65184" target="_blank">📅 14:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65183">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec47112ddd.mp4?token=DcavQXHd6OUyQEj663L2wfrwc2j_ufpnNHg_8vncBK7NJLXX3Rw8k9HDHy2OJ2Vh_A49BE0izmrZxgjsP3jXc2GysnG6HtrGg37al73nT1kuIGDvMSyvqw634OhOybrI1tu6VzuoH8vUbLZML8YFXDq4Qzv4M6oXWbfheyt4E6NECjv0cwGakrmc2kZOE6-76ZJMunqR3e_uHWpULGa3sxCtPvayH5ozCfogbDz0k72xaTroBI4q2Kvq-jzSik-PPBcYnnFKFJ15ZDOgxWxrJ5BCwId9tFco0oX5tTFjvmRY2h6lxzCA1KeRiI-6Dc5S9tlRsHnQ3Rb4CwyKaUWjuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec47112ddd.mp4?token=DcavQXHd6OUyQEj663L2wfrwc2j_ufpnNHg_8vncBK7NJLXX3Rw8k9HDHy2OJ2Vh_A49BE0izmrZxgjsP3jXc2GysnG6HtrGg37al73nT1kuIGDvMSyvqw634OhOybrI1tu6VzuoH8vUbLZML8YFXDq4Qzv4M6oXWbfheyt4E6NECjv0cwGakrmc2kZOE6-76ZJMunqR3e_uHWpULGa3sxCtPvayH5ozCfogbDz0k72xaTroBI4q2Kvq-jzSik-PPBcYnnFKFJ15ZDOgxWxrJ5BCwId9tFco0oX5tTFjvmRY2h6lxzCA1KeRiI-6Dc5S9tlRsHnQ3Rb4CwyKaUWjuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: بزرگ‌ترین سرمایه ایران، «رسانه‌های فیک‌نیوز» هستن که مدام موفقیت‌های آمریکا رو کوچک جلوه میدن
شما یه پیروزی بزرگ توی یه نبرد به دست میارید
ولی اونا میگن شکست خوردید! این واقعاً چیز بدیه برای کشور ما
@News_Hut</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/news_hut/65183" target="_blank">📅 14:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65182">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7-oJOSpKp3fty92f4BsxiOmwYMtfvnaheLVWW6JjMoX3dQNylarxTExVm9LtGHluPJlZS-jSYimt2AZC5y-AW19wqQrQ3Xgru_sS8Axs8h9745B5Q385WVL4q1Q_oJ7aHVWrCunxPUVf2aa6uM9SdeZ0cuhVBfD0qtR3z_TIi7Ev_mWwUBXQkJ80Ul8-W0pU1gvH06_GREYVb1sTNjo3vyfDBqd1PRROzuvJMNQY8BvXILMA4CWvSHT0JG5v0AIE_Dt265jAfS9vrD8EfQkEn77k0UleJMyLLw_KMjPJtGtquBGCMraKXM9cf0BWh8leB6URzYXZRY4_2licK0IYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تردد خودروهای پلاک مناطق آزاد  تا اطلاع ثانوی تو سراسر کشور مجاز شد
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/65182" target="_blank">📅 12:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65179">
<div class="tg-post-header">📌 پیام #1</div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
