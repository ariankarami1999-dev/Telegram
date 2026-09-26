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
<img src="https://cdn4.telesco.pe/file/D1YSc4QyUKLklhC20sbDWv_i2pa16qmPt4GYYyagysRe0IoQ8KtpKeTMelgNiGB-9kZi1Z5ZH1a5f6wy0D6oVLaOi8kUrcZxBeKPeN8ow4YKzi5ZQAQR5rqzJyLuhwH0zPqyIPI3bVqKKNjanr8G8so55RIUCQjZWfCEFQ247M644ixQn3692bSmlemN4J5a4c6XwDJSRW_luFHLPG4grZKUZUNWYMpG6oM7SPBaapAdLGfJ6pSSgiEviXYErblEoJnT99rSwTsPY7GEe64IBNJzyZokj1vR3W3g7ew9ri5eU3Fg5ppDDfNNwsjaQ3bANHPl7zcyS5orM5qQ1eJW2A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 446K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 20:48:23</div>
<hr>

<div class="tg-post" id="msg-30499">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITWkgojcOqkkhdUZ7XciR6xfm_V9VZYWOnWD0vmNmAa1ZQ5swuC7IkJPUbrithkXE2Z9krPhuQKU5oB9ZosgRCQ9lDoAMI3ZUm-oS3X9suLcYLKWQmCr73TQloyKtxnxm54V040rtAsCEz8p_oI9azp9bpG1LwaY6Fpe4AtckQuDUxGYrarPQWA1XqKVy2R1rJE8wljogZRqFhXxsIWVF-WlX_9nowc6D2XZHbwVb7eaRNebL4XjuNcs86QVvZHR70ErNhgs1OwEp_vjRQly--cAlfiNwInjWCy0yzjD-0OuiHLh4Ngp_OTz6LW_XJC9en5Fd2d78pemjj_kQZKsgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صحبت‌های تند و جنجالی اللهیارصیادمنش فوق ستاره ایرانی لخ پوزنان: میدونستم قلعه نویی هیچ اعتقادی به سبک بازی من نداره. تا روزی او سرمربی تیم ملیه هیچوقت برای این تیم بازی نمیکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/persiana_Soccer/30499" target="_blank">📅 20:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30498">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d92fMGvm-C6iJ8RHYkQR4TsbEJENv7x2EH6TNMjAcQIV60I3Xa_r1UiigKsATjrSV7eiOVIaEgDOLuzFKHQz-y7w79PuiRhNuO6s6LHZPtlx61ms8MNvHmNKsHsnqyjkdF568n2MmcmBLz0-O_lmEq4t-PKRo4S96d-KeUtBn-zysKk-jFH8THIf2R33cc5SAk1oHTtOuAPylZvsJivgM6726K-I4eBkdlg8kmEIZLhfqqGjI3oUnxoDYuPV4iECHaOfH9n3cMvn0_sUj-3UiGn4vxs3e2Pu3cabNMq0rWBkgigGp7VLC1xYZ8vez80gC_890MT_z_YbKMwAgVKPfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
81 سال‌پیش درچنین‌روزی؛ باشگاه استقلال تهران تاسیس شد. آبی‌ها باداشتن دوقهرمانی درآسیا پر افتخارترین باشگاه ایرانی در قاره کهن است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/30498" target="_blank">📅 20:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30497">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1d9a03df6.mp4?token=d-OpZZX8pUpFnClSP0KHrvoNAFWdi54_xAxVdM3tbKRlMO893fQXf7NO4xvutiBzI7lL1MjdikrXf4Cqf1Mcydcs9E8lpNMZNvbick4eQy_sJqFbD7Z1_UK-zmH29EKuCMHYf1-_sGypDdTqvMDRoQa4MXiOna8uvrocY7Aah4r6loPtYr5zOL7bktJ0WjgpiPkEh-s-vSBuBvhvRbmiHioUXAbSfaNMaAzwlHNKs0mS3yEipi1j5GPBjc5uCoTBmXaToSQztjeYSfLYv9D8Bj8S_sjiTsRBhrHRFRZKcWHK8gx2XU0OjBnMp_sm3XrWZK8niQqoD2XDsC_p8XyGQ0vyLZt4-HG1QOnbIvEq-ZUP_FpAb7FoRPuBLpirS1rx3P50iG2FjS8w6YOcDJdv6t6IXm8FzgMvajB_771Pw7oU6fDCR7n_BMWaS0AOx0dUYA9_xz3j4tBbWri-RZHBvH0o9L84av0JACuSniWuiURLIwfCNbvrRzgjvmbEdZ2KdckApeEaBa9tPBuyQOJ7jdbqI3kAJTkKmZXfm8DBGz19oVCUAzvKkxwZF4SvlJQaf2FvYVCiDAnKtue_BNYSSjBBL948tOA1e_Eq56Z8T6t71GuaykaWOPQQvtd9m7E8Fh75hKY3jY4nzD0tebyNgFU-CH8f43j5dCX2XmzErgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1d9a03df6.mp4?token=d-OpZZX8pUpFnClSP0KHrvoNAFWdi54_xAxVdM3tbKRlMO893fQXf7NO4xvutiBzI7lL1MjdikrXf4Cqf1Mcydcs9E8lpNMZNvbick4eQy_sJqFbD7Z1_UK-zmH29EKuCMHYf1-_sGypDdTqvMDRoQa4MXiOna8uvrocY7Aah4r6loPtYr5zOL7bktJ0WjgpiPkEh-s-vSBuBvhvRbmiHioUXAbSfaNMaAzwlHNKs0mS3yEipi1j5GPBjc5uCoTBmXaToSQztjeYSfLYv9D8Bj8S_sjiTsRBhrHRFRZKcWHK8gx2XU0OjBnMp_sm3XrWZK8niQqoD2XDsC_p8XyGQ0vyLZt4-HG1QOnbIvEq-ZUP_FpAb7FoRPuBLpirS1rx3P50iG2FjS8w6YOcDJdv6t6IXm8FzgMvajB_771Pw7oU6fDCR7n_BMWaS0AOx0dUYA9_xz3j4tBbWri-RZHBvH0o9L84av0JACuSniWuiURLIwfCNbvrRzgjvmbEdZ2KdckApeEaBa9tPBuyQOJ7jdbqI3kAJTkKmZXfm8DBGz19oVCUAzvKkxwZF4SvlJQaf2FvYVCiDAnKtue_BNYSSjBBL948tOA1e_Eq56Z8T6t71GuaykaWOPQQvtd9m7E8Fh75hKY3jY4nzD0tebyNgFU-CH8f43j5dCX2XmzErgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
👤
ویدیویی‌فوق‌العاده از آنالیز مسابقه شاگردان امیر قلعه نویی در بازی هفته اخیر مقابل ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/30497" target="_blank">📅 19:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30496">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/777a222aa8.mp4?token=kstWO147ItG8YDyl7QN-lR4g1N6Ow6brXsTRj_FJUuB6EzokQKeiKVB95HjJ_eCUgXoEBnU1pW7ibK4XtWg5UMClstB8nblu5SV1iatk3B-L8HTItA-O2Rlx3qvk6tvVQ44uABwfQTAxyQrxUwO-bG8i1AGjrnyxUd9m5FQfI8lpBGN3oY_AgWCAwtcq6GS_6SMiouNv2j6LTMfKhYxOMMgQbo-G8ISBfR90wsE00dqeeVJmWNxdlprOmAMnRut2nybO3IC93UEO7RJLFYNQE33Gyuvfiyo0L68BM6lkMK_Bx4AAiowuNbjh2lT9bDJztF6OKWNffJhq1AX-9vy8DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/777a222aa8.mp4?token=kstWO147ItG8YDyl7QN-lR4g1N6Ow6brXsTRj_FJUuB6EzokQKeiKVB95HjJ_eCUgXoEBnU1pW7ibK4XtWg5UMClstB8nblu5SV1iatk3B-L8HTItA-O2Rlx3qvk6tvVQ44uABwfQTAxyQrxUwO-bG8i1AGjrnyxUd9m5FQfI8lpBGN3oY_AgWCAwtcq6GS_6SMiouNv2j6LTMfKhYxOMMgQbo-G8ISBfR90wsE00dqeeVJmWNxdlprOmAMnRut2nybO3IC93UEO7RJLFYNQE33Gyuvfiyo0L68BM6lkMK_Bx4AAiowuNbjh2lT9bDJztF6OKWNffJhq1AX-9vy8DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇧🇪
#تقویم
؛ هشت‌سال پیش درچنین روزی؛
ادن هازارد فوق‌ ستاره‌ بلژیکی چلسی این سوپرگل دیدنی رو در ورزشگاه آنفیلد وارد دروازه لیورپول کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/30496" target="_blank">📅 19:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30495">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ED_EKO70T3bOSE7_qvxspN-1dwemei5jY4krxihXNdYB98xpPibYvopMQaP2M97J9pgHu7WjXesXxq0SDdRnTyenP5KOvVpoJCe74rnoSaWFdyD5q0wclTVWzjiSSsJ02TH08KPS--Tl-qbuWUdeGXjYbCtv6yyKJxH9zRa2w_zyj8Viee8JiDZx3Jebj7Daal27WwXqwmklQpaDvpFkmnO-Q8i-v4fZdLLNnu-atdkfJ97r54DkC2EWfLSNuvEji6y98jV22HNYWqHUIOnTjVidwp5Grn-FQ6aSCTYnL0g-BYMq6PaJ8iMqa0Mf3w9A1jzNaHjUPJrStCqPsS3TDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی فوق‌ستاره تاریخ فوتبال روز 14 مهر آخرین بازی خود را برای تیم‌ملی آرژانتین انجام خواهد داد و در پایان اون مسابقه از دنیای بازی‌های ملی برای همیشه خدافظی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/persiana_Soccer/30495" target="_blank">📅 19:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30494">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇪🇸
🇦🇷
تعدادی از کاشته های استثنایی لیونل مسی فوق ستاره آرژانتینی در دوران حضورش در بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/30494" target="_blank">📅 18:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30493">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAbI6ifJfmAHlO2nRyNFYf5FWj3Y4k9KEVyNs02VJEJJM_vcT4Dc0r6d0Vc0Z6WJ9X5XNuFtjbOXAzvmxtxcjept92fHW-3Mqzkfz4zEoGD3dQnrHiTBEQrlLVaj-x_bgTDxH9pOXwNedvWuabJJ43ENFte0gCc9KjNyguBbbabmwd9e7tgitNhMG1SussA9dujf3q8TckkdpQvqfLlNTdsSTUdLyL7Xa9nxsuROwD34xRHOyN7HpP-ge2xoct65vbOENSVk_XSzTB_8EM-xbPscjYYScHcMwWuj8aqJCYoJvPyw8Bh8WgeadE687Fzrur-InMQ2wWyvsCMQy8m4fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇴
رسانه‌تلگراف: قرارداد هالند با منچسترسیتی بندفسخ نداره حتی اگه این تیم بره دسته پایین تر باز هم بند فسخ ندارد مگر اینکه سران منچستر سیتی با فروش این بازیکن موافقت کنند. بین رئال و بارسا هر کدوم 200 میلیون‌یورو به سیتی پرداخت‌کنه تمومه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/30493" target="_blank">📅 18:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30491">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fg3aLT8B7IL6k2nYRZm9FBQJciH2P79vgLQB9jtAqPZuHSF5TqaTUx8Agx1X8m9YE9A-4tO3GRIZf9BVzeDjvc9_zQu0wj08Lk_1EkzwZLbEo1Z6pl3XT4ar2Kd6H5Z145RlbuCMVPjseXGUMDSSRI6m4n0XDp-KWDYW4EJKV5K-htfPB3DqPXknhf8B2giuz0qRNmSQrl2r9ylhOmSRCzP3Wyg6bTVca4tcF5CLuHka9vqaQn7bU0j6IDqEvdT3YqjqPX5D0p-YG8meSlIiV9dyiooK8xGjK0boSJrltVD-oy1vkXZnm4sWfofIgYPE_wtRgEI6cRIuevZNxk1v6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LN0mztnn54mq_EFbb9JePTnc6MBVF4hxwmK4ofwxALseS1zjCDfhvsNirUlbpDQthjyReOEpADbyofsyWPDjmVasHHa_fDpC8bDdpVh6TtwZOqDT3ISfigYJqJHs4HoVfrjxGl2s15VwOnnA-xHqH9fMMxTTP9m7eveq55Q3tVdY5P4QZ7UbTRxEhfeaaLSwCQ17EdDpkVp_sZvGaEMhMSnKLZejxA08pvTwj-M12lhvgJokz7jwHkTtwynlI8_qAgSXiaU_TfDauoc648SAicN_slwogSS4U9AnoHpu7oGMKyVJVhsyH6Y0f6xVyFVJfxfzoq3nTrzoWDEVUlV7IQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
رونمایی باشگاه استقلال از آیتک سلامت ستاره جدید خودبرای‌تیم‌والیبال این باشگاه درفصل جدید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/30491" target="_blank">📅 17:56 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30490">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flxYzUcghegMrOgCdbBoxzD4A1zc9_0FhReQNvjfwjPiF1fa1vAHJHtTNPvIcN0Vo8S7VVt-NWax19oepqHlPaCWjwjaA1xADLBNUTEmX1d9WCzCYlREHsDdoldEyE-P9xlVMvDd3IgMmYIMpr4xxr1L5SgJhm3vBs8a97alAvdm8rPj5VBqFz5_NsLUbBGrBWKlmB8x-DE6pIRKEQz1q7oaOizFBCiFxJIhNqc22G2OPk10RGvVLGjuUAeRT-6TWegMSAMHyzDJgl73g48s28v6AkWaQbe6RJCDI1g8Q-dJa4rMiKBOun2c3wxYwukXGH-R2byftgJhP4-7OcvGOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقایسه عملکرد لامین یامال
🆚
هری کین دو کاندید اصلی دریافت توپ طلا در فصل 2025/26
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/30490" target="_blank">📅 17:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30489">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5IarIu6hqSVP4cTgGiUtIBQLSOeNYN2T3bJpR5tTdajg5Oz4j0SKvk1AECkC1scMp-lA1CWSeLI4lh0mwkXIRQO4EkIIgt8scDXGbKKUk8HzLuZ7YNljJfXWKTjLabRSVrD8UXAZtkPHPiXIG0wMqrFIr9CUgiQc0S-U0IenFXlM1rraircKmuCm_RvdXkB8weZq1vmIZGM72PJBJvZYgIAa0QUZNcaPIHXRvpyRkrY2Xawi1S31UEldHwvpYwvoCxDyRYQmQGEfx7vnq34KfiB7PHcpl1p5oqRsiAHmqW2OBT9Ra-eMefNkCh9e9xRWqFd0xayv_SCKCp_krlCBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از بی پولی خسته شدید ؟
🌹
به جان دخترم قسم اهل دروغ نیستم
❗️
وقتی حرف‌از حباب‌شاپرکی منابع‌دار میزنم منظورم همچین چیزیه
❤
۳۱میلیارد موجودی ناقابل مشتریمون
🎉
حالا بشین فکر کن ببین با پول کارگریو کارمندی کی به همچین سرمایه ای میرسی
🚨
با گردش حساب طولانی مدت راحت و بدون دردسر نقد کن
✅️
تنها کانال معتبر جهت ثبت سفارشات
🫰
💸
👇
🗨
https://t.me/Sales_Bubble</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/30489" target="_blank">📅 17:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30488">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5roCUt0B3pT8dyjilvwoaO-PWklojVQkHjXUYadwUIFiXYuGpQYOyBU7b98dLpmQvnSvT9lXMXk6xxNHrtzQ1ZWIJSABSuDGFitEvQLg8Mz8UJHmGEDUlhfEEJyC954vwp6BDZpEYQ1CSG_dnoRJ-T9veFfcRR0QhUPrE7CJJe9TjqkAQZEXPSbcx1ZAkyJheZBs3J_HGjGg86YE5Xp5cxiz7O9TxhTdN8ssogKSB120KtGO-wUrZG3eq4yEKHhRPxxRA_j1EE5pziaKC-f_EcvFU_M3yj2mv1FqVCSmA5MTjeLKFfdc379O6k0k9oc1m5_zWwES564k0sq1oEGyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصاحبه جدید دونالد ترامپ: پیشنهاد ۷ شرطی جدید ایران را رد کردم. مقادیر زیادی نفت هر روز از تنگه هرمز عبور می‌کند و شب قبل ۲۹ کشتی از تنگه عبورکردند. ایران می‌خواهد تنگه فورا باز شود چون خسارات زیادی از بزرگترین محاصره متحمل شده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/30488" target="_blank">📅 17:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30487">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_yUByA_N8d0fOFr2gLvVeOygbKUUeproHmgpqIeBEvLm6CV-S4P4GrY1j5V4mdTHR-QV7PxSHm2WoMyijyPKniJpshYaWl4C_iMhy_7VvlpbP8eS-0AfS3FlVFr9eGXDw2kukgmzJiJ-UdVmKexSsk8qNDwtKGYCYn03y4tgsWl3JRlwfEwe_CL9PzUdttWsi7gTz5Z9kCeW89Kb-YA396dS6W5ngtIKTnRIkcLP1mDIV6x6WytB_Vt5lcaq9oaWw7T2PPVXbyuCAnNxP4vHW35s5x9yk9C_TF0SUm06Dyi2XVpoWeVW56kxiMgd_-Owkud_FBcre8rtZ0Xv2Q0nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
یامال که قهرمانی‌یورو و جام‌جهانی داره: من دوست ندارم برای بهترین بازیکن تاریخ با پله و مسی رقابتی کنم، همین که سال ها بعد بگن یامال بازیکن فوق العاده ای بوده برایم کافیه! ۸ قهرمانی لالیگا، ۳ قهرمانی‌پیاپی درچمپیونزلیگ و ۶ توپ‌طلا برای پایان دادن به فوتبالم…</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/30487" target="_blank">📅 17:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30486">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NC-sivyCsdULjK8eLnTwHqZjnJX50B3OLXiOlKotpijyG1-Y2M2YZCCUa6cAhnY8o1sfGTw25IvucP2jZlmVzmEY7LPoWm-sI1CLi8wkI37Xv_TgWMoe1UpI08hr5IGSQnMoCL5fXsYVAGcDQynHMSGJbxXoCPGyGGfLiPx0Piffqnbm07j3akNgXNnI90SQwAfbcgQaBOuAWJkaBvumvh40Eq5MCJPmQrhwTrmvgoJpWlzADa2GuzjDb3DqKML4Nnc7jf6p4S6keY1-tTSn3a4Rcb_U_ewZQ5BqyroQGJ0V0LBq7rLTL5bfp4u9T2qEr0KLbMUfRbOrsOgdC_yfsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برسی کامل‌ودقیق سیزده سال ناکامی امیر قلعه‌نویی سرمربی تیم ملی در رقابت های ملی وباشگاهی؛ وقت بازنشستگی فرا رسیده ژنرال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/30486" target="_blank">📅 17:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30485">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bd7l1zZ6votKCueJAefnguZ3oP5MVV5K52ZWoyWm4yHkj8wb_8HP7FZz2fvmiluCsHqLB0jAKC8ZwYMxDESlHLONYzwHS_1V_CNVZv4K6YUQ0opCn3791UBWL_xJli0p1KfTUwnhbglEfKGSbTgDJriaRHUaS9nB0ctwK3WTCk09Os_TlDYy0XZ7CHgHlrMQkzdO6gLmkJllhWi7VGkQZq_oXbwxBr2JiLy-K-GSbima77InbPBAkXy_p6wWTU9mxVBMiJI8eBtkWDwYrAJ2NXUYjwnWVeStQxzic3HUYTULBXRI6mzgLt1lffBT90fG9cteA66S-1ni2tZ1EqsSSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبرنگار باشگاه‌فنرباغچهه که امیدواره هرچی زود تر انتقال کریس رونالدو به فنرباغچه نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/30485" target="_blank">📅 16:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30484">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQH3QUxY5RsWlc5HNS-Gvn1s_XggF5U_WUkR0MCL0K7BbqG-zqcT9DmEfoYsaNPhrfk9nPVj9fqvfFoB5BTsnoh5VbgcSbhf1Het1Zhis0YpaIQ9sru0Sh6SjkYKnc9RDtJd8FGHfeLS9HN32mpK9RSppIrrpgDUkLY4AxBEgaZOa4DE0KCnh_6Ub60aWUaHEAL8HxyVosD9xg6eWPrG1QpT8-6iw7x1Ku9779itKmajOzjXgQhRCic7tQGTE5Lx-xCJQRHwXlwNktb5bbVvKIRCNSGRPnC3RdJnCZWyY_w-UqLAd-ngWdNO8YeDD_VnOgeg2TnJfbNziV0Ak2jAXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام حجت کریمی مدیرعامل باشگاه تراکتور؛ معافیت تحصیلی علیرضا بیرانوند یک ماه تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/30484" target="_blank">📅 16:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30483">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHuIG5Ink5lj_m7LGvj2Ms4zYkFiLsTBLBuTbVtvn_ZLbD8ilyXzPsKpb06TUYEX-fuXG4_6h_vGHUCvoQxiTNLmC7z90xmgHA15ckZl3gk13aIA3YeSSP3JL01tNyp2_hWF2e8Ej_7BBYYu1GEjFTuDVVpBnBtDt6ht4Zqh8WdWbmkacQp25Gi4bpDZcoP5BGfdKyopP2Ro3Gu7FhNYN7TVrP5369Ua9s0AEpLENgararLb2Xod6fc2_885yQN-L1maFRALps_jwkV7khyTOwMpyuPJfalRLnghID-Rnj_nqBwsSTO55jn2XzK0keyLPWXvH0aKQcpwzc4emf6UKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
👤
مصاحبه دو سال پیش علیرضا جهانبخش کاپیتان تیم‌ملی: بانهایت‌احترام بازیکنان ازبکستانی هیچوقت نمیتوانند خودشان را با مامقایسه کنند آن ها نه در لیگ معتبر اروپایی بازی می‌کنند نه عملکرد خاصی داشتند، آن ها توانایی شکست ما را ندارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/30483" target="_blank">📅 16:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30482">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jh2ieWo2NgAdsyTzn2d5GRpv_uSUuAnbEJCf6msrTzg8RWi5dC1DVzHfOgJO6cNBJZ_IKiHUfthXXRaI6_Wl7BdOiPRAEpv1CseDejwm18qoiOssF92kFrd0oz_VjBiKZonSAYx7hlLdBP_Jhk_TYk25ByADTPT0eT7jF11QyJkqQxaI_Cmvth2suJ6WleqRVcY7OTfp64fa3Xk0LE9TXF8bnEiuhafZqYryZkWdNw9oI1tDzgAsRm9fKkJDyLXJ3Q0RW_hygSue-BL5mpW1nIcjjX5E12DgcW-Khod_D4pAUXNDQSYB8dqSm2mYDd5ZFe6e6KpJ6NRZptJbPzPTwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کارشناسان AFC؛ سعید سحر خیزان رو بهترین بازیکن دیدار امشب استقلال
🆚
السد انتخاب کردند. سایت فوتموب‌هم بانمره 8.9 لقب بهترین بازیکن این مسابقه رو به یاسر آسانی ستاره البانیایی آبی‌ها داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/30482" target="_blank">📅 15:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30481">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpn6ZpjOdzXzD7-YpTTE1mNk3t1QOd0BKxSjdUMFPJLSctM8CjxKKKbitjAk5v1OrXAGx2I6kZGDrI4rXHLVxH1uZX1BXXPgLou9VBapD8vVc9f_VEND6tgwuMHeJuwL-yBwcclIQiQV_XN4BdWXOym5KCYcNStVp5_f2fYCZQgYBhpjL4gJd6hSGTX9J-3FMK5j0pB-0ZgIKDbQSQxQdJx_wrUKnHyPSYxtcTiZBBcsSsqsGdiypnQnNlp7j0nErsC2jRTAy8f2yyYoIqhPrD3XGUx2uGstIbce6qS56XfiR6bhlIl-ocVcmhZOpuDj8p1xau9KNiiOYTOu0Yfo2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگه تمام هشت قهرمانی لیگ برتر منچسترسیتی از فصل ۲۰۱۱/۱۲ به بعد پس گرفته بشه و به تیم‌های نایب‌قهرمان‌داده‌بشه این شکلی میشه. تو سایت‌های شرط‌بندی احتمال‌محکوم‌شدن منچسترسیتی بسیار بالاست و ممکن این تیم به چمپیونشیب سقوط کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/30481" target="_blank">📅 15:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30480">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✅
تابانی‌به‌فینال‌مسابقه‌مسترالمپیا 2026 نرسید؛
بهروز تابانی درجمع ۱۰ نفربرتر مرحله مقدماتی دسته اوپن قرار نگرفت و از صعود به فینال رقابتا بازماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/30480" target="_blank">📅 15:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30479">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6y8HI07bKyh6812-ShlO5TJlFSDi4ffDf8yHYvHRIGgnLcTqmMGk8zyAdffYCkG8UbCn78KGM4BsDDP-ZI4W-JpvxBe8_Ch3ZoqknWLITFcXuRsfR9wTYEvnSQ9YKODwamHMc90wom-FwkkWDIuk53ukzGOAQdlhwOoXH2oz4ciBdA_fgfL_Au6R00CFv4rXWRSDf0ZrW2pW4Q11lFdLOgOOs3HjTSil3is4xjuud6fltzFnnKlMAvaq7oNFaPXxiVFd7U81q_3hKHOo90N3lNW1QXZujcEIhip5lOvPhY6SDXQMnkEwM-MkRi0mfwbSUw-UVLapafD9qhFdQ_gwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
مقایسه‌تعداد جام‌های تیم‌ملی پرتغال قبل کریس رونالدو و بعد از اومدن کریس رونالدو به تیم ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/30479" target="_blank">📅 14:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30478">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tcFV7W5GGSHfJCNjmE6K_5AXcoJM1d5ZxbgnyEAx-AqlYtSZKEhckJDxggrO-mkMHSvMIbHcL8EEXZB80lnCSakQstXh3l2SGZFEQlC9csj0V3F7dX90ISyJpxKAl_KTrO_bqp9UsF36fH-vEiKB_13sldIdOKmopqNT01dmHj5hxmQ6TjVL2HWqV9DCxR5H3_ejpQiCC5M0RjTHXNFr_UUlB5tbN0CveAgAzoC8lT_4UwlX_OIovlmrnKfihsJXN1GFkplneSSzFU6d4G4mlceA-DAecwSC7oqZqd0fJoonMVPzcFAwEbU82SBM-vyQLO0hfAI6I-wAfo1pefk1Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مدیریت پرسپولیس طی روز های آینده و تا پیش از نیم‌فصل‌قرارداد اوستون اورونوف ستاره 26 ساله‌ازبکستانی خود راتاسال 2030 تمدید خواهد کرد. توافقات بین طرفین انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/30478" target="_blank">📅 14:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30477">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXVPrd_jzvmTt3RTKhFIPfEWPE2zNM3zyMGqwhjOTQvt8-yAh7Ai4Ebt7ZJSf0F_j4yGL7awf-nbgTM8jk-7JrYeFYsnsouKIfJjS2Vs8yaOyMQSEKxjC_YEg0Fs0DOfS-X5mM0YphP3LdZj_WqrR71_X4pDu_7zblaqmbdqrDcTSELOreuoXbQtL1bYEx_K_8H9aXXXe7Tp6kPhhSQg1dIqZ9Uf-SsNE9dxvcpzQxjGkv0EqtBNW17mhC2BEJYE9VsmsTf04dMqZ6h9PZbOxcwKwfIbl7tLvIZODvr6QX_y7nSJN7X1XVssr8vnibtSTemYOu61SJ109MmwzZVmGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سلیمانی وکیل علیرضا بیرانوند امروز صبح بعد از کلی رایزنی باعث شد که سربازی‌ این گلر تا اوایل آذرماه به تعویق‌بیفته. او به بیرو قول داده که تا آذر ماهی راهی برای معافیت کامل او پیدا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/30477" target="_blank">📅 14:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30476">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USHWxtuDroylHAab6NSFB4VhXb1OsJCRfS9t6a6IbqulKh-Fg1FgsSyMnFw21S2ck9FF6DFVEskSURZHYq8A70xGHPr_NMBUYyCFZj34KSF3YV6cdVWLrEvM9sHJ17yKlZmevWzT1rWiCwyril7mRZQdWY8vrHtp-qBFnXz3gmpx8C-6txdhHusTFb5s_xNhb_z7EopZduN1RvBXVafFnl7Ow6nRqtWzRDs9TMeWBIhkklkvb_EwJsMO9mpDIx7aERDiRy2N_UZzVv1zBkNJF2HLLmc0lig5DUB3oZUHmU9aFy075HNBdNM1LEP6LTlsheUKGlkoR9tgxTGHHJX7uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کول‌پالمرستاره24ساله‌چلسی:
خیلی دوست دارم که یه روزی درآینده نزدیک شاگرد ژوزه مورینیو شوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/30476" target="_blank">📅 14:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30475">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">📌
قیمت روز خودرو/جهش قیمت خودروهای مونتاژی در بازار امروز
💢
آخرین بروزرسانی قیمت خودروهای پرفروش پلاک ملی طبق استعلام از نمایشگاهداران و دفاتر فروش خودرو تهران،/ ۴ مهر ۱۴۰۵
⭕️
این رسانه هیچ نقشی در تعیین قیمتها ندارد، بلکه صرفا اعلام کننده قیمتهای کف بازار…</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/30475" target="_blank">📅 14:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30474">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/am0fX_DxTTim3BLMVjZbIDs49BPC8NuKtVUTO1zcJdQeZwRG-RLR2wSorSGhbs6LvDnq6vWWopZeb6qf0rriaRvS7RAYyoflgD3-o_5P9y0H-910-DBu-hFHFqYBlg6dZct8JfF476J4yDZIvxZEWOf7gNT_jCqlfvZyyR6xdBmzLeJeOKmyBnP1wCx2LzDXsBLQLSL9UdTLglRDRZ_Dpx45NphQAnmvisgEjryipBlpyzRV58E4fxpb6YKz9_IZ70MHKxlKeJhd1YJFZx29USrwMPD6GGwzZgysVRSL2pA-ATNyd2Pk6a82tj71DTZArMOrFmEnrmjyvZiEXxW8Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برسی کامل‌ودقیق سیزده سال ناکامی امیر قلعه‌نویی سرمربی تیم ملی در رقابت های ملی وباشگاهی؛ وقت بازنشستگی فرا رسیده ژنرال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/30474" target="_blank">📅 13:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30473">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HIa9rh6lgi_pWyaG6Uyj4_QnDD_eI77fV7uX8ZOBAkeH59HBY1TaG26rvOj0BUEVzAbrs0sTdsXFSCPKEjLK3kF1_r0NTD6NYcLjffLBhxbi7_kOY2t0peD_iONnjmpdlahKPA6idDcu_T_j--E0XFKax76eWO9ao6mgFVztSCR3LnGmxDfW2rT6aIJz8TDqFiafMkjNa-QTFqHP7qF_RPfOIRp1IQtIPNCGSqCtYdwkRprrpHD3r0HRo0Ttzcay9DeuzN37VMJLFC8K57zZeX43RSAvHq9hOPdwVJMh1Dfu9BXc95sQ1cO6I3hBxbkwQWhhBsdV6qLmvH0zYaKvLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🟡
#نقل‌انتقالات|فلورین‌‌ پلاتنبرگ: جیدون سانچو ستاره‌انگلیسی منچستریونایتد درآستانه عقد قرارداد و بازگشت‌دوباره به تیم دورتموند قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/30473" target="_blank">📅 13:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30472">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63e94cf509.mp4?token=EC-ukQASjMSnl-YEtKsh9kSvyH0rsgNXpt3bVj8jQw3wf9oDX95HcXeLm42GjxMUDmBGWZtVWULNZCGYZ-sPbhXSzwXuBqRtLom_VP1ihDryw0oJ9wsm02z7qf_GOt4mcmY7k3CM_piKT5QVQfmwaudY857BNznz7Cq95zAY-WNh1XQv1YPXOad0VtemlqzoIPGeJRitVbjx7TaMsQFZdFepZFKtkh_W3Bg5xfRar7nkNo57IKAun7mGjE6s0RUl5ZyagAQWKCJLXjCfczBWHuCafigSLiz_oY6ArkgejbdbfUiznqLcx6nMSX_MMrETGdIp0wODXC6Qo6Yo7YZboRIvSxsZxpaIPjBamyzn-A-91KLqFxLWRpcUKN05_KURDU_4nSfsd7ldZJIVJ6_9wlHzap_ctiuyL23UN2wxTv2Ed67jBZJef-HDioJo0ePU4DJDPTZqsh2OcQVqTzUHakAjgQoClkAFMliNMd-F6GNJi38IEqnpaWQzGTU0K1oblOrTcb7uk6u9Xp61Kz-2mFbXQafylj_0icoaoEVL8iOYTMaxc_G1SpSZNIzjZDkU4fMJ9RoOTY-jBdeu72iISAgj96hWXk0el7q8GDxT-y9fKsqL8P85WfTV7CuArOGSd6T9jKsB4_hmP0YgNdx5rE0BGDI6voUGMJ7VvcTBt9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63e94cf509.mp4?token=EC-ukQASjMSnl-YEtKsh9kSvyH0rsgNXpt3bVj8jQw3wf9oDX95HcXeLm42GjxMUDmBGWZtVWULNZCGYZ-sPbhXSzwXuBqRtLom_VP1ihDryw0oJ9wsm02z7qf_GOt4mcmY7k3CM_piKT5QVQfmwaudY857BNznz7Cq95zAY-WNh1XQv1YPXOad0VtemlqzoIPGeJRitVbjx7TaMsQFZdFepZFKtkh_W3Bg5xfRar7nkNo57IKAun7mGjE6s0RUl5ZyagAQWKCJLXjCfczBWHuCafigSLiz_oY6ArkgejbdbfUiznqLcx6nMSX_MMrETGdIp0wODXC6Qo6Yo7YZboRIvSxsZxpaIPjBamyzn-A-91KLqFxLWRpcUKN05_KURDU_4nSfsd7ldZJIVJ6_9wlHzap_ctiuyL23UN2wxTv2Ed67jBZJef-HDioJo0ePU4DJDPTZqsh2OcQVqTzUHakAjgQoClkAFMliNMd-F6GNJi38IEqnpaWQzGTU0K1oblOrTcb7uk6u9Xp61Kz-2mFbXQafylj_0icoaoEVL8iOYTMaxc_G1SpSZNIzjZDkU4fMJ9RoOTY-jBdeu72iISAgj96hWXk0el7q8GDxT-y9fKsqL8P85WfTV7CuArOGSd6T9jKsB4_hmP0YgNdx5rE0BGDI6voUGMJ7VvcTBt9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ناراحتی آردا گولر ستاره ترکیه‌ای رئال مادرید از مصدومیت کیلیان امباپه در جریان بازی شب گذشته دو تیم ملی ترکیه - فرانسه در لیگ ملت‌های اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/30472" target="_blank">📅 13:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30471">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3tDiZ7DZfL-anynF8tZhoQdDnVfoJTZ1nM5SSf5HrDlb4fproAf_eGH3qv918u2KP4jvb-89TJEkq9Xha7odFqNMtXkkUinLVBKlUa8ZWIO4aXP5E0EbmmnvWlZ9MO76QerQ6ud6jjs_veF36GVHuWr6Crh-FMGSi_PqZzDFRe9hz4Yc3n-wIzj__ZzCe9hEyXO9i1Kfx2pT-UA-wLj1k7qKM1F_RPXror26GA3EIoc97wMOm6I8ir2_LkO1hp4MiWP-JcNlXtGNJ9lxfwQ3H1mMJQ2uRwDAbxhqliMDY_Q3aI2ZIKTSHnpczrW_fTSJrg5vVMd18ZcnX2tiIlkUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درصورتی که اتهاماتی که به من سیتی زده شده ثابت بشه جام‌هایی که در لیگ گرفته به این صورت بین این باشگاه‌ها تقسیم میشه: منچستریونایتد سه قهرمانی، لیورپول 3 قهرمانی، آرسنال 2 قهرمانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/30471" target="_blank">📅 12:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30470">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWI77XTPzH9cMwdPZR5wNUyIK1lWal3oK3QYs5c7zMRlEWYA41XvwyKsyPCqXEdU4fOYgD4HNG3GwAUJs-WeeY_atx2OmqGzz2tkgr2cWeX-z-YxI5LhDqeOebOrSlY8_LQY8I82Oltyf2nSPdu6jhZb0I-_hhKF-TuT08ruPWmke3TNUtReE54wwYUyF0rd_hRaCfaSE6zp1qbG9ewgnrlNbn1stUGLhgqf5770ePM12PMb0NkHMMt-2nb8Xdo1Dc60wzyhWgoPWg_eGccmYYoK5CIp9IgJIcahdxmOClWHO_GlECa8PV-gh8v6tFY9aNzKRCXBCH5mODAEAba26A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇹🇷
باشگاه رئال مادرید برای تمدید قرارداد آردا گولر ستاره ترکیه‌ای‌خود تاسال2032 به توافق کامل رسیدند و فوق ستاره به زودی قرار دادش رو تمدید میکنه. پرز دستمزد آردا رو حسابی بالا برده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/30470" target="_blank">📅 12:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30469">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWbo9fcojbNGxB0XZ_ub-OAhJoRRO_FfzhGVu8ott5-ByX0vOUUPMvCr94iXH4KlieWNp-izmRG0mEuXOW6VVJMNLumwBbzYGZf7Vs9ZAWhbwCSX8JwoWz-Omsadg1bRqMlCHhymiVo85teK9GCUk24_Gvo2TKLFqJI0vrTe0Lai3FHE7eZyqQ99KeDpC87sKBG3NKYG_-zvMsLqchdfS42JAEAYaQc4Aknbf46tKirrDXEex42uPwBXhS9vuYuTNAkMVGREqTmECVr_lxbrJC9Tn0qdTvF1anypn8L4-Pxw00fuX1JaCdzxVWx3NTyrimUlZ8fJbP3KDNzNgvBuow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
شوک‌جدیدفیفادی به مورینیو و رئالی‌ها؛ در فاصله یک ماه تا دیدار حساس با بارسا؛ کیلیان امباپه فوق‌ستاره رئال مادرید در دیدار امشب خروس ها از ناحیه‌کشاله‌ران مصدوم‌شد و زمین بازی رو ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/30469" target="_blank">📅 12:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30468">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea4b13e0d2.mp4?token=HOnyAVdNRktEj0azqwZT0qqOXFIAarlKq1UKTcllNTg0M1XC-9M_6L_bODCBE4jEXuUAgGGBg5jvVH7bvL232pKrFDV-kZ2vdMAHNRx1mAZNa59Fucmg51rvssr8cAcprA_tT6yZB1z0yk9WtjBrTscsO2jLSvvnusEhu7KNt_s23Ze5-fGx4GAZ85evZeGdQ8tOwW109qYcFhO4FCjj18NVBFHtfeixteDLb-hRiPw9-6HzkCtFat-uKIdEMV3mE0fCQwISRjPEeTQ0GzJOQG5I04WNaQvpY4sF2LS6lPZ-UtRavhiqyZHqJlJ6BU3mEZEGYTjjOO2fsi7RvcXDzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea4b13e0d2.mp4?token=HOnyAVdNRktEj0azqwZT0qqOXFIAarlKq1UKTcllNTg0M1XC-9M_6L_bODCBE4jEXuUAgGGBg5jvVH7bvL232pKrFDV-kZ2vdMAHNRx1mAZNa59Fucmg51rvssr8cAcprA_tT6yZB1z0yk9WtjBrTscsO2jLSvvnusEhu7KNt_s23Ze5-fGx4GAZ85evZeGdQ8tOwW109qYcFhO4FCjj18NVBFHtfeixteDLb-hRiPw9-6HzkCtFat-uKIdEMV3mE0fCQwISRjPEeTQ0GzJOQG5I04WNaQvpY4sF2LS6lPZ-UtRavhiqyZHqJlJ6BU3mEZEGYTjjOO2fsi7RvcXDzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
تعداد از کاشته‌ های استثنایی کریس رونالدو فوق‌ستاره‌پرتغالی در دوران‌حضور درمنچستر و رئال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/30468" target="_blank">📅 11:51 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30467">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c87985ff1a.mp4?token=slWFqzdcI6z2_0EShEfBdgWJYY6Lid7LGkHRc70pV6InPcf0KYsxzYj0dJzgLGz_sW1CUTytbfKBqUCA9rqWHJWzPymtunb8fxaDiW9sOIn6wKlev4b0ZW7uPbGp8cmEtkCyyps4sArTBrHzzRG9y3QNUjNu55oRnAKwpsga5F_tlEY0rVGpWKyOJE7SIi023CvUvGZPT_RAAzS3lghXeS1jZm1h3ERDf_ZhHy1GjDpP5zN-6zgVzjm20q4jJgBiY0AXBPq63I6rFtaiCSo2twECH068rw-TbCn9xkrQUy8RvVnDVomL4pWpGdW3OWQj3J-5JnmfOySZTGxAjXIbYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c87985ff1a.mp4?token=slWFqzdcI6z2_0EShEfBdgWJYY6Lid7LGkHRc70pV6InPcf0KYsxzYj0dJzgLGz_sW1CUTytbfKBqUCA9rqWHJWzPymtunb8fxaDiW9sOIn6wKlev4b0ZW7uPbGp8cmEtkCyyps4sArTBrHzzRG9y3QNUjNu55oRnAKwpsga5F_tlEY0rVGpWKyOJE7SIi023CvUvGZPT_RAAzS3lghXeS1jZm1h3ERDf_ZhHy1GjDpP5zN-6zgVzjm20q4jJgBiY0AXBPq63I6rFtaiCSo2twECH068rw-TbCn9xkrQUy8RvVnDVomL4pWpGdW3OWQj3J-5JnmfOySZTGxAjXIbYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
چهارده‌مهرماه شاید یکی از آخرین شب‌هایی باشدکه مسی را باپیراهن‌آرژانتین می‌بینیم. شماره ۱۰ بعدِسال‌هاافتخار، جام و خاطره، حالا به‌آخرین فصل‌ های دوران فوتبالی‌اش‌نزدیک‌شده؛ جایی‌که شاید هر بازی، آخرین قاب از حضور او در زمین باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/30467" target="_blank">📅 11:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30464">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c60d4945a7.mp4?token=VYVnIE0GdBzAQJszV-NEmd3T8drTENTasLg89ZT-5zEUBSbrDjcKrZoj3w5rxYNIczsQK6H6NmxqhDCQHeGDewcmR8SY1U8wHu4v5TOmvbrCwizD8ygo-zKDPWqsS3cp04DM2Kc1S9c8LNyVuaayrAMODKzfW8dkQzRe8ypLv23vixsqXXlq-SWam_VHqFFPBZDZvykSAa_TnkDHG_WwIb33N3EvJFc4X3ae70bOPfKRyIXpbPukiKgQOu4zlmF_QaliD2jYO-vUcVyETKR9vkrvaGoY_HZZ1shnWc2GPTb25gOqLE3y4I-Zr89P28EOGzw60ziKxcwXK09Ms9ICfSx1qPcakrLqllo4HAqv1nBWrcjQTWitaF9Cj5AgqSqpCYX0tcvN9ArdEBoTthba_YKaVK5E1EV1ytGam5wWv-tlnFBGCUeIVxXD1k-I6kbepteUGueys6Tbna-KJ2vHOnp1yejFmh73A1ko6hbJSPg8LOpYG1gKvPcUyhITZaBKszqt_dAXevo4pY_mly0upnSKnYEE7_K9Cnm8vnt9ih7gQR8ZdhLio_n_uFX9xQJpOaOS5jOtDj_rhc2xj2GDXU1GRi63JAosCpeY5NoPJ8vDJ_NyUsWrKcJ41MOAbVmlq1eSfnU-0Ntu2lr0-aPEHRaNpQEDfgB35Y2RvFDM30c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c60d4945a7.mp4?token=VYVnIE0GdBzAQJszV-NEmd3T8drTENTasLg89ZT-5zEUBSbrDjcKrZoj3w5rxYNIczsQK6H6NmxqhDCQHeGDewcmR8SY1U8wHu4v5TOmvbrCwizD8ygo-zKDPWqsS3cp04DM2Kc1S9c8LNyVuaayrAMODKzfW8dkQzRe8ypLv23vixsqXXlq-SWam_VHqFFPBZDZvykSAa_TnkDHG_WwIb33N3EvJFc4X3ae70bOPfKRyIXpbPukiKgQOu4zlmF_QaliD2jYO-vUcVyETKR9vkrvaGoY_HZZ1shnWc2GPTb25gOqLE3y4I-Zr89P28EOGzw60ziKxcwXK09Ms9ICfSx1qPcakrLqllo4HAqv1nBWrcjQTWitaF9Cj5AgqSqpCYX0tcvN9ArdEBoTthba_YKaVK5E1EV1ytGam5wWv-tlnFBGCUeIVxXD1k-I6kbepteUGueys6Tbna-KJ2vHOnp1yejFmh73A1ko6hbJSPg8LOpYG1gKvPcUyhITZaBKszqt_dAXevo4pY_mly0upnSKnYEE7_K9Cnm8vnt9ih7gQR8ZdhLio_n_uFX9xQJpOaOS5jOtDj_rhc2xj2GDXU1GRi63JAosCpeY5NoPJ8vDJ_NyUsWrKcJ41MOAbVmlq1eSfnU-0Ntu2lr0-aPEHRaNpQEDfgB35Y2RvFDM30c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعدادی از گل‌های کیلیان امباپه برای رئال مادرید در دو فصل گذشته بعد از پیوستن به به این باشگاه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/30464" target="_blank">📅 11:18 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30462">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KoQIDkzcTAB5A3Ezn4z_od1C92uvyQhvk2gqFUgH_NACKu8-A89KXj0ImZT1xv0dDtkuzurl8Y5NaFB-sRse1yxUR2Z0-ELdz7xyiiz7cMl38cFFuzNv6mzwm9Y7LHCkovpOtY-hinrCgxF-Sm7anjfLOSyapbGkuNVnTEJuIsARHJlO7-j8C2empbpRBQeKC4KM3c87n5Lrj9IjKePTH34hzwE9zDCjLZ57kcZmcqYzuRyjQ7iNtEEwvyu-3AFL_m61-2ucv4mvUieGzJ5yreLQdRIxCktE63hyVeZaQR0K6EaC2XEeYxhEj3Fhl8p9T2w3FX1ejCezMM2csDcM7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y0TplsJ27ZIn23ScXfZ9FirUCYIUBRJgzftVAViqKRGYG6Frt5bUJDRSh2Z0YPWfBpMzq9KdFpLkZvh3AR54JHMJXJu3xVv7bII3ilefxGu2zYItGi8K-2x4uehZ_NCVJmVaunhjUywEmUh-OE4iBDIfxS01ZHSEYdtKKyrmNOpA6LP4y0pqRmxEqFDx-agKQ7L8BXQs4CGbTjcX-vx5NvF8Utkl5Na3wvE7AHeVBuwjc7vjJh1I6--V2efPCsSxDrU08C4Hkhh-qJAmEWUbzPUcgQIc3FoMo1G-fs6FH1dZiaJBEAshyozgsSGYrE_4mcnUWsICLZ9eb1-ImnN1NA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
برسی کامل‌ودقیق سیزده سال ناکامی امیر قلعه‌نویی سرمربی تیم ملی در رقابت های ملی وباشگاهی؛ وقت بازنشستگی فرا رسیده ژنرال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/30462" target="_blank">📅 11:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30461">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه‌استقلال تاپایان‌هفته جاری 400 هزاردلار به فابیو کاریله پرداخت‌خواهد کرد و پرونده این سرمربی درفیفا بسته خواهد شد. نظری جویباری پیش از عقدقرارداد با ساپینتو با این سرمربی برزیلی قرارداد امضا کرده بود و حالا بدون اینکه پاش رو تو خاک‌ ایران…</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/30461" target="_blank">📅 10:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30459">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6160de2528.mp4?token=XLJfWScQCw5B4zfvWKfZJWR5k6jSdhNehY8uFmfxoz733Ix4PAGhpws9TzMER2Si_A1-0ND3z1ghdI8zjiJrI8GuXCKKYPVqpoemjsJkIF9BZuw03Iv2zVVCIi_k3Aa1VNa80TSSdNglUFxjgNK4HqoGDQMhU42HB763DgZmyhQnKXaitfSVCOOeCb54ZXQV7SH5Ix4_JYSJDXUeVyAQwX6wH3hkCg1WMQgG50U0VOhbLdEO5SmoAvdEOfCkCqWPkuP2933SUH6bWpi4bV-4ilxZ3LV7Gmpfg9pHuY5GgzNYRfxBfXPIZ4VaWAfmmbLY29_m06B51iz408omL8fqag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6160de2528.mp4?token=XLJfWScQCw5B4zfvWKfZJWR5k6jSdhNehY8uFmfxoz733Ix4PAGhpws9TzMER2Si_A1-0ND3z1ghdI8zjiJrI8GuXCKKYPVqpoemjsJkIF9BZuw03Iv2zVVCIi_k3Aa1VNa80TSSdNglUFxjgNK4HqoGDQMhU42HB763DgZmyhQnKXaitfSVCOOeCb54ZXQV7SH5Ix4_JYSJDXUeVyAQwX6wH3hkCg1WMQgG50U0VOhbLdEO5SmoAvdEOfCkCqWPkuP2933SUH6bWpi4bV-4ilxZ3LV7Gmpfg9pHuY5GgzNYRfxBfXPIZ4VaWAfmmbLY29_m06B51iz408omL8fqag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آلیشالمن بازیکن‌تیم‌بانوان‌کوموایتالیا با انجام این فری‌ استایل در اینستاگرام کریسمس رو تبریک گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/30459" target="_blank">📅 10:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30458">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eT2vXESX6hIBByGJNd95TeErOTTcmiNKU3E0AuzuL4zjj6tQuV28jIpsroM8FY3OA4cSAKTIl3QX-jnLzKEt3IiFbIYY_6jH9hrakpfzPXIisee7YMufIiZ2AYO1Qo5DkGZBaNvJqj8KGQjzO6mvGmlGDdL5RawOoR5hJN_a_ou-e8uJTmSiqg3m5xIu3QOvxqM2eNYqxjdd7hlvNFT-_SDOC7JXl_3lfPr4fj5TamHeto02KT5tfG0YVlrp2gfkuQVS1OHFMfI7XB7Z9cAEw63T4k-vIX23eg2hvAPsol4sg3SFV0O6zswvH96c0aaUpiUWm17mNPlYkuSLy6Gxzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های رسانه پرشیانا؛ باشگاه استقلال مذاکرات مثبتی با فابیو کاریله برای تسویه حساب و بسته‌شدن‌پرونده او پیش از شکایت به فیفا داشته و بزودی با پرداختی مبلغی این پرونده بسته میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/30458" target="_blank">📅 10:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30457">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLxhnGwp036NgmvRXDacvaZGdgIt73PCaRmFA_VNge7yXRrmR6TmYzHo1jk5Qcrl0g0iVF8jDu0inv9UwiCdScd8YVO_-0MQFwhwcYtJ0eGvSBw-phK4Cye3Zczm-tSsR-GarWDdOoaJWzFOuvJWvXIO8pQ6-kXY-aAHsongQecHXZLbLfmy1BngKoJH8iYBfFGgV4lzmHsoCXQPb8dg7JCI7eUl8PTOrKKt9Me16hXsn78LdFj9WG2Dh43fLDDYEYXEhRRhOA5rE5kxmDpqSw_q9S2C3JkXBMQdb_JbBp1oL4N4n5B9TGu79vAHWhi0qAmQVUz7N6p1PjD1XoHOnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درصورتی که اتهاماتی که به من سیتی زده شده ثابت بشه جام‌هایی که در لیگ گرفته به این صورت بین این باشگاه‌ها تقسیم میشه: منچستریونایتد سه قهرمانی، لیورپول 3 قهرمانی، آرسنال 2 قهرمانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/30457" target="_blank">📅 10:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30456">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari.apk</div>
  <div class="tg-doc-extra">46 MB</div>
</div>
<a href="https://t.me/persiana_Soccer/30456" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
جدید ترین نسخه
اپلیکیشن بدون فیلتر wepari
ثبت نام آسان
✅
📝
🖥
رابط کاربری راحت و سریع
📲
کاملترین برنامه موبایل
🇪🇸
اسپانسر رسمی لالیگا و یوونتوس
🇮🇹
🎁
بانس 100درصدی  اولین واریز
💵
Promo Code
:
sport100</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/30456" target="_blank">📅 10:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30455">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPepFWcOaVkU6spaqFmB159X3LtsYyVmUgHPFGpzWVQ9hguiFlMvGqJRvHIuU8lRF667bmTWuD3jIdXdTfs8dusW4AdhahkwZ7rWAKs1PSGUXy9QdHf0c54gIFcdUJbLzqYAz9IlMJv29HK6W2oIDgLtQEYdaiYbL1Q2IWS5pwLQRV48_Zf9QL2BeSHTJ2RYWCmHdsi37b5siEwX_hBZ3naC6gvgTmXLKHaMVgeQbCadXwmyQOdGHtrnyXMUS5etNCSNvB_dbTHMzNiK2oGw_hcbiKDInfqi-JTWdiroFQxUkgardcoyccOdn6YhRZDhiM1v-rSPdPOchUhgL_FGzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
بازی های مهم امروز را با آپشن های تخصصی
در
wepari
پیشبینی کنید
👍
💵
امکان شارژ یو ووچر پرمیوم ووچر_ترون تتر درگاه مستقیم بانکی و...
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
🎁
بونوس ۱۰۰ درصدی اولین واریز
🎁
هر یکشنبه تا سقف ۱۰۰ دلار بونوس هدیه دریافت کنید
📱
کاملترین برنامه موبایل
🇮🇷
پشتیبانی از زبان فارسی
‼️
لیمیت نکردن اعضا در هر شرایطی
برای ورود به سایت
فیلترشکن
خود را
خاموش
کنید!
🔑
❤️
🖥
Wepari.com
🖥
Wepari.com</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/30455" target="_blank">📅 10:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30454">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f59d54b38.mp4?token=lymRA_YQKC8WaRZR9j5fTNxtnWaM6qAV3S2ddM7yLuwokUOvh-e3fQpyrioW2h5Drt9ZmiDtgRR01jNMoXWSlQy9Qp-VXak-6Nw7Qhj0skPdvR_CNl30z6WEVRRliXo_vpd0lqDwa6nM6Ecs7qNR8XhDcZYH9WSIUz8r5M2NgMcWhPV2FAAN5tiJ2qR-KkViJS6HnTugSZIPOrKkaVXo2yOQIkTYHcmjNz5zHCIeUVvkheUow45Lb3CAzlPCEI36aDScgUK1UxZ_bJSsO-RqNTd4_lfiPURrjgVytnaMJ5_2OWwJtZmS6xZ5u836sPNgfYf0cODlEY9fSS6tCW3AqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f59d54b38.mp4?token=lymRA_YQKC8WaRZR9j5fTNxtnWaM6qAV3S2ddM7yLuwokUOvh-e3fQpyrioW2h5Drt9ZmiDtgRR01jNMoXWSlQy9Qp-VXak-6Nw7Qhj0skPdvR_CNl30z6WEVRRliXo_vpd0lqDwa6nM6Ecs7qNR8XhDcZYH9WSIUz8r5M2NgMcWhPV2FAAN5tiJ2qR-KkViJS6HnTugSZIPOrKkaVXo2yOQIkTYHcmjNz5zHCIeUVvkheUow45Lb3CAzlPCEI36aDScgUK1UxZ_bJSsO-RqNTd4_lfiPURrjgVytnaMJ5_2OWwJtZmS6xZ5u836sPNgfYf0cODlEY9fSS6tCW3AqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مورگان راجرز ستاره انگلیسی تیم چلسی:
کریستیانو رونالدو بازیکن مورد علاقه منه اما من در نیمه‌ نهایی جام‌ جهانی در برابر لیونل مسی ۳۹ ساله بازی کردم و باور نکردنی بود، تصور کن در دوران اوجش چی بوده، نمیشد در برابرش کاری کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/30454" target="_blank">📅 10:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30453">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b295745c6b.mp4?token=MN6TORNuE4dlB_jK2iVS0Jk1qKZbVhSfulmCgL94ge0Brp1pwSb8JZQrPKfOG2IpeJAarIB5X-mtC77CiJY5cVFzflLip7AqFTPEMsZtk9A0TclVtvPHiK3U8sc7ErfXDwh3Lxj0Lmsh1xd5Gw-BGsyw7Z3Vo8OFdUoEPhRBrW2DtkmxH01iAv47vpDsrNQRjQRdfsu3cztw6QprS07rKSBh5QvGnd-3kvw9i_uhxgrzj2fwzxBxtzJ29mwPU3KfdOM4AtmwSoA-9ZAaDQXie3FrecGP2wCccfMY5jSg1mFNL2A5j_jTLJxyHl1GtektcAwk97iT9qkl2ZHkRJ-FZWSES_WUkL0iFK9Ynjn8MMaamHnmRvTDGOY8M1psFbIvLhrzlD0vFJnC3nSSrve1A2Wr44B8rNW3fsuEFTjBjSDU6XZO0ZU05mAl5lp5AFijITQl-5_IpoMlpd5QbKy0biPBCJ36u3irjwTEBt1Y5RThFUnPVBkxiKXzAz6IcjGjluZLb7Qto4ovNWTyYBa1Y40cDrqUhvlTkgEg1cmqBEPuqPrlhbPuPpfqGKnmCw-sfb5F747fu23PUEW1YT3KOcJXBSHKe-7g4A7IOP-1LVZMcoVBSk4HM6vKqvj-BXHbZzJiCrYcSjugP8x5XJdRHR6IpYLvg4W8oZTj-tR1Gbk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b295745c6b.mp4?token=MN6TORNuE4dlB_jK2iVS0Jk1qKZbVhSfulmCgL94ge0Brp1pwSb8JZQrPKfOG2IpeJAarIB5X-mtC77CiJY5cVFzflLip7AqFTPEMsZtk9A0TclVtvPHiK3U8sc7ErfXDwh3Lxj0Lmsh1xd5Gw-BGsyw7Z3Vo8OFdUoEPhRBrW2DtkmxH01iAv47vpDsrNQRjQRdfsu3cztw6QprS07rKSBh5QvGnd-3kvw9i_uhxgrzj2fwzxBxtzJ29mwPU3KfdOM4AtmwSoA-9ZAaDQXie3FrecGP2wCccfMY5jSg1mFNL2A5j_jTLJxyHl1GtektcAwk97iT9qkl2ZHkRJ-FZWSES_WUkL0iFK9Ynjn8MMaamHnmRvTDGOY8M1psFbIvLhrzlD0vFJnC3nSSrve1A2Wr44B8rNW3fsuEFTjBjSDU6XZO0ZU05mAl5lp5AFijITQl-5_IpoMlpd5QbKy0biPBCJ36u3irjwTEBt1Y5RThFUnPVBkxiKXzAz6IcjGjluZLb7Qto4ovNWTyYBa1Y40cDrqUhvlTkgEg1cmqBEPuqPrlhbPuPpfqGKnmCw-sfb5F747fu23PUEW1YT3KOcJXBSHKe-7g4A7IOP-1LVZMcoVBSk4HM6vKqvj-BXHbZzJiCrYcSjugP8x5XJdRHR6IpYLvg4W8oZTj-tR1Gbk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌از این چالش عبور توپ از اشیا؛
هیچ کدومشون نتونستن کامل توپ رو رد کنند تا بالاخره نوبت به اسطوره تاریخ باشگاه رئال مادرید رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/30453" target="_blank">📅 09:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30452">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWfY4K3GvHNVY9HdAORJ-AOHf12lzLVJGSeqfjUn29R8YJjdjafgwOozofsEOTlmarmAsyTZ26s0tXdwwALkRfqum2Smst_SFs902wf0Rk1NBOWbGWlmsk7VFs4tT3qdjyiDWGxrr6cHP-5DqVLcsKxEfUi5nrI4X8IatNjTy1Uf1tpRCsQWG41tRA4HPzda1JM_ReSQjwVU_lZGY4OSUleuzsPdOwIBogisGY5rLgq_rSGRuf3-av0fMSTQRw9O-tAVEXd73rzCM5Wds_eA1bkSxMRZ4PzHGxy0xsCb5r7Jd_Zgdywbdb5YJGF3sDTKrh5PA4vtWRpEGENoWwuKjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇫🇷
#تکمیلی؛ بااعلام‌فدراسیون فوتبال فرانسه؛ مصدومیت کیلیان امباپه از ناحیه زانو هست و بدلیل جدی بودن مصدومیت امباپه، او بزودی به مادرید باز خواهد گشت تا روند درمانش آغاز شود. گفته میشود امباپه حدود 3 ماه دور از میادین فوتبال خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/30452" target="_blank">📅 09:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30451">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/th76l21XZsYjIqECtQQtOxKs9gOBEvPk3D3YrA3i3kAiMTxY6zVs5se2LGa6kT0OfI38O5TIwHWt7Dtw-V6CY4_HqLbFgsbIQUGN0XWFVKdqx-I5gCPwZIxeo4Q_OJrXohKt3ES9OftCU8qIJ_pQgKtJdvnTCigiIz1w43w9ciL_9QQ76ksBD8EAERRXIWBYxKxvIg5wXqiLcxmPcLXisO8-9si9gn7dFqjq0eONiupxVrSZDYvjRNWRg5orvYBAjm4BFx8UQovRgt_aDv3zFwiokRyjxk0DEh1e1F67FC7qNhVv0U1kBu42t7XJrvTyC6a6YwP3unrj7a7i_U4D9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇳🇴
رسانه‌ های بارسایی در حال مانور دادن خبر انتقال ارلینگ‌هالند به‌بارسا درتابستون سال بعد هستن و قصد دارند بافشار به‌مدیریت این انتقال در تابستون 2027 نهایی شود. از نگاه اونا پرونده انتقال آلوارز به بارسا تموم شده و این انتقال هرگز رخ نخواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/30451" target="_blank">📅 09:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30450">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W04LDYGbaNrdC1C0Ozay2sbMUDQEQ_llchIrfhN-BdvWy9z5eyHrIQCsAemST-fBJhoNLFDq3GcQoG3IdGp4Qwg8G5CvYxjE3VWCqf4bYJn7kwFqsGttbqSHYinp3Q0EfX70byhit1IfEiq8Z6gSrVSZE2ZmhM-eHgNe_BriP2hCR_8dYKYd5bz626AJmEHXZ9Mdv2yYyE30sMSy7txoKUf-KoqdRKNldD7AF13oQltou603StpEDO7aDsEDPpTiedd4NNLj1vn8EI0hsEr8ayTLrCnoQzmY9EffoAKAKLa-doHLqQ5eglFjllP2ld5pya-Ke7EEvca03uSKRvorRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
شوک‌جدیدفیفادی به مورینیو و رئالی‌ها؛ در فاصله یک ماه تا دیدار حساس با بارسا؛ کیلیان امباپه فوق‌ستاره رئال مادرید در دیدار امشب خروس ها از ناحیه‌کشاله‌ران مصدوم‌شد و زمین بازی رو ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30450" target="_blank">📅 01:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30449">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34b91abd7e.mp4?token=p53ytFCq85T4aJ0aeAdwWPaDhiyIhicyqdA-V5NKS2VCWfEUZ0FsHwImjsfnGcNBLCsc-8jwrKLhcLqoDSybbyKWR5utfYEoIuxj78QtCn7F7ah_0lEbUs4NPDocuwxrqcypS9dx-VKwGcVV6KnZiSjniGOPjM8JuNkP_Xh1rx5Aj6IjOP1scz1I-OuZbvJdC6vVrhsMKjMAPgYhr2JPdLtxasDlka-4r8SDP8MLGrJQ1v6rJXRy_pq7DJSnKqyUoMUvx39LKIZoWzRe9zc-8W3k4aNVGNXxZEmRDscXKVyF0MxL9Pp6cTeyivbEdJVXgvAlcHbe__Dl8oszE6X3AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34b91abd7e.mp4?token=p53ytFCq85T4aJ0aeAdwWPaDhiyIhicyqdA-V5NKS2VCWfEUZ0FsHwImjsfnGcNBLCsc-8jwrKLhcLqoDSybbyKWR5utfYEoIuxj78QtCn7F7ah_0lEbUs4NPDocuwxrqcypS9dx-VKwGcVV6KnZiSjniGOPjM8JuNkP_Xh1rx5Aj6IjOP1scz1I-OuZbvJdC6vVrhsMKjMAPgYhr2JPdLtxasDlka-4r8SDP8MLGrJQ1v6rJXRy_pq7DJSnKqyUoMUvx39LKIZoWzRe9zc-8W3k4aNVGNXxZEmRDscXKVyF0MxL9Pp6cTeyivbEdJVXgvAlcHbe__Dl8oszE6X3AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش بازیکن شماره سه تیم ملی کبدی بانوان ایران بعد این اتفاق خیلی خوبه. اول برگاش ریخت بعدش رفت ازش عذر خواهی کرد بلندش کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30449" target="_blank">📅 01:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30448">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fv3kX-mRPiB5Z73rPfgu0DgWIEAufVcVHzbNo6rMyAD8w8mM2u51G2curwJJ-BF2lw1wDzv6RZnVNC7TXuqDc5UL0qYpXdVB4jg7Qwi41qw2BIE3ghS6BVGdDg8SObxljbi7XKyaywSQ7VtcsHVz4zjmAgutrryQBpcVwneThcxHt0244q_Yi2-DW_NDpBqsOTnvAdZ3F0ydBQNgrzjtFv8yvmqZRItX139TWlt7TvMvT8waGSmax-4A4TH1twu6Ao_oFHLgl44qS4ivknv5ZerAcU5wJbfaTRiBb76tJlF4lZEaRquJIYE0f0QUU06JQjxOsVKNEGSIPeQbznzPtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛تاکیدچندین‌باره سهراب بختیاری‌زاده به مدیریت باشگاه استقلال: بین مامه تیام و فابیو آبرئو یکی رو در نقل و انتقالات نیم فصل جذب کنید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30448" target="_blank">📅 01:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30447">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0H56iuMtR3gyfp111CtVZMmA26OpVZO6jFginTl1kfMPN94dS4g6TmMkO8Bq56esVe2hEN7updjJc8SawDqekypJ52TTCGAH8iYjFQY_Nb_y6FDhtwvq3yatCOBhZxe4ftJIp71YE58ZlrRnrpu94DJNcbe2phFCx3fUnDxVXPpIht1PKe_O9pNPbVUFSsanxID030QvjHyHyfSJurF663hYDgFMRWwD0wzN4MPoVhyToqJe9-rnsCxIIvg8wp1H9Q5hl9sLw_ph2UTqw2aJS6nzTdEK23f6jKY6j_0wSWOWtYkHthJ-CST4oW9p4D0MOoZBxI8mdDiKKo20ebh7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ تکرار فینال یورو 2024 با تقابل تماشایی یاران هری‌کین و یامال در ومبلی لندن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30447" target="_blank">📅 01:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30446">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAcZNPd50o9qvfJpdL_XaNfuGvXwTLqwf9d7rve9QqdUoNET0RFY0FmT48i1TZ2XXjZelBAo0Kha_S3BLcFuEkIHEh4qZU5ADA-vB8LJTRptpUcfjM5tCMrsDhe8jwHDrpMkARRA4Gmzl8lMa3Le0FcY7pjTy9jX-XQZyyb2Wz3_5291md59feGEs1EswmKXGHjQh0ITxQtBh4bxVwodLObQ-Xi5hSYiGmT2YcWJD9994kcJC-8qoCQ7JF-kaqfCcoCL56GxchqIJ4zHSP1jOhAQIruDljlgrpn382CUoboAGWwT5roCin5Q4_M7MkxDlHaAG3-HQyfh_Z1QETToeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌ دیروز؛
برد فرانسوی‌ها و شکست ایتالیایی‌ها دراولین تجربه زیدان و بازگشت مانچینی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/30446" target="_blank">📅 01:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30444">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LOIXUPB7UJ1KRtjCWaJ-Rm4XqIOnudTLm1giMFnIec5TlLu_5V5l7ZLQ0_puclg0wn50IyS8r9gbau5phNVqxhSmHndaGtgOHMcyLllzfiBun2Nz4y-6q-93CEBquHrYUZgCbZyDbZaqs_j2kwL4KIxqyj4Z7E2fbaLg4jIVzKyZ9b4foUuKAZGV12HT56e0FziamKc220a1Jn_S2fke-rR3nH7iflwtGnmRQY64FcqFuryYOLbE8whl5nY_C_7nh2MreUYrwh1HIaycbPq7sz4vnauSRVmWjg8HFQM8zC7ZRaUO3o5dYRoQXS0GNWJo1BAMwAcMMKTbFBStgRa1MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌بازیای امشب هفته اول لیگ ملت‌های اروپا؛ مانچینی با شکست استارت زد؛ زیدان با برد. سوئد با درخشش گیوکرش و ایساک سه امتیاز رو گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/30444" target="_blank">📅 00:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30443">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xx49y0Hj4_yc1BSn4KnWliVI5qrdmHwO67VyDXhiXkTbXb4PTA1PMMBaQeSMJ0fI8jsvCEH3WXnwGQpwoI39lnqzhK-wd9MxGxHvz4rxc1XZq7jZqsVDiyp-JHRWWgtjFDm8uCtrxrRbvbFSJf05mRvpjkfbn91K46SpAcsGjrwna4EUMPrFGcbVVDF1RBczaSHLAPGyyUDRZTWy8xoVGUZyshMa1027q3eLIr8FVN8Wt7IRLkYChKkqBGNC0ZCIeCCfR_ScMLWgJb6eJ6aFGG7VzwI5eD6tpKT3ZVBGC2cpMoycqdcG0jnHGJhWQbw_NvTsgZqHrnOnuVo3jnaZxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز؛ ازبازگشت زیدان به عرصه مربیگری تا نبردخانگی لاجوردی‌پوشان با یاران کوین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/30443" target="_blank">📅 00:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30442">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XL0p0j7RX-WJSqmzzhky2bOZc4XHPfLqm7FdIELFOYOL8pCF0pQ32qrGqoNqWi6i2CutcNyoGf_nEi2iVGyqPA37uXTh5cKnu9C8MGRz3SPB9p3Mu4rbDGVm5QDjD91gXPOXEs0FVq2erPoskusbXPg0f73ZxHNzW9C6bAIOViKQyUuFTyXlFquwJCR_N5IiZN_C3SGL3fgtyLeJ-dIOb_n_ZEfG-t1wvlhuFIQh2CR65FhE_ETjuEPJDaHiUsxjWY55zqkFZyysVWIFQvK8XCvo8ujgs2kCOtpPMcduTOzmQd6-nYNvv24RE-Hpe-I2-45op6OIDaviowFaCa_ZEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ قرارداد مامه تیام با تیم چوروم اسپور ترکیه تا پایان فصل جاریه اما هر باشگاهی که او رو میخواهد با پرداخت 300 هزار دلار میتواند رضایت نامه این بازیکن رو از باشگاه ترکیه‌ای دریافت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/30442" target="_blank">📅 00:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30441">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0-dEZU1RYH4-870Kf278i3JTzw295WgUU0iYVt4sqf_-J75jm5MiABWEAKwvUzU6NfiaiLqBIs7WetlVFEevjSFKCgrOvO6a4Sg6z32k-yA24_pfK4fUGu0Z531qtRdmCkgujbp8ar7cbwY5CPnRIkIWnfMOMnIoMNspOV06z5AkAtRYY78sAQo0uRoI7Rr2QNm_9aYAMGyj68vY9WBVDH_SLllDfDtuEZw3Li4Y48C5AiXJbiSgcYTQscwwtWa9DxEVrVsD78_z714QEENMtPLZG-oEez5EMwfizreMpsJUKAb2c64gbYPQhAOiuk_OOIPmyWVghlEDLKiH-AGjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج نهایی و جدول رده بندی رقابت های لیگ برتر بانوان در پایان مسابقات هفته دوم رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30441" target="_blank">📅 23:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30440">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWQWuscvYEtYt2ABhSL8xfB4FsQ4Da3UrN3cZ_7NfXWjJ-UO-oWMYT-FE-XWOuUoqmkTq5PS9OnRMUs67AtnHhN2aIyEZaT6ABSlrP-MNPldwe4E6X2X1-HB-H2DzP_JnSlGjOYxo9ctLMFIxScinkto2JN_ByGHxbdZkia4C1HhWE7FG3BOw0wVYzJuZYKTsu1O3wr5PmW_eu5jcqezyzN9XM1d72GTwQb_E2_jWQoWEDYQsZzaO8QAASHSh-YeEKy4T2xjgI1f0s-rfVME682kMcqjj5qBzCyZ5LVTpg2vVKSoIOPz-jd2PsEUygzth_Vf9UfsdOZ7AYLwWHyOew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت مصدومان پر تعداد باشگاه رئال مادرید درفصل‌جدید؛ فده والورده و ابراهیم کوناته به جمع مصدومان پرشمار کهکشانی‌ها اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30440" target="_blank">📅 23:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30439">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔵
👤
مهدی توتونچی مجری شبکه ورزش خطاب به حسین گودرزی مدافع‌چپ تیم استقلال: مطمئنی استقلالی هستی؟ فردا روزی مثل جلالی نری داخل یه‌برنامه دیگه بگی نه من نگفتم استقلالی هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30439" target="_blank">📅 23:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30438">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JY4mfJSxU-WknEnJVxPf80_BcMVWz4mxW5HXUzQXYzvibavVyMUkQwkbggsT2QtLfFkQW__-kWK-OkANnjyCmj8NRO3OvI1zYYaF2PtiBPZ4L8S5HAnwijcle60yT1bQxI7j2J8Nnljut3dxjl9MHmFX1U41PyQlyvMvb_xBD3HDhFAP0VxtnbXSXslVaXop94Qy4lso-rHz-QNGARO9dbshitIr29QA7qNdJj3_N0mq2m_2NRjToO4aywVsM2YiSWBNryqYYYRFuk7YMRdVXUE9VtM1ylG1QIpfebBokSjPGvYlu7a_irgfRpMzFFaw_GTkxowlgDVL0jzQ7tR2Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شاگردان مهدی‌تارتار درپرسپولیس امروز عصر در دیداری دوستانه یک‌برصفربازی رو به چادرملو واگذار کرد. علیپور بدلیل مصدومیت دراین‌بازی غایب بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30438" target="_blank">📅 22:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30437">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLa_lv8TNsVTGuJXj5kJ5j9MRgPm1JqhDySmiwKKndf2YIk31jbEn0URuAk75CQyOY9Sw0yBOqtYFX0wQKw1zieICki2EIPPnYrzA4k3NhohqyGFMJGqPqrLAxTg33S3vPzYNhij9ZnGhzr9JojPAqGLO3gELuikqR7zz2G-0vVyh4_5OHRyRdLHjCjeTlKKQP9Q5yoED_N7IJ8DMTgXfDC9b3eQOCC9v86069fMlNRHf1One2I2rgfSuMZc7Q1BOTJqND5JRvGvaHEk-LFPlzORq4hpngBueab2rTal4BiTHW8kLwLjMgfDUQQSJcJHYlJaLf9FTK2_epFvHDRd8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🇳🇴
#تکمیلی؛ باشگاه منچسترسیتی انگلیس برای‌فروش ارلینگ‌هالند ستاره‌نروژی 26 ساله خود در تابستان سال‌آینده 200 میلیون یورو میخواهد. از بین دوباشگاه بارسلونا و رئال مادرید هرکدوم این مبلغ رو پرداخت کنند بند فسخ هالند فعال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30437" target="_blank">📅 22:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30435">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K0vkx4Kl5-drBOCuFK_57SjXv01O31dCEIbesAzuSl3vcAzs_SPlubU6Nc-pgUnyjtyyFcDhOxFoCZe3xxTNrThs6KNHGnVym5NLUBwzyFlYnM6XtvC67_WVyCisWjs6oq6Xua3tMDrl7qMIsDA4spqcGdZrOFqwaygh2RYp0ZHidaGcv-vR80zEBfp5QdkD9vvTNlj2wutbSKuP0-OlYE0fNPKRP_1Yg9ydBqXxtHSB5UbQ4cBqqI6T1SW7RIbz7dzjBuStyfZGshY7SVljgRK2W7vtfHlR3X6Arn0nny1WmDlsAchxIj1neMeB2SedpNzeGwhwA5uss1lQucvjyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FdBvqF63wQq-7jI-viCxRvnKkuF-ugTTX33sJY1XaZlQ4pFlKquwmWldAqFIbRD8_ZTRLk03AjY0KcFeDSYTnSOXcGDmNTCOXmWRH1ipoQk0WDEf4l_tU2rHW0JaJe4gQcx9CmPiAU3BMOH3k0QLBN8uLMHUKSiXXtvg57WEP7wzz5raUZGq7j9SeOE7JpqK2DKo86CFXsg3BX5TyoYg1vTvWFtIeRoeH1hS2GFSQAqz7-DOBLhRPzglf2Uh9AbLab1OE0QN6YL-druYFAiHaa60SV-1Q6dHWk8Stu0Ha4rNjeeT9NGBZsHpmMuPwrj6xziin_XbTfc6D4lOUNR43Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
جدول برترین گلزنان تاریخ؛
ارلینگ هالند ستاره 26 ساله منچسترسیتی‌که تا کنون موفق به زدن 370 گل شده گفته که هدفم اینه تا سن 33 سالگی به رکورد هزار گل زده در کل دوران حرفه‌ایم برسم. در حال حاضر کریس رونالدو نزدیک ترین به رکورد هزار گل زده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30435" target="_blank">📅 21:52 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30434">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21cf909039.mp4?token=u0YfQIzGmda7JFtSqShUMGuzSk2WxBAw5qPpa747320WgwPef4LoJoH3fpPc6-CAJon0owWM35ImrwThQZtbgHVbyGQ6vTbmsqE-FlacS6x5M_nD9WgE-tHOum-FgdizZFRcCI5Qe2r4vbQrLuIPTG5XivFmlNErqcK5IJGH-_R8W5xP_6uU-ZZvJBo_2SiizgtFClp8GAQOkrOdOZ3l0wMO2qrdru7cf8N6V_-ga1Rt4DIb3RGoC_EqEEpCDSXXRlU8_QNScP_194bvBn2cHQ34K1S98KgJUG0Yat-TXoG3vLDizKC2rFlOoXRBpzgs4AvU1tsqCXFvpWuLYdqZIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21cf909039.mp4?token=u0YfQIzGmda7JFtSqShUMGuzSk2WxBAw5qPpa747320WgwPef4LoJoH3fpPc6-CAJon0owWM35ImrwThQZtbgHVbyGQ6vTbmsqE-FlacS6x5M_nD9WgE-tHOum-FgdizZFRcCI5Qe2r4vbQrLuIPTG5XivFmlNErqcK5IJGH-_R8W5xP_6uU-ZZvJBo_2SiizgtFClp8GAQOkrOdOZ3l0wMO2qrdru7cf8N6V_-ga1Rt4DIb3RGoC_EqEEpCDSXXRlU8_QNScP_194bvBn2cHQ34K1S98KgJUG0Yat-TXoG3vLDizKC2rFlOoXRBpzgs4AvU1tsqCXFvpWuLYdqZIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقاد تند جواد خیابانی در برنامه زنده برجام از فدراسیون‌فوتبال و کادرفنی تیم امید بعداز شکست تحقیر آمیز مقابل کره شمالی در بازی‌های آسیایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30434" target="_blank">📅 21:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30433">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGvBcyoSZA7V3pwLW-g6Ya5XSrBdTZMkvO28Z8hLLCxE14hzWWj0nw9tlSk4l8hJY509JoF5QILbonh72ZyvKxa8jXlIlUSV1RynqB3Zm5-3Lr5d_RtTSKtqepohjkFtolpq4RcTl5y2jGZLibrTIt_q_FtMvG6N1uRWmskAujj3BsgKARaWZTlGyKWkJusU0JFTSWIhYLD4hOBWN-xGRyP1LOTk9fdz490vVA13h3B6LM15Gk7s2Wb4eik6V5LdQui8ytPMws-TeLfiTg4ukGXMaKIvMBKmU1C8zfMoepbf2_fUaicWKcfNuFOh9jGNPc8AL-tsauvn5y1XA6r6Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
به‌مناسبت فصل جدید لیگ‌ملت‌های‌اروپا؛ نگاهی بیندازیم به پر افتخارترین تیم‌های این رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30433" target="_blank">📅 21:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30432">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KygFtUltFs1r4jMTX4aWThbiYByyddQXcqUmkesTnjsgG8YJ14hjSuDxLCHb9geZGQBd3kWWwdzDEJmLm4AVb9gpyQUCZxl91mphQzSvn6c6qeEnrdTNiMTrqmgPHCiLw44mp2jneMN2yGVTU0IAzZ-B0j9-93c_QqCICkTpsy4_8yIrfvhLr0BjHOHfTlkrwaKzyDEHJZzxCqcEEl_AemWzPy6rB3Q1CMdHqPJvnwsotIwcDZEXM_yYrzc-Mfz0BQsXa_GrrYKU-KdCA75N2F_w3Qj7AW-KbY7zD8aXYIXocmiWyebs4XrB7mvT2t4TjJXr8GOtAKnkGWlR_Xpa1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
دو لیست‌متفاوت از تیم‌ملی؛ لیست محبوب امیر قلعه نویی
🆚
لیست‌سیاه‌امیر قلعه‌نویی رو میبینید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30432" target="_blank">📅 21:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30430">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/537ed2cb9e.mp4?token=M5RHVF5JSE5w6JCBzt2GViM1KwTza11cacifSBYLjqgHd3GlMws6fpmHaEbHu5IPv-_3XNLvZHCuAklc8fkLtguZ4kZIYGZ6LFJMxnk2a1coTDICPg7cl8mvCn6xaj2PsDP-MseyeSmgE_SpLDUuj1jkeQ5PBmT1sPISfIYNk9BQL1D8BcVYX32iEMq4vs74a_kVYrqgwduk7olAq_MVyMreraWc3N6JIoXOnuX-ICMRUNB_DeIowqtTd0ZUZhp_zfujFRcT0ME-_PS1jzoAlfVrqChsu1tvEet-g7VroDrsZ0FAFzVNuBXrldDTRvwVHuTEc5hY6LX4PdI0IqVeNyFncemT-Wx3Fim257RTBsWSlsfxLHbS30EvreJieyhgia-KO9iWWR9_AwjEnaRqrgdxFwowqLETvr5wSLG0nRa3SS5owDatu3aZ-twgj7JAvu4_FsFZRGG-BB_NDXa-re_3g2OXzGiqqttlBFFITQrxyjC5Pbq159U5VXIgenkE3wNfetzoSAZ0WRjI5JgjSe4qr7Vq4U323qceW68H2P343xyoTb2obJNAsj0bCAFvoXm_i5YxcF6wI2ZMBxuMMPoBYIICkcxk7Q9wlowq-Lng1lGMZ-MzdEkZRY5Y-1-qFYiRoj6_4aAdQPMKomC2xMpPqDsekObyJpyctSR7HX4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/537ed2cb9e.mp4?token=M5RHVF5JSE5w6JCBzt2GViM1KwTza11cacifSBYLjqgHd3GlMws6fpmHaEbHu5IPv-_3XNLvZHCuAklc8fkLtguZ4kZIYGZ6LFJMxnk2a1coTDICPg7cl8mvCn6xaj2PsDP-MseyeSmgE_SpLDUuj1jkeQ5PBmT1sPISfIYNk9BQL1D8BcVYX32iEMq4vs74a_kVYrqgwduk7olAq_MVyMreraWc3N6JIoXOnuX-ICMRUNB_DeIowqtTd0ZUZhp_zfujFRcT0ME-_PS1jzoAlfVrqChsu1tvEet-g7VroDrsZ0FAFzVNuBXrldDTRvwVHuTEc5hY6LX4PdI0IqVeNyFncemT-Wx3Fim257RTBsWSlsfxLHbS30EvreJieyhgia-KO9iWWR9_AwjEnaRqrgdxFwowqLETvr5wSLG0nRa3SS5owDatu3aZ-twgj7JAvu4_FsFZRGG-BB_NDXa-re_3g2OXzGiqqttlBFFITQrxyjC5Pbq159U5VXIgenkE3wNfetzoSAZ0WRjI5JgjSe4qr7Vq4U323qceW68H2P343xyoTb2obJNAsj0bCAFvoXm_i5YxcF6wI2ZMBxuMMPoBYIICkcxk7Q9wlowq-Lng1lGMZ-MzdEkZRY5Y-1-qFYiRoj6_4aAdQPMKomC2xMpPqDsekObyJpyctSR7HX4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پارادوکس‌شبانه‌ابوالفضل‌جلالی‌روی آنتن زنده: من هیییچ جایی نگفتم که از بچگی استقلالی بودم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30430" target="_blank">📅 20:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30429">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NI3zI7nHDr3SdL16NOhM6-m5c1gp7LyNCCdOsfLhML0ttVyDnsGr7nYTpzd4raErfdNrdyzTE61CR5pgxhtTWjPny6v_JqmaUhMidb-g5xmFdjPTf9tl8uyJfOLKUF0C-S0Hghlao0nBC8wUvVezVKzXNQ4daA9LYloIuJI7gKVcaPhC0RIBuhbXLWeq-WErjVhAh3JANIh3VDjGldLbgHd_iawx70eYknY-7kEkpM1rZQR2C2EqjeITSej2m-jcEUfN7ssJZ71EXZLGe8ACJ9rHW_aH8QqaltjFmX6i_Urt5suvnKIneqv3oqvE278RWac4Tjf2yhhkDGPbg20GzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ‌برتر بانوان؛ آتش بازی پرسپولیس مقابل قوی‌های سپید انزالی و شکست آبی پوشان پایتخت مقابل خاتونی‌ها در ایستگاه دوم لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30429" target="_blank">📅 20:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30428">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkppN8UzKPzK7VC93UL1_im-4BOXQVMlOc1hCNlyd-XhcgjXNpSEmkeh6B0u5oMWhgDfcQjTbYi1T57yBT7rctjHJpUwepbGet60RVeysYup4xtUrzMHhxseO3qjA-_lwsgFLQBopRGgnNEGVOZVGv2oE0ddME-pbdzU16Uboe65O6gp7W-dWPtGM3DzHfWqidHEgJ_uJ5NEqXvB1_IQZoPuYqCVUusP6Sx1nPMWTVeeGAdyIfCt4d39tzCAYyPuiylMLZl82oaOyWDIhk-Zj4CE6LaO93ml1T2N665EiZCOQjg7l3QTOUw3_bLC0B-eS4hs1jv8S5t-mx2ZNzYkOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بااعلام کادرپزشکی باشگاه استقلال؛ حبیب فرعباسی دروازه بان مصدوم آبی‌ ها به دیدار شانزده مهر با تراکتور در هفته هشتم لیگ برتر خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/30428" target="_blank">📅 19:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30427">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdFOUiN9fwDbPzI_6kqhWFEb57IQNoknTZFGWHnbBB16e8xlKpMB-iN7JiJrc5ss7IBrpYkr9Ry9WbJuL_opLBEog5yszlTkd6MsJ36V97Ag46u47YZfpqr_R1oGq10yKxrjFBapRH4y8HNghpl8vbSdACmBaYwA-dWaXLSrhBq8-_TUx00p0zZdmf5NUBkX5ZB4RfJFk7qs2kNDiWCIuvsBRQ9NOIfOyvUuNGK0UmnPiwmQfCZQhAWvevXEBGGjsPGTg7jJ1fzmetZfNShEh8wqZpis2svWNBLlOUs78vKjPCS0qkis_Pg2naAyDF1SWhuoC44hnbF230-HN-OrsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
عشق و حال مهدی قایدی ستاره ملی پوش النصر امارات با پسر کوچولوش میلانِ عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/30427" target="_blank">📅 19:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30426">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYTLCCg78UTEXmuPy37LjKJlBM7rQOYIDbw4nu773vdBHGm_81pRNMsTWwlbHGxwk67XI3ydTroYFimLP-MWEQ8iiW9HCOYUTYIqx1lYdM5B0WcHy2vK8xxob97_I0CL3JfvpFKjIISfUBEm-rdmaurmTyBGfl_VL6k9zNTnxwUVNfo2nVy17mSLSw0q5In9rBqMfc9h8jggfm1lRMwbke_sw_iLTD_xmzUgi7ONXHsS-SHpft3IJrK0AWz04dMw56vn_fiFBstTfeER9M26QvhH--Ln7hXWsfhYeCyHR4Ggx_nG0HFf3_BMgPu3-GwPdEO7NCyuiE7nCgohTvRUgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ظاهر جدید وین رونی اسطوره باشگاه منچستر یونایتد با کم‌کردن 40 کیلو از وزنش در تنها دو سال. درکنار کاهش وزن رونی اخیرا یک عمل رینوپلاستی "عمل بینی" انجام داده که باعث شده همچون قبل خروپف نکنه و راحت کنار خانومش بخوابه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/30426" target="_blank">📅 18:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30425">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eG-WljYdDu01TEmwKpXu0_ek2akjj_x_hnISIGtXGOVpIuSGSjeRZOszuofnn9s33tt7CjB1YR0csWyD_k6PZ1ezIVFNtd9_yQ09HfvWhuk9oiA_8YVI3b-li2NKkCliPoUTG9y24C3ytOVwUEl85tHGnL8tFhTymBk65icXua0BNJDaUOcRIqnveh-iU9o1zJT28U7ZEfapcTk2QsPlaAwhaTRO729SZZAXVCPtgjebyr8bBxGbYkrtp1TC8AVxi7wZwmfMoB__Uej4mNxhqMkPXP3z6zEf_MKhIjJBxOXb2TKGNSeN4fiIUQkZgmoUOxWsX6FOEF1uuqRuQ0l9nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
👤
بعداز تمدید قرارداد اوستون اورونوف؛ باشگاه‌پرسپولیس قرارداد پیام نیازمند رو هم 3 ساله تمدیدخواهدکرد. تمام توافقات لازم انجام شده است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/30425" target="_blank">📅 18:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30424">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ua9QFzMFw4QPvbUNk7BNHAdneJ8rhkk4LZRhVWIAEyJS_-UzVLyDXoWJ7QkcdppX3Lk5qHilOHPwRATBvf_UnRGurxjwPCCBtEXMSJsrs3L_0GBbZJP6pG8GH6yvy0zsQPdTRPXkTuZ8dleqFlHpt2nbdSZ3n00pNnM8RuCH30Qo9EXKo_qHvYxjyJKgrLUFONAC2sQN3Fr53GT22VnaYSqDwR96cRS2qUs80mI7isakSd3FfSxhznTEhYB1de598JH0cUe49TL63yWMpyKmB_cBOAXPO9WOcLxCtgPPZdbWwNz9DGZogTtleGyUMceuF6Ch5-Q0CQzQM1wBTOBiUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ‌برتر بانوان؛
آتش بازی پرسپولیس مقابل قوی‌های سپید انزالی و شکست آبی پوشان پایتخت مقابل خاتونی‌ها در ایستگاه دوم لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/30424" target="_blank">📅 18:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30423">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-ax5TBpzgbVAvCIMPh3FVQ5ThNr5NbYtAsRyk14scwT67E_XVxIww6SnDTjd0p02GPD1yJcKWzdv_z4KWJF2G4JWDcVSNi_BKi19Ai07RrS20bXfwcR0IZMHw50kkQD5Rf2osATsHxclPfhUPiqTMNMofSSBoCkMTvLtz71Ulv0dZ4uQts-TLLcJdn4fQ0V-zZsX6pkFQjVOlW3oM6bSBIBQhFUr-Btsrx3Ut05oZJ1znAkwAPkHxFl506UFd7gh7LBVDEUcY6Y0xchMorvl1M3YLYF6gLo4xh5iwVLp118e_n2wqair1Eew9WdkIGyytCB706sdu8C62XwJBLeww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
پرسپولیس دربازی‌دوستانه امروز برابر تیم چادرملو با این ترکیب بازی میکنه: امیررضا رفیعی، پویا پورعلی، امیرحسین طاهری، علیرضا همایی‌ فر، میرشفیعیان، مجید عیدی، محمد خدابنده‌لو، یاسین سلمانی، محمدحسین‌صادقی،تیوی‌بیفوما و سرگیف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/30423" target="_blank">📅 18:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30422">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmUuAmMDifq2HoKf2uGsYmnms-w8APOOpRbYrvCd7eo7McdX4TCbQsOOMDw4AhiL4hne1pjB84stdl3p6MxO6ieg0p-Zu9ZU2P9Q0Wt34XFFkVnSFLtisUp9ov1GMt3NmmDPVJoxFN4G4EW41phZCKnHwb3QKXKK7l-mu-SLX9aBAhBsuYzoRDgWKeDMYEtwFt-sHFJP66z-vC9rSoGuK2Q9Tp7Hr8CgntWdhjO8vp_xH7iWLY80SkjobsgrZp5c3U8C7sbHYhrlf_f1ukdv1pOunr_UKg4jjxFxsp_zQih2c9CECcmsgjnX8hOIbioDncVtdCKBS0zGKhCXWyDt9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیوید اورنشتاین: من سیتی درتمامی ۱۱۵ مورد از اتهامات لیگ مربوط به‌تخلفات مالی، به جز فقط یکی، مجرم شناخته شد...! هنوز درمورد مجازات‌ها تصمیمی گرفته نشده و تمامی تنبیهات همچنان روی میزه. این مجازات‌ها میتونه شامل جریمه‌ های نقدی، کسر امتیاز یا حتی اخراج از…</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/30422" target="_blank">📅 17:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30421">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAXuDlPWIXqpU_4z-ZNi2PMy8OIKlyWMoOy5285ByyaQ1J9FR_bw0nY3zc0upd-I1eECwM8YH04qm80ymQcY2SAjQf-aJ0WxuBfFd-GylVDF2EEQQ0W-l_SX3srpuSkoBIyb3ykig-1O_TQ7VAm_as4ltNIpPh-QgqhA62sMEmw6qNnGWVoq32LHfEus1IouZ0SwOXKaypKwlYTnTDFpEaPqyl1VRXSPAq7LJ7niLjjfNvXGW8JeeDg5bgfHbqSCxCrw-NyhwYOGcCErCfYIQhe1XhMke8icTZfflBaTfyJ_-kajP8TKsx59lxblby6X2VsccsGxQYjOJVXToJWzTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیوید اورنشتاین:
من سیتی درتمامی ۱۱۵ مورد از اتهامات لیگ مربوط به‌تخلفات مالی، به جز فقط یکی، مجرم شناخته شد...!
هنوز درمورد مجازات‌ها تصمیمی گرفته نشده و تمامی تنبیهات همچنان روی میزه. این مجازات‌ها میتونه شامل جریمه‌ های نقدی، کسر امتیاز یا حتی اخراج از رقابت‌های لیگ باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/30421" target="_blank">📅 17:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30420">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BzE4Ty_h509TgdNq8jd7sJBGqax9vGXZqvicm6vhTnDLuYO-FBS86Dvvn1aDmt6WUhEMS9nynezhWcHzeVaADIISs1PqZtQr2T3Srgsc61ceCo2c9xbhNYNqMfRCkM7fWofs-KFlBqH0vCcP5L-P5CVzcmbn7DIat4P9IFUEkGwrb7R9L3k1-g04cnYAVOcibxxD5g-UvfONbKbWERG4S7sR0rOhjQpCloT7KFG7kiG-o0YdX3-Wm2IpFtNkmRDHwgSi-Zkx3HKYHGRxuAjuc_zj06fH5LDxvJS3OmT3U8ZvYv5chQwl711ubd3cZ9koAEPhjxGR2b6IBDhpf6J5Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
پرسپولیس دربازی‌دوستانه امروز برابر تیم چادرملو با این ترکیب بازی میکنه:
امیررضا رفیعی، پویا پورعلی، امیرحسین طاهری، علیرضا همایی‌ فر، میرشفیعیان، مجید عیدی، محمد خدابنده‌لو، یاسین سلمانی، محمدحسین‌صادقی،تیوی‌بیفوما و سرگیف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/30420" target="_blank">📅 17:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30419">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fg0ai8lxEcVfAuFkFkzofJAaiCybSXT1dk78YikFbVQYilEIEj6pPFSQDelw313GU9DYbZOOHN5Fsmd4J76LF3aScDCnm91ak46GQ4RJLloQWPGyD3sahppMfMElYr5dInshKBHtxsB2SycR9mQN8TkRHWnHmtDEPc4IY6X2-uxsd7fo_Gstc_kRS2njrMAjTkHZI_8M4PcjMpmn5SkriBnS6JCk9dpnG0rMm5Pioug-Cxb30-3skRWzaLDRi3f0s3UqTXo_HX33uDD5-yZtKgAFK63MdBPGkuIxzps5fRi6Us0qho3wjtDrYU_iMM9pgSLjER1UXcKd3MlvVHixSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تاثیر نادر محمدی بر فوتبال روسیه؛ گل عجیب با پرتاب اوتِ آکروباتیک! الکساندر کوزمین، مهاجم بالتیکا، بایک‌پرتاب اوت همراه با پشتک حرکتی شبیه نادر محمدی انجام داد و توپ وارد دروازه روتور شد. دروازه‌بان روتور نیز بالمس‌توپ در ثبت این گل نقش داشت؛ اگر توپ بدون…</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/30419" target="_blank">📅 17:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30418">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e998b3c1.mp4?token=vhEwB_3pWpuDKhRk_KPCXBdL9dSSZ2Ki4_qCFNbmvBmnTIGaLHgGycTo4LccnqkSlPxea_boM-DVQCwU7hezxolCE1sSxIlxL35NeS4oDKit_dAkYt_aPUzQxrYXQANoDblAJxvuWWTPx4M4uWanC-rubWV_ki5piaxYzSiEJZOS9cRao8ZezNh9y3xuS-whmTWG4H95lRSZ5xrrI8ND1Wb1Y_Bo5k18-TwX-JW5KpoBGgiT22Id9aKQcM6CzZJp_RcGdIpFKxapVsnEj73hICoNE0S-YaLbMdgcFLwGo23dfYTH2SauIQhEICdlacQ2PDAzNlylIOv8GwrQLzoMVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e998b3c1.mp4?token=vhEwB_3pWpuDKhRk_KPCXBdL9dSSZ2Ki4_qCFNbmvBmnTIGaLHgGycTo4LccnqkSlPxea_boM-DVQCwU7hezxolCE1sSxIlxL35NeS4oDKit_dAkYt_aPUzQxrYXQANoDblAJxvuWWTPx4M4uWanC-rubWV_ki5piaxYzSiEJZOS9cRao8ZezNh9y3xuS-whmTWG4H95lRSZ5xrrI8ND1Wb1Y_Bo5k18-TwX-JW5KpoBGgiT22Id9aKQcM6CzZJp_RcGdIpFKxapVsnEj73hICoNE0S-YaLbMdgcFLwGo23dfYTH2SauIQhEICdlacQ2PDAzNlylIOv8GwrQLzoMVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
بعد درخشش نادر محمدی درلیگ روسیه با پرتاب اوت‌هاش؛ حالا تو تمرین‌ماخاچ‌قلعه کادر فنی یه توپ دست محمد جواد حسین نژاد دادن و میگن هرچقدر میتونی پرتابش کن به سبک نادر محمدی. انگار فکر میکنن همه ایرانی پرتاب دستشون زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/30418" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30417">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65e769a610.mp4?token=ER_E8EB-ZLWca804DJZNjmDmXruJf_RM7I5Sr10N5QE3WKALcSMSOTadOk4Ygm_Ai5l41ujEfCGKf5wtmPzsJ8MgUGHoGin5vn9nkEsu6LY0NEwpMbiUU9k_7TjORUPWZx51oAYIiRqN2h9Yzo359pyaVf64cQFqzDxzWRSanKz41MYiA9WqGSvhRTwmlGwBPu2cEPDcokFZeritFgCeO-74E_Cfi-du40BcSZv3xIGb7KscHASzXk6jl5npUAFUXCZLmSqaTDIJVu-ZPWPPNbEnx0hcQVXBWFgeE2oKmfQ6fUGtrWbwt1MIfHgEwXbUE8lKLoJzp_jASH2Wo5Qk_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65e769a610.mp4?token=ER_E8EB-ZLWca804DJZNjmDmXruJf_RM7I5Sr10N5QE3WKALcSMSOTadOk4Ygm_Ai5l41ujEfCGKf5wtmPzsJ8MgUGHoGin5vn9nkEsu6LY0NEwpMbiUU9k_7TjORUPWZx51oAYIiRqN2h9Yzo359pyaVf64cQFqzDxzWRSanKz41MYiA9WqGSvhRTwmlGwBPu2cEPDcokFZeritFgCeO-74E_Cfi-du40BcSZv3xIGb7KscHASzXk6jl5npUAFUXCZLmSqaTDIJVu-ZPWPPNbEnx0hcQVXBWFgeE2oKmfQ6fUGtrWbwt1MIfHgEwXbUE8lKLoJzp_jASH2Wo5Qk_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
ساعت13:30 تیم‌ملی‌برزیلِ کارلو آنچلوتی با این ترکیب در دیداری دوستانه به مصاف استرالیا میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/30417" target="_blank">📅 15:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30415">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PPROe2N6ccxWIgBptmR3SHt5zJS6W5j31Vf_WIoSGd1YR_lLfz2Hgj0PKaLeASnrFZqrcDmw-rOl6MTI-Zx1gBM6LQRyTY9EEglRDIpGt73CeG8-w_obPoO9Q39ficNyZAh8cUlURMw8P6YwhimG9t3nLYf5FgiAiQSEe_pQOgAUdS4ozCqXaG6sSAFZJPF1gGEijZUPpr9NwWWDq5hxdrlxHXlBDxgGD5c-BBxdjaSTmgUp58DNQdks9mYr1jPlRaV7tQILOFnbfXwR_icdqCw2qszvdVT6OVVGyYwOIaI0WBCd_pgawFTXRWyJ5Q6v2K6p4LR7C84WtFS-YZIamA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YjascPSojNDWpHZYOKWXBdeMkSucVtC5snjIFw3XrZp1pskfvF44MT-1HJ8YRucfNMFBfXY7LBD5IXyNmuo0k1xlRYFJze2EtC_FgxZrAuJiqyqcB9u-CYc90uxpiPSTPJTaieScn17vfbwmmxTudgUBO1-ycaR2jTIDLlTAjP5QfDsKrlBVXDcbgRLDfBAcgPZ4TlWsz6oX01cn50megqfqTkpXpqJiEvf_eywsBBOk55pGfmwsqE1Qp96Ou_i-cgjPrnRK6puBr7ZrNeG7f7sOiF5dNS95n50EsEghAekLry6Nv7HCumEGcGabJjRdaskPYzdR9CGBrO0qRAfyrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
انتقال سهمیه بنزین به کارت بانکی از فردا؛ نحو اتصال کارت سوخت به کارت بانکی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/30415" target="_blank">📅 15:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30414">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df9587608d.mp4?token=i4D2gRNob8hQMfEULohA9K9TJ0i_gtlJrb4CpVll9hvq7EwHGH37-rS1e9uD2ezUX2Y0M8PAH5Ow2poDjrecO5YcJn_FbkqBI4T9cF4yV8MBaBGtswEyaMgG78vaqy1ybjOI1RAHBc_zw4XB7_Rwo_39yga907OAMdqWv8TqXsegxdojheHYIJX1WHjJOV_2bC-BjpLa9Z6NIJ4Xc9e8MXh0Sw2dxH49-yzPl_vlYhCKl1RqG_yJ9ERxzPpxqtBHpP1khRgxeij6BntMk6666Qg4f8GD7stVK1nS6CPmwI7ghCjAEzycNv8nRptmC1STEdAMq7zI3KyC_EDHQRImJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df9587608d.mp4?token=i4D2gRNob8hQMfEULohA9K9TJ0i_gtlJrb4CpVll9hvq7EwHGH37-rS1e9uD2ezUX2Y0M8PAH5Ow2poDjrecO5YcJn_FbkqBI4T9cF4yV8MBaBGtswEyaMgG78vaqy1ybjOI1RAHBc_zw4XB7_Rwo_39yga907OAMdqWv8TqXsegxdojheHYIJX1WHjJOV_2bC-BjpLa9Z6NIJ4Xc9e8MXh0Sw2dxH49-yzPl_vlYhCKl1RqG_yJ9ERxzPpxqtBHpP1khRgxeij6BntMk6666Qg4f8GD7stVK1nS6CPmwI7ghCjAEzycNv8nRptmC1STEdAMq7zI3KyC_EDHQRImJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقاد تند جواد خیابانی در برنامه زنده برجام از فدراسیون‌فوتبال و کادرفنی تیم امید بعداز شکست تحقیر آمیز مقابل کره شمالی در بازی‌های آسیایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30414" target="_blank">📅 15:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30413">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6521c21a5e.mp4?token=PGC2A3JFQEyGvSkEV5mcYTizomx4L3QiKgbEO8qA2-aZQjimacsS2lelU2CXn0_zdbCWdBxSaaqvSJHjRFhHRWHkI2K-JIZ7GCu7wqFuVW8t-6CRf8AsMOA68hirbUm2HNYuvgkGfc72XqLeL41uMtb4Hfj_4Nq48iTEpxaI_5QrapdWir1dRDuJdL5rTK5JaGNEitljd9LGOUpdkjaDCy4q-ddF84vsHfIfuQh5-btTinm-nqx-2q-OtIKVLsvW9oZUi6mRuvJzw-R4plD3Zy5-_Xgs_exxxteXa4rLmqj6FXJxvXHBkjdXjFWxNi5K3LJhjDBCfwkmPwOxWmrndqlm5d0EKatXwsOyMXqhB8LXGc5eEoFtIkTt5Z7vUD1DsLDTKEEwOHqT3KDjAG2uJDWFWdWWAG_jD-oDYN6_0fIRZaOhD0jAVDc8vr6sREx7zsqCuyDelFh8vrjK-uEnlOejir8_YSWLSPNDO6fpZQ6gqoacXv7VqfpIgBrqRcKSgZ2usM5eqA-UGdzNyw9F0WaNfWOVn4D3P09jOJhsSWkP_9iDRlOWnw9BrqRHfoqlIZefW6pNQH5U0k6wqtrqFrDXdAvWkxTrEG2cbLcGIt0wv3F3De04qRi_2rYocd_w57PpHfKwVoxPy4CgyBqB3lFcc0tPg6n1qU0rRMR-jhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6521c21a5e.mp4?token=PGC2A3JFQEyGvSkEV5mcYTizomx4L3QiKgbEO8qA2-aZQjimacsS2lelU2CXn0_zdbCWdBxSaaqvSJHjRFhHRWHkI2K-JIZ7GCu7wqFuVW8t-6CRf8AsMOA68hirbUm2HNYuvgkGfc72XqLeL41uMtb4Hfj_4Nq48iTEpxaI_5QrapdWir1dRDuJdL5rTK5JaGNEitljd9LGOUpdkjaDCy4q-ddF84vsHfIfuQh5-btTinm-nqx-2q-OtIKVLsvW9oZUi6mRuvJzw-R4plD3Zy5-_Xgs_exxxteXa4rLmqj6FXJxvXHBkjdXjFWxNi5K3LJhjDBCfwkmPwOxWmrndqlm5d0EKatXwsOyMXqhB8LXGc5eEoFtIkTt5Z7vUD1DsLDTKEEwOHqT3KDjAG2uJDWFWdWWAG_jD-oDYN6_0fIRZaOhD0jAVDc8vr6sREx7zsqCuyDelFh8vrjK-uEnlOejir8_YSWLSPNDO6fpZQ6gqoacXv7VqfpIgBrqRcKSgZ2usM5eqA-UGdzNyw9F0WaNfWOVn4D3P09jOJhsSWkP_9iDRlOWnw9BrqRHfoqlIZefW6pNQH5U0k6wqtrqFrDXdAvWkxTrEG2cbLcGIt0wv3F3De04qRi_2rYocd_w57PpHfKwVoxPy4CgyBqB3lFcc0tPg6n1qU0rRMR-jhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های پیمان یوسفی روی آنتن زنده درباره حواشی امیرقلعه‌نویی و دعوت نکردن مهدی قایدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/30413" target="_blank">📅 14:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30412">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMbyrU1S2YfqLqvMwvwf1-RGefCjW4U5ayH68b4dn5cgtuYMom6p2sqDz8xz5Ca11ad_m4TrcUS1DCX15gTjb-dqIdfe40C9lcxCktJLe_U0GXKKid9l15OtH1hSWpj7cpUaoFHDGK2TE0Lz_3YNFj3LpW5RAw-vS-qIy15TDDoiqGCExbE-chGWVwTw5jeznJmDUVwUFGc6mL8_fGgGmquF3AZLVolfWgMSDc2sGsFBg8zYFkKbGxyQi6h8VlArDtX5GWTRxJV0IgNaiSuWMsWhjZZ41A4GigKruDK2zs6KFobf7oHRO6EsacC5KM46NmfNOG5eO4Ocjsaqq1yFEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رافینیا دیاز کاپیتان بارسا؛ صاحب جدید شماره 10 تیم‌ملی‌برزیل؛ این شماره سال‌ها بر تن نیمار بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30412" target="_blank">📅 14:30 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30411">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4UjXAw_6H8YpE724T8zxnuY1PFyASR0YMTluqnNHrqyv5NQ_o4_rOZD2Exmv5KemNNPCDj0--KOOx-kEPxXSE1lQQQkoNfz4nzD1J6r7mYGGSyDsq0O_TFW7VXSB-o8ZeYbCwvzjyf8M2z43n5JYu3VgKADL3z2eoQPDXdfn7Xetk1GRSy_jI00EX274ylUP_zlXGD0avWVe1I0LgfYnynbio0C2dNhDvsV40BRXuSLgjhOJmoj-v1iYQPSYYKRUR0ekkuJR5OOiNNiSsOJtLcs_F1Lcqqsx5Q3Jmw8IQZsBpSBSgHRHnNRyc2nQLYOO-EAlQ8SyOu8B_jFqFeidg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه سپاهان قصد داره درصورت جدایی مارکو باکیچ از تیم پرسپولیس درنیم‌فصل او رو با قراردادی 1.5 ساله جذب‌کنه‌. مهدی تارتار علاقه‌ای به‌سبک بازی باکیچ نداره و بلافاصله بعداز فسخ‌قراردادش با سرخ ها با باشگاه سپاهان قرارداد امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/30411" target="_blank">📅 13:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30410">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6Mhv2MpnWwCidDaNssfuJplmUz2ofst4jghuDhS28IK4ESV3H_OHT_2tJC-4Bwa-mdWwByTh_ruclK1ORKs_59IO004tJNNpQX-uVPJ50KNuTQPOxHkby7jtKZI5fs9tX4Zw5J3gmxEMLbM2cq0e7QfvnfjpmbbFQJwH2pJ0i06VJgH-DK1rlBMzSQDFe4T6wY90TbIkxa4USjjPuS9-J1qLdLMPlmwaknU7_PACzjlb_goLz4v9V_386fK2D8Tnc8gJV8ydLnCWv0t7exIfPaBBZZDlNaMShnCqllKeXH_knErc9WBkJJifapvwQ_2q3nrhWtDuV3TBTplNhBrEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج 4 دیدارمهم‌امشب هفته اول لیگ ملت‌های اروپا؛ از پیروزی خفیف پرتغال با گلزنی ژائو فلیکس تا توقف شاگردان ژاوی مقابل آلمانِ یورگن کلوپ و پیروزی شیرین نروژ با درخشش ارلینگ هالند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/30410" target="_blank">📅 13:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30409">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0rpRkWdz2-pXVuS10yVtWYrKffdHi4RbsGKanhLN8uhPuWwKm2M_qpZ7T6O9KbJhYNnWwkSw3EPNGtycHhWehafZDca_6G0tg8WB3hXYFrKNFPRQNlXqX84vPtUqUlm2zWUnlOAgbibl1GaRczPcIY-0g-cvTjV3k4ARKP1L7iZ5ndx2M3FrcHt2ikVrw_SfGtxLWpezCf8P8aeJrKMweutE3qQB6z7iDzHaBrCpQJCid6nhpNUJX40C3cWRlLtrI4nc5pZ-TK05mOsYEDqoY3gELqaueJcIOuhylr5d_qNz9O2oE-7TD36zxhxQsDW6nFodcY1Og8EBX6L3o6V1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
ویدیویی‌از سوتی‌‌های عجیب‌وغریب پیرمرد های تیم ملی در بازی روز گذشته مقابل ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/30409" target="_blank">📅 13:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30407">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghQ9ATB9BIgpWbbslLOVy-gU0j-ISz4jtPt4qJ4Ia_ZGg0RIjbLck-EKohSQKuq0tmnV0-AUt0XRuuw33_rrHkB7XuqwOezeq7xWI_td2-SiTPcYVJ-YA1tcUJBcFrHyg2HvONCHtUW8956ztsbVu4whYGoAWblwtT8f_8X6ktzPTrvx-afZ4iESy5ML35DBzMWIZE-LF0_MIZ1AeO0gSHZmNR2Dv33dRjh5IN5hshXhYFPqABhvJ0ftcKH4jxQ0toUbbbapW7jVNuJtfRux5McEHkECrXH-xC3XbTDnJ2BaKgZGk4MGJelO61-n_RNCi3CrBMRz9rVIOEL14OkFAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم‌برزیل‌فردا دراسترالیا به مصاف تیم ملی این کشور میشه‌. حالا اعضای این تیم به محض ورود به کشور استرالیا بااین‌استقبال میزبان رو به رو شدند. همشون زدن زیر خنده‌. قیافه آنجلوتی رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/30407" target="_blank">📅 12:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30406">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkFeRtynP9CG2LCsuCKclxbONCyhyVE38wUe8GfmUTx-u8tuk86z-GHhFdkh1Zd6xJx8b4dERfPnRmzHZq7zZe8EaldSxfqnqwUgYqtKR5q1KV4D7IbnCFImS7ZT54tC5mWuCMcgAoW8B3LRR74hcLCWV6Yk5nmvu6Vezy8PjIcEOZOzYcJ7AWRz1wILWyK4eBHOJzMbsLJYt-zSPKHD9OX1aGqulMWNYOxREcmIMD5TOqE4hrTSpcCdTpB0zjQgQjrVBKqm-jN7gWJilAeT0URASoqHiY-dlVpYRsAvuYGbns02EXXSdn2ZE2z02ZeJl6NDjyP-JCpe5f5CIJ0f7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق آخرین اخبار دریافتی رسانه پرشیانا؛جدایی‌دنیل‌گرا و مارکو باکیچ در نیم فصل از پرسپولیس قطعی‌شده‌است و مهدی تارتار به مدیریت اعلام کرده نیازی به این دو بازیکن خارجی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/30406" target="_blank">📅 12:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30405">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W14o4G_dXbbi8zLLAXsi1lGGFnW-85KQDFRjZa_VMC9eKut97yOlce1w9b8Kr005UZUT04Dqv4EIC5y7b7gQyg7HoA6JhUfzLK1odzWpsGKsYPuoyGn5bvs10MOjuhr2QqEubPFgjhY-0iLYPLw0je3q8DaZ2tUXS-CFMhB6P05oxydDJtz4Nt2vp-nD-PTjJHS3Rv6qnIO0_mRtKOxAvJqrWxY2C3qDouswRB-OpuSHsNwe8uRpb6DiFkArGHRWog2w8PCY9zxx-RVAkSfHTgtLMLUAgQyUA7MRybdXixR07Jfdp7eTzDEhtbYk-wNXGsNbGdrCaJ49SYxJyFUXAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ طبق پیگیری‌های رسانه پرشیانا؛ دستمزدسالانه مامه تیام درسوپرلیگ ترکیه 750 هزار دلارامضاشده و دستمزد فابیو آبرئو آقای‌گل سوپرلیگ چین 950 هزار لار درسال ثبت‌شده. جفتشون‌هم 33 سالشونه. آبرئو در نیم فصل بازیکن آزاد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30405" target="_blank">📅 12:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30404">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGYkVkk8mnveTeskp5IjUdrSNnMj2K-RoMdKHW0OvO5Ug3XyqtSMk86JZRr8Bz3NEueKfVJhf_Vo_SWH4lpyKyFoap6rGrnLOKLXQ2hrv494CBgsqvkzefx4iiKxCWOU9-WGLyzciBo5YOHusYvqVBSqX5kQ8av3_cXyYv9mQrFiacYsJb778t-MHQLs6AkiQhhGrIHhKNy9rKC9_vU6an7C68UAHdG8Ol9GNU_81FkEFNBKiSULNpdkdWjIyiXYRTJ30AymBQtl7OXLMf1XbDFhhJAFuct5PWeB-GhlLP_FT9TsvOmj5jri6irYOCZBYhG1wcAicKjFXTfeClMd9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آلیشا لمن ستاره‌تیم‌بانوان‌لسترسیتی: بارها گفتم بازم میگم نباید تفاوت زیادی بین دستمزد بازیکنان در لیگ مردان و زنان باشه. الان همونطور که لیونل مسی و کریس رونالدو در فوتبال آقایون میدرخشن من هم درفوتبال بانوان فوق العاده بازی میکنم بنابراین نباید حقوق ما…</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30404" target="_blank">📅 12:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30402">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbBAhCRzeSwWLJ3n8QZQreZ7b_8qdMHOdfefdMH3eHQpjV4UMRtJBfqTKjVizLJqM0Aox_O_B4j6UkP2LKK1L46YguR71rJRdIVGayM9mdxBrlPxLin8ULHM6OR9LE65g1L_c53c60rJCm6pbZ_lK_P0ORINFyafyBqTfbtJFKSeV0f4NIr9gAtSLWQdO7NcQxgY1YhQC4-2VMf64nNoznNP4CYxmFECmcs594qq5YYpQskNMrnRMMrXJ0ERjiqb1VRnht4inY5g6t-ilBL7knP9inxq-NN13AweOGx-pvr6bxfX2F9-vclrNJVPSMCFoAxKkm9CtN4Zl7u4zUu2bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه ال‌ناسیونال: اولیسه خواهان بند آزاد‌سازی ۱۷۵ میلیون‌یورویی درقرارداد جدید با بایرن‌مونیخه و گفته درصورتی تمدیدمیکنم که این بند رو بگنجانید و هر باشگاهی "رئال" این پول رو داد بند رو فعال کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30402" target="_blank">📅 11:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30401">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/638f1de447.mp4?token=TBFhjNphvLuVNybJmGRk7psVic_NNQHyl_H9QTEbCEXN5NoU6ugGOFbVsdMDzpkoTbL7bCEgHbg6eHmd411FsXXerHnkmEtJepXOPPdZdi9NtzLuAELprNMdaCOSY45GUqWutT8VeGEnmQD1l8cE288VmORjU9pW0RQfD_V9NdUFuCUtnTOyV2jqw_7FfNVukxnm_vPzDy9sTdSUVXAKe_tXonCloR8QmqNeZTb6XNxlnArBhAVBjO-DN-t6W3g4PGyXh5s25irdPQzMrqnpxzBH6noTxl8FV25XeQNRjpnsFIUaYmlziJMWwxm3VvTnfhkiwMIL714HN8zebW5tkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/638f1de447.mp4?token=TBFhjNphvLuVNybJmGRk7psVic_NNQHyl_H9QTEbCEXN5NoU6ugGOFbVsdMDzpkoTbL7bCEgHbg6eHmd411FsXXerHnkmEtJepXOPPdZdi9NtzLuAELprNMdaCOSY45GUqWutT8VeGEnmQD1l8cE288VmORjU9pW0RQfD_V9NdUFuCUtnTOyV2jqw_7FfNVukxnm_vPzDy9sTdSUVXAKe_tXonCloR8QmqNeZTb6XNxlnArBhAVBjO-DN-t6W3g4PGyXh5s25irdPQzMrqnpxzBH6noTxl8FV25XeQNRjpnsFIUaYmlziJMWwxm3VvTnfhkiwMIL714HN8zebW5tkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رافینیا دیاز کاپیتان بارسا
؛ صاحب جدید شماره 10 تیم‌ملی‌برزیل؛ این شماره سال‌ها بر تن نیمار بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30401" target="_blank">📅 11:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30400">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifsb6Lo6lZp0bvdG-ZU1Vn-FejsHBMrxqXMaq957T16dtDUW466alpAtgFo0VWlwhRZp1qCKLSARIa4AlEa9DNeD1iw3oVaafyA7TSdNiEPN1C3Xhg8AA_u0bjaoGblu8ap3MpCToOAreGKYu_tAyqIzstXVVOXssY-EXdkaaYUcgDgniVrv5Uin3VPM3Ncmx4tdQ_8WhHVvIzcOw1PGv2XZZsN1fQITf0h8g3qkz_sDZbVCkJ6tBKbaWNx5lsnukm8xqxgHwLLLFs-OU-k-Q_b6FX-rQTK1X_3kYRhOhNFJ3P6zh2R0i9M7mVQx_PAI1naCme6hvpbPNbMhFNpIsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدیویی‌کوتاه از تکنیک و مهارت‌های خیره کننده جیجی‌ گابریل 15 ساله‌که‌ بزدی یه راهی بارسا میشه یا رئال مادرید؛ هایلایت کامل عملکردش رو تو کانال دوم گذاشتیم. پسن ریپلای شده رو نگاه کنید.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30400" target="_blank">📅 11:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30399">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/649db87b28.mp4?token=mPRlumuYj8x8-9X3P4AhWl2FsLLiNd1vYoTwCxs5eS7FSHfyWr782Ag6g47NSRjzoS04q-cTCTlJWiyeqxkmGGipBJBMpvyQZsW0EDAHqKY3u66OKrojXi5KNzXI5QvQtWkVYkHnDTl3NsdrtmQswQggP23vQaXiw9VY1YqRE-1fofs1lZ5wbUVjzve3S0ktqEq8w_SHBJKJ38go0OUBWduBHeHaMSBvBE7gCLPJOpUTlhB1vW9f7ETzPuqtgsqq7O2dy_kaCVpWrFiYLa_fhN0smjhAG13ZwKz1ffa5HPp8vNh7L6rNVgtHAjHfto7uOk-8tdj45TcBnGuvUMGh-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/649db87b28.mp4?token=mPRlumuYj8x8-9X3P4AhWl2FsLLiNd1vYoTwCxs5eS7FSHfyWr782Ag6g47NSRjzoS04q-cTCTlJWiyeqxkmGGipBJBMpvyQZsW0EDAHqKY3u66OKrojXi5KNzXI5QvQtWkVYkHnDTl3NsdrtmQswQggP23vQaXiw9VY1YqRE-1fofs1lZ5wbUVjzve3S0ktqEq8w_SHBJKJ38go0OUBWduBHeHaMSBvBE7gCLPJOpUTlhB1vW9f7ETzPuqtgsqq7O2dy_kaCVpWrFiYLa_fhN0smjhAG13ZwKz1ffa5HPp8vNh7L6rNVgtHAjHfto7uOk-8tdj45TcBnGuvUMGh-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
👤
ویدیویی‌از سوتی‌‌های عجیب‌وغریب پیرمرد های تیم ملی در بازی روز گذشته مقابل ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30399" target="_blank">📅 10:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30398">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXmHonkZ1Hjc8ClAiUQoZ-vCTjDHrJvjsy6ysE-6NqN6m6xW0nTKLdxObQsFDRBL8jwf35YgDQlSnDsBqnsI94gEmgjekxrrkQ24cMLHRVIsaee2MGc_fM4iETnZAVHMMpYWIGNmwclWQQ6n2J9LiyBjy5WbYeGLmTSRW63laALtf7XNEDXMKyDR7_w2QERpNvK3szO4wwM93eIVHyRPNI1LM9F149112SHqKXrKKAZjdUA5MrN_904vwoOOuvDABM6irDZ4yR0n1X4XbimQDIQ16rDPgedH_2TTZmFWxlAjp5Y_L8VCJIoBefEPaWGYC2sW47MMi9b10JNtLqi5RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
ویدیویی‌از سوتی‌‌های عجیب‌وغریب پیرمرد های تیم ملی در بازی روز گذشته مقابل ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30398" target="_blank">📅 10:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30397">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/698f9deb89.mp4?token=uSDgVU1VuDHJKvSIV8xrZBqjtLCn7v9EF7NyPJHS3ReV-f99tHBArA7AJDy69hY4R_dVNcWRi138hM09QHWYlFqtAa1ATgxzfklEhlZLf3FHzWsSwrS8ZbvhvV_7lsViWxwOEEmIu1HcvSKVPGSmpUDCXQN9lbIT670VFJCVE_aFyDwT_ea4rhAVViYaJyPfpnYGQ1DOAmE9lwrz6DZQV1PFEDLT3mrG4MH5qhrv2yXgOZRJs9BAsoZOplqVBuFGWZM8wtOwg-TxFN7Eo7QSkbua5oA2rvXIrvYrQ_jn88BpSRqljRoSBVD48f-EKl1XHwdUxt7iepNiqOmnDqNcQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/698f9deb89.mp4?token=uSDgVU1VuDHJKvSIV8xrZBqjtLCn7v9EF7NyPJHS3ReV-f99tHBArA7AJDy69hY4R_dVNcWRi138hM09QHWYlFqtAa1ATgxzfklEhlZLf3FHzWsSwrS8ZbvhvV_7lsViWxwOEEmIu1HcvSKVPGSmpUDCXQN9lbIT670VFJCVE_aFyDwT_ea4rhAVViYaJyPfpnYGQ1DOAmE9lwrz6DZQV1PFEDLT3mrG4MH5qhrv2yXgOZRJs9BAsoZOplqVBuFGWZM8wtOwg-TxFN7Eo7QSkbua5oA2rvXIrvYrQ_jn88BpSRqljRoSBVD48f-EKl1XHwdUxt7iepNiqOmnDqNcQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولین‌گزارش نیما تاجیک خوش‌ صدا بعدِ جدایی از صداوسیما در بازی شب گذشته آلمان
🆚
هلند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30397" target="_blank">📅 09:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30396">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCx90pSIAaA1d8ZGdD-3Y_u9jOj9sLnihSto3cpjIyBlXiM2Nh8jbm6X39rQvH9GUJA13eyCdT3LPpGPIXx9AQ4DlIxdPH8LS1vBU8Qiv6uV4zGj6xO1HVUJmfOhT87EOiLJG_UYV6SN6fDn3HnpZXZen5fMUUUfkokb0I5ztX6b6OLZv_FIWOIhA4XHOqNQCkWVLVP6LYp5YiyEVBLDfCZEa7U8nbwb5fQkj9ihLlng6Igc09vv-OJZr2eK7WiiEHuRm6724-uq6wM2AV2o-loqgWTXynxMfZ08NtZEL5v0maVOgSHI3xXdii_6G4mDSDCKgCTJvuX8KAoYy3EP7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
گلزنی‌تماشایی‌کریستیانو رونالدو 41 ساله در بازی امشب پرتغال مقابل ولز در لیگ ملت‌های اروپا؛ این980 امین گل کل دوران حرفه‌ای رونالدو بود. البته دقایقی بعد این گل توسط VAR رد شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30396" target="_blank">📅 09:30 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30395">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da1f2ad337.mp4?token=hoQbFphHE7kniR6rp9heuY9FC-iBDYLRaGGqEbJtmadxciF2d8AlQiprwy6oM8q0fNz9g2cZObTU-Otw_inDFQiJFHNghPO-jUS4XqVg-IA6c44CtrsYsEO-t-8nFvqBeRCnXI0kM0gn8YEElza3jPeL1iSMRdoDpMRAsDiEf9xNFKqg1rnLpjD2m2voMSvJ1udD55u9kytgW8oJld5xuPwIxWuzmOdCSGxi1YvyL1NDUiWFnrPiMkbj5wLSxhqGs1imGYLi5l_eTO40OqABUF3nQ6bWKWrxY75Da4AiceFMU2nUKAKMbG1mEGlV4-DVsMnOgyf9jwDWuGEtLEWkpC3BJrSP7bzJP5P19BKUvlKizx3wGCaxYovGRc4wmGEel9WNQBRWaZHNzmZyJyYoTThmYtlOFcp0a0c9pGspJYGmbb82v4UGBAqgRz5objM7K87jCp72T4q5dTNGGWD1f03fdGWPQmF_TGn1ZmstNfMzNHZsskxBJXMjLJQnrprOywc7VuwFPw59ZhcbF9Lcvqo-KsUari73132jAub1EvxyugGc9_URXpSATDydy7zRma_snk3H3P2pv84psflfFLg12W7rSQlWBiHiblVQBNrrO1sqjGlR7QMh-DlRhie3HWrJA5S7K7V-Kyty5JOKQOM70DVEZAtQRN02fhL2FjU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da1f2ad337.mp4?token=hoQbFphHE7kniR6rp9heuY9FC-iBDYLRaGGqEbJtmadxciF2d8AlQiprwy6oM8q0fNz9g2cZObTU-Otw_inDFQiJFHNghPO-jUS4XqVg-IA6c44CtrsYsEO-t-8nFvqBeRCnXI0kM0gn8YEElza3jPeL1iSMRdoDpMRAsDiEf9xNFKqg1rnLpjD2m2voMSvJ1udD55u9kytgW8oJld5xuPwIxWuzmOdCSGxi1YvyL1NDUiWFnrPiMkbj5wLSxhqGs1imGYLi5l_eTO40OqABUF3nQ6bWKWrxY75Da4AiceFMU2nUKAKMbG1mEGlV4-DVsMnOgyf9jwDWuGEtLEWkpC3BJrSP7bzJP5P19BKUvlKizx3wGCaxYovGRc4wmGEel9WNQBRWaZHNzmZyJyYoTThmYtlOFcp0a0c9pGspJYGmbb82v4UGBAqgRz5objM7K87jCp72T4q5dTNGGWD1f03fdGWPQmF_TGn1ZmstNfMzNHZsskxBJXMjLJQnrprOywc7VuwFPw59ZhcbF9Lcvqo-KsUari73132jAub1EvxyugGc9_URXpSATDydy7zRma_snk3H3P2pv84psflfFLg12W7rSQlWBiHiblVQBNrrO1sqjGlR7QMh-DlRhie3HWrJA5S7K7V-Kyty5JOKQOM70DVEZAtQRN02fhL2FjU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولین‌گزارش نیما تاجیک خوش‌ صدا بعدِ جدایی از صداوسیما در بازی شب گذشته آلمان
🆚
هلند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/30395" target="_blank">📅 09:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30394">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-8qz07RakU17AXMqc1N74lgY_QRUrmVYxC_5-4VuxTHH6pSIPBy3H_UwlDSFeXkiSToLCsxfo0EwmuX7zMoL0VmR3IwzVDcEufO2SUu6hHyjZQ3rSVqrGJFQ6JROR_Ro3T4btHmoiv66xMvEJ0-bvuiiAAM2RM-zEwVmupNdxAS53GDZQDS0I400uXv_6lUllg6VJvAM4lTr011pVNVU8xrROnQrrmgKWxzwnM9LYjCQ8M3UOHfjt6wKpC_6eIrdESApBSV9YiIEupkwl_wldAqmpQL8_qmg29F1SxNn968UrBOajpkykTWyTaVJFqr2N2x-0NQJERLLJpSLtYt9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ حسین خان عبدی بعد از افتضاحی که دربازی‌های آسیایی به بار آورد بزودی بعد از بازگشت به ایران هدایت تیم ملی امید برکنار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/30394" target="_blank">📅 08:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30393">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-H9PK64ILpCa_LrTf8f8j3JHBmWRawr48Y_8Syz1RQ_4tE7EQAnbp-icRy6H43zJbIw4jFb2zzw1i_rjCdNR9YSXF7QSxdd1gl1DMZo2TR7CssnU_QsRuaf6AWJcP8xA6lchVaubJYJQsV9weec-nGly25EQib0UcuEgDmuplDlXKzqPDcdI-XuzRoGfvbpU-COnnnRgIHD0NdcS1hrgAGNF-1dNfGFCvSeAeKojaHamOg5UiLBIvyKFtcqlk5l_LFt72-1nbXWFXuTsVnRUNpONLgUFwKo7AEKV4HlCug9MfHvOR4no8dDG0NuO9hOwRoR5xesyoMZz1gxtN-VbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ جالبه بدونید ازبکستان بعد از 6 بازی و 5 ماه بالاخره طعم پیروزی در یک مسابقه رو چشید. این‌بازی‌های‌دوستانه تاثیر زیادی رورنکینگ بندی فیفا داره. باتوجه به برد قاطع‌کره و ژاپن‌به‌احتمال فراوان در رنکینگ جدید چند پله سقوط خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/30393" target="_blank">📅 01:52 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30392">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57e45f06f2.mp4?token=ep-OEMXeBbRvSkhGxiwqU46dGsoW4L3e_O9V1eCfcMiRkl0hfqFuGHsWIx3t0QvfZz8SsYpsl-MtMB8S6XoA1HA_I2abyVBdsGOt2pAO_Tv20b8OjpjNMCPyvXNfxl9iBBVT8cl2G6wykeutQLXHblTK2M-FhrDfN3aakFq65D2S2dLHPRLCyp4fCiyX62YL6nVS1Ilk8mw_imrl7BlrwLkKPMW7MfumJ53iIClScUfM7NMskKWiUG47bpzw7WIctjyLLDDDEvl-OGRDJdoltUT01s-EeTM8gjpxhEkazS4q6CjkHKgAlA-oSFeJKgbJFuOz6IZk7xKgQFBURT6WWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57e45f06f2.mp4?token=ep-OEMXeBbRvSkhGxiwqU46dGsoW4L3e_O9V1eCfcMiRkl0hfqFuGHsWIx3t0QvfZz8SsYpsl-MtMB8S6XoA1HA_I2abyVBdsGOt2pAO_Tv20b8OjpjNMCPyvXNfxl9iBBVT8cl2G6wykeutQLXHblTK2M-FhrDfN3aakFq65D2S2dLHPRLCyp4fCiyX62YL6nVS1Ilk8mw_imrl7BlrwLkKPMW7MfumJ53iIClScUfM7NMskKWiUG47bpzw7WIctjyLLDDDEvl-OGRDJdoltUT01s-EeTM8gjpxhEkazS4q6CjkHKgAlA-oSFeJKgbJFuOz6IZk7xKgQFBURT6WWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
👤
ویدیویی‌از سوتی‌‌های عجیب‌وغریب پیرمرد های تیم ملی در بازی روز گذشته مقابل ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/30392" target="_blank">📅 01:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30390">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqIwj-a31xyQGE8tjKb0Grw8CVNaO40MrdPDboGmsFjtsIem0w3dCABSop4TTceLIx9LZ5zotG6LEFdT4Yszp2DdTWceIflkiSjUZeaklkmqqOw2Dh36Tw2g66WWTj4VA_pVGog3gJY-on8fmhNlimHkvlxr-haPw1dLssd_GLXzo9RvbFiS9bOd2N2OYSM4I0G3zo6-pD-UJbKcNsTHwJhjCxIaT8ZFLOi5f-vAFxXLAz10QTgrbtJAFT7BY3LRDaA2iAsKjHzsK-9I_td7DRYGm8qzVZizsi37xy3cHngmB8bpgTpVdTPnJwJUlSayuOjSiwOcOxAJMfRNJcT62A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ ازبازگشت زیدان به عرصه مربیگری تا نبردخانگی لاجوردی‌پوشان با یاران کوین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/30390" target="_blank">📅 01:23 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30389">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSkLZNAy9ogTXgGPhJq4Y0De7gv0mWkMxB3UxjecdjEzppDlx0AcOCtln7ktrpynue38LtEXaQNt-kRVa4oK4fecVXF1bVU0Xb4G-bVxSBoQdsdwLFjVFSahQ3WMXnNhkhAZt0JE9MgN1XB-g37aWmJbTVYZByA7QozUV_rOtBxeFS7OcZcL1lP-aCLhtiFvfMRxQB_bJtLJrfGfvZly-J4stNWgf1VT0VzHdWmKmLdSN9dPLKXQULvpThl50aLKne6eJSiFpwNdYVjC5fDkpqEvy30LSP1coIBIrFkY1nszlcwi-r_9nFuTaDpIHxTcpUl6r_L9Qot6AYjydtlE-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
ازتقسیم‌امتیازات در تقابل هلند و آلمان تا برد سه‌گله ژاپن و کره جنوبی در شب شکست سه‌گله شاگردان امیر قلعه‌نویی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/30389" target="_blank">📅 01:23 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30387">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KROOd9AORamCaIELx40gd0DlPEOt7rL8avbc0c5cvQt35PxujuHS1WhkrrTsr5QVKZATG3LMzIoq6Z2rEaiCR79s8wXKcjJGgjLlSQrDafeAB542Q4Qs8MXOGZDJMURvfaaGQRZsM7AP79gTVlpkMFWfSlH25M1DM4DPtpe7P7J6xKRjAfANtP9b35V25fZCO_5aHlfDBtqgo4pNULPbu0-CHtvBcT3lypPAgg0MXOFP-v1AjqTB7_iO2xhFZ1eRNDUAGRZFPw8OXPFlavcFde92m-B-wUi5rPq08GEG9-GEjeVcCSUwDR4uYrjNO1iU86WxdzmSBKODK-mPNY34RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ طبق‌شنیده‌های رسانه پرشیانا؛ دو ایجنت نزدیک به علی تاجرنیا رئیس هیات مدیره تیم استقلال از صبح امروز تماس‌های خود را با مامه تیام ستاره 33 ساله سابق آبی‌ها آغازکرده‌‌اند تا در صورت عدم موافقت فابیو آبرئو برای‌اومدن‌به‌ایران بلافاصله مامه تیام رو…</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/30387" target="_blank">📅 00:46 · 03 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
