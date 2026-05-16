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
<img src="https://cdn4.telesco.pe/file/KtAzV1Pmir1gkKl-4ODKdWdhVbBys6Zs0Fa6yJjg1Q8I8_DPN_DckRlefO0UVj8OC2Rvg6A-jvr72vxqLaADOFrL983gXtm4_IjZNpAATG5gaTNaTHWgmUN21zwxMKLOh8AAUWnXHBE9bBm-UdPgqg5PEEhOCIFRcg8iqFhgP0J2Kpm-_1dQ9rjEmw4_Rfyw2wlweQLPIq-dYVRxu_0AOxxj0dwq56WVIvz2QqtgcaUW5Ug0sOS5C73qgq2QKsyOuUJZYAg73KbQZ8wVDqhNm9bPJF-m1YsYuSw_rcbhUCusZurhd9lRv_B_8ISBc-hTnlzGpd1WQXOcH4w17tZrmA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 954K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-26 11:21:50</div>
<hr>

<div class="tg-post" id="msg-120334">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2mhTc-JUgbIrorzKoMYvfhtP_N6rGJOO85-7610FcCNN81iJZhDVKHltUF3pNtj0YTShts9Rn5usmfvF3UdyCY6lX6gyU8fnszZJ6nVZSC-5nfI2VcWEL8KL20kRVPTDBVxCWJ2ctzfpcSf7CGvUPwCki9I5Um_Qtyf4ITKRs59mheWmEl3pwfbT4WEYYj1csGZiyuPGt-1Jq7GlCJP5DsHFosNNLk697jz0tG-aveb6B2MMET4dzCGtbbzOAHsf0krmFlq8JuJ-8cpdbjULJ-jSMnh_3QS0_EZbKc-YJVCufC0gPHlg299e3ZKog8uHsPBcVczwGlnV9rdZTu_GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت استثنایی گیگی
2️⃣
2️⃣
2️⃣
تحویل زیر یک دقیقه
✅
دارای لینک سابسکریشن جهت دیدن حجم و کنترل مصرف
✅
بدون قطعی
✅
بدون محدودیت کاربر و زمان
✅
جمینایو چت جی بی تی و... کامل اوکیه با سرورامون
✅
🏪
پشتیبانی کامل
✅
شروع فعالیت از سال 2022
✅
پرداخت ریالی
✅
ضریب و این چیزا ندارن و تا آخرین مگابایت برای پشتیبانیش درختمتیم
🥂
⭐️
@Napsternetiran_bot
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🔶
@Napsternetvirani</div>
<div class="tg-footer">👁️ 624 · <a href="https://t.me/alonews/120334" target="_blank">📅 11:19 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120333">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
ارگان رسانه ای وابسته به سپاه نوشت: وزارت اقتصاد طرح مدیریت تنگه هرمز از طریق بیمه را پیگیری می‌کند تا امکان مدیریت بر تنگه در پساجنگ مطابق حقوق بین‌الملل فراهم شود و برای ایران آورده اقتصادی نیز داشته باش
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/alonews/120333" target="_blank">📅 11:16 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120332">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
الجزیره: برق کوبا پس از خاموشی گسترده دوباره وصل شد، اما بحران انرژی همچنان ادامه دارد
🔴
برق در سراسر کوبا روز جمعه پس از خاموشی‌های گسترده دوباره برقرار شد، اما بحران انرژی این کشور با کاهش شدید ذخایر نفتی همچنان ادامه دارد.
🔴
شرکت ملی برق کوبا اعلام کرد که پس از قطعی برق در ۷ استان از ۱۵ استان، «سیستم برق ملی دوباره برقرار شده است»، با این حال قطعی‌های برنامه‌ریزی‌شده ادامه دارد و نیروگاه‌های قدیمی هنوز در دست تعمیر هستند.
🔴
وزیر انرژی، روز چهارشنبه اعلام کرد که ذخایر نفت کشور «تمام شده است». کمبود انرژی خشم عمومی را برانگیخته و شهروندان هاوانا با کوبیدن قابلمه و ماهیتابه اعتراض خود را نشان دادند.
🔴
کوبا کاهش انرژی را ناشی از تحریم‌های آمریکا می‌داند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/alonews/120332" target="_blank">📅 11:13 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120331">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
آسوشیتدپرس: بازگشت ناو هواپیمابر جرالد فورد به پایگاه پس از ۱۱ ماه مأموریت
🔴
وزارت جنگ آمریکا اعلام کرد پیت هگست، وزیر جنگ، روز شنبه در پایگاه دریایی نورفولک در ویرجینیا از ناو هواپیمابر جرالد فورد و ۴۵۰۰ ملوان آن پس از ۱۱ ماه مأموریت استقبال می‌کند.
🔴
این ناو ۳۲۶ روز در دریا بوده که طولانی‌ترین استقرار یک ناو هواپیمابر آمریکایی در ۵۰ سال گذشته و سومین رکورد از زمان جنگ ویتنام است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/alonews/120331" target="_blank">📅 11:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120330">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
کپیتال اکونومیست: قیمت نفت به ۱۵۰ دلار در هر بشکه خواهد رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/alonews/120330" target="_blank">📅 11:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120329">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
نیروی هوایی اوکراین اعلام کرد: 269 پهپاد از 294 پهپاد پرتاب شده توسط ارتش روسیه را شب گذشته سرنگون کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/alonews/120329" target="_blank">📅 11:04 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120328">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
نیویورک تایمز گزارش می‌دهد که نیروهای نظامی آمریکا "در حال آماده‌سازی برای دور دیگری از حملات هستند... این بار با شدت بیشتر. این حملات ممکن است از روز دوشنبه آغاز شود. اهداف نظامی بیشتری از ایران در نظر گرفته شده است که شامل زیرساخت‌ها نیز می‌شود."
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/alonews/120328" target="_blank">📅 11:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120325">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HAFG02CbZxF8lKCt8mtm6MKo4gMgyN-24FH8Q4hmroDooKiKLwFQT7n465oCLKrqxi9bintqMaKgrMKAIj3Cshq9hxNoE8UDKo4ItWbBWw1U_TbxJgyBzcAPUgnSUoDXgwvscui4MNveXa9V8GG-fpvYULEwCMC9xS3NL9uXvpxm0yUJ8QnLHustJFEeb1I8xIXWR8rM1HVM4MksyRS7SjESQhAa44J_b-g6RN7Es5gBarkFv0mckdf9aBoGjAPBAXHFeBTN2h6HAhG7qwFbw1595kmY8XEKhPQCu1XtAwhR8mucUFk3WYLMy_Iz8hiqzb7yIxSBd06fubn3pnSw8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o-THk5kZSDcyfINTrEtr161BcA1vXe9OQRqvRHYMRou7aqAcsIEumI0kG3CmtQDUce8TuF75-j2rm2Eu-VZzgZ1Q5wD2LRky1oz4_rP8vZucbL8LdHcFhiVONVz7afvJsC6wUubCvyFWjKRJXKGelguQhAYFSh9pGNWM477-3eKY2ypIa-vfIa_QgFxoGsm4PdxQhT0HlGqzEMzGdCpCWXcMxvOsoqmIPGRMua6qbKq1Q61j--RzBx4TByapBUc_uMAnAa1L566-z7UlMIaLD11-IcVHfH2f2sKUnYXleJl1G6S_Z_AS66Vce9VS6HaLXDhr-g2wRAAdoElKSQ6hXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dTDXgbAB9kFi6WqCdK0-wMU6wKq0Dku2DmI_ZI1hpt2WeVcBuYXmS41smvEm7JOhpj3o8UPe7VRiQsP8wqa7_TW3Hw4_YQoszcsZbaOrgMBeOgr0wkaKzIl-VsIt3jniIqfkdiMO50vtRTiqug7g48xJTz-hOifHbTRTSTIdCsao8fLzKO9cwf8q-4BOKiUFiXDTlqg0gqaVRAJPjkVsoA2cRUTSX7A6pnN7oDeTDXTscWfeeRbOweylbb2kWgu4SfUewZ7y4jNHJEk_rtK02mIHbWCBH8sSlmYeFPKZ3Qu2TtS8nzxS1iYJjTCQna7uK6gS6qHXQZgDCiBg3CIqbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
شب گذشته در بسیاری از برنامه های صداوسیما، مجریان با تفنگ حاضر شدند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/alonews/120325" target="_blank">📅 10:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120324">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a78a5c4a5a.mp4?token=uml108V9Um0ehOcVz2ukgSRV3usIyq5a6e4tyKUpVQZMsF9JH7a8DBQWvksGwBYhniQ1hICSPfBDBqSrIJFgR4MioIzvJRKipeILCpE-7K9C_ZomboKe6kVum_9to8di4PQuFl116ukNXQKGAGm1Q5cvZExOH4mnSol5QnZaAgtYdK43fJCm6NNQLnv3_UV8VviolseXEO_tIgwt-UbDHAba-qYA2I5HfAD6SJ8ln4L6hBz2jqJrIT7huR0WKX1hZiMp6umppI3cPgRLpqUnkW_InKxYJOWB0z1gZX1euSMN-gSsAvVKrRNo0CAMAG959Z0VyDPHmLz3Q5M2HxwwwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a78a5c4a5a.mp4?token=uml108V9Um0ehOcVz2ukgSRV3usIyq5a6e4tyKUpVQZMsF9JH7a8DBQWvksGwBYhniQ1hICSPfBDBqSrIJFgR4MioIzvJRKipeILCpE-7K9C_ZomboKe6kVum_9to8di4PQuFl116ukNXQKGAGm1Q5cvZExOH4mnSol5QnZaAgtYdK43fJCm6NNQLnv3_UV8VviolseXEO_tIgwt-UbDHAba-qYA2I5HfAD6SJ8ln4L6hBz2jqJrIT7huR0WKX1hZiMp6umppI3cPgRLpqUnkW_InKxYJOWB0z1gZX1euSMN-gSsAvVKrRNo0CAMAG959Z0VyDPHmLz3Q5M2HxwwwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو: چین کاری را انجام می‌دهد که من اگر رهبر چینی بودم انجام می‌دادم. آن‌ها تلاش می‌کنند در تمام این صنایع کلیدی آینده بر جهان مسلط شوند.
🔴
شاید ما از آن خوشمان نیاید، اما این همان کاری است که آن‌ها انجام خواهند داد زیرا به نفع بهترین منافع خود عمل می‌کنند. ما نیز باید به نفع بهترین منافع خود عمل کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/alonews/120324" target="_blank">📅 10:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120323">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e012e3f1b5.mp4?token=vkJkBCQRS9YpZ8NXVzfOQ7HZdLjMXY7FSqsNlqqdvW3_7AYxbq8vCWWl7-pB0TVeKjox6fV3LMYXuAPUl25vIJTVpoCo5vyKsqI4UKVTm-n9yciRbA5Bu5yxAclkyDxYfx__pCYqerwRLkCj1REku_gHJuOnm_n0qdWRQdkJW7eQ283lcEqUL3KiHBCXAUb6Lh10aDWnR5TvQEJbjwYDs-pXDFVjT6qDdY8cvxTQqVNyipCb94fZN6mYRYgzRJpgGhS7PzDN9kO0qmPX1OyGqwjReGKBkjFJN-pzdvg3oVjV5_Yl6R4AxVb_YFumYrFD8bmx2j1s6ES5uMU_xk6Rag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e012e3f1b5.mp4?token=vkJkBCQRS9YpZ8NXVzfOQ7HZdLjMXY7FSqsNlqqdvW3_7AYxbq8vCWWl7-pB0TVeKjox6fV3LMYXuAPUl25vIJTVpoCo5vyKsqI4UKVTm-n9yciRbA5Bu5yxAclkyDxYfx__pCYqerwRLkCj1REku_gHJuOnm_n0qdWRQdkJW7eQ283lcEqUL3KiHBCXAUb6Lh10aDWnR5TvQEJbjwYDs-pXDFVjT6qDdY8cvxTQqVNyipCb94fZN6mYRYgzRJpgGhS7PzDN9kO0qmPX1OyGqwjReGKBkjFJN-pzdvg3oVjV5_Yl6R4AxVb_YFumYrFD8bmx2j1s6ES5uMU_xk6Rag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روبیو: اگر جی دی ونس کاندیدای ریاست جمهوری شود، اولین نفری هستم که از او حمایت می کنم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/alonews/120323" target="_blank">📅 10:30 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120322">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
روزنامه عبری هاآرتص: چهار ماه از ایجاد «شورای صلح» برای نوار غزه می‌گذرد؛ تاکنون طرح ترامپ اجرا نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/alonews/120322" target="_blank">📅 10:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120321">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
ترامپ: نفت ونزوئلا ما را ثروتمند کرد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/alonews/120321" target="_blank">📅 10:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120320">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEoJr2epALS8dnvzsVzDQ-_LLbL4DsESy-YQ7Zgb3dw1Y1KU5WkqtH0QQ4xoKlbsY70ukmkiihcz0XZGEN_hHNISBmEf1TEL18pG725G65dLZfU4NkKa60UFlrfUtdbz3yf_w8p-34T7kphfNH4WQ4B4YyY3szvkCJmoqcmbMGw6HlsApSg7x7VgYk9LE8RfBD-xbQO-CFvyoAQhOjOhADKkxYKrKew71K8GPAfl2bKXF8T6HkmRiB5IA61-tCpr7ASQ7QB3ny2ych0zPjfStzeP4h6kBA7bYowz7FxtUiDXFLs_guw-ygxlramsPQ9rbWs9_zxKY45Do7iXZa8lcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری مشاور قالیباف در اینستاگرام
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/alonews/120320" target="_blank">📅 10:24 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120319">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
وزارت دادگستری آمریکا با صدور بیانیه‌ای، مدعی شد «محمد باقر سعد داوود السعدی»، شهروند عراقی و از اعضای شاخص کتائب حزب‌الله دستگیر شده و به ایالات متحده منتقل شده است.
🔴
وزارت دادگستری آمریکا افزود كه این شهروند عراقی در برابر «سارا نتبورن»، قاضی دادگاه فدرال در منطقه منهتن شهر نیویورک حاضر شده و او دستور بازداشت را تا زمان محاکمه صادر کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/alonews/120319" target="_blank">📅 10:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120318">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
سی‌ان‌بی‌سی: ترامپ چند هفته قبل از آنکه به طور علنی سهام شرکت هوش مصنوعی Palantir Technologies را در شبکه Truth Social تحسین کند، سهام این شرکت را خریداری کرد.
🔴
سوابق نشان می‌دهد که ترامپ در اوایل سال ۲۰۲۶ بین حدود ۲۴۷,۰۰۰ تا ۶۳۰,۰۰۰ دلار سهام Palantir خریداری کرده است، از جمله چند خرید در ماه مارس. او بعداً این شرکت را در یک پست در Truth Social در آوریل، در زمانی که سهام فناوری به شدت کاهش یافته بود، تبلیغ کرد.
🔴
اسناد همچنین نشان می‌دهد که ترامپ در فوریه تا ۵ میلیون دلار سهام Palantir فروخته و سرمایه‌گذاری‌های بزرگ دیگری در حوزه فناوری انجام داده است، از جمله در Nvidia، Apple، Amazon، Microsoft و Oracle.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/alonews/120318" target="_blank">📅 10:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120317">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
کرملین: پوتین در تاریخ ۱۹ و ۲۰ مه به چین سفر خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/alonews/120317" target="_blank">📅 10:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120316">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
رسانه‌های عراقی از شنیده‌شدن صدای انفجار در منطقه الکراده بغداد خبر دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/alonews/120316" target="_blank">📅 10:04 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120315">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
پیام پزشکیان به رهبر کاتولیک‌های جهان: از موضع اخلاقی و منطقی شما در قبال تجاوزات نظامی اخیر به ایران قدردانی می‌کنم
🔴
حملات آمریکا و اسرائیل صرفاً علیه ایران نیست، بلکه علیه حاکمیت قانون و ارزش‌های انسانی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/alonews/120315" target="_blank">📅 09:54 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120314">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
فوووری / منابع روسی: یک جنگنده سوخو-35 نیروی هوایی روسیه، یک جنگنده F-16 فایتینگ فالکون ناتو را سرنگون کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/alonews/120314" target="_blank">📅 09:41 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120313">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
هشدار نارنجی هواشناسی: بارش‌های شدید و وزش باد در شمال کشور
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/alonews/120313" target="_blank">📅 09:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120312">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
کوبا: آماده دفاع از خود در مقابل تهاجم احتمالی آمریکا هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/120312" target="_blank">📅 09:16 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120311">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
مدیرکل مدیریت بحران استانداری اصفهان گفت: در ساعات بعدازظهر امروز تا روز دوشنبه وزش باد شدید و تندبادهای لحظه‌ای همراه با گردوغبار در استان پیش‌بینی می‌شود و سرعت باد به ۹۰ کیلومتر می‌رسد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/120311" target="_blank">📅 09:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120310">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
انفجار کنترل‌شده بمب‌های عمل‌نکرده در شیراز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/120310" target="_blank">📅 09:09 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120309">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
رویترز: ایالات متحده ممکن است از اسرائیل بخواهد میلیاردها دلار از وجوه مالیاتی فلسطینیان که مسدود شده است را به حمایت از طرح بازسازی غزه توسط ترامپ اختصاص دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/120309" target="_blank">📅 09:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120308">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1860318fa.mp4?token=JDewH6F4h9sK1MPgJJOGqbKZJKuWZES2XuLZhKS88Ir5IkjWULB7uhNGVPhA0Vj0zrzSNVUxIwltfD0plLImsNp0HrZ94xKlWcsoiOFAXJ6CQ3kZcVJPkuMl7l1KgNMC_nSJTQ4yT5OM1MgcdZgVET0RFMA-bxKJ8GMhMITqHvpi5ZhLXT5AOhnUxTN25hCyfMOzmvu29hh3AJycNieWPbtM3JFPsTljnC8CVpG6y3JYQYXTNp0oMEMXQ8kzeDB0CoQdHAGw_iSEgKLdsoK16Dob7cPaBFuT58sjwmWmXf5duLpvcu7o8V4grjjWZPC20tXSXTjha0RQmpVufPzqB5vvtzRFZotHvGeSvZNev3ezaQ_ZGu9iazTHFY_QfC4lDrAzwqEeITtp4REuFpWeJkjaRSgqJx1wqZb7mjeEdY_iHenb--s8ZIyz_1kPcW6iMk3xw2EnlBi2c5FQzGJbBhH2Up3nL1CyvvZGdap1b3d5cLxpcjkUN1qbAEUEXIwWPAyOZIA9Dr_v4RCywr3mIHDqvhq0ESuh2UWcGsalllazqnFdbUhmqQGP_iNijZsjQtqBDGZ7rA3yckUvoUJeNXsrUPqdlx9p7X1pBS6VkogUbH6zSPpmmQoKnkQI44se5GZPvBtoM2wiRWsmTI12OjL5O3tYIplO4DBMOlYT2zI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1860318fa.mp4?token=JDewH6F4h9sK1MPgJJOGqbKZJKuWZES2XuLZhKS88Ir5IkjWULB7uhNGVPhA0Vj0zrzSNVUxIwltfD0plLImsNp0HrZ94xKlWcsoiOFAXJ6CQ3kZcVJPkuMl7l1KgNMC_nSJTQ4yT5OM1MgcdZgVET0RFMA-bxKJ8GMhMITqHvpi5ZhLXT5AOhnUxTN25hCyfMOzmvu29hh3AJycNieWPbtM3JFPsTljnC8CVpG6y3JYQYXTNp0oMEMXQ8kzeDB0CoQdHAGw_iSEgKLdsoK16Dob7cPaBFuT58sjwmWmXf5duLpvcu7o8V4grjjWZPC20tXSXTjha0RQmpVufPzqB5vvtzRFZotHvGeSvZNev3ezaQ_ZGu9iazTHFY_QfC4lDrAzwqEeITtp4REuFpWeJkjaRSgqJx1wqZb7mjeEdY_iHenb--s8ZIyz_1kPcW6iMk3xw2EnlBi2c5FQzGJbBhH2Up3nL1CyvvZGdap1b3d5cLxpcjkUN1qbAEUEXIwWPAyOZIA9Dr_v4RCywr3mIHDqvhq0ESuh2UWcGsalllazqnFdbUhmqQGP_iNijZsjQtqBDGZ7rA3yckUvoUJeNXsrUPqdlx9p7X1pBS6VkogUbH6zSPpmmQoKnkQI44se5GZPvBtoM2wiRWsmTI12OjL5O3tYIplO4DBMOlYT2zI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئوهای منتشر شده در شبکه‌های اجتماعی از یک انفجار مهیب در مکزیک خبر می‌دهند که یک جشن مردمی را به تراژدی تبدیل کرد.
🔴
این حادثه در ایالت «خالیسکو» رخ داد؛ جایی که پرتاب جرقه ناشی از آتش‌بازی به مخازن گاز، باعث ایجاد یک انفجار قدرتمند شد.
🔴
در پی این انفجار، دست‌کم یک نفر کشته و بیش از ۲۰ تن دیگر مجروح شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/alonews/120308" target="_blank">📅 09:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120307">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2419fa5807.mp4?token=i1CUHnHxG9RS578IaeoryUjigLzm_7oKJISRtZdNmcMZSbVkK1eGiOEgFFIIoaObSBspBaHkJHKf0yOVQP3NmsJPCjbxV7a0VBG26urKa3Xf7QbZNvFe3vEAydb7FRHJfEX2m6QKL_wJ_Zs7zcyQ8bjX9Vq3xpkIvsnDJb9W_xJYBR31FhSOzU-QUBx13M-NrNT06S0_Jsu_QELBXhZ6BHe11BYQP0Xix09_VrCoPzo6m5-5i89mg5_q9l_JDG5-bdkhAYSatZmtZ1cgIj4ndCIGMK49y8NMjT9byVsWKqnejjdtUJpLwgV-ubu7Y2l3mnqRVqcH6jOGnDphyY4Zuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2419fa5807.mp4?token=i1CUHnHxG9RS578IaeoryUjigLzm_7oKJISRtZdNmcMZSbVkK1eGiOEgFFIIoaObSBspBaHkJHKf0yOVQP3NmsJPCjbxV7a0VBG26urKa3Xf7QbZNvFe3vEAydb7FRHJfEX2m6QKL_wJ_Zs7zcyQ8bjX9Vq3xpkIvsnDJb9W_xJYBR31FhSOzU-QUBx13M-NrNT06S0_Jsu_QELBXhZ6BHe11BYQP0Xix09_VrCoPzo6m5-5i89mg5_q9l_JDG5-bdkhAYSatZmtZ1cgIj4ndCIGMK49y8NMjT9byVsWKqnejjdtUJpLwgV-ubu7Y2l3mnqRVqcH6jOGnDphyY4Zuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بن گویر وزیر امنیت ملی اسرائیل:
ما در دوره نصرت الهی هستیم.
🔴
ما در دوره ای از آغاز رستگاری هستیم و فقط باید به راه خود ادامه دهیم و بدون توقف ادامه دهیم
🔴
در لبنان، غزه، و یهودیه و سامره (کرانه باختری) توقف نکنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/alonews/120307" target="_blank">📅 08:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120306">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/66b24dd163.mp4?token=KluH3fRMNSLNoaFB0QcTzRCxcgQBtqq2k0uTNeZypYnx8I4lY4hsBMQPq0z4HFWEGWVzUDCzLoVcChMRpZAMNy_g0-yD0h067paND8n3BqEMEJxbv6jXwIQsj9HYzd_qw1_Weavi8ZSJ-_7dBxBWngk3ujtSa87_kzgIqlnR81qd56sFnMRpRi-gsPuifq7IX_IzJY7x6PrKBBSY0OlodXoIc0nW65LPzGBvF7hgl0qH_smG7rKgAf4qMf9RfGKtE7BVa30m9cEmAdLyoOe9k-AsYjV0Vneliqt73Xu21gKRpBoyFJakStARakYo_GPyD8T97biELn_M12p9Yz8pqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/66b24dd163.mp4?token=KluH3fRMNSLNoaFB0QcTzRCxcgQBtqq2k0uTNeZypYnx8I4lY4hsBMQPq0z4HFWEGWVzUDCzLoVcChMRpZAMNy_g0-yD0h067paND8n3BqEMEJxbv6jXwIQsj9HYzd_qw1_Weavi8ZSJ-_7dBxBWngk3ujtSa87_kzgIqlnR81qd56sFnMRpRi-gsPuifq7IX_IzJY7x6PrKBBSY0OlodXoIc0nW65LPzGBvF7hgl0qH_smG7rKgAf4qMf9RfGKtE7BVa30m9cEmAdLyoOe9k-AsYjV0Vneliqt73Xu21gKRpBoyFJakStARakYo_GPyD8T97biELn_M12p9Yz8pqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
به دستور ممدانی شهردار نیویورک، ۴۰۰ موتور سیکلت این شهر که رانندگان آن ها از کلاه ایمنی استفاده نمی‌کردند منهدم شدند
🔴
به گفته وی، این کار در راستای تقویت فرهنگ استفاده از کلاه ایمنی انجام شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/alonews/120306" target="_blank">📅 08:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120305">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrtb6G9AGVZ07kcHG4pKmq1PXcnrJ2k7IeXfGBNSFuRFw5qehD1s--gNiqO4-YW5Ef-OaNh8s4eUJhaouKCXQnqHGQooE33j9_C1H8hyGQ-P2sFC43JIFJs85PJ0DgHmL1NLcM0LWtlyt1HyIJg4PqtLBOpZ1CZYh58IFodCVii8-cg3mkTC4HtDaFEiRkRB4ZcngvHSd5JTP2ekAOZujsQWkRd3BAtjRRXayEqycIgpvC4rHftv3-nwwGQ6WRUp8GDXb-8XKEPhsbaoXhnHhaTxor7cOocWeIBQUOrXa1BBFnZXlr1qINo51ueOmF0t8YW-mwnWgyslVx7XyOGkrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس‌جمهور فنلاند: آمریکا از ناتو خارج نخواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/alonews/120305" target="_blank">📅 08:49 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120304">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNxJKSr3oIE9ni9GVWyYWX3q9_T7CKTdkuk9EHUn3AlHB2r0eGEiAw1lObzfe745IB3imGVjaBqokGgIBr3KatoW5CrKi_LNHWC2omoCwPuToBSkwL6q2mkW3IkxgnL8Hb2aRP2DmnBd53yXIWr8atoE3kJWWPDDldSnzuesouMPv6bxm9Veh8CtCtceIMJqFe65DvdtIWMbwBLQ7TLAKiy53EyUy0x4FG4__RdJKl-ky0IZStKb_uRAUGNf_m9SarmwUyNXGf9vxipsN9aYUjcVU4wXSW5Psq8f7Ng1DhzkNEiSP8nMhgpCmJ65NDUhoqTvl5L99TkBz3bXEE-wZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس سازمان اداری و استخدامی: ساعت کاری جدید اداره‌ها از امروز اجرایی می‌شود و تا نیمه شهریور ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/alonews/120304" target="_blank">📅 08:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120303">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ta_JZxfn7iFR53U80XQNr9vXHYOq1qqpnlBoBPWe1OrAxGS0h0suYD6tYGGXzujnBuKXLXaDC8QKZOcJg6yhnDzfduFx54YhSq6MCFqnnKdnaIJkoWT8NHArOF_i0EFvASD74SIyvwgk6QkshVwKoCV6aaZlrv6uaNS0_3SwAaJT5b52Z8J4DRCrzzWw_jxvw5DpfQ0ID6_i7SIkuqAnWTiAuUQp_d7X9rxXFKMWQUB9G21YkQciZOVjulKEvmWDcdzpT73p5ijZRAkWjGNRSYkO1tdIUg-Y4OAdZPLfhTu4WsJfmH2HcprAiPGHuUB_B2Oiygxfj7W7cGnLlzh85Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روزنامه دیلی تلگراف گزارش داد، احتمال آن که کر استارمر نخست وزیر انگلیس از سمت خود به نقل شهردار منچستر کناره گیری کند وجود دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/120303" target="_blank">📅 08:41 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120302">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
دونالد
ترامپ
، مدعی شد در جریان یک عملیات مشترک میان نیروهای آمریکایی و نیجریه‌ای، «ابوبلال المنوکی»، مرد شماره دو  داعش را از پای درآوردیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/120302" target="_blank">📅 08:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120301">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
سفیر چین در سازمان ملل، از پیش‌نویس قطعنامه پیشنهادی آمریکا و بحرین دربارۀ تنگه هرمز انتقاد و تاکید کرد که محتوا و زمان آن مناسب نیست و تصویب آن کمک‌کننده نخواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/120301" target="_blank">📅 08:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120300">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47a9d3010c.mp4?token=SDLgv5badNwpR6Z4nMlLddsXbk_DNdj0uYNroYQ6ld26pxfJNEkRi2lNxcIZ1q_pU75WBw6nLVilNZzxxhKv6RwuZgbqjn-KegVCIu1AYn1gcEEsasY6yU9KaopxKYdFcB8eTljAowcKJNuzTaEKGSriHlYlW38GGLGOuS7O5kgRk6hg6uJXkSrw6CIPthLq3PW3UpKM1YrGljqebiuVPwTCBXEpqpsMAx0dM2ErL9d7-hjSt9z5zHpoIcutxqd5eu27SoYRy24RTEDE3bXKRuZnRFHAkVtGcwxA7M3XzmLnIJEKu01ipkmd8Uw9Roa64Ukt9fwMFZtvmTHEWid9Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47a9d3010c.mp4?token=SDLgv5badNwpR6Z4nMlLddsXbk_DNdj0uYNroYQ6ld26pxfJNEkRi2lNxcIZ1q_pU75WBw6nLVilNZzxxhKv6RwuZgbqjn-KegVCIu1AYn1gcEEsasY6yU9KaopxKYdFcB8eTljAowcKJNuzTaEKGSriHlYlW38GGLGOuS7O5kgRk6hg6uJXkSrw6CIPthLq3PW3UpKM1YrGljqebiuVPwTCBXEpqpsMAx0dM2ErL9d7-hjSt9z5zHpoIcutxqd5eu27SoYRy24RTEDE3bXKRuZnRFHAkVtGcwxA7M3XzmLnIJEKu01ipkmd8Uw9Roa64Ukt9fwMFZtvmTHEWid9Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس جمهور ترامپ در مورد ایران:
ما نه تا دوربین مختلف توی اون سایت داریم و دقت به قدری بالاست که ما می توانیم نام یک شخص را هم بخوانیم.
🔴
اگر اسمش محمد است ، بیشترشان محمد هستند ؛ شما می توانید حدود 50 درصد درست حدس بزنید.
🔴
هر کسي که به اون فضا نزديک بشه ، ما میفهمیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/120300" target="_blank">📅 02:23 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120299">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8501d1acc2.mp4?token=uMd3aK_eQcn6Vd89DtQ_ZKRC8rZ6d9mSXd9WiEvcQQBm7i1Fuk8j5u_Bu1xs6Zyp_U77yDLfmmrkQB7uBfOt6EWww9GNpxyaNmvYp6NIQptQS2vmxx9Ngst_MAjM6p8Vb5AqOsxKfjZMhwTCkSPyURIvw0CPkRd70RgapCiPA8XFC-WXM51WThn2p_Y1Or8oVT8Z_pBlLj7pmAx-h1lnPZus1hOJfqEqGP-nGYcouT_S9bp33p2v1UHEVJgIRltBz21_nzuVFuxF-WwObkG83U23npPjKIrZdipjDe9w91IeigQwRUbCENrFew1xVluh_2BUdEhlLjq6BXl3QWQ-lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8501d1acc2.mp4?token=uMd3aK_eQcn6Vd89DtQ_ZKRC8rZ6d9mSXd9WiEvcQQBm7i1Fuk8j5u_Bu1xs6Zyp_U77yDLfmmrkQB7uBfOt6EWww9GNpxyaNmvYp6NIQptQS2vmxx9Ngst_MAjM6p8Vb5AqOsxKfjZMhwTCkSPyURIvw0CPkRd70RgapCiPA8XFC-WXM51WThn2p_Y1Or8oVT8Z_pBlLj7pmAx-h1lnPZus1hOJfqEqGP-nGYcouT_S9bp33p2v1UHEVJgIRltBz21_nzuVFuxF-WwObkG83U23npPjKIrZdipjDe9w91IeigQwRUbCENrFew1xVluh_2BUdEhlLjq6BXl3QWQ-lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: گفتم گرد و غبار هسته ای را می گیریم ایران گفت: "شما می توانید آن را داشته باشید. اونا گفتن ، " ما نمیتونیم تحملش کنیم. ما توانایی مصرف آن را نداریم. گفتم: "چرا؟ اونا گفتن چون خيلي ضربه خورده"
🔴
برت بایر فاکس: چرا این کافی نیست اگر هدف شما این بود که آنها را عقب بیندازید ؟
🔴
ترامپ: از نظر روابط عمومی به اندازه کافی خوب نیست‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/alonews/120299" target="_blank">📅 02:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120298">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/013d87334a.mp4?token=r88osW5Qlyx2uVNmKgSv_BBihPx9JAPu5Uel-2wJKk2yGnYSPefwz3vhE1yo6RZlj6Hm6Mty2keT-ZdDsVKmw8dZ9Zj9mZ5a9tPJL9wSklQLdygISm90KLC8_EwSsTE6iW1k-9skMXNn7425LXOl0XG2dEsGYLI01AJ6ltrBriMZ2icIHvdigBlsJ4Ubtv6xCmQV_lxqvIsWm70E8xHg_KjhqDp9Yn8NWyLU9lXy2R-J3qTZlMnAl0S4luA5EsXLjAbQVq0pyBpG5yuE01qD8FBfSw_R7uNPce8_tlLPbxHWK3G0mUQh8nz0bi19j5HYgUHLY8MbQsAqkLcO705RGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/013d87334a.mp4?token=r88osW5Qlyx2uVNmKgSv_BBihPx9JAPu5Uel-2wJKk2yGnYSPefwz3vhE1yo6RZlj6Hm6Mty2keT-ZdDsVKmw8dZ9Zj9mZ5a9tPJL9wSklQLdygISm90KLC8_EwSsTE6iW1k-9skMXNn7425LXOl0XG2dEsGYLI01AJ6ltrBriMZ2icIHvdigBlsJ4Ubtv6xCmQV_lxqvIsWm70E8xHg_KjhqDp9Yn8NWyLU9lXy2R-J3qTZlMnAl0S4luA5EsXLjAbQVq0pyBpG5yuE01qD8FBfSw_R7uNPce8_tlLPbxHWK3G0mUQh8nz0bi19j5HYgUHLY8MbQsAqkLcO705RGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برت بایر از فاکس: فکر می کنید ایران به زودی تسلیم خواهد شد ؟
🔴
ترامپ: بله ، من هیچ شکی ندارم.‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/alonews/120298" target="_blank">📅 02:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120297">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/057506e9d2.mp4?token=i11YOhqw32iBGkfQ14mdlfhLipa8vSU4GRqlG029Qj8Y4GfzhTcSd40oGT8CKZTbl0dHv0bRFQ29QGx9FBUimsdxT9v9Ke8BrKu6Z60UrB-sm_e3IlnBndaiVSKx-nVJsh2HdAVP2xcMt8ZBdWg7VuIL7uqB06ywdfdrlNpv0h21oOL-MsMg2iwZiqP04D2EBJpLiFYXNXyJvkho5FQjl2bJpY9ATWoBMWPFpzuq0u3hjCd5w9h_LtDIggdHJiqIbeHqY-YVGc4VtmXPNUN1EwbvEqgOD2atfizgjrUerQ_LyyK0ohwRj7KZH5fofZSZEVOYehsKCYwLBDcl_OBa0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/057506e9d2.mp4?token=i11YOhqw32iBGkfQ14mdlfhLipa8vSU4GRqlG029Qj8Y4GfzhTcSd40oGT8CKZTbl0dHv0bRFQ29QGx9FBUimsdxT9v9Ke8BrKu6Z60UrB-sm_e3IlnBndaiVSKx-nVJsh2HdAVP2xcMt8ZBdWg7VuIL7uqB06ywdfdrlNpv0h21oOL-MsMg2iwZiqP04D2EBJpLiFYXNXyJvkho5FQjl2bJpY9ATWoBMWPFpzuq0u3hjCd5w9h_LtDIggdHJiqIbeHqY-YVGc4VtmXPNUN1EwbvEqgOD2atfizgjrUerQ_LyyK0ohwRj7KZH5fofZSZEVOYehsKCYwLBDcl_OBa0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس جمهور ترامپ در مورد ایران:
ایران سالهاست که جهان را با تنگه هرمز نگه داشته است. اونا در گذشته تنگه رو بسته بودن اونا ازش به عنوان سلاح استفاده ميکنن اونا ازش به عنوان سلاح با من استفاده نميکنن
🔴
رئیس جمهور شی دیشب با لبخند گفت: "خب ، آنها تنگه را می بندند ، و بعد شما آنها را می بندید."‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/alonews/120297" target="_blank">📅 02:13 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120296">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65d4e78216.mp4?token=tE-tCVklohY7KeJlzkGcR53NeXlBkNQrBQpRzp1cHjOqVipZTov6c-SFyKtmkIpZ2gB0L4IIYaw6WlNXsHWncKm8x8G0V0_n4g8l-3683XFx1STjqTq7VS-FWTwRR_iwrjmWjma8PNXC8ZD7qrnvgVQDrZVM1AbeVNq9YphF8h4q_Tl4XN8PNewVJZwODQp54hI-pHJpGY0h3Hv0G6pDGybE_titM8TZ2Zv1LVIIaPZOHuBPfgGu7Twcb34lNwJk2g9JSUbSieHpaN8vAqVk6SHO59tt_fSGL_Qr3Y-U56bvdRcx0lMrJ_qzlQ9im8SVn6pRGAbDjqSlovfXYM7zBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65d4e78216.mp4?token=tE-tCVklohY7KeJlzkGcR53NeXlBkNQrBQpRzp1cHjOqVipZTov6c-SFyKtmkIpZ2gB0L4IIYaw6WlNXsHWncKm8x8G0V0_n4g8l-3683XFx1STjqTq7VS-FWTwRR_iwrjmWjma8PNXC8ZD7qrnvgVQDrZVM1AbeVNq9YphF8h4q_Tl4XN8PNewVJZwODQp54hI-pHJpGY0h3Hv0G6pDGybE_titM8TZ2Zv1LVIIaPZOHuBPfgGu7Twcb34lNwJk2g9JSUbSieHpaN8vAqVk6SHO59tt_fSGL_Qr3Y-U56bvdRcx0lMrJ_qzlQ9im8SVn6pRGAbDjqSlovfXYM7zBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برت بایر از فاکس: آیا تاب آوری ایران را دست کم گرفتید ؟
🔴
ترامپ: چیزی را دست کم نگرفتم ما می توانیم پل ها و ظرفیت برق آنها را در دو روز از بین ببریم.‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/120296" target="_blank">📅 02:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120295">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7b5ca6f24.mp4?token=eMgdtdRtc7aVWHG4kj5Jo_47kVcP16E9a38XpXMw8zFZQmzKLJj_DLvLx05UYFlShRriU7JZQ7FZdf1kDgr9CvyPMa8VRgOXumk6ODrT2Wu92koL61fyPVK3nZDI1l1V-65_dJRfjk8SH4Y-R44hFW-KhobGf79_fQ_rjU_GKKBlwBadHSvbqchk92gdVYnhlTOZoP8yWinJsMRLymgm09BPc6P4wAQW9S_DK_MrajnWzDJVdICKcc2ZVwwuDNWFXR6CsXxqrHla69dFNEDnTxJsd1l8hUs7HX0KM_QlfjAQacCwfh-UB3wQC70JohXuJFeQj_bOy0YiMx4hHRxk2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7b5ca6f24.mp4?token=eMgdtdRtc7aVWHG4kj5Jo_47kVcP16E9a38XpXMw8zFZQmzKLJj_DLvLx05UYFlShRriU7JZQ7FZdf1kDgr9CvyPMa8VRgOXumk6ODrT2Wu92koL61fyPVK3nZDI1l1V-65_dJRfjk8SH4Y-R44hFW-KhobGf79_fQ_rjU_GKKBlwBadHSvbqchk92gdVYnhlTOZoP8yWinJsMRLymgm09BPc6P4wAQW9S_DK_MrajnWzDJVdICKcc2ZVwwuDNWFXR6CsXxqrHla69dFNEDnTxJsd1l8hUs7HX0KM_QlfjAQacCwfh-UB3wQC70JohXuJFeQj_bOy0YiMx4hHRxk2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : ویتنام ۱۹ سال طول کشید، عراق حدود ۱۰ سال، کره ۷ سال، یکی دیگه ۱۴ سال، یکی ۱۲ سال، یکی هم ۹ سال
- ما فقط دو ماه و نیم اونجا بودیم
- چین هم این هفته سه تا نفتکش پر از نفت ایران رو برد، چون ما اجازه دادیم این اتفاق بیفته،شما اجازه دادید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/120295" target="_blank">📅 02:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120294">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز: چین جرات اقدام علیه تایوان را در دوران قدرت من نخواهد داشت‌‌
🔴
پکن از عدم نیاز واشنگتن به هیچ کمکی در پرونده ایران یا ایمن سازی ناوبری در تنگه هرمز خبر داد‌‌
🔴
چین برای تامین 40 درصد منابع نفتی خود به تنگه هرمز تکیه می کند‌‌
🔴
خب، به هر حال ما به یک راه‌حل خواهیم رسید. بنابراین یا این مسئله به‌صورت خشونت‌آمیز حل می‌شود یا بدون خشونت. و من خیلی ترجیح می‌دهم که بدون خشونت باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/alonews/120294" target="_blank">📅 01:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120293">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtJilXCWqskyisHWOCDL8nRodaZLLwmowQEyfSrU6_1yp2zAjKCPPnCQNuyJLV42hDOValHkgIKcvgtYqfFmz8DXNV_90zxS5vuAf5NwuuH515L6XHE9r9WdXeHNYFTfPjPE4GfesW4-Xbwwo8YF42bH7DXw6m5EcvklTY1qj3xiUtHHSU2GKlaixK7jnpU_2xN6bNuFZ1o3tVMrfpanK6ufV6MfsUpxY9Qe-X8SJnsuVdYvINECnykPjCi3AUOdWlPnY0K5PVmc3G3x4vncrN2td9pT5ULMf8SBZtHrdXNwDZZ7eolELIWQWLY_AjQvrH1k0oxtFAl3hX0ClUP-6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پک ۱۰عددی کاندوم با افزایش قیمت به ۴۸۰هزار تومان رسیده!
🔴
دولت باید به اینجور چیزا سوبسید بده تا همه بتونن استفاده کنن اما.....
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/120293" target="_blank">📅 01:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120290">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ee9cf6e98.mp4?token=mybfeosUrxXC6T54etAfnhA-VdrD4_tlDY4sjph1VVQwjxIaEMRhhEqueh5iwIehLMG343yNlLQhGGJ53OV2Nh1oZUwHUxWGI1TU1ewqIkgU9G-HYzGgIxRH-s_w3yippVmxXhYgl6ZCNzEKSpkEgexL-3dkkJYixE3nAhAzW1BzukXI39aeYEOZfW9D9PpYZwhl_Dgu1WFmiANPcuhGynzuKZ-cKfvKX5EV3cbamKgcgZZ-W-gmG7nHQWmR9MLav5VceAP8BPYnvQ-mdIv6bBCMtXqfghiSxVBUsuKlkhuIMz06nnsZTw-aHOPkuZN8r0FuBcMHpGHJYgY1L0qvkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ee9cf6e98.mp4?token=mybfeosUrxXC6T54etAfnhA-VdrD4_tlDY4sjph1VVQwjxIaEMRhhEqueh5iwIehLMG343yNlLQhGGJ53OV2Nh1oZUwHUxWGI1TU1ewqIkgU9G-HYzGgIxRH-s_w3yippVmxXhYgl6ZCNzEKSpkEgexL-3dkkJYixE3nAhAzW1BzukXI39aeYEOZfW9D9PpYZwhl_Dgu1WFmiANPcuhGynzuKZ-cKfvKX5EV3cbamKgcgZZ-W-gmG7nHQWmR9MLav5VceAP8BPYnvQ-mdIv6bBCMtXqfghiSxVBUsuKlkhuIMz06nnsZTw-aHOPkuZN8r0FuBcMHpGHJYgY1L0qvkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجریان بیسواد صدا و سیما برداشتن یه تصویر هوش مصنوعی رو گذاشتن و دارن تحلیلش میکنن!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/alonews/120290" target="_blank">📅 00:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120289">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/444d83ba6e.mp4?token=cRlz6M1ADneTrHR1PqN7Z7L5wU6dTr69zMyHbdjz90DXFjm00nK7Q3uRRuhmOM-YjDxXZ2-KuLtgqgwMZSRkmTmo6Y9UBDcWDzJyYAdO7RuEKvnQd83Uqh-WSHPnGGAb8Mp6fZwuoHPkwLT4SwMFyx2bHYjCiNJziC89eVhLt3Ez2c14oeda82APO-adT82murt4r3DisVgWJBqWumcF7EEdutnaApNsRgJCwBuDlR1eVK9VLM5wSNGJanpdJqA937aBuOcDlxNctRlyrw4cuV5q9FtKY9_84FOmFue9a48T3H1MdkHMjszD0BE4z21fVvOkDhyrFnMB66P8zDX2RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/444d83ba6e.mp4?token=cRlz6M1ADneTrHR1PqN7Z7L5wU6dTr69zMyHbdjz90DXFjm00nK7Q3uRRuhmOM-YjDxXZ2-KuLtgqgwMZSRkmTmo6Y9UBDcWDzJyYAdO7RuEKvnQd83Uqh-WSHPnGGAb8Mp6fZwuoHPkwLT4SwMFyx2bHYjCiNJziC89eVhLt3Ez2c14oeda82APO-adT82murt4r3DisVgWJBqWumcF7EEdutnaApNsRgJCwBuDlR1eVK9VLM5wSNGJanpdJqA937aBuOcDlxNctRlyrw4cuV5q9FtKY9_84FOmFue9a48T3H1MdkHMjszD0BE4z21fVvOkDhyrFnMB66P8zDX2RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مصاحبه‌گر : قبول دارید عامل گرانی‌ها محاصره آمریکا علیه ماست؟
🔴
حامی حکومت : نه، قبول ندارم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/alonews/120289" target="_blank">📅 00:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120288">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
نیویورک تایمز: گزینه‌های ترامپ در ایران شامل نیروهای ویژه زمینی برای کنترل اورانیوم است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/alonews/120288" target="_blank">📅 00:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120287">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09e3b53b1a.mp4?token=sunbuM-6fQ3pNkPCIh5hkaBZnpZ__FvaYgwXIdyNHo0Op_Pct0XuTNZaurgRof2hf3hWn8ov92ZQ0iGnL-dIpYF-m5rCdUWMhnqovqR3Xo0fk7Cbr586dqLs8mfyk_0Idr5YACuLx59H2df3k8QscPcxaiHW7GqxvrE_4SsjJ3sDmaTIe7-reMYAN6j37JUu5qqkn3vXIkxYYrBe3p0sWsHbgJ13-9B78BirVrV_kCSesWfKBAYs_aOlP0LDUPDw_1QymERnWgTZdn5cN0l_sclZH7CagicWD9y9i3oI1_GLCIk1xQHOv38unvtGDjEP9tUBAQNw6-n53cyapDuTqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09e3b53b1a.mp4?token=sunbuM-6fQ3pNkPCIh5hkaBZnpZ__FvaYgwXIdyNHo0Op_Pct0XuTNZaurgRof2hf3hWn8ov92ZQ0iGnL-dIpYF-m5rCdUWMhnqovqR3Xo0fk7Cbr586dqLs8mfyk_0Idr5YACuLx59H2df3k8QscPcxaiHW7GqxvrE_4SsjJ3sDmaTIe7-reMYAN6j37JUu5qqkn3vXIkxYYrBe3p0sWsHbgJ13-9B78BirVrV_kCSesWfKBAYs_aOlP0LDUPDw_1QymERnWgTZdn5cN0l_sclZH7CagicWD9y9i3oI1_GLCIk1xQHOv38unvtGDjEP9tUBAQNw6-n53cyapDuTqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گلایه مخاطب ایران اینترنشنال از قیمت نجومی عرق سگی
🔴
قبل جنگ لیتری ۲۵۰بود و با دوستام میخوردم اما الان لیتری ۱۵۰۰ و تنها میخورم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/alonews/120287" target="_blank">📅 00:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120286">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
ادعای نیویورک‌تایمز: دو مقام خاورمیانه‌ای ادعا کردند که آمریکا و اسرائیل در حال آماده‌سازی گسترده برای احتمال ازسرگیری حملات علیه ایران هستند؛
آماده‌سازی‌ای که بزرگ‌ترین سطح از زمان آتش‌بس محسوب می‌شود
؛ این حمله ممکن است از هفته آینده آغاز شود
🔴
مقام‌های نظامی آمریکا به‌طور غیررسمی می‌گویند پیروزی در حملات جدید بسیار دشوار است، زیرا ایران بخش زیادی از توان موشکی و زیرزمینی خود را بازیابی کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/120286" target="_blank">📅 00:06 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120285">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
نیویورک‌تایمز: ترامپ روز جمعه پس از بازگشت از چین، با تصمیم‌های مهمی درباره ایران مواجه شد؛ در حالی که نزدیک‌ترین مشاورانش طرح‌هایی برای ازسرگیری حملات نظامی در صورت تصمیم او برای شکستن بن‌بست از طریق فشار نظامی تهیه کرده‌اند
🔴
مشاوران رئیس جمهور آمریکا می‌گویند ترامپ هنوز درباره گام بعدی درباره ایران تصمیم نگرفته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/alonews/120285" target="_blank">📅 00:04 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120284">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
فارس: نمایندگان مجلس پیشنهاد افزایش ۵۰۰ هزار تا ۱ میلیون‌تومانی رقم کالابرگ را داده‌اند اما دولت گفته که تنها منابع افزایش ۲۵۰ هزارتومانی رقم کالابرگ را در اختیار دارد و سازمان برنامه هم اعلام کرده که پول نداریم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/alonews/120284" target="_blank">📅 23:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120283">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
ترامپ رسید آمریکا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/120283" target="_blank">📅 23:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120282">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHitin_D1tV6B6BVGQkhjajQ1OfX-yahDB0s-BhXlC2DrvpYPB4Wa5hC7anWtjng7kuGFDuVGjDNAwUcGplfpKzDeL0aWEEtX6Zsep4Sa_TMmkt6w9T4sVBnjp1L6N2uAsBgAOk1ZePIf1_JvBAe0ZsqqT4R8gC8wv3wpWzUJe0JompIBSRcyaGUTDq4brTlkkMcveuRocoPs8ECDqWeb2oHq-HHSXQqZUE_GoaqULPxpQR5Wdk3OXU4nTIXRZYm8pGHDw1_MtnrwfSmcYOkVIcXCKUwiO5UqXxG-dl_-MboybpwjkphJonkYizdxl6n8AOdbicBhYPe192LEye3Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مقامات آمریکایی مشکوک هستند که هکرهای مرتبط با ایران ممکن است پشت یک سری نفوذهای سایبری باشند که سیستم‌های نظارت بر سوخت در پمپ‌بنزین‌ها در چندین ایالت را هدف قرار داده‌اند، طبق گزارش CNN
🔴
هکرها از سیستم‌های اندازه‌گیری خودکار مخازن که به اینترنت متصل بودند بدون حفاظت رمز عبور سوء استفاده کردند و این امکان را برایشان فراهم کرد تا خوانش‌های نمایش داده شده سوخت را دستکاری کنند — هرچند نه سطح واقعی سوخت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/alonews/120282" target="_blank">📅 23:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120281">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
ژان-لوک ملانشون، نامزد ریاست‌جمهوری فرانسه، درباره ایران و تنگه هرمز: «وقتی کشوری از خود دفاع می‌کند، از تمام ابزارهای دفاعی خود استفاده می‌کند.
🔴
ما هم همین کار را میکردیم.
🔴
ما تمام کانال مانش را مین‌گذاری می‌کردیم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/alonews/120281" target="_blank">📅 23:39 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120280">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
منابع عراقی از حملۀ پهپادی به مقر گروهک‌های تجزیه‌طلب در کردستان عراق خبر می‌دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/alonews/120280" target="_blank">📅 23:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120279">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
فیلد مارشال ، محسن رضایی: قواعد نظم جدید جهان دیگه آمریکا محور نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/alonews/120279" target="_blank">📅 23:24 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120277">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f3b1bc7ef.mp4?token=TNkqwX8EdVvjSAlCEQN4zktzEfp6rLxdrZC_0HQmkrpLotpmFUjq2N8WKDajA5mwhaKOZkX5jGb5urvPX_23gUAoWszQn2BDj6x4d-N4Vs5wFjmYgWNnVr7BZSZkdZWsht4Ks2G12XdQVad3cnP4Is9yldjmsYkOWqyknLspZhmmtW9zP1gSh_9UQRJaWS3TcsA2rvvKSLOVHGrnM_pi1B6XFMEQsIYb_4xnvM8JOZSs94KLqy7gWPtCEV5CAIDXMvII8InUPgk9piuKsr_Q-pdMBjFk_pD2rbsR3WzC9X6i2hZM4Y-6SexIksqQDmOHnRRKbz_actSyW0nQ3eDVsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f3b1bc7ef.mp4?token=TNkqwX8EdVvjSAlCEQN4zktzEfp6rLxdrZC_0HQmkrpLotpmFUjq2N8WKDajA5mwhaKOZkX5jGb5urvPX_23gUAoWszQn2BDj6x4d-N4Vs5wFjmYgWNnVr7BZSZkdZWsht4Ks2G12XdQVad3cnP4Is9yldjmsYkOWqyknLspZhmmtW9zP1gSh_9UQRJaWS3TcsA2rvvKSLOVHGrnM_pi1B6XFMEQsIYb_4xnvM8JOZSs94KLqy7gWPtCEV5CAIDXMvII8InUPgk9piuKsr_Q-pdMBjFk_pD2rbsR3WzC9X6i2hZM4Y-6SexIksqQDmOHnRRKbz_actSyW0nQ3eDVsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهر صور تو "جنوب لبنان" بعد از حمله‌ی سنگین ارتش اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/alonews/120277" target="_blank">📅 23:20 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120276">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
واشنگتن پست : ایران واضح‌ترین بازنده دیدار ترامپ از پکن است، با مخالفت علنی پکن با اختلال در هرمز، تعهد به عدم ارسال تجهیزات نظامی به تهران و توافق بر اینکه تنگه «باید باز بماند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/120276" target="_blank">📅 23:15 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120275">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/195d80b28e.mp4?token=d46ht0c6MGlAJk7SPhPfMQ6FcDXgV644l9GL4V2oa3qHS28FTxr7PgEg56ER002SfVCGCCcyM0VUS8Fhh2jc2IfUEQ-fjvb3Ty2W5vUfKx4x4RIQoeiBdxQqm6O7jOVKdf3mQ8Usdz2eeaeuLSWMoJ9cMFK4g4-66Xsis_e-_maecOL4hQ7WTlZyXBxxCYwQ10YDri4UzGwVsyzJZEswFJiYshq8PDIT1kegIu4i9lY9m6tBdK2ma1EfQ_P_4Clisov7TBpl-8y31bg2Xp9SIrXkEQD2D4ND-1GkEhbQlLeGiy4cp-VkcanOuSPFM6Bei5TpW1G3C_bk7WBHLnANCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/195d80b28e.mp4?token=d46ht0c6MGlAJk7SPhPfMQ6FcDXgV644l9GL4V2oa3qHS28FTxr7PgEg56ER002SfVCGCCcyM0VUS8Fhh2jc2IfUEQ-fjvb3Ty2W5vUfKx4x4RIQoeiBdxQqm6O7jOVKdf3mQ8Usdz2eeaeuLSWMoJ9cMFK4g4-66Xsis_e-_maecOL4hQ7WTlZyXBxxCYwQ10YDri4UzGwVsyzJZEswFJiYshq8PDIT1kegIu4i9lY9m6tBdK2ma1EfQ_P_4Clisov7TBpl-8y31bg2Xp9SIrXkEQD2D4ND-1GkEhbQlLeGiy4cp-VkcanOuSPFM6Bei5TpW1G3C_bk7WBHLnANCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره تایوان: من به دنبال این نیستم که کسی مستقل شود. و می‌دانید، ما قرار است ۹۵۰۰ مایل سفر کنیم تا جنگی را انجام دهیم. من به دنبال آن نیستم.
🔴
می‌خواهم تایوان آرام شود؛ می‌خواهم چین آرام شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/alonews/120275" target="_blank">📅 23:07 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120274">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1806e8ed23.mp4?token=tDCOsuf-PV8tPDQVPa9AGAYE90vwD_aHfAMw9eOvaJI33TWxoh34Arry5O6fhcnEBnbf1dO1SBVnSq_AVKdr05W8eY3BH9rdJEH2e88Sp8SGJokRt-xOutj8uoBWbyxpoLkvKKXW98Ke1BcGvkJa8divSuPwEyfIst040o4-lwiP2ogVRsFpU4DMcX9xdh2QSeZl1v_2aRp319aaLVgSQMZeG_jOdREA9FvCpQHrwBGODpYrVG1dO11HybZm09IJCdEf6zvTZdBpxLcfXFv-jDtBopr0t0Hzlfr9XMeLSl-JB3FUuRRintaFXQShK73OU7c6Z-pS32V4UGjQvsTHTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1806e8ed23.mp4?token=tDCOsuf-PV8tPDQVPa9AGAYE90vwD_aHfAMw9eOvaJI33TWxoh34Arry5O6fhcnEBnbf1dO1SBVnSq_AVKdr05W8eY3BH9rdJEH2e88Sp8SGJokRt-xOutj8uoBWbyxpoLkvKKXW98Ke1BcGvkJa8divSuPwEyfIst040o4-lwiP2ogVRsFpU4DMcX9xdh2QSeZl1v_2aRp319aaLVgSQMZeG_jOdREA9FvCpQHrwBGODpYrVG1dO11HybZm09IJCdEf6zvTZdBpxLcfXFv-jDtBopr0t0Hzlfr9XMeLSl-JB3FUuRRintaFXQShK73OU7c6Z-pS32V4UGjQvsTHTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برت بایر از فاکس: شما در حال انتظار برای تصویب میلیاردها دلار سلاح برای تایوان هستید. آیا این روند پیش می‌رود؟
🔴
ترامپ: خوب، هنوز آن را تصویب نکرده‌ام. خواهیم دید چه اتفاقی می‌افتد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/alonews/120274" target="_blank">📅 23:07 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120273">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be4f5115bb.mp4?token=rgA_tSTAuUj5fXHSts5tvJTvzqWs8pvYdTQbeflOkfx1owenV6PGF8g9DMDHyEwbn3e_eFkGnTowLyRxyq9GN6MC3Iwf1_XRdbI23VkjLnCKbaZJK9JoIPjJsm_lqtPLrAyg160VpgjTZL1Oihy3U_poa49HlBpZ8-JqxZ8w2bKrGLEfPYWaEkdJerBP07WNphU9NqLdoJ2TT2SVUeml4WaWAhboy-U-35Dt01XEHhrEUwF1eRN5b6sr-FcQ8-xjonRxQ9clYrjant7YeU281bLYhh8L5rOAhgHR4YrYhDEoAzsmYWzy3VbBUxgsJ8mn-6kblfOnd4MVX3s9PEt66w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be4f5115bb.mp4?token=rgA_tSTAuUj5fXHSts5tvJTvzqWs8pvYdTQbeflOkfx1owenV6PGF8g9DMDHyEwbn3e_eFkGnTowLyRxyq9GN6MC3Iwf1_XRdbI23VkjLnCKbaZJK9JoIPjJsm_lqtPLrAyg160VpgjTZL1Oihy3U_poa49HlBpZ8-JqxZ8w2bKrGLEfPYWaEkdJerBP07WNphU9NqLdoJ2TT2SVUeml4WaWAhboy-U-35Dt01XEHhrEUwF1eRN5b6sr-FcQ8-xjonRxQ9clYrjant7YeU281bLYhh8L5rOAhgHR4YrYhDEoAzsmYWzy3VbBUxgsJ8mn-6kblfOnd4MVX3s9PEt66w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سفیر ایالات متحده مایک والتز ادعا می‌کند که «نتیجه بزرگ» سفر ترامپ به چین، موافقت چین با عقب‌نشینی از ایران بوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/120273" target="_blank">📅 23:00 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120272">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
امیر قطر و محمد بن سلمان، ولیعهد عربستان سعودی در یک گفت وگوی تلفنی درباره آخرین تحولات منطقه با یکدیگر گفتگو کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/120272" target="_blank">📅 22:55 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120271">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de25f2d379.mp4?token=KA3Ak0UPOpbBEpYuYqjaiehl-_cI-3de0SvZcxI68KDLqyy3E3i6IJPXM_B95n_oM-MW-YtUDMUQWkWUZhpZII4qqADdOeoEPsT7PulwuJzuv1R06wtf1g6_EhCUUxfjogFBBNELSKsaHLJA5-I5ViC4QY98xIYYPw_Xu6d9jkBnUthURkRqwSxLW6OMwqaulX2p4FJI469QKQFxI1JSZ0Fe-QXAh6XM1AOfg5PkRfceMCx8v-I5SoLRdlHToUttOH83g8N-PYptECirFI_2qpjlfpTBBKLxV8sS-ca0Lj2AXBoyk1-A3QGSXw8L6vvdT5NRNZ7UfYXLF3cQB7NogA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de25f2d379.mp4?token=KA3Ak0UPOpbBEpYuYqjaiehl-_cI-3de0SvZcxI68KDLqyy3E3i6IJPXM_B95n_oM-MW-YtUDMUQWkWUZhpZII4qqADdOeoEPsT7PulwuJzuv1R06wtf1g6_EhCUUxfjogFBBNELSKsaHLJA5-I5ViC4QY98xIYYPw_Xu6d9jkBnUthURkRqwSxLW6OMwqaulX2p4FJI469QKQFxI1JSZ0Fe-QXAh6XM1AOfg5PkRfceMCx8v-I5SoLRdlHToUttOH83g8N-PYptECirFI_2qpjlfpTBBKLxV8sS-ca0Lj2AXBoyk1-A3QGSXw8L6vvdT5NRNZ7UfYXLF3cQB7NogA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
۳۰ روز طول کشید تا جنازه عبدالرحیم موسوی، رئیس سابق ستاد کل نیروهای مسلح ایران، رو پیدا کنن
🔴
پسرش اینو به صداوسیما گفته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/alonews/120271" target="_blank">📅 22:55 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120270">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEd1cD8BBNb_NxyDnmM8GKkjnr1Xfarn7rHMzF2nBwKx5Q5mP1EdEIYMHsDlty9N7tpLeZh0dKof2TErQ2Es70-78RN4OQY59CtPAWOeXMA8caRY0fih1RotkS1MsgT2ip6CUeZeZoJbQibHuK3QYfSIxH-auqC4a8ZbTw4HN2YWSI6SEiAMZuCax-XWvAqUyuEe3F9V7pxI4qCRLCyeE9hago6yaY_zmqCP3ZoyyIHCC3trUjJMZylztJqrcERtx-dzVXjHKU_8Tuyb3jSJmxXAqEZcnTFfoZH_l4dR3cQ21oiH9p7Ns2b9pLh-Y7LZ_nvgjgAkqc_wnFMVvLntUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت جدید و عجیب ترامپ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/alonews/120270" target="_blank">📅 22:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120269">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRg4rFjrpc_e6YEUkQsiwASWtDAr9LqiN-UL90urkVMrlEa3N2XM4_qCQfKCodaaMahxLpyXWzLV4-3cNHiqWb5AEAbVMtdkl8hIVvDeC855wcB-_aGqR9bxhVnaUl9YK8f9SRGbpjFfM_0JlTvFYw5DpiZRrHYcpzOtbs-Rkvz5lwx6bdD5a_-ytypJ57J6eGdvm6q0Hir1_JK4N_FDr0kaPP9v79VZ3tgT1S95Fx1Aaw7_lNmImlm9SpqU_mnrf66XFVfDNyzoIPQwuc4bEV9_twQ8WBfbY54_xj9uKfFapNGFe-4PKkTLpS-l7SmviZXGYFHLE1en_kr-VHnSvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دنا پلاس؛ ۳ میلیارد تومن ناقابل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/alonews/120269" target="_blank">📅 22:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120268">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MMiRFLrTkWzABJ8PQULn9CxQ63PUSBDozbZUyUPSYqL9GCXIrnpTCn5T2lKCoUiWrEQ-S_wl7JIKRj3QkiH6jwoEPjOLof9Oi63AJggy4dkxvtHqMHVS6cPVW2dzn0KP7EqwjBJGVI0Yxg-c9AWeY1GWnVTnq5e3THTP9iVWpCXOIwuwYUSkOcJlEx8vL-7QvjlY8bMXljwBHdRl6MVU-u25jzmfBxXbr2tsO0KY1e-Q95DRGFGYO5bg8imgkCgl5cj89aYcDF0FYKv0BSLXpVi_lgCjPFd9AgXWESnvTSNbIT_zu5qyYvrjUNoTMpZKLenUV4u5WGv0bQIZFOGauw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۱۰۹.۴۳ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/alonews/120268" target="_blank">📅 22:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120267">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/foS5ZIy8riCGyf1Yr4CDc1VCN-lM5COi0uYzi5XIRNmTT5sJvRHaJq4-i6iMnmedZRZAmKgNuKAh5UrZB7FQDEWiYYR3HQhLwant_NElzzhdCW9-lUegiWamGN96bnwKkHpQw4HzRAlDoeeyiPcgOP4nKewf9FJ0am_8PnEB-RqEB7QKhRkvH0bqMOoci7OL5nBCJyIcTxy3wnDcvbegNxjTpeZSGRKro6dk7mPhd2wTliFgKGLHyRbWOJsPcGOb0yarsnhL723u5ZZP0sCCfs-qm4w2SQRWbJuY0Q1WCa58DBRkhEY-KyXIyH2MDQLiOqZMUOpdvd45MVpCfxs5iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هشدار مرندی: حمله ایالات متحده به زیرساخت‌های ایران به قیمت نابودی نیروهای نیابتی آمریکا در منطقه تمام خواهد شد!
🔴
اگر ترامپ به نیروگاه‌ها و پل‌های ایران حمله کند، جمهوری اسلامی برای همیشه نیروهای نیابتی او را در خلیج فارس نابود کرده و زیرساخت‌های حیاتی رژیم صهیونیستی را فوراً در هم خواهد شکست. رکود اقتصادی فاجعه‌بار جهانی تضمین خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/alonews/120267" target="_blank">📅 22:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120266">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AhU_pFOO30wixtdX7p_PSw4xAp7_IdYPsn_aVklIFifValYWd9WRifZdT3Udxwfh5cc9YXit3lXaVNPWe6c8bqYKRiCSBqeUoFLqaze0SW6c_kYRTgMfDmFkJp_YZjH430VuQneNFJWhdGD8Us0uS9kCWQ6w5D3v7rO_Piteb_mszD45PAeLp_nTWo3kh6qOEAJqHAFJ5ZNu944nEvfaPg-t8LcBFVPthfxtGx_11w5NUzyyQVJgKAN2zwv-HiZ1uTYrHFnrtXkyMms10npVHpo2Dns9rMv19lVLfVxqNmsulTkBlh5MyOaXOb_VNPL5A9j4pLyt6pMK7ivuuzRWPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تعیین جایزه ۲۰۰ هزار دلاری توسط FBI برای کسب اطلاع از افسر سابق نیروی هوایی آمریکا که به ایران پیوسته و اطلاعات نظامی حیاتی را لو داده است
🔴
شبکه فاکس‌نیوز گزارش داده است:
«مونیکا ویت» متخصص سابق نیروی هوایی ظاهراً از سال ۲۰۱۳ فرار کرده و اطلاعات طبقه‌بندی شده دفاع ملی را در اختیار تهران قرار داده است.
🔴
او متهم است با استفاده از دسترسی‌های امنیتی خود، هویت همکاران سابق و جزئیات پروژه‌های حساس اطلاعاتی آمریکا را به مأموران ایرانی لو داده است.
🔴
مقامات امنیتی آمریکا معتقدند ویت پس از خروج از کشور، همکاری نزدیکی با نهادهای اطلاعاتی ایران آغاز کرده و در عملیات‌های سایبری علیه پرسنل نظامی آمریکا نقش داشته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/alonews/120266" target="_blank">📅 22:23 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120265">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
الجزیره: هند پس از افزایش قیمت سوخت، عوارض صادراتی بنزین و گازوئیل را افزایش داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/alonews/120265" target="_blank">📅 22:22 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120264">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cf44I_S0nVBflzA74K7G22khL61Deyyks7UADwDrG3pVyV6_CTIg_mImaNet-SoDUjBhNBCIB3H4qyZONjCZgEICmBI7USyFCYMw2qrilYiSimQYvby8TPmnoUHULqaVCRyuAKX7Pj9QOpOwhhVX9mwROAOhLNz4O2vNRHsOJdvzH5pQQzHI6S5pO89H51nxhU3jdG8dON5ksWxWevVfGEd8lID2kZ9RerkLciTsHxraPpXGx6Hch8xAS5jdj4s-Os9UxQgXFHMS7MtJYC7o4tFXCofYfdxL3U2CSXgQCJSntOjJK_clyQXoR1gtCYHz2FppWZwA5-ZRG56a6EJMXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر امور خارجه پاکستان، اسحاق دار:
خوشحالم که اعلام کنم ما در بازگرداندن ۱۱ شهروند پاکستانی به کشورمان موفق بوده‌ایم، همراه با ۲۰ شهروند از کشور برادرمان ایران، از طریق سنگاپور، که در کشتی‌هایی که توسط ایالات متحده در آب‌های آزاد توقیف شده بودند، حضور داشتند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/alonews/120264" target="_blank">📅 22:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120263">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26232c3807.mp4?token=A--mIMy9dz70Cg8GZx7pJUuJnw-utqruA4YcXMA7x7FechtDmqWWaQwpcxXpcLQPk7x45XrbJ6VxE92xlKpWezfbzHbfQPwjPd5F3czdRgTVhp2KK7I5KO3IE2MHqNXlfqMKb81BOtCDXBakaYXsWYvv8ELNicawe6e2m-lz9GFCuwtM-rO1geumQAo9GcgInKaHnkmhMc4yl_3hHPaL4ASfC-ihMSQDbqifiVzbs9lvAnefAeMLnXiedGFswbV6Dfw5FfuhkLa5Sj6pXyHbffP_L5JfARk00ox37-mYjbpZ0s_kmirOZUvI7e6h7h4dL4QAzkpKku6Z-6QRr58DeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26232c3807.mp4?token=A--mIMy9dz70Cg8GZx7pJUuJnw-utqruA4YcXMA7x7FechtDmqWWaQwpcxXpcLQPk7x45XrbJ6VxE92xlKpWezfbzHbfQPwjPd5F3czdRgTVhp2KK7I5KO3IE2MHqNXlfqMKb81BOtCDXBakaYXsWYvv8ELNicawe6e2m-lz9GFCuwtM-rO1geumQAo9GcgInKaHnkmhMc4yl_3hHPaL4ASfC-ihMSQDbqifiVzbs9lvAnefAeMLnXiedGFswbV6Dfw5FfuhkLa5Sj6pXyHbffP_L5JfARk00ox37-mYjbpZ0s_kmirOZUvI7e6h7h4dL4QAzkpKku6Z-6QRr58DeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕️
یکی از صدها موشکی که برگشتن رو سر مردم و جمهوری اسلامی طبق روال همیشه با مظلوم نمایی انداختن گردن امریکا و اسرائیل
🤔
مدرسه میناب جای تحقیق و بررسی زیادی داره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/120263" target="_blank">📅 22:12 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120262">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k59dvWYQywRvYT4aW3Nvi4h8CVURbVhRvB5niOo7vm4OpTbTUddnXaKBhydhsMRVvi7dhxFtUhhgnGAb1rFoGftBrAVsnBZVN-IM_e-u2Z_Ayde7FB0kiAGE58V2MmUiiw3Z8BI5DNeg2zhBCokysrgnlp1jrPGpA4QphjmmXpwyc66eDNKaZp9RP5VQQ6rNbqUPuBn-PHoy4A6raz8RUlEYadXi908UIeT1ALOfwQJPfA1dWwKRYZydDq3fCba2rxsnixe3Eqyjukuvx_fhvThq5EZI0gvRq03kfIhromLx-72KrUOUsGLSX1jDueQE3cfvwC1hSO5FS96b06doKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت جدید و عجیب دونالد ترامپ:
کشور ایران ایالت ۲۴۳اُم آمریکا است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/alonews/120262" target="_blank">📅 22:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120261">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
اوگاندا و جمهوری دموکراتیک کنگو هر دو اعلام کردند که شیوع جدید ابولا در کشورهایشان در جریان است.
🔴
۶۶ مورد مرگ ثبت شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/120261" target="_blank">📅 22:04 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120260">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
وزارت امور خارجه آمریکا: آتش‌بس بین اسرائیل و لبنان به مدت ۴۵ روز تمدید می‌شود تا امکان ادامه روند مذاکرات فراهم شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/alonews/120260" target="_blank">📅 21:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120259">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/120259" target="_blank">📅 21:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120258">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hyRlVB-em-c0kvfXEE9vwrGqYkTdNWmOoKVKdMPrgYat-gP3E6XNAK5x3akJP3PB9cphDNl2EPbc_mC5rAaz57mUFTYy8w5r6igtyX7Z7WfrE-TG7k1fRdzNxJl29-FtXNbJ44RTAo4tEbgd__sAjmEJ543Dd6l6obMVd_uOuo_QnJY_22jFGWUKzhbck3nZ0eiQq-a5BIUhv9qX5dePfNzFg7K_LWw4OFtOiHORDqpmbKaK7L_viN5DSiHkHzX6uXRYqY5BQ6uTuHLxnMECBXc3tQo5Gm6KWPPfGnp-ocJyHDJOpsgftBYMsQMZc6jprSGeRIOnsZpScT1rSxLPvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت خارجه آمریکا : ونزوئلا 7340 کیلوگرم اورانیوم غنی‌شده‌‌‌ش رو به آمریکا منتقل کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/alonews/120258" target="_blank">📅 21:53 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120257">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KmTOFU02dYI3CaAC1-xSdriP0TUhPFr02zywZnbKaRSVbGxdfnRmsd3-l1FXylnHF6szCfYcoFF3HKzQu-QTv0bRs5GHIL4IHODdPfW8tCJc1e0_jBr-cR5QySm4pi8fWxKcHfG1JpQJyicUDt4zbaK1iQ0l0ODteFq99xTALUPeESYXohGiiUPyLlAWujxl_zrlZYv3ms6K9sUo5vKiLiY3jQFxWQDwyGI2bDxDMauqD34ujIzBcSwXJn77IfP4ZAPTyis_EX9__ZAIOh8E_vs7733XStjDCvLsqAbctOhsigxz-wBblzRSs6VtlmG6bUDUVyxjT4V7iGk0CU2R2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوروش وی پی ان
👑
ارائه بهترین کانفینگ های ایران
👑
👑
👑
بدون ضریب
🤴
👑
👑
👑
همراه با لینک ساب
🤴
👑
👑
👑
پرسرعت
🤴
👑
👑
👑
همراه با لینک ساب
🤴
👑
👑
👑
۵ سرور متفاوت
🤴
👑
👑
👑
همیشه در حال اپدیت
🤴
👑
👑
👑
کانفینگ های رایگان
🤴
🦁
توجه کنید شاید یکی قیمتش ۱۵۰ ۲۰۰ باشه ولی هر قیمتی دلیل بر خوب بودن نیست بلکه ضریب دارن و یا سرور های کند دارن!
🦁
تنها چنلی که کانفینگ رایگان میزاره  :
👑
https://t.me/+nVsNnhQep1s5YTA0
👑
👑
https://t.me/+nVsNnhQep1s5YTA0
👑
👑
👑
👑
خرید از طریق ربات :
👑
@CyrusV2ray_bot
👑
@CyrusV2ray_bot</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/120257" target="_blank">📅 21:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120256">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/575f6be6da.mp4?token=FL_zxyeEpLoT17tF-6r4S7l225pUsnmDCP6eKaottRk0SIbhvHWojhfyKNVuupZIj-Q1GK5XcdG1t5lfXCB8Q3aWDxgQ7vQypWrVAzCNLNLfX27qX6QBK_mhk9LzjuF0Q1NMPmCj1_U-XB2RNznITMJkJE8_KVnRiF9z5LoU74b44-hm2PjZ0hI9b3tiizSbDlhnzW7bDnzi7pG8R77XQGJBiOKKBooCanP3Xl3f5Pm1T5jTEs-aWBZdZHSs9Tzjk-ojKFrVMLq3nMefn-kpJp4mU6U5fu4vVvQBviP2BFPymuD2L6uIFoLEChuifocuLnwt1WYtK7MBqS9WDlXo_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/575f6be6da.mp4?token=FL_zxyeEpLoT17tF-6r4S7l225pUsnmDCP6eKaottRk0SIbhvHWojhfyKNVuupZIj-Q1GK5XcdG1t5lfXCB8Q3aWDxgQ7vQypWrVAzCNLNLfX27qX6QBK_mhk9LzjuF0Q1NMPmCj1_U-XB2RNznITMJkJE8_KVnRiF9z5LoU74b44-hm2PjZ0hI9b3tiizSbDlhnzW7bDnzi7pG8R77XQGJBiOKKBooCanP3Xl3f5Pm1T5jTEs-aWBZdZHSs9Tzjk-ojKFrVMLq3nMefn-kpJp4mU6U5fu4vVvQBviP2BFPymuD2L6uIFoLEChuifocuLnwt1WYtK7MBqS9WDlXo_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کاوه مدنی: وضعیت دردآور جزیره مارو (شیدور) ملقب به «مالدیو ایران»
🔴
نشت نفت به خلیج فارس پس از حمله به تأسیسات نفتی جزیره لاوان در فروردین ماه عامل این فاجعه بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/alonews/120256" target="_blank">📅 21:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120255">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
ایلان ماسک : برنامه "اینستاگرام" برای دختراست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/120255" target="_blank">📅 21:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120254">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e2c4db2b5.mp4?token=Qp5YACgnCmZn7PyahcbwlyBsS9lTN8oH-nsK_m5G6kigsYXAl4TzVTS-nO6ce8oniNnT-_fszk_ynqzhcsJJVHxlYs2Jqb29EjCGGU_D2bXHH4CchsaoZvhvY1EEmtXYbdm7bNyO1_RjOB0L272UifPsMktFO0p5z6mGGwGgHBIglSrIRu9q_uwoC7s_6s6Cy5fYbl51Mm_5mCEPypPEMZb6k9bJtW36cpAGbweL-z5p4nVYQ_NQkaW6cOXW-3tx9M0TcDmOfdyGptHBzFX988U4_M-VQqVsbi-iCYqRC1okuNobDJlFVGwwRbWkG2rO0dFdTJF08YSDA8HeKVdmBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e2c4db2b5.mp4?token=Qp5YACgnCmZn7PyahcbwlyBsS9lTN8oH-nsK_m5G6kigsYXAl4TzVTS-nO6ce8oniNnT-_fszk_ynqzhcsJJVHxlYs2Jqb29EjCGGU_D2bXHH4CchsaoZvhvY1EEmtXYbdm7bNyO1_RjOB0L272UifPsMktFO0p5z6mGGwGgHBIglSrIRu9q_uwoC7s_6s6Cy5fYbl51Mm_5mCEPypPEMZb6k9bJtW36cpAGbweL-z5p4nVYQ_NQkaW6cOXW-3tx9M0TcDmOfdyGptHBzFX988U4_M-VQqVsbi-iCYqRC1okuNobDJlFVGwwRbWkG2rO0dFdTJF08YSDA8HeKVdmBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عضو کمیسیون انرژی مجلس: دولت به دنبال افزایش قیمت بنزین است؛ مجلس مخالف است و اجازه نخواهد داد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/alonews/120254" target="_blank">📅 21:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120253">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
رضا پهلوی: هرکسی که در ایست بازرسی کمک کند و یا برای نهادهای امنیتی خبرچینی کند و یا اموال مصادره شده معترضان را خرید و فروش کند؛ در فردای آزادی مجازات می شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/alonews/120253" target="_blank">📅 21:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120252">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
عراقچی وارد تهران شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/alonews/120252" target="_blank">📅 21:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120251">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
رزماری کلانیک عضو ارشد موسسه Defense Priorities: به نظر می‌رسد ادعای مخالفت چین با دریافت عوارض در تنگه هرمز فقط از سوی منابع آمریکایی مطرح شده.
🔴
خود چین چنین چیزی را نگفته است.
🔴
تفاوت بزرگی وجود دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/alonews/120251" target="_blank">📅 21:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120250">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJFC4McTt_IDFD31ncEXxO0dYb9KvUOqY8bma0YRgwIUvKAg6mZrxcvkn8CrYrxjx1SpOOaiXtRHYx1wTF9RU1xUAzslAgz1RO7j1-9pSpKQ9orLJ-xOnfM7I73wdRUI0UpO7dL1zb-WST9fys2igCCrUiXUEUuCrWhTsFjdK-454v62kytjaST6WxsCcyMN0oeikkmAhqTLwylxkXJXVDzBhB8bf8fL0TGAAVw8OsKjDAwtkBQKd5GO0TiLRqVaiZelTD_2_7BnwQ25rh5FTtfgRQmLsc5sPwEoRgBZiYlGWzaVOEnTNp9_QqAZLmueK7_u-OZTIdTujRIpvDlK0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چادی هوپان : ما با زحمت و هزار دردسر به قله رسیدیم، نباید بازیچه دلقکان مجازی شویم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/alonews/120250" target="_blank">📅 21:22 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120249">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
امارات متحده عربی روز جمعه آنچه را «تلاش برای توجیه حملات  ایران» خواند را غیر قابل قبول دانست. این واکنش پس از آن مطرح شد که تهران این کشور حاشیه خلیج فارس را به ایفای نقشی فعال در جنگ خاورمیانه متهم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/alonews/120249" target="_blank">📅 21:17 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120248">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
رئیس جمهوری‌خواه مجلس نمایندگان آمریکا: عملیات «خشم حماسی» آمریکا علیه ایران به پایان رسیده و ایالات متحده هم‌اکنون به دنبال بازگشایی تنگه هرمز است.
🔴
دولت آمریکا در حال حاضر به جای اقدام نظامی، در حال مذاکره با ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/alonews/120248" target="_blank">📅 21:12 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120247">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0d07cbc7e.mp4?token=bf7o4-lTDk2hi-lJJUZslArbx0VAT3PMME6O64JN3Z-9xvAwk43dhAaDrROvu4jKn8USEmwdQFeaTyPs-fEaPGqzyWOkZM5OEK2ApDgFiB0HtKKPTCR9ifye6KdqG-_oRVaCESsWCFk05vQJL-ZB1JItlCvuccks7FMcarT6nZ3SzrBwwSyR7XqpkKdv73opsIgyt6EEThND5QzR0rqz88jNfpGSaBB4GPaRT7W9rdEVPk_6tsRZsPbtP-ZXvt1ite3odWLrWTGiwtWcjf9Ze5u9GNzqT1LQEj1ke1PPRx0S2gR-yfnl7chB5LEch-vrKk_gKRGH1pczX2Q6HmtAlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0d07cbc7e.mp4?token=bf7o4-lTDk2hi-lJJUZslArbx0VAT3PMME6O64JN3Z-9xvAwk43dhAaDrROvu4jKn8USEmwdQFeaTyPs-fEaPGqzyWOkZM5OEK2ApDgFiB0HtKKPTCR9ifye6KdqG-_oRVaCESsWCFk05vQJL-ZB1JItlCvuccks7FMcarT6nZ3SzrBwwSyR7XqpkKdv73opsIgyt6EEThND5QzR0rqz88jNfpGSaBB4GPaRT7W9rdEVPk_6tsRZsPbtP-ZXvt1ite3odWLrWTGiwtWcjf9Ze5u9GNzqT1LQEj1ke1PPRx0S2gR-yfnl7chB5LEch-vrKk_gKRGH1pczX2Q6HmtAlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از حملات به یکی از پایگاه هوای ایران طی جنگ که نشان دهنده انهدام تعدادی از هواگردها درون آشیانه و همچنین هواپیماهای فوکر نیروی دریایی بر روی زمین است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/alonews/120247" target="_blank">📅 21:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120245">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NsV2oJoPueg0VgyF9VkhBXuwjD9I1mgzeGl6MHx9XAq3OEAhI6UbXqAzEoALuMq-m2FCxIQmtRxHMH0C3KBN_S2nJMPfSVoR6XNpKUY3qsv4hrY5vr6kkUjY3ogDmNVqO0D4TnoMciy8_5e_b3rNwxz4u7E2dA8-SyQnRNtgBQGmzhCGmbOr8KQ7NYiGIPPvVEoK72t_TiA8_MLc9GfLqR8sU7IhQTcDh1DWxh1YbPLlsIZoTT1Z31WyMuoGl2dzKnXp-p9SLwiJ9UDQsqQ3lPD35PwtN4jFUX7RTK1PdTX6tLtlPvM0_yY4THUCFxelciOA4ca68ezEsT_hTRyTjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7ab41979c.mp4?token=ntWigK-VJOcs9fWHcCl0RN45uqR1xx_kL-ivMqpLOXBDam3felhruXt5jZqUzcSppFZQeK1Oke43Pl69OFcEjkJMTQRV-FgT1gARUJYp-bcSjF2T39IUCLdMh0eJwdZeKHnGJ70nSgqkaMqlB9CHPsP9rTHlfM7GLqYZ48HnINXT-49VTD1rlKXLDUR5AxDzmtYwTqhgEona1s0CEu1Y2XQYEy_70qhoPIijQMRMO0c-nkLx-BrjayXogcDobjg0x2NO9ll50gjBzCLDJjbf0OojU82bQgTDMVQ9PwvE5FHp5Bv5vCWCnjfQ5LVW3tLHhWQHLg-Eayk2UFnJtY6Vpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7ab41979c.mp4?token=ntWigK-VJOcs9fWHcCl0RN45uqR1xx_kL-ivMqpLOXBDam3felhruXt5jZqUzcSppFZQeK1Oke43Pl69OFcEjkJMTQRV-FgT1gARUJYp-bcSjF2T39IUCLdMh0eJwdZeKHnGJ70nSgqkaMqlB9CHPsP9rTHlfM7GLqYZ48HnINXT-49VTD1rlKXLDUR5AxDzmtYwTqhgEona1s0CEu1Y2XQYEy_70qhoPIijQMRMO0c-nkLx-BrjayXogcDobjg0x2NO9ll50gjBzCLDJjbf0OojU82bQgTDMVQ9PwvE5FHp5Bv5vCWCnjfQ5LVW3tLHhWQHLg-Eayk2UFnJtY6Vpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
محل ترور عزالدین حداد فرمانده گردان های القسام در شهر غزه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/120245" target="_blank">📅 21:04 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120244">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
رضا سپهوند، عضو کمیسیون انرژی مجلس: یه دلیل بمباران جنگ، روزانه ۳۰ میلیون لیتر کمبود بنزین داریم و در کوتاه‌مدت هم امکان افزایش تولید وجود ندارد، راهی جز صرفه جویی نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/alonews/120244" target="_blank">📅 20:55 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120243">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFeip4HpWu_4Zot3f6C8jTGHgnyE3BV3tojhcO5TP1BHNsIhg2iFPQ4fjT-yLaPgd9-NeS6CGZ1gEtHgepKUDGaDU0z04kmRiW9UJzQHwkJ3lvrXshI3wK8_qh091ZMbYCRZa71qJeEos-lasiem3FszjXAhYhErVrhWrlXMRL3Mk6_LfyuT3U6YOuqly1eeu5vgT3Bt2rY4KQX8Eafim5Ap0__EUd-fhEWf7soBNJTKyqb5wJ7AUaa85lY8INghAEO6CQ8IEBkKY_etp_-9yvrvDKZRSpYVkKSbSB7zbNDOP64Ursi71J965Wx7vq26vSJ6uEjt6Fy6yah5vI7iPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / ارتش اسرائیل : عزالدین الحداد فرمانده گردان‌های القسام، همراه با محافظ‌هاش ترور شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/alonews/120243" target="_blank">📅 20:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120242">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
رسانه پخش اسرائیل: تصمیم از سرگیری جنگ در ایران هنوز به رئیس‌جمهور ترامپ بستگی دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/120242" target="_blank">📅 20:49 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120241">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
کانال ۱۳ اسرائیل: سیستم امنیتی معتقد است که ترامپ با حمله‌ای محدود به ایران موافقت خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/120241" target="_blank">📅 20:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120240">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
آتش سوزی در تاسیسات گازی در ونزوئلا
🔴
رویترز از آتش‌سوزی در تاسیسات گازی تحت مدیریت شرکت PDVSA در دریاچه «ماراکایبو» در ونزوئلا خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/alonews/120240" target="_blank">📅 20:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120236">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5Qgrt4nqoe700bm1lQ8vkS-H2HJmU8c_YtUYDMs0r6n1YXDChMtyTlPunB_LCIvMS9IS0i_XVCWc0ycLOfz36-JQe7SQpJc6f-ima4b_Kq8oTuVNA345kiYfmf7mhq8_zn9H3eU9n3-M7BfOIwjNc69fTCe6r7Sc2XO0G1OK8Lp9xLAwQn5pJX7g5UlWgom0-kZfIO_GPJP5ayVg_R_vTKf2Seuh3eSofEA0KAgAWB_YVHFSuIMAGcn7zIGqiySMpS1uCL8lKUD-AJm5zpWZjrl05W2tkgnfI7LXIGJ_dni3lBF656rdf7ZGRnqohqKIakyqsTuThstjwb6Od3RpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5424fe043f.mp4?token=KdBpsx8OQwg6k5tTsL4Iv-0o1mQvwDWSmOgUF2X6X6BszrjGfjUS1OCyCHjeFUXMNw-Wm2mtizBJS_ERA7E8kLd7VbhEsPIbwbQO0XruLBarXWhs18vsUQSZ-1x9_o0w1OSWLTyk4x-OW33f1_6yY33a4yViJBrccPVYdWQ-GL0XMhKfdUWzgtRZ8IpAJTVTnIJ95Bw7JaqkpGyxQT9NGAX2-scd4UP9wb4v5e5syrIB-Hksn_WlRc_DGfng2P5KtqLI25LTQ8cE72N2bFjEe5KsSnmeCvfWvB5FtOLE3LJv7pNIHVl2MGlCQBf1LBLhxTkY7QYWZxJhkMOIp6iKnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5424fe043f.mp4?token=KdBpsx8OQwg6k5tTsL4Iv-0o1mQvwDWSmOgUF2X6X6BszrjGfjUS1OCyCHjeFUXMNw-Wm2mtizBJS_ERA7E8kLd7VbhEsPIbwbQO0XruLBarXWhs18vsUQSZ-1x9_o0w1OSWLTyk4x-OW33f1_6yY33a4yViJBrccPVYdWQ-GL0XMhKfdUWzgtRZ8IpAJTVTnIJ95Bw7JaqkpGyxQT9NGAX2-scd4UP9wb4v5e5syrIB-Hksn_WlRc_DGfng2P5KtqLI25LTQ8cE72N2bFjEe5KsSnmeCvfWvB5FtOLE3LJv7pNIHVl2MGlCQBf1LBLhxTkY7QYWZxJhkMOIp6iKnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چندین حمله هوایی اسرائیل چند لحظه پیش یک آپارتمان در محله ریمال شهر غزه را هدف قرار داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/alonews/120236" target="_blank">📅 20:39 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120235">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
مرکل صدراعظم سابق آلمان: خروج آمریکا از ناتو به ضرر خود آمریکا است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/120235" target="_blank">📅 20:36 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120234">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NatvjDglYvMmArWMLa_Fzae-52Ms3lB_R8TRwcV11bWYMUjraYUCp06QTylnI6wvlU5zltjw_MBVK74ybb_Lwj7-cq-QHcSRN1pnMMy7Q1XrM8j6sjrWlbwknm1CFOqPTmxUDX4KvfGfQ8tcMRSImjhgLbhLtHVjUO18km1cZVq4LH5dcXxIhKBESI1Tp0w0_AdwesACZ26T2lgTVtnZCzO8A4zMhUDV1O_68bNNlwxwQfHNDjX4hqO1zwFItTSs8w1z_TecN4r2o90KyG16mnTLuDCiYeY53F8uPWRdcnBnAVC2nucalokPxqQyyxTzqieueCBah8J_vK0T-KnwwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ چند دقیقه پیش از آلاسکا به سمت واشنگتن پرواز کرد. پس از توقف برای سوخت‌ گیری در انکوریج
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/alonews/120234" target="_blank">📅 20:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120233">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlJUzKpslg-UyiwPsE2O0eJpDchzhfRLYoyfRfsvnU8lQUJuQH_0eu9EUzMMUfcR1KHSkI5RZ0C_UX5Je3SQIPEKNoA044qS9GTLGVYTGa67QEeLPVBwbiRo1v9dRFOI2y2GVrC3wEhAMR062wDxNCdXZtDpFL_YbP7DxRgl1gJ2e0LI8OeF9rKfxyPqdyjWstdGynnG9OU3AdesOe9xxfyK2ore9V8ceAWj95BYOEzFQQAkw0p1E4nxjLpw6k2DFJ92Itrknq6WlP2cK0-Pm5R7FHEUB4vkG-PgFlUTIJLyTBTFQNF4dJS-nRcEklwhzK0uFFkh54Rt55sxmtCWQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاهش چشمگیر تولید نفت کشورهای حاشیه خلیج فارس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/120233" target="_blank">📅 20:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120232">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
کانال ۱۲ عبری: حزب‌الله در عرض یک ساعت و نیم، ۱۰ پهپاد به سمت اسرائیل پرتاب کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/120232" target="_blank">📅 20:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120231">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
قیمت جهانی نفت به ۱۰۹ دلار برای هر بشکه رسیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/alonews/120231" target="_blank">📅 20:23 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120230">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
علی واعظ عضو ارشد گروه بین‌المللی بحران به نشریه فایننشال تایمز: ایران با موافقت برای عبور نفتکش‌های چینی، به صورت پیش‌دستانه توانایی ترامپ برای چانه‌زنی با چین بر سر باز کردن تنگه را خنثی کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/120230" target="_blank">📅 20:20 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120229">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
منابع اسرائیلی و آمریکایی به کانال ۱۱ اسرائیل گفته‌اند این کشور در پیامی روشن به واشینگتن خواستار از سرگیری جنگ با تهران شده است.
🔴
براساس این گزارش، یکی از گزینه‌ها انجام حملات محدود و هدفمند علیه تاسیسات سوخت و انرژی ایران است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/120229" target="_blank">📅 20:17 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120228">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
سفارت آمریکا در اسرائیل در حال بررسی صدور دستورالعمل برای خروج فوری شهروندان آمریکایی از تل‌آویو است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/120228" target="_blank">📅 20:14 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120227">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
کی‌سی.سینگ سفیر اسبق هند در امارات، درمورد افشای سفر نتانیاهو به ابوظبی:
🔴
«دولت اسرائیل می‌خواهد مطمئن شود که رئیس‌ امارات، محمد بن زاید (MbZ)، آن‌قدر از نزدیکی و تعامل صمیمانه‌اش با اسرائیل آسیب ببیند که دیگر نتواند با ایران به توافق برسد یا هیچ نقش مستقلی در شورای همکاری خلیج فارس (GCC) ـ جدا از اسرائیل ـ ایفا کند.
🔴
با توجه به اینکه من بن زاید را می‌شناسم، این موضوع برایم ناراحت‌کننده است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/120227" target="_blank">📅 20:10 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120226">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز: من تاب‌آوری ایران را دست کم نگرفتم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/120226" target="_blank">📅 19:58 · 25 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
