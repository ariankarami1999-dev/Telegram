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
<img src="https://cdn4.telesco.pe/file/WdwJDQpNa2na9MkaJY_OqkXkM_ayQOd24J0OjA5xB55kpr-MhT0aKK3VqlHcOCY-UIf2ow5-OD_5a7iCeQZrEsdUvl6veTTf1IC9lRwAfG_ln1UlU_SipQmT745QV0aJSxpj6gDNBtnNXiSPG8Lx4qTiJR8HujMyT_A1bQ4fNvcM_WITAkttvS1fP30jAWu9ZxE2xjTU5r46kh0Orub7xeaj-kO2DjRrZCZc5MHgPpMS5queKJrq1x3W6Y2h87wwlZtnCq_YR9PpoEOYXGLmWeMD25EK6iDc-2RzHa79QPR60jm_75fUzRKCSDq9KlruMLiU8EZgOsZzZc_swY-_3A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-01 16:38:53</div>
<hr>

<div class="tg-post" id="msg-444042">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVHYnrWvmhpJqa53zIZT-5OIOSJsuKVnjDn6K5AWKeXs75OCM1Hs3qRBuHCKgroZBcoZ9Wfq2NnD5qEf4FVTF78yjM1_ZLpv0bRrtAZC1bxGbVXaXHK8SeN2S6KnQZKNg2pKjp78OZPmqPhSkkpIZKfNoyxCOcItgvswsqc_QfqQdTI7jetwSoF0onQLjcRL6HvldhEKn0ZYG9zHmKvducMLVW0X5V2K0qC9M72vGbKvOYy6dfckwusNBU7z33bjpjr47E3TSMeulEL0QbkCP0DOFiUGy7rwnXunboWlPHI_HYKxO5gV8GsUunANsNv2Lhgfto74aA9OFL7DLPmEiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسیب هر وعده قلیان برابر با ۲۰ سیگار است
🔹
محسن فرخ‌پور، متخصص ریه: هر یک وعده کشیدن قلیان، از نظر میزان آسیب، با مصرف یک پاکت کامل سیگار برابری می‌کند.
🔹
هنگام کشیدن قلیان، فرد حجم بسیار زیادی از دود را در یک بازه زمانی بسیار کوتاه (حدود ۲ ساعت) وارد ریه‌های خود می‌کند.
🔹
این حجم بالای دود در مدت زمان کم، می‌تواند آسیب‌های بسیار خاص و شدیدی را به بافت‌های ریه وارد کند که با مصرف تدریجی سیگار متفاوت است.
🔹
اگر فردی تصور کند با محدود کردن مصرف به هفته‌ای یک بار، خطر را کاهش داده است، در واقع در حال وارد کردن فشار شدیدی به سیستم تنفسی خود در همان مدت کوتاه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 38 · <a href="https://t.me/farsna/444042" target="_blank">📅 16:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444041">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c1d5f7f33.mp4?token=W54OEBggCZpD4mOt-3ajpU502iEtlPDb5ScwHWHY-MEImIwiGntK3I7Q2JyplhOiQ02bIrCrjD4Nx4xmNK0jxHdxB7M6sue4dwqzI1V6bfx1vnLxvse15ZkUtp2oTm0AoUe11gtG64tPCWvrjMM3wQpFWzDNv9uvhSsC1cnu5jyEkZWOmh_MYA40ysfma9gBIerh3885aa42h-Lol4uEfBDcETXgJRT21611BIeOrdBlhT7V4KfhVoHv2yI05adYDt-FqXkSGNlowzrvURY9yKIMdLtcMZLmxkRHC3umU4tC3lQV6XZtZE3UVcP94s_LmYOzm3Dg5s3SGmuYKMmI-bfteq9gwJbQXULpeUwj7vXBtRyebDGGYOd4sX1Blujx7ZCkvyKyxmfNriFNZMQPX5vLOMQQ2mqySO2wCUhuscvP5i4MIc5hgPUlVq7in1uAtatPTlcllCxjKqvhC-U9U_mp3IAEZz5jxar61boNDpqk3CStNVlPuAE76hYdj2OVs_KIY-4ddqVIJv54mHZawjFbiKU3i2kES2AGZD-_3rlywB-mjlUKaH6E7MR6NbLCnNiMi6ZEJwjLtBNUThyRBqr83SuLt89kI0dPTQdpvd9WecoiSVARESU2f1gYKfsYryqj9oHENO_t5mnF0y6367gLFN8KnTyQI0s9tQPzbMY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c1d5f7f33.mp4?token=W54OEBggCZpD4mOt-3ajpU502iEtlPDb5ScwHWHY-MEImIwiGntK3I7Q2JyplhOiQ02bIrCrjD4Nx4xmNK0jxHdxB7M6sue4dwqzI1V6bfx1vnLxvse15ZkUtp2oTm0AoUe11gtG64tPCWvrjMM3wQpFWzDNv9uvhSsC1cnu5jyEkZWOmh_MYA40ysfma9gBIerh3885aa42h-Lol4uEfBDcETXgJRT21611BIeOrdBlhT7V4KfhVoHv2yI05adYDt-FqXkSGNlowzrvURY9yKIMdLtcMZLmxkRHC3umU4tC3lQV6XZtZE3UVcP94s_LmYOzm3Dg5s3SGmuYKMmI-bfteq9gwJbQXULpeUwj7vXBtRyebDGGYOd4sX1Blujx7ZCkvyKyxmfNriFNZMQPX5vLOMQQ2mqySO2wCUhuscvP5i4MIc5hgPUlVq7in1uAtatPTlcllCxjKqvhC-U9U_mp3IAEZz5jxar61boNDpqk3CStNVlPuAE76hYdj2OVs_KIY-4ddqVIJv54mHZawjFbiKU3i2kES2AGZD-_3rlywB-mjlUKaH6E7MR6NbLCnNiMi6ZEJwjLtBNUThyRBqr83SuLt89kI0dPTQdpvd9WecoiSVARESU2f1gYKfsYryqj9oHENO_t5mnF0y6367gLFN8KnTyQI0s9tQPzbMY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری سنگ‌زنی مردم سبزوار در حرم امام رضا(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/farsna/444041" target="_blank">📅 16:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444040">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGV5nC-lnkXT-FQM2HgINvET1YTcyfGR8rIKzZFNmNgzEBEcRsHjySRODgGW_Zi4bMtSuNocAgBWfaJFJRdn3kISSruO2uspUrZj6VIIrmrbMrp-VAbCtb5BttCl_ZhMMxTUR27HuwNa1A3_jy-3-cxOIgv9yNxfIS0XX6JGr9Sg3o5b2pd1fK_hZpSJYD0h2rlSbhhDGpxfTcCkMGXCYbnlfPIufuh82hG1NF8mnQNOz83WbS6YDcGH0CXiYn_jw4yIEXCctUYaIFKRHO0MwdtPvDVUwShi2nOId3oBrXk_ra7has24T-8VV0ZVswLYT_CZHvpMpwhgwpnMurHV2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
تأكید مدیر عامل بانك صنعت و معدن بر حمایت از تولید و بازگشت ظرفیت‌های صنعتی به چرخه اقتصاد
دکتر محمود شایان، مدیرعامل بانک صنعت و معدن، در حاشیه بازدید از نمایشگاه ایران اگروفود:
▫️
در دوران جنگ، خطوط اعتباری ویژه برای صنایع غذایی و دارویی اختصاص یافت.
▫️
هدف، تداوم تولید و تأمین کالاهای اساسی بود.
▫️
حمایت از سایر واحدهای صنعتی نیز ادامه داشت.
▫️
بانک از بازسازی واحدهای آسیب‌دیده حمایت می‌کند.
▫️
بازگشت ظرفیت‌های تولیدی به چرخه اقتصاد در اولویت است.
▫️
توسعه صنعتی با استفاده از ابزارهای نوین تأمین مالی دنبال می‌شود.</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/farsna/444040" target="_blank">📅 16:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444039">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMV6MXKUBUyan_7zOtyhLAb2Av0VsBAIJbZh-UkGyL9NZ2TuMdOr48X92KyGayk_N2-Hhp3VR-Zu0DJlEMzOZ7II01m8wUaF3I8_1YkPS_jyXP9qBtXbrBU6xVhfFTQmq7APEk1fftIyTJs4wwfyHS3F2erh-O2crT8aZH_aQyClpfbq1YGAAiWRCaWFrOKhUANMZako8LUoiyTCRqQgZxJovPmuoMe3dXKbbKDE2e0dw4Hbm8zLYDcS27FWNkGTlnWUErew4CkxExiNjw4vXpwM-WahpJppIT-SapuVFCM-P2Oo8CUsSY4NnNHKS6xbM7_IxbwtcWcPjbTnDFzXmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به مسابقه جام جهانی دعوت شدید!
جام دی همزمان با جام جهانی
با جوایز جذاب و متنوع
⏰
هر شب از طریق شبکه ورزش و
ویژه برنامه ۲۰۲۶، همراه بیمه دی باشید.
پیش‌بینی هر دیدار،
جایزه داره تو دی‌دار
ورود به بازی
daycup.dayins.com
#کانال
اطلاع رسانی شرکت بیمه دی
@dayins24
#دریافت
نظرات
@prday24</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/farsna/444039" target="_blank">📅 16:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444038">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/farsna/444038" target="_blank">📅 16:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444037">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8j7em-SENrZghaavR9jL3GBpG01HR4vavKEbyy6gqLct_y-8RmSxwz2J_KQJkh9MYQN8O0ayPjn3MleheCtNena0M9XXgGbyb3XQ9LGYJc0fetepsIiK-NXNwNEhBE5yXy0WenH61Ys0MUAao_-W9p48zkFv3bJfK-3NLoSanVI1KwEzmtpNsdGgyVFhyOgKXQb9eq6AEtBZYsOl5HXtBsk-DLNDOJHq60_3hjvnM5bMknSbFODBa0ecXpMtWmbmjEcVQb_ETzY59X9AASL-OFsyHMeKaub0STZOOU0PEDI0FP9ATMeGOBoYlq6H4cswmD6WBNpjoFylCQCdc9Frg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طوفان در راه تهران
🔹
سازمان مدیریت بحران: مناطق نیمهٔ جنوبی، غربی، مرکزی و ارتفاعات تهران در معرض وزش بادهای شدید و گاهی بسیار شدید قرار دارند و احتمال وقوع طوفان در این مناطق از اواخر امروز تا روز پنجشنبه بسیار زیاد است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/farsna/444037" target="_blank">📅 16:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444036">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h2baQfab8D1M4RoQofbQiO_DPrZcsgDWsDT8Z6-b_M8jyMCFUjhjlfZ1IgJMXiEA-6Ruy8Fc1R3DJs1QzV8BNogN1XUpmoZ3dImMc6e2H5iSax_QKyWTQwfiwc9HWDPwALoje6_qqm4r6AZxgUo7jYO6Ge2ODuwsmzN9em3N8Sx_4HNmZWrYq0P143PrLnwdkY1EetD9BsrZ6yyM_cmIq-PBksafZgFcKElscOIB7HOE5JwBQlvoT_2Cm0mStTd71S-GtmYf3rvj3nApNHr3l_ss_artrKW8jtPPcCBJj3FCIOmE2e9kXdGrNUjn0IYSnZSvkQbmBEpme6c3orEhgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۱۴ تُن سنگ طلا در ۶ کارگاه غیرمجاز تبریز
🔹
دادستان ورزقان: درپی بازرسی از ۶ کارگاه غیرمجاز فرآوری طلا، ۱۴ تُن سنگ طلا کشف و ۵ نفر دستگیر شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/farsna/444036" target="_blank">📅 16:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444035">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7acd6299aa.mp4?token=JaPVKUUeJMgzf_GOKORIApMq-PFJeQCSzjGWbRRw-oQ7TI00tSESaaWXL-M5gGGO7fAvEaKUFEsJTW_-CtcbG6TKbmirCdXUaPb-VeYkrW4rdEtXpkD_k9hrd7pZrL3aRVFit1YARNo_OXobZh0Na3zcAirjPx4FNeeDp54wJGvrYkX3XomQY1D9M_OUihRsCGYEfe_tDTpfXRaP5qKNFXBlLdGRNqhAzu8gbMoSJXTVFqMG-Gi0wnW6SohdnsTw3CQTemvnBD-hpUoMIq2vpg5eaGSNG3GzIwdkcSQfdtOfbk-Xw0ARXNhM3fqAR2BlDIP7-_D3ysSC2e0iui39uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7acd6299aa.mp4?token=JaPVKUUeJMgzf_GOKORIApMq-PFJeQCSzjGWbRRw-oQ7TI00tSESaaWXL-M5gGGO7fAvEaKUFEsJTW_-CtcbG6TKbmirCdXUaPb-VeYkrW4rdEtXpkD_k9hrd7pZrL3aRVFit1YARNo_OXobZh0Na3zcAirjPx4FNeeDp54wJGvrYkX3XomQY1D9M_OUihRsCGYEfe_tDTpfXRaP5qKNFXBlLdGRNqhAzu8gbMoSJXTVFqMG-Gi0wnW6SohdnsTw3CQTemvnBD-hpUoMIq2vpg5eaGSNG3GzIwdkcSQfdtOfbk-Xw0ARXNhM3fqAR2BlDIP7-_D3ysSC2e0iui39uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظات آخر در ناو دنا دقیقا چه گذشت؟
@Farsna</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/farsna/444035" target="_blank">📅 15:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444034">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrObUXDgDaSCdA2FDtSwC1rlTRwt-3vtTYm1NC-m_a0hn7wLAxRS9f9pqsjpT1USCJLgIUObebO-vW_5pjaevGcBCGG6MEyefxZZymaumjTkxyHj1sPLYSVV2fnBAGpnbzOJ_lba6mgGO24kk1CZapx1g9QCi6nPOm1vPuazjISlbpScsGX4XzI5BxOfj7Npc4ZzSsUHLHrO0OtB-USfwAgB4h0wpUuMzZJqCTVnv4Y07FIzf4MyKP0Sluk55LyWi0TR-ZZqjyMxynmqR3mKDGOT-sxASbVwmzuOzu2f1jhTIsLQ4GlsRAh0xqfvkgSpp92iAd0S0SLVLhOLm8VwGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده قرارگاه پدافند هوایی خاتم‌الانبیا: نیروهای مسلح در آمادگی کامل قرار دارند و ما برای هر سناریوی دشمن آماده‌ایم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/444034" target="_blank">📅 15:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444033">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سروش‌پلاس‌ هم اختلال پیدا کرد
🔹
بعد از ایتا، پیام‌رسان سروش‌پلاس هم به‌صورت موقت با اختلال و قطعی مواجه شده است.
🔹
علت اختلال، قطع برق در یکی از دیتاسنترهای شرکت زیرساخت اعلام شده است. @Farsna</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/farsna/444033" target="_blank">📅 15:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444032">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2-TYCaXlOo-SXVozpuDSzdmMcaU4iU_Bz7i0AoG07BDLhuwEi6zE4FEMtM2Wwb4ss09iZHuB1VFAm28kNUTvdWl2F-Z9_V94jZMkshKbfYjKTXnfyACFktgZA-RauW36H8ZdKoexKRMUO0Wlgk-Cpfn2A7lB-mTWn9PPT82pJX3MwJD9Bepw6NlVqF8TmkZoQHApt4CdgOM93EShFyLKwP_kXScI0dPIX67JEcanhTl-D0zjyFvj7PLJMxjVnnXhAd1Og70CABhqjR_Dix57tHE3O22FM2cdpBEiiaJhiu_J1aQuYlm3MiKwGFbjUAqLeQ4rRRRGW-IefAc2huh0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طعنه اوسمار به پرسپولیس
📲
خدا همیشه خوب است. متعهد بودن، حرفه‌ای بودن، با دیگران مهربان بودن و قابل اعتماد بودن یک انتخاب نیست، اصول شخصیت انسان است.
@Sportfars</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/farsna/444032" target="_blank">📅 15:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444031">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">رئیس شورای‌شهر تهران: تصمیم داریم رایگان‌بودن بلیت مترو و اتوبوس تا بعد از تشییع رهبر شهید ادامه داشته باشد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/farsna/444031" target="_blank">📅 15:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444030">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8a1ddb47b.mp4?token=epmFwA3_olA8nCaSegE_ZX4xgb1vHYqQM16pkPbZEj-6nCmE89fVd3AGXEDq_WJ5e7xEqUDCbOPqi-HFKmaMJde61XCsrxDvJeLBvfPuSkUh3a_BYK5BybwthFPSnBEvfsHhtdg8WHgfN7dDkyEbcouPHeDL06vNoGD-aFoHDJHRe9nWbKvThT3S23WwzUWvlVp1c6aNjqz-oEH5e43VNJotyuTyN8ny7l77nY0C0ar3wzWO2qUZOTMJSvW21DABRxCFRtnLje5tKHnqsOTApHVHsZfx4NBvVZczwTCnH1lG0lHMBLxt0XCR6MzoLswuGl3SK3HjZJA7exT18lvQQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8a1ddb47b.mp4?token=epmFwA3_olA8nCaSegE_ZX4xgb1vHYqQM16pkPbZEj-6nCmE89fVd3AGXEDq_WJ5e7xEqUDCbOPqi-HFKmaMJde61XCsrxDvJeLBvfPuSkUh3a_BYK5BybwthFPSnBEvfsHhtdg8WHgfN7dDkyEbcouPHeDL06vNoGD-aFoHDJHRe9nWbKvThT3S23WwzUWvlVp1c6aNjqz-oEH5e43VNJotyuTyN8ny7l77nY0C0ar3wzWO2qUZOTMJSvW21DABRxCFRtnLje5tKHnqsOTApHVHsZfx4NBvVZczwTCnH1lG0lHMBLxt0XCR6MzoLswuGl3SK3HjZJA7exT18lvQQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون ترامپ: معتقدم می‌توانیم به نقطه‌ای برسیم که هم تمامیت ارضی لبنان و هم امنیت اسرائیل حفظ شود.  @Farsna</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/farsna/444030" target="_blank">📅 15:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444028">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e821a5697.mp4?token=JmhPigX10j4jz2zdWe2nw5BT4t5goxWTz3GnJxRnPsj4opF426ioMv30jJZuRjoafYZ1jHIlaONj1WnAgkSBtd5oBSJcRcAh6MjQInu_DITMYaBn8vtg4bsIfzKwzIVuYSjtTnWjEZCn1RqjifC-3KH4UY_h-hnoOCllX1XtTcbZVPNrKSAu3F7mpVjE4VpmB3UPcrgVKucJmdnr-G522CkDYb5UcuVmIX6tFITAylJdPkA1Gv17LepmqypMOVg7U-QHxAuni_A7WZgkfofpcmFSn0114m4NXt_1AcjtKmkNTwVRpKS4uuufy2SMX8QdN26-_nCNfAkfwkT6sjmNYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e821a5697.mp4?token=JmhPigX10j4jz2zdWe2nw5BT4t5goxWTz3GnJxRnPsj4opF426ioMv30jJZuRjoafYZ1jHIlaONj1WnAgkSBtd5oBSJcRcAh6MjQInu_DITMYaBn8vtg4bsIfzKwzIVuYSjtTnWjEZCn1RqjifC-3KH4UY_h-hnoOCllX1XtTcbZVPNrKSAu3F7mpVjE4VpmB3UPcrgVKucJmdnr-G522CkDYb5UcuVmIX6tFITAylJdPkA1Gv17LepmqypMOVg7U-QHxAuni_A7WZgkfofpcmFSn0114m4NXt_1AcjtKmkNTwVRpKS4uuufy2SMX8QdN26-_nCNfAkfwkT6sjmNYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون ترامپ: دیروز به ایرانی‌ها گفتیم وقتی شما کُری‌خوانی می‌کنید، نباید انتظار داشته باشید که ترامپ به آن پاسخ ندهد
🔹
وقتی حرف‌هایی می‌زنید که واقعیت ندارد، رئیس‌جمهور به آن واکنش نشان خواهد داد، من به آن واکنش نشان خواهم داد و آمریکایی‌ها هم به آن واکنش…</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/farsna/444028" target="_blank">📅 15:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444027">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eebec29282.mp4?token=VATBYskqsiz1CER8avpIXvH4SzVyfQHZ3XIURsgO_MDcWEVpdYqWyge-7T4NclTGEOSA2HB_GQ87phUL4Yj9K5L9f_LPsDD_EiQxr81lf2CTk0L4j3FXWSDDfYD4sxMAO0SQf1-WzkwdiPTpvl8pdByEiuCSlc_5vzidsVwjgYG5sdZ5rPsg7-SCGVBqFwUXVIlCrf1nnUUjWZDp13woZhzGshir09YbeD1Oi9MgaoZg3aZkQcgf3Vko2g_wcxWsb6fxcTroBKrYhBTyNkjoiBmvw612kpAVoir1K_vnKzBkeE23Owlk8tY-J1BGcPrnMJvjSGTU8O-3peCpwpMXmqV6xxHX1CvHZGDSbShzFfzqXdmcFEvXT65ukh7RU773NO-tqmY_SMnlCS3NBo3Oeu_gDyzCfVxMgARGxspgLFo2Vrdn3ONY7phcEzvMYmdIHEQysm3lypvcOlDs5LnMi6lLIMCdd144a1nU534Hoy4ksBOEG3u3zm3htidSLMjfvplxs8jXO8KeePR7vEYhugV-NVtCUW8DX3g_rkAqYkuwbgw8jH6a1iF4OGMrD73a9DZrNB7bshWOb1yxmuRt18-HNGO5Qx4iZaT5zN237yE4cvWxe9s01a-VB3j7HihNQtYVoRa4eqdJYMPFWPqlsEOV3GL2u6E41xXYmtZghQo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eebec29282.mp4?token=VATBYskqsiz1CER8avpIXvH4SzVyfQHZ3XIURsgO_MDcWEVpdYqWyge-7T4NclTGEOSA2HB_GQ87phUL4Yj9K5L9f_LPsDD_EiQxr81lf2CTk0L4j3FXWSDDfYD4sxMAO0SQf1-WzkwdiPTpvl8pdByEiuCSlc_5vzidsVwjgYG5sdZ5rPsg7-SCGVBqFwUXVIlCrf1nnUUjWZDp13woZhzGshir09YbeD1Oi9MgaoZg3aZkQcgf3Vko2g_wcxWsb6fxcTroBKrYhBTyNkjoiBmvw612kpAVoir1K_vnKzBkeE23Owlk8tY-J1BGcPrnMJvjSGTU8O-3peCpwpMXmqV6xxHX1CvHZGDSbShzFfzqXdmcFEvXT65ukh7RU773NO-tqmY_SMnlCS3NBo3Oeu_gDyzCfVxMgARGxspgLFo2Vrdn3ONY7phcEzvMYmdIHEQysm3lypvcOlDs5LnMi6lLIMCdd144a1nU534Hoy4ksBOEG3u3zm3htidSLMjfvplxs8jXO8KeePR7vEYhugV-NVtCUW8DX3g_rkAqYkuwbgw8jH6a1iF4OGMrD73a9DZrNB7bshWOb1yxmuRt18-HNGO5Qx4iZaT5zN237yE4cvWxe9s01a-VB3j7HihNQtYVoRa4eqdJYMPFWPqlsEOV3GL2u6E41xXYmtZghQo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حامیان پهلوی هر روز به یک نفر حمله می‌کنند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/farsna/444027" target="_blank">📅 15:12 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444026">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4edf909c74.mp4?token=QoHn-zx5rdi-54aKGHY8rz4uFKdotyIpK2i5g34tCeUaYEiaxJgjSNdFcEnBLSiokf-WFRiVbLbfCj1FHkCXZZ4FVLvF8GZ3lExT2JbeLknLERL5h6tsgaRa7JkZlCYTQj34X7QmGwUrfBx1n8T47AdWMZhuyl9Sivu54P4yPPSUh2AgdbJF2twunFJU8-VVzln6QdJ70zuR3y1vDmWQspMO5grY9R0MxjluoV709s5qZ3PkWPoFQzF9HNDGz0VJ3YBkHttJdZwvEDX3udTpxSodaH0qHAxcW9PIpoisUeHj5_Kn2c5bJpFEJFARxNNVw31xd_DWLexSAHsCAjbHEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4edf909c74.mp4?token=QoHn-zx5rdi-54aKGHY8rz4uFKdotyIpK2i5g34tCeUaYEiaxJgjSNdFcEnBLSiokf-WFRiVbLbfCj1FHkCXZZ4FVLvF8GZ3lExT2JbeLknLERL5h6tsgaRa7JkZlCYTQj34X7QmGwUrfBx1n8T47AdWMZhuyl9Sivu54P4yPPSUh2AgdbJF2twunFJU8-VVzln6QdJ70zuR3y1vDmWQspMO5grY9R0MxjluoV709s5qZ3PkWPoFQzF9HNDGz0VJ3YBkHttJdZwvEDX3udTpxSodaH0qHAxcW9PIpoisUeHj5_Kn2c5bJpFEJFARxNNVw31xd_DWLexSAHsCAjbHEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون ترامپ: اسرائیل حق دفاع از خود را دارد
🔹
ما می‌خواهیم مطمئن شویم درحالی‌که آن‌ها از این حق دفاع از خود برخوردارند، در پشت صحنه روی این موضوع گفت‌وگو کنیم که چطور این درگیری‌ها را کاهش دهیم. @Farsna</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/farsna/444026" target="_blank">📅 15:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444020">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HeUqdnmUyWWUpCaj3ILIrsGQoYOekh4Q9oLSJG2-hgfTWFQaowHk0e6OZejWa5bWursHtosAJJZp4ODL6aubhzh6qotvKdGuJsuQhZEZZW27nyhybtYwDCuWEGLtg-Nv4FJ-OjlbKBu3lZvF_9RDz0syfnXU9K1kE3VtfEYayHd0hyJpIr4cV1QCbNmAO9wCuRQGD3HoUU2WkYIUgZHSJ1O8j0-mSNUyqZsxO_JeZ8BlL0p6qQbVpUJvRaTpx6A4wn3FWwNud5GyD4CQi3lPYUYilcRBxKkReNpn9bbjYpBEx6BUZ4H5YOSk8vrmCGNrzEHkMDpUF8eQSG0bIt77kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RcdTJKubRquVa4DkycO_d7VP3y7OroCoOLMpSi_d_aLWxCm3QMm-uutnlAbZiRFf5iVZ-vl_B2MLwre8pKVIoSu9oSM7XS8oBU6oue6-XPkBKRwwnJBHOehm4aKrI7ccPZsKTIdCX0k9bJgdU9TKqQMahGuoq13L24cfhE5rDQYOKEkC_46gvp3KCXhAka5lHbERv_n3Rc2J1zOQxGjlF5CPf9frzXHqRPsz-VQviNRdS5__KZh_-ova7mTSTlP3OnaZdTTMJKOSLBuvpF9KEI5zZR4-UaddimDXI-5UvrTjPvkwSF9tk1_qrBQkqo1fegWpS7wp87cg2AMoFGtmiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d3IUAhNcDRW4CQAPWGE4O2n3_XxpLsHG6kM1RfRAEABs1TwfSXS1pyedH1C-tVmgXhybAerqFNJC56WED48SYzLREj8wkRSDea5A18heJG5fHZ5v2hYf2Mj2CBOdJNBFTH_YOxjs_sindc0LVmLoBf44j3J-c87VhmlmmWNwRXkdPy7zRutYbYTi6xOeHgkb_3nBHFzboCt0UzLaYTWY14Bl4dczZzlnY7MZQAWq2Jlt47n0rwqrXEl8q30OzOgPKX6HYw2LCnuBqwYzYzmjDzZOCE2eMq0gFXPXIrqWiecEpQiYyblKVNHBEH4z1Xn-Yn9y0QG8J4lphKP501SELA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jU2dI-6_9EJO5EBflsfSn4ZicUB5rKkfmt0DloyLgXRVuLcVTYWXA2NHUwGh7I8pvJE3MEWahAeoOtL7wjjyZ4qFLgCwNPG7lH_M_SRrr7c1W4LeDOvDdT3S71pnLAKXpRo5BimBhx4Z8f1Fu5l9fnabHFXpqND3VOic9fgIl4EWnLWEWs1_-XluN3EskiZJHZRxqOxLY79i0vSGOOnBAbJ5hSrGBnhxFVO1PwsuiiWmd-gAKhFNMaQisCEYYnTN5l3DQ1dY8FiqkbBLPaYsEYbJ_C6eVBhdwtQkGaH8sRquEiXx6rUBfwQddT7mdDiWA6EfYixjC9khYRhAtL8lTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/idT-8hu7SyKcBPQWCDc1mG6_p-YG1JF5D41Qpq_ZFsKgEWKiTn4uvh-jBQtxR8xKbBf0ZCwZfejBghklMfiTvnzKaUSb5FWFHCfGmEiD7UPXZXpc7S2v6_EJH5OiJD30Kk72jpcO6cVkGgf4jMPI6rY_NXsu6nG-o9G4Qy90zyDMr4Bi2iuhQanFN6B_mvdx-zyqM9eGQMtR8MJDXEWr-D6UiXIsFmwe7gbENFZKGs116icvzn0tuA5lFaVoQ3KC9Gum4pQ4-dZl94YEGaifkA1dG2R1qDozFQoD5Zi64nIGW3CPjAv7AhCaJKUi1yJOpNaQJA9BPPSAhaR1ekskXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IFt39_OguWaSTyLr3OvfUVMya413wz_5eMvYOyxRfNFFNr_RY7LeJg_9M7B-mCTpnx4umEX6OLbncDmPjXvGFYWLbv0NiV75hkxf5h1v8fzG-EO58bjIIE0taYik1T2iYzV1nFyPlMhamyZQTqsKvv1Mac2yh3ddxZk_9fW5KEtIGJCduDBSWE0M30qDKyQxYqV7sLZAcKoQ-kwdhx4AxAPxKmvxBHHeVjdWF5DFtEC32mPv551ZU81aJSME22cAXReEaHVDaZductfpDxWtw4SLuY4Cs_Psoj5MTu-WYJ2etI7WGO8-AMHkY84RS7TyxoE5qOKUTvdquYWK22mVmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
وقتی خمره‌های سفالی بوی نذر می‌گیرند
🔹
هرسال با آغاز ماه محرم، در طول ۱۰ شب اهالی فین بندرعباس حلیم نذری خاصی در خُمره‌های سفالی طبخ می‌کنند.
عکس:
رهبر امامدادی
@Farsna</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/farsna/444020" target="_blank">📅 15:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444019">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a0fd76046.mp4?token=XxJj_DkgasXXLcTNCnYDo6AxJJlRW1aVHJCWyk2H8YdJgsVkNe_CgTD0mJ_cKHXEAOqJj46cGr-ud3X3gBQhqnUq2oh9ctWS__pp7r9cN2szb-dszHITx4UfkLtkJqYsdn8JG6Awb90ArpeNbFznJZpe80_7fgvwnnsgZa2YIWHPZHdCwFCCT-jlnlHuYIIPcLzw8iXv8dve6Nsd6EDiIPPraJFVpRRU1r1FLuwJ4HUMb_3Ww7DiHyQBKlMeLqx9XYJx8V0lLHVYMQvfDkGgkAUg8rycCmGANfCsarc8gKEySdzAzxSx5gBPRcorRM0HgOh0GRlWwcPtRMsSyooegg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a0fd76046.mp4?token=XxJj_DkgasXXLcTNCnYDo6AxJJlRW1aVHJCWyk2H8YdJgsVkNe_CgTD0mJ_cKHXEAOqJj46cGr-ud3X3gBQhqnUq2oh9ctWS__pp7r9cN2szb-dszHITx4UfkLtkJqYsdn8JG6Awb90ArpeNbFznJZpe80_7fgvwnnsgZa2YIWHPZHdCwFCCT-jlnlHuYIIPcLzw8iXv8dve6Nsd6EDiIPPraJFVpRRU1r1FLuwJ4HUMb_3Ww7DiHyQBKlMeLqx9XYJx8V0lLHVYMQvfDkGgkAUg8rycCmGANfCsarc8gKEySdzAzxSx5gBPRcorRM0HgOh0GRlWwcPtRMsSyooegg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون ترامپ: همان‌طور که ترامپ گفت، گاهی اوقات آتش‌بس‌ فقط به این معنی است که شما کمی کمتر شلیک می‌کنید
🔹
در مذاکرات می‌خواستیم مطمئن شویم هماهنگی لازم را ایجاد کرده‌ایم تا اگر شلیک یا درگیری بین اسرائیل و حزب‌الله رخ داد، [با ایران] در گفت‌وگو باشیم و راهی…</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/farsna/444019" target="_blank">📅 15:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444018">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d26db87a.mp4?token=Y9JOkX-n4vHtkePjHNNf3iGfolxKA_xogcA753MHZzzHd7R0GXT_8E2zpjna2VzlqsTMrV9Sh3LduqabokLw6UjV_3GhIwlQ_c_TY5eHA9uTOASqQf1Bxp_j109meGpsqHny3vNOOJA2UwGOlbyPwYzkih10UfWgTkQ-5BHpmnZBGF-Kb_RUdLD3r-RkPL0Wl1D7hEOp8nMIyZp82smyAHxyUdDIZtfPRykl_2BjRLX9NKlO8QcvQT1B6dp2qsJLeTfhyzDVLzT5F8dmL7gpXb7zSUaYmE9OqDXdBKSHJ9GCciCwB9h2Q_IuS_aKSm6Gm-mj4UjWYYnWHlmSxCS0Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d26db87a.mp4?token=Y9JOkX-n4vHtkePjHNNf3iGfolxKA_xogcA753MHZzzHd7R0GXT_8E2zpjna2VzlqsTMrV9Sh3LduqabokLw6UjV_3GhIwlQ_c_TY5eHA9uTOASqQf1Bxp_j109meGpsqHny3vNOOJA2UwGOlbyPwYzkih10UfWgTkQ-5BHpmnZBGF-Kb_RUdLD3r-RkPL0Wl1D7hEOp8nMIyZp82smyAHxyUdDIZtfPRykl_2BjRLX9NKlO8QcvQT1B6dp2qsJLeTfhyzDVLzT5F8dmL7gpXb7zSUaYmE9OqDXdBKSHJ9GCciCwB9h2Q_IuS_aKSm6Gm-mj4UjWYYnWHlmSxCS0Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون ترامپ: همان‌طور که ترامپ گفت، گاهی اوقات آتش‌بس‌ فقط به این معنی است که شما کمی کمتر شلیک می‌کنید
🔹
در مذاکرات می‌خواستیم مطمئن شویم هماهنگی لازم را ایجاد کرده‌ایم تا اگر شلیک یا درگیری بین اسرائیل و حزب‌الله رخ داد، [با ایران] در گفت‌وگو باشیم و راهی پیدا کنیم برای متوقف‌کردن این شلیک‌ها.
@Farsna</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/farsna/444018" target="_blank">📅 15:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444017">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/596445e94c.mp4?token=BbvZip5mvX-FF4RH1YDUelgtX09hbBmU5Wc972Z2qCXU2LZrF7VkyJLvV8w9LUVWAABSdI3Zfx89xMskd2A7g-x5Lhq5pO2eZqytLJxKYoz5Q8bny2w8Nf_iPeVlU6-L0SzW5we9449a28PH11T2xds9KPnZ6AcgNID7dQAR85iJAQpN5cZWxaJ3ZWPGvjIeRFVFabfeWq8Zu0sOeJBJKIrpjq6sCMoaOZ5wHUUpUKCmjPyDPT6L3Wf3rAhvHYEqumuUDnbZZD8_ahz3W7t79v_KahJhbc3wN2-uRrbRQ34xsadU0ZNnUbcWbbMok6ivwSUb0llnQ_zPhl3mCX_Ukg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/596445e94c.mp4?token=BbvZip5mvX-FF4RH1YDUelgtX09hbBmU5Wc972Z2qCXU2LZrF7VkyJLvV8w9LUVWAABSdI3Zfx89xMskd2A7g-x5Lhq5pO2eZqytLJxKYoz5Q8bny2w8Nf_iPeVlU6-L0SzW5we9449a28PH11T2xds9KPnZ6AcgNID7dQAR85iJAQpN5cZWxaJ3ZWPGvjIeRFVFabfeWq8Zu0sOeJBJKIrpjq6sCMoaOZ5wHUUpUKCmjPyDPT6L3Wf3rAhvHYEqumuUDnbZZD8_ahz3W7t79v_KahJhbc3wN2-uRrbRQ34xsadU0ZNnUbcWbbMok6ivwSUb0llnQ_zPhl3mCX_Ukg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از حملات امروز اوکراین به پالایشگاه‌های مسکو  @Farsna</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/farsna/444017" target="_blank">📅 14:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444016">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igTUakqyCisvkFIZ-qPDBcbjdPbChtx6ZwWaLqKkdvXa_3s92A_Bv4-CbtR247Mdd6Tn_hh4LtMkm1OzBQWvVRW7sOXhdxeGwI9QfKDHBr_6jH3OvJ2v-lLk9Jt1kd7YYPFChgM-XUBw8JIn9X9z1hli4EZbxCZ1Hk0bwbyKv7zm81Cof9xF-btGWSRzU2FJ0zmSIOCTlMy7qveKpyqqCSmmH-hQCXfIIINaeKbfzFxzKNXGu246ZupH0yUv31yWd_EtNk7aQmi7aQkopoFpX-kOWdiroEPXeJ6P2-rNeLscyTUMJAgFMgbdc8jqgO5232QGx_Fa6Ms57IsfOXXEqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحریم صادرات نفت و پتروشیمی تعلیق شد</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/farsna/444016" target="_blank">📅 14:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444015">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GS_eTnJb6hw3FH-cOjScVEdfTB1w1J0lBR903oX6-kk59E54oOz4x9a9ponBjZ7Hv9R8ihx-Bxibwny5gHFgqdv8r8cG3BF0hPkKv_e-xZ3VfovmSFcJNaiLIrTfX42BvRqUEi73ONMbsl8l7FqKb_N2XUUAW-63rRoVSwetPAqu8EtuDG5S1401yxS79JskoneMVnAYZ3utAQhDcbigq-7OpioZKTs6-XX0us8oCoHNtJDMy_YB240ygX7uVts3wV9oscnI9rzIWEeuRY6A1-Zj0GH8cLdFfPIpH5Mj5hSL548qo7xXVOsJOKUS_RcRtmAxlJjqdC8MIANT1HX4Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچ مذاکره‌ای دربارۀ برنامۀ هسته‌ای ایران در ۸۰ دقیقه دور اول گفت‌وگوهای سوئیس، انجام نشده است.</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/farsna/444015" target="_blank">📅 14:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444014">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4929d7f10b.mp4?token=jJYcBltWF8OldKOcmZ0KVwBiCzk9n8xU8SzYlEBH7lZlH-EzkYar7SHHb_7Rm3iRe3jKfsiGpA1XAZuE5fFx8wjrWrqRDK5opaLUmGlwzA0uaJC1yo-QXVvxExT9FosvSRBo1UvoqmgUG7nom7lBdE0etrgaExYVEep8g29N7vD6E9zTR8QcQHH-yoxMyQ2fY0e6vP_C60KZ58d7WYf-w70va0p7H_aVuocGbtPeUvYt7bm93H0Q-_vnAmlyB-UVdpQD5mbSGHVkPdZ-4FYSukSAFgNXSiwDkxiEzWERqS0MCx6OldDUQhvZ7JLyDmp0SGtluNSdKmDBvyeYUyLwqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4929d7f10b.mp4?token=jJYcBltWF8OldKOcmZ0KVwBiCzk9n8xU8SzYlEBH7lZlH-EzkYar7SHHb_7Rm3iRe3jKfsiGpA1XAZuE5fFx8wjrWrqRDK5opaLUmGlwzA0uaJC1yo-QXVvxExT9FosvSRBo1UvoqmgUG7nom7lBdE0etrgaExYVEep8g29N7vD6E9zTR8QcQHH-yoxMyQ2fY0e6vP_C60KZ58d7WYf-w70va0p7H_aVuocGbtPeUvYt7bm93H0Q-_vnAmlyB-UVdpQD5mbSGHVkPdZ-4FYSukSAFgNXSiwDkxiEzWERqS0MCx6OldDUQhvZ7JLyDmp0SGtluNSdKmDBvyeYUyLwqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برف‌روبی مسیر کوچ عشایر در روزهای پایانی خرداد
🔹
روزهای آخر خرداد ماه، موسم کوچ عشایر خلخالِ اردبیل است و این روزها مسیرهای تردد عشایر درحال برف‌روبی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/farsna/444014" target="_blank">📅 14:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444013">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYON9Ab7QCx7d5J_3pv3BFxZFZBaeYPVCHvKA_ehPKtJnhhrOpnwFmOxImiPmPXMqtd5gKDp6SI89JIsIx-9SQlGEWpvYskhNkjoDTcOpHq2ROMcrvuMxqIpV-AX8IaB-tdNOqAdVbbME9h9GC7DHIFGkZw-AbKWSml4JQr6vbCcrPYsI6dPPGrhH0cuuNa0VDGryUh1PomumShr4FCIWhKUxVEKPNH5hKuIDeWfCaPYw7jroCCVt1qg1hChdjKF9a_Daj2taVuTNgKuDMibluupeYoQ34X22ubLvegS-6LflN5lRBnLIQE2CZYrTGI6oUspU_AAykDCG9wPxEvmDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اختلال در ایتا به‌دلیل قطع برق دیتاسنترها
🔹
درپی اختلال در دسترسی کاربران به پیام‌رسان ایتا، پیگیری‌ها نشان می‌دهد علت این اختلال قطع برق دیتاسنترها بوده و تیم فنی درحال رفع مشکل و بازگرداندن سرویس به حالت عادی است. @Farsna - Link</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/farsna/444013" target="_blank">📅 14:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444012">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjkDcL1LqBIpohkw7P1SbQLGBlYwjrDmXaQfOKLIk-ocahDJcMcKJSq8TxCQBRCbVtK-i4JKFJmUokiyWKwPse_tTPp9WF_Bn8sgUqfWhHLuRUiUcS5CyltpLuaEgVA1MwWISkLZ-GGwqZ2f-3LmN4yb6J-6ZRRHCBUvH2SYNZ7aSQqaKeS73SVIXoXODEz4BATr3epXpKsOvHqx0Kwt-xfvhopJdnbsxOsKY1EoKf0O1E3Qqfx1zKDPaevAnw39S12aKLeaeM6-VA1qLH1Vg2Lv8wqDYeKcBnCTuudRF9A9kMy-AdBYQ7jQlGyCmMVxMNKkCRHIt986SS18Ilb3HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اختلال در ایتا به‌دلیل قطع برق دیتاسنترها
🔹
درپی اختلال در دسترسی کاربران به پیام‌رسان ایتا، پیگیری‌ها نشان می‌دهد علت این اختلال قطع برق دیتاسنترها بوده و تیم فنی درحال رفع مشکل و بازگرداندن سرویس به حالت عادی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/444012" target="_blank">📅 14:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444011">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1XnwuhF47RXzYDxvR3gbmLnrD0hTNAFV0UyBAoWhw3SqO_PziIGz2wMMeNSItTfjy2S99c1F-dpk1SWtbTezkkbYOva8jxLetjrzPzvXtN-KgHA15i5KZ3V4Fcc6r8pFRAnYWWKL_a_aOinNoXYByV6dRtcShek-Y_omP9tcOrAnphQJuneMQp8ueeVmd5-96tWPiRDKfvJejVjjolzx05a60_xZc-uylbESHpX9zclyp30DCysXVddjLvn95Z3pl5jDnH2qcUnax-TEXbN3CAxaMMCC0I_7v8VFuTxU1zXeFumSNh1uwodQi2dW0kxDCBWLRgnIRdOWCwvN3r8Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
هوش مصنوعی روضه‌خوان حضرت علی‌اصغر(ع) شد
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/farsna/444011" target="_blank">📅 14:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444010">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">المیادین: احتمالا پزشکیان فردا به پاکستان می‌رود
🔹
المیادین به‌نقل از منابع پاکستانی گزارش داد که انتظار می‌رود رئیس‌جمهور ایران فردا عازم اسلام‌آباد شود. @Farsna</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/444010" target="_blank">📅 14:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444009">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f2b8417da.mp4?token=E65GKRryWzc4SVt7bwsJWHYtiJpkU6lbE8_3dCQOg6rSJTLwPPBYMaZ7xYUX7eZa5wJeS_T2PaZxAxLrJHlcPC5drUv47uv6Ce6GnhU4DDGEjj3DMyqUe4FA4OcyeAyobwX9dDDqwTloJH5uQAuS6lGHyP1fufqr-YLiOSRJKHello6jigGwT7gOs8xdT3ZeHYuQ4teCc-Xem27skvOaO8eJwR5blS_3p_0Fl9U6OoaXFv1FTObUWzMaX_leUbos7SLMehXPeMM3acewBWOfohcG18zGDgBgq4TSUhzDW2FVpn_IZDLcTlRM4UVKJYwZatpziwhH7rynld5Xt_hl-oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f2b8417da.mp4?token=E65GKRryWzc4SVt7bwsJWHYtiJpkU6lbE8_3dCQOg6rSJTLwPPBYMaZ7xYUX7eZa5wJeS_T2PaZxAxLrJHlcPC5drUv47uv6Ce6GnhU4DDGEjj3DMyqUe4FA4OcyeAyobwX9dDDqwTloJH5uQAuS6lGHyP1fufqr-YLiOSRJKHello6jigGwT7gOs8xdT3ZeHYuQ4teCc-Xem27skvOaO8eJwR5blS_3p_0Fl9U6OoaXFv1FTObUWzMaX_leUbos7SLMehXPeMM3acewBWOfohcG18zGDgBgq4TSUhzDW2FVpn_IZDLcTlRM4UVKJYwZatpziwhH7rynld5Xt_hl-oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ رئیس بورس: بازار سرمایه از مرحلۀ تثبیت عبور کرده و در مسیر رونق قرار دارد
🔹
برای ورود بازار به رونق ۴ برنامه داریم. نخستین برنامه، تسریع در عرضه‌های اولیه است و در هفته‌های آینده شرکت‌های بزرگ‌تری وارد بازار خواهند شد.
🔹
توسعۀ ابزارهای مالی دومین برنامه…</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/444009" target="_blank">📅 14:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444002">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ooWVQtbbTBWsKUBqbBCXiXOt9KUrYZtoNvqxKfwHLLmkHIeo0m5jekGGsIzCNCf9HtY5TjZGH_r2kN_B6yvbswDAbNaJeqzXkJ0yXc969lYUCKfgQ179hy8SI78mRSYkd_vtHsKgPYPNjumq-qOykcIu62xUZkapIZseqSs4ElWBSyAaIJt3TWUGElnVwLPBZFyw8ovppYXy5Wl0BvsGkRk7PGDCGQrNm5CU-95wPbwp7xTDxtvCz-XxsErALhsy_-PUOojlCSawFy4yhr_6x_jZzXp3V-2C8Bl1eM4CWJGyG3Sj6YtJUnpsJhjePWptVXBZjiAiFkzZUdo_WNIQTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BvPdnbsrsEqaP2tFpKeKRyZacsRchbJXp4E_Z9l8JXKWXk983fxriBV2mntHDvixwc98RQrl4H-f3Ut6afuXygSR8XYkOTqUZjlXVtF9z-XNAMxbHaectB0BEYO6XsiMkUt8cHRm0QLXY-yTDkfvkdQalnBzBjtaXh63fLgRg03h0ZpD8GtQ_WQ8LlEfacb10-gKlFK275tTqotgtaJN48vhMec9ByM-MiFY4UvUNa1C3fgDfUb-M5u4RaK4Nc-VxwnzIwexocfn4xtn-Vr_vapCQbJ-JC58RGBeJ3IUdRNJ40H6x29HpKbYKUDDfmQY2NQquSmjSKm9Pucog_8gAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bXlftBeHoaCwAyf4ImcuNa6SH7o4uLSaGdjNHmViKhsHCZuIPfb7oogqDvuj6UapG3ZpvedHxNdBr7s3FQT59ZVKj-tTVibTSxd8U68f32HpVdZDl5HMf0Kvin1pp7IMC1MiFWfAPQdtnu1dvXkoix0MdZ7lDOE_HcSEf0WV_ssu5mRxAwuZWWHZvlPRTFz3GTm81VLG7cl6mvjVHg4ps2Ip7Uf7DBeAhw2ZM-uBYC4MfPrAPjjhKK9xyJ2h_pVh0hGJ2gZ0k9UoekuxxIk_SB-rLe_S4kj-wKwQ57SFi3Jen3UT25MJ97Pol3C0sycCQ5Gt8l3xCBJvtnZtsF29VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M-ZQVBMoMded0hFQHRXLwzDC0oI9OEym626A9K0uPPzjuGJsPnE9WBM18Xxi3zouGpSyCfqHPRht4nSrpiPOXEKyZSpwGCEDR9hEPP3JKA7nhpZfdZE0BHUJJBkWlI8lT-CVao_AXx-tZl8O2pIrM-kDWvoLs839ZGUg9vitM1gNGbeZJ09GGJZOzBIOdwPumLOGkXNtbhjMMxoSm75E27vS8LT3swgCNtvUmjuAWCVwypaxZ2a-OBi0os3W6CpL5ZisscrvAymCD8BrV2SPu2zGnDPv-cCw7jCK0Bo1ncxmVOAb_DX9zgksbVzmHKPfpHzERqU4CenuRCnSMdnzAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HK19m7xZxWIZa_ziSQfk3oRspXC9J8eiEiMfx3k9CevS2rlvgUd9V6_NUxAdHBeW7TZ7AGtSGWt6IVR5wDX8r1jXz8D4XVZc6HPK1eDAzxLeuS86mwAnDxmXbOaXZET4onZ51C1pWZqlZE0J7mo8cOqQgVeFdA7UHfaHigjjMU8ZRSfj3T05tv4Gracl5fuOygcRqKJ7teLe2J_44i7ISNHfxXLHeG9aO_S1y3-UwZLke9JrcsFOa5-W0qEXE9tYIVWzmCVdJZGA0Fdg8Ha1KcFr6tem4grADq0ISPMFWBocrcQufchzSjwBM-ZO81hwkKzHShoCJ_z7UWxm5bjkpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YGW5_rniYycfvj1wmNOJqC5hkuWvJZerwY-ZQjvJkJq75u_9cdR17xNKoiItYR4Lq_rkX_ndRJG7Mi9G6TFOTY4oOCI5hBSwQds7gKLhD-eQ_fz0mL0F4p1Mb10oXO6uRRoZJHmRop6910oNbVhxwE2U0OW8q5Sp07HL1eoAXLum1moLOm_2hic2e3c5XfOcpYNd4BzG47WxXG8eT_OQBQ0daJAjakh16OxjyGbWZerMQC4gDCuXFPegnkO_HE4eLiytadqgx7c7fQ81s07HBigWTUqQEuMXFSMSWGHOoMG0cbXU96iuIdct_pZNbKG2d_4olx4FoQERdD-PeYTPlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WRlO4qz8JkK2QTS-y8U6ukqU1-z0T3WwDq5YOn0I4YbElWzyFn9vztlfp4sVannmq-0PQbxssPLb1QKDpPUGkFq3r6n8y_DUxMqYOqX3wpq20p0oU8cMrcSPYmcd0IDfDusa4clzbRwcOXiY36qJ4isBsWANmvu9BpHfDL0OMHl1lbBO_e_5V0wpwekJmRRuay061yHR8Ke648ZoLJaKAdGuMtRd2q1TO9aMxOO8IiAIKBFxV_AfgFEiilNY_7NtRGBMm0v51Mh6KqNRRrGhHzELX_GsrVWDlV1bQfh2pbJEcufdGyhiYNVC_a8JJteig1bYc2yV2OWu7jPXLhQYSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
چهرۀ این روزهای ورزشگاه آزادی را ببینید
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/farsna/444002" target="_blank">📅 14:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444001">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/If6Bfasd1lP3TuGhx8YzymDJSSsCAFya1O-N8LvvbnNJdElORIgHUI2I3oHcVL0sSh4bvj_fKPFHj6cCXGYsnzV9MCPPumhUnehtUo0YWu4APQ-MtFcjrvBEfwiAnuJKg9dQ44HLh_5mV2ui0evcXAyDO7bUK0C0dcj_PgeDggTDH3XgRqVRSmhUKdFNlGQnaUCVDZmDkvhuhAC9Z-RJVuBzW3ayYjGAnMCvyWCXN4KmBy4nJSFItajBB5-5c_ba4FUZoqXVLMX388UVNw7u3TQGk5yN9H38gymCVUfqUk-uSBudqqgZVFrRKdrxpRXxFC1PQ5-6jO_-x9w3DpzQVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در دیدار مدیرعامل بانک شهر با مدیرعامل شرکت مهندسی و ساختمان صنایع نفت (اویک) تاکید شد
💠
توسعه همکاری‌های مالی و حمایت از پروژه‌های کلان صنعت نفت و گاز
🔸
در راستای تقویت تعاملات میان نظام بانکی و صنایع راهبردی کشور، مدیرعامل بانک شهر با مدیرعامل شرکت مهندسی و ساختمان صنایع نفت (اویک) دیدار و درباره توسعه همکاری‌های مشترک به گفت‌وگو پرداخت.
🔸
به گزارش روابط عمومی بانک شهر، در این دیدار، ظرفیت‌های گسترده بانک شهر در حوزه تأمین مالی پروژه‌های بزرگ صنایع نفت، گاز و پتروشیمی مورد تأکید قرار گرفت.
مشروح خبر را
اینجا
بخوانید.</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/farsna/444001" target="_blank">📅 14:17 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444000">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس پرس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8CmEiEGh26uG7Nl-23ynPxcNYCuYOafAF4GWufqCSWYxG9ge6XFjP6-F_RHNgH_1txNHal26LAboHIBjEhokMFB18d3vuC4sH3uq_61Z7wv63EZDGBgrCKTdlfMAAgR_SfUxWv_afg0VxvmZoCEWwSf5hnR8w-oq4Pt_OzkMBNJHcuXoFV8Q-eX4dH0VsLF6uf73_ya4zvpGZQfbzhirAoXG2L22uPtGzAjH4wE4ZbFwoCWrahvLJHYv3oxSHXzonxNvWax6Ja_IpDrP37VWbVc0Le7DZ2T0pc-at_79MbSbGE2bk00Ko22JQlwr8JmRHOdAYd14dx6j5ZSsNeStQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
در جلسه شورای معاونان شرکت ملی صنایع مس ایران اعلام شد
‌
🔰
افزایش منابع زمین‌شناسی مس ایران به ۲۲.۳ میلیارد تن/ ثبت عمیق‌ترین گمانه اکتشافی کشور
‌
🔻
شرکت ملی صنایع مس ایران با ثبت رکورد ۵۵۰هزار متر حفاری اکتشافی، افزایش منابع زمین‌شناسی به ۲۲.۳ میلیارد تن و حفر عمیق‌ترین گمانه اکتشافی کشور در معدن میدوک، دستاوردهای جدید خود در حوزه اکتشاف و توسعه معدنی را در نشست شورای معاونان ارائه کرد.
‌
🔹
در نشست شورای معاونان شرکت ملی صنایع مس ایران که با حضور دکتر سیدمصطفی فیض مدیرعامل شرکت برگزار شد، مهندس شهریار متوکل معاون اکتشافات و توسعه معدنی گزارشی از مهم‌ترین دستاوردها و برنامه‌های این حوزه ارائه کرد.
‌
🔹
براساس این گزارش، شرکت ملی صنایع مس ایران در سال ۱۴۰۴ موفق به ثبت رکورد بی‌سابقه ۵۵۰هزار متر حفاری مغزه‌گیری اکتشافی شد؛ رقمی که معادل حدود ۷۵درصد کل حفاری‌های اکتشافی ایمیدرو و شرکت‌های تابعه و وابسته آن به‌شمار می‌رود.
‌
◀️
ادامه خبر در پایگاه خبری مس‌پرس:
https://mespress.ir/x6Rc
‌
@mespress_ir</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/farsna/444000" target="_blank">📅 14:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443999">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/farsna/443999" target="_blank">📅 14:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443998">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با کاهش ۵۳ هزار واحدی به ۵ میلیون و ۷۳ هزار واحد رسید.  @Farsna</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/farsna/443998" target="_blank">📅 14:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443997">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LtyvfKrooZRPvnKPKMjntzTUGLsdNaZwfxsqxoPw-VgAiGCx_CgF-MsQlxY08jWN2bCaIqdBYLOFhLbjT1VJqsn7YBzSTUQaRnnigybV8E5ddrFUMtdOF3j96vPtxCCh1MoPLDzmlmH3D5U3NGtJ7_SNEO-wclGtT6sqO3Kzc74lAW0IbuihsIvdLbOjaWYuVKF1edRslhcnY-AwzEYuDAc_t1dF2Tau426kXpi1Aae72mabYzjC1pNNleY8JqfoBRmwO8JJBqkKCLN1cKj9Klghd1HOPM0srRcXgCQ0koGG-YSfh_XlC1EsmB-TOieUfI2i6dogDWGOsgIzfk6tCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جنگ تحمیلی اخیر ۳۵۱۹ نفر شهید شدند
🔹
سخنگوی قوه‌قضائیه: براساس آمار پزشکی قانونی، در جنگ تحمیلی اخیر، ۳۵۱۹ نفر به شهادت رسیده‌اند که از این تعداد ۳۰۰۲ نفر مرد و ۵۱۷ نفر زن هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/farsna/443997" target="_blank">📅 13:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443996">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VwQYNQ92hD5YGqQN29gCpXjDDk_AiMoin1Dd1hvEXn6vv1SzksFfAqbgmgRn5HB72CnR9ihXDu1tCLGxuUXXXBW88Nzrza9bXUy35_wJ9VxIVvMnJDkyzGTKGC4t2j8gg1LQqtcazEujXZDiLHj2I1DX0kEtLVJuCw1NeG7GoEI1mphNLIAcokw4nZSH7ngZXziEmto62HzLYQ7YS25K1bz86DQ7KJ-4SR914m_CCBRm3Zyf_l43eLNsMIcrNZ8BvBodjCZj_qWG_gWJ7Ehr9iUMrJ9kKcsW18ftPNV7AgAPRsl-bo6wR6Ki81bgLPPAdRDjroP7YQ2KHLHDepJd0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاره بلژیک: دروازه‌بان ایران همه چیز را گرفت
🎙
ماکسیم دی‌کویپر، مدافع چپ تیم ملی بلژیک:
🗣️
من واقعاً با یک حس خیلی بد اینجا ایستاده‌ام. ما شایسته پیروزی بودیم و موقعیت‌های کافی برای بردن بازی داشتیم، خود من هم چند فرصت خوب داشتم.
🗣️
امروز از آن روزهایی بود که دروازه‌بان هر چیزی را که به سمتش می‌آمد مهار می‌کرد. با این حال، موقعیت‌هایی که داشتیم واقعاً کافی بود.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/farsna/443996" target="_blank">📅 13:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443995">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mipbi23medAuqMKMm1Y56JJ_C5XBOD3LYYQdzs_GeojFbt-HwkXJ6_r9bwV6_G0otJcX8CYvEza7HTgznMyD0pKLR2NL2pDN1J-fTN0j7OTcs_HmT0y_eVI0ejRhoIJYTfQfJoif2kPFTt9Nkp3v8DtGx0oZAIIhNJVgBn8YowchzlAzpvcPn7HDxcQGAGR6FdobBF6BPS7Wu4_PNHtWVmWG9nclq6srT643tKhk6Xri-gfHBepYJDbWuyt-MjxAtyP6MqeWn5l0ux4-ixlUDa_SdbXTVIVoIMSXQKqOnV6x4DzAcWsm16bY24mWsxb8YaHEc5zd_5bipnTGEX1rAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">المیادین: احتمالا پزشکیان فردا به پاکستان می‌رود
🔹
المیادین به‌نقل از منابع پاکستانی گزارش داد که انتظار می‌رود رئیس‌جمهور ایران فردا عازم اسلام‌آباد شود.
@Farsna</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/farsna/443995" target="_blank">📅 13:48 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443994">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdlAFIZN3PXvrWhOcnn2-qCwW7yz7pl6LHsd5Z6pso1T08oT31J-D3aSr9DmED376LVuu3bpBTwk5hD_WzYt7t1Pn0xvqrD8p51T2PlMEgb2CZnEPKsaiKewTBbLyIlVt_9ZDZXi3RptIPtr8RrvTOlr8IjlJnmumeUmGqz_qiqZkK0Y2YDqL_1iod_HSu3RGyE8ctob6hgQCvFoJ1_1-nF6OU08NIHhJXoFnL0Dzwp8HggwRhJSVTugPJYrYgH6g3SxfRI_Jq0yUb5lTDbo4T7Pol_0SFxe9BpqnQqJMBjF6ky_tA6jX_MqUB-hi9--p1vLjkj9prxP5WVZ3OgTDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۶۰ لیتر سهمیهٔ بنزین تیر خودروهای شخصی شارژ شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/farsna/443994" target="_blank">📅 13:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443993">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35d95cf9b1.mp4?token=fQ4OoboVzO4YVCAMui7LW-W69L3yqOBIjw0qR7jFEQW5XIpcrwHIHVPEp8ImuUFiSLE_OJ9sHDZ8pDy8uhQ62caPHfqxjJ94RVsdONp3YLTtbWyM1CWT21he4Wl5VqKajlmG5YvB7m-UrWvu-BbR4RPw8myJ7WibNdkG4eEtrOY8uiaCAafz3c7J4cRNUbUIxnFEJw4XYaj498koWB2ZmTUgD05egnleRTODqlyLSFapQXFB_vyIMMBDfyDcdIzmhDI0xhk9f1iQsE6MjwL1NWejbcONUl5NlCU7AEklYsLzlzZAqEItDk2CBPX8WWAW_BksPD41sKh8lQ9MARSQtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35d95cf9b1.mp4?token=fQ4OoboVzO4YVCAMui7LW-W69L3yqOBIjw0qR7jFEQW5XIpcrwHIHVPEp8ImuUFiSLE_OJ9sHDZ8pDy8uhQ62caPHfqxjJ94RVsdONp3YLTtbWyM1CWT21he4Wl5VqKajlmG5YvB7m-UrWvu-BbR4RPw8myJ7WibNdkG4eEtrOY8uiaCAafz3c7J4cRNUbUIxnFEJw4XYaj498koWB2ZmTUgD05egnleRTODqlyLSFapQXFB_vyIMMBDfyDcdIzmhDI0xhk9f1iQsE6MjwL1NWejbcONUl5NlCU7AEklYsLzlzZAqEItDk2CBPX8WWAW_BksPD41sKh8lQ9MARSQtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دنیا به افتخار ایران کلاه از سر برداشت
🔹
واکنش تماشایی بیرانوند برابر بلژیک و نمایش دلاورانۀ تیم ملی در جام‌جهانی واکنش‌های زیادی به‌همراه داشته است.
🔹
خبرنگاران و کاربران شبکه‌های اجتماعی به نمایش شجاعانۀ بازیکنان تیم ملی ایران مقابل بلژیک در ورزشگاه سوفای…</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/farsna/443993" target="_blank">📅 13:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443992">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2JSLCVsHNfSL49YvX0sqidaaTJWHQp10cqyBjvK9ZQMrkxIoj80PHI0a6yF1MEr82kpNIzKWbMZU1jbIKQTH3cam8oP_R9f5_cuipUskzw1H1AA9qJwFtULRxTOnr0DUHeJf4Ud4BKIZMhtGmKbKYm3ztMYIO82pJOdz3zUc9VLI-75S_l3FygepowmXdFss_z0QNbVo3pa73uJZfKYDZen0NJA8ZTw7rnz8vBUly7HL_K2I2KRE0aZMco7_r43LmBHY-_5XeXTouVwPvSvm6NwrfuQWmmQOUkatgfjrcCXmURZi0riiXFamGjBVgyIKpXi-FzhamfcEMpFA119Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
پیگیری خبرنگار سیاسی فارس از تیم مذاکره‌کنندهٔ ایران در سوئیس: کارشناسان همچنان در سوئیس هستند و روند اجرای تفاهمنامه را پیگیری می‌کنند.  @Farsna</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/farsna/443992" target="_blank">📅 13:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443991">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9046bdbfdf.mp4?token=spln8eT53BFTl_PuNi6RDoJSa_qPGDzEaBrzqKqGGwqDMVCO0RFcT26MSY4g_1BUHZ_B8GmMEpjD0T_pQa3hYlURaj1bJmF4W5ErEQbiTOesrICR4nTK3Cp50zoaW-FO8rCENlAbWtOY7FutSHMth6SGAykRi9L-GGdj_57WUq4xBxIVercuM6NfvKadYZ8gyQDLWahQCvsl-UfbJGncK63_arEjIl-90GUPzjHZhHdOCHGToXKwjv56aHwBsA_AqfvQf5jPqy4wy3rk7YXgl0p_LAbOKEe6KXrRUcqvTzYgp4Jxr6rIVZWnSZ6D76oeZYvg0U8ZHqAWbKzeIsiH9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9046bdbfdf.mp4?token=spln8eT53BFTl_PuNi6RDoJSa_qPGDzEaBrzqKqGGwqDMVCO0RFcT26MSY4g_1BUHZ_B8GmMEpjD0T_pQa3hYlURaj1bJmF4W5ErEQbiTOesrICR4nTK3Cp50zoaW-FO8rCENlAbWtOY7FutSHMth6SGAykRi9L-GGdj_57WUq4xBxIVercuM6NfvKadYZ8gyQDLWahQCvsl-UfbJGncK63_arEjIl-90GUPzjHZhHdOCHGToXKwjv56aHwBsA_AqfvQf5jPqy4wy3rk7YXgl0p_LAbOKEe6KXrRUcqvTzYgp4Jxr6rIVZWnSZ6D76oeZYvg0U8ZHqAWbKzeIsiH9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: صدها راه برای عبور از بن‌بست اقتصادی وجود دارد
🔹
شما استادان و متخصصان حوزۀ پولی و ارزی گردهم آمده‌اید تا راهی برای برون‌رفت از این وضعیت پیدا کنید؛ امکان ندارد در دنیایی که در آن زندگی می‌کنیم، راهی برای خروج از این شرایط وجود نداشته باشد؛ نه‌تنها یک راه، بلکه صدها راه برای عبور از این بن‌بست وجود دارد.
🔹
چرا مردم هر روز وقتی از خواب بیدار می‌شوند، ناگهان مشاهده کنند که قدرت خریدشان کاهش یافته؟ شما و ما سیاست‌گذار و تأمین‌کنندۀ امنیت اعتباری مردم هستیم؛ پول مردم را می‌گیریم و زمانی که می‌خواهیم آن را بازگردانیم، دیگر ارزش گذشته را ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/farsna/443991" target="_blank">📅 13:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443990">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c525fa3b8.mp4?token=Gyl7r5kPVpcS4ADtDJ1lKri1BiW5IRTjDOvGY4HcaE6xXW9CQbwAGv9G8OQLk9V4TNEv3mb3P4jUgDKHXW1408U7tUFuFtW0h3RFWanFTWFduSXO1LfpwWPkKDx8vwRthO0d2LaQkjeRUjWc_Kw_WNzsH5P4AgkAzpuZH4LfcbEu-gsc0evqUou_GpvKsQpHahrbmIyzAft6pdUTCMVb-z_xrdsRpNlF0KAhnlKFepdVx26o_7aX_UuEeFZoFduwGuqLzMA48JZsgExN5hfKLLn4hCH8s453qRJQbTgC1AU7W9GgdkpjyGXjr_pIKP2gXOt2v4zGFcnbprp05Gf7zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c525fa3b8.mp4?token=Gyl7r5kPVpcS4ADtDJ1lKri1BiW5IRTjDOvGY4HcaE6xXW9CQbwAGv9G8OQLk9V4TNEv3mb3P4jUgDKHXW1408U7tUFuFtW0h3RFWanFTWFduSXO1LfpwWPkKDx8vwRthO0d2LaQkjeRUjWc_Kw_WNzsH5P4AgkAzpuZH4LfcbEu-gsc0evqUou_GpvKsQpHahrbmIyzAft6pdUTCMVb-z_xrdsRpNlF0KAhnlKFepdVx26o_7aX_UuEeFZoFduwGuqLzMA48JZsgExN5hfKLLn4hCH8s453qRJQbTgC1AU7W9GgdkpjyGXjr_pIKP2gXOt2v4zGFcnbprp05Gf7zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دومین کشتی کانتینری پس از رفع محاصره پیش‌ازظهر امروز در بندر شهید رجایی هرمزگان پهلو گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/443990" target="_blank">📅 13:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443986">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/edaiRe-p9THsR12DrXi10wC7nkMibeF0uwr_XqsWploHeGaNpAdd4RfMjEe9YH6DzyjfGB5X_LXlehEdDoK2NyosHoco7cB3UdnG7T_W2Ku-IteeY8B3l9Q1jlcCi6RMi28Z1KCeCX6VEuglBsOzWc5Z85V0l7nmgElmxB2YSZkWWYC9D5R98Z7hexSYgNTA6bwZ0v7JExf3kOxHeOVVdMziHbW0gxVf4YFqaq2apQ9Fv2HFGo5Js3U8WqV_U8NCb-Zz6Ft2IG_gW0zmlLGjDo0CfxGngbAHtSAoElQ9juZJFm5xfU8gt8ULtiex3la1V0uvY3sFb67o7nokDUwwNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RJTqv5kd5FrhPpjMSZ_rvEE9ij1dXbo_58mfM3goY4-GPFT-75QoR6nqg_tNpA_ATtrfoXESqiGOJpu_9FK2RwmEDvo8ezHc3n4fe-tR1PfrY2dYwQaFgOOuJOiGTAPyvxhwcZfsrxBebTm94wF1Phjp1hnK5OCaAWkiQGJKtIFQqq75xt-qUUOoBjVCNOiFj_psidRptnoN9tmOx2lv2gGhMSdkYWCuUYnTyB2UwV4t2l_ZhYd4FiBlkJ7_VXND2P94XVZklwH8EBevqoshpA78xugNwKr1-pCYn9TnTyT0lBNxEXeJRc69fueUiTN7EtcgdJgllP2DArtl6IjsSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hPzQGKfTGUgRcTTMF7DwLGpVxHgX3bBfY20u-7UjRyeP6CuaVt8xYgcPd8_0lyLqCpG0H4tD1fCuwyDYRCwNIp_ryU91JIKfZ7y1kjijxUDeoEw-1DGk7-wS3qLrY2D9xWfTcUeKxPSOxM2Esdm8RkqoqdJsCycNxS3Fwf5uLEB678f5162yBNNmTwMBJzuMEexCSTXESaIHzfhhKvn37twiIfJAEHKe0cEZSjcRNIDur2l7ExvdFxCXrMm67QWnspkQj07875geUA2P0keojlPcNti2QHoy3h6Kl-ylBdanmSwZbVFNZ0FEZhz9aLmiVN3baosxg4uYK-sLtEd6Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AjthyKxjmyhFeQjrRtcZJFHw_ETHr9RwGuolhbf66bVSaccsU7KFEqnb3kriJnzDgILBQZbk1eW1ZZXr2SIsMheCtS9-XRRZtrkFNjGj5S-kE2ESlYfm9dwNQErfJZTPXUoqMFxoD0I_Wr7_Y8-gO8yrV0mS8jFl_Cpji66aXkQwGNXkPTnFvDIK12EaTBQZJRzU0tpdT7d2yXQDZ4PR5aRAB5juAYkDqZpU3b5pH29u6oehpAdYIKXIN-jFVWO8xHkOiRTdMF9loCVuqHn-0Iq4QEmGuG5v1WGA0Fb4LkGbtPC7zPBk4q_SiC26wN_TiFW0dJzMp_eoirEtjH7L-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
انتشار تصاویری از سردار سیدمجید موسوی و شهید طهرانی‌مقدم
🔹
تصاویر دیده‌نشده سفر سال ۱۳۶۳ جمعی از نیروهای هوافضا سپاه به سوریه برای آموزش پرتاب موشک اسکاد در روزهایی که ایران هیچ موشکی در اختیار نداشت و امکان خرید آن نیز فراهم نبود، سفری که بعدها به یکی از نقاط آغاز شکل‌گیری توان موشکی کشور تبدیل شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/443986" target="_blank">📅 13:08 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443985">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XoZec1DtF8wSMLA30UH8NfivqboOsrSuPrBFF9chQ33NtNpu1XCf1V3b4_jczMqln7U3rPEt5SIOShLTo_a4DEmfYyYrs4rkC0vBEKFaPTeVscpM2Gd31WKAVQFcc9HN-c8MPHbmI9I5wmTmplRujE333M7zm-UhlJHtUA8Ljf7FqkxQZCIBqAHp4kOhOzdOmwhjlm3_Vz-nHxSBxCJhudoFwckhVkcPuPCsD5xxz550nuUXEZM8mxQx6Dz-VsHGMDoBB8w0N4FYVbTavuzN_vkGj-S82jgba6pc-YFr5ImNP-Bh1MdzidfMWjfniS5jo6Qk25NZNRuP_I62yTGkkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی ایران و بلژیک رکورد مصرف اینترنت کشور را شکست
🔹
براساس آمار شرکت ارتباطات زیرساخت، همزمان با برگزاری دیدار ایران و بلژیک در جام جهانی پیک مصرف اینترنت کشور به ۷.۵۶ ترابیت بر ثانیه رسید که نسبت به سقف ۵.۵ ترابیتی هفته‌های گذشته، افزایش ۳۷.۵ درصدی را نشان می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/443985" target="_blank">📅 12:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443978">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O5mM-MfaK5eThETtgrhWDgQM74Ohl0x0UJdKW-M1Pq-ogI3ZE0tTJkZRyPg50M2ke1NIViZW2Hc4qIhKZgEfe2PQE2qZvKyxwflP0lkT5H0BhelxnMlFCvDzZyNUgtWfMq8mEmzu5DM5Wsu8fPnEZbzG1Env98w6731BWyGbw-oN8VcO4L58tenI9u8pKGCaMYD9ZF3tV0ZqGQRjbR2DP1Q-fVBaiM87XzSHOHn743SWAP50f0FQuVRplZUOaUFEqbuBYkpyxH5syxURY0U6ZYEmhYxn4KwVcCbwGHAKEr00EQ9qNgv45OIzgv-Ue_7QVPT1llmy6MRNG7hRIZiWEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T2AUw2_DZVmPlPlzA_5rEwrJSIX_bHGtLRw36yFmjS3ZFeKdpGOsUaGVC4f6tr6kCMjd_gDS33aN0fJNQZLWyvph8tfNuud9-p_qJQTZZ1i7HBU_JdXharuT-rlC_c6_aVaiFNIuIWJ_pixN3TYZFTHCBywBnhlalN445C0gxTE-GdfeVS62sI1kQMUqAE-0cubbNQHl1RTs5Id9hbBZlSywJbl6GxykQ_GLi_swRqSU9B9Oq2wMn3xOkcCnAkOpIWfxx9rvwGzoS3SZrBpNzOrGghFRJQ0VV0mUmRf7XJWXzc5tjYJi5DRJuiqEdMCwRt0uB_86Q6_KKXcD3Zuy4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SiqVFK4xUVTBVq66uvyDGGJRypQ4qjR4gjRepiS3-noEDG4dXFlNi_KVsLSqemYBGhkfqmLWbMNSKxZ0q0rd8iJwQzvkI153AFscFFwyjwZCk6dxo9dol1XIGXQJcXjI8hRAIyDJHkj8SqSIbX7E-N_4T5i34Py7NShMu0tSdT7ZTzeyei1aZ4xmg-We1X-fEJaTbUHJq0lJg-0ryR2COk22HSPSFmJIS8g3TMrSKsr6LhocQJoppLV_dxuIxmliLIjQVcyK8v6KWdfdo5KzqBUWmAW5IKpEyvxvzP9HYGHMNh5wgaM1Kvcj108UaiDIyToly2eqZslVW1azjqj3LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WIi1P4qeEx5ioDAgDz8eMBtGZyE6n4IL0_d2X6y0zu96Fxd9XPNmUY5ldRaiJFyKTZ8LWCpHQ6a0AGU90o_XAPflsE-g6C2MRmMnqBFClLbC726dzr6bXhlsyoWrbLvMZymXKxSiaczTpJesvbySs87PMDNaQ2ipOije0aWdPpyqx_oyDNvk6H-d5LCzi5nuwnpKYIJFuKSR8OD-y9diAi7gO-XO2bsmzytCyf6Ev3k_B2tLLoVS7z848fkopKCRe1D4qOPTNlpdad7B36g2a47iBdvs2ZvXeTP8DEtgmGQPCXMFrZVUmLN9Ittv3LLP67ZkdH6W3K9n_hXicgwlFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Is5eGNe8Kuockdtle27xkOHbaQPjcuojsX-zCsShjPjnR965ZYObcw6aRMO4zvVq_3qccZIa8DgjkQdIfDr3UVFOjAToN1vjgP6mgK_THZN9cYf8wibuOKcHry8H8Z1ckwUi5jLaS2eG1D-xGkIbm0TUhIryDTdYQv81_6Caza-0OuCenjtNVTDMRnGW4IJJ8i-vQb7Jclf4TkOtexwTmfbD3kRNXSmAW-0nF7cANL49q08aZ9Vgu-e7pA_Hwn9YJYuOhZiABeBTJrw4-ovZ8QLQeEfJajUH9VhAT8V2_n1r5pNKFzOz_gFUr1nI30wo1pXkR1H1-Y0KrpZ4w9vuPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NEaSlgwmAV4pKoTZ-zWa3n540ThkhlNEPGRgBg7QcQGVKF0KX4dElhgQCdCyWkoYR0h5Bm7CbXqA-meULIJuuwkbxJgCsmfbKGxCXUdipPVAsa0oBsl9D6yR1YX0H4Pn7CnamQyCnCfJvtvVfFLT43DBWTSe6wIMQw1mvVPSNQFYtVTfLOYqLodNxqd-pSgpOSqg142mGGsexFTPk9HUs8xKa4duhiiQsPuUds89G6pVWktstYwIU3i-crRnKqa7VObTak8aR9J8VEwB-wFWtgUJDoDL78-yMvChtWJbjhg4iwNw3_3-5scXLl8mZOnQhI07cFC5I_cmPnuYycwhdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HuYsa4PFD59sJIt3gV9heTue-lX5C7iuySiHuK0gRm3yseiq3fCRZuMWUlupEE3xo6g9lQcZP5t838QpQ-vwEhrqp31yMFSiMtxTLwJ8AZvF_ks4fI9o9XyW2muwsTumO-dmKEHyNyH_vtCL23nJnm6v7My-N52aVYFxhA2QoM07GPBc0Lirrxl19s_xSiwHxTYAehcsb3vO23edxJqyeTUbR0Sp0lA9EFABYiEItziTGYfX57bbQcC9Si_Jo1mHVoJImYbBwbdJC0QzErbu8IUGGHU_rWPclLKPXq6zT1Spa_eygQrhO5U59xpAEb7K605S0XCVO13q1891wAYt3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
سخنگوی ستاد بزرگداشت عروج رهبر شهید انقلاب: تشییع پیکر رهبر شهید انقلاب روز چهارشنبه ۱۷ تیر در شهرهای نجف و کربلا برگزار می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/443978" target="_blank">📅 12:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443977">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFcaeG4XNQrDHq97QDLT06xNlS4ZOjhs_NDcCdtUBpe86FwF_o9oaxZv8IupNl9mt4fP14tpDxKjT23SgaQS2aAPaHAtOusyaQk7gW8oizsb9NjGAAa7-itsW-7ZBtt5NgEVJl6Al6I_ONvLyWIp7IcDwptQMbzMqbRu-QfzartlCgkYQKMj91gJTfwWFmMS7-MYsSk59wSmqgDn4fXsnQeXDv03wXL_P3eXcS2ezFa_xmf7lEgVVKr-7saj89Rv0JyReurh-u7tos7kBTzvukipUnC6LWHXlGtVG3zvGF1h6UO5LUmQ1tiUAYvYBXRjpHIewCNf6lZCAWPHM-YC4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با کاهش ۵۳ هزار واحدی به ۵ میلیون و ۷۳ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/443977" target="_blank">📅 12:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443976">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/053f57ed74.mp4?token=kOxDn0YkFltTuQTCEwfBDH0Y7Pf5KgIJ3m95A573LFpvHjA-1qvlBMs32RuNm_nO8mm3xTnsY_iKvxZ8cTvZ3miR-o2y38cP8CoHQ8nmSxocWjxSnU22RLD-MKyWKuXF-8YwvrkeH162PeOmdxCymy7whEl_HzhTv4PbUhmGxYQ9a-2Kl6A7NJU73MzqR8H6OFOWR34LCqMBV0hVar-DEIzBQO9LzlKKyivqqZIVmRTMkcF0MBOm_a_tZUIJeMxaZamqa36EQ1fs3GvfmKT4WBJYx0iZGQXjfL8IjnU60_Vn0v2lx_zFrvWnhipFXazejTRoANYSmdq-RcQlBPNXMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/053f57ed74.mp4?token=kOxDn0YkFltTuQTCEwfBDH0Y7Pf5KgIJ3m95A573LFpvHjA-1qvlBMs32RuNm_nO8mm3xTnsY_iKvxZ8cTvZ3miR-o2y38cP8CoHQ8nmSxocWjxSnU22RLD-MKyWKuXF-8YwvrkeH162PeOmdxCymy7whEl_HzhTv4PbUhmGxYQ9a-2Kl6A7NJU73MzqR8H6OFOWR34LCqMBV0hVar-DEIzBQO9LzlKKyivqqZIVmRTMkcF0MBOm_a_tZUIJeMxaZamqa36EQ1fs3GvfmKT4WBJYx0iZGQXjfL8IjnU60_Vn0v2lx_zFrvWnhipFXazejTRoANYSmdq-RcQlBPNXMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
پاروزنی نروژی‌ها در میدان تایمز نیویورک
@Sportfars</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/farsna/443976" target="_blank">📅 12:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443975">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHFUD3kEcPogOZ7xNsuwIzHCUYgHSrZQDKnIoSyJlEa-6LbqDqFBxz1DV8zpAAR_rl1MaBKcAcl51xVV_Hy_kFfSFcSnYBZPH1WpqtT5CJTw_t9B2TYI96paFVFBIEQ5PAf4y_-QfgUokGZJmXhzQpi8QtMSYQE6tTknkY_sBhVAFFposUH92hP7n9St4ZhOF8sDJWj3tLdQu2Qaqb9rqHH2Z-F0RKB9b9hmEL2Gqmpi0npAU3Y713ePN_hp6a_sZElsAdmYWG2LfrPLwqt9zQuIBbbD27jyKOk091AzI_1MpmuOAdzu2Ji1KtoB47NHJRoUFFeG9edqfwB-oTvt2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف یک تُن انواع مواد مخدر در يزد
🔹
فرمانده انتظامی یزد: ماموران پلیس در ۴ روز،‌ درپی توقیف ۱۰ خودروی مربوط به قاچاقچیان، يک تُن انواع مواد مخدر کشف و ۱۴ قاچاقچی نیز دستگیر کردند.
عکس: مصطفی گرجی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/443975" target="_blank">📅 12:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443974">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">استانداری هرمزگان: صدای انفجارهای بندرعباس ناشی از خنثی‌سازی مهمات جنگی است
🔹
حوالی ساعت ۱۲ ظهر امروز صدای ۴ انفجار شدید در شهر بندرعباس به گوش رسید. معاون امنیتی استانداری هرمزگان در این‌باره اعلام کرد: صداهای شنیده‌شده در بندرعباس به‌دلیل انفجار کنترل‌شدۀ پرتابه‌ها و مهمات عمل‌نکرده و باقی‌مانده از حملات آمریکا و رژیم صهیونیستی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/443974" target="_blank">📅 12:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443973">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‌ تکلیف افزایش حقوق بازنشستگان مشخص شد
🔹
درحالی که طی هفته‌های گذشته میلیون‌ها بازنشسته در انتظار مشخص شدن وضعیت حقوق سال ۱۴۰۵ و صدور احکام جدید بودند، تأمین اجتماعی سرانجام اعلام کرد احکام جدید بازنشستگان و مستمری‌بگیران صادر شده و از عصر امروز قابل دریافت…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/443973" target="_blank">📅 12:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443971">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilVUaYxtZQQ2BfO1hy1f-1_PUHnB1mEkhlscOLjn0GEMEIhcQOgUaIQctJ7y8E9ukWvecBEo-S9D-duPpRpn1wnjP4uH_Mjmg9_peuz6AhSbPcU2-x0IoqbTRTNJPv1s8ikqHSJx0NUECOyRs6WmdVskrHuCaHpW0csX3TUKsip95BIn4YWX_wPPwpivBFaqguMP6hyb0WggATR0MacHL3GtnIOl8p1L7k4eLtGFCsBgTLIFz9olX9FNviDfLM3cQoXG1s_hkXVjo1k3MZShdCglXGGzT-3jXv_ut7TvnhUBYYTHr0fNNPqF5bUsmxMX1IeJCx65w4lIn245lIh1MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منابع انگلیسی: نخست‌وزیر به ته‌خط رسیده و استعفا می‌دهد
🔹
روزنامۀ آبزرور در گزارشی مدعی شده  که کی‌یر استارمر، نخست‌وزیر انگلیس احتمالاً روز دوشنبۀ آینده استعفای خود را اعلام کرده و همزمان برنامه‌ای برای انتقال آرام قدرت ارائه خواهد کرد.
🔹
استارمر که در ژوئیه…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/443971" target="_blank">📅 12:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443970">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXKPG8C86JNrSDtA8RbNRoMztsrmvSLm9txSdJ2kATeUQRUORLYSuA8yDlDCjossqTl8O60c2WZl4JL5te2KdiibT0x0q909IndjyaBAkVZVAxtw0e9zANOVMruAVG8IsF7pzrz_-GEEbjzo0Z2u9SF59qmFa7pGavTfQXalSaQCn42gq77tmUiIUElvJiSA6e85JmGn6oqwLyweamkTouF8a0uA5-KOgeZL5Syq0Q8HVqEWZo4TKG1bmkQuVq1wLgywuGKP7EuqQxB8JgdgQI3GdA5acTmeA6vJkxbxx0y48tXi6uqMxJhEu954xjcRFhkzI5dj8WUgnSaH6HN3pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس بانک مرکزی: در روزهای آتی بخشی از فشار تورم کالاها کاسته خواهد شد
🔹
برنامه‌های جدی برای کنترل نقدینگی و مهار تورم و نیز تأمین ارز مواد اولیه و واسطه‌ای واحدهای تولیدی داریم.
🔹
بخشی از افزایش تورم کالایی به محدودیت‌های وارداتی ناشی از جنگ باز می‌گردد که در روزهای آتی از این فشار تورمی کاسته خواهد شد.
🔹
با پیشرفت مذاکرات، انتظار داریم درآمدهای ارزی دولت افزایش و قدرت تأمین ارز بانک مرکزی از محل منابع مسدودی، افزایش داشته باشد.
🔹
با برقراری آرامش در منطقه و پیش‌بینی‌ای که از درآمدهای دولت و منابع بانک مرکزی وجود دارد، انتظارات تورمی کاهش پیدا خواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/443970" target="_blank">📅 12:08 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443969">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
هیئت مذاکره‌کننده ایران، سوئیس را به مقصد تهران ترک کرد
🔹
هیئت مذاکره کننده ایران به ریاست محمدباقر قالیباف، رئیس مجلس شورای اسلامی امروز سوئیس را به مقصد ایران ترک کرد.  @FarsNewsInt</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/443969" target="_blank">📅 11:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443968">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tw--DSK3Ac8rosMaDu6YjKjDdyZdefyIjDkn5ZR3d47svEsM7jkbJiFxWIJHh2lR6pw_3-QDhvjSBXB85bfRwQkIhpxVYA2-HiToIll96IQ6zBBWmLeNDW6SbS4fuW5QLzqUpNz-7XiIL03kRWlwV5nb_BZmYdMAlOBdJ2S54sgFSgl7tEogOu5pQ45Y32lWM-4LWrMDjHauUPYjv8GGm04Z8mHk47C-sTWiqJe78fL64hTBJCkNulVM2I5gOVOWpJVpBoh0ElUoAzsgA0_OGPXSxP1lDrm5MSnYKxaTGhWOA4tKTpnisqzgrKky7bEMvD0nzL344xCIB37diC_oNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات ۳۶ میلیون بشکهٔ نفت ایران در یک هفته
🔹
تانکرترکرز: ایران در یک هفتهٔ گذشته، ۳۶ میلیون بشکهٔ نفت خام صادر کرده است؛ تقریبا به همین میزان نفت نیز همچنان در آب‌های اطراف ایران و روی نفتکش‌ها درحال حمل یا ذخیره‌سازی شناور است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/443968" target="_blank">📅 11:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443967">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/My3AWFr2uExTtB0Kb94e9ZJmJzs6WEEWIH0DI9XydYiDSgpBrE-fQJMYOa7tWd5iBPhadD23irN71w2ondJtYmVr1zEFnnMStKERqnRF4x-H3xXOjysGFtKXosxrQgbpD5u0cL2eM0cLKCbxmNsvSNOGN3Mijg0gFVLIl-JxNqKpKRltXRq_Oejz1txswT9UoZewNft2tJ3ct0J0Np68aznLRgm8Pi49Bkk8DOZYrNndGirrbMX8GC8U1Wht7gt7vbQacOK3Vtq6Tqy5rETsaIzRBQc_ZGoDE6MI0yC9JGxw-7UuoOm6dCKSvmBOSJQ45QstjuSmUFCiZzCWn2TcLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفحص پیکر ۱۳ شهید در جنوب لبنان
🔹
سازمان امدادونجات لبنان خبر داد که پیکر ۱۳ شهید در منطقهٔ النبطیه و مرجعیون را از زیر آوار بیرون کشیده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/443967" target="_blank">📅 11:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443966">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yy6A6FLAL5fCB9up6Pn5VewCxKGgBxK-T1Uj6nRCwj_KFhrqKWhlQVo5ZdOZZcqhXBneRx_wqk-G5kR_Am66TaHQjnxYuVNKwQ9SfCkC1pi2mU3OLmKMm9u3N77qF6Tx0vmH5xWtCScvfEFO9illUF8fni64nsV7btLSYED0-IbqM_zKXspojneCF9fBVLJs9x1a0mXy17ZKXaut_Kh9YEk7Kv8UDb-lcSJe4dBwtGo69xDQ1LBpRpqegPjn5gmIGmy-oLE0arhZjv_Uq7roKUoHPVbJWGk4pYYx0xobibNHTyixxta_RA0S2ehWljyRqeZCB3nyXDQNV0j80XWc0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
جدول گروه G جام جهانی پس از تساوی ایران و بلژیک  @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/443966" target="_blank">📅 11:12 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443959">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HXg8RIPlg7VF-zuvpFnvaE0NnSHNi-9Qk8Pv9FgfjPEWpUBKLm44KxDInk9Uwy6HgMgi3plERdPnLNwWn1A26C5S7LDlcTzBtcxozbg37OblxjiLpKYxs7BH8nWagOfsoWT9L1PHMxZd51wkmALcxwZ0hCudSs-5s-b0d1HGtMQUEtrAk-rNj9a9H8GHbl_siRfpEyIcWGj8Pt7PSa3wBYyvG3CtJeRlyFyZeeh-Y0PmzdLI4PHHWS3qhruZGDL-BljCKhXgBZCQ8taVMz8EHUSmE0pEb6nme196ETvpal8HFIoNSbyFikQYb-19HvIbfKYr3FHxuLtfPg9ScTINcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BRElNdzPbiphMIREgL01y3qyJpg5phZOu-A05yb_sDTrXQM9qfyX9VelhRG4gbLIOFb7oBk5_UWems14Et1IkW1j0qFoB2_2KrnZzH67IbJ0m-1QnLqpce5tqzvFTSIdmD5MV4Mphf7gPeWCDhJMaoLIU8pQr6yWOZ9h9xVonjtuggFbMrq8gH3N0BMWGaG3wRzOOWEmSHdD88UVULp2lyYdPLVCrSHuDiPYIM7az8zPiflDvhNXUZ2QOJsuF0Ron7IXhpTNTZpu2ri3Pyld_rEp7G3sAFrWKmdl-84jCmuBD5mYJA7xwh63eP9Qpu_NaH9CMvus8ylp2BHHY8_WTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hL06eFHvmWCLeHgtTFQaxRNIA6tHHP6Q1aYMlm3gm8XOulu3AsUWDyCCTw_u_20QJK--0eR04EpVdUJlDwtOKh-NuVgmqr0Nash6SqfpzlKl0mNW4dAInW0lPhk03sffehIAk_2e0APAugW_mXs2pBW1hgPERAtj4NoLXzPXbA9SnrC9N20SToVuBUxa2J0rHBiBNW40pJZl03wdE5Zl_53qPENpc5z0i0zNPh5DJ5XLH9LTPOJa2uXdehLXb_MBTfLq3-KWtxYzAoyPMhBnjd_5VarQF9QYPv5kIGb4e1esGlWa9heVz6pCixFxdZNmP85HFkt4vzx1SthIYzpvHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bufq2p1_fio54VLljGiPKNJZuAfW4yvnLu-i1IM_dxYzh1TmPSRGJTLSpMKQSIf-VhQoEKRTvKEWHc9b2bsFaVQJ7d_VtzLxFXSHcfXg4wErzVLoAHzcofUQbjbOBuEnroF59PHnEhPOgOr9M2FEyNbyZbJhIANwETdmrvowXXVutH3OIZGiju5H-hmI-2nDhrHwC85zL4JPl5L2LdV53Uu_Kd9afifa3WNocO8tKA-lYr3uDYVuEmb8dpnWTCBnW4n5Q7AHrPzgp7jWqS_pal-bqAlR8Nf58qkg8uh8l-oq2XQ4qe93OXlZHGzPMsyI8OJ0LvKwhnPYJPirm1jALA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ttS_k2fh-7CeCvSaWZTBqEMTdeSeSKiwKcELZkBQU1EwGBWxoNts7R5FdwMjEfhJqXJ7kmWO-MC9Hjb95AMhmscf6V1J7rlEl91wlh5Q0C37abx0Gf7UcfGC3FgOVfoXklrOvGIpNQiA2BixwwseRxggxnVzkLzPkl6tBX6kYdts-nh0mZgd0e6XCJQDcrwFpfLFnMm42XdZD16HWsn-LZAIRkR78Hsh7c2XPx4bsxnRLfvHNZ5CtvazscOAfTABWz60ZRLapu1tSYSAjYeHrjtXCVV6vRMbXNJDR3bZJedezzUDSl_QKCcXg0p7LOPU1EvDBB5rS_w66ssUjIrmjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LvqDTUYlVucBgYQADlEgPUtUdwzqmIPqCzc3D3dRKfBpqQjuI8M3-_6LYM6oyUPRTPjYoTQiP8K6HUekjqhMQXws2h5btnBWZHtuPElKf3n2Wva4eOerFSYaxkIXropZYe8Bhfxr3xRsvyW9dkopNF37zwFZHKVdMuJ2--9aoo2lfMti6DnMV3su9SuZ9V2sfTR_D8AttPaaEtVHO8X-uXozlMy40b7SRYQjSRWBP8gmXh5vL2ywNvhq6ZGeyvhNkYr08frtbPEP5GcACkexI1iRjUiI2d5onpeFKx4nzRFr04hJ4QKUbRKcqe9BhAG0IoP5qySt64lF_0dmwYhTeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UA2b4Drd_cPy3px1TgqIJ2QRSQZ4ZY288mSgQTJuPVcAkRZQJCrJA8X8FoOEmDEofgUsusPWQYKZhSGoqqjK2LJDaQNWzSUVnvlclcycVGW6IlpH_oIR3k6RiWdNaRGYKHPelI267NantwIPhDPgWrgp23ugvmFLyFL-a0Is8S5ZVkQ7OTU-Tx7IKvTPK_mCMeZQFEAnbJRYpdOLndlAEUtNTmNA_iyAW1MuET24XJW-JA-WV03hbzLGdf40haE2o9n8YQ4VGTA5XP82e91HzASmyRJq-yGLn_bGuCOSxCDZdE8hYYVcFLEiIoJ87ukpSe9W9GELTE9Xf_pomGhY1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
شب‌های محرم در بجنورد
عکس:
رضا خبازان
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/443959" target="_blank">📅 11:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443957">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tr2jb8ayEuV3ZZR8PHHtpZYKmtvnQJoveHPeQZ2EzH0ERl1IoOX8kR2_C7QHcSHOmK-kPIRGtOvftDD9j3ODtqAtBBsiLoIpqVMk-pcBrGQgJaChhPAWu3afdfy6CPnv1HFJGyTNjkaJbC3TebvhtnXcvskEs49hPMGcqYl6OqDIoaTb7cOi1E2HwS6k9lC55Ky6xEZdTi-bdC5T2spuziU9E7D3LedenEEMbAH3RiuWdfH0MDUAQDKaKtCRHitL4hOycmfs01gY6ko4O0tCzhg8D0GL1lMkMaaelJOAGfJaOZGoKmlaqaNdUfREY7hfX8yM4ZGj9l_Htshzcn5Daw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هیئت مذاکره‌کننده ایران، سوئیس را به مقصد تهران ترک کرد
🔹
هیئت مذاکره کننده ایران به ریاست محمدباقر قالیباف، رئیس مجلس شورای اسلامی امروز سوئیس را به مقصد ایران ترک کرد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/443957" target="_blank">📅 10:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443956">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a51b86576d.mp4?token=WwLbnS5twC5mGsvqbywPCW0Xh6b8UTx7RFKBd-9xjQaulVV9T2Lv_xyaga5Ou1wLL5Mf_dsWmsOjPij-0V6ZgnX4qcPLPIJT9Iegb6wJy5NTOiz6pE4OixeEO1OUyKkKc73FnF_zeSDvHJmbwumtcSFqnlEeU3N8EMEg4gPjzgNIAloHJFHhVl69DH206N8IsU8NxMlSHdxljnyQAd9OA-Ecdq7HFAyQ-LwTdGd0hTbyK4hTcYlDjTKwagTAIyVc-FJMYbcsF41f_JGVYiV7pnbfznAuCB2A7HyJfyaoGmdzpWlWrOosecwOwYJnJp56Bg2MkW2wYMZJ7lYEcYBxXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a51b86576d.mp4?token=WwLbnS5twC5mGsvqbywPCW0Xh6b8UTx7RFKBd-9xjQaulVV9T2Lv_xyaga5Ou1wLL5Mf_dsWmsOjPij-0V6ZgnX4qcPLPIJT9Iegb6wJy5NTOiz6pE4OixeEO1OUyKkKc73FnF_zeSDvHJmbwumtcSFqnlEeU3N8EMEg4gPjzgNIAloHJFHhVl69DH206N8IsU8NxMlSHdxljnyQAd9OA-Ecdq7HFAyQ-LwTdGd0hTbyK4hTcYlDjTKwagTAIyVc-FJMYbcsF41f_JGVYiV7pnbfznAuCB2A7HyJfyaoGmdzpWlWrOosecwOwYJnJp56Bg2MkW2wYMZJ7lYEcYBxXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ سخنگوی ستاد بزرگداشت عروج رهبر شهید انقلاب: مراسم تشییع پیکر مطهر رهبر شهید دوشنبه ۱۵ تیر در تهران برگزار می‌گردد
🔹
در این مراسم، پیکر شهیدان دکتر مصباح‌الهدی باقری، سیده بشرا حسینی خامنه‌ای، زهرا حدادعادل و زهرا محمدی گلپایگانی نیز همراه با پیکر رهبر شهید…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/443956" target="_blank">📅 10:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443955">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🎥
سخنگوی ستاد بزرگداشت عروج رهبر شهید انقلاب: تشییع پیکر رهبر شهید انقلاب روز چهارشنبه ۱۷ تیر در شهرهای نجف و کربلا برگزار می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/443955" target="_blank">📅 10:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443954">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1GNXQ2TZWT-9sa3wQgYX0T8Qy0hXDG1-u0NTmRjmqyxLnOBn1TKsUqHWZcKPt5_LoZM5qNM-kG3SNxdNsgMo5KsCvmssB7rysWD327tywUoRkEa-iDwt_Wx6ad4vOmzAp0tdZ3oEyX1ODHLkbcldbshVRMjuv1tTAtnHqt4ajrgzaVYnoL0SaWAm32p32sKjxHPZ3EhvRkQ5McDH_YbqPHWnPW6xcuzev13n9IbBoIaTDaq1DGICECCJwFd3CUPFJQIGtWhNl6NjdcIHZ8Y-q1qkptV6uiq446TzdVnpwk5a7gOiuJvIYok-H4U8IE_Q3VJiAPfS9iYEsUJSIrVxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صاحب عدد در ایران فوت شد
🔹
۶۹۷ سال پیش در چنین روزی، ریاضی‌دانی در کاشان از دنیا رفت که عدد پی را تا ۱۶ رقم اعشار محاسبه کرد و تا ۱۸۰ سال، هیچ‌کس به گرد پای او نرسید.
🔹
غیاث‌الدین جمشید کاشانی که در حدود سال ۱۳۸۰ میلادی (۷۵۸ خورشیدی) در شهر کاشان چشم به جهان گشود، در غرب به «الکاشی» (al-Kashi) مشهور است و از او به‌عنوان واپسین ریاضی‌دان بزرگ دورۀ اسلامی یاد می‌شود.
🔹
شهرت جهانی کاشانی مدیون محاسبۀ دقیق عدد پی (π) است. او در سال ۱۴۲۴ میلادی، در رساله‌ٔ محیطیۀ خود، عدد ۲π را تا ۹ رقم در مبنای ۶۰ (شصتگانی) محاسبه کرد و آن را به ۱۶ رقم اعشار تبدیل نمود:
۲π = ۶٫۲۸۳۱۸۵۳۰۷۱۷۹۵۸۶۵
🔹
این عدد آن‌قدر دقیق بود که تا ۱۸۰ سال بعد، هیچ ریاضی‌دانی در جهان نتوانست آن را با دقت بیشتری محاسبه کند.
🔹
کاشانی فقط به عدد پی محدود نمی‌شود. او را باید مخترع روش‌های امروزی انجام ۴ عمل اصلی حساب (به‌ویژه ضرب و تقسیم) دانست.
🔹
همچنین او اولین کسی بود که کسرهای اعشاری را به‌جای کسرهای شصتگانی رواج داد؛ نقشی که یک قرن و نیم پیش از اروپایی‌ها انجام شد. برخی منابع او را مخترع نخستین ماشین‌حساب آنالوگ نیز می‌دانند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/443954" target="_blank">📅 09:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443953">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🖼
جزئیات مراسم وداع، تشییع و تدفین امام مجاهد شهید حضرت آیت‌الله‌العظمی خامنه‌ای‌ قدّس‌الله‌نفسه‌الزکیه  @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/443953" target="_blank">📅 09:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443951">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‌ روش‌های اعتراض به قطع‌شدن کالابرگ‌
🔹
معاون وزیر رفاه: متقاضیان می‌توانند از طریق سامانۀ حمایت به نشانی hemayat.ir یا سامانه سیمین هدفمندی و همچنین مرکز تماس ۶۳۶۹ موضوع خود را پیگیری کنند.
🔹
ملاک اصلی برای دریافت کالابرگ، ساکن بودن در کشور و ثبت صحیح اطلاعات…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/443951" target="_blank">📅 09:36 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443950">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🎥
معاون وزیر رفاه: افزایش کالابرگ فقط برای دهک‌های پایین انجام می‌شود
🔹
با وجود تورم سبد غذایی، افزایش مبلغ کالابرگ ضروری است، اما کمبود منابع اجازه نمی‌دهد افزایش کامل متناسب با تورم انجام شود.
🔹
برنامۀ دولت، افزایش کالابرگ فقط برای دهک‌های پایین و خانوارهای…</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/443950" target="_blank">📅 09:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443949">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/567505fee0.mp4?token=avDTPjxLNG_MbrRVSnrwu_Sl_gEQmQGNEU1wB7CXqG_pFXqvyilwelPDpwdwYZaqKQrljLyyhfD_t1VXoN_GZvnjrCXNFjf1mvm6ausyobJNy0qeaP8-3X_BnGkwO2Lt5aG4ay4KcWa3JKWihxW7z6I_U1Ql-zW5MBeCXGwETFRxUKXsW9JVdUEggTYWoq9yMiIJqWOWfGV09o7W32Vnu-j2hhduMeDUpLYMTL_ZtBE8r9JW18iJLx3PzzESpdGr1kl8BBoBdHLpPnfit_VH29vsWOyJBt_-SZTxz5NStGHMTn-VjX8iZpVdtURUYEKjycdEm19cIz2pqFIZj2V09LeKQpKH5XrVrOh5kldLnhATn0DlckW5J6fT9GZNazrYy8sip863e6ed-EbYGumTB9fqiJ4CUAyHT2JLHCPTOICvImfW4jebMg6Oxx_UXcJuomCJ930XLF5RfAqOiHXdO5CAaKc6BUG8LcvNXa4ZKgYeS94IAGjljIhH2sqv2KA4FChTdoLFZFpV1aKxrbG_hA5RVQxrg3G9Ns6kB3erEn-NX1Qz7PNMP8d1GQIpRxWeFraz9RJuGyagrdjUsy_Aq-56jDB3E7uUH0icamuZUsReWwcGOGQRWXK-s7GpCR_7sTsP7rO8-0g0UKW5nolFVgk0ZdPZseYqqM1Wp4AVYWU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/567505fee0.mp4?token=avDTPjxLNG_MbrRVSnrwu_Sl_gEQmQGNEU1wB7CXqG_pFXqvyilwelPDpwdwYZaqKQrljLyyhfD_t1VXoN_GZvnjrCXNFjf1mvm6ausyobJNy0qeaP8-3X_BnGkwO2Lt5aG4ay4KcWa3JKWihxW7z6I_U1Ql-zW5MBeCXGwETFRxUKXsW9JVdUEggTYWoq9yMiIJqWOWfGV09o7W32Vnu-j2hhduMeDUpLYMTL_ZtBE8r9JW18iJLx3PzzESpdGr1kl8BBoBdHLpPnfit_VH29vsWOyJBt_-SZTxz5NStGHMTn-VjX8iZpVdtURUYEKjycdEm19cIz2pqFIZj2V09LeKQpKH5XrVrOh5kldLnhATn0DlckW5J6fT9GZNazrYy8sip863e6ed-EbYGumTB9fqiJ4CUAyHT2JLHCPTOICvImfW4jebMg6Oxx_UXcJuomCJ930XLF5RfAqOiHXdO5CAaKc6BUG8LcvNXa4ZKgYeS94IAGjljIhH2sqv2KA4FChTdoLFZFpV1aKxrbG_hA5RVQxrg3G9Ns6kB3erEn-NX1Qz7PNMP8d1GQIpRxWeFraz9RJuGyagrdjUsy_Aq-56jDB3E7uUH0icamuZUsReWwcGOGQRWXK-s7GpCR_7sTsP7rO8-0g0UKW5nolFVgk0ZdPZseYqqM1Wp4AVYWU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس‌جمهور: ما وعدۀ افزایش رقم کالابرگ را داده بودیم
🔹
در این مملکت وضعیت اقتصادی برای یک عده بدجوری شکننده است.
🔹
نباید اجازه بدهیم مردم ما مشکل معیشت و سلامت پیدا کنند این حداقل کار است.  @Farsna</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/443949" target="_blank">📅 09:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443948">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHAdoyKHMiS9_5UQdLzWraRkE6RfEQrpKNqDUeaHQfBx1mWI9BdbtHz7IMNsiPg4csLK6-tfmyInwgpvuKRtgqneZRz_wyl9S4MrrKPDpmTQVPMcdLL38C_EIlipXdtx8jmBniJPdDffZQ3YOKzEMPVJIm5T3g65OnM4NfnwoCt2uIvGGZX1zmkJE8vSKtvRG1fI9o2sHpUm7YtNj0Uk5sL5j2nt1xLok4ZrgrkwFcNX3FhvKDv9FOEhIkRWdJwihJW6BFUv9iIUHJxw0tNp3bTZ7CxpcsqVJ-WeW-LChvbiBCwVAwci5U60VJCnoBYdGdjy_-k79qsPI20_ebkYHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عارف: ما برادر بزرگ کشورهای منطقه هستیم
🔹
در مذاکرات رسما به کشورهای همسایه گفته بودیم که اگر کوچک‌ترین خطایی از سوی آمریکا از مکان‌های متعلق به شما به ایران سر بزند آن مکان‌ها مکان‌های مشروع ما برای دفاع است و عقل هم همین را می‌گوید.
🔹
ما باز‌هم عبور می‌کنیم همان‌طور که در جنگ ۸ ساله عبور کردیم چون ظرفیت تمدنی ما همین است؛ ما برادر بزرگ هستیم و برادر بزرگ هوای برادرهای کوچک را خواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/443948" target="_blank">📅 09:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443947">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d01uCwhqaunSGl9anlHy98AE1HjhLk5B5g8YDd3qr7JnfVnf5me4sZbHFO_9wTfWi2bZZtYI2VeJDEqD4UGonOCH1HPkRCz-bf8OXgqWzNb_QlkHwMZf5GwU9h0G1h4L-NRMn8osHrRIscRIfnO7wcw8_6lu7kN3ga6z_EoMiRrJv--jCfswOAEvV7lOuaIfCX-yesM7BSuwYZ81tSyIFIS9koSJ6jXzANw619mHSIut_m3XrEhllO4DtG4Z29yJ23wZ5-289QF38JRHh-18Q7RWewrvuJGwhG1WPybnmxv3r2x6YJotEiL_wOSF5_2hRmuB33MynNh4MMr31-kLig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادر علیرضا بیرانوند: خدا را شاکرم پسرم سرباز ایران است
🔹
مادر علیرضا بیرانوند، دروازه‌بان تیم ملی در گفت‌وگو با فارس: علیرضا در مقابل بلژیک جانانه از دروازه تیم ملی محافظت کرد و اجازه نداد دروازه ایران باز شود.
🔹
این موفقیت تنها متعلق به او نیست؛ همه بازیکنان…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/443947" target="_blank">📅 08:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443946">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">◾️
حسینیه خودش لبریز آه است
◾️
خودش امسال آخر قتلگاه است
◾️
همین‌جا بود ماه افتاد برخاک
◾️
از اینجا روح او پر زد به افلاک
روضه‌خوانی جانسوز مهدی رسولی در جمع سوگواران حسینی(ع) حاضر در جوار محل شهادت قائد شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/443946" target="_blank">📅 08:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443945">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FyO8aJxjrUG7sqyjldoE0AgEZs3dx4IB6GeZr1o76K9eV1GGyJNtbuFeRGlP4x57uaaSWSOwu-qNIAb9yKnbs-q1z9moa0MpKAN5md9DigENNZuZ7mBXzbJFvB3yzb9RB6xDBrZMtJedYktUkxXLXSkUJt7M0OH1ZPto3uBBLZ9V7ExqCw8g-EvNJAyGsbufXAaC2ehdACFjcsWKLP5e0p3H7R3qp6GHLh7xVBTfUKodhUV8ckmJr9P72wLTqQomt0hBKVYux0NTPXFlGTU9bpQW6fyVLPxP8q0pu6s_84aZTtyi8JwhHQelBbcpi4xFwAcqOu1g7i00lXOa-jN8Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲
اثر برای شناخت مردی که امام فرمود: «مثل او بمیرید»
🔹
«مثل چمران بمیرید» تعبیری است که امام خمینی(ره) در یکی از سخنرانی‌های خود به کار بردند اما از همین شهید تا سال‌های سال اثر قابل توجهی برای مخاطبان وجود نداشت.
🔹
شهید مصطفی چمران که سال‌ها در ذهن بسیاری از ما با عکس‌های سیاه‌وسفید و روایت‌های جنگ شناخته می‌شد، با ساخت فیلم سینمایی «چ» به کارگردانی ابراهیم حاتمی‌کیا، بیش از پیش به نسل جدید معرفی شد.
🔹
از دل این فیلم به جای آن عکس‌های سیاه و سفید، دیالوگ‌هایی ماندگار در ذهن مخاطبان جا خوش کرد: «تا زمانی که صدای اذان از گلدسته‌ها بلند می‌شود، ناامیدی گناه کبیره است.» جمله‌ای که حدود سیزده سال پیش بر پرده سینما شنیده شد و امروز نیز همچنان معنا و اعتبار خود را حفظ کرده است.
🔹
«خاطرات موتورسیکلت» ساخته امیرحسین نوروزی نیز از آثار قابل توجه در این زمینه است. این مستند روایتگر گروهی از جوانان موتورسوار است که زندگی مرفه و آسوده‌ای داشتند.
🔹
اما با آغاز جنگ، مردی بزرگ به نام مصطفی چمران دل‌های آنان را دگرگون کرد.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/farsna/443945" target="_blank">📅 08:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443944">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">برگزاری آزمون ورودی مدارس نمونه‌ ممنوع شد
🔹
براساس بخشنامۀ جدید آموزش‌وپرورش، ثبت‌نام دانش‌آموزان جدید ورودی پایۀ هفتم مدارس نمونه دولتی، صرفاً بر اساس شرایط عمومی و محدودۀ جغرافیایی، و بدون دریافت شهریه انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/443944" target="_blank">📅 08:12 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443943">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">چین ۱۰ شرکت آمریکایی را تحریم کرد
🔹
چین اعلام کرد در واکنش به قرار گرفتن شرکت‌های چینی در فهرست سیاه آمریکا، محدودیت‌های صادراتی علیه ۱۰ شرکت آمریکایی فعال در صنایع دفاعی و استخراج عناصر نادر خاکی اعمال کرده است.
🔹
این اقدام حدود یک ماه پس از سفر دونالد ترامپ، رئیس‌جمهور آمریکا، به پکن انجام می‌شود؛ سفری که ترامپ با هدف کاهش تنش‌ها و تثبیت روابط پرتنش میان دو کشور و در جریان گفت‌وگو با شی جین‌پینگ، رئیس‌جمهور چین، صورت داده بود.
🔹
اگرچه دو کشور در آن دیدار توافق کردند برای کاهش تعرفه‌های تجاری همکاری کنند، اما روابط واشنگتن و پکن از آن زمان تاکنون بار دیگر تحت فشار رقابت‌های فناوری و نظامی قرار گرفته است.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/443943" target="_blank">📅 07:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443942">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9e98253113.mp4?token=AAHcy7dfs8ginY-vgq7kbWT4CBC6-mkL5iePyPw0EuI80KHDCvjSpkOnwTgHzNYB0klKkqMcUaMrdHeexQ7Ss788aKbPeC3vGgzHXBPMvw5omVEAqiIj2ZNp6LeV_mIxD8ntZkZLTdypVEpq9XjaLaGkdYCLxwmUd4m4pjlE6lKpJKTnB_xcR1ujMNvijj8Z2IHBxlvGf1mu-pHyXF0mq-op8hYAGr8mnZh1hCi_wjHFHrYp4lvHOZ8YLIE3V44GtLUnTiiRYZRa4c_jOmA3ZA4RKZAtX-a3XMpZlG2R2RTMqwE-gy78pfFN59J-_yxZespkWWHarfiodas0NcaStg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9e98253113.mp4?token=AAHcy7dfs8ginY-vgq7kbWT4CBC6-mkL5iePyPw0EuI80KHDCvjSpkOnwTgHzNYB0klKkqMcUaMrdHeexQ7Ss788aKbPeC3vGgzHXBPMvw5omVEAqiIj2ZNp6LeV_mIxD8ntZkZLTdypVEpq9XjaLaGkdYCLxwmUd4m4pjlE6lKpJKTnB_xcR1ujMNvijj8Z2IHBxlvGf1mu-pHyXF0mq-op8hYAGr8mnZh1hCi_wjHFHrYp4lvHOZ8YLIE3V44GtLUnTiiRYZRa4c_jOmA3ZA4RKZAtX-a3XMpZlG2R2RTMqwE-gy78pfFN59J-_yxZespkWWHarfiodas0NcaStg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تیراندازی مرگبار در یک دبیرستان در فیلیپین؛ ۳ کشته و ۵ زخمی
🔹
در پی تیراندازی در یک دبیرستان در شهر تاکلوبان واقع در فیلیپین، سه تن کشته و پنج تن دیگر زخمی شدند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/443942" target="_blank">📅 07:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443941">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
متن کامل ترجمۀ بیانیۀ مشترک قطر و پاکستان
🔸
بیانیۀ مشترک دولت قطر و جمهوری اسلامی پاکستان دربارۀ اختتام اجلاس دریاچۀ لوسرن، نخستین نشست کمیتۀ عالی‌رتبه با مشارکت ایالات متحده آمریکا و جمهوری اسلامی ایران
🔹
نخستین دور گفت‌وگوهای سطح عالی در چارچوب یادداشت…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/443941" target="_blank">📅 07:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443940">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brV4X42TlX1ZivivlDvY5-WPArEiASd5Q3-c70dLbb_SA0J6IMDvGi9xFO5WzGHiq07GMh0Wd3sGMfQhQJfjGt0Dk5bmZsjutJ8qteKn2z_WpdoqlpkIMbysaq5ulYftqhTZMTZ7JvwywqaH3zB-CppJdRGpuuADY2jGc7Q5uEu0amDbZR1iE-P9tI5PAxJ-v4SvLVxnGbqAE27dVu3QLKfIQfMeYd8c_5swtZ18CtrzUSFoU_8Frjrnm8FOxkrEacAv_CS3IwhPT0Yt1MxtKwgfDPEiW1T-4V02BX7GSyOQ9cjilr0_qhZ2zd9AfRv-7yvqqPoRXNq-hnrr5n4nkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حلقه محاصره تنگ‌تر می‌شود
🔹
روز ششم محرم سال ۶۱ هجری، کربلا بیش از هر زمان دیگری رنگ و بوی یک میدان نبرد به خود گرفته بود. امید به پایان مسالمت‌آمیز ماجرا کم‌رنگ‌تر شده بود و از کوفه پیوسته نیرو و فرمانده به سوی دشت کربلا اعزام می‌شد.
🔹
عبیدالله بن زیاد که…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/443940" target="_blank">📅 07:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443939">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9jaFte7KaWHV00Fjrat4jvqJSvTp0fMxh29amXEgnD-7v5Xx6fvk8XH-DOdTJ2XJSffyY1FsN7h1nyWqHN0Yg1TLWcFuGQBypvfoWcSekSEk_rdWjP-yiA6FNUU05c-wcWQIrEdY4JKBqo4EUJdny7EacXlX6p6KajsfwjI2mxaLou7V406nDDh8YzS54p275O_zut2a7v4evQUe2fxoCdg4CM7Z_jpuemvChzgYgRAjHNAXN_e2wCwEb0pEVnoCLUfL87vj7IIaJ1tRYby7CzTjuc0CqQMt-45QawzWgwrV5ZGZ8AVelbvV227f8HLcpikjsdkzv7mdScJ87LEHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
جدول گروه G جام جهانی پس از تساوی ایران و بلژیک  @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/443939" target="_blank">📅 06:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443938">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/htX4v345lkvfkOJlpVtwuc3In4LLS-N9AHUfLuh25DHw5gtvunjN5_reiPd72O59gjVYJ2fQwWPDDHmLUoOzWJ8DaSJLzA5g3hmLFKaVCf4x7LElQ81yi5755WwOAQ_u1vS9MiYEHoWdwHHR8HT3JgO1gGAfeLWM93bUqqGqczMqDIRliskEaZzgjDKw9bYePvXXIl08ebg4t_Baam_n2h9X3SmDrN6auBzsQvtomn2k2WzwW2q6R4Ys3BaxvZb1FAoERFkZlueE8UXqu3ElpUFGU4SRvxDxWxfns2gjKeFwViJ1GXTT-pZ556qW-_J1m48OR_18b3FXGpP2CMOlFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین برد مصر در تاریخ جام‌جهانی
⚽️
مصر ۳ - ۱ نیوزیلند
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/443938" target="_blank">📅 06:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443937">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e20416fcd9.mp4?token=Vf8LQFL18AG-NHJxR2-CJ5-RIpfp40ft9icQi-aZI26L5L1shd1CE5hnYxpE4TqN7EEl0CBDrG2R06cKOT-zGftYPN4kSAgAVZh_0fXdrNJS7Q0ogoraj-sQ-KPDss1R_ZAXazL_VmwjfnzLPPsNkbSlSwwjqEmYi4-OKGNFOzepADAkOXZfd9eirKgZFOJlxVnKMaFubOOIWxaL7v_krPfDhF1ByM9CUsMsMT8MYeLPLG2pmC3UsviODHB3gyX2yaFkFr6nE7brlyOBLUEJdmBbf0CtWvesQi9cGMSE-gnfA9ZadEkeUmTAwI92lOJUOfzN1nT_szOuh-XXVmxGGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e20416fcd9.mp4?token=Vf8LQFL18AG-NHJxR2-CJ5-RIpfp40ft9icQi-aZI26L5L1shd1CE5hnYxpE4TqN7EEl0CBDrG2R06cKOT-zGftYPN4kSAgAVZh_0fXdrNJS7Q0ogoraj-sQ-KPDss1R_ZAXazL_VmwjfnzLPPsNkbSlSwwjqEmYi4-OKGNFOzepADAkOXZfd9eirKgZFOJlxVnKMaFubOOIWxaL7v_krPfDhF1ByM9CUsMsMT8MYeLPLG2pmC3UsviODHB3gyX2yaFkFr6nE7brlyOBLUEJdmBbf0CtWvesQi9cGMSE-gnfA9ZadEkeUmTAwI92lOJUOfzN1nT_szOuh-XXVmxGGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
احمد زیزو، بازیکن مصری دروازۀ خالی را خراب کرد
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/443937" target="_blank">📅 06:27 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443936">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‌
🔴
وزارت کشور قطر مدعی شد علت انفجار در تاسیسات گازی راس‌لفان، نقص فنی بوده است.  @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/443936" target="_blank">📅 06:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443934">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44ab733207.mp4?token=AntEyxdEcWYsmN0AKatTRcMQPZmLSoZTTbfaEW4rw187hcdi1Dl0f4NeIaSRz_lDOW_y-bTQK37c8oiW841hbDvTGVYj2nQxRCO6_Ctb_EE16Chyg5kbYfxtIcxAIhY4nUwWJoRlY44CtPFcxBCdLIxBawLeEU10X6WBFhh9xvcNFTamDObqEgfiRbcVkoJXHAzLJgYjqDFuu90MBb_iHbMS-8_0nusSuBXfBDP0e9DDedP2waGTmiSMkunFFR1nxo0ZZ_Yt5HxHF8UoWyCONC9cOHSf03F6L_lOT11Q95pWK3AVEKwzFHxaiKnrRZE9q7IwHLG1atsHym7Xkd-ebw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44ab733207.mp4?token=AntEyxdEcWYsmN0AKatTRcMQPZmLSoZTTbfaEW4rw187hcdi1Dl0f4NeIaSRz_lDOW_y-bTQK37c8oiW841hbDvTGVYj2nQxRCO6_Ctb_EE16Chyg5kbYfxtIcxAIhY4nUwWJoRlY44CtPFcxBCdLIxBawLeEU10X6WBFhh9xvcNFTamDObqEgfiRbcVkoJXHAzLJgYjqDFuu90MBb_iHbMS-8_0nusSuBXfBDP0e9DDedP2waGTmiSMkunFFR1nxo0ZZ_Yt5HxHF8UoWyCONC9cOHSf03F6L_lOT11Q95pWK3AVEKwzFHxaiKnrRZE9q7IwHLG1atsHym7Xkd-ebw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تعویضی گل زد
⚽️
ترزگه در دقیقه ۸۲
نیوزیلند ۱ - ۳ مصر
@Sportfars</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/443934" target="_blank">📅 06:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443933">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IR6zUYpEq6GAuw6HHLLGCfbwan_ppfikd6n87UslMF9Pgy25I5qInBrSh7n6uilPokms_3-c0p3OWkr1UtMgtjrnUdtslw2vmspQAWXAghJCVjkHjLk05A75OgtIW-Pz-w9vo2tYDQ1E1Qa395KFN1SPa1SdP6Scksod8pKqAI-CC3HQXqaBgQ2j0bqhP5U67Z7nav1C9S1SJJiBCc0uCExZQM97wxm4P3PTd0mv6axvKy3i7utadcce_BophCngZ1d9QK64EGfXBKv2WYcY4BFCXZxzBm1F3K390JB8uGPnRbunCpOF-BP3bo1Eo_LDvl6c4fBSYwFCZCmOmwQiMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عراقچی: از زمین فوتبال تا میز مذاکره و تا میدان جنگ، هر قدمی که ما برای ایرانیان برمی‌داریم بخشی از یک مبارزه بزرگتر است: دفاع از عزت و افتخار مردم عزیزمان.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/443933" target="_blank">📅 06:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443932">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9459bf3d1e.mp4?token=WrOyRsoBGy-_NZHfgi25ELmVd4BOC8cwPs6qWGUFkzXmhfqDTufJMEqKm6TfnsRpb49SytXQqDliY32dvcGSLyAp1DpVrxSRHBN058IMIMB4BKTkgqQ3GvV4W1FMRtCQijCLRnIboiT_tnbD7BJoGb_gUcrRcwx7dOBnlu__aiqusoWgNaeegIEx3zb6siUVijejJsDZzWo0Yy9sgeDj82_CDTVo4Shik6zV4RmGi63MwUQfKWn2d1qEhi69DG3D_mim9A_c0oWxm_hmrrZPADFRq8zggIYNAE0j5GoTwRR8R3pJRFHbxY8yoUGJTjhsqc6OO0YksXfD9ldkfdi6Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9459bf3d1e.mp4?token=WrOyRsoBGy-_NZHfgi25ELmVd4BOC8cwPs6qWGUFkzXmhfqDTufJMEqKm6TfnsRpb49SytXQqDliY32dvcGSLyAp1DpVrxSRHBN058IMIMB4BKTkgqQ3GvV4W1FMRtCQijCLRnIboiT_tnbD7BJoGb_gUcrRcwx7dOBnlu__aiqusoWgNaeegIEx3zb6siUVijejJsDZzWo0Yy9sgeDj82_CDTVo4Shik6zV4RmGi63MwUQfKWn2d1qEhi69DG3D_mim9A_c0oWxm_hmrrZPADFRq8zggIYNAE0j5GoTwRR8R3pJRFHbxY8yoUGJTjhsqc6OO0YksXfD9ldkfdi6Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تیم ملی فوتبال دقایقی قبل به تیخوانا برگشت
.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/443932" target="_blank">📅 05:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443931">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIhjP9-wCh8f4_iJRGqxHuXASiltr8B935w6nX6o8NmjM6leKZCb1yICDUIj3p4YkiaT6P_c5Z4PWX725Tob17w9Fp6-FslDtfS0fSs1X4BX76FI5BFKScTu98hjAVEBPSfNF5vtayg03JR6Pd7qCS8v2fPVZIHek7AKFVuq8mkqtq6RuVEGpDrELQeeLiBQOnix8dn2bXHXwg4tcmOE9mYt7UvNavwQ5bcLZcgfdT6BvtsIBqPLa-iwlSjJurLgZL8F9rJX80_IFN0LKZ0UAB9fGp6azRNcY1upZj1FEdXzvCIHuKaHQp9Q7scpMHBdvoGueJJBIDkobp5nOpvmtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تشریح نتایج مذاکرات روز گذشته توسط وزیر امور خارجه
🔹
میانجی‌گری خستگی ناپذیر پاکستان و قطر باعث پیشرفت های بزرگی برای پایان دادن به جنگ در لبنان شد.
🔹
همچنین تحریم صادرات نفت و پتروشیمی تعلیق شد، محاصرۀ دریایی برداشته شد، برخی از دارایی‌های مسدود شده آزاد…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/443931" target="_blank">📅 05:08 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443930">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOn1UY8_Bn1wZzOYtu0qFpSdv9z8UK-0lv1Fc3yN3a99dHm033Fjyf3Qgh6JT3xCzbXLN4uwO0kOYHQj-vaYUZKQXkd3M_R6jGv2IC7pmeZ7yHwDVj0ss-aZHvmKNvz1C5fTpZ3QhHjP8s_nIrKAm4aJzJ7rPTsuUEIqXulEsvjXeD-1m9XAC235Zl-huR1H9jDBH9wWgn7hIuTuIQckBUC0sW0bBiZpqD4OOVaqwcVbA0eIxhJa7icNZQvSPn4lj1U_zw7nvEML8lKX-QHuADxXOnqO34k5_v_ilewWv3jMP9SDPRbFZdWV99tha3wCqcHvKGTVg_pnGLCXKtoGKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تشریح نتایج مذاکرات روز گذشته توسط وزیر امور خارجه
🔹
میانجی‌گری خستگی ناپذیر پاکستان و قطر باعث پیشرفت های بزرگی برای پایان دادن به جنگ در لبنان شد.
🔹
همچنین تحریم صادرات نفت و پتروشیمی تعلیق شد، محاصرۀ دریایی برداشته شد، برخی از دارایی‌های مسدود شده آزاد شدند و طرح بزرگ بازسازی و توسعۀ اقتصادی ایران اجرایی شد.
🔸
اولین آزمون واقعی: رفع درگیری‌ها در لبنان
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/443930" target="_blank">📅 05:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443929">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cc09b214d.mp4?token=YldFsYRBpQrURfCoUjKGnAR3fnwCxVkPH6OZAF4KHJzNSrqt1aJhqOkIfSsR7TiJTnKuOhNnPesmyCsHjgBgWs-Q6Jh4zPHR6b8a-NdcUHj8D1EWMlXA3lc3HGL2fKeLC9bJGyQkhachRUnyoz0tlDKcoK2nUBC95kRuPEH9LVsbSxID1A5vVTvLY263KT9Ep2LmLD_cn9fXFuQkdOrpZUsAs5XuSoVuZbyr77PWMfHyuu84bdXOSJNJXzb45M1YcyeSzivE1ZGjxJE4amY-vFpdIl0DubHUUZQTiccv0br-25d8Ki-tnm7y_i6LjKhqKhxJzxvD_SoYCjTIrL9Zfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cc09b214d.mp4?token=YldFsYRBpQrURfCoUjKGnAR3fnwCxVkPH6OZAF4KHJzNSrqt1aJhqOkIfSsR7TiJTnKuOhNnPesmyCsHjgBgWs-Q6Jh4zPHR6b8a-NdcUHj8D1EWMlXA3lc3HGL2fKeLC9bJGyQkhachRUnyoz0tlDKcoK2nUBC95kRuPEH9LVsbSxID1A5vVTvLY263KT9Ep2LmLD_cn9fXFuQkdOrpZUsAs5XuSoVuZbyr77PWMfHyuu84bdXOSJNJXzb45M1YcyeSzivE1ZGjxJE4amY-vFpdIl0DubHUUZQTiccv0br-25d8Ki-tnm7y_i6LjKhqKhxJzxvD_SoYCjTIrL9Zfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بقائی، سخنگوی وزارت خارجه: با حضور میانجی‌ها، سازوکاری برای اطمینان و نظارت بر ادامۀ توقف جنگ در لبنان و تمام جبهه‌ها پیش‌بینی شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/443929" target="_blank">📅 04:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443928">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
بیانیه مشترک قطر و پاکستان در مورد پایان اجلاس بورگن اشتوک
🔹
اولین جلسه مذاکرات سطح بالا تحت چارچوب تفاهم‌نامه اسلام آباد در بورگن اشتوک سوئیس با حضور نمایندگانی از جمهوری اسلامی ایران، ایالات متحده آمریکا و دو طرف میانجی، دولت قطر و جمهوری اسلامی پاکستان، به پایان رسید.
🔹
اجلاس دریاچه لوسرن در فضایی مثبت و سازنده برگزار شد. پیشرفت‌های دلگرم‌کننده‌ای از جمله ایجاد سازوکاری برای مذاکرات فنی بیشتر حاصل شده است.
🔹
بر اساس این تفاهم‌نامه، طرفین با ایجاد یک کمیته عالی رتبه موافقت کرده‌اند که نظارت سیاسی بر میانجیگری را بر عهده خواهد داشت.
🔹
مذاکره‌کنندگان ارشد به طور منظم به کمیته عالی رتبه گزارش می‌دهند و گروه‌های کاری متمرکز بر هسته‌ای، تحریم‌ها و یک گروه نظارت و حل اختلاف را برای اطمینان از اجرای مؤثر تفاهم‌نامه و سایر موارد رهبری می‌کنند.
🔹
کمیته عالی رتبه بر سر نقشه راهی برای دستیابی به توافق نهایی ظرف ۶۰ روز توافق کرده است که زمینه را برای آغاز فوری مذاکرات فنی بیشتر فراهم می‌کند.
🔹
علاوه بر این، یک خط ارتباطی بین طرفین برای مدت ذکر شده در بند ۵ تفاهم‌نامه ایجاد شده است تا از حوادث و سوءتفاهم‌ها با هدف عبور ایمن کشتی‌های تجاری از تنگه هرمز جلوگیری شود.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/443928" target="_blank">📅 04:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443927">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
بقائی: یک متنی را دو میانجی یعنی قطر و پاکستان صادر خواهند کرد. این به‌عنوان سند توافقاتی که در جریان ۱۸ ساعت صورت گرفت معرفی می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/443927" target="_blank">📅 04:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443926">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: زمینه برای آغاز مذاکرات برای توافق نهایی بحث شد. قرار شد گروه‌های فنی به کار خودشان درباره موضوعاتی که لازمه اجرای موثر این یادداشت تفاهم است ادامه دهند.
🔹
در این مرحله کار هیئت مذاکراتی تمام شده است اما تیم‌های فنی کار خودشان را فردا ادامه می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/443926" target="_blank">📅 04:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443925">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: نگاه هیئت ایران این است که باید گریبان طرف مقابل را برای اجرای تعهدات بگیریم.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/443925" target="_blank">📅 04:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443924">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
بقائی: اظهارنظر تهدیدامیز امریکا باعث شد ایران حاضر به ادامه نشست چهارجانبه نباشد
🔹
در زمان نشست چهارجانبه اظهارنظر تهدیدامیز امریکا منتشر شد که باعث شد ایران اعلام بکند در چنین شرایطی حاضر به ادامه نشست چهارجانبه نیست.
🔹
قطر و پاکستان تلاش کردند گفتگوها ادامه پیدا کند و ما گفتیم به صورت چهارجانبه نخواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/443924" target="_blank">📅 04:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443923">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: جنگ در همه جبهه‌ها از جمله لبنان باید خاتمه پیدا کند
🔹
در خصوص باقی بندها که لازمه برای اغاز مذاکرات نهایی است گفتگوهایی انجام شد.
🔹
درباره صدور مجوزهای لازم برای فروش نفت و ازاد سازی دارایی‌های ایران بحث شد و پیشرفت های خوبی صورت گرفت.
🔹
در خصوص عبور ایمن کشتی‌ها از تنگه هرمز قرار شد سازوکاری ترتیب داده شود که مهم است.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/443923" target="_blank">📅 04:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443922">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YxptsQnpRIx_pLN9glObTe_ZpGuwq4nhbmIpA8hB9pfhhef5gWMHSohwwerHexY8Bv3fmsPZQT15NidAzca4kPauwXNHnzwKItMC63P_EOVVZOl0P3r9y4T9uqaT-pULGOO-9kiKPSRTFsUvz72MfPcsX-vVySDlfCOXzBtSDjZ79__5jPyvifCMsYyfXQIQwQrvHXnPAZcBLeY0cnD7p_0xs4jW9BugXEkPiV_tjGKqxHIDanTCs5-XI7LrHM3Lh-imlVmE5bW55cPzpFjFMPOZo9-kE4fP_mCbg19xx0bvhg_Q4XJ3R29tcmOz5dVdiuRhIXUIzeeOMDORmaabaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش فوق‌العاده ظرفیت قطارها برای تشییع رهبر شهید
🔹
مدیرعامل راه‌آهن: صنعت ریلی کشور در آماده‌باش کامل قرار دارد و تمامی ظرفیت‌های ناوگان مسافری، ایستگاه‌ها و نیروهای عملیاتی برای خدمت‌رسانی گسترده به عزاداران بسیج شده‌اند.
🔹
افزایش ظرفیت قطارهای مسافری، راه‌اندازی قطارهای فوق‌العاده، بهره‌گیری از قطارهای بین‌شهری، ریل‌باس‌ها، قطارهای ترن‌ست و تقویت ناوگان حومه‌ای از جمله برنامه‌های راه‌آهن برای پاسخگویی به حجم بالای تقاضای سفر است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/443922" target="_blank">📅 04:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443921">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EC_4NYHVeqEpfI4lXzWKv61YIkLdLn4p-cyCA0jYpVSk3G008nl8ftTU4i2_lUNfJtzFez_6c830iyAgEC7SLGkj9I5-Xx6ZhSVcoUu9rRZqJ2aDgT_tIsSHHDCg-7VRFbiyPFc5XujSWrkDJ6sEbOv6xtdCE8b-Ktd0iUtdegIaHfnDD9VV9pFzEWzuvSwgVk7GqawOC94njJMgFvX0PrXvDf08eY8VDOl2XlBemCbbJGFa2WK-q89irXQNUat_kH20NecbR6Mcw3hyAWyOj8-8uuEk8bZdhekV-CRp9G50Ve-66yYvaTH36ir9q_ifO2XvlKlu-tEOy4nqdthBcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تساوی دور از انتظار اروگوئه مقابل کیپ‌ورد
⚽️
کیپ‌ورد ۲ - ۲ اروگوئه
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/443921" target="_blank">📅 03:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443917">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k0UfCqmLToEd3GfVA_HweS_WQxjAXsTVRYRKzErMkWp50mIXrvdu3y6ikbUXKdd2ska3tgm0r2kd3lzgtut6o3vm9lQmyJEFULQzx-Byhu5bJULBOybWjqrxiN8SNHIewf1-x4fo5m4jjCffIkcacmWXESWwAOSNkJyWyp8j3EhinGL_DYQaJzJl6DXmJtpxqa3eQG4c_y1oYol9jxia6lYaTLQAKEGQ2yyaqTauauL_kzITT_GYS72vPALYThzhxU95WTQfjMqeod9bCKOExkhHV7oMllC5Sy3817zaZfRX_CnoNDdSMJW26n_lLdqDZ_UK7uZ4gLZa9vDqj75DKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j5Yjf8Ilh_p8vEtimpr7y_YPFBuO5Ogba0EXiaRJ-8AC59lyLhe16S8g4IBWinYcZiBBJ1fg1M5MIpuoPRz_xbnQnI8Tt_cniXofrt3_qfzFH2yAAfaHzsmY2gvx8N25_6dQ-Xwy73oJda9oAydj1oW3i-AG2hWM9M5tlaLvVyCp6sVdVyrhT6_bJPWva9VnQ2dsDW5G6H6C2qK-ENTazjzVdd3rerSpj8wfWytKCeLGFUVQuze2s9sSe4KIre1I5-zsgzWGEx_VSapCAx00u4cLbzbtl9F0WR7NdNQY9JQ8cstka-VD8_yC3VPEEo60l94x9eM-izrXLLhDU4KPiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N4-2OCcAd6ZRGMqPFID7RJBkALo8eTkw2efwiJaQHvw1nE1toSl2WPEDM33NVHCt4VSWSgePTzHcFfC7AWL_e7O9_k4WRaBInWNd2QM8AT4EQ8IfVGpSLIn1m8-0rwS5N3fXob_7WmxdWGjARWRa0dwrvwAsc0jNew9LXpYfPj9XFylTdJqM9sINNNWoj7LIV1vtx-ka4zmXFT9TQmrA_a2xUqN8P9ejA9mLh5nLrnnVGMjyC4Z3c6_-IvpyRlGLLhRCXWwWrjDf_aSVTtBaSmu-Xll95FKhWC9iTEpyPyPOLbWO9gpnPvFCw5P4WG0WQS90trvWU94Wf-v0iGznMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wl_RxUj2IJPsPrHM_BjmPl_GIQG9jy9VGmM4tozFoc4nbelrgInV8Jyh4ZEuXG-K4N-zA5VkPhmuZZ4jOxhOptOeaIpGN6B7Eqqw-7L6bnp4q99vpWI0JqSuvdfHTsH1K_-1QSoGwryuWay_a0aNcpR4AhqNIEQmIPJ7Rgtag5p9toKWLFK3ZOo9kYjkAQcWfJGPZy7wZQxTeaMVPuRdT6FkaEyfbf0_zBWW9rzEH28WfPq-LRUeymYRYtoBdXErMS-yP-nLY1ngucuEASteHkVpEjB8H5AwHI4oSo8AYHNZwEoxeutI6SMEzQERIrSRwHRJMP3WzYHBIBZNfbNJHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دنیا به افتخار ایران کلاه از سر برداشت
🔹
واکنش تماشایی بیرانوند برابر بلژیک و نمایش دلاورانۀ تیم ملی در جام‌جهانی واکنش‌های زیادی به‌همراه داشته است.
🔹
خبرنگاران و کاربران شبکه‌های اجتماعی به نمایش شجاعانۀ بازیکنان تیم ملی ایران مقابل بلژیک در ورزشگاه سوفای لس‌آنجلس واکنش نشان دادند و تیم ملی را تحسین کردند.
🔗
شرح کامل گزارش، و واکنش‌های جالب کاربران شبکه‌های اجتماعی را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/443917" target="_blank">📅 03:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443916">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9ut20Let3-VSkPfzKN35q4UtCC86TqZiNFA-DpRqC2z63FDf1NPC5pWn3lNh-SQRsorojzBURxWOXY9V1Y0vgoM-dcCGdv4y5uv4YLW8kLpFfq9sTZ-vV0tHZn_wGWgzm3-Y4FrXRkv9MU7ViaBrQAAhBN3NwNM3tTEMSu2zFfyMrjnAKSs_d-pJk0g9z0CKF_CKcEbSKTFi7Z80mwy-D65IXsemq83BCUYoGed0bXO4NKZRHRylyU0CvhwO6YItxjxSVWz2tenzg1mGbf1YLPAjEGtVC26PrizXUaDrOWpR8KUTQ2DzpOetBsYx8rKwh9g51oY0M-khtPShFYZhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هراس ارتش رژیم صهیونیستی از شکار فرماندهانش به‌دست حزب‌الله
🔹
رسانۀ عبری واللا به نقل از فرماندهان ارتش رژیم صهیونیستی نوشت: حزب‌الله بار دیگر سامانۀ رصد و جمع‌آوری اطلاعات امنیتی در مقابل «خط زرد» در جنوب لبنان ایجاد کرده و تمرکز خود را بر هدف قرار دادن فرماندهان ارشد میدانی اسرائیل گذاشته است.
🔹
نمی‌توان این واقعیت را نادیده گرفت که فرماندۀ پیشین تیپ ۴۰۱ بر اثر حملۀ هوایی با پهپاد به‌شدت زخمی شد، معاون فرماندۀ لشکر ۳۶ با یک بمب کنار جاده‌ای هدف قرار گرفت و زخمی شد، و فرماندۀ گردان ۵۲ در حملۀ هوایی با پهپاد کشته شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/443916" target="_blank">📅 03:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443915">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">می‌توانستیم پیروز شویم
قلعه‌نویی: برای برد ۳۰ سانت کم آوردیم
🔹
قلعه‌نویی در نشست‌خبری بعد از بازی با بلژیک: ما ۶ ماه در شرایط جنگ بودیم، لیگ نداشتیم، یک‌بار و در یک فیفا دی حدود ۴۰ ساعت در مسیر بودیم تا وارد کشور دیگری شویم. ما شرایطی را پشت‌سر گذاشتیم که همه دنیا از آن خبر دارند؛ بحث ویزاها، تعطیلی لیگ داخلی به خاطر جنگ، لغو شدن بسیاری از بازی‌های دوستانه و مشکلاتی که در مسیر آماده‌سازی داشتیم. بعضی از بازیکنان ما لژیونر بودند و برخی هم لیگ تعطیل شده بود و بازیکنان بازی نکرده بودند. فکر می‌کنم در بدترین شرایط ممکن وارد جام جهانی شدیم و دوست دارم همه دنیا این را بدانند.
🔹
در بازی بلژیک هم ما می‌توانستیم ببریم و هم آن‌ها. ما هم گل زدیم و هم دو موقعیت صددرصد داشتیم که کورتوا، دروازه‌بان بلژیک به شکل استثنایی مهار کرد. با اینکه شانس برد داشتیم، این نتیجه هم دستاورد خوبی است که دو بازی جام جهانی را شکست نخورده‌ایم، مخصوصاً با شرایطی که توضیح دادم.
🔹
علیرضا بیرانوند یکی از پرافتخارترین دروازه‌بان‌های تاریخ فوتبال ایران است. امروز یکی از روزهای خوب او بود. از همه بازیکنان و به‌ویژه علیرضا تشکر می‌کنم. او تمرکز لازم را داشت و توانست یک امتیاز بسیار خوبی برای ما بیاورد، هرچند ما می‌توانستیم ۳ امتیاز را هم بگیریم.
🔹
فکر می‌کنم تمام کسانی که بازی را دیدند، لذت بردند. از همه ایرانی‌هایی که با نگرش‌ها و باورهای مختلف در ورزشگاه بودند، ایران را تشویق کردند و به تیم انرژی دادند، تشکر می‌کنم.
🔹
ما فقط تا فردا می‌توانیم از این نتیجه خوشحال باشیم و بعد باید به فکر بازی مصر باشیم. مصر تیم بسیار بزرگی است و فوتبال خوب و با برنامه‌ای بازی می‌کند. هدف اول ما صعود است و ان‌شاءالله بعد از آن برای مراحل بعد برنامه‌ریزی می‌کنیم.
🔹
فکر می‌کنم طارمی کمتر از ۳۰ سانتی‌متر در آفساید بود. ما برای خودمان برنامه خوبی داشتیم، بلژیک تیم بسیار بزرگی است و در رنکینگ جهانی جایگاه بالایی دارد. با این شرایط، فکر می‌کنم کار بزرگی انجام دادیم. هم آنها شانس برد داشتند و شاید حتی بلژیک شانس بیشتری برای پیروزی داشت.
@Sportfars</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/443915" target="_blank">📅 02:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443914">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MiGMvBSSZAT4U7qs11EpmDwGoJXn0k1_v6m5VTn6nzjLTUyzBYHVOL9j00VF3fEyEH9x4mLzX_Txftvw9BP8usDwQaWfr4B2N3rIOW5JqBa8jWl4aQBd168m3CLrDif8BH-6BYy2H13UsktcGEPq5PposlQMrM-nCB1ASX796iCYdIFHRCa8SQkBS8PAYGKvn2rT73Ai1y-5q2pXa9iKBXs42rGh3HH-tTzzgWlpxBXaupJgFWhVqBG_TbZ2jwQTxduJ2icncWWV_6AHzvIwbmhwormldWGpYHz4PInVglfxahOqWIT2zAIOjKlVab4Cp4IXVtWmSIVg_UgNzz3EIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سرلشکر رضایی: آمریکا باید پاسخگوی تجاوزات رژیم صهیونیستی در لبنان باشد
🔹
ایالات متحده بر اساس تفاهم با جمهوری اسلامی ایران، مسئول تجاوزات و اقدامات تنش‌زای رژیم صهیونیستی در لبنان است و باید پاسخگو باشد.
🔹
در صورت تهدید علیه ایران، آمریکایی‌ها را پاسخگو می‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/443914" target="_blank">📅 02:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443909">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l_GbTr3p9TZw3aKj-sg9DIp0VJbbpP7g853w2h4l3sryuMbZyz7cmUGRqT01WiYgRCEsVLsXyOw0AJVO-Vv2jAgNd1CcnNR1u5tVbdC07s-5Yl8gXByXksTGrr-LxF3WW5SItDf0kgM_WY10rTP4MC0nqgBddwZfFerqa7LVnie6cuZ_kxFu9aeJdYbER10ATGtH3SllndekI02zi7ZJhWq9wzuZlFtwRmbvxfmm5viHLC0QKZGXw-rfdleknUFBl5MPAfpZgabKBBv4F_L_cKg0ZGFcVnxwEbNiNMjF2NmCSSDagKGL5lA8d8EOBGFQfSboQy4WW9BJ_fXblgHvNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ptAHQ1dw3RQK8b1MSy5lzBNiWhZ1cOm8zY3BSRJPXasWr6uAgBmkTU_ry5vu4F_djaxDcwvNCMKB9nXt2gVVwS3mxSLk7CKTzQX57U2izUrtPCcAlZpA2eCF5YO3PKlpMTeUSG6eVsy7IMKL6HI3888V3QaubEWDDV2tcKIg-FQ47QLC-9N--6p4JYbazKM6XI8GJ6DBmmZdx9KxwOZNh8XE2j0OmbcHIvY5lE97hMrBDq0-Yc9BWD-gEyA0UcGUnsniPyg8uQZyZ8jXzvdanzJBwgARuLmuu5-hrRjThuPsetYO9lbJxuVWShbOfeeINl_rCLJ4xnrPX2Bbrur6Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pFNlwLVe1sq0RKm76lcLB60zlITSTP9-L0um1oiD15u9LauoQjw4AJVrWb95jyqGelMu7ucO1BhW1wuNqdVxWVUJb0wfhyRGsS6qbnrm6AGx-79B5spAeAhd1YUxzLWxgfAXTtGzaOU2YGKz5E3qTOszRR5PKENDnpd46wquy3ZUZDOwzpfmT2u59vLLSzTXwwJr0wxSw0xgYucCynIFGX1Lk32nS8PTG9nTeykeKc3LtXpp7XpeN-Am-TGifLcXkittZh7VTmb0x02-Q62AYj_HoJI6A93GOMTbX4bJ3xNzAQ8hElHhPHr6ZvOXw9SIFrOvXN5L04ZO-WHdkcwfWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Crb6uy1-yLlEAxo-OvzdR2UGf7j3xxCpfV9owvwVfihjP-MM7L2tBR5AzNkH2YciOKyO5NTqtHy1vPNGiwfq-zy95K9h0U0yDvgmOqERc7Ocm3o6wFDLOqYUmc33yid13DzE-Yn38oKyG0sZzcNmKA9OXJzCr0UseI-Af_w3gctIT9lZJ-iBWrSMyM02KA83urYUoR6vnifsmpPdztr43Zwnd0_qil8_WS99X6EMj-cB0Zc1UBqfJgAva-0lU6fpZrI9cTvWiIf66bzPoit-SD9c2RrKJqOA8mz8rkIFbSL4s7BZPDwjyjmj9I3zwktrnLxLE6fAcmSembe1Mm4Omw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F6xa8Rz1HEWnNbVxnTySI5TvlHXOlmnWA2AR2KtIVUHoFPZ9AiHRKThI4gUhi_L9n0nowlMrJOuKpB10sUP6YyP2MksWx24mIWq1uaf0ABZCeQSas9jxpU-UXKdK1LvS8L4ntSeQJ5FkVepKWbNtVUaZyrqr1OUMU8hi0ywu1KdonpP4T9avEPVDNyqL-nAu8GSSB306fDWwpjxxHe-DvMNCidotee0XfqfBCBIIEDBE-WQCj_GEBhwYuNpBXKEpKl1L7JGX5YBFpSk6TpeFj2vN0DFYLp6rtzkpa3cHXMrRUynPAaj6qi1wfKBq9dSgKa53bZA7Co_So70aIZ35Xg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | دوشنبه ۱ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/443909" target="_blank">📅 02:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443899">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gWV8rAWJsnNeKXcQHiUIvbACcea2vnP-PZuySA4cyUVaMNpyfo3r1gn2JkhTsvcAuLOgkJ73mLfGWMyuJSmalI3xoYTX50T-gVs5Ct82w5AXtzW0Y2VWpNg6Dkk6YYpvsGY9Ql0YwzsxBN-FAURp5j98B22Wle48xtDkvIpgAO6Jiu8ZSVebyR0AcbBcKq-7e2yp1Qgq_Hlr6hs0ess1501YW_HXSfq4j4hu0LB06_nKM14uJn_jDSzM5NJCGh354zIFyg7dQDiEE5Waf0CGJxxK78Or-aadD7Uo_0hWHdF3I0jz-MiYNvzwFWNBP8WWuOEsSuv_2BV9u4vWGCM3JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PdsHVLXlTaG5CjQn_gJHFF5d70fohMEDbF5AxaDEwPdlmhnYvWhkAKItthUoeAZMQwo_h_O2hyQ43Btm3geB0FzhlhizgcB83b3jCCK_g5ihLTmSRLFBojRIVmts4KPEVvjy7FG2e2CriKrkBr-GQWr31xii5-9sP8Jq1CiFdfFCukNvz1S-r83McHIXCNR-rexfObysx2CfUMOTWMZdiQ0r-_ylnOYGG1zWhrjjBRGzG_CQFIBHV5_1kAYBkPwgg51yaS-9TqaQGeAmkGhSEgnvgH0dfb8cUSDDbYOrPoiAqUIGzLtXrXxqe-gfuQx9WQWD0pQsbhdRYtbRNxYlSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BeB2I1OpXCyk2WMuxJxJII4e47klnWDiFzTGbvVB_9_VBZpogpX-sR86Ru8_kkvoW3vu1iGz7DWO5dUcfFWS-LoClQQn9Io6q7ofVZ_Wld19AZdZgwTiGnGB_dkP2Y1WgRcmXUHnimH0mcg3JQkcrZoI5jCuQ_ZWgv0Vw1T6rT8tk3NX7QxznzvxS13-B2qqvDT8IR1lJDbVZdXddXDLIpCWnh9MVt1DqdllIbEphyAWXwFdYAzyZpuEUkUjc6AYxvbYMCPbvvxnxB4fmx3vj8QNEv8b2eCOKT9qHgU50symKiuX22MK8vfU9a7ILXf0SP-QOAT92yQBY5HDoW-AJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZWWNDK0yERJNQ9vJl4NeDNzncogjFQfXf8hwYi4Qumc1KaKgdvtAFEEGomhq_xmznvwaGUxGZ6IheNXbWcpG2dxaQFmnRDQqP14tMYaicCdC0UZ3H7j2T791CAjt_E06_dAIffIZEnic-LbQCq0nCvtoo8b-YTeDPwlif7O-MPzNWAZdHe4e-D95xYcZ-hXnjytC0cV6AP-3N4K5Dto4SPbA6VRHZZa9RogkpLQ1_NB-GPG_R83rWURFkA9ccI-gHAkbEbft1AJrU6qfvZm_Jz5KJfHkMnOrdPGdX7gK8IbBEB4jcQUHtMFLA1LiYKBjvjP7gcd9NCN7eNiRTljkjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MbcFDeTAEfKubmXi4Xbohgj_qT2RyIQRRt20qCZzIaMhDvr2NTyG4cHPWnQTxCdAGNZ0B2i6hxcdOAcTedtJ0-2M-S2FL2p_7MumOxpyMF9cfJsJAjgjQ7C6l8WP832rM-3f7CJNQnN22W4rn00YZunlZpTIHDLLQ-JLPgfN_mdRct1OyUZJdsG6BV5RMhBOCLYG9Z1lFejj1yTy1JOPJE8-1JT5KXjTuoVbun8c_OUGVKpDOyOBGISxHVY7cVQDynwmjZArE7IOAblkOddq75Ojh_N83S15WahArdAjkUapudPSwjEhi1VhooG0I-IdAQDsIAePJ0LTCU4XESSLTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MoGbQtsUCy7hASMHJgSuZ32tp_MWwlsAT2qvd9cp7LIVCgpDteVRsaLRJNfWnN7ORC8z2O0JkU_rRVav3CK44wTEh1gP0vpSXrbWEM2mF4DNGwtqquhglH1jZA-2aBEpoK4dweHxdCRg0zCn-U6XtNnrvKBcQZ6LaeE_yQQb56SiHuq1y80ZSlPBZbThD7azy-Z4O9MAuTKX15nodCN_NxAsVycLsxCHMduDSBDleqRSypLNZTgXleCfKofSG950KmoN958q-fd_hZE5p3ItqwlPZZO191hnoC8x6NVR-PoH3xWp22wddGnRhppLEs893x0I-o3nYorf2VYnwHl1_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PP99d0YM73KNWOXAzxA7YX5t9OFNv7otHKTS0NVt0ZpLkBAxjM3lnuG54m1QC6XNKCtusWbjqfMM3WiU5yhW0f0pFDG6xt-8G6eAc8wdRkGFJH0BX52WDvIGNwtttqu17NT28UDGZx6QoJL9USY1wxDv_Unyq_AzaMFMWYtHat2YxC2D0_Sb1c7UL6ZLMK_hnSqILuNVP_bye56hcLn6FujAqbAXILyBLawoXIV8IlK_kUJmAw-Tg3w-9xKv4ycChodCG7eCG8Dj3uTgpNLrsXLUuChqmZ0Kzj8PZWSo5uTHGv9EEWpPokjYkw5rBUqcEH4XXINU1kN8OOyoxvjEGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uBdGdyZnPohSpPR0i4ji1FrCS780AWgGIf9Xa6uMhl-7MimqA9xjGGzD_adtlg1hgotgdcAVb2NIY7n-5SC5RKyMAjNmKELwJYbbJB6ZVhe_07oAVERWjkCzsYsKh6O3rHXzeGvxSOXA5e1cFv88WBJsPBh50r9wSlaAqJiHxyBGcDtwDOs5kozwgMtn-n3Qe6iNu1DZTfxcmcFaJe1pe-yqzscii07IbXE972uaPO0oKfk2aoV31L72UQl_xoB7uZ5OKDf4xpkDRx5cX4VFunFv-U_kyiHHnPOZgCXiLupMJicHo3dQimNkiwiLXKWZJPVJEX8hY5UKByNCko0oQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AsjoYibrQKm6vDx4AQQ4ws9afFK39aznEAq4qeiRD54YAPCyQ0seGh9JxmDFy-oPhXrCv7v0CezEiWzAB0yuMTbmd9KuKCR25jEiWbkEmZqlpQfYDPiht-rLlYH3ntQ9QtccXG4J9JwZTDH-tJ8up5ezItKnTyYPpu3h_NlQ3a4UA_XvifmexbrBITNt9t6W1CDDTep0vZdylPAlzdyl3k58wJQcfWR05YdcO-sCc1oKJwQUtT6Qbl6xqN9x7RLOgdEX_kJ1njWo1_bbB1bgDMg1OuOgxo1OXNqF31MTFP0uBBS_pxHDL0qgOGLJvYMc9zGwnq2CFro-2eyii1SuAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TsxPG2wgbLIEU94UD4VBcfAVGjnWl1LrqlTK8kV1WJiq-auhCHMTqfM5J5rQN8QgG_QHb_ZE29M6Ua3XZb27acZSuLZ30VdMboUTsoCC23niN1hzyXFIYksA1deIIP2R4nUmYJaT7RRhHCZhlIlhaWhM0LjMbIzoelPC36UYLY-ri1_548M8GPc3O4sHrzNoa5nCPOx9jOGoXwz7BzEFK8iaLnw3Vl7VcplQSCeW2yhFL5F8xm_4_W4DnTEKKkg9cTgKkiO8sUtCuPYxwg5o6krtRTRNRSiKMhq4U_IlNMmj5PFu21P3ozMiY9JM-HcoikpajCoMr5TjZcVAZFZfLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/443899" target="_blank">📅 02:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443898">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTW9xOzy9kXPceQ5rJ2DVJRn91BIIUvrnT1kTPYu1cZy4bOB0KFIuWdW4tVDNYPaL6aEeX67rVZqgG6AmXELpIFTAPr-WTexvYalEgxgUScxMN9EB0ICt5fDDQsfqkKZjoR9fyiarjcFOibuUxTljFImY8j6SUxy93OVvYnppz_vfE2qiP8yTMk3qezBJxLwiI9Lu2JM9e5cz0osKOE7fIFxdVy9lixTtugCKqOhz0ZIh8AZihSiDh-jvvEpeR24_lYURCh5g2egANfhfThEvkAZgzSR5RXqduz2uR6jZV65LDuGP7oMTlw3tzSNqmG3uhxNZlC5a0b7epLFZS2vUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجولانی از ترس حزب‌الله به ترامپ پاسخ منفی داد
🔹
الجولانی در توجیه ترس خود از رویارویی با حزب‌الله تلاش کرد سخنان ترامپ را به گونه دیگری تفسیر کند؛ وی مدعی شد که ترامپ از آنچه در لبنان در حال رخ دادن است ابراز نارضایتی کرد و درباره نقش سوریه در یافتن یک راه‌حل امن و بدون تنش صحبت کرد، اما این اظهارات به‌اشتباه این‌گونه برداشت شد که گویا سوریه قرار است فردا صبح وارد لبنان شود.
🔹
وی تصریح کرد: من نمی‌خواهم سوریه مداخله منفی در لبنان داشته باشد و ما به دنبال راه‌حل‌های اقتصادی هستیم، نه نظامی.
🔹
سرکرده شورشیان سوری عنوان کرد که سوریه به لبنان نخواهد رفت و به ترامپ گفته راهکارهای دیگری غیر از جنگ و مقابله با حزب‌الله وجود دارد.
🔹
الجولانی گفت که می‌توان بر سوریه برای یک راه‌حل مثبت تکیه کرد؛ از طریق تقویت حمایت از دولت لبنان، تقویت نهادهای رسمی، و ایجاد پیوند و ارتباط میان نیروهای لبنانی از جمله حزب‌الله، زیرا راه‌حل‌های جزئی و ناقص مشکلات بزرگی ایجاد می‌کنند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/443898" target="_blank">📅 02:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443897">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">کتاب آه</div>
  <div class="tg-doc-extra">قسمت ۷</div>
</div>
<a href="https://t.me/farsna/443897" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قسمت ۶ – کتاب آه</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/443897" target="_blank">📅 02:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443896">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7gq8PYonEwa-dDMrq7S8vBPQMytLG_lNapAUO1rRODGndDr0wDfVEhKFVKo23AWDd2AhOEqkiSd5pvqA7Uhzu-F2Ogo3cGEq9qGzqOfEs9hslLxFFP1aV0_X3ssLjO9hJEKNMDCcj3wMtv8xMfWzR3cEy8JOZRvoZUT2lA0zE5Es330_hRANrdZ6kvsG3AhmH9_onXiUDldsm5vmSlZWvuyywfHGoVVrmdi0ZPo6oqlXa4bsFVW_1mPmBXad2jfHafFI3lltXvLujK_RrxSvn8PK1GOyF205wYvXeZAFPniU5R9Ab-zz2CU0JAhes2efpXEjz2uEHViKPE8XUxlRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادر علیرضا بیرانوند: خدا را شاکرم پسرم سرباز ایران است
🔹
مادر علیرضا بیرانوند، دروازه‌بان تیم ملی در گفت‌وگو با فارس: علیرضا در مقابل بلژیک جانانه از دروازه تیم ملی محافظت کرد و اجازه نداد دروازه ایران باز شود.
🔹
این موفقیت تنها متعلق به او نیست؛ همه بازیکنان تیم ملی باغیرت، همدلی و تلاش مثال‌زدنی بازی کردند و بار دیگر نام ایران را در سطح جهان مطرح کردند.
🔹
مطمئن باشید دعای مادران ایرانی بدرقه راه سربازان عرصه ورزش هست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/443896" target="_blank">📅 01:43 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
