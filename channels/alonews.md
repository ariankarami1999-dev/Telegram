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
<img src="https://cdn4.telesco.pe/file/J5JFblfJNQ0YddQag41ngFPQkhZvh2zSv_kGiAH0vfEVFePHuXB8CzSGsoUWq1K4o3DPntHCy4ak969KYBLI5w0fW5qIz6KgeXTpNzkjXRIGpSQBIkyNnlqNPmu264xizUyvl-oyzyXMOMHAZIYEIPoouNlRQ5O1xdVXVbsYlHAkZ6o756hDQpH9xHeZTuIbeHRP613B53TITNdDQJ-F-CGfbSQd3e6fk0Xqxi11-QUKazIxm-djYhopthDO8ECfOefsjT4wQA9shx3ZwVnEzKUP0S1r66WZ2oV_LwcE4BS5AkByp29x4t_uU0R_DbmQhxLHyN1kHh1lmAgq0R_lJA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 971K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 12:35:58</div>
<hr>

<div class="tg-post" id="msg-125478">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
غریب‌آبادی، معاون وزیر خارجه ایران :
آژانس اگه روی بعضی سایت‌های هسته‌ای نظارت نداره، به‌خاطر حملات نظامیه، نه اینکه ایران همکاری نکرده باشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/alonews/125478" target="_blank">📅 12:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125477">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfNt_0hlczSSyxx3lRhFxfmzFa8mZSQz6igTWrrIV6z2izIARiqNZrWxhD9dZIhAPLGBa5uuezy1OdP-ngIaPuzz1juwxpOQsc1d3qMbVBfnL6GE6l9E5uKJL6kAUq7u8lFMKZWsyi8OTSVk6vfFAc2Jvpqsds9DAw3zi3uZ0PilcIbtL4tFAYuKyZcFeJux7EwUlI4Sv8Nw4FDH-CRLRXNeilvFb1afLsiNDw9h5GlEaYlgKdAkvjdGFn8bQrzXqTccZFDuG-W0soHcnEo1ariwFCm2xV7d5rJcIH1HvSalqKmqqyWB32zdDsWQN6ySNc8EZECHRr4hh4bLOqumYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل یک سرتیپ ارتش لبنان و دیگر پرسنل را در حمله‌ای ترور در جاده خاردالی-نبطیه هدف قرار داده است.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/alonews/125477" target="_blank">📅 12:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125476">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
ایرنا: وزیر کشور پاکستان امروز به تهران سفر می کند/وی در قرقیزستان طی روزهای پنجشنبه و جمعه، دو بار با اسکندر مؤمنی همتای ایرانی خود دیدار کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/alonews/125476" target="_blank">📅 12:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125475">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
لاوروف، وزیر خارجه روسیه: روسیه ناگزیر حقوق روس‌زبانان در اوکراین را احیا خواهد کرد.
🔴
این یک پیش‌شرط برای راه‌حلی بلندمدت است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/alonews/125475" target="_blank">📅 12:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125474">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
گروسی: ایران نسبت به ما تعهداتی دارد و باید دسترسی‌های لازم برای بازرسی‌های ما را فراهم کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/125474" target="_blank">📅 12:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125473">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f714df4f8.mp4?token=PfK8UXjXH2-PuSuzxEXrrOf_ZgTjue0ENdJn-4hQkEjr_bQW3XT-OB6ghBMnRcURr6-dx6Gx37oE3DSk0E9XVb87VLcwLQd91YDIrLWiD1gcHSv6mjbwJejLxAWQ0rzVRM30LH4VT4RAbb1ifnFsMYrUQO5LjENHrowZkdy9lXZD9O1TqTMycON3qqeXRllXdfgNe2uI00nNBAWmhussja5RSF6YPrDIDn8c2qm1ZF6sDARSBiEzMIVhJ9sz1Qr35JGSnF-Nc_4kge2OUhRBYCeNaiVKw8QSDewd5mZjo-qvEF3rZSsgXKpinm-WqZvcmF04g3CmQLNrFPlSOgS7wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f714df4f8.mp4?token=PfK8UXjXH2-PuSuzxEXrrOf_ZgTjue0ENdJn-4hQkEjr_bQW3XT-OB6ghBMnRcURr6-dx6Gx37oE3DSk0E9XVb87VLcwLQd91YDIrLWiD1gcHSv6mjbwJejLxAWQ0rzVRM30LH4VT4RAbb1ifnFsMYrUQO5LjENHrowZkdy9lXZD9O1TqTMycON3qqeXRllXdfgNe2uI00nNBAWmhussja5RSF6YPrDIDn8c2qm1ZF6sDARSBiEzMIVhJ9sz1Qr35JGSnF-Nc_4kge2OUhRBYCeNaiVKw8QSDewd5mZjo-qvEF3rZSsgXKpinm-WqZvcmF04g3CmQLNrFPlSOgS7wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملهِ هوایی اسرائیل به شهر
السکسیا
تو جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/125473" target="_blank">📅 12:12 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125472">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
زلنسکی: این جنگ باید پایان یابد. اما رهبر روسیه می‌خواهد به جنگ ادامه دهد.
🔴
شب گذشته، پهپادهای ما حدود ۱۰۰۰ کیلومتر را تا منطقه سنت پترزبورگ پیمودند و انبارهای دریایی دشمن و پایگاه کرونشتات را هدف گرفتند.
🔴
قدرت ضربتی دوربرد ما همچنین حدود ۵۰۰ کیلومتر از منطقه کراسنودار را پوشش داد و یک انبار نفت را مورد اصابت قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/125472" target="_blank">📅 12:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125469">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d49e89d4ab.mp4?token=DaR_YauX4xcztQW7nmatgQMtF8uyD7AVjrurq6QvPjZrh1E8uhW-7bNrZj3r_AWSHZNLvfZuzvRO3rgd70vtoNZYsQ-v1cBXwBBD67RdWpgE5sbilW70TrvTbRjwWWMsSA1X1FKzbLIZ1Wru4WCM4xUTIVZX4b_ppsnfZ7M2_UE0cf1d6J6Mk2xM8Mie4iMlmBwDryMgRozGes6Fe1ij6NHgzvoMzgvCliAx3cvPixcxMLg1G7dnS5oxlGqANOi_r2vQfecVvDak3uoHdVjVNWcl19YzpdZZqsIMmBGySJ3UU13oAvL_ez5RUuNPPFXCxzTCoFXDtqM0CpnK-h4s9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d49e89d4ab.mp4?token=DaR_YauX4xcztQW7nmatgQMtF8uyD7AVjrurq6QvPjZrh1E8uhW-7bNrZj3r_AWSHZNLvfZuzvRO3rgd70vtoNZYsQ-v1cBXwBBD67RdWpgE5sbilW70TrvTbRjwWWMsSA1X1FKzbLIZ1Wru4WCM4xUTIVZX4b_ppsnfZ7M2_UE0cf1d6J6Mk2xM8Mie4iMlmBwDryMgRozGes6Fe1ij6NHgzvoMzgvCliAx3cvPixcxMLg1G7dnS5oxlGqANOi_r2vQfecVvDak3uoHdVjVNWcl19YzpdZZqsIMmBGySJ3UU13oAvL_ez5RUuNPPFXCxzTCoFXDtqM0CpnK-h4s9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امروز در کشور، دانش آموزا به تأثیر قطعی معدل یازدهم توی کنکور، دست به اعتراض زدن
🔴
«خسرو پناه حیا کن، کنکوریو رها کن»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/125469" target="_blank">📅 12:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125468">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYyMWk7GBJWmkJsMP-9KoC4xwEGEILAfWXIMsDNa0yPAz-sNBHLpD3KNEBTFs3HxWIatL9wlGsCeDejBwoDz-46pnROLd9fuGG5T2QyOesFO-GEmYef_tlhRgF16Kn9JuNMLd9PLr-z4KcDlI5Sipu-owu82qQz_j48VfXh0x4vB1qe4YGh0EyM1ZaQ4rzUiW9Vlx802BXpZGd9EILnYESHSwevqNkwvQ1EUQ-UAiJrmZhDbyBzJW1J2vBICLMV9krW3KJRoFFFRPdJePZCQ5Op5RIta4kZxdLRiNEF810CYaVlwAlbfCfs5XWPM-PvyyHDDlHhXxmPsqRz-67Sh6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تریتا پارسی: به بازیکنان جام جهانی ایران ویزای ورود به ایالات متحده اعطا شده است. اما آنها شب را در ایالات متحده نخواهند ماند
🔴
آنها در مکزیک مستقر خواهند شد و سپس برای هر بازی به آنجا پرواز خواهند کرد.
🔴
این بدان معناست که آنها باید در همان روز بازی از طریق اداره مهاجرت ایالات متحده از مرز عبور کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/125468" target="_blank">📅 12:02 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125467">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
معاون وزیر بهداشت: بخاطر قطعی اینترنت یک رتبه علمی در جهان نزول کردیم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/125467" target="_blank">📅 11:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125466">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmL_qYbC4V2fNX5dsrjTYzkyPjadMR5Y_PoHVnVzBlOjb_YNeg1RU7cwbHcMIZ4eBAUlgfxM6Qu0CxU2bfkGoKMfCfW4oBNmEoAROiw-FAi0r70-ONx4ypSofrP5oi-9_zH5D7H2MMDTJovPIGqDixPE2E8PJ_nC-azfk9nFD1Na8_QJVoz4h755QvzBnILE-z16w86Sz0hLo86WdQs6IfRecmAwyB_KY0fN6FMcjWjcvtbeMyRaSVPIHWwrdku9mDw63Xf4qeaeYoo80BMRSynDPtR71LAsXRbxcA1RujA5I9KBtpCBb74W6va7VneYV3PvJ1xpQiGl1XdyO3CJmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اینترنت مردم پاکستان داره قطع میشه بدلیل اعتراضات مردمی!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/125466" target="_blank">📅 11:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125465">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
مشاور امنیت ملی عراق تاکید کرد که ایران پیشتر اعلام کرده که عراق از محدودیت‌های عبور از تنگه هرمز مستثنی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/125465" target="_blank">📅 11:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125464">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
سازمان هواپیمایی کشوری کویت:
از سرگیری ناوبری هوایی پس از تعطیلی موقت دو ساعته.
🔴
تغییر مسیر ۱۱ پرواز به منظور حفظ ایمنی مسافران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/125464" target="_blank">📅 11:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125463">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
تهدید جدی تاج: آمریکا ویزای همه را ندهد، به جام جهانی نمیرویم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/125463" target="_blank">📅 11:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125462">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
ادعای آسوشیتدپرس به نقل از مقامات آمریکایی:درخواست ویزای برخی از اعضای تیم ملی ایران به دلیل ارائه «اطلاعات گمراه‌کننده» رد شده است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/125462" target="_blank">📅 11:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125461">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
رویترز به نقل از وزیر انرژی آمریکا: کاهش قیمت بنزین در گروی توافق با ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/125461" target="_blank">📅 11:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125460">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
الجزیره: ارتش لبنان اعلام کرده است که چندین سرباز، از جمله یک افسر ارشد، در حمله‌ای اسرائیلی به یک خودروی نظامی در نزدیکی نبطیه در جنوب لبنان امروز صبح ترور شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/125460" target="_blank">📅 11:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125459">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
انفجارهای کنترل‌شده در جنوب اصفهان و بهارستان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/125459" target="_blank">📅 11:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125458">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_i1TH5MJ617Sl3ITIYqExaRa_jcyhfscDYGIr_9r4qOvEJ2BiHfvSufPOHNZU1k-Kv-KNN7-VvJFECBsCyKx6aEYDgUtJgPDIp-5EHXIxk-G7dEL52qJRWFMvjIcwecLSEJC4ylRDA8m2zUGavmjS3pZxDnnSNxhVuZVp5OCt-HS1Unct9ndciaUDOIBXEceaiJ8poGT8dQxD-erHblU8xYZAEBFnqeIKFQPXWWBarJbbh1dpM7Z_d-swiq4cwlBEiviCa6MpgjAHTy6SwPLvT7PgVLIMPmWkvdU3GJtSyj8eHTxf74baXP_26t0IxPijbHEM-v1GEP3eyhKHz6mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت بورس مملکت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/125458" target="_blank">📅 10:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125454">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SADz6sfRQinaeSLvSLV4Ha8y-sPv_0py5nQ4Q1qUbyBXVWkHAd0-pDC1eWTjcKpVr1y55rUneSjQUGZ-nMUysQmsFee2kvNyAbHGHCvxBrjU5HBQBxYsyijWJe12lb3lIyLi-lUsaMqHLNGe4p1X8sJCE52yMyCD9naN_CnWBbuCPEjbbdzliWPgyYJ3fuJDa_lOyYFp4H9LpcTArqiktrtUfsG4z3NTnIi1DG7soeUOpoaHX_hB_57GOV9PLuAkEKlat49cQ6oY6frinTT9zpdBxWRNTpJVIxFlpcFMEdHiHd7yeih9ZCQqsCMVjZw3pL08NLtCmqHhxDp-UVOaJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gT8_5uALH_YayelNSiSejJxrjghFIq_PBNCiTtriC8OVRm3J2CKcH1F2SZwwF5Hnwc2iqd7edj69Z1-e6soDGGbxZa4OH1FhVz-TVZAmtiogOXaGcoiJB3mJRK-r4wfvQJVx4DgtGizrLhWCngAsYqCyJzH1rQCQqAt_t6ZZnFYvXmXy03maRP9qC7uF4nKPrXuInIDx-LH5n97d8ylhte2FaMopqV_1buwv8a4D_WIiwSPX4Fm8TLG9wnNqizcSsS1VRdZcbbPVAl56to3GsGVovZ3S8f0LKhpCy7EykhvEe-RJMJyuxaLShJ0kVrMHtqZPKv4XUXAUZKPsVKWZfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PexPr0RFRAlN5KNXp1_12Yyhxvx-nP6QhetS08Z4qejz4Zyf-veqSyXlsxxBgRmNTcXYH81DbztKKJ6JxM5i1tu0gn7a9XCiEND68DgP4k0B8gHwua40QcgzrSgp8j35vZML1UsTS3-jbOS-ReJfhmKDfK57lGDx-kFEFV9GmRz9NWYUfmWSdcchcZavSdziu0J2k73NNKp252wtTkmXYokyrCogi8JLtjN7tbMeHnAiUxSpNGMgPgI-czcGJFDAsnFs9UMy8Tr778JhjUwqEGlJOO0Obd7eTrGXZSg96eG7PBAJ8Ztb60rnFlRYEaHGDbdwujCqNDr7vnh70DZtGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p-8sqdclMylQVVapfxRlFr4DKPW3SnE9IrCvwuSKBC6K2j8ELfwBFlkL_Gd5yzoBMLGMc2zy8Q59sFl5dMCq0nik6chdWWvJouJRqLgF4e1ZedeOdOdJfrDH2g9FIBXbvae3HpT4DBDud4z55XuOxRbqwibqsjCvXcjAkx1DvDe8Dbk6ct-c6oqz35-FSTsvqgUC2YxFZzcabS-YBXjtJBOYpFwK0b8whIIxf-Af4sqiJoUuy5Tgy1_TMz2ThlTpBCw2zHeuNPG8QsYYxi0Zvd7EsoTUcVPTnTQG1fpAGTtMhndSX5J9FCvqaA5_uFGE9G9Ous5Sa-umrWhAXjmsww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
دیدار فرمانده سنتکام با مقامات ارشد بحرین، قطر، کویت و اردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/125454" target="_blank">📅 10:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125453">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kYUVkjRkQ3HOswY7DSx2nwseiQzQw8pIXzWi8S1tUDIlp_HCczzRd3McWZ-GaBckonzX-EKOP-zRngg4ggmcV4Qao31NWDwjzHxU2e8cbJ-KoVTwHyATQRg0chJICHIrkf14EsXnbMgIfiD0w3lgT2i8fLY0Ln-luySQtObG4ee-hNRyCS_WV2zZmWejMYVpnZHig_TbklgnLsDdB5STe50L2SFCTX3iQmLDbMf59rnGvTJmIVZ60aV7wcbhb4adrBqnzgW2-ypx4qHpmyuFg-DJndmwNeeiQpueMEZRkI28xqjAd63oJO6UeUEtfMVP4SGe0_HMv0ermRu5YQpg-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بحرین حملات موشکی اخیر ایران علیه بحرین و کویت را محکوم کرد و اعلام نمود که هفت موشک بالستیک که به سمت این دو کشور شلیک شده بودند، با موفقیت رهگیری شدند.
🔴
بحرین از ایران خواست تا حملات خود را متوقف کند، تنگه هرمز را باز کند، در پاکسازی مین‌های دریایی همکاری نماید و عبور ایمن کشتی‌های تجاری را تضمین کند، و هشدار داد که برای دفاع از حاکمیت و امنیت خود، تمام اقدامات لازم را انجام خواهد داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/125453" target="_blank">📅 10:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125452">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WkEeN2iF0I7GOMFHbd5G1BFnb5OrCGrc39MGfYNzQ9fe8XurrO47GhDjGB3U-DbTHnRBoppeFQTOm1EiuXeDdWjeAx1PjNOANri16V_xIOZ32XP03dTyHUP7yDxqfeNeRvVyLrXrhy2_lzE_eIwyr6jXeTXOcVQ07li5sPwMgrlHMMc0q8yu73fu1hggyiRnry7di8jmk0mXb2-ni_Gv4aRVctLL0XQPpPpibWypEFGOScBcW7EUUXyJJ5dWXv97pVUhGULZbzUUC1Vbg5BDMbJCQ8y6XIHunFwK7c2NVrtsRapM_nnJKlvrqzxU1hSdB_FOe-pE0CdcZzbZCZFOEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس اتحادیه تعاونی‌های مسافری: با ابلاغ شورای عالی ترابری قیمت بلیت اتوبوس‌های برون شهری از امروز رسما ۲۱ درصد افزایش یافت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/125452" target="_blank">📅 10:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125451">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
سازمان اورژانس: روزانه ۶۰۰ تماس مزاحمت برای اورژانس داریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/125451" target="_blank">📅 10:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125450">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
سنتکام: ۷ موشک بالستیک ایران به سمت کویت و بحرین شلیک شد
🔴
فرماندهی مرکزی ایالات متحده (CENTCOM) اعلام کرد ایران هفت موشک بالستیک به سمت کویت و بحرین شلیک کرده است.
🔴
بر اساس ادعای سنتکام، شش موشک توسط سامانه‌های دفاعی رهگیری و منهدم شده و موشک هفتم نیز به هدف مورد نظر خود نرسیده است. سنتکام همچنین اعلام کرد هیچ آسیبی به نیروهای آمریکایی وارد نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/125450" target="_blank">📅 10:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125449">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N4REkdOJr7Uk5Zyj6jmy6GCVtBv7-EUK7_qTvS0ODtwr6K1Z2fVxivoGiKvnbB3xU3qUWbNfXu5dmPjVliPalgjvXb5L1TULdrQs3NNUi7nk1x5ewHxYlVhWaUnSIswNb_fBwdoHf6pWtnoh-n5o2aZC_oqCOx-KVkQrV4uozSyeY4NZVYnw7PfKKXF0qcq9rEJLwQ-75NJ19stxbirw0NlvopVXUWyTdiBvJr5iz5QM5mlUr-6KwjmCr7F5Pmo1Wca78l5BP8Kg5XDbgrOdMBSQPxBoOxXmmtSkkrIEk-s8wkPlX4j5CXSrYBOgNiYE2EcSfWffClOpD5INM2cr6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل یک سرتیپ ارتش لبنان و دیگر پرسنل را در حمله‌ای ترور در جاده خاردالی-نبطیه هدف قرار داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/125449" target="_blank">📅 10:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125448">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
سفر رئیس سنتکام به بحرین، قطر، کویت و اردن
🔴
در حالی که پاسخ ایران به نقض آتش‌بس توسط آمریکا ادامه دارد، رئیس سنتکام «برد کوپر» با مقامات بحرین، قطر، کویت و اردن دیدار کرد.
🔴
فرماندهی مرکزی آمریکا در غرب آسیا در بیانیه خود اشاره دقیقی به زمان این سفر نکرد.
🔴
فرماندهی مرکزی آمریکا در غرب آسیا گفت: او (فرمانده سنتکام) همچنین با اعضای نیروهای مسلح ایالات متحده که در این منطقه مستقر بودند، دیدار و از (این) نیروهای استثنایی تقدیر کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/125448" target="_blank">📅 10:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125447">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgJni9F25_6lfsRAEhdfpmf100xpf2i_GKNvoTKoqQxqFfzbWCUUlfoXZK_0IlRF5ZZqfKNKcizJrK4sJSePImlk0qeMCbXKrgWkRsoy-omzvs6C3iXBcJNmVjQUlRWOPKxW1gPxbbhbA1IPcVBuezFusXHPBFF6wdB4zRDclGeP7jocuFm7PKEcT04HI17S2Z0dg4M5x_9t07lqg5Yslz22x38pmat8f0E9-vbK-c7GxSqg7zzQ7oVvaX_kML0Qu-nOrtLSaj8PU0JT4GTG-dgX3sM2RUAa86kgjnaAaUI5syvMygmLD-yUyzDDkVONFHennqJICM8PY4NNx1LoFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی میفدون-زوآت در جنوب لبنان را هدف قرار دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/125447" target="_blank">📅 10:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125446">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
پولیتیکو: آمریکا به دلیل کاهش ذخایر موشکی در جنگ با ایران، توافق تاماهاوک با آلمان را لغو می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125446" target="_blank">📅 10:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125445">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbd9a25e0f.mov?token=hkCWN9OdaGDTfoMLHOvqPxcLpFe6T9ckhPBEUUKJQFfQ2ajarndHYQUaWugyhshrSR-o7CmNL-7QHVs5WNWcautoSBaQmj4C1QPvioo_e6iCUgm4qWdfRGg8HsDkrUMFFmHqVH_SFmQwVu6wNl9CDzK6KrEcDRpSceMCiCjqrKr0M4V9n7s-u0o4MFLv4gzwkayEGgS9QXJTUf6QXHflZrZX6THUS2-a-vqLScZ_mwl8JVgvNI-VP4fBMmhiSRdEON0YLqjdW3sp3BpXJ50PmCNI0lmvZkKVlcnRrGQPHB3LSw8s-h_QoFcLeNum71w3ir5bS3HQ06GZrtsNtOs_yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd9a25e0f.mov?token=hkCWN9OdaGDTfoMLHOvqPxcLpFe6T9ckhPBEUUKJQFfQ2ajarndHYQUaWugyhshrSR-o7CmNL-7QHVs5WNWcautoSBaQmj4C1QPvioo_e6iCUgm4qWdfRGg8HsDkrUMFFmHqVH_SFmQwVu6wNl9CDzK6KrEcDRpSceMCiCjqrKr0M4V9n7s-u0o4MFLv4gzwkayEGgS9QXJTUf6QXHflZrZX6THUS2-a-vqLScZ_mwl8JVgvNI-VP4fBMmhiSRdEON0YLqjdW3sp3BpXJ50PmCNI0lmvZkKVlcnRrGQPHB3LSw8s-h_QoFcLeNum71w3ir5bS3HQ06GZrtsNtOs_yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دورهمی و میتینگ تینیجرهای تهرانی برای حمایت از تیم ملی در اکباتان!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125445" target="_blank">📅 09:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125444">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82b7b5a89e.mp4?token=pVWMjzXlxICoWiOnQPI9Q5WHn4P-IWnnHc9ESbxP0GOmgApBvEmOu6tiuXFWkYlOi8xdGSvD7-5DorzVEv5UaMliv2iBUy9shS8eeWBOkStzJ3zPdjxRB-w_RDWqXMiIfl7oci5xftZcVymbHSW97VWIkS4rdIKcO4_qeVK5uNNSsJvqAX7_qrX6rRbNMiHOazLQTdbneYt74MirdU2_Z8-UutNhLeQLls412XH3_NrSK-AAKThiS1BwyAVTwPnnH4YuavahEUbSvikG7fBN18WplvYiA7a6ZTqmZyke6QUj1sqpbzWez6WIepiZ8WT_OhDTxxPOBIjY0hYicOg3Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82b7b5a89e.mp4?token=pVWMjzXlxICoWiOnQPI9Q5WHn4P-IWnnHc9ESbxP0GOmgApBvEmOu6tiuXFWkYlOi8xdGSvD7-5DorzVEv5UaMliv2iBUy9shS8eeWBOkStzJ3zPdjxRB-w_RDWqXMiIfl7oci5xftZcVymbHSW97VWIkS4rdIKcO4_qeVK5uNNSsJvqAX7_qrX6rRbNMiHOazLQTdbneYt74MirdU2_Z8-UutNhLeQLls412XH3_NrSK-AAKThiS1BwyAVTwPnnH4YuavahEUbSvikG7fBN18WplvYiA7a6ZTqmZyke6QUj1sqpbzWez6WIepiZ8WT_OhDTxxPOBIjY0hYicOg3Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فلاحت پیشه: امثال ثابتی حاضرند ایران غزه شود ولی توافقی با آمریکا امضا نشود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/125444" target="_blank">📅 09:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125443">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
ترامپ در گفتگو با ان‌بی‌سی: رهبران ایران هنوز برای پایان دادن به جنگ جاری با ایالات متحده به توافق نرسیده‌اند زیرا آن‌ها «قوی» و «مغرور» هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/125443" target="_blank">📅 09:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125442">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sELUtwEpxFgIVh_Y9vRsQKT-hrqYofBYeU5O6hZiGFegX3OnaMvMtJ4ZbK0kbQjFjT1WBpXiaed7xe4SYUNp-KDXQ7PhkiU7YXRS-Hb5IneVx-xy6PNzUqA8lEl-Q5qGv1K5OtAACkn0hhsu1jPLUDvAFBMEwYu4LGEtLrZ3yT2j_pbCwBQ63naHGpe6syRuI8CnUmyTXp185a4v9412T30cmZmRQn08wANtxKu7jXYdPCn7g2eXrZWYiCklCpoLWq7G3i4VROU6hHlCHivB5P1OK5VTjmXn8yHk1pgaE6CvtBXru_9dXsAJXhJrF_epe0MC91QgnfZmillRytd-bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یاسمین انصاری، نماینده کنگره آمریکا: دونالد ترامپ امروز در دفتر بیضی کاخ سفید، چند بار به خواب رفت، دوباره.
🔴
به همین دلیل من خواستار اجرای متمم ۲۵ قانون اساسی شده‌ام، و ده‌ها نفر از همکارانم هم همین کار را کرده‌اند. ترامپ بیمار است و باید از سمت خود برکنار شود، این یک بحران امنیت ملی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/125442" target="_blank">📅 09:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125441">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e01c119656.mp4?token=KrQy3rqa5RgXUItyL87_1xWHlDUueAEIGbU-l69Hi1QNvic8nsKTO2tne_rcG2eZOS7ua2DJKpgrq2arhSJHr9HLnQkXz1W_NuJHDomxppwVLm-f8orsPAl4YCCsn6l6jfflKP_TQjUgMQCLCg6ALHAl3abf_xDKQOcSOhfrc2jhG-mwcOyJdN_f3kq-V4QOQOrknMp4Ry802-Ri4jtY1-KP8tqZonf0wylU4t7mGNq0F_re2MskGImtgEY1--GEJ0GVzEMyE7XFWRFV4Uj4Tn-YPG2wE1nPkFdiaM9mT9P7LxMmrY6derdBZJy4_ak0aDajp-5Y-SRwE7I0bpn2pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e01c119656.mp4?token=KrQy3rqa5RgXUItyL87_1xWHlDUueAEIGbU-l69Hi1QNvic8nsKTO2tne_rcG2eZOS7ua2DJKpgrq2arhSJHr9HLnQkXz1W_NuJHDomxppwVLm-f8orsPAl4YCCsn6l6jfflKP_TQjUgMQCLCg6ALHAl3abf_xDKQOcSOhfrc2jhG-mwcOyJdN_f3kq-V4QOQOrknMp4Ry802-Ri4jtY1-KP8tqZonf0wylU4t7mGNq0F_re2MskGImtgEY1--GEJ0GVzEMyE7XFWRFV4Uj4Tn-YPG2wE1nPkFdiaM9mT9P7LxMmrY6derdBZJy4_ak0aDajp-5Y-SRwE7I0bpn2pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سنتکام ویدئوهای حمله به سایت‌های رادار ساحلی‌ایران در سیریک و جزیره قشم را منتشر و اعلام کرد حملات تلافی‌جویانه ایران به بحرین و کویت رهگیری شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125441" target="_blank">📅 09:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125440">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
رئیس ستاد کل ارتش اسرائیل در دیدار با رؤسای شهرک‌های شمالی اعلام کرد:‌ «ما طرح‌هایی را برای گسترش عملیات‌های نظامی‌مان در لبنان به سطح سیاسی ارائه داده‌ایم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/125440" target="_blank">📅 09:16 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125439">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
پنتاگون سطح تهدید ضدجاسوسی اسرائیل را به بالاترین حد خود افزایش داده است، در حالی که نگرانی‌هایی وجود دارد که اطلاعات اسرائیل تلاش‌های خود را برای جمع‌آوری اطلاعات درباره بحث‌ها و تصمیم‌گیری‌های داخلی دولت ترامپ در مورد درگیری‌ها در خاورمیانه تشدید می‌کند، گزارش NBC News.
🔴
ارزیابی اخیر آژانس اطلاعات دفاعی، توانایی‌های جاسوسی انسانی و جمع‌آوری اطلاعات فنی اسرائیل را در سطح «بحرانی» ارزیابی کرده و به چندین حادثه اشاره کرده است که نگرانی‌ها را افزایش داده‌اند.
🔴
در حالی که اشتراک‌گذاری اطلاعات بین دو کشور بدون تغییر باقی مانده است، مقامات گفته‌اند که انتظار می‌رود کارکنان آمریکایی هنگام سفر به اسرائیل یا ملاقات با همتایان اسرائیلی احتیاط‌های بیشتری را رعایت کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125439" target="_blank">📅 09:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125438">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfITrN0Z2z-JD_iNuHQyiKZgryosdQrFvoYEVSWHylMPdyktokqnDgHHS4wZxsdQv8KckUTOZmhMLtnqjiVfLDtNDE8zTHpDLTZVBPdMc5AtDrfeiHYDMyuNXW0cmcFp4gOBZfNe-a_BAwGQd2KI87Ym8P_8Ce0zXiw52gOHCHthR64z6_vDg7989lImiqfiEGeX7czAEgrmrjGy01afV-KuVpAxM6MimhPtjUEqqb_xYIv9_GKnB-eIz0IM9raSL3kmsHSCJ03Ef64SFsvtSz2By-HpN8elM1alCix2rkPS0MuywaLLdeAg_mF6QC_0zKlZKq7qNwYTGfF0E3XOzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پیش فروش بلیت‌ قطارهای مسافری برای بازه زمانی ۱۷ تا ۳۱ خرداد، از ساعت ۸:۳۰ امروز (شنبه، ۱۶ خرداد) آغاز شد.
🔴
پیش فروش بلیت در همه محورها از ساعت ۸:۳۰ تا ۱۱ صبح روز شنبه (۱۶ خرداد ماه) از طریق سکوهای مجاز فروش اینترنتی بلیت آغاز شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125438" target="_blank">📅 09:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125437">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYwxEWb-q5-v6jZpOL04532mLwCxCwxqco-oxZeNBPH8So2KwD29RvRzd6KDCvXg50Mmihf2h47HAPyRCSPQQGgS2tmwGtyRzXsX6fEUJoedwVNmVadkSAV11s0rS7pJAsheX4M9f6WSoxRBT6QEnX_XAiRDDEJ4FFKSf8-kWgP3TyjHrocpBJnAJ3ZmlUOiqGma8pmuTMyhUyqpOSrj6Ur-Idpi4qCvM_mWFBsjXfcBccn4MZ87Xsv7x8YURFqDGxzzO9YdABg4BWZiyOaqbR-SUTvS4dIxI9fDNN5jYIAoF8zYTmbv1bLhmjJAHJlaM_g-oBD-WKxiD5afqwzsZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی به رئیس‌جمهور لبنان؛لبنان را از دست دشمن واقعی خود نجات دهید
🔴
براساس اظهارات آقای عون، ظاهرا این ایران است که یک پنجم خاک لبنان را اشغال کرده، یک چهارم لبنانی‌ها را آواره کرده و کشور او را روزانه بمباران می‌کند.
🔴
اگر لبنان برای ایران ابزار چانه‌زنی بود، ما مدت ها پیش به توافق رسیده بودیم.
🔴
لبنان را از دست دشمن واقعی خود نجات دهید، آقای رئیس‌جمهور!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/125437" target="_blank">📅 09:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125436">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
پوتین: روسیه هیچ سلاحی به ایران تحویل نداده و تهران نیز درخواستی برای آن نکرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/125436" target="_blank">📅 08:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125434">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FoLeAyT69_66TGJ3PZJRZWTnnU4cwhUOc_ah4Z4IaL6ko44lBz6yVqvRalleCj6TD3W_cYANMUhzKXgNgBUtmd83EEFNkZmLijW5PLphVfM1_4p7cwv44Tr1tgBREKxa5ajsrM44001DFRzBXkTnqXqjSVC2AKpZnDhOQwXJQCdCi7UWue5kFuVib5fXdElhIL43S9PFSAu3yn87tNmFJVZCmb8F48GZyoNv9PrU6i2XXhAhB1xDs74hXu7_iK25lzGSBYrskACHV-QT_Li56gSNnpZnoydpruWgfuKSPmZmLjnQLb-ukYmB6y_29z1-p0z60RQT8xXfD0lknJJO8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cDMru-5FxYiKh4_BP8KXtlHDNhIYtF5MGttI2WRU47NhZFrxSu4BJVyOEaATV-84BShUXShJuHK1gQjhwotEYH4G5DDWN0Xl171K1R3i5rW79IFb73MCiyDbevma-twZeyqWalcTPVe_Sz5k0qKg2QZPyPMo9171XR2gUxoyKMuk9Kfr1kfbensc4zJ1BSgIWPq018Yd8MS5B2S6MD_FQWJg499tkLdu6mLXqyQFIDSiYYUGYTY59eJ0jebS61CZskt5psCNf7p_7KWriFEmH3H-6zmiZgvrW5tRQ975bczMXAJAViUuGSxuHtFQCaqM11sAs-a-S0QD9SHUpKPIhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
کیم جونگ اون و دخترش (جانشین آیندش) در آزمایش‌های دریایی ناوشکن کانگ گون
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/125434" target="_blank">📅 08:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125433">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
شبکه ان‌بی‌سی به نقل از مقامات آمریکایی گزارش داد که نگرانی‌هایی در داخل پنتاگون نسبت به تلاش‌های اسرائیل برای نظارت بر مقامات ارشد ایالات متحده وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/125433" target="_blank">📅 08:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125432">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
چهار مقام ارشد آمریکایی به نیویورک‌تایمز اعلام کرده‌اند که درخواست ویزای تمام ۲۶ بازیکن تیم ملی ایران برای حضور در جام جهانی ۲۰۲۶ پذیرفته شده است.
🔴
بیش از ۱۲ نفر از اعضای کادر پشتیبانی (از جمله مربیان، آنالیزورها، پزشکان و فیزیوتراپ‌ها) و همچنین مقامات فدراسیون فوتبال ایران که قرار بود تیم را همراهی کنند، ویزایشان رد شده‌ است.
🔴
مهدی تاج رئیس فدراسیون فوتبال ایران موفق به دریافت ویزا نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125432" target="_blank">📅 08:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125431">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIo242VRzLISlskZ0BDoZFpNFDCMHCiIldTHMxQ2EvHyFh7u53NOsKaBhB--nY6MxCIxaq6m-nUOk__Srd-h1gU2p5niGhbSDZcFDUkcCsSsfSCClphJYRcxEo_WhzPbtWLXPenzl1jyyuFJHzmzGnR1sjPpqQ7n6Yp5Lalzta-_E3Z43106PqkkVZdYNrhogqvjAwIZ7cZtFo2Rkvzsa9hbvdbzL1KMV_DmWFL5KD33oHes6o-NKm6oBHZV_C11RIugNLxSbB8mTVO4Dy8TxuTelimcFoghXnvR4R6fClAcwXoIvLIqCiJup6VZCsqi1Mhoo_LdFxiMcUU9qD4x_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پس از حملات ایران به پایگاه آمریکایی‌ها در کویت، ستون دود در این پایگاه مشاهده شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/125431" target="_blank">📅 08:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125430">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
سنتکام: نیروهای سنتکام چهار پهپاد حمله یک‌طرفه ایرانی را که به سمت تنگه هرمز پرتاب شده بودند، سرنگون کردند. این پهپادهای حمله تهدید فوری برای ترافیک دریایی منطقه ایجاد می‌کردند. نیروهای آمریکایی سپس سایت‌های رادار نظارت ساحلی ایرانی در گوروک و جزیره قشم را برای دفاع در برابر حملات بیشتر هدف قرار دادند.
🔴
نیروهای آمریکایی همچنان هوشیار هستند و برای پاسخ به حملات بی‌دلیل ایران در دفاع از خود آماده‌اند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/alonews/125430" target="_blank">📅 08:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125429">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
کیهان: دولت پزشکیان بخاطر استقامتی که در جنگ نشان داده، دولتی پرافتخار است / محبوبیت پزشکیان بیشتر شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/125429" target="_blank">📅 08:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125428">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhLTSvH_YptfgBvkjohtyW1EfyV_IYhKQBPI53YGrTG7E9YxOuY0sL3SJYvdPg6UMEIjcwamz0EtC7GTFg8fi15RZJcKQ5fjaHxxURtdkhL6I_zeLoq8aBF7p_h5e9nhjUU5S0ukUQG3FMr9RfzSZPn_PjbhYXJDXPsg_lvuTiXtdIu3MpQ0MbDedZ7itp98zdNtteZuTq-vn-munN8AFwrwBMxGtByAUoHl6ZHudVNl-1htwDu1wvg3wb8DXvg-wDf7OJzIAqOUt8t_TeaPYnb2aRJTD2wbwLMzSMVh9CVgoduza0N7OpLXr_jnC2pkMhtCfnOMvi1uavIpb-CnMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سی بی اس: تا الان هیچ کشتی‌ای توی تنگه هرمز به خاطر پهپادهایی که ایران فرستاده آسیب ندیده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/125428" target="_blank">📅 07:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125427">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6388d22ab.mp4?token=Fld4XE3AwhJHPuRxxZOmaHBZckveHK232929FEuZQMJbQS1iYQbmWWWoin-JZAab5DSlT8SF_C-bxcojlJPl4NaG1i2OGBY2D10AXAwLsH1UJzrF9LXT8w09qr-hZP5sfz8MYl8WZcGKONZnZ_GXHr73De8TKRy_96oowFkpM9C66qswPuzjiapT9n0opuf8oq8YZA9u1jMZRNpJEYk1kqqbZ_-KL3tKocREYQBge4o0nadRH5ekApn9q5VToMeVVqiUynjwtI5fKnqpuxa1EwigveCn3XsANXjS_CztXswdFnZ3P6zX2D4ez8hYeRWvCv6m2P6OG4g2QdZpbpx8LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6388d22ab.mp4?token=Fld4XE3AwhJHPuRxxZOmaHBZckveHK232929FEuZQMJbQS1iYQbmWWWoin-JZAab5DSlT8SF_C-bxcojlJPl4NaG1i2OGBY2D10AXAwLsH1UJzrF9LXT8w09qr-hZP5sfz8MYl8WZcGKONZnZ_GXHr73De8TKRy_96oowFkpM9C66qswPuzjiapT9n0opuf8oq8YZA9u1jMZRNpJEYk1kqqbZ_-KL3tKocREYQBge4o0nadRH5ekApn9q5VToMeVVqiUynjwtI5fKnqpuxa1EwigveCn3XsANXjS_CztXswdFnZ3P6zX2D4ez8hYeRWvCv6m2P6OG4g2QdZpbpx8LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پخش دیشب برنامه «خیابون انقلاب» بخاطر این حرفا لغو شد.
ما اسرائیل رو تهدید کردیم اگه کوچیک ترین خطایی کنه میزنیمش، الان لبنان رو با خاک یکسان کرده و ما هیچ کاری نمی کنیم.
ما همش الکی تهدید میکنیم اگه فلان کارو کنن مام فلان کارو میکنیم، خب چیشد پس؟ یه بار به دشمن نشون بدین که ترسو نیستین.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/125427" target="_blank">📅 07:02 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125426">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
نیروهای آمریکایی از هدف قرار دادن سایت‌های رادار نظارتی ساحلی ایران در قشم خبر دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/alonews/125426" target="_blank">📅 06:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125425">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O56C9eIa_gX5pzkIM6rs95xLhUUpZcG8BLR3Xc8U-aXQJCHqLjvWNZfiVVma2oaKDmKWRybkYjYI3AgC8iBCcaYY5RQZ4m7e7zoLzuMOiPaR3K4XnyWK5-DKI4qdkIqofSWktnAP8lIKoDmKezXeMV-QyxzlrdVQafD5AIb3CSevkeo0QysELvZVXHVCsFQISRFJq2DkCW0e0mjTc0tctRtAFftaVXzqK8yW5mhAM5VKjxW2tMbGVeTcJKC7rRyNQzLmXXMYFzm2qHF1x4F2rp_zFZ_nseWDPheQaWIwXhINBTtZ7_yKKFM9SR3qkqdAvz5nda-sSYeU3NzQQcrPyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">​
🔼
کسب درآمد از فروش  VPN
هنوزم ممکنه!
درآمد چندتا از نماینده‌ها رو ببین
👀
پنل نمایندگی وی‌پی‌ان گذربان، سریع‌ترین و
راحت‌ترین راه برای پول درآوردنه
✔️
​
🤑
چرا پنل نمایندگی گذربان؟
🚀
سرعت و کیفیت بی‌نظیر
⚙️
پنل مدیریتی حرفه‌ای
💵
سود عالی
⭐️
بدون ریسک
​فرصت رو از دست نده و کلمه «الو» رو بفرست
👇
@GozarBanAdmin
@GozarBanAdmin
@GozarBanAdmin</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/alonews/125425" target="_blank">📅 01:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125424">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
ترامپ به ان بی سی: خیلی از مقاماتشون هم مغرورن یه سری کارها هست که هیچ‌وقت فکر نمی‌کردن مجبور بشن انجام بدن
🔴
ولی الان مجبور شدن، راه دیگه‌ای ندارن و این قضیه زمان می‌بره
🔴
داریم درباره ۴۷ سال حرف می‌زنیم که هر کاری خواستن انجام دادن
🔴
توافق اوباما با ایران خیلی بد بود و از قبل هم عملاً تاریخش تموم شده بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/125424" target="_blank">📅 01:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125423">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
ترامپ به NBC : وضعیت برای اونا واقعاً سخته
🔴
یه جورایی استقلال زیادی هم دارن، ولی سال‌ها با یه رهبری ضعیف و بی‌اثر از طرف آمریکا و بعضی کشورهای دیگه طرف بودن؛
🔴
طوری که عملاً گذاشتن هر کاری دلشون خواست بکنن.
🔴
من فکر می‌کنم خودشون هم الان باورشون نمی‌شه به اینجا رسیدن؛ جایی که عملاً خیلی ضعیف شدن
🔴
این موضوع باید خیلی وقت پیش حل می‌شد
🔴
توسط رئیس‌جمهورهای قبلی یا کشورهای دیگه، لزوماً هم ما نه
🔴
ولی واقعیت اینه که دو بار تا ساخت سلاح هسته‌ای خیلی نزدیک شده بودن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/125423" target="_blank">📅 01:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125422">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
ترامپ به شبکه ان بی سی: رهبران ایران چاره ای جز رسیدن به توافق ندارند‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/alonews/125422" target="_blank">📅 01:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125421">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adb22b3119.mp4?token=Jpkdph4gtkigefSOD9YEjisGAIgKyypYEF3yPXughwC1MoIWoEXcWPK9gauGo1UHEm7YH8f5fTviWiFS8JIJnQvRlQKpQ4QWK6GesdSy6qt3DgbT2x46dT6WibbMjPa7KppfRbXcPi9jRRoDSQ7zhF77pEB8rnZ2_pjWFPHAL-wTi5NunmBTSXWizTl0xznTivfgPIKsnHGSatyi1VojweAAMzs6TtohXx3BBbO1H_cskldCsxgJe_G0NwvK-Mawr5VgjtwbcBtNoneTSpeEpWc-LLxCAYKJy7NQRAUrBcvoxQemGo1mFPbCDgxX5-tCZEzUyFFCptN62CisjYj4UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adb22b3119.mp4?token=Jpkdph4gtkigefSOD9YEjisGAIgKyypYEF3yPXughwC1MoIWoEXcWPK9gauGo1UHEm7YH8f5fTviWiFS8JIJnQvRlQKpQ4QWK6GesdSy6qt3DgbT2x46dT6WibbMjPa7KppfRbXcPi9jRRoDSQ7zhF77pEB8rnZ2_pjWFPHAL-wTi5NunmBTSXWizTl0xznTivfgPIKsnHGSatyi1VojweAAMzs6TtohXx3BBbO1H_cskldCsxgJe_G0NwvK-Mawr5VgjtwbcBtNoneTSpeEpWc-LLxCAYKJy7NQRAUrBcvoxQemGo1mFPbCDgxX5-tCZEzUyFFCptN62CisjYj4UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله تروریستی به یک پاسگاه پلیس در منامه بحرین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/125421" target="_blank">📅 01:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125420">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
ترامپ به شبکه ان بی سی: ایران بین 21 تا 22 درصد موشکهای خود را در اختیار دارد‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/125420" target="_blank">📅 01:17 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125419">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
پرواز جنگنده‌‌ها تو جنوب عراق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/125419" target="_blank">📅 01:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125417">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
ترامپ: ما خیلی سریع از ایران خارج خواهیم شد و نتیجه آن، به هر شکل، بسیار قوی خواهد بود؛ چه از طریق یک تکه کاغذ (توافق) و چه از راهی بسیار سخت‌تر. شاید حتی راه بسیار سخت‌تر، آسان‌تر هم باشد.
🔴
اما ما از این مسئله عبور خواهیم کرد و قیمت کود شیمیایی شما به‌شدت کاهش خواهد یافت، درست همان‌طور که چهار ماه پیش بود. قیمت کود شیمیایی اکنون هم کاهش یافته است.
🔴
قیمت انرژی، نفت و گاز نیز همگی به‌طور قابل‌توجهی پایین خواهند آمد. و صادقانه بگویم، من تصور می‌کردم قیمت‌ها بسیار بیشتر از این افزایش پیدا کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/125417" target="_blank">📅 00:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125415">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
ترامپ: محاصره دریایی که در حال حاضر علیه ایران اعمال کرده‌ایم، باورنکردنی است و جهان پیش از این هرگز مشابه آن را به چشم ندیده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/125415" target="_blank">📅 00:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125414">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7514cef466.mp4?token=cVKNLTlAdr4HVinmbKL-BeGHA6yWEftSSYe30X6DA8RUeAOumseXG5mBITbgdPlGH2VvS3vqagKY6BjP_4mopbIo0cqNSldYYgLZOTOd3EhbUzaTvxOxAuW4mGj0quYrj7tKz-PeXiYh-CkscRgSQSPZQOXF3Jk82r2IeooLMIjMubjfVKpH91h95GxzzH6YPcbCm_9o1F80_93eEeklupaWPEJPGmPUVWeWFQT87r12KH6m1IYBmQlOj8sz1xXLy1-HGVVOOEuWbT9WUEPAmrAZl_q_LVXzyUie3_Sw496PKVC8pmVe2mlZm3x02vH6bR77USQXCpa9IldGd1T-RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7514cef466.mp4?token=cVKNLTlAdr4HVinmbKL-BeGHA6yWEftSSYe30X6DA8RUeAOumseXG5mBITbgdPlGH2VvS3vqagKY6BjP_4mopbIo0cqNSldYYgLZOTOd3EhbUzaTvxOxAuW4mGj0quYrj7tKz-PeXiYh-CkscRgSQSPZQOXF3Jk82r2IeooLMIjMubjfVKpH91h95GxzzH6YPcbCm_9o1F80_93eEeklupaWPEJPGmPUVWeWFQT87r12KH6m1IYBmQlOj8sz1xXLy1-HGVVOOEuWbT9WUEPAmrAZl_q_LVXzyUie3_Sw496PKVC8pmVe2mlZm3x02vH6bR77USQXCpa9IldGd1T-RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : این دیگه خیلی جنگ حساب نمی‌شه
- یه درگیری نظامیه، بیشتر شبیه تمرین می‌مونه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/125414" target="_blank">📅 00:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125413">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
ترامپ: ما به هر نحوی که شده، تا حد زیادی مسئله ایران را حل کرده‌ایم.
🔴
ما باید یک سلاح هسته‌ای بسیار توانمند را خنثی می‌کردیم و اجازه ظهور کشوری با حضور گسترده هسته‌ای را نمی‌دادیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/125413" target="_blank">📅 00:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125412">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
فوری/صدای انفجار در جزیره خارگ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/125412" target="_blank">📅 00:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125411">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJj9Hbk0XlXLQYJTv7FYy2eWADvFveEz6iIw_fUyfr-78RmjEApZzQ8TSeI-rDPq57T_SOJZwEUVpW5_Qe25gEJb70o8qfhZq9nSlJhaAVKLGbn-sdrTJVtduNc5mEIVRwey5pywCFitLEAUKSMryF9sQ7SoIxjmMAQjO1yE0OOK3Sy8Arvw6-fMTAtIK0lerojW5pVWx96G5b7Z8i19cuSHkphEViZuCU76XBnvlI9KEE7cmfI3R0fm1trCNxREJT4P0r17eCD9FiRl1avKlsnm24yWQIqCVnmqXX9Q5MN9C0H7OZ7FVfBAXBYnzj6rdLu9lnH1M5eo__Cp-XW4RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آژانس بین‌المللی انرژی اتمی جمعه 15 خرداد اعلام کرد که یک حادثه جدی در جریان عملیات مین‌روبی در نزدیکی نیروگاه اتمی زاپوریژیا در جنوب شرقی اوکراین رخ داده که بر اثر آن تعدادی از نیروهای ارتش روسیه زخمی شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/125411" target="_blank">📅 00:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125410">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNddW4oVBVrroyJZKCXnusw0eRRHkye9wtNamWrz-puZQDIVAfPkcLnaOZn0pblcWxYMIuga5NoeJWnjplnBz8PEFx-iDs4dK9xJV5UCSge0ZeyfaeIBCsARPYHko-5_ujX8KXZCnfONw8-XixwRtJmywx8Ehrg9uMZ-Icus1scRk3aqddtS3l6Gcd_3Xe7eAdzVyYLnWhUeELpaBoB6THJLBq3TvOQ8ruPQCxT3JRdaACObjAaZaP8JB7D715SsYWX2Vt8b9aJWN9xfnwD1S_QXGqCU2ZPGrV9nMV5yy7rdRDNs3xZGZNKzsQkTrC1baMtU47TaPr352DAqBTMlJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مهدی طارمی: اگه تو جام جهانی گل بزنم، اونو به آقا مجتبی تقدیم میکنم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/125410" target="_blank">📅 00:16 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125406">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LyNIPJDv4igPDVhMXn6DWJdvDPbL2CP3dSKGO5dk7vcNTK_LiFVB26SbHgUnW43AEO0Fts6PmlUZZM1Tf4BFkk9wS-jUeiM6-UjjdFxCOxPzhQBntxo8xHc-GbSipmpg3sqgmb5nrOmzx85-jo-9k_fwevZXPd3bbDYIHK4T3uiYnQqpzFfL1H-YoJ8JnKQTDecgKi59Hbd5lTmhTRhgIgfusWS0DjwporvbD3VM08JVAhBecpESezLu9hG-7rrj-_Ql6OcsqkEzieTEkonI1eizxhR-51lX8vn7oVYc181RwVP1V0lcAYIdKjQVky3dSfL93Ta_xy44MlXx18gliA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jid4raCLcA4NQU-HsjNobjZ7gS9BSFBuuKAXZmwb7SFZXC4c0x93e4D_lao2C4QiCl6niUConJN4GfIlREIyBGC1QxnE4_ZGj-icOcr-LdlzH93JaxUVvegBPLDhmcVOR6qcpDfnjNPuajClTkQPrwUxI_vjxI0uEzcjDRil7oGpOYSlFOIi3xZyHXMpF9A1lj6ICNiFFGGdF0d0l3JIXJV1HdHz2z2n2i4pctimhVUCiacLheYYRkltrMhhY6O1G-bp2AnhSZ4pVPc8Xtco_QpLLcUF8d-VXJBfdt7F7xWEq0mdsR1cjmL5o1dRo3R6kio4ey_XAZG5a2QnUi3mMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QJ1pE2feAPfoB7c9GPnAR44FmQ-5zL8K_04LYV-ALwmFZeEduWpCeeRaPfUmfVopr3X_w-mA0D0RMBHVB3DVfSlIW7H0xOERABu3OOe9uCVwDjAepZoTB94k2GZe9ARK5s5njOiMmi0ZCKJqiYycwnOWutRxRX_enSTiMarFWsdCobDZIxPgJUlVzF3N5_0PE9fLzINFUjS6nNiGHAOPQxrbIwq7RE7nThsVjR8jThnn3e0ja7DPyZ_E6GfM9KLGKfcYleA4wiCmR3B3WTN9W9ou4RorrXKCcRh3V5sqwlXFpdj07Emdj5ODJiiwmiYkJCk6g7u7jmv7J8qyk06PYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iJuFPl9-opn8K1hpoX2fCBOMVnJ2xKEthJuQy5L18Oynmmec_Oxl-yl4_mFHOChz6SB3xBnS_f07yEhHiQwMcRasURESKbRGM8Usox5uXcl6cT6aWuPlORLOOa8SrrOt8pmxCLChRpbui1H_MwouOf0P9eVXQygeeVhZwsJWeEcbHfSLCcKxkjpfSppMJmO11PFvd1SZNVX5U8Gl5UwygsYmVfn4xYWcVhgMpKmBnE1V8ZQ6GET85Vfjo3lHyL1oIyLEgEOSc9aeVSV3FJfDsfwZIIyEsazjwoWERoq65tQ4polquimufStvH0eEjpj_vGc3CZaCFjhLLflknpqXqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
صدف طاهریان، مدل معروفِ خارج‌نشین، امروز با یه استوری رسما اعلام کرد که به ایران برگشته
🔴
وی اعلام کرد منقلب شده و انقلابی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/125406" target="_blank">📅 00:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125405">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a13944d664.mp4?token=MnGAT6WZm2Xr6IBV0JV_3aKak__gCo39fs3f8bL7ILQzuf6RvtdP5ot50A7lDUUe46VbS_K0XHPBdtv0puTqN5LKPnLEFcrepd2qcqgKl3xdV92udH8DxfWJYLHmNC06NA1DDEHw5IvSHHY-QfmrFdrcf2LJzdhWfwboSiZZGs0aODK6kwSE8a1ql52PI_Ryq40eeD4HTTxSJNBKparUQR_hy4gK7D4X4D_OWHaubPc4sQBW3ZFlLAvYa4vcPrfoWAxaz0nWc_7WzdG5LbqmoF2Dcr2kOg-V-F31oqxVog98ogKziqEtjoID62XeLt6PUQwZlFEFcmdyq3cNr55hcw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a13944d664.mp4?token=MnGAT6WZm2Xr6IBV0JV_3aKak__gCo39fs3f8bL7ILQzuf6RvtdP5ot50A7lDUUe46VbS_K0XHPBdtv0puTqN5LKPnLEFcrepd2qcqgKl3xdV92udH8DxfWJYLHmNC06NA1DDEHw5IvSHHY-QfmrFdrcf2LJzdhWfwboSiZZGs0aODK6kwSE8a1ql52PI_Ryq40eeD4HTTxSJNBKparUQR_hy4gK7D4X4D_OWHaubPc4sQBW3ZFlLAvYa4vcPrfoWAxaz0nWc_7WzdG5LbqmoF2Dcr2kOg-V-F31oqxVog98ogKziqEtjoID62XeLt6PUQwZlFEFcmdyq3cNr55hcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه فیلمبرداری از جنگنده نسل 6 F-47 آمریکا، این جنگنده هیچ حرارتی از خود بروز نمی‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/125405" target="_blank">📅 00:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125404">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
ترامپ: در حال بررسی امکان ارسال سلاح به تایوان هستیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/125404" target="_blank">📅 23:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125403">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMfLGg5CMBxKuRg-1xbWY3C-A1RuvaRJAjqjo7uUNQTrMhsgnIE6694glOGEYD9r93u-HV61HP8CNf-tEh7UDjB73QNOCseJCTPWGC0D3bXZUooUpZpQFu4iGSnGikKC8W2OcOhuJikWqXM3kCgLazNUyMq569VFkseGswXbYj9g-FZ5_OJaBT3knKlpR5rDSC7RJ0ThhPbq2Tkk48VE3xGDqInmF_koi1-mj0OoNsVjP8oKiL4hC6-SX1gl433e34O7Iu8sy_7Y8_2Qirn8MESGq-jmSnDSibTwbE3JXahRwIgmVGkysm1_k4sA1v_nDW85AGjj8REmlXjogTFnYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عکس امروز از دست ترامپ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/125403" target="_blank">📅 23:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125402">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
نخست‌وزیر پاکستان: همواره در کنار آمریکا بوده‌ایم؛ برای همیشه از «ترامپ» به عنوان «مرد صلح» یاد خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/125402" target="_blank">📅 23:31 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125401">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
فوری / نایا : انفجار ناشناس در نزدیکی کنسولگری ایران در استان سلیمانیه در شمال عراق.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/125401" target="_blank">📅 23:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125400">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8048ec0b61.mp4?token=mUgrh3I1nL1-_4f-oZX2kh3qGzlRhQJL0HhjKHIDaO9d2xKO1rdCZieO6GTpvVQwkgm8PeSNH7U9j6eZP9YQEYx4ZLHZG7arwTMKUUwtrD4WSy6FanH_oYb1Cc8QFv9EzJZBjrvJ1JWywyGQwfHGrr8Q1Pbqxq1wmhaLQTXoX6eiw6MGt7lQsoZcSdV6qNVIiCBfrT177JYQqAK-4AOi6vQncr9l_6oQjUWkSMTVD9lOOOZYZ3QkunlwfH6KA1ckSeDzVpj1igYSvzZe6LZwellK8QmvfbxQeiGzVc7lOG5ziT69FsjXQkRdVj42kIxnAs43Dx5hO86ye0HDy5IH8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8048ec0b61.mp4?token=mUgrh3I1nL1-_4f-oZX2kh3qGzlRhQJL0HhjKHIDaO9d2xKO1rdCZieO6GTpvVQwkgm8PeSNH7U9j6eZP9YQEYx4ZLHZG7arwTMKUUwtrD4WSy6FanH_oYb1Cc8QFv9EzJZBjrvJ1JWywyGQwfHGrr8Q1Pbqxq1wmhaLQTXoX6eiw6MGt7lQsoZcSdV6qNVIiCBfrT177JYQqAK-4AOi6vQncr9l_6oQjUWkSMTVD9lOOOZYZ3QkunlwfH6KA1ckSeDzVpj1igYSvzZe6LZwellK8QmvfbxQeiGzVc7lOG5ziT69FsjXQkRdVj42kIxnAs43Dx5hO86ye0HDy5IH8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری / نایا : انفجار ناشناس در نزدیکی کنسولگری ایران در استان سلیمانیه در شمال عراق.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/125400" target="_blank">📅 23:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125399">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
الحدث به نقل از یک مقام آمریکایی: دیدار ویتکاف و کوشنر با کارشناسان هسته‌ای نشانه آن است که مذاکرات در مرحله جدی قرار دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/125399" target="_blank">📅 23:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125398">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
المیادین: در حمله به یک کشتی ماهیگیری ترکیه که در دریای سیاه در حال حرکت بود، یک ماهیگیر کشته و 4 تن دیگر زخمی شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/125398" target="_blank">📅 23:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125397">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sZLNGbuHIuMxSnGSAxLHHJm6HhVjlKVW_3vi9X0eWPMpKzzcQd9QKwcw6QOimraKJ22cbXSJk5K63OgeFs0KsRM48NpYCBDmE8jWjKMZBqjENrh9PmDq_c1LfML1vNBreGoyJNNo_Fxsm0vp5AEds70nYZFQD-bk1XVieI-ZGBzTFbxZMEPUXbF2_z6lRkh7Nbh8lVR4USqhvY8_zmDmKW4yfDOFTr0_m_qLMuGkwwqB9MAEjpqZtaa861yQWtf3VuxqYxi9nqJQ9DffX4hZaRXgvLqyP152jszKtcmqyKrNwWO0Pmmor75CLfhbg0PUZEaGgzQAeTWbUuM_Tt_gDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز دو نیرو حزب الله توسط ارتش اسرائیل (IDF) در درگیری تن به تن کشته شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/125397" target="_blank">📅 23:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125396">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
خبرگزاری فارس : آمریکا هنوز به برخی از اعضای فنی و اجرایی تیم ملی ایران ویزا نداده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/125396" target="_blank">📅 23:09 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125395">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTplTrBTLUbYi48rT3gYn35-YYSojEJPbS3eejITW2WJKo93AIVpflswJ2KspiKEsASTnJ9MXXuAn8X9RSltk5g473_zRu75HXPvaEWYPudDHgSbs4aIeyHgFXjRVZ_VcaqRfVBoD4VxO4LXzDtuDRDqMXsuOmHk0WO5Zk565wO_Jgcgu3ZuUdMBB6fhnJn1IeUExZV28Py5LOVZAeORbeXeaAoM8Aw2Py-YdAwxxsQ9roAPwBAqs28crb8LHVUsmMim8k8JkPiWGjcXORA0fgq6fUexzvtuGxvooDIcJX2J6MaJKnU67klySaEms2Ov7SMKqIayzeSZjA-TmFCkfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارش ایرفورس مگزین، مرکز فرماندهی آمریکا که بیش از ۲ دهه عملیات هوایی آمریکا در خاورمیانه را هدایت می‌کرد، در جریان جنگ آمریکا علیه ایران به شدت آسیب دید.
🔴
چند موشک ایران در هفته‌های آغازین جنگ به مرکز عملیات هوایی ترکیبی در پایگاه هوایی «العدید» در قطر اصابت کرد و آن را از کار انداخت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/125395" target="_blank">📅 22:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125394">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJkqIcGI_ZhZVaWg9x5mezWCeD0eXdsqBXcjjS8DPunLwRMI-YRrfn-f14dvMr6KneO0YBY8Xr_J7OXy10FdMLDBVixyj3i1pdT8GiJ2MvmPsyFS15xSFBB74N4xVzzSoPp9uRxbrk_vL1FgAnrXMuslGt2RN8eZygidEY9SK-beQebZ3h8JO5NKYtkmNllTGQwxM51fhv7bKQ9CvgU_VCf_jKz9DIVaHjzwEeA7xAGrPw5ID8i2KKgomhSa_6hW-x1IIXffPFZO4uaYVJ4klx-H7Ujw45Hz2ZSIV408pTZudQEkGHfcsYJFQW6P0zECzdROhR5_rExkUm1w3OW6ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هشدارهای راکتی در گالیلای علیا و نوار گالیلای شمالی، شمال اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/125394" target="_blank">📅 22:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125393">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🤩
ارزون ترین قیمت ، با کیفیت ترین سرویس
🌐
❤️
فقط گیگی 2t ، نامحدود 290t
💫
🔔
آره درست شنیدی گیگی
🛍
2
🛍
تومن
👀
5 سال اعتبار ، 5 سال همراهی شما دلیل این خدمات باکیفیت ماست برای جبران این لطف و محبت
☑️
❤️
👇
تست و تهیه اشتراک
👇
@tvpnshop_bot @tvpnshop_bot</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/125393" target="_blank">📅 22:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125392">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-Yaat1jO-xrDbTwbYARdES4VnXBnYyseUyuZKf8dpv7t_1wwkeFPSeQuFRQAXC5cqe_Z26oZzxcUOJfZiL-cTC0GZrgjtgojC52qQVLFVZ-pl_jpglGbQKUlkh_z9anbAouSE3g7q4izcxQdL0TRXs8zYWMyUmN5gPkUuI8Gq34d9jjwOk3TNAXa6Ppcrjeiqh3lz0FUZ_5rw-QU3nWF6A2dL6LjCapIjUjI2dqPHsWh3RneMHqKA-Vv4yUpv0uO22bOHUjsdvhHJC1q_muSR9nltn2sd1j3L6pOJWYcUA5DIokjhedht5cYxW7uOFbTMV8ejc0jbURWnWt_e5vDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
ارزون ترین قیمت ، با کیفیت ترین سرویس
🌐
❤️
فقط گیگی 2t ، نامحدود 290t
💫
🔔
آره درست شنیدی گیگی
🛍
2
🛍
تومن
👀
5 سال اعتبار ، 5 سال همراهی شما
دلیل این خدمات باکیفیت ماست
برای جبران این لطف و محبت
☑️
❤️
👇
تست و تهیه اشتراک
👇
@tvpnshop_bot
@tvpnshop_bot</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/125392" target="_blank">📅 22:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125391">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c84acc359c.mp4?token=Fjv664K_MDyLvA10DndjfKai0A2GBlQ-GgEeWWiTa8H8NVUeUuCn6Mc9D_DJQXOMEuvNrUw75_oZhrxaK8FsgYQCPlcQCEh-ffhg_X2hd8Q8CUwoSOJvFGX70TEUDX6_5lheXemmjz8OrDVS-Tf77kdW4M6vQ_41TdXDeuUoOZ2TBzID_PCluh_CIO_0rXuraXZbgIVQZJoOkoJvP2GSwDGEMNkMaeEhXLhjnykQWu7tc0p4ZWH0HyfdLfaCy5f8AVu-4Je5O-IN2h63N7LdaTNXOfs8twtGtPBiT3HWPdhWTJSk1tX4PF83lzFTjQnycZijh3jbK3Fw8DQ6sv_EY2ATYrqhjOs0wXW6oCpLfBXGGeF1Zz81s89etUtGxcoZ-2XFcnOpVFB9Kd7jRBCM-BomnuooSHum86WQflEy-fy9bIwMmSk0r46xah9AAV9liLsuZdb8TT9GB770T-z9HDJgTN0p4AGX_1fiEXUqr7yMaZAispRq7mjZ_XKxxC7tstoOGZVp2yK-mQJeii894Pgkn8bZqBK2uSRskFmdc9QD5nUYeD6nPnzl_pxOU7eTeiWUzwRznP2V2XUtFQlJGcSpi57aUHIK9PI2x5-42WjDlBg1JV9yJiCgXY8cNtEmwDl7ghSZr2xQ1IrUPc9ZByTETBCGFjAx5-ZZfZjPUR8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c84acc359c.mp4?token=Fjv664K_MDyLvA10DndjfKai0A2GBlQ-GgEeWWiTa8H8NVUeUuCn6Mc9D_DJQXOMEuvNrUw75_oZhrxaK8FsgYQCPlcQCEh-ffhg_X2hd8Q8CUwoSOJvFGX70TEUDX6_5lheXemmjz8OrDVS-Tf77kdW4M6vQ_41TdXDeuUoOZ2TBzID_PCluh_CIO_0rXuraXZbgIVQZJoOkoJvP2GSwDGEMNkMaeEhXLhjnykQWu7tc0p4ZWH0HyfdLfaCy5f8AVu-4Je5O-IN2h63N7LdaTNXOfs8twtGtPBiT3HWPdhWTJSk1tX4PF83lzFTjQnycZijh3jbK3Fw8DQ6sv_EY2ATYrqhjOs0wXW6oCpLfBXGGeF1Zz81s89etUtGxcoZ-2XFcnOpVFB9Kd7jRBCM-BomnuooSHum86WQflEy-fy9bIwMmSk0r46xah9AAV9liLsuZdb8TT9GB770T-z9HDJgTN0p4AGX_1fiEXUqr7yMaZAispRq7mjZ_XKxxC7tstoOGZVp2yK-mQJeii894Pgkn8bZqBK2uSRskFmdc9QD5nUYeD6nPnzl_pxOU7eTeiWUzwRznP2V2XUtFQlJGcSpi57aUHIK9PI2x5-42WjDlBg1JV9yJiCgXY8cNtEmwDl7ghSZr2xQ1IrUPc9ZByTETBCGFjAx5-ZZfZjPUR8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عاشقانه ی وزیر انرژی عربستان سعودی در مورد مشارکت روسیه-عربستان: ما با هم می‌مانیم تا مرگ ما را از هم جدا کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/125391" target="_blank">📅 22:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125390">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
پروازهای فرودگاه رامسر پس از چهار ماه با پروازهای اصفهان به رامسر؛ در مسیر رفت و برگشت امروز انجام شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/alonews/125390" target="_blank">📅 22:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125389">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
ترامپ: مقدار زیادی نفت وارد کشور ما می‌شود، و مقدار زیادی نفت وارد جهان می‌شود که مردم حتی از آن خبر ندارند.
🔴
و به همین دلیل است که قیمت نفت ۹۷ دلار در هر بشکه است، نه ۳۰۰ دلار در هر بشکه.
🔴
وقتی همهٔ آن مسائل مربوط به (ایران) حل شود، نباید طول بکشد — به هر صورت، این کار انجام خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/125389" target="_blank">📅 22:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125388">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/197efe458f.mp4?token=ed5NbJR6PPLHXNEfAqwfy9Q1Z3aGn9_WnOO3Ai3Iln9nmiq0e6HU8M3cGkcSSk8Fct9rho8eU7ZryWSThgFGygmx0Pr6va65J8Zjnz0Cv3tczcq8s6ccbapj5oYdRt16kzeGLKTMWraccLbVTy928dQKGl3XcRt55w271VlgOZD1QcwLF53B0USeN52Ncqgp8B3RTu8YiZQhYQtyniPnZ2X4GXrxCspG7kwTzJR9H2WKinh827IosI5CYCbdyvsuZLVlUGOKvjfTg5rVOy5j-T9xddH9VWEMLJ_e3_6IvrXS9JyWzqpIw_HSD09Xa4NoD6581Wlq6i40oo8eM0x6BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/197efe458f.mp4?token=ed5NbJR6PPLHXNEfAqwfy9Q1Z3aGn9_WnOO3Ai3Iln9nmiq0e6HU8M3cGkcSSk8Fct9rho8eU7ZryWSThgFGygmx0Pr6va65J8Zjnz0Cv3tczcq8s6ccbapj5oYdRt16kzeGLKTMWraccLbVTy928dQKGl3XcRt55w271VlgOZD1QcwLF53B0USeN52Ncqgp8B3RTu8YiZQhYQtyniPnZ2X4GXrxCspG7kwTzJR9H2WKinh827IosI5CYCbdyvsuZLVlUGOKvjfTg5rVOy5j-T9xddH9VWEMLJ_e3_6IvrXS9JyWzqpIw_HSD09Xa4NoD6581Wlq6i40oo8eM0x6BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گشت جنگنده‌های ارتش، کرج
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/125388" target="_blank">📅 22:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125387">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSjavF8uvRtcDpM1sGC5a3rPcQyjTs3OZKMsaALulPUZrwCgYWwBqF2Erlf2460yTcpjal_ftOScOucgwuI7jkYU3T13tJwh2PVWT3mwTfBLkvxNcmhFaFMHzyEKJanI3MRJ0zaGwUxPnY33hzffB2n5jrVs7b91_nqqwF7u31Fc-8r7Zb8KlXXr7T012i_qOGE0h0kmoL2IZmrp2c6YDNDF23NmHX1fHc0EgTl_XIKDsGLqDVZHl80MiEXmYYrSAc83SoVkQkZKwU7qeY7d-QdhDMFENNQ-97OXwtFbi4wY73ZImy-nhOa_J6G2EMWvv_DC-D0uQv6FSrdCchfV_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آبراهام لینکن در فاصله ۲۸۰ کیلومتری از ایران مستقر شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/alonews/125387" target="_blank">📅 22:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125386">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pA6iQ_S6Nl-xELiBkcykqggeLJ9i_T032QrJNyoUIEihpWrLHrMf7Or4D0Wb06pF-hHays_oeuTZ40ddiL6DJANPn0DnlsLMN8AtqIydJPo5Hx2tmuulxrFoNKxr_hK222ooL_qKeLEfj5SISE96meyzgv_GQRQHl2IIVitcdbv1-3jky84SNJDlaXZfyGGAV2m1dc6FloluvL6lneo3J3xEyyP6skVc4ye7zQQFPaWoXHfdQlKobZQQh2nlu8IJB7QbvsRgpAuSSHSHveBPzMu1RLhLIE26EXDBtgmpBQ6UL6cAACVLzLatDJcOEXuQe_S-sbIG_t8-yy8uvaEnnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیت کوین باز هم ارزان شد
🔴
۵۹ هزار دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/alonews/125386" target="_blank">📅 22:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125385">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee89a57631.mp4?token=ZKkzyzEHJM4-OiunWTRcg5HFfafMjZUVBOE5IJsk0JV9v5liJ149gcTJihTSyddx84NcsI06oC_r1fPB_IQc1240MqS3zOQ89MUDrT60g2lTTE0CMWxdOaH5OLhKG_ifeAr8QQdknCMKFXo5cU42676s3hfm-4kJ2MLH5wzDn58e7NPD3F2sT-K8_anqj4SMOPUi57tMF3AqKhj0QTAA_BkSGxsJQ-P7yJTm8BLmG1EzJXNR4sKmUZfK2yjQzYmInp_fhnnATM6-HGtHJOYQwi9KTSkn8bu1XqvyhZOQxN93ojfx__xuMm1slmn3pzbuMm_FCEsbRP7bixc608rSGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee89a57631.mp4?token=ZKkzyzEHJM4-OiunWTRcg5HFfafMjZUVBOE5IJsk0JV9v5liJ149gcTJihTSyddx84NcsI06oC_r1fPB_IQc1240MqS3zOQ89MUDrT60g2lTTE0CMWxdOaH5OLhKG_ifeAr8QQdknCMKFXo5cU42676s3hfm-4kJ2MLH5wzDn58e7NPD3F2sT-K8_anqj4SMOPUi57tMF3AqKhj0QTAA_BkSGxsJQ-P7yJTm8BLmG1EzJXNR4sKmUZfK2yjQzYmInp_fhnnATM6-HGtHJOYQwi9KTSkn8bu1XqvyhZOQxN93ojfx__xuMm1slmn3pzbuMm_FCEsbRP7bixc608rSGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
جاویدنام ‎مجیدفرنیا پدر چهل‌وشش ساله، هجدهم دی‌ماه در چالوس با شلیک مستقیم حرام زاده های تروریست‌ جمهوری اسلامی به قتل رسید.
🤔
شرافت و وطن پرست یعنی مجیدفرنیا و بیشرف حرام زاده یعنی عرزشی جیره خور.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/125385" target="_blank">📅 22:33 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125384">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
ادعای اکسیوس: اگر مذاکرات به مرحله دوم پیش برود، تیم کارشناسانی که با ویتکاف و کوشنر ملاقات کردند، باید برنامه‌ای برای دفع مواد هسته‌ای ایران، چگونگی محدودتر کردن برنامه غنی‌سازی و روش‌های راستی‌آزمایی پایبندی ایران به توافق تدوین کنند
🔴
برخی از کارشناسان هسته‌ای که در این نشست حضور داشتند، پیش‌تر نیز با کوشنر و ویتکاف در عمان برای مذاکرات هسته‌ای با ایران قبل از جنگ همراه بودند.
🔴
یک مقام آمریکایی گفت: «این‌ها برترین کارشناسان هسته‌ای آمریکا هستند که می‌دانند چگونه مسائل فنی مربوط به توافق با ایران را انجام دهند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/125384" target="_blank">📅 22:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125383">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
خبرگزاری آکسیوس به نقل از مقامات آمریکایی: واشنگتن تیمی متشکل از ۱۰۰ متخصص هسته‌ای را برای شرکت در مذاکرات با ایران تشکیل داده است
🔴
برخی از کارشناسان هسته‌ای که ویتکوف و کوشنر با آنها دیدار کردند، در جلسه‌ای در سلطنت عمان شرکت کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/alonews/125383" target="_blank">📅 22:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125382">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
آکسیوس: فرستاده های ترامپ روز پنجشنبه به آزمایشگاه ملی در اوک ریج، تنسی سفر کردند تا با تیمی از کارشناسان فنی مشورت کنند که ممکن است در مذاکرات هسته‌ای با ایران نقش داشته باشند
🔴
مذاکرات در مراحل پایانی خود است و مشخص نیست که آیا به توافق خواهیم رسید یا خیر.
🔴
ترامپ درخواست کرده بود که این توافق شامل یک مهلت ۶۰ روزه برای تکمیل کاهش غنی‌سازی اورانیوم باشد، در حالی که ایران ۹۰ روز می‌خواهد.
🔴
اختلاف بین واشنگتن و تهران بر سر میزان و زمان آزادسازی دارایی‌های مسدود شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/125382" target="_blank">📅 22:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125381">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
خبرنگار : با کمک اسکورت‌های دریایی چقدر نفت از تنگه رد شده؟
🔴
ترامپ : خیلی زیاد، نمی‌خوام عدد دقیق بگم
🔴
مقدار زیادی نفت داره وارد بازار جهانی میشه که خیلی‌ها اصلاً خبر ندارن
🔴
برای همین هم قیمتش ۹۷ دلاره، نه ۳۰۰ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/alonews/125381" target="_blank">📅 22:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125380">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f50084c22.mp4?token=RHX2au1iTrSdGWkvRshZC7xx3MQrLM-rIWib42UhRXDjlK2OBouCtOkh1XJH9EemXQOtrq0FARncIbTdWBF6k5hdaboA0Y8y7Gn-LKvB9sD54TzRYEyaLJUA-qwxw58vA0_iHmivmBJwa2k0txy1q_PGodYt13_GSQThCUYSSABxrJ3Uqx6lC8DglpEQ10DR4WcPPEU_D2hWqDHbbOGGLdF5c7V8wPftlogvGkNf_XUDJd-OAYqYxfoPC23eIrhJOUJ6alIuO-azYmRNa1c0Xdy3prpXDM8TMzDSgmAQm7Zqg5XX4C8kxsK985Nqkck0FKDuVNrmWrhV4Bjh_-RvUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f50084c22.mp4?token=RHX2au1iTrSdGWkvRshZC7xx3MQrLM-rIWib42UhRXDjlK2OBouCtOkh1XJH9EemXQOtrq0FARncIbTdWBF6k5hdaboA0Y8y7Gn-LKvB9sD54TzRYEyaLJUA-qwxw58vA0_iHmivmBJwa2k0txy1q_PGodYt13_GSQThCUYSSABxrJ3Uqx6lC8DglpEQ10DR4WcPPEU_D2hWqDHbbOGGLdF5c7V8wPftlogvGkNf_XUDJd-OAYqYxfoPC23eIrhJOUJ6alIuO-azYmRNa1c0Xdy3prpXDM8TMzDSgmAQm7Zqg5XX4C8kxsK985Nqkck0FKDuVNrmWrhV4Bjh_-RvUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: بازی فینال NBA که شما می‌روید، ارزان‌ترین قیمت بلیت ۸۰۰۰ دلار است. مردم عادی آمریکا نمی‌توانند این رویدادهای ورزشی را بخرند.
🔴
ترامپ: می‌توانید آن را از تلویزیون تماشا کنید. تماشای آن از تلویزیون تا حدی رایگان است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/125380" target="_blank">📅 21:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125379">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ies0GCkMyV0XbC1k6ZCDYfP070-JoKbzfKnx1HFSCJ4xAMgFIyVvkTvGiPy7_cSFA7KsnHKP8Pj7gHcRCRZXfxOM2FLI-R-8OwqgQZeT-F_yhEtzlt5J7TCf2G6iIkgUb5e_vVhOk5zrQKCnuiJuHpfGDFWGKyvwKOdKzqSncIgd5Jl00kUIDLjcgCJ_eYqAA4-2AB7d1cdkMIAT8agVtXFaKIEJu-jeOSvF1iFaBEZ4RlW0WbDLfJKMpU9BseULGCvdXEndnGMadgP7WOsMVvt1r-mNzX5MNvOKdWVswjuCTVFitLXhjTWCXsHt2ytb3vSxcUMxZCU7Xl3hcVhwVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/alonews/125379" target="_blank">📅 21:58 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125378">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
ترامپ : کلی از نفت با کمک آمریکا از تنگه هرمز خارج شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/alonews/125378" target="_blank">📅 21:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125377">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
ترامپ درباره پوتین و زلنسکی:
بگذارید خودشان حل کنند. من کسی هستم که آن‌ها را به این موضع رساندم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/125377" target="_blank">📅 21:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125376">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
ترامپ : ونزوئلا داره خیلی خوب پیش میره، ما داریم خیلی خوب با هم کار می‌کنیم
🔴
کشور خوشحاله،مردم آمریکا رو دوست دارن و الان شرکت‌های بزرگ نفتی دارن همین الان وارد اونجا می‌شن
🔴
و ما قراره میلیون‌ها بشکه نفت استخراج کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/125376" target="_blank">📅 21:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125375">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما در برابر ایران موفقیت‌های بزرگی کسب کرده‌ایم
🔴
آنها در موقعیتی نیستند که سلاح هسته‌ای داشته باشند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/125375" target="_blank">📅 21:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125374">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
ادعای یک مقام آمریکایی به الجزیره گفت: ایران قصد داشت مذاکرات بین لبنان و اسرائیل را مختل کند تا بتواند اعتبار نجات اوضاع را از آن خود کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/125374" target="_blank">📅 21:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125373">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
محسن رضایی در گفت‌وگو با سی‌ان‌ان: اگر ترامپ مذاکرات را جدی بگیرد، ۲۴ میلیارد دلار برای آمریکا مبلغ زیادی نیست.
🔴
اگر او می‌خواهد با ایران به توافق برسد، این ۲۴ میلیارد دلار آزمونی برای اعتمادی است که ایران می‌خواهد به طرف مقابل داشته باشد.
🔴
این آزمونی است که آمریکا باید از آن عبور کند و راه باز خواهد بود. این پول ماست، نه پول آمریکا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/125373" target="_blank">📅 21:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125372">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a301b042bd.mp4?token=RIttrZ-xK94MHhVG1Ynug4tOji7bl2VOXDpDLy4xcX6X8RL4lTJ6XWAXA5lf_-u6SKpDyhkfbPoels70uoBhrwgjZqBgxaEicv5gDjhsnxk5BTiZJCI1YFD8jH7abDzGDR0MU5mD_7f2oRspIWw4BLt7O0P4KCfWuiorA1z6ds_DkYwcLYV9UjRF8plrJbCOcwiCYgDTTMOq8VGJ9xtPFpBFbfrBPnVvq1iOhE-iUcj9B7YvLdZ-XVXKNarTmCLDuDGuSAwlPMGqWLajN1fWyZ5afTQNscDlhcMdIBRCKJuWsREcX_Ff8_7uUBtAs6nnUQ6xr6_KuAzKuT0PBvk-FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a301b042bd.mp4?token=RIttrZ-xK94MHhVG1Ynug4tOji7bl2VOXDpDLy4xcX6X8RL4lTJ6XWAXA5lf_-u6SKpDyhkfbPoels70uoBhrwgjZqBgxaEicv5gDjhsnxk5BTiZJCI1YFD8jH7abDzGDR0MU5mD_7f2oRspIWw4BLt7O0P4KCfWuiorA1z6ds_DkYwcLYV9UjRF8plrJbCOcwiCYgDTTMOq8VGJ9xtPFpBFbfrBPnVvq1iOhE-iUcj9B7YvLdZ-XVXKNarTmCLDuDGuSAwlPMGqWLajN1fWyZ5afTQNscDlhcMdIBRCKJuWsREcX_Ff8_7uUBtAs6nnUQ6xr6_KuAzKuT0PBvk-FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ که بیرون کاخ سفید با خبرنگارا حرف نزد، قبل از سوار شدن به ایر فورس وان هم هیچ مصاحبه‌ای نکرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/125372" target="_blank">📅 21:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125368">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NmmuINUWYMzXwrdXQFS_2GxRZLMB7y5J-q-CkQ7tUmO0ULprsDVyTOxKSJPV_xf4B2Hk9lBkfxToy3Zmc5u3S046o5099VyQO5JNS3w6l5p-Xsyu0IJPI881TtrUp3CkzViIlL8LxyKpABwwdsfVz-y-yrw8AkMqq0dRQ9IF-OVLUuUsYBDtgYlAl4ZHJpJFPE2GcVT0cteK0q6l9jV4HYVuvhsqO05OzCUwsOY8bzh1-R8u5M4eB6_bg6onfsMABH8G1Pr018UjOMSduiTOVo4RuwNiRDyKFF6o2QqSdTgrtod4D6veHRwUCAa7GxP5xhMTU1FggsAhyKxy1_pT5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r_OjscryW66_5lErDz-o6Qr8fd2bKJ-9dgbMr4QHtocDxlYrIB7TrWYh7pJUbc9XtuUU0HqTuabkIwB1GSPcjhGEEc7yv6djaxYIFuDaSPLSM0OfFW6nbQI-BDnpY9POTM9gvqqSV-RlxZ2nEAtw1D8xVeB3_DO6AayoW9IHhOVmbS9HcbGk0e6Ehypl3Ld953UItsvCgIHtEwOhr6wujTP_1ugH3oJ-WKMjYb3VO7E5D1FvI4oRsZrwKAFE11fukxo9o4NgWolQTWF4YyWLkqOZOSQSTZNvjUjqNQg5DOBWxlsq-g86Ds9mEMEvTI6N1IbkMXiCf7Hg5AxMs-qHWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ErQEzsGO2DjKe_0Q-jtjJb5bTec2d8ebbQ8jpB71g2CZEm8eJtREb3Ml260vho6wNsE8MwYDF_L1IF7H-3Lz7fcnHRZlUJ9g3IlmqksX6rj404ZtNWs01JqFKJLspFhVZ2AlMk0VatbMDvl_VVj7fbK6inTHJAar3RCPaFFFVM1S1OKR3QEWiDmHhCHF83DX6nJyrvhEI8ur5XMWMWQgwWeQD3QWY93XpZBUoBOA_tvLegjwCgQQzVWHd3v4AyOsYGPr_Lrm8Q9VXqWgst9Thnb73mQPv_cRT0hwsOVBgpo7ranuDb_zlu8SxcoVA7Uc2Gc7_M-BAy6ml3AMB97P0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lS9J-pYOshp28cGARTdLy3XvyQMcdWEjf_ft4szHShvwidjdA1iRs7LMdxQGb2o_ddIn6ImAyNlQBghhOmvCkoLjK72UMOIwmaAg1yORh0OuftVOphz_P6_GyTZZf4BX0gfUs9DbKJtMdRLIO4b-F4Oug2xnWHsNSvXyKMExqZWEVXbW0pwgmb6qxj67cQu3tN3IzPlhtsKpmjC6VK0F4iVljCyETzGf5H_Bcuq01qwm8xXSeshdj5UBQuF9lmVDzifDD4WdGUk92TGBsSHPG8GQk3LxLHuIFtr-U8QTIB6dePiVp91ZtkhrVScXeGUw6Xwx2CMszlPNr1qzpGZBYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
فرمانده سنتکام، دریاسالار برد کوپر، در سفر اخیر خود به خاورمیانه با رهبران ارشد بحرین، قطر، کویت و اردن دیدار کرد.
🔴
او همچنین با پرسنل مستقر آمریکا ملاقات کرد، اعضای برجسته خدمات را تقدیر نمود و نظارت بر انتقال رهبری در ارتش مرکزی آمریکا را بر عهده داشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/alonews/125368" target="_blank">📅 21:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125367">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
رویترز به نقل از یک مقام کاخ سفید: ویزاهایی که به بازیکنان تیم ملی فوتبال ایران برای ورود به ایالات متحده اعطا شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/alonews/125367" target="_blank">📅 20:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125366">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
جروزالم پست: منابع اطلاعاتی اسرائیل، جی‌دی ونس، معاون رئیس‌جمهور آمریکا، را متهم می‌کنند که طرح موساد برای استفاده از نیروهای کرد علیه ایران را مستقیماً در اختیار اردوغان قرار داده است
🔴
اردوغان نیز سپس لابی کرده تا ترامپ آن را لغو کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/alonews/125366" target="_blank">📅 20:54 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125365">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
العربیه: بیت‌کوین برای اولین بار در دو سال گذشته به زیر ۶۰,۰۰۰ دلار سقوط کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/125365" target="_blank">📅 20:48 · 15 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
