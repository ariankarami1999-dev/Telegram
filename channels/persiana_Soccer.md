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
<img src="https://cdn4.telesco.pe/file/WBzt2zUGlmcITvCdpAhzq3bbONodZEvLiZioWT2xcJ_ftTkxDoiMmeSEPr1iLurQyq_kRuoIG37squRxOUfB2BB4zKcVYX5VQWDjO4UixvsN6ZvJAVOia0fDVx6rWCBkifsF3L1kTVKX2GIis7oviniXTDtzy8WolvHF_yyR9m1KENEHmi3EqXyCtDNLnXH-87ZgERrdrdhaVwzYkSQysNYFtF0xDDsedcXh4kYfL-PCMBIZyerMbDcaeprbOpYDVs4X74CGAsDxz3nYQnDHBaxZYo42MJbGZNleXUVhUx8dax7VYNULG22ips6zc7tPVbaCqMjTMafkDZTMfnevyg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 371K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 01:55:57</div>
<hr>

<div class="tg-post" id="msg-24976">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5736be2a0.mp4?token=GezN3ksoTu6rNwnp01shMoZMDusfd0yKil5tND-FbS9cXhnHhLICGAEoPMUwrZFWwcsJStz_MVAaQu3FfQF9oKlu3zCLSZzlA9es029n14NAXBhtMpvMx4rhDRrsTAqnS4bs0QsQ8jdnMquQcDVmbRNWXAwxn8oyxQD1Vmez_n-JkyvL_GHMwPyefwOHvLyO8u9hbHIcHyOkVUBjW-nt2Y6lDjPqDpulqpBJHgCI4WD0mdLBzREuICncjV1SnTFVBr_HPRnLKHGPCZaxj55564rUJk3e9dqhYJOn7ryouRwuaEMHYB0_oag-9NpXXHpySzdzugRhNHkixExm6txj2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5736be2a0.mp4?token=GezN3ksoTu6rNwnp01shMoZMDusfd0yKil5tND-FbS9cXhnHhLICGAEoPMUwrZFWwcsJStz_MVAaQu3FfQF9oKlu3zCLSZzlA9es029n14NAXBhtMpvMx4rhDRrsTAqnS4bs0QsQ8jdnMquQcDVmbRNWXAwxn8oyxQD1Vmez_n-JkyvL_GHMwPyefwOHvLyO8u9hbHIcHyOkVUBjW-nt2Y6lDjPqDpulqpBJHgCI4WD0mdLBzREuICncjV1SnTFVBr_HPRnLKHGPCZaxj55564rUJk3e9dqhYJOn7ryouRwuaEMHYB0_oag-9NpXXHpySzdzugRhNHkixExm6txj2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👤
👤
این‌روزها ترکیب جواد خیابانی و خداداد عزیزی خیلی‌سمه‌خیلی؛ از دست‌ندید. این بار خداداد به جواد گیر داد ولی دهن سرویس کم نیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/persiana_Soccer/24976" target="_blank">📅 00:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24974">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fs0cpzgNs6BwDOPPznL5uOQj2SHuSfFVme6fA5Lc_QmMe3UKV6rtmroMOMKFCDvKS-iwSNa-Z_FR729-IZBBJJIU9146vvlEGes1CMTLaZ0ooJ36kF0MLeBlAJWJ574IMiWozVg1lXbmeGjKR-OumT511hHfE6aR7cL-HwPWxj5jKqTCiDRtMR2_rUSq8AHi79_zyWClBbUXoxUYmdLFEK-B8Or00bFwrDNvzq3ehq-ENWCSa_ojbZEQf7tUtKcfLqwd8J2cKCG1qJVgUWUjVAM2UtyUhznSBTwb0GDR21R77oX0qHk6OAsduzDogEScOTwH3C50-c_zE9pdHfz2dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ گزینه دوم باشگاه پرسپولیس برای سکان هدایت سرخ پوشان مهدی مهدوی کیا اسطوره سرخ پوشانه که مدیریت باشگاه پیشنهادی سه ساله با دو دستیار خارجی به ایشان داده است. مهدی مهدوی‌کیا از مدیریت بانک شهر حدود یک هفته زمان خواسته تا پاسخ بدهد.…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/24974" target="_blank">📅 00:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24973">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vO5yBqTVBE2sm20Gn2dHqnv7TIdzpYHLOYlknWz869D-_CAnyMG2ptkbvEpkZXRBNz8X5WL-aNYPGksOc_ywjvaOhhMcS5YVE_pBSOtcyVEq6pLH5R8ailGmBGSVII0KWQ33i3trdpMC57V811BW1IZQdnbQCjaOq5tD0ex1_nukJHQdLhxnEC6lnVdLK6T9BQbPokCBqjv14-cV7ERuXNN13CTCTBv2uEEahWq4a7RAo4qolZxdf32pqNmIHPjN0VGwf7taeFNXbYpZvBZ146tgNmyLA5xBF4F3aqYIP2eLyBvc2xnUh33z8wneRjrocXTzWVpQ3WUft03E7VbgEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارها‌ی‌‌ امروز؛
از مصاف فرانسوی‌ها با پاراگوئه تا نبرد تماشایی سلسائو برابر یاران هالند
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/24973" target="_blank">📅 00:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24972">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdMH_NIDsspAZrlQy8RerpBR-Cl6HqA6-e-Z1IYFMUHKJKfiTZKKvgMJjTAO9Qx4wqEiQlDZeZJEIEBTHz6Z8yChtDF8Jwjx7D2NSyfj73XmPeOSOdhcTPvVq58vB94Ov7cFRJKUlqAgpDbPn0Ld3CLUr4L8uzbb-V6qrRBJwq8NVlqcRQD89W41iKrlV032j9mBn7mLG6Y1Qn0DTWZp9FqFijr_Ac8oiragTeWaEwc7YMTC_rHHgKi2_9zu3KyJHjwZdxZpsTB1ArJuEJFQpXAZRDc_qiEACAwWAdQ-YHA4flmix7uRSl9prLkAdvhrPQFH47WS6f54LDGU7TaaQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
صعود دشوار و نفس گیر یاران لیونل مسی در دیداری تماشایی مقابل کیپ‌ ورد و برد قاطعانه مراکشی‌ها برابر کانادا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/persiana_Soccer/24972" target="_blank">📅 00:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24971">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/persiana_Soccer/24971" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر پنجشنبه تا سقف ۱۳ ملیون تومان بونوس ورزشی
🔗
بدون نیاز ب فیلترشکن
🤩
آموزش کامل استفاده از اپ
🔜
💰
💰
💰
💰
💰
📱
Telegram Channel
👇
https://t.me/+dukgrB6-zGsyNGM8</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/persiana_Soccer/24971" target="_blank">📅 00:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24970">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ge6SdET3HiYOH_Jd15cw3Fdy-qh1jWmiUgQBkYcMP08suW0fkcC5V4QlfqajMfa8-pUBYL-oV-36i-Ks7mRa1-uHETXWZTZl42lVthz1YkSUORCyYKrPU28s0pkEBbBVXAtz1ssdPLXqGO1Yk6GEuCLZ8jbDwWyUePPsb5ntns7swnY0JF5ivh2tY3nwWv96jsdxdNN7YJjMp-CLeTPi-fN_WrNIIGorxfQFrcgmtKnPnOGqis5q6TJK9_N9h3cWVl8DkzjYVQcLThTQTO3bqOpTgEak_7faFH2fpj3cEwM1EPhNXt7NtJ-OG4MzB_oNBSUhLNsmRY7JZYsYvGtDrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اولین سایت جهانی برای کاربران ایران با واریز برداشت مستقیم
⬇️
🪙
سایت بین المللی و معتبر لاین
بت
❤️‍🔥
اسپانسر لیگ  فرانسه
💳
واریز و برداشت ریالی
👀
بازگشت باخت ب صورت هفتگی
📣
دارای پشتیبانی فارسی فعال
🎁
بونوس
💯
روز های دوشنبه
🎡
کدهدیه ثبت نام
➡️
L5670
🔗
《
لینک سایت برای کاربران ایرانی
》
👍
《
دانلود اپلیکیشن اندروید
》
❤️
https://t.me/+dukgrB6-zGsyNGM8
🔻
جهت استفاده از وبسایت از آی پی کشورهای آسیایی
🇷🇺
یا کانادا
🇨🇦
، استفاده کنید
13
🅰
✔️
آموزش کامل و جامع شرطبندی
👉</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/persiana_Soccer/24970" target="_blank">📅 00:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24969">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNqgkvMUhul15PXaRNTNu_AvJPBfuEcXEVMZeAAQH_gie1If4LUdhwH5dB3eZWzsrrDLEwk-kRsggZYaNV_8wJTfj7U1XYTjEgE3SPUOv2M84-CIMYxWDtsjGKps5B5Wlhuzy77nzCkMvoy0kx9d8cy9hP1PHY2ZjxbyfNMSejMlLvVTT2pGonf1LBsjX8_x9QONvPqlA4Wb8SvXfxqw6-6213XEFa5-XfpOqNSxVTsWBHmwBA-fKh_HnF-0pd7gaLWJzsQig3EjTjcNFSefUqMGEmcqVb_9TdoZ_fQe9T2u9jlrQ8-mzgM7Q0CLjnZY8CdPPxsvQ5HGGjN5Y7BaNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الاهلی عربستان؛
ریاض محرز ستاره 35 ساله تیم‌ملی الجزایر از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/persiana_Soccer/24969" target="_blank">📅 00:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24968">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDL0LB70NJOFzaXs0iIy36eAE8QqsaQSvkL2adBqt24Ei3OF1Sk6bR7ObbDGcteAr8jsfIu6HbcajcopxfsnRXIpZ1y2BZ-ihqAcp55Uu8B8pkXOz6_zwtUvJ5aMg3bzXPbGhdLUFIANLqps4i8af_d52Ru1D79-qPbtyD05tL1eloGFSvGWxGZ3YkMI12kgrUuXp3SghpCSzjGvxySEd7txWF2kFGyY-npVyYGrFe01MjfoZw6HmkzRVHxN-DCD1ABDVbbJzEyLoJEh5y45VSi_Uti6knFEyTTvATkgyMgLwebFXt2OBMt3LZskWFfCbAzr5GZxc-oGl_OWBIh0cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌دوگزینه‌داخلی برای سکان هدایت سرخ‌ ها در فصل جدید مدنظر داره که سعی میکنیم اطلاعات دقیق و کامل درباره این دو گزینه بدست بیاریم و امشب یا فردا شب بهش بپردازیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/persiana_Soccer/24968" target="_blank">📅 00:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24966">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQbPyBUYqaCsvFw390eV1aIVkLiSzXVTPtuOAJV4DUtWbzSKKT3kbbJgx0aoTUtLF3_hHWu3J64FgU148YkUAEdWCkvGGKFDysmsyClnjq7BDvTVXr3HvDvOROcRTcZkY7JW9lAOGQ5v_NxuGqIYRy89guX8xgku_D8UvB2nD_Sn8onVdyI2TDU2Yx3pXHWD2oi6RnIsKAneCXs_iJSQ5UY8P5K-J0YlJWoPAjzuvuBYYZtnKpfq3qi8Bn10qFHWqZkJ_kKJpYr1Z7F4QikA21L0ohJDTgbXtaR-0Xn1yZC2mKru9R2EuTIGCqwEhKH-pGgzkAE8H7PmGb7qMKjVjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه گلگهر سیرجان که اخیرا قرارداد مهدی تارتار رو تمدید کرد بندی در قراردادش گنجانده شده درصورتیکه باشگاه پرسپولیس این سرمربی رو بخواهد با پرداخت 20 میلیارد تومان رضایت نامه تارتار صادر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/persiana_Soccer/24966" target="_blank">📅 00:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24965">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pnlm3DCZgq-QU8dSTinAKWwZ3XRK3gKieW7Foau9i2bFK4SkkaLeIjPB8HHfh1tsolHmecAKot7Pwn4k62NozMxdfkZHG4y2YyEocvP2v_zvhvtUAiNhR2pM731rrJRTMrPzBnmueWlf4XkzYmoB9wT_QouFTwDbeoMac0RrE3RoH_-CXMMg589GzeK1HYyf5qj168oUXsOzar2z4AoRFxCSYasRQ-CRfOmetrY3vUOGmq1YCjzLzaHdYMYtO0ecAXAri2ysO2m5r7OmNCSE8GKZanKa42CSQaK6wngWB_f5mQwHfaVlSDGtFU2OysaSVYPgLY0KRxFoPpM-9YysMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛باشگاه‌استقلال برای جذب دانیال ایری پیشنهاد فروش عارف غلامی، محمدرضاآزادی + 30 میلیارد تومان به نساجی داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/24965" target="_blank">📅 23:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24964">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCqVlt5rACVvAvD4oozXQyYb0x1SB4r148h2_KQMMPepYe0q8oGeARe11pQE1jAnMEG0rXts2bSEhZJiXS78kCOCw0m1t1ju8A3wPoYvcw9mUvJYlySUdW6zVj0MwfosrtjL89-MbV0NmxGuTHcjnFosjr772bxElo32-yWaF-7cKMiVy7kBW-pfRRzWNmCDaOJrcBUUpXkaD7g7z-StLuDfVMYcAiIJk5ePeXJFJbClzdO4UOBaFMdDsZdoxqwTFSEepWARNnXlPhEGHue_UxKO9hnW4VlX1G18gb1xr_hK-aN3oe4dbAE8obd4l3yUpmi8gG6VzM-wliucFIiC8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
💰
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس با ارسال نامه‌ای به باشگاه نساجی رسما خواستار جذب دانیال‌ایری مدافع‌ملی پوش 21 ساله این‌باشگاه‌شده‌است. سرخپوشان به مدیریت نساجی اعلام کرده که 90 میلیارد زیاده و تا 55 میلیارد ما حاضریم برای رضایت نامه ایری هزینه…</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/24964" target="_blank">📅 23:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24963">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBcKyuu4zBK59MLdfUOCITTuAOZoYQ0y84bbG5af_Smy8t4Aj1swZeYJPYuQOGdMyCxmKRT09TIOugGVS45rEhxvxF4UJRCkkElCfIzbZF8uaP5RtyIkfShBj1LA3j6j-d7RLV3jXLtKT0N70lXmz603Ogn3ytCXQHGT6V33R9zX2b8Lwx3eqjVT6Q4Nsv-rEXZK1A3ZJ7cL3x03QimH5WrbFXVT7pXGRTGwgv8uktQbzzi1QPKIAtju6i-AT3rttLi3G046UKUrEoTlsSUinEaNvn8xmU4y4xZTmkwzkxrnCizMfc8FRu7VVQCuTCvgVMGB1jwUmhr2yY_CpUk32g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
در بازی شب گذشته؛ این هوادار آرژانتین کیتش رو میندازه برا لیساندرو مارتینز که براش امضا کنه، مارتینز هم کیت رو برمیداره و با خودش میبره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/24963" target="_blank">📅 22:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24962">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XSlFoStaTyA4MFtka6b3wMlGAvF2NIqahPXqddcD7MTTN6ux7s1T1w4SgscK8Iby948N8StXeAjerhEmiBD6aKTomY8CJUifgHTp_nrBUi7hcECa73btaBtVSGOHoyylqJK3rbK5b6lvst9HrLx7R2YgaA_9gp3YNT6SmFriodwV5rAmzR8HAzupJXERCnv-6FJwLj4I0F-pF7TANHaWzqib9VTxB9wdxkOxxOoqP-WLFFk8M4YvQwlXbKuEGbwPYUlfxZXr7MJd_OMFAA8243eBlrzNZtvCL9AuJfzgxcYlBCYsh8NRyYoTUf0hh87zNvAU8iV5GNJ5VVkrfZfXHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک هشتم نهایی جام‌جهانی؛
پیروزی ارزشمند و شیرین یاران اشرف حکیمی مقابل کانادای میزبان و صعود تاریخی به یک چهارم نهایی رقابت‌ها.
🇲🇦
مراکش
3️⃣
-
0️⃣
کانادا
🇨🇦
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/24962" target="_blank">📅 22:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24961">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akvAmE3H-pdfeyY_1LhIbg7QDxDmMZ2riunh7LfzDz1qu3fWxvTnToRxQgylN1WS5oa8YMbS1MrhGkomezXKgZq2DYmrd8kvzuCVZoN2CInL6VKNXyptAPDEOR1CB2F6IwCtz1R2HkxkVYCM0CnKHnyjXNPCg0OCwFwLPUP1l4EcFZ9tfeXObtuDaOyI3pLYmiQe8WZwGbn-KK2q6SC1pW3r3sLqbgEWkF1bVGAWZEWmJKndM4txwi5I8CJrWHiakdMKEGoJVxn3A3CBfq-uK7rJm07haRjfl8VkMWItuyP0fGVwGuq2nDFP71X3gIxAIvlNTY7F0qHFf7YpwEofLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/24961" target="_blank">📅 22:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24960">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCBLRZt8NZhnfrxj1bao49SdsmDSuCtXyjWQAtYPDVMAD0TfnFDtLnml-IEUnFVUM1D-lLYOur0wGoh0ekcnvvEaZ2G2l8oF2MGHbCoBQTSRxkGIIdHtmRTHqg9AoHtG4odME1YNkH7bV3utN0gLU8UR32ZtjYLhV_AT3U3F850Kh5D4tSW2PKoMo7lQ7tN95DFvO_Y7Mze_dqVjICXqnsCr34UK8UT1lHOWxMSq7CjHELwTRU9sm6B33zjvuDT_ICnezcr3BrSZIOOkfuakJKhXgSRPCedqn5WXDaRHgrB2n6_997m-gqyT0z_wS1kYyjcUhm7KC6U7_5mE1z-T3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هروه رنار سرمربی مراکشی تونس بعد از دوباره از عقد قراردادش از این تیم جداشد و در حال حاضر سرمربی آزاد بشمار می‌آید. کاش بشه ایران آوردش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/24960" target="_blank">📅 21:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24959">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOT3PEnKf11SOXOE7aWKqo37ZPSyFDkgLRPS5Iz3QHfHsN6TTHuegL5eNFEVfzoSCwn6QEQTOec_13I7PzX4TcjUs_wSkQB5uaIuSq0QOqF-brgDWoxq1-iibvI6YAxTuvazMHZCu0Vu_6ME2MdPuu2kZuzmt_7_5-9VsBoc7iHd8Ez59C-iO8r9HWHjC0xQrJZ_QZavZvYx5NgXNf9-gksCmTJjMqi3qTFo29OaoDVFH_nFT7WHHxawRuYoDtX8_hpJfzAottMcqixJRyWTbRhWiByhZUgcwJ3dbCDHvH5KDEEd4I7AsPI6N73mJhAQSqDQg_Zm1qKCmDkH1t6Fnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇮🇹
🇧🇷
بااعلام رسانه‌های برزیلی؛
کارلو آنجلوتی تصمیم گرفته بجای پاکتا مصدوم نیمار جونیور رو در بازی‌فرداشب‌مقابل نروژ فیکس کنه. نیمار در تمرینات روزهای اخیر با انگیزه بسیار بالایی حضور داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/24959" target="_blank">📅 21:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24958">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b83yXRAY30HV66FGWv_qtGw9hTdjcCd9IskvrY2OXc7KkpGg7sCm8evvbCNYqm5Fg1zfEtiL9dNpXzWY0ZNs8qA8mFzkcic35D9moWNFNkbtq_Qbwm9U27j841fnLSYX9bUF-sHtwBTgF-MvyBXN2Wlsbc5VUNP_2qfRCjmXUD1aFyZPLV5n7kOkeC-TqwblMPJuBFoSpGFkfbphaJEPWzJm88fzHgacVnvL1WtVHRXtOPgPMPm71UkbLzembMAOnk9UBjiP-A2hcgjvs59Tj2uPr1myZlKjVSR7DBxwA5R5eNfW6TQIR-l4nlIkS-ghMaYoVeP73skTLpjFzLTalQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
منیر الحدادی ستاره مراکشی استقلال امشب در تماس علی‌ تاجرنیا رئیس‌هیات مدیره استقلال اعلام کرده تا روز شنبه با خانواده‌اش به تهران باز خواهد گشت و به تمرینات آبی ها اضافه خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24958" target="_blank">📅 20:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24957">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkBPWZnXHgd9-jsilGZNh56uW9gIDXnK0Bf7ZypaqY3mWhKAPyyMupLVaDGCNpGpqUCgN0mj145eLw6tCiIXYq0UPoQGc2AVRKgyy3lPJRDNpK1h6bqmw4XCTd_eD-1NCgSH_Y6D-eF02u1k2PzI67roup_USA6azr36E236QcqvArVbEaIhPuLkct0mRpKFR_XZFK_RHIz-HeUCTf8TkKfRAn0hXm9DbUfjwydYHBAZ8f1O-X5ICCJ_v31GlhhTM2664xnigyZjNYvTjk7pG7vvab-rGfr-75o9m4FV9BCUFeSV-j7F4u7j7cs711KZgnv_L3NhRyUL8trK9nf8Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24957" target="_blank">📅 19:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24956">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUHDU-qVb8ONRU4KmdpaLKx6G6Bqbl4KYgsq24ScWvjO5ocHBxpNP-VcFFB3OnKk-8SiLGEXFpCTHiIc8IniCg2LVLvLbxw0NDfRnywbrRJy1i1F0fIpvQF6MHFLI8zucHp1Ybjb3aIdfJgvKGITeDOeVOr-7mAaHnZHXUPepnuQ1Ex-rwqd2l9Ln8XJnPnMQD8yM0yx7dKNKnLAZwW36gdJ0TkxyYu8ijycxBjVBNKhsaQxXmvPNbrLeTN4gX3vW9C9UplPTt_EIqTD19axwAZtXtvyRhwXXo4c-u_gRvNNnQy9xf3VEesx6QMTNcl1ikeIgIpYO4B2lWZMsPYNwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول‌گلزنان برتر جام‌جهانی در پایان مرحله یک شانزدهم این‌مسابقات؛ لئو مسی با اختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24956" target="_blank">📅 19:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24955">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‼️
خودزنی‌خداداد‌عزیزی روی برنامه زنده جام جهانی از دست جواد خیابانی ؛ میگه اگه زنوزی اینجا نمیبود همین‌الان برنامه رو ترک میکردم و به ارواح خاک پدرم دیگر به‌برنامه برنمیگشتم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24955" target="_blank">📅 19:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24954">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UWMrdfcb4j5sFhsnPHManqwOArAgvtwVsL6-mmgbwx_wpGtBgFp_GvrXNjpZATOatMOb3DNGM5T8lNeoB4UPbwP28IkxQvzAe1HF4i87yJ39CRqZGSb_dRH9WvFx6DesL0cqh_Mwaga-eZQgfvTNfFibI2IFLFUCpgn5LW8CkAo8WYWzm7f55e9_kpWtp2uR11UfaxAV_ak20Z8b50sHPcS3XXwIFNedUTV0lRHZAi6vYLLdxtwuesvFZ3zYOaievtZVQFPI1ulY3frK2Vxgpar5MQpU-wizB1KoyY9TeBkxqSXkfJ7YP2G60NrWUwRbqTQnILK153Cr2lQL6yb9Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
مراکش
🆚
کانادا
🇨🇦
فکر می‌کنید کدام تیم برنده این دیدار خواهد شد؟ رأی خود را ثبت کنید و اگر پیش‌بینی شما با نتیجه نهایی مسابقه مطابقت داشته باشد، در تقسیم جایزه
۱۰۰۰ دلاری
بین برندگان واجد شرایط شرکت خواهید کرد.
💰
جایزه به صورت مساوی و مطابق قوانین و شرایط سایت، بین تمامی شرکت‌کنندگانی که پیش‌بینی صحیح ثبت کرده باشند، توزیع خواهد شد.
⏰
مهلت ثبت پیش‌بینی: تا قبل از شروع مسابقه
👇
انتخاب شما چیست؟
🇲🇦
مراکش
🇨🇦
کانادا
شركت در قرعه كشي:
Https://t.me/betegramd
📺
پخش زنده بدون سانسور در کانال تلگرام
🚀
برای تماشای مسابقه و ثبت پیش‌بینی، به کانال تلگرام ما بپیوندید
عضويت در كانال
Https://t.me/betegram_official</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/24954" target="_blank">📅 19:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24953">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BN75oZ5T0F-OObSMQgXqGLAWt-3jl1-egTT9c3egm252W8AAmyNXJZB-pXNam750UCfxXrLMuRcU-hZX-9OiWo-3w9DyJTjwrU0n3U_75-f3O2A59ThUIe_TKvLt-cSpMM_7YrZtj6CxXHd1pxCeltqK1hOk5p6oW__uOHFV_hgg3gMjAn8J185c_OqfoBYl7nhuGYYv3WJyP-VYlvU-5V7Tq5uWtERUXvdLOXWnEpKcssdzMSmV1iienWbc7Vpx6nBXAq0S2d_UpjywEMGcOkMbv-3zkxAZcKpWLy7dOjwC-ZzC1IQxfgUXrMBA-QC85DKzehuxEpWX-5-AALwqeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24953" target="_blank">📅 18:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24952">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-WmUmdg286_cJooLu7PatmI6avX0lonYjxr-_t_35Tn73TXZkuUjAnEMdrSPgIJtSUFI3-J2mC9bMWJu0odXhxqjbA9r8bXOUH-5h16aTggo80FpqzOV0WVALqlI5_H8fWaehGA8ERLLMhn1asit6qlXBb4iN4xFmok_wqfpnYcg2MloEOxpPXsJuhiI7BZguPE4iwZUsy66nWqZhBZJFCpT43GAk9Ik3_69xwx04sxbAjCx1SitM0QW58AdPtL0ini3FdZL23SA23rC-Kan5kROgSMu7khayRr84x2acn8usw0fi6oksEMtaLWsTMboLYoVDu9NdaHvNhPkQcZEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وزینیا ۴۰ ساله در جام‌جهانی ۲۰۲۶: ‏۴ بازی، ‏۲۳ شوت مهارشده،۱۸سیو، ‏۷۸.۳٪ درصد سیو؛ مردی که ۲۵ سالگی وارد فوتبال شد و از رانندگی اتوبوس و برقکاری رسید بدرخشش مقابل‌آرژانتین و اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24952" target="_blank">📅 18:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24951">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tSo3WN7yzIfck_C1kuwYcswms7lJre8YEFYlAXloPOBzC5zRG1iWxxGPCCcc9WlRiPFrJNCv9zIG5sLSVUShjPZEnJSEShoea6vtahK6_fRAdxKwTfsIWIhGD4NS4MP5sC1JbxEeKZIdccJ-tRuLF2JfC8P4P6_spc6XOxUJSsR6-Uv-pXuaULyLIdC6Whus7sGvPlNidqZ61809GnqaGCQNN0A7KVIfMbxUv2ctglDtXQia-yG-zr_hkZecfZCtHAyaB5itGos2hUmOVDT-uS2oicD6EfH2Cl9T1SFfoTIM_BOft0owechezM8yUixpapvgFBdYMFarNNq43VxZng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا
؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24951" target="_blank">📅 17:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24950">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPmU4iosfckwTQpg9MkMbA2IleHBvsPcDEs4LBbd-K3wOgq7NrINh6AKmThnW0hCzZdM4O-B6stXs__nx4mhcXRrUx7k3NVoVgBn2YryLrpjtahaEeb8eP1T56PbMN1R9XPeP56vNZ__80nonsZYHRVw5ooGUzK6934aE6bueqWbCPfy9rRTjgOQPv_bpkm_AMmmvt9DoHGqY9enxIW4nfYQ2zhkkD6VGnhQea8b5YThFkrMGFYVKT43jqx16aLtbf4oedDCOEvXv0NbGPH-zvxIDAH7ki5UYmGolj1Y91XBesA5JoqqkV5i2EN5deEAG53xGIOah1AdDDfC3derwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌دوگزینه‌داخلی برای سکان هدایت سرخ‌ ها در فصل جدید مدنظر داره که سعی میکنیم اطلاعات دقیق و کامل درباره این دو گزینه بدست بیاریم و امشب یا فردا شب بهش بپردازیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24950" target="_blank">📅 17:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24949">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxRy2aWfiosgiC0Ea6pJaUOH1z1vddU0yNvUSPNTeWOh_gdiiYDdljrekMbcwWTYkAJUwwo5If1cDI47g8f5ZrWvuC3AaWfTAEtSsqqXqCMLfSsOA5lf57JRUeZmOhW9CM9Io8ZaETniH996dsGieyFw-AigWSil1bvln5TBgZqQhvKFHcDKwZoWOhbtWF_xwDMZIG0nQF8tbPILIvojJykLKn43kzNUrKgJkK8lok7I-4KxD1NVB5uUk6TQpF7O5oOPNnBTP7hBq7-PG4xPss5yldD5_VIix7Glq2mnYmZXmTmNZTvRcFyszLbs582Y03eayPIxKHc-CXrwu74CXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وزینیا ۴۰ ساله در جام‌جهانی ۲۰۲۶: ‏۴ بازی، ‏۲۳ شوت مهارشده،۱۸سیو، ‏۷۸.۳٪ درصد سیو؛ مردی که ۲۵ سالگی وارد فوتبال شد و از رانندگی اتوبوس و برقکاری رسید بدرخشش مقابل‌آرژانتین و اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24949" target="_blank">📅 17:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24948">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnS5x17foUZDgsOK8QlKiU0kEwb1zj0RrcOm7DjAqkklPzFoEtezHAf3ZcBzi99BxaR7fqf9lalMAJb_wyn1viCMJEAjCO2Dd8BTmeH6gK-e5NBDz_ajChmyL21rWj3-OECup69EoyTktbst3Yw_8Bsaregdqf6enwoQsjazi1uTNYOYc5rgT1LBIOJKeNp0moduFUTH0WKvfNI3v9CQF7LAdxN-a3h1wSKvMuDC9Rh6zlJvFYxFqXBTk53gpJ8URSDNvNoXC7qt12KYopiVJAKMdFhYCLZj5MFqUb6dbiWjqliX1RexEU6C0jHAtSg72J76i_3EFhIlBj71YiOlSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
15 تا سیو مقابل ستارگان اسپانیا و آرژانتین در جام جهانی سرنوشت یک بازیکن 40 ساله که تا قبل از جام جهانی تنها 50 هزار فالور داشت رو تغییر داد و به رکورد خارق العاده 20 میلیون فالور رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24948" target="_blank">📅 16:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24946">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rOV1nlr54NAOeiHiaC1rdBwL8vhc8Mlx-ZEckWtqFgtQb9sBR0odf1KiehcaJcTNQol44b8FrutN0C5C3prHhhIU81-xjNf0E8HK0flWZY9r_iMI3zKNF3PbR1JJfz9MQOy13cdNNK-N7lgz6Zknuxj0Chyk5bi-YVxcGvxcopmkmusA30jHY6UZtZWZ3-au3_FAk3xGPwL5-Tkb81KhDxuRBrDnf9Ul3jebAf5Gbx_-6CW8S5NNBZnOuX3JG3GoAaaWHmDmwuVcs09gy1elCNd6q6daTgrf_iy6TiCYbS3ASrXhS86hpg_yBrv7JjBfNZC4-zIIp5UbkT9soDkjWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/soDTPVQDBL0YK0UrQGf5wkj9l6xejYmKm4NwWh-r2dcJJwzAFH22u5ZYr8Ep7xjpRP9h9WvhobeMCywVqIaozu_BtHrsZxNkPJrCrW1bLZkLHN4aOWmFhftJLp92ewlu6RWP9i8gwYARTquXhFiChwyHgAl14eO_mv7yY0uyg10N4J1SEWF88to-fj9L36OeacT-XsXt0x3hdtLEbW2RKoAuFm1pWkghBbVGFRLL8-MVJIWlyUJkLSBnajeZKKh9_uNtP5sKqZ-BOgj1XpiRtaQ_IS8m60GaH3tccfFNQxxy5wOrM3hM4tAVI7CehsWEEPncKsxZ0fUNoZW-J29avw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
هوادار تیم ملی الجزایر که علاقه زیادی به لیونل مسی و آرژانتین‌داره‌ودوس‌داره این تیم قهرمان شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24946" target="_blank">📅 16:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24945">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZKWbvH-L_IPHXs00HBdaXEc63PGQCd5UsILUmHLVdOQ2ZQO20msSx9LleoWRBLVWccMVKteRIJqpZjdkPCTYeWs_h7T318ZMLpRsIwAo9nJ1rpV1Tq5DD3j0L6IvYBjJBxhUVfCY6O-Ioc_Eda02ztCPlt6ZhgPl1uEX9sn4vU17zazZKyC_Xd5wq5DxAff_OoujgJHZi_O53MOZ24KkGUNratbJa34H-8hzHk9wEoXW-YcO3ovuTYCVhAGL7JFm3CNbrNTCI_HR5feia5i_EsZXKnzfESs6dcm-HUO09jAgX2ncO4TdfRTC66DmYzEgd12r8KtrAutZvWfOX5eXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
مقایسه تعداد گل‌های لیونل مسی با پیراهن تیم‌ملی آرژانتین در دو جام جهانی 2022 و 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24945" target="_blank">📅 16:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24944">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qq4VPisiGs5RR_qWpUj4O_lIEouZjKUGK0-Ax2MhzpIPek5kAE2sw6QhhVy7Hbn4KM-uXXwsWa-6AT9aNkUv9TkjYybp4wHPAisPx-8KQp4t3YbrB5wap9RZI_J7eRECpZlq4iY2PMF9EdjWJ-BYyyPCTuhdRbdmIsBRFHR68l3NBlFeRzBHjWEoTwg-YmLw9DEpsOtRS8Qcm1e4h5fzKVItM3VlBP86WOfpwnfMflfE4Psnvhc61Ez-iX0L1FFoAW8nUtF14tscPoRex34c3aILuDVZ5zni2h1qocTVE3fyCSXQFOkrsyWBI5TkxNKRV_X-qqGFWKQt89moan8VLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24944" target="_blank">📅 15:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24942">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOEVVMQFkJ3f8uIQddJWrOPR5TrL-vo23Aot9HcgqgJMjEOdlxccHIyfPFXFblvbIcn9APChLdQ4LGNBPgfIYiABgpSJ9F-h25eX27o3QAi83PpeYvZNoi9VPkV4KepK9BqsCVWXHMc8X3m7kaOOb7K-4uiJ_2LRZ4GIZtaJ0ozBv9cGySATi3Q1kUcSkPY2JqNkImMLx4ClH5PR-a8Azc7VQGmis6vDwOCX3u19tOaaF_O4sEKg8dZxd17B1fLknkP4wgPoXbokoK-jCPq013n2u3noMffxeQcO5_TjZPtvKSyDLaPXODNIv37nTTdg-2tGNCop7M00J5wyp2C8-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#نقل‌وانتقالات
|امیرحسین جلالی‌وند وینگر جوان فصل گذشته باشگاه استقلال خوزستان با عقد قراردادی به‌مدت ۳ فصل به باشگاه سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24942" target="_blank">📅 15:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24941">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejjR8KmeD9QxSDcg3D32hAmqATswLSytytuWZ02v9cF7EjcqTvYK-llg8ywl3TadooJGAAGi2-H_4dGGpCnIZ0JcfqiOkV9wex6_FBLeyqr2PDgZs-zgZgi2d-f7SF3qyh1Xf_rs-7b-Wy6jcfnVQ9o9eTfjW-MiKI0ivrMzmAe5hSxvQzV4eGLSK9MrcHBDqZ-gpZ07x8iYjplRhag12TBGbBF8hHmybN8hmbSwPXL7VF5AvHSdFG4dxpR96dQKwz5ooS1G9a20rqoaAUkjuGQhudPfmHAzHbl4nah3GCqJ4qyoZ2tt8LSl65GKlRUIwkdRVt69VC4qQWyDsGAMXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مقایسه تیم های حاضر در ⅛ جام جهانی 2026 با تیم های حاضر در ⅛ نهایی جام جهانی 2022
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24941" target="_blank">📅 15:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24940">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJ2AVPrtOvWGswWDe9bOlhrTywd97EmPNduteCgg7vW0Az7J15MQUq-f6MfyuagpIwgK9QHmnxDz9cJB_DGLwk10kdMp4JO4fWiJmP0q2XU-DmVrf9XIcof0EbXu6XZXC9jt5N9Znj8wug4AOBGVCOPwtBmup3fDZBovcu8xuOPpSplnUqnmyS0ApnAA_UFrEKz8U_rh_2ASpCE8JH_5RhcKMwTkcc0GWiHkbC44HwyB2zj8kN8JxibKHxE2FXj873FIhymxLru8WJvqs71KZg_8QaFOUxpacvUl49oOfxeN8I3GPFqUZzsSVjBcvphTX9eNpJ8rk8W8jP_BqEgk7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
همه از عملکرد نه چندان درخشان بازیکنان تیم بارسلونا تو تیم‌ملی‌درجام‌جهانی2026 حرف میزنن ولی کسی از این حرف نمیزنه که این نبوغ فلیک رو نشون میده که با این بازیکنان تو دو سال اخیر ۵ تا جام‌برده و تو سال اولشم تا نیمه نهایی چمپ رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24940" target="_blank">📅 15:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24939">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fU499nIgXIHoxoqXO5Wa49KTyFxso7HkxwaKq1wq2i73IOJHlXYoEmqslAjMQdgn5qDHyJtlpeFAHJWEyQHi7LBJIf4QyPlzkbTglRzlY7NMP5Hqa0TDA2Upxxbu3_Fyx4cfdTITblAg-8_oywEfhBUp8-57ZTJP8DRncLP4YaYvkZ6ZCtITx4plaBxVRhxqtm3cH-JLQf6l6h3Lm0z6zcGmjJdLxZWYr3_P_WeU4OQqscwa6UlUKQw4oHShIVmEvHe6jmXwuUluLthrKs7jyNA6BMbx4B0leylxWQio-NRQbLaTTCGhZpfjlpKPABD7AjB089xdftCwB0cPkn3aqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
در بازی کیپ‌ورد
🆚
آرژانتین؛ لوپز با یک شلیک باورنکردنی دروازه‌ی‌آرژانتین رو در دقیقه‌ی 103 باز کرد و بااین‌گل‌دوباره نتیجه‌ی بازی به تساوی کشیده شد، ولی آرژانتین‌ها در دقیقه‌ 111 گل پیروزی بازی رو به ثمر رسوندن و به مرحله‌ی ⅛ صعود کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24939" target="_blank">📅 14:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24937">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LeFKsKXSfvDPHaJxqdopy6No1M444SWWrNSM1SBp-OO9LUB6--INzcmrNKKg1pI-AD4THzVvRqseEqYj3aNeiLLpIReR7aWg_umRVZ7Xgeq9HldLG7OgCDu8O7Gx62LJflIz_Scy_MTwesbYUhw3zsJQ82aoFHk9oigQyWL6drSKLvBT3TJljql-Z_b9ZThBdhEEiJG1UkIjpLhn7w2GE4nx_NUdoKePOc_al8i1P1t7dasdp79_fqS7dXwAXgLAJGpDj8hArGiaeiyoPP1IHV1kBu3hyOKiEo8US5xfMvdS6FUIwvbb5E4RD01m8_-oGNsETgRk9C5s_V_bByqH7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qi-GHpMTiiZPufGI53Bv6TUpSFs82DUrBRO0XCYhE3c9IrBH7jCmwfo7KvMu9aYoJAcvf2VI9TQKpI-Wc1wKZC5a4v8IsDClIMFCglKTcHoWSPs0QElniR-_PL_FOIu06WO85bNO6Nve0Fx9AnTVZwRcRAGISPOAiR_cShH1ejCyxyFs838yHKBGCu_DTXkAcqSOIhLwOXMhPqY8ZZI2QzCZ0lqzoZNRRdVDf71dwl7zhQfYNynn-qwuZp7hPJZrmTAZWKOQvWUKNwvrr19zQOjoDKrKYMI44Do7zehyh4JlEfSjrH6hbOBuhUY_Uk9_rnh07Dbld3w8ojSl4m3-BQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
احتمال صعود هر تیم به مرحله یک چهارم طبق میزان شرطبندی ها تو سایت پلی‌مارکت:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24937" target="_blank">📅 13:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24936">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bbb73e166.mp4?token=JaVGH0aw7Nk4jRMoXyGkO0D-pNEhSu3CLbWEh9j3xr4YjE_3nrwTRx4M_qC1BmcQdMo4lwVcUA4P85C8S963sFCaHL-qblolHgpEZpBQ1sU_i1Z6jhvptEtQZbyfweIvQkgpiLwM7NArAyMCfGukASdotLZ4DfIzoVdWzAfwzbWyn_hMHxhGoSGG3dJH-1JgNRBexl-tc3yQqzk3-KgTUCr77DGmR8vda7htCuewMqmfnwOVph33gJlauyHeJF-mPNSsanQaRJzhwuSXuwEclSfQ62oCa_O1BKTDicsNcpXji_K678P8EmDJW-DabKrk1IuEDqU3qfT2GLcsiGbf9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bbb73e166.mp4?token=JaVGH0aw7Nk4jRMoXyGkO0D-pNEhSu3CLbWEh9j3xr4YjE_3nrwTRx4M_qC1BmcQdMo4lwVcUA4P85C8S963sFCaHL-qblolHgpEZpBQ1sU_i1Z6jhvptEtQZbyfweIvQkgpiLwM7NArAyMCfGukASdotLZ4DfIzoVdWzAfwzbWyn_hMHxhGoSGG3dJH-1JgNRBexl-tc3yQqzk3-KgTUCr77DGmR8vda7htCuewMqmfnwOVph33gJlauyHeJF-mPNSsanQaRJzhwuSXuwEclSfQ62oCa_O1BKTDicsNcpXji_K678P8EmDJW-DabKrk1IuEDqU3qfT2GLcsiGbf9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24936" target="_blank">📅 13:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24935">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EiFvRmKeWyQgBLnI1lNS0hDBC9e70ZRehfoNfDXL04PILZjZTNeO1owBRCumuzq_e4LkYKV1kB1mzjY9g9nov-tfjG2gnMqhMVfEntzX1Ow1tMLiWXICvjYf5blT0qnwjLga3F4mllxNhdb2Degt8KRVXTkUKtjCP16BBVX8FKfKvg5QbzOdUn1fmMo23UvHjabW974OiWWhUzyV_fp05X3QP84vEsR6EJF3JvWxWVDqD2jaNzO-j_Rs2lIC3cfGggWi87bHnVNYVbeZIMVn8ezOTtmYnj9VMvyPV8RyC00I4TfPJ2lJY9WD1mZNvSnLsL2mHbeKfWAnZcEBwilGnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
دیگه با استوری که‌شخص دراگان اسکوچیچ گذاشت همه‌چی‌برای رفقا مشخص شد که اسکوچیچ دریکقدمی رونمایی با پیراهن پرسپولیس بود و هیچ درخواست جدیدی نداشت اما اختلافات بین مدیران بانک شه  باعث برهم خوردن این انتقال شد.
‼️
کانال مردمی پرشیانا هیچوقت خبر رو از روی…</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24935" target="_blank">📅 13:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24934">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2N_ALIaREpI9Reso6DdYLfF3Zoyh1sx8a5ZDNBYw95zYVE6Wld_coCu9bm1ozsM1-tkrNvi67OgeF5Ih_UzxLsxdURqPWwNUYQq_imO02tZ_RKsFJc27A_-vSRKr7-B7YqnjBRqyxQLlLOF6mXzylgt3A336r_R4dWPv0R7MzBYIzRf8FlyoFyD8Ju2Jr5FvAf235AHYbqWCe78jyccguSbA5JL6FetSg5cWsVPC-krKe1Oe4YyIYL7lZcZLinOEikTEHjBeX9a2P8oa1BjhPNAGM5OE2hcA76xll2BIQfGX5FhwzI8fMEuCVFP0gD1RIBAbuN21rxdEySOh7uGAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کی‌از مدیران بانک شهر از این اقدام پیمان حدادی دلخورشده</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24934" target="_blank">📅 13:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24933">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OaiVEx03J9FhPNFB_TzkzcKs2CHv_as9RsYdagW-PJrQDWDbaACTtpvmlqT5WDg9wn_psyEmAdKySwYqPtd6ZzTK5dQ4QjIf_IkNDS0qE193uvJpibCnYa5IGp0sYBCcQUwXm4KXI9Sk53-dkU6XosasXonqfkFpZ9RYa0cjinJiSWsl94dAu_S8MMwAqhQlgFWoo582g1mENakU8oT5bBfMNpm3q1Fj7tFRL4ZGHxhC3Uw0uJQOwmg4qwrAClW2dLq8JSmdvpVQEZ9pDp_o14kSO6i0kkbKF9c5I8W2NpPEdeJdnqwg1vXldg_QUoiaZp6InG6z4Ev3TK3ejxl1iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دراگان اسکوچیچ: مدیریت‌ تیم پرسپولیس به شان‌وشخصیت بنده توهین‌کرد. تو عمرم ندیده بودم مدیران یک باشگاهی این‌چنینی با گزینه سرمربیگری خود برخورد‌کنند. اگر شرایط مهیا شود روزی دوباره بعنوان سرمربی یک باشگاه بزرگ به ایران برمیگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24933" target="_blank">📅 13:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24932">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9iX4uImYElAtMpBXvWtkQce3Tb5fQ6S97I_7rbmdrUQPzYrzy5MqchlkvtRkHJYPz2cXNh0z2zeNaBond1jnSw4yPFrMJK7u5r8EIuyyYxRq-1-WzVzKxsgxH0xGFRa-9HaPa8rxtSpw4Mm3DdzPl1QjdwLg1zI5PkIoGGp64cFlVSxZLNnbL1VonY4XblHBkOEyNsm7JJoHzKXlI5xN5lDFcpCara_iTupsbx4SXWIDGTohZVGfeY0Z75xxHgvmGsqQmGu68XSafEqv4WBQFBAOJ-YdfKiywtqpcexZLM2Mq-hxmPFwiZzyKJhcE0uYltSDm3rOHRVPa5wD9ZWSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کادرفنی‌ مصر برای‌ضربات‌پنالتی پنالتیای کیلیان امباپه در رئال مادرید رو به بازیکناش نشون میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24932" target="_blank">📅 12:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24931">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AnMbWQ5dOheQdK-PMPrFEbY1u8_DVYX2OXA4bKAIcz1BidkvO_5Jwm0MPEqoVgtHj7BYz_OuSskI0v7Uhf6RNJtPsIwsdwZ19XnXlD_WfKFVtI9fhwNSnIBD82pI1YYdAt3yretsUKzp3RE68rJgRR9WyM0KmpLRMTgQwGG1cnyd757iaObY54g7R9fJLByHAyRx7iwEPSIxgc9-30vBLOPEos-3U0uTZq1bqMoH69MvG_8oJdOC5lfhlIBMmlm4gAKKlblJmXhuLTVsKcAuejr0TGrz8vO5MkSDaer63bBswQ8_zomdlMHZEMQqznZ2wP0jYd25-38aJUGVAf1MqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
روبن‌نوس:
هنوز با ژوتا صحبت‌میکنم، چیزی که افراد کمی از آن‌باخبرند. ما یک گروه واتس‌اپ داریم که من همسرم دبورا و همسر دیگو روته کاردوسو در آن هستیم و همچنان در آنجابااو گفتگو می‌کنیم. هر زمان که اتفاق خاصی رخ میدهد من چت‌های آرشیو شده‌مان را باز می‌کنم و برایش پیام می‌فرستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24931" target="_blank">📅 12:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24929">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cfc13f85d.mp4?token=KXRjF4RwJr7q_kI2EMCJQsiSK8Q876MQdQ8RQyFI0ouCgcmsIgLrIRv_AyYbv0w2IIwTxqbQeQCWhmQPO6YF6BMHCA-9gq4jJrbK2DzKzxoqjfSIpfqhUwhPPRPm-1Bnmisufvcqlx0xnuMOK6pd9YGvyILnBcqiziqqVbQ1SXnKmNfBRSvu56BbLGAugbR40fKOldS-8mvOVehLsulf47z6kmrcQ4wE1PvWzCPq048RGtcJ7Qxi6DTJcmLwaZGj25Oh6nMuQ07uvFEhsVsytFQC5Y5Qf2HRRETp0rZaCH-nNng_g2cvLBCpPEcLX0hfa0SLX1-QRZRuE9Lw87fd4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cfc13f85d.mp4?token=KXRjF4RwJr7q_kI2EMCJQsiSK8Q876MQdQ8RQyFI0ouCgcmsIgLrIRv_AyYbv0w2IIwTxqbQeQCWhmQPO6YF6BMHCA-9gq4jJrbK2DzKzxoqjfSIpfqhUwhPPRPm-1Bnmisufvcqlx0xnuMOK6pd9YGvyILnBcqiziqqVbQ1SXnKmNfBRSvu56BbLGAugbR40fKOldS-8mvOVehLsulf47z6kmrcQ4wE1PvWzCPq048RGtcJ7Qxi6DTJcmLwaZGj25Oh6nMuQ07uvFEhsVsytFQC5Y5Qf2HRRETp0rZaCH-nNng_g2cvLBCpPEcLX0hfa0SLX1-QRZRuE9Lw87fd4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇪🇬
در اقدامی جالب توجه؛ مربی مصر قبل از ضربات پنالتی، خلاصه بازی‌های رئال مادرید رو برای تیمش پخش ‌کرد. مصری‌ها این دیدار رو بردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24929" target="_blank">📅 12:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24928">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c33bd6932.mp4?token=nAB045fmFjzlWN8OxrtP1Q4_fEHhwChZ6HaPcAWrbckS-k8QAK6-NGtTHCuFm8GLJbD1R6JMpzwREjnvu3c-WdOHDDUGEkPxkDAvdw4lNzgIbeQv6gudtG1P_ycc7DzrKuYG-J_K8z_ThY1NHzzHUp3kRpFZ9nxNAtpzHEOp3fZ9riuSo2LGzfheDZaHiJTXAIsNAgcEqIPKQ9LoaZqSuEBxx6S6u1l4I9qHrLz6uG3TE1YioA0meYWlMZq_tMKOLEzTQ9oOxYeBvcv8c98gqLL4Sa8K0Gc0TrRRHdpMD3X5jqqYNPUlIgKHaKh3Jnuf0U1Uyyxz9th_KeI5xvklTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c33bd6932.mp4?token=nAB045fmFjzlWN8OxrtP1Q4_fEHhwChZ6HaPcAWrbckS-k8QAK6-NGtTHCuFm8GLJbD1R6JMpzwREjnvu3c-WdOHDDUGEkPxkDAvdw4lNzgIbeQv6gudtG1P_ycc7DzrKuYG-J_K8z_ThY1NHzzHUp3kRpFZ9nxNAtpzHEOp3fZ9riuSo2LGzfheDZaHiJTXAIsNAgcEqIPKQ9LoaZqSuEBxx6S6u1l4I9qHrLz6uG3TE1YioA0meYWlMZq_tMKOLEzTQ9oOxYeBvcv8c98gqLL4Sa8K0Gc0TrRRHdpMD3X5jqqYNPUlIgKHaKh3Jnuf0U1Uyyxz9th_KeI5xvklTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
در بازی کیپ‌ورد
🆚
آرژانتین؛
لوپز با یک شلیک باورنکردنی دروازه‌ی‌آرژانتین رو در دقیقه‌ی 103 باز کرد و بااین‌گل‌دوباره نتیجه‌ی بازی به تساوی کشیده شد، ولی آرژانتین‌ها در دقیقه‌ 111 گل پیروزی بازی رو به ثمر رسوندن و به مرحله‌ی ⅛ صعود کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24928" target="_blank">📅 12:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24927">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTMByOO5YS1stfeqwMDZSQn7ySyd0YPAMe019LUMUibkL2-SW77IkeyI2XFDXLgOrmI4Uz8qDVpI1hJNdzBRODw3QdkeBwcpP-ZOKgR064q2UGYh97HMYt7yJpZCAWalHii753tgKvyOYTD4u4t4zFloQNyzjZJ0JlpVyfxuX56qYEahW-zj9eZK2hmicKoDJ0RJjihbK7SEl9_R80rtiqL6aqRuRr9UjaEZvnLTRMRdBfVkVz8TP0Dq_Ddpj118wsyk1OJPtRR8VnECY4--08DUz1GbcgXmj8TwgXnSeQQiTTA2mY0UjlzXc4MNMgQu0FyktSKqAZ4HV0PPqCt5CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
طبق اخبار جدید دریافتی رسانه پرشیانا؛
تیوی‌ بیفوما وینگر 34 ساله تیم پرسپولیس با باشگاه فولادخوزستان درحال انجام‌مذاکره‌است تا درصورت توافق نهایی شاگرد حمید مطهری در این تیم شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24927" target="_blank">📅 11:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24926">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAttYyzcemLm3v_pEcc6UNReIuyL4F4CDOF7aoRfxd1H1BMacduRm9BXoBxmAVvp0A_C8tfN-w4y08yRcTUaUkOfaEMOys7vhcNc7NoKidP3NdJNXRgqJxBio-rGJ_tPZICnZu1u2A9IlJs1EWSDFaFtWEU4tUr_MnjtQumgetzm2pppuFoq9bgfF-rRYFdiGgeCu2ckAGm5tbqzZ8diniWT6P5_asRKbW7nEVBJZZ6endey4wCspnCjt8fz8viZKPco1n6vf2iEk137clgKiUnWIFCXzuz1uaD1m50jvO0amoIREH3W2mATcpNHlwJPI_DPwZZU_WwUH280wFJHCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هوادار تیم ملی الجزایر که علاقه زیادی به لیونل مسی و آرژانتین‌داره‌ودوس‌داره این تیم قهرمان شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24926" target="_blank">📅 11:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24925">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZaeFnLyqMB3Eb2M-VlIJ-53PDLAKCGtgHrgooc2n9dEW9Z1HAQkdHUVkNhhclaJlDBJ7kAb2f1zCHp5z2TLVI50TSEFR8ZOQPmJB9bPHcePj9CattOri_o9IcJfoOWVM4g9uWGCMNfKY8gplruvlB7DdgnoIs-f0tZllaqZvqM6DvzlwxqJbsYWp0U9NjiNvAE2Nd6WY0HcQscm26pjmZFYMTxEla37ABsfherhiVqzSrY2k9yktNErNj5qqSuoThxv0KYxH02Ai0T8rWUSHdNA66d660Ftkv_oJ4B0XEnSp7ub6yOqc0lVENI0vdzbUEfBDMaNBeWtKy08rwEELg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌ملی مصر امشب با برتری سخت در ضربات پنالتی مقابل‌استرالیا؛ به‌یک‌هشتم نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24925" target="_blank">📅 11:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24924">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MelBet2.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/persiana_Soccer/24924" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🤝
اسپانسر رسمی جام جهانی
🔵
کاملترین برنامه موبایل
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24924" target="_blank">📅 11:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24923">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S5_fdzg8sthhi5SHHVEh9unntbU9Gh3l8oey38ziUruWKzM5OXHoowcR_lTyZr711UfYLNvx4cegGPYkcerl9gEaJPNTb8uzdYzNvXPJ39q4pWjc1PKv7Ti8ki1irsm1wWCbfumdhvgj0-2M4js_vKS_P5GBB5g5sjL5bp67G6QrT5XP-x7ZXpeqjCd4gZmDkBkMcpAX5Lea0asJ1w9fIpVNMfen2CS7GGuya0UvWROFFJL6EYNvcc3vbZHf4XNodiSS5E3gJaGBVRzGlQlBXF4_aJfw8i8bVau2XzTLkDgJFMAKjKboBV8IZ6LFclQkEPWKKgqPuwADnb2nwru0xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
55 درصد از علاقه‌مندان به فوتبال، فقط 4 سال یکبار شرط میبندن!
حالا چرا جام جهانی
❓
خیلی از نتایج تابلو و قابل حدسه
💯
مافیا که کارش دستکاری کردن نتایجه، زورش به جام‌جهانی نمیرسه و نتایج واقعیه
👀
به دلیل تعداد زیاد بازی ها، دستت بازه و کنترل ریسک و سرمایه آسونه!
🔽
🔼
💡
کافیه یه سایت معتبر پیدا کنی که شارژ کردنش آسون باشه و بدونی پولت امن میمونه، MelBet اسپانسر رسمی جام جهانی، همونیه که دنبالشی!
برای ورود به سایت فیلترشکن خود را خاموش کنید
🆕
Link
🔜
MelBet1.net
✅
🆕
Link
🔜
MelBet1.net
✅</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24923" target="_blank">📅 11:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24922">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONV7lIuh71yl4tNgfXjGtkHnH99CJE_yCmvuKaGyLAW2CMUAS9Cfo-hIgaAerl0QdHlIpaflfwjGAgTWJYA5sv8k6MGjqeVGn34HrzlEN3ZIIm4il5FvZeQ3ZfYNNKRVZCN-_dPgkOVx7lsyr4SU_QSBt2Kw6E-mM0iMb7aK0YdG8Oj4f1W_8nfhKm4sc_bG5c6Q49HDs8k-3G6sWxdiBotZ3s1ca-zMVlNlyylFm7qWihzTba6L7vBqS625DjYWxTGxjemNz_V1K9CtFAd0oskCqI_1aR0NgY3IxYo9c11N8RAKZPCXaG-KGQhQHgwwOkfRhZ-AGFqr2WK-LdYc7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل مسابقات مرحله یک شانزدهم نهایی جام جهانی؛ پیروزی سخت و نفس گیر یاران لیونل مسی مقابل کیپ ورد و صعود به یک هشتم نهایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24922" target="_blank">📅 11:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24921">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jqr6KVPM094z3ivqePXRbEMFTcq2ObjZIx6WIFKq5uPS46fnIn-rZ4lcVw8xx4Av1rvq8EQyWqgtHvdUvSD3OqmmyFqnC9a58RrPl50sHHpF8w0aIOfUUvT5tt2268ATeUBKKcJnzW3_8PYlXCwmBB-133Cw-YiGM0xAB87i4nJ_QwnpbMAqz_2_DHzL-q_zg4wjNOs8vSMYEZEVcthFXsuLD32vH4n9F9AegOCKFGa39sxNZBBQAryP98bY2XgfacgQZ_lSoRU3SrpE0TwEQVgWJUMUjCshQbi2ww2D-3dUTrm8WcPa0uTlwBTtdkOqNd7YMKy-hIEusQjulBegkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
طبق شنیده‌های رسانه پرشیانا؛ آلومینیوم رضایت نامه محمد خلیفه رو به 70 میلیارد تومان کاهش داده اما باشگاه استقلال قصد داره با 55 میلیارد تومان این دروازه‌بان جوان رو بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24921" target="_blank">📅 10:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24920">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqT8oovkSabbsVfuyTxOR8Nu-9fgBhXolRmX7feBrL2QTZrFkshHQLoMaJcG_RktUm7I0Dtx1NQyjLQHpGvwvN5Th1TYGdEANCznZIHwq3t6uQFmqZcEEpc5Xn_rHBvNXCbBorNmj5ybSQhP898q5HWiqCozc1hhHnAud5uo19uTm0niEDhPZM3kJyhVaxfB-zroHBiNEbp6S9jQVtIOXiB8JegiajPVHLRcQ0kJcxnotZpKY-6JOD9VbCtZ5hhfSpL0NB6R8bTDnLqjViTO6LWtRN7d7r059MdMit_7XalQDtk374UoMRKyK0XzB6Zb0iY1ki6zIm7vLyJN6Nq0iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24920" target="_blank">📅 10:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24918">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvFqmPzY39aGU3AjfqC86cze7-0yZPiHnTdunKC8hi2B7CICRCGtgWiCys7xmJ7O6W4uSTluNRptsKvQ_lB5IQtQhY3UbiuRk_AJxgZOsVZhCKuuZmzgpn4Zf_uVGtzNY9b4DcKY6oQHaeF7_Ae6ARZyegFH9QnKQue-mQEMEgjl1hcqMCdmUzvfeoad_7w6T84IEIQ-kIQfvrM0_ouPEr0UBTjCtWaBhe321U2xr4mEhAAkyuLvgqd8db3uJ0iHzePWwUvK0WQTZ9EAvvkZEIolY0VxSWPVMbiRrgyKjV4lr9N4Xvf_rxcOm7DMRwsNJyu4-kWJ10mxYyZJrkYZpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
8 سیو دیدنی وزینیا گلر کیپ ورد در بازی مقابل آرژانتین؛ پبجش از 18 میلیون به 20 میلیون رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24918" target="_blank">📅 09:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24917">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef17610d75.mp4?token=ukBJl5Mmxl2PHO05fhfjSItyNngg1EOhTr_gm4fahcNxNCBGC0wmDfa1x1C1O9bc0UTRqvrJjKIFkNxoJ6V7QINF22kDwYCAn1rFqmgWouboySp-GMKDwloqhNn-z25kc0CQxFMzTmzizzrg5iMHjfm_dqbMkVAG42ZxwhjOoMlog3H-tl-JokBXYMBzarab_U6keWdGUtdEV5rjIDQ9zX5usdNj65STwvyq-Xe3WwP6TqXJRuPWL2k8H5pyvFNpJqGzwTLNSi1iXQ7tc1Bej-1Kvk7Vc5BxBoR8y6AxhmfQPut-RVgb0usp6KTtU24iChIY-DIAqHbgIWcoWiYN2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef17610d75.mp4?token=ukBJl5Mmxl2PHO05fhfjSItyNngg1EOhTr_gm4fahcNxNCBGC0wmDfa1x1C1O9bc0UTRqvrJjKIFkNxoJ6V7QINF22kDwYCAn1rFqmgWouboySp-GMKDwloqhNn-z25kc0CQxFMzTmzizzrg5iMHjfm_dqbMkVAG42ZxwhjOoMlog3H-tl-JokBXYMBzarab_U6keWdGUtdEV5rjIDQ9zX5usdNj65STwvyq-Xe3WwP6TqXJRuPWL2k8H5pyvFNpJqGzwTLNSi1iXQ7tc1Bej-1Kvk7Vc5BxBoR8y6AxhmfQPut-RVgb0usp6KTtU24iChIY-DIAqHbgIWcoWiYN2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
هوادار تیم ملی الجزایر که علاقه زیادی به لیونل مسی و آرژانتین‌داره‌ودوس‌داره این تیم قهرمان شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24917" target="_blank">📅 09:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24916">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbvUgXO0fLhY2E6QACO4B_Jg81ZGtBKEQLYWEXYxzNOFINkZVxzyMXcNNILivNP5vui4t9I2Iw2hQ8z7ChiM0yYCFUNajIXLej7a7qgezcI0q0ECFhJcH_xJLthjihe31t8gGKm5p1aPqHrYuDK4d8eO2kTRWZtjJkSIQFJ5WAdeMyqsYIttCs9pefxm4TFsh2AbqcH2LCGDxZ_TtrgDWVkoeWyufiv7lCFX5i01ANZOcYVpOAQyy1ImQN_9O2Sog0uF7E81c3vgnjz74BdxUy7eoTgwSk78PFARJt6yQsXuRxBigk8NbrM2YxwpyqLMwL9n51-utq51otAQIaccQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مسابقات ⅛ نهایی جام جهانی مشخص شدند؛ لیونل مسی و یارانش به صلاح خوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24916" target="_blank">📅 09:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24915">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ch09otTrs-ZrUkoAAgH5qSYFfrAhHiG1lbxlPfFKmr8Y-AlTLewPfGHshJ6GjoKazR_dZjKI81TkqZhGGStCpP2-reaCJ6CAdlCMA9YvtpV8OMsZTF1nYgMvyZ6-FsWf_m3K-t8AHluDMEurwb8TD2Bb1bbEY3bGTvHhE-KW6xuDCo_P14ho2gxXjklfi6__osZa_YfA-2VrIKMl7SMnCoYUBRhOykrVdnUOhVLZyj5CgMvHG2Xgm442U6Qev7KBzNt97UR3rMiV8ddfObsTUZEsF_ePH0lfb83jYArXEPFM_LRoLBbpEqcsO54kOA5RIyTYr0wHMc48SuQPWLt9MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ کارلوس کی‌ روش در بخش دیگه‌ ای که از مصاحبه‌ اش به تعریف و تمجید از مردم ایران پرداخته و گفته من حدود 12 سال اونجا بودم. اگه روزی ازباشگاه‌های‌ایران‌پیشنهاد رسمی‌ دریافت‌ کنم ممکن است به‌آن‌پاسخ‌مثبت بدهم. من برنامه‌ای برای بازنشستگی ندارم و علاقه…</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24915" target="_blank">📅 09:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24914">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/579197cdd6.mp4?token=Uwl9w5tYO6Pt98GRT4qNiC4Xqz2peKFu0GTx0_3BaT4OC_iqkwuF6QjBCWVYKOFBTu_FWpKGdjf-14I-id1IWj9g_SPXNr1IhZ3UubejGAHV7MRitJ0i0gVFdP0IJORJs0OMDScuccWVuMNcPgNqJIx6BDnIYqx8VCkgoxyTI43u6nsIlN8CadINb9AgmRFy0T6G0fy75zAAabeuk9wuqg3VHoohOGgpJ-2NVTyXt5FlZ-ks8-L2q8RACtiXJ1nVD7hAOrrAUlgvveyiaJqiB2vcfqGgf5CYJ1nRZ_ITnLFt7iQaQeMxjMeZmwDALGs15f4hciOTMndMAKQuXoKdwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/579197cdd6.mp4?token=Uwl9w5tYO6Pt98GRT4qNiC4Xqz2peKFu0GTx0_3BaT4OC_iqkwuF6QjBCWVYKOFBTu_FWpKGdjf-14I-id1IWj9g_SPXNr1IhZ3UubejGAHV7MRitJ0i0gVFdP0IJORJs0OMDScuccWVuMNcPgNqJIx6BDnIYqx8VCkgoxyTI43u6nsIlN8CadINb9AgmRFy0T6G0fy75zAAabeuk9wuqg3VHoohOGgpJ-2NVTyXt5FlZ-ks8-L2q8RACtiXJ1nVD7hAOrrAUlgvveyiaJqiB2vcfqGgf5CYJ1nRZ_ITnLFt7iQaQeMxjMeZmwDALGs15f4hciOTMndMAKQuXoKdwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌سنگین‌وداغ هادی‌حجازی‌فر سوپر استار سینما و تلویزیون به میثاقی مجری صداوسیما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24914" target="_blank">📅 08:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24913">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34a4a83cf.mp4?token=RXkwkNCq1WCsPKkQ-Fz9e4JYoKmVPncrLzhgz2DMsLPUhxoOJToDiFiiDOLrmyk8lgrYP7R8LrSC2cFWF-GEoBJ8VfQuFMaN7mORML-gFdUXgoEV4ByRDwjzxsCfSdCEh95tk-dj_Leo5M3ETx9pQJNB7pkJDd8Q8kJ560LMT359aGwe2hjpXVNulVO6VoZ975lQI-ob5wc3-j3J_JSqNSUJrSEIRITwdOLy4DmFThAcbwgUIkwVv42fRmtBcDREI1QyK3hHG0_Y4c9zW-klfviInJzGIk1p0Qytkp-p9wFL9-9BOMxvKt3AtLOXOklyz4wspIja3f3cleh8-LDCxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34a4a83cf.mp4?token=RXkwkNCq1WCsPKkQ-Fz9e4JYoKmVPncrLzhgz2DMsLPUhxoOJToDiFiiDOLrmyk8lgrYP7R8LrSC2cFWF-GEoBJ8VfQuFMaN7mORML-gFdUXgoEV4ByRDwjzxsCfSdCEh95tk-dj_Leo5M3ETx9pQJNB7pkJDd8Q8kJ560LMT359aGwe2hjpXVNulVO6VoZ975lQI-ob5wc3-j3J_JSqNSUJrSEIRITwdOLy4DmFThAcbwgUIkwVv42fRmtBcDREI1QyK3hHG0_Y4c9zW-klfviInJzGIk1p0Qytkp-p9wFL9-9BOMxvKt3AtLOXOklyz4wspIja3f3cleh8-LDCxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
گل‌های‌دیداردیدنی‌بامداد امروز دوتیم آرژانتین - کیپ ورد درجام‌جهانی؛درسته‌حرفای جادوگر درست درنیومد ولی‌کیپ‌ورد 120 دقیقه بدجور این تیم رو اذیت کردند تصورهمه قبل بازی این بود که آرژانتین همون 90 دقیقه کار حریف رو با 3 4 گل تموم کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24913" target="_blank">📅 08:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24912">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
👤
خداداد عزیزی: بااسکوچیچ تفاهمنامه امضا کردند اما به یک باره همه چیز عوض شد و مدیران باشگاه پرسپولیس‌درخواست‌های جدیدی داشتند که درنهایت اسکوچیچ اعلام کرد با این شرایط نمی‌آیم.
‼️
دقیقا صبح گفتیم که باشگاه و بانک شهر بشدت دارند سنگ‌اندازی‌میتونن که اسکوچیچ…</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24912" target="_blank">📅 08:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24911">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0MVcMxSdJmgZZKxgvDywERKqjad47aTdaBb_qrMKixiwuItIjmXVYqnnm2Jfn9h2gPd-RpF-Cv4-zuKvab7Y9y75F4lts1mfB1m9v_O7vncfO9OH5FhQrCm_vmoQDTgOaFkGJiNmfCUx8kSfnuO8IJ5ArzkAQVe9nuy6obwSVOtotvDSo75qFM8mS7_Y3oGp_g9oH3sNATNM5Mcaue4vxN61s6jWwVhG9KmjffVDhzqfeYRqSGZOSHqxUTDc_1Mz3eyGydSFtpVq_FUb9wTBMH2spYxk6af0tz4c4j-sMVD-LHPpf1sLiNIQVqcq83qtbxQr_tYIXNSNb2GL_DXcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
دریک خواننده‌معروف‌کانادایی - آمریکا رفته پیش‌کریس‌رونالدو و بهش‌گفته‌روی‌قهرمانی این تیم در جام جهانی 5 میلیون یورو شرط بسته است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24911" target="_blank">📅 07:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24909">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24909" target="_blank">📅 07:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24908">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lV_thsLXBPxCer_kEu3vOFyAOvF-PaVfj_zxZOAZ5R9qx3pjiXW09uZbdzpeOmFOe3vOHHNI7GdURNYy16dyTAJOmsqUiIl2AkV6nzWvEVvC8peeQfwYkNDw6Z8PS_fRjvdrAqnDhdOQxpSx2q1WhCBc4j10Owq3n-HPyg1TI_Z-AlkYFzy0LD4d_C2YSSBtuJsWv_ItFfKv3o_uC5qVJihHridYsDTV3gHhrcdktP-YpQPt6sAZoIEuVbEmqFe8fMdDZpzUobAsNAyfxd4PlFaV7DQdj9PLp4KuIGvpPqTCS-VWdVJQkC26ffuPtlKigkL2L67GxR1DRRdnji2gtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل مسابقات مرحله یک شانزدهم نهایی جام جهانی؛ پیروزی سخت و نفس گیر یاران لیونل مسی مقابل کیپ ورد و صعود به یک هشتم نهایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24908" target="_blank">📅 07:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24907">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6T-nZcMYUOTg_pKz9TBrm0dNkM9Z6-fFVWoFG-XJD9RzSmfGOlAEbw42bRyFWkPFdlU81TnLDJkng3U3snJmUpmYDvQrkVkBn38xAk59-eI_NF1wr63TVhsDUshT14ST2ojA4fGgszxnm5fho19P_6cV8uHWYwJd-n3U3HA4rkbkDOcFRCv7_nLjIHouY-6gZe1Vtug9fmPHW9FN3u0egGDsvIUwQSjT_H8sDeJPHy8RFws-aaDl1KUnit5JrUCttt_gsrBWKRlfUEPFC_95OmuPiIAqt3hVEW0LygLYCFvUfmOJmUOU6uvFUXjV50DKX6hk2OhPYSEt2Y3_1y3Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24907" target="_blank">📅 07:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24906">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dllhHFX3Rue1JFM4Zo7c4aqIIcMb1Q8zFGAiEJ8YMvKMVmdrTn980vsNvLQxeOM-i5Hyu68NCaEhvoqUN68DdlG_lAf6oMR2zhiZJZIIzQO0NiqF0fFhk8B20xdl73E0JcJNDp2vD5yFdIjH3-7OEbL0V1o1uABP32KEb2ux0h81RHFZ1UieFuAQPd8W0mssUOL37u0y0Vv-8cVE5QvGSc-f2wsXtAvLFNXXXcLwXZfnxvs6KtQtURvsiBO7b4VGSvRtPCMN6l-S91SedRft-UsBsgEFGw_chXfv4dZnx8C0JmHwK495oD287KZAQeFDIunxYoJXTsoADoGYEDoEjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی درگفتگو با ESPN گفته شک ندارم که آرژانتین باتموم‌ ستاره‌هاش مقابل کیپ ورد غافل‌گیرمیشه و خیلی‌زود از جام 2026 کنار میره!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/24906" target="_blank">📅 03:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24905">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-ofFcykza0Mtj9FMdxCYkAd-4kDIXsL1_WqtDpSeimtzvYF6eB827ncDTThaHGTNhufxIU8lCZqcMu7M1NwsqYJZ_d_WNMNOoQq261y6cjRa8GKeWiTGhWjjLC7UbEYqL6tyeceQgqBgl8-KMsLC5vmm3OTZs9pwRoJV6ahmja-Kd9k4ExibNCIRUr0JbI4LfQDZb_v0p6rHhyy9-_84hk0gKGxGE0FDnve6SCafF75jA36ux4gvnyFUndVmaCphmQU91l5PcS3wJ5U4sAET3t9HQFCIwFWEn0HGsJ3uVGXrQSKFWZRJ2eHSEK2bmFJ_alBPibIrf43211lY3PW5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
گلزنی‌لیونل‌مسی دربازی امشب آرژانتین
🆚
کیپ ورد در یک شانزدهم نهایی جام جهانی؛ این 20 امین گل لئو در تاریخ رقابت‌های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/24905" target="_blank">📅 02:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24904">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0965bbee9.mp4?token=V9dtXDc6jIPl6AVT1wH1nx7TD2yJ57CyS2VdcdV236PU0VOrgq4r1ofrjcX6M6mMEzSukT9SmBjngddG9xfX8Eb1GK-ljPohRnm-Ax235noeHch6TwePHV1eaI3saGLkMdIR92xc7xoVeUX8gJKFf0IVj-nFwiVssx4lLFLGaD4L10Th7wFJaEhvY4Dms6e3RNq4w7BZbUTTBl2Q65k2hOvkr97YekiQ61SYGWJD4OHBsSAWU7rT9IIItmBz9fTMFWZgGUyu6PC5wPU-0LirwmdzM8Z6siVCdu8aXf9MnAANRXc8l1nGLPOrjvarJYFQeoofeVnpKZZtEJEOt4E1-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0965bbee9.mp4?token=V9dtXDc6jIPl6AVT1wH1nx7TD2yJ57CyS2VdcdV236PU0VOrgq4r1ofrjcX6M6mMEzSukT9SmBjngddG9xfX8Eb1GK-ljPohRnm-Ax235noeHch6TwePHV1eaI3saGLkMdIR92xc7xoVeUX8gJKFf0IVj-nFwiVssx4lLFLGaD4L10Th7wFJaEhvY4Dms6e3RNq4w7BZbUTTBl2Q65k2hOvkr97YekiQ61SYGWJD4OHBsSAWU7rT9IIItmBz9fTMFWZgGUyu6PC5wPU-0LirwmdzM8Z6siVCdu8aXf9MnAANRXc8l1nGLPOrjvarJYFQeoofeVnpKZZtEJEOt4E1-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌ شانزدهم جام جهانی؛ شماتیک ترکیب دو تیم آرژانتین
🆚
کیپ ورد؛ ساعت 01:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/24904" target="_blank">📅 02:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24903">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9zxOIxPhVQ21Idk89BAapTvJHN9-bKH8ZDzqjsQn4yCL3SkRvdclxisABqc8rXEy2GvJDic_1fTDmskBYUqQ2swADriMg8uOMHHI_dZgwkZ4mjTIXRH5E_n3G7KAOnudGJb0KgkW1FI57TRH3nvWF-Lqd3m0v2wBq5H2QFuSMaUtEECxXGa6nutDscccOM0RJP9KOUowiZlM3cXvYFCbrXLfd1xt-4bQE7onRKoN11wQS6wYQASvd4pUzrYksh88OUjgOk1cQMQ2-KJJPtwgxQ_NXg5fBxfI1MEEw_9u6deSAq7ZUf2RjnRz8bntJa1BSW7sKUxZJ2fEkOvDdsLVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/24903" target="_blank">📅 01:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24901">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5DO-yTPnb5lZHYh9g68J521jJyAryJ0lD4S8Dx8kpefYJc-pXNn07RhVc2OkRRVPRPSx8IwYvp31RGmVHaetLE_e-woc0vzxHAGmvVDbb5hmryqCvvvVfvHu-9TwmBsF4CG-rXtI_pZpUGMsKm88_GNZAh0jahF4mCDh6kSD1SWXQNQq3Mduxzya1ybJzml1CWz5E8awbDN3C1UE7k1PEdGT9hHVS9fKjtSbu-TiJIN6fROubkz88OZoZm19FdubVMXC4Ax7Rs3Kei3-GqMvQ2NEU3nR_xggTEx8APR-FC6-tL2h6TWhrjXc4VKtFqHMMUCIKS4Ex0DRq2aSHGhCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/24901" target="_blank">📅 01:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24900">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GxrydRb2xODvjwzxrXWyOiLThZ3OtcTZCOW5Nsd-8TyRovzl5_H-chZZX9JJmXrSuj3jFTX2EFZbGA5aa8FKgy7BLnFibngEW218YSwCLsO_wH83tL0kpOV6ZCYMuV4Cl7IAEz51xc5gO2BVmhsbIwTbibKi0VFEH_1xWx79t0C-73aFbvIGP-fFaDThNcf-VnWHMcbggNOZSNi3uLyvqlJjg00GAqgza_M2a2mC3NDIFd7dvggRJivMr1zRjHbmHWbgrkfQmp80ef76SCTyYgtoRwntdCs8cndcHdXbnKxUs6dvX2mSv4m8GbBz590C5cRAB6S9WPnx0vx7iPr57A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت: کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24900" target="_blank">📅 01:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24899">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTe5wN6PSBCroAJQ-tAD8kAxy-0_Rcv748bo7_V_sq-4CWjNl1HZGmYi7GYXseR_NJh89W6uKiLzirj5xjnwH4eaK2B0itG1ubJcnY1AB5onthu1un7LfLG5D5IWZpplNkf-SXZzrAOqB9w_ORauwoxOIWSxK63l8n6MjJgsks4vd9CLHzjs8-t6zOSs1TDADKbyfkekX-4yiYwiFKN_iThwLFqOmc0hPxCqaTDDZEEtFnhP1XUzo3V6GUs1nMhCvn0L-kROVtB3uq2UquiXY0k4-oeg_b0KFhzZOevhwlPt-c-5XNyvY5y9yt1w_Fu9_t92ZOJNpe0EOy4Nd0fk-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌کامل دیدارها‌ی‌‌ امروز؛
جدال یاران لیونل مسی مقابل پدیده جام‌جهانی 2026 و بلافاصله آغاز بازی‌های حساس دور یک‌هشتم نهایی از امشب
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/24899" target="_blank">📅 01:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24898">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fsj53mOMdXhQnc9XOA1QaaNM_CUjH33IJEet469BVphBWNO9PMG4Eq6bT3BCQD2-GePZ0yJY0NIboM7vkItgjQBSyoCLjrDpFO3R4F8382vPsg5KsZhRvoTH8qDG79licy81e8VqRJsch39Kdx2FXsxvIZgsabFRPiQtqKaPxKjpy9NUoGWk-TiGnxIG8QP1h_KHxqEUJvTJCKAD3Hdhc8sd15o1REAPWPzykMGhvClLNlpM39FQVZqPI1HNcSQbCZa5BB_KdkM9_qbMdoWQhF1--1s_yayrvIgiKLztAZjOJbJSZq2WUqhTCk2ND8FLfCc3eb1qp9ZwR3yAsj9pRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از برد دراماتیک پرتغالی‌‌ها درجدال برابر کرواسی تا راهیابی یاران ژاکا و محمد صلاح به دور بعد رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24898" target="_blank">📅 01:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24895">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXKQiy6aQq1GPz1LnaxF6u1hR_OO0LmAqorJrH99afC_IbBhAAVafeneDP0IkIqW2FNuwRHNOI0526SY4wlbRssid57fNLnmyzJp_gGngK0pJZygcP5kzkBQh2p6OhtEv0zPscdctgEtX3izlQHHaxsIfvw4OPC4p57oQjWTJyN2BcJsCFYhPgC_FJGQwSq3kRpheyhTisLNlz9w3LVlAp7OZ-m_Rpq0WHpcaSkAMsoTfsceG18xcIl40TuUqjPM66lAOGq89JQgJzojhfezN497oqpKbd1T3uGYsxv5_L1oSEnJxXwMn6MBHvbfSi9CD7Fh_LRvxEh7zKM2JKQe8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ دراگان اسکوچیچ حتی لیست ورودی و خروجی خود را آماده کرده و به نماینده و ایجنت ایرانی خود داده تا بلافاصله بعد از رونمایی بعنوان سرمربی فعالیت خود را در پرسپولیس اغاز کند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/24895" target="_blank">📅 00:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24894">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c8ce51440.mp4?token=EGFQX1MKKUOXwA_J8MJalZtDgvUVfnvxciD06UEQj12RVj-iNYFimXeH1XfdSl-mP5gxdzSeVr3WnZJbpfRmoJPjryYXxPYvKrVX9_qR7yVC0zJa8jCrlUgwEXAIA4ALiep7CFgKv4eBVDawgC4U2LmcyTNLwIS9wbZxRslOyvR8Fm4KwWnc26RGrRKklb7JDadFbmSCHjDCV9j7f7W5LKjNyV8sfLw725Iezo2Wk_eLSV-0kgysUjAv5BBCdFVW_r81RgaaZwuOA1GD1sPUb4J3pNfxVxtX3-SS4zN-yc0pGJSNtehYBYm48EW-hv79SLeiIvxxQ5zzjMXEi-WdAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c8ce51440.mp4?token=EGFQX1MKKUOXwA_J8MJalZtDgvUVfnvxciD06UEQj12RVj-iNYFimXeH1XfdSl-mP5gxdzSeVr3WnZJbpfRmoJPjryYXxPYvKrVX9_qR7yVC0zJa8jCrlUgwEXAIA4ALiep7CFgKv4eBVDawgC4U2LmcyTNLwIS9wbZxRslOyvR8Fm4KwWnc26RGrRKklb7JDadFbmSCHjDCV9j7f7W5LKjNyV8sfLw725Iezo2Wk_eLSV-0kgysUjAv5BBCdFVW_r81RgaaZwuOA1GD1sPUb4J3pNfxVxtX3-SS4zN-yc0pGJSNtehYBYm48EW-hv79SLeiIvxxQ5zzjMXEi-WdAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تیم‌ملی مصر امشب با برتری سخت در ضربات پنالتی مقابل‌استرالیا؛
به‌یک‌هشتم نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/24894" target="_blank">📅 00:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24892">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LoGYy-C4pk6Xm4NxHC9Qovk2XJWOUkFLVMKcLYMbuqMpx88CDYEFQp5OeP_7ACI42kMIJ2mUyxop7W3vp4bpfWNG2NS_OOrfstHM8sqxRMl4I-_04hWzh6K38JIZlqmCCMbVlC9asXL3rmItLxGk5w_jE_Yj2RtK7uEiOjhcqcmsQKArt7nCDlg8_sxL6Fg6j72ixlI4SzLChm_AcoZgy-Mae4FqFozSiWEhBfGEgxas3EHdIVZtnVbscDpkQFZpb4h4wpLuCl4DMmQWJT0O-tGKkqQJ9t1fnNKupmuozHipy76RxTGLDhsVu9pODF9YNebZPo6chnOc0sRvwaSD0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z4zlbnQUJBZYugFfdIS0ExUGn030Gp-TWiDPT2BD-f9TrOh4A-KhEc6gWGINcMwUAYB6KFBv256x6tQaEaezhf2EHej_1v03OshdhvifnfLzJp7TdeTb63LIRjcX7m68Pcox00aIdl8LwfAJjMQqrq3A9wVM4TVA-_GB4NdKTkR9LtK5CcrruTSxfQcf4szM3tc4fibc1ApYQSz8aVzjRMJD_2t7ofLJIdOQ6cVsxmbpy49x9d0XvCGU1HiFEkNe1sPgXM9Mn4EG-MwdxCg5aBTfu3Vnjb8VRXO2FfI9rSjFlkx2vk_8_JoeQMJSeTkRLaAJ_GyzjHZ8gIH76Rxjew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌ شانزدهم جام جهانی؛
شماتیک ترکیب دو تیم آرژانتین
🆚
کیپ ورد؛ ساعت 01:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/24892" target="_blank">📅 00:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24891">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSJmrg2T8SZ0STREMrmDj9uaTvJV7Hc4NVdgdDnztgR7lzdiKwaXMmKkOw3PjftunFs-yMOp_DrxBneGYiUdkLhVU4UM9HaUcCPcKPKK93gD5UixMiAJ_X1QgJqlmpiziIJuaX0pQ4-FQ8wOYGdlONDzT1jRicwYQSe1QtO-Ww6p9-N7g50coTbTTdWDL2H6cTAZXssBLqglSGkn07wR87Qg0Fu-1rtKqW1cFCsAg9kEq9xWFxdH-cGeWM28lCdj-21pPBRDhZQnt7525qkR7yqYBDeHOWZ0Fpx7MWl0-GCpZ8S7mu0uparqBm2rqeH57Z7iHSA3Ue0cc_BfvyzbwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هواداد تیم اسپانیا در جام جهانی 2026؛ لاروخا در یک هشتم به مصاف یاران کریس رونالدو میره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/24891" target="_blank">📅 00:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24890">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jldcOlVQVixTNgGQlEZNVxE-hOaiKI2N_ADA49Bu17VOjkZ5z195yfjX_DMz8hqB3AxUMvgM9Il6g_QOeHE_klC-3QC9k07LuSZAZKhl82YS0RwOe3x3rm1MdyDYewFFf4Z653tjYMg1q0mR3Dj5VWQj_jR7UtiIPuwNL60_Bqepd91aCqX45NCYpvGDNsHrJv_lqebxyq-s3p0VuIKhNbEdHB9tw1cQr9_Z61l7-slFFqWfo_jR9O8HKRE9SrkAO2Pax1MdBM4_tvZiWZ8zSw1ZHuQiKUwfgAa7RdTj7fAoOXZ9dOgrwF8FUjBlOtb9Y-ceGQaH2N5RUkCCisZH0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌استقلال بزودی خبر تمدید قرارداد علیرضا کوشکی بمدت سه فصل دیگر رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/24890" target="_blank">📅 23:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24889">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WExLLZi1mh2E4tqvAQOdW26VT8AhLP6xIUUfTPO1NYNga_cNJ3T3hZGjYVezCNmByvh2Xp1fdf6A1I0hnU7zvXbu_76XoTFf-2yxTf6i-M1qCgcQsuOoed3Xnen5AASWd3cjasbwTsvQZpHpgod8BN6Bte1OiLlruiwyoXCJ1PfV6PHpCzPxH9x1eYpbGjAejNFGWObRXTozxltEqHaadH_jR9enbJAH4VIPlvJckiTzJ0d-Z7TLaHn35MbhHBVRXMF3eGFDyVDbYaVRWesPEEsGnTGDN2o4SnG0Je6DZUOXVKESqJ42oXcy8B94QeLQTRH-FrR8DLWB28p8uPBFGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/24889" target="_blank">📅 23:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24888">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFfMiDSWJsPc6Wo2WU3S1YhCcIUeMMSGtDJO2qKOEfgFl3YD23Mnnevsbf34ef4DLxgjJQb7Gz6v3r4yrSPYFkA2PVTJq0YyB0DB0N3wCQsNvey1kh-TwD1bsjttN4XTQ3nEagyCxoMwwJ0bOWjeWvtRaqQVABKiRpo6DizFcOgHzd36fcib4Q0bCRX23BcViTf9Zj8dtlCaQ1RjJsSKsIkPhuTeux4tkF-_wlOA4lTMl_Jfi55W1h9iV5v2fAhNE6oDhADCWIzi_z9IhX5xgk1x3L3xO6bNQOzHErW_9DGXKsGsbec0u18ce_kX3iNyKnv6YkKuTBJtk426HVyWpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور که در روزهای اخیر بارها گفتیم؛ دراگان اسکوچیچ سرمربی سابق تراکتور پیش نویس قرارداد خودرا باپرسپولیس‌امضا کرد اما اومدن او به ایران منوط به پیش پرداختی ازسوی بانک شهر است که بارها گفتیم یکی از اعضای هیات مدیره بانک شهر مخالف جذب اسکوچیچ بااون‌شروط…</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/24888" target="_blank">📅 23:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24887">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ts4mpy4t_K65wptbm1nU1L2omUDeoL1OEw0DFwvSPIGbKMO-Z8hLh9aRwmHcem_Gil5AnAaT3WdkiDtRrQbG--TKjpGXYuctpuDeN6n-6mUJd3ipXxyOAjjtroYjIXi6wNJSkYeZ6GsI0im35kRFqKCOKYrqE9PhZlsAbbcQFPgnvcaMqBFwI_HhlxigRC8Jg1kg_ysMiJ6mB80ft-bvDm61cwZpxvAqN8E1G0MNGWE9L8a86AP9bPNlKi4-V9HNWFAqJIGkY1Pbv-pb0YHJBUlqYYOTOmUQw9hZhJRz8MG4tdRGUj063Iyx4oSPC8nU8V7os-KnDU4yfWXeUDr4tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
تیم‌ملی‌اسپانیا بابرتری ارزشمند سه بر صفر اتریش رو شکست داد و به مرحله یک هشتم نهایی جام حذفی راه پید کرد؛ حریف بعدی لاروخا از بین یاران کریس رونالدو و یاران مودریچ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/24887" target="_blank">📅 23:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24885">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VK1WJoFuUBTB5CVoZb6-G_lvcO7PGqurbEYV_EnvVjmWtG0ZBd-LhXZVHVaoN6GcLIoIvw6lXi-pvpjasFez1yyxCSWPaFU6WarADfj8FPC5wCLZ6vvfMK5seI0b1r3rnJfv3RE-NIAjqx-7VqkOgpJv9JfO41W3uwwBRYBp6AxNtCslPM4Ng9JjkS9U-C2MN4Mf0kNoEeuxdp_wmVDWuBvsa6zAq8Bo1DZ3jlmPXWbZVHXK8RkPV8JXEvt_YMl-wjdLnKuJNQmC2IibLnN72tYz0ZZ66tkl1OEucOsQEJJM7b35IFjiG4yS2Pau134qv68i5AG6T9o0BePm8lZJlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق آخرین اخبار دریافتی‌رسانه پرشیانا؛ وکیل ایتالیایی باشگاه استقلال عصرامروز با ارسال ایمیلی به باشگاه باردیگر اعلام کرده که ظرف دو هفته آینده پنجره آبی ها قطعاباز خواهد شد. وکیل آبی‌ها در این حد از بازشدن پنجره‌مطمئن‌است که به تاجرنیا اعلام کرده اگه پنجره‌بازنشود…</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/24885" target="_blank">📅 22:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24884">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEZYQX-RoQF4JckxE_cwLTe7STj6VMiK1ld5vBpjERaDGiNd_8wmoyUqUw5S4qsId7Cdl45M5FTrwxHyJ0u3hPbObISwB4xBkCE6vuh9tJUczkNlcKvbkfoZ3vqxHyu9CqycVBDlQLc3iC2R0WbsA6UY_5y93SVr2-KhzBqH51H9QEutW-rIihHd3CIABQTKY-h_an_GUfvyafj1oJ9yMS91jTASLqHRyXRuunWsh9RvT9r2lSmPt17PCXsYClbYjyZ5iDxvMQkN1u9IvnN9Rifv-xOJpqO1FUp6JlaCTvSjkMlXa98JgJnYfZfuLNrvg5I6E7gD76NjHZ4FexV0kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/24884" target="_blank">📅 22:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24883">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fee6a7d4a2.mp4?token=eX46LuQyKZvsUZKafkyXwXKnlGUZwJj0ONRIwwuwREY2-Cy3DgXbEtbvj_txqj-ZejpLwOljLEYPlijoxM47fnUITGvBJ-gQXE6kyHQ_kKcMFLOMwzvsVPYrbQbNxjFlsmznOAt5pfBn2OeGKZCD8OKU1wDz2Jo9k9EEtfroCtAaivh84gCg6_8smKm-GLwY7INV8FeEzE3KhBdDii0Mmohfva2pDIQ7M1fFhEMmRbMCbNH79DK9vWyBW3NRHSKGMVsXDwhQNm1GmgSl_cFAhPEP9ACYfd0aBQk90V0Ab7QSOFkyjW6thhKyng8Iih1gr7BZ8rDnacdMPbgX_SKRBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fee6a7d4a2.mp4?token=eX46LuQyKZvsUZKafkyXwXKnlGUZwJj0ONRIwwuwREY2-Cy3DgXbEtbvj_txqj-ZejpLwOljLEYPlijoxM47fnUITGvBJ-gQXE6kyHQ_kKcMFLOMwzvsVPYrbQbNxjFlsmznOAt5pfBn2OeGKZCD8OKU1wDz2Jo9k9EEtfroCtAaivh84gCg6_8smKm-GLwY7INV8FeEzE3KhBdDii0Mmohfva2pDIQ7M1fFhEMmRbMCbNH79DK9vWyBW3NRHSKGMVsXDwhQNm1GmgSl_cFAhPEP9ACYfd0aBQk90V0Ab7QSOFkyjW6thhKyng8Iih1gr7BZ8rDnacdMPbgX_SKRBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
بامدادامروز دربازی‌پرتغال-کرواسی‌شوت Cr7 به جایی برخوردکرد که شبکه 3 مجبور به سانسور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/24883" target="_blank">📅 21:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24882">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fK3LGhofwdjlA_M0eElAj84sTqCxlFO7m9Xfc9aCRfNZOP9xXIkO6Q19sDNjoFE4W6Z29hPqfKfvMtLh3LodvFx2UpkXxnJ4zL8wF92Vl_SaClew8PiD20m0M-gG-hlcooCgSIw3oUBt_A5o5NtLxQxz_oIG5W7EdzxifCJZXYcK0FsgFy47_ChVgW8RTa_phuKdNcS-1x-1EmIxCpGEP1G7fPFu6Ldgyr8NcNhom9LqhAGTfDO9RAzf3VrhzG2G09yARlUxhQFIk2JilBamxzfNmvXyo7LyMLnDHL5xSQmf7SRKfQfPwn6x7YWluSHQEIRA1JNKS_Rjl9kYmiJ3sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
رودریگو دی پائول:
یه بار لئومسی دیر به تمرین آرژانتین اومد و من‌بعدش به‌لیونل اسکالونی التماس کردم که مارو بخاطر زود اومدن به تمرین تنبیه کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/24882" target="_blank">📅 21:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24881">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AyxbXSmdwt_Kbi0a0eJN3XD3oJFqxlLa0MSbD5L3q6ydZpqJY-5mGgfUrSC7utXARf4Qqlf2AMb9wvnZyEY3JgOdFZPEmDedAEWRmwqIcTC8CzJzYJ4GDCI_xHoJ36TvEu7OkYG1yWH8C9UrR5g3mREdmpUItcbvbioWEGRrVEF9dSpvUOzPSK4s8210ucKq9ES2MerYvXdGEKFzKwM_v6yKo9nLH88A16UB7C7X9ksotEQ2n_fQ8_3bKJ1Jf9qaQ7dpXSkFsFrQTkh9EErchwt4WPl5UqI-_FteuEmHJ_S5y5ehvNcGRf6PUBhuEk88uL7201t7IFYUFRTb34cleg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
علیرضا فغانی داور دیدار انگلیس و مکزیک شد. به‌امیدموفقیت آقاعلی عزیز در این مسابقه حساس. ایشالا خبر سوت زدن بازی فینال هم منتشر بشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/24881" target="_blank">📅 20:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24880">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXiC1fSpG9XGIaS3sAablp2SmPYkwWPj9aRg87v7K-M4L1xany7H0E3KVqB7FvtuUWxHsP8DOtByVNLghXr8-3DTPn9r_9wQYSSSH_mLEhbWpEdY5ocJqeitmbV0uy1joj30vnmGi6RDLzmUZibXneOT2ILQFMwdQLAv_scBtCr-mwQr-H3UYCwnQZPZQvK0Z5fdK8JRyPxf_wKIY8fdWLB2YzaTKfKFjylbJKo_2JBY2ypc0nFPnxK1MAx3IOMpILwXxigztV5NPFCw5g21vbcwVE48_FZt_5W4tHjHLNhQhMLxUAQL86GkmfW8XmyuN0DbWcGM0CuWYlUtEgl9nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سپهر حیدری رسما اعلام کرد از ملکه پاکدامنش جدا شده و دیگه رابطه ای بین این دو نفر نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/24880" target="_blank">📅 20:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24879">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9736fee745.mp4?token=gdE8ZFMHbOUlNOO33l9_IUj1Q7eWnPymXV5Hd8LbZ_v_QA02PPmtF7uJn87QqrbtriEiKC3vLWRqjC98ilt38CzKpk7xd0B-KWsuk_NoalgI9s_M1g9t4gmMgOVU9eRvEJaOcDjiaWe7M2l5s8-WFFIC5qgBPoM3nXYMeBaZZWi71Toz7Xu1DflDa3w8PD2n-LhYXmKdFntQ8uagdvEWr9iEZI4EagFPDJliWseHbtk44d7ckUUpXfOKHJj5x1wbelFKWbJNEfptQlEnjSl_yudSDNWXeXoYuWcOEd3oTYm-Njj-bqOxl1PBQuW1TaRfEVTZYQR2TLIO1KZGG-pnpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9736fee745.mp4?token=gdE8ZFMHbOUlNOO33l9_IUj1Q7eWnPymXV5Hd8LbZ_v_QA02PPmtF7uJn87QqrbtriEiKC3vLWRqjC98ilt38CzKpk7xd0B-KWsuk_NoalgI9s_M1g9t4gmMgOVU9eRvEJaOcDjiaWe7M2l5s8-WFFIC5qgBPoM3nXYMeBaZZWi71Toz7Xu1DflDa3w8PD2n-LhYXmKdFntQ8uagdvEWr9iEZI4EagFPDJliWseHbtk44d7ckUUpXfOKHJj5x1wbelFKWbJNEfptQlEnjSl_yudSDNWXeXoYuWcOEd3oTYm-Njj-bqOxl1PBQuW1TaRfEVTZYQR2TLIO1KZGG-pnpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
وقتی‌قانون‌برای همه حتی لیونل مسی فوق ستاره تیم آرژانتین هم یکسانه؛ فقط خنده‌هاشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24879" target="_blank">📅 20:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24878">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FnPkLDy08USmrgQ3RdROaPENvKer74GfB5xZAVjfygVSQ5kVPL3vTgvGsCgIcXn41uMk1Nvsi8ykRJFwgrLK6nIWDwwZYLDR30PKqtU2wRUpviDjmLT9GtHDGaIdP8yt0EqB-UKRhiMwl-4pkjzcimagzReZ7ltksQ80zzEkhjNUfe3Phucz1f38RN_k82OZmsm4oX7MI7S9DXUO9_GqH8WpVG1_r5TPmLUKwX8qni0LE6IpsBkv5YYDFgCw6b0aQDG1t1Fv_JXBP8wRBHkuqfnYjIL2mST8rl_9Nt8KLRSKlh9VcJDqkiZoomd9uSX5sqdvfCMPIOVDZMy8k-IUGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق اخبار دریافتی پرشیانا
؛ کاوه رضایی ساعتی پیش با حضور در ساختمان باشگاه سپاهان قرارداد خود را به مدت یک فصل دیگر تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/24878" target="_blank">📅 19:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24877">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/459003d30a.mp4?token=cKbeTdstO_CzCWUmKNCkqgnHSigYFMMzXxmJvdxKXYcijaRO4em2lFTMCmHW1Ab6bBWR7dDfKw2XpbqV-epdjXqzkD7-mibC4-lD_GVuUqly3-SUdjWU12uoOY4Ci4RuU4inDm8IfcgJKP0e2Nh8rQCq5byDbySDhWFdI2tX2fJOWER_h_UgVHbCRHFIYMzAEdy-IDstqH8uhj4iGlK2_IEFjRGZi-daeHblSjb3umSLA5gjeOtmHmIPD_pdAiskvxpIeYY7VJV-iewv_akNqI3RHQhYwf3WRfqd3wWXSA5DCAHeUw2JxCYsQcr-E8p8n45BOktgWgOwdDqw5PrlqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/459003d30a.mp4?token=cKbeTdstO_CzCWUmKNCkqgnHSigYFMMzXxmJvdxKXYcijaRO4em2lFTMCmHW1Ab6bBWR7dDfKw2XpbqV-epdjXqzkD7-mibC4-lD_GVuUqly3-SUdjWU12uoOY4Ci4RuU4inDm8IfcgJKP0e2Nh8rQCq5byDbySDhWFdI2tX2fJOWER_h_UgVHbCRHFIYMzAEdy-IDstqH8uhj4iGlK2_IEFjRGZi-daeHblSjb3umSLA5gjeOtmHmIPD_pdAiskvxpIeYY7VJV-iewv_akNqI3RHQhYwf3WRfqd3wWXSA5DCAHeUw2JxCYsQcr-E8p8n45BOktgWgOwdDqw5PrlqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
طوری که‌‌ تیم‌های حاضر در مرحله 1/16 نهایی دارن بمرحله‌بعدی‌جام‌جهانی 2026 صعود میکنن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/24877" target="_blank">📅 19:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24876">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZuAS6twZ9-rvWI9zuXzr_0DPHEaZ41tdqUE3jPhhY-wY27hI2wpXxPt1VqVZ8eNEyOI5NzYL_A4JohdYFnlJp15BcXYe6wbWNm4dkIYWOWo1QbhxyKXWxCS5DA-F2IyUofTL3mg69SdGayY7TPOjOgZoPNUSH7IOGb_JTFSK30koG_CFkO74A0_jdBGaCiWgVjsXkUz4buqi63yVagwX2Vm_X2uIvpqA72932hdAPkSwn06RqNii74yajm1O_naA1NjnfnjbLKGRGn_onNLByHIVQhg9Of44ThnG8VLzXNkloQgl7XcObGiHumqSM97entd-1VEj9TADOuL8rKzObQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
👤
شیدا مقصودلو همسر29ساله خوزه مورایس سرمربی 60 ساله سابق سپاهان و الوحده امارات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/24876" target="_blank">📅 18:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24875">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/376f8db7a5.mp4?token=oTReQOIN1HiqG9G9MswvEJBkpaNWp9OxOZY6Hkfckts_QopcgaWj4CVhFilGQzHkBxOfBP059PzdrhsMSil-Cor2aoI8cno8AoMZEobYxMvMZgLUkstKT-TrY9RjECObav1K_VqoRJLSwrWkIkEz6FvzPOB6zIK_uRm6tDEIg1EB4R1qDuiprDwUlZ3FoiDr3upAO_oYDigJO5oVw2oDGjs9WPruUrLRuF7A1KWUpna-WlkXJPKhX3DMAfaTGM7ggSeVzVCWfZfivoirsS8DWq4tKxR6sP2Y9yxCercFpzt-LjEzilz378tp5OuVvcgFCww5HSFTCzDNOPDXHdruuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/376f8db7a5.mp4?token=oTReQOIN1HiqG9G9MswvEJBkpaNWp9OxOZY6Hkfckts_QopcgaWj4CVhFilGQzHkBxOfBP059PzdrhsMSil-Cor2aoI8cno8AoMZEobYxMvMZgLUkstKT-TrY9RjECObav1K_VqoRJLSwrWkIkEz6FvzPOB6zIK_uRm6tDEIg1EB4R1qDuiprDwUlZ3FoiDr3upAO_oYDigJO5oVw2oDGjs9WPruUrLRuF7A1KWUpna-WlkXJPKhX3DMAfaTGM7ggSeVzVCWfZfivoirsS8DWq4tKxR6sP2Y9yxCercFpzt-LjEzilz378tp5OuVvcgFCww5HSFTCzDNOPDXHdruuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
​​
وقتی بعد دیدن بازی‌های‌تیم‌ملی نروژ و تشویقی وایکینگی‌شون‌میری‌باشگاه‌وحرکت قایقی رو میزنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/24875" target="_blank">📅 18:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24873">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97048a0557.mp4?token=Qsq9FbgYoafczS5f8XI5JNwK-FVzi56ixNfSfWk43ZuEaJZAE2QkgIt5SXWPNpKZPC8d0kszRXce-3d-P1SieLduUQLvsvRWYFTqeuTSL8h8pFPZhbtoa7zv8fZdDdtpRA3d3GtzHeiKia04qZR72OrTCGdlfI4C3NnA6bRPAuVSpW0A1wdqMfmB-xlm1Bi9IjduhKlKPi5nNkFfj-B5AdwtGY5p0AcNvEqDbz9slMJjDM7kezTukpE0dNUlLu8L2kzX_x3cOcbtV8D73dIGefwk9Kls0W_P87ZlwZTw_q3fQXR0A1me0V9oZrqgF7as5Sw6F7EOxbkWWaRx-rg9PLWXU9nlhljzkAajDtpekgCKqNYIrQXAsf4ACxBIQr0ZrOgzEuVw4TYr6H_G5_9jziOid8_CN-qGBH1F2ET39O7UgKZkwb0hTYMtQpsjZUE55P5DgSNcFJsPXts7_9RZqG-URanQvC2QXCtEP2MiAE8qk10RqgBEr8ahTJbzBicVACEDI19ZCYF8lVH_0AeutYMpRbAAGzEQaGq2HCdja87CaaHRzjULFI7yK4j4Dgy-uSB6rfG53VnapvW6GsuP1rf_Sn5ps2rgLr8sU7q3BHbkjIrA-OIC9YZ5Xpm-gNfg3q-hq2grOB4ldUxdGwVmd0ocqDVXKzZ5gtULZ1p7cSc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97048a0557.mp4?token=Qsq9FbgYoafczS5f8XI5JNwK-FVzi56ixNfSfWk43ZuEaJZAE2QkgIt5SXWPNpKZPC8d0kszRXce-3d-P1SieLduUQLvsvRWYFTqeuTSL8h8pFPZhbtoa7zv8fZdDdtpRA3d3GtzHeiKia04qZR72OrTCGdlfI4C3NnA6bRPAuVSpW0A1wdqMfmB-xlm1Bi9IjduhKlKPi5nNkFfj-B5AdwtGY5p0AcNvEqDbz9slMJjDM7kezTukpE0dNUlLu8L2kzX_x3cOcbtV8D73dIGefwk9Kls0W_P87ZlwZTw_q3fQXR0A1me0V9oZrqgF7as5Sw6F7EOxbkWWaRx-rg9PLWXU9nlhljzkAajDtpekgCKqNYIrQXAsf4ACxBIQr0ZrOgzEuVw4TYr6H_G5_9jziOid8_CN-qGBH1F2ET39O7UgKZkwb0hTYMtQpsjZUE55P5DgSNcFJsPXts7_9RZqG-URanQvC2QXCtEP2MiAE8qk10RqgBEr8ahTJbzBicVACEDI19ZCYF8lVH_0AeutYMpRbAAGzEQaGq2HCdja87CaaHRzjULFI7yK4j4Dgy-uSB6rfG53VnapvW6GsuP1rf_Sn5ps2rgLr8sU7q3BHbkjIrA-OIC9YZ5Xpm-gNfg3q-hq2grOB4ldUxdGwVmd0ocqDVXKzZ5gtULZ1p7cSc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
و بازم‌هواداران تیم مکزیک؛ اونقدر ویدیو‌ها زیاده که باید هایلایت‌کنیم بعضی‌هاشو بذاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/24873" target="_blank">📅 17:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24872">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a06e45a5e8.mp4?token=JtyMMcQ_3HqP-xvF-AbNlbqrizvh2lF0pZv3swGi57N7B59jED7gsADx0MXGKjK2V4Xz6lox2OQ3-4mB5YrzZ_zXs_LO7w-BGehN97AuwKoQyxmZTAqrTrZ3-Na1fznuZsVxe8Mu_mNZ2oW2dpagYbSY2IpAIHghN-0qmMcGB5uK2fyFB_ggKlhVmeZIgSMXfZW7yrO8Q-g9NxWw5E45_1laoWOZ9N8Np0GIfWLQFZ3wQZiFwOfyom9odFNhtrxQbI1IJRIufCT3B0pl9Pr1MxiBYk5YN1ZfG2R_s4Rh2CJLw27_m5EFpk3Rty2RiGD5N8_cHIl_8aDSWtRZiD4NhXPtRGdPBf3LUANJmLzjS2iFGsbh2S1llLNtk4G0Q4sMyX09chfrB38J3GbuoQcuAi5Wm8oyFHfmrNpGxTKtjClpM3ZXU79Cvy42S7vlvomTFDrJkpA2xo-En2A-_0Qz91lqvMU9O0xee0fto0Tw0EMEQYgCvir2m-Be8UgSrEYKfLUYhhArAqhY7V1Aj6TyRoM5PAotmShDZDFV0txEAWYuRXxg6OTb5xDv5CNlYeGxPb_yi7SI-hki8dFpwUEKhcZ_XILYEGITscLET8icUv1nbgRk_MaT1vMA0I_b88OYLyW1hbyyBJjpKVS-0qYlBGZkuAlL9_d8ykd4OxudvOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a06e45a5e8.mp4?token=JtyMMcQ_3HqP-xvF-AbNlbqrizvh2lF0pZv3swGi57N7B59jED7gsADx0MXGKjK2V4Xz6lox2OQ3-4mB5YrzZ_zXs_LO7w-BGehN97AuwKoQyxmZTAqrTrZ3-Na1fznuZsVxe8Mu_mNZ2oW2dpagYbSY2IpAIHghN-0qmMcGB5uK2fyFB_ggKlhVmeZIgSMXfZW7yrO8Q-g9NxWw5E45_1laoWOZ9N8Np0GIfWLQFZ3wQZiFwOfyom9odFNhtrxQbI1IJRIufCT3B0pl9Pr1MxiBYk5YN1ZfG2R_s4Rh2CJLw27_m5EFpk3Rty2RiGD5N8_cHIl_8aDSWtRZiD4NhXPtRGdPBf3LUANJmLzjS2iFGsbh2S1llLNtk4G0Q4sMyX09chfrB38J3GbuoQcuAi5Wm8oyFHfmrNpGxTKtjClpM3ZXU79Cvy42S7vlvomTFDrJkpA2xo-En2A-_0Qz91lqvMU9O0xee0fto0Tw0EMEQYgCvir2m-Be8UgSrEYKfLUYhhArAqhY7V1Aj6TyRoM5PAotmShDZDFV0txEAWYuRXxg6OTb5xDv5CNlYeGxPb_yi7SI-hki8dFpwUEKhcZ_XILYEGITscLET8icUv1nbgRk_MaT1vMA0I_b88OYLyW1hbyyBJjpKVS-0qYlBGZkuAlL9_d8ykd4OxudvOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
گنگ‌ترین همکاری‌تاریخ سینما؛ حضور غیرمنتظره مسی درتیزرفیلمSpider-Man: Brand New Day
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/24872" target="_blank">📅 17:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24871">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUL20j9R-Pii7xDOHYTNaaHHgWyC7TlQ4UopCtHO6K4c9SmZ1MWiDnES_mp2Lvmt5YCnqtygyGlPKvat2CI23Z30qpcjP5s92Nhw32KTpEzc3-CUHPH4XP8S_aH0Ku_sXprdLCttV2VpMnlkce9IjIVQfVloGMyBIRhGyucLc1o77XhkoWRkepSOf1DDTHMTfo6JG-wgT8kXO0yNF3nrKTSD7F8fmObNDMnArsJOOcqAgHnRw5YfvsATJ240rSoolP_q5w2iIGjI1ULtO9jEYk0k-UVI1WY5cHhokDjeovzHD1CUQb33cE92zfhVyqz6TBr5TJCKF1SUuZ-cQDFZRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
🤩
رسانه اسپورت: دیگو سیمئونه سرمربی اتلتیکو به‌سران‌ باشگاه گفته بزور نمیشه یه بازیکن رو راضی‌به‌موندن‌کرد.150 میلیون‌یورو ازبارسا بگیرید و آلوارز رو بهشون بفروشید یه مهاجم بهتر پیدا میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/24871" target="_blank">📅 17:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24870">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a0d41c219.mp4?token=AZmjRMSrC2Z6-HJLA-giBR0TSSL6MVyFM9v46LGz2zM0EcYoCCtG2GHSYNxSiihe1SjEA6LE7NIHTWkQMFemyxIeT2e0y-1xZeVMw6OtULPbPBQC7xAfFMHRN8XTgJInxDWrmuwDOnzt8eyZQUT_nGhgJdf1XEBq0zfEgzzShD1CQ4F-vC26n7hh-JsFRff8jocGIUF5kh8KskPr0mRSPfuH3tVgG1bb3qbxGGweg1Ccsja3fdBc_UrIElkEkuTOw08mQW7y5ck-k_0UGfVwFTeHclFk68ax165V8Mw48VWam_Z7Mga_wrBaXefLMmUvWdiOkxP8-SIvExbiWAsHQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a0d41c219.mp4?token=AZmjRMSrC2Z6-HJLA-giBR0TSSL6MVyFM9v46LGz2zM0EcYoCCtG2GHSYNxSiihe1SjEA6LE7NIHTWkQMFemyxIeT2e0y-1xZeVMw6OtULPbPBQC7xAfFMHRN8XTgJInxDWrmuwDOnzt8eyZQUT_nGhgJdf1XEBq0zfEgzzShD1CQ4F-vC26n7hh-JsFRff8jocGIUF5kh8KskPr0mRSPfuH3tVgG1bb3qbxGGweg1Ccsja3fdBc_UrIElkEkuTOw08mQW7y5ck-k_0UGfVwFTeHclFk68ax165V8Mw48VWam_Z7Mga_wrBaXefLMmUvWdiOkxP8-SIvExbiWAsHQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پدر آقای‌دسابره‌سرمربی‌تیم‌ملی‌کنگو در حین جام فوت شدن و به ایشون خبر ندادن، بعد یهو بعد باخت به‌‌تیم‌انگلیس وسط کنفرانس خبری یه خبرنگار بهش تسلیت میگه و این از همه جا بی‌خبر قفل میکنه که تسلیت چی؟ و با یه حالت شوکه تشکر میکنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/24870" target="_blank">📅 16:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24869">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8337fefdb.mp4?token=tGQqYE5c7kombYCmnOM9ioChwjb3sRtvLUwBX3mZ_VvFKhd2eULfo8iUN2UTz1Hiwf5yUDO0y-4-bFjRqs9AGXwmcKXJRqt536wBBQtUwkdqibTJU1MqHeUBLjOPMZ3O0U6AdAJVzPk9sador5PGkxojLnSC0TObX__PeWhy_j0eZerOL0ZXmfLaRw7yPB99-Yc8sFjni1Ol957pkJHvAeinq3iKYP4eSBqgA5bxKbNJnasgsG2_1JNl3eEHTZK25d1Hk44O1_kJRLgKydxX2hlZvPoEC_dYyl7MY3Q3fPMU_4bE-hpAGDpWinMbV67NBNmA1JcS_qKa4zad2_qNMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8337fefdb.mp4?token=tGQqYE5c7kombYCmnOM9ioChwjb3sRtvLUwBX3mZ_VvFKhd2eULfo8iUN2UTz1Hiwf5yUDO0y-4-bFjRqs9AGXwmcKXJRqt536wBBQtUwkdqibTJU1MqHeUBLjOPMZ3O0U6AdAJVzPk9sador5PGkxojLnSC0TObX__PeWhy_j0eZerOL0ZXmfLaRw7yPB99-Yc8sFjni1Ol957pkJHvAeinq3iKYP4eSBqgA5bxKbNJnasgsG2_1JNl3eEHTZK25d1Hk44O1_kJRLgKydxX2hlZvPoEC_dYyl7MY3Q3fPMU_4bE-hpAGDpWinMbV67NBNmA1JcS_qKa4zad2_qNMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس رونالدو: خواهرم‌ گفته این‌آخر خطه و خداحافظی میکنم بعدجام؟ دیگه تصمیمای عجولانه و بی‌هدف نمیگیرم. بعداً تصمیم می‌گیرم، نه الآن.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/24869" target="_blank">📅 16:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24866">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8659ae843a.mp4?token=KQu02cJ_-SJ9jGy0aGkY2my30lmA4Pp-fyWkbJ997m4c4CcB5ijYmCgN8sVHASnGEKQsZsV6LhJr3SogK5xjRuZ6P0yrZKpV3FrfqqoXXrkewFAqcS9f9BrOE6MFwqECZh56Xf_TF_pkW9tLNAoYbBNwTEvdUZMlhTBrOQsfs19l9t6rwZj_KaIVy4BTXd_tXmA-II3686NJ7ITLfrgCUmLSBi_ltdej1tJjfOn1UcmiDl0UQFJhHGacCWOsApjVL7elrugZIAnxSd7Y_ZekU6mSV90KLkbvJ40sJD0_Vw8J0V94wsAroB7ROJhECKEEk9f62Xw8VEDV2Xt818NHhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8659ae843a.mp4?token=KQu02cJ_-SJ9jGy0aGkY2my30lmA4Pp-fyWkbJ997m4c4CcB5ijYmCgN8sVHASnGEKQsZsV6LhJr3SogK5xjRuZ6P0yrZKpV3FrfqqoXXrkewFAqcS9f9BrOE6MFwqECZh56Xf_TF_pkW9tLNAoYbBNwTEvdUZMlhTBrOQsfs19l9t6rwZj_KaIVy4BTXd_tXmA-II3686NJ7ITLfrgCUmLSBi_ltdej1tJjfOn1UcmiDl0UQFJhHGacCWOsApjVL7elrugZIAnxSd7Y_ZekU6mSV90KLkbvJ40sJD0_Vw8J0V94wsAroB7ROJhECKEEk9f62Xw8VEDV2Xt818NHhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
ارلینگ‌ هالند ستاره 25 ساله نروژی باشگاه منچسترسیتی اگه درکشور‌های‌مختلف بدنیا میومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24866" target="_blank">📅 16:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24865">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euQ7O_Q97_UXJlcxZdYnkXIbif51kKdbyZGH01HA8RvberIUPJ62Ri-z7IqWNB8JGKisVkU-A-EPEoplCGZu79PKq8qCUw0lucTr4UGRYrtRApEXuBx3SGlyDqk7qNjS-Z_R11IUNeVDGXrpnOZ6fEtSpbK86Cibi1qeGpyRhZaxl1SYH_1Erwb_pNv3TXYUdxC3u4iFFW3qHRYSLnxGH8JED_5hRr5gPV_cyjUzSDZdGtC3MQPZqpG5iWpBSijDiOzomqSF5xxMgigGl-wG9Lvse-ypk-kiveyoa8F_vZ34URbdPd4DIqEWyJsOkWUlIxkWUvH5rAUrZZJvR7SGfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس رونالدو: خواهرم‌ گفته این‌آخر خطه و خداحافظی میکنم بعدجام؟ دیگه تصمیمای عجولانه و بی‌هدف نمیگیرم. بعداً تصمیم می‌گیرم، نه الآن.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24865" target="_blank">📅 15:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24864">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFLzGJUfQU3t6PSTuSKEXnbLY9YZ5qSkxT-z6MZNF-G9Dk4qVignFqFfWLv0yGnWQyBhWxuism_f0udpE8INI8ZUx8-Qign-4g6kXpf3EqqVZ9bW0xGGNC4EWDyjUgbUCoz43VD_4r5RcLuUAxDeXuDFAtgD9rznAoxWCfWlxUFNGsmcPv7QWwdvF8UepVpHduNsN6BWGskofJCk1FJUz_HQIn3kwc-IXsmA_BsSeMsDn5q8ZwBd9w-37VHhZxHHdaTbNHrTEApnyEsuWox6NICX5zFzqLA5-P4tHeHAD-S1bsZsYdAF7V2zCgMUPh6r0s50DdTMigjGSZI4DJa0bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
محمد خلیفه گلرآلومینیوم‌اراک: باشگاه استقلال باآلومینیوم به توافق نهایی نرسیده. الویتم حضور در لیگ برتره و دوس دارم که در تیم بزرگی بازی کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24864" target="_blank">📅 15:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24863">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MMPrmZ346P0IjRUfJYZgr5sblRNXndB9KC0XmOvNpb81NeLgraS1rdZReFQTrjDzeLodMs8wznSo6IbsRqqzUvK9v2FPiJm2m-EtaPjfsjiTOHh4UbaTSKpsdFPR-2dgC3OumzzxOc_LQ0CVQRqEy86k5AQ_HI5THpBWDtI5eWNfkdmBx1XeFfAyQXSryHq8m6M_cPwyMOmTFloJau1tEwWSvOyrhllMgqHKQkfyOuE9szp8flhnimuiIVhWrGTKaISuWT3cxltKFQ3bkzn3Vzho1FQWTeor-hFbW5eS6bQRP6D-gHcx9A9IXIgTo4HDC0ma_uF6Ck5FuEkzSM1j_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛باشگاه استقلال دراین‌پنجره نقل و انتقالاتی بین‌علیرضا بیرانوند و محمد خلیفه یکی رو قطعی جذب خواهد کرد. با توجه به توافقات صورت گرفته بین‌ابی‌ها و مدیران الومینیوم ممکنه که محمد خلیفه بزودی قراردادی پنج‌ساله با استقلال امضا کند اما یک فصل قرضی در…</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/24863" target="_blank">📅 15:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24862">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2z0KDAusMeBx3a_C7ciBeqnBzueCs5M1vf5hpgrg-hAw3pTYKF9O-ZsA9npAkqOlYaymJvEjlYy_Au79qKWoVw6qR6uD1gMrm7fg9CBjsSb11_CFLkFvIA_EDSP-nZRUfn7eNQzLhy8NpVEVbVOLQUTkT4TFLi1P-YPF4UjDqBLAAODvwG6_aSU7fUrI1A1eOGKfcD009osQldZwOZZVWsvgUkuYSpaTzM2JDekCvEDLkJu3TKLmxatUu6OGbod86UKlqdVdKr3puRTWwX2OKszODluiVWxMBFSRcn1TITqnzHKml2Iun18K9_znylJ2XenBCorUsqx7sskGNJmaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
دو تصویر متفاوت از کریستیانو رونالدو در دوسن 21 سالگی و 41 سالگی تعداد گل‌های CR7 در کل دوران حرفه‌‌ای خود به 976 رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24862" target="_blank">📅 14:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24861">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOIyLKTWDsrewVF9dD9BAXshTc_G7vFaKzWhL4G2x-O8KvRbRfMz81NjbfwDYQZC3zD3kmWxczA_d7PpDDRelsuN18WRlmnTr0W9i5vFxa8S5p1f6qhYYCcscTeRy7MyrQ4xcS2OBmZL2MA1oe1y4JOjiaQhGrWj-ozc__yuQr9zAr5hoKqXnVLPeq369No4diAz-aGl3eXj259-B-2cpePv1ER-7xy_Xi9HN8g5iSsRCBLUV55lqGgbB3naejBxxbrWtcrK-jGlMEfjtg0Rbj9fr0s-Q8fEbw2HmEE5NjZAFTQT0FGXvrYXRBU7BiJWPtsqkIPGt7nOJhZAVSOatA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
🇩🇪
#نقل‌وانتقالات
|
مارک آندره تراشتگن با عقد قراردادی‌قرضی‌تاسال ۲۰۲۷ راهی‌آژاکس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24861" target="_blank">📅 14:44 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
