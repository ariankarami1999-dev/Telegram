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
<img src="https://cdn4.telesco.pe/file/QvX0uhb0ClCPHSw-Xm2PJPLQNI0B3_pXXWi-7A76a7qjhRg82DsmhAOwB4E8UdYQi-JLbM7_sKBghWxKzVIqTHQDSCXItJ6N2OEFXv0UnTRGpRQ4_38Q3RF4QCzTALNrjBZRimvDTC7R-QQ0LRgakt0gyNJEyk1qQIDJn3zPv3ioj4WLH5if_BfIHfKJAexOJUoJVGwZrJPnyLoTHjAYQ6ynmohZVYBIPHCfzEQ0rssJ7b7NVMDG1fiSAhLnQ__ILUbT3WYz81drtm-Z0NbzbDDuCMFwVQtvfVA9tGlXa3TEhfook6t3NOM0D9oYDB12t0hl9Lt9bnN7POPUjMoU_Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 503K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaaa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-15 13:03:45</div>
<hr>

<div class="tg-post" id="msg-31131">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccUM4g8C7HAzSIvQuAAlNnhoJ4-xz4s7QQpN8PAZi9o-E9_A-RyknjHr8XpqMYzwyBxr_zCq6TAJ7JHlaUk--q4KrlIiBFeIfvYoDiQbZQ6CiuPZsUUjiQOgHizK4_z9cQJ_ovkHSlEvCLYJp2FJ0NSpUGw_3xob29D-rVRNYUqDzv8XVqf0xDsL0WctpjrpOomO4DHO1rVuZ8R5Zt_Mo0X1mRrGljbf9C9CxDsKemdsDN4AibBj1yw5FooiFEcJgyfsZf6hUuidGzRRIDkUCa03Q9AJAp85yRgWZE0Uvs6CMnPFM8HvL8QkicZsVNM5QIQi3OqsX5vGKL73EAeH7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
ویدیویی زیبا از تموم جام‌های لیونل مسی با پیراهن تیم ملی آرژانتین که از 2021 شروع شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/persiana_Soccer/31131" target="_blank">📅 13:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31129">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3ceb15f26.mp4?token=v9hjvaPTJg1W28x25ZgwBV1avj4Cu6Zm6VEUscvDsNqnD7v3dKrzXaNlEcveFnEIyHsQOnuaE4HQzTztp0S0Pg8hsYkG96Ssx5DtisBh7cwpOZqoZvhRV1EiBFY0BpE7Nc96fXEmwnjEXJMHeOZ9-ddNrWG5D_4A3JE6QHVl-8mwvUi60kl5EC9lOEvTra3Cbd_rP-vMpWuvohj14o9-f-2SBPeHeYeDEWWP3vmFkxSTS49VHxFMES-1Enl8JUc_kkUbPfSBEe8UH9HVO6uTinKZYLS1Rp4XIqxOknO7T8tUJV5CQ221U0aGzTtdJ8SOf5ctACxssYXbP7J1b8I0zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3ceb15f26.mp4?token=v9hjvaPTJg1W28x25ZgwBV1avj4Cu6Zm6VEUscvDsNqnD7v3dKrzXaNlEcveFnEIyHsQOnuaE4HQzTztp0S0Pg8hsYkG96Ssx5DtisBh7cwpOZqoZvhRV1EiBFY0BpE7Nc96fXEmwnjEXJMHeOZ9-ddNrWG5D_4A3JE6QHVl-8mwvUi60kl5EC9lOEvTra3Cbd_rP-vMpWuvohj14o9-f-2SBPeHeYeDEWWP3vmFkxSTS49VHxFMES-1Enl8JUc_kkUbPfSBEe8UH9HVO6uTinKZYLS1Rp4XIqxOknO7T8tUJV5CQ221U0aGzTtdJ8SOf5ctACxssYXbP7J1b8I0zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
دو ویدیو از علیرضا بیرانوند دروازه‌بان تیم تراکتور در پادگان حین خدمت سربازی‌اش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/31129" target="_blank">📅 12:18 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31128">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTdGd0R9KkgL4JIVrb4ygbtvKZJudwg9kJbE-A_HGTidNJaqGvsY3ICHpzTq3crVCJmsOSid0UlmOBkmQTkwsDYWuazqObvwc3FhRa0N6_DWURX6y9hgVXEkBX65CPLxYnarZDfTrh5TT5_cJup-04EJs3d566bdTRfxR1GkPnQNK9d00fcO2uiw4bSN3gzXWw3-CVQZ9YJKDWg3mZ5b2elyLsZgI59Qm8PUSqU9fpQnt_VHfyvChN53Winc-Jh_ZOGu-CgTwNuqkv31R4pWpL6dBXsSX8mjty6tX8mCMSr3oODTxPbjus41_eKy0rQ2fnwaOyQKOh4tkfjp3cSx3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
#تکمیلی؛ رامین رضاییان که‌دربازی با روسیه از ناحیه خصوصی دچار مصدومیت شدید شد حدود یک‌ماه دور از میادینه و احتمالا دیدارمهم مقابل تیم پرسپولیس درهفته دهم لیگ رو از دست میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/persiana_Soccer/31128" target="_blank">📅 12:13 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31127">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOL158URa9DDym1pILey9O02F1vYZQt0OKIDkFZP-0vALDG1Voss4_ri_VQfkjU9MH5NBQ3nuuFkBl0z5ZOiV2zbX1L8RFaN3Y_N37uaWH2IpM0M4HLGxm356SiUKDzuWHxFa3e8qBF3bd3s53veyDp-2WtZytSpJgux5jD_x8vMo2cwDwJKC_DJ_TkE8_uxAzIDIK9rmPUWfEMwYbkVIY5ADg_z2yx25D3yDo5jBWj9psLmhpWAZP4oC4MVWqVKBGUKQWl0uCvRE_wh9pmznebL2fiF2QCRm8ZYpmMPG-3YKQAvm5FaxVVcD297bl81DWMuCCLvQhXbyXLQpdiWJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
#تکمیلی؛خبرنگارباشگاه النصر امارات: کادرفنی‌النصر از عملکرد مهدی قایدی رضایت نداره و تصمیم‌نهایی‌اش رابرای قراردادن‌ستاره 27 ساله‌ خود در لیست‌ فروش این تیم در پنجره ژانویه گرفته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/persiana_Soccer/31127" target="_blank">📅 11:21 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31125">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce783c6799.mp4?token=k3GBGzKDxN2W-JLUFHGvSb4upE96CqhTlufuIuMn-3HcKh50IdoFG5HBgI2AAgcmBSCHJnWI8099KrBIXQzo6PitAtUzEXH_GUCk63uDjpIB0Xn3bvoKVItQr2SY_KCuUNGKheAYf8PguYBBhvk_w5kY-LKqXOShGYfrupXyJxEVIy18d_chRx54mhJd8AWLcsJRyIeTWfc_FZh0OsYMW4dxHg29NEXTfk0siX3SJmgJswksFB088d-syw7GGp-q2iQcI0PTvlLHZEh48cUOmd0hrp59nPwr-sluDKDvBR_wngyXpgPAKbJV1H9pRdv4jMf7seaIlNW6arg5j9lrbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce783c6799.mp4?token=k3GBGzKDxN2W-JLUFHGvSb4upE96CqhTlufuIuMn-3HcKh50IdoFG5HBgI2AAgcmBSCHJnWI8099KrBIXQzo6PitAtUzEXH_GUCk63uDjpIB0Xn3bvoKVItQr2SY_KCuUNGKheAYf8PguYBBhvk_w5kY-LKqXOShGYfrupXyJxEVIy18d_chRx54mhJd8AWLcsJRyIeTWfc_FZh0OsYMW4dxHg29NEXTfk0siX3SJmgJswksFB088d-syw7GGp-q2iQcI0PTvlLHZEh48cUOmd0hrp59nPwr-sluDKDvBR_wngyXpgPAKbJV1H9pRdv4jMf7seaIlNW6arg5j9lrbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تشویق و خنده‌های آنتونلا همسر لئو مسی درشب‌خدافظی لیونل مسی با پیراهن آرژانتین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/persiana_Soccer/31125" target="_blank">📅 10:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31123">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owHfS88_Jj5k0yh_l6j8HzL4EHsfGPv7thZCnQuYJF6-x7CI5yZoxOGz4672h7ltssDqotgM1AZoWsfrkMEl4VASeI02bpbSubdc0an4mervmcMBDt6BYOsc4rBeSLfzKE4o85TbzSFXh8Oi4M0WTMd2Y4fChX0ILfz75Vihtu6w-d3l1sLAWti_QqnlIO8gglk3b5LRVrEyKjW3f6xEO9MOxbZVdjG3caSycZ9iUn6oO_1fxfBipC_AcKnUMCVGcj_LHMGmBbeP2A5RIBuC2rifhRQlIhQzGdW-5-wsXnhZF1WY6h5AZKnVEh0eZb3-CeH2Do1-tUntwbs-_zwDQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد لیونل مسی
🆚
کریس رونالدو با پیراهن دو تیم ملی آرژانتین
🆚
پرتغال در تمام مسابقات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/persiana_Soccer/31123" target="_blank">📅 10:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31122">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSxECHxmE-fR4X1S4j2HDMqZ-EHFWP8c5mgFsLYsE4BzNy5qh71iQBbK4uX5EF0ic7V3pRc9jr8w5smoFj7YmL5Ca47LtFhT394Wf6mlTjpIaAygPcgvH9MXEdAD1NdMzZOIk-LoOMsC-GocoZWnMxoKmk0DNnOwQbxmk6gfxdYEuDql7kg6KGek78ERuGxdUjzYI4NBdfq1E9bk9lcEKP462d5XE-2qCFqaVgPOGypOKxOpl60s1EsIEzF4D9BS50s-CpguWUnkV6XNXD4JW3wQ4COUUeVeSaz-2USMCXS_OCYzwLjn0npkqp8tn2zfb7TWqed_cmfPqz9fTz9QTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تمام 126 گل‌ملی‌لیونل‌مسی به تفکیک هر کشور به مناسبت خدافظی همیشگی او از مسابقات ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/persiana_Soccer/31122" target="_blank">📅 09:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31121">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYq9WA_edKOLjIJEgGpbX1zDyzQddU_Ca8m6ecr1EnDWipd0evAladBbo4fdvrltsoFvmXeNSbEbcevVTakvIfT-_K5ixdHJn5RoaeI89KKyG5UZbUqlL08_x7-6XmQ6rBAk82B5my36eupWf5Vb7yqDAfZQch-QKrs1ytBEZJnGPtQhEHWcFbxb5gR_GqsZYH7Ph2umMfhi4N017sGmtsf-hkj0lJeB5xBwKdhfAaXtImkMz9HaFn-fgR6Tf_1ioBoD5QSOiWUikczeyYoR72SpHXdpCCiU2P9rqMKiWEh3EnkCeT9jzzvlErH8sTZDU57DHwbRniBY6EyYaNDnwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
هایلایتی‌ازآخرین‌بازی لیونل مسی فوق ستاره تاریخ برای تیم‌ملی‌آرژانتین که بایک گل و دو پاس گل همراه شد. دقیقه 10 مسابقه متوقف شد هواداران لئو مسی روتشویق‌کردند مجریان شبکه ورزش فکر کردند لئو تعویض شده. ببینید خودتون عالی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/persiana_Soccer/31121" target="_blank">📅 09:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31120">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">📹
گل‌های‌دیدنی دو دیدارمهم و مهیج امشب رقابت های هفته چهارم لیگ ملت‌های اروپا 2026.27
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/31120" target="_blank">📅 09:18 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31119">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCSSbCNPMwYS3UkYCWUE5tjOFkwajw0nTRBKiDbNV7fxu2Nlhc7DaXy9tvazjlHG86HWyCmdlsuJDN6VL0W8WjVSUZDJUFiiEjCbK8ttaw75bfJocSvk3ZHbbRj6jTycDIRtFqlyeRa4Jt6vg9Ccast87l9D-eC3BsCo0jM7_qgorEB6ArPQOd_cu18YmHlsFd0oVbZzP2WmS63xg-a1R4NZQVZo83IHPjjTtRjP-Q3GBoPFN7OZSGpe-8Og4fFSL0-Kprr_M0eLd5fbTl1t6EpyL_HYjEcMJ5eB22hYvPgdxek-o5h8CvjP6Th5oViSNSSnFX_2DVK1qUsNRVplBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدار ها‌ی‌‌‌‌‌‌‌‌ امروز
؛ شب خداحافظی لیونل مسی افسانه‌ای با لباس تیم آرژانتین و فوتبال ملی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/31119" target="_blank">📅 01:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31118">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LdPZs12Fwqw2IXAFC89nfVdC0HKjPo-AspWpnnLOSvPOBQ8JRGyGN6nX87x_egfasxuBsrDNqkJ6M3CNeVnA9uOmEfj-j5TlyMBcIuEcVnNLQYHDF13QvwBT8YyLe91h2Xb7nh9GzslCb4kltRGvnRF8rNw0i4jfeUoxFvviPNFY_kaRoJS7ALBqoHp1Usjx1myXHyeK1g2e05L6edt9TTztDADrYo4IPFbnvrIGo11_0pmr20fh1fFC6JZV92xNKESvGSaQeww09VVdX6NliKL_DyFveMOe-R1ws3_FtuA5dxEg1zpJoL0WJPp4boPCZQuwuQYxz0CLz8Lot_1DFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌‌‌دیروز؛
کامبک‌اسپانیا به کرواسی با دبل میکل مرینو و برد سه‌گله سه‌شیرها برابر چک
🟠
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/31118" target="_blank">📅 01:21 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31117">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✅
هفته چهارم لیگ ملت‌های اروپا؛ پیروزی ارزش مند لاروخا مقابل یاران لوکامودریچ باطعم کامبک و پیروزی قاطعانه سه شیرها با درخشش هری کین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/31117" target="_blank">📅 00:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31116">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpBCW2GjAoY7iv5Q6Bn3G0qFlsbqn8x1_0UrsdU4TemaYgcZLw7_3dm15ZEkqjyXTBSKvk81_f1DRQNN1cN-zLB74oMp6WmFoQ59x6iz4TK9QAZA8VupqbJI111qyOcCwWqtnkZ41aJuSFwCkxB5MET5QN2lgz77TN9PU2XWcPw0ncuz5lFPWlGnXDBduYLQ7KMp6VV8-JP4dehd3-ysukMGEYh5SxA4eGe8zHDWD807aMam4Hhv81B_6H1JCVwbneFfubSas7HeUhiIizQ7cPhe6aYeOl1nS2XhRkkVmSl3RgrGl-p_3Jiy8wmx4Dos88JH3PYIPdGa5xXl2f6OEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدار ها‌ی‌‌‌‌‌‌‌‌ امروز؛ جدال خانگی کروات‌ها با اسپانیای دلافوئنته پس از تحقیر مقابل انگلیس   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/31116" target="_blank">📅 00:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31115">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVxSbQNWOM4MTFtM-l_zT2BxBv1G1oQpiRitJr9rQrzMi4g1ikafm6cEgKXPdd48mONTHny2TNVZdj3YBAhI77DYE48kZm7GKhnMubMvuF6vDh7NVqd5U8oX5RnzxV5TzpZJ96jL1h1XiD7t2kpLw9zFn3ocQqz2zFH1NIzVa3HPU4LrNHtZMnhmyySE94DThRISmh7TkwBhdT9dNH4YZcp5bvXSSKgNlvL6eLh3KviC8XorHqQEED_uijnvdmtV3jkv6D1JBVd_Plf9DOqxMWtoCfBH8Jx31Y28-uamyomEtrsjAzpPdtlE_Vvq1Q0IRwYvsUXlx5-PpGdB4THGKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ نشریه العربی امارات: رضا غندی پور و مهدی قایدی دو ستاره جوان ایرانی شباب الاهلی و النصر از شرایط خود در تیم‌هاشون راضی نیستند و به فکر جدایی از تیم‌هاشون در نیم فصل هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/31115" target="_blank">📅 00:07 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31114">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUKILu61hNP-elk6tz6U38J1exzXZfSYLLyas3qqLCTTTFNPamIuKWilEMXcxiZJu56lySmOLiT-BjY6c-rUYynLzWiwEhS8rH2Fii83EnZQoymYYZ0LW3mJNSmXjPgilEOmIAqSJXJN0TfRH33woAJphdO5iMryPQalOESuW1I_JnXotUVoHeMpoLUFuQUmEkdJCZrXRRkf7IZU-EwqnPGf6QQZxbsdsbkRobwzOlY5ptq9TK1u7dLz2AqHz7Rn2fvqtdZrJIrnP8Nc4FyTrC5deyQ-cnqgtaL7f4LHireGo7yam_zE_WecbW2Jbw7QNEPG3BdVIVbXpclHnV4EZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارهای هفته هشتم رقابت‌‌های لیگ برتر بعدِ تعطیلی چندهفته‌ای‌وحوصله سربر این رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/31114" target="_blank">📅 23:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31112">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BI3iEXdHoRMVyURWz_6ZX2eS7Bwes4F3yLKfSoqS60GjOLWh423GDeqmQO81_0O-dgihuimcMU8rh9IlyoIpp6K8zHQ6pXlumH6UnfFcjMDwt88Jmko9-lIeiuiRekket-4Xu9xyi1TrjSMiPNZaN36CYVTRfP5nTeufzAbTdAkanJgjMAHd9dsee5sWEsPE_DOfsRv4jmjR0nmsnxlEEmXsRsbIFd1YF27FwekCUmlrAjDtlSkpxAbr0MbWW65YB78lPlzbxzE5lzQ5lDfG1RpSVgqeZAZpjMhxbevzkV8GwR4CTT9ges71rLnTioFZMre7ATCotVfsNdI_q50MrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HpD_Z63iQZ6zECQdTMdKtelcGC6rq4_UV1f2SjwNnsSSu1OymNVNlLQss1VZVvjqT9ZpCkxVczvJNOf1ywJGP3Mox4LVtkU4KuaSefblhrvyhQIxOa4Y8zvgKR0__uNgBc-5S5fTCB5jkk6XcslNv4LVnfXfxx2iLSVe_i2b3mWUZY8Le-Moysc9uaElCIlZ7WtcClKsGNUBsQLINb8rfAY_qNsaVPS1C5LxTYQZk6byYtPflzfomA5TEd7yl6fnN_yFnKAjaICIKBaB7jEg35Mh_2e1f5IL3PBrOMwY7EqS7B2-MSH4y8n0csQIvyg9s0VWZzgI-XB7-ij99zftTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
در آستانه چند ساعت تا آخرین بازی لیونل مسی برای تیم ملی آرژانتین؛ دانشگاه بوینس آیرس دکترای افتخاری خود را به مسی اعطا کرد که بالاترین نشان افتخاری این دانشگاه محسوب می‌شه! دکتر مسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/31112" target="_blank">📅 23:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31111">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R31Xu_z-pjw-P3bpO2nzEfWtoFf1t7szm3YegcNy5gAcGSxJO3TqyHeok2THbeHY3L5Q12RubQaNR0n2glQrUqeAtbfnzcRDrclS1wU-b1qIYbewyV7hzbU3SdxsSOGyRnqJ5juqLMrXpsk-vP5k-StlsOeH_vmkkgc08QBKTSexLB1kHGpetDDiyNThTQJ32LfCw2w96bTxFfv8HukDPjTVFmCGdXhjm9d3EOYbWRmYlwmdMLSebXlFR_RA0JKp2mE93IlkMeF2ItDhvZx8H0B8yc84O6IVAclwkhGYUq1aUdqIigXbhfziFSPxGM2xYB-tBF-vGMfymKnrfi-4pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد لامین یامال
🆚
مایکل اولیسه از ابتدای‌فصل2025/26 تا به امروز در تمام مسابقات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/31111" target="_blank">📅 22:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31110">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFoK6UF5TIpUYVFYEhEfurT1GCb089vDaRs5VhOIz2CYC-FZGZIWolqx5Mt1BOnzKF8e1e8p0OF_iMe0Q2vV8SwpuJHNcb1DUNIAd_htRbCjU9cU9RIURo-g8weuppYyllIKvifMsXqZP231nKt1a0erEt1mESLBzjZ99dlq2jC3bUMMtMy4pNo-jmoCkOpgUoBDdQpbK-rcY1AifcqzehfH1yA4n1_NE9cR7UV6zwD8LFd7GiQr9iwJlx5RBvcAIOP2T1I4BleEWC6FKWmQAHw6c229g8pcV4r2TSBPWS54dlN0-Lc7_bR9oxHwBAHUOZUIkEigPnm7-OzQ-Rv3Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#تکمیلی؛ کریس رونالدو: به هوادارانم قول میدم در آینده چند بازی مهم یا یک بازی خداحافظی با پیراهن تیم ملی فوتبال پرتغال انجام خواهم داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/31110" target="_blank">📅 22:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31109">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qe4aB3e-UPo-wmi6Ehn07UY8yO_82vIPJmRAS5OEMtf948fgDOTiUZzfrlWYPXAszqmoU95f49Qm-PEZhwZyTuLehR6tVc6oJ858s_R2W21LGIvvuPpORwmNcgOxniEZ7XInzf0QK9Q8mzJr_iIYzzcfkYIk12JN9ASeVSfUzDYYgOzP1F9lItHKoBYqfSV7o2sezzcOaqEgvabtTOZ7B9MmWV2fikBFmmjaiU2Sa_N2JinSw3tk7kMDK4AQLfusPlVUpb7On7SB5Ht7AlQjE77XTIFuo4n4FMowjtCZMlVV5l0Jajss8LTSCvQPbgfqZEXa3QjRS_PYbJJAX-fbHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
آب پاک کریس رونالدو روی دست فدراسیون فوتبال پرتغال و خورخه ژسوس: تا زمانی که این آقا سرمربی تیم ملی باشه هرگز به پرتغال برنمیگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/31109" target="_blank">📅 22:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31108">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gzm2gzU0CpNMaXz0HqVuKbsitAXKuGpzq7rGaubKW3nRtLEs3KQLfTAeicwfJ6MktdsYh1RUY-yyAGoVcnYfT7EUWhJafgutI-DzibTPhyEpXWUCSAR5fSWJx0q9Bo7cVNk-ixXuhYm_3jKArZ-1XGv8vK-ORJQ-CBmJm7_ZiSj55Ijto3pggvhHza2E6MDBCfFNJ1AQvFmAdRm_PwYLDm9aIWK6LAtUSC59f25gdOb9qNzMqD1Cf1zy07zxV5teSV5EXbPZFQfMMWEnExpxwxImcoWbEqWjU0f42Y58DlVTOpzM9JDmJHZqCQL4WTzztLR2hrWW3qKjCUwVPVVSxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
وضعیت پشم ریزون خیابون‌های آرژانتین رو ببینید که مردم‌دارن‌میرن‌سمت ورزشگاه برای تماشای بازی خدافظی لیونل مسی با پیراهن آلبی سلسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/31108" target="_blank">📅 21:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31107">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IxTyUmbpH0X1IIb8Od0aSjbbqtEqPRfcJr8AzswR468aEmRwcCdO7jAYtXZcvBbNYzCBTm-FaeCtCAmq6nNSCDIruKVfCGoaJ9-MGYEcidvt2eTlkpiovgXxhhcmUsjyhrKWa0xUEgY-02i6e7d4w9BfykufhrGBzyZwv3EpbniPynDD7lP5lKlZJhx6-m183SiEB1VJy3P4UuqrEXlB5RwqWwOabXdZcuZI0llOX80-zT4JQVzzzGDl0VKcPmFML6IXHajtYnOXbHCFFtlADvv3FwJha5et9sVGausVXNlqfm5haDtGS5CmKfTkW3u-ZLKu1hhl8j_hsgbu_X3dxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
وقتی بارسلونا رونالدینیو را به خدمت گرفت، این باشگاه چهارسال بدون‌قهرمانی در لالیگا، پنج سال بدون قهرمانی درکوپا دل‌ری، هفت‌سال بدون قهرمانی در سوپرکاپ اسپانیا و یازده‌ سال‌ هم بدون قهرمانی در رقابت‌های لیگ قهرمانان اروپا سپری کرد.
‼️
باورودستاره برزیلی همه چی تغییر کرد. جادوگر درسه فصل‌اول خود، دوقهرمانی لالیگا، دو سوپرکاپ اسپانیا و یک UCL را برای هواداران به ارمغان اورد. یکی‌از بزرگترین‌ بازیکنان تاریخ تیم بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/31107" target="_blank">📅 21:36 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31106">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85a77e7bd5.mp4?token=gXjM1zZ5ZXglGBR1ztoDOpCu83lXPA6sL14rpKFKfer_ig7P55KNDSiSZiKogFZfR9E_uzHroTlgTE7pKDu4TVAQ27sjd3pIJi7OPg_tmfArebMThL6OWaQstMKEs-UE0lWKscJna5hBOAXpihNxA1hQfsQ_LGEeqzj5idMS_n9DugYb2Zt4ex-uiS2-dZDjKRP-Y4UrCStlewS-6tD3MRMqwC3_bIliq5qI6mFbOUOl_oMACnME-cbWL-kPSPwwk-dMSWtIgz3fwGNPw3x9bpx0Ar4h_SfYhwldS1G6gcQVIH-bJp19ufjp0PKDQkxykOHenKnqL2pqPYE690cji1mohGQ03GmQ0S0ceIaLB_7b5NY7m1Rk1J7EJYIQhGYhFQ1l4iPe3ngL6iBy2NDgqWQGKxtXP8u5eAJcMf-yKBTufzPcljd5qZYapiT0ur42KRWOW3dbjilr1wK1zlXSjgzguQ2es6PVwksqSwDlON93yxoTxIaYomNDOJN8TvHjZw3dzZwAkPHd6rwcBRyoC5teSQZYgqzEqbvzxC5JnAIfrla9xEllJcPIBlKgDtr-gOENgjc4GVNMtpKUKZE0DUunRPk_RX9YZxJX4zX7yg_KHHwLTH-VVKm1_weqzn8RgyZZy_jVYStJee_CPoK2Pz6rDbNcjr_Di4LDqKZJ1Xc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85a77e7bd5.mp4?token=gXjM1zZ5ZXglGBR1ztoDOpCu83lXPA6sL14rpKFKfer_ig7P55KNDSiSZiKogFZfR9E_uzHroTlgTE7pKDu4TVAQ27sjd3pIJi7OPg_tmfArebMThL6OWaQstMKEs-UE0lWKscJna5hBOAXpihNxA1hQfsQ_LGEeqzj5idMS_n9DugYb2Zt4ex-uiS2-dZDjKRP-Y4UrCStlewS-6tD3MRMqwC3_bIliq5qI6mFbOUOl_oMACnME-cbWL-kPSPwwk-dMSWtIgz3fwGNPw3x9bpx0Ar4h_SfYhwldS1G6gcQVIH-bJp19ufjp0PKDQkxykOHenKnqL2pqPYE690cji1mohGQ03GmQ0S0ceIaLB_7b5NY7m1Rk1J7EJYIQhGYhFQ1l4iPe3ngL6iBy2NDgqWQGKxtXP8u5eAJcMf-yKBTufzPcljd5qZYapiT0ur42KRWOW3dbjilr1wK1zlXSjgzguQ2es6PVwksqSwDlON93yxoTxIaYomNDOJN8TvHjZw3dzZwAkPHd6rwcBRyoC5teSQZYgqzEqbvzxC5JnAIfrla9xEllJcPIBlKgDtr-gOENgjc4GVNMtpKUKZE0DUunRPk_RX9YZxJX4zX7yg_KHHwLTH-VVKm1_weqzn8RgyZZy_jVYStJee_CPoK2Pz6rDbNcjr_Di4LDqKZJ1Xc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رودریگو دی‌پائول ستاره‌آرژانتین: هر جور شده به مراسم خداحافظی مسی میرم و از دستش نمیدم. اگه زنم بگه یا من یا مسی!!! من مسی انتخاب میکنم و اگه بخواد بره خونه باباش‌هم مشکلی ندارم. من با مسی رفیقم و کلی خاطره باهم تو تیم ملی داریم.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/31106" target="_blank">📅 21:22 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31105">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mF3YJIPtQGvS0qyVOvplItJrUSlGcppoEBMEabergEE-lDXDLIwiox41WH1-rHZJcEjwFNdBa_6ZKf_zpAubfBpAZ2bwyMGTREIAmcaOTWTSszTXBsJwSLrvKMKuZpAH7WW2mZHGQVyOSvdE0aObs_Wc7tHJ0Vw3YugmJYyKNHo1t0Amm3_G_dRDJi0DBwMu9FyjPDC1t4bQXsCQWLdo43md-CV8cBxWKJQQl84yEhoUxrDcah8EWXw8NEMpZ0jheGopqomuoSk2yqqDwUY8uyX8Phpguzf9aBTTaj4CA4fHwHruol2bdhmKNMenkoUmbEt02gqaRWItmr-_Tlm0Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ مصدومیت حبیب فرعباسی دروازه‌بان تیم استقلال کامل برطرف شده و او هییچ مشکلی برای دیدار با تراکتور نخواهد داشت و با صلاحدید کادرفنی این تیم میتونه برای آبی‌پوشان‌پایتخت به میدان برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/31105" target="_blank">📅 21:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31104">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvRcegiio3G0FY9ctK7D0ibOEYLBf_HN40V7u_rhaA4tw3LPozOpuVy9U2rNR_QPQ1_JJYrn3KKrjIqVKI6J5gNl-_fOCeCwQfiZ0PvXlB2KqCFgf0RQVwzsvJMUc46VcsBwpazthoXLgigGfBdrmYrj0KaFtuIN1dn-2M_VK3h-5zsOXnlHN6eXNcHXTSBPIjYrEgdZj1GvZptZdnRimS-PC6vjlhGFwqtWwEPuMH6iAvUUUutiJq1Hg77yUCH47vDcBBy8n1TeQOlQa4FDOeGEw6hsqE8hx2sM_LuR91n1_Pd5lHPPZfr5Vo4zsymF1-V579UfQRuTLDxqPbSHUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
واکنش کریس رونالدو به صحبت‌های ژسوس که گفته از او عذر خواهی نمیکنم اما در فیفادی بعدی به تیم ملی پرتغالی دعوتش میکنم؛ رونالدو: حتما میام!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/31104" target="_blank">📅 20:24 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31103">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/elXU1nrTMxtIGULxemQsXhUX0Ug7MYSowxlSwp-n_TjfBAMfgHj9NvTYm87megcq6sxRt3aIOiXVHgB1uW6srsL9TgAgOg8j_Z5GMS8M0FGsD10nNPzXfE9H7dX9qnNNZemP5_wt56EB1B-8_yotZVME-T2iDJBijkzk6qn3TXsqr9NgUfPob1ki9wWK1I_s7B__XRmAR_Xuo-bkYMLSf9B6hLPKL7I6uISsV9UahSjTUuCNGP1ABmQ4Ph9sjjvB2XvB7BYnK5Pa54Zi9sKQhqxzlVZGpOCjzrcca00rZkm8ZH4qCqhWMxciI86D_lOkGyqovOgi5kJLufr30-VjNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کادر پزشکی باشگاه پرسپولیس؛ حسین کنعانی‌زادگان و دانیال ایری به دلیل مصدومیت دیدار روز جمعه مقابل صنعت نفت آبادان رو از دست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/31103" target="_blank">📅 20:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31102">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VaORK_pTdFobUtjgRliKw2QjsfqutW5Vzy1BaM00WYjroTtjQYJ_KJ8vkxIb74pon6s3RZeMTM11ad2imXZyZIP3SoPddvNjN8_v1uHisRl349Qt8pj_zO_-KDZuW_Yh9MzcGCHeG5qsviILnsFqpLGgzpiKBm3Ebmp73MclwxVlBXzLVLO_OqKsNBUr05m3vWPy6heHMeJ2JQaqxwuXFj14jD9iM9y7WvPAADsNBNTfi1_UcdfbjaadvbosNkNRs5KJAp-JsIYo0vp7z-MO284puZfcgPFFDeH4Lh01b7Yo5xQEW_TwMyn62rUD1-lml5x2qerDRxnbrArdSTNsjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جود بلینگهام ستاره تیم‌ملی انگلیس که این هفته یک گل و سه پاس‌گل به ثبت‌رساند و نمره فوق العاده 9.8 از سایت فوتموب گرفت به عنوان بهترین بازیکن هفته سوم لیگ ملت‌های اروپا 2027 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/31102" target="_blank">📅 20:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31100">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/th6YvDfMTuyyngXjUy7PkUqfjFEpBJCh-0USHYVRq8SXNNm_j8pBYBkq1-mO9l5VkEmShtYhxurEwn8xfac7AgHBu-Zp3wO8vgvEwK5w_vPTzf4P-IvikQYEXt3l0z8RWMyZeOct6sabhGzl62q3BHxUmvkxKpDje4ReqCvcg3iVTJw_VPrULzdYPiuVFlJQE94D8fexdsl15Qhn94U0EvNPqbUX16iYYdTTpR72jSDmZd6U0j0QvjGRzp0wtG1GIwIhlCdjDsDryIK3Trw-y_5Tp06Gq6zfnRVVOhUePjs28KBRkC-WouLnjMU1zvPo09BOurolvcjenM60tZnc3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون‌بریزه؛ یه‌خانم باتیمای‌بزرگ فوتبال ایران قرارداد میبسته و ازشون پول‌می‌گرفته و در ازاش با داورا سکس میکرده تانتیجه‌رو به نفعشون‌بگیره. بعد از دستگیری این خانم اعتراف کرده که با بیش از 40 داور سکس داشته و باعث صعود خیلی از تیما شده.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/31100" target="_blank">📅 19:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31099">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UI4zGsoY2SLvwoILYPaa4Hlz2J2xMv_F3rS4xW7ub-207p7J0TUGABq8WWv3S-el6GhFXc9CzqvrbVFPBsziN00eEmMt9h0_5KFn2UrCbp5ipGplM8cCuLRyb29MUHjZo5ss5tq_8UIi15xFTx-I3GvCBlGV3OP_2D9b05IvyzvHgDZSwBUrFvR3yzo3fz0E98YDZx54tcqrAkUWKhRQ8qg9NpdGxApayqDuVkKwBZ9BMad3uUJWd1t8zCMQR4YDU66jESdLQCERlXziOfPXSzl5mPOgyvPZUjurP-oJlRivGUiOSnf9n3s4JVD3g03nNSj3iWmzhyd3oQop-cy12g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
🤩
فدراسیون‌فوتبال آرژانتین قصد داشت که بعداز خدافظی لیونل مسی شماره 10 این‌تیم رو برای همیشه بایگانی کنه اماقوانین فیفا اجازه خالی موندن این شماره درمسابقات رسمی مثل جام جهانی یا کوپا آمریکا رو نمیده و باید حتما به یه بازیکن تعلق بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/31099" target="_blank">📅 19:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31098">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZuvqFMaUc1l7LEw2tBb423oQPIU5b0m-YJRGZaPrzze4OoAwpr6_VUfOSOAw2pi9UXZuTHb5DR1dvFqlogc9eRVyHD2Mdbvqw1cjBSMoFGdQhnN-aFHfIYeX_h_DyGB7-elLNfRTJ5ChPZrS8wOVBILH7H2QTFYBV26kOxQHQbm47j6EQNWxKUEvXETQdpCQPhMl2WaP0eHPLLqt5pMFcjHUXXQDZrMejx8L1wzPyx2KzjKlxR6fNKH9p0E4qpIDG4eN396bZ7r6uJFWExg57VIvnFzxT4i8IsgyrLXHceK_D_Ru5Mg32bjEvVk9wgAIeqzQ162ReDTxFnB7toSvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇪🇸
فابریزیو رومانو: دنی‌ کارواخال مدافع راست 33 ساله سابق‌تیم‌رئال‌مادریدآمادگی خود را برای عقد قرار داد باباشگاه آث میلان با کمترین دستمزد "سالانه یک‌میلیون دلار" اعلام کرده و درصورت‌موافقت روبن آموریم کارواخال به جمع روسونری خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/31098" target="_blank">📅 18:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31097">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXzXfiaoNgTzZMXkMYfgXbXIKbbg1OHMzUr5VPX9D-QacIcUA6EdjHN6hJjJdOPec7xbYE6CxUV-hpFl6rUmiRbkLuYvgGc_qTQAldhbl-zE81f_CB0n9A61V7sEnHMaCI7pq2GX4d7cbjPj1wUOoO0S6dZ8clIU2UnptbWlqkUcGW5IpSwmQ0DKzGQvc5byq38r8tKiRTN_unD4tcwF41syWsgzrDvcIEcNR6hJcjaQhRJiAEnzeUVGJIwnWX2hrVknLG9dmZW3gLSGSRIGDl7i72rY-yYamrcfmj3EXAIhd4crflYD8MXewQCg1bJxB5yNw1JL8j6if3eLDmuvjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
🤩
امشب فقط یک بازی دوستانه نیست؛ امشب قراره که برای آخرین بار لئو مسی با پیراهن آرژانتین وارد زمین بشه؛ پیراهنی که باهاش قهرمان جهان شد، اشک ریخت شکست خورد و در نهایت به بزرگ‌ترین‌آرزوی‌فوتبالیش رسید. بازیکنان بنین گفتن امشب فقط میخوام از حضور کنارمسی لذت…</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/31097" target="_blank">📅 18:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31096">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12aaf08506.mp4?token=vOneQme_AKYe8x5hooATSye9RHdnExMpv-YAbNtrFx-rwEofCA8oahkjy0yIa7ROotQv1FJvJsx0z-547c7N_BxIqyOSOmuBtSB7RboNIQZRUI7mPU4VqJKGARVx2_FEu4MUny5s168fOqk_HlNnBqJHLi2zv_UqWN7Oq23xgwtM1MEuLBs-bvGzSokODZLCHls5_8KNml_5tYV43XjIDkc8Ewtl-GEMTSCaqaE8mabK2qfXrVzqscZV6e2eqFZXOGi_nLUUx3U2L-kch2jjB4nUkc9dr9hlBcmITLcdDUEk5h_GXxwZEgiLJfcA-ezYL5ikMx4QGC3oWxarnX1z5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12aaf08506.mp4?token=vOneQme_AKYe8x5hooATSye9RHdnExMpv-YAbNtrFx-rwEofCA8oahkjy0yIa7ROotQv1FJvJsx0z-547c7N_BxIqyOSOmuBtSB7RboNIQZRUI7mPU4VqJKGARVx2_FEu4MUny5s168fOqk_HlNnBqJHLi2zv_UqWN7Oq23xgwtM1MEuLBs-bvGzSokODZLCHls5_8KNml_5tYV43XjIDkc8Ewtl-GEMTSCaqaE8mabK2qfXrVzqscZV6e2eqFZXOGi_nLUUx3U2L-kch2jjB4nUkc9dr9hlBcmITLcdDUEk5h_GXxwZEgiLJfcA-ezYL5ikMx4QGC3oWxarnX1z5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ شاهکار زین الدین زیدان در بازی دیشب؛ فرانسه درحالی یک هیج عقب بود زیدان در ابتدای نیمه دوم مسابقه 4 تعویض انجام داد همون بازیکنان کار رو برای فرانسه در آوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/31096" target="_blank">📅 18:27 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31095">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd044daffb.mp4?token=vop5mDmLVG40gPEva48sYMiUpBaDDUBKTDyZ8unseU28rZ7mvN7mFFhvBVg3krgsJskBCKANfZ9B-WW2ZkKaH6e-TWpoyvXAFg1LJ5hvfNIykhoktbLZu8rpUpVBOkDAestFTeoFJMgGpKU6gAjczFdp2M6UCx6LSZKf3VEh18joY_EZL8Cg64AEyOQ8bXnVRBQoFtTrOLv2Me-bwk3EnBGCV8ZXRBRuMLDty0fcO9uEEI3WdaEl-ospwazIaqQP9Eq80MhSos9z3rgO7ZpU37fx_h6M7r893MQ0LMbO4N1s3gEwfHwFyn0J5ziTySaMcvQTM9ERlxwyXhbb4Ty8fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd044daffb.mp4?token=vop5mDmLVG40gPEva48sYMiUpBaDDUBKTDyZ8unseU28rZ7mvN7mFFhvBVg3krgsJskBCKANfZ9B-WW2ZkKaH6e-TWpoyvXAFg1LJ5hvfNIykhoktbLZu8rpUpVBOkDAestFTeoFJMgGpKU6gAjczFdp2M6UCx6LSZKf3VEh18joY_EZL8Cg64AEyOQ8bXnVRBQoFtTrOLv2Me-bwk3EnBGCV8ZXRBRuMLDty0fcO9uEEI3WdaEl-ospwazIaqQP9Eq80MhSos9z3rgO7ZpU37fx_h6M7r893MQ0LMbO4N1s3gEwfHwFyn0J5ziTySaMcvQTM9ERlxwyXhbb4Ty8fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
لئو مسی از سال 2005 تا 2026؛ تیم ملی آرژانتین راس ساعت 02:30 بامداد فردا در دیداری دوستانه به مصاف‌تیم‌ملی بنین خواهد رفت. دیداری که آخرین‌بازی لیونل‌مسی باپیراهن تیم ملی آرژانتین خواهد بود و این فوق‌ستاره آرژانتینی در پایان بازی برای همیشه از دنیای مسابقات…</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/31095" target="_blank">📅 17:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31094">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hNfbouzYYnSXGhnP-RoobkDLESxwkAF2hMo96SwDvgnAjTU7Z4Bb5uIFw19uYcRGRlEYu5olXAv7cYKZavM2L1oM9y1oBwLXCwK9hhNV-H1drfmPMMbKZpqjIYZikA2QOFEf140EoYho6YOJJrM5Ht5D1u6Yejp0VtDpno8sH8Es-eblvwKMvYddUeT19Nj9L-NDzl74Bc7ByFgU5F7QFSPDExpdeLleorVyjRqpbUWibif-KDz9cUtjmIrDuu7URERws0qsdS5d16WKCGSs3mzt9QthE2Z2MmgkhA6akPNbi9ErQWYuJgewxBmFodxovCRgJvsEFEZtP4tdxAfl8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
ادعای نشریه فوت مرکاتو:
نیمار زمانیکه در الهلال بوده به سران این باشگاه گفته جزیره میخوام اونام درجابراش‌خریدن. درامدنیمار درالهلال به حدی بالا بوده که درامد سیزده روزش رو به خرید جزیره اختصاص داده‌. نیمار در تیم الهلال به ازای هر لمس توپ، حدود ۱.۱ میلیون یورو دریافت می‌کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/31094" target="_blank">📅 16:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31093">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e1a596a3d.mp4?token=jeDEva2SHwFP8IBSBnqT6Aqt0BAOhTygPhNzk76YCvc6QYxouTuBNY8mxKS9O-UfDorPt210L4jcYRHQo4avKGF3Cz5P8LX61fAiXz3VMoJkjr5bROvMzcJNNO8Y-ZiyELD5ViYG32l8GndmSCdeWxqIsBWi9734eiuguWWeLDmSIUWVejWrHfTPLLKaRnrR8mf-39Ndgz7ni_Qdt9jElhsS3MzDLLdin7ZEv6KuW3OcVgYwFiF2UjutG4k-_SMMejkceTvYrQ5jKmp1x24yviRQV3tyRbW0y6GE3pXPhsRCoefOahALLR60pSgL0-BIA6oIk74NhkK3TgTbmhbeQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e1a596a3d.mp4?token=jeDEva2SHwFP8IBSBnqT6Aqt0BAOhTygPhNzk76YCvc6QYxouTuBNY8mxKS9O-UfDorPt210L4jcYRHQo4avKGF3Cz5P8LX61fAiXz3VMoJkjr5bROvMzcJNNO8Y-ZiyELD5ViYG32l8GndmSCdeWxqIsBWi9734eiuguWWeLDmSIUWVejWrHfTPLLKaRnrR8mf-39Ndgz7ni_Qdt9jElhsS3MzDLLdin7ZEv6KuW3OcVgYwFiF2UjutG4k-_SMMejkceTvYrQ5jKmp1x24yviRQV3tyRbW0y6GE3pXPhsRCoefOahALLR60pSgL0-BIA6oIk74NhkK3TgTbmhbeQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیدواژه‌های تکراری امیر قلعه‌نویی در چهار سالی که سرمربی‌تیم‌ملی‌بود؛ همه‌ی همه مقصرند جز ژنرال!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/31093" target="_blank">📅 16:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31092">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fc_2GooEEnM2esQ8dD8kEIquxRuJR-rEkUhM3iBgmsBVJhV56v0tmMuUyJKRhKfjemBrJCT0r1MxR_ge4nvVjQV8uRTg1xPkBYH5HckCnKTtOaCUJY2gaXMoUcDtj80aXFh5UA0k3MGZeDr5r1qAjUbLDYA1K51XPvnYNK2PYSJtgBzWOltnEvbTi9Xp5k5I50MwfpLHLZW6fzfY_ojjvyVIIuSTL31P37Ad5RhBlwA3VG7YRZipQAOBYrA-lPTwXcbRIo6x8RGC6G0kk_npBPZj8zm-MNYRel4S7J5qDkb74KCQjQ-K74FOtn_RcycKX-4znLp-_rYNTFW-SIlAog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
تصاویری جدید از دوست دختر کیلیان‌ امباپه ستاره فرانسوی تیم رئال مادرید در فیلم جدیدش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/31092" target="_blank">📅 15:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31091">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVMrDHEqfXFz-cyP3VWHfcbjDYeUAl8pvDRiG3ulUFL4eZCv19-j-0R8g39_HWHyB0ozwaDAhB8dHjXz6GW2ydAxmqaycT359vymllXUyKQQWssZ3P25ynhrxR7iQV8P2bPNUInGmJf8EwBnJgSxj4yxydvK-oSdHoam9e9AY6IOOMhjyVRfasatJh3UyHQ91b3U_gCpFAAkxK7o4LUm79jkFldr6_ZVm0LsC6Zw-9jfchKOWB6dhyiqwcZ97_sa0xKMWOqNlQmhUr7kyik8Y0bJPLa3dUXNSAdkW4cVrsr8M7qH-LFsg1pINEueMBOl9-mTXlnN3V6C8IIS56L04g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یاسر آسانی و نامزدش بعداز چهار سال از همدیگه جدا شدن! یاسر گفته بخاطر استقلال میخوام برگردم ایران که نامزدش‌همچون‌همسر منیر الحدادی مخالف برگشتش بوده و آسانی سر همین ازش جدا شده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/31091" target="_blank">📅 15:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31090">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1967f5895.mp4?token=nYCVQu4YpwLBJbHGVbO_9CuaFZbxUoU9wS2_1_9cVYz1Y7fvHQM0u4fGy8noQ5aJLyadH_yfvyMms4k8IE502Td8DR6jj5FUHH7lvsyzq1JaDzlzQSNyIHnZYhu6ziSb6DRF5LsUc0SdcLLbQhjKNBF_xaG9V6eoJ8qE9OgV6wZOrQvpMHHQPYPwXdiS0L6SKdGvXzJIkuZaKhMCJMaeIZR2-gne0RnYGlv64zvQDxy-zEOvKRbCmUxRKNP6drDOxbTuo3B0KxamJcDzKqdzAeaU1UV_GeymvAo7UXI3s_y7ZdDAbsi24-l0QKcfPNn-e7XWkthW_bguhHD7v6RvmTmQD49OYA-iHn825FoHmswJkjbBW23nDIwrqzaieY2_Eg5KdF9k3L-RcwTuqcdg3n8TytDrC7mu2xKnG2k8eJmC6TL7mfwm85FNnQ3EVvjN2Zp3nuqyodW5Ge-9-O-WiIbVH_pjf5Sg5WOJdREzkvHcvUHDcrAFEqnTRnZ5O_TEIg5Y6v1ExWRQki6C5Z_oEDTQuqI0fMEhpNwXYLKJ-27TrXuM5auc4e5ca9g2D14x1sdiczqKWOJDZwFaLXMqyLV_gNJJcTBDjtUnZGv33yYAdlS5MDU0dRNkML6fXiOmDY4jrMHmmvyHsMG0iFbPjxpzUyUw-WwB7HBNZR5ZwAY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1967f5895.mp4?token=nYCVQu4YpwLBJbHGVbO_9CuaFZbxUoU9wS2_1_9cVYz1Y7fvHQM0u4fGy8noQ5aJLyadH_yfvyMms4k8IE502Td8DR6jj5FUHH7lvsyzq1JaDzlzQSNyIHnZYhu6ziSb6DRF5LsUc0SdcLLbQhjKNBF_xaG9V6eoJ8qE9OgV6wZOrQvpMHHQPYPwXdiS0L6SKdGvXzJIkuZaKhMCJMaeIZR2-gne0RnYGlv64zvQDxy-zEOvKRbCmUxRKNP6drDOxbTuo3B0KxamJcDzKqdzAeaU1UV_GeymvAo7UXI3s_y7ZdDAbsi24-l0QKcfPNn-e7XWkthW_bguhHD7v6RvmTmQD49OYA-iHn825FoHmswJkjbBW23nDIwrqzaieY2_Eg5KdF9k3L-RcwTuqcdg3n8TytDrC7mu2xKnG2k8eJmC6TL7mfwm85FNnQ3EVvjN2Zp3nuqyodW5Ge-9-O-WiIbVH_pjf5Sg5WOJdREzkvHcvUHDcrAFEqnTRnZ5O_TEIg5Y6v1ExWRQki6C5Z_oEDTQuqI0fMEhpNwXYLKJ-27TrXuM5auc4e5ca9g2D14x1sdiczqKWOJDZwFaLXMqyLV_gNJJcTBDjtUnZGv33yYAdlS5MDU0dRNkML6fXiOmDY4jrMHmmvyHsMG0iFbPjxpzUyUw-WwB7HBNZR5ZwAY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این هم از ویدیو کامل قسمت سوم برنامه فان و جذاب با ابوطالب حسینی؛ عالی بود از دست ندید.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/31090" target="_blank">📅 14:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31088">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ETN_TB3974TPZQYgMg-JRT36Bya1d-LyJzJKuYWgR26DsDWHB-grv264HdzlD1hlMIVqOOLSg_cRsM0zVnqiRQ_v8WUAUX1SDg8Gzrl4EyPUwydstt7FywkZevj5jAbYYfUna2AglCV43Uk7jDVBbIjLV5RL40SQ8LAlBAJrm6xyvVOnSfQtpMtGZr19ACLKYcvw5m_p4WiIb_D8wJWOiaNmhBhzelJqQf2nAThXCvhzovLSzSuv_mWWuYevonrqWxCu3ofOI1BL6h6ZSqRzH9SK8fbu3ffsRYlyhci6YuW4rNCtwgS30Y3lb-HxFkAfC6qwHX8DZQqm2gY58DGffQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Olvq8Y18ecSwZw5lXHu7HySeXV-UbfWvzN67SYgFcjFi7Aggul7trgjN7xl9Yx3ICdu4HoHo1fZTbdIOJBxC8tnSquF228n2_cEHg3Ij0BGLFlQHHyzG0DgdQld3SU9Bt8AAZA4NeVN_ZtuyRIJaC3Xau60Vrl58puQCJ9OFKGeXZoqHbGGFbNpppBPgQdCzTzIInF-hdybsfnWNwka-WKtybMLhV8_9DHSCXvLWtd_u-4DNxChJkbH56ShBt1J85dtqeye4CkC23797myhMZCu6jUgLIxZ2KyIrRytVgS6Qc_zHpESvTRHU3qF75XvBEpQpqkOv8FnARE5eT9nfMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
پنج فوق ستاره برتر قرن بیست و یکم از نگاه هوش مصنوعی در دو قاره اروپا و آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/31088" target="_blank">📅 14:24 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31087">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHTNytidR7tuJLN6EkJxSJdT1gb7gE6LsITFtXVM5qKEw168zl9E8csrEmB0KDENtfnkPN9R_43IfmbG4TBQJysW7kY7KtTvyHWbnW3q0zSuoqdLzIAVcNJv4YLRy24zOH3Wv0hgXlhUP0FRrulnSHoJZcYHsfRVXjn_ClIaEBT9anZBtSZUmFw7nBgRvJiD2I8S1S36Hznf5O0s2ca1Kbx4H7AqYtqeZ_S1qNEEViGhj5T9OFqt8z0kmYl1stEfhcrNBLwdoIgEbcaF1-VQuvf7BzeldMPkquwaFNLkPR21vMv13WLBXrl9k33pLTiRgiaXs65w5BktIfLK6_fw6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛
مصدومیت حبیب فرعباسی دروازه‌بان تیم استقلال کامل برطرف شده و او هییچ مشکلی برای دیدار با تراکتور نخواهد داشت و با صلاحدید کادرفنی این تیم میتونه برای آبی‌پوشان‌پایتخت به میدان برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/31087" target="_blank">📅 14:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31085">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XwBBFDjEOqzGP-_BNPTjqhz8n0WmlBl_K4NbN_20Ae6JN92Zg8YT8NHH6OrZ4GjgIvVV6P9T-0ZXJQZEAaGuR5ay07UH9FZbjyJ4d0ewTg2tzTf_FLIlo3yF1VxOgfBguwioxbgpaYnnXEclomRmNeK457CUwJ1OLgVb_wjhgzfGOylQwRVZsSJZmMGRt7VTZCPdWy9LWzkWCR2wXXXKXgFo7s0bE-G1oHr0Og43qLd0zXshaat2-sH7Y2TYYvWS7__xRVQnAWvrRH6tibO0XewqsudhFt6w8IagGlcQYYWpkymOzseTj6SvUZ0WZoP5xxuo2whA7Y5Id4vduM_ADw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BzJ-QttluAqKC6cPMT3DJzZdKMAsb4juEnHtP0pcTEH9vOp8w5HPX8EyBNwMMMc8MaBXawvf24jllW-oDuNSQ4y-OxClRyX4QZ2ETa6KghOp2lzgQc1WSEszEEaVA1LxyAJh_5l2e-czVZ3kGo8EA6jg8OCht_4vC4G_9P6nJhmM4eJW7rKM5boZEfidEHranfootTQtrsn7ez_EpIY3xq6-VKJbHgTUkmV87xurKVyHuUiM7NFuv3KmXH9jPK5JVLdu3RZ6SJ5AhV3kP8WVDSSWUJwY1Yd5EB6A9wzTJTlaFuGK3e4POa_5qFuF43uZewlNlWabzgEJCIcdwfRbJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
پنج فوق ستاره برتر قرن بیست و یکم از نگاه هوش مصنوعی در دو قاره اروپا و آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/31085" target="_blank">📅 13:37 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31084">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0GwGkBGfieaf_sty9yavjDwwlSspLMIKstbXzMRtkk8HHjX2-RebHkYSCkxVf8hjNOYEA0zP90b-G3-DyVdO-P46fUFTzxW4WFkVwQ2vc4FNuB-SXIVBGiYDIvjqnt5cPkmc-gWfOkat0Yjy4D1aWEFaTUGQTlih54iFeqtbW2nNb6YzcBP8ox22AWcrMIu5kvcVv1g15sRiFZzVCgv3gw4P5DYNrndmZDgxJ4B89WK9r_5mVH3DglcquFzeh5O0ir55ArBIobJoKx0ZxktVijR1RKv4WIvhjvkev7zUxvNRlKa-e0T50ByaM1Z3ZwU8-TFK656vIfDsZhR0SJZOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام وکیل امیر تتلو؛ دادسرای تهران حکم به آزادی امیر تتلو صادرکرد و او بزودی آزاد خواهد شد.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/31084" target="_blank">📅 13:22 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31083">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U431yOhP0k11oEoT6vubWhWxh5IznAL75OJVaN5oDxKEfGtOXmAAbyeV1nAidR6mhXsYkmjzupHUdKz8WyL3cutlCt3ybV3nhVRdRZ1h_rvUE1W5cqS_DIcBPr_e3SqM8h4SZXafHcJXiW7gKVx-iZxwx52-9VJmrs-0TIhNARgfx6uBaLKUr8F0sGtJcy8pyO4T6ZK4s520cxrOvr1yrwayZoV8AbvIapRI-2Utk8i8rE6tCan6YtYC8V2r0Y8TcHXvAP5EYo7ywE8MQcudgSt1or754imEJVrSRwVcBxLOdfcCeiqPe7w8cMs7hEFF8GOjAh9LBI6qnoe15OaI8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌امتیاز تیم‌لیگ‌دویی پادیاب خلخال روخرید و از این‌به‌بعد با نام پرسپولیس B در رقابت‌های لیگ دو کشور حاضر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/31083" target="_blank">📅 12:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31082">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wtz7ZUL6Udl6-25n79T0qVNnBJlRlcPJswa2rIl-3lWOEtqM-JvJpczuTOdJx4J_2efs-uHg1WGrvaISLBhpMioK0fexgPKrf2waWLHxgqIffQh0chIkB9vTcU9_PMs56lrbB7l5YsTY7O0n6-gtxR8040wHbAvOLg2e0E3jkuZ0P0WVkqoy-vbLD_f7lew2Y76wcf4ibipTZ-u8pT7oG6ienE4nS9qbWR7037hBHrrKOeLRnnTrd_98iAjTAmVVqI3PLuEk-9NGnSWvPAwd1CujgwWX24NSy6oF_e_Ia4l-ZjwjGQgqz-2RSi19QW4w81xaYoKl-8-DHvIhi_f3EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛ تمام‌خانواده لیونل‌مسی درمراسم خداحافظی او حضور خواهند داشت نه تنها همسر و فرزندانش‌بلکه‌برادران‌خواهر و مادر و اقوام‌ دیگرش نیز حضور خواهندداشت قراره‌این‌مراسم به یکی از بزرگترین خدافظی های تاریخ فوتبال تبدیل شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/31082" target="_blank">📅 12:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31081">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2ed844901.mp4?token=i-ywUIdigNyWPfoUqHp8UcUFV2w4dD6VUojRwUYlYQWF9gw-c61C-MZh0wKFNFLXAN7v8mdSDzPDqctiFuPY7Jge4i2srkVMgPXkcjXn0aMPpucBkGk0RCPumAyZZE_hs0gDceJInJ_prbATDB9n91nHAWkepPk7paBniFswh4tP-zN4NdSCVEBn1bOgPK7NCSTXOTjhO9-Rr8Quf5JWvkcNNb3MZtHqwQGxju03CICC-TnB5h-i8shWYszQVgkq8ZU4BwgPzP1Q97ElXVLnkcH4zOQ0KxyDQ5eadOeHfkUK5maitaP31u5B6kVz_SaSWh3W64ZM7MYOLix1Lut4iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2ed844901.mp4?token=i-ywUIdigNyWPfoUqHp8UcUFV2w4dD6VUojRwUYlYQWF9gw-c61C-MZh0wKFNFLXAN7v8mdSDzPDqctiFuPY7Jge4i2srkVMgPXkcjXn0aMPpucBkGk0RCPumAyZZE_hs0gDceJInJ_prbATDB9n91nHAWkepPk7paBniFswh4tP-zN4NdSCVEBn1bOgPK7NCSTXOTjhO9-Rr8Quf5JWvkcNNb3MZtHqwQGxju03CICC-TnB5h-i8shWYszQVgkq8ZU4BwgPzP1Q97ElXVLnkcH4zOQ0KxyDQ5eadOeHfkUK5maitaP31u5B6kVz_SaSWh3W64ZM7MYOLix1Lut4iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظاتی فوق رمانتیک و شبه هندی در شبکه سه؛ روبوسی های واعظ آشتیانی و علی خطیر در پخش زنده؛ قبلش داشتن هم دیگه رو پاره میکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/31081" target="_blank">📅 11:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31080">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETZdgPjlRL5jaSTxEeHiP5Q0o1Hn8RJA9k2hUQS4orgwAbJZPqQNbYCE4WPbHnw-bxxw59mwJ7uq8i5kzwdz8PXzCtbtxJ2ZIEKdUg3yecN8AcU7-bMfc4Jd0OnH3dBUDNLuon8ayyz16yOIt9yfcsaxMxtoVeBfImeNj7tvAuQ5GgDNolMpd0lzcEOWVPMygK7RaiUkYStmrJP4P_vIvALISuxNaEMQAKUaLRPpItMDRRJ43RcvZVdDSGuMzsQrpHctvVlv-9zXXd3RQg1gaR62fixOkojFXjhLyb9gsjngGeAIs4Zji2IvOUDRNMovIlxUf0IrcWtMJmv3jBwQjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ اهداف مهدی تارتار درصورت‌ماندن‌درپرسپولیس در نقل و انتقالات نیم‌فصل‌لیگ‌برتر:ابوالفضل‌رزاق‌پور مدافع چپ فولاد، محمد قربانی هافبک دفاعی الوحده، فرهان جعفری هافبک تهاجمی ملوان. جذب یک مهاجم جوان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/31080" target="_blank">📅 11:19 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31079">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95e2faae04.mp4?token=Ew4pakn9GdIEL62bjpukkpPhgdJnjxT2bB4JbDS7v41KSfbMcCSt-_IP1m7NMHto_FX56AzxvPG9DVqXkAq09otg0TyNzRxTX1neZQuUZzFWU1y-XxAADOqA69mSV_kqg-g4ytq3eYO3Edg-g_X-sEP5LEv8c1ZA9hpX-zFU-ZMBIOyb4IoZQQmC0VzHpcn76XoS3jx9rRHkLsu5fGb8UGiwBFCBtrFNUNezJAOEYTwvWM6jCqix5D9njW6y_7dI32PBP-BwYHpOqr_9HxH6sfAYwot6LrwczRAacjClYipd3TVKEAce2j5dDcub3I7L_Znr7TzyPVqOzGkQP2j_-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95e2faae04.mp4?token=Ew4pakn9GdIEL62bjpukkpPhgdJnjxT2bB4JbDS7v41KSfbMcCSt-_IP1m7NMHto_FX56AzxvPG9DVqXkAq09otg0TyNzRxTX1neZQuUZzFWU1y-XxAADOqA69mSV_kqg-g4ytq3eYO3Edg-g_X-sEP5LEv8c1ZA9hpX-zFU-ZMBIOyb4IoZQQmC0VzHpcn76XoS3jx9rRHkLsu5fGb8UGiwBFCBtrFNUNezJAOEYTwvWM6jCqix5D9njW6y_7dI32PBP-BwYHpOqr_9HxH6sfAYwot6LrwczRAacjClYipd3TVKEAce2j5dDcub3I7L_Znr7TzyPVqOzGkQP2j_-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
25 سال پیش در چنین روزی؛
دیوید بکهام با این کاشته‌ تماشایی در وقت‌های‌اضافی‌تیم‌ملی انگلیس رو با اون همه ستاره و اسکواد خفن به جام جهانی برد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/31079" target="_blank">📅 11:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31078">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_0LWArbncJ-wdvTjU133jqaYgGaXxnzdbbP29WYRXq8ERZBxIo5Mj_ANtiQm76Zb44Kg5G46cATXBw6RXXKRfhE1bDX9ue0mXtI86lLf4pjpSg1lkoax7aHy92rmLK7hYLa00kW5T2uZyoJis28WS9ERSNYMdvlmMeP-6nBKOzefS9Yjw0YgXipanlYq9dpKp3YarmUz8YROy4oLxx3-DDLERBG0SXapXWezb1Wr-rw9PgqGEKuSyiPe4TLD8hczxm13ja9SH1CUNU7v-K9d4NNLiDZCSatjWIXdlEer_o1wJDLjIrFBmeafTPnm-HyzIJAvGoajYzIbpESGei9hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسامی داوران هفته هشتم لیگ؛ وحید کاظمی داور مسابقه تراکتور
🆚
استقلال شد. احمد محمدی مسابقه پرسپولیس
🆚
صنعت نفت رو سوت میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/31078" target="_blank">📅 10:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31077">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb0144545d.mp4?token=Ti9yL5EkwGtT2JwLstADGUSdbaS0oKY2SPNzElVn1dku7EREC_BQ5BLWzBeGec7JYS2f2t2T4adiCRPQMMxT1Q3QM77h9NN1JL0oDcQatOxWD7Iycm9vBYyHBxSbBDHQc4hk6-zhl-UiKiRQeUXjifAzKd9hPLgGzAi0qibnSqfZdlenTJPbV1fLBzFGDjGyfeddpDsBh_fkYJOLyh2TcItKP25-WnHsX9Kzaw9ILKnhHDAYEzD5yeGkG2QocNAP1W2hZAO9gITvLeZnQiVAEVywCMFyxJp7cvL-opbvBo-4_U-mptOks9pVwCIF06ksUnTG_9XP-yZS7Yc24eRRYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb0144545d.mp4?token=Ti9yL5EkwGtT2JwLstADGUSdbaS0oKY2SPNzElVn1dku7EREC_BQ5BLWzBeGec7JYS2f2t2T4adiCRPQMMxT1Q3QM77h9NN1JL0oDcQatOxWD7Iycm9vBYyHBxSbBDHQc4hk6-zhl-UiKiRQeUXjifAzKd9hPLgGzAi0qibnSqfZdlenTJPbV1fLBzFGDjGyfeddpDsBh_fkYJOLyh2TcItKP25-WnHsX9Kzaw9ILKnhHDAYEzD5yeGkG2QocNAP1W2hZAO9gITvLeZnQiVAEVywCMFyxJp7cvL-opbvBo-4_U-mptOks9pVwCIF06ksUnTG_9XP-yZS7Yc24eRRYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک دقیقه از سوپر گل‌ های چیپ و تماشایی در مستطیل سبزروی هنرنمایی فوق ستاره‌های فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/31077" target="_blank">📅 10:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31075">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWkxRWIvzhncrolXWbzhK6BhEfqozeXXIhRmy1RQep5ZZXky_tXKtxdvvMq-0SG39tUNQ-CfpHGn9C22EvTddQcaH05zols9W8rQKaJK48DEkqJtzsRMLeYOqpRRUb_n2UYONrup6YV9VOFg4HADXFAn7qKNh31XvbYwXUVmHHoXKo9PSmAUjgtz8QhzRn-IXPwWF2dVx7AZdkIIOT-OpZr5HVfd-EO3YexOwLzsfRIoMPZtXsU8O9_DNJcqNW0k46gKYjGWtJ4jfCFjb9XTCiivcOlk79qacTllaZZoJpCtd9Dh6a0p1x05_Lw5BOONxcZDu-1ZZUTWpJG5UiuwTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
خبر خوش برای هواداران بارسلونا؛ با اعلام دکو مدیرورزشی‌آبی‌اناری‌ها؛ این‌باشگاه با رافینیا دیاز فوق‌ستاره‌برزیلی‌خود برای تمدید قراردادش به مدت چهار سال دیگه به توافق کامل و نهایی رسیده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/31075" target="_blank">📅 10:21 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31074">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-u67XjdJgVyCWxco0Lcb7azP0aEOWTfnNPorZr5shlC83QC9IGZiIBxYuK5zbaBcJstsbxFpUtLUjRUAwPTRn5c4yMgDnASZ6dGV-W-kRzqC0rgyr2fmfdoI9zOXbmfasKhrCbBNYVXdz4270FenL-JvwY46pvV51ZzuWem1lWwJJkG78OfwAGUiVoDqFeDoWc7ErPbYFK5ZdghG6Pzy4y-0hDhWfoV7IqXLczTy_ev1GqCIgXe5TdupEbxsiHJj2t3yNPlDCSfXjHlVRkf76fJgdZ2FuKtxwb4j5tqCrfqUjTWtZUYJD_iNJJUw89s9y782b5AJZRCdOhBefxGMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسامی داوران هفته هشتم لیگ؛
وحید کاظمی داور مسابقه تراکتور
🆚
استقلال شد. احمد محمدی مسابقه پرسپولیس
🆚
صنعت نفت رو سوت میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/31074" target="_blank">📅 10:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31072">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PUK41VBAcQdKAH7mEyBDtrrWAfedNxg_N6HV2DQ5_pdewCRk_D2E3j1malyK2LcjiPU3dolXcepzGmBjUBSfIFiR21X4wyIDiBHcf6nLgRA679YhFF0pFb98UUJT9T8zYsgAvy8nR-r8I8fKa-TXH3uAdpqiYvl30YjnGCwtIOEuEvLOn7qfOZapVx5behI4dkVjxXbFGKTEC5jZtW4ub24ZL4GcZkgeg1ckG_oDd6xWQcp0EwsKI6QxvzUHD5H6WNWYXr4GFT7b2I0LR0B8BTyvOTCf_cMZWoY5tYXkfEd7GNQCXqLfazoJ1-Hs8DpiGC7ATES1K9D6SeibSP2pIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kk_01iUvos_CLI3CXEWyVRnZU2J3FssGNUdMoXkdHn4LUmx71JC9mGqLs-Pg_IBrjNqeMofjgmS6wXm6S5Ctm6LRR2pXQlnJmMBKaKb85v50K42WNjjbAEbNHc0gZQOC2Vtav9xJOUZgvhWg_S6edfiObqYXa8Ri-IVPOVRdy0wMF0syXohmsrNe8lelmfDbx1j042jSmlLLf9GXuWIZeYQJNutM_qS_0oi3GBAZrXO9isTNxlK7ovR-FBT5F7iolvxVi8IG_afitoo9WK_zt8afvUtqOenyPqHQ4VCTluPJVUTsO4ggdxZKGoQoE2LJFncSXLe1NCvhM6bHN74PWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
👤
سنگ تموم پپ گواردیولا برای لیونل مسی: تنهاجایی که ۶ اکتبرخواهم‌بود آرژانتینه تا در مراسم خداحافظی مسی شرکت کنم. من به مسی مدیونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/31072" target="_blank">📅 10:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31071">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10ac8f2e13.mp4?token=Os2T7YmeFSCjylz73Se7iwIEb6SbILCWLj6AHT9GJyNUdjxeZqONPS0Ua67j4jNWq1A9-PnECW7gHhSrRzzjCFnNY22UMBqzsn6Qz63NtuXaRSmLOk2I6DR4xtKysJ9k9KaZkpLh5nqQhexKVYen2uccLImQP2lZHgb8Dc8j7Vmd26o32nE_wuNf0oDCFPcl5pgQex9wRLttoHklOi7ntWZiq8jCb__xmqpxhkW2l5lomBJbRbz5xxyFvGlbrpUmsTL1YqgVIR6RAAPiZ8fIXld2l_qPN3HA1MmAbMPW7dmhLPDWOhHA23wIwpjKCp63Sc26Ud3oLIFXJ3wkqP9dyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10ac8f2e13.mp4?token=Os2T7YmeFSCjylz73Se7iwIEb6SbILCWLj6AHT9GJyNUdjxeZqONPS0Ua67j4jNWq1A9-PnECW7gHhSrRzzjCFnNY22UMBqzsn6Qz63NtuXaRSmLOk2I6DR4xtKysJ9k9KaZkpLh5nqQhexKVYen2uccLImQP2lZHgb8Dc8j7Vmd26o32nE_wuNf0oDCFPcl5pgQex9wRLttoHklOi7ntWZiq8jCb__xmqpxhkW2l5lomBJbRbz5xxyFvGlbrpUmsTL1YqgVIR6RAAPiZ8fIXld2l_qPN3HA1MmAbMPW7dmhLPDWOhHA23wIwpjKCp63Sc26Ud3oLIFXJ3wkqP9dyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه‌ های‌ سنگین‌ و جنجالی ابوطالب‌ حسینی‌ به هادی چوپان
؛ هانی رامبد دیگه‌بهت برنامه تمرین نمیده؟ ایرادی نداره بیا خودم بهت برنامه بدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/31071" target="_blank">📅 09:49 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31069">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s12aZSHweVdaCqv2CuIea04R8mZ4kA_IhzuoazXmt_03621PeYMEZhYMS2jNuh3AUE3NfrsXhQhYx5OG0TCBLm7oUYr1e4ceuyj3MaA2MhOPZHGfXBRyLsEH8fYUIlHFsbpqVt6dHpFkwrxSEE3i9CwpBDiAh4ypphCF5tXtghg8F6VGJ8FkxORvKETPsZ0M094dbFT2zXGd4ikJms5ff1jLB_4Hn_J8p9hQl3bkn7T5NbVbDomK2U3qTwdebO-UKCjTFEQSm_0SabU0fRYQGGZRcFSiRnCG_ns93RQYTKq3xNFRsixggsuyMkUHr1uQSOHQf6sE5km8gCsQwK5Emw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
جالبه‌بدونیدکه؛ سال 2013 تیم رئال مادرید میخواست تونی کروس رو از بایرن مونیخ بگیره که مخالفت شد اما سال بعدش این انتقال انجام شد.
‼️
سال 2020 کهکشانی‌ ها باز هم خواستن داوید آلابا رو از باواریایی‌هابگیرند که‌مخالفت شد اما سال بعدش قطعی شد. سال2026سران…</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/31069" target="_blank">📅 09:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31068">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAeoHuErdTzTdG7OOd-dYMNqufrBDM2LFUJNrgGkN5CIsbIpaBMbi13ITX-aE_rz3gudmfPORxU5nutD3qvhAJnn_eGMKncndQN5nNVjba_ttQ6f5SsKbwKw-MAyM2-Gd6K10sSluZO6x1_Q7UF8udWVigf92rqe41_b5r9xNqn-FzTCKHnTeU-dnpIYTN7PpOoVJBdJx4pehRET6MuIViZA1IHcwUgJyXga-iKiB8mf4vhvLe52bgXNgjiSTUVKUgFgR1U6nJ6alcQunojaNfFU481EjXt4AosdhCYQxX6lSMmWgHNZv1zWb26UYewnupAkiMCQjfef21VOpuTGCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛نشریه‌بیلد: باشگاه بایرن مونیخ امادگی خود را برای‌ تمدیدقرارداد مایکل اولیسه همراه با بند فسخ200میلیون‌یورویی‌اعلام کرده. سران باواریایی‌ ها حاضر نیستند با رقم زیر 200 میلیون یورو فوق ستاره فرانسوی خود را بفروشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/31068" target="_blank">📅 09:19 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31066">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZS2yw0E_9VTd4w1ieG_LLVB5yWZsZBTm_IreMJUyClh_DVkDgfN6TPIyUm8EOJPkApyvPXSt_hUFcj3ayHWIzgzy6e0HWVit2DUdi0Omoey9knTKgKZIO5gkeauP_tZNNmDmoezUMMXFrdvT90ljUGeKAhoFdfpmyVKRlcBhrcAULNrR0jES9Cdh-LslTbAdzYLMxOVts0hD3JWZYiRF_QNwgEy1v5843p0UX0_O86UeICVapYY_jC15I_73brIVgoEvtS-Sg53lOx0uV2FwtWZe2oa_cPVfNukdnZdTEs_d4ksZ8Y6mou22oIn5swiYhLULk-dkOzpjT8r97TY6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84daabae54.mp4?token=aiopCfCRYCfUDtPiSaW-Fxsqu9G-0vYcVqHCjQAd_6V0Qz1OVdjCURqZIZ2HCYx1ylp-ckjwzTjcFYOP3PHqGas9xNLtgmmnl_DHwcZfgTf31UKYskjBtrepvciaqm6cdo0baHWxys6TEyPP-qhdfHMh-48kzPoYbySWX1Lxj8zs6QC93hv960DCsJvXMNUBLJWID7OVwtwpWQ2qoVsSBrYmb7Y5IFiYfZrS4jNx1ixQ-ASvXbOoMwzno1mrcfNXezK1hTIch4QTN4N9LfmIMKUVfx1znAI1u-kDUzLqLMdY35g15PBn_vLj3O4mZucsvNelXllg5CTUWDIInPinHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84daabae54.mp4?token=aiopCfCRYCfUDtPiSaW-Fxsqu9G-0vYcVqHCjQAd_6V0Qz1OVdjCURqZIZ2HCYx1ylp-ckjwzTjcFYOP3PHqGas9xNLtgmmnl_DHwcZfgTf31UKYskjBtrepvciaqm6cdo0baHWxys6TEyPP-qhdfHMh-48kzPoYbySWX1Lxj8zs6QC93hv960DCsJvXMNUBLJWID7OVwtwpWQ2qoVsSBrYmb7Y5IFiYfZrS4jNx1ixQ-ASvXbOoMwzno1mrcfNXezK1hTIch4QTN4N9LfmIMKUVfx1znAI1u-kDUzLqLMdY35g15PBn_vLj3O4mZucsvNelXllg5CTUWDIInPinHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇺
گل‌های دیدار امشب دوتیم فرانسه
🆚
بلژیک و دیدار ایتالیا
🆚
ترکیه در لیگ ملت‌های اروپا
👤
شروع‌فوق‌العاده زین الدین زیدان با فرانسه: چهار مسابقه، سه پیروزی، 1 مساوی، 0 باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/31066" target="_blank">📅 09:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31064">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBBgnItgzkYy7Tenp3peocD0XP5NWSjUDdHQL6p4HRR5vUBN4VMI3rv3r2EWVWj0LhNpbwN3_RSXcUrAdlDH_T242tV_sEzMlGKWN5fhB4vWCIdidgMkkGnX3Fj6-D2KFIlBDs7T0PnAc8QZh8zK0OXQ4dE5YxgqQtRpGunwiF9FPRnuBdcyG-VvXR1BW8R0LJcD-92Yj150gsGfcfLGwR2CYmKhRkqUTKCnMq0uDtxze8mwIzSDA39IlC7hRrcqiFjAP9yMBZiOqA0bB8U5dIj6KwMWjzwBLxNnpyRxQ5gwvqCgwXxN3B6oQsc0ZBVbtyQfL4D6f5QS-A0TB1TCmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌‌ دیروز؛
برد چهارگله خروس‌ها مقابل بلژیک و دومین برد ایتالیایی‌ها با مانچینی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/31064" target="_blank">📅 08:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31063">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVNLCa1AXuINZSkxcqCTJYiX9027hEnDmbPbHAkBCVB275uCVUgdeELtX-J15Y619Fq_kgsLb_VnSxJTeVVgUBUj2Ho50AcDXnWvhU9UrZFMuahxixwjhz-LcOeK5dd1FY1snZONVjCNX61XiBTgybvtQ6byHEtelzhujSoy5edpEQuEsevlreNc-31hVmufgdzDzXVoLJIi3QN7xHOQFsYbEtqAMz6ClMHyvtOpm8zS5FjR7ZInTm_3zxtZwdI29SK4c1ay08VENRBWCy2AYQJID_LIJ6H5QSsq5ZdxDvdSEdPI-6TMgq2B3EukC8-qHXhLUtOrmxrbECmZ0JSQbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدار ها‌ی‌‌‌‌‌‌‌‌ امروز
؛ جدال خانگی کروات‌ها با اسپانیای دلافوئنته پس از تحقیر مقابل انگلیس
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/31063" target="_blank">📅 08:02 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31062">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e146e3bea.mp4?token=WjJfR9AIYioOB2oqb1OS790hYmojkik611kNHeYrhknIVAxyLxzFBeFRlMPhrqx1VOQIaTYL98WpSGXj9jZOWWci2KwRA1XbTISEd8Bn3gTb2pol6UqNG0naYGh8W6FL8MP35cuv9szVdq1COmWWyqsj6Nb6au1OvHvkqtoR9jq4vWr8HEIthqTTACIUfoOv0XKFzhrxZJEjJ9WyL3I7fskrGmFEjFfndpwftclJBf2RuqXJvtmQ1Beu--ra8BCPq8ZzOnsCaTkS4ytvluaqR12obsGvVbIaA9khlfVCGKLaOAq3HEErpc6paFbv-FjvoHQpxHLzu0iE7M_pj57CcoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e146e3bea.mp4?token=WjJfR9AIYioOB2oqb1OS790hYmojkik611kNHeYrhknIVAxyLxzFBeFRlMPhrqx1VOQIaTYL98WpSGXj9jZOWWci2KwRA1XbTISEd8Bn3gTb2pol6UqNG0naYGh8W6FL8MP35cuv9szVdq1COmWWyqsj6Nb6au1OvHvkqtoR9jq4vWr8HEIthqTTACIUfoOv0XKFzhrxZJEjJ9WyL3I7fskrGmFEjFfndpwftclJBf2RuqXJvtmQ1Beu--ra8BCPq8ZzOnsCaTkS4ytvluaqR12obsGvVbIaA9khlfVCGKLaOAq3HEErpc6paFbv-FjvoHQpxHLzu0iE7M_pj57CcoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
باشگاه‌استقلال‌خطاب‌به‌فدراسیون‌فوتبال: شما جام قهرمانی فصل‌گذشته لیگ‌برتر رو به ما بدهید ما خودمون نمادین اون روتقدیم شهدای میناب میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/31062" target="_blank">📅 02:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31061">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/612b743bd9.mp4?token=D4MuY8Qhsw19Hn9DzGEuk2ccX2vrapdQlMen6Hf8pn55w01LBhsk7rTUiNXoNpbVedqi1Zi98YciIBlT_Lnn7AiSzJO5aDww0trncM3qn-Cut8Hfz-oNe3mPSXQFm2CnW1nRTc5RN_XgqCfe1JRHxyIjOd1t8G_eyAqYnr0N55ER3qHt04PpQ_TRifEX6w2mgd5RRed9oETW864ZAG4358Sp_gX0cqQ0e3yFFVUWM7T4dilwFRpbIGbo68f0FUDqiGrNcxZX_7aEZ4cTEi5REhYvQc5IPMBJ1axUe8eMCxWF_RTpGkDOw0-eFiua4XZzwtSgdCi-VEIrZfR7w8bhkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/612b743bd9.mp4?token=D4MuY8Qhsw19Hn9DzGEuk2ccX2vrapdQlMen6Hf8pn55w01LBhsk7rTUiNXoNpbVedqi1Zi98YciIBlT_Lnn7AiSzJO5aDww0trncM3qn-Cut8Hfz-oNe3mPSXQFm2CnW1nRTc5RN_XgqCfe1JRHxyIjOd1t8G_eyAqYnr0N55ER3qHt04PpQ_TRifEX6w2mgd5RRed9oETW864ZAG4358Sp_gX0cqQ0e3yFFVUWM7T4dilwFRpbIGbo68f0FUDqiGrNcxZX_7aEZ4cTEi5REhYvQc5IPMBJ1axUe8eMCxWF_RTpGkDOw0-eFiua4XZzwtSgdCi-VEIrZfR7w8bhkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیو کامل برنامه امشب عادل فردوسی پور با برسی اتفاقات اخیر فوتبال ایران برای دوستانی که علاقمند هستند برنامه رو کامل تماشا کنند.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/31061" target="_blank">📅 02:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31059">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMI_syr8pIkzP3DnKIlL7L-A3p4He1H0q-UnDPCqXssQmxfmD6j9XJ6djR9mDkial2y1neFcq-UqIr6wqJjUNjfAcWrYP89n5CnFk_dk5Ax8yWg7uGnLA_DUYpPL2-R8zyg6u3WsYAXk1j3tbctMrcJ1et2hxfZPs2pDe0BC1XNqvZ7tvXs3PSpDFSa7voSiyWKMKi7ad5iIz2Zl7_VU-vQEcwAA51q3RxwIW6QDJ_lOkozpFxgxDM24z6xYI6p308A_ySLdv1iN9p6UR3sdtm1v8sNbjhiIRpDEtRuDkgHAHSRosOZZT5byIqkIZxdZ5OlQjtILNNJsqxTkme_KiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
روماریو:
امروزه مد شده به فوتبالیست‌ها میگن بهتره شبِ قبل بازی رابطه جنسی نداشته باشید ولی من باهاش‌موافق‌نیستم. من‌شب قبل بازی با همسرم میخوابیدم، صبح هم که بیدار میشدم دوباره باهاش میخوابیدم، آدم باید تو زمین احساس سبکی کنه. به بازیکنان توصیه میکنم این حرکت رو بزنند معجزهه میکنه. دو راند نیم ساعته قبل هر بازی توصیه منه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/31059" target="_blank">📅 01:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31058">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1edc763594.mp4?token=m0O7m6HywTbWDzK2aQYkVrFcqCuQviYYjcN6IlKyIwRGYmXKheper3-I8-1FYX8fHEj7khhNVlgWovcIloGq_eY6XlFaoWT5WuDPmTXX3uF6jjUIFtntOVTkPG0G3ZBRHnURHDeMnQzeOblILLKNCnryyQO39OEA0W--Il9ntHJNROvRx2QUPrHLhtBj-wRA_zMHV9FrJsPelJ-4J3jNO8tCo_I43ad0RNdQVzTFmeLXrI5T-ljT02vNIXGulVgjlkQm-AJ3l86nCWfyX3T6ZjXIUzQWppT6uDpzl3aCfpX9OSkL5PRyA-Z-OKtOPZBIgvuUIryinm8Jo1fhGtVxKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1edc763594.mp4?token=m0O7m6HywTbWDzK2aQYkVrFcqCuQviYYjcN6IlKyIwRGYmXKheper3-I8-1FYX8fHEj7khhNVlgWovcIloGq_eY6XlFaoWT5WuDPmTXX3uF6jjUIFtntOVTkPG0G3ZBRHnURHDeMnQzeOblILLKNCnryyQO39OEA0W--Il9ntHJNROvRx2QUPrHLhtBj-wRA_zMHV9FrJsPelJ-4J3jNO8tCo_I43ad0RNdQVzTFmeLXrI5T-ljT02vNIXGulVgjlkQm-AJ3l86nCWfyX3T6ZjXIUzQWppT6uDpzl3aCfpX9OSkL5PRyA-Z-OKtOPZBIgvuUIryinm8Jo1fhGtVxKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ تیکه های سنگین عادل فردوسی پور به مجریان صداوسیما: توکه‌حامی قلعه نویی بودی. رنگ عوض نکن. حق انتقاد ازش رو نداری دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/31058" target="_blank">📅 00:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31056">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇪🇺
درهفته‌چهارم لیگ ملت‌های اروپا؛ شاگردان زین الدین زیدان باطعم‌کامبک‌مقابل‌بلژیک آتش بازی به پا کردند. ایتالیا هم بادرخشش کالافیوری ترکیه رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/31056" target="_blank">📅 00:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31055">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N52cqGwHfhrObFq4JZiyx0fWVDerMeNwDk1k0Qvb_XuoACWL31C2slyb91U-ym0hOE7MWJhhXYWby5vgBDp1ceBS5u9wWFVU3fLs3QUa8jfFmS8IMl8K6r_N6h2HJ42IFINfOB8w0rwHqXSJQ8dxrlnyEs9o9m6qazW2lmNaE_zuAFRVryAHtXpqUekyxVTAhwF1_MHrJZPqS4ax4RrmpcBc2WqddTi8-VrNmz_3TrFXKIyomeAIUL3RBRANVPGMnrpO3Qsr9b2G63EaXJpmfwVGgDzuz0qRmS9zq0lQh34K795D1PumQhjHC8vR8G4I7a3S3yjRCizpM2ekM6s3Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدار ها‌ی‌‌‌‌‌‌‌‌ امروز؛ مصاف خانگی شاگردان زیدان بابلژیکی‌ها و نبرد آتزوری برابر سرخ‌های ترکیه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/31055" target="_blank">📅 00:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31054">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZg5FN4ZsbpEpEy4nB9aIYDDOgakCPTeI1UhTy3gE_eZinGFxAw3dcqV4cLhmP2e9VYXZCI5Md3UkhXxtiUsoDnt3MNbxTu-P9dHBd-FGDeRvcxGrorRH0PlcZ7pgEQR2K8b3gRVjvdazIK-eBkOkJLIviOIHEPABrYumPR9BjfbvwPTA4795_wGtegiD3fxU8p6KA0W2AljHFURyyI2v-JEsujAxTuQIPJnCrWIMPiyhvlEVbYlewNAINhTQRUy06chIAzTFfOXJWIMWAi-OmnC8XLlr2KFqWUfAPwQhqX8AQKGHhikfxmOhbuUovdcG0yjEBmH2n39RijVKOLo1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
از کیت عظیم و ۳۰ متری آرژانتین با عبارت «متشکرم ۱۰» در پشت آن به افتخار مسی در میدان شهرزادگاه لئو یعنی‌روساریو قبل‌از آخرین بازی ملی وی رونمایی شد. امشب مسی خدافظی میکنه.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/31054" target="_blank">📅 00:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31053">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9410553bb0.mp4?token=kZV4Bf1xQyqQhi4gD6kHAFdbsQG-GK6V-U1-2N6JV51dyoNKf1F2vqSeIOEU4SBMh7_QRKLI5wuL0BKH5H11k--VnLqqta9LxgtSINH6lxdOIxCiWeYVjUbeyo7L1Bp-i4AgFuNWF4v10SyYcJ9CtOIW8cpvV_P8RKRTojZ0N1Vnxga-hR5YQ2PzpvvOt712SSmhaYB1B2AUxKuRJApIMilZl_yMs-vLjAFfqaJSHAxSXzrQEvbil0vD4c5AvpuA_oQ5DmIgZHeJ9SQE36FqOJnRRyhTC9X1cmjFFmTMb0IzwXEOPtD18qaINpuDw3RvNzKdbZbDqRvEeMs2QLrzbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9410553bb0.mp4?token=kZV4Bf1xQyqQhi4gD6kHAFdbsQG-GK6V-U1-2N6JV51dyoNKf1F2vqSeIOEU4SBMh7_QRKLI5wuL0BKH5H11k--VnLqqta9LxgtSINH6lxdOIxCiWeYVjUbeyo7L1Bp-i4AgFuNWF4v10SyYcJ9CtOIW8cpvV_P8RKRTojZ0N1Vnxga-hR5YQ2PzpvvOt712SSmhaYB1B2AUxKuRJApIMilZl_yMs-vLjAFfqaJSHAxSXzrQEvbil0vD4c5AvpuA_oQ5DmIgZHeJ9SQE36FqOJnRRyhTC9X1cmjFFmTMb0IzwXEOPtD18qaINpuDw3RvNzKdbZbDqRvEeMs2QLrzbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ ادامه تیکه‌های سنگین امیر مهدی ژوله به فدراسیون‌فوتبال و کادرفنی تیم‌ملی درباره حاضر نشدن گینه بیسائو برای دیدار دوستانه با تیم ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/31053" target="_blank">📅 00:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31052">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wb8KKI0jEFw17JPMLkcFun5JRAIB8wKiqDNPdflodQ_GEvtacl7Lq5-ytko_aEeg9vhlLbJsrZn-WGlM81-dwe_K4AVXCFPok9u41PCY5Te9AqDgD9qtoyCapOOU9OM6B-hLAHSR_Erm8W38erGdtYEHTh-OBUoIG08xLqOzZW1hNA4idOyW6Dic7OZtY373Zxezldzea8P3XRXda9En4jSMLQepICmwZ4X_WKDePvKucNXuTp6ys7ZGeULDnVWDQiLiaerDRE65aCyYNh8dvhyqiBK9ncK1oxU1Pd6-_scA27nvw3h0muGWt1RmPsk9-3jnBJ_SwZylXY_nE689jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خورخه ژسوس سرمربی‌تیم‌ملی‌پرتغال گفته چرا باید از کریس رونالدو عذر خواهی کنم؟ نه نیازی به عذر خواهی از او نیست!!! پس بشین تا برگرده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/31052" target="_blank">📅 23:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31051">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aC737gPbqCIJGkgDjAjLlY7ac0EBmTkgxcxqm_2FnzRTr__wR4hDInNJu7RzS-qnDUAdRfqHlM0JZiqhoZ2_PS99xzpB_zo5RlMCxycg3ZdWw_61Kxoi0vQ_2WeWpZFE6nGY9N7o-rmllIGlysciSY3AmNtRhtCblIuxDj7FHwtMsyvP3oDDIH13st64Yi6NEGoIYKKLhMBCWeLmsLrr3VIcFGvmUCEx7hWDuQpnrMfNehSeUoLYSpPlxkVuVmxG2ET-9NSONuxnDxfbhsZnUbb5qrdn26gfPHrmQd9pkoOjSOo00xE6_GUWisv-J5w448SinnapkN7pNDcfwPlWCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رقم رضایت‌نامه‌سه‌فوق‌‌ستاره‌ایرانی ماخاچ قلعه، الوحده امارات‌والنصرامارات: مهدی‌قایدی: 2 الی 2.5 میلیون‌دلار،محمدجوادحسین‌نژاد: 1 الی 1.5 میلیون دلار و محمد قربانی؛ 1.2 الی 1.8 میلیون دلار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/31051" target="_blank">📅 23:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31050">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bbe125227.mp4?token=BjpV859QoMmqzMDTRGjqt9tu1QjD-BLUx_Bz4IQ1le_0M4MCM4CT2hRK7160NON2ssGJq94C6u0dnOTfWQcmSaacIzcKQbmnTsmpl3IjiPyGJC1dEjcmu214nPMK82XWbjt1oQh7tEsucbvNLxIWyATFHfj7LU9P7DR2oQO4yMxaN2u5mzlj8S3yBD7oFjrgilGNT1EA8FW9wKpWgb6MRGa6aTq19EGFgUsyBCHXeLfz4vppDTpst-XAC42MeU5DSJZpG-21zTSuD6nqb5js3N2vehMUbj2zCZf3huYZkSw3O42Qd1dT74H6DJR_MkFchmUbkph0s0_AOL5mR0vxLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bbe125227.mp4?token=BjpV859QoMmqzMDTRGjqt9tu1QjD-BLUx_Bz4IQ1le_0M4MCM4CT2hRK7160NON2ssGJq94C6u0dnOTfWQcmSaacIzcKQbmnTsmpl3IjiPyGJC1dEjcmu214nPMK82XWbjt1oQh7tEsucbvNLxIWyATFHfj7LU9P7DR2oQO4yMxaN2u5mzlj8S3yBD7oFjrgilGNT1EA8FW9wKpWgb6MRGa6aTq19EGFgUsyBCHXeLfz4vppDTpst-XAC42MeU5DSJZpG-21zTSuD6nqb5js3N2vehMUbj2zCZf3huYZkSw3O42Qd1dT74H6DJR_MkFchmUbkph0s0_AOL5mR0vxLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری جالب عادل فردوسی از تعویض عحیب تیم ملی در بازی دوستانه مقابل تیم ملی روسیه: قلعه نویی تو بازی با روسیه از عملکرد محبی راضی نبوده گفته خودت رو بزن به مصدومیت تا تعویضت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/31050" target="_blank">📅 23:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31049">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umdBb1rkoqQ8iH7OvPw__mLe-9leWVe2xYhX9yPBrZ3qO5hyN1wW7Lzbu5cp_IKJG13rt8uW-3dPTUKNQSvxaGPt4gR1Zd6Q9wU907A3iYE9dT7v1ARKxX2h84aQanw-5GRPNGPVmQKw1t3pHHgtDMYwOX1-ZNwlcPbFoa8C-WaqNfpBM6eJyVrBbtL8fwshXYj9Rf8REXr73cQjA_K4POOqV6CD43ACOEEHjPzt3cP4lp_bw80H6AJPHH4CcWTEnWvcB9Rp4TY3LPsFpSZyCb6aNnQSpN559zWyDnBn_gELaQAtFah6H55papl5qFaQiQujG0m54wUXZGLsjbksBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سکانسی جنجالی و جنسی از فیلم جدید دوس دختر کیلیان امباپه که سروصدای زیادی به پا کرده. کانال دومم داشته باشید کاملش رو اونجا میزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/31049" target="_blank">📅 23:00 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31048">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39c5af2a82.mp4?token=MvJz1ftUl-VClcC7qoYNqrO3M4hDR4DgC7qliv8S-Ruyhw5Ev7dbEc_gBXhCAReRq_V3cf0cf9NSdSHnfOKJMmJzuhSGxOq2EcsKzDuNC0UkkCJ3Brzi8zFKaDg5SQntH_GnKJlCj9pq8sA80gqLGHHaDYPsya28y1shGOgPaKpVoyC35cxWf3UwwcqvfIwZzAz3dbREFewVE9w-ajZvKNIXxFBy8k24uSw7gMsWlSwwmnann6sZkuYZdOIQUy7TBdI9vrjNzNnG2xDCaizfbQL80dB1pWDCwJww32_ieZbLd5lZd5Ys5mtnaov8FAXHccC0Bx3ThIuD4UND2tnUc1knfdfQEL3E2nvR0FDNU8ZnYYKRiTYl3QtWliQ5ikXhNQiiv-LPeLPrJr2cckCGAIoWeUVkLkvso3FOxwTD5MR6DHfejpWS-2howMahfYQ5BfdJiTDKUFmYrHfEZTnmrxtLQ9seif1J1zK_SN-5OcQvNoWepSZ7m4z3oQvubb-zRpBElGaBVEHHRcGlBIuzvTroDy5iiAXzBY8eZUZNFJDOscopcPBOv-rY6hgaZw6GOSsVVcCAlU2fIb6MzsWkfk-x9AcWsF_PfMXFTSaDl9cLX5X2hzN1qmbYLOvrkPCT0VuH3NCbOTM99pDWaGIuYo3bMHmeEs88bKoa1svu5mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39c5af2a82.mp4?token=MvJz1ftUl-VClcC7qoYNqrO3M4hDR4DgC7qliv8S-Ruyhw5Ev7dbEc_gBXhCAReRq_V3cf0cf9NSdSHnfOKJMmJzuhSGxOq2EcsKzDuNC0UkkCJ3Brzi8zFKaDg5SQntH_GnKJlCj9pq8sA80gqLGHHaDYPsya28y1shGOgPaKpVoyC35cxWf3UwwcqvfIwZzAz3dbREFewVE9w-ajZvKNIXxFBy8k24uSw7gMsWlSwwmnann6sZkuYZdOIQUy7TBdI9vrjNzNnG2xDCaizfbQL80dB1pWDCwJww32_ieZbLd5lZd5Ys5mtnaov8FAXHccC0Bx3ThIuD4UND2tnUc1knfdfQEL3E2nvR0FDNU8ZnYYKRiTYl3QtWliQ5ikXhNQiiv-LPeLPrJr2cckCGAIoWeUVkLkvso3FOxwTD5MR6DHfejpWS-2howMahfYQ5BfdJiTDKUFmYrHfEZTnmrxtLQ9seif1J1zK_SN-5OcQvNoWepSZ7m4z3oQvubb-zRpBElGaBVEHHRcGlBIuzvTroDy5iiAXzBY8eZUZNFJDOscopcPBOv-rY6hgaZw6GOSsVVcCAlU2fIb6MzsWkfk-x9AcWsF_PfMXFTSaDl9cLX5X2hzN1qmbYLOvrkPCT0VuH3NCbOTM99pDWaGIuYo3bMHmeEs88bKoa1svu5mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های عادل در مورد بالا رفتن سرسام آور و تلخ قیمت دلار از آغاز هفته اول لیگ برتر تا به امروز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/31048" target="_blank">📅 22:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31047">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f9838cf82.mp4?token=Qe0CGbJeG_wZozXRDMRX0VWV5MSn-QpvYiMDtSTq5DyqpfShy4CWFc6M5Ts4MkX2IuVuymAUm1_gdkCUjOo6Gbm9WHzI2nKoFsAwY8okrtICSWISKEoCfht3zfUEebao9qzn5_BY57XuPDyb4Cm8iM1qmgEeRtS--VmelS3_eQ6KAfytBBrZnCTECCGZ2aMT2rBNA0kh31DNUPqHxbT_bNX8ZwgSciLtElZx3FcqW0sEUPMMdetWR2hB9zM0CCZvAc1PdDIKr0cjBMLiM-uBWXUPY7FaqdXDBah41igBt2CrPsTA7fFNOQsi0_pNHM3ojJmPOnh8FVRiJhWVcHoBDStACCTs7z40LUHR6Ztrt8LyhIKgmHv7XKzXH06UsFTTl8hJAPoiA3Q4tBEsOsNVl0Zbs6iq6imWwGONYuBOqJS-Qtfp7IV8Nl82lgUP7X4kkE0Q8aNwdTwiZggrLXmsQzYap3sD6LRj_fiWQQI29rGCDCQAOPVZ475L1Hyz367Sl-F-Sx7cwzhNqA_5c9aoRN5J5J13arLgzn0E-QVSPeeL7qHRdtsDhwBNxfEsWm2qySNYC5p0dHEzG95_HKCZa0XP6rowUWrnTWMex6bTmnNS1IuWKYcBWyWwcjgsmGlMO2e_gDqiz2PDSrRrUI06lp0hoiM8ceJoRpYOBepbTR0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f9838cf82.mp4?token=Qe0CGbJeG_wZozXRDMRX0VWV5MSn-QpvYiMDtSTq5DyqpfShy4CWFc6M5Ts4MkX2IuVuymAUm1_gdkCUjOo6Gbm9WHzI2nKoFsAwY8okrtICSWISKEoCfht3zfUEebao9qzn5_BY57XuPDyb4Cm8iM1qmgEeRtS--VmelS3_eQ6KAfytBBrZnCTECCGZ2aMT2rBNA0kh31DNUPqHxbT_bNX8ZwgSciLtElZx3FcqW0sEUPMMdetWR2hB9zM0CCZvAc1PdDIKr0cjBMLiM-uBWXUPY7FaqdXDBah41igBt2CrPsTA7fFNOQsi0_pNHM3ojJmPOnh8FVRiJhWVcHoBDStACCTs7z40LUHR6Ztrt8LyhIKgmHv7XKzXH06UsFTTl8hJAPoiA3Q4tBEsOsNVl0Zbs6iq6imWwGONYuBOqJS-Qtfp7IV8Nl82lgUP7X4kkE0Q8aNwdTwiZggrLXmsQzYap3sD6LRj_fiWQQI29rGCDCQAOPVZ475L1Hyz367Sl-F-Sx7cwzhNqA_5c9aoRN5J5J13arLgzn0E-QVSPeeL7qHRdtsDhwBNxfEsWm2qySNYC5p0dHEzG95_HKCZa0XP6rowUWrnTWMex6bTmnNS1IuWKYcBWyWwcjgsmGlMO2e_gDqiz2PDSrRrUI06lp0hoiM8ceJoRpYOBepbTR0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فلش بک بزنیم؛
به وقتی دوست‌دخترِ کالافیوری اونو درحال‌مصاحبه با یه زن دید احساس خطر کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/31047" target="_blank">📅 22:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31046">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzSskgKoK1iu7Pxi6qOUpMZVPY638j2-s0EurYK8utoMIRzpGgEPvcN7ynYE90HdkAZkE7AcaElqjFIC3Flt1De1hDRu-uHyBarB2yC4byK7GfevpdIOLkCgn-VFFTeLaJr6k-3z5NpVzRxJxDzL220AJLezQ5klGtbuNw8iYqet7TojeoRh2pSEk6GzKzsL4ofTCe6mrE_uKMy63hVOKOxFZQOMpFDH2hnvc58lSIrv8WS--OOGWJwmVwDLryMIchUYLdITnTWwA-Rbfc-oS6jJZrF4gnfBAwGcUKYHnKxPO2WWce7HTq64fBSMVesc9le7E2gE8e57UkUCBbZjVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درحالیکه هفته‌اخیر سارقان تو اتوبان همت تهران تلفن همراه‌آیفون17پرومکس پیمان حدادی مدیرعامل پرسپولیس رو زده بودند. امروز همین اتفاق تو اتوبان تهران - کرج برای مهدی تارتار سرمربی سرخ‌ها اتفاق افتاد و گوشی جدید آیفون 18 پرومکس او مورد سرقت قرار گرفت. خداروشکر امنیت داریم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/31046" target="_blank">📅 21:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31045">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fe541534a.mp4?token=IpPiyg-KxlmuTNl2lrbhFm-dd_sHxGWbHdohw9Kyta3n_o8POQTFP7Tb5F_vmVMoS-hedlYACMnUY-yJ5ysiePsiRuqSiiPeZZbwixOqoXNr0KR7PgslMZLgm_tY841rk2XdBzftoTz3CvmfvHEEIlaYKfjhukJiMCWIKjk1gMrYNA7yhxXdq3_jI211o5WPuCL7JM3pNnUGlzTwxvDw4QUqDQ8dN39LZkAu5fFZBbSGiJfrsFhWFceaRAPqKB3ut391D_GmNiVExB84m71O8hkT0XgMwXpZ64IKM5AnRD2hu-2dQ9rJu-ilIsps0l6rkCGfVoBaUpFeFix_Ot0JBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fe541534a.mp4?token=IpPiyg-KxlmuTNl2lrbhFm-dd_sHxGWbHdohw9Kyta3n_o8POQTFP7Tb5F_vmVMoS-hedlYACMnUY-yJ5ysiePsiRuqSiiPeZZbwixOqoXNr0KR7PgslMZLgm_tY841rk2XdBzftoTz3CvmfvHEEIlaYKfjhukJiMCWIKjk1gMrYNA7yhxXdq3_jI211o5WPuCL7JM3pNnUGlzTwxvDw4QUqDQ8dN39LZkAu5fFZBbSGiJfrsFhWFceaRAPqKB3ut391D_GmNiVExB84m71O8hkT0XgMwXpZ64IKM5AnRD2hu-2dQ9rJu-ilIsps0l6rkCGfVoBaUpFeFix_Ot0JBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های سنگین ژوله به امیر قلعه‌نویی: من یکی دیگه فرصتی به تو نمیدم. در طول این چند سالی که سرمربی بودی میدونی چقدر خون‌ها ریخته شد؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/31045" target="_blank">📅 21:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31044">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nEK2PXHMtDv1oijJ4aFA8MxM6K6B-fPBL_sCZLzV2TBff4E5LgIONu32n0JbB2c9nQBvHZPOF9Qbi9Pn9bstxbyTdUN1JLoRLNnV2S86_hp2nZhi-1VAgGbdllBGIkrbtzvtczx2q9250i8k2D5UNsk4wHpd0FtOPRjNw3s36lmS0VwkWiwkI7WWuXgXxwKnGnpTwRG9GmLiGE66hxzPFa4k3WonyKN5Vihs1Xmhr268xTg9c5a5Lo_9jx3T1V8SZgLu5QpQudOMzGoijPoHBdfG1_ZfffOapDf7J5touZWBOhyTRhueYh7Huc2ZXxpm7QDlO9ouR2Dsdv0heABiVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
مدیر ورزشی النصر عربستان: با کریستیانو رونالدو برای‌قطع‌همکاری‌به‌توافق رسیده‌ایم و ایشون درپنجره نیم فصل از تیم ما جدا خواهد شد. مقصد بعدی فوق ستاره پرتغال فوتبال اروپا خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/31044" target="_blank">📅 21:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31043">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">📹
ویدیو کامل قسمت دوم فان فصل جدید با امیر مهدی ژوله؛ عالی بود. از دست ندید و حتما ببینید.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/31043" target="_blank">📅 20:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31042">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IyvMfkitP3iY9A_0DwTPWhXevGooxNcl6FB7EzY4QPClS9d8WjDxeuAgqSLyJS7YBmwvbtEVACPIQ-pc-fBSitbulBh3vikwDCe1tSHTUD9zWhqi8XhZITKzBAIFYzOw69Y_NTK2od7FtiUEgCL4IK96yJNC1GEQkpsejfhT-1Al_ezRZlisg-0_mOUOkvC8cp3Y0TuN1lQODDsTBVkn5orRgnOVElib5lTNu0ReAtU2TGNfBn2bLvjd_68OndQGQ4fN7naSeoM--C1D6HBpwLzMjdc-cGxgj49-iuDtXuon8-lWNGYDWCmQ06dYSvG5FDSe7RtFwWNRgNegNbd_7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین گلزنان پنج لیگ معتبر اروپایی تا این جای فصل؛ رافینیا دیاز فوق ستاره بارسا در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/31042" target="_blank">📅 20:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31041">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lB7D75poxK47aWq6HxaoU9zjphgE4DhlficVStMR291SrDWbHSFlv5tvpCywIoxbsAVvbheCA_v0Waiqt1YeLb47jslM5ERXcv-SxL0_60ltD2WverEbX67XjpKe4XuMVw_Pu8WvQG5xgzTvEXVIKbBr1eQZEaVHuI8b4khjKANQpfpYCueTfRfX6tl3uGmLeAIAC_5Fz93hU-UTNnanRi1BwwBS4eaC0DdYxcfoPrcW046Ja_PiBGl8DG2Keems17CTsw9FKPIYDlSiNSMlrwU0jCugq2453D5aojXFDsYV15So59jH0GaOPXjZCLS77R_3b1-EOneFkPDUG2lPoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکردخیر‌ه‌کننده و درخشان جودبلینگهام ستاره 23 ساله انگلیس در سه بازی اخیرش برای این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/31041" target="_blank">📅 20:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31039">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7381a71b01.mp4?token=icjaun75dzOUAKxeEFTkwRJCtz4n6G-A5ehZsbngYbdydCdCBt-OHpZbthT2jaNBBf_9-tmphmORp4slpdMrI4WBXyCPG04G2pEz55S7K81sH8nvlk0B6p4X4axMIF0ll8-o_4u7C_VDFH4EC03N5xHawSsDrX2xNyUd92gDeBZP3pVc_k6G7fdwSqH1FAS_Lyrl3npjaQh5orDpOe2Db09eb3PShq5qlbDSiThRykLfaqqA0spZUTo_bNUwePgz0kQF7kJ_6mEagSfWDgckNRROZvwaS0iHD_0900yxKLy8xaZRR2qCE5RC0u8kCJJ7O4R-17OiZATJ1XDj4FjkRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7381a71b01.mp4?token=icjaun75dzOUAKxeEFTkwRJCtz4n6G-A5ehZsbngYbdydCdCBt-OHpZbthT2jaNBBf_9-tmphmORp4slpdMrI4WBXyCPG04G2pEz55S7K81sH8nvlk0B6p4X4axMIF0ll8-o_4u7C_VDFH4EC03N5xHawSsDrX2xNyUd92gDeBZP3pVc_k6G7fdwSqH1FAS_Lyrl3npjaQh5orDpOe2Db09eb3PShq5qlbDSiThRykLfaqqA0spZUTo_bNUwePgz0kQF7kJ_6mEagSfWDgckNRROZvwaS0iHD_0900yxKLy8xaZRR2qCE5RC0u8kCJJ7O4R-17OiZATJ1XDj4FjkRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیو کامل قسمت دوم فان فصل جدید با امیر مهدی ژوله؛ عالی بود. از دست ندید و حتما ببینید.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/31039" target="_blank">📅 20:24 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31038">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qk_3xDwhM24nQzzOT1V3xa8boHNnb2MUsYDbJa9dPdexHca_dhuVV2y4_v4jSflSOo_GGEcytBGkGRb1ZOxHHWl59lYGZ8XWM2KImBrFGBpb5DgHguNiboQj45pqXQ4HlgbhvJ0vuFZj-Aeq6jjDOmLeFbiXPfQAflgXXvpfYY6pSWZ_P0LkCN3A-8sbkGay_Lu4gAKLaeewMQ9meqRSjugEVHP8nQzN0QerVme4NXeQsxd7OmeO-Lmrty0c_ElWAl0Ko_h57p7aRDIX3WLJBYxLw15GsGwhhAY489NLg6GV5GZ4eN-1Kuw4_JBjDvKH_IhkULyWtihAyi6HslY_kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇪🇸
🇧🇷
#تکمیلی؛ با تاییدیه کادرپزشکی باشگاه بارسلونا؛ مصدومیت جزئی رافینیا دیاز برطرف شده و او مشکلی برای همراهی آبی اناری‌ها در بازی مقابل ختافه در هفته هشتم رقابتای لالیگا نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/31038" target="_blank">📅 19:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31037">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_49b9mXGvR31qvtffeghBbRDbu31WCL07-CqQ9QbFstILdQJ1ydJmm4IlH-vUssyK4WyXRdo8q6trVEdyHqNHAkSZWEGrFLawKl6UgtZR3DrfuRs4hZBMfgQ7IIyGCt2cBAXKimgM1rLT9J7kCgfU3mZD3NE2o9LWoKEVV_MfJ4cHe3aU1zfqlM7gdQdyrEuY3SL_3dgoZhRtaf9DmMio0AxdqSFS2tKEQpY8tLjszb1iVs85OCp62Qc6V_VeyDCj3JxXaUx9RWK1eIkdWvdA08k_Vhurova45KHBRmnF_j5cbdMWQUXnLYlTuQUqELLkcfFz4d1dtrOT1YbyUx5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
مهدی طارمی مهاجم 34 ساله تیم الوصل در اقدامی خیر خواهانه 8 زندانی در تهران رو آزاد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/31037" target="_blank">📅 19:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31035">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKzOztEdc4pcK0z2irmeLs44dy-G3XL_gVpG7fRncjhPyOgm2691apQrozox_qekYbD0fzPHwcxv6aCpksHWy-PEJ2m8WR1PcgNnwfBvN392QHQ60FwcGU1DaSjDUQTFjZo98Qqd1_uTMhv5A-sfumBwxyOZw3HZ7-mU7BPBXxMccbrMG1Iw0q417ZkslKh8fPhG6WVbegx98TgpdKci069BQDzAA7EhzlUbnCaaiQAqh0i8hK5e_iTsLS8vqtd2FojpEH0mbIwLzwntvfI_gQfw2ZjXOxqIf_qTx_mtEtMohMJNH4RrZvuO5cPP_8bOuaBEwtEz_cZ7aTEsF5blqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
صحبت‌های‌جالب ساغر مرادی و فاطمه از هدایت یک میلیاردی سردار آزمون: این کادو برای ما خیلی با ارزشه. سردار همیشه به بانوان نگاه ویژه‌ای دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/31035" target="_blank">📅 19:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31034">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r33izZnT3vLLWtr5l0qk-YGodcxvqc-aJhjYgBCpjZPmNKMHi12oRS-P81aXm6THygMfYzL3Ja-ScyAlsbvcmn258a05mmkKUZrFKXM78Ef2EAhAFp7zfqtxsSKsqz0BYPstFzaV94MASO5CXbPS3ygwRxeTPO7IIXskCmbHkaPAMQC2V9YSy0W0nMc297ETrcNh_jjcQk0hgLzYPXbv6AU2vsThIA4s_VsjDo5IgRuXx9O1F4Bj2parAgU1xnqtXVT30AEoAKBVrRLldOryroOJRqNCNC8MAklwIHSfM1tHZoN_5yyLNspzwSDnVLAoM7OmiZirBKFzRjC9BtUzHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خوزلو مهاجم36ساله‌اسپانیایی سابق رئال مادرید و الغرافه باعقدقراردادی یک ساله به السیلیه پیوست. خوزه‌لو پارسال با الغرافه به قلعه حسن خان اومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/31034" target="_blank">📅 18:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31033">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRFMO4Sld_7miMeXrHh4UVPOyMNLME9_Rkev1hiRxsAhhE4O-uOILdDeXPwZ-e-ACuGgpyBAz6NXzchFYpDhffsfGFHSKZ2jwX-gz9egv8EYixOeR70_k9qSgBluP6OLw0p7Hv7KWUSUX_iQ1CQ2PtF17Iu2Xy3QfVLoxttPMS9KIqTyb-nrDDHuaIrOFdlSkYLbRGk_GfLbp_aEgCzhyoEvYIoBw54P-iVOXDHT9_ePF6Nu7z8XCTKhIFvC6yZa5xwtBJGjgEKH8ixGlDwr0Dsw_O6gejshkuHnjxDnM6tQUWdA_lLsF-eP84AMiUXxmbCj4nw44QObBJAQ8Q93Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇧🇷
تیم‌ملی برزیل در سومین بازی دوستانه خود درفیفادی ساعتی قبل بانتیجه‌پرگل چهار بر صفر هند رو شکست داد. یه‌زمانی‌همه میگفتن که هند هم مگه فوتبال داره اما حالا فوق ستاره‌ها دنیا این تیم رو در فیفادی انتخاب میکنند. اینور هم حتی تیم گینه بی صحاب هم حاضر نیست…</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/31033" target="_blank">📅 18:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31032">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOGn57u_gIM0lRcbRQyGo9yImhT-nYr5HLkdm7EgEruYbQpv5Emmho7z9YHnxqyd0-1AUMIN12-zPVuK5gMcVDCjqcb1KtbVs91sOkcJzIviUwgXbgY7cjC7fA1fhma0JRZImJJ6ioMJC1k5_ux50urU0l7QpKbpqewWNZThiPjUTmflQne5Z1cqnT1hJciSjPDA-QIszUE2_zxKLJN5EKIPUkdXWi6M_XwkUjFirBI8hjfq4CehbhBmt03B_NksA7ZRczuTCdHI4v-Hq63niZobAMJdktFwCSTe1B_JP0L738ioen42_JwJ_-H5zsfIqUZr051URldws2nmxzT1Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خوزلو مهاجم36ساله‌اسپانیایی سابق رئال مادرید و الغرافه باعقدقراردادی یک ساله به السیلیه پیوست. خوزه‌لو پارسال با الغرافه به قلعه حسن خان اومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/31032" target="_blank">📅 18:08 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31031">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJgLycbyADpLuhT4bDi59A8lboHWuRosZD40Stys6Xj10yzGU4UaB3OEuJSXIj5hU9zhM18AjKSDCt36jm0dvrzot5iLA-ZD1LOYjAzmfrg3diCn38PXaBGXleCf19m5Pq1kHYp4GDKKWIzMznQ3xgx5Rhm4tySiM20hVlyYp3ltXJv5qwYnsLniTjSDCXXH1M9opJSsg9TEGh1BPZU0C_kh6oYf-EF2UpCGkKsvoUyw9TT6k19-f8O-zJYdgyszTehs4Grx4PK13sw_939g2oGJTf_tTS2eMV7jo1n-2-S11Za1BS0JVJq8Awy6OUWwdS82ksGfIPZnJACQMchZcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گزارش ESPN از ایده جدید AFC برای جذاب شدن بازیای ملی:
کنفدراسیون فوتبال آسیا بزودی با الگوبرداری‌از اروپالیگ‌ملت‌های آسیا AFC Nations League رو راه‌اندازی می‌کنه. 8 تیم برتر سطح اول مسابقات به مرحله حذفی صعود می‌کنن و مرحله یک چهارم نهایی‌رفت‌وبرگشت‌برگزارمیشه و نیمه نهایی و فینالم بصورت متمرکز و تک بازی داخل یه کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/31031" target="_blank">📅 17:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31030">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgShSjHF5mqhyB-U3B1ZYTTU9Gc6d0drp8iND2atkxDS99KGgmanBLndJqR74hII2MgQ11i89G3Xj2-dHOw9xE0v5NCmbXAJ_RPat8eOlMKw1SCtY8i-dl-CKOEHm153jQLIDSF3IxeMqhX19fUmqh_HArRaxfbf_JVeb26dvF1W6KpwE1N_97uLk-AqMmVv-z4xhPd3mxzuqFJ3NyL_9mccscCD9vGJvAMdgAbl7osL9g6yaoAJvytUb_mk8713lMKZjweFobEcTqvi6hkNSLHWhLlmvPqYV7Ge17qYdUION1q_JFMGET-5xOvlC1JtaXBDqE6nGMjScQkCIBdFYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
کلودیا پینا ستاره 25 تیم بانوان بارسا در بازی شب گذشته مقابل رئال مادرید موفق به ثبت پوکر شد اما فوتموب باز هم راضی نشد نمره 10 از 10 به‌این‌ستاره آبی اناری‌ها بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/31030" target="_blank">📅 17:48 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31029">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MaAw5YzukqEdEvjVBUYpI0rbECcoEmUSo5dxpdNOqkw71DQf8Ul4f9CEdkuMN94pN_M06NZZ1ytS4QvQnMDpFpd2V2XdV2jDefkidOH9dk1BmJ3Js_P6G8e9q1FQN9r9DtgWXH3uw50UmV6liE_pF4lYrTv3u7WzkwakXajlAICJuWGGuTKQkymX8w4n2QutQn5j1ChvB78_StVlDVbqvyK-FYrcg3iWkdZi874dnb-I8H9v4s4AeFFox1KTG1FCnqIDFQ2L7b5Hs664yiwFtzkNbiVPyMl13FkCJw_YQMXNs5fJNYxyj3xbeFizpL08iw80bnk_mjd2CUOlO7PY_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
تیم ملی ژاپن امروز در سومین بازی دوستانه‌ اش در فیفادی؛ دو بر یک نیوزیلند رو شکست داد. ژاپن در 16 مسابقه آخر خود در تمام مسابقات تنها متحمل دو شکشت‌شده‌بود که یکی از آن‌ها مقابل تیم ملی برزیل در رقابت های جام جهانی 2026 آمریکا بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/31029" target="_blank">📅 17:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31028">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24cf5abb84.mp4?token=P0BNQjUknP0EFP5nifcmtmCLXRgPSohyZdvpF0ryJj7U3JOzkcwTtM-vTkOZGUrJ1Z546UaXEYWHjuwhZImm7bW-CORZp1VEq0RgL9mInTexjycGFrewVmmZVPtx8XB1tG0A9gTdUojmmsWVxHly-7IH5v2FNwJb1xl-PyVoR5o3HMN7DhGTihvgTekMg_ykN-P1mRxqaMb-klincM6Xd13ChKcLZzlIulcvip8EJ6h7rZtd_t-wx8f0cTaA8VDyyEGmQQswsZV1G4wY0AH1qzWoDUKsjcF90iPGrnHIm3JeH4dKG_osy8ElanGTEj4h37OFinK4L0QtdFTA0Iw16Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24cf5abb84.mp4?token=P0BNQjUknP0EFP5nifcmtmCLXRgPSohyZdvpF0ryJj7U3JOzkcwTtM-vTkOZGUrJ1Z546UaXEYWHjuwhZImm7bW-CORZp1VEq0RgL9mInTexjycGFrewVmmZVPtx8XB1tG0A9gTdUojmmsWVxHly-7IH5v2FNwJb1xl-PyVoR5o3HMN7DhGTihvgTekMg_ykN-P1mRxqaMb-klincM6Xd13ChKcLZzlIulcvip8EJ6h7rZtd_t-wx8f0cTaA8VDyyEGmQQswsZV1G4wY0AH1qzWoDUKsjcF90iPGrnHIm3JeH4dKG_osy8ElanGTEj4h37OFinK4L0QtdFTA0Iw16Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ماجرای‌شجاع و حمال‌گفتنش به دانيال اسماعیلی‌ فر دربازی‌اخیر تراکتور؛ عادل: یه روز باید یه مصاحبه با شجاع بگیریم و قطعا اون روز دعوامون میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/31028" target="_blank">📅 17:00 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31027">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HumlTUfbStwpjoYeuS92N1SfubtZ_jQglxHecpaEj679crL0jKf4Ytk_qnjLpHb6mP_AoQANZcYuoB-m9yeg5scAzH0md6eyOHAN4BbicsJXtYh0SLuANJEsTqUCT-m7nByeAet4Dq9JqeYXpKlabgm87AuzI60lW35rWR1XJLZXWJg2rNhDJhgvTVYPz4OhTzUbLMbAoX-Ol8xWOsrmeLy30isQUUlVkzMDdzKlRzPfii1GWmZNzVPvsrFwtMzuQ4a04WgyMlC1uUHgjNGHqDzpFQyM6XsdD7WCsgoLc9UGfmjlGiIl9e-aytannOkpL5YfYoxEUeZGgJdr0dXkAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
درهفته‌سوم‌لیگ‌ملت‌های اروپا؛ شاگردان توماس توخل درشب‌درخشش هری‌کین و جود بلینگهام آتش بازی به پا کردند و با گل کل یاران مودریچ رو بردند.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/31027" target="_blank">📅 16:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31026">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eadafe2e38.mp4?token=hvYW0XAjtdUVUZiG46RS3nh15zwYMJBENq_I12-XGnUY95i9snGec5JkJtNM2wc_UxLyIFbbGh9PD0qRLrbTbGjiOlffrIt_1KS3j4iXHw239B5SFJj6dqf1XGwbdGyZ-XB_O_wZqaJdiiVYjw1HV5dvihKvO1Jzvg420WZPhr2bHHv9qJCEqAO5gvhzp_QxUMADIodajnuMmBue7QnURpiSzYu2zJFpyyhondbkaVKrE53OfkckvSyxBUfWfz_rqI8Wh0e6ujmc5lwhSeyPkoYszywDGgE-NIEddUSYAp4gxe-F2jYbRE9lKG7EPnOi8uC_LXot8m4RP6dc-s6oVIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eadafe2e38.mp4?token=hvYW0XAjtdUVUZiG46RS3nh15zwYMJBENq_I12-XGnUY95i9snGec5JkJtNM2wc_UxLyIFbbGh9PD0qRLrbTbGjiOlffrIt_1KS3j4iXHw239B5SFJj6dqf1XGwbdGyZ-XB_O_wZqaJdiiVYjw1HV5dvihKvO1Jzvg420WZPhr2bHHv9qJCEqAO5gvhzp_QxUMADIodajnuMmBue7QnURpiSzYu2zJFpyyhondbkaVKrE53OfkckvSyxBUfWfz_rqI8Wh0e6ujmc5lwhSeyPkoYszywDGgE-NIEddUSYAp4gxe-F2jYbRE9lKG7EPnOi8uC_LXot8m4RP6dc-s6oVIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعداد سوپرگل پشم ریزون دومینیک سوبوسلای فوق‌ستاره‌مجارستانی لیورپول بااین پیراهن این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/31026" target="_blank">📅 16:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31025">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/476bc74d95.mp4?token=e3Z2660jEIc73m9l3gz7cqyiGWowLuJYXoQnBsXBWH-jr8dhiVaO-bc3jvYTeBPXLb2j9ZWAF8x7cvwzoMVic25Vi4V5ppnNPePMFo3lsWoGtd3WfRbrDU6oSOagaMtlW__1z5hBzq1n5Lh4VsP71k747Oim8gwZvgPalquyt0Uc2JKmFvlInL0RWLK6PNvkqDNDdrvOP9rufgn3GKyKzivukQzNqqLOB43uyKxjEnPxDxaXPGF6DPz9q3VpRjxVHukcFSK7Nmy827OVekm6qCXsI6Q3w7OXzP1sEvIRwB4lrhpPn6Tj8oj01l_8RidyDIO9GdS-DblL9_2L7k5ndliAcAjPpKWJdk-I1aGmiChx7X505_1fXqfRTUIMT734Ut842Ja25exFeaVrVqp4aTVnppz5c-LedXwYID3Tmek3av5Bgf6svc1NwXgFV9-idrqVCTzOSTKkaPijEDyM-ksMJigzmWn6CKTWVcCoXmW7NZKHKpLMqslJSrLbk23DqCaGlYO_PKrD5I8easmpCfgnpPMlPz90upWeaRV5MYWSr-a1wIUWPz9ixebx2MBJzgA3YpNAzles2Mg3tTBV4pWtTA6G_yEyRAR9qhVbPNs44DGAXTEMe5VhxurQtjjvpIfrK4eUTYfX2rfsKVTqjbTzX283NywuvFQKDvTtvZE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/476bc74d95.mp4?token=e3Z2660jEIc73m9l3gz7cqyiGWowLuJYXoQnBsXBWH-jr8dhiVaO-bc3jvYTeBPXLb2j9ZWAF8x7cvwzoMVic25Vi4V5ppnNPePMFo3lsWoGtd3WfRbrDU6oSOagaMtlW__1z5hBzq1n5Lh4VsP71k747Oim8gwZvgPalquyt0Uc2JKmFvlInL0RWLK6PNvkqDNDdrvOP9rufgn3GKyKzivukQzNqqLOB43uyKxjEnPxDxaXPGF6DPz9q3VpRjxVHukcFSK7Nmy827OVekm6qCXsI6Q3w7OXzP1sEvIRwB4lrhpPn6Tj8oj01l_8RidyDIO9GdS-DblL9_2L7k5ndliAcAjPpKWJdk-I1aGmiChx7X505_1fXqfRTUIMT734Ut842Ja25exFeaVrVqp4aTVnppz5c-LedXwYID3Tmek3av5Bgf6svc1NwXgFV9-idrqVCTzOSTKkaPijEDyM-ksMJigzmWn6CKTWVcCoXmW7NZKHKpLMqslJSrLbk23DqCaGlYO_PKrD5I8easmpCfgnpPMlPz90upWeaRV5MYWSr-a1wIUWPz9ixebx2MBJzgA3YpNAzles2Mg3tTBV4pWtTA6G_yEyRAR9qhVbPNs44DGAXTEMe5VhxurQtjjvpIfrK4eUTYfX2rfsKVTqjbTzX283NywuvFQKDvTtvZE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سردارآزمون به ساغرمرادی و فاطمه احمدی دو تکواندو کار ایرانب که در مسابقات بازی‌های آسیایی ناگویا به ترتیب مدال طلا و برنز کسب کردند، نفری یک‌میلیارد تومن هدیه نقدی با هزینه شخصی داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/31025" target="_blank">📅 15:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31024">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6e4569c9e.mp4?token=cRqpZ9WRoJBuYFOuH0dCrvDHuXpDQ_hpDaCWngo2DjDCAnZclHHfNQoL8wklnTFWY7H1civW8Jx88RA0de60G4bOFt-vffn6ZnaoKDuJxJID0cCsJDjOXvkrInyIZxWMzHX3-gspFz4QZZsdpwdWUrqWS90tKHM_0N4k3DRvDadpCD1QYA_jooEW270BwVuPjOj0Ys9X3GDHDTH0Zxfh6czeD-U86KJDzrs0ZuUWeDNN5cqeIyxbRRZjVoayU7H9efd_VtDLhrudsXMY3fdEtQXStLjBhfqbR98xQ3RqsRjYqpHda915IOydZabq5z0uJ1tRf4gZyxNt7aM7Navt6zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6e4569c9e.mp4?token=cRqpZ9WRoJBuYFOuH0dCrvDHuXpDQ_hpDaCWngo2DjDCAnZclHHfNQoL8wklnTFWY7H1civW8Jx88RA0de60G4bOFt-vffn6ZnaoKDuJxJID0cCsJDjOXvkrInyIZxWMzHX3-gspFz4QZZsdpwdWUrqWS90tKHM_0N4k3DRvDadpCD1QYA_jooEW270BwVuPjOj0Ys9X3GDHDTH0Zxfh6czeD-U86KJDzrs0ZuUWeDNN5cqeIyxbRRZjVoayU7H9efd_VtDLhrudsXMY3fdEtQXStLjBhfqbR98xQ3RqsRjYqpHda915IOydZabq5z0uJ1tRf4gZyxNt7aM7Navt6zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صفحه رسمی جام ملت‌ های آسیا با ویدیویی از بازی ایران
🆚
ژاپن درجام ملت‌های آسیا نوشت: تنها 94 روز تا شروع رقابت‌های داغ جام ملت‌های آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/31024" target="_blank">📅 15:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31023">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQK3DQJIpM0waeVioch4kI-z50Kkt2mTicYnwah8k7uiK1IiJuVwnifZbVGnBeEvVKCLyUASH88TjNNz3guA8MN65UPCvNLvMClQwwPa5thc1Qv1mtex52vpkqvOCKsK7iJyGa5pUabs22uBSDSp_vfqZLb1ZJyJpUD7CYa7FoR421OZpVz6DalYpKLkpry7NoWl-mh-kXgNlEcyS9e3o-oAVNR2XWKn7pSwD3iXtmjmyjwGYZv5Fgf1HEjWmYamHZaY4Xv6_SoFJb5yyFWBXVY8-DiczLCCM4kO0aeT3iDa4u_PJzDtocKPja2rderyiPGRxeembaaj62adVZfe9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کمیته استیناف بعد از برسی کامل قرارداد یاسر آسانی با باشگاه استقلال؛ با انتشار بیانیه‌ ای شکایت سپاهان و مس شهربابک از ستاره آبی‌ها را رد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/31023" target="_blank">📅 15:20 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31022">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJe5IsafJT9qswzy1Widkg5YoYXVIBGiTMNb4bKv2_HQ0h6AqJ-Owqan-IettKqDMulC9-7ulqClVi6iMzIQiq7h0ft3xX-riCuXAQrXJIr9gaMGNfPQ59kUoMUxgnb8lYLuZIkZtIP_R3cTEXmoaHV8bUKRWOhfDAjXdOYFH_XlTPAgGKevYFPlKW4oMzsjhzwhpWikfAd8iuL6qzpj1aHZ6lbNv9SZ1L2JelktUWNjmk-l0M7SrV5tFljxvNVl6p5kDeSDt9CqJMVJLST4GGO8A1XYcxC1ZQqstPH6KV_mDYxAeaGrXjf-cmY_TTAb_1FSq6DMvxQfn3ES_tYKoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛ خبر کوتاه است و دردناک: لیونل مسی آخرین بازی خودش رو با پیراهن آلبی سلسته از ساعت ۰۲:۳۰ روز بامداد چهارشنبه انجام میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/31022" target="_blank">📅 14:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31021">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olO-C7bJeLrSWoi-J4ojhFIQ6N73vhimeTm35j8QUwzHKfH9Dydq8SDdQ-9pe_c52PAXDMb4jC5QznhMI39h7cS4cwasWUOh2LsbFFoThryvEhwJYTwD4AvCddKguEUDpGDfik422ERbsqyYTDg7mt5Ze03rYXmjYvep3aunP_qdrRvu8AX46iz8Xd_49u_FcrJzRYDQ63B2Yg-VZMEdCii2JyFst5LSBx4KfcHEWkSXfhKvNtbFTl5lCuQNybnky0rPNd2fnrQkRmP_2pnbHRfJ73MlQZ2RSJyPXltMkKsPqHlV816KxQM1qbvM8RvvI7yXxvdAkCSV5hjGG9VaDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇦🇷
بیشترین تعداد گل زده برای دو تیم ملی آرژانتین
🆚
پرتغال در کل دوران حرفه‌ ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/31021" target="_blank">📅 13:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31019">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Do13WBb1onofc8wbC_tFB7QXJFgMpyjN3arlntXyXEU3XrUyiN3IRKUijbWeOmftE-3wyEpgaAtm9Iy3sUDLP5r83v8zSgR2MxmAWMdg3fIjBbJOvJrAZ980MnJtSzOaiXm4UxKiv-o_dTaKH1zRkV9nQ2hq404LSDAHCVE32Mw4XgPwBPE26x84RHgydywz2rNzv2ohXZhuPUW2h6d6s4uNW9qSJSq7jxTW8UeBPnJbL2sf6LRhmOXOcn_4sQgVX2oH3wBMpkiZ76nRjCbRv9NEz4K6EqO0h3Q7050A_28aVhND_mqrLfgJYegspY1cl5lt6QVNxKiaaud1Gnjkbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fgkod2QN7omYC8BrC5Tmh7dSEi3oEtM6tQ4F9oVxhLAiMCUEEAxhuu1HX1Q5Ydi-s4NDsMHZtUrP9_6UwyeUmkYGwfHGf-bFw1OIqvFqXBhBPZTTrmMZ5VrTMD59OHlD339ay9IaNMhuNX9FAR--lBX074h8zRQlp1tB-7iyjgscjm1FK9sB3hoX_r_N9iWMf4lqWUCtEfwaBMHJJtL-OP1Hs-ishDprDbGslYrByuLmymivnnU0YREfhO-jeuWoNBKiIjjUc8A67PlVmyZ-N5QCi7IyCXSUlCryQUvgSNkVEQjf3OXmsK4_exM7uspb2yb6_zXdKoJdDeDeHZW3wg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
🇦🇷
بیشترین تعداد گل زده برای دو تیم ملی آرژانتین
🆚
پرتغال در کل دوران حرفه‌ ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/31019" target="_blank">📅 13:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31018">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W243T5I0arm9Ub9M6IcFAZEFjiF_nJWMx3f3QfO1kQrW4Z3HfE_jluKxacKbMJNmDppN3D5V0HZ_EzafAuwfe1M7txQ8A_Tp2A8c1bhAjX-U-wcECNngy38D6KFbFyWjgM_QHx1YesnTRBlZrG2CUunzhsB0pLr3SDVhAQeEQ8jbvOjyknSYP97U8dIdKnn-ZLFFHE2K5ZcQtsWjNOCILHGBE93ugqwNKk2zaDZQwzidec9qm9XzE_qAIci8NVSRuOipEanHj5bjN5fsj3pkLJdMDIxxB7EqdoKaEzrU63h-T_AaziLTM5a0AVdIyataiP1YUxpHqtklVqYxFrt85A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خورخه ژسوس سرمربی‌تیم‌ملی‌پرتغال گفته چرا باید از کریس رونالدو عذر خواهی کنم؟ نه نیازی به عذر خواهی از او نیست!!! پس بشین تا برگرده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/31018" target="_blank">📅 13:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31017">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/034d1249e3.mp4?token=QWdfK24reO2pADDzBhdsDzbALDR7mGe929xZReNJW_cDen-SHLUgOaJN1MhtNST1s04pcQZC--AqHl8-UBgyQs6dMNS0Qb8C9phOw8HztyANLtEIltoSHrxIy3rfIXWtDvIL0MbHPOplVa3cQewQPJy19hDfgjIMSTQV_0yJD3sJIkBN2XTiHpwXsPg7wCAHvoU9KhUKhZLRrXNKuDFcgW5q2Jo_0F5NmwQtLMkWsq30_nZnl8ohnI4e_QfYhxMug7bX9cjYr0B7HP0K9zNAdefhJ9V_XxGUhLTOcEk3c5kmCVXUGLSajfRnR9hwCpPppXPijasV1gTA35eEVMZ7JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/034d1249e3.mp4?token=QWdfK24reO2pADDzBhdsDzbALDR7mGe929xZReNJW_cDen-SHLUgOaJN1MhtNST1s04pcQZC--AqHl8-UBgyQs6dMNS0Qb8C9phOw8HztyANLtEIltoSHrxIy3rfIXWtDvIL0MbHPOplVa3cQewQPJy19hDfgjIMSTQV_0yJD3sJIkBN2XTiHpwXsPg7wCAHvoU9KhUKhZLRrXNKuDFcgW5q2Jo_0F5NmwQtLMkWsq30_nZnl8ohnI4e_QfYhxMug7bX9cjYr0B7HP0K9zNAdefhJ9V_XxGUhLTOcEk3c5kmCVXUGLSajfRnR9hwCpPppXPijasV1gTA35eEVMZ7JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
چراغ سبز سرمربی تیم‌پرتغال برای بازگشت کریس رونالدو؛ خورخه‌ژسوس: پرتغال همیشه خونه کریستیانو رونالدو بوده و هست ولی‌اون خودش باید تصمیم نهایی رو بگیره. من هیییچ مشکلی با بازگشت او به تیم ملی ندارم. یه سوتفاهم پیش اومده بود که برطرف شد. همه ما منتظر بازگشت…</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/31017" target="_blank">📅 13:05 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31015">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Da_42NdhWGfrYJQ2G8seEw_2zvEXTTdO4YUZ_LPLVEGyEpfutamdSgnrDT-nWDbyLSONmOYJpthk6I49lMlm4-ySqH4Ge34_H7sE53AOpju2hpo0naDwKlkWIx273EFWOHJxZtLNtZM0zZuMeB12CuWI9h7TLVFpHLHRLTeQKZpk-AiscrsGUBO1PMZF-8czIyUU6zTErc9oJPemqr214boD-Mq0qNli5UY2p9ItPNrNgTjidADJn2qHZ-zAPbqqmc2d_oJkXcMZ1fH7ZaKYu7gytCs8AztP3xWKcqChXwjkgDD1Tx7ZXlhqyydG5XTNh1U1I-s6C5nAu5OaBVQmHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/niOu44xzH8tQghm7sWda5uj0f-345TW07XZuzGf0ps1FFrW7wM41yx5ZY_qmesBenYEeqGrHcyM9FFmuzxy_NoAySCHbWFvXIv-4alr8_TDVNE4Bsw-KZ8aid-VIIwDwdZ2HcoVBp2GtXX1S0yy5GesVkfCxCKjb5FExi9r7vzatz046HN7iSRT3xisz982_YYYDIOp4Skv76UNVBqFPW4-jzvTR55y75BJ5V-Ijis-jQPnjY0Gm3YeiPMwcTrTPfGsk__K62LzZDl_fa2B4oNCPxepvz5XIVb2_E0buy0hOXUVV8bDbMs5a7zgDZyhsXEoMyiUA-fSoNNXSKrsNTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
#تکمیلی؛ هفت‌گل‌تیم‌بانوان‌بارسا به رئال مادرید در بازی شب گذشته؛ وضعیت دفاع رئال مادرید رو ببینید. قشنگ میزارند بازیکنان بارسا هر کاری که دوست دارند در محوطه جریمه انجام بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/31015" target="_blank">📅 11:23 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31014">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQtMCnIFUSrCK5ZSuy44mV9tJ1m1DLrx_01L5yG9HHU51AWlLwG6aoGSjgzABogA9Mvf9ii1HmpJFWFop2tASc2Tpsszw0pBarcD-uO8ZL64RgQl_ACF2vO6Uc0DPebI5gDrwTZlkrbyzoVas50VYzoH_Zi4dVO3IarfWxsr1e_4b_37sNQYR-Rbhfy4xuAsreZF9GsIJta-z6GQ5dXrSOGgGMlT8H8cFyGxJBolk2Y7vu9gebODIqTNVxq4H7Jkl_egGwvcOSDMssS1G31Qngqekiiio5k1m_s96W_D9CKcybpkqUifrPX9wbDPKaLMpeXGtVUkAc9K9PyR145gSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تتلو آزاد میشه! پست‌جدیدصفحه یوتیوب تتلو: امروز دادستان و رئیس کل دادگستری با تتلو صحبت کردن. درصورت‌ارائه‌گزارش‌مثبت‌تتلو فرداآزاد میشه!
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/31014" target="_blank">📅 10:48 · 13 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
