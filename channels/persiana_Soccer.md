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
<img src="https://cdn4.telesco.pe/file/nOW0vlctd2TQ96OKwa3NFmsFNoQvrBhAoEosFhnUPjxNPHlrEbzkD87PA1G38ZQzVAwAb5JssDcuSFOGvzu8W-NTnbBut4RiUAr12uA6zT5nzySNxV2MucoB-x6z07O3RQpAc0xYV03DRyjsSsWFkOXrac_i3IwypK85XjQ2OEP3HNL1m5ISFVypP-_dLIIcWWDsmxzfMn_WFXrzRJlGhZk3SgxrdISQncaOl4XWtmDF9FiRtstsNiexwUI-xkqCnfIUI4OAf-ffSy91wLCd9EcjozgeUTaITERZ0s4oqPzibfmth0FSBgwaWrvh0UNJMHUx5Bzd7bbgIx8VUGsHig.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 478K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaaa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-20 20:39:24</div>
<hr>

<div class="tg-post" id="msg-31443">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JSQuRCgfOpfxfvYC6eKnZyDZwtU89S3p1Rcp1y4OoXgL90n_3MGnWq-Km3I8ytlZdr2iZVhGTclY-jhDaopU4B9WiujNddgrgUF52s_GlKpq8h8lrn-MicQYRkPvkTY7TuHXkAVZBrQO34GZvcEXGBRWS7pJbS4cSyVrwU8svJ3XSZy2ixydf5buSdHt2-evh9UjHJwsklY4s4Tgz-PAEW9jUFcNUAscwJ5FeyQQcqgFObgBJiMagw3dejTOZHDsC-UO-Ggs3qLa3ecW9L3XjBcHHZwx-DpgaJjcS0XjAgw9d9k65zG3AAByU438DTpV3SgzzuuVP7sd_pPLOqv0Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ‌نخبگان‌آسیا؛ ترکیب استقلال برای دیدار مقابل الغرافه قطر؛ ساعت 21:45 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/persiana_Soccer/31443" target="_blank">📅 20:34 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31442">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKT3gDt7XMgM9PWaR7lQKva6g-EVspmJzivMY6z1SlxajfB8rXGw2NJbJVvc3O9BcDlgJBf8762tVefynJoWlSmUGl6DGJB1p66CZn1-dC8yKsGR4WlFI9-adE2ZZ80aYefoquhqeb90mbs2RSZ0oisCJ5lPVr6FXa3zsQcXyc6JRywCvwLanUEecgwsxQZQxyUe_3kjHunTeXTkdOtqDdfQg98g10CjTtXUdyLy9Y2plWVFSt0oeJv3rCO2diGR6CsALUoxK2H_U8zScezJ1sCuBqYQtytvhzQ0UZ-3K557PaVMfLlZlnx0O0bE3kv_Jad8MhzdUTugzd9QpJ8n2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌پرشیانا؛ یاسر آسانی ستاره آلبانیایی‌استقلال دیدار روزدوشنبه مقابل تیم الغرافه قطر رو از دست داد. این بازیکن ممکن‌ست با کاروان این تیم به قطر برود اما قطعا بازی نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/31442" target="_blank">📅 20:18 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31441">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9509bbb5ca.mp4?token=GUdh9KMgRupDYYm0NOm3mmveci69B8Yv3P3rwIQhNlAN6COAmWBVDDgpPpNFH1dBvuINYYZgifA4jolbvPVZZ7Ird1uj_f5Rc6EAYBaaClQ7KIBVRjrIjh3h2eAUiTnLbGofzA12SqDc2LdIZE53UetBjAA9oGO2OW9B0NM2stEp5ZFoOu4cLoAdsLU-YZVs5wk485qopYlIpbZdyFHzQczY-sJHhovXhKJp6bmk0e7vaUJTTTg5i5N_dAmbIq8zw3LzVQQkbDD90uaw9qYlSi7KNhQnF8eETmYdDytdSSMXakMUQs37SPTYpjLxaRs_YhwAPclQdOFFM6UvG-GrmIFCaw5UCT-G-ALGyZw3wnLG-OQ5073hiWdtZmNg5Ncee8mRXCXkgQrMCjMrFBDlWVTswSrZTOjYfpDDfaFAPWvUh1q5vP-tzCl0vT2EQpmAJmUlVv0fMhgkPUK378_CcGf_PmvD4lT8WWMLEt9JizK6rLWqu9R06EOBJKKYi7XGfMnVuUw-US0HGCrOOWw7pg-6SsEiZWwh31W9CSlQymoNIINasQS8OBfdiGnvr9ylcxv0meg0_WGFe2kLGMZrkOiHjmaPCXFitMzZn4VNWPtvXlbRF6RHcccTwUX5NUZU4jvkPwTvka5vEJbJX2uzaWXOP9DuST9KxXJmYMKCbuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9509bbb5ca.mp4?token=GUdh9KMgRupDYYm0NOm3mmveci69B8Yv3P3rwIQhNlAN6COAmWBVDDgpPpNFH1dBvuINYYZgifA4jolbvPVZZ7Ird1uj_f5Rc6EAYBaaClQ7KIBVRjrIjh3h2eAUiTnLbGofzA12SqDc2LdIZE53UetBjAA9oGO2OW9B0NM2stEp5ZFoOu4cLoAdsLU-YZVs5wk485qopYlIpbZdyFHzQczY-sJHhovXhKJp6bmk0e7vaUJTTTg5i5N_dAmbIq8zw3LzVQQkbDD90uaw9qYlSi7KNhQnF8eETmYdDytdSSMXakMUQs37SPTYpjLxaRs_YhwAPclQdOFFM6UvG-GrmIFCaw5UCT-G-ALGyZw3wnLG-OQ5073hiWdtZmNg5Ncee8mRXCXkgQrMCjMrFBDlWVTswSrZTOjYfpDDfaFAPWvUh1q5vP-tzCl0vT2EQpmAJmUlVv0fMhgkPUK378_CcGf_PmvD4lT8WWMLEt9JizK6rLWqu9R06EOBJKKYi7XGfMnVuUw-US0HGCrOOWw7pg-6SsEiZWwh31W9CSlQymoNIINasQS8OBfdiGnvr9ylcxv0meg0_WGFe2kLGMZrkOiHjmaPCXFitMzZn4VNWPtvXlbRF6RHcccTwUX5NUZU4jvkPwTvka5vEJbJX2uzaWXOP9DuST9KxXJmYMKCbuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ریا بوز، استعداد ۱۹ ساله انگلیسی، پس از حضور درآکادمی‌ های چلسی و برایتون و تجربه اسپورتینگ، حالا بازیکن وستهمه و بصورت قرضی برای ساندرلند بازی میکنه. به‌ایشون‌لقب آلیشا لمن جدید داده شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/persiana_Soccer/31441" target="_blank">📅 20:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31439">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qu6rWytozL03MU7Ytxdi7PlJJJVjGU5_2l7FyFdrInm5fNp0AiaOfFx1EGxuliJs2UDYGiSiMdfNBthzzDP8D9s_6vS2Q6ngfnf7LmmykSYkVwdSXzfpFZE5LDmG3k4B9LZJRDj-2pSSUl2NOc-9rQqDlERZYBD6JJFUkqLfRnS6egJPuhvJ982cyJzPvdMMwkzbcFUDBHbGUCv6sbVDqoKpmetqD1l2QK51BVvd4Kbs8MoTZkjBm41qkOEW28TEVwD4MC2celKVUy--9bc-Nv57zMzy43fmx7XMVUU8KFh7ZVCjOQcA4y8PFzb9s66eclfvQ8r2oFz7fpFyyAHGLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
هفته دوم لیگ نخبگان آسیا؛ شماتیک ترکیب تراکتور برای دیدار با الشمال؛ ساعت 19:30؛ حبیبی نژاد بدلیل مصدومیت این بازی رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/31439" target="_blank">📅 19:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31438">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRo5Xx5xe57eeuEiGIMyVynZf_3EuYgwYoyP4iwebAWKJENEOHB4Jo9ZPN843f7GIL1n4nMtnkyyk76Vo-cxnjUVAyuNmitz49vLfFV2R5fH-Pyg6fi9b4DTSar1os-V8f8qJyfX152bGZ-LZuWhgzX52EUn2ehwYBwG77mO4W9LaHzi3ADpoa6kNhpwOnwdWtrm1RbtTHHpOwCf0z-5mggAZXAvPiucmkkqQurLkDNG8ISH5pdsIsbOcXZETNDaScP8HIlu5RFe-j7l2IRfkiEkk1EDLBIX2yYIhJEaRJTOYiT2_M0W0oyvK1nZq0imqgUzu5rlz3wp863Plw590Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مقایسه‌عملکرد مهدی‌تارتار
🆚
وحید هاشمیان دوسرمربی فعلی و سابق‌پرسپولیس بعد از هفت بازی ابتدایی‌سرخپوشان درلیگ برتر: مهدی تارتار: 5 برد، 1 مساوی،1 شکست، 16 امتیاز؛ وحید هاشمیان: 1 برد، پنج مساوی، 1 باخت و کسب تنها 8 امتیاز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/persiana_Soccer/31438" target="_blank">📅 19:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31437">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_EvmqqMdFJotlZkrB9h-D4bunUdPFZ-9OZFDA_yB_WzR63-9QIcP64a2wXIcUQwdjSXuQJb7855RNvc5ArDSH83JSsXNjsbOark6GLzgUoQUotOQ8ptujDGqoycknaYtJ0DMKGF8cfn42VzaTWLuSJIPKWlVPVkLReo6r3mNkykmKsedQ112UI4iBkfTFka-19yNK_iJVZ0BdndGfjXibh8BoFnOqeuayZ1DegKvI7gkQHlbJ4yGHsibW85EDLkWnBZJoIyjsHkZVQMnyUlhnLli5xG_BpqqlO9EPWB5X3nJaIL7s719tJTYyCRM9Ua62noo7N7QC14AQRZE2sogg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام فدراسیون فوتبال اسپانیا؛ وینیسسوس جونیور ستاره برزیلی تیم رئال مادرید مسابقه سوم آبان‌ماه با بارسا رو بدلیل محرومیت از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/31437" target="_blank">📅 19:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31436">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HI-ZmQZYuvV5rp0ar1gmJKjHQdaOpGLYHHmtaVzzZh5APwWk_hxYfuH7Sc9zllFtWcsokq6Ii6C9BbwMjHgusqqWzlswmk41dKetzqVzMyC7CDv9SurDhwvARg798jSBX1S7JsFCNqDih4SKWtn3yfqsBnZnTd2MgWFpPEn8czSZjsj6oEn37toqpOqPEls0vQEpD8S47X1wNrjSd-Duc06uSL_7SopNCHs5VTSc8cBx3LjdImFSunP-oiPIYCOJ1WEAO68mUfMCvpFzmHb1yYYh7ehsOQPuIoccPLy0jYhVSjUTxDZEhciaTUMjr7zKYvjfXKpKV2_eS-QBUDFeDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
مقایسه از هزینه‌ای که باشگاه بارسلونا برای جذب پدری کرد بابقیه‌باشگاه‌هاکه برای جذب بازیکن هم پستی پدری هزینه‌کرده. پدری درحال‌حاضر یکی از بهترین و آماده ترین هافبک فوتبال جهانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/persiana_Soccer/31436" target="_blank">📅 19:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31435">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvIMRJAJ2EcD58WILNHa83OpmQOv6kyBO4i49E3GLpNjVdFJ9nH99dtuHI8Jw0jMp315BMXMSWXP6u8enuqnkfSv6xHq51BAguwZ0a1NS2f50GghTFbRGO5HmOYJ_9jbJD2btXCbes2zG82YFsfQ5T_bvRx0uU1riVoTgimz_zaiMDW4oHSKWoRPbPIUABBhNSTg-GAsLdLTwbxHJCryMTs2GAyV4nH3yUKoc08GGJOHA91Px38jEk6yU_s7k8JYnJjPjBvC3G4moms7zaLqBda1bv1gpRiatzwPzTnBJxpDcFTLmcaZV-whZ73aQTcko4s5PESjr0aj6PWnqA2gbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
G20
🅰
🛒
ورود به سایت
👇
✅
https://ikruyxysd.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/31435" target="_blank">📅 19:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31434">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGoqYELd2Vf3UwIT1VWX887ZK7Ex04gauMKDyOP-mpEqImUw0C6-SKL6kkOoRxA4gAZU4NQjDF2gXbvHpMZwXFsuzMpjieXX1Ey3lesXuWj2iwYNXNHvc-E77T3w8jFZ0OYqJqBIt7NhYpyW5tDdKEqlJbWPbnt04XqiRlQt9KQj_UR6oqnRiMDmlruCW5ZDJsibonaB2XY4NDiR945k99i-WcJps2mRT_PnqBzvlfSbGr3U_t39mcFnljgUPaC0Mo81w4yDFEEA7lu7Q9iQolkCCKtpyjKjzezurRTXMesUdroLjFDqr2aBq0aevmFComf_pvy7Ek8nwVqaLkNq7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇧🇪
باشگاه رئال‌مادرید بزودی قرارداد تیبو کورتوا رو تاپایان‌فصل2028 تمدید خواهدکرد. تمام توافقات بین دوطرف برسر جزئیات قرارداد انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/31434" target="_blank">📅 18:51 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31433">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d320f9626a.mp4?token=DGLY3gISK_Ak9_VnOMnnhvGHpGVLUdNF8iUWk4nxaTA1Y45RSqR2ufy7xZRdvv44AakGIzvNqWb96L4J4qGQgHxKtxbdFdP9BjQkMoHxya0O1BwkeNdPaWUxKNMjCt1T69_XMbbwwWyvjQey27wNifZNlRffvBMwbnnAkRFG90uCaMd6sAgoofc7U5A22_W8oLwp3XjLhntwifPATyD283Yey__i_fg721wy03V5hS8NpNEwTJMkH5i70ufmZ-86wmHIQtKYDDZoBVY0Idv4ckMiZo2BmryI_xtB98nX9sBBPHIAItTdPZJZ8xmBZC7JIXk85SNG0UCey3r2gLUO9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d320f9626a.mp4?token=DGLY3gISK_Ak9_VnOMnnhvGHpGVLUdNF8iUWk4nxaTA1Y45RSqR2ufy7xZRdvv44AakGIzvNqWb96L4J4qGQgHxKtxbdFdP9BjQkMoHxya0O1BwkeNdPaWUxKNMjCt1T69_XMbbwwWyvjQey27wNifZNlRffvBMwbnnAkRFG90uCaMd6sAgoofc7U5A22_W8oLwp3XjLhntwifPATyD283Yey__i_fg721wy03V5hS8NpNEwTJMkH5i70ufmZ-86wmHIQtKYDDZoBVY0Idv4ckMiZo2BmryI_xtB98nX9sBBPHIAItTdPZJZ8xmBZC7JIXk85SNG0UCey3r2gLUO9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادت بدش روترک‌نکرد!
جواد نکونام سرمربی تراکتور:
شرایط به‌گونه‌ای‌است که همه چیز به سود الشمال است. چالش امروز ما مقابل الشمال شرایط خیلی سختی است که برای ما به وجود آورده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/31433" target="_blank">📅 18:36 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31432">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjE3-8v4jLSSRj9p_UZDIv0BIBuFjDISOGJpBWO3vH_bxwutfQsRwrULgs6bvSe92p8NVQ1lubTOzdKOWdsS9Ml_D1tlyyQpWywAREj92qAIJilSxha5_R8rYoz8qTxGAV41yUm3YijeRhJBLWahVmyckuBeCWAvqWnHzP0gEejSxdAnVMfteHhI164dfl7nIn-7VArVz8QZdZeA--2nj4nl3NB1Hm52RigHJ-t80odHoR9aHEl_CriQjzFhT_oAfVMCqh2PfOM-6MS922BHPjbtJm9_VWQISiDgAtkxgRc4ZvY4HJPCHjOv5zIkF3YnhvBybIeKmoFitX3DIX8xiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
هفته دوم لیگ نخبگان آسیا؛ شماتیک ترکیب تراکتور برای دیدار با الشمال؛ ساعت 19:30؛ حبیبی نژاد بدلیل مصدومیت این بازی رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/31432" target="_blank">📅 18:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31431">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YF9LDJA_PwG0mLucvMMAY_PNM6zWsr5dCy-sx8tyDuhk3Ye4TVOSEik2mwAJ5RHEt-KlUg2ui5ja0t-IUbbAh1qjqKZPjKb64wCxbvA4fgeGMesvLQn_4Y3re1-8p4rZ9PV7gnxdJ46gAWvQQzQpFjdL0OINys7st8RpSTiezhN2uDsi-slxL4EhrkzGVoTK1qB6887IZ0XlGcA6mTS5ShZPi4a2GOTNSYQZF6UrUkki5TYjKZlv-33UgKPhgnDL0AKnDugNWK2HTAsVIcHYTjJ_bwebLivZqEdjxs_bBGGceYgixg9b5dnc0KQAu35x8LkB097u4qiU-jKRpsCtow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افزایش قد عجیب پسر رونالدو!
کریس جونیور درحالی‌که فقط ۱۶ سالشه، قدش به حدود ۱۹۰ سانتی‌ متر رسیده و حالا ازپدرش کریس‌رونالدو باقد حدود ۱۸۷ سانتی‌مترم بلندتره! جالب اینجاست که با توجه به‌سنش، هنوز صفحه رشد قدیش بسته نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/31431" target="_blank">📅 18:09 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31430">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlXSRqyHQY-5eiQQUmAxqWGxhR8u8LeCG2Z1QwvFOMbPsJQvAZ4GslUG8fcwvsr4do6a9JdY1P357qP8Ig8_KT79nGGsDBkRBQnSmSLz4DEv1aR4LDCPbAfwhDeTuxh3pc-Qc_yMOnkAEA7Iq_NBLh59ywlwlXfXAz_1I8w0kgjkiO80axtzm5LBTkLOq1_Njgm6-kAzDZI9sK5W3unnuVBA5qem3NuDGC6pUBMY-3zKeOT8mHn2t_23K2TGa63o2m-E7XojHVXgCX5lsMfND_xglkPL5HtiZPw1VTZqFUDajPMKnAuElFxebCpfaAF2O8Ah9Dqq-e_x9QlhZYJZdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریس‌رونالدو: اگه‌کسی‌مسی، پله یا مارادونا رو ترجیح می‌ده، این سلیقه شخصیشه. بهش احترام میذارم. اما این که بگید کریستیانو یک بازیکن کامل نیست، یک دروغه. من کامل‌ترین بازیکن تاریخم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/31430" target="_blank">📅 17:42 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31429">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l95OVfu00xEQKK0I1jcV85wR_6x3QcxGQlhPM7aXQRAWSqO7j0QDSmh378Y_uyAx1QJ3hkcVzAVF9GwrdHLbd60dOnpL8b2tAKA5VtbZNirxXq_bmn7AqlQ5N-w85yQ6HkAoQzXDeMuAzXcYhN_PSJBK0QjMF54w-tCrf76TzHkqFyKJf_iomxx9RI6hv5ObiSNzfzQJvYnwFi6y2K6vyKQHUy-7KL8cZFW0MaqQQFJjM2hBU7LgLT52Q3_9JC8aat4nAYjR2B6kor56OvOP_YQFC6fNtGnhYMQ40_bk38F2rLDh3m8XuswyIN8ggLY-WcR3NOxTElGkL9j9y45Nvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخواست‌پزشکی‌علیرضابیرانونددروازه‌بان سابق پرسپولیس و تراکتور ازسوی‌سازمان نظام وظیفه رد شد و از اول آبان ماه اعزام پادگان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/31429" target="_blank">📅 17:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31428">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SjmQQMi0X28dOYBvMqiTW7p8oBrtjVJfQ6sXihWvqaHVIuUF4TmozYjkt08nh6z30CSWlYwhGV0QIaBZNxXb4z6cx-gVCDVMJxVcm4I2s6tOFo5gktq-zCeRf_IwF5H03BOYqfptn0XNKewIPcTd86b_5hiww0Tnr13Q6YfRBXrTn11lt8rkHx9dASencUh9JmjBTRA00D6wByacI6EXVYYABFjVseLLrKriU5T9WzXJFCCsxpTJoenyuOmmgcasiYvaTFkIbniCnwvE4kPKvPbmFsljH80mB-YNLjNp03Hbpfer1vJS80oTI4Rz8iZrAuB3aVG11DRli-CyPQ0_uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ سهراب بختیاری زاده سرمربی تیم استقلال در تماس بامدیریت باشگاه درخواست جذب همزمان یوسف مزرعه و یادگار رستمی دو ستاره 21 ساله فولاد خوزستان و فجرسپاسی رو داشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/31428" target="_blank">📅 16:22 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31427">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tdma2PV5QLjwdVlFt1m6NuMsmX8JJOgwcyfbYBbTPkC39mFBPA-g9nagylLYStY3G0gCFsnWRgd5iXwccbXavd__vqnwExA2LwWN0vqflWuvcWt03YqC5RoJ5zjsH4kEiaJlyqaCQclEM9-F8JvK6438Krb4pPB_I5F2p_0e7_gHQDB2kImC7Ll-3gg-mam_qiPk6Lq-ckkl1FsCK9ocOPG3rypUqe0ZfZQ56QIseETNCK1UHuz-eGu6Q2EAdD394uXwrPdOqm0zyf8a-aCF7-q9wBCeao5Ebd9QdspSwj2tedrhmVPTdgCqXFGwFwYKrlsLcOPVAExX46-zdE7prg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
#تکمیلی؛ کازویوشی میورا ۵۹ ساله قراردادش را با باشگاه فوکوشیما تمدید کرد‌. میورا فوتبال حرفه ای خودش را ۴۱ سال قبل و از سال ۱۹۸۶ شروع کرده و در فوریه ۲۰۲۷ میورا ۶۰ ساله خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/31427" target="_blank">📅 15:12 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31426">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‼️
ویدیو کامل قسمت سوم فان 360 با امیر مهدی ژوله با بالاترین کیفیت؛ عالی بود حتما ببینید تا آخر.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/31426" target="_blank">📅 14:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31425">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcseGrpeM7RMC3ZVURV9CNNr-3VpJS62wXW4T6gwHO2Tf_7BThQVxkr8iGVaRamnyF01moFaxMRiwG7_4qfmzv7rgOQgkN7nk4wgK1aQC7p6viJEtOgb2h_RmlV6cAb9k8FS_L_CzDNg1w4GdT0Txau-AtgCMjtUa-eIc_5Vd72Om3xocCWYavS2v1CvKQnJBAO3k-g3He_HH58QXneKhpPQu6QA2I3Oyb5WiNe2_Nk4uvnIQ2GSOpSc3xtC6NcdPe3iv-TXC-AeytbZX1cpNbcIq8Ic-U-023fJ_DVUNmpWsZs2jpJpct5Hwc359UMEBztkuHnDAwc1F6FGhdiOhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به دلیل جنگ اخیر دو کشور عربستان و یمن و شلیک و برخورد چندموشک به‌فرودگاه های عربستان احتمال‌گرفتن‌میزبانی جام ملت های آسیا از عربستان وبرگزاری این مسابقه در یک کشور دیگه وجود داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/31425" target="_blank">📅 14:14 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31424">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVnJoiJyUQ2dRCe5QQhfIuqkrAHYoBLQNuaffhgGhZ-drsWSUjkL7O5-9NQRbajp0ZHA1dvKPlkbuwASgF00wPOhZxQluKAVDi2A5y5NdkmQBLyy3KOCXy19t0h9FggGgQ2HpPY4yuA6LNmA1y33lD26MR8LVoR8zbzEDMdNAzom5CF_VZr45TY3OAU2KEeCiTYALvQU6zZVvuORdGLcVpq2uMCLFl2sluePmQeMOPr-LJWaCVR3GLlEtEvAi5eGxOlzRfVHB5FoENuWEUsn-uvyzY1-UYbTnJ82y8rgcLj8b7zeKGKZISfY3NB511RxpWgNrVblsVgqQ7rf7ccxfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
مهدی طارمی مهاجم 34 ساله تیم الوصل در اقدامی خیر خواهانه 8 زندانی در تهران رو آزاد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/31424" target="_blank">📅 13:57 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31423">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bb0f80f69.mp4?token=MGoqtfa_kYR5LwRw-HiCh452khS5pQ1e9Yvn2PUeFYIs7Bz89CY2nUlO_3Muwaw0tyXKhZNcP0SeSWHU6KjqIsW5Lwfq4gmZ-roDBdhZZFYkJctqh-s42e4HAiG7OzufvWceLUwwqSRaEi4Q5KOTGoun8LoQ3NgnaMxAzoB5TzGw_HncKmhkcPBZKvtcywi7yrsql1qrJN0Abh_IOj2ZlJ98HxM4FT4gNxTOthQl4te474GJ6K4jVuwQhM2iVrZy5K0T3sq0Wsnro-Q8m_EsL8Ryu_sPJ98ejqQaiSknLQyTgylTEOok7MfmDo6EVPcxAXJriXREcXX_QY819Mxp1IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bb0f80f69.mp4?token=MGoqtfa_kYR5LwRw-HiCh452khS5pQ1e9Yvn2PUeFYIs7Bz89CY2nUlO_3Muwaw0tyXKhZNcP0SeSWHU6KjqIsW5Lwfq4gmZ-roDBdhZZFYkJctqh-s42e4HAiG7OzufvWceLUwwqSRaEi4Q5KOTGoun8LoQ3NgnaMxAzoB5TzGw_HncKmhkcPBZKvtcywi7yrsql1qrJN0Abh_IOj2ZlJ98HxM4FT4gNxTOthQl4te474GJ6K4jVuwQhM2iVrZy5K0T3sq0Wsnro-Q8m_EsL8Ryu_sPJ98ejqQaiSknLQyTgylTEOok7MfmDo6EVPcxAXJriXREcXX_QY819Mxp1IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعدادی از گل بخودی‌های تاریخ لیگ برتر؛ از گل بخودی‌های عجیب و غریب محسن ایران نژاد تا گل بخودی مدافع ذوبی‌ها در فصل جدید رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/31423" target="_blank">📅 13:43 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31422">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCmmPO_SMa8WJJn-POWqNbx1-dXrldA83_Sn8322Sy2BS22yEuyajvPf34J59d67kdcOucew17bwVXmBOUZOByhuFfDkytoPRXbYGHF36aqxM5rgS9uTYKWeTQTdkpJpGeqh8KPXcjk6CxXQ7bHFyWW5tTexNN2TOhJJYrfPpJ8fBvLiMR-WvuZ8jfg31xApQqaLz2x3Z3fK1Io0PF7vquCZWSUWgrGZ5H9VlZm7XzoC9QNuVYaMB2k28rQlCgk-VnfyVoPBFJCBqql1PxmsmNp3TLISQsMR9pAGJyn1Vvck-XyEwI6nxvn2uhfxw3y-FRlQoUtfMTFI64Hd-E3NRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#تکمیلی؛ عملکرد درخشان کریس رونالدو و لیونل مسی در بازی‌های این هفته تیم‌هاشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/31422" target="_blank">📅 13:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31421">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqJBpz_GBLjniZhZFfYjxZ0jwehFSSXWLKOrxF9T_9jEMs17j-LrTxgmx0UA5ujTqyU9M9FidjyaPoF8gi4gUCG254XmNp0SH9HTcghYB1PoTvDezO2Q4NwEPoUnX8cdYe0VfPuHbT9wzu0h_Jbwd7r5QobB9vEevhTW68BnYzRsx7RAtYzgkU34EmxwfBz6cuWpgHNnvWPMhkwsLWT1_08VS-CB1_FH5u4nTt0cq-XM4c1xkG8sitF2MOi0QeyINEGui2qYAPU6igk4kEZpL5XrtoIZlnXIpid9_xoCKH8g6lwT1MiVfRJAu3za71BX1cwSiuBfKjJOdN8ASz_kMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریس‌رونالدو: اگه‌کسی‌مسی، پله یا مارادونا رو ترجیح می‌ده، این سلیقه شخصیشه. بهش احترام میذارم. اما این که بگید کریستیانو یک بازیکن کامل نیست، یک دروغه. من کامل‌ترین بازیکن تاریخم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/31421" target="_blank">📅 13:11 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31420">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjMitMqdxwfJj-aJVnCnPYsyR-BsTdIm6i477_QPwrg7nsp-0tqKxulLO9jcsVQdl5svOS1Au8BOf5jd24gW3UqmHdOipwcU-BiDviHPPP6rZ30GUDP89LKpxJAbjuSfKULu5VVVcoVyKMscBFM54QYkmsjpDcmQ2BPrIjEgI5rp1XvUs86t6Q1XEw6WmZFN0XPw4v2bIn1u3vv4Y-rusoOBxPdcLyHFq9RQe_CETeBtxybyzfhj8LUh3JvOmXP1wE-WaiCDjOJDFR_f67TeoKa0nVsqm5VV3D9-LBziZX07den-TaBMxBWoFaMtXyft-vFiL844rjoZYjlzwbB9RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چهار افتخار بزرگ لیونل‌مسی که از سال 2021 استارت خورد. مسی حتی‌قبل‌ترشم از بازی‌های ملی خدافظی کرده بود اما به یک باره ورق برگشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/31420" target="_blank">📅 12:39 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31419">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUkuffn-qgY5zLADj0PYQTAoVbz-g9Vvchlg7o2BDBcmL3WkXhmbl_03x44P4lSs07tmsYia4GoSzBzD2o_oC7jcaVhxb45Ll--l22GwVxxoi0FxlrX5kP370jWu638FwTEUIJ4ySTMNcPxZLHzWohTbz474_1Cyq-WD0W7GovI0DbMD5zO7Een-vfBOOxCXlmBYR8Oxn7J6HY776uk2p8C74loe4LPNmqTGAbv43a9Gm-2yxxTEHVTq0tHApdHCJMe9v_DY-_rLm93G9UwjsEARc9EBVjIRJy_xoeNU8jmlv7PftYhx26IuGPpWF6mR_9Qi75FC-HGsGpyMYSt_wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛طبق‌شنیده‌های‌رسانه‌های پرشیانا؛ علیرضا بیرانوند ساعتی‌دیگر باحضور درسازمان لیگ قراردادش رو با باشگاه تراکتور فسخ خواهد کرد و راهی سربازی خواهد شد. او از اول آبان سربازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/31419" target="_blank">📅 12:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31418">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D92YBmf111vFYl2xhzfmKne82vsHcgjHE3EQbOYJfEJTNRnPYKm6DfKXBqUA04L0oGQMY4_SEVf8npPfrxvj8DXySmhDh3TZm2PmbdPP5iJsRXvrJ1lLXeQA9xEcLn9238Jjcq3Y9NQm4zk5g_CDPFWi-wCmeR-ZdRY_8CQ1qq8YalmnxjtqdPQdxBqT3TBa9mMhCZTw_MChQ2DGSj-BZGvKoj3XpLgz69bPwoSiiJlt2wUPZetAkRucuWkVsx7IsvYpnWcdcHOyoBT5xC4bfvolU0SUbh_IPaDOhqJVWYlWlv9Fj_jVBSc8WkNqccQYu7wMb9pAgsmEH8ydWgqSdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ تا به‌امروز اوستون اورونوف، سید پیام نیازمند و محمد حسین کنعانی زادگان بازیکنانی هستند که موافقت‌خود را برای تمدید قرارداد خود با باشگاه پرسپولیس به مدت دو فصل اعلام کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/31418" target="_blank">📅 11:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31417">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJf0hfTE0ZvZkn2Igcf_35A2JLmKDR4yFyDMm82dv2cz1zmUq8ipQPswMDLBWKf68hGXla3iwUGVPVkFmlMcQ4MMHLTPUuNQEIiucgsuynXw1k9tTFdQTTR7j8AxMkS5op-qidmQxWsP5XCePmLfSs41pT3SKdctyuZPJI-4gdJqF1So2VpVC4qGLKOBYn8Xscok2U-T5P7c9hvr9ZSY2JdNt_PyNU2x_Sqd6ty-MyfKqaxEC_-XSFar3JjWKQf0HRFhcUBw54jpGtBNSa9yJzn_KoBWabIF_UvFrTh_EpDR6VhpHWpGGbsPEH55tbdqj-VhAE3nwb9gYpPZcYw7Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
علیرضابیرانوند خطاب به‌شجاع خلیل زاده: هیچ نیازی به فالوکردن بازیکنان‌تراکتور ندارم. من به تراکتور نمیومدم این‌تیم‌عمرا قهرمان لیگ برتر میشد. بعداز خدمت‌سربازی به تیمی خواهم‌رفت که قهرمان خواهد شد. ثابت میکنم هرجاباشم جام خواهم آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/31417" target="_blank">📅 10:42 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31416">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZqURutYO-1eVYGRdWmCrrbJKv4yHgWXut7nCmZmHY2k01V969VWWuCNNYw5_Rwlwldn2p6_4hvTNXb4CA38kKHqp_7dUqfImid-RHQUsddvuk1cFw3ZdSJ7Zm4nrZ6gjx3K39L9C0x9p21VyK39csuP-__FE1rkT2TCvgChgPSUtG6WrTXUBHCVmF5v64z080Un-Jhv4F53gtjpVidAZPYbHUCEPes_siBX3pOw8qOu2tVskKqV6SaMAkwA1H4BkpRj5XcnUngl5zzEfn2kl1eHwQn5RLmoG-si0wvaD_O_yduTAk980Uqesn4irGXkFZ3eD0zNe0eAOpBFENxHfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌پرشیانا؛وکیل‌علیرضا بیرانوند که رابطه نزدیکی با علی‌تاجرنیا داره در تلاشه که قبل ازرفتن علیرضابیرانوند بخدمت سربازی تمام توافقات لازم رو برای پیوستن بیرو به جمع آبی‌ها انجام بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/31416" target="_blank">📅 10:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31415">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uC1rJvtNO_uXc4jNkRHzMLWWBdslAXmlDMT5NIlzP3e001gTcnVWXKuHyeZQe8E1nJsGI29f12gQC401XzQa8MxXP1wK6l8bnUppo5L9H8ODIi8xQTxJ1605mGdeAqPSIx4rjMZKI3RWvdqKZmUs8g0FrST_auxEyMNNpvC6_hLkdz1KO2lJa5EynhoYerJexZ0JQTkc1SmkMUG_K0qFji4a0S8-0VWXxRmXTVDYnv5Pg_DMsfd9C7Sv0ZwkpgjnoYa0VDJpyBDuoTeQ5vnz8i5lw_548_Trs99y4Nxz3XJGThhQYI2Da-BQxuaez-7yHQvSMbU3qvxCBl0QBaymUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد فوق العاده جی‌جی گابریل ستاره 15 منچستریونایتد درفصل‌گذشته:23 مسابقه، 23 گل زده، 5 پاس گل، میانگین نمره 8.6 از فوتموب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/31415" target="_blank">📅 10:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31414">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGBHh0GyYxDWVW4KTtcNVcbK6u3KnEZuTujBQ6tY6wxHSmPtAztQYV7TDfw9hBGYTaFvAHrY3vlnO2-3Bnrz6UyiiqZQglhT7Vf6B8ue8Jwk7N8jpk9NMWK-gLrcuLrPIWHQ3Ge2UTnNH-Kh6SvjA4oc22jpopu71EvyrCa0KSsaCO8cZtHQqbb5gRScGBZMpw0AQ_kXwYH8VdH9mNSM7BRbMAKh6t8cdIocP_LUfH3NcqHXftGMLbPs5sVxSUt_EaC8-37FobcffFzsPTYhy6H5u2SefCohwtec2LfotzR800x4hAHf-SxRBP6oJm3r-WU1WcW4QH4l3Cjj64neIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
الغرافه  - استقلال
🌎
ساعت ۲۱:۴۵
⚽️
تراکتور  - الشمال
🌎
ساعت ۱۹:۳۰
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:
🅰
r20
🔗
https://ikruyxysd.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/31414" target="_blank">📅 10:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31413">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8f6d230ef.mp4?token=Ou5zaAACWohb7UgyMFEfamCf_JW7WT5jlLBXZ5GdcfvOFE_xSPVco-HwX3wtxnppsjOueSPYqhZ-Qb1GmPNZtjJtyz_TFWo6KI0ShStxMKr7gK_z11hXGYJZDzHuBd900fLUKvKoztOFXk7WJEzCFyQR5MyTCjFJ0ZixZyEziwWMHvUIUOz8KASVQsGKc74Mc5jNv-mF15XexQETjH28BMQ69Q1TRWLBbUrMoQkGuKEKbyniCWvhKKbh8QO_OfwjAo8_ZXMAwjBZarWg82Pyo4DSIY6Yk6tQ8yAYUqICnPtyDm7yngOIk63ket2CAKa_vFDgbMNH6_VE09gg26Qx1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8f6d230ef.mp4?token=Ou5zaAACWohb7UgyMFEfamCf_JW7WT5jlLBXZ5GdcfvOFE_xSPVco-HwX3wtxnppsjOueSPYqhZ-Qb1GmPNZtjJtyz_TFWo6KI0ShStxMKr7gK_z11hXGYJZDzHuBd900fLUKvKoztOFXk7WJEzCFyQR5MyTCjFJ0ZixZyEziwWMHvUIUOz8KASVQsGKc74Mc5jNv-mF15XexQETjH28BMQ69Q1TRWLBbUrMoQkGuKEKbyniCWvhKKbh8QO_OfwjAo8_ZXMAwjBZarWg82Pyo4DSIY6Yk6tQ8yAYUqICnPtyDm7yngOIk63ket2CAKa_vFDgbMNH6_VE09gg26Qx1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
مجری‌جنجالی تلویزیون خودش از ایران رفت! زینب‌ابوطالبی‌مجری‌جنجالی«مملکت مال حزب‌اللهی‌ هاست هرکس نمیخواهد جمع کند از ایران برود»، از کشوررفت. ازفردامنتظر عکس‌های نودی ازاو باشید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/31413" target="_blank">📅 10:03 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31412">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f5075dda3.mp4?token=q0XF5hylwtt8sMVr-LC-Vnm7Rl6RZ7UUWK6d5M9IlGyfoTsBjT3R_VEs-BeenUo-Haot3PbsFN5DN8jZkm5Bh_E66vRXZm8Oqo92y_lC-IOuwhPCZzPkL-3jOIyEH6w6qkB0ICoCNfV49LnAeeth7BUHYN0OpEybQdtwLgJz6IvB7EuqeKuZdf2af0nEnENGk9AFc8rYQqr9UeqptT8zoYeGPANhztqIYq9I6rIr27GluFfPjUcImxxjirfi-VR8dN9NxIQOPW9dAXw1U7x0z3K4ZoqcrEg3RzOfYRI9XhR6Oq3w-jumcXj6S5rLiVYlL1eMbMfjsFu3IEDAUaLbTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5075dda3.mp4?token=q0XF5hylwtt8sMVr-LC-Vnm7Rl6RZ7UUWK6d5M9IlGyfoTsBjT3R_VEs-BeenUo-Haot3PbsFN5DN8jZkm5Bh_E66vRXZm8Oqo92y_lC-IOuwhPCZzPkL-3jOIyEH6w6qkB0ICoCNfV49LnAeeth7BUHYN0OpEybQdtwLgJz6IvB7EuqeKuZdf2af0nEnENGk9AFc8rYQqr9UeqptT8zoYeGPANhztqIYq9I6rIr27GluFfPjUcImxxjirfi-VR8dN9NxIQOPW9dAXw1U7x0z3K4ZoqcrEg3RzOfYRI9XhR6Oq3w-jumcXj6S5rLiVYlL1eMbMfjsFu3IEDAUaLbTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نادر قاضی‌پور نماینده سابق مجلس:
تراکتور پر طرفدارترین‌تیم‌جهانه.بالاتراز رئال مادرید و بارسلونا. درترکیه، ترکمنستان و آلمان همه طرفدار تراکتورند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/31412" target="_blank">📅 09:39 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31410">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7024843df.mp4?token=Y69sKwxXLXogoIfmf8mSrRD407KBUXS_i-Strvvtydt5ElJj4UzjFycqdeSDa9LU3f8FGz2FZvt_9pmiXdhrEqstja4bVP6LqsPpaOZh2Rs35xbygzFUUlHAyidOKXMb864mR65sS77Yhn-cJQ4BhW5AaC7u1YYCaK2ESJo-e_xE2FsJhB4lKQEUmGddI6fXAsbs3jJirfHIX-opm_F6e8w39oCkCyjeXDvbgLcMQdv50dTOfHKVyn0PuyrIhG55NbJwfR1ANDoweH8hocshYWECC8szPhWQWaUTFio5EOlS_n6_OBAj6xc6cz480cQVGSFH8JXvMTwIYMcT9WjUoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7024843df.mp4?token=Y69sKwxXLXogoIfmf8mSrRD407KBUXS_i-Strvvtydt5ElJj4UzjFycqdeSDa9LU3f8FGz2FZvt_9pmiXdhrEqstja4bVP6LqsPpaOZh2Rs35xbygzFUUlHAyidOKXMb864mR65sS77Yhn-cJQ4BhW5AaC7u1YYCaK2ESJo-e_xE2FsJhB4lKQEUmGddI6fXAsbs3jJirfHIX-opm_F6e8w39oCkCyjeXDvbgLcMQdv50dTOfHKVyn0PuyrIhG55NbJwfR1ANDoweH8hocshYWECC8szPhWQWaUTFio5EOlS_n6_OBAj6xc6cz480cQVGSFH8JXvMTwIYMcT9WjUoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ذوق‌زدگی امیرحسین‌قیاسی از حضور رضا گلزار در «دور امیر»؛ پز دادن به دوستانش با حضور گلزار!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/31410" target="_blank">📅 08:53 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31409">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tpg4TpP4RebNcbp_6aCvKiT6EXh0g_IC3foA3dzNH--nBR5A1xyixiZZCa6GUOgof8N1XrAJz5UWRcAZ8SV6idzzBKHInongu2pTSsQUCH7AkgUvxGxkSPU3oLnOyafiWmxubtvcWkf5tdxafkZo-vBpz4mKd0RUl7gm3eUPrrbOliJtep_ljNIQ8PYaQm6jQhoTn-Ac6YKMXVnhpUOp11SL-7MYm6MWGQv5vu-dSm9f16Ar-3H03qqHb8aAdL4V_J8Hgejf_MkTOhYKIQFK_1PwAex7rul0s_5fdEukG-JQ-CSLZSmiZQh6CnxsaRDnURKWG1KhifMTEasP1ACsVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
گلشیفته فراهانی با جان سینا فیلم بازی کردهه؛ چه لبیم گرفت ازش. الان دارم میفهمم چرا حکومت داره تلاش میکنه گلشیفته رو به ایران برگردونده.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/31409" target="_blank">📅 08:37 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31407">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwLaTl7YlBDAMPX6nd3nUxXJ34i5UiusjARTaqEEJbm-CBKHytpqG2iCVKd7_LBM-1F7m2WDQ36IYTo4ZmVmJTpRQCgn38EV3L3HFKewR14qHE7HBEa2nacNDNjK1jvPegehJnn1m2Jj6w3S8_AbMfyzT50IlkE-bF4cF5BB8Kp9I7zwrUQabZj7omgOHhfea210PNrlZhHe8DvkJzM0LCBrlXfJnD285zVCY4oiN3fX2BRJsQD_1RXrwoEkE5P8juclFbjIGPKyxVKWL4Cgssuop5Cn8QA71rkPEYVJ4gNysbERPDyu8-ppRKhWDCqp3wdi21SGFmdqURpUrN9-Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز
؛آغاز هفته‌دوم لیگ الیت با نبرد حساس شاگردان بختیاری‌زاده مقابل الغرافه
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/31407" target="_blank">📅 08:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31406">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjqKErL72PJpmgrh5-RbMPNkRaC1Hm-XScqftVmjmfvMUpBpVcynUhUiq0iiGJSG1Fwnc_GU0rWJAdJtxtwA-5QW5bykZMhLjLsyx59KAJPXkpiGk_n3IGPIUUYLvjPhnClayhSkmp-AAoZx1Vg1FLhiHB8WRaOKGS7zQWBnel9trlc9k-rFct0TRfz5MmEljCbGjnn-cxxuAxkkYd3Zy_TIi-jdtUHsxFkVGwIpLyRUSwy2PjgOi6Hazpkqt38-FisGADDXtrFSAQj-feOQqUUVSWE9A0GLwNt8uvSHLg4X29P6URssMlWc_2St_yWOPW0dBhRvV1VK6zzqqy5LuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌دیروز؛
از پیروزی بزرگ شاگردان مارسکا در آنفیلد تا توقف روسونری برابر ساسولو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/31406" target="_blank">📅 08:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31405">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">📹
هایلایتی از عملکرد درخشان محمد خدا بنده لو هافبک پرسپولیس در بازی این هفته با صنعت نفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/31405" target="_blank">📅 01:18 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31404">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromایران تحصیلات | irantahsilat</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxWbByn2ZIyhcBJPO1xKTDeWQnRYa-dBkMXtWshwNt3OLbaNoFyp14WLdoW-T6734hYJ4uWu71NIbvijTXMkJw41K5sIsqR78x9cdYgPtonBhhiMV0TLLoYlWNavQg1cOXcXHXIeOC2nPpiOVXT4arvFR4gmYpjPuIzaMxSPiO0JeQrfZhdQBJkPj4fMSbJs8IBYc-yn9xrvxDm4i_mQM2RSEIT-xx7AlP_wtmzOG3naSSWbI_PqzwsRkolmnQuWMZsJ3SNY3pTM_qFVwu3KG1kbO3HSR6qxfP-A5EGtd7FN0cXePmJ1UYkUwL4a_FEqDeq1Ms07exi0_whlYnerCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
مدارک رسمی «دیپلم تا دکتری» فقط در ۱۰ روز!
✅
قانونی، قابل استعلام، کاملاً غیرحضوری
✅
مناسب مهاجرت، استخدام، ارتقاء شغلی و ادامه تحصیل
✅
ترجمه رسمی و تأیید توسط تمامی نهادها
☎️
مشاوره تخصصی و رایگان
:
https://t.me/irantahsilat_support
📺
عضویت در کانال
:
https://t.me/+1I9Ex4YFtcZkOTY0
https://t.me/+1I9Ex4YFtcZkOTY0</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/31404" target="_blank">📅 01:18 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31403">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLZJd6XdL9kg4q59MW_zdh7u3Q44cA0IckDOzHYSdpjVVqChci1Of0xB9836zwBgrIVqG25adIoIAsaBGoMJTZrdtH7eN-NnKc_VfhFywh5Q0FYw149j5oP6QciQwMPRzaLKn06FTC1TsSzTpICTccUJSKr5ykslSARF0yhG6u0xlL2paNsyzntnkmhvaG5Xsnc4lCw_HdwWk4Qd9TnWOY70vFJKZpppRP-rclrxRAZEwhJNByDAFTtvPN9Kh4PBJYjDibgAwFB0QXCtsmXYVNwAcWJclCkJIrWhYYLYo08Plr7oiiiKMM_Ny_eoKWTKa21qxAZ4PzxFEUyCLSZ8tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هوادار دوست داشتنی و ناناز باشگاه روبین کازان روسیه‌هستن‌که‌اخیرا گفته از بین بازیکنان ایرانی به سبک بازی سردار آزمون علاقمنده.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/31403" target="_blank">📅 00:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31402">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKRGySIUXqpxsA-Rr0qtF25_JnTgdlC1_dUz4hTeFGgPyhDsFUMr8Wc8iJqjOjY6yWf-iWEjBWq6q22PuSvuQlBvOAmjEJdWcmPHn7hX7dcqfhjgNREMT5CkJJ0q-N3QQ0k4SgU5PYJ6M080oR7RLH5oMi8lUKbFfeZLIF9EB35P4E2dvuJoX3wjQZsD9gdvgJZUspfEyEEVtaOF5WiVVpa3oUUxBKLJ6aJD2BatkEZAtT8IoblVh6t5rSqo06OKWXZX3H9OsYVmz7auwb_ZXJX3ewHeSVrCNJG7mcQdDSTZvqPh2lmk05_MAwpuGPQ8LtbIhySsJeZ_FcrvX1icBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق اخبار جدید دریافتی رسانه پرشیانا؛ یاسر آسانی تنها دیدار با الغرافه رو از دست خواهد کرد و به دیدار هفته آینده مقابل گل گهر خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/31402" target="_blank">📅 00:21 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31401">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2jSMrssQEkDAaajCYdH_Xb0_uha5ohhymsqq6rSX7fZxXcLfXdvEJ8hcZBoqU4zJvuqrSv449vcLk26IIZC4jrbZRrxt3K-wGbytE4_NTxTfdH53y-OIklrb30-a5gwOpSwBgGDkpXQ8LTjv5rIomvpVTVWPRLQARe6pLTLge9nUNQgi6DP2Nup4mAlFbQp6HZfI19CobSXZeM5k9BB8mStOYGloDQ_LuzLIWyl6HzKxPt4Jn_yeuKd8HzunOZ3HO9YE-AK7_ZZUR0O5jJLS1g8G3no5tg62ERCzI-slriSlqyUexK30aG9pd-U7J5fT84qcQ8JbQI-X396ZEC-2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز؛ دوئل حساس لیورپول vs من‌سیتی در استادیوم آنفیلد بدون حضور پپ   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/31401" target="_blank">📅 00:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31400">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMD2ELsQrElNHmGNYOuZyN2O7sWSUs22QjVBYPb74iefjUzL-klQbURE1Uaj5qZlD90n7aigDxO04EZ0WbQXykJXvuQWJeeI8g_qlsSZ4_S-46RpCswCf-b56UPN8IO6_-eBVzfkvwVzwrGalOKI5ng58iEAikqPh0p6ZG21-2DcPv4ZuS9XP11ue5FZAABj3uIYBRGDNQ4UZghYw_hYDKfFy1OFiKHYTy7z4rPBI8nUBrr4UMI_Tp1yMoBgapb4KaYTBQgwAG-CK9ybXTvF0mf-nixqCHR4iz2IvKSo7Nw1Qzd2lfcOazWQZKt8rd5QGLQvxBcWZaPvo7m1AhlOUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه تعداد جام‌ های لواندوفسکی
🆚
زلاتان ابراهیموویچ درکل دوران حرفه‌ایشون؛ زلاتان فوق ستاره‌ای‌که‌هیچوقت‌نتونست قهرمانی UCL بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/31400" target="_blank">📅 00:06 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31399">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GpaTJBk6AdkqYU9TV6VrcZRVEi2oJw6PYjAP9mLXmL5pZFvLZ8ueD1V9NOwZrKcygJjosMOvxvmUzvcke6i5Dap3FEoM1Y8BYGv1msXhl4qHDS53IN18s68JTcH6pQ1JIx_y35jGvBGTGZBsJdSY10_dsfVmL-0_8izo2Wm8yNm-RcPs9VZ8xkUL7SIT6BGv2X5E7WBG3t8tRB98FCqz33Sw6qAs6m8gPAOwRFmV6hPB6WeL-gloXeJetpB6ditaDM7XSx2RyOpjURGdlv-HRZV_PGq4w7o-kj_bmWe6TY7kIZpHA8tUzbvQJ1YLjLqwSnmHIAQG0u8VU9eu6n9uYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دستور واتساپی‌شجاع‌خلیل‌زاده کاپیتان تراکتور به‌بازیکنان‌تیم‌تراکتور:همتون علیرضا بیرانوند رو آنفالو کنید. او دیگر جایگاهی در تراکتور ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/31399" target="_blank">📅 23:58 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31398">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z42NQjZHNNvT0Bo85k_NQxMUJ6wbjrJdOAGt6esK4zXP2-rHecgNxxXYTvdBzkHSw5jimNKXMtr8Nu3VLbjLOuZyJc1_6UAO0REHR9fhiYY4ZtMImQnQGCFSpMGivf2WHglUL4XeHV5dlWnBG-ulBJbzNpMDzgdo8KmJTTgw2beceNLdiGyuCia-wNpMBGAYycNk03FPtnSBCOBsJVwMlHvySWxz7Nmf96yueEGZ25sSvcObTvSJv4AcjkHVwK7q5RajyhRIPihlxyICW8Jrz8Osvau0zWoKzUho6n3W3DD8CcAT8jFsHUpZp4QzVmp43HczGb30r3BM60SoRVw5rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
شباهت‌پشم‌ریزون گل دیدنی ارلینگ هالند در بازی امشب به لیورپول به گل تماشایی او به آرسنال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/31398" target="_blank">📅 23:42 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31397">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWakdxpxWccPSCVn_uy2o4Gb4etorr16eSAMkyj9lmLIcH5yBhGCxcl3qY7mVGHVbK0mZGnwjYqSVLPwBYjB761OyS-LDHaoAZFRqV-yTLp33yn1UY3o_NZXJem3aHogdZYTtvSPPSg7YrexIaGMXh9eOF5M9Umo2Mx8DIyH8zgOBzou0SK09oGJ5Pd4SgPjknceaakYxrrwkvVcGr9dgQaNwtqd44QvhO3qcnRKkUKD39-HpG9Xmhu-IGtp0gM9NJM8DGTr8z53kvpBC54NaNTsEwxOBROnRu5FLCZUmIFxtq5ccwN94-5Z7WUvfqkkBIkUO2JWP6bUae-msGj7-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
افت‌شدید ستاره‌فصل‌گذشته تیم استقلال؛ علیرضا کوشکی وینگر 26 ساله آبی‌ها آخرین بار در تاریخ 9 آبان 1404 مقابل آلومینیوم اراک موفق به گلزنی شد. حالا درصورتیکه که علیرضا کوشکی تا 9 آبان ماه موفق به گلزنی نشود دیگه‌یک‌سال کامل از آخرین گل او با پیراهن استقلال…</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/31397" target="_blank">📅 23:27 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31396">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAWTxXVyxHFpc4XgvzKonDkPP4BuKYXJwuvDhHOOahAo7CB4Zuff-nbGmOEKyJBhRkF2Kb3o8D6BjtsvmV5DWZr1A-PLjFU_YhTkMxuQkMpQ6uGoM1XPYwfcYVIohAvQO2l3g69O2j7KCroNXYhaWHKTUdbAdmEL1ICFaMt9zQmwvxhJX5_mD_gN2xkXTv-0eTiu92KyyFeJ765x8ZwFJF8p7zBo8v66g2oOGkZRhP8r0QtPfAVLIymP9Yy7FDecK5Z5cYVCF5jOwbXSTI24RaxVLOq-ABD9Nru0GcBE_IWR6_KoGF24DKmyuL-mOf4fmtnzjnJ4HqVs-CtIcvxDlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد رونالدو
🆚
مسی با پیراهن دو تیم النصر عربستان
🆚
اینترمیامی در رقابت‌های باشگاهی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/31396" target="_blank">📅 22:42 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31395">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/095e7b9659.mp4?token=Ib2fhooutmLTCqceP5oSmQ4MPBvrfBvEKhBr73gpAbGA0AaLAg0jviaojgfMWUBNIa-hY3W2EuAOIZrHgNcaMqpK-5csU-7tLFH9S6eAd1SUPkjFK8ZQxeGIAnScO6uQp7VdHUOY7h04IztWQatB5Of03gs5jAaoUj6FlGjhcwAxdKICNa6UBxi5ma9tQzyBk0AmpFuKnbgKZiu6oepAi2obiset3NC7QolSJ_Izcarhd9F2Wo2Au5_R2vJs3cN5gzUAbJx-PcoGSaxW12MNioTaVz0KmocTBNlZdIhmR6Ztoun1LBPjD7mEc-r5BBPKIqE72-mXB34Reehij5tqug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/095e7b9659.mp4?token=Ib2fhooutmLTCqceP5oSmQ4MPBvrfBvEKhBr73gpAbGA0AaLAg0jviaojgfMWUBNIa-hY3W2EuAOIZrHgNcaMqpK-5csU-7tLFH9S6eAd1SUPkjFK8ZQxeGIAnScO6uQp7VdHUOY7h04IztWQatB5Of03gs5jAaoUj6FlGjhcwAxdKICNa6UBxi5ma9tQzyBk0AmpFuKnbgKZiu6oepAi2obiset3NC7QolSJ_Izcarhd9F2Wo2Au5_R2vJs3cN5gzUAbJx-PcoGSaxW12MNioTaVz0KmocTBNlZdIhmR6Ztoun1LBPjD7mEc-r5BBPKIqE72-mXB34Reehij5tqug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برگاتون‌بریزه
؛ دانا جین وایلد ورزشکار ۶۱ ساله کانادایی، با ثبت یک رکورد جهانی در حرکت پلانک، نشان داد که سن مانعی برای دست یابی به قدرت و استقامت بالا نیست. او توانست حرکت پلانک را به مدت باورنکردنی ۵ ساعت حفظ‌کند و رکورد جهانی طولانی‌ترین پلانک زنان را به نام خود ثبت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/31395" target="_blank">📅 22:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31394">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTQWv4xdvnVU-OmJ3Pw7WNp-LYu-R1ChxZIphefTlQ1MAJ-39oDslf8R3Q2VRkTTk6kKuS1ueOlmyCKe2CoF7F-OtcZha-KMZXRd4nZ-Bx0ju8NXqjDw8uQZ_GbgNC69epweD4b76q0Dj16LuIkhCPsFLAMl8twdN1-otOg-H_NacN4OykRk7FumgwUoc5o9ydJ8NYYOUqzDBuQ1G9WNh_sRMARHNcO81ePVX89Na_eAFN68Pb7HGpbcEgn1O4LJQkitLjE7e4UsRM13RqoUTC9fsL6bBXV72IP88IhKZ5qm8P90jgZpBieMcEHPp2SzWk9HBtQj17EKyerVyZZg1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام رسانه‌های معتبر خارجی؛ وینیسیوس جونیور ستاره رئال مادرید بعداز چند ماه از دوست دخترش ویرجینیا جدا شد. بچسپ به فوتبالت مرد حسابی. پیر کردی رئالیارو از بس حرصشون دادی‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/31394" target="_blank">📅 22:02 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31393">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPjQUMw-mK5DVnG1WIvrdUGPIJJ4fsIfTeMjIPupO3vnkeZPyL-FwPV4v1t2pFhef4O-Mw_tXGPDN0fsbkCN7gMM3QZNi9tyX4_v1iyMq0v0pSPwQhASw6AXN0b9rstEi0fJgegNNRozkprTVfqCI2Qd3S3NZOiszmD0ekcu5qF9FP6WR3P6eWNrBCsA4HyTvBWfoS_bPnCKWCmv26atT1GwU_D6_G6zB8dqt-s1CiRzkEhG7JBMW0ppXJPmRhNh-tdA4fZwDEM4LWz69C0WYLL9GPoeI2-jjKiiVXToEIssDYPwcuAa7fRC6J0gjm0HTuGDvVvpgmf9X51-520dQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مجری‌جنجالی تلویزیون خودش از ایران رفت!
زینب‌ابوطالبی‌مجری‌جنجالی«مملکت مال حزب‌اللهی‌ هاست هرکس نمیخواهد جمع کند از ایران برود»، از کشوررفت. ازفردامنتظر عکس‌های نودی ازاو باشید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/31393" target="_blank">📅 21:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31392">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6abb5815e.mp4?token=BF4cltl3QipG6tgE2mpgLUXAdJCv180zB47im-CwZvJz3qEziR0j3GQxE60BDYHtUWnLxdB607VMXu0L8Y7jF3D0sHi7P5sAzJQ02ijI7Jyi_lvU1_9ljnJg1M2mPmxQ92uLbpV4NqV7gZtsHI90fks2GvczJ58hfcDQE37R_fm5KLx4ai5kpTy1EG2Zka_Ad7cUCokH5NpeSD9HtxvetdTRWAJdTfjTVYBor-whkvDua3T38wUHPrESZpFx2XHhJRKcEjZxyTlr8AeR9X3wYvdPj-O07MX1on7VT--EDkWhILTW9vsSQqZ4JBRznBP5D_CcIEu6YdlYZZq9IuqWoYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6abb5815e.mp4?token=BF4cltl3QipG6tgE2mpgLUXAdJCv180zB47im-CwZvJz3qEziR0j3GQxE60BDYHtUWnLxdB607VMXu0L8Y7jF3D0sHi7P5sAzJQ02ijI7Jyi_lvU1_9ljnJg1M2mPmxQ92uLbpV4NqV7gZtsHI90fks2GvczJ58hfcDQE37R_fm5KLx4ai5kpTy1EG2Zka_Ad7cUCokH5NpeSD9HtxvetdTRWAJdTfjTVYBor-whkvDua3T38wUHPrESZpFx2XHhJRKcEjZxyTlr8AeR9X3wYvdPj-O07MX1on7VT--EDkWhILTW9vsSQqZ4JBRznBP5D_CcIEu6YdlYZZq9IuqWoYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
در هفته ششم لیگ جزیره؛ شاگردان مارسکا در منچسترسیتی درشب‌درخشش رایان چرکی و گلزنی ارلینگ هالند سه بر صفر از سد لیورپول گذشت و با شش پیروزی پیاپی در صدر جدول قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/31392" target="_blank">📅 21:47 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31391">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BaXM4prpzXlUSrauGZsXxt3xFkgg0B2r9eE1emq6R8fKVvNbE8CdoVh9VO1QyaognBrZs6CsxYjO2N8zNlk4lst7zgoAC-3maSwi67B7uT_G7aAhin_q1cTLYYbWS9TI-nVos6YGipHwEkdhSjo2ayWDcsYyI-6ehkuCP6TfX8cf4HklgnaIWwu0qSm8LQjjl8wu_TyH6GbtolFFK1E-nojgDZlFdhvE8qugwnodVH6v6vy-vOi9ZlbuovSRd35TyFYKSgm1HQj24pJRibOygYmj55zr2vq6ksqgg33s5bdUM9or6fl662G62XllYNCW_tUhYKHrUbHiPCZfH9zIPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ جدایی محمد نوری از نفت آبادان؛ با اعلام باشگاه صنعت‌ نفت آبادان، محمد نوری پس از شکست مقابل تیم پرسپولیس از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/31391" target="_blank">📅 21:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31390">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUtU8e_vUx8SeNPNMamqIKcMmskC2QJFJR5lqszpZT0a2tQQbiQ8O5EaFZ337iBJP2IXHemejyvx1v48oZNb8S3cI3qrbW10cvSi8pALifhAp1NkpiVxm1Vd2o_OUPZYU9kp6gFM2uOgUld8RaBg53Xmeekoc0SY-3bLyMOoWUJhfB2We5KmRsOd8egxinymsYOFuDZdbRuFugV48IYzqIaKPGa-Byz0vKrMwPeJK9wacBOdffpxGPA_vQTah1UCUq1uuoGoPBaUsq51ZFYp8tLUOjflwSyvQem4QqpkrFv8-5GNESGbMe8v1uB7WbAC35Zgw371TUN4cjtaPqa9Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
متاسفانه‌دوست‌داشتنی‌ترین‌زوج تاریخ فوتبالم از هم جدا شدن و خانوم ویرجینیا باید فعلا تنهایی سه تا بچه قد و نیم‌قدشو بزرگ کنه تو ۲۷ سالگی.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/31390" target="_blank">📅 21:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31389">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKIthuhL9zQYsPjLxi6h5hg0f_Sy167Tx0bQSCINzfFLWsSy-JGYAZ7ukt73DNVu_5fvcAq32guU7eqUQsgx2KHbSikEpPF2q1mbGXeAVAuHisLHuvnJDeWJvq-DGraVU2jqF2ijqsgwwuGYyehQJHdod6s16Eyq2MPz--fSJqJaJfCokzfF0vcs3RwKXdfN2GjlLGLu2awOtfXVM3Wk-OBAqzT7wTpc1e8EHu2q6w1kvEzlyYyNNqLfOm8mj8VYnHpYsLIT3XvDXjyDX3IbcYol-njX-n3cIVrMJpJ0xJOYUReAHeKurQ6rNBOV-dTf409Apqk7M6HxAnw7m5DTJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
در هفته ششم لیگ جزیره؛ شاگردان مارسکا در منچسترسیتی درشب‌درخشش رایان چرکی و گلزنی ارلینگ هالند سه بر صفر از سد لیورپول گذشت و با شش پیروزی پیاپی در صدر جدول قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/31389" target="_blank">📅 21:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31388">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🟣
گل‌های دیدار امشب دو تیم منچستر یونایتد و تاتنهام در هفته ششم رقابت‌های لیگ‌جزیره انگلیس؛ مایکل‌کریک سرالکس‌جوان‌نشد و در آستانه اخراجه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/31388" target="_blank">📅 21:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31387">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNvLt9EJohl9U6JoQ1AEgLLl_UNYvPCFROxyxLxes7iK6Xr0AmKdb3HHZrpYm5CLLpc6wk0keVrD4P9hdeimTF1mZN_4K_qTrJyQkpZFMM66Ty18-Zj23d-LTQY_1cMbSasQy0rorwDO8WuXY_i4MOAwJexwY-NbtDRHiGyqvZd0pKe0AM0K2W63chcINKlJV_1ExDfBxEp67DCAldk-vebxnxl0e8PgN6O1980VIbyWLxcLBFTdupGwKBPj8M90trM7AJudkrzig3gpYys_TMezO5RMEVz4hmN2rag232obpcEzAKnCIrHsvFgquvlEqCYCvXL2oQgNdivIcwUbOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌پرشیانا؛وکیل‌علیرضا بیرانوند که رابطه نزدیکی با علی‌تاجرنیا داره در تلاشه که قبل ازرفتن علیرضابیرانوند بخدمت سربازی تمام توافقات لازم رو برای پیوستن بیرو به جمع آبی‌ها انجام بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/31387" target="_blank">📅 20:55 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31386">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10ee700462.mp4?token=Fp-PE-eMbwGHFf57XOGsF3Pi6832YXddWtIPFPFPmPItJmuDWrAZ-pihwsc1sC7ZW0mqzXyNae06L2j_y3HmtCgxiJa9UQjGscYiz33cEEIVEbozr7SkXhHh3o4udjiSJDYnSjpzIZO1yqYZCI6PGPjGlcQqwiuYZnTdzEyTjHYYywz2fz1YA4BmOUqHL2DkrQI6lc99_23KcukeqSZd1MF-JusMPB3bra2wvogVqd6sWNPI4GjCH2scFOvJp2fH4HcyCgHQA_FYcpXILQHFX4rqmPk-bnYiGmAGAnKMqkBGB_793mRaSuGOfk_8PfTQYk44kj-I2l8Wxznmck7C0wXvYeO05GWzCkKq5Nr8wdsouTnIk_c8cNU-S7mP8AlPXutgwwAJibgbAnXOqgi7BS7SbGAZMBc7EltNyG3takz_twPivMfXGcj4WBOaowXZQ2ZsyDBd5heo55xNkg_9viVC_iak9Ck5E2rBxx2ccTbY5zjbxPN3b5qT52j6X_bNm7HGg5vUk9tf5S8SSjpdhvTwIRhxAYJnSyTclAYgim8SeUk-Xl2y8kruyabdzh4qu2Umsk1muqp9huXuWls24FnDWlyyPhevKKEYildHB_YcAPrj5okgmsEwgjgoZF7r_7NxJWqXmW3SzXLCjy5HtP3Ty3mRHP4Hqi3dLAQpY1k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10ee700462.mp4?token=Fp-PE-eMbwGHFf57XOGsF3Pi6832YXddWtIPFPFPmPItJmuDWrAZ-pihwsc1sC7ZW0mqzXyNae06L2j_y3HmtCgxiJa9UQjGscYiz33cEEIVEbozr7SkXhHh3o4udjiSJDYnSjpzIZO1yqYZCI6PGPjGlcQqwiuYZnTdzEyTjHYYywz2fz1YA4BmOUqHL2DkrQI6lc99_23KcukeqSZd1MF-JusMPB3bra2wvogVqd6sWNPI4GjCH2scFOvJp2fH4HcyCgHQA_FYcpXILQHFX4rqmPk-bnYiGmAGAnKMqkBGB_793mRaSuGOfk_8PfTQYk44kj-I2l8Wxznmck7C0wXvYeO05GWzCkKq5Nr8wdsouTnIk_c8cNU-S7mP8AlPXutgwwAJibgbAnXOqgi7BS7SbGAZMBc7EltNyG3takz_twPivMfXGcj4WBOaowXZQ2ZsyDBd5heo55xNkg_9viVC_iak9Ck5E2rBxx2ccTbY5zjbxPN3b5qT52j6X_bNm7HGg5vUk9tf5S8SSjpdhvTwIRhxAYJnSyTclAYgim8SeUk-Xl2y8kruyabdzh4qu2Umsk1muqp9huXuWls24FnDWlyyPhevKKEYildHB_YcAPrj5okgmsEwgjgoZF7r_7NxJWqXmW3SzXLCjy5HtP3Ty3mRHP4Hqi3dLAQpY1k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
ویدیویی از آنالیز عملکرد پرسپولیسِ مهدی تارتار در بازی این هفته سرخ‌ها مقابل صنعت نفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/31386" target="_blank">📅 20:47 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31385">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T37H1pXeX7PLNqp6wwv2pK9yH5R4vXy93bwaYeaVNSs2YJMipb_UwJwDmu3l7cnEQkH3Frk9NJ-w7zoBmrYi80oYiTfKdYqACE19VNzPkypR6kKWqT4KsA29BxFMknRfFfiARbzdSQTxMobpUdEiAE1OhBCPYD45uxPBi01n38ZxD9BKmQFyL6pB0agpaAKIyOnrWU4PBHnOvAxEEKBMbiYQhRP-QbUaAbzpLpAi1c0KcCderc7J_yopZKlb9iPxVF3IGkEv-UT7VZGkPLPkNKASXLfyXPv_Su0iFZoraruOupG0sLJ6DY6cH9851SHlcZFqbPyt6cWe5pdsaVnF-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیکه سانسورشده از مصاحبه چند روزپیش رضا گلزار سوپر استار سینما و تلویریون با امیر قیاسی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/31385" target="_blank">📅 20:19 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31384">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nG-HSWdGzaeWpQcJXYZgrul87WZTLId0Im4Jh1Ogol6Xxq0r6to1eUqUwbxRhBKzEZ4MkSZIfhFJSYp_s0a0jRrDD_IKoKMtfgrbEe1suPj8GiheZhOfkjjQXEMoTCH6ErXS-IDCZ8SitODKhTgqLRm0Ju6toxhW9uyNVT-R3r0Phy75Km1g4xGt361Kt3oLQDM96keuox5STZSd-wMLeYvGPNcB_sH-sRT0Y3KaLOI9pizia9nLKtR6LXSgJQd1aM2Q7FE1CYNtIenXUVg-rEKbiPRGmMS5KAl_T5BI-y6cmZshT6qU3OLYC2p1SaMALfn8YlluJbSTYYgCBxljow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق اخبار جدید دریافتی رسانه پرشیانا؛ یاسر آسانی تنها دیدار با الغرافه رو از دست خواهد کرد و به دیدار هفته آینده مقابل گل گهر خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/31384" target="_blank">📅 20:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31383">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TuMGaT-F5gB8Rgvhu4GiqHTW2tz1NtpgJoFW3VF3uCWxd4vZg052I9MY7jxEUmg_zXUuwiNitiXpnVNSKAMnispuQSvdeyoeAJRIxk1weITNPpowE2OodvSqi-DHvijAVONDQGCdV4dOWSwlAm89O7HYj0mSshMMCqUjGmer2z_PMbCTyRPbb8kA5-l6JR3_rVa4d5Qflz-aal17sk1AguNJSqyjD7bvAQLjH85kcKYsDTGnfJ5N19ZmvOG0UBbg7ANa0tyy70q-8dgLgrdUdOi_NGYvAXv_Vuod7csDoV3YThFm0IpqCESAmC5dyZGFzpl_O3voo5K1hgpeA1Ccdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مقایسه‌عملکرد مهدی‌تارتار
🆚
وحید هاشمیان دوسرمربی فعلی و سابق‌پرسپولیس بعد از هفت بازی ابتدایی‌سرخپوشان درلیگ برتر: مهدی تارتار: 5 برد، 1 مساوی،1 شکست، 16 امتیاز؛ وحید هاشمیان: 1 برد، پنج مساوی، 1 باخت و کسب تنها 8 امتیاز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/31383" target="_blank">📅 20:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31381">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZ8llCuNpkTXDOS6apP6IPUlXF_B8_PPM670gkt17GN10BhNPCUmojXBoQWsEQabNmu6B4OBiNsFUSU03n50qEkFWepqqUVUHJsWT66GxL-s8y8NHi2X8q0-JXvELEyvPES_gYhq0jNb0lzKpJOMEW0TbgGYMd8Zv1Kw8Ws5U-WdHQBXyYX1OhOkU36_VyLKZdKyu8o-dKsDVHCKCqJl6kjfAZgLMnurA3D0GFAQy6uwZ-snh96Bj9hrWT-BJ5bf_7SsAUmAnS9-s0Vl2niRqRHtqez-V46XhWuoLTJJlrJeCE4w2jTciHwCk4f3XnlB5hxoF_KaEdi02b-hc64sSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ زهرا گونش ستاره تیم‌ والیبال واکیف‌ بانک ترکیه باز هم نامزد بهترین بازیکن ماه لیگ ترکیه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/31381" target="_blank">📅 19:32 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31380">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMdcZXDPGA0CPSRkyocY3JF-lbUlU5gQt5BWKHA6NHQfPE4hxyXIQXXpuWdDwcrDiMgaDRxgnaoou1zX_7j8e3i9Uhqa_QL19IXZvna30gOaBtvtjJEinh6v9_pazWrv3bGNJjE_1cGxPaoE8NxeDW0XGzzjUlRU88deW9tB28UZTuqzlQLtRZ9lDmi7Kl9i2kt_eQ7QzcdedLXIRX3Hl8WIcOjILQoGa9ziWp1a4_ALI8qr9X60U5D1zUOkVSh-_AGfOM6FUUErreRbQd79yfYJnxntI-l25ZnVYwqtqZ515mIZ_rnYviZ63kT9Ur4m1Uc4alKyNqGx0cSLI9PTTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
سریع‌ترین بازیکنان تاریخ فوتبال برای رسیدن به 100 گل در5لیگ‌معتبراروپا؛ CR7 همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/31380" target="_blank">📅 19:18 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31379">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cr60RHJGdxZvF_p1SkfXbSSQLeDTMDoS-t7rPZHKhgvCilaI_NyWBIPBSUbLQAZ8ssdGZTiMSr6bKxWPVw3im8tdJkbNs8aVQWXPk3DAgHLUPCShmXMHCTY-Y9Fk_SUramoEf5Or26Hrwpf3z0oIWv_5ZDVF3Z-z_ktvXmhNU9YylbAmIRfbxOewm9EB3CzJ7LRMHiuqeWErB6rdsTAYIcEFgzQhLTUGausA4YzFFezOpK3bxwZqoa46YHzhTp6fAL35c9nvbsAaliyyk9F0d6513BKJUn8o0XkQL5jvAsBh3YK8SJgsh9Key6QvWwGFhVtPyVgIlquKEkrEfLsZSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
خبرنگار تیم اینترمیلان هستن که افشاگری کرده وگفته مائورو ایکاردی زمانیکه در این تیم و با وندا در رابطه‌بود دوبار درخواست.رابطه جنسی با من داشته که هر دو بار دست رد به سینه او زدم.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/31379" target="_blank">📅 18:41 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31378">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/We6Epw_mDhRaqMzdXVM8MpAuRZQ9i6qK8ZsZuQSYYzS2kNDnUC2_CC-V0uSaZxcSQP3ySWI6fM0XvXevoKwIXFsiTUrEEceOOoTKFZx0NUKcpONSZbqSdD8G6fvy3ik3_5AZg9NBog9heQoDwjASWOVOgCR15fMxaxyalTpobrjhAu29k4tRz01pqcv4EZYwU_fIisCllbpnDtKEWqPnmAeykfnYZlXH1uKkPlxNiH0MP8F-nLCuLu0tYFgmDMZsUDFwVcCpMoKxmmU3ftKdqVOj-eVCBFpIf7ex7gd-Ds0sZNInMUkXbvb13dLr9gKQ3M5QBR9YHCtbDQ7APYtcWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیپ‌واستایل‌تمام"بگی"عیسی الکثیر مهاجم سابق پرسپولیس که تا آستانه یاغی شدن هم پیش رفت در اکران فیلم سینمایی ما که اخیر ساخته شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/31378" target="_blank">📅 18:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31377">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDsRDHydVkNm94YhvG-WawUwvM0YAMiEuW-gPC9e-XQ7A_3WOjHzhNF9u8jNmgG5D6uBu7c8ZQwSbo9BYelZ1_RGpDPuHiNwqgtxrI5AwRbgMznjvZ4aSVy182lm1Qubb3FEimIBDXRNYDkxzOLrrpgquPMnFhibW0z7mfPXDengm7wbqF3lAo5hY3TY3A41WCzzqEZ_lMRCWIZM7-E8WEJA9KlG58d-7M3T49KYUNxI7H43vw1mIB2UvLxgjf2Pppe4f8nLdkMsXMooqHzyz-uK-86x8_ZX1X-nAgHOO_sA_HQTyiQ_108KmJSdL8cuA7Y-q7uGbzZEv_ueZxpANg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درفوق‌العاده‌بودن رابرت لواندوفسکی همین بس که تعداد گل‌های ملی‌اش از تعداد گل های ملی کریم بنزما، لوئیزسوارز، نیمارجونیور و هری کین بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/31377" target="_blank">📅 18:09 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31376">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GRqg7GrO6r_kA94Wvx-Uymw52veHmVIRXzwaSW5V4GpNgOyokirSQkBLHaZuU92nDlKUv08KeL8irh9Eg4YZlF8SUHq97QivrIWSRL7gf8ziUHXfFK8NKNr0SSe-GYLLzKNAWj_udd7f18YczDMcBJdQyUT_lIex47E8izly9KzvnfKjJHAifWm2gQiXPTvXkUKS79nhnzi10YGDX3ztIe1XHRVbsQbhHd1EZZB75ucvpDXxUGJNDrtrUeCTmePNxYWHyCMv6u85ZyyNMXTGfYVwMT8kpMXvb-wcVNIvKIVESbJiRszp4H5fKGjiXWnESIWfusFECpnwFveYOry3OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌استقلال بشکل‌‌رسمی با کلارنس سیدورف مدیر ورزشی این باشگاه قطع همکاری کرد. سیدورف برای تنها یک فصل 250 هزار دلار از آبی‌ها گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/31376" target="_blank">📅 17:44 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31375">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tKbgRDOpn9vzcxjmfClQccWGKNUEfRz_wNbBkHLOx0A25vgQxk7ezL3Cdxn5P0x1ttyHKom3IVmVntS5-W4KgBxEzyqZQ4_qVSWKeo5f-KqWxhMgWR03nf2xaOXR2r_2fn-haJ9M49Mk4jcnpgKx3X-NsGkEqY-DEpIBA1aWcES_2EVvgujdie3VqDq04gM6nMCoL1fq7I8tgRcIyLHp0vIVAW2T62_Ys7Kr7-kcaArlZnHubIxmPZwGaA0CpQDH0hW2_yXjDr_k3vZuathVChIhb_Y1ZNBt1TR-aaDnuFGhdMYRxZcrVbKIcyBwd6nW-O6-MOw0gKlbJoOrpD7Dtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب تیم منتخب هفته‌هشتم رقابت‌های لیگ از نگاه‌سایت‌متریکا براساس بیشترین نمره در هر پست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/31375" target="_blank">📅 17:19 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31374">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4aSiVOOI4JHkVmtPaqMUJ3zJLHR05ptKtG09zWlJXckiKaweQgiEWZ7BJrJY3guG4jLzL_kqIeJWUlZLxEG3lPbCPFQoBbHAeFWarWTc6b_NCO6JGFXhPDZ08dm01A4IpFnpxDv1ktlnTnOWLntzXvQ-CFPpqwadvpeJXgHcCnz2jfZM8HurlyvDR6xP88WrvP08iYELZ2NpQ4KVxBmDgiJQf4VdOKc7w031LLio-z1cW9h0AUpUPT4oQpSfVLCuloAI7HYo4a_eKKqgFJyylhKjCcpbcTpvPMhAmACF0xnYW_weIn3QLtQ4Eu9_vwgCv0m4j5b9xexvbbhsWI9qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
در هفته ششم سری‌آ؛
تقابل شاگردان گاسپرینی و سسک فابرگاس در ایستگاه ششم برنده نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/31374" target="_blank">📅 16:07 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31373">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UV0QMLuGhDh3tBoBNn0J2p_vUSdN3n1n5pLDAnN_LS3US2ApPESyiCgE4vqP3uuqGrednzLfB1ViOMwVpmKTf9jaZ37sFcwGz1CtmqvqLf1tG1X5VdL0rdSpCj4XYdr-PXXRmkDcuX_9N1_5uSAkXdzdd0rY3TQwCUUpHQ2k3UC-ytvpFwZT4_GVH_79clrolVA5HSw9MivZedPF4KObWhHodo5gZdsV-9Vs_ZdMCjSCI_M73jiWf_QtFTeZzpjDQ0b2LJwsG9Y0s2Llg5BC8MUQqxsggWtv53oWBDMGyR15-jzlf8uaF4-3iFSkopK5hPywuSnbfckmmttjf6nXzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سهراب بختیاری زاده پیشنهاد حضور در کادرفنی استقلال رو به پژمان‌منتظری کاپیتان‌سابق‌آبی‌ها داده. منتظری گفته بزودی جواب این پیشنهاد رو میده.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/31373" target="_blank">📅 15:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31372">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPyR1ZVXvz9GDJyT6I_H-gn89K0IohmYrtkRiejP1z4TF-6EeCaMB1nU5CeWvSCeMitbEUHwVMauxia0ecwFCdsdXuQ_8cRsq-5X-mOVKNsdaDrQntJrhJHkiDzvH6D0CXsCQxIa6K4pbKqh-Dg3YHKxkGe23XbBSMsLnOe9OF180kdV38JQ7hR5Bx7-L782u5XQ-bgz0QqgPuhzaP4Ns4rsbOQ8utL2GfwdlrubBMnGAr8U5EzkxusInIC3IZxgdtEUvyUAfMyngu17GzvxkcXHMCkq7PnHNYieJ0sciR5pgcPcuiwrUk6fp56uoEJ1pq1SyzERWHDqz0AOgGCHLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روایت مؤدب‌ترین و باشخصیت ترین مرد تاریخ فوتبال ایران ازسفر۱۸ساعته کاروان تراکتور از تبریز به عمان به دلیل محاصره هوایی ایران: پنج بار فقط سگ ما رو گشته. اینجا هم فک کنم صف روغنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/31372" target="_blank">📅 15:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31371">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIPtYfmTjY0RPPeDeEVsGm2jNBf8zYGVdqrBeMUGpf8UEfKgEtn8EPZ6J6mdSl49wnKejc25cGEQwfWOx2BOrR91NUTvvNK_qLw2UQZit4UpryIaGAf2ircSL0bq6HAwRUgHiiAPXR6K_NWbc551QZSMeBQhjur23LzQ4nPKsU051-Z1cXWOgQpdwP7Dj6crYxQpgEYh9BYEizPr_7sZrMoFLUhQ9KyWfpYenkmTwN5y3UOX4e18L1eto5rGrXVtZ5SncaXgs2SXXjPLB261ed1NgRD-h2iM_hOex2_cZSt9F1RmWuGEFCtqBPCJBmXOMA6pkyevVhbqPIO43UaPMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ ضربه بزرگ فیفادی به تارتار؛ علاوه بر دانیال ایری،محمدحسین کنعانی زادگان و علی علیپور دو کاپیتان‌اول و دوم پرسپولیس به دلیل مصدومیت به احتمال‌زیاد بازی با صنعت‌نفت‌رو از دست میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/31371" target="_blank">📅 14:44 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31370">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f85d440852.mp4?token=jpjMdxJyzsLyFbMXqxj523R7w6fbnY7G6rv3S9lILBfXc4jtCtx3pRNxkEpldj_D_cqedjQNoOpr3P82YStHnHPmLm7SafWGZR7PHnv1AWt4yp4y8IfRXuKnyyQEevcTH9efh1EZ_ytwbye81wXxzQ4XfaYUf_VbbaN_gwMFHM-dgia-LP0tBlZNVXNZ40ZuwfDFecuzkmJxPja23rK6eNiOh9kXcPCAMMC48jIe4K6IPQ7dG4vrTCN0cgIYDCMdPhTHx6WU-IUNbR211pqC54_DM6D5wG9Z06ujG4RJ3k4vDIEEfdx8sFwnc1TopxYhV3EGIvjjzQt60rI4NtfGlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f85d440852.mp4?token=jpjMdxJyzsLyFbMXqxj523R7w6fbnY7G6rv3S9lILBfXc4jtCtx3pRNxkEpldj_D_cqedjQNoOpr3P82YStHnHPmLm7SafWGZR7PHnv1AWt4yp4y8IfRXuKnyyQEevcTH9efh1EZ_ytwbye81wXxzQ4XfaYUf_VbbaN_gwMFHM-dgia-LP0tBlZNVXNZ40ZuwfDFecuzkmJxPja23rK6eNiOh9kXcPCAMMC48jIe4K6IPQ7dG4vrTCN0cgIYDCMdPhTHx6WU-IUNbR211pqC54_DM6D5wG9Z06ujG4RJ3k4vDIEEfdx8sFwnc1TopxYhV3EGIvjjzQt60rI4NtfGlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
ویدیویی از پاس‌ های تماشایی پل پوگبا در مستطیل‌سبزکه‌منجر به گلزنی هم‌تیمی هاش میشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/31370" target="_blank">📅 14:40 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31369">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJg7ZeE0iHrGaz4N_m6zja5pfl-xrCeY6_R98yGnIdq8ORMBdq5lGaiUOLALjsreszi4xySULbzQj090H8Zj4VqsKXGX8NZ81lTuYz1cmz5YinDntkxUASRo60KsYQIh2-DxRDLsG1bZEeSo3-mUFTuBkXp8Ql-3BhZBjMR1vEe-mgWd3qwG55cEDKPhze8bMtAegr2pl8-A-89Z3AgjRIuxG93DiSncGGppjiEjd0yOKZvctBP3EC0mwiskWmCeIKTunxFb0-dEdVp5EXUxgH_bexTmg1a99h7c56URmPty-5lZLrhlE216jLoNTuCppMnHgieeAWh9uv-8d916BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌پرشیانا؛وکیل‌علیرضا بیرانوند که رابطه نزدیکی با علی‌تاجرنیا داره در تلاشه که قبل ازرفتن علیرضابیرانوند بخدمت سربازی تمام توافقات لازم رو برای پیوستن بیرو به جمع آبی‌ها انجام بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/31369" target="_blank">📅 14:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31368">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEci8GF_c6rj8HenVWBDKWgq2U2COUwL8oxxSQQzwhatQF7h2WH7rERG-ctT8Az18ZsNjvj7anjQOhbb4kt0EmENbFm0XYoUOiqSj3K5r0NcQ6ZG_D8Y_aEms6Oimt5KfR7XQIVlxiV_hwqiN03gR1XNf3kb6JfFf2dKW9G3qSs6Y1aQNqyLn3SrU1SAdFFv6EcQ8mZGn6yL7vbyQbFBVMy6i-4mAo6wbY0iepbIXqnHLW4lIaDUbNxNkLQPxWAN7_itHuOfQUvSzXm-IzehiDY-tzEVJy5rPsOyAh3FA01blMVv-R4yNzWauSwQigYInsOKSZ7nihYqm7zsp_Tvcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگار شبکه DAZN ایتالیا و از طرفداران تیم آث میلان که گفته روسونری با روبن آموریم به جایی نخواهد رسید و باید او رو از این تیم کنار بزارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/31368" target="_blank">📅 14:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31367">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmDddXsx-5Yau8QwfCMG0SAdl3akdcKqe8j-q8Lht8M6pkiqS9HqnWGltRhfxhzhUnZW67-qytixdNPfqYJAbM0XJ9euHLHkPwKLK7ndfh5pl0G3AWQ-_b7BPxpc08kqtWXOu9L6Mix_5d9B63mvW4Tbs1graCxha4abPPSz8rgW4_vdfHFkYSbyNxJO3XjXywCzhQkgqg6GSfJM2qlWd9DvaO4VDfWENxSeNQYW5fIwRt0cv91-g_V-RKFePfUpWWMfauZoR1U0V-dXTdsnemGG7i2WjgdaUscEE6ixMMiRV8JvalseHJ8A380eKk7LqmpO6kS5-z3GoO5J0WrfZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ساکت الهامی سرمربی پیکان قبل بازی با شمس آذر: من‌دیگه‌اون‌ادم‌سابق نیست و دیگه دست به زن ندارم. ساکت الهامی در بازی دیروز با شمس آذر:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/31367" target="_blank">📅 13:36 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31366">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOtCjDklcl4T1-L5mWZINqt24-vtW7Ao0yYF_iqJfQEoD9EEjzctkI3OypJblh6o_gEVbpR2R2W_bQPqfGBI51IayTowCPArGIKc_TAG0H5WlXY_01uXPUMr0lI9fy_1k3ACvxjbnZ39spGV9NcBxgmWH6_Fq5zKhFK5yoeN0QTs1RjLz3G2GWfj0K_7y3qIaaK1bJ1YRPVqDPJ-QfyYPogqJcJX8oxjJagXI-W1PPXizdf8dOAIbIiHAhg7t902ph9mJL-_t17cgYUDRwD9dlTUCSRxtMgqQJ6jQwMO6O3yUllkDJLsJZUktQByYWO7QYVp5_AZkKxEc8lLAGBuWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#تکمیلی؛ عملکرد درخشان کریس رونالدو و لیونل مسی در بازی‌های این هفته تیم‌هاشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/31366" target="_blank">📅 13:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31365">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9b16df533.mp4?token=PKns4tFXk6ceTosO6PRX5bckQo0oda-6tyHrWyA-baooEdh0MBYu8dG7KTaxBp1Gu3JE6F208gZhMvVz1cBkgsTvFSzdYMwnAzhqVAKHe8VtDFv5yKDGMWQsfrk_zHMnEZ--O_v6FkO1r5Hvj3LoDGJBWPe13wSoyC68gvV06HEu_V-vXh06068JLRCfwpiRZrgYzT6lQ4q-goiGp8hCE11g8NGPEHXbI2V4sc13c2kEdxnUmaFf1t0QquvhifHa6Ye8bpwhjWSwtOBKiiEci8a4D3dozBcab4Z0d3EEQJ_6FYGqvw6UBwYTxCWeIOFdotFFqwAEDxAS8Lirh_zwsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9b16df533.mp4?token=PKns4tFXk6ceTosO6PRX5bckQo0oda-6tyHrWyA-baooEdh0MBYu8dG7KTaxBp1Gu3JE6F208gZhMvVz1cBkgsTvFSzdYMwnAzhqVAKHe8VtDFv5yKDGMWQsfrk_zHMnEZ--O_v6FkO1r5Hvj3LoDGJBWPe13wSoyC68gvV06HEu_V-vXh06068JLRCfwpiRZrgYzT6lQ4q-goiGp8hCE11g8NGPEHXbI2V4sc13c2kEdxnUmaFf1t0QquvhifHa6Ye8bpwhjWSwtOBKiiEci8a4D3dozBcab4Z0d3EEQJ_6FYGqvw6UBwYTxCWeIOFdotFFqwAEDxAS8Lirh_zwsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ساکت‌الهامی‌سرمربی‌پیکان درپایان نیمه اول بازی باشمس‌آذر اینجوری رفت سمت حجت احمدی و یکی خوابوند زیرگوشش بابت اعتراض به کادرفنی حریف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/31365" target="_blank">📅 12:58 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31364">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b580b78a1.mp4?token=KWbKb9tfhJwMnG3f5C9QhZOD5hrpYRhPIVHrG5AeL-Py5_H6c-u8vNU4jPJmq3ztMwhJPKH7rdjcLjmRZOt9O7MOq6pXJ1WRq55QQBdctOsh1YaxpsYU7AS-4o20r7JvvJ2jFHG2hpTVRRRnbdbkPqpTKjT88Zt2c3oMDGZW4DwN6QZtB5s-2Il1sNJZUw0oweDMBbRp6AptbLWJ8bp7XqDTw3MasIqH81Sac_kpmKNLSO6jh95Oi4OvN3SBzJ_k1c-r4KAbqzzUUtnWRLhvgWY-u8_RuzGLKNMuwXp3U9PkuWh6o2auwEywTKPC7007JfV41h_7vtv5EYnaeYGOnDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b580b78a1.mp4?token=KWbKb9tfhJwMnG3f5C9QhZOD5hrpYRhPIVHrG5AeL-Py5_H6c-u8vNU4jPJmq3ztMwhJPKH7rdjcLjmRZOt9O7MOq6pXJ1WRq55QQBdctOsh1YaxpsYU7AS-4o20r7JvvJ2jFHG2hpTVRRRnbdbkPqpTKjT88Zt2c3oMDGZW4DwN6QZtB5s-2Il1sNJZUw0oweDMBbRp6AptbLWJ8bp7XqDTw3MasIqH81Sac_kpmKNLSO6jh95Oi4OvN3SBzJ_k1c-r4KAbqzzUUtnWRLhvgWY-u8_RuzGLKNMuwXp3U9PkuWh6o2auwEywTKPC7007JfV41h_7vtv5EYnaeYGOnDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه سانسورشده از مصاحبه چند روزپیش رضا گلزار سوپر استار سینما و تلویریون با امیر قیاسی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/31364" target="_blank">📅 12:58 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31362">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b124cde064.mp4?token=fR6d9ow8l_a0lGUzeQ1hi-eBXi8sQKlKxYxGuVfbBXeA20coqWMh1OXNwgu6Zn4EjxeUoVoO84dhYl4spAH_pnRuKGIoIAPp-doX2jlGhiINQ2PrXE4ojXKVaNtGsrNBHdva3T57Y32B23siYqL5cesoaBYILRCZwBuFUB8bYlahWgIBYzOC_PrJfsSlron4k6UiDI-3mx0G2EeM7IDIfxZbpD-9z8-RvTzQwFPUbYqJzfGMcpomg2AEo9QmZ_rQ-YKem44iRkhAJ-AeQJVVOawQysquK0jty9W6Jaisva5tjySKBjxSUJRlTrWThyaS9Zv1dWvmcdIZuv_JBWRwPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b124cde064.mp4?token=fR6d9ow8l_a0lGUzeQ1hi-eBXi8sQKlKxYxGuVfbBXeA20coqWMh1OXNwgu6Zn4EjxeUoVoO84dhYl4spAH_pnRuKGIoIAPp-doX2jlGhiINQ2PrXE4ojXKVaNtGsrNBHdva3T57Y32B23siYqL5cesoaBYILRCZwBuFUB8bYlahWgIBYzOC_PrJfsSlron4k6UiDI-3mx0G2EeM7IDIfxZbpD-9z8-RvTzQwFPUbYqJzfGMcpomg2AEo9QmZ_rQ-YKem44iRkhAJ-AeQJVVOawQysquK0jty9W6Jaisva5tjySKBjxSUJRlTrWThyaS9Zv1dWvmcdIZuv_JBWRwPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
برسی عملکرد پرسپولیسِ مهدی تارتار بعد از انجام هفت مسابقه در فصل جدید: پنج پیروزی، یک مساوی، یک‌شکست، پانزده گل‌زده، چهار گل‌خورده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/31362" target="_blank">📅 12:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31361">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/230f3b6f7c.mp4?token=K2HnVnQSO_VA-BLAjCguFcfKg6AKdmuwp94CNH9lnRgaGFPGNF1tLtGyd7HT5IzLENKzQRIM1jhe_q48bUHBfVlezjVUo2YQazCVKU3LyRMyTxWiqVO8tDJ9Sy1qhDvtdWC_nrm3Xb8NprskfA_hc4viJ7_TJpHghLdJyycaS9G77W-cP0TvKIB0HEp4gddGQ7zwX9gZNlMFOgriYWojuArHUASLlRgUEjnvUYX2DK_QNtGgCzdZPRpn8sUKrJzvmSzFg2BjuwDhsm3ZualLM5tGxqGDwHifuAgFqH33ULTCF6hdrE6OJmjirYTTyDcIQULnCneGuQRdjmjNW6H3NTaEbpazBqapDWZ-j_fDAfrQvy_WSoUxcEa_s7cDqn0Nvb4r4z7DiaJ2zm4g3tN5Hb5SbkbSg6LzmOLjVhaQtAS-YTNLbMGGYXwSRDaepjglH1bwV20svK8LyGcHTY0NQ7OgkRXPvwsz6_flGKnM529u_c7dfN9nlKABBeXx_T1sa8OrN05vkkVoZf-0j7AL2mLp3AvJxK3irHikvvcjmCRZd9npcjetrBFVLQc1Z068pBPlgcpGTIvUIXvCpfDjZbqjgxAfTGHxG2JDikkIuCFHIyKRXQ_BUIW93k682YERInraVxw1PrNNMEv7YceeDDNmfmZjW37KEQREkcUivpE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/230f3b6f7c.mp4?token=K2HnVnQSO_VA-BLAjCguFcfKg6AKdmuwp94CNH9lnRgaGFPGNF1tLtGyd7HT5IzLENKzQRIM1jhe_q48bUHBfVlezjVUo2YQazCVKU3LyRMyTxWiqVO8tDJ9Sy1qhDvtdWC_nrm3Xb8NprskfA_hc4viJ7_TJpHghLdJyycaS9G77W-cP0TvKIB0HEp4gddGQ7zwX9gZNlMFOgriYWojuArHUASLlRgUEjnvUYX2DK_QNtGgCzdZPRpn8sUKrJzvmSzFg2BjuwDhsm3ZualLM5tGxqGDwHifuAgFqH33ULTCF6hdrE6OJmjirYTTyDcIQULnCneGuQRdjmjNW6H3NTaEbpazBqapDWZ-j_fDAfrQvy_WSoUxcEa_s7cDqn0Nvb4r4z7DiaJ2zm4g3tN5Hb5SbkbSg6LzmOLjVhaQtAS-YTNLbMGGYXwSRDaepjglH1bwV20svK8LyGcHTY0NQ7OgkRXPvwsz6_flGKnM529u_c7dfN9nlKABBeXx_T1sa8OrN05vkkVoZf-0j7AL2mLp3AvJxK3irHikvvcjmCRZd9npcjetrBFVLQc1Z068pBPlgcpGTIvUIXvCpfDjZbqjgxAfTGHxG2JDikkIuCFHIyKRXQ_BUIW93k682YERInraVxw1PrNNMEv7YceeDDNmfmZjW37KEQREkcUivpE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌فوق‌العاده زیبا از جشن فارغ التحصیلی دانشجویان رشته علوم ورزشی دانشگاه شهر اهواز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/31361" target="_blank">📅 12:27 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31360">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">✅
هفته هشتم لالیگا؛ پیروزی سخت شاگردان مورینیو در برنابئو با تک گل دیومانده؛ اختلااف 6 امتیازی با صدر حفظ شد. وینیسیوس ممکنه به خاطر کشیدن موی بازیکن ویارئال دو جلسه محروم بشه و الکلاسیکو رو از دست بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/31360" target="_blank">📅 12:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31359">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PiGOvi-pfRYSJ7oV_O3ivCj7iyNB_iYgz4rM4ZHzb3i6sXSjBc53rYurAv-sbjZeElFjlaq6AWKcCirNOLjMKawtdkZ4M4_v85JCZPtqfhrimsCamARDrwcwSwfQDWlOX7GMcdZBsi71SgVhzQIWQdJ5SbLBLaj6bROrpfCK0mFKE9ygsgEDnmOpG9W-Zsz1VRZyHPLHhsl6UHHX3-041O57hBRvbkx6z4b16Zg208GtMtwU8fDF_RBrhzVXNb5AdM0_jcGP1d7ZP0ZjKRoclxvvl2gTxRgEmPKrP9gWjHYTt-R_B_4BMl4Obpu_GQTDiD2iXYvBTGNKPpE_XekKTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رئیس هیات‌مدیره استقلال: با علیرضا بیرانوند هیچ مذاکره‌ای نداشتیم اما درآینده هرچیزی ممکنه.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/31359" target="_blank">📅 11:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31358">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-RQSzHZqz1o6Kd8NIx5BgPjFFvvQFPeno9mhzI_-mGoFH8WgDkERMID0aFRxggWXbyYXJKKVpRhsiyQLcxCkeebUIjIKsB7Z-fn0kuuGOILw8-nEH9H-7ELm9uRHS3x_SnQdOUDtnry7N2Q80kOCCDR-6i2uNesFWRJKdPXkgA-WMzX8VKuZIOu0j2f1sCZjDttGAXC-v_1OSPIvfmZtW_o-dCH_ZXgatemsPzaBzsp00KVcZeq5V88dhMvtr6YzJHQW_XttXWy1p7YGC7D5zkeMzdFrTN19PjbkCrGe-8LmkuQAwg0RKcy-tH_zaU7etzl9EB-I_kydbseQiKlSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
گل‌های دیدار امشب دو تیم منچستر یونایتد و تاتنهام در هفته ششم رقابت‌های لیگ‌جزیره انگلیس؛ مایکل‌کریک سرالکس‌جوان‌نشد و در آستانه اخراجه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/31358" target="_blank">📅 09:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31356">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fCzD5WM5T-9lxuHVOsDMgTpqBsyiwgUkB7drjRJAj_36QAuoZeSgyPUYcWti7KKP9Nf6R8kUdPVazxXQvUVjsYXY9te8MkDXARDciGaTKW9at1T0d83m0Uy7F7e8MeBtT4rVYmsGUGUKc0XhSfXOGWZ05HZ2vogXI37ldEAu3oMUzATLKEFCcxv6-3a80dDve7ZQVRgu3Hg0mJ2BL14kk1KlecGZlOceJMPIeUWMumm7m1_1daYkOW0HX1eW-_Q2IdZoEpq1OCP-nDYu_GP8NzmIYDDc_M2vNDkBt4iU-oVJBONkbHhEStPdWhG8Xh2qvyONOXkCrdMmaomMlI7tJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MqTBb1qhLpOePQjpuTxBMjKwT_K4JNrclMqepqtzksfDbbTrETRvAw8PO6dpJPLmZwKWM-SIB5fMg5aLhg7JU5d78Y8EsR9iJNqgFtPDu1_ZXvK5hxC_iGda0nsPBmahDxXlU2nC0qYfev_FRl5RwCDJJbh4KinVHW4n8PK9AUr9d8c3Qu9RGlS88ey4mgDxVAwNzvkc-aBXZhb1Dwi8lXVI6aezRai39ARhfuTujd0-ij-oBZ47bfeglIh7me3ydugf1oUTKHOqpzluvxxr_GjGXMZpoLOEfGoPaj2Wkfafq55O8dpPg0iIWYoPiLlrOaWP9P_MaWHb2GKmO_-8qQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟣
🇦🇷
دبل‌تماشایی‌ومحشر لیونل مسی فوق ستاره 39 ساله آرژانتینی اینترمیامی در بازی بامداد امروز این تیم در لیگ MLS؛ تعداد گل‌های لئو مسی در کل دوران‌حرفه‌ایش به 934 رسید و برای58امین بار از سوفااسکور نمره کامل 10 از 10 دریافت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/31356" target="_blank">📅 09:38 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31355">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SrRuNQJ4ytvv-S7JfZFIYJCAkZytcyYQAgVscjV8k0GJgE3JdP1LVMQBe58BuT5fXlSJ3BpcZQkYeS62J-d2kqmu4k83h2oNOan5AmGRPIQDFYiOCmwVvFRhJKHKLd7_IM-BPMUs_yyJdQzpV-qt7pRyms0iAKZOMhIHIkC1ZKxJXGMLO4BonTDkYli8AfruDwdZtgnetYzTE4W78Px4lCjuJINzRdaDyZfGLyMoajMa9-vtRb7q9LIp0Sk1faeVEyq3KYF828mOx9wS0IpEHDPsSGVubsnZpeK2-surAuF8XvoLXISxIaDPCUMNqXwk4Ljwxq015Jwdj-eHNPFxCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
بارسا فلیک تو این‌فصل: 9 بازی. 0 مساوی. 0 باخت. 9 برد. 39 گل زده. میانگین 4.3 گل در هر بازی. بهترین خط حمله دنیا. صدر جدول لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/31355" target="_blank">📅 09:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31353">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa22c27bfb.mp4?token=pHcZIBYvXMPsGGpNpe8rpNFX_jgdLg_Tu0BOtkucBSVjPe0acGrlykdLMkivy7qbfa1xHVotdpjdrOFmQA-ONTtYVdGWThHxFdKVXTKydRl0bwJJi2Eke65SriWDz15PYFpGjf7i7VfGn3hzRHm-RQtvUQKw4ENlAIV9L9rz_AWBM9dg4SVo3eEQbwp1yE-pHVWJQQazIl1YLhZ0nl1CITZaSio0kmdHGv35-5oluQ-eNvLj23H9_PYebD8n4H3hMjBwteh_azyU1i2Mu6o0PMVLdp7MvBvpLYRubsxw_3cvt_kOW1cBo6VgQIfQ77efn1KQ_sjtXrjMlinVfua9ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa22c27bfb.mp4?token=pHcZIBYvXMPsGGpNpe8rpNFX_jgdLg_Tu0BOtkucBSVjPe0acGrlykdLMkivy7qbfa1xHVotdpjdrOFmQA-ONTtYVdGWThHxFdKVXTKydRl0bwJJi2Eke65SriWDz15PYFpGjf7i7VfGn3hzRHm-RQtvUQKw4ENlAIV9L9rz_AWBM9dg4SVo3eEQbwp1yE-pHVWJQQazIl1YLhZ0nl1CITZaSio0kmdHGv35-5oluQ-eNvLj23H9_PYebD8n4H3hMjBwteh_azyU1i2Mu6o0PMVLdp7MvBvpLYRubsxw_3cvt_kOW1cBo6VgQIfQ77efn1KQ_sjtXrjMlinVfua9ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
تفکیک‌ گل‌های کریس رونالدو و لیونل مسی در مسابقات ملی؛ رونالدو 146 گل در کل دوران حرفه ای خود با پیراهن پرتغال به ثمر رسانده و مسی 126 گل برای آرژانتین به ثبت رسانده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/31353" target="_blank">📅 09:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31352">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDFMldgCdWR64M6T8-NFk8OyipqzdojWSwc8nvopeH7P_WhUMTrOAbZHNz_bX7POCGGegUWxCd2Gl13h6SEWkgLCIC_uoLQMKifj3dCu48cOCa5Do-ZM8i0yzVJ2GhRZSBj59ZAl33zbXddcZ6CKw5iGfJu4pZ0QIzwTojwdp9Lq-2SZe8MJjN1JBm037hO0FwdrwrhMzqUHJHymtfRztiMQIw2cTTbygyXrpypzyQJvLtwpzpPLY8swuVyL4-9glFf1sH47R10HF-UO2aS5MXIwCHuEQg47-O_Ul9rhJe-10bSAAcLUC_4QQ6vrfEn32QQ4gGUbxNcgm09F8idhuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز
؛ دوئل حساس لیورپول vs من‌سیتی در استادیوم آنفیلد بدون حضور پپ
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/31352" target="_blank">📅 08:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31351">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PiY06FHrzSrVJ874glktq1FMJG6khZ1uItVJNja9EEUg5KZYG_CiF3afQFR8AO386BMOkpNs-4wdTN5eUWXcnBjYyQ_lueOA18lQYnqSyRum2ez3aU05BXngUAiDsuvCgR_nS77tA0oiWtognaOIY94jxwHJ6OFCBfQfP7cy896kexPrnmodQ-dG7hhtPBSefsAOkhhmeOnJUnHazhktRrxzysl4mROCYIGcDy50kdPPA3zKZy_uYr8wQHj-UXIPymYBwl8_s9otE8aiou4Z2idho9av08UExJFfSrDVjIWrEqg7jd-vDu3ytIR7glg7VxRPHxKUuEKmgrWOgN6eXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌دیروز؛
از برد خانگی بارسلونا و رئال مادرید تا دومین تساوی بایرنی‌ها در این فصل
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/31351" target="_blank">📅 08:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31350">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGh07yEnble65-uUa10krurt2IjHFnlscgTI5N8KBH5m_B3lN4bJ7IY20YT_QONMdyJivFzx2_iUA69Ev6L6QpYg88EFgw_SoUipzNyN85FEQ4zU9cLWbOSPXTcgXCtIF184usi4I976Wh-YOCz2KASPfzOwM8cvu9RUbx81KScUiOrJgK6U-Zr21DCfFQYEcGtqF_JPgnSna5xj3P6vOtwKVb6TC4fkt-_2pUgy_wqDkD0SQcvy94oYmXpsHfqLY92R9wtY4HSuCO3LO00GjjtcOngxaeBHhPExlbh2_OfazPSjh6dmtd2FcKrcmmD19wWulvI8vo0jMGf538kMBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این‌بازیکن آدم بشو نیست؟! اخراج وینیسیوس به دلیل‌کشیدن مو سر بازیکن حریف؛ وینیسیوس که توانسته‌بود دروازه ویارئال رابازکنه با بازبینی صحنه به‌ثمررسیدن گل، ستاره رئال مادرید به‌دلیل کشیدن موی بازیکن حریف از زمین مسابقه اخراج شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/31350" target="_blank">📅 01:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31349">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-eTlGFzHcf55jbAzNRaY4ML4ElEiCZ0NR2M-YWB6lLc30xG5P_erF-yHq-CsW_IPKCKhnKiJq16wGhZE3pGAu1ctFNdklOVf6pmWIGNoiH_ZlrX7pIaIM69oS2072KTCFomt6qn5HhvTawl6x1Rgh3l09Blv30_ViTUGAL373zO2I8wzYv189j_n4rimdKnIdPYT_vjC4EjfbaK8ModVafSCp1e0v9rrnsB9pq4wr9XE5RjCD7lfs_N1leBb1tp1iVknPy2Q41ItWKfNIMITBeSLZs-_Fn_4JjFUZmObr9qDrrHvqbvVK-J2OabV9b2iIX8_Lc75WyLfARi3jLTBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته هشتم لالیگا؛ پیروزی سخت شاگردان مورینیو در برنابئو با تک گل دیومانده؛ اختلااف 6 امتیازی با صدر حفظ شد. وینیسیوس ممکنه به خاطر کشیدن موی بازیکن ویارئال دو جلسه محروم بشه و الکلاسیکو رو از دست بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/31349" target="_blank">📅 00:38 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31347">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XKHs_iK-I5P51_kSp7eahnSNtJ4lAOMLQoahO7b4Xyni-IS-9MtBRnSP1teyhTkj8wNb8UZvmi9yWgSXSsXXjBWtCRADLsE3jMre42fjGfeBnnT0IUrfHEZbMVnAgIf7VMu6TJHNZEHRQj1-zQiTCMVJE_OVC3_VAVq8ElfWmpZRX4mtGnrlbtlx3LIodDimWbHfJ0RKbzaM4UtFDFOUG-MYKSuQbI0WPQQOvVaPgyUyICLkiZ9wJEadjEVwq9mdwVEi81Vx77y_s7jV-3gviGl1GhPNeh3gqwI2YcXGqT4A3b0kocuYb88PqFckDPq5hHLltb9jr9ie6KfjRpzvPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o__q-9AxevyKwsgFYKqfFJY9gqF6liNFI4fjCcw7_xVK6Gubo2ERLpddXr-AAxlTBKm-hCNYS-kBMRzclFoeGqT_T3OAIS-eEUk1RoJZDfsGBpZG1WUKCEaEf1yYe_KaQLHSR2Faqg4RAtTk829QIYnjmI8_B_u5hDTarDldNkPcZjCzEsKJpTODsDiACZHO7hF-NRrk5fhNN1TYsPeJv9ruiSkqc1JHJZXpKRA6fimsLLcYBbKgYPBCAU9ovqFG82eQX1bJSD31_QljIHSOP6FCh3cq9f5CXXlboU7MyyJ-ByjwZP8G5oHpq4rwsuko685oXwi2t8OAJga4u20Ubw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
این‌بازیکن آدم بشو نیست؟! اخراج وینیسیوس به دلیل‌کشیدن مو سر بازیکن حریف؛ وینیسیوس که توانسته‌بود دروازه ویارئال رابازکنه با بازبینی صحنه به‌ثمررسیدن گل، ستاره رئال مادرید به‌دلیل کشیدن موی بازیکن حریف از زمین مسابقه اخراج شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/31347" target="_blank">📅 00:31 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31346">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfSt1nKgQfml2oK1N5G6JQTHWXPVHI9fiH_EQrddk_9h-ngPZ0hicWW3JzOdX4WzQ3Sw2bx07x_durLe-DCALBqLKaPd3TpgzNZ6RJGIwAAjEVlmY7NljWZJu70YfRgczaXuRyzxJAGZAH6osvfKDnOXINURzRnhIgargzKiS0M5oYuTAyNAyrcn6AUr30Lhq-ocvHUAlun0MqWQH69-Lqra2nCtvGefpRSyNeauh0QSwnPk6hdUgFwQ0VG3sp3l9PypERiSnewSjG6R0BEY0Qt9cMpFtbeSpNSBNePEPbfksOy7htCtYdwvAd2wgtM3xPVmOocf1g4NRC83Pbxn7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته هشتم لالیگا؛ شماتیک ترکیب رئال مادرید برای دیدار مقابل ویارئال؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/31346" target="_blank">📅 00:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31345">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPvGzBjxPkmSgJlulA8V8jfT4uSHVBmzJJ0dpZU-u7E9a6q4q-6zSqqMJULVkFWh_ZuJiASdEJuBQ34lGyUsi53FN6yeFJ2LkH_UAHehOJTw6O43GwXUsiULuoevNwOrLqxESW1DgMsob3El0olu2t0ykiKOQB2p-ynulvOJzkyW3d5vf7TSWkW2FOpQfzfTkG4k2VFWRG4qxLYVSs0khYoe0ovz6KXwMJ-f_olaINF_cnFZ7NBthbxdSs1NkXVfI--L3-6P5QIIKQJhbY-PYVnSzKyRVycaV2VDsmVAtUEFj-h7AkFsXHWHdT44dYm6WXpJROaV6gCsm4GE89sqig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
برسی عملکرد پرسپولیسِ مهدی تارتار بعد از انجام هفت مسابقه در فصل جدید: پنج پیروزی، یک مساوی، یک‌شکست، پانزده گل‌زده، چهار گل‌خورده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/31345" target="_blank">📅 00:06 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31344">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oH82UHoFURp3KSlv_E6NruNq9KEwKhfbNWsV6ztfpSkM4Zql3adtUGX97sQLTQ4gE5PHPJVrru2Fv-XlkZMS0WIIxhr6WVHMromqYXbSyNmjnTHLz3wAODyXiIoSs9Y1c6f_wk0stfCADqP_3cN-vZhX1yj4Tqxi4TFap4_rq8qo4St_tUIMtF-LClvcVNTcdL8m-f_az_NpbFrYYn-fE1xLOAKcwR5w51b4xDUF1yNK6ILNhWnJORPmECh2-_vDGTCGo-1mc-zxlWkwZq46LS5aK7usxVDLzghNY1b4RaYCoaids7__ewyfaCOny_eGN0ip79emrZzVQ-p_K5bUYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌پرشیانا؛ یاسر آسانی ستاره آلبانیایی‌استقلال دیدار روزدوشنبه مقابل تیم الغرافه قطر رو از دست داد. این بازیکن ممکن‌ست با کاروان این تیم به قطر برود اما قطعا بازی نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/31344" target="_blank">📅 23:44 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31343">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
👤
برسی عملکرد پرسپولیسِ مهدی تارتار بعد از انجام هفت مسابقه در فصل جدید: پنج پیروزی، یک مساوی، یک‌شکست، پانزده گل‌زده، چهار گل‌خورده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/31343" target="_blank">📅 23:10 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31342">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEJ1u_4vEg1eHMnz87LeP7NLqIUkDTkJaFpy0fU_pHdNk8A_ItZSMSDMu8m4OriVuba05mATx17xj2nB8lmZHC3_e0LU1lKiMJcuCtZR6nmeXOlcbYDqepvuawbeQs7Eq8gWbclKb2TnxmEbA1VS2G2BwLFYoS0dnykReoaapjGI8RoEfE0fU4R4bsp4yXCQwn0UVSsSXjnHf4s6q3KZDomgGU7xLcdJhihis1OXOmpYGM99DgCFhXF-SxVZGUpPsykjyhYxkKG-sTE7hb6q7jyJCs9xyTlWq5w0OcUsFpBS1ZH7ZqfZ5TlX6B4HTv_urLoY-3t85CIWE9Xe6M7Iyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
گلشیفته فراهانی با جان سینا فیلم بازی کردهه؛ چه لبیم گرفت ازش. الان دارم میفهمم چرا حکومت داره تلاش میکنه گلشیفته رو به ایران برگردونده.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/31342" target="_blank">📅 22:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31341">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ece2dc9b.mp4?token=b6z1ZJR_JVicrRGPt95DRQ_eREhNsh6DJWXrN0kXd9cjUCO_qUk-fO2xkoYsvDG2DzUSPZBmaBUduDek-jl2GHaFP00jqBr22lvtzAYSvycoAD8eS0nz7bfYDOD4I9DEqRn87lpCjQ6Ele4fWW4PLLnCeqj6snme7cbZ_xQc5g7KtcySb54TUf1y6fn2B5vxfPnMYTM2CiusPvkOHCZti5BFGu0oZ54QNH6d7FLCwQCWtD5Wg8fK60Fx2XFvTSewsGXQrJ1pawkfNxFLZLMaUcVMg6kR1jK7lT2trx5SntS6KAUPONJ1iQMkMTRAq_9Xvfqmv1l_HbmArs8mqDnzzrwQ7vuYEj0hZG3Bxwypil1di2hBRmPQy6mURuN1qZhWPm9fnwzOr_ANXAzhUUWQ0gU8K7jXXrWW7SZAA9zX5mNnzBuXpMfsZq2u6-dAzTWedJQYSllRE76UQo7L04QRJgfaOslo8JcO3O8BfgDcBWgQJdXCCYDy7XRLbU4zghR7FjScFm3gRodH9DQ-MZ93fSqA6xT0B6XNftLZOoeGUdaSBOtIT4Q_TGKcs3rSp8zzsMxDYr29mfzaCvF7SyjpiOUEwuiXQjYf4_t_cyCk9qWjNL2EAMT9QGFv9wO8ocfhxshG_M3pJBLYNTnNUWYmHoxNINXeYEdEWELbWVK0H2E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ece2dc9b.mp4?token=b6z1ZJR_JVicrRGPt95DRQ_eREhNsh6DJWXrN0kXd9cjUCO_qUk-fO2xkoYsvDG2DzUSPZBmaBUduDek-jl2GHaFP00jqBr22lvtzAYSvycoAD8eS0nz7bfYDOD4I9DEqRn87lpCjQ6Ele4fWW4PLLnCeqj6snme7cbZ_xQc5g7KtcySb54TUf1y6fn2B5vxfPnMYTM2CiusPvkOHCZti5BFGu0oZ54QNH6d7FLCwQCWtD5Wg8fK60Fx2XFvTSewsGXQrJ1pawkfNxFLZLMaUcVMg6kR1jK7lT2trx5SntS6KAUPONJ1iQMkMTRAq_9Xvfqmv1l_HbmArs8mqDnzzrwQ7vuYEj0hZG3Bxwypil1di2hBRmPQy6mURuN1qZhWPm9fnwzOr_ANXAzhUUWQ0gU8K7jXXrWW7SZAA9zX5mNnzBuXpMfsZq2u6-dAzTWedJQYSllRE76UQo7L04QRJgfaOslo8JcO3O8BfgDcBWgQJdXCCYDy7XRLbU4zghR7FjScFm3gRodH9DQ-MZ93fSqA6xT0B6XNftLZOoeGUdaSBOtIT4Q_TGKcs3rSp8zzsMxDYr29mfzaCvF7SyjpiOUEwuiXQjYf4_t_cyCk9qWjNL2EAMT9QGFv9wO8ocfhxshG_M3pJBLYNTnNUWYmHoxNINXeYEdEWELbWVK0H2E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
نتیجه دو مسابقه مهم امشب؛ هشتمین پیروزی پیاپی و ارزشمند شاگردان هانسی فلیک در لالیگا و تثبیت صدر نشینی و توقف شیاطین سرخ مقابل شاگردان دی‌زربی. مایکل کریک در آستانه برکناری از هدایت منچستر یونایتد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/31341" target="_blank">📅 22:32 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31340">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇪🇸
👤
نتیجه دو مسابقه مهم امشب؛ هشتمین پیروزی پیاپی و ارزشمند شاگردان هانسی فلیک در لالیگا و تثبیت صدر نشینی و توقف شیاطین سرخ مقابل شاگردان دی‌زربی. مایکل کریک در آستانه برکناری از هدایت منچستر یونایتد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/31340" target="_blank">📅 22:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31338">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ecruesUVr7G2ELlBkmPhdIxJqx0xVmOWGg2zQFDXsNA73DvMjYFQPedGA5cJLl-_tQ5Fuherkm2NRk9RGcD3yEPmFGEP8FPIO7ea3_U5oiaObXL8Ievij93uvElDsIPIUFm8JbK-bDrNH6lKIDb-0B82axP4SwZw406jEwuNIeOSteHNK91wwmt-L1Q7OnZMvNoFEvxLSCzh0IIZE0zqpTTFjKSnEHGafqNtEF4HaszuoAVIEYUUQo09e_0PNCzsw07iGe5hAA3OY4Z_HMWukgoSXN6JKoVw9qySDDBMKbWk2fRsLJ74qcETejWOEjAezCK7VTSBEYHROFPA4x9xHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m9gGaDQ8Gx36Xg5wdfWUhOVZ15xWHDdiVTA2BCxlF9fDBQ-LDcqcaklf9EyuRNYiBXwr2kbqSlKV0TeorHxsqMSSz_9E-Xe9DR33m0nCYuMbWiC47VHfwMSPA9rnRzhgRGQaBJRTasd2aikUPyNH36NqVCTpfIQBaC_s2eXrVfHoroTPWAjl-s3fb1AwAUus8iW4dMg_zVkzL_YOwdrs5jTD96skJ8b5MEGGDaWW5Fumoo7lGNl95Bg090fQmQxYe0ggLY5Zb4gWy2PRpQXq8OBRjymZ_yabmvWVjUbZEpM-ojgXlfBZXR3PSSTqYf-v8Gx3DwvXRHtKt-HhdrArGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته هشتم لالیگا|شماتیک ترکیب بارسلونا برای دیدار امشب مقابل ختافه؛ ساعت 20:00 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/31338" target="_blank">📅 22:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31334">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VTqG2R4Eq-eUBY6cA_MneN6RkDv329rI-JO9DdPYpcfiUazJE2Nain6YSBZIj5zehW2oe5mcIwEU3HDirJv1Y_3pvv-XM-wPDMQONnI_zTB4vLKc_bCjoPtZcsl1bNieGA7PGFMFPIKnzqpLO-FcsC8YeZ6UzbumaqwlW5HBoY1ixpi2MYqmK674C4PjMARIrZLvRIvWvoMRHEwezC8mJuoY1jwsyQtE_MyPyzjPRjWU0U16TK_VpBCQN3Mw2nDYRh4nn6JNn9IZlHDMs7KI77R7GQ5OQ85SmFWDpM0rCAd8k4sCtBl555GKElhpu_4aYWJbf6NLtRrvp4aUy1eygA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/txuiVksAn50U0xpzM05Eu08v4mQFncCgkxI1NXqh3kqJ6oJ6v5XcNHYZEd03o_v09lc2xzkP_homxOVjkgFxVtxeSyqpnfctQ3jj91TlBhxYoWbJN4E1k-6Fqyd6-gfdbSJYIGpjrzWvryFIe8iYAacseMYTw2gvneQ-Oz1mzJ6dgeGvhE6zMS-kHVQRqDqD1u975H_J1KP9a_8yg1wD0e5vREUSaaTpa5KDQ0ShtNMJ37xSIJa8udaobBGuTdxu0WmI1HzV7rdHmgm50F4QvHKdCCPi4zui4SRcuraHi23JwXOSibxgeW-UhcfWogf7bbjuxDxWzUI0L8SnFmhnmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته هشتم لالیگا؛ شماتیک ترکیب رئال مادرید برای دیدار مقابل ویارئال؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/31334" target="_blank">📅 21:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31333">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oawsMNhPsgBW3DhzcYwSEnYFN121fhV3N28FsSalfXRd1Q6cuJoE0ep3CYCnIhtfKs3sHknyqudj9pmsEJeo9fI-qJWnY5FI1vQpMZs_JXH-c8d_pRQ71gJvAQIHerzO0cNdhe2_glsMeO70NyXLJKk4r_KOrG9o28mqGQsaFlc_M-nFaIIfrAALjZcrDUFUkLmxM6Uy7tJPlJOLLrDJJ0-U8zJIhD1I7fcPkTGReNJLOCBKWUJt0HApJJrDcDD9QHD0mb4JqvKWBdPPpRyU2XIDKFQ-KEXQ9q0TZy_kOSb585RcAFUNSxKtSBbh-MRf1gfu07e7461RaJ81h8FFlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
رسول‌خطیبی‌سومین‌سرمربی اخراجی فصل جدید؛ بعدِ شکست‌سنگین فجر مقابل سپاهان مدیران این باشگاه با رسول خطیبی قطع همکاری کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/31333" target="_blank">📅 21:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31332">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBR9r5JufJ14BatwEJ7h3jiAMtI3_72CjIOOo5ioU7medI9pJ0alhVsWnbllnNoDuxgie50C6Yusk32zldxMiB-21woXCGKe-WYs0f92g6K22C7C5oij6oJLHxe__rIemTLiY42uE0xOz08xI9J9LgjtFFWu8gn87hrKCSdaYmnzF8b06G8gDvDfMlCnWxkXseve0s23fvy4syTExhbDyMieRNJZmtAmfJ2rwBTc7S95lMezt517VCDA_nOH705M4f6XhL96T7ir4RtPbpZbXN0WbTU59hSuBzuXNjs0g1JkY16UtbVJAxyFu5kEeX1LGOV2ONX5jMTPI8AjRouwEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته هشتم لالیگا؛
شماتیک ترکیب رئال مادرید برای دیدار مقابل ویارئال؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/31332" target="_blank">📅 21:15 · 18 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
