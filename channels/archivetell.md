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
<img src="https://cdn4.telesco.pe/file/UnraAnSI4fdrAqu5YerVvaa1cj2GbqgoTA6bcmTwAHkhHUHGz55LnsvU7XBRmn2WjbOvYMj1tBDGaCp6-Gkda5Tzw9E7C8MJSRj1gNjDUY8_lCAgMPYKk4oocyNPP77YbWaPCzmKOngA34-wB0IGIdDmk5UTOqb-Um53E1cdBclExqCucjoYaHG98SABoqH1pIVOMJBIwhVsvu6o3Lz3EnzZcG70715bVwKAGXMqDaUVKBalnddVA42Au8gBCzMuwnx916tNz3XXMATZrqsfZ9VL-_6MqyS8Sa78AtMPwGtRH_jHd7Z0RMElLyoF4sV7eVZucHJ7kfGVTSehM4vG8w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.44K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 00:13:13</div>
<hr>

<div class="tg-post" id="msg-6145">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اگه نمیزنید ما بریم بخوابیم</div>
<div class="tg-footer">👁️ 791 · <a href="https://t.me/archivetell/6145" target="_blank">📅 23:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6144">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">Fasten your seat-belts
Pack your Backpack
🗿
😂</div>
<div class="tg-footer">👁️ 933 · <a href="https://t.me/archivetell/6144" target="_blank">📅 23:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6142">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">185.226.117.8.txt</div>
  <div class="tg-doc-extra">38.3 KB</div>
</div>
<a href="https://t.me/archivetell/6142" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ریزالور</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/archivetell/6142" target="_blank">📅 23:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6141">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.5.1-universal.apk</div>
  <div class="tg-doc-extra">16.9 MB</div>
</div>
<a href="https://t.me/archivetell/6141" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/archivetell/6141" target="_blank">📅 23:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6140">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ریزالور
95.80.164.6
84.241.3.33
185.179.170.127
188.136.174.86
46.143.244.4
46.100.46.8
46.32.4.164
62.60.167.216
185.128.138.250
185.128.138.249
188.121.129.238
93.115.151.185
10.233.249.52
217.170.242.11
185.57.135.72
2.180.21.144
213.176.4.6
93.118.162.116
5.160.162.44
77.238.123.238
216.147.121.66
176.59.222.24
216.147.121.152
95.217.210.65
176.59.31.187
178.252.180.62
176.59.31.198
176.59.222.28
176.59.31.195
176.59.31.197
81.168.119.130
216.147.121.105
176.59.222.30
176.59.222.31
176.59.31.191
176.59.31.192
176.59.222.27
176.59.31.194
176.59.222.25
176.59.31.189
176.59.222.29
176.59.31.186
176.59.31.188
176.59.31.184
176.59.31.196
176.59.222.26
176.59.31.193
176.59.62.14
176.59.31.190
176.59.31.199
https://t.me/archivetell</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/archivetell/6140" target="_blank">📅 23:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6139">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ربات تست ۱۰۰ مگ فقط با ۴۰۰ تا رفرال بزن رو لینک</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/archivetell/6139" target="_blank">📅 23:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6137">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/279755f66a.mp4?token=WkhcwKLbq3oLHQ9RnInQkRqkBLyl-xtPZRmRbPkPGjJZIu20NJx7UvlCLgDMlrofTer7ZbFsxoNODK-0c7s28YHkqk7wGVlvXat8i5IDp8a4SLXD20U1G_Mw69uw0Qf3eWYWVf04iKRuOfzoUuJVo7MaemfsJm4iGrXpzeeqI-FQCe7SrFu82ix3MyyLadcDnPf70rLobsRW6AqqCG1NAxWmbOjhfiqpBCbXjx_GVd4aFQSdPebpxuHxTRWAiP7XEeCREOUjyGhZN8Lx4WFkQ_lUqDOSwgmnD8eeWwUXUE8N1wPJCScwU5Q3QcmLUILB25aV2P2tI3fuqGx8hkiGWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/279755f66a.mp4?token=WkhcwKLbq3oLHQ9RnInQkRqkBLyl-xtPZRmRbPkPGjJZIu20NJx7UvlCLgDMlrofTer7ZbFsxoNODK-0c7s28YHkqk7wGVlvXat8i5IDp8a4SLXD20U1G_Mw69uw0Qf3eWYWVf04iKRuOfzoUuJVo7MaemfsJm4iGrXpzeeqI-FQCe7SrFu82ix3MyyLadcDnPf70rLobsRW6AqqCG1NAxWmbOjhfiqpBCbXjx_GVd4aFQSdPebpxuHxTRWAiP7XEeCREOUjyGhZN8Lx4WFkQ_lUqDOSwgmnD8eeWwUXUE8N1wPJCScwU5Q3QcmLUILB25aV2P2tI3fuqGx8hkiGWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/archivetell/6137" target="_blank">📅 22:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6136">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">۵۰ گیگ کانفیگ اهدایی
🔥
vless://8879af15-f3de-4ff8-a4dd-e9ee7f33477f@v2speed.solarmg.ir:8443?type=ws&encryption=none&path=%2Fdownload.php&host=v2speed.solarmg.ir&security=tls&fp=chrome&alpn=h2%2Chttp%2F1.1&sni=v2speed.solarmg.ir#ARCHIV%20TEL%E2%9D%A4%EF%B8%8F%E2%80%8D%F0%9F%94%A5
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/archivetell/6136" target="_blank">📅 22:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6135">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">خب دیگه دوران صد گیگ هدیه به پایان رسید
از الان یک گیگ هم غنیمته</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/archivetell/6135" target="_blank">📅 22:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6134">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6df24a7408.mp4?token=GqqMQ6RQ4pQA278b0teZKSOt725MblJm2CrOPyWVgxMjdY3C9UWQiuYlY1vUxEhrUlCi7bS3Noih6Gf3N-R7jCn4ZNae4iF5eB6ePjb6j9anXb6zBV9iy3Gj8HSJ4ESwQwA3RrPaJHrn9Bx5J647_iBWvyGi9E-EmI1Oaek5Lb9HPRXq2UtWzVbLISm46VwlAjLvSmKqAUghEC0n_FH5iQndNSPsZToLVBsbE9noQ_JdClknTvQ8MlUJgkRDOWciAhDG_XbP7f5-a2eWXunm2KTx03dvnnQxSULrgzBzmcxKrISu66KV9Rokr8d6BFjw_6nI4JgFXTUFPMml4cncMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6df24a7408.mp4?token=GqqMQ6RQ4pQA278b0teZKSOt725MblJm2CrOPyWVgxMjdY3C9UWQiuYlY1vUxEhrUlCi7bS3Noih6Gf3N-R7jCn4ZNae4iF5eB6ePjb6j9anXb6zBV9iy3Gj8HSJ4ESwQwA3RrPaJHrn9Bx5J647_iBWvyGi9E-EmI1Oaek5Lb9HPRXq2UtWzVbLISm46VwlAjLvSmKqAUghEC0n_FH5iQndNSPsZToLVBsbE9noQ_JdClknTvQ8MlUJgkRDOWciAhDG_XbP7f5-a2eWXunm2KTx03dvnnQxSULrgzBzmcxKrISu66KV9Rokr8d6BFjw_6nI4JgFXTUFPMml4cncMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/archivetell/6134" target="_blank">📅 22:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6133">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/043de26847.mp4?token=HPNdyKGU5eaTgzAOoDlJ3tYVu82fo_EYstISY38sbECBS14AE3W1yghUWPlAiQ6OVucO0zeZ0k2HClkc6hvkdDxYNoJiiKvyOJre-aCrxogLd4ZP0Bia5dGhYstwMc4Wqb1FxOtfOus6QpCUsFl0_lz7ikJrrKA-joeTNZBrlRnTkw9Ykd-4dzQJ-HH4x2r731xEAyHosinirJ7qG8vLVTGhiyEu7MyIf3_qmNFOfjfm8R78desAZKyFOYZygJUjawciSAbhpmuEVFIYiNZxIL6ZwGhXw5PIsYiNaGiznXmnYny6WyTRZsTdg4VfGRHVFI4CmOGIiTJ7sKHDyAtaBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/043de26847.mp4?token=HPNdyKGU5eaTgzAOoDlJ3tYVu82fo_EYstISY38sbECBS14AE3W1yghUWPlAiQ6OVucO0zeZ0k2HClkc6hvkdDxYNoJiiKvyOJre-aCrxogLd4ZP0Bia5dGhYstwMc4Wqb1FxOtfOus6QpCUsFl0_lz7ikJrrKA-joeTNZBrlRnTkw9Ykd-4dzQJ-HH4x2r731xEAyHosinirJ7qG8vLVTGhiyEu7MyIf3_qmNFOfjfm8R78desAZKyFOYZygJUjawciSAbhpmuEVFIYiNZxIL6ZwGhXw5PIsYiNaGiznXmnYny6WyTRZsTdg4VfGRHVFI4CmOGIiTJ7sKHDyAtaBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/archivetell/6133" target="_blank">📅 22:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6132">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">.</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/archivetell/6132" target="_blank">📅 22:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6131">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">از اونجایی که بو درگیری میاد نصب کنید
😂</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/archivetell/6131" target="_blank">📅 22:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6130">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">حال کردید
😂
😂
😂</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/archivetell/6130" target="_blank">📅 22:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6128">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">از اونجایی که بو درگیری میاد نصب کنید
😂</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/archivetell/6128" target="_blank">📅 22:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6120">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSlipNet</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SlipNet-v2.5.5-full-release-arm64-v8a.apk</div>
  <div class="tg-doc-extra">25.7 MB</div>
</div>
<a href="https://t.me/archivetell/6120" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🕊
@SlipNet_app</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/archivetell/6120" target="_blank">📅 22:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6118">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">تا کمپین اوکی بشه این ۱۰۰ گیگ رو فعلا داشته باشید
پر سرعت
🔥
🔥
vless://58e82e36-32e4-4368-8742-f51446c3fd28@45.130.125.66:443?mode=auto&path=%2F476T682e67a4f84a3c838ca94R86273&security=tls&alpn=h2&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%2210-50%22%2C%22xPaddingHeader%22%3A%22apinode%22%2C%22xPaddingKey%22%3A%22domow%22%2C%22xPaddingObfsMode%22%3Atrue%7D&insecure=0&host=ticket.fibernet1.qzz.io&fp=chrome&type=xhttp&allowInsecure=0#%40ArchiveTell%20100.00GB%F0%9F%93%8A%E2%8F%B3
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/archivetell/6118" target="_blank">📅 22:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6117">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دوستان ببخشید کمپین جدید مشکل داره از سمت ربات
اوکی شد میذاریم
سرعتش عالیه شرمنده
❤️‍🔥
تا ی ساعت دیگ اوکیه</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/archivetell/6117" target="_blank">📅 21:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6115">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">کانفیگ مخصوص کلاینت happ
زمان : 60 روز
حجم : ۱ ترابات
لینک دانلود
Google play :
https://play.google.com/store/apps/details?id=com.happproxy
Github :
https://github.com/Happ-proxy/happ-android/releases/tag/3.22.1
happ://crypt4/vfb1onL0njkmd47DHXNPUKKEEPQNrpfahCf5vmgczvqBX6IcP0JkObKmWDw+hAZ2VwZ21pi6REi4WyyLXGQxIbppw+LrTNA2hI/+0Mv4HBgFZV3AEzeh1kgwD0yr9nppZJsSGofePhJLN2CcRV095i4udLU52HxgvaCcMSlW+MxM5BQyQycn0iznnAt+/d3fjhtJbMsGGPwC3VAK25ERXDg4IQVlPdk1K7QOfMqddVfnbPKHx6cYrLbYlh0jQS1ya2pgxEDHAHnKBapy6ldkGRojSL5NkZ0hDNhagnbvlB6EG+7WXfXLGBG4HTDv18z8kKwMcd8SqxlQs7xoZnsmUaMDLdiy7WLZ1feY8Z0upkOTj72B1Iwj1TIShiG1ZNyvKn9pPLCrNhntsChX3ckLrAMCI8U3iIRjoTgfW3WftxxTLfTN45xFAYGkektT1C1z/v1Bs+E5FZujJdzi/rCA+RoFpO8p7CvIbbCizV+dYY5deDml/Y0aBtTcy5J/Haukal2Wsx3Rrhcb8V1+L9FM6PfN0aKuZyzZ6cEZ2BCJTSEG4CAv0PSOwqQHts5lpfRLDdE6M5em9jkYuS5sdwxU2PULK4QDUn2a4LmkW5NMWQq/QOYuNTaiPsN1QqLKsTi0eXaGC9sJNHRLFOXahzwCgnKKr+ios8lIK98MoQ0KoUU=
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/archivetell/6115" target="_blank">📅 21:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6113">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIcR5nbpQXMJhs21LOOgztrr5aF6uGVJ7TrZGTQzxZQpJSY901K2YRsB6BYaIzo9Li8b_aejp3pklnZsWUrRAVwIEXXtDBv2qBWxxgJn4Dy45V9YTz7Cu2v8hst5lPrFUDeAh_6EaJK86W274LuaSo7WVCBj8ZLUOaluNzxbVYNiSGW1d4pwebPg4WsQcbYahKu_ptM4bPQ-E2xO4nBHaK4SW9Ccuc1n5MKrCxCsj-cnieQ_NKLrv0J3bFncMILRhh3oDwF-YJCf_IQlACmf_95g8aUTzlCZzvD9_htp3ynppBFkDjb5YhMI0zzSXX7DiPz7xFgFPzrE_IuPZ2gZlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
✨
دریافت 10,000 اعتبار رایگان Figma AI
اگر از Figma استفاده می‌کنید، با این روش می‌توانید 10 هزار Credit رایگان برای ابزارهای هوش مصنوعی Figma Make دریافت کنید.
🚀
💡
کافی است وارد لینک زیر شوید و Team موردنظر خود را انتخاب کنید:
🔗
https://figma.bot/4o7EDMQ
🎯
مناسب برای:
ساخت رابط کاربری با AI
• تولید Prototype
• طراحی سریع صفحات
• استفاده از Figma Make
#Figma
#AI
#Design
#UIUX
#Freebie
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️
کپی پیست آزاد برای چنل عصر نوین فقط
😐
😂
🙋‍♀</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/archivetell/6113" target="_blank">📅 20:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6112">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🤔
آیا گوگل هنوز برگ برنده‌هایش را رو نکرده؟
با نگاه به رقابت اخیر هوش مصنوعی، به نظر می‌رسد گوگل همیشه چند قدم جلوتر آماده ایستاده است. هر بار که یک مدل جدید سر و صدا می‌کند، مدت کوتاهی بعد گوگل نسخه‌ای قدرتمندتر یا فناوری جدیدی معرفی می‌کند.
📸
از Nano Banana گرفته تا Veo و Gemini، بارها دیده‌ایم که گوگل بعد از اوج گرفتن رقبا، مدل‌های جدیدی عرضه کرده که توجه‌ها را دوباره به سمت خود برگردانده‌اند.
💡
نکته مهم اینجاست که کیفیت خروجی فقط به مدل بستگی ندارد؛ مهارت در نوشتن پرامپت هم نقش بزرگی دارد. بسیاری از کاربران از قابلیت‌های واقعی مدل‌ها استفاده نمی‌کنند و بعد عملکرد آن‌ها را ضعیف می‌دانند.
🆚
ChatGPT یا Gemini?
• هوش مصنوعیChatGPT در شخصی‌سازی گفتگو و درک سبک صحبت کاربر بسیار قوی است.
• هوش مصنوعی Gemini معمولاً در برخی وظایف فنی و استدلالی عملکرد پایدارتری دارد و کمتر دچار خطا یا «هالوسینیشن» می‌شود.
• هر دو مدل نقاط قوت و ضعف خود را دارند و انتخاب بهترین گزینه به نوع استفاده شما بستگی دارد.
🚀
چیزی که مشخص است، رقابت بین OpenAI، Google، Anthropic و سایر شرکت‌ها با سرعت زیادی ادامه دارد و کاربران در نهایت برنده اصلی این رقابت هستند.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/archivetell/6112" target="_blank">📅 19:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6111">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba62c4ab7.mp4?token=uoRh5t3RRyB6OLXTidKmIOiG_trAOIW6MA3sPmFqp1PJ16E3e-pOjenlykgBFmQR48iRhipspDNk4yqEn0A-dEfy1_l6hpi3Kzu4dPNx0tZjc9lb9u2LMCY5rdo6AveCbwJc3Fbaqq7OKudsys2DOLfxAB_ElYgZTQiO5-ULZdSO3VTeiQDUGk7d9JKAkvAXRDGsYgNPHiQPgePaZm9-A4TwBWiwnlC21J7zErHWSBIm3sXNeHvIcibKnHYNoEbZDaMKCT9x0Dp-V4KldZPQgMjSH7SoqxbX3fdIU3fGHV24R50jMgddcW-HsfEE_ZktQsPL8u7hdl2LEuRXUWURIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba62c4ab7.mp4?token=uoRh5t3RRyB6OLXTidKmIOiG_trAOIW6MA3sPmFqp1PJ16E3e-pOjenlykgBFmQR48iRhipspDNk4yqEn0A-dEfy1_l6hpi3Kzu4dPNx0tZjc9lb9u2LMCY5rdo6AveCbwJc3Fbaqq7OKudsys2DOLfxAB_ElYgZTQiO5-ULZdSO3VTeiQDUGk7d9JKAkvAXRDGsYgNPHiQPgePaZm9-A4TwBWiwnlC21J7zErHWSBIm3sXNeHvIcibKnHYNoEbZDaMKCT9x0Dp-V4KldZPQgMjSH7SoqxbX3fdIU3fGHV24R50jMgddcW-HsfEE_ZktQsPL8u7hdl2LEuRXUWURIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🧩
یک نوار بی‌پایان از معماها به جای تیک‌تاک
یه اپلیکیشن جدید اومده که جایگزین اسکرول شبکه‌های اجتماعی با حل معماها میشه. تو این نوار، بازی‌هایی مانند وردل، شطرنج، تتریس، سودوکو، پاسینس و بیش از ۱۵ ژانر دیگر وجود داره که به صورت تصادفی ترکیب میشن و ترکیب‌های منحصربه‌فردی ایجاد میکنن.
میتونید از جریان خبری به چیزی مفید برای مغز تغییر وضعیت دهید.
🔗
https://puzzle.express/
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/archivetell/6111" target="_blank">📅 19:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6110">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c8c59be67.mp4?token=aFrod2uaeTkRzH509WFhT3704oiu8hVE9EArmxTHfnEg1LHztXZhTQNXXz0juNQA1OpoGsWIPE-OKJhbfXgXtvvMZC1GWa8sXrbCyFSrd5eLB8wBmPwcfwKNcDkuuyIcRqNCP1DlzLgp5J6DMZFrRIMIH2H6gEfOMgd3MQ_YgP5K6rFNbyqJ56fgenyuH0UWWmDje_X7rONOSJLIh1gaPhugHSbKqLucgerBJS_QzL0009Mibk-By5yMmHQjW876SOEriM9VVvbCpqchfie-faUH1fOG4A0cjYPQO4wp0lJ3LgaOt34F1BxF5ve5ppiXy8JLQHD_88mQfKJ83THBrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c8c59be67.mp4?token=aFrod2uaeTkRzH509WFhT3704oiu8hVE9EArmxTHfnEg1LHztXZhTQNXXz0juNQA1OpoGsWIPE-OKJhbfXgXtvvMZC1GWa8sXrbCyFSrd5eLB8wBmPwcfwKNcDkuuyIcRqNCP1DlzLgp5J6DMZFrRIMIH2H6gEfOMgd3MQ_YgP5K6rFNbyqJ56fgenyuH0UWWmDje_X7rONOSJLIh1gaPhugHSbKqLucgerBJS_QzL0009Mibk-By5yMmHQjW876SOEriM9VVvbCpqchfie-faUH1fOG4A0cjYPQO4wp0lJ3LgaOt34F1BxF5ve5ppiXy8JLQHD_88mQfKJ83THBrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/archivetell/6110" target="_blank">📅 19:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6109">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔐
دریافت SSL رایگان ۱۵ ساله برای پنل ثنایی با Cloudflare
اگر از پنل ثنایی استفاده می‌کنید، می‌توانید بدون نیاز به Let's Encrypt و تمدیدهای دوره‌ای، یک SSL معتبر ۱۵ ساله برای تمام ساب‌دامین‌های خود دریافت کنید.
⚡️
✨
مزایا:
•
پشتیبانی
از تمام ساب‌دامین‌ها (*.
domain.com
)
• اعتبار ۱۵ ساله
• بدون نیاز به SSH و دستورات لینوکس
• قابل استفاده مستقیم داخل تنظیمات TLS پنل
• سازگار با Cloudflare Full (Strict)
﻿
🛠
مراحل کلی:
1️⃣
در Cloudflare وارد بخش SSL/TLS → Origin Server شوید.
2️⃣
روی Create Certificate بزنید و اعتبار را روی 15 Years قرار دهید.
3️⃣
دو مورد Origin Certificate و Private Key را دریافت کنید.
4️⃣
در تنظیمات TLS اینباند ثنایی، محتوای Certificate و Key را مستقیماً Paste کنید.
5️⃣
در Cloudflare حالت SSL را روی Full (Strict) قرار دهید.
💡
نکته:
این گواهی فقط زمانی کار می‌کند که رکورد DNS شما در Cloudflare روی حالت Proxied (ابر نارنجی) باشد.
🔥
با این روش یک‌بار SSL را تنظیم می‌کنید و تمام ساب‌دامین‌های آینده نیز به‌صورت خودکار تحت پوشش قرار می‌گیرند.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6109" target="_blank">📅 17:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6107">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJ71nePDJG7c2LLi91HrNlU-mkbiI3nBjVkP52WF6P-MQPt7t_6WFfawp41w1SA8fmrvkYu3dKFYmKeOV-kcVmQ8n5uZkR3oTN3uMw3d8662Bz8ui1uL2lnEfyIxQQc8NcxMKUz8Dez-u_y35BCKUHKOrAxkDV6sdGKZAi9WQ_BrCdDnFNttyHBGfT8OP0PyeKSa3k7xkWo8w3Z0ugpyNyg_JyAlf96hYBwyJXPAzxnvzx7YO2p1qM_yZtfL0KMH7N2BxBcKHH69ICMRamldfQoM8qzY-9SI0ahkohu-aHo1Ug-qxWQf4AwRAs-AA90sNEggKdBHbiDCzwoE55-6Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت دامنه رایگان برای پنل ثنایی و ....
قابل ثبت در cloudflare
بدون نیاز به احراز هویت و کارت و ...
فق یک ایمیل و یک حساب github لازمه
https://domain.digitalplat.org
https://www.gname.com/tld-eu-cc.html
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/archivetell/6107" target="_blank">📅 17:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6106">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین: 50GB
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 50 / 50
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/archivetell/6106" target="_blank">📅 17:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6105">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
50GB
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 50 / 50
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/archivetell/6105" target="_blank">📅 16:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6103">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">انقار میگن نقز شده این سری     .</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6103" target="_blank">📅 16:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6102">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">انقار میگن نقز شده این سری
.</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6102" target="_blank">📅 16:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6101">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be2541bf82.mp4?token=NsUFaNUFzIxFF6e1iho68fvnLSBQYaPjMb0_uoqGfxkaac4UZ55I4Ce35D-XM7vFY2MBV73UQiOWB9PaP0qHj9jYh8gThO7ReIxiEHCy59pYph6EjyLk2KqaM_07QJcLKFQyDokkBVESKBYLIdZi8EDOtsW0N30kfeZAmvU80sgZ1gS90WljyDXtnrS551WmtWxUqVtnoGg8O5tAdIHeQW9HRoKO-tHjUwoU3OjSCH79pHKD3hBMO-J7DzTs-8EmA2JgmzjU3yjAuyhm_70q1b9Fp_d_QAib3zMnbXhUqzI-_mwfN9pB0QRRWemalR_rmlF3nlSG4jDVB9r_4rf82Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be2541bf82.mp4?token=NsUFaNUFzIxFF6e1iho68fvnLSBQYaPjMb0_uoqGfxkaac4UZ55I4Ce35D-XM7vFY2MBV73UQiOWB9PaP0qHj9jYh8gThO7ReIxiEHCy59pYph6EjyLk2KqaM_07QJcLKFQyDokkBVESKBYLIdZi8EDOtsW0N30kfeZAmvU80sgZ1gS90WljyDXtnrS551WmtWxUqVtnoGg8O5tAdIHeQW9HRoKO-tHjUwoU3OjSCH79pHKD3hBMO-J7DzTs-8EmA2JgmzjU3yjAuyhm_70q1b9Fp_d_QAib3zMnbXhUqzI-_mwfN9pB0QRRWemalR_rmlF3nlSG4jDVB9r_4rf82Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک جایگزین رایگان برای CapCut — توسعه‌دهندگان نرم‌افزاری منتشر کرده‌اند که تمام ویژگی‌های این ویرایشگر ویدئوی معروف را به‌طور کامل شبیه‌سازی می‌کند.
عملکرد: تقریباً از تمام ابزارهای CapCut، به‌جز برخی از ابزارهای هوش مصنوعی، تقلید می‌کند.
سرعت: بسیار سریع‌تر، روان‌تر و پایدارتر عمل می‌کند.
طراحی: رابط کاربری مینیمالیستی و شهودی.
دسترسی: در همه پلتفرم‌ها موجود است.
Clypra
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6101" target="_blank">📅 15:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6100">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">یوتیوب و اینستا شماهم روی همراه اول و رایتل باز شده؟</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6100" target="_blank">📅 14:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6099">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">💼
🤖
AI Job Search
هوش مصنوعی که برایت دنبال کار می‌گردد!
اگر از فرستادن رزومه‌های تکراری و نوشتن کاورلترهای خسته‌کننده خسته شده‌اید، این ابزار می‌تواند بخش زیادی از کار را به Claude بسپارد.
⚡️
✨
قابلیت‌ها:
🔴
تحلیل آگهی‌های شغلی و بررسی میزان تطابق شما با موقعیت
🔴
شخصی‌سازی رزومه برای هر فرصت شغلی
🔴
تولید خودکار Cover Letter حرفه‌ای
🔴
بررسی و بهینه‌سازی مدارک قبل از ارسال
🔴
مدیریت ساده‌تر فرآیند اپلای برای ده‌ها موقعیت مختلف
﻿
🎯
مناسب برای برنامه‌نویس‌ها، فریلنسرها، دانشجوها و هر کسی که به دنبال فرصت شغلی جدید است.
🔗
GitHub
#AI
#Claude
#Career
#JobSearch
#OpenSource
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6099" target="_blank">📅 14:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6097">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzHwhXaklUxzfDR8oshzSRKPpS3yAJu-9yfOGbnPQy1bNIYpWc2Vb0-aS7bGAi6VMNb7BB9Eo2gP1qdmCxKrCaP_snLAQPknVlwOery-6TiW-hDBXgZQBxvYUjh67MyVgzQG8k73mQPGwYqBPCl6C0AX-GCs081s-SCNW7tsl0zYZrnWgdIeWH4j4xi2jW8aG8N4fF0VdLvnC2-16BnEHMwtItiqC6E8XJa-Ri8qOCaHwFUdqLWf-PFPQ-kwyA3ZJEkPWfLEHLHRy4DzeMXvHoHpAqRIiBCMeg-J8nbo_BQsf7jRyUs58yj0f11M_SwfrUxDkQh-0mbiteMs1w3OxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
🔥
گیم GTA 6 بازار بازی‌ها را به‌هم ریخته!
با نزدیک شدن به انتشار GTA 6 در
۱۹ نوامبر ۲۰۲۶
، بسیاری از ناشران و استودیوها ترجیح داده‌اند بازی‌های بزرگ خود را در ماه‌های دیگر منتشر کنند تا با غول جدید راک‌استار رقابت نکنند.
📅
نتیجه؟
نوامبر امسال تقریباً خالی از عرضه‌های بزرگ شده و بیشتر شرکت‌ها بازی‌هایشان را به سپتامبر، اکتبر یا حتی سال ۲۰۲۷ منتقل کرده‌اند.
🏆
بازی GTA 6 فقط یک بازی نیست؛ بسیاری آن را بزرگ‌ترین لانچ تاریخ صنعت گیم می‌دانند و انتظار می‌رود توجه میلیون‌ها گیمر را به خود جلب کند.
💬
شما هم فکر می‌کنید GTA 6 رکوردهای GTA V را جابه‌جا می‌کند؟
#GTA6
#RockstarGames
#Gaming
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6097" target="_blank">📅 14:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6096">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">نامحدود
🔥
vless://991898b1-426b-4108-9d11-188339714c53@168.100.8.115:443?encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&fp=chrome&host=168.100.8.115&mode=auto&path=%2Flokayb&pbk=ZqgdfgPqBr3zZuk4yw6Rtw5u1ar3pPBYooFil3IKzUw&security=reality&sid=4dc2accf4ae6&sni=www.samsung.com&type=xhttp#@ArchiveTell
https://168.100.8.115:2096/sub/4spf8icnqa5e6si8
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6096" target="_blank">📅 13:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6095">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">50gb-@lxhosein-@archivetell.npvt</div>
  <div class="tg-doc-extra">1.7 KB</div>
</div>
<a href="https://t.me/archivetell/6095" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">حجم : ۵۰ گیگ
زمان : نامحدود
متصل رو همه اپراتور ها
✅
پسورد :
@lxhosein</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6095" target="_blank">📅 13:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6094">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🤖
مدل جدید Huihui بر پایه Gemma 4 منتشر شد
یک مدل 12 میلیارد پارامتری که برای اجرای محلی بهینه شده و روی سیستم‌های معمولی هم قابل اجراست.
⚡️
✨
ویژگی‌ها:
• مبتنی بر Gemma 4 12B
• اجرای محلی بدون نیاز به سرویس ابری
• نیازمند حدود 16 گیگابایت VRAM
• مناسب برای چت، تولید محتوا و کارهای روزمره
• قابل دانلود و استفاده رایگان
📥
دانلود از Hugging Face:
https://huggingface.co/huihui-ai/Huihui-gemma-4-12B-it-abliterated
💡
اگر دنبال یک مدل سبک برای اجرای آفلاین روی کامپیوتر شخصی هستید، ارزش امتحان کردن را دارد.
#AI
#LLM
#Gemma
#OpenSource
🔵
@ArchiveTell
|</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6094" target="_blank">📅 12:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6093">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvc7HPNWkfPmyL7a6ZBNdqkVFykbK5Tjszq-vmljkjfSSqUq_lYwgwTvNsE_b3TGKXQTnuVZrjKiWIERXkQWg0FYz0tGnw3_-6Ib8B9M8U9XJddkMzF4rzotsou5Y1UMvU_EaNK6X9edVSHNLjB2IemHTVT2xpX2eeeefmlczYY2CIxEvGOSSEVGjCdquq5IZEqyKwreyVqI7jeRi1gwvSy6kZSrmMeWtEVvqqd5OC6CcAdJB-ygIfXZsA3wikohcqDSB33iY2aHWil7RqSxBHTr6UOcgLEysG8_volFLr7UKWLSzekqTiB5MayCTIrmrqvmCgXiFzYFc7Cz384fFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
خلاصه کردن ویدئوها و صفحات وب در چند ثانیه
دیگه لازم نیست برای فهمیدن محتوای یک ویدئوی طولانی یا مقاله چند هزار کلمه‌ای وقت زیادی صرف کنید.
⏳
✨
افزونه
Summarize.sh
محتوای صفحات وب، ویدئوهای یوتیوب و حتی پادکست‌ها را به‌صورت خلاصه و قابل‌فهم نمایش می‌دهد.
🔹
خلاصه‌سازی ویدئوهای YouTube
🔹
استخراج نکات کلیدی مقالات
🔹
نمایش خلاصه در پنل کناری مرورگر
🔹
صرفه‌جویی در زمان مطالعه و تماشا
🔹
مناسب برای دانشجوها، پژوهشگران و تولیدکنندگان محتوا
🌐
لینک:
https://summarize.sh/
🚀
ابزاری کاربردی برای زمانی که فقط می‌خواهید اصل مطلب را بدانید.
🔵
@ArchiveTell
|</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6093" target="_blank">📅 12:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6092">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKjh744UDdEMD3xBamJNwjy836w-UJVH7vZsf_qiHlIbZdLqwCot1uHrX69G1Tjh11eSW03UBSZe_hhIMP2jOTBnSeukNjcMAJ2s3Zp7AOjuSZjtHaXO75cJBm6JUTU5WsftWFCmUXyrs3BjrufU_iWRcj3MAqzNNA9sAh_ZrhHVWyTgKpg0GBPibqMeFR1En3kU-trJwNDzj8IMdtzCLnLogY7zHarHPa26hW-LdDhbH4aHGgtw3bpvWHm93wIZ_TkaAcD1L_wGOtiQPK4XGRegfYwXVRfecIofFAFnZJkHU53aOYNfjaOWnh-byfUdv6DdF6RZBTWFetNOvbD3HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
مقالات پولی اکنون رایگان هستند - دیگر لازم نیست برای اشتراک در سایت‌های محدود شده هزینه‌ای بپردازید.
1️⃣
آدرس مقاله محدود شده را کپی کنید و
http://r.jina.ai
را به ابتدای آن اضافه کنید.
2️⃣
تجزیه‌کننده هوش مصنوعی
Reader
تمام متن پنهان را استخراج کرده و آن را به Markdown تبدیل می‌کند.
گیت هاب پروژه :
https://github.com/jina-ai/reader
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6092" target="_blank">📅 12:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6091">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">📚
BooksBunch Bot — کتابخانه‌ای بزرگ داخل تلگرام
اگر دنبال کتاب هستید، این ربات می‌تواند به یک کتابخانه دیجیتال همیشه‌همراه تبدیل شود.
👇
✨
امکانات:
🔎
جستجوی سریع کتاب‌ها
📂
دسته‌بندی بر اساس موضوع و ژانر
❤️
ذخیره کتاب‌های موردعلاقه
🔥
مشاهده کتاب‌های ترند و محبوب
🎲
پیشنهاد تصادفی کتاب برای کشف آثار جدید
📖
رابط کاربری ساده و شبیه اپلیکیشن، بدون نیاز به نصب برنامه اضافی.
🤖
ربات:
@BooksBunchbot
⚠️
قبل از دانلود یا اشتراک‌گذاری کتاب‌ها، قوانین کپی‌رایت و حقوق ناشران را در نظر داشته باشید.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6091" target="_blank">📅 23:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6088">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
200GB
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 100 / 100
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6088" target="_blank">📅 22:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6087">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚀
آپدیت بزرگ UAC Spoofer Android منتشر شد!  نسخه 1.0.5 با امکانات جدید برای عبور بهتر از DPI و فیلترینگ:
✨
حالت‌های جدید:
⚡
Fast
⚖️
Balanced
🥷
Stealth
🛠
Custom
🔹
سیستم پیشرفته Fake SNI Probe
🔹
تنظیمات حرفه‌ای Fragmentation و TLS
🔹
ذخیره خودکار بهترین Strategy…</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6087" target="_blank">📅 21:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6086">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین: 100 گیگابایت
🥳
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 85 / 100
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6086" target="_blank">📅 21:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6085">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
100 گیگابایت
🥳
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 85 / 100
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6085" target="_blank">📅 21:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6084">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚀
آپدیت بزرگ UAC Spoofer Android منتشر شد!
نسخه 1.0.5 با امکانات جدید برای عبور بهتر از DPI و فیلترینگ:
✨
حالت‌های جدید:
⚡
Fast
⚖️
Balanced
🥷
Stealth
🛠
Custom
🔹
سیستم پیشرفته Fake SNI Probe
🔹
تنظیمات حرفه‌ای Fragmentation و TLS
🔹
ذخیره خودکار بهترین Strategy برای هر مسیر
🔹
امکان وارد کردن کانفیگ‌های شخصی (Manual Mode)
🔹
منوی فارسی
🇮🇷
و English
🇬🇧
🔹
افزودن Certificate داخلی
🔹
بیلد و انتشار خودکار توسط GitHub Actions
🔹
لاگ‌های پیشرفته برای عیب‌یابی
این پروژه از کانفیگ‌های VLESS و Trojan پشتیبانی می‌کند و با استفاده از Xray داخلی، VPN محلی و تکنیک‌های مختلف SNI Spoofing برای دور زدن محدودیت‌های شبکه طراحی شده است.
⭐
اگر پروژه براتون مفید بود، حتماً داخل گیت‌هاب بهش Star بدین.
🔗
GitHub:
https://github.com/Floxu1/UAC-SNI-Spoofer-Android
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6084" target="_blank">📅 21:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6083">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">😎
پروکسی‌های اختصاصی آرشیوتل
⚡️
پروکسی ۱
🚀
پروکسی ۲
💡
روی لینک بزنید و گزینه Connect را انتخاب کنید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6083" target="_blank">📅 19:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6082">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFwLM7ei_Pt0wqJX5rlNVK-cHItAR8BDX0r4e50UBeqGT_CNajHvZiPxKV0WZ8A6wNmKjSEOIqGg0Yqz5FayMftRZJyFLMxSn8tG79kwrpfgh-01EWyiw5fkTzHWNjX0--hRf4vhQxWENt4zjrAShMF43wmudZrEHS4ErqrmY5mjm5AlyTh93S6Z_PFchepHYo2InI5XOPABfX1u53LBvma_e6SgFd_WmjnhmRB13YiPHRHeFcwMTHgvJMoN5UH9OReXZ_ct4MSdqAiKBkOBLLbrKTnlTzI7c604yrGfj_JmuRZSfTg0QOyiJY_gJv_Zj1HSRxueKU13KBY9ldOsMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📄
✨
آپدیت جدید UPDF منتشر شد!
اگر زیاد با فایل‌های PDF سروکار دارید، نسخه جدید UPDF چند قابلیت جذاب مبتنی بر هوش مصنوعی دریافت کرده که می‌تواند حسابی در زمانتان صرفه‌جویی کند.
🚀
🆕
امکانات جدید:
🤖
AI Copilot
تبدیل، فشرده‌سازی، محافظت و مدیریت PDF فقط با نوشتن یک دستور ساده.
🔍
جستجوی معنایی هوشمند
فقط دنبال کلمات نمی‌گردد؛ مفهوم موردنظر شما را در اسناد پیدا می‌کند.
📑
AI Bookmark Agent
ساخت خودکار بوکمارک و فهرست برای فایل‌های PDF طولانی و چندصدصفحه‌ای.
✍️
AI Editor Toolkit
بازنویسی، خلاصه‌سازی، گسترش متن و اصلاح محتوا مستقیماً داخل PDF.
🎨
AI Creative Studio
ساخت استیکر، مهر، واترمارک و پس‌زمینه‌های اختصاصی با هوش مصنوعی.
📋
AI Page Management
شناسایی خودکار صفحات خالی، چرخیده یا دارای مشکل تنها با یک کلیک
⚡️
برنامه UPDF کم‌کم در حال تبدیل شدن از یک PDF Reader ساده به یک دستیار کامل مبتنی بر هوش مصنوعی برای مدیریت اسناد است.
updf.com
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6082" target="_blank">📅 19:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6078">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bc7ad03ba.mp4?token=UJqABYY-YN8lzGXlb_UnSDQT3CMGyzpTpVCpDS3Vw9HQmL48oI77-xLd5G6vmEJmAWvkY5X5CQ-5_ElB_S5S8MNQZ3WA_DLyPy315HdtIbEvNjCu-M6-x-gSmpvsB46NN6fQvxc9Ipz9IsTETXjDf1Mk8FHNH3IjhEc5tWif-7VvFP5-F9Pq8wzMRxS6oXzNKmgHvKSwn2MaVYYZRB--EPV1J66punI_W0uiBqDtoBnfeRzTnzAGoB61wn3jFI-5KsW8AwK0eJcoNyI-2biEPm5MXdidsbMRwx_VSYOsINgJGz1XB2oGvIR792rVATZ0bxzdsBsE5Ut4bzzxTuNMkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bc7ad03ba.mp4?token=UJqABYY-YN8lzGXlb_UnSDQT3CMGyzpTpVCpDS3Vw9HQmL48oI77-xLd5G6vmEJmAWvkY5X5CQ-5_ElB_S5S8MNQZ3WA_DLyPy315HdtIbEvNjCu-M6-x-gSmpvsB46NN6fQvxc9Ipz9IsTETXjDf1Mk8FHNH3IjhEc5tWif-7VvFP5-F9Pq8wzMRxS6oXzNKmgHvKSwn2MaVYYZRB--EPV1J66punI_W0uiBqDtoBnfeRzTnzAGoB61wn3jFI-5KsW8AwK0eJcoNyI-2biEPm5MXdidsbMRwx_VSYOsINgJGz1XB2oGvIR792rVATZ0bxzdsBsE5Ut4bzzxTuNMkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎵
🤖
گوگل یک مدل رایگان برای ساخت موسیقی منتشر کرد!
Magenta RealTime 2 (MRT2)
ابزاری جدید از گوگل است که می‌تواند کامپیوتر شما را به یک ساز موسیقی هوشمند تبدیل کند.
🎹
⚡️
✨
قابلیت‌ها:
🎼
پشتیبانی از ده‌ها سبک و ژانر موسیقی
🎹
اجرای زنده با پیانوی مجازی
⌨️
کنترل و تولید موسیقی با دستورات متنی
🖱️
واکنش به حرکات و تعاملات کاربر
🎷
شبیه‌سازی انواع سازها و صداها
⚡
تولید موسیقی در لحظه (Real-Time)
🎯
مناسب برای آهنگسازان، تولیدکنندگان محتوا، بازی‌سازها و هرکسی که می‌خواهد بدون دانش تخصصی موسیقی ایده‌هایش را به صدا تبدیل کند.
🔗
امتحان کنید:
https://magenta.withgoogle.com/mrt2
🎶
آینده ساخت موسیقی هر روز بیشتر به هوش مصنوعی گره می‌خورد.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6078" target="_blank">📅 18:12 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6077">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FaYDJ71qgMxijNOES-j8JGnh-nxEaw2ufK62Bgt6W5esb1P7fNP1cCpeQiGknUA98WfB1aTalflo8dDUpd9KR9hfGJ3f9YLTq-FSGXVKxc4mzYmMIOMCWP9nJgfnTHkG9lC3tiUSO4sEFkWOnyyjYJJmi7oBhBqpZCMElo7IrEdoCJbejunktNlbTSPyj54PhrUYYLP_sHFI68XA6isSdOLeuOyQQ17Q_sPrd1-USsUnxsp44IqTwaQZXYQ060aWSRVrsUOkE3NYykFK5ymuS5sJde2iSVgHZtQF8zbGVEcgPlKFUtokoqpATNW3YIB_ctMqcaij_afsnsDPlwFv-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه اندازی پلتفرمی توسط OpenAI با نمونه‌های کاربردی ChatGPT
🔥
در این پلتفرم حرفه‌ای‌ها از حوزه‌های مختلف تجربیات خود در کار با ChatGPT را به اشتراک می‌گذارند. آنها توضیح می‌دهند که چگونه شبکه‌های عصبی کارهایشان را ساده‌تر کرده‌اند و دقیقاً در چه زمینه‌هایی کمک کرده‌اند
⚡️
🔗
https://chatgptpro.substack.com/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6077" target="_blank">📅 18:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6076">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">زمان : نامحدود
حجم : ۱۰۰ گیگ
متصل رو همه اپراتور ها
✅
اتمام حجم
❌
vless://d601f422-a626-4533-a3d9-8fddf16517b5@171.22.136.84:8443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#100gb</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6076" target="_blank">📅 16:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6075">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
80GB
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 80 / 80
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: پایان یافته - تکمیل ظرفیت</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6075" target="_blank">📅 14:55 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6074">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✨
اطلاعات عمومی
[5/23/26 3:48 AM] ᴍᴍᴅ: ثنایی یا صنایی یا سنایی
[5/23/26 3:49 AM] XrayUI Group:
ث</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6074" target="_blank">📅 14:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6073">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpJWnVBRzJ3d0RkaWJMV2R1VkZ6YmVY@45.95.233.55:443#%40MohrazServer%20-%20%40ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6073" target="_blank">📅 14:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6072">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">کانفیگ مخصوص کلاینت happ
زمان : 40 روز
حجم : ۱ ترابات
لینک دانلود
Google play :
https://play.google.com/store/apps/details?id=com.happproxy
Github :
https://github.com/Happ-proxy/happ-android/releases/tag/3.22.1
happ://crypt4/vfb1onL0njkmd47DHXNPUKKEEPQNrpfahCf5vmgczvqBX6IcP0JkObKmWDw+hAZ2VwZ21pi6REi4WyyLXGQxIbppw+LrTNA2hI/+0Mv4HBgFZV3AEzeh1kgwD0yr9nppZJsSGofePhJLN2CcRV095i4udLU52HxgvaCcMSlW+MxM5BQyQycn0iznnAt+/d3fjhtJbMsGGPwC3VAK25ERXDg4IQVlPdk1K7QOfMqddVfnbPKHx6cYrLbYlh0jQS1ya2pgxEDHAHnKBapy6ldkGRojSL5NkZ0hDNhagnbvlB6EG+7WXfXLGBG4HTDv18z8kKwMcd8SqxlQs7xoZnsmUaMDLdiy7WLZ1feY8Z0upkOTj72B1Iwj1TIShiG1ZNyvKn9pPLCrNhntsChX3ckLrAMCI8U3iIRjoTgfW3WftxxTLfTN45xFAYGkektT1C1z/v1Bs+E5FZujJdzi/rCA+RoFpO8p7CvIbbCizV+dYY5deDml/Y0aBtTcy5J/Haukal2Wsx3Rrhcb8V1+L9FM6PfN0aKuZyzZ6cEZ2BCJTSEG4CAv0PSOwqQHts5lpfRLDdE6M5em9jkYuS5sdwxU2PULK4QDUn2a4LmkW5NMWQq/QOYuNTaiPsN1QqLKsTi0eXaGC9sJNHRLFOXahzwCgnKKr+ios8lIK98MoQ0KoUU=
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6072" target="_blank">📅 13:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6071">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lx4L2soGncLi1dU2osOqM2Q-pvyN1F3gvT1t4d7YGFBUuQAgA6AY-0swP7jIM4tkvk2Y6I6z9rlHZLDVJjICoa5ngQXP259wIMuSlXJ1OVfIVZhYh0DhTgmW1Zb2gofEETJaM4fBox1muZjuY_f5XuAGvjPOnzFkCt_bRavtnfvaxkZlBxil-u2Me_WDLZcHptG8c1X4JdlSqmLDdaShp4FR2jSewe7CeGdM00Uj6d93TbNjRhGFNgBmBOSZLXskQteJNl9DXekcC2hW1CCzYEItOVOlEZcTI3QPyp4hHOzXzmwU9vNTdmJll8vtVjtpEhbAMAl4tJ6IDUaV0b2LVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوتیوب پریمیوم و بدون تبلیغات
https://morphe.software/
قابلیت ها :
اوپن سورس
دانلود با کیفیت دلخواه خودتان
امکان تماشای ویدئو در پس‌زمینه و با صفحه خاموش
امکان تنظیم دقیق پلیر به دلخواه خودتان
گیت هاب پروژه :
https://github.com/MorpheApp
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6071" target="_blank">📅 13:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6070">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🤖
وگا | نسل جدید ربات‌های هوش مصنوعی  وگا فقط یک چت‌بات نیست؛ یک دستیار حرفه‌ای و همه‌فن‌حریفه که بهترین ابزارهای AI دنیا رو کاملا رایگان و بدونه زیرمجموعه در اختیارت می‌ذاره
✨
🧠
گفتگو با قدرتمندترین مدل‌های جهان GPT-4 • GPT-5.5 • Gemini 3 • Llama 4 • Qwen…</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6070" target="_blank">📅 13:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6069">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔥
آپدیت جدید NipoVPN منتشر شد!
‌ابزار NipoVPN یک ابزار متن‌باز برای عبور از محدودیت‌های اینترنتی است که با مخفی‌سازی ترافیک واقعی داخل درخواست‌های عادی HTTP، سعی می‌کند اتصال پایدارتری فراهم کند.
⚡️
🆕
مهم‌ترین تغییر نسخه v1.1.54:
🔹
اضافه شدن پشتیبانی از پروتکل SOCKS5
🔹
امکان انتخاب بین HTTP و SOCKS5 از سمت کلاینت
🔹
بدون نیاز به تغییر تنظیمات سرور
💻
پشتیبانی از:
• Android
• Windows
• Linux
• Termux
📥
دانلود:
https://github.com/MortezaBashsiz/nipovpn/releases/tag/v1.1.54
🎁
همچنین توسعه‌دهنده
چند کانفیگ رایگان
برای تست و استفاده منتشر کرده که بعد از آپدیت برنامه می‌توانید از آن‌ها استفاده کنید.
⚠️
قبل از استفاده حتماً برنامه را به آخرین نسخه بروزرسانی کنید.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6069" target="_blank">📅 11:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6068">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJeN7fGdLyDomtH44aRTV8kk_7bM5QOJAflyHCzRbQVcusqeV0VQslqBJB4uozvOZALe7dG4y2ypd7PdxkO5gej2Vpqtzu04D-_CFROLZjtzFjKwxvpPvTf1FO-_g0-A98EZCt3X2_bDm02gLr-AUbA4HiYiSi6dpR9MPJbNRhfX83pt_8wSiG3A-YeP43ZDLQrXJ2b_-mhph9Ccqzijpbu7NxmLAWpkEQ_GOKVPwCwdd3YE_EHXEA6B1wvVbwDfq9vXN5gHcWIqR8j7AhCbHLGOQedlN400o-RAzt1IMTQ9MU191spv0B4_eZq0kz9QPvk2NH9Qx4XyRvz57clIpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حذف سانسور مدل های محلی هوش مصنوعی مانند Qwen , Gemma , Llama و ... با یک فرمان ساده
https://github.com/p-e-w/heretic
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6068" target="_blank">📅 11:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6067">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1602b4fbe6.mp4?token=Mq35_D2BlNRG7EdQxBKxIBphQIHQzzW0o2qQucTFXGHOyxParfd3WA-iL3oEMZt6F7IwUy1tLHdWj6Z2rKZhaIiI5sVqfDdhoLH9wex2vJxkPPXDJ391Gu-ysGkwWwO9yw1aYI5qHluLH1YMZMreLZiflkK7zDpA967gfxS0xoI_oF9JQnHDkBxhMI8_9OVIuXaV71Q-lSMmaHW5yVyKgA6FAfeTwXq3SN73MhUV7nD7DMFfeweM1r42VxJ8plI1FGeOWrU44K652DBtc9hS3CkAwthuxGhoUfpWaBQ54_8P0eNzkHx3pBXAPlNkHD7kN52R7fk-C9QPB3XmZj7Ndg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1602b4fbe6.mp4?token=Mq35_D2BlNRG7EdQxBKxIBphQIHQzzW0o2qQucTFXGHOyxParfd3WA-iL3oEMZt6F7IwUy1tLHdWj6Z2rKZhaIiI5sVqfDdhoLH9wex2vJxkPPXDJ391Gu-ysGkwWwO9yw1aYI5qHluLH1YMZMreLZiflkK7zDpA967gfxS0xoI_oF9JQnHDkBxhMI8_9OVIuXaV71Q-lSMmaHW5yVyKgA6FAfeTwXq3SN73MhUV7nD7DMFfeweM1r42VxJ8plI1FGeOWrU44K652DBtc9hS3CkAwthuxGhoUfpWaBQ54_8P0eNzkHx3pBXAPlNkHD7kN52R7fk-C9QPB3XmZj7Ndg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
🤖
آیفونت را به کنترلر مدل‌های هوش مصنوعی تبدیل کن!
تیم LM Studio ابزار جدیدی منتشر کرده که به شما اجازه می‌دهد مدل‌های هوش مصنوعی اجراشده روی کامپیوتر را مستقیماً از طریق گوشی کنترل کنید.
⚡️
🛠
نحوه راه‌اندازی:
🖥
LM Studio را روی کامپیوتر اجرا کنید.
🔗
کامپیوتر و گوشی را با LM Link به هم متصل کنید.
📱
اپلیکیشن Locally را روی آیفون نصب کنید.
✅
با دنبال کردن مراحل داخل برنامه، آیفون را به LM Link اضافه کنید.
بعد از اتصال می‌توانید مدل‌های مختلف را مستقیماً از روی گوشی مدیریت و استفاده کنید:
🦙
Llama
💎
Gemma
🌊
DeepSeek
🔮
Qwen
🪨
Granite
🐬
Dolphin
🧠
Nous Hermes
و ده‌ها مدل دیگر برای برنامه‌نویسی، تولید محتوا، ترجمه، تحلیل و...
🔥
یعنی بدون نیاز به سرویس‌های ابری، مدل‌های محلی اجراشده روی کامپیوتر را از هرجای خانه با گوشی کنترل می‌کنید.
📖
اطلاعات بیشتر:
https://lmstudio.ai/blog/locally-lm-link
🔵
@ArchiveTell
|</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6067" target="_blank">📅 09:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6066">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🎥
سایت های تولید رایگان ویدئو
⚡️
Dreamina
— تبدیل درخواست‌های متنی به تصاویر و ویدئوها. هر روز چند تولید رایگان ارائه می‌دهد و برای پروژه‌های تجاری مناسب است.
🔥
Pika
— یکی از دوستانه‌ترین تولیدکننده‌ها برای مبتدیان. حداقل تنظیمات، شروع سریع و محدودیت روزانه تولید رایگان.
🧠
Runway
— یک ابزار جامع برای کار با محتوا. ویدئو، تصویر، صدا تولید و ویرایش می‌کند.
🦾
Wan
—  می‌توان آن را به صورت محلی اجرا کرد. ویدئوهای با کیفیت می‌سازد و نیاز به سخت‌افزار قوی ندارد
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6066" target="_blank">📅 09:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6065">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ArchiveTel
pinned «
ArchiveVPN | کانفیگ رایگان
📝
کمپین: 184
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 94 / 184
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🟢
وضعیت: فعال - در حال توزیع
»</div>
<div class="tg-footer"><a href="https://t.me/archivetell/6065" target="_blank">📅 08:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6064">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nY9Q5WUAaIJqN3JoKCPBO0_FzQmvwzrm5YqwN-0z4EJ0_3QXQbOKY8Y-v7uo3mIyrf30BenABJerYHD0KbE-MDIDhtCvLzRuJ7w6spTONTqTksn2iAhqqCzYHmsqnh60sMxcEnxa4L6A2Nr2zbIgZp8JumGmFHwBsaF9W_gGQvK5Fp03XL5ccTYt_o61sAlun-KmKY7uiAyfnsxy5LDuymmD1tIfSPpZtSLaFUdWKLxvD6Lf4SlfuvpOphk9e_896Kd4p_oxxtGVC6c7GVBlUjFTT3T50ZgxqEpH7vDUvos9S04AgMNpL0uc-omEZ_g4Z4lUSbPOxcWwIxz81U6qlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آفر 91 روزه F Secure Vpn
🔑
ابتدا شما به یک ip سوئد
🇸🇪
نیاز دارید ( حالا هر vpn )
برای ایمیل هم میتونین از
@TempMail_org_bot
استفاده کنین
📩
وارد لینک زیر بشید و ثبت نام کنین
✌
link
حالا رو add subscription code بزنین و کد زیر رو وارد کنین :
BNAUH-EFCTO-EQOCZ-RXHES
و در آخر ایمیل رو تایید کنین و تمام
🤝
دانلود F secure vpn برای اندروید
🕹
دانلود F secure vpn برای ios
🌐
اگر اروری دریافت کردید حین ثبت کد مشکل از آی پی شماست دوباره امتحان کنین
❤️‍🔥
تا تموم نشده بزنین
🩵
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/archivetell/6064" target="_blank">📅 04:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6063">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
184
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 94 / 184
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6063" target="_blank">📅 03:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6061">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🤖
وگا | نسل جدید ربات‌های هوش مصنوعی  وگا فقط یک چت‌بات نیست؛ یک دستیار حرفه‌ای و همه‌فن‌حریفه که بهترین ابزارهای AI دنیا رو کاملا رایگان و بدونه زیرمجموعه در اختیارت می‌ذاره
✨
🧠
گفتگو با قدرتمندترین مدل‌های جهان GPT-4 • GPT-5.5 • Gemini 3 • Llama 4 • Qwen…</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/6061" target="_blank">📅 02:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6060">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پروکسی
🔥
https://t.me/proxy?server=channel.t.me.tradeip.store&port=8443&secret=dd7fe6d9803aafad7823ee9eecbf31886a
tg://proxy?server=channel.t.me.tradeip.store&port=443&secret=dd9c214385c44ee56c5f8d0a0f07475c3f
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6060" target="_blank">📅 01:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6059">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🤖
وگا | نسل جدید ربات‌های هوش مصنوعی
وگا فقط یک چت‌بات نیست؛ یک دستیار حرفه‌ای و همه‌فن‌حریفه که بهترین ابزارهای AI دنیا رو کاملا رایگان و بدونه زیرمجموعه در اختیارت می‌ذاره
✨
🧠
گفتگو با قدرتمندترین مدل‌های جهان
GPT-4 • GPT-5.5 • Gemini 3 • Llama 4 • Qwen 3.6 • GLM 5.1
🎨
ساخت تصاویر حرفه‌ای و خلاقانه
از عکس‌های واقعی تا لوگو، بنر و طرح‌های هنری خیره‌کننده
🎙️
ویس چت هوشمند + تبدیل صدا به متن
صحبت کن، وگا می‌شنوه، می‌فهمه و پاسخ می‌ده
🔊
تبدیل متن به صدای طبیعی
ساخت پادکست و فایل صوتی با صدای مرد و زن
🌐
مترجم هوشمند چندزبانه
ترجمه دقیق متن و ویس به زبان‌های مختلف دنیا
📊
قیمت لحظه‌ای ارز دیجیتال، دلار و طلا
فقط کافیه بنویسی چی‌میخوای
مثال : «چک تتر»
👥
مناسب گروه‌های تلگرام
با قابلیت AI Agent برای تعامل هوشمند داخل گروه‌ها
🚀
همین حالا وگا رو امتحان کن:
🤖
@T_Vegabot
📢
VegaEnter
-
ArchiveTel</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/6059" target="_blank">📅 00:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6058">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Etp4aXemHdfMq__o2q4LDx7ML-UdoLzAzm-6p4MdVTa5wgBaDjShrtq7pSHLlNf_pnvGChWFWnJe67h4OP5zI0hXiUNpRtEP0hCGqi-WmzY9W8bMJKO7ArzY0JpV76rpdTAzEkxdXsVBoZTJVKclvy1F1aKe3EUHWoZlTUo7_y0DLPgREQLye_3Yf-I-JRXPPlkQIvPY04NiiIQP26SMh7_fTQkc9g4xXbISpQAdbPk0NOUeqSE58HaiaRDvqgdlcqlmgtzZ6gCh_-n2oNmvEBdu2_zmVBWp7U_RRkhguzxYNNC6K1PdK6hf7WRBtsce0RL0hoZxDKuQLS0RqEOe9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">➡️
Atomic Chat
دانلود و اجرا کنندهٔ هوش‌مصنوعی در موبایل‌ها، بدون اینترنت، کاملا آفلاین
🔹
Android
🔹
iOS
❄️
atomic.chat
💬
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6058" target="_blank">📅 23:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6056">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚀
معرفی اپلیکیشن AzadiTunnel برای کاربران iOS (آیفون و آیپد)
خبر خوب برای کاربران اپل! اپلیکیشن
AzadiTunnel
منتشر شد.
این برنامه تمامی قابلیت‌های کلاینت محبوب «شیر و خورشید» اندروید را به آیفون می‌آورد و دقیقاً از همان هسته قدرتمند سایفون (شیر و خورشید) استفاده می‌کند.
🔹
ویژگی‌ها و امکانات:
✨
اتصال امن و سریع تنها با یک کلیک
📊
نمایش لحظه‌ای وضعیت اتصال، سرعت و ترافیک مصرفی
🛠
دارای بخش عیب‌یابی (Diagnostics) و تنظیمات پیشرفته انتقال (Transport)
🛡
کاملاً متن‌باز (Open-Source)، امن و مبتنی بر حریم خصوصی رابط کاربری بسیار ساده و تمیز
⚙️
آموزش و نکات استفاده:
تنظیمات این اپلیکیشن مشابه نسخه اندروید است. در حال حاضر بهترین تنظیماتی که خوب جواب می‌دهد، استفاده از پروتکل
CDN Fronting
است.
همچنین اگر IP و SNI خاصی در کانال‌ها پیدا کردید، می‌توانید به صورت دستی وارد کنید.
اگر کادرها را خالی بگذارید
، خود برنامه شروع به اسکن می‌کند (ممکن است در اتصال اول کمی طول بکشد، پس صبور باشید!).
📌
پیش‌نیاز:
قابل نصب روی iOS 15 به بالا
📥
لینک دانلود مستقیم از اپ استور:
🔗
🔍
(همچنین می‌توانید کلمه
AzadiTunnel
را در اپ‌استور سرچ کنید)
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/6056" target="_blank">📅 22:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6055">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
800
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 76 / 800
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6055" target="_blank">📅 21:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6054">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7gaHn3wXOwMSxY5aJSTY9zuwr7PTRmY2bsuga8vNejxLohmbEcnuL1wYGxGGtMIjFjgSdNeDxqnPPmFGctIZHJ5KoiOJZPYDlDhJ0w3WzLgOsqo5NfqlexRq-vF0wli1PeTgVPOc7rxhad_uHUjjQ79v2Ael8kieArgfRev3kU9c3mWDsudkdLlqhLUjv5cqDgcIo_CpT2KALtmgZeS878OC9G_PgJlXUllS4Xf49BvqxlDQI9AmNvgMNanDXFiqhueFCKe6P_s60U_ZY8JiGmGi3RVUadXXAnMAJ-MMdNGoVM4aIdYfG4OeCquAVpuImLQFYCfBuAHOtKba19fCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرشیو تل؛ مرجع محتوای ناب و کاربردی
🔥
گلچینی از بهترین مطالب که نباید از دست بدهید
❤️‍🔥
به همراه پخش کانفیگ رایگان
🎁
عضویت در کانال:
🆔
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6054" target="_blank">📅 19:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6052">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdMP-v7jX5XK2NUUpW1CMpafEBbpH6s26_RPQGQwrqhAIPyMONTCxwH7RW6VzUXWbcrSvnKfL-uss87jcYr_y3PL9H-x9iSuFkjJSXjFKVp6LtPrcHK0m6XjDAPU35ShQVOYryPaZmlTI82IM94RzEvriTQA99jrfwElKLQMDvXs51f20Y78GaFkcbH02XGDgucFJpBjuTb6d-nG1Edmh6deTSzAp0d5n0_B1j7NEKOxhjvM_c3Rx-p1SavfgPX5OZG5x-Uti1vx92QRgrhGIMIVNPY4--ixBf_ejCZCWMROORlOiMMMjx2wGJBQ7-exblxVF6C7qaa8y4sf_QEm1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تولید ویدئوی هوش مصنوعی از متن یا تصویر با کیفیت 1080p با Seedance 2.0
با ثبت نام 10 تا credit میده
https://seedance2aivideo.app/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/6052" target="_blank">📅 17:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6051">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ربات قرعه کشی هم داره
هر کی رفرالش بیشتر باشه
شانس اینکه کانفیگ بگیره بالاتره. یعنی 10 تا رفرال یعنی 10 برابر شانس بیشتر نسبت به 1
امشب قرعه کشی میذاریم
یدونه کانفیگ اختصاصی خودش حجم بالا
ممنون از توجه شما
پرزیدنت بچلر</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6051" target="_blank">📅 16:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6050">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ArchiveTel
pinned Deleted message</div>
<div class="tg-footer"><a href="https://t.me/archivetell/6050" target="_blank">📅 16:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6049">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Sorrow of Sophia</div>
  <div class="tg-doc-extra">Draconian</div>
</div>
<a href="https://t.me/archivetell/6049" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/6049" target="_blank">📅 15:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6048">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6x9X6C-BcAaOS8vS8gcHqmXMiAL1stT3T-IQPTZwOgCEyN6yP_1xtzhqGghxWb81_ULn8LmuvrN7z1pqL2vWdB_f9PsfpukwADcRweEC0mPy7xSrp-xbjTWeR6dAAqzkDXB9zInY5Lu8QYAj9vQQjd1MRxwK8D0VbGLeDhzpwQG_RtjQi88XxnVlqlOXVG2nml-a5n9RjnHv6rPWD74PcA4RT4qF-HNmNp_I4bA886jilM20SSfcFfAkQ7Te6AM8JmsZJGNMHPnp4YvBq7nq6VucD-EhdcQh5WcVwvRiY4WwPiGi2OimRrk3xHTnUsXEcgmRooe1xhjYqUkmjq6og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📂
⚡️
FileShare v1.3 منتشر شد!  اگر برای انتقال فایل بین گوشی، لپ‌تاپ یا کامپیوتر دنبال یک راهکار ساده و بدون دردسر هستید، FileShare می‌تواند گزینه جالبی باشد.
🚀
🆕
قابلیت جدید نسخه 1.3:
📱
اضافه شدن QR Code به پنل برنامه و صفحه وب
🔗
اتصال سریع دستگاه‌ها بدون…</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/6048" target="_blank">📅 15:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6047">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IvEfX4PrdVgJLnHa2ffgNtdp6-2AGZDH-SqpBYfKvbEdyptjclYrI-t9w2oTugxnYwitmlHaAbqLnUaxeSWq0zcbbarHg8uxsL6H65HnffrW5hE4t_67XM9-X1sI7AhVQ2r6rkpLlhSWrwGdw0Fh1SlPn3I5jmT_8fhyg2TNW0QoBKENZgcrIaGpyvCRftjQcXpvA9y9i4NaL1FmJQipx0wo7pyf-Ctk2-qdyjiAWmkePUxdwN3URrgto7Jm_7n6X2A8GBvtbSJMbWthQKiXQANNzXKbj3kJQvME-jqp94YvLvJL-bI-6athjZZqIIFh2iaund1jsAmWUX3C1LOSYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">FileShare.exe</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6047" target="_blank">📅 15:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6044">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🎬
دانلودر یوتیوب در تلگرام
دیگه نیازی به سایت‌های دانلود و تبلیغات آزاردهنده نیست!
😎
فقط لینک ویدیوی یوتیوب رو برای ربات بفرستید تا:
✨
ویدیو را مستقیم در تلگرام استریم کنید
🎵
فایل صوتی را با کیفیت اصلی دریافت کنید
📥
ویدیو را دانلود کنید
🗜
ویدیوهای حجیم را به‌صورت هوشمند فشرده کنید
❤️
بدون عضویت اجباری در چنلی
⚡️
سریع، ساده و کاملاً داخل تلگرام
🤖
Bot:
@youtubedownload12bot
👨‍💻
Dev:
@Bachedev
#Telegram
#YouTube
#Bot
#Downloader
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6044" target="_blank">📅 15:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6043">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
کمپین جدید
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 64 / 100
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6043" target="_blank">📅 13:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6042">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
همراه اول Happ
❤️
🧭
شرط دریافت:
کاملاً رایگان (بدون دعوت)
👥
کاربران دریافت کننده: 192 / 600
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6042" target="_blank">📅 13:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6041">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXKFNtqHJJPa4J4-ZzpyCB2VVDUOSo_EIF63_s3lxszHwhBDatUayFo_Vny-CPfg-pOhpDe_zDDdmob6oreDNWn4036X6kqqoz1BroZM02q36taEHNBRmghJW8eDkukRSVwDHgySKmRlD6hi7cZ7WS9Ja9n44MdFZjBs4nt6qXIAGOs0c8tXsGcMuIlKhtDP8FA1II2jKYvCFA1LvnUfyuGSx9v8LKk0drdb_sri6gHL4oeLrECpnmZdRJ7uIY6xdx-MSvq6czzm4dMxAHPBJ_zdoRHlIsf0E1y47ZdqGslofU7afzTB6N36qy7U9WF3a32ukvmE3DP0Mydi0Nk43w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
ابزاری که مصرف توکن‌ها را بدون از دست دادن زمینه به طور قابل توجهی کاهش می‌دهد.
به جای اینکه فایل‌های عظیم، لاگ‌ها و تاریخچه چت‌ها را به مدل بدهیم، Headroom ابتدا آن‌ها را بهینه‌سازی می‌کند و سپس برای پردازش ارسال می‌کند.
این چه فایده‌ای دارد:
🕤
قبل از پردازش زمینه را فشرده می‌کند و مصرف توکن‌ها را ۶۰ تا ۹۵ درصد کاهش می‌دهد.
🕤
در صورت نیاز امکان بازیابی فوری داده‌های اصلی بدون از دست دادن جزئیات را فراهم می‌کند.
🕤
کمک می‌کند تا با پروژه‌های بزرگ و جلسات طولانی کار کنیم.
🕤
از Claude Code، Codex و Cursor پشتیبانی می‌کند.
https://github.com/chopratejas/headroom
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/6041" target="_blank">📅 13:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6040">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b7b603d8f.mp4?token=TzutCBY4iKX0gaOWpcW210wHhmYr0QFj6JEELQgWupPoxHlKHSEzUaX0cox7cSUHsLm3P63ZaaRm_U9ZFm6XCLSDgP8A4SPt5Z1EPWbW_nrWP0E9s5a5ftfmEIeRa-TZ8EqWijaTy4_E2VlPdyoaL7cnV2gH2cisafU3h7U_RCC-AVwkNKNEKWWAJPJQW_k-KntGsVBZUD1viToTXaZxnvw9FZgQghTzs0f60NmdGQ-qDFkwRBTYrJM79CUApAacBqBAW0acP0k1LD_sa84H8Yz5_6jJjQ1CNX_luC5w7CJ7-qIY3L_mAM3AeBBmrdAQzNdpLHj4fxKgDJPMR59-3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b7b603d8f.mp4?token=TzutCBY4iKX0gaOWpcW210wHhmYr0QFj6JEELQgWupPoxHlKHSEzUaX0cox7cSUHsLm3P63ZaaRm_U9ZFm6XCLSDgP8A4SPt5Z1EPWbW_nrWP0E9s5a5ftfmEIeRa-TZ8EqWijaTy4_E2VlPdyoaL7cnV2gH2cisafU3h7U_RCC-AVwkNKNEKWWAJPJQW_k-KntGsVBZUD1viToTXaZxnvw9FZgQghTzs0f60NmdGQ-qDFkwRBTYrJM79CUApAacBqBAW0acP0k1LD_sa84H8Yz5_6jJjQ1CNX_luC5w7CJ7-qIY3L_mAM3AeBBmrdAQzNdpLHj4fxKgDJPMR59-3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗂
ارسال فایل‌ها به هر کجا و به هر کسی — ابزاری که همه چیز را فوراً ارسال می‌کند.
می‌توانید سرویس‌های ابری را فراموش کنید:
🕤
پشتیبانی از هر نوع داده‌ای: اسناد، عکس، ویدئو، موسیقی، آرشیوها و پوشه‌های کامل.
🕤
نامحدود مطلق: هیچ محدودیتی در اندازه وجود ندارد، حتی ده‌ها ترابایت.
🕤
انتقال مستقیماً بین دستگاه‌ها انجام می‌شود، بدون سرورهای واسطه.
🕤
رمزگذاری در سمت فرستنده انجام می‌شود.
🕤
رایگان و بدون نیاز به ثبت‌نام اجباری.
https://github.com/tonyantony300/alt-sendme
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6040" target="_blank">📅 13:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6039">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTIKQ0k1LIGwJqRCTVLaHtK-6b4Z77IYbUsdiVsiuZQVaLFU20fFuMesxZJrw0Vn4WLMIn63LgNUsU0xuIycZCSFiqQdeTVtSR1Xy7XabtOdkENRqWxLkGVY1KWo_k9-YWDyGZCY14QM_kizZx5sXtqF8YYiuxGHwCuuBQEH6ZpURkZWS7Gua8Ui_RkB5j3P0qjA13Jkgj3EtkutrvT_HUeJ9T6Z6e6hWs6B_pgn48oHjfjs_5tx3IfuugA_pliht4YtBl1-5d_c-X3EaAkHX29Ub-gKWWTarv_4xKhbfugrsH-UDZ70AOFi_uvKsiz2r2De_XFKXS4nXP2m2ZerVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حذف رایگان پس‌زمینه تصاویر با هوش مصنوعی
پشتیبانی از فرمت‌های مختلف، پردازش در مرورگر به صورت محلی، حفاظت ۱۰۰٪ از حریم خصوصی.
https://quickbgcut.com/
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/archivetell/6039" target="_blank">📅 13:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6038">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVRKfyU6As7-g6oT7qcnT7nOkEP8kDwGviAqlhMjZeDjfdLEi9sUKyunffQlabVBV0F7j68C1ZTZxOxbiDZDa1mrh4hm2fC0xJXeDi6r5Kg5Y953jSEO1xZqhr0cvxXbNqf-DIKKby7QTYEh3XX1E0gt4ZZvpbjCBpUksx-tJX6k06GpRWI2R_Prp68PESbCqWT2sijunSwSoNhw-GLLRMjlkUPA82Omq0eARnfwcIDXv1Kd7eAHGpuHE3eAkcNoaw7Oj1P4pwPybUukzRRkn6-avlblWjeUTRH_fC0JrEvVN8d3dVQb5Utqcj2tQ0vvvh4W_zgW9PpCvOl37egZ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📦
✨
حجم پروژه Node.js رو با یک دستور کم کن!
اگر از Docker، Vercel یا Heroku استفاده می‌کنید، ابزار
untracked
می‌تواند فایل‌های غیرضروری را به‌صورت خودکار از خروجی پروژه حذف کند و حجم نهایی Deploy را کاهش دهد.
🚀
⚡
قابلیت‌ها:
🧹
حذف README، LICENSE، CHANGELOG و مستندات اضافی
🗺
حذف Source Mapها و فایل‌های توسعه
🧪
حذف فایل‌های تست، نمونه‌ها و پوشه‌های غیرضروری
🐳
ساخت خودکار فایل
.dockerignore
▲ پشتیبانی از
.vercelignore
🚀
سازگار با Docker، Vercel، Heroku و Yarn
💻
استفاده:
npx untracked
برای ساخت خودکار
.dockerignore
:
npx untracked > .dockerignore
🎯
مناسب برای توسعه‌دهندگانی که می‌خواهند حجم Imageها، Bundleها و زمان Deploy را تا حد امکان کاهش دهند.
🔗
GitHub:
https://github.com/Kikobeats/untracked
#GitHub
#NodeJS
#Docker
#Vercel
#DevOps
#OpenSource
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6038" target="_blank">📅 13:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6037">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
اهدایی
❤️
🧭
شرط دریافت:
کاملاً رایگان (بدون دعوت)
👥
کاربران دریافت کننده: 292 / 352
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/6037" target="_blank">📅 03:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6033">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwVCbRi17uZieu9l39p0CpE3kg3z62rMhELHcmWk1FoSGiOvQXLgUULS7VSjYV_ZaIm2Vo8SHleft6yVJctFAjMhGafX_nXM1HxCm9JOWWB7n1Oh-nYE9o1BoZbQDwonh4uF0-eV_A56Pn7qYoSbww0kqkQ-57i5rNRai8rOP3Wb0WY9WzyD6rLM52VTgBQ4C6F45AQ3vHy-M6HSu8tFl_lROIN-aKSgB0M_NosUJkMObpJSgSiACgZby7dHOMu1qUBHztGlNfdol8dA7xPWizlj4I_tjxSY9-4Av0uQUk1_Gnd77J0RpbjWncJ0hbcoKwpluDLGkj04SjPrMJXSOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین: 100 گیگابایت-تایم نامحدود
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 149 / 200
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/فایل
⏰
مدت اعتبار: بر اساس تنظیمات دستی/فایل
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/archivetell/6033" target="_blank">📅 01:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6031">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین: 100 گیگابایت-تایم نامحدود
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 149 / 200
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/فایل
⏰
مدت اعتبار: بر اساس تنظیمات دستی/فایل
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/6031" target="_blank">📅 01:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6030">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
100 گیگابایت-تایم نامحدود
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 149 / 200
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/فایل
⏰
مدت اعتبار: بر اساس تنظیمات دستی/فایل
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/archivetell/6030" target="_blank">📅 01:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6029">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚀
UAC SNI Spoofer Android
ابزار متن‌باز اندرویدی برای اجرای کانفیگ‌های VLESS و Trojan همراه با Xray داخلی و قابلیت SNI Spoofing.
✨
امکانات:
•
🌐
اسکن خودکار SNI از لیست دامنه‌ها
•
⚡
انتخاب بهترین کانفیگ بر اساس پینگ و اتصال
•
🔒
پشتیبانی از VLESS و Trojan
•
📱
آپشن Split Tunneling برای انتخاب اپلیکیشن‌های عبوری از تونل
•
🌙
حالت تاریک و روشن
•
📊
نمایش لاگ زنده Xray، VPN و خطاها
•
🛡️
مدیریت VPN محلی با tun2socks
🧑‍💻
پروژه کاملاً متن‌باز بوده و با Java توسعه داده شده است.
🔗
GitHub:
https://github.com/Floxu1/UAC-SNI-Spoofer-Android
#Android
#VPN
#Xray
#VLESS
#Trojan
#OpenSource
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/6029" target="_blank">📅 00:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6028">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🤖
Private Link Bot | اشتراک‌گذاری فایل با لینک خصوصی در تلگرام
دنبال راهی هستی که فایل‌هات رو سریع با بقیه به اشتراک بذاری؟ این ربات بعد از ارسال فایل، یک لینک اختصاصی برای دانلود می‌سازه.
🔗
✨
امکانات:
•
📁
تبدیل فایل به لینک دانلود
•
⏰
تعیین زمان انقضای لینک
•
👥
محدود کردن تعداد دانلود
•
🔐
رمزگذاری روی لینک‌ها
•
⚙️
ذخیره تنظیمات پیش‌فرض
📌
مناسب برای اشتراک‌گذاری موقت فایل‌ها، اما توجه داشته باشید که فایل‌ها از طریق خود تلگرام و ربات مدیریت می‌شوند و لینک دانلود مستقیم خارجی (Direct Link) ارائه نمی‌شود.
🛠
دستورات:
•
/settings
— تنظیمات پیش‌فرض
•
/help
— راهنما
🤖
ربات:
@Private_URL_Robot
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6028" target="_blank">📅 00:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6027">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">چنل های رسمی مهم:
🟡
چنل شیر و خورشید
🟢
چنل MahsaNG
🟣
چنل TheFeed
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/6027" target="_blank">📅 00:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6026">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکلاینت شیر و خورشید</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZpTFXrtEkoyWoLNV7AJBoEjCp-ju5ee80HLLadjrvqXg6hgpsF0WLKyl8NE4Yau3PY7e3i1FsxVmMMOCVPgjBQCGtn0ja9Os_vBUgDPC5-eRX59IUyDXU9FG9aB1WJI9w57YPl-CKZvsgXZ7zjIajBywhGaHmyr3a5dQAlOz0T9okzOixU5RfPibJv0bJIusFVhUINHioIisGanGpI4BCukWNr_SGhoVMNSupCAklQlRzLoPZadMIBw2LVaQhdodG_uS2I6HuUrJBChre8CNt3TyA-IR6ojEHh-sAvFcOfNgmHvGZEJ_jsZO3xV0re2dP3FjiCtyXSm_K7fPPOkQiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال کلاینت شیر و خورشید را دنبال کنید و به اشتراک بگذارید!
https://t.me/ShirokhorshidOfficial
دیروز متوجه شدم چندین کانال تلگرام که خیلی هم سابسکرایب شده بودند خودشون رو کانالی برای آپدیت های این برنامه معرفی کردند. دقت کنید که فایل نصب برنامه رو از کجا دریافت میکنید. فایل های دستکاری شده و ناامن در بعضی از این کانال‌های جعلی دیده شده. تا جایی که امکانش هست فایل نصب برنامه رو فقط یا از گیتهاب برنامه یا از همینجا (تنها کانال رسمی در تلگرام) دریافت کنید.</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6026" target="_blank">📅 22:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6024">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">دوستانی که قصد دونیت کردن دارند، دایرکت پیام بذارن
کانفیگ ها ازین به بعد به این شکل توزیع میشه تا سهم کسی ضایع نشه و بهتر بشه مدیریت کرد
فرقی نداره اوتباند، کانفیگ یا هر مدلی
ظرفیت ها هم طبق کمک شما عزیزان و تیم خودمون اوکی میشه
❤️
افزایش پیدا میکنه قطعا
ممنون از توجه شما</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/6024" target="_blank">📅 20:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6022">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ArchiveTel
pinned Deleted message</div>
<div class="tg-footer"><a href="https://t.me/archivetell/6022" target="_blank">📅 19:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6019">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بعضی کانفیگا تو ویتوری ویندوز وصل میشه ولی رو اندروید با همون نت وصل نمیشه
راه حل
😁
از کلاینت exclave تو اندروید استفاده کنید
😎
لینک دانلود از گیت هاب ؛
https://github.com/ExclaveNetwork/Exclave/releases/tag/0.17.41
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/archivetell/6019" target="_blank">📅 19:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6006">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h1QBNK_Vw_JV6u60dBp2qdPCg8crMRp4p8PlN0UsEL5pLiec_h__JQOlD0ooOMvpONjFKO6GRpFkjUyuMOg2QEISjoOpRgIVWDxEoNcdq08-2wALxT6VspyCHHoy1-mXmYG15gcW0dZKnpzV3E8e7U8y3-Vx1eZ6tZsMPv9G2dJCA-TB_0ZIjsoeE_o-h6bktOt-VHGiMENCpGcrf_V-LGqNOM5qC7wGQD1g5JCkIWLa_QO7i-AMY1NrcMu0rYKZir6MxMyT4VTiXVKL6PWIT74HC4PUAVPQKQeVVRLfmOxmMEEyQdaKOF1saAqV_oXT5Ko6qihMwp_70nlVYTHWFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lLmLnwiXJoMwuGCsfb6oc0eX7U9EP2YsnAh_MZ0yCI7zrIjbQ0iqNZNvzoREELY1xJGizfatMoyAXPDuWFduozK4J3orAAhCvCohyVLnSct1Ac2XKc8lYJBKP_Xqf-e_G3mEe8HwNssNubJzYSO-B_vfxZc6ZOOzy9JQBxtsgldrBGbKP6xEpricOx5shMHaal55EgOxuPFr80z5xvqjspozZ2SJ_qg_2ivza9kS7BXHvsaCE8lXvbdT5HR5aCmlyPlMeXomMk48l6hduGo1dzZWyZJg66Ig9CLFhMecWsdmboqg9hkbZ6chFXZBpxWAA-zwc536j8kORbEfXYT5tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kWPGSOuDP2nJZCGwGdTfkZwknzuMo1AWB1ZO8CmAZHw_ruTNjyZfnDzB8x5yjByma1sTr8vU8KbW-k7fBgWmhs8-wwCKh7exzn86UFWmn5gKe9PdcNDho-skEk_fS-0-yrF8E6pF5kGtRdpbannuTStI9eu2mZz4KJHZMC08j5W_qDQuITEqfgNQD1X0INoO3mMICD0wwsAnzjU8JDgqZaKNj3AJ-UFN0LqEgDHk6y4GRIfePqds6VFjsFjHQqpW9YWcNNY-3iwnEaT7QscvzUB1XKg18WCwjPS2lffBCFuOOfQS6YiJejox-ZqORMJ-ExdLpt2ODTOTRL3Yo7WF1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Nano
🍌
²
Faithfully restore this image with high fidelity to modern photograph quality, in full color, upscale to 4K
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/archivetell/6006" target="_blank">📅 12:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6005">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">عملکرد بی نظیر جنریت عکس
Reve 2.0
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/6005" target="_blank">📅 12:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6004">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🎓
اکانت Cursor Pro رایگان برای دانشجویان  دانشجوها می‌تونن ۱۲ ماه اشتراک Cursor Pro (به ارزش ۲۴۰ دلار) رو رایگان دریافت کنن و به مدل‌های GPT، Claude و Gemini دسترسی داشته باشن.
✅
بدون نیاز به کارت بانکی
📌
مراحل دریافت:  1. وارد سایت cursor.com/students شوید.…</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/6004" target="_blank">📅 12:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6003">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🎓
اکانت Cursor Pro رایگان برای دانشجویان  دانشجوها می‌تونن ۱۲ ماه اشتراک Cursor Pro (به ارزش ۲۴۰ دلار) رو رایگان دریافت کنن و به مدل‌های GPT، Claude و Gemini دسترسی داشته باشن.
✅
بدون نیاز به کارت بانکی
📌
مراحل دریافت:  1. وارد سایت cursor.com/students شوید.…</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6003" target="_blank">📅 12:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6002">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚀
ابزار V2RayEz — ابزار متن‌باز عبور از فیلترینگ مبتنی بر DPI
ابزار V2RayEz یک پنل وب محلی و تک‌فایلی است که مجموعه‌ای از ابزارهای شبکه را در یک رابط کاربری مدرن ارائه می‌کند. کافی است فایل اجرایی را اجرا کنید تا داشبورد مدیریتی در مرورگر باز شود.
✨
امکانات کلیدی:
• پشتیبانی از Xray و Sing-box
• تونل SNI با قابلیت‌های ضد DPI
• دامین-فرانتینگ سمت کلاینت
• کتابخانه مدیریت کانفیگ‌های V2Ray
• اسکنرهای CDN، SNI و IP
• پشتیبانی از Psiphon و Cloudflare Worker
• رابط کاربری فارسی و انگلیسی
• بدون نصب‌کننده و بدون تله‌متری
🔧
فناوری‌ها:
• توسعه‌یافته با Go
• پنل وب داخلی
• قابل اجرا روی Windows، Linux و macOS
• متن‌باز تحت مجوز MIT
گیت هابش:
https://github.com/macan-dev/EasySNI
آموزشش تو یوتیوب:
https://www.youtube.com/watch?v=Y3tVfMqgys4&t=28s
#OpenSource
#GoLang
#V2Ray
#Xray
#SingBox
#Networking
#GitHub
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/archivetell/6002" target="_blank">📅 11:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6000">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🎓
اکانت Cursor Pro رایگان برای دانشجویان
دانشجوها می‌تونن ۱۲ ماه اشتراک Cursor Pro (به ارزش ۲۴۰ دلار) رو رایگان دریافت کنن و به مدل‌های GPT، Claude و Gemini دسترسی داشته باشن.
✅
بدون نیاز به کارت بانکی
📌
مراحل دریافت:
1. وارد سایت
cursor.com/students
شوید.
2. با ایمیل دانشگاهی (.edu) ثبت‌نام کنید.
3. فرایند تأیید دانشجویی را تکمیل کنید.
4. اشتراک Cursor Pro برای شما فعال می‌شود.
⚠️
داشتن ایمیل دانشگاهی (.edu) الزامی است.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/archivetell/6000" target="_blank">📅 10:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5999">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">کانفیگ اهدایی نامحدود از ممبر عزیزمون.....
🇩🇪
vless://6d3c8903-86c1-46e7-a5dc-b45823dec9a7@fmmgkzjac48e.dxdx5.com:9023?security=&encryption=none&type=grpc#gum0fyg1
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/5999" target="_blank">📅 10:54 · 14 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
