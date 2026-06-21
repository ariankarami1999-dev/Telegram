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
<img src="https://cdn4.telesco.pe/file/WdwJDQpNa2na9MkaJY_OqkXkM_ayQOd24J0OjA5xB55kpr-MhT0aKK3VqlHcOCY-UIf2ow5-OD_5a7iCeQZrEsdUvl6veTTf1IC9lRwAfG_ln1UlU_SipQmT745QV0aJSxpj6gDNBtnNXiSPG8Lx4qTiJR8HujMyT_A1bQ4fNvcM_WITAkttvS1fP30jAWu9ZxE2xjTU5r46kh0Orub7xeaj-kO2DjRrZCZc5MHgPpMS5queKJrq1x3W6Y2h87wwlZtnCq_YR9PpoEOYXGLmWeMD25EK6iDc-2RzHa79QPR60jm_75fUzRKCSDq9KlruMLiU8EZgOsZzZc_swY-_3A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 18:51:00</div>
<hr>

<div class="tg-post" id="msg-443744">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-uiGoU7Z9H9jwt7P3f2ZZVDJhkoj_HbCahN9gQGm_LDI_YjuA7ViJAAqtTfHDBCs3ptc0JJXIfYiJqyu_2ztpsT3c96V0awCLhk8dOIaywqzqVmt4jcUxgqg3mFPGGW1aLGK1ww0DqX5bLyKmjQaOOmKeM5-cRYv-veDd12QTw3gsVqC7ZXaDteWxc29D1Rjvb6lgZBpLISdO0eGr-O2RuCg2BV7U2JvmaOhA9DEYqeBjxWoKQFai6skNBd1r3bN2_1KmhxgR0MOwAs7DJbAA58zdHGFRyjwx8i_fv-xYhsFu3g3CdOZLbRNJva2Fw_4FcUkaUCFg0GHUpSDcMNgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مخبر: ایران از ظرفیت‌های به‌دست‌آمده در تنگه هرمز عقب‌نشینی نمی‌کند
🔹
محمد مخبر، مشاور و دستیار مقام معظم رهبری، در گفت‌وگو با خبرنگار سیاسی فارس: جمهوری اسلامی ایران دستاوردهای حاصل از تحولات اخیر در تنگه هرمز را حفظ خواهد کرد و از ظرفیت‌های راهبردی این آبراه عقب‌نشینی نخواهد کرد.
🔹
سال‌ها از ظرفیت بزرگ تنگه‌ هرمز غفلت شده بود، در حالی که این منطقه امکان تأثیرگذاری قابل‌توجهی بر اقتصاد جهانی در اختیار ایران قرار داده است.
🔹
ایران در چارچوب سازوکارهای حقوقی و بین‌المللی به دنبال اصلاح برخی قواعد حاکم بر تنگه خواهد بود، اما در هر صورت از همه ظرفیت‌های قانونی خود برای صیانت از منافع ملی استفاده می‌کند.
🔹
هر کشوری که در مسیر اقدامات ضدایرانی حرکت کند یا منافع ملت ایران را نادیده بگیرد، با هزینه‌های سیاسی، اقتصادی و امنیتی اقدامات خود مواجه خواهد شد.
@Farspolitics
-
link</div>
<div class="tg-footer">👁️ 354 · <a href="https://t.me/farsna/443744" target="_blank">📅 18:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443743">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aa75e8800.mp4?token=qGgqFb2oVhQxDNb234ibRgubv9v5Jt_WgILNwFW2QeHoIDJkVWsSV4f5wNa8vAZB0T4oIvYqSmJoq1pNwOEirAO5hm7PHOR_OoU4c7ik5lcXHG75tnGFGVVjpcLq3_GrxY5KK5MfWQzWfkaLJ-kT4LMITvH32hBqIYKSflhI-RtgYtP0-uFuUDD8KuCH-7L3h42AomUHP5Mu6cMGbhh-pIvVfahwK6mTsjoFFnNI9XP0V78IesyfK0vOsueQg4FTJ3PGhxjOPas0s4hFcV7SU8eJnMcr_MLuCJz-pjTx5d9vAtDL-gJnlQZAmilBwqrhmuFIetyMEKN0MJy5gKYD3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aa75e8800.mp4?token=qGgqFb2oVhQxDNb234ibRgubv9v5Jt_WgILNwFW2QeHoIDJkVWsSV4f5wNa8vAZB0T4oIvYqSmJoq1pNwOEirAO5hm7PHOR_OoU4c7ik5lcXHG75tnGFGVVjpcLq3_GrxY5KK5MfWQzWfkaLJ-kT4LMITvH32hBqIYKSflhI-RtgYtP0-uFuUDD8KuCH-7L3h42AomUHP5Mu6cMGbhh-pIvVfahwK6mTsjoFFnNI9XP0V78IesyfK0vOsueQg4FTJ3PGhxjOPas0s4hFcV7SU8eJnMcr_MLuCJz-pjTx5d9vAtDL-gJnlQZAmilBwqrhmuFIetyMEKN0MJy5gKYD3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایران به مصاف شیاطین می‌رود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/farsna/443743" target="_blank">📅 18:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443742">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‌ یک منبع آگاه در تیم مذاکره‌کننده اعزامی ایران به سوئیس: هم‌اکنون دور اول مذاکره ۴ جانبه به اتمام رسید. @Farsna</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/farsna/443742" target="_blank">📅 18:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443741">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2c8569887.mp4?token=GlqXaBaOEQjV2q8PQj-zBj9yBzzZYsP26Wt3bcrBJBHD99Gs8Q5YbR40TWk-ak1Kl1bCehuksnH1q21NJSCy1I_2rtBy4W9JV6M33Z0C2mmiDjovJT3LHDdpZgtW4rntvQ_gg3Xo-syxposrklw1Ly__OI3aG-eUeJllc1yJs3RZq3Pj31ilG8dzv75Sp-07fcPxWFr9Mav8tHhh7znwB4bW2YWQ1Vmk0H_cSbRWGVHgMcXLu7Ylvh58_Sn04E-2P861N7YYNSOfw1r1LKmYk-gH7lYImyLzxonQWK9ohAnrmcc-lUzETdxDVp2zaiOBmKheqbZZdosO8Nhb0Fuia4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c8569887.mp4?token=GlqXaBaOEQjV2q8PQj-zBj9yBzzZYsP26Wt3bcrBJBHD99Gs8Q5YbR40TWk-ak1Kl1bCehuksnH1q21NJSCy1I_2rtBy4W9JV6M33Z0C2mmiDjovJT3LHDdpZgtW4rntvQ_gg3Xo-syxposrklw1Ly__OI3aG-eUeJllc1yJs3RZq3Pj31ilG8dzv75Sp-07fcPxWFr9Mav8tHhh7znwB4bW2YWQ1Vmk0H_cSbRWGVHgMcXLu7Ylvh58_Sn04E-2P861N7YYNSOfw1r1LKmYk-gH7lYImyLzxonQWK9ohAnrmcc-lUzETdxDVp2zaiOBmKheqbZZdosO8Nhb0Fuia4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پروژۀ ضدشادی مردم از کجا شروع شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/farsna/443741" target="_blank">📅 18:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443739">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🎥
آغاز نشست چهارجانبۀ ایران، آمریکا، قطر و پاکستان در سوئیس
🔹
نشست چهارجانبه هیئت‌های ایران، آمریکا، قطر و پاکستان با عنوان نشست دریاچه لوسرن در بورگن‌اشتوک سوئیس آغاز شد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/farsna/443739" target="_blank">📅 18:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443737">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/443737" target="_blank">📅 18:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443736">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spvXubatBz8gPWOd-7zNYpHfFwsw9oYdqN15_hSknBGCMfI3iNePkbNZ_5XTaA3yCVMgrwPaFzud__9GpYnFU-6p-Yo2FIzGV5f9vaRsQs_ya8Tb1FAfJpK1vUvARS3h7b01lqVSfBMyG-B1xwosn-3akEgkLFaFAI8enh-2dPltZp7D2b-FJEsl8PJOY_jagTuYugFFukCPfhnmWA074-nJHI_1NrOF5i9HKm3nDR4SWpx7lwKl76h5M7gP6A-jTlNMbAPZVkkWDO0GTmV5dYAOMWtL0t2PGgBDoYPnlw7fzHl3fsyVxgrw6Z2NNdE9XDTdTepb1GqbspfP2IAw9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش از حادثه‌ای جدید در ۵۰ مایل دریایی سواحل یمن
🔹
سازمان تجارت دریایی انگلیس: امروز یک قایق حامل افراد مسلح به یک کشتی تجاری در فاصله حدود ۵۰ مایل دریایی جنوب‌شرق در ساحل شرقی یمن نزدیک شده و تلاش کرده است سوار آن شود.
🔸
این حادثه در حالی رخ می‌دهد که تنها در دو هفته اخیر، دست‌کم چهار حمله مسلحانه دیگر به کشتی‌های تجاری در آب‌های یمن گزارش شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/443736" target="_blank">📅 18:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443735">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۷۳.pdf</div>
  <div class="tg-doc-extra">2.4 MB</div>
</div>
<a href="https://t.me/farsna/443735" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۷۲.pdf</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/farsna/443735" target="_blank">📅 17:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443734">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMetayb7U9yVijF54-sz3zF-A76Ix1P2Mua_vKJfXCWcFuGQAqfERqxQDafVTPKCG09ZF7vFM0gzI2i-YYeE3kW6egXrnBKel5HPBP6eoocpziAHioz5VXFrWYmd4kLfNz7oudp0QhOVh6ytNvrlXSUHtmELNHq3LZ3AtJyUkWI0rvCmAvkev3OeKkCUZaAcZuboNOWs2_Rd5LwzIDf941HycuL6fDZXrMBwtdxw4TOpgMAOq1fpcXvIwRXjhhIFkWPlLuWmRA4JY_lXjlQB29b_bcOOzngG3_cXzswOsJzC143XwDCSFc9DhNQuIOiHkJK1kc859hdjHCXkSJdRyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خشم قلعه‌نویی در جام جهانی پیچید
🔹
شرایط نابرابری که آمریکا میزبان جام جهانی برای ایران بوجود آورده باعث اعتراض مجدد امیر قلعه‌نویی در نشست خبری امروز قبل از بازی بلژیک شد که نشریه تلگراف انگلیس در گزارشی به اعتراض سرمربی ایران به سکوت ۴۷ مربی دیگر جام جهانی پرداخت.
🔹
نشریه تلگراف می‌نویسد که سرمربی ایران به شدت از سکوت ۴۷ مربی دیگر جام جهانی از ناعدالتی میزبان نسبت به ایران گلایه کرد و با عصبانیت رفتارهای میزبان را غیرانسانی توصیف کرد.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/farsna/443734" target="_blank">📅 17:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443733">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مرگ ۳ اسرائیلی در سانحۀ هوایی در آمریکا
🔹
یدیعوت آحارانوت: ۳ اسرائیلی در سقوط یک هواپیمای سبک تک‌موتوره در نزدیکی شهر بوئی در ایالت مریلند در آمریکا کشته شدند.
@Farsna</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/farsna/443733" target="_blank">📅 17:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443732">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CeNSj0xzEb9gktPM0K3exWIav23mQrL9oLE8O5Cn_T2eBdiIYGMWBji7lC_55fxtwFv8UBX-odhh6ZgqPtrJUy7AxNhOLFQAhL8n_3ZQaJmBycQqtprAm-coaW8yFvGFWlM1gxAnjXUON4wMa9DdDi-nhZI-45uYAkDW42Wb9f4nfCkhsj5-YI_S_M2iA7cahLCWxbnlecPNN0vlW1h9hel86GsUpzaZidgwvGlfjVAZ90_QsEvkUFYNvT69ezXC5S5Bt5XEZfCN6qClOFKQ8sjP-1MIDJArb6SXDxYyPxn4KTQLtDQllZFhd5CNgDwLy0jA4Oanod98RpfmFqDAfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷ شهید دیگر در لبنان با وجود آتش‌بس ادعایی
🔹
رسانه‌ها روز یکشنبه خبر می‌دهند که در حملات رژیم صهیونیستی به لبنان دست‌کم ۷ نفر از جمله یک کودک به شهادت رسیده‌اند.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/farsna/443732" target="_blank">📅 17:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443731">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QumEAOIdT_0R5rLCgc_ZvT9FuJsNpdkdnV-eYWENc50eTaNI8Zd7YnPIRbJUnxBe_DvmNuVK2IAU4BYzE0rOdkcXCgIiGgVibxsvVw6bX2GFOm8gOveCWzvJI7psaZ4WlFo2A8BBNfr9NOL9UjE9-AMUKkrtnAuVHekWE6fy4FAYFtrapaNqIkFh1audhxx3YoY8vy7b7RFGwur4W2II8Vmvph-ZKmndpUeuzKzmuNmn1EcDA-mnCoSFPGDMMxtd68hdGlLtSIWIjGcj9c6dykI_w2luvGy4mpmq09uLq-CFMI0FWiQsSIoV8uNSQUHEzwhVUzmi3JZOT3r6pvUxqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش‌سوزی گسترده در لس‌آنجلس
🔹
چند ساعت مانده به دیدار ایران و بلژیک در لس‌آنجلس این شهر با وضعیت اضطراری ناشی از آتش‌سوزی گسترده در یک انبار بزرگ مواد غذایی منجمد روبه‌رو شده است.
🔹
شهردار لس‌آنجلس، با اعلام وضعیت اضطراری گفته اطمینان حاصل می‌کنیم که شهر به همه منابع مورد نیاز برای مهار آتش‌سوزی دسترسی خواهد داشت.
🔸
محل حادثه حدود ۲۵ تا ۳۰ کیلومتر با ورزشگاه سوفای، محل برگزاری دیدار ایران و بلژیک، فاصله دارد و تاکنون گزارشی درباره تأثیر این آتش‌سوزی بر مسابقات جام جهانی منتشر نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/farsna/443731" target="_blank">📅 17:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443730">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ارجاع پروندۀ یکی از معاونان رئیس‌جمهور به دادسرای دیوان محاسبات
🔹
دیوان محاسبات کشور اعلام کرد درپی طرح موضوع واردات بنزین و اعلام آمارهای غیرمستند، پرونده یکی از معاونان رئیس‌جمهور به دادسرای دیوان محاسبات ارجاع شده است.
🔹
این نهاد همچنین با اشاره به مغایرت رقم اعلامی «۶ میلیارد دلار» واردات بنزین در سال ۱۴۰۴ با داده‌های رسمی، خواستار ارائه مستندات مربوط به این ادعا شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/farsna/443730" target="_blank">📅 17:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443728">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">🎥
آیت‌الله نظری‌شاهرودی، رئیس مؤسسۀ دایرة‌المعارف فقه اسلامی: تنگۀ هرمز ابزار قدرت ایران در شرایط جدید است
.
@Farspolitics</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/443728" target="_blank">📅 17:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443727">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42306a07df.mp4?token=ZfAWVBf7lyB-2dbS3jAV_OyjTL6KzYGPCLMBkbL9mNDizB22iRjSBZ8SfroXuCGstsdUW_4CWUYU4zuNK285MKJ_-Y8tfizfG_Oac_7kK-cACc6od3sPS6StrL7uxnQJkZbuRGMOFxvC9wZtWYv2IcPu5736iV9Kmqz3TcTXqv8FlHVKXQfNVnl9LGpsasU9iyIzn1jk6jMsR-MXp9kH57Z3Wg5T_2cn_jP-C8DXORlwm5cKlQ1E6_leqGWRPO-7lhkc3M1sN-e-3KQ9zWh1yqXRYJl9fBx3nWBkOPKZ5cSPtzcZwxeseB-33vSQ19lTvqv1Qnj9GPNdvnUiulgVq1MCKB3KXFUjVziXipCdWIFUuhSk-MAFVLUq7n3TZxEx9ojIBP1yLvWbaX0gdzoPS5xodC8b5bRYyJzVo-Cv-SeSP0vzLH8Zd-sNOIM-hpUDoo6SorWKoMBND1ugEfY6w4nIicsIAToo5PhWWw_uCSjKynkEBXyN4iEXcuQtiIB4P9DF-6eFrAwQRxMQgE-QSD9lWlsusWk8AMmJdKtvy9ut_rmfnnwileDfYd1a98MYaFzlt4Nol1cwpMFzlX0zNfpYCwWlo320H7NeCF4MrkdMVVm-3LKBS5PtfFKBl4tnRKFpTuaKbUfZ2PURJigMZtr-6uS1jF8AHA-ac3Upkk8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42306a07df.mp4?token=ZfAWVBf7lyB-2dbS3jAV_OyjTL6KzYGPCLMBkbL9mNDizB22iRjSBZ8SfroXuCGstsdUW_4CWUYU4zuNK285MKJ_-Y8tfizfG_Oac_7kK-cACc6od3sPS6StrL7uxnQJkZbuRGMOFxvC9wZtWYv2IcPu5736iV9Kmqz3TcTXqv8FlHVKXQfNVnl9LGpsasU9iyIzn1jk6jMsR-MXp9kH57Z3Wg5T_2cn_jP-C8DXORlwm5cKlQ1E6_leqGWRPO-7lhkc3M1sN-e-3KQ9zWh1yqXRYJl9fBx3nWBkOPKZ5cSPtzcZwxeseB-33vSQ19lTvqv1Qnj9GPNdvnUiulgVq1MCKB3KXFUjVziXipCdWIFUuhSk-MAFVLUq7n3TZxEx9ojIBP1yLvWbaX0gdzoPS5xodC8b5bRYyJzVo-Cv-SeSP0vzLH8Zd-sNOIM-hpUDoo6SorWKoMBND1ugEfY6w4nIicsIAToo5PhWWw_uCSjKynkEBXyN4iEXcuQtiIB4P9DF-6eFrAwQRxMQgE-QSD9lWlsusWk8AMmJdKtvy9ut_rmfnnwileDfYd1a98MYaFzlt4Nol1cwpMFzlX0zNfpYCwWlo320H7NeCF4MrkdMVVm-3LKBS5PtfFKBl4tnRKFpTuaKbUfZ2PURJigMZtr-6uS1jF8AHA-ac3Upkk8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایران به تولیدکنندۀ فناوری‌های راهبردی سلامت تبدیل شد
🔹
دبیر ستاد زیست‌فناوری معاونت علمی ریاست‌جمهوری: تولید محصولات پلاسمایی، شیرخشک نوزاد، تجهیزات پیشرفتۀ پزشکی و مواد اولیۀ راهبردی، از مهم‌ترین دستاوردهایی است که طی سال‌های گذشته با تکیه بر توان دانشمندان ایرانی محقق شده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/443727" target="_blank">📅 17:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443726">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iILQuzou6cZPKsLhI0QgPEILXKSxEkL-Z3nA2MEcrWJZe_nISjhEvYjXymwTOnJly9R4O0wVe1hYKOufeMVXis0be7B4FD7-DuRe-ocj0945terdeZi3-ifr_ywb7gHY0QvzMHg_EpmhggvQC5li0zVXecTs42Yw65NOCz4l2Q_vEmDOp_KnCHElIdtS0UUvcQ3WUQ_Tv2fvg7iFWNeaBw6aH1PfeRffjpQs3ypU4CZvrg-EFznbC0fRnVi3UAf7o-Fq3lC9JpQnTn48RoYv8H-SGelGz7dcv4o5xz7Eg_skybU3XdtW11BnytNltGSZRJzGiAxBFXCC0sg4tKL2EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ایران باید فوراً جلوی گروه‌های نیابتی خود را در لبنان که درحال ایجاد دردسر هستند، بگیرد
🔹
اگر این کار را نکنند، دوباره ضربهٔ بسیار سختی به ایران خواهیم زد، دقیقاً مثل همان کاری که هفته گذشته کردیم، فقط این‌بار بسیار سخت‌تر! @Farsna</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/farsna/443726" target="_blank">📅 17:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443725">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ev6hwjsthpT_gXBDqbAgkQErg6wzFFPwKJldQFubLxrBQYdT47fRDK8VDsuPqw3NVTZUiy6GCY7orvOIp55Pfkyjw1hTuGaKCSAR4iEeD3CMZeAHhltQta-7rOH4cPRaDStQXFmWvv_W8D7LlNcUZl-iRVZ3jfm6D9oLXzE6AsHwwE0MwO0IcxRxG52oeCkhhenP9CppU73y8g03YIVzheU33Qknq0U9q9nabrzscc-bIXd9n7I9B4n1seGFrjKvJkXJXQfeXGhOB84Nb_LkVBffyh9zwe0a603Y4F-59PX39iy15CRdbCuwOaCRx0Pn6qXd7NorheKKRfPdzor6zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
واکنش ترامپ به صحبت‌های پزشکیان: مراقب حرف‌هایتان باشید!
🔹
ترامپ در واکنش به صحبت‌های پزشکیان در مورد اینکه ایران از حق غنی‌سازی دست نخواهد کشید، گفت: او بهتر است مراقب حرف زدنش باشد؛ بهتر است رفتارش را درست کند، وگرنه بقیه کشورش را هم تصرف خواهیم کرد. @Farsna</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/443725" target="_blank">📅 17:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443724">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e27ae940d4.mp4?token=C5tCpCh6ywz7anghYZsDdo8gZvifaIalxTwV-MW3fQaE1cb_k1Ho6e9mt3yJwDbQewPsyk4PnF_FTQ9QmZT-XZinI0j4Cdn1kesKQt-puJikZeJgBD9_pZQSDascq4FdQcia5EO8wlTwPF_Jh7tavtzXuJj1HVpc4jP3RY2zl2_DRmbNDM1r2RZUgPLMj5uxX89ZhPkg56SgdDY286C0NLjrMiMkixaRpEFNk8NqTQkLGtufFlVKChQY6Jt0HgDk4zKfmpeyD1bmcK_tGSDoYiJ0Qv3bGl0k2qQbILQ0u_l4vgmLjD3SO2XsGhny9MN4IIQtk0dpsRTmdWw1W8Nztw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e27ae940d4.mp4?token=C5tCpCh6ywz7anghYZsDdo8gZvifaIalxTwV-MW3fQaE1cb_k1Ho6e9mt3yJwDbQewPsyk4PnF_FTQ9QmZT-XZinI0j4Cdn1kesKQt-puJikZeJgBD9_pZQSDascq4FdQcia5EO8wlTwPF_Jh7tavtzXuJj1HVpc4jP3RY2zl2_DRmbNDM1r2RZUgPLMj5uxX89ZhPkg56SgdDY286C0NLjrMiMkixaRpEFNk8NqTQkLGtufFlVKChQY6Jt0HgDk4zKfmpeyD1bmcK_tGSDoYiJ0Qv3bGl0k2qQbILQ0u_l4vgmLjD3SO2XsGhny9MN4IIQtk0dpsRTmdWw1W8Nztw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ مذاکره‌کنندگان ایران را تهدید کرد
🔹
رئیس‌جمهور آمریکا در مصاحبه با فاکس‌نیوز مدعی شد که به طرف ایرانی گفته است: «اگر تنگه هرمز را ببندید، کشوری نخواهید داشت. حتی نمی‌توانید به کشور لعنتی خودتان برگردید.»  @FarsNewsInt</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/443724" target="_blank">📅 17:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443723">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOsgIJys9zGl3k4JJVQVT2B70HdP7D24t2WMUyJT0JR0T-v9HVs66pXCIovUQFs8bl8FGQaEQyjEbWhNkOxwxka3GH53M2cNQjmPlnXhOQBzG-QE2u5ER1zjgBSGi0T74mTBNgWvUDYBoYPxKgs3j-JcjOPm42iv3XmicbrXGEC8C5DibUS9JhWa9-R6d9YRnUgtwtnWAf54wZrItOjdcf69lXGaLQvtJGNZJoKa_OgYvvZ-CMCO5EjP7aTZfoFBAAvL7HwmtF1B9mhvNz9iQ7dJ7fFyHlLHpNyITghu5i3gqD8lmzLSGyyUB0k1SENkBNoKtconUnHe4FXxzqz-4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ مذاکره‌کنندگان ایران را تهدید کرد
🔹
رئیس‌جمهور آمریکا در مصاحبه با فاکس‌نیوز مدعی شد که به طرف ایرانی گفته است: «اگر تنگه هرمز را ببندید، کشوری نخواهید داشت. حتی نمی‌توانید به کشور لعنتی خودتان برگردید.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/443723" target="_blank">📅 16:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443721">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5111e0f33.mp4?token=qdl3CmtHvoUJnYVG52PvgUn7xcdyxp_tulakXQMoTC2psdjqukjngHgCFFAEQCpZqMkNfbqHjSkKp3l4fUd4L6HHcGsi0mM1ZyX_kyAr2_TgGx5_UhTWhKl6nS3LInYh9gZwfOMXDxcQpY2DuZwm9WA4w3HCzcfmdMB0xlscQVcISfpoUsqoo0e6nP5U70ThTbFKV-Px1Mnel6Xyp8v3PiB4VqgIa7WuejonRaPpEzbkB2UMHqxEcD6qvI_ItYuy5lINTqqkY9fd5muQZ7oQ9zXtOS3g6lD72nnUvr1Si7TNQKmO1dzDFTd12j_DptA7Y7JTGcl119OqjcswHFCYvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5111e0f33.mp4?token=qdl3CmtHvoUJnYVG52PvgUn7xcdyxp_tulakXQMoTC2psdjqukjngHgCFFAEQCpZqMkNfbqHjSkKp3l4fUd4L6HHcGsi0mM1ZyX_kyAr2_TgGx5_UhTWhKl6nS3LInYh9gZwfOMXDxcQpY2DuZwm9WA4w3HCzcfmdMB0xlscQVcISfpoUsqoo0e6nP5U70ThTbFKV-Px1Mnel6Xyp8v3PiB4VqgIa7WuejonRaPpEzbkB2UMHqxEcD6qvI_ItYuy5lINTqqkY9fd5muQZ7oQ9zXtOS3g6lD72nnUvr1Si7TNQKmO1dzDFTd12j_DptA7Y7JTGcl119OqjcswHFCYvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرنگار صداوسیما: هیئت ایرانی در مقابل نمایش رسانه‌ای آمریکا در مقابل رسانه‌ها حاضر نشد.  @Farsna</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/443721" target="_blank">📅 16:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443720">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cad37392ac.mp4?token=o0EnfdwbTXpq6ktaMpBKYr-ga2HAmA4pT9yQmaQa7r7bLmdhANlBckf5AS3drcpQXiyzGtfidaNr63EW_ZRX4EJLAtIfjmkZTTtq-CjIjrrRQJbXBC-xJVVKBAMrFCj1SBDV1GaBB-4y2uOgO2lVs3u5Sk0kAWaV6Q4a4sqMqT3Z5BMVLkj7XT3UPdysAf7mAGO9StXLTuficYjZM7B48EzDxtM7cV2FT533SENodjer0bpxAJKlZs-aYi2PwiC8Zyl-hBVBKHuRiUEbMHyqxSPLTRJaX2q3QGmVXOkI7BblIahcfw-E8v6z9pmSr8LNJ9Mqu5hnetYC6bRiUU-KIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cad37392ac.mp4?token=o0EnfdwbTXpq6ktaMpBKYr-ga2HAmA4pT9yQmaQa7r7bLmdhANlBckf5AS3drcpQXiyzGtfidaNr63EW_ZRX4EJLAtIfjmkZTTtq-CjIjrrRQJbXBC-xJVVKBAMrFCj1SBDV1GaBB-4y2uOgO2lVs3u5Sk0kAWaV6Q4a4sqMqT3Z5BMVLkj7XT3UPdysAf7mAGO9StXLTuficYjZM7B48EzDxtM7cV2FT533SENodjer0bpxAJKlZs-aYi2PwiC8Zyl-hBVBKHuRiUEbMHyqxSPLTRJaX2q3QGmVXOkI7BblIahcfw-E8v6z9pmSr8LNJ9Mqu5hnetYC6bRiUU-KIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرنگار صداوسیما: هیئت ایرانی در مقابل نمایش رسانه‌ای آمریکا در مقابل رسانه‌ها حاضر نشد.  @Farsna</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/443720" target="_blank">📅 16:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443719">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb11cac05d.mp4?token=UKyo4M8PDmhUaemFe7yxg9pcmdCdN0nBj-pUc1xMoqPN2UhN9cwt8bj_WFHdU7MOIGxk_mhOM1pi-6nXHywR5B0kxi-vPDcn77n5maHLxLrogFHnAETZidaxx1VB_PgwMkmZ9NFl15GC34ffYPTgdSqVuJ2mL97BmOmiPZEXgCWOxMIavQKpmfBb5j5BLih-KHrQuHoRxb_-O7-biv3hfhBoykkrS0Wd4uu--UPhonDJ90WQbFHmInekdH4-g9bCwIxeantuaJUl8Xzr2PwK59GkVhwHsMffkvRO-fj-ZiAt8jl3TkJJJ1FMZb43Hl5AMKzOKcpJ6MMigFiQNnDGMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb11cac05d.mp4?token=UKyo4M8PDmhUaemFe7yxg9pcmdCdN0nBj-pUc1xMoqPN2UhN9cwt8bj_WFHdU7MOIGxk_mhOM1pi-6nXHywR5B0kxi-vPDcn77n5maHLxLrogFHnAETZidaxx1VB_PgwMkmZ9NFl15GC34ffYPTgdSqVuJ2mL97BmOmiPZEXgCWOxMIavQKpmfBb5j5BLih-KHrQuHoRxb_-O7-biv3hfhBoykkrS0Wd4uu--UPhonDJ90WQbFHmInekdH4-g9bCwIxeantuaJUl8Xzr2PwK59GkVhwHsMffkvRO-fj-ZiAt8jl3TkJJJ1FMZb43Hl5AMKzOKcpJ6MMigFiQNnDGMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز نشست چهارجانبۀ ایران، آمریکا، قطر و پاکستان در سوئیس
🔹
نشست چهارجانبه هیئت‌های ایران، آمریکا، قطر و پاکستان با عنوان نشست دریاچه لوسرن در بورگن‌اشتوک سوئیس آغاز شد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/443719" target="_blank">📅 16:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443718">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2e01a58c0.mp4?token=Q11XG_F23DOQnlQM07Q-uWJnp6fsEDU6KKElgnTBTLfN8BNwUGw2a3cN6dUJKPgBx_E96VqA5jimnzEjf_xhM32BtlPg6m8eNl0hf64qsvYnCh4xiyKWCg57IR-lP-oMTKF56upm-zsqhAAiereFYX-dBRrl1RF2OgnZvArC15AuaQYKpr_35TyWO1nyjIaSMf4apQRF8TBHhY0v_G8SuJLHnLcHQzP7_kER4053-iWO98G8o2ixTqA7rOXrl_5jKiLFcJOwo-AcHka33kkHl2UIvYv3kPrUe2pBwPN2MABYDyFvLKQJ_KzwkINfEz19HI6fxolccTe3rHq3BbRrrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2e01a58c0.mp4?token=Q11XG_F23DOQnlQM07Q-uWJnp6fsEDU6KKElgnTBTLfN8BNwUGw2a3cN6dUJKPgBx_E96VqA5jimnzEjf_xhM32BtlPg6m8eNl0hf64qsvYnCh4xiyKWCg57IR-lP-oMTKF56upm-zsqhAAiereFYX-dBRrl1RF2OgnZvArC15AuaQYKpr_35TyWO1nyjIaSMf4apQRF8TBHhY0v_G8SuJLHnLcHQzP7_kER4053-iWO98G8o2ixTqA7rOXrl_5jKiLFcJOwo-AcHka33kkHl2UIvYv3kPrUe2pBwPN2MABYDyFvLKQJ_KzwkINfEz19HI6fxolccTe3rHq3BbRrrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ونس: در همین چند ساعت پیشرفت‌های قابل توجهی حاصل شده
🔹
معاون رئیس جمهور آمریکا در مراسمی پیش از شروع مذاکرات چهار جانبه در سوئیس گفت، تنها در همین چند ساعت پیشرفتهای قابل توجهی حاصل شده است.
🔹
«جی‌دی ونس» گفت، بازگشایی تنگه هرمز و پایان دادن به برنامه هسته‌ای ایران از اهدافی بوده که به گفته او «پیشاپیش محقق شده‌اند»! و اکنون تمرکز مذاکرات بر دستاوردهای بیشتر و ایجاد تغییرات پایدار در خاورمیانه قرار دارد.
🔹
وی افزود، «اینکه آیا می‌توانیم روابط و معادلات خاورمیانه را به‌صورت دائمی تغییر دهیم یا دوباره به روش‌های گذشته بازگردیم، موضوع اصلی است. بازگشت به گذشته گزینه مطلوب ما نیست، اما قطعاً ممکن است رخ دهد.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/443718" target="_blank">📅 16:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443717">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df4cff1d6c.mp4?token=ZK4PmHMNrNdX0PlV-ht5QTf4h823szacTZ_pAjOgHEUuM-TzIDuBt_XwFX_WBLo3R9d3OMXoyQq0biKKawh7wCwkK4RFWJjLTQS6NbeLqOn9PVlcaIWV30V9Gdy3q1wKK99BfN-qzCPf654K0wEu0EZJ0iud_QnXMNONnDf7RlBysuBYK2oQbiRBcy5D34pQrZW-UKUOmcU3zXWjNTqxOSJKiC2YewQBUkL6qxL-aqsKG_Jj6d2zD3Ibx0fsmcUdt9YktClqVyuHvHbRLX6yrYOHyEnejn_c7hTg6oa9D0t8enH-UDw8CH6ujKwNuIzgDFhPmrys24TM3ai4nL3UaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df4cff1d6c.mp4?token=ZK4PmHMNrNdX0PlV-ht5QTf4h823szacTZ_pAjOgHEUuM-TzIDuBt_XwFX_WBLo3R9d3OMXoyQq0biKKawh7wCwkK4RFWJjLTQS6NbeLqOn9PVlcaIWV30V9Gdy3q1wKK99BfN-qzCPf654K0wEu0EZJ0iud_QnXMNONnDf7RlBysuBYK2oQbiRBcy5D34pQrZW-UKUOmcU3zXWjNTqxOSJKiC2YewQBUkL6qxL-aqsKG_Jj6d2zD3Ibx0fsmcUdt9YktClqVyuHvHbRLX6yrYOHyEnejn_c7hTg6oa9D0t8enH-UDw8CH6ujKwNuIzgDFhPmrys24TM3ai4nL3UaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز نشست چهارجانبۀ ایران، آمریکا، قطر و پاکستان در سوئیس
🔹
نشست چهارجانبه هیئت‌های ایران، آمریکا، قطر و پاکستان با عنوان نشست دریاچه لوسرن در بورگن‌اشتوک سوئیس آغاز شد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/443717" target="_blank">📅 16:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443715">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc15366906.mp4?token=OsoP6bhy08BA1CH-sBq8ymZjWlfYEtgBu0tDxnYqtPQQ0ZXAmcEuzSm49lpLh5amkS0e6xqLBBFo3F97hwx2i3aaeg8YegCJcNCGkf35bSoGB3s-UdQ6_JvHrVH0edNkMraFNDtUqsgPlzCYGHiVmJadfLP3DqEsB7hVm5uBlWaOIFJ1yKVVwdJCIIU4N-O8Yy36OFHUhK6iOkKas7u2PxTIkwAJz5W4AKMOzwz8kBfWiYqxsdH7TkJDAnH40e6alcNSmT7ZMxzcEleua1vk8vr66I25amRSTM_yu8BaF7Fwb1v1DHA978Oi6sqb4yyyUo1Br436A32qgmMhbgg2jwdOr_g-ChMWLRA194K9FPBWKyeAsIC1NccUBIjtoU-yAZG3Q2ECFQVBxF0CvzICGjikPmvfytTEThv18RKntxzhpnCKnH_SgF8JRk0k-v3SNfK75JeP_0V1f9IDy8wR9ZpcYyUpiO64OK35crFfhxip-y7qW2euywOUV8jeMPbQralmef5gKfQbSLBdjW5SuRDuiIISY8mnsGXn3ZK1ahHL59Ix_RpYCPE3ZOi4wZIMRgn2VKXCr_I3tdS-qeKdRNVIqwrK_1sDlIUsKzfDdoxbKByVD_M0AXgfXNbr41GNq8MZof96aXb427oQ_GBhbsppMy7vSqJSKJfTabiw63I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc15366906.mp4?token=OsoP6bhy08BA1CH-sBq8ymZjWlfYEtgBu0tDxnYqtPQQ0ZXAmcEuzSm49lpLh5amkS0e6xqLBBFo3F97hwx2i3aaeg8YegCJcNCGkf35bSoGB3s-UdQ6_JvHrVH0edNkMraFNDtUqsgPlzCYGHiVmJadfLP3DqEsB7hVm5uBlWaOIFJ1yKVVwdJCIIU4N-O8Yy36OFHUhK6iOkKas7u2PxTIkwAJz5W4AKMOzwz8kBfWiYqxsdH7TkJDAnH40e6alcNSmT7ZMxzcEleua1vk8vr66I25amRSTM_yu8BaF7Fwb1v1DHA978Oi6sqb4yyyUo1Br436A32qgmMhbgg2jwdOr_g-ChMWLRA194K9FPBWKyeAsIC1NccUBIjtoU-yAZG3Q2ECFQVBxF0CvzICGjikPmvfytTEThv18RKntxzhpnCKnH_SgF8JRk0k-v3SNfK75JeP_0V1f9IDy8wR9ZpcYyUpiO64OK35crFfhxip-y7qW2euywOUV8jeMPbQralmef5gKfQbSLBdjW5SuRDuiIISY8mnsGXn3ZK1ahHL59Ix_RpYCPE3ZOi4wZIMRgn2VKXCr_I3tdS-qeKdRNVIqwrK_1sDlIUsKzfDdoxbKByVD_M0AXgfXNbr41GNq8MZof96aXb427oQ_GBhbsppMy7vSqJSKJfTabiw63I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور هیئت ایرانی در محل برگزاری مذاکرات چهارجانبه در سوئیس   @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/443715" target="_blank">📅 16:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443713">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7f02f1da1.mp4?token=VV1cUV3OoC7_ZCJUClkZiLYjvSkzdLH_8VWEaWMvVWGwtm7JqlVpWts-WNe50ZLSFtMun0w6QSm0C7gN5doKD0cAfjBXvV2JDmLEc1pl2ApBrQNf3TLVTodIbZ-hGsWEsl1HhkLAXuMb6MN3RaTHtlr4T7GFzosHsbl3r-V6Ug2sWkk-1hZ_QzbbYZldP8djLejH1xF65OQ8kepMZKHhsGUq5Apc-12QpbZ2vcAf_kq8ym3ag3nuPAGe_wS5oXP1Bc1ICArc06WMQTulEHwc4F1owQkYMro8LovggNoVZZv-LNLKhhD3dpEItaovIo47jkO9qadLoNFfPuW9VoJOBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7f02f1da1.mp4?token=VV1cUV3OoC7_ZCJUClkZiLYjvSkzdLH_8VWEaWMvVWGwtm7JqlVpWts-WNe50ZLSFtMun0w6QSm0C7gN5doKD0cAfjBXvV2JDmLEc1pl2ApBrQNf3TLVTodIbZ-hGsWEsl1HhkLAXuMb6MN3RaTHtlr4T7GFzosHsbl3r-V6Ug2sWkk-1hZ_QzbbYZldP8djLejH1xF65OQ8kepMZKHhsGUq5Apc-12QpbZ2vcAf_kq8ym3ag3nuPAGe_wS5oXP1Bc1ICArc06WMQTulEHwc4F1owQkYMro8LovggNoVZZv-LNLKhhD3dpEItaovIo47jkO9qadLoNFfPuW9VoJOBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
محل نشست چهارجانبه ایران، پاکستان، قطر و آمریکا  @Farsna</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/farsna/443713" target="_blank">📅 16:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443712">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwz3TY1t4AKQ6ZI409A0SC58VjyvWE8QCHUYRgSj-k26iSuqMaB_7vr6TLotgKaQM80gBFDMHPUBsBsaIV3Tr7O-2dzKnQ81WCRLW5_Rsg5Gf881Qm8c70wuygiryN1vQ5WE9gGTndAR6-44mqP8ZryOu3y5dt966pGA3EjRf_YsBOdvZ-6qxC1lWRV8mxCh_1BAVN5gSqPm3dS702uqQjPtKRPPxjRdIOLA10tZEBaHJmTIe37AoHA2b9a7Ai6sIHKU-YHSbL65i3nVyAy1VPHLmk7Cc8ldY4RgKV7jE648YlZ3_K9qzGzC-6XAvmKkBReatb2FIR7EJZZqPnJoZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دیدار نخست‌وزیر پاکستان با قالیباف  @Farsna</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/farsna/443712" target="_blank">📅 16:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443705">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B3ihs45hHMvBxpeiAcv18DX0agrcvW4uPmnAx6lqMobOJhW_iOtG_PIyWyHPp-M-A-vZ5SFsVMKNZOVXy67_kJLbHJdmpAQ0AwgyQvxFGXhkRQkopTWwOtiRFsMotpTR3Sj7mAi555yPGKRnvSa1pKfoSTLYjmARz7wpa6GIzyoBby5e3furfqPgM45MEdpCZR8juQxYtulLUlbV4nzj7rzSMBVjtcnfzfMisZAJ6Oh7gWK52WTPsmiy-w1Z2Xke08SPvlAELpidLiaeiPcytzTaFP56aZJ_Fv-NzhmCSYyq5Ztc1TgYyieJ_DksVsCsstnwwMTjKYgZ3kcEcUxQMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mLf-jFsiZ6FfnFUqZ5t6FtBBHLPRTCJXU3BwM7CIDQGf_ja0xeEqcAsaP8ss1S1gV315mSDGyhhqyDk91hN0RH2XtOX23SGKEh0Z_nsZvFx_5pfRnFKXHPxgzLWZhAanC4MVyQjPt6mI5t8dhKuF43mkZRnE-SkJ0sSM11x7N1pJm5BcVGhHNZH6nF_cy4UGXS8ixx9ZPLGXZ-9dgyIAKZAR7zGnId0bRVRhkB9k7fM6kZCzSZdLGjf7OyI6MbOaTZ5U7-b0GPVegzXofc6HviM832iwJLjRO8WLEnQ8eTcwjSGVsDFyv3mZL3psOSLo-LHl_ApHZVrCTrO2-0Ylfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rrYLBpJZArvt-a2O4KhD104XADdKfHuIhaMj8dMgPXRKuNp-ZjPIPRzKkkKAbyiW08ItbOTOMr377gUyWNNF1fVRqZztBrFeuFuhPyB5W-KevwYDEbIsXrqLsybJAZQwQJRV5DUClNL6GUQQ1-j4ekO3iuf_2bqb3ECLb9MBNDq0h-fh3h096-E1Xahmk-fMpmVtRSyZrnPzx3ngIlw6UWqNGqAGymKzMCeVnbkpTWMxQtXVYvmpvnqrlUEWS_ySUWKFCavtC4lzE6NQ08J4dgki4aT-cy39TM63_KEtk2-8CN12N040941a4Zcah8yQSE2cS77n0a4QZbM6Ueb4EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sMsQ6nGj35JgMaS6we4jP44JIJW4qLvkPSwUWEIVktDZz0BTwN87FAmxXXuIhUYolMoveMibFRyfp08Z-7qvF3rMPpJseyM-FGKYGRy2ArJzEwYRXdZZnVpM9sJ6qr4K-WRRmih9n7d6eEjkibksQ1OpZDLiJpp4O_piHav92Cg1ZFfJ8_fzBctqu0V8yTSaq9boqnCB2rurHXjspEVceN9_jTD7yQvdv-cDolMmQljHwLOlXYyUmO-yrtCZSvHAbZckVugq0CO3b57zdf7bWd2eZ9cZbtJLI9bv3_T1eLNWqQW4XJ0WeFM9z3f2YVbETKUd_VqpOSNo35_nRX3c8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qPy2A1PRFlJK4M5e4wsiYlO3nVT2rDnU4jCy1PzjK8e3WyyMaB6jXkIBO60yp9inEtLRFZWzumeg57DgYZ3FJg9k6Bs9Na58bSpEdWiB9S0EDudnNCtQJVkBt0rmtL6ouDrx0becvhC1zu2lOyXqGp56pxVqYHA86co1c9l2QkzITM7j2OFalEEaGCdZ6Rgjf7mm-ADiFNHUeRtMiPKHGSaySq82xLOW2AcbRYTqUnG4IDzxzQJ7k-V2dHYrsmuUls7vposrsUdNWlLbrnrvut945zneRSh8KME9t8Ftce_vss_Ew-H3ejdzogDKhSwDoVjB7MQUsN5V5qvMM3Rtyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BSrSfFEXxoFCEyDsZ2TRe0_UwLaT7jAdUsxJhOCzjsE35Vm-kBeeOr0WJsOc8d41TfUhHSprn54WREh0bbHutJ_RbBi-gWUdqG9JGDd9HfJQhBAaBj0RGYwGHwH6koqvLKhA11SQCK9PTj1AcdK4yCR1NCIESugvQklCUopzqsWo_wGbk1MX0NDpgBNiGL_9szl_UXgf9Uu7EnPNBdy5nzVT4dcbuXC6JZQ3xVyIw7BNMsjE8zkRS4rJT2Ma_3FiDzJVQcR8oO0gEDVW7kOIgB98DNXNHK4vWgwDtnk_m1p_bVON9jD_CBnTwcylo_MN3a62yUqvgg8pqBmZeahTYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CpKCs5qTtvXNxtQCc-7sFzBUaBoNkOT4DvHzwJjgDvB0MzJIN9lFxfdXMIFfvPL8kNbd7rY2C5-7wlwfC4l29_iaIR70VVfrg1xxROSv3721oR6b-OxxWeGK-D8jHxVVrSM8GoWdXVlk473QRJHszh8iGu_YICcmUBTtMb4co-u8xY8ORLtw6NqlvWgijXncKNMCy0UlLncKV_n43k-4PD6R3YjBC8Uegbwncjz-UGDl6SaMs3nIY_9wdhqwrEEuwiBH8CtgnIG5EwzslSo_ze6qBi1QwouKLZiUoypCOF_WdMeqqBIG_9K0jFCDvxuZpdJupm5xxWw4SB7DfMomIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آیینی ۴۰۰ ساله در دل کوه گنو
🔸
مراسم ۴۰۰ سالۀ علم گردانی و چکچکو (سنگ زنی) هر سال در روستاهای اطراف کوه گنو، برگزار می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/443705" target="_blank">📅 16:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443704">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpPi6py5VeFjCwfCwuq2tcBYJy4WHfeam2FbUdAaAqagxcpNk6BDK-3tikYzLUL5bB_lsWOZ8b1YZHkLyd1DniHqlsyhvwuuIpQ4s-ir-kSDrfhqIvoLJxJM3iRitL63gHI__DuLj4oWcVMVk0KcfOiJJrqmjiOz-j41cOd7fSLe546bLeEU_u8aCQiP1XK_i3MjDQjXrgpLfYqtwzH86qnNr3-v8a-n5TcyVle7lRZuY3JwE0Q2NrxsM_2A3dti3_t72pbgqTmRFdmrVU5AuZ66z0O64xhI4H7O4kkZURzfoICk6F0202Ygvc_uOow52p9FTovni5NLyoxsKY561Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
حسن یزدانی راهی ‌مسابقات جهانی شد
🔹
حسن یزدانی در ادامهٔ مسابقات انتخابی تیم ملی کشتی در وزن ۹۷ کیلوگرم، با پیروزی در برابر آذرپیرا راهی مسابقات جهانی شد. @Farsna</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farsna/443704" target="_blank">📅 16:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443699">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tQoMyFNMh5wgQl0VZgs2o28mdcWsFIsj44qxoHutyfR_Goxnrm6wU1u_TbJcSPwDmiaCqjMCnbDh0r6VohTCN-MF3xNS9_Q_ULFpnHKs5shdPT8M5Nyf2lLrAA6eZTzMKgKtMagDhPybsnwt6qP0ir9L3fiD6KbVYwbqzybcxB92yQwgzTrMoYqBiwtGEKTUNNyhw_I_wD6MGGnUcvdF1x_2HkESroeted0QTRbTDDPdRYU7A24vOG6qU6Z0CEIHlw99gUhz5zbuPZ-D6cRX_zXBki9YRKnlqy1tkib3HmTHlWzWEDZJo9JJWkfp9OrLCWrTZwRHqfwNgkwzjC5kZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AeIzA7Uc4zU0DyUDD5BYRgUGR9CRt8kd9kim6O2VoJDP7APynKnOotmltRlqsTSIxC4aXxcMTH3XjvQAdIJGwVgttDELlg1AtMvrYj7viheejfxk-kTPpw8B3FY2XPwYaJWmZ5srkvCdnS5h6N8UZW3jj7-4pIwtA7RoIadrSOYkUjJSwFwbVylnk0PRQkzb7G87V7vJzHCKaYTgjpKZnXJnVoklypGFXwomdF2dB4fx7K_mpeMhmHAerV8cDWEZd9fPlAAwD7JpdqqNN3eQa6L4IhYoyeVeiJpz4rnv_VcN1_xrr2rIIMHalMDe04iBo-L6tSCuE65Eb_LuFgN7hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M04u2J316r_KDw6rvMTn2hTctiS1a4S0EiCOetBHv04yGptEfJ_Qdv0fv5hAKet4V4wTUsy7Q4lCaJFtwdoV0U1TYRbkfTro08Iyu54GrCHtzIWqQsBUcJstlwpOGjReomeYL3iOuAyc9qbLyO9u5WE__esJt7Ymo913lvytS4TNEjxAo4ol0DN6b0sM520dIFgkOi9iWoeWFdIjgDTx0giUAXp_nZs8yKiQnPBZmgkf5BvoyjUrhRXUpm3h6QHV3qbRu3i6-KQKsKAVFjaB7gxHaNzY-7vSLUB77nMZ3inB5eUKBUjOV1LB8sI1kv1TYUxQ_4Ul43fwFHHoSkwYrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ft4aEJaGCX1aE1nqrsKdlJZY61By2QMMu_WEb9b-DdVVSJi3zOu_5S2-V8c31mlDmrm17RFsMpbN-wEgVe-3HgcLz3iIUwmvknCZMUnbG0k2ykeNOE95DWpgyI9xcDjs9s1CSyXj6F9matFvVKUdL6UgJqzXMS1okvH8x5f9UKmVUcpZNtQy4He4bEzcfENw7sYv6EUepz5jM6yqrd0w4e03J578u0qi-MIItzqtXzheXhak7Dc7VLSSOEzzk3-yoA-vj17pX_qCJ7y_zUoXAlb-iB6mZrtOpEYJKyJ7WSNbZTh3mjCTn9DuT_FNxXoWVs0Yk8SFEBtW-tj9qAuRPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hSllrOJcnS6e-xin6764ta8JIz2M-RMulppFH18_9vvyrnKURg87Kr8F3xBLhh5vK90k6EeZLfZlTXBXVYauUuzDwlTncoK5G50qKiYF2baZfRu6FAehbiFBWMCnE8T2AJbwvh4t1hmyZw37hMken4wN4BI7Lx8n4vf6UR-YzfbDRsrR3xoWWiz6TjjLY0Wg42pPH-T7_Rad0eZawsb0zr5y_lwKmyYzPdUesLAsCwDzmD8sejpqSgrj9qSs1qxOAaHp5pOvWwb3AR89HaFZ7SFykUBTVWr_dsShkX5QM4I1sSFDb2PKy7VxreW_LCm82FjIZKo96QsLZdH5e2RP1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">«آلبانی فروشی نیست»؛ تجمع هزاران نفری در اعتراض به پروژه داماد ترامپ
🔹
هزاران آلبانیایی در تجمعی در تیرانا به پروژه ساخت یک تفرجگاه لوکس مورد حمایت دختر و داماد دونالد ترامپ اعتراض کردند.
🔹
از اواخر ماه مه، معترضان هر شب برای مخالفت با طرح ساخت یک مجموعه هتل و اقامتگاه تفریحی که با ایوانکا ترامپ، دختر ترامپ، و همسرش جارد کوشنر مرتبط است، تجمع کرده‌اند. این پروژه قرار است در بخشی حفاظت‌شده از سواحل این کشور حوزه بالکان احداث شود.
🔹
معترضان بادکنک‌های قرمز به هوا فرستادند و شعار «آلبانی برای فروش نیست» سر دادند؛ شعاری که بر نمای ساختمان نخست‌وزیری این کشور هم به نمایش درآمد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/farsna/443699" target="_blank">📅 16:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443691">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G3eQS-27rPI2-WXivM-tJ5BydZLY7yONGd4hwJNcvT11E5CNijEzGcXu6hsAzAGFXbCwtRh8nvOB9QiV4wJNjXvPgfWCL0pYkpRd0XjgWEq85mF88Lei6-vMWgz0HSrN6mZqPstbVVWLrFdsrJuKaQzR_2mCkImfRzwiCumSvBeBrvTgpvwVMJiqt3k2tVHiA_AkOozGUEgFYrwur9r0sORxx1-ij5Nb0nVwJYi9OUI6_QpDQyG5b9y902bsWiFVGiwQItxrEa6tnUlSznZMaRRFGKwyME5dPZ-lPoZWH3LOGVU4hJ0ICzE9hOtnAfznW4U_lsWvko8n_Du356IPNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ccrstn96uToemf2KEc3lIrVEBqJ4IZqmShQzx4tjpaaQvg0s1Va-TbesVANj7261c3nv_EKe1d-xYcPAF2tPOyuk6c9YhtFcBZ3SIh2l6pVjkC8NDnY2QF8pdsEzt2cIefqwKO6R0fDPW2Vcb1Fi-yqvPfHdS8RU1-Wlz24eHfJ_dxpL0q7wy5-aoRP6pQkPC2oQNai6M-QYaGEsj5prV_3fytiYiqOHR3o4UpnuFfm-J36ZenLS5yAurey7CiY5O8SndaeM9hbAKa1dkJ0OiXckDN19wlWPwTra_0Py-e4AWgCCmb6G-lhTN0XtCRqwfCWwIeTwnf9VSxm_dattVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PFBAsNhwXcbNlpwtb6tpzNYncq4fVIcmy5SYePvJb9wH6OstZoasK5GjMSaVamKBUA94yG9Icnd9GTxp86yolMnGWANmMrwqAMwcQtZMbYvCcaVb3MPD_z5KNXHXybTQRZeIQFJkxVuAD_3EyW4I2Be-scI7J7WD-GSE7tBn-ez9wDvOBaAEYOMJBSc6gR40kfJhxJZrhIVWbev_zxycHMDyfAFpIq8tOc3vSuQr2DU5_7P3KLF-5Klve6on-Hnv5Sem3mhI_-N2gR4lH-KpTDmyh_eKV5iO6gMENDzT5-EC-h_PSgDrybxFYIbMpJV0b0lkJj5CXzhbvEd5WsaGUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TfQg63JUGQEey78d6-8OIAsAotR6MNChsFMRrEkX52Dnho0NhgS3_RwY6W38vh5ncGNlssjxFazFv5t4cLQ5eouWvJJOajf0TRtGFYM7qBRjaqusa9k2nvTzgIrnjxorxA0rU_h1NPQn_EnVGgrsCIDxeKGGa7YNZelFA5P17UzeRELzPReIXIM0YQ_Ie1xH5qyS-enesc__wrz1p0tzxfv_6Y4Jnus8DLGYd7_VSYYdGKz3LVh3qBYSdac6jzheJzH-KsKFEbh9T-N8A_5ylVO69OqOuhCk5QtG51n9_Tf16KSsfTp3THttLPPZ5iJoE6BVIZyQTeXt14ecb-asHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NV8Yzpjg193KSstKv5Z1GNPIO5VxySfmS_vNAT6qLmqFIH0OSJ-x2A8_zb0yiD5a3-c8KL0pvWKOw6s-URaFzppFYabGgTCtvO0EFJjhXOv_1YAnqbtzU0WygU2cJELfvshZ5rv3DDHc6qnZ0mIdUXttphbN-agKEMljayyb-V3qZScGV27dv657nIUaPW4DSV7oJgy9GIdcFihacs_IS--6mMkRFDv60ZUO7-9QasOm6xbhRi-Cgu8ovbn_nNKZl7EIUKJBh5YD-6zbNTqUgqjPMAKsisUGJ5ieVF0zonquIFPMoUwC9NCnd7UkJKDlcvr1d869n86L2oel2ah6CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gTzge3teh0qwgE3m9sbwTxLWabGs_EDb8Ooh6jX1UU7lQ97MuPj22f3ptFV2-b-uIy5Jj17N0yyjBMLdxLp8kTn2ceDuDUzgEIAalZqi8A15thbXlnwksU3ESZSD_6yyX1uh4X-C_au9peL9FzQ4D3YVp9yyPz6-kuBkdM22NVltWEhqLmPbW5evINJ0vnuS4Tr5CO72jZ-dgw2n8tAZG5G5qd6KfzaEriGJvTpYkgqiI5mk2jqZcOVj7twD8F85RBsuCQ0gaZKdWDJ1a8DZx2Z5iF9L993AKUMBzXZuMHQZBPS3tMrnKxHAgCStEcmV0MDEJLYhqJYB1te-TzUWqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ywxe_xl5m5x4y_8OOaElmNjZBxKGA-MHc6VNUXKvwW64aNRG7_KvNoEGYMSFWCHBlK2nYxowg-NQe8owryMCXeVfsiSUmurwlebUqFqVYId3PIUZ2i5vDnXa94p5x5viKWMLCH4yf0R53MyhyN-pIHLJyrIqa65s4aY1Nmf4LQwIEuLhOatFXMfAZgyhBFMJxPmuVCVUAd7tVMfQXqqrX36n4tAXmqHkQUxRMx2EhmdhK75iFVBm9KgGifCY-Ls0Cmjn0Hdf79iU_ijFqOs_V_OS8ZYtSDHGKPkFq1XX8A0-UOjY-EG4lFFp9I_JWusJycEgUyKx6Q2h5snIh8xUQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم «احلی من‌العسل» در حرم امام رضا(ع)
عکس:
حدیث فقیری
@Farsna</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farsna/443691" target="_blank">📅 15:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443690">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzBYO2d8v4tSVerfv2Rt9OysG0_BCC6iZtS26uWQ7NLbcxtl7I0sgpSjxzDJ9LF5CMcMMyBDiVSfjPRuI0PwvEZC-axFtgS8rX9mvOAwV2vgTykU33uGEWRu-2iHqt9NJlb9CGZpcI9idCS8JIZyDjlEbOYwGJupF5DmomIFnYzGNRM9fLENs-iAop3WYazVn86ntnhJgDefCyhQQInWTFZB0y7QXog5FMtrNWpxyfFVI8Vr3IbiBZ9sprfhuYCZtvmN3B2WYfdX0EVCnMdVqvC-k-9vY24LOuhS7zTxfukoxexN9ayXtbNKsdZx1-qxEFLfw01nDO0ocB2hX7a8tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تنگۀ هرمز از همیشه ایرانی‌تر است
🔹
اژدهایی، خبرنگار: امروز کشتی‌های کانتیتربر در بندر شهید رجایی پهلو گرفته و کالاهای اساسی و قطعات خودرو در حال تخلیه هستند.
🔹
در اسکلۀ دیگری تخلیۀ ۲ هزار و ۵۰۰ تن شکر آغاز شده.
🔹
نیروی دریایی سپاه می‌گوید همچنان هیچ شناوری…</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/farsna/443690" target="_blank">📅 15:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443689">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">احتمال شنیده‌شدن صدای انفجار در حومۀ بندرعباس
🔹
سپاه هرمزگان: فردا از ساعت ۸ تا ۱۱ صبح در برخی مناطق حومۀ بندرعباس عملیات انهدام مهمات باقی‌ماندۀ جنگ رمضان با حضور تیم تخصصی چک‌وخنثی اجرا می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/443689" target="_blank">📅 15:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443688">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1y1KpmeFxKi2FwQ5lHmSgJrsUmqDQBuTAa1pxFzGQxV4rEEtviMsI5GjhmBaQ1MKXrqCw6cxsZGc5Xr33sYfCSqYlNYe-Gme4YwP75-u0ye31X1IfL7am0EjHGKM-iyjywcxDc7VSDKkec2ZxMqVrDFvPSX-L5V3x_k1FIQE7WoajIkMqdQ87Y5B84-b6-iy47CTctQPtT_2Rz9Lcu0aqkfBsrWMFjYJHtzVt5jpaX04zt-nIt8yKJYsMcTB3B3P1T_tAhoL8Fu51l9Lqo9DqazGctpGDTxNmHz0IQE9gAeB8ZvVQ7kHS2cs0GMvU4elXYGD5bvahglhCghGE2iZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس شورای‌شهر تهران: تصمیم داریم رایگان‌بودن بلیت مترو و اتوبوس تا بعد از تشییع رهبر شهید ادامه داشته باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/443688" target="_blank">📅 15:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443687">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85fc759331.mp4?token=jJQaJjSRpBAXlmG3Dlz09dRS_9PexMdGy6OgIrNiUG1LjZbzxWHytpZlkUwJ2dxUCciwufOD1LoUL5SSt2Izz_tSnuCQtZ-oNhxkinv8Ya-ybTRs3C4kMtHA-gSFKmu3pAumkfot3UM3jDQXeF-hPwTA4mIQmyJ9el4Aeqfnqc9Nb4Thi3-k-TX_ZwLaqEOtgwqPpWhQqqub4YwCCWgtDdAfDxVWNBUSLvYhbwD61ZuuxjRYoVyKuc46wfeVJ9oVIuSntWQbvPaxQ8Wqzr1knpaIg7bP67EX8SIRMeeXioOo5EMfAcUp7ntC7xyv2AeAZ9Z_jNV3eArCNRjbDg_B57WFoZY68BFOAgROvmb1QE3eVkNC0SY74Z0coFHr70kByIWAny7O2aCcPBi1zrKqXPpVrF72kbyFo1iJlMIdtkFyDIPlD1kDfia_ES6i-iYXkwlyUnEjCjNkFDPlBjc7s1q3HLGycIG6E-Hvaj-kk3RCUKlVYnp2agupvsTjEuWfwLq7a96n-cI0mfWr4QKKFpFDRT5zhHM39l5jZJSWXuli6iY0Tp-CAFcnwsnTugtS6LMMEgbu8jtBF6ZC1JNXJbg5De250rXYnQPjFz7zgtY2hh-6J0dyvCcvLSjf5Qsbd_DUrDwPm6X7WrloB_AmqsVHg_RkHp3grqL06K-xIVo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85fc759331.mp4?token=jJQaJjSRpBAXlmG3Dlz09dRS_9PexMdGy6OgIrNiUG1LjZbzxWHytpZlkUwJ2dxUCciwufOD1LoUL5SSt2Izz_tSnuCQtZ-oNhxkinv8Ya-ybTRs3C4kMtHA-gSFKmu3pAumkfot3UM3jDQXeF-hPwTA4mIQmyJ9el4Aeqfnqc9Nb4Thi3-k-TX_ZwLaqEOtgwqPpWhQqqub4YwCCWgtDdAfDxVWNBUSLvYhbwD61ZuuxjRYoVyKuc46wfeVJ9oVIuSntWQbvPaxQ8Wqzr1knpaIg7bP67EX8SIRMeeXioOo5EMfAcUp7ntC7xyv2AeAZ9Z_jNV3eArCNRjbDg_B57WFoZY68BFOAgROvmb1QE3eVkNC0SY74Z0coFHr70kByIWAny7O2aCcPBi1zrKqXPpVrF72kbyFo1iJlMIdtkFyDIPlD1kDfia_ES6i-iYXkwlyUnEjCjNkFDPlBjc7s1q3HLGycIG6E-Hvaj-kk3RCUKlVYnp2agupvsTjEuWfwLq7a96n-cI0mfWr4QKKFpFDRT5zhHM39l5jZJSWXuli6iY0Tp-CAFcnwsnTugtS6LMMEgbu8jtBF6ZC1JNXJbg5De250rXYnQPjFz7zgtY2hh-6J0dyvCcvLSjf5Qsbd_DUrDwPm6X7WrloB_AmqsVHg_RkHp3grqL06K-xIVo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تارتار، سرمربی گل‌گهر: سناریو چیده‌اند که پرسپولیس و چادرملو برای کسب سهمیه شانس داشته باشند
🔹
انصاف نیست این دو تیم که از جام حذفی حذف شده‌اند برای کسب سهمیه رقابت کنند. @Farsna</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/443687" target="_blank">📅 15:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443686">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cdf401ae2.mp4?token=odHJtsSwMwZ3pViwmcKWbI4QdM1LYCItLoxdWjnrsPneyQxEPR9r_2E_2onaafxARkZxfWfZxaJ-YLSP-aYhastz_nds0wbIDFX0DErDxpKvANMjnSqAvN0GSGctakVhRWWr_urWF477DthHfXWqcwdmQqEEFx0_DZnVZtZ8vz6Hjjl7QI_mDEDMtqsRUWATb70NUDEi4JIZzmi76z6YGpGCUM3EAFQEt29_umYDGo64Wz3nzW5xB5qePPkM4cVrXXzFSambntpimVbTzHmbZc-x3htKjrK2UiF7ir7K_vgFPBoOUyRm1QhBHFyczKn6AGbWSxD9ID0ceeOBpFGNBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cdf401ae2.mp4?token=odHJtsSwMwZ3pViwmcKWbI4QdM1LYCItLoxdWjnrsPneyQxEPR9r_2E_2onaafxARkZxfWfZxaJ-YLSP-aYhastz_nds0wbIDFX0DErDxpKvANMjnSqAvN0GSGctakVhRWWr_urWF477DthHfXWqcwdmQqEEFx0_DZnVZtZ8vz6Hjjl7QI_mDEDMtqsRUWATb70NUDEi4JIZzmi76z6YGpGCUM3EAFQEt29_umYDGo64Wz3nzW5xB5qePPkM4cVrXXzFSambntpimVbTzHmbZc-x3htKjrK2UiF7ir7K_vgFPBoOUyRm1QhBHFyczKn6AGbWSxD9ID0ceeOBpFGNBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر صمت مهمان جلسۀ وبیناری مجلس با محوریت خودرو
🔹
سلیمی، عضو هیئت‌رئیسۀ مجلس: وزیر صمت فردا مهمان جلسۀ وبیناری صحن علنی مجلس خواهد بود.
🔹
محور اصلی گفت‌وگو پیرامون مسائل حوزه تولید خودرو، ارتقای کیفیت محصولات داخلی و نحوه حمایت از کارخانه‌هایی است که در…</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/443686" target="_blank">📅 15:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443685">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef2ea02d45.mp4?token=a2Pqr75iWXveJPyuF6nX0x1A6b_Mcf2yiYXQg7LRm6rqpjZJ4ezV-QanhTKg5uesTGZG8-gFYm_JjsjFLzxCuP0bcwJTU8U37_vuldgNczn6bTBLnJs_ORh-EYHFvQkYVOcn3343082GSrTPiHkOXHcuvxWhsJkC7sOyKBknmA870l_-Van1Y1Y5A6Qjz3WViQjeos4IwTltpYMQNmYwPzKjAam5RGgh2oJR8jY2MsxBLySekRFPCjnXGSrzHLwsRNpaJOMZEAqmRy3VdaZ2dDO7Bc9WUmDCbBF_4-AvR6pejM1B5Haj3I_TCHup5cNWW2GlZASnWI0p0oWT9weW2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef2ea02d45.mp4?token=a2Pqr75iWXveJPyuF6nX0x1A6b_Mcf2yiYXQg7LRm6rqpjZJ4ezV-QanhTKg5uesTGZG8-gFYm_JjsjFLzxCuP0bcwJTU8U37_vuldgNczn6bTBLnJs_ORh-EYHFvQkYVOcn3343082GSrTPiHkOXHcuvxWhsJkC7sOyKBknmA870l_-Van1Y1Y5A6Qjz3WViQjeos4IwTltpYMQNmYwPzKjAam5RGgh2oJR8jY2MsxBLySekRFPCjnXGSrzHLwsRNpaJOMZEAqmRy3VdaZ2dDO7Bc9WUmDCbBF_4-AvR6pejM1B5Haj3I_TCHup5cNWW2GlZASnWI0p0oWT9weW2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گفت‌وگوی تصویری قالیباف با خانوادۀ شهید مدرسۀ میناب  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farsna/443685" target="_blank">📅 15:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443684">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-text">🎥
علی‌الاصول دقیقاً یعنی چی؟
@Fars_plus</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/443684" target="_blank">📅 15:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443683">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/taQii5NeyJacQ-MONnAmJ05pb5Sm1tIa3AvMmezh1bTDgEgqaF7NELZQHpmXNbPiA3YQD4wY4tG0AkEc2jnPbbaaB5M8Im7-NRbHHM_wrYbewv5lhI9hR1bv6aLRtDUcjC5GK-qhjeaqrBxFSaoWOPsRnqZunlrxGcCY8DYeC7mdklVRNZTuz7mfuABAAW2Ru7hEZYnCyOnl63NVyXSm1BtnZtlTRIqqDiPeGWNAxTTxS6vbllds-1NhWnbl-yL9Yy8GhO-Flvf7YIJa1LAzLFK99j93ILEHypOgb9gQcgOKlDFT_qtbnHgzITPnyA5zsQUOQP5LDUXt6vKcjq9ESQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
قطر از آغاز اجلاس لوسرن بین ایران و آمریکا خبر داد
🔹
وزارت خارجه قطر اعلام کرد که «اجلاس دریاچه لوسرن آغاز شده و اولین دیدار بین آمریکا و ایران با میانجی‌گری قطر و پاکستان برگزار خواهد شد». @Farsna</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farsna/443683" target="_blank">📅 14:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443682">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAuiok3fEx5SIAk1JoBshywt_1y06mujzkbECqhTJa_CCIKliN0eURKygd8GP5T3Ol0HSPvpwBN7Ma95y2_XgqeQ9AbKaE4H9YLv12Y_LPN_k117npIyQFpFs9Ve-LJfhGO7JZqxPTG4_8fvPEjHQkEDTbzSbv7mzpkaJ-T0P7HoEBT3XWLxxvSAKqsnP_DMiUmFZJo1Pw-RNMWxetvkeKxBMMj53xevRx5wiLxbDKcb76pfLzq4apa3S3FeHS_Wjcu80XtaE1PbH-PajbbiTl9J3-bSWjBcYR9XsUxJwmDnBZ8wU93OoXnIWoEY9kHzpGusFbAQczBKjP1pvTJutQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منبع آگاه: گروسی در مذاکرات ایران و آمریکا نقشی ندارد
🔹
درحالی‌که برخی اخبار از حضور مدیرکل آژانس بین‌المللی انرژی اتمی در سوئیس حکایت دارد، یک منبع آگاه در هیئت مذاکره‌کننده ایران با تأکید بر اینکه پرونده هسته‌ای در دستور کار این دور از گفت‌وگوها قرار ندارد، اعلام کرد گروسی در محل مذاکرات حضور ندارد و هیچ‌یک از اعضای کمیته هسته‌ای نیز در ترکیب هیئت ایرانی حاضر نیستند.
🔹
همچنین در هیئت ایرانی نیز هیچ کدام از اعضای کمیته هسته‌ای در این سفر حضور ندارند و این موضوع جزو دستور کار گفت‌وگوها نیست و مذاکره درباره موضوع هسته‌ای در صورت آغاز اجرای بندهای ۱،۴،۱۰ و ۱۱ در دستور کار ایران قرار خواهد گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/443682" target="_blank">📅 14:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443681">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🎥
عاصم منیر و شهباز شریف در سوئیس با هیئت آمریکایی دیدار کردند  @Farsna</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/farsna/443681" target="_blank">📅 14:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443680">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNbJUXx7nFGLfs-vSq59zOwsvkmIO-hXbnppaQ5E4OLWbHGxJdEIOX9qsnZWiVWLk1epYylTOiTUy_-E2xqvL2GkFZ-a3EFH0eHhfrWvHZE6549WEHn9UaKCFMsDbb3IcMxYDRtZyUW3I4i5T9joPcYciqRl7qjQNmSCJEkdb3Hxj0O4cX3ixsinIND-iSp9EvFHeEcNW5FI-GNcDtkEcPSvSSbmHEm8pLbtkQM4lYLnyOQuV2jF6_4NhzgcRSxZ3nnwCfL7s1RxGzQZvBalWX-0LTbkr99_otOxuwtWjSsCD0zyf7FK2YC78-c9gvYowkYAdiR3eg2TIKKppVJb2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر اقتصاد: صندوق ارزی برای بازسازی صنایع آسیب‌دیده تشکیل می‌شود
🔹
هفتۀ گذشته مجوز تأسیس یک صندوق ارزی در بانک مرکزی صادر شده است. این صندوق با جذب منابع ارزی مردم، منابع لازم برای بازسازی صنایع آسیب‌دیده در جنگ را تأمین و به این بخش اختصاص خواهد داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/farsna/443680" target="_blank">📅 14:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443679">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47c575507c.mp4?token=DHthYplAOjOu_27e2ciaQpLrTpRk7ew_ytDZZYMZb4xV6XSNEAM_Fo97Nbbi2vVX-WaVrzixmNH4ZMMRTHf7add3cgjtWzcePDqSMONNxyH4lZJqNb85wmFV-r52k__GXM8AJW_5sZZjcE86bCEi8o4J4TRSYZ-BegSxwzD_J8_itB7yndt27T7tAei0M_tSuz9Zs0wvtXXkG0OoTNnWhZCE3w-GIKADZoPq-jWxZMhbXRBNSS7Vs9rEFIaUj4bsAVYaM_ohwfvwEJy915ns5YesE-McvxhVPtHxpUDhnn132-o2wGa-Om9OkY97No1nCWpy121IQG9JuHnhlPOnqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47c575507c.mp4?token=DHthYplAOjOu_27e2ciaQpLrTpRk7ew_ytDZZYMZb4xV6XSNEAM_Fo97Nbbi2vVX-WaVrzixmNH4ZMMRTHf7add3cgjtWzcePDqSMONNxyH4lZJqNb85wmFV-r52k__GXM8AJW_5sZZjcE86bCEi8o4J4TRSYZ-BegSxwzD_J8_itB7yndt27T7tAei0M_tSuz9Zs0wvtXXkG0OoTNnWhZCE3w-GIKADZoPq-jWxZMhbXRBNSS7Vs9rEFIaUj4bsAVYaM_ohwfvwEJy915ns5YesE-McvxhVPtHxpUDhnn132-o2wGa-Om9OkY97No1nCWpy121IQG9JuHnhlPOnqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر اقتصاد: قرار است رقم کالابرگ افزایش پیدا کند اما فقط برای ۶ دهک پایین جامعه.  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/farsna/443679" target="_blank">📅 14:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443678">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1763a151c4.mp4?token=Dsvrj_sId-L6FY_cub_H3BVpoHouJm4Vh0ZFgBv5QdLpeUe4_58fgPf3lTxVrjYZYQ7o4dZJFhcL75vvnm1IFqi5-llS2NfK3X0F-UwYeFLRhvSrn8NfV1XT-uuc4B-pWs53UjW5WDVo2ME9ASO_4SJgmPIW-afKptTn2sbkM02x0DmhSNS5CYKz5Ai3yRb2l0Q2JcmewE3HU6f_h4G3n0OBpm9TaWAZMM9WUrElDJwtl1pjvaZqAlaEZF2sUUcdVSi0devyUX4u2dIphuSYWPIhjhFVSJts3Of6tU6ecuappYDDuWONwOvkxG4Uju6VKgG_A08Lth_P9X72ryxAow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1763a151c4.mp4?token=Dsvrj_sId-L6FY_cub_H3BVpoHouJm4Vh0ZFgBv5QdLpeUe4_58fgPf3lTxVrjYZYQ7o4dZJFhcL75vvnm1IFqi5-llS2NfK3X0F-UwYeFLRhvSrn8NfV1XT-uuc4B-pWs53UjW5WDVo2ME9ASO_4SJgmPIW-afKptTn2sbkM02x0DmhSNS5CYKz5Ai3yRb2l0Q2JcmewE3HU6f_h4G3n0OBpm9TaWAZMM9WUrElDJwtl1pjvaZqAlaEZF2sUUcdVSi0devyUX4u2dIphuSYWPIhjhFVSJts3Of6tU6ecuappYDDuWONwOvkxG4Uju6VKgG_A08Lth_P9X72ryxAow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور: مذاکراتی که آغاز شده، می‌تواند بستر بسیار مناسبی برای رونق اقتصادی، گشایش بازارها و حل مشکلات باشد
🔹
نخستین دستاورد این گفت‌وگوها آن است که دوباره می‌توانیم به منابع خود دسترسی پیدا کنیم و درباره نحوه استفاده از آنها تصمیم بگیریم.
🔹
منابع می‌تواند…</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/farsna/443678" target="_blank">📅 14:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443677">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVs_T0zKLA9_dVdOcvU4dyXKgmqosGYZlWznKsZRh0qGOlbhCKLTF9ym3aqY_S8BNGv8uhrD4up9e3wZ-wieN75IIE17_ky-30T_H-ptqsrcRQiQ3o4A-BIbbzwhTzoa27ni4bnDns0LKLdFLEgcvVfff04p8ON7AGU8AeqyGoGc_wxsitK8dI1ReppWvDXDaKtLrLFl7PZbAMr4VklWJYKUg1gfKp8eFJ-F01C3AGwE2joYCKa6Ytg_YiEt80Z69e4nWgmHaqVB1OyI_SQIO7VY97cqq59rhytTNK12r7N2-mOLXrIkG1y0sRZmFI1jezD1xrSiF8ovlTdtTANr7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۲۱۶ سلاح جنگی و شکاری در خوزستان
🔹
سخنگوی فراجا: در ۴۸ ساعت گذشته، ۶۶ قبضه انواع سلاح جنگی و ۱۵۰ سلاح شکاری، به‌همراه ۳۷۸۴ فشنگ مربوطه در خوزستان کشف شد.
عکس: مرضیه موسوی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/farsna/443677" target="_blank">📅 14:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443676">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e87a9a732c.mp4?token=WxmrBMeExARrBE68mHuOwhH-S1k2TbRwIEII22DnS9qCuKqv0liva-L1c-r8txhpd2D_ga1GDEQ3I_mk3PdUBEdeOAcpF4P-l6q6_X1Y-zelH5ZQFbbVZ4E01-cof5zv3zdm26DphIuDUByqhp-YjVqBaw4xfcIywBVPaUBeJg904x0iVjoW0L45mv23iJCFRWT6HQkO9jr5_PtSZ8dP7LhKC5s3vP6TDVQTJ6mL48shYdEr5DU9enEYGMXQeRL84-7EITJf_SvYlmIjHXY9epzlYidRF_DdYISPzCjvh_A_1SWoLbadDJ-Oyr2gfcLeUs31KF4HDGWrjc5trSZGnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e87a9a732c.mp4?token=WxmrBMeExARrBE68mHuOwhH-S1k2TbRwIEII22DnS9qCuKqv0liva-L1c-r8txhpd2D_ga1GDEQ3I_mk3PdUBEdeOAcpF4P-l6q6_X1Y-zelH5ZQFbbVZ4E01-cof5zv3zdm26DphIuDUByqhp-YjVqBaw4xfcIywBVPaUBeJg904x0iVjoW0L45mv23iJCFRWT6HQkO9jr5_PtSZ8dP7LhKC5s3vP6TDVQTJ6mL48shYdEr5DU9enEYGMXQeRL84-7EITJf_SvYlmIjHXY9epzlYidRF_DdYISPzCjvh_A_1SWoLbadDJ-Oyr2gfcLeUs31KF4HDGWrjc5trSZGnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تنها کشتی‌های ایرانی از تنگهٔ هرمز عبور می‌کنند
🔹
اچ‌اف‌ای، شرکت تحقیقاتی و تحلیلی در زمینهٔ سرمایه‌گذاری در بخش نفت و گاز می‌گوید، از روز گذشته تاکنون تنها کشتی‌هایی که به ایران می‌روند از تنگهٔ هرمز عبور کرده‌اند. @Farsna - Link</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/farsna/443676" target="_blank">📅 14:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443675">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17b1e0a760.mp4?token=v_3TJs8HrayAaMEz0R2FTBArcx4B-NC_d-5KmtJUN-LPycW80L4viNIIpV_ORnQ0PApCOJpwTfhyISnz4Uv5I_OfMQsuEg48TlG7nfBqnKID1Ij4rnK2kw_PRSxo9xCjzIegiwrEuyfBEvNBl1AP-pP12-j8DQIHxq6JHW7ZpbwP27iyK3rlhKDiAMBwAvtgbcxbR-EcfFRQAbLvJY5pfgqVaBTr9wKj2l-OltICD04dd-91YsqrAHLD1Db5pkOVYLtcWKV-rLo4BefKu_PAjVtbxIvVK0kSS1zxXgwcI9hmhsN5ioKb0okNS7ec8Q6NmGVUj1ht58uODrDeKxFnEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17b1e0a760.mp4?token=v_3TJs8HrayAaMEz0R2FTBArcx4B-NC_d-5KmtJUN-LPycW80L4viNIIpV_ORnQ0PApCOJpwTfhyISnz4Uv5I_OfMQsuEg48TlG7nfBqnKID1Ij4rnK2kw_PRSxo9xCjzIegiwrEuyfBEvNBl1AP-pP12-j8DQIHxq6JHW7ZpbwP27iyK3rlhKDiAMBwAvtgbcxbR-EcfFRQAbLvJY5pfgqVaBTr9wKj2l-OltICD04dd-91YsqrAHLD1Db5pkOVYLtcWKV-rLo4BefKu_PAjVtbxIvVK0kSS1zxXgwcI9hmhsN5ioKb0okNS7ec8Q6NmGVUj1ht58uODrDeKxFnEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
قالیباف در بدو ورود به سوئیس: کودکان مظلوم میناب و تمام شهدای ایران عزیز را هر لحظه ناظر اعمال و رفتار خود می‌دانم
🔹
خدا کند که شرمنده شهدای مظلوم و ملت ایران نباشم و روسفید به یارانم بپیوندم که برای دیدنشان لحظه‌شماری می‌کنم. @Farsna - Link</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/farsna/443675" target="_blank">📅 14:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443674">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jR4DnIZWjmKVtVV9T03PJNPNFadrTkxR2cdMCxBPS4LIIWhgRPPAQq5mkabcWuZ0Mp7DmruYj4huyWK7iygUgx3hQX1JtWRMMAXsBUOSfrKiyFs8UcIMaD2ftT9MaHYPimAK_nMEhjJlunmPM8Ej05fQVCektVz8Ebm3T0Uyy8ETdaBU9npI5CXBGvAPHcBIz6aoj3XUOYMyXWkaLBOaZfneudnbHBVZUERLeSwPS8G-f6z2pV3y3v46Z7U9DNRKrSbtfq2zc4_u-aZWMJIiSmOOPbKg0sfE-L84B3GAHMGNTXCoC1a07NCmxRxubZ3Kljdl5fbT2gXbQcXJPLHD-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
وزیر کشاورزی: افزایش مبلغ کالابرگ همچنان درحال بررسی است و اگر به نتیجه برسیم دولت اعلام می‌کند.  @Farsna</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/farsna/443674" target="_blank">📅 14:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443673">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPPz8ZLvuAmGlWxOdbbWeITbUL18yxFX0O0LhqhUcCHg5hkjxoUjAV1R8oYRC5-vx-NK_Dxd_rbp5gXI6sSF9olT87oeY5s4Tzj0lTYOTAr_Nchvc93aYQuaJwt_-xAJV_7RiYluNUeXQspn7THwUwTSP98-cmR2bLviXZC8Q_ppuwvRJVeJ8MW2K9g7u-of6UiEB7fOYhvA9Hz5PYCFmzZcqOmocvnMPuRUum4phutbRzaw5G0nWTxafgkq8oj4d4bfKKgYWis-MJeTp3jmW8Gm2isNB0xyFhUUZdoseywbPK444w-Ai5Y9Zg6BkTrR9o3ugPL3pu-ddjapHeTHjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز ۶۰ قطعه از پیکر دانش‌آموزان شهید میناب خاکسپاری نشده است
🔹
رئیس دادگستری هرمزگان: هنوز ۶۰ قطعه از پیکر شهدای دانش‌آموز میناب که در تفحص‌ها از محیط مدرسه و فضای پیرامون یافت شده، خاکسپاری نشده و باید شناسایی از طریق آزمایش دی‌ان‌ای روی آن‌ها انجام شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/443673" target="_blank">📅 14:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443672">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7w3_6uuGgeWWD2RwObMsMCtYyFSWn7YDC3SWBbJClbCsuUjv-oNmTJNOXYRPJHMS8foo5CmrEs5YgbCgmciPR_6sotZUGMGDUDAs_EdMnnzFXA-WcXn_tZ3gytCcxF9Yle3SgFGzfdgTSn1aAc3b93OyfYz5O3Q5Geht6dwOtRe5DfwMXDPYM7daykNaXzE2ygGGbvt_YqVebdABJbqIpRIum6ZoVg8wecqgCjyR8OsCE-_dN-1S6U9xrAwK73vuolrDehs5fhIG2vCyf0xBJmjptyKBDA2MSrAAlohkeq4SoxZ6xW5Rge0DN9DgK43tRgWS28dcUzU1A9ICkMcsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بختیاری‌زاده در استقلال ماندنی شد
⚽️
با نظر کمیته فنی و هیئت‌مدیره، سهراب بختیاری‌زاده در فصل آینده نیز به‌عنوان سرمربی تیم فوتبال استقلال به فعالیت خود ادامه خواهد داد.  @Farsna</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/farsna/443672" target="_blank">📅 14:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443665">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L2YTQxIZZTC-MIrVBw1kGLkokpTPGCQ88dkFowmsnD2DI9_0Roo4zPN_th_x3jasEimAE-DCKhZHwseWH3JHB97WUp4mopXdo5mQnxcyshqu3MpCPHJa4fFpPxSji3ZaUkYJKklCXynTZ0HpR3jI7FRfSHJuQupHBRe5WCzYyguHJkCQ-STsS25H7Q2jyakEbXs-52Yk9MA1tdYavrNc2b7zAXEaopa-0400385GCFF-yrNuS896_mMorV6qnY9qRdq_t4Yj75rDLWHr-jEtV6kpHtlB9Di6W-fwSGHn1Ng_44TXWVhX2A6EWVFU5d6XA2ArYe4YO4LjrEZ6fVbxMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uD3JQswTQGJi8aVtbtRQ4EBaaRu5o_VIRHJE7xsLs0WmaOrhcYrRnG8tz5bcWYhwu8JWLQOhugkQtuwi6ANfoaNG_N_rS3VaVcPZqkYXL-QvE6ojoA9LpFjbom4wveV5-Kt1Eh8o9cVdtm1S5Z2ODl0vO-o5ukiUd5h4q0h9ZtZ1LGkPJ_x8429O20hHONTxNoLqtolMdCdmBqhV-q-dbTabDCdknxGCsZZ3zNReiYNvdb5f9bNJANcq3FdDvVNByOMAcXu3BURV7k2eXHltXR0IqN7mDDhDHalisFrx1CB50r8ym3ln0FUIkzbN5bMPPBiCpzPgu5pBouLEcJg7Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IDw89EvyTpgr0eWpQI6G65AIB32kWMPgifXfgO_eZu5oqdHYjeDCXjLb6ylNixEO2QJbao8oiMD-H38pODZ33bzBNnUFtleuFZaN_fldgNVCUY7hMphuUjag7pd822wWJx-Wk9Jb9LuPWWzWffbLXLB-n7afp0KaZRH2S7nw9aOvBZycKJXWbDFk3vwIq4geixdqgdmfaiJli5TcCGADr_fBa_8IzTHxAp9-N0AY90M5O3P6aTjS8B-WmaCZbw-RnSwGi0tbr7s6a_GHdcEb5DoVgC2b7tPLcl_n9VfvDpWfGndkBbiiOGvkwI86LoEqmkgGu2S23bKdjyrr1hXgEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CWYdNxaJXKqVOUwSpiDOTQ5u309d3Pd5EJFh_OD0wP-MeOL7gSf_cswuwR8V0IGkF1X8UIFK9fKahQ4gqi40dwx5B8HE0fxFX8nuN3vqf3gUlAvfhETja_xXj_WtcVcNSWm8hDazmga-ZdjqhWMfE3irCl4yOgMoX6xcsBMFxitL04_M5mWAD2d_WxEnJZnDg2DRqB_MmlUid0CDHMKG9KVPq6F0YMqDouR0Vxq6Osb2MnNs2sN_opWd5M8v1qCsXsMeB8E8fS7ghvXIKfyKnuVyO9qmVTuzR7T4NFBUtoCCRf_gWuFJqp9pt5dXoaaZZZqCxUk6iQ62BST7gVTRzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sNUG1nZGYN_LiuOcpGZW3rAydz90tscW3Ibs7qrazMT4v3YnDGpydZqbPEXENZVwrDkYc3gUo_WnghuvYyD1sPcRRmmDnIdDduwjXzCHRnvebP-wjYsd0t8WDtrlxsU8a-9s0FFbQj-gAOd0z8JJgGFirytPEeee2M4N2_T3f_5_NG4Sh4tqj6yFbNrFVEBjyHQCBke9-5Wi2CEG6qX_jfcxXNXQaHqNHTG9ZbCYYgfG9g3L055zduOxVCYejlJwcL845o4J2ARVj4mpRfASyyLEN0wiuKovPNYlfRoL9O1zNeQmd9Vn6Fhkv9LuECsAOHNqhrYMe-1FNtTJaD-oRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MEEhIP7XnGRTO0Csfe3-pDFsDVCU8PHIZMvRzeuuZ2IMAxlBD8Dq80tkYZyH9I4a5rPSll10hgJZe6bZxf6-ywHrQKp8ABxmmIbxA9Nax0VaNFaEF0fRnIB2NBGzIWdI7F95Djy2IrEJTib2Ncp8nAzaqrum4JmZWGMSxmi7LzwMQ_hitjySMTKRWb8CBH00IaMS5LzUIr4uo2Hu7UNt3OiqR6eNAKZ9quhDuWbktoBV4z1Hnd3FF2tuDh6ImdXsPMKK7jJ4XHkV_OH3X0-RrYX2IksHKjFuIMma7sH54Iz7TUBtzjRtTxWtz-eUNsJ5wcMCvqWLaWlSkHFXKkWOxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DOaw-LBtfLb8yrEzcyx1CnMgmzLhibS7Qp1UghGIRWWV2GRbePXLpUXKJpV8E4NQ4zYcFjF1XJ106zgLehXjzr64nh7l4uEbt4IZRKV0tVE99j0GH3SEoVcC4SitYwbwtMIIDaVngfvgVgUvMdkudcp3FEUEYJ-R4FHvTMFQhGTeQIkUOe49y3q5ahxba_Ae0M0Zyw7GV1SvLHVcxhdpZJJydlA9lgw3hSddeM_GwLjhjj6Zr3FqaSMGx_0kDIjc7WpGF669tSibdDPhfHtnlQclQcDO0GoQVmBFPtAJ2ehlQoWCX3vp8cAYLWKfDguoegs505LSOBDrrlNgUrDHwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
سوگواره دانش‌آموزی «احلی من العسل» در شیراز
عکس:
احمدرضا مداح
@Farsna</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/farsna/443665" target="_blank">📅 14:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443664">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d8a877164.mp4?token=PUD3aqpK5AN-4Lke0MlNwzA3wDRXFj2rUMUZSUsnlJEyHt186GuYSaUMFWoqdosj_aC8sK76cpcb2OL0tu3vHP-aGJNYjXYU3fQTXSGOpNcH68KyW8ycV3HoN0VXhOY8oqFmbAnNdEWyQjlhoVjt4kWjYnIQ5hSgaD8ZeWrbzf-HG4NTQ97POFM_locPJBLxJ_jidp4eMPAj1dtjgZppW2lO1Z8DVGc0RMTjyQ21x4_adYjpOwqpMiecdQ9LZVB4z2sSBAm4MDgLc5F6FELhOExeTRPnBvkmoYWlILqidT3LWMG2SRXezDRnXzB_rsJjgTAx62C1VUyjarDE2KRvdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d8a877164.mp4?token=PUD3aqpK5AN-4Lke0MlNwzA3wDRXFj2rUMUZSUsnlJEyHt186GuYSaUMFWoqdosj_aC8sK76cpcb2OL0tu3vHP-aGJNYjXYU3fQTXSGOpNcH68KyW8ycV3HoN0VXhOY8oqFmbAnNdEWyQjlhoVjt4kWjYnIQ5hSgaD8ZeWrbzf-HG4NTQ97POFM_locPJBLxJ_jidp4eMPAj1dtjgZppW2lO1Z8DVGc0RMTjyQ21x4_adYjpOwqpMiecdQ9LZVB4z2sSBAm4MDgLc5F6FELhOExeTRPnBvkmoYWlILqidT3LWMG2SRXezDRnXzB_rsJjgTAx62C1VUyjarDE2KRvdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مخبر: هیچ‌کس حق عبور از خطوط قرمز رهبر انقلاب را ندارد
🔹
دستیار رهبر انقلاب: آمریکا در ۴۷ سال گذشته بدعهدی خود را ثابت کرده و جمهوری اسلامی نیز در برابر هر عهدشکنی، متقابلاً واکنش نشان خواهد داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/farsna/443664" target="_blank">📅 14:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443663">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">رئیس‌جمهور: مذاکراتی که آغاز شده، می‌تواند بستر بسیار مناسبی برای رونق اقتصادی، گشایش بازارها و حل مشکلات باشد
🔹
نخستین دستاورد این گفت‌وگوها آن است که دوباره می‌توانیم به منابع خود دسترسی پیدا کنیم و درباره نحوه استفاده از آنها تصمیم بگیریم.
🔹
منابع می‌تواند…</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/443663" target="_blank">📅 14:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443662">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWLDsAqTTycxfd26S0lCxUGFhqM6qfguA7nDOyUSO6TeukvW5Rc_1QPbLwD0GHamHPD1kiPnMv9JGfRLipbux7MAKUmTphwi_YFhQ7UeDmJOpacnGABKDXglXM3vq4keQVvt3kk-NvfUoaIZ5tdp83n95__5-ofi5YK2d6iLyfoarV8N6DtZV-t0aREzi1RprwB338YqN7FPfEadLNdaVCdXHnPYVuYGCcCp7NBfddD1Hng9v__JkmRXbbAc6BHwb1vPgT-_aUMCpU8BsXVxGDB5oUaA4UFzDjZCLg5bglgwIoiaJeYXbm52BMi6282kKPAU0DiXQYRzHYMcPr-TdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: قاعده تغییر کرده است
🔹
پیش از این می‌گفتند باید دربارۀ موشک‌های ایران نیز مذاکره شود؛ اما اکنون می‌گویند همان‌گونه که کشورهای دیگر موشک دارند، ایران نیز باید موشک بالستیک داشته باشد. قاعده تغییر کرده است.
🔹
اگر طرح‌ها و راهبردهایی را که نتانیاهو و…</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/443662" target="_blank">📅 14:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443661">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TFwqHF0McPAEWIS1mt3gXsEczbNgZxkeKaiFAH7Il3Ga5ysYd2offMI-KCB7VHS0_BGqvcFQT46gnJKet1AHCj_6a3UdcfSjqOduatR3Bb59_1MLzkSP4VQ_u5lQIad0snwHiqPu_38TU-FgmdRDGVRtihNbVhtg5lu5boHWwQ-z7tE7XGXoC3zMV8UbI8qBvJIz6OMxGvTQAJy5rjj0PlaDlVp3rCf_H0HWGRJIzpWts4d13FXG0V5dbSjCC3l3N3f_y1wMCcTH6TjYccdcOvTtWxxdYexlAKuouClREqG-AhYluf4zGGvExR7XbQaS7qBNH0kh8egxf6YAskJxzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: آنچه دربارهٔ تفاهم‌نامه نوشته شده، دستاورد یک کار جمعی است
🔹
در شورای‌عالی امنیت ملی تقریباً همۀ اعضا متفق بودند که این اتفاق باید رخ دهد و تنها یک نفر نظر متفاوت داشت که وجود یک نظر مخالف در یک مجموعه نیز ایرادی ندارد.
🔹
همراهی و اتفاق‌نظر موجود،…</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/443661" target="_blank">📅 13:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443660">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1783186ed.mp4?token=HGS0O5fEg40Q_OU77ndmtSE6x_MiJo4iJkSv0_RV4N_jW1eRgIwGoAymjhL3IhQIgupeZHSzjry6nzY5HiymGzoocsF6y5dJ0m1jr6DVVEPp7cJZ-3-p5tg8G9oGK48afdHoaeu0Ukjlx-AEdQe2r_OuoFEOnjw3w5YVvm2FVbJVnlQz_VbiNQldgeKKFsmcbnXbJ4X1UAuMY9a0rkGqvm-weCiTQRCho1yB8s3Y49YVlLgFyIoTA4yYOPfvX_FuoZoXBwj_K9XcTiUqf-Cj-Spbutvr_XV3XFcqy61v8HmppxbfgeYiPSbJ6LnG-7RkKnlJG6nLW7byan76r2k-ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1783186ed.mp4?token=HGS0O5fEg40Q_OU77ndmtSE6x_MiJo4iJkSv0_RV4N_jW1eRgIwGoAymjhL3IhQIgupeZHSzjry6nzY5HiymGzoocsF6y5dJ0m1jr6DVVEPp7cJZ-3-p5tg8G9oGK48afdHoaeu0Ukjlx-AEdQe2r_OuoFEOnjw3w5YVvm2FVbJVnlQz_VbiNQldgeKKFsmcbnXbJ4X1UAuMY9a0rkGqvm-weCiTQRCho1yB8s3Y49YVlLgFyIoTA4yYOPfvX_FuoZoXBwj_K9XcTiUqf-Cj-Spbutvr_XV3XFcqy61v8HmppxbfgeYiPSbJ6LnG-7RkKnlJG6nLW7byan76r2k-ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
سخنگوی هیئت مذاکره‌کننده: ایران مصمم است روند اجرای تعهدات طرف مقابل را با وسواس و جدیت پیگیری کند
🔹
نشست امروز برای پیگیری اجرای مفاد یادداشت تفاهم خاتمهٔ جنگ است. طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات توافق نهایی منوط به اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱…</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/farsna/443660" target="_blank">📅 13:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443659">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bq0pciNcn84SOin1g5HzF7gOMItInYuAC80A-z1GsUmNjk8eVeKJNQHg4etRZuoZNIfS2tldNuBKDAG_oVo6DpkLmuX_qaJTmdcYQEZab1_IiqOGXI411Mo4qgyn5W5MT4aypchRqAdVsTFvSvTi7xVhhIeA_PossoQBx6QyEg4kaQWrq7JUaiwplbxZJiCsX4z8pvzv2qHtleIH9nqMJrK8pY__CVJlG482fN_OYOyZ1sWCzN4znLlMFo94EPrWxjjsl8IpujBKEylwLic-O27YWF3tQmzd2he4RezcJC-59nH8RwDWiGz2wvqA5YnynVbuPgpT6dfAnNHSb9mB6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
رهبر انقلاب: بنده علی‌الاصول دربارهٔ تفاهم‌نامۀ رئیس‌جمهور ایران و آمریکا نظر دیگری داشتم
🔹
بنده علی‌الاصول [دربارهٔ تفاهم‌نامه] نظر دیگری داشتم ولی از باب تعهّدی که رئیس‌جمهور محترم به‌عنوان رئیس شورای عالی امنیّت ملّی از طرف خود و سایر اعضا در پاسداشت…</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/443659" target="_blank">📅 13:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443658">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6qn_1nE0CMUagTF6w9NlWIEATcFp5pczEmWzuqeRl_ZUGVfAUAd-ORX6bHiiE8cP2psFcaogXtAQw1ZFsg0cyMJG4guJqDYPZQC49xWjqDEWT1uU5CUKyZkzXrDqpvmmV3ZPo5_-r5h44CddL1bDPMzyHmieP7aMnI6pj9jHwx6cOkJyZ7x984m3RujxjN5_4SR2D8T6AZrTOtKIDd7EM4MaZSfQ547sAx_jqPukQsZxLJH7AtmHC6qcD3nsbkoEuK-M7tfZ0X48So0J91-lPVwW54l-ED2fu5gmvhukrL7c7w3U14Hx9y2YOZP5VDLiEXl5wCK6AjJjfRw4GRsFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: می‌توانم به برخی سخنان پاسخ دهم، اما وحدت برایم مهم‌تر است
🔹
می‌توانم به برخی سخنان پاسخ دهم یا مطالبی را علیه افراد مطرح کنم، اما وحدت برای من مهم‌تر از پاسخ دادن است؛ به‌همین دلیل سکوت می‌کنم تا وحدت باقی بماند و کشور با عزت و سربلندی به مسیر خود…</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/farsna/443658" target="_blank">📅 13:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443657">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRnFsydlABOsu--2czesfjTHt2sP-ihoT-u8zH8AgzR_CkWvFtRv5VqVWJ03tBX5wuzNTmaKVnNt_aMRnM59NISo6YRGqsQWCt2xdfnnM_IxSpYysV_-xVtT6U92h8ZQX0bjM_7X5ElN3-ZoKLTFekQcL3bs-tKDvMk039r4FoeLnH5wiDYUILXJW1WHk_2JmN7_y7gm49kEyyLO-lDOHrerNCjBedSG7xpe1fIrfIqPekRk6qaW_rt2hmFdkKzSmIF4lcGvo2Pd7zSBIqCVCCJEmtEtn8KSCat6z3iGKeojqijsoLUSVCP2jJhr-w1wiYU9E8cWUG46x3I4RPV1kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: می‌توانم به برخی سخنان پاسخ دهم، اما وحدت برایم مهم‌تر است
🔹
می‌توانم به برخی سخنان پاسخ دهم یا مطالبی را علیه افراد مطرح کنم، اما وحدت برای من مهم‌تر از پاسخ دادن است؛ به‌همین دلیل سکوت می‌کنم تا وحدت باقی بماند و کشور با عزت و سربلندی به مسیر خود ادامه دهد.
🔹
افرادی که بدون توجه به آثار سخنان خود هر مطلبی را بیان می‌کنند، باید بدانند که با چنین اقداماتی آب به آسیاب دشمن می‌ریزند. امروز کشور در دوره‌ای بسیار حساس قرار دارد و حفظ وحدت و انسجام بیش از هر زمان دیگری اهمیت دارد.
🔹
اگر قرار باشد بر اساس نیت‌ها و سخنان گروهی در کشور شقاق ایجاد کنیم، دیگر نیازی به اسرائیل و آمریکا نخواهد بود و با از دست دادن وحدت، خودمان کشور را نابود خواهیم کرد.
@Farsna</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/443657" target="_blank">📅 13:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443656">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMVYG_EboWVKbjfh28HpgO1fCKyY-BKDVrDeqKOSYYjqxAJOR39cCwZEJf7I_uAKOsj7JmCpsTMT5WSI_ayUCvourkWHbU_pxStW5Tuv6YTYmir0IKqAIIYn3CPO7V91CXtzIMTaxsELkgu3WATyyFyFBEoZADgcD0SXN56w1gcqSEyjNmsebMnvppSKZOVF0kKTrpZB_igxsZVjF3X39BPG0ncXJP1ci51uiCNoSTtLwIy8OmpvgGMdrRRrDfkFHZpz878FiaaYBDEHXSeHjjuM9GUrfW3zsONWp64o45i3XYpdDxdU02MNpug_v7C7Cnh4hRqCgfHLrYCWfQEsSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی تیم مذاکره‌کننده: برنامه‌ریزی ما برای گفت‌وگو تا امشب است و فکر نمی‌کنم بیشتر طول بکشد
🔹
بقایی: ما برای مطالبه‌گری و بیان موارد نقض تفاهم آمده‌ایم و در نشست عصر امروز بین میانجی‌ها و آمریکا هم این موارد مطرح خواهد شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/farsna/443656" target="_blank">📅 13:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443655">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYTWKAoWLJ4Ge5KMwvIJ8AkH5JRiYg0MjBMibnWBrahAFzgLfCmzooePDR0NjVP9rcBUFFAfV-Tnx4vvw1hZQUiRnbuWTxLGIFdT7XyKx9Vi6LBZlFjBEAIaZQJbP0syhlZ-9ANqga7wU0AgVHTW92QPHky0GEhRgBl9xnTPr8iFO-juS8PA0KujgpudJuoTgX8IHelP9-4KMOkVp648eVxn3ENdPBF8TD8Ei-lIRN0c2o30_jnPNPJYvzt4ubHLWqeZOF3lVHfLq6MkAmgGrfFxxM5g-tI_tNrmnKCn5dNI4QEQbVIMpP37O5PwVN_XN12yCkMdg5vtGLqjM6TAuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورسی در پایان معاملات امروز با کاهش ۳۴ هزار واحدی به ۵ میلیون و ۱۲۶ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/443655" target="_blank">📅 12:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443654">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqhpXxoczXhUnsBBavXQOLcQD8JESB56qMb2phHFA7tRbQGpxDoE0f9MVsthLhtFgbzL9QZZYl9TTJ_FR9kHX-mJRWbNELBpZLndlD-v-44Ue4mfs5Vh4Jb9_FqBUIM_jsZJcydq0c4UJEtdPm62SiP7gOymQkUkFRWEuJJGZ-8X7qbiUZ_o6luMS10qPCEd3omAjLimdPb-2_OGgYHfzwiLn5uGQpjb4sn7W50Gdh3h1-Zqpq6OoRfS6NoGeZxjAag4nma-h-BUkqUgt6m88gwUSWVxn916BEhAi7L_-YEcgWAAvPUXM5bjsTLMDa4PVStXOQEK6_mJehnd7sIfQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
منبع آگاه: خبر امضای مجدد توافق ایران و آمریکا صحت ندارد
🔹
منبع آگاه نزدیک به تیم مذاکره‌کننده: اخبار منتشرشده از سوی شبکه الجزیره درباره امضای مجدد توافق درست نیست.
🔹
برخلاف برخی ادعاهای مطرح‌شده در رسانه‌های خارجی، هیچ توافقی برای امضای مجدد در دستور…</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farsna/443654" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443653">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‌
🔴
منبع آگاه: خبر امضای مجدد توافق ایران و آمریکا صحت ندارد
🔹
منبع آگاه نزدیک به تیم مذاکره‌کننده: اخبار منتشرشده از سوی شبکه الجزیره درباره امضای مجدد توافق درست نیست.
🔹
برخلاف برخی ادعاهای مطرح‌شده در رسانه‌های خارجی، هیچ توافقی برای امضای مجدد در دستور کار قرار ندارد.
🔹
روند گفت‌وگوها در چارچوب‌های تعیین‌شده از جمله تحقق ماده ۱۳ و شروط رهبری ادامه دارد، اما اخبار منتشرشده درباره نهایی شدن یا امضای دوباره توافق، فاقد صحت بوده و مورد تأیید تیم مذاکره‌کننده نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/443653" target="_blank">📅 12:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443652">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb7022943a.mp4?token=DMPapRMA3JbqS0zQM9gPWRaz02r1zbPSn2QcP3bewdYfgCdEIjorBXK8l05XTVJ-CTcIWR3N2EyX2rwKck88TbD6naf9RAd5k9t3pDGyhIJ8fgndPMhRzz36aP9TzU8AOTB3tpRoUSbdf045G-k2cTC8V9aOE53TbhHLekQ5Kk8Z9X54HQDCPCskMJG79mcpUFelwvdJWqkFQDwM2Dh8lkLuJ1WZE-4eI2dmpcYrnitZ060npFwo9nWR2IXl-T_d4zF0KwolIFibcRkeqKnhcOIaF1I-Bbgi34DiwBGNvHROdtGeU0E3Nz7-qnVQ6SX9fubyfQi6rjtC8jTrvO8LpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb7022943a.mp4?token=DMPapRMA3JbqS0zQM9gPWRaz02r1zbPSn2QcP3bewdYfgCdEIjorBXK8l05XTVJ-CTcIWR3N2EyX2rwKck88TbD6naf9RAd5k9t3pDGyhIJ8fgndPMhRzz36aP9TzU8AOTB3tpRoUSbdf045G-k2cTC8V9aOE53TbhHLekQ5Kk8Z9X54HQDCPCskMJG79mcpUFelwvdJWqkFQDwM2Dh8lkLuJ1WZE-4eI2dmpcYrnitZ060npFwo9nWR2IXl-T_d4zF0KwolIFibcRkeqKnhcOIaF1I-Bbgi34DiwBGNvHROdtGeU0E3Nz7-qnVQ6SX9fubyfQi6rjtC8jTrvO8LpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ منبع نظامی: تنگۀ هرمز همچنان بسته است
🔹
پیگیری‌های خبرنگار فارس از منابع نظامی حاکی از آن است که تنگۀ هرمز همچنان بسته است و نیروی دریایی سپاه نیز تا اطلاع ثانوی هیچ‌گونه مجوزی برای عبور شناورها صادر نمی‌کند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/443652" target="_blank">📅 12:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443651">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQcAVCbsqLiT4xj30-RbkClu7DBbY82S9_co-yIb4zLdwawYWJOOdDXCUqIue3nG45gCtUTk2owRc5hfI4gK80aBPCGJSD3if_j1Kx6LW2F_REDvvkgvOsx2F8HHLv12WJnY-HkuvphoK7NscD-gWPXydy9IHEnfBYjUfXJo3d-SY1kV0KJhqOoWDSJwTl5oudqZA6qnDue-rlOmtD8CJ0UGBmi7JcdErDNJLNdEoBesKmkzALbFwV8mI3gx3XqOtJGutFuI3xKc0fBSsuksgUqQkdrZlV-3Vfc4GyfQwN4AAV53g6Lne93081QLGpjfCi-Y9qJ1wpaklMY9f1sCYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ رئیس سازمان بازرسی: تاکنون ۲۱۸ نفر از صادرکنندگان دارای بیش از ۵۰ میلیون یورو تعهد ارزی ایفانشده با مجموع تعهد حدود ۲۳ میلیارد یورو به دادسرای انقلاب تهران معرفی شده‌اند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/443651" target="_blank">📅 11:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443649">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLdd9upDJDUNdj7aAfuqo_ZwTkR8aI64hlBk32KPwkHDSuicoqawtkSc-d28YY3aWGSfK6MQF1S_--eEEzclI6o8zx08OWilAcgtFwCJGfSvDsIFD5YxhZFYz75Y5NBru-ZJzxkCTTtXgR61JDhtV85ba27J1FIHr4BjRpkYZ5POyRUHC5pyLPzW-VeLJTr-_mnYBkNeFDbMmGkOfA_-0EpClWuPXMIldZ1AnKAZp68wsSAwEMmaC5Kc2LPY8kWRZQt0tkuf_xnVFLwrbtfz3XvU-sHF_FGiv51S8ustg3RPe0N-iA2_jjMozBSkIxv7zXKCUkmufXSiqQqluXfmlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار قریشی: ارادۀ مردم ایران در مذاکرات باید اعمال شود
🔹
جانشین سازمان بسیج: دشمن همواره به‌دنبال تحمیل ارادۀ خود و تکرار سناریوی اشغال در کشورمان بوده، اما این‌بار با حضور هوشمندانۀ ملت و فرماندهی رهبری، نقشه‌های آنان نقش برآب شد.
🔹
دشمن به کودک مینابی و سالن ورزشی در ایران رحم نمی‌کند. دشمن خبیث ما می‌گوید ما به‌خاطر تفریح ناو دنا را مورد هدف قرار دادیم.
🔹
نباید اجازه داده شود تجربۀ تلخ برجام مجدداً تکرار شود و ملت ایران از دولت و تیم مذاکره‌کننده انتظار دارد با الگو قرار دادن شروط رهبری، منافع ملی را در اولویت قرار دهند و اجازه ندهند دشمن با حیله‌گری جدید، به اهداف شوم خود دست یابد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/443649" target="_blank">📅 11:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443648">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nV8MWKTEDswojlhcM5aSQf1QrNY_d4H7ZwNpg5VytY2gTG70rjM2x1pV4czz15kIu26oIOhLDF3n6jrXk8aKlWOLEfCLqjcKssCvIB2Fzkkjs_Q818-DWHJJUs0eCohCdGRkZfxPFE2tGGu5H9TgF3-DZHf2a-AvLSrLv6JDlrFSgsBrVdnyiwweGGXkl8cyi5w7UzlTKrnwvAzXv4hVC79iHb56uUl37gxNOzOx7Gc8bRMejRAYvK-_BTZ-W8W85zs5xnWtrHovEcriBkwPzk4mQ8xwLUebI5O-J6lxCYoLENTHfIjaz5xKNASQpgZc3bjUmwHduhFa1GJ4oLodMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنگۀ هرمز ۳۰۰ میلیون دلار هزینه به غول کشتیرانی فرانسه تحمیل کرد
🔹
مدیرعامل شرکت کشتیرانی فرانسوی CMA CGM : اختلال در تردد از مسیر تنگه هرمز، حدود ۳۰۰ میلیون دلار هزینه اضافی در نیمۀ نخست سال به این شرکت تحمیل کرده است.
🔹
بازگشت سریع به شرایط عادی در تنگه هرمز قابل برنامه‌ریزی نیست و اتکا به بازگشایی کامل این آبراه، «غیرعاقلانه» خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/443648" target="_blank">📅 11:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443647">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">رئیس سازمان بازرسی: هفتهٔ آینده پایان دورهٔ ۵ ساله مدیریت قوه‌قضائیه است
🔹
خدائیان: گزارش‌ها و دستاوردهای این دوره از طرف مسئولان ارائه خواهد شد. براساس ارزیابی‌های انجام‌شده از سوی معاونت اول قوه‌قضائیه تاکنون بیش از ۶۰ درصد از برنامه‌های سند تحول و تعالی…</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/443647" target="_blank">📅 11:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443646">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUGRmJdeTR1yoTYR7m-vAwXWXngjum-DfRJr_hLSVpWHo3kU3krvtGkahYIZYUsmEfsmemwK1BrNPYmF6HSZFbGSw6EiXAJIlzfAyeHhC1XXSnkjZY2NseLvjFLmW1ng3D4ra12nYj7Prpjffwsodh7eVH59FCSqyopJ4XOG5f8YGr8Gg6j8BbvmCDDzNVOtcjTePbfI3z2tQEuWaqdP5z_Bj2CDd54gjBo99XdpsiaT6htj8Yb6mqhiWsM-_1FR4nJOaNqcsKDRjtAM8YwmC9ZI814ttsPz8n87ltTseWdQCLBg4ks2OhBpJpnq3A6-_WHQr_gEW31Hlw1YtYk2yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار عراقچی و همتای سوئیسی در بورگن‌اشتوک
🔹
وزیر خارجهٔ ایران در سوئیس با ایگنازیو کاسیس دیدار کرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/443646" target="_blank">📅 11:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443645">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
تنگۀ هرمز بسته شد
🔹
قرارگاه خاتم‌الانبیا: نظر به بدعهدی‌ و پیمان‌شکنی آشکار آمریکا نسبت به عدم اجرای بند اول تفاهم‌نامه پایان جنگ، و در واکنش به نقض بی‌وقفه و مستمر آتش‌بس توسط رژیم صهیونیستی در جنوب لبنان و کشتار بی‌رحمانه و آوارگی صدها هزار نفر از مردم…</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/443645" target="_blank">📅 11:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443644">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUzT76pRpn7lO5AXDE359Q6pUflwq7DZOjkEwBR0pQQ0yhGnwRCbc_FiXzBTqzlqz8kmbFQI4M0BDOupJV3gf6R92Tj314wXzvx_VOT5HWP2ono682P1L4XiD7OAVtehXbZK8fzbv-fJ5h01v_QFPMOE4EItWkluhnQ8x_V9YDM4K1MUX4913786cY81Jj8eGsc8HCRuQgjTtxxqy3j3-_2qNJR67EWZmn_YomJxxeTMT-w18_YOdWe2g_Jr0HAN8hMwOiQcZE58sTmutw2ans8mqhIeL666F1qNYJb5It7Pn69NyiPFkUXesj23sLZpjj3OEPey4hrpyuDTb-0gvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انهدام باند ۱۰ نفرهٔ آدم‌ربایی در پایتخت
🔹
پلیس آگاهی تهران بزرگ: یک باند ۱۰ نفرهٔ آدم‌ربایی مسلحانه که با معرفی خود به‌عنوان مأمور، اتباع افغانستانی را ربوده و در ازای آزادی آنان درخواست مبالغ کلان می‌کردند، دستگیر شدند.
عکس: امین جلالی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/443644" target="_blank">📅 11:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443643">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c574ef04d4.mp4?token=o0x8OLaCSp0EQ0N0e0VtPzkmHRE3tFmkHEGPSy8Va6ggSD6o_P2h_0r-3VA1uKXtub049ylbrCrAYK41DD4-NPrXEK-LMqzGV4EKqwhRrsLjP0cVNhzY0c-GO3fqVzhW-IUeIn-knd12GiitXElLOQSm9rX2F4ch_M0c2x3PQc0kaUmYXXQt4HgZD9eIJkYcr5MNscZs_lzVrjZ4NK-oGKEnddLgY2eNKmZ7I0bwh_CveZAuuCsCGyKOBTJlW0VvWHsZZVxENxgjppdHpKbX10acLNigBfRju5MPEnZU6yDRTQdS4VvgOnWfSGFm9LsoPevgQOB6Lz9VaZCR31IDgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c574ef04d4.mp4?token=o0x8OLaCSp0EQ0N0e0VtPzkmHRE3tFmkHEGPSy8Va6ggSD6o_P2h_0r-3VA1uKXtub049ylbrCrAYK41DD4-NPrXEK-LMqzGV4EKqwhRrsLjP0cVNhzY0c-GO3fqVzhW-IUeIn-knd12GiitXElLOQSm9rX2F4ch_M0c2x3PQc0kaUmYXXQt4HgZD9eIJkYcr5MNscZs_lzVrjZ4NK-oGKEnddLgY2eNKmZ7I0bwh_CveZAuuCsCGyKOBTJlW0VvWHsZZVxENxgjppdHpKbX10acLNigBfRju5MPEnZU6yDRTQdS4VvgOnWfSGFm9LsoPevgQOB6Lz9VaZCR31IDgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جانبازی که بدون دست، میدان‌دار شب ششم محرم شد
🔹
حسین محمدی، جانباز دفاع مقدس جنگ تحمیلی اخیر که در دوران جنگ در پای لانچر دست و پای خود را از دست داد، در میان عزاداران حضور یافت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/443643" target="_blank">📅 11:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443641">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a4ee7ad85.mp4?token=cweCVMnSOYUfk-mdfMNI6C1d1L-bSQ0ht2YUeIu433Ve_dSXUJVQWgvWHbilFfSAhrEMj6oDb8CVPrYzSLBkEkf61wiQI8X_XMPgR0MhpInuY5A3s0j8FMTPjPWFbID0k3adnqqNCOpEfuWkbSgd1Zhp1HlmK_Rkswb2im4bacOsz_EJKPOzMKlb8uUe7hF4mgFE5tGbNlzmwwPWLAZsoo5hOer5JPFMzumgi3I8bXM0-cQ5nokXmdgW7-1rkFikX74OnPv0TwT6tyBYD-hWS8IURDf2I3hzjHHaBEKl4VM9H_nhsmWbZUhQnq9ZQiEJfPVOLJgZsTlXbxX5sn-faIV7qig4IjPzpuR2ZMPWPhCybn6ybp70uaRTBWfyeYDrtqQdcZppXwPHRUrzuJj6NG0YOgKjQ15TunU5_blwntueAQDHiBJ829BemO8rnb5bymhj7CEMebCWLkDHK6LsfY-6BjiFKG2oIknSqfvUmtWGi1AFm-BhM2D_eMeocEwH7N8q7dB00vlzY7kWyzrCrNk5M2XZF8LeKEeRLZ3vI25XCdlZWuAtoSbn5pUdimJEVnROeyWOnUgQsrRRubMvktRKCfJjhx7jfJcxQ99nvFqIKLUqGecehcD8QmN_0CpqKd09XBQ8znZzwPqkynlzUlQ3RbbUL09931aMjLlFUi8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a4ee7ad85.mp4?token=cweCVMnSOYUfk-mdfMNI6C1d1L-bSQ0ht2YUeIu433Ve_dSXUJVQWgvWHbilFfSAhrEMj6oDb8CVPrYzSLBkEkf61wiQI8X_XMPgR0MhpInuY5A3s0j8FMTPjPWFbID0k3adnqqNCOpEfuWkbSgd1Zhp1HlmK_Rkswb2im4bacOsz_EJKPOzMKlb8uUe7hF4mgFE5tGbNlzmwwPWLAZsoo5hOer5JPFMzumgi3I8bXM0-cQ5nokXmdgW7-1rkFikX74OnPv0TwT6tyBYD-hWS8IURDf2I3hzjHHaBEKl4VM9H_nhsmWbZUhQnq9ZQiEJfPVOLJgZsTlXbxX5sn-faIV7qig4IjPzpuR2ZMPWPhCybn6ybp70uaRTBWfyeYDrtqQdcZppXwPHRUrzuJj6NG0YOgKjQ15TunU5_blwntueAQDHiBJ829BemO8rnb5bymhj7CEMebCWLkDHK6LsfY-6BjiFKG2oIknSqfvUmtWGi1AFm-BhM2D_eMeocEwH7N8q7dB00vlzY7kWyzrCrNk5M2XZF8LeKEeRLZ3vI25XCdlZWuAtoSbn5pUdimJEVnROeyWOnUgQsrRRubMvktRKCfJjhx7jfJcxQ99nvFqIKLUqGecehcD8QmN_0CpqKd09XBQ8znZzwPqkynlzUlQ3RbbUL09931aMjLlFUi8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عاقبت دردناک وطن‌فروشی
🔹
علی‌نژاد: به هیچ‌جا نمی‌رسیم و پیروز نمی‌شویم. خسته و زخمی‌ام.
🔹
سلطنت‌طلب‌ها به قتل تهدیدم می‌کنند. اپوزیسیون هزار شقه هست و خارجی‌ها مثل لکۀ ننگ با ما برخورد می‌کنند.
🔹
آماده‌ام برای آمریکا جانم را فدا کنم. در تاریخ به ما می‌خندند!
@Fars_plus</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/443641" target="_blank">📅 11:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443634">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uv2TJcVnHobWiWgAFvPbuf-QEd2iNfOZdPtwVMUnn2qkhcqjmYj0ptWEE-SdEu4A8xsey2DGp8JVnyE9EiVm99lYy0f9YEWW7-aLwD2eVR7PMvEOioW6Qkgc1HK9UbfWBSYrQT7UeV9kHaC8LMt9eWsiF-ySIRMq22ZcxrZsqBIbwfLC5Gena-ovhlaQVZIuBdtNfDEH6RGJ6nZwidTw36kHbcOISobxaAwxnB6HF2dJR6ankUnfKBD3Gyrckb_hag2z-X6AGttP7X8gXVEDVyTQ4AtJc2OOI7vzmyPWOUNhfSAMKi4e16TJjd4MKRWkcFjqP5zjVfEv9SAYtP_p3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mXt6iDmrFINovosNqUR8PYKNf8sSPZH_BJ6n58derI7DBCvunolhhg7pg_Vu8WP4UqgwrHGbIEtGY8v5yjS0kj5u10qEU59SPxliDO4OsDeiMb5YqiVUnJ2y3f807qeKhIrf3Z6uku1TjMCAYhAtBy1uK7RJ8SaQj0sS71dXupxDAEPU4Iona0fTwBg10NZ0eReV6h5o0aD70iHgesoZgxG3T4VRmN_OrpTrBwkIO8PWJWNEyTsA0a316m2hdqz-BvZdvrUuprqXRO3F12Sx9WUhOrY629m9W5DKny0MtxoCdk2iPqPAQcWwgp4OzHpFoCANqB8b0NPMvkgl08ofyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CgB8TZESZ28kec3UGEAvNFOHi7Q3kk7JmdOzLc0_n3QolwBHDXDksAe4AZyffaGujqMkG_LG0qtgUePNMQRuzk9wvkrZ3o61ReNFRSTK703carZjy1-5m8nP5i7V3fdizVJpsUFkQZU9bQQt6V8TiVTKkLt2fFjyMnwVL4vEWeb64gOxxLW8tBbCRaasag_dniaWdi1hWnv6V1KHmLHtavAkhYM6pfWoXZRPt4oB6eXAEqbqfBBvbWNCZ9XGlkJugWcm4GDQc_kuee394XYIXOohiqTO266vBCJiM_BPV-0wQqQGMwOAcsjAn-iwEsp6tCCKbqvD2l_aow5WmYUNAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gpgotZB8y9AKAQEbfN6LPMkt-m6OlNDq8eqi6hibySkCqQmb4_85iHDDRg8NtStza-PCGSaJTGpiIskM2pc2FDWwHI_XHjVXRPt_c9M_bDI7mXTa4ALfPtb4hCtoGSKDEP7p6_tKb98dmPDMj9P-_LfKWqOvOKtbXQf45zleL9Ho_A6Hqqviqrmx27J7taEG1_If8vVR59otPDD_hkyaKCykpH7A13g8LwRNlpbLQYcPRY_D_SMHNROPqSQOlrxgVFbjgORyQkZvAfT2MIZ109UZ2rnV1UOwqFf0QuKpdN9osGx9A-V9YVVIpWoVjXKr9KtiVqYEQkO5zAqd5eGs-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bWIKgIuVBdRqwdrAzLKYDqOLUogbM2Mr3YEm2Ks_JfPLu6AzAv03eBeecU6BOSVeGOyPusP2ppcILbsQSsiuw6ZXekF9MXVxdTjno11jJIPcj1WY1ofZ1BmPFa6ecXWEh7JY5j2EUZ92suis6ylLbwwBH2w_yOEU6ivtWdV-nPz9GX-1Uj_7At-LvhZeRL2bI7RmsOn99yGR05rW4zzTo7M6aZs4lDG_wnmO9I5PUplfRqGtpdhay28xDJ0Raa85adAqBVPFeMBiOf3cvEpGBFZXuLlpyenwhsSEsBvgHs_e-tFDWbJbM48Jt2hfEto2ieJ-opPkKFN1ADMOL0NtqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BfccwFmtn75Dinkj2BCmfLe-pDyHUJG43bFLw3Aq0k_l5CoiZFauUgECj_MfE4VkBhnuclVg7teDAlRoDr7aHTYEK-C0iMiCGyDsDoclCTuxpzVe7xwnux4Ov1dTEnYF3jXBSTOBfrtiFfG0B7648JbYI_ZtAuPuQ97NtsFLMjNixrMzenwEXB9lRg7zD9eLAik4YvbTYrNE8eXf8DN7313pateQoogvNPwgujDkNYoBM-3Z4jOUQ7k1LZ-5aLV098C6vO5g36-QlWpsjiyjoF1YbiDkYjh7CrG0W3c-tQbaIR75Q2faUyyzhV3h0cUj83EV_jFg58o4cXpC8Khskw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GSwNZg_LtgOesvvhe7u30zc0A0ujaDvLMqWAHNbbKU_wOgTaMAyPi-KAzeDMhdulmjA13k80KfMAzV6D83M3RxRazF_vmR8sKF17yUSAFZOWrc2y-6FBvRbJx-B9icBrwMHZb9riCgkzG9sZkQauyqHQRS657WE1KTXpBiATpZ175YILSIAQvdK7cUfmTj90kAnTpiD9rxr1lK4faqbE-MUrNWfFi6wXdZo2XmxSLxwA6JTlRUDYBvT3Va6NGQo0FVHfP_QC-WczNpW5WfzFP3OtxNRhLYHoc3aevFKbyoIoSA_QIMVOQ4r1-a5X6kXUy-MZB0WuBkEoKFGNB4PEEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم عزاداری شب حضرت قاسم(ع) در آستان مقدس امامزاده صالح تجریش
عکس:
محمدحسن اصلانی
@farsimages</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/443634" target="_blank">📅 11:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443633">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUc3ORTIfOsEQw2nDBktR9I3Jz6sdFmEGvcYNNra5KSOfQhfsUafDoqUTCWefupjmYXlfkrE9NZOJwye-fNdswj4ufk2oWrSS1iHKV-OqgMxzTB5cKHNDv6PexDg5nqSlSXHUScI4C2xNJ8Cvvsg77V-w0gqzEVcSYpcwkmn8XnJ5H_E42p0IhPnKAJbN6Ve_5WHvzNoxUNV00gqmNrWYqGnx6Zln_mQRQQzWcTaAJC_oyPt1C76JGcQDjFjYxQdTONYjmiQxPKovlMWIRClEFNWkdCzf9m1NvMf7PlnQ-RQJTwwisR4ck9NfviJ3ZvAwCpSFe1M-KC4YBW6C2hRow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان بازرسی: هفتهٔ آینده پایان دورهٔ ۵ ساله مدیریت قوه‌قضائیه است
🔹
خدائیان: گزارش‌ها و دستاوردهای این دوره از طرف مسئولان ارائه خواهد شد. براساس ارزیابی‌های انجام‌شده از سوی معاونت اول قوه‌قضائیه تاکنون بیش از ۶۰ درصد از برنامه‌های سند تحول و تعالی اجرا شده است.
🔹
در ۵ سال گذشته بیش از ۲۳ هزار هشدار به مدیران و مسئولان ذی‌ربط صادر شده که نتایج آن در پیشگیری از وقوع جرائم، تخلفات و سوءجریان‌های اداری مؤثر بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/443633" target="_blank">📅 10:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443632">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tp1ED4B2J5NdJ_Ao4F3DRKKm00mcW34WLOiJZe7ZeO_P3ok_fiK28ilzbcdui_JErzTPz5bFnLAS6O3mabl3QAqG8Sjm0Q8z1MhVH4RlI5mX9HRdoO5vFxor_a0GxBRpUVdFHFZNRRIVBpEwEqCQ2VWtAbgCqp7-TjFF5w0JWmnV8Kq0V14g1AEQ0cJZH4mEc2Wzc52L7QSh2ubpaBZxpd2qDBaaS0ut5MoRZaJogjcRV5VMzK5NXfUw7nDjyiwNZc7a7OgERgzA5PuoCVP4gKrXSTBziM_mUP4tgYeGU-7VR12NcW86QI-m1cmUcQ69bDN__msdO6nmMlWPTjEx1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
پاراگوئه اشک بازیکنان ترکیه را درآورد
⚽️
ترکیه در دومین بازی خود از گروه D به مصاف پاراگوئه رفت که بازی را ۱ بر ۰ واگذار کرد تا بلندپروازی ترک‌ها با ستارگانش خیلی زود به خط پایان برسد.
⚽️
باتوجه به اینکه ترکیه دیدار اول خود را به استرالیا باخته بود و با…</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/443632" target="_blank">📅 10:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443631">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0KdSv0xUs6L71Qhmk1QhjuwUE5j3Qjo3v2REbNHH9NolCKVcgnHr208-c51k3dy1Qa-o4DiWE8XblYU27a6z1RmZpQVwHLnRFgA-75W_Zsu0fP7SKWpeWXw24Sga44HSLo1xaRGpy7NL9W8HHv10Jhkp3ZxReaTViWaA_zzzRUHYPBrkWvY8ggjPrHx_lRmom6Rtui9GbqNCI8tPTH1AzkO8zGRDVLAym1Iwui4BicjVnYr3frAHah5sxAdxGh7cu50bRKNdkPsD1S9TPTmTRPg1tRxqYbl_v4dD0uuZsTzdIBriB1ipqeba9OnVoBKamcY1TQVl9ZDLHMbiQVD7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندار شهرستان مهران: از ابتدای ماه محرم تاکنون بیش از ۸۰ هزار زائر از مرز مهران تردد کرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/443631" target="_blank">📅 10:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443630">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLu8JhHSeKKe02IJFp0_EvP2Y3022slVxZF-rWv52Vf1rzktWq1mFt_A3motgmyg2738f5VGBR-z3ia35H3Zx4ldeAgnIcrLGcbB2N_dkcZVGZa360FGQ8qLQRlCI95JrJx9e9mbwTEznQ-IY_XxkBgF_jW5HQg_ErPH7d2FVaKDsUFr0i-hzLf2Z6V0o7hu1tL1Emt9YKDu4PifjOuvRkOPGvf96mJAQyDoG5nmwKhffe3ntLZpKGTFrdTJS--cZNwvd9sKCI35LGirXX_KSZ9FiUwAPnU4fUtbvPMLCDZ3cmC9U63vc19CAzoKaVnUpCpr_D8RDzOzr3HFBrNgbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هاآرتص: ۳۶ افسر و نظامی اسرائیلی از آغاز جنگ با حزب‌الله در حدود ۳ ماه گذشته کشته شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/443630" target="_blank">📅 10:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443629">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">آغاز ثبت‌نام زائران اربعین از ۹ تیر
🔹
ستاد مرکزی اربعین: ثبت‌نام زائران اربعین از سه‌شنبه ۹ تیر همزمان با نیمۀ محرم آغاز می‌شود.
🔹
نام‌نویسی همۀ متقاضیان تشرف زیارت اربعین در سامانۀ سماح، و داشتن گذرنامه با حداقل ۶ ماه اعتبار الزامی است. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/443629" target="_blank">📅 09:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443628">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TiMIqmzYlFQui4QyFCWxs_ViB0vv4ItQNy9TRYMfXk7FcYDCaqi1Iu7OSJMF-JMYzIuGbFzgW8J8FZlbwQfg2kAIP60-9cWuIBbo_7MXjX44oB7LeoX_WSdege49tiqyKdmJLhnzhK8MNpj5r_VoSYwiscZV6MleHNzvHkhph9qAE7eWaAXFb_RuJ5jP7x_3QN4OLiSZFlhg6adUZty4yknGPRQJcg8iId2S5CfKoSq-jJvLQeG8gN_S3wjfGFUXI9_J1n6JEPlmfbwQ7GGfItd8ZgeiH8nDs5e-IprUv1aoF8MsEDAGPBKMGLxKMZ1jw5mXS8eO8TkcvHjcFko2sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سرلشکر رضایی: هرگونه خوش‌بینی مورد سوء‌استفادهٔ دشمن قرار می‌گیرد
🔹
آمریکا قرار بود با راهبرد «صلح از طریق قدرت» ایران را وادار به تسلیم کند؛ حالا که شکست خوردند، از سر استیصال اصرار به مذاکره دارند.
🔹
اما دشمن نشان داده که عهدشکن است. باید مراقب بود؛ هرگونه خوش‌بینی مورد سوءاستفادهٔ دشمن قرار می‌گیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/443628" target="_blank">📅 09:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443627">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در دزفول
🔹
فرمانداری ویژه دزفول: بر اثر امحای مهمات از ساعت ۱۰ تا ۱۴ امروز، احتمال شنیده‌شدن صدای انفجار در خارج از محدودهٔ این شهرستان وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/443627" target="_blank">📅 09:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443626">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/525dddf3d3.mp4?token=tEXBOsx9OeqwEHi7uyeKbsh5wfKzpm_7OOR6Y3uA8XkD5gWhYCSaKFcfmJAXk7bT8DD1wlCz9hQf4Nt6I3RtUWhvYb8s2q6as5DHlVCV4QUCLzYm9NP5PoyNyhcquJ8USIULKFo-vmPGn1Oea4eMImujCwMHnjqhv129Ocz0BZ-1GBby5sEoJbZ7h89lNCFXIX8xdmnEo_WAg6gfGG16X6HERLDQwnyVVT_BQIu6ChAVoC0bknKv_uM2-qM-iZIx0cINRHU5oguKY9pqxGNGx2CY2f8RGFJKcu2l33VEl1d3KKrPtrW_GY5ufzjsFDVyLRV4g_7yCFSYYPTkKFBE6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/525dddf3d3.mp4?token=tEXBOsx9OeqwEHi7uyeKbsh5wfKzpm_7OOR6Y3uA8XkD5gWhYCSaKFcfmJAXk7bT8DD1wlCz9hQf4Nt6I3RtUWhvYb8s2q6as5DHlVCV4QUCLzYm9NP5PoyNyhcquJ8USIULKFo-vmPGn1Oea4eMImujCwMHnjqhv129Ocz0BZ-1GBby5sEoJbZ7h89lNCFXIX8xdmnEo_WAg6gfGG16X6HERLDQwnyVVT_BQIu6ChAVoC0bknKv_uM2-qM-iZIx0cINRHU5oguKY9pqxGNGx2CY2f8RGFJKcu2l33VEl1d3KKrPtrW_GY5ufzjsFDVyLRV4g_7yCFSYYPTkKFBE6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل سوم ژاپن به تونس توسط ایتو
⚽️
ژاپن ۳ - ۰ تونس @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/443626" target="_blank">📅 09:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443625">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKX75PgpUdVLbNYB6XALJ49103hG31vi79zMDrsxUv5XmSx99cyx-5pepVD-VBLHLu7c85fqjwKkn20zmQHqn398RR8KSY2lcVxNVlIuO80pnSgAMzvPm7Nj8piTfY_WDgCV5eGExzm70b0vbtGi9zag13mvMGSDl4yOSb19Nn3pLWDKAVexcBTBenQNs_lRME5UOQ2paNY1_JarXlPBHUVduPgsRRxI35nG8RCBQa5cYOGvJfI5hkn2VniYWM7LXb9mZcYVCxgxQmQp0PiMkwA51opKMD2msHo8HDqvFHJGWnNXxTvugXvAGbZudkmxFc-l_-z8qPR-bsKlp4MvKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
تقابل یوزها با شیاطین سرخ
⚽️
پوستر فدراسیون فوتبال ایران برای بازی امشب ایران و بلژیک
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/443625" target="_blank">📅 09:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443624">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5d235dca4.mp4?token=EpnOy5dM1aJF0dzqJur3l1H5d2lMAQ8xHjE8QndzEqgLmte-VpoeNMhbYlGy4S77dgoelt72HC6ihGOUIHrEPTC4aD83GBUEo4UxxTU-nIkD1IQpC-La7yzqsZRV30gsNEGCxfQQeKtZAil43B46tFO96eCMp7wfjfrNg8PIBLU1QG8zhXxDf29YCl_1RetQEOuF9KgjnlB_jkvrT9lDw8QDXudJlo8e0lMY9TO_Xm5KtuxkQ5YBjFk67XY-CN7Xl6h3Wu8CEdPF-EMByg3qSfmyHQPS48jb-nbRPtAgyzUK-GQHSR7hALJcJfTgtXUYS91uRO8a75M4ueaLNs3fYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5d235dca4.mp4?token=EpnOy5dM1aJF0dzqJur3l1H5d2lMAQ8xHjE8QndzEqgLmte-VpoeNMhbYlGy4S77dgoelt72HC6ihGOUIHrEPTC4aD83GBUEo4UxxTU-nIkD1IQpC-La7yzqsZRV30gsNEGCxfQQeKtZAil43B46tFO96eCMp7wfjfrNg8PIBLU1QG8zhXxDf29YCl_1RetQEOuF9KgjnlB_jkvrT9lDw8QDXudJlo8e0lMY9TO_Xm5KtuxkQ5YBjFk67XY-CN7Xl6h3Wu8CEdPF-EMByg3qSfmyHQPS48jb-nbRPtAgyzUK-GQHSR7hALJcJfTgtXUYS91uRO8a75M4ueaLNs3fYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
با شوتی دیدنی، آیاسه گل دوم ژاپن را به ثمر رساند
⚽️
ژاپن ۲ - ۰ تونس @Farsna</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farsna/443624" target="_blank">📅 09:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443621">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfd89da9cd.mp4?token=IOjh3SGgYp46TxfT9SvZJFdhXpjb7v3HdnnfPKwtjhntJYxRTkGUUGhwPlGcqL_dgru7zerWE-cGBK7Jfijow4lvMIbbv1LNUHPxLDH0huF0LkOkCBQpaAJOi9f81qG_kGuL0hZaD68XjmB9P7f-CSu21Dp2C-fCXAH19Hv3x7ScFfWAUfeQkp3Vz3dvQMI-WmUaZL1n3HE0HTJAGAX94C3UibqMGlnZT4z6oVHsXHnTF2b_cYRg6l2A6LOVXxfxl0dj8RG3OCvO0rQeuaNFiHcrmjTSUS-STfWpsZQZUvmtzyjcpTiSYayWyhQXsnLYtUEae_V_k1Q4mlguI5HQgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfd89da9cd.mp4?token=IOjh3SGgYp46TxfT9SvZJFdhXpjb7v3HdnnfPKwtjhntJYxRTkGUUGhwPlGcqL_dgru7zerWE-cGBK7Jfijow4lvMIbbv1LNUHPxLDH0huF0LkOkCBQpaAJOi9f81qG_kGuL0hZaD68XjmB9P7f-CSu21Dp2C-fCXAH19Hv3x7ScFfWAUfeQkp3Vz3dvQMI-WmUaZL1n3HE0HTJAGAX94C3UibqMGlnZT4z6oVHsXHnTF2b_cYRg6l2A6LOVXxfxl0dj8RG3OCvO0rQeuaNFiHcrmjTSUS-STfWpsZQZUvmtzyjcpTiSYayWyhQXsnLYtUEae_V_k1Q4mlguI5HQgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
باران‌های سیل‌آسا در چین
🔹
بارش‌های شدید و کم‌سابقه در شهر ووهان چین موجب وقوع سیلاب گسترده، اختلال در تردد و گرفتار شدن شماری از ساکنان و خودروها در مناطق مختلف این شهر شد.
🔹
براساس گزارش‌ها، ووهان تنها طی ۱۰ ساعت حدود ۲۲۰ میلی‌متر بارندگی را تجربه کرد.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/443621" target="_blank">📅 08:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443615">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P-n3w0IdSLIZ1bFU1i5d2zyJGWdv3_Q5vkUMLLtt7VLo0tR5GAoSkZrnaH17rbhOAIFEhe5r0wkbZRBZ0jyxpj_5AoqeleRjo96hjvs8Xm2nTx8GLgVZPe6BnOEGYJLjo8VwA_3SRwXFhyq3VwhdyutK1jGBNYX6Vdjlz__w2ay2iA2vKaYzv8raXKk0nRRPctRuGfqByeP0WnvE69R3XDCqx6rrDf79lBHVOfwpkyxpzK5q4GM5-qghSq-oqNuM_Kncc6-Nrzi2d_2anbYCpp6b2PELwVrbgQ7PGUUyfNV6AmcXpSpWdnB4Ao57U41HIugDM9beG63r0o_Vcl_AOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SO2KMFKMnSAZavkMbMXnjsKC7rKHpNhtqsypd0dTDsWmo6J-mSZejk8k38O9qfz0JRz-cOt1wV8FKOoUo90TpHz3Loe2syzhDlWnbbaidaGlJh6jmOv4NR3clWG0-bVI7oW7h_z4O-1n1xGMZ5Q_fKP9ZVgTRTz8m8-L4goIS6Q9SNKiWP9Lw0uesVy71-d1VeFqnBea07eo7Q_64cTe5eNmYWLI2oan8b7vW7bcmhTBbo2CXC0pBbBPoTetcCtl-VAvobMikCSUr0E3UKpOKUqY1VzoAmwkYFUJCaBUkVQ2homKZ6LtyEoE6WaWdIqVtWmlkg4hsAHFIVy2_9DMkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bakT20fJ1ZSrFyZwN-hsHkGNBEeo4L_j0REgLXBnsGSrJ6q6Y-P0CB-fZNL5LU17RWb0gbq3O_xPWfcg5vn8TdNglxYwGZnc0FXPcQCrCglsLMisZBHRErSkhisPSL7mMz6o9JQcnLsTTU6sAwsmmzt_TpREL4bHmMixbVVy7Sl7RbvwrvBn2niYm4fmBNl3CHEORene5L-54YSvbXhSgw3MFuRuentG3S5lGJBgLD82tboqAFN4b6VLZrEHJv4Rfz0cif4LYS3MGwIfaliOujBqeOtSIwW76H6URY5KtorsVsOzS8tF4La-Gr_6JvCW3xECUbiL13x5jmF2GzyzWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/stA00GcYc-pbhhGQRbuqR6xnl4LfBG_0uUFuuZMST0wmjjoYu9Kd6ijiTfzmBNm7RD21BPtIwrE2OpAMsXvfyguD0ymph3b4olC9WNEuI8GGCheORcBKGJ-_hh3W1VHjZ2G-2LQ3cVYe2jp4YlMU9UteX69DNzRTW8vFax0QOkD0khrjMMBocKamXaRTPS_LOKvcvxZ0z6AfEA3p5PJeiKqssUc35up_GZx5POG4ahSMg-R2NaN-WO0AzWulxyuCr-UGYnKDAEokGBfazMRxV_ZbGP_9lFFCTGnjzLPqx8S_XjqutJFdPHckR6zZ5SXHimvy8GVXs84gpXn4h_TyuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oe6tIsfmdyVH6tUufAhaWjsmFUfx0umvdNjwUwCMjWSGgankasb0PVNAE9sB_1qP3GwfIBg3FZ8pDO9zzWDKD87k7yBRSNLjYk9l92MFr0U-3xTON7flrg3SwHzmhp5QV0g9sHUwSwIZTjyORw50ITaBYnTRG70DX2ecsgCVfpdWT_MOZTUp5H7BxJSva3jhh6Cdegts6wGHKOiQx41QNJAt1-6vYqpxraMnOYw-Vqssp_RdZlS943RzTzwmx9H-lKD3veqf8HVoVCMmVrBwk30dyKyKM_2yvwo-dh9D1iaUrakC1YorJ6dnGXddTG5CspT0GH4hSKHJNeFZK0mbKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uh_K0XEQKdxhVSv-gkAs-mm2BcdVYEH8dUDMQqUB3v4YmThDiG-8BtQreHx9hGNuyLxhUocAY_bUYtLL-IEzICSdOCLsT5uhg1AVzc0RD1omOtfxyM0tma1v2ALbmV_4EYlpXAFRtNz_8Z7NQ0zyAc1GwUNna3FGIq07VpIvaV7O-XUQg3W_v6CYJnoy8J4BHjVi_QlrQ-sosw8234TDxeeKVTBjIBsvuATm_w8_mXnGssEjeNDNcalU50Rumy9M3KByqMccLkvkvv4Re6wl0KxYK5fHsSWQMicyhGBpYL5MszlmH481vlc0HXVj0qaQfCTnMR1SPiF7fD2-l6xp4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آخرین روزهای بهار در تالاب استیل آستارا
عکس: حسن حقی
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/443615" target="_blank">📅 08:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443614">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQF5ROEQbAG-pAoDesFhmxtJLxwqW3fw2fFfqGLmGrvarY6W_eHw3DGvxgW2_pP4D9JbO4Hk542DLwBDrLKXepdzO0Atx_aZgv-oKugB1BQucOtQKp1q_33ZKlaXeUDSDDA38Mz48N-wCH32I-V4LE7TkWG4aE6VvfLXy4qC88RixYZ39Bhgdhrs8NXkjtLJLkT9jf4GTDEZ2JkC69DVcTXbRI1Z1lat-9nBrjl0jdC_EmjmnM1dxs9XtYtU-3xktgBpWF1U72miRoh_NJatc1rthvqnHEMroMHkAa3YkqDhxsPKjpBd-8ebHlk7TnnNGaKX_5vlzC0WwyxSlU7EOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
کومیته تیمی بانوان قهرمان و آقایان نایب‌قهرمان شدند
🥋
روز پایانی بیست‌ودومین دوره رقابت‌های کاراته قهرمانی بزرگسالان آسیا از صبح امروز با برگزاری دیدارهای نهایی در شهر بالی اندونزی در حال پیگیری است و تیم کومیته بانوان کشورمان با برتری در دیدار نهایی مقابل ژاپن، عنوان قهرمانی آسیا را از آن خود کرد.
🥋
تیم کومیته مردان نیز با شکست در دیدار نهایی مقابل اردن به مدال نقره دست یافت.
@Sportfars</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farsna/443614" target="_blank">📅 08:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443613">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hMPD9-HxSdbsH901GxBWL0PCFJDc6Wr8zRnv6b04qVgtblVzoyYp-1BKetrGWPsdqfDo6YBcV2WqZcDnMqv60MajiLoFXpzUkyk5YS4x4Zs7jnvB358UeEG_WARBpfBqT0qEHk3jK3J8YDyOJcznGVKflDWdSg0s2wXrJU8xtJqbkeUwB8BLpW9V02mU2TjaQW9Dn6lwb35ydS_wQ8yXF881iTBBpf79kbNjfqmT9N35m9G5-E6s_c8NqaYgvFV-BzWOzJddhLUeBrooFxAC1fpXkD-0lI0U9BZss8bRYqD6Dryf81ZFCXNDTEUd1d78xiwkl9WGlwbvFrN0K8YzWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلاکت یک نظامی صهیونیست در لبنان
🔹
یک نظامی ارتش اشغالگر که روز جمعه در پی انهدام تانک مرکاوا در جنوب لبنان به‌شدت زخمی شده بود، به هلاکت رسید. @Farsna</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/443613" target="_blank">📅 08:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443612">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">توقیف تریلی با ۱۷ تن اضافه‌بار در اصفهان
🔹
رئیس پلیس‌راه استان اصفهان: باتوجه به خطرات حمل‌بار بیش از ظرفیت مجاز از جمله افزایش احتمال واژگونی، کاهش کنترل وسیلۀ نقلیه و آسیب به زیرساخت‌های جاده‌ای، این تریلی توقیف و جهت سیر مراحل قانونی به پارکینگ منتقل شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/443612" target="_blank">📅 08:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443611">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5c4c5dbc0.mp4?token=eo1YKEAc1jIqgh-ZACUKjWbC25Amih0EKNW2zgSPI6zlHEbY3KIfjseREKaY39q7EeM1Wi-BTXSj4vb9QqsRh0gd6hKpSzGNsbcF9MUM6-lF09xQEhfv-2BVG04BKYQ4wu8uYGfn5nF1v7dzFiuqWC_70Zz0kg02Nu5Ryq1SK9wXkP_s-2n4NKpEc18rJy1Pb9VkQhrpz7O1rz7prNiBRcYXExsBN_L-Opnj1NDQX2KVfu-x2i6pjPwPPkl698wX1hkHcbs4hTjZtlkij-M7zeA23LEUijy20mk8iwqalwtT5p0qyvFVgNt8uI1cjUNe6UabLGM_VLs4l8gaTS-sIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5c4c5dbc0.mp4?token=eo1YKEAc1jIqgh-ZACUKjWbC25Amih0EKNW2zgSPI6zlHEbY3KIfjseREKaY39q7EeM1Wi-BTXSj4vb9QqsRh0gd6hKpSzGNsbcF9MUM6-lF09xQEhfv-2BVG04BKYQ4wu8uYGfn5nF1v7dzFiuqWC_70Zz0kg02Nu5Ryq1SK9wXkP_s-2n4NKpEc18rJy1Pb9VkQhrpz7O1rz7prNiBRcYXExsBN_L-Opnj1NDQX2KVfu-x2i6pjPwPPkl698wX1hkHcbs4hTjZtlkij-M7zeA23LEUijy20mk8iwqalwtT5p0qyvFVgNt8uI1cjUNe6UabLGM_VLs4l8gaTS-sIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سگ‌های رباتیک هم آمدند
⚽️
در هزارمین دیدار تاریخ جام‌جهانی، سگ‌های رباتیک هم برای تأمین امنیت ورزشگاه‌ها حاضر بودند.
@Sportfars</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/443611" target="_blank">📅 08:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443610">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/319e6a7959.mp4?token=Hib2eAM165vZy3JqX5yQ_xLS7QWSEhfr1nFTFr1_ILa5CJZ1KPVI16t21-ZobV-iUOMNIx8L_p3bAqZIJDhxsPTGeG94i-RDiaGIvqFQLDV0rLmI1m-51q8ybE6Fn-KFJ9aQsBNAFb09lbmsVOuHmTyLjV-eDFWb9-BUhqadz_PpHe32fobyYlT5bVQtDBvdaZVYcsMvhrccf2hc9VPWkrhALiVXgScir4QcEb_OqLNCHWj5PBvo6oHWWifdMhU32yHsHRjR6atObCtvsvCsbr9BKwTdn4S8rD-PCox8GOmSPqd4xS9JyplnA5L1Q8LWIe61GWv01H4BtPadO4UgVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/319e6a7959.mp4?token=Hib2eAM165vZy3JqX5yQ_xLS7QWSEhfr1nFTFr1_ILa5CJZ1KPVI16t21-ZobV-iUOMNIx8L_p3bAqZIJDhxsPTGeG94i-RDiaGIvqFQLDV0rLmI1m-51q8ybE6Fn-KFJ9aQsBNAFb09lbmsVOuHmTyLjV-eDFWb9-BUhqadz_PpHe32fobyYlT5bVQtDBvdaZVYcsMvhrccf2hc9VPWkrhALiVXgScir4QcEb_OqLNCHWj5PBvo6oHWWifdMhU32yHsHRjR6atObCtvsvCsbr9BKwTdn4S8rD-PCox8GOmSPqd4xS9JyplnA5L1Q8LWIe61GWv01H4BtPadO4UgVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
با شوتی دیدنی، آیاسه گل دوم ژاپن را به ثمر رساند
⚽️
ژاپن ۲ - ۰ تونس
@Farsna</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/443610" target="_blank">📅 08:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443609">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLyue-sAZijz_9rttI6z5MQE4qOzgUtsxS-eTovDXPnu_EWGQt7H0hm0B_D-Y3bAUnvLlaSb0HeB700RJY8y6DB-c08nEsm1hrLUqc2lBrjxh5Hin50t3kXKLyjSnn9HfcwWzzvUr7FtEe9VPQJRldwCgot3w_VjrawJC5j11guGvRskkOSV-lR6iFP_fPIQRGcKrBWT0i7SMNTQEe9DTJEnUqFWfPnjPTc0jTbtny5mgR4C12iICDUJZkM6oMRBjzVfk6GiyXRKsLz9OCsiZq3qH6eGpTzbd-soCCB22SKQSR1iT0jdCfZMvqOMSuBhqVS8v-KlZW5Epkbp0eRgSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درخت افسانه‌ای رابین هود پس از ۱۲۰۰ سال از پا افتاد
🔹
درخت بلوط عظیم و کهنسال «میجر اوک» که قرن‌ها با افسانه رابین هود گره خورده بود، احتمالاً پس از حدود ۱۲۰۰ سال زندگی از بین رفته است.
🔹
به گزارش آسوشیتدپرس، انجمن سلطنتی حفاظت از پرندگان بریتانیا (RSPB) روز پنجشنبه اعلام کرد این درخت امسال هیچ برگی تولید نکرده و کارشناسان معتقدند که دیگر زنده نیست.
🔹
این درخت که در جنگل شروود در ناتینگهام قرار دارد، یکی از مشهورترین نمادهای طبیعی بریتانیا به شمار می‌رفت و سالانه هزاران گردشگر برای دیدن آن به این منطقه سفر می‌کردند.
🔹
مرگ «میجر اوک» همزمان با اکران فیلم تازه «مرگ رابین هود» توجه بسیاری را به افسانه مشهور جنگل شروود جلب کرده است.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/443609" target="_blank">📅 08:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443608">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVvSQn_Cpz6GDCwIjZV2NHuiJGwopKYrbnCAOK7sSHSMsBvgUe16NaplSv2aF0_D6f41AKP3D-rDAfla1kGIgv5ZL4xPaRfvYpDWaVNXlsgrEQ_GSbrRkfc4FRR4nrvHgHA61zLEa8cbjRtTmVhhdx4_FLX1irIKi4NJSg1DKqOndHatTVc_dtMD62zbaEPLgZ70jCEHqzwVNuRkjA4npVcH1Ce2o4RL_PCAmgUcfwmy7B3zK2D_AB2WsFq8FJ6kU-r2a0jtcj_M_RDUFF6xDL_FAg5WtHzBmW_X08-4E5Fg9UEok29DuZXK5LLnbl0cp1iWUTo_avN9rmw0HRVwKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرب نخستین طلای ایران در کاراتۀ قهرمانی آسیا
🔹
روز پایانی بیست‌ودومین دورۀ رقابت‌های کاراتۀ قهرمانی بزرگسالان آسیا، از صبح امروز با برگزاری دیدارهای نهایی در شهر بالی اندونزی در حال پیگیری است و مرتضی نعمتی، نخستین نمایندۀ کشورمان در فینال، با برتری ۳ - ۲…</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/443608" target="_blank">📅 08:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443607">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFrli8C7-7m6kmlr8C1LMwiPHt6MAPBz2D5TKO_BrjhqlA7nwHOxi3ILiv69BU2Qt6akhTDRJiGNTUt7jqL8L_2DfYlje-MsRHmoiuLWn9bkPR-hru2xvWoFZmGTzS-bBv4v9GWBK01Sc2eV7S394omdaqAVmKbMoHa4z-qL_MHRqjvMJqskx-G201UMP0JG00FDLbfT4oN8Y5JUp_rnxFQNhvKNwJx6uAhm5iGy3RYMExzPRvsPO4gXxAPu8krgD_U0_xt-JgQKSIiWt9YKXVXDtP1GHM9wJxmDkV0nWzg7nnqw3qSOjomGZKwPog4ZFDrrz9PY3Qq4jpY7Cjc7sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدرسۀ میناب میزبان زائران راهیان نور می‌شود
🔹
با تصویب شورای سیاست‌گذاری راهیان نور، مدرسۀ شجرۀ طیبۀ میناب به‌عنوان یادمان دفاع مقدس ثبت و به فهرست مقاصد کاروان‌های راهیان نور کشور افزوده شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/farsna/443607" target="_blank">📅 07:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443606">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e2d86b402.mp4?token=c4RHQDzTX1b-TPMI5xN5wcv12gyiL-_iJawl4rX2wQ-dvwr6bJQ0MnmDDPdbkKSXvlizACHCQR_D9BVHyzKnexTzPOYrX_O8o7ZCNns0XKH4l2Eb6ZRhWx2buMrpJo-NE2gzcoOtlL766_WYPk_DTaLhY1dHgpA6Wt7jaIL5VycioTkh59KqrMj1VHkaN3ErG8O9xRyBdY0BVA7fZ8J4f8ouxXaxg057cTFtY1cZt-e8en0UmHSCnSJILO-EUIeqW9aQG6wd7fVnDrLrlueyhyTYauapUvWufXV1wtvrdpnA2GsR-7jTgOcj5A0u_ioqNKZl3TbQeAT9l3bdfTx6fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e2d86b402.mp4?token=c4RHQDzTX1b-TPMI5xN5wcv12gyiL-_iJawl4rX2wQ-dvwr6bJQ0MnmDDPdbkKSXvlizACHCQR_D9BVHyzKnexTzPOYrX_O8o7ZCNns0XKH4l2Eb6ZRhWx2buMrpJo-NE2gzcoOtlL766_WYPk_DTaLhY1dHgpA6Wt7jaIL5VycioTkh59KqrMj1VHkaN3ErG8O9xRyBdY0BVA7fZ8J4f8ouxXaxg057cTFtY1cZt-e8en0UmHSCnSJILO-EUIeqW9aQG6wd7fVnDrLrlueyhyTYauapUvWufXV1wtvrdpnA2GsR-7jTgOcj5A0u_ioqNKZl3TbQeAT9l3bdfTx6fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سامورایی‌ها طوفانی شروع کردند؛ گل اول در دقیقۀ ۳
⚽️
ژاپن ۱ - ۰ تونس
@Farsna</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farsna/443606" target="_blank">📅 07:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443605">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kl3QFpmOyrbouq8KNXIO1ISg08RBByIV-naupIulAPdtND9VQFgSJfTBrXxfGbMAxwOWMG5AhkacBJ1y6iplIorej_rAEa_1oBA0gmgZZpF1fdGc-RqciUxcOCCTkKtu-5EyGiYvQUtzFzXuzB33Z0-zlvERf4mpt8xpScdUSK4Y35B7GXXDlRY81Sz51tRmeMXaWyEUyDpcUG6TztPEP53Tio1LIosZpGP4vtS0TVSsUN1QO6Oq3fSgomSUUUU-eeAPW2X4PzC8M2duCTyEDkhoGoL6lYHqck4jnV1-VTf3DoXGBSwWfb0-CcDCwJRP-MGGl2xsncIrDo4yQ6Q0NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
دیدار تیم‌های ژاپن و تونس به‌عنوان هزارمین بازی تاریخ جام‌های‌جهانی آغاز شد.
@Farsna</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/443605" target="_blank">📅 07:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443604">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAu1JpLi582Z5y-l8w5lnsELBSasyx0K2nWo_X0vM6Qo0VJjEzE8cUBx_niEvxjIAo2ekvHLOv5fmNna7bFOtT7y1rYQVqOZNKawrO0sLHvHfy7qEkJkGR9mC_Y1jZC-JphaOOG9wjjXnUJSrD2A99Kmst60j3CKyIVkBlg5sSRGKANu2EhII4QJSclYo2rqbZwaggyJi_V6oFAfisLjVBrI7qPUCYXXAXCJzYXEuCHnwWaDgg7SmbbDxMwvMpYyRVgXULcQnWsdebtMbdmXFKvWd2OBndx9Nau74T0538QYgWRjjL_8cbrY1Wl3uDbZ9jzuToZa_LCoZN4Z8Js6WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرب نخستین طلای ایران در کاراتۀ قهرمانی آسیا
🔹
روز پایانی بیست‌ودومین دورۀ رقابت‌های کاراتۀ قهرمانی بزرگسالان آسیا، از صبح امروز با برگزاری دیدارهای نهایی در شهر بالی اندونزی در حال پیگیری است و مرتضی نعمتی، نخستین نمایندۀ کشورمان در فینال، با برتری ۳ - ۲ مقابل حریف اهل قزاقستان به مدال طلا دست یافت.
@Farsna</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/443604" target="_blank">📅 07:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443596">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j4jDCgpVxgZdfvNqCnoFiTuBaxgerVa7NmSMGqpCr3S34uHfxxSL6xpz9GHWKMfpSgmvsU1rKRz5h2rBs769ilsvH6cm9VrOejx50aIm36eXpPTPucDnxGWhMNMLKA0lENccYCN6oZaGi0PvLgJUewTWUjALe8FttjN3zbRq0bjMcJEK3X-Uw9_nYsnL0SUdPqn4FsZgUDqWCObGjEoXeLhtrBXNDGUgm0f9DYcNedBTOgGfvSJXdgeZ3YPKUMgrQmBTLlaPc7AWDAydy6c8IjDYAongAhFgbRW2ZvvSSAvsd6XeesiGEswxTz9gJJ81LWmydgFGVuAhXpSP7cj58w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rx07q1NRy3NDU37x4BX4K4oQKthHHiURw6lNerAE7nX1FCTWPc4b0AflYjNy1dwXe-wtPDNuwSGuXOlKCXT328o2dkiYx-ojLk_hCQ7UNGVruMuwTtJcgucICusjOHm_u3sdAmr0rH9o7jht7WwVTH5lWsEe5g75ZJtM0apfVbXjJ0UenH5YVOm7AGIJosC_TwrWQIUbWbDo92mQzhQGn6xx02mFYGznJ_UW3-ITv8OoZOLxLtfay_C53QlKjnrdKDiKy-WAboM8IiJHVygVtvIU43VmOR2wb3zLjo7h8CEVhg9faJYrgJlf48nUVOgEGdfkyQil6S1m7_iIKAWqaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iodHW51IofbBI3pHi2V8JSeKgGTmt0c89ycpwkl4krBT2rpxYkDF-5aK-NJ_5W5lqcY57PeMPvimSKOERd5kLe8OdTx8ho_rgXQagnZVr-7Q8omAsUjOfIg-Btam7FPc-7gbMvExoyQFVCcpdxa42BVtzVYIoeLDwtgVu08ONWTEomZpjKmpyHm04nHxf2zFAitkv6uXVhh7TyNeDYRgwUog8TQu4izCyN1LzQ2SJxfZJlicTbQa21R0vqIJxXTIcQRRPRiy-RASdrYapk2YeWVzGv7blNRZFnU4hXoL3vEygxXixgTZA-YbrM1vbPUrEH1C6-lQk3hcb7M-e8l83Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gYVvOoUBYW0RNUvrHb0xAISfKJrkna1Nolotah0Z0uqqy6QDIbDwcuLbUzNXgBALHp85GRBjn79DlqmDs5efcqj_GNXtC9mbV36eOWlrOqZadIYPrk3uQxsq5q6L333AN_lbNbrk-w2W7t96K0oyMUOowANDkn80ELRHhaX9lWr3kDN5cRu_fyKeZRY5aaiaOCum9blIl1dEONRvo5DzZPEmXOGkZ63wwMxA_F4T_moDmbfj_93KvEBI7yqXuD3IBH0kaxBJryhtKQVzDTU4qVWgcG0oV1C_7TDNrk82qOxU10hMXsm-wLQSSjDFvK23MHDzrxnPdXrnoe7ILrDTUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nyW8aj4bYwqU_JJx1zuOqvXhy1HUOUclfgufnEJqCDhP7PUdgYlgPMnnctFqVUkor_uuv4KAZ2Vni6mm47LJhOmAn5ppRfOhg5_eGEHWdGY_V0QKQcvFQIIxhIlDDApgZYyKYo4BtKfZcOgOKV9q3NAJGe6TNr6_szk2HLtwizfYmT9pg77z-xxrd2d15uW2_fHsW3xsC168XdFFmkxTTpmV6EUtOkMqdvzM2BJHDrmDkunumrB4Oj3MgYsuipPPGNdIqhm1LAEejJfzaSivzlXkKbTZABrTr4LoVoeJ_J57D8JI38qCTrPsFd6UwppU1hbrnan7D5kqZ9vMw2u9QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f_d-JvTifprZjgwZRFpY_Z-8RMCCpKw7pzRGhwKykSFnvb0QlYsMVU-bsLM_d_1jGhN7EQlxj_27hykBmyZOu_wZZX2WgdR6GbHaSbDCwN9B6zJCJ51TYWjSSSLN2cPQ9JIrMLGQ8oYqOpfWphsTp7EoUX-XEDDfKS4d62lJZcoKgfmeLQX-4TiFujj1sYrpn6wyJof0FdnZJ58gnVgjzd0RKsg_7QgemW0Szys5nUbizO9BTOIpha4k-pruAWyeG97R9PaU23b8QBqskDQa3XJihAjICo0yUp7hfEvczPgtoMTcTtfAK-4stP-IhJzewksUMmKARnyrcmSOG9qr1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/guwG56yBstQ0QPpYhH6E6fOwEg0963W0-1RT2bSsxgZ47yDiPiZrpM29smxh95SH3i3oOv1qAA4aje6Tev34ysouWqojQKt4NQuDAum5RV77_XtIBCO_MRmGsns1i2NInKCBecUpVv0ZzkRus_vA9-BtsNphpki85WQ9ShFdOSx12pOYBON1SQtKISkrgli43uTFkF1H8ngprpU3RnUbqbPg_8K2mQnsFEFVt5KERqJoyTg-Jiy9fI_v3_tnVkdxr5Zmv1C8jrIhBoUez-hoP4dsvKEL0ToE1S4N94vZ6LZXEvLDbrtZQoWyOY8IwP0cBqMTU-9M41rjjBuI7G0DPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ilBlIxgWq7szn2qcj_bOmdasZ5qyL5KeWEcuxAYy-hn8YDVHisEqG4QhGwrOP0CsAXqVOr6f6kK19jyJsJ3-NyftRdTsduihEIK3hB_VHPOJEUS9n5jjnbDfGsYZI7E9bGnTc9J_7nnwdK-oi8M_SRnN6pHN3w4gpcr1lIXno16913LSgMdCjrakkUB0EyxlYBMO_-cB3QwKM_0j9tKjBNVvUX_SKsUe8V7MqM0HdQQpOG5MjdnIuQ1GyLKpp8oMagPFsqS5-RfvGjjYesTG1PQKrZXP4o4CcQGWky8zV8a-ZPbbjVtraQT5__E17yD-L9TC5Cw7MBOTa42HY8Wp2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
«احلی من العسل»؛ تجلی عشق نوجوانان به کربلا
◾️
مراسم سوگواری شب ششم محرم و گرامیداشت مقام حضرت قاسم‌بن‌الحسن(ع) در آستان مقدس امامزاده طاهر‌(ع) برگزار شد.
عکاس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/farsna/443596" target="_blank">📅 07:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443595">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس من</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/430a0eec4c.mp4?token=kMIVwZ8SYOmiCBilvYmRqxNAh_exk0W8k8sTxIisnjrWc6UMgmuGXnAAjCtoEsW1xRZQbJ-jGmaSVtV_HD3yT0zHNUI3Iuo7Zrad45JE3aBz8SbeDuPDkDHuiBiB6Kb-AS95mOpCscubL3DY6Byj72ke9NE1vwwW2zGXW4N46JSekAXhNXhi0OS2ZffgRegT5U6C6e8Trh1DlZZqw07B0cuKb3dfxv7ZJFj_5FtbFFpXI5ix08ZVpWxyIZNait5XKb_8_Hcchx2EvPutg9OV7TAFqiObIfeNIX3GH0a_0Ycuz92R5gLbNrGg2nnFnhOSfqJpE3_O7Xpturkqql2zpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/430a0eec4c.mp4?token=kMIVwZ8SYOmiCBilvYmRqxNAh_exk0W8k8sTxIisnjrWc6UMgmuGXnAAjCtoEsW1xRZQbJ-jGmaSVtV_HD3yT0zHNUI3Iuo7Zrad45JE3aBz8SbeDuPDkDHuiBiB6Kb-AS95mOpCscubL3DY6Byj72ke9NE1vwwW2zGXW4N46JSekAXhNXhi0OS2ZffgRegT5U6C6e8Trh1DlZZqw07B0cuKb3dfxv7ZJFj_5FtbFFpXI5ix08ZVpWxyIZNait5XKb_8_Hcchx2EvPutg9OV7TAFqiObIfeNIX3GH0a_0Ycuz92R5gLbNrGg2nnFnhOSfqJpE3_O7Xpturkqql2zpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدای مردم|
چند ماهه که فرزندم صدا ندارد
🔹
ماه‌هاست کمبود قطعات و باتری دستگاه‌های کاشت حلزون، شنوایی کودکان کم‌شنوا را در معرض تهدید قرار داده است.
🔹
خانواده‌ها می‌گویند به جای وعده و انتظار، باید برای تأمین فوری این تجهیزات حیاتی تصمیمی قاطع گرفته شود؛ تا این کودکان دوباره به دنیای سکوت بازنگردند.
🎉
شما نیز می‌توانید مطالبات‌تان را در سامانه
«فارس من»
ثبت کنید.
@Farsnews_My</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/443595" target="_blank">📅 07:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443594">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfLhLuQh1i4s1U56VI4POAucRtYdtFJBDb52UOK7mwmAhkyTIfVCTY8HBgPRC541OWAPzDIMS2Dr9aySU6Klu9T_JZ-xA5AyvltvyVttrgFsih_KtRvpn738fIHPn5rI-EF2dgTBhSuoqRHuVAV5-UmLoQVx0aLnmsvcdmxSrRn4sIFD6lcHuaOFa71uuBxQQm6IuCkPiFjXF3rUYBSJSjVSvpejApYami23YbqfjZY4Sv4pub-V-Gj0dsviZWZofQmPC3uH19xRITQrqGmcNsWhqccmrTxaMpBtAzo9lmduvGywswyaWNZBh2cd0cpuX5uxMDyWi2oaeEoXR8UXTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش از آنکه شمشیرها از نیام بیرون آیند
🔹
روز پنجم محرم فرا رسید. کربلا دیگر به یک اردوگاه بزرگ نظامی شباهت پیدا کرده بود. از یک سو خیمه‌های اندک خاندان و یاران امام حسین بن علی قرار داشت و از سوی دیگر، سپاهی که هر روز بر شمار افرادش افزوده می‌شد.
🔹
در این…</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/443594" target="_blank">📅 07:02 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
