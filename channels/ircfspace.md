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
<img src="https://cdn1.telesco.pe/file/pXJOLAqNXf7Zia-dppT5GTqvvX4epEZhTyl5PQP3-XHCbQi4OjOErZcfOsDyRR_r_h4q_ghGuZNc8U6He9jnxppRNESyihUV7yyugBlUy1-sh1MPTAZbUGBmUw9szWOGLSb5qGrpf0pmxyJjj_Acqc6ZsIDaC7an8KG_14KPxc8-1ku84rMOcGYNwSThZiWNXiq9pIBF9875l74ZpXjZvr5PC_O7zFnfsewMs3suqbOX01-1rVeQWo4ZytB-fZotlb1bIP6p8dpyeU2dKhBO1dfdL-152DzWWMlCFt4F1Uvr6ssQukJEkCURV4h_hQgTNQvp_SXdwJvljKSKxs_kdw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 96.6K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-16 05:37:29</div>
<hr>

<div class="tg-post" id="msg-2657">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eKdLyTWAGXzBgC6qu_ts4622a6UAWpcmrQ5I3MBOO3Eofytavzg_gsFG7pZeVWpdvzEMVYFfjX2Rmf327uZTHtAOoO456sZVkDvqBN6c_6-wOkj-_U456-rPT7IEGWd3MrylZnCnPfeSq7ZSMnRFbuQ8Mz4xKGU1BLGkIrLinlR8UnYtMQSpBENS37ACJV2oVWBnPetsfk26TBHUov2ZiaoNU5-ZpJO3UeE89JBJTmopSJuR9T9vn-gPvMjwbzIVOX2JvfSHjukqGK3N-YiOXQqi6dNMEmdYLALjxlDoG153Tuvc2VyliD3IG_DwOzlgjb4kzFZuu7KHVr9ZMtN7CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت متن‌باز و رایگان ZedSecure آپدیت جدیدی برای اندروید، ویندوز، لینوکس، مک و NixOS منتشر کرده. در این کلاینت از هسته‌هایی مثل سینگ‌باکس، ایکس‌ری، اسلیپ‌نت و شیروخورشید پشتیبانی میشه و در کنار پروتکل‌های DNS، امکان استفاده از OpenConnect (سیسکو)، IKEv2، OpenVPN و AmneziaWG فراهم شده.
همینطور OpenConnect روی دسکتاپ بصورت VPN سیستمی قابل استفاده هست و امکان اجرای زنجیره‌ای روش‌های اتصال مختلف اضافه شده؛ مثلاً میشه سایفون، تور یا SSH رو از طریق یک کانفیگ Xray اجرا کرد. روی اندروید هم قوانین مسیریابی میتونن بر اساس نوع شبکه (مثل وای‌فای، دیتای موبایل یا اترنت) تنظیم بشن و با تعویض شبکه، بصورت خودکار تغییر کنن.
👉
github.com/CluvexStudio/ZedSecure/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/ircfspace/2657" target="_blank">📅 20:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2656">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nj2B6gl_g77pPswdY0ny6TtdUz491ePKri0gFNXrUbiVRyNntVNYJq5ImJ5MM50uc8Tk9ib-yozXEELe7EwAUqqhFc1RtG8fqoHeZPt2GoYlBtUon1IOv1nL44Aq0MH0SaTJ3e1irn0DxFiujFxt1T2CbFfPJ5G3skAql6qAPTTTMvUYw8NEyH2-yyNZVzF_lDcnzHgcJCLchcIT5LAvJv220LWVv0hsatzlqbfaEBMu4UFsUEtjffCMI4Gon7m9WZM0co9NcpiGJ77vpQtiA1phYV66GfQoR7XYJm1Yu80VnVnHK50g1D2VrTfod-VaJ8FtllcMtcNv97Xyb8Jv2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس داده‌های رادار کلودفلر، از ۱۲ مهر یک ناهنجاری ترافیکی در ایران ثبت شده که همچنان ادامه داره. ترافیک اینترنت بعد از شروع این اختلال بطور محسوسی کاهش پیدا کرده و حوالی بامداد ۱۴ مهر به پایین‌ترین سطح خودش در این بازه رسیده، هرچند بعد از اون کمی بهبود داشته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/ircfspace/2656" target="_blank">📅 20:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2655">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CizJRF7yIbbsGdVbmAnxJiNikWadgV93bt7c0PJ0exzZfK423AAgTon7s13bjC2_BYfODFNoAws7QxzI4zCScNicoJnu5RZVVgu4lIi4Am2_G7kO4u-iqqqnkbg6cDqwy9BBx6UHd3VeAh8J6vgtPrsB90izC-WzkPEojc1TR2BZAsPX4OWAUa5qcXqzT_Mzs_3cJLbhp1NXGzBy1P8ZcPYVVBicgLWVae3Cigp87M8snDtH5Nb8Ac27Kq44yf0FADJQXXN0bCVb_BmIZkXimUWaocJsA6gFw7TYlFywGhoIOPPjkQJI5BGjJWUOrlDTrPF1ree1LyDBsE9tuOZdIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه جمهوری اسلامی در واکنش به سرکوب اعتراض‌های دانش‌آموزی در فرانسه، سفیر اون کشور در تهران رو احضار کرده!
با در نظر گرفتن کشتار ده‌ها هزار نفر معترض دی‌ماه و ۸۸ روز قطع سراسری اینترنت در ایران، ممکنه فکر کنین طنز باشه، ولی منبع خبر تسنیم بود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/ircfspace/2655" target="_blank">📅 19:55 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2654">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O_E0ZENxlDJk8wssEik88iFUYLHb8aMazOuLZBdMbXsLjP422Z1UImgfiwRw0S6wPYtPIwitPcmF3OMSVGAEWGM8wVAhV4-cM3nh2EYL3sD1DjB9DzyPAPjQwbXXWAM_A75pmWhtI8ZG7x8V1lymD8zycUtC1TVgEZSX8lo9a60RslAK_bGoMiP1wOwyc5WkR630jGQ9R0WOsmYMGe3B9azN8uzxuFyzadSAypU7_O62Fnv6p3K8BGa7ZvGA4LDR3ZIXXRWte488DDuAkZxFhQZuLsLvCTkDBf9IE9uyE_L9UJA_x1imM5EhI23-w5E88LBwzsiSS0YnDjPTipRdqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از اسکنر متن‌باز و رایگان SenPai Scanner برای ویندوز، لینوکس، مک و اندروید منتشر شد، که توی این آپدیت قابلیت Anti-DPI اضافه شده و با تکه‌تکه کردن ClientHello (مشابه چیزی که در PattNG انجام میشه) امکان دور زدن بعضی از محدودیت‌های DPI رو فراهم می‌کنه.
حالت Gentle هم برای اینترنت‌هایی که وسط اسکن آیپی‌های تمیز کلودفلر قطع میشن اضافه شده و حالا می‌تونین آیپی، رنج یا دامنه رو مستقیماً وارد کنید و اسکن رو از فاز دوم ادامه بدید. امکان ذخیره اسکن و ادامه دادن اون بعد از قطعی هم اضافه شده.
👉
github.com/MatinSenPai/SenPaiScanner/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/ircfspace/2654" target="_blank">📅 19:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2653">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">شستا ۱۰۰ درصد سهام رایتل و ۵ کرسی مدیریتی این شرکت را به مزایده گذاشت. قیمت پایه واگذاری ۱۳۰ هزار میلیارد تومان تعیین شده که با نرخ امروز دلار آزاد، تقریبا معادل ۴۸۳ میلیون دلار است. فروش به‌صورت نقدی و از طریق مزایده دومرحله‌ای انجام می‌شود.
©
stup360
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/ircfspace/2653" target="_blank">📅 19:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2652">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fRtJJ1sc6VnFUA4I2o12aZTO3LivfmQ0tfD7ajuoPjMmXXHEiRtnwgXx_eWO7GCEhCw464SM6Me8WARiVbZv0nwfNV4aKbFygCG0KdUgTz0_LPMwOqM9ZOLDcw-rgxFFd8jN4Z1W1Zw7JKV-23twlxbIgrnERZscZYovruczh8H9tRRB9rgb2Jm-jdS2LZBksVImZ5sF6TwZuwSLFNQ5w1CcOSHGQrsiE6u6J92QwCTLimrnDhYdZLzNbNoP7iqKJkcSxfelLS5rt4i8oTGXvKyfI3kDRIQDWq-rg7jy10Z4QgmfPBOi96HQquX_1SD5U8-rCy4YGl4EpViKhy2a-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پترنیها در تحلیل وضعیت فیلترینگ ایران، جمع‌بندی روش‌های فعلی اتصال به اینترنت آزاد از طریق کلودفلر روی فایروال همراه اول و ایرانسل رو منتشر کرده.
بر اساس این جمع‌بندی، روی فایروال همراه اول میشه برای اتصال به CDN یا Worker از روش ECH با یک IP مناسب استفاده کرد. استفاده از IPv6 هم یکی دیگه از روش‌های فعلیه که بسته به فیلتر بودن یا نبودن دامنه، تنظیمات متفاوتی برای finalMask داره. برای WARP هم میشه از متد WARP-in-WARP در اتر روی IPv6 استفاده کرد و با اسکن، IP مناسب رو پیدا کرد.
روی فایروال ایرانسل، برای CDN و Worker میشه از متد F&F استفاده کرد که نیاز به تنظیمات مشخصی برای finalMask، cipherSuites و فینگرپرینت داره. WARP هم روی این فایروال قابل استفاده هست و محدودیتی برای نوع IP وجود نداره. علاوه بر این، روش MASQUE/H2 با اسکن IP و تنظیمات مشخصی برای فینگرپرینت و finalMask می‌تونه برای اتصال به کلودفلر از طریق هسته اتر مورد استفاده قرار بگیره.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/ircfspace/2652" target="_blank">📅 23:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2651">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/faXX3nwNjbnth2qfggENBVfYT5W1frQiEQip3yRExpxkMP3b-Mhe9FiAUHzzAw6KJ59sI7bRJEnKmp5-VuwsHk2TF4ucSUgYme2hnQ-Tvi9gsfWjfaHUnqO_gw5AiN-qvaVpP3lKiytUXm0CgeTyubbweflcuLHlC2ICh1ukQTfOB7ivALzVIXQn3jq_QbCw05tAfcfEcJ_IMUga4y8CM4PfWxiebj3-zwsFTCbGA4PtsBk5kB5oyyfl34CvDPuEFhecWPQl90QfRkpdwgZVXhcVLgvgX2Ly5lcj-ZYD4Lm8RVL6b8us-hWVyXXsoOZbTiGQ0ZD0HfddUx217gv6aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن دیفیکس توی جدیدترین بروزرسانی خودش قابلیت تانل‌کردن کل سیستم رو بصورت آزمایشی برای ویندوز و لینوکس اضافه کرده.
در این بروزرسانی عملکرد کلی تانل بهبود پیدا کرده، مشکل نمایش پرچم کشور محل اتصال رفع شده و چند ایراد جزئی برطرف شدن. این نسخه درحال حاضر روی گیت‌هاب و گوگل‌پلی منتشر شده و بروزرسانی مایکروسافت‌استور و اپل‌استور هم بعد از تکمیل ریویو، در دسترس عموم قرار می‌گیرن.
👉
defyxvpn.com/download
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/ircfspace/2651" target="_blank">📅 23:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2650">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iC9P5iDcsUgq4NlvxGV-E1nilc5g90ZW19YhEtpflcv8fJ3_dCdowUc4cf6-M-DiQ6tIsnj1V0r_S1lQExk9FcySNyj4oHp3kuTMuq45XTwxIBSqwbEdfj6yBT1irGjGsv-8w8m_jQ1YKRwKxvs876F1vt6cYJJ6fPGN0b9h6rfTz9Un8alG5TBjsmt9Zufv1Lzk06d-noQfprfFs4kdw1rZaAVHEykdowKzqkfZ1C6fvKsx-SauYV6Z5Fz6hh0chudhALpZto2pdvrIP_6GJdPnjVUcGLCp5eKBFX8FsS5oUpmkppb--lrOzm0jhR7w_aYMID_NKXTy1k-7Mj28Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای "قطع اینترنت کل کشور فرانسه به‌دلیل اعتراضات دانش‌آموزی" فیک‌نیوزه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/ircfspace/2650" target="_blank">📅 18:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2649">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cKIEbwD6ad9kQUVoIiNhNVS4aTPndW5gYz3DQzZZPWTLqTbDV3dq9an-Y-bDM7SRJGIre4DsDl2GJAUnc8ymvUGbbR7ym12LouEOl-n9VjNWGXKL2GfpFaUadlzvU4dofThUxadS7IUt2GZE6uRU_nAw-1PNLa89nWkvb4iNpOupG79LjaVlyF01-tlTNW2DbTVf7rhZTrapRrEBuSOMQl7dNc2lrEkRSZUXFe3NgU2YBmqT4XM8Fetl33_1dPL7AvkBKniWIRIUXhFd-bKCZicGEHHf1sNjwzQXsjAzLtAdqfK0aCx9X4PCOKDWFnMs7DNB2mg4IOyMwoV8iV5-gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی در جریان اعتراضات دی‌ماه تونست با جمینگ و GPS spoofing روی
استارلینک
اختلال ایجاد کنه و حتی تو بعضی مناطق کیفیت اتصال رو به‌شدت پایین بیاره، اما اینکه بتونه استارلینک رو کلاً از کار بندازه، دور از واقعیته!
اسناد ITU نشون میدن که با وجود این اختلالات، ترمینال‌های استارلینک همچنان تونستن به اینترنت بین‌المللی وصل بشن. حتی راهکارهایی که SpaceX برای مقابله با این اختلالات اعمال کرد، باعث شده سرویس در بعضی مناطق دوباره پایدارتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/ircfspace/2649" target="_blank">📅 17:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2648">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JIRwRS-8A0EADEHCDUpRWztbyeyAULlBTnYmWM3-fuxeapYa4bqZ83D5NA_FXUh1I14aJ6org_I1OdIrDlXjymqDodIaYuJwms8xywk9axWCi7i03v8MwusLv3pwsXwK9afQiGwp7MfcJX7FmQHdEHdGFYi0RaQKDpSwoNEHXck_Ew_Ztzryo_0eRZ7PFil33K-hYnP7_HoVh6GNT4hPu3rfXuADB0valQ-r5zdC8NI-k_LlW8TJGDfiawaIoqOC4UCHRif61Y99RW1E-NtO8tiD2ERMPX6gEaxpH40Xf-gfjShp2cSHbdu9gtz5AVErfCxeoEmlCvfvObggzcJTbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا: هر سایتی که اقدام به اعلام قیمت‌های کاذب ارز کند، باید بداند که برخورد قضایی و پلیسی با آن به‌طور جدی انجام خواهد شد. /انتخاب
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/ircfspace/2648" target="_blank">📅 17:45 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2647">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NXHyZt4okl-Y9ay7fhAURyGvVip5ZonmF7gt5QQDmP8jB3aNtkisBmbAsz7N-EsSzC8cnsFG_uFF8YHf_ylZwKDQlV-ZK6n9ckpzoZuYNNAp4D6E3ruDUYiGwatACPZDb8OXosRU1RDjozJ4tyMStt2bku0PK1MEAdQP9Lv9_5531mqh24iNQ1dhYCp3KCYtNJnNIuQ9dhQ6djpbOuiwXM8rUkzBDgBke9wdLsxYS1q5vtg-e49dUDev9wD1yIilfHz44pSNzBpO1NVrjtRA3eFsVE6_jsh3YEfNy9soxThVomuAsKR3i8H0zazLqwx3k10wwlhpKA1UgojRinstUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید از فیلترشکن متن‌باز و رایگان Aether-GUI با آپدیت هسته اتر به جدیدترین نسخه و اضافه‌شدن متدهای اتصال سایفون، تور و مسک‌این‌مسک برای ویندوز، لینوکس و مک در دسترس قرار گرفت.
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/ircfspace/2647" target="_blank">📅 17:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2646">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/btaCmU0_13Q0tlqo09mTBAk5OeYnnmiYYN3MG9BCI7ObHeyiqHs6TDdRuqQsE4PoZ_urIqCG2YhhdqP1xtrJQeZXwrRE0i7ry6iE1iYCdHiTn-ey1dJacVmiNHDDOdmpNYrfeJBGwxjUAOiklAtSYlXvkiRRsm-KmPu2aXBkEh9P0_Sc9RaN6RHCKkIxF1JYq3w3IsN28lW05X0H2EJaV_UGI0l2JTSr0OUMXx2hztkNsS2zTjyuj8YKuqrtcJzxHoQZdGBI2Ud1OVUzwWqlHTORwxEJ3TSlIgNlORTBy6MYydGMrSGtuOnG5eQagiOe2nK5VZEV59LrqnCBrKiCDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس مرکز ملی فضای مجازی گفت: ایران برای اولین بار توانست با موفقیت پایانه‌های استارلینک را در جریانات دی‌ماه سال گذشته از کار بیندازد. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/ircfspace/2646" target="_blank">📅 17:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2645">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lG1ZWajRrSJ1uMOdjX20rrWmsWuuVDXL61rY5BYSRhH1zO0vm_9RAj4CRGup6Qkitr5-Bhl3x5OClVGgFgl-G_O-JfXiqZbFsrl-woNrMIeejfFIKLB6iQEkMxN7eW447dWjL6lGGfJr_e3-Fwczm9h_DEjuaEpNl3512A9DmW-TCZWBZobFqCrSBzVKs_TzVwxKCKMMwdQ-l6Pn4PDiXDPAuAkskF0eZhYwc6JjK_4ZVMI8_uqJjDZ8QRQ9572oaN1xent2CzJnDWPY6Hr-UIWL3o_4uSvQS4JzIF4tyCfPIVYd0t8CZrZCA4WoFghKH9eEvKjD8Y6zkXbAwSfn4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زومیت در گزارشی نوشته که در حال حاضر دو راه رایج برای دانلود فیلترشکن JumpJump وجود داره، که یکی از گوگل‌پلی و دیگری در گروه‌های تلگرامی هست؛ اما بررسی کارشناس‌های امنیت سایبری نشون میده هر کدوم از این جامپ‌جامپ‌هارو دانلود کرده باشین باز هم در خطر هستین. فقط خطر یکی بیشتر و اون یکی کمتره!
جامپ‌جامپی که از گوگل‌پلی دانلود نشده احتمالا یک فیلترشکن دستکاری‌شده هست و به نظر می‌رسه این فایل یک exploit یا آسیب‌پذیری قابل سوءاستفاده داره که می‌تونه دسترسی root در اندروید بگیره و رد پای دولت‌ها در نسخه دستکاری شده دیده میشه.
حتی اگر نسخه کرک‌شده رو دانلود نکرده باشین، بازم برنامه اصلی دسترسی‌های نامتعارفی از دستگاه می‌گیره که نشون‌دهنده ناامن بودن این فیلترشکنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/ircfspace/2645" target="_blank">📅 17:28 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2644">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lCWhfa3iXBqS-bZPkntonQ31JXo7xCr29krKuGare6joWPlt_Js_6WlpcyjZBdwxnGqRWoHw5e_OoXzEgJEsLQgx4MEf9XIQ1cgbOeMYDWtgOwEg7VjJ3leOT4Chmuskq7kn1QyvBnUFONy-RpNMPfQ1mLHxCA2Uot-otn4YWKQJttcByuhpHQdX-w5IKD90nK2ilRQ-0BEFkjvXerezGYjQK1BbGDyJ4Xg9TUagUDM6Mp5PDt7VLYsJLNuZaT84BLWnobtW0Z0ksK5RBamldxKh5JyJ0VlKLBv1v4fGqQID7fYK8lkOT65eQ0JrAToF43Vz5BkCc_Ek6vs6Fb3v_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از اپ سایفون چندروزه روی اپل‌استور در دسترس قرار گرفته.
👉
apps.apple.com/us/app/psiphon-vpn-secure-access/id1276263909
💡
play.google.com/store/apps/details?id=com.psiphon3
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/ircfspace/2644" target="_blank">📅 23:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2643">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lGqMrxMqQMCBwnI0bFPTTCt-Vf5XflV74Be_frAEr_wQsejLGWabksRg_xXk-phnbIBH4Ec2ZOAK88ufOwhNN6R_5vz_Cl9KLbDw4dXjwsliIY2qltBQzdSjrxbAuW7qpRbxAIfT3zBD9gBbEnpxorxaCnRjQ_21YN1e06r1UQ4InOjRxjWJVXcXQ-MDUxMG7U8MoBCmAvuX8uyqReAQwm7h1yS6q9VTgYbuZWJU0eo-8LgfmHN4jrMRpuYRQoUcM2PacLGmDmsDfS_cfwDlopLbejPuFn9whPqCK-qiArMGGUIuw3D18TB7GE698tTD5nIX6WfYGjRM7FlZs2silw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق آمار رادار کلودفلر، از ۲ روز گذشته ترافیک ایران به کلودفلر به شدت کمتر شده. اکثر کانفیگ‌ها و اتصالات به کلودفلر مثل وبسوکت و xHttp مختل شدن، فرگمنت روی همراه اول و مخابرات بسته شده و روی ایرانسل ضعیف کار میکنه؛ همینطور پروتکل UDP به سمت کلودفلر کلاً بلاک شده و اکثر رنج آیپی‌های هتزنر و OVH از بیخ بلاک شدن.
©
mahsanet
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/ircfspace/2643" target="_blank">📅 23:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2642">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AXIfUvS946GGkA1GYCyrT0JkmnQpl0RSFrr1zqwDISQ8Jr0ng8El3b57H8iC2lLcdITJMKhbxPTW62FZrcm-Jjhi7xRNh9Cc5T8S9-8DLn5iwqhkCxiUQsNeQf0f20TegK198Z0yDwqt1VS4azRFiViDo20ip8S__ph2iwHM_ukBYwekSUqCm_DThGOJgr6KQqKS3u0J7rCQqD2P2lNcnJpvHeB-lWo1fQ_8vrKHojZf0BKQlbghmzGysoRefBwXFSLVJ5RJDv6G6KVxmkgN2w8tvuM_vgobsLtl7KMTCOX9yAUW8uvDqAgW-nT-6BvT3phaJJX5YtkUP8o4RL-OTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نحوه استفاده از برنامه‌های PattN و PattNG برای دورزدن فیلترینگ
📽
youtube.com/watch?v=CnEQipAJ2hE
💡
t.me/ircf_toolbox/25
©
𝐀𝐥𝐢
👉
github.com/patterniha/PattNG/releases
👉
github.com/patterniha/PattN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/ircfspace/2642" target="_blank">📅 23:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2640">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CxI5NMCWNJ4O4z2RCYohl5HoDVcjIXfLEbpCtgBJ-iLaCyRQqsZGdA_wAsgUVNUTPrUdd8YH9agyU4RGuHxu_50EzonRsNaGYpaw3ktaOeqPMLP_2yzWU96wyEruiflyTN7GD2qbnr0LhzQY-QFIYfYoACRFygtuQLK8UrA745iiRv2qBinsYDql2Uf8DMw89ROawzAuihR9ZhagdSp6dS_m19AxfIfrLt2_e2kFvFf1allOZKUS9T1TWuM_oRjZy6X7AGLHiCHGUWEpNQ7qJqW0do5viSVX_w1n3zhRl_U9nr37XlyGA829o0sYqVOSGMuujpa_n2Ywnngin69r-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید از هسته Aether مشکل برگشت آیپی ایران در متد اتصال Gool رو برطرف کرده و محدودیت اخیر دریافت کلید وارپ و مسک رو روی بعضی از اینترنت‌ها دور زده.
اگه H2 روی سرویس دهنده‌هایی نظیر ایرانسل به هردلیلی ایراد داشت، میتونین طبق داکیومنت از فلگ فرگمنت استفاده کنین.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/ircfspace/2640" target="_blank">📅 23:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2639">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bie1lCMXbcEjqrHMZXgcw1bv_z6E4P1Ym11GyDukdx6Y2PmR5i9N2lc4RKCpzxAcD8UKbYGscSSBEIt6Ox5QtB5gak-Hmt2pEOBiU6OvEq3RvoSYIeKMmzF4pOiGTy5yN9mIgNUhlaKt01OHQ1v3nszG5_RIUzFBI9Qccb7kppviv-glxRbleaQsYfqoWZCCNKePTlWiUm2hmUHuH9W4FZz1cVBmsQ8mAdA2vOv0mQZzW47ie7qC_xB4MEPbJcCo0vEBRUlJIzYuHxYY1I0Fu-LZBx6H0d5X85trzCSfLuPYuQvCnXIcFn7Hwqu0KlH5OOPW_XiiN24ZI_tvgCxq0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱۸ از فیلترشکن اندرویدی MahsaNG منتشر شده و توی این نسخه هسته Xray مهسا آپدیت شده و پشتیبانی از پروتکل MASQUE رو اضافه کردن.
برای وایرگارد و مسک حالا یک اسکنر IP اختصاصی در دسترسه که از نویز و پورت پشتیبانی می‌کنه و میشه کانفیگ‌های این دو پروتکل رو با کلید Auto ساخت. امکان بکاپ از کانفیگ‌های شخصی، صفحه پروکسی تلگرام برای کپی و تست سریع پروکسی‌ها و بهبود Fragment و حالت Auto هم اضافه شدن.
چند نویز جدید برای عبور از فیلترینگ UDP، کانفیگ‌های جدید یوتیوب و پشتیبانی از Cipher Suite برای افزایش سرعت آپلود در متدهای پترنیها به این نسخه اضافه شده. FinalMask حالا روی پروتکل‌های جدید MASQUE و Hysteria در دسترسه و علاوه بر رفع یک سری از مشکلات، ابزار زنجیره‌ساز کانفیگ هم از Fragment، Hysteria و MASQUE پشتیبانی می‌کنه.
👉
github.com/GFW-knocker/MahsaNG/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/ircfspace/2639" target="_blank">📅 08:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2638">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v8L0EG0RhxGGXEE2FTSJpe0aLYdJFhhkz0YCJq-zpHbTc5dKQHt5hqnb9jksy5kiHBm0unM-9GmLtOc_aoWkKRHPowmM_GeHC4umBnwj9T7ENuWbarTd2Z0R7yM9ro8X0bd5njb5wiVdkhZ6y90dJ3N3wlrI9NvqaEPSEOF8xjJHQveyY8z7a4bEbyu62zcAfxhv13Kn0UwHozTKmPSlB-knkB-tklyV1O2ELZY1x4_iuat_yISQToBNZ7nm32M34MG2E210RXwVu6mJqltOVxVdYGx4Nee_WaqtJp3ng5MQ5Hu7mTY2xwQLCrIHv_Q0v15yYOSuhDvWP0X8G51mRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپل از نسخه iOS ۱۸.۱ قابلیتی گذاشته که اگه آیفون ۷۲ ساعت آنلاک نشه، خودش ری‌استارت میشه. این کار باعث میشه اطلاعات گوشی دوباره وارد حالت محافظت‌شده‌تری بشه و ابزارهای فورنزیک مثل GrayKey سخت‌تر بتونن قفل گوشی رو باز کنن.
حالا شرکت Magnet Forensics که سازنده GrayKey هست، ظاهراً راهی پیدا کرده که قبل از این ری‌استارت خودکار، گوشی رو در همون وضعیت نگه داره تا مأموران بتونن فرصت بیشتری برای استخراج اطلاعات داشته باشن. این قابلیت با نام GrayKey Preserve و همچنین Evidence Preservation Mode معرفی شده. البته فعلاً این موضوع بر اساس یک ویدیوی تبلیغاتی لو رفته از شرکت مطرح شده و جزئیات فنی روش منتشر نشده. در واقع جنگ بین اپل و ابزارهای بازکردن قفل گوشی همچنان ادامه داره.
ناگفته نمونه مأموران توی ایران برای باز کردن قفل گوشی بازداشت‌شده‌ها، نیازی به GrayKey و این ابزارها ندارن؛ زور و تهدید راه ساده‌تر و دم‌دست‌تریه واسشون!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/ircfspace/2638" target="_blank">📅 19:42 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2637">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پروژه Nexora یک پنل برای مدیریت چندسروری VPN هست، که تا ۲۵ کاربر و ۱ نود رو بدون نیاز به لایسنس و با تمام امکانات پنل در اختیارتون میذاره و میتونه برای مصارف شخصی یا گروه دوستان یا خانواده قابل استفاده باشه.
نکسورا مدیریت کاربران، نودها، اشتراک‌ها و پروتکل‌ها رو از داخل یک پنل انجام میده و از پروتکل‌هایی مثل VLESS با REALITY، XHTTP و Encryption، VMess، Trojan، Shadowsocks، Hysteria2، TUIC، AnyTLS، Naive، ShadowTLS، Snell، Mieru، MTProxy و SSH پشتیبانی می‌کنه؛ در کنارش پروتکل‌های کلاسیک VPN مثل OpenVPN، OpenConnect و WireGuard هم قابل استفاده هستن.
از قابلیت‌های دیگه Nexora میشه به تانل بین نودها، پشتیبانی از CDN و چند آدرس برای هر نود، همگام‌سازی بدون نیاز به ری‌استارت، Rule-set برای مدیریت ترافیک، مسدودسازی تورنت، محدودیت دستگاه بر اساس HWID و انجام عملیات گروهی روی کاربران اشاره کرد.
برای مدیریت و نگهداری پنل هم امکاناتی مثل احراز هویت دوعاملی، بکاپ رمزنگاری‌شده، بروزرسانی خودکار و Webhook در نظر گرفته شده، امکان مهاجرت از پنل‌هایی مثل S-UI، 3X-UI، X-UI، Marzban، PasarGuard، Hiddify، Marzneshin و Remnawave رو داره و از زبان‌های انگلیسی، فارسی، روسی و چینی پشتیبانی می‌کنه.
👉
github.com/nexora-vpn/panel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/ircfspace/2637" target="_blank">📅 19:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2635">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hysm220L9TdWF7yKsNXE9-jHhWxMLbtBnGmQF2owzK0HnekyUrO1Vh9yhgRZsdTXV-MsSGYhCV3QlHIQCn_AgaWA8I0ZNiINIerDvNzmkZPi6qqpKOSyZ9mRoRQutHYD-gbjzC8EEPb5gvKmaXEa8yZi5iDnvcMSKuUpTyr55I662DufcjAMAb-CXOc1KpC9fYlls8Wnj1n0mpEeSPhra-Ety5xxz9pCUiqb3u3j1l6-9CYf2GLMpfGbuF3TYTq4tD_CasNvWT9Y6qJ_a-BWEDKh5kAicIhzMPMjXIu5XLNAMIbgr_mFFEy1xOTpoLXp3ijFKfIqMxkTslHXDiQL1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حساب رسمی مایکروسافت در ایکس با بیش از ۱۳ میلیون دنبال‌کننده هک شد و مهاجما از اون برای تبلیغ یک رمزارز جعلی با نام $Clippy استفاده کردن.
هنوز مشخص نیست چطور به حساب دسترسی پیدا کردن و تحقیقات ادامه داره. مایکروسافت هم اعلام کرده هیچ ارتباطی با این رمزارز نداره و پیگیر اقدامات قانونیه.
©
theverge
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/ircfspace/2635" target="_blank">📅 19:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2634">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xiluaxc13ZwAd4Cu1EZMknJHd3uY1prlAqREJatAJsulSgGv9STS_3P96HpsBn_uXqNtfx9j9OZCWXjP-9rqyuWPOK_eTu69xXFv3p4GKKwWt36Jk7pI6_VNtUuw22CfMrmmzReDJXMX8kBv0_fyvrlIm-az-IgHqRsQH0vRHGzJlR-v7-g60mbVPL520WPh_UBtx2aJaxniNbHnTTl_dYUkKjBhYKGoy1W4AOdk7VuuuDHAGgzuMjhZulUB5ZyQGLZmXpAvxCOCoGMZX9HRiIJfCNtMu2yRlrKmsBpkTgfl6vyCKpfyaVeaNZPy7C7j7HuawO5uFmiC4-TL_9qETA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر میخواد تبدیل به یک مرجع عمومی صدور گواهی دیجیتال (CA) بشه و در قدم بعد، گواهی‌های جدیدی به اسم Merkle Tree Certificates رو هم در مقیاس بالا صادر کنه.
هدف اصلی این کار آماده‌کردن زیرساخت وب برای دوران کامپیوترهای کوانتومیه؛ چون الگوریتم‌های فعلی مثل RSA و ECC در برابر کامپیوترهای کوانتومی قدرتمند آسیب‌پذیر میشن. MTCها کمک می‌کنن گواهی‌های پساکوانتومی بدون اینکه حجم و فشار رمزنگاری روی اینترنت به شکل شدیدی زیاد بشه، قابل استفاده باشن. کلودفلر گفته هدفش اینه که این گواهی‌ها رو از اوایل ۲۰۲۷ وارد محیط عملیاتی کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/ircfspace/2634" target="_blank">📅 18:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2633">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rxA01vD-tBSL8Ol2qDOrly87s0P11UPljj7D7auvwfjnIZ1iMyj_839sGPvbGSqSVq6mxvRmVMfnPL5Qvcd31Zno-8b2Ml5oSm0h2NKhE43l2r8oveuh5Mh7HFNKqXd9rho7KI-LOljnvZnXKiWOJXYluwIBo-XrbsH9WDVCAqrjeILi4e71_fm_6vhS9uxizsjkbVtBEMHSZeZkQWE7Tq2JA-E8ruSINdDvzwmDEu6DcoZmQViZhDS1YThq-Qyz25K_bhrf7BJoQ3P22OKUxbWXyJuVUGbLbllHY8qf77-drBXbzwVbjltdpTt5RKT2sKmbZm_BU80uJZG9C-XPoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه از TeamViewer استفاده می‌کنین، چند آسیب‌پذیری امنیتی با شدت بالا پیدا شده که در بعضی شرایط می‌تونه به مهاجم اجازه دسترسی غیرمجاز و حتی اجرای کد روی سیستم رو بده، که مهمترین مورد CVE-2026-92370 با امتیاز ۸.۸ هست.
فعلاً TeamViewer گفته شواهدی از سوءاستفاده فعال یا انتشار کد اکسپلویت عمومی برای این آسیب‌پذیری‌ها ندیده، اما در نسخه ۱۵.۸۲ این مشکلات رو برطرف کردن و لازمه آپدیت کنید.
©
bleepingcomputer
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/ircfspace/2633" target="_blank">📅 19:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2632">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X4NsIoANWiNUkOThPrZ1MpAtQ2QFUiiTdHIuLsJLePSkPRUhRxxizYUAHUCa7Ur_WDf12oG_L0X3A3yuhcsNSoPZoMxm8UOBhdhBkm_rsiexpNjKIh0u8ub3fzlp4uILz4fhiQDiue6mAf0Nt2LvkLZuEh7hQRYq5R1ZjVYgN2MSN0nY5Pb-KnPBQt_tgZ5rOqor0Nm2Hfyxh-yyS5i6X4MbXH91GTx0Tswyp3RB3O1sQiAQJt0VxucFdXPGzOJqulcGxV7VJKJLUICX2gBz8YLMAeNR4Fl1N1ECNTMX5u7Sk4QXAIfaTTUg6zIm9lied3Himye3ucNNDsKqQAuMFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ج.ا در سال ۲۰۲۶ رسیده به راهکار ماه‌های پایانی حکومت قذافی در برخورد با مخالفان: قطع سراسری برق!
©
ArminSoleimany
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/ircfspace/2632" target="_blank">📅 18:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2631">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lXKCmVvmgqiSbOG4WcxlRnk2BEhSCR_EN67Mhs63k_21mDbumI_JzNo9-8kzrBCQWCjZtPHsSNOjHlzldj864qJQOm9xLmL6uHvtTEY8YVYMQiPsZLXigkBzKF3dPxjGsiFb1_yJ0lKmb2fEm3I99aN2Rod8-MXE5_R3HDBQ8ab_t3C27VypS9St8aR5BoPsBbEHIDbil5wICrRszT4A3OCbPCmYLpnVsg0aZm0BoQ1dv9Gtg-dbgmK8qAdSck_bG_69sSCnE_8TRvDr94Jpu6jLcE4nGNOyDWbYUb44Y7vM6eFCB4cWHk1MZJ3quy6brQ0vcTOkzdTpRkc8svKKWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتیجه این و اون خبر چند وقت پیش در مورد تغییر شرایط استفاده letsencrypt می‌شه گواهی ریشه داخلی و پایان بازی. از مسائل فنی اجرایی صرف نظر کنیم، بحث‌های مهمی باقی است: «حریم شخصی» و «امنیت».
در کشوری که با مداخله در پیامک احراز هویت ۲ مرحله‌ای حساب کاربری مردم رو تصاحب می‌کنند و پاسخگویی هم در نبود قانون و ضمانت اجرایی نیست، امکان جعل گواهی برای شنود به خصوص برای موارد بدون SSL pin هست.
©
Hamed
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/ircfspace/2631" target="_blank">📅 18:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2630">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qzb2EUFbmG-5GfYrw72hnqHuK-vMKHKEGwIH3Z5tXy55mJE5Gjd3VP0XM-4Wm5Xbv_folIVfHVxQXa7N9miFM04EDkftxICTyiNNeKdnqH-Q_DeN4Ozj71PfQLq0ZRoT6AdwmddLHkHgRgkWu7l7Lz5i1YZqJmmP_9k8b6xRM4L0kZDgVrrhG7L85px3ytlu0MAJr9lZ_CViawCr_GzdOXqjXHqmG7PaQIwQ9tZdFGMhUZubooJo1iWd3bnoT07WP3GFBwpQJFtofOmnF5XwavXS4frA3kEAlkeIuidi1NOx3gdrb3o2oAzQJxEF-_orf5gjxLUG2GKyhfb4qTJo1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راهکارشون برای مدیریت قیمت تتر چی بود؟
نمودار قیمت رو غیرفعال کردن!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/ircfspace/2630" target="_blank">📅 18:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2629">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">کاربران در چند روز اخیر قطعی، ایران‌اکسس شدن و اختلال مضاعفی رو در اینترنت تلفن‌همراه و ثابت گزارش کردن و میگن آشغال‌نت چندروزه که شدیدا اسهال گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/ircfspace/2629" target="_blank">📅 07:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2628">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Eviwt1QlwhCap5U2QOO-r6Db8xNWtU451fvZejWixdZwlawmvPek034CgXZ1X_7sAC3loCqps1YnrDfUjdnu-wrLNi7s-lcVRwyJIUkQR157QiM7Z4DI99abb8zs8xThR89eaAAd5kUybxWrgnfLlCzvJLoL5swCCVN2eXLiW2zmXV0yGKVn-OjpQ0oW_l4G_9etbK6QJA6imFGvCty9qqURrdR72oAnSueliaCH9uFfo58ticI0X5RNuW5JygKsz0YAq8uHOB5qSQCWLQXDViJbaJOV0Hee8FwflfK9mMa21SMQjz1fWAH8T6PSDDa7Gj1JWT3pftBADEqP-hGoWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش Group-IB، یک بدافزار ویندوزی به اسم HEAVYGRAM شناسایی شده که از تلگرام بعنوان کانال ارتباطی و کنترل (C2) استفاده می‌کنه. این بدافزار از پاییز ۲۰۲۳ برای هدف گرفتن روزنامه‌نگارها، مخالفان و منتقدان جمهوری اسلامی استفاده شده و می‌تونه از راه دور روی سیستم قربانی دستور اجرا کنه، فایل و اطلاعات بدزده و حتی از صفحه‌نمایش اسکرین‌شات بگیره.
نکته جالبش اینه که مهاجم به‌جای سرور C2 معمولی، از بات‌ها، اکانت‌ها و گروه‌های تلگرام برای کنترل بدافزار و خارج کردن اطلاعات استفاده می‌کنه. Group-IB در گزارشش ۲۹ نمونه جدید از این بدافزار و ابزارهای مرتبطش پیدا کرده و با اطمینان متوسط این فعالیت رو به گروه حنظله نسبت داده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/ircfspace/2628" target="_blank">📅 21:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2627">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اتفاقات امروز و تصمیمات هوشمندانه‌ای که برای مدیریت اقتصادی کشور گرفته میشه، کله هممون رو خراب کرده احتمالا.
ساتوشی می‌تونست وایت‌پیپر بیت‌کوین رو خیلی کوتاه‌تر بنویسه: دست به دست هم دهیم و دستگاه چاپ پول رو در
ماتحت
بانک‌های مرکزی فرو کنیم.
حالا تقاضا رو سرکوب کن، حساب‌هارو ببند یا سلطان فلان و بیسار رو اعدام کن، این باتلاقیه که خودتون درست کردید، توش دست و پا می‌زنید و ازش خلاصی نیست. این وسط، عمر ما هم رفت سر ایدئولوژی شما.
©
GrizzlyBTCloverr
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/ircfspace/2627" target="_blank">📅 20:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2626">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hPA9IQW4Z-6JQ65uzFBwx12TEc1WcIEoeuqgPfkJOkpiwe-V3_DobUvPwphfwwT0lfYXUU9YK9Tf4YgJ9rgvc_3iEKyonuckVoAX3GNQdkin_X_CEvyVgPcNZ1wVckMt92A_NnFFr4P4Oh_T1eVvffAL0h3nuN57HWpP_tILwpc_ryYZm24Iid2c29U1bUO88tQSXw3F0jhz8ZLGoAuAhEE3glBITxBM4pKWfZVlwZ8BQbixm99I-YLX_LToojl03Tx7trW4JOM9mgh37XmeAfnh1bGSgTWbhbvvCB8-oBDxyWLgv7o98FLtP8csDdAV7K8IZm9OhXSd-Lpym3wBHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از دیوار چنین پیامکی گرفتین، ازش بی‌تفاوت رد نشین!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/ircfspace/2626" target="_blank">📅 20:13 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2625">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hT3G2k_SYCDwAPqROMQ2KYxyolFTh35E73UqNM_s4jUzYij9UU8dFO-DoYEQJrJYKbsLAC5Vo9zbykUVXc6y7lZ6sarMN5dK_derTf78WydI6tFMBiqh6MdoVmKcBRsGVoTy8RqyfqFEvX_NV6s7QoKbHvU1dFZaFdOj13dIZI1I3zYPoSiVD4TmlfdFDJc3OzDmn3TO6JG2dgRCc8bmHqP4UB1DKluLnvTxHBFqHU0QrsmGuLQtPckukxN78gCUzwrJjbYp0Y7yp4kxuyMs5G98PssOziKAa-Uw0n_Gg_p8OoSf2kcMf86o8uFKK_JgR4X_ZD7SaA5g_x1MojZJvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرامه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/ircfspace/2625" target="_blank">📅 20:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2623">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">مجموعه‌ای در حدود ۷۵۰ هزار رکورد از اطلاعات مرتبط با کاربران صرافی ارز دیجیتال والکس مربوط به سال‌های ۱۳۹۷ تا ۱۴۰۱، در فهرست فروشندگان بانک‌های اطلاعاتی غیرمجاز مشاهده شده.
این داده‌ها شامل اطلاعات هویتی مانند نام، نام خانوادگی، شماره ملی، تاریخ تولد، شماره تلفن، آدرس، ایمیل، اطلاعات مرتبط با احراز هویت و همچنین اطلاعات مالی از جمله شماره کارت بانکی، شماره شبا، اطلاعات صاحب حساب، آدرس و موجودی کیف‌پول‌های رمزارزی و سایر اطلاعات مرتبط با کاربران است.
افشای این اطلاعات می‌تواند زمینه‌ساز فیشینگ هدفمند، کلاهبرداری مالی، مهندسی اجتماعی و سوءاستفاده از اطلاعات هویتی و بانکی کاربران شود. به کاربران توصیه می‌شود در صورت فعال بودن کارت، برای تعویض آن اقدام کنند، نسبت به تماس‌ها، پیام‌ها و لینک‌های مشکوک هوشیار باشند و از ارائه اطلاعات شخصی خود به افراد ناشناس خودداری کنند.
©
leakfarsi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/ircfspace/2623" target="_blank">📅 20:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2622">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s_uTZoN5jWkhiAIkkfYawDoN94UL6SdUFYeI5Mk2ManYQnZ-0zMBJgo2GtcyEXWbFk9maK2xGZjllAuu7YXwkqwqx-Xz10Cm20ElPIdMztgkUbhqOfil-c08I-0rzN-bJXmKxLfTPs6Yp7ZwU9i_MR3wuI9aIwWwU-YwJS9pe49IGe_jn3vSaM28_TFkRlNkjZZlKYgwa_yKb7aaOwd_lRHIylk_H7dm7NLPsgrB8SgnGcNV6xlJbkmVSfgn3G2m4ASU5M3iG0ZIyOLBqoxknM0K32sEM7IxRCsAh4AfCfxo0LxyHzxeS04GGDwmI6pfHjizgF13pTHrTt47-WYwug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر قطع‌ارتباطات گفته "فراگیری استارلینک میخ آخر را بر تابوت حکمرانی فضای مجازی می‌کوبد".
۸۸ روز اینترنت رو قطع کردین و نگران حکمرانی فضای مجازی هستین؟ بابت ده‌ها هزار خونی که ریخته شد، باید منتظر کوبیدن میخ آخر بر تابوت ج.ا باشین!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/ircfspace/2622" target="_blank">📅 19:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2621">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R1rsln37IfvkeeoAq5HOoHMxQ4Uj0dSASj1agh1f8a67SKrei3tnCcUC-b_eKw2_g0ta8yYLJsDJ2OY_vs0RktjgcBdbpbWcL5WzFtLx9-Bn3qMyov5qaFxYxangantFFy1tOTZ36rR-Llot-igep5m-3RIBLLRrhD1Di7y8F0oQ4Xu48R01mM7rFRwK4jyGOy7ci62JzELg3zu5jAUL6l3JhtoeO7HmwmiMvRrkCARRKBgBtQ4mJN55EYjoKC6NP1eAh88zxwUvbh2I9tYkqZdJxPShZKHENsBbFz5HXssSovR4RrfkK1v4vc_NzahhjeNLPdlW_6NDA11MjOEkqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک مرکزی با ابلاغ یک بخشنامه‌ی رسمی، ارائه‌ی هرگونه تسهیلات بانکی برای خرید طلا، ارز و انواع رمزارز را بطور کامل ممنوع اعلام کرد.
این بخشنامه بر ممنوعیت مطلق پرداخت تسهیلات، چه بصورت مستقیم و چه غیرمستقیم، تأکید کرده و مقررات یادشده شامل پرداخت وام از طریق شعب بانکی یا بسترهای دیجیتال برای خرید طلا، ارزهای خارجی نظیر دلار، رمزارزها و همچنین فعالیت در سکوهای مبادلاتی مرتبط با دارایی‌های دیجیتال می‌شود. /تسنیم
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/ircfspace/2621" target="_blank">📅 19:52 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2620">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kzQiqetsIbxFOk756djHlvifZcyRkIuZL16rOSqolpt2vNnGbM4-lJHpIlmNiYZxjBsMBHgVdboUgv9iBpVeM-Pa4ICIC6CafXdytvFSaSVpVLCNe5for7NSKUDYL5807nSe66B-CTUpt6tCs9ioVDAS18audVx5VZrJkT1CBVJA9LZHrqLvJrPR_kCApCyxwQLUi1vETF_d2L7ahKlzsq5XCwRQmoW7h9rYHvluFwN5rfsj8IMiSaV2httOVj8X5fRH6-QHFfrwdhIfmzbKHm808XlwZM2S3l3os1c3KSK4Z2YPb1mEv6Hyg3i_f2jVeYzMgdSjqLCNkD-5Um_0DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت تتر به تازگی اعلام کرد "به مسدودسازی نزدیک به ۵۵۰ میلیون دلار دارایی مرتبط با بانک مرکزی جمهوری اسلامی و شبکه‌های تحریم‌شده کمک کرده".
الانم با عبور دلار از ۲۵۵ هزار تومان، صرافی‌های رمزارز (با دستور مراجع) معاملات تتر رو از ساعت ۲۱ تا ۹ صبح روز بعد متوقف کردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/ircfspace/2620" target="_blank">📅 19:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2619">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">هم خبر تحریم ساخت ایمیل برای ایرانی‌ها توسط گوگل قدیمیه، هم خبر مسدود کردن ۶۰ اکانت مرتبط با صداوسیما توسط گوگل.
فعلاً اون لجنی که توشیم هیچ تغییر جدیدی نکرده
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/ircfspace/2619" target="_blank">📅 07:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2618">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KyTa4AiNfBSEGFdA1u5zHirf7mMIhVdQGSTxbYre2j3QOLhO78fp4gXom3tUUEooQd2bS1k0C3kf56CVMRepaw4OCEu0ZSOkeI5VFT41DwxPbiKKcgyKbz6ptCdVGNBzUH9-qwk81AZd4J2oQbjS45rs399ONWeCb7XZz_IOxyhWrce3Q6yBDDfy36n1kJ-IrY3aGwN_jaj2pxL42XTEWwJIKM_bnqapJA__zPjVChaQ5J_ADNcVyS8aJD-CIFVqbvzqW_DBb-uJ2UZpdLyZqh-DBo7y_mfr2QUudqacdY-OGxg4phAo9119q2efMZ6k3IQ1trDG3KzGL6Ho_RHGhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ sushTun یک کلاینت متن‌باز و رایگان برای هسته ایکس‌ری هست، که از پروتکل‌هایی مثل VLESS، VMess، Trojan، Shadowsocks، Hysteria2 و WireGuard پشتیبانی می‌کنه و تمام ترافیک سیستم رو از طریق تانل ایکس‌ری عبور میده.
یکی از بخش‌های کاربردی این‌برنامه که برای ویندوز، لینوکس و مک ارائه شده، مسیریابی هوشمنده؛ تا بتونین مشخص کنین ترافیک ایران، روسیه، چین، تبلیغات و دامنه‌ها یا IPهای دلخواه از تانل عبور نکنن. امکان تنظیم DNS، فرگمنت برای TLS، Multiplexing و چند قابلیت دیگه هم وجود داره. حالت کم‌مصرف هم اجازه میده ترافیک‌های پس‌زمینه سیستم مثل Telemetry و آپدیت‌ها مستقیماً به اینترنت وصل بشن و از پروکسی عبور نکنن.
👉
github.com/soroushdeimi/sushTun/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/ircfspace/2618" target="_blank">📅 07:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2617">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vdFXPfukdX6DEnZNQLlPN8GaKZYZJRraOT_8SR4n7NY8pZqhOm2Ul22h8iKmNxRi5077BvPdtEjnXg_WoWjajM6QQYftiTshGMzYO1SIHISSfMPcgZuPB5OEuUGlf1ffSgv7p_V1O0-kEESYgOo8pNnbVAamXrCeSCVwlYOYzyg8bKb2mskAg2p1UvsxCGsH8mz4F3QxkegROpAxJ8Zj8HVKZi2LlCnZtwtGKa-Ue7Bl4ot8xd5jROKJnHYwaPMMqZU8fPQT12N3OAzndFprcaN2LR8HsdaFJ6hvejGefxv_hx6uX2c0nyzLe-uW5f2V7siTIdbk-4MgEEEmV_fP-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت Satelite یک اپ پروکسی متن‌باز و رایگان برای اندروید، ویندوز، لینوکس و مک هست، که می‌تونه بین هسته‌‌های sing-box، Xray و mihomo سوییچ کنه.
از وارد کردن انواع سابسکریپشن و کانفیگ گرفته، تا Rule-based Routing، پراکسی‌چین، DNS هوشمند، System Proxy و TUN رو پوشش میده و یکی از قابلیت‌های جالبش، حالت Multi-Core هست که اجازه میده چند هسته همزمان کنار هم کار کنن؛ مثلاً سینگ‌باکس هسته اصلی باشه و بعضی پروتکل‌ها رو به ایکس‌ری یا mihomo بسپره.
انتخاب هوشمند نودها، تست تأخیر و IP خروجی، مدیریت DNS و Hosts، تشخیص اتوماتیک پروسه‌ها و اجرای دائمی در System Tray هم از دیگر امکاناتشه.
👉
github.com/zn0wii/satelite-proxy/releases
💡
github.com/zn0wii/satelite-one/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/ircfspace/2617" target="_blank">📅 07:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2616">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cvkSTT2pqhsf6ZclUzOdZchB1Fq0UEtM2PzkF3AZRS-FCEQdYYT1d0Y5n_yA7iE2OBIZgt56JXSp7gcIEI5XdzAIUHRIMiECxvS7hbsIEacCCO9rYqKEkMUNYI5bIksBgxVwICoLUvZnnaJ00BXiXHocDBOEj4wPC3SrCHGGoBCC32HcT2s6rNyzmqzDMFOSFwFBMf9krF1KjNzyqDu8iNRmGkuCz191YtwPGoszskoJi9abdk1nPi2tOvAqKARpHQC3tr0DSeW9oeI6mFqznnPTUSVQdpIRmy0bYRNXSD12lD4CylqcRGksqPTajKcBBfMKHaNSiHBLHEEXSuH3Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی فقط دسترسی به شبکه‌های اجتماعی را محدود نمی‌کند؛ محتوای حساب‌های شخصی را هم زیر کنترل می‌برد.
شماری از کاربران با انتشار پرچم حکومت نوشته‌اند که درباره فعالیت‌های «غیرمجاز» توجیه شده و تعهد داده‌اند در چارچوب قوانین جمهوری اسلامی فعالیت کنند. پیش‌تر، انتشار لوگوی پلیس فتا در صفحات اینفلوئنسرها و کسب‌وکارها نشانه توقیف یا محدودسازی آن‌ها بود. حالا انتشار این تعهدنامه‌ها، نگرانی از تبدیل حساب‌های شخصی به محل نمایش اطاعت را بیشتر می‌کند؛ جایی که مخاطب نمی‌داند آنچه می‌خواند، انتخاب صاحب حساب است یا حاصل فشار بر او.
©
filterbaan
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/ircfspace/2616" target="_blank">📅 07:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2615">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">معاون سازمان تنظیم مقررات و ارتباطات رادیویی گفته "حجم‌خوری نداریم و بخشی از ابهامات و برداشت‌های کاربران درباره نحوه محاسبه میزان مصرف ترافیک اینترنت، به وضعیت ثبت اطلاعات محتوای داخلی در سامانه تعرفه ترجیحی مربوط می‌شود".
خلاصه: حجم خوری ندارن، ولی باقی چیزارو قول نمیدن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/ircfspace/2615" target="_blank">📅 07:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2614">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GJCXhxmXYrzR9L24Wm23Hrw3LJ51uNBDQJqXA7g0IKEQvJni4NEUY5oyMrE-CD_QCw6u_HOUkp00wTRiKlcEaD7ZauMqipznu5XAKI9JnngrUsiOmeNvk-DM6gCf4py3V3KfKooHSS5CPc9aZ4e778TCe8uWZH61wR5qaKZe2oEZXA96atwe6ZNxaPAiQ05jeoDfECUkguXkweXO_78dSx0ztd2dV9vDO5ya7uCpNTH4XptjYiM9jmOKawY7iyzSsemhTPE7KjF1a6wywkEwyW92BDKA1TA1xsvK9xWYOIOKGuzhQoF4B4K2S7ialhPSgSmJLofFxk8rXdjrC-6i0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش Qrator Radar، شبکه همراه اول با شناسه AS197207 در ساعت ۱۳ روز ۲۹ شهریور، بطور ناگهانی ۱۹۰ پیشوند شبکه رو اعلام کرد که باعث ایجاد ۱۰٬۸۶۵ تداخل مسیریابی با ۱٬۵۲۴ شبکه در ۱۰۰ کشور شد.
این رخداد که بعنوان BGP Hijack ثبت شده، در ۲ مرحله اتفاق افتاد؛ مرحله اول حدود ۸ دقیقه و مرحله دوم حدود ۱۵ دقیقه طول کشید و حداکثر انتشار اون به ۱۰۰ درصد رسید.
وقوع BGP Hijack میتونه باعث قطع دسترسی، انحراف ترافیک، اختلال گسترده و در بعضی شرایط شنود یا دستکاری ارتباطات بشه!
البته در این‌مورد مشخص نیست که بصورت عمدی بوده، یا خطای فنی ...
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/ircfspace/2614" target="_blank">📅 08:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2613">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">بانک مرکزی نصب «گواهی ریشه داخلی» روی دستگاه مشتریان را یکی از راه‌های ادامه خدمات بانکی مطرح کرده است!
اما مسئله فقط رفع هشدار اینترنت‌بانک نیست؛ اگر این اعتماد در سطح کل دستگاه ایجاد شود، می‌تواند فراتر از سایت بانک اثر بگذارد و در شرایط مشخص، زمینه رهگیری ارتباطات رمزگذاری‌شده را فراهم کند.
مرورگر زمانی گواهی یک سایت را معتبر می‌داند که زنجیره آن به یک مرجع ریشه مورد اعتماد برسد. اگر کاربر یک ریشه داخلی را به سیستم‌عامل اضافه کند، دستگاه ممکن است گواهی‌های دیگری را هم که همان مرجع صادر کرده معتبر بشناسد.
خطر زمانی ایجاد می‌شود که آن مرجع برای یک سایت گواهی جعلی صادر کند و مهاجم نیز بتواند در مسیر ترافیک قرار بگیرد. در چنین شرایطی، مرورگر می‌تواند بدون هشدار معمول به واسطه اعتماد کند و حمله «مرد میانی» امکان رمزگشایی ارتباط را فراهم کند.
نصب گواهی ریشه به‌تنهایی به معنای شنود نیست؛ مسئله اصلی دامنه اختیاری است که به آن مرجع داده می‌شود.
البته راه کم‌خطرتر وجود دارد؛ اپ بانک می‌تواند فقط برای سرویس‌ها و دامنه‌های خودش به یک مرجع داخلی اعتماد کند، بدون تغییر فهرست اعتماد کل دستگاه.
پرسش اصلی طرح بانک مرکزی همین است: برای حل اختلال خدمات بانکی، چرا باید اعتماد یک مرجع تازه احتمالا به ارتباطات خارج از بانک هم گسترش پیدا کند؟
©
raaznet
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2613" target="_blank">📅 07:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2612">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HaX8EJ-z7atUCeHc77hvItIw-x3dnvmdN5HGIdWgMsZhJG_2XHF_6ysdEo7Ki1Z0Wb-lm_W_ocJR6vVc-iF_RnfVG_jWUWys3pcWU_624bKT2vhBLXKe38uUVKASfnMeGEQnZWw7tgeHUFb11fyWyBjqk_YcEpvhSrb9wxlrlpydcpjjGTF2JkH5G2C_S7gg7YmT6UlXmHd6kk3caqleWEBj-mRoGlBtxRp5TMO73TLwu_NA__vMErWTaYwG-UO1sxPTBByPtk9qYko8ss4HIF1rzVZ5qI5BvU6U3saJ4jxB56p4hHj0WuzuQgFs-IXyGCP-IZbHN_h30zI3GugXOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراقب این نوع هک باشید!
یه صفحه جعلی شبیه Cloudflare میگه برای تأیید ربات نبودن، Win + R رو باز کن و Ctrl + V بزن.
چون شبیه تأییدیه‌های معمول کلودفلره، ممکنه طبق عادت انجامش بدید، اما در واقع دارید یه دستور مخرب رو اجرا می‌کنید.
©
milad_joodi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/ircfspace/2612" target="_blank">📅 07:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2611">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uovdoJYi9ErfIHQgAuTd78NTnMo1HNY_uqwoLh0blvEkvIEvUjMpS0re4fGmn5ngaTfTvz8ZmH-yH3xzEPyaf04xWEn_cIPU-TmYPIKuMXfYagf_ATHK6OJSDC9WeV10TjPRn8Ckg3z3XCN_z4uYz2psvIZrKQzmA3culJrbpVllTOUVtX_Ac8uwF5eUvXu4-SpIfF3RrhuOOYHN8TlXYsXL3D3IxOY4qU4bQko2T4XzfVYNpvywR7QyWEy-evAfijvlWmhI0__9w3EHmRkX7bimwiPoe7qbpKCJcJwOSHrMPQqOeymHNgxAnlvfWVCkOmzyDt9pGuDXnFnAlSjxGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زپتون یه موتور شبکه‌ی جدید، متن‌باز و بدون وابستگیه که با Zig نوشته شده و برای کار با رابط‌های TUN طراحی شده. ایده‌اش اینه که ترافیکی رو که سیستم‌عامل وارد TUN می‌کنه، مدیریت کنه و اون رو به ارتباط‌های TCP، UDP و ICMP تبدیل کنه؛ بعد هم ترافیک رو مستقیم یا از طریق SOCKS5 در اختیار برنامه‌ی دیگه‌ای قرار بده.
پروژه Zeptun امکاناتی مثل پشتیبانی همزمان از IPv4 و IPv6، NAT، مدیریت DNS، مسیریابی خودکار، فوروارد ICMP و پردازش چندصفی TUN رو داره و برای Linux، Android، Windows، macOS، iOS و FreeBSD ساخته شده. طبق بنچمارکی که روی یک رانر گیت‌هاب گرفته شده، زپتون عملکرد بهتری نسبت به Sing-box، Hev و Tun2socks داشته.
این مدل هسته‌های مستقل، می‌تونه برای پروژه‌هایی که نمیخوان تمام شبکه و TUN خودشون رو به هسته‌هایی مثل سینگ‌باکس وابسته کنن جالب باشه؛ مخصوصاً با توجه به اینکه استفاده و توزیع کدهای پروژه‌های دیگه می‌تونه الزامات لایسنس و کپی‌رایت خودش رو برای توسعه‌دهندگان داشته باشه.
👉
github.com/Noisemux/zeptun
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/ircfspace/2611" target="_blank">📅 08:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2610">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rzv1lrzZ7vLOHw6dYpOALtX8pvCqiY0Sw644yZ70Dbc4Kr6o-Pe9CWFHHWTGXP6p_ZJ278Laj2ak65UCtDbz4WkPN_SX4J5RufAJ1olQO8RNq0uY8lFrYqcOZ8H0zLJcXNNbEl5KfzrZolOPnPRdVD7oIr0C8aRct8Cd-_2BKlSZISyVUcHQoEeZXRtvRYHKupiiIs08y2kkvwz5QdOwMk6MA9V96RTZ0RUNMwu5RmTTA_ZmhxNLWbmbcPyVKd_p1YY3Gh46iVwdQbF-uiyfiOaoOjzT-SijOXPqnYHF_FtOFgy2YrfskEZojSZKJ4vfBgCIAnSYQ1GKubqOAPBW0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای، چه گوگولی
😄
فرمودن "مجلس بدلیل پایین بودن کیفیت دسترسی، با افزایش قیمت اینترنت مخالفه و انتظار داریم وزیر ارتباطات از حقوق مردم و افزایش سرعت و کیفیت اینترنت دفاع کنه".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/ircfspace/2610" target="_blank">📅 08:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2609">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SGrDubV1vkAEzHnj1JvBUMHeAMA-p8qtGK1a62AbrpIkN1fL6blEFTp75dvQLimu13I9dpjE0GT4-ja70Cr--pfHHhzXw5gWbGRhd1L31AIsRmeACSuk4AE-_JZJL1vNUDz4NqueI1pNXRpWQucou8Vp-mdn66aOsJjUPxnMJfXxGJ9sxwrhmGd8xkegtRa0H6Mxu9F2nFOBvksu1NWdjHLRSH5ffzcFwvD8WqLDNJNkTiIN_2Z7oIJbdO2h2PhbER9sqbdGoWcR1-Rqxw6RUQ0r6Gpugw6LkCaBjCVzvNdkR9kyng3uuoSqoXSq34tQUdfWXN1ymhSlGqb0BGf4aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکریپت Google Flow Helper برای اجرا از طریق افزونه مرورگر Tampermonkey ساخته شده و کمک می‌کنه محدودیت‌های دسترسی به Google Flow برای کاربران ایرانی دور زده بشه.
این اسکریپت درخواست‌های داخلی Google Flow رو زیر نظر می‌گیره و وقتی به پاسخ مربوط به تنظیمات و محدودیت‌های سرویس میرسه، یه فلگ مشخص رو پیدا می‌کنه و مقدارش رو از false به true تغییر میده. بعد پاسخ اصلاح‌شده رو به خود رابط Flow تحویل میده؛ در نتیجه فرانت‌اند تصور می‌کنه اون قابلیت برای کاربر فعال شده و محدودیت مربوطه رو اعمال نمی‌کنه.
این ابزار VPN یا فیلترشکن نیست و خودش محدودیت شبکه یا فیلترینگ اینترنت ایران رو دور نمیزنه. آدرس
flow.google.com
باید از اینترنت شما قابل دسترس باشه. این اسکریپت بیشتر برای مرحله بعده؛ یعنی وقتی به Google Flow دسترسی دارید اما خود سرویس بخاطر محدودیت منطقه‌ای یا تنظیمات سمت کلاینت اجازه استفاده از سرویس رو نمیده.
👉
github.com/maanimeisam/Google-Flow-Helper
💡
telegra.ph/Google-Flow-Helper-09-20
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2609" target="_blank">📅 07:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2608">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HNomO3LXruj-FSXgmHDiiztHHN7gOna9buuVJ72yv3rZRs_NfuEnl_iM81eD8HElZNnKHrMioZfElBxAiVbq74dmjUGgyjM6_yTbTSFZ6TkTFfBE7_M303GcdGKjK9TkufWSaCt7nbAyRZnMMCqWV7Brhk0NllVKnk6GQ_-R64xIyt2PnTA7-erWyYnIep0rhx5_gW3Vo0dI2OkoxVhVoQNiIs-8rthEj0asFrIEBxSTsDaHlJnN_0MpQ-v3wCqet4iFt_GRjZgkZsNgce5Pecin_aLO-ZjN4rWxFZ84ALHZyXqWD2PpiWEwxVR5AZciXyWuN35c2lGjW0qqDr1vcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحقیقی از TechRadar روی نزدیک به ۴,۸۰۰ اپ VPN اندروید و iOS انجام شده که نشون میده تعداد زیادی از VPNهای موجود در گوگل‌پلی و اپ‌استور، اطلاعات شفاف و قابل‌اعتمادی درباره سازنده و سیاست‌های حریم خصوصی‌شون ارائه نمی‌کنن.
در این بررسی، ۳,۳۹۲ VPN اندروید و ۱,۳۸۷ VPN آیفون بررسی شدن. فقط ۶۱.۴ درصد از VPNهای iOS و ۴۰.۸ درصد از VPNهای اندروید تونستن تمام بررسی‌های اصلی اعتبارسنجی رو پاس کنن. بعضی از این اپ‌ها از آدرس‌های رایگان Gmail، سایت‌های ناقص یا غیرقابل‌اعتماد و سیاست‌های حریم خصوصی کپی‌شده استفاده می‌کنن و اطلاعات کافی درباره سازنده‌شون در اختیار کاربر نمی‌ذارن.
در نتیجه، صرفاً حضور یک VPN در گوگل‌پلی یا اپ‌استور به این معنی نیست که اون برنامه معتبر و قابل‌اعتماده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/ircfspace/2608" target="_blank">📅 17:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2607">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j4bygXEeW7Bt_v-EWR4sRpcRv782gTwLkUGnxFxe5O8m-y9JNUIGOdMdKm59wBCpfRULQj5JoafZLjeIjhJqeP3AtXqEM-Jzt6R516ALG0XiHswmCRK0ndwdG0ATKKVtYA4NlbSkwS3mc7deRfvcjJ6Wf_f1GgQLLMGLCnANvkXZ9DmVvrkuX8vJwrPVg9rT9ss8jFc6VoufPALrlfp0DRVslwaNCBywz9JJ55xpG_9O9P9GpRH2ptruw1IwrcB8uNQFcN4EUSs5kvFvNjre0SQUsrhq9ORPa0m00S935OxOohbSB2xflVmZMICPAShPYqegjObDGw7lJoEKERyDfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عکس مربوط به مسابقه CTF بلوبانک هستش، که برای اینکه چالش‌های مسابقه با Ai Agentها حل نشن مورد توجه قرار گرفته.
طبق تصویر، در هدر یک دستور داخل Response گذاشتن که اگر یک AI Agent در حال تحلیل پاسخ HTTP باشه، سعی کنه اون رو بعنوان دستور خودش برداشت کنه و به کاربر بگه چالش قابل حل نیست و اصلاً آسیب‌پذیری‌ای وجود نداره
😁
مسابقات Capture The Flag، یکی از شناخته‌شده‌ترین مسابقات حوزه‌ امنیت سایبریه، که شرکت‌کنندگان باید در سیستم‌ها و برنامه‌های از پیش طراحی‌شده با آسیب‌پذیری عمدی، به دنبال رشته‌های متنی پنهانی موسوم به فلگ بگردن و با کشفشون، امتیاز کسب کنن.
©
Maji_Call
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/ircfspace/2607" target="_blank">📅 17:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2606">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EjoR8M4SoSPa6PQv6viF6zm29H8prqmU5m76Mga3yXoYwG1ER1QO9H_Rs3bJhcvvnIe0A3I6r11KMDO7niGlyes3S59LAuYIR4NKDQirZ3LmoJloYn_xFCPQjumvnv39_PXcRN0SEXKVhZCp3W02br4aqavbGH7VVQiZRzSJoPkusAs93qFfWd64MbIJFBLkmAaez90-8VT4UbHqSnaPrGR1LewiidH-IgPmTqfhv4EbRPqbOEqNvj5EaI3lI4hDHxZklwbkD_sFK8iDf220Ite1CWhIYJB54qzbw4IASWmKszM-nIX15Sv2RyRdrjSzjJ0k5PbB3BPVhVJzvwaBXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از ویژگی‌های مهم Tor VPN Beta، ایزوله‌سازی برنامه‌هاست و هر اپلیکیشن IP خروجی مجزایی دریافت می‌کند، تا امکان ردیابی رفتار کاربر بین برنامه‌های مختلف سلب شود.
👉
play.google.com/store/apps/details?id=org.torproject.vpn
©
PasKoocheh
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2606" target="_blank">📅 17:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2605">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/coC46wyucmOdvJ7r1WdGNfRaoZA6s6kARJe_geEpohGsEHvF5nnMWe2rzufmqOAFHo2ZqRgExhUyK221SNRdgumg_D9rGnErx6GoR2z5c_UCLXnkcha6sG_Z3yZrSJ9zv_YjzEOXLGchW0pUPe-_soKZy77qiHfsoEpcWxEGuD_pLoXXaNRgGJJNpYwf_9FMH4UMxbGIg7dT5MPkKuLN9Wpjfv601KifLBLLB-VumTFFysxitGTEBo4SRQ-6g0Y9NtcZ-RuqoHD6V_1gHF3iTZNbsEpj0M1-oB0Ekwo8ueeZVKwJFjIUSXlqLi6uP6okqAHGXlxWmZtxT7v3Oc5CuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کپی میکنید حداقل اسمش رو تغییر بدید :)
تصویر مربوط به نسخه وب ایتا هست.
©
Ralireza11
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/ircfspace/2605" target="_blank">📅 17:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2604">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ایران در جدیدترین گزارش اسپیدتست نه در رتبه‌بندی اینترنت موبایل و نه اینترنت ثابت حضور ندارد.
تا ماه گذشته، ایران فقط از رتبه‌بندی اینترنت موبایل حذف شده بود و در بخش اینترنت ثابت با رتبه ۱۴۰ جهان قرار داشت؛ اما حالا در گزارش جدید، رتبه ایران در هر دو بخش حذف شده است.
©
itiransite
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/ircfspace/2604" target="_blank">📅 17:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2603">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QlLGr3aRSnQg1Wu28nO4wFgkVn-He2pv_Sm40KNk0wkZbi2NoxbkcIxutH6-LKXEf9wwiu-fybD6tVatF-kJu6h3280Zc2uIAh-zkKNB6IorWiUgJwx1PwL1ZWU02-CNlXgXnzFz7aRpL87-u3p2Adhaf6UIPMiSM5zpavEHEr2ZizOo8AfP7APT7V81hOAwA2rDFBICPXgWYEitmpEXSYR39Tky_JwgLl26GzstvNZBUDanLZpAgaiTTD0HwaPR3yygQeksQTwghaL4brhQDHdPG9hbkB3eyaLQvotxg8iS3Ay_oltCoO5pGYHGGH_u7eG0KGnH2Xa3OJlgUAnYTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صرافی رمزارز کوینکس اعلام کرده فعالیتش رو متوقف کرده و کاربران تا ۲۲ دسامبر فرصت دارن داراییشون رو برداشت کنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2603" target="_blank">📅 16:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2601">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CFC1YxMJm7SjELpIlDlz9eZtD7FQ31TvfxPfRRzdhjMc1PDzFHNP60zs9cFGZiC-bFeYwA3-MDXdCqZmiG2CAQK4K26WLylhPr6oS3_tzLvld1YUiYW-_3CDMyHV1L3PiNGwxzljqUTD8cpynzfs48bKPgqoWNBY2NhtahY89nBsenm3xyy78PPNgK8mGcdSE5y1mxquFGs4yEMzuZlLTjCqW9FsiqGGGcXixOTCSXR4wyN8aE0_2Ato3NcVfWh8Glb8fCqN_yG__43E1uAqJEVqoJTVBFT6EKbWo1aEkkqVMV8OViGZAKlds2jB4MUS-Lxy-qPAx7fPb6LN-A4FEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی خبرها
دیدم
که ساکنان روستایی در منطقه فتح‌پور هند، در اعتراض به کیفیت پایین و ناپایدار اینترنت و خدمات تماس تلفنی در منطقه، یکی از کارکنان شرکت مخابراتی رو به یک دکل 5G بستن.
امیدوارم برای وزارت قطع‌ارتباطات پندآموز باشه!
😁
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/ircfspace/2601" target="_blank">📅 08:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2600">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Lt-drBvXaNP8bikRsrzOBa17oMwxFV5ggW5QgHjucytqrm4g9ibWOILwpw5n7xGFn5jgx5_eQ-bixzqkb6nsB_oHLE3hEU8iJPR96WmY2yKhdY5YaEkJAklFtxBlFu2I3Ju1tm9q7sRd9oIUA-9Sq-uQLWep138Si0trw31vfD5I23LpJcfTsuIuQ5AjRBSbjaVblnJ-_bdinAeeUzzQY8SMEe8HsXDiGYhCTfPqUo0eqmvUzWUHPXPlrRaIKSAU_jlEUcpSMYIen-1FGqx11UKCZt43gFYIWqoZr4ZIglFKeAO2RhqMxrWjHfpqjoSAGOQjMEoUf_ZGRF0E2Xup8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات سرشو از برف بیرون آورده و گفته "اگر درباره محدودیت استفاده از IPv6 مصوبه قانونی وجود ندارد، دلیلی برای اعمال محدودیت در این زمینه وجود ندارد و موضوع باید با سرعت پیگیری و تعیین تکلیف شود".
به مناسبت همین دستور سریع، فوری و قاطع، از تصویر پیوستی اکلیل باریده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/ircfspace/2600" target="_blank">📅 08:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2599">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EdAwAIGgbGDhtOIsbzh8PjHLy2wMHKWPsXUITmRg1UoZsJ0FwHZ3dxRQZiWX9lVIpvbYWKsJiWEBp_54g0foqSVbW8m1KELqf2mq64x_82qkMk24c-kBFDJJhdlDUIf9Mc5bOj8aeygTA7aE7uNvRMu53ajB4s5FTMEg9-DouMbhQ4TYU2xpNG_KCGUQgUjU63r5i7nsjG9UP4L4XYkH_XD7aCKdl_Aq5-YPbUnPg2y_jxdpCgwfMAZD-JK3eO_lqq_p3iASRzA9HYV7TDn8gi2ihYkKik0fbvG8v2qRVrMjX8-cu_4sgA__YLXcIAllHOVJXYbgo7g_Y1HWhS7utA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از هسته متن‌باز و رایگان Aether منتشر شده و این بار Tor هم بهش اضافه کردن. حالا می‌تونین از تور بصورت اتصال مستقیم، اتصال Tor از طریق وارپ و حالت معکوس استفاده کنین. پل‌های Tor هم بصورت خودکار از BridgeDB گرفته میشن و Aether می‌تونه پل‌هایی مثل Snowflake و WebTunnel رو امتحان کنه.
یه قابلیت جالب دیگه MASQUE-in-MASQUE هست، که در واقع دو لایه‌ی مسک رو پشت سرهم برقرار می‌کنه. این حالت باعث میشه برای خروجی، رنج آی‌پی متفاوتی نسبت به یک اتصال MASQUE معمولی داشته باشین و توی این حالت دیگه آیپی ایران رو از کلودفلر نمی‌گیرین و رفتار اتصال تا حدی شبیه متد Gool میشه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/ircfspace/2599" target="_blank">📅 07:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2598">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R6XFZnfZ59w-oc1MeqSRCCqgtFYb-50bzuHq33QgXnayak0itMjcW8u83AgqxZi7CSr4V2MGO1wlwmHSkxgT8dY_e-nf6wV9IJ9pfsAcmOnwedKNNoB5TllVsJsYMfHKSbGmC6m-SeQt4ItnCi-Py1OC_0aQlgFkQQp_om5qL8vr2JF0rg2e-fZumHm2fb7QHyN5HmC8jV7y9xaSv3hFoFCr7nu7dEZ5wPi07VhGyljr3A0oIpVZw0U9O2UKkw8MAKuHeA0MzFPwym59-kT13M19XMSQvsxJxzKXOPZ6XNynMEhr_x7YjO2dehQO0LFfMlObE8WvWIgXBgo2zj5ypg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنتروپیک، شرکت سازنده Claude، در گزارش تازه‌ای درباره سوءاستفاده از مدل‌های هوش مصنوعی، چندین عملیات مرتبط با ایران را بررسی کرده است. در این گزارش، ۴ عملیات مستقیماً به جمهوری اسلامی نسبت داده شده و مواردی هم به سازمان مجاهدین خلق و یک عملیات فیشینگ علیه کاربران ایرانی مربوط بوده است.
در یکی از موارد، یک مجموعه مرتبط با جمهوری اسلامی طی یک سال اطلاعات ۶٬۳۸۸ ایرانی را جمع‌آوری و پروفایل کرده و برای این کار ۱۵۵٬۲۱۶ توییت را تحلیل کرده است. در عملیاتی دیگر، بیش از ۵۰۰ کانال برای جمع‌آوری اطلاعات افراد داخل ایران بررسی و ۵۱٬۹۴۴ پیام برای ساخت پروفایل‌های روان‌شناختی تحلیل شده است.
استفاده از کلاود به تولید محتوای تبلیغاتی محدود نبوده و از آن برای جعل هویت، پروفایل‌سازی، توسعه ابزارهای نظارتی و حتی ساخت بدافزار و ابزارهای فیشینگ استفاده شده است.
©
RaazNet
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/ircfspace/2598" target="_blank">📅 11:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2597">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tfOeoCutpw82DSBmesFqpwdEKYtIuvMlCTRZG5SIoqJQ_hAKRzGe5uDPJb8ubPgGnxJ3Sac6Pvbwqrrb3DS-qESlJz2NOJCKpEMN85N2iqo4_pdrP64H43g4rhrHDcQvkoHW0aaoIgmF45oxHEmJJOn_jIcNcS1Wz-b9jirfhCe3XM5Q53JStU74uiI0gHleFc-pCMH5qYM7EdLWijjSHV0eTN9p6Jm2cPf9hIzJdtIZ6Dmt6xh12TtWSU6lzclRczYgYJFeEyX5RyFXpJE_MhDKX5QdTiTXfOh8mvyGhSzCVwnhGtyzsgRykvtDj0mcjqNcG7dmAUYT7Ln_gWPKPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون علمی رئیس‌جمهور گفته "۸۳ درصد رتبه‌های برتر کنکور در ایران مانده‌اند. این موضوع نشان می‌دهد بخش قابل توجهی از استعدادهای برتر کشور در داخل فعالیت می‌کنند".
البته نگفته ۸۸ روز اینترنت رو قطع کردیم، هزاران نفر رو در خیابون کشتیم و خیلی از همون‌هایی که کشته یا سرکوب شدن، از استعدادهای برتر همین کشور بودن.
نگفته راه خروج از کشور رو برای خیلی‌ها سخت‌تر و پرهزینه‌تر کردیم، عوارض خروج گذاشتیم، ارزش ریال رو در برابر دلار به پایین‌ترین سطح ممکن رسوندیم و انقدر محدودیت‌های مختلف ایجاد کردیم که بخش قابل توجهی از آدم‌ها اصلاً امکان رفتن پیدا نکنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/ircfspace/2597" target="_blank">📅 08:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2596">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/csF6AAhE69B-YRPsyuBjtqG6Mk0FqsOBJEZh7PULzJKWFplaDekOgsVl8HgNRdOxgx0cSa8UWRrgziDUNUvCmmk03P6AnzjbTvxv1D_i9yA3uSKLE5jCQfyZpy-71vyMGO1WhifMZMW_5VglGKM45YAyUBgYDcRyNWV-Wi6TEHANGXyOm7bao8DTU-cAo4RNnJo767wRnDyW7bfRAfM32MxXaF3fViMk_FAXBORJqRRs6ToBlwnoGoPlnKYydBUUN12YQe7rHstICFqpOm5J_DtOqpXX1VaauqXUKw861xgtyZWNSoqVcRUWM0AxUFvy--G6CVYq0D7FGflpyVBrng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیتابیسی که ادعا میشه مربوط به کاربران فیلترشکن JumpJump هست، توی یکی از فروم‌های دارک‌وب منتشر شده. منتشرکننده با شناسه leakhunter ادعا کرده این مجموعه فقط شامل اطلاعات معمول کاربران نیست و اطلاعات شخصی و نسبتاً حساسی مثل اطلاعات پرداخت، اطلاعات کارت‌های بانکی، تراکنش‌ها، موجودی، لاگ فعالیت کاربران و اطلاعات دستگاه‌ها رو هم شامل میشه.
البته فعلاً نمی‌شه صرفاً بر اساس ادعای منتشرکننده با اطمینان گفت تمام این اطلاعات واقعاً متعلق به کاربران JumpJump بوده یا اینکه کل دیتابیس ادعاشده صحت داره، اما درصورت صحت‌سنجی، همین اطلاعات نشون میده جامپ‌جامپ ظاهراً اطلاعات شخصی و جزئیات مختلفی از کاربرانش رو نگهداری می‌کرده، که این نشت می‌تونه برای کاربران دردسرساز بشه.
اسم JumpJump قبلاً چندین بار در گزارش‌ها بعنوان یک اپ ناامن و مشکوک مطرح شده بود. بنابراین اگر از این فیلترشکن استفاده می‌کنید یا قبلاً استفاده کردید، بهتره موضوع رو جدی بگیرید و حواستون به امنیت اطلاعات خودتون و افرادی که باهاشون در ارتباطین باشه.
©
hamedvpns
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vr6mxaZ7oUpLzRzdTvWSouGtPlONGH3IBCbQ58LIkDD-WtefflVYg1Mf874_VeDPDcaQhxys51grkfXgypDGtg2u3t5EPdyNAaQDzx-3hBVHgLSOUwh3fgBA40bgI1PkHJKtG4ln06h8wIT6Jgg0Noq4p2vcMVV6AVn7cYCmP4hNnB_v7X1BVXQg-SEDJmRCdZy7TZqusmu_pKSBnK5fEUWgUoaZxdB1ixk5HxKgapgGEpB_-737BhAXgg-iHEbUTWeFTD3cLvxeBqmnQZg-yEpy_O8g0D12q5avXHj3htlO0Hdz_-qBh8lBNCxeo6ovuj5skpI5kpyJb-H97VbgNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه پایدار است، یعنی به همون آشغال‌نت قبل از قطع فیبر نوری در ارمنستان برگشتیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cF3BBAjW_0BditaSsmxElKSYz8tMMKdB-oZjmyfHV3ZG8egYlzLExfxZS1ybzO46U5I05W0RBM8SZzNDTqvX5uV4glwJQZyCYdmzvk5wDqX1SOSla8D_Ghe9urkLanKJso2vnpd-F_AYfw5zBw34wyYRrSe6KhTeXHjnr1ccniaWn7lXmao_W3-YN8g8aGQdQ8rQwK9aWHgK3zW0bkKyf7AeDWg9HXyDhXN8X0gQdFsnoOomy6JaYdrR747exNnT9g9zJFFheKsamqeJrXXaGhRv-3WaE1NC9_-bU6ofB-AZzOAAlNC6rZusuPIxQwttyVU0Xaq3heq2vkGlXSnwcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از مدت‌ها وقفه، بالاخره فیلترشکن Oblivion به مسیر توسعه برگشت.
در این نسخه که برای اندروید منتشر شده، هسته برنامه از وارپ‌پلاس به Aether سوییچ کرده، تا امکان اتصال و دورزدن فیلترینگ از طریق متدهای وارپ، گول، مسک و سایفون فراهم بشه.
👉
play.google.com/store/apps/details?id=org.bepass.oblivion
💡
github.com/bepass-org/oblivion/releases/latest
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2593">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GcuV5QR8Lr091wUbPfE-uE1zxu27fVOWNWiA6ndEO-aCbXHp5UeohdwAeX9GZgXF4tRkFyYdU_Yg1aQ8XsBmjn3rN1SPZjSGFF9gm2s5oGNX6aJ-FKP-Ni65otpXsb5tHg1f1H98yMxLY4K0S7QQBnM-Z1AuBAZBlOZgL2oYj99-oVHcVoua6X7m_uJxwXsBzIaYvMwFVKDnoc6unz316_yusZe8nIOYrOndnP4MA47BFipvNBc3uFCf4dE6PpcjgFz1c02sr8pqVo5bnvKn-JxHqR1f1f7kJPwsZnpmcSKle2KK4y5AyAPXtQGtlTrdTRcFiJvT4SeBqMcXw-Ua2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل یک آسیب‌پذیری روز صفر با شناسه CVE-2026-85046 را در موتور V8 کروم تأیید کرده و هشدار داده که هکرها از آن در حملات واقعی سوءاستفاده می‌کنند.
این نقص ممکن است با هدایت کاربر به یک صفحه آلوده فعال شود و مهاجمان را قادر به اجرای کد مخرب، سرقت اطلاعات یا از کار انداختن مرورگر کند.
لازم است پس از به‌روزرسانی، مرورگر را حتماً دوباره راه‌اندازی کنید.
/فیلتربان
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/ircfspace/2593" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2592">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aMzycVNFiHmVcvJMm9lvwTB16at0RnIEmE8qQfK_DcYSwZZoLV3sQQhNU0dGhe-aAjQHddpZ-t_4bAKjEL_2NICna87VfI9GszKvEMhpQMqbWBV4F9vd7uK8OlqwBvhSDG0k7Lzn2YYnYrEwYp_uQEzJ-GSTKA1C8N4ATcVs78tCoiLSdpAVnA6YfQuXyluPNZ0a69d2CIEvi1D_oKRcpsaj3wcIF8O0YLgWMRS8lAUIDvV5qOGb6x4dkzA36MHB3cpTrKDbMyRAvwM2C8L6zOZNLVh_jKHNu2Ywaf1L7RHHuPIYtfnZ4Rc5AffLTjBXJAGcC8tDdWrIVOjY5kytMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیفیکس اعلام کرده که این فیلترشکن توسط تیم امنیت
پس‌کوچه
مورد ممیزی امنیتی قرار گرفته و تیم توسعه درحال بررسی نتایج و کار روی چندین بروزرسانی کوچک و بزرگه، تا در کنار حفظ عملکرد و تجربه کاربری، کیفیت و امنیت برنامه رو بیشتر بهبود بده.
این تیم گفته ممیزی‌های مستقل و همکاری بین تیم‌های امنیت و توسعه، یکی از بهترین راه‌ها برای ساختن نرم‌افزارهای امن‌تر و قابل‌اعتمادتره. هدف این فرآیند، شناسایی و برطرف کردن مشکلات پیش از سوءاستفاده احتمالیه و انتشار خبر این ممیزی هم بخشی از شفافیتی محسوب میشه که به‌گفته دیفیکس، کاربرانش در چین، روسیه، ایران و ... که با فیلترینگ دست‌وپنجه نرم می‌کنن، باید ازش مطلع باشن.
💡
defyxvpn.com/download
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/ircfspace/2592" target="_blank">📅 18:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2591">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K-OWWCPuLwL37ZPVgchmgDqEQWdynD4LVnrs2Ov5601WBLysaCJs-4lhcjy0_VzT9pNMjW8xlk-H0tMnnnomy5Jk_ITFjED-A6khQNM1rgrKBL9dlIjSZkPhmKKDh7_NAVis_P2DhkKblU16V8wON5QNqFbstxbQZ93J4vH8rDN-JKRWiFCCWWNjkoyMVlpDFHRL7BUOkNQJllkc1dPxuvwC0zL7-FWzmgVjnXNXCgGYlYanAx4zZVyrl3kHWe8hNX0nvIIYVAd6j48AjIgGXV88nrjDkrhO4O6GUeAxDQwT3s01cbAbT8eIF0FDoKzS3g1rCweE4eUJKWpo1EOMAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه کد QR حساسی رو می‌خواین مخفی یا مخدوش کنین، نصفه‌نیمه رهاش نکنین. ممکنه اطلاعاتش همچنان قابل استخراج باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/ircfspace/2591" target="_blank">📅 18:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2590">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A4f4AH0ms0q7sD8SdWoAy4zvC5V7mltkh3uenkJJigPbgbDlULBsrAFkR90Dok9g1DaDKSXJEn9SeuOcXu_WxLt7OQG11PoUPYD_U9kGq48ADXJm9x83dRjWFH-QFI4QgEBMBIh-3kL6MBNASBzO8sXErK_-ewZ0aDRzKkTCQBoBz3ctWNPysfhSXa7W_GbbzTxb7jCYdFDlvw4BgDP_oa1iX_VD9DsN7yM94-3c31upQvCWrpqO1DYDXANxoe5g-IXMAE9AtREP-MVrewHtXTnJ3VpiANQaaAtlMedi1v9hJNE0vNJsbT03pKgUClNTDfiV8dC5S-TL-k9iF8lCog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سم جدید
😃
☠️
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/ircfspace/2590" target="_blank">📅 18:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2589">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oaTRT6DAvruYHUSmMmidSQ46FSWQbRHoNjIwEmNZhhHLtxAF6HI7fUC5SizeJihfpQ33Vk81xvlmQI_Te9QPbzBDVHW07t3UxwUFKTwqWTOZVFyYJVzryT4u0cgbByyP7CKfUSZbRPuocS7bCQzD-PzCMBcluAXewCuhoOJvlPxdq9iwpLL2nfY7Oz67yaMIJ3bXXFow20x1IS97LAKdDJaKXhoVfiqnUQmkC8CW5Uf6sGOjjkVPLFHiwXNsgKGrothzkOjJJs7EQvPLKVRuqLh3K5AqER08_17YNj7dOct9vvbSbY59JnaLf-m5hPYUOhNayvwrcVb15RqBmWF6Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات معتقده "قیمت
#ملانت
به اندازه سایر کالاها گرون نشده" و احتمالا باید بیشتر از این دستشون رو توی جیب ملت فرو کنن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/ircfspace/2589" target="_blank">📅 17:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2588">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UWG6hHxMSiOQPaC2S2KWwavwdOPFMaGYwPuvY-VP5ohwAKmIlXYcgyaElcaVX2ZCKD1btSDXhi5PV3p48GPzeNDQoG222uo9GLa4oAjTLfGqshU79dQe07RE2irKORXAWUsskwmtBSg9jI3O_VwmUsnieutBMa0RjsgfQHUgyTz3DmHVf6nIEhpK0t4yXL-Tv69VkrK_LUMYLk2yVBeRu6UVkvq5Jn2LSVkBjDAGlfRkFYZG6Rf3tkJZqLl0F5mVylxlTxi9N4_AJ_SxMAbwX2eP0PT6edWc-B4EADFhDaYu5vPIxf27K24NPX6r6QHAn5LFVkrrMVPG0YMZnbEKIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واحد امنیت تیم پس‌کوچه در ماه‌های اخیر حرکت حمایتی قشنگی‌رو شروع کرده و اپ‌های VPN متن‌باز (که در ایران مورد استقبال قرار گرفتن) رو تحت ممیزی امنیتی قرار میده.
طبق آماری که دارم گزارش این ممیزی‌ها تا الان بصورت محرمانه برای ۷ فرد یا تیم توسعه فرستاده شده. اکثر این اپ‌ها درحال کار روی بروزرسانی‌های جدیدشون هستن و بیشتر از نصفشون آپدیت‌های کوچک و بزرگ داشتن.
این‌قضیه تقریبا برای توسعه‌دهنده‌ها و جامعه‌ی هدف برد-برد هست. اون فیلترشکن‌هایی هم که نسبت به مشکلات گزارش‌شده بی‌اعتنا باشن، به مرور از چرخه اطلاع‌رسانی و توصیه به افراد کنار گذاشته میشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/ircfspace/2588" target="_blank">📅 17:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2587">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TIT38wsqzseuYltMmbo0gVAi0mhGwLZ74BFedeIxW5F26IyzSS1fnuoRta5FHdth3nrtY4DEVelTFlUHeB8rLWGBYqBi8MLkNMqJ__ygHT5YJ4hOc-gYF9KKqyxf-OMrnCfTA6M5YyyvyQKH-ZoinX7Pb5Jig_MVS3FDP3dm3viNaDnSDIM7Syi5QR-CFCq639U3c12Cc_eNEQGKKZdOH90CQJvHP3PLXQYhmteAxfsoB7jNcrqn95ul18d6ao6HuzmamSAQEmasEE31ky5Ei_RwGiM0q6ankzWxTgGhbL2LdBH-BsrbgkdXcTpkWlPLsF7QMsWHelzrkmtriba0UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلسی که خودش کارت قرمز داره، به وزیر قطع‌ارتباطات کارت زرد داده
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2587" target="_blank">📅 11:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2586">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IlBopOQUwvQ-yZWejS2if_fAq9FjZlJkVcleiuRxRR-wlbd6wsBJuyNZ4inFBLnLO1nAYbkk5ArWPYA5KwWX9A7H1I_1vvQLZp1NFzUv1icIbFDjp5A6-X-r22iLJFqSaPXrmNfUwMsmGGlsDpq07VYOWSS-Wnt73x7LB1coN3KNWfXD73nT_SbvkcIZjbaGh8AzLlc6__ZcbObXQp5LZwWlNBef6RY0Tuq2xQygu6hE--UY48C_CJhO5uLgtbFQ5FnVdJtIujFB97-QEafdqshz8X6mQ4nrieOAtgg1LYHRmQGlnjbcVYeW54Aj5zHeMQpnkYsNOJMCBFxANUAmtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور: طی ساعات اخیر اخباری کذب به نقل از اینجانب درباره رفع فیلتر اینستاگرام منتشر شده، که کاملاً ساختگی است.
/اقتصادآنلاین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/ircfspace/2586" target="_blank">📅 09:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2585">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Smqp6ZGoPjHW9Xl88KUiwmzzwvgdVRswAcZ2H0upOfjKNpZ-EPJAv0G_YJrXJiWSOAAnwatY2oiXueu4_zXpL8L-YGg8bcW44Bf3KPNzhJDBI-9nSWb-QIy1d4e5VQzxGep3M4VehZ6YyTJO7BURrI7pgs4lgxXOhcVQswnaZhFnVT_5-6iSjKqPwlyXre-HkHjbfBHMY3gkZY2XJ6njJ1SEWTBKQ9medXzfSBK33si848ItROrL-sKGmDajv_qeKEmLZKeD0lCZYwC1Lml9hO4D8SRNJJiS6TRO3LvujdOnRE6WQPsK1u3Hl3x7-vYQsrNgEw-Ni1mVA3Y1aHOwnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاسپین یه ابزار رایگان و متن‌باز برای ویندوز، مک، لینوکس و رزبری‌پای هست، که دستگاهتون رو به یک هات‌اسپات مجهز به VPN تبدیل می‌کنه تا بتونین فیلترشکن رو با همه دستگاه‌های خونه به اشتراک بذارین.
کافیه لینک VLESS، VMess، Trojan، Shadowsocks یا Hysteria2 خودتون رو وارد کنید، تا ترافیک دستگاه‌هایی که به Wifi کاسپین وصل میشن، از تانل Xray رد بشه؛ بدون اینکه لازم باشه روی تک‌تک دستگاه‌ها VPN یا پروکسی نصب کنین. درضمن اگه تانل قطع بشه، کاسپین دسترسی اینترنت دستگاه‌های متصل رو قطع می‌کنه.
👉
github.com/Iman/caspian/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/ircfspace/2585" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cDWeqUxTe1hJV3hbTp-7rzoeBmD_OxYNrBGrtMJkpC4KP6n5ITDB1nvhT5ED8qVC5nEJf4VE76oRd0wUq131Pe3Osztcoe7Ju3ixx20GoEauAn9FI-sYCkQxRTceThpP19ygedAoIt1onXQl8sXYSsy7hXxh5D1pOQq7lDPknYzm1YAka92XsSjMzgJPrEK_pf73l1SjVceKyfBZitvWFuk0gC1XM25-Ax0aTR13od7itGT78bjCIbD25-qZQo-0x0ZbZLH0azf9o8O3_mt_iSBpPW3sqe4-UK3HukvpZWY3LxOrJW4bQQvA684zBazvYLTflYpr-NUbtzgyUSPDOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Misga یک پیامک‌خوان متن‌باز و رایگان برای اندروید هست، که به شما اجازه میده پیامک‌های اسپم، تبلیغاتی و کلاهبرداری رو بصورت دلخواه فیلتر و مدیریت کنین.
این برنامه چند فیلتر داخلی برای اسپم‌ها و کلاهبرداری‌های رایج داره که می‌تونید نگهشون دارید، تغییر بدید یا کلاً حذف کنید و فیلترهای خودتون رو از صفر بسازید. با Filter Studio هم می‌تونید با Regex یا متن ساده، قانون‌های جدید تعریف کنین و حتی از هوش مصنوعی برای ساخت الگوی فیلتر کمک بگیرین.
👉
github.com/mirarr-app/Misga/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/ircfspace/2584" target="_blank">📅 08:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2583">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RH8bIBJwTVoK4txY2rL1OzD8udvGe6FJXHWEmuexkpzf-CzJNM8XI9SSgT6Tu0zDYKpzRqR8ONTr6J9-MfYAsxB1GdpXDGTbZbjMfDl0qRW7Wn_2dSdyKsG5hVKQ0k_LAylAxRZyhL5rdat3aF1l8Kfer3WSjzrco7Al6r8PGfqSFXoYsbFlDuAbDT2rAxeaMcwKPDDDxMjLQzGM5nGREj5zznQLkKKzVBS8lPanyuI6nYDUkcvowqekrJgZuiFa7xm11DZ3GWqv7Mwu9viM1I6JwiqsEOOFNwbVn-CS01js58mOBInnRX0_8-lVtPWgV54OInu3RSwoTiKsbbOm7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند آسیب‌پذیری بحرانی در RouterOS پیدا شده که بعضی از اونها در قالب زنجیره‌ای به اسم MikroTrick در حملات واقعی هم مورد سوءاستفاده قرار گرفتن و می‌تونن در شرایطی دسترسی کامل به روتر بدن.
از طرفی Shadowserver در اسکن اخیرش بیش از ۱۲۲ هزار MikroTik با SSH باز روی اینترنت پیدا کرده که حدود ۳ هزار موردش مربوط به ایرانه. این عدد لزوماً به معنی آسیب‌پذیر بودن همه این دستگاه‌ها نیست، ولی نشون میده تعداد قابل‌توجهی از روترها مستقیماً از اینترنت قابل دسترسیه.
اگه MikroTik دارید، حتماً RouterOS رو هرچه سریع‌تر آپدیت کنید و بعدش لاگ‌ها، یوزرها، Scriptها و سرویس‌های ناشناس رو بررسی کنین. SSH و WebFig هم بهتره مستقیماً روی اینترنت باز نباشن.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/ircfspace/2583" target="_blank">📅 08:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2582">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c2CgQBtzl2TRhfkFMESzgLuSJHNvws-6StU73YZ5feXlP5Cbl-7ADWBF8-FZX4aWlm_Z-hYwSk10SNGK1DUOg0jArgmCSst5OzqRK1vQ-5Dyfx5YTUYRl94qXxuA9PCgP9fNxaW7KZlKTznbR7HHxrPCtOY4nxaQR1OPZbdjcbANdSguDOYDuDEDV76-0lF6R7kYIrKECv_5JhizWAK3y_nADw3k3rThS838EocnPFpfNUjs2nH7ne5xLT4jjUQD2V4O2CP_syuWeIOO4wOjgInUHApN_KvEuHalBh2g3B624_rOtZIWLa4y4jmQw9FoDWDP5ryNzmX2SwNMZCfgqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه یکی از زیردامنه‌های gov[.]ir به افراد دارای مدرک فوق‌دیپلم یا پایین‌تر اجازه ورود نمیده و حتما باید لیسانس داشته باشین
😁
©
SePeHr
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2582" target="_blank">📅 07:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2581">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nzYi5cgk9oP3wq2bJt6Zd48EHaRpWCjs9GqiT1OzzS_MLO3cn7bzUJwBN9VwGr665Geoa3v4FmNZvQ6Ni55sPQhR9edtPvGlosb68fUYEk2jcXL8N40oPlRJtRIFYBL5b1Mawkim4-7fecFUL2shiZvK5iE8VPh_rXAkTKopC-S1i7FBMUXlt7Ad7IWmkr_JP5whKBQMqkfDG1ozPc1vC2N_d2793vjV-5IljMsG8MbihY0vlPsrLiRUzdidCSQf7vfE7b_gvZ9P2ohUuNp5ZZopzQWoMaBY9LfSBLKBG9__m2LC8N3fKiDd4r5RlwJcFaEVeTdNK7Tpilr9_0W8jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن متن‌باز و رایگان دیفیکس اطلاع‌رسانی کرده که امکان تغییر زبان رو در گزینه Diagnostics & Experiments مربوط به بخش "ترجیحات" این‌برنامه قرار داده و حالا کاربرانی که به چینی، روسی و فارسی صحبت می‌کنن، می‌تونن DefyxVPN رو به زبان مورد نظرشون تغییر بدن.
البته این‌بروزرسانی بصورت آزمایشی از طریق گیت‌هاب در دسترسه و بزودی از طریق استور هم در دسترس قرار می‌گیره.
👉
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/ircfspace/2581" target="_blank">📅 07:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2580">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ایسنا خبر داده که
#قوه_عاقله
بخشنامه مربوط به "ممنوعیت استفاده از پیام‌رسان‌های غیربومی برای اطلاع‌رسانی رسمی دستگاه‌ها" رو لغو کرد.
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/ircfspace/2580" target="_blank">📅 07:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2579">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">حکومت در حال تهیه لیست IP کاربران و در قدم اول مشتریان دیتاسنترها است.
در این طرح شماره موبایل + شماره ملی + آیپی به هم وصل می‌شوند و بدون ثبت آیپی در سامانه شاهکار، دسترسی به اینترنت ممکن نیست!
نقض حریم خصوصی کاربران و حق ناشناس ماندن در اینترنت با قدرت در حال اجراست.
©
souzangar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/ircfspace/2579" target="_blank">📅 06:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pzMgJc9twAU9wNvI3K_g2k3AiLdxAkCjYhPfyltN5YP2Sxs77jQurwonL2xc3fCpW7g063APKBwcax-JESNmsp8Lp0xqTMO6vdPWwsGDAB8jVcHOoZ4Ybij8tHOeKcM75skLcq7CEMJgd1JGUCEypsccwRYngf92ANTsD3_7XYBQl1S_lwDI5U4cVlUDyBJrYfoT5uot9zmEkqnmeO6auWWhdc3eDikHOxNkmfO06HipIrX-v9AR1R_r4gBEQ1t98hI8xIpRb1yrilDW04TX4M0ecJqLi6VNJwiWQHQ8pCVS7PiYLnaoMMS2krN7hBZi30OFapAMI2OvmfGrupdA8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از هسته متن‌باز و رایگان Aether با تمرکز روی بهبود سرعت و عملکرد منتشر شده و مهمترین تغییر، فیکس شدن مشکل سرعت MASQUE روی HTTP/2 هست، که حالا با اصلاح پنجره Flow Control، مسیر ارسال، فریم‌بندی پکت‌ها و MTU داخلی، باید در شرایط مختلف عملکرد بهتری داشته باشه.
از طرف دیگه، محدودیتی که بخاطر بافر دریافت TCP در Netstack روی همه ترنسپورت‌ها وجود داشت برطرف شده و این بافر حالا بزرگتره. ضمن اینکه می‌تونین مقدار بافر دریافت و ارسال رو بصورت دستی تنظیم کنین. البته برای WARP-in-WARP چندین دستور جدید هم اضافه شده، که اجازه میده اندپوینت‌های مختلف رو بصورت دستی مشخص کنین.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/ircfspace/2578" target="_blank">📅 09:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OljZLWrJWZaofK0tA4peNU4QMnqHD7FUAabAZiqLXTs1rQuKQQIxWwcbusvytcDOoY7T8omtF0WyvpjrV7OFyb7N5cH1rZm4aFm4F42GDIweVOVVMnzDrgTg4cL9L-0msCQxW-bF6eaiTxVJtWxVJ_OJmTzWMDOvuk9zeT6YhfDTz3itgohoAtMxY1EJlZ8oatwr5Nfe3SInJVnPuxHFNZPkXzbnPNleSGW_W-8-2zlN_E1eDyyUMpq3yUWueFYZjXokuqM19R1xifrT-17Hw-LlP0UmMFGEh6AdjEX7tSWcYFNUfXAyp_Gx9_xL4gKtDfGZbrAJyRxXEt9a82gTYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات در مورد ۸۸ روز قطع سراسری اینترنت و بعد از اون اختلال گسترده در سیستم بانکی کشور خودش‌رو به اون‌راه زده و با سیس عقاب اعلام کرده "آماده انتقال تجربیات سایبری خودمون به کشورهای منطقه هستیم".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/ircfspace/2577" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C1onCLpIL3JAOKTYwnbnXzcnT1ORkywHcjBa2lDNb4jLYt-5ejB6Q04i3ZpdvV86M6aV2z-NoEhoOjlXuWT8AoSoMzlplIgkFY48kf3Jb52uT2EVwqPsycL5CYrXGlQ0L_F0hpXYZH-jchrwmJoKpkFAbe5g6SKaatdsMM7QRRErazz9TWeKWOX6uoVj_trV6t3V5aSji8wBFRKDALVjndFhAz7jC1YeQv4iqWltJ8kui_G1AAE3V8b73HS7YUTYEZUA9TlVcQAcMOzt2UqM6jeRvOsyais-2COnpIuNSHXZ5yYPcnEGEF06pCLEtol2-Obk45lPaWExVXUxnPL-zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه باگ توی واتس‌اپ اندروید پیدا شده که روی بعضی گوشی‌ها می‌تونه اجازه بده بدون باز کردن قفل گوشی، به گالری و عکس‌های شخصی دسترسی پیدا بشه. این کار نه هک پیچیده‌ای میخواد و نه دانش فنی؛ فقط فرد باید گوشی رو در اختیار داشته باشه.
ماجرا از طریق تماس ویدیویی واتس‌اپ و گزینه‌های Meta AI انجام میشه و روی گوشی‌هایی مثل Pixel 6 Pro و Oppo K13 جواب داده، اما مثلاً Galaxy S25 Ultra جلوی این دسترسی رو می‌گیره.
©
notebookcheck
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/ircfspace/2576" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2575">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PaoMviDVhb7ZuimtR1nV5nM7zEWWpHy6wtylo7vRC_BOW_se-vGDt4lWHM6hPtIlr0lxI-1JO5YRy7LqyQk1iG1gT2NfQgO1uG9cKu6HRUsakQBkBz4LbjLed1R2QxxpmTGTYvDTNwp_wIDhom8ueDtjy8QaTtmeA7XR-y2oYILDupdt4tNu8PMxElh5PPCNWLaw6qA4VKibg_87y0o4X00KRqiWJstvGpf9lCUVKWFGdG2aebvxZifQYELHEX6JY8DY2PL6QZ7LOIiCfnh0fwTBm3tJCpQOfJabWcXUtXd0zfnzsnal9Z8cHjs8m8YsGJ8EnOlXz8gUm_sawzEDeg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/ircfspace/2574" target="_blank">📅 11:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vyeoddq5p77JATnfZ4lu1eQkNWy_LgUVWOAoVAJVx76FN5ogAS-U_zhXEXs8BA4esWdtPLE2AhKCwiFp7Z_twu11ANOLcpD4Lqn_TlT91Tti-QiPh9y63sRUqunyWXDw8zvbJrHoLshGQxtr3ZmQ2wZAW9PpXxG0Bep-bjqZtWHlRRT2XaGzpVlDerJrAssYkat41rvLaRRW4GkrOZvNW2MyHFiwPxV6NlJz7yiAZjnxrwkoadD5GiEmzn4qraKJ94_gQTjT4WbLASaNndF2hOJdCtkRrR2ZivLapHmHBqE4uPtRxkWbGX97HOCCm1H5BASKtyokA_0HtJe6PNHK7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36K · <a href="https://t.me/ircfspace/2573" target="_blank">📅 11:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X0NPtZhfewInuMnRtGRea2IREyZQbC1CkE8uaH9OpBDKJA4Tb8kRxxCNMnovX8fCGwiYugms1MNMRSNWxMVmivkpgvrnGvEK0ThJgWRJZqnAcdnGINzYE-mIb7wBgacoqrFp9j-h7Q3YwMrdE6oTZVt4GbNq4dimW3Koc6pmDqvPzZDpUbxtltlJZovr9Bf-wcr2SG6HEUmaJo8HNni1zE6mbIwLtI-du2nBrXBZ3oGcfVT5xk-LuJeTvImyJM-2mGgVZfQDPq-I-bkb8dWVQUHvNOrC-fnKEMj1b_QgBy0P8yIDqONlAVmJRcIR1ww0xxUYh2OuF4t2TQSV_nCOwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/ircfspace/2572" target="_blank">📅 11:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EzZ9pA8zI3IqnGJdGA91OTv8ezqAGIqFr69uEVh2rGhverByDDVCskLlzizlUnxQmg4jStZArSccGExnCzEMh4DC8vmatDmNuvVA0ZxUNF-Mj2oloYpKlv3aQoc-me6Dj4QGv-rW3yLxWElQTF630hDY7UY2mMywKFSt072tC46N6Gb5Y6AKDBFUJCb1QEL1Ce9CUnDiK26ykGbMQHdkrRPvW8J0alSCzz_Q45K_MCttWTRzgsiO_-BXv4vhRLp7zbb4AhpzoBJgmo5YM_4vOqmcnd5ErhUVRzJYW2bznseZLCw8tjguoXNedpN4HJsgWQ3f5YMGK0FVcac-Q78RKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل وزیر گفتاردرمان (و فاقد مصرف) قطع‌ارتباطات گفته بود "اگر استفاده از فناوری‌ها به نقطه غیرقابل بازگشت برسد، بخشی از حکمرانی کشور در حوزه فضای مجازی عملاً از دست خواهد رفت". در ادامه "بستن پرونده فیلترینگ را یکی از الزامات ارتقای حکمرانی در فضای مجازی دانست".
فقط نمیدونم مخاطب این صحبت کیه! اگر مخاطب مردم هستن، بدون تعارف بگه بیایم برای پیگیری و حل مشکلات وزارتخونه آستین بالا بزنیم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/ircfspace/2571" target="_blank">📅 11:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2570">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/ircfspace/2570" target="_blank">📅 11:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ObYK_su9dHwSahXRJMYw5yDAMWoPrNAOX3Ku9I-KvvP_8ZQ_04iGyTNagtKtTNicUmmw-tjLDrs_PESinFVUHWRCHbgvS_iwWRg0ALmGZA6zQw81kAPxUiQC1FLbAVLUwpMDZBA7ismMjQrz3AUAgI9wOD7RWQ8rAm8_ugpZEeM4hJcdOX45QIhryN1J8-4DLNbS2-aalSOKOwfvDhd_57MGZi633oQFzX0_8N6EeOC9tSd-2jAD-sjVyhIPZ1qEV4YY8b2zEPqhy3fy2oq9fdDTpI_0-Jj5arSx36cgrjBfhmUKpz3evhs91LTxVqLEzWbYYJhn1_nfZ-o_KfmIWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/ircfspace/2569" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2568">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">از بین همکارا، اولین نفری که تغییر شغل داد و رفت سراغ آهنگری، شدیدا تعجب کردم! با اینکه خودم کم آورده بودم، ازش خواستم جا نزنه. اما بعد از چند جنگ، کشتار معترضین دی‌ماه، قطع طولانی‌مدت اینترنت و حالا تداوم یک آشغال‌نت پراختلال، آدم‌های ‌کاردرست و خفن زیادی رو از نزدیک میشناسم که سال‌ها در حوزه‌های برنامه‌نویسی، طراحی، شبکه، مارکتینگ و ... فعالیت تخصصی و رزومه قوی داشتن، اما در این چندماه رفتن سراغ مشاغل غیرمرتبط مثل نجاری، دست‌فروشی، مکانیکی، واسطه‌گری و و و ...!
لعنت به جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XvmBN4GR6QzIPAh137NfJHWhZUDIDYYGZYe6H79UcpSG_dFofsZzU8htYjvSEii_7g7IEKexgixB0Hv4YCUKc3pEAObfHnx4Hjfk2KSfVDb23d084B8jwaYK0DNMAcyiewhnLh7q9BqBog5MvU2ucPRHZVom-ZN4YMpwTJ9Zr1AIYmK9xu__O8vUwkiOX-7or4ofpdbr53mn144CSugK0P59C5UA1Cn5e8mtBz5-EJ1euXMkg2WoZObYIZluR7E-N3XDjK4GolgxBzZnSpw8GZKHUjiedFH2zeaNl6sRn4J25ZN5q5yP9OuB1n9IrhgnuXjsUUVw6iyU-_enoIrpkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/ircfspace/2567" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m1xlfwXEBaGENTyPbS1VykSToqvkdtt9QCelefy4Ge2nSEUJ18bxU5Wa4vyOjuj7JhHtcINwhZlU3DHTF13C1oAYWt0ZXyOSakVqiW5A0XrLGPC_QTgoU2MjrlNoX3jW5PHcGQWDWIowGpbI9T0gR3WGNcdLU0o2eSydiNttoZFij0xVzMLIzIVGXkPzv9wyddJz1p3RkJKjomZspwjFiWHKqfZHtf5YhpOi9wstU_KELJURH7QsZ7Abr7BKZkq-R-saeuLR7-ne-32sBdg-QJjw1gFY4UIyo475TjOjhNHDqpBUlspXDexddgICjSTzweXj3ydtxqqY0LYAvwUdNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا از کشف ۹۹۷ دستگاه ماهواره استارلینگ در ۴ ماه نخست امسال خبر داد و گفت: در این رابطه ۱۶۳ نفر دستگیر و ۱۵ دستگاه خودروی حامل تجهیزات استارلینک توقیف شده است. /ایرنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/ircfspace/2566" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P1mgR-SNGoDChSJgBr7ujUJp9A7YsdvUe161RbQ5nLirZCvtx1g52_VkhGltvGABAEvsnlGMcpWFYWfzxisMo3040GBJuqS3vCxnrfJM_AZWFG9hXd0bK_Wk3kIkAYAqOTJq5j6Dwqz8HV7ut1MorJOfVe-2MWRdybOtga3YkQDIMOZxALsz45IS4yzpg0tDdBmf-cUzry-n8e23SRp86gxe6KOdupT_9m9sIrRN-7bXcqd4WDajOcQmuPh0gyuYstwB9zsis_r3Sx5Xvi8fj243YoEqLa72f4HcGvQHoJyISV4XaWEiWOD1jByc9pN29TwE2JzXCDlib0rcvDwRow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/ircfspace/2565" target="_blank">📅 19:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WqRyP7Zbkzbrzww1DcyX3DzgOGg58OWeL5sfCudHk27_5-Cpp6rCBjrQTkSVarlkzRxfIJGZPOJ3Fdl9ysxAKoFC__tbl7iXl-afaokR6mK95_W631Mb5_h3y1ckmFqgrTq3GMSmvcJykdNxYpuay8bHvc8iTGKTtPFUJEful920xgxc_ckzQgOrNNAiqTrmRdxjetXwMxJwqUs64XcRHt21Y_b4NVK0ZdwrAkyxSm35kPfMOHJd3chzFlUxdaoFhZoiCu3X4EeeV8wpV07OYx7kJ8axnozvlWNLgTomGLQ5uL4e8BeFvfqRAmlQJ5t-mpJM06iA2cpqFV0UfHtHsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/ircfspace/2564" target="_blank">📅 08:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2563">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uZwuBx-o5yykcAR5UKLjHbQ5TkgPTFYbeHzHkA6NXEciFIUgC04SH1LFefT9H4eAeMOjU_CF0Gm9aqnJ8SgFGl_JuQ2URn4iTS0VaNDE4T-rSkjVmv9tHKsidjp8dayYPiTDfWUtYTF1XKu8HvqZWfEZioRr8ojgKhnEhU9JqLiiQQuUSNKDkwPj25xVmXhMudCnRVhDKWvKcYZsjRG1P_pnBWf7RQYGe6pj3rOuVBSFmTpwuDJWZRlGtrVe7wRsHLIr6DNUefxKDU4Zchhu0doUHs4W3MAGfk4C7drBhzMfx7OfaqOzrVu8oCouzqrDPbkiCEY87MxIVHWsbSUwtA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/ircfspace/2563" target="_blank">📅 07:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2562">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/omW8v9gjOfOoeRh9-CjkwkbnUZL_TUvXDjKhAKIQ5is05zuplFbwv-3zp6Vf4zcIksqIoPB80X1_NZ-07DIH-HYlg8fdUUkQx9btySVRLvy3TfdGHUnwduwmPBV9iQhmwQikNSPVDJAcwYkt9jHcofiwcPc2qKBHRbmryl48wlkEZYIq9nw2wUD7jn2zMhvblVm7pJRWBKvfRo72SaKT304Sbijia96i0tz2dUn8ppjhNMH9KgAFtR1NxsXW4BfOC1L2Hj4MrbSAcMfGI3gWLfXxVerPErxt0ESefiRvYZYs68NhnRoYM4SXC7AfhNU9ydLe3T8Nl5cWrBdVvbRfLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/ircfspace/2562" target="_blank">📅 07:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2561">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aSScsCxbMlYMvXXRzlyZXeX7tGIHVzL9fS8Ru4TlrBiNp9YVTb--PwfBIfHOOdpvlQ8TAl3mZo3LKvChRkE2n9kYsGZuVGRqhUZnXoqzuQjkODeqLLamUbFDFZjC2-fJSpruOvlDY4PX0oQ8TI548tlao8_s6VsNdM9ytolTNUcEZvbOjV7cQer1iaDmIBvMUiVnYz9YNL5pbUJxnDETsHI1u2B4jQfKX8ztthAU8EaexxGHvgbrqId4nhHaDzLYAmup7KIZJKY2PL4K4iynhm29YaOCEOZjxl_Zdav_EdJXXLJbgjy2WKvvgqww9TqNTNODdpikFeOKzonxQfxRog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران مؤسسه فناوری کارلسروهه روشی توسعه داده‌اند که با تحلیل سیگنال‌های رادیویی وایفای و استفاده از هوش مصنوعی، می‌تواند افراد حاضر در یک محیط را حتی بدون داشتن گوشی یا دستگاه متصل، شناسایی کند. این روش در آزمایش روی ۱۹۷ نفر به دقتی نزدیک به ۱۰۰ درصد رسید. این پژوهشگران هشدار داده‌اند که فناوری مذکور می‌تواند در آینده برای نظارت و ردیابی افراد، به‌ویژه در حکومت‌های اقتدارگرا، مورد سوءاستفاده قرار گیرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/ircfspace/2561" target="_blank">📅 16:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2560">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-footer">👁️ 38K · <a href="https://t.me/ircfspace/2560" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GnFNdFS_0EfKJ5mVABeTQtumGjFOe5l4LMvDB4DkRX6gbXHxpI7NTNrlRB_4rd0qDlLOWG0yqZqBxPiLDUpxdUNmJUtMfW1zFtWtxNjTAquT9Wj7izSp-EQ_5yuLswiVMwFPeJ35VNU4tN6yyriEXwDAnDn_OUMoDf09HCZuKkMx2T_h6c-mWhVJeomErdSs9oE4GyOMLXwIb-N6y6qBE42CP8B4J8-bMAB7OPOzN_FAl8pH8FIEoVxSzg5kV4AZSD6F53q7_3CSGKIoGUxdGxz7CXX2MvFgCvXRgl6kzddx4BXF_zlwEpXx4Pko-s_rekaQy2ERs7T0uv1uQdGGkg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UgIqRZkKm-b9DvsgLpbCy4Vz6zIexWnX4mv19DsV8W81nJN62OEG4-rlN1x9U2idOe79nz4mlyYcKDhU9kGj8qruSuhOM7Yl5PATjehrhi6eX-mpdi3NZgRSKS-GudS-Yk9AdDMjB3mNQsgEE9Qb4C0CKtStSJ9l_5BZqkvSZMMAzAwF_QEYJi8HFhfy1jp4-r6K_jNPJyGM-CO3T0P0fyemfL87HGpEl0zCJlRpxQChwzcYbb1BsqgXZ8IWxJvoi4InuMnQoWlPGCaUzaUVqaKk9tPyq7UCWzfwdh8GQcqlOOiHrm5opIkYZE9UwfCj5yEddrrI54itP-ioVuiD6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 51K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2554">
<div class="tg-post-header">📌 پیام #1</div>
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
<div class="tg-footer">👁️ 43K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
