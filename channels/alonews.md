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
<img src="https://cdn4.telesco.pe/file/dwZbFyAdL54vlTBLUUxV0mghyeE0dOLbv4XHH1_Xn9lDEwb1L5yhzv_wRnHqPIUeyhwzm6zpPthsNI7CFw6_XDqJRb8wux9jU7TVh3DxkptjTWRGIWr0Td_fFn_F1_QCIHNoz8fF3KDaGSVH2aL0hfJAdZH-rLqyrnrnN2bEk1yYRmNSnGNmd-xdEcrruSd5d-I0ARstqwRkSI-R33_jmQb-neA9CxYGiFuSy5d2_sgXA8hPXa1-Ko7f0fjTCvgh2evvfTTlzlsjt0gewOaM4uCabowKDnxwpMVgOSWmqeMmQIXdwfgmIzYDuvGcorpwJqHrjEBZSHUGASY9YDiFvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 944K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 16:18:20</div>
<hr>

<div class="tg-post" id="msg-134414">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
فوری/رمضان رحیمی عضو کمیسیون آموزش: کنکور سراسری در صورت ادامه‌دار شدن تنش‌ها، به تعویق خواهد افتاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/134414" target="_blank">📅 16:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134413">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5c5356b55.mp4?token=VYoTzrLU6jBEnmCmY_lHPOFiR3F6pUxi2p1pQ90CmMTGCGqIrHkAaWhCv0uVD1DulWcpcYCc6WYm555M9gyj6YMVn-lSE_kduPYAnZKQpZJiH8PDHXHZE7FIkrwVwFmvxr5GG8PfVf_8ECqFXm5fRRV4uCnJQjsyfjSG7QAo9v56_eK1Kcoa40rmrUvgf6yOzdjK_AYmCmso6NTeGA1tM_-YGh9QZsIdPziaieNTGwxZYkwvSrA-J1PTHKm3_9hY6kVOPXIRPJl4TTdHU6kVcEWi7f_ZJKM570QlBQCptOfXU4Iu5aCM2Q7w4n9t5e1HfhosaDVIUTWF4ZrYst2bew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5c5356b55.mp4?token=VYoTzrLU6jBEnmCmY_lHPOFiR3F6pUxi2p1pQ90CmMTGCGqIrHkAaWhCv0uVD1DulWcpcYCc6WYm555M9gyj6YMVn-lSE_kduPYAnZKQpZJiH8PDHXHZE7FIkrwVwFmvxr5GG8PfVf_8ECqFXm5fRRV4uCnJQjsyfjSG7QAo9v56_eK1Kcoa40rmrUvgf6yOzdjK_AYmCmso6NTeGA1tM_-YGh9QZsIdPziaieNTGwxZYkwvSrA-J1PTHKm3_9hY6kVOPXIRPJl4TTdHU6kVcEWi7f_ZJKM570QlBQCptOfXU4Iu5aCM2Q7w4n9t5e1HfhosaDVIUTWF4ZrYst2bew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رسانه‌ها از وقوع انفجار یک تانکر حامل گاز در منطقه الهرمل در شمال لبنان خبر می‌دهند.
🔴
جزئیات بیشتری درباره علت انفجار و تلفات احتمالی هنوز منتشر نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/134413" target="_blank">📅 16:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134412">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
رسانه i24NEWS: انتظار می‌رود که دونالد ترامپ و بنیامین نتانیاهو روز دوشنبه در واشنگتن با یکدیگر دیدار کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/134412" target="_blank">📅 16:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134411">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUWuOuiW6GPslRx5ycgIDBAF0jdpXASHasDa24uA7uRCs7zJeMFYadkjAr99V_n8uOvDK5b8ingPaUfUHwxpAZMdMwG3ZJ_uTJvR_el2zMrBOUEe60ogP43cTUZD0IiS3VncHv3_ibOPreIhgzIG0JgQpXt1DTPAwN3weazo4pdX7_bzgu71N-dOukubjqWkbTkJXfY-HDiT35R3UqdKXl-8y9H_pCrzzy_x5WrTa31-Fp5B6_235bYkQp-JYgMuDx7r3fJTR8l1AtXgX6LQY-Jb8L9ITrUcBv0Jl8ckdrEKkL6or4EFbNgTQ-7ZRW-OFSr9OkuVHtqQK2VhjX8cnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حضور محمود احمدی نژاد در سفارت قطر در تهران برای عرض تسلیت
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/134411" target="_blank">📅 16:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134410">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
ولایتمدار، عضو کمیسیون امنیت ملی:
به‌زودی دولایه از مسئولان آمریکا و اسرائیل را قصاص می‌کنیم
🔴
مردم نیز خود را برای تحمل شرایط سخت آماده کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/134410" target="_blank">📅 15:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134409">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
سنتکام: در طول موج حملاتی که به مدت حدود ۹۰ دقیقه ادامه داشت، فرماندهی مرکزی با استفاده از سلاح‌های دقیق، سامانه‌های دفاع ساحلی و همچنین پایگاه‌های ذخیره‌سازی و پرتاب موشک‌های کروز در جزیره تنب بزرگ را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/134409" target="_blank">📅 15:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134408">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
یک هیئت ایرانی از تهران عازم قطر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/134408" target="_blank">📅 15:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134407">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
ستاد فرماندهی مرکزی ایالات متحده: تکمیل دور جدیدی از حملات علیه ایران/سامانه‌های دفاع ساحلی و انبارهای موشک کروز در جزیره تنب بزرگ را هدف قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/alonews/134407" target="_blank">📅 15:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134406">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
صدراعظم آلمان: ایران فورا باید وارد مذاکره شه چه در بحث هسته ای چه موشکی، و تنگه رو هم باز کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/134406" target="_blank">📅 15:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134405">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
عراقچی به قطر سفر کرد
🔴
عراقچی به منظور شرکت در مراسم ادای احترام به حمد بن خلیفه آل ثانی امیر سابق قطر به دوحه سفر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/134405" target="_blank">📅 15:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134404">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
رئیس مرکز ملی اقلیم سازمان هواشناسی: موج‌های گرما تا پایان مرداد ادامه دارد، اما از حدود ۲۰ مرداد به‌تدریج از شدت گرما کاسته خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/134404" target="_blank">📅 15:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134403">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
مدیرکل شیلات هرمزگان: با وجود شرایط حساس کشور، روند صید و تأمین آبزیان بدون وقفه ادامه دارد
🔴
مدیرکل شیلات هرمزگان با تأکید بر تداوم فعالیت ناوگان صیادی در تمامی بنادر استان، گفت: با وجود شرایط حساس کشور، روند صید و تأمین آبزیان بدون وقفه ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/134403" target="_blank">📅 15:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134402">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/jPKnDi7tpc7NCWf0jpR6K5c8CF75Ny1cp6f9-KUgF8DXb5wMgfTKJtIVpDA8gQzCDB3-aQnVH2XwBlHnO1UOSUaBXdXuWqWsKUXDZmV92G2ZWPARZaETgkPZ8S3fC4F_2SFe3Q5g4cZJzyLOdQlNN9DTavjohWiubLlxwA_lt_A-mvtr7bR9ZmqfIIsV-bDVtPWosBLMBVK0md5M6o-RJHvEJhj0bscNmrWwDV4RbkaD3FdivxTXmhud2H2LdgFqZchR-dUBoJwOLgPEcgfSkw6IiyWfdRGUqLWqVaM2mQ_XqWMo5yWlT3SdLrIC51C_20Pa9R8_uMUPRgTc1_J-3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هیئت ایرانی از تهران عازم قطر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/134402" target="_blank">📅 15:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134401">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔹
🔹
یه چیز عجیب و خفن پیدا کردیم...!
👀
🤖
وقتشه با یه ربات هوش مصنوعی خفن آشنا بشی
😻
✍️
نوشتن متن، کپشن، خبر و ترجمه
🖼️
ساخت عکس با هوش مصنوعی
📦
ساخت موزیک و آهنگ با هوش مصنوعی
🧠
پاسخ به سوالات، ایده دادن و کمک در کارها
📚
خلاصه کردن متن، تولید محتوا و کارهای روزمره
🚀
سریع، راحت و همیشه در دسترس
✅
فقط پیام بده
✅
درخواستتو بفرست
✅
تو چند ثانیه نتیجه بگیر!
اگه دنبال یه ربات هوش مصنوعی کاربردی، حرفه‌ای و همه‌فن‌حریف هستی، اینو از دست نده
👀
🔥
🤖
لینک ربات:
@AIBotLabb_bot</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/134401" target="_blank">📅 15:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134400">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
نخست‌وزیر مالزی:اسرائیل را به رسمیت نمی‌شناسیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/134400" target="_blank">📅 14:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134399">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDmjcUDvkF_cZ28YeC4qjwMukd2Y_SFlaP8d9aTA4Xb6s1IpkhRwcq4DHH4KZJGogRlAM2dkGWR3-EA6b71BuiocHFDlJELeUCtJ9WnF26hyBwQiY8VHn7_0RZSEwgz0UFrdjVXsy-Pir3yJbHmr5wPQcPJzwUWRd9JR1ZEbkQmwWCADwFYg9ZgxAQrYMYE-6YSrkl6tNpbx4pau1rla4Ud9whnn-7_-G6vPWsEBUGrorazUPhcL5W3Wvigbk88POCvN2E73YvcENgKLZaF0mK7Wz3OWrEytg5zilDIqyZn-YJS0ce31NeVuX16ORxhGiBcyeE6QXNvyl0gFnRhfrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بابک زنجانی: یک میلیون پیام سین نزده دارم
!
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/134399" target="_blank">📅 14:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134398">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
وبگاه آمریکایی پولیتیکو: میانجیگران منطقه ای بین ایران و آمریکا، پس از تنش های چند روز گذشته، فعالیت چندانی برای کاهش تنش نشان نمی دهند، چون فکر می کنند ایران و آمریکا قصد دارند طی چند روز یا هفته آینده با  زورآزمایی در میدان نظامی شرایط خود را برای مذاکرات احتمالی آینده، بازیابی کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/134398" target="_blank">📅 14:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134397">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlmToZur6tZVHnJoSGUtk1FpjEi2H866HGST6wEvQdaa2Khjp6u7JnpoQJ5qRQh6GL1Hvybs6vU0VpMccPRiKuZu2g8ZDiEujbV65i6E5KjvlITgfpoWbuyeMNu4KDLDEt8_K6UZAZ2dVrbaiqK-i2P70x8JYY67XpcjTF2GSI7sKeYb_Nn2bWPMvnKAU6pNEnl8khM79giXUZUf15vuLba4XBUzBxFo-RVha_3Ld9C5PFaJAXYhpLGKHEmzXbL7YDIp0cZtFVG9Cnuw2UGUIZW4uwT8PcDlZxacgnyXKroZKsN5IAVh0u5JUTorSAMYTQ1Gmvu_qHshy0f_i-FieQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث سوشال: خبر عالی برای آمریکا! تورم ناشی از دموکرات‌ها بسیار پایین‌تر از چیزی است که بود، و ما آن را باز هم پایین‌تر خواهیم آورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/134397" target="_blank">📅 14:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134396">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
وزارت بهداشت: واکسن HPV فعلاً به سبد واکسیناسیون رایگان کشور اضافه نمی‌شود و اولویت وزارت بهداشت، تأمین واکسن‌های فعلی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/134396" target="_blank">📅 14:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134395">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
وزارت نیرو: جدول خاموشی منتشرشده برای تهران مورد تأیید نیست و شهروندان برای اطلاع از وضعیت قطعی برق، فقط به سامانه «برق من» مراجعه کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/134395" target="_blank">📅 14:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134394">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
پولتیکو: تلاش‌های میانجی‌گران برای احیای مذاکرات، هیچ نشانه عمومی از پیشرفت نداشته
🔴
احساس کلی این است که درگیری فعلاً ادامه خواهد یافت
🔴
یک مقام سابق آمریکایی: حملات ایالات متحده بیشتر یک پاسخ تاکتیکی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/134394" target="_blank">📅 14:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134393">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q148rjwLg2ZkNl1Ik91UdocChRpVvnrD3emwPUln4g8txWdhP5evfSO8ZsFsVS_yE6dkEUR6Cdm8k8LGw1u275LAoWjHjw6pKL4eua3xv1s6gMA9zxn_4svh78fZ-k4U8NdAyUiqUpli4m6rDwn-dQgH2bgeEiGLJXY1SvE0rZDPQfFX0JT6IjCfnudVu9XLaclSrOaea-M1HeWECCKP-xzL7of0pPJTuoa-pQTjxBHv5_0HzopdxHsuVXjT4_2hAPth20JR9LVuWmjM-Kr3FG1RtE_kiTG9nPb3jrxmElfTFdegAKr-STpwd2wVpCNFTNmIJ___y5LnMGxWXibhNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا از ضرب سکه طلای جدید یک دلاری با تصویر ترامپ خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/134393" target="_blank">📅 14:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134392">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Btch0V0SGONLpbWm6LqO0AK1P5kHzYEdefHw8uJnarec_BvXV8nUN0WugvzbJamHWvezEc-M_eNcuPksseOonALURMuxrwPLxsGhG_IqpoiEbt9tYMLnKPMknc2DpCssEQZSHRQaovtxKLQpCvviD0vhvy8ZWSVL43bR7IDBw0YW8FT-cTGffySC79OffbqO4KgKkmCyvb8QhO9ZTbLHZEeslyaUiPjBZGOAEOToUKgchR75AngObY_OZ40JbZeyBjs72sHpF_kQFW-HkB9JL7PNycvjZu3o5xCzsYc3yyzXNmLthGDDBxqGmkqM5KVBJmTIYQ2qKSz-Ssh2EB0PJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سالار ولایتمدار، عضو کمیسیون امنیت ملی مجلس: مردم خود را برای شرایط سخت آماده کنند. ممکن است با محدودیت هایی در تامین برق و سوخت مواجه شویم و به این دلیل مردم تحملشان را بالا ببرند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/134392" target="_blank">📅 14:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134391">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
فوری/امتحانات نهایی رشته های تحصیلی پایه دوازدهم در ۴ استان لغو شد
🔴
بر اساس تصمیم ستاد عالی آزمون های این وزارتخانه و با توجه به شرایط خاص کشور در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، امتحانات نهایی تمامی رشته های تحصیلی پایه دوازدهم در روز پنجشنبه ۲۵ تیر و شنبه ۲۷ تیر لغو و به زمان دیگری که متعاقباً اعلام خواهد شد، موکول می شود.
🔴
امتحانات نهایی سایر استان‌ها و امتحانات بعدی استان های مذکور، بر اساس برنامه ابلاغی در موعد مقرر برگزار خواهد شد.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/134391" target="_blank">📅 14:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134390">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
هاآرتص: ایران کنترل تنگه هرمز را در دست دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/134390" target="_blank">📅 14:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134389">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEshHmbr_BX_ErttcDarBA2D4OHLIRsvElVtmmQyYIQsWykIbOyBoi_axW70JKdDlLPCPaL7-Ybcrt3R5jJ8pjOD3Hgy15y4tY3k4eVHpEwrIQ-xQ8sfxbQhUePiSHxjInZ-GbhlhEOiHDKwe6Q6ndj61GBnvoi49Fw0sjJdE_S5dMiBPSgUud3ZLb70el8bpXbE0NDY6GdXfWNeXJSH-DMWgfANjICe-EMBCGcDFg4INF_aBw8hmupN6YSQqsJSS2yXHsMstrjHVD3PzA-237HvsxefRr9JJgNju6F4JLkVBM0dj4xCe_Ul2U_1e5qQ5J8DjY-XvKkFqwEjz1sycQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عامل نابودی ایران= j2
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/134389" target="_blank">📅 14:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134388">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
بلومبرگ: سازمان ایمنی هوانوردی اروپا، سطح هشدار را برای شرکت‌های هواپیمایی فعال در خاورمیانه افزایش داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/134388" target="_blank">📅 14:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134387">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
فرماندهی مرکزی آمریکا (سنتکام): «نیروهای فرماندهی مرکزی ایالات متحده از ساعت ۶ صبح به وقت شرق آمریکا (ET) موجی از حملات علیه ایران را آغاز کردند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/134387" target="_blank">📅 13:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134386">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
مهر : صدای انفجار تو شیراز مربوط به عملیات معدنی کارخونه سیمان بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/134386" target="_blank">📅 13:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134385">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eX3gYz0hyLFL_nqb0ebYreq8SuvJ0Ndm6GB7mHAXvjyIkYPKGwOlgfS0qMjqY3F02X5tiWhlSs3geYx7ArPASc-JiSBAqhRkz_gHzINC8pIl5Fb9_RiWu44sUo3HryrhPfFK9JwtTEowAWUtm5tqZ1xeXaSmuxObRPz7SAtT1pWClesSrXRkUU8RIP_NEH-2IKIMqanzvMRD8b5KR-wdFhm4apN7m5LRpF9X99OgtKN5545etYGm0MLOZwhdXuCWlXNd8B_CJEsdA_uK_pu3yekIjy_jbmDz6uNhZkeM4RU3s7gKPW3HduOHGOOKrCOM-GYEYeT3w4El_mfvSLqbIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس با ریزش ۲۷ هزار واحدی در پایان معاملات امروز به ۴ میلیون و ۸۹۶ هزار واحد رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/134385" target="_blank">📅 13:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134384">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/StD3nowtaKn3Ftu8DdTBtBeBtU21ZAxFXvlspbIjIXxTNqO2MDjM5zdvqr5A3FFkZwNnrPb45oIau3fJFGh9LkuKHtVVYO3pVDGicr7Hr49vHG7nlM6WDJyc_Y9GksZx5mE9gyeke9p-pRKxhQ82IUFwZTWk4Xxi6tM0arUMfa36ChWI5Z9aY1iv3HL-L6xdVZkeSEwXbNXQtmKzoiEuG-4fEzZ3Ls2oX0AXKqXbX-Yec9zkS3qgd8IiJndcti1beWT3TSkBQPYoinVj52EprkW3YPppQA2Dwq8mKcHtaZiM-fouU3yxWAmShPwkdKbrIyXjqUrKq4XTKEFsWWCwng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نمودار نوسان قیمت تتر در ساعات اخیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/134384" target="_blank">📅 13:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134383">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
فوری/ مقام ارشد امریکایی به سی‌ان‌ان:
ایران از توافق‌نامه تفاهم با ایالات متحده خارج شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/134383" target="_blank">📅 13:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134382">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
معاون بین‌الملل وزارت نیرو: قرارداد صادرات برق ایران به پاکستان و عراق با دوبرابر ظرفیت کنونی امضا شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/134382" target="_blank">📅 13:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134381">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BeKkvSDiMoNu3HODZHClBkNuQZ9ihHsfaSqxHvCAm4wkKY5qok-srTi_lwoF0I5xcEgF8oS9JWLmwgupV-wu5FAk1dUf0ujTHyL94VjfliC3s9210ZgPwrzoY1TI3vKgtL6Lk73OxdOq1u0N2XfPZjICGnakoTa83JWOIoGJnXUpuPjm-8H1PxljWixaWVnlSIbuHfI1Qj9k2sLKASMte1cBLc15ssrNmyEv3aPy3oe2B3QYn7Toynu0DgzpxU_IRegooLyjVYJ_COhkG-wO_dahhdYr_YXPhh7xBDdbAeC5KP8M-jMjDFyiBR14kEpxhjxocqh3uhsM2dCC5DIi_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکونومیست: ترامپ برای بازگشایی تنگه هرمز گزینه‌ای جز بازگشت به تفاهم‌نامه ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/134381" target="_blank">📅 13:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134377">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b35c029e2.mp4?token=CZLpBbxt9id0940_al9ydiBTHjFwjNsA53uI-0GifT3J1h0yijYq-BgSnvUlCPkxEJyicdO0KMOmNaHwppBkjm-mbTTI1E3oPUfepiqJ89it5ITsdLJk-SR7gx72QrECCiJ3LN6xZ0tkN0uUjRP0_ioloTwVAHsStCbXo4FmcPvy-R9V6-1pYiyJnZYUvKpkyAdfqQU1vg_jd5rDVSXw4ksBoE1ssLEVlfL4ktex83fJM4sCYbcEIdX2oC9TNFl61y59bcQ_PEoc25FxXgcciWwyvWk3KP92fS05dfmVHqwtr6c39SAzadqvi4bVJwwhaDgJxe2dUzR7fwUqtrMnNSFy3T1i5NzsSZk6nw3pRrdnWVH0oUAwOdj1BKu2hAd9hggNTscnITTcP_g_84kGOR83l5_68Yq5Pl4qlWsWSc9aCt4qHVRGQ15oenP37m36_bqyRFXavkxldkOoZeYJ9EzMLzkfzN04DXBek5b6VQnM14dudhaDGoS1rl_Wk6RrYcPAZdSeScZuuIQITcHyXQiDgWvLqA8cByiBT3whoSwv5AX0ZpLH9BXsSujapt0jE5rU5hVskhkJQKadOHvVP6PBoqLGGshktGlHHMYpF8fBZb_zOm-FmUHsNMyXU24GzYZgTv7rkMMI_b1EWPmF88eIHQDJzHdtUn97W0rM72s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b35c029e2.mp4?token=CZLpBbxt9id0940_al9ydiBTHjFwjNsA53uI-0GifT3J1h0yijYq-BgSnvUlCPkxEJyicdO0KMOmNaHwppBkjm-mbTTI1E3oPUfepiqJ89it5ITsdLJk-SR7gx72QrECCiJ3LN6xZ0tkN0uUjRP0_ioloTwVAHsStCbXo4FmcPvy-R9V6-1pYiyJnZYUvKpkyAdfqQU1vg_jd5rDVSXw4ksBoE1ssLEVlfL4ktex83fJM4sCYbcEIdX2oC9TNFl61y59bcQ_PEoc25FxXgcciWwyvWk3KP92fS05dfmVHqwtr6c39SAzadqvi4bVJwwhaDgJxe2dUzR7fwUqtrMnNSFy3T1i5NzsSZk6nw3pRrdnWVH0oUAwOdj1BKu2hAd9hggNTscnITTcP_g_84kGOR83l5_68Yq5Pl4qlWsWSc9aCt4qHVRGQ15oenP37m36_bqyRFXavkxldkOoZeYJ9EzMLzkfzN04DXBek5b6VQnM14dudhaDGoS1rl_Wk6RrYcPAZdSeScZuuIQITcHyXQiDgWvLqA8cByiBT3whoSwv5AX0ZpLH9BXsSujapt0jE5rU5hVskhkJQKadOHvVP6PBoqLGGshktGlHHMYpF8fBZb_zOm-FmUHsNMyXU24GzYZgTv7rkMMI_b1EWPmF88eIHQDJzHdtUn97W0rM72s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئوی‌های جدید از حمله؛
به محدوده گمرک و اسکله شهید کلانتری تو چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/134377" target="_blank">📅 13:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134376">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
گویا حمله به صنایع الکترونیک شیراز بوده
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/134376" target="_blank">📅 13:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134375">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
گویا حمله به صنایع الکترونیک شیراز بوده
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/134375" target="_blank">📅 13:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134372">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uhqDSksQZGHxGhnQWhBeSuUF9LpI8y-8WnwYniMH6Ynzriz7mNVuWyMN-rkNlykoNfgo5vfkOyM5faaR8yUDDbOes92P7GiP0EM53i0rfBLucTYMEnBjWBuhPkOp4-g7SsXpmw154Rtwlt7GeFYnQ6V2WiSYNgjGPhNfVv0FgXeZj-M6uQUYUOv2kNNdCgL4vGsPHbVz4B3Hj7k-4uVvnTsPLkfWpFDkItxtXzkvf0GQczwKB7AQedYYFeVORrHCxnHBOHRPk9enr2HgNr4580wDuziKS-ZLL8r2IKZqwT7BZAYCpzR2diWvDcDyKUIhnFadL4Lf23kP8aGzsNXNxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OmSmGuVzPru_sUaNFARgpMvCvlYm82hWYEXZUQwRTXGU47HPGC5CDHPzgYB-7Vr6H5SCPB7m_RuKYQp8F3vY_-VKitJHI5id5cUKVYjw4DFFjcYrGGbyyna5Uh9UI_b9DxiPm6-FL_devTs-226zpBD1NeUiIAN3srZgusGBD7YlgDhmCaIHmlpsuUDq4uGn3J4EZux3bHYpMvAx6dRobia4jnDdDKCh3hGf1wJqjekOFmtEuyM5W_uy_ccPrXLMISszkfsIJP2QAH_FpW77KRLyr5rveTeMjQNu-yEpudBRkIfAbRtaTvm_1cHcgpOCLQ7y9UXVQt6_OCjxq3pTOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a57f3aee50.mp4?token=lUjYRuR3PuKsUsXmBRhSV62Bq8y9zYieZ3oggK-z8ISzaDqRskw6EDU6AB7MAXWl1O7DYMu3c8jOyJM3YYIaoNQpqBbhOaMpPF9nsE5LiAyHilx_X3gIEFxm3dsBhaWbGO7nY2Cw9y_C4_AlylH6bsBcGIPR2NyLvvXnCW65V06Dl3slk3GhtP9aqMbeLsZjw5LodkMYyBBCJK_YEmzV2q_TgFxv_kO5DLwlao8CeVFQwmw4jIGtlc7eFWlprnE1P42BTia3z8mLbXEQDUheRxTenrCP7yc7yD7_7NiVSCTC5kFbyQ6O5iqxZhpzwgqzLM4ri36yn-wTwdC4cKegFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a57f3aee50.mp4?token=lUjYRuR3PuKsUsXmBRhSV62Bq8y9zYieZ3oggK-z8ISzaDqRskw6EDU6AB7MAXWl1O7DYMu3c8jOyJM3YYIaoNQpqBbhOaMpPF9nsE5LiAyHilx_X3gIEFxm3dsBhaWbGO7nY2Cw9y_C4_AlylH6bsBcGIPR2NyLvvXnCW65V06Dl3slk3GhtP9aqMbeLsZjw5LodkMYyBBCJK_YEmzV2q_TgFxv_kO5DLwlao8CeVFQwmw4jIGtlc7eFWlprnE1P42BTia3z8mLbXEQDUheRxTenrCP7yc7yD7_7NiVSCTC5kFbyQ6O5iqxZhpzwgqzLM4ri36yn-wTwdC4cKegFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارسالی از انفجار شیراز
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/134372" target="_blank">📅 13:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134371">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
انفجار در شیراز
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/134371" target="_blank">📅 13:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134370">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
نایا به نقل از یک منبع:عراق، حزب‌الله لبنان و نهادهای مرتبط با آن را مجددا در فهرست تحریم‌ها قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/134370" target="_blank">📅 13:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134369">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59cab094fd.mp4?token=Ao2DNqTpi4rZO9fgBh2eBPTJcTkgkU9Id7N_eViYY_5ZYDi2a0Jikaf8nG3ku2TDPqyYsV8NB89L_-0N_Az9hxMUhmvrYLKK33ezG5WaC3-d3JqOWRfytafF5WNscCIgXhz5JhdNezmuhbJrY8r_b1E4XSe9aewfIO_C7hrWuac_vtj3iQHmZD4khAX_J3Un9T10h-mholzWvG_VkFG-GWGU4HZCAy-KBqagl2VHnZa4dMQVKd6k9-RX_JvCikIJB_lWb9kL3UgP5wbKx_l_16qLgGZ6SJsrmvIHKplVoSosElmrVx_9fXwufK3R39Zp4Aaio3k4mLtjeJwhvDZKtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59cab094fd.mp4?token=Ao2DNqTpi4rZO9fgBh2eBPTJcTkgkU9Id7N_eViYY_5ZYDi2a0Jikaf8nG3ku2TDPqyYsV8NB89L_-0N_Az9hxMUhmvrYLKK33ezG5WaC3-d3JqOWRfytafF5WNscCIgXhz5JhdNezmuhbJrY8r_b1E4XSe9aewfIO_C7hrWuac_vtj3iQHmZD4khAX_J3Un9T10h-mholzWvG_VkFG-GWGU4HZCAy-KBqagl2VHnZa4dMQVKd6k9-RX_JvCikIJB_lWb9kL3UgP5wbKx_l_16qLgGZ6SJsrmvIHKplVoSosElmrVx_9fXwufK3R39Zp4Aaio3k4mLtjeJwhvDZKtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آهو های زیبای جزیره خارک که از ترس صداهای انفجار به خیابان‌ها و کنار مردم آمده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/134369" target="_blank">📅 13:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134368">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
مدیرعامل شرکت آب و فاضلاب استان تهران: تاکنون هیچ برنامه‌ای برای نوبت‌بندی قطع آب نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/134368" target="_blank">📅 13:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134367">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ON4eipCrfDGCBKGY-qhp8LofgXZzRi3VH8pYw-3XW7NuBK20rKA2UYGgXq6TpW2jvTkGGcDn8ggBjIUxiM5lgVUsJt-AAEiJUzaGvt69_P80NmA_CFVEpTAV61nUQgppLEy77yakv5YK_NCFOEdMrTlcDVnmi7KvgmvfBxg7a5GMLxBAshyQx_1oCNl53rlMUGsYk7G51QcACnN8607LaIxhmQSUQmG3hvw8WLwbKaex7QtE0ERbmiR0WXnerrcAESsUoE0DbLKaEknkd074jlAkyNg-mpFnopt3DvjuXPcDi-B4uSCT89V3WY2RI1eamYXkQ4ywdd8uGdHBS2tuzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روی سخنم با ثابتی و امثال اونه، مرد باشید برید جنوب و از اونجا توییت بزنید جنگ جنگ تا پیروزی
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/134367" target="_blank">📅 13:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134366">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aR7m1VbbDchXtZEUL1QoIzSQe4WsHkw4wAglA2hMRTCqvsuQUEC3BQek58onYKu1mlqdzm2swgdew-TALRbXycXOkE7DxYNJX0kdOjgRmIrIQ-yO_c55lovppafVEesaln18iBtri6NiwN_l02PafXy_rRARkVSM9EPpQuvd6FJpt1bZhycpQz1ElMhe-rR2UPoyK0ZCPXCsbK5xannRTV8UcA-k7vtBeiSiQOuKU-qHP2R76VesXPdBA_aZ3yQ3iABgzFiS6HUi9f1rV7p9AlNbkHGHcnChMDp5xvtO1kLQNRCL-atuxuZE8csuFKj-_Jeh-jWm60QVBwV7hIwLUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت فعلی
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/134366" target="_blank">📅 13:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134365">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
گزارش‌هایی مبنی بر وقوع انفجار در اهواز و بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/134365" target="_blank">📅 13:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134363">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cx_bWh_Gue1Hxh27vKDy8e3PI60IQj1cQe3cbwQNBYdzsHf3URemIVG_mfqjvwJDhm6jC_sV6zdafVcls0oNI9pKhOKegAEbqFd8rzbHiCXhaQ5GgZqQzg6sgzqFxVBkc-Mevf7XnJux_GQarHQgYH-ZlEWpIJxEccV977LFOK9vnmYmvqNzYs90A2Bmn7BuJYlrPyNyTeXds8KyEN_RKvF4ame3qHxJcbSVp8pB--194DAgyC3GL6r67u1VeuFcttKK143qxn8UCOCyLoxxqFco3SJUiHv_Op1HTAw-RfwGcbZFMOgYZCBo80lSzDO9o-VPQU3D20HXg7ngOs6gXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EtPV9BGH4BBDYxPNvsVgBhIpeiCLY2smUtJTyZtGsezwVa9iuYY3Lt_j630EevAw8QjCS_4lUm1x0Nkg9ZoC8YFGG2Sq3MvvGFWOx1eeEELCSOQaO-0cySEIEr4ePgkcfhpQqKEr4h8iLonjPBYbBTrzfph27fIYCXFhh2hoVaxWbFwVQVyX1cjVgWKoG_M_i6_MMcGoXIu4nOZQwaslQ-WWMZIFKLgk7iO3fOc9DjU9x5nAeUmgLM3cp8nr8CtbrK5cARSYu6zxMBC4A3EdIlKKsElI9vzAfmWky7ATqs7M4EtQLAD_mr2dtxDsXjU-vqXD8eLAld-2RvxmkkHjwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نباید با آمریکا وارد درگیری تمام عیار شد، دلیل؟ تجربه
دلیل امضای قرارداد ننگین گلستان و ترکمنچای رفتن به جنگ ابر قدرت اون زمان روسیه بود.
باید از تاریخ درس گرفت.
جنگ گنده گوزی برنمیداره
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/134363" target="_blank">📅 13:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134362">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
رئیس کمیسیون عمران شورای شهر کرج:
بازسازی پل B1 کرج ۲۵۰۰ میلیارد تومان اعتبار و ۸ ماه زمان نیاز دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/134362" target="_blank">📅 12:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134361">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
نیروی دفاعی بحرین: صبح امروز شماری از حملات هوایی ایران به بحرین را رهگیری کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/134361" target="_blank">📅 12:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134360">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
ارتش : ۱۳ مجروح داشتیم تو این حملات(دیشب)
🔴
۷ نفر هم از نیروهای کادر و سربازها جونشونو از دست دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/134360" target="_blank">📅 12:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134359">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
گزارش‌ها از شنیدن صدای انفجار در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/134359" target="_blank">📅 12:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134358">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
بلومبرگ: عبور چند فروند کشتی از تنگه هرمز، [هم‌زمان] با اجرایی شدن محاصره دریایی آمریکا
🔴
یک ابر نفتکش تحت تحریم که حامل نفت ایران بود، به سوی دریای عمان حرکت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/134358" target="_blank">📅 12:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134357">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
رسانه‌های عراق: الزیدی پس از واشنگتن؛ هفته آینده عازم تهران می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/134357" target="_blank">📅 12:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134356">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
بلومبرگ: کشتی‌های حامل نفت ایران در اقدامی نادر، پاکستان را به عنوان مقصد بعدی خود اعلام کردند
🔴
نفتکش‌های «رانی» و «آمیل» که حامل یک میلیون بشکه نفت خام ایران هستند، سیگنال مقصد خود را به کراچی تغییر دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/134356" target="_blank">📅 12:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134355">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا: بیش از ۱۳۰ میلیون دلار رمزارز منتسب به ایران مسدود شد
🔴
اسکات بسنت، وزیر خزانه‌داری آمریکا، به‌طور رسمی تأیید کرد که بیش از ۱۳۰ میلیون دلار دارایی رمزارزی مرتبط با ایران مسدود شده است.
🔴
این کیف‌پول‌ها که بر بستر شبکه ترون فعالیت می‌کردند، حاوی استیبل‌کوین USDT بوده و به ادعای واشنگتن به بانک مرکزی ایران تعلق دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/134355" target="_blank">📅 12:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134354">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
اکونومیست:
ترامپ برای بازگشایی تنگه هرمز گزینه‌ای جز بازگشت به تفاهم‌نامه ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/134354" target="_blank">📅 12:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134353">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezizKOew6f9hvYaWiwtRgT4CPULcMWzyraiKKB0tHwmn4E1ZVbusM29PM-g_yA9AnKmSGNkhnqRwpDThlYuq40I0CMfiS8WQwnHnBwGgUv-08YZak8YcbU2J91C8Zw4cvqfKx-tqiV2tocJfveO2_KFx2KWT7cyiDIq0KWqj6huNyzWq3AkikYr_trchSkyL5Tn92diWAjqT9XbaitYerBBNWvSEHO4Nt-MUW4NVNlHsv_m6sWvUyHQHfKU5k9N2GIa4PfyrwyHVtiq0hliTJuDw_fi3RESXItK1N7WnQSqo9X1fVWLs5ENNZ_d8x9NqZonxwNLjs-qFr3Xzf3xdiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل ششمین زیردریایی مدرن خود را از آلمان وارد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/134353" target="_blank">📅 12:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134352">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/530aefe381.mp4?token=PmLIRmcvtph7_llaOtrOMFP2lX1Fe42UMDeqaMHkhjLPTJbFtW0H1thAofhLd8TltHBo3uDrS1v9Zqi-6RLpeakHQ4BrXPIBhKe3vPiaN6U18gbH79PG-UFfYItKIpKq6qbj2tO17A291P1a_jZbSznaLy_IQDJtomIxGWyEePyxvcd-4lvg26vJ280g9EYj2ORwz3DafiHSGoA654EHhnWk20q3g_Xp9lZFRNwzHK6IvWEW8fEDr3aLPKflpKVwgTATjgulv1IXEJR7UJL9M26ayuNUe13Zo1fnuxFaLVBtkzTOBQINV7bHJ2WdxcRGVc8inMN4yBKjCw4Kj0e-kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/530aefe381.mp4?token=PmLIRmcvtph7_llaOtrOMFP2lX1Fe42UMDeqaMHkhjLPTJbFtW0H1thAofhLd8TltHBo3uDrS1v9Zqi-6RLpeakHQ4BrXPIBhKe3vPiaN6U18gbH79PG-UFfYItKIpKq6qbj2tO17A291P1a_jZbSznaLy_IQDJtomIxGWyEePyxvcd-4lvg26vJ280g9EYj2ORwz3DafiHSGoA654EHhnWk20q3g_Xp9lZFRNwzHK6IvWEW8fEDr3aLPKflpKVwgTATjgulv1IXEJR7UJL9M26ayuNUe13Zo1fnuxFaLVBtkzTOBQINV7bHJ2WdxcRGVc8inMN4yBKjCw4Kj0e-kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت دکل مخابراتی "پیامبر" بندرعباس پس از حملات دیشب ارتش آمریکا.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/134352" target="_blank">📅 12:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134351">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2a0455d7d.mp4?token=SfClki0tjG9X_7qsCVupQCC51zzvYI7x9ctkODV6uHMaME7D8OQLAkj-6oykdtcrujawj5Pp1LRudCXRxEHyrPyDbEQHs12xar0Ubz7s3reCgdAOuBtAXF5OUHuSUN3nj3G3rfYiWyI4s-YPaB_AAYGxlu6paUjnUWKiLN4wTkLUr7gsH8oc5VF53g63Ti8vubMN6dJCRzcefyGs8r859j71rNT_ywvWCMx_Dul7PqKiaRluxOyK0CRpL82DEGgwCjkOBagMaWEzq6s3zRvkNRrkxkKzM9ZLh99wQ8KmXcX_R7Q8lBg4aGLL6oI-1EYorEtB-ND9zSug-afd1gGG3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2a0455d7d.mp4?token=SfClki0tjG9X_7qsCVupQCC51zzvYI7x9ctkODV6uHMaME7D8OQLAkj-6oykdtcrujawj5Pp1LRudCXRxEHyrPyDbEQHs12xar0Ubz7s3reCgdAOuBtAXF5OUHuSUN3nj3G3rfYiWyI4s-YPaB_AAYGxlu6paUjnUWKiLN4wTkLUr7gsH8oc5VF53g63Ti8vubMN6dJCRzcefyGs8r859j71rNT_ywvWCMx_Dul7PqKiaRluxOyK0CRpL82DEGgwCjkOBagMaWEzq6s3zRvkNRrkxkKzM9ZLh99wQ8KmXcX_R7Q8lBg4aGLL6oI-1EYorEtB-ND9zSug-afd1gGG3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
منوچهر متکی: بجای موشک زدن خیلی راحت میتونیم پایگاه های آمریکا رو تصرف کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/134351" target="_blank">📅 12:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134350">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
اینکه توی شهرهایی که هر روز زیر سایه موشک و گلوله‌ان، هنوز امتحان حضوری برگزار می‌کنین، یعنی جون بچه‌های مردم براتون هیچ ارزشی نداره.
🔴
اینکه سرباز وظیفه‌ای رو که با اجبار بردین پادگان، نگه می‌دارین وسط خطر، یعنی حتی جون همون جوونی که خودش انتخاب نکرده اونجا باشه هم براتون مهم نیست.
🔴
هدفتون کاملاً مشخصه؛ می‌خواین کشته‌سازی کنین، می‌خواین از خون مردم روایت بسازین، شاید دوباره بتونین فضای داخل رو کنترل کنین و مردم رو پشت خودتون نگه دارین.
🔴
این همون کاریه که سال‌ها با جنگ عراق کردین. از درد و مرگ و ویرانی مردم استفاده کردین و هر چیزی رو به اسم امنیت خفه کردین.
🤔
بچه‌های مردم، دانش آموزها، سربازهای اجباری و خانواده‌ها سپر سیاسی شما نیستن. هیچ حکومتی حق نداره برای حفظ خودش، مردم رو قربانی کنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/134350" target="_blank">📅 12:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134349">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SwZSv5hWCn6CmwiSq8kEwirhx63WN1yhaJvQ57lRFjbcpp5v6pAojx6M4NIugdDqRSbEIkFd9x0s2TVFIyO8KQBtmDWrh0tAcm-VKcD24Nw0VveJkRN-fx4bNvtpXmqgwM-5G73_5hVRee3DAcyP7kEHlH828kpZe1f5sf2Oa2lIpLFSdDUMbS8eKsLsix_lWuTzkFeMF20qK8jDOS2S6aO7jS537qvWYet9zIgI8s_1SDlSZ03qXTPN5kiY48GUwpWJjl1teYjU36EAWZRpYAPjoEfYY5pRB2Khzm2lQ2FE_FU2jyB2-TdH9t9RS71HgZnHB-RLD3DYqLC0oVkxCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فواد ایزدی: قالیباف همون روحانیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/134349" target="_blank">📅 12:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134348">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0869c470e4.mp4?token=nuRuXERGtml95HiaBuD_kUGoYxwR7WsdaqWD1VDUFZ2yrBHUT2Z-sSl0Yv655K5prnYfqlqoPLozne5sa8O1pPGx3GKzQ3lWNK6gu_nhn5Tr_BSpikWQQdaMgzgG4dbEui3lffAsqmrbU4708uXSQA8GN-ww6ddms6qx5FlmGdyRMl4co5N3r07Dxy9jmHuT00-vwsNFUCwCCBcC6xgcv-jZlnxYMbTE1PJtVAG8tsUJjtykqSc7vZSO_cfcHGB3iLHp5wmK96nJfQbJv77wIbfx8WZTNla9LUrBWMSKaYlMJSSbdkD5XF5svbVQ7IOh0d26ewzgpD78y1Qg3_IIBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0869c470e4.mp4?token=nuRuXERGtml95HiaBuD_kUGoYxwR7WsdaqWD1VDUFZ2yrBHUT2Z-sSl0Yv655K5prnYfqlqoPLozne5sa8O1pPGx3GKzQ3lWNK6gu_nhn5Tr_BSpikWQQdaMgzgG4dbEui3lffAsqmrbU4708uXSQA8GN-ww6ddms6qx5FlmGdyRMl4co5N3r07Dxy9jmHuT00-vwsNFUCwCCBcC6xgcv-jZlnxYMbTE1PJtVAG8tsUJjtykqSc7vZSO_cfcHGB3iLHp5wmK96nJfQbJv77wIbfx8WZTNla9LUrBWMSKaYlMJSSbdkD5XF5svbVQ7IOh0d26ewzgpD78y1Qg3_IIBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرواز "
F-18
" آمریکایی، دیروز تو چابهار، با ارتفاع کم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/134348" target="_blank">📅 12:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134347">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
انفجار در اهوار
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/134347" target="_blank">📅 12:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134346">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csbG28ZCcnio8-l7X2-JJ3vFN9UxlpEd6YVUgQEnbSjfr96tJ_VyLMyOpGY3OK-D8_phIIRsFRqjb5ie9ViRhP48LSt3i6DCvupWfQvOCOmRaJrNwLg-YRpIqzABpBMuH3G0VZ_TtB_JDrPokL5D_sCLow7M2wGm1_YpHGFCLEqpuY5MOOOhMltpY3lDkqmt_w3vqGBgtOk73foTt1VjPqeWc65VBP_rpnlkwrO2gqIi3bEzFzvtjR1a0rDDSEkpGzKVLXFvwv0gemuDUjvv_2K1spQu_O6jVLCAiaQxJ9VMMh46IAEU-1ajqkrlz5WyKuySIgkwQ4ABqMQlbZHJ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فعلا برنامه‌ای برای واکسیناسیون رایگان HPV نداریم
رئیسی، معاون بهداشت وزارت بهداشت:
🔴
در حال حاضر، واکسن HPV جزو سبد واکسیناسیون رایگان کشور نیست و برنامه‌ای برای آن نداریم.
🔴
اکنون تمام تمرکز بر تامین سبد فعلی واکسیناسیون است.
🔴
برنامه‌ای برای افزودن واکسن جدید به سبد واکسیناسیون نداریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/134346" target="_blank">📅 12:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134345">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be3919ab6.mp4?token=WPJC4RkcKgTOxouR4oRrfGQiYx2cAfMxHYgRbjBoQ7UvKqJ1S1kI-l6tAkhjbaxrHZHgrQ8CzvdoCeVZtFTKBfwgiIpTA2jkyHRcSkvwLCHW-ht_v6D-5Cv21ZVEkmoTeSejbFHZJzW5cdwCTReRcJxSDkhEPluueyONrsGYUzPNGG8m6cGrK7HsdnViBvhmRiuzLRpNHntCaagT085ySLutheOSvnZg49YYzcjw69hqBnd1dpDZjDyrG_5NiqypoIRpS3P_zaFjbUGsMjyTF5u4DkFYyGinhwwYVhMj3IjCAdcw7Sp4YzEVnceGLaS25iZ1PLb_s302H6o4mK2jgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be3919ab6.mp4?token=WPJC4RkcKgTOxouR4oRrfGQiYx2cAfMxHYgRbjBoQ7UvKqJ1S1kI-l6tAkhjbaxrHZHgrQ8CzvdoCeVZtFTKBfwgiIpTA2jkyHRcSkvwLCHW-ht_v6D-5Cv21ZVEkmoTeSejbFHZJzW5cdwCTReRcJxSDkhEPluueyONrsGYUzPNGG8m6cGrK7HsdnViBvhmRiuzLRpNHntCaagT085ySLutheOSvnZg49YYzcjw69hqBnd1dpDZjDyrG_5NiqypoIRpS3P_zaFjbUGsMjyTF5u4DkFYyGinhwwYVhMj3IjCAdcw7Sp4YzEVnceGLaS25iZ1PLb_s302H6o4mK2jgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
این ویدوئی تاریخی اولین لحظه ای هست که آلمان نازی سرنگون شد. یکی از زندانبان‌ها به دست مردم افتاده.
🤔
حداقل از تاریخ درس عبرت بگیرید تا سر خودتون نیاد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/134345" target="_blank">📅 12:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134344">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
طبق گزارش کانال ۱۲، یک سرباز ارتش اسرائیل به پنج سال حبس محکوم شد به دلیل ارسال ویدیوهایی به ایران که شامل تصاویری از رهگیری موشک‌ها و همچنین تصاویر حملات موشکی در طول جنگ بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/134344" target="_blank">📅 12:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134343">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
چین: با اعمال هرگونه تحریم آمریکا علیه خرید نفت روسیه به شدت مخالفیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/134343" target="_blank">📅 12:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134342">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
بحرین: ما هم اکنون تحت حمله هوایی سنگین هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/134342" target="_blank">📅 12:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134341">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
جنوبیا چقدر مظلومن! هم زیر حملات آمریکا هستن هم بهترین نظام دنیا برقشون رو تو این گرما قطع میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/134341" target="_blank">📅 12:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134340">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
وزارت نیرو: هفته آینده خاموشی مناطق گرمسیری و درگیر جنگ کاهش می‌یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/134340" target="_blank">📅 12:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134339">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EryiyAZty21W1XL--ZgvOfMit7Tn_ZHo5FRgZmk6zpDgbOM0W_3heOT7vREnjZ_2FqqBFWK_CFS0dB-USpHnhI7gyYlHOAoO-n2_DE3ydytJmd-HAK57VjaT5f4Fqfoyr0OfN43-cm5jEhw5HDM_gm3krQcxmhUAYLjSCNs1DQdHUSZiQWnjOI2QCAcFytY4SdlPcJTjExpF7Ic5PWz5YhVqMDsTBYGG9L1CE6a6T1l4Bx-ByQDt34nc5oAEsIw1Gr7X6Hv7A5kjK_oEhuubZqnq3THLMC8nnT129Qbo7WuWAKVyGcER-fjqjV7sXSHBuAp0-OZYQ5Bsnd2svqNdvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ام‌جی لاریجانی : مردم خودشونو برای یه جنگ 3 - 4 ساله آماده کنن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/134339" target="_blank">📅 11:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134338">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
بلومبرگ: ۶۰۰۰ دریانوردی همچنان در تنگه هرمز گرفتار هستند.
🔴
تنگه هرمز همچنان برای کشتی‌های تجاری بسیار خطرناک است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/134338" target="_blank">📅 11:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134337">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
استانداری خوزستان : دو انبار غلات و آرد گندم در دشت آزادگان و هویزه مورد اصابت پرتابه های آمریکایی قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/134337" target="_blank">📅 11:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134336">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
فوری / سپاه
:
اگر صادرات نفت و گاز ایران متوقف بماند، مسیر صادرات متحدان آمریکا را مختل می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/134336" target="_blank">📅 11:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134335">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYJM22WjBRMZ850O9URoHz78wJ3kEX4-iQyQF8qViSkqnMUCSJWdvb9Q2JFUtcP5N55WwOm5LR7z_k6IYfk00KDmkMdhBqghdsDsoVLnKV6wxlpgDhWrjzNmg6OtbQALn9ytlNsDO3s_kwBn77VREkiA43BtmybgkHOQdR0Jgoc8os1wWeMuaCF6cdctjhSkk8FSyBlDV4sJ4Y6Om096R3Sws3ngPV1djpjz9PS3AD52TbmHkRSN8D-Njk7o3501i_YpgQvubzhSTvswGBAdF9dKcCr__etRmdWC9iIZQJNz7OilhL7Tdfzzs-oQGDiOSxo3ZHR_bFANHA4KyHcVsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طرح جدید دیوارنگاره میدان انقلاب با  شعار "ما ترامپ را می کشیم
"
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/134335" target="_blank">📅 11:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134334">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
انفجار در بندر کنگان
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/134334" target="_blank">📅 11:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134333">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72056fdffd.mp4?token=ezkm7O-SFcS7FB4DqsvjDTvr4aXajpYge3mMubQg3-l0iuPoJnrPNeFVBYp2son_cuzC6Z_th-LrGzUKtHgFqNz2Z8Hlm_2N-ScRGO3XPq56ej7aVcDDNiSfjbn9tXWqql_ofrhqpUJ6kspO6yUs_zNHLWX0gNFA4fwisNto3vqlX3-JQIJj2fqJeVr0WnVHGMkXlzy5AJnIsVdpsNQ66cJu7--Ca88hrdA0wxBMcuuBG_hdmVK-5ffNDWrDb_RCXJ6GY0LJKFPWgf_Sh9NYfGvyuet8SS2RHU3NvGJIB7Jt_ypbgzqFlxg353JKSiq-5aGBOtoU49basHQfG5pRzq4XgZRp7L2kFjyNO3StWpsuDScw-N5NsJ1w6P-dlGkosnAhxRinmpkJ-r18-2oT89M9rkFd7pk6WxDC-v7HtXPNbPrhXvvtDdIPGq0yQ2lPFuhBp2ZduNw3Ush_4BuKJnRmeTHRz_NsLGGTdKfGBuEo3_XRUyAaXdfn2Mg4CZt0EJquNy7PV2XISqL7pBT9-0SBZOS-lZvmuefw-MTqo1H950FgWb7wSok0DJNvMmgjSBsQgH6jOwoKjOKO7peO-2n-VLv0_R62Py4y3tvgHlIXc-PDhkTWvNS74Qig0IZCLPwFk2iiV6GgYjH7F42Y18G6wQfTuzoKJFDZ9uMO4PM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72056fdffd.mp4?token=ezkm7O-SFcS7FB4DqsvjDTvr4aXajpYge3mMubQg3-l0iuPoJnrPNeFVBYp2son_cuzC6Z_th-LrGzUKtHgFqNz2Z8Hlm_2N-ScRGO3XPq56ej7aVcDDNiSfjbn9tXWqql_ofrhqpUJ6kspO6yUs_zNHLWX0gNFA4fwisNto3vqlX3-JQIJj2fqJeVr0WnVHGMkXlzy5AJnIsVdpsNQ66cJu7--Ca88hrdA0wxBMcuuBG_hdmVK-5ffNDWrDb_RCXJ6GY0LJKFPWgf_Sh9NYfGvyuet8SS2RHU3NvGJIB7Jt_ypbgzqFlxg353JKSiq-5aGBOtoU49basHQfG5pRzq4XgZRp7L2kFjyNO3StWpsuDScw-N5NsJ1w6P-dlGkosnAhxRinmpkJ-r18-2oT89M9rkFd7pk6WxDC-v7HtXPNbPrhXvvtDdIPGq0yQ2lPFuhBp2ZduNw3Ush_4BuKJnRmeTHRz_NsLGGTdKfGBuEo3_XRUyAaXdfn2Mg4CZt0EJquNy7PV2XISqL7pBT9-0SBZOS-lZvmuefw-MTqo1H950FgWb7wSok0DJNvMmgjSBsQgH6jOwoKjOKO7peO-2n-VLv0_R62Py4y3tvgHlIXc-PDhkTWvNS74Qig0IZCLPwFk2iiV6GgYjH7F42Y18G6wQfTuzoKJFDZ9uMO4PM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بندر فجیره امارات که مهم‌ترین مرکز جابه‌جایی نفتکش‌ها در منطقه بود، پس از حمله موشکی سپاه به دو نفتکش(VLCC) از چرخه فعالیت خارج شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/134333" target="_blank">📅 11:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134332">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
رسانه‌های اسرائیلی: نتانیاهو شنبه به واشنگتن می‌رسد تا در مراسم خاکسپاری سناتور لیندسی گراهام شرکت کند.
🔴
وب‌سایت "یدیعوت آحارونوت": زمان دقیق ملاقات نتانیاهو و ترامپ هنوز مشخص نشده است، اما انتظار می‌رود که آن‌ها اوایل هفته آینده با یکدیگر دیدار کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/134332" target="_blank">📅 11:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134331">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
قیمت دلار آزاد به ۱۸۶ هزار تومان رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/134331" target="_blank">📅 11:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134330">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFvtCRj3ub0qhRtZ3kk8AXNvB485NbhGXgYt7-Ee4-xrCG7qoPviagO3JiWkxBy15G0cmF0NvH_stHWWezjDJwl1joKH2pnK4S8OCmy3LjYENZLe8XGaPHZ_2AfsKWKJ8yvrJoWIK5G_RUigp3uiBY3keVMsYiVO7-Rj685Z0OnDuZZ3S4U7xFj2MDgeD-DCNdVuGiVie3cTZZ9Z48N1d4WjCWjhoiMlH9a9eHt6VcdoKCg3u9zf_lHCGS2ec2dcvZ3SowVV7mfJMTQy8zEx1Phrjfn1ZcNCF2Pf_rVNUc4ylJpp-gNFUPOSa5ZfuHwABWDjxbllVg9jsnrxrSS7Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش روسیه به دنبال نصب رادار بر روی بالون برای استقرار بلند مدت آنها در آسمان کشف پهپادهای اوکراینی که به طرف آنها پرتاب می‌شوند است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/134330" target="_blank">📅 11:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134329">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fa0f0b984.mp4?token=m7-bpSh98MiAYp3pkxC3JdWoQKxjmeSgBD0Y7E6x3zBHCNTAKi08BFHWgaq_YKAgJcXPxEbp75OreX9K0-2Q5Onj-H03J9LQL8UtsDLWBQabVUySGfPxu8tvvbw93W8iumkJH6A6lRuInj4tGjnwKaAVcZMQr0mqXKweoIxCYGnfWmUoDsYYbIfq7UFwTOOAjKr-yY0dQ1ttCvzQ16wrsQOAoimehsalPmm64ekFMu_mSC42mzVs5dviSoThxcLQ8pLC5I80ZAdPXfCtxy0mRaV6oJpOCvFnv1ORanxuMIw6YMfJ0wZabzMCpbTZv3yNJ-u3n8TYTuMZ_18qXUGVHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fa0f0b984.mp4?token=m7-bpSh98MiAYp3pkxC3JdWoQKxjmeSgBD0Y7E6x3zBHCNTAKi08BFHWgaq_YKAgJcXPxEbp75OreX9K0-2Q5Onj-H03J9LQL8UtsDLWBQabVUySGfPxu8tvvbw93W8iumkJH6A6lRuInj4tGjnwKaAVcZMQr0mqXKweoIxCYGnfWmUoDsYYbIfq7UFwTOOAjKr-yY0dQ1ttCvzQ16wrsQOAoimehsalPmm64ekFMu_mSC42mzVs5dviSoThxcLQ8pLC5I80ZAdPXfCtxy0mRaV6oJpOCvFnv1ORanxuMIw6YMfJ0wZabzMCpbTZv3yNJ-u3n8TYTuMZ_18qXUGVHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو درباره رئیس جمهور ترکیه، اردوغان، گفت: من فکر نمی‌کنم اردوغان باید هیچ سلاحی تهیه کند. او خودش سلاح می‌سازد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/134329" target="_blank">📅 11:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134328">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4285afbb6f.mp4?token=Mjh0SG6qoOip4SxqwaAi7Rsq-dlGpPtlRmchZW_TVVCrkvYsDM7OuJXiCtmfd5JuhEFKSMiPMxyqcdnyrI94bWkcRrUG8XOQJsmNTjzZrk5irvp-YR7j6tYT4jRzSL19JKW1fiTwcxnQYVWf0mj5f13_kVwZeMkaKC_U7-X3KPvz33dPWK-wmHzDJ3shFys8c0NOj8DtoV0eH9QTBpq-ywuSeldEyhyi4t_MM7auVy8AVoeNHib1PrkM_QvYhk_nxwAFvk4-v268Ua2e21FRSTdKjAeogVYpU7CX9WpezzvYlynAbGBTmI0Xijvebaab6A3kJI55R0zZjo5z5Ua_wDdl76xFJCqBmF2-hdQvxRg49CIrpMHeZ-y3vj8ChJwYq3T8YSsRemCwP0oTxkQRCcTmBJKar1jMI69Kua2XdYObkhQ6818GBDcWJ0KAXvxq2sDfcsBJeDVGpdxm-VbwkYaNBOiB4RvDeEd4T5DnWxz9SR8WnBkIwehXmn2St4JVokZ0_yqmvcUcZlyhDGYM9ueD_D05zgSfEcyV8iMizle_T3Kkc9JoJbyZa1YqSh4TIoeiAipS-jy45eQmcwEzAA_oCNTlIlOWmqipLl4oI310S2zWySoBTNAADyRwIGPHiOtiqflpirlCMow_Nw-ucN6G6t0Isczd6uNAPE5HjsM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4285afbb6f.mp4?token=Mjh0SG6qoOip4SxqwaAi7Rsq-dlGpPtlRmchZW_TVVCrkvYsDM7OuJXiCtmfd5JuhEFKSMiPMxyqcdnyrI94bWkcRrUG8XOQJsmNTjzZrk5irvp-YR7j6tYT4jRzSL19JKW1fiTwcxnQYVWf0mj5f13_kVwZeMkaKC_U7-X3KPvz33dPWK-wmHzDJ3shFys8c0NOj8DtoV0eH9QTBpq-ywuSeldEyhyi4t_MM7auVy8AVoeNHib1PrkM_QvYhk_nxwAFvk4-v268Ua2e21FRSTdKjAeogVYpU7CX9WpezzvYlynAbGBTmI0Xijvebaab6A3kJI55R0zZjo5z5Ua_wDdl76xFJCqBmF2-hdQvxRg49CIrpMHeZ-y3vj8ChJwYq3T8YSsRemCwP0oTxkQRCcTmBJKar1jMI69Kua2XdYObkhQ6818GBDcWJ0KAXvxq2sDfcsBJeDVGpdxm-VbwkYaNBOiB4RvDeEd4T5DnWxz9SR8WnBkIwehXmn2St4JVokZ0_yqmvcUcZlyhDGYM9ueD_D05zgSfEcyV8iMizle_T3Kkc9JoJbyZa1YqSh4TIoeiAipS-jy45eQmcwEzAA_oCNTlIlOWmqipLl4oI310S2zWySoBTNAADyRwIGPHiOtiqflpirlCMow_Nw-ucN6G6t0Isczd6uNAPE5HjsM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مصاحبه‌کننده: زهران ممدانی (شهردار نیویورک) بارها و بارها شما را تهدید به دستگیری کرده است. آیا نگران این هستید که وقتی در ماه سپتامبر برای مجمع عمومی سازمان ملل به اینجا می‌آیید، او این کار را انجام دهد؟
🔴
نتانیاهو: نه، نگران نیستم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/134328" target="_blank">📅 11:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134327">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2a6279b60.mp4?token=J-wwJyljvd6dsB9ECb6Kl5pdXcyl7_kjWLkWTDw3kw-p4FBHv7IZB73Di9zNk5HXaqeWD_C1H9DOiuQORWp5g1_RoaRcJlb2oS8moL0xehB1v3DRY1--BbvbjJCwlbHSDXemAAGGcKqXJy98XwhZ4tz-f9gZZL-e1VxoY3sDVNpi1avR8U-NgxQ4DWxJ6cyD4UCMdGjjwZWYWn6Wizw6KE8krfZA1VuRrDlG7nMTSJ8evT4U2xlf_np9xPD3yhqLq44xQ89n9LwfQ8z3Z_VqKpQ34vcUsPbhZk5VUHOscEYp_m4pprP8z87CJtEDe7VtSyjhyE7igsFoeAF7OybS6Tx_xLJy28h_xu7YM_Tnwqsf5AgroYjoK3VJVUoDNlv3YNjgLG37sWgGx0JYyNW_LkuphHSUYGu079m1eWUD3e_Sy07tAz8z8UU4b93WqW9syow4Q7QfG-8UlxpUSfGdYi7sd5uba39ZbV6-vU3JTbpcCE_NZCgDBbwSrd0vLe2fQaIVkRWekHVZkI7Ot6qiksS2pw6gzrz_pr7GJUX-ptHIa_geWHtuYILbCW4Xj_IoARaV8UD9Dnay0D4V_I4q5EpRIq1fcLTbawqph9VgDx0njns_L8occ7nFOPv1jEktombpZyxF_n_MbqGg-opEwaLoj1mQWDtHxT9K8SR1xlI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2a6279b60.mp4?token=J-wwJyljvd6dsB9ECb6Kl5pdXcyl7_kjWLkWTDw3kw-p4FBHv7IZB73Di9zNk5HXaqeWD_C1H9DOiuQORWp5g1_RoaRcJlb2oS8moL0xehB1v3DRY1--BbvbjJCwlbHSDXemAAGGcKqXJy98XwhZ4tz-f9gZZL-e1VxoY3sDVNpi1avR8U-NgxQ4DWxJ6cyD4UCMdGjjwZWYWn6Wizw6KE8krfZA1VuRrDlG7nMTSJ8evT4U2xlf_np9xPD3yhqLq44xQ89n9LwfQ8z3Z_VqKpQ34vcUsPbhZk5VUHOscEYp_m4pprP8z87CJtEDe7VtSyjhyE7igsFoeAF7OybS6Tx_xLJy28h_xu7YM_Tnwqsf5AgroYjoK3VJVUoDNlv3YNjgLG37sWgGx0JYyNW_LkuphHSUYGu079m1eWUD3e_Sy07tAz8z8UU4b93WqW9syow4Q7QfG-8UlxpUSfGdYi7sd5uba39ZbV6-vU3JTbpcCE_NZCgDBbwSrd0vLe2fQaIVkRWekHVZkI7Ot6qiksS2pw6gzrz_pr7GJUX-ptHIa_geWHtuYILbCW4Xj_IoARaV8UD9Dnay0D4V_I4q5EpRIq1fcLTbawqph9VgDx0njns_L8occ7nFOPv1jEktombpZyxF_n_MbqGg-opEwaLoj1mQWDtHxT9K8SR1xlI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو درباره زهران ممدانی: فکر می کنم زهران ممدانی پنهانی از آمریکا متنفر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/134327" target="_blank">📅 11:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134326">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
نتانیاهو: مرگ لیندسی گراهام ضایعه بزرگی برای اسرائیل است.
🔴
اسرائیل تنها کشوری در خاورمیانه است که خاورمیانه را متحد نگه می‌دارد.
🔴
ما از تسلط رادیکال‌های اسلام‌گرا بر شبه‌جزیره عربستان، اردن و مصر جلوگیری می‌کنیم.
🔴
اگر با جایی که ما در ۷ اکتبر بودیم مقایسه کنید، اسرائیل بزرگترین بازگشت را در تاریخ داشته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/134326" target="_blank">📅 11:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134325">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
جدول خاموشی مناطق مختلف تهران منتشر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/134325" target="_blank">📅 11:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134324">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
قتل ۲ زن سالخورده به دست پرستار خانگی / متهم: من کلا اعصاب ندارم!
🔴
متهم ۵۵ ساله که به قتل دو پیرزن زیر شکنجه اعتراف کرده، درباره انگیزه خود گفت: من اعصاب درست و حسابی ندارم. وقتی می‌خواستم به آنها دارو بدهم و مقاومت می‌کردند، مجبور می‌شدم آنها را کتک بزنم تا داروهایشان را بخورند.
🔴
وی درباره قتل دوم افزود: به خاطر مسائل و مشکلات زندگی‌ام ناراحت بودم و حرصم را روی او خالی کردم. فکر نمی‌کردم فشار دادن گردنش باعث بد شدن حالش شود و او به کام مرگ برود.
🔴
متهم که سابقه پرستاری ۱۵ ساله دارد، درباره نحوه فرار پس از قتل اول گفت: وقتی خانواده پیرزن به من اطلاع دادند که او فوت کرده، ترسیدم و گوشی تلفن همراهم را خاموش کردم. با گذشت زمان، وقتی دیدم کسی به سراغم نیامد با خودم گفتم حتماً پرونده بسته شده است و دوباره به سراغ پرستاری رفتم.
🔴
بر اساس گزارش، این پرستار خشن پیش از این نیز در سال ۱۴۰۰ توسط خانواده یک زن سالخورده دیگر به اتهام قتل شکایت شده بود، اما به دلیل فراری بودن به نتیجه نرسیده بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/134324" target="_blank">📅 10:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134323">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m81HXdykCtWwOjOgWB2yEPk2OaMI3gfuirTFbTACYzL2ske11E2SWM-sIoY_bFoHvYfS-8nPh5TGaBpidaXAGSwroBXVtLJdfmrLCp8s418M0iYjsdk6DqwM3-CXfV0HSLyKZy816RRYAnjZjsSUZ6BvgU4vkzo4vcMeYqRLWe_8_qfm41xGfJ11an-MyaS2vHAE-NLaArzyX93X1Ofep0rMogYPhgsG4zhkAc_dhlUGuvATyhQqZdpIHs8htYv2RQoShPf3QegeQJ1jkx6cDL4v6ySiRwg3o4JMjWq_H1Q3c_5zlfhuzPy_0TnZVW99P5J1uZD5S7uQUeAk98jhVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت با ازسرگیری اعمال محاصره دریایی بر تمام بنادر ایران توسط دونالد ترامپ و پاسخ ایران با انجام حملات در منطقه، افزایش یافت
🔴
برای دومین بار، نفت برنت در بالاترین سطح از ۱۲ ژوئن و نفت وست تگزاس اینترمدیت در بالاترین سطح از ۱۵ ژوئن بسته شدند و در معاملات صبح امروز چهارشنبه نیز به روند صعودی خود ادامه دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/134323" target="_blank">📅 10:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134322">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDmGdRsPCHs4LIWr0GOnvOso8vIt6HtcC0uCw6Ct-0weRq1zt_OCqJI2usW_yYE9ilXFwJHk_pf63PRjsUCUaC35Xogp2n4qVo5VNqwcPTzOPY8ZmKibL2PK9OdVnUuPa4tkFq0NEObGpKSqwjm4S4utVxEQOSF-v5vPGu143qG1A8W8y3jfRn0HHaUh43c3mZ6FvBS4yxVt10ZQvaQMTmUOPheRCNuHaoiBf69H9V6bpDQzXaGb44u8zn0ixrjIqJo8Am32EEnXH3T8nGDVLpxqskECHOVP_dXd6EDaYMif8GdsNDqp1mOnvevFHa3fHMPNdlnj2EKwWQ49fEtVbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال استریت ژورنال: امارات متحده عربی، پس از کمک به آمریکا در جنگ علیه ایران، از طریق انجام ده ها عملیات هوایی علیه ایران، به مزایای قابل توجهی دست یافته و به دسترسی گسترده‌تری به تراشه‌های هوش مصنوعی از سوی ایالات متحده دست یافته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/134322" target="_blank">📅 10:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134321">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
رئیس مرکز ملی تغییر اقلیم هواشناسی:با گسترش پدیده النینو در اقیانوس آرام در پاییز و زمستان امسال بارش های خوبی خواهیم داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/134321" target="_blank">📅 10:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134320">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3194c525fb.mp4?token=TRGs3l8a5_sQUeq03Rc8Het5zEpNdbpF8UdPLjLZ1gklzFQBryXLsr8lUzJyM_wcg-E9aFIWc135TV1y8FqU6jzcj3qlZBJze0iilgJOGwN3Z-W60OkosvrI4FTFEzvfR3BoKjB1sNQZR0PXpPif942EoA4VV_AjqmdeWxrZ3TIIxMlBUnCTpfsujfHgSiVMEmh-MHSAxFpdwvvQSS46y75lq8nOEBaa_hAtEdqfMJWrLRfKMJW0i_qKAvDcior4aw6djsCTrgF56nKrY4TCgeC6YkV_S6vJ6YA7b-htvgnl0g1LSvg-kxjQ2tShiWWRg6qLnpA_Eo6d385skZv3lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3194c525fb.mp4?token=TRGs3l8a5_sQUeq03Rc8Het5zEpNdbpF8UdPLjLZ1gklzFQBryXLsr8lUzJyM_wcg-E9aFIWc135TV1y8FqU6jzcj3qlZBJze0iilgJOGwN3Z-W60OkosvrI4FTFEzvfR3BoKjB1sNQZR0PXpPif942EoA4VV_AjqmdeWxrZ3TIIxMlBUnCTpfsujfHgSiVMEmh-MHSAxFpdwvvQSS46y75lq8nOEBaa_hAtEdqfMJWrLRfKMJW0i_qKAvDcior4aw6djsCTrgF56nKrY4TCgeC6YkV_S6vJ6YA7b-htvgnl0g1LSvg-kxjQ2tShiWWRg6qLnpA_Eo6d385skZv3lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قطار باری در محاصره آتش‌سوزی مهیب جنگلی کانادا
🔴
گسترش آتش‌سوزی‌های جنگلی در استان انتاریوی کانادا، صحنه‌های هولناکی را رقم زده است.
🔴
در یکی از این حوادث، یک قطار باری در محاصره شعله‌های آتش گرفتار شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/134320" target="_blank">📅 10:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134319">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1JPYBkQ5ZrzOpDvgckQeaYxldPevHDXNriXxQ1PFKjtTUZJspe1pJ56HGOyPOfYhAZogXezTeSegCQrrPKMX0lTQuGE_KWTgnmn8tEwtCATwegbJKhsgVLWC6GjPNJBCq11RNLulw2WLcjDszNXHyLllHrTNAJLBEq-pe6JPpjIoYX9NGFBs5SndKSFGFLTkyEpS6KYbswdGpRJOy-jE1KkrGmbcl5xUsFPgnqQ2dpM9Ynluzu3w_pFzzISOaDzgJE9x_czYGbY1KidWi0u4a9PtL12jfTJLNDloFHwqVPC5npAC6keZJDFML5Q_7u77s3e511B0GmJ8NQysxF5jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی دولت: در حملات  آمریکا به جنوب کشور، بیش از ۳۰ تن از شهروندان غیرنظامی جان خود را از دست دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/134319" target="_blank">📅 10:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134318">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
فرماندار بوشهر گفت: ساعتی پیش سه نقطه شهر بوشهر مورد حمله قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/134318" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134317">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddnnxVAaXrz8CZQBCTwnTjFKnfCACevcKe2I8wWSzvBJnL5VZCP1fxJkxN1Hoep-Nht0InN374VxXsHfL96BI5jtMh6R-kd-r61Tv_AjsoXLi1Kwmz-szYZVdF8n608JPkMLvLlBTk8Dpl5vIU98hK-mtPFBb2YBPwP8daRnXbqXKQqEGe2h87DDMTAAB5YI84KjkKGLs4uTAA1s35RCn76QLGBCpbGRaVhjZm0VAUcOKRQP7XZE0T8UcUjQWPY5FiSdsMwJ5FS-chDkoNheI6uSRxyVi6BnAukYItuW1vbZ07QDCwzl2WAhO0gzS1l43kMC1mMxaTWbjXyzYjsK2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جدول خاموشی مناطق مختلف تهران منتشر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/134317" target="_blank">📅 10:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134316">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
دموکرات‌های سنا به دلیل مخالفت با جنگ ایران، لایحه ۱.۱۵ تریلیون دلاری بودجه دفاعی آمریکا را متوقف کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/134316" target="_blank">📅 10:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134315">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/635b715ae7.mp4?token=kPKIAbvv78Ux5wgF3zwVxBWG2tsbTyOv76tvl5zFQ-oOtDkP3g9TF9cCCZRC8XCO-Ca_ZU03JWPm6RendDICg-AqBsO7T9HoQV77pJ7ul-Bvp5R4Oo9Kk2CqlE7gXQ5qtfZ1T0WbVXucRKUwtMKaLLg9UzMnzkAISKCV_55VWus4gKTCRr3H5UHSxd6lorEymFb6qNcJOuaex0Aw-E2a8vaOGiL1IzyCmu4AcflX_Njvjm1f29rDKPN_SRFGJfVzD0rRrUUlBdc_-9-hSjudVPnQt4nfNHdjTq3Z9SSUhZvOSbbnpAQwqoNo1ZGVddtuTnueC7bLtTVxARLYTJwN8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/635b715ae7.mp4?token=kPKIAbvv78Ux5wgF3zwVxBWG2tsbTyOv76tvl5zFQ-oOtDkP3g9TF9cCCZRC8XCO-Ca_ZU03JWPm6RendDICg-AqBsO7T9HoQV77pJ7ul-Bvp5R4Oo9Kk2CqlE7gXQ5qtfZ1T0WbVXucRKUwtMKaLLg9UzMnzkAISKCV_55VWus4gKTCRr3H5UHSxd6lorEymFb6qNcJOuaex0Aw-E2a8vaOGiL1IzyCmu4AcflX_Njvjm1f29rDKPN_SRFGJfVzD0rRrUUlBdc_-9-hSjudVPnQt4nfNHdjTq3Z9SSUhZvOSbbnpAQwqoNo1ZGVddtuTnueC7bLtTVxARLYTJwN8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای از انهدام دقیق مرکز تعمیر و نگهداری جنگنده‌های پایگاه العدید قطر
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/134315" target="_blank">📅 10:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134314">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qk1wC9Ei7KJldQ2jnXHTZ13uhcEWWyJ8_nizA0DgqsGoyL_30DIqKUREmH_8yqaG0ztKs9L7VzwWen_kKhfVZ9WtI4HR7TGxTFWVOecr_vCDSVvGxbhZvGfWictadnMVFIqnyv-407rgu57Z7bHrK0NJUbu5mESjWt9k82idE30L86y57D6OE2wcJvwx0frDn_DJsbWGpl_BvS5leU_QW8n7PMWE8BiIWe63xLPKadeecPqOirVHPsMBGRxo6Exvxndgd5YVZ8ks0hriJVxwnhJYrkeZG4TjzGo9YYOEXdpUF12gbvrk3_EFk2WIIZD4sZKLwHdGtaSc7QbbjtjqjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منتسب به حملات آمریکا به چابهار، صبح امروز
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/134314" target="_blank">📅 10:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134313">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
رویترز: بر اساس داده‌های شرکت ردیابی کشتی‌ها، تعداد شناور‌هایی که روز سه‌شنبه از تنگه هرمز عبور کردند، افزایش یافت که بیشتر آن‌ها به تجارت ایران مرتبط بودند
🔴
هیچ تردد قابل مشاهده‌ای برای تانکر‌های حامل نفت و گاز از سایر تولیدکنندگان خلیج فارس ثبت نشد
🔴
۹ فروند از ۱۱ شناوری که روز سه‌شنبه از این آبراه عبور کردند، از مسیر ایران حرکت کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/134313" target="_blank">📅 09:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134312">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
استاد روابط بین‌الملل دانشگاه شیکاگو ، مرشایمر: جنگ با ایران وارد مرحله «اقدام در برابر اقدام» شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/134312" target="_blank">📅 09:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134311">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a21e369331.mp4?token=f6zOwypvrAjAQgYOlEDJEeyRn0f_TBYaPW7JHe8O46SPGFCNs0MNeoSAek29hxG0ChoLSEC6lU_uJTVnE5W1aHS15wk4odJGx4VhvST_ugqJ96As6dRAJJN-aOZ7DvkGR2eou29Wsr4TRHfXCtRAAPEcpUDjS2sk2r2zTdUNqZ7d2Joyzs99WXbEyfA9AVPHET5FpHn8X77Zn0Wo3ei9B_XXFqgeG0Tm0qLoM199eix3ljVQrfn7hpTQHdBsiZ585vZ0eWR05uGZi0AVPH0XSKnARZWytigVQaYOTZ2_u-NIJFdtlBAEU-uegsSvUQ-lTsWEqa5XcMkuNI-cUBtcB4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a21e369331.mp4?token=f6zOwypvrAjAQgYOlEDJEeyRn0f_TBYaPW7JHe8O46SPGFCNs0MNeoSAek29hxG0ChoLSEC6lU_uJTVnE5W1aHS15wk4odJGx4VhvST_ugqJ96As6dRAJJN-aOZ7DvkGR2eou29Wsr4TRHfXCtRAAPEcpUDjS2sk2r2zTdUNqZ7d2Joyzs99WXbEyfA9AVPHET5FpHn8X77Zn0Wo3ei9B_XXFqgeG0Tm0qLoM199eix3ljVQrfn7hpTQHdBsiZ585vZ0eWR05uGZi0AVPH0XSKnARZWytigVQaYOTZ2_u-NIJFdtlBAEU-uegsSvUQ-lTsWEqa5XcMkuNI-cUBtcB4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
منوچهر متکی: باید برویم زمینی، پایگاه‌های نظامی آمریکا را تصرف کنیم و صدها و هزاران سرباز آمریکایی اسیر بگیریم
#تریاک
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/134311" target="_blank">📅 09:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134310">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
الجزیره: افزایش قیمت نفت
🔴
قیمت نفت با ازسرگیری اعمال محاصره دریایی بر تمام بنادر ایران توسط دونالد ترامپ و پاسخ ایران با انجام حملات در منطقه، افزایش یافت.
🔴
برای دومین جلسه متوالی، نفت برنت در بالاترین سطح از ۱۲ ژوئن و نفت وست تگزاس اینترمدیت در بالاترین سطح از ۱۵ ژوئن بسته شدند و در معاملات صبح امروز چهارشنبه نیز به روند صعودی خود ادامه دادند.
🔴
نفت برنت با ۱.۴۶ دلار (معادل ۱.۷۲ درصد) افزایش به ۸۶.۱۹ دلار در هر بشکه رسید و نفت وست تگزاس اینترمدیت با ۱.۱۱ دلار (معادل ۱.۴ درصد) افزایش به ۸۰.۴۰ دلار در هر بشکه رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/134310" target="_blank">📅 09:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134309">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
ارتش اسرائیل امروز صبح عملیات تخریب گسترده‌ای را در چندین دره و خانه در شهر بیت یاحون انجام داد، و همچنین جاده‌هایی را که شهر بنت جبیل را به شهر مارون الرأس متصل می‌کرد، تخریب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/134309" target="_blank">📅 09:10 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
