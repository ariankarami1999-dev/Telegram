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
<img src="https://cdn4.telesco.pe/file/h-gvLBS3_WEOir7T1VuDkCGEwFaLuWplxFamZpQnQkgUs3Y228_R8MX40yoMwgHyDhewFVjaHssF5gJKvYBuyLft2g0HGO3oqRB_s8QY1cR7d6V0XCWC7Qzj6mCSI8KnlK4L4k-bp_LdOgjThIQtyZl1nG9HtCLekHpTAt-BM3Ai3YpWw77XK3Of3jTOj-wF_gQ-0uVHzTUnfrtnyHc7NrCRw4tqaQRIXeQHOJVdskspMHehlho6OH5PgfwWltzwv3RLXqc7T6Fmb9T6-s_cxs16P_60lrYZOlZgi2md6SulGr_C3Dp1J05vzSs50l3WxSIJlKNlEodCUAT5lN6QsQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 180K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-09 11:30:51</div>
<hr>

<div class="tg-post" id="msg-22459">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5359012d10.mp4?token=korwIgW9R8_WX1G8PbnkJ45wWiPSgGR90w5Xa6NI1dAMDLyF0lbmkioHrJs-FTQimiYlAbQV7yMpOnEwKLOg-uu20Oe_zjzZOGF_SwqF2RTJDPqjwzaiflsn_kSXQxDgS8jt60sRB6PoPsYMbVPfMuuRd8rvb6-f3mSn1vlyFbGJ4Xz3-Goa8uEHXW6A0ARVCc7HgSAO2Pr6FA36YybWI7DBw-IoDyo8dluawKYkqEJlfOvj2Z0DDY3MSOTlyodIt62T5G0fu_BJh_XQERiI_WdR1ZjRYlOUarZsMMlwzieNam8jjGeUEAJKIi86WAP9i3AZAPWQbCx2fpakjH_oVX32girNudR4193u3jmP3YEJ4yfmkKG1ilixh-dxv4vTJyD-FtJUUQdCDZxYsaGiYSUQCOJ1ebkPz8OWKKDZtWCw_SfrXt6JVLiT7mfD5BGp4d7qupUsmWKfA3c_69M-2byvp5wP0wWwWSy-ElwcPEzIbRsLmZoIaiSxVXtgPA-voCIh0n3lRXcHamDYAPwmh3p8R6EmXLV7slyWlH3Tn5tpoGZBu_0MAfNVGAAsOLeLOqxDzbjvEPqzhGSMwAMuvOXqOFmGEr8Z-ViDHF3t2o6RJgX_XZTtCqGSqE0_66nVvcNGL6at37WK3fnq6uXGvko_yFBsuzKiV_1kIu1n-5Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5359012d10.mp4?token=korwIgW9R8_WX1G8PbnkJ45wWiPSgGR90w5Xa6NI1dAMDLyF0lbmkioHrJs-FTQimiYlAbQV7yMpOnEwKLOg-uu20Oe_zjzZOGF_SwqF2RTJDPqjwzaiflsn_kSXQxDgS8jt60sRB6PoPsYMbVPfMuuRd8rvb6-f3mSn1vlyFbGJ4Xz3-Goa8uEHXW6A0ARVCc7HgSAO2Pr6FA36YybWI7DBw-IoDyo8dluawKYkqEJlfOvj2Z0DDY3MSOTlyodIt62T5G0fu_BJh_XQERiI_WdR1ZjRYlOUarZsMMlwzieNam8jjGeUEAJKIi86WAP9i3AZAPWQbCx2fpakjH_oVX32girNudR4193u3jmP3YEJ4yfmkKG1ilixh-dxv4vTJyD-FtJUUQdCDZxYsaGiYSUQCOJ1ebkPz8OWKKDZtWCw_SfrXt6JVLiT7mfD5BGp4d7qupUsmWKfA3c_69M-2byvp5wP0wWwWSy-ElwcPEzIbRsLmZoIaiSxVXtgPA-voCIh0n3lRXcHamDYAPwmh3p8R6EmXLV7slyWlH3Tn5tpoGZBu_0MAfNVGAAsOLeLOqxDzbjvEPqzhGSMwAMuvOXqOFmGEr8Z-ViDHF3t2o6RJgX_XZTtCqGSqE0_66nVvcNGL6at37WK3fnq6uXGvko_yFBsuzKiV_1kIu1n-5Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
پنج‌ موزیک رسمی‌جام‌جهانی دوره‌‌های اخیر؛ تنها دوازده روز تا شروع داغ رقابت های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/persiana_Soccer/22459" target="_blank">📅 11:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22458">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfU_9t8iP74dFWmAKbEwklE4rKvCHf_7JyAZwhOj4QaPcCSHpSpxggwsWWPyyHWN-FXn4fHCsyfJ30lw8-lavjzEusvaFJv9_7ZCWTuAx_lcnkDBKJnmtsAuXNkREL9Gxd8WZtNQ7Y1gon_Ymyse0rVM_SDoSHieTACbmFUC8ZiHIiT-PfWqWkap62ppT08euwhIZwss9K_OO9F0pCnf79GMtU3pgrpGJuXVgJNbgSJSWPjFzZEq0BwZI840zHp6u4CC5-uz1bLvNi1KTUyqM9yjZqpLPr4l8fgp1iqRjqNIf5yD0OBJ-MWHZ4benqZmODHCKTQvJCs6jbfFRd11FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
مدیر برنامه‌های نیکو پاز: ما با باشگاه رئال مادرید بر سر تمام بندها به توافق کامل رسیده‌ایم و نیکو درپایان فصل‌جاری به این تیم بازخواهد گشت. منچسترسیتی، چلسی، اینترمیلان به دنبال جذب او بودند اما نیکو علاقه داشت به رئال مادرید برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/persiana_Soccer/22458" target="_blank">📅 10:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22457">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/au0spLpXee-AaAOi2PCdRzFsbrsxpHY4eaD9J1TMowI2fOeIlmonM4br-Xzjk2Vto7xAbWfRbO4jTGSJjt8VUxWu3Gd-5POYDyQgK9yiESAYF-qVRs_Cm0q7RrH3r1jNwE00Ulop0sM7-Vk7_SLwyDG7EZkOMpgqJCwZbdmt2OQuVubetaYSAc1MtNV0jl215kxS95RO6LnIvcgUPVDR35Yp853LC0EqQm91SpFaNp41RZ_Tdn3rzeyVsYs2o6RhhrSkR8MNjt470BOD8C0MIQAm3YQ4Om8UiqkVRkpMjcWxEvtnsVn5vk1q5wBiF8IccoKlpTW9XHYENfIZWXCpPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
به‌مناسبت فینال امشب و حساس، مروری بر فهرست پرافتخارترین سرمربیان تاریخ لیگ‌قهرمانان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/persiana_Soccer/22457" target="_blank">📅 10:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22456">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mq6uqzFim3ws79eY1kPfmE2E0PGBhBQXAEZMlFzCdq43PNnuTOqYniV5G9UR4BWKBrOy3NHcokWtPQ9fWGECxhw_ZGkynpkNU0hI8WF_-KpFukvkHhRwJ-ta6j4UjlNJqx-pZLFYilkiR7omOdEe5Uo7FFd_f2iWioPb76fNh6ZKDXsNKyT4-rneUDtylYLY6tMIM15bqg84ykk-48itMxOCo5g8lqYNh7GK56WxwOsJEDwQHlIBbJvOhF7em7Lod1LiTMK6e4dr1vpQNYbUW6VrM9zfitEc5zvFkWOl5F5_S3gbuq8Oq0JrsCtwD4IttkeMg0CnB04dTnruuJJQKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
لوئیز انریکه‌سرمربی‌تیم PSG: میکل آرتتا گفته قطعا آرسنال قهرمان چمپیونزلیگ میشه؟ اینا همش حرفای هیجانیه امشب‌میبینیم کی قهرمان میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/persiana_Soccer/22456" target="_blank">📅 10:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22455">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2yAwI6HyB4Zw8VI-wfVauz3_fqFVh73hFFYCYcLXd07xNMUqWMkc2SaK4IcL37j2nC2hZBJmofT1_Grr18n0P-vL-nXOuQvM-xunN5UUqkGQvD8JqsMJwFwM-wrQDHuagEjfVsAx-RSgyi_YZoCbK1yky_o238wRtsvtjzdOGEFvMAslKFPrXLcljSpGYoP5P_vmwJvcA2LwXwbnhbip37CdStBGGC9Rs7a_shcwRrwRNRXLGr2A1KVOMbVrLr9AxAZIGq7REQT4u0p_dvLwbeA7V-9W_WDWo5LCfpybsoUfZ3CnQNyG-97EY9gIrqT6j4Y59zhECncVnui-dsG4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👇
فینال لیگ قهرمانان رو
#رایگان
پیش بینی کن!
🎯
با ثبت نام در این لحظه
#وینرو
بهت
🅰️
🅰️
🅰️
هزار تومان جایزه بی قیدوشرط میده
⚠️
🤔
میتونی رایگان شرط ببندی
👍
تنها کاری که باید بکنی اینه : عضو سایت بشی و
🤩
🤩
🤩
هزار تومان جایزه بگیری بدون واریز
💖
تنها سایت مورد اعتماد ما:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
r9
📱
@winro_io</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/persiana_Soccer/22455" target="_blank">📅 10:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22454">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d629612bbf.mp4?token=bpQKSAKV6kCCwJAQt1LGFJksNDOX6GUN70UchkKHL5uSIKfyAXdoJWDvt7ILfIpeAe0X633nRZNk6CbGNWIgm8ciaeSNIYc34h4WqwyY_sDWPh3Vmgi3s__D12wmU1UMXORtT2GpDdZrMnMi7_R-CxQTNPTFqJlN4vaY8F8nvt4Z9pgmD-yxLScVgixS-RMQRisMOmZBB1WtkOeugZGQGNRd4xPzqGfXEwi7iic4t0cDOB3DlfXpAZ4K79h7boFRil5gXsMBWB55Or8eA8BMiX6ck8PeRiYHopiYCxsxUmHKi0RlGhj_ISYbYOV-5eI9Ev7cjhn4FbsCKxh1fALtIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d629612bbf.mp4?token=bpQKSAKV6kCCwJAQt1LGFJksNDOX6GUN70UchkKHL5uSIKfyAXdoJWDvt7ILfIpeAe0X633nRZNk6CbGNWIgm8ciaeSNIYc34h4WqwyY_sDWPh3Vmgi3s__D12wmU1UMXORtT2GpDdZrMnMi7_R-CxQTNPTFqJlN4vaY8F8nvt4Z9pgmD-yxLScVgixS-RMQRisMOmZBB1WtkOeugZGQGNRd4xPzqGfXEwi7iic4t0cDOB3DlfXpAZ4K79h7boFRil5gXsMBWB55Or8eA8BMiX6ck8PeRiYHopiYCxsxUmHKi0RlGhj_ISYbYOV-5eI9Ev7cjhn4FbsCKxh1fALtIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
پدری به‌همراه فران تورس و دوست‌دخترش رفتن شهربازی، اونوقت پدری نشسته کنار فران؛ فقط قیافه پدری که متوجه‌شد شب‌قراره تو پارک بخوابه
😂
😂
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22454" target="_blank">📅 09:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22453">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c867b80a08.mp4?token=dCk5isdks51yFmYoFDuUbDPZH4p-e6DYssPyDadSbDNM46DBeb3vIKxqIhaP-EqwQc5Xgm81af1W3nV2_lP549JlSadO4rQ60g11Yex7uGn48s1YVHSRRA_UqAdPL-gZ2jYVXf-3fc3Y02hoLhMyk1FiURe_sibC-RE6WPbJHG4wX67h_p57sETMLm1cgMF_47TIOEEDHKo3AoX0NmTpP3Wazb9lQk8_bRkc3Bsm_aZarPta30uJJKH6eGrQDCQo6F1k6irNblSvl1qQ_Y6wk8oLjJFC_4pG09W3MQh8slDiB7tl8cnmoGDeAyTXKIm5_MZj1ch0RW-BYHMSj2OEln7dUPTyN9wLCiJO7F-u_3b-6Rety5UdVWGK1sG6QipoZwIWFHdm_xRWx2wN-kJk4G2Q62-3fGMSq3zADzAY6bmVwsa8AQRY-jNEgJKEe99oS1NAMRph5RXHmcqUHn9PWKltN_HERJF4Ffmj6zDq0dWY_TELNOGHzZGtu77aCadKSf_DeYRT41JtHt_I0qerexIiKBEqfck0rSVPUYHZofKoG4r7PCDPP8I8NOSaZGjDBM97u36VopglL6C6kwG6ZXOKZqqpfmU_vqwbJMbZGLwHA_v3_565iklphf_SIbfgLklS5NeUmKD9k4XwMIryntX_lVtGTYTYVmGZzs1Xlq4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c867b80a08.mp4?token=dCk5isdks51yFmYoFDuUbDPZH4p-e6DYssPyDadSbDNM46DBeb3vIKxqIhaP-EqwQc5Xgm81af1W3nV2_lP549JlSadO4rQ60g11Yex7uGn48s1YVHSRRA_UqAdPL-gZ2jYVXf-3fc3Y02hoLhMyk1FiURe_sibC-RE6WPbJHG4wX67h_p57sETMLm1cgMF_47TIOEEDHKo3AoX0NmTpP3Wazb9lQk8_bRkc3Bsm_aZarPta30uJJKH6eGrQDCQo6F1k6irNblSvl1qQ_Y6wk8oLjJFC_4pG09W3MQh8slDiB7tl8cnmoGDeAyTXKIm5_MZj1ch0RW-BYHMSj2OEln7dUPTyN9wLCiJO7F-u_3b-6Rety5UdVWGK1sG6QipoZwIWFHdm_xRWx2wN-kJk4G2Q62-3fGMSq3zADzAY6bmVwsa8AQRY-jNEgJKEe99oS1NAMRph5RXHmcqUHn9PWKltN_HERJF4Ffmj6zDq0dWY_TELNOGHzZGtu77aCadKSf_DeYRT41JtHt_I0qerexIiKBEqfck0rSVPUYHZofKoG4r7PCDPP8I8NOSaZGjDBM97u36VopglL6C6kwG6ZXOKZqqpfmU_vqwbJMbZGLwHA_v3_565iklphf_SIbfgLklS5NeUmKD9k4XwMIryntX_lVtGTYTYVmGZzs1Xlq4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
موشک‌های‌گرانیت‌ژاکا بازیکن ۳۳ ساله سوئیسی سابق باشگاه‌های بایر لورکوزن و توپچی‌های لندن.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/22453" target="_blank">📅 09:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22452">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/928b5d2877.mp4?token=X4QtD4EOw1OUUpnhUngjtYz97_G7ZBDlc-nMRa3thVGmlAxuRhcan-D2DTqB2Htg9V2b4Bn3EeNbsDfsCR_HtY-xiH2Ta7Y09xaF2vEM1Ot3DiFGmiQtSaeJdbgSqDji52Oo6riHxQ7UzA17XVScTKcBh2_rU8vEHvk5Xikp4_JmHDmjJ0NF4_JMORPfy5Vi8cB8utRqsi6LnmlFTuOOP_a6peBCfkpJm65C5EbALXbuB5qxNc8A5qujBDDnAXEH6ao5BAb2ee0Sr3YffrSGsIZu0xAakPM8qXRouYlJKZG-GNw30eNwynhK6Kd7dcvlHVrLSErADXlMGmefMheK3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/928b5d2877.mp4?token=X4QtD4EOw1OUUpnhUngjtYz97_G7ZBDlc-nMRa3thVGmlAxuRhcan-D2DTqB2Htg9V2b4Bn3EeNbsDfsCR_HtY-xiH2Ta7Y09xaF2vEM1Ot3DiFGmiQtSaeJdbgSqDji52Oo6riHxQ7UzA17XVScTKcBh2_rU8vEHvk5Xikp4_JmHDmjJ0NF4_JMORPfy5Vi8cB8utRqsi6LnmlFTuOOP_a6peBCfkpJm65C5EbALXbuB5qxNc8A5qujBDDnAXEH6ao5BAb2ee0Sr3YffrSGsIZu0xAakPM8qXRouYlJKZG-GNw30eNwynhK6Kd7dcvlHVrLSErADXlMGmefMheK3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
لوئیز انریکه‌سرمربی‌تیم PSG
: میکل آرتتا گفته قطعا آرسنال قهرمان چمپیونزلیگ میشه؟ اینا همش حرفای هیجانیه امشب‌میبینیم کی قهرمان میشه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/22452" target="_blank">📅 09:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22451">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb17964484.mp4?token=GKHkE6u1dnSyOm1rwxaG6Rvb-inqJ0K1v-YdCOMr50JMKJlnDwwUvGQ0lyACPHzH428_lJMUvWacybrzEfBWh2zIE1wHZqeLZlhKraBViagqTeWgCTNHv0VZTuM9GLjaHaNrAAOiMpsijEzSjA6YepXZ3z7HJwIQIBLFW8BSmkpYZr6iyc19T2KtTTNxCn8dTM6XbSXfIjS5eY466-mn3KpHqeLYWI1Gvuhi3c8Rl5_O6IHbZABiLd7RtfdRZdHrnj2GqKLsI45VMvV15yMte49mXX6lqdTF1TEFpRYRUdh9qCIVqwXQ7SthO1_W2PILr3c5mdSJHmDo62RtMYCa_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb17964484.mp4?token=GKHkE6u1dnSyOm1rwxaG6Rvb-inqJ0K1v-YdCOMr50JMKJlnDwwUvGQ0lyACPHzH428_lJMUvWacybrzEfBWh2zIE1wHZqeLZlhKraBViagqTeWgCTNHv0VZTuM9GLjaHaNrAAOiMpsijEzSjA6YepXZ3z7HJwIQIBLFW8BSmkpYZr6iyc19T2KtTTNxCn8dTM6XbSXfIjS5eY466-mn3KpHqeLYWI1Gvuhi3c8Rl5_O6IHbZABiLd7RtfdRZdHrnj2GqKLsI45VMvV15yMte49mXX6lqdTF1TEFpRYRUdh9qCIVqwXQ7SthO1_W2PILr3c5mdSJHmDo62RtMYCa_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
وضعیت خوان لاپورتا مدیرعامل باشگاه بارسلونا در روزهای اخیر بعد از پیدا کردن نفت زیر نیوکمپ
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/persiana_Soccer/22451" target="_blank">📅 09:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22450">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WeP0IiXNth1VGaH_bSd71MlqkQY4lG766PZDtxnZr4aA6s96JWsPDDcadM6R9ZTuiGXwnUswExrQrdejHppmuTXVxBPgQrxQdiwsXW9H7iv5NqHtLDdyDSNKMYcIu03jC0Q3No-GqGXsZqVzbNW5xbW18yZYJWNLFYfUv3uGQVQKGaQQm4jmHnvww2jZWkeyqCnyleBq7krShf61RcnR59bsZ80ukRRnNyaTINblWra47XIJWNsE0_JNHBon2U-vS1nCSCDspkMfQ-DBF74tLUE_qsy_O1w-0OO8PhR-6w1NQzEm6Zmohpox6YwG6Z33ZvLqeCVpk9qTv7z3rjnQDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/persiana_Soccer/22450" target="_blank">📅 01:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22448">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkwUTfyxclzSwA1EQhuwfW9K1gLtUx3n0iOntRZbVRn2I4nvut9td74aJPGUyt6JrvslqC8HwuJKfHG_TijPHzVSsYp8wj0X3yYGvJSl0OHGhELLon4te_3hRN57gulKQv50K5YIZheFcKlGxFsF_-ZHvpK6AlPqYjacQYwwwM4IMM9YYDYOGOUbmj4O2L_SQ6WLC9r1_LO0eKVJso-Tjz9WH4B0zxjsHu8jCPFwIeebIAtdhXmvklnnF4I5i9CesAeoR1TL7Rn763wXAZfjZC6vw2kp8R4eh_KU6ER6DshEtfRj090UOLb4jrAY7JVlivF0IP0ohbSCHiuCQS4WQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه تنها بازی مهم امروز؛
پایان فصل باشگاهی 2025/26 با فینال حساس لیگ قهرمانان اروپا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/persiana_Soccer/22448" target="_blank">📅 01:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22447">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/slsRlnx5akXn2EDuC3GUAG5qjQ7Jlyv0geISS1P3yaSV_nNv5myPcnEkU-h3rfVSjwqoFCX11Mo43EOaaFLg8gMRm_2gkWN_Ofq1iOciojHGqzeicZdOaMT3ANU9gqKyhjhmWsG-i24ZERhis2hFtpXwSRblDky5XcLy8of1ba3xAVFcQviKu5sqaIC_BeQCQzbmEIJNkBgkXbSZhfyOinGB6PO7M4jVXIfCuPhmU3bHR59SxXiNmtYMlGGg32Ds_G_I7YnmkopzqsKTnzelrqaz1eLxfiBVE-pLnynPLsDtwWkNS_iQ_wSaA2LTGoQEE1hNQLPAnzY4obvd2i6ycA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل دیدارهای دیروز؛
برد تیم‌های آسیایی در فاصله کمتر از دو هفته مانده به جام جهانی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/persiana_Soccer/22447" target="_blank">📅 01:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22446">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3s9Cgh0ZPmZzSVbSmi62KjJ0r2vHDHU3AFi7b2eo53ewWdUkO6vMGykDqT_Sjzs8EPddJ6k1Im_3tOtDdu9uPYJ5AxVqc5dPkQZrNDHogi20fLTtDyf-1E4MPeWCkpb_K4eLEcrYv4ZawBAZdfSuWL1vTd3AVE6seX2A-nal25UgvyD1HYzed7KH-wvUHy6ae72X_nPyGPWC4UACFTm6709FMtwIlXpUqS30b-Hbp548dxo0d_i7ct78mBEXCzOwegEXUSfnRFeB_CgdSQZZ1iIQXVnpQa6cGd5h3dinL87wrWzWhzCWYcOv0wduIaSWaznwXm_YU1gpXv1l8QwhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فواید پیاده روی رو ببینید؛
گشاد بازی رو کنار بزارید؛ فقط یه‌ساعت پیاده روی عادی میتونه بیشتر ازاون چیزیکه فکرش رو میکنی بدنت رو تغییر بده.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/22446" target="_blank">📅 01:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22445">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKnLteNg5L9iuYm67FiZpzyIOsbORAnO_-AC_8U6G-GEjC7BunmralIlXbplYs6uPfSpoMlnX-kHqTGXBOq24srDLqoqgtPSxEopMyI_-3QpFMULe50-Hzuo-TjMquBWVutOqILtIHHxuo8VZul3enaCrA2ZM7gIjtHQaDmSh3BWv25OKMPwOPjuUZNoMvI7snvYxT1uXXu0fiy3-v7pLWn2Xh0XtPsBFZmd3dXfFx8VAKIlMJWdObkdeviS7o8of6iaprI0nzs3GEtO28wrsUYJEGp6_ngeKGu5xJV_CFW9tcul37zeeqLTAGwUkZd3BPD4xniWlk_GqYtWoy1r3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بازی‌فوق‌العاده‌حساس‌وتماشایی فرداشب آرسنال - پاری‌سن ژرمن رو در آپارات اسپرت ببینید. عادل خان هم بازی رو گزارش میکنه. از صداوسیما هم یکی دو دیقه جلو تره. کلا سعی کنید هیچی از این سازمان مزخرف نبینید. لینکشو فرداشب براتون میزارم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/persiana_Soccer/22445" target="_blank">📅 01:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22444">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLkDCbaGUO017ZsujiMkyh1Zb3uERJrDGr4FZzfoiu0O1SXeE1XjKPKXz9oRsltie66U8jMfq3qkcnZfGoKNjnjJa0uS3LcoiybVR3WG9-157dVkQfYvb0r0ECMQ1lEKen0oGCRwNhYM81o-Nv6V8K0zbpQTccemVgzCIzuAWcEddkpwNf0O45O8P0FBevwtf_X0E0aaMHo7kTKTHR2f7CMsRbtL0cckf4WaplVaVu7VsB7KJ1UpeirQd_veG7qrETr7UfpluUxmh_BjQDAiSvpExBG5-fDmA9VcUFZDKCY-J-HfLLAfmez5ptObrGHGqJAvYPsbVNP0mGWmrsdUvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تاحالابدون‌واریزی‌روی فوتبالها شرط بستی؟!
🎉
500هزارتومن‌بونوس رایگان فقط با ثبت نام بدون هیچگونه واریزی!
😮
تنهاسایتیکه باعضویت بدو
ن
واریز
500,000 تومان شارژ
بی قیدو شرط
میده
#وینرو
هست
💰
👑
#معتبرترین
سایت ایرانی
⬇️
🌐
Winro.io
🌐
Winro.io
📱
کانال اخبار و هدایا
a8
🎁
📱
@winro_io</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/persiana_Soccer/22444" target="_blank">📅 01:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22443">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bA2mk9HvN7oyNhScsCeoZj5Sz1SnxZarDAbjvtopEIxlo0zMxSA0HTY8laK1G6EtDrvqbUKpadx_ul8whBxO57D-6EQUfoK-wCfSGLUBFWH0JQ5fOGLZmzoREYYR4jHGecVfghQPX5kGARAFI_YTMqDJNy3ObRLkW1iqapRJNGlsLX6PEfQjvj_ZIQn6HrDMuw9_mRXJuoA6p1ikvSAHVp0jXQDNY-K5W4sgdtR_9vYiCcdW99oId-9jMYU_kuVfqZut7VMl0o_2FzDkwRg0XMzhrvSMYZDlZY0tZAHE62dEP3YCH7Lz2DE_jkyGEvKI-na1sylOYLCsJxSYKtzDIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رومانو: آنتونیو رودیگر مدافع میانی رئال مادرید قرار داد خود را یک‌فصل دیگر با این تیم تمدید کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/persiana_Soccer/22443" target="_blank">📅 00:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22441">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IeCC26haCesUo6rx1Zas6nmmw3EdZ-ziy-LKk1bK6oHY3NL00Ha5hF-wJLfkomDcNY1L9qY4Caze_EN9J6TsMd36VjYK7fLAa1VEp7XbpBgXvSO5cE7GiYsbmFCPhoSaGNJ2d0YFLFWBNgd7F1OD04PGDQN_ZfKzSgRgI4U9srOxrk9_hAPtNgAHaN1eC0WrcNvRx4XMFSnTAaBnyZSXad6KHLSBpnm0r4T7ir7j_O1TDy-W22x9BZxQWApeBQ0bP4dq9S9cW_FVolV6OsHiWFeUo7NYrp0PzpbtJrQwwBTcH0GwBgdD-Emvx7KDxbsgWEsFJv9eam54130rPLr0OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uFgabF-o-udtLH9D3hIAEO4yW1Y7djEIEtKnUrUnUlV1nLgYmULJ9Ey3OnqItMVsv7PRgF3I4Js2-vB-0i4uvF2HKGiuX5EDRgGyfHarz8Ol-UG84nbneA1cKX2e1zzKkTm00dP-W7dTDIWqM3_3NWdDWmW3P9elQkIxdc8b5e92IUR4Xh2Tua5AziSKXV6XCIKIpiQL9Ak84PUn7bN6GrF4YwbmHyDfp_7rY3TP0F4YsVs2MTttsft9tmJ1GOK2ptzTN-HvVV2ib-uVIyjj-TUPT7Nj5P8NNuyOKnoCk3yHJXAPv-IQBDSK-mz4DEPqQyVQaiJZ6Zzuzulgwc95Kg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">▶️
هایلایتی‌از عملکرداستثنایی آنتونی گوردون فوق ستاره جدید بارسلونا در فصل گذشته رقابت ها.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/22441" target="_blank">📅 00:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22440">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFjgOX9vVHATKSfkTvyOQzgJeWVAoiz9cZkl_Igks6QjMQBVtHV9IOfHdSau8qOptJEtGe8EVZfk_FQz5gDbn_0Rg5Uu_dWdlSF5mkc5w5IC_pgD0S9h-PMDNYndKBeUiPrz6ydsAEA-SySOAibO2LvNA0EOzY8w-8ECBY-4X3nockSD1-eFvadctLOdFqCsJ0k25Qs7pjO3-XmF6ypP5OKl6KgjLybG8J8wbLHjIyAgoC6WXtMFz-okdHVw0wVoVw3anssOoAL7afHA9OH6MxOdBz-4NKv_kSleb1UsxdHK8GILpFGUEcZ5ElF70TKgsEUy6HAJPGb7vuO4xTRMLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ریکاردو ساپینتو سرمربی‌سابق‌استقلال‌که در روز های اخیر با عقد قراردادی به پافوس قبرس پیوست با این باشگاه قهرمان‌جام‌حدفی شد. از معروف ترین بازیکنان این تیم میتوان به داوید لوئیز مدافع سابق چلسی و آرسنال با اون موهای خوشکلش یاد کرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/persiana_Soccer/22440" target="_blank">📅 00:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22439">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwL56U5IWcqFyW4p8Ylt40AHaIEm6VZL2qEspmccFVsuTKojE7K6A_Fq4afrd_2IbQcwGYfUmg_yR-E0oRWHvC7NNH48_ecEQveCLTmrN-jLYeGwHrQrJgESiC3NZJKiYp0tBv3_c5yu6fAhFv3JkbploAioAGzLla5fY29ypzTyAZ4kgrxdwyYGg_wG4-GYkbn0DwKQKU3fsKibbvLU1qakaPf9TfBkffWGEN_-hqGpLeBhrXX1nv9fyrNbnsvykBWvUWsc0Zq2fEli-SjDYKjfeb3wSZO5Webd7Nqf0UOiVvkv05_q9AksSaJbSCnbrRIdMHLNc2p7qfcnyO6rmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کدبیس سه‌شبکه‌جذاب ماهواره‌ یاهست که بعد بالااومدن نیاز به‌واردکردن‌کدبیس دارند. اولش دکمه F1 میزنید بعدپشت‌بندش‌سه تا 3 بعدش یه صفحه میاد که باید کدبیس رو وارد کنی:  کدبیس شبکه جام جهانی HD:  BISS:2585AB552585CD77  کدبیس شبکه ورزش تاجیک HD: BISS:03A01BBE20C16D4E…</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/22439" target="_blank">📅 21:24 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22438">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHWQqevTT1jCmTRzMt7TDYwS36FOj0SxWfjfBy-15x9OkzOHQ16hNUOr3BnBOmh4HmLFgCU9jIaP7fmbiw6AvD-RTf1vzI9trI-PM-6GUYbfToEkOTXJgjr3nv8eUo6JXmYZSqks7VO_GTykXxhCogtcHN-ihi8K9Ev-n-zqH3eozpFrmFi3zxid2IzyG_tkRDBlOu0TV5E95snVtiE2a44pjbhU1xylIuK4Fxmr_Lt8uhjlQbs4HQNiHey82tnCk9-OmTtnekFRU9azuFHEBOoTk9cAn015yDx16ieSgdZkAVnihdfucaKuPgyQplpE0mcmyx0IPn-Qobn9TqF0FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛ ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/22438" target="_blank">📅 21:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22437">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✅
تیم‌امیرقلعه‌نویی مقابل تیم دوم و ناقص گامبیا که در رتبه 116 ام جهان قرار داره سه - یک بازی رو برد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/22437" target="_blank">📅 20:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22436">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cW77n8e_ZwS-Pb2KuC29uSKvyAu0hp6d2T_VF-qV4f_GrkKtQ-WRAmEOWodb3W4IcI-vHKLLk_gfulvEZmNYZzqh8y3qiOpw4naYUSD6MP17Hhe8w8DCO_bsb5qS79jic_aM0UXWZ5dhHG4f8Iy3U63JvxRTur3T2DzM64vGJG-DQOHrRPi00OWsbLbCl46qT3kZzP4poDx15tXqf0LWkmpeXzajVhG_BjNQEvneUiz6TZxx0rVsETj5hGcXdUaK6JewE3eFaN3QklxR6YCZOXNHJEAcFKTgGYOZRW1JOHIVYiBaF5vcYrSWgVCFgZ_IGRkAjZOb5PaU3sFmsTKwLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات|سران باشگاه منچستریونایتد به درخواست مایکل کریک سرمربی جوان خود با ارائه پیشنهادی 100 میلیون یورویی بدنبال جذب فرمین لوپز ستاره اسپانیایی باشگاه بارسلوناست.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/22436" target="_blank">📅 20:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22435">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🏆
کار گرافیکی تماشایی از قهرمانان جام‌ جهانی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/22435" target="_blank">📅 20:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22432">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RaKsqDwJasLNPJqlVTR4JVElWmdZaJPNZVtfnjNd-iob7xzN3alBy0wrMoDeS7okjDOIsADAlD6DuI79Rsol-6FOG3Aj5giDscYnHxjdC-FtHFBNI1ZTzDPVCv_qsds2embHC-YI8H4e8ll_90v6g92SzACsQXqia4GyaenzIg6KWKonwESyptaatooLzxOJBiNAtr8VNxAlL2YtRMPObyWGVLn-UcmYvs1W6C9bPQSTRUt7ykCkX5dX-X4p5xePzlBqr80hF-L8zz2eqAnrHPj4t5QDKiCCDoqLncF_Aao__NeQWcb15o4736H9yAAEvpcdAqPSJ3xJGCH7yvaZDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
بیانیه عجیب اتلتیکو علیه بارسا: «هیر وی گو! ما یک فکس به همراه پیشنهاد خود به بارسلونا ارسال کرده‌ایم: ۴ بلیط برای کنسرت فردای گروه «بد بانی»، اشتراک سالانه ABC و یک کیسه تخمه آفتابگردان. مشتاقانه منتظر پاسخ هستیم تا «اعلامیه رسمی» را آماده کنیم.
⚪️
…</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/22432" target="_blank">📅 19:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22431">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwjgUcFSFOFPzKQrM-yClfi2ak1tvJKKlytZ-2sRKXnolqtfYnUER90pIhKWVY_VKq6DOAAbq81-_5PcnC_9s6P0Mh4RaV48JCrhUMUo9KOPPEn9k7ULDMpkeWHiGnmeOmF4MxsQTTQFqNvue4T9ahZ0rJlXadqKRIET665V7InUMfaHOTvnoRtRYC2KSqOqaut6agLXCTy5_thAw82b82_rwd0odpBjsHXq7R_iCAg7lg5vuXYcS1HqASo1mQuMt3-75DcXtVFt9U9XZ8G_3T0_0A7PKfDwTjRqn5ft_yg9dY815hyRwg4ddqMmER3dUzmWuSvBcB0Bdyy_g0gCmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
بیانیه عجیب اتلتیکو علیه بارسا:
«هیر وی گو! ما یک فکس به همراه پیشنهاد خود به بارسلونا ارسال کرده‌ایم: ۴ بلیط برای کنسرت فردای گروه «بد بانی»، اشتراک سالانه ABC و یک کیسه تخمه آفتابگردان. مشتاقانه منتظر پاسخ هستیم تا «اعلامیه رسمی» را آماده کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/22431" target="_blank">📅 19:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22430">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgBrESRFP9q5GIeTdEOGNqn6sTDoKUlXBqEH0VZejMQocHJv0d740VvfeaH9rIVIDos8IyHIMz4Pw01xWBECT9f6eWkOFYZ57yWZGVNhO32tUJaOpKFXddVdiKXkTmdGOwToTsAGaXVNYbrsStZmHbtA4eONwYyg0A-Hn3AixAj1NlnqddZXK8NygGmcxixmB7TfpN5aU6DP7TlrR3zZuw0fuRmYFLV-KZ32AeQu2RTN3RWhijZzuUZaE876Hex3Bp7FAQ9mkzP7-1t2cxR-c5AjT2GlUtULgYnehh6PoP60QXl2hHxq85PskrX4OCri4fTTufalSnzM9RspGpXNgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخرین‌اخبار منتشر شده؛ باشگاه بارسا طی ساعات آینده پیشنهاد برگ ریزون 135 میلیون یورو برای جذب خولیان آلوارز به اتلتیکو ارائه خواهد کرد و این بار این باشگاه با این آفر موافقت خواهد کرد و این انتقال رسما انجام خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/22430" target="_blank">📅 19:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22429">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7qVMwCp7dABu3R1AEFPC0jamSJDVlFOv3f85jGIuhyJrRdViiUOZEyd07rtgmtolfTd0Conm5tWvI_dzYWJbvW4LuymOi-nMgwowgtP59_buWHp5Q_0MdHPhxAPMYZdh1b-JN45zkVjcxbRyx7D2f98Yr8YGRY1lrbjwcTHP9QtwKvXB-tkn9sRSL-aKBW5mH03VoCgzdkJQDjhBIa0En9izrt_JcKnmBJCURVOvF0-Q4dneqZdiyACYsYYKakfU6uZ5f1b0OfwISazKf6SN5TyXecfyXe-eQsEThDRzQTrO1AiOonEkb1j-qJAnmdjf4i3b_58BqrJAWr2V9cLsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام ایجنت رامین رضاییان؛ ستاره ملی پوش استقلال که نیم‌فصل دوم به فولاد پیوسته بود برای فصل اینده به جمع آبی‌ها باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22429" target="_blank">📅 17:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22428">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e99804290.mp4?token=T4awkiHBjVC8NnM73lRoh7l7cvNALWjkoRo_NhbB6uK6O8UFk0PfmFM47QBaoQPLNgGkrcsuNLtztOuRcCrVUQgmsBNjCvh06iqhA9DtohZZUrOCtqYeVYYjnk5XoPiyuqNbo57e9qgBKHPk-y2FhCMbRjNXRL2fGL5w4VHa_4jLGO0O80yXSfLU6wlRWpzJyxihssv86D0oHJjY3BZygN_3m_AxQyTKNGSQn_GTQ-gW5xw_YPdtRO8PyucSSW4TLjGg02xcI-CSQfqBwmQiNzSmV2D_IfcSr3NZPfRpdOSrlMoYU27wt6bFFz8X9xG33S6PqhCUoWUJfm2aD-4agQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e99804290.mp4?token=T4awkiHBjVC8NnM73lRoh7l7cvNALWjkoRo_NhbB6uK6O8UFk0PfmFM47QBaoQPLNgGkrcsuNLtztOuRcCrVUQgmsBNjCvh06iqhA9DtohZZUrOCtqYeVYYjnk5XoPiyuqNbo57e9qgBKHPk-y2FhCMbRjNXRL2fGL5w4VHa_4jLGO0O80yXSfLU6wlRWpzJyxihssv86D0oHJjY3BZygN_3m_AxQyTKNGSQn_GTQ-gW5xw_YPdtRO8PyucSSW4TLjGg02xcI-CSQfqBwmQiNzSmV2D_IfcSr3NZPfRpdOSrlMoYU27wt6bFFz8X9xG33S6PqhCUoWUJfm2aD-4agQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
گل‌تماشایی هریسون رید بازیکن‌فولام به لیورپول به‌ عنوان بهترین گل فصل لیگ جزیره انتخاب شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/22428" target="_blank">📅 16:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22427">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsNPDERe-6HhVbcImpnQOs86DRNEDnLy4SuB611GEG8j7ibsgyQYHs82tcJpHuuT5mwVEeY0FL4AEt6J_ph93-gH-EjKlxdXswLWdJNUHR-p-z9_IK6kldzTJ30vUQ9cg1uWF9GXJ3IFmJ96NqovIy8KY2glF-kc7LHN6FKxozkE2K_WVbzdxpTla7xxxn-Mwkno2gd1YsQbR_YM7SQR45RflrsgIoW-AMTc0rW1F2IVn46bbNarui6gUDCGzTybBaAeSNd5iv88fylXMAiC4qxKRSrw9RdEzg1_WUN0CydPW7ZgzM-zemwBZ1pMewecQZH-qrrNPzdIHJBlf965Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ خولیان آلوارز به‌مدیران اتلتیکو اعلام کرده با بارسا به توافق رسیده و دیگر انگیزه‌ای برای ماندن در این تیم نداره. اتلتیکو حدود 150 میلیون یورو برای فروش این بازیکن از بارسا میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/22427" target="_blank">📅 16:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22426">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBrd6wfgM1mT-JfHt986eUr_FekfkunGY1u_F7xMjBR8osUYOWPJDMSfuIx5oWjvY3hvj3Rd5hYlg_g-0GwnbzC8Mhb0smqKnv_9DpM2u6XcdgFh5hd9OzgLiKOvUJ5oQOx-Dd8BEAe_6EiZhb7uru_8Ezh3RfdXiw4oZTJQXRptmdeMiDES_RDguj1-PsLlFRxEQbfch29yhEyQyfzr5krf2nBvIGY13vUFZLiNJF5oj3QbHPcsaQY3zn45dMEkqc2v57bdp5MVdMxM0gcqjryxESajnfmIGountolJchOODcT3ZRVFWeZoEiFhxTIG9poMBCXw6rx8-mew7pEH2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رسانه پرتغالی آبولا هم مدعی شده که باشگاه بارسا در حال نهایی کردن عقد قرارداد دو ساله با برنارد سیلوا با دستمزد سالانه 8 میلیون یوروعه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/22426" target="_blank">📅 16:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22425">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ccdf1c58d.mp4?token=b-jxRSpHuXpM_6SOcY4lfN0HSVsirO6s0Laqsze8X9Ml7tizh9SBFMqwdaAY9SFxnR7knmsvSqirLKRKgSqwxVuvIDX_gkT1EeeUIlUT2NY5FHt4FGSyvcYbXBsKdbkCUPSMLDzoDifOPBTh2LFWv6_X6onPOkP7UJvVlqx3dmQR7TYSKQlFCnlNyn8p216ASugdcucF-yqzJhlVjB8dt9QFyLzu6papcTb7_pKGSwXXDSc33mWlMUgDv-XGdc0g7Qqadh-kqquKZO_wNayFp8FPV8WixdWI5fFn756wzSOHrnfbywXwz7d7YqkRVoUVojrQn3IXb7mOMoweHYq82oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ccdf1c58d.mp4?token=b-jxRSpHuXpM_6SOcY4lfN0HSVsirO6s0Laqsze8X9Ml7tizh9SBFMqwdaAY9SFxnR7knmsvSqirLKRKgSqwxVuvIDX_gkT1EeeUIlUT2NY5FHt4FGSyvcYbXBsKdbkCUPSMLDzoDifOPBTh2LFWv6_X6onPOkP7UJvVlqx3dmQR7TYSKQlFCnlNyn8p216ASugdcucF-yqzJhlVjB8dt9QFyLzu6papcTb7_pKGSwXXDSc33mWlMUgDv-XGdc0g7Qqadh-kqquKZO_wNayFp8FPV8WixdWI5fFn756wzSOHrnfbywXwz7d7YqkRVoUVojrQn3IXb7mOMoweHYq82oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌که‌باشگاه ماخاچ قلعه روسیه از عملکرد درخشان محمد جواد حسین نژاد ستاره ایرانی خود منتشر کرد. حسین نژاد تنها یک فصل از قراردادش با این باشگاه روسی باقی مانده. درصورت باز شدن پنجره آبی‌ها مدیران این باشگاه تهرانی برای جذب قطعی این‌فوق ستاره 23 ساله اقدام خواهندکرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22425" target="_blank">📅 15:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22424">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHkZE4Vrc6Mf2PYFRK260rshwUXmMHerr67CuDAp9XxmBNxFi1wSj4yXvoZhj7BlMcK_GsQ1yZPjl2P_F9hx97hnRJolGGesvOTOjzd8M4KY4kLEQg4jixCQgRYQjb3k64x9AYwIZOCYoYBqrSuhwFu3kS5laJHQsgLP5gIsGTPIamTqEq4OVBdN9BPqPU-l5WLNyndLgTRjBANryUghScM3wc_JXhI7Q5tbEVKcSJ62ixKjM0czp7tOAhxFtfJFGCXSbPJ5Y4w9lhF6O6z-nV0uPTmI9krirrC9esBczy93rMW1vKMFgh47-hmHHd8SAFMgmU88IjrQk6CSQlwDVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات؛ رسانه مارکا: رودری ستاره اسپانیایی منچسترسیتی میخواد از جمع سیتیزن ها جدا شه و باقراردادی 4 ساله راهی رئال مادرید شه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22424" target="_blank">📅 14:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22423">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OA2QeNw6AQYtn59xWNq8LZfiFn2I-osK2tHQRtVacn_vgHrBRO8IH4DshTc2N3DrKMDK83XZW8mkPBkJMiH1gH25sp9HAVhFDJi1Wk8sfPyH4enJOMSlARiRfU4h3sUjxxVjElbObBs1B_Z9y4J9kTgbnOvAceGlT5vzh1qISIEPjCFhZbpK__6BfcWL1joUbzwkshfU0bET9pUmDUW0qmbUfxnKlgK5_UAZtPg_DuFhUhShrHrdY5j5fhKCarPjdk2RDflZO_-vNXlht9bLFJln9nsSZCMgjqufcYhqU1-EF3AAPB_iPZzF3sl0Gl7QJwiCpM9ljzqSwuD62wqrpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جرارد رومرو: یوشکو گواردیول مدافع سیتی نیز همچون خولیان آلوارز در خواست جدایی از منچستر سیتی کرده. فلیک عملا با تماس هاش داره راه انتقال ستاره‌های مدنظر خود به نیوکمپ رو هموار میکنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/22423" target="_blank">📅 14:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22422">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/do4m45Yt3X5m91rb3bqMPtd-FgRJjrwmmvppRunJOebxfp_UNyQ3xYV0TBWKtolNwxHtlfdUFvmsmkll00EA9fgPEE7GerBwhS43IVwu68HJSmjoPk9fL0qom0ET3safwaaM8judu67LYnni2RxX6ELaKd1aK3deApB_8T-61R-VGIQU1Vr4pQ54uG1K6okPlswqvR75_EFJq_CIcCF6sR7c0E6csWVWevlxGPjpTaBVrx77cOMO4FR-NBT3fykO6t2V5BD84unfutcFT040lD52KwCkspT_FLZhbk3v1yxtrUZhzQTJtkOFYnuTjhS2BRmhvwATM2jHmeG_cONZsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌انتقالات|ادعای‌رسانه‌های‌انگلیسی: یوشکو گواردیول مدافع 24 ساله منچستر سیتی هدف بعدی سران بارسا بعدِ نهایی کردن قرارداد خولیات آلوارزه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/22422" target="_blank">📅 13:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22421">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5jpgXcipW6z4Vwg4OAETnl67lundILyPe8hYIcXLj4xOzr6Yj--9avJLLpygv130LfkVej-M3ghLlvZldNSPG1wYHhf_9gu6Su63zIHOS1Qs9kIzyKnSwy7A_5udfme49vEka8tpdBhyvPWWWXCugxeDDrQvgFdWHBN1yvnzrTeeVCFEKUdC2NQ5FrLzZ7JyBlsXT7PGPowTdfhjum8l_JAXchchL0NsEUz0MSNaf2BHOxDcg8dxRs0IpR3vznC6Ur3_xcWyVpF225K8JdIQ1qqqTSUIvl73iBAo75R0CtTYFsGvPdoy3eiYjjvpHj6p1wCcGriGNnEWq2PbRrpIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات؛ رسانه مارکا: رودری ستاره اسپانیایی منچسترسیتی میخواد از جمع سیتیزن ها جدا شه و باقراردادی 4 ساله راهی رئال مادرید شه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/22421" target="_blank">📅 13:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22420">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jq4b441M34tyELi16tz4F-N3OHz2lzWN-OK3j8ncDJ8TQcA9AzdvkP5ad17YLaxZf7y1KX8EcWswUseL1uqExrWLpSZNfSr5B7SE3E2ItPDK5OtFXpa_KvfkoBWC51lE1e1Brx0lg7VDAf6PRmigpv1um96Sod9JAF_2YJ0evzFHGZu2j5-CzQgErhmqiFf9a8cixPaRUCvnKmDAfUwfnCAJ3Pnkpc-zsuT1I_Rc8R5pgj87uqDUOlVUbpjagr1m7J-yGX0qyGSqNDaKdmLSCHQ_a5ndPTib7DNlLZicy6KUJMjMkyhWRX5ULhgLmd3XykIw41hq-0d-6qquJTCc5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد... یاسر آسانی ستاره آلبانیایی استقلال امروز در تماس با علی تاجرنیا اعلام کرده که فصل آینده رقابت ها نیز در تیم استقلال خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/22420" target="_blank">📅 12:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22419">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uim-hmQB83m5MwaH5enr-yZJVVTh3gmBOfoTUZ_ELE6RcJIE84yFbcwVDj-LKo-fBDSqKEskSiokH2Ed-AqoFO9M3BtrXcDFO7Zt6UNbGO9hnal2EtrnMadc5zUs2W_0Xuc7cTwmTEY6XaZ6uKRSnjymsh24HoKEvksMTEFm9WadL2NEdtNW-EYup4_w88nuMt5LPq_GdrSHQNXx1izO0rlo09L2KyMdb6sMH96_U9mFf3jXLgelIw8g5p8O6X-0bBGDuM1A-ATU5HGgUU2eLVf9D0r4EDEZlgfJmUf18hbCYNcxWaQ0ClVukip-kzBIt-fkXdwLP-rWXpxcxCrgRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ خولیان آلوارز به‌مدیران اتلتیکو اعلام کرده با بارسا به توافق رسیده و دیگر انگیزه‌ای برای ماندن در این تیم نداره. اتلتیکو حدود 150 میلیون یورو برای فروش این بازیکن از بارسا میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/22419" target="_blank">📅 12:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22418">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgtAnZQPQewlYS7FFL1GShSrdfmWQjinP2edYd-DYOdXRtu6wCYlIZcAR-sVwIoCXUHVuW0IY_6ajftBCy1Jpyztg9xNNaGazXSj8dkCDf3kvoqSWtjGNviBqdCRHW8bGf1gCyD1dnxTdGHiVAJu4dK_gMPq4-H_FQtnccM8khFqfosjcbIWSRudhMoDcjNK92Pv7QLJ6L2cRZxjUxQvmITYKkbGn1mALfJ3LE8dcDgmMTvptgcZ2TzYc-4PYlS_uTiSITLF0oBOGgExHundvl0WvfrIx5ZZ3DssBVHV7weNhmiTDCgpBRAtqdHirA6d9koCOM99XFzsJ5cdLSAblA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇪🇺
به‌مناسبت فینال لیگ‌قهرمانان اروپا نگاهی بر ۱۴ بازی گذشته PSG مقابل انگلیسی‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/22418" target="_blank">📅 12:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22417">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljNFJyWM0pA_KOFiVM7wMmB2RupVnoT_pbUuTvBh3_xVheKAuIfcZgz66dmiyhTYGjeaQIAKd3Cc95WLNCTTOCkb5lbE8UfBRRgTFyd2I0jB7H-mylMF-pdtnndffSang8l_0FChZIL0wiqwEN349TBRYv2U-_Ar3TQHZIzDZTwpBkAztdpf01awUTZILFySpXb0uiMJC2ipRALR2_D6M64fUrA2TchvyeScfKjNupCWHmjeN17FDfwKgXDP8tHlzNIIoVvdOwtvL4Hoz_cPdWxpDLJYINDwoJsMsqpI9NruZUdy7eVEe6a0pnDDJGMOIzKX813BOEtL5CRsmHbYHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات
|کوناته مدافع‌ فرانسوی لیورپول به‌سران این‌باشگاه اعلام کرده که پس از جام‌جهانی از جمع شاگردان اسلوت جدا میشه. از رئال‌ مادرید به عنوان مقصد احتمالی این بازیکن یاد می‌شود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/22417" target="_blank">📅 11:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22416">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDa0Yf5UX0v33THSh6IcxGgb9JsJkBLvfFQ9EWDS_AQ_mDJcY9Nl0Wq3bD1zlZL60yEccnH6vfjcCv6WoMap4aTUOoNnTq36FQ5Ppmx-l58diD-mqA64s1CLhDgkuivt1LNe9xY6V9VIqGwOhmUk9ecyqfshvXyF2aWtqrqHa8eUyHeQv2C3W0k0BmqwcgUC43hQWBEgx6tLrNwSifACJ3m-FvXOiuWcNzdGkzyd7EzPNemeYLits6wbk9wjbDeZniW7813xelNZUeiKmPb_Y5KKoRivHQ0YBIpJmSrI-sfkKK-CrN23kz6Zbf9wM0-RIKsZYJvjhDc_Judr5UDqSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: باشگاه‌بارسابعداز جذب آنتونی گوردون و خولیان الوارز باز هم خرید خواهد داشت. هانسی فلیک امروزشخصا با آلوارز تماس گرفته و به او اعلام کرده برای فصل بعد روش حساب کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/22416" target="_blank">📅 11:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22415">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjnxXaREnzy3rjh4eNBjzGlmxUD0klK_iGJIG4yEX1AEOzEKQSofI4Ec3y5ldt-_MS_kHWZZ0CTgcLoh08q-kHoYL6U1vGwXuUseaAHXbGAwudM_FijmkFvlFOsdftokMnfwzhTQhUZTUMBB12jnMLu19mB9hEDkqn1-V3NBNyHUUl8EYyvTFjzmNsck-gv3Ok0xc3nayCGP_Wi8-BeEvNQBaJzNhzMPSBXMrcJqYQEVSytbR8JO1cHD1t0biB9azllrbjsCiyokcf5S-xg2GQaGcvSuoGLTCtvxQZuyzsFFugSORjqQzurtx4j1-Cmgwoc6FwylX-uS_92cNPr7qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکل اولیسه، انزوفرناندز، ویتیتیا و ارلینگ هالند چهار هدف جذاب انریکه ریکلمه درصورت انتخاب بعنوان رئیس‌باشگاه رئال مادرید؛ انتخابات ریاست باشگاه رئال‌مادرید روزیکشنبه 17 خردادماه در تالار بسکتبال رئال‌ مادرید برگزار خواهد شد... فلورنتینو پرز و انریکه ریکلمه…</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/22415" target="_blank">📅 11:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22414">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DT7s5HO12TUkbw8DN66cHcPK7snLxGa4KzBkepkYqh2-T4BNL0HtLcwE2Ukkko0MbUR7GIM767U-yjeNZ2fKeCaTRTA-R5ebRcuCin9cHnZygsWlo0kJ8BnYyiQ_pG5fo7xu0EDd03BlVKrMdCMzAsr4QLCzFk51QNwV8P6frgJw2aKCt8xNaslVRk0fEHH1LJkkqydIIryNTDnEP2BXZV162opwPPJ7Q7cjIs3hUHTha9tc4Fz9W2oV9d3QfTm6i7ds7HplSc0sddroTdAk33CmhaXdJiUYswLRXX8TR9cElSFxaF9VmM5zKj5xzWIiEmoZnLbLWmpreww2lD58Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه جذاب عملکرد ژاوی هرناندز و زین الدین زیدان دو اسطوره تاریخ دوتیم بارسا و رئال مادرید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/22414" target="_blank">📅 11:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22412">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOhf9BMT0742JyIcoYlJ9igmz7aUo2CxwP8BMndglCG-HYOsLuGNkXwikzd28dtuLwiPgEk1e6xAS9u4gTyylE2eCrdpa05-21ne0nYTCASMrx5TAi8x2rVWVWoU0jkGoSe6njoYUl37DQ73C2n_UWCrvscdVI_QOhW9p0sO1V7X7g4pR75FbijmTlTYcZn2E7b_HCck1k4KnOPylowBxK1gCC6qWakvOqEaqYIjNUrCusaD_9eclLwC6iJJoWIvrrTEr8fCZVcrPtaHYyvX9-ZRCFbvr15qgs1s9WC3eh1QGkO4EuTnlkNDZrkS9DAgO60doJdvIREMt4n21KnfjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
برخی رسانه‌‌های عربستانی؛
خبر از مذاکرات مثبت الاتحادی‌ها بانماینده یورگن‌کلوپ برای پذیرفتن هدایت طلایی پوشان جده در فصل‌آینده میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/22412" target="_blank">📅 11:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22410">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ضد حمله‌ و بیلد‌آپ های تیم رئال‌مادرید؛ طوری که زین‌الدین زیدان با رئال بر اروپا حکمرانی کرد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/22410" target="_blank">📅 10:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22409">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c001aed77e.mp4?token=JP6N-XimTclLmfbybgC9B83PjLZsP1rezNYz_Zx_qx0wCF61PLNkdV0GV8-1UX4OnnmwCrLAkGBGju6T1XDw2OS8qjvTE91m8dcsIETAPUo8QNL39G_86l6xRhlu0metHXhC65py6DJBddituQhPFOkLgoIknPFMTrzTLOrV-4qSgO8N5eQCGVYwkbjx_yZa2wBbmewj4CQ3vWeTvGhZFze3IiNgmbVZzPsRTLE8RNlVT0BBROcbjqJtV3dP1WGzEMeshRG5k10ZZwNGamg2XZ54gieLAIswwXUVUtJ2bThcy3xPcjV_Mjkd1XrQsLg0Gpe2s6YKFlMbFJU_0_YX8FNPyiUcqxrZlaSVWMyoPePfQeuIJfE1H988Erx6to88xQB4ACTRV4PU0K-2AChEChbm3I427gKXOkfdHX6Sfd76JbAvwug8hot9OIWcMJgd1wIFJQKvEkx5RPX3Myi1tH9eXmkf6cXJgleVR0QskF9VZ2mhN3E5TN4orecIOPRX9yQEfYah9Gs-s4ELusQi1w9xsJiDrz_u9Eg8WJfcSArTvFeGBlyhowMp-hwQ-tw74KYv-Riji5D6xQietZDAhjuY4Xp3OvRHitQDdiz6ZdIGHAFUIspnK-S7ufCDiSSHP2KlE-KO-3t0JhaeAbrlhakGiVGx6Yor6yEG9RvUzE4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c001aed77e.mp4?token=JP6N-XimTclLmfbybgC9B83PjLZsP1rezNYz_Zx_qx0wCF61PLNkdV0GV8-1UX4OnnmwCrLAkGBGju6T1XDw2OS8qjvTE91m8dcsIETAPUo8QNL39G_86l6xRhlu0metHXhC65py6DJBddituQhPFOkLgoIknPFMTrzTLOrV-4qSgO8N5eQCGVYwkbjx_yZa2wBbmewj4CQ3vWeTvGhZFze3IiNgmbVZzPsRTLE8RNlVT0BBROcbjqJtV3dP1WGzEMeshRG5k10ZZwNGamg2XZ54gieLAIswwXUVUtJ2bThcy3xPcjV_Mjkd1XrQsLg0Gpe2s6YKFlMbFJU_0_YX8FNPyiUcqxrZlaSVWMyoPePfQeuIJfE1H988Erx6to88xQB4ACTRV4PU0K-2AChEChbm3I427gKXOkfdHX6Sfd76JbAvwug8hot9OIWcMJgd1wIFJQKvEkx5RPX3Myi1tH9eXmkf6cXJgleVR0QskF9VZ2mhN3E5TN4orecIOPRX9yQEfYah9Gs-s4ELusQi1w9xsJiDrz_u9Eg8WJfcSArTvFeGBlyhowMp-hwQ-tw74KYv-Riji5D6xQietZDAhjuY4Xp3OvRHitQDdiz6ZdIGHAFUIspnK-S7ufCDiSSHP2KlE-KO-3t0JhaeAbrlhakGiVGx6Yor6yEG9RvUzE4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وویچک شزنی دروازه‌بان 36 ساله و لهستانی تیم بارسلونا، بعد از ۲ پاکت سیگار و مقداری آب...
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/22409" target="_blank">📅 10:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22408">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3294ce3a0b.mp4?token=dIWNYjzXO8Nb4x5gQ8MS1Q4FKd1ky4YMJLRF8xxXp8GU8SCX0jCCOUXDomUWlwDfR3W_p4bCpQhuX16zvvJGgajx5K6o2fwMkUahPo2_UJIpimZAtsdYDtcf66jMuHZGjVC0czwPCkeHXFTUOBJNLmdZNRK40U240HdM6yVtfo8gzYqgBEKCi6jIyZKKNi81dW30JcO1M5d3M2n_j0p7kNMPblX3RX3H5oNIQkBulKIKILW0QujJtRQheQsUbbf-rYfrfsZoRs6ZCKRrJHAl4Bg1aq2MOjuYnmqWr1fD_TYrvslDfwPn1w5CAYsFae6trMmkqfP_SpS1jGHlZ_zvWbs9pLdvIyZjwERf9r2Yr4orts3H_bPypEAm6M8dxcntMTkWlO_Q4OpxZRn8PQpnySlU9fZQ31cbbYlDIBgrUqNGegjtKAsIeCYmHs9_Q7pcO88DOY208vCry6stEZraqAkFjKX7o0vjmTDUsGeXQnk_0iX16vssFGDD6Q2GqWbToEO6rj8R1Hlj8tIfFP4nvPYZiFFSLeZChuSfsT01-kWCIfwpVo_ZPW_jWPF3Rr7Ra-x5usvON3JwJmYRcBdjCmbAZP8YC9TCtugaUFEv4rZBAjjLTw4Wi0hZN0p6saQQjNz51Wxe-MD0dLg8uuOtg29nIo8qk5Fc5UIH_G_eeLY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3294ce3a0b.mp4?token=dIWNYjzXO8Nb4x5gQ8MS1Q4FKd1ky4YMJLRF8xxXp8GU8SCX0jCCOUXDomUWlwDfR3W_p4bCpQhuX16zvvJGgajx5K6o2fwMkUahPo2_UJIpimZAtsdYDtcf66jMuHZGjVC0czwPCkeHXFTUOBJNLmdZNRK40U240HdM6yVtfo8gzYqgBEKCi6jIyZKKNi81dW30JcO1M5d3M2n_j0p7kNMPblX3RX3H5oNIQkBulKIKILW0QujJtRQheQsUbbf-rYfrfsZoRs6ZCKRrJHAl4Bg1aq2MOjuYnmqWr1fD_TYrvslDfwPn1w5CAYsFae6trMmkqfP_SpS1jGHlZ_zvWbs9pLdvIyZjwERf9r2Yr4orts3H_bPypEAm6M8dxcntMTkWlO_Q4OpxZRn8PQpnySlU9fZQ31cbbYlDIBgrUqNGegjtKAsIeCYmHs9_Q7pcO88DOY208vCry6stEZraqAkFjKX7o0vjmTDUsGeXQnk_0iX16vssFGDD6Q2GqWbToEO6rj8R1Hlj8tIfFP4nvPYZiFFSLeZChuSfsT01-kWCIfwpVo_ZPW_jWPF3Rr7Ra-x5usvON3JwJmYRcBdjCmbAZP8YC9TCtugaUFEv4rZBAjjLTw4Wi0hZN0p6saQQjNz51Wxe-MD0dLg8uuOtg29nIo8qk5Fc5UIH_G_eeLY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یکی از مهم ترین دلایل‌موفقیت انریکه و PSG
: اون برای بازیکن‌هاش‌بجای یک پاداش بزرگ در پایان بازی، پاداش‌روبه‌بخش‌های کوچک تقسیم کرده: مثلا هر پرس = هر موفقیت = یک پاداش عصبی کوچک (دوپامین). نتیجه: انگیزه پایدار در طول بازی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/22408" target="_blank">📅 09:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22407">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc6b58323b.mp4?token=GlsLnNqzQVkh8EZyHvEpv1OSEb5oH-0kWuczsZzelB3KDXvyEJQTs7Dd8kaLMD_G69s1doaYODx9hwOeRcvxQe0h7WbtR0KQQB2ukrMtuAMFGCzlqZxym4uUfwaW--QER8XIH0hbl39DCNKPhoNCd-Vf7veo2QHz7HEHaize5mYMd0unJIESdHdUvafl_M0NIAH4Tds3AmJMsizn7YlWoZ5reCWcY14KXNh3OFkosDI6z2QqR_xNU_LE4j_wuPZGW1hJ6XPM5MWtGLb2VpBKllurvzWQ8NqBo6P83rCgDGMqNgCqPF8RGN5FHUh2gy2Fuo081yJLT-UpzMjny0n2fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc6b58323b.mp4?token=GlsLnNqzQVkh8EZyHvEpv1OSEb5oH-0kWuczsZzelB3KDXvyEJQTs7Dd8kaLMD_G69s1doaYODx9hwOeRcvxQe0h7WbtR0KQQB2ukrMtuAMFGCzlqZxym4uUfwaW--QER8XIH0hbl39DCNKPhoNCd-Vf7veo2QHz7HEHaize5mYMd0unJIESdHdUvafl_M0NIAH4Tds3AmJMsizn7YlWoZ5reCWcY14KXNh3OFkosDI6z2QqR_xNU_LE4j_wuPZGW1hJ6XPM5MWtGLb2VpBKllurvzWQ8NqBo6P83rCgDGMqNgCqPF8RGN5FHUh2gy2Fuo081yJLT-UpzMjny0n2fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
وضعیت شنبه:
آرسنال با یک گل مقابل پاری‌ سن ژرمن پیش میفته؛ داوید رایا گلر ارسنال  دقیقه 34:
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/22407" target="_blank">📅 09:35 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22406">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8j7lcbDamyAitgfrvvBP9Q3EKr45-RO2_0JzvR__h8-xomCbaPfKZUwoQUgiQzvP2RIsRBV3TLocpV2giG9nkfeLT2Yk6UmI2kDcNe491vUyRP8ggBJGoqpGWWOd4NAuBR1tPGWLIjdVh6aQ6MkWndG8wbzujxkDUzhDRsdQ1L4iXNyLMCjbaqUjWZp5FNJx4hYX6xlq8Lfhl_Tnz9R8CXtD1DIC6RM7wp-iIVQ_niY6Uab39PuBmThgPFJFhG9SfBu0XIyF03AGf4uQ4u_ts_qvr4vUcm1boRe16zqKmgwGWOb5LaLSFeZTOuYVTy5iMu_-8qVCaTlHC_OxfhXLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ خولیان آلوارز به‌مدیران اتلتیکو اعلام کرده با بارسا به توافق رسیده و دیگر انگیزه‌ای برای ماندن در این تیم نداره. اتلتیکو حدود 150 میلیون یورو برای فروش این بازیکن از بارسا میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/22406" target="_blank">📅 09:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22405">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKVJ6e4XFxdGQ5bO0UA6FzuGRTZp98KXlNC5T7RcHe5aZa2EtXopp8ytIS8flUP5brjt9tZ0LI2GtDX3GzcY56D6OUmJHxPZG5N5zOU9ZT6LFIUXdlPubu0rrykjZB1mx7stqr5ZE5SaYYd1k5O42DhhS03yncsloPe3_GXsWF4xREwI5T7Z2p3vfOim6G4_tZfTOH-R-Zfrc7aw0ohnd-BdSkSnGCI7CQVZSCfS7bAZVKUwxEdsvt87p23Vzx21EKkRK7NF4fofcSdyUL4jILf1bDWtUr346OU0Zl0RDBuZW9zTAfTpVwwvEbiCuEV5INiH7jQtDdzUfNm-fJzwUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئو آموزشی‌نحوه‌واردکردن‌فرکانس جدید بصورت دستی در رسیورماهواریاهست؛ شبکه‌های یاهست که بالا معرفی کردیم همشون تاپ ترین هستن که بازیارو باگزارش‌فارسی، کیفیت فوق العاده، بدون سانسور و تبلیغات‌آزاد دهنده و جلوترازصداوسیماپخش میکنند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/22405" target="_blank">📅 09:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22404">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IC6bE6rZO8hzmVXSzXMoFEQakwRWUpPQdNKR0HB2S0gsLQsamHF82V0IMptzxglwl9tRe1-InLdJFFO_uoNuItIBhVgQ0xuOiu-Np9sIHLonYSqFExb69JEHup7sxEdsRS27SGzvErjvQAgmNX6Pf3nwoxAVMzgRk1UXBaJ65z0cLBGpOmVpfuJYDGGf4nw1-r2vY5XhW2VvPeo0o8qEn-k7nA7IdLIOwSoU6ELxp6F9tHVGPCVFDciY00VxKs2jWnoKJ8E1u9bto4rCzSdgeZSLYESw-WDlcX-tmamhzMdwwOxdp68cLkHOg73sWST7DasfN1gpIQUP_guQvxvRdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ الهیار صیادمنش مهاجم 24 ساله سابق استقلال و فعلی اوئسترلو بلژیک رسما از این باشگاه جدا شد و در حال حاضر بازیکن آزاد بشمار می‌آید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22404" target="_blank">📅 03:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22403">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhztGGHv6SLjhBHYcij82yA3MvpwCjeb1lVHdY9HjzmSm59bMV-JLI8yWDBTVOteoQJhzfKrXUEUkjQjcWPm1RH2NDCXxHj1sWj55HeNwj6sWOn4-yVKhZgTApjReW3MZSvTXdXEbfTwDPW9shGu6NlX1fsNNewQdBjS8W6mjecZix-X4RsXJiGO_l_r0L3eaSduvpc9w7EQ_4hAN1j3kflguNWe4D9xef04RwtUf8taiMMYhq6JCfOutd3_pevjI29BqI7Ziu0IiV14jMOukJDTkAFdI1mssAvH1bPMuav0p9lQr1kblGknTaXq5lhxMEnRtn_0DjnWZm7Va8OmMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لیست بازیکنان تیم ملی آرژانتین برای رقابت های جام جهانی 2026 با حضور لیونل مسی 39 ساله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22403" target="_blank">📅 03:08 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22402">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C02NqwGr49uY41WBgCU8rnGuLTzeQfbyAjbD_PF9OgsfCmkDxczNjQbTsGSa3GD2IGVwIsllTjGuzBKmdOHeUkBW98Fnw0xdyTEXra217uhp4wNEEEPD9ZxWEBNfb1MIFah0SIJ8TnlPAROI1agigIN9ShZZKDc9Wz60FjApI083lCsRSER-Fyy-9AbRkCoLG_KcfyvVO3b1koURw-y1YDCr4hLE1XFCa7JhtvUpcL9oLmCz4c0b_0jz8Ra6of8RXbZLxYmcJl6rnAiG3gHSEzmg9UXhUmg4H9YthQ3wGhPYOr0S6ItVkTQmgn95hGgOXvH70EX9FzFBuowP6Lo0Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه بازی‌های‌ امروز؛
دیدار تدارکاتی تیم قلعه‌نویی مقابل گامبیا تیم رده 116 رنکینگ فیفا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22402" target="_blank">📅 01:30 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22401">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSwoBJeqAjOgEsb0SnZEHHXYOh6LVBPNMa1PFwzhYRtg9ZVQ5gFcn5YY2j5KfFSbu4ZzzxGdYOIwSE0zBWPjNQAtx5Sd9ImjaGTxEo9HF-hRh1Gqib4mWkD-fEBwzk21Mn7IvqxP9Mxcwwz4fttb8iYSCTKR6tv1joo4upK0AWPlM0WGCU9kcy5k1Mj8T-_iZz5lFqxSp2mj0rkg9Dqp3TlGn1iTlTD2RK9pGjhufaGjHasRA1W9PJFherBAaXr-mWsBKWRmX_X4qwacAcUtHeBKpo-N1p8uSxOrj5aDQg7pKtndt59Ae1NLBBcHDtFlmiOY8Qcj8VY8Xm_42ndtSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای دیروز؛
برتری مصری‌ها مقابل روسیه و شکست یاران لوپتگی در جدال با ایرلند
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22401" target="_blank">📅 01:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22400">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uN1vRXLNyswqOPY_ibbglom3t7smlGgfASds8ODY6vBCM4Zxo1VzaDDdkR1hZQHsRa_pGWjxZXZhlYS6RC28OfRjNmA7LJma9_JBoi-RVGjagZvemnKPMCQGHi9OfdHabehKyRbuz_1RIFIzKwEyaM-lzVEQzgu5_wh5M2HJZGkvsJjHkP9l8_3ZrZJ7amC5vsIGow6jXUwe0adLqQlIJxXdNJDXScMT_ITJ2iMvIV_bS9ccEWfVeocXR8Ms45fFIAileCdhItqf1qxSNHv8eNhiXETRCE0vPzaTfiLgeFwpTW5dmqpdHbavf5sGKTegRiOcgR6z1aY4-ksWOGqAXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: باشگاه‌بارسابعداز جذب آنتونی گوردون و خولیان الوارز باز هم خرید خواهد داشت. هانسی فلیک امروزشخصا با آلوارز تماس گرفته و به او اعلام کرده برای فصل بعد روش حساب کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22400" target="_blank">📅 00:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22399">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AL82k6PLSRJYx7YeX58jLfZUXC5fA0cmnwVPrbJovK1Ijla6G_wx4fxCIgQ8eWT5VCLqhCHAqRIwzWyEvXOXqI5Hsqh70dvSyiouCwGCCGASvoH0lH-lIf5YQghI5MbwaMdnk0WMg-AltvChrdCm7jWBH1_ywnEJGmE_Nvsiq4aTK5BtbhbD6rEhU4n8dptpQdjlI4wMPz49qP4MRZ9Qu9YuR-BRc0-Ufke32nCPQhRtnUjkHlmqgC-6eZljSEwbwhu_zQ5uhbGdIObUS7R6fZsSf-fzEla5-JEtCAAIK4enQV0W523coTxEaBfmZI21Q1abURsiFg7A2GUreJOfag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برای دومین فصل متوالی، کیلین امباپه فرانسوی بعنوان بهترین بازیکن فصل رئال مادرید معرفی شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22399" target="_blank">📅 23:34 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22398">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ReUqFc91u7VrtYaEdsQl7x8i7FjmUf1xEidwUEf5xyWfqv5A-DfMOXNspmqwg1vYMaR2335oH3yhiQDEArYXCLzVuY5BJ7wUovLUFco6TmbmmgQxbAYYHdjGJQooESnAlGscckoSl6Yl-KSLayAk4lOeAAaWhM8DePhV0rmTiTbTaNMyjB27pwOlo6t3l1yPuow0mvw7DyHxRi0M7WaxmSwu2nfj7tIg9bLZleUhoyFOdBWsqdRH92eWswKb8a5OfOuuYPUPS4hAWtddvdEpBR41lptq4fsZosjZsn6trCELbKx3OWVhkbPe2Gw3el_CCCrl_Mb-wR30utokckpFig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی #فوری #اختصاصی_پرشیانا   دو باشگاه تراکتور تبریز و استقلال تهران از طریق ایجنت مونیر الحدادی به دنبال جذب حکیم زیاش هافبک تهاجمی و بازیساز سابق تیم چلسی هستند. دستمزد فعلی زیاش 750 هزار دلار در سال است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22398" target="_blank">📅 22:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22397">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=ZmTzx2sW265DSXXM_0JjIveVu0YxZWz-f2cZQnBpbYP_u5UPVV8aaW5LWAGym8GiP-4SOmw2vKTyhBjriH-NNvwUcSfr36AIlja19V5gnWXGAdoxLYPts9QXhf4L6ovJfbkuZSK3lXKNkfLinbSXAluQ3xNnTlLiL7qRH33j0RrropO6DE6ZKWoZturuy2oJnc5HKe8b3ynLlOkUj0ikJvdhVW8saT4CeLORJL1IgDNFpu7_pbuxG4c9wI0LkybW4d-b0yKbHhQAU4DVP0ADDA5ptwMPzjQR6CYt3lAOC22q_KwVAYBCzxxXwezCndAPOc1Zgsd43xmKpDJop6TSew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=ZmTzx2sW265DSXXM_0JjIveVu0YxZWz-f2cZQnBpbYP_u5UPVV8aaW5LWAGym8GiP-4SOmw2vKTyhBjriH-NNvwUcSfr36AIlja19V5gnWXGAdoxLYPts9QXhf4L6ovJfbkuZSK3lXKNkfLinbSXAluQ3xNnTlLiL7qRH33j0RrropO6DE6ZKWoZturuy2oJnc5HKe8b3ynLlOkUj0ikJvdhVW8saT4CeLORJL1IgDNFpu7_pbuxG4c9wI0LkybW4d-b0yKbHhQAU4DVP0ADDA5ptwMPzjQR6CYt3lAOC22q_KwVAYBCzxxXwezCndAPOc1Zgsd43xmKpDJop6TSew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نت بلاکس: این‌دیگه چه کشوریه یا ابلفضل. اینترنت ایران برگشته ولی با اختلال و فیلترینگ شدید! هنوز تموم مردم ایران به اینترنت دسترسی پیدا نکرده‌اند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22397" target="_blank">📅 21:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22396">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXO7UbQHXuTKoGhFnoPY-kA7thIURLYioSMH-x_U19Eh0qK2YiTgIrgXgGKZcfpF_eFLKx3HHuB6mAbjw76jQqOy9GRv_IfarfPKXSMk4vpuEt5jCBn4mWyy8O-H1p3Arcu1N4bhdTFu667xCzicz3VzD_th-n7mkgaL2cSKbOZkl0V0vtZDDayVmrLK3h7ufwfW3ujmx75BtcUjmpgeJAUSV3zmQET5ZgjefBJAFYlhk7dxIsAvXCPnIOyciABI5kA3IuScZGT0HE0Ax07Ix32Y5Q0AnsfBLLQYnaXq72POoIt4Ll1wSHqTpyV1cA2ybevPhj1vspyqE9miyD5CyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ماسیمیلیانو آلگری سرمربی فصل گذشته تیم آث میلان با عقد قراردادی 2 ساله سرمربی ناپولی شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22396" target="_blank">📅 19:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22395">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7629a35090.mp4?token=JWCPI10YayQ_s8s6P-oWRR3MZcmK99TfETmR2pquQqP17j9f-Lx2tXZPFkgMVJOSFZwCtKz8HfZkBy5njTe7giNfsGpKUFq2Zg-QaIOsXAWURyRWkzt9xBwdEDMjhg2gDfFfdH_2TpVYI4QBf-5THLmMs6iM0FnfMfbfKWoZH10SubrVkH5iR4Tor1RH_jbNK0d9xAQZbBVDhFtpiXZdnHB6xGjlKxVTMxUe2ld-r4umaO_J9UbsO7lkvVgOd4RVYgJtCZpzTCk5ckTlpVjey18cB6InixNwK8oS9GhoGQTarrUvqfx-rF1uW0RIM0hWSj2k03Z1MF_GL69QuhOHog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7629a35090.mp4?token=JWCPI10YayQ_s8s6P-oWRR3MZcmK99TfETmR2pquQqP17j9f-Lx2tXZPFkgMVJOSFZwCtKz8HfZkBy5njTe7giNfsGpKUFq2Zg-QaIOsXAWURyRWkzt9xBwdEDMjhg2gDfFfdH_2TpVYI4QBf-5THLmMs6iM0FnfMfbfKWoZH10SubrVkH5iR4Tor1RH_jbNK0d9xAQZbBVDhFtpiXZdnHB6xGjlKxVTMxUe2ld-r4umaO_J9UbsO7lkvVgOd4RVYgJtCZpzTCk5ckTlpVjey18cB6InixNwK8oS9GhoGQTarrUvqfx-rF1uW0RIM0hWSj2k03Z1MF_GL69QuhOHog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لیست کامل شبکه‌های رایگان پخش مسابقات جذاب جام جهانی؛ بنطرم از صداوسیما نبینید. اگه ماهواره دارید از یاهست این فرکانس هارو سرچ بزنید لذتش روببرید اگرم ندارید روز بازیا خودمون لینک پخش زنده میزاریم ولی واقعا از صداوسیما نگاه نکنید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22395" target="_blank">📅 18:46 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22394">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e8d402777.mp4?token=fY-22HFq6eRNPAfmcKMSJBrMQmIAHC8FzYqrpmtV_S5GrNTyhBVSqSL21-wRB2Jql0JJtUiBuWe9g-eQo8wjN_nshO3ipHj30L9GlY86PEYmkFTpK06QjNYhys8vGSZ9BrNQEDxplIn6yEPKZXka0il-PgE_oQkDS35v0RtDf2HBw4kDKM4HfoOh_iw8fxe2EW82Rn9XmCKLxfNQKwjaglYkXSmFuZcEVTjbMa_EzR6gcv0FegVnM1F9cDK0vqy57zpZczQOpU57xmI_wgU976k9X5GePFpECSuJfLgPZGKc3DdCEOG2PKsX7e_alYq9p9fXCMq49Y5sOuUxsK-vEZJuRspuiRjN_3Te2A13XAMcMwO4SY9_Kg1M8yANQ3yqxXIuRMPBcklvoY7ZmC52ZMMjgCtmRmmavtvF43Oo2kkMopfrNFv9-9L1bqHYXvXwKIpHCNQJIHcW0wdJoGoHTje88W1sRnoTt6LjqtwipAjq6PuvweV62dO4MQoTZDT8qADeppBqaTSUdYqpaX5HNB_7fLhiaMUM-yEGx8BdiQC-U3Jon3dT4GLuVGjE81hnp58u80A1-Rk7HLpF9XV7GRTDWPk7-SqFMY9r4wyFKD5DnUaGlEad_ta86MMlzXjWo8Gad1iqI8T-3I5KYrUTp9iddkbDQkMtc8dHV6mEo6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e8d402777.mp4?token=fY-22HFq6eRNPAfmcKMSJBrMQmIAHC8FzYqrpmtV_S5GrNTyhBVSqSL21-wRB2Jql0JJtUiBuWe9g-eQo8wjN_nshO3ipHj30L9GlY86PEYmkFTpK06QjNYhys8vGSZ9BrNQEDxplIn6yEPKZXka0il-PgE_oQkDS35v0RtDf2HBw4kDKM4HfoOh_iw8fxe2EW82Rn9XmCKLxfNQKwjaglYkXSmFuZcEVTjbMa_EzR6gcv0FegVnM1F9cDK0vqy57zpZczQOpU57xmI_wgU976k9X5GePFpECSuJfLgPZGKc3DdCEOG2PKsX7e_alYq9p9fXCMq49Y5sOuUxsK-vEZJuRspuiRjN_3Te2A13XAMcMwO4SY9_Kg1M8yANQ3yqxXIuRMPBcklvoY7ZmC52ZMMjgCtmRmmavtvF43Oo2kkMopfrNFv9-9L1bqHYXvXwKIpHCNQJIHcW0wdJoGoHTje88W1sRnoTt6LjqtwipAjq6PuvweV62dO4MQoTZDT8qADeppBqaTSUdYqpaX5HNB_7fLhiaMUM-yEGx8BdiQC-U3Jon3dT4GLuVGjE81hnp58u80A1-Rk7HLpF9XV7GRTDWPk7-SqFMY9r4wyFKD5DnUaGlEad_ta86MMlzXjWo8Gad1iqI8T-3I5KYrUTp9iddkbDQkMtc8dHV6mEo6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌ببینید از تکنیک‌ناب نیمار جونیور؛ فقط ببینید چه بلایی سر بازیکنان حریف میاره‌. خدایی حیف شد همچین بازیکنی توپ طلا نگرفت.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/22394" target="_blank">📅 18:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22393">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OODKpJsZ5Kf_2sjCr5ilXGiWK00LWbug_QrFfK6TrqQkdkJDQTzSke27ILLdOi4Lx2U23jeaHviT0or0EBbQkFKwvFnpnF8MuaYqtrAYLLa5Aj45JwCATrPG2icGVc-Tj4J3hMAT6JjRT5HkQe_tKDuGvQ84ODKPK43Yz3EI7eAzVNtaVkuB5eTIOSMZ88VqCrmxxrjWuwj5oNViynH16kcq04Vdl6WFWwhttx4OWLBMbVgWuZiIAENGTzO3LCQT_YzNrUUQeicAdXThg6RkeI7b0C5tvPAmB4cmgymyBWBlk8JQP1fSUZMraU2Gs7OyfOOvdmqfH3qEUja3_0zt4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه چوروم اسپور برای جذب مامه تیام 150 هزار دلار به به باشگاه‌ایوپ‌اسپور پرداخت کرده بود و 750 هزاردلارهم به تیام برای 1.5 فصل؛ روی هم جذب این ستاره زیر یک میلیون دلار هزینه داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/22393" target="_blank">📅 18:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22391">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVQuYLOiCerA57VDg3S8ucLh6UdpFhxfF0e7eJ0OQFMwp5PhWAoa00TuT4S75BQD6K3LrBr92chWTxipwxjwibNNtHyCmOdmgBBLdK5ZXztko2NNcFVnzoHyI6tAoPFxVRh3n1-hQF_9ZFzgKwRcYZXyf87e0coSXOJhf8zIR2eUJgtXEAwYqG_i7VzxAgNemLM2E9GfYw-0Q-OCQRp6_XMEphWO5zeuoskSu-hiM8_pm2x_-GsIdgrOILXJEvHBdHjZQfiwHdeRKVTIpVEtKGrgQU-yQnb9-ittGWbC8uEbEcAn67T7eESttrRIVdmo0dkBnhU0pHV3aFi2itXGsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛رسانه‌های‌فرانسوی: کیلیان امباپه، مایکل اولیسه رومتقاعدکرده تابافشار به سران بایرن مونیخ موافقت‌خود را باانتقال‌این ستاره 23 به رئال مادرید در پنجره نقل و انتقالات تابستاتی اعلام کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/22391" target="_blank">📅 18:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22390">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W51AV401nwQ49dOGfD7fIrqjF05CsjSwH2SehvXkjNJEw0kHjCojcIa4IrS2arstQ7SEfd2h9gBati6_0vxtQUV5LkjJz3irqkz2U-i3xkeyTWzK0gEMfsPQMWjPxqz--JU77mDqxXUOJeJkVxe3OFXzkDJ7zxeYk8qmc1v-t7gNrzz4GsZP6uNgRZghI36IZOYbE2T-aIPmH6xPwe6khS_7pdt4m_VtOPSwcLB5yJi1tyvZGi0VCLWY3eWKiY_D7xjSwzOR1xkFTrotF57JmaC668k-MRJXTbnTUfN8QF6ptDPsGOLlStv3_FEiRo7yZHi_EFWT1DclYsSWNQ34cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت بلاکس:
این‌دیگه چه کشوریه یا ابلفضل. اینترنت ایران برگشته ولی با اختلال و فیلترینگ شدید! هنوز تموم مردم ایران به اینترنت دسترسی پیدا نکرده‌اند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/22390" target="_blank">📅 18:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22389">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVbAapxeu3HND4kukg2dEkbKi4-oXn_NOSpYcOstb2cZZrQx0VBVNHoHkJhA1yY6OhuLsGBCEESMxdoWjum4RrHb1HeCjs8C1EcnGm7c4iC_Uzske7Zo_Oq9Xda5B2zTbR9nW2RP1O7bGlwSke2F_Kcq9N1dFYUyr6ZjHw8b5Yqr2Q5vToqLCY-DdJqs5XVBfFlE5Wf-MBIRXDdtAV4RFuk13sg7IHQH2mH8c52LHuw3Y66UHhntxG5dRaek0OzFHCE_xGpjW0Bx4e6WAMNklawk4pE6naEPmr8TEKkajgWkRiKygWqXyMlZw1h_ar2gXuPeA8_5qhknDt1o_bZEvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: باشگاه‌بارسابعداز جذب آنتونی گوردون و خولیان الوارز باز هم خرید خواهد داشت. هانسی فلیک امروزشخصا با آلوارز تماس گرفته و به او اعلام کرده برای فصل بعد روش حساب کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22389" target="_blank">📅 17:57 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22388">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OkbVmCMwItO6gcO4EvOdm3l5qjZpeHQfymq94o9qSZovwVnvvYIfQQ6HPHIDEbkVj69jBFnQGbs0v9buStWHL0vYvOAwogJal-JlxINKF-tZIvcaRCRHsVNg-TYzRdv1K2qcLQEzFbmk6Rw_lRSL4QvMvreKHWffEt_j9mC_OpmeSh9MCZDh5kROlQ9-g6cYlR2XsEFq5oKKNugZmkw03tQByVNEV6cwYiSCwHi3RyTAGXMclTX7-YSvI52MsMdQJZRSEtUJ16S_uWigBlSHUwpNdzar8Gmh4GyK22Gy-6-5Yds2zh8SnqY_kDPd3au39LI8UTIMVHWeRsPNqAUgKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بعدازجذب آنتونی گوردون؛ هدف بعدی سران تیم بارسلونا به خدمت گرفتن خولیان آلوارز آرژانتینیه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/22388" target="_blank">📅 17:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22387">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/maha96LD5mQz8R2EoNZj_jMD6wEW61XxXQ31al3iB5pWCwHpRSZN-SD4U0ZCauA-F4Ta9ObpPKA0jYiduMuchwRAH6NaCUvfz_ckOuve2VgwaYlGWSjuYtSRB02u6lhk-DMegUifRVFL0AvFO3WzQqj2XnOYeEfby2ltQkIUP0aKgI7kkq7tPLDW8LEu8KcfViI0UGfka43tfONYMFXdMmoUruR1aF6m_5ZyzhaJPJHYyNihTmfuVhaEab39IObKY25YvuVLwzrg6IifWPvcxIldbP-F91DpizQPun5yaiTOghVaAJgvHOc3x0e7hMoSuDEG6SX5FVO-sxAX5dBB3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رودریگو لاسمار، پزشک تیم ملی برزیل، نیمار جونیور از مصدومیت درجه۲ساق پا رنج می‌برد و ۲ الی ۳ هفته از میادین دورخواهد بود. به این ترتیب، نیمار دو دیداردوستانه‌مقابل پاناما و مصر و احتمالا اولین دیدار سلسائو بامراکش را ازدست خواهد داد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/22387" target="_blank">📅 17:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22386">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66baeb4dd4.mp4?token=J-cofkufIgXQvvtvLViAkKS6XEKkFvSj_ihmI0SencvodAN5qUg1CrDGH_-fW-mNgUz-hhRdUcsRKlT_N-jKlQ10prgFOvVb_SiZuDnjYbyoUxcEpQ-tEnSgLCcLeFe7fGypZDGpWIFFWEJQWv0Cao_5GTsX9apwWCdHyZzAD5oC9GNRiOsrgJvLWUwcQ1tRXNuMAE7sBIUeA2tuzYk4JvVuBqmnjieBwBfZKi9r_7-KJr75TbtWvkbz5ioHGCRhOPt4fXnhL_MNmt62CiHVOWFyDddgMhqvHb1OgHMJ8OoqV_ozx-GZ7KeudBa1YvclYUkT06wxtl4bi0peB9Q1iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66baeb4dd4.mp4?token=J-cofkufIgXQvvtvLViAkKS6XEKkFvSj_ihmI0SencvodAN5qUg1CrDGH_-fW-mNgUz-hhRdUcsRKlT_N-jKlQ10prgFOvVb_SiZuDnjYbyoUxcEpQ-tEnSgLCcLeFe7fGypZDGpWIFFWEJQWv0Cao_5GTsX9apwWCdHyZzAD5oC9GNRiOsrgJvLWUwcQ1tRXNuMAE7sBIUeA2tuzYk4JvVuBqmnjieBwBfZKi9r_7-KJr75TbtWvkbz5ioHGCRhOPt4fXnhL_MNmt62CiHVOWFyDddgMhqvHb1OgHMJ8OoqV_ozx-GZ7KeudBa1YvclYUkT06wxtl4bi0peB9Q1iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اگه‌چشتون‌خیلی‌ضعیفه‌هیچوقت عینک رو از رو چشاتون برندارید که نتیجش میشه همچین چیزی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/22386" target="_blank">📅 16:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22385">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0eb9ae9a4.mp4?token=lDbV2ReuBxwkU9BggbLKS7yTJBmxvU7B4xgVDwaSCS-RxTH7vOf_a6ZmcQnQ4Ij1WjaCAp5a1hIkfPq7ML0B7rj745Mh61PVWOb-yAQj5zEMUgSXbdbnLwON6gttvOp-q-ViSQYkg8PusgFhaJdJN-CsVKjJOikHosHfD9O0SNu3LGrikXtL7dZ-_zpTbpS2uO1AceyyTYRzFMVIjToHCzy5uxT6yHMq97_I17DEgAgII4Fy0eo-xEXZUxZ1LIF_hzSOn8XL62s4QNPXg19LnRDrCeCsbDhNYlY2dVhvam6rXk7r2pirxbDvidR9Oa9YzbrZ-Ytzpxf5wJ7QBPVINzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0eb9ae9a4.mp4?token=lDbV2ReuBxwkU9BggbLKS7yTJBmxvU7B4xgVDwaSCS-RxTH7vOf_a6ZmcQnQ4Ij1WjaCAp5a1hIkfPq7ML0B7rj745Mh61PVWOb-yAQj5zEMUgSXbdbnLwON6gttvOp-q-ViSQYkg8PusgFhaJdJN-CsVKjJOikHosHfD9O0SNu3LGrikXtL7dZ-_zpTbpS2uO1AceyyTYRzFMVIjToHCzy5uxT6yHMq97_I17DEgAgII4Fy0eo-xEXZUxZ1LIF_hzSOn8XL62s4QNPXg19LnRDrCeCsbDhNYlY2dVhvam6rXk7r2pirxbDvidR9Oa9YzbrZ-Ytzpxf5wJ7QBPVINzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
هایلایتی‌از عملکرداستثنایی آنتونی گوردون فوق ستاره جدید بارسلونا در فصل گذشته رقابت ها.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/22385" target="_blank">📅 16:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22384">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AF7UH752cc0rABDv4LIGRFBPs-5DIcY0tI5mHEq5O4knQclwf5ombGQr3NWNeafPxeizceukeUNMaTGSggi1Adh_0mAlcgcjjbqGm9oMrnqsFRPeBpmDxGLhbzSSGtXTlqb7PJfqmCqAD9_bm9tYRZqJ9c9OwCsP4Ov9OPgNO2LySKg5s4c95EUPf1aWUyQh1-EmatSbEYbztHYWdVatxAaDXXqvHxsKkiJhjC-hE2ewus3t-IV8E_9gOO2RdOdnmEuoy9Hn4ErNo9A1SBggmvsF87xKYDJjMp8-4Hy5rSIw6ioVevCigQrKy7YL-n-6oUKm2JxkRV2p2ybYieUHfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست کامل شبکه‌های رایگان پخش مسابقات جذاب جام جهانی؛ بنطرم از صداوسیما نبینید. اگه ماهواره دارید از یاهست این فرکانس هارو سرچ بزنید لذتش روببرید اگرم ندارید روز بازیا خودمون لینک پخش زنده میزاریم ولی واقعا از صداوسیما نگاه نکنید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/22384" target="_blank">📅 16:21 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22383">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DfvrRWwYnbP0Sw6DJ_h6JVlet_bWAVWErk4HVDp4j7H0LWQ8YbY7gRpf2lBdV6b03jkbyi5RKz3RmL6rUgFhS84q5BR7H0xTBl5WKxJJkYauU11Ce3kgObGPXiuxJeS564YCiaCESzphM5BuZiNq4AW95bt4ExvKxWc6IWFuGHQOYilMg14BFjQoV_Aet3_9f5Ds0Am05Qp4qVojWd76hsEyidyk4Arqj_AaedSbk2Pd8tTJ_M0uyBu-OG9OPMKwi-uAfWGiioiK7bc1nEAyUFqJB28IjmSHQBzRKreJyJYGQ9sl_WToD_Lo9IxYKgUH41ryhkVLWabbbqhd99trhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق شنیده‌های پرشیانا از مدیران باشگاه استقلال و طبق آخرین‌پیگیری‌های علی‌تاجرنیا مدیر عامل آبی‌ها پنجره نقل و انتقالاتی تیم در تابستان باز خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22383" target="_blank">📅 15:34 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22382">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFtM_nvE3dcrVjZ7w0Zq0XsEB-7XRBdXig4yxjdmNRHAffcBhxLq0Hs8zyQ1eZtiWg9XsaHfN1QxjiED_PPSTC73hb0VUIj6CxEU5HB9w_hKUrTYsoI5iNfmMSfiB3zWhoCcrocRDp9VIhYvVKl1MJKrulOWZYGXsr0J4PIRhA5tjBuaapWUHN7xe7f2EqXsmRnoSWlog8ORAdV2JeqWv6v_QCMCeN9IY_TpeA7M1vSIFrC19TPdMa4EWXWSZwo9L6WflaBAg0CS8hLwWuXSJrq5APvDG4Vk1ar7rPcnRWyNFR3NDoxMM9xZG8v5YT08fhKU3tSrHBUQh-oCAO6dvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ همانطور که پیش‌تر گفتیم؛ اللهیار صیادمنش و علی قلی‌زاده درپایان‌ فصل قراردادشون با باشگاه‌هاشون به پایان میرسه و درصورت توافق با خودِبازیکن‌سرخابی‌ها میتونن درهمین پنجره با آن‌ها قرارداد امضاکنند و باعث‌میشه‌تیم‌هاشون با دریافتی مبلغی موافقتشون…</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/22382" target="_blank">📅 15:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22381">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z16YJUF1dhVGfmbHVketQ6c5xCMAtOzYz4v4Mb13MYhHst7FDdOdr-SXwUysfhjfxP51ifUSkY3furTrYAu0ts08SBNhHm7QVgeZqpA4WlAV0DJZYhc2BSeOy3Q-WpkumUDyafLkoTjRHnxm2cKdbwvjdBjB6OXkfv6WcHYZHRfRfChwlChuo4rzfQcrzs0UHxukXZmYKqPmE-5Wc_E9oCpka4l5QUllU3yW-8kLJxm7PrQyQAFCziFwrzQaR4Uv1ZUUlPa-6jJ8PKHyYOhbMuNbiZ1okz2dyQgjnMjihWZvgIJAjMjiesom2hUZyH1nLp1J18mfZuCp_5YJaawy9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جلال‌الدین ماشاریپوف کاپیتان 31 ساله تیم ملی ازبکستان در گفتگو با رسانه‌های ازبکستانی اعلام کرد که با تیم استقلال قرارداد داره و در این تیم میمونه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/22381" target="_blank">📅 13:30 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22380">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">▶️
#تقویم
؛ 15 سال قبل در چنین روزی
؛ بارسلونا با پیروزی مقابل منچستر یونایتد در فینال لیگ قهرمانان اروپا برای چهارمین‌بار قهرمان این مسابقات شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/22380" target="_blank">📅 13:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22379">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tPnnghQLTUCyvOpYWpd3UoXFTBPgxzpLqIZMtHBr0auA1bJfQrtNg6tMe57Kc4iSv5vubZkTyQg6evUTK7cweoUQIpQHsiz0XQi-FmEMQOSs8-K6jm6KJbKcwCddvjnrLAPqsyucxV1Bvd3Gk1Uu88jVRIl1cvkZ6nF-fZxPoT313KFjPe1wMmdvVdzSVBVzl8nKB40_lLJRbAv_RpIKuGhadaMgqYk5d4ZwWKPBWVG7eYWXiwyWhy_JehVzedjrv7mRjJFJ1-W1N8PdUjn8m1M-3PJz0hQxLVmumkMNrcU4EcDK9h6kzmiVXVhHHgXc5-MBvUa10OEvwpU7fY_MSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ محمد امین‌ حزباوی 25 میلیارد تومان از باشگاه فولادمبارکه سپاهان طلب داره که از طریق ایجنت او اعلام‌کرده حاضره در قبال دریافت رضایت نامه‌اش ازطلایی‌پوشان اصفهانی طلبش رو ببخشد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/22379" target="_blank">📅 13:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22377">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbe2dafeed.mp4?token=Zo8CxH0N01NBEQj93tlVJL0jsCucp7C-3j9ldvU9SKd2aM9p7PwxeWz4bgqdBZ0g1TVmc28-MmmnQ5GGqsowZU4Tm46pn_0B6qhRAzZ7lfBgKKPcXoKPoDpxWQO6lF4bd4SZAhWpnpVAN3Fkd4iWAtHMgahqcm-uC02xeNRkPzho7UzC8Gkhc7t1TjNyFt2gjeLZ0969te_Jpa7DMVEvb7C6MSGZTDxpBoly5DHw351Z7i-kjwFOrbUY4XtqG499-pU94BekRfs9JkC2YGDoxYdyxrJXpqzGsbIr2pXXXDuT8B6xpJu9lpCZLTSIqbIBY2SNI8SmnGUKrWURAdw_bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbe2dafeed.mp4?token=Zo8CxH0N01NBEQj93tlVJL0jsCucp7C-3j9ldvU9SKd2aM9p7PwxeWz4bgqdBZ0g1TVmc28-MmmnQ5GGqsowZU4Tm46pn_0B6qhRAzZ7lfBgKKPcXoKPoDpxWQO6lF4bd4SZAhWpnpVAN3Fkd4iWAtHMgahqcm-uC02xeNRkPzho7UzC8Gkhc7t1TjNyFt2gjeLZ0969te_Jpa7DMVEvb7C6MSGZTDxpBoly5DHw351Z7i-kjwFOrbUY4XtqG499-pU94BekRfs9JkC2YGDoxYdyxrJXpqzGsbIr2pXXXDuT8B6xpJu9lpCZLTSIqbIBY2SNI8SmnGUKrWURAdw_bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
نروژ ویدیویی از لحظات پایانی رقابت علیرضا فیروز جا، استاد بزرگ ایرانی‌ تبار شطرنج فرانسه با حریف هندی را منتشر کرده. به گفته فدراسیون شطرنج نروژ، پس از تساوی دو حریف در رقابت کلاسیک، فیروزجا با تکنیک آخر‌الزمانی و با چند حرکت حریف صاحب‌نام هندی را شکست داد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/22377" target="_blank">📅 11:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22376">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNe4l3GfmMWWQ7jVyW4gfL289LEkBmmDaS6dhDczfU1t0fZnqyWZCOmqd2fxbi4SM3yAFms5XIBSbIRg3FY2KWTYxcidKU13sKAfjqwENxGcPvbedZ_HVkzlx58hLc9CfHl1ED2mIAi2wKzZZdV1Rb76ihtAqK9FjWhX6UzatASs22vPMeZFfWcbvEUQcnT4Rt4623TsvBpsheYo8O53Bb3aQVi1FNz-nkpuR6QF5OKAUNNOmixyNrC8srtKKRF6BJYDG_vKtw4rXoX_2TDAZoeNY3hk6YbN598lMaTTGgxLuBR7HZSBf4t4cnmOIjRemjS-ychrUHtaDVvTRTafug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار فعلی مهاجمان خط‌حمله بارسلونا که ممکن است آلوارز نیز به این فهرست اضافه شود
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/22376" target="_blank">📅 11:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22375">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqB-Fk1GAD2Tos9x_3fheY2X_iZ4a1gK0WwMKu77BH7WaNzDYasqAzzjqEBAvxcTpBQ8JCb4tLXjjnC-yMRw_dD9XAofMsuzXnyhlJiTpg9FUlm9rD-6l5O_bJLyBzmi7RhXguIiSrsFIFL8uRhGUImU7cT_wqDWd2B89rN4SOejnhaoOjSKJAthz3kehxRL1XRI_Q_CefWeBTVVu5yArxzqKhT17fmABJvRpwxCiEmsVFp538Tc1Kse26tNi5V8gtF9Rmhs260AvDtClw6_4kWzvDd1se9PyL1gWsHBgfa-b9ZPERrT6S-w8JD0MGeJZ90Nvv4ZTgVauml9nC8ibg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اسپانسرهای پیراهن تیم‌های حاضر در جام‌جهانی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/22375" target="_blank">📅 10:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22374">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SwkZ1trlb_a3keCRZZsJZQptg1pqOpnjojPwBzMvnIZ3o3GkPc9PTVl_oSZABfhwBwomTuEMD2dvD77pvbSGxpQVxz0emGsl20bh2pekfb-rEtXOzdcxDsDLSyTW7byYIff-KNBlAd-2CG34rAwJfyRDrfKNcog9Xs1VmRWfGk9lhZMKZA7f3IO9NWTyXEa12tLb4x16CpuUitACMEBp-ndi6Tv74YOwKcTRKguEIo3ZVHyTrbJNCOQJ7MEUBPLzSoL-LQCsC_Vgjuba-9c4oWsIhFK1_M0G3tX9H1vxk2I-tbSMMLvHc1Y2SPfB8pmIrkKExrmH9fKT4cuV9Lvr1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ کاسمیرو هافبک برزیلی تیم مچستر یونایتد، آخرین بازی خودش با پیراهن این باشگاه را انجام داد و پس‌از بازی‌از هواداران خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/22374" target="_blank">📅 09:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22373">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4j23cnoWqCvIZeD6BnVomLQfX5k42ngu1hbEOSnop5Ue_vD2GWBcgfDqEgMQJ018gb6zb2qYP8lpqJlVTD2M4BOCJYfEtxQPa8_0R2-Zqp4kXKyfP7xF2HHvL9pNA3qlgusAjtr-M6hDU3GWlqKLuaKu_DncBiuooz8qE0XywAr0YNjkG8OvJCbMn5dBSBeuVHLCkktP92ATyD7bL0FmSRzHuPQJOf7xQZ9SlMo40bT85PAJub9WZEGL4isxq3PwsAXUobzeXW5W9vrLwQ5Yul7O7IvKoZd9Mu-njA_4880l2Ane_nkSXhoRzEFdeIZm4Db5VTBp9KHJO5PpGXxMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کافو تنهابازیکن‌تاریخ‌فوتباله‌که‌ توانسته 3 دوره به فینال جام‌جهانی دست‌یابد. حالا لیونل‌مسی و امباپه این فرصت را دارند که در کنار کافو تاریخ‌ساز شوند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/22373" target="_blank">📅 08:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22372">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20ca45cde3.mp4?token=O87eUD8oegVReHUpzLiReUnx113ruovXja2-HB32BU1RUrdYpiwBqw6w6--6OG32JCQ4zxwm7QMimKooYFEQQVdhq6xpXGk2aVE39_6u_7MCkPHDj_USCgBu5GSF516Q9E-EfppZ5ZbPHQPxk0k_8Ep4b1_sAtyxmKCEE8RrpZYim0f3RxVNETxEcsekdAtKNYPH2isMZ8ZdQLd5RJ4QJAqBX6UMWai_-mV1RRnOzZXmUjvfVhMIXboInw8ll2Ql4jxnd8fxGIFrp1Qwo7q09AtqhBgTD3nWx1lCsntpTJUD9wXS_ti6ZaaHppCUlFnfF4Pl09W6Wfjf21mf9K0BJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20ca45cde3.mp4?token=O87eUD8oegVReHUpzLiReUnx113ruovXja2-HB32BU1RUrdYpiwBqw6w6--6OG32JCQ4zxwm7QMimKooYFEQQVdhq6xpXGk2aVE39_6u_7MCkPHDj_USCgBu5GSF516Q9E-EfppZ5ZbPHQPxk0k_8Ep4b1_sAtyxmKCEE8RrpZYim0f3RxVNETxEcsekdAtKNYPH2isMZ8ZdQLd5RJ4QJAqBX6UMWai_-mV1RRnOzZXmUjvfVhMIXboInw8ll2Ql4jxnd8fxGIFrp1Qwo7q09AtqhBgTD3nWx1lCsntpTJUD9wXS_ti6ZaaHppCUlFnfF4Pl09W6Wfjf21mf9K0BJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های طعنه دار ابوطالب حسینی به وصل شدن اینترنت برخی از کابران بعد از حدود 90 روز. خیلیا هنوز نتونستن وصل شن. از 70 هزار نفری که همیشه پستارو میدیدن 30 هزارتا آنلاین شدند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22372" target="_blank">📅 08:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22370">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bv32AOWTYm16NUf72LN89fLuPz4MDMat19Up9xQIzlVfdsfau6IOQbbX-9XCjTEWzbJnDDCqcOa2UGUtIOXnS7hWJuAuMAZwLCvyj0cFHZWb6zmNVLs83wJfCjGiM1ylgwVaathUJ5Z4MyXHLUUxjdQX8eMiKIkh2TwTFQyzOSKSYrDrzx1w4-kWap4KMCgMeyd9Y4JQclbnj26A4nnK94hPmnw2uzzl0JNiMbJglh3qxClAXmO7XeYmjl7XpbRMBj9rdY3PGkjqdIOQ3zgVSXliFv3Vc2pHSZoTzpZInimG0ArxWYJy9KqfZ7XEcz3oTpPcNktjsQjkQqWsAEOj0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
نبرد یاران‌صلاح با روسیه در بازی‌های دوستانه ملی پیش‌ از جام‌جهانی 2026
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22370" target="_blank">📅 01:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22369">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKdv58Z7MftfWuWRNbZfatmiRgEJjKFQgxFEXNFyCiIb5eoVV9f17hkTpRKVDaciAfyJLUVZvVbIs79fjK-X9Ynl4ZpgKN_iAJsXAMG2yTNxrK73t9SCcntT_VMqvYYvnNN4pjcxislCau68sLsSTcqZjdGnyK3UK0RfTEEk51MsJkCOgSvO1WIDPjvu1QsN9Al43q3n9KhpQ7EFf1-1hEULvCQdc0CajuC-EyTWIrxQvQauJwk88qSdH2pltAE3QSUutIN72R4t8lYMM89xngkm61RcB78aZsorYnS_5V__1DGNEpYamHRmSWu7D4bSbEaUlnDYf_TeKSzMChwRwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه تنها دیدار دیروز؛
قهرمانی شاگردان الیور گلاسنر در لیگ کنفرانس اروپا با تک گل ماتتا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/22369" target="_blank">📅 01:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22368">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olH9sb2Y-I_aA0T5e89fnFTkeBh2F3EZbqKdOl0Y_OcPvG74oby50e8AWYEPArtXGCXcvF2oqBh3sb_YgQR4Q5OSkwQEJLUQzQKO2YwWbCfdSm0qhE1oJLK6nI9EJxi86eH4UxTm4y4YoFvStR7dK0lDTjOUUHvNOaIyFVFaT9mKV11fIlzPCdaiGLjyeOEiWbEMmq0h26iTd9hWzdozUPvul_jqgtmKFHXQEUKHBNbVTMWqGUEU_UE4OX1Kb2PUP2t50tgVy5tWG4ZvaIJNay75eJFzKiFMh4XBEzuz7VuB7-KtsAah0mo_1AlN2BT6p3No0fp2emFGoO1EtX_-UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
اوستون اورونوف ستاره‌ازبکستانی و تکنیکی تیم پرسپولیس درگفتگوبارسانه‌های ازبکستانی اعلام کرد که در باشگاه پرسپولیس تهران خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/22368" target="_blank">📅 00:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22367">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42f6590fb1.mp4?token=By9KGf1aNdH_ttFckNk4y6YV0VzHe-EOuozCc85r4spTnSnvKpcpP0z6_wQOgSJgFG2eyqn4kbMYWK2afvzaj-Be6jDpL5XINLUMXsGxRpBlo3DjBiMPchycpGXzNE2Fg5W51lSrMQPGCUTm6ZhHzLaPxV63GPMgFjp_fRe_X5831_8jbr1n5IBG7sRbxo4y_kavJnUZ_uKeNmzAla1y5IAqWZ2k3LurwEv90gOPepWQF_dxuk9KWrxZ0AIouwl2c5eop1BDPNelmCmapvzJcjXZ3n8mXYe14C7DdC6CkowC_sRwTdzAA1-EzOlo1CI4mK0p-NYs6D5gOW9ZryoXZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42f6590fb1.mp4?token=By9KGf1aNdH_ttFckNk4y6YV0VzHe-EOuozCc85r4spTnSnvKpcpP0z6_wQOgSJgFG2eyqn4kbMYWK2afvzaj-Be6jDpL5XINLUMXsGxRpBlo3DjBiMPchycpGXzNE2Fg5W51lSrMQPGCUTm6ZhHzLaPxV63GPMgFjp_fRe_X5831_8jbr1n5IBG7sRbxo4y_kavJnUZ_uKeNmzAla1y5IAqWZ2k3LurwEv90gOPepWQF_dxuk9KWrxZ0AIouwl2c5eop1BDPNelmCmapvzJcjXZ3n8mXYe14C7DdC6CkowC_sRwTdzAA1-EzOlo1CI4mK0p-NYs6D5gOW9ZryoXZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تعدادی‌از فوق ستاره‌هایی که جام جهانی 2026 آمریکا آخرین‌جام‌جهانی‌خواهدبود که در آن بوده‌اند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/22367" target="_blank">📅 00:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22366">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJ2JxY-AEUm_nJ-gYDPbSWwszRitDXoeZ6pv8ZuAFEflTLQnLtLtqRHJ58L3OWakBBad1kinT7cA4qCvmkXZxaGaXtbrdalz_2RWSJJlMGMV5IfAUH1l6KW1CkpnNY0anxsfgU07wHDEPYqUQ9wQqvnw1ixE8O0HSBt0OM_rLAWln2XpeEgdpjIMMmJC7qp4Ots_1aEvfmfpYVyn8YogR5PBahIZCemmjAsNREIwdu0Qs1hDuLiAgG21pjO2LWcHcYk3f-sc4vOkpkQoRWhA3r9vKvbbwqt1ekPhDzr0Tkfs2BuzAecKO8SvswWRbpSiI9ExXX0bQozq-Fe0KpLNEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه هتریک متفاوت و قابل تامل کریس رونالدو، لیونل مسی و لامین‌یامال ستاره 18 ساله بارسلونا!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/22366" target="_blank">📅 00:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22364">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYiASi9QduaCkkgVj3Ha1hLGZuTwNJa5jdNdZRJB2hiC3vlXLkjpHW39H3Fef609hZQYB1qPGyQaNUI2U8XXoZhUZ9jWjB9FIzXsQ8Jd9te3v16yAZY3Rvs6h_5FPFlkuI19SQpiJHdl_Y-ZRWEynTfPgQ-fflRDZqrDZtCYHCeVTkokZnyYqsgMDaF3WiJZQSD8veB1HaBT6fpKTPSAErs6DfLtvxNILy7GcMFHYEhHGgRueU1E5VLC26g5VDIf9tz5QC4NpgoQLSJeKp6bGSv1FUvcgCS7aNuXL8M_ar6Itt-Cb3n2jZWY1tglc-2RLkWTT_ywuAf5R0alExMTRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#تکمیلی؛ طبق‌شنیده‌های‌رسانه‌پرشیانا؛ نماینده محمد امین حزباوی بزودی یک جلسه با مدیران تیم سپاهان برگزار خواهد کرد تا توافقی از جمع طلایی پوشان زاینده‌رودجداشود و راهی پرسپولیس شود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/22364" target="_blank">📅 00:26 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22363">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxM_C-4eoFU6b5DosYGlo6dkqOk2cvnr07NrQSwPZ3OU5h8rPpXBvokxsd3n9ZmJEBPpcjPG7vu-1CiX_bSuxYu4E_FjTyj8-hmMn92OnwovGFmhlEoH2Cq5LCXz7D2uauxsNuRQRCiAWhALqpv6NgDHAfFp2bOggNK32RIEhClSGRdulyGFSKZWO82oJ8mAXLP6H1xEeaCTNoKnfHUda_U2dHQSFd0I6K8o8JAbipO6ZUj60yTxczTDj9-raQQLr7mEQbU5kRzX2xfEiDWNgJNE5GRBB7p-KvTEufHbp6iqqim89EcmDXYZHSAbJkNjFaNvCSe-WNm0mSAz5B3DUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ بااعلام فابریزیو رومانو؛ آنتونی گوردون ستاره نیوکاسل با عقد قراردادی رسما به بارسلونا پیوست. هزینه این انتقال 80 میلیون یورو.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/22363" target="_blank">📅 00:19 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22362">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-14bVowyBcOvduRqAosYzXGuf1EW5AcoBVryw5DHXtu1LKe-LAdnEORi8Kn82GmheQSJiObKojV1yalNy7gsiFPNL4fQVR5bgASppBfy5SW5kdnQYqcZDjYo3Ru6RHtKu620M8vw0nxlINEnBe8hhY_1lsE0_F_FsYCKTaG68WoCwfH34pi0hn_E5kF4cJAbulwNYbKvwRkK-YDEKCcPxp9geyqdFKrRqRGRch89Nnw6T-EcrrAn8VY0vtaMnJOV1XgHpORv6eZQ_DsS93YW_KkR5rImk-I-V0Vd1xaklsd0SAh6JafHY-gRCJUudh0VU5IoZ9mZUla5db8rBK3sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ آنتونی گوردون ستاره 25 ساله نیوکاسل درآستانه عقدقرارداد 5 ساله باباشگاه بارسلونا قرار دارد. توافق شخصی بین طرفین انجام شده و تنها توافق نهایی بین دو باشگاه باقی مونده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/22362" target="_blank">📅 22:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22361">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be02e7f18e.mp4?token=P_ev68bN6t3ocTLsNcA-CqEK0jO2RwaZlSSmzRF-Jha5kv5hThuC3MdYfF10A2sadPq6cWOYu-uX4Znsk0Z87s8MQFcU2hhszO9H5-AolwpP9IvashCbj2cRzlLzaQ0XlncrHCk16WNAAqxQkt7t4AxqMUp-UPfjsJy5_qDksLuHOprOeP7GbShs9vt3eLWL3EMweob2fkvcBKeTZYVAWQxUU_7PZxcqWiP7ZAGgEcD5t4t3xdzcZ7UGsiEhAfOgG5qSrla4JMrPRnHanIiM3jDckwPF6gzFv38OrzUbLktK8KkJ7Vw-W7tvcDOKQA6EY9uFDE90A-O65aAb0EARqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be02e7f18e.mp4?token=P_ev68bN6t3ocTLsNcA-CqEK0jO2RwaZlSSmzRF-Jha5kv5hThuC3MdYfF10A2sadPq6cWOYu-uX4Znsk0Z87s8MQFcU2hhszO9H5-AolwpP9IvashCbj2cRzlLzaQ0XlncrHCk16WNAAqxQkt7t4AxqMUp-UPfjsJy5_qDksLuHOprOeP7GbShs9vt3eLWL3EMweob2fkvcBKeTZYVAWQxUU_7PZxcqWiP7ZAGgEcD5t4t3xdzcZ7UGsiEhAfOgG5qSrla4JMrPRnHanIiM3jDckwPF6gzFv38OrzUbLktK8KkJ7Vw-W7tvcDOKQA6EY9uFDE90A-O65aAb0EARqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
از عجایب فوتبال بانوان در لیگ MLS
؛ بازیکنی باردار درحال انجام بازی در یک مسابقه کاملا رسمی!
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/22361" target="_blank">📅 21:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22360">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5s2Qpbfan-GeBlJjNtAq78hGghGBBDTsCkSw4e86fD-WXc6mL6_Ec2K8LNqx3pGT7SUG-K220CWTKWBO6fnSpJeSi4WsgOOIKP-aknR6BE2hZmKbH52sxkY3l4orImNus8QfdMYwhPMws3W2I5tnNx02ZlAh2rqDGOrz2Yurh0xGJiiH3CE5lvka-fNzcuf2IIIg2WJL7UAdOxoPEDy--g01QplPtUcwvNE46mJgUrphvjM6pVJLxcgzikXjj-HPH3S8Dn90bJs00zd2hzzL0Q7ZYYMqVuEkUDTtTBSIWzkQOpm-giEaANM4CVKh7QxQsNZbEbjpaQ7vOCCWPhpag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ آنتونی گوردون ستاره 25 ساله نیوکاسل درآستانه عقدقرارداد 5 ساله باباشگاه بارسلونا قرار دارد. توافق شخصی بین طرفین انجام شده و تنها توافق نهایی بین دو باشگاه باقی مونده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/22360" target="_blank">📅 21:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22358">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30152b67bb.mp4?token=falrS_adqu4CgHs4kV30gamqmDBbz0EbQ2gd70BEvhbUvvdCT0tth461M1og0oOJ48mwIrrekV5tcB3PNHcy9H0VjllraYxqAOyWcg47DdkdE2BDhG3RjytvgYkPvqLx-FhCO1_OHlJbmRvqgLFTAf5Rc8o3dY3svuGZChoP-eJwUOvUre2QTz_jmQDLxSWFutNhMG8wZo64A6Wn9yl0a-ykFipCM6X3uOetSzwGr-ot7tRKhEl85QKoPVsjqbuXalm065rEl1wyvr16npJS6bgEyFCVFzc83cjvZZOkA_5l_qEo2XpkKJVR2c9gLiS9zdmzq1BOtqFTKLfVGCAPXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30152b67bb.mp4?token=falrS_adqu4CgHs4kV30gamqmDBbz0EbQ2gd70BEvhbUvvdCT0tth461M1og0oOJ48mwIrrekV5tcB3PNHcy9H0VjllraYxqAOyWcg47DdkdE2BDhG3RjytvgYkPvqLx-FhCO1_OHlJbmRvqgLFTAf5Rc8o3dY3svuGZChoP-eJwUOvUre2QTz_jmQDLxSWFutNhMG8wZo64A6Wn9yl0a-ykFipCM6X3uOetSzwGr-ot7tRKhEl85QKoPVsjqbuXalm065rEl1wyvr16npJS6bgEyFCVFzc83cjvZZOkA_5l_qEo2XpkKJVR2c9gLiS9zdmzq1BOtqFTKLfVGCAPXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوست دختر جدید کنان ییلدیز فوق ستاره تیم ملی ترکیه و باشگاه یوونتوس ایتالیا هستند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/22358" target="_blank">📅 21:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22357">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YY_2gpDxp4ioGdy7rWN4lDq8x1RuaYQbBG-U_0M0I2tkmHPKqBk-kwg-MpHJcLb6P8JiZuIzHCpJwF6hl6L8rwIleCznkm3YBCzo0MoQSKQ9BdqEL5cMI7vcFBv9ge-CO9ltPLHkTKT-Dxeaf72qGH1mdbwN-QczlogvgDyyiwh7vP15nuXfRm49N-xTb1YaA6L0o_PhzA-g7zD4ki_wnFdclZZrpDHtTF1H6_u8v_Ig4wnJ9SaTCa_NrHJYhMu4vhAqARqtbR6R-V0y-jY8wNGl1Q4g7Hcj4xhcO3No1SZEhBfaDTUyupt2Tz2GzdV-CVuo1PXYjaiJknilSG2GZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فرناندو پولو و فابریزیو رومانو: بارسا گوردون رو از بایرن و لیورپول هایجک‌کرد. بازیکن تمایل زیادی به پوشیدن‌پیراهن‌بارسا داره و حاضره‌دستمزدشو کاهش بده. نیوکاسل برای‌این‌بازیکن ۸۰ میلیون یورو میخواد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/22357" target="_blank">📅 21:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22356">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNGTWviZAmorrlok1uf9fkQnboIwjUSckUUs_v7qUWnQ4BEGJnmVaiA2yI06-Ouat2P_g1L_8eQckg4cscgvEM9Q9tX8MWAUxR7au2E5s02oMtXxeBq8Ik5psOoH9tptCMGkHKatV1JfEG3Cc-ntfP9ZGL7mMxKzFtg9Ek2XjTuBPyX--Qja6iQWKMraNFSRRSUFGK956ieh8BZ4clVSSXQ47txgOn4_z0DJNrKWw2dQ4wTBxsprBK-IWMpDiOXGuAk6AEtGg5FRQ0wtXTkd0cgpeap_tWbYsVxPTlJ_cE4b3FgkrK5IWw2eZ-CvVAjZg0n2mxb3ucxmWeE57-FJrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی لیگ آزادگان درپایان هفته بیست و سوم؛ نساجی سایپا رو برد. صنعت نفت باخت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/22356" target="_blank">📅 20:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22355">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fcgk08eKzSevQhSMtH1mf7Zxu8e66TtFtTD_J4S0HSdebDaAB84IANF7zygYSRuwNxdY2svW2pWfKccLr0qwRFotJuDvBaGjVKO6JiGojml28btXq6df8sUZ_z5cStpV0_2ACzWZueXtiphAJyxtK72GS6KCDF_WTQDKXvd5VrNHHCYpOIvpWLtJjk000ZR3JZpgoEy0VDo_gteNdJc5j2LE4OpmPlRMPYC-sc9eLTAK_fPPNgHkLtHxBtpXwUJj2lUimzXjicYqX0vgW2ZwljDrcQ7RqIjGATcPcv4_zfKRufHzV5njZhXG5MCMwFzvB_fHsWGyi-VTQO84FaJvFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛‌طبق‌ شنیده‌های‌ پرشیانا؛ دوباشگاه لیگ برتری بار دیگر سراغ‌جذب‌حکیم‌زیاش ستاره مراکشی سابق چلسی رفته اند و این بار احتمال اینکه زیاش بالاخره به لیگ برتر بیاید بسیار زیاد است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/22355" target="_blank">📅 19:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22354">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMwQc1x4KWgP6fAQTs8eD7pKnPc-I0ZlmG3CwHx4C0qCAAMmgTvJv3EGEsp8o2d97cKJoo15QmTihd9TxpBMs4jrDp-EF7sWGbWJyzSZVHACdPZTzJDRaFRjNjHkTUoxLNnMB6OGa5Fx5NoyKM0GmjHWWp1V-Y1xMytifnoW0BimuyMcE564F1e1KDAYSwPmrpMM9GezFMKGU2Fnzf4aQIoxRSVcxQzrKepAKnkvPHczQ3XaxQFK3DnUgQRwL1rLa8xhhMErwbNptT8rvmrVdWSF5_nWVnkEQ5Quyejp_Sezrh9F6qX11zgMlR_KacPB-BiWaeWYhCW9x4nX2MkQUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ گارسیا دوست دختر جدید لامین یامال: لامین بهم‌گفت‌دوست‌دارم تو آخرین دوست دختر من باشی و دیگر علاقه ای به رفتن تو رابطه‌باهیچ دختر دیگه‌ای ندارم. لامین بخواهد براش بچه هم میارم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/22354" target="_blank">📅 19:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22353">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GedvYJ1jTIGSwxGBebsNb1TGkJBTnaOeg-1AzjwnKTHA40XJt2XtmiFL8XNOpoS0FtLPCKBTgnVt4qYewysH0sEhpzvpKyTcpJSxoStOdw4ZuxdE4wU7KYiSszsZgoNrIH4D6Lbx-XWs85XK6c7EnsaP7Q52H8dIUEVucLVWzuFtB8unWGNckjwwEEfGVKwS9jbzJokISYg0aXKXr1pgeiRNooKLEeLbJ4Eq8UgcE76jbMJHlHFUgeSR192YFFwfWQ3MVjDjdxpjRqKhEsO2lK0xpA1U3yBmxYiyrQc1d65fx3YPAuDWeXUnTV_q4EzFPlVq_4xoCgSND5cWijoFaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#فکت؛ آرسنالِ آرتتا جاودانه شد‌. آرسنال در فصل 26-2025، اولین تیم تاریخ لیگ برتر انگلیس لقب گرفت که فصل را بدون دریافت کارت قرمز و دادن پنالتی به رقبای خود به پایان می‌رساند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/22353" target="_blank">📅 19:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22352">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30945cae67.mp4?token=O62ep_mISAgsQK-DW_g1D6jKVUAWc2gcnbwqC81tARihLwozlYSvqPEa4f3Pi4sxGgOAmlZvNP7kjwIxm7UPy_WskKXAXfGSZVeXpzExDPL-5Dh3pvi7EHjvyOEw9a7QxKt8Ut87xKijifX0FEkA5Ogqhom17XDFtqbEAeBVsSggL4HuNtjGxLWJH5vu600-9Ew6fIzdlnImpev1YTdY-8lmAbpb6oa_2jcKuT-CIcUCUkc4K35fHgpqBHMm_Ng8WCmUeigjigHZ8JchpyGtpynQeCVXCYOs_v2opjE-W9AULiF_tSsA1NjMxaWatDtGad1rSFc4l0Cxa86L5ZcV_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30945cae67.mp4?token=O62ep_mISAgsQK-DW_g1D6jKVUAWc2gcnbwqC81tARihLwozlYSvqPEa4f3Pi4sxGgOAmlZvNP7kjwIxm7UPy_WskKXAXfGSZVeXpzExDPL-5Dh3pvi7EHjvyOEw9a7QxKt8Ut87xKijifX0FEkA5Ogqhom17XDFtqbEAeBVsSggL4HuNtjGxLWJH5vu600-9Ew6fIzdlnImpev1YTdY-8lmAbpb6oa_2jcKuT-CIcUCUkc4K35fHgpqBHMm_Ng8WCmUeigjigHZ8JchpyGtpynQeCVXCYOs_v2opjE-W9AULiF_tSsA1NjMxaWatDtGad1rSFc4l0Cxa86L5ZcV_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
از حواشی بامزه مراسم خداحافظی باشکوه پپ با سیتیزن‌ها و شوخی برناردو با صحنه مشهور پپ
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/22352" target="_blank">📅 19:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22350">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vViv_L3wE0yA4c8oJBnbWPNudBtSCAkrKXwVIK_19vlWeJ6rRDKMg4pZWhq9DYNFrIStRKcxa4x1y8wFlSeOkZmLZOBkUX8vetKLimahoo1O4mWieGOVnNlhnLWOERWoZlRP9ncBpcXp502dLh1vxBwxgmH1Ut937g7i40P9LhnVRLi8ee0uKse6v5zoGiZFCYtZk14qmCiakWUtNICGHXNKN1cN1DlJTGf_7ITEkmk1J_-PTLoTOMk6tOfON7dnLHcGVJlE36s4wblfrGGdoZzR8PRmAbmG1c_cYtqgJA9v4icR2IRBVfgjc23KD8McVJmE_3mQHYpQHUSeOx6xxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#فکت
؛ قهرمانان دو جام‌جهانی اخیر در مرحله گروهی در گروه C رقابت ها قرار داشتند. تیم ملی برزیل مهمترین تیم گروه C در جام‌جهانی است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/22350" target="_blank">📅 18:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22349">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFdH8ORgJZzad0ZjsLZApPwFhF8etP6LDCtlArK0_vy0x1_eMk8kFXC_tSS9wGxUoDDniswH7FI8ddkUoENywHia-6S1AiNIH9hTO8bjBlJmWVzU_pB56DgVYQDkVaNnMAqRydlTHxy-5wrh2NUtI1x5krfGp_wsJeuDIUDtuJRjVEazDe7gkmdzp2JROOGS-Nk9YR9V3tON0aax_wDQS_3TKkfjZtWpFDMY74TrZi_hANBZMpNnoB5u-HPaJ6RBtF8I1tU_lapSudaq1nB1QqtlUY8LI8LoqHa0w_70vlTEzTIYpn3Nr1LZSlAiKBpTfVm7SswWKsKPzM84tMOfBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#اختصاصی_پرشیانا #فوری؛ یکی از مدیربرنامه‌های فوتبال ایران حکیم زیاش رو به دو باشگاه لیگ‌برتری که یکی‌از آن‌ها شهرستانی است پیشنهاد داده که میتواند با قراردادی دو ساله به ارزش 3 میلیون یورو به ایران بیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/22349" target="_blank">📅 17:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22348">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6d0b75c07.mp4?token=LYtAKqUjP1V3truWR9hAUJqUGWXv_gDrbMXL7AdvJq3TROUK7yIyj4C6xP3oE8Wfye60w_HRkl2kwtoVIUXA6lbo-aDoaI1VOCiyncE44dIwxHNTPiGb1ft8Fzz1d6S-O2sYBImlsKkSobDFeuQ3IMjqRAO-TxGwtexSSvmpfnnNtqk4HvNGkkKlFbTBv_SV0xjgX_e8r_xYxtUBGNZl6qjYNZA_fM_K1w0ediD-r_Ja6PhfG3kWcVVze6Gsb-wt6jE54yiD7vxiJA4pSijYpjpn98soKkC-XVe-JpNywTPuaK4uDmOgJeIKiwFMFBuXI82JSUmaHhhR83rp4Jb8fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6d0b75c07.mp4?token=LYtAKqUjP1V3truWR9hAUJqUGWXv_gDrbMXL7AdvJq3TROUK7yIyj4C6xP3oE8Wfye60w_HRkl2kwtoVIUXA6lbo-aDoaI1VOCiyncE44dIwxHNTPiGb1ft8Fzz1d6S-O2sYBImlsKkSobDFeuQ3IMjqRAO-TxGwtexSSvmpfnnNtqk4HvNGkkKlFbTBv_SV0xjgX_e8r_xYxtUBGNZl6qjYNZA_fM_K1w0ediD-r_Ja6PhfG3kWcVVze6Gsb-wt6jE54yiD7vxiJA4pSijYpjpn98soKkC-XVe-JpNywTPuaK4uDmOgJeIKiwFMFBuXI82JSUmaHhhR83rp4Jb8fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تنها 15 روز تاشروع رقابت‌های داغ جام جهانی 2026 آمریکا؛
بنظرت کدوم‌تیم قهرمان خواهد شد؟
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/22348" target="_blank">📅 16:15 · 06 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
