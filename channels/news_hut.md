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
<img src="https://cdn4.telesco.pe/file/OVmEd3_krpBPPz52Ay3BjEMPIvFNtYYtnEpNUqj6H57cVFgOOz0x4A8_tqojEk8LTGIHXG2izU4hwnWMol42fHmDR9dhpweat4v7SVjlMPTHApmIeCAjydF9WHhAILcdGIFEkeXWWve_RsGzKSBbk5bwWEfHsNRYKWZeWbRtQsrRQUgIEYTVrYiMPBgNbwJSLhfsgRE9GgyprpygdV1kDsR_b7cpGNMlHI83VsndwE98JyTnN9mT9zqwAx_DGg7CDJ_6hhBFLTU9wYRTe8Zv794p-wzY3-UbDK2POAK5SwnXaOKIo4szAubNb2j_eXUDE0dSkGktcuKq0Txd28iAmg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 226K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 15:23:01</div>
<hr>

<div class="tg-post" id="msg-65833">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFMXRfP491veJV2y2McJYcjGLyrSeZ--A8YUhVL7qixjT5o7-e_zj-Lwjse_gfGkTtK2D6aajFEuUXoSUPQYFPbcPmHYLgCBP1mDbqcMQLzithYbiL80NKOa5GeEzoubJnTB6s2bNYxOeguRx1jc0ioxBU9tM1Kk4qyPPabAZ80frINIV6ZcuAQ2uIxm8438Hf8Lads6wAsS0BAtF_0ShReDqrPsn1UnB6Y7pHL5q-1_Iq5sGoFTp54cpv9uW5OHKfVwAp8hTJFTh9FsoH6In-0KIBF9W0sbNFhHwsJMvR0-uHVKIMHVSyc7iJMHMXrCXpQODy-e2L9mmMLwfynKyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
نیروهای آمریکایی در ۱۰ ژوئن سومین نفتکش ناقض محاصره ایران در خلیج عمان را از کار انداختند.
سنتکام پس از تکرار عدم رعایت مقررات، دو موشک هلفایر را به موتورخانه کشتی M/T Jalveer با پرچم گینه بیسائو شلیک کرد.
اوایل این هفته، هواپیماهای آمریکایی کشتی‌های M/T Marivex و M/T Settebello با پرچم پالائو را به دلیل تلاش برای انتقال نفت ایران یا حرکت به سمت بنادر ایران از کار انداختند.
از ۱۳ آوریل، ۹ کشتی متخلف از کار افتاده، ۱۳۵ کشتی تغییر مسیر داده شده‌اند و ۴۲ کشتی کمک‌های بشردوستانه اجازه عبور یافته‌اند.
این محاصره به طور بی‌طرفانه علیه کشتی‌های همه کشورها که به بنادر و مناطق ساحلی ایران وارد یا از آنها خارج می‌شوند، اعمال می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/news_hut/65833" target="_blank">📅 15:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65832">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
خبرنگار صداسیما: شنیده شدن صدای انفجار در محدوده سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/news_hut/65832" target="_blank">📅 14:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65831">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugzCfbz54v_MwOhGKetpoAhd1ASj_0rCiiQGLczZd5kxPNkEgBiYe3RdVMXfW0A2s7aL9c4dIzqowTHb7CnWnYUyczg3MwvD3A-c9o8wH4qm6i265506yQCvJBmN2Qfnxl_AIBdFAUDDO5mIlSBQkQ2bPOt-8hiSowT23Z_tM_-fYTO0CPGmGG1dgjMAHlUk0fTLH_fjM4sasSVDCvVCchIWiZEcT_6daOxmZ215yFas-IXuIYzf9gyUW88Rbb-dOIjG8yCoCtgo57ljYxGwboOdEnREL4i2sBtX0WexbDvVBN81rSb2sDtpDEOjwg1Aw6STiyyqYPJQL6NgerLqIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚬
🚬
شاهکار جدید رستوران های تهران:
⭕️
پنیر+ گوجه+ خیار+ گردو= یک میلیون تومان وجه رایج مملکت!
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/65831" target="_blank">📅 14:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65830">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
دلار: 180.700
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/65830" target="_blank">📅 14:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65829">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
وزارت خارجه کویت:
حملات مکرر ایران نشان دهنده رویکردی سیستماتیک و تهاجمی است که کویت نه آن را می‌پذیرد و نه تحمل می‌کند
@News_Hut</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/65829" target="_blank">📅 14:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65828">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKRxloDdBtXu1bXvT0ciYLBqmRs0yjS5JgABtUxp3psuCneJKu7d0Vja0mInyLx3GsxaomstNrQrw1AMZkDZ6zaeySlyaZosut76eeywzfKHVl2qA31s7PTnIgHwpc6Ol_e8OlHjmJFEo-FKXcgoV0FYDot9NR5zsoFw9jTFajkQlFFbpsUSdvo9ZozwKRYSlpYmwjVUTZ96Bs8hUrSkAOSU47TDhAy6Yh6irfkCVLY8Ry_HANfQ1lWpy0hjVZP_VCfcE1sb0EmJfpGR5qgvcOvga9l1Ncd-8AtBs_vxu5IEgSzZ5ZNv-PUg80hjxC2eAK_aYdKq2kPTQvP5IjRfqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇱
اسرائیل به فارسی:
دیروز عصر و دوباره امروز صبح، حزب‌الله، نیروی نیابتی رژیم تروریستی ایران، با نقض آشکار آتش‌بس، از لبنان به سمت اسرائیل پهپاد پرتاب کرد. حزب‌الله به لبنان خدمت نمی‌کند. در خدمت منافع رژیم تروریستی ایران است، در حالی که مردم لبنان و ایران هزینه آن را می‌پردازند.
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/65828" target="_blank">📅 14:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65827">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPcqEGvBwDpAVSYCNBMxjBA--Bbk7OMYmtMABvPGoBlhNUe-NoiYJAjK_uCisWNxwYubOmZXx_19rLojynd8YHKTClq2E-zbvfY8v28Y_Ldg61CIQP_6FpQuZAD07mguypakOjvGd1PgEv3hoid1mKykx4VGzchWknrR-h8_8yTArN9JWV7IEMI7lyTVCNu06aUMIpTqzydIMHEWdgN1E03wzix-dhdbpYEmA-pFVJYhR9UWN6Qx-DK0SU7J2QzgFmH0v0mTJRpVvb3VDiSRBXusc8LQ1lHJKvpHpFB8GUbFfv6_c6XVgYoYmEvELEwuRZY-yDgAmO-3HfZsShQUwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سی ان ان:
هیئت قطری امروز صبح پس از برگزاری مذاکرات شبانه با مقامات ایرانی که با هماهنگی ایالات متحده انجام شد، تهران را ترک کرد، در حالی که حملات آمریکا به ایران در همان بازه زمانی مذاکرات شبانه صورت گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/65827" target="_blank">📅 13:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65826">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a59b3948d.mp4?token=YBB3k5sRUy2Eo6dQDvW-0-8s-vWjrvTbZTJQ__-Lo147xE4H51gmiOYKYSecQQ9LeKOeU2VvFU525_X-Jfx9nga9ddPDS8Cap1q2g-fJMhmQsa3Il_lgUXVIaE2cmZ7tNxzwPKeUYRMz_XzxpmvA-U0imt45YsgjGHrCwhGsk-AX7wwjMexiD7wzl1BCuumJFDTE6rhqPzw0nZXHVdXbw-uBqVI83ltbl5-kddujKjkHeZDkiyfkiNOAZv1ZUBciLcixFqOevzezC1-Hty712E7RrkhT6HkpH6WAzUe4kQwkM1OHd_i_3n476DcPDvwjoqsh285jWSR_eYuzH1xXvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a59b3948d.mp4?token=YBB3k5sRUy2Eo6dQDvW-0-8s-vWjrvTbZTJQ__-Lo147xE4H51gmiOYKYSecQQ9LeKOeU2VvFU525_X-Jfx9nga9ddPDS8Cap1q2g-fJMhmQsa3Il_lgUXVIaE2cmZ7tNxzwPKeUYRMz_XzxpmvA-U0imt45YsgjGHrCwhGsk-AX7wwjMexiD7wzl1BCuumJFDTE6rhqPzw0nZXHVdXbw-uBqVI83ltbl5-kddujKjkHeZDkiyfkiNOAZv1ZUBciLcixFqOevzezC1-Hty712E7RrkhT6HkpH6WAzUe4kQwkM1OHd_i_3n476DcPDvwjoqsh285jWSR_eYuzH1xXvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات امروز اسرائیل به اهداف حزب‌الله در لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/65826" target="_blank">📅 13:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65825">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‏
🚨
🚨
منابع ایرانی به رویترز:
ایران و ایالات متحده هنوز در حال مذاکره درباره یک توافق اولیه هستند
تهران هنوز در حال مذاکره با آمریکا درباره مکانیزم آزادسازی پول‌های مسدود شده است
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/65825" target="_blank">📅 12:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65824">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7dae3f50b.mp4?token=jIp6g-m93i5QqO8BeiJ9Q1Hdzt-YDqIFrN35Bd55fFsFRJQGMsDTvclMlCsu0udSVbd13f4QyQbF2TJFV0LeToSbPj_LzjFoHiebdSL7eoREfOysZ925cdVl_q0nz0H2-PYYciPWC-GeblK33M4aIJIjH9Ggmxb2j6blV-3GEH8k6m4S5-ZkglG1X2v80nuwX4Ut9mhSiEiFoq87_6VyG0lLM5Zp-0oYGpmv20_qbNcqzDeVZEyddfqukaBwuqTGp5zVQIctdJLA3vdLMLHRbcoagec259UZ9UteT-XOtVWpwJk6t54Sp9tH4kKn_UubEkaqeT5jA1heDxyLCloKbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7dae3f50b.mp4?token=jIp6g-m93i5QqO8BeiJ9Q1Hdzt-YDqIFrN35Bd55fFsFRJQGMsDTvclMlCsu0udSVbd13f4QyQbF2TJFV0LeToSbPj_LzjFoHiebdSL7eoREfOysZ925cdVl_q0nz0H2-PYYciPWC-GeblK33M4aIJIjH9Ggmxb2j6blV-3GEH8k6m4S5-ZkglG1X2v80nuwX4Ut9mhSiEiFoq87_6VyG0lLM5Zp-0oYGpmv20_qbNcqzDeVZEyddfqukaBwuqTGp5zVQIctdJLA3vdLMLHRbcoagec259UZ9UteT-XOtVWpwJk6t54Sp9tH4kKn_UubEkaqeT5jA1heDxyLCloKbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
واکنش پزشکیان به سخنان همسر سرباز ناو دنا که گفته بود حمله کنید: انتقام که فقط جنگیدن نیست
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/65824" target="_blank">📅 12:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65823">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">1xbet_ir.apk</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/65823" target="_blank">📅 12:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65822">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/65822" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">1️⃣
▪️
نسخه آپدیت شده اپلیکیشن وان ایکس
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!
• آدرس سایت 1xbet:
🌐
bitly.uk/connect1xbet
❗️
نکته: اپلیکیشن بدون فیلترشکن کار میکنه برای ورود به سایت باید سرور فیلترشکنتون رو کشور های اسیایی یا کانادا یا ترکیه تنظیم کنید</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/65822" target="_blank">📅 12:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65820">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b88e4c73c3.mp4?token=jQG7gnnVKc5igx-AfCZiDVziLqtTVhwR1-4dD6U3znODqGgx0soqgpGM5iFuYJkeT23Vd7ioanNpuxjsE19Rt_TJfIWP02X65A68JxJY2fPm0TbOZXYQb4knCVHVBGUB5T7Wyz1F2j5V1UuNA6KTqo_Gx7UQHT0SZRgRvNcQ0SPqf_8YsJ7WwKZk_OsWgMbgnewfaicvcy6bRD3dSTuUNYS_MCWIRlTYyh9jzMZqg5G0QR6A4olzFFl_ilWmLg8X327FYcIUN93SM-7K_-eyU5QdN_AD_NSjUVZbFGuckDkluxSiNV7udEv-BWDYRtVvTp1QSdz0k-veJHNRR0E84g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b88e4c73c3.mp4?token=jQG7gnnVKc5igx-AfCZiDVziLqtTVhwR1-4dD6U3znODqGgx0soqgpGM5iFuYJkeT23Vd7ioanNpuxjsE19Rt_TJfIWP02X65A68JxJY2fPm0TbOZXYQb4knCVHVBGUB5T7Wyz1F2j5V1UuNA6KTqo_Gx7UQHT0SZRgRvNcQ0SPqf_8YsJ7WwKZk_OsWgMbgnewfaicvcy6bRD3dSTuUNYS_MCWIRlTYyh9jzMZqg5G0QR6A4olzFFl_ilWmLg8X327FYcIUN93SM-7K_-eyU5QdN_AD_NSjUVZbFGuckDkluxSiNV7udEv-BWDYRtVvTp1QSdz0k-veJHNRR0E84g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از کشتی JALVEER که امروز در نزدیکی بندر شناس عمان مورد اصابت قرار گرفت.این کشتی را خدمه ای هندی اداره میکند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/65820" target="_blank">📅 12:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65819">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hi7dR4p__CUJVQfmGYfs3YcCTtoiBJ0HAAvKmNC51Zyt2kDGT69B1-l74_29UqFMkDI45_3EJRDzgjN9MruYEXzxDmB9EXEamJVxZdQVzciFg92aIaZWinHHpf8AK9x5IeIEee7Zz6uMy7EBYnF7ctIeJqVDzGTIuGEeXS0Z4_OoipmPRRG59Uev_MT3TxRbIhbn-AvJTlbwd8EJ7p5Vp6mTP0z5Ylo_8-tPGYob2PULW1ycLKD02dBE1h78NeayM6StH53kBBzOtmP7TZFvdBRFrQPe7hYr9DPPg6u8ANkFr8mYIytRnasNBtBWYlOaBRoN-XttxkKDGbhNAxhPwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه وزارت خارجه جمهوری اسلامی در خصوص نقض آتش بس توسط آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/65819" target="_blank">📅 12:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65818">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bec45c0e2.mp4?token=nPV9soWh1Gzibo-HAecjQk5QLQi-C6lbZrvjBOkPoVhVeVebhSEOPT7DWhdZadG86dzfRg6LLAr2gR3uCNKbB6p1vDNbrB-2sJ9hDMBOXsLCGoWzulK4A1VxxaykymT3zq3mP-JO3JybQrLb9l_KzNZgdO6JRNKCr1XmiBqujUf3ELtnh6VLuNGPIlNWspoLfNwgnzrJi2e1IFeZQwGUfobVc-1ZcSnSRfpqgTTIXzoU_ATRMy2rt9qYEHF-NnXJ4ocQSbDdHgwhDAcACK0YJ6yJyLBYk91m5i44RDP3f_2C-zd_IDoDMYQiv8g7-n5JxGkEE5nUGipaUph6Mdos0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bec45c0e2.mp4?token=nPV9soWh1Gzibo-HAecjQk5QLQi-C6lbZrvjBOkPoVhVeVebhSEOPT7DWhdZadG86dzfRg6LLAr2gR3uCNKbB6p1vDNbrB-2sJ9hDMBOXsLCGoWzulK4A1VxxaykymT3zq3mP-JO3JybQrLb9l_KzNZgdO6JRNKCr1XmiBqujUf3ELtnh6VLuNGPIlNWspoLfNwgnzrJi2e1IFeZQwGUfobVc-1ZcSnSRfpqgTTIXzoU_ATRMy2rt9qYEHF-NnXJ4ocQSbDdHgwhDAcACK0YJ6yJyLBYk91m5i44RDP3f_2C-zd_IDoDMYQiv8g7-n5JxGkEE5nUGipaUph6Mdos0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
لیندسی گراهام،درباره ایران:
اگه همین الان توافق نکنن، باید دست اسرائیل رو کاملاً باز بذاریم و خودمون هم از نیروی نظامی استفاده کنیم.
امیدوارم اتفاقات امشب باعث تغییر رفتار بشه.
اگه این فشارها باعث نشه که بیان پای میز مذاکره، باید استراتژی رو عوض کرد. باید با تمام قدرت وارد شد. کار رو یکسره کرد.
بعد از اینکه تکلیف ایران مشخص شد، به مرور زمان مردم ایران می‌تونن کشورشون رو پس بگیرن و مسیر صلح بین عربستان و اسرائیل هموار بشه.
همون افرادی که میگن زدن زیرساخت‌های ایران اشتباهه، باید بدونن که این‌ها اهداف نظامی مشروع محسوب میشن
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/65818" target="_blank">📅 11:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65816">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KA8aS9UISkjk1z4YRHCzWVt3yqieO1cFDsUqwyTt_jIRltPHRLxh69bZUNv5N9HaBStgXlxNGjs4WaNDp91_yPD_svvtnhpO-Gg8iY8HsMYBoHcDtCFBtPehEK9kL75y-cgT_cmy3tRKp1BArdoqnhCzhsjsaW-0_KCG600DNBBuFWRqShTI0bMu9l8_A6LVfl5RCbOEIecDFCtoxQuFFLZg9GwlQEuGIBU09h1ilYw9bA6V1jT0aqsv-wYpYmEJY1fUrwwnQb-Fc0VsnAxpaHrzZn4Vt5iWAaOSftt8W5QfRjjqDIrrI24ZUCnmT9xrfX7oWCYxccvPQn_Uh0I_Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sYPdnqWBNwa4sIc-6A1HZzg9SW4i0H6-SHrqqEJSAGVuiuGjDRXLZL62TWFe_grM950bre45ynyXQiFf8x676aSBC18PzWrcvPclEem6xLtEv2Odz-zorQhgOIsOrw-clTeTsSEpMROew0s2L_onxlsFObwJg0pPLQ5GNKmTsdIy6NzoUwtIOZKHnVvtrEYxakX-xIKuN4hGCoNHUNQ0l8HJtBsdMMvPLhjwt92kC9MPotFBi8gBW6qEoYvkb8OZtWsIyv8ghfdODZczuvGQk5OAJ16DReXncV5xelYqXzj4GtQkMmUeBo7p1pBRQbBjzolx_sy8A9wWWJsdf_AF4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
وزارت کشور بحرین:
این خسارات مربوط به حملات دیشب جمهوری اسلامی هست و دختر بچه ۱۱ساله ای هم توی این حملات زخمی شده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/65816" target="_blank">📅 11:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65815">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mf2UP1nqJ4EGb7SVwLWxLT8F_KmYx9Y5WTmDYZYI04uwKTfuqo4R1tufBoIcKKGwjSSkPOGioqA3Zuorlff6oGr3VmukdxH1bki7tIHt87TqOYlPU-OPAaOYypUK9WL68my4zpzLFhKfmxWmcNABW_hHH__fNYYMgmJU3TNY2JH5wHhqmoQGdLyNa6km-Ct5QXSzhRAACyxQxTesnnVf-X91J4BxY1gfYJor-3PHyFGUgmwV_U3G-4EZm2oJJMvxELGtJ6btTTus-x5opCH344e1TtTIsaiL3oiMkryK1TLlLRkengzHpFJfrJjTy2SzfI_DRQzpPa2LAr4TjyzKIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آلمان از پهپاد رهگیر جدید «کبرا ۶۰۰» رونمایی کرد
شرکت دیل دیفنس در نمایشگاه ILA 2026 از پهپاد رهگیر جت‌محور Cobra 600 پرده برداشت؛ سامانه‌ای که برای حمل و شلیک موشک هوا‌به‌هوای IRIS-T طراحی شده است. این پهپاد با طول ۶ متر و چهار موتور توربوجت، می‌تواند موشک را صدها کیلومتر دورتر از محل پرتاب به منطقه درگیری منتقل کرده و برد پوشش پدافند هوایی را به‌طور قابل‌توجهی افزایش دهد.
کبرا ۶۰۰ در واقع نقش یک «سکوی پرتاب هوابرد» را ایفا می‌کند و برای مقابله با پهپادها، موشک‌های کروز و سایر اهداف هوایی طراحی شده است. استفاده از موشک IRIS-T نیز به این سامانه امکان درگیری با اهداف مانورپذیر را می‌دهد.
این طرح ادامه‌ای بر مفاهیم قبلی آلمان برای ایجاد رهگیرهای بدون سرنشین مجهز به موشک IRIS-T محسوب می‌شود و می‌تواند لایه‌ای جدید به شبکه پدافند هوایی این کشور اضافه کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65815" target="_blank">📅 10:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65814">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
نیروی دریایی سپاه:
به دلیل نقض های مکرر آتش‌‌ بس توسط دشمن آمریکایی تنگه هرمز تا اطلاع ثانوی مسدود خواهد ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65814" target="_blank">📅 09:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65813">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
ترامپ:
اگر ایران توافقی که ما میخواهیم را امضا نکند فردا(امشب)ایالات متحده دوباره آنها را بمباران خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65813" target="_blank">📅 09:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65809">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AiR_G_6gJcFZg6s2pYl0WaEU9voUU2fdOMuTff7GUhoLc9L3oHXl4c3GDVRh7pLfsNmzqw6uVDZaWR69GyMR1vTS2EF8wguw3WE9-FO5-aJlJ5neZONEOTd9QIf0uKJdMPWmf_nolq-fW0fesjN0FaHCycLCTXQE9c9chUphybnqLUjkLqfWJ1HMc9Z4WzXaWY9Blmh1ukBlR88rCynkS-jSV8pTDbeWiNiJniO7Cs98LI7BE1mCcQZEqgUL3zEk_ZUS6R08-cVQwpEUZHR0JdxauAO51pLV2moWFhrV4MPtRacYZa7EMQYo-zq6Fa1wUyqcREX5CX9R_nga-rvDVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TECsIBC7DxU3MXlI2EYNja3k80bweLis6N8GRZw62tykBDIfy6B8oDRpNebuzjLbiZKWh6YUcpR-MFYNHlxVYUsChhCE6grKJC4Tfv7gIZuawpJDJe1WqxVSkMaAiEmx7KmqE8SJ00p4qgSea7o1E0GeQ2GSKpTavCD6wVfcDwW79gyteNDxNh2tqL95DSQORcvdaGbeV7RSLTVOpy4K2-WUccccxCMxbh32AASo_FT-xlVHiA4xWgK67YDvJkeB-vDuKkhWRUbSAu5fnhA_IJvxBK41f5zsTvsJn0VGUYWZaWsPU_vPut8dIKCKlTbtofLvaEwRkGUSZnydSKUfew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uisq01iJn6R_2LJkClHOEDiGGCbZ93rA446xDgdU5J2Z4yzjFFGO2FNGMyqI8Pu62oDRyNSydwwoXCWsfkBh3Xs91IBMbbziqM9lbfPXsUW2XiPXMOLMB56LFGvelLXKNlfIPMSMXgZ6_M7UV434soZlWgVDDphHleJisL35waig00-jbdcKGvRiokySqUcTCYnzsND3yE7IiYuDHwGWKgwLKjHWfD-Hc3f8PQnQyz3xuG_JdPdND22kcpYTwhmsLItHGjor0I-R1rtplV8pskPtXpRsUKSTPFJGeXQBN7rTSnbWhiCVBRaTGpls6wRbEG30gDeTNWaAGqG6MWa5Uw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad9bf04a71.mp4?token=j24AQXws7aMIP6Ygof-dFt_V7UUvF3g7ymF81qZLYLOymHBDzLidkCHdQHsfKgSMdSnh_OI-OrQtMW5CKZP9c7VEfPQZRjtTddManJycPgjc6rvzlNE0iu8JTI8WZ4OKrAJR2HrZzeohDojz2_2ekKPhORV4-5idfqR9DKltZ6KsyUXT_GATwGoK66qyWTX2R2uquhovMXdcf0lEWpBggDih0-0CgSLWu3uZFGtMT_rnmmw7dco9A4E6DZSM2v1qn0mWxRN5adTQRXs6XuyFL3GscN9EWPragh5ML9EvCCKkCJsdIh5vtVd1OmHTTkr2hKA59TiXx45T9cREifnC4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad9bf04a71.mp4?token=j24AQXws7aMIP6Ygof-dFt_V7UUvF3g7ymF81qZLYLOymHBDzLidkCHdQHsfKgSMdSnh_OI-OrQtMW5CKZP9c7VEfPQZRjtTddManJycPgjc6rvzlNE0iu8JTI8WZ4OKrAJR2HrZzeohDojz2_2ekKPhORV4-5idfqR9DKltZ6KsyUXT_GATwGoK66qyWTX2R2uquhovMXdcf0lEWpBggDih0-0CgSLWu3uZFGtMT_rnmmw7dco9A4E6DZSM2v1qn0mWxRN5adTQRXs6XuyFL3GscN9EWPragh5ML9EvCCKkCJsdIh5vtVd1OmHTTkr2hKA59TiXx45T9cREifnC4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بررسی وضعیت راهبردی بحرانی جمهوری اسلامی پس از حملات چند شب گذشته و فروپاشی بازدارندگی و چالش عبور از بحران
متنی که ادامه می‌بینید یک تحلیل جامع نیست و صرفا یک بررسی وضعیت است از راهبرد جمهوری اسلامی پس از حملات چند شب گذشته‌ی آمریکا و اسرائیل؛ خب جمهوری اسلامی در ۴۸ سال گذشته تمام تلاش خود را برای ایجاد دو اصل
#بازدارندگی
و
#بقا
انجام داده ولی حالا در ماه‌های اخیر با فروپاشی شدید مفهوم بازدارندگی و حتی بقای خود روبرو شده است!
استراتژی‌ای که بر پایه شبکه نیابتی، موشک‌ها، پهپادها و تهدید تنگه هرمز بنا شده بود، در برابر حملات آمریکا و اسرائیل به بدترین شکل ممکن آسیب دیده؛ من همچنان معتقدم که جمهوری اسلامی قصد داشته در دوره‌ی چهارساله‌‌ی ریاست‌جمهوری ترامپ مقاومت کند، زمان بخرد و امیدوار باشد که در انتخابات بعدی یک دموکرات روی کار آید و فضایی برای تنفس و معامله ایجاد شود. اما واقعیت میدانیِ چند شب گذشته این محاسبه را به چالش جدی کشیده است!
‼️
درس تاریخی و تأثیر بر دموکرات‌ها
من قبلا هم گفته بودم که سیاست آمریکا یک سیاست واحد است؛ یعنی حتی با تغییر رئیس جمهور هم سیاست کلی عوض نخواهد شد اما تاثیر گذار خواهد بود؛ برای مثال حمله بوش پدر به عراق (۱۹۹۱) ابهت صدام را شکست و راه را برای حملات موشکی مکرر کلینتون به عراق هموار کرد؛
امروز هم شکست بازدارندگی ایران می‌تواند پیامدهای مشابهی برای سیاست دموکرات‌ها داشته باشد. اگر دموکراتی مانند بایدن روی کار باشد، ممکن است بخاطر این ضعف، سیاست‌های سخت‌گیرانه‌تری اتخاذ کند یا حداقل نتواند به راحتی به سیاست‌های «تعامل» بازگردد
شکست فعلی جمهوری اسلامی نشان داده که «ببر کاغذی» تهدیدهای منطقه‌ای‌اش تا حد زیادی توخالی بوده و هزینه حمله به آن بسیار پایین‌تر از تصور قبلی است!
❌
وضعیت فعلی اتاق تصمیم‌گیری
اتاق تصمیم‌گیری جمهوری اسلامی اکنون در موقعیت دشواری قرار دارد؛ سوال اینجاست چگونه بحران را با کمترین خطر پشت سر بگذارد و همزمان بازدارندگی را برای حفظ اصل بقا، ترمیم کند؟
تهدید زیرساخت‌های اعراب
بستن تنگه هرمز برای اختلال در تجارت جهانی انرژی
واکنش‌های نامتقارن و کنترل‌شده برای نشان دادن قدرت
ظاهری
حملات دیشب آمریکا صحنه میدانی را به طور اساسی تغییر نداده، اما به تدریج در حال نابودی قابلیت‌های دفاعی ایران هستند و این حملات بخشی از الگوی گسترده‌تر فشار حداکثری و ضربه به تأسیسات نظامی، فرماندهی و پدافند است!
⁉️
قمار واکنش افراطی سپاه پاسداران
سؤال کلیدی این است که آیا واکنش افراطی جمهوری اسلامی (مانند حملات موشکی گسترده‌تر یا بستن کامل تنگه) می‌تواند چرخه فعلی حملات را بشکند؟ یا دقیقاً برعکس، خود سازنده حملات شدیدتر خواهد شد؟
تجربه ماه‌های اخیر نشان می‌دهد که جمهوری اسلامی در حال حاضر در موقعیت ضعف نسبی با استراژی های بشدت هزینه‌زای زیر قرار دارد:
تحمل و دوام؛ یعنی جذب ضربه، پاسخ محدود
انتظار شکاف سیاسی در طرف مقابل
در نهایت، موفقیت یا شکست این قمار به عوامل متعددی بستگی دارد:
انسجام داخلی رژیم
توان بازسازی سریع نظامی
واکنش بازار جهانی انرژی به تهدید تنگه هرمز
اراده سیاسی در واشنگتن و تل‌آویو
‼️
چشم‌انداز
جمهوری اسلامی در حال حاضر بین دو گزینه سخت گیر افتاده:
ادامه مقاومت تاکتیکی با امید به تغییرات سیاسی در آمریکا
پذیرش نوعی عقب‌نشینی راهبردی برای بقا
هیچ‌کدام آسان نیست. سیاست عملی رژیم در دهه‌های گذشته بیشتر «عبور از بحران» بوده تا حل ریشه‌ای مشکلات؛ برجام هم نمونه‌ای تاکتیکی از همین رویکرد بود
🔴
ارزیابی واقع‌بینانه:
بهترین سناریو برای رژیم: تحمل ضربه‌ها، مذاکره تاکتیکی، بازسازی تدریجی و انتظار تغییر در واشنگتن (دموکرات‌ها) اما شکست بازدارندگی قبلی این محاسبه را سخت‌تر کرده — طرف مقابل حالا هزینه حمله را پایین می‌بیند
بدترین سناریو برای رژیم: اگر اسرائیل/آمریکا فرصت را غنیمت بشمارند و حملات را ادامه دهند، رژیم ممکن است به سمت «همه یا هیچ» برود (بستن تنگه + حملات گسترده) که می‌تواند به فروپاشی سریع‌تر و یا حتی نابودی زیرساخت ها منجر شود
در مجموع بنظر من رژیم اسلامی ایران نه تسلیم کامل را انتخاب خواهد کرد و نه جنگ تمام‌عیار را؛ آنها می‌خواهند زمان بخرند، ضربه‌ها را جذب کند و با حداقل هزینه از این مرحله عبور کند تا بازدارندگی جدیدی (بر پایه تنگه + هسته‌ای پنهان) بسازند!
اما شواهد میدانی نشان می‌دهد این راهبرد پرریسک است و موفقیتش تضمینی ندارد و تحولات سریع (مثل حملات دیشب) می‌توانند معادلات را یک‌شبه تغییر دهند؛ بنابراین حالا رژیم اسلامی ایران صرفا در حال مدیریت انقباض است تا زنده بماند و در یک آینده‌ی خیالی به امید شرایط بهتر، بخشی از مردم را کنار خود نگه دارد
!
#hjAly‌
@HutNewsPlus
|
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65809" target="_blank">📅 08:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65808">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">در ۶۰ روز اخیر این سنگین ترین حمله‌ی موشکی سپاه پاسداران به کشور های منطقه بود  حالا باید از ترامپ پرسید، کدام نیروی هوایی و کدام موشک ها از بین رفته؟!  #hjAly‌  @News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65808" target="_blank">📅 08:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65807">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">در ۶۰ روز اخیر این سنگین ترین حمله‌ی موشکی سپاه پاسداران به کشور های منطقه بود
حالا باید از ترامپ پرسید، کدام نیروی هوایی و کدام موشک ها از بین رفته؟!
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65807" target="_blank">📅 05:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65806">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFgUZlGNVQWlctxUleQoBX7XV5DDNFKOzIfzrmJNDoG-gBW9DyU7A1jg7f3r98QgmkWWn4JRlyLbusA4F-xh95UugFmH_tJ2UXAB2HKy8-W8oA-H7MO4STQ9EHDg1NGtGm7wJ24gG_KCr1vTBq976enfvrVTxe06wkyuJcKoKYpnuu4oYijLNynMDbo4A_aFblagIQhJMY6mjE9TajXn4HAl-r9Pfnj48JPaWCJria-zDOCebImlBkcmAFmTpNOeyNXY-U0Uk5JG9JQH4CLmF8Mj47Yap7ixr_Ufc6Hotvz98H-x9bbwEdWFoJ8IytLPCnCgxa4-p8OpgZjMEyLh5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کردستان
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65806" target="_blank">📅 05:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65805">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7vOk8vnUfrJ5pHtU3etysgAMwNphcYcza-L_BNHx8S7mMlRrqgDuMY2gS5c1q0fRj7bukJvTfxwnGioanKWK3rj4ZLr4QpCGlJQcj0wIw4qjyvTZG0uPR4-8x-rE433Jx_mpHVesGGcu018hTlQOPUCjIPvyq2YFvmexESYRYbbmB3LbN4gmJawwu4wi-SI7L7B4gbl3zNDhYBy_qaK86tPIQdBVcUVkGOzTyAZsHgjwZ_m_wNpz-vX3xq4BNDIuMyy19jFg2fMlg4mTyUnijkIWAGlpXZMlEuFiU7B6jKFdqRs2sROlCGOag5PQzN4v-U1cM6agbb4EqzJTjDOKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ارومیه
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65805" target="_blank">📅 05:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65804">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfk6lgEgbvWTpqarPZ3XfzxKyfqyttAF6cEeswxM1-ttZS7rkGWr2EJuI3nNX60KQs69R_XEYEl3bKNWBBi_iOz7W8gEnbGIxDO1u0hrxJDJ5PE8zjKNSujFyf0UfRzwCJx9yaceHzY5n4FY8kghfaXRz0O3WOUnrZAb-QUutalY_kBYiyzpYxGzMrSBHzQHwAVdvH4on6fgXUmPAFq2uhPFm1H4FTZrMMh5NbsI4bO6CPuAYndcKwiWw84cbL9IBmQJDNR6ra9RGB7Fn45BnOpNjGQsvOokBuAjC11E3l8S3U4WnFRB_IJfyeGkAhHZjq1o8mk7XyNSyn-pPWqPpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65804" target="_blank">📅 05:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65803">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ofp-c4yU9COErHV_r5E4NmRUfIgYYhwi3TYpt6zR8LqtDww7P9091RK95kbWMRF1S5Z823eMzkJvRhnNxH8myVK22jllWmklKtQqHeLC_1-eqrZdwJblSh6WGjc_hmuxxXFSBDTnaWcTRkhdYBr_JTFPy_vL3yAx3ieeRKSMN4x49qJFbYnJ8_KsoEe0cW5d6La_RnTPVN11nhCnqQ-XoG5sOYPSgaOo4xjHSzY6-2RpIPDE6A1Pxp39T-IyLD2R3sCX0O3IaCqE4OugwOwJo7tBQ35JmwLHfhw98XSCkfY-RUYgw5RBli5RJbE6WHLDxTQRUp2Of_18Dpcn7rVJIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
زنجان
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65803" target="_blank">📅 05:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65802">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l94mlJdY-mFeO5yTZVLWNGNeJeTaDCrPG4zpWCYprPtKYwpWKJi-NK6n-bQAOtgwl72DEfKo_tyNtxSuzYrrl0HKNlVNAMgdF4vQMyie7KEl4wQV7tyTy4i34wctkhHQRNnddzt-cqf1Z6QW9f8dvEbzmz_IQFxT_oSW0UcrJhFiK6XMNkXARrYNVuWnJYsaK2RavIpIjrWZr8HJ5eVtoqdOrlNoIfFNJF9mtJDhNjJ2lAhkJjhny5XPEVvfdqo5bJ5TqaPacR0XTEHGgmuDKy-bNzyykzW-Iz8YukpcsNh9TXCDqffyJPdeFUbAPeOdNs2IVeKVDUBI6s-LKg5WXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون خرم آباد
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65802" target="_blank">📅 05:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65801">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین سپاه آغاز شد
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65801" target="_blank">📅 05:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65800">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔥
فیلترشکن پرسرعت و رایگان اسگارد
• نسخه 3.0
متصل با همه اپراتورها
✅
کاملا رایگان
✅
بدون قطعی
✅
بدون محدودیت حجمی
دانلود مستقیم از فروشگاه گوگل پلی
👇🏼
https://play.google.com/store/apps/details?id=com.vpn.esgard</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65800" target="_blank">📅 03:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65799">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65799" target="_blank">📅 03:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65798">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OCNJInQCklrUcFJPKvrOCdJyiE7q3dDo1OoaGoSy66RLTczF2i-X-qNrDW9cqoU3ecbPcxxSeqdm7NQZpin7rYa99pqt3c1pa_b64Nw1Fox565B2JeqWzeBkT90_MeHIKxgnHezCj75vyISS4AhLoEUCoWVp0FQ9c88Lyp9BNxz9_0jg5WXSmvLFzQaob-tZ9zdPzUTOkURwUr4i5hGL6159Wlxcyu5TtzAVVskOHX6kCjjYw3awoLKriF46K2tS6_slewP-eWpkdF2Wx_QDstVzeMziTnx-aQ6lvLGBTKrkbNFnYy90RHULLMx1-aB1IDEABhTZRkTBWY1tpEnz8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65798" target="_blank">📅 03:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65797">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
ترامپ:
اگر ایران توافقنامه رو امضا نکنه، فرداشب به بمباران آنها برمیگردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65797" target="_blank">📅 02:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65796">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
ترامپ:
مستقیما با مقامات ایرانی صحبت کردم
«بمباران به زودی متوقف خواهد شد»
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65796" target="_blank">📅 02:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65794">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
قرارگاه مرکزی حضرت خاتم‌الانبیا:
نیروهای مسلح جمهوری اسلامی ایران به هرگونه تجاوز و شرارت ارتش متجاوز و تروریست آمریکا در منطقه، پاسخ کوبنده و قاطع می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65794" target="_blank">📅 02:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65793">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wh_XVEYAb_gssVpwUthgXu7-crGwh_PfIGBWUkSny7pdDeAx62LObtHu_8J5TAzyKWOGE9CSFtq-aDBfmD_sZsPAZ0VEIiSiaBcnRQlzntuZBcvW9Dl1uy0BZfAzvohKnKxxkmdaVW9StU88ZkEo0PAmchUJMaAxN_G_fz8AphvceiJZvoUmu_4ReGpVHhJSYlfM-7PAYiMx3poLwyRf1VncyNa2U-JSWgAM_m8YTUdR45hqUeZhAIrYkoOV_bSYzZRVAHWkOieXjn-WNqj138P_sEtG2Z4sjPbcSSwWg_JW6cx6H1HZ16pHqusAxiu2_KINkXBHuMhsjdaFEerEqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
مارک لوین :
دور دوم حملات به ایران همین حالا در حال انجام است. من کاملاً موافق آن هستم.
من درک نمی‌کنم چرا حملات ۴۸ ساعت پیش اسرائیل، که در پاسخ به شلیک ۱۱ موشک بالستیک به کشورش بود، این‌همه انتقاد به همراه داشت!
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65793" target="_blank">📅 02:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65792">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
گزارش هاازانفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65792" target="_blank">📅 02:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65790">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اگه لازم باشه آخوند حتی تا دوسال دیگه هم مذاکرات رو طول می‌ده، ترامپِ جاکش تنها راهش اینه یه لشکر ۱۵۰ هزار نفری آماده کنی و تو تاریخ جاودانه شی
🌂
#hjAly‌
‌</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/65790" target="_blank">📅 02:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65789">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
نیروی دریایی سپاه:
دو کشتی که قصد عبور از تنگه هرمز رو داشتن هدف قرار دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65789" target="_blank">📅 02:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65787">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‼️
بزودی  @News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65787" target="_blank">📅 02:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65786">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1713aa9451.mp4?token=BjrCWt7Z3s3L2dXr5GhHVXBM1mrLnoWcLa0EXHGPzsmDPzq7f1u9poDEM9FcuLZgyGb2qtD3PBCmkwVPw0YLOuYBddjuPfS5RAGQEs7ERNX2UjN1evWAIzyCVm2fEfF7NBJfRFs_votB8EWphjlujiuzw6vcnjxFf7kod8pFgaIFhy42iyRV_6lesy3qwd_GzleOsub04TqkfGI1QVhUxC_hcp3KvccYWUFMmneow3Q1w7A6t4PLXUMn7eN5blfcpCdTo1licy3IVx-PIShJjDoorR_GXPaOkQHniLBboj9KANh5DOq2wQZWNh1bFkAxySCFVl5Cw9ZfCv5D8Vaivw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1713aa9451.mp4?token=BjrCWt7Z3s3L2dXr5GhHVXBM1mrLnoWcLa0EXHGPzsmDPzq7f1u9poDEM9FcuLZgyGb2qtD3PBCmkwVPw0YLOuYBddjuPfS5RAGQEs7ERNX2UjN1evWAIzyCVm2fEfF7NBJfRFs_votB8EWphjlujiuzw6vcnjxFf7kod8pFgaIFhy42iyRV_6lesy3qwd_GzleOsub04TqkfGI1QVhUxC_hcp3KvccYWUFMmneow3Q1w7A6t4PLXUMn7eN5blfcpCdTo1licy3IVx-PIShJjDoorR_GXPaOkQHniLBboj9KANh5DOq2wQZWNh1bFkAxySCFVl5Cw9ZfCv5D8Vaivw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بزودی
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65786" target="_blank">📅 02:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65785">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">تا الان ترامپ هیچ اظهار نظری نداشته و حرف هایی که بهش نسبت داده می‌شن فیکن
#hjAly‌</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/65785" target="_blank">📅 02:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65784">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
شبکه ۱۵ اسرائیل :
موج اول حملات به ایران به پایان رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65784" target="_blank">📅 02:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65783">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
صداوسیما به‌نقل از روابط‌عمومی سپاه:
گفته یه جنگنده F16دشمن رو زدیم
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65783" target="_blank">📅 02:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65782">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">کصننه هرکی نیروگاه بزنه
#hjAly‌</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/65782" target="_blank">📅 02:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65781">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
#فورییی
؛فاکس نیوز:
اهداف بعدی نیروگاه های برق ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65781" target="_blank">📅 01:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65780">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اسرائیل هیچ نقشی تو حملات امشب نداشته
#hjAly‌</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65780" target="_blank">📅 01:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65779">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
انفجار های مجدد در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65779" target="_blank">📅 01:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65778">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEohZVGOuxE5Nne_S1fyYAEvjmxieHDDw-zzLdH8S926ebFIK4dval48SfZDMxMixr9v25idhx9E0_sDtrq7N30eWZq_CrkhQY3Gm3ByrG_oyK5kva88PojdebmKg2T_l9J0GrtI3mOPWepU1BSUYJgqYteZdzpd8PDaxNPKy5RFqvtdTT42eET0EG_62a3AuzLItec-Uo2HUKyTpUP5D67NIheWV0lcmPH_JqUwRGL-cnoldiWpZYxxXfxLr4M1wuOcXMkL_t1EV8ddfLgslrFXJHJel3aLeo_LEBbgkEhKZCjVh_0VBQDmAEt3bX_Y-xeOTCWY3xzj5oeT9hxl5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
یدیعوت آحارونوت مدعی است که یک کشتی جنگی آمریکا در تنگه هرمز هدف قرار گرفته است
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65778" target="_blank">📅 01:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65777">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFbPxohDBfaHXLYOM0jmWt3hjgSHFdKX8lRWYTqqjAc0tsiMny1QEs0T2i5f8z-Y6u6_6Lb5ckbADTzmq2axkyyFLY78OgnllVMpnL-vtd5kdRkxyd-k4WktP384zDqFxb_nekTWn6w-D8IXEMsAbDWumQntg5blv7vS8SizXBLSDNkrUS2gPvN03oLTriw5qL0wOBRbQCt_igI0vVn3f1LKRsxM2k_jk1mGt1hzexOOchckJaIs2Q1gbf2VvEzVzoKQV3mfHsODVT4t24Dys4Ae-3EfzO80gt15lbsXJJACWqXVmQlxRHOTJnqw9e1vXnxd3gNi6japJIP8um5Rzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
خبرنگار المیادین از درگیری و تبادل آتش در تنگه هرمز خبر داد
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65777" target="_blank">📅 01:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65775">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P2C-4gOBRu15OzSP8yYzUHvWCU2Z9jLZ9xW2U_4F9QAovQ9mwSsLQHATN9cIvFCIqKV_FpiBzSj8cVrV3rnYZ3Xqnjv7iT5ASHaz8RoqHPx_S93lq9EBVbcA82fw3hqzf0_jjInK7gs3fuDnG-XcOLCT158i1qBS2aicdO11J3zjKSV6MF4gmgIoTGkHCmX3rayn9eAL-WQl200dMBCKRkTl_pa23OcnItQrxn1gn_RzKtER0SORNApT9A2LDBD2ntjG1U2n4U2k0cffk1TjOCuNMwAJzRrp1OZI5S2ZLsZjETSOdGcVaFcUCFo5Sz6s_4G5PuzHb7qc7KMuAwE87Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qn4BESCG2Enm72Kr82oNVYRBaGxf7wgMMYhaeBZ8eQQECzOGqlRqRJh9nROxK2Vr20UTdzSzgxAwb665ybomThkz_mJlqy6WuxosmTXNS8lHlMSnSMKak17AQNM13QUmJEKQ3wWFQwoXxyzshnZz74DRrkI50fPP0KuILv7coJMD3SEO3_1LkW0UdbPggGTqmTyb_JYHcrvRnRZ--js1N-k177q58FLASLoz-wIgYBY7NsEz2dXhsu7KRm9qlUxDcqQ4aSKKMVEdRmy6-YYWSzJQwfj18aX5pTDC4h0lxK__Rxyp0VLIl-gtRsuRF-l_SRz28l1pHtvcKUhhi8bCfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
دو فروند هواپیمای سوخت‌رسان هوایی KC-135R «استراتوتانکر» در حال انجام مانورهای سوخت‌رسانی در جنوب استان هرمزگان، غرب تنگه هرمز هستند. این استراتوتانکرها از پایگاه هوایی پرنس سلطان در عربستان سعودی برخاسته‌اند
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/65775" target="_blank">📅 01:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65774">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UB_eT11ZU8C5Q6cZgXZ1Oc_Gc9xDFqyyPxvQ4YvzUgGJE2lVJeEF8rGIrscDRfCClASPtF6iN_qUdX_nUCrfcCHxFCKkRjQ79PSbk8O4qyVJ9fkFEco-bM7IH4F6YciQ5Fg4ULszv6cGPuas7YEGqOiWmupJ0Bzg9QM1fCs5luHkZy2RiEsVWcd9lRnNNBe9hdb6jCnxSluUZJAAuZ05FuEXyQD_NP_MwR2R9J78nqqVnEt0qN_kM6_FUeZ18mSpj7VnyQfHQ0wUQEYL8QllYyMooy9ZQyyQQhRaPZ25legM_sReH11EqigaOQbejpgtH14fxhoTjlNHzpfM7Hko8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
دود انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65774" target="_blank">📅 01:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65773">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bbd6f07ba.mp4?token=hkbZeOH5_CYuo7ZkLAxLM26yktpmNVW-1AoND8vgg8N7IHT-FtzY5rjUld0wEqp2EEYopb35CU6ZS64RfzMrvf1VBytueJEjUSjsit5d_2--I-P-N7oWJD46Nf7ZdlgCIHIlx0_bgAuMdqdw1q14eDfdYevRlgs7Tl_mSmC_lGquXJ1JzMiA_YTezRG0ejBeMjqpubUbhFMkr7iYzFPFKX6b4_AQCPiOPWBTp1v_4YRH1E5Qq0AGu1Pxtu-LaWVUJMOTtr7Gh5aNfa7mfOe5Pfzh_4xsoGaFmMED8sZIjd1ftI2H6VjSfhbDPHVXFStL1wWkjZitQJDmRhYk-1tIZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bbd6f07ba.mp4?token=hkbZeOH5_CYuo7ZkLAxLM26yktpmNVW-1AoND8vgg8N7IHT-FtzY5rjUld0wEqp2EEYopb35CU6ZS64RfzMrvf1VBytueJEjUSjsit5d_2--I-P-N7oWJD46Nf7ZdlgCIHIlx0_bgAuMdqdw1q14eDfdYevRlgs7Tl_mSmC_lGquXJ1JzMiA_YTezRG0ejBeMjqpubUbhFMkr7iYzFPFKX6b4_AQCPiOPWBTp1v_4YRH1E5Qq0AGu1Pxtu-LaWVUJMOTtr7Gh5aNfa7mfOe5Pfzh_4xsoGaFmMED8sZIjd1ftI2H6VjSfhbDPHVXFStL1wWkjZitQJDmRhYk-1tIZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#hjAly‌</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/65773" target="_blank">📅 01:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65772">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
وقوع انفجار ها در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65772" target="_blank">📅 01:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65771">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XJajVGqy7l5dvNdmn2Ycj9quzexE-feSRYZ6eiBu-YkmsDx5WZRMKbkkT5zPWQM531hbsFnh7K5Jfz0BJqqydtSZog607iDgjko0GhuaWX4tof6hMBJSBkyKsNy1MVO94brMfSVuqPj-7aZC9izlBY7XRqYbJlRVmcsOrrCO9EFmh5vXnhXxTnpbcpid49VSlbtZ9liSa52vVeQjonsYCqMP6kP0700SnzAAKMeTYNlLtZwtZ0havVGxBFARhdlHfR6BbxU2xXgxCgfP6xxiORZOr8UCF0jw_p-Oo2ru-fu_Ba8tmjMvKuR1MJe5vNMY2sOPMnmnGR8Vs2EvfV_sSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
توئیت جدید سید مجید موسوی
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/65771" target="_blank">📅 01:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65770">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
گروه هکری حنظله وابسته به سپاه:
آغاز پاسخ ترکیبی، قاطع و ویرانگر اتاق عملیات مشترک فرماندهی سایبری حنظله و سپاه پاسداران به دشمن تا دقایقی دیگر رقم خواهد خورد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65770" target="_blank">📅 01:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65769">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
حمله آمریکا به پایگاه شکاری بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65769" target="_blank">📅 01:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65768">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ekVXOYX75OFSIJimaWfaacDzx9rTu0C1o4oQGXXTi2EJgDULi5oMc7IFcjOs9nV0CTqKcYkKswuqzWRTYyn9qL0F4lDPsksCUR6mTjDQV1vMtvYgA2JCZqq03EovRMDXV7Fot7bPP4V_AxfZ7bHhUKbdz9P2yb29EavuY0HIg8kETExcSp3F60bngUDm8vAyb20Rg2qOfAddnbwH4_rKXbNWro7V2kpMYb9NuFo3UR7Jw4ZMjDuQz2HLlolN-p2NaPJXMN6CR8YnL4_yu4DHiQlHRPMS9icrkBuhMSsq5nBp9zX34ud8SAQpgCFg3D_0UPK3VpA1hw_KSifeoPEUeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا قدرتنمایی کردن برگردین حمله کنسله
😖
#haa4m</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65768" target="_blank">📅 01:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65767">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
خبرگزاری مهر گزارش داده که میان نیروهای جمهوری اسلامی و ایالات متحده در دریا درگیری هایی رخ داده
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65767" target="_blank">📅 01:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65766">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dI0-HHYnSoKvlgeytzo-qnLzSPhgizSIU0elsushTyP9MI5u7CREVwrvh_BBuYRuO6hvkZiBmEulUBZrAAYDhLJ7Z2Zrg7bGg2pGKemCZ1suc0jywpXgmuYbzocEW-OC7QhcqDpBWjwPEPFceFjM56O-K16iLmk85n7ovphoYS9l4-CLL69dmN3JTwlOH-J7Vs4tsK_AsYBCbRv1vIs-3Q6DHZUx-4V5Dm4bJVo1qbvtCTu7jtKFM6A14SjLNCTnXN-p28o8S4l2uke3xwsCfitk8PTOezd097ya9MYwHsEzTNy6xnWtiU3qWiL-Z847TnCYlFNy2fOxTO5oeiFqeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه مرد باید با موج انفجار کوبیده شه به در و دیوار، نگرانی چیه آخه
#hjAly‌</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65766" target="_blank">📅 01:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65765">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
گزارش ها از حمله به جزیره هنگام
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65765" target="_blank">📅 01:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65764">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
منابع داخلی:
تا دقایقی دیگر پیام سخنگوی قرارگاه مرکزی خاتم الانبیاء در پی جنایت آمریکا و نقص آتش بس
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/65764" target="_blank">📅 01:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65763">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
وال‌استریت ژورنال به نقل از پنتاگون:
این حملات نوعی اقدام از جنس «دیپلماسی اجباری» است که هدف اون وادار کردن جمهوری اسلامی به ارائه امتیازاتی در میز مذاکره‌ست.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65763" target="_blank">📅 01:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65762">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
فاکس نیوز:
موج‌های دیگه‌ای از حملات در راهه و درگیری فعلاً ادامه داره.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65762" target="_blank">📅 01:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65761">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">یه انفجار شدید تو بندرعباس همین الان رخ داده #hjAly‌</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65761" target="_blank">📅 01:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65760">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">یه انفجار شدید تو بندرعباس همین الان رخ داده
#hjAly‌</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65760" target="_blank">📅 01:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65759">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای انفجار در بندر کنگان
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65759" target="_blank">📅 01:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65757">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nW_MhFEqQ2wdUUsAZN0ThJ5dsYO1x_haEw0uB017dMxjtpS_L9QcAH-NIdNYwW1C6GuJ_sD4q9qnx236YsNcxGpk8dYO9ytmZy0i9RZVnQoHMgXWPJkg2JyFti_h-1-nDA84Q35BAjveD4TW-OOvjGi8zS9kWUsfwdf2SYOqMSGSutR0R1feAf7WYWFfBHeL_dRi1krwLmRQBSpLGrC7mTDScSu4_1oMBvsOHTt6-2977kozskqysXpT2lAlKD6FGeropm1iuW3Xje-Q5Jc23kcR9ky-PXiUT4QeQOIV9UesB7pNXI2cUQZ9VhHSvX_jSqkR4bbCiNhiMSqWHzwsBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا وقتی یه ترور کله‌گنده تو کار نباشه واکنش سپاه شدید نیست، مثلا دیشب یه پهپاد فرستادن بحرین گفتن خب بسه دیگه #hjAly‌</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65757" target="_blank">📅 01:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65756">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
تسنیم:
هم اکنون یک کارخانه پتروشیمی متعلق به مجتمع گاز پارس جنوبی در عسلویه بمباران شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65756" target="_blank">📅 01:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65755">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
اون طرف اسرائیل هم حملاتش رو به حزب‌الله شروع کرده
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65755" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65754">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
حملات مجدد به میناب
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65754" target="_blank">📅 01:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65753">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">تا وقتی یه ترور کله‌گنده تو کار نباشه واکنش سپاه شدید نیست، مثلا دیشب یه پهپاد فرستادن بحرین گفتن خب بسه دیگه
#hjAly‌</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/65753" target="_blank">📅 01:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65752">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
مقام آمریکایی:
این دور حملات اهداف نزدیک تنگه هرمز هستش ولی گسترده میشه در ساعات آینده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65752" target="_blank">📅 01:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65751">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
حملات آمریکا به بندر کنگان
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/65751" target="_blank">📅 01:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65750">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
گزارش هایی غیر رسمی از وقوع انفجار در عسلویه
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65750" target="_blank">📅 01:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65749">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🚨
#فورییی؛ سنتکام:   نیروهای فرماندهی مرکزی آمریکا امروز از ساعت 5:15 عصر به وقت شرق آمریکا، به دستور فرمانده کل قوا، چندین حمله دفاعی دیگر علیه اهداف مختلف در ایران را آغاز کردند. این حملات در واکنش به اقدامات تهاجمیِ بی‌دلیل و ادامه‌دار ایران انجام شده…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65749" target="_blank">📅 01:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65748">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از شنیده شدن صدای انفجار در اطراف قشم
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65748" target="_blank">📅 01:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65747">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gu9Q_PEM_9wpIlV1zrtcEKYd1ObiZaG1mzrmitGxqJDUbMK4FxTq4rFD2qtW4jOHUYlVkjyZ3mojYbma8AuOw9DN3jDf6_oyu__wBsT0ZWNKBUGQN-QB_-srtDGb3xXec6Q5uZbb9Rg3QCH8WLN9ix_0IB1yESSX1d6rLlRR8cwu1cZuF6bXLHC3lDITvY1-hK9kuLBpUaUbCmN4-RaKIofco-VSU0X1Mt9MMSBBKO5fLUZtUXpDD8bGcThUDrSzq48PEstFtXy3VxlSnlYcA3rY9dba_iIztizoa1PIp-TIx1ho9aKLR8qMJWMHzY0alKU908dLQjNmdJ4a59Xw3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فورییی
؛ سنتکام:
نیروهای فرماندهی مرکزی آمریکا امروز از ساعت 5:15 عصر به وقت شرق آمریکا، به دستور فرمانده کل قوا، چندین حمله دفاعی دیگر علیه اهداف مختلف در ایران را آغاز کردند. این حملات در واکنش به اقدامات تهاجمیِ بی‌دلیل و ادامه‌دار ایران انجام شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65747" target="_blank">📅 01:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65746">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
مجدد، انفجار های شدید در بندر عباس  @News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/65746" target="_blank">📅 01:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65745">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
مجدد، انفجار های شدید در بندر عباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/65745" target="_blank">📅 01:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65744">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
انفجار ها در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65744" target="_blank">📅 01:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65743">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر از فعال شدن پدافند عسلویه
خبر داد
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65743" target="_blank">📅 01:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65742">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
گزارش هایی تایید نشده از شلیک موشک از تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65742" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65741">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
تا اینجا تمرکز حملات به خط ساحلی جنوب کشور مربوط بوده
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65741" target="_blank">📅 01:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65740">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
انفجار های مجدد در میناب
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65740" target="_blank">📅 00:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65739">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛ رسانه آی ۲۴ اسرائیل:
شروع شد
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65739" target="_blank">📅 00:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65738">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای انفجار در میناب
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65738" target="_blank">📅 00:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65737">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از وقوع انفجار در قشم و سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65737" target="_blank">📅 00:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65736">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فوووووری ایران اینترنشنال :    جنگ شروع شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65736" target="_blank">📅 00:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65733">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر:
فعال شدن پدافند در غرب تهران
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65733" target="_blank">📅 00:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65732">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران: پاسخ به حملات آمریکا دیگه فقط جنگ منطقه‌ای نیست اهداف فرا منطقه‌ای رو هدف قرار میدیم  @News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65732" target="_blank">📅 00:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65731">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران: پاسخ به حملات آمریکا دیگه فقط جنگ منطقه‌ای نیست اهداف فرا منطقه‌ای رو هدف قرار میدیم
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65731" target="_blank">📅 00:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65730">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
سفارت ایالات متحده در بغداد: از عراق خارج شوید
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65730" target="_blank">📅 00:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65729">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما: هم اینک صداهایی از دور در کیش شنیده می شود که منشا آن مشخص نیست  @News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65729" target="_blank">📅 00:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65728">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما: هم اینک صداهایی از دور در کیش شنیده می شود که منشا آن مشخص نیست
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65728" target="_blank">📅 00:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65727">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65727" target="_blank">📅 00:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65726">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
فوری از پیت هگست، وزیر جنگ آمریکا:   سنتکام امشب حسابی سرش شلوغ میشه؛ چون ترامپ گفته قراره ضربه محکمی به ایران  بزنیم، و دقیقاً همین کار رو هم می‌کنیم.  @News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65726" target="_blank">📅 00:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65725">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVuOxYFVYynbPPlVP8VDq86jQ7XSuV7h1VNRSUOCVhJASEGdRdPJQ3i8AXstaspoG8PE_NGt-QyP_poVmqQ710kto_FfmyxLg4Tr5IWOjxkNFdTEcP6qJVSrSmvYRtOwt-BOBX98z5tfJTSlNvkcb-wmBlbRhKlMCnjBs2Mr2GoZ30sQrqoXbEIiXgKCnHk3-YqOONGv9_xyy38EgfPy4iU31iflkti9lIlfDIbSu17H7LMEyrXxFy_9TudzCS40rg-NMEESHN1GWvrplHXc_BRxpLJ3CHVItOchmTmHP8dfqDUWin0TRwfPYV1dZJ4-PYtF_yMqNuvgKUys-4QErA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یجور مذاکره کردم که تو آتش بسم هرشب جنگه
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65725" target="_blank">📅 00:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65724">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0911dd57d8.mp4?token=hrz3YkSeHSNYgPsFi7J5jmxZQnFtqLTEUYRdHH59Aed58HSE6tY2FzXecpmM5mtMYmmwVQ_YJ_XtD28zU71NKvFpJAbtgWamEDhR1CUYkzs-XR9H7wv9VnG1uSKFbMaIxkR3znTZDQSuOgOMw8pLckDSxguXqSQeeOaIIA9n2LOLtxzSivzj2FZ-7cZ7pjGrmlqNbVTPqhikKgsCw21pxQh2-TFnCuXzm5QwmzIx3SakEx578OL9nOTgWvSpZMJcxA3LIGjuo_8hLucCOr150c0WIIEztNIrrOBlAPi6MS9wrjwbgX6bu7dnnWgMWW88Up_Q7qXuFUT99_e218V_Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0911dd57d8.mp4?token=hrz3YkSeHSNYgPsFi7J5jmxZQnFtqLTEUYRdHH59Aed58HSE6tY2FzXecpmM5mtMYmmwVQ_YJ_XtD28zU71NKvFpJAbtgWamEDhR1CUYkzs-XR9H7wv9VnG1uSKFbMaIxkR3znTZDQSuOgOMw8pLckDSxguXqSQeeOaIIA9n2LOLtxzSivzj2FZ-7cZ7pjGrmlqNbVTPqhikKgsCw21pxQh2-TFnCuXzm5QwmzIx3SakEx578OL9nOTgWvSpZMJcxA3LIGjuo_8hLucCOr150c0WIIEztNIrrOBlAPi6MS9wrjwbgX6bu7dnnWgMWW88Up_Q7qXuFUT99_e218V_Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فوری از پیت هگست، وزیر جنگ آمریکا:   سنتکام امشب حسابی سرش شلوغ میشه؛ چون ترامپ گفته قراره ضربه محکمی به ایران  بزنیم، و دقیقاً همین کار رو هم می‌کنیم.  @News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65724" target="_blank">📅 00:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65723">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/431e022a4d.mp4?token=iky82JnJ7JbcU3WkAfdUBMj8PR04gukLeBMUMoUAW6rLrNEiBcL_0a06HGZekeukZD7UQHo-uvFWPV_GcQCvZZGhI8WFaZGzK5cJ4zLHwBSVcWHdjumcYSkCmuNGetIw96rFZnpQAcB-unfJxFk26JeuSsqadmi41N-7YBCsBSX9DWZ18g0SWbWO7WHZ_VlDoreINjvJ0eCJUqwRggxj81NPGpdr4ywViypiNE_Z3ndBmlfPXCL2elU4cFiJDBUzKm58agE0vHxN3nR5siN3p5L0R8vHT8kQ0MrUc_wyCit54hXfhOadq6jNKsVYntAecNlQnOljkevBnPtPxpUY6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/431e022a4d.mp4?token=iky82JnJ7JbcU3WkAfdUBMj8PR04gukLeBMUMoUAW6rLrNEiBcL_0a06HGZekeukZD7UQHo-uvFWPV_GcQCvZZGhI8WFaZGzK5cJ4zLHwBSVcWHdjumcYSkCmuNGetIw96rFZnpQAcB-unfJxFk26JeuSsqadmi41N-7YBCsBSX9DWZ18g0SWbWO7WHZ_VlDoreINjvJ0eCJUqwRggxj81NPGpdr4ywViypiNE_Z3ndBmlfPXCL2elU4cFiJDBUzKm58agE0vHxN3nR5siN3p5L0R8vHT8kQ0MrUc_wyCit54hXfhOadq6jNKsVYntAecNlQnOljkevBnPtPxpUY6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فوری از پیت هگست، وزیر جنگ آمریکا:
سنتکام امشب حسابی سرش شلوغ میشه؛ چون ترامپ گفته قراره ضربه محکمی به ایران  بزنیم، و دقیقاً همین کار رو هم می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65723" target="_blank">📅 00:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65722">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
ترامپ ساعتی پیش با تیم اصلی امنیت ملی‌ش در اتاق وضعیت کاخ سفید جلسه گذاشته
جی‌دی ونس، مارکو روبیو، رئیس «سیا» جان رتکلیف، رئیس ستاد مشترک ژنرال «دن کین» و استیو ویتکاف در جلسه بودن.
موضوع: ایران
@News_hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/65722" target="_blank">📅 00:28 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
