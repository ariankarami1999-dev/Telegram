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
<img src="https://cdn1.telesco.pe/file/ohI3TyLOooGsifbWymmLPmItoN6a48cYAjQNru9uK5WzehODluKK7Vz5djf_4-zZS3dd6gKFnxsR5bCLoDEkN6T3jaZgMI0B3kqgDkZro724K2nKpx_CoFe_iPTG1OWwJrjG0WxaAixiqXgWNDL0KcneJrJ5Y70ZmVbbFzAuDNW8nku4gDNQhPZg-DDXdsKXIKOvKTOuS0Zy-xxP5LIy-OHgeXMXgR11WjegeI1Oo72Kh-pI0emQm8rEM1pLoxlLvYT4INsUQGFt4GqpZN0lvCbiS-QiE3DVloe7mmDZHdpTi5TwHYHwBheRhXuqadjtlHs5O0nSBe8YnS_tIMgL9Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 96.8K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-16 12:43:35</div>
<hr>

<div class="tg-post" id="msg-2658">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fx6BtJ2025ybVafJI-O2imMV6dg_A09-eawm1P8KtfGJqEq9I7TsxRiRCX9iEy6MTg9isfWFklLOdLTqb7WF9_EnG96qw6zDNOdU6yQoY654UqjAVxN8tpYjmRA9nzpEHJlTTngKoUWD2d17fbk8NILd9oqaYHf44NpBbDlLVRTnEFDOVF4RiLitaoPXAh5vML3g5a9fiInZ8lwVblWfBb1Ei1TUuRX6AiFYNujD6aIH1MPJB1AW6Th4XC0ajhbueqX8F4a4nli2qvwk0G0dDrUyEZWBdaw1pY5OGV93SoV-9WJYH83EB8FLmuPb1b-hHsyIPjmnoe4YGmA2ySOSSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گروه Void Verge مدعی شده با توجه به تغییراتی که دارن توی شبکه ایجاد می‌کنن، اختلال‌هایی که روی اینترنت و همینطور اتصال VPNها دیده میشه و مهمتر از همه خبرهایی که به گوش میرسه،
شبکه زیرساخت برای قطع خیلی از پروتکل‌ها آماده شده و فقط منتظر مجوز برای اجراست
!
روش‌های مبتنی بر کلودفلر، ایکس‌ری، سایفون، DNS و حتی تور جزو روش‌های اصلی اتصال فعلی هستن که فینگرپرینت شدن. تجربه جنگ‌های اخیر هم نشون داده روش‌هایی که عمومی شدن، زودتر شناسایی و مسدود میشن.
این گروه معتقده در چنین شرایطی به جز استارلینک که البته دسترسی بهش محدودیت‌ها و چالش‌های خاص داره، به مرور باید پروتکل‌های ناشناخته و ایده‌محور جای روش‌های اتصال فعلی رو بگیرن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2658" target="_blank">📅 07:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2657">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/ircfspace/2657" target="_blank">📅 20:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2656">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nj2B6gl_g77pPswdY0ny6TtdUz491ePKri0gFNXrUbiVRyNntVNYJq5ImJ5MM50uc8Tk9ib-yozXEELe7EwAUqqhFc1RtG8fqoHeZPt2GoYlBtUon1IOv1nL44Aq0MH0SaTJ3e1irn0DxFiujFxt1T2CbFfPJ5G3skAql6qAPTTTMvUYw8NEyH2-yyNZVzF_lDcnzHgcJCLchcIT5LAvJv220LWVv0hsatzlqbfaEBMu4UFsUEtjffCMI4Gon7m9WZM0co9NcpiGJ77vpQtiA1phYV66GfQoR7XYJm1Yu80VnVnHK50g1D2VrTfod-VaJ8FtllcMtcNv97Xyb8Jv2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس داده‌های رادار کلودفلر، از ۱۲ مهر یک ناهنجاری ترافیکی در ایران ثبت شده که همچنان ادامه داره. ترافیک اینترنت بعد از شروع این اختلال بطور محسوسی کاهش پیدا کرده و حوالی بامداد ۱۴ مهر به پایین‌ترین سطح خودش در این بازه رسیده، هرچند بعد از اون کمی بهبود داشته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/ircfspace/2656" target="_blank">📅 20:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2655">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/ircfspace/2655" target="_blank">📅 19:55 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2654">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/ircfspace/2654" target="_blank">📅 19:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2653">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/ircfspace/2653" target="_blank">📅 19:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2652">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/ircfspace/2652" target="_blank">📅 23:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2651">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/ircfspace/2651" target="_blank">📅 23:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2650">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iC9P5iDcsUgq4NlvxGV-E1nilc5g90ZW19YhEtpflcv8fJ3_dCdowUc4cf6-M-DiQ6tIsnj1V0r_S1lQExk9FcySNyj4oHp3kuTMuq45XTwxIBSqwbEdfj6yBT1irGjGsv-8w8m_jQ1YKRwKxvs876F1vt6cYJJ6fPGN0b9h6rfTz9Un8alG5TBjsmt9Zufv1Lzk06d-noQfprfFs4kdw1rZaAVHEykdowKzqkfZ1C6fvKsx-SauYV6Z5Fz6hh0chudhALpZto2pdvrIP_6GJdPnjVUcGLCp5eKBFX8FsS5oUpmkppb--lrOzm0jhR7w_aYMID_NKXTy1k-7Mj28Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای "قطع اینترنت کل کشور فرانسه به‌دلیل اعتراضات دانش‌آموزی" فیک‌نیوزه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/ircfspace/2650" target="_blank">📅 18:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2649">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/ircfspace/2649" target="_blank">📅 17:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2648">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JIRwRS-8A0EADEHCDUpRWztbyeyAULlBTnYmWM3-fuxeapYa4bqZ83D5NA_FXUh1I14aJ6org_I1OdIrDlXjymqDodIaYuJwms8xywk9axWCi7i03v8MwusLv3pwsXwK9afQiGwp7MfcJX7FmQHdEHdGFYi0RaQKDpSwoNEHXck_Ew_Ztzryo_0eRZ7PFil33K-hYnP7_HoVh6GNT4hPu3rfXuADB0valQ-r5zdC8NI-k_LlW8TJGDfiawaIoqOC4UCHRif61Y99RW1E-NtO8tiD2ERMPX6gEaxpH40Xf-gfjShp2cSHbdu9gtz5AVErfCxeoEmlCvfvObggzcJTbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا: هر سایتی که اقدام به اعلام قیمت‌های کاذب ارز کند، باید بداند که برخورد قضایی و پلیسی با آن به‌طور جدی انجام خواهد شد. /انتخاب
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/ircfspace/2648" target="_blank">📅 17:45 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2647">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/ircfspace/2647" target="_blank">📅 17:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2646">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/btaCmU0_13Q0tlqo09mTBAk5OeYnnmiYYN3MG9BCI7ObHeyiqHs6TDdRuqQsE4PoZ_urIqCG2YhhdqP1xtrJQeZXwrRE0i7ry6iE1iYCdHiTn-ey1dJacVmiNHDDOdmpNYrfeJBGwxjUAOiklAtSYlXvkiRRsm-KmPu2aXBkEh9P0_Sc9RaN6RHCKkIxF1JYq3w3IsN28lW05X0H2EJaV_UGI0l2JTSr0OUMXx2hztkNsS2zTjyuj8YKuqrtcJzxHoQZdGBI2Ud1OVUzwWqlHTORwxEJ3TSlIgNlORTBy6MYydGMrSGtuOnG5eQagiOe2nK5VZEV59LrqnCBrKiCDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس مرکز ملی فضای مجازی گفت: ایران برای اولین بار توانست با موفقیت پایانه‌های استارلینک را در جریانات دی‌ماه سال گذشته از کار بیندازد. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/ircfspace/2646" target="_blank">📅 17:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2645">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/ircfspace/2645" target="_blank">📅 17:28 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2644">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/ircfspace/2644" target="_blank">📅 23:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2643">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/ircfspace/2643" target="_blank">📅 23:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2642">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/ircfspace/2642" target="_blank">📅 23:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2640">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/ircfspace/2640" target="_blank">📅 23:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2639">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hFpyMs6O4bHxxEtqbIl8ULxcyOBdXnlSzW0Rn94Zdqo347uPd9Emffytsw57bNkPSWHlOeuUns1JiKUzrSOhdqmFW_xGYKEJx-q4JoakSu93CKy2_u2I0UqvplfTAayE5nCT0aOVmsS6KWixJcWu3xiRI-1wPNuUcF_bzQcJLg8IFrjE59K5oIEoSRw9xlxzaETaxjO84TtkOYf2paPVh41EuGCsqksSMEXl9ezw2BcfEG4kV6d5UpAZszcMEg9GJ-8M1kmoi9wcEVDkhrOYqS4vfKYjXzEvwN8gtMBY8tyyE95gMUp7ujE4FDfmirH10Z_uMqWGB4pnZDw0MmW3oQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/ircfspace/2639" target="_blank">📅 08:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2638">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/ircfspace/2638" target="_blank">📅 19:42 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2637">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/ircfspace/2637" target="_blank">📅 19:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2635">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/ircfspace/2635" target="_blank">📅 19:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2634">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/ircfspace/2634" target="_blank">📅 18:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2633">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/ircfspace/2633" target="_blank">📅 19:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2632">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/ircfspace/2632" target="_blank">📅 18:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2631">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2631" target="_blank">📅 18:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2630">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/ircfspace/2630" target="_blank">📅 18:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2629">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کاربران در چند روز اخیر قطعی، ایران‌اکسس شدن و اختلال مضاعفی رو در اینترنت تلفن‌همراه و ثابت گزارش کردن و میگن آشغال‌نت چندروزه که شدیدا اسهال گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/ircfspace/2629" target="_blank">📅 07:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2628">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/ircfspace/2628" target="_blank">📅 21:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2627">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/ircfspace/2627" target="_blank">📅 20:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2626">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hPA9IQW4Z-6JQ65uzFBwx12TEc1WcIEoeuqgPfkJOkpiwe-V3_DobUvPwphfwwT0lfYXUU9YK9Tf4YgJ9rgvc_3iEKyonuckVoAX3GNQdkin_X_CEvyVgPcNZ1wVckMt92A_NnFFr4P4Oh_T1eVvffAL0h3nuN57HWpP_tILwpc_ryYZm24Iid2c29U1bUO88tQSXw3F0jhz8ZLGoAuAhEE3glBITxBM4pKWfZVlwZ8BQbixm99I-YLX_LToojl03Tx7trW4JOM9mgh37XmeAfnh1bGSgTWbhbvvCB8-oBDxyWLgv7o98FLtP8csDdAV7K8IZm9OhXSd-Lpym3wBHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از دیوار چنین پیامکی گرفتین، ازش بی‌تفاوت رد نشین!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/ircfspace/2626" target="_blank">📅 20:13 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2625">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hT3G2k_SYCDwAPqROMQ2KYxyolFTh35E73UqNM_s4jUzYij9UU8dFO-DoYEQJrJYKbsLAC5Vo9zbykUVXc6y7lZ6sarMN5dK_derTf78WydI6tFMBiqh6MdoVmKcBRsGVoTy8RqyfqFEvX_NV6s7QoKbHvU1dFZaFdOj13dIZI1I3zYPoSiVD4TmlfdFDJc3OzDmn3TO6JG2dgRCc8bmHqP4UB1DKluLnvTxHBFqHU0QrsmGuLQtPckukxN78gCUzwrJjbYp0Y7yp4kxuyMs5G98PssOziKAa-Uw0n_Gg_p8OoSf2kcMf86o8uFKK_JgR4X_ZD7SaA5g_x1MojZJvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرامه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/ircfspace/2625" target="_blank">📅 20:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2623">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/ircfspace/2623" target="_blank">📅 20:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2622">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/ircfspace/2622" target="_blank">📅 19:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2621">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/ircfspace/2621" target="_blank">📅 19:52 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2620">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/ircfspace/2620" target="_blank">📅 19:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2619">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/ircfspace/2619" target="_blank">📅 07:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2618">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/ircfspace/2618" target="_blank">📅 07:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2617">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/ircfspace/2617" target="_blank">📅 07:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2616">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/ircfspace/2614" target="_blank">📅 08:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2613">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/ircfspace/2612" target="_blank">📅 07:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2611">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/ircfspace/2611" target="_blank">📅 08:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2610">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/ircfspace/2610" target="_blank">📅 08:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2609">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/ircfspace/2609" target="_blank">📅 07:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2608">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l54qWkV54NQpc_dxZTz6FlB-VT23HxTgXC5VxnynNJA8_319e_ROjOl260Ta-pxVf5dKaL5WqfCgjJYnb2QotMe9JFvfxwJLKxGGVL8nNitGWoJO7uV-AFI_wjvNDILcvhNKVx0o4gHGWCY_tO8az4g0RYTZ-37thS-MAb-7olwnXOSv0JAsWq6X8DA5ck4X3_Z0oDNycJiL8tO8m-mSCEK6ApUAMQYMdiflu_trSRfO6ZAWlsCeqSVoDGBO4ZJq3bmqSvITgEwm334h4I3G85S-IhrMTX8yOBKBb5QzvvcJDo7DhK8EO5AuJ7Qys5ZuMOCl7b9OhmiN_E4eR3iD4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/ircfspace/2607" target="_blank">📅 17:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2606">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2605" target="_blank">📅 17:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2604">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/ircfspace/2604" target="_blank">📅 17:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2603">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/ircfspace/2601" target="_blank">📅 08:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2600">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FHGO2vzAhdMT9BoXmPOOwXLviekuGsCjxza-dEU0XHdu8jqcC4q5IcwDE489cj8Q4Za3b0JlrZAoYjXfR1YknwI94DAUbNRj8RJ6BQQHy3T53qkH64HCFI0gdYGM_PesR4H3uJzCANakmxVwmSQS9CjEmaYXsL5DPVBDQAwagucNyj3HYj2d2EqMyrKLkVthMKJpO1OoZWdKLzU2Bczv1FF0Rd8vVy532mVYPH5nGXGphY116sW0IT7s-dyyhovztp7CBR-9beZ2EoKxK5pMOFwGKgO8sT7xte-jG4XMhQzUAnbQ958ETu9PFFV4Vq5_qw2SAudXA4AzjSoRg20aLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YjwoPR3f2stu_9ue-eQ8cYgk3pI-vwb2NXaIlWUzBt5PuiAGOcrZ4raNz3mFZSDDL5I2iAUZ2GDx6HpZQfOFW4pP3TufRoky7NwcTKoWkivs_KUj3AxCCR2wO4SueMQJDQ91xze1pJ4N8NIshRlnjEg7DHKCAFDcUZzBngGQwS9p6NCiwXG8v8F5PfAObohJZHIDz3SbjAvYY1ZGhAM-oPbFnUs_8fgMc-TCv7Y7yMpvHHq-DNDflc3zNTco4R_QOd77GQiB-ByB1pDwCg7b9DRB7Zfdp2fXTUqxfj1MWpzjIPWvO6nfYpRYhTb6Db12O9lDyqoEbBYomUJLjR7E7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/ircfspace/2597" target="_blank">📅 08:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2596">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jcnH2slQ3syim97hur0a1z4lxaDgHFo5gWVpq3hsP51X_V5WY-oCKO8stE8gL1TtzTTH53R9nRmI09iefQkIUw305fApX_IOXQOXvhj966W4wHNA5SxIEYlPzVs94fs3y-wqEuGuep_7pCFyysjdEa9w5PmzxpwMXBgwVOjPQ8HvfR5LSDOy3MeszE5Bcabfd7Y47nQuhGy13RysJC9EiDOQi6d10IQj98M4vWljHmsN7u6mXYpz5JHZ2rCTQOPrgWLfjggmMvEcQo6RyAwoFj4rF3D4n1vb9cyNG3GKOwGpFwjZwSiCrTWfTtrrGUS8quuAi5tAIum7hJH5jDRT9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/osNOc5qUtK5eE-9YUKzMwsvRQ8VoXhB7uC7ezdRv0GA9W6hdevhreNMeVqSnk08t-_b54TEKa6WhrQb7EJsxKwtrFsHnKRDzjjyVbUvuEO5kNVKA-QQ8Va34zKAcT-VxiN4gEGdy-m3pCpoUlnmdLUh116IfuXTu1XLB_QcAGtlx4AzCpDZ3WHSD7r8PcdYZJhTyVHbCUPjWaO7_hsmfQrnILuTpF3-VNPTF9YTd7WvVKN5_lpMP5KfYj4YVrkorxiWCN5BhE_4uL2Qn3xdJHhEXvJxMdgPnzgmpDDMkbNSLvmDcJn0866n1YXQfLzRWpz9BkoXpul36EC-UDbYlJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه پایدار است، یعنی به همون آشغال‌نت قبل از قطع فیبر نوری در ارمنستان برگشتیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SN4HPhMfxwgUZ8MTHnctM2nQgA2fVcX6GqPxCVMKgcG90Nkr0yZDDKSmrVox-_Uqgbnz0bJ312TRtW8HxJVzYLpjegtZoGz1Gc1T5IUlRBoxPnpOM4JlRQ6fprs9MkYH9GfmRyifBE7DykcQmGawSqn_JPw-GV8xMXPQ85AjuGo2jud2VdPZiuW-TQVSpYEOjDZvc-NeR5PuiYFfpZ0yDN5QsZatHyP0OqHjDKSGq-33ZycyOA4wquzLL9JvoHFfbvchL25jYvIjHmkjJfHR3_x-_ot_M_lO8ErNeAP615fSxamBiNRSb8BGcVtVxBR3CYhzPFXIkXlMIPi0v8s6Jg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oHijIru6-8X9Llm4dBsWs9AHL5R5IhgH_ztXMkee8Sx2ZKYuV6U-NVSK1x6gaLT7Z6sJutXu4kcOyI6btsviu8BPOGpm46U6N2p5bngnE0aWH734DWNDxr7FZh8z6t1T9A8dIcY--8hb6d2EoTAyAtGcU5s0BL218JCy04YZJLmJqbNLS5sA7hf1c2cT73ZNZzEY3ZaeHXURk0FUIsAHLDDCckgn0rc5w-kvZdACxefDn8Je8jKCCrdy0F-zM0N1mwaZuSOT3WmJ0bc3CdLqmGNt0nRIr2V9cgk00TKfjKZL7gfTkzdKQ4KnnlSofLMkUo9TFw-KQM-DUjcjew9UZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2593" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2592">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lVdEXNrNVGMJX9v_nLV0rlf_UOWqmqx6z8caxHz1m_xCk0lojGO4wpMykgBu4i42t3_U4mwnQpn7ovPbRLfk9HQGOA44GiaMp1f1aop4P4WxQ-q73z404WK9X-6dVfJ_Vr5CxBopv0FPt8NJTmAC550NYHc3lHwn5VPgzbTH-HnwE6CC-s2CpbJoT2xBqzGuQpQSROxWsaRRQKioUFFEsf6R3OHj6IHOl_5Qxhv0fiH8rA_9MneZOD9S0FHuw5dRZDNulPwvqsQk4Fdaf2YF2HLn1GTGCoLN3G7qxpM3XTgduJj5sm0OlX4EPhxCOFhLBv6ZnviTYDIONrF7hbsT5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/ircfspace/2592" target="_blank">📅 18:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2591">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C42Gk5AezizB-E_RJp9QHfEWFEQvv5sDkzE4Xx348ZI-K4R7VHdd3IHODzBY0qW686EK3DbCac7nzF6BkSabA-idlKjgUXQ3cgff07DY_5Tny7ISoZsJwn6nEm1Gb-ODKrRokOM4d55nD1dJ0VS715DUv_jUjRoPAHV7Cxz4-iBzY0O5q4PUBZl-X3t69oRNe6rqQ3hdc9rnNAyo1bcCrAiiMx0y5qzf0gFEffLaYARCAJpHr8mAOo7QYfdCtwo1IyzfWzF1D4IJBVLS5nXvCCTLD7u3d5PAXt4of4vkq-jZuqzehHpbiEzWlOCz5IocEWWRQjiAlVJyMFpi526llg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه کد QR حساسی رو می‌خواین مخفی یا مخدوش کنین، نصفه‌نیمه رهاش نکنین. ممکنه اطلاعاتش همچنان قابل استخراج باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/ircfspace/2591" target="_blank">📅 18:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2590">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DKuqzpcYjzy2o1b9Oa7vde-uHE8ITtCwyVszP9TCM2JkMH4oMIrNIxA7X4P09mnMhEIjQe1dl6C61mJZqP8QgNtG3mrZEiN6XzedRh5LmW3r6LFKOPtNylbVlvhALG86VJY5xq2yscBG8KXAX85fHpLd8INOm0O4aP8Sw9FjDWNxF6Kt1RBQ4FKLURzXGQg3nevdB2gDrY4exKXrtTexeSbM9voVwp8ePRk32r0itgnSQ2xDeGrXJiM24ytYC64F5DwmhHCSrm-S3gpp0a97ECZL8hnrldBliXlxPIuYnsVtsRKFf-rmrak2aMOO0QJhmOMaNi7sv9OcfBvyIJa_wg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CUaVb3S1CC13MINk2l7AdnVVLp8hwTXk-PhhtgFsFxPy8ctGxiu2MRuE6ym_1m_r8O0P71ayZpT3rLrRDvYq4eyf0mIsz9vg4mw4Mgsxo_1sYz3T2qdRLP-v2bobzAFfWeX0sQT3lrzHHIA_tziFbrw0RagGIfN90ln8Zp7Iok1XXrbfpXJyOiY7sUO3-2jQKfyzMXlPGm-QGfsakTqdoyvqU4_yFqGqrd9c306A9QFUIbfPVGheI0F0pdTknaziHIvcgHNa_kAngoExaWgpr9bMhdKSq23VBBsm2Wf-b0fFdPcMqpie0RnwPMlgGNUMlEn_TbB0y9CDXCxfN1JIJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Jdcw9wrnwJGj0BzAN-fq0H2_IkFXy9UdbH4__D8btPE5V-_-uqTfBkHrGcJgyJM_pfSu5mPwmM-ghb6oPRbz9xd3cqCyLp1yAPYKVYyCu4VCIrZt-99XG5hfuY5b10XtxvGHgMRc6HtNi7jYBKixTfUQ4AdCTwFwTGgyh62-Knwjf-Lnla2njENwkgktwk3XQy9ky3iEQRFQrs3KJFr106NFvV_3YRWH5exp5ZWHU0viqAksijaiX7oerr_3Ezkz-ZWkThrbWnzpDxEWUi5tpwcH1J9PPiaaYTi_kn3noKC97e2trQVNtRA2UnAb7kQrBWXJFfBLQLOLnHs4BLmnHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GdD1n3_lDiHqMrJoakMQhLb9VtGj8cFB3kbVReEy7_Zo7v_rFwuE1f-J9vQayMwu4MORlHr4qBw9P9XhghQc0AdaUZFUNnR3P7HySU8mSJ-MENaDuSoqE7RiddE-iwL810-bQi1gh41p2b8C7xwIDMCn-WlbXIl8fmAJ8hzPRvRbtJ-rnP4px0IyFae5KfTo9qstsNM1FC2UBvpN0y4Lnisp6Mhu-ylx48ZUMZwf-U62Ffc0B0P-GU7pnmOGFC-7pHbEr9uhRGIDEA9kiHItxAHhLWwFiTzjcs41ZWNq1aRhoeH7Uv19XCDlay5m8DrV-RTLxslKjUwfcrdCHDHwvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z2ax6kPZrDuGWdpxcUj3ymQ3W9flG8mEkbDeWywcnCb4gVq2EaOg3XBf1nB5oWAwDkX6Kw_3dLLJc7K9yVY6tg0gdamdHGwYm_reFaEnYWQ8MmfMdWEt_PJC_Lyv9GpskvzLy1W_a-TYkwfzTS42KXta2Do6-8rFd-cc2r-re2WNWNQtErsZWPSFirMIrZ0c9J9ystLL7vcFcRwves3yYwIQVpCkDlMZRJskKP21XqPRHOkZGzLzJZb9TuB6sHfqdBjYQ5KR-56QjnE_2X9O0z1dJgFuQ4fNs3dRwbWPAG98zXmACoG5YS0qPAWHE3MepihsiZ9LWsSLRTrB7OrDgQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l92c69jNyc_LFb9Gi90L5u5s_VzjM5tlSovNKAKHOynJYwHfj7tSKeTmtycJg0r2rnc4yd8DiBxyw157dGsVmAyleZZctfSucDeNvVS-K6eeGzA9zHm9NYjKfFIsmBM_Y3mkRte-gvI_aFqo8aqEY_OrKcPPC71L0pMu_zWqC6Vug64liJ9qPhQ7_F3rD5VCzs6_zQc7hR7u4ttsnB-D3TNV-PezMT2ASxAVMrlk-KD62z8zOgMykrg-TgeaOdEZuLJlAA-dtutStRL5Zm2v6YyeU2NU47xIY5LqodrDECrm74FPOeMH-Dw1kC-QoMYG-EIFGKgp5Qq-cpDDud5L-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M1kBsxcVgWqq9wthMEGZXDIoHuuwmg3v-kRdQ1PWGZO0WGcLIecYvneEqN2wlEIMtnuqmXkdNJXG1OGBbAdiz-GXgcOPQ3DLUMT1ehVX2VFdLsUBmYK768c2W-6uyTFmrp-3ctz8eb6B9TdpsykDMIXUUTwklMPpRiC1epQFAzRgcFbzdIA7LMO-GUKaW-qNDVQXcw5hfp5xqT86AJIZQ9vuHBNfprAgHcgo88DZ6J5nwFkT9F98YMSK8tLLWzFQMI0l77snmGhMdrUEJcVgb_tcIHC7uXhDkXT4CaQM3xvkk8_XxABME6f7Qn3xF4x8w5A_Lg-2mI-sZp4VMpu4Xw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qgLwwmplHagC1mErnH2Kt4F-PvM-umv3pIBHyHXy6cYJFCchQDqsJz7D_vl_q7gv1PEcs3vHKqxnvvRSNPfGD1JD7TxK_9_u71vnAAIcb9KKWqnrhC58U07XRcxo2gb5hcnjLTqenoU9bI1IAhlfPIAgx7qrLAXRdO6_-LIzt1e0gGBFXKAVPWTuoINR_aKRcpAVTomGD__7Ahha4l254nBudmK-xqppgZRQe80T8yzJ0jAfPVKm7e48QoON2HHJRPlnWFONT2PDrGG_DbQ2cJH6dp_vzHFinzESLaZcA9qjFhAkvoU97y-HqZElF490Qx5VffugaI4_f-s-SL2clg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hXOktGOYlrS14RCNubIbAmfeobtFLFpPllfp5ZM0_1BnzutERRFTex9l7bc8Ao-T0BixEpk1rfykq4NUSbXAPwhKHslSiZz9YFf2flm7Eg-mA6RWtM8ZjmBItLLlMdSoS2tgbShrWeUoxcE3UeWI_KaonL0xIgOqAZUrWMTLitf6UgaXtrf-cmCCznCax0i4j7kBTqdoV2mjVGPA-cvhXMt4rwO_JtKgWidJA-tPeP91rt3cHtMCSRL3YBNJX5TLyd6hkqWPrb1g3g06senQbYZnrcnyWPVeQwP4vVMzJayonPSvH1TlOROeAujmq-QPsVMGiszNzucZAvgivqjqMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sy3K5388P29medZLYFumXa2uYYaBkwvkZYoqRHfa4_qg8YDy5QQQXB_j8OT8lGx1_9l9BJg2QVuM8Yc0ubngWYEKXcTlasJY8O5MgRdXAOjlNZ6R9P0Vp7kx4t70AIjLfiQszLENwrSNsMBE9OnPZqB4HmUWzYFseBWEzCjLD-bPgLOKIP2rbom_cJKRRKAtyieEoDsKf1I8z-6Fh2ePN8dhGZJuVPfg4WqvGm-St1Q5CeMqDFfBfkUuPitUPx8uZzmRdhI5T9IUQQ5RbZK4Ik00kFgVZZteXmWAUZNaO7vgvbSERCvmxd5kmqtxeii7Xhceme_997LLhPwWxGZi0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tZomMvmeuujFR3ZxXcoayFvwsfrTbli53x0qjuXYlkcIsfXWiNGtcDhjwcgjUNRjTapIBnBjd0OI2xZ5ZVqpX22_CPP1yGzDnqUpVqq6J1ID3QurBEvGIZmOjt_It83N_RJW3QoCOIHnxLEZ-ox5Ung85aNJj8n1zBN0NkyEMopKj_F1dQ9h-x-eTUMdrvXniiS5eKNsRb9QXzLsnwKCUcmv-GzD3we9Wz-9-rzlMXvILsH1tQTTXKg4Wtb9PaPPaD46cQ8Gmvxi7eW7uS80Jl_GdP_TZvHGpBD4MtIv1LOfKNwvwBoSNFES8cAXyLPKYellUjueVtKMdZ8Jmc_7HQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z2YmLcFfIk5owC85TeDoyFYEBz-3DeI83CdYYKZtQ_KYlEz6atbIYQQvFIePkYmLif8CfGlpRrHxUOWbADNoZ3FVgFU4BmX7SOuekTbgtreVPWzkOrhvtoT2W-pxzO4Io0MfmPZ4-lcnNs4bc5r-w7wjYme3779ZNXd_p5D1Gy0LJFt1F1jnsxsinl1_ZvO4V1p537VHPMqb0R5ybrRadhpzmoN_7Gg8weYKx8VwdTPmAqQHnm1KQY-VbcsZ-d958aoGO_qe14teEU4lr3ZlcIUDaPKABDCnasTvAYiBsK17BFWJMSZ6dHC-yWqxl0mDwVrAJfiXwFgimh06avWeWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pZZsgxPujJovkt1AslthE3GM4xVZ-bhKlRUcoy7ztEjq7Y9iDp1aSaNFeXxc8wRu6xe22oPtCZ0sXExQyXVeV_ZYz9pxaPZwVgrDe7exxITx06pFwSVBXi5KM-lsJ9TuJpwgWSz3PFgZrSup0h1apsiMTlQdC-B84j9pL1kvfbcX6RHDTLmo_7Zc1fWkxJ641xZNoUwha7QW-lCNBp20x_fZbEJPKqKhafpsl-Ad30jVCWypnMlG_yZ63LTkU2SLwAHVtnt4enm0vxmEPFQE6qWvoQpnLSU6v0yVeXGLjStuBOtDxjduJARPK2DcDX5IISMf4Q81ck1DbHj8Yrghig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jm-ONDdP4UPB8V-nA563qufU6ei7Q_tfIun6d5httsDg2NjhyxcGn8paqDK_BMr_b28VU2MrBOVp046A0SXTRZwKHsb_i20GV787g42GjWEAQKZdzp4STZIZxhnQyZOlfXDepq27s3UnYrOH144WUwKriHAd57aliliCj0-cNlH4FqZZ5MUMlMrCLAnfjWqZmYFprmG3nFbUVn1_0giccHhFo6TM5x3EpRmN62zLYjU3zwbMrnyTgeyhAEATAmGcWQUbUMVtIwiu6i9kWekSBUfqX4RewsZ6MAXJ_EcXSH0vmz2BM1r_76h4-P1BkcoNvgAomilIehLe4o-mNW9Gdw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VQOBeopNpRlVQPVdbjFGVoc6MwNRhcIehldXUKR6SBuGbJXM6VxLIIWizd9ivuOlwgN-igZ2bUzdQBRHkUK6GzG1a41l5QFIt_LHilnwuikMU083PEhH1n87bBYNIH6yOHbkIzwnljW6HXguCGY1XhNYcyh63AKcKkpjeWyxWiihvK4Qnf6FFhshuCZhXFvQWZUOfVDS8xR96wShdi9K7H77clss-6Xm__tfUdA5Jjxz1FPeXTt8LWEARiHobzhkUDAnrQc33Lh-ctoUiM3pvvUXn8HGCF0vbKi6HYbBBCQE7oYjQr7t1nNPK277kSWEYIR_onMunU95c286SZY_oA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/stfpn4NAUk62rVukzIStCjSH2KQlM0ESclRaMM1866U2iRkf-KD-jk7OSXN-zMcmC26vJf1_ba4QR0yNPbxnsXVz5Ohpg-SJRYPVY77XhGx7zhAT8WqZUnkvx76czMr1wGsqjLghsYfFyq-CJTaHO4dpdezkKqUsL4qAi2IzMMsNSqs1qvEQcbG7j2ma_L_MQqbb96qVelDPjToivfkaB9B6Su7g_GbgG9ICE4RxXo7ZP7jxRfwQMOf2jAXRLsWOJmzxMq7XipZoVHVQIKwOLiJtbk6NaTQQgDIMN_JkxvBqMmOKg_76uv9TLAoeEWjlXK8uxDyN6HSj4h0iOoljTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X79iMsvy6e_Fm2L2qaEO0V7c6usegYRWGQuDx_MbwtGjVfP40bAQGHzaHlPvsvjVg8RnDueLpPOLx8v75YQOOrMiHaJvo0tg2TkjtqMzrsBZ3fwTU5nofWYuKGp_2Lw6YdU6afozLtbjYeFxtQb9MwooAeHtuL4zymfc0r1bI5xPer5_zA_y29H3FTtEjmOFxqUvky-QQ8NwguLlsP8snPGeVVmoEdtbLCk1HyiuovUG6kDFn1pXe-qLf9MSdY4HJM3mHO1MkCaYFx0t8-4rtBEB7-CTYQtt3iQjW-azIcP4gcMNEnMIeKeQ1UQ8d_K1i2Er3qIVNko-zH91XAybdA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZST3slTmV5K_FTMPjySn2zav4Bsr5Wn1Q3SREy366ADmgzz3weJRii9D9SCiwljIB1yBirorGGnR1Z_DQj7ZqAapgK1LLW3z4wDtN7OJfD5QTs3GZQOzPPBWipLzw2HbPiKukMdKtBxgSHMwqQoTW72o-n6mCmhl_M5YEvbFOCzPE1L9u36dTpkfiZIpVM_Ms6RliszRhs8fvpcqPtF_V3OvwZSCO8PnrEnq63bkpbTEYTjCuyzGAe9tiLgTswwryQzm0xnivwdQEUA6g7os1qtiZdlP7Ajj2sid_w4lSpy9V1nDsl38TWaNWqExY5gAL_TT3G7lBJ5365cKTME2EQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FYUow3tqB6L6wJG6OlRO13XMdVphiAa56k_WrRV_oETe2jiUzL-rRR3VfX1kVzyt43PGmprz_tdgDCkx0aAMYdGdc2I6-W84mckJsuyCuDaxpL0WMF9mPVcdy4qsJq747_NIK7hxl0jBsFiox8hp38Z3QjL6wNFiyeNQq4mAVlZvcVAaXQYc-ViFX3QXG-1bcA0k3KxrZw9xSHPPTgHySRfErLccNyFS4HVJ00mCYMdoKHwDNfP0iVTwvcb7GVJj8ZExlT4TyZx6UQw9oVDyYlZNK9K6DI3zu0_OeDYXsX6ho1Fj5Elz9TdjAktSn5UUSNibE6xSzatclMIH1j2oWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XjBwkbAYfrj4KjoQ-wo_Bol4wcw9KiyMH_vPsUlLLc71xNDjF6TQ7azgMRLUk4g-7BmBhRFtNqbie18cT13OlKOi96wdGkFLZEiqkJ_tyxQHjdPNlx6t8nVXm5se8Ue8O0WCLxYiDKzCaZTYWDehv3ykr3edVNsXWxNlxsdoahD4sh4ZRjxo9CBlCMqVpX4_LAOC5TFdFyfpOs6OQlMB89Omx5UJIPDPrULVT49kkGCFV1Kpm53ZOV4gjaRy90pjPiMiAG_QlrO_Xcv7L9fjVCUkJUtjWzCgxGowmB1QRIYXXCjW9AftEWxRuPJRVcLfbQKWliE3yEz-8riWo5ENFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZliVzfiHJGPAH1vhaEAfZeN_H4qeaktFdYFyM-rlGToGVIZXJo6ZWYdBLvElWai_WonHjelXGjQH3AF_ScnbKHysW0GS8Yy_NhxAdiZDKNQSwL2X7OcEsHdnhVmO6kZbsMlsWR1I1NOUZ4Gu1uTgr_2tpp43TLMfTsZthlDGeLVdFp_463wOvSdRZOfRwmb0FB4sDovn8Kh-8WO8q6N7HOtRJzeRyidNSHJhG1FWV_z4txzJ3is68R63JAqkIEeJSG5CavVNmtlPEB1DoDcqs_8NykLvfsotgHcWO_QQwM2gcEGbgOGYehxJEaAv0mv10h-2B6hhNZjajSluuKIB-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nG21GSCQMRHpKRbK9RJXmhVhubw5kHhAIsJUjANFvSVWnI7UZvlnVkyVWoDoywqZPXoD_0nCsieDnbRyjQlBedPO1XUBMGsvrAmw85ckiTHMOiW-rbkk61ZSjVaQZGK5Sr71A54k-hqVxbVHQGVTgLmCJnr1f5wsyaUxoOGURsdwWxavDqSff8DoudzxTP2_aJt6FriXOeOsI7DVRkjw5vNzRGZFx__4gFejFrcuWRYnRdB0QATpriSGUjbrDTeQ5zPfs_tTTS6wEdf5UPSyleMYP--ggIQPpxg4ut9lHa1xCYgJ9WxPbX_d56EACoTz-DPUNTM2EVIgNlMUDlKxzw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EKC7C03c0DlZBBGa1db-Yd3nkizqvIQSHFcjy3c7ooaHrfVyu9inw9ybV5jpoH0jB9udxbw6BOu7YNLu1aNA_V3wBPYMpIHr_lIw5r1cbceFdZCT2npoxPlRdAziPSTlriyfyjh0RuTPLRvB6BvewqVNaCChxmXtZjiT-6oVBVjtHhrZX3_zHTS6jT9nhRcWoedRoDDrZJN__0SOyYn_r8fZgxJ5MWBWCN6onwwCqswjzREw40tBD9hAmjujQL5UfKBtY0oF4WfYEn4pyEisOWutzQLki7PRADX7pW9Ww14DQuSVUSF4h8ho62CS8xjxOTSltKVvrgMOthZ8sEKuWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l56ActqQExixmUAkcGI3hLUzmnDN81B_EUFv9lNR2DV001nG0GIAMuuWPIWu3fwds8j27Om7juzW50MfM44XeagV4i1x87-2ZYbDtUq2cSvjj8T2554RyEy1uxULb2AGD7V1x51kGOG81z6IHiW2N-8F0G2qViQ6o_P6o8zACa9INo4qp6km4xSQAqDGwUMIl40Y8Nlqctj_Z3CWJrQ5aCC5Hp6j_ZlCgLrsMD5oR6vKmHI-Yld-2qLeSkdl_6ch_Vc-DbzhChXlM3nE9e8iuTPYr6mDHXNfFYhHvu41lBgot27u4sBYChx9h1NQ-t5wRJCj2_yYkU274g-Ob4LvJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Avw_WU7_qHe_yt3qCJ85tVnQkI8Ts615kfbOnpBKx3JN3bsCySa9y7aCipJSF9h6TN2fiyYawKY3WP3JXSuTaviU7aRH3nHMTsZ_t6jlh0cCE1u8Nk6zihKPzLCXNCMX2bdvq18f1pPUxZ4bxwMZtuokZBJZKPkkiCdxVnV_7jPF7i_gKZg8ysfSJ1ViztB2BnFToCR6E0HpNcwDkjZ8J2MzQ4gXOddJqwmCl7cXmQTNzCGo9EYOnUAhmqH3TxvGOPRt9kdlmLgqq0YsszyKoZrQExEyGSSTYhpzcddX-9bpsLZI1VO_tpi2xSrnk2aYTr58dFBHS8HqRBpqSqGlmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-post-header">📌 پیام #1</div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
