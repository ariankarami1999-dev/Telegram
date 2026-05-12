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
<img src="https://cdn4.telesco.pe/file/lowYcSn0XK7aIQbaTOU1ed5wfYafMkO27kNDECxkMbv6mh8EZ5ryeZX-3U7fH5gC6JuobQ1Ntxbo2hHKcyMLQfa2nHd6TD8KmqzGZ3ZHxYditFOu57loIvQ8pcTPNUJsqwgn7MbbcZiXoxHbHSGuNK3mN4RcBOL2IaTaCk2oYlSB2lH4IfNYmwzNBRfUISgEzI1ZBugwf1XeUqpsRwdkIk6sAb3-vFOXQ5fOzeEBpZC8OrK_G5lFImwXeQcK4CDy5naXQiXnOnsfgarGoDiWsyIuKX1bAyQ8JupI8BKQlHSP-FbRGfr8VNXorcfN_T9t_7mQdWxa-03kCyC8oRSLkg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 963K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-22 19:27:59</div>
<hr>

<div class="tg-post" id="msg-119520">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f3nNlanPAbsPlTSo_3bfOX7SfYbfheXshni9_keAWc_IJAZ-Pb3smoXGjRFxUYeHgNaGbSbHhOEVauY1HCn3lUwsKZtWJ_HiVnKW-YQeWKJLsTVaODfhlL39xlQYRya0-HQ3e3Q3dXll-l7iIUe6eZlyC-alSXk2oMZDkb4fXwMNzPZOxB1wtQ-t8az6LYsH3ZEC49dAzj2H9Zg2OvbIcfk3jct_HXTEdONLloQy6wj200FXudfahQFvKb-xiNQGhdMXNUU8y1ZlbTXwK7vKPvcLTaC_WvZZnf6hVTGKmFDTRcDdTpOJ36tJTIY74eSR1I7DDdiMRHx0Ay5-X2C1lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فروش اینترنت پرو توسط فروشگاه ها و دستفروشان خیابونی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/alonews/119520" target="_blank">📅 19:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119519">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4255c4c9e3.mp4?token=ZZpojpYOmVRWxeGgv-3oweT2AZEyosQNbusWGSBscmyyatQXaC181U-t2czUgK4Tv342s1I2IyrnqYwU7lObYWO8dKTLdlvL51bmsPuudfFWe9_0MkOSzCMThK3cxD5Mb0y0yvX5kNZ2LL_LvatqyTVg5kMdTG8P3lf0FOhetCuKBXSH-eMr0omSIAP3gp9ZW6n0P2BidTMpYTb3ojflIZCIAEtqc02yKoVlQuqfCR2gfh22zhUJh7vXib60Qy2FltW-DvDV1lykiOaohhy5_7I2C3awA_0BfelmZX2env4yKM2DSmnXyxDaXibomUi0b4VEXDgK_qgQr-89r0AIxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4255c4c9e3.mp4?token=ZZpojpYOmVRWxeGgv-3oweT2AZEyosQNbusWGSBscmyyatQXaC181U-t2czUgK4Tv342s1I2IyrnqYwU7lObYWO8dKTLdlvL51bmsPuudfFWe9_0MkOSzCMThK3cxD5Mb0y0yvX5kNZ2LL_LvatqyTVg5kMdTG8P3lf0FOhetCuKBXSH-eMr0omSIAP3gp9ZW6n0P2BidTMpYTb3ojflIZCIAEtqc02yKoVlQuqfCR2gfh22zhUJh7vXib60Qy2FltW-DvDV1lykiOaohhy5_7I2C3awA_0BfelmZX2env4yKM2DSmnXyxDaXibomUi0b4VEXDgK_qgQr-89r0AIxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
واکنش‌ شهبازی مجری کریح المنظر تلویزیون به نت 5G افغانستان و سیستم بانک جهانی‌ سوریه:
🔴
اگه اینارو میخوایید داشته باشید، برید همون سوریه و افغانستان زندگی کنید!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/alonews/119519" target="_blank">📅 19:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119518">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
90 نماینده پارلمان کارگر اکنون از نخست‌وزیر کیر استارمر می‌خواهند استعفا دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/alonews/119518" target="_blank">📅 18:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119517">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
آکسیوس:
احتمال حمله قریب‌الوقوع آمریکا به کوبا
🔴
تشدید تهدیدهای ترامپ و روبیو نشان می‌دهد که حمله به کوبا می‌تواند قریب‌الوقوع باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/alonews/119517" target="_blank">📅 18:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119516">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_401KWbmyFfZOybe3kBjRKyOpqLHtiF2QR1HH9ojm7TAKAGWsJYW1ivXZpiNa2TIE1jkjxR1KNQI3-VnExg4r_XlSEhB3IKz2w7c_FFBsPe4CxjuiIU2oP16ri6Ggnb1PKlXFHZT_ilcXcv-wNEbIRy1jr8KE2WUN7UP8S9Fd7XM_4BTy2GwbylihmKi1tda0-cqHKkKHDQYIidcmvOSB4U_c41xvz5hVxolitKrnPhLgaclurFyOBtDdwYbE7bHczsWlnmhJ3fMYp85N3TTE3HMYMaAKI3psl1ZQlG9_D2pF_rkJp6_Xc0wvpWjINGz5xFBsexrK-Jv8FClMhAlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حاج علی دبیر: تو جنگ بالای ۱۰۰تا موشک اطراف من خورد اما شهید نشیدم، اما من عاشق شهادتم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/alonews/119516" target="_blank">📅 18:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119515">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnCMB6-nfGyCI9CWNntr3mRkeucuE2luNeuAGGvt5JviTODSqdYvkxjvh7qbkAe7qecQ7J9MsBgCIPY9kVyt-e27Ga7FoFe9rGGLts1WzkoFLUvmP8zSv0qk53N-btlHdG0fvkLZSiu43GHCwSgTYcPO7DCFBheE3WnlBHcbaQYAJIJNOyv781xFTPTF09TD3syAtTHPxzbhfSuK_BV19MseR5pzYT0fMeDqQPSts6xPJPZSHyEup1KhfJZ402GA4x4v0Jx_1IXWQMnNLUIZDQPaf0KrhpcI9pGv5kYAoW8NroTZ4wubm_ESwhd2NaKBmTajDyYBHA-cbBBmbeIsZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تانکر ترکز: امکان ایجاد مسیر جایگزین برای تنگه هرمز در خاک عمان وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/119515" target="_blank">📅 18:02 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119514">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
تورم در آمریکا 3.8% اعلام شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/alonews/119514" target="_blank">📅 17:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119513">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
جایزهٔ ۱۵ میلیون دلاری آمریکا برای مختل کردن سیستم مالی ایران
🔴
وزارت خارجهٔ آمریکا از برنامهٔ «پاداش برای عدالت» خود برای پرداخت تا سقف ۱۵ میلیون دلار به افراد همکار با این کشور، با هدف اختلال در سازوکارهای مالی سپاه پاسداران خبر داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/alonews/119513" target="_blank">📅 17:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119512">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
ترامپ: من با نتانیاهو خیلی خوب کنار می‌آیم. ما شریک‌هایی واقعی بوده‌ایم.
🔴
بدون ما دو نفر، اسرائیل وجود نداشت و بدون من هم وجود نداشت.
🔴
چین قوی است، اما ما از چین قوی‌تر هستیم. ما از هر کشور دیگری از نظر نظامی قوی‌تر هستیم.
🔴
شما این را در ونزوئلا دیدید. این کار برای اکثر کشورهای دیگر سخت بود. ما آن را در یک روز انجام دادیم، و حالا به آن نگاه کنید.
🔴
به ایران نگاه کنید... آنها همه چیز بزرگی داشتند، و حالا همه چیزشان رفته است.
🔴
ایران از نظر نظامی شکست خورده است و احتمالاً هنوز خودشان این را نمی‌دانند.
🔴
اگر روزنامه نیویورک تایمز را بخوانید، فکر می‌کنید که ایران وضعیت خوبی دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/alonews/119512" target="_blank">📅 17:29 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119511">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
عبور نفتکش قطری از تنگه هرمز
🔴
در حالی که روز گذشته اعلام شده بود نفتکش قطری MIHZEM  توسط ایران از تنگه هرمز برگردانده شده است. این نفتکش دقایقی پیش موقعیت خود را در دریای عمان ثبت کرده و از مسیر تعیین شده ایران از تنگه هرمز عبور کرده است.
🔴
دقایقی پیش بلومبرگ هم خبر عبور دومین نفتکش قطری که حامل گاز طبیعی قطر است از مسیر  تعیین شده ایران را تأیید کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/119511" target="_blank">📅 17:13 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119510">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
ترامپ درباره «گرد و غبار هسته‌ای» ایران: ایرانی‌ها به من گفتند، «این مال تو خواهد بود.» اما بعد نظرشان را عوض کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/alonews/119510" target="_blank">📅 17:11 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119509">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0a5e04443.mp4?token=HlfpbsGX3_cBoRV4gPNF_QItL0_UwxTVyhCYPdem7prBHCpUm1zEhlnMhvg8zGFrvNJIwCWq1AmMeZR1ohYzrOBWXaEUznOxrW1ZeDW_1JH2bJKd463UWskn-onemcs-kjuUWKKDC4z7VaytDPfxBqrj8uCYr6JOfbbdT1nDEioU3rjEy50WjDOrT0rPwMGsOLdFfV_cl0ow_7IpWXyOX0V-Gr3WJ2alSIDL0M9nOuoAXeV3GrVd6-37pTZ-izqyt_GJiF9ScWTveKbgyKKDKMQv3lOKGHQx4_zPKE7LnnX-NNJ0CFGPWJHaohbKa6Kgc6E2PWA_BaDyZdPwiyrHVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0a5e04443.mp4?token=HlfpbsGX3_cBoRV4gPNF_QItL0_UwxTVyhCYPdem7prBHCpUm1zEhlnMhvg8zGFrvNJIwCWq1AmMeZR1ohYzrOBWXaEUznOxrW1ZeDW_1JH2bJKd463UWskn-onemcs-kjuUWKKDC4z7VaytDPfxBqrj8uCYr6JOfbbdT1nDEioU3rjEy50WjDOrT0rPwMGsOLdFfV_cl0ow_7IpWXyOX0V-Gr3WJ2alSIDL0M9nOuoAXeV3GrVd6-37pTZ-izqyt_GJiF9ScWTveKbgyKKDKMQv3lOKGHQx4_zPKE7LnnX-NNJ0CFGPWJHaohbKa6Kgc6E2PWA_BaDyZdPwiyrHVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هگست، وزیر جنگ آمریکا : ایران عملاً تلاش کرده از الگوی کره شمالی استفاده کنه؛
🔴
یعنی با داشتن توانایی‌های نظامی متعارف بسیار زیاد، طوری قدرت‌نمایی کنه که کسی جرأت نکنه جلوش رو برای رفتن به سمت سلاح هسته‌ای بگیره
🔴
ولی رئیس‌جمهور آمریکا ترامپ جاعت این تصمیم تاریخی رو داشته و حالا امیدواریم بتوانیم از طریق مذاکره‌های جاری، این موضوع رو به نتیجه نهایی برسانیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/alonews/119509" target="_blank">📅 17:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119508">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
ترامپ: آمریکا در تماس مستقیم با مقامات ایرانی است و عجله ای برای رسیدن به توافق نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/alonews/119508" target="_blank">📅 17:02 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119507">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
ترامپ: ما انتظار داریم اقتصاد ایران تحت فشار ناشی از محاصره بنادرش فرو بپاشد.
🔴
این مناقشه بدون نیاز به عجله حل خواهد شد و ایران با انزوایی روبرو است که آن را از منابع درآمدی محروم می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/alonews/119507" target="_blank">📅 16:57 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119506">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6526976731.mp4?token=GBlklY3w7leVA0A9KwSucjjhXIYe_sLqIJaeQ8ZJ0webQOcSq2Q6ORynoEjMrc-lKJq579LqCen6PZVItXcQc26CtQOXv_of-7pPIYQZyCmNDttEUqFB7o7Bsiyjd_EDlo_MDNYtzKT9WpGHGQzufVIMvSo2Yaie21g-66QcY0ErN8j7iMuuNcGoaEBKNbgM9sS-qNTKO4qFqGastdW4j8RriK_Nl8351FquLgqtu2j2tFD5KMFOuHKmj8odaFTS-zdJDWK-yiL6kIhiBRhMpZtU8OyYzbv5wpz-r1s-r2UUxyVeVdyYUE3S9BBm6HrO63uV_RkLgrRFbCkrpzr-EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6526976731.mp4?token=GBlklY3w7leVA0A9KwSucjjhXIYe_sLqIJaeQ8ZJ0webQOcSq2Q6ORynoEjMrc-lKJq579LqCen6PZVItXcQc26CtQOXv_of-7pPIYQZyCmNDttEUqFB7o7Bsiyjd_EDlo_MDNYtzKT9WpGHGQzufVIMvSo2Yaie21g-66QcY0ErN8j7iMuuNcGoaEBKNbgM9sS-qNTKO4qFqGastdW4j8RriK_Nl8351FquLgqtu2j2tFD5KMFOuHKmj8odaFTS-zdJDWK-yiL6kIhiBRhMpZtU8OyYzbv5wpz-r1s-r2UUxyVeVdyYUE3S9BBm6HrO63uV_RkLgrRFbCkrpzr-EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگست درباره ایران: ما پیروزیم؛ در هر بخش از این درگیری که جنگیدیم، پیروز شده‌ایم.
🔴
ایران می‌داند که بر اساس تخریب فوق‌العاده توانایی‌هایشان، به همین دلیل دیدیم که آنها می‌خواستند به میز مذاکره بیایند.
🔴
چگونگی حل این موضوع بر اساس شرایط ما و شرایط رئیس‌جمهور ترامپ خواهد بود و ما تمام مهمات و توانایی‌های لازم برای تحقق این امر را داریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/alonews/119506" target="_blank">📅 16:56 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119505">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
وزیر جنگ آمریکا: ما مهمات و قابلیت‌های کافی برای تضمین دستیابی به آنچه می‌خواهیم در ایران به دست آوریم، داریم.
🔴
وزارت جنگ در آمادگی کامل است و در صورت لزوم آماده اقدام علیه ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/alonews/119505" target="_blank">📅 16:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119504">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/800e2c9b1e.mp4?token=Y0i-3fPb3p3NCApLuqJsfw-FmRBCrlht7lfEoKHaRsjKwY9c3xkPmMyKwTkvwNdC9y2O5fKQ9WAd_5I_is4Yqp5axTFe4S5-N3WUN3VtZuXjhNk7aN1PiANvPF1b2WXSFe73gU9eH64VhNc9Ia42cgSA1Mpw3-wiYZ0JsZlhHnNLrwZHjdcwl2xfzK4mTo53JVEwRbGixvO-eIqtditMxAW3btdqALN4WbJsp8xZKoki3ehUyllVwz9FNN0L1ug1UfjHlceRQ75TvTUDDLfxwvmQP54z6e8pJTcQPft-kvpIIqHCcgWHFLC-apQUQSmMzTCpeJR76Qs6Jn8p3AQmIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/800e2c9b1e.mp4?token=Y0i-3fPb3p3NCApLuqJsfw-FmRBCrlht7lfEoKHaRsjKwY9c3xkPmMyKwTkvwNdC9y2O5fKQ9WAd_5I_is4Yqp5axTFe4S5-N3WUN3VtZuXjhNk7aN1PiANvPF1b2WXSFe73gU9eH64VhNc9Ia42cgSA1Mpw3-wiYZ0JsZlhHnNLrwZHjdcwl2xfzK4mTo53JVEwRbGixvO-eIqtditMxAW3btdqALN4WbJsp8xZKoki3ehUyllVwz9FNN0L1ug1UfjHlceRQ75TvTUDDLfxwvmQP54z6e8pJTcQPft-kvpIIqHCcgWHFLC-apQUQSmMzTCpeJR76Qs6Jn8p3AQmIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری : واقعاً فکر می‌کنی می‌تونی ایران رو از غنی‌سازی اورانیوم و در نهایت ساخت سلاح هسته‌ای متوقف کنی؟
🔴
ترامپ : ۱۰۰٪. اونا قراره متوقف کنن خودشون به من گفتن،ایرانی‌ها گفتن ما قراره تحویل بدیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/alonews/119504" target="_blank">📅 16:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119503">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
مقام پنتاگون : جنگ با ایران ۲۹ میلیارد دلار هزینه داشته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/alonews/119503" target="_blank">📅 16:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119502">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه ایران: آمریکا به دنبال تسلیم کامل ایران است، نه مذاکره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/alonews/119502" target="_blank">📅 16:42 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119501">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
دبیرکل سازمان جهانی بهداشت: کشورها برای موارد بیشتر ابتلا به هانتاویروس آماده باشند
🔴
در حال حاضر، هیچ نشانه‌ای مبنی بر آغاز شیوع گسترده‌تر بیماری وجود ندارد اما مطمئناً وضعیت می‌تواند تغییر کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/alonews/119501" target="_blank">📅 16:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119500">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
پیت هگست وزیر جنگ آمریکا: به دلیل حساسیت مموریتی که رئیس‌جمهور ترامپ بر عهده دارد و همچنین برای اطمینان از عدم دستیابی ایران به بمب هسته‌ای، گام بعدی خود علیه این کشور را فاش نخواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/alonews/119500" target="_blank">📅 16:30 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119499">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
وزیر دوم بریتانیا از دولت کیر استارمر استعفا داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/alonews/119499" target="_blank">📅 16:25 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119498">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eed0b7b145.mp4?token=bOAEErILvCUAd-IikzrsrOULqjwMfDS6BhzpP6DVZi9AFZ8R6xudsUioQX2fO7Uk0sQzLkSGY4wjxRfD_QA_PCr3IyhjTsnkP-wtJx-ciffnDRQkRCMzRM8VJOwmOs5FSmSE_vMi_uYKuBZtPIPShKkPySk-TfhJ-8311HY13-yrxaRdiaS83ldCYD6i2H3zHB5aP_vbVqAAVYCONhsGbfrGvUCavpDI62Gie72R81oI9jKQmUQJD1kD0mCWyPrUewar4CmM95Et8zqTE7YQeisHeYiPcHMAtD07PCpSb20UOKy5EuRIRrpxzJDLYIYJZzVSHuGtIeNdxlP5cxV2qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eed0b7b145.mp4?token=bOAEErILvCUAd-IikzrsrOULqjwMfDS6BhzpP6DVZi9AFZ8R6xudsUioQX2fO7Uk0sQzLkSGY4wjxRfD_QA_PCr3IyhjTsnkP-wtJx-ciffnDRQkRCMzRM8VJOwmOs5FSmSE_vMi_uYKuBZtPIPShKkPySk-TfhJ-8311HY13-yrxaRdiaS83ldCYD6i2H3zHB5aP_vbVqAAVYCONhsGbfrGvUCavpDI62Gie72R81oI9jKQmUQJD1kD0mCWyPrUewar4CmM95Et8zqTE7YQeisHeYiPcHMAtD07PCpSb20UOKy5EuRIRrpxzJDLYIYJZzVSHuGtIeNdxlP5cxV2qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجار در پالایشگاه نفت در اوکلاهما، آمریکا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/alonews/119498" target="_blank">📅 16:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119497">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
هگست : اگه لازم باشه، برای تشدید درگیری با ایران یه برنامه داریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/alonews/119497" target="_blank">📅 16:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119496">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
پیت هگست، وزیر جنگ آمریکا : ما داریم یه ارتش رو دوباره می‌سازیم که مردم آمریکا بهش افتخار کنن
🔴
ارتشی که تو دل دشمن‌ها چیزی جز ترس بی‌وقفه نمی‌ندازه و به متحدها هم اعتمادبه‌نفس می‌ده
🔴
ما تو هر سناریویی برای بردن می‌جنگیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/alonews/119496" target="_blank">📅 16:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119495">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
دبیرکل ناتو مارک روته: من به آینده ناتو بسیار خوشبین هستم به خاطر رئیس‌جمهور ترامپ
🔴
می‌توان استدلال کرد که ناتو در حال حاضر بسیار قوی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/119495" target="_blank">📅 16:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119494">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1c1d6291a.mp4?token=L_vfxhWjGX2CX-ogd7VN1tl0oG4ZNByGZnbTZt2hBR2p9ezciwO56eVlsKMmihaB1M_5f--w0ZNjLk11K4R0P8O2rOW5c0nKv3wj0WhlYSznXaTLmRJiV97HRVO9hDCHsYtb7EJbxcwf2xoAXNh0etnXJ3lPguJK125S870RPD_-xawz-dYIDAGRKkMSgJyPgjG0qp8SrmcK-ceY-RQLxr69m0fiNcMJnZtzsRjcQg4Nk9EDsjxDypLtyfK_Epn9VODoRh-auGA9F_n7aXbgGmGY5rEAlk64O2SyyrQiiDRdE1S3O--m-OguW_Win4Y5aYi-ULgV2yZ8JbwgxivG0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1c1d6291a.mp4?token=L_vfxhWjGX2CX-ogd7VN1tl0oG4ZNByGZnbTZt2hBR2p9ezciwO56eVlsKMmihaB1M_5f--w0ZNjLk11K4R0P8O2rOW5c0nKv3wj0WhlYSznXaTLmRJiV97HRVO9hDCHsYtb7EJbxcwf2xoAXNh0etnXJ3lPguJK125S870RPD_-xawz-dYIDAGRKkMSgJyPgjG0qp8SrmcK-ceY-RQLxr69m0fiNcMJnZtzsRjcQg4Nk9EDsjxDypLtyfK_Epn9VODoRh-auGA9F_n7aXbgGmGY5rEAlk64O2SyyrQiiDRdE1S3O--m-OguW_Win4Y5aYi-ULgV2yZ8JbwgxivG0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دبیرکل ناتو مارک روت درباره تنگه هرمز: بحث‌هایی در جریان است.
🔴
آنچه در حال حاضر می‌بینم این است که فعالیت گسترده‌ای برای پیش‌قرار دادن—نه در خود تنگه، بلکه نزدیک به منطقه عملیاتی—توانمندی‌های حیاتی لازم برای مرحله بعدی انجام می‌شود.
🔴
ما به وضوح می‌بینیم که اروپایی‌ها صدای رئیس‌جمهور آمریکا را شنیده‌اند و پاسخ می‌دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/alonews/119494" target="_blank">📅 16:13 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119493">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده: نیروهای سنتکام ۶۵ کشتی تجاری را تغییر مسیر داده و ۴ کشتی را از کار انداخته‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/alonews/119493" target="_blank">📅 16:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119492">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
نرخ تورم تو آمریکا ۳/۸ درصد اعلام شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/alonews/119492" target="_blank">📅 16:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119491">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
ساعات کاری دستگاه‌های اجرایی از شنبه به ۷ تا ۱۳ تغییر می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/alonews/119491" target="_blank">📅 16:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119490">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
الجزیره: با محدود شدن مسیرهای کشتیرانی در خلیج فارس، شبکه‌ای از جاده‌ها و راه‌آهن که ایران را به همسایگانش متصل می‌کرد، به عنوان جایگزینی رو به رشد برای حمل و نقل کالا و صادرات ظهور کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/119490" target="_blank">📅 15:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119489">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
پزشکیان: اجازه نخواهیم داد عده‌ای از شرایط جنگ سوءاستفاده کرده و با ایجاد اختلال اقتصادی، به معیشت مردم ضربه بزنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/alonews/119489" target="_blank">📅 15:41 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119488">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUg5V8DHJYOVULIOlE-aiY3-OWr6F9pfwKlfpmcKE5OtZfJh86e98BeezF9CK4eAoybBbM2Ob1i45pcKMZv8RVNmgz3xoFs8y1rcvdFyvUK6TXaa0jo9eR19ITruIuyAntGr5qZKpLlN4M57RP0iGHtqR1CC90FMSjUPXb27ug2FAmbxgynDYjhXc1tQDpTQEX8M65VyRa7FqJlJnZmaQ5GHNkOlS5svY56RuY88goXmpbtpWVbVmUuKTjL5T1H-LDPFscFpFp7D2WWaokPnx74uT7jdSipLN3nDrb4Jfjwn6oMQ0yI2J3G-O1JOdm3TziuOH4Gtl7mp7GJcC7jE1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست ترامپ درباره ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/119488" target="_blank">📅 15:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119487">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
وزارت خارجه کویت: ما از ایران می‌خواهیم که فوراً و بدون قید و شرط اقدامات غیرقانونی و خصمانه خود را که امنیت منطقه را تهدید می‌کند، متوقف کند
🔴
اقدامات خصمانه ایران نقض آشکار حاکمیت کویت و نقض جدی قوانین بین‌المللی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/alonews/119487" target="_blank">📅 15:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119486">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
فیدان : به خاطر جهان، تنگه هرمز باید باز شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/119486" target="_blank">📅 15:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119484">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oulGVxfUzSLRtXFSMzTHEvbDz7M3LA9LrkVqIH5FKU3buAVsyXN7R6Ma_KMsH7-4LE5YjBigFVTBW2uOWWAjqm0ydNsN97cgMCTwd1QyeofEIZ70a52c_DGUyLW3NsGir02gSsnMHJuIb4zBhzfKtmuK_uKN-dTYhsXIW8BwzryjXDKJXRlvzqqD6h2I_iEvche204-8kOuR-CTvkF4cZrhz_9TNxPuoi79XOcwhbq48EecR0CYDHV0fF1HPf1YZpTY8TARe6D3bZVzQA9cnfLEq7lK7-Y5BegGLpHhA7Os7aeZGYfX9tZS652NMwRNQAd7AHVUT776EEAAbe-Ycug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EqIiroN7FKxjBtMwnvs_P4OuOZTICReXBlnV4tLPlRhCSQ2ODk4JLWtDV1Wl0D1Bd3CgwmPF40RuwisqYWaYxDvkYJHvL_y5EkhOL-htCnWfEc88riI7YuckOBWSOBfT7zBOxpMgpKFihLaZLs4pELFx7QsdWZB-_q3b1ZVf_JbzG8aLQpAp3Sv-GXLrFeefPyoxAWSN8cgD6BPynXOfkBN2FTr2IzBb-jd3Yk0N2ALEWFhRCMInvrwpHynsfZv4BfUuwUIQxN3p3zZ0wzCvYEyLyHQt5PpmDwp-VJpUC_KMWefRhFA6bFVxvGT9uiRv-jf3HAjE3f_wmJb8Xgc5Og.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ترامپ به بازنشر تصاویر تولیدشده توسط هوش مصنوعی مرتبط با ایران ادامه می‌دهد.
🔴
او قبلاً همین تصاویر را منتشر کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/119484" target="_blank">📅 15:31 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119483">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2dfApCsnDBiKydkp8BP9u2V_15_wkpE9CDGNGYbYP2cZcy0d7TtT463MH4I__hqaRqBbjmc_OnAkq4RmarfAUrTeCB0Q4AhcKk2_toxkilpEdMqSPR6gGXAj3tWeA7V0aQ2bMYXJZcAoy2vWd1E8wFKxyOg1SHuPG0NEtgHYffcN3UzoMfh1BC8hB1RUxFRlj9VIRcSn9BGj7Tx_6aOXR6lZ59On1LVAioxdqQZErtxruK6WaQDUXqEG-CfZW3m7S1wPSS-TAT4tqehY89WdCUL145RBQq2cSFvhjivfHR2xr6eYhP6_HkJpNieYE8pLz-vsD7FWuOzk-eCnD-hZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت جدید ترامپ
🔴
دموکرات های عاشق فاضلاب هستند !
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/alonews/119483" target="_blank">📅 15:29 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119482">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KpuGWp2mkqCfvBhNpWdBM74HXKUDpspjIGNyrtVQLUwY9sVZqjyD95hdy5UclWDFTmE_jfINQvTE3S6UwOlDyAlHT5kGMFVYRdOA1YBxMMsXczQxDHvhQYXYlfOV3nezvnD5fbVftkK12jMUNZaH6WH4hsbr4G5n2LATYpAfZnJQpeEBHUs_1XM4lU5iAh2Y0cBkyS1EWhLP29xuaQ2Xy7XWdXBqonowE9Us5j66T8r3heKI9ZKQnyV-1k48WShxaI1xYj_MYeNh2KIottw6cSQ1AHw1pSAmeRXo-pN9eSNKuq3wgsxoWRzYue3s00Wy6hHRHILhSkpuOrXns32UjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق Truth Social:
هیچ جمهوری‌خواهی تاکنون درباره کوبا با من صحبت نکرده است، کشوری شکست‌خورده که فقط در یک جهت حرکت می‌کند - به سمت پایین!
🔴
کوبا درخواست کمک می‌کند و ما قرار است صحبت کنیم!!!
🔴
در این میان، من به چین می‌روم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/alonews/119482" target="_blank">📅 15:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119481">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
سفیر آمریکا تو اسرائیل : ترامپ قبل از انتخابات پیشرو به اسرائیل سفر میکنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/alonews/119481" target="_blank">📅 15:19 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119480">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
ایالات متحده و اوکراین پیش‌نویس یادداشتی را تهیه کرده‌اند که یک توافق دفاعی جدید احتمالی را ترسیم می‌کند و به اوکراین اجازه می‌دهد فناوری نظامی را به آمریکا صادر کند و به‌طور مشترک با شرکت‌های آمریکایی پهپاد تولید کند، طبق گزارش CBS News.
🔴
این پیش‌نویس که بین وزارت امور خارجه آمریکا و سفیر اوکراین، اولگا استفانیشینا، مذاکره شده است، پس از افزایش علاقه آمریکا به فناوری پهپاد اوکراینی که در طول جنگ با روسیه توسعه یافته، شکل گرفته است.
🔴
این توافق با مقاومت‌هایی در داخل پنتاگون و کاخ سفید مواجه شد، به‌ویژه پس از آغاز جنگ ایران، که ترامپ قبلاً نیاز به تخصص پهپاد اوکراینی را رد کرده بود. اما یادداشت جدید نشان می‌دهد که این موانع سیاسی ممکن است اکنون در حال کاهش باشند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/alonews/119480" target="_blank">📅 15:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119479">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
سخنگوی ریاست جمهوری روسیه: پوتین اعلام کرده که آماده است با زلنسکی در مسکو یا هر جای دیگری دیدار کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/alonews/119479" target="_blank">📅 15:12 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119478">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
تحلیل نشریه هیل:ترامپ به احتمال زیاد پیروزی در جنگ علیه ایران را صرف نظر از نتیجه واقعی اعلام خواهد کرد، اما متقاعد کردن آمریکایی‌ها به شایستگی آن جنگ ممکن است از نظر سیاسی تقریباً غیرممکن باشد
🔴
جمهوری خواهان بین وفاداری به ترامپ و افزایش نارضایتی عمومی گیر افتاده‌اند و بنابراین ارائه جنگ به عنوان یک موفقیت استراتژیک «عملاً غیرممکن خواهد بود»، به خصوص اگر توافق نهایی بسیار کمتر از وعده های اولیه دولت باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/alonews/119478" target="_blank">📅 15:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119477">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b509f732b6.mp4?token=QzToBR1PwIU7COiDPEWdFSgZgq7em7OWJjseOSKo6pUm21K5nJo5mnYir7fF9iQIz1i2CE--55Jv7rwZevY7H9eCXs0BHshudB3FgZGgPyaBtG4RYmGFAY25IKU4AJRXxnx0bkOrJIUiudVcf0xhyQ3LUBQPc3pdjYGe4--g_v_XLLxkhNcAQOHryjH8jl8qUOeMxTOkROAAX7xPGAkcnEVEEHYkcXqYK3RvBFiB4K5AvKi_QLVS2kRTrVkJB7LIABKIobQ08D-cNGc6jOPeks25G1GGojGCU0AGd2R4XFj7fkWQOkSQ9LKZJEMvtM2lvpmGHiCYLk267mW8o5e9pEcKVPZP10N2udcPvNb73yXcMhJ0jYwN5WeSUdyWxJdRx8qRIt4aoeYqymds0wcX604YxOAESQdGbLsgMhhlWunrfGlsowp_KaVZjCUkhiJb7ftWKQPwen0hbw5XnMe71zWjh9WuTiWioDbEszACHb7iEJvdPp5Gk7-hz-tjQ55QKoddFfpD0ijgOipCdFJLFQz90CbiuG4j4uQ1JC_SokXI6aIHgsbCqdHFbRL6OFzGrcNezmziCyp4Oy_GfPBCainYZBGSlmV6CIb-Stzpx717rKmd-F0QhsoH_RH5iVm0xt-fsxSa_gDHKzWxd6DjYEH7y2KUMwnEFSmuRZz-EUU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b509f732b6.mp4?token=QzToBR1PwIU7COiDPEWdFSgZgq7em7OWJjseOSKo6pUm21K5nJo5mnYir7fF9iQIz1i2CE--55Jv7rwZevY7H9eCXs0BHshudB3FgZGgPyaBtG4RYmGFAY25IKU4AJRXxnx0bkOrJIUiudVcf0xhyQ3LUBQPc3pdjYGe4--g_v_XLLxkhNcAQOHryjH8jl8qUOeMxTOkROAAX7xPGAkcnEVEEHYkcXqYK3RvBFiB4K5AvKi_QLVS2kRTrVkJB7LIABKIobQ08D-cNGc6jOPeks25G1GGojGCU0AGd2R4XFj7fkWQOkSQ9LKZJEMvtM2lvpmGHiCYLk267mW8o5e9pEcKVPZP10N2udcPvNb73yXcMhJ0jYwN5WeSUdyWxJdRx8qRIt4aoeYqymds0wcX604YxOAESQdGbLsgMhhlWunrfGlsowp_KaVZjCUkhiJb7ftWKQPwen0hbw5XnMe71zWjh9WuTiWioDbEszACHb7iEJvdPp5Gk7-hz-tjQ55QKoddFfpD0ijgOipCdFJLFQz90CbiuG4j4uQ1JC_SokXI6aIHgsbCqdHFbRL6OFzGrcNezmziCyp4Oy_GfPBCainYZBGSlmV6CIb-Stzpx717rKmd-F0QhsoH_RH5iVm0xt-fsxSa_gDHKzWxd6DjYEH7y2KUMwnEFSmuRZz-EUU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر قطر درباره ایران: ایران نباید از این تنگه به عنوان سلاحی برای فشار یا باج‌گیری از کشورهای خلیج فارس استفاده کند.
🔴
این یک گذرگاه آبی بین‌المللی است که باید همیشه محافظت شود.
🔴
وضعیت کنونی تنگه و آنچه در آنجا اتفاق می‌افتد نباید هرگز تکرار شود، و باید کاملاً روشن شود که اگر در آینده هر کشوری به تنگه آسیبی برساند، باید برای انجام چنین کاری فلج شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/alonews/119477" target="_blank">📅 15:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119476">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
وزارت دفاع کویت از دستگیری چهار نفری خبر داد که تلاش کردند با یک قایق ماهیگیری اجاره‌ای وارد کویت شوند.
🔴
وزارت کشور بعداً اعلام کرد مظنونان اعتراف کردند که به دستور سپاه پاسداران انقلاب اسلامی برای نفوذ به جزیره بوبیان و انجام عملیات خرابکارانه هدایت شده‌اند.
🔴
مقامات گفتند این گروه پس از فرود در جزیره با نیروهای امنیتی کویت درگیر شدند که در نتیجه یک نفر از آنها مجروح و دو نفر دیگر فرار کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/alonews/119476" target="_blank">📅 14:57 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119475">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره در تهران: شواهد و قرائن حاکی از آن است که چین تمایلی به میانجی‌گری بین تهران و واشنگتن ندارد، و دو طرف نیز از این موضوع آگاه هستند.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/alonews/119475" target="_blank">📅 14:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119474">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره در تهران: شواهد و قرائن حاکی از آن است که چین تمایلی به میانجی‌گری بین تهران و واشنگتن ندارد، و دو طرف نیز از این موضوع آگاه هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/alonews/119474" target="_blank">📅 14:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119473">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2dcf15e48.mp4?token=diUKPp9C0nqHGmcY2FOH9dAFVq4JdfpHo3LJgASP3_C6Lkw9lTC2bkmuf7ne-sBQlaacq9hnaZ8p1RIhoTBf7uHM_bFbzsdG7D8Bmk-n4CKg73szHFdhjLxBU_GLDwPAHw2Sxi1JQ2AtJBKNGEBg-cU9vRFmEwsD5XLwaUjoCaXa3vihusNstDowl588erB6H-gXfKtGg5n-E7_67Ftn5lahO0fylftzL6s_8-DYCrIugZ9n5vOtLrtv48xgIUSbcD7gDP-f8wBBUCdXfjVmtbFfJwYOWY43qgKwfJYbQUh8-_NBjbxT7YbhtyayZjULg3giLZOcadSYZbbpzXLv0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2dcf15e48.mp4?token=diUKPp9C0nqHGmcY2FOH9dAFVq4JdfpHo3LJgASP3_C6Lkw9lTC2bkmuf7ne-sBQlaacq9hnaZ8p1RIhoTBf7uHM_bFbzsdG7D8Bmk-n4CKg73szHFdhjLxBU_GLDwPAHw2Sxi1JQ2AtJBKNGEBg-cU9vRFmEwsD5XLwaUjoCaXa3vihusNstDowl588erB6H-gXfKtGg5n-E7_67Ftn5lahO0fylftzL6s_8-DYCrIugZ9n5vOtLrtv48xgIUSbcD7gDP-f8wBBUCdXfjVmtbFfJwYOWY43qgKwfJYbQUh8-_NBjbxT7YbhtyayZjULg3giLZOcadSYZbbpzXLv0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فعالیت پدافند اسرائیل برای رهگیری پهپاد یمنی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/119473" target="_blank">📅 14:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119472">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: مطمئن هستم هر کسی که جرأت کند پا به خاک ایران بگذارد، به‌شدت آسیب خواهد دید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/119472" target="_blank">📅 14:40 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119471">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
فوری/هم اکنون ارتش اسرائیل از رهگیری یک پهپاد که از سمت ایران یا حوثی ها به سمت جنوب اسرائیل شلیک شده بود خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/alonews/119471" target="_blank">📅 14:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119470">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
وزیر امور خارجه قطر: قطر و ترکیه در حال هماهنگی تلاش‌ها و حمایت از دیپلماسی پاکستان برای دستیابی به توافق در اسرع وقت هستند.
🔴
ما مسئولیت داریم که اطمینان حاصل کنیم جنگ از سر گرفته نمی‌شود و دیپلماسی راه پیش رو است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/119470" target="_blank">📅 14:32 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119469">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
هاکان فیدان: بازگشت به جنگ جز خسارت و ویرانی چیزی به بار نمیاره.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/119469" target="_blank">📅 14:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119468">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
پنج پیش شرط ایران برای مذاکره
🔴
این 5 شرط که هم در ویراست رئیس سازمان تبلیغات امده است و هم در مصاحبه سردار جعفری بدین شرح است:
🔴
یکم : پایان جنگ در تمام جبهه مقاومت،
🔴
دوم : رفع تحریم
🔴
سوم: آزادسازی اموال
🔴
چهارم: پرداخت غرامت
🔴
پنجم : حاکمیت بر هرمز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/119468" target="_blank">📅 14:17 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119467">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjkRWelIkSgVStE--hiRezITNlivbxZ5o4i_3MXXIBGA4KfoS6dkmUUjxGXbBTJWXtRyjR9k26ZzSGhSLsLe8dqed1RgLt21U39EatQT_kWffDqyD3GVgQpOE70CxYRPuA84v59jcsb6USByOG00izsxgdv4S0Sk5HJdlYm5U-376ox-RO_F8bME3YC5DO2D5VFvfj2WH0TNxEiB6w4AqdtLq2Ggmgj_xbnTSyPtY-yGzvjw6Wtv-3vDUoGb8w7N7OL8JhCCCZCHv1a7MrOcY8Q0Xvm9rB6ZxbnrtCLZDeGzMhYqh705zDsiSKaSq7M11OZ-lGIb91aky78WN0Xtig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علیرضا دبیر عکس‌ کارولین لیویت سخنگوی کاخ سفید با بچش رو گذاشت و نوشت الهی داغشو ببینی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/119467" target="_blank">📅 14:02 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119466">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
سپاه اصفهان: امروز از ساعت ۱۵ تا ۱۸ در محدودهٔ زردنجان احتمال شنیدن صدای انفجار کنترل‌شده وجود خواهد داشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/119466" target="_blank">📅 13:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119464">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tUXQzbhrO24PvwFtnTL6DmkuM7tan6Y3cioXGuNnoWJbJE9Yd4dE5PpZwmIydc07fX82-yX9kUWhpEcu6F2itFBfP5eEFj43czRvmmUDyVf_2Ig-UkHZEeWBfXow1KqlfUXll6FIiASMaSlscFo0lFTSS8erjPv7pDxK397QTF3GRqUVInmTlwXQ-yFw12BeceM2vkWwFugsZa_q7RzLO6O_ZiF8Bq8aSNBsM3ys6-49gv4vYdljTAe1IEPoNtmMCn-LqnlvxEikQeYvUGhqbuZ07KvqAHQ_6oRR7xmwnyVOkvUMuYOWS3snXsVaoYa0PkOp6wVDBqDBD2vSbGe-eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kLtLH4xzkkAMGS39H1NfCGnTzn87c9cNJEOXLzNkK4OHe7HROyZn4-JD60_S6cPQPZ8FER0_MO3YWEEJ7wLHvJ1UU7dGR-TEqFyD93fq8qwh4eoIht3VJGhjVs9Si8UU6WBO0HbW3mwcvz6FYwFOm5mxOFvDRbTsa1vcBeA_pVWaZD7cF_X9kbwiNKjB0Idcvp2Il89jSBhcUn4HgxP_cIQFwW4FqoCosCGsHltTnZ8ZwtbvH90NcEyIn6s1899lWTFVLsPu-6D-FBKkyGVdPn9Ua79sNW8QAuxTSfybNY3Z4jSzquLA9lTeDO7k4fpBXPnDfotx1TT4Or3K1vhOiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
به فاصله کمتر از یکسال بسیجی‌های دانشگاه تهران به اونایی که میگفتن قمار باز الان میگن شهید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/119464" target="_blank">📅 13:40 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119463">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
احتمال شنیده‌شدن صدای انفجار در تبریز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/119463" target="_blank">📅 13:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119462">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ej27_QNFbEcNEPUFdiDwklWH3RTuLNSLyFPvrbnuyaNyrcH7---mih5PJZVAiQ0dXGHpsxippnil-IdVF5m8O0yqddAwo3PIpXS0SeeB7tgwU_LVG3fwQL7O-3f0s_FdPVtuLEq7Kt93jAPhW9QEXrcPU51LbU9aLXf1-lJKAA3H2tvExwkcDF3VZJ7WWWG8DzFN17d2Nz4ERdupgga7FhN-zr3L6r2kAGU0qosy7ts13SDrsO66m86BBWPEW5sGdnpjauZP6IwJ_lwfZrACZjma1NSnHBN9GdXc5g-152-mLad69hNBsP_yOyMknKxA9xQI-zWfeRa4JG6w5xRKQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
علی خضریان نماینده مجلس خیلی شیک و مجلسی گرای یه پتروشیمی بسیار مهم کشور رو داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/119462" target="_blank">📅 13:31 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119461">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
دیوان امیری قطر: امیر قطر با وزیر خارجه ترکیه در مورد اوضاع منطقه و آتش‌بس بین تهران و واشنگتن گفتگو کرد.
🔴
دو طرف در مورد تلاش‌ها برای کاهش تنش‌ها و تثبیت اصل راه‌حل دیپلماتیک گفتگو کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/alonews/119461" target="_blank">📅 13:25 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119460">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGcqsntREKVIrEbDJqL387RdJGcSjuoPRFQ8Ytx2bO2Hff4D64qiM1LzCsJNcgwKNhtu6Y4MXOIGOBjYAlk8gYVn4qzVBCbKpi1h9Ro5_lkiRCkCn5oY0CMe4Ekr7BeQpQ_HGXfBl_rGuLt6hNknGqmK2BbcR8MrX0jlAsEViloMTycJETdqN5QXRofgrORFXtdU7SRnHhNVF_K-mbbGc2ekgEZhFNH-wUnhbRmjayiDofQyvf2iO32amESLSrStp2W9etMYZylehIit2_hFsw7wy_j4mf9A7sxo6kNj4tcHRSIPRxzZrFdqIdC7tvBnzMh1vof8sMujdk1pFjJwEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
هر گیگ فقط 150 تا 100هزار تومان
🔥
🔥
💥
🔝
تخفیف ویژه به مناسبت 100کا شدن مون از دست ندین
💰
🔍
دنبال یه خرید مطمئن و ارزونی؟
🔄
💯
فقط با 150 تومن، مستقیم و بدون واسطه خرید کن.
این فرصت ازت دست ندی دیگه نیاز به هزینه اضافی برای فیلتر نداری واسطه پاک‌کن مستقیم خرید کن
✅
📣
💎
ما ۲۴ ساعته پشتت هستیم و اگه راضی نبودی، وجهت رو برمی‌گردونیم.
بزن رو لینک و امتحان کن:
🎮
🛡
@premiumzone6bot
🎮
🛡
@premiumzone6bot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/119460" target="_blank">📅 13:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119459">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzcwjxNY02wjI12w1kLuQIo5WdATW2AJcwe7BcRceSQkkYf77L7qbOlvz7yfpvgH_1AruI60vVu2-2iPG8gIz1kw52eHLBBLeGe_55X-mcWYAcCojIv4BBQXiP11_BtCfgGw62XByEDm2UK8o2PGHhH0t2mHc5NX5Lwu73LM4VStmUIJ58hph-jJZ2N8D6W8vgzbg8jR6QSTX9JWwCbGxZJTd2k24C5dmGnRASk8kmlb349op2-7HPatl_BwkhsqDxZizp9TE-Re1yCiUCIXmekQm8QDwY4LqopC2qFgbfID484qrSP1wD_wPfb_Ex_9CR3sNSvjvB58PuuPoGgyyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۱۰۷.۱۲ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/119459" target="_blank">📅 13:19 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119458">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
بحرین : برای ۳ نفر که متهم به جاسوسی و ارتباط با سپاه پاسداران ایران بودن، حکم حبس ابد صادر کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/119458" target="_blank">📅 13:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119457">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
تداوم اختلال GPS در تنگه هرمز
🔴
داده‌های شرکت ردیابی دریایی WINDWARD وارد نشان می‌دهد که اختلال GPS در تنگه هرمز همچنان تداوم دارد.
🔴
حدود یک هفته است که اختلال سیستم‌های ناوبری دریایی و GPS به دلیل تحرکات تجاوزکارانه آمریکا در تنگه هرمز افزایش پیدا کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/119457" target="_blank">📅 13:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119456">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
سفیر آمریکا در تل‌آویو می‌گوید اسرائیل سامانه‌های گنبد آهنین را به امارات متحده عربی ارسال کرده است
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/119456" target="_blank">📅 12:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119455">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
ابراهیم رضایی، سخنگوی کمیسیون امنیت ملی مجلس : اگه دوباره به ایران حمله بشه، یکی از گزینه‌های روی میز می‌تونه غنی‌سازی ۹۰ درصدی اورانیوم باشه و این موضوع تو مجلس بررسی میشه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/119455" target="_blank">📅 12:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119454">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLG_KwmTXUejifju72LB-Kh2NQ142qDYcV7Yh120F5b0N-XaVaaTpydLoPygiOrcDJgJXODM9ibw9RtA22wk5Mm99xAxPJ6L7axx83K4JT0NCIBaTwxflEEr0nifMEaeJ8ArJVLzSm8-UYH0YYaxdiAZCaaph66oaSmRisEMYIonM7IgXSMsmTx93TKicH7teulc9jkPTpcgW3l3uJidcBDb6nR-iIfV1ABPGSRuAPLFyzv3xQIbDYt9HalYbiyRsw-iq47RiRrzJDiys5avDIAH1xngafqVdyc00iHIZqeOp69kc9XTGfm4SRRpb6W-nsWv8mcENGXxOyCdMqnyxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز: به دلیل کمبود نفت، ژاپن چاپ بسته‌بندی مواد غذایی را به صورت سیاه‌وسفید آغاز کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/119454" target="_blank">📅 12:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119453">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
داده‌های ناوبری کپلر: ۸ کشتی روز دوشنبه از تنگه هرمز عبور کردند؛ ۵ کشتی از تنگه خارج و ۳ کشتی وارد شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/119453" target="_blank">📅 12:40 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119452">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
صدر اعظم آلمان: توسعه اقتصادی ما برای سال‌ها راکد مانده است — حداقل هفت سال — در حالی که کشورهای دیگر اطراف ما رشد می‌کنند، برخی به طور قابل توجهی.
🔴
پیش‌بینی می‌شود رشد بالقوه کمتر از نیم درصد برای سال‌های آینده باشد.
🔴
برای کشور ما، برای رفاه ما، برای اقتصاد ما — این به سادگی خیلی کم است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/119452" target="_blank">📅 12:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119451">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
سفیر آمریکا در تل‌آویو می‌گوید اسرائیل سامانه‌های گنبد آهنین را به امارات متحده عربی ارسال کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/119451" target="_blank">📅 12:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119450">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KqD-geYRu-NZOWNF6h-2r2gQCSh4fivGpnjRqfZb37d8Ni5d3646NNfQT8hwU8COLLLP3tmYiPbZS842d303_qopZ4nmuSCdhJ88yZfZeAmncC1hAPmKftaq_VKIXH5bMYlV6cDtZNMuh-0hu86wcS0jZSZKVw518mIKGeOHXX6RDpHkzZl7UK9HJosGS8UMgFMlBP9yYq5iq9RyRHp8HaYLf116wOBhudM5CivIFH5J8x-IDmwygH1JSlJLV9rJzOwuQ7wTRRWKmvnZWo7nDlmPibSzWtxZsszPUhiFJuNhZbLZlT43e4zbviz6jsQISQ2urpXcqPPFjj87rJ2ifg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چرا ‏گوشی ۱۱۰۰ دلاری در ایران ۳۰۰۰ دلار فروخته می‌شود؟!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/119450" target="_blank">📅 12:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119449">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
وزیر کشور پاکستان: انفجار یک بمب در ایالت خیبرپختونخوا واقع در شمال غرب پاکستان دست کم ۷ کشته و ۱۸ زخمی برجای گذاشت.‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/119449" target="_blank">📅 12:12 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119448">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVarzesh+plus | ورزش پلاس(K_B9)</strong></div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/119448" target="_blank">📅 12:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119447">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
وال‌استریت ژورنال: آمریکا و ایران در یک بن‌بست دیپلماتیک بر سر موضوعاتی قرار گرفته‌اند که سال‌هاست دو طرف را دچار مشکل کرده است، و این درگیری اکنون در وضعیتی نامشخص و خاکستری قرار دارد؛ حالتی که نه جنگ است و نه صلح
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/119447" target="_blank">📅 12:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119446">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
سی‌ان‌ان: بسته‌های چیپس کالبی ژاپن با تشدید جنگ علیه ایران، تک رنگ می‌شوند
🔴
شرکت تولیدکننده تنقلات ژاپنی Calbee به دلیل مشکلات زنجیره تأمین ناشی از جنگ خاورمیانه، بسته‌بندی خود را به سیاه و سفید تغییر می‌دهد.
🔴
این شرکت در بیانیه‌ای اعلام کرد که این اقدام در واکنش به «بی‌ثباتی عرضه که بر برخی مواد اولیه در بحبوحه تنش‌های جاری در خاورمیانه تأثیر می‌گذارد» صورت می‌گیرد.
🔴
نفتا یک محصول جانبی نفتی است که گاهی اوقات در بخش‌هایی از فرآیند تولید جوهر استفاده می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/119446" target="_blank">📅 11:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119445">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
فاطمه مهاجرانی: وزارت علوم مکرر و روزانه پیگیر دانشجویان دستگیر شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/119445" target="_blank">📅 11:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119444">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
مشاور نخست‌وزیر عراق: گزارش روزنامه «وال‌استریت ژورنال» درباره ایجاد یک پایگاه نظامی مخفی اسرائیل در صحرای نجف صحت ندارد.
🔴
آنچه در صحرای نجف رخ داده، نه ایجاد پایگاه نظامی بلکه یک «تلاش برای عملیات هلی‌برن» بوده که توسط نیروهای عراقی ناکام مانده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/119444" target="_blank">📅 11:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119443">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
بی‌بی‌سی: ایالات متحده مذاکرات منظم و محرمانه‌ای با دانمارک برای افتتاح سه پایگاه نظامی جدید در جنوب گرینلند برگزار کرده است.
🔴
این پایگاه‌های جدید به عنوان قلمرو حاکمیتی آمریکا تعیین خواهند شد.
🔴
تمرکز این پایگاه‌ها بر نظارت بر فعالیت‌های دریایی روسیه و چین در گذرگاه GIUK خواهد بود.
🔴
ایالات متحده در حال حاضر تنها یک پایگاه در گرینلند دارد — پایگاه فضایی پیتوفیک — که این تعداد در دوران جنگ سرد حدود ۱۷ پایگاه بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/119443" target="_blank">📅 11:41 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119442">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
سفیر آمریکا تو اسرائیل : ما نمی دونیم که اوضاع در مورد ایران به کجا میرسه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/119442" target="_blank">📅 11:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119441">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
گزارش شبکه i24 اسرائیل نخستین بار از شروع جنگ نیروهای واحد گولانی ارتش اسرائیل درگیری در آن سوی رودخانه لیطانی با نیروهای حزب الله داشته اند که منجر به زخمی شدن ۸ نیروی تیپ گولانی شده است و به ادعای آنها پس از کشته شدن چندین نیروی حزب الله، مابقی دسته اقدام به عقب نشینی از منطقه مورد نظر(روستای زوطر الشرقیه) کرده اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/119441" target="_blank">📅 11:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119440">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
العربیه به نقل از سفیر آمریکا در اسرائیل:
نمیدانیم اوضاع با ایران به کجا خواهد کشید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/alonews/119440" target="_blank">📅 11:25 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119439">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
وزارت خارجه پاکستان: اگرچه مذاکرات رسمی هنوز از سر گرفته نشده است، اما تماس‌های دیپلماتیک در سطح بالا ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/119439" target="_blank">📅 11:13 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119438">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
کره جنوبی هم به مذاکرات چندملیتی بازگشایی تنگه هرمز پیوست
🔴
سئول قرار است امروز سه شنبه به یک نشست چندملیتی سطح بالای وزرای دفاع برای بحث در مورد امنیت تنگه هرمز بپیوندد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/119438" target="_blank">📅 11:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119437">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02d23b20d8.mp4?token=a9DaMaObRTVamUSown_XzJSv8piyyp88PgOz99v1dk4rHnDxX4LGRm7bFZ9dzigXqtq7siMUjuvgrxAWJu-_-wqVnRQPysNMImEJROT2hxbLb9p20FZQUpzrJR8tawKOrEsZHeF2YaBtB6q1cF3nyIukIahSLeFFOr6YeO-UzXlqAoagkBGuAOHmIG0zUt8P1Ozd5uJEj9ml60toOKMAQB3so7Wt0Sj_qXWeu9U58IofsWdq9L5kF30wY_2mh1e_i2XHk_98ZKTeq13YFyFWbLo9GgOcsHa4yDISsUR0ackyhUEDWEqtZ8G8qgy-1THvrl4XUYtqVTzX5qsuCyEMFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02d23b20d8.mp4?token=a9DaMaObRTVamUSown_XzJSv8piyyp88PgOz99v1dk4rHnDxX4LGRm7bFZ9dzigXqtq7siMUjuvgrxAWJu-_-wqVnRQPysNMImEJROT2hxbLb9p20FZQUpzrJR8tawKOrEsZHeF2YaBtB6q1cF3nyIukIahSLeFFOr6YeO-UzXlqAoagkBGuAOHmIG0zUt8P1Ozd5uJEj9ml60toOKMAQB3so7Wt0Sj_qXWeu9U58IofsWdq9L5kF30wY_2mh1e_i2XHk_98ZKTeq13YFyFWbLo9GgOcsHa4yDISsUR0ackyhUEDWEqtZ8G8qgy-1THvrl4XUYtqVTzX5qsuCyEMFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ پس از شنیدن صدای یک پرنده در نشست خبری کاخ سفید: اوه! فکر کردم یه پهپاده؛ این روزها پهپادها رو در اندازه‌های مختلف درست می‌کنن و می‌تونن خیلی مخرب باشن، همون‌طور که احتمالا شنیدید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/119437" target="_blank">📅 11:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119436">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
معاون نیروی دریایی سپاه: تحرکات را با دقت زیرنظر داریم در یکی از موارد اخیر، یک ناوچه آمریکایی قصد عبور از محدودهٔ تنگهٔ هرمز را داشت که با رصد دقیق نیروهای مسلح مواجه شد و پس از مشاهدهٔ برخی رفتارهای تحریک‌آمیز، نیروی دریایی ارتش با شلیک‌های هشداردهنده و هدفمند، پیام لازم را منتقل کرد و این شناور نیز بلافاصله مسیر خود را تغییر داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/119436" target="_blank">📅 11:05 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119435">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tO9Eppm7h2mUB0ZCks3b-qD6YV_Lo33EMDNA4gXqE-zx6AwHd2xJbfcvBpPEefIqo_CByWQSpwekdXcyHbHdPC1xqJ2nJsCVJkCIzbI2nJUXcQ87Ok7L3isG9Ws2xcE824koFZIRhQno-N4c5mgO0JSZAXrikkH1zqSNyfIP1zbWydlW_tB1MhVpjYrhFRE2W9ZLpBcgqTzyuQIMX3qEYN89RCxbEN20FYOGfy_cjAtrcEZCD9ACRS16DFS0Teciu7bbCKmuMoRzaIgIafRs2BUSSVjN9DAIquQRIcdyJaJXDGFniRKquzHhLApMCt1VAyxkSMW9tUMAPb5RZUHj8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هاکان فیدان وزیر خارجه ترکیه با خلیل الحیه رهبر گروه حماس دیدار کرد
🔴
الحیه تحت تعقیب اسرائیل قرار دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/119435" target="_blank">📅 11:02 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119434">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
سخنگوی دولت: اینترنت پرو مصوبه‌ شورای‌ عالی امنیت ملی را دارد و اين شرايط موقت است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/119434" target="_blank">📅 10:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119433">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3823c68f75.mp4?token=bFl6ZJCZhW7bwKJIEEuPgiJNxPH9i9L6RmDDm53qxQS9mvNfSLm7s1kxsGSdibSCLFZ0WgPPtH62LjDVV9xhOxYYz0BkOrv_2JsUUSF4thv_cA6wh7mPfMq6bivfFopzZJh-6Ihmzo6983sp8KUu-RRB8TYgvjTOl2hm1BMTA6n2qInAxnlm1IKddDlpOW3G8StrQ_OtPyC8QIaVRNt6suoEp2Wp-PrL8WlJ0GG9xkw3kzBIXSnOjqDvYmoZRWwsIFc2Jd40fsu_I8ivWLelyKYO0CUxyHd9d5-pdltRYArxiuol2hzmuefYXV9TbaZA2mo4hhZPd-EHXh1aw04gv4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3823c68f75.mp4?token=bFl6ZJCZhW7bwKJIEEuPgiJNxPH9i9L6RmDDm53qxQS9mvNfSLm7s1kxsGSdibSCLFZ0WgPPtH62LjDVV9xhOxYYz0BkOrv_2JsUUSF4thv_cA6wh7mPfMq6bivfFopzZJh-6Ihmzo6983sp8KUu-RRB8TYgvjTOl2hm1BMTA6n2qInAxnlm1IKddDlpOW3G8StrQ_OtPyC8QIaVRNt6suoEp2Wp-PrL8WlJ0GG9xkw3kzBIXSnOjqDvYmoZRWwsIFc2Jd40fsu_I8ivWLelyKYO0CUxyHd9d5-pdltRYArxiuol2hzmuefYXV9TbaZA2mo4hhZPd-EHXh1aw04gv4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : همه ۱۱۱ موشک ایرانی که به سمت یک ناو آمریکایی شلیک شده بودن، رهگیری و ساقط شدن
🔴
خدمه فقط حدود ۱۳ ثانیه وقت داشتن برای تصمیم‌گیری در هر درگیری
🔴
اگه یه محاسبه اشتباه بکنی، هم کلی نیرو از دست میدی، هم یه عالمه کشتی چند میلیارد دلاری
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/119433" target="_blank">📅 10:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119432">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7QETnACDp3vQOCMuLIMetrUvKu4ZYKORRBmNKMKMrsA_Ct0T9C-4qSXskohSpXTJ7uRkpT3imopfSqLWCb7ey-fvjGVfQv3nLoajU2SOhY1RodFxKq7VSNGfYpEiTWNbOzbN7CMt6EQFZiAm0bpq0fVYKq3eVV_pznRF4GkJ4VIShfs4qNtqQ3cJcJ5DsdoW6fba1EjF0nTZhFei9mzCGWAoRC8fQX_dnNamwDgf4p4MoYjVRTIXObWdj6iPbGrsSaL1drOYp7Sn4Ra3tC-rZ6fUdYO-1LUVqtwaMV3h_zHMuKbEwW2CReWQNICx2yLlm1akAwFelFzFHwlPdkZcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۱۰۶.۳۸ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/119432" target="_blank">📅 10:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119431">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
قراردادهای آتی نفت خام برنت بیش از ۲٪ افزایش یافت و به ۱۰۶.۳۸ دلار در هر بشکه رسید، طبق گزارش رویترز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/119431" target="_blank">📅 10:40 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119430">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
شیخ حمد بن جاسم بن جابر آل ثانی، نخست‌وزیر سابق قطر: عملیات نظامی به طور کلی به نفع منطقه نبود. آمریکا به دوستان خود در منطقه آسیب زد.
🔴
عملیات نظامی به طور شخصی به نفع نتانیاهو و برنانه‌های او بود
🔴
او به صراحت درباره نقشه جدید منطقه، اتحادهای جدید و اسرائیل بزرگ صحبت می‌کند.
🔴
آنها از ساختار قدرت در ایران بی‌اطلاعند. این هرم طی ۴۷ سال ساخته شده است،  اینطور که آنها فکر می‌کنند فرو نخواهد ریخت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/119430" target="_blank">📅 10:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119429">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46b814539f.mp4?token=C0e63bPzWbVZ8oRa6juC2wfQ9vkqqwIiPcZKa7dZ0mV5cVwbHBKHWuUslBWLNhleqctB423OC3Q0rWMVbN032sL2RLg2GFIDBwYBtO2dYCE02wgK4tWr1n0n7wVF1g3YcoKnaWE9T9il7L4EOjk0YYefnElxVrP6s_qICct3j1h0VsIRXuG4LNU_Fd1gg3GlR1Q9eNvwazFnpnHcP101akLhAakP3OpAT9Mshzmq09HyPSkXjdbTSz_D6-PZNPW7cqFRslgAIMBNiTT62khxczhnmXMCfq-2d8-TVNlVxZsxTAYEgPSSk6mBM4Io75MfvzP2j-FiQgc_FhL7E3Gnkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46b814539f.mp4?token=C0e63bPzWbVZ8oRa6juC2wfQ9vkqqwIiPcZKa7dZ0mV5cVwbHBKHWuUslBWLNhleqctB423OC3Q0rWMVbN032sL2RLg2GFIDBwYBtO2dYCE02wgK4tWr1n0n7wVF1g3YcoKnaWE9T9il7L4EOjk0YYefnElxVrP6s_qICct3j1h0VsIRXuG4LNU_Fd1gg3GlR1Q9eNvwazFnpnHcP101akLhAakP3OpAT9Mshzmq09HyPSkXjdbTSz_D6-PZNPW7cqFRslgAIMBNiTT62khxczhnmXMCfq-2d8-TVNlVxZsxTAYEgPSSk6mBM4Io75MfvzP2j-FiQgc_FhL7E3Gnkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ از رئیس جمهور بعدی آمریکا گفت: ترکیب ونس-روبیو رویایی است!
🔴
«چه کسی جی‌دی ونس را دوست دارد؟ چه کسی مارکو روبیو را؟ بسیار خب. به نظر ترکیب خوبی می‌آید. ضمناً، من معتقدم که این یک تیم رویایی است. فکر می‌کنم به نظر می‌رسد کاندیدای ریاست جمهوری و کاندیدای معاونت ریاست جمهوری باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/119429" target="_blank">📅 10:30 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119428">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NhaMAK-DMGJjsaNnjyjsNHmpPIoERqwFQ-LIykRaAJNdmjbi-KOCD0CaY5q4d-zSHRyBV1lvHxtLfzQ0eZzwHsVetEMhcWFb9VSvaScpKrqkVOoIy81VASvijP_6zF-MrqWFOM1w_ly6rxUHnxXJGIjxJEELVewXxl7KqnMBLjZGPGrIdNWvKf1BIofX6Yj7U6Ux6OEw0fMVqZLo1KW0kZBZqomQxorX-bHvip-eHVRTZJW1F03oy7BBPD6PKh-gLxxwO6aouGc5x7cRrIBEB0KtooJdUuMLPMA6u9E_5WFyvQO9YmOtJO1obMSnyJzMNOw66DHgIALihQqETJvhgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: از نظر من باید با خانم‌های بی حجاب برخورد فرهنگی و انتظامی بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/119428" target="_blank">📅 10:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119427">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSpfXsbx-G5b26k2baSEbscjWFk-xC5EJzlxA8JDM3j6dy3C-ETaQ0zGPB2oyhe5pVOdJruprzxYSmy-GD6c9uoaqVcu7m1SxsNf64mjpSStUjtJVtL3a_S-p6-1_jqP8oPCvEnhw52IikCfx46IqlzTVuikgH55sT4GoUFpfWFA8JKmXQAsHikMcp2EGh-XnC5EbI8vPImLWgzqDXHsgn1PQPt3zH0B0ZAr1UATgDisTa5KG2FD60Bl2-xIwh9DHpu4gNvKp9EiXU4K8ntQhUYOZUvYuWWdEO6nWYNLA9TcRbECS44oJrPp8Hi-t092aOgOb3u2a3byU28gxrz98A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی ارتش اسرائیل، آویخای آدراعی، هشدار فوری به ساکنان ارزون، طیر دبّه، البازوریه و الحوش در لبنان صادر کرده است تا فوراً خانه‌های خود را تخلیه کرده و حداقل ۱۰۰۰ متر به سمت مناطق باز حرکت کنند، با اشاره به نقض آتش‌بس توسط حزب‌الله و هشدار اینکه هر کسی که در نزدیکی اعضا، تأسیسات یا تجهیزات حزب‌الله باشد در معرض خطر است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/alonews/119427" target="_blank">📅 10:17 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119426">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/759573b975.mp4?token=GfwmMufn-aau0R7JarmKVXZOG4OXARKhX0mRiizwroTApIVfKgGwCBF2orgmnyXByB_JQIeW-Qf6uNgtOGiMdOm9W90-xcqx793ZgF4WWS8WogKmceN3lpdlr1bVU-gZ-BOTX-1A-aG1bhlHpeMb8mGAP0KV_NuhuHoM4ToBrZKKCKIAN37YuGILk-uzNvQkQ6X5D1vnmVaRrF-XcipKFEQCNyLNi6HF7lLGufyFh5mwF-yZKi5lNvYm94hN0IEAbyq1dU9lyDVuJlKMZA311mPH2D5idSG_ux85Zqmrxc8eriyi-ZCx01fqFXydvPMCp6mKMTa_RYv5NplRLM1hrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/759573b975.mp4?token=GfwmMufn-aau0R7JarmKVXZOG4OXARKhX0mRiizwroTApIVfKgGwCBF2orgmnyXByB_JQIeW-Qf6uNgtOGiMdOm9W90-xcqx793ZgF4WWS8WogKmceN3lpdlr1bVU-gZ-BOTX-1A-aG1bhlHpeMb8mGAP0KV_NuhuHoM4ToBrZKKCKIAN37YuGILk-uzNvQkQ6X5D1vnmVaRrF-XcipKFEQCNyLNi6HF7lLGufyFh5mwF-yZKi5lNvYm94hN0IEAbyq1dU9lyDVuJlKMZA311mPH2D5idSG_ux85Zqmrxc8eriyi-ZCx01fqFXydvPMCp6mKMTa_RYv5NplRLM1hrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عوستاد خوش چشم سری قبل گفت جنگ نمیشه اما شد، اینسری گفته جنگ میشه ظرف ۱هفته و باید ببینیم دوباره گلشعر گفته یا نه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/alonews/119426" target="_blank">📅 10:13 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119425">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cad4ea0df5.mp4?token=i9YwiqMyzSq5AgK4ZeoKgC2rgRERYKAxhDiB_uI9MdjTsi4eLbwIVPJUtETbBFmasnKcf5CL28xF6ufqcuegNqRbVUoqytLqSd5MxHcfWe0VIIK--VpDCmGuaaPDmp5fRYpvWwErj9e0FVPDeEch9q7oQsnjw6YA4wzuVml8FdMkUExEuav4QkjbsNgvVjB-_OzoEI_pNo4Uc0Uzj5NDHwV7Z25XG-3R-n6oUh9vU7aZhAimEPFl7-5EDWWfCakP37T-uM438vjbxa3BNzNlyfcFIP5W1P_uQNcXCdGlBwbj4hXj27SjdWWb1-7D9NI2t7IT2D9IdtzQmxbQXHSVkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cad4ea0df5.mp4?token=i9YwiqMyzSq5AgK4ZeoKgC2rgRERYKAxhDiB_uI9MdjTsi4eLbwIVPJUtETbBFmasnKcf5CL28xF6ufqcuegNqRbVUoqytLqSd5MxHcfWe0VIIK--VpDCmGuaaPDmp5fRYpvWwErj9e0FVPDeEch9q7oQsnjw6YA4wzuVml8FdMkUExEuav4QkjbsNgvVjB-_OzoEI_pNo4Uc0Uzj5NDHwV7Z25XG-3R-n6oUh9vU7aZhAimEPFl7-5EDWWfCakP37T-uM438vjbxa3BNzNlyfcFIP5W1P_uQNcXCdGlBwbj4hXj27SjdWWb1-7D9NI2t7IT2D9IdtzQmxbQXHSVkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجار پالایشگاه سالیناکروز در مکزیک
🔴
براثر انفجار پالایشگاه سالیناکروز در مکزیک، ۶ نفر زخمی و بخشی از این پالایشگاه تخریب شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/119425" target="_blank">📅 10:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119424">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
ارتش اسرائیل تصمیم گرفته است کارخانه‌ای برای تولید پهپادهای انفجاری به عنوان بخشی از پاسخ خود به توانمندی‌های پهپادی حزب‌الله تأسیس کند، طبق گزارش یدیعوت آحارونوت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/119424" target="_blank">📅 10:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119423">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
سفیر پاکستان در مسکو: مذاکرات ادامه دارد و ما معتقدیم که دیر یا زود به نتیجه خواهیم رسید
🔴
بن‌بست زمانی است که شما کاملاً از گفتگو با یکدیگر دست بکشید
🔴
خدا را شکر، آنها هنوز از طریق پاکستان در حال گفتگو هستند و مذاکرات ادامه دارد. این چیزی است که به من امید زیادی می‌دهد
🔴
مهم‌ترین مسئله در حال حاضر باز شدن تنگه هرمز است که در ابتدا حتی روی میز هم نبود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/alonews/119423" target="_blank">📅 09:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119422">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cdzzrx878DC3ZZqPaSWCLqfe41XEI2nEG51hFBcXkV5qdp-qfmNWKMMn8YVscW2pD14RCpd1ShY6arEbNI4pypBvKGemDzGYH8fTErg7YWKlgcSvjxafh1i0HDjxHYZahvh_nH39En7sm1ir5psGE76FEFXzBFdKKT-dlKmmCV58tYdoYgHP4LTyf0uPKtyh4Dp3MyW2mlAeGhFUrsu6_VZlUceOuvAtZ5-u_KRJliSXInKT3E40M4KpYOcaAX5fmvqlundvPdyBSta78LEWbD8SKsvW1_zgvf1ZNqEWfIDR489ZCd4WCpMDf6RT5xBErlM-8GXKEetYos4yJivvCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ پستی را بازنشر داده که خواستار بازداشت اوباما شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/119422" target="_blank">📅 09:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119421">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
انفجار برنامه ريزی شده در 3 شهرستان آذربایجان شرقی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/119421" target="_blank">📅 09:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119420">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
روزنامه تایمز: وزیر کشور انگلیس، به همراه شماری دیگر از وزرای دولت از استارمر، نخست‌وزیر این کشور خواسته‌اند که به تعیین زمانی برای کناره‌ گیری از مقام خود فکر کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/119420" target="_blank">📅 09:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119419">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
وزارت علوم: به دنبال حضوری شدن کلاس‌های درس و امتحانات هستیم
🔴
دفاع دانشجویان حضوری شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/119419" target="_blank">📅 09:22 · 22 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
