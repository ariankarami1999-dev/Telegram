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
<img src="https://cdn1.telesco.pe/file/NrAquYLaHaFqmkMzKByVLcR_g0HLzJADKdD9jnKaEpYjE7t2l4Y0b5CQyosenv9RLuUbvPE2T_dYAd075dzzSJHX1792BUTI13TqTOW-Ezvp9kTD8uqj32n4HDMofTsVHQe4vXxks8qt46NRQXJ98eqrjQrYm-f9wnYDgqFpEcAAMuC1N6Xdx39EzFX48sWW5PsYnjnqZ1B1TjhU7o8-voQUkwbIeLFpJzo9Lmh1JwpbgaXC2kRUeW153RFeJhxbB3xzNQu6eKfmT5KrzcDyr_hr_ljlie5if0YwIDAMqxLhSn53TIAS--gaJcn0tbuoOHvjDMOJrkDwAhNL_85jjQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 96.4K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 03:11:27</div>
<hr>

<div class="tg-post" id="msg-2575">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">معاون سیاسی دفتر رئیس‌جمهور گفته "پزشکیان معتقده دوره محدودیت و فیلترینگ گذشته و اینترنت طبقاتی و فروش فیلترشکن به هیچ وجه قابل قبول نیست".
حالا حدس بزنین رئیس‌جمهور و رئیس شورای عالی فضای مجازی کیه؟
جواب درسته؛ مسعود پزشکیان
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nwyBsb3Q9bbvBjLmE7YFqh8o9rtOhjQGO1mNk1xnqTDCv_dDa0qzIJiaRcUthVsIceyYZ4lns95NcHpLScAB2whwUH9AzSDsQHP7asa1Jv2oH1plV_CEcmL4rwjAL8AfYkG8FxN-guaUmxeWmX5_zTZ7ZxstT0dZrV15k0hXtyniQ6dmWa93_2dv5tC5t9K_zaRD6ArdUWnRvIj4FHM3-133f--WPzt--zMDsJbkX5R1aJBL_WTPMItY5vYwj91vfU8djIyDo6nc5eaIzCYTOpr_6_ayOYu2I4lEHnklIWYj89rLjonO-q9ZxFbo9GbVaS4KfZYe9L62Mfyl3mMn2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Echoes یه ابزار متن‌باز و رایگان برای کارهای شبکه و توسعه هست، که چندین ابزار کاربردی رو یکجا در اختیارمون میذاره. از جمله امکاناتش میشه به پینگ، اسکن پورت، اتصال SSH به سرورها، بررسی اطلاعات DNS، WHOIS و IP/GeoIP، ارسال درخواست‌های HTTP و مدیریت DNSهای کلودفلر اشاره کرد. همچنین امکان بررسی وضعیت سرورها از نقاط مختلف دنیا و مانیتور کردن آپ‌تایم اونهارو داره.
👉
github.com/SinaXhpm/Echoes/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/ircfspace/2574" target="_blank">📅 11:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jZOvFfi6y55fE1euoCuU8_O7sx7TFf7YgZLd_YmjvKhCBmgqz0VG9saREtzQpu1F8krCBSJc1V0Y6zf4iwhC8GaqgvzTFupp6VnFun_jO8RJyEJb35bDanRwQvdyLaV-1zB9UJ-9RVyUPlBb47lEPNgW8ep64tcTnZBqVo3QmWdjHD59J062zw9TsGW6D95SxZ_eJueBwl2lQwZIEoVq2J1HbV88-aBftGCIYbDM0Alsm9BOScATF0rafESNwEPVeAQ-jZlFc60baYYFaooRbYJ8cRTfx_pgpvYhPPnKqxIhJzpp_DFC2-KhfGYVf1d4VsGsyeBIzmvgamH0VwjSWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت بانک مهر ایران!
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/ircfspace/2573" target="_blank">📅 11:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ewjrX9p7tti93VWTZcWXfqlSGVxfpx3M7m7J2YhZbRK32PQl4W0ytft4PN-bPFJFLriFm4RdLzmVZpOeNJF-T3g99ZuT_p3lwABJ265gjzxs3GQtW-WlSizNoLblMkJeBCdX3FwP8a8ifT7StQf0tyVveIK6aE_aCJZ620qCQVLzHwk4FWwMjaUyqc755nJO1Twt4NrqxqF159VzihSxiTybbhPw4wbNxZVJADaR1xHIPizF8mtRQ_zyGQGcUb3wNYYhe-ag6Q8VZ1NoPD3nSj4Uq_HpcolPjHzhc_F0fEDyLNjf8-Ghgpp1ZS_ljbkfVp1h1COXdqVYhRowx1sUSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتظاری که بانک مسکن داره، ستودنیه!
کاربران پیش از نصب نسخه اپلیکیشن همراه بانک لازم است، ابتدا هش نسخه دانلود شده از سایت بانک یا سایر منابع را با استفاده از الگوریتم استاندارد MD5 به یکی از طرق معمول محاسبه نموده و مقدار بدست آمده را با هش زیر، مقایسه و در صورت یکسان بودن مقادیر از اصالت و یکپارچگی نسخه دانلود شده، اطمینان حاصل و سپس نسبت به نصب نسخه اقدام نمایند.
©
alirazzazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/ircfspace/2572" target="_blank">📅 11:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UDt3mqj2v89SxJ8inN_rY0Ee1TMk6NRPquOBw6QZnbi9PbjqhljE_cGmQczYttSt688lRGdDo9wklStQ9LdR7HcQGj9UqfL-_4xw1HtPUM8a19Ez4FHkc_TbMVrcvlhBmnzRnmxmI7jR9APhpm9s_XJErpVAM5krUzXCNq3V2QFgwCfR8ADuQnL-upc658IKAXa_EHqTS39lZT8uMHVR5CG1N_lK9q4TvPkbqTulxfdPPZ3HsLokUabc3pqmu86h_sgU9DYcdDhZwJhAea4_0JcqI7iwfydNeoD7l0ea5Vc2uh3XwIKChy4issDQ1CkHlnLFNNf92ltqoRqJo_zmcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل وزیر گفتاردرمان (و فاقد مصرف) قطع‌ارتباطات گفته بود "اگر استفاده از فناوری‌ها به نقطه غیرقابل بازگشت برسد، بخشی از حکمرانی کشور در حوزه فضای مجازی عملاً از دست خواهد رفت". در ادامه "بستن پرونده فیلترینگ را یکی از الزامات ارتقای حکمرانی در فضای مجازی دانست".
فقط نمیدونم مخاطب این صحبت کیه! اگر مخاطب مردم هستن، بدون تعارف بگه بیایم برای پیگیری و حل مشکلات وزارتخونه آستین بالا بزنیم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/ircfspace/2571" target="_blank">📅 11:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2570">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دستور پیگیری فوری
#ترافیک‌خواری
اپراتورها به کجا رسید؟
چندبرابر پول اینترنت میدیم، چندبرابر هزینه VPN میشه؛ تهشم آشغال‌نت تحویل می‌گیریم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/ircfspace/2570" target="_blank">📅 11:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fRzpTtBN5GmkH7GVyPXRWQ17HpZ4f6nS1xBj08xy8BAbiwzn_h1hXpvM94cBHSIMtMtYoFhLIEV6O2c_6a-OtRe0wf4XyofTA-C66W2cbS9PQx8fUkwsWTaDiIhPB22xG_UX4ACx3AjIjJzfvLcT9DqY-lNvL1fvcgUAHXSBOOtCk6lCE_OqVAaWAajG-Zm4fYrp5i1MevtJps2PwilNOle5hEL7nisafpQC20Bjc-zOYAN7rchuFhM_ziHxucotlRzoN2DO0tAEjjHK80gvt2uVr-2lXfKH2duTUukZw_eClagqprPEBk89y1fCgSGFLGaUIjn8G_CRV1vNUxHieA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پانتگنوس یه ابزار متن‌باز و رایگانه که برای پژوهش و بررسی‌های امنیتی روی فایل‌های کانفیگ VPN و پروکسی ساخته شده. این ابزار بصورت خط فرمان و نسخه تحت وب در دسترسه و می‌تونه فایل‌های رمزنگاری‌شده با فرمت‌های اختصاصی بعضی کلاینت‌های اندروید و دسکتاپ رو بررسی و اطلاعات قابل خوندن مثل مشخصات سرور و تنظیمات کانفیگ رو از داخلشون استخراج کنه.
ابزار Pantegnos از فرمت‌های مختلفی مثل SlipNet، HTTP Injector، DarkTunnel، NapsternetV، NetMod و Happ Proxy پشتیبانی می‌کنه و برای تحلیل و بررسی کانفیگ‌هایی که توسط بعضی کانال‌ها و منابع مشکوک منتشر میشن، می‌تونه مفید باشه.
👉
github.com/FrontierTM/Pantegnos/releases
💡
frontiertm.github.io/Pantegnos
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/ircfspace/2569" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2568">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">از بین همکارا، اولین نفری که تغییر شغل داد و رفت سراغ آهنگری، شدیدا تعجب کردم! با اینکه خودم کم آورده بودم، ازش خواستم جا نزنه. اما بعد از چند جنگ، کشتار معترضین دی‌ماه، قطع طولانی‌مدت اینترنت و حالا تداوم یک آشغال‌نت پراختلال، آدم‌های ‌کاردرست و خفن زیادی رو از نزدیک میشناسم که سال‌ها در حوزه‌های برنامه‌نویسی، طراحی، شبکه، مارکتینگ و ... فعالیت تخصصی و رزومه قوی داشتن، اما در این چندماه رفتن سراغ مشاغل غیرمرتبط مثل نجاری، دست‌فروشی، مکانیکی، واسطه‌گری و و و ...!
لعنت به جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TR_vOiNVv6QNGtAuPGHreh01Xw8EbCk1q50tFqisfNd5buWgiyehPk_IQaEI4hXNVhApsKveHFu09TkZNteth0f0AoaV2OrmR39_O7h1-MDDeMh9xurwJDbjA-5v_lJadUVjRK_rmyJnIUIXaytggcOVBnKioGOb3vnMoAzXHWWo7Am6Yzw7zPFHQy38LDqaLlN4Uq2tBfDhkjL-_PsKY-I3YyeIvLUqb86EWYmm32GFWjIrItecjcfFtRHA-XhCAiVXxMv98XMzpRFnOCU9RZY5YjO2mli9BhezNy_LF1elMerD52f7Kb4dofy_3HDjBzyIU8Ojv979TW2-17hsAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپیس‌ایکس می‌خواد Starlink Mobile رو به یک رقیب جدی برای اپراتورهای موبایل تبدیل کنه. این شرکت در گزارش مالی جدیدش اعلام کرده قصد داره سرویس اتصال مستقیم گوشی به ماهواره رو گسترش بده و در کنار شبکه ماهواره‌ای، از زیرساخت‌های زمینی هم برای ارائه خدمات موبایل استفاده کنه.
©
satellitetoday
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/ircfspace/2567" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E2J8dlSKtK60iug_ntoC31dNoe_huAy-2eybrJtpDkEuQErHnEl4RlT7LIq1O4XJBcRvFvt91WafQFXOx-VHRu_ZRV75lJU6uHp1TEZZtXcltY4AB-5AlTEQp-KlynbxAS6sES-byLx8fRhmpqxNimSPj5O0jc-ZB3pFWW79T1zdPNAzy36zXTday30sL3bEwWG2bFZBbffkRsBcKpeUgPtxEzGG3e2i0xI4pzzp2wepIlvLgeaw3MRMWPAee6MG03x1s7aDeJRLzV8FBA_RWFZaaX2ScXWrQP6AZD2ppEtnNqfmVsQa41mRaprWJ7rOhRndzEA78iPbNXMlQMEEAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا از کشف ۹۹۷ دستگاه ماهواره استارلینگ در ۴ ماه نخست امسال خبر داد و گفت: در این رابطه ۱۶۳ نفر دستگیر و ۱۵ دستگاه خودروی حامل تجهیزات استارلینک توقیف شده است. /ایرنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/ircfspace/2566" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qBvrkOQO_ons5Mpa_9ozZgF06awnTBac_P8oW4nza1ShCoNXwqoseMyqSIwkhZNxAUL6HYLHqpLsHLnZvPyg8X68fV8VmXVSuY8Zz91SY-9bqmEx516678bYrCAMKjcOGgTOwof7_4hU2tXf9j99aS8rXgwgw370U_pTBvzG_ih-z6ShkDoPNLGpcRPEGqakGVV0gWO-MZ_wdHl6bAOlxB9x9UuHTHkI16XQXHQqYJvX_XJeCtjoTbysYe_VfyaadIOEvkVTx4OXo2SRH9x7PxQAsVgu9-eB9frCPs5CEtfw8zlUUa0Fy7S4Ww2RVS5U8wKdLeVas2Uck74tpYqrgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام داره روی یک نوع WEB Proxy جدید کار می‌کنه که ترافیک معمول MTProxy رو از طریق یک WebView داخلی و روی HTTPS یا WebSocket منتقل می‌کنه. در سمت سرور هم این ارتباط‌ها دوباره از هم جدا میشن و هرکدوم به یک MTProxy معمولی وصل میشن.
این روش به سیستم‌عامل خاصی وابسته نیست و نکته جالب اینه که دامنه این WEB Proxy مثل یه سایت HTTPS معمولی دیده میشه و فقط درخواست‌هایی که اطلاعات مخصوص پروکسی رو داشته باشن، صفحه واسط (Bridge Page) مربوط به پروکسی رو دریافت می‌کنن.
👉
github.com/telegramdesktop/tproxy-server
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2565" target="_blank">📅 19:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OIR9DBpMxz3OWJFJ5K6XoSiDA6fpn7MSbpGHuoalAdq8ENEEg1Zdq1k9MAKTGoRjbIG477zT7f6ec0eSkbD30RzNPxAjSsFlM_DJZM1xDA3yyYzCMsttZ67Sq9-M0JOQEVuV9MJ0hZ8W-iX4dAYfqjnZfCL_tojpYIqLuLqi4-vCcAgvh9ktKvEMCC4UbZWs6oCLj7qOFs_bgR-FoAbe-eCJTmFTGZuc0KyUJtFHO8OaLguKMzCH97qzWtjKCKkSljZr39SRkQPKHB61Tklkv0siPXBU1k42B1J9to75M8Y25GfdfUGLAFncMIw7afrIeLUXIeWTNRkk17nU4Z7GLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در کدهای نسخه دسکتاپ از تلگرام نشانه‌هایی از یک پروکسی آزمایشی جدید با نام WEB مشاهده کردن، که از WebView و ارتباطات مبتنی بر HTTPS/WebSocket استفاده می‌کنه. این قابلیت هنوز در حال توسعه هست و مشخص نیست نسخه نهایی اون دقیقاً با چه معماری و مشخصاتی منتشر بشه.
©
telelakel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/ircfspace/2564" target="_blank">📅 08:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2563">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a198ca7RTsx5kiTXHD5cvJPL7hIBpDIPzsqEKalQhRxKgC96qTrrZ_UcOgu4-fl3QuW66l5BaWrD4vuFImdWWrvW259SeTK9y8Scn7IUfWic5QAsk0ZdrO7FV2lfJKPFdmpnZSkeYHTQHPVxZRZ37QzxMlbqgwktlnoHR7G4IRChLZTs0Yyzu87lwMZq8WrmxWqi-Co4-DynhPiGF8tGg9jWH8e_m6VfwpKbJCudEKh5u2Xe5mg6fmiyO4OW3Db9Bk4r2dw1Hy3vdenY4AQO6QdZRzCR8eoXdmKZ9HVElGf5Zivp55dE4baLFUCgqXJ1AwMToSWpw64cUPh_TofKdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتحادیه اروپا با همکاری سازمان ETSI یک استاندارد امنیتی جدید برای VPNها با نام EN 304 620 معرفی کرده که در چارچوب قانون Cyber Resilience Act قرار می‌گیره. بر اساس این استاندارد، VPNهایی که در بازار اروپا عرضه میشن باید حداقل استانداردهای مشخصی در زمینه رمزنگاری، احراز هویت، مدیریت کلیدها و مقابله با آسیب‌پذیری‌های امنیتی داشته باشن و این موارد هم قابل بررسی و ممیزی باشه.
البته این مقررات به معنی ممنوعیت VPN یا محدود کردن دسترسی به اونها نیست؛ هدفشون اینه که VPNهای ناامن و بی‌کیفیت از بازار کنار گذاشته بشن و سطح امنیت سرویس‌های موجود بالاتر بره.
شرکت‌هایی مثل NordVPN، Surfshark، Cisco، Google، Palo Alto Networks و Airbus هم در تدوین این الزامات مشارکت داشتن. از طرف دیگه، ارائه‌دهندگان VPN باید آسیب‌پذیری‌های جدی و فعال رو سریع‌تر گزارش و برطرف کنن.
در نهایت، اتحادیه اروپا میخواد حداقل سطح امنیت محصولات دیجیتال، از جمله VPNهارو در بازار خودش بالا ببره و اجرای کامل الزامات این قانون تا پایان ۲۰۲۷ دنبال میشه.
©
techradar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/ircfspace/2563" target="_blank">📅 07:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2562">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p8-dSzMH693IF_3UsxCAAo1vqULRPKZna1Xc-OgrxFirwtoSw0I9y4s_s4QEkXQBhXSBkJhTRaC6uc7XN8PFJmpozZCFnTYsAHR69in21L1PDoiFUiTxG1dF7gOcR0ZZC3ZcVYVscnbLWDh65EEZ47Ztrnl11kdNqOcz1k0RbinoLChQnEl4mZ3gnBBI7kvigTBmXFq-kESMa7nphv-ZDxweoYMDB_9pEaAnEc7XVKqWwm89l-s5HBCm5jzST3BmwbQqGXTfNgKBYwsKRmp4WsTl2alghmSCYAwKbspdmWjfcYpuAUan2bEXlQHNg1amf-D7MmgcKWOBEVSAN1N8gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم پس‌کوچه با بررسی نسخه اندروید فیلترشکن Line VPN که تا الان بیش از یک میلیون بار از گوگل‌پلی دانلود شده، ۶ ایراد امنیتی مهم در بخش‌های مختلف اون پیدا کرده، که در سطح بالا ارزیابی میشن.
مشکل اصلی و مشترک در تمام این موارد یک چیزه، که اپلیکیشن در چند نقطه حساس نمی‌تونه با اطمینان تشخیص بده آیا اطلاعاتی که دریافت می‌کنه واقعاً از سرور مورد اعتماد اومدن یا نه، و آیا هویتی که برای اتصال استفاده می‌کنه فقط در اختیار یک کاربر مجاز قرار داره یا خیر.
پس‌کوچه این وی‌پی‌ان رو بیش از اینکه سپر باشه، به ریسک امنیتی تشبیه کرده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/ircfspace/2562" target="_blank">📅 07:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2561">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VrJXGp6gsq2YWAtMyqxbLq7SfIqZF70L9Bxa8z7LcOQ1mwdVGoePZY0EyZLIyRbSLrTuCNyXfdijUlekLKUtAuVKXXhBvqhYN33XyCUzLRlMzLy2XFcujUS8yZaUVLLZhp0o_ydE4jCBq5K6RPTcEMUh2wtIO-1ZOvRc3YfQZdGBiSgig-dxr4N9USfEV2hDFOH-rxUPHVyRh6HCeOL-5yD7cj7ngM-Sht5VOqspUwbJ6i6mNkKtwGpdL1zzMll8oyyD19eMMMq1PlyT04QCj_odx4l8i9VOiz_LKrKgS2nDGWqi5NmIEAJaCLtp5tBU5oJoaIybZQFPlDF8kiZSXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران مؤسسه فناوری کارلسروهه روشی توسعه داده‌اند که با تحلیل سیگنال‌های رادیویی وایفای و استفاده از هوش مصنوعی، می‌تواند افراد حاضر در یک محیط را حتی بدون داشتن گوشی یا دستگاه متصل، شناسایی کند. این روش در آزمایش روی ۱۹۷ نفر به دقتی نزدیک به ۱۰۰ درصد رسید. این پژوهشگران هشدار داده‌اند که فناوری مذکور می‌تواند در آینده برای نظارت و ردیابی افراد، به‌ویژه در حکومت‌های اقتدارگرا، مورد سوءاستفاده قرار گیرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/ircfspace/2561" target="_blank">📅 16:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2560">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ایرانسل و همراه‌اول فکر کنم یه بسته رو به چند نفر میفروشن.
©
ali__m___i
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/ircfspace/2560" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ظاهراً پلتفرم شنوتو، میزبان هزاران پادکست ایرانی، توسط کارگروه تعیین مصادیق مجرمانه فیلتر شده است. طبق قانون شش نفر از اعضای این کارگروه ۱۲ نفره از طرف دولت هستند. دولتی که در «ستادش» اعلام کرد دیگر هیچ پلتفرمی بدون تأیید رئیس‌جمهور فیلتر نمی‌شود!
©
hamedbd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dyMh0p2FR0ofhA0oemBSbmydEyEx5f8BZXiVzDCAFGm1QCNLAlc2S9wp3C4YE8fjKf7m5n6fGf61vwSQY5S0jR9NAdp8adIIazXFKk2rcHCpHeD464ZmXtGQmxt7WM252utviEMb3InWHrQ6gqw7_62rURW2hy9uVpzjfPxTM-8FdiiU0OwTakO3UC7vqYwvrABCoahsfOakbGqG2_epOLYygmcSYsmWLmrkHCeEEK1-3MVe3PICcf84_-DhkRWxTQRsXMkjuFNVKOXuYeWFmxoPhPZfE_9_Uas7iif-KPhcZupeSQlGxKB1KOXNdTDlGvOfx13xsEoO_x5HNh8Z4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران شرکت امنیتی Socket شبکه‌ای متشکل از ۷۳۷ افزونه رایگان VPN رو در فروشگاه Chrome شناسایی کردن که عمدتاً کاربران روسی‌زبان رو هدف قرار می‌دادن. این افزونه‌ها در مجموع ۷۵٬۴۸۶ بار نصب شده بودن و ۲۷۴ مورد از اونها با جعل نام و هویت ۶۶ سرویس معتبر از جمله Proton VPN، NordVPN، Surfshark، ExpressVPN، CyberGhost، Windscribe، TunnelBear و Cloudflare
1.1.1.1
منتشر شده بودن.
بخش عمده افزونه‌ها پس از اتصال، تمام ترافیک مرورگر رو از طریق سرورهای SOCKS5 تحت کنترل یک زیرساخت ناشناس عبور می‌دادن. در نتیجه، گردانندگان این زیرساخت می‌تونستن مقصدهای بازدیدشده، IP کاربر، اطلاعات SNI و داده‌هایی رو که بدون رمزنگاری HTTPS ارسال میشن مشاهده کنن.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HzUF6if1PUdjj6Ra-xfOnof5pXHg3_d2mZ2kf6wbhQN3ZbGHXtoBRF1brEOmpwim3841HODjP2ViCEyx2WNPnusFw5alC2ryB7i6I-sbQuj0oJMZiCUkhRLSwNeeP32hGaMw-DEsL_9tIQ5Nj_QL-c4E6DFtL3qnWMvZc2vgeTJjVguDNRYWovdtvXS8aW8_K3Up1h_LgQoSNGpYKoj992RluNRkDJFVopt4AfrYdgr7kdiFGYC-SWcFGA7TUqXdlLLVf0t4JRe9Q9d4VRV2DcdmBPwBd18Cyz86sqoPpZGd2sb3jA_yObXW5Y1H0V4XLmx7XoDEJvmYBDSyf7O3zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ WhiteVPN یک VPN متن‌باز و رایگان برای اندروید، ویندوز، لینوکس و مک هست، که بر پایه‌ی هسته‌ی Mihomo ساخته شده.
این برنامه با پشتیبانی از پروتکل‌هایی مثل VLESS، VMess، Trojan، Shadowsocks، Hysteria2 و WireGuard، امکان اتصال از طریق سابسکریپشن یا اضافه‌کردن دستی سرورها رو فراهم می‌کنه.
👉
github.com/WhiteDNS/WhiteVPN/releases
💡
github.com/WhiteDNS/WhiteVPN-Desktop/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">قوه عاقله برای بار نمیدونم چندم دامنه
workers.dev
مربوط به کلودفلر رو فیلتر کرد و مشخص نیست بازم از فیلتر دربیاد یا نه. بهرحال "در سر عقل باید"، اما 404 مشاهده شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اینترنت همین الانش هم طبقاتیه، چون هزینه بسته‌های اینترنت رو اونقدر بالا بردن که دیگه خریدشون در حد توانمون نیست!
©
Kiyas
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2554">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اینترنت ایران باید به لیست شکنجه‌های تاریخ بشر اضافه بشه ...
©
thepanue
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=TTLRxRBEQddiYa2yMeXh6W-_35iKS7L3m2_cOVwUNvipr3VULhu0CaPR0wDMld-jPuitLe4L9SvjPqHJiA8lY5T4yNbbNlxIjmOtuoe3kbHIdLbMfAwUHdv5vASK_eUrPsVBJ9OnstY1wJDeITd1yRGJeSp0x-VDOx3ilHsunK_tTyPJ3vCwHegTCk6EDxJAfudrw1ajc__BPqbIW9QSm_A6nuvjovd0b2BZQdm2p8E5iLzfPs_q32UrZNWqOszex4qfEW06WSXfaa-wsdNgiqIKp0Joh0VJBtQxXq2fQ2IN17EqIXxfdeQt72_CbR6M_ucNmu55NqmTlISaU0c59w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=TTLRxRBEQddiYa2yMeXh6W-_35iKS7L3m2_cOVwUNvipr3VULhu0CaPR0wDMld-jPuitLe4L9SvjPqHJiA8lY5T4yNbbNlxIjmOtuoe3kbHIdLbMfAwUHdv5vASK_eUrPsVBJ9OnstY1wJDeITd1yRGJeSp0x-VDOx3ilHsunK_tTyPJ3vCwHegTCk6EDxJAfudrw1ajc__BPqbIW9QSm_A6nuvjovd0b2BZQdm2p8E5iLzfPs_q32UrZNWqOszex4qfEW06WSXfaa-wsdNgiqIKp0Joh0VJBtQxXq2fQ2IN17EqIXxfdeQt72_CbR6M_ucNmu55NqmTlISaU0c59w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ممد ساخته. یکی از محمدها، که نمیشناسمش و قرار نیست بدونیم کدوم یکیشونه؛ ولی باهاش کلی خندیدم
😂
©
Mohammad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/ircfspace/2553" target="_blank">📅 10:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mYnha2mYMqKnKc-GkhVL8Cr0gm9yPkjdBa_zuRQZlOHYTgG1kN7zpYbmuGgSZUWhFnaBK9E7lqKr23ZXAib-Js5kE5MvIV1w2Ku_PJ2aOPdFSu-F9pjCQXS0RzokoGbsMftsM5ZG2E8jZJ2FV00Z8Wb9_M79IVYKzjkWzgeRneNp1CpnrupnwPTQuQIZcqIQOH_8yNlzNcxnFGTbknUCV6cEPMk9quF0Vm7lojFOx1nIiwNLh7nOUrjZZfCl0w3C-BPy8QIu5junYnma-M8fRDA5pi8B2uNyKEofjf2HDYvptIXZ0SgYdyV3driYv27jH46CBf8OCWDtt_oImcBK3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکثر آنتی‌ویروس‌ها (از درپیت تا لاکچری) سایت بانک ملی رو فلگ کردن، چون سرتیفیکیتش منقضی شده!
©
Teeegra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nJblDOKhspVb86AzN3P_KnEldP-OwWtv4zWrO2imYtPQw4ZM3HKF_j3hGI6RQLszKGHuIm9IEBSxRqedtCVUOZ1AIGtidPaA7bcvS50pOcsHyP2GmfV-NnTU5sVwgeDYojQTsXVurIf844XyrOpaS6YrN3pdIqGhrN1iLwRr95FLIc_iP1xE9wFN34vo_jxcxivSM0Owg4gUiLhjii_vTFSsHXWwcSsdJOLLLfKvd2a1WmtCia9Mhid9LevvV0gaZSjSSC9T3uD2mqWYQAgd_ocBOk7ilZLs4K7YGMXmbdI6xKXfJwMyUr8-HoX354UPPIgH7crdMAcgrhZ_-qiZvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات مخابرات گفته دستورالعمل جدیدی برای محدودیت VPN روی اینترنت ثابت ابلاغ نشده و ممکنه از مشکلات فنی شبکه یا نحوه عملکرد خود فیلترشکن‌ها باشه!
🤡
در رابطه با اینکه اختلال‌های اینترنت وضعیتی فاجعه‌بار دارن که جای صحبت نیست؛ فقط اگر بدون دستورالعمل دارن گند میزنن، یعنی دیگه خیلی کاسه داغ‌تر از آشن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2549">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ObNgKrM1V-jCR5vkkoF4IjfWMgyrSRKhaB39lXFIF3WKxebhTbrNIZfiBi-AHjeqnuwV_e7wg7wp2WE3qrEPR-XrOv6HD0FA2uiaSY_af-7klLZoEIcnSvV75zjukFKxlPlzMHRrgc0lMBRnR105bLuqH9Vces2TOCYNS92oRGIiniqE98RBYeNoB-vr2Dz8kJqpY4YFC5upf9ssNy0JKqLgXSTsjmx2TBLoacvgZE1wVH-KgpJhFV-t3Gs0UL_czzht2QG5L-S5g0C0-B9I8mLdxyjkEtSM5oaRTL1k3vE53jdHT9Sj5aSHKgZ7LMuGGOMeQHdjL908pD_sWlkG8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فیلتر شدن فوتبال ۳۶۰ و دستور رئیس‌جمهور برای پیگیری مشکل چقدر گذشته؟
هنوز نه رفع فیلتر شده، نه کسی فیلترشدنش رو گردن گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/ircfspace/2549" target="_blank">📅 09:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2548">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tCI4BEgxeLC5Sl_VHwtn2Sqohsi4edvKGItnKI_deM-vL9YFukbk2KFXWxpqsVNVdAGHQTmGXKv6v1zzrCkEEZLzSaykweFhLYrzgTNS7IT3HgxOB4knq57mHB4MNy7wnWhIp4VjQMOUGN-ApgLKdxqbqFGu2WuTFvTMk55FqpmhZxMRPhwi116AuAo7qlP3rh4HOQ45WpCT5Uq0JJa0fsbN5W5Vjcf_f_QComp0Xaajcs9U-i4wkmqOzFHNm7EgEzITALaSPbskIV_umFU4LepGx-oVOSyDrelzBdyCooBkukojHwIqJXysFM71a8BhBuCVV9cIN-lKo3y2LGQfnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلتفرم لندین که برای ساخت لندینگ‌پیج بود، بدون اخطار قبلی فیلتر شد. بعد از یک‌روز که با تعهد در دادستانی رفع فیلترش کردن، اعلام شده دلیلش فروش آمپول لاغری در صفحه یک کلینیک زیبایی بوده!
یعنی هنوز که هنوزه نفهمیدن فیلتر کردن یه کسب و کار چه آسیب‌هایی داره. هنوز که هنوزه نفهمیدن وقتی یک صفحه محتوای خلاف قوانین داره، کل کسب و کار نباید فیلتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/ircfspace/2548" target="_blank">📅 09:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DTq840xsCBx82SqeED9oqHnOSAMKrrP6Yo9iyWG5MsgiCI1XM53sKy_qO1tzI6oDjPFKMD4aVQMiO1QJHLozDnSOI6y6s8PxqQvVHDw1urqwjA0ZubTa9EhGfFkwc_dSzPnZSeaKlngYXO7LtVZllmNxAXO1FY4iZkiuWxJCzniu71Sp6A0Qqpj-E2nSEL5rkxJPE31j6qFQL8iqzhvb_IY0QAkZnjKagou2OaKBD1ChP8cLt70Zi-UX6OnqafaL6EcSeB7zL3urFp0X1HDfKSd1XLJjutqlX4PCE5lyNoSYTD8t6guRWgx2E46uS8skkd4j8Krmslu2WXe834QfTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با قطع سراسری اینترنت و نابودی هزاران شغل، هزار میلیارد تومان به پیامرسان‌های رانتی کمک کرده بودن! همون پیامرسان‌ها در عین دریافت پول بیت‌المال، اختلال داشتن، ثبت‌نام جدید نمی‌گرفتن، محدودیت‌های تازه گذاشته بودن و چشم‌وچار مارو با تبلیغات کور میکردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U0mFR05ZHKFyfRoJW22_cSRF-yhCj1gMFx3yupeZ83dbC7oHpWcqmgqfd7bVrTWqYrv6zDDVCECTL_t_mx1-k-55msMxXL3O5wy7ysbaGb0J-xojsNZlxgGFElNxunTZpGvSSCg5jtAaj6tPfFJL1DLDIJ14ZM5Sy7p53F9I-YPWqexw6ZWYDVylE-v_sa0ULl9GLnAsx4VasJcS_z6J30IoO4aC0vvud_3YDJii8F-nLalYrt3qnG-nrwGHOrI-UaGjQh65FACESrka2pxdLJppbcVa83dI6SNJebqCRraO--j56ah9kyuaseF34YeUnMbySnMJIAptOaDwisXDGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه عده‌ای از عناصر فرصت‌طلب سودجو عنوان می‌کنن اینترنت قوی و زیبای ما گران شده است. برای شفاف سازی میگم بسته‌ای که شش ماه پیش خریدم 1,348,000 تومان، الان شده 3,870,000 تومان. قیمت فقط ۳ برابر شده، گران نشده.
بنده هم با ارائه سند میگم اینترنت گران نشده، فقط ۳ برابر شده!
©
mrweb24
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UMJF-z14xTAiZwWUUJTvd_mBc114VO6bhtjVD-npWL4fl7HBNb4UL3vXW4SeIh5yXYym5XXbO73jR-6Pz8w1IghuOMPz1nthB4DUwHnFHUOh87Q4Yv_Td1SNTh7DsfdO_4ryTzwjBWQrzpyAvaVbisY0RXgtNrQtwC0-bp9sWvyLK5p5h1cHoruclzAR74Z0h-d2QYZGfoAqhX0gOvtdYl-eS9znshHyQuq1fSJrMT4Vd6dqP8qR-j55i4WMKGZSlGChPdJ-Ea6XSJQTNJetho5ZwwmHFStMPfHtXv3NzuyoKPZ4JSxtWBQwf_4OzG688Hn839WEf31gxng4Oibz1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگین چرا با وجود اینکه چند روزه اختلال‌ها و کندی اینترنت شدیدتر از همیشه هست، چیزی نگفتی. خب الان گفتم؛ کدوم احمقی قراره حلش کنه؟ همونو بهم نشون بده!
ده‌ها پیام داشتم که نگران بودن چرا چند روزه نیستم. غرق در گرفتاریام و گاهی حتی آب از سرم رد میشه، ولی دوباره برمیگردم سطح. نگران نباشین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bRgNAHvfcc3_ULQ64U21PZseK0OxQi0QRFROWbm9nS6BqppuDU5UU1IzGjSqu1I3oVQlPWMmK1fK4yb83uODH96piqkf6YGzvf5Ijl6I4brYZdUas3YbmOgklY1i95B8AcmecuECtIHJlFbo_zHtYrka91vCWrcGD04vDbT8Kg1WiMy_VtJQ46JM3QSypGi7H94T5BWG_-gVFnn_Y9_024jUR7uEQZm1yAU_HZzNZIlpKJm4qibAdN4vkIszF5m8HGRM6BLipeA5qfAvbPNymJPm7CXn7zJnauEU6MivpnoLFxOlUb7wUY_S8rTVggvE6TbX0eME4NRW7TrdTAlFtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر لو رفته از وزیر قطع‌ارتباطات هنگام رونمایی از طرح تشویقی "نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی"
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/ircfspace/2544" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2543">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">این قضیه اینترنت نیم‌بها و ترافیک تشویقی برای استفاده از سایت‌ها و سرویس‌های داخلی واقعا داستان جالبیه. فقط ایرادش اونجاست که کاری می‌کنن تا سایت‌های داخلی روی ملانت باز نشن، یا به حدی کند باشن که بازم فیلترشکنت رو روشن کنی!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/ircfspace/2543" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2542">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">چند پورت مهم مانند پورت ٢٢ از سمت زیرساخت بر روی آیپی‌های ایران به سمت شبکه بین‌الملل محدود شده است.
همچنین شواهد و بررسی‌ها نشان می‌دهند که ارتباطات زیرساخت برای ایجاد یک قطعی گسترده در حالت آماده‌باش می‌باشد.
©
manageit
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k9-Tjr8Tlg0_zaxmuigbNEtJDXJ9uG-MWf4qGW7gCphWedDyUWThijAGzFLf98eBtk6hMcZL2xh-9dcwyNrnvygpbjbimOPQyLQ7ReGoMdsgGQuWBU9XThuTd5d0V44UuRUeovTo-eAwjWbAGesHndw0p1R_kbGrrSvArQlQR12_3IDqwPm2L84cz2kPe_25OMk1vnBEn-8o4DXs1XdN4zR18yp3sTSnGhPiVS2dLMYAKLmKJRFCB4TonNfQtvzphc8OUNXX83alDILzhGLsIB3r3gOtCqy6oufcCd_-UykwY4MS0fwYmX28a7S9eLMp7uECGc8DJKwfRp2-uX0BwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشد که بعد از ۸۸ روز قطع سراسری اینترنت به جای اینکه بیرون بندازنشون، به نمایندگان حکومت تریبون دادن که در اجلاس جهانی اینترنت سخنرانی کنن؛ بعد دیدم این اجلاس در چین برگزار شده!
روابط عمومی وزارت قطع‌ارتباطات گفته نمایندگان جمهوری اسلامی در پنل‌های تخصصی اجلاس جهانی اینترنت که دیروز برگزار شد، مجموعه‌ای از پیشنهادهای راهبردی برای توسعه همکاری‌های جهانی در حوزه‌های اقتصاد دیجیتال، هوش مصنوعی، امنیت سایبری، خدمات ابری و تاب‌آوری زیرساخت‌های ارتباطی ارائه کردن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2540">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">چرا کسی از این موضوع که "سیمکارتایی که استفاده نمیکنی رو واگذار میکنن، در حالی که طرف با اون خط اکانت تلگرام داره و چتاشو شخص جدید میتونه بخونه" چیزی نمیگه؟
©
shara77miaa
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/ircfspace/2540" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2539">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YdYQd0bX3Nd_Q6qe_5LHg7C5bQeDFt00c95HtBUk8nHyPhRrEzE8qRjqeLA6SM_Hn6CI7HyzIv2TrBhnvr-krdMIuWlcp5EF8fwywBcppioRN0Q-XjfNDuUIolLCm3aPJVZ5kgnLCD-RnsLXlEonA4Nj6pErlvX8PqXEf82Rb8vMCoD8r-15Gm5SOuWSBUO8GE_cbh_Rx4Wg0hvNe1e9ndoZbEXSPQcX-vI6-S6LV1d6LNMi0_HUx7QrRMwM9R2UMH5dt4o6PUcxCsl_DcBCZ2bHTI17hCvvD4biro7gmnG3k6coB3_zct0G_pxZAXP7QzLV6Ug6mc2ipsGvAcJDkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین داده‌های مرکز آمار ایران نشون میده در بهار امسال ۶۳۰ هزار شغل صنعتی از بین رفته و سهم صنعت از اشتغال به ۳۱ درصد کاهش پیدا کرده.
حالا این آمار رسمی مربوط به مشاغل صنعتیه، ولی فکر می‌کنین آمار خسارتی که بعد از قطع ۸۸ روزه اینترنت به درآمد و مشاغل اینترنتی وارد شد چقدر بوده؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/ircfspace/2539" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2538">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/upJ-aZ8cinGCnj0LSmG6lPLJYAzwadXftqKicQ_H2GiGeeWxqdpEAATSic80tAOYo6kU955wZDVB4Oi0RjyaaQ99PKRDcwHs2Y5qDfO-6LEFsS--wBWiCGmJO2fdFKY2T17T5sRfBHDkWNpfDU-IfpwzPPj6qQ2qcc--M0qxhIA7tITNubggZFkrZYlbRGS0AF1VSb3K7GciA-zTYNATvGAEuMvV_WIfWrGNsw6vrnYmzGyxfMXgGsKf-bi-mTe_c0dvSd56aZv8yRyJnkzrmavh-fDoTzg1XjPzq3tYT_k9YP5qR5rgdRonhwA5BG8zi-rBCPJB-iHj_2v0N8F4cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه کسی و با چه مجوزی تصمیم گرفت ضریب بسته‌های اینترنت بین‌الملل رو بدون اطلاع‌رسانی تغییر بده؟
قبلاً ۵ گیگ اینترنت میخریدیم = ۱۰ گیگ داخلی بود! و فقط پول ۵ گیگ رو میدادیم. الان پول ۱۰ گیگ رو می‌گیرن!!! فقط نصف اینترنت بین‌الملل میتونی استفاده کنی! بی سر و صدا دزدی میکنن با عوض کردن مدل درامدی!
غرامت قطعی‌های ماه‌ها اینترنت هم هنوز پرداخت نشده. این دزدی سازمان‌یافته‌ست که با حمایت وزارت پست و تلگراف اجرایی شده !
©
iSegar0
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/ircfspace/2538" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Pi3HyHONh3yxM9d_mK-c17QcOEZiJZGPx-F0ewdurgAPCEkojVKvsqVNLQ-_5PCQgVP2Pg5raDHdJHNpC1CjcSvJl2oZKrmdj4ToeAjJMmoL-5wxkvavH9KzRPcre63R6mIRD4pLl0BvLaeq1cepyFXQP_3FUcRVOdGtfdrKnjSyeI9vIWtyFDHKlADs3IxUlVOFCsBiV1bJgQ9wV47aTAZ3O0W6XWz2QQgqKk8nLThHFD1L38nGyYmhJFj5PfWkuB_h4Z2VRXMATDbdVZLMsUCX-fGlqvQwitphWdLBmyVKDU8_lLv8pkl_xmdgZpR0eizXa2PVa9lsNS5Ls2-1Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aerial یه رادیوی متن‌باز و رایگان برای اندروید هست، که باهاش می‌تونین بدون نیاز به ثبت‌نام یا استفاده از فیلترشکن، به ایستگاه‌های رادیویی مختلف گوش کنین.
👉
github.com/shapeshed/aerial/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/ircfspace/2537" target="_blank">📅 20:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2536">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DAt_qg8h9b5Xq3OB3O5bfWpSJUMxTetD0_dPAL0Teww_wxfejViXVfGmWqqqJHlKvfk3RcMPDGmN1QmMrWt3Bscy5kAedB80DYA3AH-VMVMhSrnNd2QkqC1fk2lVixprAxL05f0iVNnCP_lKgKhPQwvfZpkC2zCPaNP-_obaQjdc28j63AcQX4m8bz7eirh-mcMN2Ex4ObfQagK2LzgUuHwInKIXADYD8c2wSyJQDBvqqSKaFJN4rSvyhk-oLuQ1s5YRlPaTfHv1bh6DzerbgdE5gUMW6wKW_4RCtztCaz74djw-og-q0ybCN_HpHihWbjmjZfsEaQQRqZM8ZXRduA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری برنامه مثل GlassWire، NetWorx، TrafficMonitor، DU Meter، DataMan و ... برای اندروید، آیفون، ویندوز، لینوکس و مک هست که باهاشون می‌تونین مصرف اینترنت خودتون رو بصورت روزانه، هفتگی و ماهانه مانیتور کنین.
چرا میگم؟ چون صرفاً مصرف اینترنت شما اون چیزی نیست که خودتون دانلود می‌کنین و ممکنه خیلی از برنامه‌ها در پس‌زمینه مشغول رد و بدل کردن دیتا باشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/ircfspace/2536" target="_blank">📅 20:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2535">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MLNdGJTmNXM4ONdGWvooqljwEu_-yperBrfNjFO3gj4EIXW5d5eFgYSJL8ezSRaDhmTteyD-W7i_3XC2usS8C_iAqueLTl8l_YEZCdWPjdcU4ZjICKUHvTJqk8WLBzrnTLCwW1lTyqZOnNch5g98s1vWpawVI0SMDBZesU81FZvDfaeCS81p9fHhAL6j2UpyhrOkK6r7WJ_zQsUgvnjqMMrNGxl6i-drXzuXeM5oA3XlmBV7IehnXw8u1-Z1dIq_oRxYOJp7GRhv7cxrlq0ExLY0Jn_xJXMkwjYZwjcIIuwt5wIfXv2r4Bd4ljCR_cd3oZrJiZXOMdelZ0tZNi5CqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از راه‌ها مخفی‌کردن صورت مسئله، اینه که چندهفته پیام خطا نمایش بدی!
©
AmirMahdi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/ircfspace/2535" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2534">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CIBVY3YEbZND-ScZjuUfjFPIYgx0Iyr54Ix5lOLEc8DSDI24_-c2b_vPToJzoHJgm16qiDUaSG4tqFq6o1XGpKlcY3lVhPnXFZDyTc0l8-OJTuYMzReZ8loNgW0qyKb5_DziDQ8Jbt-1T8vWX0Oz35LhDKvyc9QkP_AAsOGJ6Q1VZgMqb1nmGfUk22hGbgFa2lxJ50BZvNHKZ4wymNNTWSO5KmzpOPfg8gxKhxYugcOhUN-MnPL1SddSe_pgARYS33_7lf-txfDWyl8Ar-rFrChV0_3r-lZNDKKQ62WLHTO9prYMCNfFRKSbvyXwAFkjCCxl0WMkQaV_Q4EvV8ym6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه این تصویر وضعیت رو برای بسته ۹۶۰۰ گیگابایت شفاف‌تر میکنه. در توضیحش نوشتن برای این بسته ضریب ۲ واسه اینترنت بین‌الملل لحاظ شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2534" target="_blank">📅 20:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2533">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EMf6Oz8_9xkMyHjYpMNe74iTYUlKskSOcaI47IGgkmHu4LIh2OWEG4uzMVayhQ_EzLM6LDDRtmyYej8LCOUTjQX9lGpdBzHRSBczUjlfs-vjMjPY3-GGHZ9jZGuf9djzzo2vMA_T-ij8PRf2ldo_Bdf9s6Bs5yKzty2_uD9zl25sO_qAsexyYnwqHQqvlUiq9A1OTLgDZ02cLxhttQx5f2fR8Dn6y693_HcyoOE2h4ZyBmS9JcFZkw6P7VjCoAzd05CH0-50AVXfKIKdDWzomMDhcGnU3kSj73csFDA2PtNHtvjKlj_2banxtrAcujx24laXeqvmtxcBSuB-jlbUpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهت کنجکاوی در مورد موضوع ضریب جدید روی اینترنت بین‌الملل، ۱ گیگ دانلود کردم و توی پنل دیدم ۲ گیگ محاسبه شده!
©
Farshad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/ircfspace/2533" target="_blank">📅 19:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2532">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ضریب اعمالی به اینصورته که شما اگر ۲۷۰ گیگ اینترنت داخلی دانلود کنید، ۱۰۰ گیگ حجم از بسته بین المللتون کم میشه.
این کار کلاهبرداری خواهد بود، اگر حداقل یکی از حالت‌های زیر اتفاق بیفته:
۱. اپراتور موقع فروش به شما حجم ترافیک داخلی رو نمایش بده.
۲. این اتفاق برعکس بیفته، یعنی شما وقتی ۳۷ گیگ دانلود کنی، از حجمت ۱۰۰ گیگ کم بشه.
ولی هیچ کدوم از این دوتا اتفاق نمی‌افته.
متن دقیقش اینه: هر گیگابایت ترافیک بین‌الملل معادل ۲.۷ گیگابایت، ترافیک داخلی است. به عنوان مثال سرویس دارای ۱۰۰ گیگابایت ترافیک بین‌الملل، معادل ۲۷۰ گیگابایت ترافیک داخلی است.
مساله اصلی اینه که
این تصویر
و وایرال شدن این قضیه، شاید بیشتر بخاطر ویو گرفتن بوده نه انتقاد یا اعتراض. ما میدونیم که انتقاد اصلی، انتقاد به گران‌تر شدن و بی کیفیت‌تر شدن اینترنته؛ و همیشه هم این اعتراض رو داریم و در موردش بحث کردیم. اما انتشار این خبر که مبنای درستی نداره، صرفا قدرت تکذیب اپراتورها رو در مورد مسائل مهمتر بیشتر میکنه.
باید اضافه کنم این ضریب ۲.۷ اینترنت داخل،
در آینده میتونه بهونه‌ای باشه تا بی‌کیفیتی سرویس رو توجیه کنن! ا
ما فعلا در قالب یک هدیه، کادو پیچ شده و به ما تحویل دادنش.
©
Taha
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/ircfspace/2532" target="_blank">📅 19:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2531">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی ۱ به ۲.۷ هست؛ یعنی اگر ۱ گیگ خریداری کرده باشین می‌تونین برای استفاده از سایت‌های داخلی به میزان ۲.۷ گیگ مصرف کنین.
اما چیزی که کاربران میگن دقیقا برعکس همینه و جالبه!
چند نمونه از پیام‌ها:
- اپراتورها درحال شعبده‌بازی هستن
- ایرانسل و همراه اول ضریب دارن، اما هنوز از رایتل ندیدم
- من مصرفم در یکماه طبق آماری که خودم دارم حدود ۵۰ گیگ بود، ولی ۲۵۰ گیگ رفت توی پاچه‌م
- بسته‌های اینترنت با سرعت چند برابر تموم میشن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2531" target="_blank">📅 19:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2530">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">پیام‌های زیادی در این چندروز داشتم که میگفتن اپراتورها ضریب جدیدی لحاظ کردن و مصرف اینترنت بین‌الملل رو چندبرابر محاسبه می‌کنن.
یکی از پیام‌ها اینه که "امروز با پشتیبانی آسیاتک تماس گرفته بودم بابت اینکه یک فایل ۵۰ گیگابایتی دانلود کردم و اونا بیشتر از ۱۰۰ گیگ از حجم اصلی من کم کردن. پشتیبانی بهم گفت که اینترنت بین‌الملل با ضریب حساب میشه و همه اپراتورها این مصوبه براشون اومده".
توی خبرهای رسمی چنین چیزی ندیدم، ولی اگر اطلاعات دقیقی دارین می‌تونین برام بفرستین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/ircfspace/2530" target="_blank">📅 19:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2529">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YuQCb_tPMoJC49hKEqQCKCgjI4yz1rHmptBCe8iSPcwaI7a3bnrAuogTl_7RQiVUTZKT1g2feMs_mAMqDdkj_BBXDLLDv5h9vhjZ2FO1qGI1bxd427bcsRnE7VbtePdmqRtfiPZH17NVGoW_ZeSAvq3WkeAwJBoF5ZQypCRJlYEZ6BMOd3FFNDL83FZIeWVQAtw3Li_2LAjzNrG07kSePztiBzfTs8Bpc8gIMm5x3ogaaR54bCByUu-vv2rmRGGugCrclejLl_Vfxny9oKSF16qky_uq5HZAIAaZvOtZRq5gY9M8hfZt3E986u570bAIrcG52vjq0SYZxgPUa6Rcdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچ‌کس این چنین به ستیز با مردم برنخاسته بود ...
©
sadroddinfallah
بروزرسانی: تعدادی از کاربران میگن متن داخل تصویر گمراه‌کننده هست، که درست هم میگن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/ircfspace/2529" target="_blank">📅 19:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tkDCo2GZXQre-y3BTNy9Uz7d2ztjrdDq7fOaBw5C1CXny9KVVH-w3mHKEDjr7jt8MN6kmjlNfm9o1eQ1JitSQ_FVBCPfG7RFpxDfcHppFvk1Wld1aBjnSFiIDoYoLBMBFNRZCXEWwXbGUY-myQHI0qGwmk-m4xKQXz3QGt8hfJl1i1sOyVdxHFpAhF3Utn0uhvooTjstNYYBxXn287EzcdMQewspX0FwaombKgvO1kafxGorNiVa54_OWXaWQf-X3OCqPEmJglM669YMVKesLR7smcN9lSBv09cFUaxyZLiVbBCCM0Tr5hMPdRUlTT74zkm9NL7Bn6T1XtBUitcYHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هسته Aether یه آپدیت جدید داده، که امکان پشتیبانی از Zero Trust و تعریف قوانین مسیریابی، مهمترین تغییراتش هستن.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/ircfspace/2528" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2527">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hoAJ_SktpSiBRZIJQuVc_eO1THvJV0vx0ULX_xE3Jc5X8ewq9YitGsiAWqqRCT5E_uQG4AVr6q4Z4q7cqrVKnDGhgAeGJiFoUKbC6mjOD8oJRwUc0eQDQ4cUeFD--B54W3YoDslIDLCsu068zv3y7dXluHeJoS-cHHATUT7pEKwllVWZE_wnf8MPJioEON9RVjYTtEitQfLe9QykwMyOLU32IPA_9lT6HfbF7xCsO2EVETPrf3S0KKkfuAdKa7vYRceK7WlBc06y5NqPpGZ1RUImE-eYchaI5Hmu8NNQ_MndJ3_aOkXUDCoMQqZR6i2gp2Sm6105Zx4TDe5obL56kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از فیلترشکن بگذر برای اندروید در گوگل‌پلی قرار گرفت. همینطور می‌تونین نسخه ویندوز اون رو از صفحه گیت‌هاب و نسخه آیفون رو از تست‌فلایت دریافت کنین.
در این‌آپدیت هسته ایکس‌ری به جدیدترین نسخه بروزرسانی شده و روی افزایش پایداری اتصال، بهبود عملکرد کلی و افزایش سرعت برنامه کار کردن.
👉
play.google.com/store/apps/details?id=cloud.begzar.begzar
💡
github.com/Begzar/BegzarApp/releases
💡
testflight.apple.com/join/cRSCr51a
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/ircfspace/2527" target="_blank">📅 18:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2526">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته توسعه زیرساخت‌های ارتباطی کشور حتی در شرایط جنگ تحمیلی سوم متوقف نشد!
انگار نه انگار ۸۸ روز اینترنت کل کشور رو بصورت سراسری قطع کرده بودن و بعد از مثلا وصل شدنش، اختلال‌ها در ملانت ادامه داره ...
برای راهپیمایی اربعین هم در ۱۰۰ نقطه اینترنت رایگان درنظر گرفتن و پولشم که با افزایش ضریب و هزینه‌ها، از جیب مردم پرداخت میشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/ircfspace/2526" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2525">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nudl5BuVm6nCHiKLajblYe63dpcUy1yL2VSQA9QQmhbZpQq0htlGTCKMvsf8n0A7SlOGIHIbvYGaqU18VX-tLcrETnvk3PiKtNmbNKba9Gw3gf1i_a4_Z9_-9vJsIBj6B-ENfpqWl2-vNTqwnU-0AnU0tafE36ykxB-m8pQYr87CyH36-SayYh8lr_3Lni3mPBjHzkAdAuWoeKds-qV-GGb_c9Gd1ne6CiioayHQoBeYCA2pQ8KxOCg3HAUbtF0YVGRVxUXUr7T04xtx11jpMvZUvMOQh8z-4AYHg1yq66XNn4lR7kEVbi-7VoXnqpQBd5eymHh9Zqf5eYSsCcmlwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردش مالی ماهانه بازار فیلترشکن‌ها ۱۵ هزار میلیارد تومان است؛ بیانگر حجم عظیمی از سرمایه که به جای ورود به چرخه تولید، نوآوری و اشتغال، صرف حذف یک محدودیت می‌شود.
با چنین ظرفیتی می‌توان ماهانه برای حدود ۳۵۰ هزار نفر، حقوقی معادل ۴۰ میلیون تومان پرداخت کرد؛ اما این سرمایه، به جای آنکه به موتور رشد اقتصادی تبدیل شود، در بازاری گردش می‌کند که هیچ ارزش افزوده پایداری برای اقتصاد ملی تولید نمی‌کند. /هموطن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/ircfspace/2525" target="_blank">📅 18:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2524">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gsjGvMIVEk9kU5gWGLPii3l4e2CEbLOgQE9HinW0E-lTU8H20EbpX0cDo4UYwDu0-pirScleyMAfmoX8J1eVPomkx4Jo9cXy3124gjNfXGSTrlabsPaPYtQ_euR75OD-lV3LwcwiO_MNsTmv7PaMiarzxwyJdeXOqcUMV_cSgFmVCyamaRjkRpYyujNszdejiq3Lib59tlCcOOE3w2kkN7quD4OwPvzZEmZeu7tZ9rHq8Xiy8jPf1YiGkZyR4z7wPBED2Vna3AnMpI9Hq9JauBFw8oiYpPER7JyhKN0wOpdq6sEK-lOgwCFvf2MtWO2Av_w8mHhTxBqS2UjCCrYhoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز کسی مسدود شدن سایت فوتبال ۳۶۰ رو گردن نگرفته، اما سخنگوی دولت گفته "هرگونه انسداد، تعلیق، تحدید، ممنوعیت فعالیت سکوها و کسب‌وکارهای دیجیتالی پس از اخذ نظر ستاد راهبری و ساماندهی فضای مجازی و دستور رئیس جمهور شدنی است" و "این موضوع یکی از دستاوردهای رئیس‌جمهور است"!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/ircfspace/2524" target="_blank">📅 18:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2523">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cY-T9NqL1a7c_ylICnKJEtNuErA1tcx1ArufO-TF-wWo5rTZ6qmhuNIY47oTJUyaNv1mrFWTZjHO7vKOdpCzQuI6JU9dYnt8dHBTXiacmaP_wtMx8BaJx_M8Tmd6zI9lpwXVJxrg0h_uj_meinIJOLKo9G5vU7QcSeohdWyLNeQ_OjJxmPqtOi5-dG46mv4ZJ3FWVxvK7TSRVkaR8IOVOVVZXuYZXP7-nT4_4mcmETIaE_XUxX67AHfx-DQBuyiddEBr35d7pAPSsBfN5Iwy1VhLd2dVVWSXlXm7yIABHbsfgK8dV7guXiqoV-_fLIjT90rjTj4p1eKsxaiHDXMxRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ AetherST Tunnel یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که با ترکیب هسته Aether و SOCKS5 مبتنی بر HEV، امکان اتصال از طریق پروتکل‌های MASQUE، WireGuard و Gool رو فراهم میکنه.
👉
github.com/immaghzbad/AetherST/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2523" target="_blank">📅 18:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2522">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jOA1rsvWlhsFvAzviWl_2qJYqotJMzL67EGXQCtdBzkrOboYtT21tm1-tEIJ8jTl3i6Lp7hYDHItm3G4_lcwfobCf1m8Y1AFwx3vpSUd4X96OrXWV0f7uB-Pg-d_sXzTUx7f73OTFtpuFADHjeqdWul97LBvSDFNMPkgiFZb9-U6n2qQhVOc3rPKztmIhWcRTd1F0IRk1YkCBlvYmopkjBuoS8nRYN99JMshkayd-ZgqyZnnhWAM6hvy-51QYESvZ4V2Ldge_ePm6Btr-bl1T40FfgBn58G_zGw7yLr87FqsqZDuKLINNwpz1XaH4cMdvhqcbR_3ssCp-u0wtP2YGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از چندروز آینده بخش جدیدی از قانون هوش مصنوعی اتحادیه اروپا (AI Act) اجرایی می‌شود که شرکت‌ها را ملزم می‌کند در موارد مشخص، استفاده از هوش مصنوعی را به‌صورت شفاف اعلام کنند. بر اساس این مقررات، اگر محتوایی مانند تصویر، ویدئو، صدا یا متن با هوش مصنوعی تولید یا به‌گونه‌ای دستکاری شده باشد که بتواند کاربران را درباره واقعی بودن آن گمراه کند، باید برچسب مناسب داشته باشد.
همچنین چت‌بات‌ها باید به کاربران اطلاع دهند که در حال تعامل با یک سیستم هوش مصنوعی هستند و محتوای تولیدشده نیز باید دارای نشانه‌های فنی قابل تشخیص برای سامانه‌های دیگر باشد. البته استفاده‌های ساده مانند اصلاح املایی یا ویرایش‌های جزئی معمولاً مشمول این الزام نیستند.
در صورت نقض این الزامات شفافیت، شرکت‌ها ممکن است با جریمه‌ای تا ۱۵ میلیون یورو یا ۳ درصد از گردش مالی سالانه جهانی مواجه شوند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/ircfspace/2522" target="_blank">📅 18:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2521">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uIxF8wZcGJydok7fxaDESgI2auRG5F8WWvYOPhILKZm-RqYN3OA7b6RTWtNRCyz2JE_DVNk1BnJ76FtLtMJ7-8HVB1txP7y7573GeriIsX8QrUH0305eDuW-OPct2KzTioFnsmrKNPAOFWr1onHxt5Ea9rhDL8fOfZuGNvtJnRArf4HX8qlShHJbPSYDo-3pm0bqt_l6LiGqReaJVIAbCzkfOpr-vydWCrIl8mZZ5AdcGWchJ1V_74TkfBTKq-PaDQxL-0k2JOjsIq9S-myqss4uWQRvkbZt_Z6EFHz4HpcjOVoF0gwS3Jur5vyle-KFSen9lWwXtv2yCOvZk6mb5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسپرسکی از فعالیت تازه گروه هکری تحت حمایت حکومت ایران به نام Nimbus Manticore خبر داده، که با نام‌های Mirage Kitten، Smoke Sandstorm و UNC1549 نیز شناخته می‌شود.
این گروه در حملات جدید خود از یک Backdoor ناشناخته ویندوزی به نام NightLedger و دو ابزار Tunnel با نام‌های BridgeHead و ArcBridge استفاده کرده، که قادر است اطلاعات‌ سیستم و شبکه را جمع‌آوری کند، فرمان اجرا کند، فایل‌ها را سرقت یا حذف کند، Processها را شناسایی کرده و از صفحه‌نمایش Screenshot بگیرد.
بخش نگران‌کننده‌تر، ابزارهای BridgeHead و ArcBridge هستند؛ این بدافزارها سیستم آلوده را به یک Relay مخفی تبدیل می‌کنند تا مهاجم بتواند ترافیک خود را از داخل شبکه قربانی عبور دهد و به سایر سامانه‌های داخلی دسترسی پیدا کند.
روش نفوذ اولیه هنوز مشخص نشده، اما این گروه سابقه استفاده از پیشنهادهای شغلی جعلی و صفحات تقلبی استخدام و ویدئوکنفرانس را دارد.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/ircfspace/2521" target="_blank">📅 18:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2520">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">فیلترشکن
#دیفیکس
در نسخه ۵.۸، هسته وی‌وارپ رو بروزرسانی کرده و میتونه به دورزدن فیلترینگ از طریق متد مسک روی بعضی از اپراتورها مثل همراه‌اول و مخابرات کمک کنه. همینطور مشکلی که باعث میشد فرایند اتصال در همون ثانیه‌های اول با شکست مواجه بشه، در این‌آپدیت برطرف شده.
👉
defyxvpn.com/download
💡
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/ircfspace/2520" target="_blank">📅 07:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2519">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f0jC0bBNWyMx9HvmWFiuCdJUBXSLHOGKWjiA4vynK1LgvUlX70fJvoqIFovUH2l_47M_D677qEVHx5ruwutzi6gMexE_NbvWqbW4NSg2gjj87IY0b8Keok3R9M-OzztPeTFFObCcw-espgX7e5YjRc1qQVnpzUXMn8J1WnlPYL2CTaVbhm5knxnJeqfZNCG-lh9dYXzeU4PqxX5YJw7mkcTLARMqMjVWOnsbNkHR1-cUd6AR0UDevJDP3TjGvaT0E0LkJ6Hn7UosZX_cmKIcaAHVzB9YuqEs6_JSs8uMkRJkrJ_UFMFYpL-KGpvPrwf3rlBswKPSNoCEbW39oNcIGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ
#Aether
یک فیلترشکن متن‌باز و رایگان بر پایه هسته Aether هست، که برای اندروید (AetherMobile) و ویندوز (AetherDesktop) ارائه شده و از پروتکل‌های مسک، وایرگارد و گول و حالت‌های اسکن مختلف پشتیبانی می‌کنه.
اتصال مجدد خودکار، انتخاب و تغییر خودکار پروتکل درصورت شکست اتصال، برخورداری از حالت نویز، امکان تنظیم MTU و Keepalive و همینطور Split Tunneling، بخشی از امکانات این برنامه هستن.
👉
github.com/QW-AI-Code/Aether/releases
👉
github.com/QW-AI-Code/Aether_Desktop/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2519" target="_blank">📅 07:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2518">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SKfP_UsgONICoj26SUbQ-3LfJieJR4Oqk4yFl9H5Tyk5SwFjwlMm1CMPP_DupgYrqvr8P5IhV7X6p0QCjER9yblyutRU8nQAOtzwTfcf1aEEqn2XWd48RCi-eMC5Q0YJpMV55L2xKDniWHw0Toueq6lFojompctrL_wTNyx7QygEG7RVKQcfBh1SsW2T-qJTlHmhp1S1os6pIl_LczqcjtJNHV5Viq_nR8uhD6NcoioRmC5Oqya5M4NvvM7TFycQ-RNz22xDSO7fGv2aB20AttiSf4ksb19pLrsjOPDbuKDK7djNDsA6huCjggdwfbVtz1IplrYUDUuikhB0EbGv7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تازه‌ترین نمودار ترافیک اینترنت ایران بعد از ۲ دوره قطع اینترنت، نشون میده ترافیک هنوز به حالت قبل برنگشته.
الان دیدم یه نفر یادآوری کرده "۴۰+ هزار نفر دیگه نیستن که به اینترنت وصل بشن"!
#دی_ماه_خونین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2518" target="_blank">📅 18:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2517">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DcgqgaPROkl92xvVdH-1K63VQBKpSYY08wdwIRHSWcqjcdHN2Uau8n2XMbhumGx9dvyhftMgKi3k5mEC_tBCulygJLl1uytShRpIt-Fjx_jyC_cf8xekhxix1twN43SRRPyAs2ZiMRq3dI36ADOTANUIDH2maEaz3EJi7J7kOOVVHDpf7xssOLYHoRomRHe7i_sjojnUB3KMXvKf1Z_1BKlxPwhYekYr6IoqRHA_d603BIZ_wjF7Xhk6vs9bf8a5evmDk9oic04gguv8NHUKQi2LKIhUTtjN9ZJ0x_FlAy3NkjH5rTEe2G0dhBYj7PvKIACsCDaGCEQM7AWW3tP2Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته "سایت‌های ارتباطی در خاموشی‌های بیشتر از ۲ ساعت قطع میشن و راهی برای تامین انرژیشون نداریم".
یعنی از هر زاویه به این مرد و عملکرد درخشانش نگاه می‌کنیم، حل مشکلات و امیدواری به آینده فوران میزنه!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/ircfspace/2517" target="_blank">📅 18:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2516">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UYOLvRsIVrNIskXVKWrXhJHZmggPEut9Jkckgy168abkdO7_0ZdAQwiOtwFldce2FIGEpwRBo9wPmXhmXQM3tXTkZEelVCuCLo1PFBRxjX4y162RjfN6PtSqjNAkGy3pvB07sp7Ly-R-8wku7yeVkf0pT5v3faKZUlZokPW7NIwALEX4bSb705zQaFTQ6qDyEEwxcc0BZxWqbAp9vTxRanQn6tfrbApB-vuWW2ZGZ613A3lC2Le1F17q5przbgkgyJpQjXcirwOp94RSrWLv8bBKGn4KAB682x_siomz4wm4jTyplHGGt3-Z40VK63J70P8Qf8UnG5WRQ20wtTr7bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی هسته ایکس‌ری از نسخه ۲۶.۱.۲۳ به بعد یه سری هشدار برای قابلیت‌های منسوخ‌شده اضافه شده، که شامل allowInsecure و Shadowsocks، VMess، Trojan و VLESS بدون Flow میشن. مثلاً برای Shadowsocks این پیام در لاگ نمایش داده میشه:
"The feature Shadowsocks (with no Forward Secrecy, etc.) is deprecated, not recommended for using and might be removed. Please migrate to VLESS Encryption as soon as possible".
اگر در حال ساخت یا انتشار کانفیگ‌های مبتنی بر Xray هستین، بهتره به جایگزین‌های پیشنهادی مثل VLESS Encryption مهاجرت کنین، تا بعداً با حذفش به مشکل نخورین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/ircfspace/2516" target="_blank">📅 18:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2515">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q7djs7Q5siDRl0RPLd9J0T0OqB7mliW2jOien2GVVguZ1NZm_QC3P85zSahNlil41Anw1TuNdg0AApmOIMId3gyRvBqkYnPY2CtwGMp1HTHWsqSj70AwbcIcJwuo9vK4dkfuQf0QWqOzRltKhuh2M3F_-FHGsZZx9iInjnIRAlXQ3MkebNY5F7LboMR2xtske6NhuLx677fZkLrDVqPpsTuQcmXjm-bB7883r2X24RHZm9bsKP-J2Ez1gLtvi8okAsCCdX6dOeuuQ_PIaOmLuiulmt57ATUDpJeZ9Kfz6YCC6ssCzRpp8LLO2AN_JpwmIruBFtN0m1IQ3b3Z9QfWHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت دسکتاپ v2rayN یک بروزرسانی امنیتی اضطراری منتشر کرده و از همه کاربرا خواسته هرچه سریع‌تر برنامه رو بروزرسانی کنن. این هشدار در چند ریلیز اخیر هم تکرار شده و توسعه‌دهندگان تأکید کردن که نسخه‌های قدیمی حتماً به آخرین نسخه ارتقا پیدا کنن.
در توضیحات این بروزرسانی اومده که "یک آسیب‌پذیری امنیتی بحرانی در دانلودر داخلی نسخه‌های قدیمی برطرف شده، که می‌تونست به مهاجم اجازه بده فایل دانلودی رو در مسیر انتقال دستکاری کرده و به جای فایل اصلی، فایل مخرب رو بهشون تحویل بده".
👉
github.com/2dust/v2rayN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/ircfspace/2515" target="_blank">📅 17:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2514">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z9j3upRPemNu8EuAzNdpjC1MPr9njRlI17VlbohX-90nwQ2icxGFny0vwYa_jD8uTe0oy7fp0N0-FfhkUkccBBxA2gulARg0w-dowWY9so0EyXuZAU33gTgvbPmeFz43xvlyE-kRoBRIti9gP9SWpsQwa9ayDCA3C7ai8fxi69MWIyDwgps8RNknKKpwbu9NOx2_OrfZwbh-ZW3S1mvNwlJkMNUp9zKaIU8RkdFhApAYuF6SE30cWmNilOjczXzcx9eSSjJ-GTnJiUCrRM-kuJqF-Zv0gMV8jKdhobxozzEyXfe8TUEFxQr4Rd4CpnVmrgIzMYvhsZEBqKsV-0iE9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع اینترنت در راهه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/ircfspace/2514" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2513">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YovBGISHjdhH9J706FrYMsvUMsVY-ObWdHzsCh0CnsLCqInftNcnL-Iyga410drdL9XKTSti2rtxlLUsrAuKKXDxLDoYj2D9Za_34UahRUjpXsBpw594zBtizX8RP_j0MCaFGADKkhrePE66M29DSX8Y5ea-13ei58H67UlYoP87oLHJRXAEwv6g5R5RJsDAAIzm7wtixqbVrMtePXh2AFFQA2r4epNE0tZkIdlHs7gEZg05Evlu-hZC1Ib7Bph5toUZ3klpAT0Lsws4bVKWCBgq5Ak2PVZolohgtNvBt16h2jki1vNAMULbJgcfNY6L2OsaMvA-IDT2IMxuaF8QsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبلیغات تلگرام ابزاری شده تا بعضیا مرزهای بی‌شعوری رو جابجا کنن.
هیچکدوم از تبلیغاتی که توی کانال نمایش داده میشن توسط من ارسال نمیشن، به هیچ‌وجه مورد تایید نیستن و اگر سرتون کلاه رفت یا امنیت و حریم خصوصیتون به خطر افتاد، مسئولیتش پای خودتونه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/ircfspace/2513" target="_blank">📅 19:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2512">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y1O_UUhuZPCJVAxLP9m_4CmBkS3sqOR-iDNXQ3WnNw0JdNVG9hmxzPRGq4tYbQFkdv3IkoHFZGpAVxK5_QDZ7I58kOblVbY0U1sps5WITY_zTS2E6paFZJN6d5t9VPvFG6uz016xnKnVxmr6JaCyWHyeSGwn6YZhirBME3vf0_t1UkR-Nr25Cf_bwB1HbB3UecWZVvIKK0ktrrhmBbU02hktkTZNqe-zyI0YPMEZwb4icQvshJXcUk7qzzxMnrJZXhxQDNfSgbrsx7N7e16P8u-PXccWC8uWK3Gpt3PYO_7hehwnoW9fIpY-Xo3Gb9_AzC3xevsphEu7xt5kFo5I0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن تجارت الکترونیک ایران یه بیانیه داده و نسبت به تعلیق دامنه فوتبال ۳۶۰ در رجیستری ‎.ir اعتراض کرده.
اصل بیانیه قابل دفاعه، اما امیدوارم برای کسب‌وکارهای کوچکتر، استارتاپ‌های کمتر شناخته‌شده یا پروژه‌هایی که بدون پشتوانه رسانه‌ای قوی دچار مسدودی دامنه یا محدودیت میشن هم کوپن بسوزونن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/ircfspace/2512" target="_blank">📅 19:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2511">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ساترا گفته نقشی در فیلتر شدن فوتبال ۳۶۰ نداشته و قوه قضاییه اعلام کرد مسدود شدن این سایت ارتباطی باهاشون نداره.
وزارت قطع‌ارتباطات هم طبق معمول نقشش فراتر از هویج و سیب‌زمینی نبوده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/ircfspace/2511" target="_blank">📅 18:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2510">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tL3HJ4v2Nhr41wepg5v9KXW62MfU-2lUN3xnKGC8MggX5sLaBky8J_QUZdSGgXamfKnQAWjQk7JZMkf7JkknYsye3UhRDd3EnuJ8Mwrfc0WJBWMn8ht7zbxJJ-kDsrvzEna1sg-qSpbKTMmpBT-uIJCREIN7LTMB8cgPEwwIDx1BoAKoSLDz1FrZtI0el-IOTvDn1afIVIUcOgc68W24vHPneOnw_VEJS9ifdEJeTKB049sZCQWK61JGtDcHbCmgNu0ivursegFSXXTHzT86OpeUACVo46XkXCOcC6ixjZhVHZm-WNrTKv7kobJaZ2UFkHF9OVmx8uVnE2lEKEcCCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ ShineNET VPN یک فیلترشکن رایگان و متن‌باز برای اندروید هست، که از امکان انتخاب هوشمند سرور بر پایه هسته‌های Xray و Aether برای دورزدن محدودیت‌ها استفاده می‌کنه.
👉
github.com/shayanheidari01/ShineNETVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/ircfspace/2510" target="_blank">📅 18:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2509">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZuJfZQrg-s8xacDocVR7hT-hD63oTZ2qMaBQEvakcp91ddadEsGHVld-RfK3RdgONlRg5Yov0DaTptY2m3u7DEyCUZLdx148IBEHd60EnnjFMAmCEzWF8hX4dV_Yq4EWvRXAPGL5IWiAb0QZqoO-q85ElQImwN8CgGmZ8EOCO2t8aYfn4oYoK5U6jdA_sBo6yc8IBukTKKGFyzfZ5TecaEIbv14Y4t458lNbeMbdw-wcx8j64DnKr7aSuYulMRx2iCf2578f6uJVF295wGpTpOX9L9cOWHb8mG5JsbXadDruHcstDViiFeCu8DRa-6iF64gHp7ym3rHETp2F1PQyCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت فوتبال ۳۶۰ عادل فردوسی‌پور توسط قوه عاقله فیلتر و دیشب چند دقیقه قبل از شروع برنامه زنده از دسترس خارج شد.
هنوز علتش بطور رسمی اعلام نشده، اما این اتفاق پس از درخواست سرمربی پرافتخار(!) تیم فوتبال جمهوری اسلامی برای برخورد با این برنامه و یک روز پس از جوابیه به امیر قلعه‌نویی صورت گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/ircfspace/2509" target="_blank">📅 11:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2508">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LQhPjMwAOoZ8c4PabkIQ4guvlormSnSths4lkDHwxn2oqMZqpZrO-Ow3dAS0rwIAwvdrh87ohb4u14zGwchs7smJMCK_GKjrl95MPajVxBQ_X2fgu_bcNwSnIErVSsXNHNidporHzUwgniJk_UICxoEKNzyeMQxOFbgEzMPPwNoi2Ft_rbUxn-Y4APlK6qVlvWG4qOGyM8ikET6N3HgMOxgx2ZyXZeoiu1-9nmcHWFSB20BOBo8ydlaLwREnMt78oMaePcUuteS0ovgkSatGPvVjDoYRBfOv9R9j2qrUPZCWbNUbbC61YRkFPOQZVoqfBTgV_ASGRR5l6eoAz0PKsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن Aethery برای اندروید یکساعت قبل به ورژن جدید از هسته Aether بروزرسانی کرده. اپ Aether-GUI برای ویندوز هم کمی عقب‌تره و ۳ روز قبل بروزرسانی کردنش؛ البته احتمالا بزودی براش آپدیت جدیدی ارائه میدن.
👉
github.com/ZethRise/Aethery/releases
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/ircfspace/2508" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2507">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SMyXvGQKK4XT8jEmKsCT7kPdZoF8zbjVFhNlfVeyP2Xm0MySAGELiZQmsxZJqjvyGV__SWZ8nh6qX_0gzgd7aPsBdpqdUJxlSedkQYPDSKeHKw-PbjV-F5i_4nV9yvVqBPkRL4Qni0diaXzNKC5AYOHYG8yMZyrQ7XQrjtuAlGegUM3CSwsEsaK_DIpl_4mgBRRpDgZjWqsj9AlADx0qf79XEzL1ldzTc5wubPAjOceeUZ3Bo6sciMTkr6IFsr1cNvWsvRvqxxaBmbnAbAsiaiAYYaX5VW3bLtQWbpi4w5Jq0gHugIUsFUzleALN4C0mV-xgG_QMPzNTGffHOU53vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱.۳ از پروژه متن‌باز و رایگان Aether منتشر شده و مهمترین تغییرش اضافه شدن حالت اسکن Ironclad هست. برخلاف حالت‌های قبلی که فقط بررسی می‌کردن یک اندپوینت در دسترسه یا نه، این حالت قبل از اینکه به یه سرور اعتماد کنه، یک تانل واقعی برقرار می‌کنه و یک درخواست HTTP از داخل اون عبور میده تا مطمئن بشه اتصال کار می‌کنه. البته این روش زمان بیشتری می‌بره، اما در عوض احتمال وصل شدن به اندپوینت‌های خراب یا ناپایدار رو تا حد زیادی از بین می‌بره.
توی این آپدیت روند اتصال مجدد هم هوشمندتر شده؛ اگر ارتباط MASQUE یا WireGuard قطع بشه، Aether دیگه برای دور زدن فیلترینگ مستقیم سراغ اسکن کامل همه اندپوینت‌ها نمیره. اول همون اندپوینتی که چند لحظه قبل روی اون متصل بوده رو دوباره امتحان می‌کنه و فقط اگر از دسترس خارج شده باشه، اسکن جدید رو شروع می‌کنه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/ircfspace/2507" target="_blank">📅 16:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2506">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پژوهشگران امنیتی Insikt Group وابسته به Recorded Future از شناسایی یک کارزار جاسوسی جدید خبر داده‌اند که با استفاده از بدافزار MarkiRAT، کاربران ایرانی را هدف قرار می‌دهد. این عملیات به گروهی با شناسه TAG-182 نسبت داده شده و طبق ارزیابی پژوهشگران، ایرانیان داخل کشور، مخالفان جمهوری اسلامی و فعالان مدنی مرتبط با جنبش‌های ضدحکومتی مقیم اروپا و آمریکای شمالی از اهداف اصلی آن هستند.
مهاجمان برای توزیع بدافزار، نسخه‌های آلوده برنامه‌هایی را منتشر کرده‌اند که برای کاربران ایرانی کاربردی یا جذاب به نظر می‌رسند. از جمله آنها می‌توان به فیلترشکن Pis2ray VPN، نسخه‌ای جعلی از Star VPN، برنامه‌های YESHICA، YEPlayer و YEMPlayer و همچنین یک وب‌سایت جعلی با هویت Starlink اشاره کرد.
بدافزار مذکور پس از اجرا می‌تواند اطلاعات سیستم، فایل‌ها و داده‌های مرورگر را جمع‌آوری کند، اسکرین‌شات بگیرد، دستورات مهاجم را اجرا کرده و ارتباط خود را با سرور فرماندهی و کنترل (C2) حفظ کند. پژوهشگران همچنین زیرساخت‌های جدیدی را شناسایی کرده‌اند که نشان می‌دهد این کارزار همچنان فعال است و احتمال ادامه فعالیت آن وجود دارد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/ircfspace/2506" target="_blank">📅 16:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2505">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مدیرعامل شرکت آسیاتک با رد شایعات منتشرشده درباره کاهش ظرفیت دیتاسنترها و احتمال قطع اینترنت، اعلام کرد: تاکنون هیچ‌گونه اعلامی در این زمینه به آسیاتک ارائه نشده و خدمات ارتباطی و دیتاسنتری این شرکت مطابق روال معمول در حال ارائه است. /سیتنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/ircfspace/2505" target="_blank">📅 19:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2504">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گزارش‌های زیادی از کاربران در ۴۸ ساعت اخیر در رابطه با کاهش پهنای باند، اختلال یا کندی اینترنت تلفن همراه در مناطق مختلف کشور وجود داشته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/ircfspace/2504" target="_blank">📅 19:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2503">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/unD3MMj9Wtp_6azNx-0jTAmvbi-pV-yXViJ7w1uS8icr-PjV4enRDNKKvhLQZMe3dDyVf-8zWHq0LqxIl-hjaR5pwoeTbVn-iVPgCKGtnKxGQan2KY_p7pAJ6OPJY3bGmJIjjXV0YeaGvT2rxRXmpkSF-gMDwOjzcTCCFa9aV3YVkfKcPFt7S2xzy0lTquCusiLFeFUVD1GxhjbniAlt6sNNbA32PY2qs5VEsXb8h9Enkqo08wVkX-c0MwBZNiPfC9fFwtZXQSwVpDrGSPVJexi-S84L6Ijh0yz9ld0GlvqXrN-LTfEXLR2I7LOBbu3b9ImKuo7e1iYRrMMFkvq4Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران امنیتی از شناسایی یک زنجیره آسیب‌پذیری جدید با نام wp2shell در هسته وردپرس خبر دادن، که می‌تونه به مهاجمان اجازه بده بدون نیاز به احراز هویت و حتی بدون نصب هیچ افزونه‌ای، کد دلخواهشون رو روی سرور اجرا کنن.
بدلیل شدت این آسیب‌پذیری، جزئیات فنی و کد اکسپلویت فعلاً منتشر نشده تا مدیران سایت‌ها فرصت کافی برای بروزرسانی داشته باشن. این مشکل در نسخه ۷.۰.۲ وردپرس برطرف شده و برای بسیاری از سایت‌ها بصورت خودکار در دسترس قرار گرفته.
©
slcyber
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/ircfspace/2503" target="_blank">📅 18:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2502">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بیش از ۱۱۶ دکل مخابراتی استان هرمزگان در پی حمله آمریکا دچار اختلال جدی شده و خدمات تلفن و اینترنت ثابت و همراه در شمال بندرعباس و بخش‌هایی از استان با قطعی مواجه است. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/ircfspace/2502" target="_blank">📅 18:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2501">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">زهرا مرادی، مدیر اجرایی سامانه پیشگیری از خودکشی طعم گیلاس: در روزهای قطع و اختلال شدید اینترنت، روانه حدود ۷۰۰ فرد بحران‌زده که به کمک فوری نیاز داشتند، امکان برقراری ارتباط با سامانه را از دست دادند. برای تصمیم‌گیران، شاید اینترنت تنها فشردن یک دکمه باشد، اما برای سامانه‌ای مانند ما، این شبکه تنها پل ارتباطی با انسان‌های ناامید است. قطع کردن اینترنت، فاصله میان زندگی و مرگ را کوتاه‌تر می‌کند. وقتی شبکه قطع می‌شود، افراد آسیب‌پذیر دیگر نه تریبونی برای شنیده شدن دارند و نه راهی برای دریافت کمک‌های حیاتی. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/ircfspace/2501" target="_blank">📅 08:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2500">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DNF57-ibtXV5lZD-79veRh05dW_kjdWTKq9zZLOq8BY3JkNO0PKutmXXBnnKGFPWu9S7irKe5abWzsUcqut43WwQWTFcfOTH7D6gG4lMulxMg1HxgC5OzO70aRiKkhqo703dpnSFcyloGDRtDYKun0G2VX8r_-RI7XOf6vXhGd1a-ILsTCjoozVmmlJXRBqPWAAoMBwjM3iDG7qnjsVSj3ZjDSCrnPU7-cy5Zgy9t_pv-GvSpbIimZ0Ep5_QQG9nuIp_PnhQ4PWj6L6CPNPy4g4lJqf-Ib3UnYTGfc1JaJx43iX2VP_fOdZ2rHW8HvxRtZM4qV7YMzrw-h5BvCrr2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگرچه قضیه ترند شدن "لغو عضویت جانفدا" در نتایج گوگل بزرگنمایی شده، اما یه نقل‌قولی هست که میگه "وقتی دیکتاتورها در حال سقوط هستند، فقط دو گروه کنارشان می‌مانند: هم‌پیمانانشان و احمق‌ها".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/ircfspace/2500" target="_blank">📅 07:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2499">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FAXZXfkQulybvLX2-bU0jzfZ8Hyu7vg_WoDh7XAWvMN5gt3a8iD_1m3XspTsGXLToQzUF704mDX4lpwnE5qU-pwMTHooTBzxTf-N7Tqewf-iUFEMFrEK2ZWijIWvNSd2vmrmEIgdjGUb8YTJp1chfOmbN53L9IqHxv3pWBd5hOwDKOzxsZ4KYVLvhIyK8xAYad7KvWPvRuc5piQUVu4oTW_zvlDZQtasuQYYfIm9sK0kx1KfMvzIboaT6I37eAJVs6vThw3-rG5uHk9O8DB0NSlYjQEqtysWjvT0XSLst5WksFoUmFLFZCQ-bdXT5cWrsaJynNXXcuBx10XOPfWxKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ dicodePing یه کلاینت متن‌باز و رایگان برای اندروید و ویندوزه، که مدیریت و اتصال به کانفیگ‌های مبتنی بر ایکس‌ری رو راحت‌تر می‌کنه. این برنامه از مدیریت سابسکریپشن‌ها پشتیبانی می‌کنه، می‌تونه بصورت خودکار بهترین سرور رو بر اساس latency، jitter و سلامت اتصال انتخاب کنه، از حالت TUN/VPN پشتیبانی می‌کنه، آمار لحظه‌ای اتصال رو نمایش میده و امکان تعریف دامنه‌ها و برنامه‌های خارج از تانل رو هم در اختیارتون قرار میده.
👉
github.com/mcodersir/dicodePing/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2499" target="_blank">📅 07:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2498">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پژوهشگران دانشگاه میشیگان، دانشگاه نیومکزیکو و مؤسسه فناوری دهلی، ۲۸۱ وی‌پی‌ان رایگان اندرویدی با بیش از ۲.۴ میلیارد نصب رو بررسی کردن و به این نتیجه رسیدن که بخش زیادی از این برنامه‌ها برخلاف ادعاهاشون، امنیت و حریم خصوصی کاربران رو به‌خوبی حفظ نمی‌کنن. توی این بررسی مشخص شد ۶۱ اپلیکیشن بخشی از اطلاعات رو بدون رمزنگاری ارسال می‌کنن، ۲۹ مورد دچار نشت ترافیک یا DNS هستن و بیش از ۸۰ درصدشون هم با سرویس‌های تبلیغاتی و رهگیری در ارتباطن. علاوه بر این، خیلی از اونها هنوز از تنظیمات امنیتی ضعیف یا روش‌های رمزنگاری قدیمی استفاده می‌کنن.
اما نگران‌کننده‌ترین بخش گزارش مربوط به ۵ وی‌پی‌ان بود که فایل تنظیمات اتصال رو از طریق HTTP و بدون رمزنگاری دریافت می‌کردن. این ضعف میتونه به مهاجمی که روی یک شبکه عمومی مثل Wi-Fi رایگان حضور داره اجازه بده تا اتصال VPN رو به سرور خودش هدایت کنه و تمام ترافیک کاربر رو بدون اینکه متوجه بشه زیر نظر بگیره. به گفته پژوهشگران، ۲ مورد از این برنامه‌ها این مشکل رو برطرف کردن، اما BambooVPN، Free VPN و 101 VPN همچنان در برابر این حمله آسیب‌پذیرن.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/ircfspace/2498" target="_blank">📅 17:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2497">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MO0XiBamsRE7hv-5hGGIrO5XoIJHuEuTDge9AWI95ZBIW-hbp0HXgmzKhiqPhGaNOW8ETvDZ9UoqPdT0R-02O-xYqMpc2ecCnbLFnF3Bl8EBuJ07UsQTmB7BvdMXXfmJL6nsjFKVHuZKHMj5ARZlLtpBgDpccjEs-aBivcSJxY8kBntYRwUir89ZPOH1-sQufr32exBKLt62-MyJ7AhfNY0qyOsCHx41OjIsnv_lYb_i9SaJ_GUa9hfGnH7xyl1f4lJQ4m6ZAS_lUJj-H71PXP7BWfoF3IRio-rtS8eoMylKMcwbc5aG6n4u3F8OI5bfyXIf2LtiymHZQRUnuxEk6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aethery یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که بر پایه هسته Aether ارائه شده.
👉
github.com/ZethRise/Aethery/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/ircfspace/2497" target="_blank">📅 16:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2496">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M_C6ujsfq1NgPzbF4suJSOKMl1CrcrNYAuCZNINOB7Zo202S-PhKF7NpTOEwkvdOVRM8qNkd7HwUnZxOCyapo9NyGPJdMTGR6RH7y5rxklq-WA2wbq2hfDV6A2N_U_ibbYZmgQ7aE6L1z01X_OD8KWZdem9ojf1d8Yq7EysECCq_V5lV4nIPyb6Q149Qs3-LjDJ8jIZ2faPUlLvyYzs3Od5TeEVsV_gi8rTl8ja8cWZhrg_N3nVFJF9iCZKhzKBKnRb04RfFbD6QB2VeIxa_pBo_a6sOeCVWE3uUELV1p33p8fVsQiopp7wMMI9-bc9CMtPmT4TEECibIKogrhU64w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت رسمی Sing-box برای سیستم‌عامل ویندوز بصورت پیش‌ازانتشار عرضه شده و طبق اعلام توسعه‌دهنده‌ش، همون تجربه‌ای رو ارائه میده که پیش‌تر در نسخه macOS در دسترس بود.
👉
github.com/SagerNet/sing-box/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/ircfspace/2496" target="_blank">📅 08:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2495">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YFvPeyyuCQIsCKgbuhAro8xEJW_l18n-zWdigwzAJ-4_1BNL3gJFxMmh7uK4DjKw0vDJNA4ELE0IkN8ZMrFivFnuvkjW9bh8s6a18Ql_6YIdZ-ILl_bM9rdUd4DQAa9wvZoniHudacQfFdbEll4Y26OAINHSLlY79nkTO8wj9vl3RiV4GEKVvYOdPw7d1716G0Jk89lnxQxS1R-MMsRJ92v-uJHZbFCqYC1G_gFNr4rQm8L1F46jpi0fKmcARV6Ia_BrKvqYinRtoDELz-Fw7TKVL2Tvin1hc93-Mnvw3sHJI_vHOBzqKfRScDSzDi57b6BgrhgxO-OOKDSYWMuS5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aether-GUI یه واسط گرافیکی برای هسته Aether جهت دسترسی به اینترنت آزاد و دور زدن فیلترینگ هست، که دردسر سر و کله زدن با محیط ترمینال رو برای کاربران سیستم‌عامل ویندوز حذف میکنه.
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/ircfspace/2495" target="_blank">📅 08:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2494">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TWJbscTjp6XISpVo86pwl9De3Xf4SMGParCh7mJjlCpXXmCJyliGueRpwc5fLbVWknUi_57LLhC4n7m7EN2Olna6sJDT5fszwCmhaOWVY6J5-B-HiDvVOdbpn44eNAe3k0xPvXGzT1HwS5nARTi6UQWOtDsoKorUZ3wgykSnvWtXKeSJPmhTr3uLKQyy9J43m-1FzhZqSqcUe6FFTm7ZLlNqKjSyzmr1Y3bjlmgAyL5FKVVY1bh6FudHuKjXWcUmh3CJ4dWkf4MCf-15-pBK_RUXq5kIxwu2nOPlpy2SVoYR7miVQiWMTNGRYcY585ShhMoaxvONdb3bpQykOAfO_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت در بروزرسانی امنیتی جولای، بزرگترین بسته اصلاحات امنیتی تاریخ خودش رو منتشر کرد؛ بسته‌ای که ۶۲۲ آسیب‌پذیری منحصربه‌فرد رو در Windows، Office، SharePoint، SQL Server، Exchange، Defender و سایر محصولات این شرکت برطرف می‌کنه.
اهمیت این بروزرسانی صرفاً در تعداد خیره‌کننده آسیب‌پذیری‌ها نیست؛ دست‌کم دو Zero-Day Vulnerability پیش از انتشار Patchها، عملاً در حملات سایبری مورد Exploit قرار گرفته بودن.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/ircfspace/2494" target="_blank">📅 07:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2493">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jCcaxZyiOYLWlce-6ieOtmv_x5XXW8O0iupjWm8yJuToBpZds6qsu_A7ZF7MC6cpji6ZUvENBoPlUpoT2Y1rUYB0ed4kKCAY4MihD2of8uMIumoeoS5-c-2mqYz_sLHli_53xdJM3hx25P1agOF6-gKvsoptfuWSrPhk_BZyd1j5QpyYt2TYBrplAMjQXMsNHvgMtRcDwa9sddpfH7Uu7Mruly8eJVup9zIzLGfBfX225EXeVXoODyBR-ZHtz5cdeWUxVbKvRcewKrVX6tAKNsrtNlWWRGdREbvLGHkAKJW8ljteBpGBKoJYDhpOKCrJiSk6uNGBFS9YqabJ_UTdgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه Aether یک ابزار متن‌باز و رایگان برای دسترسی به اینترنت آزاد و عبور از محدودیت‌های شبکه هست، که با تمرکز روی سرعت، پایداری و مقاومت در برابر فیلترینگ توسعه داده شده. این پروژه با ترکیب وایرگارد، MASQUE و WARP-in-WARP، ترافیک رو تا حد زیادی شبیه ارتباطات عادی نشون میده و به همین دلیل روی شبکه‌هایی که از DPI و روش‌های پیشرفته فیلترینگ استفاده می‌کنن میتونه عملکرد خوبی داشته باشه.
یکی از قابلیت‌های کاربردی Aether اینه که خودش بصورت خودکار اندپوینت‌های تمیز رو اسکن و بهترین گزینه رو انتخاب می‌کنه؛ بنابراین نیازی نیست که تنظیمات رو بصورت دستی انجام بدین. بطور پیشفرض هم از HTTP/3 استفاده می‌کنه، اما اگر شبکه‌ای QUIC یا HTTP/3 رو محدود کرده باشن، میتونه اون رو روی HTTP/2 قرار بده تا سازگاری بیشتری داشته باشه.
این پروژه روی ویندوز، لینوکس، مک و اندروید (از طریق Termux) قابل استفاده هست و توسعه‌دهنده‌ش اعلام کرده که بزودی قصد داره هسته Aether رو با زدن Pull Request در فیلترشکن‌های ابلیویون و دیفیکس ادغام کنه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/ircfspace/2493" target="_blank">📅 19:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2492">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VGPC0EAVZ5R3swsj0dYjuQBSmwM0Dx9ZhVPFuS07Vo4s2OMoNqytq4pvp359byHtSyV7ddlDT_Uf75srRgGhFG3rqC11RAfpfEPXmbXCXTo7bCDMqHju1VMaNWOMXDSxWPPqAQJhV1ApqhnbdH_hiFBahrQNuwF3CTEqKidNJCX2SCs5mamiukBwmfAvIw8ANSkhAbC6xPkhdmgCz0I48DioU3qQRVNV_suISYNFp2Hjb615konoAeLEpQxgzn--LEUjfNtTfYlOKZGNZbz5c1O91YxwNffzi5jdPAsSrc4pTUsn1FKteMRlgrf8KHTQ50yY0uhq-cWDG0HFrCvo7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دامین
t.me
که بدلیل تحریم‌های وزارت خزانه‌داری امریکا مسدود شده بود، مجدد فعال شد.
©
Linuxmaster14
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2492" target="_blank">📅 19:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2491">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">نزدیک به ۵ ماه مجلس تعطیل بود، آب از آب تکون نخورد. ۱۵ ماه وزارت قطع‌ارتباطات هم تعطیل بشه، وضع اینترنت بدتر از این نمیشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2491" target="_blank">📅 19:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2490">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دیروز کاربران گزارش دادن که IPv6 بصورت محدود روی بعضی از سرویس‌دهنده‌های موبایل باز شده. همزمان گزارش‌ها از اختلال شدیدی که روی اینترنت موبایل و ثابت بصورت منطقه‌ای اعمال شده، زیاد بوده.
در مورد اینکه آیا با از سرگیری جنگ ممکنه دشمنان داخلی اینترنت رو قطع کنن یا نه، نمی‌دونم. البته قطع مجدد اینترنت از کسایی که ده‌ها هزار نفر از مردم رو توی ۲ روز قتل‌عام کردن، بعید نیست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/ircfspace/2490" target="_blank">📅 08:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2489">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KLgu61R9G3LQGFgGM4oV-o4HXPeRwTYxkuC6TGjJFqWsId1kro5wTIU8CwihlFr91naRug-C4ESsY_O_n8N90YAmrD8_az0VS338o9d6B5ooBjM9UojE86fnl0093PerGk3ie8h4ctpx6ZmkP8dq2mSHHF7DhXoNqw-XyUrxQC0LSmB5_-Gc-nBAgSDEp_7x9kQfBEI6h25cWH_6p7iT9j76AW4_ldq8te9SlCgz9yrIn2PMf5mTKRVzt7tN-De2PghOUZPQs1xFLN6TYK7AKVkYlcd6UsMvMlTspG5Lc9V8rcsXdjPFXkAWY-wpT-R6Jes3OOEP1107jRvgFYAVAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به یکی از شرکت‌هایی که API می‌دهند مشاوره مارکتینگ می‌دادم. چند راهکار برای کاهش هزینه جذب مشتری یا CAC گفتم، ولی تاکید داشتند که باید API‌ رایگان هم بدهند. پرسیدم چرا؟‌ خیلی راحت گفت: چون رایگان است، طبق شرایط Privacy & Policy تمام پرامپت‌ها و داده‌ها و خروجی را می‌خوانیم و ذخیره می‌کنیم. فکر کردم شوخی می‌کنند. بعدا دیدم نه. جدی است.
(...)
مواظب باشید، لااقل اطلاعات حسابداری و مالی و مارکتینگ و اکسل فروش و لیست مشتریانتان را به این API رایگان‌ها یا این سرویس‌های هوش مصنوعی حتی پولی که در ایران هست، نمی‌گویم ندهید، می‌گویم دقت کنید.
©
AdelTalebi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/ircfspace/2489" target="_blank">📅 07:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2488">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZHzRm72UnaWpnKY5hWK1sZQbjuyyVbeho8sBIiMHJLfb9whwxZQnGq91jr7y4endYExrrAF6b_KGc4_Rf0qI47eiV6UuuRoiYW-fLc57N8rsnmCvyWE767VC6u-BcvmOp_PLL7srKOTw_fYa59Ymx_5Ti_sJhMmTePe2Ec8x6tGKLvUm_K7Nqly_7aedwyVIjz2ker1Wj8NHRum5RU-jD5DfusyzjgNJ0DiT_XzVjcj-3UbnYrz6kwtspcM_38JGOI3L7rggXbDakpepJrEy1jX8RvsK-HZjV1sQ25Fi8wj_TViu2T1YhWdwsUiHdFCyjZwJRUK8z-0C1B4l0MTg0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروتون در
یک مقاله
جنجالی ادعا کرده ویندوز دارای شناسه‌ای پنهان به نام GlobalDeviceId (GDID) هست که میتونه یک نصب ویندوز رو بصورت پایدار شناسایی کنه. به گفته این شرکت، این شناسه حتی در برخی شرایط با وجود استفاده از VPN هم میتونه برای مرتبط کردن فعالیت‌های یک دستگاه به کار بره و حذف یا تغییر اون برای کاربران ساده نیست.
پروتون با استناد به یک پرونده قضایی معتقده مایکروسافت درباره وجود و نحوه استفاده از این شناسه شفافیت کافی نداره و به همین دلیل از عبارت "ویندوز یک جاسوس‌افزار است" برای انتقاد از سیاست‌های حریم خصوصیشون استفاده کرده. البته این عنوان بیشتر یک موضع انتقادیه و نه یک نتیجه‌گیری فنی قطعی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/ircfspace/2488" target="_blank">📅 07:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2487">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">بانک ملی اطلاعیه زده که "کلیه خدمات بانکی و مالی این بانک شامل همراه بانک و اینترنت بانک مجددا فعال شده"، اما ایسنا نوشته "اعلام بازگشت خدمات بانکی به شرایط عادی، لزوما به معنای پایان مشکلات برای همه مشتریان نیست و گزارش‌هایی از تراکنش‌های ناتمام، کسر وجه و اعلام زمان انتظار تا ۳۰ روز کاری برای تعیین تکلیف، نشان می‌دهد بخشی از کاربران همچنان با پیامدهای اختلالات اخیر دست‌وپنجه نرم می‌کنند".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/ircfspace/2487" target="_blank">📅 17:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2486">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">طبق گزارش‌ها اینترنت در برخی نقاط کشور از ساعات گذشته با اختلال و کاهش سرعت همراه شده و دسترسی به برخی سرویس‌های آنلاین با مشکل مواجه است. همچنین گزارش‌هایی از قطعی‌های مقطعی و افزایش خطا در اتصال به خدمات اینترنتی به گوش می‌رسد.
©
IRRadar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/ircfspace/2486" target="_blank">📅 20:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2485">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WGS_-LGnqarvW25SMrG0ipMA0ZOc-5LQ83oItEkXAAWu1AAkLso33egDitB1Gpeu6BnT-K2RMWhW84Z4saSHdBiOnisxD976j1M8fDMrnTtLRs5dxAU_GxlSPmLH3bq_Rxpw-CeFY8poWzjjUlpGVjO_U_KoVeJJ6YckKOkBLxHbyiWBrFoLMO-0VjJ57bvXElN4e0nd1xJill57rAAgml1H2kk08iQIHVpC8CaUgKqYr8tnQMHldNHJYgdhUPZGwfmu43bOypy2SPfcBHjC195sgDhH3wkYxK5PmOo_u0eodPIXekn4KsISOR8tw-V4a0leAAZ8oxRjN5_AzwwkgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن JumpJump که بارها نام اون در گزارش‌ها بعنوان یک اپ ناامن مطرح شده بود، حالا یک محصول پرریسک دیگه با نام SpeedTop VPN منتشر کرده!
این برنامه با وجود چند میلیون دانلود در گوگل‌پلی، طبق بررسی‌های فنی پس‌کوچه دارای موارد نگران‌کننده‌ای مثل وجود تعداد زیادی ردیاب، درخواست دسترسی‌های غیرعادی و کدهای مرتبط با شبکه P2P هست، که می‌تونه دستگاه کاربران رو به بخشی از یک شبکه انتقال ترافیک تبدیل کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/ircfspace/2485" target="_blank">📅 08:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2484">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V27pZES-_6PRepUVhPevEmsguEHdJDUF9_IfCoSwCMpMKgOgthGMWYYRoOtY4BgaQ8DMQPyqVP45Wgj8wlQaKT5hTjcdWl7OeNpnynbxXUFSJ5Ujf3HLES5X_Yrg721ynIjBrYSu4ZHkvpPfte8m6m0KhQBN4hpqvoOnAQIGUU-SnQOEpyb-2lGP1Gkgt0VEVwyPIAUnKVtvy3lsFx9_nQDKEMYVKjUqPgQ6fM0xM9bRIt9uUJEA5PzrhjDk0FYCG58IAQpEqBtbN0pEx-jAXRyyQ2RykU3Uhv7LQ1jDTVmRNyZmO4HBWXySdbpTNTGGhr7Hj_TnDHJPN8vKXf67LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنل زئوس یه ابزار متن‌باز برای ساخت فیلترشکن رایگان روی بستر ورکر کلودفلر هست، که امکاناتی مثل آیپی و لوکیشن ثابت، دریافت خودکار آی‌پی تمیز، لینک ساب و QR Code اختصاصی، فرگمنت، شبیه‌سازی فینگرپرینت، بکاپ‌گیری و ... رو بصورت یکجا در اختیارتون میذاره.
👉
github.com/IR-NETLIFY/zeus
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/ircfspace/2484" target="_blank">📅 08:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2483">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XftL-hTmgWtgZTbIbYCWygeD85LUCq9jOo7lr3kGe44e4mAPeQkzq5hZSjOl8GMa0rVVvvAM1HBiQkIhJpLMppKR8AFDaYvs59Pi5tr1Ytyn-RlCTuN1Wh0U-09joeO2ijbz6e72Fk9_i_9lV4yZ1yxjEErOFp2g_TRB2lPQtnEi_ti-vDPHeSoganPGK5tDL9g3iFu5yujqMoCqLS9oW0DJwEliMH9JojnWCGrfd3qIwxUtoWaup2fFt9jH02CW-6fOS7Uf2CQlUBpqpKKslOnLbncmyTUuIz_EtRjbXXDNvrIsy2_8nMLwewPeCTOQ7xi4qpqhGNwuFpDEb7XSWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت یک آسیب‌پذیری روز صفر در Microsoft Defender با نام RoguePlanet رو برطرف کرده که می‌تونست به مهاجم اجازه بده تا با سوءاستفاده از یک نقص Race Condition، سطح دسترسی خودش رو تا SYSTEM بالا ببره. این مشکل با شناسه CVE-2026-50656 ثبت شده بود و حتی روی ویندوز ۱۰ و ۱۱ کاملاً آپدیت‌شده هم قابل سوءاستفاده بود.
©
bleepingcomputer
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/ircfspace/2483" target="_blank">📅 08:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2482">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vIoVCtERz_WFoB-Cz_00wg5xYfJhroUju7lDYirf1fNf3xtM_tmcvjBIKzpe4fSOvZtG3wXUpY_734FcHcPABB0JpqyVurExwkdjNhdmOXx_U4SNkbB9ojUXCRW_ojV3zTmWMJUZRdT1UZ4FTWYfdUc6fESr5wslWrXqpAZTf7jqGrf8PgbCOtQ786Mcm2DwfUuWDqC5nNnCO-0pOVeiYYDF1FTOamSFEUBkHvmTbOE2GNl_F_mQW4n9WmRSBnDwvUq8gfOSOVwK7WwKdl0VXweT7AskIHC83RR8fBhBUNE-LgYvqrBF63HEY0NlRnWohLNgSRzFdQCQZFzaw_VXpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت اندروید NipoVPN که برای اتصال به هسته این پروژه و مخفی کردن درخواست‌های HTTP داخل ترافیک عادی وب طراحی شده، حالا روی گوگل‌پلی در دسترس قرار گرفته.
👉
play.google.com/store/apps/details?id=net.sudoer.nipo
💡
github.com/MortezaBashsiz/nipovpn/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2482" target="_blank">📅 08:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2481">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ojqammxSTYARs-dkXZJpTJ4vfoliX64TLDcUWqEHfLSEiWMuHDnU4QsQvNel5yUblgnmADisD0rjqu_pNbgKLvTocfMXboAJMVuDvlsY51XL8izYMqlj6zo6VrXBawxGuvi8lHOIyQJHzHkI3r7t-RTy2V0-vrD-U0bhmGPUi-sJXapiuy_uHARo-ouWmYL9p8XIwEMvJvFf1ATsaWnfL4hqMXr0o1eRwa5O97zK_4xjXamZCujl8RQlfcLdJDuVPcbJmXA813VQSjmfQrLMzFLApRIPhmGgRWSJ_EY0bLHI7lF8AHUHdR2p9oR3LYJXVNz3iBER_fA_n3ftp17GOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابزار BG Scan یک اسکنر متن‌باز و رایگان برای پیدا کردن و اعتبارسنجی سرویس‌های شبکه هست، که اجازه میده چند مرحله اسکن رو به هم وصل کنین و عملاً خروجی یک مرحله رو بطور مستقیم وارد مرحله بعد کنین تا فرآیندهای پیچیده راحت‌تر انجام بشن.
این ابزار از پروتکل‌های مختلفی مثل ICMP، TCP، HTTP، TLS، DNS، DNSTT، Slipstream و Xray پشتیبانی می‌کنه و علاوه بر اسکن، امکان اعتبارسنجی و مدیریت نتایج رو در اختیارتون میذاره.
👉
github.com/MohsenBg/bgscan/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/ircfspace/2481" target="_blank">📅 08:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2480">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U8vwO1qrbra-Rxk-w_yyxwZ3_s7fzpifdvLtDNx7Pzz9TbKJUJ7-KQio_Ll4oeAJZDS3rjHkRUcdA0OnFGssOLtfXBrxB5jf07AHIZhk_WWaUhrtk51cVTaBqAS-P1ctEp2s-o2hcuzqRfYjgtlAyquVFKIHcT8ZELYq8G2B7mA2A9LBrsNvjBHgjvcnTbbYVCSbKlPykqteez6dHWwTNSYL0lOnC6-2dSw3LKnjUHOqXQAORF02IZaeJgFVTywTRVvkafODaIA4eTnXjP-b0asA-MKhDcbNBUxD6_P_h7gsnnE93O2_kXWFN41rPOcMgbbNvNR80pKmQ45Mr1BPoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاوه یه ابزار برای اسکن، استخراج و اشتراک‌گذاری کانفیگ‌های فیلترشکن هست، که کار پیدا کردن کانفیگ‌های سالم و به‌روز رو راحت‌تر می‌کنه. این وب‌اپ میتونه چندین کانال تلگرام رو همزمان اسکن کنه، کانفیگ‌هارو بصورت خودکار استخراج کنه و در نهایت یه لینک سابسکریپشن بهتون بده تا مستقیم داخل کلاینت‌هایی مثل v2rayNG، v2rayN، Hiddify, Streisand, v2box و ... وارد کنین.
توی کاوه می‌تونین کانفیگ‌های خودتون رو با بقیه به اشتراک بذارین. علاوه بر این، حذف خودکار کانفیگ‌های منقضی و امکان رأی دادن به کانفیگ‌ها و منابع از جمله قابلیت‌های این ابزار رایگان هستن.
👉
kaveh.yebekhe.workers.dev
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/ircfspace/2480" target="_blank">📅 08:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2479">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m_MFHYK4l8l0Pfc7ZNwFt2dxUBn1Lem0YKkdVmgZb592APz2erHHSWU6Yw_2cgb6Fx-b1H7r0yHUvKZ4ec3EC_4KftnrgtgvmwjZoBpvo8cDZgTQCGwxhcR2HEKUJc9LJNkIbNSwF1TrrqdWJ8cHvZWnq99WXmV2eIBBcSmQccSda3tCZvy5WgzTZYhAmq2mjxh3SM1A9PBUJms2x2CRYJuEg9VPap6zD8eyJcCckwmMyeF1FGcVCZyIANrLe4a91Scjd0TISErJPcNn4P-V_IZvZkLKdqlv8iZKIHG1B7ItuKEsdGPkGK_A939VC0kPmSsdV9qxSf7-IL43OHBvUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ابزار MTProxyMax آپدیت جدیدی منتشر شده که توی اون از بهینه‌سازی‌هایی مثل BBRv3 استفاده شده تا عملکرد سرورها بهتر بشه و مصرف حافظه هم روی VPSهای ضعیف‌تر کاهش پیدا کنه. همینطور در این ابزار که برای مدیریت پروکسی‌های MTProto تلگرام روی سرور شخصی هست، قابلیت‌های جدیدی برای مقابله با DPI و اسکنرهای شناسایی پروکسی اضافه کردن تا شناسایی و مسدود شدن سرورها سخت‌تر بشه.
👉
github.com/SamNet-dev/MTProxyMax/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/ircfspace/2479" target="_blank">📅 07:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2478">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F2wNrhsWNC7feIn5twyyGprS-2E3_xX84ol0REXFvX-2ISPSYDu2cHlJMHcB58lUxwLA2oCrVmPa5lxUAUxBML6F92K21vrR3-bUeT4ZL0aAVfXbk-DPs2puWh8xcchYmNYQkB-z6LgonRSiL2JJAOFJd5TnqI3Bra7IanptanBCtG6jyy66cSc9rYxFVxcMh7xYJTWm8zwqgNox_2oLRpFEzdcvKCuTU0opZGkqtSspAAPt67TQHueISJMvVCb7_A3oKIgNGoW9vThW9W2YG7YYZasa9CAfbk9wPSUGSnd3F4BrRC8mDr5FMEOooRizLMDOwgLH1zOiFFfPwcci-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Intra با استفاده از فناوری DNS-over-HTTPS (DoH) درخواست‌های DNS رو رمزنگاری می‌کنه تا اپراتور اینترنت یا هر واسطه‌ای نتونه آدرس سایت‌هایی که باز می‌کنید رو دستکاری، مسدود یا به مسیر اشتباه هدایت کنه.
این برنامه فیلترشکن نیست و آیپی شما رو تغییر نمیده، اما چون جلوی سانسور و دستکاری DNS رو می‌گیره، در شبکه‌هایی که فیلترینگ از این روش استفاده می‌کنن می‌تونه باعث دسترسی به سایت‌های مسدودشده بشه. علاوه بر این، رمزنگاری درخواست‌های DNS تا حدی از کاربران در برابر حملات فیشینگ و برخی بدافزارها هم محافظت می‌کنه.
اینترا توسط Jigsaw (تیم نوآوری گوگل) توسعه داده میشه و سورس اون بصورت متن‌باز روی گیت‌هاب منتشر شده. این اپ از طریق گوگل‌پلی در دسترسه و برای استفاده ازش فقط کافیه یکبار فعالش کنین، تا در پس‌زمینه کار خودش رو انجام بده.
👉
play.google.com/store/apps/details?id=app.intra
💡
github.com/Jigsaw-Code/Intra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/ircfspace/2478" target="_blank">📅 07:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2477">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T-0qhNB9pMDfJJeNpKIp2rNwQXMzG6osfs8fAWYLmAWfSIsKCRjhp7VuRjX4whb5r7dmPMYjzmcMxJM_JJ7Z11pLsMLw_1FvfN0SklZtYn80kjvl2MnVlaFWOy5GJUaaXoKjXyxwjEn0Ch3KdEBLdtFjG71RdUDS1OPn4g197pA5Qvbzqo-RR5rdPfwCSTgyLZ4S7VTLzZXfTkRRrHLBPXsEXEg-bJgxyj13AhX06WwiYf2F9m_wDb_RSnMPO890d-R1ZFjoKVdPyxWah9f4Unr9uU0y4AwmtnjiUJuJ7h5Of_jrke6NHqsstNy7Xxg9rliV0NXpU9mZoiQ5Zdv5sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محققان Datadog میگن مهاجمان با استفاده از بیش از ۵۰ حساب قدیمی و غیرفعال گیت‌هاب و توکن‌های دسترسی (PAT) افشاشده، از طریق API گیت‌هاب در حال جمع‌آوری اطلاعات سازمان‌ها هستن تا برای حملات بعدی آماده بشن و ساختار داخلی، اعضا و ریپازیتوری‌های اونهارو شناسایی کنن.
توی بعضی موارد هم تونستن ریپازیتوری‌های خصوصی رو کلون کنن. به گفته Datadog، چون این کارها با حساب‌های واقعی و API رسمی گیت‌هاب انجام میشه، تشخیصش از فعالیت عادی توسعه‌دهنده‌ها کار راحتی نیست.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/ircfspace/2477" target="_blank">📅 07:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2476">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/URBcEjGmChu-RFws8Me4TOzFRSKToB8zuanMnOCfB5iVfWaMveY3wlMbVtZNKsk-FpWC4P5XgPKs_Ep5hojjo9IPKeVdiQN0MkDO5NGOXvIBMdPSrq6R0KvEKIayqOfh8OpbF0VcPn-fNKbuYecNF0OUe3yI1p1Rd4aej1JYZG0I6tSG02JrwWZoI-d6afAUPYIngBAUAujln-G97k5JopyJzvfPejKJv5ztijlazgJ1hpNzpsP2iS_yWXqP8iDUZJz5NXE2aOdMBUmKKrSIxi5QKnUJ2zUiUk9O-6z8gZ2Nm3g7RiG0Qoy0cbP8X1RU2B28Cd9J7mbQRV2MBxzsTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایک سنتوناس، مدیر ارشد فناوری شرکت CrowdStrike میگه خیلی‌ها دارن روی این تمرکز می‌کنن که "کدوم مدل هوش مصنوعی خطرناک‌تره"، در حالی که تهدید اصلی جای دیگه‌ هست. مشکل واقعی اینه که هکرها حالا با کمک هوش مصنوعی می‌تونن آسیب‌پذیری‌های قدیمی و جدید رو ظرف چند ساعت، و بزودی شاید در چند دقیقه، پیدا و سوء استفاده کنن.
به گفته او، هوش مصنوعی بیشتر از اینکه باگ‌های کاملاً جدید کشف کنه، باعث شده هکرها بتونن تعداد زیادی ضعف امنیتی شناخته‌شده رو خیلی سریع به همدیگه وصل کنن و ازشون برای نفوذ استفاده کنن. یعنی اگر سازمانی هنوز وصله‌های امنیتی رو نصب نکرده باشه، حالا خیلی راحت‌تر از قبل هدف حمله قرار می‌گیره. هوش مصنوعی لزوماً حمله‌های جدید خلق نکرده، ولی سرعت و مقیاس سوء استفاده از ضعف‌های امنیتی موجود رو چند برابر کرده و همین بزرگترین تهدید امروز امنیت سایبریه. /اکسیوس
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/ircfspace/2476" target="_blank">📅 07:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2475">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n_qLsFmZnC8jjXrdbMvj8d78mOgmepnMAsdLrtHmsGwaaORrcNAv3fDESuZ6SdowZJzzPLOqrN-rmuX2FbiGk0eq3G7c5M15i9lW7Ch5Af8SEBrV3sUq4GiAMnJn5mE94Br6LDd57tbrUAi1oE8iGMIj2xKlnenFCTwvO8oLoi69v1bNf0Uxi9It3i6kllZ4nitBCm7Wxm0dD8oJ9i7qmXIOJEoxnIW2_ICo5Jduz01u8RxsnzvNw3FWq8p_nH-ttar7jwMtahEJOr52W_uDNeQk7I7sGOYyPrcKkaxVQxUjmfbrky-LcvKPZcE-JokH-dCX9fTVJX3iLC93xJ80-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ GRoute یک کلاینت متن‌باز و رایگان بر پایه هسته ایکس‌ری هست، که امکان استفاده از پروتکل‌هایی مثل VLESS، VMess، Trojan و Shadowsocks رو در کنار ترنسپورت‌های مختلفی مانند REALITY، TLS، WebSocket، gRPC و XHTTP برای دیوایس‌های اندرویدی فراهم می‌کنه.
این برنامه از قابلیت‌هایی مثل اضافه‌کردن کانفیگ وارپ، مدیریت لینک‌های ساب با بروزرسانی خودکار، مسیریابی تفکیکی، پروکسی برای برنامه‌های انتخابی، فرگمنت، Sniffing، نمایش لاگ‌های Xray، اسکنر آیپی تمیز کلودفلر، امکان تست کیفیت اینترنت، بررسی پینگ واقعی، تاریخچه مصرف دیتا و ... برخورداره.
👉
github.com/SuOracle/GRoute/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/ircfspace/2475" target="_blank">📅 08:14 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
