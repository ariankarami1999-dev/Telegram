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
<img src="https://cdn4.telesco.pe/file/OmnSSnxanoCXCxHJckNwsPtokqW-sErO63vLTsE7iUJHcjh_x8CWZ7lqy8f-gmdUANYH0KEJsmXrM9vS2H3eIHvUruRnhVpWsbiglnCnCdlnOvOKn14kJ902aRBg_Ht3dNXuBY4hzjRlI6UAzfKGbnAMUuRk7VlcoN2rXHZv1CUBwzluD2tU4tlbp7zQFNniYy_6YCINDjH-ZTOfr2DtCvyULJ4dJfxUPHqf0PeBHyqZry3o6tCqCpUPToR1DFp-e0R6qpiUNQTwngh2nfU_i0EZVADl36EHeFOC3b_tsrw2EU58js78A1qSKgznmf-LqsemhfzobkIsRfYhdoauzg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.49M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 23:05:04</div>
<hr>

<div class="tg-post" id="msg-660538">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
فاکس نیوز: کشورهای خلیج ‌فارس از اعطای حق کنترل تنگه هرمز به ایران خودداری می‌کنند
فاکس‌نیوز، به نقل از یک مقام آمریکایی:
🔹
کشورهای حاشیه خلیج فارس از اعطای حق به ایران برای وضع عوارض بر عبور و مرور از تنگه هرمز خودداری می‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/akhbarefori/660538" target="_blank">📅 22:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660537">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
ادعای اکسیوس از انتشار متن کامل توافق ایران و آمریکا
🔹
متن کامل یادداشت تفاهم ایالات متحده و ایران، توسط یک مقام ارشد دولتی در جلسه توجیهی با خبرنگاران آمریکایی ارائه شده است.
🔹
این یادداشت تفاهم پایان جنگ را اعلام می‌کند، از ایران می‌خواهد تنگه هرمز را…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/660537" target="_blank">📅 22:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660536">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
رضایی، سخنگوی کمیسیون امنیت ملی مجلس: افرادی که برای مذاکره رفتند تمام تلاش خود را کردند
🔹
مسئولین حتما باید با مردم حرف بزنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/660536" target="_blank">📅 22:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660532">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نوحه</div>
  <div class="tg-doc-extra">حاج‌منصور ارضی قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/660532" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">پک هیئت قرار  ویژه شب سوم محرم
🖤
#محرم
محتوای مذهبی ویژه محرم در این کانال
👇🏻
👇🏻
@Heyate_gharar</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/660532" target="_blank">📅 22:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660531">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tygl7RACkK7CeU7CceJvVRlvAWIG6Mf6v3SvDDOGBMhRkF_qiLE4ixhtqwbhdoWnEPKpvrVpsc-yvtHgmIHuRodBPXMElZwZZHs2zCWKC34UXgFIfLAUefYcBQHHZXpg1dQTH6wq4ZQD4P9Fitv9F_Zv_CESrSzLLs8vUR3V6CNdQQMUVl_Uqq2aI97VG0BBlP4Mi0PVeLe9BsI0777QdLNoKuoNiJ6cfmIEH-cw-KjTmKFtFPSnS1QR752GbIUJOlFXmfM-3GT0PQCjJZfmds2LbOokVsDcfOF29YSzUDTz6ttw10qdIVDGmf3vFxN1xeCsNZszugxBujW9pYC0uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبکه خبر| انتشار متن تفاهم‌نامه ایران و آمریکا تا دقایقی دیگر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/660531" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660530">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsUkhWR8h-VlP9StbB5ueJ4BwMZ6u_7LxbjGLs2KqSjBZYNwH-jFGajd1waqnPE9bsOgm-xmhSxDUM7xbzioG2DH9_2IsoUWMvYfWsnNTdLXRqk1EzerRhcuqDXDbY1u-NdcUAZps1QDU-MQofP1x4FFo335cC8e-QrXhxR0PK8PM9i0BPB6ySAr-vEKPHB0pIicpXyCcEfDZOQXKVbymqr-OB6TikxKT4qYDFNmmRb6_hakfO1hBnXzBTwar5EqRLqWP7VqCYpsJn4ByDnwgSTI7aWS2sO9AMNLmJe5cR3T8zxZH5GYYIHoQ1uzwGv8ig2HyC07oqhztgsubA_GYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گل تساوی کنگو به پرتغال
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/660530" target="_blank">📅 22:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660528">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fX6hFTqBiLNpw4icbjvo-qcmE-n20mOSmZ2GyGrZ_v3eltrwVE-kqhnoa47wGH1uM762lRLweQ03JFo0JDbRhPWjQ9WPqEu-bIY8jjEOR0APhyg5W8anHG5Rk5mKxV09egCWpPAJlJvhV1lT3sLIp-dOiUfPaMiJDkMTqrEquuzlAtHjLtiB2RPmR8HpIqjUuE4Vnz_8GapsD3WHCikNifhGKl5PgQTyb4HHN67ycAD5jedvjkTsAkxaBmFlTb0ZjLPhXr20cQBFIG2X5V5CsDLNaLJUC8CjL-g-LTlLz1Pq4p1oJAC02glaLDPP_EUm0V2Y1dzD4HzUb-sebg_gJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ در قتل اپستین دست داشت؟ | جفری اپستین قبل از خودکشی، وسواس زیادی برای سرنگونی ترامپ داشت
🔹
بر اساس یک گزارش جدید که به اسناد و گفت‌وگوهای منتشرشده از روزهای پایانی زندگی جفری اپستین استناد می‌کند، این سرمایه‌دار بدنام آمریکایی در هفته‌های منتهی به مرگش در زندان به‌شدت در تلاش بود اطلاعاتی علیه دونالد ترامپ پیدا کند و از آن به‌عنوان ابزاری برای کاهش فشارهای قضایی استفاده کند.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3223625</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/660528" target="_blank">📅 22:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660527">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNQsrUIG_0gFn8mdaqVY_Tq3ABr5khjpjKVi1bpumth6DMJ_C6fpgen81RiNTT194ZGU35h7ICbAhOJ9w1iscrccvT2DohBjymlj3AEYLLhVmLZzye4A0OKM4Fo4xKxBpNpIiZjoh4axIvmuykaNioMw_6Onp4iwWe3PAvrPgcAkltmDz8qPea1XyQweJtGIfyQK0Ox4u6uR0fs00dV5IimbQkys9631ux1hH5MDiwtDoct6eXF4KF0qNDFX7hYwiCup53aLx0-0FNvbgm_pU0wMwFMKu4EGQVPbP9lP6FvvRtskoM6azYLW2V0K4pOZVtJS_5aZjpklbtx0lDHK4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویری از محل سقوط بمب‌افکن استراتژیک B-52 آمریکا در کالیفرنیا
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/660527" target="_blank">📅 22:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660526">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
منبع آگاه: پیشنهاد امضای الکترونیکی تفاهم‌نامه ایران و آمریکا پیش از سفر به ژنو مطرح شده است ‌
🔹
یک منبع آگاه نزدیک به تیم مذاکره‌کننده، از مطرح شدن پیشنهاد امضای الکترونیکی متن تفاهم‌نامه میان ایران و آمریکا پیش از سفر هیئت‌ها به ژنو خبر داد.
🔹
بر اساس این…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/660526" target="_blank">📅 22:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660525">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
مدیرعامل سایپا: مجوز افزایش قیمت نگرفته‌ایم
🔹
در صورت صدور مجوز افزایش قیمت، موضوع از طریق سامانه کدال به اطلاع خواهد رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/660525" target="_blank">📅 22:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660524">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8pjDoWdmOJCW-OgysdTC1NUgHcJxs_LYdnL3YfAXu1hjpVFU1sUYr0AizYGoAUbQHIpb4PXyXT6TgC7A6hZfwMTrlofKoREzJiRXLtEPwIhrf7oUHRpcgjIkpSgfxFxrsZzk3mHi0mTTX5ejCKHbf99_Uk4iDZ97qnsI0mvjEaXGz6Waag01cgCokJaFE2lIouXrFdzmVZR3VXWm6HsXfWUMrI6VEFSoulZXZ158MMYqfhm9BOHaPvDvfWpaOf3MpLMbs2MLNgAnIe6oPkSvIO2E-HGE-YkI1ce9uSsYLMJp0R-8tDr7ZTzmZ9k4dB1Q-imeUb6UtfHrK_V0Ri9uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اراده خداوند بالاتر از سخت‌ترین اراده‌ها
🔹
امام می‌گوید خدا را از گشوده شدن گره‌های سخت و شکستن تصمیم‌ها شناختم؛ انسان گاهی اراده‌ای محکم یا مانعی بزرگ دارد؛ اما ناگهان تغییر می‌کند. این نشان می‌دهد بالاتر از اندیشه و ارادۀ ما، ارادۀ قدرتمندتری وجود دارد…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/660524" target="_blank">📅 22:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660518">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a644bb4b89.mp4?token=No7cLHvOhO29zth5Z4cYzcVmCFytV63mI2EmfTbynd8eCQqvUhXup_wzCOhh9bDSqdYw7ynx3fg7Soa2Jfx1REr7lj7RTZxK-98AZywCATgBLd0grXC0CrNxyM3FyvjXoySN-4q1zOB3AucgEThBGGCvacMVJpGUHJiWXlGwYTWD7xNeT6mGbratW_ick1XC03eTC2mro56CUkX2FQ7xR7ts2kq-Pm30StRIZfaNperIx-29sxV3a6-xrNq7qW6Ce9TfPnz-_9pdrxaa0RmzPNHCklRw0rqUfvTuLlNwi1kdWgGjnI6xK5ZZpY0IvsbnWAqVgNxWQWVfzy0RiWNo5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a644bb4b89.mp4?token=No7cLHvOhO29zth5Z4cYzcVmCFytV63mI2EmfTbynd8eCQqvUhXup_wzCOhh9bDSqdYw7ynx3fg7Soa2Jfx1REr7lj7RTZxK-98AZywCATgBLd0grXC0CrNxyM3FyvjXoySN-4q1zOB3AucgEThBGGCvacMVJpGUHJiWXlGwYTWD7xNeT6mGbratW_ick1XC03eTC2mro56CUkX2FQ7xR7ts2kq-Pm30StRIZfaNperIx-29sxV3a6-xrNq7qW6Ce9TfPnz-_9pdrxaa0RmzPNHCklRw0rqUfvTuLlNwi1kdWgGjnI6xK5ZZpY0IvsbnWAqVgNxWQWVfzy0RiWNo5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
پک
#استوری
ویژه شب سوم محرم به یاد حضرت رقیه سلام الله علیها
🥀
شمع ها می سوزد و زخمی ترین پروانه ام
عطر نان تازه دارد غنچه ی پیمانه ام
شانه های کوچکم از بس که می لرزد دگر
عمه زینب سر نمیذارد به روی شانه ام
محتوای مذهبی ویژه محرم در این کانال
👇🏻
👇🏻
@Heyate_gharar</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/660518" target="_blank">📅 22:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660517">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnK50JsXgyJq1CyQUA1qCOeb4wBgMZk2-5WC-Ka7pfsRleiZ_EnDqPT-QK3qH1tjB2KhPKHuv0UTRTfMZfDb687lI_zAeGCkV-QVDF1HFlIax-PiTP4ewg8nhvjC3X8vEVgZ_ditBxRrLU2JcQIfm_LapA1mbz94K2tcEL_14HhsBe_GVB9tHIF5MUK306d87NmDDc8yA-tjarpxmK-TIellTmdyO2WS5d6J-5FsV7HCI1gb27uPgfFYNTi_PKRljdiRkAvPBo1Kc7z0sR-Q-T-y_R-iI4Ayt45u3s9uXetIzvMWmevgZjZImJ-29ltjUzwz-mrbuUgOT5TkSwIexA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍺
بهنوش ایران در نمایشگاه ایران آگروفود ۲۰۲۶ حاضر شد
▫️
شرکت بهنوش ایران در سی‌وسومین دوره نمایشگاه بین‌المللی ایران آگروفود ۲۰۲۶، تازه‌ترین محصولات و برنامه‌های توسعه‌ای خود را معرفی می‌کند.
▫️
همزمان با این رویداد، بهنوش از محصولات جدید خود در دو گروه «دلستر» و «آب‌گازدار طعم‌دار» رونمایی خواهد کرد. همچنین کمپین «جام اینجاست» به مناسبت جام جهانی فوتبال و حضور تیم ملی ایران، همراه با برنامه‌های ویژه و اهدای جوایز در سالن خلیج فارس برگزار می‌شود.
▫️
علاقه‌مندان می‌توانند از غرفه بهنوش در سالن خلیج فارس بازدید کنند.
▫️
مشروح خبر
khabarfoori.com/fa/tiny/news-3223870</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/660517" target="_blank">📅 22:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660516">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
مقام آمریکایی: توافق با ایران از طریق قطعنامه شورای امنیت تصویب می‌شود
یک مقام ارشد آمریکایی:
🔹
یک سازوکار اجرایی برای نظارت بر اجرای یادداشت تفاهم‌ میان ایران و آمریکا و تعهد هر دو طرف به توافق نهایی در آینده ایجاد خواهد شد.
🔹
ارتباط بین تهران و واشنگتن، شاید به‌طور ساعتی یا روزانه وجود دارد، اما اعتماد بین آنها همچنان بسیار ضعیف است.
🔹
تا زمان دستیابی به توافق نهایی، ایران وضعیت برنامه هسته‌ای خود را حفظ خواهد کرد و هیچ تحریم جدیدی اعمال نخواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/660516" target="_blank">📅 21:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660515">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: دربارهٔ اموال مسدودشدهٔ ایران، طرف آمریکایی تعهد داده که موانع را رفع کند
🔹
بخشی از مذاکرات در این باره انجام شده است. برای ما مهم است که به اموال ملت ایران دسترسی داشته باشیم این که به چه نحوی باشد جزو تعهدات آنان است.
🔹
در این مرحله…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/660515" target="_blank">📅 21:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660514">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
بروزرسانی قیمت محصولات ایران‌خودرو معادل حدود نصف نرخ تورم/خودروهای اقتصادی ایران‌خودرو کمترین افزایش قیمت را تجربه کردند
🔹
بررسی اطلاعات منتشرشده درباره قیمت‌های جدید محصولات ایران‌خودرو نشان می‌دهد میانگین افزایش قیمت خودروهای اقتصادی این شرکت حدود ۲۵ درصد و در محصولات میان‌رده حدود ۳۵ درصد خواهد بود.
🔹
این در حالی است که طی ماه‌های گذشته هزینه‌های تولید خودرو شامل مواد اولیه، قطعات، دستمزد، حمل‌ونقل و سایر نهاده‌های تولید رشد قابل توجهی را تجربه کرده‌اند.
🔹
بر اساس اطلاعات موجود، الگوی اصلاح قیمت‌ها به‌صورت پلکانی طراحی شده و کمترین افزایش به خودروهای پرتیراژ و اقتصادی اختصاص یافته است؛ در مقابل، بخش عمده تغییرات مربوط به خودروهای اتوماتیک و محصولات جدیدتر خواهد بود.
🔹
کارشناسان معتقدند به‌روزرسانی دوره‌ای قیمت‌ها می‌تواند به حفظ پایداری تولید، تامین قطعات و تداوم برنامه‌های افزایش عرضه در بازار کمک کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/660514" target="_blank">📅 21:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660513">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‌
♦️
سخنگوی وزارت خارجه: تعهد ما این است که در مدت مشخصی، ترافیک دریایی را تنگهٔ هرمز به حالت عادی برگردانیم
🔹
این مربوط به خود ماست و نیازی به مشارکت یا مداخلهٔ طرف‌های دیگر نخواهد بود.
🔹
برای تدوین سازوکار مدیریت تنگهٔ هرمز و خدمات دریایی، ایران و عمان همکاری…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/660513" target="_blank">📅 21:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660512">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: ایدهٔ امضای یادداشت تفاهم اسلام‌آباد توسط روسای جمهور ایران و آمریکا درحال بررسی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/660512" target="_blank">📅 21:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660511">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3ebnNeHGIMtDMBJo2A2p4sWT-4vl67sRuN_gLKAdwVUkNXnENY8keVq0WvYXdi5S6lGGqr_TGXXLByAmwsBEaC8f0hXIGNKot6oV8CV5mQpWPtm-LgFCEMsURtmpj5A1njqWyKfmLcUoGrqQ60CKO_Sh3YTfdM2H9ZtSrRcb_2IZ5jdNnmDmQH84WRlixTzqtt4mrzX80XeRu5qnc1zv5S8Injyfujb7ZhIhKOIuWrZx4B17pJJshFg2c4QNodlNqMnnKubDA40ACreZRxKpzPYQJ97fi7vfDguK9FNX1Mcbk5nru1lIMt4yyrvTR8rjVzzOQdH7Zm-pLmmHeyqOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ازکی: از هر ۳ بازدید بیمه بدنه در ازکی، ۱ مورد توسط خود کاربر انجام می‌شود
🔹
داده‌های ازکی، به‌عنوان بزرگ‌ترین پلتفرم فروش آنلاین بیمه در کشور، نشان می‌دهد حدود یک‌سوم بازدیدهای بیمه بدنه در سال گذشته توسط خود کاربران و بدون مراجعه حضوری انجام شده و این سهم در اسفند ۱۴۰۴ به ۴۲ درصد رسیده است.
🔹
ارزش اصلی این قابلیت زمانی بیشتر نمایان می‌شود که کاربر در روزهای تعطیل یا خارج از ساعات اداری قصد خرید بیمه بدنه دارد. در چنین شرایطی، به جای توقف فرایند خرید و انتظار برای بازدید حضوری، کاربر می‌تواند تصاویر خودرو را ثبت کرده و خرید خود را تکمیل کند.
https://www.titrtejarat.com/fa/tiny/news-10218
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/660511" target="_blank">📅 21:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660509">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
منبع آگاه: پیشنهاد امضای الکترونیکی تفاهم‌نامه ایران و آمریکا پیش از سفر به ژنو مطرح شده است ‌
🔹
یک منبع آگاه نزدیک به تیم مذاکره‌کننده، از مطرح شدن پیشنهاد امضای الکترونیکی متن تفاهم‌نامه میان ایران و آمریکا پیش از سفر هیئت‌ها به ژنو خبر داد.
🔹
بر اساس این…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/660509" target="_blank">📅 21:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660508">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c851e52224.mp4?token=Y1gjdCl6sTYmczQvj3f6gduOX7o2kdis7aaNWrqwFKVsNflomL0eiWEHOE2v0CyBGeWiWL3CYRma94hwohVgs38TBYcWh_0CFTcvyzBkk8KUTIVEdhraP67vFGpqDwLUebFenG9F6Bhjy3Xnaf4y2r7NUyzokF38H4DFNxEWd340oiONr2OtVfefCLg3K0A6pqS_Oa2brukqraL4-TxQHh1CYQsc41_8p7K20hbQqRb3QViroueW-vSfPAJ176T4Gq5QxcIWCzrOMH1wSYgOlb9x-g0B4mbkcM3ySlMBWxyHV_3C3Jfbtd7Kv6EQZtK-AZEOzuvNN0tWTpDoFhZnBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c851e52224.mp4?token=Y1gjdCl6sTYmczQvj3f6gduOX7o2kdis7aaNWrqwFKVsNflomL0eiWEHOE2v0CyBGeWiWL3CYRma94hwohVgs38TBYcWh_0CFTcvyzBkk8KUTIVEdhraP67vFGpqDwLUebFenG9F6Bhjy3Xnaf4y2r7NUyzokF38H4DFNxEWd340oiONr2OtVfefCLg3K0A6pqS_Oa2brukqraL4-TxQHh1CYQsc41_8p7K20hbQqRb3QViroueW-vSfPAJ176T4Gq5QxcIWCzrOMH1wSYgOlb9x-g0B4mbkcM3ySlMBWxyHV_3C3Jfbtd7Kv6EQZtK-AZEOzuvNN0tWTpDoFhZnBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شاید برای امضا توافق در اروپا بمانم ولی لازم نیست
🔹
خبرنگار: برای مراسم امضای این توافق صلح با ایران نمی‌مانید؟
🔹
ترامپ:  شاید بمانم. اما این یک تفاهم‌نامه است. ممکن است از آن نوع اسنادی نباشد که من باید امضا کنم. اگر درست پیش نرود، تقصیر را می‌اندازم گردن…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/660508" target="_blank">📅 21:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660507">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
معاون وزیر ارتباطات: کشور به سطحی از بلوغ رسیده که حتی در شرایط بحرانی و التهابات شدید نیز می‌تواند بدون قطع اینترنت مدیریت شود؛ دیگر شاهد قطع اینترنت نخواهیم بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/660507" target="_blank">📅 21:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660506">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
ترامپ: یک نسخه از تفاهم را برای اسرائیل هم فرستادیم #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/660506" target="_blank">📅 21:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660505">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
قیمت جدید کارخانه ای محصولات ایران‌خودرو
🔹
لیست قیمت جدید کارخانه‌ای محصولات ایران خودرو ویژه نیمه دوم خرداد ماه ۱۴۰۵ از سوی این شرکت اطلاع رسانی شد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/660505" target="_blank">📅 21:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660504">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdxLKY_E0rsl-opwyYh2sHR9x6ketW0guOPw2DBFFPVzJTE9ClQ_JBB5VJ4V5eF4ThGCU0ijk-_xc78vDpExwi_jPDZou782WmIyiLxVHqIhEqslm1mIqfQMET9G7pXfW2E8f-u-EGBWsn8ObgIUnaKDrRFJBegPqjaAkGZaYLUV2V3kC08mNcxo3-UCCxEsdOp9uZoAYoBpXyI8BIPlLkFJWi8LcdmFtijZBvDSmvIszu82zYZHFolb0ysfmGbRepYn0iM1qm07UiRl92rJAELKXzicZUSsdbMIdp45-wWZz2RhVPJZ9ebR1M3mdCFTFBQ9QQXLuwq2RI4b18Dc7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیشنهاد مسیر تشییع رهبر شهید انقلاب در تهران/ اهمیت پوشش رسانه‌ای در مورد این اتفاق تاریخی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/660504" target="_blank">📅 21:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660503">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e5a81c71e.mp4?token=Ndd_RfWWkE8RCUBYuMKam59Pk3_lyRjsMNYoEXMsKimyW-nxbbZ2FtDrXa8qZaV_U7W7WV3ReDL7cSaPn9ebmwrvue44lEBhjShm98tzOZSWvLNHdywtzCZps2yQ5KNCyzDPwWfWt2aErgAOcv-avouw3kXeruBHN8NdnnyG0-nA2LmLb8eDBZ--DrhagvhtboWT7nEaCVhf_ze2W4NxpKNj-PHprdOFO95NKya9goK6AGsosPZmCg2gQVhYEdjWreH5IqibrO1uziZCWobRQxqFOSEaoB75XxcinIidSTEn3F0DOzkWflNQfvXxLlvrLb3dNM0Y03Roe3UpgLuXfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e5a81c71e.mp4?token=Ndd_RfWWkE8RCUBYuMKam59Pk3_lyRjsMNYoEXMsKimyW-nxbbZ2FtDrXa8qZaV_U7W7WV3ReDL7cSaPn9ebmwrvue44lEBhjShm98tzOZSWvLNHdywtzCZps2yQ5KNCyzDPwWfWt2aErgAOcv-avouw3kXeruBHN8NdnnyG0-nA2LmLb8eDBZ--DrhagvhtboWT7nEaCVhf_ze2W4NxpKNj-PHprdOFO95NKya9goK6AGsosPZmCg2gQVhYEdjWreH5IqibrO1uziZCWobRQxqFOSEaoB75XxcinIidSTEn3F0DOzkWflNQfvXxLlvrLb3dNM0Y03Roe3UpgLuXfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل تساوی کنگو به پرتغال
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/660503" target="_blank">📅 21:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660502">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
منبع آگاه: پیشنهاد امضای الکترونیکی تفاهم‌نامه ایران و آمریکا پیش از سفر به ژنو مطرح شده است
‌
🔹
یک منبع آگاه نزدیک به تیم مذاکره‌کننده، از مطرح شدن پیشنهاد امضای الکترونیکی متن تفاهم‌نامه میان ایران و آمریکا پیش از سفر هیئت‌ها به ژنو خبر داد.
🔹
بر اساس این پیشنهاد، متن تفاهم‌نامه پیش از عزیمت طرفین به ژنو به‌صورت الکترونیکی امضا شود تا نشست‌های ژنو بر بررسی جزئیات فنی و مباحث تخصصی مرتبط با دوره ۶۰ روزه پس از حصول تفاهم متمرکز باشد.
🔹
هدف از این پیشنهاد، تسریع در روند ورود به مرحله اجرایی و جلوگیری از اتلاف زمان در مذاکرات آتی عنوان شده است.
🔹
وی در عین حال تأکید کرد که تا این لحظه جمهوری اسلامی ایران موافقت خود را با این پیشنهاد اعلام نکرده است./فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/660502" target="_blank">📅 21:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660501">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJT0LlwxbjYG6XDGoefSmEqSwfZE2TiMCvq7VtBSYoBd4GfC4QEVCnXGURlC1U5aoOHRqHTFQIAuXoD7r6_mIyFYS6V0ZAD5IVSqsT0ewS0qP25xdweioJcs42zdH6MGxKQDoWKsBTJQLJmCy9NKTOw1h4buU1aBIY5AtVcySMPEeHh84kB7xQdnLqtcq3v2IwGj9eUj1HXkAuByTkjQuVlKkqizOCa35ZW106cAVPLONx_YvhK6cenRFcmDaE8CeiR7hpB81OQ-_Q7BQB-_dxqkZTfpFKfbnT-JR8w0RcWsyh-H4-9YH4gGDOChcNnGWFVbDUux4pw2gM-7a3YoFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آماده شدن چین برای جنگ بزرگ با آمریکا/ ارتش پکن «فضایی» می شود/ این سلاح چین «آمریکا» را به وحشت می اندازد
🔹
روزنامه «هوانکیو دیلی» گزارشی در مورد آزمایش آتش واقعی سامانه جدید دفاع هوایی چین یعنی «هونگژی-اف۱۶» منتشر کرد که این گزارش جهش قابل توجهی را در قابلیت‌ های دفاعی ارتش چین آشکار می ‌کند.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3223746</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/660501" target="_blank">📅 21:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660500">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bf5e67b4e.mp4?token=dLl0N0LRrn-n0Mz62mC2peBuMAoTbmon9o_jGi0xSzhVfQW6ABEKWHQ4jJenVTVJvUapRXlZkSLOwDRldobWwSaNLs_kIsJG05OryRzg6JPBLz1N3_IeuJW8OqhQ9S-t0n60WcMwA8Y8w3hHyaJDepAslZzpQ1SbFbW26Ui2S3jhVilvK4dWojg6rqOp1XYsrCFYG2e0xYYcMN9VsJMmNNjs6YlGz3cIeZDLXVEtMaMe2VZ3f4vfBKbrjslAGXEm6e_z2ZHOewvYufXGSbv9um2xL5hmiCUOLdyqd0YF8cfk2mdZ9gIKDJ41DDigkO4NkuHxV_pEqGdHs8gD3lafjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bf5e67b4e.mp4?token=dLl0N0LRrn-n0Mz62mC2peBuMAoTbmon9o_jGi0xSzhVfQW6ABEKWHQ4jJenVTVJvUapRXlZkSLOwDRldobWwSaNLs_kIsJG05OryRzg6JPBLz1N3_IeuJW8OqhQ9S-t0n60WcMwA8Y8w3hHyaJDepAslZzpQ1SbFbW26Ui2S3jhVilvK4dWojg6rqOp1XYsrCFYG2e0xYYcMN9VsJMmNNjs6YlGz3cIeZDLXVEtMaMe2VZ3f4vfBKbrjslAGXEm6e_z2ZHOewvYufXGSbv9um2xL5hmiCUOLdyqd0YF8cfk2mdZ9gIKDJ41DDigkO4NkuHxV_pEqGdHs8gD3lafjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: ذخایر نفت آمریکا ۴ هفته دیگر تمام خواهد شد   رئیس‌ دولت تروریستی آمریکا:
🔹
ذخایر نفت ما حدود ۴ هفته دیگر تمام می‌شود. ذخایر نفتی در سراسر جهان وجود دارد. ذخایر ما واقعاً تمام خواهد شد. #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/660500" target="_blank">📅 21:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660499">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
بقایی: احتمال امضای تفاهمنامه توسط روسای جمهور ایران و آمریکا مطرح است
🔹
برنامه‌های ایران برای نشست ژنو تغییری نکرده است
🔹
سخنگوی وزارت امور خارجه اعلام کرد تا این لحظه هیچ تغییری در برنامه‌های ایران برای برگزاری نشست ژنو ایجاد نشده است.
🔹
وی همچنین در خصوص…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/660499" target="_blank">📅 21:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660498">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33b73a6021.mp4?token=rvQVWo9Sy6R0i_15v_TCkh7u5KIyPhAYr_XcbU8vEuMr8VxibIhQS8I0sf8zpqF4Kom_XrlHWcrE2XvVhJRi4WmAKY0TSoZaVPLO9k1Ln-q6TcK1C8bzW8vhXyHkFD3qJX2OEJ4N2r1BJch6KAksPjm6V2YFjwLrzBLCjWdgedIr7r9Cw8d-uWyHkNjC0mLg0QRxccfgkmAwUf92mPccDKODFWFsKqxUJZrD0cU1kEzAV4dBY2iyHMSYSVCyW5gZv_fsZOC5YMx7EC5pLrKQr9KISbDI1UixgPrH6Tb5qBNkbyTHHTrJ3mPeNKUz7yzv4fLzfE6hD1ODOsvfQUYVBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33b73a6021.mp4?token=rvQVWo9Sy6R0i_15v_TCkh7u5KIyPhAYr_XcbU8vEuMr8VxibIhQS8I0sf8zpqF4Kom_XrlHWcrE2XvVhJRi4WmAKY0TSoZaVPLO9k1Ln-q6TcK1C8bzW8vhXyHkFD3qJX2OEJ4N2r1BJch6KAksPjm6V2YFjwLrzBLCjWdgedIr7r9Cw8d-uWyHkNjC0mLg0QRxccfgkmAwUf92mPccDKODFWFsKqxUJZrD0cU1kEzAV4dBY2iyHMSYSVCyW5gZv_fsZOC5YMx7EC5pLrKQr9KISbDI1UixgPrH6Tb5qBNkbyTHHTrJ3mPeNKUz7yzv4fLzfE6hD1ODOsvfQUYVBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارشگر: یک مرد دانا زمانی گفته بود، در ژانویه ۲۰۲۰، ایران هرگز جنگی را نبرده اما هرگز مذاکره‌ای را هم نباخته است
🔹
ترامپ: این را چه کسی گفته؟
🔹
گزارشگر: دونالد ترامپ! #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/660498" target="_blank">📅 21:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660497">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
بقایی: احتمال امضای تفاهمنامه توسط روسای جمهور ایران و آمریکا مطرح است
🔹
برنامه‌های ایران برای نشست ژنو تغییری نکرده است
🔹
سخنگوی وزارت امور خارجه اعلام کرد تا این لحظه هیچ تغییری در برنامه‌های ایران برای برگزاری نشست ژنو ایجاد نشده است.
🔹
وی همچنین در خصوص احتمال امضای یادداشت تفاهم توسط رؤسای جمهور دو کشور اظهار داشت: «این ایده مطرح است و همچنان در حال بررسی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/660497" target="_blank">📅 21:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660496">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
حزب‌الله عراق: نبرد پایان نیافته؛ دست بر ماشه هستیم
ابوحسین الحمیداوی، دبیرکل کتائب حزب‌الله عراق:
🔹
نبرد تمام نشده و مراحل خطرناک‌تری در پیش داریم؛ لذا وظیفه ماست که با دست گذاشتن بر روی ماشه، برای هر پیش‌آمدی آماده باشیم.
🔹
این دشمنان، وحوش بشری هستند؛ اعتماد به آن‌ها یا غفلت از مکرشان، عین حماقت است.
🔹
معادله روشن است و آن‌ها هرگز از ما راضی نخواهند شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/660496" target="_blank">📅 21:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660495">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e92fb48380.mp4?token=cW1UojoL0MjGv877CfOH4eqPBH1bXroX5weKdJadHsyTSnMLM6dcAe-I50M_w-0_UBw5Mu7SRPmY9dp0CIAYNHwD4ST1FjDIiijv-ub6a82sKEj886v0h_U0wyg9_KsLxB-oY6JndwI_YszQhVHMStPOhKIdi6rKPRK9guFU02IGDnbpjWh-sGGg8S7YEQXTZxbYle8pMe0IXId5JY8k-DoQDv1PCHW8hevphMV8F5IeWnVnpZZ1qG21JI8zl5C3A0NFs9ZksHsgBEH2TRLrFfQSg8RbahkwNXAACVIwZCTaXYixIcI3hJ0f-TtMqf23OMQ6wAu_WfoTe6Oun-C60w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e92fb48380.mp4?token=cW1UojoL0MjGv877CfOH4eqPBH1bXroX5weKdJadHsyTSnMLM6dcAe-I50M_w-0_UBw5Mu7SRPmY9dp0CIAYNHwD4ST1FjDIiijv-ub6a82sKEj886v0h_U0wyg9_KsLxB-oY6JndwI_YszQhVHMStPOhKIdi6rKPRK9guFU02IGDnbpjWh-sGGg8S7YEQXTZxbYle8pMe0IXId5JY8k-DoQDv1PCHW8hevphMV8F5IeWnVnpZZ1qG21JI8zl5C3A0NFs9ZksHsgBEH2TRLrFfQSg8RbahkwNXAACVIwZCTaXYixIcI3hJ0f-TtMqf23OMQ6wAu_WfoTe6Oun-C60w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: طی دو سال گذشته همکاری خوبی بین وزارت خارجه و صداوسیما در حوزه‌های مختلف وجود داشته است
🔹
امروز با توجه به شرایط جدیدی که الان در صحنه دیپلماسی وجود دارد، لازم است که هماهنگی بیشتری با هم داشته باشیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/660495" target="_blank">📅 21:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660494">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMu1GPHKJ-bcZUkFBRV_Obh-eBJDzjMKLKlv1b3octphxWmBcz23X62Lhuinv3rA-NdVhGXvaQ0x7z8w7aKeTMrjfE_qx7xwy3QI-jJPj7Ymdww-nj52OviXyEpO-_XjjVe1mL90ZIVyHwYsc38VPTeodelx7nGvgliHgidXsdq3Y5oFZDhmdRgYOUHk9F76l_I8sq4O2Tju-4F89VU3wx5tgsklG-xwgxzb4w-04GMwqW3eYeIW6fC5aSxDWVo8vWFAzu_vqzKSlh3lqn4usL5ojRNeQG8NNjrgRVIXqCE3UWPj2FPfN6sdlGyeFysgWAkJ6W-u6ykiMA-zQ57JQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بودجه فرهنگی ایران در مقایسه با منطقه
🔹
ترکیه با ۹.۱ میلیارد دلار و عربستان و امارات با ۶.۴ و ۴.۳ میلیارد دلار، بخش قابل توجهی از بودجه فرهنگی خود را به پروژه‌های توسعه‌محور اختصاص داده‌اند.
🔹
بودجه فرهنگی ایران ۰.۸۵ میلیارد دلار و معادل ۱.۷ درصد از بودجه عمومی است که بخش عمده آن صرف هزینه‌های جاری و اداری و حفظ ساختارهای موجود می‌شود.
🔹
در بسیاری از کشورهای منطقه، سرمایه‌گذاری فرهنگی بیشتر بر احیای میراث، صنایع خلاق و صادرات محصولات فرهنگی و سریال‌ها متمرکز شده است.
@amarfact</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/660494" target="_blank">📅 21:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660493">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21dff10eb3.mp4?token=o_2gR855U6_1CCcs331ruCR8Re2eewepbD5k6vU92A0zn-20cnOF8l061UiyWmLZv81XuPGLJwh957WCIQOrgyXbeQmHHM6flh-hY0oFKJEA-O6vknsIAh7NQj78155jfz7xEKf9eD_JTMZ6BFsa3tyWISqiYlpVt-ONGRWSrvVSmZPAc5-g1zI79MDp9QWjah0t0WUoraczWRUWn_Jd9K3MmjX7UgWbC7lLcrZA6-01hcJYW-L8-yugYRLVG7Z79BRfePARvAHngHUivwoGwtpnrelaoq6YIyoPDS5iDzcGJlwz1_IOaIjTuDDzJ2IccQJl8Y-gnt8YSgFC4aOwLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21dff10eb3.mp4?token=o_2gR855U6_1CCcs331ruCR8Re2eewepbD5k6vU92A0zn-20cnOF8l061UiyWmLZv81XuPGLJwh957WCIQOrgyXbeQmHHM6flh-hY0oFKJEA-O6vknsIAh7NQj78155jfz7xEKf9eD_JTMZ6BFsa3tyWISqiYlpVt-ONGRWSrvVSmZPAc5-g1zI79MDp9QWjah0t0WUoraczWRUWn_Jd9K3MmjX7UgWbC7lLcrZA6-01hcJYW-L8-yugYRLVG7Z79BRfePARvAHngHUivwoGwtpnrelaoq6YIyoPDS5iDzcGJlwz1_IOaIjTuDDzJ2IccQJl8Y-gnt8YSgFC4aOwLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روبیو انگلیسی را به انگلیسی برای ترامپ ترجمه کرد
🔹
ترامپ به سوالی از یک خبرنگار ژاپنی پاسخ می‌دهد اما با وجود اینکه آن خبرنگار انگلیسی را با لهجه صحبت می‌کند، نمی‌تواند حرف‌هایش را بفهمد، بنابراین مارکو روبیو مجبور می‌شود به عنوان مترجم انگلیسی به انگلیسی…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/660493" target="_blank">📅 21:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660492">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48f3dd6944.mp4?token=biGOi0ok-vf7EFLgz5Y6nbdF5n94kmrEEceXYVE1X4Czm3GDfDMxAXoBnd2YAXZthIFdaQ30SszYtWYDLkFCPgz2N-TWGu0TUnGyKvPadzdGDXhQUp8kR_2mTs4owhMh-giyRvT_e5cCPzJryPKzRERnY89dTQvziB5xYwd0QCJ9W1SoRM7c4aNf9H7h5JJKcPU6c3wQavzVVzbfO8DATOum3XafZxzqhjWo-Y-D65Wnpb0KZe_HgBpTELVPkzEngwVx0e_X0NmiKrmVNSCEY2VwEDBWNcaC7NhzlubVD3dVcmaAwaEA1RgJfUmxpWyuDsFZzu5oK1tunitdl5t8TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48f3dd6944.mp4?token=biGOi0ok-vf7EFLgz5Y6nbdF5n94kmrEEceXYVE1X4Czm3GDfDMxAXoBnd2YAXZthIFdaQ30SszYtWYDLkFCPgz2N-TWGu0TUnGyKvPadzdGDXhQUp8kR_2mTs4owhMh-giyRvT_e5cCPzJryPKzRERnY89dTQvziB5xYwd0QCJ9W1SoRM7c4aNf9H7h5JJKcPU6c3wQavzVVzbfO8DATOum3XafZxzqhjWo-Y-D65Wnpb0KZe_HgBpTELVPkzEngwVx0e_X0NmiKrmVNSCEY2VwEDBWNcaC7NhzlubVD3dVcmaAwaEA1RgJfUmxpWyuDsFZzu5oK1tunitdl5t8TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ اصابت موشک به مدارس در جنگ را توجیه می‌کند
🔹
در جنگ، اتفاقات وحشتناکی رخ می‌دهد. همانطور که اشاره کردید، مدرسه مورد اصابت قرار می‌گیرد. چیزهای دیگری هم مورد اصابت قرار می‌گیرند. اتفاقات بدی در جنگ رخ می‌دهد
🔹
جنگ جای بدی است. من آن را می‌بینم. من آن…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/660492" target="_blank">📅 20:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660491">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403de8ea87.mp4?token=AvmEMQSZryznG9defutNqeSrwlsGKty8N3fhiCvK8bjDcGaGZCMeGzUh0X1uo_wC_F9pYFRoDbrlvd7FI1zShuCJSW1cVf42wH0zk0NU1aTykmP_ZOvr1xmMFP9orEb63gSJYH20JITfPjIomQALcVmAfF_QvdXsgOauvWTWEXduF2OzZqHYlwSGsyPd9IguN_igYWQZM94ZWe7r9LNMtbAKOj9IMmKrQwkFv4p4S1qlW15eJLtVDypkes-JT_6n7QYvzUMtK48qwkhWVVz6cbv9euLpyWqZP6E8rfDn_4xKUCOm-q1h8-HDAW_bB1P43RsNSLzL1DeD6QJMn9BKuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403de8ea87.mp4?token=AvmEMQSZryznG9defutNqeSrwlsGKty8N3fhiCvK8bjDcGaGZCMeGzUh0X1uo_wC_F9pYFRoDbrlvd7FI1zShuCJSW1cVf42wH0zk0NU1aTykmP_ZOvr1xmMFP9orEb63gSJYH20JITfPjIomQALcVmAfF_QvdXsgOauvWTWEXduF2OzZqHYlwSGsyPd9IguN_igYWQZM94ZWe7r9LNMtbAKOj9IMmKrQwkFv4p4S1qlW15eJLtVDypkes-JT_6n7QYvzUMtK48qwkhWVVz6cbv9euLpyWqZP6E8rfDn_4xKUCOm-q1h8-HDAW_bB1P43RsNSLzL1DeD6QJMn9BKuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ درباره جنگ ایران: از پوتین و شی تشکر ویژه می‌کنم، بیشتر از تصورم بی‌طرف ماندند #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/660491" target="_blank">📅 20:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660490">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb83298358.mp4?token=YGMGxX4XRQt1Z3AcfuLdMDTdCQH4y3D0JmGnGv6XjfknF730i0QKKLui3mR8K7gaK-tzD4yviHAnBXphBsOJevK_i9WV8GaxJTE0IK2oVRoqFemHaPnb92AhDgSCmgqRLUVVzMHR9wQZaYOtS3jGsLrdwUDoAXkUIfLagsJkRxmIRqKfXRHBNQ37zo6svfzAZWe2PwQIlhwGducoFXNTyoWIg1GqfzmUw-nOF2e3wDALIxaMiJpTEfudTJf0h809WaCjA6jNKZq985a1t95PYsBgBMUtnwS-SvO23Rkucy9RCEsPFGh23iroFS-QkaXLOo5OdZ9h2InEsX0WsT1V6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb83298358.mp4?token=YGMGxX4XRQt1Z3AcfuLdMDTdCQH4y3D0JmGnGv6XjfknF730i0QKKLui3mR8K7gaK-tzD4yviHAnBXphBsOJevK_i9WV8GaxJTE0IK2oVRoqFemHaPnb92AhDgSCmgqRLUVVzMHR9wQZaYOtS3jGsLrdwUDoAXkUIfLagsJkRxmIRqKfXRHBNQ37zo6svfzAZWe2PwQIlhwGducoFXNTyoWIg1GqfzmUw-nOF2e3wDALIxaMiJpTEfudTJf0h809WaCjA6jNKZq985a1t95PYsBgBMUtnwS-SvO23Rkucy9RCEsPFGh23iroFS-QkaXLOo5OdZ9h2InEsX0WsT1V6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هیچکس در دولت ترامپ پاسخگوی کشتار دانش‌آموزان میناب نیست
🔹
خبرنگار:  حالا که به مرحله جدیدی از این درگیری در ایران نزدیک می‌شوید، می‌توانید بگویید که آیا کسی را در دولت خود به خاطر حمله به مدرسه‌ای که بیش از ۱۰۰ کودک را کشت، پاسخگو خواهید دانست یا خیر؟
🔹
ترامپ:…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/660490" target="_blank">📅 20:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660489">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8911e65b3.mp4?token=VH_ZAT5YvNUALa-h9h_2vAfTP_C2x4EQ597WWAhreNPxUOBD8UWpvlA_QRGT3QFWDN6XItCC24lAyQlGfIEytRGyauGXm10EuQpJdspiMS9uQ1UemSPiGAtIJi2ySf1tOGwquNa2sdYKnyqZ4QCRnM5bG2r6g92t4hnjhdw9CM3d22lYUbDEwAgfB-6U8VmsBYjKHHSL1sAiJT4SkJMH7b9VEO6RbUhTYcx7pLQ-Exy-ZVHqADUbSt6lF1zUbHI6URfepfRMhKgn_69v74lM5DkG2DPqh_JO8ckD9hg73fh4WvVMsf3eW0CaqqDwVKrNk9eWhqKr2eSPWdca9bnxsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8911e65b3.mp4?token=VH_ZAT5YvNUALa-h9h_2vAfTP_C2x4EQ597WWAhreNPxUOBD8UWpvlA_QRGT3QFWDN6XItCC24lAyQlGfIEytRGyauGXm10EuQpJdspiMS9uQ1UemSPiGAtIJi2ySf1tOGwquNa2sdYKnyqZ4QCRnM5bG2r6g92t4hnjhdw9CM3d22lYUbDEwAgfB-6U8VmsBYjKHHSL1sAiJT4SkJMH7b9VEO6RbUhTYcx7pLQ-Exy-ZVHqADUbSt6lF1zUbHI6URfepfRMhKgn_69v74lM5DkG2DPqh_JO8ckD9hg73fh4WvVMsf3eW0CaqqDwVKrNk9eWhqKr2eSPWdca9bnxsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در مقطعی مجبور هستیم پول بلوکه شده ایران را پس بدهیم
🔹
خبرنگار:  می‌توانید توضیح دهید تفاوت بین دادن دلار آمریکا به ایران و آزاد کردن دلارهای بلوکه‌شدهٔ آمریکا چیست؟
🔹
ترامپ:  ما پولشان را گرفتیم و بلوکه کردیم… در مقطعی حدس می‌زنم مجبور باشیم پس بدهیم. اگر…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/660489" target="_blank">📅 20:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660488">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344296f6e6.mp4?token=dT5gZOT9dEHjC5NQ6w1QK07Q_J_oTfPY38I4XMxgyV5H-icOaq_6FfeY0VgCixZ-vheopDcEB4-3uRXw38rMoWx6UXcmkVt2W1PCfVYJre01oqB_yaAzirQLzsGvW5Dhb6eal9oP-1FhWn8csEt5qoctnF86-_N-ll7no0wI6dGBbj9_EPW0LnXeEF1vhnfk-X8l_HFD_irs09XE08lKa9cSt7zG5qkUsBPspLzR2D6wbbCN78xojCXmqY6CzpCsgXfNG2nd5h2ymHrhDkYbAc90G1Tgw5w7-RFElAxNj_4doggGd0yB2a21heu_I4VykcQ3JzaMp0jofjLCYCXPOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344296f6e6.mp4?token=dT5gZOT9dEHjC5NQ6w1QK07Q_J_oTfPY38I4XMxgyV5H-icOaq_6FfeY0VgCixZ-vheopDcEB4-3uRXw38rMoWx6UXcmkVt2W1PCfVYJre01oqB_yaAzirQLzsGvW5Dhb6eal9oP-1FhWn8csEt5qoctnF86-_N-ll7no0wI6dGBbj9_EPW0LnXeEF1vhnfk-X8l_HFD_irs09XE08lKa9cSt7zG5qkUsBPspLzR2D6wbbCN78xojCXmqY6CzpCsgXfNG2nd5h2ymHrhDkYbAc90G1Tgw5w7-RFElAxNj_4doggGd0yB2a21heu_I4VykcQ3JzaMp0jofjLCYCXPOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روبیو اصلا نمی‌خندد و دست از اخم برنمی‌دارد
🔹
درحالی که ترامپ چندین بار در کنفرانس خبری شوخی کرد و حتی بایدن را به باد تمسخر گرفت، چهره مارکو روبیو هیچ تغییری نکرد اصلا به صحبت‌های ترامپ نخندید. #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/660488" target="_blank">📅 20:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660487">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0baf8b2c21.mp4?token=WKNZtnz9P7vg9B0NEqapCyFUCYe5J1Vx_XFwthvoqaJz99TxTAZX7nCaepS5UBVgM790NQOjCx5WHN_g8wcWA1yodJ02qBf53yW0mVAF3NxM7M6lK-49AktHgvnGxdB9I0PYtqQsWvY38MxHfQViLfcMH8Hlp3jzNoukVIGA7lq3gEXq5crNbIz62bDxKekQBaRtnZsco3inw3ws_11uAQGpqImtIvPJKqnjEP7REXS5y8ZuINehlfc1ToSUY6Yd8F5nCrVqbJlutCPo_6nQ-pJfuSGQyaRSl7PMEWlhLKjAoBYhXLK3dtUxeiHEK7m9RlXds5AZzkEjbAbivx-LxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0baf8b2c21.mp4?token=WKNZtnz9P7vg9B0NEqapCyFUCYe5J1Vx_XFwthvoqaJz99TxTAZX7nCaepS5UBVgM790NQOjCx5WHN_g8wcWA1yodJ02qBf53yW0mVAF3NxM7M6lK-49AktHgvnGxdB9I0PYtqQsWvY38MxHfQViLfcMH8Hlp3jzNoukVIGA7lq3gEXq5crNbIz62bDxKekQBaRtnZsco3inw3ws_11uAQGpqImtIvPJKqnjEP7REXS5y8ZuINehlfc1ToSUY6Yd8F5nCrVqbJlutCPo_6nQ-pJfuSGQyaRSl7PMEWlhLKjAoBYhXLK3dtUxeiHEK7m9RlXds5AZzkEjbAbivx-LxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ متوهم: در ۲ روزِ آخر جنگ بمب‌هایی به ارزش ۲۰۰ میلیون دلار روی ایران ریختیم #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/660487" target="_blank">📅 20:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660486">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
گزار‌ش‌ها از وقوع حادثه دریایی در نزدیکی سواحل یمن
🔹
گزارش‌های امنیتی از وقوع یک حادثه دریایی جدید در آب‌های نزدیک به یمن خبر می‌دهد.
🔹
گزارش شده قایق‌های تندرو و کوچک ناشناس، یک کشتی عبوری را در فاصله ۱۰۵ مایل دریایی شمال شرق عدن هدف قرار دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/660486" target="_blank">📅 20:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660485">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b04e9fe866.mp4?token=inagvIZ2TWSSyBx6WvT6VZl3ejW63CHvdjNGMhYZmlPtxbejY8N1qniEQ2DFl1DgPH0V7Ji5_iwmojtWl719CJUKn23cfRRxyip95GgzVaW8I7dg-5udT51ooee1qZgMc7RDk2D00mOV80xduC1ITYqbHPN9_x0XS-ol1XvGy-yOBEqA0u2lP_by_3gPmSOs5i1cw5H537l561OryqRQKlDvYMpEhm_QOdDSvXBdRG3yRmTHfuHEM7nBAX11DJFMBLtlBNYAzmvYY3YwxPQe8hnPvPSCywbdwaiSVDUHi6qd3_flv1Bt7_w9IVtTMnR2S2dZAdZJmvE_1sgWeIzIvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b04e9fe866.mp4?token=inagvIZ2TWSSyBx6WvT6VZl3ejW63CHvdjNGMhYZmlPtxbejY8N1qniEQ2DFl1DgPH0V7Ji5_iwmojtWl719CJUKn23cfRRxyip95GgzVaW8I7dg-5udT51ooee1qZgMc7RDk2D00mOV80xduC1ITYqbHPN9_x0XS-ol1XvGy-yOBEqA0u2lP_by_3gPmSOs5i1cw5H537l561OryqRQKlDvYMpEhm_QOdDSvXBdRG3yRmTHfuHEM7nBAX11DJFMBLtlBNYAzmvYY3YwxPQe8hnPvPSCywbdwaiSVDUHi6qd3_flv1Bt7_w9IVtTMnR2S2dZAdZJmvE_1sgWeIzIvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول پرتغال به کنگو توسط ژائو نوس ۶
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/660485" target="_blank">📅 20:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660484">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
ماجرای رفت و آمدهای وزیر کشور پاکستان به ساختمان فاطمی تهران در جریان میانجی گری پاکستان؟
زینی وند معاون سیاسی وزیر کشور:
🔹
وزارت کشور با هماهنگی وزارت خارجه، نقش فعالی در تسهیل تبادل پیام‌ها برای امضای تفاهمنامه ایران و آمریکا ایفا کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/660484" target="_blank">📅 20:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660482">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZUx112g0s-x79cJlejcejKkPAv8T9s24QgbO3xsw1nG2hkbXp3kwBs0iz6x3DHZzj3Wv9-FeuW1-ay2BvVMS_MOFrgucS6DZGEY8rFFVhgyhiWBSeKgvD7M31wRNLjalPOoE0Yj3D735xQsk9o5kZXkNlgaEaYrT93-lHoQJrRFhs_jD00_xs2W1vS3vX7WXTmM8TDNTOlVr7Z97Cr5m8F690pHB-NlWpEL78WcXsQx2FWlEOuan3ybmQoahnJfyjciM-fnaOQuQqljer8eOWbe_gk9b1iXfACgPVTV58KNajDrql8WW1ubPbJfy6Q22k58UBNWT0YfH36XZRT7m7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oPJraBcNmBVME_pbp_LoA54u0E0WKNCDOeutbcDWunxdjqVaOXuC33sFUDP2B27RgVY5O4isLX5pZX7BJA4QbNgDZvsZj_GqWduuSJTVlnVNaz7LWaj705-xe8N2dbxN0VtLsjPTvB37kAwrOgU1DVpS5unvdOvjgy8I2BtaxZRPOQ8xZAur2NzeXhbomjzF6hrVhi0SDp06xueCzny2vuu4cgRmiF2hi4KNs4JfF0I_IgFO7f6Cpp3C-Mj4LKSGLlZYveGijruzUb-Jjqz31OrhbY0TL2_MuJN6aS3nNroxLIc43RWzdbfqrfpBh7HbPCEx9YFxtqAsedCFZrHwZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📚
نام کتاب: سفر شهادت
🖋
نویسنده: امام موسی صدر
🔹
این کتاب، سخنرانی‌ها و نوشته‌های امام موسی صدر را درباره عاشورا با موضوع تبیین هدف قیام امام حسین، آسیب‌شناسی سوگواری و بررسی نقش زنان، به‌ویژه حضرت زینب (س) گردآوری کرده است.
🔹
مطالعه این کتاب به تمام کسانی که…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/660482" target="_blank">📅 20:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660481">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
زورگویی در دنیا، بازخواست در آن‌سوی مرگ را به همراه دارد...
🔹
00:10:30 سنگینی کفه بدی‌های ترازوی اعمال من
🔹
00:16:15 ماجرای شنیدنی از کنار گذاشتن چادر توسط همسرم و سیلی زدن من به او
🔹
00:22:10 وظیفه ما در قبال غیبت کردن دیگران
🔹
00:27:40 تنها عملی که به دادم رسید خیر رسانی به مردم بود
🔹
00:30:40 پیغام امامزاده به زن غریبه برای رفع بداخلاقی‌های من
🔹
00:44:00 اثرات عذاب برزخی بر جسم مادی
🔹
00:59:30 طلب حلالیت از برادر دل شکسته
🔹
قسمت شانزدهم (حلالیت)، فصل چهارم
🔹
#تجربه‌گر
: یاسر درخشان
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/660481" target="_blank">📅 20:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660479">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9af33fa341.mp4?token=qIptpHKxU0TTWIZy8UGpOHwguzB5fYSAVx3PP89kkaxhT3tUjUOf37iCYnuzDKt4wFEjNLBDN-hk-zUN9cDFQ2ujEzO5EGn0B_KWbwJRZmk69k-8dGEMDMZlO3z8u8huFARlr84oGfjWaaEsYsPonBmCePXA_K1Qp-DikhrBykz-NqaaXWVrFhQa70HXc7hYQFzr3IeHTMyvbccQpVXef1khNS-8ZQ76DL63NPXldDOGQtojsYWWzSl7mctttkjcsaipHYqfaLqznb_WXSiNOSJQf1KHeS7vzQ5IcnR0ljyGxVtcn6-u_Bax2mggL-cEOyT1tdWBycO0gdZf06aanQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9af33fa341.mp4?token=qIptpHKxU0TTWIZy8UGpOHwguzB5fYSAVx3PP89kkaxhT3tUjUOf37iCYnuzDKt4wFEjNLBDN-hk-zUN9cDFQ2ujEzO5EGn0B_KWbwJRZmk69k-8dGEMDMZlO3z8u8huFARlr84oGfjWaaEsYsPonBmCePXA_K1Qp-DikhrBykz-NqaaXWVrFhQa70HXc7hYQFzr3IeHTMyvbccQpVXef1khNS-8ZQ76DL63NPXldDOGQtojsYWWzSl7mctttkjcsaipHYqfaLqznb_WXSiNOSJQf1KHeS7vzQ5IcnR0ljyGxVtcn6-u_Bax2mggL-cEOyT1tdWBycO0gdZf06aanQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: یک نسخه از تفاهم را برای اسرائیل هم فرستادیم #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/660479" target="_blank">📅 20:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660478">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc928aa446.mp4?token=GTXQM_liKgMIpoF28RvYDiZmAAOjRHzi8WAPRMBpMn0Fz-aNnG1BDKZID_AJb6NRwKa7WzeSOQBXUz1K5PdoCEdoOco59xaluDq6KztET0naaIUeDAiiUWzNa44gLkYPn4Xb8nDv8JEjpmZxx6KprShoHAJUtOflLqtM-YJtxR80A2KAnCLff6dWJ43iY9_9ekboLy9iENJOxvScJSonimNKUcEE5EFE3xXd4YGnl3crsVmG2E5JrPYoMhP-ZspQbotibhYELmafBrqKDN70JvpD74mlaOMziGisKVJAB7XmmfDEZDRypkplyxYl0bv8aZkY69f27Z2Cnui2Yj2pGjU2Kfhr5yBN36Dga7GXpTpOvTPbNspX4mIBSvEjwmP-ZIKDVbbAPAzty5CmLaKBpUg7Mxvikr4sqgjd8oOkZdi5plYKRXVUBN1SMqtXWB0ato1TfgN8DXapSuVk1mLQoBcPomxf-bkBCMbfsKNJRbYfj8GiB-Bm73yfvaFYnGmC_36n4KN4RcTioM1IJWu16dkzFuvqmDYOqGrOOpzxID6GoF8Enguw9MqknMGqjZXBSEqrblLW9WdKIG7tgIgP53mSEC6aM64nKpkjNuiR81zt4vwzMc-EdNDwbsMSnLWK2vIkrJvePGQdYIrBtJuUQZ2eeWb8gbRBBpWvy4gM7KY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc928aa446.mp4?token=GTXQM_liKgMIpoF28RvYDiZmAAOjRHzi8WAPRMBpMn0Fz-aNnG1BDKZID_AJb6NRwKa7WzeSOQBXUz1K5PdoCEdoOco59xaluDq6KztET0naaIUeDAiiUWzNa44gLkYPn4Xb8nDv8JEjpmZxx6KprShoHAJUtOflLqtM-YJtxR80A2KAnCLff6dWJ43iY9_9ekboLy9iENJOxvScJSonimNKUcEE5EFE3xXd4YGnl3crsVmG2E5JrPYoMhP-ZspQbotibhYELmafBrqKDN70JvpD74mlaOMziGisKVJAB7XmmfDEZDRypkplyxYl0bv8aZkY69f27Z2Cnui2Yj2pGjU2Kfhr5yBN36Dga7GXpTpOvTPbNspX4mIBSvEjwmP-ZIKDVbbAPAzty5CmLaKBpUg7Mxvikr4sqgjd8oOkZdi5plYKRXVUBN1SMqtXWB0ato1TfgN8DXapSuVk1mLQoBcPomxf-bkBCMbfsKNJRbYfj8GiB-Bm73yfvaFYnGmC_36n4KN4RcTioM1IJWu16dkzFuvqmDYOqGrOOpzxID6GoF8Enguw9MqknMGqjZXBSEqrblLW9WdKIG7tgIgP53mSEC6aM64nKpkjNuiR81zt4vwzMc-EdNDwbsMSnLWK2vIkrJvePGQdYIrBtJuUQZ2eeWb8gbRBBpWvy4gM7KY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت تکان‌دهنده مادر شهید مینابی از شناسایی پیکر فرزندش در حسینیه معلی شبکه سه: از روی انگشت‌اش تونستم پیداش کنم!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/660478" target="_blank">📅 20:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660477">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QnI37qzOgUnQvZm5ulVltWnwxfV4jv9ZaNO3H75Tqds_RaEl26uCggV-RZDFDIDFtz7MlYTKgPHJ3Ke2fZo78Refmy4yOHRTvxiESiXWHc-_q6_2vIxVPzfHG2r_cdZjWHgyp6dqwIN1UHy5phvN3dM5mcc6ex9BG6sYPT5fzFjGKHhCWvdJwB-OgvLbVICcBMjqgkr2RDijT7SM1u_91T3XVobn7RMVgFRRzpMOArzi4gTfk4EMP6DRZ07PONicWSOMZTZheYheNlo1gcsGvaG2TuA7EazPrwv2Ph5-QxY47VofJQA6hH9ZK6i_TlWeuK5Fe3SdDL5nLoJNANcZFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهردار تهران: پیکر مطهر رهبر شهید انقلاب ۱۷ تیر در عراق تشییع می‌شود
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/660477" target="_blank">📅 20:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660476">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‌
♦️
توهین دوبارۀ ترامپ به ایرانی‌ها
🔹
صادقانه بگویم، می‌دانید، آن‌ها از یک سو فرهنگ بدوی دارند، اما در عین حال، این یک فرهنگ بدویِ نبوغ‌آمیز است. آن‌ها مردم بسیار باهوشی هستند، مذاکره‌کنندگان بسیار خوبی هستند، اما ما هم همین‌طور هستیم. #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/660476" target="_blank">📅 20:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660475">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1870ccf7fb.mp4?token=hBljUkRoa1aLfL16e3A02LwMFbF1OPQNwb_PnvfO_NA-5zquyQiCTv5XXPv8zTPt4c_1gWLCbGvBpSrh9ReeAAHA9pY4tooMCxULlf9hCaOiEM0DbRYo6Jv2DyWDrpyXNlEcSF13nRNkuMc9L3nkxFKxiKnzIvGIE0sVdE9-0H8-DVu188DVJhq4shSzmLKKOFePS24nOF2O_ngIL8a5aG37_1WrGgzvIlWYxNW1ip07DCiznisP06e2k9UYyPjWQ_GudIoYNsQ30VuC46-2LS9cpqAeJJcvxzMcnbzIbjI_y0CdULefd6CPonmkf5i_jy8xY8kzIVliGrrERFwF-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1870ccf7fb.mp4?token=hBljUkRoa1aLfL16e3A02LwMFbF1OPQNwb_PnvfO_NA-5zquyQiCTv5XXPv8zTPt4c_1gWLCbGvBpSrh9ReeAAHA9pY4tooMCxULlf9hCaOiEM0DbRYo6Jv2DyWDrpyXNlEcSF13nRNkuMc9L3nkxFKxiKnzIvGIE0sVdE9-0H8-DVu188DVJhq4shSzmLKKOFePS24nOF2O_ngIL8a5aG37_1WrGgzvIlWYxNW1ip07DCiznisP06e2k9UYyPjWQ_GudIoYNsQ30VuC46-2LS9cpqAeJJcvxzMcnbzIbjI_y0CdULefd6CPonmkf5i_jy8xY8kzIVliGrrERFwF-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ آزادسازی پول‌های ایران را تایید کرد #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/660475" target="_blank">📅 20:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660474">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
ترامپ: ایرانی‌ها باید تعدادی موشک داشته باشند، چون دیگران هم دارند
🔹
ما روی یک تلاش موازی با کشورهای حوزه‌ی خلیج فارس کار خواهیم کرد تا به مسائل غیرهسته‌ای، مانند موشک‌های بالستیک متعارف که درباره‌شان صحبت خواهیم کرد، و حمایت‌ها بپردازیم.
🔹
کسی می‌گفت: شما…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/660474" target="_blank">📅 20:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660473">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/851f11e503.mp4?token=JrxEaNhYQYNJ-Tb6KoTPUsY5ohr4x_l4336CbfRe4-N8PwNCCn0S9ra_2WTeZMvxN-lqETvReuQ5QRsf-KqoInvLgBjiBeT0X1yOex3JBtLNSXbNyIsAtNPW-EMkHLAumaWxlLiW9l7nmVSHecDn6j5ruqshjm33Bj05yBX7oOtiTSmc7MAFWWYlLKuRxFWOn_wuNOnneMucRswjomdX2UMokkB3VqKbKshr3ElBBARJBRw5_A249-zF0Dq81wkLSfjc32JRlKYY38mXHHWdZEXY4lMnjCx4cs1IJCLxkdMuTZvAIWs4kUnj7HLu70pbFwHNZxcLnr87FG__QelRRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/851f11e503.mp4?token=JrxEaNhYQYNJ-Tb6KoTPUsY5ohr4x_l4336CbfRe4-N8PwNCCn0S9ra_2WTeZMvxN-lqETvReuQ5QRsf-KqoInvLgBjiBeT0X1yOex3JBtLNSXbNyIsAtNPW-EMkHLAumaWxlLiW9l7nmVSHecDn6j5ruqshjm33Bj05yBX7oOtiTSmc7MAFWWYlLKuRxFWOn_wuNOnneMucRswjomdX2UMokkB3VqKbKshr3ElBBARJBRw5_A249-zF0Dq81wkLSfjc32JRlKYY38mXHHWdZEXY4lMnjCx4cs1IJCLxkdMuTZvAIWs4kUnj7HLu70pbFwHNZxcLnr87FG__QelRRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ قمارباز: با ایران فقط تفاهم‌نامه داریم و اگر موضوع ظرف ۶۰ روز به سرانجام نرسد، ایرادی ندارد؛ ما دوباره به بمباران برمی‌گردیم
🔹
آن‌ها توافق کرده‌اند که سلاح هسته‌ای نسازند و شما این موضوع را به وضوح در متن توافق‌نامه خواهید دید. #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/660473" target="_blank">📅 20:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660472">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d268e25c74.mp4?token=nBBXRYKLwqysOAHgnCLZeYkQDxc0yy165TRdpBHMMhrltw7PQPG7_EU1b72qWQjx_cWbHdMzH_wJPXpA3sHneTrUmaSwYkursvQL0GXK5xs_vRu4tCNiIUwNlxIg4f-p7e__6tnraRYvnb0o3ojvfEZUO8An0DNTzzjlloisyEBDcRrFlEpw9jwPMQCbZhfN244h5vkkPeBTThNHPEX8ZOkqRRY_8Yah6MWXmK3bzZEwwNWqz-K0Z1FC9sGENmo-ugHBL-1Evg6ohgWZh7KG8Hk8a5uVjSoE8-UfHLikquvFqnJSm4PhKuIJlhU763VrQxzqqUuMjzRTZLDkYHBrXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d268e25c74.mp4?token=nBBXRYKLwqysOAHgnCLZeYkQDxc0yy165TRdpBHMMhrltw7PQPG7_EU1b72qWQjx_cWbHdMzH_wJPXpA3sHneTrUmaSwYkursvQL0GXK5xs_vRu4tCNiIUwNlxIg4f-p7e__6tnraRYvnb0o3ojvfEZUO8An0DNTzzjlloisyEBDcRrFlEpw9jwPMQCbZhfN244h5vkkPeBTThNHPEX8ZOkqRRY_8Yah6MWXmK3bzZEwwNWqz-K0Z1FC9sGENmo-ugHBL-1Evg6ohgWZh7KG8Hk8a5uVjSoE8-UfHLikquvFqnJSm4PhKuIJlhU763VrQxzqqUuMjzRTZLDkYHBrXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ متوهم: پل بی ۱ ایران، معادل پل جرج واشنگتن بود و ما بمبارانش کردیم
🔹
مردم از من می‌خواهند که پل‌ها را بمباران کنم. چرا بمباران نکنم؟
🔹
من پیش از این هم چنین کاری کردم؛ چون می‌دانید، آن‌ها زیر یکی از وعده‌های خود زدند و من بزرگ‌ترین پل آن‌ها را بمباران…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/660472" target="_blank">📅 20:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660471">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cae7b917c7.mp4?token=OTaHMClVDK0FZNodNZf5oiCEZndShSPhWaZ3ebODTWkyNDSlP4M1Ykh19p2U2AMBeXtaJBiPWcq_rnqInd7tH1ZKQPyqYB-GaKh3_afgpsy1LZptLrhsE7axx0kalYYNgdBzKIF2CN89u1ePFU7HvF9JYmktXjv_N4BnMwEZO8IEFMvRF_y7H05X7aPWZdDuNjunhX-jYFNd1exmtuowgzrwNkdXz2lGL5UUHrGkurW9yQdaM1UwAzmayogUdU7I5tmZusDwEgmp-wqtQXcgrUn-T-of_xuxaoNKUoqQg1UOSc3JUx-3G15CE5ohQO9RoCxNIxlXReZ5iVucWA4HKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cae7b917c7.mp4?token=OTaHMClVDK0FZNodNZf5oiCEZndShSPhWaZ3ebODTWkyNDSlP4M1Ykh19p2U2AMBeXtaJBiPWcq_rnqInd7tH1ZKQPyqYB-GaKh3_afgpsy1LZptLrhsE7axx0kalYYNgdBzKIF2CN89u1ePFU7HvF9JYmktXjv_N4BnMwEZO8IEFMvRF_y7H05X7aPWZdDuNjunhX-jYFNd1exmtuowgzrwNkdXz2lGL5UUHrGkurW9yQdaM1UwAzmayogUdU7I5tmZusDwEgmp-wqtQXcgrUn-T-of_xuxaoNKUoqQg1UOSc3JUx-3G15CE5ohQO9RoCxNIxlXReZ5iVucWA4HKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ به اسرائیل در قبال حزب‌الله توصیه می‌کند: رفتار بهتری داشته باشد
🔹
اسرائیل شریک خوبی بوده است. من فکر می‌کنم آنها می‌توانند در رابطه با حزب‌الله بهتر عمل کنند
🔹
وقتی دو پهپاد حزب‌الله بیابان شلیک می‌شوند و بی‌خطر سقوط می‌کنند، نیازی نیست ساختمان‌ها…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/660471" target="_blank">📅 20:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660469">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XnG9P6x2zPGj-br2lvofuQG5JeQyCKuh7gHXwtDzaaYVAZDnfJ1Q8uxmx1GraW3wlgdkRy-0EHyXawcv6LmJOV4z79uGeVc6IOuqzYamexMIbGhkG9-RZj09coqfpfhgDSsRHowIWv0JYZX-ADYf_RqVOwyfJ45qagamoMazPCrDGR-TV4wSvMy5ovhbAh6WCfNWB9oXEgkCZP03d0F7uXWQd9a2aB2x02lrLvhUgMsr2X1gfWGlGhX0yO5q5_HLKndxAIMOdKol-GmCtz5UeC79ifr8l8u2YXM7LeyP8ALGyg0YXuh3gVfEOeXlghRlBTRz_HRACexPv0hQ1Mtw0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سقوط کرد
🔹
با تداوم روند نزولی قیمت‌ها پس از اعلام توافق، بازارهای ارز و طلا وارد فاز اصلاح شده‌اند؛ به‌طوری‌که قیمت طلا به کانال ۱۵ میلیون تومان بازگشته و دلار نیز در میانه کانال ۱۵۰ هزار تومان نوسان می‌کند. این شرایط می‌تواند فرصتی کم‌نظیر برای سیاست‌گذاران اقتصادی باشد تا با اتخاذ تدابیر مؤثر، از بازگشت موج‌های سفته‌بازی و جهش‌های قیمتی جلوگیری کنند. در صورت مدیریت صحیح انتظارات تورمی، تقویت ثبات اقتصادی و هدایت نقدینگی به سمت فعالیت‌های مولد، می‌توان از این فضای آرام برای مهار تورم و کاهش فشار بر معیشت خانوارها بهره برد و زمینه را برای پایداری بیشتر اقتصاد فراهم ساخت.
🔹
هفتصدوهفتادوهفتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/660469" target="_blank">📅 20:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660468">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db97435661.mp4?token=KgcdHHQ-XPCxQJysbCMvasrgxuDjjXZecu-QshGCZZoxokUAA97q9FSRFM_9yShg76_tff6cdud5alvILlnUyNMuNanbTfRrK8E9fv8oDkXEQ9qGeTSv_DUpgaD3QQNGxeC1t4Zi_V5BAycG-fVw81AHSZz4dwBSNpHDOIAqi1asWIDrnvFthqkohKlRDjMIrjLkb3h3Y-1C85I-Oe6-1ZgHmFtEYON2kkvdh158ZsMktZ_DEJ5qE9pFkOlFOLGlEuCTPURoM6kLSI_ANJemDARlMeRCRYxLXe7bydv7xlvVi-Sp1bir29PxAg4RwQJBpbizC6oacWknrJqplpLh9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db97435661.mp4?token=KgcdHHQ-XPCxQJysbCMvasrgxuDjjXZecu-QshGCZZoxokUAA97q9FSRFM_9yShg76_tff6cdud5alvILlnUyNMuNanbTfRrK8E9fv8oDkXEQ9qGeTSv_DUpgaD3QQNGxeC1t4Zi_V5BAycG-fVw81AHSZz4dwBSNpHDOIAqi1asWIDrnvFthqkohKlRDjMIrjLkb3h3Y-1C85I-Oe6-1ZgHmFtEYON2kkvdh158ZsMktZ_DEJ5qE9pFkOlFOLGlEuCTPURoM6kLSI_ANJemDARlMeRCRYxLXe7bydv7xlvVi-Sp1bir29PxAg4RwQJBpbizC6oacWknrJqplpLh9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ دیوانه: هیچکس نمی‌تواند به اورانیوم‌های ایران دست پیدا کند  ترامپ:
🔹
هیچ‌کس نمی‌تواند به آن دست پیدا کند، بنابراین مهم نیست که ما این کار را سریع انجام دهیم، اما می‌توانیم آن را نسبتاً سریع انجام دهیم. هیچ‌کس نمی‌تواند این کار را انجام دهد
🔹
اگر این…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/660468" target="_blank">📅 20:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660467">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90da295199.mp4?token=cKrkW7gmLdistJhbemlgUvC084Ndbt3tmfDd7VFEHL3NurW6-cqGcZN7z7DJAThADs0__CmVRmw1QlmunASlRelo7Nz8UKdISNOiRKlVbtz2lVcpiTd4SePWLYSTxeioqx175syiYv0fv-lV_x6l1z7Efybs24KRF-IUelXu_K9qu20u6K_Xic_msqFNCamQsNW_7xpq8mJWRj8lCZ2hMrKqLqN9E-x1hjjVnf3p7zGXjNBxDxWIkVQSfxjXZ9PTAQB0eODv8lERg5ckeNtD2n8dYPqodW3NZWkHFQ-lxvGqRjQF7KBLvxw_V257yxI7U1s-k4LDv5rDP7SKMTYyAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90da295199.mp4?token=cKrkW7gmLdistJhbemlgUvC084Ndbt3tmfDd7VFEHL3NurW6-cqGcZN7z7DJAThADs0__CmVRmw1QlmunASlRelo7Nz8UKdISNOiRKlVbtz2lVcpiTd4SePWLYSTxeioqx175syiYv0fv-lV_x6l1z7Efybs24KRF-IUelXu_K9qu20u6K_Xic_msqFNCamQsNW_7xpq8mJWRj8lCZ2hMrKqLqN9E-x1hjjVnf3p7zGXjNBxDxWIkVQSfxjXZ9PTAQB0eODv8lERg5ckeNtD2n8dYPqodW3NZWkHFQ-lxvGqRjQF7KBLvxw_V257yxI7U1s-k4LDv5rDP7SKMTYyAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ قمارباز: به احتمال زیاد تفاهمنامه را با ایران امضا خواهیم کرد  رئیس‌ دولت تروریستی آمریکا:
🔹
اگر دخالت نمی‌کردم، ایران، اسرائیل و غرب آسیا را نابود می‌کرد. ما در مورد لبنان با نتانیاهو کمی اختلاف نظر داریم.
🔹
او می‌توانست تحمل بیشتری داشته باشد و هر…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/660467" target="_blank">📅 20:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660466">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: فکر می‌کنم توافق با ایران انجام شود #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/660466" target="_blank">📅 20:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660465">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76cef89fcc.mp4?token=n_HBNwx1fPgVlxs8EwdoqrwadbvvqthrEaScga6CtMNDqGtbnLuen1msza5xedvMtGJt8Y4pqZRvSV60kZbEP0VPVvxXQC3axx2aKKrGNkp9FzeXJjI0VgWvRBpO53tW-NO5kh_T_nKmzGpzb1V_ouguXCEBCKamfw4mPtq6sT3_-sl0FtsBAYR0wZtS5NgJxnrggeGJuXcIv6NcZt8DtTRy5lCtobDXH1iIUd8CF6hi5deekMKaKGGAnffNFac68W1txLUFcQ1eGSSevzauAQxtDVx7FaC6j-20lLpCeU64FzzY3QdtCgJVwP-XAhMJ6-OQrgEFLktjsfpgE5B7MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76cef89fcc.mp4?token=n_HBNwx1fPgVlxs8EwdoqrwadbvvqthrEaScga6CtMNDqGtbnLuen1msza5xedvMtGJt8Y4pqZRvSV60kZbEP0VPVvxXQC3axx2aKKrGNkp9FzeXJjI0VgWvRBpO53tW-NO5kh_T_nKmzGpzb1V_ouguXCEBCKamfw4mPtq6sT3_-sl0FtsBAYR0wZtS5NgJxnrggeGJuXcIv6NcZt8DtTRy5lCtobDXH1iIUd8CF6hi5deekMKaKGGAnffNFac68W1txLUFcQ1eGSSevzauAQxtDVx7FaC6j-20lLpCeU64FzzY3QdtCgJVwP-XAhMJ6-OQrgEFLktjsfpgE5B7MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ کودک کش: وقتی سربازان جوان‌ آمریکایی را می‌بینید که‌ بدون دست و پا حرکت می‌کنند، یا صورتشان بر اثر انفجار متلاشی شده است، بدانید ۹۵ درصد این موارد کار قاسم سلیمانی است
🔹
او همه‌کارهٔ ایران بود و مورد احترام قرار داشت. او یک نابغه بود. از قضا اهل ایران…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/660465" target="_blank">📅 19:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660464">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd2dc10635.mp4?token=LQXGxfCGOVozLFa-WXepPglDXdQI3cd_ntPhxBSpHt4jyUdM0ilONIscG6-PNPi44nIXSzKStxCrNh6pq8fQ1Gt9BefM3PWjcCqDhLXUNk3Dtjrb1QpMY8EtvZGifi2RmCOSSmHu6zwD0Mwzy8n5SgcaEqGvhbmQzfpGEOGTwV9SprPyUQnBzufPDIQDz8QGiiZSMWRiqrEHiC7x8E1ffDh8hLUTLnaZ7H4uqGbCvLQTkPZxiVD2IqEXO5bee_Xz2pK1GybGcsycc6ujpuFaR0uc0yfJf7tBtET4h-goX_SDP0ahBR82dTBre9SX9F-4d7ac5NMVXBtijSZiEMEW5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd2dc10635.mp4?token=LQXGxfCGOVozLFa-WXepPglDXdQI3cd_ntPhxBSpHt4jyUdM0ilONIscG6-PNPi44nIXSzKStxCrNh6pq8fQ1Gt9BefM3PWjcCqDhLXUNk3Dtjrb1QpMY8EtvZGifi2RmCOSSmHu6zwD0Mwzy8n5SgcaEqGvhbmQzfpGEOGTwV9SprPyUQnBzufPDIQDz8QGiiZSMWRiqrEHiC7x8E1ffDh8hLUTLnaZ7H4uqGbCvLQTkPZxiVD2IqEXO5bee_Xz2pK1GybGcsycc6ujpuFaR0uc0yfJf7tBtET4h-goX_SDP0ahBR82dTBre9SX9F-4d7ac5NMVXBtijSZiEMEW5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ قمارباز: ما فردی به‌نام سلیمانی را از میان برداشتیم. فکر می‌کنید اگر او زنده بود، اتفاقات فعلی [برای ایران] رخ می‌داد؟
🔹
او یک نابغه بود. مردم این را فراموش می‌کنند. من در دورهٔ اول ریاست‌جمهوری‌ام سلیمانی را از میان برداشتم. بدون آن کار، احتمالاً…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/660464" target="_blank">📅 19:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660463">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01269cc71d.mp4?token=UQ6692ImZIosAM0UkQSSFn7dyl3Cq3Zkw5516oVKWOZKsacrLciytaw89kZWjc-yNc_0jJMZvqcR9-hR7YcXif9_e2NNfEZBvQgUkirJYKksKveRXp-ZdL3Zj364QbcAiapFSwv66fyXydFwJJ_HhdsMBzAAEZQ9SKIS8EP5ODYwxYk2sckaxwsAc5zKVhNEq5ktcQ4DNiG5CEg5btjgVlIb8efN1Hm-QQUnL5ilVRcZncAEKMNX2TY-99qYxonZXWuC0__WvadeVEVIETLyum3SjnpXa9rtH4ka1AVt0GN7yLvfhqSPk8kF1WbGc9LLe6tBV_BUe3k2of8MF0Jh9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01269cc71d.mp4?token=UQ6692ImZIosAM0UkQSSFn7dyl3Cq3Zkw5516oVKWOZKsacrLciytaw89kZWjc-yNc_0jJMZvqcR9-hR7YcXif9_e2NNfEZBvQgUkirJYKksKveRXp-ZdL3Zj364QbcAiapFSwv66fyXydFwJJ_HhdsMBzAAEZQ9SKIS8EP5ODYwxYk2sckaxwsAc5zKVhNEq5ktcQ4DNiG5CEg5btjgVlIb8efN1Hm-QQUnL5ilVRcZncAEKMNX2TY-99qYxonZXWuC0__WvadeVEVIETLyum3SjnpXa9rtH4ka1AVt0GN7yLvfhqSPk8kF1WbGc9LLe6tBV_BUe3k2of8MF0Jh9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: ما باید سنگر را از بچه‌های لانچر تحویل بگیریم و مردم را از زیر فشار اقتصادی دربیاوریم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/660463" target="_blank">📅 19:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660462">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebed2fc585.mp4?token=daMZ2Bvi08a7PsAes3huB8s0x6uT6q1p7Q97rUZirxKVfqXc9EB52Ll_fcborYF--k5iFNne_Mo4cr-DcSUr6bcJxJ8fzL7hWJbwp2EEufxaHSuCG6cCDfwxQvJikJsa4OkOI_OGCvUb7TYZM5sT2wOeo2AH1BD_5OCLMlA_W8B-qz1bbj9WRAMcGptdRIbkf8UMNKlQ9FIPH_bVheOKHO8pe_BEcQ9EBzgLmvtVsKkLiv5mg1Rh3I5gsFZfhflDXO-7ytWZ6rpekaXSz-zQsMvRQnYtjIz8gW9xv902OBM0yhZxUb-eN7CJC8FTpF7oAlh4KAbAdO4u8e4RCFdkzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebed2fc585.mp4?token=daMZ2Bvi08a7PsAes3huB8s0x6uT6q1p7Q97rUZirxKVfqXc9EB52Ll_fcborYF--k5iFNne_Mo4cr-DcSUr6bcJxJ8fzL7hWJbwp2EEufxaHSuCG6cCDfwxQvJikJsa4OkOI_OGCvUb7TYZM5sT2wOeo2AH1BD_5OCLMlA_W8B-qz1bbj9WRAMcGptdRIbkf8UMNKlQ9FIPH_bVheOKHO8pe_BEcQ9EBzgLmvtVsKkLiv5mg1Rh3I5gsFZfhflDXO-7ytWZ6rpekaXSz-zQsMvRQnYtjIz8gW9xv902OBM0yhZxUb-eN7CJC8FTpF7oAlh4KAbAdO4u8e4RCFdkzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ متوهم: اگر ما این تفاهم را انجام نمی‌دادیم، تنگه هرمز باز نمی‌شد #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/660462" target="_blank">📅 19:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660461">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
ترامپ و عصبانیت مداوم از اروپایی‌ها: برای مین‌روبی به کمک اروپا نیازی نداریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/660461" target="_blank">📅 19:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660457">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brJc58AGpAggOiTYg8GAMp7fg91EX6ExcsW4cDG51yH0C6vW3HZY8stb8D_XGImRHvijxNLpfwRM1YSd3pXUuUutKBxp3BqeCMqMj5kI2QBPj9nG6vflfm7loOHj-wZhWxfLkyAPss-wjBQadqS6RN60gZHulEdopQWAkaNWoTe2JkGiYGUyTa9378FnnT4NRMCNJePtIQhnPd9vAhdBiyYcM7t7FVi1TjjQCQQ5lj-9ApXlX7raktfxmtXB_hCSIwKHRaZdtNXPCYS2kD6NVq7-7jeY8YLQ_BrizvTuLiMfnK5phOmZL_fcvIQGzVrAtxEK0M-91mjaxxH3bZKC2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: تعهد ایران به همکاری برد-برد بر پایه مشارکت استراتژیک جامع با چین، قاطع است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/660457" target="_blank">📅 19:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660456">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e23d196b0d.mp4?token=eNWXOba1v69mrfKjB5E1pP2I9OStnkJFGBWeYm00ptdjE-YXzPIJR7Cyc_7912eZTeEd9NRGe3ublLl2G25H_t_Tl_k9oQZPAMcaZ-sYep0GtESGl4ZCKp-210-QsR1u2Gn-O2xZHn-mVqiY3QoIsnNcD6Q_j_xjo-eVGTnu8Mvex6HdQ9S8pnP0lfjM9g0CHW1Ne0Ds_4h08YP9E3eCKXAEvWZ-p8jVZcbV1P1jTawiS9ckCDPrUdfN3ImhFHJYcTOGhOGmCJOPuGE7wLrpDF30QiIvUzlDRvU59VyrHFbOj4ZLLj3nXD09sU4XclYvrfUdyLQA-gozo7JzB-izVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e23d196b0d.mp4?token=eNWXOba1v69mrfKjB5E1pP2I9OStnkJFGBWeYm00ptdjE-YXzPIJR7Cyc_7912eZTeEd9NRGe3ublLl2G25H_t_Tl_k9oQZPAMcaZ-sYep0GtESGl4ZCKp-210-QsR1u2Gn-O2xZHn-mVqiY3QoIsnNcD6Q_j_xjo-eVGTnu8Mvex6HdQ9S8pnP0lfjM9g0CHW1Ne0Ds_4h08YP9E3eCKXAEvWZ-p8jVZcbV1P1jTawiS9ckCDPrUdfN3ImhFHJYcTOGhOGmCJOPuGE7wLrpDF30QiIvUzlDRvU59VyrHFbOj4ZLLj3nXD09sU4XclYvrfUdyLQA-gozo7JzB-izVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ و عصبانیت مداوم از اروپایی‌ها: برای مین‌روبی به کمک اروپا نیازی نداریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/660456" target="_blank">📅 19:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660455">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
بازار زعفران ایران از دست رفت!
غلامرضا میری، نائب رئیس شورای ملی زعفران در
#گفتگو
با خبرفوری:
🔹
با توجه به شرایط موجود، صادرکنندگان معمولا نمی‌توانند زعفران صادر کنند. اگر بخواهند صادر کنند باید مانند گذشته زعفران را به تجار کشورهای همسایه‌‌ای بدهند که معمولا تولید زعفران دارند.
🔹
آنها نیز زعفران ایران را به نام خودشان آن هم با قیمت ۲۰۰ تا ۲۵۰ دلار ارزان‌تر به مشتریان ما می‌فروشند برای آنکه بازار را در اختیار بگیرند؛ به همین خاطر بازار زعفران را از دست داده‌ایم.
@Tv_Fori</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/660455" target="_blank">📅 19:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660454">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OkZZDUqyr61n7-T8AkD-vf58-wJi--qW4JS73p9BHC-WSQzllxVQDG8TAMSoXzG-oT2rmu6aVxVcAHiClgJpAn07C0UNbEGuabN2KoMuYd20v8M7J1OOG8E3KH2h8oF2MyDeM4_lINzQZ_zGXBBsAkdQaaOY5XpaudU9Nl71yDEmO97JY6lNm7J1khLtyFTyjLP8nOTfnT8LbkYpBAuVOs0nsj0VMj6X08pmpFBnVhs3FOljxjqK-S7skjhgei0XyFcw0PVHjoslLKtjPp5Gn0qtup24mpo7nPvnhm0dcnGe6NStvuNXpyHtU3eBNbm8BTJchmcIM9O7I4eH4a5g1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/660454" target="_blank">📅 19:04 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660453">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22add1ff84.mp4?token=KKcS2fITeB-0JZ0hb7xddLxiAkputnlEDGeihmjiWeDKhkEWSXm0SnlJ1Phu0P-Zu_ExJlcfbvyxldVjW4bspUHtG9on5m2mKxvlxApRL-Lq4OeCFVYC-W6CBag0K2kKcMw50fBkP2dKP_K-dZMqEFZ9kAnyJK3AHB4llqLVg1CHky3Pj_B_DQYzdx95nUSqTbxI1mSncZdCugwDKOOfHpDjB98EqcjNOTRHXF2pAB1Y36jnr8LHfVYyiHWOzSeB2hqhimiCYT5y6PPQyAUSZM9vxkmgNC7eLEsFlgUyqqffn9pwQ4_P2YsbW6Esgz36yPxMHyrUlExj2XXkzcDKtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22add1ff84.mp4?token=KKcS2fITeB-0JZ0hb7xddLxiAkputnlEDGeihmjiWeDKhkEWSXm0SnlJ1Phu0P-Zu_ExJlcfbvyxldVjW4bspUHtG9on5m2mKxvlxApRL-Lq4OeCFVYC-W6CBag0K2kKcMw50fBkP2dKP_K-dZMqEFZ9kAnyJK3AHB4llqLVg1CHky3Pj_B_DQYzdx95nUSqTbxI1mSncZdCugwDKOOfHpDjB98EqcjNOTRHXF2pAB1Y36jnr8LHfVYyiHWOzSeB2hqhimiCYT5y6PPQyAUSZM9vxkmgNC7eLEsFlgUyqqffn9pwQ4_P2YsbW6Esgz36yPxMHyrUlExj2XXkzcDKtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات مضحک ترامپ: توافق من با ایران یک دیوار محکم است برای جلوگیری از دستیابی آنها به سلاح هسته‌ای
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/660453" target="_blank">📅 19:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660451">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ecb9c2dc2.mp4?token=EScPj57giaUaBuETLicjHVnR7R154NaO50mUy7YO6qf4bg6drMsyqknVc53UsKry2ghT_fEpk585iVsR_Pwvh6eOtrLXVv7g0P__KM8jMkkIx4l-z2idhDxJ2Rune8pfc6urqQFFdj4iDeLvovMgkRpXmvVsAbsQ2Q9ed-2hUKrjCfQZc7rGpqbPvkzbbwrLO71QsCunp4BZP5TrWdu1DB-N9T3DbMM-_XslRc6Zli3cV17JGP_AfWa-5i1auq7dba95b3GQ-mvWgevqMP4hs_8CwhupZcyVVdBcyzsR2wmV-nduvRLqysXeuL5JDg5MilDHHUHPiGY7P2OFA9O-Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ecb9c2dc2.mp4?token=EScPj57giaUaBuETLicjHVnR7R154NaO50mUy7YO6qf4bg6drMsyqknVc53UsKry2ghT_fEpk585iVsR_Pwvh6eOtrLXVv7g0P__KM8jMkkIx4l-z2idhDxJ2Rune8pfc6urqQFFdj4iDeLvovMgkRpXmvVsAbsQ2Q9ed-2hUKrjCfQZc7rGpqbPvkzbbwrLO71QsCunp4BZP5TrWdu1DB-N9T3DbMM-_XslRc6Zli3cV17JGP_AfWa-5i1auq7dba95b3GQ-mvWgevqMP4hs_8CwhupZcyVVdBcyzsR2wmV-nduvRLqysXeuL5JDg5MilDHHUHPiGY7P2OFA9O-Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماکرون خواستار صلح در لبنان شد
رئیس جمهور فرانسه:
🔹
هم اسرائیل و هم حزب‌الله باید به درگیری خاتمه دهند. نباید جنگی در کار باشد. باید صلح برقرار شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/660451" target="_blank">📅 18:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660450">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
سفارت ایتالیا در تهران روز جمعه بازگشایی می‌شود
🔹
وزیر امور خارجه ایتالیا اعلام کرد که بعد از چندین ماه تنش در پی تجاوز آمریکا و اسراییل به ایران، سفارت این کشور در تهران  روز جمعه بازگشایی خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/660450" target="_blank">📅 18:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660448">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iarynnur0qDgvLL16eYdfvxtnuNefqhnKaaB_5UZu2vcaRXBL7j_NbfbTbm53E-E-caG2GtQmlPr6GZjdCA8nmZ2MRxMadDKFLZ3TVx9eR1IKur6BTG1kDmeJ_PNG0WET2wN2MJVLvlc43gKjRO5V530UKjUMDRGC8kD4t_LrWA6MIHouLQvtuJPCRqJ-lp5NdV5XNP07RDKsfdVu0RgN1vG6XQ05BIjhOboLtKvhChxXNKv-ivGHRKtmMN4WNyaBDNWu1fn0j_GkhzLPN9xswdkhHjJS0pHNoa3uzm_4l36sMhxfaU5KS08glK5hh6IDnIjMRnT06SvNIY6jsQaUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران؛ شکستی بزرگتر از ویتنام!
فارن پالیسی:
🔹
دونالد ترامپ جنگی «انتخابی» را آغاز کرده که ممکن است به فاجعه‌ای سیاسی و نظامی با پیامدهای طولانی‌مدت برای آمریکا تبدیل شود.
🔹
تلفات کم لزوماً نشانه موفقیت نیست و معیار اصلی، میزان آسیب به اهداف استراتژیک آمریکاست؛ همان‌طور که جنگ ویتنام با وجود هزینه‌های انسانی و سیاسی، مسیر قدرت جهانی آمریکا را تغییر نداد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/660448" target="_blank">📅 18:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660447">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
‏
منبع نزدیک به تیم مذاکره‌کننده: سفر تیم مذاکره کننده به سوئیس لغو نشده است
🔹
سفر تیم مذاکره کننده به سوئیس در روز جمعه لغو نشده است اما جزییات ترتیبات مربوط به امضای تفاهم نامه همچنان در حال رایزنی است و هنوز هیچ جزییاتی در این باره(چگونگی امضای تفاهم) نهایی نشده است./ تسنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/660447" target="_blank">📅 18:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660445">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9Cw2p5LxLKDQ9ux--tYuj6P9H2Cl6jbCq_qgVyePmx7UpS-etizLxQkQh8CS8ZvTgADuTtSLhZDx0gICLdDRITzPmVHp0lOosP1aZ_1Evv8YMSTvypi3CXDjyCBOLuD3032YTDBNbItcQwzPIgk9tcop1epjqBwNbT4-g4itk9JjtojmKtIKI_bz2ULfGwTCFyDx7-a0wpTvBbbTFao2LbZZxO2NEkOPTZXe1Pjp12oOBvNqLjOTmt1c1-avuSr__LSblg6eOlUxqvr8bZz9SHXEoDd6CMuj1fcd9R-ZSS4rK9JxE7yoIQBn53W5Se4WKOU_SgNoLLUAfRMUj9XcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تاج‌السلطنه؛ بانوی مشروطه‌خواه دربار ناصرالدین شاه
🔹
تاج‌السلطنه، دختر ناصرالدین‌شاه قاجار از برجسته‌ترین زنان اندیشمند عصر قاجار بود. او با نگارش خاطراتی کم‌نظیر، تصویری زنده از دربار، جامعه و تحولات ایران ارائه کرد. حمایت از مشروطه، توجه به آموزش و دغدغه…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/660445" target="_blank">📅 18:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660444">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUgeEtUIW9aR5MlNpqPayGFb27n-rVlZgGzofoftZ1D3U9kqfHSk3ELnnnbFUT5_PrZ2LwJ5aBACeUCG8z5_DBVyYo3WnRUcjtoQnp2qd1z0nKIPL-fVBubS772tYrH3N7U-4edhDSSoXsrGvhZXklyl8bgm0w0rCLGPVIcx1Nd1qCaB9VRA_vdcnq1jvHk1LjdYk4S-mhHNv29GolnEHkBp2K01j8mbJEcPV9mCQFODflqW8hOpZ6xfrwPZe_FffkHDO__0J8V-CnL8JErpyCqM_2FI9eqK8mzTWNs_n8Qo9MNW5MyPsdGlvWIHkZnkB4tUfiVgN7xdBJBTeHvp0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
سیم‌کارت هوشمند شاتل‌موبایل ویژه جام جهانی2026
⚽️
💰
در جام جهانی امسال سیم‌کارت هوشمند شاتل‌موبایل رو با ٪70 تخفیف بخر و آیفون 16برنده شو
🎉
📶
با امکان اتصال به هر سه اپراتور کشور با پوشش سراسری 4G/LTE و 5G
🛒
خرید از:
shatelmobile.ir/2263
@SHATELmobile</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/660444" target="_blank">📅 18:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660442">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
ترامپ: با برداشتن نفت ونزوئلا، ۴۰ برابر هزینه جنگ سود کردیم
🔹
ما چهل برابر بهای جنگ را با خارج کردن میلیون‌ها بشکه نفت دریافت کردیم.
🔹
ما به مین‌روب‌های اروپایی در تنگه هرمز نیازی نداریم.
🔹
ما به آن‌ها نیاز نداریم، اما اگر آنها می‌خواهند اعزامشان کنند، فکر…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/660442" target="_blank">📅 18:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660439">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b9641e919.mp4?token=ddroqzjx34Nxa9MbYuMv-DTgzVwu9TXlPeYS3EPLy1loosKchAdgR5AmUSZV9UIzVPhzoB0q-cvwm_uW2j2tZ7pq-6IgAUKqSRXpyuWoutODrkOL5GxvWdrLU-QQVNa5hoNXoCg_w3yH6q_20yhVZODeuwvW6u_AgRsq5ltcCTU07h5a-AdWW1q0E7J_uQOj5_rtmbuQjrk9ii4oA7SGnEYD8nElJUsIizT701unrqSraEo1a8OZpPvjpVEji0jJIYJwQ4Bp_7rH5LL4Z6FTVBbQtLkaIG_uNJonSyz8bF6dflTkr3QfkLzp5RR8aJGuzclIp45ch8284OzOAjmaaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b9641e919.mp4?token=ddroqzjx34Nxa9MbYuMv-DTgzVwu9TXlPeYS3EPLy1loosKchAdgR5AmUSZV9UIzVPhzoB0q-cvwm_uW2j2tZ7pq-6IgAUKqSRXpyuWoutODrkOL5GxvWdrLU-QQVNa5hoNXoCg_w3yH6q_20yhVZODeuwvW6u_AgRsq5ltcCTU07h5a-AdWW1q0E7J_uQOj5_rtmbuQjrk9ii4oA7SGnEYD8nElJUsIizT701unrqSraEo1a8OZpPvjpVEji0jJIYJwQ4Bp_7rH5LL4Z6FTVBbQtLkaIG_uNJonSyz8bF6dflTkr3QfkLzp5RR8aJGuzclIp45ch8284OzOAjmaaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شدت طوفان و تندر عجیب در مشهد
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/660439" target="_blank">📅 18:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660438">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
ترامپ: نمی‌خواهم کارزار نظامی اسرائیل در لبنان متوقف شود
🔹
خبرنگار: آیا می‌خواهید اسرائیل عملیات نظامی خود در لبنان را متوقف کند؟
🔹
ترامپ: خیر، من می‌خواهم که اسرائیل بتواند از خود دفاع کند، اما می‌خواهم در این‌باره به درستی قضاوت کند. #Devil
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/660438" target="_blank">📅 18:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660437">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a63e66a81c.mp4?token=aNUuuWigGuxGV2xXn7o4xhizNQqnwxEy8ffLfDxepigj85d0_YvGWJXEOAoIW47LgCSR5p0h8v9xT0UQ1dq3NjUssUgtdlVcBLq307MMK4fK9Il0AXLmt0uQjAc1u1FyNBF3J8OEL7Yp7QQrJvHcNeezuuqhcU1UD1LAmP9RF6-JkL-E4ypxQbe5hprVtuotzK3zQKZl5hJj45jTrZ1v2v-KDxToilxD9Qhzh6w0eKGRfaVegJtiBuCPz7-ji5UgSELdnylNLuDdKUBGj4WB9_4tltduE9Wbu3GpNJ1PxXjSvktcWAv9gXbMYNX48tmKwwtgk4HY-1cZ3BlpIxpiAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a63e66a81c.mp4?token=aNUuuWigGuxGV2xXn7o4xhizNQqnwxEy8ffLfDxepigj85d0_YvGWJXEOAoIW47LgCSR5p0h8v9xT0UQ1dq3NjUssUgtdlVcBLq307MMK4fK9Il0AXLmt0uQjAc1u1FyNBF3J8OEL7Yp7QQrJvHcNeezuuqhcU1UD1LAmP9RF6-JkL-E4ypxQbe5hprVtuotzK3zQKZl5hJj45jTrZ1v2v-KDxToilxD9Qhzh6w0eKGRfaVegJtiBuCPz7-ji5UgSELdnylNLuDdKUBGj4WB9_4tltduE9Wbu3GpNJ1PxXjSvktcWAv9gXbMYNX48tmKwwtgk4HY-1cZ3BlpIxpiAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: نمی‌خواهم کارزار نظامی اسرائیل در لبنان متوقف شود
🔹
خبرنگار: آیا می‌خواهید اسرائیل عملیات نظامی خود در لبنان را متوقف کند؟
🔹
ترامپ: خیر، من می‌خواهم که اسرائیل بتواند از خود دفاع کند، اما می‌خواهم در این‌باره به درستی قضاوت کند.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/660437" target="_blank">📅 18:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660436">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f35d9ebf38.mp4?token=GnJNVj9am442zsDnLvGYgqadRsdqpNt4HmFUQ40d_wVVp2PWuLNA9vn2qOqiVbNWSTGC1uycuCrWlVO2-P3S3b8NrUoaykyzHb_Fk-WkIBEvbTS8VzmnzDvx3j_6Iy-FqnqyJyIZv3MxIuoBFzxXg2Puf8x6FPzTG2FOwMQ4UwbncdaADBv6-m-ow8brRDiYuYCw6ERoHPdxWMX-rJYOISvwayMEPy5Tr05z9IdT7RqFv5nAwgypWQg3MVWQ07Cqvb4XVXEROTDTOpAc-GBkMuR7CEukx31fdDMpSYqaZMjWPuFN97VEXVnbE3xL_d4mq-t6-jVbNJ9ycGgBU_rQ6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f35d9ebf38.mp4?token=GnJNVj9am442zsDnLvGYgqadRsdqpNt4HmFUQ40d_wVVp2PWuLNA9vn2qOqiVbNWSTGC1uycuCrWlVO2-P3S3b8NrUoaykyzHb_Fk-WkIBEvbTS8VzmnzDvx3j_6Iy-FqnqyJyIZv3MxIuoBFzxXg2Puf8x6FPzTG2FOwMQ4UwbncdaADBv6-m-ow8brRDiYuYCw6ERoHPdxWMX-rJYOISvwayMEPy5Tr05z9IdT7RqFv5nAwgypWQg3MVWQ07Cqvb4XVXEROTDTOpAc-GBkMuR7CEukx31fdDMpSYqaZMjWPuFN97VEXVnbE3xL_d4mq-t6-jVbNJ9ycGgBU_rQ6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: اروپایی‌ها به این نتیجه رسیده‌اند که حق با من است
🔹
خبرنگار: ما در این اجلاس شاهد برخورد بسیار گرم رهبران اروپایی با شما بودیم. آیا فکر می‌کنید آن‌ها دارند با جهان‌بینی شما همسو می‌شوند؟
🔹
ترامپ: خب، فکر می‌کنم آن‌ها به این نتیجه رسیده‌اند که حق با من بود. راستش را بخواهید، من معمولاً همیشه درست می‌گویم. فکر می‌کنم آن‌ها معتقدند حق با من بود و الان حس خوبی دارند.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/660436" target="_blank">📅 18:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660435">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ec434c658.mp4?token=igdTs9mFFMw8nW0kBF6-r_TZBsbOfp6NWyKEGdJlrimLpmsIvaP93BC-B7ehSo6ukgyUjCLcjUnZQUQn4JKeigwH92Ff7KwxO_6w4upCESq-ZDhQUlHxrWGni1zeH9EB5nvfV1YzHt-86Y-CEEfImVL3qlU3_k32-lASi35m5YnBHxGXPC8FTjk8gbp0s5VXcx9fxq8zSLdltiJQKwr3_04hQRtHfJzlRKfjvRIZvOtAGzNGFzcTuDHS-gNu5anjF8AB3F-olmzmt7Qt-HYeXbIt4vz9KFNSqO9CNxMYIpypWkuQbkQ_DyJVsRJosZw_4sNn8o7d2uK8NSD408iiqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ec434c658.mp4?token=igdTs9mFFMw8nW0kBF6-r_TZBsbOfp6NWyKEGdJlrimLpmsIvaP93BC-B7ehSo6ukgyUjCLcjUnZQUQn4JKeigwH92Ff7KwxO_6w4upCESq-ZDhQUlHxrWGni1zeH9EB5nvfV1YzHt-86Y-CEEfImVL3qlU3_k32-lASi35m5YnBHxGXPC8FTjk8gbp0s5VXcx9fxq8zSLdltiJQKwr3_04hQRtHfJzlRKfjvRIZvOtAGzNGFzcTuDHS-gNu5anjF8AB3F-olmzmt7Qt-HYeXbIt4vz9KFNSqO9CNxMYIpypWkuQbkQ_DyJVsRJosZw_4sNn8o7d2uK8NSD408iiqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ درباره‌ی ایران: هیچ‌وقت نمی‌دانی قراردادها چه می‌کنند، اما به زودی خواهی فهمید. فکر می‌کنم انجام خواهد شد
🔹
آنها می‌خواهند امضا کنند، می‌خواهند به زندگی عادی بازگردند. #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/660435" target="_blank">📅 18:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660429">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qziqn49wc7DKZv0tEYfCNU-y4_1vgbDwjel7vXyYCkcRPnQomkwrgOIY6w4erYcduywKoouRYss7Wj-4ARuzlBgHJjLdFwCVhAgf_TZrJOro3FcB7fNdjcy3Tv1TCO7PkALhTQtdlBgS0LARIcGfAdfWdWkserEATxccu27klUXFUqKjq9nsYwTa4GBk-52GWGE4YbY9QZ40JYhxr8noFXvM9VvyCwutB-U6J-LHNBVew-P0La07nBfqlT82yp3QeNaUqTZAV-aNrw2CL_MMEcaQeDv_ol1OnZXTZWVWNoNVPH3e1WdcLEX7_kALzzLd5jada10OoD5Cro3gAQskXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rT-jwoMWezFqUV7lg05WTDWw8M3j3QZTNaWg3YDErTg7XldOAokDF0sWaCPYEZf1YtNgBjz6t7vRrSJfjiWfxIC4N7RBLwfLEjA6W5dHZ07X6mXQoAwkKbQNuRkAWjNzPWQvWuRinalk7pKyxRWeTuL79qjoWbgiiZYPotYBepue7P64AX90f4BSRCm68VMgwhhCBXa91xe-bGPKmbJ6ytz4QT_kA5oAJPbvRUqWPMQJztSS1PIsJlZsILB01oSr9IyIzkuZRA_rEbr-UjjxRUFvQp_5C4uZ1vKx50YaQCJJLa1QsPuPIaF_DihjOWItA_47DitC_Po-_krYqNXH-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NWJ97U5pl6qh3oB1M8c0KWagTN3IaDEdTSvjLLB1X3bSqNL4lPCa5D4S_8pW6nKNIqoWhN-dKXKdq5r48GhGeK5OAYD5vkCnomWKXZuEYAU1l94kvl9cVlqI0AUzp4HSljnVw65fyp6yTi6OdLYIgK1boAWJOVg1KKbzZcRNePx_Y9wVVJ1ZovgHkmkzqvkHKwPcIA6KWL7jzwiBf0HSVv56Y0PYF46f3Ryem2mwqkrrkE91PdF9HhVQ4gr9rNholUgc6ZRR4QWQODhXBqnPWT8WjEmQ-6-yIWKxiEki1HlrqB03rc1YNjTscWUkH6cFViC4Uxuz2vi23sSPlkztLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZBMfs0QAKMx7pHsQAp8sX11P770u9lf7qvMo55cpXzYdkDZWO2eY5HMqPyRpQni2l7pKr_Gh0SmhSlBbYgxUeotq773ppFRDYqesU2oyv8MeZbZj4fIrp8KRWgUT_hmA14taPcYoL0S3wfGPg2WHbdQFK68uit4IT4EQkxBd3_JHJrNv5PNjhXvzNTrYOr--hd-Y7FCtVsN7w90oM19aT39LfjdO8q_FSNA8ToMhKAoqWVE1l87QCFzoJfRDXpEhJ1liQPagOEvAvhyRv5JRHssq04UMyWguTbg900TDYCUGemdguKuKXvmj2QVMtWO9vLf4OBiNjQ_Pw9rriUEUCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hSBDw2nd1erQ_1y7OBOye3JDKTb6lQq4svZnVRVyvi-BgH1WfoWi8_AgvC7XYzz87L7D7EiQJAm2YaTI9P7CJcjp6n4CsyiwhuUJE-EBSIDzAGL9HE13zIpbUf5zLDN7ymg46MKEaUKSPFcO3gnoXw0V4BEVanniph4PrzOxr94OoydRTGQJYB7bgpvLUfuO5v8ktav1wlpsImjmoor16Fw2XZzFn5VpS5vMWvQ_9j-2PgH1zcQKk7WYnqoq0f6lbpCSXv4vFfMSyiDKL9_eY7UmX7X58zcp7eyGKP9dVNvvS1tBOrJYZs8mq9iJJiU7LRGvwOCEiHmzmCcQNmDJZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AiXVftL2QYzHVAC6e8loeLGT7d73rUWd2iy4udg0HC1WMrHH4wIuHN3QBet90eySTLWrCiAowLdAKnGLhePrtj9d6mUa2EUWXx2TKaXv5gtOIt3-loJ82rTr84Tzi16GIz9OwU5VYPBaK8Q28L08IQJ294zoZxKRX-d5m278Y8WYVTLqAYzq0N-cktcNEQuFhzEH9ObrKfqNNGF1yqlYnOZre_z1eyEIKWxE99nM40fWmrpdX4mGUURPpoErM1_lFAhPxbF7nNfFK45Db9-_ir1RKaeSaMAo0mQm7F9WH5UTyB_cgupeVpPpVtrv_r-_bftaVWUpCCfc7EywwVlQNg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
قاتل‌های خاموش لپ‌تاپ!
🔹
۷ اشتباه رایج که در این اسلایدها می‌بینید عمر لپ‌تاپ را نصف می‌کنند!
🔹
بیشتر کاربران هر روز این اشتباهات را تکرار می‌کنند، بدون اینکه متوجه آسیب بلندمدت آن باشند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/660429" target="_blank">📅 18:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660428">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3de55bcdb0.mp4?token=UnO6yIPLW9uNkO2iE0srznMzqciEQKm-rucQo5I_JRmCkyKp5TQQMNLEROjKFECweG_PKqfomLrLsg5aU1Bu9nEpi_J9p2R_fHxhSvp1z4ebIXpevj9uNKnTHMLLA2AXq23vL171wW6sPwM4nzPdIqrA9yuby1YsZqoY3reDLny9x_H5GcNT_pFUt1hR_6ItupI5QGNNr8PFy3J9wz0CWWmEHcKLqss8xyMaKUjggXKCMFJhRdap8tB577lJ0IHKPC5p4vhy15EZDc93Or7b7bIWN4kf3pWjQY_Ty161keCjIOatURXJ5-Pqgjp_TVcFFO5TheXyrhqSYuxoUZJXDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3de55bcdb0.mp4?token=UnO6yIPLW9uNkO2iE0srznMzqciEQKm-rucQo5I_JRmCkyKp5TQQMNLEROjKFECweG_PKqfomLrLsg5aU1Bu9nEpi_J9p2R_fHxhSvp1z4ebIXpevj9uNKnTHMLLA2AXq23vL171wW6sPwM4nzPdIqrA9yuby1YsZqoY3reDLny9x_H5GcNT_pFUt1hR_6ItupI5QGNNr8PFy3J9wz0CWWmEHcKLqss8xyMaKUjggXKCMFJhRdap8tB577lJ0IHKPC5p4vhy15EZDc93Or7b7bIWN4kf3pWjQY_Ty161keCjIOatURXJ5-Pqgjp_TVcFFO5TheXyrhqSYuxoUZJXDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ درباره‌ی ایران: هیچ‌وقت نمی‌دانی قراردادها چه می‌کنند، اما به زودی خواهی فهمید. فکر می‌کنم انجام خواهد شد
🔹
آنها می‌خواهند امضا کنند، می‌خواهند به زندگی عادی بازگردند.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/660428" target="_blank">📅 17:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660426">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dc74569b6.mp4?token=D3w8mbbVUyOrWYzAfe4qhvALiKwnjDYZ1SqdAKFmDePokJF40jSezWbPkkP0ZB7k-OgvxzA3mPuHYLCuVcpFaMMdU1wUYP1paPuzksnqGsRmHDwModgECnRJks-Cg8k_WA8T4HgrOfTo6g-hU7vBfVJ09ovz4rzOTd2DQCWR9Ak6LY0OpiMaEOKV-Xl_6HhTyDFyW1gK9DWtxaoj0_2YJMUMhj1oW-LoLNlYKthAumpFFlSWJuSQxzE0w15kvpyn0TJymcxXSSZr8BfH0sBkEPMXUNQUQIRsfDxUsXuZtfybemCoXaQCW37jwrHr1yxfkl-xo2fV9LC-S4-CWbA1VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dc74569b6.mp4?token=D3w8mbbVUyOrWYzAfe4qhvALiKwnjDYZ1SqdAKFmDePokJF40jSezWbPkkP0ZB7k-OgvxzA3mPuHYLCuVcpFaMMdU1wUYP1paPuzksnqGsRmHDwModgECnRJks-Cg8k_WA8T4HgrOfTo6g-hU7vBfVJ09ovz4rzOTd2DQCWR9Ak6LY0OpiMaEOKV-Xl_6HhTyDFyW1gK9DWtxaoj0_2YJMUMhj1oW-LoLNlYKthAumpFFlSWJuSQxzE0w15kvpyn0TJymcxXSSZr8BfH0sBkEPMXUNQUQIRsfDxUsXuZtfybemCoXaQCW37jwrHr1yxfkl-xo2fV9LC-S4-CWbA1VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این ترفند کفش‌ها به خوبی تمیز می‌شوند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/660426" target="_blank">📅 17:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660424">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00d77ad613.mp4?token=GSqcwVE_10Jecf-lRtA8FgtwBHbvuqoTRPa8RZbnGhU1ms6MQDEE3DAPJP7k2C914ZGH1k-U_9c57r6D9W2rTaY4KlBlCY-BHRjFQTmT5ayR-OJa00PAfLM91hPTJ6vtjlHpE9bRwQqT5l9aEGJu5UUdn22FPnh7p4oG7AiitMAb-EpXlJpDWv2ONZIg9VX2ER4qH5UdAfRLRsvlo6zVVY2OpH59zUCgij4x4rNqFicTbWi1jphnsh3qJ6xSR3q4wttPW2mnwg9GlZgdFCUcv4l-II7exLd8SJbhVqnMxg6wBGH_T3rZSEFjG0jOJHjcYoOE_1CkOl1_h8fNjd96ezzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00d77ad613.mp4?token=GSqcwVE_10Jecf-lRtA8FgtwBHbvuqoTRPa8RZbnGhU1ms6MQDEE3DAPJP7k2C914ZGH1k-U_9c57r6D9W2rTaY4KlBlCY-BHRjFQTmT5ayR-OJa00PAfLM91hPTJ6vtjlHpE9bRwQqT5l9aEGJu5UUdn22FPnh7p4oG7AiitMAb-EpXlJpDWv2ONZIg9VX2ER4qH5UdAfRLRsvlo6zVVY2OpH59zUCgij4x4rNqFicTbWi1jphnsh3qJ6xSR3q4wttPW2mnwg9GlZgdFCUcv4l-II7exLd8SJbhVqnMxg6wBGH_T3rZSEFjG0jOJHjcYoOE_1CkOl1_h8fNjd96ezzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تشویق وایکینگی هواداران نروژ در شبکه‌های اجتماعی بین‌الملل ترند شد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/660424" target="_blank">📅 17:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660423">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgFnjeXet62I8FmnrscYzAfaMcXjTEgp_gQt61HRR3wbrhqXbUVh_NE4JEVlixXfq60OqkiudyMTiNYglNhf--oyydiFa4w9-S7c6lK51fPnzVjZShYmztcY9VWFtcg4emsfJXH-g9OQs7atwXzBjLaZLg_Bddgr7vtw_d4mqvfVcEaWp65X9wfwmS-bY7xq1s47_bqBAmegQ4ey89tC5vO8pTa4Lw76Yu3Qm_9c9JWdnE3A3_0Wi3Y61P0EPGyCbWGgQpEXRe2oLPOHjREvKYiPlqhhzhoLV71i6e8m2o2tDot6LDxKrw9Hz4AzAB6G0yBgkbtXPzCR4zWOL2Q3Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقشه وال‌استریت‌ژورنال از دارایی‌های مسدود شده ایران
🔹
بیش از ۱۰۰ میلیارد دلار از دارایی‌های ایران همچنان در کشورهای مختلف مسدود است.
🔹
طبق گزارش وال‌استریت ژورنال، بزرگ‌ترین بخش این منابع در چین و قطر (هر کدام ۲۰ تا ۵۰ میلیارد دلار) قرار دارد.
🔹
پس از آن عراق با ۱۵ میلیارد دلار، هند و کره جنوبی با ۷ میلیارد دلار، ژاپن با ۳ میلیارد دلار و آمریکا با ۲ میلیارد دلار قرار می‌گیرند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/660423" target="_blank">📅 17:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660421">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
پلمب کلینیک بیمارفروش در سعادت‌آباد تهران
🔹
کلینیک زیبایی «م» در سعادت‌آباد تهران به‌دلیل تخلفات گسترده با حکم قضایی پلمب شد.
🔹
بر اساس گزارش‌ها، برخی جراحی‌ها در این مرکز توسط افراد فاقد صلاحیت انجام می‌شد و «بیمارفروشی» به سایر کلینیک‌ها یکی از منابع درآمد آن بوده است.
🔹
همچنین ادعا شده تعدادی از مراجعان پس از جراحی در مراکز دیگر جان خود را از دست داده‌اند.
🔹
این کلینیک با پرداخت مبالغ کلان به برخی سلبریتی‌ها، تبلیغات گمراه‌کننده انجام می‌داد و مدیران آن متهم به تهدید شاکیان و خانواده قربانیان هستند.
🔹
صفحات داخلی و سامانه‌های پیامکی این مرکز نیز مسدود شده است.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/660421" target="_blank">📅 17:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660414">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vGCLZ4Cx2ubK_OMwWG9Bgr3eHqL54kOZm6b4q0VpbPZ_oUUrgsdWLbyljBO3QqtNsDUJY7WcUSNYSVkD9FoUjJ88NetRcoaPSUIe7YhcmK5TgUmP7elKftsYdAQrECTY2cNRCkeAMQg_dumrnT8MivUzV29ifjpD8HmJ2BiwA_YqPXI_ZTlFknEE208ojh-dJHne7HgDDLVYs6tTK90pwwCGbuACITJO4943OQRY0xH5YfGihZR2p8a36IAKXmk6eSQ-LcG2hmTmfT0w9IDKolHi_tI7Q9eGDHSFwSCX7RVLkHGt2O5RDhk_UTrB5W-X-Kar1MLmeHp93hh6Va4jBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iso-Z1hoUEfsrJ4ISvbfnATpeldJrkwwY8Nc4LaSXMXce6SgO4MXcAXilDAdaIq-LRRgdmP0zzIAxBJQZhDJ0L_Yduw_i66fy5azlyxwAyuKA4Qr1G5LN92RxDrztHYpr4P0Ad-0a1JAfSpaPBNyCMu-_tjI9H-JNPbrYR1fkiJISrkgqQf5dAggXynPimn0YWoIn69s67HIj7WVZNK33C9kMEnwKO6X-5S8Y_7tI2xIkZJdT4Srw6F9kWvtotwKsW16-Ei3ylDxiPCeU_XX6ijNeX7663moQPUEuWbc_c7I3jMyO5MuyW803ED3IbTt87L2cjJ_sUmiSjEQDPJEZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hjt8_NAhQBXxHzUQF1Yvq8hxVYw1mCjRvO-no0ar9toJTF8EWr3o8r4x70DNBMzGXqqy0fp7I3NV-rTbmURgvceU5m_DdovvlcECqvzkLRSKzvMNYAFa46YDBX44GhxYNoZwOdXGk12mbr5d7lymJthU3WigZn_YiCeh7fz8LlbH4hajjdpAMr9aAtf0ALF1s72YqDX9gMQmJKaQfgm88dueipO5KSZsNnQOnktAiys9DLlCDnskjGV87LmW7MLYerUeBd6Qg6_vZRqlumiEOIy_t-Jg-QGbmlwdEJ_dJupbOKIzNGkPSkB8AZIkpausH-Ll1_0HhgrGwBVV6mEndQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bv0bOIN4ZR7AwsIIssOtQ8oeOfmSBKbC3JbDssp4Y73A02JH3AKXjUYdkytW4AMDATSSZZvcnDMcxdcLwrGbqABwyN41JC1Skmd5lfFVFrW_13GFuawSoI8YlnB-j1tjQg9xF_z7KSCUuj-ssZP51PakZLf3eUv1s5HLvIApqY8FMQsKUHSLJO3WeHnVObwLp32T9ZKPjpeTpfzxiLinJ2ZOq3mDIkLT5kr0DXFmswwhoLlTTtdmCVvk_g2BuCaCO1WGRqa8QDTJ2sIwDswhVJ-z0_mtrqVGSxbHt-uaeWUzi7ltYIpQB5uat4m5NqAeaSAv1PpkzqzZoFTCnPv1rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MI3S7uzvTNmJgl7Tll8miXx8hB8gIs4AWgWPGcnA4xQ06cxm9drAOCop8343u8odo6-Qm36dkRS9EpDdwvkPXJXUMnck8CLFpPwcbEs1QPo6XhyNLiV6kEBYL0fQa3EnimoGeofX2odjPd0PEdo--ToJkF9Q-voRMgGbFdPCA8Y32OtuvgVdJnNU5rj8L0oTDAYtYuq0ATS1yZLwlpETAxiojgA7tKo5NR2kVbJG3uT51zARZNs-OGEpOyhaZ45R-xl_jaLB0ZPALt9HddsOZ5O1UB5y722gBGj89OZrXCoJWwnh3zoWIn7nIdRBqc5btkU9SDr3teTcYLV6-3DfwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ARzfyZEIPu8-W6NQkrbQUF7LS3j90eqVXkNbybnvakHmE3IZ5WNePf90yRdsriWCDanE_8Uq1yZ8hd5lPHDU-wQxMF4DaDGWyvpPF-bVNxqNK7menmFprsdjPBlZ9nk5niKvj93oMfXgPO07Bu6Vv2mOpIY_tNkU3uQTiMvwBEjb7Hqcm_8swSRccwqCnqGdgnBVtvWLHQ0OTQiRsW3yUJQkgXemHAmQ8sU3F5eJeHICplFNHWUOXUQTlI6U-lXCL0jVCEkJdCLFJDhUtxsO6qDXmJZBv4m9T31HuKyVUXmdz5NOkd0DJzkvUQJYJCjm3wP70y7cuNj05fyhzuQrVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WqGMW5gG41knU0bFJzTu1g4MUspDKdZJajVBXaVqEfqul7EU8jgjmv4Hc0CaBxuDjO6YxT3P0MU3-vhJGXHSkUo9Z-HqwPuv05MdEVDobxZR3M66x-JahWBWkHRa3RQPFjtzyS6spLgp5ymDnLS9JJ_YXpwf7Ua4NeB-G_oKqrXkZm590kmZVel_RX8-mPMaKpx_FrEVbC8V1oZuXXel0E9aJh3eYpNijoeBUkZLhVph5BeZppuDiShcvouTZhoJHu1btW7nXLF_idOOik1mf88to-WrM-D5bk6XaBcdJCws85cr71btQ1ozdJ2q9MJI7ZqhRPyD6jP0KzrvvX6JVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
۶ دستور قهوه سرد محبوب
🧋
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/660414" target="_blank">📅 17:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660413">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gghmw8zWYaPWiM-RBSZpEwc0eln7AXFYaSUvmkxAD3Rc1IyjBvOH6fHkTBwnsCfZN1iyUNasTSleyRTS7kibve3f3djqillPEmxrPJ11BA4XjY9ROO3buVj2sWvL1ij_i-5B2L5zgkbqcSflk2RvBJBVRlg4TYZAHse5ZvEmNAAZ24v8fciZcAMLOptG0fUFI7dRcnYvNWBYceTbLb8YDPRXMUekttrydyL6A_wn0qZDkVErY-gxABhYQk_yMsVIkqrGB4uCm9TgfoFSkwt1ttNs29S_BG-pQz1FuxAhmc9H8L3id9a_I9v7T1ayKKVHm1D5HyIgKZpo0Js8QhMtGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/660413" target="_blank">📅 17:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660411">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/296d273d86.mp4?token=iBBzsPSqrR4dvDskayT0fsEiVajXQPhlaXw3wNJ5DBQt4RixMDhN7QH23Z1UYU9tfYzlJKoTVY_i6tGyRdaE7hKwN-4Hmy8EC6VS5IX3z-EOFg3vukA7S5GHvAnDb-O4V7BYKSeJLpcmxhTb_YKu1pP8xJIuM18RSXRXLzVF99tn-ORJWQ8Mf8S0aR8sM3mnjr75CBD3_o-VooGTQXmES9io_py4QcZU6HAosRw6TSxtb_raP5cXigjCL25QFoBnu5yDrKR8f5mK7dz5zs9PWoHD8nansddTTCkSkNXwyRHf3cvrnMoSJey_-DF5xs_TPjO4771N0USVqntmKAwy3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/296d273d86.mp4?token=iBBzsPSqrR4dvDskayT0fsEiVajXQPhlaXw3wNJ5DBQt4RixMDhN7QH23Z1UYU9tfYzlJKoTVY_i6tGyRdaE7hKwN-4Hmy8EC6VS5IX3z-EOFg3vukA7S5GHvAnDb-O4V7BYKSeJLpcmxhTb_YKu1pP8xJIuM18RSXRXLzVF99tn-ORJWQ8Mf8S0aR8sM3mnjr75CBD3_o-VooGTQXmES9io_py4QcZU6HAosRw6TSxtb_raP5cXigjCL25QFoBnu5yDrKR8f5mK7dz5zs9PWoHD8nansddTTCkSkNXwyRHf3cvrnMoSJey_-DF5xs_TPjO4771N0USVqntmKAwy3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بارش رحمت الهی در دومین روز از ماه محرم در حرم مطهر امام رضا علیه السلام
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/660411" target="_blank">📅 17:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660410">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHUZfy54yiH2s2NvyjP0jNXKfz3j4M679YfPnKqvX3X1dH0yHfhpabvsGcTs059TIQqkEuBLgyaHys3CwDVw7OhVohlNBn81Hhs-5Gm76UmEOCNe_5GeYCyyZTFFL5LnUykPyy5iPItjhJjsn9qKFKThxDfBmyLqrkvNvXDjdSq3VHGJmmt7GXn5gcuGZ-mw5efaU_kkryByfY625ZoS-Ey4Qw5U5jgc7DLtxgw60LzWRnEhJ2AIOJAQa1feOwPjNyXuKFTlMiUMM6rgykmiLTc3PcHfftU7KNGe0Pbga7rDGDsMjqatkWudC8yAlninckxdLEgAXGYvGxpvLZMi7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روایت سقط جنین یک مادر باردار در پی صدای جنگنده‌ها
یک پزشک متخصص زنان و زایمان:
🔹
در جریان موشک‌باران دشمن متجاوز، مادری باردار به دلیل صدای جنگنده‌ها ابتدا دچار خونریزی شد و سپس جنین شش‌ماهه خود را از دست داد؛ این زن پس از ۱۲ سال فرصت مادر شدن پیدا کرده بود و پس از سقط جنین در بخش بیمارستان فریاد می‌زد: «ترامپ قاتل بچه منه.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/660410" target="_blank">📅 16:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660409">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
جزئیات پیش‌نویس ۱۴ ماده‌ای تفاهم ایران و آمریکا منتشر شد  منبعی نزدیک به تیم مذاکره‌کننده ایرانی:
🔹
بر اساس این پیش‌نویس، توقف دائمی و فوری جنگ در همه جبهه‌ها از جمله لبنان، تعهد آمریکا به عدم مداخله در امور داخلی ایران و احترام به حاکمیت جمهوری اسلامی و…</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/660409" target="_blank">📅 16:51 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660408">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rENVW30R_okobhox1PwM-IatLFOKakWASM6IXf6wXyqcnpflC81bNyx1ntrAAUPNnLOZyKj3cyU8AW5dePfUtFykitbhIE2j70Tvi1kC5akDWyrKWUgthvJ6Q3JqPnfFz306HJVk8aQWXn-FzkMLyrHgn5ltcoOMfK-NM_Dpyvih5e0VE_1Aj4Wg0JbXp64whccH9mohwLSHPZFiUfGNxscGVHp8xgBvDGmWgDeISvhd9QEEwXOK4Ak0j7_yerQOBtYn3yN0XOXlSuYKr-O3jL4_PCfdRtMCotfWNhn6aJK9teCTxy5SkA2MZhnKhR6a4eIXbnbPxAfl_tX0u1wjag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت جدید کارخانه ای محصولات ایران‌خودرو
🔹
لیست قیمت جدید کارخانه‌ای محصولات ایران خودرو ویژه نیمه دوم خرداد ماه ۱۴۰۵ از سوی این شرکت اطلاع رسانی شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/660408" target="_blank">📅 16:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660407">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
صندوق‌های تامین اجتماعی ادغام می‌شوند
اسماعیلی، عضو کمیسیون اجتماعی مجلس در
#گفتگو
با خبرفوری:
🔹
یکی از دلایل اصلی طرح ادغام صندوق‌های بازنشستگی، تفاوت عملکرد صندوق‌های مختلف و سردرگمی و مشکلات ایجاد شده برای اعضای آن‌ها است. در مورد ادغام صندوق‌ها در فقط یک کلیتی بیان کرده‌اند و کمیسیون هنوز به جمع‌بندی نرسیده است.
🔹
کمیسیون اجتماعی با این طرح موافق است و یکنواختی در اقدامات و صرفه‌جویی در هزینه‌ها از مزایای طرح یکنواخت شدن صندوق‌ها است و شرایط جنگی عامل تاخیر در تصمیم کمیسیون است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/660407" target="_blank">📅 16:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660406">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
ادعای جی‌دی ونس: متن یادداشت تفاهم با ایران حداکثر تا جمعه آینده منتشر می‌شود‌‌
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/660406" target="_blank">📅 16:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660405">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a08cf29fe6.mp4?token=b56nhlyO75Aq-S1wMK7uLY5_Z5pTMiz6vJoAzKeLqSn3LwZ00e9MA6zuigLJ97m91_O0hhJ8y0BuQ2qeX8W8Cs9p1FhLkpH7vXkvOlmaO6yk-Kx9GMjvRMwPppgxh7dmptdh3XvO8YkNorq9l-q-640kylwmla4smqMHmJjwMi6VhPcRutx8gYGfWuspJd8UvC-50C-U7yFwwRz69MqcDwnB6DexHyMzphRIjY63Zu63vzM1fuq2GltP3_03ombt-ZBRFXwK8Dxhrv3DarzvCQf0Q537wiA8atTpqolmU5T_2Y4US-mAcIAxEZ8osnYIa5ONjLtHc8h-EK8LdoD2jZtg8BSYG4vy-1MfIHmkuEtw0g4BxJ1Puq9YGshLZJbhTe1qVitk1UCBkhfOmD5j28KIPJmg1ILl_EItPgcBP9WJXjyONQuIVMKGzPQ-o1WVUQY6a81PazISPM2u5iuE25Owc8GEIcnlnutURyS0Xjk7GiSBHdOp0vauhO456I5fd4R6xh78unhbuyWQ4GjfT5YfjXb5szdnSPTEzlaCMNPukD3vA2BYMeS_RA2RsBs8gbh1PU5GaZqzwWIeH8o7-vNvIUi72tibfBqFudSFU9WB_L7t0i8dPO1Noj-2MU622YPhXokTsa3TKUCav0iSzDvcazkBd3fBW6EEPlRa6yI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a08cf29fe6.mp4?token=b56nhlyO75Aq-S1wMK7uLY5_Z5pTMiz6vJoAzKeLqSn3LwZ00e9MA6zuigLJ97m91_O0hhJ8y0BuQ2qeX8W8Cs9p1FhLkpH7vXkvOlmaO6yk-Kx9GMjvRMwPppgxh7dmptdh3XvO8YkNorq9l-q-640kylwmla4smqMHmJjwMi6VhPcRutx8gYGfWuspJd8UvC-50C-U7yFwwRz69MqcDwnB6DexHyMzphRIjY63Zu63vzM1fuq2GltP3_03ombt-ZBRFXwK8Dxhrv3DarzvCQf0Q537wiA8atTpqolmU5T_2Y4US-mAcIAxEZ8osnYIa5ONjLtHc8h-EK8LdoD2jZtg8BSYG4vy-1MfIHmkuEtw0g4BxJ1Puq9YGshLZJbhTe1qVitk1UCBkhfOmD5j28KIPJmg1ILl_EItPgcBP9WJXjyONQuIVMKGzPQ-o1WVUQY6a81PazISPM2u5iuE25Owc8GEIcnlnutURyS0Xjk7GiSBHdOp0vauhO456I5fd4R6xh78unhbuyWQ4GjfT5YfjXb5szdnSPTEzlaCMNPukD3vA2BYMeS_RA2RsBs8gbh1PU5GaZqzwWIeH8o7-vNvIUi72tibfBqFudSFU9WB_L7t0i8dPO1Noj-2MU622YPhXokTsa3TKUCav0iSzDvcazkBd3fBW6EEPlRa6yI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیرترین حیوان خشکی‌زی جهان در رکوردهای گینس
🔹
لاک‌پشت غول‌پیکر سیشل به نام جاناتان با حدود ۲۰۰ سال سن که در جزیره سنت هلن در اقیانوس اطلس جنوبی زندگی می‌کند، به عنوان یکی از نمادهای رکوردهای جهانی گینس شناخته شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/660405" target="_blank">📅 16:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660404">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B02WmFtqwCiEINZ5mBUY5UlRffS-4LcRE_Z7cTQ-ZMMI1IiC4qPWVTqAE28ulLhgac7IYtWkp2ROGblJzGoBk3d9cD2g-NDIBj7rLHYlNu6MaIsjIERKLYC2IAAN8Qe9PPtfbk4Gtvz15vvquMoresqbUcgwP7hvM3Y-x2j9TJ63r11qZJjfWjOBfqhxcJjzyt5gj3LQFWCnyZA3RumUrb8oTfUAegd8h3Zv8LyYBQOQKrVNAD1OkAduxMB9vF7vG5hSFtfepTTyHEx0Nqx5-DauY-KCTvNDINQCt3uLpmkw71yoWhD-l_Uz0Sk6JyGSXT0IC9QBcQwfXAqJvwhaYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نسل حسینی
🔹
همراهان عزیز خبرفوری؛ عشق به امام حسین (ع) از کودکی در دل‌ها جوانه می‌زند. در این شب‌های پرفضیلت محرم، منتظر دریافت ویدئوهای کوتاه از مداحی و عرض ارادت کودکان شما به ساحت مقدس اهل‌بیت (ع) هستیم.
🔹
منتخب  ویدئوها در کانال خبرفوری بازنشر خواهد شد.
🔸
ویدئو های خود را با الوفوری به اشتراک بگذارید
👇
#ایران_حسینی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/660404" target="_blank">📅 16:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660401">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
تغییرات در دولت با وزارت نفت آغاز می‌شود؟
عصرخبر نوشت:
🔹
در آستانه تغییرات مهم در دولت و برخی پست‌های حاکمیتی، نام محسن پاک نژاد به عنوان یکی از اصلی‌ترین گزینه‌های لیست تغییرات دیده می‌شود.
🔹
از پاییز سال گذشته زمزمه‌های برکناری وزیر نفت بالا گرفت و سپس شنیده شد که با چند گزینه برای تصدی وزارت نفت مصاحبه شده است.
🔹
با رخ دادن جنگ رمضان، این تغییر متوقف شد.
🔹
با پایان جنگ و برخی حواشی حالا به نظر می‌رسد این تغییر اجتناب ناپذیر است.
🔹
اما مهم‌ترین سوال این است که وزیر نفت بعدی کیست؟ آیا از بین افرادی که در زمستان با آنها برای تصدی این پست مصاحبه شده وزیر جدید انتخاب می‌شود یا گزینه جدیدی عهده‌دار این سمت کلیدی در دولت خواهد شد؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/660401" target="_blank">📅 16:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660400">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
خطر سقوط آزاد خودرو؛ قیمت‌ها چقدر پایین می‌آید؟!
🔹
کارشناسان بازار هشدار می‌دهند که صنعت خودرو، بزرگترین بازنده احتمالی هرگونه توافق سیاسی با آمریکا خواهد بود.
🔹
تحلیلگران معتقدند حدود ۵۰ درصد از رشد نجومی قیمت خودرو در سالهای اخیر، ریشه در تقاضای سفته‌بازانه داشته، نه نیاز واقعی مصرفکنندگان؛ با حذف انتظارات تورمی، این حباب عظیم فرو خواهد پاشید.
🔹
نکته دیگری که کارشناسان از آن سخن می‌گویند این است که دولت به احتمال زیاد واردات خودروهای باکیفیت را آزاد خواهد کرد.
در خوشبینانه‌ترین سناریو، قیمت دلاری خودرو می‌تواند تا یک‌سوم سطح فعلی سقوط کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/660400" target="_blank">📅 16:21 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
