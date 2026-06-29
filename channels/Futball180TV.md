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
<img src="https://cdn5.telesco.pe/file/Uo1KV1i3JQ99jogJx65kuC8P7tIK5U3iCG10r0xX-QB0oaC7QHtPQ6zw6THi-ra7gZIlEKFDK7DsbD1YJGzlcd64BZPVzNqNuzZkO44OdYSyZyKn-cbC0bBjUb4tUIBRiob9r411c-AsYJ_bQpQ5dbEr0ygtLULoAYPAz7EHxCKqCqc-mkQmRLx-h0A9Aa4EoQoTYnZsKnXU71WiygkawXfwTpFF5tZJ6zc9GRk42XJWpuFSkrGrYBnVaLU6w566eGPKZpi3KcFsuWa0XkTJULeAZF55dUU5fcFakpdlU8cgdV-8GvzDy-kxo1JdMadfCduQJgXvGoLvd7CrFPctOA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 684K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 00:35:10</div>
<hr>

<div class="tg-post" id="msg-96902">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d25973fec.mp4?token=uNSCIKPPSmAlTu6So-kFs9BIBXhQQrje5glkulMH6cdnk_TPHTOXk75MF2PQxB6z5KaRZf3oIWfLc0A4K4jgD519ghwQTIdjbC0QygYcwdG0OVC6Mf-i205QqpLN72JcThbDW7W9j-qkGzus9m01Ij9TevV6RiYlNRTrbkBZ5V4vGgxcwur4odeUtetiu4pD47HEcDRY8IiBm4Ad_EfJJnXyM3kUXNuniBShquAlk99pU5Rq2ueusnO38YYR1jd9M91YbA6TouxYLLAQDbPSQJ06NsSDSUr712EY10tKrpBsCg9Yjnb7oTkhbp4BaPQDQ1DcQXPhWuB3biY0Jc6KIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d25973fec.mp4?token=uNSCIKPPSmAlTu6So-kFs9BIBXhQQrje5glkulMH6cdnk_TPHTOXk75MF2PQxB6z5KaRZf3oIWfLc0A4K4jgD519ghwQTIdjbC0QygYcwdG0OVC6Mf-i205QqpLN72JcThbDW7W9j-qkGzus9m01Ij9TevV6RiYlNRTrbkBZ5V4vGgxcwur4odeUtetiu4pD47HEcDRY8IiBm4Ad_EfJJnXyM3kUXNuniBShquAlk99pU5Rq2ueusnO38YYR1jd9M91YbA6TouxYLLAQDbPSQJ06NsSDSUr712EY10tKrpBsCg9Yjnb7oTkhbp4BaPQDQ1DcQXPhWuB3biY0Jc6KIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منِ هشت ساله وقتی برای هایدریشن برک میرفتم خونه ولی دیگه مامانم نمیذاشت برگردم کوچه برای ادامه دیدار حساس با منتخب کوچه پایینی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/Futball180TV/96902" target="_blank">📅 00:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96901">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بازی تو این ۲۵ دقیقه هیچی نداشته</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/Futball180TV/96901" target="_blank">📅 00:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96900">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BN0-_KFZWStEdxbEG6MkBaxjk8dnWVUP535RQA6D7Ia4ILA5zNhAVpxtNeRlXC6EA1-H4Rn8mTFwqg1F2G_DWxEabRedLAgGbHGUn7PKfuYIB_FeMKXAiAPUwW_6P3q6LHzJyrU_KaqB0-xmePfZv7RnaDN6IZ_lD7h48gqdX-jqTGcNhF2OeLUV_4YamZLPFMjUKGgAysQW4ZURii7fz64pWfALqIYnX29mR6YsTn_re-ClGcLmkVJbWXA4cEeaTxIRaPxIprUQF5Qd7FwvaFBjicfrprGE691CHfn4oMVBthJda7FwNUo9OzewXIPunvDqJAif1iQRAmgtd5sVpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بجامونده از برزیل - ژاپن و انگشت کردن یک هوادار ژاپنی
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/Futball180TV/96900" target="_blank">📅 00:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96899">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fuyrqa640oYSXPONF26UX58RiXAOtl25DIM_wBhLn-89I-Lu3HvE8jD-wAgFT0q_OQfixfmmsbiARJr2UPvFMQmiejBw_dd2_0SP_mCR1Ff4GV1R1YyOoDiW0eFoTjGQXAK-2ERLsB-cOfdtX3Hrh0HELQirZKC2Ls9UGOHB2mx1IDemFTMIfPOcQ6h29QFo45SlKmKJy8tI0VBOz21Rz0r2_rbuGpCCEVw-OWUG01ozjYaCnWjJ2BeCxYrUy3d1J-8UqXKy2eck0KS4RSThO8-ApzLzV7i9Nh82-HXXyoukLyfjfN8V4roLD5YgzFMkBIKHTAls_wxruEc1vPn78g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو: روبرت لواندوفسکی به شیکاگو فایر آمریکا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/Futball180TV/96899" target="_blank">📅 00:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96898">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">شروع بازی آلمان و پاراگوئه</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/Futball180TV/96898" target="_blank">📅 00:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96896">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c7XugRdlZad0D6Pmgr10_ka7dSb3kLpdM2T54gcEU7TFOAm3rS00saBOLRAaAeb3z_H9gvRpiDN4HfwXC7nioQSoFZdeq_d_YupO4ZLC2VzMaI6Burp9fZu0kAlJ_7VTrQmaZehI-5WEK_TTtTvyI_p1Jwust9kjbhcMcmp4Mg1oi1gBZs_3tgc_-lKjoxlpC6hFrDZMmf1sLDoW5aDjv4IL5gZ81C9S3hgBuPT5leNfioSJVvSoV2ku1UjwcD_way6sHWNrtaM9y5YTIfpEAGbAXpl_tYemz-wwyCfQlhq8vZi-qNh87-xW811KgdVLkOREFBnn34B31lyl2EZ6uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JQ9kXEpZ987Nlfy6EH1KiVWLTUm7_WUlM-y15Lq9gbXCUvRQfVIAz41xy0sFL-MNzNaiCrA2r_0r-HWFWXqzElcoY8dIC2re1a-n9BFvTQxHZJ_eeCuIlnQCHG_WaCsN5_qZZDTvglR_S2FccIH8o7PQWrnE1zyxXe-X-o8l8428K4SLCNF-Xpp9Mis8xB0PaoGaDD2rVjF2Xeq2MmxmhGD9hCt63zs1JmjuvLQM0NxfOrVtgz2dd4K6TRyXY4jstR3vJFL8k9e-tmYTnnROJt-hPP3CTjk2FuVD06xT8hKeuFniiKbR4GdQzqvt9Wz9dw5ZR0iEAjvzgX8oQgwzHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇯🇵
بازیکنا و سرمربی ژاپن بدین شکل از هواداراشون عذرخواهی کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/96896" target="_blank">📅 23:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96895">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLwrMm61yPU4eiNLChD72D9GkDOxL39gzaeY9epk9G3E5hB_gbd0pZVQ_ejHq-9pgt5nYN0SWNtLkarjn-g-_okMEthMNVJMVW2gr1fzX3Ib_zRhwWUud-BK_PFXm7knzZGh1xobnVbuldnrpgVi-SfWu6w_I4nsfLokNWqYZZjnSq1GgK6Z1nnP1jVd625gHJ1EFsormS-4C3v4xSXSYxFX62a2J9mkSNKmCBBJ5IODiDQy6o__r182b95CldLEKiMoQI24jASxSZ6W6JFDr4YnbxzjRbxPUWwv5IvFBJsZJ32s7n71vbdTOAqUSGn9mzAZcQwyT06I8P0LFIAnlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
#فوووووری
فابریزیو رومانو
:
❌
بارسلونا هیچ پیشنهاد رسمی برای جذب هری کین ارائه نکرده…. باشگاه در حال مذاکره با هری کین نیست و روی این انتقال نیز کار نمی‌کند. تنها اتفاقی که چند روز پیش رخ داد، استعلام بارسلونا درباره وضعیت این بازیکن بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/96895" target="_blank">📅 23:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96894">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMyOpvtAdjeEKGVBOJ7pjkNViPZxnSv0wr4pIz2ehwcCbml1mnPksbQ9Qw1ue6W7SzIVVxkHyKb-cr_UhLM_PgwmFYJtyDS4xlSlEU8GvFbXV-RZN4tnYFP0jg04vo2xIJv9cH4pI-lz02iykTA5YzNEcx1vsSDjLZUFA1uPrSmvMzuFWmpFcMgbyAbJHxg1VJzf_O4JjLl-Nv4hxQ2sv9raABuVmaDSMM1U-7M5QtlZJ29ZWY-09OGdzWH6pfyUxph4H373Wf3XkMmsFOL2AmJ3Vdzp3G8ZSB2JpaYPdQwGAJbhjJ-q95wpWD-tSOrHm8hXnCuqS79Gf7w65-J8xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فووووری
؛ استون‌ویلا قیمت مورگان راجرز را ۱۵۰ میلیپن پوند
تعیین کرد!
💰
🇬🇧
آرسنال و چلسی به او علاقه‌مند هستند.
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/96894" target="_blank">📅 23:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96893">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9V1YJtrb0kw3DTny1Nqplf_G7_VlQWAN1AtEUYXISdBBkUskDN7zIGQ6jK8UkoyAOFTEU5E5JO84wfn9jPK1hMSa2J2tGNhTRGJCg76kEN1Tqg8_3HH9IuRQVpoh_G_0QXlipq7LBAdqhIOwsvV7XwTIv2N-Q8ZFUYvks3TrlKC3_13qeazQcltt-_wndQB0sw0fxDbinufHOxtngSFVuWL0k9CjiVHeGZsk6PUw8fZeTqK3NCbLZIPtwEXfpucfD_DZNdwnxplN5NlDwPPyHYexSJ8u7YBpQMgUTIT3QBZkfdT7bhM5O5SoygmQtU2J0NrYeBobxC1YDyuAVLt8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
چرا نیمار وارد زمین نشد؟
‏
🚨
🚨
🎙️
آنچلوتی :
🇧🇷
"من نیمار را برای وقت‌های اضافه نگه داشتم. با او صحبت کردم، و اگر مساوی نمی‌شدیم، او در دقیقه ۶۰ یا ۶۵ وارد می‌شد. اما ما مساوی کردیم و من نمی‌خواستم شکل تیم را تغییر دهم چون کنترل بازی را داشتیم".
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/96893" target="_blank">📅 23:07 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96892">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
🏆
برنامه مسابقات مرحله‌یک‌شانزدهم
🇨🇦
کانادا
😃
-
😏
آفریقای جنوبی
🇿🇦
🇧🇷
برزیل
😀
-
😃
ژاپن
🇯🇵
🇩🇪
آلمان
🆚
پاراگوئه
🇵🇾
سه‌شنبه ۹ تیر ساعت 00:00 بامداد
🇲🇦
مراکش
🆚
هلند
🇳🇱
سه‌شنبه ۹ تیر ساعت 04:30 بامداد
🇳🇴
نروژ
🆚
ساحل‌عاج
🇨🇮
سه‌شنبه ۹ تیر ساعت 20:30
🇫🇷
فرانسه
🆚
سوئد
🇸🇪
چهارشنبه ۱۰ تیر ساعت 00:30
🇲🇽
مکزیک
🆚
اکوادور
🇪🇨
چهارشنبه ۱۰ تیر ساعت 04:30
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
کنگو
🇨🇩
چهارشنبه ۱۰ تیر ساعت 19:30
🇧🇪
بلژیک
🆚
سنگال
🇸🇳
چهارشنبه ۱۰ تیر ساعت 23:30
🇺🇸
آمریکا
🆚
بوسنی
🇧🇦
پنجشنبه ۱۱ تیر ساعت 03:30 بامداد
🇪🇸
اسپانیا
🆚
اتریش
🇦🇹
پنجشنبه ۱۱ تیر ساعت 22:30
🇭🇷
کرواسی
🆚
پرتغال
🇵🇹
جمعه ۱۲ تیر ساعت 02:30 بامداد
🇨🇭
سوئیس
🆚
الجزایر
🇩🇿
جمعه ۱۲ تیر ساعت 06:30
🇪🇬
مصر
🆚
استرالیا
🇦🇺
جمعه ۱۲ تیر ساعت 21:30
🇦🇷
آرژانتین
🆚
کیپ‌ورد
🇨🇻
شنبه ۱۳ تیر ساعت 01:30 بامداد
🇨🇴
کلمبیا - غنا
🇬🇭
شنبه ۱۳ تیر ساعت 05:00
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/Futball180TV/96892" target="_blank">📅 23:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96891">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5-iKPZ7TwJwM2C5Ft-RzAOlWdx4wvsbOz6pcEQA1hQeFYYszkUDlWaDC07SDPsxiJQUJIkjFVWrj4mND-WEZa2PTjZKOeU9sk_SgG5RCRiUcXHaQ_5WQ4DRMJ6ssG1uYqzZMcYplZxFPyoMC3YY2hkzvj6o1uFMr2CiPTjOm6x1R5S0hqmrW_zqNPbrmsyCpDwDECMhFek-GRwXkgxVwwHK0Jga-RSQGh1P7x4RbVYEcyTKU0d9_frYnH9BalgdCVe4fGfyF-Olt8OPOLvgoZ5iGqJmc-cFWeUgMdT3qFN5wa-cGWxGegbLj-5MaOvJb72HEDvI-UVJn7oMqM3yKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇧🇷
تیم ملی برزیل برای اولین بار از ژوئن ۲۰۰۶، سه پیروزی متوالی در جام جهانی کسب کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/96891" target="_blank">📅 23:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96890">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBs4o5kDyyqugqyFoH40dd2-ZBqJmGFcJ3qQjzdL4NwrexZPbsOdqLXqEMn6KRvMyLCucVahGp5DQKe-e2WGgIiWTLD-TJyRL_hnk1i13zibpyavk_6qbzi8y8oHsqKlFi69wV_IvMvDZfVQywFtBKECDv7a-BCqy8zsj_na0MqbhSd_3xVkuRflqivqSO2DtyRhdheORRUiHuGlGCQbm5bo5vx_pu7swX6nfxQFwSm9f9FO4400ZsZ5KP_dhEXtdU4WlgIn-BtRtjxZKrdltD0a_7qeWLyGLmhFbBlgaEkFKaQvkWLqUP5JavOSEemVfvE0L9uJIxYokERmnjLFMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
📊
گل گابریل مارتینلی (در دقیقه ۹۵ و ۰ ثانیه) دیر هنگام ترین گل برتری ثبت شده در بازی‌های حذفی جام جهانی است (به جز وقت‌های اضافه).
‏
🇳🇱
ادگار داویدز (۱۹۹۸ مقابل یوگسلاوی، ۹۱:۲۲).
‏
🇮🇹
فرانچسکو توتی (۲۰۰۶ مقابل استرالیا، ۹۴:۲۶).
‏
🇳🇱
کلاس یان هانتلار (۲۰۱۴ مقابل مکزیک، ۹۳:۱۸).
‏
🇧🇪
ناصر الشاذلی (۲۰۱۸ مقابل ژاپن، ۹۳:۴۱).
‏
🇨🇦
استیون (۲۰۲۶ مقابل آفریقای جنوبی، ۹۱:۰۴).
‏
🇧🇷
گابریل مارتینلی (۲۰۲۶ مقابل ژاپن، ۹۵:۰۰)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/96890" target="_blank">📅 22:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96887">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qFUjRv3_WEXEm_k_YKlpEn62Q84ExibMBNsFDvv9alBOOHpsEh0MS5ks9zGSwNkyxhCDlCpWFwN7oPC1jxzr2c25ESqFnJFbOVg3fE9D2DdhFOR613DAvwHjWUxPqLGrR6JdFnA6UCRyFPOQYZINNRrWT7S_Ejze_Atk4Hh5tm8JA9dorVRlLwjkR5vQb8WKcngavTmQJM6smYKmIbFNWdN79eqYcovrzSysbRwU_ZQytC5xZsrS1lM31Vo-BHKs7y4gh2J5m89IWwYpbvutKyoAPWe5Lir7bcbCuep39Y3Lo1Gq22GMpjS5eHXgIGd5mfpgfpWFpDncv18L3gxADA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pYNMu5lS2BhVULPvWHpSDuQtdeH4gmqW5RWLPirt_HtviN3ReqriK7-BjtSsE5u2EwQn38n3Te1ejVWUI11rPpZAjZBKeXxy8mqy9jqAYPga-fvUdlTQIOXrmSljQCcbOIjx8Qw6UeYCbYR1LV5y6kC986-Wl49dN5b5XE6hjxRF8teJRAolyUT0DjkGVcYLjICrSImaTj4AXMtYvna6EUFRDeQiMy0a0s0tYsmAZtS2C6n67rGVVBodcYAtiQxXw3ge-981Ci0Zfra3k_tYnuzcXpaNIJz_KRQL_QzHeJVVvI4T6CU3xYBpcaMnsY6zuWfXR-ZdIzP1nkp3TZMoRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QNyfjx0i2gUPv0Qcz3PVB7N7h1hA7zI158mpx0WcJj7OXZWzo2Gww9gb6Ys3VQchAOUmW7xkrQyiewQuFLczEPHQKeHbdJ4tB3--4Jr7syjFJQulFXxZCqIIiuPsMoi6j4bTmLgtiy7TCEMUxH4_7r0ktF-AExivHLE49EAWUPTQXtZxOx8l22IUJTx_KcUc-yAF5neM9MTImpxc9Qe0GR0pagtse1ystIFb6XDZwIPpFJzi_xrmBV50LIlYYxDBL4hAdueGM9eZ2jOD0RVzwNRRpSXcZiyKrrIx7SCdgZsYeBkeQzF94lCgo5rUnGgHurFRLpkMlZu3vmuRVbrtwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👏🏻
👏🏻
👏🏻
🇯🇵
شایسته‌وقابل تحسین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/96887" target="_blank">📅 22:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96886">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6doP0i6cEBNUGBv7blp3KgfQUcIuXGvKH_qM2sy68Xzpfvnf05s8U7OGvmLHz4nmkqApEq-Y-z3_V1xKMFAfHzkf5b0OSyRSO5W_V1LnqEOHh28VLQiCsq8ntaPkGSx3pfWyR-Ip_6WSivIa22UAu2toVlcjudasPT2JGfKhakkyvymsGFHXQGNsm2nIP5DmdlJZNJ7gBn-ZM5OGbzFdM7-uJoD8aJAzehN9zzdo4dzxBv3ObeTfXDff7RUON7JgVCA2dWgrnXU7XiCzLwfStV1WZ6UZU26ebV_tnTezbW2-05vnaS8QD0BV3lYkiN_k-gsf2in-DIUXVlxeAhcAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکی سرمربی ژاپن از قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/96886" target="_blank">📅 22:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96885">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsKHWejrq5BDj49QlC-0jMfu7Mh2SAsV1Az6S7N-CtXNpbzOArHYpANoit6FzXo6EaI2J7w8VnYxRa6ziXMM8h6y8xsNh-wMXDYC0ke-3soeGLv5l5LrU-NSz_ggzLM7e3cCFakxGWrS2D63ILd3BFMpCo9IS5ZbcO61SCsovdEBniPSRDXTdld17d_WsxstPPSsbcADolLbzcCDFPCKGU-4KDU_5NK6x29fkQjRL1Vu_rsHkg8LbL7NWZTKLdJYQEyxbhYsz-wYasnz_DZG-vqANnnU17pqiLMfdJc3Ehequ3VwABy_2Dx5ilv572Djep5wuL0Mt9pg_j6cMblPfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
📊
برونو گیمارش در جام جهانی فعلی:
💥
‏• [4] بازی
🪄
‏• [4] پاس گل
‏
✅
👑
🏆
صدرنشین فهرست سازندگان گل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/96885" target="_blank">📅 22:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96884">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🇧🇷
🇯🇵
متئوس کونیا به هواداران ژاپنی: "ما پنج جام جهانی داریم کسخلا.
🤏
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/96884" target="_blank">📅 22:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96883">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iw3FLbhwaCdnaECrKqyhMR8WGBNHWzR7UpTwidPXbpvP_EE_Yx5gKaQ3NL6TZ_oqpBsw28fdEGTp0HDiEof5-gxEN3QZw_inC_fZzwiXq7w7sSVDFGHq30FDaKhtegekVCWDFIB5GNadAsJwL1iKDo4FI2RsV2rS6caGILBYDWcNURXSqW8PO5DjzilBlZ67sEmW80n9RRoyvT9JlEb6EGy6NisjRcqoK1SI_40PrG1Oy6XydAz2tg0aMGV-tuupR168SWvnEL0WIpk3g83KKQcLAHDvuFE_bS9ARRBrSQ4CNGakgiJBtsA7MFokF-ZZaSPEBG7UroGOQgjaLUcdxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😶
🤯
🇯🇵
ژاپن در ۳ بازی حذفی آخر خود در جام جهانی پیش افتاده است.
❌
🇧🇪
مقابل بلژیک ۲۰۱۸ — حذف شد
❌
🇭🇷
مقابل کرواسی ۲۰۲۲ — حذف شد
❌
🇧🇷
مقابل برزیل ۲۰۲۶ — حذف شد
۳ بار پیش افتاده است و ۳ بار از جام جهانی خداحافظی کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/96883" target="_blank">📅 22:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96882">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eohAnGX-xFqSucubTmnV-y4-yourLEeSUu7zLUaWsevU-D3W2AbRmglVZr8-AOzAV920HwQ-ObvpU8YSR07dZv3JRtDvX-HVokQjGYtnopOpk4EvKsfPNV5_hvRngzzKCVwH72UQtEdrcmVGsFp9RLUL9KIQmH-9exXh7PljMMQ-G1qgrkEVeSVkroWur2RMlKZf6txUCtkpzw3KELOpCIgr5FjVUr0asODQCXDHuEXFo5iDHv15FSjhdyKiMAY7EXGJxg_y2EaJ2wd--2Np6mHDo6gAxQkSgTzSWH52C0fE6StY-gUCDM5YyoaQiHwR21NvMJGwnG5x9s0Sn7PaVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇧🇷
🇯🇵
متئوس کونیا به هواداران ژاپنی: "ما پنج جام جهانی داریم کسخلا.
🤏
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/96882" target="_blank">📅 22:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96880">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/df792jo1Gyd-wEodr8FfSwNrFpuL_y-KFmWZj-ZGahVrCRPGrbcPOIP5jmcK0uOFXOy8tEs9O4tBVvtqB30i-MgVfEOAIxjUfaj2MnNipIekS8GPHZdX6ac-2v6QgU-p0rinAzigOKZEP07-kG6mhp9cnWyIAgVlTJ0qXCaLn0IyZBFVogdgHJrNpbz0loDA7nPAGOKgBTpWtLjgn5rcl0tLwdplJA4mpYxQj7sQy_G8ev7ZIwoPee6URWmJTawEqSAHcqPDMzyfIiTCdX3o801Drk_k3EyX3B3g8Y4beoz5EqYWGWrwYwn4eRwNiuUR5gamZ4D4g6WNxAY6CCW7gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OWLSSQ3iP7j68JidTX4RDp8WhGFYsqYYHX_NmHs7XfMVZ-1d0eCsSFTGr18xfgNKifB1u0-1p9E6se8D--Sl2iTVRZAeXJAqtJJcmzGkBtqXkKXfmYpovRsI6gg6Y0lQdbgrPXXghQz-GI-R0pnCiR4CixiYG9HyAVGgawF-2Fqw9IAvLaRU47ZTSnu3lPca6fDfHSuuQSxaownnhcv-wQspLrdkJUdrZ42Sx7IcC7Nbev74V2x0KgcQhV-IUayNrwMxEarru1IDN295WqrzxVFcmKIlFKso39CvEkPK4xKfKY9rC1P18q6pKCfLUAl1lMHN3gfcDgKaADT3wW5iHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
📊
🇧🇷
کاسمیرو (۳۴ سال و ۱۲۶ روزه) دومین گلزن بزرگ تاریخ جام جهانی برای برزیل پس از پپیتو مقابل دانمارک در ۳ ژوئیه ۱۹۹۸ (۳۴ سال و ۱۳۷ روزه) شد.
👏
💛
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/96880" target="_blank">📅 22:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96878">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ta1n7QFdOyxRWlobCuO5AicT386yJgJXzry8vwtw_ax6KKReIl5-8XCJef3NK9_hpUg2uVmM0GjnI-1w7NA2c8UngfO63GdDXQ-FpnI9skZ8lzJWhLL1-0a1_TsG3xKuqeRGGlXLLJACRzufw7O6oFA4_NuBBTVZQmSOz6eSIBolBoytOR-t1GCSZUpf5aUOWYRZSFzKAaBhm7qypT6eS8PEnmw3MJ_UECUep40K8GK3syHxincf6j7OIMfG90BNuamiSK2PDt30sFkcexXamJmIM06A-1ATie5o_zifWBELBh_hv97knWvxY-Bh-Y2JPTUGrWUAre9W2hLmVFXyNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vdn1Q2sUpJoJQJNBPsCYa1yFRT2QypKZD7ayTdByIUTq-q5cwMxz_zcYvC4lWOG7Lqa0FJ9jQhodSRKcwktAq7dL_Ku_W7mpBEiJCH9sVohj1ixvhZ_MoNPuGDN0QQcsOQz234C-unaQaCl_-hSIPHLYciLB9o9Lb5-Arl8E-1IJTntHs2L_3WsHbhpfMXxPzOCy499GBSTfBHpDBMaYhX373VJsCET3Z8N6NguhPZ34jCYx-vph2zs_jYfei5kxd_1JaT-iW52DFk3qr7atWL3ucDib_OIDYIfXYmxsIaodSAl7poawvVzwyQyPxYpugng5eXy2H7RGAMl8WZAEFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇩🇪
🇵🇾
ترکیب آلمان و پاراگوئه، ساعت 00:00
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/96878" target="_blank">📅 22:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96877">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VIXcvXPJKTrgGGD3B2pgmiaWJ8VGNyom5--w1pwlDqx8KFyJZv3sRzIMNd1twubcvVLkvjkbEZQjJlnIW5Jtx8_4PRInrt24khxK6EgWPklxPtVyfCMsVtkJ-qlllAaCtqx59cOi-F_55sjQ0l79P9_3MRsCabPlLvnkVr00YPYNMQWQdEhjgKsFkoHdx56uCw3WjNqbj4D0GLa8tGqaZwkA18sGX6VhYOjW8Lvfrs7DJP9hUles1SS1nh42A45ER3iyJXtpSJI35WBKkxjelS4hFNxXhkQjmAmTRrXEf9kqrpxvdpLQSYPl2088nu_xHdEimAD0puffUZdEsqMoGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنجلوتی بعد گل دوم برزیل
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/96877" target="_blank">📅 22:42 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96876">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVV7vx5p-G52glVbKFw_jSaIgHXZt3KqZe7Ily9KAo0xP8Ne6-FyCbj_AtsUBFSzFDttKu3z2FIV_Ff_Uz91i9fLaveAu5U0J8twk4gf3VyeWoCTQJUmBAbFA9fWvLDLLppS6CoFio_bRUyC4FhRHHfC1qh3mIY2dUOy96uQRpTBRERkczKDeHcOU2iJaeixdV3dyCdTLE3U1HA60ppDtJmiJ-gwc4jzOQB19zgobFqKeGYn2saw69-kWMcGEqyn71fS6aB4hWcIE5yeqiffc4zoy90y3x-rqdlyX5PvW00FWJ633Z1xVMkIysR6iX8s4TbOm6UVFhyM5NfzT8K4jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
آپدیت نمودار حذفی جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/96876" target="_blank">📅 22:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96875">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Plwk5jePYxxa_0remOnPqXA3cKMoM7ruCVTlRdivh7aTiRP6k1-ZfldgGGahSu4qzmczHnqgnCsBX99K9m2_RsX7DzAR7ddYAYkecLGJlSIt4ntHYiHqoXlT6IfNKeSPBSFLPA-pB6FhzB2phE2qsPYWmkejG7D2uswzSq3bsbp6wEhRB9JFPOx5F3Q10SKVX8rwob6VUmYb4uk-EB2kL9014ZRFgF0DV5mrIxMhRHwyFQ9-d-z_A3MgfVDhh4-K8cZda3_kUMB7eCIRrQEwSWHZ_YjF-QCHvAJW_wipXafDgYb2Vg-m2N1Imx0ONaCHEnzo2RzcmmoTQbLhxQby9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
رسمیییی
🇪🇸
رئال مادرید به توافقی برای ماندن بازیکن نیکو باز در فصل آینده ۲۰۲۶-۲۰۲۷ در باشگاه ایتالیایی کومو دست یافت
✅
.
- گزینه‌ای برای بازخرید حقوق نیکو باز برای فصل ۲۰۲۷-۲۰۲۸ وجود دارد
✅
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/96875" target="_blank">📅 22:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96874">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGlPW_h6l3Gi0scSqg8JjNrkKPRV0ihmcdRDlKhijgyWieQsj24u40nkuAFGNm4CGWqfjztF9kHNP5JUAvB67W0X9tVJ_6gB6KU3hXTsMaFULk5-qTx2syTg1pR5nuwOUsf48Uh-aMy2xFYfY3DQFxP_DDwf8ivwi1FAzsUfp-TM7XFhK809Kf__t7_xkBtt6HlNgI3iTZLG-GT9A3R3JpXPgQlc8i430s7gJvaWdb1_nm3_N3NDiSp7ZI2h5C8v7e_xCnrBwiYkidJPLnBS5dfA91JWUWEhy8Azfb6QYriJ9lI6Aic4e2ZBCGRMeQZDWpI7Y1UdTdB3SArIr88kPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز هم آنچلوتی
باز هم کامبک
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/96874" target="_blank">📅 22:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96873">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQDCLwIgy61ZPxvANrmL2W7kpJSOA5qbMmuTjfqYaUuSA5n7_RjzXCcAxSRyFehOLFhHobanDsnpul7wZf0Lt2xhmiKNOzMSYJ1U7tpUp8xYY9439ADTF79ApsISmtfscsUvmAPfm2RJnskErMfq1TN8XmKqjr8Ox-WEVMXn2OWQfJ51JHgH4XSL6zHL2JwtQ2YAQl13FvETKMbxw3eMegw44QRU2d0zp3cBVgz3AT9s4MEcZAozi-pjy9rwicEMAj7nuU6vQyqwr5ptG5OQw7AIDCHBjpKG6C7BxIWI2zSEn39NcznVXEACxwKVXa2oVU8KgWn-Y87dcqm3GkRRIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | پیروزی دراماتیک برزیل در آخرین لحظات و حضور در بین ۱۶ تیم.
🇯🇵
ژاپن 1 -  2 برزیل
🇧🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/96873" target="_blank">📅 22:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96872">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/490bef5d86.mp4?token=LR-0CJvNy8GLL4fLmbIaA_mEt0LrLxMVaKKR2sfP9Savd2J9opkP6puS_VhanqfBxtx1Vd1moNbZuK2J1L7tAJXltW_rSd_WuvgyVbrdQAreoLWRo-_TP7yh_wN1_x36iiuj-gjG1SqPduAzHjaAKbDHesNRiGDdCZyGKs2gLmZxE0Jte9-sbTDBXurYIu6MK_nqy0pkbk_1fpY5tIaOU6K2-ZAlG3Zw0PrKsGV0-aP3NHtfRbTcM4A2jxCrGxWO48g8JWkDkruDPX0BVUWqtIvbCgS03m6vLGmSDm7Aco-BCPRjKfbjdz0sigtPTeohYAPDWnBGSFWaMPmE05FZh5gvobb44_rmC3GqKuuNtNdOXbZbDHYEmDzlFSQc8LuWEgHlivfkqLYgZ3OGGqDx9lfPb90PXUt4n51UH5fFLN8AYbInoXTd9WONDzBGNwskVuVioo_-n29zFSXJlxvmthDUePer7ixQeOmQ4H3_RMBqZoYcvzJ3bt7yLsENVWnVOI7rtV8s3l4CjE2-GyVHI37-53T9ODfJ1fjvfh-tfWJH_-xwKL0sxxF7LKbiTJJn1I8vkakNEnO4_6sXzu-OR7D_kHUNKP5579bUSu5cZch93tqnLkiJBrzy_4bYMFK-fse0vpH0l27IlGVdcWmL1b5LVFmOg0r2LY_-MQRHXXo" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/490bef5d86.mp4?token=LR-0CJvNy8GLL4fLmbIaA_mEt0LrLxMVaKKR2sfP9Savd2J9opkP6puS_VhanqfBxtx1Vd1moNbZuK2J1L7tAJXltW_rSd_WuvgyVbrdQAreoLWRo-_TP7yh_wN1_x36iiuj-gjG1SqPduAzHjaAKbDHesNRiGDdCZyGKs2gLmZxE0Jte9-sbTDBXurYIu6MK_nqy0pkbk_1fpY5tIaOU6K2-ZAlG3Zw0PrKsGV0-aP3NHtfRbTcM4A2jxCrGxWO48g8JWkDkruDPX0BVUWqtIvbCgS03m6vLGmSDm7Aco-BCPRjKfbjdz0sigtPTeohYAPDWnBGSFWaMPmE05FZh5gvobb44_rmC3GqKuuNtNdOXbZbDHYEmDzlFSQc8LuWEgHlivfkqLYgZ3OGGqDx9lfPb90PXUt4n51UH5fFLN8AYbInoXTd9WONDzBGNwskVuVioo_-n29zFSXJlxvmthDUePer7ixQeOmQ4H3_RMBqZoYcvzJ3bt7yLsENVWnVOI7rtV8s3l4CjE2-GyVHI37-53T9ODfJ1fjvfh-tfWJH_-xwKL0sxxF7LKbiTJJn1I8vkakNEnO4_6sXzu-OR7D_kHUNKP5579bUSu5cZch93tqnLkiJBrzy_4bYMFK-fse0vpH0l27IlGVdcWmL1b5LVFmOg0r2LY_-MQRHXXo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
گل دوم برزیل به ژاپن مارتینلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/96872" target="_blank">📅 22:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96871">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">پشمااااام</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/96871" target="_blank">📅 22:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96870">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">چه دقیقهههه اییییی</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/96870" target="_blank">📅 22:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96869">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گلللللللللللل دوم برزییییل</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/96869" target="_blank">📅 22:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96868">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">گلللللللللللل</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/96868" target="_blank">📅 22:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96867">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUmDLBct9lSpIaC8FDB0Wt2HVe3cEkqqXWBzoxXkkJ6gKw_YQnHypYcYiD5NCIFAWvmWITkR7gUtVZB3APy1h7SvT9jPBNj9huUon21QgkBAtOQfgoXy8TUTn5bbZSkAye0jwc2qYtrE8QqsKUsO-DKLXvLY_ZaYMV3kesedyQfZw-ixp7C2L56jZKqPK6HFXEx6J4q5Vqrs_fkf7cIwygJ0-aOcJ-edcCpS9AwUw17XQ0tr16oH3qxIwJ1VqWLEVLPbf3eYKg4ouAI4jSA1fjQg7Gik_YI-dwOdsFsLXHLoboDX0SjvQt7xSRBkfilfi39_QFP8_X4pZpZZYMiD3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سانسورچی خیلی کم کاری میکنه اخیرا.
😃
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/96867" target="_blank">📅 22:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96866">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnR2_ASNaHRdVS49b3OcwkWrkvO3kpYF7vgu5l21vkCDsJl21Y7S21Jnt6Z8YK_iag5qBQzJ3VXRWZYW7oTVvOMrEVPB4F1rX2Odf23CjpuYwZj3KMsyBygXgJTFsI4MOlUxxT3ZOeEj_pIgtpdCUObjYQa5tZg4_Y8pymeDfJJjtGl9YO9Kn-vpbc91TpPmP0Kc9-GKLaDi1oYmN6oLJmx0JdeBGklDHn9xmgI8gJRriSgfPg6Ay6IENNd1zwvaX4wuy2OhKYWHoFKquf90jtNBKYKCBt4pdatA3FOu7RNRTcmDFy8WkQpgw_XzyzGb5VewczXCphlBaRoE-FdJKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
چادرملو اردکان با برتری مقابل گل‌گهر سیرجان در ضربات پنالتی، راهی لیگ قهرمانان 2 آسیا شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/96866" target="_blank">📅 22:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96865">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">آنچلوتی این نیمار ما چی شد</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/96865" target="_blank">📅 22:11 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96864">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">گل میشد این توپ بهترین گل جام بود قطعا</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/96864" target="_blank">📅 21:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96863">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">عجب بازی ای شده</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/96863" target="_blank">📅 21:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96861">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">تاییده</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/96861" target="_blank">📅 21:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96860">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">مشکوک به آفساید</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/96860" target="_blank">📅 21:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96859">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/60a5747017.mp4?token=f5uuOa0LgnWdHcIym2vvuZpmSs7-PPUaCxdkumtwQjIrBh08YW6joVar3Gpm4Dk6aH29fuUN_96JDUAVXJWl24hl24k_VLENgR3A9TMmmiI5P_nBi8iQ6ap85dhm0qvvNhVJawmTxby7-x9-Z4zGOjQv-O3QO1F8azI7NE5br56Q4pIuKLda0mHaAgArl2zXwmGihlYTlblIu-DxbyuZb00-ivHd-vwgCm010I9-efAGU4aU9cATp3D6Vm6oKn7gVly_tJznJTS8WA-fUqmaDrETYOyJpJCA2ox2QWp4WOaV5BtN-XSo9FxEqBzw_gk0Mhf5mwJV8FxodB4oiSXvj4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/60a5747017.mp4?token=f5uuOa0LgnWdHcIym2vvuZpmSs7-PPUaCxdkumtwQjIrBh08YW6joVar3Gpm4Dk6aH29fuUN_96JDUAVXJWl24hl24k_VLENgR3A9TMmmiI5P_nBi8iQ6ap85dhm0qvvNhVJawmTxby7-x9-Z4zGOjQv-O3QO1F8azI7NE5br56Q4pIuKLda0mHaAgArl2zXwmGihlYTlblIu-DxbyuZb00-ivHd-vwgCm010I9-efAGU4aU9cATp3D6Vm6oKn7gVly_tJznJTS8WA-fUqmaDrETYOyJpJCA2ox2QWp4WOaV5BtN-XSo9FxEqBzw_gk0Mhf5mwJV8FxodB4oiSXvj4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول برزیل به ژاپن توسط کاسمیرو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/96859" target="_blank">📅 21:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96857">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">برزیل زدددد</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/96857" target="_blank">📅 21:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96855">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/96855" target="_blank">📅 21:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96854">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wjqa9koTTOaGYhx35niVMMbFupl92Aqf-5Eu70mW4wF7F7GisrLUQ-hVLy1nVoz2NZtda25bYdsl-8hv5w0FWaceaj5hfrWJ_aKw1K0mpLJfhwUnCtZvSpz50mkCcWoTmyiPUZJSg9zTswVA2RWhYEn5ihSN-RVl2w0TEJsweAuwjPGLHbyBx2-njmsquipAHyB0k4Rw7ljRxEWBGVM5nZDxejXqfWZ4G3zjXhLegxBvBL9BTjmvDPiYoc3Y_eHw1soDT_iCcTDN-2ShW0K6_6cNmgujKc0LvFaTRKKTVZr36l4QLGWd2mzi0K977XMnHk6CB6iQ7U6ZBn11Wg6HJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطوری گل نشد واقعا برگام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/96854" target="_blank">📅 21:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96853">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">این چی بود گل نشد واقعا پشمام</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/96853" target="_blank">📅 21:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96852">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">برزیل خیییلی خوب شروع کرده نیمه دومو</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/96852" target="_blank">📅 21:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96851">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">پشم ریزووونه این سوزوکی</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/96851" target="_blank">📅 21:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96850">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اندریک جای پاکتا اومد</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/96850" target="_blank">📅 21:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96849">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGfWZA9tobvlGf2Cqb4mKU_qzfzLjCbOy-pAwyziV3NjU4rOB0YCv2KTaJPffnQzeVuiP_zXWF4VZ57G49CPWzGxV4F1FODa5LkLSfuxIqeI-n1-VP4x1_Vk_esvApKl6B0L6V4boT6Ukt4o2W83Z462D_iD7_FNdCC8IUSu26CAejvbsPJLnfnZkuNBSJ2L9p7QgmdO3pXpa7vDjf-wflGdiTpqL-0efuIYMDkBd8Bfi1jQ8bc3N3TeXrOTZUn2jnupg9xx6b8MyCX5V2sjMW-4Jt_qDHyB0VHI4kdaijvxhbFB8OL4E1E_rSPFH9uvHXRXyWOpqSAd6KRwSokJdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ژاپن تاکنون [8] گل در این مسابقات به ثمر رسانده است، که بیشترین تعداد گل زده توسط یک تیم آسیایی در یک دوره جام جهانی است.
🇯🇵
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/96849" target="_blank">📅 21:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96848">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOUhQqyF6rMGAcAotCRPHd9iyBdSIerfwLrnEA65vGMlk-iI_LXR2zyur_rNiCb79muP_cB1gFOjmM7tyH31Sj3UKHpBN4zqTzKZEXatMIrnR1ErC9pgwsjzXwORUwTjgIN6qAMhODqEAgzzY8sODfYoVAJF_9m8jmktuVzDNz9F28_Y_q7AUpgeQWnLqYORXAlxvW1CRaalprsCQ-GxXRNy5oJIZYFH7NGbVzSwecTtJo7Gm-r5_NroC8xm03RvChZgJ5Lr8uywwiGc2q2h2nzxTEB5n6kEMFbv5n3SgAylw5sSUoYGsvi92OmwHrahCtEcZtBhR29qc30emyDOXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار و ارقام نیمه اول بازی برزیل و ژاپن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/96848" target="_blank">📅 21:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96847">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/96847" target="_blank">📅 21:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96846">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cHdWldjjrIxuz56tN6AdDF1TG3VhzkljDY1CxQ5EpIGHL7AhtJqrRUV8xGOlA0W80yegUGaDqiYG6nHH6xAwjs3S1amWexRmpKZWeYxvYLSazSJ6M8WYKLvfFbcrWwf3lMiu2IuyMd4j19y_vh1iZKEenA9KtqZ96BSrBCcBlbi4m2wqvMHScYrzhZlX6jC6sC7lvvgRtSiNqfU5zC4jpo1DBsV4bgb8vtn4I4p2JZWD7XO_nOcblPWZyuL73-pXYT5mUdT6uJm42ypxJYxoyGx0eoJ_m_v-y3jVvd1i4F2t_mmXeHoiIwh95-NnBhogCEVj5IQKxxXcmYBlmEsFJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/96846" target="_blank">📅 21:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96845">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5K1C5ktG6TiuFtrUh23660DifG8CiGTwmUk5ugUUiKKouogPlLyfWITBZJqv2YV4M6hEAcPBmiucZQS4I3UftHQikX01mpJDV5VZGAeI1r4lyL68lG8vrGBolvxrLzUZmpmUiwERQsWLA5ywJuRBCfJTYvDaJO3Z9x2TRqphNil4y5JthZjPDn8V-S1GMZMwh6FzTTnlPPAT4CGdcs2HF_-L9ygCs8Dlqt4arKP-QAUPtJYmvlxHJjo5TmKEYu9tTYSr-XYrnx-CV_F5WLW12EWc1Gaboq9utL1bspMFlKQhWxNUdVwCMsKetzB2fcNmycQml7f4f2Bkk8eJe2E4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
برای اولین بار در تاریخ جام جهانی، برزیل در یک بازی حذفی مقابل تیمی که نه اروپایی است و نه از آمریکای جنوبی، عقب افتاده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/96845" target="_blank">📅 21:25 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96844">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">پایان نیمه اول؛
🇯🇵
ژاپن 1 - 0 برزیل
🇧🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/96844" target="_blank">📅 21:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96843">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9WY6NeVXih7xpJMpvbMEHCF9n4dXC4wlqBg68mbDb9eTeGPdF56CB-JqCiXczUZSSJNi-xyje6gJKEVecwsg1s6mdOTKTiGL5jvIpXIBISjdHN4n4XuHc6yhk7auMay8kEl1MWf_XdSJ_RbqSzb52GKZqfFAz4KylcpPuv1zlOkPEOO3yERAHtgWZMBOgpBI_zFIR2lS7R_he-e7OFBMOiNiXuH91-UcYDoM-umIjzfCYmbNRO23QhDN-PNPlznFglX97w8LrI3mfIhYsd_6zFK529W_YsOvmvZFkIKpC_qsD5zcsJjPBG-9QqLO3apXKOM3EIwMQ4EClQdfNcMGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت آنجلوتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/96843" target="_blank">📅 21:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96842">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">کاظم داداش چته</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/96842" target="_blank">📅 21:10 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96841">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wfj87If1oxqwAgjOb92Ks9rzmghZUBzwgFzq_Om9pfQKQWzqbOhjZFHbDjnny_LjFJEPaowfHNlJOELtv1wkjB_hk2BApLqYq55Lhsa2TDbb8r8r4Qen7TH-hc7QT3wD5NP0CIxrlC9Hq2tHhxOzVjwp9USJ4M6oLDNSesZ1z4lPIEsKO-Cqfw4UhFjYWbJbtWjqyScMHr8c-kvkLA0GzKpAPHVhPcAPF3JUvdIM7pWSDjuHvciLHl7z0LgBZOmwoYj3VOUYEQ21A0wFMdsAN-n8oz7qDvT8dMVagRLq5KaByQtuYqNMH5iq1KlzUV-fz2kjdy0Gk480R4EmgUpnlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلویزیون ژاپن بازی رو اینجوری پخش میکنه.
😃
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/96841" target="_blank">📅 21:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96840">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHbfULrWfEB2VLuaveR7q1Vt8CiCLNJA7cn9f5j_uuoKWE3xyNKloan2LuRFQG_0YsmC7Q7wodvVSxNDdLrZcwrhNuZg-8f4kPs4x4VyInDV1Pcf2_nMx4FT5mR5Fkij_SxVVAzczarPH92wWNJQhpA2XHgYGcHXeWlXSWLed_3sltqpRcbsPvlOXeMNOpaUtpagM1qH2VBi2XfwrKQh-sWiR1PENHJ-St5Q2o1xjiBiUU5dg8w0NYWNkahbDprng8UPH1UqlyIHZnnPUzTHBmHgmDpZVkECVyoSwMW0Yay2iXBcmnHlcj8bJrINYtIGG8Gjew4VP2D543rIiqtMPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
گل اول ژاپن به برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/96840" target="_blank">📅 21:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96839">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">خطای خوش جا برای برزیل</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/96839" target="_blank">📅 21:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96838">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خطای خوش جا برای برزیل</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/96838" target="_blank">📅 21:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96837">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">با ۵ سانت دول با چه اعتماد به نفسی بازی میکنن واقعا آدم کیف میکنه</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/96837" target="_blank">📅 21:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96836">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e64cdab91a.mp4?token=U7Ui4DmhWkguLOSKKgYYT7OQsYU-3zYgVFet08Yb5gMZ8gMjllONZjdZIlov9pxvj_xk0UwzJx9Uc7kidzeH0bx_dnBAklYIK7d-WXv-OZhQQWVeZ5Ck22t_Gq9XFFl9yk_0HL2RQHDcCvahif-GNvnQiIarELOMeORBL8N3wuX_siI9Ek2j0_E2Zs9Euqqg8FNW5rRB7kTXmssnwOsIO6REs7w4EmeH05TH67mCXlCW0QRqw3cck8XOYFSAdUK_GIB5cV9srlq_CUQ-70zA7GcufRpfnBqnl195AKW7Q5ejBKsLbqHsVkzomBV6zsD54Hx0bI3BJOD9Q9PzSRI1pg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e64cdab91a.mp4?token=U7Ui4DmhWkguLOSKKgYYT7OQsYU-3zYgVFet08Yb5gMZ8gMjllONZjdZIlov9pxvj_xk0UwzJx9Uc7kidzeH0bx_dnBAklYIK7d-WXv-OZhQQWVeZ5Ck22t_Gq9XFFl9yk_0HL2RQHDcCvahif-GNvnQiIarELOMeORBL8N3wuX_siI9Ek2j0_E2Zs9Euqqg8FNW5rRB7kTXmssnwOsIO6REs7w4EmeH05TH67mCXlCW0QRqw3cck8XOYFSAdUK_GIB5cV9srlq_CUQ-70zA7GcufRpfnBqnl195AKW7Q5ejBKsLbqHsVkzomBV6zsD54Hx0bI3BJOD9Q9PzSRI1pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
گل اول ژاپن به برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/96836" target="_blank">📅 21:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96835">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">چه خوشگل و راحت زدن</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/96835" target="_blank">📅 21:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96834">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">برگاااااام</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/96834" target="_blank">📅 20:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96833">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">گلللللللللللل ژاپنننن</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/96833" target="_blank">📅 20:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96832">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دول موشیا چه بازی ای میکنن</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/96832" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96831">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVslQkU2om4QB0nOntCMh6OM41YnWRkpOlwmPgVgtBjeh4zsecFjZU7jxrKKU9mF2lkXzyzZD8anuY1zy62a8J7oTz-B-2_rrdDJ_SKQ8WyC2IH6jteo2Xpv9qoRZ9J3VEGEEt-YSX9ExVdwGk9MexHTOfp1uucsp5my6FWvmQ5uqmoxRXcOuEeDlOYbfO9lKNt5ygEmUC2lKGwCVoQP7jZ40UXjqK-3s3EP14wwS0C6tTiXh_rcDwKIehnf8aQEyLdHfpSbImcFgJu9XK7f4wsXqALmZ87vFb2c7dD1vuO3PsuR2hdEs3Q-RLo9cybACkfkKPnCa8YwWQ8V254iMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرشیووار: بازیکن ژاپن باید تو این صحنه اخراج میشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/96831" target="_blank">📅 20:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96830">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سوزوکی چه سوپریه امشب</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/96830" target="_blank">📅 20:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96829">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">برزیل داره فشار میاره</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/96829" target="_blank">📅 20:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96828">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ke45wNyFvgqcLg8Gmy_bdBAoJjEGtU9tXuSAyK_vUtIRklCwlkdtIxzJILZQqROZMPVGca_B0YJes0Tx7MPqQeN3zZgCaZ-y5HuCmm3p4LTrzutz7ug1ZNTTPi7jV_Qygts5r7gU1woj5FI222sL_tonyRShFfOUaSVmFFinJRgHNC51d5oLxlSIprzUO2SMRF8cj1aP6joAgKrHMbZPRpZafjsksS_VzPWw9m89s9ZRBCptSVPf7XKmAZRP-lOKeRJMIpR7cx3wDqQJdYFsgtJjiM2GCH4cTrUgrbEq5qztF-Ib4OA39sZHWsGupHRVlQvGbhkI0Ikzh7Qjg2BMVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عشقتون رو نیمکت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/96828" target="_blank">📅 20:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96827">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">موریاسو همچنان درحال یادداشت تو دفترچش</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/96827" target="_blank">📅 20:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96826">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">شروع بازی جذاب برزیل و ژاپن
🔥
🔥</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/96826" target="_blank">📅 20:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96825">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpj9jhj_8lQqW0e4P9DO8B4ySIUbyADI9HjKOQ_LmkZF6ljzdcQuWPAQ-3U5cBow5XE4tjHzwE_PFn3G95c_dRCS0EkvZMVlEhfzIHzA2JUpB8_Y47MDFYfXv6UB5dPx_lioNjOfOTb3eTtmrRO7UURMsjEuC1dcQ4nhYZ_fKZFCzEJMgJUvaDAuBUIlBMiloN19yoY7CuMtzf7d1-O-EtwsjCauBXz69ASLKli7IchTNRi5ZaKt46z5wtVypmkiDAJ5lZvWC13QJyaTRjiKZtMpAkIlREA7YkgePnN6d07uXCG-O8_tVyWgrfRNDUcgqvH0AD7-ADDOjMt_daKSsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور رونالدینیو تو ورزشگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/96825" target="_blank">📅 20:26 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96824">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9e1e888ed.mp4?token=SXPA72FMaimj-cRSDSnAN_vAcZQJ978Fi3LBzti9e2zvghkcOm0H_rBo7x9dXu7oXTDk0dB4oh0uc7TLT5zgLnun4APtCWYc_807b0yBAU6lcDvBVUPeyr26vn0ZUI4DyO359IqwlcUQkdCQobdzXKCGGWmaSZC2s2OMDz1aRTNZkznv5zj13l0Ao3LsPEVM130PXsRWtSblwoCxpB64mNpiDGTFSWv5JYzf3ox9IvT0VsPIegvm8J1H7_iYyGe9TKCauC5rIOHmBTG9VneSj3JdUHe7mOprk-Zx6OILHYJYNq-be7drLQPO7fIfeGkBMoQU48dAN3Ziq0ecWr2ubQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9e1e888ed.mp4?token=SXPA72FMaimj-cRSDSnAN_vAcZQJ978Fi3LBzti9e2zvghkcOm0H_rBo7x9dXu7oXTDk0dB4oh0uc7TLT5zgLnun4APtCWYc_807b0yBAU6lcDvBVUPeyr26vn0ZUI4DyO359IqwlcUQkdCQobdzXKCGGWmaSZC2s2OMDz1aRTNZkznv5zj13l0Ao3LsPEVM130PXsRWtSblwoCxpB64mNpiDGTFSWv5JYzf3ox9IvT0VsPIegvm8J1H7_iYyGe9TKCauC5rIOHmBTG9VneSj3JdUHe7mOprk-Zx6OILHYJYNq-be7drLQPO7fIfeGkBMoQU48dAN3Ziq0ecWr2ubQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امباپه تو جام جهانی وقتی هر چی گل میزنه میبینه مسی یدونه بیشتر زده:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/96824" target="_blank">📅 20:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96823">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🔵
🔴
اسپورت: بارسلونا قصد جذب هری کین رو داشته ولی طی روزهای گذشته پس از پرس و جو متوجه شده که این بازیکن از موندن تو بایرن راضیه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/96823" target="_blank">📅 20:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96822">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/750ace79b0.mp4?token=V26aUdFMegGY5xKqovor78yvMrwJQ--DHVr9cnieRvPA20C2oZ1gK0PIgElLDOFV8pva0LtHwx_icKDF77CVcbF5mdwDFmIZe6w1w08KD0ptW7dhb01kPpdkzMNTxPdWwivDS3A68yPsHRHop_KZ1JwwrwuYjkLmAtV4KQ2LXggqrA0sMwxwX36WySGdjYW3CEzC2A4LRYUjd5YGT4Wapv-aaPRTrg-HFYqocicOWlJx-Gq5tHHc-G0oReR-ELCAIi7AWrp0xrYH2ai1Q7yMsu18NhLsq5aLltn79UL_5P2QYisbEPYLtx9qJJd0sRyoG3lCTtPUF1Rlh8WS_KzIYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/750ace79b0.mp4?token=V26aUdFMegGY5xKqovor78yvMrwJQ--DHVr9cnieRvPA20C2oZ1gK0PIgElLDOFV8pva0LtHwx_icKDF77CVcbF5mdwDFmIZe6w1w08KD0ptW7dhb01kPpdkzMNTxPdWwivDS3A68yPsHRHop_KZ1JwwrwuYjkLmAtV4KQ2LXggqrA0sMwxwX36WySGdjYW3CEzC2A4LRYUjd5YGT4Wapv-aaPRTrg-HFYqocicOWlJx-Gq5tHHc-G0oReR-ELCAIi7AWrp0xrYH2ai1Q7yMsu18NhLsq5aLltn79UL_5P2QYisbEPYLtx9qJJd0sRyoG3lCTtPUF1Rlh8WS_KzIYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
😂
پشمامممم اینو ببینید امشب جمشید خیابانی دوباره سوژه درست کرده و روی
آرناتوویچ و خداداد عزیزی
صداگذاری سمی راه انداخته
خداداد عزیزی رو ببینید فقط
🤣
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/96822" target="_blank">📅 19:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96821">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTRcxwSb5FT4Px-c7a5LLlZ3Tzh9r09BTax359IjyHoA00Na48kjyXki73SAjli92C644k7JZfWsA6-LqdSjMfjYZNpnAIMlkl9DW1wqoqiRry5c7iZUPFRYt1UMRG9N7WQfb7QjOr5Cn7hQol60zTzFHrewDbQVII2XMo7wwUtXy5rJNDgys9gv_zQbtU44sy-5DK1CplqvusU3xIEveqC2TqoPUeAOMcSN_Lisg93MsQP6AphuvyhnxAahqSyEv4pNVhtnQjCKa5T7K0T_SdXL4hKVfCCge3nwexnAszbmimwdBZ4T1gYuywcPFo3Mkw8c9QjuBRbvKlkn39IJ5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👍
🇧🇷
نام‌های فرزندان نیمار روی کفشش.
⚽
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/96821" target="_blank">📅 19:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96820">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RdE-Q2HTkaiGBdqQerlOEA9yp5DEOszXWdBrEnmrN0W3HXbV5inIFPa9UJF7zdSvxACK8SNEgk_GvzEKI7o7wIBs9ccGsOQGAu0fINCp4ImiYij-xVo7x-zasgDf0G-12ycaxbxt0v9iUNGMFO-QPD8lN5E9Q4rHkv4cptDLsnBKhqy-h_RsR5Kyp5145cdGsVUBxTh6pakjiNB9KPe8tUSNeMcerlIf6ovUcpLEjYmzrfOYF39W6WZHyEfAnu7xxQkC4eoUtJcqyBWIfy8lJYmyEPGBmkfNTi7JV9VeIeKd6obc_2yxPwRRBErdYdFKLwrp6lZP3A6ck_HKO4NJMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
پرتغالِ قبل از رونالدو: 0 فینال در 75 سال
🔻
پرتغال بعد از حضور رونالدو: 4 فینال در 21 سال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/96820" target="_blank">📅 19:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96819">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixFPOOSB1wxzR83pmOXbg5OH9NOuf2-n4pUr9NuRsx12nqhCrCjtivESdT8XP0jzJ0aj6vKxlusSrHu7y_NjAvBlSz5Dq1FxUlqkRFAWO_XOG92c2m2OSQVc9CcwOZjl6mx-18DQ16P40v_tPeu5IRdkx7OFxG59FO7rMBQKfF7vJMjcWCfaSXq7iIIfgwBkxqzLU1BPWr7Euv17G32PSEKZFEXelZifgYaM2Ywui6fkcsIoMLW0XNY7N0vW2fWvKyoXPUrJyrHhdoPitOdTywb-fcAYoS4q_DrruLid4QIzZGooTg-hRjMDiDHaOyXuzcQ1q1fZebX010R9LdT1gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
برنامه فصل ۲۷-۲۰۲۶ فوتبال اسپانیا
:
🏆
قرعه‌کشی مسابقات لالیگا، فردا ساعت ۲۱:۳۰ به وقت ایران برگزار می‌شود.
🌐
فصل جدید لالیگا از شنبه ۲۴ مرداد ۱۴۰۵ آغاز می‌شود و یکشنبه ۹ خرداد ۱۴۰۶ به پایان می‌رسد.
🏆
سوپرجام اسپانیا از ۱۱ تا ۱۶ بهمن ۱۴۰۵ برگزار خواهد شد؛ دیدارهای نیمه‌نهایی در روزهای ۱۱ و ۱۲ بهمن و فینال در ۱۶ بهمن برگزار می‌شود. محل برگزاری این مسابقات هنوز مشخص نشده است
🏆
فینال جام حذفی اسپانیا هم روز ۴ اردیبهشت ۱۴۰۶ در ورزشگاه لاکارتوخا برگزار خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/96819" target="_blank">📅 19:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96818">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEiax7Gyg5AOYT9gUCfvrk_LJ--s4VY2dEaFrsF6eH0_Xll2-STEJmel6WYqaL7Z-Dyd41OGqP6U_aIKAtIOvrJ5920nfqeK7mjS7OsBWHFJ8wSWF1xBuDKCpHrnmsZM9Y9r95hYnH7RJ61wR9PxNgPDnSHIvcGKCxcPzqUS9WKNck9MblvHocL-c4alsQP-WNNXpaxp9RdEoIswQdLkiFsRUaTFeb1tR19MTpFO2W_iHcOPmwZSBfaxQMepAazuzC7fhh04jyi0fVY8-expaXdg5pKKAm3HYd2XsXanVSFiJq0PoPSfy5ELgNC-xQbwUX3aQ066oSjFwPIZ8FYCoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
‼️
برزیلیا در یک حرکت فوق لاشیانه پوستر قبل بازیشون رو ناموسی کردن؛ این شخصی که میبینید دوست پسر مادر سوباسا هستش:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/96818" target="_blank">📅 19:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96817">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4223b69552.mp4?token=K_1BNZGD-h5lrBIb28MfKr4vlJbKY2HejlqIeMmKmr_UTdp2VVhbzCSWAGL3geWQMzqUQF387HMyD-W3q2Bzoaw_qbqRdEf-8cp4SxyZFIa79oLw6xj8G0tamlmmywj5ssCu0ke8LDp32sPz53Q8hfIrsocu501HzbFk8FhWu5_TgRIkQ4lkPjy0cK2SqjQO1b1ynnlGTVpeZG-7fDVHtBt-h9rWI-5vU-YeVmMYQDlqP7GcBNLWNMK_pu3c9HICgg6Ddr82VdIsnYci0tO1JdA0syBnGhcuTUJ8ZheESz85x25zQ3SpSYLw8pO1zlP18poHvE6F0wrUhE3E2-T2cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4223b69552.mp4?token=K_1BNZGD-h5lrBIb28MfKr4vlJbKY2HejlqIeMmKmr_UTdp2VVhbzCSWAGL3geWQMzqUQF387HMyD-W3q2Bzoaw_qbqRdEf-8cp4SxyZFIa79oLw6xj8G0tamlmmywj5ssCu0ke8LDp32sPz53Q8hfIrsocu501HzbFk8FhWu5_TgRIkQ4lkPjy0cK2SqjQO1b1ynnlGTVpeZG-7fDVHtBt-h9rWI-5vU-YeVmMYQDlqP7GcBNLWNMK_pu3c9HICgg6Ddr82VdIsnYci0tO1JdA0syBnGhcuTUJ8ZheESz85x25zQ3SpSYLw8pO1zlP18poHvE6F0wrUhE3E2-T2cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ای خار جبر جغرافیایی رو
🫣
🫣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/96817" target="_blank">📅 19:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96816">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLrdfrPq1trW73KDukuQP8vqmj5GbpVhPRsPREXQVbd-DT1OCV7B63l-NtiCiaDzJpeD1wu6ac9q-i0UFMWVXM1nyrgbLbJzf0A7hOjo6KrArXSg6gMfmDLDfzRUtmjGhFI8352AvvMuVmO-5lvtlCstMKXk6KdCLPk2s1aE8kLNYsZi_6BJOzYm5PcwoookQYGXWnOtB8B0OteX9tiYbZaSKVfCWkBJ1bvmBKbYfPzQxVa_dkwVtuwZ3XpoC7N0qgdUnzZ-domM668N7H_Lmtj10eV7dYtUIrV429X6rumLoyVRYltKoWdc0j2gMoS7ly_sjL5qOO5pdbDlHt5pgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو نازاریو: وقتی به امباپه و بازیش نگاه میکنم یاد دوران اوج خودم میافتم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/96816" target="_blank">📅 19:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96815">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3KiZTMXNgqcppmIOZmen41qthdANfEymEMD_pfwp0f8hVYPxpJN5WjIAYC7SC0GGG0JjV04_qXo1_OaLMMQqPPXOedG7Twpyl3p4ITenPPUHZIi_Lfhs1J_zjibaEK824tWdRWw7age9IcmTSG-A_pD8WRCk-YVYzj2dTQmTz5wQPAOJ3cQmHKHerhcllGRCOPXOGdk7Hl6p-1-YjWlowqLf0GcQl3EyI6D2fC1_4I4bj4c-ZXnbNdzj4mOY5qHdWi3er6539vQNCqC7xunzpq3HLo-esb2Usj-dBMjNyYAfNuFqnP62A_QXVP9B78yLMChuhQac6ncO2DBM21Ptw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
ترکیببببب رسمی برزیل؛ نیمار نیمکت
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/96815" target="_blank">📅 19:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96813">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GrOIkRIAItxbcmMhAS4SpnrTTgs6_PIWd1ig9WbAOs6jQYi61GW-PwTLOm1M6birQDJfAvLuJpTnjVb6bOowPgm62PhSe0tLbzvhjYDNl3RHPrNdu-3EAJNJiRzC5xYstN09q5tD3jES3EwG4nbyyej43z9sHNHsdWdBol8Kj0gj_u4T_ETbgE6_IciaUDxbOUHdrJI3u9UBmQtnmhvFOzrtPmin_50QfRFfxxyJgKabrWspYrQaaRWlyYOx6hQwRkPyfODvh3jE526_SOvwnF7dSLFW2D7imicqWLt4YXFornEpvAbCGABTj9wf_jO_9qIlcQkm4Y_la5_YuvU-6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GduxflbekdIlAdIXtOBxEmZyVvCPNJtTBkIUhz98a4LDp_0gcatWs1F6rOsnY8YxcpnZ63lI_AJTLepCWMZP_UwMXMNLiffNNCQSQ3mOUpzDxo4GkpuYix4n74_UfCgc2qbHcZj5bTr__zNhwc20Tx_L-L0qf_NL8WPsLQ7s7G9offuOP3PduwTsJeVEdS95aXv-7H2uB4WwzsHWFE7I4rbkdSJ5ahx4vqHRwPXwmMdscYD6kFYY0uMWPBkCDHf-K32mJ1JeXT2MHO8iNA2ahiSP8sHBBgwzV7qzl4ap-NBikLXK81ALXcUPjCC-SKrqYw-QHBfjY2KMjt3KEqN35A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حضور بانو ویرجینیا در استادیوم
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/96813" target="_blank">📅 19:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96812">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqVZVDydeOTbaiOTDajCzj97XUrVWLdl3ijUXHkuTuCOaH4aK6JYe5WItRXvaU3mq3t3z_lN5WaPOBG-tMVlhq_qhpeGiWUBOL-Z0AA6GRz8ZvPNsfpCCK9ERUzzWlpPfEsG9eVKmvGKTJQRF6v49VY40Wbzrri5zl-ul8Eutuw05FdtJZKa5UFFKsF5SJDAKb0_DhKj_SDQ3nhNpcXQj_ny4SNZoUQCz-3D3VO7n26ucVXV4z1ipwxj_NUm7G77_ENmGY1zaiC9VEHbFUpkTzGKsjExH2fkuytGLt0gpfFw8sBuXnPhazkHhjx3D8fSJvdFPpv3tmnHDtOFUlTxWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
ترکیببببب رسمی برزیل؛ نیمار نیمکت
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/96812" target="_blank">📅 19:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96808">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m0MtApU-j61JaqCAXSWBa-Yf4HcB24SHwE0wLjXcVkD3lLnuBCf8eAR5mRwIuQ0bFGA00QwIYGbJ1KsUeFkfgCkxKZry0EY9I3tlS9zuXUTDlSsLGiOdakeUwq9RWciO9d4PqW78qzUOydke6jvGrhuB4-sj3bhr-VlJp2bhUrT9REIpfGExmm7-dd0paq1nCIVh9MFsjuO-PsLBr6mLcDVFTU_-DPoiba7RYnFPGmK5JLSpozTrLAMToKOEhJw6nCOuWfRQxnC33o_fekUQn-psBvViSFHd1CwP-eValnJFEV587I0knZuFqI8NqXKblvck5e49w6ADPmhDu6SWKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gOnCohOWBfH8IwBo4_dQAnmAMuEfdrbEuMtrQeW-2AF5kulT3jtdZgr8aDVC1NWYXPkI6-4XGM-cbI4uARbNjejacaN0dqkU9Zc90BG16_-axcKFnLbQ-GP_FB7zNMVDpn5vwJYZ_s033FdxWNs1ep_Inh5nxbF0DTlK6sT8H4nXptu4ZUSUVZudeTisHDGr7FM-6Qo9tR8PUdolmAtI_RRkcYmpMaHNYaKNAa-xEIll3pASBPZ3JYPwz_yEaSNvi37CxQVbvI4K4ZbjWUzX1WQylwHuRQDWerLXn9HeJVXTB9LdTOpFxUXLdFvpj8pgp-qNpfCjVzd8AsFtW682Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ot_FWU6PvWjAY2-22ZUgLxa7w7PjqhdZt6yTtEvIYKoDJRAzdPWglvveaiTy14uDSqns9F9N0rF7JIoOW3T1dzXH9sXPZ7vfjwO3rVslW-VP9I_iIi_Qt8O1it1Ye1tzpDbmep38_Eya-OBnvTw35V-LVLSYkSkAjDgsXWL0EUARnn-wWsFz_cXweaVPXrCSPIxPdHYc1RbwbsnJXgUUZiUj99ClG1KWRDzvzCtvif03_obJtOpelKJxA4s0Au8CXMKDcUM-CMrRllf3a8dvwD05GvwJ6EbhQf5Te58vXNiUsTiloVYiCEYbJ2j_WWVblBETBcjY2U4d17SkT2CSXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ce5XCO1w_gynJJniNzqQ5LVhu-mbvnqw5ql2Xt567-2Tw7S-NQtGDs4zGtduo94UiExFpjbm07ROIYixndj_1JZ0beT_tnYbOWNvLgVBB7T0GZe3ka5v6TUy7dBzHpci-qKlli4JwqpPcRX_F3rPKS4FE91vf4OyoIntoZu5WReCQ1rRs3CcQZyfQSMJylWVTtpgCIs8nKN0sE3JhHKDVXgTv_ZGWltSDGDVPOIuN7ojQwfstPzQUPMxlQXZrzjyIHgSzYF3UR5wBVG9tF3u4EJ_c4cACIQO87H_2GIfzbE6B0GQb_ASWPTJE4r1HrywOBedjVj2GR3NihgDeIovwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
🇨🇭
خانم‌آلیشا لمن بازیکن تیم‌ملی سوئیس هم رفت قاطی‌مرغا
👍
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/96808" target="_blank">📅 18:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96807">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwwwysEcdbiKVBCIReGONjqTDtMghaUuQdvLWWhzZGjA2EgGwPiOgqzu49EkU4MjDitT1vEVhWfzp3oR0obEAiate-jPhLVNyyUFd2kwjnJlktWHSOqXD7Qa_FGJdSq0rL7bHetHQ6bWFqge8vriiZaUqVNDg_TOH92qo2zAqaSk3pZEQN57ynVqCE6wuyQ25CZmhV1v9NG2vVummXeG3lQwMeHu5SYK1hEX3nRkmbZ4W6NT9EypF8Ojn3unqdJQCIw5HqHLgaPGX2aXGHS8EFXCosVpGRWGr4i5PvNX1rNOgGl8Zx9ConvUiFsLOzYPLCdilMJN4TNldtvYp6_tGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار دو تیم پرتغال و کرواسی همزمان با اولین سالگرد درگذشت ژوتا خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/96807" target="_blank">📅 18:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96806">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c36f5ccc71.mp4?token=vkCj_BiOgPXROeDeGuVZ_x1tv-SreQdcksQZs2gJMqK-xT5htGtCr-LmkX3bDjbyc4djFrW0SyYNgKghVIX8hkFlFE1oQjxgq1KIjopZ6xUmsmb1VKCa1aMIDj4qTm6aUF2pGlFUcmWDgwEv2lSAxX3OVi7gv_3MlBfwY9vMP6HwzIaWf7Q71Qw9mf-AvSHc5AH_CW4immtuT0zJyenP1xcIRa67t2a7MN6ZHj09bAlYCxAaXasuFA92oRxQjuLjbsf9O6QgSnrQEMiQCfbtfPUp1DW413WQABWEQfyDnpZIbTk-CQQVFkNCScDgi046mR8DDJNjenelyfacon8RLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c36f5ccc71.mp4?token=vkCj_BiOgPXROeDeGuVZ_x1tv-SreQdcksQZs2gJMqK-xT5htGtCr-LmkX3bDjbyc4djFrW0SyYNgKghVIX8hkFlFE1oQjxgq1KIjopZ6xUmsmb1VKCa1aMIDj4qTm6aUF2pGlFUcmWDgwEv2lSAxX3OVi7gv_3MlBfwY9vMP6HwzIaWf7Q71Qw9mf-AvSHc5AH_CW4immtuT0zJyenP1xcIRa67t2a7MN6ZHj09bAlYCxAaXasuFA92oRxQjuLjbsf9O6QgSnrQEMiQCfbtfPUp1DW413WQABWEQfyDnpZIbTk-CQQVFkNCScDgi046mR8DDJNjenelyfacon8RLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🙂
💥
خواب دیشب مردم برزیل:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/96806" target="_blank">📅 18:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96805">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUIxZ8IVKpdrN8P8SoAJNKRrmGR_W0Ln3vQCzJHhSVWcmyznizm3i5I7R5mwNJgBKa7x8BC7uOgMbD39YaB6gRyWbRrvUZNsuQoQazbjgricuvtLUD4Hx6-B66k_SLTzCC-HoKSMTn9Ykz-BTcEZwNuf8Z_WhnMdSJwjwln2Dpfx270MlulTGkUxhiYEYo-gzOYD06EcyrNR4ycK4V-rrbEYiReuq95zNSM6cYlUmoftma7pl2E8U_j7nLL-kRtvd8mWPPWaZpNDzd1p-QNwW6RtcNb28c04AvMSqMRQ7R5L-Dg6rDXdlS4-QbrzKBbb7Ns7-sMbtBypV9C-3imx4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
68 سال پیش تو چنین روزی، برزیل برای اولین بار با پله 17 ساله قهرمان جام جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/96805" target="_blank">📅 18:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96804">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دیس ابوطالب به جواد خیابانی در برنامه جیمی جام
والگلد قراره یک کیلوطلا به شرکت کننده های بازی جایزه بده
و اگه میخوای برنده باشی کافیه توی بازی های پیش بینی جام جهانی پامپ بازی کنی
تا فرصت هست ثبت نام کن و بدون قرعه کشی طلا ببر
اینم لینک :
👇
👇
👇
ثبت نام و دریافت رایگان طلا
کانال تلگرام
@pump_vod</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/96804" target="_blank">📅 18:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96803">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YiiDPVzpR6U307Kga_YXXGzDiR0b45rlCV5fMd17Hvla83W4VC4BoWRi_3cyzKKjhxXO-cSC5qzSOZ6D-T40-EVkVTz0oxQ7pSrZfYCpHt6kXqrevQmMEwAnjQsOBDuTX7IOzK1lUyRQdOdGABjIRu5VlkRD_-VteioY4IOUwo5AocNzUziVmZUaGUxFa6w8ENRHF8sAzgQG8S2IF7LGGwkCUkun1gpchdE-sPO0ZFfkT97_4_5jh5_JnXoD4k2rvbAff9wQKEdBetRbkO67AY0xvddqORNwt1983F_nMoZsuHknLiBHr0TgTO8HPE7IxImPaMfZKhxM9KN04D50sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت هر قاره‌ تو جام جهانی 2026
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/96803" target="_blank">📅 17:54 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96802">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MX9rzMV21Hy69nWBHQYG4pura4vN2FCjeDxTlJK2b4v4BuwzNaX2bETE4I8q12p5wISujqYBpVKJrgW531CPw06kLQsZSaHbc2HecGKRVlKoNXtSRViNTeRegES1xQlxWnUYop3TnWMSga6Q4t2vPgG3dKvqvvcJnYKaZaWkmT1ucftZmCsrlkO_zhoh3iWryJCbbeBnXHxl02fvEK-ZVvV9WBLYxDs9Ju4QKTK9o6-lm4JmjtYCZEfZJM7bVCTOjHy2vPDPtHbi3fI2Qj-Qbwr9-EpMOtNUJs-8x_6d5RX0l7Dq5KTK_7sXPI-okglQMX26wqYSOxM12S13XftOdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فهرست بازی چادرملو و گل‌گهر برای تورنمنت سه جانبه آسیایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/96802" target="_blank">📅 17:54 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96800">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dEXSquXFRcod5bF1AkOoog8ziUJNpTvWD538yjo9XT3hZhIVvhZasgvpUgkTVU98KSsJ9H4fCnMHfGp4M-PdnPG3_l6ONqZ9RtS0hCKMYDddmi3x6enyYdzzlD2O-dM2Z840tE3pR-ku29rJw4Dv8N0iuiYeX_r9_j_gpWLexSCq62RYMX4UfWfXIpkyT2LNIvZ9I6_q6umRtkNHhJ545FUFJnLwLOmt2k66AsoeJ3P7XdyBVl3DmOi6hgRGOZchD_gHuBPH9PX0iqMIssTfgKxf-0TkY1IjRtT-TD6TuiuxyghCDgX2sAVg8DWF_MklMfpJp400r05Xe55fqyHnug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FjlGMoMdJbTQBCT6nJ9_IlY1Cl-BRFtK4ZkNrmV1QyPaSZZcocE_xuK2PUe7mfCyMBgB9hPRFSR9RHOZY--aHhny2bbGx0Z06UFXjioXwuvVyGAolEZxGVNNuJCsbAwxvv5Ue3gfGLyaKgPkY8pYX0_io7WqTv185C76sw7BVHSHc0lakHZKC0s3RHWVzHpq7O9n02U4IHNt4d5xa956piaOcDRJVbk08OhPxVfhuMUtxfHQ9Y2CTv4sZOgB7uwuD9_wgmiaYFe250OI9-NG02-1arbWjN4hdP0fmrKIsI9yld76aOpEMW9-1Rpi8LMNJyI-zyxS_2B3Nm4klnFQ8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
🆚
🇯🇵
🗓️
۸ تیر
⏰
۲۰:۳۰
برزیل
🆚
ژاپن
📌
برزیل مدعی قهرمانی یا شگفتی سامورایی‌ها؟
⚽
🔥
برزیلِ صدرنشین برای ادامه مسیر قهرمانی به میدان می‌آید، اما ژاپنِ جنگنده با امید خلق یک شگفتی بزرگ وارد این جدال شده است.
👀
🚀
⚡️
آیا برزیل مقتدرانه صعود می‌کند یا ژاپن همه را غافلگیر خواهد کرد؟
🔝
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
🚀
پوشش کامل بازی را در بتگرام دنبال کنید.
👉
🌐
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/96800" target="_blank">📅 17:54 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96799">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPwj7ZHa08EXRh0s-w8FesTpwsflUhHDWjwNOTi8S9NM8wizMtp28DlErj9sAYXnyNyhzz1Kj6-UUFz1uOi8xrRVqSrCbFQtBOQ9p-QWKvwuXECixbZWSSKld_zNmk-CSBKronDph5ufx9lEGLyB4xTFvt5EyV5H0o8JrgMcQJ9w71KrjMtMlqRsQZD1m13KYMFGWUQi6FTzpvwSEBrzyCwumvzU2jjhP_KC7DG7gtV0kCYnZDSyAreSPoOCMJ8aG6GflFA86bEw6Jsq8ns6ySODLHYKAmUYV14q7hO1V_9WhpeuTc8-K_wjKw9yEy3w0-3FC4JnsFzbtFjGL5oiFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
فکت؛
فقط مسی، وینیسیوس و صیباری موفق به گلزنی تو تمام بازی های گروهی شدن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/96799" target="_blank">📅 17:54 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96798">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🔵
با اعلام رسمی باشگاه منچسترسیتی انزو مارسکا با قراردادی 3 ساله به عنوان سرمربی این تیم انتخاب شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/96798" target="_blank">📅 17:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96797">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVN6p1R48QkaGRBx4DoElGRO9qiiNpi5UzQx7_nWTmLb7EqQGOI8lXrednGfr930qk529rwtmSKgDL0MuPeWgWyyBlAfnlmOeyPuFl-51nnZjvRtAsJfz7f9OXQIqkA2QD7CM3iAwtaGoaLEArE2IE_oVAh63g5gk8jbyplm293ctM4W8aI11ZoULFAyLfmA2FtNsAe816axBd7pj8N0DUgGTVqK30ptQwjCpt3FPw9_TKOCdLtkXrXwh9gM_zibf2QO1pUk2dNlwOdyyejCNuFppeoaFiwNeT0fW56vz250aq3W1eLuAheO353csc-RdnXfRAynKhhKkrqoRwmreA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🤯
🤯
پشمامممممممممم
🇪🇸
‼️
رسوایی بزرگی درباره بازیکن اتلتیکو مادرید، متئو روجرری، امروز صبح فاش شد، پس از آنکه زنی پیام‌های خصوصی که او از طریق اینستاگرام برایش فرستاده بود را منتشر کرد.  طبق آنچه منتشر شده، متئو روجری به ازای هر پیام صوتی با محتوای جنسی که…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/96797" target="_blank">📅 17:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96796">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f6c4d178e.mp4?token=BTRpaAYfmkQVgQsNk4z8rAX0BgDRpl0TKrk7-BeiRZxCJMgQU4rkbpKVj10OliDdgWUfJbEfdj5U_v3t3vxnFEih2MVLnTA7AdL3RyxO5gbb5ivd_agcQ2gb_TfJRwX4oUDaXNQszw_oPjt9b24d9Giu3eCZ7d8Dx-xiaOzGnPHSBBIkeQM9Vpa0P8AEL3rNL46-XfQnwpafj2KrlYG0sIAKoS4BIv2_jyiPn75ssQfLiYw4oeF3QhlkqdLBNXxbtAACnN5jX4FmtKkz_5jXVwRhOGvVVCtmRK3sLKXmUHFJOz1Q6M_3qbh83qgkDfOMN2h5sAc02HoY6ZET-jZiwmS8VJcSOHrEWFbq8ephrCHLk6_tTPK-0hnmRGmxFIwulzT6cEYs_TuNltgSHmuE-vDMVxBDMO6JRGCSRQmZ7peCQ4yLObaSsb_FZV1TL6e7wZbEaI8sjMZiM5Ehl1GW653u0MuxrKp7KAFC0ZLgBmvey1MP7kJaSjPr6i75dNzPqhNhTgzpatJll9NMvabdAv84YajdpyalhTSoNb0wRvUn5GeyaqoXznXJZgO0OyUfv4xHXBgXQzOFC1BeaRMt4T7G9MrU5pTS7NGUinsmAYvhXSxwtHVg1lBFVy0_2Td9Ndu7gRoOk15wD9xT3SuudhK8qRCC-s_T8jm6ppuPajY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f6c4d178e.mp4?token=BTRpaAYfmkQVgQsNk4z8rAX0BgDRpl0TKrk7-BeiRZxCJMgQU4rkbpKVj10OliDdgWUfJbEfdj5U_v3t3vxnFEih2MVLnTA7AdL3RyxO5gbb5ivd_agcQ2gb_TfJRwX4oUDaXNQszw_oPjt9b24d9Giu3eCZ7d8Dx-xiaOzGnPHSBBIkeQM9Vpa0P8AEL3rNL46-XfQnwpafj2KrlYG0sIAKoS4BIv2_jyiPn75ssQfLiYw4oeF3QhlkqdLBNXxbtAACnN5jX4FmtKkz_5jXVwRhOGvVVCtmRK3sLKXmUHFJOz1Q6M_3qbh83qgkDfOMN2h5sAc02HoY6ZET-jZiwmS8VJcSOHrEWFbq8ephrCHLk6_tTPK-0hnmRGmxFIwulzT6cEYs_TuNltgSHmuE-vDMVxBDMO6JRGCSRQmZ7peCQ4yLObaSsb_FZV1TL6e7wZbEaI8sjMZiM5Ehl1GW653u0MuxrKp7KAFC0ZLgBmvey1MP7kJaSjPr6i75dNzPqhNhTgzpatJll9NMvabdAv84YajdpyalhTSoNb0wRvUn5GeyaqoXznXJZgO0OyUfv4xHXBgXQzOFC1BeaRMt4T7G9MrU5pTS7NGUinsmAYvhXSxwtHVg1lBFVy0_2Td9Ndu7gRoOk15wD9xT3SuudhK8qRCC-s_T8jm6ppuPajY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😁
😁
ایران صعود میکرد اگه اینجوری میشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/96796" target="_blank">📅 16:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96795">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqzFSYUNhC2rVw6YaTbimDCNL4NmCunV1_2ElVMQrwiPyb3ouqpOGyoZ2WuyS2UgeY_j_KgMCU6DWTm77WWhxr0ZVp5pnQHnKebI6hmttSpH0UO6KmnXtwewpaT4itQWutpieZ7ZrYEjxrmcCIN-wKkOshCDmhYxYV9OFzFLxnSbd5nnkkAqDJDFzBYEb-6TiGeHFYvRUjPVeAeg3X5LVjfcsBf7XPzGpgznBixXUD3wjHF7ThUfEaqMTL9Wiq075ynMH1QQO8TUvyJ4LgDR_3rPm84aN6535kIDYoaqt3ttu3ef_vkF9szrKoanhOut8orivU-2_J5mszpxu6ADjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
با اعلام رسمی باشگاه منچسترسیتی انزو مارسکا با قراردادی 3 ساله به عنوان سرمربی این تیم انتخاب شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/96795" target="_blank">📅 16:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96794">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SebI1XZr1oPJbvNjcfT83NfPuYPWew7B-N6aFh08XaOUqS52FBxAft1CnoWBeDAdAvytjGvyKpbheCyfU6KppoeL7DF84cXyHqzRWD1QLU9xrP28TDIutuNqQdKZ2y9WQ5x9v5IV4QkUBD2HO9uq3Wsgr3P6z42TEUAsoYV8AF9xtyR3p8i6YQBO7pMwoJMwM2mSXilEMDO8lof3j6HVglmvle4LoA_vk2gDNokPb1yo2_YhEJiaWVLGBKuEn_XsyRF74HAscL4ygRGAmiaCGX0h4Sf956uosCjKP1VJ8hyPNpshXYwFmAPMtO1iH3mBnVuYFjEA4Tj3eX4_HMThrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇦🇷
لئاندرو پاردس و همسرش در بازی با اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/96794" target="_blank">📅 16:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96793">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09f8bd84ff.mp4?token=BUnVcAn1tf3DMPpyuvyOZ1YLbbAkeDafxgvu08LRqf6EE01r4OFEulHEnufKseyBEctIPd_0pmDpsqTV3-Sy_DkL-IMG6JIfeo3lEOgCOHJVH1MqEtfOIZv7IQwH5nyGl6OcMuy3sZnYwfsp20IN0_eWXSlXNAh3mga1upSr1aaS11ptFr-2YU46kNok97L-8pnoiL6EqBTeKGPDfGwvUQqjaubsWbk-bTWDq2IhDJD54YyidxlKyEStwVFMAj_yzjYxe-FCsFDV6C0i15nZgVKa37DWquJQ8bZopCH5CD3lmXau-ajcyATXgksqsHBtCTo8W-myVtcbAeRSPRTMZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09f8bd84ff.mp4?token=BUnVcAn1tf3DMPpyuvyOZ1YLbbAkeDafxgvu08LRqf6EE01r4OFEulHEnufKseyBEctIPd_0pmDpsqTV3-Sy_DkL-IMG6JIfeo3lEOgCOHJVH1MqEtfOIZv7IQwH5nyGl6OcMuy3sZnYwfsp20IN0_eWXSlXNAh3mga1upSr1aaS11ptFr-2YU46kNok97L-8pnoiL6EqBTeKGPDfGwvUQqjaubsWbk-bTWDq2IhDJD54YyidxlKyEStwVFMAj_yzjYxe-FCsFDV6C0i15nZgVKa37DWquJQ8bZopCH5CD3lmXau-ajcyATXgksqsHBtCTo8W-myVtcbAeRSPRTMZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
👀
🙂
این‌خانم نروژی بدلیل شباهت زیاد هالند سوژه محافل ورزشی اروپایی شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/96793" target="_blank">📅 16:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96792">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29b044b968.mp4?token=lQx94P9DWo_pvQ4UQv8DfyShVBhxkuh_nb593GyvDitVFgLlNTcb5hQyfo0WasG54mWsOkgaXHD0PpLuSbTH0NNb6GVmehk9tElbCBVkre8ymr0LKQB7CduklquB_R60evNZ0c3fuzwSNzZ6Pnu-feustZIrYECNTbdArCIF9XVS5YdFN5iNjrBbLCimBFHiAY5yii-ulSZ2Lisvpc9OybTIriO95_4GLciW0NhlZK7IEczcyKWpxyhdjuCc98EgzAk-_Ln6wfQ9Y3WBjoWohYtvHKZojjej4vjXbmUVZVLn8Qj6ekngotphTmjwtRRcSYNjqYMb6_0azmondGq4OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29b044b968.mp4?token=lQx94P9DWo_pvQ4UQv8DfyShVBhxkuh_nb593GyvDitVFgLlNTcb5hQyfo0WasG54mWsOkgaXHD0PpLuSbTH0NNb6GVmehk9tElbCBVkre8ymr0LKQB7CduklquB_R60evNZ0c3fuzwSNzZ6Pnu-feustZIrYECNTbdArCIF9XVS5YdFN5iNjrBbLCimBFHiAY5yii-ulSZ2Lisvpc9OybTIriO95_4GLciW0NhlZK7IEczcyKWpxyhdjuCc98EgzAk-_Ln6wfQ9Y3WBjoWohYtvHKZojjej4vjXbmUVZVLn8Qj6ekngotphTmjwtRRcSYNjqYMb6_0azmondGq4OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مود پسرها در آخرین روز مدرسه، بعد از اینکه کل سال از اون متنفر بودند:
🔺
دقیقه‌های آخر زنگ آخر؛ زل میزنی به تخته، به نیمکت‌ها، به همون دیوارهایی که کل سال آرزوی فرار ازشون رو داشتی. یهو یه موج عجیبی از نوستالژی و دلتنگی میاد سراغت، با خودت میگی: «یعنی واقعا دلم واسه این روزا تنگ میشه؟»
🔺
اما این فاز سنگین و کلاسیک فقط تا دم در خروجی دوام داره! به محض اینکه زنگ می‌خوره و پات می‌رسه به بیرون مدرسه، انگار یه آدم دیگه میشی. کل اون غم الکی جاتو میده به جنون و آزادی مطلق! دیگه نه بیدار باشی هست و نه امتحانی..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/96792" target="_blank">📅 16:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96790">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pNFdtFf5EatZBh1zprR7k9vZzAmNiaE0oa7XU0342Xc1njokYk1EgKcvlc7Mk2uZT_Rczg5r6WYq7f783l5xTfGs8Yl5r-yTDm7aXu-Olu7C4LbuHtsy2GUEQiGBGp2Y229sIDPlsiIKJUnma-v3UElzTD5AFvRVN-L1gk1d6uUAw3S_28jQAU5Tz4wSOMZd0wiY69jrfE-9qNUl9V3T0ZOCfbNpQAAzFVj9qO4kIgC4iXQ0OFcC1tkiUt8DpzaJFk9TlrzgJzJXInGD5eGxaOiGJLuw5Xq37iEUGWrn6oXX4pHrohhA7cOoAwdLjlig0RxRtVjvvbev7nMGRBqPmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QYAbtdVtTLRjhqbL2Q_TrCM8-_-T8FzraLss6ZWVjinpdcGWGaRhHAdCJCz52-4EPXebYO-STt5HWeXSAJDrwl-yw6OHOUm0wPRikX_Ggyc_v2oFOKAnHFGUwNSPxk3f5AIlCxo4OEKWPNGK2fJhaywUIfxAXftvx84y0sJwmKIup3ACxMFECTSGY_0U5NHX0uYJUXTrCKddnGzjNXMgljZocfPSqzJFxPoqKhC3UrQfkPKMUpGUUzgCJ5dv6wdKCwYw1OMrZREuf0Tw4lta7fMKkkRJrBLqEwi3N7ddSUHhl6h2haLKQwKW9elt9gQ1rVqWngTk0idUDnpO0oLHoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
🚨
⚪️
میگل سرانو:
مورینیو به کاماوینگا خواهد گفت که نقش بزرگی در تیم نخواهد داشت، و این مقدمه‌ای برای جدایی اوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/96790" target="_blank">📅 15:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96789">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hhjbzu2n0KvduF1yiRagsIetlWM530aAnHNwnh-0eSs0Rq9ybUCknsvNiZhc0BqMDJH8n2l0PNGIqy1Jo-Ret2Q-76P43rX2sEySjNuux05ihE64P8IuhTQdMAI5yRI8Fc4pzaJJEmkxYaeVwYScAGg2fsbx-nHzAXnsV4TGQccwP8YjaPO--fIfdGBAao2VhQh4qSCwaV7v_8FQ1cbfeO708xsWwzyPAyBe2sbKN2YIvYQxBnDxjPgrzS3uZE4oYYSviumSlnYM8heM-JA6hZUsWeX11RXeEDbUFaTaS2H9sqHEFFIT9gAapuFFkqxR45wWJNDvfqJgYYr2S8porw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست اینستاگرام بازیکن های کلمبیا بعد بازی جلو پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/96789" target="_blank">📅 15:47 · 08 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
