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
<img src="https://cdn4.telesco.pe/file/kfHfrG-F7S42UZS4SkgpODQGFGeM6JtXVwaLEKrXz2mdlO-Cgb-pfo67mIceLgv44P1DqBVtlh6fVs5GhuWwu4GLWV7Li3W4MPlH9EExvyV4Wk4s-l74tje4kov7EsM33sLMjq1l8bTfH7cyWyJVWSJQmuvuRhFpf-3VMEK9fDYjvgVKsxIyNrnCfZxLlvscXVSeKm3ylgQRnz34821peSBPNmDQHaDTmjr4XZrkrQw_wnbKqc05FfDf0ATgongMfsOLQuZY_WrGhnfRYctuDDFIV4thZVHi-s2R-se_A7zBVHEFJ5acOXQEjh6AQyQQ73pRJySHt-Irw0FjCnwQmQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 609K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 19:17:59</div>
<hr>

<div class="tg-post" id="msg-28870">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cy9-8enC0EdoK029ZLbQIxSKfW0fhRh7Fyo_T08wTNSflGANaV7vkQS3vF1B6WcYaiEpV_dwOAFEXVeuVSTR0YXIPhz_sj6dqiBIsl4Zkj-9kzWohcdlCQEYT0GW8zJ5prQvld3iLLu6IUMZqpWOXxV3iE9aSYFg63ZlzmH2dIOYMZr3WE5ecrxF-2ka9nO9NveYaJFjduUjAQTgUMu9Pe1gaT7v3EotatKqjVUxMcPlgnnwaDCDSrLELFtnTYBCEALqrw83MBEw3iy2-pi-bZLdlvmLZz0_3YRAO9JuVKyshue-0Ih0GPPYpz5hiNrypPspszzeut16C54rJVd6kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qXGWOsgTKJ0ZNHX8cmysHUsm73pG9p44wWq0t3xOBr0FzQEnv7peFv-PoLK_Py-p6J9GCiMHBrlDBgLHXptQ17Ff1lkT4N0d7BMwkb0PJcd6IcPxQLtbBsuwZQOzqTOiAnW1Yd4C4uvRFiYEYePwFjehe-nqDhfit60kZg7WegefekGDSuzHf0MhHgVJAWqStflQ4S0rjpoN8gjZIeVaXATdDa-Gok0JcemRKl902A3yD8Dh3zMW_HNavWu1rvJq5DMP3tUqtdXtFywJ2fczQEDSZ7RQ6BiPBrFdO9NxRoOm0oSRivDj0_CVGYjsnlvonHgKZc3suAGq1E7otCFHoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📱
کاپل‌های‌ فوتبالی که رکورددار بیشترین تعداد دنبال‌کننده دراینستاگرام هستند؛ امباپه در صدر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/persiana_Soccer/28870" target="_blank">📅 19:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28869">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QS_HxyVz3fSHjgWT27Jfd7xUiSDtAgnWllxsGEUeOO8yJf_t8crAnpsi5s-HOJ7UgSCifDIWJi4i2JqkCLQf7OzzIBIrSosVQr7PAFcnAsQhFQ9oO4ec-1weOvQMt-1Msa_EgtNFxP8QNlxxLlmVUlqq110rFajyuVsiDfdYWXB1_0dAgDMkEkiIUrM2SHXd5w1ZQEaOr0WyHOC2NW6zC60njLEDlEuF3O5vfUYNHgpb2seyw7sZkmQv4_sI2DoCeOcSuyjvO0mIRlcyToU1DZyTkFGgHkjhQiqClzV4uDnW9nksIMN_-qnzxmkutJ-5oLJEQMtfsfhnYhPR96khtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
دوتیم بارسلونا
🆚
رئال مادرید روز یکشنبه سوم آبان ماه ساعت 23:30 در ورزشگاه نیوکمپ اولین الکلاسیکو این فصل رو برگزار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/28869" target="_blank">📅 18:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28868">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHrKXNBa9K5o1cmTSerigXQ0xOuXOW083SaBMjTN1r7ISGVvQgIx_hleJlDXfhhVeTLA4AZK6XFcZuDMdKrJZaqJDwXhKxNWoStMwGGs_M0wvGb9WEp8JjXJH7DfmuJlZ6X1fsERqO0reQhMKZX5zRjKOgmpz81vq0Z4lnljGFqafnzAk9vuQHnPkhruxr24t3Luz7DIbtXBllpWRE443nwZCdSSem1FxJnvoE7oS_a_p4TtG_mt2FuXHJSNZ-i-5xMbzzaRJyMsbfqpmYNKVFVKIF0kVWVGdVktXm8NZOZvUQCQF9rNdkBy1252-7iHolesD52Q4s6yEvnYKflCeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇫🇷
#تقویم
؛ سال 2017 در چنین روزی؛
کیلیان‌ امباپه باعقدقراردادی قرضی همراه بابند خرید دائمی به PSG پیوست و با به ثمر رساندن 256 گل زده با اختلاف‌بعنوان‌بهترین گلزن تاریخ PSG تبدیل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/28868" target="_blank">📅 18:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28867">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADQjkDZyI9840VMJDkGygExKR6orhsb-8g3pUj2IFZ4DObLuxnhgwF6bgXxzw0cZq8LU4ZuOcIPPahN5YuedoOe_rG7DcAaSfHBsFD9qjFAcYCp2SSACoraMMd9iNj9529Ir9phqHFQCahL9-r0ihU672gSxrv9vkkOjLLzGUdQfrPq9Nt6JP25KSkdSKiiQ0tPFskioLyVyuVr9oKmjTyxJsYS8HAfqoJggpyIn29CvSzD18m2A7YDRqkmRLnKdp3Our9xn3WvljbaO65nLboeDt_iW42mkzod_WQwBmTQInHvE8PGVKJ7TaVkCl-Dvw6cdFlB2Jiazh_q7SQt5Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌برتر؛
شماتیک ترکیب تراکتور برای دیدار با شمس آذر؛ ساعت 19:15 از شبکه ورزش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/persiana_Soccer/28867" target="_blank">📅 18:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28866">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGKya4txi0ijFYfRoNwgWuaNzmvHdsSZyflt4K6a0WhzCiAPOYBfhu7hRAzw8uVRBd2tYwvXYg_mKBKVvbLpRbae3--ZFNDpASUo4lDou-exWRhdPbm0iGZ2SYWu3S3dbPYX1A4K5cJAd_fEnE8PSKnqrq_EfmF6OG3UXr-fwX5fxnwx8Ow5YgWSQc8zKYsaEHNN7_o0gYLBmyrgF6hiZqPiqLLfjnYhIdE4Lbyv8Nr8YqUZAGjaax48IuZwG-kXG8ZLwy_hYE8rrVMrDYbcXBG-5zjRv-x0XOxJ7Cx1fvoRZtJNBm3XNBKOYI5KiMTNuvixQKFmSFdhet-nlnl4Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انگار نه انگار فردابزرگترین‌بازی باشگاهی ایران قراره برگزار بشه. نه تو مدیا، نه کف خیابون نه بین مردم‌هیچ‌اثری‌ازدربی‌نیست. خیلی‌ها حتی نمیدونن فردا بازیه. مسابقه‌ای که از چند وقت قبل از سوت آغازش سوژه اجتماعی بود الان رنگ و بویی نداره. فوتبال، استقلال و…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/28866" target="_blank">📅 18:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28865">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cc-kxHlQe0gjdzT3OcT8sbdLgYMbZF2dC7vXk72RGefRYUsWkrCRkbFRUZk3V5JLdpQx7Pf_roCUK0d88PA0sIAhxPjxonRt3bV2i0HFEZl462nibNeoRU-FInAXCOgAQXGiY9D8FrZwUdxxeeub8r_mJCGpkRDW5CqQex-2pRLmIUfUe5jy0hx0p5H3-okcIZNArG4VoaMyW4V46CgWPqrGI8TnMQ_mghM0U-gxTwjyX9HsH7DerbXYcbzbSpCDRxTmiW7x3Jpe1zLGbK7vMXSKrgaUYMEXfkM3fesjxOHLm8gUrdtof38LNLc2J6c76-_LrC2MdmEA-1GkFvhX-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انگار نه انگار فردابزرگترین‌بازی باشگاهی ایران قراره برگزار بشه. نه تو مدیا، نه کف خیابون نه بین مردم‌هیچ‌اثری‌ازدربی‌نیست. خیلی‌ها حتی نمیدونن فردا بازیه. مسابقه‌ای که از چند وقت قبل از سوت آغازش سوژه اجتماعی بود الان رنگ و بویی نداره. فوتبال، استقلال و پرسپولیس به بی اهمیت ترین موضوع‌بین‌مردم‌تبدیل‌شده و این‌حجم از بی‌تفاوتی قابلیت ثبت در تاریخ برای نسل‌های بعدی رو داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/28865" target="_blank">📅 17:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28864">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57ae770053.mp4?token=FXAukTO4h9PNj_ezbqlkHcPKx7QiS08E0jgfiMGK8dQfTmNjfKZTHL8gOx9zJ8gV0BV0vHDjwpUwxzY5GI7yR__RPV3JmOLZTX8y2Hq1hnHMpYvE7KMqA_O1Rx91THTrLTJZ7TE0-qF6yEEnu8Fx0wmpgzFIEvXEWSoACfIqABqLiL7tgtiudPwPYHCJfGQ5-vyURDhbY0vpKMC_z2sOHnaKX7T40G3WaZuujWfNqS93RUbfB4DOy2Y_axwWAFTuYyD8hAgpBipyaYbXJpqTPnxOmw6Cff69fKMR9l8vumnMrGwG_brZkk7tgTRse4tvRQTgRGZI2-2KDSQ3sB-KnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57ae770053.mp4?token=FXAukTO4h9PNj_ezbqlkHcPKx7QiS08E0jgfiMGK8dQfTmNjfKZTHL8gOx9zJ8gV0BV0vHDjwpUwxzY5GI7yR__RPV3JmOLZTX8y2Hq1hnHMpYvE7KMqA_O1Rx91THTrLTJZ7TE0-qF6yEEnu8Fx0wmpgzFIEvXEWSoACfIqABqLiL7tgtiudPwPYHCJfGQ5-vyURDhbY0vpKMC_z2sOHnaKX7T40G3WaZuujWfNqS93RUbfB4DOy2Y_axwWAFTuYyD8hAgpBipyaYbXJpqTPnxOmw6Cff69fKMR9l8vumnMrGwG_brZkk7tgTRse4tvRQTgRGZI2-2KDSQ3sB-KnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گل بخودی های فصل جدید لیگ برتر تا پیش از شروع هفته پنجم؛ هر هفته گل بخودی داشتیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/28864" target="_blank">📅 17:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28863">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CjexJtDgDJ6TaugGAU--wtNBQkbvItg1EUr52fgw9QIAr8B4EbF5q0nVy5ljyGUdxxoXbfeS5KdhWqH_gz22hm_4XVwLKBxAJ8xbpPoy5JEeZ5BBlSjNZiRug9MHbgT80zlK4us-eoz641rxnck1QwuAOlWB7X3KLeP0O_-Miz6gYlqjevBG27-3Q2g7uwyWxq2TCRIfXOPOrFNV5oRnwkMULnmb8ND9ZsvNzrvP5HAcdUtN-pzRg7EjZDsEydXANiLdA2y7hKogoUZz83R3Xslse383M-9kennsOa0fyvlAqBjzWrlnm_2sFKcGgxE5KrBmv5iIXazPgtRLXOeiXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
بااعلام‌باشگاه‌بارسا؛گابریل‌ژسوس‌مهاجم 29 ساله برزیلی با قراردادی تا سال 2029 به این تیم پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/28863" target="_blank">📅 17:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28861">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XCWY8Xvedx-lX8gNFw7pow-Z44iXYBj_QajRGTrxGQWkG4mGd5qAG6y3qE_BTLgJyZE0hDglujkM-44RGO_UIYT3rJ8TB0OrKOZXn2vMKSHFR72yoCWWVNEi4lQ53UFH73CwPKLSJPdKOl1hMdN03YaUgD5Dp8VAIb_-EoR9p_lMyPmWZepcEDqWME5ozt0lyA_wA9nHrytZrD7Qh2Uo55BzE6rrJ1V8lWl09On46QcxgAWic7UE8EjUvW_UIcbHlNSeam4Iwbr5xSwNfWstIUPFZ3RJP5sGTPGlHWf50-jlZZe0nv04OxmaZ0d3D5RqMGYR_Lnbogqr6LMMr7IoZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZsU1GFwWvZ4UL4Hb3N2MTqxUKMynUWwh7bY6cN49oOPUvhMZ4GVEdA_kVfV3BAXy0PcokuvJEudeCt9-4kGYopDUHm6micIicSKvOyAs3xfBOyaPfcLqF5LlkhBVSmZgtcZ6sF6qV6dmFftyO5l2IKXhz2U8-0NtmdfgR37E3EkmKhZfXEQMbI_PcmTYpDYh1-7sS95m60YkUdmAqeoh04cOsP9LCm6R4dEujL5DeGte1t3OcSzj0TIGxfAIdlq5uyclIB49MzNNkM4fHkjiCkcAAFYOiue55MnHROm5FEYxqKRrBqAiGDYFcxzIPzeDeTDo-q0HPFU9Yz6fSA-iJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
خبرنگار رسمی باشگاه‌شباب‌الاهلی امارات هستند که از نگاه‌او سعید عزت‌اللهی بهترین بازیکن این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/28861" target="_blank">📅 16:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28860">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Suah6fjVqs7uLH_3WPn-nv6EZ2-3-_SsIJ3JyFmv_r534Lz9S9raqNyPliuakIsih0aoFSZkwkBu2itMvOveRbzBghC0ZGn-d_8s-vT1NOVFVDSx1SCnvjz7I7C1XV5VKJfXRWuQee3HutDAMawzqLi-ejKwfaVTSbXRF8uzqeyLDgXoc04NHTJimby4wvJVfMIkqiCBSVIquX4yJ-lTnPcYav3d_4bscN33DzIcfFGp9NCwrC51vLmAtGgz_H8LMplVmzLp67oaYVO71HLbbPAeN8OVmq395I11lUfwSgw71JDsDT3Q1r3NNETWKgMIdLyS0q6bhmbTzS8CYXzUVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ قرارداد ژسوس با بارسلونا قطعی و دو ساله توافق‌شده. سران‌بارسا10 میلیون یورو بابت این انتقال به باشگاه ارسنال پرداخت خواهد کرد. تا کنون بارسلونا 174 میلیون یورو پول رضایت نامه داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/28860" target="_blank">📅 16:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28859">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cShAPTJR2xcg0EGTx3o4NERnLursmXxmTyO4t8vKYn24wwgNNmWaXLKdOKRYgRJ9zmXDLR1CI9sJuCexgb9qmGK93enNQSkDqYwef_UEkVSvadOOy4LHeqUVUYAsOM9WHWVp1Lvj-tjzl0Z-uPgz-yvMqgOGdIvB_nOJLd9EA-Ogr8tnSC1lADZgzu0yYktGlI1WY69slbechWwt2TDcBKHlzRymdqydJ7j0XV6GSSrLIx-2G9dpDjPnDbPk2GIhJcCO-5-zYgcMsDelwxGAXIKcZpavb8fxURsDCe42J2lKGL-cfmDsq9ZNixVeztJgtKlv2U0IJR0vzuLsUmiQZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ لژیونرهای ایرانی حاضر در اروپا:
‼️
علی‌رضا جهانبخش: اکسلسیور هلند؛ الهیار صیاد منش و علی قلی‌زاده: لخ پوزنان لهستان؛ محمدجواد حسین‌نژاد: ریوه آوه پرتغال؛ میلاد محمدی: ویتبسک بلاروس: نادر محمدی: دسته دو فوتبال روسیه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/28859" target="_blank">📅 15:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28858">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUe9r5Nx9OkhdBPIa-Z_RINC1Rf0uVPHHSKV2EW2T_uJ67bObwaZf_riiNcORHV9gjYnpYD6CXn43SxE6F2t8ia0n6uJGe0oEo9i5bNqRi6xiinXwECIGaC5Al0UMfQQ2yABcwiJabZFiPZdmVQfcMx09CNWtVvMgYV_Lt5ZmOWlMfh2Gu70PYrTU4iuiFrO7RaI-AZiVhsVCfaSU3n8AXa2GcIiOL7UMORGLGrzO9f2vXD5-aObQ92DVC8Iuv2YQ9C3KcfB5GL5BmHO8o7RWsJsBaX7zXoTyW10XapKhfPrY0SVj0Ux54vAxaV0KrVrODylo7NfcYAhr-vPn2YRqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌رییکای‌کرواسی با انتشار این ویدیو خبر از عقد قرارداد با محمد محبی ستاره تیم ملی رو داد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/28858" target="_blank">📅 15:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28857">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgnXGnXoAZoQwYgfGtgs7p_kudFYvRtgGfd154HGWIJfRnK9W4dce5pfjz79RE4nrCoonl7SMWOk6XUzIfQ5Z2BSwlenhzCHX5LaaNm1dwv6wjBrs-w0dKcwwXEnPleNoeQ-pvMnW_YsyG6tbg2nCBR0M_HiKC3r3kIE_A6qJR-v6R9Qv7zDodxpO8ColjXhfrAfYaMnzSNPX_yI642vAbIchvJTi4LUzpaSgTHfz-F3tfKdrB5OTJIu_y3SvlZ6yHgKPBdKFl6QGQZJKcavJ5H6PbffqYt8EtdJVorXItYLlhT7oKragTiZ11UfRel4kjzCyjuDzi3GV1MfFZSnZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هوش مصنوعی دیگه داره کار رو به جاهای باریک میکشونه؛ یه چیزایی داره درست میکنه که با واقعیت مو نمیزنه لامصب. اینو ببینید‌!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/28857" target="_blank">📅 15:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28856">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqRJcT8GqTZew6Wp2CiaEb0iV1FBvINymOI4s0RfzgtXkL82forWNBXz5_c2Q5X8qMmiOAbSxcpeYn7-vXzV5huj07tFjyaExI5T5cXp-HdxACagZcUBCWvicvMtYGC6iTS8GScDM8LdcTwY-Q_tFqc-xZAWkixA7WDg8fj5IG40PlCFiZ7SgfwgJck9xBB1u961at2i58B9-9NZgLmSGieD7zslupo0tmD2TXQHU7rHfEe7zGqLVlbBHDeUmST4Vb3oif12Hrfs66ERO2SBgJavfb_JCwjbWRZajLW0Yh9XfELTBwoxIYd9I8BIV4rsUuj44KIxJgjQjcujltX5tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته پنجم لیگ برتر ایران
🟣
شمس آذر
🆚
تراکتور
🔴
⏰
ساعت ۱۹:۱۵
🔴
انواع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ شرط رایگان بر روی اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/28856" target="_blank">📅 15:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28855">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d453f3d9b.mp4?token=o0B3wGuJmN-dcbcPsuUS1U40LVMuWYCHqOBCybqKfSFn6yWUNRwyZznWK-kwufSQ5u7FPTRsugofLJyhm3fYCXAxeh2-GW8sPR4Qyfph4doUmO5AX7LKFQUk7iTPRoDEMhDAe2IZ5FcEg2CcC16MizwJZ-mLTWyGhMZcGFeLWz4BaJomfql5dE-HU52jYNhkqpmFy94zObMkES1R8cKAk4Mi3RfJyVHhuvKdwf-_BSIjOk5CYQu7pJZzNqEarweMIJxRqgjlYeePNoKuVVJ13Z6ZldC_NSKdjEA992NjRc7CfEqstxV99Bd-3GAUw4Oz7sSGjxN4gOQLZS7OQ_pVVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d453f3d9b.mp4?token=o0B3wGuJmN-dcbcPsuUS1U40LVMuWYCHqOBCybqKfSFn6yWUNRwyZznWK-kwufSQ5u7FPTRsugofLJyhm3fYCXAxeh2-GW8sPR4Qyfph4doUmO5AX7LKFQUk7iTPRoDEMhDAe2IZ5FcEg2CcC16MizwJZ-mLTWyGhMZcGFeLWz4BaJomfql5dE-HU52jYNhkqpmFy94zObMkES1R8cKAk4Mi3RfJyVHhuvKdwf-_BSIjOk5CYQu7pJZzNqEarweMIJxRqgjlYeePNoKuVVJ13Z6ZldC_NSKdjEA992NjRc7CfEqstxV99Bd-3GAUw4Oz7sSGjxN4gOQLZS7OQ_pVVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
باشگاه رییکای کرواسی بزودی از محمد محبی خرید جدید خود رونمایی میکنه. قرارداد دو ساله و رقم بند فسخ یک میلیون دلار توافق شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/28855" target="_blank">📅 14:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28854">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RbM5RvReRumIRbolKdAwt6_3JuC5YJDX_KuPh2xa2YT9yzti0-XzOVFJkiiCtLKkHpjhWqROrui-TgUCWjmjLAsX8UkZAqcBvUTkXXpoMO6LLrlGlEmpmURHB-lhNxsnKYrUzkst4DgccAEK0ps1YCUYBrR1kJ-1hB0Pgt0sBMMBOpvDGkw9OqDkVrSo3X-1NCfHOtjlzHBG7D4Qm8pkNCUQYbhG6EvNP2Er1TkjRsjjfV6zgyOymY1fbG8WRodEGtjvvNwv6NE2O8bw-fEmxg38SUXiGtFDj-foUvkpdgGoJ226A818xAUC0SmVTJOKqkMfdN34SppdM0JtC1igbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
خبرنگار رسمی باشگاه‌گالاتاسرای ترکیه هستند که معتقده این تیم امسال قهرمان سوپرلیگ ترکیه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/28854" target="_blank">📅 14:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28853">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔵
🔴
درفاصله کمتر از 48 ساعت تا دیدار فرداشب استقلال
🆚
پرسپولیس؛نگاهی بیندازیم به زود هنگام ترین گل های تاریخ این تقابل بزرگ فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/28853" target="_blank">📅 14:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28851">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Et6Zkbem1VhsdbHLEzWOzlCMpGOKTgxiRJ2xsNw9AaKLSJsVOydpSMEiKuXz37H5JtdKJnxR7XMQBocodZKMuFthVa30K-k0S4I1N4YqT8ecrDxwh_hXY1tukKnDEtUue2KEOkNXuGqGzTIkWJ06fevM2-zeFEguG-6f3CIEB4X6309Jx4e7tLpVht9N0NNtPBl3VItyMFTrnbrVsrqnZd20Vv7SzkHTnbHAjpMccBu2N32UnVGxTZXsa8bXJTdjEOpAimgyD9d3tT6o4V2SeUR7NAeNsae9asPdG3iUFwa_B_NRNfncf90LKbUESBcXvZDzQwhBIsTCdwZfHtOV_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B16do5TEAKQTOwdX_LgctMu8G_oPLc6mydLjUuwxn91z6iOWuhQqHKA2KhgLO1CEMljwaQaV86oKnzlYiZ4b_ljVKStsmU6e5twIyNAWoXTdvLP0ls28iu4p-PztayserQ_7TvbpgMzbJ27-upGDg1ZbRdBeTc2RH6jhv-oDjtbIHvSauHqNU2i26-3ba0MCKOk49ac7Z5goZSHIup3yKZEzxzNGAaPAfG01KVmeGsl96wj2BdzjJz4Ky39YYCxiCWLVqQbFv6YDJi9VZaMzt7uLe2PmNorU2Rn1LdvbQsM-AO4c5IyzevYiA2_7VaYENqNCrlbJSYH_xx1Yse2Cig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باتوجه به‌ سوالات‌زیادی‌که پرسیدین؛ بعداز پیگیری‌های دقیق از مدیربرنامه یاسر آسانی بااطمینان‌ کامل اعلام میکنیم که‌فسخ‌ قرارداد یاسر آسانی درسامانه فیفا ثبت نشده و تنها یک نوتیس برای باشگاه‌استقلال فرستاده بود و هیچ‌مشکلی برای همراهی…</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/28851" target="_blank">📅 13:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28849">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bxjRZs-U0-YKEmH0W-d_JHmsbl59j2faGKi8AhwE72A6vrt2m1pFb4VGXfgbFNhCOoA6EMdc343vXhyV1N406ee_NVw_4LPznq8sTxftBNocEOch-_vtL7upkcPSUhAc3IawzKSqzXnNn2Gza9UHQAb1IsRlC7o9afRHOwDwdDk3e0pPuODMcllSxT8UTRqoxCQDVXUC-nkQA8OQmTHYah5c6tVBoFg05OagPEYyEUjR_0X6Ou0JsJsyffWzQciMBpFepjFpAqIDzmCmfWfs1PkqHBXpKmr9IFUfNsUgSJQizaw52MD5vkBthWxZUFnG-XguoABJ6E22wwLgdFMyOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cF8kko-gLUY7g8-rWSDgLvS4MqybXYkXee5YaJoJx1pLwFhR_ZUsFU2ICzjXQhrxtFs0-vPICpxtEj3nmTSQVy5oKDG1ikw0OBn-V7GPySb9RmobIW7R3QXS3GpqaP6yEdm1qvOU7ybsnd_IJYWUrfACUVPjFQbuXhW0Yk-QjPLTIk7KusRSvDM6ECl0_33NkkYlrFi0xjty9USTaTdCFYwYCFdtltc7lwBiADiJrYm4BTdV9nwbzsLcw9tT2itxZIpFajPRvoeHoz_GWMvzC4kMuNFNShauBg2fDUwIlCFWyeYv4HsZZC5HGofrwkz1kKuTiOJxxl_hDLMF1fQY_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
پوستر فدراسیون فوتبال آفریقای جنوبی برای پیتسو موسیمانه سرمربی‌جدید تیم‌ملی این کشور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/28849" target="_blank">📅 13:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28848">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYDRTBKXKsSZxy_YTTpSUy6b28GaNodnETOO6swwtnJqT1_B2aOGcb51jslQQ18aSZOD5Ry4E1ID8lpjpixyltRpSKBKu7fTCvtiGfUzdlBK1PNOBOdkUorKY3OVOiwYZ1mRMANfWvJSYSrxDCV5TjtDKCHqZCakfPlwE0wcjLCnPURgy76A8EdSSmu0YEDLpLx1rcI-4sYA5TRacAjyLRce2FGNwKlUCrP8KiPj1-XgToTBmVwOeagbXhACWHqbXTsBSfDo3yT3GyfwKO5rrOO9K4Nt99uqGymjWGsbM3XqMopg9IddOvcWdqgWRMKmNFl6UFHQIWQh1tB08pvx2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
فابریزیو رومانو: انتظار میره تا فرداشب که پنجره نقل‌وانتقالات‌تابستونی بسته میشه انتقال انزو فرناندز ستاره چلسی به منچستر سیتی نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/28848" target="_blank">📅 13:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28847">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oj-c0eG-n-ZFuOCiJ1WQowOA3U7-kD8dmP9GmVN6u7HjidTFK7gvbDMqY-RVDnhLfuDicgVDveIpn-Ei_d7s0DIbqJ9fy-LdWjZ_kWP1ov6HGN7QopSbY0tMEu9YND7rSxMdL7dnkku9_DvOHrvw2Dx9wwLNlHkOtgQDlrT4WjgEpExPqoxOVsp5Ge8pCYKQGCUTOB01nVlTGiZ3doM1-jh74LSrdu5tCsavWT5fTQCo4Ujj5cyRFjVdq7wq0X_3FIi3dfry2h8p4MhCRaiw8WH8Ch0Sf1SkXV0GNo6hmUV8hatSced0uthvgw0T57eqF5KP87FAELMFY9O1aArWjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مورد جذاب گابریل آرتتا پسر میکل آرتتا اینه که چشماش دو رنگیه؛یکی‌ تیره‌‌تر شبیه‌ پدر، یکی روشن و شیشه‌ای شبیه مادر که توجهات بسیار زیادی رو به خود جلب‌کرده. جالبه‌بدونید در دنیا تنها چهارصد نفر چشاشون‌دو رنگیه‌که پسر آرتتا یکی‌ازاین 400 نفره.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/28847" target="_blank">📅 12:43 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28846">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eEntTZ-1Drb6yVAmO3O5gnaug4968cKFjZlXxtQqw7-50881wSunOMuFVAOiHuFm2r_uW8s235fPpOhPMbrVsAeeE0clivEyqNFC0RH8yIKbDbi11OqphdkCTB--PBh0j7uIoXe9kQrUTmP1NSsxAZreuUpzkw9M41e6plakLTwYN6TB5N-f2Kph04gBIorhoWx_UWq5MU5CAThmIwXX3W4rreKKDqBzpvWhP9ddgUhO6R4ASZnf9c3ErRb3oZ5B46s0E0PDZY3mA2KGus8m8JUoz4TxczkxigXeliqr1UIdaySXYYnYJJQrKiUNdHYXcxvo_ZQE0QNFz9X4ERkE5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
نشریه‌مارکا:خوزه‌مورینیو ازوضعیت ادواردو کاماوینگا هافبک‌فرانسوی رئال‌مادرید راضی نیست و به فلورنتینو پرز گفته او رو بفروشد. پرز برای فروش‌ کاماوینگا رقمی‌بین 60 الی 80 میلیون‌یورو میخواد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/28846" target="_blank">📅 12:11 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28845">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">▶️
ویدیوکامل ویژه برنامه شب گذشته عادل درباره اتفاقات اخیر چهار هفته ابتدایی لیگ برترو افشاگری‌ های عادل علیه فدراسیون فوتبالِ مهدی تاج.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/28845" target="_blank">📅 11:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28844">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZpM5Z8HS-_U3D1LW6X6hOuUH5e4yIDbcogNzPIDeAfAYRR5gkicW7uH0aYKWS6fCphOxHbw_A-Tgu1uKz2nBGuqdo0_ybjdtPyNOELgI3SmFMAtrOy0LqBpe4Q_Neo1Y8Z758e3dyAym5lFsfAzMMf-wTIIj7Syv3PleCNwHk2vOoXPlexEwbP6Kk4CvjNuXxUqijmukEfQo956Hlzp-m4XujnWmYUxUdqz61PtBlpfhPiftHF1NKeFbMtlZoBnN-K2-Q3-a7UVzBLBnLCLozUKwB6W_2qHQpSVc7X2A9ehCQ6Y0cO1j9uhIYXqeAcHY3GnjSxL7kCCbuJ7ZmaKAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
دستیارسابق‌انریکه سرمربی تیم کره جنوبی شد
؛ روبرتو مورنو سرمربی۴۹ساله‌اسپانیایی‌ودستیار سابق لوئیس انریکه، به عنوان سرمربی تیم ملی فوتبال کره جنوبی منصوب شد تاجایگزین هونگ میونگ بو شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/28844" target="_blank">📅 11:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28843">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeXSB8kks4L_3rKvM4XQ8Jn7MFeGL6P8Haicw7ySSXqbP-VolS7mcsi8O3w_P0zYGRcbNPNALcJ0k8xAxw92kIPs7-nAPJOUXVed0m4GF0ukRzHF-gJI0JYR3HTVuiF3fuUAzjMhV3NUyMcWQxmICSgwqnfaiqldaZHU6--TrR3HOPdMJfub227j4fsKTortb9ntGpfuPsRNKAgx66bXRmiCRXKlzCHN_07-AjTpCjseetIACm6JyBpRcno-4N38ITGZJG8E7TvuD3i1cFNbGhEX_FQD-IrUiDjpoFTuL4doE14BJbhUnPd2oHu-JMjvIf2pVHswbStnqymYELI9Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئیس‌کمیته‌انضباطی فدراسیون فوتبال: بعد از برسی‌های کامل مشخص‌شدکه قرارداد یاسر آسانی با استقلال قانونی‌است و او مشکلی‌برای‌همراهی آبی‌ها نخواهد داشت. بدین ترتیب پرونده شکایت باشگاه‌ها ازاین بازیکن بسته شد؛ خبر ریپلای شده هم بخونید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/28843" target="_blank">📅 11:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28842">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4afbdcb0fd.mp4?token=TFPFfbxiSoWdkPkdjCwv09KINlMWwQhcDqOZHJxwxWLTohQlc2AAS5rDQY53NpngP91YtJQ5kpWd46e-A2CGkQPZQssMMg9_F6LuF7r9JmK0OQFup9wECN-N29t1rwKoVJbvSm4cnAb9EyqkwdLVAgpvBB3gKtlf9fdrGyREXv_7aRhxNOSUHR58Y0pvnIOdyiTC8z2Tcdswa1zRC018IT5VmGy9DR96rtjcX5Nz95z4sVnF4tKpUuBGuS7MRUoQ1SkTsaTJ2otnPE_V6eCtUeblho2wOfof1UlPGLOKNZswpuN2jmgkFUsig139VS8Adf9yOEHnT4-gHURasqbeTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4afbdcb0fd.mp4?token=TFPFfbxiSoWdkPkdjCwv09KINlMWwQhcDqOZHJxwxWLTohQlc2AAS5rDQY53NpngP91YtJQ5kpWd46e-A2CGkQPZQssMMg9_F6LuF7r9JmK0OQFup9wECN-N29t1rwKoVJbvSm4cnAb9EyqkwdLVAgpvBB3gKtlf9fdrGyREXv_7aRhxNOSUHR58Y0pvnIOdyiTC8z2Tcdswa1zRC018IT5VmGy9DR96rtjcX5Nz95z4sVnF4tKpUuBGuS7MRUoQ1SkTsaTJ2otnPE_V6eCtUeblho2wOfof1UlPGLOKNZswpuN2jmgkFUsig139VS8Adf9yOEHnT4-gHURasqbeTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
صحبت‌های جالب کریس رونالدو فوق ستاره پرتغالی باشگاه النصر درباره سختی‌هایی که کشیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/28842" target="_blank">📅 11:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28841">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYb_8v3cGHwgfUVpNaGkTnSQAzjYIhTfceIQs7XpQ6zVZP7yWVGmqqzFowIXkjdUb8pdOsim6Ho-fwhjmkD4RDpxSBPiD9GNN7q84VY-vV08uI3cGRPNYjCZeBvsN4ZJBnhwp7QEVYgoJbhpAAL9dnR59cvfUiSqMkcSwV3EYJcS9nAofy6jPynEJUoCnvu4HjvR30aoHfRhCCHk8vXqmiG9pDTPMzzjd7tKkcDoYECYSZMkL2wJhncdXtThWfOt_nvmeJTIVvHrrmhauTgruTNOHUOneJGzwgt2tkldJbjP5iOzrZtxTF3w3S1wuRVbTsl5RX-bN6l4Np3DlPk77g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب جدید بارسا درفصل‌جدید بعد از پیوستن گابریل ژسوس ستاره سابق آرسنالی‌ها به این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/28841" target="_blank">📅 11:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28840">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXEvf-aZ19lOdw4Rld6n1qTbZMjFR5q8dsv7VKjTICAqJ3pnNJbONFIobYWuusL4CBQqL0jA8nnvHrVejY39f1SbId5J2AP_006nCMeQ8CdFJme0pRTaZqGso42gjSQ-v-zDzE1_hkBcZG0q_uQC1faTjud-lLP7w2REMl8R1Y0r0r2uoNz4WKxp_xR-mwhTg3zmrdiXPH9t9k5JvZwKWbJl3ILIvLBhx8ik8JQc9sHAM6cd4rE2JCzQx1h5D6IMr2AJnl8dz5YGyvVm_M3SvZGtWE3SX4ccD6dPeaubKlZof4h1co0rEQtgoUo1ADLiwv4r5rsyHRDHAOWkeV6fvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/28840" target="_blank">📅 11:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28839">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQN-s0nHrTFvrnNk_C00l_ftfe3YGoxNn8NChCKjX-TmMaafUW0yTxqZQcBxDPBAvDuZWTyQYI9Ablo4NHX7g5iKgS6votXu_GEF_IYzFh52S6MQ8s15VlnRWCWt61vdHGUBtd_0l7m5_0SxjPGlL_tq7tIPFrOMO4cso1qdhZ8KqcUb37AkK6WOHpwjCbI4rpkGKyV4GzvfG7M1zwkroeKbmxz1bAug89BbfhkubyOidbJRB_F-8egMkvHANzjInat0FIVFDAcasMLRiAY9i3a4igy_AxWQs90_pSRlNTnSmqf2uUDl0iAeUR-zF4MJgZJcMOTJCs_7QwHGBHov2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
تکلیف نهایی داکنز نازون دیگر بازیکن خارجی استقلال نیز ظرف72ساعت‌آینده مشخص خواهد شد. یا به جمع آبی‌ها برمیگرده یااونم‌توافقی فسخ میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/28839" target="_blank">📅 10:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28838">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LudwxTjVbOZWjMI4DnNKUCdP5Gifk02athY5HWJYwysTWl86rwaddJdqLkrYCmEr83Q0CXKfGJH3RQ2ak1a-dbTr7x3SFEkG4KHOk5gCddMnawbNHkXS-jsLLtcaqjp_TTEVcxKaCTeCa04Ildq_cO8pJClcpKwJCNn2byhKdCLNBq_h8eHGZLyaahXVGMVAbgJLIY3TUjll2oWsSdSgN4JDkVrfAiCs-bMZYueXl22xpRs2x6vKasSI5lBUxs56PQavVSoNHIBi_ZajsL7WSvein2A_qu8VAgNQyQ4PaKwc7Lfqlt6kUqdglqZy8FpCoaXm0QQHx6lpXPXV7hHLfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو خرید برگ ریزون و فوق العاده الهلال ظرف 48 ساعت‌گذشته؛ گابریل مارتینلی و اولی واتکینز دو ستاره آرسنال و آستون ویلا به الهلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/28838" target="_blank">📅 10:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28837">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klJj78ndq_dLWwchWDKkSwt89uNqWxpe0fnckwyLx0Kj-J27MH_T9zlNW0jxjaBpWJAThn05LNIXwkP17zVMNXPeqFVhq7aSL03TYmjZWMvK3RYHbXSnVMmWPh-s7RpPUSfUJYuVickLYxK_OSJxHqcL0mPLfGFyYJ2Det2_MvtTwfaH6XcmY3yU2E8NqD6_YsLrpjJErEDrZRoB__lZZGa1SxdGOpZ_Jk6GfC_5LvkxVjYaWONHBdYNHuLRQZrjg5BpML73jXNlZ1frNpXPF7i-9LrZusnRWgbjrmWGmpZ3Ce3tuQm5jqlfWcpRYJ4V_dsrxypSs0RVZwGy2jXi0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
فاطیمه یوسفی فوق‌ستاره 21 ساله فوتبال بانوان ایران هستن که با عقد قراردادی به ملوان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/28837" target="_blank">📅 10:11 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28836">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUfBP-2yN4nJ57jxcNqWBLv81BuIfCNUhSK1UuUeXZGtv-Pzk0ZvVUwn-i6ob3zm0eoomYd6EgJJpSN3KGHi6PDSKsSrA1PEdxeGU1nA-0ZqNSBPEzF8Z_tYE3FrRDaue0jhyBK5N-ed9bDO2YThyQ0Jnf_CEa7NYz5SCTAbSMdgreYDOGLuj1RwoPAxC-yVDnKXhks_KUEzjzeZQ-FtTI9mVXcPji9cmkwC1Pqvopg8RkmVziDhisw7PycLUEdy77HyDIW12jWJSuJ2Quv6NCLxiCpFNfzFWJC5YkSI6mHEa_tKy_mji1Sv1wOLTxHza3v6Ga_Aj6_2HjrhZBnLow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
امشب‌ساعت02:30 پنجره‌نقل‌وانتقالات تابستونی تموم لیگ‌های‌اروپایی بسته خواهد شد و از این به بعد باشگاه ها میتونن تنها بازیکنان آزاد رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/28836" target="_blank">📅 10:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28835">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ddec47474.mp4?token=LV5oz0VWWEvD5CSG6oLO3N5tK1W4i5FujN-4CbHqdkvlAwZeQ5JH-svd992EbFsRVBC0sCYCmqxRoTjBb37xZqVFSQhEGmZEF6nCBIF7ubCKtLVre_eo9xEWpQEK5nB6gqKqm5wID11NdgXVVHPCaS9Gv0CNtR88vh2VWX8bwh8-oHCg82Frl14S5Cderf9usVstjfiaS-guEbZm0GUEccsVZmYmavtoP8alZ4Yyr1aHEd2fahNRMvzfIkqZSKC1rHGT801hdU3HY0EPoqGM2ZBUBb2h6CAjc3pCxKcxVBtOyKzDNJN4iClCvXuCpiIa2SsK84gXakNbjCOiiGMBwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ddec47474.mp4?token=LV5oz0VWWEvD5CSG6oLO3N5tK1W4i5FujN-4CbHqdkvlAwZeQ5JH-svd992EbFsRVBC0sCYCmqxRoTjBb37xZqVFSQhEGmZEF6nCBIF7ubCKtLVre_eo9xEWpQEK5nB6gqKqm5wID11NdgXVVHPCaS9Gv0CNtR88vh2VWX8bwh8-oHCg82Frl14S5Cderf9usVstjfiaS-guEbZm0GUEccsVZmYmavtoP8alZ4Yyr1aHEd2fahNRMvzfIkqZSKC1rHGT801hdU3HY0EPoqGM2ZBUBb2h6CAjc3pCxKcxVBtOyKzDNJN4iClCvXuCpiIa2SsK84gXakNbjCOiiGMBwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
ویدیویی زببا به مناسبت خداحافظی لیونل مسی فوق‌ستاره39ساله آرژانتین از مسابقات ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/28835" target="_blank">📅 01:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28833">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcJz2Tgw7Bmzk8glrivRv_B2iLmZEiozTBeTnD5NTc61X7qGE01iEKzISsequ_U4sdxzhWbk_tUBfU9kUgwhDC8gHA7XeJyAO63p7Ym_n-mbxyp3MVH5WKUkkqzlQD-kFCIyQlqjSblc7ZeFNVqL6E9a_IY1hgnTC2kR_SwOKH2dN7NS1d5LNvV1oHVsglafLhTOSDrB7JV1d3Yx5P9mW3eOuXPIn5z9fdyIxpQzvRi7ddQktx6fOBWzYqeBsRwMeJXwR-BdzUFUmbn1Nve4CoKiS_F2yKwBm41ll0ccW9ecHav4_-SSsY-amooSVCfjfFPljLYCe6f-61Pt19UQiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛شروع‌هفته‌پنجم‌لیگ برتر با جدال یاران نکونام باشمس‌آذر برای حفظ صدرنشینی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/28833" target="_blank">📅 01:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28832">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_s1A9yxL0xl8nDzU__r7GfyrwRs0OzsBD3faDZjw1WfxDeMQCl6qUErL6r3CiVt6Q261qSbenvfSdMn8ci4ONpYfgYLobLD6Snul6PwXYFnXyqVz9Kt9oiCaVmNqJt0u88M83ivCe0IepDlpOODurOwa9aezayDCQaAkRgJcsMFwuhu-Ii8QCmUnG02V0mCEMe2biKP8YC2_hAcD89Ne25vPs8vUpNYUZWSyduoX-Xwkr9RxrwlZRbul7miqHIbqvfZrHR5GjHfTYJpzAmSoEJWoWnkEldaTF87ufwa22JsVEX9oovAY64-hMPYgRGp7bPMiK2dqnHrJ8lFMMKcew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدار های‌‌‌ دیروز؛
برد اقتصادی آرسنال و جشنواره‌گل بلوگرانا بانمایش‌بی‌نظیر رافینیا و یامال
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/28832" target="_blank">📅 01:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28831">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd806e1b22.mp4?token=ne9hQ_5hk_Ve3P6_u9YuTaYxST8W7EEAMg24r4ENY9a7IR04R8Sq2og57CNtF49UDyGS4b3f0GIzk3cnI5oIDdw0HXPzcAl7sdZV230XvC-Joi9Xje5yFNmVR3wke0xYhzMpuzX4UwYNKv41Tt8OhQi6rY-Dh2GE889tv78BYSo3VA-69C5qn5Y6S7Px0Lzi2zR_50Fh7o6qt7lyUbhBiYLB4Edljh-MbWrimJfq9_benADeZcFYdHQmSERCXqOVshSkgmabm4tjjiGf43VYd2cCiaQpj8o5Pb07pcHYyTyPfs6WllHNcHIBXflyJ-KgYnRZxNKNPxspebUU0OT6eoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd806e1b22.mp4?token=ne9hQ_5hk_Ve3P6_u9YuTaYxST8W7EEAMg24r4ENY9a7IR04R8Sq2og57CNtF49UDyGS4b3f0GIzk3cnI5oIDdw0HXPzcAl7sdZV230XvC-Joi9Xje5yFNmVR3wke0xYhzMpuzX4UwYNKv41Tt8OhQi6rY-Dh2GE889tv78BYSo3VA-69C5qn5Y6S7Px0Lzi2zR_50Fh7o6qt7lyUbhBiYLB4Edljh-MbWrimJfq9_benADeZcFYdHQmSERCXqOVshSkgmabm4tjjiGf43VYd2cCiaQpj8o5Pb07pcHYyTyPfs6WllHNcHIBXflyJ-KgYnRZxNKNPxspebUU0OT6eoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته سوم لالیگا|شروع طوفانی بارسا هانسی فلیک در فصل جدید با زدن 12 گل در 3 مسابقه؛ پیروزی پرگل آبی‌اناری‌ها با درخشش یامال.
🔵
بارسلونا
5️⃣
-
2️⃣
رایووایکانو
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/28831" target="_blank">📅 01:28 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28830">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jib6kRr6GDZShsHdd_8keR7XITVQKsT_WCNbBXuKFUecfoMQpsOb1nyZ_JpsiGZiSLI3cDlKq_1eFKb7cNneBaBjFgmXgrQEvBErdFG0WH7i31Ajwj9cM4Y1caX4v-C1_hmvFsiiqLI0mRTyRV5mEGKd1twjd3GCcfUpei8cdfMDKHxG8w-kPSx4fwO-yTmGhLVG4rRODQHAhhifZ8m28-KkwruEi17YUFYVRTuLOPQfQ8amhw7e6ynj4aCzgvRq_k-6VFR8yXNfcizBwxnTAFBuW75YtdW_DfPN5yuWd9PjGAsEGGIsIWtdtrwlAokg5fGhKrzho5gKXn6gEz8Vsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته سوم لالیگا|شروع طوفانی بارسا هانسی فلیک در فصل جدید با زدن 12 گل در 3 مسابقه؛ پیروزی پرگل آبی‌اناری‌ها با درخشش یامال.
🔵
بارسلونا
5️⃣
-
2️⃣
رایووایکانو
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/28830" target="_blank">📅 01:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28829">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3AaF3QcOIWgoJKlO2TpiBUlHrxQ22sU7DgCFh-ujy2-W6aeJMkZMe-A8FPk1DS9DZN4Z3dhj1MRrnliAkcJsFRcUKxOCFSr_9nOHNW-t-rVyfsvJpjiPlnh4md8moaQ2i0dNDYzH15fn3J8E1JHiRZmxQqdPl6jwQmc2O8FxqQQej1D3DSRYdQSfi1UV1iVdN9X3-oT91n7PwUL7DxUigUhz6cYP0XzH4Taw97FSUGZ-DYu2fHGzSbcU5JyAU6GAEZsveOmrKLLy0XgiQzUMOm1cmmMfgo9pH6Qxaafj4Ulg2rDPJTt4d3tWGuwz6iOYzbVaJOgPJfe3C_xSKep8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لالیگا|شماتیک‌ترکیب‌ بارسا برای دیدار امشب مقابل رایووایکانو؛ ساعت 23:00 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/28829" target="_blank">📅 01:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28828">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f678a57f6f.mp4?token=g3AM8GOx5PwOs-8qPHj-ewYmQF07El_nZRkseIXRPNuaHRz2cWe7pZ2OSJTgU1G8V5UssCFZzUTSR7PXiSlZ7nKqJ-5-SOXur_dT947RL2meIk1kuA0wh4S4ueQHvzgp588-4hIHDIyVl7jZ4O5KKr0SFJ-I5cXc3ETnKN21iSgaBJcPrvXwEyEOlnMm7f6AqRFzlRtdqZrsYP3fBkioedwxmp0cmpCzE0T4Xot7g7WWV9C52gCTlr2qBsShBaQoAwbvfiq0oogmIOPWd1oLLj_tBEIj7Apvmf6PF0iFIOlsxid0q2yANnpUKHZwRvYzclqx2s5pshBsA2ciRnopqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f678a57f6f.mp4?token=g3AM8GOx5PwOs-8qPHj-ewYmQF07El_nZRkseIXRPNuaHRz2cWe7pZ2OSJTgU1G8V5UssCFZzUTSR7PXiSlZ7nKqJ-5-SOXur_dT947RL2meIk1kuA0wh4S4ueQHvzgp588-4hIHDIyVl7jZ4O5KKr0SFJ-I5cXc3ETnKN21iSgaBJcPrvXwEyEOlnMm7f6AqRFzlRtdqZrsYP3fBkioedwxmp0cmpCzE0T4Xot7g7WWV9C52gCTlr2qBsShBaQoAwbvfiq0oogmIOPWd1oLLj_tBEIj7Apvmf6PF0iFIOlsxid0q2yANnpUKHZwRvYzclqx2s5pshBsA2ciRnopqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
باشگاه سپاهان از باشگاه‌استقلال و هواداران این تیم‌بابت‌حرکت‌زشت و زننده عارف حاجی عیدی عذر خواهی کرد؛ این باشگاه همچنیین موافقت خود را با قهرمانی باشگاه استقلال در فصل گذشته رقابت های لیگ به فدراسیون فوتبال و سازمان لیگ اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/28828" target="_blank">📅 01:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28825">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFpGLog-T938Klzm8OXXEVDMdaRz8vA469MI23T3B6B_KVIA6uL79pp6L8U4WVfZgBc1HZyxFXdyfihhhRdLzB6RedE6TRk19NWPjIkYLg8Kgt70uBxu3-ez5KFJ2Ug_slLt5zkzFMExrvCBTiMOwH224iritsYp-H6e397hPazR6zVIT7K6WWeAfNt5GxDqeqloQk0fQ2uI1xZFZyaj-jMSo0k3phAFR4WIxQf4r5t-WRkneMBUJRtT7z5TnXJHNeUGTWK5WNW6L0ojSxT_v140v71fKBVuBpJSkwn63zWL-kW9lsX-8XZzVZEDLHYApFqe8jwpfUPCLrRrQKTu_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به مناسبت رسیدن شهرآورد پایتخت؛ مقایسه ارزشمند ترین بازیکن دو تیم استقلال
🆚
پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/28825" target="_blank">📅 00:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28824">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c6848cef.mp4?token=cUdwX-FrD7mi_EPgPDksyJrGuUhS05hx24-hjQgl8yHzAemzKWIjo_UUf12ryWUvw0Pcz360g8wEv2nm2nx54r7NOwAzfGRwACFNQpq-yCmppMjRvKdtiD7-f-u3aY13CU-vKgrdxyROkcmlgRgczHw7mkzYNum_oZ8urIQfyxoQ4-lGtmZzYS7AEomXOSEXcqVV54VpXWZubqrzDUlk8qGndfrhOVijIrWqBMzwpihFIaVdokezn66UgPYjJmTxdgttEi9GZFxuIcjb06HICcO9SlrNkC95zQ5obvyd8DzNNaX0Vvj-J9lbJCYqirt_dxItb8BYe3QTC_hzO2f1nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c6848cef.mp4?token=cUdwX-FrD7mi_EPgPDksyJrGuUhS05hx24-hjQgl8yHzAemzKWIjo_UUf12ryWUvw0Pcz360g8wEv2nm2nx54r7NOwAzfGRwACFNQpq-yCmppMjRvKdtiD7-f-u3aY13CU-vKgrdxyROkcmlgRgczHw7mkzYNum_oZ8urIQfyxoQ4-lGtmZzYS7AEomXOSEXcqVV54VpXWZubqrzDUlk8qGndfrhOVijIrWqBMzwpihFIaVdokezn66UgPYjJmTxdgttEi9GZFxuIcjb06HICcO9SlrNkC95zQ5obvyd8DzNNaX0Vvj-J9lbJCYqirt_dxItb8BYe3QTC_hzO2f1nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
ویدیویی زببا به مناسبت خداحافظی لیونل مسی فوق‌ستاره39ساله آرژانتین از مسابقات ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/28824" target="_blank">📅 00:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28823">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWLFJakt-SW1oux1dtT2Brdd1GaJSekGePaHHqkJwY2XuYHs22mRXbkYdmBSqCkdjn-ryOjeiT0-BE4KbAaLGDAysSbzsk4ZKsFAWWf2g0WdWNuPBZiok4-T3TMW87lAWls1VVdCfe1T9bzw_mXhKrywWaPExwYNTGqfWFu7FE14XXIlkuxwgSj15JqcYXNTRyT_shjMLeCkmK6FA5EaLwLApi64MhfZcsbiwadyzkcs2SQHwteIfLky0RkSVM9cDFFaGle54nn4_aUkSWG3klkidldMfoECJbyG8AjyaVzqEpxzk-TLYDC9Pd-PEYJ8WNClzahvao1tELuRNHRxaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
به‌مناسبت‌رسیدن شهرآورد 107 نگاهی بیندازیم به افتخارات دو باشگاه استقلال
🆚
پرسپولیس!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/28823" target="_blank">📅 23:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28822">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isJ0yRKkWS79PPGSEYjepUw4gAF27jYxG6ygHseNqBaYJg36paRGDTPVN2lTRA_XLm95Mzf-YI23SH8LqoeC53GPrSPqQwsRykGjyyESUBpetiZpnyP7VyToQVkMMJIrgB2W3zeFqGGIQKgUOb68n_6zt9BYEm2frx86dezjBfa8w_p0l55ED5bzo--LxDel9j-jZq_5gw8x7Wv3Kl2nxQev36mjnqOy7GZjb9UK9pg5AG-2OHK1gxtEcZ7rHxE0vmjaHYlTnl7qvzF8cTtlRaVYv10kk3PnyFrFFPlYhkPcspwjh3N-yAMeGtXxLy5PzbszUbR1M_PiEIqAJrKASw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل‌مسی؛ از کوچه‌های‌روزاریو تا قهرمان ملی آرژانتین در جام جهانی  دیگر لئو‌ را با لباس آلبی‌سلسته نخواهیم دید. "خداحافظی‌ام را در تاریخ ۲۱ ژوئیه ، ۲ روز پس از فینال جام جهانی نوشتم. امروز ، پس از فوت پدرم بیش از پیش به درستی این تصمیم اطمینان دارم"
⚪️
…</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/28822" target="_blank">📅 23:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28821">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fW-id7Qiz6byur4lNMBvOm7MhOVFKkBFUQ9rEm5JCzCcEKhOR0iVxnRKg4iJ3iyNAb2-bsPGugC5h0pwWR3Xfbp4QxCJtHzvMaYg82pgO5N0IZSGWIADWPtTQ-Vu_S-dzVp0Xvkh6yyuWCg2GkoHVQDiI9br4H_mXM6o3vOywOpjSMc8m4TeXstcLghcd50V8QtfZ7hoT6L9KrCK42VOfZmRJO4aRpDt_xeAJMAg7HMcQV4Jj6C4YgZusCEreV295KGNTCLILxwEeUC8W3MxqfuIN8em7kcNvsDFamXZ3392EOTjKTNQYztjVgQIybD2-rqcN3VqfswHdtpXGasE2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف شایعاتی که امروز مطرح شد؛ همانطور که دو روزپیش‌گفتیم‌تمام‌مصدومان دو تیم استقلال و پرسپولیس یعنی‌مهران‌احمدی، رستم‌آشورماتف، جلال الدین ماشاریپوف و سیدابوالفضل جلالی درلیست دو تیم برای دربی قرار خواهند گرفت و مشکلی برای این مسابقه نخواهد داشت. حالا…</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/28821" target="_blank">📅 23:20 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28820">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d24f702f0.mp4?token=OiGJ18oewAzBxkgDTjNVQO_1AEmDUa6GMWcdBkg8xnDD1ZEDhg9D41kFkGkq6tzvdBbc7BhbLuaNmRLF_HYV65cOUk07act7wHDW1TprbKaj-PFOex7yT6jKNnEhW9G1vpt7yCtRPQbnYwDiidHeks-irfVwbIsKARNTlCDf3SIjMoH4CZffWFrFk_QLvZA3YcI_Dn2JVDxLj86-3sU-LjKFDrlR3D7AZGwwV2HCSPw_Mfewdesn5pjliV9NsWkX_EedZ5Qtv33v6_MD7-MZ8l_dmycSBQi02RoDGR7y-JSqgHS9Dn6j0RHzQIkZjLhg9ZZIxShnXHMEwv0xYUCq3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d24f702f0.mp4?token=OiGJ18oewAzBxkgDTjNVQO_1AEmDUa6GMWcdBkg8xnDD1ZEDhg9D41kFkGkq6tzvdBbc7BhbLuaNmRLF_HYV65cOUk07act7wHDW1TprbKaj-PFOex7yT6jKNnEhW9G1vpt7yCtRPQbnYwDiidHeks-irfVwbIsKARNTlCDf3SIjMoH4CZffWFrFk_QLvZA3YcI_Dn2JVDxLj86-3sU-LjKFDrlR3D7AZGwwV2HCSPw_Mfewdesn5pjliV9NsWkX_EedZ5Qtv33v6_MD7-MZ8l_dmycSBQi02RoDGR7y-JSqgHS9Dn6j0RHzQIkZjLhg9ZZIxShnXHMEwv0xYUCq3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نادر محمدی هم یه تنه تمامی قوانین فیزیک رو داره نقض می‌کنه؛ در جدیدترین اقدام این پرتاب 45 متری رو در لیگ یک روسیه انجام داده که کرک و پر تموم رسانه‌های دنیا از این پرتاباش ریخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/28820" target="_blank">📅 22:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28819">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7g6t1_psYj8uPFRPLG1MA0vOxgc9h8RnbCOGWoArWcQOlqkLMCnrNWBrwsRNjyysqEoBgA_MW2cVbVJHIHT7odRctOkxMOM7pg722E0sdcTL6byZu6eCd4ghQcW-sfV8WyWBEh55xaFPkYD4TBLwRTWU5WYfdldrVtC_InTdiwj-5kUElZXuMN9hXcChnwDucYAYWbc8kYMk9CzhdtIiyUzlEB5RW-Kx8IVfNff-Eegy20aVpDc4T2gRmPDSSuGPkLBiCkZr6r0q75C2nKmBheZYg02LrGsYD3VKzxeoC0RmBYNzGOhL718LBp6sHdusZ2cXx41NlKYY8ctUXu4AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به‌مناسبت‌شهرآورد 107 استقلال
🆚
پرسپولیس نگاهی بیندازیم به دیر هنگام ترین گل‌های این تقابل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/28819" target="_blank">📅 22:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28818">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPdLMqbYhOrYMF36irZ14r-i5lpeUfYnDAvGg5w_7xxzWeZIeHZXLUyXMsL0JR2YGnB-qng3YBC2zmhR5j56M05d078hCjQQDl3WV7KmRDn3VxvZCurFhVtrC1LJMVWZqRccbYLHgiBOIcSOunyhqQfb4ektXIbJzMYp5njonXH-5ZXH9E_-RAkrHTra9Xeu2Ar53aC6yWHOB6KqB6xLnnIV3FFu9Q6nn5Ne6oIYLEFEN5NIOBogzOYGD1XCEO9zNEeOJqIt4rWBo8R__7xafeYCy4iPb4HUWBBvtozvbKqxvGGsHek9BGJz_Q0cdIOkeSi52F1ge_194k4ZxW6YpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
ایلیمان اندیایه وینگر راست 26 ساله سنگالی اورتون باقراردادی 5 ساله به منچسترسیتی پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/28818" target="_blank">📅 21:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28817">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aa9U1tfgY_PeIwyevoXUoLIapfeGLwHLBWOuQ0c0dMAXRB5LcpqFX8H2TQcOIoxBj1gtDIM8Fqc3VCcJxUVdsjVqtGfeFS7rqlNpdAtqrWYjn5tCHWwsBnEk9UXymSk2EH8uC0vq41Pf7oIkJBIEXke5-0ldZb3WFlbbNtUSrrLHy7D_l0stApK5CxbSM7v1BaNSDD_nOslPhdRQ7tRNWzp3_SRrN52d1ur0CYzvVrPGcLkTOWDXtlzw6KL8SsTX-15Gwq5e7NlAIurwJfZZI9sG6vsGHKgbf890EFbIvNAN_oXQKwC6xowIFBXTKNxMjGQYewFNmgbUsO5wNdP-Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لالیگا
|شماتیک‌ترکیب‌ بارسا برای دیدار امشب مقابل رایووایکانو؛ ساعت 23:00 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/28817" target="_blank">📅 21:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28816">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQaRiiFc4VfLf0GoKSg4RQXJWk_nv66Guy9I9hCm9xDdNI5-fkXdYRdOwmWjs-DoHyZO8Cu5xPAWo4Y-0Q-mZ6zi-MSDzStN_7ug5vIEMzDT6bYLJZiDPtP0HkuABliwWDroBG4yeedRiBBq100o5Tz7k1820qdgub0pmD8HVX9cuJm8TL0IzcVpwXA8z1V3QoxcDsxfMx3Lg4X-IDn-f7XwZWAgRvn0abPb7-eyzVY_zGcaaTezozKCJs-e2rSj6C72j4EWD6GCPeKlG9J0MiFudrSZgwnGeNHstajjFhlxa9pRz33Yp8y56CXQFf2n73qGkQcsA-NShX63ZqzH3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باتوجه به‌ سوالات‌زیادی‌که پرسیدین؛ بعداز پیگیری‌های دقیق از مدیربرنامه یاسر آسانی بااطمینان‌ کامل اعلام میکنیم که‌فسخ‌ قرارداد یاسر آسانی درسامانه فیفا ثبت نشده و تنها یک نوتیس برای باشگاه‌استقلال فرستاده بود و هیچ‌مشکلی برای همراهی…</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/28816" target="_blank">📅 21:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28815">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‼️
به‌مناسبت‌شهرآورد 107 استقلال
🆚
پرسپولیس نگاهی بیندازیم به دیر هنگام ترین گل‌های این تقابل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/28815" target="_blank">📅 21:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28814">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2-W4JrUohIrcKn3ryiUyXTX7hoqQv8HvCUSPaGjWm9U7XIp5g2Ze1IKWG0BXooyodDqHvFs-ob-zk4dImh4VVxXBDNJApOX9mlO-UGuIFt_WdiscFvvXCXCa9DGKb-YiyNnuPU5oyrGGACg03xA6vJrmGWgxIPdawIVN2BzNMpS6wdp4nQ6ADC8VdL3mmoqfnB_8NMQkf0pUUhbFCUJoZaRTnQKAfgQ7J_lFFel8MuAAqJHEX_M3ySymPWCJqgi7WWre4JDXbYf4vd_Yn4B0u_1Uy0s0bovkHU1N_W_6agUb4KPLU6rCK7fJySnvV6SFUFFXNu6aHbebhQFRShSuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام‌اسامی داوران هفته پنجم لیگ برتر؛ موعود بنیادی فرد رسما داور شهرآورد 107 پایتخت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/28814" target="_blank">📅 20:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28813">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIVZ44xKGIFXsRO1ChLVrCS58ZvldZlUWD0-l6qiqMhGMq3WQB-D1q82cwshbeZB7qCCG4sCVTGa4GL5PrZUMdYkL8HnBix5fcM4pm5T8k49UW8x15WZTzqSlJV04VD3JKJHdiS6S9S0pdLlK_uUcytGm8BCkMeWJimx9bLdHOybPQ76MEOh6zZoXF5qPlx2GuQ2I6BCDVPNncED7yYG9kDi3uDCwsivmjFcLjnHfeNLBz9o4wfpD8jgfTQhyVp96-0_MS3dqeniQWuFRI48omf2dfoIcsgd542cGXBiOsQPmQ_1gskJQfU5ntZPfR2Hl0yC8ubnJPij1GfZ_t88XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🔴
جای‌داوروسط و داوراتاق VAR شهرآورد پایتخت عوض شد؛ موعود بنیای‌فر بعنوان داور وسط دیدار روز چهار شنبه استقلال
🆚
پرسپولیس انتخاب شده و سازمان لیگ فردا این خبر رو منتشر میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/28813" target="_blank">📅 20:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28812">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGFpmJ5H6PFNuPi5zDElqvKVIgD4XDbELq1W5ZjHIELQBLJdmEuP6LANsb8Jt2DVdQyLMx-kFC1BiVx_WTXn5ZMaaZ3skpXVqrRFsTXSVLy4AabzCjQPY1twkxgWPG0G0Y29p9Hj1Iqr8nk_Vt6uy23dZqtd4YC7BtSALs4fQ0wR0nLXIKS2LEQngnr6k9r5UbFBJ0eeSJqGhhL1PfJPe1RKPWmXKV3ZnkhsyJkob4hR4Cq6ChyOVI7GWgrlUyqpsPImBmoJoPi9SimTRkYVZADVYy8p7wDmIh-Ljtaxgv-n626TxmjvBSQMiVWVDG8T82MdO64nANsosZI5HujpvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
آنتونیوآدان دروازه‌بان‌فصل‌قبل استقلال رسما اعلام کرد که بخاطرشرایط‌جنگی به ایران باز نخواهد گشت و مطالبات فصل گذشته اش رو نیز بخشیده و هیچ شکایتی از آبی پوشان به فیفا نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/28812" target="_blank">📅 20:23 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28811">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lOUPfilcmWZaxAb4FFhQFxFb7OtmbP2Q49vwQaWcTjBzE72jWTk1rImmKrquDGup3Guh-MNCJ-oaDKx5JQ42bvmVBhSGabD2e6Nmd2Ht0thr2HWp4wLX5vRCljbif8cYMDX4HMuskoDbSAhOwz43CVdC7jwMPRyEUzKCs6jEfwqrDLfis2i-RhixpPAHTNtPdAxg6fK7NpNV5VJbegspY4Vll1ZFlIH4Q-O2Uj1VoRlrOHVGgZpVjM4R_nhhJKoPrHOaHiytJ4nB1luE9i2k8RQvVAEwrM62h1N8YrEVLorKcFA8CKMyKqm39bq3u30NeW_pwk4g92SSZmH1W2Pe4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
علی‌تاجرنیا رئیس‌هیات‌مدیره باشگاه استقلال: اتفاقات‌مثبتی برای اهدای جام قهرمانی فصل گذشته لیگ برتر به باشگاه استقلال رخ داده و به زودی اخبار رسمی دراین باره منتشر خواهدشد. در تلاش هستیم که‌زودتر آنتونیو آدان و نازون رو به تیم اضافه کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/28811" target="_blank">📅 20:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28810">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOmYQLjhilLCFm6eghSEkm-I_970Ah4LNnMs_Hsn39bbQcQyHhwrU7wcxglVJ9mxUcAiyiiljL_lqmZ4DtHvBicvqZ8SxnIRmo22xNuAt2zPRT-VzebVo25P_fbbiZm30qvQBVqG1W_wIX31LM4tOOilDbdRy22S24j8EI49wlweNrjvlV5YGTZKuU92JvaVDtIz1oW6YCQ84ggMhj-PH65ALRvhWwAEVkbeBnLhM19Vjnqu7rkKIc6bl1Y9uyP7EplCicB9hSHdnNlihm_I-CIUhatuxJxqFHe8tW9Jg9M8-V7-UfjgaVNurKihRtnThLu4DpN8bsEFAVvuaP2nFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#فوری؛ انزو فرناندز ستاره آرژانتینی چلسی با عقدقراردادی چهارساله به منچسترسیتی پیوست. فابریزیو رومانو بزودی هیر وی گو رو کار میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/28810" target="_blank">📅 20:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28808">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2y7fIEhej2K_7sgFjI9VHbxocxtSGL7Vc_LAgs0KbFu_pOFihwxf08g5-2EHYbGXr6UB_qTAxggD72w93VWrwVnla5fr9EeDfuauqy0glMuHKWrQH-Ba8FeYg_IQ_CqObcaZ-r0M6nsxzCucRD4HQx0Um8ZJxi0Ltb18fYhhyH4qjGsDPEu7JD6suFrDRv5Byy1dfEY2SFNHipEJPfQUelpuSQfjgAg6l-RDndS-fl1FKLgWAxda244qEsFmBCWnQSoHwMoMZk5_df0ce3xzZTrszGx2LuMQVr7EMqT4e2eyqanDV3SavXwoqqvz9VLt-9h6tPVkxu_M5-SAtlTQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇱
#فوری؛دیویداورنشتاین: کودی گاکپو ستاره هلندی لیورپول تصمیم نهایی خود را برای پیوستن به منچسترسیتی‌گرفته و این‌انتقال بزودی انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/28808" target="_blank">📅 19:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28807">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cae4f4c53.mp4?token=I-ZOrTfP2OSFs7Avk8TrutloNCgRG-Mpa06jeoaS1nSQjacUi5ZvbR463xiJixQdUwAMVqvVJDpiJz9_Adet7kdMCLyxiYH2syH79QhRvyiyhujShQpts_ZhhmZ6MArBt1CVFx-32W4V8TohEeK1O8wYSp7Tsxk6-4GwnCHNk3xDlR7oly0UKoPZvsL1cBhzpLgiKzDyHec9JHlWFUZnkt55NxqiwnYee38dwZ84EC1xyBTxjIMh-FErYXUoR6UwrANFqqTAL8TQrku51XfzDIJIqDny1FdzDTGaDMNpsYvc1k5jTmaE0u3AkoIMkcOdJbqI46SrspFx8wdstXq5uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cae4f4c53.mp4?token=I-ZOrTfP2OSFs7Avk8TrutloNCgRG-Mpa06jeoaS1nSQjacUi5ZvbR463xiJixQdUwAMVqvVJDpiJz9_Adet7kdMCLyxiYH2syH79QhRvyiyhujShQpts_ZhhmZ6MArBt1CVFx-32W4V8TohEeK1O8wYSp7Tsxk6-4GwnCHNk3xDlR7oly0UKoPZvsL1cBhzpLgiKzDyHec9JHlWFUZnkt55NxqiwnYee38dwZ84EC1xyBTxjIMh-FErYXUoR6UwrANFqqTAL8TQrku51XfzDIJIqDny1FdzDTGaDMNpsYvc1k5jTmaE0u3AkoIMkcOdJbqI46SrspFx8wdstXq5uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
لیونل‌مسی‌فوق‌ستاره تیم‌ملی آرژانتین با انتشار پستی رسما از بازی‌های ملی خدافظی کرد و اعلام کرد که دیگر برای تیم ملی آرزانتین بازی نخواهد کرد. خبر شوکه‌ کننده‌ای بود واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/28807" target="_blank">📅 19:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28805">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FRikZX29O52KrGXOMDI_7Cmel6aMS1A1gVuYn3VOGT0Ps5NHbmvbDDAdT7RDnd2uMO6g8y4Yj53kTuKoyBn237vzsDiPTrUQY3joHYsc2WzrLllNnZGhL7rYimS_B9pz8qpoMmAoKFXzHqpFHbyV0QQuyz4DOXLw100Ux-r9NO-mkqLhA1gadgtoI1iTe8HRWT5Bbtlv_Cw9Dht5ZhYIp79iMfyCkFoelF5cKsZ72CHFtxoCArgY-VR3YD-66zmjfWCRY1ky3fCtS9mZLD_dqxE4Gvgf12Rzz_l-HugG78tO4_zQ-UhJYroNoPb-Zg_DbJbMW1ULi-rbzuFob3987g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R6ojRH_J8V8B8WBdDlvNlx_GgcGYKW8nbK7mDTxjZRtKEHF5ahXK1RBcnL0vrNGV-NBaVM_US9IHSI2CYK55DGVvQWz_Xjg5bdW9mqP6z6jUWllFsxFAD6O8D4PcyEgjEWwYOgg9z5noATDztd4CN5eOBmCXDUl4UDeYpNXRAjPJnatG1tiyAyvVsIBrctzMzR5MptGlEjQSybfQIt2SSvP8mnQVFfAMegRxfLdzZlxEv4Tv2C8o39polVSWzHBJhgU3xB03fCk6WD_dCChSDQ62A6g1mccB2eDnDztEM574_OaIWnEzY9IvQDNEwXjvdsi3YIsNqtlfDWk2YxZPrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
🤩
لیونل‌مسی‌فوق‌ستاره تیم‌ملی آرژانتین با انتشار پستی رسما از بازی‌های ملی خدافظی کرد و اعلام کرد که دیگر برای تیم ملی آرزانتین بازی نخواهد کرد. خبر شوکه‌ کننده‌ای بود واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/28805" target="_blank">📅 18:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28804">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDo37TsF3na8FJO7nhUJewwTake_ieB_JnSQADBwZ0z7su3PpyMpImclV5NU7IXH3oODxPb_wCa6W6CcKUn_QU2d8FTeUZSJk2nDzswjx9zMW6zlJtf_FwMrSTW5WOHV7oqAR8hDZT_3ug_mqieWdAO1WfpAfxn1B0zomI2UrM_lSu9VmhoBn4DxWESs6aYqswA8JTy3UZO0boxBYzOkfB4Q6UnsBapjzlGFlJuHWTEJ1ssCHljgyiQBezjNP_HQmd4ckIbQfLHJBmSvw5gU_f7j9kRAXZaHq2whwluXfCdfVIbtieYQBrTNmo__P-p1UfFWhNRvYRGtHJYhFVguSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف شایعاتی که امروز مطرح شد؛ همانطور که دو روزپیش‌گفتیم‌تمام‌مصدومان دو تیم استقلال و پرسپولیس یعنی‌مهران‌احمدی، رستم‌آشورماتف، جلال الدین ماشاریپوف و سیدابوالفضل جلالی درلیست دو تیم برای دربی قرار خواهند گرفت و مشکلی برای این مسابقه نخواهد داشت. حالا…</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/28804" target="_blank">📅 18:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28803">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1X8AcvqVbyD6jbv0hSOPhkIfjeL_QO_595h2ad7xNgMANx6iMN_dz-yOzlp_b_HMRWlxNKOrb0fppOaKVDO8c50bnzdI8145u4MnBgEbTtWJy4vRv-fc2yzekrezUM964pZ3MyWiu_tkk-aJU9wIpG0hZRzQAR5KRxWd6jwhkDeKH659qRHDe_eoPnktpG9m1Zt3UNPdF8GQSeFCjyR3fg7edCYsntY3ERrdXX9T-57aztGVtUE3g9bqX2xainQcz_xb4BVXcLNx-icq-3oWVqTe0xiJliEM7JZIlNRC5mt_YX7cEDBMYkm81ky5zGyrCKWWiHGm0FKYGF1ohqKpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
👤
عملکرد فوق العاده لیونل مسی 39 ساله با پیراهن اینترمیامی: 98 گل‌زده درتنها 111 مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/28803" target="_blank">📅 17:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28802">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttt-kXTkt2UYebhreqvgPaYKwLvcHilV9dHDlI6JyIRCaazq-OTrPQcwbc0FEXCJQGSe3NEvpLSOd0FZdKQQb1jtpFn4flzb4wofDOiTF3TqhKcSl_TGsx-h-1o-Ru07AKxMzEB_JHBtfk-wXxOLIF1JLckQFKeLE9sRiEx4MZ6Q4mAsIToPaXsz3R9q3Ikxq7E3V4ApxApfn-mcBbzKifqkX3prFAFPvvwc2Jce2PM6TPTNETafEi6MsItLbW5Crgmc4k0CxT3_tkVYOy_EjYg0gayBwuofEBTkCFborXFB2E60dzj9xhmsIZl6IQKKoI3XG4ozp-rlh4WHN64lkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇫🇷
#تکمیلی؛ سانتی‌آئونا: کریم بنزما ستاره 38 ساله فرانسوی‌قراردادش رو باباشگاه الهلال عربستان فسخ کرد و رسما از جمع آبی‌های عربستان جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/28802" target="_blank">📅 17:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28801">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3ImQTeBUzrHRpnSF40Yh401Jd86Kj6GNMxwTj9aNNih-HY1xwOJflDsfaGObUpZN7pqhwIqZEg9C66t8ECF-NcqHvZWkoWUxYk71BTrwn2hWf8iNGJAxzLn7ufGvT-9am25gebTB5ubvOonyHhv-Xxtd6hcsCb2piEW8wHpnlrXOCc541tYusexgusRt-J-PLljdoov39163IwgxuAyQSFqR3Ci8vy6I1QpV5JiDCv4QISdvEndrf0ZytAxgkiKaDrYdCrZcM-SINpQ14TACEd_D3QOXXAP23-qx94B_gC0Vkv4dSOfj1_i7GbDasQcL5Pn0J4hcsu5DUi6wkxJgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
سید ابوالفضل جلالی، مهران احمدی و رستم آشورماتف سه‌بازیکن‌مصدوم سرخابی‌های پایتخت به دیدارحساس‌شهراوردپایتخت رسیدند. تقابل‌ بزرگ دو تیم استقلال
🆚
پرسپولیس یازده شهریورماه ساعت 19:30 در نقش جهان اصفهان برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/28801" target="_blank">📅 17:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28800">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/joAK1CO-yp3o-5FBRAbW6UeGa__1RqomsmRB1_l_4owPELpsD6mDOElQ9sigTepo06fN0ko-5IY3Se2B-UO-z6WgKUCnvspjtG58kpB3FQvraNbV_b9VEwHEJQINViguNgPxYVFw6MUxTiuf9ZdKOOsWgu1kYhlCIMVMxkRgXRHQkxN7rSgGyYtRK5X1gxBC2yxMuHTgahhuBU7kCUX5B5xtmAkx7II5DcJKMpIMJtyIdH5oXP8bBeg6JnIEfrrgiamg8GLFWLdWjRg5XoEeWhOR_45-_Jc94Z9_8pWd-u6Vb4aRUaksU2UFu1q34vmmTyi2jOH4QDG7nAOOzARWCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رونمایی رسمی باشگاه لیورپول از بردلی بارکولا ستاره فرانسوی جدید لک لک‌ها. لیورپول برای این انتقال 106+ 17 میلیون پوند هزینه کرده است.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/28800" target="_blank">📅 16:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28799">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f80bffe56.mp4?token=aXnfzmUvMOtz8ddCST-Ve55uT7TVmfBfLz0nwuemfTPSp_6LzMI2oWLpVIHAMnCNNdyqs2zRED0CGfY1FrLoB5391m1wpFbvYjJwvgV2LUF6H2FzsJZ6XrCO4xq8ngEvnKiEMm1WqrvLQhk-15ZrQgMjJ4rSZxDi2tgUSAtUzgLlxMxXf3cxDiuN1ws64DjiGRJGWS6qw8wsw1k48rSx3ZH3eFc9W9ljYnLVJfude6VVTHELM3kxtVKsyVOyo1K_iulWWKb4JYTK4B26mQ2uDG1gERoAcKWqNHfrv0DXL5lLl2fmH6XbnTjGmFm22GQAMwxfKhulVhi791VICkAz3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f80bffe56.mp4?token=aXnfzmUvMOtz8ddCST-Ve55uT7TVmfBfLz0nwuemfTPSp_6LzMI2oWLpVIHAMnCNNdyqs2zRED0CGfY1FrLoB5391m1wpFbvYjJwvgV2LUF6H2FzsJZ6XrCO4xq8ngEvnKiEMm1WqrvLQhk-15ZrQgMjJ4rSZxDi2tgUSAtUzgLlxMxXf3cxDiuN1ws64DjiGRJGWS6qw8wsw1k48rSx3ZH3eFc9W9ljYnLVJfude6VVTHELM3kxtVKsyVOyo1K_iulWWKb4JYTK4B26mQ2uDG1gERoAcKWqNHfrv0DXL5lLl2fmH6XbnTjGmFm22GQAMwxfKhulVhi791VICkAz3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌جالب‌از استادیومی‌که.دولت تاجیکستان در عرض دو سال ساخته. اینجا هم ماشالله با وجود حدود سه سال هنوز ورزشگاه ازادی بازسازی نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/28799" target="_blank">📅 16:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28798">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faeb0b6b1c.mp4?token=rG-AgfKgteHKNnLGdxUNO681F21BJoA2u1V6Ad3K6uaTCySNLxbjVH_DY68x0t9u3hl_ioXYNdQPtMYFpQWutbqVP3t68g2dEw779xvfeccWuuosJlGX4xkhhAcH-WUs_rwtRWQPRqKUNSqNSkZwhDfxUYDDUNAIWlw1c9qHOSM5d6esKS5kExGK8rCxprSeDYLJLLaz934CUZtJaGQqDiATDDg-RfmX172UimfRVZJ-36fxY5_uTcYJ1-uqYgooTWHsUqhabn-2m9clwP0NZo8NzICLM2EM0mN7qnUSl9b9H8IYYElbOKB1VDklTamDYKEC1w3quQvTQuKI-q3WVVJS7UfBxK1m4j2NZLeBVQ2myfOWI_0kL5VK9p_x6chXbRS0HtATmVWUNhN62ZSXu9MMjUUvdwfGUoDjeljTb7Xv_5e9GJoolsHZ7QTTZ-u6dfVTlbQbrq8SgbDWNLmGEJoRO3G-kMbfPLNuiBaroVSAglIpKeMg3p49E5SM7sb3QdWSIUOYT7H9_i6OPnY9QdNGMN_UL_X7-i649Yi7wsoOQT7_SIC_KysaxE46KBcadtMUFU9s4b-x0haMda4AIkkFoU80rFT5aTA1wswDiebBbH3SFZHpBj_GxZF4RWP-zhHDFC9xBXj66RtqOaV1LREp0KoAdSL8K9YrN0iKBqs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faeb0b6b1c.mp4?token=rG-AgfKgteHKNnLGdxUNO681F21BJoA2u1V6Ad3K6uaTCySNLxbjVH_DY68x0t9u3hl_ioXYNdQPtMYFpQWutbqVP3t68g2dEw779xvfeccWuuosJlGX4xkhhAcH-WUs_rwtRWQPRqKUNSqNSkZwhDfxUYDDUNAIWlw1c9qHOSM5d6esKS5kExGK8rCxprSeDYLJLLaz934CUZtJaGQqDiATDDg-RfmX172UimfRVZJ-36fxY5_uTcYJ1-uqYgooTWHsUqhabn-2m9clwP0NZo8NzICLM2EM0mN7qnUSl9b9H8IYYElbOKB1VDklTamDYKEC1w3quQvTQuKI-q3WVVJS7UfBxK1m4j2NZLeBVQ2myfOWI_0kL5VK9p_x6chXbRS0HtATmVWUNhN62ZSXu9MMjUUvdwfGUoDjeljTb7Xv_5e9GJoolsHZ7QTTZ-u6dfVTlbQbrq8SgbDWNLmGEJoRO3G-kMbfPLNuiBaroVSAglIpKeMg3p49E5SM7sb3QdWSIUOYT7H9_i6OPnY9QdNGMN_UL_X7-i649Yi7wsoOQT7_SIC_KysaxE46KBcadtMUFU9s4b-x0haMda4AIkkFoU80rFT5aTA1wswDiebBbH3SFZHpBj_GxZF4RWP-zhHDFC9xBXj66RtqOaV1LREp0KoAdSL8K9YrN0iKBqs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔵
باشگاه پاریسن ژرمن در این پنجره با فروش پنج‌ستاره‌خود 335 میلیون یورو درامد کسب کرده‌. البته انتقال بردلی بارکولا هنوز رسمی نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/28798" target="_blank">📅 16:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28797">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLH0EOvmRACP_5H2mAApk8x9gXEsZkHuFYZtawS6kg_UZ-LzHBJDN7QCPfOZBbx-qby-P9Yp6ijxETTbVhzAxnnAASHG15uQ8Jcamcb-cMMRPOgozv-YHrDwUXNUrVqPz7_-THsUTTibX2ymGnK5nn-QUFz4107i5dxn5sxWyj-LVglEIpUYG07VE6nH--AzcUWLUTJdy2co8fIGk_S3stiwG-abMAtwEHcXVRouXJ9Tnt1_oQahAm3EUS0Kc6lT64q82StJc1eNz4j75ZBum_h4OpUXzsQJpAKeVfZmy8482DabTsrG-wjEJv-B677wr2m_KBRorNaOa3mKEK8i9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
خبرنگار رسمی باشگاه‌گالاتاسرای ترکیه هستند که معتقده این تیم امسال قهرمان سوپرلیگ ترکیه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/28797" target="_blank">📅 15:13 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28796">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRenhWI84rCMwf7kFCnOHTzIqWNjOTWtBTXGEl8hMnjAo4G2SSqPEnYWRZag9_1ntVT6rM_thUWg67N0IoCbXotpaauGtB3Fj6-nl-uNeMv8Q-aevW2jVwIsbKcuhLMeFVdV2t0n9GyMx3C8eGAP_TZjM0eRc9WHqzTLQVJgL0uhcOyq290sZLEoUJ-hW-32P7g9vJcrDiD20n6W4YXhf42vQHhWX4OQlURkYjKfFbbko7oUt_vncqYvBEdw7-5VVX0PYXLI7rOEW3DsYpwEOtJ9kmjvnuS3W3xfIeQLVGVZ4bbHGN8zZDV87fSgpFe5vizmTAwmYaBKHd9N9ITXPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛ درخصوص عزیز گانیف ستاره تیم ملی ازبکستان؛ پیشنهاد مالی باشگاه تراکتور بالاتر از پیشنهاد باشگاه استقلال است اما مدیر برنامه یاسر آسانی در حال تلاشه که گانیف 29 ساله استقلال رو انتخاب کنه و با آبی‌ها قراردادی سه ساله امضا کنه سپس بعنوان بازیکن‌قرضی‌راهی…</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28796" target="_blank">📅 14:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28795">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pjty-09zeO7JbzEC42-K3MBbKK8NjWfnvecDKV0_Gj72tzu2PRHV94U9y-1Z9l0sjDfrHsiN2gHlxgpkGSvtfcqksC4-OLzcb-TF6bLO7T2ugQTSXGZ9vqSri5D82YvEmn7JqQePjucuTpl4kzSkJW4N6xgeXopspxPQz39zztqIkZZ8OoEF2YXqh5BQ7rXdq7BQwYX8H28XStdnC09Ft6N856crS8AzzmMfQLxUL43EQHJrlwResyV7UlyOus-DLz8fR2zbXg0oa3yULV7bCnX9HsJvJ4BpkXTMH_IT_fbQ0qQbniuyaUjSFAdqQ52SoAwuN3FSbtlL6Qho-PzaAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه رییکای کرواسی بزودی از محمد محبی خرید جدید خود رونمایی میکنه. قرارداد دو ساله و رقم بند فسخ یک میلیون دلار توافق شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/28795" target="_blank">📅 14:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28794">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔵
🔴
درفاصله 48 ساعت تاشهراورد 107 پایتخت؛ ویدیویی ببینیم از زیباترین گل‌های تاریخ این مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28794" target="_blank">📅 14:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28793">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DaiX-olW7BPrhWmj_8h1jA96dRKQFqXB7DeWndas4oWVNU_hbnXJT6jddqz56vgdWD3HPqit_pXIR9z9tPU67Rcq6-x9rejFOh4JO1tJIpHAn4-KikG-r4NRDvfl9PeRkivalSkmnpg9Q9o_8Ykp_TAVTq-b4jrRyfbUTl3NASKs-eLdCT4RrFnx_9QbnDGoIArMc8SGQeGKqMEgJnLlXgkD3ES5EczoSK1gjSNrnaB2gl6xmfJQ34lnM8tZe8fhF0dX-5yE_Y2Y8X4STzpTTn_wXn1G_7usWuNxasCnXo1fX4i16borNfm63NYk4Kzhnrx8R-GrsNRr3VruU2pbPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های کرواسی: آفر باشگاه رییکا به محمد محبی دو ساله به ارزش 1.6 میلیون دلار بوده. یعنی سالی 800 هزار دلار بود. پیشنهاد استقلال به محبی برای پیوستن‌درنیم‌فصل سالانه 1.2 میلیون‌دلار بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/28793" target="_blank">📅 13:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28792">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKjOqHj-Er2zadpky97VjiU1oUio9kWv47D_ji1aDseKpPhNMenKsMxUy-Sxr4yL1FBPQ-2ckgOknbmljWPY0eZneQ9HcOMt-TivRwYGXKozHhWs7pqrUlA--n2XVxjAgBEkqY_chjhsFFBM2pbO33HODBDJpKx6wP5OsFtOT1If94AoCWEUdpUTFFWw9tTesadt2rwPaDThGc9ezKucQp3lcJRBzASYg4AB65bPDVvCIYLqjFljCRsOADKNItJMPIUrgjsakpFenRmkiWLS1YBSgSvbPju_Bte1opnNbfwDa3KYll5Ta7mQxXtmT6dc7ZWQ4eZK-EOH9Bes7I5cVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ به احتمال فراوان موعود بنیادی فر هم بعنوان داور اتاق VAR شهراورد انتخاب میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28792" target="_blank">📅 13:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28791">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/627b425286.mp4?token=MoRYh3g8N5Yt-dWBAIAgFxehp1PHPIDh4gy68AhzGi8LyjFGpJeJjt6G5AULgzuS7OXr8ZMCnZrTsLZ2IgKvvSJmJb4qpOQJBZfdLiLJMkxBVtsYZH67gq5a0yerNuE4Tp9C6l3zz3pmigB0J6kB5BJbFgSay5FLeg2JLwbyrCTM85SzuHOJutI9SKavaUFklKIvfjV262zEBwF5jV4wrPiQD8H8S1W04Epa46kXxQzl8JmyujCMByxvqj7Q5eH-1tFOGAaPwLeaz2YpTCe2BqX3DsRpuQowJSP7xf189HrSyoiptmGws6vIk_JTjvX9SY-6-K3M5uUZmqsdMC2PcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/627b425286.mp4?token=MoRYh3g8N5Yt-dWBAIAgFxehp1PHPIDh4gy68AhzGi8LyjFGpJeJjt6G5AULgzuS7OXr8ZMCnZrTsLZ2IgKvvSJmJb4qpOQJBZfdLiLJMkxBVtsYZH67gq5a0yerNuE4Tp9C6l3zz3pmigB0J6kB5BJbFgSay5FLeg2JLwbyrCTM85SzuHOJutI9SKavaUFklKIvfjV262zEBwF5jV4wrPiQD8H8S1W04Epa46kXxQzl8JmyujCMByxvqj7Q5eH-1tFOGAaPwLeaz2YpTCe2BqX3DsRpuQowJSP7xf189HrSyoiptmGws6vIk_JTjvX9SY-6-K3M5uUZmqsdMC2PcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
بااعلام فلورین‌پلتنبرگ: میکل بازا پسر خاله شانزده ساله یوناتان تاه مدافع آلمانی بایرن مونیخ با عقد قراردادی تا سال 2029 به بارسلونا پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/28791" target="_blank">📅 13:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28790">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezR0nawpRzDyJLeG9fBSvMrGXce5IxoLYswz9FGBFFIBZLhc-E5GjW5Fd8wYYdntGb3SoIhbSi0yjHXpCdbS64KzI-c0eZpIlXXQah8MYTnF7wQ19tfDOwNoip2vR1j6dlNdrQgR6-lWDSUS3Y0dfjCOy5u1MBqYR74VQWkYzwcVtbrQVPnUZr3j4Gdv37vQeUZecUSQ6Hy3IYEwbdwp9HDzkrKz3hYA9dlze5PkcF7cdnKEn5JNSCdjuD9M8R1LruNmpgBKJjpYLy2HYef17ijr4STxn_AjnpAbVtKCGRxrFCL6YnOqF86Eu-craO7WL90lRkRwnu3IZ1_u_ob6Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سایت فوتبال تیکت اعلام کرد که بلیت فروشی دربی از این‌سایت انجام نمیشود: بلیت فروشی رو از طریق باشگاه استقلال و سازمان لیگ پیگیری کنید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/28790" target="_blank">📅 12:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28789">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUgAZW7eLq8ywUvcoTitjtS_XOv5kr7604ucJOdzPPIX5JQhm9NWrlXi23PwM5dBqmPB2BNVOnygiLeV4T8iPDb2Wo_OYS6NPozhZOqDLQlN-IBYOpHVRnIjp5AlYb2aI7Rtxkf2XttHhOLZLFvXTJWyy-lGUkTz7hWnPAQUKZbLSKxwHvzIWk2vx6HeU_CIBy6EeM-rKWXE3x2EIm36Assx6IQ3kLj7LJVKGZYF7FvsFoNNZuuZqux9mW0_9UrxKQHZrPHkwzR5zQ2yGvAgdoxXV7jZpY9Hy9eOgAKC_kqeXmqxLiULk-iUzLR5Y_avKtu9OXNa_tr7q5cEf4LGiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
هفت خرید بارسلونا دراین پنجره که بابت جذب شون مبالغی بعنوان رضایت نامه پرداخت کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/28789" target="_blank">📅 12:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28788">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIv4JSyJMcSjFBfENfbBZNJzrX42ThBlqlNyqyMxGWo6URNNIon_9ZuOdNlKevCtzZQz5gJGjTdewUn3wXKY0KjUbdObnkpqiFfHMGqQMf3IAi0QI8kmgmrgcC-7l--7AyIXv6GMMqU-M3m06fqKvxu798sslKCWcgN60zEQQ94-B2T3dQphL7-pb3oIpUMryCAuc98tX0SxXATwhyJtiC6BXQDWiJGScNx6xhfZMo_zHDvcx9SLx6Lhf21QTrhpc2B5tUssw0xanvtwApmNhfY-NVaUfVBNTWOHeuPruThNnykdByVjcLBbqRv9b5-M9xKG2UzZWrfn30mfAwyCYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛ درخصوص عزیز گانیف ستاره تیم ملی ازبکستان؛ پیشنهاد مالی باشگاه تراکتور بالاتر از پیشنهاد باشگاه استقلال است اما مدیر برنامه یاسر آسانی در حال تلاشه که گانیف 29 ساله استقلال رو انتخاب کنه و با آبی‌ها قراردادی سه ساله امضا کنه سپس بعنوان بازیکن‌قرضی‌راهی…</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/28788" target="_blank">📅 12:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28787">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtnPSrRFY-JXdkIdFAld3VcurQ7NcNJNWHutV6welXdnplTPz1rD81rS1vQKTGKf7FGpJJFkHqQg53YMitplmRPavsA-eMeABX5n4Cns5Ub9MK0IHEeuiehNQprI87ZiJMxTRpnUR_XBTWppsBBnjttk90dZjOwgPVkqMuNRL7JtiW_7W7Nn-DEi17ESfStXNLHe653ZerQuvQ_TTR8bivRaMl5P3CQ8IuLVl15GVKvqSflpIHYIEHbFkJtzpg_Qc3QA3ENJzpqZ8VqZSumACUsjuMKvxP69TBZUFgCc2YJfEYDhBDTe8Oq9LdRVWlSqeojZRNRigfCG2lBbh14vZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
🔵
#تکمیلی؛ طبق پیگیری‌های رسانه پرشیانا؛ درصورتیکه‌هلدینگ‌خلیج‌فارس‌تاپایان این هفته 400 هزاردلارپیش‌پرداختی به عزیز گانیف ستاره تیم ملی ازبکستان پرداخت کنه این بازیکن قید حضور در تیم تراکتور تبریز رو خواهد زد و آبی پوش خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/28787" target="_blank">📅 11:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28786">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SawXiI4dD4OEUe2WfZ4-DTOBV3AyGh6Y_VbOvuqgLfl9e6eBLoyMPa2wIAwQYNsqvdkd_q1yb2QX9wIVAjWxUWR8PLjn398S-1jdaQGQW5Io6KsGmFxkHenDX1EoGNPy-u0I2LxNIkrWABgK7_RfYPl6F0YlV7lZYtxJ0uRypuszQcv5Mm4zSoatVhzrlNULLPtnePsy-2tgHq1VbD4yOwTxoYKfaABwypulsFgDDJWjR_11Dqv3JgxiRuUHPxgCj1w1tDa_Y6wH8k34uhKZKg2UWXpUpnMOwuAZiBmHGuOSU7EEZV1QdzePXJNtxwS_4If5W21dX9NJKLoFFw8ibQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب جدید بارسا درفصل‌جدید بعد از پیوستن گابریل ژسوس ستاره سابق آرسنالی‌ها به این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/28786" target="_blank">📅 11:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28785">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_ae0t8zSckjFAP5GVps8pCw5Rw_ehEDsdIcyHAEtgN0uSyQ3QG7vnVecf3oX1Y33QOQpCpZ0PrW3OxhjWwCFPWXgAURH6eOFGTx5NWZ-lwy1RbthCKztrW44-N-lAw0XsSoVtcKTZrmJwVpQFeNu-1povIkJrU1DByShVSv0xqynRJUaxGs6Fkt4QwvNjdIdsSCiDcDLFGU9FTXZ3AO3sw3K3-mVAcNqEbbAmaC8FrbVYCUunLahbw-odlAEXWsl5tzSMWYgS4-xFxhSWCwtikO5GihoeIYc9TvrYAtALMCfRfERjuFNutleGeQY-5PAo0U77c1gf4V3fJCfIc8Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#فکت؛ 3107 روز بدون شکست در جریان بازی در دربی؛ پرسپولیس آخرین بار اسفند ۱۳۹۶ در دربی شکست‌خورد و از این‌بازی.تاحالا ۱۹ شهرآورد متوالی بدون باخت درجریان‌بازی‌را پشت سر گذاشته است.
‼️
سال1396:قیمت‌دلار 4500 بود، طلاگرمی 140 هزار بود، کرونایی‌وجودنداشت، پراید…</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/28785" target="_blank">📅 11:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28783">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLhuKzWn-aNING_ouccILjfwgMgykA_JF6aEJeWiwtQ_FZocBd7_ScoB3EFQK6c2twQXoHffnnTVHaSmyOlCMoVY1AWZXFTeNQ0nnXDc3jVIB86oXx3YQjOAEZnHpRSvpNLhnWYv5OTCjmBkTYydEalop_GAjwGo04-f78J7L3ktTAmcoIzDhXyqychp03RaLlPzTaWbgeesBkxlGtznZSteJIp2-rIlDtKf-tsL94YScl8qgjgsY_ZCQw3iVnORbvDU1--iwLNsQLSViG8-mDDoq5HZZugjp8Kd1fjjZcxzrTPBF5GZ4TkDgArf4h8c1qFUhHEOZf2lqOZvoF7c7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ قرارداد ژسوس با بارسلونا قطعی و دو ساله توافق‌شده. سران‌بارسا10 میلیون یورو بابت این انتقال به باشگاه ارسنال پرداخت خواهد کرد. تا کنون بارسلونا 174 میلیون یورو پول رضایت نامه داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/28783" target="_blank">📅 11:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28782">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf70d43b37.mp4?token=s3S3Oj5LAbcPduJYegQIprNcAk0Hd2K93GBG7xxiNv7b59jOfH4wtINjwZz2lubFr7pYtM8Kr0aJJItYZvGTr9l7VI4Y_Wno6ZdtjRB8BiRPEimLDOb98XLn80QWMdTApbx4K4gdDSgUGbQkeO_9TbByCBmNKuGJX-l2zYNPhWlWjQUCJm_PuFN4vhhcWgqlky88-yVWjBq5tSa1GXxA5rlQzhi4TS2N-Z9Rt66lLPc0v-gG1B20iLWH4jG8qTfVoTF2gd4r20JMRVLPG1tF1cfQU_R-Os0sCRMBXALbeqxFQPd4rPa1BqJwhL4wr0GzlmdmJ-73KdzRDB11oSoaQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf70d43b37.mp4?token=s3S3Oj5LAbcPduJYegQIprNcAk0Hd2K93GBG7xxiNv7b59jOfH4wtINjwZz2lubFr7pYtM8Kr0aJJItYZvGTr9l7VI4Y_Wno6ZdtjRB8BiRPEimLDOb98XLn80QWMdTApbx4K4gdDSgUGbQkeO_9TbByCBmNKuGJX-l2zYNPhWlWjQUCJm_PuFN4vhhcWgqlky88-yVWjBq5tSa1GXxA5rlQzhi4TS2N-Z9Rt66lLPc0v-gG1B20iLWH4jG8qTfVoTF2gd4r20JMRVLPG1tF1cfQU_R-Os0sCRMBXALbeqxFQPd4rPa1BqJwhL4wr0GzlmdmJ-73KdzRDB11oSoaQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ویدیویی‌جالب‌از سبک بازی خارج مستطیل سبز کول پالمر ستاره انگلیسی 23 ساله چلسی انگلیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/28782" target="_blank">📅 10:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28781">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇺🇿
🇺🇿
هایلایتی‌کامل‌از عملکرد درخشان عزیز گانیف ستاره‌ازبکستانی مدنظر دوباشگاه تراکتور و استقلال؛ همانطور که شب‌گذشته‌گفتیم درصورتیکه آبی ها این هفته‌پیش پرداختی رو به او بدهند آبی پوش میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28781" target="_blank">📅 10:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28779">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‼️
هایلایتی‌ازعملکرد موسی‌چنپو وینگر مالیایی سابق استقلال در تیم جدیدش پانایتولیکوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/28779" target="_blank">📅 10:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28778">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zx7uMqdrqmI1xGi5pBStap11Ytti3aO5x-0R7PflnvijCellIdcGaUHMQZtGQ6F9SYsvJPRYD1ronP74fpFRDGOcvf3TzHphmLr9SoBCfjSIPTjQLh3wmNnBRwHxwsDYwyr9sMw18o6EX9tgjdgOe01Ei_LhozOSPOQi5GLeHrjCp4qmffTM9ucBAfNrK1rbxdybbod4iWiM_eprSCsGXR8McPgTAkiI8Bh7rvx7gROgBwnTZE2cKCF-YU-Fqxu3OZYQrQsmPa4sqiWayrLqnO0fy6SI1lc0ytb94fX0AWGSeAd0iBomA5Q_7piCuUb-WkbiQ14pRWOi7RjApLfHjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مصدومیت‌جدید مهدی ترابی ستاره 32 ساله تراکتور مشکوک به پارگی رباط صلیبیه و به احتمال زیاد ترابی 8 الی 10 ماه دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/28778" target="_blank">📅 09:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28777">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0edcdd5b47.mp4?token=Ox1bh-_vLh-DGz0_5DpiWjFaOJ-beb_CpAU0nsNcgoPFnQ6WSvyTuehjiaaRKp5J-wXsTW6TX8-glw7Ny-6etwGzd1sYF059prIdmvnNw7qltG7lWjHWdla1sIGlU2ShjR58c1aTp9tAw_9S9Jf2H5bcZyUmO4Txlr294bi8-cut6iwShuzhDQq_uGRXzKo0aCbM9qPFy_5l_kVzl0DGNjg4vgs9fYdFvl6IAbEAvB5P9HURBCKAy_uW3WJyJi1w_dpOVd3riFVujEMhSv7Ti-D5XFx9Z36ogW_LrAvUTgKXGYoNudYKJ-9UY3UQeI6w8znO8Dbqhy1T7t-0zH3Vqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0edcdd5b47.mp4?token=Ox1bh-_vLh-DGz0_5DpiWjFaOJ-beb_CpAU0nsNcgoPFnQ6WSvyTuehjiaaRKp5J-wXsTW6TX8-glw7Ny-6etwGzd1sYF059prIdmvnNw7qltG7lWjHWdla1sIGlU2ShjR58c1aTp9tAw_9S9Jf2H5bcZyUmO4Txlr294bi8-cut6iwShuzhDQq_uGRXzKo0aCbM9qPFy_5l_kVzl0DGNjg4vgs9fYdFvl6IAbEAvB5P9HURBCKAy_uW3WJyJi1w_dpOVd3riFVujEMhSv7Ti-D5XFx9Z36ogW_LrAvUTgKXGYoNudYKJ-9UY3UQeI6w8znO8Dbqhy1T7t-0zH3Vqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شباهت گل کیلیان امیاپه به مالاگا در بازی روز گذشته به گل دیدنی CR7 به یووه در سال 2017
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/28777" target="_blank">📅 08:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28776">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3785816e6f.mp4?token=erBuQUKAupeFU5qeZ9r82MvBUFYQ2FUZSgvEzWRxH6Xa8rUeeMME4KeRDAirW5rv5xlXm1bGLyVhA02V8DgyozzYWDcTfjusV6XGW1yY8vYnLCRKxALa5V8dVwNWNnbUSJz1WdMoJkxOOruxWCcg32htTc0jZPedrdO5ZEeMa5th-sauaI9Jzk3-PHxZ0kvzcx3dvWc0BkcsL8K_7uHuhXvtsc6CnpaXeVIGt6IfApxAq7JTftiB_S7m9Af4gh33IxutBdaP93QEiakfiHftxhbEkaLGVVhdlj5RdfZBX2svqatsUdU8LKwZV87jVJUpCbdi1aYfd_aa-eqrMTUQRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3785816e6f.mp4?token=erBuQUKAupeFU5qeZ9r82MvBUFYQ2FUZSgvEzWRxH6Xa8rUeeMME4KeRDAirW5rv5xlXm1bGLyVhA02V8DgyozzYWDcTfjusV6XGW1yY8vYnLCRKxALa5V8dVwNWNnbUSJz1WdMoJkxOOruxWCcg32htTc0jZPedrdO5ZEeMa5th-sauaI9Jzk3-PHxZ0kvzcx3dvWc0BkcsL8K_7uHuhXvtsc6CnpaXeVIGt6IfApxAq7JTftiB_S7m9Af4gh33IxutBdaP93QEiakfiHftxhbEkaLGVVhdlj5RdfZBX2svqatsUdU8LKwZV87jVJUpCbdi1aYfd_aa-eqrMTUQRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌بسیارزیباوارزشمند ازهیجان و استرس مادر برای پسرش حین کشتی گرفتن او در جشنواره کشتی امید سازان المپیک 2032. عالی بود واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/28776" target="_blank">📅 01:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28774">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kafFrJwjTIeVjGDwFeo1ISHpY745_OQZimWhLVBe2yapQmTWaHrUcF12ovjq6HGhMcrcx1ap35zgEgw45pUHR2YNZYTdYDB_vRyCE_Yx2VyHsAtq_ensOk_jxco9mWhabTooykaVPXr5ap3wyWHTS0oMtJxw0foeIfUjCJt5fM3Sz0hHnUTX67VLsrHsVt_4foG8ScfRpbqLcLYD4Xv0TljVYnQvwDUB61On4Gf2TCQ0as5B47wDBKW2-Q7oIrBpy2K6qMpCopTL4T_NoarEiE_ifM-2k1QE5NigG6KM8ZVX6xIqf8f79uxKCE2gWxqW6dWZ-Rq8BmQ8hlplQ0Sj3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛ درخصوص عزیز گانیف ستاره تیم ملی ازبکستان؛ پیشنهاد مالی باشگاه تراکتور بالاتر از پیشنهاد باشگاه استقلال است اما مدیر برنامه یاسر آسانی در حال تلاشه که گانیف 29 ساله استقلال رو انتخاب کنه و با آبی‌ها قراردادی سه ساله امضا کنه سپس بعنوان بازیکن‌قرضی‌راهی…</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/28774" target="_blank">📅 00:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28773">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IuxWL571WqHQv-EZrPieB-mLSI6Z3QppOMzTNaig3rGZRO41wjz-PuIbrZOPsnPXDt5Z2Z4YtlWzu1bNy2oZBAH88775IPjTAt4AnZ9tgimxcKmktg4jl2KcqLQjCbEOYSC52zJiZRaz9mmrlPTcR9RIcSHKLc_EUSOKYFxdSt4mqqSvNRCwQ9GtRibptQhvqcU89f2OqDLOMUZ22E53rIG-nO2lq2aUv5sRPQIi3pXpR2djwEG7_Y8WMG_I9hst3bxn3_t3mXiqPlX2zmXpfc_NT9HJW6rG8pRXX9zl6okMPg3_Hqax7R-JX8S1T7mUevRdrujgtuJfnzjSsea6Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛دوئل‌شاگردان آرتتا و امری در ویلاپارک و جدال کاتالان‌ها مقابل رایو وایکانو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/28773" target="_blank">📅 00:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28772">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TiU1AvjW4frBqpvOdzj6xxRpoj6aovfn1_1jRD_tb-lY8eC3fwyVGTfgy9T85WxX6YUfVWyhlPaewS-vAOhGyB-YdIT3osf4--C5a2b4Ewj3xl4rxnXFRscYS8JdUmqFvdX2Ej1PKMOR9wI_RmprMVnlGwYTf-plLiwRCWIYeKU3nCTaziud9lqEaFjDiQveZpsSaL7EY6OA9YQA8_5ogHZLyYxIRtMQYxET3ja2n_0NCLAv4cRd47wZ3EBZFQVUjTOPAZGypVtcg_jnBzrD3RPpc3QsSA-LGcGNGZCNyvsq4kna7yK2vmb2otgFn4qecGUcJuSEUs1Fu7F8diXv5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌دیروز؛
از آتش‌بازی لئو مسی در MLS تا برد دلچسب یونایتدی‌ها مقابل ایپسویچ با هتریک برونو و ورژن آماده کهکشانی‌ها با ژوزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/28772" target="_blank">📅 00:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28771">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBAvKcTDSLVUE6nFc953PBmqovXu01d0Z2_HOVms24JwBHtNZDYJXVXZPuYRRXgBMuHj1tuxFi0txykoWYZ4W_WX4hix2KbfFnFegKnN1jgvVV8bSmgZ2gwClaXDRF5X6K3k2ywzidWG_ooBiv2vrrrV_YhY45Q0w-eSW0aR3mJ-Tkl4ZSNdOrR4Hy3rWNL8cgJjqAIvv8W6VdpEAAhAroFSHUk6EEFbl_YELPdVnfT0FAkIOqHGcYcu18pZeDBCJ5l8aNYKSeXkNHbuiSL2MddJgjBIM3_CDrzAv4xXcGKq_6qr6Ei-MStEutrpHr5pFMIQ_vwPGXtOKxUkvok-7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛بعداز اینکه‌خبر از مذاکرات تراکتور با عزیز گانیف ستاره تیم ملی ازبکستان دادیم. حمید مریخ ایجنت‌یاسرآسانی و جلال‌الدین‌ماشاریپوف در تلاشند که این بازیکن رو از تراکتور هایجک کنند.
‼️
باتوجه به‌باز بودن پنجره نقل و انتقالاتی تراکتور فعلا شانس‌تی‌تی‌ها…</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/28771" target="_blank">📅 00:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28769">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmKFgw_XbGUKxm7GHHSRcL1x0ALvEajzuqJUhIz8tRuAZ7dgRMmDlMbNWbv2I7ijKKZ3jjC6ubYONN61nMJgFQ-jxSVF_U8IELp4oZUNQBDyrS5F0ycZ0opCQcuPS6N8mb_vobCX7qC06TSA1rbrxofb_VLK0HaUDWlFAVyMMA5qxN3ykLL_cdmY-ri60T35VRjUC4d5f168GLS3dz5NUKS3cS2DJ4ea2TjHJVPdUwIWcmBTAa8DTfysO7S7_ZolodTnlCbCBC6gWCUW92zd1bwyRtxBpOyIqS2k-WyuvelAm5jHO301KcZ6hE3MOEMJJwdWwUtHV6zVGf0N5wZR3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
🔵
سوپرگل‌استثنایی و برگ‌ریزون هاکان چالهان اوغلو در بازی امشب اینترمیلان در هفته اول سری‌‌آ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/28769" target="_blank">📅 00:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28768">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTldziiMO-knxdNJ9arUX57HhqqaWmil6gpirN1ujVMkDdfcucl9xDKnUuhIqEIs4ojkC7sHX2sJdDOhZXEqr-1cBJM6eHkvGh4gPrGFqxQjS_v2-N9iMzcHW1lbthy9MwYsUzY_oErKfSnEPoXty20wF0ZX3awNKqBRCyMZ-AQDANPiU0eNyuRf_FYAsM0odMXqbgmJEuzvEqEjuPOR7LOiFupDxB5641bLjocuq6ZYNbNTL6k6M_IngYxVWMlbH7t6SQW1zI6VitWYEOLc3Lhc3JA13CEgYC_TEUoERKO0P2M_COfzlvO0H9bLVkGc_KSN3qfziBtzDdKVZMKQEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مصدومیت‌جدید مهدی ترابی ستاره 32 ساله تراکتور مشکوک به پارگی رباط صلیبیه و به احتمال زیاد ترابی 8 الی 10 ماه دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/28768" target="_blank">📅 00:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28767">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYmg3vH4dcUJC78y2R7ued6vOEZL4xcmOF_fuRjLi3YQ8AVQRJiTRKiiWUphiJKym2C7dN7zO8nirTtJNEb4HfHUldSCUv44mDy-_8Gg9Xc-AM8UhYKLX_KQKOO9jTAjM6gfE8Gjf1P1l_21AtFt_ZL79ynQ19rPFeGt9psnmpGScdMGj-ae6EmrBAbZbdU03jlHfaJJ7rDyIyMd1Uhhz2P9-oj5AOtd7mdMx60wZX4hE4QzdXz3IUrX3nQRc5GRXLdn8rmitl1OHB1uGChdMrIwE-vuSN_yf53ioglOrIjMoJa58CwAfNtaP-NzoAoKwVBWr5o2H3WQuZhxe2HArg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
هلدینگ‌خلیج‌فارس و بانک شهر پاداش ویژه و میلیارد برای بازیکنان دو تیم درصورت پیروزی در شهراورد حساس و حیاتی پیش‌رو تعیین کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/28767" target="_blank">📅 23:47 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28766">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUBBZqfgmkrj7bq8q77vOWd9WaCLnfJfoEhUuCE-03DhBgjBw7KAN87f7nJeoJSkSMCZe2dwrQYmVkyEz_gX_Br5sZUajq-ITH6wngsRsGYcXUPM_N9dwWiS52oiePCb6mNi23J4l73U1guNg9Deo4OUVB3gaRxRzJRY802PB9f_uMS5w6jBnIJ6jCq14sQnSXzYMwTncuf2_YFQxkU5Nrd31L7FR7XSjfKeyqUfk2Bk70XTgXV8pQjFibozkRVFniDw3KpvGgmsZLEFNch3B3REfgcgm0ffv6bbm8WCDoZ44G5oZaKabLDzKGdbpjS3RU9_-7RQHWcBN64rpo2zsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
گل‌ های دیدار دیدنی و فوق العاده امشب دو تیم منچستریونایتد
🆚
ایپسویچ درهفته دوم لیگ‌جزیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28766" target="_blank">📅 23:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28765">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trbb7fVyemBtRJDZsHi-cTw-Tv-VI9XyQHfuAKJqIvuzVu1TPqbBGG1mHqdilJ_OlbDvYOjOXDnXw50gMZhg4GJuQazBJHd1FxTiaEGd322Wrj8KAAorEFo2rFAPiQHzsti_6xkVNC5LzUjDfURgZ63rdXHcBJKy3dJtx8vJtIhIMX7F5UG667gIfgqJVmNx7mGAdIoH1mZMQnoJpYXgdTls98ppGs1zMxBl1fcVd-MP5_Ai8XKFgsE1vW_Qqaz92qasYun6XWNV3xegJv_xPLUziksTSgOciWii2DIGSDWuT40RhbZRz00rXwLQANAJt18dEPgYMpI4_mcHdDCeaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ امیر عابدزاده دروازه‌بان33ساله سابق تیم‌ملی به نزدیکان‌ خود در تراکتور گفته درصورتیکه جواد نکونام سرمربی پرشورها از او بخواهد حاضره درصورت‌جدایی‌علیرضا بیرانوند راهی تراکتور شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/28765" target="_blank">📅 23:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28764">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m78J6fpNmrqozWGlsBH3jKjR0mzq5Kc7BLJyU3sQ5FRtxkprqpYx--o5cG-6UJHv8OuXPnCZSBr8SM4MAufs9kqdWhzGMoUSujcWOkxY0l-kSifs2smSP3KsvslzOQHVrnWEHCl7LLTqMQW4mcmq4XUQ2ZKTf1CwjJFt9e-d3txGE8m990utI8UxdI_rJhe08xOZtipM3aE8vj11KARvaESxV6-anCDK5sTuQRDtmkOuQE1K4XjCRvKxNLjm01dE5DKYEZwH0p2d-jvreGN7ipBOeSNCFMgeIX0DQ9U-59UZkyI_hoC1DzCsnDHby25T4CVRTkdwR2D-1KOMhliS8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ به احتمال فراوان موعود بنیادی فر هم بعنوان داور اتاق VAR شهراورد انتخاب میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28764" target="_blank">📅 23:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28763">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/881c007350.mp4?token=J2bIGL6sWqQVMtBYz7BVYayd5XElGpKyLki8aTkNMmKoOL-D5ues7SbBMyE2ybTV10atQb51tUpTYOVFEXwwpLtshTDhK-lQyDKfG7RyWy2xoA4s5wkYDpdY8-xCBzraikvBBLxTthDZYGm8tMfTBUKrMIlK_OmdqSGMdKfRPGL9ZhG83XBS6-3mnX79nwaZbq5DvPRGmNZdypFjUYes1NHjmToYAn5b8ayZpa78UsEHaEaKn6uoK2yTvzBmIbPds9ypLtzY9EQcBPm5yFY9z0wchgeRz4MpgJCa7onQiVdq3QecdGzU-q2yq-SyXulJGyG1sccYZy3frD5ezH6efA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/881c007350.mp4?token=J2bIGL6sWqQVMtBYz7BVYayd5XElGpKyLki8aTkNMmKoOL-D5ues7SbBMyE2ybTV10atQb51tUpTYOVFEXwwpLtshTDhK-lQyDKfG7RyWy2xoA4s5wkYDpdY8-xCBzraikvBBLxTthDZYGm8tMfTBUKrMIlK_OmdqSGMdKfRPGL9ZhG83XBS6-3mnX79nwaZbq5DvPRGmNZdypFjUYes1NHjmToYAn5b8ayZpa78UsEHaEaKn6uoK2yTvzBmIbPds9ypLtzY9EQcBPm5yFY9z0wchgeRz4MpgJCa7onQiVdq3QecdGzU-q2yq-SyXulJGyG1sccYZy3frD5ezH6efA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
گلزنی‌دوباره اللهیار صیادمنش برای لخ پوزنان این بار در بازی امشب این تیم مقابل تیم کلاکسویک
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/28763" target="_blank">📅 22:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28762">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eujIFV14RC6dhEMJhbjndxTTr8aOB0agIv9pJ_OelkrS3dmiBzTORI-zEZuqWMBUmOI83lE8SePGDABWRjPKvhMkRA5l0eynpt4Q1bIbuY4pR0sZoh9LTsDYKXOx-f7ExzFn2DdLPEajTdG6bQJhlPzPES9Fi36WlZEjWZA_T1dNPhmTDqoULkeOQHQ0zCqPDZDgYR0tom5lt13xKcav3mFt90ykwPj3w-WYfTo4OZTJgDIeKK86zbLBnE2M8jz1UgK1nabJmGsHxb6a50v5k3hv7q1WlBu3R97Zey50yQBT2DhQejP443LVWSUnwmShNZOWkcIWv1d8MBkeru1z0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
درفاصله سه روز تا شهرآورد؛ کوپال ناظمی اصلی‌ ترین‌ گزینه قضاوت تقابل حساس و مهم یازده شهریور ماه استقلال
🆚
پرسپولیس است و اگراتفاق خاصی‌رخ‌ندهد ناظمی این دیدار روسوت خواهد زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/28762" target="_blank">📅 22:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28761">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pct5RBzlmjZ-owN6G8vUsInCqYrcFhpPbYS-2E-_qM1xq3ltKzYci3Bat_Y0PFA2ApqawkXsFNVA2kv52xWBbrQu1BCSwYaj2GfF__XGzbiJdW_Zvrp4_KqtBdYjQ0R43FLcMg0s0hMnUQ--LbOkNwUtEJtiDyM3IataXjyVqSJBKlmcmnt8tBDXIOqwg4Kvxt0W3_3F8aQd6zEL8vw6vgPRqjo50NfC-T9dcBaZhmlEp-ufebbzIC5y3dEYLGhzFVjTHvt6_HcZNcblAXi96JCwjiuyMPAZ3b8FvyJSd2VBr5zj4sPTbfiTrJtLE9ftMcGD8cAG_eTOSvbOwlht4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باموافقت‌سرمربی پرسپولیس؛ پوریا شهرآبادی، دانیال ایری و پوریا لطیفی‌فر، سه بازیکن جوان تیم پرسپولیس، به اردوی تیم ملی امید اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/28761" target="_blank">📅 22:11 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28760">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53b5db2489.mp4?token=bcI2XbdjfXB3oTLexdYzg2te5ka1AeY-hHWXm5GdbxtHv2GymP80UuCPs5VMq4LvG4pJpwv692f4IL83vr5poy4TixQXIhUx5a7UuQGvjz6mYZvE1B9zXsDMg60IEncAc-eBhg1BpnofqODB-9RsVlObuVNjYo240iobCIV8y0lNQjt-UgDS68f5BbS9dZ5D8ajSs-A8aMpixHUZvJbUNVRnM4-OO-XilXDM-HQ_24PEQEFXALkOV8o8M4b65pXLE-jCFft1sUVeUvlU8DKNcgeV8kFulGhnzXbbEmUVLxcqnqodWwBdByVegqViPqwFRcFEANOsqCUaq2UWZaj9NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53b5db2489.mp4?token=bcI2XbdjfXB3oTLexdYzg2te5ka1AeY-hHWXm5GdbxtHv2GymP80UuCPs5VMq4LvG4pJpwv692f4IL83vr5poy4TixQXIhUx5a7UuQGvjz6mYZvE1B9zXsDMg60IEncAc-eBhg1BpnofqODB-9RsVlObuVNjYo240iobCIV8y0lNQjt-UgDS68f5BbS9dZ5D8ajSs-A8aMpixHUZvJbUNVRnM4-OO-XilXDM-HQ_24PEQEFXALkOV8o8M4b65pXLE-jCFft1sUVeUvlU8DKNcgeV8kFulGhnzXbbEmUVLxcqnqodWwBdByVegqViPqwFRcFEANOsqCUaq2UWZaj9NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔵
هواداران چلسی یه ویدیو دو دیقه از عملکرد سانچز در فصل اخیر لیگ‌جزیره ساختن فقط آهنگش رو از ثانیه ۳۰ به بعد گوش بدیم. این چه سمی بود:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/28760" target="_blank">📅 22:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28759">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYptZ0um4aPQQH4SqRwvLMUkfVfcq9fbsrDVYk0Hsf21QWizu2cPjgWlEVdcRF6I23a1EuFE93eLfZBLXkhRaHLbxRK2FswnLhcV7fAGI5E8va6wnnnSgDd4NrOgAkF9ereVIq2Y2N_PNWr4dbFZEdKuwDomfq1uCgc1OXoSiNYvZ1j-hV47GuaekjNx6PLhcWI2Qqs8c2DwRJcWFS5tRdkCpNGF_wBpwgK9Iw7-jIwzrRw5vY2Ax2ZiCiA_3W1w169b4gldbJ6VATmvbD0s_zOn_bHpbSboncdlKd1fykrGVejHjhqVxrs-1Ke8aZceNMOhDFJT_1vS7V7XTh7ctg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
گل‌های دیدار امشب دو تیم رئال مادرید - مالاگا درهفته‌سوم‌لالیگا؛درخشش فوق العاده جود بلینگهام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/28759" target="_blank">📅 21:44 · 08 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
