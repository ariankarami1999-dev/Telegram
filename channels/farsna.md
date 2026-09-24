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
<img src="https://cdn4.telesco.pe/file/LNf_NGgmGa68bjo5aD2m-CMOw4tjhd49sBT3fURp6kEb4yNRY1HbmU7dtVZ8o5h8vNFDBmSpDKmlfAj2SomHUmnIA3qLX3YcPTIpkvrE9ANRbqtxaQFWidahbc-hl8e6xpFqTETox49PCv4fCze1f_v_H3NE8AgWkpetv4Jiunl2UQ9iVoZe_c_9OmUIKWRlNTV8yvIKpmKBjOoF6sO1fJCYqdoASVcAaqZjUujMea9UWZb4X5A3JIwzK42_XbuvL6mULdPh93XkuIDTWvo-J3NJboIE6TqI_H7UGUeWn1v6sPtaOCJxbetA7ipVPWz1Za26yp_g3AXkOZE6R9mVyg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.79M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-02 09:10:22</div>
<hr>

<div class="tg-post" id="msg-464088">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbe6f0800c.mp4?token=B5KmlqBDflVvfYt8tRQq9RsapLN-vcFQkOnuG8ZaYhEMJ8RpQOIM9s6F_v2GNUcWqHzLOJyQwfZsH1Kx1tT5X6qb_9jLgzoe1HWVfw8QuHQdCJiX6nrcpzmALB096uzFHNV7jqfPgUTEE0X7c779C3oF8q3HmAkWvgbKWBmDD3IIqTW9X3R6karc_ScbnZVqGxadklY2hTs6zvI2refZ8wKTz0_ElfLRihzNLnkQusu8ZH8VjbHI3f6Hl1am0XdBmbXoZit6rBO3-D-Q4FDPRyExbaku-GAzPkyZRgYBgVNHFjn0hSQ7AvhSXLCZhgZdrnGBlEEB56NHaRSGYY8n3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbe6f0800c.mp4?token=B5KmlqBDflVvfYt8tRQq9RsapLN-vcFQkOnuG8ZaYhEMJ8RpQOIM9s6F_v2GNUcWqHzLOJyQwfZsH1Kx1tT5X6qb_9jLgzoe1HWVfw8QuHQdCJiX6nrcpzmALB096uzFHNV7jqfPgUTEE0X7c779C3oF8q3HmAkWvgbKWBmDD3IIqTW9X3R6karc_ScbnZVqGxadklY2hTs6zvI2refZ8wKTz0_ElfLRihzNLnkQusu8ZH8VjbHI3f6Hl1am0XdBmbXoZit6rBO3-D-Q4FDPRyExbaku-GAzPkyZRgYBgVNHFjn0hSQ7AvhSXLCZhgZdrnGBlEEB56NHaRSGYY8n3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: از فردا بارندگی‌ها در شمال کشور آغاز می‌شود
و تا روز دوشنبه ادامه دارد.
@Farsna</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/farsna/464088" target="_blank">📅 08:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464087">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e2cb105f6.mp4?token=FJ7HT-yH_aN2J30xIdIMUMHnC8iJYDJNveaf1UzzJYsu5t60CjJmzQ5Lj0CnB5YilBBuAK6d97_7EVlstFdKgXbYwySgohxLfcKw73lTjC6q54E9M3QXDFgtHZ8Lgixn13ZwLMSTGrTUNDPeQ7F2m_GhO9sVOj5-DZYqUvFTsQdIaCjgNZM1aXlJW--eNZlqiZFR0NFnrHkLtftfKtdjtl8oQZVsNWoBruHxf5CZn5bguS6RPUPPWJM0NKossZ4bfVNb_OZm_DmCKuRQd0sY-2rj1c_qDk4hFkP487-t3Hn8-RbcaTfjzu6e57PAk9-MpS6wx47i0UxONVNztEFZLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e2cb105f6.mp4?token=FJ7HT-yH_aN2J30xIdIMUMHnC8iJYDJNveaf1UzzJYsu5t60CjJmzQ5Lj0CnB5YilBBuAK6d97_7EVlstFdKgXbYwySgohxLfcKw73lTjC6q54E9M3QXDFgtHZ8Lgixn13ZwLMSTGrTUNDPeQ7F2m_GhO9sVOj5-DZYqUvFTsQdIaCjgNZM1aXlJW--eNZlqiZFR0NFnrHkLtftfKtdjtl8oQZVsNWoBruHxf5CZn5bguS6RPUPPWJM0NKossZ4bfVNb_OZm_DmCKuRQd0sY-2rj1c_qDk4hFkP487-t3Hn8-RbcaTfjzu6e57PAk9-MpS6wx47i0UxONVNztEFZLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واکنش سرد رئیس‌جمهور چین به تلاش ترامپ برای قدرت‌نمایی
🔹
در جریان استقبال ترامپ از رئیس‌جمهور چین، یک جنگنده در ارتفاع پایین به پرواز در آمد تا به زعم ترامپ قدرت ارتش آمریکا به رخ شی کشیده شود اما تصاویر نشان می‌دهد خودش بیشتر تحت تاثیر قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/farsna/464087" target="_blank">📅 08:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464086">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee735f735f.mp4?token=i5hJGov7ScXp3m9JjPJEtpTI0CXwUzECgWOPW2-PSFD-XVdvlwer79ffnFHC42mabWr-xkFeBC478oYPi7HgoZIg0nji4B16eNAyP-ScPLe9cR68GyDep_xmblUQDrmBcH6kPo0DI-EybxbPlFCopQDyuHDxngxC_-_iwlW7VKLEE0ntgqz-Q3ARxcip3vWwwk9bglNk68exs3l7-D0-GMmETBSoNPd9yQL-F-eMYJecq4SQ6qICR1OPA5eEl_xoITGNeCW4ht_u0ofF5uK0fwxaGXDrX9w3wypjwk_HKXO7Py3KxVz5IKJffzsy-SP66YQ9TnUvGxfoHHM8ZgLiQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee735f735f.mp4?token=i5hJGov7ScXp3m9JjPJEtpTI0CXwUzECgWOPW2-PSFD-XVdvlwer79ffnFHC42mabWr-xkFeBC478oYPi7HgoZIg0nji4B16eNAyP-ScPLe9cR68GyDep_xmblUQDrmBcH6kPo0DI-EybxbPlFCopQDyuHDxngxC_-_iwlW7VKLEE0ntgqz-Q3ARxcip3vWwwk9bglNk68exs3l7-D0-GMmETBSoNPd9yQL-F-eMYJecq4SQ6qICR1OPA5eEl_xoITGNeCW4ht_u0ofF5uK0fwxaGXDrX9w3wypjwk_HKXO7Py3KxVz5IKJffzsy-SP66YQ9TnUvGxfoHHM8ZgLiQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: ثابت کرده‌ایم که از جنگ نمی‌ترسیم و تا پای جان برای دفاع از ایران ایستاده‌ایم
🔹
بمب اتم در دست اسرائیل است اما آژانس از ایران بازرسی می‌کند. اسرائیل ۷۰ هزار نفر را در غزه قتل‌عام کرد اما ایران بمباران شد. @Farsna</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/farsna/464086" target="_blank">📅 08:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464085">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e440cbc01.mp4?token=bbFljElDWWOSF54Ciq6XuIQWGFYv3WI2Fx7lED1JrG9ZJevRoriyRVZDLss83I3TdEVGo9Ug7IVR4Mq7HU5FNbJ5ZcLqwnFDpRjxzLWGR-snEUZ3tiUuZFSknTPiL3V_SY9f4gM0LBwp87zjnEhNn2l0Bp548qh1P0ym56J80916nYtEOIsxwepeL9C0bHSIEBJDEI16jUDk3zIPNPi4gyBhxbadj--NiaC3EPUv-qtXChIhXSoGS2MEL-_Y-uqaQHjeP44fR0c452MLiip0QOhuZWb28CrRk6XqcA2l5RDSCBtRPA8ThN-O9pOvCqSHFmLaBzC0PT1rCxuICHYC9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e440cbc01.mp4?token=bbFljElDWWOSF54Ciq6XuIQWGFYv3WI2Fx7lED1JrG9ZJevRoriyRVZDLss83I3TdEVGo9Ug7IVR4Mq7HU5FNbJ5ZcLqwnFDpRjxzLWGR-snEUZ3tiUuZFSknTPiL3V_SY9f4gM0LBwp87zjnEhNn2l0Bp548qh1P0ym56J80916nYtEOIsxwepeL9C0bHSIEBJDEI16jUDk3zIPNPi4gyBhxbadj--NiaC3EPUv-qtXChIhXSoGS2MEL-_Y-uqaQHjeP44fR0c452MLiip0QOhuZWb28CrRk6XqcA2l5RDSCBtRPA8ThN-O9pOvCqSHFmLaBzC0PT1rCxuICHYC9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
افسردگی و اضطراب یکی از عوامل مهم اعتیاد است
@Farsna</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/farsna/464085" target="_blank">📅 08:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464084">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ab34188e7.mp4?token=jleMakeLuZzcS9U6nRIR2QKeCVQr7d53IkWA0RJ-Bz9MMUZt14g8J4SFPvL1dm8kpFaNfpCmTbe1UdTXIv1E9hbFKKafsHNpbY36db3wRHj0FU-YZzeAl6f8BeAWIplAqayRmWAqlNLxCttgQ5dnFxsI1x6IlQXm4G4ijs0-dUu3JI6jE9o3XHi_QV2WBk0Tw9n9IegXzNQEfRvLHRZiFoXE4iukAT8l9kqryTBQDblVoP28ora0eNZNTXGX4vrJWSEewYVFJAlmNptbWRGi4IuPm67bh_7alNEONdA9XrD4GEIELwENQ9qkc4wqEBqpJH5vR6li7yeSIELHpHxdoa-LdlRkz-Z6iTQNERvMZAT9ke8gZ_PXttBatKtDvyC1S13aVUc-9TQ5dd2jvhMEOWRrk-n__H2SetPXbXtoKi6YdH8FZ-d2cIiijWBK_0bDuJyMI8VxOGWSbzytyaIZerFkqDEBLwNpsQBCFQgoZsz5gT43cSQZPWwiX6KL9dahVd4V3TzF18dwYrOX40I3vVT1HNtMkp-gQtPwEidPbTUyPRUqf_6Kq0uSQrVNL7ea6H4GnBrAs6fr5CBTId-bCi1jwL0HHmaTg9nhl1JwzQ-GdXBP25F3BfILQrzbu-YGaQSyCoe4UrwnCTOxXlT1rzifFq3Xi7RN7JjX9C7fxA0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ab34188e7.mp4?token=jleMakeLuZzcS9U6nRIR2QKeCVQr7d53IkWA0RJ-Bz9MMUZt14g8J4SFPvL1dm8kpFaNfpCmTbe1UdTXIv1E9hbFKKafsHNpbY36db3wRHj0FU-YZzeAl6f8BeAWIplAqayRmWAqlNLxCttgQ5dnFxsI1x6IlQXm4G4ijs0-dUu3JI6jE9o3XHi_QV2WBk0Tw9n9IegXzNQEfRvLHRZiFoXE4iukAT8l9kqryTBQDblVoP28ora0eNZNTXGX4vrJWSEewYVFJAlmNptbWRGi4IuPm67bh_7alNEONdA9XrD4GEIELwENQ9qkc4wqEBqpJH5vR6li7yeSIELHpHxdoa-LdlRkz-Z6iTQNERvMZAT9ke8gZ_PXttBatKtDvyC1S13aVUc-9TQ5dd2jvhMEOWRrk-n__H2SetPXbXtoKi6YdH8FZ-d2cIiijWBK_0bDuJyMI8VxOGWSbzytyaIZerFkqDEBLwNpsQBCFQgoZsz5gT43cSQZPWwiX6KL9dahVd4V3TzF18dwYrOX40I3vVT1HNtMkp-gQtPwEidPbTUyPRUqf_6Kq0uSQrVNL7ea6H4GnBrAs6fr5CBTId-bCi1jwL0HHmaTg9nhl1JwzQ-GdXBP25F3BfILQrzbu-YGaQSyCoe4UrwnCTOxXlT1rzifFq3Xi7RN7JjX9C7fxA0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رزمایش ۴۰ هزار موتورسوار «جان‌فدا» جمعه از میدان امام حسین(ع) تا میدان آزادی برگزار می‌شود
🔹
ثبت‌نام علاقه‌مندان تا ساعت ۲۴ امشب در مساجد و پایگاه‌های بسیج انجام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/farsna/464084" target="_blank">📅 07:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464083">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">محدودیت‌های پلیس برای ترافیک پایان هفتۀ جاده‌های شمال
🔸
تردد موتورسیکلت‌ها از ساعت ۱۲ امروز تا ساعت ۶ صبح شنبه در محورهای کرج-چالوس و هراز ممنوع است.
🔹
تردد تریلر، کامیون و کامیونت در محور کرج-چالوس همچنان ممنوع است. روزهای پنج‌شنبه و شنبه درصورت افزایش حجم ترافیک، محدودیت یک‌طرفۀ مقطعی در مسیر رفت یا برگشت، اجرا می‌شود.
🔸
از ساعت ۱۴ روز جمعه تردد خودروها به مقصد چالوس از ابتدای آزادراه تهران-شمال محدود می‌شود و از ساعت ۱۵ نیز مسیر در محدودۀ پل‌زنگوله به سمت چالوس به‌طور کامل مسدود خواهد شد.
🔹
از ساعت ۱۶ روز جمعه، مسیر مرزن‌آباد به سمت تهران یک‌طرفه می‌شود و این محدودیت تا ساعت ۲۴ ادامه دارد.
🔸
تردد کلیۀ تریلرها در محور هراز ممنوع است و عبور کامیون‌ها و کامیونت‌ها، به‌جز خودروهای حامل مواد سوختی و فاسدشدنی از ساعت ۸ تا ۲۴ امروز پنجشنبه و جمعه امکان‌پذیر نیست.
⚠️
امکان تغییر محدودیت‌ها باتوجه به شرایط و حجم تردد وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/farsna/464083" target="_blank">📅 07:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464082">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nR7fgY7ZBLEByIrm1waOlBpuxu6g6GWlYwbBgkVsHLkNVsHT-bGRPiTUqbK5GYfJWWf5S1NwwMfMxb_rL8tux-RU8pWnupZu9LBV5hrNWvAT-cfZY9a9gVXrIeP7pjVGRLwvEgLCJDi8LOzQgYd6VBkhyCjiOBR81KsJRZCK4dCLrVZMSySTniyAR2mXOWhc3kGOQU94TM35Wf8ihSOTmcqFhyooiBPFk2VRlDcjpiVvn_xDKxd6MJB6aIfbYLGYTCUccQ_CtF-ffHptQzI9JaFOJXIdOBtamDTuNpZYvH7gSd1YVj8E2NU2Xaf2ajPvHMLT7wdzf9f0-_yUnQCFWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش دورۀ آموزشی سربازی متعهدین خدمت آموزش‌وپرورش به یک‌هفته
🔹
متعهدین به خدمت آموزش‌وپرورش که از سال ۹۳ به بعد تعهد خود را آغاز کرده و هم اکنون دورۀ تعهد خود را به اتمام رسانده‌اند، می‌توانند دورۀ ۲ماهۀ آموزشی را در یک هفته طی کنند.
🔹
وزارت آموزش‌وپرورش باید قبل از بکارگیری فارغ‌التحصیلان در دانشگاه‌های فرهنگیان و شهید رجایی، برای برگزاری دوره‌های آموزش رزم مقدماتی در مراکز آموزش سپاه اقدام کند.
🔹
افراد واجد شرایط باید با هماهنگی اداره کل آموزش‌وپرورش استان محل سکونت، درخواست اعزام به خدمت خود را از طریق دفاتر پلیس+۱۰ ثبت کنند.
🔸
سایر متعهدین آموزش‌وپرورش نیز باید قبل از شروع تعهد خود نسبت به ثبت درخواست اعزام به خدمت و طی دورۀ آموزش رزم مقدماتی از طریق دفاتر پلیس+۱۰ اقدام کنند‌.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/farsna/464082" target="_blank">📅 07:22 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464081">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">هوای تهران «قابل‌قبول» است
🔸
شاخص امروز کیفیت هوای پایتخت روی عدد ۸۴، و در وضعیت قابل‌قبول قرار دارد.
@Farsna</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/farsna/464081" target="_blank">📅 07:11 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464071">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XNdmp30wrclqkhHtkLIoej-vArOOtlEEu5kTzSF39gu_cuO_2ZjXdx1Z7yDPWc9dx6Mhu10c7JeBXQTY8cRBb-B82OrGCdSc3ACbeGc1YWofh6wfvbb3HZlE9ndMFErJtXp0nHNhEIfNp9LjPpAxgQ3DpC0yJOKiPse2nVXekfolGGV2x9D-x6ErczBMZwX9hcMDKFrSO3gxk02gjorgoOncUGbG_dy6cjCx0e2Y1r_7btOqWsg99RPwlyG26V60cjliT6-b8wbNqa6JLVGRmzlBkG0SB-X_rnockIlFH0qhKgWzAHcMPtKV5pO1Yz-91SLOjRh_XSH0Pi6M-Gnytw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RXj40naIzQ9itxm6OAhQzGr9CellEp2KX9E9cFXjSlgKkkweaFIe_hFahyvg0PBQmWd6Ukba3T_Mi8nP_QhtiWFnGLprbfKtcwdjCsvwvbFwI8iwThQiqUPXI4LRZg8hbblKtqyEBdvp0jYuBXDAVLfC0FX94QUYM_genG0hLGpe_CFOn33jGJdJqxWTYKXXqPtqX-rK_K-7IIVRO_Nijlz1e0jm7J_Xwywth3QGsonQDpzmXe59-a0WfAl9IQJmGkPoUmCFNU7bBj9xSd9-40hm2hYNUsy5cuH6LEc5SBctd2tjiq8y0vN1kfOJTspd6Z-yXVsMmJkBlDmNBVuApA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MdcDMuC5uZke5v-jY5DSO1zKgy6KLjVo108zwB8GSaQrl6R7kxaM4eyNSB3MjrZL3C-JAXanvMm6B18RFh5edGkK7LShc5cuOU5JgErNHtQAp83ptXFWV7nGTdYX7OueOKKvaTWrjErGoEXaZnljeqp5ofPah8rvIMZpKblbh2kJcuCwlZ6UtomUD_7zzoAsdk5SjtPEth8jhKKoCAvNpGrM00p6V-tYREQpdfQ2Yul3ekAkEKBFMZsyW7tivdBytjtplQV0eV2suzT-NiqRAp-3TlOW2Jm3rNEwD9awXMv_8Ix_p3rwahhVRmO1In_wCFKkiMKCgu3A9-cgJKYGQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ppDSHYQuR-Ft8OkaAE4xWui64ML_wR_F-P20SHJplMsI_-0IAfkMRZ0wElMJmmdP-HDBnxC9xFIOWUhPmHQs613yQg8KBnhRbh9qbDjyhJoa5gJqwFi8IBjxz9wY5Rqb_-odtDWRsQ1Ik5f2lBPDQjSnuYdz6AC54Hi8gEz-CMoTJZ8fQmX6j4qhl1V23v6wHtJXa4sXC53m0TysfTHWBecqLUPEIyjpbFRrV83zpv8ReXkNsPZH1Mbjv6imCMTQyv-_8qf3h22sWYAgX9TM9v15uPU2r0P3TmXX64R60HhrjK6iLujo_nltS9tsPolR4Tv49b7Rvfg_Gu3jSCSueg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y6-f8s_nYf0NjW4zg21BK5rUzA6LUbyaXM3-2gbVTmJvgPSNHT0DMal9fndgG8IrE_WH7NHcfbYWDAnGcHcnNFzBHRLVgWWr324rNHCgSnlZlFJMvcXwtaZ-2k_p0qxS-AyEISQQYF73gfVf6BdVuoA2C3xtT6ZBGkAkd6VIMLJwGWi1ZItfEya0qkkxOWVCvS22YjL50cygprpXtUDAiGYOYAwWvwSpkBS9koFEgqqmMG9EFfmg-w41JXqRoaGpXY8rAqNYxzQDjLDbu_Dt2rThVnYyqw7Ey_cKsvkxp_we8m2_rErFPNO2d6q6oIBKfoP0ZfxdjFXKsgDfNv1D3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J1HdJ2Htv5I22HhjgSLSQ-5MfVhpiZenCR0zuL9ib-Rkhgm8LmjgnLRHJoWomsFpip2OjO1YNOMwapEOE-lkza5BeHuQisnWErodpMpqLVHDOKSUNf0QTKVudgPvrAe7u5ePFB4oS9AUVfhKG2FEOfrPwjx0D_3a2CMQnp-S04bf7P21Bh9L5L6PsXR_p1sAtsoQhc_tUVH8XElxCI7sPEtl1oworg4VnpBV_2dEVXnw1P-Q_10zCSJDuRibwQvEszvQrKtlJqgKwhjHScA_PGxDL0UvjCiQ2CP93_7h5DwI8E_blosSQ_slfHBk6a5jjSRskQJ0peXYviggtofNIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JVEa2hQwLXbm31AspnGUup2MHpds4NneLYrVNcmyRcibNg_g9GDvc1AfYbGZps6VfD44j_sN3M0FM5YJsRDdz4NomTRbx_bQ2zHpazxMB5BZxyE_2QVBYooDFXRxTyIrq26vw9B4JuMRv7aL9FMSC85BMI01M20ZXYsLJy0tDUNRxDSRVp-CdpPFhGy7eB7dUZ5a6whk2K-6YvfqJlR5f0kuDt_gqcHjxWLBbKqfKsHYT7bI4oJVDpUGAs2sSs2I5Oanc3zUwDCK4gomhgA91lqCIVbOgzSG0va3ti_Pi1pGsW3rp8JRwXVRFlhnngxyeTmBUN-XNiz4dKnQ-QLvOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uy7TLEBXuop_ZFqSzY0KMbuhXQ2I6_5O4VnUAq_bO961YJhbCVnSjY1ZlzRFRWEJ-4RTKHXD0C4oTkniibznh6LofFgTki-NrXpj7QALIVQwWn6aC1WmAnOUrY4bW23dkrn9Fg85dpS4SLXfMoRqD0fmQHfXHtiiYwFUS4OZ07WSlKOHmx0AXLtKiJx8JiGzFvUriRy4jSYzX2DaRZWbSKdDHwKX31k5tHTwF2uN8Mcl2dZUd-6mxUwUiZO2m40yZalEnIUdOkaitaJoGOQU4R2wVskq6kQxd4XYfSOR1S3LpVg5vfKAWaKwyWT05lWQQkpqiPxAqK6Y8dUBzKqzgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UISc-GRQ274iPT2-HbzG_odUafoFDo4BMbblQ6LAOBBqG5dP-DSQMVFLAjKRCwV1QG22L3TPNyRWqWq5o6wbRU4H2c1l419dZetwrxsRDXbAk9-yPOKATS_TEl9AxsJCTiViWCKfr84WreFRIdqs7prfFJ1mZNJ6JIQQYswt_vQ-i3nlpSAUa6kYrWcuxUm89IlZ2c_6cJzh8jhUBOYYljNqI0k83kIfCCYCGWyfPSk8Ej2TLo_2OYRcLDpVvnIDpBCqQvMup8plmuG7Gq-zosOH_emQ8j29ml3UAaUfEWNi8tsEmlUFo4OTcSJS04ZmhbVW_ckGMhDvZ-3pPI0oaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
برداشت پسته‌ در خراسان شمالی
عکس:
رضا خبازان
@Farsna</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/farsna/464071" target="_blank">📅 07:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464070">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcakAyiw3rVsDZVvcVKDqeHc9uF6KbTnJ2kUU0OljcSDbcMkiJPnE40mfeyoeQJwpGYBe4xkJSxvTv5megaUBavQvqykuuuz4ArsgvcKXmebkfbYikXPP7ScO5ptYITuQTKPnQ1uAT6HTh-hVpIiG2m9z56rVaZDJn7TKSH3lbT8w19BnzEPIdZki6nnWpZo65_do4nSY5mj_A-AMPhb4cwB-_91PmsGImwEyY7XtyW30i9_5UYd_rROXqSQx29nCK4cOuqSTbgW5LI36bSqF3VUHc9-I8HdrCQii_rx_GUfUnkFxOxmYsdQdUmqtpWVzBRRQg7npIjJYDebF6TRsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی امواج، پیکر نگهبانان خزر را بازمی‌گردانند
🔹
فوک خزری نگهبان سلامت اکوسیستم خزر بار دیگر دو پیکر بی‌جان خود را به ساحل بابلسر سپرد تا نشان دهد که توازن حیات در این منطقه بیش از هر زمان دیگری در لبۀ پرتگاه قرار دارد.
🔸
با کشف این دو لاشۀ جدید، آمار مرگ‌ومیر…</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/farsna/464070" target="_blank">📅 06:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464069">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhhTWfIkDOpsAo-7sNjp5u0CxfzAkznH-FNCXAuyGkkreATVyJhKUSMBCE2XYPd08DJmn80UFKwFsr9l_xGu8OoE9XDWxON8wGPCNOl9ubfTraZ993RHRxX0G50swFj2pR5eN9S581tLfiHJ607611pPULOltH9xlR52lQcHlplgXnCFB2QQLpnJdFVGmv6SFCmJDiJ4iCDN7Vid7RdoSUUyeY_da96nL9954rMTYTXzK3BscF6V7MWj3TL_Fr7y1SF1-C6i_JHwqrbS8R-7_mV_lZhwdVVxfjXhH3wVIjv4Fi5EtTCoI-Y1EVkipVxcozrwUyaCv2leYmiUrbDJpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش بقائی به اظهارات نخست‌وزیر کانادا در توجیه اظهارات جنگ‌طلبانۀ رئیس‌جمهور آمريکا علیه ایران
🔹
سخنگوی وزارت خارجه: نخست وزیر کانادا به جای محکوم‌کردن تجاوز و جنگ‌افروزی آمریکا در صدد توجیه آن برآمده و تهدید به از بین بردن یک کشور را به‌عنوان «زبان دوران جنگ» معرفی کرده است.
🔹
مارک کارنی باید بداند زمان بی‌رحم‌تر از آن است که اجازه دهد توهم و نفاق برای همیشه ادامه یابد. روزی به آنان که زیر سایۀ قلدری آمریکا ایستادند و گمان کردند با تکرار زبان زورمندان می‌توانند خود را از گزند زور در امان نگه دارند، نشان خواهد داد که چشم بستن بر حقیقت و فروختن عزت‌نفس و کرامت، آدمی را نجات نمی‌دهد؛ فقط او را بی‌سلاح‌تر تحویل زورگو می‌دهد.
🔹
شاید آن روز به ایران امروز نگاه کنند و بفهمند کشوری که روزی برای کوبیدنش با زورگویان هم‌صدا شده بودند، همان کشوری بود که با ایستادن در برابر زور، مشعلی را روشن نگه داشت؛ مشعلی که اگر خاموش شود، دیگر چیزی جز قدرت عریان میان انسان‌ها باقی نمی‌ماند و راهِ متمدنانه و انسانی بشر برای حل اختلاف، زیر پای منطق بی‌رحم زور دفن خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farsna/464069" target="_blank">📅 06:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464068">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEX-GsT4Z_0nyAbZmjDUNxudIbqL1tZJ4lP1i2CPu9RTSpOryzqT3wGHqeTwuczJvzT2FXJkw7yAKQ14RQsVa4-cv2x-gWH4-gizLVOY_0xIxXtaiPRFRhixYxtPu4XXa8UAOO6BwbHYR0Q9h5863XOVPXeb5UlyExuScTeBOEPpDw1k7OsWos3yq6mW2fhWxtDVO85m7mZLzjIon348wIbWizFd0Ap7s5V9DWvJwyTli5i86HacF-2na_7GJlt3kvEu6nSKvoBao0qeTyKPD69vTB_LhgTKhaa13A_EQj4dxKvJYQVQHrerzExJOQabBy7MMS_r1Q37izvY5kS2SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست‌وزیر اسپانیا: نتانیاهو به قتل‌عام در غزه ادامه می‌دهد
🔹
نخست وزیر اسپانیا طی سخنرانی در مجمع عمومی سازمان ملل متحد، به انتقاد از سکوت و انفعال این سازمان در بحران‌های مختلف جهان پرداخت.
🔹
پدرو سانچز در این‌باره گفت، من برای دفاع از اصول و آرمان‌هایی که الهام‌بخش تأسیس این سازمان بودند، آمده‌ام. اصول و آرمان‌هایی که توسط دولت‌های مختلف حاضر در اینجا نادیده گرفته یا تضعیف می‌شوند.
🔹
او با بیان اینکه بنیامین نتانیاهو، نخست‌وزیر رژیم صهیونیستی به کشتار جمعی و قتل‌عام در نوار غزه ادامه می‌دهد، گفت که من شاهد بوده‌ام قدرت‌های جهانی، جنگ‌های غیرقانونی را آغاز می‌کنند و مرتکب قتل‌عام علیه غیرنظامیان بی‌گناه می‌شوند.
🔹
وی در واکنش به تهدید آمریکا برای تحریم دادگاه لاهه به دلیل صدور بازداشت مقام‌های صهیونیست نیز گفت نهادهایی مانند دیوان کیفری بین‌المللی باید تقویت شوند تا کسانی را که قوانین بین‌المللی را نقض می‌کنند، تحت پیگرد قانونی و مجازات قرار دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/farsna/464068" target="_blank">📅 06:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464067">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‌بانوان ایرانی بازهم طلایی شدند
🔹
کیمیا زارعی و زینب نوروزی در فینال دونفرۀ سبک‌وزن روئینگ زنان ایران با زمان ۶:۵۳.۹۳ اول شدند و مدال طلا گرفتند.  @Farsna</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/farsna/464067" target="_blank">📅 05:41 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464066">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGhXJoEvXX-INAEE8QbsE7gacmI_tGQ80OsiOhhZeCe85h9pycbc133goCE62J9hgOhAin5Dt0OTIs5EHwzADkSubCemWDzDSUrixuUSDU2M3A_1uzs0J5mXdOr2zWUSjcDFILR5mVrO_qX7lLVqX3VrajtFbzzE6ablcXsO4YaztY-7fdX6ggG1SxUxrLlQU10KPwDLDOe8UjgLhM4y5OVHVpaSZHAxMPk5886VijD1X4sHbE1-_Oc5Zy9CNkCobKfNxHQ0srcrWf5iams8WqweGBa7EG4HcJEbroBxfbsyx_J4Kmjl1jyzSbrXxkKZlZLSyYIbdix-okjJ8U7e8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
دیدار پزشکیان با رئیس‌جمهور سوئیس در حاشیۀ نشست سازمان ملل  @Farsna</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/farsna/464066" target="_blank">📅 05:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464064">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPKpRVttooIVJ0qbwfSLR4YU6LYROATLqVfQPCBO7aEfaV093VMWd-rHJWvN7-AOJSkjZtwz7VdyuhfuytjbhVWKDMx0O4h6V0BhBigiCW2TeaF4NPdPOgSVJp3uwqQufizBJl1yELwdpWm3y9Iae9JhHIHn_mulGRlQtAgkc0ohLtvNCYLEaBY7HMq4Q6reWviu5JQeIGOCwmzZrP3-UsQHCu8Lx9KFI6ybSpiFXsxLx8xO41ZMdTShB3wPdLnn-sY6b4wZqXLZYKjy1p8vMsWmdj1z5OeRSp7aZKzXmJdKy2MoFSr4C7VA5dchjB8QQjSkGWOzgbxICm1v2kzPBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هت‌تریک نقرۀ ووشو
🔹
عرفان محرمی در وزن منفی ۷۰ کیلوگرم ساندا سومین مدال نقرۀ تیم ووشوی ایران را کسب کرد. @Farsna</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/farsna/464064" target="_blank">📅 05:14 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464063">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWTr2EzTU7sIIDcN1-8ZLz25UZsZa5O1tF4Wm_oSZ56f-7ymXLs-LHPWbJWLPxuZWR5ZDx4t_6P-SErVsWZRmSKzkRkpyt3Oc_Gg-RDEafSPTdJh8NUW15o-Z8u2awI3J141KTQL9Pui1_fmafCxq4OUwGzuK9SQH2jvzcWWG730RzBtFJcyth2FwPvYaguZ02AszFHj2IWrVstonudf2T8WG21SBuM7zIiQIAnM3m1hK5lbigAjnXrTHEqF1SSqLohypBZKlgmq4hiZOWD7lCUtPMuVF-d0QcJkvaNgcheIfnAdn13gf8m6FvFqC9O5buJ7Wg_GVc8dtSGbYSdEgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دومین مدال ووشو هم نقره شد
🔹
شجاع پناهی در وزن منهای ۶۵ کیلوگرم مردان مدال نقره کسب کرد. @Farsna</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/farsna/464063" target="_blank">📅 05:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464062">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ffd249604.mp4?token=HRABiKoKW1fgjjSm2zag3xEbyC6lnZpg0Vfkzg-p4vFN4lk9klB0VinKwDDw_cPwfcxJ4IH8NcRrbk58OjPrDNoNjDmKPKf1MbVfGjsn5EAVaEFNIudG5_uoxxR5xx-am3JWcn7w_j6ghq4ipn71R2f7PVMkBF1LvzTOlXWUNG8gE1jhoX3a-duAsh8Rk_OKypkCgHTGGsIlTrA3qXOJCF0plEY89AjrLxY8m8tZtusyIJ90MKIXlw2e2GCOlPZ-P7yDrA3EQxKmA5VXY65xN2olx0APO4lSbzD7F1i6MRKWxR_un21EvhHsuLQFMxLQG44ezchyO3cdW2iTz87WxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ffd249604.mp4?token=HRABiKoKW1fgjjSm2zag3xEbyC6lnZpg0Vfkzg-p4vFN4lk9klB0VinKwDDw_cPwfcxJ4IH8NcRrbk58OjPrDNoNjDmKPKf1MbVfGjsn5EAVaEFNIudG5_uoxxR5xx-am3JWcn7w_j6ghq4ipn71R2f7PVMkBF1LvzTOlXWUNG8gE1jhoX3a-duAsh8Rk_OKypkCgHTGGsIlTrA3qXOJCF0plEY89AjrLxY8m8tZtusyIJ90MKIXlw2e2GCOlPZ-P7yDrA3EQxKmA5VXY65xN2olx0APO4lSbzD7F1i6MRKWxR_un21EvhHsuLQFMxLQG44ezchyO3cdW2iTz87WxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاطمه مجلل: مدالم را به دختران ایرانی تقدیم می‌کنم
🎙
خیلی خوشحالم که توانستم پرچم کشورم‌‌ را بالا ببرم خوش‌رنگ‌ترین رنگ مدال را گرفتم و از این بابت خیلی خوشحالم.
🎙
مدالم را به دختران ایرانی تقدیم می‌کنم. امیدوارم تمام دختران ایران در همۀ زمینه‌ها موفق باشند.
@Sportfars</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/farsna/464062" target="_blank">📅 05:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464061">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bztDUrEtCrYOZAZHBuVaAEHSKZx6BC5jaqcauU97VH0nudVvRnd7aRq4U-ZPG-n7ifKsVsErnifGL9qneM_qu5qOXXmeeNf0mqlItfIa5GaWPD7bJHEBvexkyj_acXv914AO_Qdm5XAGiTPuRHWoX89Q7FiodHEtBvSYz0mJNwVMA8NuvBm7f8k3dxt05KfiHpMTxLXY_13JaxqKMtr-NNnXvqBvP8gV60W_8vKEqiyS9lRd_pR26oW5RtmdTb3YXAH4fi3hK_-Cy5HmPMCvGAloUsZS5YFohRSaH9_GENwUV0m6xiHM7NYwxUR56rTck6JNeMPb872879Hs_SymFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانوی ووشو کار ایرانی نقره‌ای شد
🔹
در مبارزۀ فینال وزن منهای ۵۲ کیلوگرم ووشوی بانوان، سوگند سینکایی به مدال نقره دست یافت.  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/farsna/464061" target="_blank">📅 04:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464060">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/311f23114b.mp4?token=TggbOJkATxwfJxSVDGX8NJNibKBZgDPZ2y7D1XnHFbyHHrvG0ckQmuD2u88RbNcEy69XNKvo9cOOM_bblp8p4tdKuPKHEwRedmHN5tozTYQ6UxBK2OFtAeVSqxx0Hmzf6FZVunOHEjM5NkruTmgtPPfGyr2GIGWbSN45RsUoprWBgpODZnuc8IpnqZ6BuGoJk91MFioR5EumH3LyVurSWeLjRthbzW1MxFEYeLHOManpx0GCjrx4n1ZJu3Z7eUWTwSSV1Z_zmtllPIgyYVOHSDI2pAB4HxQcs-3NNMoSAfSK4r_z-JoSCM65BRqpiZ32FqjtLP6CBPxhPe5s4DJgjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/311f23114b.mp4?token=TggbOJkATxwfJxSVDGX8NJNibKBZgDPZ2y7D1XnHFbyHHrvG0ckQmuD2u88RbNcEy69XNKvo9cOOM_bblp8p4tdKuPKHEwRedmHN5tozTYQ6UxBK2OFtAeVSqxx0Hmzf6FZVunOHEjM5NkruTmgtPPfGyr2GIGWbSN45RsUoprWBgpODZnuc8IpnqZ6BuGoJk91MFioR5EumH3LyVurSWeLjRthbzW1MxFEYeLHOManpx0GCjrx4n1ZJu3Z7eUWTwSSV1Z_zmtllPIgyYVOHSDI2pAB4HxQcs-3NNMoSAfSK4r_z-JoSCM65BRqpiZ32FqjtLP6CBPxhPe5s4DJgjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراض فرماندار کالیفرنیا به یاوه‌گویی‌های ترامپ دربارۀ ایران
🔹
فرماندار کالیفرنیا به یاوه‌گویی‌های رئیس‌جمهور تروریست آمریکا دربارۀ ایران در مجمع عمومی سازمان ملل متحد اعتراض کرد.
🔹
گوین نیوسام در همایشی در حاشیۀ اجلاس مجمع عمومی خطاب به مردم آمریکا گفت [ترامپ] تقریباً خواستار نسل‌کشی ۹۳ میلیون نفر (کل جمعیت ایران) شد.
🔹
وی با کنایه به مشکل روانی ترامپ، گفت این‌گونه اظهارات عادی نیست! هیچ‌چیز عادی در آن وجود ندارد!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/farsna/464060" target="_blank">📅 04:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464059">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dfoPaEdvgQKXUdb8RKCEs7sVUpw0NF7pa2_85mCwQGMCJP5NERDe8W6nL0RdZea6BRnqVIkxqp6wAdyzgvqthUGlm7vyCbA1Cr7niY3sDNgk7XEOn_97Pa5gVCodLGkNmrdTqFL8AKSVBDHJ80NjYDkhS9j3bjkPNmQo1RFyr1v-tA4T8QRklfxUvP6Ei_dSY5Vwzwv3A_J1gJE9mHCIjGZTl5WgaNdfVY9bj3-ADvV3nOlwMz7Hdx9rDeLjwBltsxXwv8w0GNML5kBXFSPqWEOR3KjBdDnr7j6ff8OkuacmNIVRf9elkPFjmqFhqX2SxGkE0nSSF0iQQEsR7pQD8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانوی روئینگ‌سوار، چهارمین طلای ایران را صید کرد
🔹
فاطمه مجلل در فینال تک‌نفرۀ سبک‌وزن زنان با ثبت زمان ۷:۲۴.۵۷ به مدال طلا دست یافت.
🔹
این اولین مدال روئینگ و چهارمین طلای کاروان ایران است. @Farsna - Link</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/farsna/464059" target="_blank">📅 04:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464058">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حملات هوایی پاکستان به ۳ استان افغانستان
🔹
به گزارش منابع محلی،‌ پاکستان حملاتی را به ۳ استان شرقی افغانستان انجام داده است.
🔹
همچنین گفته می‌شود قندهار به‌عنوان دومین شهر بزرگ افغانستان، هدف حملات هوایی جنگنده‌های پاکستانی قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/farsna/464058" target="_blank">📅 04:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464057">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNQk08lTMaaq5DGfrJ4DcJUS29I-CWgpsVI0jaVf6h3TXgxdphzQDaY8MtgUGYBRyb0ZoGWHvJ7LefT9XQ8m5APNvGIIhawbLyWGEi7HHpxqhtJz5OLmyq-nH0PlBVE5WZmS4-aHmUuzvxym6rMFczu2j3TH_b1Lg0rZbDUiXiW6ypAU6o1GF6WfRlb41_WzBWgvXb5c7rOYXJwiJJookD6PnqtJl6gvP8ojiZ8zdTr9002sIy-hB1f5PF3j5eMKtzlVQL5eAsLFttNtvVzdsetqKh2Eem2DIvEFyTYGoufCreSQNL6LPE-6bn-GF6ciO57np7I5xnS85rrIiwGQmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانوی ووشو کار ایرانی نقره‌ای شد
🔹
در مبارزۀ فینال وزن منهای ۵۲ کیلوگرم ووشوی بانوان، سوگند سینکایی به مدال نقره دست یافت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/farsna/464057" target="_blank">📅 04:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464056">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAp2hYf0-ZUIC0UKyTik2DW9olbs5t53fRWUG0e7TRjddeQYRsFpz2chdxVYNyVqUVzR7CVw92uChahgvUpU31b_6S9G7Eqe8U8dmfTst9LMEfkR0CH3GS2_a-unLarh4VfDQfSyecDClOyTEc3lXJAQGo-BsKiLxJAmfJPqfVyNfwQW6nnQ69fijTQY0aN2kWIFPoUyc8DDukCh41m7HE7T7BrWEpHNuHi2U0G4jkCtxPb__MmBHbN3ucOjoqLBqKTrrNSReybBcP_GqguDVBzZvtAbOPegjFAdsa8A1x5X6SGwp7EPhfOLlxz0oRwannfyqZv78TuCnAAgPCglhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان در دیدار با رئیس شورای اروپا: دخالت دولت‌های غربی امنیت دنیا را تحت تأثیر قرار داد
🔹
دخالت دولت‌های غربی باعث شد امنیت کل دنیا تحت تأثیر قرار بگیرد. اگر کسی دنبال علت اتفاقات اخیر است باید به رفتارهای دولت‌های غربی دقت کند.
🔹
انتظار داریم کشورهای اروپایی در رفتارهای خود تجدیدنظر کنند و استقلال خود را حفظ کنند. ما در جنگ اخیر از برخی کشورها بی‌عملی دیدیدم ولی بی‌طرفی ندیدیم.
🔹
اقدامات اروپایی‌ها در اسنپ‌بک و برجام، و قرارگرفتن زیر سایۀ اقدامات خصمانۀ آمریکا باعث شد از چرخۀ تاثیرگذاری در تحولات بین‌المللی خارج شوند.
@Farsna</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/farsna/464056" target="_blank">📅 04:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464055">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd1704d80.mp4?token=ObOiUxffWyDjR_VONPqoyhe93UEyn6NANkrPHznJ9zqd5me2cSxVZYlPf5WDc5QqDsGHzwUthGBpJFx-427gkevd8abASxzzmAgPKbi8_Qf4HzXLpDpt7-Gd9uptrP0U7cXHUqXN6MpYftTd3LnosVIkCrlpZCKrzY_y0Sq9SSGg-6A8pyJV6w08V89XSyDiz8_fQudNnNa3wCFsHr6R8npBccvA-n6qUx6p6dt21JQba3HRDdAXbKBqWcxYLyYmkeRqX6OuAeTSjjhVTZsWvgoisCoYGM4hrQuCsJnrantVRum_4pHlR4XGroIuYJB4ngtjjTat8IUevzabk0KYWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd1704d80.mp4?token=ObOiUxffWyDjR_VONPqoyhe93UEyn6NANkrPHznJ9zqd5me2cSxVZYlPf5WDc5QqDsGHzwUthGBpJFx-427gkevd8abASxzzmAgPKbi8_Qf4HzXLpDpt7-Gd9uptrP0U7cXHUqXN6MpYftTd3LnosVIkCrlpZCKrzY_y0Sq9SSGg-6A8pyJV6w08V89XSyDiz8_fQudNnNa3wCFsHr6R8npBccvA-n6qUx6p6dt21JQba3HRDdAXbKBqWcxYLyYmkeRqX6OuAeTSjjhVTZsWvgoisCoYGM4hrQuCsJnrantVRum_4pHlR4XGroIuYJB4ngtjjTat8IUevzabk0KYWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیدار پزشکیان با نخست‌وزیر ارمنستان در حاشیۀ اجلاس مجمع عمومی سازمان ملل
🔹
پزشکیان در این نشست گفت: سیاست قطعی جمهوری اسلامی گسترش همکاری‌ها با کشورهای منطقه و همسایه است، و در این خصوص دولت همۀ تلاش خود را برای اجرای توافقات به‌کار می‌گیرد.
@Farsna</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/farsna/464055" target="_blank">📅 04:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464054">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GreMoxUcQKOaOUM8fCWS0A1ssieISeC9yCVP-dXpLL9HJ0LrJbQw_9L9-gx2JV29GZokfaLIPGU_ePT4b-V4oHw7PMgIrk40XMMzUo1nhQEqKMsdad7BLsDEvOckEn4f14p1WswifquFH7a1SjAaVa-9hXjk10_4_LKW6J2Z4CF5iHqmalSpLxA6mvq4DENNP1IPxKH5_PTsi8JMyVoKp0HbUgZyecwFfbkcxx_DsTJ7aPWxrnsRaGOuU60by35TaRH30VGxDoGNeQj5Xa9MC23mkITB1MgE-0i_0YtsM1wjztsLPhSJC1-DCGPoNEFOsSPUEWT7LLMoPExC-EnuQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانوی روئینگ‌سوار، چهارمین طلای ایران را صید کرد
🔹
فاطمه مجلل در فینال تک‌نفرۀ سبک‌وزن زنان با ثبت زمان ۷:۲۴.۵۷ به مدال طلا دست یافت.
🔹
این اولین مدال روئینگ و چهارمین طلای کاروان ایران است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/farsna/464054" target="_blank">📅 04:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464053">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">انفجار در مقر گروهک‌های تجزیه‌طلب در اربیل عراق
🔹
رسانه‌های عراقی گزارش دادند که مقر گروهک‌های تروریستی تجزیه‌طلب ضد ایرانی در شهرستان «سوران» در مرکز منطقۀ کردستان عراق هدف قرار گرفته شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/farsna/464053" target="_blank">📅 03:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464052">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c61e7ff434.mp4?token=QgqKySbyNrIIUNjpSiAvjTNKjY8IWIKYLFtoMc10c7IPR601ZNPWzOxnjb7mqYTTW3LWRM-yTRBO8iokszLq6XtHa8Ve_uurvTAr63J89W_HuMwkyf1JUV2yKgLNja0wsUbiJ5BgVxoZlI8UMA9EDb-6qDdf24BzGB3OBn_NBbd7IrytOP4GnKbeANRzOCqxXKcXzF5VNlhRpk_WzQggx-_32sIlWsVczp-70coGn1_tizyHu9hnvBDwCvIlC000G9JYS38DfGTePz9RrMCju7y5PR9vax-NcD0JU7CUobS4gxJJnsxoTW9Y3xcf3aQDTYOkOeOegHjDldN_0Rfrgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c61e7ff434.mp4?token=QgqKySbyNrIIUNjpSiAvjTNKjY8IWIKYLFtoMc10c7IPR601ZNPWzOxnjb7mqYTTW3LWRM-yTRBO8iokszLq6XtHa8Ve_uurvTAr63J89W_HuMwkyf1JUV2yKgLNja0wsUbiJ5BgVxoZlI8UMA9EDb-6qDdf24BzGB3OBn_NBbd7IrytOP4GnKbeANRzOCqxXKcXzF5VNlhRpk_WzQggx-_32sIlWsVczp-70coGn1_tizyHu9hnvBDwCvIlC000G9JYS38DfGTePz9RrMCju7y5PR9vax-NcD0JU7CUobS4gxJJnsxoTW9Y3xcf3aQDTYOkOeOegHjDldN_0Rfrgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خدای ترسناک
🎙
حجت‌الاسلام رمضانی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/464052" target="_blank">📅 02:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464051">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGglC3xoF8SKp5e_H-TKqYWLMhXrQbQWWSaiVgsbX2q2x6WINzcPsF6CnwyVpp32z2qNc-ckyEVXNxk3imO4PHxcMyP94IjwTShpruPC3oPDJTm4IjPPh_AOouEX25ynBeGa5SiKKeQz7Ygzo0xbcGickFexxGavrQdG5LUlf2I1aCKZ1DtdY-N7Bo81IsrpgwiQGQl0dxXQrWJG8_b8V_WMrzC7fKnzuDqljjg-nVs8E8x8Vdjiaxw7kyn8Aj7Qh7n9CPYjwPVykiEfe917vAhkAWiQ23z4eHvzCVi5Ls5BkSOBEJ7cAlKhiQ55BiOPm3N-BIAR3ox1Ghx94zxKEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تأمین‌اجتماعی: بازنشستگان نگران پیامک اشتباهی واریز حقوق نباشند
🔹
سازمان تأمین‌اجتماعی: پیامک اشتباه واریز حقوق شهریور برخی بازنشستگان و مستمری‌بگیران، ناشی از اختلال در شبکه بانکی بوده و حقوق کامل افراد امروز به‌صورت خودکار اصلاح و واریز می‌شود.
🔹
برخی بازنشستگان…</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/464051" target="_blank">📅 02:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464050">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/464050" target="_blank">📅 02:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464049">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">صدای انفجارهایی در کی‌یف پایتخت اوکراین شنیده شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/464049" target="_blank">📅 02:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464048">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">انهدام انبارهای تسلیحاتی سعودی در مرز یمن
🔹
نیروهای مسلح یمن محل استقرار نیروهای کمکی و انبارهای سلاح رژیم سعودی در «الطوال» را هدف قرار دادند.
🔹
این عملیات، در واکنش به حمله هوایی دشمن سعودی به منطقۀ «مقبنه» در استان تعز انجام شده است.
🔹
از سوی دیگر گفته می‌شود که نیروهای مقاومت یمن حملۀ بزرگی را علیه منطقۀ «التربه» آغاز کرده و جادۀ تعز-عدن عملاً غیرقابل استفاده شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/464048" target="_blank">📅 02:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464047">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34fc1c6bbf.mp4?token=R_Mnoknm3gbW8Gj3TXK3fcweFJNf1UwD33oI-PCjOtCyJAZMVzdBJntZFQVgUUOxllfYlRYg3OpJ45Y_Au0YeHueyWnkYZO-O3HxWL8L0Ja-WyTOoPHdnsX3tRfZYdYqsDI_07BzF7QjT9b_PqPKgcYPcM2eu7awHjWCSDnO1RgeLoFFADfMVrS3U2hpbmgLaHZMZETEjNscoatksLraDzKhpD55J5EAeN2oSO_Ag3DdSoXW2tFDr8tUBuYhNB8xcwyipYaF--BdEesAM3Q6Agfp43vGItxd8ClvILvnjYHVjXe-mAyKrDIO12knea7hPoi4FIP7ku2HVMneHUWCOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34fc1c6bbf.mp4?token=R_Mnoknm3gbW8Gj3TXK3fcweFJNf1UwD33oI-PCjOtCyJAZMVzdBJntZFQVgUUOxllfYlRYg3OpJ45Y_Au0YeHueyWnkYZO-O3HxWL8L0Ja-WyTOoPHdnsX3tRfZYdYqsDI_07BzF7QjT9b_PqPKgcYPcM2eu7awHjWCSDnO1RgeLoFFADfMVrS3U2hpbmgLaHZMZETEjNscoatksLraDzKhpD55J5EAeN2oSO_Ag3DdSoXW2tFDr8tUBuYhNB8xcwyipYaF--BdEesAM3Q6Agfp43vGItxd8ClvILvnjYHVjXe-mAyKrDIO12knea7hPoi4FIP7ku2HVMneHUWCOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استقبال غیرمعمول ترامپ از رئیس‌جمهور چین که برای حضور در نشست مجمع عمومی سازمان ملل به آمریکا رفته است.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/464047" target="_blank">📅 01:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464046">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d86ca3127c.mp4?token=oenI0bjloo7FZQnUmGCZ-0Gx8u3Lc37Pf4lhOclCAVLJACl6MzXkgR0cRXJFrY4CtkH1sT8_xGzYXZEjTfysFez84zNc-kI2SP61lSotqlCFxwpJELKJgG5Y8N7AwqbGy_jsHydgtM_EsV1UE2xsPDdcmj2Ak0iwlas65lID9FhMCh_3rzh5gPdXN7t-xJsrZii2DZOEnokvCIiLWx6RadlwkWPwjmoS9rK7SytwCCIb8O0Zod75C6mUdAX2ZoitcEJuWnEMBKjIRr3ofFwNsWEuP2mBqHTP1ZSWYkh_TgGmrMGGKNX0XzOKHQl8-VasNF14hv6xQzcKQOXO_67MEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d86ca3127c.mp4?token=oenI0bjloo7FZQnUmGCZ-0Gx8u3Lc37Pf4lhOclCAVLJACl6MzXkgR0cRXJFrY4CtkH1sT8_xGzYXZEjTfysFez84zNc-kI2SP61lSotqlCFxwpJELKJgG5Y8N7AwqbGy_jsHydgtM_EsV1UE2xsPDdcmj2Ak0iwlas65lID9FhMCh_3rzh5gPdXN7t-xJsrZii2DZOEnokvCIiLWx6RadlwkWPwjmoS9rK7SytwCCIb8O0Zod75C6mUdAX2ZoitcEJuWnEMBKjIRr3ofFwNsWEuP2mBqHTP1ZSWYkh_TgGmrMGGKNX0XzOKHQl8-VasNF14hv6xQzcKQOXO_67MEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
هدف‌قرارگرفتن یک کشتی در تنگۀ هرمز
🔹
سازمان عملیات تجارت دریایی انگلیس اعلام کرد یک کشتی باری در داخل تنگۀ هرمز با یک پرتابۀ ناشناس هدف قرار گرفته است. @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/464046" target="_blank">📅 01:39 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464045">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0165df036e.mp4?token=D2lnYzFvT9oUsaDC8j-oBMQjmIPgIRAXusc4f0JtbeIo5av5yFSw0PkdoUHX6fj6ekMjtXpYwTuYVJYiiyLl2MXjClLDF6hZ45-XOg_b9FsKG_Aydt-rvavrXQONcfM3aa9CH0_ZyliSfbU8UbetZ2xP-aa8i9s6ZR6Si5EhN08ol_tGNIVIAmXnke_4v5Pkovhxm_DnkAg8WBCtwp8d2v1r9M5VlIRzQIQkcCeDP3CAB9YYg6X_g1lkSS4b83VkiBB5d1CX01uRL9o2Cnv04mYeOM3150_t8km7VbWZWcDTyjXmrQKUK3OSFkXOqjvOBSoldRCzxnSwtLhFbGPSZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0165df036e.mp4?token=D2lnYzFvT9oUsaDC8j-oBMQjmIPgIRAXusc4f0JtbeIo5av5yFSw0PkdoUHX6fj6ekMjtXpYwTuYVJYiiyLl2MXjClLDF6hZ45-XOg_b9FsKG_Aydt-rvavrXQONcfM3aa9CH0_ZyliSfbU8UbetZ2xP-aa8i9s6ZR6Si5EhN08ol_tGNIVIAmXnke_4v5Pkovhxm_DnkAg8WBCtwp8d2v1r9M5VlIRzQIQkcCeDP3CAB9YYg6X_g1lkSS4b83VkiBB5d1CX01uRL9o2Cnv04mYeOM3150_t8km7VbWZWcDTyjXmrQKUK3OSFkXOqjvOBSoldRCzxnSwtLhFbGPSZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پادگان آموزشی جان‌فدا در پایتخت افتتاح شد
🔹
در نخستین مرحله از طرح جان فدا، اولین مرکز آموزشی جان‌فدا در میدان امام حسین(ع) تهران افتتاح شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/464045" target="_blank">📅 01:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464044">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec50b856cb.mp4?token=v66aRA8ntIAT78OZm8VDkUssxiUkS2wXMRmiEvTQLD5AvZ_NDzK69b10lzV-8bSmupykleXk4eD8HTwlSk9nqg7FE_JE8nc7eUgG0mIpuX5TjgdlqyGLQO2rPptpoYZZcSwb8Fw9ZOUX5Mtq9h1za3q9OkELZB7cfCVxN1SIjGK5ThySZW02UA4HoaxsHoPv7FnbcsMODUuU7CNBLxCKVT02OUeNpZSrzxnhkNmT3T7SNCU4nNFYaPwO3oWBopWSd4TXB5GoRVNIapNydawB0zxTbba7W42MmPcX-XiGdI6GfmahiEHL5eMBQh2yALM6LJMjJIq_LpAM-YLF05Qr2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec50b856cb.mp4?token=v66aRA8ntIAT78OZm8VDkUssxiUkS2wXMRmiEvTQLD5AvZ_NDzK69b10lzV-8bSmupykleXk4eD8HTwlSk9nqg7FE_JE8nc7eUgG0mIpuX5TjgdlqyGLQO2rPptpoYZZcSwb8Fw9ZOUX5Mtq9h1za3q9OkELZB7cfCVxN1SIjGK5ThySZW02UA4HoaxsHoPv7FnbcsMODUuU7CNBLxCKVT02OUeNpZSrzxnhkNmT3T7SNCU4nNFYaPwO3oWBopWSd4TXB5GoRVNIapNydawB0zxTbba7W42MmPcX-XiGdI6GfmahiEHL5eMBQh2yALM6LJMjJIq_LpAM-YLF05Qr2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ملت قدرشناس از مواضع پزشکیان در سازمان ملل تقدیر کردند
🔹
مردم شامگاه چهارشنبه همزمان با حضور در تجمعات شبانه، با سر دادن شعارها و در دست داشتن دست‌نوشته‌هایی، از مواضع رئیس‌جمهور کشورمان در سازمان ملل قدردانی کردند.
@Farsna
-
link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/464044" target="_blank">📅 01:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464043">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0vJeagRnRvsU6v9WOGyHan-nYpKo8Wst_QTQqIM39QpgcjsW0b1zLztpT7Z_VoLsaZa5FkwFlsbRLOvdE63lz_GtEWWbDEVy2xixMBJOKc2TNIAjalv_gvde7q9fmeADlFYKV8OWtEGYfzd9P3jRWPMXJpFe0duoUYtuAJDqypVAo95m7jusv6V1IQWXGwoRv8iRLnp-EpIy0fmhh-So_QJ_jLEHFRyjNJaLDDz4FXAtVMlBdLfO-ZSxfbJDP_IQtS0UkvlPyP0g5EKxirKfAFjfQRTKW6SphUHNHdoPhKyyyljxT9Et4B9xv9wUqpnQ2UgZPSJeaWHBMXQ-RBpMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهش قیمت نفت با سخنرانی رئیس‌جمهور در سازمان ملل
🔹
نزدیک به یک هفته ترامپ و رسانه‌های غربی تلاش کردند قیمت نفت را پایین بیاورند اما سخنرانی چند دقیقه‌ای رئیس‌جمهور در قلب آمریکا و هدفگیری یک نفتکش متخلف در تنگۀ هرمز، نفت را گران کرد و به مرز ۱۰۴ دلار در هر بشکه رساند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/464043" target="_blank">📅 01:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464042">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3ZlJ31BXujMABHClyvDCKHWL2p1gjLRETZ1W-tFgbHdOvo3P4FMVj2HoSMkN3shYlbWmE4yFPDVC_j52BcpCn4EqQzu3lWXw87SYZfESCs-fXv4ubCnpo9fr8HVVWllguPI5FFGfK-QMi_9mxrZImpAvJ78t_zBJV652seGprBOH8f9-QO3rGfInw_7wr92K3XNh4RUoz6EGRML_DQC6FQvkUcJWkwV6OLNVRwBz7spkzB7CTpJEzz58AYJRa4X8tvtBCXYcOj0ijUb6dqE507wnhliAXjVG3Hpdg8WNWCaZrqc2wBil5aTQ8LoQebTXPPMvZqx_zE8i9eQW_qZ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خودکشی ۸ خدمه ناو هواپیمابر «لینکلن» حین جنگ با ایران
🔹
شبکه «سی‌ان‌ان» بامداد پنجشنبه گزارش داد که به نامه‌ای از «هونگ کائو» سرپرست اداره نیروی دریایی در وزارت جنگ آمریکا دست یافته که در آن به اقدام ۸ نظامی حاضر در ناوگروه ضربت «لینکلن» برای خودکشی، از ابتدای استقرار در جنگ تحمیلی علیه ایران اذعان کرده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/464042" target="_blank">📅 01:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464041">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DiHITOsUTxwyihGt6wRhkKyjAx42_ZktfUTB3s6Rb0RUcn_ByoG7t8P1soGG8IQU_1Wj2MdrPPFfMlxOU38juVyF2PDWZRNMXrIYyytlLj08ceO6yqfvE3PE2QITbenEngUgOSWwxAU7uqlRWTHN6MMvXH9TRWto8dFTSr9u2PRBaITANKxHPRyBiy6Qe5CMwVIPnU1zpLppH4DsNpH8OQ15VaTmfi70fVmZIunka-dZWnbI4IjhrgIkqJJvIcBbX6zCy-Y2IGEkO78guQ-BjsRmyGDoO2JFEYmfkZc46z1nxKIV8zuTzwNt-VzCqg_EDzD9Hz5G1NlorNM6MMM1yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات جدید از افزایش اعتبار کالابرگ
🔹
رئیس سازمان برنامه‌وبودجه: فعلا برای حدود ۴۴ میلیون نفر واجد شرایط پیامک ارسال خواهد شد تا با تکمیل یک اظهارنامه شرایط آن‌ها برای دریافت این حمایت مشخص شود.
🔹
افراد تحت پوشش کمیتۀ امداد و بهزیستی، و خانوارهای مورد تأیید این دو نهاد، بدون نیاز به اقدام خاص این پرداخت را در مهرماه دریافت می‌کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/464041" target="_blank">📅 00:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464035">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fck5R3u4EgU5mfafFsPxHWmmlRyX8-H3ZJHBj0CRPOhaog-B4CfKHJxAq0l8t4fMIQEvRnhooV5qFOtRm1enH_mkwRVH-kLe2rD5j2tDajen34q29WbwO2DGoZe_b-7s5UcD0Z3CBNtnv7avxQZVhdW7_pJHZ3IALsL6OEwaunR87CO9_swYx6EZNhV15ma9afgpzJd5QIHFtfl0Sdmymo2YrQUTF5TpJQlkm3KAjNtFucrxfZJqR864WHPI_dH-rvnuASj7lMR1-VP5JEX-AT-ibkdzx7R8EqXvZPEJrw6V-uDXqeWhRCkSpiA-Jeps3krtWuZ-jjBzoUvhwtZfEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N7JZx2WUkS2N9fuWME0eVyeD7VWcptqQydH-aazLr5Ct-80_hV_ZGUZOdtKuICT9JkTPNEyAVa7Q9_0aN9-hm2SRaxDlHKz3VxsZv-0ykVBoszMw1cugEygW84TMn46wFxDtOq8qE6O0YVmxZCbWRsK71qvMbiNDmdJjEb-4d5afcvjt4TT9ZHi4xuqyv_gfyytXcM3BkvQG_s30LjfahK1EVQEfB8psRbYJbirmVZUKOyNqMGCfZ1tac6G17bRp31XbIOalSHFojTZPNIaprmLNHMBjXkMD2HZoxq8Cg_uAszfd9AmavtZK4fvBof4sUpf_iMrhWAXqcx09m_Mpnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X_8hAgoFxfe1talg8aRW09kBFTpcDsBPqBvPv8GlOfseZhIbUUizpEkje0f2v5U09pnEG9wbMBBPm9hzVVEg38A0e-B5ro876cmSYvMbjeVHzzDkmQUWBwKa3JxCjZcvfR1zAMNhWaGJQYKwV-dWANpOSIH5R0xSs3681_eFleeT0rAvLns8BadOl-S17qRLrRw6ggE6QcrKwVLeN-_dbqnz8okedtLpOR05j3RUQuCofBAAeAYuCq5O0jInPTO-S3nXwveO0lBpiiFDtVck-WtitZdPGpwtHjCPp26Z7yVbEY_PqO-rsLiGtld5yl77mTyZa3HznSUCCqHRtSbyUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OhzYZ5atKfHLlzu-wJgiGyLt2z-YuI16kngcKyVcACtgsOARNRnhGx_wT7QdUPV2HYXw99koP_i_0tI4isBLZnyHVNkJ5l5Zyp5OP7x3Gn3UIQct99ddFI1GaADVMScZbFzh0nKBQqVJ9BnyIl7vWinEXH21NZ7Hlu79_nv1eLafgSYTzR_uaL45n4c1si1UzS0urFZE-gt4vOpHSunis1LjtHfIp84l-SUc5nPfSXWc2KNrFY9frEFQGBt_mmqmEQUT_XDk2VRt2Paf3dA_3WqRcfvBaeknBwm-l1XhrSgnH_sCJHwyK2OQoOMQu2hMH0oFiaXH1pQl_ENH7G6Bfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TXW4Hf5br1Kxb_Ph7FYz_AJlTn350ZDjY8slee3V53U-H5bGb5Ma-G_QxB3BGzYiV6zVJBqxiuvT2oy__FVePAG4xKR4nDCwstH31o4TmopPbcAYfDH5--8YmXYn5MucWaDOEMFLLEkG8wbZQJLu92fvObHp6wxeNeepqdwWUazUZeWvTr1fOKGLOJLWlvmSb3-uM-i8sLoliXj9fQgXVtZzKz_x6lUHReyhV2iMb_KTTQ4Ri4u48Fvdcsf2RCMehunc4_tGQCQdD0bva2EsC_O9Oo8UqzGXKgI2D0_NMmmFZn0H14Dy0VdQfhtSVrx0jqmUwkd2_zDoLRZ08BbKWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HGfoNrjpBa22utkjKYL_EldQanX_hzAckAVuO_gKimJC3EICzA_bvm5YwMbUoueOuKhyF8oZt6KZE_z5GCH8mvjg158qFquTthkMWPdcSQc6W5HU4Ok1Ud4doM6XR5S_fQB7j-3rmajPZrsVm7HCOWXM5ac0YwQhf2Q800nK3J1KnMavuCx1TKHCFaoqP-5MWrFOVYx50yRICSue8Ea6nKtH-ITg7GIDLROfkG5KfDedbFne2OtC2FzrGqP5aAkHxv5BShiuRYQwzetjIlPMEKmMFki2GzhtEtPAGRP0NGQbXIe-WlPJz_GqfrVmUJIEzGkN_QhNKEttRFTgphGJrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عکس‌هایی متفاوت از جنگ تحمیلی ۸ ساله که کمتر دیده‌اید
🔗
هریک از این عکس‌ها ماجرایی شنیدنی دارند؛ از
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/464035" target="_blank">📅 00:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464030">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ErVCY4qtsmBvAzPZrjbiwHggefu-5IlreSIzrl4qA9TBalpOMxLYZAPp0FNPFOdleE8tM1nfO_b9tlYcgvV_118mE_UOUUx2IPO55NYllu3t15zsYM3j4H14ABt-_baTr36eSm48mDTfO_Xb1hY3YYQdtkgm-_zI7GIHGCTp5LYrt-XAHbO7y-83Ox9YPyI6YD6KHcVeqQPskARQAehy4Qt2jzCorCX6y6S9mSeTERyK7Ji5dhjKTmobNBkqTqvC9Qmg301W13kjDIPdWtUs_QkH7QGIoSZmSYhIpbXg40HGGkyNqu4VAH0k3TDhVKpr_sHex4En_2MbBsoGdDXdLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dUH8K6ID4Vx3qqmDGyZip2YpS7_2b6GXv3p3ydkLzbdjoyZcalcfqeKiBum1zWY8asoRGn96cxGQg-CGFRnGLIXEMSbRxECjvnTznJ1H6ozOKAgLu2IBdQ1rNKpcRDDcYgWPDm3THHGLwj8tiguKnadb3MoI3yijaFayONRVzNsqknXCHjItvMXHzFoYSh0Cd6QzMjZ56cmiRNYumPF_orEoL2ylsmFWoFQAbdDld1zXMv3PtpszX0KPIq50OwrwlhTrI6oZ5QLNW52TtD6g45lu7310R_wDD4zFCUgbIAnzUC_9776L5BEFF42WSQ0dlTl-0qEZbsyCfpejQXhnsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nPYyQ91JQwEfVo9qYA49klwZL2-ykZ8Z4fP2-Fw4lMCbl2miS_M-fCgsCIdu81Ir7IIJE6_xGE3fF_GGo26_4o58FZ7aJBbErir-G9IylzoiivjnRGcF-CqtfP5VywimtBiaX4gGWk9XLnVEjR_eNPYoWQSk4FfPieyYQYUYRMDnBvEtDOKt-YVBcOSutqBMnltDIpfQ9TLjqlW0mBnxXNxjSdB38gpMCIzBxaszO9Us-kmXdXxnd1vPC8RtHP3FblV6eKXoNv8ka5Wu7wCtw8C3hHp_knFZ6xevme5kbarXZvvMzAzvLIqth5tN1viW-ljPm8PP67l4DDm7Oh5ZHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ByiUbDgaRttvEF88EMoYrx4u1U9TI20pMdkFF1R5VAq6USkklCUpZHuu3Dc5ZiJ5aQ5FT1sGJUhX4TNAOwAq6JdcOgoFZhEkRz8hoNV_uazkK7xyv9cx49rxt76AMROWZblssyvjtQl9Y02trtnlA9mhCYZ4zeFhmIls2B1F21pYs_YKfuaM1x29JI6T-Mh3UGzuCrbPX-hMQfur5sJV5DRGLz_o48tbwbr0fA92DrjytKzhJG-9xOVDSalp3UPNNVPrRZ2eLZ4T4YorSmZDgP7qyQGepZEjCb06njThhmzOIQVD6rt12mv3B5oMzVpBqUi7yd1zyRGxrwHaNTH8Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qI7RMGIpNtmacyDrvafJfXcILdUpkAs94_KNZWILafsBU_0V1-LBJ7nuBU8tnLqgxvaM83SAQBGWTrCpLohOq0TeGReyGZcoN6OuuaLqesw3kRCvpqqZWrP8eLDA7MahhbhYf6c0QmccALBX4Owk3OY0iN2ru72izf7bPoBps5w3FDlodp8VhUpDypHhZxoRe97VFpvKfIPoWqa1vLwBRv6OHmeBRNmsRB4qen9xRsKJWj9mhSVXqaqCBub3sQ5bVNUTj20a7V6bwd6aI6EaGY7CTniM7kGkI_X9K4KuMOVZ3Y2xRST_priQHZvtLchrPhlzSU2CSlEp9KgESnsJtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
پزشکیان صدای ملت ایران بود
تمجید شخصیت‌های مختلف از سخنرانی پزشکیان در سازمان ملل
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/464030" target="_blank">📅 00:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464029">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kEnXeGzQfe7c8ehNmIuBdcmDttf3Bkuw7YttQNN_Cgc2S-k051aJGWc79ubkYNClQ4nlEXJmBW7iwzBnCAXcOSqfuOuhNaoJNli_FcoGxxEE8O_DfpGzqGJTFRq3ZsZkjtyQPOodF58BsGT1TaSLmeT8lmGqkTwN6a_6Ex7oOzxEOSx430kNjZTBgyigAbkCkDI-vQbS93p7pAfgqkm3H8pW5MEkwLEOEywgyhwZ2p_fQU6jPFMixgPrdCeXD2_vcqJTJZ9O1aaL6Z3Y8ikgbphTvHhsdfuqAa24wMYHiD81Cn4lEBTiHzd447tqyshu-oWcjBmxsPvEi8sWq_ya1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدادعادل، مشاور عالی رهبر انقلاب: سخنان دکتر پزشکیان چون از دل او برخاسته بود، بر دل‌ها نشست. به‌عنوان یک برادر و یک ایرانی از او تشکر می‌کنم.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/464029" target="_blank">📅 00:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464028">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vx41geQi9tjLXRz390owKB_kFbnpSRYXLlMrH6Tkd-nyAAydFumO0k0cfP5VyXsbAjNOf5N4ZkSf1OEjjc47tn-Tey5HXF5dxWrqVxHsPz052KLgvmkVOLvY4yanXuAHbdpJ6sh58D_QdAWUS6jDosOChqqZYwq76ZvHRXSucsD3yl9ePs8_bh8rVKOtp10NXFJoI2T_NF3fVJtFwQ-eYZejT9bAUdxyZ8q6AmcK2s3JBQe06B84xhLWV_HkjoGpVbGh4grcRy7aeNebvuUHm1WdrL9D_uR4BmKXS1kbRwhn4cET5mRbHhs7jcVlgBxpsf1Lwpa-Gz81Jb7Fib87Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انسان ناتوان
🔹
شب هنگام، سلطانی بسیار خسته بود و می‌خواست بخوابد، اما پشه‌ای سمج مدام روی صورتش می‌نشست و مانع خوابش می‌شد.
🔹
سلطان هربار که دستش را بالا می‌برد تا پشه را بزند، پشه می‌پرید و دست سلطان محکم به صورت خودش می‌خورد.
🔹
این اتفاق چندین بار تکرار شد و پادشاهی که بر کشوری پهناور حکومت می‌کرد و همه از او حساب می‌بردند، از پس یک پشه کوچک برنمی‌آمد و به خودش سیلی می‌زد.
🔹
در همین حال، یکی از بزرگان که از دور شاهد این صحنه بود، رو به یکی از عارفان و دانایان حاضر کرد و پرسید: «حکمت آفرینش پشه با این جثه کوچک و آزاررسان چیست؟»
🔹
آن مرد دانا پاسخ داد: «خداوند آن را آفرید تا عجز و ناتوانیِ ستمگران و پادشاهان قدرتمند را به خودشان نشان دهد؛ تا بدانند با همه ادعا و قدرتی که دارند، حریف خردترین مخلوق خدا هم نمی‌شوند.»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/464028" target="_blank">📅 00:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464027">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2071160e16.mp4?token=LXkiX_uNYfsRTIOlnWu_8MN8dhb51Zx3hzKvJ5_JR_nt6QmOIsI0Tvt0nyXUSnjLFXq0AjLG_DIWoFbUdyqFFPq8I7NzTBTg1u8B3Xcu15z-SEjnQoQnpw-U-9QGayScvYQ28JcZKlpYL2QufVepfPdYmwf-mj4Zkjt24dzAUBZOZ3HZvsletEyJcooEGf3KaECqcno0VaxlKUiUMV6ts-WPG0f12omxqdj6PXT7icPUDgDEw9Dd36rhSvAdv51qVrGWZO8HDzIh6z_Q_46iFZAPZOsjm6Xnt-8nQczdzLc5oS7Bq1pqO7pXcl02YLQKzEpynqAiMTMyN48SA22m5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2071160e16.mp4?token=LXkiX_uNYfsRTIOlnWu_8MN8dhb51Zx3hzKvJ5_JR_nt6QmOIsI0Tvt0nyXUSnjLFXq0AjLG_DIWoFbUdyqFFPq8I7NzTBTg1u8B3Xcu15z-SEjnQoQnpw-U-9QGayScvYQ28JcZKlpYL2QufVepfPdYmwf-mj4Zkjt24dzAUBZOZ3HZvsletEyJcooEGf3KaECqcno0VaxlKUiUMV6ts-WPG0f12omxqdj6PXT7icPUDgDEw9Dd36rhSvAdv51qVrGWZO8HDzIh6z_Q_46iFZAPZOsjm6Xnt-8nQczdzLc5oS7Bq1pqO7pXcl02YLQKzEpynqAiMTMyN48SA22m5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ارتباط زندۀ رئیس‌جمهور از نیویورک با مردم در تجمعات شبانه
🔹
پزشکیان: قدردان مردم هستم. دعا کنید شرمندۀ شما نشوم.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/464027" target="_blank">📅 00:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464026">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1c2n5mq5bKf_rzMkAQtc9pN7jlZkuuOHVA-wzlkMn9OWJmRGrpBwGgOifCNiRuFKGv68hztkudRDfcXsmKbdbzdxXiTGP_UEOzeYICf9et0IyqvwmGdp14tbcBKHAGIiFzUsTNuC5I6QRXFC4ylWYIyYyNZ80egiznDmZga89qZz2Zvzg5yosh0uA28dc8X1sv8oNfCIv0DnyuhEzPmfJ86wX-5Pv4tKpK7Jpb3m4RK9TfMqNY_aklRXd1EKsloaIr1PkedhQnEUgTgdcgr6WmANEYMhW1qSiE4gBQqEc5zREz3ItAQz7cR9hObdGtKtv-zF2rofingV5o2XSqN7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سرلشکر عبداللهی: مردم ایران با دست دکتر پزشکیان، در برابر دیدگان جهانیان، به رئیس‌جمهور جنایتکار آمریکا سیلی زدند
🔹
رئیس ستادکل نیروهای مسلح و فرماندۀ قرارگاه خاتم‌الانبیا: سخنان رئیس‌جمهور اسلامی ایران در مجمع عمومی سازمان ملل، صدای رسای ملت مبعوث‌شده و سربلند ایران بود. مردم شریف ما با دست دکتر پزشکیان، در برابر دیدگان جهانیان، به رئیس‌جمهور جنایتکار آمریکا سیلی زدند.
🔹
نیروهای مسلح، همنوا و همصدا با مردم و رئیس‌جمهور محترم اعلام می‌کنند: انتقام خون امام شهیدمان و کودکان میناب ادامه خواهد داشت و تا زمانی که آب، خاک و آسمان ایران تهدید شود، هیچ کشور متجاوز و هیچ‌یک از حامیان متجاوزان، امنیت نخواهند داشت.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/464026" target="_blank">📅 00:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464025">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1b916aa5f.mp4?token=ce1GIeJtsJCn-iAPDiyvVy3p8U4BtRZ7zswyzjN0-Y_-T39mmUH52wkYr9D167p9Yn0pe_BG-orJ6kKH9y1prmr5pwYZI__HqJkmWxVc5_L-_t7xDNUHtUGzFoVjY4x8etQlZeXX-_dXzTnDgWQeWJXz4wePwJFAWNnrUclGDRF7JNoyKm02cAh7KFfYYP-svKzD5EA-WybOyKNovaJnc5DLlyMzBzzRNRbr8pnQW28IjSYrihM_JtpnDX9C9qZ7JXDrH6KN8G9hKhwoH1rL5YUMI3K9ZhywfZFD40oPu7OMZMLqX8sktAO5iG67Vfy8_OjzSwlM6OpTtw_QxRTqUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1b916aa5f.mp4?token=ce1GIeJtsJCn-iAPDiyvVy3p8U4BtRZ7zswyzjN0-Y_-T39mmUH52wkYr9D167p9Yn0pe_BG-orJ6kKH9y1prmr5pwYZI__HqJkmWxVc5_L-_t7xDNUHtUGzFoVjY4x8etQlZeXX-_dXzTnDgWQeWJXz4wePwJFAWNnrUclGDRF7JNoyKm02cAh7KFfYYP-svKzD5EA-WybOyKNovaJnc5DLlyMzBzzRNRbr8pnQW28IjSYrihM_JtpnDX9C9qZ7JXDrH6KN8G9hKhwoH1rL5YUMI3K9ZhywfZFD40oPu7OMZMLqX8sktAO5iG67Vfy8_OjzSwlM6OpTtw_QxRTqUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهردار تهران در تجمع مردم بندرعباس: هرمزگان امتیاز ویژه ایران است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/464025" target="_blank">📅 23:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464022">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qx5YhQHXNqVj3d3Xq_dGfetsqtp9kn8N3hjx0qZsx2otoss6gGw92GlwpK0hj5OIgzMLwUEcuuwWC_oMlxdfnLrwxHqjYNC3m5XKS9Szexf_hnxJqXLU2SntQqyytZqQkzlz27tbXMMxbrkOx1-X-inrStC6b3D1SxsKED0GI4WKzofROJZmHo5XPjwa0QmzL_l3QBMIZhWcV54xO8_0inoZ4s0WmuwgSor5r6tS6QFv3o9b3rgmnlKKIstR7dBuX5Q51szeNkG_aQbRVOKRY-EzDwtpvgsWMFpd70DsRjC368HZ332PY-7r3PFeQ_XRzuqRWkAJ_-sGtqSaL8s_yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Prj6IUfyT9DPZtf9-wHpZOWjnSDK_9yVSpORSWC3FEEaKKf4iMIdSs14vh2jbKrev2b7hUMoDjwK8jeB3C3_geBhO36MFsIBc2itSpk49K4dXe8dlqbWvZWXLIVdIeVLAN1SfWXQrFPnPDHN0VdK9EzX1I_L-vcznmD1NTdmvARcRZVvahVwC-2O1L28qumQQsgnVKLpuyZxBwukj5XGOqTIgZ5AJJmu6KJT3qaJ-nZrd0vYzJtwJqMLEoOsy4nljTZ9ThpygdgCvS0KQeF9ikde6YljzYP7Y0rfhJMMqPBhORVjiSpfDv1yRv8uWvfuczkmH_0iy7yhhOUNtTD71w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">منابع خبری لبنان: جنگنده‌های اسرائیلی به حومۀ شهر القنطره در جنوب لبنان حمله کردند.  @Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/464022" target="_blank">📅 23:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464021">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-JfFbna1vJ6ddSj6qOSVMmnSUYXCkpHNfWde_BZNs1PMdxMr02GkO3l8joxUJ3V7cTkNH8ZdiB40eigaAF6JreHkJxv5MNbtB9YKwGsOA1u9I5RhvXSLG89RxRi6-6-IAQgze1fXYt_Wy-xJKbMjP7xYE6IX1N7S8856w6OH52y11MVnejbSFGXjRyE3uArDbvgoVzKjoa1fMTLYZ2edizTKM0NVzhd1h4CVwuNu3RU-m-ppuOKKEfoVxgEkj2c0XNKsimTvoaR8havC-_fdK3-N05yklPrex_VYbexU8m_cT2uBgecUXh3jPuEZieu7i9S6le8B4XquVSJeltC2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ۵ کار را به چت‌جی‌پی‌تی نسپارید
🔹
چت‌جی‌پی‌تی می‌تواند در تحقیق، نوشتن و برنامه‌ریزی کمک کند، اما استفاده از آن در برخی حوزه‌های حساس می‌تواند خطرساز باشد؛ بنابراین برخی اطلاعات و تصمیم‌ها را نباید به آن سپرد.
🔸
مسائل حقوقی
یکی از این حوزه‌هاست؛ زیرا مدل‌های هوش مصنوعی ممکن است استناد یا اطلاعات حقوقی نادرست تولید کنند و گفت‌وگو با چت‌بات نیز همان محرمانگی ارتباط با وکیل را ندارد.
🔸
دومین حوزه حساس، استفاده از چت‌جی‌پی‌تی به‌عنوان درمانگر یا
مشاوره روان‌شناختی
است. چت‌بات می‌تواند به صحبت کردن درباره احساسات یا مرتب کردن افکار کمک کند، اما برای تشخیص یا درمان اختلالات روانی طراحی نشده است
🔸
اطلاعات محرمانه کاری
، اسناد داخلی، کدهای منبع و داده‌های مشتریان نیز نباید بدون مجوز در حساب‌های عمومی هوش مصنوعی وارد شوند.
🔸
پرسش‌های پزشکی
و مسائل مرتبط با سلامت هم نباید به جای تشخیص و تصمیم پزشک قرار بگیرند؛ پاسخ مطمئن یک مدل الزاماً پاسخ درست نیست.
🔸
رمز عبور، کدهای ورود، اطلاعات بانکی و مدارک هویتی
هم نباید در چت‌بات‌ها وارد شوند؛ چون افشای آنها می‌تواند پیامدهای جدی برای امنیت و حریم خصوصی داشته باشد.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/464021" target="_blank">📅 23:14 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464020">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/271e3cb0da.mp4?token=HENEFeamulcg3T80Y0Cw0I3nyJz_N4sLWhcVcQ3kUDvbz0mUcZCc9sqHMMpEZgduurhvmU9RsQsCnkquuSgcwxD7rXTrUEoksDt4svWZYx0SUZiXtupiP7ebpDmGjnYU7EKS0APIqYD_qbrNO6VtceHtpSR1_u6ISms-CF2jKEAtgAG2QaGQoKz1eMxATzbrOnZUDkKHazJdVksbXlhAModlSYJKSKSpxJ7x88Ve991USAwe0PMl82TdXI90QUxAJup8jJxz7gyp5NUAQ4yhkCXMIs2he7xcJ1dt8-bOsLU3V3wkme0rRWmQN3w5g0CiguISVld-B03aQkM5cyOLsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/271e3cb0da.mp4?token=HENEFeamulcg3T80Y0Cw0I3nyJz_N4sLWhcVcQ3kUDvbz0mUcZCc9sqHMMpEZgduurhvmU9RsQsCnkquuSgcwxD7rXTrUEoksDt4svWZYx0SUZiXtupiP7ebpDmGjnYU7EKS0APIqYD_qbrNO6VtceHtpSR1_u6ISms-CF2jKEAtgAG2QaGQoKz1eMxATzbrOnZUDkKHazJdVksbXlhAModlSYJKSKSpxJ7x88Ve991USAwe0PMl82TdXI90QUxAJup8jJxz7gyp5NUAQ4yhkCXMIs2he7xcJ1dt8-bOsLU3V3wkme0rRWmQN3w5g0CiguISVld-B03aQkM5cyOLsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حافظۀ یک دیدار؛ درس سال ۵۸ برای ۱۴۰۵
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/464020" target="_blank">📅 23:06 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464019">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9oEFeMhO9opXEp1rdfxUX_mV-KPPnk1MbzQQGZhZgjvvrg--RxoPjk6NMcBY_TkWeDTi6F2aS1ptcCNrDEKBB6thULxKMmbi-9JsVR6w1McJM5preGk7tlSwXelz2TB8Tece8BpVrKkvr-O51FAb2BkDbGr9pG9Zhm4F78mZ3_Lr0Z6xndgFlOTw8gxmJt1gz3JDcVL_sL65eQ8oy86FvIqL67Dl1xmcHA78n1GRLPyJZIFiNwk-YMRx6jGz6amP1sdknneqJyxM_K1nLbziMjOSpgqh0xNYUloNfKCiOIx-746xjhNGOWQU7ZyLOCzxcNWHU4Mm4DVizPUioasYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه: رئیس جمهور ما پیام اقتدار ملت ایران را در قلب نظام استکبار باز تولید کرد
🔹
سردار محبی: رئیس جمهور ما امروز در قلب نظام استکبار، پیام قدرت، غرور، عزت و امید ملتی را باز تولید کرد که هفت ماه مثل کوه، اقتدار را در اوج مظلومیت، پیش چشم مردم دنیا تصویر کرده‌اند.
🔹
ما با اتکا به همین یکپارچگی از عالی‌ترین مقام اجرایی کشور تا رزمندگان سلحشور در میدان، و مردم مبعوث در خیابان دشمن را مأیوس و آینده‌مان را بهتر از گذشته خواهیم ساخت.
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/464019" target="_blank">📅 22:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464018">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">حملات موشکی و توپخانه‌ای سعودی‌ها به غیرنظامیان در شمال یمن
🔹
خبرنگار شبکه المیادین: ارتش سعودی بار دیگر شهرهای رازح، غمر‌ و الظاهر در استان صعده واقع در شمال یمن را با موشک و توپخانه مورد حمله قرار داده است.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/464018" target="_blank">📅 22:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464017">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjL59_SgvsyJOmw2Ue2qCppJn2SjkoyFcgh2xaYFMytj3sD82W9f1vBS4lSrCgVCQzo5IKhjvbu8Dg6VfIDIZhiLOHQprszqF05cWyVpHNXpgmpZOBWe_cdcFc5hRpGguds6tXeSNEz9Ik603nLPmUtM-Qd8oFLLLzaTyUkdL8tOesweLoL-ycBuqEfT8C2GXwVAfK138oQMTBHhYulJQseaKyy9qVdpgaJN0gnHVJDKaUC-DRMumn1CkNZNBs93rgngIdtw9HehTsuQzzboyldXMQrBDp3H_M-qxsLnzJRlPqHFpabal1TVQZcepNxqeEyszJWLL9qfrrKpq0lC0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت از ۱۰۳ دلار عبور کرد
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/464017" target="_blank">📅 22:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464016">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09e97e2c99.mp4?token=poQGJSA37V_-Pf7qOwYHldw-z_UFO_humlVbwcNbALsqSujn5ot8hJF-2jhrozpfi63HpCkPGKkKcNOAEIzj5RIDvzH-6u7CSLmodYZGyh95WhqPoTTztxbfrnd106VprSQ0TTsq6b-qEnfp9rcaouVeQvFJZ1tfFZiMNmeuVw8mpgc9KOwxVadwxQCgQmO4EBz8UX4gFFbQignEiMDjh5ntS4xws8WZukh6k5jEy5gbmsDOisoJbVHhd0qk5aigxN5Qu5VkTpMtS0oIqTW6rHWwuqy03AvLV_rFbK-19xzmo86Htn4LknO_HNETWvhNd3UHsw1_zSO4cRHvgZn34TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09e97e2c99.mp4?token=poQGJSA37V_-Pf7qOwYHldw-z_UFO_humlVbwcNbALsqSujn5ot8hJF-2jhrozpfi63HpCkPGKkKcNOAEIzj5RIDvzH-6u7CSLmodYZGyh95WhqPoTTztxbfrnd106VprSQ0TTsq6b-qEnfp9rcaouVeQvFJZ1tfFZiMNmeuVw8mpgc9KOwxVadwxQCgQmO4EBz8UX4gFFbQignEiMDjh5ntS4xws8WZukh6k5jEy5gbmsDOisoJbVHhd0qk5aigxN5Qu5VkTpMtS0oIqTW6rHWwuqy03AvLV_rFbK-19xzmo86Htn4LknO_HNETWvhNd3UHsw1_zSO4cRHvgZn34TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رژۀ خودرویی مردم پاوه، شهر مرزداران ایران در استان کرمانشاه
@Farsns
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/464016" target="_blank">📅 22:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464015">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01dd9ffa59.mp4?token=qukY35rezEVW87PoN1MOSZtMhQz66p1DPn0YBgJ4zMmMB3DQ6xuv3KPrclzJn6lr1hQoWCKUI7FipOt46LBDNnYhu8uhvBX0WFlF3GGy6PJB4xtoY7mdPr4peO7bsR4gy3AHSi7ZTn6xSQDTwLhTQcIlxhm93OIQtiqC7I_Xk7rJjz_a5_cdT1vMkTqXLhx6EdBUWkYfSjZPYaztUYgXOvYDP8asS2Qw4JAB50GHRJX2tWHU4409ZXrkCpmZqWA3aauxM7sYnRvpu-U0JA0CpVtsAk0sXhrF0Uc3MiqehtGKKE91IoimK7d0c6n012cMhm3WCgZxNrs5hd3lw5KcCoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01dd9ffa59.mp4?token=qukY35rezEVW87PoN1MOSZtMhQz66p1DPn0YBgJ4zMmMB3DQ6xuv3KPrclzJn6lr1hQoWCKUI7FipOt46LBDNnYhu8uhvBX0WFlF3GGy6PJB4xtoY7mdPr4peO7bsR4gy3AHSi7ZTn6xSQDTwLhTQcIlxhm93OIQtiqC7I_Xk7rJjz_a5_cdT1vMkTqXLhx6EdBUWkYfSjZPYaztUYgXOvYDP8asS2Qw4JAB50GHRJX2tWHU4409ZXrkCpmZqWA3aauxM7sYnRvpu-U0JA0CpVtsAk0sXhrF0Uc3MiqehtGKKE91IoimK7d0c6n012cMhm3WCgZxNrs5hd3lw5KcCoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تقدیر مردم شهرکرد از سخنان رئیس جمهور در سازمان ملل
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/464015" target="_blank">📅 22:37 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464014">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/111b48b8d9.mp4?token=Kr5x01tYHC19uvbSIAsZK47G7yQIDDZ4aGvaHvQgo4om2jtzgK0MxGQXgKTs1y8ThISzEbruFvUo6Lcxne-nVSHNo2MMoiliHnFWYRHNa-vKpNL5qDPpGgRaizvl1lGFRzHwW1tMaqYIolce_yL4K09eZTW3QsnDBIzfh-nxCH2wS1WC9Kp6bv-9rG8OfjxNtCUmeS8ZgH5iWccLYid4Qlg4AMeW_MWgOefsA-d4mjyYYz1sFEx4vL5OIgAHhkaMz9VyuP1jm8LxFtomA4ViokplscZ3SNvXJIKKYBg8AOID8WY3g15h_ej-EITmuafxOvCQuawtMtoX160cXhe99Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/111b48b8d9.mp4?token=Kr5x01tYHC19uvbSIAsZK47G7yQIDDZ4aGvaHvQgo4om2jtzgK0MxGQXgKTs1y8ThISzEbruFvUo6Lcxne-nVSHNo2MMoiliHnFWYRHNa-vKpNL5qDPpGgRaizvl1lGFRzHwW1tMaqYIolce_yL4K09eZTW3QsnDBIzfh-nxCH2wS1WC9Kp6bv-9rG8OfjxNtCUmeS8ZgH5iWccLYid4Qlg4AMeW_MWgOefsA-d4mjyYYz1sFEx4vL5OIgAHhkaMz9VyuP1jm8LxFtomA4ViokplscZ3SNvXJIKKYBg8AOID8WY3g15h_ej-EITmuafxOvCQuawtMtoX160cXhe99Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار مرگ بر آمریکای مردم دیار حاج قاسم در قلب کرمان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/464014" target="_blank">📅 22:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464013">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3IPmTtw4DrIHxkpiqyrkGkbMdtm9BVuy7IJuHQS_UoQebYDGcnahOOLyyV8J-8fdk26Rp822nxY_LJQhkz37smxvqkkGQ7H4-K_QStXXI_FhfmkGjhJLI59aBuq1emav0kq1fMz0gBR8zla-mYdUw-P_ZiMcZ2b5P_Ca67uBTEY4a06-tbdwfLke_UzEtcrrO9WX4MCLZf8bM6C80nGssC9zNDQEf7T6tJo4OkbbnMqcjpBYlyHV1NK5v8eyd4_pdZvsyVJlFuZ2TgWHEIHO21JTh2zKGPUwjMDnc1CzhyLRAiUoJn2LBTqB-zRHzy5l_LrjZ3Ul2tqNu6zCA7qcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منابع خبری لبنان: جنگنده‌های اسرائیلی به حومۀ شهر القنطره در جنوب لبنان حمله کردند.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/464013" target="_blank">📅 22:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464012">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43c274c1a0.mp4?token=BVtxW75PtbGqdjilDdkMtTzj4lzZ2vRo6Wgjzu0EeEZebyzn8pUSaYX5rVL6Q4Td0Kv3FrSlnY5Fw92BCcaY2BVZP_EVYdLNRgM8jVEsDNEk8hnlcGW6z0rwoWyVxlbL1t6GuUMjvbKYqqrX8Sg6MJWysRihU1BtVS1r0EJ_L51FgkrhHR0BTUh_NBRXbG2ZuLN32hB4XpiCHuJ2weEak_KVln7FObOcMgaqsKZ2puedwV2cOfdTYZOAluhsCJwHk_OJS7cZm-5MyPiy32Ua9JUfElQNMoV_uo4XP3quW1kyDaHYnBZMu5Uz9qGiXjKqBEwRZ_HyxS7LRXJNYX4XEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43c274c1a0.mp4?token=BVtxW75PtbGqdjilDdkMtTzj4lzZ2vRo6Wgjzu0EeEZebyzn8pUSaYX5rVL6Q4Td0Kv3FrSlnY5Fw92BCcaY2BVZP_EVYdLNRgM8jVEsDNEk8hnlcGW6z0rwoWyVxlbL1t6GuUMjvbKYqqrX8Sg6MJWysRihU1BtVS1r0EJ_L51FgkrhHR0BTUh_NBRXbG2ZuLN32hB4XpiCHuJ2weEak_KVln7FObOcMgaqsKZ2puedwV2cOfdTYZOAluhsCJwHk_OJS7cZm-5MyPiy32Ua9JUfElQNMoV_uo4XP3quW1kyDaHYnBZMu5Uz9qGiXjKqBEwRZ_HyxS7LRXJNYX4XEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رونمایی از اولین داروی حلال برای کودکان و داروی پیوند کلیه
🔹
وزیر بهداشت: کمبود داروهای اساسی از ۶۴ به ۳۲ قلم کاهش یافته است.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/464012" target="_blank">📅 22:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464011">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/909ccf2b29.mp4?token=tUI1aZSp1tV-cllk91VXcuaWnpKyUn5axjIqGnmmq50GPxC_nkj-lCUKRXangsvmZcLY4lYz_zZKcIWZaDwvN0dOSi150RddyWATwc1OuqNoezd-R_917jzcZohXeyHY4BpUhq4jillfvn2iOPxsrRHY439_uHn95acyxsCSrar__daGF9S0S02Quen-Vd4QRPRW_Tmk8T6fdzCYleAwAwAEIOIJBnNvyuDrVM9XRDxp7QYynbbjdG1sOMzGYMjnArRC1m0BfxZSjvd-fG5NgF8LWLrUT_LbfGL-fHvOfY3kgXJAOHhaTd1bc0qdZEdK6KOOA_hb75jaktpEeCKFdhJA4G3yU972_f5b83bIqwVTlUslDAlbxCYMmDOrInH-M2opE6pRj-n6Tmjp9een2JbskVsRHl89RdYXGBwF1EXrOrgP8CDzdAyjUjdbDP597k1yRP4OS7cSkTNT-IqlDeVrvab7wrXFKxBuaJN5-x6KC-b9LrNgVMCQpZcAaeRvMdBvH3o2CpBpZuBfHsR45024KKILVH0Lyox2Y4_iXBPyGV56ezJh85Zkr0LO6A_uFZ6qkrIEIW5aF1G-rG2TnDIstjDDWeLEGWjstMDYtaDvz_5F9viADx4QxK79v8aiIoFpY0L2vG_azfroUbQaP6xMxSFl2dejQkSJaltkhSM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/909ccf2b29.mp4?token=tUI1aZSp1tV-cllk91VXcuaWnpKyUn5axjIqGnmmq50GPxC_nkj-lCUKRXangsvmZcLY4lYz_zZKcIWZaDwvN0dOSi150RddyWATwc1OuqNoezd-R_917jzcZohXeyHY4BpUhq4jillfvn2iOPxsrRHY439_uHn95acyxsCSrar__daGF9S0S02Quen-Vd4QRPRW_Tmk8T6fdzCYleAwAwAEIOIJBnNvyuDrVM9XRDxp7QYynbbjdG1sOMzGYMjnArRC1m0BfxZSjvd-fG5NgF8LWLrUT_LbfGL-fHvOfY3kgXJAOHhaTd1bc0qdZEdK6KOOA_hb75jaktpEeCKFdhJA4G3yU972_f5b83bIqwVTlUslDAlbxCYMmDOrInH-M2opE6pRj-n6Tmjp9een2JbskVsRHl89RdYXGBwF1EXrOrgP8CDzdAyjUjdbDP597k1yRP4OS7cSkTNT-IqlDeVrvab7wrXFKxBuaJN5-x6KC-b9LrNgVMCQpZcAaeRvMdBvH3o2CpBpZuBfHsR45024KKILVH0Lyox2Y4_iXBPyGV56ezJh85Zkr0LO6A_uFZ6qkrIEIW5aF1G-rG2TnDIstjDDWeLEGWjstMDYtaDvz_5F9viADx4QxK79v8aiIoFpY0L2vG_azfroUbQaP6xMxSFl2dejQkSJaltkhSM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امضای موافقتنامۀ انتقال محکومان توسط وزرای خارجه ایران و کره جنوبی
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/464011" target="_blank">📅 22:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464010">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JHwzyt8cSRFo8hCPOOgtY7IbHKTCqwlKcRX6nt__AwgcdG3nfMf5ib22tAl9IQ7Irv4G1i-GI43I8hSVFWAeJPcwRY7AeWsx7qH8DBGBv7elshV_khx9KQbouK58PrkZAA2gN_Tx-LUB7K9E_b_WhA7lUR5u01q1B6CcnZe-x8BbLl_ErmTRSAtHwpkdwTUEyfs2v3k-qY271_QGGudvrUQJynNOPy0uDE1eY0xRl4p8zywtPTdeeewquPDNyGZu0QYsg4Y_zmtXm229yXYf_4vXsV7udUzS7kVNyGroAdLCtrfmOp2AqyGkBV5lNNnCdup7G6zJICqtVtKYdlCwew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قدیمی‌های تلویزیون هنوز برنده‌اند
🔹
آخرین نظرسنجی مرکز تحلیل اجتماعی متا حکایت از آن دارد که سریا‌ل‌های قدیمی تلویزیون از جمله «متهم گریخت»، جز پرمخاطب‌ترین‌ها هستند.
🔹
در آخرین افکارسنجی منتشر شده از سوی مرکز تحلیل اجتماعی متا، سریال «متهم گریخت» با 37 درصد، پرمخاطب‌ترین مجموعه نمایشی مردادماه ۱۴۰۵ اعلام شده است.
🔹
در این داده آماری به ترتیب، فصل سوم «آقای قاضی» با ۲۵ درصد، «مختارنامه» با ۲۲ درصد، «خداحافظ بچه» با ۲۱ درصد و «الگوریتم» با ۱۵ درصد بیشترین میزان مخاطب را در بر گرفته‌اند.
🔹
این درحالی است که به جز دو سریال «آقای قاضی» و «الگوریتم»، سایر آثار متعلق به سال‌های پیش تلویزیون است. «متهم گریخت» که به عنوان پرمخاطب‌ترین مجموعه نمایشی در این افکارسنجی عنوان شده است، ۲۱ سال پیش از شبکه سوم سیما به پخش رسید.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/464010" target="_blank">📅 22:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464009">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">انفجار کنترل‌شده مهمات جنگی در جاسک
🔹
فرمانداری شهرستان جاسک: فردا از ساعت ۸ صبح تا ۱۲ ظهر احتمال شنیده‌شدن صدای انفجار در محدودۀ شهر جاسک وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/464009" target="_blank">📅 22:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464008">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
پارسال لحظه آخری به خاطر جنگ نتوانستیم
حج تمتع
برویم. پس از سال‌ها آرزومندی با این
افزایش خیلی زیاد قیمت دلار
باید قید رفتن به سفر حج را بزنیم.
🔹
لطفاً مسئول رسیدگی به
وضعیت پمپ‌بنزین‌های استان مازندران
را معرفی و این موضوع را بررسی کنید که جایگاه‌های سوخت، به‌ویژه در مسیر نوشهر به مشهد، سرویس بهداشتی قابل استفاده دارند یا خیر. در مسیر ساری و حوالی آن، در چهار جایگاه سوخت با سرویس بهداشتی نامناسب یا غیرقابل استفاده مواجه شدیم. واقعاً تأسف‌آور است که در مسیرهای پرتردد چنین امکانات اولیه‌ای وجود نداشته باشد.
🔹
۲۰ سال است برای خانه در
تعاونی مسکن میثاق ماهشهر
پول پرداخت کرده‌ایم. با پول اعضا خانه‌ها ساخته شد اما مدیرعامل و هیئت‌مدیره شرکت برخی واحدها را فروخته یا اجاره داده‌اند و ما
همچنان مستأجر و سرگردان هستیم
. در این مدت برای پیگیری موضوع نیز به مسئولان مربوطه و اتاق تعاون استان خوزستان مراجعه کرده‌ایم، اما هنوز به نتیجه‌ای نرسیده‌ایم. واقعاً سؤال ما این است که آیا بعد از ۲۰ سال مرجعی برای بازرسی و رسیدگی به وضعیت این تعاونی وجود ندارد؟
🔹
مدتی است که
لاستیک دولتی
توسط شرکت‌های معروف داخلی
توزیع نمی‌شود
و درگاه‌های فروش اینترنتی بسته شده است. قیمت لاستیک هم در بازار آزاد خیلی خیلی زیاد شده است.
🔹
خواهشمندیم صدای مردم
کرمان
را به گوش مسئولان
دانشگاه علوم پزشکی و نظام پزشکی
برسانید. شب گذشته فرزندم را همراه با نوه ۵ ماهه‌ام برای ویزیت پزشک بردم. با وجود داشتن نوبت حدود سه ساعت در محیطی نامناسب و بدون تهویه مناسب منتظر ماندیم و کودک به دلیل گرسنگی، خواب و گرما چندین بار بی‌قرار شد. پس از این انتظار طولانی، منشی تا دریافت ۸۵۰ هزار تومان اجازه ورود به اتاق انتظار را هم نمی‌داد و معاینه پزشک نیز شاید پنج دقیقه بیشتر طول نکشید.
🔹
من معلم رسمی منطقه ۷ تهران هستم. بر اثر یک حادثه ساق پایم شکست و برای درمان به
بیمارستان فرهنگیان شهید باهنر تهران
در منطقه یک مراجعه کردم، چون تصور می‌کردم با توجه به فرهنگی بودن، هزینه درمان برایم کمتر خواهد بود. اما در نهایت بیش از ۲۰۶ میلیون تومان هزینه درمان پرداخت کردم؛ ۶۰ میلیون تومان را مجبور شدم به جراح پرداخت کنم، ۴۶ میلیون تومان هزینه بیمه با احتساب بیمه دانا بود و ۹۸ میلیون تومان نیز بابت پلاتین پرداخت کردم. سایر هزینه‌ها هم مربوط به عکس، آزمایش و دارو بود. باور کنید تمام این هزینه‌ها را قرض کرده‌ام. چرا یک فرهنگی باید در بیمارستان فرهنگیان با چنین هزینه‌های سنگینی مواجه شود؟
🔹
در سال ۱۳۹۹
شهردار وقت مشهد
با مصوبه شورای اسلامی شهر، در قبال واگذاری حدود ۳۰ هکتار زمین برای ساخت پارک چهل‌بازه، به حدود ۴۷۰۰ خانواده تعهد داد که پس از اخذ سند زمین از اداره ثبت برای ۳۰ هکتار باقی‌مانده پروانه ساختمانی، ترجیحاً بلندمرتبه‌سازی صادر شود. ما از
سال ۱۴۰۰ سند زمین را دریافت کرده‌ایم
، اما با وجود گذشت چند سال
شهرداری
همچنان با بهانه‌های مختلف
از صدور پروانه ساختمانی خودداری می‌کند
. این خانواده‌ها بیش از ۲۳ سال است در بلاتکلیفی به سر می‌برند.
🔹
مدیر سیستم سوخت گفته ماشین‌های بالای یک میلیارد
سهمیه اول و دوم
را نمی‌گیرند. مگر ما گناه کردیم با قرض و بدبختی یک رانا خریدیم. بعد هم مگر
ماشین زیر یک میلیارد
وجود داره؟
🔹
ما
کارکنان مراکز خدمات جامع سلامت استان فارس
، ۴۸ روز پنجشنبه بیشتر از کارکنان ستادی بهداشت و دانشگاه علوم پزشکی سر کار هستیم، در حالی که حقوق و مزایای بیشتری دریافت نمی‌کنیم. با توجه به غیر‌اورژانسی بودن خدمات بهداشت و سابقه تعطیلی پنجشنبه‌ها، درخواست داریم در شرایط بحران انرژی،
پنجشنبه‌ها تعطیل یا دورکاری شود
. پزشکان خانواده نیز به ‌دلیل قرارداد با بیمه‌ها همچنان پنجشنبه‌ها حضور دارند و خللی در خدمات‌رسانی ایجاد نمی‌شود.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/464008" target="_blank">📅 22:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464007">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae2e5d0310.mp4?token=igops0-p90e8g5cGTxpA6YjV7qk90dQqoC2zlV_EN2FkEb1rmtvhM71wD4yoMRuCv_oOWpOj5UKeixwKx4jSYbLCBusnHVu9EOzaKtJX3uU1RGffo-G8Z9i5mOl28kEEbdLsdN_CV0Gp5tgxjRNjgxOwPQr0fPoe218srfllSOtHMAoxr8f4kDqh7kd_ZI_lFkqLrcadTOqVppWNjM19Okc2DcDCRHnxihF0B8z1Zotu68fy3JJRYR0ttesbqj6NYzt60LDi5ZUJjdmdk279MsKTPPC8s0NrMn99wfDpZBkk42pHmn4ePovJb2T_RDuGYlolYSpu2Y1dcsYniSB7Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae2e5d0310.mp4?token=igops0-p90e8g5cGTxpA6YjV7qk90dQqoC2zlV_EN2FkEb1rmtvhM71wD4yoMRuCv_oOWpOj5UKeixwKx4jSYbLCBusnHVu9EOzaKtJX3uU1RGffo-G8Z9i5mOl28kEEbdLsdN_CV0Gp5tgxjRNjgxOwPQr0fPoe218srfllSOtHMAoxr8f4kDqh7kd_ZI_lFkqLrcadTOqVppWNjM19Okc2DcDCRHnxihF0B8z1Zotu68fy3JJRYR0ttesbqj6NYzt60LDi5ZUJjdmdk279MsKTPPC8s0NrMn99wfDpZBkk42pHmn4ePovJb2T_RDuGYlolYSpu2Y1dcsYniSB7Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس بانک مرکزی: در حد توان تورم را کنترل می‌کنیم
🔹
مهم‌ترین وظیفۀ ما درحال حاضر این است که نگذاریم معیشت مردم دچار مشکل شود.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/464007" target="_blank">📅 21:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464000">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/stFe91rbjCb9UHPGOb58sMuQj9gE2VWGIAOlTBZga56rdflPXkV9u7fx0hBUNYIYKwKiUo4g_AZ2lqWxPawLCmyvd-8iutEkLKlFoX1nihKletDsMtAk7vzPPREEzCaQj0LJ8KnyG4vZqUqjc0Dyp-7FF3XHrS_7LgmgUoRxagjbX_8l48MN9KefaUnZkdaEMlitKEbhThQrl3SJCyur1stdNVRCNJFGnwFyp82y8nrqjYG6TpjAROqgYQpqsf0y9G389710QvIWez9wC5_quV4nWuQaDX5ztRi3blxskwDTcgfho5yt0s8c734N503TKDcc1Lx8p25PXV-KKGp0BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ilE0bpSmvWHVBnEeuncC2agAS8VW3a9GF_93IGvz2o9e5q4pdYp6hhOgkfbcGrNH1rmNpe60a8kU7RYy9DpYDWI0s2cwYfEV8AlKjYWdghwOTWHT-ldGvOUm51vmxByATni_R2hZD7Svs1KkOQr2IZBOc2jB3jUoa5JUD0KV0aeOzLpdJtEQRJ60soMbYZHPjzFB1QnXJpTzxI3_W1EJHKYb6Kve7WRlH1F0XE3xpAWeECbqHVfeiJtPEUc2Kngmew2RhpWkbXAYgvlHLdPrzNdklmI70nBy2TBBEvU3QXO-ByeXKHlQA5TTma02K5UCB40moAGs3sKrpeyB6HCGkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BHrPJFm1qRPpr9l8uzpM_GDrk98G8-zoQ7cJd_hlP723ABiTriBMUOeCH07jY7ZfYx3jNW5kxYKQPHiVqb5QfzVYNQoKztmVCHTJr_GMmMJU0NblORJ0RwiBuhDGo-jMLPt2LXArn2uoD_raG76K5dsV3W0Imb_B6PH9IN7Kt_5mngOBcRXmowAncIVvYO7lqaFC7szIY7etLb7mHkfjqxV9Pfo072-oDeJJ9G5XlyVzVtOzZ8RDtcbU_pluAm90K4Fi8uZMKHYM2uVfYld2ksQABq6NNh3kHNnpuQEeZ70VpcCKKtHt-lBA61Z_LkfoxWsAJe9xxsX-XAvg3wkhXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MxqyPnv_5z8B88UygETia7Fi7Wm6oeGYmN4VLE7MyWTi6wPO-JhAKztEaCq4zLAd2A6KbupmaB7gaPXuGozdCOqYDc6aKhAZONPg_0GUu7SmsVrqivttY1toCSfs50nWqooH0B0kwpo54Elnhm6x6aLYnl1UNQXI70MEht1ezn9lyGVXtXiHzIF6d4go4tLSOzXRObG56KAfwAeS_-9dqXY2kNGabPH1brwRDy-bpE_OFKeqFOx0ydfzCW972zJWrigUcbFyqpQu33VEqzkiG_4zn8Tuh7xWLzbqoBBO2AFys7TcKiQsn_BZfspkOfHZmw1sD-znBE19_lNpsrJwPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jQ1Zjz5Oa7ySJIrSen7DKR-fF7c1m1urAZYiPkz1LiYv-8szJ51Kp3YucikIRoInjrxFmWVDqJO8_Hl1uRWlXu2slbmWE_CDzfaI3mwzaIWOwbaWtH1smiS_VppwuFwaz7LaaamD8W-8GVO9RL2zDM41SqTKT9Dggtx99za77nYVJkJKDCuIL65tD3PNNPW0dWe6qikeRcIxodaTvkU9N6o54u7XeZ6Cg2QLwWPANFy3ep6kzpdV47v70hRbGUfevkApOTpiTAu2fiidc7amV2QIItSogx1RRvS6gxt-iulJtCqBfu4hpXGIqXUV1K0WKpKaxBxS0bKzyEmJnc1gZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CgEwe5Pa2niZ16c8eFP_YlAcvhqtNsPSX4CrB8uCRJ3_o3CuLtBYZiZMqYPhrHUUlOt-J3AHwHsIdBKebu13QQffGeR6535KRs8Zz5xtd2UspASCjkRR3BPdC-o1n0HDkOYLg1Pp1i0DVFbcA_x3whuQ3rMH3Hd2LEIiKHlzBANshd1S5W6hF8Q1hIIjmUNxaHWmrS6Baf22P4g_ZwyUJi7RBIj7RuCYFLCM5SyZtQmP5IStHcUMrEQ5t2hc177kZTAow4Vnqp3_8xRfk5PX0TEX4HQ9PWyAR6EGTVds9VZRaSeeGPBR_Amy5z5Ohz1k49P5K4C_D8FgXU-Bzm8nxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RSqVeDuVkquQpK0yX6ydqV9HU3rD-blLc_VZ3Dii3ffqSNfRxbn1zFqF2e_EaUonra7YB5PW3pqC9hvq-SEALIF1BGeZUgUjPYaXZ9gd6BZa5z-uAYwMggcp8Cq99XsYWfWdNMTwwtCm9vhDsiKDSSfOSFjJ19s2TuLDnjNOfL-Bdr08XqidU9aRAR2P_9y6bm1Sb4poeK0ukW7zKSEltLnJoY9RBB5YFQR1wy_l_nCAJ59y2oX9dlGntTZJwlsUuraDCJHJm91qw00y0OzMAFo6sViHQSFou4IaxpaWlMwUIfsa7ljiuvpcZQTJ6lD4Pb8C3GN5Pk_uM0mf1Y69Mg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم ترحیم آیت‌الله شبیری در حرم حضرت معصومه(س)
عکس:
حسین شاه‌بداغی
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/464000" target="_blank">📅 21:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463999">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4e99c01a7.mp4?token=Bdc-c2135jhnL5VFmGgIPxe0Q3eFaYJb9Rv83eMNif11OdrpIFzlqGUbcJZleg5fDDV8JbPvHmVv3xC203xyQsaxXvXYnU__7PzT4r61th0y9KO-4XghQytMalkuWrgPUTD_VJ3lLW9nwYM6BUP1k4GuWNY4HhCUw69wDiva6d-uXH8CVf8935NVx913xBKSC3bs9LTWinqMJoOJs2MZ7bDrw6uQwdjONoMt2nytygf2Znz_vgslDwIZSsFbgeParXqKKCoQZUqtmnDKF8s_wZtRplT6XcQoPWPxRPvobsD-Ff5XOC3SJPSqbWaR5rlK3hXPDVuHAhCSAjfzCaS_OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4e99c01a7.mp4?token=Bdc-c2135jhnL5VFmGgIPxe0Q3eFaYJb9Rv83eMNif11OdrpIFzlqGUbcJZleg5fDDV8JbPvHmVv3xC203xyQsaxXvXYnU__7PzT4r61th0y9KO-4XghQytMalkuWrgPUTD_VJ3lLW9nwYM6BUP1k4GuWNY4HhCUw69wDiva6d-uXH8CVf8935NVx913xBKSC3bs9LTWinqMJoOJs2MZ7bDrw6uQwdjONoMt2nytygf2Znz_vgslDwIZSsFbgeParXqKKCoQZUqtmnDKF8s_wZtRplT6XcQoPWPxRPvobsD-Ff5XOC3SJPSqbWaR5rlK3hXPDVuHAhCSAjfzCaS_OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲۰۷ شب ایستادگی؛ زرندی‌های تا پای جان برای وطن
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/463999" target="_blank">📅 21:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463998">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff5c92bb3d.mp4?token=bZ7x3eOfzd24-NcnHtbc0c1LMDGI7OyX45Ib9tXzdJ3o_X36o6azqIZOEl9nyAKqn0fhYfNwoMW3cB31CzrGYSRoUmkRY0GBoMb6URyR0Z-UYynag6Ms6ymgDTmanh9CgexpxWI9lcgrDhvt2fs63BiaMcqn3NTuawuhzEt0ZSgC3kL7m6wK3S7awHgR1VQY09bJ-b1exb1QwhEz1FJ36l67oyQuuX6a5B4-zVP5updMj8cI84rXYDOUTseS5inLOgsRpjatgMoHA3mOGbYWx9EwaQAznH5COql7JV8E6MUeDoUi_hOIx-Gpgvwwmtpver-0aqU4Ju6lFdSYfn-RVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff5c92bb3d.mp4?token=bZ7x3eOfzd24-NcnHtbc0c1LMDGI7OyX45Ib9tXzdJ3o_X36o6azqIZOEl9nyAKqn0fhYfNwoMW3cB31CzrGYSRoUmkRY0GBoMb6URyR0Z-UYynag6Ms6ymgDTmanh9CgexpxWI9lcgrDhvt2fs63BiaMcqn3NTuawuhzEt0ZSgC3kL7m6wK3S7awHgR1VQY09bJ-b1exb1QwhEz1FJ36l67oyQuuX6a5B4-zVP5updMj8cI84rXYDOUTseS5inLOgsRpjatgMoHA3mOGbYWx9EwaQAznH5COql7JV8E6MUeDoUi_hOIx-Gpgvwwmtpver-0aqU4Ju6lFdSYfn-RVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زلنسکی: امروز حتی ثروتمندترین کشورهای جهان نیز نمی‌توانند به اندازهٔ کافی موشک‌ رهگیر پیدا کنند
🔹
میزان تولید فعلی صرفاً کافی نیست و حتی کشورهایی که سال‌ها صرف ذخیره‌سازی موشک‌های رهگیر کرده‌اند، بخش زیادی از آن را مصرف کرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/463998" target="_blank">📅 21:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463991">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p22hXU6A7WJlBC5Mp9bqHdo3dSfN1AdTEcfGUOBY_x0GeB5ibucvwn9ajVB3mbO1eN-Yrpb_pdRB1Vaymc7sNp7s9nGFxLllFYP3KjXJyV78YKtC7tgxSlb5hanwtgKXbsewlrWPPADvRjx6ey1tsNMm2n34nOQRlkv8REhRBBnmOqVlDhhZgOkHAHYehIX6XKuQaF7psxfauqpOXi8MgnQZrSA-jhrZK7a5bnRi_KIVfHyc83uu48gHaHD54EmmAi7smQKuXxj4L52D3D3e12s0SgdMaNEux0lAJmqwYxdQr1cP-j8VyxgBnqaMrRUK2F3W9-KASNlWsfY9t_4rpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hi7kmVhNDVe4jP0-P0atVSWN92nkGt5JY1hJd-5LQk3MmehzJ-H9BOCnWC3AgdZKP4azKEpa8UBazvIKf2QvW8RFLt5Bs8CpEhEtWqDxQiG0VD1VOYYXpf7DAUGEAAxu_lguh72ukpMdKMJxSFjLRxajRmRp8qNzYn1Ntgc9wG64H-pwthFbWHRsPZoVU1juJQhXaHLJ14R0LGqrmS6lYuckkMuPk6FefxQRDM31XedDnKsy_l66Rqp92NXMMcbqFQyIvKzV-H1kAcQI917tWtWGzY2XUX3xHesxayS7mt6OO5WiXNSgcFAsDn8UK3cbZuZzdbxY6meQfXkqUDl7AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/reEgvBMey0JT-nMvrOIUJcu0Skp9bi-Tt3yBLrxk-iZh--TnWgv1VJkJYlBhwaoSiz6gYd2pMkluf5zfe2VOq_SZwtKNZ_YPHIPlTOWC604WFDe_dByOWcb9_IWg0ONfsNsE3UBQsefXDf2PKYSAheUuW62EWUeL2-VnYCMwCjxCFNujfV86Qqx7VTkGdfYMunwbaOwzugz8YdkjtSFVVu-6XiPE8URBN-OmHkd4c5mS2PNziXOXS7lTdksUSu_hJoLSz_4UseL539XyUUBUGHassqY1HOukMuIqw3hw2K5-jW2J491klZaO2F-RRpSUYK3JJ88M5DGLX7n__db63A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/muAiEpCy-uaiKB2jKq8RsqF7L9on6a0fVkrdMXMLjUGPK9IkgnGliT1KxvluJEvRmHTpsvwKcmrniX9XmV_NAiwlbfFv3sN96pt5SNkxStgtvW68X3DLcZMDpuHqTVtfQzsFA9UvdDP4GWbMC29Oa5gtCc3ZtnIN376dH18vQ8skAHHogZc2c5F2DFCTiVTkzg97yD-DpV-AS8eWGsGH2G0TuzG7LTEGRmvVWVbsrPNV5B8MOxdaV_dQn1pwD3lRcVNzX-LrFHSY43Yseg7TdMbKPYKL4x4TO6n7TpYxxpUVjHkBhX3UgsFooeDp_66WzIi3HsxQUxloKCRb00DkWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lwt_dfm5okM3eU22GEyNeSpYwMDdV_d1T3Be5glMsSMN5NreiyGCLhB4C75z8ARI6Obxvg28gwKUnsuOH8phLA9YxVB6AIqhiRr9qJsf1nOwo6qY1Xe2WUO9XXEicfQrHmU2tycdaafNYKRYcELan29PNpoVrN98n7VxUZBvkLSk3ctUrlIn2vtQ78R3lDuk0yCA4-4_Mz8YGrF7uJXWio81rKJua2QvzB822LvgsC1ecz8OZYx0CP_f-tNfY-Ty0ZaHD1wkDkvDQ6PdYcizGLpUAwRfvnDxxwq-9uY4K7P0IJ6yU36l4OB6V8QwXxIfaaRIYIG8fh5ARfBIJ0oNLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KiTFf0xJWF_VFISjIqkckv0JBTSOh3knV9kZrHKsV6z6nQJPN-ynUj0K01Fdt_C3xykhds2JF8XhQK4RcZaqDQYcDsX5HRArF9E0mmvmPYivHD9NuE2m7vyKKP7CMB5SnM5NO4oBfTkTGm33j9R37qctDjmp66KCFRDfFf-HVBEDZ73lhSAl_rVPdBOmAhKAqRhwZbJ-Hc0VLhIj0KDirowT2JBbZg-0Ovj76Ss_N9Ki8_daS4kVoLAHletnEvuRLUaQErqN5hxOdTvSQdcan34VyFCtH84_C2I2FjaLLX27QFrVZTlZDMG7m_3-8Iw6z2pcQ9QesyKrZPsU7Jpuvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZsDFsnwj0yDsQvPNBB86JRHQ_pIOn8BZ1alm0EvljdoSzZy5M-zm_iEYPt1nZTmQjQBJL6FrS_5tetYHCyumblsxtwII6OFNAx352i47ZWn86zobnleoTvK34HYgWiISAcKrzsyfFmHJ2WJjbwkU27mog9AjHXxOCMSZ9zqXe7qEG8fQkcAZ6uWeohg9WoQdw5HfogEP-nG5kOND6Y7ibnx5_lx9Th0hHsFli12bam603CtTj6jK1qxtYJuWZ-G_lcNSbnxcb6G44z-b0hhuNExr1YExCXCkASYrOp5aDj5rFZTLtUYqG9SF5RHexokjqEyzcmHVcNsH4qDm3Nj1Lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور قالیباف در جمع دانش‌آموزان مدرسۀ شهید آیت در اول مهرماه
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/463991" target="_blank">📅 21:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463990">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adb12ebd04.mp4?token=eTnR2Qk86ttiEckHqb0no3fT2M5Z3AqRxUgsHR-984fCsY5kuc6MRMt6jDpn8hxpnmatKXdysxVXX1Y1gWFfH65I7_pgGWhenotbFwTUa_3ESATNA7rtuXAsT14ij9rlkDSQaEv_OrgEGRl8OwoIZxo5S6TWvMmFwMWlaMFsRPm5omPtw6yFQD4NjDxa6Yf80kuRJgq84xwJReN6OG2OZZwHajT4VZKrk-v1dwlKdM7p1nAmVehrplcpgqlxjw6FV1b7O93loCx5JrV7j7shr59M5YAAr_hC93ceR0xNQuQFqPtw8xJPVrGMZgFEdgr4PWFgZZmcd811KkiS9pvJAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adb12ebd04.mp4?token=eTnR2Qk86ttiEckHqb0no3fT2M5Z3AqRxUgsHR-984fCsY5kuc6MRMt6jDpn8hxpnmatKXdysxVXX1Y1gWFfH65I7_pgGWhenotbFwTUa_3ESATNA7rtuXAsT14ij9rlkDSQaEv_OrgEGRl8OwoIZxo5S6TWvMmFwMWlaMFsRPm5omPtw6yFQD4NjDxa6Yf80kuRJgq84xwJReN6OG2OZZwHajT4VZKrk-v1dwlKdM7p1nAmVehrplcpgqlxjw6FV1b7O93loCx5JrV7j7shr59M5YAAr_hC93ceR0xNQuQFqPtw8xJPVrGMZgFEdgr4PWFgZZmcd811KkiS9pvJAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیدار پزشکیان با رئیس‌جمهور سوئیس در حاشیۀ نشست سازمان ملل  @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/463990" target="_blank">📅 21:43 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463989">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0xnBnvvh6Qu9Dak8YgJBEhncd_mhEDBo5SzUv6XVdsaXGaoQNFHmmljMRYdjo9DYyEl6OXu25Bs_Kc0WPImBcvY6NBnpq2BTdhqvx_TY7hd2EOKhnKdeC42bXX8LHam9T1NuTz_Umfu-Ea2aYjciY3EkwxvML4xH3Mgh9lzYe_rQRf4ieZtk7kUofnRTFNF4lAq_BRIS3t9IFdb3xCE-2TIl2jND7ZxrRofm9w6IoME397jK6Cu1yOUiu1IsNn9c-SSuy7hYqHcmzxlruOqNivx8grngkHGQuhNoT_eEEQ5vg2eKrWwbTIUBlWzuxozJAwxFOnwr0fJ3pg6KSLCpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: رئیس‌جمهور پزشکیان صدای قدرتمند شجاعت، مقاومت و استواری تمدن ایران بود
🔹
زنده باد ملت سربلند و مقاوم ایران. @Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/463989" target="_blank">📅 21:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463988">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79decdda7d.mp4?token=N9qcjmFyi1Gqq9DSu4xbGB_Px0dSk6cKWIIyLT5o4pORAmmzZF_U-gDKobZDkNG0P2OhwcnTaMGya3lxBzljPG4o3yeKQ2t0DPOd76bRf2vDRFcTFJ7y6Mdnchc_buITnlRpr13t97dzorXWJDToUlU0trXqu0F61X65xnsBViQ8DBs6YNr_AnuyuMEb4sDElfgXuREjhsv1xpBOUobqzf5QWV5vHDX9It6qdxUjMmO3skNKvjQBILD8BLp2-_aIBJieotW2mwVZtoFzZsLu54Xn8ISwEbO8V9tGLvkKowlksQ7bpJEX8Htgmcq7N6QHmX2JsQEkMZo0W_fNFf0kWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79decdda7d.mp4?token=N9qcjmFyi1Gqq9DSu4xbGB_Px0dSk6cKWIIyLT5o4pORAmmzZF_U-gDKobZDkNG0P2OhwcnTaMGya3lxBzljPG4o3yeKQ2t0DPOd76bRf2vDRFcTFJ7y6Mdnchc_buITnlRpr13t97dzorXWJDToUlU0trXqu0F61X65xnsBViQ8DBs6YNr_AnuyuMEb4sDElfgXuREjhsv1xpBOUobqzf5QWV5vHDX9It6qdxUjMmO3skNKvjQBILD8BLp2-_aIBJieotW2mwVZtoFzZsLu54Xn8ISwEbO8V9tGLvkKowlksQ7bpJEX8Htgmcq7N6QHmX2JsQEkMZo0W_fNFf0kWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم بجنورد در اجتماع امشب میزبان خانواده شهدای میناب بودند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/463988" target="_blank">📅 21:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463987">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/579850fb0e.mp4?token=TBee5jkllklEGCaanx3_n7C-uTx825lpA850v2xblUgHTkcxK54YEmUUTeLT-cKzVOsTMi0LWVfI2S1BpLJ33Ustkx0ERUcKGbiHmtYFH9r-C1mlKCkZRgn0LEmCZ0idxJPhXStMpeb4DqZyxpn0Sgu8WopYLQ3EKRQDask_XX2yFFizXtrcosjND0b3bTwOyDFB8WzE6uL002ZbzYK_5Ab4OUk4h4Yrl1KRDhKoDyCFt6OaCUgwys6vO3Av-yeVNnSQr7qK6hhrJ6Xso5cbJ6JCyEcgV7jgdiRu0ejeheh-B-ZV5Oh-yEZ5pCaAOX5IBpPXyXhnkHYbmea0kib2fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/579850fb0e.mp4?token=TBee5jkllklEGCaanx3_n7C-uTx825lpA850v2xblUgHTkcxK54YEmUUTeLT-cKzVOsTMi0LWVfI2S1BpLJ33Ustkx0ERUcKGbiHmtYFH9r-C1mlKCkZRgn0LEmCZ0idxJPhXStMpeb4DqZyxpn0Sgu8WopYLQ3EKRQDask_XX2yFFizXtrcosjND0b3bTwOyDFB8WzE6uL002ZbzYK_5Ab4OUk4h4Yrl1KRDhKoDyCFt6OaCUgwys6vO3Av-yeVNnSQr7qK6hhrJ6Xso5cbJ6JCyEcgV7jgdiRu0ejeheh-B-ZV5Oh-yEZ5pCaAOX5IBpPXyXhnkHYbmea0kib2fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیدار پزشکیان با نخست‌وزیر عراق در حاشیه اجلاس سازمان ملل
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/463987" target="_blank">📅 21:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463986">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d79e1a0646.mp4?token=pwrPH2tW_XNDI2rl-c-A5u4Mq8qZYRoFwIAjl8S6ThyXDVPEAIBZ-M52ZF9HnAjNqEHKj3c6MVdMLdmkek6CJQrf8cUuur3eFRoFbefhM1W9elOCzqXCrB9FOJqIvXCBynbOlGnxKhbxv74GK-qvZj-lihwvhMLEBvJT1PaIFwlodyvFhiVA-1wWJQ6cfwWo1vHvSyUMDT4P7GexsK_rAAm9WN6L-vWvVEK5m_wdOnAPO12bI44zMSj2S-pGfNUnftYuh1JrJYUvV7MvUQMphaa3oztu6BA2oSqcJe1BMm4JVMAGZrah81ueAdxliFx1uRLtkp6DcsxBRrg8K8EC7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d79e1a0646.mp4?token=pwrPH2tW_XNDI2rl-c-A5u4Mq8qZYRoFwIAjl8S6ThyXDVPEAIBZ-M52ZF9HnAjNqEHKj3c6MVdMLdmkek6CJQrf8cUuur3eFRoFbefhM1W9elOCzqXCrB9FOJqIvXCBynbOlGnxKhbxv74GK-qvZj-lihwvhMLEBvJT1PaIFwlodyvFhiVA-1wWJQ6cfwWo1vHvSyUMDT4P7GexsK_rAAm9WN6L-vWvVEK5m_wdOnAPO12bI44zMSj2S-pGfNUnftYuh1JrJYUvV7MvUQMphaa3oztu6BA2oSqcJe1BMm4JVMAGZrah81ueAdxliFx1uRLtkp6DcsxBRrg8K8EC7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آب‌تنی افعی شاخدار در آبشخور پارک ملی سیاهکوه اردکان یزد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/463986" target="_blank">📅 21:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463985">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">ترامپ پوتین را به نشست گروه ۲۰ در باشگاه گلف خود دعوت کرد
🔹
مارکو روبیو اعلام کرد دونالد ترامپ، رئیس‌جمهور آمریکا، ولادیمیر پوتین را به نشست گروه ۲۰ که قرار است ماه دسامبر در میامی برگزار شود، دعوت کرده است.
🔹
در ماه آوریل شایعاتی منتشر شده بود مبنی بر اینکه ترامپ قصد دارد رئیس‌جمهور روسیه را به این نشست دعوت کند؛ نشستی که قرار است در باشگاه گلف رئیس‌جمهور آمریکا برگزار شود.
🔹
روبیو نخستین مقام آمریکایی است که به‌طور علنی این خبر را تأیید کرده است. او روز چهارشنبه در جریان مجمع عمومی سازمان ملل در نیویورک به خبرنگاران گفت: «اگر فقط با افرادی دیدار کنید که با آنها موافق هستید، این دیدارها بسیار خوب و خوشایند خواهند بود، اما هیچ اتفاقی نمی‌افتد.
🔹
«برای حل مشکلات، باید با افرادی دیدار کنید که با آنها اختلاف نظر دارید یا ممکن است با آنها مسائلی داشته باشید.
🔹
«بنابراین، ما رئیس‌جمهور پوتین را به نشست گروه ۲۰ دعوت کرده‌ایم. فکر می‌کنیم این فرصتی برای اوست تا نه‌ فقط با رئیس‌جمهور ترامپ، بلکه با دیگر رهبران جهان نیز تعامل داشته باشد.
🔹
«امیدواریم او این دعوت را بپذیرد. اگر این اتفاق بیفتد، در ماه دسامبر فرصتی برای این کار وجود خواهد داشت.»
🔹
ترامپ همچنین در سپتامبر ۲۰۲۵ گفته بود که ممکن است شی جین‌پینگ، رئیس‌جمهور چین، را نیز به این نشست دعوت کند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/463985" target="_blank">📅 21:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463984">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZ4N4Rc2Yv3u2Fa7Wf2cUYIUO6L-GaYUt4Unuqc41XMlhmhm-TSinl1MqyXxdm6inXNq0FosK2Pr4qAJhTlMA_aMcY5SjKMldEh6d8c_HEaHdwUqcnudZK9zNOmhPranrS_LgjfcvJ-z7EYOy7dREcH4CBrtkmIVfqcbjegC-FbiNti3tRu9bCRvjhiXwInRHPxnWN6k7YNpWxiqr4LxSfQRWoWY-ojdpVAA4E7UowizWrJ_egKBJokfrAeuH0cvkAk0O04GpvR2H55UXgj7FnWFnywBPmpw8Hz5Y-oJypOzuQCEbZdQAVSip3t9HBjjY3sc3pdWL6w-69-yWizdsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به‌ دنبال ممنوعیت ۹۰ روزه صادرات گازوئیل برای کنترل قیمت
🔹
به گزارش پولیتیکو، دولت ترامپ در حال بررسی طرحی برای توقف صادرات گازوئیل آمریکا به مدت ۹۰ روز است؛ اقدامی که هدف آن کاهش قیمت سوخت در بازار داخلی پیش از برگزاری انتخابات میان‌دوره‌ای عنوان شده است.
🔹
بر اساس این گزارش، قیمت گازوئیل در آمریکا در شرایطی که جنگ با ایران و حملات اوکراین به پالایشگاه‌های روسیه بر بازار انرژی تأثیر گذاشته، به میانگین ۶.۵۲ دلار در هر گالن رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/463984" target="_blank">📅 21:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463983">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9947a74c6.mp4?token=p2-xLL9VstCBWofYAtHDxMq8dep9_Qy3MEhnklcRTdH0FmpioNb-VZUJwSQLrLxPQowBlklWBXqAwCkJ9BR2gOduXbu8Jw8JxS6a7K2ptCor-bNuYAoWREUi8MwAF0uqpqavxJ935p4bBvXNbwvkVYW3h5gnGCGLCmixrTtvB8OvOLUfOmnUbFlsVYUzwI3SSnRe6WMe-s1N_iDIA_78YGnq8J3nPZNvN_J4BplrWgMBt9wCliQF2cK6q81prK5DVdDgQNGRC5DNuyy1J76mkYwGdPnNFpMx4M7Wr7D_afwsf2DO2dBbrPXOmUXYjVMs0zoRfYlJRnGyawJufIn35g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9947a74c6.mp4?token=p2-xLL9VstCBWofYAtHDxMq8dep9_Qy3MEhnklcRTdH0FmpioNb-VZUJwSQLrLxPQowBlklWBXqAwCkJ9BR2gOduXbu8Jw8JxS6a7K2ptCor-bNuYAoWREUi8MwAF0uqpqavxJ935p4bBvXNbwvkVYW3h5gnGCGLCmixrTtvB8OvOLUfOmnUbFlsVYUzwI3SSnRe6WMe-s1N_iDIA_78YGnq8J3nPZNvN_J4BplrWgMBt9wCliQF2cK6q81prK5DVdDgQNGRC5DNuyy1J76mkYwGdPnNFpMx4M7Wr7D_afwsf2DO2dBbrPXOmUXYjVMs0zoRfYlJRnGyawJufIn35g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقامهٔ نماز بر پیکر آیت‌الله شبیری زنجانی به‌امامت آیت‌الله سبحانی  @Farsna - Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/463983" target="_blank">📅 20:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463982">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f070b601e5.mp4?token=PStaxrXprKeyqNaVcXi-g0jJbqS8z_mMmdCrw3WEZEXKrYJO-x6YOzS47amBmhh60reIKmIp-Bqzgk-5GxkNzfqgikVM4PNrn7EnU7NSZjZ_YDnnTdOnoFU45Yr2lc7P22_h1DTIlA7tc3QCVhdI23_EsQnUNy6T_G6MAUmYIXTOISl1yrVcUd62rp4a4MB_RGE0ZsiM8QoN_x0EFZ8JqJdGDpbRXBBDMXZbExY0wwOwi15kaN5ww5apkQAGQLTfNvuR--7dl8R1k621La3BrqMx0KLKRDLzbij4mZKGJh-URxtA9cSzk41pjClRFtcyzeYmUhwtiqJ0BEdOD-1AQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f070b601e5.mp4?token=PStaxrXprKeyqNaVcXi-g0jJbqS8z_mMmdCrw3WEZEXKrYJO-x6YOzS47amBmhh60reIKmIp-Bqzgk-5GxkNzfqgikVM4PNrn7EnU7NSZjZ_YDnnTdOnoFU45Yr2lc7P22_h1DTIlA7tc3QCVhdI23_EsQnUNy6T_G6MAUmYIXTOISl1yrVcUd62rp4a4MB_RGE0ZsiM8QoN_x0EFZ8JqJdGDpbRXBBDMXZbExY0wwOwi15kaN5ww5apkQAGQLTfNvuR--7dl8R1k621La3BrqMx0KLKRDLzbij4mZKGJh-URxtA9cSzk41pjClRFtcyzeYmUhwtiqJ0BEdOD-1AQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نفت: پول نفت‌هایی که فروخته‌ایم درحال وصول است  @Fasrna - Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/463982" target="_blank">📅 20:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463981">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a00c1412f7.mp4?token=AZJ6zinH_z1piFoHP9Bk3Fcrjecojac3KipKObhfSc4svcmjghvtrquWjWwc-27_s7i5Dik_g19FnNZifaybC8pH0IV9eMbDFBRpWjf1u6dwl9RDHi-84BzsSnR1Bv1ivKbigJwvTD3oOf4t9B_oYnTp7YR5WCwEnmrW7SWEoGS9vKoMR45UfYxpM1dQpF6kQpALWbzwVymYiMF-7OB2J_AKRDs8gQicBDWdbRBjO2nluwFYggq_U96OnfDidjYuEcnNJlrI50XULKnoVxkGcl9twnW7QztCp7gNeX19i-cENRL-bS3KgfbF9XMltKuk4CfAU38EcMrrOy7Dp8_-qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a00c1412f7.mp4?token=AZJ6zinH_z1piFoHP9Bk3Fcrjecojac3KipKObhfSc4svcmjghvtrquWjWwc-27_s7i5Dik_g19FnNZifaybC8pH0IV9eMbDFBRpWjf1u6dwl9RDHi-84BzsSnR1Bv1ivKbigJwvTD3oOf4t9B_oYnTp7YR5WCwEnmrW7SWEoGS9vKoMR45UfYxpM1dQpF6kQpALWbzwVymYiMF-7OB2J_AKRDs8gQicBDWdbRBjO2nluwFYggq_U96OnfDidjYuEcnNJlrI50XULKnoVxkGcl9twnW7QztCp7gNeX19i-cENRL-bS3KgfbF9XMltKuk4CfAU38EcMrrOy7Dp8_-qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نفت: پول نفت‌هایی که فروخته‌ایم درحال وصول است
@Fasrna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/463981" target="_blank">📅 20:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463980">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNVo6p9SR0G14h8ke4Py--SvFTD0jMbLVeD9Cnh00Powqaawe3Cy35BjxhkVr8pY66F9_Bn4zEWde5hpDFZpzPV1Lu6uS8gi05qjaAobXrMnW2fI7i_SrX4Oq_6b7OKFM8V67XPOABqVMlb2bNQwgxlCt0ikswhaE710LKB7JdKVT0fKl4twpTnhqLS118aCMjKE57mbFH7d7oQrO4EgppeJWyLRYR1Dm0kNbf-Yvkfsvd1k3LQEmCrOTw6ApW3rlLc0fHfFqnGMGgATNdg_F9T-tdeTVz5MaA_6UEKGOEFPcJFxAJcIVO64JSN0PlgO4Pm5YmGEMUwju4XuLy-GrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عارف: امروز نه پزشکیان بلکه یک ملت، هم‌زمان و هم‌صدا در صحن سازمان ملل با دنیا سخن گفتند؛ از اقتدار، عقلانیت و مظلومیت
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/463980" target="_blank">📅 20:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463979">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa7e3c5727.mp4?token=EK8Wd1PYcGCZwO8ue9RvHKNjLJNqmStVqSzQm9x2p8SHUR4K7j3jNY-O_cbwX5omTEioEb_992B8TiwBeeaGcmtLr7wgmrnCa98I2drGFhYexhBICVHnL6xrAqvnWixJryt-DSjCX9sNa-VgSZk7kwIqqB2yaMdIv5WwQCtDfD08oEw1M88LMIehSSMLVVpmMxHM7eTJdFN5ABgdFVgUEY9_lRP_k2vF8QqnpEY-zEIe1rBs-EhQhguJXjsadfCVkUgm8VlbsHYmji7dT1Hjj8sjLe_6VUlJd2j02fv5UNKmIXKOl1PSTAooVc8gh-zPg24p_XBaR57MchOQyZg7Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa7e3c5727.mp4?token=EK8Wd1PYcGCZwO8ue9RvHKNjLJNqmStVqSzQm9x2p8SHUR4K7j3jNY-O_cbwX5omTEioEb_992B8TiwBeeaGcmtLr7wgmrnCa98I2drGFhYexhBICVHnL6xrAqvnWixJryt-DSjCX9sNa-VgSZk7kwIqqB2yaMdIv5WwQCtDfD08oEw1M88LMIehSSMLVVpmMxHM7eTJdFN5ABgdFVgUEY9_lRP_k2vF8QqnpEY-zEIe1rBs-EhQhguJXjsadfCVkUgm8VlbsHYmji7dT1Hjj8sjLe_6VUlJd2j02fv5UNKmIXKOl1PSTAooVc8gh-zPg24p_XBaR57MchOQyZg7Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روح کودکان میناب همراه رئیس‌جمهور بود
🔹
انیمیشن لگویی از سخنرانی پزشکیان در مجمع عمومی سازمان ملل و یادکردن از کودکان شهید میناب.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/463979" target="_blank">📅 20:41 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463978">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1bs6UAET2MwURaAcOxjgAKjKRFOen7z0gHEi-9WnecNHy_PekVeDkUKU4Wj59r0iBmaqfljE_gj8GhC663PcEecr9IXxE1oZLZsi792begYFOWI6Mo19l1nWTTUKeins2PbX7G2ZXK7Agqhk9GWAccdIXuVQ-u1VG7ep9bhPAV_sFvrH8NxHLzfKy3Cs6pT1mBVlGlYfhgSkUo768amxKkvbtKfgSYEFwti8uGP2PUxA87gy0C2rIbYYOUWVRtg_LMgvIHX_6vTiJAgSGcoLUzsEwqfpcShyn3qbYJ6iRJEbETwcLmquv0lrQigY9bXJj-6sz4vP0ZSEdvuYVaQ6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ هلاکت ۳ تروریست در سراوان
🔹
معاون امنیتی و انتظامی استاندار سیستان‌وبلوچستان از هلاکت ۳ نفر از اعضای یک تیم تروریستی در درگیری با نیروهای امنیتی و نظامی در شهرستان سراوان خبر داد. @Farsna - Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/463978" target="_blank">📅 20:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463977">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GiqGPIPLYfbqKq8g78jBQr9cLoX3AWkJjg9xsAOMUpI6XpsF-SXm_0et6w2ozJhZ6xB74p3lPy-1BUIeFzcKZmmrP64HeEynC2AnTs1wQaYG1alvsWi-2XYK4_cL6MnLtVQT4Q7GBu2ekIgV1oUih5ATT1iDVLuvbV5FUx559-vrggh-r6sUw_mO6_adOesu0v-TrEHio50Ai2f8DSn3yW0l7i0FbObJoh6dnzrwoKyfKQfci4tyX65_lvJ77ud1LrdadNnWh8xhxqKHVk02qGktaJfocxl5xX_rmttr1e-Fn238rpG1hiIZyQjvFmxh97K-fkiLZoYRmt2K37cmeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دومین شانس تیم ملی هم رفت؛ کنگو، ازبکستان را شکست داد
⚽️
کنگو ۳ - ۱ ازبکستان  @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/463977" target="_blank">📅 20:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463970">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YqvJUneg5l9aQ-afniVpiy8Nv-GTQ6YNDsBr6ZrW2t-2vjZVkltFcdeUDQqxkTgzS22p_dwO3NuIZpnf4YEJq198ura6URmt8eIheIHRal3aQdXRNElkhiOY8CB_Iqw-l6ooMEgWUYw5DGa_jzUgHqyKaHWCiw-CCKgTH_TGDnj4PvcuVZsw8m7lC4f0QE4tDGS3R_gHqGHnZ15fbEuU3jSRlzDpz5orbQy2-ENcd6D2VnFvcdJknUnLWGytgXH2jYfzBF7ruEz30yqk-fYlhPuHpdl8pvWeuk_218VtY0ZiwHU07bSF2M-FV7gZTifu3bLWHgNJAWKf98Cw_huNGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EWDCn5iuYDt1t8mN1SOwMS_HXTx7oj1Ql0BPP9BeHAXP_s9sJoXu8Ee3yqi84aEOod7ZrPD1HnM19_GEkH_0S5kKxNh8wGqDwFQu2A1w9ytLsf7n82fm4sdL6WRmK2hkajiNX8DYb7UiBQlx4Bmw0bcDkOtJWoIZ5KguN8mPA5kKaYYU4ypt-VtB9YxWSv30d-M5hvrctQIbOq8gJwpbv_qzMAs1Uf_uBinwSoRAwprEimVvHfvmli7bjcbUUlS9Wgca1GedehG_RMElVfF0sh8g8E52xh-tXJ0UdUbhnFtYjrsdY7mr76no-PFZz6x_t1VTNA-T8dY0QA5XqASp7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WNnRWra2L0sc7csuDmum2T6Kat3zanFRQGTlXuBz1-E24-ges06nkRMV_sSx1QlQpdtmhRWeKXgHWsrQsKQAK5-arKQsacDmoJw4eevvBFT_uqFdP-mALibM9d-pN1yvMXev0qhMEkTVZQYrIi73cBAwSCIf6d_MkdVfPW_UazB5i9ekFJbvYVNrEcFLAxECrbFeupxLDrZMTY9nhDh5XAzI8FkdHfBaxSkDVSGk76kt-0NxwPMeW9eCeDscRhxV7_01M3yAsl01F2wNI2bVcCwbS4dKsfP_3BYwzt8frOKvkEwK0pa82V6RQkEUi8uy06_Cb9U2r4iVOC-kyjsvJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L6B-RhMGAhmtha_NWcHcZ-G3M_ty2cXOpRNLSwuRyzzWY5q9bhxGEA0Myy0MRi2WnIEbO45iMk_3imIj6gwWUXOIB5CfuYeZSDEQOqBU3xdmJbzvPHUKCxn_qpPWEFJkwUow33rDMveDmLxZabNyE5m1zmIsQHpzqJ1uh_ZeHn2e1Y5r7hINrx_AgYHLRcllOZRtHS_fmufn5moHeuOfKJhMnco6zRjCbpDyuI2iJYAYrzNbLsXiqQV9okdmKtuOSwg7ISpApxqw37JbSl5qgmDnU1NYAAD3hx9KZBs4aNaDEwbTfwahdb3x6aPf9SDI-YkUruRN28lwFFJcoHI1kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MIKSP4VeP-Ck2WQXeoCikeHTjyHafM5UXMAeSlMgCgboQarF9Y4Hg4sTrAVBHvFK-1yHI2bKkLZbP0eihuZRZ6tbc9MwWo4puUQbsAPl5hEdBrGnEGajRARzfqSCqqD6y71lWNr_Ou4sJTpdhpBQ9DWgfEE5A2_S08ytzGz10AdXx3jOFKyljQKXjTBoZzv0AE-8dM03mTqUkBtyHclrTzSdTDAP2QxS_bK7AfkmEh2hTvwtBzT0hJLgRTkgrqwfags29DrGW8WvxRB5sImb1EgHXDBibYXZvFqZ97p-Fd3ZAV0mNFyTTVXjOm27zlaMUPRN9fDq-frfy7KhVvcn-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZNcRpQuiVTlMWgtNUGQoPzhowinGeXoa1s6FxiMAUbU391eV67MgN3dfhizt2w_IZVCSl5B6dP4softLKNSaxc7U6Bf3xqU7tR0hHapw8sgjmew7k4E2h1lQx2N9i7cBrJ6hZ8UJywHXM8GDxVRa0NffZjRC0RubW3VFqq4mqQrb1QA_1gDOJDapRU35K2YgdIXeqhlsr-EBVQd1YzKaoR6MdzRh1YWZ1UNoYHoy20gN4lvNSuyTQC7lKXEqp-0lu0LVVg5UENLDcAmI01-Lwfsj3ThDR44QNXkkL1LS69mNFdWz3_yzgDOVu-8Syn3-gu4RzBdmq49Nf6ZuTZDXYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IY42lHoIXxIbxfokeBlkfcjUekLJgwMsJ2NkjPow-pcyLNsGQEGZLx8ngRd0SnNS_DNOK7WjBfEHsM7hnMwYZ-rYj7w8PcpDKg2h8Hby0BztwUeu-0UeUVxjb45IZE_Z_Ht8B4SmB_l_3Om2KRHVs8fTfC9eVFY2t2U1AIQi_TVyfCe9GP62_A9Hh3Z1NwmOAUfB0EuNnIsi5Jox0-3ofu5VFK8aOtlAtbiRv5usE07XynejtvcrbOpfx17qJ_2zXghtxFAPa8pmi8LUZX1DrcWNqgMIa3Hl8zy5hZaL8GtkA2pvo8PAYa34PdxlN879nnP2TRjqNgF5Dd62NGmbkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
زنگ اول در مدرسۀ روستا
عکس:
مبینا لطیفی
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/463970" target="_blank">📅 20:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463969">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">هلاکت نظامی صهیونیست در عملیات زیرگیری
🔹
شبکه ۱۴ اسرائیل از وقوع عملیات زیرگیری با خودرو در جاده ۴۴۳ در نزدیکی بیت‌حورون‌ واقع در جنوب غرب رام‌الله خبر داد.
🔹
بنا به اعلام رسانه‌های عبری در این عملیات یک نظامی یا پلیس صهیونیست به هلاکت رسیده است.
🔹
عامل فلسطینی…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/463969" target="_blank">📅 20:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463967">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9p_H6-QSG5HQbOuxH-4VmLFqGM9H0MfA-p6Ec-yeIfxx75-TLdzPG2A0cYnWphAjRIMIsRwKhUX3EAF2tPWkaxyVy2dpo1OgxVeW3BLSWs5N2iJ54gb2SALx07nC3VqoUQN0lX-Rb_rrnaMAI_UviM37PdOchTfTUDaWT27sKJU8QYZLLLzt7LZmVK0r_85L62LdTo7AHGnrhoZFyFTGxiGhz1Crj9Aebo-c3wUQ74kLZ-PJCb1NPGMXDUbb1pleT3cqhnsc-gH_Njy7m1nwEEbdPXmPBmEserj_POMuxeiLsf2aQAcGO4yP7FV12VZtys3PHSowIacQatexmKqXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان در نیویورک در هتل مستقر نشده است
🔹
پیگیری‌های خبرنگار دولت خبرگزاری فارس نشان می‌دهد رئیس‌جمهور پزشکیان در سفر به نیویورک به‌جای هتل، در محل اقامت نماینده ایران در سازمان ملل (رزیدانس) مستقر شده است.
🔹
این اقدام با هدف کاهش هزینه‌های سفر، برای اولین‌بار توسط یکی از رؤسای جمهور ایران انجام شده است.
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/463967" target="_blank">📅 20:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463966">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpaFaui-4NOkm1ddPaL7XqfXgtet4_MjNQZNGCyH2HH3fVPDAuhLF1ZseDm82p9uX2p-9VVaeP463JCuRPzE4-IuORtTF-zHodug2HCY3-mg2gVkR_8k4ad7F1G1B8flLUOVSiElquIZed-0N2y3YymeE0GquwcdH0jKV4vJkl1hjubnh6hdNq1umV_DN7KQegPmLYc7UsZECzJoNRpFOxcEi4roTE9Hj7DfwU0kLMCS0UjB0UjRzdYzYWarMkH5G9yTJwmxG7_lnrgDykJWEQK8E9lI2EDL6YTdTZZAD4lZc1Eg_Hcg1qMnSm5P7zZStDVtTIk7YpBoIyWNt4q4cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائب: ملتی که جان‌فدا دارد، پاسخ تهدید را در میدان مشخص می‌کند
🔹
رئیس سازمان بسیج: ملتی که بیش از ۳۰ میلیون جان‌فدا دارد هرگز شکست نخواهد خورد و پاسخ هر تهدیدی علیه کشور را مستقیماً در میدان نبرد مشخص می‌کند.
🔹
سازماندهی نیروهای جان‌فدا شرایطی را فراهم می‌کند تا داوطلبانی که برای حضور در رزم اعلام آمادگی کرده‌اند، با ۶ عرصۀ دفاعی آشنا شده و توانمندی‌های خود را ارزیابی کنند. نیروها پس از این ارزیابی اولیه، برای دریافت آموزش‌های تخصصی‌تر وارد گردان‌های دفاعی می‌شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/463966" target="_blank">📅 20:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463965">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TybBP12BmUv2w-5gKJS-sB2d3axjGWJpMcmFRYBH6JEYf_sn8vDvWqIRZzVPOGwOFytnEgyGWwGtjyVKmTUu2Hlj8cdlyTZ0W9bsexnxW-VHAhFDp63Da7riHWXznzbYHHHtaeat0LVwbaS_JjlfdclIOvzDCgYjX-r9FMBcXDoKyrGOYV30HF2GipvGPkVpsreD46h4vz5bGr0QjgnqahUJp637k3HSkJFN7-HhdXx7VKnqsU158FAiMVY7mfdIFOtoNLYl_vNjkvUHq3xhmcJr_B8JfTsudUUFMrW7_z-ViymZ_PtBSO7bodfiJYFmWdT99MKysULsm_18ycubQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
دبیر شورای‌عالی امنیت ملی: دیپلماسی جدید ایران به گذشته برنخواهد گشت.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/463965" target="_blank">📅 20:08 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463964">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dfc948a6d.mp4?token=vPV2oT6FoupMX8-VGg5-x4yZoLZMgDAr6L_dpUAiQ4iZMC8D3eJtUJNGT2yUjMRTuiD2S_GU6BPIyYutY4g-uSPidH0phkn_YX7CocRkkPFrc1QTkZdkF77F5bgR4lFD9RNqhtY0V_2skmpdYfUGKyixY9sEohrrXShQ4zVTridBBj6CfiUh3_pOArYOnsYX1JSODaos_Cw2Z0BBQHr-kU5N1j5RVarCUQBO9eTixg8jpgc_Fl_610rTrX4OFuIk6iEuo6hJzI61I4ci6eXJkIxgJ8UCpwr5iRPLO3ez1mFIjUMv-oIdNH8Q6KjCwEdby9JkdSe4KwIPdoqk8srcHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dfc948a6d.mp4?token=vPV2oT6FoupMX8-VGg5-x4yZoLZMgDAr6L_dpUAiQ4iZMC8D3eJtUJNGT2yUjMRTuiD2S_GU6BPIyYutY4g-uSPidH0phkn_YX7CocRkkPFrc1QTkZdkF77F5bgR4lFD9RNqhtY0V_2skmpdYfUGKyixY9sEohrrXShQ4zVTridBBj6CfiUh3_pOArYOnsYX1JSODaos_Cw2Z0BBQHr-kU5N1j5RVarCUQBO9eTixg8jpgc_Fl_610rTrX4OFuIk6iEuo6hJzI61I4ci6eXJkIxgJ8UCpwr5iRPLO3ez1mFIjUMv-oIdNH8Q6KjCwEdby9JkdSe4KwIPdoqk8srcHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیدار پزشکیان با رئیس‌جمهور سوئیس در حاشیۀ نشست سازمان ملل
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/463964" target="_blank">📅 20:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463963">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39f6980138.mp4?token=AFswIVGYSc3ZykfUmOgXbXNher8aKpfQsYY6xydebL1HP4kKR-u7CnqNGu1bp-f0keU4HWBAMf8iTapA_LGsrZCY34tLHmqBTZyxBVPUSNG4bBSd7nsh8r8fsitjBPvw3jMr0nwqJ9P6uEiNxWk4sFqykXpe3lryDKIB80yjw326PIb9MQ3trxCBBnXfFAbXboQF-rIj93ULgcLcE0fc9gIhBnr27Ln2At7_evca7Qk5-l5ZLkw4zl75VF2TzV3eqJRorDVzDXCVv3K8Bebttw4wSlbeu9PysnIfBKFLHBOJMkPD2A9NxXLVkjgurwFvafTTsAtwpNT_iizG9nRlhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39f6980138.mp4?token=AFswIVGYSc3ZykfUmOgXbXNher8aKpfQsYY6xydebL1HP4kKR-u7CnqNGu1bp-f0keU4HWBAMf8iTapA_LGsrZCY34tLHmqBTZyxBVPUSNG4bBSd7nsh8r8fsitjBPvw3jMr0nwqJ9P6uEiNxWk4sFqykXpe3lryDKIB80yjw326PIb9MQ3trxCBBnXfFAbXboQF-rIj93ULgcLcE0fc9gIhBnr27Ln2At7_evca7Qk5-l5ZLkw4zl75VF2TzV3eqJRorDVzDXCVv3K8Bebttw4wSlbeu9PysnIfBKFLHBOJMkPD2A9NxXLVkjgurwFvafTTsAtwpNT_iizG9nRlhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
سردار آزمون در شرایطی که امارات خاک خود را در اختیار آمریکا برای حمله به ایران قرار داده بود، تصاویری از دیدار خود با رئیس این کشور منتشر کرد؛ تصاویری که از آن‌ها چیزی جز حمایت از امارات برداشت نمی‌شد.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/463963" target="_blank">📅 20:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463962">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c5551bcd1.mp4?token=MFJx_KPGOpVf8LwGx0eYE6npioRhk7X1t2akJzGxVBI8kDg8-HaaNkuUt2UOo-ESI-MtabSS8C2Po8F_rDA701gFqVStVwXCqfLBuqgTUmKVqF8hKi4Drhmdza68wCkZyhLQcl6BDHiyOk1T9TX0LnXKUaNIVtEwxN5Vr6iptaHx3pGC4dBFU3PpR0_a5m2w3El69avQtCfYwS1lm-MODdjsmGe8DaBI1078-1b_UCvSymGNzaTiUQ0LUGoSWvKy6TS1CeTrNxqtvvBGpqQ_hqIM0JlJDluwg6yMb-vT-kkn27Dnq7gmF4U826UgJIA7wmm-UvlQ9C_luUf9A5iVfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c5551bcd1.mp4?token=MFJx_KPGOpVf8LwGx0eYE6npioRhk7X1t2akJzGxVBI8kDg8-HaaNkuUt2UOo-ESI-MtabSS8C2Po8F_rDA701gFqVStVwXCqfLBuqgTUmKVqF8hKi4Drhmdza68wCkZyhLQcl6BDHiyOk1T9TX0LnXKUaNIVtEwxN5Vr6iptaHx3pGC4dBFU3PpR0_a5m2w3El69avQtCfYwS1lm-MODdjsmGe8DaBI1078-1b_UCvSymGNzaTiUQ0LUGoSWvKy6TS1CeTrNxqtvvBGpqQ_hqIM0JlJDluwg6yMb-vT-kkn27Dnq7gmF4U826UgJIA7wmm-UvlQ9C_luUf9A5iVfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پینوکیو هم در سازمان ملل سخنرانی کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/463962" target="_blank">📅 19:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463961">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/293587e08d.mp4?token=Thysjam1nwN2Z_p81uj_gDz71F6OknU3ow1SO8L8Ny2nlEjPQX-Nhr0yvrIOVFA05FcSRuAfp7OK6Gjo9AOsOV8UBPXyUnmP2e3Ae9atHkRhRd-3weUDNv1nGpmfVncCWnAfA8EyQjcXN-GfSnkJ9u03gj0LaABf3TynRPyqycZ6WyYb27nyjgV8UuW6uZttbI81FT4Jmzsgd62Lp82GAlt0lLupBJVGYphsx3bXElf6wA5kwEct9B0JIi02Sh57UhuF-_oBKGuN2npyeUHE7JvWQnuGRgrv4okeoSkyPSbgWN-6E9T8cV1jOGwGg3jJHwUsb76m4scli6F0Bdc_Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/293587e08d.mp4?token=Thysjam1nwN2Z_p81uj_gDz71F6OknU3ow1SO8L8Ny2nlEjPQX-Nhr0yvrIOVFA05FcSRuAfp7OK6Gjo9AOsOV8UBPXyUnmP2e3Ae9atHkRhRd-3weUDNv1nGpmfVncCWnAfA8EyQjcXN-GfSnkJ9u03gj0LaABf3TynRPyqycZ6WyYb27nyjgV8UuW6uZttbI81FT4Jmzsgd62Lp82GAlt0lLupBJVGYphsx3bXElf6wA5kwEct9B0JIi02Sh57UhuF-_oBKGuN2npyeUHE7JvWQnuGRgrv4okeoSkyPSbgWN-6E9T8cV1jOGwGg3jJHwUsb76m4scli6F0Bdc_Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پادگان آموزشی جان‌فدا در پایتخت افتتاح شد
🔹
در نخستین مرحله از طرح جان فدا، اولین مرکز آموزشی جان‌فدا در میدان امام حسین(ع) تهران افتتاح شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/463961" target="_blank">📅 19:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463960">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAXJTnWPTIdX588DdgItfKEeJTlHDKOWD3pGzNCdHNcTcW05I57o5X0nNqtUKxVkm84oFUpivJwUbcjWu0ch9IAOmOhsqeN9UN7YrwmPb-W7NrPryPTA9fNa9TjuRciKygrbWJ-TumhXz8n7w09kHV5o20myJFRxmPNbDenYNGfJynISxavhKfT2RtTVYK-5It8Hoyr99MOCPhmqqF7HGEKJ5n62CLy7kyt1EKM4-7KrXIwJRzbf4bWx5pmcA6SYq2YQ0xH3qBavYouBnohh-4g7OsPbDpkYvz5772PzniqUQ5V_l_Ogn-vDb42xYpBQGhi6poEsAApo4ZGwoKunow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قلعه‌نویی: تیم ملی جای تغییر نسل است نه جوان‌گرایی بدون برنامه
🔹
سرمربی تیم ملی در نشست خبری پیش از بازی تدارکاتی مقابل ازبکستان: در فوتبال روز دنیا سن یک عدد است و آمادگی بازیکن از لحاظ جسمی، ذهنی و کیفیت فنی اهمیت دارد.
🔹
تیم ملی جای جوان‌گرایی نیست بلکه جای تغییر نسل است. جوان‌گرایی باید در فوتبال باشگاهی و تیم‌های ملی پایه انجام شود و سپس تیم ملی بزرگسالان مصرف‌کننده باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/463960" target="_blank">📅 19:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463959">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RskOrnSeVW4M3V6v9Q6y1TScHIBKCjCAxS8J30u2JhM9ACsMlioAn8hoxQClIE9By2zYaoNTPkLdyeAe1W_oL4EaX7cXmbS6aGXvaO_qQBkPejvLW5Dwzu2yncxmgeSNXLbJUty49qsoRMbSanNGNlyobrY5Q4jbKJ31pa9mBt62ehUl_k3b9wAcYaB4yi1dZK4DJWUOkLAgnVlvW0FBcTpkGCg2AqcDypXWr6T6lacwyiZEqrDrs1YFIGhSbDO3_XV22P33oXF2_p0UVIKa7enkU5P5hlhC_XZu278hVeMYPrAVCUHXM0QmW7MBYQ-Uc9NkSsRfNOrc_1FkQpbabw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از نیم تُن تریاک در شیراز کشف شد
🔹
فرمانده انتظامی فارس: در بازرسی از یک دستگاه پژو ۴۰۵ در شیراز  ۵۵۰ کیلوگرم تریاک کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/463959" target="_blank">📅 19:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463958">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a911dbea86.mp4?token=DCpcK_9mMZy6clFvR4Syy-eMOFLvD5MmMiWPfli35fM3Zqp8fTUJdSvoK71dCaSqyqiHoL-EeFrYLnoeBCqT2q29SYMQSZc4dDiKjod2CKukuHK04b1LUNU43oTMwmY6VeoUmW3KUMcVDy3qxA84JOJfiDgtThGpVQz313dGBqQBuDd4Jk47Z7CscpTTYoW7eti5_lqHOcvmEOkns7jO1t0_jyYwxzhMI7AVYsl1vY543N-zTBf2vcsERN8jyxMjtDNMtSuNljSnR55FdbfETmCE5Hctl_PiK0v0cmF7sV_hRZlr9xCDuH1dpEGVIyZwR-zkb1d3mXdnlmBB3iVGRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a911dbea86.mp4?token=DCpcK_9mMZy6clFvR4Syy-eMOFLvD5MmMiWPfli35fM3Zqp8fTUJdSvoK71dCaSqyqiHoL-EeFrYLnoeBCqT2q29SYMQSZc4dDiKjod2CKukuHK04b1LUNU43oTMwmY6VeoUmW3KUMcVDy3qxA84JOJfiDgtThGpVQz313dGBqQBuDd4Jk47Z7CscpTTYoW7eti5_lqHOcvmEOkns7jO1t0_jyYwxzhMI7AVYsl1vY543N-zTBf2vcsERN8jyxMjtDNMtSuNljSnR55FdbfETmCE5Hctl_PiK0v0cmF7sV_hRZlr9xCDuH1dpEGVIyZwR-zkb1d3mXdnlmBB3iVGRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرپرست وزارت دفاع: دربرابر آمریکا از مواضعمان کوتاه نمی‌آییم
.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/463958" target="_blank">📅 19:41 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463957">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEpgVfRRQy31I-_gkfZcSoxMzZqD4u4k07KdrHqJKDVoA_gvYj3k3T-88if2J3pKc3lPgBlfwIjwHt1dftBNoAUGq23qh2jY37R0ykuc8O8L2Xd3RVhOCv2bUGe_tLjENOOBBQxanijKWSRmq-trh0duf_Yzr7cvu-xOxLnfkZ_59PBfZLyQvdv_0Er5xNs9uNdd4caCYSntVbgUGunB2GhVB6ml0BCLXFYo8fJOHx1XbWQquRMxOja_Gj6mdTEENKk99pWuwZgwALrzl6Ug1G33n2DJHD0cH-jRUc69zkjFdsgREitZBrKUXF7vYJAa2J_v7bpewvDZbl2-poOoRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شعام هنوز درباره انتخابات شوراها نظر نداده است
🔹
علی‌رغم انتشار برخی شایعات درباره تأیید شعام برای برگزاری انتخابات شوراهای اسلامی شهر و روستا در ۲۴ مهرماه، پیگیری‌های خبرنگار فارس از وزارت کشور و هیئت مرکزی نظارت بر انتخابات شوراهای اسلامی کشور نشان می‌دهد که شورای عالی امنیت ملی (شعام) تاکنون نظر نهایی خود درباره برگزاری انتخابات در این تاریخ را اعلام نکرده است.
🔹
علی کشوری، سخنگوی هیئت مرکزی نظارت بر انتخابات شوراهای اسلامی کشور این موضوع را تأیید کرد و تأکید کرد که تاریخ برگزاری انتخابات باید از سوی هیئت مرکزی نظارت اعلام شود.
@farspolitics
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/463957" target="_blank">📅 19:41 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463956">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc327c5b5a.mp4?token=XubKsGSZ9VzjhbPRzDdX1_5h98KAxS3NhcU6EMRkqWwJyDKePGl3icZ0R94l7JCdMKAONNET9om7_GXSqmdETIUguqlUgbjgLhBpY06PUhfaIsCR11rxPYwYGAEIX3vV4NIrYtKArscn8_fUuGkb6eUkJfvLXS--14MfIgE4UrJ3Frdirjls1EZFyFXFFb96IFK6rG2uzwKXDt1zExerz7pfovxXuZoEdDqgI0vQI8CSc_f7QFDi_QEzTW4ManTB0suyrh_uSQTuos3BFp_ZA5skTkhjKwYVOi0LAZPuwOs6jfr2SNm45102YtjhktIQxQTMTJScwqI5VHYoqtFNHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc327c5b5a.mp4?token=XubKsGSZ9VzjhbPRzDdX1_5h98KAxS3NhcU6EMRkqWwJyDKePGl3icZ0R94l7JCdMKAONNET9om7_GXSqmdETIUguqlUgbjgLhBpY06PUhfaIsCR11rxPYwYGAEIX3vV4NIrYtKArscn8_fUuGkb6eUkJfvLXS--14MfIgE4UrJ3Frdirjls1EZFyFXFFb96IFK6rG2uzwKXDt1zExerz7pfovxXuZoEdDqgI0vQI8CSc_f7QFDi_QEzTW4ManTB0suyrh_uSQTuos3BFp_ZA5skTkhjKwYVOi0LAZPuwOs6jfr2SNm45102YtjhktIQxQTMTJScwqI5VHYoqtFNHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ای لشکر حیدر کرار خنجر یمنی را بردار
🔹
مداحی میثم مطیعی در حرم حضرت معصومه(س)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/463956" target="_blank">📅 19:38 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463954">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fo49Au02syb419jPAlYRP_1T9qEiIvuIrEWV-E9mu2Q0kvkh8Sbwa8OKMDWYbAHzz2pC1pr3O8bpSkF3jGiX_sMluUAce6aZPATidicksVWGzG7bqVuWRIsc2pN8xlRFsNf0zQ3sKoZYrz7Ba69J0bmFQmMawB9xDFUDBsOB4_F2E-qXdlZZxrbimWUd8OgRS8F0GH3emtDYALM-I4BhKaDoSBVImJJxzAB0VVIqB4cJBqBzBTeC9r9fKcEti7z3E6q0_v6lLx2npr8lh8qZbGAEomwlYKYAIBRni0Ff_8okRjKhNXq1at7jeKeEn03lYSvgRMAemooxv530MKRpBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پیام مخبر و زاکانی دربارۀ سخنرانی پزشکیان در سازمان ملل
🔹
مخبر: پیام رئیس‌جمهور ایران روشن بود: دربرابر قلدر سر خم نکرده، شهدایمان را فراموش نمی‌کنیم و متجاوزان را پشیمان خواهیم کرد.
🔹
زاکانی: سخنرانی شجاعانۀ رئیس‌جمهور نشان داد پروژۀ اختلال در محاسبات مسئولان…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/463954" target="_blank">📅 19:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463953">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‌
🔴
دبیر شورای‌عالی امنیت ملی: مطرح شد که ۷ شرط ایران را آقای عراقچی به واسطه‌هایی که بین مسئولان ما و آمریکا رفت‌وآمد دارند ابلاغ کند.
🔸
تا این شروط عملی نشود نه تنگه باز می‌شود و نه مذاکره‌ای درکار خواهد بود. هیچ تحولی ایجاد نشده و فقط ما شروط را ابلاغ کردیم.…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/463953" target="_blank">📅 19:24 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463952">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8390bd356b.mp4?token=SxLbWDzS93QaozwQlA9jf4aHG3vjWoa-v0GDDtbadM8XXeZYWwdvGBVWYk2Gp1nQEIP3hCBUJ9SJaLbxCLIwULrtF69gQZINlY513hcnhuUV_GdLqnJtgDPs-YKM7cbM9hV0Bg2ep1SRSJrsRMxa-Ql1nhHCafw-yp5gzWlPkjgBbiVaZLjS5jnUdWragwBXJ7nxunfq7-ekOm2dygtZEWT4FJ9v1fGt-gKX3W4n-m7YtCjXHh5Pwq_mBYHQEuX5mRxVYNiZUnDV82EYe72XACFSnBVnWRVPQpFaUiRKrzP0rrbywQ-qX-KPnk44_Oqo_75BesrtuC7gnINj5O6xPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8390bd356b.mp4?token=SxLbWDzS93QaozwQlA9jf4aHG3vjWoa-v0GDDtbadM8XXeZYWwdvGBVWYk2Gp1nQEIP3hCBUJ9SJaLbxCLIwULrtF69gQZINlY513hcnhuUV_GdLqnJtgDPs-YKM7cbM9hV0Bg2ep1SRSJrsRMxa-Ql1nhHCafw-yp5gzWlPkjgBbiVaZLjS5jnUdWragwBXJ7nxunfq7-ekOm2dygtZEWT4FJ9v1fGt-gKX3W4n-m7YtCjXHh5Pwq_mBYHQEuX5mRxVYNiZUnDV82EYe72XACFSnBVnWRVPQpFaUiRKrzP0rrbywQ-qX-KPnk44_Oqo_75BesrtuC7gnINj5O6xPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملۀ هوایی صهیونیست‌ها به شهرک القنطره در جنوب لبنان
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/463952" target="_blank">📅 19:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463951">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3IM1IFEZF9sWBqgd2YJ9R-JLl3YjgAnLjEOEjXcZhQzJTZHLrk9yzWvS_VP_hF90VVR_NHuVIqT-_AewfbtDNoqfS8A73m3EvOWC1Y_Qsp23Pw_yafBhOcmqZNEWeRK2XIGy5jXq-6TChGRcN7Bzam2Ja1oBWIQNdhIOFAsXvOXsOvlveX1C77GXmhfWju9ppTyXl4u7rW63AILgiQ38SNG86Wn4VEZn094ygwNWE1wUgn9QuNVT_0cWM5xRGKeiWwF0zaeEuugWl7MgWAkmIg-Bq-ftnKU9tiFfz10ikKIfDwASNWww91wol0QJXmiLhfrvKCsJVMpwSg12sUAOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پیام مخبر و زاکانی دربارۀ سخنرانی پزشکیان در سازمان ملل
🔹
مخبر: پیام رئیس‌جمهور ایران روشن بود: دربرابر قلدر سر خم نکرده، شهدایمان را فراموش نمی‌کنیم و متجاوزان را پشیمان خواهیم کرد.
🔹
زاکانی: سخنرانی شجاعانۀ رئیس‌جمهور نشان داد پروژۀ اختلال در محاسبات مسئولان کشور ناکام مانده است.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/463951" target="_blank">📅 19:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463950">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cf5f4100f.mp4?token=cMyqbOu-qr7x5cO9oLibb3a7J9_TJJ0OlGKCBQ3TmswP50XF8NCcH1WC5A4PIubARpOc50z3gKbxhov0axQorEZDpbZZRFQ7fwHrqSYA2mYvNSkSPm2M8zfdEcC5QMv8NJnh74-mSoe0CtFRwYBAkPiyMAY5pbE-ON7L4R5E0oC4uFgaI1m8oxiYNRWeHudfEml47ZV57UpugoMnp9Vb5T4SceUyQfnHJxJb2clf_iXS_VxDguTz5VuIwW6orrRhhAA-OFfKmlqO5wrZYHU3fj4C0Pfu-2Q-gDTXohCAXLTLT0TRUe1GSTBfhYwKBPzqRYjsu94fHZ8_nJ1dyvPCOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cf5f4100f.mp4?token=cMyqbOu-qr7x5cO9oLibb3a7J9_TJJ0OlGKCBQ3TmswP50XF8NCcH1WC5A4PIubARpOc50z3gKbxhov0axQorEZDpbZZRFQ7fwHrqSYA2mYvNSkSPm2M8zfdEcC5QMv8NJnh74-mSoe0CtFRwYBAkPiyMAY5pbE-ON7L4R5E0oC4uFgaI1m8oxiYNRWeHudfEml47ZV57UpugoMnp9Vb5T4SceUyQfnHJxJb2clf_iXS_VxDguTz5VuIwW6orrRhhAA-OFfKmlqO5wrZYHU3fj4C0Pfu-2Q-gDTXohCAXLTLT0TRUe1GSTBfhYwKBPzqRYjsu94fHZ8_nJ1dyvPCOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هلاکت نظامی صهیونیست در عملیات زیرگیری
🔹
شبکه ۱۴ اسرائیل از وقوع عملیات زیرگیری با خودرو در جاده ۴۴۳ در نزدیکی بیت‌حورون‌ واقع در جنوب غرب رام‌الله خبر داد.
🔹
بنا به اعلام رسانه‌های عبری در این عملیات یک نظامی یا پلیس صهیونیست به هلاکت رسیده است.
🔹
عامل فلسطینی این عملیات به ضرب گلولۀ صهیونیست‌ها به شهادت رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/463950" target="_blank">📅 19:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463949">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">📌
ببینید/ ابراز رضایت شهروندان از مسئولیت‌پذیری شهرداری تهران در جنگ/ شهرداری اجازه نداد، پایتخت چهره جنگ زده به خود بگیرد
✅
در نشست قائم‌مقامان ذی‌حساب شهرداری مطرح شد؛
رئیس کمیسیون برنامه و بودجه شورای شهر:
🔺
شهرداری تهران در اوج بمباران هم اجازه نداد، پایتخت وضعیت جنگ‌زده پیدا کند و حتی یک روز، خدمت به شهروندان متوقف نشد.
معاون شهردار تهران:
🔺
باید هر آنچه در توان داریم، برای خدمت به شهروندانی که با این همه آسیب و فشار پای کار کشور ایستاده‌اند، به کار بگیریم.
@farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/463949" target="_blank">📅 19:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463948">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AxDvPAzhffG7AHtuohWibRvuErWmtL23RdEXQr_jBiNqnpwCsU700wZPs9Kb4Fb-Zo5jVr5nPdlSJlXxMz2CF4JGgevK6W1pNU_TU1_7Mk210U8hWMhyarGDm4ww0XFw5TMb1Yxg_MqxVbxQWAwa-wo1fuY3aUUmyw6c5U-_swcEu3RIfb4tEEXlAqW3L_aOcC9t642xE_Wd7KDiJoCjY7X_Xvqgu5Crs7Hm9OdztkfZS7LAai4_382A2V5h8sb7V3S20eFa5o_eHeESmEQE3-4by7-HGXL28-xoWXIOCkxCLRio03zjqY6wG17rQfd3lOO3-KYyNcVKdJ6gJWugDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ثبت رکورد جدید جذب منابع در پیشخوان‌های شهرنت بانک شهر
👈
پیشخوان‌های شهرنت بانک شهر با ثبت رکورد 12 هزار میلیارد تومان جذب منابع، موفق به ثبت دستاوردی جدید شدند.
👈
به گزارش روابط عمومی بانک شهر، محمدعلی بخشی‌زاده، مدیرعامل شرکت توسعه و نوآوری شهر، با اشاره به دستیابی پیشخوان‌های شهرنت به رکورد ۱۲ هزار میلیارد تومان جذب منابع و تثبیت آن، از تلاش و همراهی همکاران و راهبران این پیشخوان‌ها قدردانی کرد.
👈
بخشی‌زاده اظهار کرد: دستیابی به این رکورد، حاصل تلاش مستمر، پشتکار و همراهی تمامی همکاران و به‌ویژه راهبران پیشخوان‌های شهرنت است.
🔗
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/463948" target="_blank">📅 19:09 · 01 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
