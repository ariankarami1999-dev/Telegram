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
<img src="https://cdn4.telesco.pe/file/Wb5vikQKjnR3R064ZObBTHz1gJJuCo74W78UKpOhVvFS2Map67uxXatO8taB6JER1dNWDdtX0pdhMfysmMZxqgirDg0QiTRwZ67CR8ZHsW_VI-92p5iIsCCAFjG0B6jxrbmA0IVR3STpyV-PDjwTSMvhL2uBUwlv2KoilXLF-LfhntpGDwhks-qwkVJ2OIFOqneekX8pII0Q-D1-C0vPozQxFBzvhKZaI-BC6SqcIZijzwedTv3AwRKEatLyjBaJ1sGn3FQ-bzNd_bghF1vbMkHbnUIPbw1paApMmKXdpQsUJ7rJlDcD2N9ZWLnkW1yh-jUA-oXT2tZSVNLX1Q1OSQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 126K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 15:09:19</div>
<hr>

<div class="tg-post" id="msg-69936">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vct1DEK63YEq8hVqrmXGLoU0aqtIyoaVMogkFZNxnHbIXa-vojxxGRarV8sRheYViJkeKvuFuLZX6mjI-7gV5fFyc1AtbKnaqqnJKWrmBrRGUoO5CulBwmrs8me2QIGdJSf0I5X_Lv8J88aU9qhIO9ocVhwCv14Y7bkqbPfNXCFWuwjOEhOA_74gUlKheapY0fjqRMDrgC44l4sSt9hJ3PVqcGkntJpjNwGBbHEU5WhAuLGhphPbzy66kdfqu4cPRvf4g4p2Qg2KqXjNtyw8MS6-h6JJHbKIyUrmzAcL0vpH0u2VTlFp-lik9N9kZLhA3TFZtY2oFDkfGdTINY0rWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
🇹🇷
🇺🇸
نیویورک تایمز:تهدیدی که از سوی ایران مطرح شد و باعث شد رئیس‌جمهور ترامپ ماه گذشته به طور مخفی هواپیمای "ایرفورس وان" خود را تغییر دهد، زمانی آشکار شد که او در آخرین روز حضور خود در اجلاس ناتو در آنکارا، ترکیه، در تاریخ ۸ جولای، در حال عزیمت بود.
اطلاعاتی که توسط سازمان‌های اطلاعاتی آمریکا جمع‌آوری شد، نشان می‌داد که یک تهدید خاص از نوع موشک‌های زمین به هوا علیه هواپیمای "ایرفورس وان" وجود دارد، صرف‌نظر از اینکه کدام هواپیما حامل رئیس‌جمهور باشد.
همچنین، فردی که در نزدیکی محل برگزاری اجلاس ناتو حضور داشت، در حالی که یک موشک قابل حمل روی شان خود داشت، مشاهده شد. در همین حال، عوامل ایرانی دقیقاً می‌دانستند که ترامپ در آنکارا در کدام محل اقامت دارد، از جمله طبقه محل اقامت او در ساختمان.
@News_Hut</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/news_hut/69936" target="_blank">📅 14:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69935">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7465fa629c.mp4?token=oFjSyF-qxgxI4SxMfCT-J2PaafF9DIGGoxTpq8PAh4KtEMw-tpczuX-HITO5R5TC2NENUMqWOkINzHw_Zi5IeinXjBXbQlqO9k3f1rM7Wnsw-oW2XmnVs3mFmytgu6W2Cxhr952CRdIOydeXfEUpI6UeqkOexZUwOBc_fHhIj0byuwn0Fjg2CiuRBYGWsiKAi4xqaKlvcSmROj1iR3bvnWD8Jh6veIH5BXzERXpUNAHMUTuEFJxJSLGlin6z-ICBDxr1r3biJhKBUWO603Xp8Yi5MIDcSLs8JAn1R47s2sFYrXv8PigQ4sK_ym12RskNSgiKWRMoypSP7odZ6Lr0XkJpgtzmwsEe0ZKRoQExMFGqUwLjlR-fnI0-Gfidp_Lj4inzx8w_s5r8aLftp1js2yhXeAgZx-Q_Q8SgngLHllDTcZwh2DS8d3qao65H9cLg-crXZ1db_fCSzoBFrqyBtCx0M1nKI6Rg5RRKAyTYT_-9mtZzMMzHr9u_-2rEb0W89jqDwMxqe0tKb77X90qjbhVajwGXjs3uW2Se3VSrIlIS3ps6ncoj_HH-7mfR5F4n9qYY1kFabQf-y-pjRtXxr9Gmx7ioVRq0ur6Qd_05K5bnV4i7tZWsfN_f8-3FvrzYr7vbZafiOVpTjOKEAuClelSYxyqV7bix9uYQX4gkNaE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7465fa629c.mp4?token=oFjSyF-qxgxI4SxMfCT-J2PaafF9DIGGoxTpq8PAh4KtEMw-tpczuX-HITO5R5TC2NENUMqWOkINzHw_Zi5IeinXjBXbQlqO9k3f1rM7Wnsw-oW2XmnVs3mFmytgu6W2Cxhr952CRdIOydeXfEUpI6UeqkOexZUwOBc_fHhIj0byuwn0Fjg2CiuRBYGWsiKAi4xqaKlvcSmROj1iR3bvnWD8Jh6veIH5BXzERXpUNAHMUTuEFJxJSLGlin6z-ICBDxr1r3biJhKBUWO603Xp8Yi5MIDcSLs8JAn1R47s2sFYrXv8PigQ4sK_ym12RskNSgiKWRMoypSP7odZ6Lr0XkJpgtzmwsEe0ZKRoQExMFGqUwLjlR-fnI0-Gfidp_Lj4inzx8w_s5r8aLftp1js2yhXeAgZx-Q_Q8SgngLHllDTcZwh2DS8d3qao65H9cLg-crXZ1db_fCSzoBFrqyBtCx0M1nKI6Rg5RRKAyTYT_-9mtZzMMzHr9u_-2rEb0W89jqDwMxqe0tKb77X90qjbhVajwGXjs3uW2Se3VSrIlIS3ps6ncoj_HH-7mfR5F4n9qYY1kFabQf-y-pjRtXxr9Gmx7ioVRq0ur6Qd_05K5bnV4i7tZWsfN_f8-3FvrzYr7vbZafiOVpTjOKEAuClelSYxyqV7bix9uYQX4gkNaE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇮🇷
محمدرضا نقدی، مشاور عالی فرمانده کل سپاه پاسداران:
«ما بیش از نواخت شلیک موشک‌های بالستیک، در حال تولید و تحویل آن‌ها به رزمندگان هستیم.»
«ما فقط ۹۵۰ شهرک صنعتی داریم به علاوه صدها مجتمع صنعتی که خارج از این شهرک‌ها هستند.
اگر روزی برسد که ما هیچ موشکی هم نداشته باشیم، ما خطرناک‌تر می‌شویم چرا که دشمن با تاکتیک های ناشناخته ای مواجه می‌شود که می‌توانند منافع آمریکا در جهان را به آتش بکشند.»
@News_Hut</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/news_hut/69935" target="_blank">📅 13:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69934">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyCngHQYJ8Px8QVZzaC9dqLFTCY3mLChmHEfHpit-3YQPbsBYsWdJB09e2BeFQIHMh1Em-k2IDxj_4Sl1PIK8MSFz8x2XQDGxb8YL0z_QeFmTCfYeL0P1TvtPKie6P9qWUv6KBg46bm2fgz52Fa0yX_wyUBFa71hiF7HFWCkBDrLAuLEwVir-WfjHox9R480UXfMKhZAh71RkFsQ-LPMAEB5DUkpkF9FN7-mwhve-_azG8PuWNQtCb4ksMfOhbIfH7N2haOkX0LeIaleocPzFXC8uDCWqOXs0awpsmZc-xd2dSQrA3Fl7xbRcehrlLFHHHD_CpnDH7_1nWclz8FLBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
امروز ۳ تا اتفاق نجومی قراره همزمان تو آسمون رخ بده:
خورشیدگرفتگی، هم‌نشینی ۶ سیاره و اوج بارش شهابی.
@News_Hut</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/news_hut/69934" target="_blank">📅 13:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69933">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fae5c53c68.mp4?token=SyfiZdCJhCgKWwVTJ-7Mo9bcpG2BQmhZdhcRTALTO9C5Cev63X9DE9g1VJNBnbXUH4WsmbzxK7WvpZBWGeXqOJdYZjsOSMsQItBKayWKs8T7tGjoaa5p7RM7BwOptjWwDro2Isk1ki-umw_ktv0NAF4fFbq0NPZ4EklVVwNFqk_QHkprNSwvAbqZKFE9lrdOZPBtLpMxmhdF57pa2PLq352szhUSAzhzqs-bGZcvVwyDH8PFLbq8YnT-WOC4Fc4SKTAYSMvTxPRirgg9JoRPaH9uzYomSaJbMvI0wenM4cG17gWmD9zt9S5ONE79RPWSDqJypomexeftmBJxFCykvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fae5c53c68.mp4?token=SyfiZdCJhCgKWwVTJ-7Mo9bcpG2BQmhZdhcRTALTO9C5Cev63X9DE9g1VJNBnbXUH4WsmbzxK7WvpZBWGeXqOJdYZjsOSMsQItBKayWKs8T7tGjoaa5p7RM7BwOptjWwDro2Isk1ki-umw_ktv0NAF4fFbq0NPZ4EklVVwNFqk_QHkprNSwvAbqZKFE9lrdOZPBtLpMxmhdF57pa2PLq352szhUSAzhzqs-bGZcvVwyDH8PFLbq8YnT-WOC4Fc4SKTAYSMvTxPRirgg9JoRPaH9uzYomSaJbMvI0wenM4cG17gWmD9zt9S5ONE79RPWSDqJypomexeftmBJxFCykvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سفره‌ای که واسه عرق‌خوری تو زندان پهن کردن:
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/69933" target="_blank">📅 12:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69932">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ca7afc613.mp4?token=dNgac9IfY4QDzka5ifP82kXpDwJnsvJVTLqrtdvrGNkyN9edHRIgtzTbOL8o5G50CVnSF0h07wpcbTiDzqhgkJ-QSCkZB6GeEEvkVFTc4WK8DR3BidhwuFgLSShawkpQFhBnCNaZN2p31egKFBpy0zjg4hDjGSlKAcPLx2_DfD0etnnp_dgb532IBjeL2ODk5aRgP3P3hUG_KxYmlLF7WR1Dy-2Nq_RaUYYTnSL0Nby7m6JXP3JcoMcCKSUh903vl_os9M1d6c6tdLkzamL2STT0H1KepNBkQrNxNZ0GrmEYVsacdbH9Pu-4XJ0aiab6Ivb-CaEcdesBceeor1HDfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ca7afc613.mp4?token=dNgac9IfY4QDzka5ifP82kXpDwJnsvJVTLqrtdvrGNkyN9edHRIgtzTbOL8o5G50CVnSF0h07wpcbTiDzqhgkJ-QSCkZB6GeEEvkVFTc4WK8DR3BidhwuFgLSShawkpQFhBnCNaZN2p31egKFBpy0zjg4hDjGSlKAcPLx2_DfD0etnnp_dgb532IBjeL2ODk5aRgP3P3hUG_KxYmlLF7WR1Dy-2Nq_RaUYYTnSL0Nby7m6JXP3JcoMcCKSUh903vl_os9M1d6c6tdLkzamL2STT0H1KepNBkQrNxNZ0GrmEYVsacdbH9Pu-4XJ0aiab6Ivb-CaEcdesBceeor1HDfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
تصاویری جالب ، از تلاش ناموفق یک تیم آتشبار سیار روسی برای رهگیری یک پهپاد انتحاری (کامیکازه) در حال عبور را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/69932" target="_blank">📅 12:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69931">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fd2c3a8ef.mp4?token=X7qVTw5loN072RRP6TX4CDdmD-PIKQpamy8XmIft6lPESt4RBhnXXC3IgRuRJOqG2n2YCW4zVmbNZgBqzX-emCDX0ThcNR-hNiSW1OHoV-4OU0IISUATAfLzDvDXCl-kHCUmuczlIOtJEli6yadnWUamEyfAN4ctgEhMNIrkRNrYBxeoM7Jtesz2bZMSWVhUczqBhAsche26XO0kktWSxzrjfcTvwqN0jeL_e5g6JqH26nhBfI4Q2iBM4Pebax2V9N5wYy2BJ4RM7B_X2krYvtICWEhqhbKclxPD97u-vsaEuWVwZAu8gI0Oi1PTJT84KNVrd1aOUYd8crW8ZLWwHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fd2c3a8ef.mp4?token=X7qVTw5loN072RRP6TX4CDdmD-PIKQpamy8XmIft6lPESt4RBhnXXC3IgRuRJOqG2n2YCW4zVmbNZgBqzX-emCDX0ThcNR-hNiSW1OHoV-4OU0IISUATAfLzDvDXCl-kHCUmuczlIOtJEli6yadnWUamEyfAN4ctgEhMNIrkRNrYBxeoM7Jtesz2bZMSWVhUczqBhAsche26XO0kktWSxzrjfcTvwqN0jeL_e5g6JqH26nhBfI4Q2iBM4Pebax2V9N5wYy2BJ4RM7B_X2krYvtICWEhqhbKclxPD97u-vsaEuWVwZAu8gI0Oi1PTJT84KNVrd1aOUYd8crW8ZLWwHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیویی از هجوم انقلابیون به کاباره های تهران و نابودی هزاران لیتر مشروبات الکلی، در سال 1358
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/69931" target="_blank">📅 12:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69930">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/news_hut/69930" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✈️
اپلیکیشن MelBet
🥇
🎁
کد هدیه 100 دلاری:
Sport100
🔒
برای تعیین رمز ورود حداقل از 8 کاراکتر و حروف بزرگ و کوچک انگلیسی و اعداد انگلیسی استفاده کنید، مانند Hamid120
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/news_hut/69930" target="_blank">📅 12:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69929">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ahjHkbDS7PpcszymJ3A_Y45CWJKXVCrGxuQTv1SzWg4qDOk1-Q_3lV4pkk7FLci3YUhKsvUdHMrHLkK_TT6CsBNvUNMWoxxCiiD2zwVT0MPenvgMqL_sFtENVwYBhs-AaZ7MvqLWcorW1EdsvihclyNUiCdMUBmP-bWBb96HPqE4Rz5Sv-Zkpqx4lFhQ5F05xVSRVMqRPSuBsIDiGvZhuCEzdqSbN7Sow_yKjNrbxaqCLCA7I9h1wksvSFvNhmbQOuOHtz-Ph09jDOz_lE9waBCcPl9G-mHXGS15JRlnbbED-77Co0yBosLPmulN-aaODQaerFkvXrx8stebNram4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌     ‌ ‌ ‌ ‌ ‌    ‌‌ ‌‌‌  ‌
💯
‌
فینال سوپر کاپ اروپا
💯
🆕
دیدار فوق حسااااااس
پاری‌سن ژرمن
و
استون ویلا
رو با آپشن های تخصصی در
MelBet
پیشبینی کنید!
💯
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
📱
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه ای، مطمئن و در کلاس جهانی پیشبینی کنید!
برای ورود به سایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/news_hut/69929" target="_blank">📅 12:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69928">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9676b05e8a.mp4?token=KwyWNXKBKxXlG7JbWm_fwHain9JJE7BWEOpr5oQ1xwVX7NTE3d-Wb22BaoFssB8yiqTqUgwh3Rudxe6U9m620A48kaDgsnEWCsXM882o6rFFJLtMOcBcTPog8ToYp6tE-jj91RnCfsZtiwy3w-Zod3yMJBS2OjXkPi65X2VmoM29bZS_QDn1l0zq6XXykg6EDntVCbkYTYlPzR2RAsOHwRvOPze0LsFHQY_PD6M1B9FSSE8bGdS09ITyCh8ZzY9q1E6hhS0jD7Z926N7CxUo5Ae-B4nq_vfwc8PE5dPCTOof93MThu6UYwiFojOqkCmrYkGh72-7NQi_6mdZTAG9yg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9676b05e8a.mp4?token=KwyWNXKBKxXlG7JbWm_fwHain9JJE7BWEOpr5oQ1xwVX7NTE3d-Wb22BaoFssB8yiqTqUgwh3Rudxe6U9m620A48kaDgsnEWCsXM882o6rFFJLtMOcBcTPog8ToYp6tE-jj91RnCfsZtiwy3w-Zod3yMJBS2OjXkPi65X2VmoM29bZS_QDn1l0zq6XXykg6EDntVCbkYTYlPzR2RAsOHwRvOPze0LsFHQY_PD6M1B9FSSE8bGdS09ITyCh8ZzY9q1E6hhS0jD7Z926N7CxUo5Ae-B4nq_vfwc8PE5dPCTOof93MThu6UYwiFojOqkCmrYkGh72-7NQi_6mdZTAG9yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قیمت های پشم افکن خونه و برج توی فرشته تهران بعد از جنگ که به متری 2 میلیارد تومن هم رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/69928" target="_blank">📅 11:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69927">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6983998d5.mp4?token=wBla5BbLopaBzQ7kHZweGJrlRe0m3o4shvuMNfdHirhJatWcKE_jFjge-b143T6USt3MSof3DdarHsPprFDwMktlbpDv_OhXW35Rs49rTJileFL9UAhvu2NeqFt_dNI-AJW7DYFMeqoRkbGeLBpyIIWStlkBjKFrCqoPtZQAQVjwswB_rmgXn6kA-FjvVDn7T6EWkhm5IqfKLBGMxtSBf1zH5M9LQp_MWbXvyDCO8oMN1ZzZQeDl2eZ52pDjUgxY7XynVxXV5WE5bMw0RTpSTqD9tUMiXrWPf0uTIzdLjqv0wtBPkty387TGl-NBgS1ini3ZGn_xsfFOGL7_MXA-xCpueMD0e4nN9zAIdyhE42QGSKV0uB3Tgtypxf4q_5h6TGEliLzwl-4x88-rzlsZILiErNCYwjZtL7cPYMiWfVjP5VYCyB0U1ujNgu7M2eJYD60KiF68LWe6wWPQjOdPViAP8m9BrQlCzqOiWnRo0tvuH1VZ9baV5j28vUwFLgM7XLPUmNz5UEZwWGv25IfWRCfaBCBu7uIAky082bNDzuoNDYg48jDjFNJWajItJdniPhaXuUjpoXE3LrBjKjfyX4V8McELNFgRi-eftHT7ZaQBDqQWMUH-3auIWLm0jnSwmdUmnZfrNLNytHiNREQY1mFYEO_J8qI4VQXAC34W0Gs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6983998d5.mp4?token=wBla5BbLopaBzQ7kHZweGJrlRe0m3o4shvuMNfdHirhJatWcKE_jFjge-b143T6USt3MSof3DdarHsPprFDwMktlbpDv_OhXW35Rs49rTJileFL9UAhvu2NeqFt_dNI-AJW7DYFMeqoRkbGeLBpyIIWStlkBjKFrCqoPtZQAQVjwswB_rmgXn6kA-FjvVDn7T6EWkhm5IqfKLBGMxtSBf1zH5M9LQp_MWbXvyDCO8oMN1ZzZQeDl2eZ52pDjUgxY7XynVxXV5WE5bMw0RTpSTqD9tUMiXrWPf0uTIzdLjqv0wtBPkty387TGl-NBgS1ini3ZGn_xsfFOGL7_MXA-xCpueMD0e4nN9zAIdyhE42QGSKV0uB3Tgtypxf4q_5h6TGEliLzwl-4x88-rzlsZILiErNCYwjZtL7cPYMiWfVjP5VYCyB0U1ujNgu7M2eJYD60KiF68LWe6wWPQjOdPViAP8m9BrQlCzqOiWnRo0tvuH1VZ9baV5j28vUwFLgM7XLPUmNz5UEZwWGv25IfWRCfaBCBu7uIAky082bNDzuoNDYg48jDjFNJWajItJdniPhaXuUjpoXE3LrBjKjfyX4V8McELNFgRi-eftHT7ZaQBDqQWMUH-3auIWLm0jnSwmdUmnZfrNLNytHiNREQY1mFYEO_J8qI4VQXAC34W0Gs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداشمون در یک دقیقه به ۱۳ نفر پیشنهاد رابطه داد و  همشون هم ریجکت کردن و تونست رکورد ریجکت شدن زیر یک دقیقه دنیا رو بزنه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/69927" target="_blank">📅 11:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69926">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
لحظه نابودن شدن خونه های مستحکم و نوساز توی کلمبیا بر اثر زلزله!!
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/69926" target="_blank">📅 10:34 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69925">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72ecf27139.mp4?token=Stv_mSYYjzR09AzJ4zxfoD76YjPObUDMBueYAJkIo-a6I-yOEsuFLObi-AXrtwT5RlF4Trrk2ayyhXX_VzUfrsOILM_X5jbNTmcbf0-yJXqeTdicWJWi5NPppwJkFs3XBYhZw5UehtyBNBl8KfVZcve88ElhFHQQQ9Kn7X7hWItkdU3yuv0RGX1wOJCNG74sat4i_e6sngam8T8gyQrZgOs9Wzo_gqyp-eNOHrr7k2lIZYqi3FqASps7t9IZOAYOiI0NagPMejHlDQsj09bUqAkW0r8u8p-ue6lpisNmUwyLmfp3bJItj5mMCR-DCbd_gD2rCwJqcWpqu2KNjwlRxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72ecf27139.mp4?token=Stv_mSYYjzR09AzJ4zxfoD76YjPObUDMBueYAJkIo-a6I-yOEsuFLObi-AXrtwT5RlF4Trrk2ayyhXX_VzUfrsOILM_X5jbNTmcbf0-yJXqeTdicWJWi5NPppwJkFs3XBYhZw5UehtyBNBl8KfVZcve88ElhFHQQQ9Kn7X7hWItkdU3yuv0RGX1wOJCNG74sat4i_e6sngam8T8gyQrZgOs9Wzo_gqyp-eNOHrr7k2lIZYqi3FqASps7t9IZOAYOiI0NagPMejHlDQsj09bUqAkW0r8u8p-ue6lpisNmUwyLmfp3bJItj5mMCR-DCbd_gD2rCwJqcWpqu2KNjwlRxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت های یک مقام حکومتی رو ببینید که باخنده درمورد شلیک به سر معترضا صحبت میکنه:
ما به پای معترضین شلیک میکردیم ولی میخوابیدن میخورد به سرشون
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/69925" target="_blank">📅 10:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69924">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1a54f6b8d.mp4?token=tZ-F7KlFJ7XScrbeghwjetZMK6GKK95JUkiH1IZm64Y2CrM8uX5WLun2wx59wB1uAnjP1cDqOHgE3eDHmxXCBCwS2KWTIzjUM7094i68nrJyxlgpYiehFLqUp1wE8XWIl7D8GX6yKpBTdtmq5DdlU-B5d7sSNDnPCJsB_5zEuyTd1ZJ-E-moKLnOmODKa8B4Rxhtp9sBeQ1HpHche6ujA1HL7XF5W_lKVg943nSdDfmY-G1_nR-xk4b4bSb_eFO3VWnktxJp-mWp8knAc2f0CPRP81WrRWTttWdH_ero_jpdh61deOV1YLWXNYHAP3BP9lCGT8r53B9prF5kec7dcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1a54f6b8d.mp4?token=tZ-F7KlFJ7XScrbeghwjetZMK6GKK95JUkiH1IZm64Y2CrM8uX5WLun2wx59wB1uAnjP1cDqOHgE3eDHmxXCBCwS2KWTIzjUM7094i68nrJyxlgpYiehFLqUp1wE8XWIl7D8GX6yKpBTdtmq5DdlU-B5d7sSNDnPCJsB_5zEuyTd1ZJ-E-moKLnOmODKa8B4Rxhtp9sBeQ1HpHche6ujA1HL7XF5W_lKVg943nSdDfmY-G1_nR-xk4b4bSb_eFO3VWnktxJp-mWp8knAc2f0CPRP81WrRWTttWdH_ero_jpdh61deOV1YLWXNYHAP3BP9lCGT8r53B9prF5kec7dcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی:«بازندگان و برندگان انتصابات جدید در جمهوری اسلامی چه کسانی‌اند و آرایش جدید قدرت چه چیزی به ما می‌گوید؟
🔴
انتصاب محسن رضایی به دبیری شورای عالی امنیت ملی و حسین طائب به فرماندهی بسیج، دو پیام مهم دارد؛
یکی رو به بیرون، درباره مذاکره، جنگ و رویارویی با آمریکا
دیگری رو به داخل، درباره مهم‌ترین نگرانی حکومت: خطر خیزش دوباره مردم ایران.
در حالی که هنوز درباره زنده یا مرده بودن مجتبی خامنه‌ای و میزان سلامت او تردید وجود دارد، سپردن بسیج به حسین طائب، یکی از نزدیک‌ترین افراد به مجتبی، یک پیام روشن دارد:
نگرانی اصلی حکومت، خیابان است.»
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/69924" target="_blank">📅 09:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69923">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa002b9fb9.mp4?token=GDtstVzFlYS9q1WaO1FHSMSEtmEmdd6XW2Hdj-SXQyHrn-T-EUCdowTV4sNmn3iucvYLJEHzpduWA7TGSHq2V53eUlKcpKzHxZas1l6jvJLE49CulJFTRpv-K79hVNBF_IrFux3v7zXLDZwx7HYYwqw3H69Y0y4K8tm1OnLVNA4wB_hR1Y1aaWwOGAQiZnZVdSc5yDwDPCU9KtNXHniBvsMGRLjHBp8qALRwXi3vJZTYIyR7_lQOzZmRGYNGu8YMqOEyMM0t9g_9IpBX2FjFfNcMkvtlUmxBLRiOV0oASuLE9-xQKZoVMlAWWupmlK67VWJwz7I9ANrtsDlGgtrL7ajD1FHe8jVoIzIxfV0uMQAML9xy45c3NZWK-ZN3xCsX7tAoOM6KjVzOYmjFPMzwpPGFf6sx0fJ6GnThiJjyPpW7ZEFRHqwTI5yjP8QLiJqSHR49jpSuhPPznTAOK0s71y2uyOeYqV6U1Pxdb0lGiWqQAt2DSjZUkIrYE6r8vL9qaHRmPlBbHvAGGrCLJj9Im33l-vqI2aD7Mw2RGxm_mFqKMDdZ85adzvVznZtSqP4emD5raxfa757Ht-DmMdAyppzNTKC-yiUqjuwLPvMkUgU9SxbKVDYctAqeE0OJZudMMmVGlpjsRfeNbLda_VAoSq1onw2VaUZg-VZ1iGYCF0I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa002b9fb9.mp4?token=GDtstVzFlYS9q1WaO1FHSMSEtmEmdd6XW2Hdj-SXQyHrn-T-EUCdowTV4sNmn3iucvYLJEHzpduWA7TGSHq2V53eUlKcpKzHxZas1l6jvJLE49CulJFTRpv-K79hVNBF_IrFux3v7zXLDZwx7HYYwqw3H69Y0y4K8tm1OnLVNA4wB_hR1Y1aaWwOGAQiZnZVdSc5yDwDPCU9KtNXHniBvsMGRLjHBp8qALRwXi3vJZTYIyR7_lQOzZmRGYNGu8YMqOEyMM0t9g_9IpBX2FjFfNcMkvtlUmxBLRiOV0oASuLE9-xQKZoVMlAWWupmlK67VWJwz7I9ANrtsDlGgtrL7ajD1FHe8jVoIzIxfV0uMQAML9xy45c3NZWK-ZN3xCsX7tAoOM6KjVzOYmjFPMzwpPGFf6sx0fJ6GnThiJjyPpW7ZEFRHqwTI5yjP8QLiJqSHR49jpSuhPPznTAOK0s71y2uyOeYqV6U1Pxdb0lGiWqQAt2DSjZUkIrYE6r8vL9qaHRmPlBbHvAGGrCLJj9Im33l-vqI2aD7Mw2RGxm_mFqKMDdZ85adzvVznZtSqP4emD5raxfa757Ht-DmMdAyppzNTKC-yiUqjuwLPvMkUgU9SxbKVDYctAqeE0OJZudMMmVGlpjsRfeNbLda_VAoSq1onw2VaUZg-VZ1iGYCF0I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
من به ایران اعتماد ندارم. من آخرین کسی هستم که به ایران اعتماد می‌کند. آن‌ها مدام به من دروغ گفته‌اند.
ما در حال حاضر کنترل کامل تنگه هرمز را در اختیار داریم. آن‌ها کنترلی ندارند؛ ما کنترل کامل داریم. آنجا در اختیار ماست.
و شاید زمانی آن‌ها دست به کاری بزنند و آن‌وقت نابود خواهند شد. اما فعلاً در موقعیت بسیار خوبی قرار داریم.
ما با کشوری سروکار داریم که ۵۰ سال قلدرِ خاورمیانه بوده است. اگر دقیق‌تر حساب کنید، در واقع ۵۱ سال می‌شود، مگر نه؟ ما چهار سال بود که می‌گفتیم ۴۷ سال؛ و حالا دیگر آن‌ها قلدرِ خاورمیانه نیستند.
🔴
ترامپ درباره تغییر هواپیما در آنکارا:
این موضوع صرفاً به «سرویس مخفی» (تیم حفاظت) مربوط می‌شود. من فقط از تصمیم آن‌ها پیروی می‌کنم؛ بنابراین تابع نظر سرویس مخفی و ارتش هستم.
آن‌ها می‌خواستند که من با پروازی دیگر و هواپیمایی متفاوت سفر کنم ــ که از نظر ایمنی تفاوتی نداشت ــ اما چون خواستار انجام این کار بودند، من هم پذیرفتم. من هر چه آن‌ها بگویند را انجام می‌دهم.
گمان می‌کنم تهدیدی وجود داشت؛ البته من خیلی پیگیر جزئیات آن نشدم. من با تهدیدهای زیادی مواجه می‌شوم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/69923" target="_blank">📅 09:01 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69922">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/69922" target="_blank">📅 01:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69921">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=IMji__YcFJlviLGTI_s5j7bEjpZ5-2ZstFa9XPTpc8mj2gnY_yYHf3lkxbxZXFrex3F5s50PcMX-JgQ9bUJ1h9HFJS2qUbg3IzHOSt343eblKxTMmgP8Mt1LpsQVHQ51iw7S9DTvbvIfXnI2EacAlDOl9mFyp3LljYHywsMCpVtSIsszw4gH2cv7hRjm4DqUR-K-wn0bvKFj3I0I4isu6Mz5TdzTGU1a-b8uCE4Xc68g_LT53MX-EFNCMSwdpXYkZtWX1gpI9xZLhisOrwdFa0_ds4i4ZFpQILrbh8Q9djPen1vFu7Ic0Q2u28bNxYtTKTp6kFkk2RW2rTdi3W7TaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=IMji__YcFJlviLGTI_s5j7bEjpZ5-2ZstFa9XPTpc8mj2gnY_yYHf3lkxbxZXFrex3F5s50PcMX-JgQ9bUJ1h9HFJS2qUbg3IzHOSt343eblKxTMmgP8Mt1LpsQVHQ51iw7S9DTvbvIfXnI2EacAlDOl9mFyp3LljYHywsMCpVtSIsszw4gH2cv7hRjm4DqUR-K-wn0bvKFj3I0I4isu6Mz5TdzTGU1a-b8uCE4Xc68g_LT53MX-EFNCMSwdpXYkZtWX1gpI9xZLhisOrwdFa0_ds4i4ZFpQILrbh8Q9djPen1vFu7Ic0Q2u28bNxYtTKTp6kFkk2RW2rTdi3W7TaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
➕
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
a20
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/69921" target="_blank">📅 01:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69919">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0c53c5d72.mp4?token=CDjHmWIMNl80RjVBGXHog3qk2fHnCf75eCwNoJVMPO-m0enE2_cSRU-eNnBjkxJ49p5v3YHFqlqFbmCuV1pFtKXj19jI_MjuJ6fIYPhlG2GRG3VRKO_3xUkSG_6Ww953IWjDzOI6Wzx17JnMe4ak9S6vxxB5nhq1x-WJw2R88p8MuKF8gp0ZCTyd_qIYBoyfuLZgvZ0Hu6TlYo5Ajn3tV0Mti-ubXYrUzzKOUC7vFDV6t2MrsINWwVzh8djrDB6ZxGeEccGx4II5Fw-vHPEvbiQCxWqr85iJVTP4Enyi4iUFgUaS6f903FVGebJEN0tUs8lETYoGf9TWbClrEWt8nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0c53c5d72.mp4?token=CDjHmWIMNl80RjVBGXHog3qk2fHnCf75eCwNoJVMPO-m0enE2_cSRU-eNnBjkxJ49p5v3YHFqlqFbmCuV1pFtKXj19jI_MjuJ6fIYPhlG2GRG3VRKO_3xUkSG_6Ww953IWjDzOI6Wzx17JnMe4ak9S6vxxB5nhq1x-WJw2R88p8MuKF8gp0ZCTyd_qIYBoyfuLZgvZ0Hu6TlYo5Ajn3tV0Mti-ubXYrUzzKOUC7vFDV6t2MrsINWwVzh8djrDB6ZxGeEccGx4II5Fw-vHPEvbiQCxWqr85iJVTP4Enyi4iUFgUaS6f903FVGebJEN0tUs8lETYoGf9TWbClrEWt8nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی یک مخزن در اربیل عراق
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/69919" target="_blank">📅 01:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69918">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c665ef2ed.mp4?token=BGLhLE2EfDQ3At4NXmIT0pJdECfDDvlo32bLKCbPcCl2cW90h2ZbZh0c2Vuo3As_LNQhZQe8LWwSoLhNNJGDj6a7deEFYhNeWASwJH3cF8QBXudOGrf7m3V3NmCcPPyiowZt4nVv5I9yXN2bcrNr0zBqBaFLOIXZAxQL4j7v6P0wmJGn_-nirNDx00OZhTnuRGzGXZ8Mx6k1reRYTxH3owDLNQ-FczLx197y44_A7SFqO4ZX2CQf0tYktrzp-PEw8KAwCOWGS8Ils_-42r3eQVSef8hSMKtGuzTk-0Lb7it7dKtamxZ3kVPdF38YAwDEpZapsEd9MR3fwW0CoOvgfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c665ef2ed.mp4?token=BGLhLE2EfDQ3At4NXmIT0pJdECfDDvlo32bLKCbPcCl2cW90h2ZbZh0c2Vuo3As_LNQhZQe8LWwSoLhNNJGDj6a7deEFYhNeWASwJH3cF8QBXudOGrf7m3V3NmCcPPyiowZt4nVv5I9yXN2bcrNr0zBqBaFLOIXZAxQL4j7v6P0wmJGn_-nirNDx00OZhTnuRGzGXZ8Mx6k1reRYTxH3owDLNQ-FczLx197y44_A7SFqO4ZX2CQf0tYktrzp-PEw8KAwCOWGS8Ils_-42r3eQVSef8hSMKtGuzTk-0Lb7it7dKtamxZ3kVPdF38YAwDEpZapsEd9MR3fwW0CoOvgfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اولین ویدیو منتشر شده از عروسی رونالدو و جورجینا:
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69918" target="_blank">📅 01:07 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69917">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d80bd3b48d.mp4?token=VJDvgNFKSgOPEGDIMbx6aUoEedqNPCh5ZzAScX9g34BsalSP9aBx0qddY1dQ6iS8965PU8KsOmHztCzy_kq89y0zJ2HRF0RTV4GNWEtMKDNvTJYa1WdWZev4kcmqF_qBfdzY9rgZO218IvtHFM3iF5Nqh_MhqTt_YlUevo-jNrDInWVx5vcPXUibcG5lHU-r_mLNjc6OmDJue-wkQW12Zg7bgiq6Z6jhqAlaB4-drmDMohmqmo55xX_SlkhFufGDJcufuBGvWKTDUI1iHingAD2bCBCdZXnH6fD5xXnHCJGEmVWtmbse8paKml54MXzGSwRUrWEL8Y1aepYuwdu49Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d80bd3b48d.mp4?token=VJDvgNFKSgOPEGDIMbx6aUoEedqNPCh5ZzAScX9g34BsalSP9aBx0qddY1dQ6iS8965PU8KsOmHztCzy_kq89y0zJ2HRF0RTV4GNWEtMKDNvTJYa1WdWZev4kcmqF_qBfdzY9rgZO218IvtHFM3iF5Nqh_MhqTt_YlUevo-jNrDInWVx5vcPXUibcG5lHU-r_mLNjc6OmDJue-wkQW12Zg7bgiq6Z6jhqAlaB4-drmDMohmqmo55xX_SlkhFufGDJcufuBGvWKTDUI1iHingAD2bCBCdZXnH6fD5xXnHCJGEmVWtmbse8paKml54MXzGSwRUrWEL8Y1aepYuwdu49Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نظر محمدرضاشاه پهلوی درباره نفوذ لابی یهود در آمریکا:
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69917" target="_blank">📅 00:21 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69916">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJELHkLyB_FIWXKu2R7vAXTSvb635MgDUc4geghaMkRoQz4Q_hkE8mU52S_Gv7FMgvIhpsKkw-9LpAc-Z69lV7LZOiNtQq8RYPBDtPcTm_EqUGkK1M70DVVmJlIL4lYJfq97A9qaYNTrJk35TwBsBOlDIuI27wN92xi2Z0XwbmVqEanQb1Rm1c3vBZYZAgI06L9jy_8uluMcGpUIeibhtcQha5l7kowrYgJbgPcX6dfv1apC2KnnujlaIxNtJKz1DhrTYMTBKTGnVkBdbeMSiA5c-SVVim-f-dmHtZKvfwUwH4JfVwdtR_O0ZBcmbL0GMy0kkJbHF4jyvBK3Lap63Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رونالدو و بانو جورجینا رسماً ازدواج کردن.
رونالدو هم گردن گرفت بالاخره، دیگه وقتشه تو هم گردن بگیری
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69916" target="_blank">📅 23:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69915">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d1d1d4e3c.mp4?token=UXSce1fnygdLNIyfCs7ho4gKv6JtN76hz45rOhBBOIG4E7yLIfSyyT8MY1LQ8Ydl2PR6uop00_bEj3xgRh31rMlMMYMFZtviS6LXoZbGQXvzudvaysTmNP8Balinw68Wb20-7c1pLJ117V3ubTGR08wtyLIaiLq4DLDfUou5CjArerpicL23jXt87RUImyOSkmm0KDG9wp7WWMCJDpmA98DvNJeDVBMZhNRfQ_BvkyELU-mbtAOQt94YtlNQfx4W5Wfr5aM7muG78qMgiA4yPj-iCjWmO1no7f1_pkWue-1d0C9_DjlGj8_7PtsV3co9LmHuYGKD0JITwTlop6BmFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d1d1d4e3c.mp4?token=UXSce1fnygdLNIyfCs7ho4gKv6JtN76hz45rOhBBOIG4E7yLIfSyyT8MY1LQ8Ydl2PR6uop00_bEj3xgRh31rMlMMYMFZtviS6LXoZbGQXvzudvaysTmNP8Balinw68Wb20-7c1pLJ117V3ubTGR08wtyLIaiLq4DLDfUou5CjArerpicL23jXt87RUImyOSkmm0KDG9wp7WWMCJDpmA98DvNJeDVBMZhNRfQ_BvkyELU-mbtAOQt94YtlNQfx4W5Wfr5aM7muG78qMgiA4yPj-iCjWmO1no7f1_pkWue-1d0C9_DjlGj8_7PtsV3co9LmHuYGKD0JITwTlop6BmFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
روحانی:
صدام پس از کویت به دنبال عربستان و امارات بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69915" target="_blank">📅 23:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69914">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🇺🇸
سنتکام اعلام کرد نیروهای ایالات متحده از زمان تقویت محاصره بنادر ایران، ۵۵ کشتی تجاری را بازگرداندند، ۳ کشتی را غیرفعال کردند و برای اطمینان از رعایت مقررات، ۲ کشتی را بازرسی کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69914" target="_blank">📅 22:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69913">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaTDaFlrweW6jENPOUEmp_UQ1uByyOCbOriYgyxPfrv6_vtLZEEBeDJ_NgMMAOx3q-7rCAk4LKH07P5t3R_ywK0QjG7_nOHmOqlTrp8pN7khskWyPR7s1eyO2o6nMUUDAO22SV-WzLVDSHrTPWKSUrj9pFHVyxx0Gqv6neQgC3CBrSRtgJ7tc-4zbB8oqqLJCMaUCSuYuxEas4EbjWdK8ooemk0yVgP7xchx-mhv4wsbvZCiu6llwp54ELZx975WtEMZutNuCN6T-xV1BLkZCR94zUWYisRK8qipKvezptaYn83i1DuyEtt518r0i1K_jTl0MMG7030VH5OjKQBRjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
📰
وال استریت ژورنال:اسرائیل دولت ترامپ را در جریان اطلاعاتی قرار داد که نشان می‌داد توطئه‌ای احتمالی برای هدف قرار دادن هواپیمای ریاست جمهوری با موشک‌های زمین به هوای دوش‌پرتاب وجود دارد.
مقامات امنیتی ایالات متحده متعاقباً پس از اجلاس ناتو، رئیس جمهور ترامپ را با استفاده از یک کامیون پذیرایی فرودگاهی در آنکارا به یک هواپیمای نظامی جداگانه منتقل کردند، در حالی که مارکو روبیو، وزیر امور خارجه، دیگر مقامات ارشد و خبرنگاران به عنوان بخشی از یک عملیات فریب در هواپیمای ریاست جمهوری باقی ماندند.
در نهایت هیچ موشکی شلیک نشد و هنوز مشخص نیست که تهدید گزارش شده چقدر معتبر بوده است. این عملیات اولین باری بود که چنین اقدام فریب‌آمیزی در دوران ریاست جمهوری ترامپ استفاده می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69913" target="_blank">📅 22:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69912">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f811c57f.mp4?token=DptFxnPWfJlHOGpCqO7KcFw-a_6851Tv6JiuggyYM22atizUhqM4TQW3u70O6gAJR18TWdj3UBCktzT06mp64CgnUB8ZFlWK454mEd8AGBUVxUn_M1ek5bjj1bZ3nVeXNgFFTQ0SiRbcqxwkB-hGt9Yl2s5smFFv_D9iLXvWfNtJa1SlH-fmmpC23ATjprHtf5uBacAenNMYeMGa_7jGNUVPnaq4bTva6k8upxQ7B4F5KJoasB065P83pG6LO641uLSJVkS3LzWQaGinzGRkvTAw8EcnAt-7YLJNw1kwIqbk3Lex6jKrZNHyMp6PyUA1krMXQw2yIJAANpfWek3pRU3J3n3AWUzIswL4vQuBor_KrZ_D9ddw48Zs0idRRVixQbBSYtEclPyiLB2Mu7tcw1Zkx5NgL-YuuJL1tM7oEC8nAqLzTK95_fS8DKB4q1ReH_23qjpx1zndRHyvdeUFSwz4cU8rbnjQGCncL7nxFxOOZDro88j4YBEKQmPmlANdC3SYRjaEfegvPQ9QBgFQztSAskyX0ucXVFQvURLBYfGckatn1fk9UPNdGKWqQXLUp9L7xED5u20ecM2w1Egq8buDvihclF1kMPt72Yp_9_UOFJRFVPqLc4assS30eQlDnKjft8HGB-rYybBzKafQ16d80L5JBUzoOz_OH0xX2Oo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f811c57f.mp4?token=DptFxnPWfJlHOGpCqO7KcFw-a_6851Tv6JiuggyYM22atizUhqM4TQW3u70O6gAJR18TWdj3UBCktzT06mp64CgnUB8ZFlWK454mEd8AGBUVxUn_M1ek5bjj1bZ3nVeXNgFFTQ0SiRbcqxwkB-hGt9Yl2s5smFFv_D9iLXvWfNtJa1SlH-fmmpC23ATjprHtf5uBacAenNMYeMGa_7jGNUVPnaq4bTva6k8upxQ7B4F5KJoasB065P83pG6LO641uLSJVkS3LzWQaGinzGRkvTAw8EcnAt-7YLJNw1kwIqbk3Lex6jKrZNHyMp6PyUA1krMXQw2yIJAANpfWek3pRU3J3n3AWUzIswL4vQuBor_KrZ_D9ddw48Zs0idRRVixQbBSYtEclPyiLB2Mu7tcw1Zkx5NgL-YuuJL1tM7oEC8nAqLzTK95_fS8DKB4q1ReH_23qjpx1zndRHyvdeUFSwz4cU8rbnjQGCncL7nxFxOOZDro88j4YBEKQmPmlANdC3SYRjaEfegvPQ9QBgFQztSAskyX0ucXVFQvURLBYfGckatn1fk9UPNdGKWqQXLUp9L7xED5u20ecM2w1Egq8buDvihclF1kMPt72Yp_9_UOFJRFVPqLc4assS30eQlDnKjft8HGB-rYybBzKafQ16d80L5JBUzoOz_OH0xX2Oo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
پرواز بالگرد آپاچی۶۴ آمریکایی در نزدیکی قشم
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69912" target="_blank">📅 21:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69908">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b1WUNPlFdZkM_HjxFoT4VJwk6WC-nMklk980PxhF44Lp98852B7wOjtg0cyZOXiAPyR96T_4p1CPVTail4-AksO2XzuNN2EMHgnRHrCvUx34ICnDeYXDsjv3CS2ltHbf5Rra_WQlXp2Zvo7uzj4BKaoJaA37dKnx8SEPlEwYutd18X-BEa3ptkkdDkgKlcdij2whV7efqT8Xvl2vMlY5Dyt7hsrq2njy4mR5OAg2WCWzVt3jMvi6GQ7seszFDXjrB0bj-nyXVKXdC9erPSsBjddnXprIP_MTu8hJdz7gN2A5Rd3LO2BWGjSF_ROzmoxj1DWc9FWYG5_ZsOsOL1Va1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qv80zNPmg5Ubj5fh6i04tpv-NWRq7h-daejE0gA7SRMLOS5hiLJ0oao5mqbBxlYogGyd908WCz6YJ9EBjQ6-N1HCEkBL6kS3mQxwFeFiC9jUNMDip8Satn4ed7BsRHBuPccizckY-TUOrhKFWrfnW659FJQe3RItgsWgQ2KXMt_Hn2I_L3g-yNOhTs34VsQ5xmfF-lsUpIayGQ1LxNt7wzYUOmXpMCsJsVF-JqJldJn_TF8_8tIwPZk2G6x1u6KJ_WwiSZs6xCx1ZGJk1tIo3OZTMQkuTQB-KOWDEcN8aPImMc1WHOrv48tmI9LQVX2U_mAuQ-L9473iH9gJMwAvqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RDFYdFDC5tvxqyGFJ4IxEP7CRhvvm8d2QKmWlfewvIk_iNWgdjlEPwRROu8H5RAfHwCic25IGbJmCyR9amklNEvnuaA2cujRaXDHihkVxASUCG_HfWwiz85vA4bGipIiRwexsbhzpprgWCTNYDoiuntbvaR7HQRz0nELOHC_g-6XEfabbpQqz3J4xoKcKr8Op2ichIy4-hiUVg-1ANgoC987Ko01YGxPHI7kv9Fun2AngP-8bOyJmGAX6ABIvCxtfE7X_0QgUEhtFp8fDnnhF7j1IS-UUYNrvqCJRN2ViITW0an-Dw1wpJRk1XkQpM8cBrt-ohIKSw7RODv3djPlLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbbe5c4282.mp4?token=hyjBIDsDZV9N4eP4HsAYvkpjjmFkYKHdfszekCOV9L-PVzysureZnvQVw3ztKUMfUGkK-gcFEeg4IWpqCTLeTn5nQcU9-7HVQ0qlp5-lY2dSLXTIzMRFfe0Bq88Ix0HlkTd8Ntd_cH_RA0hTHVlYDhpzdWc4nTvjbaEKNHto-jF7i3erl09nckZhnB2WOgPhhZw60ETyQvRMJKMZlQ_d8RGEBBXZ4cGyf4bTI7LHq8L09YWfDr6mc1s3WBr_7r_FydAuPf8j8n4r8xcFVRlppCpFPgXJQaoRrnkvYjjIpws2ZghQTX0JhNMDItH6rLEulmI4aGoswp8B3cOM3-uC-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbbe5c4282.mp4?token=hyjBIDsDZV9N4eP4HsAYvkpjjmFkYKHdfszekCOV9L-PVzysureZnvQVw3ztKUMfUGkK-gcFEeg4IWpqCTLeTn5nQcU9-7HVQ0qlp5-lY2dSLXTIzMRFfe0Bq88Ix0HlkTd8Ntd_cH_RA0hTHVlYDhpzdWc4nTvjbaEKNHto-jF7i3erl09nckZhnB2WOgPhhZw60ETyQvRMJKMZlQ_d8RGEBBXZ4cGyf4bTI7LHq8L09YWfDr6mc1s3WBr_7r_FydAuPf8j8n4r8xcFVRlppCpFPgXJQaoRrnkvYjjIpws2ZghQTX0JhNMDItH6rLEulmI4aGoswp8B3cOM3-uC-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دریک، از بزرگترین خواننده‌های دنیا؛  با 140 میلیون فالور و ثروت 250 میلیون دلاری [50 هزار میلیاردی]  وقتی ممه‌های بزرگ یه دخترو دید، نتونست تحمل کنه و براش هاپ هاپ کرد  @News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69908" target="_blank">📅 20:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69907">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bcf8b7227.mp4?token=GDAb3PLrKQW5fhvI-pEU-NyOTkmpnSSoDgVQg1y-TLTw0ZRo3MTsV8QU0gSbsLjpVLPJ9Dxoa-pLs5FVgfpDzSPtdBzkbIHs1Y0TS7UXYBW-Q2lJ58a9wqvTBVByd_K2RtJAgJfjCkclEupTK_qAj1XzVLa1K2kK9CBo6D7Ri8Y1vEXYZMsuPmYmaANi79KFOwtnRph_tTECIRdmCZ6eh3gO9PnP2YFZWC9adb9v6ds48RUtBGrah3Y1dBNmehmr1LHR8FNj5HuKTsXRU_DNVT5A-X_GOBKl1euuEMKssrVnr6ws-dcChlm4_jm9N5yzZO_qv4iD0BPYBku688Pnkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bcf8b7227.mp4?token=GDAb3PLrKQW5fhvI-pEU-NyOTkmpnSSoDgVQg1y-TLTw0ZRo3MTsV8QU0gSbsLjpVLPJ9Dxoa-pLs5FVgfpDzSPtdBzkbIHs1Y0TS7UXYBW-Q2lJ58a9wqvTBVByd_K2RtJAgJfjCkclEupTK_qAj1XzVLa1K2kK9CBo6D7Ri8Y1vEXYZMsuPmYmaANi79KFOwtnRph_tTECIRdmCZ6eh3gO9PnP2YFZWC9adb9v6ds48RUtBGrah3Y1dBNmehmr1LHR8FNj5HuKTsXRU_DNVT5A-X_GOBKl1euuEMKssrVnr6ws-dcChlm4_jm9N5yzZO_qv4iD0BPYBku688Pnkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
رامین رضاییان:ما خودمون از عمد به بلژیک گل نزدیم و تیم بلژیکو نبردیم.
🔴
چرا؟دلیلش:
جلوی بلژیک شما دیدید مهدی طارمی یکاری کرد تیمه ده نفره بشه.
مهدی بخاطر تیم به بلژیک گل نزد.
من باهاش صحبت کردم داداش چرا نزدی گفت داداش اگه گلو میزدیم فشار وحشتناک میاورن و جبران میکردن، حقم داشت مهدی
🧠
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69907" target="_blank">📅 20:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69906">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🇮🇷
فیلد مارشال محسن رضایی دبیر عالی شورای امنیت ملی:
آمریکا باید جنگ رو پایان بده و خسارات رو بپردازه.
به هیچ وجه کوتاه نخواهیم آمد.
تمامی جنگ ها باید در کل جبهه مقاومت پایان یابد چون شرط اصلیه.
شروط دیگر را نیز از طریق میانجی ها گفتیم به اونا ک باید بهش عمل بکنن.
توافق با عمان ربطی به باز شدن تنگه هرمز نداره.
پول های بلوکه شده باید آزاد بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69906" target="_blank">📅 20:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69905">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی We pari همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/69905" target="_blank">📅 20:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69904">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/si5K2npmDngoSkXO-2TisKJqVVaT4L5pFjMwbVHLj8V3xqVYCOMMHfTvgih9AA61O0LaVHJIj2JImoBE4XKuRzqeU7T0RozD_sIPCiim9duSG9ICESNIIx7tCDQlibe3ze6dtS2RzneRNId6ZMxxGAUGNJeitxv5HyWvr8wDLdn3lqFSwqPi0_LVDwK6KEY8CZ63OeogCKwbipCHFg6_I4swszxGX-IZdKAqqu18ovOB9VvzfU3zGS37m7emwAsU-Z1_o7e4TlxI9xsCbV-wgV_7a3uSl186JE1a7ZQmK8MF_XNkVaHzh4l9nVdKwlokVfWww0tKm-5hTzwhK3Qz3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی
We pari
همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر
💖
واریز اول و هر شنبه 2 برابر شارژ میشین
💖
تسویه حساب سریع و بدون احراز
💖
دارای مجوز رسمی Anjuan و curacao
💖
فعالیت بدون تخلف در کشورهای مختلف دنیا
💖
بازگشت بخشی از باخت به صورت هفتگی
💖
اسپانسر سوپر  لیگ ترکیه
😃
😃
😃
😃
👑
کد هدیه ثبت نام:GG007
👑
ادرس سایت:
http://til.ac/z5jcpGT
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا،کشورهای اسیایی
👑
دانلود اپلیکیشن اندروید
➡️
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/69904" target="_blank">📅 20:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69903">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e58dcb779.mp4?token=lBV4ToCv3YuwX4SYEqBs8ci3i00nrf4N28m1W5VKRrl9W8kvtCwG7-P5FjmEwmWybXgeWe0zX3xAxZ69RR3bvgja2kG7aoo10R3tx_LXft_4DYA0zT8vtWrQbvaVO9qC9ZJ3RpquQJ-AdpBNgwRVysUrQnEwKUtayVKPlccFcftMCa4-o2Xy3UX97C6ZBwYrMJkzwmvbKLmEZ0LbtNwNqwDkCxfgutpLeivFFFQzpvVNY1ewY3oFiQSGAqNT4BdHSYXbqpjb09TEkzPdyFDLgKa-RuIu-cobGPPS6Tgu5tFmrtBSa5z5TIp4ODZjvodadUP_q1-vx4I_P09qhY_aFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e58dcb779.mp4?token=lBV4ToCv3YuwX4SYEqBs8ci3i00nrf4N28m1W5VKRrl9W8kvtCwG7-P5FjmEwmWybXgeWe0zX3xAxZ69RR3bvgja2kG7aoo10R3tx_LXft_4DYA0zT8vtWrQbvaVO9qC9ZJ3RpquQJ-AdpBNgwRVysUrQnEwKUtayVKPlccFcftMCa4-o2Xy3UX97C6ZBwYrMJkzwmvbKLmEZ0LbtNwNqwDkCxfgutpLeivFFFQzpvVNY1ewY3oFiQSGAqNT4BdHSYXbqpjb09TEkzPdyFDLgKa-RuIu-cobGPPS6Tgu5tFmrtBSa5z5TIp4ODZjvodadUP_q1-vx4I_P09qhY_aFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
روایت تلخ یه فرد نابینا:
اینکه من نابینام به عقیده پدرم کارمایی هست که دارم بخاطر کاراهای اون پس میدم.
پدرم وقتی جوون بود نابیناهارو مسخره میکرد و بهشون میخندید.
مثلا پدرم بهشون میگفت بیاید جلو بیاید جلو و وقتی میومدن میفتادن تو چاه و پدرم مثل خر بهشون میخندید.
پدرم بهم گفت من این کارارو وقتی جوون بودم انجام میدادم.بعدا وقتی تو دنیا اومدی دیدم نابینا شدی و این دلیلش کارمایی هست که من باید پس بدم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/69903" target="_blank">📅 19:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69902">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfb370d6c1.mp4?token=HzYiZY1sqVLIqKjNol8p-jllT7FckJ2lHwXEzmWLcHOLRSOeDaOuczem-opuAtPZ8TDrlBtRgXSW4JOMEDQIez7_a-rIvTaGOo4iuHGsyvRK0Zx9RVzga0dqV2djTaahIRiwSGaZ9YULIgiZCLQ1q_2zxilmTaXiVw0yQj4jD5PaeYX-olWAOXxuLA8D7muVNA6uDBXO1XLcUP3vcfS5TmayBD1ZTXxu0E-nYjxJffXI0j8w8ccFKNnvbSYsNm3me7JFljLQW4fNDLe-PezoViahTyJefPi4FoDxQiwnNXESpqsRz16MM_UMb7ojFaoQAfw7qUAqlxONBJdsPVtA9RNkYmjqyb-EhsrsO5rGUz1hunQ2lSC5JoYMJa9BSvDqRfFmaYV7A-Zm8Mf4FkDJalojnpzJyvR-SHxgGy6HI0S_sKNJYf_Y7MVIynFE8aTe8r3pyZzvdq1v7XuvUpWqQKt9HlU3oKNHU3aKAXUJ3Eho2pfmsmFF6katENitvj2x0NJPMtcEskLzjBFbWNPQvrK5Xpg9_SbOalpUMzQFnhV7rQFkHe9wRkKBw5VPPunrO-JtfenjFTPKX1pwtaq595fnr0OdfQHzmuL6xEfAWW7P0Qrw22nCYm5T-WYD8RkENOv9d-IACPVBTiWslbnWzpwQBKqAKe7R11CNMieIopk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfb370d6c1.mp4?token=HzYiZY1sqVLIqKjNol8p-jllT7FckJ2lHwXEzmWLcHOLRSOeDaOuczem-opuAtPZ8TDrlBtRgXSW4JOMEDQIez7_a-rIvTaGOo4iuHGsyvRK0Zx9RVzga0dqV2djTaahIRiwSGaZ9YULIgiZCLQ1q_2zxilmTaXiVw0yQj4jD5PaeYX-olWAOXxuLA8D7muVNA6uDBXO1XLcUP3vcfS5TmayBD1ZTXxu0E-nYjxJffXI0j8w8ccFKNnvbSYsNm3me7JFljLQW4fNDLe-PezoViahTyJefPi4FoDxQiwnNXESpqsRz16MM_UMb7ojFaoQAfw7qUAqlxONBJdsPVtA9RNkYmjqyb-EhsrsO5rGUz1hunQ2lSC5JoYMJa9BSvDqRfFmaYV7A-Zm8Mf4FkDJalojnpzJyvR-SHxgGy6HI0S_sKNJYf_Y7MVIynFE8aTe8r3pyZzvdq1v7XuvUpWqQKt9HlU3oKNHU3aKAXUJ3Eho2pfmsmFF6katENitvj2x0NJPMtcEskLzjBFbWNPQvrK5Xpg9_SbOalpUMzQFnhV7rQFkHe9wRkKBw5VPPunrO-JtfenjFTPKX1pwtaq595fnr0OdfQHzmuL6xEfAWW7P0Qrw22nCYm5T-WYD8RkENOv9d-IACPVBTiWslbnWzpwQBKqAKe7R11CNMieIopk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدیو ای از لحظه حمله آمریکا به پل B1 کرج:
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/69902" target="_blank">📅 19:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69901">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
🇺🇸
پرزیدنت ترامپ:از شیوه مذاکراتی ایران ناامیدیم.
ایرانی‌ها بازی فریبکارانه‌ای با ما در پیش گرفته‌اند: در اتاق‌های مذاکره موافقت می‌کنند، اما در رسانه‌ها [توافق‌ها را] رد می‌کنند.
ما از هیچ کمبودی در ذخایر موشکی رنج نمی‌بریم.
ما می‌توانیم با نیرویی عظیم به ایران ضربه بزنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/69901" target="_blank">📅 18:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69900">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24b53c400c.mp4?token=C5K5dCv8f60ZvPFjTEKnqEsQvziVup1Qdfxq672zG64rnkyLzNVOdMTo9Kn52Ba4AMPckLFFywANo9s6XdbVX11EVgbka0hsG_AWk2mscR1XeK2Hsin2acR9hLdeFS3W5Tzwwu_QeK1FrzUrNosMa4ubBNVIPu_6vYYvH42Cbsoai-AJLDbIhIs5nJGfsht_7I7aSTjVBPUzd3nN_vr-HNEqx5J8uAsaVwUABOJQxiS1y_jpKYbdQsoGwTjbLDQ7eTkRgiG4BN5VVRO85B-bCwmQr5JkHX72PHE1Op_opIbPwopnZ56VrhzxRCKqiq4SgveppQWlD__cuznUL2zAUwvBACeV9sDa4RBP0WxaMpWi4HGvTyywcKcGlUxMfA_lXtGFXpLMUXIwNtexJ659jpFSXD4aN7qUW6nQSHFbOUSESiJH_79__fzBaIOw_vQEVdKwwiVJQjigQf2BdbB8ee4hic7GR6fq4Y2um7-f22v-avIjg1MdL0dxe8sm-N-iiqerwqlFvJNR84wjVThBp8zAxOdy58Qox5KTbFFpkdXnotnFKXuFj0jDtYf-POD1x-LBTSz5n2xt3pLkULV3qHELdEM6VN8tDfOfHW0_hmiMucT0gRLHSYOjdh8Y9hxwbb4701RAjVuhlxFwfLGC16ry2D8VntHD0xMRZTgtGLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24b53c400c.mp4?token=C5K5dCv8f60ZvPFjTEKnqEsQvziVup1Qdfxq672zG64rnkyLzNVOdMTo9Kn52Ba4AMPckLFFywANo9s6XdbVX11EVgbka0hsG_AWk2mscR1XeK2Hsin2acR9hLdeFS3W5Tzwwu_QeK1FrzUrNosMa4ubBNVIPu_6vYYvH42Cbsoai-AJLDbIhIs5nJGfsht_7I7aSTjVBPUzd3nN_vr-HNEqx5J8uAsaVwUABOJQxiS1y_jpKYbdQsoGwTjbLDQ7eTkRgiG4BN5VVRO85B-bCwmQr5JkHX72PHE1Op_opIbPwopnZ56VrhzxRCKqiq4SgveppQWlD__cuznUL2zAUwvBACeV9sDa4RBP0WxaMpWi4HGvTyywcKcGlUxMfA_lXtGFXpLMUXIwNtexJ659jpFSXD4aN7qUW6nQSHFbOUSESiJH_79__fzBaIOw_vQEVdKwwiVJQjigQf2BdbB8ee4hic7GR6fq4Y2um7-f22v-avIjg1MdL0dxe8sm-N-iiqerwqlFvJNR84wjVThBp8zAxOdy58Qox5KTbFFpkdXnotnFKXuFj0jDtYf-POD1x-LBTSz5n2xt3pLkULV3qHELdEM6VN8tDfOfHW0_hmiMucT0gRLHSYOjdh8Y9hxwbb4701RAjVuhlxFwfLGC16ry2D8VntHD0xMRZTgtGLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
رونمایی صداوسیما از «قوی‌ترین سیستم جاسوسی جهان»
تماس با پذیرش هتل عمان برای جاسوسی:
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69900" target="_blank">📅 18:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69899">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736f2f73f3.mp4?token=Fr18eSrt-8ecWO6VQxJWKwEIW8jy13hyTLRHl-e-BMq3rtIrWI47dfo77R77VWYAgTyCsIozQe1Ml260dBQlPPMGLQpAOR7DOX2lEINpk9jiY9-9fw4qdEqvGtPJkUyPFW_fkJylAq4fG4qYIgHQ5anWHrCga5kyBfrNLw3voQYk4KPannwJD1xpnepGBnYauyUS0p-T_oZ6WSi3MtdB76fgdTD_93Y5m7WV2wkWbwd7HEx19CHim9UbLPQEc3hIdUgmDfVtRlW-NohU3rEMjTpnQh01UcWqHVercnIZ3V4DmxjmqPWBXsQweU7ta3BDOPQIE7vjlGhSBa40CU6eyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736f2f73f3.mp4?token=Fr18eSrt-8ecWO6VQxJWKwEIW8jy13hyTLRHl-e-BMq3rtIrWI47dfo77R77VWYAgTyCsIozQe1Ml260dBQlPPMGLQpAOR7DOX2lEINpk9jiY9-9fw4qdEqvGtPJkUyPFW_fkJylAq4fG4qYIgHQ5anWHrCga5kyBfrNLw3voQYk4KPannwJD1xpnepGBnYauyUS0p-T_oZ6WSi3MtdB76fgdTD_93Y5m7WV2wkWbwd7HEx19CHim9UbLPQEc3hIdUgmDfVtRlW-NohU3rEMjTpnQh01UcWqHVercnIZ3V4DmxjmqPWBXsQweU7ta3BDOPQIE7vjlGhSBa40CU6eyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
مشاور قالیباف، مجید شاکری:
هیچ کس نمی‌تواند با ترامپ به توافقی برسد.
این تیم فعلی با هیچ کس به توافقی نرسیده است.
او هم با ما به توافقی نخواهد رسید.
همه فقط در تلاش هستند تا "تحمل کنند و صبر کنند" تا پایان این دوره.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69899" target="_blank">📅 18:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69898">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c85bc1feb.mp4?token=dzUEO3U2pBpEr0vlRc_K1HKdatV-CorGbQzeyoVbr8RilpPXaPXnGW_mbkv79tmQsoryjs5S80u5xgCh0NVcQ69rt8HQXLBF-0WEsAY8mMFWqEsuZwvDSDkrCytXbWtp4GcTUncathZb5ijOq7WME75S2unX-HCrgAsApYTXDVd-OTuMU5ZiypHTEouqTrXi8YJL4ZvstabeBCX3vSreS4YncEfazekfkYigLL9MWi4SZ_jlUwC-ZETcO-Dun5Bnesau45aLPr_lLym8Q0vEgMtTIZyQOBEUmPLGYiBh7UTiwOuvWIATcrUybNfSkKjOPd1bx5NaFiexp123quREvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c85bc1feb.mp4?token=dzUEO3U2pBpEr0vlRc_K1HKdatV-CorGbQzeyoVbr8RilpPXaPXnGW_mbkv79tmQsoryjs5S80u5xgCh0NVcQ69rt8HQXLBF-0WEsAY8mMFWqEsuZwvDSDkrCytXbWtp4GcTUncathZb5ijOq7WME75S2unX-HCrgAsApYTXDVd-OTuMU5ZiypHTEouqTrXi8YJL4ZvstabeBCX3vSreS4YncEfazekfkYigLL9MWi4SZ_jlUwC-ZETcO-Dun5Bnesau45aLPr_lLym8Q0vEgMtTIZyQOBEUmPLGYiBh7UTiwOuvWIATcrUybNfSkKjOPd1bx5NaFiexp123quREvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
نیروهای روسی تلاش کردند تا یک گروه بزرگ از خودروهای سبک را در یک نقطه تجمع، تقریباً 20 کیلومتر پشت خط مقدم در منطقه دونتسک، مستقر کنند.
همانطور که در اینجا مشاهده می‌شود، پهپادهای تهاجمی کوچک اوکراینی این گروه را مورد حمله قرار دادند و ضربات متعددی به آن وارد کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/69898" target="_blank">📅 18:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69895">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8c9ff38ed.mp4?token=lPu7GUcIFMWRpxRITLehSIKfW6ksi7l0QCk9d3x7ywLp0HZyZtvDyZGLSV_UOzIBoLSOvfwmpoTx0Jw7iCzmYw64IPAow1F8zAwt3_c6yQc25uAMrH5BIJF6ES2d03DOrlvhrmO1fXO-mWXW7JEaOte71uCxV7AEJBlKVQT-j3Y3gBrD6IIyay8J43LhI2chfAW7AWRsJk6p2qFmVKzggv1jEwtNWa5wwYPH7STU5RKRUjhkbk2LTr4AJrAJQMaZqpI1hE2FgJ7O0FuTZNIIlZ8cjN1NdXrSvgDlnONWvpk9ovk4fs1UPhxtSTL7U0rYLC61OGO1lKSpTB23ofjPow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8c9ff38ed.mp4?token=lPu7GUcIFMWRpxRITLehSIKfW6ksi7l0QCk9d3x7ywLp0HZyZtvDyZGLSV_UOzIBoLSOvfwmpoTx0Jw7iCzmYw64IPAow1F8zAwt3_c6yQc25uAMrH5BIJF6ES2d03DOrlvhrmO1fXO-mWXW7JEaOte71uCxV7AEJBlKVQT-j3Y3gBrD6IIyay8J43LhI2chfAW7AWRsJk6p2qFmVKzggv1jEwtNWa5wwYPH7STU5RKRUjhkbk2LTr4AJrAJQMaZqpI1hE2FgJ7O0FuTZNIIlZ8cjN1NdXrSvgDlnONWvpk9ovk4fs1UPhxtSTL7U0rYLC61OGO1lKSpTB23ofjPow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سامانه‌های پدافند هوایی «اونجر» (Avenger) و رادارهای «سنتینل» (Sentinel) ارتش ایالات متحده در نزدیکی محل بازی گلف ترامپ مستقر شدند تا پوشش حفاظتی کوتاه‌بردی در برابر پهپادها، هواپیماها و موشک‌های کروز فراهم کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/69895" target="_blank">📅 17:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69894">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f4acff5e.mp4?token=gA7iENkfM9tF17WNCrCsyZeITH1stldmNNt1cZv_Uwn_2iB--LfLSqOteNaOdUAuNgawKAGZGcO16qQ42zTXeiB4thzMCOPMhIOcZIuhBM0hSGIJoEmFm30a0wnQUyTUFE_1uVl-uJg5gC-KZgJUVdM_d239PRgf_Smq_c-wrhpMuRWV_Na14LLzopySK6VYkiBD4oazCZMXcnGUTtY0gdoiFC6xv4N-Z6gdNwfEaoxcDfXGRFEHtiaVgL1Q_lzyF16NxqbE7TNC8kg93nyvhqq5qOrjKirQY1dn4k7mm8iQn7EL6v142dvEvuIQq1yOMz6n2mN8jiy0AE7v38XT9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f4acff5e.mp4?token=gA7iENkfM9tF17WNCrCsyZeITH1stldmNNt1cZv_Uwn_2iB--LfLSqOteNaOdUAuNgawKAGZGcO16qQ42zTXeiB4thzMCOPMhIOcZIuhBM0hSGIJoEmFm30a0wnQUyTUFE_1uVl-uJg5gC-KZgJUVdM_d239PRgf_Smq_c-wrhpMuRWV_Na14LLzopySK6VYkiBD4oazCZMXcnGUTtY0gdoiFC6xv4N-Z6gdNwfEaoxcDfXGRFEHtiaVgL1Q_lzyF16NxqbE7TNC8kg93nyvhqq5qOrjKirQY1dn4k7mm8iQn7EL6v142dvEvuIQq1yOMz6n2mN8jiy0AE7v38XT9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
دیشب توی تهران، یه نفر با یه دست رانندگی میکرد و با یه دست فیلم سوپر میدید
😐
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69894" target="_blank">📅 17:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69893">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDNB0EVzqzqMfUgalQ6xd2FlmnlFxdRgd2zmUovzqh8VwvDwOORoxM9PEsN5V_bpgnk1Hp1G5j8wNdGkYqf1NL9oxaejEqYFmZg4WJee2Yc-FB11V139fqA5uMg4yO-VtQ_pFWPPk3uwKFwYhHnjf6YBpgdFu7noyC8hy9MCvNZg8FMJuVAj0EXYb3M7WgBlEEdHASPG_8rCbrh4OHhW01yyGRFtWv7guKdQFKCFcSnOeiT4vbkImNFEV0bxChZVtpjKZzGceTq0e24orGjWhQ7QrAgZpqz8pcxZWYEUYlV7jTBB2S6trNN_6ah5CWvswCvI8P9aArg2uTVDKdUaBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
📰
وال‌استریت ژورنال:نیروهای آمریکایی بامداد سه‌شنبه به سوی شناوری با پرچم پاناما آتش گشودند؛ این اقدام پس از آن صورت گرفت که شناور مذکور ظاهراً تلاش کرد محاصره دریایی بنادر ایران توسط آمریکا را بشکند.
پس از آنکه خدمه این شناور هشدارهای مکرر نیروهای مسئولِ اعمالِ محاصره را نادیده گرفتند، یک بالگرد نظامی آمریکایی سکان کشتی را هدف قرار داد.
خدمه شناور در حال تلاش برای انتقال به یک کشتی غیرنظامی دیگر مشاهده شدند.
در نهایت گزارش شد که هر ۱۷ خدمه کشتی در سلامت هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69893" target="_blank">📅 16:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69892">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qFoiVr8mwLCNl-IflkS5XEfRacc-Bt2WI08SxbswHMVTMcxkRXzA_5gOUl9Gw4D8v2h1HdnyKELYgWlOqSHqwjAtenhzrmluvJqBzCpQS9bUt4CH7C6qvw0nSrjnVxgcQXbD1pJ4Ct-LHQUPpZxgkBCtaF2lYNWmm5517s7OAbxlWX_qTHBgkyA0fVPivcAWodYaaY7RNsHtHMjpJzZPjU2Ue5avs5b4yTuK9dd-qh-s1uO_UJR_dxng0bTpoSWQBiKXUoTg7kMsAZd0kqoGyRNIDvnWDwNBgLVuWRP6r2P1dYrRsjMFaWFmli_MQLeHE5qxooAp817klwCtJ_LnUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📚
#فوری
؛ زمان برگزاری کنکور مشخص شد!
صبح پنجشنبه ۲۹ مرداد : کنکور تجربی
عصر پنجشنبه ۲۹ مرداد : کنکور زبان و هنر
صبح جمعه ۳۰ مرداد : کنکور ریاضی و انسانی
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69892" target="_blank">📅 16:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69891">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62f8b2cd3c.mp4?token=EeTXxFwruAeQRK41FBLMl9THsB7YrVb3TGz-DRHsLIjyV43KFtlUDbr8CvjSIq45LHoH6dRqmEciYut-Pq_f1TaPvfXPaIUPWX_K_cxQ2OEVxK2_f7n-7AiAyggnx2pBry4JEDUiAJG2bT1jTB1Zq0ACL2g8HEsV-AEEBdHkjCCbh_zd2wW8eaZ6YDa7uS4p-2r83MQTGA7nFINy8l0bKcEnEzTOrW5Ol6q5qE5OO_cEQIled0789cdjoQI00tsd8qT2k4FR9CtoUCKsaT-__zdQ7zmlhLKWF9BNF--xMkqPsGUY9EK4ZgemcWQUgqYwuGf3EF-9jupKxZjLSjwftQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62f8b2cd3c.mp4?token=EeTXxFwruAeQRK41FBLMl9THsB7YrVb3TGz-DRHsLIjyV43KFtlUDbr8CvjSIq45LHoH6dRqmEciYut-Pq_f1TaPvfXPaIUPWX_K_cxQ2OEVxK2_f7n-7AiAyggnx2pBry4JEDUiAJG2bT1jTB1Zq0ACL2g8HEsV-AEEBdHkjCCbh_zd2wW8eaZ6YDa7uS4p-2r83MQTGA7nFINy8l0bKcEnEzTOrW5Ol6q5qE5OO_cEQIled0789cdjoQI00tsd8qT2k4FR9CtoUCKsaT-__zdQ7zmlhLKWF9BNF--xMkqPsGUY9EK4ZgemcWQUgqYwuGf3EF-9jupKxZjLSjwftQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
یه آخوند توی برنامه زنده داشت به اجرا نشدن قانون حجاب اعتراض میکرد و میگفت ملت بالای ۴هزار تا پیام دادن برام؛
بعدش گفت بزارید یکیشو رندوم براتون بخونم:
چیزی که خوند
😔
:
«آقای پفیوز احمق بیشعور حرف دهنتو بفهم»
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69891" target="_blank">📅 16:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69888">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/698b90aa95.mp4?token=XWO0cxUsuP9c5XhRkJVU0VLVQLdwc570Ij2Mz5WzHtmzbr2ZFZmjqADl6m3LO0-J9LxNm4wsZbiOnNNKXpl2Am_9ztgZ4o8xSqRpPKF-7sedQRBsT8VsqpjubjDvLzrOVt3pl4ZlUpS_nHJHCJjKu4X69WdFvbb--bVXbBUPo2XtqgQWdI_Jhs5B6dIJ4-M8A3StmKP65OXcDK8Eap20HI8D4GoXa98n3MtyA5WkjEK6lHokf-3ON6OKxeJ_b1qKq27R7G_bYBKWmdy0gNJTUqa4KlABDt_-3rCyh8VUd3CGWPRuo1nCb3OfpBCaEyWgetv5TDY8TP5kRRh76dacQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/698b90aa95.mp4?token=XWO0cxUsuP9c5XhRkJVU0VLVQLdwc570Ij2Mz5WzHtmzbr2ZFZmjqADl6m3LO0-J9LxNm4wsZbiOnNNKXpl2Am_9ztgZ4o8xSqRpPKF-7sedQRBsT8VsqpjubjDvLzrOVt3pl4ZlUpS_nHJHCJjKu4X69WdFvbb--bVXbBUPo2XtqgQWdI_Jhs5B6dIJ4-M8A3StmKP65OXcDK8Eap20HI8D4GoXa98n3MtyA5WkjEK6lHokf-3ON6OKxeJ_b1qKq27R7G_bYBKWmdy0gNJTUqa4KlABDt_-3rCyh8VUd3CGWPRuo1nCb3OfpBCaEyWgetv5TDY8TP5kRRh76dacQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترلان پروانه توی آخرین مصاحبه‌ش گفته رابطه‌ش با شروین حاجی‌پور یه اعتماد اشتباه بوده و این رابطه تموم شده.
بعد از این مصاحبه هم شروین یه موزیک منتشر کرده که خیلی‌ها معتقدن حال‌وهوای بعد از جدایی رو داره.
جالب اینجاست که اوایل رابطه‌شون شروین توی یکی از موزیک‌هاش گفته بود قراره تا به دنیا اومدن نوه‌هاشون کنار هم بمونن!
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69888" target="_blank">📅 15:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69887">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05e9aa8412.mp4?token=FhgRNzmy56ZNAJRisro6PSr49AKQz3TRm17_UByjMJ7Lgc5YWuK-y1JwLA-f7uoOQ4AuB6urszqOglzKH55lzdgaUUUTkgk8xth8Nipw-SrDSKh0k-0fDx-ocnS9ATmDfq9FPohu1z8EAxGZBafDD21a6ErSqW3NL-DVOubFp3sDkbw_UDndd4CUR0qUXzDtKhEG23jwUlzG01OWtoh0m79FBqfSh-rGiXJdD6Zqp_TgoktWdfPsaLoIPNuapWLFHDgNz49-VzpdpsjQ_36YLX_sD_FKOLCUIgSFMVxQcqQPpr2hoeCjMdXtVnvYR_b6ltZZQMMANI1vgWw7GKklKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05e9aa8412.mp4?token=FhgRNzmy56ZNAJRisro6PSr49AKQz3TRm17_UByjMJ7Lgc5YWuK-y1JwLA-f7uoOQ4AuB6urszqOglzKH55lzdgaUUUTkgk8xth8Nipw-SrDSKh0k-0fDx-ocnS9ATmDfq9FPohu1z8EAxGZBafDD21a6ErSqW3NL-DVOubFp3sDkbw_UDndd4CUR0qUXzDtKhEG23jwUlzG01OWtoh0m79FBqfSh-rGiXJdD6Zqp_TgoktWdfPsaLoIPNuapWLFHDgNz49-VzpdpsjQ_36YLX_sD_FKOLCUIgSFMVxQcqQPpr2hoeCjMdXtVnvYR_b6ltZZQMMANI1vgWw7GKklKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرود هواپیمای F-18 بر روی ناو هواپیمابر در هوای بارانی.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69887" target="_blank">📅 15:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69886">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e61a50ec6.mp4?token=lmhm7V4dygb33y1_SnbdmPrewkk4NhWzVkoaK3e-xn8sBKrRDgBtRRCMAE6VPe5q_DpzR2gu-c7NgtSche35mgA8F-G3fleFJwgzEj2OMdG5dC60VnlWYffIrTvYtrKaf-1b00o1OsByZOz6fE6KfLUK1ICm1KM7oTpnsx4JWCFvLvt_ZVtTJ5XHlUJNRUXOu2YXcXVFAQBuoHVOubidWDRoAcOrygffeVujVtkl8yqbKaxd4uSBOWbnIL-1oxknqp-9Zt5mNasFFF_jyMHc4Ldtp9QHiGrMbd2MAiWay1KT-BrLEhIPg-YI8bQGx_jP2tWTnJ0KpE9hu_QpO2wKFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e61a50ec6.mp4?token=lmhm7V4dygb33y1_SnbdmPrewkk4NhWzVkoaK3e-xn8sBKrRDgBtRRCMAE6VPe5q_DpzR2gu-c7NgtSche35mgA8F-G3fleFJwgzEj2OMdG5dC60VnlWYffIrTvYtrKaf-1b00o1OsByZOz6fE6KfLUK1ICm1KM7oTpnsx4JWCFvLvt_ZVtTJ5XHlUJNRUXOu2YXcXVFAQBuoHVOubidWDRoAcOrygffeVujVtkl8yqbKaxd4uSBOWbnIL-1oxknqp-9Zt5mNasFFF_jyMHc4Ldtp9QHiGrMbd2MAiWay1KT-BrLEhIPg-YI8bQGx_jP2tWTnJ0KpE9hu_QpO2wKFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داستان زیبای زندگی کسی که هممون باهاش خاطره داریم...
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69886" target="_blank">📅 14:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69885">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
🔴
ما سه راهبرد داریم:
ادامه دادن به همین روال فعلی؛ یعنی صرفاً پیش رفتن و نظاره کردنِ وضعیت وخیم آن‌ها، چرا که تورمشان به ۳۰۰ درصد رسیده است. ارزش پول ملی‌شان تقریباً از بین رفته است. آن‌ها حقوق سربازانشان را نمی‌پردازند و سربازانشان در حال ترک خدمت هستند. بنابراین باید همین روند را ادامه داد، چون این وضعیت پایدار نیست.
وارد کردن ضربات بسیار سنگین به آن‌ها، یا... در واقع راهبرد سوم، شکست دادن آن‌ها از طریق اقتصادی است. اما ما به هر حال داریم همین کار را می‌کنیم؛ این [راهبرد] تا حدی بخشی از همان راهبرد اول محسوب می‌شود.
از نظر اقتصادی، وضعیت آن‌ها آشفته و نابسامان است. آن‌ها نمی‌توانند وام بگیرند. ما کنترل منابع مالی‌شان را در دست داریم؛ همان دارایی‌هایی که در اختیار داشتند و رقم بسیار بزرگی هم بود. آن‌ها سرمایه زیادی داشتند و ما اکنون کنترل کامل آن را در اختیار داریم.
من بانکدار آن‌ها هستم. من بانکدار آن‌ها هستم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69885" target="_blank">📅 13:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69884">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71d56160d7.mp4?token=c8U416gcNnVEQP_fws801wD0KOsMMo1tQF5gnWMfylydsQ8mcEh2mV0eZmzmDKCwN-wP6ei0fBEt9TtOmFrR5ogY4PgTrmKutqhrzNnvxjF2m7d-_BgX0q0SFAagXufRyDJp4oLyW4ToGctozwXthlmvS0TxE9W8c6cbCoH_NeU43gkPF8mG09gSlIx5LClK7sjIMtKevBiGHQ9Z2a3AR1w8ACgvV90iBmHrODTq9oh3txoVeqCiLdQVEUWZeJHA0fZH8cKphetS0h2U_Y_2Gi-At99HOnAz7nl3b-BI0n_UEysvNN8Wxho2bS75qEtlVkkusNId3RXNoUgQlUW_Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71d56160d7.mp4?token=c8U416gcNnVEQP_fws801wD0KOsMMo1tQF5gnWMfylydsQ8mcEh2mV0eZmzmDKCwN-wP6ei0fBEt9TtOmFrR5ogY4PgTrmKutqhrzNnvxjF2m7d-_BgX0q0SFAagXufRyDJp4oLyW4ToGctozwXthlmvS0TxE9W8c6cbCoH_NeU43gkPF8mG09gSlIx5LClK7sjIMtKevBiGHQ9Z2a3AR1w8ACgvV90iBmHrODTq9oh3txoVeqCiLdQVEUWZeJHA0fZH8cKphetS0h2U_Y_2Gi-At99HOnAz7nl3b-BI0n_UEysvNN8Wxho2bS75qEtlVkkusNId3RXNoUgQlUW_Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سینا حجازی، خواننده:
اگه زنِ هات میخواین، زن گوشت‌خوار بگیرین، زنایی که گیاه خوارن، سردن!
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69884" target="_blank">📅 13:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69883">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ams0WHCCnuCsoyN8EP-jgajmj-LJC4bIjnNNxefZ5CBpTfwKA2FsSNNkXfECGy9gblz7LdCP0-0sO6bWxK6CI2_Kr4GZjZ2HaULPkPHtRZWt6Y6FclwoqaYuOuEWsNUbo9Aqu8_VO81PQqX9d1FSyIR4oOBhMNldkurUmNzaKIROs_GvqGwqugUMxsbbAc_E1wOcW5W-gO0HNI5g-S-YsX0xyQ47TGot3qPNcWL5lGMhy0p6w8mFCP8Crs4l-7iLhfKwIu7J9I_nXp9YfcWZr9W4etyExewVxM6zc0ZKXxw_YqGgV5NIfdmiVDggNgT7mz2AK73WsSyXey5eQlVL1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان تجارت دریایی بریتانیا:
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از وقوع حادثه‌ای میان یک نفتکش و نیروهای نظامی در دریای عمان خبر می‌دهد.
هویت نفتکش و نیروهای نظامی درگیر در این حادثه هنوز اعلام نشده است.
در حال حاضر جزئیات بیشتری در دسترس نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69883" target="_blank">📅 12:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69882">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b61a921e39.mp4?token=XefpAFkdO9AFiu_q4uhxwcmJlQ37etjytnnYRKVlr_1sfbze5hIeMQh8ajaLdecKcwegMtbqi6bm4lnPgxPoesYCmwo24tjwXYToONp_7jMa-c_ttjikDZSHMGM0TO-gJQyz7TYRsC2Ip66oz3CuTo47_n9hdYf6oHa6c9MtuhccrNmdOwN5wv6OlbEZ1HgfPfJymLafPN9xBet4U7l25iU_57jWzfCGsozP0dOuaIqIBRzO7mCzYBQox7W3THJ8sKINWjt4Ovizv92VPtKDZNENt7eCmBkR8lKHlMQZTq__nEnRng2jmggulBbro76SepaQBrZCQbeiNnoDS847qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b61a921e39.mp4?token=XefpAFkdO9AFiu_q4uhxwcmJlQ37etjytnnYRKVlr_1sfbze5hIeMQh8ajaLdecKcwegMtbqi6bm4lnPgxPoesYCmwo24tjwXYToONp_7jMa-c_ttjikDZSHMGM0TO-gJQyz7TYRsC2Ip66oz3CuTo47_n9hdYf6oHa6c9MtuhccrNmdOwN5wv6OlbEZ1HgfPfJymLafPN9xBet4U7l25iU_57jWzfCGsozP0dOuaIqIBRzO7mCzYBQox7W3THJ8sKINWjt4Ovizv92VPtKDZNENt7eCmBkR8lKHlMQZTq__nEnRng2jmggulBbro76SepaQBrZCQbeiNnoDS847qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تازگیا به نوع مدیتیشن تو تهران مُد شده که کلمات رو به صورت نفس‌نفس زدن میگن تا انرژی بد ازشون تخلیه بشه
😳
هزینه هر دوره بالای ۴۰ میلیون!!!!!!
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69882" target="_blank">📅 12:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69881">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46ae8f31fa.mp4?token=O-AX-foBifitf4K-vOXid2F9gNhaICDLjyJZMOFuqNP5QT1ciflbF-e8Yf6exMB-8E-mAT52WhdZj8uivCDsUfPzT1K6RfNhDBELeu_TuztXQA-OvQHP21lO4mY3I3gdGXgK1482UzZ7c3nxCgbHxRucSaiuzFH4kbEjVFTdUhNzR_kkSPF_xOa2UUhM48pI4toMtdyv7yQFLSJBLuH0c2vaLlCkhgVwfu3LO56FuWExmBF2It8pLBJlsQbQyI7cwzkvxXDOAWXfPWQHQcCwUavOfFwKv1nLsa8WiTNAKv1fKU4iCp0WmE8Yy6lriMfrNE434qZcSrbzx_s2BnGLpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46ae8f31fa.mp4?token=O-AX-foBifitf4K-vOXid2F9gNhaICDLjyJZMOFuqNP5QT1ciflbF-e8Yf6exMB-8E-mAT52WhdZj8uivCDsUfPzT1K6RfNhDBELeu_TuztXQA-OvQHP21lO4mY3I3gdGXgK1482UzZ7c3nxCgbHxRucSaiuzFH4kbEjVFTdUhNzR_kkSPF_xOa2UUhM48pI4toMtdyv7yQFLSJBLuH0c2vaLlCkhgVwfu3LO56FuWExmBF2It8pLBJlsQbQyI7cwzkvxXDOAWXfPWQHQcCwUavOfFwKv1nLsa8WiTNAKv1fKU4iCp0WmE8Yy6lriMfrNE434qZcSrbzx_s2BnGLpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
استایل ثروتمندترین ورزشکار دنیا
🆚
استایل پسرایرانی با ماهی ۱۵تومن حقوق
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/69881" target="_blank">📅 12:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69880">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf27d27808.mp4?token=WDTqV7AEaSRUpvemc1BIj8IGi7Kt7Efp0wTyrAlavtvQSDwvPHfop2BOQoGBwgIeCM91LBOjTccm3SbQFWer2XIwKfXdOswNvT6U-_NdGOEI3XAxTRC8CofMtvM0HE-3HMKZmUo6Plf9BjB8mgVSsMJG1yfuudzrqr4AeHx2g7vGxlOsvCp5RJjFr-DW2ELhqquK7WthFwJC7EXpJuIqL8DjqCQimi8690thbeFFBHZK5u5en-RzNnbnby-__qgbf-zN46TsK7LMYLKmGJ0Z4imukGKc_NPhxlIYDqKKf6VT9zWUza-PY1JzXi8oDHUcdwKerCwLs7Cl7UCsXCGA4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf27d27808.mp4?token=WDTqV7AEaSRUpvemc1BIj8IGi7Kt7Efp0wTyrAlavtvQSDwvPHfop2BOQoGBwgIeCM91LBOjTccm3SbQFWer2XIwKfXdOswNvT6U-_NdGOEI3XAxTRC8CofMtvM0HE-3HMKZmUo6Plf9BjB8mgVSsMJG1yfuudzrqr4AeHx2g7vGxlOsvCp5RJjFr-DW2ELhqquK7WthFwJC7EXpJuIqL8DjqCQimi8690thbeFFBHZK5u5en-RzNnbnby-__qgbf-zN46TsK7LMYLKmGJ0Z4imukGKc_NPhxlIYDqKKf6VT9zWUza-PY1JzXi8oDHUcdwKerCwLs7Cl7UCsXCGA4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:درباره گرانی ها هم توضیح بدید؟!
🇮🇷
مهاجرانی سخنگوی دولت:
قبلا توضیح دادیم، گرانی های موجود دلیلش فشار اقتصادیه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/69880" target="_blank">📅 11:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69879">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c1ee7cbbf.mp4?token=PPG41PtF4YXEWq-cEUYuI7FvrOHEdaFVqbNdx9D7c3iEMoC1O9EjFYI-iNtKh420qdJBoOjNOA6ZcEzJSrRN1a2F_gT_1Fv_2ZFLxbPuL3aGK8qvP-3Zh9XBIqVbfyWSajDbQxGuMzWvQ8Igr1QsCjy-2NqnbGuXJ5ok7d8bSxSmED-LIibsKFrA1vxyPjP5kEVGmhjILCLCGnd_zVP7WbgLjGKRsSKP_PzeKuSl8mWXxwJoVURXvlrgplXZIFmoVXhZCeGt5_qcULoSgUsTSjBNSvDxMwnstZ3gtWLK6RBoy2cEQGtwLB_ZDzgxZY_CmM9NeueKMq0S8CiI1wifOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c1ee7cbbf.mp4?token=PPG41PtF4YXEWq-cEUYuI7FvrOHEdaFVqbNdx9D7c3iEMoC1O9EjFYI-iNtKh420qdJBoOjNOA6ZcEzJSrRN1a2F_gT_1Fv_2ZFLxbPuL3aGK8qvP-3Zh9XBIqVbfyWSajDbQxGuMzWvQ8Igr1QsCjy-2NqnbGuXJ5ok7d8bSxSmED-LIibsKFrA1vxyPjP5kEVGmhjILCLCGnd_zVP7WbgLjGKRsSKP_PzeKuSl8mWXxwJoVURXvlrgplXZIFmoVXhZCeGt5_qcULoSgUsTSjBNSvDxMwnstZ3gtWLK6RBoy2cEQGtwLB_ZDzgxZY_CmM9NeueKMq0S8CiI1wifOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دکتر مشاور خانواده :
یه مرده اومد بهم گفت زنم عاشق دوستم شده و منم بهش گفتم که تو حق داری باهاش رابطه داشته باشی!
گفت منم با خانمِ اون آقا چندبار رابطه داشتم ولی چون اون خانم خودش پارتنر داشت، زیاد خوشم نیومد و کات کردم...
ولی خب موقع سکسِ اون آقا با زنم، من اونجا هستم و تماشا میکنم!
الانم از اینکه خانمم از اون آقا باردار شده خیلی ناراحتم چون آمادگی داشتن بچه رو ندارم.
ولی خب بازم میخوام شناسنامه اون بچه رو به اسم خودم بگیرم...
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/69879" target="_blank">📅 11:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69878">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/news_hut/69878" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/69878" target="_blank">📅 11:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69877">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOhQ1I1iqa_tqo7gjArSTAa7gjkmlRfvsyoMkB8D5PlRh4nKCgneIwUNG-6cVgXSTBZfrouQ9Nvco5gG9hO14GQR4hVL6vtQPxwybFiw6wx0uv06UkBxJX8iqOS0ynSP_ZNov7bcbUGD4vry2ecUy_7uZCkT_9DJP6vHZ_bmcLwUhghfc4YSda08AWrRrQ_2yzGG_QPwTsSHPt4--48sWhPFBUZr2w_xw6phIjdkrwgZ3xSF9nSWYaJvAAp5JkBEpW-cpg9k8ZVL4MUAPtpEiTiIHAZVm2npxdE5I9MU-NDBkSrZ-_EAVPBidW-aCjSiiubIOHkV7KAHWhn3MF42sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️
برای دانلود اپلکیشن کلیک کنید
👉
r20
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/69877" target="_blank">📅 11:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69876">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2435556002.mp4?token=ndjs1Cx1yvUzj6dph7kwAUJOCd9sZNFbZA7b5V-oov5KswpRJEFDlHWNruP5TGsa1Pqn2XyCnqvDr40uVe3ByoMC81FzoG8b8CvVNK23FJnq7L0sk0bhkdJdxYtuXAgzjaOzHJtxUJ3xICILazkdtkyGLvhKpw5mU01wT1U2dlZ5c9WtH-kBwTBdjTc0SGI4rN0BpI0WSL2yBAzV5oO-ULwHFtAoAywKzBWviRiZEPpN8CM8Hua_lMd9aSFKCx9lStWwd3Tcn-ak9EIeK8NpMVDCdBt0DTEcKjMQ33wpWX3kYXQG3UpgIZGk9Jl1LYCnk2FFuGI-mhJt4RFRozbw-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2435556002.mp4?token=ndjs1Cx1yvUzj6dph7kwAUJOCd9sZNFbZA7b5V-oov5KswpRJEFDlHWNruP5TGsa1Pqn2XyCnqvDr40uVe3ByoMC81FzoG8b8CvVNK23FJnq7L0sk0bhkdJdxYtuXAgzjaOzHJtxUJ3xICILazkdtkyGLvhKpw5mU01wT1U2dlZ5c9WtH-kBwTBdjTc0SGI4rN0BpI0WSL2yBAzV5oO-ULwHFtAoAywKzBWviRiZEPpN8CM8Hua_lMd9aSFKCx9lStWwd3Tcn-ak9EIeK8NpMVDCdBt0DTEcKjMQ33wpWX3kYXQG3UpgIZGk9Jl1LYCnk2FFuGI-mhJt4RFRozbw-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری و بلاگر طرفدار حکومت:
یعنی چندنفر باهم مشکل داشتن و همدیگه رو به طور کامل میشناختن
این پروژه‌ها از این به بعد قراره زیاد باشه واسه اینکه میدون‌ها و نیروی انتظامی رو ضعیف کنن
قاتل‌ها تو کمتر از 24 ساعت دستگیر شدن و کشور الان تو بالاترین سطح امنیته مخصوصا تو تهران.
متأسفانه قراره خون ریزی های از قبل برنامه ریزی شده شاهد باشیم
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/69876" target="_blank">📅 11:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69875">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/022aef02ab.mp4?token=gBf4GTxT-lQ2-GLCoLn0zfpgS1pJ0N9cLI_dBIP3jO8L-4ZwpuqpReTsOBH6v47Ny8BtVTpJxXH8PLxvTELolhjwSq1FUh6C_j9-rr6ldabIuuf6C75r8Ii-HxiHO-d-PunSDHWr3ZO3FD3JSt_ICPYkCmdfQO72Qb3p17RAcLkAAicaVw5TNXgnOe1DeWg6jpAJMrgiEQkoJ7IVCf6k-XUIJOPZwWTitb56fEkRUQGvz4jFqMVLhcv6M0Wwdxinw8OlcCWBCwjty93kG1bwxmYiAQpxxeTGPry8Jth8R2yycjgLZAnpM9KKa5g8KlIe9ZKrjisRBZUYAEzVnDxMvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/022aef02ab.mp4?token=gBf4GTxT-lQ2-GLCoLn0zfpgS1pJ0N9cLI_dBIP3jO8L-4ZwpuqpReTsOBH6v47Ny8BtVTpJxXH8PLxvTELolhjwSq1FUh6C_j9-rr6ldabIuuf6C75r8Ii-HxiHO-d-PunSDHWr3ZO3FD3JSt_ICPYkCmdfQO72Qb3p17RAcLkAAicaVw5TNXgnOe1DeWg6jpAJMrgiEQkoJ7IVCf6k-XUIJOPZwWTitb56fEkRUQGvz4jFqMVLhcv6M0Wwdxinw8OlcCWBCwjty93kG1bwxmYiAQpxxeTGPry8Jth8R2yycjgLZAnpM9KKa5g8KlIe9ZKrjisRBZUYAEzVnDxMvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇺🇸
واشنگتن پست:پس از تهدید ترور از سوی ایران، ترامپ مخفیانه هنگام ترک اجلاس ناتو در آنکارا با هواپیمای دیگری جایگزین شد.
او با هواپیمای جدید ۷۴۷-۸ اهدایی قطر (اولین سفر بین‌المللی ریاست جمهوری‌اش) به ترکیه رسیده بود.
برای عزیمت، او علناً و جلوی دوربین سوار هواپیمای قدیمی ایر فورس وان شد و گفت که می‌خواهد «به یاد گذشته» با آن پرواز کند.
اما دقایقی پس از سوار شدن، او و چند دستیارش از طریق یک کامیون پذیرایی فرودگاهی که کانتینر آن به صورت هیدرولیکی به دری در کنار و دور از دسترس رسانه‌ها بالا رفته بود، به یک هواپیمای کوچک‌تر C-32A (757 اصلاح‌شده) منتقل شدند که از دید پنهان بود.
سپس هواپیمای قدیمی ۷۴۷ به عنوان طعمه پرواز کرد و همچنان از تابلوی تماس ایر فورس وان استفاده می‌کرد.
روزنامه‌نگاران و برخی از کارکنان کاخ سفید که در هواپیما بودند، اصلاً نمی‌دانستند که ترامپ با آنها نیست.
به آنها گفته شده بود که پرده‌های پنجره را بسته نگه دارند، که امری غیرمعمول است.
هر دو هواپیما با فاصله چند دقیقه در فرودگاه سلطنتی میلدنهال در بریتانیا فرود آمدند.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/69875" target="_blank">📅 10:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69874">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: ما ۳ استراتژی برای برخورد با ایران داریم
رصد نقاط ضعف این کشور.
وارد کردن ضربات سنگین.
اعمال فشار اقتصادی.
🔴
اکنون ایران در وضعیت آشوب اقتصادی قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/69874" target="_blank">📅 10:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69870">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b616d440e1.mp4?token=p6mUuYWskp7K7ITPqJVmwx-NdYtBZrx1PO4rwhWIXm326iYFFrH_ohnGc8XzOZxtyGnCNV4LkWlXh5lendCEZJ9fucBjG9uX8LqHy7E6Vo7OPfwDK76FiQtKz17q-elPjWBYV_pmuIcoLAuEYPFiGuuBKEWAeAk3dhMsIwiEU8JNCcXdoqGWpoI05nKAANaG_YvE0sRHlFYp2p2bGCUn7phnwwc2RtVmKCNey7QzOoiMVp063GHxEBPffbPOMpwJJEXzL_IaxmjPCMLVZHUzwtSCC8UvPJRqh5FW1z7eUSGfD5axZu2wW1Ounwb2c51RMg49fzBwfe-thr0qJpglXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b616d440e1.mp4?token=p6mUuYWskp7K7ITPqJVmwx-NdYtBZrx1PO4rwhWIXm326iYFFrH_ohnGc8XzOZxtyGnCNV4LkWlXh5lendCEZJ9fucBjG9uX8LqHy7E6Vo7OPfwDK76FiQtKz17q-elPjWBYV_pmuIcoLAuEYPFiGuuBKEWAeAk3dhMsIwiEU8JNCcXdoqGWpoI05nKAANaG_YvE0sRHlFYp2p2bGCUn7phnwwc2RtVmKCNey7QzOoiMVp063GHxEBPffbPOMpwJJEXzL_IaxmjPCMLVZHUzwtSCC8UvPJRqh5FW1z7eUSGfD5axZu2wW1Ounwb2c51RMg49fzBwfe-thr0qJpglXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇴
دیروز تو کلمبیا، یه زلزله 7.4 ریشتری اومد و اینجوری به ساختمون ها خسارت وارد کرد؛
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/69870" target="_blank">📅 09:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69869">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22c07c5ff9.mp4?token=PodMR8jCGWQVu1L8tOPkTRCzfI2hPSJQbBNZAMIAfbKRRR_QndINonAhgdGYprBaZb7ejgKx18Oc5OilZMTsyEvCPWE0RtmYlkQ8G4q5SDCYGOfycqS3T_NQb_NQWV0r5BOi2qH7aZt4hEPQhTekRyApub0FwB8SVHIywtkSBlrRKYyFyYYbZm3gnco9H5OR6L_VusYgqfJijxbomVcbS15Zf1RIOJQhg_EUQNBYfn_iasxs1ig6mhvFJ4MHFIrgtvpSwHG29m1CmMRvyDyKIHFU0K0n1ng_ICcpep8qEMRb1ANFclyS7sN_4WUimSsYv8-WPBFeT7KVhPVaHNZD1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22c07c5ff9.mp4?token=PodMR8jCGWQVu1L8tOPkTRCzfI2hPSJQbBNZAMIAfbKRRR_QndINonAhgdGYprBaZb7ejgKx18Oc5OilZMTsyEvCPWE0RtmYlkQ8G4q5SDCYGOfycqS3T_NQb_NQWV0r5BOi2qH7aZt4hEPQhTekRyApub0FwB8SVHIywtkSBlrRKYyFyYYbZm3gnco9H5OR6L_VusYgqfJijxbomVcbS15Zf1RIOJQhg_EUQNBYfn_iasxs1ig6mhvFJ4MHFIrgtvpSwHG29m1CmMRvyDyKIHFU0K0n1ng_ICcpep8qEMRb1ANFclyS7sN_4WUimSsYv8-WPBFeT7KVhPVaHNZD1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
خرازی:
مجتبی خامنه‌ای اگه تو این سه سال از دفتر رهبری طرد نمی‌شد، می‌کشتنش
خود علی خامنه‌ای هم همین‌طوری بود، تو دفتر خمینی هیچ جایی نداشت
از احمد خمینی بگیر تا کروبی و... همه میخواستن مرگ علی خامنه‌ای رو ببینن.
ابراهیم رئیسی هم قصد داشت رهبر بشه که شهیدش کردن
اصلا بحث همینه مجتبی اگه زیاد پیش پدرش دیده می‌شد خودی ها میکشتنش
تو بحث رئیسی هم یکی از اعضای دفتر اومد خونمون گفتش ک دارودسته اینا میخاد رئیسی رهبر بشه ولی شهادت جلوشو میگیره
خیلی حرفا هست ولی خب مطمئن نیستم بشه گفت یا نه
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69869" target="_blank">📅 09:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69868">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
🇺🇸
✈️
پشتیبانی سنگین آپاچی‌ها از نیروهای ویژه آمریکا در افغانستان
⏺
تصاویر نادر و حدود ۱۵ دقیقه‌ای از عملیات دو فروند AH-64 Apache در افغانستان؛
آپاچی‌ها گروهی بیش از ۲۰ نفره از نیروهای طالبان را که در حال آماده‌شدن برای کمین یک گشت نیروهای ویژه آمریکا بودند، شناسایی و درگیر می‌کنند.
در این درگیری، آپاچی‌ها ابتدا با توپ ۳۰ میلی‌متری M230 مواضع طالبان را زیر آتش می‌گیرند و سپس برای درگیری با اهداف مشخص‌تر از موشک‌های AGM-114 Hellfire استفاده می‌کنند.
تصاویر این ویدئو با سامانه تصویربرداری حرارتی FLIR نصب‌شده روی آپاچی ثبت شده؛ به همین دلیل صحنه‌ها به‌صورت تصویر حرارتی دیده می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69868" target="_blank">📅 09:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69867">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/69867" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
a19
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/69867" target="_blank">📅 01:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69866">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SeeyXLFdSBJP7pJFwQem_qaceM7pLOgscPMQvrUoetRKDe9hAknMnnrDgadupe0F9Cea3A4NT3Nb0nQdXaxTq3N25qCkOYk5rKxBBBgu5fLP3X0pExASxvUkiE_o-iZoRjp2LVlMGYw6dPUTDJqUsSNG2my1vrJjtaKtnIK0xmHfFUL-kFFxHL6zuYhFZVsQLkvdj8aydtsoRBdvxOX5C_zBTOHlHGcmcJugJciAmjlQY1A7Xq3GBLSVOSsNR_143C3sVkTdZqXpGumEaMUA03d37FWP2eQ4WX6NbhYlryrYYpVVMG_qx7j6RBAzJ7PP36UIthv_3N2g9CBRMgbhwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
a19
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/69866" target="_blank">📅 01:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69865">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/6ad4ea0af6.mp4?token=joTrC--ZpGPahDyn4GqiO7pwLp3Gr7OAbE-cSGlRUFZgJw76UPoek2uV8zgyt7eZqzd2LyGpY2ptptiiB1j7dag1DO6z7Q7dowS45UlG8Kduwwl4REJVJ2CbClAyNNB9SwVN0V5weG8szy07P0dTlJvw0p7tNSqJl5z9DQjQrmOHruVT_EZ5LWuzntU4BJEDPCCx5fuxPJED3qSM4bvVZRA9HPjVDwpuTNJVt2_I4Gwj5JEgUESQUkV1jVht9VEqKyU44UUXJmwCsVW1O0CfciLUJGxTIBoYzr3EquOSD3mBAk1sBvpxtZefNB5a_cEYSGCCzRULrd-vwGGragTuXmJN1dccTOI0wpGHJ_PE0da9D2v_IwXn_a0u4ovhRiGVfqmA52aHb37FqwJ0meroYKk2oGwdbEeDaD4fosV2PPUgis26_UrQ9DDCQovqXCweC7Fc9wcaSBMpsn2V6H13BGM6rmZgtVVOt9t-iwsxQVwa9OmKww_RBfjCgrI20dLj4GwXmSCXjNnnjMFdImCPoBnac8MHVFCf5Iobwr_MysSb2iUXLPGcFuWou9rOAHJEjXGJi76BYhfmq3Ho2Mj1Vp9LLn5xc2SXLO2Vky19jeM9ZTzWD8IRM8Jf_urevGz3g5dRYR5Fr_z8vhAMClog9i1hn3hVF7fjLGPlwT19yPY" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/6ad4ea0af6.mp4?token=joTrC--ZpGPahDyn4GqiO7pwLp3Gr7OAbE-cSGlRUFZgJw76UPoek2uV8zgyt7eZqzd2LyGpY2ptptiiB1j7dag1DO6z7Q7dowS45UlG8Kduwwl4REJVJ2CbClAyNNB9SwVN0V5weG8szy07P0dTlJvw0p7tNSqJl5z9DQjQrmOHruVT_EZ5LWuzntU4BJEDPCCx5fuxPJED3qSM4bvVZRA9HPjVDwpuTNJVt2_I4Gwj5JEgUESQUkV1jVht9VEqKyU44UUXJmwCsVW1O0CfciLUJGxTIBoYzr3EquOSD3mBAk1sBvpxtZefNB5a_cEYSGCCzRULrd-vwGGragTuXmJN1dccTOI0wpGHJ_PE0da9D2v_IwXn_a0u4ovhRiGVfqmA52aHb37FqwJ0meroYKk2oGwdbEeDaD4fosV2PPUgis26_UrQ9DDCQovqXCweC7Fc9wcaSBMpsn2V6H13BGM6rmZgtVVOt9t-iwsxQVwa9OmKww_RBfjCgrI20dLj4GwXmSCXjNnnjMFdImCPoBnac8MHVFCf5Iobwr_MysSb2iUXLPGcFuWou9rOAHJEjXGJi76BYhfmq3Ho2Mj1Vp9LLn5xc2SXLO2Vky19jeM9ZTzWD8IRM8Jf_urevGz3g5dRYR5Fr_z8vhAMClog9i1hn3hVF7fjLGPlwT19yPY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇦
لحظه سقوط یک جنگنده میگ-۲۹ اوکراینی.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69865" target="_blank">📅 01:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69863">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcca7b928e.mp4?token=ZxgRZszoaEch7cfGLjQ0ZAlUj1_bHJdDQSX0pwhE70QZhclZkpRILekVvKK8rngmmLPEJ-9X0cXcXgpPOi_b7k-9NAHIo1tN3AIZ-dgJLDIi5AIppdVoamTSaNRu0ASk8dT82b41xs7pUFEEgZmD6f-gysgfyo-Ru2SRw4LuJfeRSlP83xBZ0GgHDGJB8xDDIo54aZvi9F5cycAOuIpO_lzFHAFTTDfIbUmPU2Ctja3wKRJ61sRWJcm4HPv-m9nI6XicC_nIapn03UPVgUrHsPuzh6TUj4BDGWMM2NvWExLzbmdweJOCauAeZqwsJuD952JvqEfGIYpyX8Zx-5WmLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcca7b928e.mp4?token=ZxgRZszoaEch7cfGLjQ0ZAlUj1_bHJdDQSX0pwhE70QZhclZkpRILekVvKK8rngmmLPEJ-9X0cXcXgpPOi_b7k-9NAHIo1tN3AIZ-dgJLDIi5AIppdVoamTSaNRu0ASk8dT82b41xs7pUFEEgZmD6f-gysgfyo-Ru2SRw4LuJfeRSlP83xBZ0GgHDGJB8xDDIo54aZvi9F5cycAOuIpO_lzFHAFTTDfIbUmPU2Ctja3wKRJ61sRWJcm4HPv-m9nI6XicC_nIapn03UPVgUrHsPuzh6TUj4BDGWMM2NvWExLzbmdweJOCauAeZqwsJuD952JvqEfGIYpyX8Zx-5WmLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
املاکی رو ببینید؛طرف یه ساعته داره جلوش گوه میخوره بعد این کصخل یجور لم داده رو صندلی که انگار تو تخت بغل ملانیاست
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69863" target="_blank">📅 01:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69862">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7d1e744df.mp4?token=QQDPin8MXqZHzQ9ZUNCq8vT85JScHNFt83MBMIwif1EykhlfxTrChoqJB3zHe1aTCWDqGkUK1RhD_YAD_wSdJeUGRpi4wv-vkKF9UpVy51uICUzLonEUuCRVfwcAq0-ubun9KGB58By2ua-XmIu1fIR_p9t6AhW_d9S9OnYKobNdwausQZy-3tsDjNOiX3-GcK4j4dXUclwxMyS414_KP-6IPFRphgINOUX5p7k42yDaIA4PKVn3de0YJBVqhghvlW8MlbRqtyE1NkvmDOCSd4CWKrSrKMDnknZtj5GYBTO1F7HrWUGjBuo9yKxdp5XoO1TxBK0GwBN_Ir06YN3pQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7d1e744df.mp4?token=QQDPin8MXqZHzQ9ZUNCq8vT85JScHNFt83MBMIwif1EykhlfxTrChoqJB3zHe1aTCWDqGkUK1RhD_YAD_wSdJeUGRpi4wv-vkKF9UpVy51uICUzLonEUuCRVfwcAq0-ubun9KGB58By2ua-XmIu1fIR_p9t6AhW_d9S9OnYKobNdwausQZy-3tsDjNOiX3-GcK4j4dXUclwxMyS414_KP-6IPFRphgINOUX5p7k42yDaIA4PKVn3de0YJBVqhghvlW8MlbRqtyE1NkvmDOCSd4CWKrSrKMDnknZtj5GYBTO1F7HrWUGjBuo9yKxdp5XoO1TxBK0GwBN_Ir06YN3pQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: گفتید این آخرین فرصت ایران هست چیشد؟؟
🇺🇸
ترامپ: به زودی متوجه خواهید شد
ما توانایی افزایش تنش رو داریم
خسارات های جنگ رو از طریق منابعی از ایران جبران خواهیم کرد
خسارتی رو اگه قرار بشه کسی جبران بکنه این ایران هستش
هیچ اتفاق بدی قرار نیس بیوفته
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69862" target="_blank">📅 00:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69861">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d10abc62a6.mp4?token=pd0UHENLbzLlaX_gZE7fv_DvO2Y-mIc6GwMxCZf-jbqG-3SS8dlHNMczLshIDLlAYUJxdzH29-_C2uU8eP2JC81NZxeKBtAXGnEXUjzGDLm3uXThfGen32RJwO5x6cXBvGXw-soPqajOCrT1E59MwL02mAZ8S06pG6eUPQQ0fDupLiI1VO1mit9Rf_FqZEgohpxksGRo9xUwi6YgQF1I6iBiBOatAwMlpiaJN--J1lqPfm8eIwztJLiyO_doVumu9COp70rNNLSxF3Fx4b7sGh84tEKsiue4z9pkF8Lw8LwpS5LWRo3c9DJ47pI3Dk3nyuUDpqXD4amZ4i9SeZ67YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d10abc62a6.mp4?token=pd0UHENLbzLlaX_gZE7fv_DvO2Y-mIc6GwMxCZf-jbqG-3SS8dlHNMczLshIDLlAYUJxdzH29-_C2uU8eP2JC81NZxeKBtAXGnEXUjzGDLm3uXThfGen32RJwO5x6cXBvGXw-soPqajOCrT1E59MwL02mAZ8S06pG6eUPQQ0fDupLiI1VO1mit9Rf_FqZEgohpxksGRo9xUwi6YgQF1I6iBiBOatAwMlpiaJN--J1lqPfm8eIwztJLiyO_doVumu9COp70rNNLSxF3Fx4b7sGh84tEKsiue4z9pkF8Lw8LwpS5LWRo3c9DJ47pI3Dk3nyuUDpqXD4amZ4i9SeZ67YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
پس تنگه هرمز کِی باز میشه؟
🇺🇸
ترامپ : بازه!
ما صددرصد کنترل تنگه رو در اختیار داریم.
همون طور که احتمالاً شنيديد، كل تنگه رو مین روبی کردیم. البته شاید هم نشنیده باشید.
اونا میتونن دردسر درست کنن، ولی ورشکسته‌ان؛ پولی ندارن، ایران کاملاً ورشکسته‌ست. حتى حقوق سربازهاشون رو هم نمیدن، نرخ تورمشون 309 درصده.
ایرانی ها صدها هزار نفر رو کشتن، حالا دارن تاوانش رو پس میدن.
اگه قرار باشه خسارتی پرداخت بشه به نظرم ایران باید اون خسارتها رو پرداخت کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69861" target="_blank">📅 23:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69860">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
گزارشگر: شما گفتید که این آخرین فرصت ایران بود. حالا چه؟
🇺🇸
ترامپ: شما متوجه خواهید شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69860" target="_blank">📅 23:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69859">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8eb808fce.mp4?token=t1CbOq5UbeLvIfM2qzqROjQ7zNOWCUy4JtqzK4r2qKWy3-azZ1T80NgcV2TFgDyDaGW83_IkBrWleQsjfmC7TAyTQB_0C8fWu_7zAcAL48M3g4CsU-DmEaQ7F00Jr31PcQvHXQN-Dur_jYPN2ynNKYTSBE7drTSQymTmhgJk4esI2b-859Rv9jlqZSn-k8TFiMRdN3G0cWdVEYKAn0jhGlgIPdm7Y1Giil3Cou3H7ZMVWNJwRsR5BuhCzm-cnsc8Bw4b1LcMMT_JuWxGUTxJuWuSgTc6dJZu30dQDOFQSM-cnEr1howpOUtG82J6rBjszyKlB_5gvRAEQ4jHlEbGcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8eb808fce.mp4?token=t1CbOq5UbeLvIfM2qzqROjQ7zNOWCUy4JtqzK4r2qKWy3-azZ1T80NgcV2TFgDyDaGW83_IkBrWleQsjfmC7TAyTQB_0C8fWu_7zAcAL48M3g4CsU-DmEaQ7F00Jr31PcQvHXQN-Dur_jYPN2ynNKYTSBE7drTSQymTmhgJk4esI2b-859Rv9jlqZSn-k8TFiMRdN3G0cWdVEYKAn0jhGlgIPdm7Y1Giil3Cou3H7ZMVWNJwRsR5BuhCzm-cnsc8Bw4b1LcMMT_JuWxGUTxJuWuSgTc6dJZu30dQDOFQSM-cnEr1howpOUtG82J6rBjszyKlB_5gvRAEQ4jHlEbGcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
🇮🇷
عظمایی فرمانده نیروی دریایی سپاه پاسداران انقلاب اسلامی:
«اگر اسرائیل، ایالات متحده، یا هر یک از همدستان آن‌ها حتی جرأت کنند نگاهی خصمانه به جزایر خلیج فارس داشته باشند، با کمک خداوند متعال؛
چشم‌هایشان را کور خواهیم کرد و خلیج فارس را گورستان آن‌ها خواهیم ساخت.
»
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69859" target="_blank">📅 22:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69858">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c15a39d1d6.mp4?token=W3VPHe7IAn1cUDhSxwYbNvQ_sIN5SwMlLP5HE_V0IOj_Z-OIGZa4jjhdtdbjsAGFkdw9exaj5QqSV3LDP3QHGmn6pzVPhzl5FoP9mlRpn9l-0IqwlYIMQaBhMOm0mZSEz8U3bBgE9mHBpfKuT9PR4tbALGxFZ-gGzhd6rx2ChvJFaoNMIO_gkMatidgoC7ofzr3TTfCfIkz8_U1vbjfarxX4SIzc7STK46iqZgmY7CV7IIQy5dnDMx5tmBeUBsUVbfOmljObQHl8fxK61xELbZlmHBMsybu6FXpohTKMX4e7BXTExwuV2Bf19gxxPztyg5yFSVAchP03bU4EPYxCBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c15a39d1d6.mp4?token=W3VPHe7IAn1cUDhSxwYbNvQ_sIN5SwMlLP5HE_V0IOj_Z-OIGZa4jjhdtdbjsAGFkdw9exaj5QqSV3LDP3QHGmn6pzVPhzl5FoP9mlRpn9l-0IqwlYIMQaBhMOm0mZSEz8U3bBgE9mHBpfKuT9PR4tbALGxFZ-gGzhd6rx2ChvJFaoNMIO_gkMatidgoC7ofzr3TTfCfIkz8_U1vbjfarxX4SIzc7STK46iqZgmY7CV7IIQy5dnDMx5tmBeUBsUVbfOmljObQHl8fxK61xELbZlmHBMsybu6FXpohTKMX4e7BXTExwuV2Bf19gxxPztyg5yFSVAchP03bU4EPYxCBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باشگاه مختلط تو قیطریه تهران همراه با استخر جکوزی سالن  ماساژ سالن بیلیارد سالن بولینگ و...
😟
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69858" target="_blank">📅 22:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69857">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiGVM7KFkywW8MmzL0ae-ZxafAAUsB0H2LIvJC4mZH14g9q3WMuzQmGoS81FYtYQ2Dql2Z3t-_Kc4A119jZXsCbX1ynqyEdGkFvdQ-w-30zbdvJNGqrF8XJajNie-e7i3PdryyxMTXJn0Hn1neVsBv_sV_VQhb77Jejk94HDoecOZBkeCzUImM4JyeYCYZ_b1PNmzqIJwNFcxLmMD9pltanRtoopPse5BHW02K6C1fMFNfdL-pOyxi4swmKUvyGiGolBfShAAIE4qxlSAeWk-gDuUBa6o8o0NwCCHnsNvIbHvXKYMOh4sijEWMaW5iCgQPyhtx-iPQCBxD_B9cxoxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
پرزیدنت ترامپ درباره ایران:   می‌بینم که نمایندگان جمهوری اسلامی ایران خواستار غرامت بابت خسارات وارده به خود در جریان درگیری نظامی پنج ماه اخیر هستند (درگیری‌ای که آغاز شد چون آن‌ها نباید به سلاح هسته‌ای دست یابند)؛آن هم در حالی که این موضوع هرگز در…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69857" target="_blank">📅 21:26 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69856">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79470446aa.mp4?token=eHs6hQ4PKdwj_OUFpwhzPZAkeZ1glkatyg0bgQQcHd-_lwyorlb2oj8PyXhCI5fUrgH3mfDyDyDH7VmDz4V__qKxCWyuC3GrbzgdDrjsob8lKCp9kFm0-pTYMzEPoKGCF5h7DLmwNb7fy__5CiOZzXVsSjM6DI69swuhPBnoyiLQk6UedDskATXY2yI42micS41uaYTisH5b2QKS4hm3nztgHLayDMRfLFguGbjM_z5EthZWwweJVeuFxTvrPHjK77xQSzKdc_NHtdCb41fXWQM7xvBAlMdgHK2ii4rg4-k1kRKja821PVQPwg3p_cG-PE4-swZUuz-Eej-cVXnNvCSxfVIuVQEziiJqYGXr-_JNRW9qjjkE6-7CQa2StzQ1DO9I9Nmy9dBwmnx-oKIRDQXDMR4dhmolxS7Nn49MXiQHEbegxtudvHgPvIxmNgd9VYTEzeVCHwAE3YLXIkVyjfhDve3e6vYxv_rN15mk0TFlbiK1ppBHQA-aPaPfbt_smBUklu5KG6q0X5HSk3p1vAOmWuBE4THxkeYMjN0qZd9UAsdXcszx15tM9eYP7SrHg3RFaF5lFhCD8YKENmF3G7O_RBZAnXAMgWqGXRXrab4ZXi2s2m-CmMceL2EYox3oPO75xvyHGYQsOur98OtbLjcFyHax6paifSPEcvMC4Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79470446aa.mp4?token=eHs6hQ4PKdwj_OUFpwhzPZAkeZ1glkatyg0bgQQcHd-_lwyorlb2oj8PyXhCI5fUrgH3mfDyDyDH7VmDz4V__qKxCWyuC3GrbzgdDrjsob8lKCp9kFm0-pTYMzEPoKGCF5h7DLmwNb7fy__5CiOZzXVsSjM6DI69swuhPBnoyiLQk6UedDskATXY2yI42micS41uaYTisH5b2QKS4hm3nztgHLayDMRfLFguGbjM_z5EthZWwweJVeuFxTvrPHjK77xQSzKdc_NHtdCb41fXWQM7xvBAlMdgHK2ii4rg4-k1kRKja821PVQPwg3p_cG-PE4-swZUuz-Eej-cVXnNvCSxfVIuVQEziiJqYGXr-_JNRW9qjjkE6-7CQa2StzQ1DO9I9Nmy9dBwmnx-oKIRDQXDMR4dhmolxS7Nn49MXiQHEbegxtudvHgPvIxmNgd9VYTEzeVCHwAE3YLXIkVyjfhDve3e6vYxv_rN15mk0TFlbiK1ppBHQA-aPaPfbt_smBUklu5KG6q0X5HSk3p1vAOmWuBE4THxkeYMjN0qZd9UAsdXcszx15tM9eYP7SrHg3RFaF5lFhCD8YKENmF3G7O_RBZAnXAMgWqGXRXrab4ZXi2s2m-CmMceL2EYox3oPO75xvyHGYQsOur98OtbLjcFyHax6paifSPEcvMC4Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله تند مجری صداوسیما به علی دایی:
وقتی جرائت نداری جیگر نداری به دختر اونور آبت چیزی بگی پس اینجا هم خفه شو لال شو
یه گروهی گول میخورن میریزن کف خیابون بعد از این دایی و خاله ها زیاده هشتگ نه به اعدام میزنن
یکی از این آقایون مشهور دخترش مورد دزدی قرار گرفته بود کم مونده بود دزد رو بکشن بعد همینا هشتگ نه به اعدام میزنن
بعد این وحشیا این بیشرفا جوان مردم رو به شهادت میرسونن یه عده یاد حقوق بشر میوفتن
اعدام نفرت نمیاره شماها نفرت انگیزید شماها ترحم انگیزید
ولی یه پلیس یه گلوله شلیک بکنه داد میزنن عای دیکتاتوریه عای خاک خون کشیدن
شماهایی که لال هستید همیشه لال بمونید حتی اون ور آب
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69856" target="_blank">📅 20:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69855">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kib-U0yLfbRY9tIGe-Fw62xTtp6Xas0kumv-cwdhhapJ46Ba9Zq5DBLDesVCo8ajkUgX0msDzH0GvFsSAyIaDwh-OSwDVC1eVV_cAjsK0MI9TmwxH1qubkMd0ZlJTmudXqOLawHuGt8dQ7rPRaof0Yf7tjm_6xfmg31cBwMOEyZSbnuUGKXiJCNR0oKtty9duIvKN5fWwumlG6I2udcecxYZgkVkJccZFyGGXOYfclbvuC621B-WwTfiHbBuTwH_jMOIdD75giSwK1J_G5XiMQoiHvA9AZspepsGW19Jxv_lXWpon4UTTfNlj2l33_wBfJw4USu7F2CQ4uRR5TlPrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
پرزیدنت ترامپ درباره ایران:
می‌بینم که نمایندگان جمهوری اسلامی ایران خواستار غرامت بابت خسارات وارده به خود در جریان درگیری نظامی پنج ماه اخیر هستند (درگیری‌ای که آغاز شد چون آن‌ها نباید به سلاح هسته‌ای دست یابند)؛آن هم در حالی که این موضوع هرگز در هیچ‌یک از مذاکرات یا دیدارهای ما مطرح نشده بود!
اما این ایده جالبی است، چرا که من نیز اکنون متقابلاً از ایران درخواست غرامت می‌کنم؛ غرامت بابت تمام کسانی که آن‌ها با بمب‌های کنار جاده‌ای و در درگیری‌های متعدد — که به آن شهرت دارند و در ابتدا تحت هدایت ژنرال سلیمانی انجام می‌شد — به قتل رسانده یا به‌شدت مجروح کرده‌اند؛
از جمله خانواده‌های کشته‌شدگان حادثه ناو «یو‌اس‌اس کول» (USS Cole) و هزاران نفر دیگر که در میدان نبرد جان باخته‌اند. به‌علاوه، باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران طی ۵۰ سال گذشته به قتل رسانده نیز غرامت پرداخت شود، چه رسد به آن ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.
من به نمایندگان خود دستور داده‌ام که این موضوع را قاطعانه در تمامی مذاکرات آتی بگنجانند.
از توجه شما به این مسئله سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69855" target="_blank">📅 20:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69854">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwOtBr3puFJcdDv1Jlsq17tFEwaqu6gCqjuJTQ9mjHYnhLrXBvrJgt4SBSYXMtew3PeJFVfCmjTfX8Lish1prywn8uGw1Xky9L6p84P-MCH-2d0tPjlKobtBrSGj3AHRcPvRrSNCW311oDg-HX70nLcfTiw3L_BeGPo40Qz_K_3_FnnaZuiKwjPyLfgkb1eFkERkSBktcKYJ9Rmhpxtou72J_EUQHjh9GNd4PvSqJ1rblMVHc8DQiV85eAnHqF8zRoX2WXIuxqA9HQCY1q5Ae5lXD8SBhGkSD2pNXOZxQHU0foA0fZC8m8dJRc9RxbUQA_GDs4YjrRxU4mk4KAXJfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
مرندی:
‏ایران آگاه است که نیروهای رژیم ترامپ در کویت، امارات متحده عربی، قطر، عربستان سعودی، بحرین و اردن در حال بسیج برای یک حمله برق‌آسای بالقوه - احتمالاً در کنار نیروهای اسرائیلی - علیه مردم ایران هستند. جمهوری اسلامی با پاسخی سریع و کوبنده آماده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69854" target="_blank">📅 19:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69853">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🔴
🇮🇷
لیست فرماندهان جدیدی که مجتبی خامنه‌ای انتخاب کرد:
سرلشکر  علی عبداللهی به عنوان رئیس ستاد کل نیروهای مسلح
امیر کیومرث حیدری به عنوان جانشین رئیس ستاد کل نیروهای مسلح
سرلشکر احمد وحیدی به عنوان فرمانده سپاه
سرلشکر مصطفی ایزدی به عنوان جانشین فرمانده کل سپاه
حجت الاسلام طائب به عنوان رئیس سازمان بسیج مستضعفین
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69853" target="_blank">📅 19:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69852">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f1723f2a3.mp4?token=Yo4Di5oiiS34xbcVFjBFB3OtoIF2AICliaJW04YD8uO_sFZRUkVmOx9kh_5F5G72G0bUJbzCOP8CWEqLzKJl1kf6KcQ-hJRe2VvBE_e_0FnMRBvAht4I3s7Z3QRQrzNPmqRO8EQgchBqX9BchnVNNya_ASC7xPqnE-d0XAN3CiO5VOD1B6HJ-SU8ATLv52ONrjPYF_2j3LubKR8VEt7VdAKPiTXqw85Hknp9x9DSwGbXxgszEYAo8LN-M92UnnJan4g3pvq2rrTD52WGh8RuxUe7iIPIw6rPVmPLa-14VxEZOTesY9rZ5kJysF5cb2K4jyfHb5aKiHakFGzgYuxFyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f1723f2a3.mp4?token=Yo4Di5oiiS34xbcVFjBFB3OtoIF2AICliaJW04YD8uO_sFZRUkVmOx9kh_5F5G72G0bUJbzCOP8CWEqLzKJl1kf6KcQ-hJRe2VvBE_e_0FnMRBvAht4I3s7Z3QRQrzNPmqRO8EQgchBqX9BchnVNNya_ASC7xPqnE-d0XAN3CiO5VOD1B6HJ-SU8ATLv52ONrjPYF_2j3LubKR8VEt7VdAKPiTXqw85Hknp9x9DSwGbXxgszEYAo8LN-M92UnnJan4g3pvq2rrTD52WGh8RuxUe7iIPIw6rPVmPLa-14VxEZOTesY9rZ5kJysF5cb2K4jyfHb5aKiHakFGzgYuxFyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇫
طالبان به طور رسمی برده داری جنسی زنان رو قانونی اعلام کرد تا محدودیتی از این لحاظ نداشته باشن!
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69852" target="_blank">📅 19:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69851">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69851" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🙄
همه بت باز های حرفه ای دنبال
🔞
شکار این بونوس ها هستن
✅
لیگ های معتبر اروپایی شروع شده بهترین فرصت برای جبران ضرر های جام جهانی
💯</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69851" target="_blank">📅 19:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69850">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LqopCum3Idg2p378wiWGas9K1twfcmsuoJ5v_-H9qF-8_7S4v124axtW7ItncS9pukpWC3WCooKwpavRPEUjfSK_ecqAEg2i6wO3hyP3Eink2qlPnZtNwhqGaxd2m4n9EXeoPfGkpb94h0B6t4GoqsPNtAYm2faiOW2skEK6nDqzKR4ybpeH2SMPGccOQRN-fS81SYTT5ek_6p0vKKBREPazzV7_xDIUFUhLt6WxFop8Vj0jJ7BycpRDC_tW6P6ewXbTytmksQb_0G1l-J4x0RYwiB7ul89Ej5pO1KoCzmAc4j1Qzf3FTzAKYcr0O66BKkxSePPu7Y7P8FNiiFzfQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤔
شروع رسمی لیگ های اروپا
❄️
🆕
بهترین فرصت برای جبران ضرر های جام جهانی با جشنواره رویایی مرداد  ماه
⚠️
هر افزایش شارژ مساوی
2️⃣
1️⃣
🔣
شارژ بیشتر بدون محدودیت
☄️
به همراه
🤩
🤩
🔤
کش بک باخت همه روزه:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
g19
@betinjabet</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69850" target="_blank">📅 19:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69849">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
⭕️
مجتبی خامنه‌ای تا ساعاتی‌دیگر اسامی فرماندهان جدید نظامی را پس از بیش از ۵ ماه رسما اعلام‌ خواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69849" target="_blank">📅 18:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69848">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a2288e087.mp4?token=bsYH3-kDKbYNYql8QBIjn0sKjOyO6t3_W-gxJPmdrXodG0OdoB8m-H3Qdf4c7pubPg330iIQaO64LppzeZCujK5LHJb5dzagiw_gkBzjuEUV8Px3pZ0-Q78gZg81auQNTvIcOqi2LXMLEbohHjmfH1KpWDc0V4JDjzQ56zb2W6277CE3HXmJ7dj76aj4ESc7y_qC8K3jbSQF7qQ7z1F9yHdZhfqy0v4xQ_rTZwtrIHvKbrjzDGbaYLR0q578SdX4n5Seif0NiaLyLW-tbARsqqXtVtLQIL767azLZW7I46fuwWftAt1oMVZ8hxZ9b25bErZWPyrAgjCuuz45K6k7nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a2288e087.mp4?token=bsYH3-kDKbYNYql8QBIjn0sKjOyO6t3_W-gxJPmdrXodG0OdoB8m-H3Qdf4c7pubPg330iIQaO64LppzeZCujK5LHJb5dzagiw_gkBzjuEUV8Px3pZ0-Q78gZg81auQNTvIcOqi2LXMLEbohHjmfH1KpWDc0V4JDjzQ56zb2W6277CE3HXmJ7dj76aj4ESc7y_qC8K3jbSQF7qQ7z1F9yHdZhfqy0v4xQ_rTZwtrIHvKbrjzDGbaYLR0q578SdX4n5Seif0NiaLyLW-tbARsqqXtVtLQIL767azLZW7I46fuwWftAt1oMVZ8hxZ9b25bErZWPyrAgjCuuz45K6k7nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان درباره مجری و کارشناس‌های برنامه به وقت ایران:
این همه علم رو از کجا آوردید؟
چندتا جوون نشستن رو صندلی و درباره اقتصاد، سیاست، جامعه شناسی، کشاورزی و... نظر میدن.
از چهارتا جا یسری اطلاعات ناقص می‌گیرن و بعد درباره‌اش حرف میزنن و نسخه می‌پیچن و جامعه رو منحرف میکنن.
من 18سال تو دانشگاه درس خوندم و استاد تمامم، الان فقط اجازه دارم درباره یه گوشه قلب که تخصصمه نظر بدم نه کلِ قلب، اونوقت اینا...
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69848" target="_blank">📅 18:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69847">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7c4253089.mp4?token=rumk6m3yAHsFof4mBCYXeNz5kRqaFzph_tLuXBOEZJ9Nm0cmJtP3noybp7-H16Aw1Ado6rB37Q1x7E1quLfqDnb-WiWyknSsN-mzGKhrCUKHKqkrtohcyPcLQ7kastAaYKUlSPOSZoOtusfBosqpeZgdB16W6wATbLJIVmCR_eEGKa5njmiWLyOoTmfsQ3zNmfNaTwbCkmfuk2IWvmMrxKoRZKrp2BeIIhtxI4s3IGMzlqdOZL0WnRCA4Cg85fa8pnzBKiFBqymS3c5_Wae3jG5tdyDvH1JDakmLXwd18aOZst4Eo50NwSAQizsORtX30luCHoOIWVlRASj7IyLjHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7c4253089.mp4?token=rumk6m3yAHsFof4mBCYXeNz5kRqaFzph_tLuXBOEZJ9Nm0cmJtP3noybp7-H16Aw1Ado6rB37Q1x7E1quLfqDnb-WiWyknSsN-mzGKhrCUKHKqkrtohcyPcLQ7kastAaYKUlSPOSZoOtusfBosqpeZgdB16W6wATbLJIVmCR_eEGKa5njmiWLyOoTmfsQ3zNmfNaTwbCkmfuk2IWvmMrxKoRZKrp2BeIIhtxI4s3IGMzlqdOZL0WnRCA4Cg85fa8pnzBKiFBqymS3c5_Wae3jG5tdyDvH1JDakmLXwd18aOZst4Eo50NwSAQizsORtX30luCHoOIWVlRASj7IyLjHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
فیلد مارشال محسن رضایی (1392):
اگه آمریکا به ما حمله کنه ما همون هفته اول هزارتا آمریکایی رو اسیر‌ میکنیم و بعد در ازای آزادی هرکدوم چند میلیارد دلار از آمریکا پول میگیریم و اینطوری مشکلات اقتصادیمون هم حل میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69847" target="_blank">📅 17:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69846">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b47958b9.mp4?token=JeM49K50Uv_u1lmhLDVD8byfz_6tXAYNl29ZmKiY_9IB1OChGf6g60i4VKLXp9c9zra0o60unQ8MxqhjuojKVfxRiRbELIeS9kOYGI5yh0y3l2Ewgiv5NdBgJ4ekbJQodqU57JTSTVZgNryfLm9JVcrNs_PjZIGluEv6hfRfum_29W74gBVNr9Y1wWvP4M9M50ozc37xrqJB5ZidlrAYSwPE810akAGunVmFaOWVyfH62XAvB5KjwRewAcmj1DOCMDI7BSO31imUrUjUYThB9dPWinOOpHBLWu0bTX6aaqE8pAZXjFLbsHT12OiBnTJDt5Ka9GLqG5Aql4yMyzLHsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b47958b9.mp4?token=JeM49K50Uv_u1lmhLDVD8byfz_6tXAYNl29ZmKiY_9IB1OChGf6g60i4VKLXp9c9zra0o60unQ8MxqhjuojKVfxRiRbELIeS9kOYGI5yh0y3l2Ewgiv5NdBgJ4ekbJQodqU57JTSTVZgNryfLm9JVcrNs_PjZIGluEv6hfRfum_29W74gBVNr9Y1wWvP4M9M50ozc37xrqJB5ZidlrAYSwPE810akAGunVmFaOWVyfH62XAvB5KjwRewAcmj1DOCMDI7BSO31imUrUjUYThB9dPWinOOpHBLWu0bTX6aaqE8pAZXjFLbsHT12OiBnTJDt5Ka9GLqG5Aql4yMyzLHsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی سمه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69846" target="_blank">📅 16:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69845">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37165ac1ad.mp4?token=f-G2b8m52YntmHQywsOu2zMPf29D8Ey0JLl_U0b95z6TAAV_9uV_IDb4O0V49NpPuNDXmuRscy6aAuxWkK-YoTiHZN1mXfDv5frow9hbQ7jNBDQOKG3MDXrcNcMJ4r2tR2bFDbI7uT326n3GLuILcqYsbH2XwkB6LTULxpuOR5_9ln78idQduf6QEBdR2vOsvNJ9pE1Odn8kPHDv0rP7OX9VLJdV3e3B-xh_Sqw7LmFfbzUb9bvzPuTO4fXbTWXkoPGWNDS9cXD4nKqY-2bVzyM7RpfCiqAY3NpzNy0xshhjyQUpv4qUegnN93McqVRapV7sAETC-wLvMVJeTTzUHKdaiAbD82jRhFAJjrtv1FE6eYuN6PB1XXbCF13J20LxlX2cAHrnHa_rc5_P2wDIgVrIKITHPXDD9ixEEsPyDzZY8V8ZZNnHRPdgPQYPGnUJR84wZc3yzJ9WGt6bwkEaA4MZym9rIuEjqkDLGIanBGpaWcZ-CXblpZOqc0m2UmjHpT4a85xI4eOHpCnnTVUDXloRUpDwvzB6DtDL8ayvDlSe1TH-yszYTFY0hFJUbr9Sy0lJFcbJAggv3hDLsNCFC5mmVKLOPSUGIcCgKtPzIQVqc-S8mjWbCkWtz8traLvklGtro70KToEHPf7MrTBL9t0zmyR3P8cLstw3o_eWCZI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37165ac1ad.mp4?token=f-G2b8m52YntmHQywsOu2zMPf29D8Ey0JLl_U0b95z6TAAV_9uV_IDb4O0V49NpPuNDXmuRscy6aAuxWkK-YoTiHZN1mXfDv5frow9hbQ7jNBDQOKG3MDXrcNcMJ4r2tR2bFDbI7uT326n3GLuILcqYsbH2XwkB6LTULxpuOR5_9ln78idQduf6QEBdR2vOsvNJ9pE1Odn8kPHDv0rP7OX9VLJdV3e3B-xh_Sqw7LmFfbzUb9bvzPuTO4fXbTWXkoPGWNDS9cXD4nKqY-2bVzyM7RpfCiqAY3NpzNy0xshhjyQUpv4qUegnN93McqVRapV7sAETC-wLvMVJeTTzUHKdaiAbD82jRhFAJjrtv1FE6eYuN6PB1XXbCF13J20LxlX2cAHrnHa_rc5_P2wDIgVrIKITHPXDD9ixEEsPyDzZY8V8ZZNnHRPdgPQYPGnUJR84wZc3yzJ9WGt6bwkEaA4MZym9rIuEjqkDLGIanBGpaWcZ-CXblpZOqc0m2UmjHpT4a85xI4eOHpCnnTVUDXloRUpDwvzB6DtDL8ayvDlSe1TH-yszYTFY0hFJUbr9Sy0lJFcbJAggv3hDLsNCFC5mmVKLOPSUGIcCgKtPzIQVqc-S8mjWbCkWtz8traLvklGtro70KToEHPf7MrTBL9t0zmyR3P8cLstw3o_eWCZI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بقایی سخنگوی وزارت خارجه:
تنگه هرمز از زمان حضرت آدم تا ۹ اسفند برای همه باز بود
ادعای ساخت سلاح هسته‌ای ایران توسط نتانیاهو دروغی بیش نیست
به ترامپ بگم که ایرانیان شطرنج بازان حرفه‌ای در طول تاریخ بودن( ترامپ جنگ ایران رو به شطرنج تشبیه کرده بود)
هیچگونه مذاکره مستقیم با آمریکا نداریم
باز شدن تنگه هرمز منوط به لغو محاصره دریایی هستش
نگرانی بابت پیمان دفاعی مکه نداریم چون همسایگان ما هستن
بحث کنوانسیون دریای خزر به مجلس ختم شد و تصمیم نهایی با اونا هستش
درباره عمان نزدیک به یک تفاهم هستیم و به زودی نهایی میشه
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69845" target="_blank">📅 16:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69844">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c431777b9a.mp4?token=nzMfYXVn3tY6bkLPp8GQIcaPvhSMt-Wzo8GQ7b3I5bmiOoGvLg8cVyvFJGHOm9YlQ_j91sheqYe2gCz86qhJSYyeUNOrGxzSYXIsHpPXG0p4Npf4QiFSLhALQ_6G5kNDrkrjvwaSpSf4mXrpyRljXJ_cLZNYEqNfqRefqkiJ6-jNbmli9FGGQnLjHHTH-poTJVQHa66Z3uj6wySLCudRFLF2YZJwP584uduu_Dlx8_sqfpt0nYjZB8VGdSNXNExJDwqfj_SWrlgjh2MocMzzDxoto42Q2xZeQq_ipdxIKM6Zfu---KOUPjIRZOn1eJ7FxswouKaARqNyrqOY4JMBdTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c431777b9a.mp4?token=nzMfYXVn3tY6bkLPp8GQIcaPvhSMt-Wzo8GQ7b3I5bmiOoGvLg8cVyvFJGHOm9YlQ_j91sheqYe2gCz86qhJSYyeUNOrGxzSYXIsHpPXG0p4Npf4QiFSLhALQ_6G5kNDrkrjvwaSpSf4mXrpyRljXJ_cLZNYEqNfqRefqkiJ6-jNbmli9FGGQnLjHHTH-poTJVQHa66Z3uj6wySLCudRFLF2YZJwP584uduu_Dlx8_sqfpt0nYjZB8VGdSNXNExJDwqfj_SWrlgjh2MocMzzDxoto42Q2xZeQq_ipdxIKM6Zfu---KOUPjIRZOn1eJ7FxswouKaARqNyrqOY4JMBdTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
پزشکیان:
با رهبر هفت ساعت دیدار داشتم و درباره مسائل مهم کشور باهم گفتگو کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69844" target="_blank">📅 15:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69841">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QHM-YeCl-NBsLcdXNsIPZF_H2G98IspOd0rOFc7WBSYYmxtBt2GcOXvTG9DhZmQ7OZy-mIZB7A96P0Mtj5Kxk0CVxmGtDMNVRrLEfScv6UqPF55scyaY9zFVCkF0g8ryryovSqV_0xteg-dqWT92vlT8SWxUjVvoZC_ZeHW0Z4S0B1nVHoeOT_qDGO_gFCcwH9RgrzhElGm28tTSNcEHtgNiveVent4sQrbRZ8TssENq5i1Z57Q4vTYtKv8hiqjgdml6JuD5xpbuEhN2eUiCuhfexuem7ZfFEiE1HIvRBOm5dycpt9G4qV7hquvj4SthmOKKHJEC80MA7NlAWwib3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kPYMIg6LgDZfwXQMq5Ai5x3PgaTRJ_3JrWznVOjvpiXERqUAHTsDMyUmoahhA-msMJGvWmesqOzECU_f-3wyZRgicHAb-h0Ih3p6JkRPllgcuPWiIbbPktOu3scjf1ksMYdvvk1ZgsRNLcDzVtP6AFDXxenZIih7R_pEjRrpkXlngLPS7bIE_prx-OZdF9cmkHHDT1Hbue6l4tSmDEwKqndtfieLbah35fIMK2F9JQM0YR6N8MZMy37a3Ht0DuMAS9i31D3GfxyJfEWNIaFxi_I9leGEJ4bJDtp7bTmdEzPYpZwGejo9RYAyVGtSwXwaLZP7UrHj4pTdVSBZKpX6Pw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92217bf769.mp4?token=axdGPbWm7YrAIDXyd_I6i88WwnL_rOtU5zPgRi6NMT_Auq7Ihg_SBCnLjqxzCcjHlhrtvBlL5xUtzysW6c5BTN4-r2WftnS_X8TvdQDLazt1D9Nc9knAopIqJV3sJyD2LIONXlX5NtGu3NJ25GxC6zkfWNSKwWGYcOKUJv5RoRZeZKE9XZOvP3Az4E1LB6HI0sXXad2gJ-aZkRP2lgDHBaMxbcbJZnhxzvdUDzet2poUfImiQi0MNmtF4I5d2GgkkVamGF7bzXM2hn2CnjjHT9ir6VHPhj-kS5YbUmbviRM8yIaOAlZOenHes7cY6tAcMwUGzCELkr_Z_zMV7u76og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92217bf769.mp4?token=axdGPbWm7YrAIDXyd_I6i88WwnL_rOtU5zPgRi6NMT_Auq7Ihg_SBCnLjqxzCcjHlhrtvBlL5xUtzysW6c5BTN4-r2WftnS_X8TvdQDLazt1D9Nc9knAopIqJV3sJyD2LIONXlX5NtGu3NJ25GxC6zkfWNSKwWGYcOKUJv5RoRZeZKE9XZOvP3Az4E1LB6HI0sXXad2gJ-aZkRP2lgDHBaMxbcbJZnhxzvdUDzet2poUfImiQi0MNmtF4I5d2GgkkVamGF7bzXM2hn2CnjjHT9ir6VHPhj-kS5YbUmbviRM8yIaOAlZOenHes7cY6tAcMwUGzCELkr_Z_zMV7u76og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
دیروز عراقچی برای مهمانان خارجی تو ساختمون وزارت خارجه بساط تعزیه راه انداخت
😳
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69841" target="_blank">📅 15:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69840">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7709b161ed.mp4?token=OBYridYq50QoEMjtaDoWTHL4uG3f__ceFPqEcqGylZxERA_ZpwVt7SnPR3NjCQ7Zsix-rRR9DhL1K5TW5wipZQMf8CXmPnAF6f2Wm0LWnzi2wkrgn_QoXPUvGj3p7ehg8A-c26ooTMMRzDZYW9h2CjzAaEwVIYjNu_I0C4T1I7DbDBTTM_OzxZaIOrq3CeBfgS6e5cLR7F-JVULtfAGMKnFT2AzCo-rbdef03ADHr9aZ4HcsNkbmNZOYd3Kun2gH5ISTsoL-Gu0mCuKFAgzPiOZrQiOA9o5nQVlGpKPazar4HuiJ08ta7nuMtOJ1hptjNT0AXQ96uP-xlVRCV0mX8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7709b161ed.mp4?token=OBYridYq50QoEMjtaDoWTHL4uG3f__ceFPqEcqGylZxERA_ZpwVt7SnPR3NjCQ7Zsix-rRR9DhL1K5TW5wipZQMf8CXmPnAF6f2Wm0LWnzi2wkrgn_QoXPUvGj3p7ehg8A-c26ooTMMRzDZYW9h2CjzAaEwVIYjNu_I0C4T1I7DbDBTTM_OzxZaIOrq3CeBfgS6e5cLR7F-JVULtfAGMKnFT2AzCo-rbdef03ADHr9aZ4HcsNkbmNZOYd3Kun2gH5ISTsoL-Gu0mCuKFAgzPiOZrQiOA9o5nQVlGpKPazar4HuiJ08ta7nuMtOJ1hptjNT0AXQ96uP-xlVRCV0mX8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وایرال شده از قیمت یک پک آرایشی که ناقابل سه میلیارد
😳
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69840" target="_blank">📅 14:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69839">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lq5ybvLAUr1BTeukmcbK06MpW_gCixGCRPK8r3BoROLBfC_3EH95rkuIyQ1vHB3OlShjXwcbAEW-Z9bEEf4m29UBldW42b8RlK4B8jNGigVc8XRmwku1kX7KamP48Dt_rITilUK6ZB-yb_4bvznJaHKSHDl31Sy0A85EgXr1r2WnLwPN_nLeroafXrDqeJ4dcl9DchqY2jPMzVlZcfgcIaX7rDgISc5eFkvNtFD40DPj2XysRxB6lsh6vXUzrKT2l3hTJgncqNknI6TX6Jj1JA8j19ei1ykZh79naLvXmCW2Plz1pP38NhGeEOBXuxhbfO6d7xgsDjTAmLS_Os9p0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
باراک راوید:
یک مقام ارشد آمریکایی به من گفت که کاخ سفید از اظهارات نتانیاهو درباره طرح غزه «ناراحت نیست» و آن را بخشی از فضای انتخاباتی اسرائیل می‌داند.
این مقام آمریکایی گفت: «ما نیازهای سیاسی "بی‌بی" را درک می‌کنیم. تا زمانی که او به انجام آنچه ما می‌خواهیم ادامه دهد - به‌ویژه در خصوص مهار حملات به غزه - مشکلی با این موضوع نداریم.»
به گفته یک مقام آمریکایی، نتانیاهو هفته گذشته در تماسی تلفنی با جرد کوشنر، فرستاده رئیس‌جمهور ترامپ، وعده داد که علی‌رغم تردیدهایش، به این طرح ۱۵ ماده‌ای فرصت دهد و حملات به غزه را محدود کند تا روند خلع‌سلاح این منطقه بتواند آغاز شود.
از آن زمان تاکنون، اسرائیل حملاتی علیه غزه انجام نداده و ارتش اسرائیل (IDF) به‌تدریج در حال عقب‌نشینی به سمت «خط زرد» است. هم‌زمان، آمریکا و میانجی‌گران خواستار آن هستند که حماس روند خلع‌سلاح را آغاز کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69839" target="_blank">📅 14:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69837">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d242d991d.mp4?token=Xu6Gb2IKMsM6oXpfSLVwFdoHkFqyKw-Syf05pVWJPQSlRdzdOrxinSztj2UdMemiWlmigO2NktVpF1vPvrKqAX_2GM79tafhDV8bVcOYWJU1-EzE6u8SYnPZO6HSPftMh6FQ-ZKqZYglxuvH8h71PDIOkWvMWZodD2qq7GSY0bEvX1QM55JGecgf0XdA0V9bkcVw4H3QuGPJxqp9U-4v5XLGwoPGp_N7n96hzhzBQu15te5P7DAQZT2rwgD_DT0CzQhCD49EYcCYEJ0fRgMVVTNL3MzzUTqY3oCnGQjeGhozsbhfmY-9Rcp20-AUrT0DKaKDGuNrvqQF28EC1WJcjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d242d991d.mp4?token=Xu6Gb2IKMsM6oXpfSLVwFdoHkFqyKw-Syf05pVWJPQSlRdzdOrxinSztj2UdMemiWlmigO2NktVpF1vPvrKqAX_2GM79tafhDV8bVcOYWJU1-EzE6u8SYnPZO6HSPftMh6FQ-ZKqZYglxuvH8h71PDIOkWvMWZodD2qq7GSY0bEvX1QM55JGecgf0XdA0V9bkcVw4H3QuGPJxqp9U-4v5XLGwoPGp_N7n96hzhzBQu15te5P7DAQZT2rwgD_DT0CzQhCD49EYcCYEJ0fRgMVVTNL3MzzUTqY3oCnGQjeGhozsbhfmY-9Rcp20-AUrT0DKaKDGuNrvqQF28EC1WJcjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فوران یک آتشفشان قدرتمند در جنوب غربی کلمبیا
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69837" target="_blank">📅 13:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69836">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81027c9c4b.mp4?token=otmPu892PK76PWzdFAbSO_H0QLisAFSl7NgxkMbvesNk_nAi4SlOtwgeYw0W6DYn8dxwtG8hqz_3zuO-0F8pnXklOWKpp1FCPKdqXKhadfalmMJ9UYUF9_zkv9RRP_NKjYMp4DP5xcAcUxIYXzGL7Byfltem1uIfrhQT4ClxYh_5hgBiN-U-JY5Ku0ZyMPtSR1WvXTsdIW4LoUFGU_OskLJhNm7TnnyPZU7lxIE5mZ7NPqjB3DiX7nTJYsruvAc_qSIbfQIsykagPrGLj0whVE7zGgPv7jiAaqkfUSLiNcuink064EqKq707Hlf61xLl6MIxaE5HyvgfoZNq9gXthQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81027c9c4b.mp4?token=otmPu892PK76PWzdFAbSO_H0QLisAFSl7NgxkMbvesNk_nAi4SlOtwgeYw0W6DYn8dxwtG8hqz_3zuO-0F8pnXklOWKpp1FCPKdqXKhadfalmMJ9UYUF9_zkv9RRP_NKjYMp4DP5xcAcUxIYXzGL7Byfltem1uIfrhQT4ClxYh_5hgBiN-U-JY5Ku0ZyMPtSR1WvXTsdIW4LoUFGU_OskLJhNm7TnnyPZU7lxIE5mZ7NPqjB3DiX7nTJYsruvAc_qSIbfQIsykagPrGLj0whVE7zGgPv7jiAaqkfUSLiNcuink064EqKq707Hlf61xLl6MIxaE5HyvgfoZNq9gXthQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشتیبانی سنگین و فوق العاده از نیروهای زمینی آمریکا در جنگ افغانستان ( طالبان ) توسط بالگرد آپاچی ۶۴ با توپ ۳۰ میلی متری M230 Chain Gun
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69836" target="_blank">📅 12:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69835">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ea33d827b.mp4?token=feCqFwl13mdWDWmzK9bijy0CTk6xia3ps-rpvK9TBdhj0l3rDM-6AXX0glflZ74WAjHURWF7w7u3JFbHQZdOhUwD3YfkB3aDMS2ljVDbtGk5mylIdO7d4u6WFGddnru9BhUSYb_OGXKhcTV3Ep6BTkQGx257vwnQ4Z34opHf6n3AcJv6QeFCVHrNFUCzZrIt5BaY__RIuWpWgcYmXQTWft3Er5FDJrISbEbQFQVgs44ZEgEu4PF8viVaoTXJbfvwzlC4-WchotjxGCNOf9dVqRaBUbiTfjAdRdBy4Etu2KzOuyIDKzq3N4d0zmKH6h3k7E8l0Qym6C6tC3HWXk4DvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ea33d827b.mp4?token=feCqFwl13mdWDWmzK9bijy0CTk6xia3ps-rpvK9TBdhj0l3rDM-6AXX0glflZ74WAjHURWF7w7u3JFbHQZdOhUwD3YfkB3aDMS2ljVDbtGk5mylIdO7d4u6WFGddnru9BhUSYb_OGXKhcTV3Ep6BTkQGx257vwnQ4Z34opHf6n3AcJv6QeFCVHrNFUCzZrIt5BaY__RIuWpWgcYmXQTWft3Er5FDJrISbEbQFQVgs44ZEgEu4PF8viVaoTXJbfvwzlC4-WchotjxGCNOf9dVqRaBUbiTfjAdRdBy4Etu2KzOuyIDKzq3N4d0zmKH6h3k7E8l0Qym6C6tC3HWXk4DvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پرستار از اتفاق عجیب شب زفاف یه زوج میگه:
ساعت ۴ صبح یه خانم با خون‌ریزی شدید به اورژانس منتقل شد و اول فکر کردیم
سقط جنین
اتفاق افتاده، اما بعد مشخص شد مربوط به
شب زفاف
بوده.
خون‌ریزی اون‌قدر شدید بوده که مجبور شدن بیمار رو
جراحی
کنن.
⏺
پرستار توصیه کرده زوج‌ها برای اولین رابطه عجله نکنن و با آرامش و احتیاط پیش برن تا به این روز نیافتن
.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69835" target="_blank">📅 11:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69834">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53aa49426e.mp4?token=IhxVeGhyd-S4QUJC8C9O7kR4ohTneK5crpJMg1DcI_cHb6YOOM1kVvfWkIHmi9Yqc1cG-0_cE_TYJASr-WOW1scvRh5elSQ1wTFNiYeJCw6k57WX60l5bjCFZ-iZUUgASIPiCP0qGoWXmcKCTsIyN_FQy9i2dbSLw50R-7rzAz2pPWH2vpElzPHDhUa5LujEnJeO3gtLaxnS4uwrGLz1-S6BIM8otyW-KEj1ZOEK0JuPxiUpro8WvZrV3IkhAiB1UueykrIcdwFVdALa483AA3towQ6PSBNUMEKg9g01TLvjR4BoEuwuJT9q_C3tkg3Z2dv07vfSRV6LEKrXyuPB2mByrEss7-a6OzyJsCP5VpPgslNs4gez55J9GbykT9oHtXRGBOlOmQfL0jq13OEB0mT2K4q5E2ymZor_LhA8IUWLi-e7B6i2lDu1y08Syawci7ljzTuDE_POBQrOjAJOhTn3r9r34df6dj59pDCGoyhEvn3Kypz56ynBa8DN3sRtLxWOJCRLQ7mVk19iyCiVggFsZyTFpOFb0v7yKDlCFtUOXdqwrOEuz28vV29unY45u7x-bHpBrYLw8dnORQKPh9ktLkJ5ZYfhkOC_APKVmLyVwia0MTtghcsGA_54eTDM21ExFClJyU70up64kqgHJgi4W1FsmTCGadVzuBAaTa0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53aa49426e.mp4?token=IhxVeGhyd-S4QUJC8C9O7kR4ohTneK5crpJMg1DcI_cHb6YOOM1kVvfWkIHmi9Yqc1cG-0_cE_TYJASr-WOW1scvRh5elSQ1wTFNiYeJCw6k57WX60l5bjCFZ-iZUUgASIPiCP0qGoWXmcKCTsIyN_FQy9i2dbSLw50R-7rzAz2pPWH2vpElzPHDhUa5LujEnJeO3gtLaxnS4uwrGLz1-S6BIM8otyW-KEj1ZOEK0JuPxiUpro8WvZrV3IkhAiB1UueykrIcdwFVdALa483AA3towQ6PSBNUMEKg9g01TLvjR4BoEuwuJT9q_C3tkg3Z2dv07vfSRV6LEKrXyuPB2mByrEss7-a6OzyJsCP5VpPgslNs4gez55J9GbykT9oHtXRGBOlOmQfL0jq13OEB0mT2K4q5E2ymZor_LhA8IUWLi-e7B6i2lDu1y08Syawci7ljzTuDE_POBQrOjAJOhTn3r9r34df6dj59pDCGoyhEvn3Kypz56ynBa8DN3sRtLxWOJCRLQ7mVk19iyCiVggFsZyTFpOFb0v7yKDlCFtUOXdqwrOEuz28vV29unY45u7x-bHpBrYLw8dnORQKPh9ktLkJ5ZYfhkOC_APKVmLyVwia0MTtghcsGA_54eTDM21ExFClJyU70up64kqgHJgi4W1FsmTCGadVzuBAaTa0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایشون هم اینطوری انتقام قتل حمیدرضا رجب‌زاده رو گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69834" target="_blank">📅 11:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69833">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48e95fc990.mp4?token=h67AL8xPZ00R0nDnf_E7yafhibPqQz89OefAeb7Z1RU8Ps9wTBH26VKd355GapEPaUzRtiZq-xaJk1TXg2_qj88xm9pqP6me7p0Bs1drtiMNavrJV267pBroZGsy6UKrJhXPjsIvsDTbCgt41QsE6JJrs8KsmDsA7A19K0hriVB705t77ge92kWCgWpsj0l0gya5eQnWSr4-xhCGJpPvSswoPBglhi-BdJjEV3OhH_EOuiYrl_IZT2GoQUBtWV4H5nJS8cveMk7e9P0JwAlmzgdYaKr3C0pADjM8ukaWV7O4oit7MwdgE0w9gtYbWnIkOJPhokakYIfMvl4drzDNvg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48e95fc990.mp4?token=h67AL8xPZ00R0nDnf_E7yafhibPqQz89OefAeb7Z1RU8Ps9wTBH26VKd355GapEPaUzRtiZq-xaJk1TXg2_qj88xm9pqP6me7p0Bs1drtiMNavrJV267pBroZGsy6UKrJhXPjsIvsDTbCgt41QsE6JJrs8KsmDsA7A19K0hriVB705t77ge92kWCgWpsj0l0gya5eQnWSr4-xhCGJpPvSswoPBglhi-BdJjEV3OhH_EOuiYrl_IZT2GoQUBtWV4H5nJS8cveMk7e9P0JwAlmzgdYaKr3C0pADjM8ukaWV7O4oit7MwdgE0w9gtYbWnIkOJPhokakYIfMvl4drzDNvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دریک، از بزرگترین خواننده‌های دنیا؛
با 140 میلیون فالور و ثروت 250 میلیون دلاری [50 هزار میلیاردی]
وقتی ممه‌های بزرگ یه دخترو دید، نتونست تحمل کنه و براش هاپ هاپ کرد
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69833" target="_blank">📅 11:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69831">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6d3c25ee1.mp4?token=rwp-p2IIcfE2jayZTBoIAfWvY_WmZJ87GJmcUt3FGelkyOQCwhp2N2kw17AsBH81Cs3Ewmora7kajx375jAeYtXusa7oUtLphxr_pYkLNsROtBVSHtW_KPcztadKcwvivVLjCtRhuwGRl9lMoMQHgGCTjnm_7pflJKJpuo_9oiOvZ-DNPPXplNtzXXrtDBHPe-OuOLG83adkdYqtkBiynIt5AKbOMYelpt8_njAbwEjnkF8R8_4YwcanKLSZ4yEV_V8hh1QKbG3rK_hMmauMOvoYgqif9a8XBeX2I84ymuS_L1cMSv8ukZQGL66XtGwXPpBXVWYzlAXB-9G-1zTBdg9WKgCZhy7AEZ1TB1_BNC7TXwAtbpsC3AkKW29-d-3Szm_Voc_v7kmdpPOzlSwhVPTNPBH5y0JTB8-aZ-led7PSJoulmQD0z-CM7T-nkMJ7nxIOsSCE26hSA_U9QR0dYgPXBXvViT0LGU5x8Uzk5ehB_6Icx3CPLK3q6iBKFp-UMyEJ3UQaBFEyJitjkCWUUzqHzbN2QoC-7pWAPL9utWOBieAKbYlUkpEkLqDYoacZjLkHxZ0EjgFB4UebxYUmvo_hgnHqbt7YdIqW1mA6ko1otN0DDtn1pJu2POXxFoPKg62FnPEFFH0ngrfx9rgT5wIzcftM5KBUg-st2hfgTRs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6d3c25ee1.mp4?token=rwp-p2IIcfE2jayZTBoIAfWvY_WmZJ87GJmcUt3FGelkyOQCwhp2N2kw17AsBH81Cs3Ewmora7kajx375jAeYtXusa7oUtLphxr_pYkLNsROtBVSHtW_KPcztadKcwvivVLjCtRhuwGRl9lMoMQHgGCTjnm_7pflJKJpuo_9oiOvZ-DNPPXplNtzXXrtDBHPe-OuOLG83adkdYqtkBiynIt5AKbOMYelpt8_njAbwEjnkF8R8_4YwcanKLSZ4yEV_V8hh1QKbG3rK_hMmauMOvoYgqif9a8XBeX2I84ymuS_L1cMSv8ukZQGL66XtGwXPpBXVWYzlAXB-9G-1zTBdg9WKgCZhy7AEZ1TB1_BNC7TXwAtbpsC3AkKW29-d-3Szm_Voc_v7kmdpPOzlSwhVPTNPBH5y0JTB8-aZ-led7PSJoulmQD0z-CM7T-nkMJ7nxIOsSCE26hSA_U9QR0dYgPXBXvViT0LGU5x8Uzk5ehB_6Icx3CPLK3q6iBKFp-UMyEJ3UQaBFEyJitjkCWUUzqHzbN2QoC-7pWAPL9utWOBieAKbYlUkpEkLqDYoacZjLkHxZ0EjgFB4UebxYUmvo_hgnHqbt7YdIqW1mA6ko1otN0DDtn1pJu2POXxFoPKg62FnPEFFH0ngrfx9rgT5wIzcftM5KBUg-st2hfgTRs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی شبانه به مجموعه‌ای از اهداف در سراسر روسیه و سرزمین‌های اشغالی حمله کردند.
پهپادها مرکز خرید گالاکتیکا در ماکی‌یوکا، که قبلاً مرکز منطقه‌ای بود و در سال ۲۰۱۴ توسط نیروهای روسی تصرف شده بود، را به آتش کشیدند.
آنها همچنین پالایشگاه نفت در نیژنکامسک، تاتارستان را هدف قرار دادند، در حالی که روسیه ادعا کرد ۱۵ پهپاد در نزدیکی مسکو سرنگون شده و عملیات فرودگاه را مختل کرده است.
طبق گزارش‌ها، حملات پهپادی باعث قطع گسترده برق در ملیتوپول، بردیانسک و دونتسک شده است، در حالی که انفجارها و آتش‌سوزی‌هایی در سواستوپول و کرچ گزارش شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69831" target="_blank">📅 10:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69830">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69830" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#پیشنهاد_ویژه
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید بازی ساده و بسیار شیرینی که راحت میشه میشه ازش کلی پول درآورد
👌🏼
دنیای سرگرمی و بازی های جذاب رو در این‌اپلیکیشن تجربه کنید
⭐</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/69830" target="_blank">📅 10:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69829">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=HB_NBIbCBjk0WtIy-bCpIGlSi7J18fsY-L2S5yAJaE-xHA2GFD0To3ByvXIKLYu6_KnTwhjCGFcXuXsMC6s69kFWk1J_syvMWELlAOvOOZ5KjBhdmDUjEC8tejvYrp-16nqgtqWEhkEEKG68mscK7rraXteQ5mpWkc-dElGhsC8vW351l3MoiCbSELhvlwjomKaFlAdMVm4Wt72_hvaW75c5iEIx1xt6k1zc4BBGdycNxXzmwz593IRzH05UCi2Ns8kh_s9AcyDuPHdv08NElR-y2t04hug8UC2l5enUDAMLLM9th_bew1P6C69Rv4b-FaBy4084RxCqvmpE3deR4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=HB_NBIbCBjk0WtIy-bCpIGlSi7J18fsY-L2S5yAJaE-xHA2GFD0To3ByvXIKLYu6_KnTwhjCGFcXuXsMC6s69kFWk1J_syvMWELlAOvOOZ5KjBhdmDUjEC8tejvYrp-16nqgtqWEhkEEKG68mscK7rraXteQ5mpWkc-dElGhsC8vW351l3MoiCbSELhvlwjomKaFlAdMVm4Wt72_hvaW75c5iEIx1xt6k1zc4BBGdycNxXzmwz593IRzH05UCi2Ns8kh_s9AcyDuPHdv08NElR-y2t04hug8UC2l5enUDAMLLM9th_bew1P6C69Rv4b-FaBy4084RxCqvmpE3deR4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖱
به راحتی کسب درامد کن
💵
💰
🟢
ویدیو
#آموزش
بازی chicky choice رو براتون گذاشتم خیلی راحت و بدون ریسک و میتونی بازی کنی و کلی پول دربیاری
🔥
💖
حتما ویدیو رو تا انتها ببینید
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
r19
@betinjabet</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/69829" target="_blank">📅 10:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69827">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAcc5n_k2v4_hLu9ZGmdY91VMWp-hIYVGjumO7pSyg9OcjAvXh2Zu7SOjEqP1PqO6efDzQzbLS--PtmFHrYFSbnv5UUsrqY3X65WIa5Wr0R_ismwqyXK-N6zSHWXfM5O7golGy1Hi4hgL0e_LmHaFe_wsrBcdXHNHSISGOnXxY9WN3zZl4HzMicDfqMF_W6QKBuwkiGeT-tARv7L8gEeqx1xAY1e0kedNgnhKiYPxVc7GjLxxburBw-G0BUfNNLbU0KzRnNNz4EfKja_kDMrpZkbnE2P_obeoWMes_6XsaEvwWtszTM8LLDuLMwbrFqrk2X8e1bY5XOvRtXHH5rVQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
شرکت آمریکایی BlackSea از پرتاب یک پهپاد FPV از روی قایق بدون‌سرنشین GARC خود رونمایی کرد
؛
این شرکت اعلام کرده است که با استفاده از تجربیات به‌دست‌آمده از جنگ، استفاده از پهپادهای FPV هدایت‌شونده با فیبر نوری را پیشنهاد می‌کند.
محفظه‌های پرتاب این سامانه قادر به حمل پهپادهای FPV در اندازه‌های ۵، ۷ و ۱۰ اینچی هستند؛ پهپادهایی که از نمونه‌های FPV مورد استفاده فعلی روسیه و اوکراین کوچک‌ترند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69827" target="_blank">📅 10:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69826">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4c36a2172.mp4?token=oLqR0tFiyYmJOYnKU-EOclPM4CYQgzK928pJo_hnyx7pzGSrqthHMxIHnNdT20bSiX_uxoTAdqmuOnsldyCXIalA_c-xCqOK8brcGUXGSdW67K7U4fgBnlqOMWrm35c8pP5dAx9QNYipk5LXYk3WKj7QeS3QJMDrwMy7eoyQJ7KL25v-h5kJav6q8EcoGafgsYRhGsqwp9jhVOI_nujDOZKqQlC6KPqMorpRZMvMPOpJddUd0e_lkP0xQvpUqdD-CPMPTbyMKLlRu5fzkZT7DIF8jYBWPonRAXbxIWBHN7YCDkb1LJC0VPHbHmk0BAnaB9a4h83ghnWJlze_coOlaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4c36a2172.mp4?token=oLqR0tFiyYmJOYnKU-EOclPM4CYQgzK928pJo_hnyx7pzGSrqthHMxIHnNdT20bSiX_uxoTAdqmuOnsldyCXIalA_c-xCqOK8brcGUXGSdW67K7U4fgBnlqOMWrm35c8pP5dAx9QNYipk5LXYk3WKj7QeS3QJMDrwMy7eoyQJ7KL25v-h5kJav6q8EcoGafgsYRhGsqwp9jhVOI_nujDOZKqQlC6KPqMorpRZMvMPOpJddUd0e_lkP0xQvpUqdD-CPMPTbyMKLlRu5fzkZT7DIF8jYBWPonRAXbxIWBHN7YCDkb1LJC0VPHbHmk0BAnaB9a4h83ghnWJlze_coOlaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
جهانگیر، سخنگوی قوه قضائیه:
آخوند خرازی، بابت صحبتاش تحت تعقیب قرار گرفته و به دادگاه ویژه روحانیت احضار شده.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69826" target="_blank">📅 10:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69825">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🟡
📰
مراد ویسی تحلیلگر ارشد اینترنشنال: «جنگ بزرگ در خاورمیانه، برای سرنگونی جمهوری اسلامی است.»
⏺
پرسش این نیست که کدام زودتر می‌رسد؛ پاسخ روشن است:
جمهوری اسلامی سرنگون شود، مردم ایران به یک حکومت عادی می‌رسند.
جمهوری اسلامی سرنگون شود، نیابتی‌ها خشک می‌شوند.
صدام رفت، یک کانون تهدید در خلیج فارس از بین رفت — کانون دوم هنوز باقی است.
خلیج فارس می‌شود منطقه‌ی صلح، ثبات و توسعه؛ چون امارات، قطر و عربستان دنبال توسعه‌اند و ما هم دنبال جبران خرابی‌های جمهوری اسلامی.
ثبات منطقه از تهران آغاز می‌شود، نه از میز مذاکره.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69825" target="_blank">📅 09:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69824">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bdd241cc6.mp4?token=AjVLiG2oJJ29DuV5f_Gq25Z8idI-lIToNCNrmNDGe3IBP3cyerA8U8JkHmuIxQxf7fx7sFXuW5n_LjXpYu-bN5e2_ygn4GNN0FIerZp3BCyj3a5G3tO35AGajo3HYW5Y5jlzCIURi_d2CXUHOFGrS-IBUP0PG8xxoGB2NdDnmCy26DidBv6gEKzXi3ZwHowETaWKfWaobj7t322zWSY0APW8L3E5xXNnthOGUA79xRAttpAPmJqA4QYfORqSRGHpPXY3yT9xlr2HTMulTzULvwwCy9XoNrijoKn4i7TPGg0Oz0Tpxz4X0QJZzbKXz9C-RPTgtZegyJndFcZEhKBOZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bdd241cc6.mp4?token=AjVLiG2oJJ29DuV5f_Gq25Z8idI-lIToNCNrmNDGe3IBP3cyerA8U8JkHmuIxQxf7fx7sFXuW5n_LjXpYu-bN5e2_ygn4GNN0FIerZp3BCyj3a5G3tO35AGajo3HYW5Y5jlzCIURi_d2CXUHOFGrS-IBUP0PG8xxoGB2NdDnmCy26DidBv6gEKzXi3ZwHowETaWKfWaobj7t322zWSY0APW8L3E5xXNnthOGUA79xRAttpAPmJqA4QYfORqSRGHpPXY3yT9xlr2HTMulTzULvwwCy9XoNrijoKn4i7TPGg0Oz0Tpxz4X0QJZzbKXz9C-RPTgtZegyJndFcZEhKBOZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یکی از نفس‌گیرترین ویدیو های منتشر شده از جنگ؛لحظه بمباران شریعتی تهران!
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69824" target="_blank">📅 09:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69823">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69823" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#بازی_پولساز
⚠️
🔥
بلک کارت جدید ترین بازی معروف جهانی هست که فقط کافیه یکمی باهوش باشی تا حریفات رو شکست بدی
👌🏼</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69823" target="_blank">📅 02:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69822">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f6c003ee1.mp4?token=UEwT5o8BaUSEMXNcUuOMTEovWCN7D8-Qku0KpMrYCKg4SfKeEnMXzKuj2T0acPvO4nG-_bWwzUlhLijoR57v0Y_6FrsiUUQAIwfwNgPfC9yrJOKgeU6mgeL-ROOR5X24TuiCk6E2sK3FO_SMlD8EyNsHuOSESc-FRfxXyfAVWgu7QP8FecJNGxFsSfXfA-wTi3WA0djIt8AzXs5QGp-NhNYVK4wnqFIPXdtOItUyPAaSLzvGmen6_zsF6seYueCSo8mIMMqUgb0p_7F9mOR4lORkSa-uTvZ17PGhwxX1R3X3LobkB6gcosfhfiNC3qCWVLsP4N7qaL5E6Ydrp69R24i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f6c003ee1.mp4?token=UEwT5o8BaUSEMXNcUuOMTEovWCN7D8-Qku0KpMrYCKg4SfKeEnMXzKuj2T0acPvO4nG-_bWwzUlhLijoR57v0Y_6FrsiUUQAIwfwNgPfC9yrJOKgeU6mgeL-ROOR5X24TuiCk6E2sK3FO_SMlD8EyNsHuOSESc-FRfxXyfAVWgu7QP8FecJNGxFsSfXfA-wTi3WA0djIt8AzXs5QGp-NhNYVK4wnqFIPXdtOItUyPAaSLzvGmen6_zsF6seYueCSo8mIMMqUgb0p_7F9mOR4lORkSa-uTvZ17PGhwxX1R3X3LobkB6gcosfhfiNC3qCWVLsP4N7qaL5E6Ydrp69R24i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😯
اگر هوشت بالاست
🗼
:
❌
👍
این ‌ویدیو‌ آموزشی رو‌ ببین و با ‌استفاده از هوش بالایی که داری پول در بیار.
🟢
بازی خیلی حرفه ای و‌
#پولساز
رو‌ از این ویدیو یاد بگیر
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
a18
@betinjabet</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69822" target="_blank">📅 02:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69821">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:  اگه ایران از این به بعد به هر کشتی‌ ای توی تنگه هرمز شلیک کنه، فرقی هم نداره با موشک، پهپاد، راکت یا هر سلاح دیگه‌ای باشه، آمریکا در جوابش یه پل یا نیروگاه برق ایران رو میزنه حتی اگه نزدیک تهران یا داخل خود تهران باشه.  @News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69821" target="_blank">📅 01:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69819">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clbflWBGfllCB--Npe4Fqe_XgK72Qix-i5ZpTR3O1po6K--RWg4BJqfov_pY-AJHt2EoTdnW3p0KcLMezRq6Ol1_Ao4SyDCkV8mv0c2v467omn8mRaX-_3BDvWP_w_Xf0uPwO1_07P11WJHcMBebwX8q0GHtQh7_9L9h06Hd4rLaRZM7oCzM208ffXJpB0DFQTiQCrdtEamxbvbn5HFybJTSIAGefgEtpbJlAJXsZfd-fuOz_nCO6g0dSrTdb7NC4wsC4UkQ0APagExfJ6grIPkNc0_mIn8YiwYFBdcgQEZzUcUQcKkm-0VuiNrXfZvjIufh7mN9vQqxSmatcu71qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94eb35c039.mp4?token=fpwX8JuNd5UowW5Nnf8mJAJMFi0_Q9bcdKqlBgOfHGSJA5MMnigDHbid_kTryfS_JB9soIKcUmHF0GzRu_j4zyqOK7xT-l9jOI_ti0_gNuK6Z9026Po4QzCHZD1OyfG2hwzs5uRB9e78Xup-rEgMXOtwbcGtXhD94DyY8kCA5wolboweDPPmmP8k3DLsVAkb3TXdG6HY1G-S0qRt4YyJQoo3v3nc6R_8K_nAWXwpOBd-t24QLhwiilyH5loaowyfF_ZuQ9Hj1T4Gf54NHVkw-Mo5GzRarAC2EUlYYWvaUf6cCTe76qO-o9KSG4ZhJ_CBMLvDGk7uai-9OgOjkV3H3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94eb35c039.mp4?token=fpwX8JuNd5UowW5Nnf8mJAJMFi0_Q9bcdKqlBgOfHGSJA5MMnigDHbid_kTryfS_JB9soIKcUmHF0GzRu_j4zyqOK7xT-l9jOI_ti0_gNuK6Z9026Po4QzCHZD1OyfG2hwzs5uRB9e78Xup-rEgMXOtwbcGtXhD94DyY8kCA5wolboweDPPmmP8k3DLsVAkb3TXdG6HY1G-S0qRt4YyJQoo3v3nc6R_8K_nAWXwpOBd-t24QLhwiilyH5loaowyfF_ZuQ9Hj1T4Gf54NHVkw-Mo5GzRarAC2EUlYYWvaUf6cCTe76qO-o9KSG4ZhJ_CBMLvDGk7uai-9OgOjkV3H3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇨🇳
🇸🇦
یک پهباد ساخت چین متعلق به نیروی هوایی عربستان سعودی در آسمان جنوب کشور سرنگون شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69819" target="_blank">📅 01:11 · 19 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
