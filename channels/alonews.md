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
<img src="https://cdn4.telesco.pe/file/uCVdvWSDkQODwAOmJb-g6QbP0m0HQFHmxtnM6sCoAA1bxKjjXG_8093pOXGRdESjfMyLPAkoII7rPicFnG47zm36b6gTLarRFlm7iR5yWABDvznaYOVpu5x_2nTR7zftdIO_xuuoC9laJM3mOXa2x8OTVsEzVlGQrz9GH2BIHJqNZVik2dmKNHlfJVHVgaRW6hY75H45lXh8Hl4g8M_M6WfKJOiJDxBsPAqLQrHDiXRW-MbYiHNJxKlXia4hr2FnVxOZwKqOPZzSsJ4Lr8qaTxiRe-l7WQZbVjGgcXNGS0zLQIlpAP7H6gqRk7Unwn4JBx_9Neo7Vg-G9UIlXGBBPA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 979K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 19:46:32</div>
<hr>

<div class="tg-post" id="msg-127945">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
ترامپ پس از حمله به لبنان با نتانیاهو تماس گرفت و به او گفت: «داری چیکار می‌کنی؟!»
🔴
ترامپ به نتانیاهو گفت که هیچ حمله دیگری به لبنان انجام ندهد و هشدار داد که این حملات می‌تواند توافق را به خطر بیندازد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/alonews/127945" target="_blank">📅 19:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127944">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
ترامپ به اکسیوس : ما قرار بود امروز صبح این توافق رو امضا کنیم و حمله اسرائیل به بیروت این کار رو به تأخیر انداخت
🔴
فکر می‌کنم امضا هنوز امروز کو چند ساعت آینده انجام شه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/alonews/127944" target="_blank">📅 19:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127939">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
کرملین: ترامپ در گفتگوی خود با پوتین، تمایل خود را برای اعمال نفوذ بر کی‌یف و شرکای اروپایی واشنگتن ابراز داشت.
🔴
پوتین و ترامپ توافق کردند که استیو ویتکاف و جرد کوشنر در آینده نزدیک دوباره به روسیه سفر کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/alonews/127939" target="_blank">📅 19:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127937">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
یه اسپویل کنم؟ جبهه منحوس پایداری بزودی دیلیت میشه. خبر دارم که میگم
😉
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/127937" target="_blank">📅 19:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127936">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
فوری/گزارشات تایید نشده از برکناری سعید جلیلی از شعام و جایگزینی باقری کنی با وی حکایت دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/127936" target="_blank">📅 19:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127935">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
فارن افرز: داشتن سلاح هسته‌ای دیگر برای جلوگیری از حملات نظامی دردناک توسط دشمنان کافی نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/127935" target="_blank">📅 19:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127934">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
پوتین با ترامپ صحبت کرد و تولد ۸۰ سالگیش رو تبریک گفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/127934" target="_blank">📅 19:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127933">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
گزارش‌هایی مبنی بر بازشدن پناهگاه‌ها در سراسر کشور اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/127933" target="_blank">📅 19:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127932">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در تماس اخیر با رئیس‌جمهور ترامپ گفت که اسرائیل با عقب‌نشینی کامل از جنوب لبنان، از جمله پنج نقطه‌ای که در حال حاضر توسط نیروهای دفاعی اسرائیل (IDF) در اختیار است، موافقت نخواهد کرد، طبق گزارش معاریو.
🔴
نتانیاهو همچنین عقب‌نشینی از خاک سوریه را که اسرائیل از زمان سقوط بشار اسد اشغال کرده است، رد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/127932" target="_blank">📅 19:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127931">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
کانال ۱۳ اسرائیل به نقل از منابع: جلسه امروز کابینه امنیتی به دلیل نگرانی از شلیک موشک از سوی ایران در یک پناهگاه مستحکم برگزار خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/127931" target="_blank">📅 19:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127930">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
طبق گزارش منتشر شده کانال ۱۲ جلسه کابینه اسرائیل در امنیتی ترین مقر اسرائیل برگزار شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/127930" target="_blank">📅 19:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127929">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMAC0kZLwGleNrGTAnqeb-Dus4AfgxNkpxudsriw-XM_tP87kzFGy-V8VTSAeo2wBCEiR9Ed_aJAfQxECPMDyIoDSLKoiMVE295Fz0yuxjUoedlkUlxTGYjaVrNgtwDuJdfE0y35NPu8hZvkhWsh9AWgTbueM-ESAXu8PyO73Rmgw0IIxW5cjVXJgUI4h6gf-Tumka7tSRGQvgAajrRR4dYl018XN3cAk71eJ49N7Vlhe2WQ8q561adegaTuY3xBLZlsTj9jKE6GhzGMkCNZnQc5PqVY43293q8s-1J9-fVcbKYnZLb7Lz-8nFCXyJBlM74k48A5kWD-i157mzJF1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سید مجید موسوی
:
گوش به فرمان ولایت باشید و از هر کلامی که اتحاد مقدس شما را به خطر می‌اندازد دوری نمایید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/127929" target="_blank">📅 19:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127928">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: آمریکا به شدت به ایران فشار میاورد که پاسخی ندهد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/127928" target="_blank">📅 19:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127927">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
کابینه امنیتی اسرائیل امشب در مکانی مخفی تشکیل جلسه خواهد داد به گزارش یدیعوت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/127927" target="_blank">📅 19:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127923">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ShaFDWDTA1zfdbkp9tCwTjfDqK_pOhtwvDoPIhqQeWLkpbsAaEP-R01Df6uBzBGNPlZfyMOECRodt0JJARawY8j3Iv6FLbwwhY-jJ6Rrt8cA9NL0p0JtUiiX_xrxFnL7tRHneKB4UklIKEi4GpTbKhPy8_XS1R3k2KxGOsCF90rZdWj4m3cxnyZOdM9B6aTv_IqqWiTsrfmnrc_Eg8S9gETEkmISJKKGkBGZebUYNpPn6rhfvS7GVk8PTcdDDqUyGiCgVbyvtaFGpnkq6u1WtEbTSSxmdSXO1mek-bHewGaAkmIfztBlW-yPmwWejDm3pghHHXSkks7I2ULLIIglyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VR1H7cvoX2tM2kXbrTWT1eb8tfhLy785-J1bWboXXWMTfdhTd3YUjl3y7Ch_Z722zDcJuMGFrwNGhSoJtHnp9tJBp-GgnolPNBNPkkNb1UzEIsxkJjNLMpsAuaiZ08NYtNVE_mNzNwtpBtnelCf7-vjPj_fo1ZzUf7UNVzRK__AXvesK5eZckt01D_UTPEK4R_Z8olY0FHyt7sQACYumGWFQnjPnA5OH-P64tIeLgm5XJROjse-97QNuuHsToYGOn6UIXK9ppcT48fPsKbmnlhlnucNY7rB0ooGl9lxLb2zcbTExO0ypMSBAf5Iq3dduKEHLxb4JiVbzck9v87qSaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mAoR2ZDAKDPBBaafN36t4QQncq8nNf5Km59ODNmqN99C530dyR8Vxl7fvbx0wMRbO3vhHsM0OLBMDGZSHB5k_WrrlPl74X-rcjzqlz3T3fdMAEd5g6JUOJB1sxwHS7l-255NE3dI0Ux47F8ddmAEBu-AiNyyEXGV20Y1R1uDK0DkpmXJmT8I_rkb6DwA83sPimIUJQUsnMpgcUYV66ZSeOfJnkQgIBsOUVeK5xaRJpY2lMk5kex9j-RF0Xs5l9vPDxiALmQ5EKODVQSK25tRorgaDof35M8rUZO7R3lJBHAdXnrXzMZs91PvJTR0HRLqH4qnEdodhau87U-FZHA1UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GKzNBnAM87SygzlHm7NhbhGH2-ZVUN-ugMIUprT23GdpKIY67Oi4CEp4BxPhY0YMVFZZVVpZ_MmjlsBqFc-NvlslA8hqHpVqCdlGWUnugF328igQyCdiy1XIkyj-bmiYYeOQ_k_Jd-56LXF-LHQDY_4HRsVeB_ye_vXV8TflyJd04bQiTlvbhOoyPWzGDhmdiuIrq9L9RpPvlj51rtql4hWndqTc2uTcZGw6BOSNGlso-nYUHyY25NQOoPhINgT2kWMKTng7ucHsni0xwxzc9_MMs8IOxB3sJgtUuaYtg59wLwhNkqRxKwswaVNk1gM6AeKt8voyxg1w1q2jhSN9pA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی به حملات هوایی خود در جنوب لبنان ادامه می‌دهند، از جمله در شوکین، المنصوری و کفر صیر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/127923" target="_blank">📅 19:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127922">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
طبق گزارش کانال ۱۴ اسرائیل، ایالات متحده در حال حاضر از طریق واسطه‌های مختلف تلاش می‌کند تا از هرگونه حمله احتمالی ایران به خاک اسرائیل جلوگیری کند.
🔴
پیامی که اسرائیل در پاسخ منتقل کرد: «اگر ایرانی‌ها به ما حمله کنند، ما به شدت و سریع پاسخ خواهیم داد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/127922" target="_blank">📅 19:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127920">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nNj9ylxOxKzwLwHgn7ZqPi00EKws1LXoIKvRAIhHcMjnrjZEORUHPkhU264jBk1G01usR-yDEqYm9YvGk9CaidHJ3uv1wmtrnQS7UN4lNMXGuJuhGW-YXXL1UzAPNlgDm8XEh6DHZSaS50BZFqD2S006tPV0Y0l_Sy8A531JUdg6Te4aC-NiY-A5wRr2aAipTh41J75P3pC60ZSCf8sJwyv4iLs7x3iAofxPszgSaVtVAOiyQSxW0EzTztnp4g_B0zjYMeSQ59QwXdFqunL_B4XNfpxtvXq9pDRlbzKIpf5tHWU4W4LWbJv-4l9i0aJg8DXDTmVCjaWvaJwT_x0IdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BMjhvsinhpFq_tywnCDJqjPqA-v4ZZ3cGZx4qzZpuCeVXCognrojH_8q7BzDjIzBTuuhjFSLEmJkCutVfofmTVlGGAShLLGq8xlWtM_c6WKczuYQi8vaQ53zT2OxIEYsYaPaGVGQNeGCcy9z1hmTqhvkthA4V7TowEyIJpIw8X0fpMLzQvzZ8MLoOF-ELGum_DH2EGxZzrfsOAWK4dM1wmNdMSrGGfENAhboYeOunBjk9GwEkE1m7AYDeAhykEnBB7_gsUlM86Vbi1T95lY-3fCat3uK8M3XxmTk7LrrW8a9_DOPPYSu34S7-a3R3qsIHZQvMeiCjcWdbei8cw84DA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملات هوایی اسرائیل به ساختمانی در تبنین، جنوب لبنان، دقایقی پیش هدف قرار گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/127920" target="_blank">📅 19:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127919">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل به نقل از یک مقام آمریکایی: حمله اسرائیل به ضاحیه، تلاشی آشکار برای نابودی توافق است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/127919" target="_blank">📅 19:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127918">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
پزشکیان: درحالی که برخی افراد بدون آنکه آثار تورم و دشواری‌های اقتصادی را در زندگی خود لمس کنند، صرفاً به بیان شعارها و دیدگاه‌هایی می‌پردازند که هزینه‌ای برای آنان ندارد و از سوی دیگر زندگی‌های مرفه دارند و تورم به معیشت آنان لطمه نمی‌زند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/127918" target="_blank">📅 19:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127917">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
واکنش پزشکیان به شایعات پیرامون استعفای وی: بنده شخصاً برای کار و تلاش و خدمتگزاری به مردم کشور هیچ تردیدی به خود راه نداده‌ام
🔴
اگر به پیش از انتخابات هم بازگردیم و این باور را داشته باشم که با آمدنم می‌توانم گره‌ای از مشکلات کشور و مردم باز کنم، قطعاً بازهم خواهم آمد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/127917" target="_blank">📅 19:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127916">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
فوری/ارتش دفاعی اسرائیل گزارش داد که موشک‌های بیشتری از حزب‌الله در خاک اسرائیل، درست در جنوب مرز لبنان-اسرائیل، اصابت کرده‌اند.
🔴
اسرائیل وعده داده بود که به ازای هر حمله حزب‌الله به شمال اسرائیل، بیروت را هدف قرار دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/127916" target="_blank">📅 18:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127915">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mW6iLLNa-qxUo9Zeshxrku4ulbF36PajprtVprctxhKtxkkuUcf_RYyF51p45TCa0KTH9EadZDZM6S1tMq5zhzP_ESHpRoqDhHpj9NPii1b0-MI1Tj-74jIgwyQJAJ5ZT1qyjJIwKEyPsJfFdabn9WnoVtHY748W4IVi4OuWYqxYcUsur8ireKmVv2XIZejd2x9iCHIYJTYkvOypFDo_jMwGadjkVzCBf9qN__Sq0HseNhQVIcj70RoRNo-eLyLTGxwRRq8L5QHvv9GitwQ3VkBuhx9rutEvOG5DSsGgWp8he38UR2oGNdvALkq4C97GXNFUelks_R9scUFhw6bhrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سوئیس به یک همه‌پرسی که قصد داشت جمعیت این کشور را تا سال ۲۰۵۰ به ۱۰ میلیون نفر محدود کند، رای منفی داد.
🔴
نتایج مقدماتی نشان داد که ۵۵ درصد به این پیشنهاد رای مخالف دادند و ۴۵ درصد آن را حمایت کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/127915" target="_blank">📅 18:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127914">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
رسانه‌های عبری اعلام کردند در پی نفوذ پهپادی از جنوب لبنان، آژیرهای هشدار در شهرک اسرائیل‌نشین «عرب العرامشه» در منطقه الجلیل غربی به صدا درآمده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/127914" target="_blank">📅 18:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127913">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
پزشکیان: هیچ فرد یا جریانی نباید خود را فراتر از سازوکارهای رسمی تصمیم‌گیری بداند
🔴
شورای عالی امنیت ملی به این جمع‌بندی رسیده است که مسیر گفت‌وگو باید دنبال شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/127913" target="_blank">📅 18:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127912">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
معاون رئیس‌جمهور JD Vance درباره ترامپ: من فکر می‌کنم رئیس‌جمهور ترامپ در سلامت کامل است. می‌دانید، شما می‌بینید که مردم در رسانه‌ها دائماً درباره این موضوع صحبت می‌کنند. حدس می‌زنم این فقط چیزی است که رسانه‌ها قرار است درباره‌اش صحبت کنند.
🔴
اما از آنچه من دیده‌ام، من واقعاً هرگز یک بار هم به خودم فکر نکرده‌ام که او استقامت یا انرژی لازم برای انجام این کار را ندارد.
🔴
اگر چیزی باشد، او استقامت و انرژی بیشتری نسبت به بسیاری از افراد کابینه دارد که ۳۰ سال از او جوان‌تر هستند.
🔴
و فکر می‌کنم این چیز خوبی است چون شما می‌خواهید رئیس‌جمهوری داشته باشید که قادر باشد هر روز آن سختی‌ها را تحمل کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/127912" target="_blank">📅 18:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127911">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
پزشکیان: تصمیم‌گیری درباره جنگ و مذاکره بر عهده رهبری و شورای عالی امنیت ملی است
🔴
همه جریان‌ها باید خود را ملزم به تبعیت از تصمیمات مبتنی بر نظر رهبر عالیقدر انقلاب بدانند.
🔴
برای بنده، حفظ وحدت و انسجام جامعه از هر موضوع دیگری اهمیت بیشتری دارد. در بسیاری از موارد، با وجود امکان طرح برخی دیدگاه‌ها و مواضع، ترجیح داده‌ام از بیان آنها خودداری شود تا مبادا کوچک‌ترین آسیبی به انسجام ملی و همبستگی اجتماعی کشور وارد شود.
🔴
امروز بزرگ‌ترین چالش ما، تلاش برخی برای ایجاد گسست و شکاف در درون جامعه است؛ موضوعی که دشمن نیز دقیقاً در انتظار آن است. کسانی که خود را مدافع ولایت و رهبری می‌دانند، بیش از دیگران باید به سیاست‌ها، چارچوب‌ها و تصمیمات رسمی کشور پایبند باشند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/127911" target="_blank">📅 18:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127910">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
پزشکیان: آنچه گاها در رسانه ملی درباره جنگ و مذاکره مطرح می‌شود، لزوماً بازتاب‌دهنده دیدگاه شورای عالی امنیت ملی، شورای عالی دفاع یا حتی رهنمودهای رهبر معظم انقلاب نیست؛ در حالی که انتظار می‌رود رسانه ملی منعکس‌کننده سیاست‌ها و رویکردهای مراجع رسمی تصمیم‌گیری کشور باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/127910" target="_blank">📅 18:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127909">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
طبق گفته مقامات چینی: یک شهروند آمریکایی به نام مین زین، طبق ادعاهای جاسوسی در چین دستگیر شد.
🔴
سخنگوی وزارت خارجه چین، لین جیان، گفت که مین زین «به طور قانونی تحت اقدامات اجباری کیفری» قرار گرفته است به دلیل سوءظن در انجام فعالیت‌های جاسوسی که امنیت ملی چین را تهدید می‌کند.
🔴
مقامات چینی جزئیات بیشتری درباره ادعاها یا تحقیقات ارائه نکردند، اما گفتند که کنسولگری عمومی ایالات متحده در گوانگژو از این پرونده مطلع شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/127909" target="_blank">📅 18:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127908">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
وزیر جنگ آمریکا: واشنگتن گزینه نظامی را در طول ۶۰ روز مذاکرات حفظ خواهد کرد و تا زمانی که لازم باشد فشار بر ایران را ادامه خواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/127908" target="_blank">📅 18:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127907">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ea33d2833.mp4?token=vq3XBJ3Ym1qpDUvYi6sLd5PPn1tBPINuqWZCFN0j-b11bkktZCiezvPGS9MiUQFWyLdO-JR3aKSjkNPkqnScIoKqqugLNeN4KC8NHxG0kyJnXsLFeoWYY5zWQZtMF9sorbHwXPjg_WIGynvgPclMMNjVMGJjKxYbBN0m4iz6TI4_J9JOFc_cZem9i9W6b69jze9GIMhASXmZeQQNQse3SV2fjRWvQZZ_-fdvtRb4ZKZeDqorZ5ZHQld16MVCqvWRahd-vb_UaRJZ_WsuyISN1Dj_UWiVV2ItuXM-hh10TdQZd7VUhZfF-_HrFaupP4S4aQ3VoH4r0h_KEYTcffiI7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ea33d2833.mp4?token=vq3XBJ3Ym1qpDUvYi6sLd5PPn1tBPINuqWZCFN0j-b11bkktZCiezvPGS9MiUQFWyLdO-JR3aKSjkNPkqnScIoKqqugLNeN4KC8NHxG0kyJnXsLFeoWYY5zWQZtMF9sorbHwXPjg_WIGynvgPclMMNjVMGJjKxYbBN0m4iz6TI4_J9JOFc_cZem9i9W6b69jze9GIMhASXmZeQQNQse3SV2fjRWvQZZ_-fdvtRb4ZKZeDqorZ5ZHQld16MVCqvWRahd-vb_UaRJZ_WsuyISN1Dj_UWiVV2ItuXM-hh10TdQZd7VUhZfF-_HrFaupP4S4aQ3VoH4r0h_KEYTcffiI7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هگِست : پروژه آزادی هیچ‌وقت متوقف نشده؛ ما تا حالا ۱۲۵ میلیون بشکه نفت رو از تنگه عبور دادیم، ایران هم هیچ کاری نتونست بکنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/127907" target="_blank">📅 18:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127906">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
هگست درباره توافق ایران: تا جایی که می‌دانم، ما در مسیر امضای توافق هستیم. مسئله این است که کی، نه اینکه آیا.
🔴
اسرائیل در پاسخ به حزب‌الله بسیار محتاط است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/127906" target="_blank">📅 18:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127905">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZpLTSRLKUFNT9jQI2j1UwnQW2Wk6xIe3ybmSMBht0hfjiZyiQ1B-Ck1BIXQNq8wP1FO4qR2ucqD2u4w_XThLPW7UDjrOWb1xVJzbaOcDMtS2qn0l-u82dJQNwqHq8oDWzkd1unQrgjRyz3oJZbq3rWhJjKUWLkb6nDTnvf6zdPWQyFija1cUie2oMju1i2BOOhnkrU6wz9NrHXnTFwyb3t9WWxBUn73xSRiEtYBGvpoYXHgqCdFxILFL_yioGbQZj_1CKLCT83s7dGFZuQeurY3upImTc_HzF-OvjZv1XzmDQdzfWYBRbBSZ1uUPTj52IaW2gdGd6r9ROqTvV78UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس‌جمهور اوکراین، زلنسکی، و رئیس‌جمهور ترامپ امروز تماس تلفنی داشتند که در آن زلنسکی تولد ترامپ را تبریک گفت، طبق گزارش RBC-اوکراین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/127905" target="_blank">📅 18:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127904">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b98c3eb0c0.mp4?token=pl9vWrwx1ew6E_LCmSPvTRebiK-mxWf2UWTeg2G4V251QNWwgqlwLeDl7__ucTJXflIixscu6Gclp12L3kgEgZr1NGZHQyy-Cja6nznNaT272JWIt5ZN9lYRGVQCGp_2SbmwIF_rv8jUbCYVKA2MXz0miaCZ8Rh66pK8lI478tPf3-7EkmRqOwZ6ItG0C_7DX0LLGnAFEO4ROgMS7UZsCkhyaFUa34p6UVmJi1UMUInzdTU-5VUnl7YiKRj-YIIzJcba-jK19f3MqP47DMjhPAnGeTx1GK00Jhz-8QeynbmmGH8Bupf9f9FAnsWaCrX4636rkvvdfNNfjpFg7zZEpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b98c3eb0c0.mp4?token=pl9vWrwx1ew6E_LCmSPvTRebiK-mxWf2UWTeg2G4V251QNWwgqlwLeDl7__ucTJXflIixscu6Gclp12L3kgEgZr1NGZHQyy-Cja6nznNaT272JWIt5ZN9lYRGVQCGp_2SbmwIF_rv8jUbCYVKA2MXz0miaCZ8Rh66pK8lI478tPf3-7EkmRqOwZ6ItG0C_7DX0LLGnAFEO4ROgMS7UZsCkhyaFUa34p6UVmJi1UMUInzdTU-5VUnl7YiKRj-YIIzJcba-jK19f3MqP47DMjhPAnGeTx1GK00Jhz-8QeynbmmGH8Bupf9f9FAnsWaCrX4636rkvvdfNNfjpFg7zZEpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برنان: اما الان با آن ذخایر سلاح‌ها مشکلی وجود دارد؟
🔴
پیت هگستث: خیر، چنین چیزی نیست. این داستانی ساختگی است که رسانه‌ها می‌خواهند آن را پخش کنند. ذخایر ما عالی هستند و فقط قوی‌تر می‌شوند.
🔴
برنان: شما در مقابل کنگره در این باره شهادت داده‌اید.
🔴
هگستث: لازم نیست برایم آنچه را که شهادت داده‌ام دوباره بخوانید... من حدس زدم که برخی مهمات زمان بیشتری نسبت به بقیه می‌برند. ما بیشتر از همیشه در حال ساخت هستیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/127904" target="_blank">📅 18:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127903">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67802ef8f8.mp4?token=FDqUQMJyXCf1cZkXBYzdOOoHPv0u3yCbMft2UEiRoAO9XR5-_U_96V7ZTNdZMaqqx8wk60jAe8LDCkk1RgeqfGZbLQJPeNMK-cCGzruC3UMeDfZORVQRjV3nKCkb3iuhm2Gbu69mapykVsR68L3dkHSdDR7O-pu9zduTl__yEbJGrHKyNr0LrxcLZcAqQjXriQjN1ky30g6XcA15jwMeZzJypMahOBgvdIb-tCFHhmLvZYWRhH8YNyyBXGEKwJ4ROb8zyfi0iOWTXwQp3zg5f3w2YhT25wpWoFKRCRyGVmWMWXCSi3v3KsXE6yI_X2o0N1wZTvYPBS06QKTOxY4Dmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67802ef8f8.mp4?token=FDqUQMJyXCf1cZkXBYzdOOoHPv0u3yCbMft2UEiRoAO9XR5-_U_96V7ZTNdZMaqqx8wk60jAe8LDCkk1RgeqfGZbLQJPeNMK-cCGzruC3UMeDfZORVQRjV3nKCkb3iuhm2Gbu69mapykVsR68L3dkHSdDR7O-pu9zduTl__yEbJGrHKyNr0LrxcLZcAqQjXriQjN1ky30g6XcA15jwMeZzJypMahOBgvdIb-tCFHhmLvZYWRhH8YNyyBXGEKwJ4ROb8zyfi0iOWTXwQp3zg5f3w2YhT25wpWoFKRCRyGVmWMWXCSi3v3KsXE6yI_X2o0N1wZTvYPBS06QKTOxY4Dmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برنان: با توجه به اینکه ارتش آمریکا همین حالا این عملیات را در ونزوئلا انجام داده است، آیا آمریکایی‌ها باید بفهمند که آمریکا همچنان از نظر نظامی در آنجا حضور خواهد داشت؟ آیا باید انتظار عملیات مشابهی در جاهایی مانند اکوادور و گواتمالا را داشته باشند؟
🔴
پیت هگست: بله، باید اینطور باشد. این یک تقویت شگفت‌انگیز از «دکترین دونرو» است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/127903" target="_blank">📅 18:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127902">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e835a4772c.mp4?token=Kj0HHJRg_fka9zEmaZeWJC-eUYk9JAKVtzrMdH4lQ9y-YAET8JLNq-p6vmLuoYC3oFkp_msz84t2cUVYdQhUM9G4DahR_vUfq_Wl6KXXJ4-T2X06k49t14qnAAqlheUNAK0ABPhWeMUk3PEAunoP2OEA9kfHp1XyRkGmrzAbtNGCs0PXYqBs1Z_kFSg5Y1tmhtRqJsI1l9jhNPotItW1VBE2gI_ZtMIcYxMGDWxS-NZSGkUVqb591zAnldk7qMclaBGGsz_t-aUITh7e3LNZiYT1SLwjFD5vkPyHfGuAgrW9l19LAy-GlTjR2OZ0RNPKkKXrh9DQxuUOiRte9U2LgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e835a4772c.mp4?token=Kj0HHJRg_fka9zEmaZeWJC-eUYk9JAKVtzrMdH4lQ9y-YAET8JLNq-p6vmLuoYC3oFkp_msz84t2cUVYdQhUM9G4DahR_vUfq_Wl6KXXJ4-T2X06k49t14qnAAqlheUNAK0ABPhWeMUk3PEAunoP2OEA9kfHp1XyRkGmrzAbtNGCs0PXYqBs1Z_kFSg5Y1tmhtRqJsI1l9jhNPotItW1VBE2gI_ZtMIcYxMGDWxS-NZSGkUVqb591zAnldk7qMclaBGGsz_t-aUITh7e3LNZiYT1SLwjFD5vkPyHfGuAgrW9l19LAy-GlTjR2OZ0RNPKkKXrh9DQxuUOiRte9U2LgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگستث: به خاطر دوراندیشی رئیس‌جمهور ترامپ، ما در داخل کشور به استقلال انرژی دست یافته‌ایم.
🔴
برنان: قیمت انرژی در حال حاضر نسبتاً بالاست، بنابراین نمی‌دانم این استقلال چقدر به مردم در پمپ بنزین کمک می‌کند.
🔴
هگستث: قیمت‌ها در حال کاهش است و شما این را دیده‌اید. هه هه هه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/127902" target="_blank">📅 18:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127901">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b3db14adb.mp4?token=tsZB8WJFVREOezmgWeisUJ_Tf50LxcqlVAu8fzZRdlEzTibZwSxYlGrN9sOaLNobRLgeyxRSVf50GTF38R2EKlWiTVbXFFOgju2DNAtZr64_gIZw2LXRN8am6phQvjuEQjWc01l6GxlqBo4Fgxb_LlsYNrqurzNRoNC9cnU17x5z9DiLEF6Wij_NvuL_K_jegzevVjTdejOF-Apkx-hhMxcMLcBiCiAlmGvG1BSQK1fOMPKvxvnW8FB0R2gNffV17obZ0rycpfZCCuTtsc04T7N3043aBgGTmYvd45_71e5ZQ1xvnaoLRzd155AsaXUWwDehJ79WyZu7QjlxBcgnHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b3db14adb.mp4?token=tsZB8WJFVREOezmgWeisUJ_Tf50LxcqlVAu8fzZRdlEzTibZwSxYlGrN9sOaLNobRLgeyxRSVf50GTF38R2EKlWiTVbXFFOgju2DNAtZr64_gIZw2LXRN8am6phQvjuEQjWc01l6GxlqBo4Fgxb_LlsYNrqurzNRoNC9cnU17x5z9DiLEF6Wij_NvuL_K_jegzevVjTdejOF-Apkx-hhMxcMLcBiCiAlmGvG1BSQK1fOMPKvxvnW8FB0R2gNffV17obZ0rycpfZCCuTtsc04T7N3043aBgGTmYvd45_71e5ZQ1xvnaoLRzd155AsaXUWwDehJ79WyZu7QjlxBcgnHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگستث: این قدرت رئیس‌جمهور ترامپ بود که ایران را به این توافق واداشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/127901" target="_blank">📅 18:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127900">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/852e5d3abd.mp4?token=YGDmmpDb94ZnHjNIOfXj-qZjT-xovAZwcLVZRrUmUiJor08hy0a7zeMqq9PJk-JPD8TzCb3DeEpXtU84Nf8xjilhLu2LjeuRYj47XTqHJjGRM4fBMHWaEslWx0j_lNnC6lWwOdQjYT3mXbmQqPGK6IuAcAW4k4k2XJAhRvMUTT7Fk5o_8DuXeexIGFKNPCbmTEOJQk9aOlVwYr2vhjKBPy7GxZPoEvJ6MYRsAAMc2OB4U4cEGLAZR6YqU040lmw843osC01f2HXl_zfE_xv5IM_w4TGU6WCVZtZgQfOh8szG6bQ0O1uPSKlzT_Mz-LWl7swi8OEpcNeUC45Z64CPwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/852e5d3abd.mp4?token=YGDmmpDb94ZnHjNIOfXj-qZjT-xovAZwcLVZRrUmUiJor08hy0a7zeMqq9PJk-JPD8TzCb3DeEpXtU84Nf8xjilhLu2LjeuRYj47XTqHJjGRM4fBMHWaEslWx0j_lNnC6lWwOdQjYT3mXbmQqPGK6IuAcAW4k4k2XJAhRvMUTT7Fk5o_8DuXeexIGFKNPCbmTEOJQk9aOlVwYr2vhjKBPy7GxZPoEvJ6MYRsAAMc2OB4U4cEGLAZR6YqU040lmw843osC01f2HXl_zfE_xv5IM_w4TGU6WCVZtZgQfOh8szG6bQ0O1uPSKlzT_Mz-LWl7swi8OEpcNeUC45Z64CPwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگستث: ایران نمی‌تواند قابلیت‌های خود را در اطراف تنگه ببیند و درک کند، به‌ویژه در چند شب گذشته که برای آن‌ها بسیار ویرانگر بود از نظر توانایی‌شان در فهمیدن آنچه در تنگه می‌گذرد.
🔴
وقتی این توافق امضا شود، انتظار ما این است که ایران شلیک پهپاد به کشتی‌های تجاری را متوقف کند.
🔴
برنان: آن‌ها همین کار را جمعه گذشته انجام دادند. یک پهپاد هفته گذشته با یک هلیکوپتر آپاچی برخورد کرد. آن‌ها هنوز توانایی آسیب رساندن به دوستان و شرکای ما را دارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/127900" target="_blank">📅 18:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127899">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adf1af4a34.mp4?token=NTf8b0RQrDjJLTPC3-DjkX_dsIo8s14Od9bNg1nZ0JIe2OUeA7U0RAQJ0iR3dk9cOz7cu9qQZyon1mmGvf5nVvF1RYAZ75fpEkDCDddjYqSCXy-UsStD6XmXGTb0yGa8tbGvzvZCWfOE2YMzoO78b_zrwg92up1k1_lp1vxyAHnXwKnEpe_nmR0sP8oti6NxiZtKINt8Tyn63y3W_2u3SyW8dOzoCg3gxfgVsYcEfzmDX5lNvAWKZqMpv789bDEZyFAJw15O-xT5A_AcYRZsE1BSKDEs3uS26WF1ds0vxt8xGglyUBSlqer7p8F6dW0Qrhx6xoTx31arNDiXLdXEsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adf1af4a34.mp4?token=NTf8b0RQrDjJLTPC3-DjkX_dsIo8s14Od9bNg1nZ0JIe2OUeA7U0RAQJ0iR3dk9cOz7cu9qQZyon1mmGvf5nVvF1RYAZ75fpEkDCDddjYqSCXy-UsStD6XmXGTb0yGa8tbGvzvZCWfOE2YMzoO78b_zrwg92up1k1_lp1vxyAHnXwKnEpe_nmR0sP8oti6NxiZtKINt8Tyn63y3W_2u3SyW8dOzoCg3gxfgVsYcEfzmDX5lNvAWKZqMpv789bDEZyFAJw15O-xT5A_AcYRZsE1BSKDEs3uS26WF1ds0vxt8xGglyUBSlqer7p8F6dW0Qrhx6xoTx31arNDiXLdXEsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هگِستِ : ما کل این مدت کنترل تنگه‌ها رو دستمون داشتیم
🔴
مجری : پس چرا دارید باهاشون مذاکره می‌کنید که دوباره بازش کنن؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/127899" target="_blank">📅 18:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127898">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3NyQ3WAVZII667pkggjSHORtJ-uRuCKp4bOpmBu3IKDA2HW1ZwQOAHy2nAm1kN_rrk9-TjuhtyuxlG43118ubd3npJgyvZEKqIOOnk0A2ZhkrPy87BI-YYc_E9t0g1Irulmgf8fZqmfJJFHeSU-LnXGPkG-T9KGwcmPy2xJuYmNkXFSz7hEu0W5iWG6ogjeIy6UzMpUx77zyBQp7kTBNoF_LhvpMsre2O5_8zHTToVRjhz6x7JV6uKHjCrQ5L5Xuwa90KSBXEmKDUTHbE7K--DU5SCzhWe0TBLK9VGUsti9OnkrGZiZmOc8AoUC3pTNT03lQQbxwhTEkxAUraC8AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری
/
ترامپ: حمله صبح امروز به بیروت نباید اتفاق می افتاد، به ویژه در روز خاصی که ما به توافق صلح با ایران بسیار نزدیک هستیم.
🔴
اسرائیل حق دارد از خود دفاع کند، اما حمله ای که به آن پاسخ داد بسیار کوچک و بی معنی بود، کسی آسیب ندید، مجروح یا کشته نشد و نباید این روند مهم را مختل کند.
🔴
دیگر نباید در هیچ کجای لبنان حملاتی از سوی اسرائیل انجام شود، اما همچنین نباید از سوی هیچ طرف دیگری از جمله حزب الله علیه اسرائیل حمله شود.
🔴
این می تواند آغاز یک صلح طولانی و زیبا باشد - بیایید آن را منفجر نکنیم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/127898" target="_blank">📅 18:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127897">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1126f6794e.mp4?token=htMfXfQSDm0WagQuw-lmzP77lna1_-nMv2xjtddGdeMfcUq94IkZA5xmGy1AWoyS37BZUY7PmDQVDMpTAigjFonaM5hiu_YRFP6hbbc5zKzoLp5kGTkZKUz5N1lYOjkyGPPY3TiyB7jhrQgI2bfVTY5ltPlCAkRsTEVikLstq0pfXZntpRYdJq_r59fHXkcdmbYjJLwUasVqbjlnPt4mDMxMpfNcdUVZd-__xd3gzePvk3b6ly8vbrAAba3-mJMv82UDiUDYIFz3tEdaqf-md2b5MAcjfCXP_zAJTRLCWEvf0BqEAtHjw5dgrxLVJ18AcZlbzhLSetORzx-zpEi-dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1126f6794e.mp4?token=htMfXfQSDm0WagQuw-lmzP77lna1_-nMv2xjtddGdeMfcUq94IkZA5xmGy1AWoyS37BZUY7PmDQVDMpTAigjFonaM5hiu_YRFP6hbbc5zKzoLp5kGTkZKUz5N1lYOjkyGPPY3TiyB7jhrQgI2bfVTY5ltPlCAkRsTEVikLstq0pfXZntpRYdJq_r59fHXkcdmbYjJLwUasVqbjlnPt4mDMxMpfNcdUVZd-__xd3gzePvk3b6ly8vbrAAba3-mJMv82UDiUDYIFz3tEdaqf-md2b5MAcjfCXP_zAJTRLCWEvf0BqEAtHjw5dgrxLVJ18AcZlbzhLSetORzx-zpEi-dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر جنگ، هگِستِ : برخلاف اوباما، رئیس‌جمهور ترامپ تو این چیزا باهوشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/127897" target="_blank">📅 18:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127896">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb30e70b3.mp4?token=ftc2R1zZXh31aR2s0WUlZLUBcfPQZzcr6-48xJhVg3uXPionMWiOc7tNIIbm4hf48VCWPvWXLbQFqmEO-D9WWog9DeRiNbKtpsa2VKjSnXlsW1rteVb7YY7Vph2K8d3Zb6sbTcjdk5DdcXaCpQBx-O00G3UXQiQlZhcbSMoqVboEINzUuKuyZ_YIt7qGAAmKKlFFDrcvF7nkAjaCPaTzf4fW66XV3WS2OJad8d6kiUWvKCoXlKJ0ROq-l2wQZNkqpwxTR-RLIbPZDG0VMALlQxqulV0xDTmBLObtpp-mrDiOo2QUYntvR80tRq5Al04JM3VOweKD3IiuNzN_6BY8aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb30e70b3.mp4?token=ftc2R1zZXh31aR2s0WUlZLUBcfPQZzcr6-48xJhVg3uXPionMWiOc7tNIIbm4hf48VCWPvWXLbQFqmEO-D9WWog9DeRiNbKtpsa2VKjSnXlsW1rteVb7YY7Vph2K8d3Zb6sbTcjdk5DdcXaCpQBx-O00G3UXQiQlZhcbSMoqVboEINzUuKuyZ_YIt7qGAAmKKlFFDrcvF7nkAjaCPaTzf4fW66XV3WS2OJad8d6kiUWvKCoXlKJ0ROq-l2wQZNkqpwxTR-RLIbPZDG0VMALlQxqulV0xDTmBLObtpp-mrDiOo2QUYntvR80tRq5Al04JM3VOweKD3IiuNzN_6BY8aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جِی‌دی ونس درباره ایران:
من فکر می‌کنم رئیس‌جمهور ترامپ هم همین‌طور است. فکر می‌کنم هر دوی ما عموماً نسبت به درگیری‌های نظامی خارجی شکاک هستیم.
🔴
اما اساساً، این به این معنا نیست که هرگز نمی‌توان از نیروی نظامی استفاده کرد، و من فکر می‌کنم هدف اینجا جلوگیری از داشتن سلاح هسته‌ای توسط ایرانی‌ها است—ما در رسیدن به این هدف موفق خواهیم بود—و وقتی موفق شویم، این نتیجه‌ای بسیار خوب برای مردم آمریکا خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/127896" target="_blank">📅 18:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127895">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
هم دفنش نکردن
🔴
هم ۱۰۰ شب تو خیابونا عروسی گرفتن
🔴
هم با قاتلش توافق کردن
🤔
هرچه از حرام زاده بودن عرزشی ها گفته بشه کمه
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/127895" target="_blank">📅 18:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127894">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
مقام ارشد اسرائیلی به کان:
حمله ایران اکنون قریب‌الوقوع به نظر می‌رسد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/127894" target="_blank">📅 18:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127893">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
هگست وزیر جنگ آمریکا: من انتظار ندارم که حملات اسرائیل به حومه جنوبی بیروت مانع توافق با ایران شود. اگر ایران می‌خواهد این موضوع ادامه پیدا کند، باید حزب‌الله را مهار کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/127893" target="_blank">📅 18:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127892">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee6c0f0321.mp4?token=NpnJQX7HI1p9UYCRtUvgr43lDVAwrzGgEwVuTJ7uFv8prpcMHtk8UT4nRkqIBfyYuJTHKKPM0Glm_k_QzPETp9ZZmoGTqeTRZ1Nj7zbNL4lMCDNqhJI3_gnXSv_j1zIHqRkcjNMGaLoj3Q2Fme6QaRdcx_2SfkMVQLeXSr_2bFORQU_ukApQACkFW7cIg5ArizhLXJCaPgvZMXxKBupT2urSP7zDB2A_6E3f_5ZfrxZn2-ZtXfxJRTgT8BIxCIeVFX-mH8_tH23-RsWYOXu6pGtdi3oEGWiYPpwI_c4bMM3QbUd-Us78KWG_C9aBPrpMzWNmWJIPWxkuZCzms-PBDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee6c0f0321.mp4?token=NpnJQX7HI1p9UYCRtUvgr43lDVAwrzGgEwVuTJ7uFv8prpcMHtk8UT4nRkqIBfyYuJTHKKPM0Glm_k_QzPETp9ZZmoGTqeTRZ1Nj7zbNL4lMCDNqhJI3_gnXSv_j1zIHqRkcjNMGaLoj3Q2Fme6QaRdcx_2SfkMVQLeXSr_2bFORQU_ukApQACkFW7cIg5ArizhLXJCaPgvZMXxKBupT2urSP7zDB2A_6E3f_5ZfrxZn2-ZtXfxJRTgT8BIxCIeVFX-mH8_tH23-RsWYOXu6pGtdi3oEGWiYPpwI_c4bMM3QbUd-Us78KWG_C9aBPrpMzWNmWJIPWxkuZCzms-PBDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مایک والتز، نماینده دولت آمریکا در سازمان ملل با اطمینان اعلام کرد که امروز توافق میان ایران و آمریکا امضا خواهد شد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/127892" target="_blank">📅 18:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127891">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
مهاجرانی، سخنگوی دولت:تصمیم‌گیری درباره تفاهم احتمالی با آمریکا در سطح «نظام و حاکمیت» انجام می‌شه و حمله به مذاکره‌کنندگان، حمله به یک «تصمیم ملیه».
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/127891" target="_blank">📅 18:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127890">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edV84_3o6K6Lqd-pYk9BImb7oAc3aTGPkmgtgZz_unbxUW9VBSlchz-qSlT6zHpBcdS-QFs2zGtVxCr63BO6f9zDWjn4MdHwUwGMNjOwbfhS13uAin5puInIqzNYkxCeD88beC9QQlfwKg6Nk9ZIbLImuHI6BwsjZKJm75gLdxZp3qtmJhyAbKpQq4-srxHjt2q7_vpBkRtcejWRuW-xNtMeDn2YEdl3kmLE-_Mh1lZz3eMAkhC2U-AuePDhIHZwXibo2VrZYvph8N27b_BgpAiB4k3FJBmeZA-q-bojWmigloJzk6mRf5j-azg32k1bQhF3wFpMnRYr86exavx33g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیده شده درحال اعزام به تجمع پایداری‌ها
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/127890" target="_blank">📅 18:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127889">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4897b39440.mp4?token=R0i0j0-4PI2Y_4jinyJqysGzE7ppyc1iLBsh9HXePV_GvKhHlCv7LqVIRpnqcvJB6nUANp-Yp1r5byzQvLu7yxs608iLtanZpiMP9txyu4owLsSSIbgSXqDVmcdxxpr2vfwPWbfy0YNCUBtLfrpwHzwUZ3JfBBbheS8iIy1A1bqh44H_mtJv3RB_OVr41WGGuDV__CiLSSHO0NPHAM1ij_wZI4Ct1nbdek4Y0ShtSXImFzClKGb4O8aXiiDsVKvy8EQJ4Lmd4qM6etOL-1nS1V90ca4EcMrFqDQpYaEeld8VUdqPdM9rJg7emSm7q8wda50Q8y1hBPhQCPjz2XMxWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4897b39440.mp4?token=R0i0j0-4PI2Y_4jinyJqysGzE7ppyc1iLBsh9HXePV_GvKhHlCv7LqVIRpnqcvJB6nUANp-Yp1r5byzQvLu7yxs608iLtanZpiMP9txyu4owLsSSIbgSXqDVmcdxxpr2vfwPWbfy0YNCUBtLfrpwHzwUZ3JfBBbheS8iIy1A1bqh44H_mtJv3RB_OVr41WGGuDV__CiLSSHO0NPHAM1ij_wZI4Ct1nbdek4Y0ShtSXImFzClKGb4O8aXiiDsVKvy8EQJ4Lmd4qM6etOL-1nS1V90ca4EcMrFqDQpYaEeld8VUdqPdM9rJg7emSm7q8wda50Q8y1hBPhQCPjz2XMxWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کلیپی از یه حامی حکومت:
آقای عراقچی شما گوه میخوری وقتی رهبر چیزی نگفته حرف از مذاکره میزنی.
اگه می‌خواین مذاکره کنین اول باید خون منو بریزین، خون آقامون هنوز خشک نشده، بیجا میکنی مذاکره کردی.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/127889" target="_blank">📅 17:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127888">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
سخنگوی ارتش اسرائیل: ما برای احتمال شلیک به خاک اسرائیل در ساعات آینده آماده می‌شویم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/127888" target="_blank">📅 17:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127887">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
کانال 15 اسرائیل:
تمام سامانه های پدافندی در اسرائیل به حالت آماده باش کامل درآمدند و در انتظار پرتاب موشک قریب‌الوقوع از سمت ایران می‌باشند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/127887" target="_blank">📅 17:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127886">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
کانال 14 اسرائیل:
اسرائیل ارزیابی میکنه که ایران در واکنش به حمله در حومه جنوبی بیروت، حمله موشکی به خاک اسرائیل انجام خواهد داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/127886" target="_blank">📅 17:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127885">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JwyiavCfM73PBj3LtAjS7l3tvd2v9dieim9g_AEN9diziNqAxy8EN_yq7C5H5cISlGxMXWjQTyJ0LBqseMjjE9ssR_3rTS4A4Kdc0V76PVwU8FmZn2o2TTi-BosgkJqE8oiq8zAra57-D6euk1JDz_0Fa2hHZBPGF_Fcio7vDFuGLiK6jKbDr7mb1Ml7u2QP6Mz60T13aiT1sLywQ4y6uBBgSgn5j0WAFd0N6JT6swQ8ItJHNq6aR2ObvlziRkgbza7VIDLaRZVhw5fosXlGQgmMG-De_jXDJnR1AQ7hLi6nPIhpWQvtRWeLjHHujIEYhNLArH88QkeKicSPSIMDsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی عضو تیم مذاکره کننده:
فعلاً مذاکره دیگری در کار نخواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/127885" target="_blank">📅 17:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127884">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4QPERifjeO-6C6xvAG37p7WB9gdDlQtTD4bIRMBbXaG5fTd8-h1TAqeMG-EHWXM3RyFcfo4aq9VCZyHX050fvKaNsYm-o5uUP2To78w2n0crK6Q3vc7FvBLNLqo9fHJreU3ZW3pcF0SVsVsq1B_1OHM2GAlHD8Glh-L8l6YPTTP4A39YXdsyCGeIooIvt2xyjbiORoXRn9IKxYFiFC56iIBZdkvWfrWsYfaL6awWu4KHt1kutO7qxEa8US4eo12b9e-0ahcY3cNKtUBLohDgp8v1lnq7nwCnoPuStLLf91R7r52Xv5hJ_X5YH2aF-PHKSwJFQ9bvhHQL0amAdVDPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار الجزیره:
بر اساس آنچه چند روز پیش نوشتم، و با توجه به ابعاد تازه لبنان، افزایش مخالفت‌ها در داخل ایران با توافق، تردیدهای مداوم در مورد تعهد واشنگتن به تعهداتش، تغییر مواضع دونالد ترامپ هر روز و اصرار اسرائیل بر شرایط غیرممکن خود، هرگونه توافقی بین واشنگتن و تهران بیشتر شبیه یک سراب است.
🔴
در دوردست‌ها به نظر می‌رسد و نشان می‌دهد که رسیدن به آن فقط مسئله زمان است. سپس محو می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/127884" target="_blank">📅 17:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127882">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
تتر هم اکنون 173000تومان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/127882" target="_blank">📅 17:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127881">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
الحدث به نقل از منابع:
علی الحاج، فرمانده حزب‌الله، در حمله هوایی اسرائیل به حومه بیروت ترور شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/127881" target="_blank">📅 16:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127880">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9U-fH57KY4qRWFbn6NWQL5q5Hutek9l0RgnVgS7eAYFpePEtni62G7stoVuU2pgVTmgmfGkm8YD_LK04Go-5ofERM7S3rcjYimIYavzseZA_Nr4ZTgef3NylsgEuB0L0apuXj_6w-__P0BwE5acADw6dVvGn4punKdlFcSLu7aULCM1Ul580FULVqoeCyeOZxHBcUQqoNCJBC_GZHKP099YNm8hv4DsPf374vo1jJ4N17BtfJ9uERKfattwOpnzuwJKjFf_HUp6lOaScQGdc0lZcMwPRD_MHQL5iii_vDqspbAALTook89QsgggIWHUk82WbW-yZ8GusopvJjq8tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل: هدف حمله نعیم قاسم نبود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/127880" target="_blank">📅 16:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127879">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/127879" target="_blank">📅 16:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127878">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚀
Exo VPN | سریع، پایدار و بدون تبلیغات
✅
اتصال سریع و پایدار
✅
سرورهای متعدد جهانی
✅
حفظ حریم خصوصی
✅
کاملاً رایگان و بدون تبلیغات
📌
دانلود از گوگل پلی: https://play.google.com/store/apps/details?id=exo.vpn.app
📣
کانال رسمی: @exovpn_dl</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/127878" target="_blank">📅 16:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127877">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXoCSqlZnp8UBSPnzE1t7yqScgnBICDcxrNQqZVc8IpH71q__D1OXVD8WM7RBxFTUoy91SEXnk5jpVsItLXrmbPkmLVqHWdPYgAhbOE8wcY_EC6WHFtTROude9IJyqOOHqHM-3zCxsMTHhwIT2Oowr19VyZZwkXUNgyhwg-Sz5U5uCbaFSLeco24mgPhHCmIl-v5sdpGOcafIM4pcGDoELIGObyiIMEyAPrPbUcPH5JteeOGiXqz3cX3OZ-C-wb2wOT1RFqhZ5YXsWEicU_a08mx_9XKvV1u-JdDXJ9gBjIxe3VqOwSyDZU2HFOuXMm5V4Tqqh3NfI9xiMXYHKrWfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Exo VPN | سریع، پایدار و بدون تبلیغات
✅
اتصال سریع و پایدار
✅
سرورهای متعدد جهانی
✅
حفظ حریم خصوصی
✅
کاملاً رایگان و بدون تبلیغات
📌
دانلود از گوگل پلی:
https://play.google.com/store/apps/details?id=exo.vpn.app
📣
کانال رسمی:
@exovpn_dl</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/127877" target="_blank">📅 16:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127876">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f5b803eb5.mp4?token=FBm_zWRFG5nfpW9rFiQaEkvkkEgl-Un2-BtniIndbHU8LD3aS7K9XUjCBiwsJ4ITba2pfroAaRCyAaehQ0oYqI2B2yf6_bg4flR-wxvPnjHNVcW_6ibsloJ-OglLjRuTbQ7VC8Ta7A4rK7YM6Ye6n3gytU1VfIupK7XFDPHL8rRADglr2xluuE5Ob4AMzT2w3FU0eJgHkYASK0wX7kegeM8zhuvB9Bd4FvF-tGL-5dpz9_5hkLXr6uBX6WnhTBlYdSePQsL_cjfUWZIs2VbNBPmgP9s7BzDv91OFL4vB5WtTMGATxHHMpK_KOP9zs3GDn3JLx-EUIbfJXM_Rkw6aeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f5b803eb5.mp4?token=FBm_zWRFG5nfpW9rFiQaEkvkkEgl-Un2-BtniIndbHU8LD3aS7K9XUjCBiwsJ4ITba2pfroAaRCyAaehQ0oYqI2B2yf6_bg4flR-wxvPnjHNVcW_6ibsloJ-OglLjRuTbQ7VC8Ta7A4rK7YM6Ye6n3gytU1VfIupK7XFDPHL8rRADglr2xluuE5Ob4AMzT2w3FU0eJgHkYASK0wX7kegeM8zhuvB9Bd4FvF-tGL-5dpz9_5hkLXr6uBX6WnhTBlYdSePQsL_cjfUWZIs2VbNBPmgP9s7BzDv91OFL4vB5WtTMGATxHHMpK_KOP9zs3GDn3JLx-EUIbfJXM_Rkw6aeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیو دیده نشده از هوچی گری دیشب تندروها
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/127876" target="_blank">📅 16:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127875">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70115bf6a8.mp4?token=NgCjdnBDn7osCnkty4FislCdn6ciVTl8vwm9mqnimxvS1Vw1_FYiHoUQNJxDOCmTQvkLhQ0w924Anyeal2dfS8g5M5tggfYdk6FRWott7-wOcrbhcBZ-RB3tyIy-ac5KvPGV9eKOfmrvX0IjUrclUMfElgt2lPjY859b3h5gsuvDDvX2tBWHMkNoEs1E9GsLzmbuH8K9-vAwDcQOR7V4g0qQX94HriUE4ot7VELdzs81vV0_aERIpckaNErcl_Va0s4CQleV2_5MIKlqA2Dk-ZMGdnETxfJKJVS9CiprdndX8TsEHCmgwM62tuRWuZbCSNJkUDQC-jWYW61iT7pHXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70115bf6a8.mp4?token=NgCjdnBDn7osCnkty4FislCdn6ciVTl8vwm9mqnimxvS1Vw1_FYiHoUQNJxDOCmTQvkLhQ0w924Anyeal2dfS8g5M5tggfYdk6FRWott7-wOcrbhcBZ-RB3tyIy-ac5KvPGV9eKOfmrvX0IjUrclUMfElgt2lPjY859b3h5gsuvDDvX2tBWHMkNoEs1E9GsLzmbuH8K9-vAwDcQOR7V4g0qQX94HriUE4ot7VELdzs81vV0_aERIpckaNErcl_Va0s4CQleV2_5MIKlqA2Dk-ZMGdnETxfJKJVS9CiprdndX8TsEHCmgwM62tuRWuZbCSNJkUDQC-jWYW61iT7pHXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تولد ترامپ
/
حرکات نمایشی موتوکراس در چمن جنوبی کاخ سفید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/127875" target="_blank">📅 16:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127873">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dFJ3ga77Nl0USlIYQ158zNtc9kpBBkXZ6pdYKaCrIEBxLynNuJlFEHn9Zq1-Culgqevg48FOMbXVDgEBLGIMayJ2kJ4_jAqtBZj1rYroemeY4meTeYxuVpaN21SgnhC-jHMOcSbEWeBvXYtHQB4kTN70kBuV2lRAbTK-CvHpxZM1I5Lss-RpECIAK4bY_zvzW0QEK_AW9fP-6EEyCOFU_9lTTAQJ0yr5YWsFIECIeoelWvhbC2NaP3s0h4Jn5vu4OoRzw3QEn1OgAHwbutgcAxSW7hAkqc-yWSp6bUwSMWj2x1e-iBCLJ-E2skI_yLF36GVUyj3VLj3KJrZhbwsTqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BUbOGN7Bq7tCVlz6k-oPgTjTrRdoEXB8q8jIsRcyn-qQzjiS76YguT6Amtg_F8CK8dvc1CCMqr66jFR6OiA-EFDElcQZLArkgDMVVqGWKw70YkKCzalS9laUwgkgUQW8lwPPuZEoEcq6S-G7zDUvrmCoYEL9dOIIQu80mc1_p_BpbeBQ-H7VtJTOQTo_HpEoAZx-dLX4oX8Nid5HkrcRbAI3eu9m96qFJeR4pW3JqDcz0_oe5boicyVk4Jwr9aKuEKYVj5xZPvF6S-XKjrk97cSJfmwNHKKVsDDdAvdeTJdnvxoehbdmWEjfBiugqq6hsLAexKt_KRMua2JTkFrPqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
نتانیاهو ابتدا تصویر حمله به بیروت را منتشر کرد و در پست بعد تولد ترامپ را تبریک گفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/127873" target="_blank">📅 16:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127872">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FvtxhqPTsLPZnlev7OkMRzG0ybqQMc1YNpan3D9WVV6kraQoL8qwSBC3Lo7U6YuP79wIgxs67rYae5WsCSuzAPYump8gYJJYtatN0asyOfMyP25krYhrdi5-8kvnlnQQHQG9_UgveXx3ZZGOXJhzCwXOx2Rbb_980qmnRNtRwPdEtCMDKlmULl16KcTITJYpnZeZe_AFS2nsRj8hxod6vSsApLL2MIADfuk2P7qjUF2dcnDNlY454rY3uqQf1xLm1K8Qu1Ufq5IKifO7cWp44j8YN95zPTlAVf58Ew0nCo-tAsbTC2bKUXl2pitZqi-US0Ur7dKC74sZ4dEYIopiiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات به لبنان ادامه داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/127872" target="_blank">📅 16:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127871">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
قرارگاه خاتم: پاسخ کوبنده میدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/127871" target="_blank">📅 16:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127870">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
تندروهای ایران
🤝
اسرائیل
هر دو مخالف توافق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/127870" target="_blank">📅 16:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127868">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfXLqFU5JptvVdK1EY8CC0WwNIMnkLH8tTdOSaRIl8VgBv9Zlaq_uOKLfi99owX0aS5-o6mA54uM9EDV5EX5c2buBuwEdE_6SHeY2RSEuyq6Vwtc_XRjx3W9jt8FALGiTp_R6hngLCtk3E-H68tKxVYtnHoNMiWRcFR0760i9ZrTeWXaLvoV0w7DHjF9Ppjesgfzadi62UeHA2oB7xb5Zqt79U8EbEQXyIdmY2fnY44JEDy2TFv9V0H7klo8tdWQ6yNkXsDd2dRF_FP_MeXdqmRSenBrMr7X38pJ2nP_Wyyw285aVE9eBORVvPUmuMcWUFSIsqOrJ0cy7w8jD0sFgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر عجیب منتشر شده از عراقچی در ایتا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/127868" target="_blank">📅 16:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127867">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WT2reubzUb4qNQG0P8GQAyD6oGuqno32AOHSc_VpGPW2T3zBzciYe8iHB1z8nIU3VRITDSet4BibK9yVhEsghw-t2m4hAjEWhcpkoWCiJYxuqO9KE9bNpBl3jP2f0-cbcqyfhsCJbvcid-XCjqOQPBqJiasqnqjrYTMoej7gm23NntA35GzcHQ1Fp1jd0OFUSzGGt9_SpEnVHya_7iP6lugVMZFg-zoHzPT3zBYr56jczOn-EQbB4Wdrymxq4XPZGnz6Z97xzjKy4X7idwm2No0mXWUv2dCXjg7VFIYZ8LIxVRohqgbGohR29LamXRXF18805u68ngbsW9z1p0x8oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف : تجاوز صهیونیست‌ها به ضاحیه دوباره ثابت کرد که آمریکا یا اراده‌ای برای اجرای تعهداتش نداره
-  یا توانش رو با چراغ سبز دادن به رژیم نمی‌شه امتیاز گرفت
- بازی پلیس بد و پلیس خوب هم دیگه قدیمی شده
- اگه نه اراده دارید نه توان اجرای تعهداتتون، حرف از ادامه مسیر بی‌معناست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/127867" target="_blank">📅 16:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127866">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5f0e8d393.mp4?token=JvTMQPvnXurjhlg8ttz8O9Ik8TswI51vF04-wRzG_SD94b5KlZyQU3RUxvkK3mraQGPo_IoI9ufGmPddexJS_uQ-8paw0cz6kaoBcDvu6ikhTAbXdk5e4LCkmHGayyv1Lxe-o3ezCnj_MJwiyzxXQrBQTcANg6c-mgtiX4q36-OOJ3Bq9sJsYWJOjgJcropdKSncJga7gVxg96Jd0l2jaLaGoQyR7F5uX5sCMF2Z5OAkhzDNuJC90G6qWN7W9bIgnqw-8qIfsOiZNgdOFoGtpG6LE5z0W_tdeBFlxmnZNv7zJsjlfX4QWSLwjRquNXgzYfZ50v8e2XhzsbnMTOiYpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5f0e8d393.mp4?token=JvTMQPvnXurjhlg8ttz8O9Ik8TswI51vF04-wRzG_SD94b5KlZyQU3RUxvkK3mraQGPo_IoI9ufGmPddexJS_uQ-8paw0cz6kaoBcDvu6ikhTAbXdk5e4LCkmHGayyv1Lxe-o3ezCnj_MJwiyzxXQrBQTcANg6c-mgtiX4q36-OOJ3Bq9sJsYWJOjgJcropdKSncJga7gVxg96Jd0l2jaLaGoQyR7F5uX5sCMF2Z5OAkhzDNuJC90G6qWN7W9bIgnqw-8qIfsOiZNgdOFoGtpG6LE5z0W_tdeBFlxmnZNv7zJsjlfX4QWSLwjRquNXgzYfZ50v8e2XhzsbnMTOiYpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این هواپیمای روس نیروی هوایی هند روز گذشته حین تلاش برای فرود در منطقه جورهات، سقوط کرده بود.
🔴
ارتش هند با انتشار یک بیانیه، اعلام کرد که در نتیجه این سقوط، پنج نفر از پرسنل نیروی هوایی هند جانشان را از دست دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/127866" target="_blank">📅 16:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127865">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
سه کشته و شش زخمی در تلفات اولیه حمله هوایی اسرائیل به ضاحیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/127865" target="_blank">📅 15:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127864">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
وزارت امور خارجه لبنان: ما به دلیل هدف قرار دادن یک خودروی ارتش و کشته شدن سربازان، از اسرائیل به شورای امنیت شکایت کرده‌ایم.
🔴
ما به دلیل پاشیدن آفت‌کش‌های گلیفوزات بر روی روستاهای مرزی جنوبی، شکایتی را به شورای امنیت ارائه کرده‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/127864" target="_blank">📅 15:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127863">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgPJb6iv4mx-jX4YJW73R5wrbLvg2MJmmB1tAU3sNRmMqIPmN9m0_mA0WsR4ZqekgDdvStX7FUZAStOvymLM-AiWd_nan_tISEdev7oy-J26o6gJoOH0gsG1iex23Td3RzMx-oxZ8LhadSmuwp2N9ejLLTv3ZPjOVW0ATU5xdzWlqWTxLqvaX0ADLXxMSQpU8WHsTjtc6loxaljhV05fNLJgFeNlPCNXdggKJAvDI5zs6l9YNHBED0cdKGHEdn-mJDIQR_XIMfqi-5toibGcRawghEyEwu2UkX5vm3il1x99UAVc6VBo-yIGBDOPob62claQfR3PzCC1wNiUQfxXEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار آکسیوس: مقامات اسرائیلی و آمریکایی می‌گویند ارتش اسرائیل اندکی پیش از حمله به بیروت، فرماندهی مرکزی آمریکا (سنتکام) را مطلع کرده بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/127863" target="_blank">📅 15:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127862">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
عراقچی: سرمایه اجتماعی و انسجام ملی، امروز یکی از مهم‌ترین مؤلفه‌های قدرت جمهوری اسلامی ایران در عرصه بین‌المللی است و طبیعتاً هرچه این پشتوانه مردمی تقویت شود، قدرت چانه‌زنی و تأثیرگذاری دیپلماسی کشور نیز افزایش خواهد یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/127862" target="_blank">📅 15:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127861">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
آی۲۴عبری: اسرائیل در حال حاضر از اظهارنظر درباره اینکه آیا هماهنگی یا اطلاع‌رسانی قبلی با واشنگتن قبل از آخرین حمله به بیروت وجود داشته است، خودداری می‌کند
🔴
به دنبال حمله قبلی در تاریخ ۷ ژوئن، موضع رسمی اسرائیل این بود: «ما در تماس مستمر با آنها هستیم و آنها با سیاست ما آشنا هستند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/127861" target="_blank">📅 15:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127860">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
عراقچی: امنیت منطقه نمی‌تواند بر پایه نادیده گرفتن ایران شکل بگیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/127860" target="_blank">📅 15:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127859">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
نتانیاهو: ما به اهداف حزب‌الله در حومه جنوبی بیروت حمله کردیم و حملات علیه خودمان را تحمل نخواهیم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/127859" target="_blank">📅 15:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127858">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkx6vxj6S1IMyu5bP7gC4Ur2SVCW2fdgOyzxZ19sirkcAObpnTur2C9PsM9ho6Z_wCicnqtDf9GhuCIFjuO_VyHbm5GzN-IJgQefca6pnr9uWaf7tNpBq-fNXvoWEBxONWYnZMarH1pzD3JtvUdJHWGyEvbavyhu1lCN_0j5xm5_ymH3THOmxQtFngCiQroWqda09wP-lVfQCyj2--oVp2roOqhN-F9koXIPFagjtzHlBmM9Dv221OlxMPWxuflzXRX6tMbWJLMPlcRCQC8hTyyh3IhffkVXE0HrdF_79gGhw66Gw1IPE5ekV00kHKk0IkmUSgUWx32tXHCrdGxgjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت اکانت اسرائیل به فارسی !!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/127858" target="_blank">📅 15:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127857">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
خبرگزاری رسمی اسرائیل: حمله به حومه جنوبی بیروت توسط دو هواپیمای جنگی انجام شد که چهار موشک هدایت‌شونده شلیک کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/127857" target="_blank">📅 15:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127856">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJJHs2c3aQ5Q_0ut3hVggpbbRrPIF3LWZUf0DX7YvwuLfQnSPnaI37sVBndE88JBJkKVMGVvvxj_CRUWe5Y2ktnjJ_VMb6er0gKBPHstrvLWjZU-aZbtR1scUecfYjMp414-ocZbMyAa9weXafLKeUSLvKJXTpM9CykVyeWYE9d-Pm2_p9E9HumqRTTJw-1FNEQm1lwd5p1cv8PCBpmvAZiYfrGRpRHzj3Cmf5Ivba7T1AunsNye2Tqbk_OMxRR0JSsZzZfcOVWN6l72qun2YOD601e1gUkT8ST169NVjG-8vtZKwzoL5r8azkdebvQYHIRpFD39PJgE7o9W3TpdHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/ سخنگوی کمیسیون امنیت ملی:
نباید اشتباه محاسباتی کنیم
🔴
حتی اگر بخواهیم به توافق یا تفاهم برسیم، راه آن انضباط دادن به رژیم صهیونیستی است. اگر این سگ هار کنترل نشود، امضای تفاهم خشک نخواهد شد و پای ما را خواهد گاز گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/127856" target="_blank">📅 15:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127855">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
خبرنگار صداوسیما: تنگه هرمز طبق اعلام نهاد مدیریت آب‌راه خلیج فارس تا اطلاع بعدی همچنان مسدود است و هیچ کشتی خارجی حق ورود و خروج ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/127855" target="_blank">📅 15:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127854">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEEvyTxIC7TnbRjmMTD2XHGu11EG_RSYkXJ_iam3v2dvrf2zMHCoTOVFRUZSep4Q9aGfG8T5NfOoobcqHjbyglt6PDt_y-7Msu9iMtm7IC01cmQQSpo75jSM99MTlhoW4t1EUJXTZjJ4wg6cEZwSXTJofCWJwoUY6XmNDRdvSCM_wBqdDeLK1rzb6z2CUTA400TqvTPaJcpj6a2WFkL-NJDbqIQUE_QTtdvmx9eSzrIzred_h7xwKjX5eg5QNR1knnzYm3DPb0aZkt6XDUY2IKYDVecWjC8o-j34fBvcaKVXFcn35IElzqUdF_pdR0dDXLQk1I4QTlC3PcHFC33Jew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باراک راوید(اکسیوس) : ایران همونطور که گفته بود، حمله به بیروت رو پاسخ میده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/127854" target="_blank">📅 15:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127853">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
خبرگزاری العربیه: قطری ها و پاکستانی ها فشار زیادی می‌آورند تا تشدید تنش رخ ندهد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/127853" target="_blank">📅 15:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127852">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
فوری/ منابع عبری: ارزیابی‌های کنونی در اسرائیل نشان می‌دهد که ایران تعادل را حفظ کرده و به حمله در حومه جنوبی بیروت پاسخ خواهد داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/127852" target="_blank">📅 14:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127851">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
سخنگوی آتش نشانی تهران: دود مشاهده در قسمت شمالی شهر تهران، مربوط به حریق فضای سبز در محدوده ولنجک است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/127851" target="_blank">📅 14:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127850">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: هدف حمله هوایی در ضاحیه جنوبی، فرمانده ارشد در سیستم ارتباطات حزب‌الله بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/127850" target="_blank">📅 14:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127849">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZttEf0SLnPGnhFCW9TVANIMLxtGijrtjsUHCgxiESkXzH0re8Nl8OpM5X7EqyGAvRfBWTG1iqc4TwdHKjQpsv4kigwicfiYw3wP_luvLckDmh1cFF9Q30cYEQ_hyU3Ba9tpfj8dFsxegokoWOhMx_GNLlUkz1J-b3_dmNlRo9_BmlpoGUfjByNJxCPfMjE8XszKDhxRwucxYVK1BcDbvQ4Xumw-UlhSmrZAP8CqG8xKXHySy2sVXgBeUGsZLx7d1yVZRpU1aYh7JLi14l9sJawSNzi_2yyIWFB_auvjhGtDhsEkvoSyQgPdkwjLPsFGmQGJEUsSxhX4me2patMheBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل: مرکز فرماندهی حزب‌الله تو ضاحیه بیروت رو زدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/127849" target="_blank">📅 14:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127848">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
بیانیه نتانیاهو و کاتس: ارتش اسرائیل اهدافی متعلق به حزب‌الله در ضاحیه جنوبی را هدف حمله قرار داد
🔴
زیرساخت‌های حزب‌الله در ضاحیه جنوبی را با دقت هدف قرار دادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/127848" target="_blank">📅 14:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127847">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
رسانه های اسرائیلی از اماده باش کامل ارتش اسرائیل برای حمله احتمالی ایران خبر می‌دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/127847" target="_blank">📅 14:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127846">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
شبکه ۱۴ اسرائیل : ما جشن تولد ترامپ رو امروز تو بیروت جشن گرفتیم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/127846" target="_blank">📅 14:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127845">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
فوری / کانال 12 اسرائیل به نقل از یک مقام امنیتی: این بار، ما حتی پرتاب یک موشک از ایران به خاک اسرائیل را تحمل نخواهیم کرد.
🔴
اگر چنین اتفاقی بیفتد، اسرائیل آماده است تا یک حمله نظامی گسترده و خردکننده علیه زیرساخت‌های نظامی و اقتصادی ایران انجام دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/127845" target="_blank">📅 14:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127844">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69e99d5be0.mp4?token=JxEQDYqsuh5BO59-pYsSf3g84aeYvYl5Rm1MIgdBR8cSY8wezAVXMc8LEQW4h0FXnp3SuU_1mainSe1BCR8j7OGvSODaGYZPxVUEWKVuypyL5iNYMPEm0QEy2fgqv8UCVg8xFRkx6Vm6ua6N7-X5to3TKnV3u6M_7MDv0mZXk2GU64ZIiKoThZqIsDqf8n6uFtR0odjR_kiiSmoHTC16oVno-BGyZCSrQoch5fq1KJl8UB31t80q9b89C12RuB6rd4JemgL9Mpy9ZxAApy_aGT1SRY6pvveiq-oCpc0fdGULU5E5GF_UtDW_4uuUpQ_Ug-tTPZXxDpsdGDWhB77e2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69e99d5be0.mp4?token=JxEQDYqsuh5BO59-pYsSf3g84aeYvYl5Rm1MIgdBR8cSY8wezAVXMc8LEQW4h0FXnp3SuU_1mainSe1BCR8j7OGvSODaGYZPxVUEWKVuypyL5iNYMPEm0QEy2fgqv8UCVg8xFRkx6Vm6ua6N7-X5to3TKnV3u6M_7MDv0mZXk2GU64ZIiKoThZqIsDqf8n6uFtR0odjR_kiiSmoHTC16oVno-BGyZCSrQoch5fq1KJl8UB31t80q9b89C12RuB6rd4JemgL9Mpy9ZxAApy_aGT1SRY6pvveiq-oCpc0fdGULU5E5GF_UtDW_4uuUpQ_Ug-tTPZXxDpsdGDWhB77e2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل ویدیو‌یی از حمله‌ِ به ضاحیه بیروت منتشر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/127844" target="_blank">📅 14:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127843">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DfwHjQ4ham49PN1WI7B1mrtADPXN2ZxpoI7nZUGVHoaHXFO9LGSy0PnuORYLSb5vQhUtVFq4ZLL2TNRFWkFbp8uJIfV7AMJL7tPNS2mYXSTg30-mfDRBnKUGdKOTeDgHjH7CXkt2cs-Kndf0YP5cDylpjQxUGZ_yGM8qxJmR9hYdQOUAlDQKFH_UbfDAcM86QT-zRjt60p9nvk6hZd1JeTkns5C1DyEaXDbz2E9akNXKFJY3OuNCaVoZLQpNDT4cDs51vSJ2iXpw2LjnnjqivOXbWVAAHZLPidLqfpULnEawY7WKMhyPa8FEZC11CBlLtdXpIRBVFyQzZWTY336r0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خسارات وارده به ضاحیه بعد از حمله اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/127843" target="_blank">📅 14:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127842">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
فوری / کانال ۱۲ اسرائیل: هدف در حمله به ضاحیه جنوبی نعیم قاسم بوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/127842" target="_blank">📅 14:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127841">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
فوری / کانال ۱۲ عبری: اهمیت این حمله در لبنان این است که ایران قبلاً تهدید کرده بود به هر حمله اسرائیل به بیروت پاسخ خواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/127841" target="_blank">📅 14:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127840">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AxLHknUjBGqF00QSooK4s4CEHIU9q8_5aDvLAgxfhksUb0ODcENroYGihzHjXFXinFY6P37eRj81S3by4mvUKFI7V7tgJaOXkqkDjNlVZv9p6FqVA6uh8gP_XMeH5NEyH0dJ0ZdkyUb7f2921ujbFZyhYrHScumNd4F69IfI_Lk3hc71Q5yD8DUdpVLGssJ2iiG4tc4ePZgKPFrp8Q3MnI8L5PsloeXMmkOSr6T_dHBlk8vGDa4Nhgz2-KgsWhf4MhAcLkPOVuUeYw8rLdAGoAJueW_N3FuMtkC927-BLBB0z-j8TQWxLtwGeIBGLmwKa51f3KNkx14CaoJkidk00A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ضاحیه بیروت هم اکنون
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/127840" target="_blank">📅 14:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127839">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab3645c40.mp4?token=HEBX0vpeNbzfIrfV86yh0lPYTKWg6cOpB5Wnm2ywiYb8VSZQuuMytUpODDRgiFNfY3aHHKRZyXD1SBCW9GlsVs_arUCzAazov-jx_Y4qzmd3lT1sOVWqVtbYWu_kG2yqOjM3vu8kJfwddGru4HWHn3j8CFEskfle7sBFC4KclktvJV3UbEsXOBpNLEGh9b4tOhX9pmofVxPiyaZKVMEGWefesV_LBCGVTg8q2rT7CFfybqJNsMct2KmJQWgMftSqcxSUajqCy37q8kyRmzDKxMkJ-Xbt0GFSuG5WQE5tpcY0M9j9fQzkRfAjiyACDuP3N5ZgwIAAxlXNh2kqv8Y-nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab3645c40.mp4?token=HEBX0vpeNbzfIrfV86yh0lPYTKWg6cOpB5Wnm2ywiYb8VSZQuuMytUpODDRgiFNfY3aHHKRZyXD1SBCW9GlsVs_arUCzAazov-jx_Y4qzmd3lT1sOVWqVtbYWu_kG2yqOjM3vu8kJfwddGru4HWHn3j8CFEskfle7sBFC4KclktvJV3UbEsXOBpNLEGh9b4tOhX9pmofVxPiyaZKVMEGWefesV_LBCGVTg8q2rT7CFfybqJNsMct2KmJQWgMftSqcxSUajqCy37q8kyRmzDKxMkJ-Xbt0GFSuG5WQE5tpcY0M9j9fQzkRfAjiyACDuP3N5ZgwIAAxlXNh2kqv8Y-nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلمی از محل حمله اسرائیل به ضاحیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/127839" target="_blank">📅 14:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127838">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
فوووری/رادیو اسرائیل از آغاز حمله موشکی به بیروت خبر داد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/127838" target="_blank">📅 14:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127837">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rPc2Bi7PvS0g_sHFVLUiqat3bRzRhhlzPaaZDMVBPSWj4fniZsNCDqVVsAmUZ57KTxxD59llomoA0wDTqaIiwFVdUyHkOBJK4CXPtsa7y_mR7KF0ORuwu7CuVqEjBcYG1ydqQQkrQkPne0VLpFg2AjvGSmtte-ellepAmIFlPnQSpCmeS1HA_m31SBX0-hANYPdAp0g-R4xzkCdFS4U7ghwNW0mQebrMO-CErYQufKKMWvsas-1OmNRdgxEas-qUzo6JgFWYknjPI0fDJy7Jk_s3PhmX0ipz7PWofu5X_fuFnTyowcBw2ZNfgRdAZNsF72SDOEITlvEQDtxePZB9FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوووری/رادیو اسرائیل از آغاز حمله موشکی به بیروت خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/127837" target="_blank">📅 14:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127836">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=QoXfuOlm843mOz0dohbjh0TFQDet_jiYs--1XTeOXXDQUcttXQVOirfhETQBdd4g5QOR1Bu409yhMxB0lBRhaKWBUAxmlMuP4Zr3umSmSQ5XFLtoxg0MK_2d8tvBPeCy-3uFc5FyPPY1At7nhbTdARPdcuWsRik1TS0JvLpa_JBNK4dGjnaBMSjqURil-0wNPRjy7by6-DOCADQ3ModYen1qq35o-VDMGS9-B9IKxH1BuqDamyHFBzqONSodHq8ADtOTw_I4Q99OECWDblrTIY-b0fmk-37NFxrXZ55ISnNtMXvaJeKOWHvSgrh9DAIY9pbdhJLPj9dM1GERzLmeqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=QoXfuOlm843mOz0dohbjh0TFQDet_jiYs--1XTeOXXDQUcttXQVOirfhETQBdd4g5QOR1Bu409yhMxB0lBRhaKWBUAxmlMuP4Zr3umSmSQ5XFLtoxg0MK_2d8tvBPeCy-3uFc5FyPPY1At7nhbTdARPdcuWsRik1TS0JvLpa_JBNK4dGjnaBMSjqURil-0wNPRjy7by6-DOCADQ3ModYen1qq35o-VDMGS9-B9IKxH1BuqDamyHFBzqONSodHq8ADtOTw_I4Q99OECWDblrTIY-b0fmk-37NFxrXZ55ISnNtMXvaJeKOWHvSgrh9DAIY9pbdhJLPj9dM1GERzLmeqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان تو مراسم امین ایران : رسول خدا و اصحابش، تو جنگ رفتن لت و پار شدن و شهید شدن و برگشتن
😐
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/127836" target="_blank">📅 13:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127835">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
مقام ارشد ایرانی : طبق پیش‌نویس توافق، آمریکا قراره حدود ۲۵ میلیارد دلار از دارایی‌های بلوکه‌شده ایران رو آزاد کنه؛
🔴
از جمله انتقال مستقیم پول و همکاری در سطح منطقه‌ای
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/127835" target="_blank">📅 13:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127834">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
العربی الجدید : ایران هنوز تأیید نهایی خود را برای یادداشت تفاهم اعلام نکرده است.
🔴
به گفته یک منبع آگاه ایرانی، احتمال امضای توافق در روز یکشنبه منتفی است و بررسی‌ها در داخل ایران ادامه دارد؛ هرچند ممکن است تهران امروز نظر نهایی خود را اعلام کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/127834" target="_blank">📅 13:46 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
