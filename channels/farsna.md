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
<img src="https://cdn4.telesco.pe/file/Xv_Fisb2B9Gc4S4juiSUqUljC5omq2RpA4QBEO3OEyqu2DKfYoX3KieZ8feykro9bJ_cBkDhA-ZLBcoWTYTS0lMjMoN0vlYMoEkj8Q1uXdZdQoszwpF4y_WuvRoXC9roPbm463h6AQEwbnEdGMsVIqmAItV6jaHSrKqL-uF3Uo_V3kLTU5SWGhaoO03DQpFID-UUMN11FZNIB6t2Wh26RByFnMJwUnDYRJfGsfGI2wgMbhQP_ApVIuBNpukjNOo4TBI66Vi_z5nJjacRxQka0sCar-j8wHleS4LnlR1RSmAK0_Ihn4kIGC_0vDmGZqZhGSb5f43_b1c8Tqtt45sT1g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-27 02:44:05</div>
<hr>

<div class="tg-post" id="msg-456690">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09b94475dc.mp4?token=najKimPk3jyYx2rn_TrMI1Pu7on8_p58H5a1c4hOCns6zVJiulepntGtGNKdfUXm1ulTH3WQ9DADdd3Cp8M-GAWgK3dDvD4PgdaKhNFYFT--9-USb3xUm45fyQOtGC4MLV8M5XX66Kp3sKp2lnhDGSO2QfK-jzo8G4dqwBeo81w6mxHcxVofAgaMoiWgwGY2fIIshmedqmJltq2JMIVNQXjrrVKXwcWXZCqsXZkAAp5G_a4SvDBFU-K7zxuIVysF3Hec8-ZKWuDKQVtTYlOws82nC48Ui7NepVQqIDhbkDqW7nTwRVVmXJ6jfOxdCHnpiPVgT9WBSWWx-qW40uGXYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09b94475dc.mp4?token=najKimPk3jyYx2rn_TrMI1Pu7on8_p58H5a1c4hOCns6zVJiulepntGtGNKdfUXm1ulTH3WQ9DADdd3Cp8M-GAWgK3dDvD4PgdaKhNFYFT--9-USb3xUm45fyQOtGC4MLV8M5XX66Kp3sKp2lnhDGSO2QfK-jzo8G4dqwBeo81w6mxHcxVofAgaMoiWgwGY2fIIshmedqmJltq2JMIVNQXjrrVKXwcWXZCqsXZkAAp5G_a4SvDBFU-K7zxuIVysF3Hec8-ZKWuDKQVtTYlOws82nC48Ui7NepVQqIDhbkDqW7nTwRVVmXJ6jfOxdCHnpiPVgT9WBSWWx-qW40uGXYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برای خودت با یک شوخی بی‌جا شر درست نکن
#اندرز_مولا
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 642 · <a href="https://t.me/farsna/456690" target="_blank">📅 02:37 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456689">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qey2LlM6f-Eeh1jtS4Y7O1xhUKo2tJvxfEm7NMtLaTspdS4kw1Y-UYHX1ENvGvnliE94twTyGfDb4iGsYqkL-6HoaXs302LOjwDKXNxcXKaqtQfk0ErWFUmNamRogcZSR_urp2w37AxKyi6alOB04vQDv5qJv7XGzbKd0b2n09CMACfl4S1CqwF1rQ45hZc-8hKjqzg5wv91uYEaFis1cbBlVsHqakUU9Nxqvn5a7Qp3aMHovvF-IFGDeRKUU0da-8zhFqQN2ffWc0DAbNogL24eDU1sugC-RbxSgx9kyJQZeosmLhHbYhcI6hn3b6atCfZMhac0DppdlK-6b9_EpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروط کتائب حزب‌الله برای همکاری با دولت عراق
🔹
مسئول امنیتی گروه مقاومت کتائب حزب‌الله عراق ۴ شرط برای هرگونه تعامل با دولت بغداد تعیین کرد:
🔸
خروج نیروهای اشغالگر آمریکایی از عراق و تضمین عدم بازگشت آن‌ها
🔹
رهایی تصمیم‌گیری‌های سیاسی و اقتصادی از سلطۀ آمریکا
🔸
خروج نیروهای ترکیه از شمال عراق
🔹
انحلال نیروهای پیشمرگ منطقۀ کردستان
🔹
این مقام حزب‌الله، نخست‌وزیر عراق را تهدید کرد که در صورت ادامۀ اقدامات خصمانه علیه این گروه مقاومت، اقدامات تلافی‌جویانه انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/farsna/456689" target="_blank">📅 01:55 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456688">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3ae134ef8.mp4?token=MO_0YG3vGPllWP5SAETou90XQ9fZyAizXJPuc83G4WXFRJozniCkWwMxDH40JYA1g5ampjFMfrW9gkG003Ym3FYCXPfkrN22dKUHs-WBshTAWcFPmdSAY4c_JfuP8puA5hc-F7WOKSasAFOUFhc18SrDZdnewzD39JFwg5S0_g_I60mw-PoKtzK4_iUmIa9wh8vuK0KHWEWrT_yzX9vXDUpvUOxqacZQE_ppWmoRaS7W5VoS5K38aDi93pSTRt4xMwjaBEYHTzCIxK4DhB3qirx1_T6ABFR3eLUNo4wFlOvzkS8oMr1J4RRgen6FnjT-m9wKelvZBgs0uJFVjB8WYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3ae134ef8.mp4?token=MO_0YG3vGPllWP5SAETou90XQ9fZyAizXJPuc83G4WXFRJozniCkWwMxDH40JYA1g5ampjFMfrW9gkG003Ym3FYCXPfkrN22dKUHs-WBshTAWcFPmdSAY4c_JfuP8puA5hc-F7WOKSasAFOUFhc18SrDZdnewzD39JFwg5S0_g_I60mw-PoKtzK4_iUmIa9wh8vuK0KHWEWrT_yzX9vXDUpvUOxqacZQE_ppWmoRaS7W5VoS5K38aDi93pSTRt4xMwjaBEYHTzCIxK4DhB3qirx1_T6ABFR3eLUNo4wFlOvzkS8oMr1J4RRgen6FnjT-m9wKelvZBgs0uJFVjB8WYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار مخزن سوخت در کردستان عراق
🔹
منابع محلی از آتش‌سوزی و انفجار یک مخزن سوخت در سلیمانیۀ عراق گزارش می‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/farsna/456688" target="_blank">📅 01:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456687">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">گفت‌وگوی اردوغان و ترامپ دربارۀ ایران
🔹
رئیس‌جمهور ترکیه بامداد سه‌شنبه در تماس تلفنی با همتای آمریکایی، ضمن تاکید بر اهمیت ادامۀ مذاکرات با ایران، آمادگی آنکارا برای مشارکت در این روند را اعلام کرد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/farsna/456687" target="_blank">📅 01:41 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456682">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rfa0dlubhJuk3SbwASLHxg4cABuSAFRxt9cVZzsH6X5jWJ5g4A_LpW-0jz8X0tiW82mnycqZtpfiyTxNH0ULJlrpLnZlYzPalCMLSzjX9nrVMUQGQc4GevrWhIESWTtcXXw0hyZ1BKKhbw6AiJprTVeNov6LnXnF8nqwU-DGPy_xxLtcc1VZBpGxWHMRUT7Ho_OGDNfHRZFiBnbgguDYE0Xju1VBpGs2omFCtS_QSWZdYP2eZYiZr_Bf_iTC_FMr8t__C8jqaLRqrvDdk0X2GmL4_-qf-cKvcXJmvbUIM9kmVs3ZJ6CnvmlCK7UZQaNMzKPL1myk_jSmxts9a0Hlyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dZvD0hQ4vM5cvXiAvA0J_GA3Q-e8pif9F7-jyMs_Cde6t8D24zO10zuD59A45-e3ISyp5ImDrVwva2Cc3FnsCTUpGfg8gCS0rR0W2INjpvATKgNaqyIDGrDJzswO9yH3PwoOPDsrGDrVk4pTwq5C0OzuF3e6VZIQbRe-lcuyqAqMV4UzsBdiYnbgc73-UmjEdZ_OZUoBnXv0q7QZIJy0FTTWGeSxklL95f3HfrmiLni0GmMAG2woq7HmBRkdNYoE3UTjgfOy6Vyb5iPSxzK113fV6ZGIsDfdbURhMVISioqf-JT7hL0PsioLoiGhWFivAiLeOs65jmSlwHGg3j-yFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F464te7C1LPN3mDFu5-N6c64pTl2zDlTs8TtwmDxWiXdiX5my4RUgRZvHz_n22H5T7_PkD3FqivcHzgbDlFlRnS_ygVFh330evQyYFJ7Nv1d4rvUwXjKJ73JtLvZ50kDEveyZvfs9_DY5GQTbwzfcZSB-wMt-bonWEfXY_XyH863e5AkQGqZoj6ZZ-g-HXJQkjwUe2oVgaZQshLuMR-nTPQh4dVYatd-c-xoDFz6Y5zGkXhuHJ0zfCujP_83cAooVca1hBly1M0LjYNt2K1oLtPUegOpp5AQeCeZkFST9ZN7ZFMsqcZL2IevRHZcuGog5djP1SSX1yaGIqQg0zABRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EeLLmfY8A0cCPL-1WSuR7urfD9AUhHEwWUOV94Zuvz52cIqckrvO7X16P3ghgsnd47u9W2yTlLyF85q7kZfgJp6Ooc4sIMsNL6ByYBcY0xRxeVZrIkt1CrgVVS_Tt1WDbw5Pi6fSYcq--bpvmK5ii2TesTmPjwGr22blU_C-nG5XOLoNW9Zxp4x40vZGZDJXH1ws2FN0AfaNAj0pBABs447pedmtGex__ARa_X5w2JGfRiGpQrqSND8rR3RSnUJ2ODTByzEM3v5juhuBTL6dAME571AA1se8-qNaA7m0Fao98gSDYVuWlTZU8-L3plDPPP9psRRDH00eUSwyYTHrEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NvtbNmSRB0Ma-PyjXDcQTSBkgBmy03pg56T6SwaPA-QQfcXa6eoTlblWcrMSX_UfQo_hASBqwUZGAUWUat9Od4Fue6Zm_i1Kxq4Eq4aBBUIzDKiGFGJptrFU2R66ynZzhnPQaLHQuyMUnZS4qeDLUmxYtY9YyHpbvKkIXMnlYaJ8n8z74jdoJsiYdCnGBGGeZe9yHCC66fwvEDolWhKsX8CXZz8iFhTa0Dwl9EEr_WGss_bkfb4fNMIBGf48Q7j_3H8jRpgGWl78pxQ8ciBWgYl6AnqpvG1IhhaMFO5WXxmVGEeS8YGHHMxDEk2mOx58_W993xYQDwkkJhqIQcS65Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
آغاز محفل اربعین قرآنی‌ترین رهبر جهان اسلام در مشهد  @Farsna - Link</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/farsna/456682" target="_blank">📅 01:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456681">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">انفجار مخزن سوخت در کردستان عراق
🔹
منابع محلی از آتش‌سوزی و انفجار یک مخزن سوخت در سلیمانیۀ عراق گزارش می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/farsna/456681" target="_blank">📅 01:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456680">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhOJNcXKLdg-xH__ToUZ6ogin-KTWSdN6VvTZDC0Lyh7c5P4dKCKOvkwuGl4uhJbwsoa4uwQ_K9wUQsL6fTBrJ_y-baQCE0pTwvF4utImn-ARLFf6_l8CdrjUf4A-34CbJdNh-VFYMl0bltqxeOfbC5bjar8tLB0oVBWIGcN9smGNA87JVb7pWR-XKenSjcECTzPSkYExvhRiSSWusYhgcUibnqrPuUz3EiB0esw6CkLbaX9XULQ5NZPSLJzZIHpIfy02DTfQEmQjZ69CfkmGeC_5355nxFN0uIHSjwHrt6ivXHx2o_wacO81ykUDAbW_zagSbW_HreFaAo_HmWnSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتی حامل سلاح عربستان در باب‌المندب منفجر شد
🔹
یک فروند کشتی باری با پرچم اندونزی در منطقۀ راهبردی باب‌المندب، واقع در جنوب یمن مورد حمله قرار گرفت.
🔹
این حمله در حالی رخ داد که کشتی مذکور در همان اسکله‌ای پهلو گرفته بود که پیشتر نیز هدف حملات مشابه یمنی‌ها قرار گرفته بود.
🔹
یمن اعلام کرد این شناور حامل تجهیزات و محموله‌های نظامی متعلق به عربستان سعودی بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/farsna/456680" target="_blank">📅 01:00 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456675">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g7Q1FZo1FT8JTTL9J6-d-G3GX8Jgwq6MavTi0CXbdbgFURqWEpqJMQLoU0UvjjVRLa5EQFd7MCphInzWil8GkoCw15BxykQpqEzDEUDNPIqKU2A00HDQKh4aQVcEQX7Z49GumGaDmyf2l7XM9j4tW55uwwDIdOGWyZ_wx8sB5hqdSuct24uJh-_H5bnaIOIbz5DXQIuMMiZgC0ZWjIGXjaW67Zj9q61s6iJx1yQ_IB3rh4UEtXP2XsQpEWrmcTzIyFFmhWMBjOdgnaNxcTix_FNondEnYQ5L9jKMLMEvb2Llhmx9vZF-ZgAurrj4VRfO_49IV0Vtc8K4uyfai33ujw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RUjWcxbmVkcHtY8yli2Fv1g4ePOgruARdwjx5DgqWhmmxY5zXmmeHIxAVIlhyiKJ6g09quJapQi_3Wd4YLEpt-XEXe6_GhqUFgA8-488Pw4rz-qPRlSoRimGj0SIUH9lgZv7uXwdEPoHdFvFB80rNdkjTmHcW3V1FXunNP4rpP2PaaPtuwHClO64x4Dqym0TrtYXs65ObUtzZY5-mpUdaMSLvwApCbLrxMaNIGJogC9WzCVGBnVCrqCH7NctbdSoZw3sc2USqNJRmKLZ2IFhLjzGJdCLq1cuEIatOKubWQ8h7W5pfHLSUZbTYMj3oS4YGH-1Mx_GSVQ9wh9S9aFSrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FdhdOcbM8xCFaZSb51f_qYm6yRy8XiW4Eyo9Bhr2asaDrtJcVOuDhIDnWQPld3IbbCsE7XkzfopwUUtyln512dzlvhT9tim2AvJthyG7l2FbvuCiMSBna2cTOcgwQhxaNkdfZoqxXYWyYzmitz8pYXqLteXNhXyMhq4xM41ivza5A8E-rxy1NRwkXQolkbEuFyvSRuxFN3JwZ0l9K3YapFBj7McrowJTt5Uk0Z1ckTtGlQ5ysM3nSiZfByAriZOJsZfgVGYNMlgsK9xA77c5aHjFsraa-toal-kOUBwQPgRo1EERF-ZsjxHQUyBZuTdNlTYpiVJfs2zFxtA4GWWHzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OP5iGXou0cu6bEhQoa_Yv2SAE-vEZ5TM-8mFkjbTl4VVAL3LtupTF0t6hqmZO6v9sPinzQNvnkkv4IfdqIwTCdxYSjIsgLNYTNjDt8OQedWv7OqMX_3KLlTUF0qzTCLFRlLMuuYK1G61Kd5rdMBzxu5ycPN9yp35Rt5w-NYqzVbCkCEMjkdKPwBcxD4kPpJBMS8go5LEUJ7jHezOwuvrS7B5Iem0jFwaKFSBoBhp9qfdKk9pZG6-LgiodmeUrmNNXZjbk6cgBiGnFLjgvjpOnqZozHLlT-_wURtbSNzzQQXm-bdRA8VAfr_hbRTiaz_JKb4zRtnY76n_Syx-50sHdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K8ZLJzrsMVNGJena4ua7DJkB0Lv6L-ZM5G7f2uclYic4QkP-oWjqAs9jEQDwtteXgGMQp8ipNbBH9ZSsKfwpsAskkG2WIeuPFtF6e5OF22XsQkE5pePHEGci8838bno5p5Z75weY1emelvHT21z-LA2Lb-bQ-TeLx4peF-XvX7c0dRk1Dtsm1w10RKcacxTc9Z4MY9PgI5jBDxq8Lcz0wdGXnP96elVxl3wMVaePH118yUU3iu5BgMa9xuVfpz70DQ4CUlWEm9alEC4mqOPlm8o7LISoCITY706NV-cHiBNwAUq2YSqgAymr1P55Ib-r9a9HN0L_5WXNJ0MosqP6mg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | سه‌شنبه ۲۷ مرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/farsna/456675" target="_blank">📅 00:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456665">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oNsqZ7XVUU6AzjHzaw1PEihKZcHca24YvTxcZVh9XmK8irLz00DYnKl6ljPje-vW6HjPIAEt61JckQcZ7ZOXcV-KiEYFWLqUYdoN7OlT74cS8J8YirhR0i2UzRdjFIZFP9FsOT4o1sYfe9f_X9hoCeiJH-8_yGHQINrodtiwi5aJVqnljAn12wd2_PgGybh6juRGmtm3zAkNkNKK2qghhBNnCGcBhEZXUaUHlt8_WJmquutqoiju24ZSSL1l-XHDNAtduNoAYSIQLArXRCV6R_fd8y4r2QBpm5RZQ1RYtahbwY-fNDDzmKQw4wgPGTZOzizxfROMMpRC4VqvEL7c4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B0txoe5uP5FM9XQXR1ajKJ8v4_UUCEuvmm0uv-P-ZxeFC4_z4MDcT8ko7u4sbO5ZoTlY55WOUsuI9WdNGLJlRYsqVGPX0CwgnzVCRTxZcNzHRqtxxBu-GhV2NmXrj7qXGug6kWocQQacfkJGIF3bbI-a3QL8JiQd0oBuuc-SrAeIcApzbcRo-0Z5bU0a4d5YtxO_ySa-qFW0TbTO0Vnnz1q2SdveySeycBTyHXVR6f8h23pn-d_tbpmQ_bTNa6xUQMnrdvV1WHN8-WdRKKFYgRcCdYyvni1uoI0t_ue7rOC5m1wni7R-WErnretLOiduzDr7M4Cs73PFCnJlabTDIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FURurWQ4PKesmRap_Fsni_8RS1Xi2b3lA-hryzgNBHB9h8m36OreEUTD6LKwFEcfs8UsUrEZc0HkpGUhgEuhD_i8Vcw6Esjk3iSht38SY_0CaETMHWzbdakMOVL7SC6EAeRs-93D37MNGmrwGEgw9qPgltiLSHHYdp0JhmUl3YlIU8sti-qemFcWtsjGG64-TNBpWkZUXEvttFzh5VVMViuE8HuIPlIvi7tDpIVpxyZGFHa4GQsDpfHP8govqGK0oxGRAy3IpLfY3ghyWtNtmlZDe7JUv1NuMfDlpDyuSQwJcdKeHzICnnER5r7f99aXgN5nTGF8NE4A36NfOK4u2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GxwWLPUOEJeMfUStlBjco8AwZpYsOHDMGKS0zDm915V1ZSC2prQPvm91aqkIjWeO5mYaPoGK-gAhhK2Ox7FNQa67U9L0YHXFK1eQrg9KudahY26na4r1I2xBOkYcZHI3Ew_cwQRuR775k8DZI9IrAMPzscjlugGP9bad8BSN9CmhIYYe4LWOgbbqVMbkGVZ1Muf1lzcjY93bcyFnHLOqywUtoY0AMYVmgL8wEUq2f9GO2DlK1jP1bayUMBqGd1PQuCBRvcQWlnQTj6THaP57lYAYP8DwdNPrRE_h73Xfif5rWwUucX4YQRR40ak3eafa346FkyY9cIihIGWuGA565A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/biIm8pnIgWrAILv98h_1QEIavbzxPwZ_8LJQPf5oF2RR6I2C4rjcYfElbTBrgHHdhBy0nig48t7eHAwLnDuIETzzjqo_bf36ZmPXqxZQjxlkUKois1B9eAx7-J5_0OfE1vSKZF42QUoNAS-zbK90Cazoeiv4F9uO2gvfe1LBDb7DByRFS3iv3aZU4ZfZq7MHI493IScD0KjPLVBGxso0R7tqVjHYloMXV36eoDttFAOuGls2YPt0UjkHMNrJPvRItuLPvM3NjA-uU4KpO5pgllYgvWVjLFaN8vKD1117kehgI61Y4Z0QKwgNcniJBNFdxqYxlEf-Fc1nqhSUEd7Jtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B6uiE0kstXYCVNYxEIGjyZG5vqeQ9Ymr-xOlTzFm59ZN-g7dvsM-IkpfECxmKuZkFiatr-WitOpRioExxQufcF8Vn0XCdxPM_ExInEJAAKPZKaTZbwOOsJLecfbFfqZgg6gDGqWtcN_-VfBls4HmqocxyrO1i_xwMlorj6FW7ZZ_9NmwrSdZxTFr5Vpq9HSls1dlm5EZp4xgnNpwbV4d4nxXgUbTAdnmkFUaikXh6K_xX8yj7TmxowboETg-etdvfozWJ7jwd_Tc0eUtB1n659kgIVsoSo4Zp7gpnMZUzLwu0rs_1p-GevBh0iIEGOalz_ilnaAlJTYG8iAGSUAdCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cTeXflu3BX8b5XuE6JwE9safTOeGE83GkC9LDLPQBf0PtVe-DxCyXyhlF80bOGgKhtN6v2-RcYcn-5VS7PfNgp8b6dO6ETwvE4ybWw1Z9PH4XoH9llOYxG0Ue5VUwMDa71QnR4Vlxw3gijpfzbaz1aJovyRUL_jVqyRAoUva2IevUlPRnXNuQdRZuVXoxOS-fHIita_992z598l4WJ91n-_5WJvVMwmxkh4WKfiGgrJw8Q4fPKY-aRar-dZkz65D5vvLgEw7V4FQhCEeAvSDaKDvkzi0hEZP4S_aDXihchDwWpWrlge9KUgzEH8DBSj5Zqzgy6kjU0X0sVhBtTcA_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RDB9guajub_A-WqYKz3mUnmO5SsTBWeqyksbtPVzkCGF62CIcADow1HKBLtMgJ5gyHvCDigvbHdVXENd5oFsJ-QqcDyaQDL0oE_nt8QbptNPX9_bVkZA89cyQv3EEmWv1cCxBS0y47yspchn39UXNMAH0v69I7qgSEJ6GMzJnpdHe5cCYsyVRrOTGme24MagBD_mW_EvjztI3rKsirW_G-9iiWsoJVldIclQm4QZtd_rSlC7D6Fe05WfsGzwyeaCXGVdfdf2Xdw2bK28G2-YH2R-4mV-P16gYatSgLLRuZxePXHBaVbXd4hErX5Db8ytQTPylIl_xVOmPy1qoiITlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ijT4k8cnhVlAMRlM4XH-fW1c5psP6ui-2cbj2mMHGw1YmMcjSpLGXk8HKRCMSCe_ROs65hTThxRSK4gVyjmW78mJKIUPvX0LVR_dRXqweyZyeGrSTWf0-hfZjRxC9agtB0SI2q6O_PbdpfdO2JUUJyI-xGWrpsyhtpT2B9oEkjB4wSzZzdVCrwaa4YiG1s8I4RDCc6QhV08FO_As6BVEsW_I3nNKwYu06HwWnMT6-XztrGlr2FfIy1dRPXfxQ4jn8owngyMci6HZmnWHHovY5Dn-wCpA8Vb5Qj_iEzoeIvNwSO_KvbYw-9Xhn-u-lt6yXMUAhXFcwm8k4FcraRDN6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/inVBO7iTgwOEoT7p5SN0diWltfJ7FxnTcrr6ytlbGjXfiPw03uSaTJryUsVKut78BFZ8nmwysZDE40lEbuTO9HkYPPZxUOzhB9ow_m3rv9J9QVot4Hj8dVge5Ay3P9DZY29yjHkNu1gZbR40DsEvXTps5d8ztqPwaNIZTPDr2-BQjfhQ3Wt-g0lzeHznRU6IJPtijsAOVvVamm4pIfIjq9mhxeeoODaTA3QiqqVdqi29lrs3ises7hacMhoSTczo_Cl4OLBnen-t0WSeq1atHg_LkmPn8LsURedUcwTg-xdGj1b4ct4ve_qXwDLneHw_xlbTCCevHhsC7OIlFixRQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/farsna/456665" target="_blank">📅 00:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456664">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">حق انتخاب میزبان آسیایی از استقلال گرفته شد
🔹
کنفدراسیون فوتبال آسیا اعلام کرد که مهلت باشگاه استقلال برای معرفی ورزشگاه میزبانی در رقابت‌های لیگ نخبگان آسیا به پایان رسیده و AFC تکلیف استادیوم میزبان مسابقات آبی‌پوشان را روشن خواهد کرد.
🔹
باشگاه استقلال در نظر داشت ورزشگاه بصره را به عنوان میزبان رقابت‌های خود معرفی کند و انتخاب گزینۀ ازبکستان را نیز در صورت منتقی شدن عراق، در دستور کار قرار داده بود. با این حال نه فدراسیون عراق و نه ازبکستان تایید نهایی لازم برای میزبانی استقلال را در مهلت مقرر ندادند.
🔹
گفتنی است تراکتور، کشور عمان و گل‌گهر، تاجیکستان را به عنوان کشور ثالث برای میزبانی مسابقات آسیایی خود معرفی کرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/farsna/456664" target="_blank">📅 00:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456663">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c87ecf94de.mp4?token=FBgzMVKb_HMB4NyR5TeLtlfpPZu-5HPnoInzropynSO33CFbDf_kHeN2ayhAQAVOsEIZCx1EtHJlTAL-rykJlQQ0ld541j1oOXZW4Pw3vQabRsmySdWRsGeFEksmk9RelHk8uXIxNRTA63_JQ8rx8r1Qd4lHtwWgZkWV1_A7MvvRA4pLoPE9ZO1eSHmmjduD-bwmR4OGuLxX9dtmr8XgWGPkop1dv2lp6FkZUU-H3S2e9YOgyWKEEHGHa4ZY0PZI3pATK7EE3s3SqgwbfKlPMyMYKSxz0ccpA85KJMiVcsrs7BsdaIyhxtlz0y4QfjY571GtEr2cyAeyzWoGt1n26BZZ2LarorqP2CXj6dYc5hjf49n1-xOcz76zj92DiaGl4e9KoNmlvlmKq6UvALGi28ypSVQ57vlMD6UkmV_EHZNOSxpqtL1oBOKmXEpudVlTP6P2Ow9Z92QUAopjgyLsMa9zH6d41VvE8HKGQ-LRXZOl47kMacQihtC2qmTNYIrZvHXplptCGdh9S-KjTkLv-JvU6ObWHZSO1zkiqcrmFc3b1LHp_q4QO0gx1Qde2i2iW-ieabfhBwZmC9Pd3l6pTXslET7L8XeaiX6oTRWmZWkRV3ezQCm25fQ1ZC5wy0WB2pMDb3ujfMlKre2t4Kd2LlbwByrSI9x9P4zt46EFCjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c87ecf94de.mp4?token=FBgzMVKb_HMB4NyR5TeLtlfpPZu-5HPnoInzropynSO33CFbDf_kHeN2ayhAQAVOsEIZCx1EtHJlTAL-rykJlQQ0ld541j1oOXZW4Pw3vQabRsmySdWRsGeFEksmk9RelHk8uXIxNRTA63_JQ8rx8r1Qd4lHtwWgZkWV1_A7MvvRA4pLoPE9ZO1eSHmmjduD-bwmR4OGuLxX9dtmr8XgWGPkop1dv2lp6FkZUU-H3S2e9YOgyWKEEHGHa4ZY0PZI3pATK7EE3s3SqgwbfKlPMyMYKSxz0ccpA85KJMiVcsrs7BsdaIyhxtlz0y4QfjY571GtEr2cyAeyzWoGt1n26BZZ2LarorqP2CXj6dYc5hjf49n1-xOcz76zj92DiaGl4e9KoNmlvlmKq6UvALGi28ypSVQ57vlMD6UkmV_EHZNOSxpqtL1oBOKmXEpudVlTP6P2Ow9Z92QUAopjgyLsMa9zH6d41VvE8HKGQ-LRXZOl47kMacQihtC2qmTNYIrZvHXplptCGdh9S-KjTkLv-JvU6ObWHZSO1zkiqcrmFc3b1LHp_q4QO0gx1Qde2i2iW-ieabfhBwZmC9Pd3l6pTXslET7L8XeaiX6oTRWmZWkRV3ezQCm25fQ1ZC5wy0WB2pMDb3ujfMlKre2t4Kd2LlbwByrSI9x9P4zt46EFCjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ تشکیل پروندهٔ قضایی برای آتش‌سوزی مغازه‌های میدان شهرداری گرگان
🔹
رئیس دادگستری گلستان: طبق بررسی‌های اولیه، علت احتمالی آتش‌سوزی در مغازه‌های قدیمی اطراف میدان شهرداری، اتصالات برق است.
🔹
با تشکیل پروندهٔ قضایی، علت دقیق آتش‌سوزی و مسئولیت احتمالی افراد…</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/farsna/456663" target="_blank">📅 00:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456662">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4504351748.mp4?token=D7ndEpQUF6KsUSwEv1KY2mBaBuitnWz0HLHR1V1j_eZoGuIJSHXya8jCoit3vhl5yUIwuuHLPXf-Pe9M0JMekeTimG8Xsw0xWhG5sdt4_MN7tdqbDVj2WbGZYKEkxWuGT8exnl2VWiGp_Alu6mm6xDu3_t4f6HPr24ui2TizqnxZ2J_z99Hm2mA6PcaObK6wK9_RGCoGiDmibjI0PkolH4WAW1G1shKNPB1cpwDxEqbhVgVDaqf1bAzHgjBpyapvf1l4W80mxHiTXY-6gKqYcTDLdUOoPeYbwQq45QfnFqlzOgjiDjE96qchJyq4a7Yddw-xzlObcGDeS1wMjjvp-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4504351748.mp4?token=D7ndEpQUF6KsUSwEv1KY2mBaBuitnWz0HLHR1V1j_eZoGuIJSHXya8jCoit3vhl5yUIwuuHLPXf-Pe9M0JMekeTimG8Xsw0xWhG5sdt4_MN7tdqbDVj2WbGZYKEkxWuGT8exnl2VWiGp_Alu6mm6xDu3_t4f6HPr24ui2TizqnxZ2J_z99Hm2mA6PcaObK6wK9_RGCoGiDmibjI0PkolH4WAW1G1shKNPB1cpwDxEqbhVgVDaqf1bAzHgjBpyapvf1l4W80mxHiTXY-6gKqYcTDLdUOoPeYbwQq45QfnFqlzOgjiDjE96qchJyq4a7Yddw-xzlObcGDeS1wMjjvp-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم دامغان: خیابان به خیابان می‌مانیم کف میدان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/farsna/456662" target="_blank">📅 23:53 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456661">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c893b286e.mp4?token=iyKWoWpLVMd_YJXi6r240QBw9b_Vi7i5EjJL8fEkhV31nQWTnvlPS0TSuL5jX4qAQuWUvW3acyB_XIgRfe72Dr8paloVB0CNj8dwCgTo0532dqZCltWmtc8hd1USLEDmg1hlBUW8q03gvcE-2rL40pOmZC1tfr3pqteYOl6J7RwZenLJ7FP-XyF_p1UXN0Rx4hYJz6sIb8Mz005SgaVpvLywplm-vaS4VY7_2IqvQXhvTgMI6YNhoFd96adk-vk6aGNMZlbXAFDYnX49WQyBS7SstbtIJSn_MQkYg_5XAsWeEhbNbKkOBXBOcfHo6cshaDJHMOlKou044J2YzwLUig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c893b286e.mp4?token=iyKWoWpLVMd_YJXi6r240QBw9b_Vi7i5EjJL8fEkhV31nQWTnvlPS0TSuL5jX4qAQuWUvW3acyB_XIgRfe72Dr8paloVB0CNj8dwCgTo0532dqZCltWmtc8hd1USLEDmg1hlBUW8q03gvcE-2rL40pOmZC1tfr3pqteYOl6J7RwZenLJ7FP-XyF_p1UXN0Rx4hYJz6sIb8Mz005SgaVpvLywplm-vaS4VY7_2IqvQXhvTgMI6YNhoFd96adk-vk6aGNMZlbXAFDYnX49WQyBS7SstbtIJSn_MQkYg_5XAsWeEhbNbKkOBXBOcfHo6cshaDJHMOlKou044J2YzwLUig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین یکتا: ما خون‌خواه آقای شهید هستیم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/farsna/456661" target="_blank">📅 23:48 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456659">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWrBzfwxPQ8Zzyax7u1SyjD_zoyLfpDYmhpnZQCforubkw_4w-Ht3UOseZYk9yZUpLbQxb4cZQwrs6cG3k6BvIEdpTlixs-B_6d6g1vVXOK47d0eAOtW4obJ7gktHg-0gk2Tlix1VFVBu6xuBO5d5dGc8tecPqaJM-LJf3ThOF7MsUWHbFeBCSgenKKTmESjhQyHWpAN9JNFrqBn42br6p76U10vu9isZYN0Qn1XqjeitiqtDb4heGYV11pKCRfVpUqEG1BtkqFLsEWpXw2SvHoK-ZnfOF1njrwIknNR1G-VrYbCAMXzyGCq-0bI1X9M54wuq6KaQHVgYTV8t78fOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b26d336c1.mp4?token=WvQ5kgtdVVFJz1PX98Brr7E_Y3G5kVepsyjUNVYZ1X9jiLSO9s7kZ5HwyWwmLXWt3Tm1Dp__Xi9W6u5ciH-iqr3qDPsoPtEqVYt8gv8xa6wB1upKdMf0bFhmSziHFe5pJj6Eca3Dh0x9NFyO-4QHYwgVK47Cw_KaRx_XqIxdCQrqB4cbbo7dsTjLLZYWhhBWAxX4Z6o9eAAcrT1r7hRGtvvVYxx8qQb-7FjgW2ppQq8g9IZcJsmmSPpHo-LeHrN5uy-W5MgrVS9FhLqgZAzECiteSFtehzMqpzxZiAw1kEI5qJBHYvlB9QKUfCc1iQidvhTdQWCS8cyeJy_CbvRogQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b26d336c1.mp4?token=WvQ5kgtdVVFJz1PX98Brr7E_Y3G5kVepsyjUNVYZ1X9jiLSO9s7kZ5HwyWwmLXWt3Tm1Dp__Xi9W6u5ciH-iqr3qDPsoPtEqVYt8gv8xa6wB1upKdMf0bFhmSziHFe5pJj6Eca3Dh0x9NFyO-4QHYwgVK47Cw_KaRx_XqIxdCQrqB4cbbo7dsTjLLZYWhhBWAxX4Z6o9eAAcrT1r7hRGtvvVYxx8qQb-7FjgW2ppQq8g9IZcJsmmSPpHo-LeHrN5uy-W5MgrVS9FhLqgZAzECiteSFtehzMqpzxZiAw1kEI5qJBHYvlB9QKUfCc1iQidvhTdQWCS8cyeJy_CbvRogQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رونمایی از دست‌خط رهبر شهید بر صفحۀ اول قرآنی که هدیه داده بود
@Farsna</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/farsna/456659" target="_blank">📅 23:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456658">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bc3fd79f9.mp4?token=HQ0eo6wcWco5q0aO0wFN5vJTkEP3-K4N2zPGp5Luo0RPlLHUzwGMLTX-55iu2B4BjvoAAgaRQ6T9hWVKlv1ihuG_iQk3rkwNjYsKsCdYHzqa7KFcMcsmt5BSdzluDoaG2vxTsV81azWddmFgf47DXpfKgU_UQFey_KxqngMW99Z_ZVcd7EU4FsXiSem7XSgZ5Kj7Yld7TfkeWU96I5BMVUKvUYFd6iVLD7NdaVaZHuXF98_UQ-geD9WaZfBQnqbUeqC_AmISrvZ3S-rm5734H6hALjszoEhl74yG4CbMHxdkvPNvK9EJTWB9sSQ2VkoqUGAvRzJ7mf18Uzl4K3bEXjRTgobk8_32MOt30xt8x3Ufe_RdENr3g3bLMlXP6G-cHJRNosvW3KkzAzV1YRz1M215wffWhLwqdlmvjznieitbiPQZ4OQKPINrKzyYOsIUvWaurt9RCRqnNzgTwyRBF3S65piF-PCXGIvJOMbtAiWzcznyKKT6Ysp3Hb-3IobfrhsxU3_qwX21nvr7IT_cpWHLOtfeksZvQmxPKqykfaQ-d3sLD4IElzBMNy-lo21pKe4E3eKCXyV_qDJ4nkAUGpTqNjWrV0J0JKh7_2gKIFsa5usW5Tb4ipkupwL5t456ngb6GuDY6QGY_uZgzsEYPNZMUY02PXDlDDFepxRxIl0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bc3fd79f9.mp4?token=HQ0eo6wcWco5q0aO0wFN5vJTkEP3-K4N2zPGp5Luo0RPlLHUzwGMLTX-55iu2B4BjvoAAgaRQ6T9hWVKlv1ihuG_iQk3rkwNjYsKsCdYHzqa7KFcMcsmt5BSdzluDoaG2vxTsV81azWddmFgf47DXpfKgU_UQFey_KxqngMW99Z_ZVcd7EU4FsXiSem7XSgZ5Kj7Yld7TfkeWU96I5BMVUKvUYFd6iVLD7NdaVaZHuXF98_UQ-geD9WaZfBQnqbUeqC_AmISrvZ3S-rm5734H6hALjszoEhl74yG4CbMHxdkvPNvK9EJTWB9sSQ2VkoqUGAvRzJ7mf18Uzl4K3bEXjRTgobk8_32MOt30xt8x3Ufe_RdENr3g3bLMlXP6G-cHJRNosvW3KkzAzV1YRz1M215wffWhLwqdlmvjznieitbiPQZ4OQKPINrKzyYOsIUvWaurt9RCRqnNzgTwyRBF3S65piF-PCXGIvJOMbtAiWzcznyKKT6Ysp3Hb-3IobfrhsxU3_qwX21nvr7IT_cpWHLOtfeksZvQmxPKqykfaQ-d3sLD4IElzBMNy-lo21pKe4E3eKCXyV_qDJ4nkAUGpTqNjWrV0J0JKh7_2gKIFsa5usW5Tb4ipkupwL5t456ngb6GuDY6QGY_uZgzsEYPNZMUY02PXDlDDFepxRxIl0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
#فیلم
|
ماجرای خادم امام رضا(ع) شدن عباس جدیدی با عنایت رهبر شهید انقلاب
@rahbari_plus</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/farsna/456658" target="_blank">📅 23:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456657">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🎥
کاشمری‌ها در ۱۷۰ شب ایستادگی، همچنان پای کار ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farsna/456657" target="_blank">📅 23:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456656">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e524f8bac.mp4?token=hsvAq7OdPgHAKV-6jZ2nL8tnLmlzAE8AipFyyOE8vuDfJAnmZjoW1BUcDKA4ZYjx058E8l5DdfUZjZ9cetrKnc4Hq2jgYT7Foyj9PVJmXmob9VsaJEeQIB_f_k9qShB-Q4waJ4np3WgwzI4hlaGloppxY3WiwvP34N4jKUlMztQYzIVV1_nfhsIwa5W563wTRPhKKKlQMfLPcLQws1HBCKqzwX3LBK9n5wg2DLJVE4hA-n-38E2sz_kEjkq1PtRSMYsIlPCdhNm-BC-5sGtOV7hKnP_viVr_lm7cKybiL55lyUif2hblh5l2Tnthr7_seWFPvXAVlmaM4zjOSkf9Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e524f8bac.mp4?token=hsvAq7OdPgHAKV-6jZ2nL8tnLmlzAE8AipFyyOE8vuDfJAnmZjoW1BUcDKA4ZYjx058E8l5DdfUZjZ9cetrKnc4Hq2jgYT7Foyj9PVJmXmob9VsaJEeQIB_f_k9qShB-Q4waJ4np3WgwzI4hlaGloppxY3WiwvP34N4jKUlMztQYzIVV1_nfhsIwa5W563wTRPhKKKlQMfLPcLQws1HBCKqzwX3LBK9n5wg2DLJVE4hA-n-38E2sz_kEjkq1PtRSMYsIlPCdhNm-BC-5sGtOV7hKnP_viVr_lm7cKybiL55lyUif2hblh5l2Tnthr7_seWFPvXAVlmaM4zjOSkf9Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای این روزهای بازار ماهی‌فروشان بندرعباس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/farsna/456656" target="_blank">📅 23:27 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456654">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06507043fc.mp4?token=uwKM3az9r46sNZPUoveVX56sM51oLG1kM4lAZMMYkGJdCi-DjTn1wftTylM9sNruZE1fonGaJ1-PfKZ-a1TR5iycfkc1uJRNf7qA7IIDbEFKvoPLs-gnpTsItwWXaullYy1P1lIXp9NMcgbAhL0vfgXqfQxR9CTKY2vw5Sv8lIyu6AvdDOztKHTlVZOn0SZ2qGwrMpV3j40F6N_lDH7by8UAjGGx16yImhdUysJ--a_eKNrxjeH1hdhsOgbe5r9qZwGr2hhJKdFP7UGfeDLm7lBP37dpr6IZMhuwWWJi8eJRhS7XgpSfhmuiL10WZyeNP1llnyFpX1-88XwsTmkvPXwFmn4RQ7qUZ925oz7kOoZBWlRJ8vwSFxlf3AFaTMXFYL_jIFmUrMAn-mgPamSmfkSaBs_ImUtcNPMDQaJBCYuQeoH7bUOkZjW24Tj4QW0tUrOvnM3SmdUupQYOsiKgY0Ix7bmViZWiQtiux1QdzRYZ8yQWgFkljFzE_e6n2A5YhILM9JPKRyNVg_RWCukCmBJTxXQrY5s6IHu_a_gUAF1Rqnfo-98yYejhvZOFJ0EyCYNB3yFjERt-O0T8ZF_Asj44lFaEQK-QxytrvWPgadPU8ee4IxUx5flGUaVfPw1iV_4U17yiBpBkOX8bDrLYiArbDJCw7Ikum0tekeJa3aU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06507043fc.mp4?token=uwKM3az9r46sNZPUoveVX56sM51oLG1kM4lAZMMYkGJdCi-DjTn1wftTylM9sNruZE1fonGaJ1-PfKZ-a1TR5iycfkc1uJRNf7qA7IIDbEFKvoPLs-gnpTsItwWXaullYy1P1lIXp9NMcgbAhL0vfgXqfQxR9CTKY2vw5Sv8lIyu6AvdDOztKHTlVZOn0SZ2qGwrMpV3j40F6N_lDH7by8UAjGGx16yImhdUysJ--a_eKNrxjeH1hdhsOgbe5r9qZwGr2hhJKdFP7UGfeDLm7lBP37dpr6IZMhuwWWJi8eJRhS7XgpSfhmuiL10WZyeNP1llnyFpX1-88XwsTmkvPXwFmn4RQ7qUZ925oz7kOoZBWlRJ8vwSFxlf3AFaTMXFYL_jIFmUrMAn-mgPamSmfkSaBs_ImUtcNPMDQaJBCYuQeoH7bUOkZjW24Tj4QW0tUrOvnM3SmdUupQYOsiKgY0Ix7bmViZWiQtiux1QdzRYZ8yQWgFkljFzE_e6n2A5YhILM9JPKRyNVg_RWCukCmBJTxXQrY5s6IHu_a_gUAF1Rqnfo-98yYejhvZOFJ0EyCYNB3yFjERt-O0T8ZF_Asj44lFaEQK-QxytrvWPgadPU8ee4IxUx5flGUaVfPw1iV_4U17yiBpBkOX8bDrLYiArbDJCw7Ikum0tekeJa3aU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیات شنیدنی از هدف قرارگرفتن یک پهپاد MQ1 و ۲ پهپاد MQ9 در عملیات نجات خلبان آمریکایی   @Farsna</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/farsna/456654" target="_blank">📅 23:23 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456652">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71102e9aa6.mp4?token=pPETTkw2_-V1otVS-V6APV1tXanRkhE3NeiXGOtP3h7dODtupsnPW8_npJXuiJ9znSOAwIak39U_dUUKvTSLwlIbwlmjqSTV7kZai8bfdIeenZVFVE2uCR6iUfT1oa1CnvSg3ppfab-do8XCj8PO8lPIQeJGVOS_uZBtICrjyY4Lvxdn3zJhyWFGhwHaozd-qjy5WMsJV4CSolvp1KwNlI9qR6rg0Rci7Wh2B1dMN0MKk5XY4OWyhWtfrjgJGvC4OXtLBT4dio1uH6xhDvCd85-1KF5AcJTIahoN6bH65UflEwCnyXCeKyUy_99HCoZwq9N63rPCQSB8s9s4ZP3zFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71102e9aa6.mp4?token=pPETTkw2_-V1otVS-V6APV1tXanRkhE3NeiXGOtP3h7dODtupsnPW8_npJXuiJ9znSOAwIak39U_dUUKvTSLwlIbwlmjqSTV7kZai8bfdIeenZVFVE2uCR6iUfT1oa1CnvSg3ppfab-do8XCj8PO8lPIQeJGVOS_uZBtICrjyY4Lvxdn3zJhyWFGhwHaozd-qjy5WMsJV4CSolvp1KwNlI9qR6rg0Rci7Wh2B1dMN0MKk5XY4OWyhWtfrjgJGvC4OXtLBT4dio1uH6xhDvCd85-1KF5AcJTIahoN6bH65UflEwCnyXCeKyUy_99HCoZwq9N63rPCQSB8s9s4ZP3zFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر نزدیک از لاشه‌های موشک آمریکایی تاماهاوک
🔸
جزئیات شنیدنی از نحوه هدف قرار گرفتن موشک‌ها در آسمان ایران از زبان کارشناس پدافند هوایی سپاه پاسداران @Farsna</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/456652" target="_blank">📅 23:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456651">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48608c55e0.mp4?token=THCuzfczW1kF_T0P988xPV5IZufljtUwWJvzHeC9yUzntWQVr2j2zx2yUKWMfBbaRekp44m19DdB8BAOO0VTo7O_5ZOE4tBQIe6mucvto0x9dptuMRYcTEmorz3J7AVE8txIDyNcbIGAVuoXZ32hu4gWpNHU91Hv61ISThUHt6NlH_qNt4e5rVRmMVrsp8wgHrdjkQlDSY-v5sO2EWTMVcloqaz-I1yUrGfUG3EY59QJUVFCCtrs7d9Jo6wsDreLTBHKQx20kecTvPSLvsagd6Lw8pCkEPgEQDHoDxsFOVuWsLNImXB7jA4wE3tWCXcabd_Au8Nr0ocrw8NgFFdJBGmapW1OQlnYtf45J6vf7IeOrJc4gXvND5eCcPubJgGpYBpisYoB5oUcEjQza-H_e8tj36zLa2bQ9ZnsVorU9MUiv-v558k-Pzr_zZVYZvYSpm3_8_oLjFQszdos9uMofoziDRAOM7SWyH2TYwd0aIIctE-7T5gymnHANXeagvEcfqzdiJjH4K6xz3Gh9UaLeQdwk56nEfaTEKQRYAWzSZX15oI243nWw1MpofMESNJp8eUCOoo7Xpg7RgE1MFx3zOe7As8OpDM87wKM4EiKo4MSS34Ek7e5H6SmK0BY1vxBAr5cF82nxc6LSM4kFCvO8D36g0uaMEsTiz57msOFh-o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48608c55e0.mp4?token=THCuzfczW1kF_T0P988xPV5IZufljtUwWJvzHeC9yUzntWQVr2j2zx2yUKWMfBbaRekp44m19DdB8BAOO0VTo7O_5ZOE4tBQIe6mucvto0x9dptuMRYcTEmorz3J7AVE8txIDyNcbIGAVuoXZ32hu4gWpNHU91Hv61ISThUHt6NlH_qNt4e5rVRmMVrsp8wgHrdjkQlDSY-v5sO2EWTMVcloqaz-I1yUrGfUG3EY59QJUVFCCtrs7d9Jo6wsDreLTBHKQx20kecTvPSLvsagd6Lw8pCkEPgEQDHoDxsFOVuWsLNImXB7jA4wE3tWCXcabd_Au8Nr0ocrw8NgFFdJBGmapW1OQlnYtf45J6vf7IeOrJc4gXvND5eCcPubJgGpYBpisYoB5oUcEjQza-H_e8tj36zLa2bQ9ZnsVorU9MUiv-v558k-Pzr_zZVYZvYSpm3_8_oLjFQszdos9uMofoziDRAOM7SWyH2TYwd0aIIctE-7T5gymnHANXeagvEcfqzdiJjH4K6xz3Gh9UaLeQdwk56nEfaTEKQRYAWzSZX15oI243nWw1MpofMESNJp8eUCOoo7Xpg7RgE1MFx3zOe7As8OpDM87wKM4EiKo4MSS34Ek7e5H6SmK0BY1vxBAr5cF82nxc6LSM4kFCvO8D36g0uaMEsTiz57msOFh-o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بروجردی‌ها و حماسهٔ ۱۷۰ شب حضور در خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/farsna/456651" target="_blank">📅 23:08 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456650">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aad7677a8.mp4?token=AZYMqNC091DXIX9_qjQUIanB-dJB0A8IH2gxvobxHXzWRFA3c-dwDy1gcOgvYYoWzgCDKN6vfQS-erwgRoH-i-vXGsfEJWyXp8aIoD4_-CmMXTyjgI9SYVZctmcAmgtgjy_Bs1lgruPpOOQ6JLqithnNwm93M9itsuUS6oD07JfiwWGmyX-lw8AUKrW9UaP_vx0mBTL0Z2Pn3D9PMfaFaod2T_IydinyW2gpYQYRLXUqwD3l0PiX-1FDPng9gEP8fwo9bIVkPuUF8MJm0DljoNwYcquxltqk6AAAoiz-2xEFoDMsHENH5GzkeRsa8UKzv-C-ZeXbmboPvKF7X6ZLQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aad7677a8.mp4?token=AZYMqNC091DXIX9_qjQUIanB-dJB0A8IH2gxvobxHXzWRFA3c-dwDy1gcOgvYYoWzgCDKN6vfQS-erwgRoH-i-vXGsfEJWyXp8aIoD4_-CmMXTyjgI9SYVZctmcAmgtgjy_Bs1lgruPpOOQ6JLqithnNwm93M9itsuUS6oD07JfiwWGmyX-lw8AUKrW9UaP_vx0mBTL0Z2Pn3D9PMfaFaod2T_IydinyW2gpYQYRLXUqwD3l0PiX-1FDPng9gEP8fwo9bIVkPuUF8MJm0DljoNwYcquxltqk6AAAoiz-2xEFoDMsHENH5GzkeRsa8UKzv-C-ZeXbmboPvKF7X6ZLQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: کره‌جنوبی گفت که برای مقابله با ایران به آمریکا کمک نمی‌کند
🔹
وقتی با رئیس‌جمهور کره‌جنوبی تماس گرفتم به او گفتم: «آیا تمایل دارید در رابطه با ایران کمکی به ما بکنید؟» او گفت: «نه، متشکرم.»
🔹
من گفتم: «یک لحظه صبر کن. ما ۳۹ هزار سرباز در آنجا داریم…</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/456650" target="_blank">📅 23:04 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456649">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93f49232e6.mp4?token=dV8Au2DcWQ34CgcUwkxK9XpuCB6ZF8dvC6evj6INDNQALiRahAMeSEjusFyjI5DQiopkpKPNOw8enkcK73lco3k1LwNUcWGIjSEHufnUvzCnphPXm8lO0Ha1FY8JbqfuI0jdpn-i_87KUEgZ8_Y5H0Egbz0XyS5zgDC_1R7VDza4DYCI-WG6o7pC4QVTM7Y_DPMr1KqajKDpES63IzF_EM34GQLVleJZy4TdZXXu7k05JauhGJKB3k4dQAX4ULd5PSYvFSw3v-0FT_b6idqoGh0JRmVC6-Z1rsfu-0V2ZlTb2yQkQsAhB0V_F9JonfFxNZ37wW4afKjmoUvXYyh3Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93f49232e6.mp4?token=dV8Au2DcWQ34CgcUwkxK9XpuCB6ZF8dvC6evj6INDNQALiRahAMeSEjusFyjI5DQiopkpKPNOw8enkcK73lco3k1LwNUcWGIjSEHufnUvzCnphPXm8lO0Ha1FY8JbqfuI0jdpn-i_87KUEgZ8_Y5H0Egbz0XyS5zgDC_1R7VDza4DYCI-WG6o7pC4QVTM7Y_DPMr1KqajKDpES63IzF_EM34GQLVleJZy4TdZXXu7k05JauhGJKB3k4dQAX4ULd5PSYvFSw3v-0FT_b6idqoGh0JRmVC6-Z1rsfu-0V2ZlTb2yQkQsAhB0V_F9JonfFxNZ37wW4afKjmoUvXYyh3Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم چهارمحال‌و‌بختیاری: به کوری چشم ترامپ؛ در خیابان می‌مانیم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/456649" target="_blank">📅 22:59 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456648">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89ac0b8d5f.mp4?token=g4BgSvTFNGw-ZGx9_h7oOWF8Xw8tMQukx_t45_n_TNTBvGL1vcfI_68K_AMb8-Zt-8fpAArTvnNJFKJDpMoM0IkyTKrcUGkO600qaaFtYPeeUt1P6f6QpytXi1E4j8mt6Rr7qQkZiEd3BhouuJFC3vzcB6hcCZ_AhuGCk3HL3C5EAviFFezTv71aK0x2QTCEi99F9-vn8QEV8YZdvWkLzPgYjOMxtOdGhvPWYmha_HRnu1EYExNf6O06Y9wRJ9vJuQWEENp5kllQKDqt9pGaHBfwP7ft3lmWvUYoMemNm-PtTyBLUcXSazJZBemLBb0Y8rMIyKagQDWYUpZDgsstq09RQzOTYdRqbTfupphjW1nk_aloFYyfq8rteiZeXaWS-VhAzKxXcAgTwNlVW7t50rklv0jcSQ2ZMZGiRQfm4CGmDeHNcCZ7HwgeudmMzG5bfesZ_11FGnf_iA5x2niJpx2Ny4gNP90EuoWrngfvSbhHU9-nZy43M5sdDTnNyMyfeoTY8anC5PiSGouX4WiYKJcOOfWMnxxN6_7lNMsRIO4CKgCczSmLefdI22U34fh41E8uRD1oS4cw7ECHzgsoXF_NkWkESWM1qPYfrV6qqcYOH7aOds08ngx70BIl7WZ-fF0dFxc3dKZNtzR-oitMw13I5ZLoQPNrkIsGHNwRJqk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89ac0b8d5f.mp4?token=g4BgSvTFNGw-ZGx9_h7oOWF8Xw8tMQukx_t45_n_TNTBvGL1vcfI_68K_AMb8-Zt-8fpAArTvnNJFKJDpMoM0IkyTKrcUGkO600qaaFtYPeeUt1P6f6QpytXi1E4j8mt6Rr7qQkZiEd3BhouuJFC3vzcB6hcCZ_AhuGCk3HL3C5EAviFFezTv71aK0x2QTCEi99F9-vn8QEV8YZdvWkLzPgYjOMxtOdGhvPWYmha_HRnu1EYExNf6O06Y9wRJ9vJuQWEENp5kllQKDqt9pGaHBfwP7ft3lmWvUYoMemNm-PtTyBLUcXSazJZBemLBb0Y8rMIyKagQDWYUpZDgsstq09RQzOTYdRqbTfupphjW1nk_aloFYyfq8rteiZeXaWS-VhAzKxXcAgTwNlVW7t50rklv0jcSQ2ZMZGiRQfm4CGmDeHNcCZ7HwgeudmMzG5bfesZ_11FGnf_iA5x2niJpx2Ny4gNP90EuoWrngfvSbhHU9-nZy43M5sdDTnNyMyfeoTY8anC5PiSGouX4WiYKJcOOfWMnxxN6_7lNMsRIO4CKgCczSmLefdI22U34fh41E8uRD1oS4cw7ECHzgsoXF_NkWkESWM1qPYfrV6qqcYOH7aOds08ngx70BIl7WZ-fF0dFxc3dKZNtzR-oitMw13I5ZLoQPNrkIsGHNwRJqk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
راهپیمایی مردم شاهرود در شب ۱۷۰ بعثت مردم ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/456648" target="_blank">📅 22:49 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456647">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ntfu_7ID0WNfUybLYG3eq_bZaR4fuT8QeCyHeOvKMa_n0jhV4RfPmhJ7JzJBA8wyH_XE1V7fp7mJh0KZ5SJngkfrf4jhRaCYTTlRp7FsDZuyappGLMId9Z1iCeP9RLslce5HWltdz7t7OW0oIQveH4zgZ7YL8nnfpqg6z4Eg-3lzSs5q2A1MYWE_aifu27SWWbgF_248wAAP7zYHy4t8m6s6lSwutOFmmpvZHg71gyFYNKLktxQOvyseFOLNe8YAWJ79EhH0_dQwFRIxjDXRZ4ZbY8aYU7ONUXw0X4uS0QQUh34TwjG7WPFH6Lj7k10eSJwfJV4-s8nDPdyOOVvzjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: صبر و همبستگی کلید ایستادگی در مقابل فشارهای خارجی است
🔹
آن‎چه بر آزادگان ما در سال‌های اسارت گذشت، فقط بخشی از تاریخ جنگ نیست؛ روایت ایستادگی مردانی است که رنج را تحمل کردند اما عزت ایران را وانگذاشتند.
🔹
صبر، همبستگی و امید کلید ایستادگی ایران در مقابل فشار و تهدید‌های روز افزون خارجی است.
@Farsna</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/456647" target="_blank">📅 22:46 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456646">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f019a57166.mp4?token=nvYtxw3euM_3uziT1RfZyPqGHp8YarD1iGq_I0vuUeGxRKXWLyESGNCzbzCAYuoIdZJF6a6bb92412wFp0St4D6hYuZAs7t_Y_28T1wcnpyyAuSYPFW3OjvOriyxqUOTzS-MSujgchzNcuMKNOgY1baz62HRrUatKyua66zZgFKSKM49mSk4SwzOgVYVbL11QUU4rpcvnWcNcMKkPA9_3gvmMjI_w0M4An5vnC9S_cjxDYZL9a_daaO0TF5JjSy5sSsSi518f_Bkdl0LE2dpMS80qE_naXruofOHyFGV4X9mDbl3aH0_Sujg19yCC4rYmhJBTh2mx1jvw4y3K7XtpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f019a57166.mp4?token=nvYtxw3euM_3uziT1RfZyPqGHp8YarD1iGq_I0vuUeGxRKXWLyESGNCzbzCAYuoIdZJF6a6bb92412wFp0St4D6hYuZAs7t_Y_28T1wcnpyyAuSYPFW3OjvOriyxqUOTzS-MSujgchzNcuMKNOgY1baz62HRrUatKyua66zZgFKSKM49mSk4SwzOgVYVbL11QUU4rpcvnWcNcMKkPA9_3gvmMjI_w0M4An5vnC9S_cjxDYZL9a_daaO0TF5JjSy5sSsSi518f_Bkdl0LE2dpMS80qE_naXruofOHyFGV4X9mDbl3aH0_Sujg19yCC4rYmhJBTh2mx1jvw4y3K7XtpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مراسم چهلمین روزِ تدفین رهبر شهید در حرم مطهر رضوی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/farsna/456646" target="_blank">📅 22:38 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456645">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3e8a8752e.mp4?token=jWb_N-WRXqXHmvShcKT1tlgQY5hzgtC1PJkHto_faQpbLoVlcRa2hxCPmzh8QOzNofC9BS_jlnFiAxukn9ThZTIHcQhewv_OIUtg4Houc8QyTZQtYz0q6OxKIUu0VJpEXkwBPmRiiTuHy18KaQEdH4RD_RALo6gkCoGpAY2XOIIKhC851StwzgHlfvMg5FzMkIgFGM9CaA0iCHEndV44p7R9wwHMyPIft-gioKIe5-mOor8Xy_7ZxsRzT5aI2mWHjA0uGueLL-gvTgiKiajlt5HgI-nQK0JG9qhsP9pF1OLKCd_eciNwLe9mq8qd8l3kyHpjMO2LTLa9UOF4op2H5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3e8a8752e.mp4?token=jWb_N-WRXqXHmvShcKT1tlgQY5hzgtC1PJkHto_faQpbLoVlcRa2hxCPmzh8QOzNofC9BS_jlnFiAxukn9ThZTIHcQhewv_OIUtg4Houc8QyTZQtYz0q6OxKIUu0VJpEXkwBPmRiiTuHy18KaQEdH4RD_RALo6gkCoGpAY2XOIIKhC851StwzgHlfvMg5FzMkIgFGM9CaA0iCHEndV44p7R9wwHMyPIft-gioKIe5-mOor8Xy_7ZxsRzT5aI2mWHjA0uGueLL-gvTgiKiajlt5HgI-nQK0JG9qhsP9pF1OLKCd_eciNwLe9mq8qd8l3kyHpjMO2LTLa9UOF4op2H5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صحنه‌های ماندگار از میدان‌داری مردم لارستان فارس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/farsna/456645" target="_blank">📅 22:32 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456644">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8c9a5bb72.mp4?token=UE1JdK2LVlTAqM-HVSDgiw6SUmwMqu23QDMElD4f4adLk9BUd3Uwsh422RCKYPlDYVCyHqPariRQhLl5B9KSyhG377IpG-39V-_xa0fFqwKfSm70CiTYddUVx0rPLV6LuJ1dpP2qToQDgnLtaIIoEcuA1ax3qii1iGAp0-FICMjzTxK9s0LmM-pFi0gdDVvKWogjb1lIoTu096PSKLqRJGx8bBR6lY13GD8zA1SRJrHUq3K_tFxhV6xrJFQLmcirnj9-KC593zbHL_Qqc5tDQCWGSyOKCHMDmyUiY3k5MSNhsI0OFnnR-gMm9zSuxrr_JfvnZig8UiaE19FvRGgeHAqUlSpPvspALGY0Z2djHBTGNcOewUGf5QC5P09S1o5ZBXdZ9PAEeD2dA4sllxPwRnqk87v6Wz23o3DtS8h4CBKodsYt8LCVhwbHVD9iA6_XoFp4WBgu_CekFLYsraXFPH01mDpNpvSUnhDLdsBqGaPm3wBm4RuKpU57HYexDQxhnC5WrFqai7zBp1piMW3-BA2zqm6aXs_iD-gqDMk-CglGZCc58qOd6weUucen_1TAssLQyG4Yso6Wjfj8D-dt42kY1nlrTCrzR29wMvcM6Dvh5gAXdkDJkvzsE0cI08Z-sdWwFKAeFYtOjbC4zTpcX_zfyNYfwaKJ83yq3yaz6I0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8c9a5bb72.mp4?token=UE1JdK2LVlTAqM-HVSDgiw6SUmwMqu23QDMElD4f4adLk9BUd3Uwsh422RCKYPlDYVCyHqPariRQhLl5B9KSyhG377IpG-39V-_xa0fFqwKfSm70CiTYddUVx0rPLV6LuJ1dpP2qToQDgnLtaIIoEcuA1ax3qii1iGAp0-FICMjzTxK9s0LmM-pFi0gdDVvKWogjb1lIoTu096PSKLqRJGx8bBR6lY13GD8zA1SRJrHUq3K_tFxhV6xrJFQLmcirnj9-KC593zbHL_Qqc5tDQCWGSyOKCHMDmyUiY3k5MSNhsI0OFnnR-gMm9zSuxrr_JfvnZig8UiaE19FvRGgeHAqUlSpPvspALGY0Z2djHBTGNcOewUGf5QC5P09S1o5ZBXdZ9PAEeD2dA4sllxPwRnqk87v6Wz23o3DtS8h4CBKodsYt8LCVhwbHVD9iA6_XoFp4WBgu_CekFLYsraXFPH01mDpNpvSUnhDLdsBqGaPm3wBm4RuKpU57HYexDQxhnC5WrFqai7zBp1piMW3-BA2zqm6aXs_iD-gqDMk-CglGZCc58qOd6weUucen_1TAssLQyG4Yso6Wjfj8D-dt42kY1nlrTCrzR29wMvcM6Dvh5gAXdkDJkvzsE0cI08Z-sdWwFKAeFYtOjbC4zTpcX_zfyNYfwaKJ83yq3yaz6I0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: دنبال تمدید تفاهم با ایران نیستیم
🔹
در حالی که مهلت معین‌شده در تفاهم‌نامه ایران و آمریکا برای حصول توافق بر سر موضوعات هسته‌ای امروز به پایان رسید دونالد ترامپ مدعی شد که دولت او به دنبال تمدید آن تفاهم‌نامه نیست.  @FarsNewsInt</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/456644" target="_blank">📅 22:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456643">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIQ9vN5RHXceghHAGGk5GMmEjABTsorQzJv5cPE_Rf5Z_HiitjXxmhEpXC63LZmhwVy491tlgmUxbRFY06C5pENPjGldnCG4hsBp4HyRCq6wknl98CtMvGC_ppZXN7WQNOmQJobAIC6ikjCR4oZKkai4gmBkb5kr8SqteMDAv-bPaagkk7OHrARH5QPDAN2LNAjA86VwwdMcAPynryFcqFpyIKwDQtCwgHOFcclccRzJzesm52UUqOUT1ndwopA0jBQ_VhyXLIRkvdwv882aEhqC_89-AMRpPDn0wY028LfMxZHtFSsX14ccoZX1zbVElAxtZiQV9Z1-FBqfdR3hdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری از رهبر شهید انقلاب درحال قرائت قرآن کریم در کتابخانهٔ شخصی
@Farsna</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/456643" target="_blank">📅 22:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456642">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0160b1947.mp4?token=HZ8I_FIE3T8Nk0-WFtP4cMvK68RBaTPgm0fePFYAS5oDaTL3aB-u4884bO2n9uFcdZnPFXtlrzl2MJTJP3sNQMHucgrPqguzTiGq6VC-6v_b8ZixBEH295FPbPkR4SWEg9v5K09YBcy-LUkly0s4o0W6y7wcEY6MHvZsp7CGLv_g-WD1WyQeTxmLFjQhjwK98oWBQtkQtNQHEVVzImeNg8H9MPxpZqPAkIaC5cWizZhssKrw9d96mdhYUdBmtYT1HRS9Dw7vnL8kQ1bdGJCGTdToIVgvYrAUHvlrhM_jlOQcfCaRIFvBAAOt5IHN95kUmCVb-o6xgEq8cuTEE_60rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0160b1947.mp4?token=HZ8I_FIE3T8Nk0-WFtP4cMvK68RBaTPgm0fePFYAS5oDaTL3aB-u4884bO2n9uFcdZnPFXtlrzl2MJTJP3sNQMHucgrPqguzTiGq6VC-6v_b8ZixBEH295FPbPkR4SWEg9v5K09YBcy-LUkly0s4o0W6y7wcEY6MHvZsp7CGLv_g-WD1WyQeTxmLFjQhjwK98oWBQtkQtNQHEVVzImeNg8H9MPxpZqPAkIaC5cWizZhssKrw9d96mdhYUdBmtYT1HRS9Dw7vnL8kQ1bdGJCGTdToIVgvYrAUHvlrhM_jlOQcfCaRIFvBAAOt5IHN95kUmCVb-o6xgEq8cuTEE_60rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی میدان شهرداری گرگان مهار شد
🔹
تلاش‌ برای لکه گیری، بررسی آتش‌های خرد و بسترهای مستعد برای شعله‌ور شدن ادامه دارد. @Farsna - Link</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farsna/456642" target="_blank">📅 22:13 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456641">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🎥
آتش‌سوزی میدان شهرداری گرگان مهار شد
🔹
تلاش‌ برای لکه گیری، بررسی آتش‌های خرد و بسترهای مستعد برای شعله‌ور شدن ادامه دارد. @Farsna - Link</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/farsna/456641" target="_blank">📅 22:13 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456640">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f614280f10.mp4?token=LP-VpBglrT9VuNs3Ir3woUjoAIwwfWM_dfTLn2UGeZUjf0iQK0U4h47pNRHv3I-ObjtxmJdQbBk_g0udH7aFqKLEmvPr1R4JHjNsmuZYMysXOjIQcKlTwFMffBbpXntJRI5tXaGG-2OewELZKKpN6iAdxOu6dFF8a672tDq3uGKQ63_xjA6gl4MZFemOCgZvRVwBPAwxpvBwD72C1KcXQrP4Jwv-Ji0bIy1OhO2EBRXGWxtx1CekKzBnULos3yBQqi0odbtYWW09ghRg0sAUQFPkJCrjgwVYhOWAkWcO87E04G4nxhiu6xIyLhmmIg7yMyf8FhYRip3wRWOp4j5yiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f614280f10.mp4?token=LP-VpBglrT9VuNs3Ir3woUjoAIwwfWM_dfTLn2UGeZUjf0iQK0U4h47pNRHv3I-ObjtxmJdQbBk_g0udH7aFqKLEmvPr1R4JHjNsmuZYMysXOjIQcKlTwFMffBbpXntJRI5tXaGG-2OewELZKKpN6iAdxOu6dFF8a672tDq3uGKQ63_xjA6gl4MZFemOCgZvRVwBPAwxpvBwD72C1KcXQrP4Jwv-Ji0bIy1OhO2EBRXGWxtx1CekKzBnULos3yBQqi0odbtYWW09ghRg0sAUQFPkJCrjgwVYhOWAkWcO87E04G4nxhiu6xIyLhmmIg7yMyf8FhYRip3wRWOp4j5yiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایران فدای اشک و خندهٔ تو با صدای حسین طاهری
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/456640" target="_blank">📅 22:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456639">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTD2feGkbFYg7_O2LMiYSngrGIsoGpJr2tmX0PZ_fOrmSIpkp3yq1Kx7w_lN2gWAcb8fAYeCNLQWf4J9IjyHB1rQ8lfqWCOnB_hsyGFNreaxg9f6vTIYv_FWJeWCmnImfg25y_I-v1x4ySCi8IiD-Ra9iZ1r__SyPZMsQ5RiT0d2MQuGhVuqu7Xd9DrYo-naVTKmFWSNX16FuoYCW7jIOO98v4RVCEogYgzeESuPeasJj7rwGRtZSAHq-vkqY1rNFLgedhxzwAusmHh1odm4-BqxyRno_f3SKauWbCMCdDhakfDcdbYoVJkIGylwUrcXDhMo9CtQWso1Aos2-epKYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">المیادین به نقل از مقام ایرانی: حملۀ امروز به اربیل ارتباطی به ایران نداشت
🔹
المیادین: یک مقام ایرانی به ما گفت که حادثه‌ای که امروز در اربیل واقع در اقلیم کردستان عراق اتفاق افتاد، نمونه‌ای دیگر از عملیات «پرچم دروغین» است و ارتباطی با ایران ندارد.
🔹
این…</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/farsna/456639" target="_blank">📅 22:09 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456638">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">ترامپ: دنبال تمدید تفاهم با ایران نیستیم
🔹
در حالی که مهلت معین‌شده در تفاهم‌نامه ایران و آمریکا برای حصول توافق بر سر موضوعات هسته‌ای امروز به پایان رسید دونالد ترامپ مدعی شد که دولت او به دنبال تمدید آن تفاهم‌نامه نیست.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/farsna/456638" target="_blank">📅 22:04 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456637">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دادستانی تهران: برنامۀ اینترنتی «آزاد» هیچگونه مجوزی بزای فعالیت رسانه‌ای ندارد
🔹
دادستانی تهران: پس از انتشار یکی از قسمت‌های برنامۀ اینترنتی آزاد و طرح ادعاهای کذب، علیه عوامل این برنامه اعلام جرم شد.
🔹
در بررسی‌های انجام‌شده مشخص شد این برنامه اینترنتی، با وجود فعالیت در قالب پلتفرم تلویزیون اینترنتی، فاقد مجوز رسمی از هیئت نظارت بر مطبوعات و معاونت رسانه وزارت فرهنگ و ارشاد اسلامی است.
🔹
پس از احضار مدیر این برنامه اینترنتی علاوه بر اتهام نشر اکاذیب، اتهام انتشار رسانه بدون اخذ مجوز نیز حسب مقررات قانون مطبوعات به متهم تفهیم شد.
🔹
رسانه‌ مورد اشاره در طول فعالیت غیرقانونی خود تخلفات رسانه‌ای متعددی نیز مرتکب شده است.
🔹
در نهایت پس از تفهیم اتهامات و صدور قرار تأمین متناسب، قرار نظارت قضایی مبنی بر منع اشتغال و فعالیت رسانه‌ای متهم تا زمان اخذ مجوز از هیئت نظارت بر مطبوعات صادر شد.
🔹
با توجه به فقدان مجوز رسانه مذکور، این برنامه اینترنتی شامل قانون مطبوعات نمی‌شود و به‌کارگیری تعابیری مانند توقیف یا توقف فعالیت، فاقد وجاهت است‌.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/456637" target="_blank">📅 21:58 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456636">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cc9486c66.mp4?token=PZQNseYuwnjN8XJf6ZkRAOqx2jt-C_5xv6o8nermCCyR4iSDGD229-8N8swaUqyC7cfMyuzWJbEFbKiN7ilBC4vLWB-rfiFQDENVBFnWdSBvPHRbahwi3WdF3b-D2uGVVCKoYZDauZ-TtL6btqkn9BlvOW9j7p1OxrIEH7CCVZrXWY4l14U2fT_PpLgRDG1fTOxLZHrEq0iUQUbU5j4QoxZjkUrtZO9B40Dp_lm4dVf8g6v9X-cSAS3nwXPsOBE5XbQV-yTeXtcLYGUirD2NvwczNb4tj9vIdPAwKDs9Eggj2q3rQ1o0aTSvRJ3etAaOOb35ezsuOhirJCXQMwGmsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cc9486c66.mp4?token=PZQNseYuwnjN8XJf6ZkRAOqx2jt-C_5xv6o8nermCCyR4iSDGD229-8N8swaUqyC7cfMyuzWJbEFbKiN7ilBC4vLWB-rfiFQDENVBFnWdSBvPHRbahwi3WdF3b-D2uGVVCKoYZDauZ-TtL6btqkn9BlvOW9j7p1OxrIEH7CCVZrXWY4l14U2fT_PpLgRDG1fTOxLZHrEq0iUQUbU5j4QoxZjkUrtZO9B40Dp_lm4dVf8g6v9X-cSAS3nwXPsOBE5XbQV-yTeXtcLYGUirD2NvwczNb4tj9vIdPAwKDs9Eggj2q3rQ1o0aTSvRJ3etAaOOb35ezsuOhirJCXQMwGmsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای مزار رهبر شهید در آستانهٔ اربعین امام امت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/456636" target="_blank">📅 21:51 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456635">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98883d627f.mp4?token=jBjvlV2wd62SJzA2mmAzTrcSv-MdeXKtCvcqueOWJ4Y07wxy3BWcO_LaADv7ZRlfJqR4l1t81v11EVwMIzLRYo6AZBd_lt3X9nRnyOdyFvOiLK9wtud9jloMW1P3txJ9F04cpqkLvEZUbJ_rMhUJfVzJ02tbAvT67R85iMRdq1Q1bido2oM2zUaQEQrHA20hfdw4g5fNljSwCs2_3u1BqV5gk_lHunVEGoF73FJf_k_iOiwgggqlTtZdAEXMrCuW0RGrMIOf1PsYJq5XQZN8zmV2Wtanv1C_xOpr6Q5T1ihwARbM6d6CXvrTteYCDdyzvZUprLnBIKXOPPOsBd3aXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98883d627f.mp4?token=jBjvlV2wd62SJzA2mmAzTrcSv-MdeXKtCvcqueOWJ4Y07wxy3BWcO_LaADv7ZRlfJqR4l1t81v11EVwMIzLRYo6AZBd_lt3X9nRnyOdyFvOiLK9wtud9jloMW1P3txJ9F04cpqkLvEZUbJ_rMhUJfVzJ02tbAvT67R85iMRdq1Q1bido2oM2zUaQEQrHA20hfdw4g5fNljSwCs2_3u1BqV5gk_lHunVEGoF73FJf_k_iOiwgggqlTtZdAEXMrCuW0RGrMIOf1PsYJq5XQZN8zmV2Wtanv1C_xOpr6Q5T1ihwARbM6d6CXvrTteYCDdyzvZUprLnBIKXOPPOsBd3aXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سوریه بی‌صدا تکه‌تکه ‌شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/456635" target="_blank">📅 21:48 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456634">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc7666a87.mp4?token=s-dnsmjfwiCSWmDhSIc76eV4IXKJUgDmNQwTOZdt5aidMkfEp44ItAsj8oG-kExP80Yp5fbJJPvhJoAxoiVGZA7kAuXm7DQBtlMB-9OGHAFxK4KlV5yiCLGjmMF2kHK_sfR6lPba5XRouF5-NYU6FgC4o2nQPw2lJl4_tsPNCXKbw-GC0nlsZLjH2VYiHUsI7t_Hb4b6n-uywivoN7L4lLgz--ZueLoTi65vWla2ypnCYbabQPTYsNR4xajAZcNJ_-CW2n4zix8Ntzm3aaF8RF3s-ei5aIsATuh0VWhnfVq1gpezSfYJnZFI9_4nnBQe7z5rnhEdxeDKLO3FsaANDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc7666a87.mp4?token=s-dnsmjfwiCSWmDhSIc76eV4IXKJUgDmNQwTOZdt5aidMkfEp44ItAsj8oG-kExP80Yp5fbJJPvhJoAxoiVGZA7kAuXm7DQBtlMB-9OGHAFxK4KlV5yiCLGjmMF2kHK_sfR6lPba5XRouF5-NYU6FgC4o2nQPw2lJl4_tsPNCXKbw-GC0nlsZLjH2VYiHUsI7t_Hb4b6n-uywivoN7L4lLgz--ZueLoTi65vWla2ypnCYbabQPTYsNR4xajAZcNJ_-CW2n4zix8Ntzm3aaF8RF3s-ei5aIsATuh0VWhnfVq1gpezSfYJnZFI9_4nnBQe7z5rnhEdxeDKLO3FsaANDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی گسترده در اطراف میدان شهرداری گرگان
🔹
چند باب از مغازه‌های اطراف میدان شهرداری گرگان از حوالی ساعت ۱۹ و ۱۵ دقیقه امروز دچار آتش‌سوزی شده است.
🔹
نیروهای آتش‌نشانی و امدادی درحال اطفای حریق هستند. @Farsna - Link</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/farsna/456634" target="_blank">📅 21:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456633">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🎥
حاجی‌بابایی: به لاریجانی گفتم «شاه شده‌ای»!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/456633" target="_blank">📅 21:37 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456632">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🎥
رسم مهم آبکش برنج در هیئت‌ها در برنامه «سرآشپز»
@Farsna</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/456632" target="_blank">📅 21:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456630">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMnJtsGwSOex_i7NvkO4TgsZidYLuf2CfB-Zr5XrowU7-G5p-661IOIUMGo-23i3camE4IlFOC9_ubyjZ-bulA2OtpBk8UHBkvgeU-Xnpv5nxgejmDmD5kUkH37gKnd9Zf6Dp_HGeoDV8u7z63Oh4JsAe1QYqN2RHEWLEmYt-IZY_FsS8JuMso28CxA1R8ciIQGSRDkImC5O5lzA4zXcBUvddPmYW7EEEhPoFBOWgY3wAPCERwT1ktvnUJtWQrNWTgN0uVSYxZecO4nAbWeyqN-REKNKHdB133r7zHMErvwn-0MOmp2CEqLZ9cqAzFbs2IclIPHIhvjpLqBHg6eccg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
هوش مصنوعی را به مزیت رقابتی سازمان خود تبدیل کنید
🔹
تحول در روابط عمومی و رسانه، از همین امروز آغاز شده است. سازمان‌هایی که بتوانند ظرفیت‌های هوش مصنوعی را به‌درستی در فرایندهای ارتباطی خود به کار بگیرند، سریع‌تر، دقیق‌تر و اثربخش‌تر عمل خواهند کرد.
🔹
دوره تخصصی
«هوش مصنوعی در روابط عمومی و رسانه»
با تمرکز بر نیازهای حرفه‌ای تیم‌های روابط عمومی، رسانه و ارتباطات طراحی شده است؛ از
پایش و تحلیل رسانه‌ها و افکار عمومی
تا
تولید محتوای هدفمند و مدیریت ارتباطات در شرایط بحران
.
ثبت‌نام انفرادی:
📝
ثبت نام دوره آنلاین
📝
ثبت نام دوره حضوری
برای دریافت اطلاعات و تهیه اشتراک سازمانی:
📞
۰۲۱-۴۲۰۸۲۳۲۴</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/farsna/456630" target="_blank">📅 21:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456629">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/farsna/456629" target="_blank">📅 21:32 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456628">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8XUO-HmLmS4LvMHWXDcz9ZJqxcSmGuh6JNLYHsL4exl3Ie9-zGk0XL5hH0Ojx2N9y3UXjkWBDmhWibaBbwqvxAj0QpwVfcdyRLEx02looJDsKkWVgXsJtU40tln28kXnIR4TYuCXM5U6yOsBwSqUg_XrTVlvbBq38n8-jialgIxKLeD7A1otrKbAfqJkFtf-ky9op4TUzVcFLRudFvhS3umMYhaLAAZvCkRQEn1GYjIFHAu9EKr1DvlB-EWb9JPIEgQjNZ2rVjWUkYb-3WDTK95_5Gfo9Z4iUD8xTc8SpvLaxj-cCUqYDDb6KJmGzcvkI94QoSOy0M3bPiSXiHXgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قیمت نفت برنت از ۹۰ دلار عبور کرد
@Farsna</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/farsna/456628" target="_blank">📅 21:27 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456627">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">داوطلبان آزمون بانک مرکزی گرفتار اختلاف ۲ دستگاه
🔹
۹ ماه از اعلام نتایج اولیه آزمون استخدامی بانک مرکزی گذشته اما سازمان اداری استخدامی و بانک مرکزی هر کدام دیگری را علت تاخیر تعیین و تکلیف متقاضیان معرفی می‌کند.
🔹
سازمان اداری استخدامی امروز اعلام کرد «مشکل ایجادشده مربوط به خود بانک مرکزی» به‌عنوان درخواست‌دهنده مجوز است که مصاحبه‌های تخصصی را برگزار نمی‌کند.
🔹
بانک مرکزی اما به خبرنگار فارس می‌گوید که علت تأخیر، ایراد در سؤالات و کارنامه‌ها و شکایت‌های متعدد داوطلبان است که به سازمان اداری استخدامی هم ارجاع شده اما پاسخی دریافت نکردیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/farsna/456627" target="_blank">📅 21:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456626">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c22cad8fc.mp4?token=UDq1XgzrpkBuJcVdbeoa6c1yeDDh3JFkmEldru1PwN9zTqKMNqgBAHoYhP03dooGa3cCiqDU9aw489e72TsYSOCx5cV6HWJ_cbneaC4y2miH8UBZlTOn3QAYeEKSIBR9nm1u6IlG66f9piOt5netA6es0bqyxnke0ZsPicRBVEPbIUm3OAthU2eQvmJgPmFOyVOCXhEIPmIRWjY0t0INr8QBqbDoDpI7d1mB582rloiU0-sXCKSiR8mx55lAkgWkH8oZ-3b5j0BfEzVd2xmz2xRdVUJYhL8DuaGBmHvJj--XEB0yXg7pOvr8tcPwGNXL9hzirUAZ_8N4Uoz0pkH9oiTJt25L7DUu3J_qLctEAauKm4pl-B5mcfb-ubKmhaJQFFY2aBT5pP9vHuTJ3OBepfezLGgyLVwHAr4e9t2_qZm7t4dE9OmWHohw248qxcnNj8z9ZjqU8KgpwDE00ZW4DIWM8-zpV-vbr1ytKOh7XNSjHY5DEWnr4LSApiisuE9wGz7vPwf2FunoIo_Bk6A1_nyVj7BfIzzywjO-xSpsujan7SFYcy_QbttKgRh4CgYh5c0IrBmaGcU7wmCoNQNup49TvGcO0hsaKIEQ8_clny6mUzrP84DpNbymxvY-yJ2E7-FTE0UuRRpfuIyjbW-MEN2kufH_V0U7kTbUcUqOkzo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c22cad8fc.mp4?token=UDq1XgzrpkBuJcVdbeoa6c1yeDDh3JFkmEldru1PwN9zTqKMNqgBAHoYhP03dooGa3cCiqDU9aw489e72TsYSOCx5cV6HWJ_cbneaC4y2miH8UBZlTOn3QAYeEKSIBR9nm1u6IlG66f9piOt5netA6es0bqyxnke0ZsPicRBVEPbIUm3OAthU2eQvmJgPmFOyVOCXhEIPmIRWjY0t0INr8QBqbDoDpI7d1mB582rloiU0-sXCKSiR8mx55lAkgWkH8oZ-3b5j0BfEzVd2xmz2xRdVUJYhL8DuaGBmHvJj--XEB0yXg7pOvr8tcPwGNXL9hzirUAZ_8N4Uoz0pkH9oiTJt25L7DUu3J_qLctEAauKm4pl-B5mcfb-ubKmhaJQFFY2aBT5pP9vHuTJ3OBepfezLGgyLVwHAr4e9t2_qZm7t4dE9OmWHohw248qxcnNj8z9ZjqU8KgpwDE00ZW4DIWM8-zpV-vbr1ytKOh7XNSjHY5DEWnr4LSApiisuE9wGz7vPwf2FunoIo_Bk6A1_nyVj7BfIzzywjO-xSpsujan7SFYcy_QbttKgRh4CgYh5c0IrBmaGcU7wmCoNQNup49TvGcO0hsaKIEQ8_clny6mUzrP84DpNbymxvY-yJ2E7-FTE0UuRRpfuIyjbW-MEN2kufH_V0U7kTbUcUqOkzo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رمز پیروزی؛ میدان را ترک نکنیم
@Farsna</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/farsna/456626" target="_blank">📅 21:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456625">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ادارات فارس چهارشنبه دورکار هستند
🔹
به‌علت مدیریت مصرف انرژی، ادارات و دستگاه‌های اجرایی استان فارس سه‌شنبه ۲۷ مرداد از ساعت ۷ تا ۱۱ فعال خواهند بود و چهارشنبه ۲۸ مرداد به‌صورت دورکاری فعالیت می‌کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/farsna/456625" target="_blank">📅 21:19 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456624">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ed9861801.mp4?token=bqrW53bfjYDDeCZYPnhpb3CUN5Dl51X-jBRl969_lF3_X2kaheZY7UFXG8fnNIWRp_0NmkYTpNvKJoGyr0XKTJ8scxm6n1MPnougGDBHKtJr6I5XW409ZjRueMRsBaGgdN2ltRCpNUmFqDitJ2ep4g1AM4A8FVSgLNMQVcr-lyrXBmXI6f_hnFBdW05Sv-BR0NLISdV87VdpYf5mhDP8xG_t0mOP_r-s4-CHJN7lRLVDLjGK7UHO4zJRhT8kURLB54FT4CfGKPMCcPHBSPOYzNhkyvHWGb8AIoytX5JAZEIm0YBUr92vDdjXSqBFscoqv3pqyh_ww5ILnPBWGYEm1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ed9861801.mp4?token=bqrW53bfjYDDeCZYPnhpb3CUN5Dl51X-jBRl969_lF3_X2kaheZY7UFXG8fnNIWRp_0NmkYTpNvKJoGyr0XKTJ8scxm6n1MPnougGDBHKtJr6I5XW409ZjRueMRsBaGgdN2ltRCpNUmFqDitJ2ep4g1AM4A8FVSgLNMQVcr-lyrXBmXI6f_hnFBdW05Sv-BR0NLISdV87VdpYf5mhDP8xG_t0mOP_r-s4-CHJN7lRLVDLjGK7UHO4zJRhT8kURLB54FT4CfGKPMCcPHBSPOYzNhkyvHWGb8AIoytX5JAZEIm0YBUr92vDdjXSqBFscoqv3pqyh_ww5ILnPBWGYEm1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی دروغ، جان آدم‌ها را نشانه گرفت
@Farsna</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/farsna/456624" target="_blank">📅 21:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456623">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f739732d28.mp4?token=cIB5hzZhQIeyhGm03TgA0nmnYki5AVv-V3uEtwW25phZEZRtbYlVBQwoajyLEYMsmB5ApsE1qmZRcp1NaSdmVXlZzxCa0rBwdGynO1XcmZLvRYlWWyYBxBwkQZaQZCx-bR4GILlMKJH_NAhYa57eOiSD5OSSwdzOeXxUwJg9fjCZlg5rhBtNKUDomhKKY_-PG9izXV1xzLNpyZeALtTUMbfQkJYwtdPSzsDgtCh5aJPXN0SOoa0eo0NKCmnyhZtgd03AR8VKQ9vrIC5Kl5cn5g5D1x_C8iyy6YAAHPYlLPRLXQPcXy7RpCBa-qnWkf5tBPwrFGr6kLFYyOEFy4TAPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f739732d28.mp4?token=cIB5hzZhQIeyhGm03TgA0nmnYki5AVv-V3uEtwW25phZEZRtbYlVBQwoajyLEYMsmB5ApsE1qmZRcp1NaSdmVXlZzxCa0rBwdGynO1XcmZLvRYlWWyYBxBwkQZaQZCx-bR4GILlMKJH_NAhYa57eOiSD5OSSwdzOeXxUwJg9fjCZlg5rhBtNKUDomhKKY_-PG9izXV1xzLNpyZeALtTUMbfQkJYwtdPSzsDgtCh5aJPXN0SOoa0eo0NKCmnyhZtgd03AR8VKQ9vrIC5Kl5cn5g5D1x_C8iyy6YAAHPYlLPRLXQPcXy7RpCBa-qnWkf5tBPwrFGr6kLFYyOEFy4TAPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان نظام پزشکی: مردم به‌ تبلیغات فضای مجازی در حوزهٔ سلامت اعتماد نکنند
@Farsna</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/456623" target="_blank">📅 21:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456622">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b19927a3d4.mp4?token=Kp0UOJSInmWKBYuIYgE_c0sUoEDJyZRFEGP4g0Ep5xOBKttJxXfTcB1d29kI7HwqMnvLlqKwbSGjcIU2l5VFNSho_FDgzGqBsPBDEMzr4hOnZnpnCV_y1HtZi9uR-47uihl-uZbwlglaN4JvPBrGIHylIIXcpV3Yhz2k6QYlg3Pr7VTJXRtbzodZTBMZ3-XNnnmRmu9fDRjsEfG5VLbs2Tt7qJBBCTWg-Ejd7O5muoyPUzx9Qsal6qGde_fDSFXNrbOWXeZzbCDhLJa5nMqwOCnfI74rUfTuHArq_wfsXz7oM1QtFjFS_ygOdbKHTTL_iM4u73k4wk9LIj1Yyq5pojzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b19927a3d4.mp4?token=Kp0UOJSInmWKBYuIYgE_c0sUoEDJyZRFEGP4g0Ep5xOBKttJxXfTcB1d29kI7HwqMnvLlqKwbSGjcIU2l5VFNSho_FDgzGqBsPBDEMzr4hOnZnpnCV_y1HtZi9uR-47uihl-uZbwlglaN4JvPBrGIHylIIXcpV3Yhz2k6QYlg3Pr7VTJXRtbzodZTBMZ3-XNnnmRmu9fDRjsEfG5VLbs2Tt7qJBBCTWg-Ejd7O5muoyPUzx9Qsal6qGde_fDSFXNrbOWXeZzbCDhLJa5nMqwOCnfI74rUfTuHArq_wfsXz7oM1QtFjFS_ygOdbKHTTL_iM4u73k4wk9LIj1Yyq5pojzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تفاهم‌نامهٔ اسلام‌آباد به پایان مهلت رسید؛ چه اتفاقی در این ۶۰ روز افتاد؟
@Farsna</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/farsna/456622" target="_blank">📅 21:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456621">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08d7c9ebcf.mp4?token=vadg_ZMCy2D7nfWH10CkSHXpNop4Z2hx9mEc0koXZZwRo5gi9uAU0OEQlyKTsobfBa8o2IwoZlrDUTT-Qm4cXqv480CEIvEcHccrPLtgLAMYuedijSmhXlwykMbdJxGhG7BTOflcNSWJLigNXR20Vyb_CR2W5fgQPPryBfs6gMUBpcmYouEazCLBt21Mq16MzIU9QPkxH0e34dCCnrHlPzNFt1-LpJ-FmGSJ2GzhG5FQQxnsftmdPmYoJ3lzBX3AXxfNNvx84wTfc44f0Rzt7EwG9liY_nShfFyigYcITYg4L_vLcuoA9lH1URqjaG9O0-sTUM105xa8li5HNht9dbaFlkbvMJXDBGGnLhiNSJGsDwZV7mp2uIkfL8ozsi5IltymLrsh06vpOm0oSSLr-3_1D4Xh09lug9aF-Swa-1lBuk4tCDUFkp1_k7gbZY5DcQnMh2WuGKuxRat5oyl3JgUmGnz3myXio4zoMl7UjJvDQnWxvMwcIVTGI5q89AyotStC7h8bH98ZpOTbVJgWQ3OwGq575ABE71Mrf1-RHIup_XBRemy6j29rlJ4jvoLBXfDFNg0KZhPRKA12j8Dqy8PB_CdC-OhRGzigpFfaKcKgxz-si39CJb4rN5ETUXE-Y9-d9qcU-zfHaJZ1bPrd_fqEMX0wMqWP5ugf1rsNAsk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08d7c9ebcf.mp4?token=vadg_ZMCy2D7nfWH10CkSHXpNop4Z2hx9mEc0koXZZwRo5gi9uAU0OEQlyKTsobfBa8o2IwoZlrDUTT-Qm4cXqv480CEIvEcHccrPLtgLAMYuedijSmhXlwykMbdJxGhG7BTOflcNSWJLigNXR20Vyb_CR2W5fgQPPryBfs6gMUBpcmYouEazCLBt21Mq16MzIU9QPkxH0e34dCCnrHlPzNFt1-LpJ-FmGSJ2GzhG5FQQxnsftmdPmYoJ3lzBX3AXxfNNvx84wTfc44f0Rzt7EwG9liY_nShfFyigYcITYg4L_vLcuoA9lH1URqjaG9O0-sTUM105xa8li5HNht9dbaFlkbvMJXDBGGnLhiNSJGsDwZV7mp2uIkfL8ozsi5IltymLrsh06vpOm0oSSLr-3_1D4Xh09lug9aF-Swa-1lBuk4tCDUFkp1_k7gbZY5DcQnMh2WuGKuxRat5oyl3JgUmGnz3myXio4zoMl7UjJvDQnWxvMwcIVTGI5q89AyotStC7h8bH98ZpOTbVJgWQ3OwGq575ABE71Mrf1-RHIup_XBRemy6j29rlJ4jvoLBXfDFNg0KZhPRKA12j8Dqy8PB_CdC-OhRGzigpFfaKcKgxz-si39CJb4rN5ETUXE-Y9-d9qcU-zfHaJZ1bPrd_fqEMX0wMqWP5ugf1rsNAsk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عاشقان امام رضا(ع) بر سر یک عهد مشترک
@Farsna</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/farsna/456621" target="_blank">📅 21:04 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456620">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32cce87104.mp4?token=Jahyky5nOKaNiXAGjbKv2UHkaScorAZ471dOZvkHlkCFTqL86AEojTGAS9I1UawPm38KZaBXa2NqKuApQHtElJFFjmxzGXpDBkwlGPo3pl7RnnBlW3RIonhtH0zdyYA8akycUVEiEz9f8jpMr8km00Qek9pb1cfdBQA4yLwVYXsNLXUSjd-MEZ6nnB_N2lnuAtye_joF-2D7GZ8CuGglRVYoCBZ7A-xOprfnM0g0H7bn-uI1LQK07KHuSlaFV_0ivvcy3bV5vMKo1SGEAyg7bk8_Aur_UkkjUAU9apbwQ5r0m67wx4_81qMteKXbaIZKftp7FbUlZoQuoxd6DFplwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32cce87104.mp4?token=Jahyky5nOKaNiXAGjbKv2UHkaScorAZ471dOZvkHlkCFTqL86AEojTGAS9I1UawPm38KZaBXa2NqKuApQHtElJFFjmxzGXpDBkwlGPo3pl7RnnBlW3RIonhtH0zdyYA8akycUVEiEz9f8jpMr8km00Qek9pb1cfdBQA4yLwVYXsNLXUSjd-MEZ6nnB_N2lnuAtye_joF-2D7GZ8CuGglRVYoCBZ7A-xOprfnM0g0H7bn-uI1LQK07KHuSlaFV_0ivvcy3bV5vMKo1SGEAyg7bk8_Aur_UkkjUAU9apbwQ5r0m67wx4_81qMteKXbaIZKftp7FbUlZoQuoxd6DFplwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شکست استراتژی امنیتی اسرائیل در مقابل ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/farsna/456620" target="_blank">📅 20:59 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456619">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PibKWO4hBmFVimvxaOpTvUAF85DPEBYo4mo3Q13uBSnEpw7vz-lB7Gj0OEY577kuWIljEq376pMD4wE7OKjqVw3cgUaJcADtsjE8W6xKZjkptA8wfZQL-x9lM7kUyXR8L2OtJ81ME-4wX0aAA3YaS1y89f-OoBzEaApiMveHtq_NTDrS-PlOoN9ctQVPXiCaWRMsAHJXqJG4PwWprCPqrpK4kBTYeZZVZBReFqfu97uGEyWm9CK-Vykz2tQkQg3eOCWpOdCQUPLX_wBLBoJKqMK9EFtHIZEU7arcoXOdo6OoqsEpP3qoxqQPAIGOGHu0spH4obTAFQFPvjk7CvA04g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دیدار غریب‌آبادی با همتای چینی خود در پکن
🔹
معاون وزارت خارجۀ ایران امروز در پکن با معاون وزیر خارجۀ چین دیدار کرد.
🔹
۲ طرف در این دیدار دربارۀ مناسبات دوجانبه، موضوعات امنیت منطقه‌ای، وضعیت تنگه هرمز و همکاری در مجامع بین‌المللی به گفت‌وگو نشستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/farsna/456619" target="_blank">📅 20:56 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456618">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae7778e2e9.mp4?token=c3jvA9dj-se3nyQsYyq-JER69V-euMUCfGhkdYx7ICqBjwB-HuAfnlo_eSS852jZ7Id3iISdATnMRc-tQ2l-gvgsIOmX6_ReGeZ_MB5rTshrVgmxC7PkCoL7Q6e298cJHFEZ8_6U3USOaKuG0Zd0VLcqIjyN8waQUHp26Xc8ZnF8fl1qDSHrDSHjQ-_MWiI4_y0pX-MCfUDH4Q0ewkWHimJIUJELOU_BhSMHRFJIZznlmBpapFenf7tYIuWkJIuaVywmhM8hHekf1Cd4XeA5Y6AavTfbNxXIKYBLPp2hTEQJ-HFsmAM_EvNB0KdzG0hmwSUTlY3NHSrSPiQX5zgJBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae7778e2e9.mp4?token=c3jvA9dj-se3nyQsYyq-JER69V-euMUCfGhkdYx7ICqBjwB-HuAfnlo_eSS852jZ7Id3iISdATnMRc-tQ2l-gvgsIOmX6_ReGeZ_MB5rTshrVgmxC7PkCoL7Q6e298cJHFEZ8_6U3USOaKuG0Zd0VLcqIjyN8waQUHp26Xc8ZnF8fl1qDSHrDSHjQ-_MWiI4_y0pX-MCfUDH4Q0ewkWHimJIUJELOU_BhSMHRFJIZznlmBpapFenf7tYIuWkJIuaVywmhM8hHekf1Cd4XeA5Y6AavTfbNxXIKYBLPp2hTEQJ-HFsmAM_EvNB0KdzG0hmwSUTlY3NHSrSPiQX5zgJBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز محفل اربعین قرآنی‌ترین رهبر جهان اسلام در مشهد  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/farsna/456618" target="_blank">📅 20:54 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456617">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IvfOiLrepdKlaPJsy-pPtC34WiuU0sgBYhaHrmV1vHCYgqMdJHPgNq7bkF5kl5J_h9mmD5xhCPTxdeFpYX4Nz6mNqj8v0gM3ZFrW1LNVeTfwd_7z0enJW-6cmOJhhfiI25pIiDzSR6_fKHc-B09rNkZOJB640KSpF2r_QAfi5A_yCjM2ZQfDA7MBJLQ_FbFH-porKKpJLHCYIHq9PJPbdkR0xQW4ZhQLdLYNLxuZ5U-x20-4rbfeKBrTyXCROYlsXPoLAt6LtyD-D_6Vbbq9jd3eZN-BeDfB6aRO8C3RrTsa8QdqdsMTxP_7qsKwJ9gMoSf7ATH-SPLH37J1JbuwhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ادعای مسرور بارزانی: پهپادهای ایرانی دفترم را هدف قرار دادند
🔹
مسرور بارزانی، نخست‌وزیر منطقۀ کردستان عراق، مدعی شد که دفتر شخصی‌اش در اربیل هدف «پهپادهای ایرانی» قرار گرفته است.
🔸
این ادعا در حالی است هنوز هیچ منبع رسمی ایرانی چنین حمله‌ای را تأیید نکرده…</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/456617" target="_blank">📅 20:46 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456616">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ce-l6Dxm0r52Tf42_4vjd2ljdfOUcYLtQLJOqFw8HiRghNX-a-HFeyDa2vvsX3ukhNNvtEkEOvgbCg0hFgBWBxt-6lrz41yd4pbN-qQEQf2HvIcoN9t3wDKe7v4zmwgKjaTAJXszbWoHLsIqCu29uOPM7YWG6VWNGJ0rfrcVfBycWFkoFc6vkSu-jugA2tuPqzDy6U9AFszy1_i0IHCRl1HKaOWBEIV4kzljitcuEgntbIwEYDvK5jPGAeXYO3OqU4HUbzKhPVCvB7GSEQUuQiHKHdp9n8EaCauz3k42Hp9vLAaqE29zsLliae-IoXRqsO9Wb1MEATs80nU6OJ1CIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلای کنوانسیون‌ها بر سر ایران؛ از پالرمو تا خزر
🔹
درحالی‌ عباس عراقچی موضوع تعیین سهم ایران در کنوانسیون رژیم حقوقی دریای خزر را به آینده حواله می‌دهد که یکی از مفادی که همین حالا در کنوانسیون وجود دارد، ۵ سال پیش نقض شده است.
🔹
شهریور ۱۴۰۰، بند ۶ این کنوانسیون که می‌گوید حضور نیروهای نظامی کشورهای غیرساحلی در دریای خزر ممنوع است، با برگزاری رزمایش مشترک ترکیه و آذربایجان در این دریا نقض شده و خطیب‌زاده سخنگوی وقت وزارت خارجه نیز نسبت به آن اعتراض کرد.
🔹
با این وجود عراقچی می‌گوید «بحث سهم ما از دریای خزر در کنوانسیون رژیم حقوقی این دریا اصلا مطرح نیست»، خط مبدا و تقسیم بستر و زیربستر به دلیل اختلاف‌ در مورد آنها از متن کنوانسیون کنار گذاشته و به مذاکرات دوجانبه یا سه‌جانبه میان کشورهای ساحلی «موکول شده است».
🔹
این نخستین‌بار نیست که کنوانسیونی بین‌المللی قانون می‌شود اما حقوق ایران با آن محقق نمی‌شود؛ نهم مهرماه ۱۴۰۵ پرونده لایحه الحاق ایران به کنوانسیون مقابله با تامین مالی تروریسم (CFT) پس از سال‌ها در مجمع تشخیص مصلحت بسته شد و مجلس این قانون را ۲۶ مهر ماه به‌صورت رسمی به دولت ابلاغ کرد.
🔹
اما دوم آبان ماه گروه ویژه اقدام مالی (FATF) اعلام کرد این کنوانسیون که حالا قانون ایران شده با استانداردهایش مطابقت ندارد و هم‌چنان کشور را در فهرست کشورهای پرخطر یعنی همان لیست سیاه نگه می‌دارد.
🔹
حالا کارشناس روابط بین‌الملل، داریوش صفرنژاد می‌گوید که از نظر حقوقی و مستندات تا زمانی‌که وضعیت بستر و زیربستر و خط مبدا تعیین تکلیف نشود، تحت هیچ شرایطی نباید این متن در مجلس تصویب شود.
🔹
او می‌گوید اگر هر چیزی را در سطح آب بپذیریم، در آینده، در صورت بروز اختلاف با این کشورها، همان مبنا به بستر و زیر بستر هم تسری داده خواهد شد و حتی می‌تواند «زمینه‌ساز جنگ آینده و اختلاف‌های جدی باشد».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/farsna/456616" target="_blank">📅 20:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456615">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktadaXCTf9zTJLA5mJkiXp9vlZXEEl11SH9-ngnXzS08pgVki-Yovdu91JOZ3B1q-KAHr-n8Bb6kxdnYd7oYyzfSx4YHrfSEhYjtwTZXbvniPs_MPX39IIZHmgwSPV5aEupPuEzpQsLZIMQkiZYDaW7aKyb8V_x0hIeqE53ixLsOFuYbrBm1gtbcs2ymjII1dCZjtmeEtubomSqv8EsvPEZXUHQPx2hay7IpA_Z72huonHNJURkAJuvwxkwCssDUNgnSi6Gvo9Gao74gPpEeVuizrAYhXi4mSlFQE2On7OesrtmNPy29jdDoLkFL45HKqBEcmw0JitW9EoKwvdmogg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا خواب بعضی بچه‌ها ناآرام است؟
🔹
ناآرامیِ خواب کودکان، معمولاً یک «انتخاب» نیست؛ بلکه واکنشی است به مجموعه‌ای از نیازهای بیولوژیک و روانی که هنوز به درستی پاسخ داده نشده‌اند.
🔹
از دیدگاه علمی، اولین نکته «ریتم زیستی» است. سیستم عصبی کودکان هنوز در حال تکامل است و «ساعت بیولوژیک» آن‌ها مثل ما بالغ‌ها تنظیم نیست.
🔹
وقتی کودکی بیش از حد خسته می‌شود، مغز او به‌جای فرورفتن در خوابی عمیق، دچار نوعی تحریک‌شدگی می‌شود؛ مثل فنری که بیش از حد کشیده شده باشد و ناگهان رها شود.
🔸
اما نیمهٔ دیگر ماجرا، «دنیای روان‌شناختی» کودک است. خواب برای یک کودک، نوعی «جدایی» است؛ جداشدن از بازی، از آغوش ما و از جریان زندگی.
🔸
برای همین، اضطرابِ جدایی در شب‌ها خودش را بیشتر نشان می‌دهد. بچه‌ها، برخلاف ما، مهارتِ پردازشِ هیجان‌های روزانه را ندارند.
🔹
در واقع، این ناآرامی پیام یک «نیاز» است؛ پیامی که می‌گوید: «من هنوز بلد نیستم چطور آرام شوم و برای این کار، به یک روتین معنادار نیاز دارم».
🔹
این‌جا همان نقطه‌ای است که نقشِ ما پررنگ می‌شود.
«
روتینِ قبل از خواب» فقط یک اصطلاح تربیتی نیست، بلکه یک «لنگرگاه امن» است.
🔹
وقتی هر شب، پیش از خواب، فضایی از آرامش، نور کم، یک داستان تکراری یا یک نوازش پیوسته برقرار می‌کنیم، به مغز کودک سیگنال می‌دهیم که: «امن است؛ می‌توانی رها کنی و بخوابی».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/farsna/456615" target="_blank">📅 20:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456614">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W69G9fPhcuCoMZwPgbZNf4FTa-9lkN_D3yDJqWHqDV0Fq_DsevJN3kvpuxoEetUWrvilPD_50wufgjNxGJUexMlEvoyowiJYHbgRbQp2nyFweycVnIjioKfL7PTVYchbm8E_2r2KnHY2p0O-dNpWr10Ezt43O3ScHeYHm4EeGyG7p7kgGIwpGWJyPYC4dUEqDjVsY31l_TBoG0VYx-zSmkvhjdHC8lGB_8JVVTz0FVmdxaghTz73FFTx0y1uzkmRBvkxtQ8Vs4uWdfwfHNhpL0VaaI06XPF1jItS7viL224eEJ13Rp9RHC8ksQAzRhbMxtADIP8pydxU_s6OfLv3dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
باتو در عهدیم تا صبح ظهور
🔸
مراسم چهلم آقای شهید ایران
🔸
وعدهٔ ما: سه شنبه ساعت ۱۷، مصلای تهران  @Farsna</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/farsna/456614" target="_blank">📅 20:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456613">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/925bd4fa5a.mp4?token=EpMUWl5ouhXs31HoxURrcDuNVVh8v4EoIAtBwlNqQR_24JI5LBJaZ7Z5FOGFc79k7TgXHY9838_Qx1apJEksh-12NHYMVike9aqOJOXRxaiLuztdklj0HGTjCGazFv10M_bSipkt4csKuMiX4W4tR_tlSTnpgi8xxWTuxGakau6F98VFez9iaAPFoxtR92dAYsF-zhlZ9GjhMdqw7JFgcwC7h1ct3_JodIi5RFzwJEBzbY6BUdYq2i_ESUlsXkf3faVpWDi3aDiQpmgWpPpAoTvcrXoKgXbixQJcnNiSxW_4ewAM_x7t-0ycclSGv48Yu01kyVW2jdTt7r_Xzb4djw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/925bd4fa5a.mp4?token=EpMUWl5ouhXs31HoxURrcDuNVVh8v4EoIAtBwlNqQR_24JI5LBJaZ7Z5FOGFc79k7TgXHY9838_Qx1apJEksh-12NHYMVike9aqOJOXRxaiLuztdklj0HGTjCGazFv10M_bSipkt4csKuMiX4W4tR_tlSTnpgi8xxWTuxGakau6F98VFez9iaAPFoxtR92dAYsF-zhlZ9GjhMdqw7JFgcwC7h1ct3_JodIi5RFzwJEBzbY6BUdYq2i_ESUlsXkf3faVpWDi3aDiQpmgWpPpAoTvcrXoKgXbixQJcnNiSxW_4ewAM_x7t-0ycclSGv48Yu01kyVW2jdTt7r_Xzb4djw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار در نزدیکی مدرسه‌ای در غرب کابل
🔸
منابع محلی از وقوع انفجار در منطقه دشت برچی در غرب کابل خبر دادند. این انفجار در نزدیکی یک مدرسه خصوصی و هنگام خروج دانش‌آموزان رخ داده است.
🔸
تاکنون جزئیاتی درباره نوع انفجار و تلفات احتمالی منتشر نشده و طالبان نیز…</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/farsna/456613" target="_blank">📅 20:25 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456612">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/456612" target="_blank">📅 20:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456611">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c53a4c455.mp4?token=r2Xo5ZYs9nWsmTFBDZs-1xCYuQUaMzRwwnaBrCaSS0w2kgTBVNXbcnEuWLpV7-7c7N0vsVjJMo2rSeYyVH9Or35BRJgbFcvi8pQJg4Vj0phhirrlGI29NCahPpjcpKc_uWowVbUi9NrlDWKJM0013FOEK9gwqjFbRD5WHoxQl1acdoO5syhz5pL7KQfnCcJ1pXtG3hlKa-5GaHVwa_nNLfKQlV1XEouabl0mvEojKnqjKeYwAdhjGcruZxsBfGTHxOeVhrm9m76t4TggzzIMWFiLa1QxXx99T9D6Za5hD9C6JNARw4MgpL6jrHBtLYIsjb0NxON5bbr5q_M-c1Ysmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c53a4c455.mp4?token=r2Xo5ZYs9nWsmTFBDZs-1xCYuQUaMzRwwnaBrCaSS0w2kgTBVNXbcnEuWLpV7-7c7N0vsVjJMo2rSeYyVH9Or35BRJgbFcvi8pQJg4Vj0phhirrlGI29NCahPpjcpKc_uWowVbUi9NrlDWKJM0013FOEK9gwqjFbRD5WHoxQl1acdoO5syhz5pL7KQfnCcJ1pXtG3hlKa-5GaHVwa_nNLfKQlV1XEouabl0mvEojKnqjKeYwAdhjGcruZxsBfGTHxOeVhrm9m76t4TggzzIMWFiLa1QxXx99T9D6Za5hD9C6JNARw4MgpL6jrHBtLYIsjb0NxON5bbr5q_M-c1Ysmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز محفل اربعین قرآنی‌ترین رهبر جهان اسلام در مشهد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/farsna/456611" target="_blank">📅 20:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456610">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwfjEAnE9M4unghOQKVFImA8tKJlIfvpkmyZy51re5U5bjHn_2m23CvLKHBBfOYo7atXBlGcOQt2N_3L0StB8XlXUWRN2OM7pnwaZ4p6SBs53mfeXtwAl_ipqGckoT_aSFSuFviALRhQ1O-mPty9gqDqsM279DPHCy-nubvdx30jDmROyqfuDNzYQHPVWsj22OvFpO4ZSoRNTuZXfzLTxcFqO_kNg9VC5eGy85FDQgY1-VuAxplvGbzrSE-tbb7L6HWRP5uBSx0e4nn_tf-B0AElGyX9Ui0wSsmTrVDi_Lq9CLCWq5t-aPQ2E3aC5BYpTUQ6sax3d1bME_Zol5eLsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استقلالی سابق در آستانه پوشیدن پیراهن سرخ
🔹
رامین رضاییان، مدافع فصل گذشته استقلال، مذاکرات خود را با باشگاه فولاد خوزستان آغاز کرده و طرفین در گفت‌وگوهای تلفنی به توافقات اولیه دست پیدا کرده‌اند.
⏺
قرار است رضاییان طی یکی دو‌ روز آینده راهی اهواز شود تا مذاکرات حضوری خود را با مسئولان باشگاه فولاد انجام دهد و در صورت توافق نهایی، قراردادش را با این باشگاه امضا کند.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/farsna/456610" target="_blank">📅 20:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456609">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35e2089c88.mp4?token=cdn2tj_tcy4G1jkGZZmY5HLSFjQqvZBWjggFfo-Lb1vH_8txFzX77IMrwsEbFr2PPIf6wosI0DAb4DtQa4e-pH_8kzGkUhAO7_Aa_71EAT3kHGTJqJ2MsDfcQ82HCLVaakVz6WGhMfqeMBVwpyzhLliP_okYONul4xeajiQDRAgoSDLYSvMo5eFmGOhZpMp9e__s0gYcBB4YUwdDmb4I0I3A-DHWCEByuiTEKGd6es5UMo5FYw1ok_qVKdXHQoTgDPPwoHM8EcO6KFpA2zaoDVac-ePv_00-eRjCbcEtm3l9bLwqsIqArw9qlUvkq7wCuwt0DBSEM63pkKwT75Q-cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35e2089c88.mp4?token=cdn2tj_tcy4G1jkGZZmY5HLSFjQqvZBWjggFfo-Lb1vH_8txFzX77IMrwsEbFr2PPIf6wosI0DAb4DtQa4e-pH_8kzGkUhAO7_Aa_71EAT3kHGTJqJ2MsDfcQ82HCLVaakVz6WGhMfqeMBVwpyzhLliP_okYONul4xeajiQDRAgoSDLYSvMo5eFmGOhZpMp9e__s0gYcBB4YUwdDmb4I0I3A-DHWCEByuiTEKGd6es5UMo5FYw1ok_qVKdXHQoTgDPPwoHM8EcO6KFpA2zaoDVac-ePv_00-eRjCbcEtm3l9bLwqsIqArw9qlUvkq7wCuwt0DBSEM63pkKwT75Q-cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی گسترده در اطراف میدان شهرداری گرگان
🔹
چند باب از مغازه‌های اطراف میدان شهرداری گرگان از حوالی ساعت ۱۹ و ۱۵ دقیقه امروز دچار آتش‌سوزی شده است.
🔹
نیروهای آتش‌نشانی و امدادی درحال اطفای حریق هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/farsna/456609" target="_blank">📅 20:08 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456608">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwMDodkGMdd1WJCJ_6_UEf-wUj8voKOSOehnNZLzsj8KpizhZPCE_7HwE0EmCJNJLqvs8v1L1BgYKzjxvaeyYwGyXFIgPjoPJ6I1HXqSHY8o_1JY_3a2kYNTVHHrizhbS9K95bI9gNqg1GTU2rrx-FRTSmv15Eub6vLnB4iWGU5mrJ_I_bUQbqb81704kSU2XQtSKyHkH3uzIjoTC00t5MFLJ0AF_DlpdLpyGK71a5-k_Fc3cPyStMgIh5xB_1XGNoFGHOs4MjXxSrc6uZdXjnD6SDREOyik9BqAsuPI3HP-JAhKYiESJysmou98IZ2ImRbokikzSTvsYjwIDngbzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌ریزی اینترنشنال برای اغتشاش به‌علاوهٔ جنگ
🔹
رصد رسانه‌های ضدایرانی، از جمله ایران اینترنشنال، که همواره در پازل جنگ روانی آمریکا و رژیم صهیونیستی و زیرنظر سرویس‌های جاسوسی سیا و موساد فعالیت می‌کنند، می‌تواند شمایی کلی از سناریوی دشمن به دست دهد.
🔹
به‌تازگی اینترنشنال، زیر پوشش دلسوزی برای معیشت مردم، اقدام به انتشار ویدئوها و گزارش‌هایی درباره وضعیت اقتصادی کشور کرده است.
🔹
این روند بخشی از یک فرآیند و پازل ادراک‌سازی و مهندسی احساس است که قرار است در چند مرحله دنبال شود و هدف نهایی آن، برهم‌زدن فضای جامعه و باز کردن مسیر برای حمله نظامی آمریکا عنوان می‌شود.
🔹
در این پروژهٔ جنگ شناختی، این رسانه معاند در گام نخست با برجسته‌سازی مستمر مشکلات اقتصادی تلاش می‌کند تصویری بحرانی و فراگیر از وضعیت کشور در ذهن مخاطب شکل دهد.
🔹
اینترنشنال تحت پوشش بازتاب مسائل اجتماعی و اقتصادی، تلاش دارد این مسائل را به ابزاری برای عملیات روانی تبدیل کند. در ماه‌های اخیر، حجم انتشار محتوای این رسانه درباره وضعیت اقتصادی ایران، اعتراضات و نارضایتی‌های اجتماعی افزایش قابل توجهی داشته است.
🖼
اما رسانه‌های ضدایرانی چطور می‌خواهند مشکلات اقتصادی را به اغتشاش و جنگ بکشانند؟
در
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/farsna/456608" target="_blank">📅 20:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456607">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omIcmqwMVLlYyxR1Z5vBJqr8smLKzqPaVH6_lx2583G0LWFx18Es8s762YWeHtp4gp6bTlL6tXq8axdqh8T-T1fp2_Uyb4FsGUWgqS7H69AmKk1WtKE8LL0UFqOOoTVyn2VNGYdlMizxSssuxRfdgy3cPaZvkdp2QtQv9ukXqMJtHI_nBSenN3E9wLfvWbwfRFqpD1wFLrZ1tPVL2E_xbUgAYaY_k15ryiO40YUMLOtHf0dXK7slv2moQnn9XqPoG-YNmJ5478p2dYOU5WIB1cq_GMzrhkn_NC890sdPTJx1dyK3jt4CF4Z1fGa_5TQ4LW4-iodVk8znyzQXCrUoUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
باتو در عهدیم تا صبح ظهور
🔸
مراسم چهلم آقای شهید ایران
🔸
وعدهٔ ما: سه شنبه ساعت ۱۷، مصلای تهران
@Farsna</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/farsna/456607" target="_blank">📅 20:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456604">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A8pAV8p5NqF0eG6nOrYE23DosN2PaEwYPa34jKH6sT1jmqPcAKiVvh8grZ9VQ8-9-fyojDLTJpHAlySZXMWQ2uvvOgsBOWZFGqR4YLyzQyTWxjS1JB0jrctzjSF2WA7eZKRTgAEOBbz2qmRZlAh7ewmWy8zJiCX6Nb6NX1tQzyQUcpXOJxiG_zkZXku5SZkUB1TmPPPpw0NnckjXpC8AB9G96lOzEMwtNJJGnBEFTsjUVM3b5VQjcu5Rl9syU-6MrpEV9qQ3XQwdEkKvPQNe00RXReXQSOeMCUIUUG9DMieIrqBpEWCh21BL9PHxNcsIAOIFyyY-ozvGZ17PUJ7vMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JsKbMzjyLKGRO67ZSuvpISApySWunozNR41-rqvrr9aFGy0pZWx3afXghnF1KSvL4t-HiKcHrpBAyuMX7oySHvHjX03vptedbY3aushSbvpD7sLjtXAWZQIxfJDtDqmGwCpBp30yvtSUv59EKP9jvkWOkIyzStsBwDEniHmNDkhu2aJJPBZc3HK6juVJEW12PLfCQXQYxLeMWh893Q9rX4caMIa_o_nEJ22K7sD7t6Ie2jycPMlvx1yIZEr-f0Qj4WFwoldxUPsKLU73OHd52MnhG566VE6O2fW5HuxZxBDkckdIzIQwrD_JrFv4Ega3CikQuGafH9pcZrSzn4ERcw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47448df422.mp4?token=nM4_uawg43hNydMj3Ys6r5GeW4uAMzx4_LmPfilfiep3QiTf5_3UIqvmA3ynidBNS2uMecehyaUe4FkmDJlxNbvKKOJ0rRGMIRpte1x1seOLxFWRUgf0Xtc6tYfMIc6zUrUwS5f-_in2liqiLV39wj4N2y9-lHakjbl3h3D4VKV5DC0NXXTG50pdbaK86Brqmb6ESx2JQVn-PQKf2mhtxMrMuu6yziRRglb0U9QMQpthUH2mWZaivN8Psk_oXoQ673DPU13YlGbpP0q9iVNZdYAongOmw7uIyjb2ebeBzj4RQMmFN-qsJ8CmDBAA11UCQROaizwEvkzDWoQsF1e-WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47448df422.mp4?token=nM4_uawg43hNydMj3Ys6r5GeW4uAMzx4_LmPfilfiep3QiTf5_3UIqvmA3ynidBNS2uMecehyaUe4FkmDJlxNbvKKOJ0rRGMIRpte1x1seOLxFWRUgf0Xtc6tYfMIc6zUrUwS5f-_in2liqiLV39wj4N2y9-lHakjbl3h3D4VKV5DC0NXXTG50pdbaK86Brqmb6ESx2JQVn-PQKf2mhtxMrMuu6yziRRglb0U9QMQpthUH2mWZaivN8Psk_oXoQ673DPU13YlGbpP0q9iVNZdYAongOmw7uIyjb2ebeBzj4RQMmFN-qsJ8CmDBAA11UCQROaizwEvkzDWoQsF1e-WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور سرلشکر ایزدی، جانشین فرمانده سپاه در رواق دارالذکر حرم رضوی
@Farsna</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/farsna/456604" target="_blank">📅 19:59 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456603">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d8cfdbf1f.mp4?token=gZhREyHiPLJsAeNIknSwQ2r0XiFHyl2E14sv2Du0QUQ-4ynHWy2_v6PnmVTN08N2b_k_lPRzFgl6Y3Wb7HO8GmLUL_1qnDjnXT9aHv1RTBI0--bQ0HsfCY0kBv3EjTY-hV7E-WqsdwayILSFu2Rt9gIHvW8CzOogsbibzZ2XRnL29yoxoq2Sxeg4UK3VksvVDav0u-IueksvaN_7-_d9ymBVxCaA8wz7yhfh_MpEe3TOniTiMg4e3IckG9psWzfnaoF3y7qMrEzh23WVHCXThwbuo5Hk17AEzMFnweWRjeTNKwjM6HQe2FRB5oU6_GNGoOGC0aPdITzEdZ-TlKaXHJ8KDX9lhEmRi77B_XNCq5of4BZmVuylr4yFoXwb7Gi7CviIDdccv7Osdou-KfMah4mxGKDQ3pGmkI8C2D0kfwwgyFMlvJvU15blkHxUoyoeFxBaHYnN3Ave58odTcd503sGRr2XnbQjIXHqcNax9pIGIjN8s5tKXItZCgIv4RsQnkvckGURdgDsugJEP1V5ZAvFivTRcRL0rQzranG-mk2nFCBZT0PauNmM0aJRLQ3Qd3u03gZbAavG8O2xxBPYY7dgOfp-oEsnGiacvOlxyEhZamJrf0EcD9nQylNjXpWXec18RCPgP8eSvrAFQ7MjhCp6MXg1Gu7_C5vRV6Gnukw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d8cfdbf1f.mp4?token=gZhREyHiPLJsAeNIknSwQ2r0XiFHyl2E14sv2Du0QUQ-4ynHWy2_v6PnmVTN08N2b_k_lPRzFgl6Y3Wb7HO8GmLUL_1qnDjnXT9aHv1RTBI0--bQ0HsfCY0kBv3EjTY-hV7E-WqsdwayILSFu2Rt9gIHvW8CzOogsbibzZ2XRnL29yoxoq2Sxeg4UK3VksvVDav0u-IueksvaN_7-_d9ymBVxCaA8wz7yhfh_MpEe3TOniTiMg4e3IckG9psWzfnaoF3y7qMrEzh23WVHCXThwbuo5Hk17AEzMFnweWRjeTNKwjM6HQe2FRB5oU6_GNGoOGC0aPdITzEdZ-TlKaXHJ8KDX9lhEmRi77B_XNCq5of4BZmVuylr4yFoXwb7Gi7CviIDdccv7Osdou-KfMah4mxGKDQ3pGmkI8C2D0kfwwgyFMlvJvU15blkHxUoyoeFxBaHYnN3Ave58odTcd503sGRr2XnbQjIXHqcNax9pIGIjN8s5tKXItZCgIv4RsQnkvckGURdgDsugJEP1V5ZAvFivTRcRL0rQzranG-mk2nFCBZT0PauNmM0aJRLQ3Qd3u03gZbAavG8O2xxBPYY7dgOfp-oEsnGiacvOlxyEhZamJrf0EcD9nQylNjXpWXec18RCPgP8eSvrAFQ7MjhCp6MXg1Gu7_C5vRV6Gnukw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نظرات رسانه‌ای رهبر شهید دربارهٔ صداوسیما
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/456603" target="_blank">📅 19:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456602">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8a4e15a27.mp4?token=WN26shZYPdmpJFGnqqCGUmf34pPVWwY-GU2XcxQrukicb3_dquxdzaEnfR0I44WsrG8JGvMfnZA0omarbljhISr5fF1jLKsFcHZPe1V1Cii9Ga4JYz7TwMmUcRwEUd-QWGley4ricow0917oLhmRO5AMRclGg3UCFkLMwygq6O96Pn_W9Th0_LzVp3dk9uO40Gjhlrs7tK-gwjbgjZx1BMhLZeOrBZzPYqkFsxIhYXiH3oLPHG36p3Oo2XvZCEMxmXqAz0yar7WjXXmpoZWY3GYOfh7zSlr8hCPHQbn_kXuz9jWULoGgDGW01NJSW_A5ODPcaCz2WBqAIVNJJdUWUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8a4e15a27.mp4?token=WN26shZYPdmpJFGnqqCGUmf34pPVWwY-GU2XcxQrukicb3_dquxdzaEnfR0I44WsrG8JGvMfnZA0omarbljhISr5fF1jLKsFcHZPe1V1Cii9Ga4JYz7TwMmUcRwEUd-QWGley4ricow0917oLhmRO5AMRclGg3UCFkLMwygq6O96Pn_W9Th0_LzVp3dk9uO40Gjhlrs7tK-gwjbgjZx1BMhLZeOrBZzPYqkFsxIhYXiH3oLPHG36p3Oo2XvZCEMxmXqAz0yar7WjXXmpoZWY3GYOfh7zSlr8hCPHQbn_kXuz9jWULoGgDGW01NJSW_A5ODPcaCz2WBqAIVNJJdUWUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاندوزی: «مرتجعین» می‌خواهند ایران را به ۸ اسفند برگردانند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/456602" target="_blank">📅 19:45 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456601">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZYI1NNeg0eXksa5cdiwZoNY1qomuAsqZKNZoHZjwX-ja27_O3t9flymx1uuzPB8rvRR5cVUEbIWuI2pqiCRb1zEDbnVBB9RxM2PyrdjKHzDzcW11_K_YphFMtUvAsDuRgvxJddB-2EHlHKPBHk65qn_28nwLGatX2_0dY1r7uLHeiNkKCzSlRo6fq9HbdaJgzDjIUVli8eU3lxhATvzlMega8enFpRQIrZULiZzv2yIKfnxkKRK4dpyMiHDOl3ukobR1GMoJ08bPmF5HPpqqUkl4Ry5eeCb3qSw3FrTaNThs5YyTH-VIjYrKd3987VeTCvMULN6PwWDtrSQ6Ot3bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
توقیف نفتکش اماراتی در تنگۀ هرمز
🔹
داده‌های ناوبری دریایی نشان می‌دهد که یک نفتکش متعلق به یک شرکت اماراتی هنگام عبور از تنگه هرمز، متوقف شده است.
🔹
طبق ترتیبات ایران برای عبور امن از تنگۀ هرمز، مسیر ایرانی یکی از شروط است و پرداخت‌بهای خدمات و اجازۀ ایران از دیگر شروطی است که نفتکش‌ها باید رعایت کنند.
🔹
نفتکش امارات در نزدیکی قشم متوقف شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/456601" target="_blank">📅 19:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456600">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5ee7db29f.mp4?token=l2Xlh2hcMtZjGf3G3x3hqpW1h2Mp7H77M3Il9q4U1vBQCaAT2jlbD-wxHHFrIX1tWQLZFvDpVJD8PGzWZQZiyUXxrbHb1Hj65WnouYIz4nRSt_0EpelAf2Zd1H1b4krK47xeMma9RIseSZ5lyE9DQ6yb39E7pWcIYrOOKuugUz_Eo41FgxyHgNAoK47TYYw0iiKvnKmCkzkDKcC_EJsvViVCvZdO7W-e0fXy1IpigsAQ6iklOUf_xDHyes3DfNyqNpBS7lharduMnDEb48jmcvJeprYYVvABp4Cp3dIelXbdXkPkOhZLjm94BA7IkSkxO--TiOopEC_zrrzOHKoeXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5ee7db29f.mp4?token=l2Xlh2hcMtZjGf3G3x3hqpW1h2Mp7H77M3Il9q4U1vBQCaAT2jlbD-wxHHFrIX1tWQLZFvDpVJD8PGzWZQZiyUXxrbHb1Hj65WnouYIz4nRSt_0EpelAf2Zd1H1b4krK47xeMma9RIseSZ5lyE9DQ6yb39E7pWcIYrOOKuugUz_Eo41FgxyHgNAoK47TYYw0iiKvnKmCkzkDKcC_EJsvViVCvZdO7W-e0fXy1IpigsAQ6iklOUf_xDHyes3DfNyqNpBS7lharduMnDEb48jmcvJeprYYVvABp4Cp3dIelXbdXkPkOhZLjm94BA7IkSkxO--TiOopEC_zrrzOHKoeXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی بزرگ مخازن گازی در شهر گلنپول ایالت اوکلاهامای آمریکا
@Farsna</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/farsna/456600" target="_blank">📅 19:32 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456593">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bHMQbYbM1msX0Rcoe-mVhXrziNskOnLumyMh3W-jXfpE8LTeJaNaHfZEo6AMhYsyfSpsbiLOnCpCIX8K6BZfi3pLPGlz8dkqzE5kuBz_2PYOBZZ1Kdvk6KePu-eOuYKeYBr71Sm7k-LjeJ5AqQS0kZG9jpYQM4scSADA1m7oNXyIZJuAATxoMCjrD2gChZ0HmT5tXA_jki1upXH4BZWc2pCJewmiMH-8rsrKbVbcjeADxS81g-vDeTdiEhT5398ks9tfkwkaTe_mHZ_QT1RQGQIcgm5M8SPKq0gOVIMneOszEExz7T9kE8IW6NAe_bpBCrmf371XZh4uwzVicrtQTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HzSTVYZtcxvRWilCFJzXC0w2xMUvSSsItf_6SyGPY7cYO59iS_VejaEJMuksC85Z4ZJ4YYfDrqHLB0296Cdsh3bn70lck0LpBZg-rxwnBeKnqkI58Zv5imaxg3E3PpomIwLfSieg5nY-OpJvtvgz_HZVX-ry-fIaHjlD3KvbA2Buo-2p0FrwmigBa-PSQNSrv9Fo5wqfX-NWv0YawfIVuuYl7XelxpTZHmybN5JKNrul0VlT0No6asbkTHeAfQRBxFZujqO7a7mWlrayMHSHN_zlPkmuGlMwKpGmpZxKLTd1fMWbM9yv9uoSBpiy-pDQAv5_np1q0QVm8etFubWz8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XHQjeBiGp0RlrR6CStVbjSLMii0tk_J3SkKBvXLf3g2O3gsSvrBJqhyzdQ3lMzTWjI7B0Xg7ypf49G0kHpNi33Py26AycXVw1OkofSeUJL10agSYsbQqtRqkfAuPXSb2d3mqX72gGFVEikafFUIRz3_0UJsNZC5dMY2LPf6jPLHBAesHT0S-xo0S-jYl7-5b2JHZ5PHNXFZBX-OO_Z-OgFKoO_vubnNiJ-2_400iijbzMH7PCbSPsmlu770DofOOR9oP2UnJ8iYxsTcLCbIumxWXyyO1a6rZ64VB5YZNPV04aKgIL_Asrxv4A4NdCgh2Axi9ahjN__3zcAnFqwYTMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iwWrWGqFWYw1ns6ZzqLEDXGkSbU9Wk4lriIrc4lLJSId_8aHMKEipXI8fV_2c60kSAlDMSAjLDeCoOojGpx_CwFM3qPtYq6mM7h3j3XLzd2UlsBjbSzT5ZdCkbVYm2A_Ysu_vD_fhT-Zbww8A-IZvJPtZHQjvYBohk2fs3elYhKl3tRu8pVRQVsHuZgRB-TS4RSdgYpf2B9KYjBgHaTiTOyaqbEB61AHA4obW2yUciRwp6GB1lCqdjWpoimCuueLIGrYe9Q0qX0IMvhZH2-HQGis5mRLxaspcxZd_6tMHTECfWxJARi370LkVEsE0hQTgQHGXHMDFYyCZONakXvwOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g39GWGwSUzf6BEWHEbokJJ2g6fShZfrlJBHoPD07H4NAiikHmqDNFYuzczw3O2nMMAX-uajO0hYAA7_bBGK3EnBAd8-b5UrjyfreyceAPb_E2E5Nr8Oe18LvBXj7rrNSpyoqf0osl7Qg0cqK_hjtmyMNBqIa9uZHFgEBuZbzanmLAdAzC5Whb4hjIrzQw9076hNBTXGK-QDRV_xijMzkTXBKMYDjhNTdBhI-Slz04bBpElMqNkZgtiZ2EsGmdEAienfLlJqwzOUFcU2NG_6ZPwoTvKxilK90Onrm8dii2wCOJhwfNUobipvVGRKUZ-ziiQ99rQaIsvlQh6ICk4wDqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GquNPN1r8-OAnj1CbAdz4ukXsyWv2dj0cAjkVO36EON_JvXC0u0_vi81I0jfekrcRhhFikj0Io_4RsWU_7Iv-i6jUncVOWcG_cYFaLESjSvhNfJuw0CTYVM_QsgEXJkNYywdLqJCjftKkWI-ibFjRWr8FTBM6oMggHCQY2dc86KHClzYZRSqf6YNyeTkQOckATkwcmhiDMmnQStQYrbLc1_KNkz4AlLlF37Y3xGIAUBRN-HXMLtw9Xqo6VJMy8Qy6j8h-SZvzmGt-G-CArrJ8PDOxIJp2pnAoHMxkBfwy6EeXrIHod01Zs2YCUAQElQTXiFKWXXFxq7gDsFZJ0juHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EKK9ZNu8DuWZ3p_rTDkF2-yDpsTwaQJO9oqKNPUBE2kEmWZs7bXy5ACj6YcvgNtrgtyz0c9lMb-kVJV92vje3f1Iuwxua5IRr9rb1we55kuT96m1wDnXfDhHwugqYmSUWxa5uW-Oo7VkaZsA7FngOU6bnErCpgL90tfMgFIlRoAiTGBKEMR5OVYJTZox94xPlFTz6q0nfO7Aa5D9wC73YNanPTfihkFhhrl18CjQPb6A5Vss6xKrc9oGiKD_s_6DialSK-2EVUve-zycnK8OaY3qdeRLrS2sKJc2FTU4EHb8QXZVkJkYRd72Cf3K0fvhTDlaEnCCfbViV2rYHRQDxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آیین بزرگداشت امام مجاهد شهید
عکس:
هادی ه‍یربدوش
@Farsna</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/farsna/456593" target="_blank">📅 19:30 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456592">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19c9490400.mp4?token=LSP-b5lHmIboOK6mP1fcJnwq0DN8KgZ99BXtoJuNay0Om5mQyrAgB9y2SMMqdxVvljETXxlJDEkIOBCYiTnTGiVJwa3vU0f__QYVDNaZjdj3eTHANZaprZrFz6Ya_ww5W4RZBf_zX63OwzPPN27E95dekSapZzPP30fGWIRGYPJxgQS2QPvw5o__he99enSX4MRcW02gm0vcJ7cS-dhNMARVVZW_d3Gpvdl8tqngYg-DofTsVGezzt8P1jY2h5xLfOhHPC3sWf8rW-woPUYk9pS_hu6Yl1BYfkEfhbK7-J-GSAcYWmPI9u3ihi8ZLQ3XSzIcaQQQulIGLKwT-vTJCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19c9490400.mp4?token=LSP-b5lHmIboOK6mP1fcJnwq0DN8KgZ99BXtoJuNay0Om5mQyrAgB9y2SMMqdxVvljETXxlJDEkIOBCYiTnTGiVJwa3vU0f__QYVDNaZjdj3eTHANZaprZrFz6Ya_ww5W4RZBf_zX63OwzPPN27E95dekSapZzPP30fGWIRGYPJxgQS2QPvw5o__he99enSX4MRcW02gm0vcJ7cS-dhNMARVVZW_d3Gpvdl8tqngYg-DofTsVGezzt8P1jY2h5xLfOhHPC3sWf8rW-woPUYk9pS_hu6Yl1BYfkEfhbK7-J-GSAcYWmPI9u3ihi8ZLQ3XSzIcaQQQulIGLKwT-vTJCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
به‌نظرتان چطور باید انتقام رهبر شهید را گرفت
🔹
امروز ۲۶ مرداد، تفاهم‌نامه ایران و آمریکا به نقطه پایان رسید اما بحث ما جنگ و مذاکره نیست؛ بحث ما خون‌خواهی رهبر شهید است.
🖼
به‌نظر شما چطور باید انتقام گرفت؟
پیشنهادتان را در بخش «
فارس من
» خبرگزاری فارس ثبت کنید.
@Farsna</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/farsna/456592" target="_blank">📅 19:13 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456591">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-J-FTK6xK8ZAUNYOZAWBAy9FRHZfhZSz_2RCsQknXT1W4jPONaLDoddPRvEbdbPJtbtDa-IdlXOD0h6HbBOrjDe6fZBHfOFKlX3DWOGEsssqCOtOq6RsE-1uOkK1B8lLNq9Lxoc5orAYRdhbkEukZhr-Ys_bvqISRMZ9tbsPhaa9V1sz_k16EmccnACteLfiCY7iGT_R870XsVtFLcoj6nI3U3NI3nujYEKOKvruvQ2TX8ASZFkkpWyhpzX_UuZ5jB08wt4Gm44ZtN_psmBuUQTqiJm_mMGHxo9TGihV-gogrP3Bd45g0Uk9iIkA2JMh6kvzIKbDP7ccZzPgCOqGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توافق نتانیاهو و داماد ترامپ برای ویرانه‌‎ماندن غزه
🔹
هیچ گونه عملیات بازسازی در نوار غزه بدون خلع سلاح کامل حماس انجام نمی‌شود؛ این ماحصل نشست امروز کوشنر با نتانیاهو در قدس اشغالی بود.
🔹
مشروط کردن بازسازی غزه به مسائل نظامی در حالی است که ترامپ ۲ روز پیش ادعا کرده بود برای سر و سامان دادن به وضعیت ساکنان نوار غزه نمایندگانش را فرستاده است.
🔹
غزه اکنون بیش از ۱۰۰۰ روز است که در شرایطی میان جنگ و آتش‌بس شکننده به سر می‌برد و مردم آن در اردوگاه‌های موقت و بدون حداقل امکانات زندگی می‌کنند.
🔹
بر اساس برآورد سازمان ملل، بازسازی کامل غزه به بیش از ۷۰ میلیارد دلار نیاز دارد، اما هنوز هیچ کمکی نرسیده و اسرائیل هم اجازه ورود مصالح به غزه را نمی‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/farsna/456591" target="_blank">📅 19:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456590">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af8bb75f65.mp4?token=mRCxYu0Z7ktkqAmdJr77Lr_h1R4pqwSKhaarGo9J4a-u0XMp2en3U51nmO1fNyi_oF_24Yyn7fmdl9RZ4jqo8UqcQJdRgQ1G5XmKTvuQSla40paPEUIlI9wePE1ZI_Mvt_7O_e0j7Qm788GrmdKndA1TXCorbX1PuJcP8q7-islidpPbZBOg4QPNYxZM3tilsSEEP1W3BwKeffEwfzC8MOTyGAXzeO8xyWVF13GjFR7bF1Q4x-kVTo1_YHdqA7b5YP_HCNWm2OlAHH1q8ODPP1L6ZZ4FaA4Jrc50BwoW_mC15HJ2Vk_9uCBaa4ne50m3bWZMQgZXzVOOEH9qg7Rnkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af8bb75f65.mp4?token=mRCxYu0Z7ktkqAmdJr77Lr_h1R4pqwSKhaarGo9J4a-u0XMp2en3U51nmO1fNyi_oF_24Yyn7fmdl9RZ4jqo8UqcQJdRgQ1G5XmKTvuQSla40paPEUIlI9wePE1ZI_Mvt_7O_e0j7Qm788GrmdKndA1TXCorbX1PuJcP8q7-islidpPbZBOg4QPNYxZM3tilsSEEP1W3BwKeffEwfzC8MOTyGAXzeO8xyWVF13GjFR7bF1Q4x-kVTo1_YHdqA7b5YP_HCNWm2OlAHH1q8ODPP1L6ZZ4FaA4Jrc50BwoW_mC15HJ2Vk_9uCBaa4ne50m3bWZMQgZXzVOOEH9qg7Rnkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دست‌نوشته‌های سربازان آمریکایی روی بال هواگرد ارتش آمریکا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/farsna/456590" target="_blank">📅 19:01 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456589">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMKs4rdLGIwvbWp0p-P3ALkBjDeml7eN36CLEQtTF6GvNXo1eN60riGBicAgoEuAJzo-0TN9Pl1Zh2yBadZPC6ixqelSD0_htmftq-0LHAv1CuX3jSepcRPNhaY5uAMP_7svWSfzQIOeWKLhZAcUqBS2AQOafh8Dy8NFsUUkrpt2pYYeGnqzgt5TUPR6bG6y4knGLufTkXbQhqPaH0jAqH9x3PlA_SemexGo0UGffYsIWkyZLiHp-4k4O0_5m1GxL8vtq6sAZLim7wooHH7UnMdEJPdMFUipuhOQjiyK6hAw8rJwDJhPg4fWt6AWGWn7HFXkkZX0jzCUc_y5a45OYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لایحه‌ای که قبل از طرح در مجلس زیان‌آفرین شد
🔹
موجی که پس از اعلام دولت برای ارسال کنوانسیون خزر برای تصویب به مجلس در فضای مجازی به راه افتاد، خواهی نخواهی بخشی از توان، انرژی و تمرکز مردم و مسئولان کشورمان را از وقایع جنوب کشور به آب‌های ساحلی دریای خزر…</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/farsna/456589" target="_blank">📅 18:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456588">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XES8ma2IU3RNcrP0Yqc1ufV4xZ6aXSqrFNXJmydY4ZvRmHnQ2mIF-OMhtnZ1DveiaYaSIkuxdl_ExY8vyFzfic69vp4SxNX04oyPwDNSddP7DezPkohs4htKQLJRN74NxdtxmdYem65WXjby6tYy3CYMqCqtXCEmVh8xUmKpxFPs84TWxI7v_Taa1HpdIEBeKZsJiBPgHFeifhT4QCEOswxLf1a-ZaCIqBmDXJWsdylEtzbnoTn_ArMtjFka41kydkYmAaV_t-i9h3FBgM4_2q2d0ip4_QUkOBDAjR7IA7w0JGPU_8LQ1szrPy_OExXf5c_Yy_ZdQZ1ykq2tHGC_kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام تاریخ بازی روسیه و ایران
⚽️
تیم ملی فوتبال ایران ۷ مهر در ورزشگاه «کازان آرنا» به‌مصاف روسیه خواهد رفت.
🔸
فدراسیون فوتبال روسیه اعلام کرده است که این مسابقه به‌عنوان یک دیدار ملی رسمی در نظر گرفته می‌شود و نتیجهٔ آن در رنکینگ فیفا محاسبه خواهد شد. @Farsna…</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/456588" target="_blank">📅 18:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456587">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس افغانستان</strong></div>
<div class="tg-text">انفجار در نزدیکی مدرسه‌ای در غرب کابل
🔸
منابع محلی از وقوع انفجار در منطقه دشت برچی در غرب کابل خبر دادند. این انفجار در نزدیکی یک مدرسه خصوصی و هنگام خروج دانش‌آموزان رخ داده است.
🔸
تاکنون جزئیاتی درباره نوع انفجار و تلفات احتمالی منتشر نشده و طالبان نیز در این‌باره اظهارنظری نکرده‌اند.
@Farsnews_af</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/456587" target="_blank">📅 18:25 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456580">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ugm_bLunFx-RAVi46qQH5NU7FUYC_9HcLSinMCC_q_eYUjCjBbqm5yIKNZ3Jr-SnefmW0v4zC6kzVs0HLo_7i0dTCkUDI4xvaU0v1mf7HAs2Us9UvDsZ1v38_TlawD8Mqj20V_nMvrbFBsEMCj4-hgXDvYQ994H5F_Sx88XdPnl8IsBWM1ZLfolfMMAAl5WWS6NytxFlNC92SD4UdqYRIMwRRaj3FsMRP_Sa4voJRqa9Eqtbr7bl3l2crBITsj8NWqA1ZhgJsgTcBd0Nm1qlG0OYfWk9fXw6DtGVTK3tWpIr0KLJnXzvqD7TbyFKYxEBSdSHa3J2r2NehspDFA8a1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SZ7WR4FZKNM6VyYw4MKwcYsoOArBt4sQljEcJDI22ULj1PGXuQc2YnoshU19DyFVVS6wZDICi3ggq3WhF1ZEfhjh1XOpt3w-fruH8284dWB8cjqGkPt1lu8xfJBQw9K4FsYIBpcdeIZazFxAqIEiR9vWYwDtsMf5ljrTJSBlfSSrQoF5OYYYmRDGU69dgcvVOUaIncKNZxoIWb6LxB50pTNmA7mjx92aYoL6hV20ETF88ue98e3NMZ9cEOe0L5qrFoVtdxs8xNDwPgd6sCKkmUFyMGvja-N7_wTHBGNWWuHeNqVK58g_ELeY1a67wg8uRfI_77MyR0UdtM0iyNKnPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V_CQJ7MLM2Mh5eCoMOuemhn8aSfV78agCIZz7lZcYVBKao39VTAWIarkeUH_pyggdLCB-09529dHdKHnfuB15TPkyiLnGRKC3hf5OGMa_EJxGxAxsOwv0S1HnH87gugesmgI8HpEP0zKVVb4ERbGgwNHcDRqBE8pXssPGNMVUaXmJD_UL4JV7VC9ng-lf2lWSCnvyECn6W9qOO-GNVFdM5NCJaD0PN1OT4CXHMUR3fw8jq6GsfclpdSJKq6esiE45oiZ4a0-Kc-8kv35CO2jdOnldwbJfpEdy8kcE9esz7OP5wC9m3K4VGYIWnl_lXEb5GZwPQTWjBLQw_QEjBUUmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MtGIFTnv0QbRbJsQgsSCj9j-NiI7YYAvDF583VqwNyNv_EtRGBrdbwZJAb9ABM6m7S9uxHJ7GtBOV1R9yaAptcCPeloyi4RcNMGHu0buTjPL5EZtHdmhqfjkEjag-d8np5r1S561Xh4HRaJu5Er6kRKpkCN9q8BOS8zriXVf54_mCod87WVcUCzkLPrg-I0CwfGcSEG8SMCg4l4Bso1Y9NNH2imtGcejRhySOlOKbwQrg9PyU_9b-VT8UMdOBky_TEP688dhu6fLdR5stPKKNoYs9v5Apc1Et4jkc8JsKPojwJb1xD9YfM_KGA5iB-gwNJ2tVQhhwlTMxMKc0vzY_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yw5_b-deXQ3Zfnr_Y9En-ugLqtRjb5uZXRcyChELdQsRq5a2eh-s4h5mcfNA5bv7NnLAGqVutUDiEhoodImdjUX9vyOIYnGcKIrGP7Rqim6lqJGJzcpOW27Y6J5Fa3PWZXq5vteSeJeDlWCNWo7Sx_NbZstWkhAzPvqnXQctXA0Ne19lUy78ZLsqW0kRwOn-uNDpU1o6O0TzKH-mhSv51bmt8bk0-dnqQw7TTFqfgyoDhWWvTzliB_cRmJwJyvu7mS1Vo2qfWuVMSDqdtlu996z21C21VcKg4LKd8EdliAowimNqxqSLcxYcYhIj5tLrlw0zYsZ0x-C5prDFBIqsdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zx8Y9E2hYrDMP0SR_Sf6U3rWKZfRIdbEYNjHSeNqtRW95bsblMFHeTrNhGb7AUQScj1n6GELdtXeys2q9IG6ep337H9qQSkMUcEOTlHgnRB-yfxnvIMDjWcrbseJcYAMK_0JvzI-gWQuJOzbjPolrr1bebIp_Y1nmR4i5xhaStDPkdTezBY6j14LpqBCo-ZdnB1Qh-NKayLI0svNVZZ2oP5wcdjTUs4SOxm4RWSYxfb3n-DYN5D1cRYVTjSSHFcuASz0GjRb8sCv9keqM7jiVgmEKVnilgfOhRQX9D5J17XULMKOJ8g2F5YqOZ6bMp5YeIV59BMTqTVD8LpyY8U4Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ilej4JtRUKZeB1NQwHll5AQ4J1I8pyKJagIcXf4NJmPL0bCpi1HWeLAwDEfWizESNy_yC-mW9IsdaUxuXr9p0hMFQPLJcDckRnDXtBikteA6tfA0JCZ013NbRJxVlOqsTTj3CXFGZTzP8yKe0mL1sDAhHQRTmzixqQhBfvd7Sm4XF5mWzrrU00J5ueMN5i7o44ReMH_J5Wq6qxBvUzx0UCXhj7-xQgVEdwXQH0jQQuWYj-BljjtuzQQEgJnEEFqCZv_O8m2E2MqAnlRjysv2tC-D4ebF3kF40KKXix_sZ0oKIFN_OFt8PYf9NTqAt9RAa7hxXiS04kU9YVdkbj09VQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
گرامیداشت راویان خط مقدم رسانه
🔹
آیین تجلیل از خبرنگاران و فعالان رسانه‌ای امروز باحضور جانشین فرمانده و سخنگوی سپاه در سالن سوره حوزه هنری برگزار شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/farsna/456580" target="_blank">📅 18:19 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456579">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lx6uy35SuWH6AscC96auLeh1NBCziISx_yTaM27hTnToNwL8m2BgYo9VGCgoCC7MKDTZ2un0AP_2txgOLAutjDIf6_-w6P_pey2D9VVqWWMHZ_k1oO5urWzFXDOGTCOWbd5wYrziG_mjmdS5IakiA9cDvvehtyPR7GP6t_GRlmiXWwn922F2T4qDTX3h7V7ChjU--ThNoHa6LJepqDpT42Ojh15VqAAuWspr9xAvgurEOj1bDOKPmauo6tRibIhxLfezPSZ-KORlaprQSdS1ECpiUCoiRjlTrN9tlSRvGX8W27DfoWM0Pr4P4-w91-A0cVl9YUpWGTzPPDjKYN0UFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سفر عمره از اواخر شهریور آغاز می‌شود
🔹
سازمان حج و زیارت: اعزام زائران ایرانی به عمره پس از ۶ ماه وقفه از سر گرفته می‌شود و در مرحلۀ نخست هر پنج روز یک پرواز از استان‌های مختلف به مقصد عربستان انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/456579" target="_blank">📅 18:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456578">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8e88157be.mp4?token=B3eTsef5UdiVAoqnfVmS7pvxM_3MDO24RfouPciwwyRAZnVkKxhb_HMBbKfapy0HfAVT_rZeZXf04MWfTBatLU1uvrTV7qahNJE8rRMB6ISJH-BE6D_6i8hQHeMj41AE_bfrh1TED2Ps-3wRED3rCiMEKKk-ABOjF8D1GLbYQ4Iko2IShIhMSllrXiBTAAo2kxp-LnoOUdudxiSdsW-YzKk0i0QKwo-hpy2NHNIBHRybN8YDsEdpohAg4PfSwH5rFz-0vKyDl8ydnudZE4kHAZOZt36OgevJtaLw9g7TdXLxeQwcnBL5Yn6RbXt-l455z6-A0W6WHaAF9cF2thTtog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8e88157be.mp4?token=B3eTsef5UdiVAoqnfVmS7pvxM_3MDO24RfouPciwwyRAZnVkKxhb_HMBbKfapy0HfAVT_rZeZXf04MWfTBatLU1uvrTV7qahNJE8rRMB6ISJH-BE6D_6i8hQHeMj41AE_bfrh1TED2Ps-3wRED3rCiMEKKk-ABOjF8D1GLbYQ4Iko2IShIhMSllrXiBTAAo2kxp-LnoOUdudxiSdsW-YzKk0i0QKwo-hpy2NHNIBHRybN8YDsEdpohAg4PfSwH5rFz-0vKyDl8ydnudZE4kHAZOZt36OgevJtaLw9g7TdXLxeQwcnBL5Yn6RbXt-l455z6-A0W6WHaAF9cF2thTtog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام خلج در برنامۀ سمت خدا: اگر کسی تقوا پیشه کند، خدا برایش راه خروج قرار می‌دهد و از جایی که حسابش را نمی‌کند به او روزی می‌رساند.
@Farsna</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/456578" target="_blank">📅 17:49 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456577">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5074a8c966.mp4?token=CfVqNNGwtAyqwT9XW6Uha3Lh9f-2mQeJBqE8cvUD3Caa60tXNYXwQRGkaGaA7dNr1jqRQQsYLU2GHWP7aAX2MQczRBDP3tJj2WxCtTonWggJFNYffxJw0C4YgzTBVcoSMn9kB6aRMfBVadLD7QvJp_wfNYHCLNdOnM61tR0XLygz967mle_tWiw76F2gNzKZkdiwnd1lqr1HM-ey0il0nQr_-X-ZITDJs0Mq_QhAWPCdaLa0fDqfiJhlmQ3JI1ZEDt085w8k7iaqEdy_n8xJH9rn6Z8-vXHO5NeIwBAHIW64jbD88cg0B1gbpwvrnItCPcZkXCrJ1Q2v9fmAbX2JmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5074a8c966.mp4?token=CfVqNNGwtAyqwT9XW6Uha3Lh9f-2mQeJBqE8cvUD3Caa60tXNYXwQRGkaGaA7dNr1jqRQQsYLU2GHWP7aAX2MQczRBDP3tJj2WxCtTonWggJFNYffxJw0C4YgzTBVcoSMn9kB6aRMfBVadLD7QvJp_wfNYHCLNdOnM61tR0XLygz967mle_tWiw76F2gNzKZkdiwnd1lqr1HM-ey0il0nQr_-X-ZITDJs0Mq_QhAWPCdaLa0fDqfiJhlmQ3JI1ZEDt085w8k7iaqEdy_n8xJH9rn6Z8-vXHO5NeIwBAHIW64jbD88cg0B1gbpwvrnItCPcZkXCrJ1Q2v9fmAbX2JmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امضای ظریف پای برجام و کنوانسیون خزر
🔹
اگر درنظر بگیریم که نقش طیف اصلاح‌طلبان در برجام و پرونده هسته‌ای‌ ایران تا چه میزان پررنگ است، عمده مسائل مرتبط با کنوانسیون خزر نیز با یک درجه پایین‌تر به این طیف مرتبط است.
🔹
اولین مذاکرات پیرامون تعیین رژیم حقوقی…</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/456577" target="_blank">📅 17:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456576">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_73xRVHjLI1VLhjtodMvJs5B32cZQTF76FXb0x0eLcWy0sSmfh1ICQl4I_UuShEXvVd7-ct5jtrWtej2pHWHvMoH6_s-xmN6ng2kwBUwomy7EStioCT87FZIYEhm_NFEJXn_hmjXX_rGyr76NmxI80TR0W_cs_zmkJtFGjqJIqG0sgfmoqNIOeu_n0nE8_tsicx6M4TUyrTm_NN9_fQFHMe94NFp-2YWXNHNQfgiIpC4Gx_N0R7L15_yFqisAl_CMYG-JMX_4uWDNvNw6Qb01ID4UgUT2UgYwdzNebC8L2z8FWyVV2RNXHcRIwNuSDSAtM1vMm7kIUoYDl1yyxwVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۹ سد برق‌آبی ایران پُرآب‌تر از پارسال
🔹
بررسی وضعیت ذخایر سدهای برق‌آبی کشور نشان می‌دهد ۹ سد مهم کارون۴، کارون۳، شهید عباسپور، مسجدسلیمان، گتوند، دز، مارون، سیمره و کرخه نسبت به مدت مشابه سال گذشته آب بیشتری در مخازن خود دارند.
🔹
سدهای برقابی سهم مهمی در تامین برق تابستان دارند، با این وجود در روزهای گذشته، قطعی برق شبانه و خارج از برنامه در بخش خانگی و همچنین قطع برق صنعت بیشتر از گذشته شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/farsna/456576" target="_blank">📅 17:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456575">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">دستگیری عضو شورای شهر رضوانشهرِ گیلان
🔹
یکی از اعضای شورای شهر رضوانشهر در جریان تحقیقات و اقدامات پلیس امنیت اقتصادی استان گیلان، به اتهام دریافت رشوه دستگیر شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/456575" target="_blank">📅 17:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456574">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Po2mOjPCQn5bL_IdaA3DyckzyeimczCjcivQ03R7raHgxKC0_OBkGEfDJLhMcxoRLtDlTH7CCEKsyGK8U4sQkAPwguzY5aICjgtR2l1Cdr9Y-eapNLZNSVTz14xunL0yw3S6ft2K9Nw8CP3oTnko6IFVb6FevFMGvNvelwuJyW-NE31aoM7RpoC9Wqqw1R6gnAz674M2kHKIFKVJvINT8NDaW4iZ4FPo10gapIueZstRJuPHXPuTlkhfLyTLMnYusIKWP9lEujnSQeUCTqDeEqF44DLuVN5hk6OfUYyy3iL2ghxcy4goeQc_gBj7c0owgU9gAz0D77Bfy5jUm0e5mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
حضور آیت‌الله سبحانی در مزار رهبر شهید انقلاب در رواق دارالذکر
@Farsna</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/farsna/456574" target="_blank">📅 17:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456573">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a88979b73.mp4?token=dLN8MEuf4g4UIZ20PjI_VX35dEkAAxbO9hgcxLKGEaurFIpdOBfucD9Avkza61gG069yfTyT5YX6BPCdPN1h07Ice63UP7pkquWW5A3Pav4rQdMWTOHNVDzIDFrZpsSDPOAHVf2kNlwRZyX3amNnho0ZDdSvc2x0bQa4qS39e5LczCYCUOUhcpRLELt1--1gsDGbqbuU9YJ9yM4m-0xi-i6M8NX5gQQG-xjgS3kKqSTZvwbBJVIohJR1Tt69Z_fMrC3BLTLyjjVaQU0SZU7FSNS957rohoLUJ9XrPg_y0jo5FarXLA4WN5mcLmiA-TugZCJ91srgNjCVzmcGRVvYAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a88979b73.mp4?token=dLN8MEuf4g4UIZ20PjI_VX35dEkAAxbO9hgcxLKGEaurFIpdOBfucD9Avkza61gG069yfTyT5YX6BPCdPN1h07Ice63UP7pkquWW5A3Pav4rQdMWTOHNVDzIDFrZpsSDPOAHVf2kNlwRZyX3amNnho0ZDdSvc2x0bQa4qS39e5LczCYCUOUhcpRLELt1--1gsDGbqbuU9YJ9yM4m-0xi-i6M8NX5gQQG-xjgS3kKqSTZvwbBJVIohJR1Tt69Z_fMrC3BLTLyjjVaQU0SZU7FSNS957rohoLUJ9XrPg_y0jo5FarXLA4WN5mcLmiA-TugZCJ91srgNjCVzmcGRVvYAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کارشناس فرانسوی: ایرانی‌ها تصمیم گرفته‌اند کوچک‌ترین فرصتی برای حفظ ظاهر به ترامپ ندهند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/456573" target="_blank">📅 17:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456572">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6ovHscbDaOXHqiz8L6UfhelD7DrC3ytEmLYKZvy0cFCZaw622j8OAMSifdlJ135grKLnfo8VkRvsyHYKOw8hDhekna-o56w9iUOnPAcXus40ShEOGpKnkX8N8eZS15Pl5SzlGnSdnLUSbB6cJzxEtxOQV3iW6j4H0OpiBHuTSUntthNpg_mN438INBxQDNSyZsC1JPcAPn4t_SFfSNA6cu3yt9OET7UanvVZ9BV0LznCLXB4x-AqZSg2LREbAFdY3Xtbgu4cs72hV4KB5Z2eCp2SRt-iKe1PUUNVn9wlt3NnmwGR0edoHSZHFHf7Dd7lUUtL87XH5NXu6wz1wzY4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه: ادعای ترامپ دربارۀ گفت‌وگوی پشت‌پرده با سپاه، ناشی از توهم است
🔹
هیچ گفت‌وگویی میان مقامات سپاه با آمریکایی‌ها در جریان نیست و این دروغ ترامپ، صرفاً فانتزی‌هایی است که به‌خاطر توهمات و کابوس‌های ناشی از شکست و استیصال درجنگ به او دچار شده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/456572" target="_blank">📅 17:09 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456571">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehvWi61Etn9eB1RAWEO2ZKmfPzio3g_vQszNB_aocJgxHB9X6MoYMGMXXSz916tjQ4ck0mhko1ZLBbUPJ1P1YYnL63kQYyV1tVFg_fyTCJPo8lVf50y2vtROPJEvEKgSJLckQsRVkNsJzvNnWX-QE0tXSJbQdtgLQTSxs3xVfAmfsO_sfEP_tnneO1eHTPi36W0C5wbEZ_tIvQcFleGKGMHyJDPKz6ODexIUVDmyAbk3MdAPeIxa7sntJJw8Q4bYGpzTzqplTsoAip3DDgkiQlbM5p75If9YXOqZrjxonkNUtH2otyS8h1xrZs2cifrwE-a8fN1vXU8_6kn4wEhRkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامۀ علی مطهری به پزشکیان: دولت دربارۀ حجاب بی‌تفاوت نباشد!
🔹
مطهری در نامه‌ای به رئیس‌جمهور با تأکید بر لزوم توجه دولت به موضوع پوشش در جامعه نوشت: در سطح جامعه و خیابان، مواردی مانند بدن‌نمایی، استفاده از ساپورت به جای شلوار برای بانوان و شلوارک برای آقایان باید به‌صورت نامحسوس تحت نظارت و تذکر قرار گیرد.
🔹
نوع برخورد با کسانی که پس از تذکرات مکرر همچنان اصرار بر ترویج سبک زندگی غربی دارند می تواند در آیین‌نامه‌ای که توسط دولت تهیه می‌شود مشخص شود.
🔹
‌عدم نظارت بر این موارد ناهنجار می‌تواند به گسترش روابط آزاد به‌جای ازدواج منجر شود و در نهایت بنیان خانواده و روحی اجتماعی را تحت تأثیر قرار دهد.
🔹
این موضوع از خواست اکثریت قاطع مردم است و دولت باید نسبت به آن اعلام حساسیت و برنامه‌ریزی مشخص داشته باشد.
‌
🔗
متن یادداشت را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/farsna/456571" target="_blank">📅 17:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456570">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MIxA3_8TpAqnAYWPg7jy_uyC-ADWmS19UbV2Hy0ECkubqA6JLx3_HB1UOzGGXOXvm1SmqGWiTJ36X-KXIO1-VQ6cZL2az1c95VjVvbkB_0HBqVQ8qk96WJqYuRMqPIYie23_y6rRjVImsWEZyghF8zQ4A-zuOQXPxBm_twAWX-99RrpWbkdiWPpfcRenkHYkcvx-Nq9Dgc9kaNtK8YHXSTVqfRorgZlh5hrcOtOHJ7elsRU2pGCZ6ELvf0MIU6wWVYtZHKcXvy0C8IHzAIgEvUIIye6AYKYvv87tk4kUe926XOWTmX2IjX9I1cO-fz_ZmM4C1t3IXXkrj65HTVpTbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدهی ۶۰ همتی بیمه‌ها مانع رسیدن دارو به بیماران
🔹
این روزها گلایۀ مردم از کمبود اقلام دارویی زیاد است و تصور این است که بخاطر جنگ، داروهای اساسی به دست بیماران نمی‌رسد؛ درحالی‌که صبور، عضو هیئت‌مدیرۀ انجمن داروسازان، به فارس می‌گوید: «دارو در شرکت‌های پخش موجود است اما داروخانه‌ها توان خرید دارو را ندارند.»
🔹
او می‌گوید: در حوزه داروخانه‌ها، مجموع مطالبات مربوط به بیمه‌های پایه و سهم ارز، از ۶۰ همت عبور کرده است. تسویه‌نشدن مطالبات داروخانه‌ها باعث شده بسیاری از آن‌ها نتوانند چک‌های خود را پاس کنند. آن‌ها با مشکل نقدینگی مواجه هستند و به همین دلیل توان خرید بسیاری از داروها را ندارند.
🖼
اما چرا بیمه‌ها مطالبات داروخانه‌ها را چندین ماه با تأخیر پرداخت می‌کنند؟
پاسخ
را اینجا بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/farsna/456570" target="_blank">📅 17:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456569">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pqbewKKeRTCZQYg8SVgmpoJ7rXAF72mxccRxHGYR-218rsrkdvVzQ48eMHO3xCRdbjRDMuN5UVopKDoDBBU91Ya0SPz3l-F_ODSx78uceOMvC_q6rKgHLybViv0vycYFHNnUPokGAU1LP_IJk591k6UtwRq86BO86_0J4qb6drntIxe4t29do-K1QuQW6DSCTVFRmudc3uepJcEXQ428a3RaDPxeujhGPjskNzhvzVPEKuoBJWQbFmke1yw9hKc9sbPbnVbeHCck2FmlIkfxhz0eOglP8Wt5kG9Lt9CWFufwcZuQ0zHTTNbHweh2D1fxV-xcU_GHpgk-qapwyxRShw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حادثۀ امنیتی برای یک کشتی در سواحل سومالی
🔹
سازمان عملیات دریایی انگلیس: ۸ فرد مسلح وارد یک کشتی فله‌بر در فاصلۀ ۷ کیلومتری بندر ماریئو در شرق سومالی شدند و کنترل آن را به دست گرفتند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/456569" target="_blank">📅 16:48 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456568">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29848cea44.mp4?token=GCml1VQfnQa_0XOzrB4_vOBYTDeUUND6earpiNGuEHQTgJYIrY1S7Hebhi4C44BCjn5Gz4iPp15wq6bCW208GZ_0TLfeu-gAZXM14Tk_O8C8vE-fYSMFuzxB5N79P7SLyZDCbATJ9cgKVlVJX3bp8QIDSU6TgoKsuMWRdCOgpLzAXzefY43VYJuD5N65QoORKE94HyzT99r49wqtc0-U0SDEc_2qaFYwLHCDT_l2ZsY0jUKWxheznzjbCpW80X_i56Rcz-pARR5TWWhax9roE9V3-6QT13egeS4ltlTpnkoHnucpecX6pAAukwtoxqCTWxdn5yiwctdp20cArCcTYGnnSoT45PbeGrywLuAVW9QxmlHW4HDFQcICww3e4D0dmcjFzdJQqP4CnTknBM2zaECgjmww4pxCcWYnR1nwSVP-yIY127CaTbUzOzQx8V2aNSUQoJnt5rnY-qsF9Jpt5sOjGLTOow1wVJ1fBbTOU6hctSElnvdPBvX5s5CIqThSlPUE_cX9C1mJRVBe0qEl9P95eItwPXULzUF2YSCpyroKAO5ahocbCpvTiu9A0E5MMa1LCTQzrJ_sW5hRamv0ycOVrKviDPIiSr5nILVODzfucu5dAx93qXL6gHniFmxRSBd2NrTHxlKlcSL4Po-PwzclzH12FQNPMkU8WYuEXmk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29848cea44.mp4?token=GCml1VQfnQa_0XOzrB4_vOBYTDeUUND6earpiNGuEHQTgJYIrY1S7Hebhi4C44BCjn5Gz4iPp15wq6bCW208GZ_0TLfeu-gAZXM14Tk_O8C8vE-fYSMFuzxB5N79P7SLyZDCbATJ9cgKVlVJX3bp8QIDSU6TgoKsuMWRdCOgpLzAXzefY43VYJuD5N65QoORKE94HyzT99r49wqtc0-U0SDEc_2qaFYwLHCDT_l2ZsY0jUKWxheznzjbCpW80X_i56Rcz-pARR5TWWhax9roE9V3-6QT13egeS4ltlTpnkoHnucpecX6pAAukwtoxqCTWxdn5yiwctdp20cArCcTYGnnSoT45PbeGrywLuAVW9QxmlHW4HDFQcICww3e4D0dmcjFzdJQqP4CnTknBM2zaECgjmww4pxCcWYnR1nwSVP-yIY127CaTbUzOzQx8V2aNSUQoJnt5rnY-qsF9Jpt5sOjGLTOow1wVJ1fBbTOU6hctSElnvdPBvX5s5CIqThSlPUE_cX9C1mJRVBe0qEl9P95eItwPXULzUF2YSCpyroKAO5ahocbCpvTiu9A0E5MMa1LCTQzrJ_sW5hRamv0ycOVrKviDPIiSr5nILVODzfucu5dAx93qXL6gHniFmxRSBd2NrTHxlKlcSL4Po-PwzclzH12FQNPMkU8WYuEXmk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای بازار ماهى‌فروشان بندرعباس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/456568" target="_blank">📅 16:27 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456567">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jm2gYf4C15dTBjIK5nDTPkI6vC394ExB2cuiWC6C67svOKW41XbwbJsWojYZN6H96yl7U-yOH8mhDTTkohX-dM6pst50yuOvEdO2vdXkVewTR2UI0bpJU6KG0DHLf8Fqpoj-Ae8CJuo_nR7Z-9asfqyGLo9mKP7yMqSrkQ0lohCD3PX-ySz-YRumE_QL_rqwAMcps4cILm4XUXIjy98arnqTtej_nIqAkt6C2Jn4v_vLyeWi56ac2f4kTdH-r-mvhVduqyPeXQXxmJorIUpNIRXA6zmac3Gp7SGx_z0nK-FDb_JBhhYGjPrUUJ_Mi1dgGCTysllDaIhgzb1Dx75x8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عارف: رئیس‌جمهور تصمیم گرفته‌ پروندۀ فیلترینگ را ببندد
🔹
اینترنت یک شاه‌راه است و نمی‌توان به‌خاطر برخی تخلفات، کل شاه‌راه را بست. من به‌عنوان یک استاد دانشگاه نمی‌دانم فیلترینگ چه منافعی برای کشور دارد؟
🔹
برخورد حذفی با فناوری‌ها نتیجه‌ای ندارد، اما توجه…</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/farsna/456567" target="_blank">📅 16:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456566">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNPid1BgytfvHoqxLcDcyRO-GmM0Dh4PWhCdvE1ACmLS7kPybgnseTVOcILvLt0xG1hvodCvZqz_ZHMuRGNCQNhkzf3UaUQwL1yV31GpgNID9yJh621ncUSR9TJTSM2sCDv6uepRRmgQnfC0QvcFbeCTZMRV3p6eCjASa511O4zSg-cXTVWn_kY0pXOIMleygNQmfxXaAGJx9UqtOX3RAcTkpQLEaILnlvrSb2rHOTBIv7qUJS8tC1Mxj6VYjzxuFWxKTzYGMPj2dgLscCXlamYtoLgp6W67JiIk539Q5BzA-D-_mLVJQWU8Cx2rKnDjwHKKR_jKXSdWRN08XTWaew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عارف: دشمن برای کودتای جدی اجتماعی-فرهنگی برنامه‌ریزی کرده است
🔹
دولت پیش‌بینی وقوع جنگ‌های ۱۲ روزه و رمضان را کرده بود و برای هر دو جنگ برنامه تهیه کرد، اما آرامش جامعه را بر هم نزد.
🔹
اکنون نیز کماکان هدف دشمن سرنگونی جمهوری اسلامی ایران است و برای کودتای…</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/456566" target="_blank">📅 16:11 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456565">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">سپاه: پاسداران انقلاب اسلامی هرگونه تهدید و تعرض را با قاطعیت تمام در هم خواهند کوبید
🔹
بیانیۀ سپاه پاسداران به‌مناسبت ۲۶ مردادماه، سالروز ورود آزادگان سرافراز به میهن: آزادگان سرافراز آموزگاران مقاومت و ایستادگی، نماد حقیقی مقاومت فعال و امید آفرینی راهبردی هستند.
🔹
سپاه پاسداران ضمن گرامیداشت این روز فرخنده به ملت شریف و مبعوث شدۀ ایران اسلامی، اطمینان می‌دهد که پاسداران جان‌برکف انقلاب اسلامی در این مقطع حساس به تأسی از ایثار و مقاومت و ایستادگی آزادگان سرافراز و با اتکال به خداوند متعال و تحت تدابیر و رهنمودهای رهبر انقلاب، با تمام توان و آمادگی، هم‌افزا و هماهنگ با سایر نیروهای مسلح مقتدر کشور، پاسدار حریم انقلاب اسلامی و حافظ تمامیت سرزمینی، استقلال، عزت و منافع ملی کشور خواهند بود و هرگونه تهدید و تعرض را با قاطعیت تمام و با بهره‌گیری از راهبرد بازدارندگی حداکثری و عملیات تهاجمی پرقدرت، در هم خواهند کوبید.
@Farsna</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/456565" target="_blank">📅 16:04 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456564">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9fIs4mJEOOPNpJ7im1GCDwCxiFS7e-SaXhiu1lvABpGZwl4A7w8YX9tU4mE2VFzxUl96W6wpbqFVm36aZOL7g1RmiZS0mdm1F3fmvj5s-DX33nBA_6xH3QrIyld_dSsQi-hl7ZLblE_OlxUyzmhQ9Dm4RXhK-WNZHsPLp43gVguNkd7iWtZBcmkVbPHGLCa8_HIzonDdBrIec-1n6AMy637G_cZUH6v9_UtiEc75BL-F-s3ZfIp7vMzXWGuoQJfMrtsZ62XcowTfnHGua6kRE2IRo6tX_2RDd8N2bmDBGKF6pT7Ptq0xKVty89n3VwlGdwmzHUQxUNyddwZIpoGEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عارف: دشمن برای کودتای جدی اجتماعی-فرهنگی برنامه‌ریزی کرده است
🔹
دولت پیش‌بینی وقوع جنگ‌های ۱۲ روزه و رمضان را کرده بود و برای هر دو جنگ برنامه تهیه کرد، اما آرامش جامعه را بر هم نزد.
🔹
اکنون نیز کماکان هدف دشمن سرنگونی جمهوری اسلامی ایران است و برای کودتای جدی اجتماعی-فرهنگی برنامه‌ریزی کرده است.
🔹
دولت بنایی برای اقدامات آنی و بدون اطلاع مردم ندارد و اگر رسانه‌ها دیدگاه منفی افکار عمومی دربارۀ برخی تصمیمات را به اطلاع دولت برسانند، دولت اجرای آن تصمیمات را به تأخیر خواهد انداخت.
🔹
من نقدهای رسانه‌ها درباره تصمیمات دولت را هر روز مطالعه و برای وزرا پی‌نوشت می‌کنم که آنها را پیگیری کنند.
@Farsna</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/456564" target="_blank">📅 15:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456563">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/444fabb1ff.mp4?token=voG53EU6pF4ht72u4F8F0zmaprofMZU5_cnwFOTJXAlUFX4c_YlRUhWxVxbvso3evqrPuhyMyxvNM24sq4JDYqRW8Jlv-OMQfVURaoEAUnjvvtqwe-Ap6YFYYLm0QbZQC8ogJcMLFnRN4mM-Fg3IRLayMUasu3Lw8jJGvmQ2NQMRm2M-2a46XiMsUjKtv3RMaoUpPZIBrL9lJcLV7-3lV_mw75F8qoqTbJ_QkDBj3Xbk7G26oTHPxPoQ0lTpxpXXo6KCuOs1Q0Xwuma1ShYJMohCRphVRFThyDiM6eWbJLgYGElnxoW5iSo0_hOWvz_6mj7Y9zA9g_UHina0EJ3yuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/444fabb1ff.mp4?token=voG53EU6pF4ht72u4F8F0zmaprofMZU5_cnwFOTJXAlUFX4c_YlRUhWxVxbvso3evqrPuhyMyxvNM24sq4JDYqRW8Jlv-OMQfVURaoEAUnjvvtqwe-Ap6YFYYLm0QbZQC8ogJcMLFnRN4mM-Fg3IRLayMUasu3Lw8jJGvmQ2NQMRm2M-2a46XiMsUjKtv3RMaoUpPZIBrL9lJcLV7-3lV_mw75F8qoqTbJ_QkDBj3Xbk7G26oTHPxPoQ0lTpxpXXo6KCuOs1Q0Xwuma1ShYJMohCRphVRFThyDiM6eWbJLgYGElnxoW5iSo0_hOWvz_6mj7Y9zA9g_UHina0EJ3yuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ سرلشکر ایزدی: با یک‌صدم هزینۀ دشمن، در جنگ اخیر بر آنها غلبه کردیم
🔹
نظامی که مبتنی‌بر ولایت فقیه است توانسته با یک‌صدم هزینه‌های نظامی دشمن، جنگی را اداره بکند که خروجی آن پیروزی نظام اسلامی و رزمندگان اسلامی است.
🔹
اگر تحریم‌هایی که غرب بر ما تحمیل کرده،…</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/456563" target="_blank">📅 15:46 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456562">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1344ab35f9.mp4?token=hAkvXUpkPau_2-bxBqNYdZrnCEf_sS-UJVkXEF8EnG4lnzzcLejf4v-awElkjtOeN2kj3tfuoFmHcubmLJy0XD6kbmnw96oBapVJ83Abzz8FL84Vu0sfnGyub--ib_keFUPB_ilDPX5o_1P8zE7ObKF-eLMb9u9G8lTnqyDIbw0UQpu25yfEPKnLDE6LtBFeQR260Tzhxj87D-s0LDzAoJ1VT0MVB1u4LPSwIM9hDjD7O7T66DIB8iuA6JujO7Yb3qGEC8oLta7Ttilx-CHkhN14u0YzQT6fbwkFXBOFkl09zQWnCORSkikeS_sE-5lpW3ZKa861a56eBvnuetHOHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1344ab35f9.mp4?token=hAkvXUpkPau_2-bxBqNYdZrnCEf_sS-UJVkXEF8EnG4lnzzcLejf4v-awElkjtOeN2kj3tfuoFmHcubmLJy0XD6kbmnw96oBapVJ83Abzz8FL84Vu0sfnGyub--ib_keFUPB_ilDPX5o_1P8zE7ObKF-eLMb9u9G8lTnqyDIbw0UQpu25yfEPKnLDE6LtBFeQR260Tzhxj87D-s0LDzAoJ1VT0MVB1u4LPSwIM9hDjD7O7T66DIB8iuA6JujO7Yb3qGEC8oLta7Ttilx-CHkhN14u0YzQT6fbwkFXBOFkl09zQWnCORSkikeS_sE-5lpW3ZKa861a56eBvnuetHOHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آب از پروندهٔ مسمومیت‌های «باینگان» کنار رفت
🔹
معاون بهره‌برداری شرکت آبفای کرمانشاه: درپی مشاهدهٔ علائم گوارشی از جمله اسهال و استفراغ در تعدادی از شهروندان باینگان، نمونه‌هایی از منابع تأمین آب این شهر آزمایش شد.
🔹
براساس نتایج آزمایش‌های انجام‌شده، تاکنون هیچ‌گونه مشکل شیمیایی یا میکروبی در منابع تأمین آب باینگان مشاهده نشده است.
🔹
وضعیت منابع تأمین آب باینگان با دقت درحال پایش است و بررسی‌های بهداشتی و آزمایشگاهی تا مشخص‌شدن منشأ بیماری ادامه خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/456562" target="_blank">📅 15:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456561">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwuSBBksjdua4ZFUyBD92s054lZUbmC06Mqiy1Kb2PBl9T66pby16g1TjbimV0ONvc_1jvE-LcLoCTw_R579KHeRXNzDXIcNVMfi5fUxg9PFrUTbW3GBOj0qEbOOa4-k-X4B59yu80PQk40d9Dl3_nC45-6BZGACvjD2aJ9wvFKvMGSPkbhCZMcXs0eC57-690pNlbdKfRn9jpDvclSeJHdaifEvXGsmdDl1cUdsgYMcKFl3Daz6kfpRyEq6SnkbRz9Sz20ixeiGdCDw4VpmWT5oioFGdGkeigNtEze5IEEU5NicTHvM2AvQZK-dHsWBNAyBTGLqZod6zBQXl9-_qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اگر عمان در خصوص تنگهٔ هرمز مانع‌تراشی کند، ما آن‌ها را به‌شدت بمباران خواهیم کرد.  @Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/456561" target="_blank">📅 15:32 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456559">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDF-DZyXo1jKK6yMjud1zxoFaUKmxM-vM0K-aEzpmPtgZJoehfQ6jhZQMcif0E-MYdVqI6MuGokKiWT6taD3AgeQIgPRwTfbr_kpy4_5W-9-JGujHx9M7shR4kbwAJifU0dDtQ_jcNAgNzo0AyxzvhaP2KOMjgRLD5QOsGmmdDdhv04Fa-wj4qHTFi_0Qd9zBITR1py1Xg7nowvqqrRZ80sInaqJ-lqYeNjeJ7pxFM-pR0lGyqZFgXEo2gnvY7monrrU1rcyAndcRl_UXbUkalgu0CCj4q3gOmC3w12Y5MlEOYle_2Iw79F3NCWGefZxCZ6X3bIGI2QmB_KpM-C7JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اگر عمان در خصوص تنگهٔ هرمز مانع‌تراشی کند، ما آن‌ها را به‌شدت بمباران خواهیم کرد.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/456559" target="_blank">📅 15:25 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456558">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
سخنگوی نیروهای مسلح یمن: یک کشتی سعودی را هدف قرار دادیم
🔹
نیروهای مسلح یمن توانستند یک کشتی نظامیِ حامل نیرو و تجهیزات متعلق به دشمن سعودی را به همراه چهار قایق نظامیِ همراه آن در دریای سرخ، مقابل سواحل المخا، با چند فروند موشک بالستیک هدف قرار دهند.
🔹
این حمله با دقت و به‌صورت مستقیم انجام شد و در پی آن، کشتی به‌طور کامل آتش گرفت؛ همچنین تعدادی از قایق‌ها غرق و بقیه نیز دچار آتش‌سوزی شدند.
@Farsna</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/456558" target="_blank">📅 15:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456557">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GuQVOtZ47_bmo0rN2_USpxlLvhyyYDwbeybrrRzmutdtP9x4tvK0tw1Df4GmmsFSqu9mLu1_D9TIAoi4T579G27ztIHr9LfM31gNrQ_W_0PnJq6EZdY8wHbDmG8L5YAjWIMovrPwrX2-Tds5GqtdaLKqhp3sebENK756AhWXa92XsX-vBdpMzXrhvE-o1UvN0-shKC-BPU_bEQ0JxGAXsDv__FCUbt772ZQNqoUoNIVEbpB09k4Cxhv7jKgJW_eGGoXqOOyZyXHjVcuSNovFcl3hK_xqDReRbq1HueudwjjR61m-KgijpZmpYhEgO6ezYNVhn_SyFT99RjiMvsKHyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دانیال ایری با عقد قراردادی ۴+۱ ساله به پرسپولیس پیوست
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/456557" target="_blank">📅 15:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456556">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/630026d9ce.mp4?token=A75J10k6m_gyLGm2R1HL2f8zLb4lfUY9hEq-zjKGPBuwoj5fTxE_RK9pnKWu6FwfI0McCGDLgXNGG4b5cgQo8Y4ltyo9L_IKstzraXF_18SafLdTDlfOu5iKd6yJOspTFn92WPAhbOxb9KkFG7YMVRsQPR2zNg_gom4lEAvE_aZNC5lBLAtYVZl61emZd6_UihP5l2KIqu-ObL3LEmjXmbXCI6kj972sWM3NcbemJRLmA44VgvNoei9X2ra1LHzwFTXQEUYT9J8x8rh5o6gdU1hCrw6ovUt5b1pyifYoSaUAVr9MR8xfhG3MGXAI3TX6_bcPls_XZGGC2kjg3_4PEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/630026d9ce.mp4?token=A75J10k6m_gyLGm2R1HL2f8zLb4lfUY9hEq-zjKGPBuwoj5fTxE_RK9pnKWu6FwfI0McCGDLgXNGG4b5cgQo8Y4ltyo9L_IKstzraXF_18SafLdTDlfOu5iKd6yJOspTFn92WPAhbOxb9KkFG7YMVRsQPR2zNg_gom4lEAvE_aZNC5lBLAtYVZl61emZd6_UihP5l2KIqu-ObL3LEmjXmbXCI6kj972sWM3NcbemJRLmA44VgvNoei9X2ra1LHzwFTXQEUYT9J8x8rh5o6gdU1hCrw6ovUt5b1pyifYoSaUAVr9MR8xfhG3MGXAI3TX6_bcPls_XZGGC2kjg3_4PEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سبوس</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/456556" target="_blank">📅 15:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456555">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae7bcb0b00.mp4?token=D2Ck_IJdWSjbQUHBhe3KHjMr2QgIBJ8I9wnNyByTV3JE5AJ9qrNrqhtzF2Do74l8SDyA21R09nV6sFG6aRfJQ4ZZn09jl-0wkhFFbos9opnHBTTM7ijfkmUQgn--xsj31Of1bXNU7fG3M92OPOZHY0kOId53rdHeQw6UHVNwi7UUqbENtwypowtUHc1H5DvX90_BkgZ6GE82aiIeOtAsNRnR9-0bR9JnvOgntOJXREZbXJz9KUXIaU5y0sbRsF0tcPyQm5M04cJ-oo35ZwEzsOcxIhT5-uv3JeFI8b45f1gKypcRIvh32FC_qzzq8fpUSojuYhx1N2wpGvF_3fIi3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae7bcb0b00.mp4?token=D2Ck_IJdWSjbQUHBhe3KHjMr2QgIBJ8I9wnNyByTV3JE5AJ9qrNrqhtzF2Do74l8SDyA21R09nV6sFG6aRfJQ4ZZn09jl-0wkhFFbos9opnHBTTM7ijfkmUQgn--xsj31Of1bXNU7fG3M92OPOZHY0kOId53rdHeQw6UHVNwi7UUqbENtwypowtUHc1H5DvX90_BkgZ6GE82aiIeOtAsNRnR9-0bR9JnvOgntOJXREZbXJz9KUXIaU5y0sbRsF0tcPyQm5M04cJ-oo35ZwEzsOcxIhT5-uv3JeFI8b45f1gKypcRIvh32FC_qzzq8fpUSojuYhx1N2wpGvF_3fIi3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رکورد زدیم؛ البته در کاهش زادوولد!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/456555" target="_blank">📅 14:45 · 26 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
