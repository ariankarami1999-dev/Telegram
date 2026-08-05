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
<img src="https://cdn4.telesco.pe/file/GBIFt5_l3E5RvyyurTKJXJqGSAxjUXZ4GtnuSkx76JLzPmlA7xjEdc551rw_WB5mWZSBIliwPzZuql9725tHLiqDL1dMvC0W4d8VeOVZ3vtqym1J35OId01CDRp9odD1MZcqGe8GXK249aiEHnVIjcH8hbHgXxkP6ga1A05gxv2usVDQcsmJzuVmuGGHbJIRAe9dq3-bjscYe5KewdUkuelfl2NqiuwmJzV-JuJQ4WmYHTtUctm1mv9VulBt2R4GPAOosvH1SaSD3IPbFkUVbaR2UNOraSHeOyyfq1GzRHU1x0u4nFqYU3gw8Z8LTYlc2eDAWIUVkf4fVjw2-QjY4Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 627K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-14 23:32:41</div>
<hr>

<div class="tg-post" id="msg-27168">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqaqFZb5FULcpD_WcQkzkAQaksXERYmh7tzVNuBVPfIdMr3kJ3KzWyvvNl6AfLjzS7hFWMMYKWHKpG_emVE3sZTvVdwzZOSaynf7mW52tbUibnzSRV3HDQIOs6xSg6ei83nkigUEVxdPTTukI2p_Q-R7v_ofF7UzFN-wK66Nk8LbyIEhXL-vRICqetNQYUYROhfg47kdUlh3iRvgGlpaH76g4l5xVBRMGFc09QDBpxqkOtDnQ317deFyH30D0MBm_19PX3JUMnHg9yksx-6EhW16EhZHXAh0RtvUoxP6QAfWGW2Hfbqny94e57NkwxdBMSGHAbZBImv3sy71Pe3sXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
👤
ساعتی‌قبل کارت‌بازی محمد مهدی زارع و محمدمهدی محبی دوخریدجدید پرسپولیس از اخمت گروژنی روسیه و اتحادکلبا امارات صادر شد و این دو بازیکن جوان مشکلی برای همراهی سرخ‌ها ندارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/persiana_Soccer/27168" target="_blank">📅 23:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27167">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b58266add9.mp4?token=Qqe6ljpu7PmUpjHt-AR_V4QgBiivRNcqxvl9UMMlzAm3KDwbtyFu16t_r_gGP8Ev5frsx2pPKSoigaeKmijc0A-95kI9AXGPfKIID0VZGitORai7tsetbuvoBAPPx3FI3lb8lwM4P4g2BcAXElz0TBbDYpMf9qgi-jjC2KRZ4OYC0qDm00LVondJRUp84cScrDnKK4FW7czBTLpx0UeKl60IEytciBZJaAXOAafrwE34wq2QvGpwfothqJoa3cHZIPvAMwCI5lda3cMojAa14czHec2uXITzmZGjbFNOoQ6tEk0FP04_V0Y8vrtOyYvz_9KqY2IfxfABoJ93sVvUyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b58266add9.mp4?token=Qqe6ljpu7PmUpjHt-AR_V4QgBiivRNcqxvl9UMMlzAm3KDwbtyFu16t_r_gGP8Ev5frsx2pPKSoigaeKmijc0A-95kI9AXGPfKIID0VZGitORai7tsetbuvoBAPPx3FI3lb8lwM4P4g2BcAXElz0TBbDYpMf9qgi-jjC2KRZ4OYC0qDm00LVondJRUp84cScrDnKK4FW7czBTLpx0UeKl60IEytciBZJaAXOAafrwE34wq2QvGpwfothqJoa3cHZIPvAMwCI5lda3cMojAa14czHec2uXITzmZGjbFNOoQ6tEk0FP04_V0Y8vrtOyYvz_9KqY2IfxfABoJ93sVvUyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عادل فردوسی‌پور:
🔴
اگه قرار بود که من چاپلوس و دست‌ بوس باشم الان‌صداوسیمابودم‌و نود روداشتم. چراباید دست یه مسئول رو درمقابل‌جمعیت ببوسم؟ چراچنین چیزی روباید باور کنید؟ دست کسی رو نمیبوسم. هجمه عجیبی علیه اومده. همیشه کنار مردم هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/persiana_Soccer/27167" target="_blank">📅 22:51 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27166">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbd4624448.mp4?token=K8j6nXIUadHX5_Yy0kE_SppnQCAymZyk9b1Au26obIjA2suV4UljMg3yQlwnqumbhkjQQUb9aBwpyyIvIXzY1ofvUrz0QvumB6upl5iUeR3XVnBq_Zozb10fW39wSeji7NKLLCIrXwRQgxvlOfoDpSLuCXroMM_RrnoU5HJpyfgWXZtT1wM8LCQYPbzJY4Vs8Wmrx3YYlVlAG5wumxTnAy8oi2Zu0pZvEEhHjAl6Ld_cekiERykGmKiP1GeOERa0jAs2aHeSAP0FQPrVKkVfDgBbOzIl9_zbr8R3VVH55CooTMFthXxKMHq2NyzDrvo-rOl-_rfm1wRK2fbncBq2dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbd4624448.mp4?token=K8j6nXIUadHX5_Yy0kE_SppnQCAymZyk9b1Au26obIjA2suV4UljMg3yQlwnqumbhkjQQUb9aBwpyyIvIXzY1ofvUrz0QvumB6upl5iUeR3XVnBq_Zozb10fW39wSeji7NKLLCIrXwRQgxvlOfoDpSLuCXroMM_RrnoU5HJpyfgWXZtT1wM8LCQYPbzJY4Vs8Wmrx3YYlVlAG5wumxTnAy8oi2Zu0pZvEEhHjAl6Ld_cekiERykGmKiP1GeOERa0jAs2aHeSAP0FQPrVKkVfDgBbOzIl9_zbr8R3VVH55CooTMFthXxKMHq2NyzDrvo-rOl-_rfm1wRK2fbncBq2dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
باشگاه‌فجرسپاسی‌رقم رضایت‌نامه یادگار رستمی وینگر 22 ساله خود را 50 میلیارد تومان اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/27166" target="_blank">📅 22:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27165">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAAK_qC1tKOj0092CNCwlbkhnMKNtmeWDubr-n_Z90gQn-WwsNwkDFEqauEuFRRTXV5gnhqn5KLTtD-eyx8vGWqqJu59i-N8Yg1J4sh2-s_RD1Y9znV_G8OgdWBf15p5bFxqG2-UqHZTm4wBvSrjyWF10bBMYYirRDXOxVRLdGkQ3A2QD9nEmegIzkgT5VRsK_zRMgCILBDsWlVNNSrZLGzqIv8w776fwS78PPGmus4vdPNVlT21gZDvoy1hWSiHlLUFTk3TkXWnEwdAX2J02D0LKW6hz7Ladk8_fYbrgGhy6qMYqhfGIlVnlhK0D3ycmFTocw4kj8Mc-kf5d3n_WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
🔴
مدیریت باشگاه نساجی به دانیال ایری قول داده هر کدوم از دو تیم استقلال یا پرسپولیس رقم مدنظرمدیریت‌نساجی رو پرداخت کنند رضایت نامه این‌بازیکن رو برای آن‌ها صادر خواهد کرد. ایری در شرایطی به نساجی اومده بود که از مدیریت این تیم‌قول گرفته بود که او رو در…</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/27165" target="_blank">📅 22:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27164">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/neDrS1C3c18Kjly-0oRjQ29fP16IvJSSgxq3HSfY3BcCPtWPv79qCcsyicB8KFVQ_jiJvljW6n0dgbjhKItaTflWvwqJKePqlD7sMyHkpRFK1537IZU91wlQjhsVL6RkDUGv8IE2wo0-CoWrKISZU9JfgmjrT1zdftOAC8vSDGVEM2j8OFEXqPNUGi_BwQEqo1M4yQ7t83rVGHCtvJPNXi27ZqSWFSRi9fesoJf_-1Kw2Pdv1mvgcWI2ubySCOmynRFMVhgn9OhJh_V4BM-ihhf5w3Jt1DhJXvx3132RE7GLxTehg4PHj7J2amUpDK_jnsOViusZ6m7XrsB7y9uAeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
🎙
محسن تنابنده:
وقتی‌حال‌مردم کشورم خوب نیست سریال‌ساختن‌ارزشی نداره. دوست داریم فصل جدید مجموعه پایتخت رو بسازیم اما شرایط جامعه به شکلی ست که هیشکی حوصله سریال دیدن نداره. هر زمانی که حال همه خوب بود میسازیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/27164" target="_blank">📅 21:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27163">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vR8SaDeMmnWeGgR9o41eqZ1DorBPgo07-YhSs8nYgScDH-CAMkd-5g_DucUGVbsMnW_jXV410vKG5-DzO5shgAODX3xfK4qp5eqxAQbrTI-I-AIuXWaE-d0H4Udg70ZG4szWSpBuQjIM1p4RyqJmeD_l6MUaniVAxq2dxRmhpIul7e9nGdcQq5tbzgozBCkPHoDIpsoXw7nAHHiJy__XQwY1uVeJwUiho8aNWVdplU_wWCs6VMNuJPXEj3bUMSJz6sndOp1hm7TwxEJ014UfXeZ8LGL9zoC8j-3PN6u_dQJ76BfO8pQnbDPZGxlXpi0FZFaAlE3WDtktfntBO8-PhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
اگه‌اتفاق عجیبی رخ نده؛ تموم خبرنگاران و رسانه‌های‌معتبردنیاخبراز موندن وینیسیوس جونیور در باشگاه رئال مادرید میدهند‌. گویا فلورنتینو پرز با رقم درخواستی این فوق‌ستاره موافقت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/27163" target="_blank">📅 21:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27162">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_BgRkJfEGcYG9Ax3MVXEihMWBShcZMW3mr_B0X-kdlKOxKf5KOUZ8-7jp9fF5pkgP9ScBhC2LZcv7oel9CIxGIdDYuuML11fSDKh7K4j8RWSJFObkksPngEhr0S1_5P_05NzejLK5fUg3xJz2NUoi2TczqF9sKwbprINwArcpG59swfsGObGcQJPqC6pnGqKtG3LSjpG0WBehxKyr7vuA6-sSKwkIFpFWgXM1F_OkMkAPhus2Yzle2rattXsuEZ6waJFkQMOidJQRierACEz4JaYFFxMvDtiXrNInqLPesfFEHPlEvQjHpqsYEbiJ1krqS2UuitBUDQXwjIqSr7KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق ادعای جدید مدیریت باشگاه استقلال؛ فردا تاظهردادگاه‌عالی‌ورزش"CAS" رای‌نهایی خود را درباره‌پنجره‌آبی‌ها صادر خواهدکرد و به صورت ایمیل به باشگاه استقلال‌ارسال‌خواهدکرد و باشگاه در بیانیه ای اعلام خواهد کرد که پنجره آبی‌ها باز شده یا نه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/27162" target="_blank">📅 20:40 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27161">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ng0o-O3isV1l8CvPBMm-fybhgS4mf_cOWzbpfRNFQrQI2ZgxiQBWvUmmzfY0FVGckPF7SzL2UwuvHMPGBJP0zsEH8jz0CMNbON9QU85RD1KyLlgCgwn_PJagpxh99b2LwgdK1Y2ysC5a9meIn6y9NRaGnqEat5FCVUibkyo67WhNNZzZm93KHZTxDH43soompejqgRn-YeWwS-mLqiyBzoQF-n5UY95Dnf3Spb8TiwbABDYOli9Raf9eM0_ZV74CSmGVF7WrJMkoXbdVuW_owr-GD4Y6Ax8KPC7fZVvfwdSsVc556wh6olnUmpc5AUdUeFZZwn2O0LL6BmSpiPsF6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
ادعای اسکای اسپورت: وینیسیوس پس از مذاکرات با سران رئال مادرید دراین‌تیم ماندنی شده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/27161" target="_blank">📅 20:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27160">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tq4YSwrtc709Q-GRM-AbWYs-OvJahaTh07knC3RmmnNUJmTG4TdsMZCITjza6C81dG88hWrSMn8iZa3BpCTXqnguM_pJeyYdt3MNHXzbXwCHf5CC03BlHcpvrO21-GoXWbAuJIt2roF-RUqXqdGTmpSiYLW-xyScwsNpdrhwOgC_l5oypZbWaLicJOP5gAGr2AtNAw_mWmpfRQb7JgNZ_FdJd5xa72_D0gpMntl7JpYfBYJSDc39USyqve9vs7ri15oDQgiRP9OPIbrL-uuEKxB8kipquJsDRp4n8KIzse_UL1Sqmhgaxz9LB4cr3z_kZWOMHqRiF1wOw4w1c4B7IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
باشگاه تزابزون اسپور ترکیه با انتشار این ویدیو از محمد صلاح خریدجدید خود رسما رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/27160" target="_blank">📅 19:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27159">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALR-zXRd-jImnhoRyur_-cfzyl-E3E1HPSKbLsSwrIl-lZVTLucqR3lR_JcpUrKfKRnvhrDQz9LgvlPloezpL2vXG8so2eZarga8sv3rj4wr-u_cfm1JzCWrICVoR9UivHJuYZgFxX8RwDAJNQP0Z8bRiTq-NNZ2B2wSGn1tOjIJQy1SO1IZrMLERav-A3FSiuwg2CrZMrApBDSQGNgUoGtFwXYmmavBtCMB1YDNqIHy_Lcp_kOyKed9CTiEBIwZdf00WfOd-JXYEpGTQXRbLId1DNFQC65CDvCSqhIOMOIdcuD_8KzDjdCCPdKJW4V9om-ZqSpVxYBJwnfle-9hWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بااعلام باشگاه استقلال؛ رامین رضاییان ستاره 36 ساله آبی‌ ها بعد از 1.5 فصل حضور در این تیم جداشد. مقصدبعدی او بزودی مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/27159" target="_blank">📅 19:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27158">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mylT040P_f6prCXpJX3P99zTYiQCT3klEDgQwV4akUhnxaluWuXrsj85-bQ8Cn14mX1IFR3YdbNn4Lb49Aq9au-USERRIgRSFLqIzdsjbPy0Jisnz3n5ZfxnFs6MNS022IPIJ8K-SakLpjiB5ooCIawL5weV_ggHiOvb3jzP6UOtiX1WqiLQr-IaUgsbhSiEAlN1tPQMswpNgScKCFCx7vGo-Csy77ma6T9CRnuzbrIqSDylWOunvtcHBVdLxS_9yN-i-fUNhYD9W6jbhWRVEOaYA4Pk9VMh5xnZV4fE1XhSryZzls9S_D5UcexwPNneXkZK1N9KrFoQfm1jJQKMfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ امید عالیشاه کاپیتان سابق پرسپولیس باعقدقراردادی 1+1 ساله رسما به تیم گلگهر سیرجان پیوست و شاگرد سید مهدی رحمتی در این تیم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/27158" target="_blank">📅 18:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27157">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ToFP031Ikh_m7KSQGopUT0FBO68R-tDwBXK9Dfo6tB913h6zX78zuaq_iF7OBSjjIgcbFfovE-4audo22XxrGc6mKsJYJvfVviY887gtWgpMyDsY4cknJX6vC95RVaE7KQN8rIIxUCnyyyIDW38JQyz7NDIXQukFEOfYGh3jSEdjfTzzyx0zfozQzI4LE1pF_tSwtAqIKheflS-MvwnK6EJKGRt6hrq2eKoWI2GsdHB14qz9AVkX5agPLnFBFs2xJJrchhIQeSTmtWN9Iu0cOCimRKCOoQ7TLi-POtJN1OGuAuHf6beGJxbVT-x1RjtWUvSSFIMzM2MwmXG-C1B90A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
خوزه فلیکس دیاز: مدیر ورزشی آرسنال به اعضای این تیم قول داده کارهای انتقال وینیسیوس جونیور به این تیم در حال نهایی شدن است و این بازیکن فصل بعد قطعا در آرسنال خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/27157" target="_blank">📅 18:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27156">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BT9RLvw1mF5so-ypUsbGHFP5GmDz5GlI8b6TmLVYDbDH2mNyWN7aoxWXz1XLHMsxGdnHVMx4E86CvBfc0A-hk-Q3sbcVIECQcScdpfKoSUj0g03aVoWJVgDVptPrGf1IAPD5XwWuLOP5tKTeuqAgX1qeluO0hbdOszRRG8aEQV6vF24iujXDX_lJ60RYKaWlIS35IUtROCgQ0jSyY5JPUwH2rWAztg4yRCrYlc880GLq6bBs1sV4LKOrXGSJEZLJdDDomvaYNbthRVMX1MTMtnISeCtdf7Cq_76Cw3xMnq3GZrTaj4bQMKhiyDk5kh5XBYk9B73culuVAgH9sffc5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بعد از کش‌وقوس‌های فراوان؛ امید عالیشاه برای عقد قراردادی دو ساله با تیم گل گهر سیرجان با مدیریت این باشگاه به توافق نهایی رسید و بزودی از او رونمایی خواهندکرد. بعد از اخباری و گودرزی این سومین خرید گل‌گهری‌ها بود که سید مهدی رحمتی شخصا با بازیکن مدنظرش…</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/27156" target="_blank">📅 17:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27155">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITh8KjcJUu9qOKpV7ym3MWwR23xxMiZu83NvCyGh9nizmNKtK9BZj2S3ppFC0Z5Te3R0pB4jWKW48Oa37o1Zwl-qjWMsUC506vyv3fCDwjFONhlqpNuHB5UWW1962sHujwTVLqBanvsEBv29xZ4_zZAna3aqGMyPj2Ye8auIsnOSoHVpt3pw_jmniREF3BJhiqHfbwEIixw2USsovAPfdG37M5pPnqet_gd2FI8Zrgj4yFk81spLJ_PScGSDjsQHMG6fmHEcYHlZUvmHtsDaTr0kUKQdTttGL0A3KTw1z77qoDY7mW6zy3Z12fXW3KEVNY4oKWYg7xVNQyFj2cN4vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های رسانه پرشیانا؛ امیر هوشنگ سعادتی مدیربرنامه‌های رامین‌رضاییان این بازیکن رو به مدیریت باشگاه سپاهان پیشنهاد داده و مدیرعامل طلایی پوشان اعلام کرده در صورت موافقت محرم نوید کیا آماده عقد قرارداد با این بازیکن هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/27155" target="_blank">📅 17:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27154">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4LFu_JNrj-L4auhMasA-YKIS6XROGekPkT5vuetmUua-X6qqXPA798MhSykBoA4qgfrsQGrkJDuvOnRac8NkqmEP_7hOfAXr3kTHn9dLnMuKhYV6-ryQCcOYd95xpLGA2LdanGZYez2CzPqUbmOBkpy63qMJW-EAioJF0A1R0xLItyeEEurIODzxiRF9uQ7VkQuyGTVveog_EQPMAz2KDdoy5gVL5k8k6YosOfQtfEuK40A7oYjmfVEUxcpAHoegs-O7ca5yIdNyvnNcVulLjHcrJZP0QfDj-rFZKNEHqUuLAOujb0B9kuRr3S4HEm0aFtw2QzUumvbgVTXOh7vsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مدیررسانه‌ای‌باشگاه‌ماخاچ‌قلعه: ایرانی‌ها با کامنت‌های پرشماری‌که در اینستاگرام برامون داشتند حقیقتا دهنمون رو سرویس کردند‌. هر باشگاهی که با ما به توافق‌مالی برسد و حسین نژاد نیز راضی به این انتقال شود این بازیکن رو به اون باشگاه میفروشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/27154" target="_blank">📅 17:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27153">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b7185f121.mp4?token=rGok9M0MeRLQHf9hnxpzm15qvUg8nq03DXhJLRrYfuJWeJkDmTAuNc7caf9oTsTedQB-pMrF3D1Wa2ggHGNnjuY9ZysShymTKrPoFiD_W30JjCvqqqP0PqXamgiEWU2PjCzbNvpZOk8vDJQXCzQQKqw51EDKyIgv1pUeyF1i8iuDEHteN_qeEplRn1Ta496naCJP0KrCMjgDNCJJtInj-w0DBqWwjOcz0K1r3F2YioCJ7lYRGWhlOqUTA9o8FEPowmlCCUm7wgiNdp4IrbxHMSuBJdrcN_EeHt2sL3N_eERU0Vy8xIb5kI978bFrTW44HZuiughK0V6fb3bS61-xSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b7185f121.mp4?token=rGok9M0MeRLQHf9hnxpzm15qvUg8nq03DXhJLRrYfuJWeJkDmTAuNc7caf9oTsTedQB-pMrF3D1Wa2ggHGNnjuY9ZysShymTKrPoFiD_W30JjCvqqqP0PqXamgiEWU2PjCzbNvpZOk8vDJQXCzQQKqw51EDKyIgv1pUeyF1i8iuDEHteN_qeEplRn1Ta496naCJP0KrCMjgDNCJJtInj-w0DBqWwjOcz0K1r3F2YioCJ7lYRGWhlOqUTA9o8FEPowmlCCUm7wgiNdp4IrbxHMSuBJdrcN_EeHt2sL3N_eERU0Vy8xIb5kI978bFrTW44HZuiughK0V6fb3bS61-xSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتیجه‌دو دیداردوستانه‌امروز درتور پیش فصل؛ توقف شاگردان‌آموریم مقابل‌افعی‌ها و پیروزی راحت سیتیزن‌هامقابل‌کره‌ای‌ها در دوران پسا پپ گواردیولا!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/27153" target="_blank">📅 17:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27152">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cs4W0y1Q2XkgcCWujiwjapIAskiKC49QMX7I9GNuTEiRHbYaT0x8PO2EHrp2F0KrBTsd6vEOJl8uvHYCnXoUKeW4sj2j6cwpJQ0XQ58CtTmW-X2GkFzX9J9mVp_k_Vw4VGhzWD80gnWjVuQYC1x0kUiiJVv_deKYWJl5HBJWMljVoc7x2pKiDZhBK_wO6cqqan8qGgwJAadZk6wRJDv2NBBA44Mh9Ul3hFp6qP7ZGwivYP81vqsfXzb-RMpXDTvj4kZKV--qtUJn4n0_5MWN0xvEr9dgpUYlo9DUMzigDwfV6Tx0ZB6ne0la-igMHqovQedVuyKAhFuCwn7YdtB49w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛ازدربی‌دوستانه دلامادونینا تا دوئل شاگردان ژابی و اسپالتی در کشور هنگ کنگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/27152" target="_blank">📅 16:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27151">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6UYbGC5aYcIgfjwGZA1078-Vs_gqioUcWfchMaugKRP69ziWnYPks-HieWuoxAHm9CDgSI8mTbmVKcD5kWEbc-YyxcEnCwUu8xh2iiCwMiLnrG_JrQfOAL71nA_gbkSLYCYbVxtwdE4PdmJxe-D_StSbTDsypQjsfkc-GLUp0QDuYEk4UoCiTn4MaUmBY06fj6hGMbscXFaZrJYRS6LOxTkqnzjD_vb_SaQDUMqgQEthRDkCNHXjjwTQ4db1CFoHczQh6tLXeUEPPv8liEW_Zy1cAZQFnEx2xx9Y3JeQ7WBJs2LvhLxhlcQzYmrdp6QJWUst13g23AhQFjc9HAlWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
#تکمیلی؛ امروز سرنوشت وینیسیوس جونیور در رئال‌مادرید و پرونده انتقال خولیان آلوارز به‌بارسلونا تاحدود خیلی زیادی مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/27151" target="_blank">📅 16:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27150">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0d917f67b.mp4?token=QKmG589GxwyvpMfxFC4oZ42PWgnWncNDBZspw2pYdlSDjKrgeoELwU_dTtY4r5H7hA8u0lHN8m1YhKM_lFXVLiMTwMZ3E_k38yK62bd0Yq4iz1XTQs8O9aGtgd5ZTlyXJt7cAWYDJ_yTMtGMz9m2gicbyicUrbnTY3Bzc9a7kNE1PEq9Gs-zQCoyl29efk2vUjdvsGBx9Hm9chAeyELoUpCqJGgSwpxmu0h38bCTtRPD00ON2M5AD3bLhjA0Q40SJd9UmjiIOOaU8_tdeGxahB1NWSdLcCm9YunzOnToiuGv4F4fAikr8y0hWl_2eyTh3qhsZeFP34U0MaMq8d98gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0d917f67b.mp4?token=QKmG589GxwyvpMfxFC4oZ42PWgnWncNDBZspw2pYdlSDjKrgeoELwU_dTtY4r5H7hA8u0lHN8m1YhKM_lFXVLiMTwMZ3E_k38yK62bd0Yq4iz1XTQs8O9aGtgd5ZTlyXJt7cAWYDJ_yTMtGMz9m2gicbyicUrbnTY3Bzc9a7kNE1PEq9Gs-zQCoyl29efk2vUjdvsGBx9Hm9chAeyELoUpCqJGgSwpxmu0h38bCTtRPD00ON2M5AD3bLhjA0Q40SJd9UmjiIOOaU8_tdeGxahB1NWSdLcCm9YunzOnToiuGv4F4fAikr8y0hWl_2eyTh3qhsZeFP34U0MaMq8d98gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
🔥
فقط و فقط ۱۱ روز تا شروع بهترین لیگ دنیا و رقابت‌جذاب تارتتا و سهرابیولا مونده؛ برنامه دیدارهای هفته اول رقابتای لیگ برتر خلیج فارس!
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/27150" target="_blank">📅 16:29 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27149">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sve9nRhjqYllKCS8UK_QQnDviBqYnDR2mQmDAiMeDKBS9VsQsucLfa24w-2FbrGZjOAFJ_6KyKF9wu6UZsr9Lc4mcBCk3pNDbY05KMGAA5681Da4oDtdqr-J0gv4p9zooMkNd0qQjKN9CGTMYfcKfCv5-nHszZqS9JirG99GclZLFU36SKMi-iZfcuPZxRDIQhTuHWT9C-DaE5TrkVyxemupKhbYWI9iko__45e5ANBN6bAaoGeMOVFsrE5psKqQ9OtuQNXf6uV786uVJfbcr1L7nqOF2B7YRR_qpuLcgZ5SYEp6rBAeQjXkme91C5TUPVk33w1wFV0OOitFrCEt8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
چه خبرهه زیر این پست محمد جواد حسین نژاد؛ استقلالی‌ها میگن بیا استقلال، پرسپولیسی‌ ها میگن بیا باشگاه‌ پرسپولیس... اون‌ ویدیو هم فن پیج‌هاش ساختند. انصافا شاه ماهی نقل و انتقالاته. هر تیمی بگیردش برد بزرگی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/27149" target="_blank">📅 16:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27148">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/315f795088.mp4?token=LDuvncOfWTY32MvH14AdeqjgaDyOVX6eIyuzqyPh-w5YGfdWSAHi07SWXJD1bTRKuWFHdoTPqwlZddXdMEEmfU4ji4PUY5S0Sv3hbp6lyQGNsCsqotZv6ZHP1XKIknaixVygvccpv1VhPmvWvtdnMWsiYm3_OAE2l44EdDkAP2JX2zS6Bp_9umg_Q4CmiZQAqICjQRZ9tA7O0V9sNhoS4SFjc9gEpIpGF9h7AIanuR_pw94dp3uunLs0PzhrFt8s3gEbSjM1JTry8fYfq5EnRz3145BPjx2P5-34KxFmt1PdKCgKYY3s4h-feJG9hd1kwK9y6T2zePxFtz7jMBJ6KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/315f795088.mp4?token=LDuvncOfWTY32MvH14AdeqjgaDyOVX6eIyuzqyPh-w5YGfdWSAHi07SWXJD1bTRKuWFHdoTPqwlZddXdMEEmfU4ji4PUY5S0Sv3hbp6lyQGNsCsqotZv6ZHP1XKIknaixVygvccpv1VhPmvWvtdnMWsiYm3_OAE2l44EdDkAP2JX2zS6Bp_9umg_Q4CmiZQAqICjQRZ9tA7O0V9sNhoS4SFjc9gEpIpGF9h7AIanuR_pw94dp3uunLs0PzhrFt8s3gEbSjM1JTry8fYfq5EnRz3145BPjx2P5-34KxFmt1PdKCgKYY3s4h-feJG9hd1kwK9y6T2zePxFtz7jMBJ6KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
امید عالیشاه کاپیتان سابق پرسپولیس بعد از یه‌ دور مذاکره با سپاهان، فولاد و ذوب آهن حالا با مدیران صنعت‌نفت آبادان نیز درحال مذاکره هست و هر تیمی‌ رقم بالاتری پیشنهاد بدهد قرارداد میبنده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/27148" target="_blank">📅 16:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27147">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aee60bdfdc.mp4?token=HwUa68fQeTGecnGMhZbgSc00WR3YcPHZ9ujX7AknxT9jhhO5-cy7iHpFdSQaZfYwY02N1Vk7_Vr11CjaV8eNlX35abETAyXjUvs_w85LoVPvSNcLvOGtas75-D9xqLcZ9rbh4mGvmM1uHl1Yxp802jwElJAvJ0kWHWL0ocobyDRpAlFfXbCdrysbSnW-9S4NlMqalzpORkk-F1PHHcZ3gp_0Ei92oVTMhhBicssffFgFH59KnQj2_FSiH-JQl2_q-wv3n5VwNfG6hbn_3nRODhyKiBmuB5MNEnI3u4hOpX3VosiT4EUTxjMCKA2mgnV_ubXD_zS22spPYl9xsQ6qvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aee60bdfdc.mp4?token=HwUa68fQeTGecnGMhZbgSc00WR3YcPHZ9ujX7AknxT9jhhO5-cy7iHpFdSQaZfYwY02N1Vk7_Vr11CjaV8eNlX35abETAyXjUvs_w85LoVPvSNcLvOGtas75-D9xqLcZ9rbh4mGvmM1uHl1Yxp802jwElJAvJ0kWHWL0ocobyDRpAlFfXbCdrysbSnW-9S4NlMqalzpORkk-F1PHHcZ3gp_0Ei92oVTMhhBicssffFgFH59KnQj2_FSiH-JQl2_q-wv3n5VwNfG6hbn_3nRODhyKiBmuB5MNEnI3u4hOpX3VosiT4EUTxjMCKA2mgnV_ubXD_zS22spPYl9xsQ6qvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
توضیحاتی‌جالب‌درباره‌پست‌جدید کریستیانو رونالدو در کنار ماشین های لوکس و گرانقیمت خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/27147" target="_blank">📅 15:46 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27146">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXsEFp6vSrYgwqJEua7GLndI6VnuCYZZx7Pb1Udd5ASz-PZa66nZ7KqUeHKoq0aaRxMhs1K_9yKXARzRdXFdegAlyDciTrpgQPOvvZun7hlMDZswBVC5kgQ3husROCuDlE_h8y6vtmDc1ftLiUsHtCsZVH54ldEZKg6MHpP81Yzkrr25XvYGsM8p0pBDtFvuY9sDqdsd_4BNqGgyasLhvudRAiTkLZNnZUgpxAQU7QqbvcZFGK9VouwwHKtf0pwOKou8OQEh5_QMSoWumUvDEsfPO7V7zzpjY6Ji6cdEeVhkEGOOz-bTke1jrjXSpb0_BOXd04oWR2mZrKTIu_m9CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
فرشیدباقری بادریافت14میلیاردتومان از پیکان قرار دادش رو با خودروسازان یه ساله تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/27146" target="_blank">📅 14:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27145">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMLlCyhnSe8-iuKqe-zbCmeuNw3dY-QcGmx1voVXU9lNmSU37Avc5KL1LLrqVj5Y4t9pfJtte4KNV_5NV9bwsHgdcSfFbODjZSXFYOxXxciMgRQZsAkljun1KVnvwmhhZldf4x52tYWlRkefSgrcJGYSxA6O9RSWE2cMfJZ-ydTocjQGHT0pnCvl2ufpCcMuC8g_U_6kRaaBeIiRwh33mgC8X6NCDv6sBfZNHDJaahxzXIlH08Gpd-IRP2VEbfwCNxCDpcr2iYHhVE_rr-WVrmh_jxN09yJXS4xbCXBAwYZYEEsFtZ9eYw4Z9pCW_A-xRKjouvurGhKmL54sLLb13g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های رسانه پرشیانا؛
امیر هوشنگ سعادتی مدیربرنامه‌های رامین‌رضاییان این بازیکن رو به مدیریت باشگاه سپاهان پیشنهاد داده و مدیرعامل طلایی پوشان اعلام کرده در صورت موافقت محرم نوید کیا آماده عقد قرارداد با این بازیکن هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/27145" target="_blank">📅 14:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27144">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09ea3c3b07.mp4?token=k4AMYJqc7qjn1jUPJgeWZEqmSEhtWBwySd1s2fV8T9LzKylHFhGgXlypFKTMa1pwqdr7PQnXKYCPrtWf1knF_f4pofp4SY5uRh6s5VAeFmIjFAPA_9moiZcH8vP3pKqdKlD8HcJYGoL034RG2Yjh0OS2n4ibIZSonmKCMQ9lVTBDim9yTh7Mh8pi0E06Xo0VL38fSk7DSP2i198ChJgbo9OggEmzF9TdNZcmFbgh7E_YYttpbEWmyyVS81GTbPWVZo5ioJjvixQjShME8xI90uztymxtw4WqjIbBBxEwiwoshfKV9sCFBLyMstEG_OSPSOrlgSfbDpMpW-Ul43lkp6nQOPdZM_wn-WPPyb_WlmIyxLALu6WH5egDP9MwuMogIwOFSktSSwHe4KMDt3xwDcgKhej4h4sSGNjtmOYB-Iy2N-g7X6xXHc2lzYq-pH_eD804O4MV2OEsDsZMC1MYOiaQxw2-XBgiW59rFDaIhQXJke19e9aFz59UowzEUD2x87yLfhvQ0T2hyFEVwlR2O3cJr7MhFEDcH2iOAPZapVFB_v9oMxSz6Tv_Tuh3OGZRHyczY9oFHjdbXtmyZ4673PKLFvwzfAI7k9aQCNQngySGTJ3Zr-Vw0UJDHHz4BhdrLjUQcJGqxkJ4S4YPEkz_lGsviVs7-YOvmH24F87yjio" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09ea3c3b07.mp4?token=k4AMYJqc7qjn1jUPJgeWZEqmSEhtWBwySd1s2fV8T9LzKylHFhGgXlypFKTMa1pwqdr7PQnXKYCPrtWf1knF_f4pofp4SY5uRh6s5VAeFmIjFAPA_9moiZcH8vP3pKqdKlD8HcJYGoL034RG2Yjh0OS2n4ibIZSonmKCMQ9lVTBDim9yTh7Mh8pi0E06Xo0VL38fSk7DSP2i198ChJgbo9OggEmzF9TdNZcmFbgh7E_YYttpbEWmyyVS81GTbPWVZo5ioJjvixQjShME8xI90uztymxtw4WqjIbBBxEwiwoshfKV9sCFBLyMstEG_OSPSOrlgSfbDpMpW-Ul43lkp6nQOPdZM_wn-WPPyb_WlmIyxLALu6WH5egDP9MwuMogIwOFSktSSwHe4KMDt3xwDcgKhej4h4sSGNjtmOYB-Iy2N-g7X6xXHc2lzYq-pH_eD804O4MV2OEsDsZMC1MYOiaQxw2-XBgiW59rFDaIhQXJke19e9aFz59UowzEUD2x87yLfhvQ0T2hyFEVwlR2O3cJr7MhFEDcH2iOAPZapVFB_v9oMxSz6Tv_Tuh3OGZRHyczY9oFHjdbXtmyZ4673PKLFvwzfAI7k9aQCNQngySGTJ3Zr-Vw0UJDHHz4BhdrLjUQcJGqxkJ4S4YPEkz_lGsviVs7-YOvmH24F87yjio" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
به‌بهانه جدایی رامین رضاییان از استقلال نگاهی بیندازیم به لحظاتی‌که این بازیکن در این تیم داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/27144" target="_blank">📅 14:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27143">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7uvKktxfBFGZEWI1SVoKk3CkPZWix_tCn7xaYxmVYSS6dhfUODwQWSbDWgNNDfTWFrbgHNVJ2fhYdQ6wcCKo4FidSuUsvm3kaiSLaJ0SHFzp1lSUTVMpkvEBq7FO2GzGTAHZvm8TgrI3AnDpt8UI5CVEd1MMGvuOBN8NUMWGxn3dl-5_ssVb4I9w0ocndjMlrIkcE45qWfE9BVM7ckpyCK8F7yrSAK2QxLlzTTchWAz1n3rcuykmm8nTVvCb6f4ZXZPOUnU33Mu2BS1ejzl8ctmu6-1LxhRE8QQq2blmh9m5giDQcWSJHdc5mRLERl3WMnFsQdkXlGoQUni3wGPlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بعدازجذب دنی ولبک؛ چلسی ساعتی قبل جردن هندرسون کاپیتان36ساله‌سابق لیورپول رو به خدمت گرفت. حالاجالبه‌بدونیدکه هدف ژابی آلونسو از خرید ولبک و هندرسون‌بحث‌فنی نیست فقط‌وفقط میخواد تجربه تیمش رو بالا ببره چیزی که توی تیم خیلی کم وجود داره و رختکن تیمش یه رهبر…</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/27143" target="_blank">📅 14:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27142">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‼️
اولش یه لحظه فکر کردم وحید امیری رو برده اون بالا؛ لامصب ته چهرش کپی وحید امیریه:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/27142" target="_blank">📅 13:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27141">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/590b770d9f.mp4?token=uqVWvnUhLR-eVpl1k6ZUU-VxQXK2QX6znCAOfOni_pV1NfoynDCtDP-LpcDHu1eQfTSWpZ9eKNvQZLKKrlQy6spCcE3zFLzBK6tGl_Jj6p4wh7T9ZpM0ZAmZuMeunsS9qDPVfZaKfkoatX1MeJotdL1wSZn25xyL_2xjzWYFOE3hbCLAfc5yqTh2wMPUX4YF52e7GXX5rSz-iP_VgBXuv6zHU_P3t45ZLoMILNlp_NXJE_rxpj-dqhqNTC3HVk_qUA5MPI3WeU2MOiarMhg-H8VPfiUqdNLu1Y_G3vkKijcv3CfNpmW3MNqRMrLglD96BlZzEa12S2FuYe89lq1cPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/590b770d9f.mp4?token=uqVWvnUhLR-eVpl1k6ZUU-VxQXK2QX6znCAOfOni_pV1NfoynDCtDP-LpcDHu1eQfTSWpZ9eKNvQZLKKrlQy6spCcE3zFLzBK6tGl_Jj6p4wh7T9ZpM0ZAmZuMeunsS9qDPVfZaKfkoatX1MeJotdL1wSZn25xyL_2xjzWYFOE3hbCLAfc5yqTh2wMPUX4YF52e7GXX5rSz-iP_VgBXuv6zHU_P3t45ZLoMILNlp_NXJE_rxpj-dqhqNTC3HVk_qUA5MPI3WeU2MOiarMhg-H8VPfiUqdNLu1Y_G3vkKijcv3CfNpmW3MNqRMrLglD96BlZzEa12S2FuYe89lq1cPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
ویدیویی‌زیبا بمناسبت درگذشت فرانکو بارسی اسطوره تاریخی باشگاه آث میلان و فوتبال جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/27141" target="_blank">📅 13:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27140">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇪🇸
🇨🇮
ویدیویی‌جالب‌ازگذشته سخت و درد ناک یان دیومانده ستاره 19 ساله و جدید باشگاه رئال‌مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/27140" target="_blank">📅 12:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27139">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e46D1h5xZ6XD9fInusUgtuaQBTsG8jy1UQm6s1TMe5OxzEIemInee5yJ93X-CzzHxubyvLQRihttSI9IwoCzO4-yIY2SwvQKV10bK_OKlvj8yKoXreXpCP2J6Xg0t_F4R9osP7KzHLZg64npxrBfY-SrzJQCmX0be4SRi4gK8QajQMdSn8ddlMDp4agCNY_20PgLq1h54R9b9pLzrew0tNz43inFBK3g9vQ36z5mERo6StnGy5WfcKEBCHGh_Smu7_sznWB0XGK0fbl8aKtZ3qjOpLgRwH234_LzmpdU_yha6Jt2c_eR6sHvrE0lgS7auxbLd8-FEL8AIyfWWMvneg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌وانتقالات|فابریزیو رومانو: با صلاح دید کادرفنی رئال مادرید؛ فرانکو ماسانتوئونو ستاره آرژانتینی رئالی‌ها در ژانویه قرضی جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/27139" target="_blank">📅 12:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27138">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upN7g5NhsijRwuzP5eypNgIiMOC9K5pNTm6gYKTy3xOKzIVef7tiPvdXBzod2j0Rl9sQNOAz4nbq0izcR4bb3rVboi8-HbbjWF62vsawwmkB7Dbe6GicBnFxq4VNbIxbayPuF1L31Ddax_DvLeZibZzf3nnw2vvaAvhSzANBgs00SXhg0-6LGnbjOz6YFoxseFWCgOiv5LLpNdG_UzeqZSwST--V33oD5kDjkJVhkbCV5bfiN0GGvwVC-f9i8y1pjrs5T510Q5LYrrUD7bcIS_ez2y3obm-v2FkfzVnj_DkrIl7FVhlkm4nnv9BO5pQuCYzZMsknn9GvuEo_fdGnKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/27138" target="_blank">📅 12:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27137">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNWWy0SATzYBYexkkdcuLGeC7jtm2eC2Ai8US4pKIJKu_p_JFxgkmWcREXPWSRzS3QOZhnZRdkGBJ73ZqhbazhhK1wCYWVnQGToVVgBsOanBjyb_IXyMble1BF9bSOExSyC1jlLdS-gO7FluwpERiY4kGd3CL6nenKpwXqCgQF2hMBKumq-5BRbKGDPqy8bYQzbKl6Crj1cbqJwMD3KmOLdEV6pNR9hhToxjem-BG1TEb-6B-Yv3CfQKfFRXNjY4M5Yw3JpOLYOkXU3WmAc22pjtABbdHDE8YOTrzF18YPE_eDrfX93GUG4HtfZqaz8MwW2caGA9y_tYcb5NXGJ1CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛مدیر ورزشی ماخاچ‌قلعه به‌مدیربرنامه‌های محمد جواد حسین نژاد اعلام کرده که تصمیم این باشگاه برای فروش حسین نژاد قطعیه. هر باشگاهی دومیلیون‌یورو بدهد و خودِ حسین نژاد هم راضی باشه این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/27137" target="_blank">📅 11:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27136">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca19ec3ee1.mp4?token=Xd8K7G3H1Ix1vMUGu5e3Llcekp6-df-ffc1BR4We-w-mbkVaaSQ80xJAHp5q0k0yneo6S5uyFO6xXKhyocaRSRMxQExiKUaKmQiqrCPnsEhTjpAWPiviwW0eixGtTxiZ5ujAHKITdxiWGcSIPq5cRmkGJqsMcMdhq69CrrTr_LYBBRif2ILV1RDpsMulf9Zc3EezAQaRxC95mWmTynwJr8Sj1_oDM-LSSpoJCZOPnpeqyV8i_kmKfKU8kxmuKsDEcapTCYB3kWC9PfaxpS4AHBF0vf47Lvt3uZkn4W6Xpy9l9OMy1ERJG-hZAcjtsWpCabaIsMCMeBdkbhc4Ix-I0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca19ec3ee1.mp4?token=Xd8K7G3H1Ix1vMUGu5e3Llcekp6-df-ffc1BR4We-w-mbkVaaSQ80xJAHp5q0k0yneo6S5uyFO6xXKhyocaRSRMxQExiKUaKmQiqrCPnsEhTjpAWPiviwW0eixGtTxiZ5ujAHKITdxiWGcSIPq5cRmkGJqsMcMdhq69CrrTr_LYBBRif2ILV1RDpsMulf9Zc3EezAQaRxC95mWmTynwJr8Sj1_oDM-LSSpoJCZOPnpeqyV8i_kmKfKU8kxmuKsDEcapTCYB3kWC9PfaxpS4AHBF0vf47Lvt3uZkn4W6Xpy9l9OMy1ERJG-hZAcjtsWpCabaIsMCMeBdkbhc4Ix-I0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تموم‌ شد؛ صلاح رفت سوپرلیگ ترکیه! با اعلام فابریزیو رومانو؛ محمد صلاح فوق‌ستاره مصری 34 ساله سابق لیورپول به ترابزون اسپور پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/27136" target="_blank">📅 11:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27135">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1ef6701e2.mp4?token=WzLP6MXzVGAXytmgqIxswZPNU70ilDH3LW-1nsVmZYwQGPBJQx9--IkA-cEnqj366iA9hEd7fxCwAL_6-O_Votjl9jq4q60x-SGGzpUtMRlNermPIFgZ_iz5I4-FEckMDFYWCyFMkrZDBN_4mUL99t25A4uIojVkoS5z6uWmgSqqKUQkuVPG1QFGDRqneE9DibECH7WwMXPFt4gSSrgaL3a5JvypEjcNUk0tsjHQFiVI_cdE8w-x6icO15KmIALsiYeBjqij45eiTrzSB1S-WVgZAGWpdrt_tfrFrjrUH_1KwoeKebugWJhMEADL3F3nyfKfiSDfcA4RL5Sg08g6DDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1ef6701e2.mp4?token=WzLP6MXzVGAXytmgqIxswZPNU70ilDH3LW-1nsVmZYwQGPBJQx9--IkA-cEnqj366iA9hEd7fxCwAL_6-O_Votjl9jq4q60x-SGGzpUtMRlNermPIFgZ_iz5I4-FEckMDFYWCyFMkrZDBN_4mUL99t25A4uIojVkoS5z6uWmgSqqKUQkuVPG1QFGDRqneE9DibECH7WwMXPFt4gSSrgaL3a5JvypEjcNUk0tsjHQFiVI_cdE8w-x6icO15KmIALsiYeBjqij45eiTrzSB1S-WVgZAGWpdrt_tfrFrjrUH_1KwoeKebugWJhMEADL3F3nyfKfiSDfcA4RL5Sg08g6DDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش‌تند رئیس باشگاه رمو پس از رفتار نیمار و حذف تیمش توسط سانتوس در جام حذفی برزیل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/27135" target="_blank">📅 11:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27134">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMM7X8wCgTx4Cjn_EU1iCvBYJ2g1LOXyhdXs3zmLyPl-nzJuNlJOXzHEdcLAqa6o2LklHTRflCp4_5u1ntZQgR8yNy0IDy1jaKVRD3cVEmaFVlIvoFUrUaFqQlh8L6FBoquwMXnzEsX7ANaPIXZ9COyxzqD9g28J3TzrGS4ZtAMS9P1J4Mj5SgaZS8FmpjQXI92eGc26OuLrVIm8-rogJpszTzTSEv7FMa-TUX1ilqUzhsMDwdY7gqgHP1XFEXdlH0AVma4hCbpZ4kT4qbfMD7ouspZGEDhTkBliKTpSZr7tG-Cd1w6WXuwfpT5jIHUuGEHr7HIF6m6J52LEq1fSjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
🔴
🇧🇷
باشگاه نیوکاسل پیوستن برونو گیمارش ستاره برزیلی خود به آرسنال در ازای دریافت 93 میلیون یورو ناقابل از توپچی ها رو تایید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/27134" target="_blank">📅 10:59 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27133">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c293e9daff.mp4?token=EEiqmYuMJzUCQ_-3RRT9JyxAdCPBQjky5OTSThapb9spBthYirQkSA_jEjs6Duv0w_npUNzy8Nyied6ZHCkvj_9yZ6anFh7FP4bFBDIrCDsVQxBdbSWaZOuklGa_tR4vAKJdX2BCzpPeC-zOaRsJ3d8ZzsIE-ldQZXBwhemSQdpOczpS6S1SnELKm5Is1vUMZ5qwdnUfskXcHlRf8hfFu4WlLuPGag9vEbpZIgv_xqwT8WQJRywsvGAhFpJ3-OFESn2arNSueCny7J3_IgX2XdbSs7NNoS0SK9RGZFXXQueZDHpuSg6AT5d9hi2cvMJNNFpoLTCyD-LQNJR3Mn4Yfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c293e9daff.mp4?token=EEiqmYuMJzUCQ_-3RRT9JyxAdCPBQjky5OTSThapb9spBthYirQkSA_jEjs6Duv0w_npUNzy8Nyied6ZHCkvj_9yZ6anFh7FP4bFBDIrCDsVQxBdbSWaZOuklGa_tR4vAKJdX2BCzpPeC-zOaRsJ3d8ZzsIE-ldQZXBwhemSQdpOczpS6S1SnELKm5Is1vUMZ5qwdnUfskXcHlRf8hfFu4WlLuPGag9vEbpZIgv_xqwT8WQJRywsvGAhFpJ3-OFESn2arNSueCny7J3_IgX2XdbSs7NNoS0SK9RGZFXXQueZDHpuSg6AT5d9hi2cvMJNNFpoLTCyD-LQNJR3Mn4Yfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش‌تند رئیس باشگاه رمو پس از رفتار نیمار و حذف تیمش توسط سانتوس در جام حذفی برزیل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/27133" target="_blank">📅 10:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27132">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRg7RMSl48oCtrspFKRvh_qUNdNjiC5LRaXjlu8M_-T4vRPtstxnoQJAUgxDOtTtaobiSCVtrsrRsnNL5EOgvo-UoRRlxnSZMzFWVcIlq2aFRz6P1vKnwMEACKqUd9foBYCna1_D4R4uiKAraK7uH1UmK4ajw-IFl-DzH541p2oqSj5lZd3ubGlW3aQifo-ANTkKtdxrDNlRevC9Q9vv9RsYrNYpAFWkDVJ_qZUgfYl5mPf2qnsDZEuZW01ioJPhyttrWEQlkNRPvmjDzJh-60Tk9I10NlepWeWsxQDw7p4X-cQDryfmXKxfXOtPABJk-tM86ppbHjLfFt9PxWB8Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🤩
با اعلام جرارد رومرو؛ دکو مدیرورزشی بارسلونا هم‌اکنون‌درمادرید بسر میبره و قصد داره که فردا بامدیربرنامه‌های‌ خولیان‌آلوارز جلسه مهمی بزاره تاراهی‌برای پیوستن‌این‌بازیکن به بارسا پیدا کنند. چند روز پیش مدیران باشگاه اتلتیکو گفتن آلوارز خودش رو هم بکشه…</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/27132" target="_blank">📅 10:29 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27131">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hl0dvr8zD-3uvR0nWwfvi5HAdNjqg43yfHOkkOyVM4o1vXDe23MMnQqfxlg8TGOdj97iGEqTNL_jw0iVaZf7_t0k-inE3DReKLuhr8cY_POKVx7ACPKNV1cBpTyfEsXTvgqKhzVDa64ASd2d5AnC0lFdJ7E5LpkYsFrGeInPOxIrV9n-RSsLHkWmSVFSMr7uqLhllA13qODGdJYsgjoEiiWVPZGB-32CuXY1cluFWWxmu4sjDrC23eU-miDTj--K9cvxjs1AzUSYaC_74I8M1NK_f0f9cMFTMdhb0fnGluPeedfTUYU_LkayT9mYKfpT0n2AEDQVowN_pYuQnhD_SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ بعد از باشگاه‌‌تراکتورتبریز؛مدیریت‌باشگاه‌ پرسپولیس نیز با ایجنت ایرانی یاسر آسانی ستاره سابق تیم استقلال تماس گرفته و از او خواسته که یاسر آسانی رو برای پیوستن به پرسپولیس راضی کند. حدادی به ایجنت آسانی اعلام کرده حاضره اون رقمی…</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/27131" target="_blank">📅 10:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27130">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7ky3MnN16YfvEYwMV67zXITc0tkBtoGTHMDWvMLr5DQ-RbIjbHwo9n1p_UkVmXk6If4ojOA7GeuHMgrsajjtj5r7HszA0stC4lhDA5r1m7_Wlzqv1XeuaX4XLwe0wxyWpbwGH-SatELoo_UQTqZ5lLDusVzvgvQCoGlfOiCExRdtm7kCz6Mtsq2bj8KXfGYY9iVRzt7R93qkp8hX03jTSdGPL8IkQY0lfmOO7TGnznDPPkif7hHu50kIISxU-GxUCO3_YxRZM9sg9EKEN8GRm_0vkIQhQoeS8UIRRtUzO0_VUtVojcng095rJFXjTY9UV4w3jRvr1fcILm94m7g0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
درحالی‌تموم‌اخبار این روزهای نقل و انتقالات شده انتقال وینیسیوس به آرسنال؛ ستاره برزیلی رئال مادرید بی توجه به این اخبار با دوست دخترش در تعطیلات به سر میبرد و در حال عشق و حاله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/27130" target="_blank">📅 02:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27129">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrsliZhPsfmGfE3md8cRj8w0XJGesqZBr_zPdRD7tQ_sBUb_g2YXGNEVycJkHwmP_IQdEmKwbYz1qIB7EDOXWLUIinRNA6rEibVrzFkuOGTXsms1yejIBUuGA2zpt9s9Qs2kNlSt8nWUim3C26ogTSyXxoButVLNGe44BgH-rjOf5MBdNaHN59EYn_HFZnGnN_VRksAACA5sV8v03cZM5n3dIaVDl2rakE7A9BsE5tEauVapedTJdchgsCR0kxbRtJ6m_q-TgrVl11f1wTbrOARKjCo4yAnGGcwGcjWqOE1bGxeG27U4tjr392c029g3JR5ZhKk2VVx9Ixrd0MjfhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ بهترین‌و‌باکیفیت ترین ابزارهای هوش مصنوعی که از همه آن‌ها رایگان میشه استفاده کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/27129" target="_blank">📅 01:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27127">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CeULr1oUFwOihdmcaW-6UJw38O9nsUgmyI55p4YCQ0WxTkuymeEokRoPeWZFnwUtYmu1R-0vwRsBxqYp-yCZORDpd8ACWh5cJ1Prn1vOouQ075xuGdn0wsBsX7epiHRoNolS6has8gjlaRECcVoxzlnYm3JCw-uAF8AWpcfVBbsi8pwjhuZsPS8gQuG6xzI5mo38NeJZPwwi6PX9mlZBE51_idhl9X57WNAbvZDDbZl3-JGBdcqFxJAh5Ib23EHyk2Eicb9BA6E-3H8VBuinXVqhfJcapI5-DLcGCnNBsMZUCjezh1JLXy2a4YReAI8EUSaYnSwoLmJQDU-aW_LBBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛
ازدربی‌دوستانه دلامادونینا تا دوئل شاگردان ژابی و اسپالتی در کشور هنگ کنگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27127" target="_blank">📅 01:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27126">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A31LIZJxfrAmqC2EsXKBf5MS_dUJJv02UsgnAdA2g4neE1_V9PaLgHEiqcH3dzr_mKd20jtZJaLl1pzHCa04BTDGGGhpHWu5AKfOx3YY8xxuChikW5b3LAP00ny-PYhasmAEaAqYWWsZe_lB6FmuryRz8BVV9ekeWvnhOO7YfpJTyiD3np3wvdx78bNxfz28QKbJ-N4hitxMq7fjrrb1Uz46rW-apiM9MJTqh7Kdtwo90cUrQ5pE9Sz9m3OmujrUeAfdU1tdag223N7cWfeY5bYphrHH52MLuZtp8q4pLVwfLK1jgH8GkUjNVZi5IN3b6abWBsyZ2DOtJFJ6sC3rMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
از باخت ماخاچ‌ قلعه با حسین‌ نژاد تا برتری بایرن و رم در بازی‌های دوستانه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/27126" target="_blank">📅 01:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27124">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqwfPnQAiTYLWODoMwg9Nd-Xfm1rsqAbkGM_WgwJOeDXrrFurdsxVCgh0YaDqkNijjt2MgEQBvVZZC5NlmLsNhSA1U077VoVImZog4vvcmEqS_VWdrN3D6fF4Glmykq2tZCAO7iqpEmcyTDK_9eSUMA7heIe5h7UQfoweL-exB1Riwker_d6VzBcoyAujfTpnlaNC76XIPdu1TIDuUEklfMbfoEANul9ax1lxeGm9iIY60dXkpsVoimNEIf3WMi0Qnm5int4d84L939r2PAMSNXuaGfBmtXnWSjmvxIBxRv1p4WN51Pdm6rpIvMCMDn0ryY_Hu8ZEuNQva3Qxa-fNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تموم‌ شد؛ صلاح رفت سوپرلیگ ترکیه! با اعلام فابریزیو رومانو؛ محمد صلاح فوق‌ستاره مصری 34 ساله سابق لیورپول به ترابزون اسپور پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/27124" target="_blank">📅 01:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27123">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGoYkdi6D0hbKh6sVvQYmWcNI5AYIuhIvMJS4DOWOS-pvCW51teQcDSqvoEaKGGzVzf-jSV1srJmWwBauKGkIqks-Zq1HpCb--Aa81cBBStCaVIoE7dbfy7JN8G_jyBrDe7FcmJjYmEwjwGYIXlsbgjOA3eL8ZruRN6u9XXE5T8OqqWr0_uR2ZX6CEP4bgEAJfsFGtKS0Rqrpnwx88r8LvfMx_esw5BfNMtodJeCjhlKQT7xjmZ-BVtra57v0f729okbM0O1iLQIPYAoiYc87_3B8glR0tzgg6HH1kEZvk49dKoEfSaqV6dEC8Djwwa4p7ufGx4NxCZbN-OCLb33fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال: مسی؟ فوق‌العاده‌ست. من به نصف دستاورد هایی که او رسیده بتونم برسم بسمه. یامال برای رسیدن به نصف دستاوردهایِ لئو‌ مسی فقط به 455 گل، 205 پاس‌گل،660 تاثیر مستقیم روی گل، 22 جام، 4 توپ طلا، 3 کفش طلا، 4 پیچپیچی، 6 قهرمانی لیگ، 2 لیگ‌قهرمانان،1…</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27123" target="_blank">📅 00:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27122">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgiyL-E1qUfmW6D757sATqI9GthyFNWvf6YF1Xmn50PFcjiLxvyiFikrVeleCMud5JnCDtsqmdgX059iEPXIVnwnIOi9-03p7odzTgq7Qx3-iuFZutKzdi0utjTgH6EGowqcS5tuApmXtQGjGq5s36ZOz2a6drdbM0JDoNmP38XDoOSFqvV1Sc3zIFKtViZW0UF2OakRsHIU9Y3L58_uxyD1i-3XFXRUbNsIaTeNtmRPO4WjLZJhhyl56f726WyboK9ccKFu2baibm_Z3vZfSVkdr3QhUx4mTk70y08v8aEQrXXmQxF7CN3VNEGseOjFHrWCRquNbKcC8mfqNFDzaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
سعیدفتاحی معاون‌ورزشی‌باشگاه استقلال: قرار شده بود امروز عصر آقای رامین رضاییان همراه‌ با مدیر برنامه‌هایش به ساختمان باشگاه مراجعه کنند تا ‌اقدامات مربوط به بازگشت او به این تیم رو انجام بدهیم اما برخلاف قولی که داده بودند عمل کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27122" target="_blank">📅 00:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27121">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sc47p_qbLF5lJB74aZJhhcILeACcUp5WPcXT1a7OYDpdrkU2jiQ7YnHU6asP2s8LIGv0Wf03BToczEnZ1-NMmULSdd9PnlARvyuNNX2rcZX_q6WShzq4e4szVnzRuUyZ0BU495LzYbN1eN5tHiRJGCG7SjkHhN0O4ubsmaddlCRcYe9stmNG3SECwfMqYJsNUGKNzEFjsKZfWwh_VYIwuFkh7dB5paLOdz3HpDObbfOVN-OKyza-yiG7e4OiZwQHmPOcIeSRuT9OCqpOFmJi_6RqMYbM4AuwKD6Ym_pvCepcqZngolOxivmegDq_aHC2AOgnA-2Wo0rcMi3mzwMnng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
طبق‌اعلام‌رسانه‌های ترکیه‌ای، محمد صلاح فردا ساعت 12 ظهر به‌استانبول خواهد رسید تا کار های نهایی برای عقد قرارداد نهایی با ترابزون‌اسپور انجام شود. ازطرفی‌هم رسانه های عربستانی میگن الاتحاد میخواد بارقم بالاتری هایجک کنه صلاح رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/27121" target="_blank">📅 00:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27120">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owVI2mooV889DBr3NfYoliu5LwKFe76z7c3XWaY5fHwPCWUVVSk59gVsmIIcI8hIKd_2zlLDwrpGD7FGkiS-cqrErzItD0VS412rDO0EyfOzbNkAUwiscMrlRiVsNBvIdxfFSfJfMYN-zMbMlLrJuT1hFwgv-sBEaqfTJUxFjV3M1oDrf21rhsC9eESF_hR8iOcoJ5D-07Mqol5qdMmDLAf22nyVWjV-wvCbP1Q0QnJn8SbqCMv1iVZSSFZA_Wx96Pvk5iDdlYqMI91cueBTchmKOjY19gB9S1u2OwIU4Ltnz4xWqZ4MvqFbLIp54VNNYukWFrl8IdkcnrN4lca-bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال:
مسی؟ فوق‌العاده‌ست. من به نصف دستاورد هایی که او رسیده بتونم برسم بسمه. یامال برای رسیدن به نصف دستاوردهایِ لئو‌ مسی فقط به 455 گل، 205 پاس‌گل،660 تاثیر مستقیم روی گل، 22 جام، 4 توپ طلا، 3 کفش طلا، 4 پیچپیچی، 6 قهرمانی لیگ، 2 لیگ‌قهرمانان،1 لاریوس نیاز داره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/27120" target="_blank">📅 00:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27118">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8a21ccb63.mp4?token=GAIttvUZtqF01ObG_K5tAVuEpp0WWPJnhUh6bYdHqpuiFKhsuE9wtBTPq9gXdXLuv-TSGuwHI8xx1bmPvenDK_BgUcxLz9L4bZ5eBFvSXpMCQFyzDaBHyXUsW17V-3i_TTODaB2PaSeTIkYBk8No-OWIJCjZEKYA4TXamjBnmNKv49GwUJIF3a9J50zfaccQD9RiqL2LoO_WZlJX2qQtOZvkkqCWR_jvWMR5narkSwHl55e940PtaOF8_vhE-5ra_tLBEe12rQwSY3GVuSZpVAyLQQkEBBJrINzDknxYr61fxr28GEDVjKLn2LwpGlLqK3FfoVtdDB31lEtSncdH2zxrnfdI6h5qElDisFPCB68vrNzqUxmtq1b4N_FCrppTX86cQhpLtN5LHXAHFcOS40n2xJS5GQJrqLlQlTdbpFWfecNFMZk4TOZeKFrmTlvPKdKkMdTI7-6-mbvmEcvPE2Rn584CRhUgYTaStR3ALssUAeK8i2zMy3WuJGICBud39j3px_8xFd153YfA_YmEqUlDuyfuK53tg5IYm4ZTBYaMY-UyLX8hooJmzvhalNel6WBTrGMgENleWJHpeBLf-gFsT0P8pygiQMyfMDplV6-xFGbWN_W4G4tMhFirSDu5XNVpbV0s__75_BB5HeUL8_LkbfK8qJFP7J-miIOLUaM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8a21ccb63.mp4?token=GAIttvUZtqF01ObG_K5tAVuEpp0WWPJnhUh6bYdHqpuiFKhsuE9wtBTPq9gXdXLuv-TSGuwHI8xx1bmPvenDK_BgUcxLz9L4bZ5eBFvSXpMCQFyzDaBHyXUsW17V-3i_TTODaB2PaSeTIkYBk8No-OWIJCjZEKYA4TXamjBnmNKv49GwUJIF3a9J50zfaccQD9RiqL2LoO_WZlJX2qQtOZvkkqCWR_jvWMR5narkSwHl55e940PtaOF8_vhE-5ra_tLBEe12rQwSY3GVuSZpVAyLQQkEBBJrINzDknxYr61fxr28GEDVjKLn2LwpGlLqK3FfoVtdDB31lEtSncdH2zxrnfdI6h5qElDisFPCB68vrNzqUxmtq1b4N_FCrppTX86cQhpLtN5LHXAHFcOS40n2xJS5GQJrqLlQlTdbpFWfecNFMZk4TOZeKFrmTlvPKdKkMdTI7-6-mbvmEcvPE2Rn584CRhUgYTaStR3ALssUAeK8i2zMy3WuJGICBud39j3px_8xFd153YfA_YmEqUlDuyfuK53tg5IYm4ZTBYaMY-UyLX8hooJmzvhalNel6WBTrGMgENleWJHpeBLf-gFsT0P8pygiQMyfMDplV6-xFGbWN_W4G4tMhFirSDu5XNVpbV0s__75_BB5HeUL8_LkbfK8qJFP7J-miIOLUaM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
فدراسیون‌ والیبال‌ ترکیه‌ به‌ این‌ شکل از زهرا گونش و خانواده‌اش بعداز قهرمانی در لیگ ملت‌ ها تجلیل کرد. گونش با درخشش در لیگ ملت‌ها یک تنه تیم ملی ترکیه رو قهرمان رقابت‌ها کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/27118" target="_blank">📅 23:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27117">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVVIgLTbsUQn3UV3poBMFfMCwD22Xud6--KjXMcr9afwrcXz82mBC5Qmbmlmm05-6VTSfNgXGXvCtsozpNDkCVfoAyV5Laf8hxNrtJfrJcswd6Xb4FP5BcPLbeUSnYjUctgyLVkUyB_xWwmY46sNSY30G3ffsaHoszeorWMSl-U0p7Ws3ZEKuH-mOJNRQzX2xrZWwlsdQoHTjGoLt8dnhNRhsiSwQhl_dZa4LV4M3DibmkT3omISEWEryStXYRtlpliUTaVlERFtTKvC7lPLQafJcv7R3H4Bwz1uj9COmL0O8S9uhkfCA5fIHnKMFRKCSadyvtq5isowOaR4dR4kxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
رئیس باشگاه اتلتیکو مادرید به زبان عامیانه گفته؛ خولیان آلوارز خودشم‌بکشه نمیزاریم از اتلتیکو جدا بشه. 100 میلیون یورو که هیچی 200 میلیون یورو هم بارسا بهمون بده آلوارز رو بهشون نمیدیم. مصاحبه های آلوارز اهمیت نداره. او موندنیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/27117" target="_blank">📅 23:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27116">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBtdyRi82lW4F23IHS31wL3LvR6wgi8VXgDvX5tugyF1UHiK3M50yx2WFLGHM88yPW_wkxT4ob8ZWw8t0YPCVJjQB1DQPc1dK3C0x_z6hSAPLFytrl0AgsekBe_TpXojWMdujyiZGw9gYde7GjOyr56JEzyH5kt7BBQ8VlPrQQeUO7tlILVEnUl2HILTz0NTo8QuLEmaeV4tWxB_zYQT6ZBi2WZKXlhYDEH4snQmKoMuKJgAaDU8KvSSxpt6plqKwI0ASu-cXC3HObIpENQ8lRUDLouIs1FEbJfoh6VyR7_ulfFgzPrDNmO5F-WfT-qusOgy7D_UCbulj2wMhdkbqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ مدیربرنامه‌ های رامین رضاییان امروز با مدیریت باشگاه استقلال مذاکرات مثبتی بر سر رقم قرارداد این بازیکن داشته و قرارشده‌ که رامین رضاییان عصر امروز برای انجام مذاکرات نهایی و عقدقراردادجدید با باشگاه استقلال وارد ساختمان این…</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/27116" target="_blank">📅 22:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27115">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52510ee628.mp4?token=G_Z3xZzLIi4qnOI26jgTEKMIoRJUmjqVqMoFxfwGmx9ylcnT43cF64v8jekMdIYejLYYKjB4oFiNVYKWw7CgZx_7QN-9xgs5y22GQRQ0TxQDsUrGU9ZjEHtC0stWOQCvoU8nFwq8kgSRdnxy9Jp6rOq5ML3kcvjn9-MEzgHTi-jZXE5fAo7LlxfJbLKgvijvXGONiv0fDtYaxXTFg1FhoFazfyGN-kpxHumzaHezhzlNO4hZBa5MWTVOXo7VpmcvbSlTeZ-eHv7OvK9g3vsCZ7-jhXwrnTL27f2QeVkaBJRtMbtM5xpcwZ6SST-Tk1Y34CslRyJB_6pDqQFisRKXLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52510ee628.mp4?token=G_Z3xZzLIi4qnOI26jgTEKMIoRJUmjqVqMoFxfwGmx9ylcnT43cF64v8jekMdIYejLYYKjB4oFiNVYKWw7CgZx_7QN-9xgs5y22GQRQ0TxQDsUrGU9ZjEHtC0stWOQCvoU8nFwq8kgSRdnxy9Jp6rOq5ML3kcvjn9-MEzgHTi-jZXE5fAo7LlxfJbLKgvijvXGONiv0fDtYaxXTFg1FhoFazfyGN-kpxHumzaHezhzlNO4hZBa5MWTVOXo7VpmcvbSlTeZ-eHv7OvK9g3vsCZ7-jhXwrnTL27f2QeVkaBJRtMbtM5xpcwZ6SST-Tk1Y34CslRyJB_6pDqQFisRKXLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
درمصاحبه‌جدیدخانواده‌نیمار؛همسر نیمار از قلب بزرگ او گفت؛ ازکمک‌هایی‌که حتی دور از چشم همه برای اطرافیان و گاهی حتی غریبه‌ها انجام می‌دهد.
‼️
البته ستاره واقعی این مصاحبه شیرین، شیطنت‌ های بامزه دخترکوچولوی فوق ستاره سابق بارسلونا بود که تمام مدت توجه‌ها را به خودش جلب کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/27115" target="_blank">📅 22:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27114">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFRwrtQ8wluX4WryN7rMr0noG0o4RAbhKjln-ijA24jcWx2ewZO_Jo6dcNlUWK0rzLrtSm9WeD5puTl4gtD2Ef4FMBT1URxW7YNl0vq2nweedLjEXou3-2YC7N_hOxk53RYVmYdJzse7hN5xtTuy15n3RvFwYtDgduBaKRahiiSGaNcHLk-5Fw_FMe3N6ACiHTc4bKaoolR1l5ZJRWcyDzyAukRUeYsj-DC0AJODh0bTdEqY3ZB7VQAeD6LKBIiKdMYhT8-x264KNGuUXkfCPk9aU2AKPdrqCjaPOD7wP-16p3SRnQiIrHxRb1GVyI14PyjMb1CL_vNejv4l4rNeAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌انتقالات|نشریه‌ سان: سران آرسنال به درخواست میکل آرتتا به‌دنبال جذب یان کوتو مدافع راست 23 ساله دورتموند در پنجره ژانویه هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/27114" target="_blank">📅 21:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27113">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWxqW5f9be3F7H4NpI8pTsha_ZRXemhskQ0jvQ5vFeztp10Xbv3mn5s3TJ5aH5IUaP67so6HaSSXuY03ynH-TrLbJ_Bhec44NcGNJ8lHI1zl-nGmuyn60Mg3Lg-k9WgwiBTyq9YT28hUOZpS-wosEihX4UiZbrVjUrxInmcs5OQDTyO16-oW0ceV56yleO-Rh-Gz1CvwNTjv-iLT4klCThUTqH4wl6a_TqmQ0hj1qE8Keh3uzmzfSJzmRNa-rJqby0pSE-x9wHYAj3e_WUneKCdSb8TDTLW-cUMfXBGY1t8FlWVZxkXp5FHkLhf-uty1QLMVT6x_j8kkZoAIgIJ3WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلوس اسپی مهاجم رئال مادرید:
الگوی من در رئال‌مادرید کریم بنزماست. میخوام با گل‌هایی که میزنم همچون او در مادرید محبوب بشم. برای دیدار مقابل بارسلونا در الکلاسیکو لحظه شماری میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/27113" target="_blank">📅 21:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27112">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sM28YZ69CfXwiAwHN5KnnwyoylJwbAeaIyP1o9rKYvSyxmU1zqsZmvsLHiSEAeP0HyZYWhSxFZjNwO6uOM-NP2uTUGM9H0Bi4IAPgwV1P0cEwcH4AHGaWFaVb3lZDkGIeHJ9eGav_uht_YmfbiWZp0UtkbbnEMG1_j0tzsVrq7Tkm0ZWPrVmGA0SIrew3aWmsydQV1WvIaz8gJNnrHDCPhNJgPqtYRvCEwCbGBgySFL7OgDsjfvNmBsoUzX6aAXqLQBxvV1I2qsrcTVYWurSSwB37D6hVnWDjSmcp7E_QNohu4WKtmAVjwsHneHcr86tW7vnbc9cPlp_4ZWMfDtiTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ مدیربرنامه‌ های رامین رضاییان امروز با مدیریت باشگاه استقلال مذاکرات مثبتی بر سر رقم قرارداد این بازیکن داشته و قرارشده‌ که رامین رضاییان عصر امروز برای انجام مذاکرات نهایی و عقدقراردادجدید با باشگاه استقلال وارد ساختمان این…</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/27112" target="_blank">📅 20:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27111">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkXW6EwwEr6B_0My76yZnYqrAx0dZ-iTtU1hulMHoNmtbCrjGJB3ZDSLAaY7BDeoK-DzHmH4tjbUt157IRg3FoKdepwZuQpgIOo3hYx7ATia7lWJaqX5cUu8Q8ZjG4dM8vQobl5ix2ojDMMZSzC3YVCLaAzJkqGFO8-XczsRMXweKwxdEBE5btmMiA7cfJ8pCQ1F5_78MgHHZcxMrUMjZZyFub_slIHjzB5tGRG1oIUhSw83ukxu7cpq18Csg2Qp2SbGo3NFhd6B2HZ5IrggUvurORmO51pA8YomwMBJEhUaCY0YuwYZ6foUsPV1uDHVHo9xgdqWSBgCb74jpCpnLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فابریزیو رومانو: باشگاه ترابزون اسپور ساعاتی قبل‌پیشنهادی دوساله به محمد صلاح ستاره مصری سابق لیورپول داده و منتظر پاسخ این بازیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/27111" target="_blank">📅 20:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27110">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyurSM-pQDSKL8VPV46z1rjuCb0IEfDoYvoAntZwwq4UTwi4TeA5PdgStVt2T8ZAp7hFQxqgWZH_wibjGNEUaAzqTow8kcnlfRUuxR9E4NlfMeaU1222lTdubmr17yvBk0edHfDOnQ8kWQ78-AoplbEraqF_7I6ra4_bSpE_kZLDOvCcXCPgZp5lnyAgdUca3_OzIrgb3hoIjFC3Gu7SvrjG1R4lNs1wSMFDnGVOXz63jPr0lKGYsIVjgTRkxKkQ4GR5UAGa4nMXVsXHdaFuvlS5dZQTXjOZrmAFdAx1-FcJvBZ4pWaxyY12E5_Ua-SCeiA5u-pKjABww8ya1BS25w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
استوری جدید آلن هلیلوویچ هافبک تهاجمی کروات سابق تیم بارسا و مدنظر باشگاه پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/27110" target="_blank">📅 20:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27109">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gig7R9kV6PmXJiErCwEF0ims6LgxY7YlJ05LwNDd1RyKTprWvXNN77z5wubjq2kTBuIdwOSF1MgsD3FUC8ngTHI72FNo3zvNsDq7kZnrVgp8lelieDigxHLtvsoh_Xu-bKGrLK4KoIao9WMUYM8ofGkIRh_Nc64Fr2dcF8UQNp5953o6E33Z3fxI57JSLZNaV4EHayfG0CfDXWNqldldD3XicqB6H2m1UNLhZLPTw6YsU1bqrRlOZ1TVQPyOOM79bOUUmDYb7vFfwQixX3jiK_i1lEqUotNmunz6ZXYXSL7115vk4azJd8F3o5VsxOzy6Ch5UwRoXwJKGBr1ZJll9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
نشریه‌مارکا: انتقال رودری و یان دیومانده به باشگاه رئال مادرید نهایی شده است. بعد از رونمایی از این دو بازیکن پرز پیگیر باستونی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27109" target="_blank">📅 20:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27108">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mU3qRSW0MIRsRV6yx_nAagNsinXAHFaBwzq71kfs_Pc9bsxo_XZxSB6sm35DUTz2rzqnPxP6_lTS2dwmuxU3P9uTouZdKzZB_Kd3eNXsNwYk8DsfUEKu9pSQV5VnAXEE80mV6-ui8iWZar2OQ4rXCmtw5P_YjvJNp7MKoItuDH7aNhR_AYAlS00mTmgTsy_m0NDVdOp_zFCxxRl2m30Q9VCwi16zuufCOVjWlqdWmnJb30Ve3rrvKlEzEM1GjQc1YlFvi-m7RFGC1kLShFJHciCPteRUDplkn-R3aq-L-gP2wTwtdqzkT8aiEJULJg2uMCnoLesBM56_eS0ESuzepw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
پاسخ‌نهایی باشگاه‌فولادخوزستان به پیشنهاد باشگاه‌پرسپولیس‌برای‌خریدابوالفضل رزاق‌پور مدافع چپ‌فولادی‌‌ها: 200 میلیاردتومان نقدبدهید تا ما هم رضایت نامه رزاق پور رو براتون صادر خواهیم کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/27108" target="_blank">📅 20:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27107">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKRXLeXW_0Z3olb1KpmVEsmguH2kB2k4kJ9aeKEq8HRLg25u3roso9wIIqJarccLViiIC75M8tp3oaFFKJ72vFP6IV8Nbov6JAnSNu-qtr1WTvjYfmr-AUO7GM2Hk7FFpP8b-b2zTvc285rSauHdSebtqp8JgtsmdUphEjPUIRHLWg9WwrAnJ4ykL02A5HVbIFV8XYtQPX2ZqsiXoAGOiLjQat58Zo6up4H2_rlozpv7B-lFSbKemmkPH-reE5_kbh_nEkKHpEQFEKHsaIgmioLnYcj8aO42TOZ0tP_HkqjC0KxdL8uVUQP3RC_HySv54ZpQBbgdY-KQ7DTaj05PFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مدیربرنامه‌های علی نعمتی؛ این مدافع ملی‌پوش باباشگاه‌لوسیل‌قطر درحال انجام مذاکرات نهایی است تادرصورت‌توافق با این باشگاه قراردادی دو ساله به ارزش 850 هزار دلار امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/27107" target="_blank">📅 19:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27106">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd6169d08e.mp4?token=a3qH3ZYop6imxiphCXVtBJuehPCqImnLuw2gGwbaZdFP3kOAymEvhl3ER_d0vdkbnvw3PbWxeuGf1I7YjakR5GrgigegrDqwub-3hom3cAczqJCmOsv3FKCJ6N39peh7miLwySebtcV-DFOjpQh0VL0B_2nfZ4mi-c6Jv9I_0Sb1ozkHAux8WMaJPxGcTxe-g8kHyFJN9jDtK607Ce5v7r9d0qWwZAL1jxVzFRtkBzIuIDX2RYS9CvTxaHhK8EnpigCut7U4fGGvrdcjqXjvnwgXZgMNqIWWnTVubbxMPquL_QJ165e5-jrGOlq3XNlQE9G8G33KQQDvo-TDZmfmKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd6169d08e.mp4?token=a3qH3ZYop6imxiphCXVtBJuehPCqImnLuw2gGwbaZdFP3kOAymEvhl3ER_d0vdkbnvw3PbWxeuGf1I7YjakR5GrgigegrDqwub-3hom3cAczqJCmOsv3FKCJ6N39peh7miLwySebtcV-DFOjpQh0VL0B_2nfZ4mi-c6Jv9I_0Sb1ozkHAux8WMaJPxGcTxe-g8kHyFJN9jDtK607Ce5v7r9d0qWwZAL1jxVzFRtkBzIuIDX2RYS9CvTxaHhK8EnpigCut7U4fGGvrdcjqXjvnwgXZgMNqIWWnTVubbxMPquL_QJ165e5-jrGOlq3XNlQE9G8G33KQQDvo-TDZmfmKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیش‌بینی عجیب احسان علیخانی که چند سال بعد به واقعیت‌تبدیل‌شد! حدود ۱۰ سال پیش، زمانی‌ که عادل‌فردوسی‌پور و محمدحسین‌میثاقی هنوز در کناریکدیگر در برنامه«نود»فعالیت میکردند، احسان علیخانی با لحنی شوخی گفت: «میثاقی رو آوردن که‌بشوننش جای فردوسی‌پور!»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/27106" target="_blank">📅 19:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27105">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSXXZxd6o6KWajmXGlQ0xzcl4wN_vHy016vmgSABxxGoXVh-V37v6bYskE_wwpBeT9nM2GvB96NjqNyz-CkOZIPquXyFHPjF1dVwOXdwOzQW0c61cHvfnSdw-h3l3cFRfOsMx-GOgrpoto8doHMIkMVqToX8aLLXglMTApf2Edz_FibqXHW0Z0b0s-BQVEvc0Pvy3e65Nc31AzAoidGMFZ893YSOnEba2UmVJVJlwzykFiOErTN0ypKRmV1xwOtUtLbLctHOndCWp-L1YDw5I-p13FIowZ-olNehZJU3mY2RLn3i8hUX9Z6jK5OuFaSjjDuNa_nIOqtnKoYV6GKkaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
سانتی‌آئونا: محمد صلاح ستاره‌مصری سابق تیم لیورپول برای‌عقدقراردادی یک‌ساله به ارزش 12 میلیون‌یورو بامدیران تیم بشیکتاش به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/27105" target="_blank">📅 19:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27104">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe05053c48.mp4?token=v4G6_p8TeOY3ZOJbZDdMuzt9eeL3T4zjsIJohp808Z_3oCLES00T8jUQ1Sahj4wKODWNygxM5dqrzuL2leZnUwrv_m6MWOV8K4qJPRQYMdZahRLASL-BGXtnr7Ou-1QUUNxQZaVB1TOkn7RlELv9Nn2RWzMuZoBs015B73O9g7yrCmFN3KHAU2oeik9uRqIeXjz6_DSa7w0KeSSwkPo2FSI4-vrUNqASYBBLoosve1nfoL5pxpkdhInBQBejzUkmltnT9J4PwRiczcI1YD7FzHiexYlqSKqHpZcyZRT4S33Gz56AxxBbt_U7IGVsrjN2EHK9EmMapZYHL-vgPNzbKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe05053c48.mp4?token=v4G6_p8TeOY3ZOJbZDdMuzt9eeL3T4zjsIJohp808Z_3oCLES00T8jUQ1Sahj4wKODWNygxM5dqrzuL2leZnUwrv_m6MWOV8K4qJPRQYMdZahRLASL-BGXtnr7Ou-1QUUNxQZaVB1TOkn7RlELv9Nn2RWzMuZoBs015B73O9g7yrCmFN3KHAU2oeik9uRqIeXjz6_DSa7w0KeSSwkPo2FSI4-vrUNqASYBBLoosve1nfoL5pxpkdhInBQBejzUkmltnT9J4PwRiczcI1YD7FzHiexYlqSKqHpZcyZRT4S33Gz56AxxBbt_U7IGVsrjN2EHK9EmMapZYHL-vgPNzbKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دخترِکپی برابر اصل نیمار جونیور!
ماوی، دختر سه‌ساله نیمار باشیطنت‌های بامزه‌اش وسط مصاحبه اجازه نداد پدرش‌راحت‌صحبت کند؛ همچنین حرکات شیرین و بازیگوشی‌های او دیشب بازتاب های زیادی در فضای مجازی داشت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/27104" target="_blank">📅 17:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27103">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/835360d02b.mp4?token=nogMbD4WT6ohXMIi2F-kD_tFMLlfZcDvF3adZqmK85oTVOs3dhD9fK-KI0MR1f2fyqlHOTj37nsCF67aNj23oWppjnDpOhYWpi7kLyV33ozMa-98jrh1TWnXbZEbhEl7S1HWuYDqZBvO3SJMZtH7e1LVPRg41KXZmVUnPHF7V9-mPBQqH8DbXEm_QRmZUhKWIWab06XEtJcOst4jjMhIL3ZXceUStLpEAc2OKqN7Re-VNTKHVQF4l31VHzea9K8PEOgKcDMUm8V1W3hWWH5V_wRTC2khna0YoSgCguoupyiPn1s_dpGiN2kILuDOIkSvhhkj9WmArEgiZpr1T2FtVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/835360d02b.mp4?token=nogMbD4WT6ohXMIi2F-kD_tFMLlfZcDvF3adZqmK85oTVOs3dhD9fK-KI0MR1f2fyqlHOTj37nsCF67aNj23oWppjnDpOhYWpi7kLyV33ozMa-98jrh1TWnXbZEbhEl7S1HWuYDqZBvO3SJMZtH7e1LVPRg41KXZmVUnPHF7V9-mPBQqH8DbXEm_QRmZUhKWIWab06XEtJcOst4jjMhIL3ZXceUStLpEAc2OKqN7Re-VNTKHVQF4l31VHzea9K8PEOgKcDMUm8V1W3hWWH5V_wRTC2khna0YoSgCguoupyiPn1s_dpGiN2kILuDOIkSvhhkj9WmArEgiZpr1T2FtVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بنظرم‌جذابتر از گزارشگران ماگزارش کرد در حد همین چندثانیه؛ گزارش فوق‌العاده گزارشگر زن لیگ MLS روی‌اولین‌گل‌لواندوفسکی برای شیکاگو فایر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/27103" target="_blank">📅 16:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27102">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAlRwk0OPwd1NDJZXY_3Pp673VlWXMNpxaAA8uCR5zciCyt9729Dn6zDAwlC72a_Zb52JIZG3SgHRSVGgRVTojTpC8xp-Z9rRICUXRLVRn1y192-cfahCHJSvQcoIZSqOkURBr-C_x3mBGkB9VlpsSQ9lYgTwI2NQalf4IGY3hOeLXTurcQazLXaynU_8heby5mPEfPNN6wKqUnBxcily2i_c_DS_8y5HbIgVxZHQH6WsDxe2wtsS1BfEycLB5m0n04C5AKjxBZl6hWK6kNTYQ9bMaxSNB8rGvgZWSfmnjTUIgik3cpsQbsatza0Z96c4Epnz5DrLH592HVL8p73oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
رتبه‌بندی با سابقه‌ترین سرمربیان حاضر در لیگ برتر انگلیس براساس‌تعدادروزهای‌حضور مداوم روی نیمکت باشگاه فعلی‌؛ میکل آرتتا با بیش از ۲۴۰۰ روز هدایت آرسنال، با فاصله‌ای چشمگیر در صدر جدول تکیه زده است. اونا امری در رتبه دوم قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/27102" target="_blank">📅 16:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27101">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40f136b3eb.mp4?token=GIHAiCO3Xoas03Bg8UcWCRB6pyv-V_vOXGizG4uO1uGI2JgDrGvD7Yo7Rwk71ic-P0QmnC4Y6GNI-SrUbV4IwSM0FzECe2McWVJObARLmUAY2xV_Ho2VlDCwXvubuzhg_bRsMnKAbFr2haQGmfwn2aVaAXMCQUQZJ7l3XyWMqe7XuE9aJOmyZgMbJLW2wn0SkezzxkFFOwOflP2uf3LJnJ8sRBV7vPeHxkcUTlkpsKpheztrbrsONo2lhoquf_AHzo1S2Rw33_D8bBixmpm11h1tvXsWYxlfoCLGl_RbU0b8kvVj1LvsMcdSXjv4G_ct0MbA9EnXqTxmZzOxXynAfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40f136b3eb.mp4?token=GIHAiCO3Xoas03Bg8UcWCRB6pyv-V_vOXGizG4uO1uGI2JgDrGvD7Yo7Rwk71ic-P0QmnC4Y6GNI-SrUbV4IwSM0FzECe2McWVJObARLmUAY2xV_Ho2VlDCwXvubuzhg_bRsMnKAbFr2haQGmfwn2aVaAXMCQUQZJ7l3XyWMqe7XuE9aJOmyZgMbJLW2wn0SkezzxkFFOwOflP2uf3LJnJ8sRBV7vPeHxkcUTlkpsKpheztrbrsONo2lhoquf_AHzo1S2Rw33_D8bBixmpm11h1tvXsWYxlfoCLGl_RbU0b8kvVj1LvsMcdSXjv4G_ct0MbA9EnXqTxmZzOxXynAfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو تو چند روز اخیر بیشتر از 12میلیون ویو خورده؛ رونالدو بفهمه تو ایران دارن باهاش چه تبلیغ‌هایی میسازن میاد از همه‌مون شکایت میکنه. طبق گفته رسانه های معتبر، کریستیانو رونالدو و جورجینا قراره بزودی بالاخره باهم ازدواج کنن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/27101" target="_blank">📅 15:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27100">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aO9Zh-2USyZIRRLnqSV2f9JLOdObcHZCXUalfnb1bsI2y4FHlFBWFkjcV5yB4KdI6_gM5VEpNqeTrYfpcpO0SZMNTh6W5HEm-o4u6g5kOXuIxQFEjQ_I9QJWPjuexDi54vPFrlwC_zHbfHznZpXjTdErpX7oh2XDfLbG1hkA90mxb3PjASRadQeqklxLHnnarewvCDGJTrKhIuZkbthVz1ZbRR8dsfu8q-GZKh2iGzKLEh0WQ-RlkQrNhPPYGmgi6x9oquyrl6X_ylIciU6Ml6aNqwYItNUs1KPlv63UMyvpQloP9kYRvUcUFx2Yc0VLiIGkbnH1nvZEYbJaPQkk5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنایی که بهترین بودن ولی از تیم ملی شانس نداشتن و از داشتن یه تیم ملی خوب محروم بودن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/27100" target="_blank">📅 15:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27099">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">قیمت محصولات ایران خودرو و سایپا 13مرداد
🆔
@Persiana_Newss</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/27099" target="_blank">📅 15:39 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27098">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AW9wsNpqhdHIK0ZxJsvDf7v8YJ7utrrkpdov7OJHImat4oPIUOo7J9lWkrRTdnK6bGzc54H4zom_TDU1EH8Q0dP9p2o4OUlYVUs2DD_NENxrkSpBt_KK4OHdOsX8YAXbVs1N-5RkBFInpXyEvfTB_-bO_Rgyt2KJItBrG4Sqjtlp-fqHWLxy9ewY9EcHODgLORpmoGeOSV79EOMZ_QkhraaBmxe61mdzLoKgP5KfkhFkZ3y6ihdMbwJNiUOantbEVVuK895N7jdD9UvHNkzwwjieCJSHDc5VUELFiLL3aj2s-AhLPWGFRvCWLmMzc7V5cn7khL21B8AO1HIkK3nAcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کاپیتان‌ های پرسپولیس در فصل جدید:
حسین کنعانی زادگان، علی علیپور و اوستون اورونوف.
🔵
کاپیتان‌های‌استقلال‌درفصل‌جدید:
روزبه چشمی، صالح حردانی و امیر محمد رزاقی نیا. البته درصورت تمدید قرارداد رسمی رامین رضاییان با آبی‌ها، رامین کاپیتان دوم آبی‌پوشان در فصل جدید میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/persiana_Soccer/27098" target="_blank">📅 15:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27097">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9w-9rUOxyKMZlzxjP-bi9EZ2apNOWJYjJgR1oZK7UpawfWpA4giSqORVIAf7Xq_WqQQFRFpF7Kq7hI_PENQ6bq3If9pHT_Wfh5BSrW_mdR0T1TvBmERwZhSNPFbgTh8bDKRuKPLVA8-rqhH0sd7VuK2xGvHwNszuQOEiNs0TgbCdE_r_WeNt1wyL3zAoEd0aD0AlB7ruP552khN2kZXfpZQevtSIUqOX8-NNd4aDQQUkjUjWmuxuXii3HBIa0Eg_0dmSbyHZjHp4gyxGzYKmqbh6JYQMxtCrGEcZ6NW2-EK7l8NBxTmA4aZldWipBr6owK58b96KVRbEuaYWlYivg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
👤
عبدالله‌ویسی سرمربی‌ذوب‌آهن: دوست دارم کاری که‌سال 95 بااستقلال خوزستان کردم رو با ذوب‌آهن تکرارکنم. بسیارسخته‌امانشدنی نیست. امید عالیشاه مذاکراتی‌بامدیریت‌باشگاه‌داشت اما درجریان مذاکرات نیستم. امیدوارم که قرار داد منعقد بشه و این بازیکن با تجربه رو…</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/27097" target="_blank">📅 15:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27096">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4gHENeKOzg0XxK-8j_JgYhwtWtWyk6VH_dCu8JG2NPhe7anynd1ncQvFJNArLqqFVItR1r0eHBCA-IwlfzRHUFnT02a847e0ndCpw32FLt7LzwJznlnXW4m0999nnjoDxOj5NlBZmO3OzyybwXO4jP57SRia-3TyElyyrL_y1DmwJjzW4aKsLq4qWRxPvLWdHax_086QGuVXmZAOGLPdZ7iCr5NCHkk3xknOTIePifVuldA9Q8HEszmkeJGSo_33l-gltP1DWN3wkowdvMLuNwESmyDJtf87ye2Yn12Hsv1VhgX1DVMiZE3oeXEAj6nJc4sL7pQ-f_Uoi0OLRkc_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛مدیرعامل‌ تیم پرسپولیس امروز به حمیدرضا گرشاسبی مدیرعامل فولاد خوزستان اعلام کرده حاضر است برای خرید ابوالفضل رزاق پور 120 میلیاردتومان‌پرداخت کند. گرشاسبی به حدادی اعلام کرده تلاش خواهدکردکه مطهری رو راضی کنه تا این انتفال انجام بشه. مدیریت پرسپولیس…</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/27096" target="_blank">📅 14:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27095">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtPPiXyBS9bWd0BuNeiskxh5rA1axL-RsqpAKhEhujNhK0OdFA4Z8hvK8F2XmyWpo55A25jVPPs8OI0VeW6PEcW4uzF-IsE9xA96Afu8u8mRe-srK_zufJ7ZAPJiqWluj7VRTMvykJWhEEo955aJ9OhgJY-3tNUh6zhECJZug-e_hU3f9BNsRi-rdmvzxjLDkkGFppPYw22dHa1ps-eCNU3SWbAcyhcyhO7wdWLBGniFvwIXv0oZzG7QypVgVZ1m-bNYJywXW74tqJFsxNh73HRQB3prdL4Z8KNkQzX9zbE050ESys7vbVW576-VASDZMwTAa_TKjVWDK23KnSvEhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌_پرشیانا؛ آفر جدید استقلال به رامین رضاییان برای یک فصل حضور در این‌تیم 150 میلیاردتومان + 50 میلیاردتومان آپشن گل و پاس گل و قهرمانیه. رضاییان قراره ظرف 48 ساعت آینده پاسخ نهایی خود را به این آفر بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/27095" target="_blank">📅 14:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27094">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HO9sNY3cOmadRUYiCZkIJz8e2uvPExUE9xXiEMugh8pTE7GFtisRXVdP6hWp0QFT9lPWNOskUdLMZ9MfEpgSDLVcrFjibmfXoCPnqeOZppVlaHCym6TQseU3yrtj8t78bcTg3GX-dZW9rNEViIpUI6kU5cM3V7whhczxjBl5kIj7Jbq9-7XmlphsF08rXfJzm6JWgpkBclEl70es14BHY_upKkwHgmNJPMvCRbGC3_fvUSllorRw6qS7RH7v66PEojXnWPEMoGNwhHZfbBW5VmQBz_sIV35AZfouOux8531AoxUmOVzt8BqjkhPsjZZciHUcJ0VEPruRjVAcWli7yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
عملکرد نیمار جونیور فوق ستاره سابق بارسا و PSG در کل دوران حرفه ایش در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/27094" target="_blank">📅 13:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27093">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6IcYBKpsy59q_8fZFy4aQhaK5y1vMAYEd2Gr7sEjE-qVxoRRZ9gn0dY45OPueFovtV7dbV-WF-n-51CpVVt8aTDW7H-OmzmNxAM1G-ja_cTCPvUNz9865s1EMKtoVU8A0KAfhQUkNrpp1ZF90R2dzkA-bquG7HEKob2feHuOfrLL38mzd4vImw9m4ijN2hqPK-6BRoqwicg5Qcyh92iNmyICTWvRa7buOAmLk7Dq0WJ-5gAttP8GeioyFxPxmsKrOt-QSQwFGOZ5rXO0lmpq48eFDMtXM3RUhkIVACV_xi1pfkLQ3wqwzzdu7vKsPYnMkYNficpG6wv-U-Y9RBNvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روز گذشته شایعاتی بود که فصل جدید رقابت های لیگ‌برتر یه‌هفته‌تعویق میخوره که سازمان لیگ تکذیب کرد. لیگ برتر 10 روز دیگه شروع میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/persiana_Soccer/27093" target="_blank">📅 13:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27092">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JiKeluE1aGESy44nBpqGl4vA4bl6bkKVJqNxWdu6o9h7Lo1rOsTvPmEmqSQ2eb0-txSiHBQkuWAk71wOHw0AK_MP_wJsXDNAEMTlqP8IHs73NaPsnjaSyFrwtHS_sDJ55OA0_C8NfX7hXLHzO-XbUnE2D62pPhQ8OtDpQd7f_3yDiE8HNyKXElsCltlDr-TM2oPpPplYV61qWfnv6IItCQvNe2umb8n5LZTioty7i7PVA4IdQVkfcaESP0LzPCuwVTmMoK71S4Jx5i35GjLOJszaB3hsefKRUiJT7hj-6J9QmKeAORuOgEoT0iG275a9hIciusDVzruQV2KYM7vfGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
استوری محمد جواد حسین نژاد ستاره ایرانی ماخاچ‌قلعه: پروردگارا بخواه برای من که مسیرهایی نروم که باقلبی‌زخمی‌بازگردم. کمکم کن جایی برم که دوست دارم اونجا باشم تا همیشه شکر گزارت باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/persiana_Soccer/27092" target="_blank">📅 13:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27091">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df9be54cc9.mp4?token=LJtVWDuKl2v5G0oCaBK2j0juJss8JEi53txxNYvcs2yc52_1IY4AlXxqEA3FTrxDNcW9nm3lBO1fZ0gw5nlV44TPA_LPXVwO1S8ulfSQ5p-7TnKS7cuZqqY7CaAjgAF49OBrQ8r56MDP3xOtgDoqfbeYv1TfA5NT7FgcYRcRjJ2ixYmwn9P4cDDfW_Dr-MAuH-uzkHhT2d9CwzQONMGySV3a0WmVLGqRSU3EhMXrSPBwXKC9GYAwTUxrXHRMdBXh9eK4NKpXa7HMEbeKdJa-joy4-LMuK6Z2nvQ2XQPNuMFty8MnjpiSJW1EvBEm_h7eY5AnbQhGsXNzKDAmfNO1Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df9be54cc9.mp4?token=LJtVWDuKl2v5G0oCaBK2j0juJss8JEi53txxNYvcs2yc52_1IY4AlXxqEA3FTrxDNcW9nm3lBO1fZ0gw5nlV44TPA_LPXVwO1S8ulfSQ5p-7TnKS7cuZqqY7CaAjgAF49OBrQ8r56MDP3xOtgDoqfbeYv1TfA5NT7FgcYRcRjJ2ixYmwn9P4cDDfW_Dr-MAuH-uzkHhT2d9CwzQONMGySV3a0WmVLGqRSU3EhMXrSPBwXKC9GYAwTUxrXHRMdBXh9eK4NKpXa7HMEbeKdJa-joy4-LMuK6Z2nvQ2XQPNuMFty8MnjpiSJW1EvBEm_h7eY5AnbQhGsXNzKDAmfNO1Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی‌جالب‌ببینید از نحو پنالتی زدن برخی از فوق ستاره های فوتبال دنیا و واکنش دروازه‌بانان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/persiana_Soccer/27091" target="_blank">📅 12:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27090">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17e27275fb.mp4?token=N_pIGIboOrC_qaa3m65wxse_L5nLORWdt6fi3dFttlLg42iP3fkmk_-UJCjw9QW06gvWoZUpKvAK7mmjrXBCGfPBQ_CMFqNLu41PvqCUWubI4IriLgf16avhnMvWk8j1JqjuRGXZGzXt4gWKrPmFZ4Wb3Lu0d1kdi8lXjWZHJHj8L7QGtc3B0-sctkLNEWLLIOdBXO-06Ub4gTxGinghLj_wevFh19fLTOP73a6NZCdo-tiTTqhjlqMg9pyxINVEtX4icx9hxy1VpWGF_p18HRm5fN-PlqsRlQOl22giigfo-L_Smnrcng2eRMOv9GXP_Y-jPddpfglIryl4Gpv62A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17e27275fb.mp4?token=N_pIGIboOrC_qaa3m65wxse_L5nLORWdt6fi3dFttlLg42iP3fkmk_-UJCjw9QW06gvWoZUpKvAK7mmjrXBCGfPBQ_CMFqNLu41PvqCUWubI4IriLgf16avhnMvWk8j1JqjuRGXZGzXt4gWKrPmFZ4Wb3Lu0d1kdi8lXjWZHJHj8L7QGtc3B0-sctkLNEWLLIOdBXO-06Ub4gTxGinghLj_wevFh19fLTOP73a6NZCdo-tiTTqhjlqMg9pyxINVEtX4icx9hxy1VpWGF_p18HRm5fN-PlqsRlQOl22giigfo-L_Smnrcng2eRMOv9GXP_Y-jPddpfglIryl4Gpv62A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بااعلام رسانه‌های افریقایی؛ پیتسو موسیمانه در آستانه عقدقراردادی چهارساله با تیم ملی آفریقاست.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/27090" target="_blank">📅 12:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27089">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/370ff98a06.mp4?token=CwGjIp9Imw5JEBWb2nViqiJkAzYOz6AFOWMAcLIrbsQwKIze5UFGhtymwKipVDtCrHV3cxsRRz0Agj3077gFmzqzjfHLzQCfjwnb3Izxtzt_bSH2uOH2UHC5RAeTY9LAhkRyZ2gKPjsvyoEnRb3JgbbyiMjwauUhn4YVguezaCGut6Xx8mQHAJ_i8KHWl-ppwDuxw7YCUDdJl4AO9dois9dwRNZlShkhySSswjONR6i1CTIoc8eeHms5IZcb85dvaJZc24aZr5otfyjU4lH3ElARJi__OcKFvIK16GfA2RAdBVGb_j3nSzO9VxrVTuva-f4vVJ0OuMv1OPMW7DeI-rRJWBodoVbWAhBNMYpUNBwpeNauQujiHluPTVXd-lwA8urp8l5V8nMKiyHY8YopRpYv4lh_Q3DxAP7ZX2ITnoNF4scs8lhOgFXug0jwHX4F1CvU9F3o4CA9Yucr2Kn1MJjUlNwjn-uzBeyeHURjVQPwOcjjiLNN0XvS518dEukaMK11Fs4X6-hAs8Olt7SYOG_MMK6jKxGWGLTE7JG6DCHpuJmVYraYYIwACiLOR08KLoYgGekY1D5r1iTJWxfX5xndea2sYv7XTtcR9vhXw6a79wv8Q0X0tze1pjBZFgUQZ10dCInKiU6ljo4oSdIA47YDSxwypkgMnJ5Uxo2khQ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/370ff98a06.mp4?token=CwGjIp9Imw5JEBWb2nViqiJkAzYOz6AFOWMAcLIrbsQwKIze5UFGhtymwKipVDtCrHV3cxsRRz0Agj3077gFmzqzjfHLzQCfjwnb3Izxtzt_bSH2uOH2UHC5RAeTY9LAhkRyZ2gKPjsvyoEnRb3JgbbyiMjwauUhn4YVguezaCGut6Xx8mQHAJ_i8KHWl-ppwDuxw7YCUDdJl4AO9dois9dwRNZlShkhySSswjONR6i1CTIoc8eeHms5IZcb85dvaJZc24aZr5otfyjU4lH3ElARJi__OcKFvIK16GfA2RAdBVGb_j3nSzO9VxrVTuva-f4vVJ0OuMv1OPMW7DeI-rRJWBodoVbWAhBNMYpUNBwpeNauQujiHluPTVXd-lwA8urp8l5V8nMKiyHY8YopRpYv4lh_Q3DxAP7ZX2ITnoNF4scs8lhOgFXug0jwHX4F1CvU9F3o4CA9Yucr2Kn1MJjUlNwjn-uzBeyeHURjVQPwOcjjiLNN0XvS518dEukaMK11Fs4X6-hAs8Olt7SYOG_MMK6jKxGWGLTE7JG6DCHpuJmVYraYYIwACiLOR08KLoYgGekY1D5r1iTJWxfX5xndea2sYv7XTtcR9vhXw6a79wv8Q0X0tze1pjBZFgUQZ10dCInKiU6ljo4oSdIA47YDSxwypkgMnJ5Uxo2khQ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ رافائل لیائو ستاره‌پرتغالی سابق آث میلان در آستانه عقدقرارداد چهار با باشگاه منچستر یونایتد قرار داره و توافقات درحال نهایی شدنست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27089" target="_blank">📅 12:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27087">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kiBxM082qn3IK1IUwHf4QTqrkbAKRypPbNKRu8r8kr8jK4oWZnETJjJD8ng12sGzuN-irEW0SkS9kDDLypKgkf7NjP9B4nwFIzRzAZJRbIDZuGIUIZ3-zPU3QBkvI8wSLnWV-_zHvsdWGJGRiM0ou7KhcmROvecmVMQHlNQaCftqej8Faf9GvUUY9ioKfwdYpplEfgNTFDxELuAX_3G6mpe03S52vXM0zLesPawjHKGLlNrIQ0ghhYP9q5GsZclQF0voqGagN50K2s4D15dlW6_GPjLZvsy8n6gy1HHpK-xQX22ShzMfkKs7Lnj2OkrB6ixYGLOK9ocYtY_xxQnE8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اینکه‌گفته‌میشه؛ باشگاه ماخاچ‌قلعه رقم رضایت نامه محمدجواد حسین‌نژاد رو 4 میلیون دلار تعیین کرده کذب محضه. بار ها این باشگاه به مدیر برنامه این ستاره اعلام کرده هر تیم ایرانی دو میلیون دلار پرداخت کند و خودِ حسین نژاد هم راضی باشد این انتقال انجام خواهد…</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/27087" target="_blank">📅 12:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27086">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkryQFONA33iA3TnXxFD5Wy6dMzAV6xw57hzUQSLZYssF6hXcvXJzm3DpfA2MR5LS8OrlL1djW5l9gAk20iTwWPmymtnfCi9VLfTm5qavvS_ez1WbB5vT4fQzXONLJJqnz4yYlC6g3677OYayIq2LKliHN-FBllGq4niqBLSCxz6pCEqLpgDOHbw1IIIn28VkhgW_fY4LP78GG25-IKPLc27erl5KMwtRU0uYNZm2lwCyBUMnUnGy3pzhsBcE3TzxK2oWFIbaEopT_Rlohn0zopVsw0KBvp2PZWZ0WEsooNu16EQyX0F326IUpO8uWZyPwiTuQ9G0vp88wY-Zow4AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
رودری ستاره اسپانیایی 30 ساله باشگاه منچسترسیتی:من‌تمام‌پیشنهاداتم‌از تیم‌های بارسلونا، پاریسن‌ژرمن و منچسترسیتی ردکرده‌ام و تنها هدفم دراین‌تابستون پیوستن به باشگاه رئال‌مادرید است و مطمئن هستم که این انتقال‌بزودی انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/27086" target="_blank">📅 11:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27085">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gaMzwWn8FWH_yDRGVUknN5pli6rksEqvdv4I--haLXzFZ6YpscYSkKXdmsEIEgN6CuvoukKYqV1pNm-Ih0-oo-uN1fXCmGmJrXibjARoE8bM8v1fTzfbPnhFMxqAepvBjqBeQcbZnxbiYkDpCNIEz66KcwTTizF8kFzKjgOLE6eqlEF4tJo7m-Su4VgHAz5w5JvoA6BBhxAJ3WQcGDp-GbXH6LXurDViB8Jio-01yC2qGe6mRzJQlVHszyNSHyzzMNpaDg0sCohsUC6wB5j5tFMaRnooGjtxMmdAZsxI8AlNq-5HKDez74V8MvNWpd3F7ZvQAYHHCbvIFlBHZY5VWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیویی یک دقیقه‌ای از سوپرسیوهای تماشایی مارک آندره‌ ترشتگن در دوران حضورش در بارسلونا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/27085" target="_blank">📅 11:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27084">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejc9E8V8M6sd0JbgPMOlqF-AvFSyjqJXpAPWf14ZYjiIu45P0ZQsXGSXeI79kxkmPkJmzAcgvbicL38p-QaZdYZns0RubiF8p4N1kWQYfI94d2tkkSU0-Nm_l3knh22v4n5VSL9fT81aUSm9MMq7-qxQ41PBNxotQFAdjhSI2z7iOf6B-KtrP2CrJ1MS4YWAvPErf-WB0zj5BAGeMHF4_35fspRr4OlxB5LWRV--iM14HOad0s214wNdRByoBzCZcsGnyh96rEqWPaQ4aEPr2mxtH2x1gBMDo8s41funWqpZGwRPbAcZtcfX6DfOIzWWis4APpH1M9WJnuIJoJqiMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دو گزینه نهایی تیم‌پرسپولیس برای جانشینی میلاد محمدی؛ اولویت مهدی تاتار مدافع جوان گل گهری‌ها شد.
🔴
باشگاه پرسپولیس بعد از توافق شخصی با امیر جعفری مدافع چپ 25 ساله گل گهر سیرجان؛ امروز صبح با ارسال نامه‌ ای به این باشگاه خواستار…</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/27084" target="_blank">📅 10:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27083">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/222ef9e7d6.mp4?token=fYAzyQoB1H1XZJ_L4lHCzUNSLt3sJ4Bq6ROjIM9HKxC01Cv2bGX0FIWjyLE2Cc2rDTUKiITvboTIh5R_lQyH72Tqjt1JQS6_jiRjZEnliz8N-fraZJMgYrR04uxn48XTr_aBgN6pk1rMQtDUlQ5p28BeSx-66nRKq96P4RVhpYqKpa6mv7Y3VzMGsUcoFe6IdOpemWPf4Z93vOeU3A8zoQNKt8Zg_777g_VbXPllC0dElrAQHk0qV65QOrxQGxg_JYnhitGZnmo5XhoUOlgJ0kpcqWggO4E0c-dIwU7g9xR5zOaQ-3bJhMw3O8iaozo9rQ2ksJbOV5otaRI-4BfSHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/222ef9e7d6.mp4?token=fYAzyQoB1H1XZJ_L4lHCzUNSLt3sJ4Bq6ROjIM9HKxC01Cv2bGX0FIWjyLE2Cc2rDTUKiITvboTIh5R_lQyH72Tqjt1JQS6_jiRjZEnliz8N-fraZJMgYrR04uxn48XTr_aBgN6pk1rMQtDUlQ5p28BeSx-66nRKq96P4RVhpYqKpa6mv7Y3VzMGsUcoFe6IdOpemWPf4Z93vOeU3A8zoQNKt8Zg_777g_VbXPllC0dElrAQHk0qV65QOrxQGxg_JYnhitGZnmo5XhoUOlgJ0kpcqWggO4E0c-dIwU7g9xR5zOaQ-3bJhMw3O8iaozo9rQ2ksJbOV5otaRI-4BfSHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هونگ‌میونگ‌بو سرمربی‌کره‌جنوبی درجام جهانی ۲۰۲۶ مجبور شد دربرابرمجلس ملی کره حاضر شود! او توسط نمایندگان مجلس کره جنوبی درباره تک‌تک تصمیمات تاکتیکی‌ اش بازخواست شد. از تعویض‌‌ها و دعوت بازیکنان گرفته تا ترکیب اصلی تیم و سایر تصمیمات فنی اش، همه‌چیز زیر ذره‌بین پارلمان قرار گرفت. هونگ در ابتدای جلسه هم از تمام مردم کره عذرخواهی کرد و مسئولیت نتایج را برعهده گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/27083" target="_blank">📅 10:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27082">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmLG0n-_hHF0rvyUdUErdclx0lkK8qQ5pwXNMAKWkWfIxd81K6GHw6qyRHWTgCVeLnq2Zukgx0x1fqxTbAw0RnxP7PWtMw7QlWlI0n9-Bjk0lINW_OA0ckY3JBoWiq40nrxRaGgithhM8h6TKI6nhu3UEuGFQFoqzMpXvXhcH6LnRUrVmoMunYAJTTWp6a9pX6ofbRPlQt8IVFJnnrrKdFwE1ZY4uyn_oS8lXBgDzxIWFcQfC1dKvdCswI8qYNt1cqsV59DndpnAv7Y5FGh6S6BHwEVCfVV7J31OFhpfD84-2f9fNPrtHeghct75WSNemoQQ7O0GTpkZL7NvqkFlrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
نشریه‌مارکا: انتقال رودری و یان دیومانده به باشگاه رئال مادرید نهایی شده است. بعد از رونمایی از این دو بازیکن پرز پیگیر باستونی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/persiana_Soccer/27082" target="_blank">📅 10:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27080">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8QndTXtoaUqIbg2sSYl0NLgj9KRWRzt666B1S1T6jYpbz7D4h-kP5BmY8SpvHgmDDVmpD16aprp7-EeGS0q5D-j29F49RlNevVTeSsUIzXclhv276CQbuRwKoPuSuBlV_ztt1Ka_VKIzdx5NFKl0FscnOaCj3ewSwrKg4hbhhD0yA5Yn2tKuBFJsVcA6gkg96k2OBihpuYJU2Qlbfd2ZRiduur5ZP_CsXao3XQYhWoDOSNpNo9J6g4mgArlQAeV1_0vmMGBizuBpM2Ws7piDE1XBEZ4vapWX-5X4z6NJvaUVPGAy5YQ4RQmHB6rXp2GLwqcSs5FXVyplVmzRDc-UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جایگاه‌جهانی تیم‌های ایرانی در رتبه بندی قدرت اپتا؛ تراکتور تبریز درصدرتیم‌های ایرانی قرار گرفت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/27080" target="_blank">📅 10:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27079">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-npic3r0Fq57x_w2tQhodWvb6fBV1UFGUC3oGP7wZKEBdxaKv-3n2SO3j1DEOjprmbrAMui08jPBciQGFa9rs251nw14xpfYA9QX1isfHoAcu7gJASXbxLAMh8oXH0FYNy0R-Qk0HvDKMa-BGCVLLdEcC6Px1e9YtT2wNDDWDFnsw4aVzPiWd-4BlxvMGRqW2zUaRKaY1lzGDtfCmu9fBjSxsMn9tsi0dB5ZHD-9pkgI9Ix7WSl3iSB31EG2G7cH1avP8w22H1llXkoPEJrUQohKn5M_AScQ25mFthP-ZvicjRQmhaLPCy6MzToQeU7w1bknZRQlcp3BJmNl4DaVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
طبق اخبار دریافتی رسانه پرشیانا؛
سعید واسعی هافبک تهاجمی‌سابق تراکتور و مس برای عقد قراردادی دو ساله با سپاهان با مدیریت این باشگاه به توافق رسیده‌است و بزودی باحضور در دفتر مدیریت قراردادش رو امضا خواهدکرد و رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/persiana_Soccer/27079" target="_blank">📅 01:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27077">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNpCdKriI3H4QEEXp0PDt3oP05hlYhcWOQbvtKUN9RgZzooa0sRB-K5cs-K7bwA6ochy5nVM89-84i7zyYERTW4vaY_3gDFjdcBrg8UB8Q7aLxgoWwsWu-bdSY3wv7AKvoVOnIIjV8JMJeycJKCVhp0oU4AZB57CBT2Kvph9wpgKvKMkF2OvsCXkgo8MUzlthXI5v7I4CLOmSSno4e8Eo_YR8tX4y5axuvqVfDUQ5AvlD27-3VPjyc7_P41Z0dyIaTOsmpzWhPMOO3epb4uuuVtjLPPG_kcaZAQsQTID5ccpBIF0mZsH_BT3ILRRrOFrau1LLOyc9AWlMqm9SMmHTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌ امروز؛
مصاف تدارکاتی و راحت باواریایی‌ها با تیم میانه‌جدولی کی‌لیگ کره‌جنوبی
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/persiana_Soccer/27077" target="_blank">📅 00:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27076">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqpr3niWlq6KC_96tMNqYqht2jg1GVpcxwo8Oe85MyCBGkzpL8_wlfyQnjf4QN54UreCu18ih6fStbSabP7iUQVJvQ7ctDh6453TgKsZZiolJ1r5CIUIQSUT-0miNUwl3Ya1wv1_ruiirC23JpgiWmBB3o9qx1qRZPEYIi0Yo4YnL9lzDzZxVgqYL1OST9cBtSGFHxEuP24NI_28tUukxb1419xDHO7foUb9az4VK5QBq2732_NUhPl8auSH76x-9or_Ob7iAXpbhapZq-o2CIM7KaSvRVEFD8OcTWcAdhWj4NstMr-iisRcFDYoR1n_sUP6C6Y4AVxFoaR5qLokzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
روایتی‌جالب‌از آیمن حسین ستاره تیم ملی عراق و زننده دومین گل تاریخ عراق درجام جهانی: در سن 12 سالگی یتیم شد و پدرش رو از دست داد. بعدش داعشی‌ها داداش دو دزدیدن و هنوز هم پیدا نشده. بعد بخاطر جنگ آواره شد و یه‌مدت هم بخاطر اینکه مخارج خانوادشو قید فوتبال…</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/persiana_Soccer/27076" target="_blank">📅 00:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27075">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgufGUSwy7dXUXwlB35-g2BLMgLv1z-LfxjtTn0fXSgdHOlDoNjt5krGw_ph_dcVqUpZM5d5RL2gRpABjNnP7dHYDGXTGUyhG4myL6DOFrvRzHMjoGLNMNcgdotryO4yn31AxC8hTaZ_aXCn_n2jllhf3pXEnYOghdT-sib5oKAe1NvaXvGeyFR4q97ioviYzo_l9OYnqnuFp33M8uSKhU1_NFu9uRXv4gb6tINYLX-BQIprFY6X1rYkNhpzzuT_IMPxqJd-ehMDEsryL-APjWdGopHiM9XRjxlAzhKavKrha4CRbh7EfcAnle4WZnfJ3OCwby5NISQzkGng-92KoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
محمد قربانی میگه‌الگوی من از بچگی تا حالا کریم باقری بوده. حسین‌نژادمیگه‌من از بچگی طرفدار مجتبی جباری و فرهادمجیدی بودم. خودشون با زبان خودشون دارند میگن که دقیقا فن کدوم تیم بودیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/persiana_Soccer/27075" target="_blank">📅 00:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27074">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5Ut33qYJAgQIKH3Bb_LMJQQf-lgQN4GyYSEvW4XF9YqQ3tE8S0RVzcKWYfK4UgNbvahfODywvr2bSO6fqGGBnBCvNBuJ07Mzp6SnH_mCvWfpWoVnnSGeYHcO4Qmz94eye2F78IYzXDWempasQ_Jj2x8M_EUHL2xs4k3xCRTJgqrrUjQ20zo-6ZFF58lF7kQ4F3-qzYhuoIhZ5NQc5ugzfsD5HIE9dcVn09wjmM614OUHFY9lDocWXvmq1-2w7jvwe4No0FEvXaUpmoFlNRy3_XeX_PAZGWIlfrj467cfpuX4PfZ-fyZ3q-2sXDQZBw2kFaSks_5J6RQr8UCwauGfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ آلوارو آربلوا سرمربی‌جوان فصل گذشته رئال مادرید با عقدقراردادی سه ساله بعنوان سرمربی جدید فولام انتخاب شد و در فصل جدید لیگ جزیره شاهد تقابل جذب او و ژابی الونسو خواهیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/persiana_Soccer/27074" target="_blank">📅 23:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27073">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cr83XI3itOHw7U-fZ8gu_ndM3bo2M_MQlHoR5ncZOkE3pbD8P6ijZel3iikulnEqRhC750Pnjp8gdIETim9QtQCO5olesd5w9P15Ayn2qJ9WfzQxFEcIxr94375ixPr_igZNUoRD7tk9q3B2JM0HOVfn2JmZki0NW1QGSpf0HMzbdd3itg8SeZowFdtiTbyH2w3LbjrSrGiokMO04cDRWBxQCvfAHnz1PDp8PvtEUs26gN779yirmucvIvSUPhNJ9Suyb8o28hluUhO8rrE1q4QHW9QchsaPn9Pp-D6Q-ukgrLf5tQwVB9UyEyCeDRhu8gEmy4k6g32yAjDiuflk_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
دادگاه‌عالی‌ورزش "CAS" روز سه‌شنبه پیش رورای نهایی‌خود را درخصوص‌پنجره نقل و انتقالاتی باشگاه استقلال خواهد داد. اگر رای مثبت باشد فیفا پنجره رو بازمیکنه. اگرهم رای منفی باشد این پنجره نیزبسته خواهد ماند و با شروع نقل و انتقالات نیم فصل پنجره آبی‌ها توسط…</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/persiana_Soccer/27073" target="_blank">📅 23:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27072">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkXTtvHU24_YfyBV3eycfekeyKO8WczbOigKuYimIqIlYqd4z6lXuwk2Cm8T79XYmPjisl62Z7VzmdmXR_ptR2JNmFF1dozb185Yy8gXrtLwn46XppZs7MmqglWJzwlhpjOVstiqfXhYIoWWDRUhGBBqvYVCvpttM88bU0zFHdj0LhHJl1fI6ui7ainPvpVyQQYZn-md3X3ToZKWbHsSW9s7HzO2OZPiCtL00c-RAaVIFgCW0B4FzMaAvfdPli1n6WwVi2BQ5Q7RlemJLhNZx4RMuGW4ohFjEdFxSLHOTlQB9_5qQE4zY7g7WvTGPYNueEZ5nrQzca3AW7j7oOgjeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
اسکای‌اسپورت:الساندرو باستونی مدافع 27 ساله تیم ملی ایتالیا درخواست جدایی از اینترمیلان داده و به مدیریت افعی‌ها اعلام کرده با جدایی او و پیوستنش به رئال مادرید دراین‌پنجره موافقت کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/persiana_Soccer/27072" target="_blank">📅 23:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27071">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQY-v0hmT5mPDNufqMTs_0dD5ynhESgI1p44hDdSP1UGAylVdu2Joc-nIcNB1olChCVtohoGnAYm_PKWvBiJq5gJEt14VXF5dWEc67uSup2rMgDjJlRCuTZ5OEwHK_dtJtTa0dYL93ZJ_2vhVpXPdAMEId1WRIJhWpVyWFDmHmQlzkTSgQzDRXCaQkqMgFAjaNLqzSWCEVBgA-ZTSZf6zBmnioC1WXp5A96oeZDk-K-NquXEO9LNYl-C_If4CmBZwYzX_Lu6iXcowwX13bxWXJoyx2qn_nshA3YPCIZEf_Ma2OnPIVBrnbIS5XUd4ofwgfkvHbo7R-KoFdiOmQWygQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛مدیر ورزشی ماخاچ‌قلعه به‌مدیربرنامه‌های محمد جواد حسین نژاد اعلام کرده که تصمیم این باشگاه برای فروش حسین نژاد قطعیه. هر باشگاهی دومیلیون‌یورو بدهد و خودِ حسین نژاد هم راضی باشه این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/persiana_Soccer/27071" target="_blank">📅 22:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27070">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b42hG6QwpexE7lO4B81B_WUXeSmUr4WH9uuUjZ_NP-Ot2Pm-8SU9URjNFjjTp-r6YDbpeeoMthO0LAIfk_Y_TtoSnCPvnGdPdOeOMWpqJxa9cMu1RYnRjRp7_22TuVhP8fBklFGWb_LBB-61LMuKKiE1ro7sTwZmDrB0ghzAk525KzriOfK34xeKPWAnQaKueoP8pMnU1u3gxdMwlvMMvKP6DKb-9_X-2wUsPwyQuHGyDFUrTUmDYczGihSdSl-wi4cXjTWgZbNX8faqBBgiX-dUy_jchXTNpoQHmZznHYKbcMhvJdJ4xo87Y8rnhgJpvI6cyLxIQxNyPDcr9tKHSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری؛ دونالد ترامپ: این آخرین فرصت ایران برای امضای یک توافقنامه خوب است. امروز یا فردا می‌فهمید که چی میگذره. قراره به زودی و به یشکل دیگه، مذاکرات پیش بره. کار خییییلی پیچیده‌ای هم نیست. قراره فرداتنگه هرمز رو کامل باز کنیم. بعدش هم در مورد ظرفیت هسته‌ای…</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/27070" target="_blank">📅 22:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27069">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vbx4M5JVR2qip37oFbvjOnKYiS3niF2b4cxXGqPfvBQwRYV0w9Dnv6cPS-jOGqh2ZHPWT6XfTq8JavmUhbaZee7dXE0DyUmaFOlQxZNDinvX5nwi5ZPYVk1tq5mMGgSb8ZfoJr33Q51GyddqEMtch-yPq-QLTxD0vRl0jB_sfDz46034fFr8C3bPyCHgsWzpmhQkO9rXdqPJb6bDOGh1ktoWeg5Cuab_vtiEoNvFSCeE6kestNOnQgge_H2Ogr-KY_oHJqQRlHiTBzcqdK6TV4HnFSaYqUANnqDM8sv8eB4CesX7wkwCP3UNeLVtGtKlwkCosKLCaO3qIWEg6USpFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
نام مهدی طارمی کاپیتان تیم ملی از لیست اروپایی المپیاکوس یونان خارج شد تا این بازیکن در آستانه جدایی از این تیم یونانی قرار گرفته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/27069" target="_blank">📅 21:38 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27068">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e97c6b80b0.mp4?token=KwFVPmA6jTEljB0aKeonLQXDRTyRrD7H1FwQyiRWX7eRIHYlkaaVfu5jDu28GVngkP01LTX31Y9mWtEyHT0z382wkiNNqZhPKs88zY9favXnoDw_H9IZwMNx-aFsPTRYebUQd9T-i8iFN5-k32td1gyyQ4Igari-IujM0bjJwnMnCSoqXeg6df7Zs-yXTHyiMBeaJXVmNip_hdm7Aqe4tkREw21Gg2AJLX34x0mfYU0ZWqPuOpsMYyDdSMM3DfVilMC6zIF4QQ5h3qpVfsZ8Fg0t-c6rqif6Y86784KHj6q4XmNQld2mn8YX59TrgW1oZJ9cgMCffceAKDOP4tJ6Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e97c6b80b0.mp4?token=KwFVPmA6jTEljB0aKeonLQXDRTyRrD7H1FwQyiRWX7eRIHYlkaaVfu5jDu28GVngkP01LTX31Y9mWtEyHT0z382wkiNNqZhPKs88zY9favXnoDw_H9IZwMNx-aFsPTRYebUQd9T-i8iFN5-k32td1gyyQ4Igari-IujM0bjJwnMnCSoqXeg6df7Zs-yXTHyiMBeaJXVmNip_hdm7Aqe4tkREw21Gg2AJLX34x0mfYU0ZWqPuOpsMYyDdSMM3DfVilMC6zIF4QQ5h3qpVfsZ8Fg0t-c6rqif6Y86784KHj6q4XmNQld2mn8YX59TrgW1oZJ9cgMCffceAKDOP4tJ6Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
فصل آینده تو بارسلونا میمونی؟ فران تورِس:
‏من‌قراردادی با بارسلونا دارم، اما در فوتبال نمیتوان پیش‌بینی‌کرد چه‌اتفاقی دقیقا خواهد افتاد. من هم فقط منتظر هستم تا تصمیم درستی بگیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/27068" target="_blank">📅 21:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27067">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d787366ec9.mp4?token=hGUvhVn8IY0Z2pvNjpNZ5oZxTyxbQTW7IgllXb_R8d1MKDGIG0AKekjDLjhXsT5PccoQm03Wj47vjk5awxjC2bqhRu7Z89ec5Jvz34CFuMeXfwwbXFHcnzJsxh3OrxFGIS5figHeq7uwo5UmypL-SmB-JOc6AxVUoBOeVfXAjKKXQFhd4JdaBCyYVzpckw19YIKg4hiK8BBe59hcdZGOwe2Uhnt8jsbhCR9KxLh8vyTArJx70FMGlQtRxLbJiGUzylznAgC0p43N_7eKaKz_HDH17T8dy2zsAlTSqV5bXGE8x5bDcFIymh5MNCLFNGT2AjEYDnAsdm5sPpOWALpioQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d787366ec9.mp4?token=hGUvhVn8IY0Z2pvNjpNZ5oZxTyxbQTW7IgllXb_R8d1MKDGIG0AKekjDLjhXsT5PccoQm03Wj47vjk5awxjC2bqhRu7Z89ec5Jvz34CFuMeXfwwbXFHcnzJsxh3OrxFGIS5figHeq7uwo5UmypL-SmB-JOc6AxVUoBOeVfXAjKKXQFhd4JdaBCyYVzpckw19YIKg4hiK8BBe59hcdZGOwe2Uhnt8jsbhCR9KxLh8vyTArJx70FMGlQtRxLbJiGUzylznAgC0p43N_7eKaKz_HDH17T8dy2zsAlTSqV5bXGE8x5bDcFIymh5MNCLFNGT2AjEYDnAsdm5sPpOWALpioQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
دلیل ازدواج کریستیانو مشخص‌شد! حتی قیچی‌ برگردون تماشایی به یووه هم‌به‌پای جورجینا نرسید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/27067" target="_blank">📅 20:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27066">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFKwILLlgi0RGC84WbHka1P5A4hM06azkJXl9L00F8lKqDYPkhTzw-djWg5LoR8B7OTfhaKBRG4wgiq0vrtnfN-13M5Z6TM-7fCbFNavshRbjU1nTgHX3aJV1ru8aSsfZi9Ga8k-nddmZVcOBw2qaD6FmTQajKIbiWs79vo6ltu4GeQREtGActFic7FNq2S0tPTZ3Rd1h6JVNVK_qgqbovuq-r7NbpczU4pVaKuz2TrriaiMLvqFlTUnAJwKW8T2GeaLzI7F0R8Dl_pjQtnoN1Pxrp1TKWVe_AyajcAHcw8BkJMeAIgOjO7tgmW8JuLK30xkCNrMGxLWsYOmB6mwFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟡
طبق شنیده‌ های رسانه پرشیانا؛
یاسین جرجانی مدافع‌میانی22ساله‌سابق آلومینیوم اراک که فصل‌درخشانی دراین‌تیم داشت با نساجی مازندران و سپاهان اصفهان مذاکراتی داشته و بزودی راهی یکی از این دو تیم خواهد شد. شانس نساجی بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/27066" target="_blank">📅 20:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27065">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vigo0_0R9tSSJoN7kZayl6d5rlUKRWbBYAisJ0pVNLuDfh3zCQgjLgPydzNBunRTVZYz0NS98rFsml2W6ME9Ybyzx0pLhiucx9_ef5-DJlJL77aiNmTKddHwt5UUQk2ZI-lgdaGh4pTv_wb3ggo2EAuLcA0jh8XPXLYP8x4kCaejw_Rv7nL9vyvopH4e0uSXUdWB27M7rX7zgKd4lRBoRDt-4I7K8_-ln6plkisaOA8Set0JTetvTxlvw0B8_IP62xKvWK6--xifIb6wiq-mAnc6Ho4Ez3IX-3qnJkfqo5WyoYp94-WbZEho33cr96df6eN412b1RPPiJeT9qNw2-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
👤
عبدالله‌ویسی سرمربی‌ذوب‌آهن:
دوست دارم کاری که‌سال 95 بااستقلال خوزستان کردم رو با ذوب‌آهن تکرارکنم. بسیارسخته‌امانشدنی نیست. امید عالیشاه مذاکراتی‌بامدیریت‌باشگاه‌داشت اما درجریان مذاکرات نیستم. امیدوارم که قرار داد منعقد بشه و این بازیکن با تجربه رو در اختیار داشته باشیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/27065" target="_blank">📅 20:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27064">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8XAvpjqaPixoWv3oSc_D1yv866oGc6oDx9kYJTuxfvrnzrdU6CzuCeeE0h0i1kw9fOSmdoEgmKKuIuGkwmmjeedydF7PgqNZTuvAKJmtpbrbNJE-YD7IwQFss9Xobvn4eDPjH65vq4SK55BawebuJaIeVRvlHPiGW6xTGpHR19VHRfA7NaDwGBOMKDlVgfcmUYMRZGYkr9VEOwm5Ld_S08QAH9i46trxT6cfPeRlYbnYocLY667q5L3AZ1W6NcVeCU_gn7R57H6EI_NunMJweRLkpHBQhb0jNo5-hnuwDI1WTiZ8fbwQ57_rVGgym45mroHjvCIQDeQF1CQGMVVxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
تایید خبر اختصاصی‌پرشیانا بعنوان اولین رسانه؛ اولیه هدیه ارزشمند سعادتی به زنوزی؛ هادی حبیبی نژاد ستاره فصل گذشته چادرملو با عقد قرار دادی 2 ساله‌رسما به باشگاه تراکتور تبریز پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/27064" target="_blank">📅 20:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27063">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thnf1rwhKpHYeZFbdVZDGbqjaBMvX-omH29MscgvhkNn2zekknt7B0EEVrMTorenaImaOpxxdKiqg1SlGqh9Shb4MmPPOnGN0Yiu5TADl6GDHVepBgCslXOA7JU_EtREhg5STzUc876Ex7ha2j043XxDNIqhxfBfxfhp3OROlw_5Dfu7mVRxdM8OXCbXcLugnqLuVb8CVxTMYfBumOh3biVFyDJd33imMACW2P6HFId5PvusSSyq9Z-jHcKnAJ4oxa8rF_olyTGImHguBTidxWGDC7xrw6gFXnmggRVakx1xMMnIvzi56tyUJeJLlqHkooU7a1lHsXqiNZTUz7mlTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
روبرتو مانچینی سرمربی تیم ملی ایتالیا:
🔵
ماجرای‌من و تیم‌ملی‌فوتبال ایتالیا مثل داستان یه‌رابطه عاشقانه است که به خاطر اشتباهات تموم میشه. متاسفم به خاطر اتفاقاتی که در این سه سال رخ داد و تمام تلاشم رو خواهم کرد واسه بازگشت تیم ملی ایتالیا به جایگاهی که شایسته…</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/27063" target="_blank">📅 19:52 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
